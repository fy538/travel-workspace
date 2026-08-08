from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import journey_evidence as subject


def _receipt(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "run_id": "jr-1",
        "recorded_at": "2026-08-07T12:00:00+00:00",
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
        "layer": "contract",
        "environment": "local",
        "journeys": ["P01"],
        "command": "npx jest P01",
        "status": "pass",
    }
    return {**base, **overrides}


def test_evidence_state_is_current_stale_or_unrun() -> None:
    revisions = {
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    receipt = _receipt()

    assert subject.evidence_state([receipt], "P01", "contract", revisions) == "pass"
    assert subject.evidence_state([receipt], "P01", "database", revisions) == "unrun"
    assert subject.evidence_state([_receipt(app_sha="app-old")], "P01", "contract", revisions) == "stale"


def test_newer_receipt_supersedes_an_older_failure() -> None:
    revisions = {
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    failed = _receipt(status="fail", recorded_at="2026-08-07T10:00:00+00:00")
    passed = _receipt(status="pass", recorded_at="2026-08-07T10:01:00+00:00")

    assert subject.evidence_state([failed, passed], "P01", "contract", revisions) == "pass"


def test_load_receipts_ignores_invalid_receipts(tmp_path: Path) -> None:
    valid = tmp_path / "valid.json"
    valid.write_text(__import__("json").dumps(_receipt()))
    (tmp_path / "invalid.json").write_text("not-json")

    receipts = subject.load_receipts(tmp_path)

    assert len(receipts) == 1
    assert receipts[0]["run_id"] == "jr-1"


def test_validate_receipt_requires_known_layer() -> None:
    try:
        subject.validate_receipt(_receipt(layer="live"))
    except subject.ReceiptError as exc:
        assert "unknown layer" in str(exc)
    else:
        raise AssertionError("expected an invalid layer to fail validation")


def test_blocked_receipt_requires_a_reason() -> None:
    try:
        subject.validate_receipt(_receipt(status="blocked"))
    except subject.ReceiptError as exc:
        assert "skip_reason" in str(exc)
    else:
        raise AssertionError("expected a blocked receipt without a reason to fail validation")


def test_revision_marks_tracked_modifications_as_dirty(tmp_path: Path) -> None:
    class _Result:
        def __init__(self, returncode: int) -> None:
            self.returncode = returncode

    with (
        patch.object(subject.subprocess, "check_output", return_value="abc123\n"),
        patch.object(subject.subprocess, "run", side_effect=[_Result(1), _Result(0)]),
    ):
        assert subject._revision(tmp_path) == "abc123-dirty"
