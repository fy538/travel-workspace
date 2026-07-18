from __future__ import annotations

from pathlib import Path

import yaml

import sync_journey_status as subject


def _journey(*branches: dict) -> dict:
    return {"id": "J99", "branches": list(branches)}


def test_branch_fidelity_cell_distinguishes_complete_partial_and_absent() -> None:
    existing = "docs/journeys/journeys.yaml"
    complete = _journey(
        {
            "id": "J99.B01",
            "required_evidence": ["FE"],
            "evidence": {"FE": [existing]},
        },
        {
            "id": "J99.B02",
            "required_evidence": ["FE"],
            "evidence": {"FE": [existing]},
        },
    )
    assert subject._branch_fidelity_cell(complete, "FE", {}) == "✅ 2/2"

    complete["branches"][1]["evidence"]["FE"] = []
    assert subject._branch_fidelity_cell(complete, "FE", {}) == "◐ 1/2"
    assert subject._branch_fidelity_cell(complete, "BE", {}) is None


def test_branch_fidelity_cell_surfaces_failed_lived_evidence() -> None:
    journey = _journey(
        {
            "id": "J99.B01",
            "required_evidence": ["LIVE"],
            "evidence": {"LIVE": ["persona-cert:J01"]},
        }
    )
    assert subject._branch_fidelity_cell(journey, "LIVE", {"J01": {"status": "fail"}}) == "🔴 0/1"


def test_trial_branch_registry_reports_expected_honest_fractions() -> None:
    manifest = yaml.safe_load(
        (Path(__file__).parents[1] / "docs" / "journeys" / "journeys.yaml").read_text()
    )
    journeys = {journey["id"]: journey for journey in manifest["journeys"]}
    lived = {
        "J05": {"status": "pass"},
        "J08": {"status": "pass"},
        "J10": {"status": "pass"},
        "J11": {"status": "pass"},
    }

    assert subject._branch_fidelity_cell(journeys["J06"], "VIS", lived) == "◐ 4/7"
    assert subject._branch_fidelity_cell(journeys["J10"], "LIVE", lived) == "◐ 2/8"
    assert subject._branch_fidelity_cell(journeys["J11"], "VIS", lived) == "✅ 6/6"
    assert subject._branch_fidelity_cell(journeys["J11"], "LIVE", lived) == "◐ 1/6"


def test_journey_set_is_derived_from_the_manifest() -> None:
    assert len(subject._ALL_JOURNEYS) == 28
    assert subject._ALL_JOURNEYS[0] == "J01"
    assert subject._ALL_JOURNEYS[-1] == "J28"
