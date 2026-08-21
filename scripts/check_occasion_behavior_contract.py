#!/usr/bin/env python3
"""Verify the mobile occasion gallery is bound to backend portfolio semantics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP = ROOT / "travel-app/constants/mocks/occasionBehaviorContract.json"


def compile_expected_contract() -> dict[str, object]:
    backend_root = ROOT / "travel-agent"
    sys.path.insert(0, str(backend_root))
    from tools.dogfood.content.occasion_behavior_projection import (  # noqa: PLC0415
        compile_mobile_contract,
    )

    return compile_mobile_contract()


def validate_contract(app_path: Path, expected: dict[str, object]) -> list[str]:
    app = json.loads(app_path.read_text(encoding="utf-8"))
    if app != expected:
        return ["mobile occasion contract is not the exact compiled backend projection"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", type=Path, default=DEFAULT_APP)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = compile_expected_contract()
    if args.write:
        args.app.write_text(
            json.dumps(expected, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"wrote occasion behavior contract: {args.app}")
        return 0
    errors = validate_contract(args.app, expected)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("occasion behavior contract: mobile is the exact compiled backend projection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
