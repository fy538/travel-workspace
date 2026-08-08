#!/usr/bin/env python3
"""Run a required pytest selection and fail if it is skipped.

The standard pytest exit status treats a skipped test as successful. That is a
reasonable default for optional infrastructure, but not for a certification
gate that says a database-backed journey was exercised. This wrapper writes a
temporary JUnit report, preserves pytest's normal output, and turns any skip
into a non-zero exit once pytest itself has passed.

Usage:
    python scripts/run_required_pytest.py --cwd travel-agent -- \\
      env SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest tests/scenarios/ -q
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


def skipped_cases(report: Path) -> list[str]:
    """Return stable test identifiers and reasons from a JUnit report."""
    root = ET.parse(report).getroot()
    skipped: list[str] = []
    for case in root.iter("testcase"):
        node = case.find("skipped")
        if node is None:
            continue
        identity = f"{case.get('classname', '')}::{case.get('name', '')}".strip(":")
        reason = (node.get("message") or (node.text or "")).strip()
        skipped.append(f"{identity} ({reason})" if reason else identity)
    return skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path, required=True, help="directory in which to run pytest")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="pytest command after --")
    args = parser.parse_args(argv)

    command = list(args.command)
    if command[:1] == ["--"]:
        command = command[1:]
    if not command:
        parser.error("provide a pytest command after --")
    if not args.cwd.is_dir():
        parser.error(f"--cwd does not exist: {args.cwd}")

    with tempfile.TemporaryDirectory(prefix="required-pytest-") as tmp:
        report = Path(tmp) / "junit.xml"
        result = subprocess.run(
            [*command, f"--junitxml={report}"],
            cwd=args.cwd,
            check=False,
        )
        # Preserve an assertion/import/collection failure as-is. The skip
        # report is only meaningful if pytest completed otherwise successfully.
        if result.returncode:
            return result.returncode
        if not report.exists():
            print("✗ required pytest produced no JUnit report", file=sys.stderr)
            return 2
        skips = skipped_cases(report)
        if not skips:
            return 0
        print("✗ required pytest unexpectedly skipped test(s):", file=sys.stderr)
        for case in skips:
            print(f"  - {case}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
