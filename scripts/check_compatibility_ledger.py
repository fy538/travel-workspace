#!/usr/bin/env python3
"""Validate the workspace compatibility-exception registry.

Usage:
    python3 scripts/check_compatibility_ledger.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "docs/governance/compatibility-ledger.json"
REQUIRED = {"id", "status", "reason", "owner", "canonical", "paths", "markers", "removal_trigger", "expires"}
STATUSES = {"active", "retiring"}
MARKER_RE = re.compile(r"compatibility_id:\s*([a-z0-9][a-z0-9-]*)")
SOURCE_ROOTS = (ROOT / "travel-app", ROOT / "travel-agent")


def main() -> int:
    try:
        ledger = json.loads(LEDGER.read_text())
    except (OSError, json.JSONDecodeError) as error:
        print(f"compatibility ledger unreadable: {error}")
        return 1

    policy = ledger.get("policy", {})
    allowed_reasons = set(policy.get("allowed_reasons", []))
    entries = ledger.get("entries")
    if ledger.get("version") != 1 or not isinstance(entries, list) or not allowed_reasons:
        print("compatibility ledger must declare version 1, policy reasons, and entries")
        return 1

    failures: list[str] = []
    seen: set[str] = set()
    today = date.today()
    for entry in entries:
        if not isinstance(entry, dict):
            failures.append("entry is not an object")
            continue
        entry_id = entry.get("id", "<missing id>")
        missing = REQUIRED - entry.keys()
        if missing:
            failures.append(f"{entry_id}: missing {', '.join(sorted(missing))}")
            continue
        if entry_id in seen:
            failures.append(f"duplicate id: {entry_id}")
        seen.add(entry_id)
        if entry["status"] not in STATUSES:
            failures.append(f"{entry_id}: invalid status {entry['status']!r}")
        if entry["reason"] not in allowed_reasons:
            failures.append(f"{entry_id}: invalid reason {entry['reason']!r}")
        if not all(isinstance(entry[key], str) and entry[key].strip() for key in ("owner", "canonical", "removal_trigger")):
            failures.append(f"{entry_id}: owner, canonical, and removal_trigger must be non-empty strings")
        try:
            expiry = date.fromisoformat(entry["expires"])
            if expiry < today:
                failures.append(f"{entry_id}: expired on {expiry}; remove or explicitly renew it")
        except (TypeError, ValueError):
            failures.append(f"{entry_id}: expires must be ISO YYYY-MM-DD")

        paths = entry["paths"]
        markers = entry["markers"]
        if not isinstance(paths, list) or not paths or not all(isinstance(path, str) for path in paths):
            failures.append(f"{entry_id}: paths must be a non-empty string list")
            continue
        if not isinstance(markers, list) or not all(isinstance(marker, str) for marker in markers):
            failures.append(f"{entry_id}: markers must be a string list")
            continue
        contents: list[str] = []
        for raw_path in paths:
            path = ROOT / raw_path
            if not path.is_file():
                failures.append(f"{entry_id}: missing tracked path {raw_path}")
                continue
            contents.append(path.read_text(errors="replace"))
        joined = "\n".join(contents)
        for marker in markers:
            if marker not in joined:
                failures.append(f"{entry_id}: marker not found in tracked paths: {marker!r}")

    discovered: dict[str, list[str]] = {}
    for source_root in SOURCE_ROOTS:
        if not source_root.is_dir():
            continue
        for path in source_root.rglob("*"):
            if path.suffix not in {".py", ".ts", ".tsx"} or not path.is_file():
                continue
            if any(part in {"node_modules", ".git", ".venv"} for part in path.parts):
                continue
            for marker_id in MARKER_RE.findall(path.read_text(errors="replace")):
                discovered.setdefault(marker_id, []).append(str(path.relative_to(ROOT)))
    for marker_id, paths in sorted(discovered.items()):
        if marker_id not in seen:
            failures.append(
                f"unregistered compatibility marker {marker_id}: {', '.join(paths)}"
            )

    if failures:
        print("compatibility ledger check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"compatibility ledger ok: {len(entries)} active/retiring exceptions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
