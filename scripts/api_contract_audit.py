#!/usr/bin/env python3
"""Audit the effective API operation registry across backend and mobile.

The OpenAPI snapshot owns method, path, and operationId.  The policy file owns
the facts OpenAPI cannot express: audience, lifecycle, owner, non-mobile
consumers, and removal posture.  Mobile consumers are discovered from source at
the method level so a GET caller cannot accidentally cover a POST on the same
path.

The gate fails when:

* a mobile transport calls an operation absent from OpenAPI;
* an OpenAPI operation has neither a product/server consumer nor an explicit
  ``dark``/``retiring`` policy;
* a policy entry no longer exists in OpenAPI;
* an operation recorded as retired reappears in OpenAPI;
* a dark operation gains a product caller; or
* a declared source consumer no longer contains the operation path.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_SNAPSHOT = WORKSPACE_ROOT / "docs" / "openapi.json"
POLICY_PATH = WORKSPACE_ROOT / "docs" / "governance" / "api-operation-policy.json"
FLAG_REGISTRY = WORKSPACE_ROOT / "docs" / "flags" / "registry.yaml"
APP_ROOT = WORKSPACE_ROOT / "travel-app"
HTTP_TS = APP_ROOT / "utils" / "api" / "http.ts"

HTTP_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"})
AUDIENCES = frozenset(
    {"app", "public_web", "operator", "server", "infrastructure", "webhook"}
)
LIFECYCLES = frozenset({"active", "dark", "retiring"})
REQUIRED_POLICY_FIELDS = frozenset(
    {
        "audience",
        "lifecycle",
        "owner",
        "reason",
        "feature_flag",
        "removal_trigger",
        "review_by",
        "consumers",
    }
)


@dataclass(frozen=True, order=True)
class OperationKey:
    method: str
    path: str

    @property
    def registry_key(self) -> str:
        return f"{self.method} {self.path}"

    @property
    def normalized(self) -> tuple[str, str]:
        return self.method, normalize_path(self.path)


@dataclass(frozen=True, order=True)
class Consumer:
    kind: str
    source: str
    symbol: str | None = None

    @property
    def is_product(self) -> bool:
        return self.kind in {"app_source", "app_direct", "app_url"}


@dataclass(frozen=True)
class OpenAPIOperation:
    key: OperationKey
    operation_id: str


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


def _strip_ts_substitutions(value: str) -> str:
    out: list[str] = []
    index = 0
    while index < len(value):
        if value[index : index + 2] != "${":
            out.append(value[index])
            index += 1
            continue
        depth = 1
        cursor = index + 2
        quote: str | None = None
        while cursor < len(value) and depth:
            char = value[cursor]
            if quote:
                if char == "\\":
                    cursor += 2
                    continue
                if char == quote:
                    quote = None
            elif char in {"'", '"', "`"}:
                quote = char
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            cursor += 1
        out.append("{*}")
        index = cursor
    return "".join(out)


def normalize_path(value: str) -> str:
    """Normalize OpenAPI and TypeScript URL templates to a comparable path."""
    value = _strip_ts_substitutions(value)
    starts = [
        value.find(prefix)
        for prefix in (
            "/api/",
            "/admin/",
            "/health",
            "/ready",
            "/debug",
            "/metrics",
            "/webhooks",
        )
        if value.find(prefix) >= 0
    ]
    if starts:
        value = value[min(starts) :]
    value = value.split("?", 1)[0].split("#", 1)[0]
    value = re.sub(r"\{[^}]+\}", "{*}", value)
    parts = value.split("/")
    parts = [
        part[: -len("{*}")] if part.endswith("{*}") and part != "{*}" else part
        for part in parts
    ]
    return "/".join(parts).rstrip("/") or "/"


def _read_balanced(
    source: str, start: int, opener: str, closer: str
) -> tuple[str, int] | None:
    if start >= len(source) or source[start] != opener:
        return None
    depth = 0
    quote: str | None = None
    index = start
    while index < len(source):
        char = source[index]
        if quote:
            if char == "\\":
                index += 2
                continue
            if char == quote:
                quote = None
        elif char in {"'", '"', "`"}:
            quote = char
        elif char == opener:
            depth += 1
        elif char == closer:
            depth -= 1
            if depth == 0:
                return source[start : index + 1], index + 1
        index += 1
    return None


def _read_string(source: str, start: int) -> tuple[str, int] | None:
    if start >= len(source) or source[start] not in {"'", '"', "`"}:
        return None
    quote = source[start]
    index = start + 1
    chunks: list[str] = []
    while index < len(source):
        char = source[index]
        if char == "\\":
            if index + 1 < len(source):
                chunks.extend((char, source[index + 1]))
            index += 2
            continue
        if char == quote:
            return "".join(chunks), index + 1
        # A nested template literal inside ${...} is uncommon but legal.  The
        # normalizer only needs the path before a query expression, so stop at
        # the first nested backtick rather than manufacturing a false route.
        chunks.append(char)
        index += 1
    return None


def _skip_space(source: str, index: int) -> int:
    while index < len(source) and source[index].isspace():
        index += 1
    return index


def _iter_call_bodies(
    source: str, names: Iterable[str]
) -> Iterable[tuple[str, str, str, int]]:
    """Yield ``(callee, first-string-argument, call-body, position)``."""
    name_pattern = "|".join(
        re.escape(name) for name in sorted(names, key=len, reverse=True)
    )
    for match in re.finditer(rf"\b({name_pattern})\s*", source):
        callee = match.group(1)
        index = _skip_space(source, match.end())
        if index < len(source) and source[index] == "<":
            generic = _read_balanced(source, index, "<", ">")
            if generic is None:
                continue
            _, index = generic
            index = _skip_space(source, index)
        if index >= len(source) or source[index] != "(":
            continue
        call = _read_balanced(source, index, "(", ")")
        if call is None:
            continue
        call_body, _ = call
        arg_index = _skip_space(source, index + 1)
        first = _read_string(source, arg_index)
        if first is None:
            continue
        url, _ = first
        yield callee, url, call_body, match.start()


def _method_for_call(callee: str, call_body: str) -> str:
    explicit = re.search(r"\bmethod\s*:\s*['\"]([A-Z]+)['\"]", call_body)
    if explicit:
        return explicit.group(1)
    if callee in {"_uploadFile", "streamSSE"}:
        return "POST"
    return "GET"


def load_openapi(
    path: Path,
) -> tuple[dict[OperationKey, OpenAPIOperation], list[Finding]]:
    spec = json.loads(path.read_text(encoding="utf-8"))
    operations: dict[OperationKey, OpenAPIOperation] = {}
    operation_ids: dict[str, OperationKey] = {}
    findings: list[Finding] = []
    for route, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        for method, value in item.items():
            upper = method.upper()
            if upper not in HTTP_METHODS:
                continue
            key = OperationKey(upper, route)
            operation_id = value.get("operationId") if isinstance(value, dict) else None
            if not operation_id:
                findings.append(
                    Finding(
                        "missing-operation-id", f"{key.registry_key} has no operationId"
                    )
                )
                operation_id = ""
            elif operation_id in operation_ids:
                findings.append(
                    Finding(
                        "duplicate-operation-id",
                        f"{key.registry_key} and {operation_ids[operation_id].registry_key} share {operation_id}",
                    )
                )
            else:
                operation_ids[operation_id] = key
            operations[key] = OpenAPIOperation(key=key, operation_id=operation_id)
    return operations, findings


def _relative(path: Path) -> str:
    return path.relative_to(WORKSPACE_ROOT).as_posix()


def _http_method_at(source: str, position: int) -> str | None:
    object_start = source.find("export const httpApi")
    if object_start < 0 or position < object_start:
        return None
    candidates = list(
        re.finditer(
            r"^  (?:async )?([A-Za-z_]\w*)\s*\(",
            source[object_start:position],
            re.MULTILINE,
        )
    )
    return candidates[-1].group(1) if candidates else None


def _product_method_callers(method_names: set[str]) -> dict[str, set[str]]:
    callers: dict[str, set[str]] = defaultdict(set)
    if not APP_ROOT.exists():
        return callers
    pattern = re.compile(r"\bapi\.([A-Za-z_]\w*)\s*\(")
    for path in APP_ROOT.rglob("*"):
        if path.suffix not in {".ts", ".tsx"}:
            continue
        if any(
            part in {"node_modules", "__tests__", "mock", ".expo"}
            for part in path.parts
        ):
            continue
        relative = path.relative_to(APP_ROOT)
        if relative.parts[:2] == ("utils", "api"):
            continue
        source = path.read_text(encoding="utf-8", errors="ignore")
        for match in pattern.finditer(source):
            method = match.group(1)
            if method in method_names:
                callers[method].add(_relative(path))
    return callers


def discover_mobile_consumers() -> tuple[
    dict[tuple[str, str], set[Consumer]], set[tuple[str, str]]
]:
    consumers: dict[tuple[str, str], set[Consumer]] = defaultdict(set)
    calls_by_method: dict[str, set[tuple[str, str]]] = defaultdict(set)
    if HTTP_TS.exists():
        source = HTTP_TS.read_text(encoding="utf-8")
        for callee, url, body, position in _iter_call_bodies(
            source, {"_request", "_uploadFile"}
        ):
            method = _method_for_call(callee, body)
            normalized = (method, normalize_path(url))
            symbol = _http_method_at(source, position)
            consumers[normalized].add(
                Consumer("app_transport", _relative(HTTP_TS), symbol)
            )
            if symbol:
                calls_by_method[symbol].add(normalized)

    product_callers = _product_method_callers(set(calls_by_method))
    for symbol, endpoints in calls_by_method.items():
        for endpoint in endpoints:
            for source in product_callers.get(symbol, set()):
                consumers[endpoint].add(Consumer("app_source", source, symbol))

    # Direct calls outside the facade: fetch/expoFetch and streamSSE. Calls
    # whose URL is passed indirectly are declared in policy and source-checked.
    if APP_ROOT.exists():
        for path in APP_ROOT.rglob("*"):
            if path.suffix not in {".ts", ".tsx"}:
                continue
            if any(
                part in {"node_modules", "__tests__", "mock", ".expo"}
                for part in path.parts
            ):
                continue
            if path in {HTTP_TS, APP_ROOT / "utils" / "api" / "schema.gen.ts"}:
                continue
            source = path.read_text(encoding="utf-8", errors="ignore")
            for callee, url, body, _ in _iter_call_bodies(
                source, {"fetch", "expoFetch", "streamSSE"}
            ):
                normalized_path = normalize_path(url)
                if not normalized_path.startswith(
                    (
                        "/api/",
                        "/admin/",
                        "/health",
                        "/ready",
                        "/debug",
                        "/metrics",
                        "/webhooks",
                    )
                ):
                    continue
                method = _method_for_call(callee, body)
                consumers[(method, normalized_path)].add(
                    Consumer("app_direct", _relative(path))
                )

    return consumers, set(consumers)


def _path_pattern(path: str) -> re.Pattern[str]:
    parts = re.split(r"\{[^}]+\}", path)
    escaped = [re.escape(part) for part in parts]
    parameter = r"(?:\$\{[^}]+\}|:[A-Za-z_]\w*|[^/`'\"\\]+)"
    return re.compile(parameter.join(escaped))


def load_policy(path: Path) -> tuple[dict[str, Any], list[Finding]]:
    if not path.exists():
        return {}, [Finding("missing-policy", f"operation policy missing at {path}")]
    policy = json.loads(path.read_text(encoding="utf-8"))
    findings: list[Finding] = []
    if policy.get("version") != 1:
        findings.append(
            Finding("policy-version", "api operation policy version must be 1")
        )
    defaults = policy.get("defaults")
    if not isinstance(defaults, dict):
        findings.append(
            Finding("policy-defaults", "api operation policy requires defaults")
        )
    operations = policy.get("operations")
    if not isinstance(operations, dict):
        findings.append(
            Finding(
                "policy-operations",
                "api operation policy requires an operations object",
            )
        )
    retired_operations = policy.get("retired_operations")
    if not isinstance(retired_operations, dict):
        findings.append(
            Finding(
                "policy-retired-operations",
                "api operation policy requires a retired_operations object",
            )
        )
    return policy, findings


def _registered_feature_flags(path: Path = FLAG_REGISTRY) -> set[str]:
    if not path.exists():
        return set()
    return set(
        re.findall(r"^\s*-\s+name:\s*['\"]?([^\s'\"]+)", path.read_text(), re.MULTILINE)
    )


def _validate_policy_entry(
    key: str, entry: Any, registered_feature_flags: set[str]
) -> list[Finding]:
    if not isinstance(entry, dict):
        return [Finding("invalid-policy", f"{key}: policy entry must be an object")]
    findings: list[Finding] = []
    missing = REQUIRED_POLICY_FIELDS - set(entry)
    if missing:
        findings.append(
            Finding(
                "invalid-policy", f"{key}: missing fields {', '.join(sorted(missing))}"
            )
        )
    if entry.get("audience") not in AUDIENCES:
        findings.append(
            Finding(
                "invalid-policy", f"{key}: invalid audience {entry.get('audience')!r}"
            )
        )
    if entry.get("lifecycle") not in LIFECYCLES:
        findings.append(
            Finding(
                "invalid-policy", f"{key}: invalid lifecycle {entry.get('lifecycle')!r}"
            )
        )
    if not isinstance(entry.get("consumers"), list):
        findings.append(Finding("invalid-policy", f"{key}: consumers must be a list"))
    if not isinstance(entry.get("owner"), str) or not entry.get("owner", "").strip():
        findings.append(Finding("invalid-policy", f"{key}: owner must be non-empty"))
    if not isinstance(entry.get("reason"), str) or not entry.get("reason", "").strip():
        findings.append(Finding("invalid-policy", f"{key}: reason must be non-empty"))
    if entry.get("feature_flag") is not None and not isinstance(
        entry.get("feature_flag"), str
    ):
        findings.append(
            Finding("invalid-policy", f"{key}: feature_flag must be a string or null")
        )
    if entry.get("lifecycle") == "dark" and not entry.get("feature_flag"):
        findings.append(
            Finding(
                "invalid-policy",
                f"{key}: dark operations require a registered feature_flag",
            )
        )
    elif (
        entry.get("lifecycle") == "dark"
        and entry.get("feature_flag") not in registered_feature_flags
    ):
        findings.append(
            Finding(
                "invalid-policy",
                f"{key}: feature_flag {entry.get('feature_flag')!r} is not registered",
            )
        )
    if entry.get("lifecycle") in {"dark", "retiring"}:
        if not entry.get("removal_trigger") or not entry.get("review_by"):
            findings.append(
                Finding(
                    "invalid-policy",
                    f"{key}: dark/retiring entries need removal_trigger and review_by",
                )
            )
        else:
            try:
                review_by = date.fromisoformat(entry["review_by"])
            except (TypeError, ValueError):
                findings.append(
                    Finding("invalid-policy", f"{key}: review_by must be an ISO date")
                )
            else:
                if review_by < date.today():
                    findings.append(
                        Finding(
                            "expired-policy",
                            f"{key}: review_by {review_by.isoformat()} has passed",
                        )
                    )
    return findings


def audit(
    openapi_path: Path = OPENAPI_SNAPSHOT,
    policy_path: Path = POLICY_PATH,
    discovered_mobile_consumers: dict[tuple[str, str], set[Consumer]] | None = None,
    registered_feature_flags: set[str] | None = None,
) -> tuple[list[Finding], dict[str, int], list[str]]:
    operations, findings = load_openapi(openapi_path)
    policy, policy_findings = load_policy(policy_path)
    findings.extend(policy_findings)
    if policy_findings:
        return findings, {}, []

    overrides: dict[str, Any] = policy["operations"]
    retired_operations: dict[str, Any] = policy["retired_operations"]
    defaults: dict[str, Any] = policy["defaults"]
    registered_flags = (
        registered_feature_flags
        if registered_feature_flags is not None
        else _registered_feature_flags()
    )
    operation_by_normalized = {
        operation.key.normalized: operation for operation in operations.values()
    }
    mobile_consumers = (
        discovered_mobile_consumers
        if discovered_mobile_consumers is not None
        else discover_mobile_consumers()[0]
    )
    mobile_endpoints = set(mobile_consumers)

    for endpoint in sorted(mobile_endpoints):
        if endpoint not in operation_by_normalized:
            findings.append(
                Finding(
                    "mobile-drift",
                    f"{endpoint[0]} {endpoint[1]} is called by mobile but absent from OpenAPI",
                )
            )

    openapi_keys = {key.registry_key for key in operations}
    for retired_key, retirement in sorted(retired_operations.items()):
        if not isinstance(retirement, dict) or not all(
            isinstance(retirement.get(field), str) and retirement[field].strip()
            for field in ("owner", "reason", "replacement", "retired_on")
        ):
            findings.append(
                Finding(
                    "invalid-retirement",
                    f"{retired_key}: retirement needs owner, reason, replacement, and retired_on",
                )
            )
        else:
            try:
                date.fromisoformat(retirement["retired_on"])
            except ValueError:
                findings.append(
                    Finding(
                        "invalid-retirement",
                        f"{retired_key}: retired_on must be an ISO date",
                    )
                )
            replacement = retirement["replacement"]
            if replacement not in openapi_keys:
                findings.append(
                    Finding(
                        "retirement-replacement-missing",
                        f"{retired_key}: replacement is absent from OpenAPI: {replacement}",
                    )
                )
        if retired_key in openapi_keys:
            findings.append(
                Finding(
                    "retired-operation-exposed",
                    f"{retired_key} is retired but still exposed in OpenAPI",
                )
            )
        if retired_key in overrides:
            findings.append(
                Finding(
                    "retirement-policy-overlap",
                    f"{retired_key} cannot be both current policy and retired",
                )
            )
    for stale in sorted(set(overrides) - openapi_keys):
        findings.append(
            Finding("stale-policy", f"{stale} is in policy but absent from OpenAPI")
        )

    counts: dict[str, int] = defaultdict(int)
    transport_only: list[str] = []
    for operation in sorted(operations.values(), key=lambda item: item.key):
        registry_key = operation.key.registry_key
        override = overrides.get(registry_key)
        if override is not None:
            findings.extend(
                _validate_policy_entry(registry_key, override, registered_flags)
            )
        effective = {**defaults, **(override or {})}
        audience = effective.get("audience")
        lifecycle = effective.get("lifecycle")
        counts[f"audience:{audience}"] += 1
        counts[f"lifecycle:{lifecycle}"] += 1
        if lifecycle == "dark" and effective.get("feature_flag") is None:
            counts["dark:unflagged"] += 1

        discovered = set(mobile_consumers.get(operation.key.normalized, set()))
        declared_consumers = effective.get("consumers", []) if override else []
        for declared in declared_consumers:
            if not isinstance(declared, dict) or not declared.get("name"):
                findings.append(
                    Finding(
                        "invalid-consumer",
                        f"{registry_key}: every consumer needs a name",
                    )
                )
                continue
            source_name = declared.get("source")
            if source_name:
                source_path = WORKSPACE_ROOT / source_name
                if not source_path.exists():
                    findings.append(
                        Finding(
                            "stale-consumer",
                            f"{registry_key}: source does not exist: {source_name}",
                        )
                    )
                elif not _path_pattern(operation.key.path).search(
                    source_path.read_text(encoding="utf-8", errors="ignore")
                ):
                    findings.append(
                        Finding(
                            "stale-consumer",
                            f"{registry_key}: path no longer appears in {source_name}",
                        )
                    )
                else:
                    discovered.add(
                        Consumer(
                            declared.get("kind", "declared"),
                            source_name,
                            declared.get("name"),
                        )
                    )
            else:
                discovered.add(
                    Consumer(declared.get("kind", "declared"), declared.get("name"))
                )

        product_consumers = {consumer for consumer in discovered if consumer.is_product}
        transport_consumers = {
            consumer for consumer in discovered if consumer.kind == "app_transport"
        }
        named_nonapp = {
            consumer
            for consumer in discovered
            if consumer.kind not in {"app_transport"}
        }

        if lifecycle == "dark" and product_consumers:
            sources = ", ".join(
                sorted(consumer.source for consumer in product_consumers)
            )
            findings.append(
                Finding(
                    "dark-has-caller",
                    f"{registry_key} is dark but has product caller(s): {sources}",
                )
            )
        if not named_nonapp and transport_consumers:
            transport_only.append(registry_key)
            if override is None:
                findings.append(
                    Finding(
                        "transport-only",
                        f"{registry_key} has only an http.ts implementation; classify it explicitly",
                    )
                )
        if not discovered and lifecycle not in {"dark", "retiring"}:
            findings.append(
                Finding(
                    "missing-consumer",
                    f"{registry_key} has no detected or declared consumer",
                )
            )

    return findings, dict(counts), transport_only


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--openapi", type=Path, default=OPENAPI_SNAPSHOT)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--list-transport-only", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    findings, counts, transport_only = audit(args.openapi, args.policy)
    if args.json_output:
        print(
            json.dumps(
                {
                    "ok": not findings,
                    "counts": counts,
                    "transport_only": transport_only,
                    "findings": [finding.__dict__ for finding in findings],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        if findings:
            print(f"API contract audit failed — {len(findings)} finding(s):")
            for finding in sorted(findings, key=lambda item: (item.code, item.message)):
                print(f"  {finding.code:22} {finding.message}")
        else:
            active = counts.get("lifecycle:active", 0)
            dark = counts.get("lifecycle:dark", 0)
            retiring = counts.get("lifecycle:retiring", 0)
            unflagged = counts.get("dark:unflagged", 0)
            print(
                f"API contract audit passed — {active} active, {dark} dark "
                f"({unflagged} unflagged), {retiring} retiring operations"
            )
        if args.list_transport_only and transport_only:
            print("\nTransport implementations without product callers:")
            for key in transport_only:
                print(f"  {key}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
