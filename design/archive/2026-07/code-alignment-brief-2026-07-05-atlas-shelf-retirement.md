# Code Alignment — Atlas Shelf Retirement: Phase 1 (2026-07-05)

You are working in `~/travel-workspace/travel-app` (React Native / Expo, expo-router), with the backend at `~/travel-workspace/travel-agent` for reference only (do not modify backend in this batch).

## Context

Atlas's home screen has two coexisting generations: a June-10-era "shelf" of four equal-weight room tiles (Inbox/Map/DNA/Postcards, `AtlasShelfRoomCard` in `components/atlas/AtlasV3Primitives.tsx`, rendered in `app/(tabs)/atlas/index.tsx`), and a June-20-era composition engine (Featured Reading hero, Ways Back In, Read/Time/Places/Reel arrangements) that the current design canon is built around. The shelf pattern was never part of the design canon — it predates it — and it structurally contradicts Atlas's own doctrine ("not a dashboard," "opens with meaning, not input"): a four-tile room grid is a menu, not a composed reading.

This batch executes what's safe to retire NOW. One tile (Map) is explicitly OUT of scope — its job (browsing memories geographically) has no replacement yet; "Long View," the design concept meant to absorb it, is prose-only in the design file with zero artboards. Do not touch Map or anything Map-related in this batch.

## Task A — Retire the DNA archetype-nameplate surface entirely

Doctrine conflict: `dna.tsx` is explicitly a "you are an X traveler" archetype nameplate; Atlas's own Implementation Spec forbids this exact move ("Never say 'You are a water person.' Always say 'Water keeps appearing.'"). It's also redundant — Atlas's Learning Signals already deliver the safe, evidence-first version of the same idea.

Remove:
- `app/atlas/dna.tsx`
- `app/atlas/dna-dimension/[key].tsx` (and the `dna-dimension/` directory if nothing else uses it)
- `app/dna-card.tsx` (the top-level share-card route — this is the route Vesper's own governance table currently assigns to "Atlas canon" as an open gap; it's being retired, not built, so that assignment becomes moot — see the follow-up note at the bottom of this brief)

Do NOT touch:
- `backend/core/context/user_state.py` and `backend/core/world_model/builder.py` — the `_TASTE_AXES = ("energy", "budget", "social", "planning")` constant and `dna_phrase` field are live personalization infrastructure feeding the concierge's identity context. This has nothing to do with the archetype-nameplate screen and must not be removed.
- `components/me/TravelDNACard.tsx` and its use in `components/chat/AttachmentRenderer.tsx` (the `taste_dna_reflection` attachment type) — this is a small, contextual, single-phrase reflection card shown inline in conversation. It's already evidence-first and contestable, not a nameplate — it's the good half of DNA that was built right the first time. Keep it exactly as-is.

Find and remove all navigation entry points into the deleted screens (the DNA tile in the shelf — see Task B — plus any other links, deep-link handlers, or `router.push`/`Link` references to `/atlas/dna`, `/atlas/dna-dimension/*`, `/dna-card`). Add a redirect stub only if there's a real risk of stale external deep links to `/dna-card` (check whether it was ever included in a share flow or notification payload before deciding this is necessary); otherwise a clean 404/removal is fine since these were never public-shared surfaces.

## Task B — Update the Atlas home shelf: 4 tiles → demote 2, remove 1, leave Map alone

In `app/(tabs)/atlas/index.tsx`, the shelf renders `AtlasShelfRoomCard` instances (there are two render sites — likely one per home-state variant, e.g. populated vs. thin-material — update both):

- **Remove the DNA tile** entirely (it has no screen to route to anymore after Task A).
- **Demote Inbox from a persistent tile to a contextual entry point.** The review-queue screen (`app/atlas/inbox.tsx`) stays exactly as it is and stays reachable — just not via a permanent nav tile. Route into it from the existing "N new moments since [date] · surfaced today" provenance line on the Featured Reading hero (this line already exists per the design canon's Polish Session 1 — confirm it's wired in code today; if the line exists but isn't yet tappable, make it tap through to Inbox when there are pending candidates). If no such live wiring exists yet, use the simplest available equivalent (e.g., a small badge/nudge on the composition engine's home surface) rather than inventing new UI — this is a routing change, not a design task.
- **Demote/hide the Postcards tile.** It's already feature-flagged dark (`POSTCARDS_ENABLED=false`) — confirm the tile itself is conditionally rendered only when the flag is on (it may already be; if the tile currently renders unconditionally while the flag only gates the destination screen, fix that so the flag properly hides the tile too).
- **Leave the Map tile untouched.** Do not remove, relabel, or restyle it in this batch — it's explicitly deferred to Phase 2.

After these changes, the shelf should show at most one persistent room tile (Map). If a single-tile "shelf" reads as visually awkward once DNA/Inbox/Postcards are gone, that's expected and fine for this batch — do not redesign the container; flag it in your report rather than improvising a new layout, since any visual change belongs in a design session, not this code batch.

## After each task

- Typecheck (`tsc`) and run the test suite; update/remove any tests that referenced the deleted screens or the old 4-tile shelf assertion, without weakening unrelated tests.
- Grep for dangling references to `dna.tsx`, `dna-dimension`, `dna-card`, and the DNA/Inbox/Postcards tile props — zero hits before committing.
- `git status` first — check for unrelated WIP in this repo before starting, same as prior batches.
- Do NOT push without explicit user approval. Commit each task separately.

## Explicitly OUT of this batch

- Map's tile, screen, or backend (`map_compose.py`) — untouched, Phase 2 dependency.
- The backend `_TASTE_AXES`/`dna_phrase`/world-model integration — untouched, still live infrastructure.
- `TravelDNACard` chat attachment — untouched, keep as-is.
- Any new UI for the now-lighter shelf — flag, don't build.
- `docs/Brief — Memory Surface.md` — leave as historical record for now; a documentation note can follow once this batch lands, but don't block on it.

## Definition of done

DNA screens removed with zero dangling references · backend taste-axis infrastructure and the chat DNA-reflection card untouched and verified still working · shelf shows only the Map tile (Inbox routes contextually, Postcards properly flag-hidden) · green typecheck + tests · short report noting: what was removed, how Inbox's contextual entry was wired, confirmation the Postcards flag now gates the tile itself, and the visual-awkwardness flag if the single-tile shelf looks off.

---

**Separate small follow-up (not part of this code batch):** Vesper's own governance file (`Vesper Canon Consolidation & Ownership.html`, the main app design canon — separate from the Atlas design bundle) currently has a table row assigning `/dna-card` to "Atlas canon" as an open design gap. Since `/dna-card` is being retired rather than built, that row should be updated to reflect the retirement next time a Vesper design session runs — it's a one-line edit, not worth its own session.
