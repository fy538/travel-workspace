from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import journey_evidence as subject


def _receipt(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "schema_version": subject.SCHEMA_VERSION,
        "run_id": "jr-1",
        "recorded_at": "2026-08-07T12:00:00+00:00",
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
        "layer": "contract",
        "environment": "local",
        "journeys": ["P01"],
        "command": "dogfood-fast deterministic product-proof contracts",
        "status": "pass",
        "runner_id": "dogfood-fast-contract-v1",
        "runner_sha256": subject.runner_digest("dogfood-fast-contract-v1"),
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
    assert (
        subject.evidence_state(
            [_receipt(app_sha="app-old")], "P01", "contract", revisions
        )
        == "stale"
    )


def test_newer_receipt_supersedes_an_older_failure() -> None:
    revisions = {
        "workspace_sha": "workspace-current",
        "app_sha": "app-current",
        "backend_sha": "backend-current",
    }
    failed = _receipt(status="fail", recorded_at="2026-08-07T10:00:00+00:00")
    passed = _receipt(status="pass", recorded_at="2026-08-07T10:01:00+00:00")

    assert (
        subject.evidence_state([failed, passed], "P01", "contract", revisions) == "pass"
    )


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


def test_passing_receipt_requires_a_governed_runner() -> None:
    receipt = _receipt()
    receipt.pop("runner_id")
    receipt.pop("runner_sha256")

    try:
        subject.validate_receipt(receipt)
    except subject.ReceiptError as exc:
        assert "runner_id" in str(exc)
    else:
        raise AssertionError("expected an unbound passing receipt to fail validation")


def test_governed_runner_rejects_an_arbitrary_command_label() -> None:
    try:
        subject.validate_runner_binding(
            runner_id="dogfood-fast-contract-v1",
            layer="contract",
            journeys=["P01"],
            command="true",
        )
    except subject.ReceiptError as exc:
        assert "requires receipt command" in str(exc)
    else:
        raise AssertionError("expected an arbitrary no-op command to fail binding")


def test_proof_receipt_rejects_an_unrequired_layer() -> None:
    try:
        subject.validate_receipt(_receipt(layer="staging"))
    except subject.ReceiptError as exc:
        assert "not required" in str(exc)
    else:
        raise AssertionError("expected proof/layer drift to fail validation")


def test_blocked_receipt_requires_a_reason() -> None:
    try:
        subject.validate_receipt(_receipt(status="blocked"))
    except subject.ReceiptError as exc:
        assert "skip_reason" in str(exc)
    else:
        raise AssertionError(
            "expected a blocked receipt without a reason to fail validation"
        )


def test_revision_marks_tracked_modifications_as_dirty(tmp_path: Path) -> None:
    with (
        patch.object(
            subject.subprocess,
            "check_output",
            side_effect=["abc123\n", " M tracked.py\n"],
        ),
    ):
        assert subject._revision(tmp_path) == "abc123-dirty"


def test_passing_receipt_rejects_dirty_revision() -> None:
    try:
        subject.validate_receipt(_receipt(workspace_sha="workspace-current-dirty"))
    except subject.ReceiptError as exc:
        assert "clean repository revisions" in str(exc)
    else:
        raise AssertionError("expected a dirty passing receipt to fail validation")


def test_physical_receipt_requires_build_and_artifact_identity() -> None:
    try:
        subject.validate_receipt(
            _receipt(
                layer="physical",
                journeys=["J04"],
                command="RUN_LIVE=1 scripts/dogfood-device-cert-live.sh",
                runner_id="physical-j04-j10-v1",
                runner_sha256=subject.runner_digest("physical-j04-j10-v1"),
            )
        )
    except subject.ReceiptError as exc:
        assert "physical receipts require" in str(exc)
    else:
        raise AssertionError("expected an incomplete physical receipt to fail")


def test_valid_physical_receipt_accepts_explicit_identity() -> None:
    receipt = _receipt(
        layer="physical",
        journeys=["J04"],
        command="RUN_LIVE=1 scripts/dogfood-device-cert-live.sh",
        runner_id="physical-j04-j10-v1",
        runner_sha256=subject.runner_digest("physical-j04-j10-v1"),
        app_build_id="eas-build-123",
        backend_deploy_digest="fly-release-456",
        migration_revision="20260810_01",
        seed_corpus_hash="sha256:" + "a" * 64,
        devices=[
            "ios|00008110-REAL|iPhone 15 / iOS 18.6",
            "android|R58N-REAL|Pixel 9 / Android 16",
        ],
        identities=["founder-a", "founder-b"],
        oracle_hash="sha256:" + "b" * 64,
        flow_hash="sha256:" + "c" * 64,
        reviewer="feihuyan",
        artifacts=[{"name": "maestro-video", "sha256": "sha256:" + "d" * 64}],
    )
    subject.validate_receipt(receipt)


def test_physical_receipt_rejects_single_or_duplicate_hardware() -> None:
    receipt = _receipt(
        layer="physical",
        journeys=["J04"],
        command="RUN_LIVE=1 scripts/dogfood-device-cert-live.sh",
        runner_id="physical-j04-j10-v1",
        runner_sha256=subject.runner_digest("physical-j04-j10-v1"),
        app_build_id="eas-build-123",
        backend_deploy_digest="fly-release-456",
        migration_revision="20260810_01",
        seed_corpus_hash="sha256:" + "a" * 64,
        devices=["ios|00008110-REAL|iPhone 15 / iOS 18.6"],
        identities=["founder-a", "founder-b"],
        oracle_hash="sha256:" + "b" * 64,
        flow_hash="sha256:" + "c" * 64,
        reviewer="feihuyan",
        artifacts=[{"name": "maestro-video", "sha256": "sha256:" + "d" * 64}],
    )
    try:
        subject.validate_receipt(receipt)
    except subject.ReceiptError as exc:
        assert "at least two" in str(exc)
    else:
        raise AssertionError("expected a single physical device to fail")

    receipt["devices"] = [
        "ios|00008110-REAL|iPhone 15 / iOS 18.6",
        "ios|00008110-REAL|iPhone 15 / iOS 18.6",
    ]
    try:
        subject.validate_receipt(receipt)
    except subject.ReceiptError as exc:
        assert "unique" in str(exc)
    else:
        raise AssertionError("expected duplicate physical devices to fail")
