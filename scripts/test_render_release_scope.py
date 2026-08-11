from __future__ import annotations

import copy
import unittest
from unittest.mock import patch

import yaml

import render_release_scope as subject


class ReleaseScopeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = yaml.safe_load(subject.MANIFEST.read_text())
        cls.flag_rows = yaml.safe_load(
            (subject.ROOT / "docs/flags/registry.yaml").read_text()
        )["flags"]
        cls.journey_ids = {
            row["id"]
            for row in yaml.safe_load(
                (subject.ROOT / "docs/journeys/journeys.yaml").read_text()
            )["journeys"]
        }

    def test_current_manifest_is_valid(self) -> None:
        self.assertEqual(
            subject.validate_release(self.payload, self.flag_rows, self.journey_ids),
            [],
        )

    def test_out_capability_cannot_become_default_on(self) -> None:
        flags = copy.deepcopy(self.flag_rows)
        for row in flags:
            if row["name"] == "VOICE_ENABLED":
                row["default"] = True
        problems = subject.validate_release(self.payload, flags, self.journey_ids)
        self.assertIn("voice: OUT capability flags must all default false", problems)

    def test_in_capability_with_dark_flag_requires_a_gate(self) -> None:
        payload = copy.deepcopy(self.payload)
        row = next(
            item for item in payload["capabilities"] if item["id"] == "plan-repair"
        )
        del row["gate"]
        problems = subject.validate_release(payload, self.flag_rows, self.journey_ids)
        self.assertIn(
            "plan-repair: IN capability with a dark flag requires a non-empty "
            "gate naming the condition under which it lights",
            problems,
        )

    def test_blank_gate_does_not_satisfy_the_requirement(self) -> None:
        payload = copy.deepcopy(self.payload)
        row = next(
            item for item in payload["capabilities"] if item["id"] == "plan-repair"
        )
        row["gate"] = "   "
        problems = subject.validate_release(payload, self.flag_rows, self.journey_ids)
        self.assertTrue(any("requires a non-empty" in problem for problem in problems))

    def test_gate_is_rejected_when_there_is_nothing_to_gate(self) -> None:
        payload = copy.deepcopy(self.payload)
        row = next(item for item in payload["capabilities"] if item["id"] == "expenses")
        row["gate"] = "not applicable"
        problems = subject.validate_release(payload, self.flag_rows, self.journey_ids)
        self.assertIn(
            "expenses: gate is only valid on an IN capability that carries a dark flag",
            problems,
        )

    def test_gated_in_capability_is_not_claimed_as_production_enabled(self) -> None:
        _, capabilities, flags = subject.load_release()
        row = next(item for item in capabilities if item["id"] == "plan-repair")
        self.assertEqual(
            subject.production_posture(row, flags),
            "Not claimed; in scope but gated",
        )

    def test_untracked_evidence_does_not_count_as_implementation(self) -> None:
        with patch.object(subject, "_path_is_tracked", return_value=False):
            problems = subject.validate_release(
                self.payload, self.flag_rows, self.journey_ids
            )
        self.assertTrue(
            any("evidence path is not tracked" in problem for problem in problems)
        )

    def test_replay_failure_blocks_affected_capability(self) -> None:
        live_trip = next(
            row for row in self.payload["capabilities"] if row["id"] == "live-trip"
        )
        replay = subject.load_persona_replay()
        replay["J08"] = "fail"
        posture = subject.readiness_posture(live_trip, replay)
        self.assertEqual(posture, "BLOCKED — seeded replay fails J08")

    def test_promoted_evidence_requires_current_candidate(self) -> None:
        with patch.object(subject, "load_index", return_value={
            "schema_version": 1,
            "candidate": {
                "workspace_sha": "old",
                "app_sha": "old",
                "backend_sha": "old",
            },
            "attestations": [],
        }):
            self.assertEqual(subject.load_promoted_evidence(), {})

    def test_release_pass_requires_every_declared_layer(self) -> None:
        row = {
            "intent": "in",
            "journey_ids": ["J04"],
            "required_layers": ["database", "physical"],
        }
        replay = {"J04": "pass"}

        self.assertEqual(
            subject.readiness_posture(row, replay, {"J04": {"contract", "database"}}),
            "UNCERTIFIED — required promoted layers missing J04: physical",
        )
        self.assertEqual(
            subject.readiness_posture(row, replay, {"J04": {"database", "physical"}}),
            "PASS — current-revision promoted receipt",
        )


if __name__ == "__main__":
    unittest.main()
