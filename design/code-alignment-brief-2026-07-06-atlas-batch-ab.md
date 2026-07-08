# Code Alignment — Atlas Batch A+B: Honesty Fixes + Close the Loop (2026-07-06)

Repos: `~/travel-workspace/travel-app` (FE) + `~/travel-workspace/travel-agent` (BE), branch main. From the Atlas PM journey audit (docs/atlas/atlas-user-journeys-2026-07-06.md). Two batches:
- **A** = the two P0 honesty bugs (would actively mislead a tester — non-negotiable, small).
- **B** = close the reciprocal loop (make keeping visibly enrich readings).

Process: `git status` first (concurrent-session hazard — several Atlas worktrees exist). Branch from main. One commit per task. Do NOT push without approval. After each task: `tsc` + FE jest (`TZ=UTC npx jest`, FULL directory not targeted) / BE `pytest` + `mypy`. Ground every change in the Atlas vision: "never fake a story," "evidence-first," "keeping grows readings," "living views."

Four product decisions are ALREADY LOCKED (do not re-litigate): (1) single-approve → `state='kept'`, kill "composed" as user-facing; (2) `ATLAS_SIGNALS_TO_MEMORY` on; (3) dispute/forget = global scope; (4) re-engagement flags + J7 auto-candidate are OUT of this batch.

---

## BATCH A — The two honesty P0s

### A1 — Recompose is a local pulse, not a full-screen reload

**The bug:** Hide/Pin/Dispute inside a reading change the React Query key (`momentActionsKey`, `data/atlas.ts:388`) → the new key has no cache → `useData` returns `isLoading: true` (`hooks/useData.ts:107`) → `app/atlas/board.tsx:305` swaps `<AtlasTasteBoard>` for the full-screen "Making your reading" spinner. The intended local dim (`isRecomposing` → `recomposeStyle` opacity 0.55, `AtlasTasteBoard.tsx:446-449,535`) therefore ONLY renders in mock mode. An in-code comment (`AtlasTasteBoard.tsx:530-532`) falsely claims "a local pulse, never a full-screen reload." Violates Atlas Polish-2 ruling 10.

**Fix:**
- Widen `useData`'s `options` Pick (`hooks/useData.ts:43`) to also accept `placeholderData`, and thread it into the `useQuery` call. (React Query v5: `placeholderData: keepPreviousData` imported from `@tanstack/react-query`.)
- In `useAtlasBoard` (`data/atlas.ts:324`), pass `placeholderData: keepPreviousData` so a Moment-Actions key change keeps the previous board mounted (`isLoading` stays false; `isFetching` goes true).
- In `board.tsx`, drive `isRecomposing` off the query's `isFetching`-while-has-data (expose it from the hook if needed), so the 0.55 dim fires in REAL mode. Confirm the full-screen `isLoading` branch (`:305`) now only fires on the genuine first load, not on re-steers.
- Remove/repair the false "never a full-screen reload" comment so it matches reality.
- Test: add/adjust a board test proving a moment-action key change does NOT unmount to the loading state in real-mode simulation.

### A2 — Mock prose must not ship as authored "VESPER WROTE"

**The bug:** with `ATLAS_LLM_ENABLED` off (default), every single-approve produces generic mock copy (`travel-agent/backend/atlas/composer.py:181-203`) rendered under a gold "VESPER WROTE" eyebrow (`app/atlas/artifact/[id].tsx:217`) with a "· kept by Vesper" header (`:185`); the only honesty badge is `__DEV__`-gated (`:187`) — invisible in release. Violates "never fake a story / it won't fake a story before there's a shape."

**Fix (FE, honesty-first):**
- The artifact carries `composed_by` (`'mock' | 'llm'`). When `composed_by === 'mock'`, the artifact detail must NOT present the one-line/sections as authored Vesper prose. Options (pick the one truest to canon — likely the first): (a) render an honest **"draft reading"** treatment — eyebrow reads e.g. `DRAFT · not yet composed` instead of `VESPER WROTE`, muted styling, and a quiet "Vesper will write this up" affordance; or (b) suppress the prose entirely and show the honest evidence (place/date/photos) without a fabricated narrative, mirroring the compose-thin honesty.
- Make the honest state visible in RELEASE builds, not `__DEV__` only. Remove the `__DEV__` gate on the mock indicator (`:187`).
- Fix the hardcoded "· kept by Vesper" (`:185`) — it must reflect real `state` (and after A/B is done, the header should read honestly for a kept-but-mock-copy artifact).
- Keep the LLM-composed path (`composed_by === 'llm'`) rendering the full "VESPER WROTE" reading unchanged.
- Do NOT touch the mock composer itself — the mock being deterministic/generic is correct; the bug is presenting it as authored.

