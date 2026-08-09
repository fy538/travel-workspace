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

    def test_untracked_evidence_does_not_count_as_implementation(self) -> None:
        with patch.object(subject, "_path_is_tracked", return_value=False):
            problems = subject.validate_release(
                self.payload, self.flag_rows, self.journey_ids
            )
        self.assertTrue(
            any("evidence path is not tracked" in problem for problem in problems)
        )

    def test_known_replay_failure_blocks_affected_capability(self) -> None:
        live_trip = next(
            row for row in self.payload["capabilities"] if row["id"] == "live-trip"
        )
        posture = subject.readiness_posture(live_trip, subject.load_persona_replay())
        self.assertEqual(posture, "BLOCKED — seeded replay fails J08")


if __name__ == "__main__":
    unittest.main()
