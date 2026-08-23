#!/usr/bin/env python3
"""Run and report the five M0 contract gates.

The report is deliberately a thin orchestration layer: each gate remains
independently runnable and owns its own assertions.  This command answers the
M0 reachability question in CI—are the authority, API, flag, occasion, and
generated-state contracts actually executable from the workspace root?
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

GATES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("api-coverage", (sys.executable, "scripts/api_contract_audit.py")),
    ("contract", ("./scripts/contract-check.sh",)),
    ("flags", (sys.executable, "scripts/check_flag_registry.py")),
    (
        "occasion-behavior",
        ("travel-agent/.venv/bin/python", "scripts/check_occasion_behavior_contract.py"),
    ),
    ("generated-state", (sys.executable, "scripts/render_current_state.py")),
)


def run_gate(name: str, command: tuple[str, ...], timeout: float) -> dict[str, object]:
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        status = "pass" if completed.returncode == 0 else "fail"
        output = (completed.stdout + completed.stderr).strip()
        return {
            "name": name,
            "command": " ".join(command),
            "status": status,
            "returncode": completed.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "output_tail": output[-2000:],
        }
    except subprocess.TimeoutExpired as exc:
        output = ((exc.stdout or "") + (exc.stderr or "")).strip()
        return {
            "name": name,
            "command": " ".join(command),
            "status": "timeout",
            "returncode": None,
            "duration_seconds": round(time.monotonic() - started, 3),
            "output_tail": output[-2000:],
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--timeout",
        type=float,
        default=180.0,
        help="per-gate timeout in seconds (default: 180)",
    )
    args = parser.parse_args()

    results = [run_gate(name, command, args.timeout) for name, command in GATES]
    if args.json:
        print(json.dumps({"gates": results}, indent=2))
    else:
        for result in results:
            print(
                f"{result['status'].upper():7} {result['name']:<20} "
                f"({result['duration_seconds']}s)"
            )
            if result["status"] != "pass" and result["output_tail"]:
                print(result["output_tail"])

    return 0 if all(result["status"] == "pass" for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
