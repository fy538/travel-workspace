from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

import pytest


SCRIPT = Path(__file__).with_name("check_convergence_candidate.py")
SPEC = importlib.util.spec_from_file_location("check_convergence_candidate", SCRIPT)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def _manifest() -> dict:
    sha = "a" * 40
    return {
        "schema_version": 1,
        "program": "convergence-ai-next-round-2026-08-10",
        "status": "assembling",
        "base": {key: sha for key in subject.SHA_KEYS},
        "lanes": {
            lane: {"branch": f"codex/{lane}", **{key: None for key in subject.SHA_KEYS}}
            for lane in subject.LANES
        },
        "candidate": {
            **{key: None for key in subject.SHA_KEYS},
            "migration_revision": None,
            "backend_deploy_digest": None,
            "app_build_id": None,
            "seed_corpus_hash": None,
        },
        "controls": {
            "shadow_default": "off",
            "shadow_surface": "private_trip_concierge",
            "shadow_allowed_actions": [
                "ask_attribute",
                "show_options",
                "recommend",
                "abstain",
            ],
            "group_visible_ai_dl": "off",
            "durable_inferred_learning": "off",
            "proactive_delivery": "off",
        },
        "evidence": {"source": "not_run", "physical": "not_run"},
        "external_blockers": ["two_physical_devices_and_identities"],
    }


def test_assembling_manifest_is_valid_without_false_evidence() -> None:
    subject.validate_manifest(_manifest())


def test_ready_requires_all_lane_heads_and_candidate_revisions() -> None:
    manifest = _manifest()
    manifest["status"] = "ready"
    with pytest.raises(subject.CandidateError, match="pinned lane heads"):
        subject.validate_manifest(manifest)


def _pinned_manifest(*, status: str) -> dict:
    manifest = _manifest()
    manifest["status"] = status
    sha = "b" * 40
    for lane in manifest["lanes"].values():
        lane.update({key: sha for key in subject.SHA_KEYS})
    manifest["candidate"].update({key: sha for key in subject.SHA_KEYS})
    return manifest


def test_deployed_requires_exact_deployment_identity() -> None:
    manifest = _pinned_manifest(status="deployed")
    manifest["evidence"]["staging"] = "pass"
    with pytest.raises(subject.CandidateError, match="deployment identity"):
        subject.validate_manifest(manifest)


def test_observed_requires_an_observation_layer() -> None:
    manifest = _pinned_manifest(status="observed")
    manifest["candidate"].update(
        {
            "migration_revision": "20260810_01",
            "backend_deploy_digest": "sha256:backend",
            "app_build_id": "eas-build-123",
            "seed_corpus_hash": "sha256:seed",
        }
    )
    manifest["evidence"]["staging"] = "pass"
    with pytest.raises(subject.CandidateError, match="observed candidate"):
        subject.validate_manifest(manifest)


def test_assembling_manifest_rejects_pass_evidence() -> None:
    manifest = _manifest()
    manifest["evidence"]["source"] = "pass"
    with pytest.raises(subject.CandidateError, match="cannot claim passing"):
        subject.validate_manifest(manifest)


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("shadow_default", "on"),
        ("group_visible_ai_dl", "on"),
        ("durable_inferred_learning", "on"),
        ("proactive_delivery", "on"),
    ],
)
def test_round_controls_remain_dark(key: str, value: str) -> None:
    manifest = copy.deepcopy(_manifest())
    manifest["controls"][key] = value
    with pytest.raises(subject.CandidateError):
        subject.validate_manifest(manifest)


def test_workspace_projection_requires_single_parent_and_manifest_only(monkeypatch) -> None:
    candidate_sha = "a" * 40
    projection_sha = "b" * 40
    outputs = iter(
        [
            f"{projection_sha} {candidate_sha}\n",
            "docs/working/convergence-ai-next-round-candidate-2026-08-10.json\n",
        ]
    )
    monkeypatch.setattr(subject.subprocess, "check_output", lambda *args, **kwargs: next(outputs))
    assert subject._workspace_projection_matches(
        subject_sha=candidate_sha, actual_sha=projection_sha
    )


def test_workspace_projection_rejects_product_change(monkeypatch) -> None:
    candidate_sha = "a" * 40
    projection_sha = "b" * 40
    outputs = iter(
        [
            f"{projection_sha} {candidate_sha}\n",
            "backend/product.py\n",
        ]
    )
    monkeypatch.setattr(subject.subprocess, "check_output", lambda *args, **kwargs: next(outputs))
    assert not subject._workspace_projection_matches(
        subject_sha=candidate_sha, actual_sha=projection_sha
    )
