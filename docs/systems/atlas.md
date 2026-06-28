# Atlas (memory & trust) — System Charter

> Surface: Atlas
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-06-27

## Purpose
Composes the traveler's **own loved places** into editorial taste boards, and
makes Vesper's memory inspectable and controllable — a private map of where
you've been, not a social feed. Serves belief #21 (One Engine, Two Corpora):
Atlas is the **affinity-corpus twin of Discover**, reading your past through the
same deterministic editorial brain. Memory without provenance or control feels
creepy (journey 11), so provenance and reversibility are the product.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/atlas/`](../../travel-agent/backend/atlas/FEATURE.md) (`taste_board.py` adapter, `story_shape.py::shape_verdict` editorial brain, `significance.py`, `proactive.py` precompute gift, `discovery_reflection.py` flywheel) over the shared [`backend/composition/`](../../travel-agent/backend/composition/FEATURE.md) engine. Routes: `api/routes/atlas.py` (`/api/atlas/*`).
- Frontend: `app/(tabs)/atlas/` + `components/atlas/` — home/desk/ribbon, inbox, candidate/artifact/learned, almanac, timeline, map, postcards, privacy, trust hub (profile/account/constraints/data-receipt/delegation/following).
- Tables of record: `traveler_place_affinity` (loved places), Atlas timeline/almanac projection rows, precomputed-board pool, candidate/artifact/signal state.

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `GET /api/atlas/board` (and `/parse`, `/facets` → `suggestions`, `/timeline`, `/almanac`, `/saved boards`, `/intended-destination`).
- **Entry points:** `taste_board.py::compose_taste_board` (thin adapter → `composition.compose_board(variant="atlas")`) · `proactive.py::serve_gift` (lean-back "what Vesper noticed", atomically claims an unshown precomputed board) · `query_parse.py::parse_query`.
- **Consumes:** loved-place affinity (`get_loved_places`), Personal Memory substrate, Discover exploration signal (`get_discovery_reflection`).
- **Never:** fabricate a hero in an empty state; surface a moment without honest provenance; mutate generic account settings under the guise of memory controls.

## Owns (source of truth)
Atlas taste boards, the timeline/almanac **projection** read models, the
precomputed-board pool, and candidate/artifact/signal lifecycle. The composition
*assembly* is owned by `composition/` (shared); Atlas owns **retrieval +
register/copy + the projection rows**.

## Invariants (must always be true)
- **Empty state never fabricates a hero** — register/template are chosen by `shape_verdict` (peak/spread, not count): a real pattern fires a `board`, a weak set degrades to a `list` with an honest `register_note`, nothing manufactures a story.
- **Provenance over decoration** — memory claims carry receipts; "Vesper learned X" must be inspectable, disputable, and forgettable (journey 11 "must never happen": forget/dispute that says success but leaves the signal active).
- **Private map, not a social feed** — Atlas is the traveler's own retrospective; provenance is left None (your past is inherently trusted), privacy is leaned on, not publication.
- **Dedup is one visible truth** — an overlapping trip + kept memory dedupe to **one** timeline/almanac entry (trip projection archived `dedup`); deleting the kept memory **restores** the trip (never permanently archived).
- **Candidate approval is exactly-once** — no duplicate artifacts; photo-scan never uploads private data before explicit approval.
- **Parse honesty** — `parse_query` keeps unmapped text in `residual_phrase`, never invents a dimension.
- **Adapter discipline** — `taste_board.py` owns retrieval + copy only; assembly behavior lives in `composition/` and changing it moves both Atlas and Discover.

## Failure modes
- Shape brain (deterministic) "raises" (it never does) → `compose_board` falls back to a count heuristic via `_BOARD_MIN`.
- Quality gate finds a defect → **downgrades** board → list → empty, never upgrades or fabricates.
- Legacy account pre-projection-v4 → lazy rebuild on first timeline/almanac access (`ensure_timeline_projected`).

## Maturity & validation
- Serves journeys: 11 (candidate → memory control), 12 (returned trip → memory).
- DoD state: dedup/restore Postgres canary ✅ (`tests/dogfood/test_atlas_dedup_canary.py`), projection-v4 backfill ✅, map/home read-model tests ✅, full mock walk ✅ (`journey-11-mock-walk.smoke.test.tsx`) · **legacy-account live spot-check optional/manual**.
- Dark/deferred: Layer-2 VLM judge (`quality_gate.py::vlm_judge` no-op stub, needs credits); live almanac LLM smoke excluded from CI.

## Canonical docs
- why → `product/One Engine, Two Corpora.md` · what(be) → `backend/atlas/FEATURE.md` · `backend/composition/FEATURE.md` · what(fe) → `page-specs/atlas-home.md` · `page-specs/atlas-backend-contracts.md` · `page-specs/atlas-signal-controls.md`.
- Tests: `tests/atlas/*`, `tests/dogfood/test_atlas_dedup_canary.py`, `__tests__/journeys/journey-11-mock-walk.smoke.test.tsx`.

## Open risks / known gaps
- **Dedup/restore is the headline risk** — the two "must never happen" cases (overlapping trip + memory both visible; deleting a kept memory leaving the trip permanently archived) are correctness-critical and rely on the projector + reconcile staying in sync. Covered by the canary; verify after any projection-version bump.
- Memory **artifact quality is unvalidated** upstream (shared with Memory & Preference) — the "is it worth keeping?" claim has no eval gate yet.
- Trust-hub routes (profile/account/constraints/data-receipt/delegation/following) became canonical when Me tab was removed — confirm none are orphaned and privacy controls stay memory-specific, not generic account settings.
