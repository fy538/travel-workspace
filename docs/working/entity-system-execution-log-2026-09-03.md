---
doc_type: working
status: active
owner: product / backend / frontend
created: 2026-09-03
expires: 2026-10-03
why_new: Records the commit-by-commit execution of the entity-system next program while preserving concurrent Home/Places work and the no-backfill boundary.
supersedes: []
---

# Entity system execution log — 2026-09-03

This log records the first implementation pass for
[`entity-system-next-program-2026-09-03.md`](entity-system-next-program-2026-09-03.md).
It is an execution record, not a release declaration. No catalog backfill was
run.

## Landed

Backend branch `codex/entity-shell-resolution`:

- `30ad05979` — additive entity-detail presentation v2, redirect alias sets,
  and a batch viewer relationship reader.
- `33ce29e15` — canonical entity refs on private outcome summaries and bounded
  private verdict projection.
- `c07582731` — no-store entity situation request/response and Plan/route
  composer with typed silence and freshness bounds.
- `e97ec2d6c` — snapshot-backed lived-experience provider consumes the same
  relationship projection.
- `9373f8665` — explicit accommodation Plan relationship reader.
- `3cfe3201e` — bounded situation characterization tests.
- `147aff72a` — expired route facts now produce typed silence instead of stale
  directions or an invalid response TTL.

Mobile branch `codex/entity-shell-resolution`:

- `e8475df47` — v2 relationship/capability-compatible object-page grammar and
  API client adapter.
- `ef6bd32d3` — expiring entity-situation API adapter and generated contract
  types.
- `78ccf1cab` — preserve the established site v1 route while migration stays
  opt-in; existing smoke tests remain green.

## Contract boundaries preserved

- The existing v1 presentation endpoint remains available.
- V2 does not call Google, routing, weather, or an LLM during the durable
  object read.
- Live situation is separate, authenticated, short-lived, and never echoes
  precise origin coordinates.
- `loved` affinity is not treated as `saved`; only an active save row yields
  the saved state in the canonical projector.
- Accommodation lived state is still absent; dates passing are not an
  occurrence authority.
- No source, Plan block, outcome, or entity catalog rows were backfilled.

## Verification

- Backend focused relationship/presentation/situation tests: passing (67
  tests).
- Backend touched-file lint/format checks: passing.
- Mobile TypeScript check: passing.
- Mobile site data and smoke tests: passing.
- OpenAPI projection check against the entity branches: passing (`438` paths,
  `483` operations, `1288` schemas).
- The full backend offline suite was started but interrupted during its long
  async teardown after pre-existing unrelated failures; it is not a release
  gate result.

## Next gated work

The next safe slice is to add a v2 consumer behind an explicit mobile rollout
flag, then migrate venue relationship/capability regions with physical Places
QA. Workspace OpenAPI snapshots are intentionally not overwritten in this
pass because they contain concurrent Home/Places Source changes; they should
be regenerated and reviewed when these two branches are integrated.

## Review fixes — 2026-09-03

All ten findings from the implementation review are addressed in the entity
worktrees, on `codex/entity-shell-resolution`. No backfill, migration, provider
refresh, or production data mutation was run.

Backend commits:

- `a126841bf` — live origin routing bypasses shared cache reads/writes; provider
  error logs omit origin-bearing URLs; route prose uses the resolved mode;
  zero-distance arrival yields a valid summary without a positive-duration route.
- `473aabc8f` — bounded transitive alias reads retain historical identities,
  respect owner visibility/global precedence, and reject cycles/excessive depth.
- `c59eaff64` — personal Plan requires planned participation, explicit trip
  filtering happens before Plan selection (including stays), entity outcomes
  are selected per requested identity rather than from the global latest twenty,
  and relationship revisions fingerprint material content rather than aliases
  alone. Snapshot consumers forward their trip scope.

Mobile commits:

- `7330407cf` — mounted pages withhold expired situation values, including on
  app foregrounding and failed refetch; save/outcome/occurrence mutations
  invalidate the relevant v1, v2, and situation consumers.
- `8682310a9` — invalidation matches numeric hook IDs with string mutation IDs
  while preserving viewer/entity isolation.

Verification:

- Combined backend relationship, alias, presentation, situation, outcome, and
  distance tests: **149 passed, 1 PostgreSQL-only test deselected**.
- New query regression tests execute SQL against isolated in-memory tables;
  they are not a substitute for PostgreSQL integration verification.
- Six mobile suites (expiry, invalidation, outcome mutations, saves, site data,
  site detail smoke): **50 passed**. `tsc --noEmit`: passed.
