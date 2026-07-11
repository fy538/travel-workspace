# Code Alignment — Atlas Batch C: Make the Loop Real + Complete Correction (2026-07-06)

Repos: `~/travel-workspace/travel-app` (FE) + `~/travel-workspace/travel-agent` (BE), branch main. Follows Batch A+B (merged PR #45/#135). Theme: the reciprocal-loop half of the Atlas vision — "keeping grows readings" and "correction overrides all inference." From the PM journey audit (docs/atlas/atlas-user-journeys-2026-07-06.md).

Process: `git status` first (concurrent Atlas worktrees exist). Branch from main. One commit per task. No push without approval. After each: `tsc` + FULL `TZ=UTC npx jest` / BE `pytest` + `mypy`. Ground every change in the vision.

---

## C1 — Close the seam for real: keeping a memory writes an affinity edge

**Context (the B2 finding):** Batch B2 flipped `ATLAS_SIGNALS_TO_MEMORY` on, but the test `test_emission_never_touches_place_affinity` proved it only writes a *concierge Personal-Memory observation* — NOT a `place_affinity` edge. So keeping a memory of a **brand-new** place still cannot make it *enter* a taste-board reading; it only re-ranks places already in the affinity graph via the +0.05 name-match. The "keep grows readings" promise is still unfulfilled for new places. This task closes it.

**The design's Memory-tier is currently the one evidence tier that never becomes a weighted affinity signal.** Existing `record_place_affinity` call sites (`backend/core/db/place_affinity.py:79` is the sole write path): save (1.0), plan_add (1.5), pick_commit (2.0), mark_happened (1.5).

**Fix (BE):**
- In the artifact-keep path (single `approve_candidate` and `keep_all_candidates`, `backend/api/routes/atlas.py`), after the artifact is persisted with `state='kept'`, call `record_place_affinity` for the artifact's place — a **Memory-tier** signal with a new `source` value (e.g. `"kept_memory"`). This makes a kept place eligible to *enter* a reading, not just reorder.
- **Weight decision (locked recommendation, tune if needed): 2.0.** Rationale: a kept memory is the strongest evidence tier — the user was demonstrably there AND deliberately chose to keep it (Action + Correction combined). Match or exceed `pick_commit`. If you disagree after seeing the blend, report the chosen weight and why.
- **Resolvability:** the artifact must carry a resolvable `entity_id`/place for the affinity row (affinity is keyed on `(user_id, entity_type, entity_id)`). If a scanned/geocoded artifact only has a `place_label` string and no entity_id, you'll need to resolve/create a place entity (or key affinity on the normalized label consistent with how `artifact_presence` name-matches today). INVESTIGATE and report the resolution path — this is the one real design question in this task. If it can't be done cleanly without the full moment-store migration, STOP and report; do not force it.
- Idempotency: keeping the same place twice must not double-count beyond the intended weight accrual (affinity `weight` accumulates by design — confirm the evidence-append dedupes on source).
- Tests: keeping a memory of a NEW place makes it appear in a composed reading (the round-trip B2 couldn't yet prove); dispute/forget of that memory removes the edge (correction symmetry).

## C2 — Build the home Learning Signal (canon §8 P0 component)

**Context:** `utils/atlasLearningSignal.ts` (`buildAtlasLearningSignal`) is orphaned — zero importers. The pattern-level "Atlas is learning · Water keeps appearing · Is this right?" correction loop — a required canon P0 component and the primary evidence-first trust mechanism — is absent from the home. (Moment-level "This isn't right" exists; the home pattern-level signal does not.)

**Fix (FE):**
- Wire `buildAtlasLearningSignal` into the Atlas home (`app/(tabs)/atlas/index.tsx`), rendering the canon §8 module: an evidence-first line ("Water keeps appearing · 14 shores") + an "Is this right?" affordance with `looks_right` / `not_quite` responses.
- Evidence-first, NEVER a confidence score. `not_quite` routes to the same dispute/correction machinery as J12 → the correction suppresses that pattern permanently (verify it actually suppresses, per "correction overrides all inference").
- Placement per canon (a quiet home module, not the hero). Honest absence: if there's no learned pattern with enough evidence, the module doesn't render (no empty shell).
- Confirm the backend surfaces a "learning signal" pattern (what `buildAtlasLearningSignal` consumes) — if the data isn't there, wire the minimal read; if it is, just consume it.
- Tests: the signal renders with real pattern data; `not_quite` fires the correction; honest-absence when no pattern.

## C3 — Dispute/forget = global scope (locked decision)

**Context:** `patch_atlas_moment` (`backend/api/routes/atlas.py:2118`) documents that correction is "intentionally scoped to Atlas composition… Discover/home/notifications, which read the same affinity table, are unaffected." So a forgotten place still drives Discover recs + home nudges. Violates canon "User correction = override… suppressed permanently."

**Fix (BE):**
- Make dispute/forget suppress the place across ALL affinity readers, not just Atlas composition. Investigate how `user_state='disputed'` is (or isn't) honored by the Discover/home/notification affinity reads and extend the filter so a disputed/forgotten place is suppressed everywhere.
- Update the docstring to match the new global behavior.
- Verify no surface still surfaces a forgotten place (Discover recs, home loved-places, notifications).
- Tests: a disputed place is absent from Atlas readings AND Discover/home affinity reads.

---

## Explicitly OUT of Batch C
- The full moment-store L-move (per-moment decomposition, MomentEvidence object) — C1 is the *targeted* affinity-edge close, NOT the migration. If C1 can't be done without the migration, report and stop.
- Long View bugs, push routing, photo permanence (Batch D). Provenance glyphs, freshness states, hero/cold polish, virtualization (Batch E).

## Definition of done
C1: keeping a memory of a new place makes it enter a reading (round-trip test green), correction removes the edge, weight + resolution path reported. C2: home Learning Signal live, evidence-first, correction suppresses, honest absence, tests. C3: forget is global, no surface leaks a disputed place, tests. Green tsc + FE jest (full) + BE pytest + mypy. Report: the C1 entity-resolution path + chosen weight; whether C1 hit the migration wall.
