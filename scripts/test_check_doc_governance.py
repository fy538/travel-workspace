from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_doc_governance import validate


class DocumentGovernanceTests(unittest.TestCase):
    def _document(self, text: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "document.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_valid_contract(self) -> None:
        path = self._document(
            """---
doc_type: contract
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-07-09
why_new: Owns a new cross-system invariant with no existing home.
---
# Contract
"""
        )
        self.assertEqual(validate(path), [])

    def test_missing_frontmatter_fails(self) -> None:
        path = self._document("# Ungoverned\n")
        self.assertIn("missing YAML frontmatter", validate(path)[0].message)

    def test_working_expiry_is_bounded(self) -> None:
        path = self._document(
            """---
doc_type: working
status: active
owner: engineering
created: 2026-07-09
expires: 2026-09-09
why_new: Investigates a bounded question that no existing note owns.
---
# Working
"""
        )
        messages = [finding.message for finding in validate(path)]
        self.assertIn("working document expires must be within 30 days of created", messages)

    def test_decision_requires_decided_date(self) -> None:
        path = self._document(
            """---
doc_type: decision
status: accepted
owner: founder
created: 2026-07-09
why_new: Preserves a consequential product choice and its rationale.
---
# Decision
"""
        )
        messages = [finding.message for finding in validate(path)]
        self.assertIn("decided must be an ISO date (YYYY-MM-DD)", messages)


if __name__ == "__main__":
    unittest.main()
