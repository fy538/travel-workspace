#!/usr/bin/env python3
"""Offline validation gate for the Maestro visual-QA flows.

Maestro's full visual run needs a macOS runner + iOS simulator + a built app
(see `.github/workflows/visual-qa.yml`), so it can't gate every PR. This cheap,
hermetic check *can* run on the standard Ubuntu CI job and catches the
"broken visual gate merged" class that a full run would only find later:

  1. Every `.maestro/**/*.yaml` flow parses as YAML (multi-doc aware).
  2. Every flow file referenced by a `visual-qa*` script in package.json
     actually exists on disk — so a renamed/deleted flow can't silently drop
     out of `certify-visual` / `visual-qa:wedge` and leave the wedge gate
     pointing at nothing.

Exit code is non-zero on any failure, with an actionable message.

Usage:
    python scripts/validate-maestro-flows.py [--app-dir travel-app]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


def _parse_all_flows(maestro_dir: Path) -> list[str]:
    """Return a list of parse-failure messages (empty == all flows valid)."""
    failures: list[str] = []
    flows = sorted(maestro_dir.rglob("*.yaml"))
    for flow in flows:
        try:
            list(yaml.safe_load_all(flow.read_text(encoding="utf-8")))
        except Exception as exc:  # noqa: BLE001 — surface any parse error
            first_line = str(exc).splitlines()[0] if str(exc) else exc.__class__.__name__
            failures.append(f"{flow}: {first_line}")
    return flows, failures


def _referenced_flows(app_dir: Path) -> dict[str, list[str]]:
    """Map each `visual-qa*` package.json script → the .maestro paths it names."""
    pkg = json.loads((app_dir / "package.json").read_text(encoding="utf-8"))
    scripts: dict[str, str] = pkg.get("scripts", {})
    flow_re = re.compile(r"\.maestro/[\w./-]+\.yaml")
    out: dict[str, list[str]] = {}
    for name, body in scripts.items():
        if not name.startswith("visual-qa"):
            continue
        refs = flow_re.findall(body)
        if refs:
            out[name] = refs
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--app-dir",
        default="travel-app",
        help="Path to the travel-app repo root (default: travel-app)",
    )
    args = parser.parse_args()

    app_dir = Path(args.app_dir).resolve()
    maestro_dir = app_dir / ".maestro"
    if not maestro_dir.is_dir():
        print(f"::error::No .maestro/ directory under {app_dir}", file=sys.stderr)
        return 1

    flows, parse_failures = _parse_all_flows(maestro_dir)
    print(f"Parsed {len(flows)} Maestro flow file(s).")

    missing: list[str] = []
    referenced = _referenced_flows(app_dir)
    for script_name, refs in referenced.items():
        for ref in refs:
            if not (app_dir / ref).is_file():
                missing.append(f"{script_name} → {ref} (not found)")

    if not referenced:
        missing.append(
            "package.json has no visual-qa script with explicit .maestro/*.yaml references"
        )

    ok = not parse_failures and not missing
    if parse_failures:
        print(f"\n✗ {len(parse_failures)} flow(s) failed to parse:", file=sys.stderr)
        for msg in parse_failures:
            print(f"  - {msg}", file=sys.stderr)
    if missing:
        print(
            "\n✗ package.json visual-qa script(s) reference missing flow file(s):",
            file=sys.stderr,
        )
        for msg in missing:
            print(f"  - {msg}", file=sys.stderr)
        print(
            "  (a renamed/deleted flow silently breaks the wedge gate — "
            "fix the script or restore the flow)",
            file=sys.stderr,
        )

    if ok:
        n_refs = sum(len(v) for v in referenced.values())
        print(
            f"✓ all flows parse; {n_refs} visual-qa script reference(s) "
            f"across {len(referenced)} script(s) resolve."
        )
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
