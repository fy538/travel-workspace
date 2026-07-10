from __future__ import annotations

import unittest

from check_doc_inventory import Classification, _path_glob_matches, classify, location_problem


class DocumentInventoryTests(unittest.TestCase):
    def test_override_wins_over_rule(self) -> None:
        inventory = {
            "rules": [
                {
                    "glob": "docs/systems/*.md",
                    "disposition": "keep_authoritative",
                    "rationale": "System charters are authoritative contracts.",
                }
            ],
            "overrides": {
                "docs/systems/draft.md": {
                    "disposition": "investigate",
                    "rationale": "Draft has not yet been ratified into the system index.",
                }
            },
        }
        result = classify("docs/systems/draft.md", inventory)
        self.assertIsNotNone(result)
        self.assertEqual(result.disposition, "investigate")

    def test_merge_requires_target(self) -> None:
        inventory = {
            "rules": [],
            "overrides": {
                "docs/plan.md": {
                    "disposition": "merge",
                    "rationale": "Durable material belongs in the system charter.",
                }
            },
        }
        with self.assertRaisesRegex(ValueError, "has no target"):
            classify("docs/plan.md", inventory)

    def test_unmatched_path_is_unclassified(self) -> None:
        self.assertIsNone(classify("docs/new.md", {"rules": [], "overrides": {}}))

    def test_single_star_does_not_cross_directories(self) -> None:
        self.assertFalse(
            _path_glob_matches(
                "docs/reliability/prompts/reviewer.md", "docs/reliability/*.md"
            )
        )

    def test_double_star_matches_nested_archive(self) -> None:
        self.assertTrue(
            _path_glob_matches(
                "docs/archive/2026-05/dogfood/README.md", "docs/archive/**/*.md"
            )
        )

    def test_archive_disposition_must_be_in_archive_tree(self) -> None:
        classification = Classification(
            disposition="archive",
            rationale="Completed point-in-time evidence belongs in history.",
            source="test",
        )
        self.assertIsNotNone(location_problem("docs/working/done.md", classification))
        self.assertIsNone(
            location_problem("docs/archive/2026-07/done.md", classification)
        )


if __name__ == "__main__":
    unittest.main()
