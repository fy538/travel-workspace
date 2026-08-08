#!/usr/bin/env python3
"""Record and report commit-specific journey execution evidence.

Receipts are deliberately local/CI artifacts rather than committed status. A
test result only applies to the exact workspace, app, and backend revisions it
ran against. This tool records those revisions and reports PASS, FAIL, BLOCKED,
UNRUN, or STALE for the current checkout.

Examples:
    python scripts/journey_evidence.py record --layer contract --status pass \\
      --journey P01 --environment local --command 'npx jest ...'
    python scripts/journey_evidence.py report
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIRECTORY = ROOT / ".tmp" / "journey-evidence"
LAYERS = ("contract", "database", "device_mock", "persona_replay", "staging", "physical", "ai_eval")
STATUSES = ("pass", "fail", "blocked")
DISPLAY = {
    "pass": "PASS",
    "fail": "FAIL",
    "blocked": "BLOCKED",
    "unrun": "UNRUN",
    "stale": "STALE",
}


class ReceiptError(ValueError):
    """A receipt is incomplete or uses an unsupported value."""


def _revision(path: Path) -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=path, text=True, stderr=subprocess.DEVNULL
        ).strip()
        # A receipt for HEAD is not evidence for a checkout with tracked
        # modifications. Do not include untracked files: they may be a local
        # artifact, but tracked source/index changes can alter the behavior
        # the receipt is intended to prove.
        dirty = any(
            subprocess.run(
                command,
                cwd=path,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            for command in (
                ["git", "diff", "--quiet"],
                ["git", "diff", "--cached", "--quiet"],
            )
        )
        return f"{sha}-dirty" if dirty else sha
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def current_revisions() -> dict[str, str]:
    return {
        "workspace_sha": _revision(ROOT),
        "app_sha": _revision(ROOT / "travel-app"),
        "backend_sha": _revision(ROOT / "travel-agent"),
    }


def validate_receipt(receipt: dict[str, Any]) -> None:
    required = {
        "run_id",
        "recorded_at",
        "workspace_sha",
        "app_sha",
        "backend_sha",
        "layer",
        "environment",
        "journeys",
        "command",
        "status",
    }
    missing = sorted(required - receipt.keys())
    if missing:
        raise ReceiptError(f"missing required field(s): {', '.join(missing)}")
    if receipt["layer"] not in LAYERS:
        raise ReceiptError(f"unknown layer: {receipt['layer']!r}")
    if receipt["status"] not in STATUSES:
        raise ReceiptError(f"unknown status: {receipt['status']!r}")
    if receipt["status"] == "blocked" and not receipt.get("skip_reason"):
        raise ReceiptError("blocked receipts require skip_reason")
    journeys = receipt["journeys"]
    if not isinstance(journeys, list) or not journeys or not all(isinstance(j, str) and j for j in journeys):
        raise ReceiptError("journeys must be a non-empty list of identifiers")
    for key in ("run_id", "recorded_at", "workspace_sha", "app_sha", "backend_sha", "environment", "command"):
        if not isinstance(receipt[key], str) or not receipt[key]:
            raise ReceiptError(f"{key} must be a non-empty string")


def receipt_is_current(receipt: dict[str, Any], revisions: dict[str, str]) -> bool:
    return all(receipt.get(key) == value for key, value in revisions.items())


def load_receipts(directory: Path) -> list[dict[str, Any]]:
    if not directory.exists():
        return []
    receipts: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(path.read_text())
            validate_receipt(data)
        except (OSError, json.JSONDecodeError, ReceiptError) as exc:
            print(f"warning: ignoring invalid receipt {path}: {exc}", file=sys.stderr)
            continue
        data["_path"] = str(path)
        receipts.append(data)
    return receipts


def latest_receipt(
    receipts: list[dict[str, Any]], journey: str, layer: str
) -> dict[str, Any] | None:
    candidates = [r for r in receipts if r["layer"] == layer and journey in r["journeys"]]
    return max(candidates, key=lambda r: r["recorded_at"], default=None)


def evidence_state(
    receipts: list[dict[str, Any]], journey: str, layer: str, revisions: dict[str, str]
) -> str:
    receipt = latest_receipt(receipts, journey, layer)
    if receipt is None:
        return "unrun"
    if not receipt_is_current(receipt, revisions):
        return "stale"
    return receipt["status"]


def _record(args: argparse.Namespace) -> int:
    directory = args.directory.resolve()
    directory.mkdir(parents=True, exist_ok=True)
    receipt: dict[str, Any] = {
        "run_id": f"jr-{int(time.time())}-{uuid4().hex[:8]}",
        "recorded_at": datetime.now(UTC).isoformat(),
        **current_revisions(),
        "layer": args.layer,
        "environment": args.environment,
        "journeys": args.journey,
        "branches": args.branch,
        "command": args.command,
        "status": args.status,
        "duration_seconds": args.duration_seconds,
        "skip_reason": args.reason if args.status == "blocked" else None,
        "artifacts": args.artifact,
    }
    validate_receipt(receipt)
    path = directory / f"{receipt['recorded_at'].replace(':', '').replace('+', '_')}-{receipt['run_id']}.json"
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    try:
        display_path = path.relative_to(ROOT)
    except ValueError:
        display_path = path
    print(display_path)
    return 0


def _report(args: argparse.Namespace) -> int:
    receipts = load_receipts(args.directory.resolve())
    revisions = current_revisions()
    journeys = args.journey or sorted({j for receipt in receipts for j in receipt["journeys"]})
    if not journeys:
        print("No journey evidence receipts found. Record a run before relying on execution status.")
        return 0
    layers = args.layer or list(LAYERS)
    print("Journey evidence for current revisions")
    print("| Journey | " + " | ".join(layer.replace("_", " ") for layer in layers) + " |")
    print("|---|" + "|".join("---" for _ in layers) + "|")
    for journey in journeys:
        states = [DISPLAY[evidence_state(receipts, journey, layer, revisions)] for layer in layers]
        print(f"| {journey} | " + " | ".join(states) + " |")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    record = subparsers.add_parser("record", help="write one immutable execution receipt")
    record.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    record.add_argument("--layer", choices=LAYERS, required=True)
    record.add_argument("--status", choices=STATUSES, required=True)
    record.add_argument("--journey", action="append", required=True, help="journey or proof identifier; repeat")
    record.add_argument("--branch", action="append", default=[])
    record.add_argument("--environment", required=True, help="for example: local, CI, staging, founder-device")
    record.add_argument("--command", required=True)
    record.add_argument("--duration-seconds", type=float)
    record.add_argument("--reason", help="required context for a blocked run")
    record.add_argument("--artifact", action="append", default=[])
    record.set_defaults(func=_record)

    report = subparsers.add_parser("report", help="render evidence state for this checkout")
    report.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    report.add_argument("--journey", action="append")
    report.add_argument("--layer", choices=LAYERS, action="append")
    report.set_defaults(func=_report)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
