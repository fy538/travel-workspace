from __future__ import annotations

import importlib.util
import json
import tempfile
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

    def test_verified_device_evidence_requires_a_receipt_but_can_be_recorded(self) -> None:
        authority = json.loads((ROOT / "docs/governance/home-surfaces-design-authority.json").read_text())
        inventory = json.loads((ROOT / "docs/status/home-surfaces-composition-inventory.json").read_text())
        item = inventory["items"][0]
        item["evidence"]["V"] = "verified"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority_path = root / "authority.json"
            inventory_path = root / "inventory.json"
            authority_path.write_text(json.dumps(authority))
            inventory_path.write_text(json.dumps(inventory))
            self.assertIn(
                "evidence.V=verified requires an evidence receipt",
                "\n".join(MODULE.validate(authority_path, inventory_path)),
            )

            inventory["evidence_receipts"].append(
                {
                    "id": "device-2026-08-09-candidate-rows",
                    "item_id": item["id"],
                    "layer": "V",
                    "kind": "device_capture",
                    "source": "docs/audits/device/candidate-rows-2026-08-09.md",
                    "recorded_at": "2026-08-09",
                    "summary": "Named device scenario accepted.",
                    "platform": "iOS",
                }
            )
            inventory_path.write_text(json.dumps(inventory))
            self.assertEqual(MODULE.validate(authority_path, inventory_path), [])


if __name__ == "__main__":
    unittest.main()
