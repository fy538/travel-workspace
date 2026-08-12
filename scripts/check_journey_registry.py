#!/usr/bin/env python3
"""Journey-set drift guard — assert every journey registry agrees with the
canonical manifest (docs/journeys/journeys.yaml). Pure file-parse, NO DB —
runs in CI alongside the contract checks.

DEFINITION registries (must match the manifest exactly → exit 1 on drift):
  - docs/journeys/<NN>-*.md          one-pager per journey
  - docs/journeys/README.md          index table rows
  - dogfood_journey_persona_cert.py  JOURNEY_PERSONA_MAP specs (lived)

FIDELITY subset (informational, never fails): scenarios.mjs / BE pytest /
FE mock-walk are the core contract/logic layer. Newly defined customer journeys
may begin without fidelity evidence, so partial coverage is reported honestly.

Add a journey to journeys.yaml FIRST; this guard then names every registry
that still needs it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
_DOCS = _REPO / "docs" / "journeys"
_AGENT = _REPO / "travel-agent"
_APP = _REPO / "travel-app"
_EVIDENCE_CODES = {"FE", "BE", "VIS", "LIVE"}
_TAXONOMY_KINDS = {"customer_regression", "assurance_pack", "historical"}
_PROOF_LAYERS = {"contract", "database", "device_mock", "persona_replay", "staging", "physical", "ai_eval", "human_outcome"}
_PROOF_STATUSES = {"active", "dark"}


def _manifest() -> tuple[set[str], dict[str, str]]:
    data = yaml.safe_load((_DOCS / "journeys.yaml").read_text()) or {}
    js = data.get("journeys", [])
    return {j["id"] for j in js}, {j["id"]: j["doc"] for j in js}


def _doc_ids() -> set[str]:
    return {"J" + p.name[:2] for p in _DOCS.glob("[0-9][0-9]-*.md")}


def _readme_ids() -> set[str]:
    # Journey rows are `| NN | [Title](doc) | … |` — require the markdown link
    # in column 2 so other tables (e.g. Deferred Surfaces) don't false-match.
    text = (_DOCS / "README.md").read_text()
    return {f"J{m}" for m in re.findall(r"^\|\s*(\d{2})\s*\|\s*\[", text, re.M)}


def _persona_cert_ids() -> set[str]:
    # The legacy script is now only a CLI compatibility shim. Keep this check
    # pointed at the module that owns JOURNEY_PERSONA_MAP.
    p = _AGENT / "scripts" / "journey_cert" / "persona.py"
    return set(re.findall(r'id="(J\d{2})"', p.read_text())) if p.exists() else set()


def _scenarios_ids() -> set[str]:
    p = _APP / "scripts" / "logic-qa" / "scenarios.mjs"
    return set(re.findall(r'id:\s*"(J\d{2})"', p.read_text())) if p.exists() else set()


def _be_test_ids() -> set[str]:
    d = _AGENT / "tests" / "scenarios"
    return (
        {m.group(1).upper() for f in d.glob("test_j*.py") if (m := re.match(r"test_(j\d{2})_", f.name))}
        if d.exists()
        else set()
    )


def _fe_mockwalk_ids() -> set[str]:
    d = _APP / "__tests__" / "journeys"
    return (
        {"J" + m.group(1) for f in d.glob("journey-*-mock-walk.smoke.test.tsx") if (m := re.match(r"journey-(\d{2})-", f.name))}
        if d.exists()
        else set()
    )


def _branch_registry_problems() -> tuple[list[str], int]:
    """Validate optional branch manifests and their registered evidence anchors.

    Empty evidence lists are allowed: they are how the registry represents an
    explicit coverage gap. Non-persona anchors must resolve inside the workspace.
    """
    data = yaml.safe_load((_DOCS / "journeys.yaml").read_text()) or {}
    journeys = data.get("journeys", [])
    journey_ids = {journey.get("id") for journey in journeys}
    seen: set[str] = set()
    problems: list[str] = []
    branch_count = 0

    for journey in journeys:
        jid = journey.get("id")
        for branch in journey.get("branches", []):
            branch_count += 1
            bid = branch.get("id")
            if not isinstance(bid, str) or not re.fullmatch(rf"{re.escape(jid)}\.B\d{{2}}", bid):
                problems.append(f"{jid}: invalid branch id {bid!r}")
                continue
            if bid in seen:
                problems.append(f"duplicate branch id: {bid}")
            seen.add(bid)

            required = branch.get("required_evidence")
            if not isinstance(required, list) or not required:
                problems.append(f"{bid}: required_evidence must be a non-empty list")
                continue
            unknown_required = set(required) - _EVIDENCE_CODES
            if unknown_required:
                problems.append(f"{bid}: unknown required evidence {sorted(unknown_required)}")

            evidence = branch.get("evidence")
            if not isinstance(evidence, dict):
                problems.append(f"{bid}: evidence must be a mapping")
                continue
            unknown_evidence = set(evidence) - _EVIDENCE_CODES
            if unknown_evidence:
                problems.append(f"{bid}: unknown evidence keys {sorted(unknown_evidence)}")

            for code in required:
                anchors = evidence.get(code)
                if not isinstance(anchors, list):
                    problems.append(f"{bid}: {code} evidence must be a list (empty is allowed)")
                    continue
                for anchor in anchors:
                    if not isinstance(anchor, str) or not anchor:
                        problems.append(f"{bid}: {code} contains an invalid anchor")
                        continue
                    if anchor.startswith("persona-cert:"):
                        target = anchor.removeprefix("persona-cert:")
                        if target not in journey_ids:
                            problems.append(f"{bid}: unknown persona-cert journey {target}")
                    elif not (_REPO / anchor).exists():
                        problems.append(f"{bid}: evidence anchor does not exist: {anchor}")

    return problems, branch_count


def _taxonomy_problems(data: dict, journey_ids: set[str]) -> list[str]:
    taxonomy = data.get("taxonomy")
    if not isinstance(taxonomy, dict):
        return ["journeys.yaml: taxonomy must be a mapping"]
    problems: list[str] = []
    if set(taxonomy) != _TAXONOMY_KINDS:
        problems.append(
            "journeys.yaml: taxonomy kinds must be exactly "
            f"{sorted(_TAXONOMY_KINDS)}"
        )
    classified: list[str] = []
    for kind, ids in taxonomy.items():
        if not isinstance(ids, list) or not all(isinstance(jid, str) for jid in ids):
            problems.append(f"journeys.yaml: taxonomy {kind} must be a list of journey ids")
            continue
        classified.extend(ids)
    duplicates = sorted({jid for jid in classified if classified.count(jid) > 1})
    if duplicates:
        problems.append(f"journeys.yaml: taxonomy ids appear more than once: {duplicates}")
    classified_set = set(classified)
    if unknown := sorted(classified_set - journey_ids):
        problems.append(f"journeys.yaml: taxonomy names unknown journeys: {unknown}")
    if missing := sorted(journey_ids - classified_set):
        problems.append(f"journeys.yaml: taxonomy misses journeys: {missing}")
    return problems


def _proof_registry_problems() -> tuple[list[str], int]:
    path = _DOCS / "product-proofs.yaml"
    if not path.exists():
        return ["product proof registry missing: docs/journeys/product-proofs.yaml"], 0
    data = yaml.safe_load(path.read_text()) or {}
    proofs = data.get("proofs")
    if not isinstance(proofs, list):
        return ["product-proofs.yaml: proofs must be a list"], 0
    problems: list[str] = []
    seen: set[str] = set()
    for proof in proofs:
        if not isinstance(proof, dict):
            problems.append("product-proofs.yaml: every proof must be a mapping")
            continue
        pid = proof.get("id")
        if not isinstance(pid, str) or not re.fullmatch(r"P\d{2}", pid):
            problems.append(f"product-proofs.yaml: invalid proof id {pid!r}")
            continue
        if pid in seen:
            problems.append(f"product-proofs.yaml: duplicate proof id {pid}")
        seen.add(pid)
        if proof.get("status") not in _PROOF_STATUSES:
            problems.append(f"{pid}: status must be one of {sorted(_PROOF_STATUSES)}")
        layers = proof.get("required_layers")
        if not isinstance(layers, list) or not layers:
            problems.append(f"{pid}: required_layers must be a non-empty list")
            continue
        unknown_layers = set(layers) - _PROOF_LAYERS
        if unknown_layers:
            problems.append(f"{pid}: unknown required layers {sorted(unknown_layers)}")
        anchors = proof.get("anchors", {})
        if not isinstance(anchors, dict):
            problems.append(f"{pid}: anchors must be a mapping")
            continue
        if proof.get("status") == "active":
            for layer in layers:
                values = anchors.get(layer, [])
                if not isinstance(values, list):
                    problems.append(f"{pid}: {layer} anchors must be a list")
                    continue
                for anchor in values:
                    if not isinstance(anchor, str) or not (_REPO / anchor).exists():
                        problems.append(f"{pid}: evidence anchor does not exist: {anchor}")
    if seen != {f"P{number:02}" for number in range(1, 9)}:
        problems.append("product-proofs.yaml: expected the complete P01–P08 proof spine")
    return problems, len(proofs)


def main() -> int:
    manifest_ids, manifest_docs = _manifest()
    if not manifest_ids:
        print("✗ journeys.yaml has no journeys", file=sys.stderr)
        return 2

    problems: list[str] = []

    missing = [f"{jid} ({doc})" for jid, doc in manifest_docs.items() if not (_DOCS / doc).exists()]
    if missing:
        problems.append("manifest docs missing on disk: " + ", ".join(sorted(missing)))

    for name, ids in (
        ("doc files", _doc_ids()),
        ("README rows", _readme_ids()),
        ("persona-cert specs", _persona_cert_ids()),
    ):
        if manifest_ids - ids:
            problems.append(f"in manifest but not {name}: {sorted(manifest_ids - ids)}")
        if ids - manifest_ids:
            problems.append(f"in {name} but not manifest: {sorted(ids - manifest_ids)}")

    manifest_data = yaml.safe_load((_DOCS / "journeys.yaml").read_text()) or {}
    problems.extend(_taxonomy_problems(manifest_data, manifest_ids))

    branch_problems, branch_count = _branch_registry_problems()
    problems.extend(branch_problems)
    proof_problems, proof_count = _proof_registry_problems()
    problems.extend(proof_problems)

    if problems:
        print("✗ journey-set drift (fix journeys.yaml or the listed registry):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    n = len(manifest_ids)
    print(f"✓ journey set in sync across docs + README + persona-cert ({n} journeys)")
    if branch_count:
        print(f"  branch registry: {branch_count} branches validated")
    print(f"  product proof spine: {proof_count} proofs validated")

    # Informational fidelity coverage — never fails (J13–J19 are lived-only).
    fe, be, sc = _fe_mockwalk_ids(), _be_test_ids(), _scenarios_ids()
    print(
        f"  fidelity coverage: contract(FE) {len(fe & manifest_ids)}/{n} · "
        f"logic(BE) {len(be & manifest_ids)}/{n} · scenarios.mjs {len(sc & manifest_ids)}/{n}"
    )
    for label, ids in (("FE mock-walk", fe), ("BE pytest", be)):
        gap = sorted(manifest_ids - ids)
        if gap:
            print(f"  (no {label} yet: {', '.join(gap)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
