#!/usr/bin/env python3
"""canon-drift-check — answer "how far is the code from canon N" in one command.

Diffs the local read-only canon mirror against the newest design handoff export,
then cross-references every changed canon file against `design/surface-manifest.yaml`
to say which SURFACE's CODE is now stale — not just which design file moved. This
is the mechanism that closes the gap flagged by the deep-research pass: neither
token linting nor visual regression tools compare code against a static design
mockup, so this ledger is the thing doing that job. Only surfaces whose canon
actually changed get flagged — everything else keeps its last-verified status,
so a re-verify pass only ever touches what moved (never a full re-audit).

  mirror   = ~/travel-workspace/design/vesper-canon-anchor/project   (what code was aligned to)
  handoff  = newest ~/Downloads/vesper <N>/project                    (current canonical design)
  manifest = design/surface-manifest.yaml                             (canon ↔ code ledger)

Reports, per changed/new/removed file: the surface it belongs to, its manifest
status/aligned_at/code pointers (if mapped), and the change magnitude. Noise
(thumbnails, screenshots, canvas state, uploads) is ignored.

Exit 0 = mirror matches newest handoff (no pass needed).
Exit 1 = drift detected (a pass may be warranted — see the magnitude column).
Exit 2 = couldn't locate mirror, any handoff, or the manifest.

Usage:
  python3 scripts/canon-drift-check.py                # newest handoff vs mirror
  python3 scripts/canon-drift-check.py --handoff 119  # pin a specific handoff number
  python3 scripts/canon-drift-check.py --sync         # after review, advance the mirror to newest
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

HOME = Path.home()
MIRROR = HOME / "travel-workspace/design/vesper-canon-anchor/project"
DOWNLOADS = HOME / "Downloads"
MANIFEST = HOME / "travel-workspace/design/surface-manifest.yaml"

# Files/dirs that change every export but carry no design signal.
IGNORE_NAMES = {".thumbnail", ".design-canvas.state.json"}
IGNORE_DIRS = {"screenshots", "uploads"}

# Map a filename to the human surface it belongs to, for grouped reporting.
# Order matters — first substring hit wins.
SURFACE_HINTS = [
    ("header", "Header system"),
    ("trip-story", "Trip Story"),
    ("trip story", "Trip Story"),
    ("notification", "Notifications"),
    ("people-collab", "People & Collaboration"),
    ("people and collab", "People & Collaboration"),
    ("places", "Places"),
    ("costs", "Costs"),
    ("stay", "Stay"),
    ("booking", "Booking"),
    ("proposal", "Proposal & Decision"),
    ("changes", "Changes"),
    ("itinerary", "Itinerary"),
    ("create", "Trip Creation"),
    ("trips-home", "Trips Home"),
    ("trips home", "Trips Home"),
    ("discover", "Discover"),
    ("atlas", "Atlas"),
    ("chat", "Chat"),
    ("stay", "Stay"),
    ("trust", "Trust & Controls"),
    ("onboarding", "Onboarding"),
    ("auth", "Auth & Invite"),
    ("universal-search", "Universal Search"),
    ("state", "State System"),
    ("card", "Cards"),
    ("row", "Row System"),
]


def surface_for(name: str) -> str:
    low = name.lower()
    for needle, label in SURFACE_HINTS:
        if needle in low:
            return label
    return "Other / cross-cutting"


def load_manifest() -> list[dict]:
    if not MANIFEST.is_file():
        print(f"✗ manifest not found: {MANIFEST} (drift-check runs canon-file-name grouping only)", file=sys.stderr)
        return []
    with MANIFEST.open() as f:
        data = yaml.safe_load(f)
    return data.get("surfaces", [])


def canon_to_surfaces(manifest: list[dict]) -> dict[str, list[dict]]:
    """Reverse index: canon FILENAME (not path) → every surface row that lists it."""
    index: dict[str, list[dict]] = {}
    for row in manifest:
        for c in row.get("canon") or []:
            index.setdefault(Path(c).name, []).append(row)
    return index


def handoff_number(p: Path) -> int | None:
    m = re.fullmatch(r"vesper (\d+)", p.name)
    return int(m.group(1)) if m else None


def newest_handoff(pin: int | None) -> Path | None:
    candidates = []
    for child in DOWNLOADS.iterdir():
        if not child.is_dir():
            continue
        n = handoff_number(child)
        if n is None:
            continue
        if pin is not None and n != pin:
            continue
        proj = child / "project"
        if proj.is_dir():
            candidates.append((n, proj))
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0])  # numeric, so 119 > 99
    return candidates[-1][1]


def is_ignored(rel: Path) -> bool:
    if any(part in IGNORE_DIRS for part in rel.parts):
        return True
    return rel.name in IGNORE_NAMES


def list_files(root: Path) -> set[Path]:
    out: set[Path] = set()
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            rel = Path(dirpath, f).relative_to(root)
            if not is_ignored(rel):
                out.add(rel)
    return out


def changed_line_count(a: Path, b: Path) -> int:
    try:
        at = a.read_text(errors="replace").splitlines()
        bt = b.read_text(errors="replace").splitlines()
    except (UnicodeDecodeError, OSError):
        return -1  # binary / unreadable — treat as "changed, size unknown"
    diff = difflib.unified_diff(at, bt, n=0)
    return sum(1 for line in diff if line and line[0] in "+-" and not line.startswith(("+++", "---")))


def main() -> int:
    ap = argparse.ArgumentParser(description="Canon mirror ↔ newest design handoff drift check")
    ap.add_argument("--handoff", type=int, default=None, help="Pin a specific handoff number instead of newest")
    ap.add_argument("--sync", action="store_true", help="After review, advance the mirror to the handoff (rsync --delete)")
    args = ap.parse_args()

    if not MIRROR.is_dir():
        print(f"✗ mirror not found: {MIRROR}", file=sys.stderr)
        return 2
    handoff = newest_handoff(args.handoff)
    if handoff is None:
        where = f"vesper {args.handoff}" if args.handoff else "any 'vesper <N>' dir"
        print(f"✗ no handoff found ({where}) under {DOWNLOADS}", file=sys.stderr)
        return 2

    hn = handoff_number(handoff.parent)
    mirror_files = list_files(MIRROR)
    handoff_files = list_files(handoff)

    added = sorted(handoff_files - mirror_files)
    removed = sorted(mirror_files - handoff_files)
    common = sorted(mirror_files & handoff_files)

    modified: list[tuple[Path, int]] = []
    for rel in common:
        m = MIRROR / rel
        h = handoff / rel
        if m.stat().st_size == h.stat().st_size and m.read_bytes() == h.read_bytes():
            continue
        modified.append((rel, changed_line_count(m, h)))

    print(f"canon-drift-check · mirror ↔ handoff {hn}")
    print(f"  mirror : {MIRROR}")
    print(f"  handoff: {handoff}")
    print()

    if not added and not removed and not modified:
        print(f"✓ IN SYNC — mirror already matches handoff {hn}. No alignment pass needed.")
        return 0

    manifest = load_manifest()
    reverse = canon_to_surfaces(manifest)

    # Group everything by surface for a readable picture.
    rows: list[tuple[str, str, str]] = []  # (surface, magnitude, label)
    for rel in added:
        rows.append((surface_for(rel.name), "NEW", str(rel)))
    for rel in removed:
        rows.append((surface_for(rel.name), "REMOVED", str(rel)))
    for rel, n in modified:
        mag = "binary" if n < 0 else f"{n} lines"
        rows.append((surface_for(rel.name), mag, str(rel)))

    by_surface: dict[str, list[tuple[str, str]]] = {}
    for surface, mag, label in rows:
        by_surface.setdefault(surface, []).append((mag, label))

    print(f"DRIFT DETECTED — {len(added)} new · {len(removed)} removed · {len(modified)} modified\n")

    # ── Manifest cross-reference: which SURFACES (with their code pointers)
    #    are now stale, because their canon files are among what changed.
    #    This is the actual "how far is the code from canon N" answer — the
    #    file-grouping below only tells you what moved in the DESIGN, not
    #    what to go check in the APP.
    touched_names = (
        {rel.name for rel in added}
        | {rel.name for rel in removed}
        | {rel.name for rel, _ in modified}
    )

    now_stale: list[dict] = []
    intentionally_unaffected: list[dict] = []
    seen_surfaces: set[str] = set()
    for name in touched_names:
        for surf in reverse.get(name, []):
            key = surf["surface"]
            if key in seen_surfaces:
                continue
            seen_surfaces.add(key)
            if surf.get("status") in ("deferred", "unmapped"):
                intentionally_unaffected.append(surf)
            else:
                now_stale.append(surf)

    if now_stale:
        print(f"⚠ {len(now_stale)} surface(s) with mapped code are now STALE (canon moved, code not re-checked):\n")
        for surf in sorted(now_stale, key=lambda s: s["surface"]):
            code = surf.get("code") or ["(no code paths recorded)"]
            print(f"  {surf['surface']}  [was: {surf.get('status')}, aligned_at: {surf.get('aligned_at')}]")
            for c in code:
                print(f"    → {c}")
            if surf.get("notes"):
                print(f"    note: {surf['notes']}")
            print()

    if intentionally_unaffected:
        names = ", ".join(sorted(s["surface"] for s in intentionally_unaffected))
        print(f"  (canon also moved for {names} — status is deferred/unmapped, no re-check owed unless you're picking one up)\n")

    unmapped_files = [n for n in touched_names if n not in reverse]
    if unmapped_files:
        print(f"  {len(unmapped_files)} changed file(s) aren't in any manifest row yet — grouped by filename heuristic below.\n")

    for surface in sorted(by_surface):
        print(f"  {surface}")
        for mag, label in sorted(by_surface[surface], key=lambda t: t[1]):
            print(f"    {mag:>12}  {label}")
        print()

    # Heuristic verdict: separate "substantive" (>40 changed lines or new/removed
    # non-trivial file) from "adoption plumbing" (tiny edits).
    substantive = [
        (mag, label) for _s, mag, label in rows
        if mag in ("NEW", "REMOVED", "binary")
        or (mag.endswith(" lines") and int(mag.split()[0]) > 40)
    ]
    print("verdict:")
    if now_stale:
        print(f"  Re-verify code for: {', '.join(sorted(s['surface'] for s in now_stale))}.")
    if substantive:
        print(f"  {len(substantive)} substantive change(s) — worth scoping an alignment batch:")
        for mag, label in sorted(substantive):
            print(f"    · {label} ({mag})")
        print("  The rest is small edits / adoption plumbing — fold in opportunistically.")
    elif not now_stale:
        print("  Only small edits — no substantive delta. Not worth a dedicated pass; fold in when nearby.")

    if args.sync:
        print(f"\n--sync: advancing mirror to handoff {hn} (rsync --delete)…")
        subprocess.run(
            ["rsync", "-a", "--delete", f"{handoff}/", f"{MIRROR}/"],
            check=True,
        )
        print("  mirror updated.")

    return 1


if __name__ == "__main__":
    sys.exit(main())
