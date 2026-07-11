#!/usr/bin/env python3
"""Journey-set drift guard — assert every journey registry agrees with the
canonical manifest (docs/journeys/journeys.yaml). Pure file-parse, NO DB —
runs in CI alongside the contract checks.

DEFINITION registries (must match the manifest exactly → exit 1 on drift):
  - docs/journeys/<NN>-*.md          one-pager per journey
  - docs/journeys/README.md          index table rows
  - dogfood_journey_persona_cert.py  JOURNEY_PERSONA_MAP specs (lived)

FIDELITY subset (informational, never fails): scenarios.mjs / BE pytest /
FE mock-walk are the core contract/logic layer — J13–J19 are intentionally
lived-only so far, so partial coverage there is expected and just reported.

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

    if problems:
        print("✗ journey-set drift (fix journeys.yaml or the listed registry):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    n = len(manifest_ids)
    print(f"✓ journey set in sync across docs + README + persona-cert ({n} journeys)")

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
