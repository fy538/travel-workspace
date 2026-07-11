#!/usr/bin/env python3
"""Feature-flag registry guard — two checks against the canonical registry
(docs/flags/registry.yaml): every `active` flag hasn't blown past its
review/removal date, and every ad-hoc env-flag lever read in the
travel-agent backend has a registry row at all. Pure file-parse, NO DB —
runs at pre-push alongside the other heavier/more-context checks (see
workspace .pre-commit-config.yaml).

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

Second check — unregistered ad-hoc flags (added 2026-07-10, simplification
audit): the registry's own review-by-date discipline only protects flags
that made it into the file in the first place. A follow-up sweep found 8
flags (ATLAS_SEMANTIC_READ/WRITE, the 4 PLANNING_* levers, FACTS_WRAPPER_
ENFORCE) that were never added — all read via the `truthy_env`/`falsy_env`
"ad hoc per-request flag" convention (see backend/core/feature_flags.py's
own docstring for that phrase) rather than the more visible, centrally-
reviewed Pydantic-Settings convention the other registered flags mostly
use. This check greps the travel-agent backend for that exact convention —
calls to `truthy_env(...)` / `falsy_env(...)` / `_truthy(...)` with a
literal ALL_CAPS name — and fails if the name isn't a registry row
(any status, so a `resolved` flag whose call site hasn't been deleted yet
doesn't re-trigger). It deliberately does NOT try to catch the
Pydantic-Settings convention (raw `os.environ.get`/`os.getenv` scattered
across ~150 non-flag config reads) — that convention centralizes flags in
a handful of `settings.py` files reviewed as a whole, which is exactly why
it wasn't the blind spot; a naive "every os.getenv site needs a registry
row" rule would drown in false positives on ordinary config (DATABASE_URL,
API keys, etc.) rather than sharpening the actual gap.

Usage::

    python3 scripts/check_flag_registry.py
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
_REGISTRY = _REPO / "docs" / "flags" / "registry.yaml"
_AGENT_BACKEND = _REPO / "travel-agent" / "backend"

# Matches the ad-hoc-lever convention: a literal ALL_CAPS name passed
# directly to one of the three flag-read helpers. Does NOT match
# `composition/core.py`'s unrelated local `_truthy(value)` (a generic
# string-to-bool coercer over an already-resolved value, never called with
# a literal name) or any Pydantic-Settings-style flag definition.
_FLAG_CALL = re.compile(r"\b(?:truthy_env|falsy_env|_truthy)\(\s*[\"']([A-Z][A-Z0-9_]*)[\"']")


def _load_flags() -> list[dict]:
    data = yaml.safe_load(_REGISTRY.read_text()) or {}
    return data.get("flags", [])


def _scan_ad_hoc_flag_calls() -> dict[str, list[str]]:
    """Find every `truthy_env`/`falsy_env`/`_truthy` call site with a
    literal flag name under the travel-agent backend. Returns
    ``{flag_name: ["path/to/file.py:123", ...]}``. Empty dict (not an
    error) when the travel-agent repo isn't checked out at this sibling
    path — this script must still run standalone for the expiry check."""
    if not _AGENT_BACKEND.is_dir():
        return {}

    sites: dict[str, list[str]] = {}
    for path in _AGENT_BACKEND.rglob("*.py"):
        parts = path.relative_to(_AGENT_BACKEND).parts
        if "tests" in parts or "__pycache__" in parts:
            continue
        text = path.read_text(errors="ignore")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in _FLAG_CALL.finditer(line):
                rel = path.relative_to(_REPO / "travel-agent")
                sites.setdefault(m.group(1), []).append(f"{rel}:{lineno}")
    return sites


def _check_unregistered_flags(flags: list[dict]) -> list[tuple[str, list[str]]]:
    registered = {f["name"] for f in flags if "name" in f}
    found = _scan_ad_hoc_flag_calls()
    return sorted(
        (name, sites) for name, sites in found.items() if name not in registered
    )


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

    ok = True

    if overdue:
        ok = False
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
    else:
        print(f"OK — {len(flags)} flags checked, none overdue.")

    unregistered = _check_unregistered_flags(flags)
    if unregistered:
        ok = False
        print(
            f"\n{len(unregistered)} flag(s) read in travel-agent/backend but missing from "
            "the registry:",
            file=sys.stderr,
        )
        for name, sites in unregistered:
            print(f"  - {name}", file=sys.stderr)
            for site in sites[:3]:
                print(f"      {site}", file=sys.stderr)
            if len(sites) > 3:
                print(f"      … and {len(sites) - 3} more", file=sys.stderr)
        print(
            f"\nAdd a row to {_REGISTRY.relative_to(_REPO)} for each (owner, expires, "
            "category, notes) — see the file header for field meanings.",
            file=sys.stderr,
        )
    elif _AGENT_BACKEND.is_dir():
        print("OK — no unregistered ad-hoc flags found in travel-agent/backend.")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
