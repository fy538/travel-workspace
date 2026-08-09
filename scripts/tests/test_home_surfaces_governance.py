from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts/check_home_surfaces_governance.py"
SPEC = importlib.util.spec_from_file_location("check_home_surfaces_governance", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class HomeSurfacesGovernanceTest(unittest.TestCase):
    def test_committed_authority_and_inventory_are_valid(self) -> None:
        self.assertEqual(MODULE.validate(), [])


if __name__ == "__main__":
    unittest.main()
