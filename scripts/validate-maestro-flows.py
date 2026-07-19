#!/usr/bin/env python3
"""Validate Maestro structure, lane policy, references, and workspace configs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


PRIMARY_LANES = {
    "harness",
    "polish-capture",
    "visual-baseline",
    "animation",
    "stability",
    "native-live",
    "journey-nightly",
    "legacy-visual",
}
SELECTOR_TAGS = {"pr-smoke", "android-smoke", "quarantine"}
REQUIRED_PROPERTIES = {"owner", "lane", "isolation", "fixture"}
EXPECTED_SELECTOR_COUNTS = {"pr-smoke": 10, "android-smoke": 5}


def walk(value: Any):
    """Yield every mapping contained in a Maestro command document."""
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def load_flow(path: Path, errors: list[str]) -> tuple[dict[str, Any], list[Any]] | None:
    try:
        docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    except Exception as exc:  # noqa: BLE001 - validation should surface all parser failures
        fail(errors, path, f"YAML parse failed: {str(exc).splitlines()[0]}")
        return None
    if len(docs) != 2 or not isinstance(docs[0], dict) or not isinstance(docs[1], list):
        fail(errors, path, "flow must contain one mapping header and one command-list document")
        return None
    return docs[0], docs[1]


def resolve_run_flow(path: Path, command: dict[str, Any], errors: list[str]) -> None:
    value = command.get("runFlow")
    if isinstance(value, str):
        target = value
    elif isinstance(value, dict):
        target = value.get("file")
    else:
        return
    if not isinstance(target, str) or "${" in target:
        return
    resolved = (path.parent / target).resolve()
    if not resolved.is_file():
        fail(errors, path, f"runFlow file does not resolve relative to its caller: {target}")


def validate_configs(
    maestro_dir: Path,
    configs: list[Path],
    flow_tags: dict[Path, set[str]],
    errors: list[str],
) -> None:
    for config in configs:
        try:
            data = yaml.safe_load(config.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(errors, config, f"config YAML parse failed: {str(exc).splitlines()[0]}")
            continue
        if not isinstance(data, dict):
            fail(errors, config, "workspace config must be a mapping")
            continue
        patterns = data.get("flows")
        if not isinstance(patterns, list) or not patterns:
            fail(errors, config, "workspace config must declare at least one flows pattern")
            continue
        matched: set[Path] = set()
        for pattern in patterns:
            if not isinstance(pattern, str):
                fail(errors, config, f"non-string flows pattern: {pattern!r}")
                continue
            matched.update(
                path.resolve()
                for path in maestro_dir.glob(pattern)
                if path.is_file() and not path.name.startswith("config")
            )
        if not matched:
            fail(errors, config, f"flows patterns match no flow files: {patterns}")
            continue
        include = data.get("includeTags", [])
        if include and not any(set(include) & flow_tags.get(path, set()) for path in matched):
            fail(errors, config, f"includeTags select no matched flows: {include}")


def package_references(app_dir: Path, errors: list[str]) -> int:
    package_path = app_dir / "package.json"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    scripts: dict[str, str] = package.get("scripts", {})
    pattern = re.compile(r"\.maestro/[\w./-]+\.ya?ml")
    count = 0
    for name, script in scripts.items():
        if not (name.startswith("visual-qa") or name.startswith("maestro:")):
            continue
        for reference in pattern.findall(script):
            count += 1
            if not (app_dir / reference).is_file():
                fail(errors, package_path, f"script {name!r} references missing {reference}")
    if count == 0:
        fail(errors, package_path, "no Maestro config or flow references found in lane scripts")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-dir", default="travel-app")
    args = parser.parse_args()

    app_dir = Path(args.app_dir).resolve()
    maestro_dir = app_dir / ".maestro"
    if not maestro_dir.is_dir():
        print(f"::error::No .maestro directory under {app_dir}", file=sys.stderr)
        return 1

    flows = sorted(
        path for path in maestro_dir.rglob("*.yaml") if not path.name.startswith("config")
    )
    configs = sorted(maestro_dir.glob("config*.yaml"))
    errors: list[str] = []
    names: dict[str, list[Path]] = defaultdict(list)
    screenshots: dict[str, list[Path]] = defaultdict(list)
    flow_tags: dict[Path, set[str]] = {}
    selector_counts: dict[str, int] = defaultdict(int)

    for path in flows:
        loaded = load_flow(path, errors)
        if loaded is None:
            continue
        header, commands = loaded
        name = header.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(errors, path, "header must have a non-empty name")
        else:
            names[name].append(path)
        if not isinstance(header.get("appId"), str):
            fail(errors, path, "header must have an appId")

        tags_value = header.get("tags", [])
        tags = set(tags_value) if isinstance(tags_value, list) else set()
        flow_tags[path.resolve()] = tags
        unknown = tags - PRIMARY_LANES - SELECTOR_TAGS
        if unknown:
            fail(errors, path, f"unknown execution tags (move reporting labels to properties): {sorted(unknown)}")
        primary = tags & PRIMARY_LANES
        if len(primary) != 1:
            fail(errors, path, f"must have exactly one primary lane tag; found {sorted(primary)}")
        for selector in tags & SELECTOR_TAGS:
            selector_counts[selector] += 1

        properties = header.get("properties")
        if not isinstance(properties, dict):
            fail(errors, path, "header must have reporting properties")
            properties = {}
        missing = REQUIRED_PROPERTIES - properties.keys()
        if missing:
            fail(errors, path, f"missing reporting properties: {sorted(missing)}")
        if len(primary) == 1 and properties.get("lane") != next(iter(primary)):
            fail(errors, path, "properties.lane must match the primary lane tag")
        if tags & {"pr-smoke", "journey-nightly"} and properties.get("isolation") == "shared-mock-session":
            fail(errors, path, "PR/nightly flows may not depend on a shared mock session")

        for command in walk(commands):
            resolve_run_flow(path, command, errors)
            if command.get("optional") is True and (
                "assertVisible" in command or "assertNotVisible" in command
            ):
                fail(errors, path, "assertions may not be optional")
            wait = command.get("extendedWaitUntil")
            if isinstance(wait, dict) and isinstance(wait.get("timeout"), (int, float)):
                timeout = wait["timeout"]
                if timeout > 90_000:
                    fail(errors, path, f"extendedWaitUntil exceeds the 90s hard ceiling: {timeout}")
                elif (
                    timeout > 30_000
                    and properties.get("lane") != "native-live"
                    and properties.get("timeoutBudget") != "long"
                ):
                    fail(
                        errors,
                        path,
                        f"extendedWaitUntil {timeout}ms requires timeoutBudget: long",
                    )
            if "takeScreenshot" in command:
                screenshot = command["takeScreenshot"]
                if isinstance(screenshot, str):
                    screenshots[screenshot].append(path)

    for name, paths in names.items():
        if len(paths) > 1:
            fail(errors, paths[0], f"duplicate flow name {name!r}: {', '.join(map(str, paths))}")
    for screenshot, paths in screenshots.items():
        if len(paths) > 1:
            fail(errors, paths[0], f"duplicate screenshot name {screenshot!r}: {', '.join(map(str, paths))}")
    for selector, expected in EXPECTED_SELECTOR_COUNTS.items():
        if selector_counts[selector] != expected:
            errors.append(
                f"lane inventory: expected {expected} {selector} flows, found {selector_counts[selector]}"
            )

    validate_configs(maestro_dir, configs, flow_tags, errors)
    reference_count = package_references(app_dir, errors)

    print(
        f"Validated {len(flows)} flows, {len(configs)} configs, "
        f"{len(names)} unique names, and {reference_count} package references."
    )
    if errors:
        print(f"\n✗ {len(errors)} Maestro governance error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(
        "✓ Maestro structure, lane metadata, isolation, subflows, screenshots, "
        "configs, and package references are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