- Touched-file Ruff checks/formatting, Prettier, and both repositories' commit
  hooks: passed.
- These fixes change no public request/response schema; no generated contract
  edits were needed. The integration/rollout gates above remain unchanged.

## Object-page execution slice — 2026-09-04

The first implementation slice from the Entity Object Handoff Lab is landed
on local `main` in the child repositories:

- Travel App `0ecf0e9f0` — internal-only `ObjectPageRebuild`, deterministic
  fact ranker/body projection, photo-or-nothing provenance plate, square
  `ObjectPageShell`, and venue/site migration seams.
- Travel App `f7a348f4a` — experience migration seam; booking and Plan remain
  the fallback when the flag is off.
- Travel Agent `1fd47c9b4` — `EntityResearchBrief` model and a read-only
  `/api/entities/{type}/{id}/research` projection over existing completed
  brief rows. A missing row is 404; this route never queues, calls a provider,
  invokes a model, or writes data.
- Travel App `c83d2fd9d` + workspace `947a080` — client hook, mock/http
  adapter, and synchronized OpenAPI snapshots/types.

`EXPO_PUBLIC_OBJECT_PAGE_REBUILD_ENABLED` is internal-build-only and defaults
off. The research request/refresh job, inline citations/source UI,
viewer-relative people lines, addressed-handoff UI, generalized photo
endpoint, identity seeding/dedupe, and Occasion-live signal remain gated open
questions. No catalog backfill or refresh was run.

Verification for this slice: mobile `tsc --noEmit` and object projection tests
pass; backend entity-research/model and entity identity suites pass. The
existing situation endpoint test could not import the repository's full API
because the local environment lacks the pre-existing `openai` dependency; no
failure was caused by the new route.

## Object-page follow-on execution — 2026-09-04

The guarded rebuild now has three additional, additive slices:

- Travel Agent `67e4f6556` — explicit `paragraph_sources` provenance on the
  read-only research brief; invalid or unresolvable source numbers fail closed.
- Travel App `748786ae5` — paragraph markers render only from that explicit
  mapping; generated API types and mock parity are retained.
- Travel App `2377099e9` — large-text metadata stacks pair and closing facts at
  the 1.3 font-scale threshold; instrument labels remain clamped.
- Travel App `a6e907766` — optional request-scoped situation summary slot; no
  request is made without an explicit validated situation request.
- Travel App `47e63347a` — Ask Vesper handoff wired through the existing
  canonical ConversationSeed owner for site and experience pages.
- Travel App `a95d1591d` — bounded viewer relationship copy is shared between
  the legacy page and the rebuild, so planned/lived/saved/affinity labels do
  not fork across object surfaces.
- Workspace `fixture-contract-audit-2026-09-04.md` — records why the design
  fixture pack remains reference-only and which future fields are gated.

Verification: mobile typecheck, object projection tests, and touched-file
Prettier checks pass; backend entity-research tests and commit hooks pass.
No catalog backfill, research refresh, provider lookup, or fixture migration
was run. Full native visual evidence for the new renderer remains open because
the captured Places run used the default-off feature flag and pre-follow-on
commit SHA.

## Contract and smoke follow-on — 2026-09-04

The follow-on gates and boundary regressions are now characterized on local
`main`:

- Travel Agent `f203814b7` — route tests assert that public research briefs
  use a short shared cache while owner-provisional reads remain private and
  `no-store`.
- Travel App `91f077670` — site and venue smoke mocks explicitly model an
  absent v2 presentation read, preserving the sparse 404 path instead of
  relying on an accidental mock shape.
- Travel App `f5243fa82` — the hand-typed research-brief alias is registered
  in the schema-bridge manifest; no API surface was expanded by the manifest
  entry.

Verification after these commits: backend entity route/research tests (25)
and the focused entity research/field/identity suite (42) pass; mobile
typecheck, object projection tests (8), and site/venue smoke tests (37) pass;
the static Places QA gates pass; and `make contract-check` passes (574
complete-snapshot paths, 439 active-mobile paths, generated types current,
canonical place identity seams green, and 363 facade exports covered by the
schema bridge). No catalog backfill, research refresh, provider lookup, or
fixture migration was run. Native visual evidence for the guarded renderer
remains an explicit follow-up because the earlier capture used the default-off
flag and the current installed internal binary may need a rebuild.

## Explicit research and people-line slices — 2026-09-04

The next safe object-page boundaries are now landed on local `main`:

- Travel Agent `180991b63` — gated `POST /api/me/entities/{type}/{id}/research-requests`
  with a small idempotent request body, cache-safe response, verified catalog
  eligibility, and reuse of the existing `research_queue`. It never runs on
  a GET, never promotes owner-provisional shells, and leaves experience
  queueing unsupported until that authority exists.
- Travel App `27fa415bf` — generated request adapter, network-gated mutation,
  stable idempotency key, and an internal-only `Read up` verb on sparse venue,
  site, and accommodation object pages. Mock mode remains side-effect free.
- Travel App `4c741bb63` — schema-bridge classifications for the new request
  aliases and the previously landed people-lines response alias.
- Workspace `60f25a9` — complete and active OpenAPI snapshots for the request
  endpoint and response models.
- Travel Agent `4d9fbb834` — queue metadata carries only `source_surface` and
  the public city label needed by the existing worker query builder; no actor
  identity or private page context is persisted.
- Travel Agent `9a5a8fe8c` and workspace `33c1904` — content-free,
  read-only entity health report plus `make entity-health` entry point for
  pending reviews, duplicate provider candidates, active redirects, stale
  claims, provisional venue/site shells, and research queue state.

Verification: backend request/entity suites **32 passed**; mobile typecheck
and focused entity hook tests pass; `make contract-check` passes with **576**
complete-snapshot paths, **441** active-mobile paths, **1295** generated
schemas, and **366** facade exports covered. No catalog backfill, provider
refresh, or research worker run was performed. The queue worker remains the
existing explicit operational owner; native visual evidence and addressed
handoff UI are still gated follow-ups.

## Addressed-handoff object seam — 2026-09-04

The rebuilt object page now has an internal-only sender doorway for the
existing relationship-owned handoff flow:

- Travel App `7a29dc9dd` — added
  `RELATIONSHIP_UUID_HANDOFFS_ENABLED` and renders the existing explicit-pair
  chooser/composer on rebuilt object pages. It remains dark unless both the
  internal build and the opt-in flag are present; the legacy venue surface is
  unchanged.

The doorway reuses the canonical `RelationshipPlaceNoteAction` owner, so pair
membership, recipient resolution, consent, idempotency, and delivery remain
outside the entity page. Mobile typecheck and the relationship summary/action
tests pass. No handoff was sent and no production data changed.

## Relationship readback slice — 2026-09-04

- Travel App `470b8af10` — the rebuilt object page now renders the bounded v2
  relationship readback when present: visit count, last-visited date, active
  Plan title, and the viewer's private verdict. The projection is explicit and
  does not render private prose or companion details.

The pure projection test and relationship/action tests pass, along with mobile
typecheck. No backend contract or data source changed.

## Research-request failure replay — 2026-09-04

- Travel Agent `0b3c48a46` — idempotent replay of a permanently failed queue
  item now returns `already_failed` instead of the misleading `already_fresh`.
- Travel App `7af2a95dd` + workspace `56b0d05` — regenerated the OpenAPI
  snapshots and mobile schema for the additive status.

The focused request suite passes (**5 tests**), `make contract-check` passes,
and no queue item was retried or mutated.

## Mounted identity transition repair — 2026-09-04

- Travel App `ce19d1f3c`, `e264c09f1` — scoped
  `useEntityResearchRequest` mutation receipts to the current account/entity
  identity. A mounted route transition now hides the prior queued/failed
  receipt, resets the mutation, and rotates the idempotency key before the
  next deliberate request; late responses and duplicate requests cannot
  repopulate or overwrite the active page.

Verification: the lifecycle regressions and shared object renderer suite pass
(**7 tests** total); app-main TypeScript passes. The worktree-only lint
and typecheck were not used because the isolated worktree has no Expo
dependency resolution; no account, queue, research, or catalog data changed.

## Keep/Unsave identity transition repair — 2026-09-04

- Travel App `b5c0a4fbf`, `49465bab2`, `712fdab69` — threaded the originating account/entity identity
  through Keep/Unsave mutation variables and optimistic callbacks. Mounted
  transitions now scope pending/error state and in-flight locks to the active
  object; late completions update only their originating cache and cannot emit
  a receipt, push, or callback for the new object.

Verification: `useSaveEntity` plus the research lifecycle and shared renderer
tests pass (**37 tests** in the focused mutation/renderer group); app-main
TypeScript and test contract typecheck pass. No runtime API contract or
catalog data changed; the save behavior was exercised only through test
mocks.

## Addressed place-note lifetime guard — 2026-09-04

