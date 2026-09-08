"""Structural fixture checks, not automatic-organization quality tests."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_life_engine_fixture import FIXTURE, validate


class LifeEngineFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.w2 = next(row for row in self.data["scenarios"] if row["scenario_id"] == "W2")

    def errors(self) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.json"
            path.write_text(json.dumps(self.data), encoding="utf-8")
            return validate(path)

    def test_existing_portfolio_is_structurally_valid(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_w2_cannot_declare_a_plan_owner(self) -> None:
        self.w2["owner_kinds"].append("plan")
        self.assertIn(
            "W2 must exercise ordinary life without Plan or Occasion owners", self.errors()
        )

    def test_w2_cannot_hide_an_occasion_in_a_transition(self) -> None:
        self.w2["transitions"][0]["owner_kind"] = "occasion"
        self.assertIn("W2 cannot create or depend on a Plan or Occasion", self.errors())

    def test_w2_cannot_disguise_plan_creation_as_a_source_event(self) -> None:
        self.w2["transitions"][0]["change_kind"] = "plan_opened"
        self.assertIn("W2 cannot create or depend on a Plan or Occasion", self.errors())

    def test_transition_owner_must_be_declared(self) -> None:
        self.data["scenarios"][0]["transitions"][0]["owner_kind"] = "plan"
        self.assertIn("W1 transition owner is not declared in owner_kinds", self.errors())

    def test_other_worlds_can_still_cover_plan_owners(self) -> None:
        w1 = self.data["scenarios"][0]
        w1["owner_kinds"].append("plan")
        w1["transitions"].append(
            {
                "event_id": "w1-extra-plan",
                "change_kind": "plan_opened",
                "owner_kind": "plan",
                "owner_id": "fixture-trip-plan",
                "owner_revision": "1",
            }
        )
        self.assertEqual(self.errors(), [])


if __name__ == "__main__":
    unittest.main()
