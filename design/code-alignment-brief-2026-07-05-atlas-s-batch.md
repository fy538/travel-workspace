# Code Alignment — Atlas Substrate S-Batch: Moment Actions, Significance, Semantic Search (2026-07-05)

Repos: `~/travel-workspace/travel-agent` (backend, Tasks A-BE/B/C) and `~/travel-workspace/travel-app` (frontend, Task A-FE). Three independent tasks; A is the big one (a full vertical feature), B and C are surgical.

## Branch etiquette — READ FIRST

Two unmerged Phase-2 branches may still exist: `code-alignment/phase2-long-view-map-retire` (travel-app) and `code-alignment/phase2-long-view-backend` (travel-agent). Check whether each has merged to main. If NOT merged: stack this batch's branches on top of them (Task A-FE touches `AtlasTasteBoard.tsx`, which the FE phase-2 branch also modified; Task C touches `atlas.py`, which the BE phase-2 branch also modified — branching from main would manufacture conflicts). If merged: branch from main as usual. Note which you did in the report. Standard rules: `git status` first, one commit per coherent step, do NOT push without user approval.

## Task A — Moment Actions, full vertical (the code half of a settled design)

The design canon (Atlas bundle handoff 19+, Canonical Experience Board, "Moment Actions — long-press on any moment (Polish 2, 2026-07-05)" section) specifies a per-moment action sheet inside an opened reading. The design is settled and verified; this task implements it end to end.

### A-BE: exclusion/pin in the compose contract

