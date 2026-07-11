#!/usr/bin/env python3
"""Run workspace documentation governance checks from one entry point.

Replaces invoking six separate scripts (and nine Makefile targets) individually.
Individual scripts remain for focused debugging; ``make docs-check`` and CI call
this wrapper.

Usage:
    python3 scripts/check_docs.py --all
    python3 scripts/check_docs.py --governance --inventory
    python3 scripts/check_docs.py --staged-new   # pre-commit: new staged docs only
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable

CHECKS: dict[str, list[str]] = {
    "governance": [PYTHON, "scripts/check_doc_governance.py", "--local-new"],
    "child-governance": [PYTHON, "scripts/check_child_doc_governance.py"],
    "inventory": [PYTHON, "scripts/check_doc_inventory.py", "--steady"],
    "spine": [PYTHON, "scripts/check_docs_spine.py"],
    "status": [PYTHON, "scripts/render_current_state.py"],
    "links": [PYTHON, "scripts/check_living_doc_links.py"],
}


def _run(name: str, argv: list[str]) -> int:
    print(f"▸ docs:{name}", flush=True)
    proc = subprocess.run(argv, cwd=ROOT)
    return proc.returncode


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="run every steady-state governance check (default when no flags)",
    )
    for name in CHECKS:
        parser.add_argument(f"--{name.replace('_', '-')}", action="store_true")
    parser.add_argument(
        "--staged-new",
        action="store_true",
        help="pre-commit mode: only validate newly staged workspace docs",
    )
    parser.add_argument(
        "--write-status",
        action="store_true",
        help="regenerate docs/current-state signals (make docs-status-sync)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    selected = [name for name in CHECKS if getattr(args, name.replace("-", "_"), False)]
    if args.staged_new:
        return _run(
            "governance-staged",
            [PYTHON, "scripts/check_doc_governance.py", "--staged-new"],
        )
    if args.write_status:
        return _run("status-sync", [PYTHON, "scripts/render_current_state.py", "--write"])
    if not selected and not args.all:
        selected = list(CHECKS)

    exit_code = 0
    for name in selected:
        code = _run(name, CHECKS[name])
        if code != 0:
            exit_code = code
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
