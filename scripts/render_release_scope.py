#!/usr/bin/env python3
"""Validate the V1 release manifest and render its human-readable contract."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs/release/v1-scope.yaml"
DOC = ROOT / "docs/release/v1-scope.md"
VALID_INTENTS = {"in", "partial", "out"}


def load_release() -> tuple[dict, list[dict], dict[str, dict]]:
    payload = yaml.safe_load(MANIFEST.read_text())
    release = payload["release"]
    capabilities = payload["capabilities"]
    flag_rows = yaml.safe_load((ROOT / "docs/flags/registry.yaml").read_text())["flags"]
    flags = {row["name"]: row for row in flag_rows}

    problems: list[str] = []
    ids = [row.get("id") for row in capabilities]
    if len(ids) != len(set(ids)):
        problems.append("capability IDs must be unique")
    journey_ids = {
        row["id"]
        for row in yaml.safe_load((ROOT / "docs/journeys/journeys.yaml").read_text())["journeys"]
    }
    for row in capabilities:
        if row.get("intent") not in VALID_INTENTS:
            problems.append(f"{row.get('id')}: invalid intent {row.get('intent')}")
        for path in row.get("evidence_paths", []):
            if not (ROOT / path).exists():
                problems.append(f"{row.get('id')}: missing evidence path {path}")
        for name in row.get("flags", []):
            if name not in flags:
                problems.append(f"{row.get('id')}: unknown flag {name}")
        for journey_id in row.get("journey_ids", []):
            if journey_id not in journey_ids:
                problems.append(f"{row.get('id')}: unknown journey {journey_id}")
    if problems:
        raise ValueError("; ".join(problems))
    return release, capabilities, flags


def evidence_posture(row: dict) -> str:
    paths = row.get("evidence_paths", [])
    present = sum((ROOT / path).exists() for path in paths)
    return f"{present}/{len(paths)} paths present"


def flag_posture(row: dict, flags: dict[str, dict]) -> str:
    names = row.get("flags", [])
    if not names:
        return "No release flag declared"
    defaults = [flags[name].get("default") for name in names]
    if all(value is False for value in defaults):
        return "Dark by default"
    if all(value is True for value in defaults):
        return "Enabled by default"
    return "Mixed: " + ", ".join(f"{name}={flags[name].get('default')}" for name in names)


def render() -> str:
    release, capabilities, flags = load_release()
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
    lines.extend([
        "",
        "## Capability boundary",
        "",
        "Code evidence means the named implementation paths exist. It does not mean the",
        "capability is enabled, production-configured, or certified. Journey Status and",
        "device receipts own those claims.",
        "",
        "| Capability | Intent | Code evidence | Default posture | Certification |",
        "|---|---|---:|---|---|",
    ])
    for row in capabilities:
        journeys = ", ".join(row.get("journey_ids", [])) or "—"
        lines.append(
            f"| {row['name']} | **{row['intent'].upper()}** | {evidence_posture(row)} | "
            f"{flag_posture(row, flags)} | [{journeys}](../journeys/STATUS.md) |"
        )
    lines.extend(["", "## Boundary notes", ""])
    lines.extend(f"- **{row['name']}:** {row['note']}" for row in capabilities)
    lines.extend([
        "",
        "## Readiness",
        "",
        "This contract owns release intent only. Use",
        "[Current State](../status/current-state.md) for the generated intent/evidence view,",
        "[Journey Status](../journeys/STATUS.md) for certification, and",
        "[Owner Actions](../Owner%20Action%20Items.md) for external blockers.",
        "",
    ])
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
