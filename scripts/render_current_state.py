#!/usr/bin/env python3
"""Render the derived block in docs/status/current-state.md."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import yaml

from check_doc_inventory import load_inventory, validate

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "docs/status/current-state.md"
BEGIN = "<!-- BEGIN auto:current-state -->"
END = "<!-- END auto:current-state -->"
METHODS = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}


def render() -> str:
    api = json.loads((ROOT / "docs/openapi.json").read_text())
    paths = api.get("paths", {})
    operations = sum(sum(method in METHODS for method in value) for value in paths.values())
    schemas = len(api.get("components", {}).get("schemas", {}))
    journeys = yaml.safe_load((ROOT / "docs/journeys/journeys.yaml").read_text())["journeys"]
    tiers = Counter(item["tier"] for item in journeys)
    flags = yaml.safe_load((ROOT / "docs/flags/registry.yaml").read_text())["flags"]
    statuses = Counter(item["status"] for item in flags)
    inventory, problems = validate(load_inventory())
    if problems:
        raise ValueError("inventory is invalid: " + "; ".join(problems))
    systems = len(list((ROOT / "docs/systems").glob("*.md")))
    lines = [
        BEGIN,
        "<!-- Run `make docs-status-sync` to update this block. -->",
        "| Signal | Current value | Authority |", "|---|---:|---|",
        f"| API contract | {len(paths)} paths / {operations} operations / {schemas} schemas | [`docs/openapi.json`](../openapi.json) |",
        f"| Canonical journeys | {len(journeys)} total / {tiers['golden-path']} golden path / {tiers['holistic-extension']} holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |",
        f"| Feature flags | {len(flags)} registered / {statuses['active']} active / {statuses['resolved']} resolved | [`registry.yaml`](../flags/registry.yaml) |",
        f"| System charters | {systems} Markdown documents | [`systems/`](../systems/) |",
        f"| Documentation inventory | {len(inventory)} files classified | [`inventory.yaml`](../governance/inventory.yaml) |",
        END,
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    text = DOC.read_text()
    before, rest = text.split(BEGIN, 1)
    _, after = rest.split(END, 1)
    expected = before + render() + after
    if args.write:
        DOC.write_text(expected)
        print("updated", DOC.relative_to(ROOT))
        return 0
    if text != expected:
        print("current-state drift: run `make docs-status-sync`")
        return 1
    print("current-state OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
