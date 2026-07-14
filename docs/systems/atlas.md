# Atlas (memory & trust) — System Charter

> Surface: Atlas
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-07-13

## Purpose
Atlas is the traveler's durable place memory: saved places, places they have
been, Vesper's readings of their taste, and the evidence behind those readings.
Its Home is a quiet, state-driven archive rather than a dashboard or social
feed. The hero may respond to recent activity, but the underlying record remains
authored, inspectable, correctable, and reversible. Serves belief #21 (One
Engine, Two Corpora): Atlas is the **affinity-corpus twin of Discover**, reading
the traveler's past through the same deterministic editorial brain.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/atlas/`](../../travel-agent/backend/atlas/FEATURE.md) (`taste_board.py` adapter, `story_shape.py::shape_verdict` editorial brain, `significance.py`, `proactive.py` precompute gift, `discovery_reflection.py` flywheel) over the shared [`backend/composition/`](../../travel-agent/backend/composition/FEATURE.md) engine. Routes: `api/routes/atlas.py` (`/api/atlas/*`).
- Frontend: `app/(tabs)/atlas/`, `app/atlas/`, and `components/atlas/` — the
  final Atlas Home, Your Places, Readings, Long View, Inbox review, Your Memory,
  and evidence/receipt detail. Compatibility routes may remain while callers are
  migrated, but they do not define the Home information architecture.
- Tables of record: `traveler_place_affinity` (loved places), Atlas timeline
  projection rows, kept boards, the precomputed-board pool, and
  candidate/artifact/signal state.

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `GET /api/atlas/home` is the landing read model;
  `GET /api/atlas/places`, `/receipt`, `/artifacts`, `/inbox`, `/timeline`, and
  `/timeline/summary` support the durable archive. `/board`, `/boards`, `/parse`,
  and `/facets` remain supporting composition interfaces, not the Home spine.
- **Entry points:** `taste_board.py::compose_taste_board` (thin adapter → `composition.compose_board(variant="atlas")`) · `proactive.py::serve_gift` (lean-back "what Vesper noticed", atomically claims an unshown precomputed board) · `query_parse.py::parse_query`.
- **Consumes:** loved-place affinity (`get_loved_places`), Personal Memory substrate, Discover exploration signal (`get_discovery_reflection`).
- **Never:** fabricate a hero in an empty state; surface a moment without honest provenance; mutate generic account settings under the guise of memory controls.

## Owns (source of truth)
Atlas place affinity, kept boards, timeline **projection** read models, the
precomputed-board pool, and candidate/artifact/signal lifecycle. The composition
*assembly* is owned by `composition/` (shared); Atlas owns **retrieval +
register/copy + the projection rows**. The Home client owns eligibility and
ordering of the approved sections; the API supplies facts, not a parallel visual
hierarchy.

## Invariants (must always be true)
- **Empty state never fabricates a hero** — register/template are chosen by `shape_verdict` (peak/spread, not count): a real pattern fires a `board`, a weak set degrades to a `list` with an honest `register_note`, nothing manufactures a story.
- **Home is eligibility-driven** — hero → actionable Needs Attention → Your
  Places → Readings → at most one timely return → Places You've Been → Whole
  Atlas → rare Learning. Ineligible and empty archive sections are omitted.
- **Blank is useful, not padded** — show search, one combined location row, and
  at most one optional learning entrance (photo or question). Cold start may add
  a provisional hero and 1–3 real saves, but never an empty visited section.
- **Provenance over decoration** — memory claims carry receipts; "Vesper learned X" must be inspectable, disputable, and forgettable (journey 11 "must never happen": forget/dispute that says success but leaves the signal active).
- **Source over confidence theater** — user-facing Memory and Receipt views show
  what Vesper thinks, the supporting evidence, and a correction path; internal
  confidence values never become the visual hierarchy.
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
- why → `product/One Engine, Two Corpora.md` · what(be) →
  `backend/atlas/FEATURE.md` · `backend/composition/FEATURE.md` · what(fe) →
  `travel-app/docs/page-specs/atlas-home.md` ·
  `travel-app/docs/surfaces/atlas-home/contract.md` ·
  `travel-app/docs/surfaces/atlas-memory/contract.md` ·
  `travel-app/docs/surfaces/atlas-receipt/contract.md` · design adjudication →
  `travel-app/docs/surfaces/atlas-home/design-refs/vesper-173-atlas-source.md`.
- Tests: `tests/atlas/*`, `tests/dogfood/test_atlas_dedup_canary.py`, `__tests__/journeys/journey-11-mock-walk.smoke.test.tsx`.

## Operator entry points

- Mock UI: enable screenshot mode, choose an Atlas-capable persona, then open
  `/atlas`, `/atlas/inbox`, or `/atlas/artifact/<id>`.
- Real backend: run the backend with `ATLAS_LLM_ENABLED=false` for deterministic
  composition; enabling the LLM path additionally requires the provider key.
- Candidate lifecycle: scan creates a candidate, review is read-only, and only an
  explicit approval may create the kept artifact. Re-run approval must be idempotent.
- Contract changes begin in backend schemas, flow through the workspace OpenAPI
  snapshot, then regenerate frontend types; handwritten parallel types are forbidden.

The original setup/build ledger is retained in the dated workspace archive.

## Open risks / known gaps
- **Dedup/restore is the headline risk** — the two "must never happen" cases (overlapping trip + memory both visible; deleting a kept memory leaving the trip permanently archived) are correctness-critical and rely on the projector + reconcile staying in sync. Covered by the canary; verify after any projection-version bump.
- Memory **artifact quality is unvalidated** upstream (shared with Memory & Preference) — the "is it worth keeping?" claim has no eval gate yet.
- Compatibility and trust routes need a caller audit after the final Home lands;
  privacy and correction controls must remain memory-specific rather than
  rebuilding a generic account-settings hub inside Atlas.
- Native PhotoKit expansion (burst identifiers, Vision dedup, persistent change
  tokens, Journaling Suggestions, background catch-up) is deferred until cohort
  evidence justifies a custom Expo module/dev-client cutover. Managed-Expo scanning
  remains the supported boundary; see the decision index.
