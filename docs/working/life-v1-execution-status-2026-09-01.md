---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-05
expires: 2026-10-01
why_new: Records the executed, cross-repository Life v1 foundation and its validation evidence so future design work can build on committed seams rather than re-open the architecture.
depends_on:
  - life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
  - life-v1-destination-and-refinding-contract-2026-09-01.md
  - ../contracts/life-v1-experience.md
  - ../systems/four-root-loop-object-surface.md
---

# Life v1 — execution status

## September 5 roadmap and evidence clarification

The [Life complete-system and Atlas replacement roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
owns the next engineering program. It replaces the prior foundation-only finish
line with Life as the sole continuity experience and explicit Atlas retirement.
Planning does not change deployed flags or complete the remaining packages.

The new static audit identifies remaining owner/destination mismatches, actual
tab exposure, full-history query cost, organization, custody, refinding and
cross-consumer repair work. The previous device flow uses mock data and checks
deep-link entry, two lenses and return to `you-screen`; that receiver is the
profile screen, not the Life root. It does not validate exact legacy-artifact
reads, real-backend data, deep scroll restoration or native design conformance.
The recorded test passes below remain valid within that narrower boundary.

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

## 2026-09-04 canonical-corpus correction

The depth reader is no longer an Atlas-plus-intake merge that the root reads
through a separate adapter. Backend commit `1b085b19d` introduces one internal
`LifeCorpusSnapshot` seam: Experience Graph, Atlas, and intake are normalized,
deduplicated by stable record identity, filtered by the requested lens, and
sorted by a single `(sort_at, record_id)` order. Both `GET /v1/life` and
`GET /v1/life/record` derive from that snapshot. The depth cursor is version 2
and carries lens, snapshot timestamp, sort boundary, and record identity, so a
later page cannot reshuffle records or cross lenses. Intake readers expose raw
continuation keys and the `read_all` wrapper drains past quarantined rows.

The root now reports `visible_entry_count` separately from the full
`total_entry_count`; a compact eight-row preview no longer claims that eight is
the whole corpus. A shared Occasion also no longer silently changes a private
Plan's audience. The workspace OpenAPI snapshots and generated mobile types
were regenerated in `cc2727b` / `b5d3cb4cc`, with the follow-up preserving the
existing booking-field contract in `4b4d64b58`.

On mobile, `b4e78795b` replaces the unbounded ScrollView reader with a
virtualized list that restores by `entry_id`, fetching pages until the anchor
is present and using a pixel fallback only when the row has disappeared.
Position keys are now per-account/per-lens, and the full Life page is removed
from the Home query persister. Artifact destinations carry the originating
Life lens, and `3110d43c2` makes the Life root's Search and Everything controls
real, accessible actions rather than inert icons.
Candidate and trip dossier headers now honor the same Life return context
(`11c46644c`, `975cceb03`) instead of routing back to Atlas/trips by default.
The cursor read also evaluates the graph at the carried snapshot clock and
includes corpus size in the root revision (`5fe91c312`, `2682fa7c9`).

## 2026-09-05 bounded intake serving correction

The canonical Life route no longer drains intake through the compatibility
`read_all` list wrappers. Backend commit `8512a4f25` reads the anchor and
retained-source page primitives directly, carries each `(updated_at, id)` keyset
continuation, detects a stalled continuation, and reports truncation when the
explicit corpus page cap is reached. Root and depth therefore receive the same
bounded source corpus and can distinguish a complete read from a partial one;
the existing list wrappers remain unchanged for their other callers.

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
and reads the canonical `LifeCorpusSnapshot` over the existing owner
projections (`1b085b19d`); it is not a second Life archive. The earlier
Atlas-plus-intake merge (`5b0e1a644`, with coverage in
`b562eb3b4`) now combines Atlas rows, confirmed intake anchors, and retained
source-only submissions in one globally ordered cursor. The cursor carries both
the last consumed Atlas row and intake sort key, so buffered Atlas rows are not
skipped when intake records occupy the first page. Cursor tampering/version
drift is rejected explicitly (`8e2d2bcb0`). Retained source rows now resolve to
an exact Life-owned owner route (`/you/intake-submissions/[submissionId]`)
rather than disappearing behind an unsafe API URL (`320223f33`, app
`29f21a745`). Record rows now resolve through canonical owner dossiers: kept
artifacts use `/you/memories/artifacts/...`, reviewable candidates use
`/you/memories/review/...`, and trip records use the canonical trip entry
(`28edd6654`). Subsequent intake reads now apply the cursor timestamp at the
owner query boundary (`5a4d9f938`) instead of repeatedly loading only the
newest head. The owner queries now also apply the `(updated_at, id)` tie-break
and can return exact counts when a bounded page is exhausted (`740e94dfd`).
The follow-up owner-read consolidation (`bff449427`) moves the shared intake
cursor boundary, lens filtering, deterministic merge preparation, counts, and
truncation authority into one internal `LifeIntakePage` service. The public
route remains an Atlas-plus-intake adapter; no new archive owner or public
endpoint was introduced. Database-backed intake page readers now fetch one
look-ahead row and return an explicit continuation bit (`1c22ce1fc`), so
partial authority is no longer inferred from an exact 100-row response. The
mobile reader carries its originating Life lens into dossier links and uses
history with a lens-aware fallback when leaving a retained-source record
(`ebbd4de7a`). The follow-up reader (`b4e78795b`) uses a virtualized list and
restores by stable entry identity, fetching until the anchor is available and
falling back to pixels only when the row is gone. Position storage is now
account- and lens-partitioned, the unbounded Life query is excluded from the
Home persister, and account teardown still clears all position keys.

### Shared workspace

- `b52bbf9` — initial synchronized flag registry, operation policy, complete
  OpenAPI snapshot, and derived mobile projection.
- `6faa939` and the current contract follow-up — integrated the Life foundation
  with the artifact/root runtime and regenerated the complete and mobile
  contracts. The Life operation is explicitly registered and the derived
  projection contains the Life route and schemas.

## Validation evidence

- Consolidated backend artifact/root/Life/API focused suite: 81 tests passed,
  including canonical corpus ordering, deduplication, Places filtering, and
  snapshot-stable cursor behavior.
- Backend semantic-facade and prior-trip custody suite: 34 tests passed.
- Frontend canonical Places projection parity: 13 tests passed.
- Frontend `tsc --noEmit`: passed.
- Life frontend reader suite: 9 targeted tests passed; complete-record reader
  mock, error, lens, and cursor-door behavior is covered.
- Backend Life serving and intake-page suite: 20 tests passed, including
  cross-kind cursor ties, Places filtering, exact-count escalation, and the
  unified owner-read seam.
- Latest Life/root route and corpus suite: 36 tests passed, including bounded
  intake draining, continuation advancement, truncation reporting, canonical
  corpus ordering, and cursor behavior.
- Canonical dossier and Life-return navigation checks: 21 backend Life tests,
  3 Life reader tests, and TypeScript compilation passed.
- Life position persistence and account-boundary checks: 29 focused frontend
  tests passed.
- Deterministic workspace contract check: passed — 443 mobile paths, 488
  operations, and 1,299 schemas; generated TypeScript exactly matches the app
  projection.
- Device certification harness added at
  `travel-app/.maestro/73-life-record-device-certification.yaml`. It covers
  deep-link entry, Time/Places reader switching, and the Life-owner return
  boundary. The local simulator run passed on iPhone 16 Pro (iOS 18.2),
  including both reader states and the explicit return control. Expo and
  Expo Dev Client package drift was aligned (`expo` 55.0.31,
  `expo-dev-client` 55.0.40), and CocoaPods was refreshed to match the
  installed RevenueCat packages. The first fresh build exposed a stale
  Release React prebuilt in the Debug Pods tree; switching the standard
  React Native prebuilt to its Debug artifact restored the native linker.
  The build then passed with `SENTRY_DISABLE_AUTO_UPLOAD=true` (the local
  Sentry upload has no org/project configuration). The certification report
  recorded 1/1 flow passed in 9 seconds. A second run after terminating the
  installed app (cold-launch rehearsal) also passed 1/1 in 8 seconds.
- Cross-repository API audit: passed — 551 active, 13 dark, and 62 retiring
  operations; 0 unflagged.
- Backend formatting, import-boundary, timeout, mutable-state, applicable hooks,
  broad-exception ratchet, and size-budget ratchet passed. The convergence pass
  removed its two new broad handlers and one inherited handler, returning the
  audited count to the no-growth ceiling of 1,190.

## Deliberately deferred

1. Dossier-grade destinations for every Life object family and deeper
   cold-launch coverage of identity-based scroll restoration. The canonical
   cursor, mobile restore implementation, and one simulator cold-launch/deep-
   link rehearsal are landed; new object-family destinations remain open.
2. Full Places/People/Threads lens projection from production data.
3. Public rollout, analytics-driven promotion, and removal of legacy Atlas.
4. Together/multiplayer write paths and generalized Occasion architecture.
5. Visual composition polish beyond the production HTML design reference.

The next implementation batch is R0/R1 in the replacement roadmap: make the
actual Life tab and owner destinations coherent, then replace full-drain reads
with the indexed canonical corpus query. Remaining dossiers, lenses, custody,
refinding, shared/prospective continuity, Returns and Atlas deletion are explicit
packages in that program, rather than indefinite deferrals.