---

## BATCH B — Close the loop (keeping enriches readings)

### B1 — Kill the kept/composed trap (single-approve → kept)

**Decision (locked):** `state` = user intent (did they keep it), `generation_status` = compose progress (is the copy ready). These are orthogonal; the LLM-upgrade async flow rides `generation_status`, NOT `state`.

**Fix (BE):**
- Single `approve_candidate` (`travel-agent/backend/api/routes/atlas.py` approve path) currently inserts with the table default `state='composed'` (`backend/atlas/models.py:385,409`). Change the single-approve insert to write **`state='kept'`** — matching keep-all. Investigate `async_insert_artifact` / the approve context to set this cleanly.
- Confirm the significance `artifact_presence` term (`significance.py`, `get_kept_artifact_place_labels`) now picks up single-approved artifacts (it filters `state='kept'`).
- Audit for any code that treats `composed` as a meaningful *user-facing* state vs the internal generation flow — "composed" should survive only as an internal/legacy value, never surfaced. The `_upgrade_kept_artifacts_bg` LLM-upgrade path keys on `generation_status`/the flag, so verify it still works with `state='kept'` from the start.
- Tests: single-approve produces `state='kept'`; a kept single-approved place feeds the +0.05 significance term (extend the existing significance test).

### B2 — Flip ATLAS_SIGNALS_TO_MEMORY on + verify the emission fires

**Decision (locked):** on. The emission path is wired (`async_record_artifact_signal_observations`, called from approve at `atlas.py:1877` and keep-all at `:1679`, gated by `atlas_signals_to_memory_enabled()`).

**Fix:**
- This is primarily a config flip (env var). In code: confirm no hardcoded default blocks it, and that flipping it on makes a kept artifact emit its `derived_signals` as low-weight Personal-Memory observations (source_mode="reflection") with the revocation half symmetric (dispute → forget the observation).
- Verify the round-trip: keep a memory of a NEW place (not already a loved affinity) → does it now become eligible to *enter* a composed reading (not just reorder within one)? If the emission only writes to Personal Memory but doesn't create/boost an affinity edge that the taste board reads, note the gap — the goal is that keeping a memory can make a place *appear* in a reading. Report exactly how far the wired path gets and what (if anything) is still missing to make "keep → place enters reading" true.
- Tests: enabling the flag emits observations on approve; disabling is a clean no-op (regression-safe).

### B3 — The "N new moments since" provenance line (the felt "my Atlas changed" moment)

**Context:** canon §2A Default Home specifies a provenance line like "3 new moments since May · surfaced today" under the Featured Reading — currently UNBACKED. `CompositionResult.source_counts` (`composition.py:207`, populated `core.py:625`) gives totals, not a delta.

**Fix (scope honestly):**
- Determine the cheapest honest delta: e.g. count moments with a `surfaced_at`/`first_seen` newer than the user's last Atlas-home view (or newer than when the featured reading was last composed). `AtlasArtifact`/candidate models carry `surfaced_at` (`models.py:456+`).
- If a true "new since last visit" delta is cheap → wire it and render the canon's provenance line on the home hero (`AtlasHomeBoardHero`) + optionally the opened reading.
- If a real delta is NOT cheap in this batch → render an HONEST alternative that isn't fabricated (e.g. total-based "14 moments · 5 cities" which already exists) and RECORD that the "new since" delta is deferred — do NOT ship a faked "3 new since May" with invented numbers. Honesty over the exact canon string.

---

## Explicitly OUT of this batch
- Re-engagement flags (anniversary/seasonal), J7 auto-candidate (unbuilt + needs photo-reconciliation arch), photo-permanence rehost, Long View bugs, On This Day push routing, provenance glyphs, Ways Back In freshness, hero single-CTA, cold-state fake-tile grid, ASK-label, Reel-as-arrangement, FE virtualization. Those are Batches C–E.
- The mock composer's copy content (correct as-is).

## Definition of done
A1: recompose is a local dim in REAL mode, first-load spinner only on genuine first load, false comment fixed, test added. A2: mock artifacts never present as authored "VESPER WROTE" in release; honest draft/evidence state visible; "kept by Vesper" reflects real state. B1: single-approve → state='kept', significance picks it up, tests. B2: signals-to-memory on, emission verified, round-trip reported (how far "keep → place enters reading" gets). B3: honest provenance line (real delta, or honest total + deferred note — never fabricated). Green tsc + FE jest (full) + BE pytest + mypy. Report: the B2 round-trip finding, the B3 delta decision, and any composed-state usage that had to stay internal.
