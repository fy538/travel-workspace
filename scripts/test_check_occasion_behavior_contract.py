from __future__ import annotations

import json
from pathlib import Path

from check_occasion_behavior_contract import validate_contract


def _write_contract(tmp_path: Path) -> tuple[dict[str, object], Path]:
    expected: dict[str, object] = {
        "contract_version": "occasion-behavior-app-v1",
        "source_portfolio": "occasion-behavior-portfolio-v1",
        "cases": [{"case_id": "OCCASION-01", "shape": {"viewer_id": "viewer"}}],
    }
    app = tmp_path / "app.json"
    app.write_text(json.dumps(expected), encoding="utf-8")
    return expected, app


def test_matching_contract_passes(tmp_path: Path) -> None:
    expected, app = _write_contract(tmp_path)

    assert validate_contract(app, expected) == []


def test_semantic_drift_fails(tmp_path: Path) -> None:
    expected, app = _write_contract(tmp_path)
    payload = json.loads(app.read_text(encoding="utf-8"))
    payload["cases"][0]["shape"]["viewer_id"] = "wrong-viewer"
    app.write_text(json.dumps(payload), encoding="utf-8")

    assert validate_contract(app, expected) == [
        "mobile occasion contract is not the exact compiled backend projection"
    ]
