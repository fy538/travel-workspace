#!/usr/bin/env python3
"""Feature-flag registry guard — checks the canonical registry
(docs/flags/registry.yaml) against both child repositories.

The guard checks expiry dates, backend ad-hoc env-flag calls, and direct app
flag constants in ``travel-app/constants/featureFlags.ts``. The mobile
convention is deliberately narrow: app flags must be direct ``export const``
declarations in that canonical module and must end in ``_ENABLED`` or
``_STUB``. This avoids treating arbitrary Expo configuration (billing, map
styles, API URLs, and similar settings) as a feature flag. Re-exports from
helper modules and inline environment reads are legacy exceptions until they
are moved behind the canonical module.

The default invocation is a full cross-repo check and fails closed when either
child checkout or the canonical mobile module is absent. Use ``--expiry-only``
only for a standalone registry-date check when child repositories are not
available. Pure file-parse, NO DB — runs at pre-push alongside the other
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
    python3 scripts/check_flag_registry.py --expiry-only
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
_REGISTRY = _REPO / "docs" / "flags" / "registry.yaml"
_AGENT_REPO = _REPO / "travel-agent"
_AGENT_BACKEND = _REPO / "travel-agent" / "backend"
_APP_REPO = _REPO / "travel-app"
_APP_FLAG_FILE = _APP_REPO / "constants" / "featureFlags.ts"

# Matches the ad-hoc-lever convention: a literal ALL_CAPS name passed
# directly to one of the three flag-read helpers. Does NOT match
# `composition/core.py`'s unrelated local `_truthy(value)` (a generic
# string-to-bool coercer over an already-resolved value, never called with
# a literal name) or any Pydantic-Settings-style flag definition.
_FLAG_CALL = re.compile(r"\b(?:truthy_env|falsy_env|_truthy)\(\s*[\"']([A-Z][A-Z0-9_]*)[\"']")

# The mobile flag convention is intentionally anchored to the canonical
# module. A normal exported constant in that file is not necessarily a flag
# (for example, ``INTERNAL_BUILD`` is private), so require a lifecycle suffix.
_APP_FLAG_DECLARATION = re.compile(
    r"^\s*export\s+const\s+([A-Z][A-Z0-9_]*(?:_ENABLED|_STUB))\b"
)


def _load_flags() -> list[dict]:
    data = yaml.safe_load(_REGISTRY.read_text()) or {}
    return data.get("flags", [])


def _scan_ad_hoc_flag_calls(
    backend_root: Path = _AGENT_BACKEND,
    workspace_root: Path = _REPO,
) -> dict[str, list[str]]:
    """Find every `truthy_env`/`falsy_env`/`_truthy` call site with a
    literal flag name under the travel-agent backend. Returns
    ``{flag_name: ["path/to/file.py:123", ...]}``. Empty dict (not an
    error) when the travel-agent repo isn't checked out at this sibling
    path — this script must still run standalone for the expiry check."""
    if not backend_root.is_dir():
        return {}

    sites: dict[str, list[str]] = {}
    for path in backend_root.rglob("*.py"):
        parts = path.relative_to(backend_root).parts
        if "tests" in parts or "__pycache__" in parts:
            continue
        text = path.read_text(errors="ignore")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in _FLAG_CALL.finditer(line):
                rel = path.relative_to(workspace_root)
                sites.setdefault(m.group(1), []).append(f"{rel}:{lineno}")
    return sites


def _scan_app_flag_declarations(
    flag_file: Path = _APP_FLAG_FILE,
    workspace_root: Path = _REPO,
) -> dict[str, list[str]]:
    """Find canonical mobile flag declarations.

    The source file is intentionally a single explicit input rather than a
    repository-wide environment-variable grep. This keeps ordinary Expo
    configuration out of the feature-flag lifecycle check and makes the
    convention easy for an engineer to discover.
    """
    if not flag_file.is_file():
        return {}

    sites: dict[str, list[str]] = {}
    rel = flag_file.relative_to(workspace_root)
    for lineno, line in enumerate(flag_file.read_text(errors="ignore").splitlines(), start=1):
        match = _APP_FLAG_DECLARATION.match(line)
        if match:
            sites.setdefault(match.group(1), []).append(f"{rel}:{lineno}")
    return sites


def _missing_cross_repo_inputs(
    agent_repo: Path = _AGENT_REPO,
    agent_backend: Path = _AGENT_BACKEND,
    app_repo: Path = _APP_REPO,
    app_flag_file: Path = _APP_FLAG_FILE,
) -> list[str]:
    """Return missing inputs required by the default full check."""
    missing: list[str] = []
    if not agent_repo.is_dir():
        missing.append("travel-agent/")
    elif not agent_backend.is_dir():
        missing.append("travel-agent/backend/")
    if not app_repo.is_dir():
        missing.append("travel-app/")
    elif not app_flag_file.is_file():
        missing.append("travel-app/constants/featureFlags.ts")
    return missing


def _check_unregistered_flags(
    flags: list[dict],
    *,
    backend_root: Path = _AGENT_BACKEND,
    app_flag_file: Path = _APP_FLAG_FILE,
    workspace_root: Path = _REPO,
) -> list[tuple[str, list[str]]]:
    registered = {f["name"] for f in flags if "name" in f}
    found: dict[str, list[str]] = {}
    for source in (
        _scan_ad_hoc_flag_calls(backend_root, workspace_root),
        _scan_app_flag_declarations(app_flag_file, workspace_root),
    ):
        for name, sites in source.items():
            found.setdefault(name, []).extend(sites)
    return sorted(
        (name, sites) for name, sites in found.items() if name not in registered
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--expiry-only",
        action="store_true",
        help="check registry dates without requiring child repositories",
    )
    args = parser.parse_args(argv)

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

    if args.expiry_only:
        print("SKIP — child-repository flag discovery (--expiry-only).")
        return 0 if ok else 1

    missing = _missing_cross_repo_inputs(
        _AGENT_REPO, _AGENT_BACKEND, _APP_REPO, _APP_FLAG_FILE
    )
    if missing:
        ok = False
        print(
            "\nCROSS-REPO FLAG CHECK BLOCKED: required child input(s) missing:",
            file=sys.stderr,
        )
        for path in missing:
            print(f"  - {path}", file=sys.stderr)
        print(
            "\nThe full check fails closed. Check out both child repositories, or "
            "run --expiry-only for registry-date validation only.",
            file=sys.stderr,
        )
        return 1

    unregistered = _check_unregistered_flags(
        flags,
        backend_root=_AGENT_BACKEND,
        app_flag_file=_APP_FLAG_FILE,
        workspace_root=_REPO,
    )
    if unregistered:
        ok = False
        print(
            f"\n{len(unregistered)} flag(s) discovered in the backend or canonical "
            "mobile flag module but missing from the registry:",
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
    else:
        print("OK — no unregistered backend or mobile flags found.")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
