#!/usr/bin/env python3
"""canon-surface-orphans — inverse sweep of surface-manifest.yaml.

canon-drift-check.py answers "did canon move under a mapped surface?"
This answers the opposite, structural question: "does shipped travel-app
UI exist with NO manifest row at all?" That's the blind spot that let
Planning-Progress Cards (TripShapes/ResearchCard/PlanReadyCard) and
Deck.tsx's raw <Modal> go unnoticed for weeks — the manifest is
canon-indexed, so it can never catch code that has no canon counterpart.

Walks components/*/ and app/*'s top-level entries, checks each against
every `code:` path in the manifest (prefix match), and buckets:
  MAPPED    — a manifest row's code: path covers this dir/file
  PARTIAL   — some but not all of this dir is covered
  ORPHAN    — zero manifest coverage. For orphan dirs, each top-level
              file gets a cheap reachability grep (is it imported
              anywhere outside itself/its test?) so a genuinely dead
              file (imported nowhere) isn't accidentally handed to a
              future audit wave as a real surface to map — that's
              exactly the DeckCompareFace failure mode the
              architecture-simplification audit caught (a component
              with zero renders that still absorbed 3 alignment
              commits).
  EXCLUDED  — orphan, but already on the architecture-simplification
              audit's confirmed-dead-code deletion list. Not a Wave-0
              mapping target; will disappear once that cleanup lands.

Usage: python3 scripts/canon-surface-orphans.py [--verbose]
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "travel-app"
MANIFEST = ROOT / "design" / "surface-manifest.yaml"

# architecture-simplification-2026-07.md FE finding 5 + Tier 0 — confirmed
# dead, scheduled for deletion. Exclude from orphan-mapping targets so
# Wave 0 doesn't hand a future audit wave code that's about to vanish.
ARCH_SIMP_DELETION_LIST = {
    "components/focus-home/DeckCompareFace.tsx",
    "components/atlas/AtlasRoomArt.tsx",
    "components/atlas/AtlasYearStepper.tsx",
    "components/memory/DNAStrip.tsx",
    "components/memory/StoryArchiveCard.tsx",
    "components/memory/TripLogCard.tsx",
    "components/takes/VerdictChip.tsx",
    "app/atlas/almanac.tsx",
    "app/atlas/following.tsx",
    "app/atlas/timeline.tsx",
}

SCAN_ROOTS = ["components", "app"]
SKIP_DIRS = {"__tests__", "node_modules", "dev"}


def load_manifest_paths() -> list[str]:
    data = yaml.safe_load(MANIFEST.read_text())
    paths = []
    for row in data["surfaces"]:
        for c in row.get("code") or []:
            if c.startswith("travel-agent:"):
                continue
            paths.append(c)
    return paths


def is_covered(rel_path: str, manifest_paths: list[str]) -> bool:
    for mp in manifest_paths:
        if mp.endswith("/"):
            if rel_path == mp.rstrip("/") or rel_path.startswith(mp):
                return True
        else:
            if rel_path == mp or rel_path.startswith(mp + "/"):
                return True
    return False


def top_level_entries(scan_root: str) -> list[Path]:
    base = APP / scan_root
    if not base.is_dir():
        return []
    out = []
    for entry in sorted(base.iterdir()):
        if entry.name.startswith(".") or entry.name in SKIP_DIRS:
            continue
        out.append(entry)
    return out


def rel(p: Path) -> str:
    return str(p.relative_to(APP))


def all_files_under(p: Path) -> list[Path]:
    if p.is_file():
        return [p]
    return [f for f in p.rglob("*.ts*") if "__tests__" not in f.parts]


def is_referenced_elsewhere(f: Path) -> bool:
    """Cheap reachability signal: is this file's basename imported
    anywhere else in the app (excluding itself and its own test)?"""
    stem = f.stem
    try:
        result = subprocess.run(
            ["grep", "-rl", "--include=*.ts*", stem, str(APP)],
            capture_output=True, text=True, timeout=15,
        )
    except subprocess.TimeoutExpired:
        return True  # inconclusive — don't falsely flag as dead
    hits = [
        line for line in result.stdout.splitlines()
        if Path(line).resolve() != f.resolve() and "__tests__" not in line
    ]
    return len(hits) > 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    manifest_paths = load_manifest_paths()

    mapped, partial, orphan, excluded = [], [], [], []

    for scan_root in SCAN_ROOTS:
        for entry in top_level_entries(scan_root):
            rp = rel(entry)
            if is_covered(rp, manifest_paths):
                mapped.append(rp)
                continue
            files = all_files_under(entry)
            file_rels = [rel(f) for f in files]
            covered_files = [f for f in file_rels if is_covered(f, manifest_paths)]
            if covered_files and len(covered_files) == len(file_rels):
                mapped.append(rp)
                continue
            if covered_files and len(covered_files) < len(file_rels):
                partial.append((rp, len(covered_files), len(file_rels)))
                continue
            if rp in ARCH_SIMP_DELETION_LIST or all(
                fr in ARCH_SIMP_DELETION_LIST for fr in file_rels
            ):
                excluded.append(rp)
                continue
            orphan.append((rp, files))

    print(f"canon-surface-orphans · manifest has {len(manifest_paths)} FE code: paths\n")

    print(f"MAPPED   ({len(mapped)}) — fully covered by a manifest row")
    if args.verbose:
        for m in mapped:
            print(f"  ✓ {m}")

    print(f"\nPARTIAL  ({len(partial)}) — some files covered, dir itself is not a row")
    for rp, covered, total in partial:
        print(f"  ~ {rp}  ({covered}/{total} files individually mapped)")

    print(f"\nEXCLUDED ({len(excluded)}) — on architecture-simplification's deletion list, not a Wave-0 target")
    for e in excluded:
        print(f"  ✗ {e}")

    print(f"\nORPHAN   ({len(orphan)}) — zero manifest coverage, needs a Wave-0 mapping decision")
    live_orphans = 0
    for rp, files in orphan:
        dead_files = [f for f in files if not is_referenced_elsewhere(f)]
        n = len(files)
        if dead_files and len(dead_files) == n:
            print(f"  ? {rp}  ({n} files, ALL unreferenced elsewhere — dead-code candidate, verify before mapping)")
        else:
            live_orphans += 1
            note = f", {len(dead_files)} unreferenced" if dead_files else ""
            print(f"  → {rp}  ({n} files, referenced in app{note}) — REAL Wave-0 target")

    print(f"\n{live_orphans} orphan surface(s) need a manifest row this wave.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
