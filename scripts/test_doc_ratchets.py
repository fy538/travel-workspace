from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from check_living_doc_links import target_path


class LivingDocLinkTests(unittest.TestCase):
    def test_external_and_anchor_links_are_not_local_paths(self) -> None:
        source = Path("/tmp/docs/source.md")
        self.assertIsNone(target_path(source, "https://example.com"))
        self.assertIsNone(target_path(source, "#section"))

    def test_encoded_relative_link_resolves(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "docs" / "source.md"
            target = root / "docs" / "Target File.md"
            source.parent.mkdir()
            source.touch()
            target.touch()
            self.assertEqual(target_path(source, "Target%20File.md"), target.resolve())


if __name__ == "__main__":
    unittest.main()
