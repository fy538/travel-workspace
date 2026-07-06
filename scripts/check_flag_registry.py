#!/usr/bin/env python3
"""Feature-flag expiry guard — assert every `active` flag in the canonical
registry (docs/flags/registry.yaml) hasn't blown past its review/removal
date. Pure file-parse, NO DB — runs at pre-push alongside the other
heavier/more-context checks (see workspace .pre-commit-config.yaml).

Why this exists: as of 2026-07-06, 26 feature flags across travel-agent and
travel-app had zero owner or expiration metadata anywhere in the code —
exactly how "shipped dark for now" quietly becomes permanent debt. This
script doesn't stop a flag from existing; it stops one from being silently
forgotten past its own stated review date.

`category: ops` flags (permanent kill-switches) still get an expiry date,
but it reads as "review by," not "must remove by" — the notes field
explains why for each. This script does not distinguish category when
deciding whether to fail; it only checks `status: active` + `expires` in
the past. If an ops flag's date lapses, treat the failure as "go re-affirm
this is still supposed to be a permanent toggle," not "go delete it."

To resolve a flag: either extend `expires`, or set `status: resolved` once
it has actually been removed/permanently flipped (don't delete the row —
it's the historical record).

Usage::

    python3 scripts/check_flag_registry.py
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
_REGISTRY = _REPO / "docs" / "flags" / "registry.yaml"


def _load_flags() -> list[dict]:
    data = yaml.safe_load(_REGISTRY.read_text()) or {}
    return data.get("flags", [])


def main() -> int:
    if not _REGISTRY.exists():
        print(f"FLAG REGISTRY MISSING: {_REGISTRY}", file=sys.stderr)
        return 1

    flags = _load_flags()
    today = date.today()
    overdue: list[tuple[str, int]] = []

    for flag in flags:
        if flag.get("status") != "active":
            continue
        expires = flag.get("expires")
        if expires is None:
            print(f"MISSING expires: {flag.get('name', '<unnamed>')}", file=sys.stderr)
            overdue.append((flag.get("name", "<unnamed>"), -1))
            continue
        # PyYAML parses an unquoted YYYY-MM-DD scalar as datetime.date already.
        if not isinstance(expires, date):
            print(
                f"UNPARSEABLE expires for {flag.get('name', '<unnamed>')}: {expires!r}",
                file=sys.stderr,
            )
            overdue.append((flag.get("name", "<unnamed>"), -1))
            continue
        if expires < today:
            overdue.append((flag["name"], (today - expires).days))

    if overdue:
        print(f"{len(overdue)} feature flag(s) past their review/removal date:", file=sys.stderr)
        for name, days in sorted(overdue, key=lambda x: -x[1]):
            if days < 0:
                print(f"  - {name}: invalid/missing expires field", file=sys.stderr)
            else:
                print(f"  - {name}: {days} day(s) overdue", file=sys.stderr)
        print(
            f"\nEdit {_REGISTRY.relative_to(_REPO)}: extend `expires`, or set "
            "`status: resolved` if the flag has already been removed/flipped permanently.",
            file=sys.stderr,
        )
        return 1

    print(f"OK — {len(flags)} flags checked, none overdue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
