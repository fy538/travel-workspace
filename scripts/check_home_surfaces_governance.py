#!/usr/bin/env python3
"""Validate the external authority and composition-status inventory."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUTHORITY_PATH = ROOT / "docs/governance/home-surfaces-design-authority.json"
INVENTORY_PATH = ROOT / "docs/status/home-surfaces-composition-inventory.json"
EVIDENCE_KEYS = tuple("DCPRAFBV")
EVIDENCE_STATES = {"verified", "partial", "not_verified", "not_applicable"}
ADOPTION_STATES = {"adopted", "exploratory", "relocated", "rejected", "unresolved"}
SURFACES = {"trips-home", "places-workspace"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _load(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from None
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: root must be an object")
    return data


def validate() -> list[str]:
    problems: list[str] = []
    try:
        authority = _load(AUTHORITY_PATH)
        inventory = _load(INVENTORY_PATH)
    except ValueError as exc:
        return [str(exc)]

    authority_id = authority.get("authority_id")
    if not isinstance(authority_id, str) or not authority_id:
        problems.append("authority: authority_id must be a non-empty string")
    if set(authority.get("scope", [])) != SURFACES:
        problems.append("authority: scope must contain exactly trips-home and places-workspace")

    bundle = authority.get("canonical_bundle")
    if not isinstance(bundle, dict):
        problems.append("authority: canonical_bundle must be an object")
        bundle = {}
    if bundle.get("repository_copy_allowed") is not False:
        problems.append("authority: repository_copy_allowed must be false")
    if bundle.get("ci_requires_external_directory") is not False:
        problems.append("authority: CI must not require the external directory")
    if bundle.get("local_directory_env") != "HOME_SURFACES_CANON_DIR":
        problems.append("authority: local directory input must be HOME_SURFACES_CANON_DIR")

    files = bundle.get("files")
    if not isinstance(files, list) or not files:
        problems.append("authority: canonical_bundle.files must be non-empty")
        files = []
    paths: set[str] = set()
    for index, entry in enumerate(files):
        prefix = f"authority: files[{index}]"
        if not isinstance(entry, dict):
            problems.append(f"{prefix} must be an object")
            continue
        path = entry.get("path")
        if not isinstance(path, str) or not path:
            problems.append(f"{prefix}.path must be a non-empty string")
        elif Path(path).is_absolute() or ".." in Path(path).parts:
            problems.append(f"{prefix}.path must be bundle-relative")
        elif path in paths:
            problems.append(f"{prefix}.path is duplicated: {path}")
        else:
            paths.add(path)
        if not SHA256.fullmatch(str(entry.get("sha256", ""))):
            problems.append(f"{prefix}.sha256 must be a lowercase SHA-256")

    adoption_vocabulary = authority.get("adoption_vocabulary")
    if not isinstance(adoption_vocabulary, dict) or set(adoption_vocabulary) != ADOPTION_STATES:
        problems.append("authority: adoption_vocabulary does not match the governed states")
    evidence_vocabulary = authority.get("evidence_vocabulary")
    if not isinstance(evidence_vocabulary, dict) or set(evidence_vocabulary) != set(EVIDENCE_KEYS):
        problems.append("authority: evidence_vocabulary must define D/C/P/R/A/F/B/V")
    evidence_states = authority.get("evidence_states")
    if not isinstance(evidence_states, dict) or set(evidence_states) != EVIDENCE_STATES:
        problems.append("authority: evidence_states does not match the governed states")

    if inventory.get("authority_id") != authority_id:
        problems.append("inventory: authority_id does not match the authority record")
    items = inventory.get("items")
    if not isinstance(items, list) or not items:
        problems.append("inventory: items must be a non-empty array")
        return problems

    required_strings = {
        "id",
        "surface",
        "group",
        "name",
        "adoption",
        "design_source",
        "evidence_requirement",
        "producer",
        "contract",
        "reachability",
        "renderer",
        "action",
        "telemetry",
    }
    ids: set[str] = set()
    covered_surfaces: set[str] = set()
    for index, item in enumerate(items):
        prefix = f"inventory: items[{index}]"
        if not isinstance(item, dict):
            problems.append(f"{prefix} must be an object")
            continue
        for key in required_strings:
            if not isinstance(item.get(key), str) or not item[key].strip():
                problems.append(f"{prefix}.{key} must be a non-empty string")
        item_id = item.get("id")
        if isinstance(item_id, str):
            if item_id in ids:
                problems.append(f"{prefix}.id is duplicated: {item_id}")
            ids.add(item_id)
        surface = item.get("surface")
        if surface not in SURFACES:
            problems.append(f"{prefix}.surface must be trips-home or places-workspace")
        else:
            covered_surfaces.add(surface)
        if item.get("adoption") not in ADOPTION_STATES:
            problems.append(f"{prefix}.adoption is not governed")
        if not isinstance(item.get("variants"), list):
            problems.append(f"{prefix}.variants must be an array")
        blockers = item.get("blockers")
        if not isinstance(blockers, list):
            problems.append(f"{prefix}.blockers must be an array")
        evidence = item.get("evidence")
        if not isinstance(evidence, dict) or set(evidence) != set(EVIDENCE_KEYS):
            problems.append(f"{prefix}.evidence must define D/C/P/R/A/F/B/V exactly")
        else:
            for key, state in evidence.items():
                if state not in EVIDENCE_STATES:
                    problems.append(f"{prefix}.evidence.{key} has unknown state {state!r}")
            if evidence["V"] == "verified":
                problems.append(f"{prefix}.evidence.V cannot be verified by this static audit seed")

    if covered_surfaces != SURFACES:
        problems.append("inventory: both governed surfaces must have at least one item")
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print(f"home-surfaces-governance FAILED: {len(problems)} issue(s)", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    authority = _load(AUTHORITY_PATH)
    inventory = _load(INVENTORY_PATH)
    print(
        "home-surfaces-governance OK: "
        f"authority={authority['authority_id']} files={len(authority['canonical_bundle']['files'])} "
        f"compositions={len(inventory['items'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
