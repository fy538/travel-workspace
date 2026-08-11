#!/usr/bin/env python3
"""Validate the V1 release manifest and render its human-readable contract."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

import yaml

import journey_evidence
from promote_journey_evidence import index_candidate_is_current, load_index

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs/release/v1-scope.yaml"
DOC = ROOT / "docs/release/v1-scope.md"
VALID_INTENTS = {"in", "partial", "out"}
CHILD_REPOS = {"travel-agent", "travel-app"}
PERSONA_BEGIN = "<!-- BEGIN auto:persona-cert"
PERSONA_END = "<!-- END auto:persona-cert -->"
REQUIRED_RELEASE_FIELDS = {
    "id",
    "name",
    "status",
    "decided",
    "last_verified",
    "owner",
    "promise",
    "principles",
}
REQUIRED_CAPABILITY_FIELDS = {
    "id",
    "name",
    "intent",
    "evidence_paths",
    "journey_ids",
    "required_layers",
    "flags",
    "note",
}


def _path_is_tracked(relative: str) -> bool:
    parts = Path(relative).parts
    if not parts:
        return False
    if parts[0] in CHILD_REPOS:
        repo = ROOT / parts[0]
        pathspec = str(Path(*parts[1:]))
    else:
        repo = ROOT
        pathspec = relative
    if not (repo / ".git").exists() or not pathspec:
        return False
    return (
        subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", pathspec],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def validate_release(
    payload: dict, flag_rows: list[dict], journey_ids: set[str]
) -> list[str]:
    problems: list[str] = []
    if not isinstance(payload, dict):
        return ["manifest must be a mapping"]
    release = payload.get("release")
    capabilities = payload.get("capabilities")
    if not isinstance(release, dict):
        return ["release must be a mapping"]
    if not isinstance(capabilities, list) or not capabilities:
        return ["capabilities must be a non-empty list"]

    missing_release = sorted(REQUIRED_RELEASE_FIELDS - release.keys())
    if missing_release:
        problems.append(
            "release missing required fields: " + ", ".join(missing_release)
        )

    flag_names = [row.get("name") for row in flag_rows]
    duplicates = sorted({name for name in flag_names if flag_names.count(name) > 1})
    if duplicates:
        problems.append("duplicate flag registry names: " + ", ".join(duplicates))
    flags = {row.get("name"): row for row in flag_rows if row.get("name")}

    ids = [row.get("id") for row in capabilities if isinstance(row, dict)]
    if len(ids) != len(set(ids)):
        problems.append("capability IDs must be unique")
    names = [row.get("name") for row in capabilities if isinstance(row, dict)]
    if len(names) != len(set(names)):
        problems.append("capability names must be unique")

    for row in capabilities:
        if not isinstance(row, dict):
            problems.append("every capability must be a mapping")
            continue
        cap_id = row.get("id") or "<missing-id>"
        missing = sorted(REQUIRED_CAPABILITY_FIELDS - row.keys())
        if missing:
            problems.append(f"{cap_id}: missing required fields: {', '.join(missing)}")
        intent = row.get("intent")
        if intent not in VALID_INTENTS:
            problems.append(f"{cap_id}: invalid intent {intent}")

        paths = row.get("evidence_paths", [])
        if not isinstance(paths, list) or not paths:
            problems.append(f"{cap_id}: evidence_paths must be a non-empty list")
            paths = []
        for path in paths:
            if not isinstance(path, str) or not path:
                problems.append(f"{cap_id}: evidence path must be a non-empty string")
            elif not (ROOT / path).exists():
                problems.append(f"{cap_id}: missing evidence path {path}")
            elif not _path_is_tracked(path):
                problems.append(
                    f"{cap_id}: evidence path is not tracked by its repository: {path}"
                )

        names_for_capability = row.get("flags", [])
        if not isinstance(names_for_capability, list):
            problems.append(f"{cap_id}: flags must be a list")
            names_for_capability = []
        if len(names_for_capability) != len(set(names_for_capability)):
            problems.append(f"{cap_id}: flag names must be unique")
        for name in names_for_capability:
            if name not in flags:
                problems.append(f"{cap_id}: unknown flag {name}")
            elif not isinstance(flags[name].get("default"), bool):
                problems.append(
                    f"{cap_id}: release flag {name} must have a boolean default"
                )
        known_defaults = [
            flags[name].get("default") for name in names_for_capability if name in flags
        ]
        if intent == "out" and not names_for_capability:
            problems.append(
                f"{cap_id}: OUT capabilities require at least one release flag"
            )
        if intent == "out" and any(value is not False for value in known_defaults):
            problems.append(f"{cap_id}: OUT capability flags must all default false")
        # An IN capability may carry a dark flag only when the manifest states
        # the condition under which it lights. Without `gate`, an IN row with a
        # dark flag silently overclaims readiness.
        in_with_dark_flag = intent == "in" and any(
            value is not True for value in known_defaults
        )
        gate = row.get("gate")
        if in_with_dark_flag and not (isinstance(gate, str) and gate.strip()):
            problems.append(
                f"{cap_id}: IN capability with a dark flag requires a non-empty "
                "gate naming the condition under which it lights"
            )
        if gate is not None and not in_with_dark_flag:
            problems.append(
                f"{cap_id}: gate is only valid on an IN capability that carries "
                "a dark flag"
            )

        row_journeys = row.get("journey_ids", [])
        if not isinstance(row_journeys, list) or not row_journeys:
            problems.append(f"{cap_id}: journey_ids must be a non-empty list")
            row_journeys = []
        if len(row_journeys) != len(set(row_journeys)):
            problems.append(f"{cap_id}: journey IDs must be unique")
        for journey_id in row_journeys:
            if journey_id not in journey_ids:
                problems.append(f"{cap_id}: unknown journey {journey_id}")
        required_layers = row.get("required_layers", [])
        if not isinstance(required_layers, list):
            problems.append(f"{cap_id}: required_layers must be a list")
            required_layers = []
        if len(required_layers) != len(set(required_layers)):
            problems.append(f"{cap_id}: required layers must be unique")
        unknown_layers = sorted(set(required_layers) - set(journey_evidence.LAYERS))
        if unknown_layers:
            problems.append(f"{cap_id}: unknown required layers {', '.join(unknown_layers)}")
        if intent in {"in", "partial"} and not required_layers:
            problems.append(f"{cap_id}: IN/PARTIAL capabilities require evidence layers")
    return problems


def load_release() -> tuple[dict, list[dict], dict[str, dict]]:
    payload = yaml.safe_load(MANIFEST.read_text())
    flag_rows = yaml.safe_load((ROOT / "docs/flags/registry.yaml").read_text())["flags"]
    journey_ids = {
        row["id"]
        for row in yaml.safe_load((ROOT / "docs/journeys/journeys.yaml").read_text())[
            "journeys"
        ]
    }
    problems = validate_release(payload, flag_rows, journey_ids)
    if problems:
        raise ValueError("; ".join(problems))
    return (
        payload["release"],
        payload["capabilities"],
        {row["name"]: row for row in flag_rows},
    )


def evidence_posture(row: dict) -> str:
    paths = row.get("evidence_paths", [])
    tracked = sum((ROOT / path).exists() and _path_is_tracked(path) for path in paths)
    return f"{tracked}/{len(paths)} tracked paths"


def flag_posture(row: dict, flags: dict[str, dict]) -> str:
    names = row.get("flags", [])
    if not names:
        return "No release flag declared"
    defaults = [flags[name].get("default") for name in names]
    if all(value is False for value in defaults):
        return "Dark by default"
    if all(value is True for value in defaults):
        return "Enabled by default"
    return "Mixed: " + ", ".join(
        f"{name}={flags[name].get('default')}" for name in names
    )


def production_posture(row: dict, flags: dict[str, dict]) -> str:
    if row.get("intent") == "out" and flag_posture(row, flags) == "Dark by default":
        return "Not claimed; release defaults dark"
    if row.get("gate") and flag_posture(row, flags) != "Enabled by default":
        return "Not claimed; in scope but gated"
    return "Unverified externally"


def load_persona_replay() -> dict[str, str]:
    status = (ROOT / "docs/journeys/STATUS.md").read_text()
    start = status.find(PERSONA_BEGIN)
    end = status.find(PERSONA_END)
    if start < 0 or end < 0 or end <= start:
        raise ValueError("Journey Status is missing the generated persona-cert block")
    states: dict[str, str] = {}
    for line in status[start:end].splitlines():
        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 6 or not parts[1].startswith("J"):
            continue
        raw = parts[4]
        if raw.startswith("✅"):
            states[parts[1]] = "pass"
        elif raw.startswith("🔴"):
            states[parts[1]] = "fail"
        elif raw.startswith("⤵️"):
            states[parts[1]] = "skip"
        else:
            states[parts[1]] = "unrun"
    return states


def load_promoted_evidence() -> dict[str, set[str]]:
    """Return current-revision passing layers keyed by journey identifier."""
    index = load_index()
    current = journey_evidence.current_revisions()
    if not index_candidate_is_current(index, current):
        return {}

    states: dict[str, set[str]] = {}
    for attestation in index.get("attestations", []):
        receipt = attestation.get("receipt") if isinstance(attestation, dict) else None
        if not isinstance(receipt, dict):
            continue
        try:
            journey_evidence.validate_receipt(receipt)
        except journey_evidence.ReceiptError:
            continue
        if receipt.get("status") != "pass":
            continue
        for journey_id in receipt.get("journeys", []):
            states.setdefault(journey_id, set()).add(receipt["layer"])
    return states


def readiness_posture(
    row: dict, replay: dict[str, str], promoted: dict[str, set[str]] | None = None
) -> str:
    if row.get("intent") == "out":
        return "OUT — not a v1 certification target"
    journey_ids = row.get("journey_ids", [])
    failed = [
        journey_id for journey_id in journey_ids if replay.get(journey_id) == "fail"
    ]
    missing = [
        journey_id for journey_id in journey_ids if replay.get(journey_id) != "pass"
    ]
    if failed:
        return "BLOCKED — seeded replay fails " + ", ".join(failed)
    if missing:
        return "UNCERTIFIED — replay missing " + ", ".join(missing)
    promoted = promoted or {}
    required_layers = set(row.get("required_layers", []))
    missing_layers = {
        journey_id: sorted(required_layers - promoted.get(journey_id, set()))
        for journey_id in journey_ids
        if required_layers - promoted.get(journey_id, set())
    }
    if journey_ids and not missing_layers:
        return "PASS — current-revision promoted receipt"
    missing_summary = "; ".join(
        f"{journey_id}: {','.join(layers)}" for journey_id, layers in missing_layers.items()
    )
    return "UNCERTIFIED — required promoted layers missing " + missing_summary


def render() -> str:
    release, capabilities, flags = load_release()
    replay = load_persona_replay()
    promoted = load_promoted_evidence()
    lines = [
        "---",
        "doc_type: contract",
        "status: active",
        f"owner: {release['owner']}",
        f"created: {release['decided']}",
        f"last_verified: {release['last_verified']}",
        "why_new: Renders the machine-readable V1 release intent as the authoritative human scope contract.",
        "supersedes: [docs/working/mvp-scope-and-flag-manifest-2026-06-30.md]",
        "source_of_truth_for: [v1-release-scope]",
        "---",
        "",
        f"# {release['name']} release contract",
        "",
        "> Generated from [`v1-scope.yaml`](v1-scope.yaml). Do not hand-edit this file;",
        "> run `make docs-release-sync` after changing the manifest or flag registry.",
        "",
        f"**Status:** {release['status']} · **Decided:** {release['decided']} · "
        f"**Last verified:** {release['last_verified']}",
        "",
        "## Promise",
        "",
        release["promise"],
        "",
        "## Governing principles",
        "",
    ]
    lines.extend(f"- {item}" for item in release["principles"])
    lines.extend(
        [
            "",
            "## Capability boundary",
            "",
            "Implementation means the named paths are tracked by their owning repository.",
            "Release defaults come from the flag registry; they are not deployed-production",
            "configuration. Readiness exposes known seeded-replay failures but remains",
            "uncertified until a current-revision receipt exists.",
            "",
            "| Capability | Intent | Implementation | Release default | Production-enabled | Readiness |",
            "|---|---|---:|---|---|---|",
        ]
    )
    for row in capabilities:
        journeys = ", ".join(row.get("journey_ids", [])) or "—"
        lines.append(
            f"| {row['name']} | **{row['intent'].upper()}** | {evidence_posture(row)} | "
            f"{flag_posture(row, flags)} | {production_posture(row, flags)} | "
            f"[{readiness_posture(row, replay, promoted)}](../journeys/STATUS.md) ({journeys}) |"
        )
    lines.extend(["", "## Boundary notes", ""])
    lines.extend(
        f"- **{row['name']}:** {row['note']}"
        + (f" _Gate: {row['gate']}_" if row.get("gate") else "")
        for row in capabilities
    )
    lines.extend(
        [
            "",
            "## Readiness",
            "",
            "This contract owns release intent only. Use",
            "[Current State](../status/current-state.md) for the generated intent/evidence view,",
            "[Journey Status](../journeys/STATUS.md) for certification, and",
            "[Owner Actions](../Owner%20Action%20Items.md) for external blockers.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.write:
        DOC.write_text(expected)
        print("updated", DOC.relative_to(ROOT))
        return 0
    if not DOC.exists() or DOC.read_text() != expected:
        print("release-scope drift: run `make docs-release-sync`")
        return 1
    print("release-scope OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
