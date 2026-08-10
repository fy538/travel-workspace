from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import promote_journey_evidence as subject


def _receipt(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema_version": 2,
        "run_id": "jr-1",
        "recorded_at": "2026-08-10T12:00:00+00:00",
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
        "layer": "contract",
        "environment": "CI",
        "journeys": ["P01"],
        "command": "npx jest P01",
        "status": "pass",
    }
    return {**base, **overrides}


def test_receipt_digest_is_stable_and_ignores_local_path() -> None:
    receipt = _receipt(_path="/tmp/receipt.json")
    same = _receipt(_path="/another/path.json")
    assert subject.receipt_digest(receipt) == subject.receipt_digest(same)
    assert subject.receipt_digest(receipt).startswith("sha256:")


def test_build_index_promotes_only_current_passes() -> None:
    revisions = {
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    index = subject.build_index(
        [
            _receipt(),
            _receipt(run_id="old", app_sha="app-old"),
            _receipt(run_id="failed", status="fail"),
        ],
        revisions,
    )
    assert index["candidate"] == revisions
    assert len(index["attestations"]) == 1
    assert index["attestations"][0]["receipt"]["run_id"] == "jr-1"


def test_build_index_rejects_dirty_candidate() -> None:
    revisions = {
        "workspace_sha": "workspace-current-dirty",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    try:
        subject.build_index([], revisions)
    except ValueError as exc:
        assert "clean workspace" in str(exc)
    else:
        raise AssertionError("expected dirty candidate promotion to fail")


def test_committed_empty_index_is_valid(tmp_path) -> None:
    path = tmp_path / "index.json"
    path.write_text(json.dumps({"schema_version": 1, "attestations": []}))
    assert subject.load_index(path)["attestations"] == []


def test_load_index_rejects_receipt_digest_mismatch(tmp_path: Path) -> None:
    receipt = _receipt()
    path = tmp_path / "index.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "candidate": {
                    "workspace_sha": "workspace-current",
                    "app_sha": "app-current",
                    "backend_sha": "backend-current",
                },
                "attestations": [
                    {"receipt_sha256": "sha256:" + "0" * 64, "receipt": receipt}
                ],
            }
        )
    )

    try:
        subject.load_index(path)
    except ValueError as exc:
        assert "digest mismatch" in str(exc)
    else:
        raise AssertionError("expected a forged receipt digest to fail")


def test_projection_commit_chain_keeps_subject_candidate_current(tmp_path: Path) -> None:
    index = {
        "candidate": {
            "workspace_sha": "subject-sha",
            "app_sha": "app-current",
            "backend_sha": "backend-current",
        }
    }
    current = {
        "workspace_sha": "projection-sha",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    with patch.object(
        subject,
        "_git_lines",
        side_effect=[
            [],
            ["docs/journeys/evidence-attestations.json", "docs/release/v1-scope.md"],
        ],
    ):
        assert subject.index_candidate_is_current(index, current, workspace_root=tmp_path)


def test_non_projection_commit_makes_subject_candidate_stale(tmp_path: Path) -> None:
    index = {
        "candidate": {
            "workspace_sha": "subject-sha",
            "app_sha": "app-current",
            "backend_sha": "backend-current",
        }
    }
    current = {
        "workspace_sha": "later-sha",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    with patch.object(
        subject,
        "_git_lines",
        side_effect=[[], ["Makefile"]],
    ):
        assert not subject.index_candidate_is_current(index, current, workspace_root=tmp_path)


def test_non_descendant_projection_diff_makes_subject_candidate_stale(tmp_path: Path) -> None:
    index = {
        "candidate": {
            "workspace_sha": "subject-sha",
            "app_sha": "app-current",
            "backend_sha": "backend-current",
        }
    }
    current = {
        "workspace_sha": "unrelated-sha",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    with patch.object(
        subject,
        "_git_lines",
        side_effect=subprocess.CalledProcessError(1, ["git", "merge-base"]),
    ):
        assert not subject.index_candidate_is_current(index, current, workspace_root=tmp_path)
