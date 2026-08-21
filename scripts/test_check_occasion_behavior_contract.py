from __future__ import annotations

import json
from pathlib import Path

import yaml

from check_occasion_behavior_contract import validate_contract


def _write_contracts(tmp_path: Path) -> tuple[Path, Path]:
    case = {
        "case_id": "OCCASION-01",
        "name": "example-case",
        "phase": "before",
        "topology_fixture": "example-topology",
        "plan_lifecycle": "pre_trip",
        "treatment": "chat",
        "expected_visible_treatment": True,
    }
    backend = tmp_path / "backend.yaml"
    backend.write_text(
        yaml.safe_dump(
            {"portfolio_version": "occasion-behavior-portfolio-v1", "cases": [case]}
        ),
        encoding="utf-8",
    )
    app = tmp_path / "app.json"
    app.write_text(
        json.dumps(
            {
                "contract_version": "occasion-behavior-app-v1",
                "source_portfolio": "occasion-behavior-portfolio-v1",
                "cases": [case],
            }
        ),
        encoding="utf-8",
    )
    return backend, app


def test_matching_contract_passes(tmp_path: Path) -> None:
    backend, app = _write_contracts(tmp_path)

    assert validate_contract(backend, app) == []


def test_semantic_drift_fails(tmp_path: Path) -> None:
    backend, app = _write_contracts(tmp_path)
    payload = json.loads(app.read_text(encoding="utf-8"))
    payload["cases"][0]["treatment"] = "silence"
    app.write_text(json.dumps(payload), encoding="utf-8")

    assert validate_contract(backend, app) == [
        "mobile occasion cases do not exactly match backend order and semantics"
    ]
