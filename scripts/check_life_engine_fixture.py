#!/usr/bin/env python3
"""Validate the replay manifest for the proposed Life organization engine."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/working/fixtures/life-engine/life-engine-replay-v0.1.json"
EXPECTED_SCENARIOS = {f"W{i}" for i in range(1, 7)}
ALLOWED_CHANGE_KINDS = {
    "source_admitted",
    "anchor_enriched",
    "owner_correction",
    "plan_opened",
    "historical_source_imported",
    "observation_admitted",
    "synthesis_admitted",
    "occasion_created",
    "contribution_addressed",
    "audience_withdrawn",
    "occurrence_proposed",
    "stale_replay",
    "composition_started",
    "human_block_locked",
    "source_corrected",
    "composition_shared",
}


def validate() -> list[str]:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    errors: list[str] = []
    if data.get("schema_version") != "vesper.life-engine-replay.v0.1":
        errors.append("unexpected schema_version")
    if data.get("not_production_data") is not True:
        errors.append("fixture must be marked not_production_data")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list):
        return ["scenarios must be a list"]
    scenario_ids = [item.get("scenario_id") for item in scenarios]
    if set(scenario_ids) != EXPECTED_SCENARIOS or len(scenario_ids) != len(set(scenario_ids)):
        errors.append("fixture must contain exactly W1-W6 once")
    event_ids: set[str] = set()
    for scenario in scenarios:
        scenario_id = scenario.get("scenario_id", "<unknown>")
        if not scenario.get("owner_kinds"):
            errors.append(f"{scenario_id} has no owner_kinds")
        transitions = scenario.get("transitions")
        if not isinstance(transitions, list) or not transitions:
            errors.append(f"{scenario_id} has no transitions")
            continue
        for transition in transitions:
            event_id = transition.get("event_id")
            if not event_id or event_id in event_ids:
                errors.append(f"{scenario_id} has duplicate or missing event_id")
            event_ids.add(event_id)
            if transition.get("change_kind") not in ALLOWED_CHANGE_KINDS:
                errors.append(f"{scenario_id} has unknown change_kind")
            for key in ("owner_kind", "owner_id", "owner_revision"):
                if not transition.get(key):
                    errors.append(f"{scenario_id} transition missing {key}")
        expected = scenario.get("expected") or {}
        for key in ("record_behavior", "preserve_unknown", "repair_consumers", "must_not"):
            if not expected.get(key):
                errors.append(f"{scenario_id} expected section missing {key}")
    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, json.JSONDecodeError, TypeError, AttributeError) as exc:
        print(f"life-engine-fixture: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"life-engine-fixture: {error}", file=sys.stderr)
        print(f"life-engine-fixture FAILED: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("life-engine-fixture OK: W1-W6 replay manifest is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