- `backend/core/models/composition.py` — `ComposeBoardRequest` (line ~281) gains two optional fields: `exclude_ids: list[str]` and `pin_ids: list[str]` (default empty; cap length ~50 each; validate they're well-formed IDs matching whatever the moment/candidate ID type is — investigate what uniquely identifies a moment in `CompositionResult.moments` and use THAT id space consistently).
- Thread them through `compose_taste_query`/`compose_board` (`backend/atlas/taste_board.py` → `backend/composition/core.py`): **exclude** = filter matching candidates out before significance scoring; **pin** = force-include matching candidates and boost/bypass the quality cut so they survive recomposition (pins must not be silently dropped by the quality gate — if a pin can't be honored because the underlying moment no longer exists, return it in a `dropped_pins` field rather than failing).
- **Persistence**: kept boards (`atlas_threads`) store the query — persist exclude/pin lists as part of the saved query JSON so a kept view's exclusions/pins survive reopen and live recomposition. Check `normalize_facet_set`-style idempotency: same query + same exclusions = same board identity, not a duplicate kept row.
- **Dispute routing**: "This isn't right" does NOT need new backend — it routes to the existing per-signal dispute/forget machinery (`atlas.py` ~line 2050). Verify the existing endpoint's shape is callable from a moment context (it may need the artifact/signal id resolvable from the moment — investigate; smallest possible addition if a lookup is missing).
- **"Why this is here"**: the sheet's evidence line needs per-moment provenance in the response. `backend/atlas/models.py` already has `AtlasProvenanceRef` on several read models — check whether `CompositionResult` moments carry enough (source type + date + matched-facet) to render one plain-language line ("Receipt confirmed · Aug 2025 · matched 'bowls & soup'"). If not, add the minimal additive fields. Evidence-first doctrine: NEVER a confidence score or percentage in the payload copy.

### A-FE: the sheet + live recompose

- Long-press (or tap-revealed affordance) on any moment plate inside an opened reading — one shared primitive across Read/Time/Places arrangements in `components/atlas/AtlasTasteBoard.tsx` (the canon is explicit: "Not a per-mode design; one primitive against the shared plate").
- Bottom sheet, Interaction-Surfaces register, exactly four actions: **Why this is here** (provenance line) · **Hide from this view** (adds to `exclude_ids`, recomposes) · **Pin to this view** (adds to `pin_ids`; pinned plates show a small pin glyph) · **This isn't right** (routes to the existing dispute pattern — reuse the Learning-Signal dispute component, don't invent a new one).
- **Recompose pulse**: hide/pin triggers a LOCAL recompose — a quiet loading pulse on the affected plates only, never a full-screen reload (canon: "Recompose pulse — local, not full reload").
- **Live evidence count**: the reading's evidence line updates after recompose (mirrors the heard-screen matched-counts pattern).
- **Thin fallback**: if hiding drops the reading below the honest-composition threshold, fall through to the existing `compose.thin` "This is more of a list than a story" state — never a broken empty reading.
- Works identically on a kept view (exclusions persist via A-BE) and an unsaved reading (exclusions live in session state until kept).

## Task B — Wire artifact-presence into significance (backend only)

`backend/atlas/significance.py` lines ~24-30 explicitly document that `memory_weight` / `artifact_presence` were DEFERRED because `atlas_artifacts` / `atlas_derived_signals` "are EMPTY in the current substrate." They are no longer empty — artifacts and derived signals have been live since late May. Close the loop the file left open:

- Add kept-artifact presence (and optionally derived-signal weight) into the significance blend, exactly where the file's own comments left room. A place the user KEPT a memory about should outrank an otherwise-equal place they merely saved.
- Keep the weighting conservative (this changes board composition for every user) — prefer a small additive term over a rebalance of existing weights, and document the chosen weight with one sentence in the code.
- Tests: extend the existing significance tests with cases proving (a) kept-artifact presence breaks ties upward, (b) an absent-artifact corpus produces identical scores to today (no regression for artifact-less users).

## Task C — Point Atlas search at the Qdrant lane it currently ignores (backend only)

`GET /api/atlas/search` (`backend/api/routes/atlas.py` ~771-855) is plain SQL ILIKE over artifacts + pending candidates + an in-memory phrase substring match — while Universal Search already queries the same `atlas_artifacts` Qdrant collection through an RRF hybrid lane (`backend/search/dispatch.py` ~658-707, dense + BM25 sparse, `pg_trgm` fallback), gated by `ATLAS_SEMANTIC_READ`/`ATLAS_SEMANTIC_WRITE` env flags (note: these are raw `os.getenv` checks in `backend/core/db/atlas.py`, not `feature_flags.py` entries).

- Upgrade the artifact leg of Atlas search to use the same hybrid retrieval Universal Search uses — REUSE the existing lane/vector module (`backend/core/vector/atlas.py`), do not build a second query path.
- Flag-respecting: when `ATLAS_SEMANTIC_READ` is off or Qdrant is unavailable, fall back to today's ILIKE behavior unchanged (same graceful degradation Universal Search has). No behavior change in prod until the flag flips.
- Candidates leg stays SQL (candidates aren't embedded — that's fine, they're transient).
- The phrase-suggestion leg: Phase 1 rerouted its navigation to the receipt screen; leave its matching logic alone.
- Tests: hybrid-on and flag-off paths both covered; assert the flag-off path is byte-identical to current behavior.

## Out of scope

- The true moment-store migration (embedding moments rather than artifacts, decomposing artifact blobs) — post-dogfood L-move, do not start it.
- `matchedCounts` on compose.heard (separate contract, not this batch).
- Any Long View/Map/shelf work (done), any design-file edits.
- Kept-board merge (M-sized, later).

## Definition of done

`exclude_ids`/`pin_ids` accepted, honored through scoring, persisted on kept boards, `dropped_pins` surfaced · Moment Actions sheet live in all three arrangements with local recompose pulse, live evidence count, thin fallback, dispute reuse · significance honors kept artifacts with regression-proof tests · Atlas search uses the shared hybrid lane behind the semantic flags with ILIKE fallback intact · green: tsc, FE tests, BE pytest, mypy · report: moment-ID space chosen (A-BE), weight chosen (B), branch bases used, and any provenance fields added.
