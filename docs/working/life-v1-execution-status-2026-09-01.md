---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-04
expires: 2026-10-01
why_new: Records the executed, cross-repository Life v1 foundation and its validation evidence so future design work can build on committed seams rather than re-open the architecture.
depends_on:
  - life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
  - life-v1-destination-and-refinding-contract-2026-09-01.md
  - ../contracts/life-v1-experience.md
  - ../systems/four-root-loop-object-surface.md
---

# Life v1 — execution status

## Outcome

The non-regrettable Life foundation, bounded refinding slice, and shared
artifact/root runtime are now integrated and represented in the generated
contract snapshots. The result is additive and reversible: the existing
Atlas/You history owner remains intact, while internal flags can expose a native
Time root and a truth-aware refinding lane backed by typed read projections.
No public promotion, generalized dossier system, Together persistence, or
repository-wide noun migration was attempted.

Landed review refs: `baseline/four-root-convergence-2026-09-01` in each
repository; the complete-record slice is app `dc4f1f66c` and backend
`fc361aeed`. The child `main` branches may advance independently with other
in-flight work.
Safety tags preserve every pre-convergence `main`; the convergence receipt
records the final local workspace landing.

## Landed checkpoints

### Backend (`Travel Agent`)

- `029e22870` — pure dark Life projection compiler.
- `1190a707c` — deterministic cross-root Return arbitration.
- `115c00d41` — additive `GET /api/root-projections/v1/life` route and adapter.
- `0f2341b7e` — merge with the landed root-v2 Strategy contract.
- `9a546301f` — clarify that `LifeRootProjectionV1` is the served read model.
- `11db134c1` — integrate the dark Life refinding route, truth oracles,
  occurrence reconciliation, and memory-custody hardening.
- `d53935bba` through `234f730ee` — admit typed Composition anatomy and serve
  authenticated owner-bound Artifact media without introducing a new owner.
- `fa768471e` — align the prior-trip summary tests with custody and restore the
  backend no-growth ratchets without bypassing them.
- `95e016031` and `b83d2393c` — canonize the four durable root orientations in
  the backend product spine while keeping the canon within its size budget.

The compiler is viewer-scoped, deterministic, bounded per lens, and emits
canonical `ResourceRef` handles. The route currently projects graph-backed
plans, occasions, commitments, and outcomes into the Time lens; empty data is
an honest `thin` projection.

### Frontend (`Travel App`)

- `3db6c9ee` — flagged native Life Time root and typed primitives.
- `6d8aa4b0` — pure allowlisted ResourceRef destination resolver.
- `013b3c75` — generated Life contract types.
- `92d1502d` — synchronized Life root contract types.
- `bd3730d2` — merge with the landed root-v2 Strategy surface work.
- `eb5288141` — integrate the flag-gated Life refinding lane into Universal
  Search with canonical destinations.
- `a05a25af2`, `227ef79f9`, and `0e50c94c8` — render typed Composition anatomy,
  preserve exact root return context, and show authenticated Artifact media.
- `9eb3d87d3` — keep the Lisbon group decision on its canonical shared Trip
  rather than leaking it into every Lisbon-shaped context.

The native root has loading, informational, failure/retry, and data states;
four lens labels; bounded Time rows; a canonical complete-record door; and
optional server-authored Return rendering. It contains no input prompt,
client-authored interpretation, arbitrary route push, or infinite-scroll
archive. `EXPO_PUBLIC_LIFE_ROOT_V1` is default-off and internal/dev-only.

The complete-record door now lands on a dedicated `/you/life-record` reader
(`dc4f1f66c`). The reader consumes `LifeRecordPageV1` through the generated API
contract, supports Time/Places cursor pagination, shows factual date/place/media
context, preserves canonical owner destinations, and keeps loading, partial,
failure, empty, and “read more” states explicit. The backend page is additive
and reads the existing owner-owned Atlas timeline (`fc361aeed`); it is not a
second Life archive. The follow-up merge (`5b0e1a644`, with coverage in
`b562eb3b4`) now combines Atlas rows, confirmed intake anchors, and retained
source-only submissions in one globally ordered cursor. The cursor carries both
the last consumed Atlas row and intake sort key, so buffered Atlas rows are not
skipped when intake records occupy the first page.

### Shared workspace

- `b52bbf9` — initial synchronized flag registry, operation policy, complete
  OpenAPI snapshot, and derived mobile projection.
- `6faa939` and the current contract follow-up — integrated the Life foundation
  with the artifact/root runtime and regenerated the complete and mobile
  contracts. The Life operation is explicitly registered and the derived
  projection contains the Life route and schemas.

## Validation evidence

- Consolidated backend artifact/root/Life/API focused suite: 78 tests passed.
- Backend semantic-facade and prior-trip custody suite: 34 tests passed.
- Frontend canonical Places projection parity: 13 tests passed.
- Frontend `tsc --noEmit`: passed.
- Life frontend reader suite: 9 targeted tests passed; complete-record reader
  mock, error, lens, and cursor-door behavior is covered.
- Deterministic workspace contract check: passed — 443 mobile paths, 488
  operations, and 1,299 schemas; generated TypeScript exactly matches the app
  projection.
- Cross-repository API audit: passed — 551 active, 13 dark, and 62 retiring
  operations; 0 unflagged.
- Backend formatting, import-boundary, timeout, mutable-state, applicable hooks,
  broad-exception ratchet, and size-budget ratchet passed. The convergence pass
  removed its two new broad handlers and one inherited handler, returning the
  audited count to the no-growth ceiling of 1,190.

## Deliberately deferred

1. Dossier-grade destinations for every Life object family, exact refinding
   continuation into those destinations, and scroll-position restoration. The
   current depth cursor is bounded by the existing 100-row intake owner reads;
   a later owner-level count/cursor can remove that ceiling without changing
   the public Life shape.
2. Full Places/People/Threads lens projection from production data.
3. Public rollout, analytics-driven promotion, and removal of legacy Atlas.
4. Together/multiplayer write paths and generalized Occasion architecture.
5. Visual composition polish beyond the production HTML design reference.

The next safe increment is to connect one returned refinding row to its exact
owner dossier and restore its Life context after inspection, then re-run the
same contract and conformance gates. Do not broaden either flag or add more
lenses until that destination-and-return seam is proven end to end.
