#!/usr/bin/env python3
"""Validate the eight canonical documentation entry points."""
from pathlib import Path
import sys
import yaml

from check_doc_inventory import classify, load_inventory

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "docs/governance/spine.yaml"
EXPECTED = {"product-thesis", "beliefs", "v1-scope", "current-state", "journey-status", "systems", "owner-actions", "decisions"}


def main() -> int:
    entries = yaml.safe_load(CATALOG.read_text()).get("entries", [])
    problems = []
    ids = [item.get("id") for item in entries]
    paths = [item.get("path") for item in entries]
    if len(entries) != 8 or set(ids) != EXPECTED or len(ids) != len(set(ids)):
        problems.append("catalog must contain the eight unique canonical IDs")
    if len(paths) != len(set(paths)):
        problems.append("catalog paths must be unique")
    inventory = load_inventory()
    readme = (ROOT / "docs/README.md").read_text()
    for item in entries:
        path = item.get("path")
        if not isinstance(path, str) or not (ROOT / path).is_file():
            problems.append(f"missing spine path: {path}")
            continue
        if "/archive/" in f"/{path}":
            problems.append(f"spine path is archived: {path}")
        if path.startswith("docs/"):
            result = classify(path, inventory)
            if result is None or result.disposition != "keep_authoritative":
                problems.append(f"workspace spine doc is not keep_authoritative: {path}")
        if path not in readme:
            problems.append(f"docs/README.md does not name catalog path: {path}")
    for problem in problems:
        print("docs-spine:", problem, file=sys.stderr)
    if problems:
        return 1
    print("docs-spine OK: eight entry points exist, are authoritative, and are indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