- Travel App `85eba258f`, `0bdbe25bc` — bound the addressed place-note doorway to the
  mounted entity/account/path lifetime. A delayed chooser or open editor now
  cannot submit a stale canonical ref or show success after the viewer has
  moved to another object, account, or route.

Verification: the addressed-handoff component, shared renderer, save mutation,
and research lifecycle tests pass (**43 tests**); app-main TypeScript,
test-contract typecheck, and accessibility governance pass. Backend ownership
and revocation remain the authoritative server checks; no handoff was sent and
no production data changed.

## Returned identity-generation repair — 2026-09-04

- Travel App `76a4df8af` — added a monotonic mounted identity generation to
  Keep/Unsave mutation variables and in-flight locks. A late response from an
  earlier account/entity lifetime is now stale even when the user has returned
  to the same account and entity (A→B→A), so it cannot resurrect pending/error
  state or emit a receipt, push, or active-page callback.

Verification: `useSaveEntity`, research lifecycle, shared renderer, and
addressed-handoff tests pass (**44 tests**); app-main TypeScript, test-contract
typecheck, mutation-key ownership, API-boundary, schema-bridge, and
accessibility governance checks pass. No API contract or production data
changed.

## Plan-preview lifetime repair — 2026-09-05

- Travel App `f38347b78` — canonical venue and experience plan previews now
  capture the mounted entity/account/path lifetime. Late preview responses and
  stale errors are ignored after a route, selected-trip, bounded-opening, or
  account transition; an existing review preview is cleared on replacement,
  and the signed Places handoff latch resets for a new opening.

Verification: venue and experience smoke suites pass (**38 tests** together),
including deferred route-replacement regressions; app-main TypeScript and
touched-file lint remain clean apart from the repository's existing warnings.
No API contract, itinerary row, research job, or catalog data changed.

Final deterministic receipt for this lane: the six-suite mobile selection
(projection, rebuilt renderer, research lifecycle, Keep/Unsave, venue detail,
and experience detail) passes **96 tests**; the focused backend
presentation/research/relationship selection passes **46 tests**; `make
contract-check`, mobile TypeScript, test-contract TypeScript, API-boundary,
schema-bridge, and accessibility-governance checks pass. The read-only health
report at `2026-09-05T02:50:05Z` is unchanged: zero stale claims, duplicate
active jobs, expired leases, retried rows, or completed-without-fresh-brief
mismatches, with one pending venue research row and one pending resolution
review left untouched. Native auth-diversity, mutation/readback, repair,
VoiceOver, Android/platform, owner-reviewed pilot, and operational disposition
remain release gates; no flag, scheduler, provider call, or backfill was run.

## Shared delayed-action lifetime repair — 2026-09-05

- Travel App `65909bb18` — extended mounted-lifetime protection to the shared
  object-page research poller, the itinerary review sheet's commit/propose
  outcomes, and venue/experience trip-picker transition timers. A route,
  account, object, or situation replacement can no longer publish delayed
  state into the replacement page; durable itinerary writes are still allowed
  to finish server-side and are not replayed.

Verification: the shared renderer/review selection passes **8 tests**, including
the deferred research-poll and review-commit replacement regressions; the
venue/experience smoke selection remains green at **39 tests**, including the
bounded-opening latch reset regression. No API
contract, itinerary row, research job, or catalog data changed.

## Entity state-matrix harness — 2026-09-05

- Travel App `e4d2a3436` — direct entity envelope/presentation reads and
  experience detail now honor the existing mock-only force-state harness for
  loading/error exercise. Research brief/status reads accept named mock faults
  so a loaded object can be held in an honest status-unknown state without a
  paid request. The global offline notice now reserves the root safe-area
  inset, preventing status-bar overlap in the native banner.
- Travel App `.maestro/54g-journey-07-entity-state-matrix.yaml` — added a
  compatibility-route native slice for loading geometry, retryable read error,
  malformed-link unavailable state, and the offline save gate. It intentionally
  leaves the rebuilt-page flag off; direct site/experience forced-read
  behavior is covered by the focused hook tests until an internal flag-on build
  is installed.

Verification: the focused entity/state selection passes **100 tests** on
`travel-app:e4d2a3436`; TypeScript, test-contract TypeScript, API-boundary,
schema-bridge, and accessibility-governance checks pass. The iPhone 16 Pro
mock flow passes all **12 steps** with four captures. This is partial native
state-matrix evidence; real-backend auth diversity, research, write/readback,
repair, VoiceOver, Android, and the full flag-on matrix remain open. No API
contract, research job, provider call, itinerary row, or catalog data changed.
