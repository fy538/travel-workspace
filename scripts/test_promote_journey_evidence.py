from __future__ import annotations

import json

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
