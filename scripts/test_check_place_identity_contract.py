from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from check_place_identity_contract import (  # noqa: E402
    ENTITY_REF,
    EXPECTED_TYPES,
    IDENTITY_SEAMS,
    contract_errors,
)


def _contract() -> dict:
    schemas = {
        "EntityRef": {
            "type": "object",
            "additionalProperties": False,
            "required": ["type", "id"],
            "properties": {
                "type": {"$ref": "#/components/schemas/EntityRefType"},
                "id": {"type": "string"},
            },
        },
        "EntityRefType": {"type": "string", "enum": list(EXPECTED_TYPES)},
    }
    for schema_name, property_name in IDENTITY_SEAMS:
        schemas[schema_name] = {"properties": {property_name: {"$ref": ENTITY_REF}}}
    return {"components": {"schemas": schemas}}


def test_accepts_canonical_identity_on_every_seam() -> None:
    assert contract_errors(_contract(), label="fixture") == []


def test_rejects_provider_shaped_public_identity_and_missing_seam() -> None:
    contract = _contract()
    contract["components"]["schemas"]["EntityRef"]["properties"]["provider"] = {
        "type": "string"
    }
    contract["components"]["schemas"]["MapStop"]["properties"].pop("entity_ref")

    errors = contract_errors(contract, label="fixture")

    assert "fixture: EntityRef may expose only type and id" in errors
    assert "fixture: MapStop.entity_ref is missing" in errors


def test_rejects_external_ref_substitution_even_when_field_exists() -> None:
    contract = copy.deepcopy(_contract())
    contract["components"]["schemas"]["BookingProposal"]["properties"]["entity_ref"] = {
        "$ref": "#/components/schemas/ExternalRef"
    }

    assert contract_errors(contract, label="fixture") == [
        "fixture: BookingProposal.entity_ref must reference EntityRef"
    ]
