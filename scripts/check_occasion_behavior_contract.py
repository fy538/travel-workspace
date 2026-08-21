#!/usr/bin/env python3
"""Verify the mobile occasion gallery is bound to backend portfolio semantics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BACKEND = (
    ROOT / "travel-agent/tools/dogfood/content/occasion-behavior-portfolio-v1.yaml"
)
DEFAULT_APP = ROOT / "travel-app/constants/mocks/occasionBehaviorContract.json"
CONTRACT_VERSION = "occasion-behavior-app-v1"
SOURCE_PORTFOLIO = "occasion-behavior-portfolio-v1"
SEMANTIC_FIELDS = (
    "case_id",
    "name",
    "phase",
    "topology_fixture",
    "plan_lifecycle",
    "treatment",
    "expected_visible_treatment",
)


def validate_contract(backend_path: Path, app_path: Path) -> list[str]:
    backend = yaml.safe_load(backend_path.read_text(encoding="utf-8"))
    app = json.loads(app_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if app.get("contract_version") != CONTRACT_VERSION:
        errors.append(f"app contract_version must be {CONTRACT_VERSION}")
    if app.get("source_portfolio") != SOURCE_PORTFOLIO:
        errors.append(f"app source_portfolio must be {SOURCE_PORTFOLIO}")
    if backend.get("portfolio_version") != SOURCE_PORTFOLIO:
        errors.append(f"backend portfolio_version must be {SOURCE_PORTFOLIO}")

    expected = [
        {field: case.get(field) for field in SEMANTIC_FIELDS}
        for case in backend.get("cases", [])
    ]
    actual = [
        {field: case.get(field) for field in SEMANTIC_FIELDS}
        for case in app.get("cases", [])
    ]
    if actual != expected:
        errors.append("mobile occasion cases do not exactly match backend order and semantics")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", type=Path, default=DEFAULT_BACKEND)
    parser.add_argument("--app", type=Path, default=DEFAULT_APP)
    args = parser.parse_args()
    errors = validate_contract(args.backend, args.app)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("occasion behavior contract: backend and mobile semantics match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
