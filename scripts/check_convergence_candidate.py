#!/usr/bin/env python3
"""Validate the pinned convergence/AI integration-candidate manifest.

The manifest may remain ``assembling`` while lanes are active. A candidate can
advance to ``ready`` only when all lane heads and the final triple-SHA identity
are pinned. Higher evidence fields remain explicit and independent; this tool
never promotes a source or database result to device, human, AI, or causal
evidence.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = (
    ROOT / "docs" / "working" / "convergence-ai-next-round-candidate-2026-08-10.json"
)
SHA_KEYS = ("workspace_sha", "backend_sha", "app_sha")
LANES = {"causal_spine", "ai_evidence", "group_trip", "integration_evidence"}
STATUSES = {"assembling", "ready", "deployed", "observed"}
EVIDENCE_STATES = {"not_run", "blocked", "fail", "pass", "stale"}
DEPLOYED_STATUSES = {"deployed", "observed"}
CONTROL_OFF_KEYS = {
    "group_visible_ai_dl",
    "durable_inferred_learning",
    "proactive_delivery",
}
WORKSPACE_PROJECTION_PATHS = {
    "docs/working/convergence-ai-next-round-candidate-2026-08-10.json",
}


class CandidateError(ValueError):
    """The candidate manifest is incomplete or internally inconsistent."""


def _is_sha(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


def _require_exact_keys(value: Any, expected: set[str], *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CandidateError(f"{label} must be an object")
    keys = set(value)
    if keys != expected:
        missing = sorted(expected - keys)
        extra = sorted(keys - expected)
        raise CandidateError(f"{label} keys mismatch; missing={missing}, extra={extra}")
    return value


def validate_manifest(manifest: dict[str, Any]) -> None:
    if manifest.get("schema_version") != 1:
        raise CandidateError("schema_version must be 1")
    if manifest.get("program") != "convergence-ai-next-round-2026-08-10":
        raise CandidateError("unexpected program identifier")
    status = manifest.get("status")
    if status not in STATUSES:
        raise CandidateError(f"unsupported status: {status!r}")

    base = _require_exact_keys(manifest.get("base"), set(SHA_KEYS), label="base")
    for key in SHA_KEYS:
        if not _is_sha(base[key]):
            raise CandidateError(f"base.{key} must be a full lowercase Git SHA")

    lanes = _require_exact_keys(manifest.get("lanes"), LANES, label="lanes")
    lane_keys = {"branch", *SHA_KEYS}
    for lane_name, raw_lane in lanes.items():
        lane = _require_exact_keys(raw_lane, lane_keys, label=f"lanes.{lane_name}")
        if not isinstance(lane["branch"], str) or not lane["branch"].startswith("codex/"):
            raise CandidateError(f"lanes.{lane_name}.branch must be a codex/* branch")
        for key in SHA_KEYS:
            if lane[key] is not None and not _is_sha(lane[key]):
                raise CandidateError(f"lanes.{lane_name}.{key} must be null or a full Git SHA")

    candidate_keys = {
        *SHA_KEYS,
        "migration_revision",
        "backend_deploy_digest",
        "app_build_id",
        "seed_corpus_hash",
    }
    candidate = _require_exact_keys(
        manifest.get("candidate"), candidate_keys, label="candidate"
    )
    for key in SHA_KEYS:
        if candidate[key] is not None and not _is_sha(candidate[key]):
            raise CandidateError(f"candidate.{key} must be null or a full Git SHA")

    if status in DEPLOYED_STATUSES:
        deployment_keys = (
            "migration_revision",
            "backend_deploy_digest",
            "app_build_id",
            "seed_corpus_hash",
        )
        missing_deployment = [
            key
            for key in deployment_keys
            if not isinstance(candidate[key], str) or not candidate[key].strip()
        ]
        if missing_deployment:
            raise CandidateError(
                "deployed/observed candidate requires deployment identity: "
                + ", ".join(missing_deployment)
            )

    if status != "assembling":
        incomplete_lanes = [
            lane_name
            for lane_name, lane in lanes.items()
            if any(lane[key] is None for key in SHA_KEYS)
        ]
        if incomplete_lanes:
            raise CandidateError(
                "non-assembling candidate requires pinned lane heads: "
                + ", ".join(sorted(incomplete_lanes))
            )
        missing_candidate = [key for key in SHA_KEYS if candidate[key] is None]
        if missing_candidate:
            raise CandidateError(
                "non-assembling candidate requires final triple-SHA: "
                + ", ".join(missing_candidate)
            )

    controls = manifest.get("controls")
    if not isinstance(controls, dict):
        raise CandidateError("controls must be an object")
    if controls.get("shadow_default") != "off":
        raise CandidateError("shadow_default must remain off in the candidate manifest")
    for key in CONTROL_OFF_KEYS:
        if controls.get(key) != "off":
            raise CandidateError(f"{key} must remain off in this round")
    allowed_actions = controls.get("shadow_allowed_actions")
    expected_actions = {"ask_attribute", "show_options", "recommend", "abstain"}
    if not isinstance(allowed_actions, list) or set(allowed_actions) != expected_actions:
        raise CandidateError("shadow_allowed_actions must match the approved private action set")

    evidence = manifest.get("evidence")
    if not isinstance(evidence, dict) or not evidence:
        raise CandidateError("evidence must be a non-empty object")
    invalid_evidence = {
        key: value for key, value in evidence.items() if value not in EVIDENCE_STATES
    }
    if invalid_evidence:
        raise CandidateError(f"invalid evidence states: {invalid_evidence}")
    if status == "assembling" and any(value == "pass" for value in evidence.values()):
        raise CandidateError("assembling manifest cannot claim passing candidate evidence")
    if status in DEPLOYED_STATUSES and evidence.get("staging") != "pass":
        raise CandidateError("deployed/observed candidate requires passing staging evidence")
    if status == "observed" and not any(
        evidence.get(layer) == "pass" for layer in ("device_mock", "physical", "ai_eval")
    ):
        raise CandidateError(
            "observed candidate requires device_mock, physical, or ai_eval evidence"
        )

    blockers = manifest.get("external_blockers")
    if not isinstance(blockers, list) or not all(
        isinstance(blocker, str) and blocker for blocker in blockers
    ):
        raise CandidateError("external_blockers must be a list of non-empty identifiers")


def _revision(path: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=path, text=True, stderr=subprocess.DEVNULL
    ).strip()


def _dirty(path: Path) -> bool:
    return bool(
        subprocess.check_output(
            ["git", "status", "--porcelain", "--untracked-files=all"],
            cwd=path,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    )


def _workspace_projection_matches(*, subject_sha: str, actual_sha: str) -> bool:
    """Allow one manifest-only commit after the pinned workspace subject.

    A committed manifest cannot contain its own commit SHA. The evidence model
    therefore permits exactly one single-parent projection commit whose only
    changed path is this manifest. Product, tooling, merge, or generated-status
    changes are not projection-only and invalidate the match.
    """

    parent_line = subprocess.check_output(
        ["git", "rev-list", "--parents", "-n", "1", actual_sha],
        cwd=ROOT,
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()
    parts = parent_line.split()
    if parts != [actual_sha, subject_sha]:
        return False
    changed_paths = {
        path
        for path in subprocess.check_output(
            ["git", "diff", "--name-only", f"{subject_sha}..{actual_sha}"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
        if path
    }
    return changed_paths == WORKSPACE_PROJECTION_PATHS


def validate_current_checkout(manifest: dict[str, Any]) -> None:
    candidate = manifest["candidate"]
    if any(candidate[key] is None for key in SHA_KEYS):
        raise CandidateError("cannot check current checkout before final triple-SHA is pinned")
    paths = {
        "workspace_sha": ROOT,
        "backend_sha": ROOT / "travel-agent",
        "app_sha": ROOT / "travel-app",
    }
    for key, path in paths.items():
        if not path.exists():
            raise CandidateError(f"missing checkout for {key}: {path}")
        if _dirty(path):
            raise CandidateError(f"{key} checkout is dirty")
        actual = _revision(path)
        if key == "workspace_sha" and actual != candidate[key]:
            if _workspace_projection_matches(subject_sha=candidate[key], actual_sha=actual):
                continue
        if actual != candidate[key]:
            raise CandidateError(
                f"{key} mismatch: manifest={candidate[key]}, checkout={actual}"
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--check-current", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        manifest = json.loads(args.manifest.read_text())
        if not isinstance(manifest, dict):
            raise CandidateError("manifest root must be an object")
        validate_manifest(manifest)
        if args.check_current:
            validate_current_checkout(manifest)
    except (OSError, json.JSONDecodeError, subprocess.CalledProcessError, CandidateError) as exc:
        print(f"candidate invalid: {exc}", file=sys.stderr)
        return 2
    print(f"candidate valid: status={manifest['status']} manifest={args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
