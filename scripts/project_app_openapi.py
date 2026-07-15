#!/usr/bin/env python3
"""Derive the mobile OpenAPI contract from the complete backend snapshot.

``docs/openapi.json`` remains the authoritative record of every backend
operation.  This projector selects active app operations (plus explicitly
declared mobile consumers of another audience) and retains only components
reachable from those operations or named directly by checked-in app code.

The output is generated evidence, never a second hand-maintained contract.
Use ``--check`` in CI to prove it still matches the full snapshot, operation
policy, and mobile caller discovery.

Component roots include both selected operation references and component names
used directly by checked-in app aliases, mocks, and fixtures.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import deque
from pathlib import Path
from typing import Any, Iterable

from api_contract_audit import (
    HTTP_METHODS,
    OPENAPI_SNAPSHOT,
    POLICY_PATH,
    Consumer,
    OperationKey,
    audit,
    discover_mobile_consumers,
)


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
APP_SNAPSHOT = WORKSPACE_ROOT / "docs" / "openapi.app.json"
APP_ROOT = WORKSPACE_ROOT / "travel-app"
PRODUCT_CONSUMER_KINDS = frozenset({"app_source", "app_direct", "app_url"})
SCHEMA_REFERENCE_RE = re.compile(
    r"components\s*\[\s*['\"]schemas['\"]\s*\]"
    r"\s*\[\s*['\"]([^'\"]+)['\"]\s*\]"
)


class ProjectionError(ValueError):
    """The source contract cannot produce a complete app projection."""


def _without_comments(source: str) -> str:
    """Remove TypeScript comments without treating URL strings as comments."""
    out: list[str] = []
    index = 0
    quote: str | None = None
    while index < len(source):
        char = source[index]
        if quote:
            out.append(char)
            if char == "\\" and index + 1 < len(source):
                index += 1
                out.append(source[index])
            elif char == quote:
                quote = None
            index += 1
            continue
        if char in {"'", '"', "`"}:
            quote = char
            out.append(char)
            index += 1
            continue
        if source[index : index + 2] == "//":
            newline = source.find("\n", index + 2)
            index = len(source) if newline < 0 else newline
            continue
        if source[index : index + 2] == "/*":
            close = source.find("*/", index + 2)
            index = len(source) if close < 0 else close + 2
            continue
        out.append(char)
        index += 1
    return "".join(out)


def _operation_keys(spec: dict[str, Any]) -> dict[tuple[str, str], OperationKey]:
    operations: dict[tuple[str, str], OperationKey] = {}
    for route, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method in path_item:
            upper = method.upper()
            if upper in HTTP_METHODS:
                key = OperationKey(upper, route)
                operations[key.normalized] = key
    return operations


def select_app_operations(
    spec: dict[str, Any],
    policy: dict[str, Any],
    mobile_consumers: dict[tuple[str, str], set[Consumer]],
) -> set[OperationKey]:
    """Return active operations that form the mobile-facing contract."""
    defaults = policy.get("defaults", {})
    overrides = policy.get("operations", {})
    selected: set[OperationKey] = set()

    for normalized, key in _operation_keys(spec).items():
        override = overrides.get(key.registry_key, {})
        effective = {**defaults, **override}
        if effective.get("lifecycle") != "active":
            continue

        discovered_product = any(
            consumer.is_product for consumer in mobile_consumers.get(normalized, set())
        )
        declared_product = any(
            isinstance(consumer, dict)
            and consumer.get("kind") in PRODUCT_CONSUMER_KINDS
            for consumer in override.get("consumers", [])
        )
        if effective.get("audience") == "app" or discovered_product or declared_product:
            selected.add(key)

    return selected


def discover_mobile_schema_consumers(app_root: Path = APP_ROOT) -> set[str]:
    """Find component schemas named directly by checked-in mobile code."""
    schemas: set[str] = set()
    if not app_root.exists():
        return schemas
    for path in app_root.rglob("*"):
        if path.suffix not in {".ts", ".tsx"}:
            continue
        if "node_modules" in path.parts or path.name == "schema.gen.ts":
            continue
        source = path.read_text(encoding="utf-8", errors="ignore")
        schemas.update(SCHEMA_REFERENCE_RE.findall(_without_comments(source)))
    return schemas


def _walk_refs(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            yield ref
        for child in value.values():
            yield from _walk_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_refs(child)


def _component_key(ref: str) -> tuple[str, str]:
    prefix = "#/components/"
    if not ref.startswith(prefix):
        raise ProjectionError(f"app contract contains unsupported external ref: {ref}")
    parts = ref[len(prefix) :].split("/")
    if len(parts) != 2:
        raise ProjectionError(f"app contract contains malformed component ref: {ref}")

    def decode(value: str) -> str:
        return value.replace("~1", "/").replace("~0", "~")

    return decode(parts[0]), decode(parts[1])


def _reachable_components(
    source_components: dict[str, Any], seeds: Iterable[str]
) -> set[tuple[str, str]]:
    reachable: set[tuple[str, str]] = set()
    pending = deque(_component_key(ref) for ref in seeds)
    while pending:
        section, name = pending.popleft()
        key = (section, name)
        if key in reachable:
            continue
        entries = source_components.get(section)
        if not isinstance(entries, dict) or name not in entries:
            raise ProjectionError(
                f"app contract references missing component: #/components/{section}/{name}"
            )
        reachable.add(key)
        pending.extend(_component_key(ref) for ref in _walk_refs(entries[name]))
    return reachable


def build_app_projection(
    spec: dict[str, Any],
    selected: set[OperationKey],
    required_schemas: Iterable[str] = (),
) -> dict[str, Any]:
    """Copy selected paths and recursively prune unreachable components.

    ``required_schemas`` covers checked-in app aliases and fixtures that name a
    backend component directly instead of reaching it through a typed path.
    """
    projection = {
        key: copy.deepcopy(value)
        for key, value in spec.items()
        if key not in {"paths", "components"}
    }
    projected_paths: dict[str, Any] = {}
    for route, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        selected_methods = {key.method.lower() for key in selected if key.path == route}
        if not selected_methods:
            continue
        projected_item: dict[str, Any] = {}
        for field, value in path_item.items():
            if field.lower() not in {method.lower() for method in HTTP_METHODS}:
                projected_item[field] = copy.deepcopy(value)
            elif field.lower() in selected_methods:
                projected_item[field] = copy.deepcopy(value)
        projected_paths[route] = projected_item
    projection["paths"] = projected_paths

    source_components = spec.get("components", {})
    if not isinstance(source_components, dict):
        source_components = {}
    seed_refs = list(_walk_refs(projection))
    seed_refs.extend(
        f"#/components/schemas/{name.replace('~', '~0').replace('/', '~1')}"
        for name in required_schemas
    )
    reachable = _reachable_components(source_components, seed_refs)
    projected_components: dict[str, Any] = {}
    for section, entries in source_components.items():
        if not isinstance(entries, dict):
            continue
        retained = {
            name: copy.deepcopy(value)
            for name, value in entries.items()
            if (section, name) in reachable
        }
        if retained:
            projected_components[section] = retained
    if projected_components:
        projection["components"] = projected_components

    # Re-walk the finished document so future component-section changes cannot
    # silently leave a dangling local reference.
    for ref in _walk_refs(projection):
        if _component_key(ref) not in reachable:
            raise ProjectionError(f"unresolved app contract reference: {ref}")
    return projection


def render_projection(projection: dict[str, Any]) -> str:
    return json.dumps(projection, indent=2, ensure_ascii=False) + "\n"


def _count_operations(spec: dict[str, Any]) -> int:
    return sum(
        1
        for item in spec.get("paths", {}).values()
        if isinstance(item, dict)
        for method in item
        if method.upper() in HTTP_METHODS
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--openapi", type=Path, default=OPENAPI_SNAPSHOT)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--output", type=Path, default=APP_SNAPSHOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    findings, _, _ = audit(args.openapi, args.policy)
    if findings:
        print("Cannot project an invalid API operation registry:", file=sys.stderr)
        for finding in sorted(findings, key=lambda item: (item.code, item.message)):
            print(f"  {finding.code:22} {finding.message}", file=sys.stderr)
        return 1

    spec = json.loads(args.openapi.read_text(encoding="utf-8"))
    policy = json.loads(args.policy.read_text(encoding="utf-8"))
    mobile_consumers, _ = discover_mobile_consumers()
    selected = select_app_operations(spec, policy, mobile_consumers)
    required_schemas = discover_mobile_schema_consumers()
    projection = build_app_projection(spec, selected, required_schemas)
    rendered = render_projection(projection)

    operation_count = _count_operations(projection)
    schema_count = len(projection.get("components", {}).get("schemas", {}))
    summary = (
        f"{len(projection.get('paths', {}))} paths, "
        f"{operation_count} operations, {schema_count} schemas"
    )
    if args.check:
        if not args.output.exists():
            print(f"App OpenAPI projection missing: {args.output}", file=sys.stderr)
            return 1
        if args.output.read_text(encoding="utf-8") != rendered:
            print(
                "App OpenAPI projection is stale. Run: "
                "python3 scripts/project_app_openapi.py",
                file=sys.stderr,
            )
            return 1
        print(f"App OpenAPI projection is current — {summary}")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"Wrote {args.output} — {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
