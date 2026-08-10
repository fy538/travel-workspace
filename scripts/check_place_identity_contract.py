#!/usr/bin/env python3
"""Guard canonical place identity across mobile-facing OpenAPI seams."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parent.parent
DEFAULT_SNAPSHOTS = (
    WORKSPACE / "docs" / "openapi.json",
    WORKSPACE / "docs" / "openapi.app.json",
)
ENTITY_REF = "#/components/schemas/EntityRef"
ENTITY_REF_TYPE = "#/components/schemas/EntityRefType"
EXPECTED_TYPES = (
    "place",
    "venue",
    "site",
    "accommodation",
    "experience",
    "transport_hub",
    "custom",
)
IDENTITY_SEAMS = (
    ("MapStop", "entity_ref"),
    ("MapStopAction", "entity_ref"),
    ("ItineraryBlockOut", "entity_ref"),
    ("PlanEntityRef", "entity_ref"),
    ("ProposalDetail", "proposed_entity_ref"),
    ("BookingProposal", "entity_ref"),
    ("UniversalSearchItem", "entity_ref"),
    ("SituationAmbientNearbyCandidate", "entity_ref"),
    ("DeckNearYouPlace", "canonical_entity_ref"),
    ("DeckPickCandidate", "canonical_entity_ref"),
)


def _is_entity_ref_property(property_schema: dict[str, Any]) -> bool:
    if property_schema.get("$ref") == ENTITY_REF:
        return True
    variants = property_schema.get("anyOf")
    if not isinstance(variants, list) or len(variants) != 2:
        return False
    return {variant.get("$ref") for variant in variants if isinstance(variant, dict)} == {
        ENTITY_REF,
        None,
    } and any(
        isinstance(variant, dict) and variant.get("type") == "null"
        for variant in variants
    )


def contract_errors(document: dict[str, Any], *, label: str) -> list[str]:
    errors: list[str] = []
    schemas = document.get("components", {}).get("schemas", {})
    entity_ref = schemas.get("EntityRef")
    if not isinstance(entity_ref, dict):
        return [f"{label}: missing EntityRef schema"]

    properties = entity_ref.get("properties", {})
    if entity_ref.get("additionalProperties") is not False:
        errors.append(f"{label}: EntityRef must reject additional properties")
    if set(entity_ref.get("required", [])) != {"type", "id"}:
        errors.append(f"{label}: EntityRef must require exactly type and id")
    if set(properties) != {"type", "id"}:
        errors.append(f"{label}: EntityRef may expose only type and id")
    elif properties["type"].get("$ref") != ENTITY_REF_TYPE:
        errors.append(f"{label}: EntityRef.type must reference EntityRefType")

    entity_ref_type = schemas.get("EntityRefType", {})
    if tuple(entity_ref_type.get("enum", ())) != EXPECTED_TYPES:
        errors.append(f"{label}: EntityRefType enum drifted")

    for schema_name, property_name in IDENTITY_SEAMS:
        schema = schemas.get(schema_name)
        if not isinstance(schema, dict):
            errors.append(f"{label}: missing identity seam schema {schema_name}")
            continue
        property_schema = schema.get("properties", {}).get(property_name)
        if not isinstance(property_schema, dict):
            errors.append(f"{label}: {schema_name}.{property_name} is missing")
        elif not _is_entity_ref_property(property_schema):
            errors.append(
                f"{label}: {schema_name}.{property_name} must reference EntityRef"
            )
    return errors


def check_snapshots(paths: tuple[Path, ...]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            errors.append(f"{path}: snapshot does not exist")
            continue
        document = json.loads(path.read_text(encoding="utf-8"))
        errors.extend(contract_errors(document, label=str(path)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshots", nargs="*", type=Path)
    args = parser.parse_args()
    paths = tuple(args.snapshots) or DEFAULT_SNAPSHOTS
    errors = check_snapshots(paths)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Place identity contract passed: {len(IDENTITY_SEAMS)} seams × {len(paths)} snapshots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
