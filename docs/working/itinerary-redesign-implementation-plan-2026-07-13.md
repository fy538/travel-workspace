---
doc_type: working
status: active
owner: founder / product / backend / frontend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Convert the accepted itinerary redesign contracts and W0-W7 architecture into a governed, cross-repository, PR-sized implementation and rollout plan.
supersedes: []
source_of_truth_for: [itinerary-redesign-implementation-plan-2026-07]
---

# Itinerary Redesign — Cross-Repository Implementation Plan

## Decision and status

Proceed to implementation. The product paradigm, interaction model, authority
model, operation model, and target-state design are sufficiently settled. No
additional broad design exploration is required before engineering starts.

### 2026-07-13 Trip-shell convergence amendment

Subsequent founder review of the consolidated target design locks the following
clarifications without renumbering or restarting this program:

- the itinerary remains the default single-trip home before and during travel;
- the resting shell uses a light trip **Ledger** for identity, dates, people,
  and the Trip Details entrance, then withdraws to compact chrome on scroll;
- Trip Details is a **full-screen, scrollable push**, not a medium-sheet target;
- Trip Details is the comprehensive index, while an object already visible in
  the itinerary may open directly without using Details as a hallway;
- the domain model is one trip graph of typed linked objects: itinerary event,
  provider booking, expense, place, stay, and transport retain separate stable
  identities even when several entrances reach the same object;
- completed-trip entry is hybrid: immediately after completion, or while Memory
  is thin/not ready, fresh entry opens the completed itinerary record; a later
  fresh entry may default to Memory only when meaningful Memory is ready;
- cancelled trips always open the retained itinerary record and closure work.

These are convergence clarifications, not authority, operation, history, or
rollout changes. IR-10 continues on the existing dependency path. The affected
delivery contracts are IR-10, IR-12, IR-13, IR-14, and IR-16 below.

The governing UX, business, surface, and system documents were synchronized on
2026-07-13 to incorporate the full-screen Trip Details and hybrid
completed-record/Memory decisions. The former documentation gate is cleared;
implementation exposure remains governed by the IR-13 and IR-16 evidence gates.

This document is the execution bridge between the accepted target contracts and
implementation in `travel-agent` and `travel-app`. It does not promote the
Claude Design artifact to shipped canon and does not claim that target behavior
already exists.

The implementation must remain incremental, additive, feature-flagged, and
reversible. A new visual shell may not expose mutation, provider, authority, or
recovery behavior until the corresponding backend capability is real and tested.

## Governing sources and precedence

When this plan is ambiguous, use this order:

1. Product Thesis and What We Believe.
2. [`itinerary-interaction-business-logic-audit-2026-07-12.md`](itinerary-interaction-business-logic-audit-2026-07-12.md).
3. [`travel-app/docs/audits/itinerary-interaction-ux-audit-2026-07-12.md`](../../travel-app/docs/audits/itinerary-interaction-ux-audit-2026-07-12.md).
4. [`travel-app/docs/surfaces/trip-itinerary/contract.md`](../../travel-app/docs/surfaces/trip-itinerary/contract.md).
5. This implementation plan.
6. Older surface contracts and shipped implementation, as compatibility evidence
   only where they do not conflict with the sources above.

The target design reference is `Vesper Itinerary Redesign.html`. It is a
behavioral and visual target, not executable product truth.

If archived or compatibility-only material conflicts with the convergence
amendment's full-screen Trip Details, typed linked-object entrances,
Ledger/compact shell, or hybrid completed-trip entry, follow the active
governing contracts and treat the older material as shipped-state evidence only.
All other precedence remains unchanged.

## Non-negotiable product invariants

- Itinerary is the default single-trip workspace before and during travel.
- At rest, a light Ledger owns trip identity and the Trip Details entrance; on
  scroll it yields to safe-area-correct compact chrome without becoming a
  dashboard above the timeline.
- List and Map are two faces of one artifact and share day, stop, candidate,
  operation draft, and return context.
- Trip Details is a full-screen comprehensive index with a stable row order; it
  is neither a second home nor a mandatory hallway for visible itinerary facts.
- Row tap inspects; explicit Change begins mutation.
- Same-object multiple entrances preserve object identity and vary only the
  return stack. Event, provider booking, expense, place, stay, transport, and
  history remain typed linked objects rather than one overloaded object.
- Add, Move/Reorder, Replace, Remove, attendance, occurrence, Optimize, Replan,
  and parallel-plan changes are typed operations.
- One server-authored resolver returns `direct`, `confirm`, `propose`, or
  `denied`; clients never infer authority from role or participant arrays.
- Manual and Vesper entry points construct the same normalized operations.
- Vesper inherits the requesting human principal's authority and cannot gain a
  broader mutation capability through an agent tool.
- Plan truth, provider truth, proposal/decision state, and execution state remain
  distinct.
- Immediate receipts, stop history, operation detail, and trip-wide Changes are
  projections of one canonical operation record.
- Recovery is server-proven and state-based. The UI does not infer Undo from an
  operation type or a countdown.
- Personal attendance, planned participation, decision ownership, edit
  authority, provider control, and actual occurrence remain separate concepts.
- Open/Review governs whole-group human editing and does not erase personal or
  subgroup ownership.
- Parallel plans use an explicit split/branch/rejoin compound operation rather
  than incidental timestamp overlap.
- Legacy trips and old clients remain readable throughout migration.
- Completed trips open the factual record immediately after completion and
  whenever Memory is not meaningfully ready; later fresh entry may default to a
  ready Memory. Cancelled trips retain the record and closure truth.

## Verified current implementation boundary

The current product has useful substrate but not the target domain spine.

### Backend hotspots

- Current Plan State route and projection:
  - `travel-agent/backend/api/routes/plan_state.py`
  - `travel-agent/backend/core/db/plan_state.py`
  - `travel-agent/backend/core/models/plan_state.py`
- Current preview/commit paths:
  - `travel-agent/backend/api/routes/plan_edit_preview.py`
  - `travel-agent/backend/api/routes/plan_edit_commit.py`
  - `travel-agent/backend/core/plan_edit_intent.py`
  - `travel-agent/backend/core/db/plan_edit_idempotency.py`
- Current proposal paths:
  - `travel-agent/backend/api/routes/proposals.py`
  - `travel-agent/backend/core/db/change_proposals.py`
  - `travel-agent/backend/core/db/proposal_apply.py`
  - `travel-agent/backend/core/state_machines/proposal_state_machine.py`
- Current itinerary schema and persistence:
  - `travel-agent/backend/core/db/_tables/itinerary.py`
  - `travel-agent/backend/core/db/itinerary_persistence.py`
  - `travel-agent/backend/core/db/trips/itinerary.py`
- Current lifecycle derivations:
  - `travel-agent/backend/core/trip_phase.py`
  - `travel-agent/backend/core/db/plan_state.py`
  - Map-state builders and frontend helpers identified in the business audit.
- Current agent/direct-write bypasses:
  - `travel-agent/backend/concierge/itinerary_write_policy.py`
  - `travel-agent/backend/concierge/tool_handlers/itinerary.py`
  - `travel-agent/backend/concierge/tool_handlers/itinerary_edit.py`

### Frontend hotspots

- Routes:
  - `travel-app/app/(tabs)/trips/[tripId]/plan.tsx`
  - `travel-app/app/(tabs)/trips/[tripId]/map.tsx`
  - `travel-app/app/(tabs)/trips/[tripId]/changes.tsx`
- Shared itinerary state:
  - `travel-app/context/TripItineraryViewContext.tsx`
  - `travel-app/data/planState.ts`
  - `travel-app/data/itinerary.ts`
  - `travel-app/data/proposals.ts`
- Current editing grammar:
  - `travel-app/components/trip-plan/PlanBlockRow.tsx`
  - `travel-app/components/trip-plan/PlanDaySection.tsx`
  - `travel-app/components/trip-plan/ChangeStudioSheet.tsx`
- Current Map face:
  - `travel-app/components/trip-map/TripMapScreen.tsx`
  - `travel-app/components/trip-map/tripMapStateAdapter.ts`
- Existing receipt/proposal/change surfaces:
  - `travel-app/components/chat/ChangeAppliedCard.tsx`
  - `travel-app/components/trip/proposal-detail/*`
  - the trip Changes screen and its tests.

### Known implementation mismatches

- Lifecycle is derived in more than one place.
- Authority is partially inferred from role, editing mode, and participants.
- `participants = null`, block-wide `event_state`, and `locked` remain legacy
  compatibility concepts.
- Preview/commit covers only part of the mutation universe.
- Add, pin, direct routes, agent tools, proposals, Optimize, and Replan do not
  all converge on one gateway.
- Replace may persist only a changed title rather than a typed entity identity.
- Move does not consistently preserve day, time semantics, and relative order.
- History and receipts are assembled from several event/proposal paths.
- Recovery proof is path-specific; only limited direct Remove behavior has the
  complete atomic/fault-injection evidence required by the target contract.
- Provider-affecting replacement is not yet one explicit plan/provider saga.
- List and Map do not yet consume one complete canonical projection.

## Repository and worktree safety gate

At plan creation, both child repositories are on `main` with substantial
unrelated uncommitted work. Do not implement this program in either current
working tree.

Before the first code change:

1. Create isolated worktrees for both child repositories with the workspace
   worktree tooling.
2. Use the coordinated lane `itinerary-foundation`, initially creating the
   descriptive branch `codex/itinerary-foundation` in each child repository.
3. Confirm both new worktrees are clean.
4. Never stage with `git add .` or `git add -A`.
5. Keep backend and frontend commits in their respective repositories.
6. Use the workspace repository only for shared contracts, OpenAPI snapshots,
   cross-repo scripts, and this execution record.

No implementation PR begins until this gate is satisfied.

## Program dependency graph

```text
IR-00 baseline, fixtures, flags, and contract lock
  ├─ IR-01 canonical lifecycle
  └─ IR-02 additive schema foundations
       └─ IR-03 migration/backfill projections
            └─ IR-04 pure policy resolver
                 └─ IR-05 DB policy adapter + shadow capabilities
                      └─ IR-06 operation contract + preview gateway
                           └─ IR-07 transactional commit + minimal ledger
                                ├─ IR-08 proposal convergence
                                ├─ IR-09 recovery/history
                                ├─ IR-10 provider saga
                                └─ IR-11 compound operations
                                     └─ IR-12 coherent read models
                                          └─ IR-13 read-only frontend shell
                                               └─ IR-14 low-risk operations
                                                    └─ IR-15 collaboration/branches
                                                         └─ IR-16 Vesper/provider/replan
                                                              └─ IR-17 rollout and retirement
```

`IR-01` may proceed in parallel with additive portions of `IR-02`. Frontend
component construction may begin behind fixtures after `IR-06` freezes the API
shape, but no target mutation state may be enabled before its backend exit gate.

## PR-sized delivery ledger

Each row is intended to be independently reviewable and reversible. A slice may
be split further when its migration or test surface becomes too large; it may not
be merged with a later slice merely to make the UI appear complete sooner.

| ID | Repository | Outcome | Depends on | Default exposure |
|---|---|---|---|---|
| IR-00 | workspace + both repos | Baseline inventory, golden fixtures, flags, metrics, API contract lock | none | no behavior change |
| IR-01 | travel-agent | One canonical lifecycle projection and parity tests | IR-00 | shadow/read-only |
| IR-02 | travel-agent | Additive schema for lineage, revisions, operations, participation, ownership, protection, branches, and Trip Shape | IR-00 | no reads/writes flipped |
| IR-03 | travel-agent | Safe backfill and compatibility projections with telemetry | IR-02 | shadow/dual-read |
| IR-04 | travel-agent | Pure resolver with exhaustive matrix and invariants | IR-02 | tests only |
| IR-05 | travel-agent | DB-backed resolver adapter and server capabilities in shadow | IR-01, IR-03, IR-04 | shadow |
| IR-06 | travel-agent + workspace API snapshot | Canonical typed-operation models and preview endpoint | IR-05 | dogfood preview only |
| IR-07 | travel-agent | Transactional commit spine, idempotency, revision binding, and minimal operation ledger | IR-06 | disabled by default |
| IR-08 | travel-agent | Proposal creation/acceptance/withdrawal through the operation spine | IR-07 | shadow, then dogfood |
| IR-09 | travel-agent | History projections and proven Undo/Revert/Withdraw capabilities | IR-07, IR-08 | dogfood by operation type |
| IR-10 | travel-agent | Canonical provider-action saga, including Replace-and-rebook, held-to-confirmed proof, and partial-state continuation | IR-07, IR-09 | protected cohort only |
| IR-11 | travel-agent | Atomic Optimize/Replan and parallel split/branch/rejoin operations | IR-07, IR-09 | disabled until fault proof |
| IR-12 | travel-agent + workspace API snapshot | Versioned Plan State, Map parity, typed linked-object/attention projections, Details State, and history APIs | IR-03, IR-05, IR-07, IR-09 | dual-read |
| IR-13 | travel-app | Read-only Ledger/compact shell, full-screen Trip Details, typed entrances, List/Map continuity, Trip Shape | IR-12 | dogfood flag |
| IR-14 | travel-app | Inspect-first and low-risk solo Add/Move/Replace/Remove over gateway | IR-09, IR-12, IR-13 | dogfood operation flags |
| IR-15 | both | Review, attendance, subgroup ownership, and parallel branches | IR-08, IR-11, IR-12, IR-14 | selected group trips |
| IR-16 | both | Vesper parity, protected/provider continuation, replan, hybrid completed/Memory entry, lifecycle, and awareness | IR-10, IR-11, IR-12, IR-15 | selected cohort |
| IR-17 | both + workspace | Shadow completion, compatibility window, legacy retirement | all prior gates | staged rollout |

## Slice specifications

### IR-00 — Baseline, contract lock, and evidence harness

**Purpose:** make every later change measurable and prevent hidden write paths
from surviving the migration.

Deliverables:

- A checked mutation-path inventory covering app routes, agent tools, Discover
  Add/pin, Map, Chat, proposals, proactive producers, Optimize, and Replan.
- Golden data fixtures for:
  - undated solo;
  - dated solo with tentative and booked stops;
  - Open whole-group trip;
  - Review whole-group trip with waiting proposal;
  - personal and subgroup blocks with explicit owner;
  - parallel split/rejoin;
  - provider partial failure;
  - stale revision and dependent operation;
  - completed and cancelled trips;
  - member departure/deletion and private context.
- Feature flags declared but off.
- Metric names and expected labels defined before emission.
- Canonical request/response schemas recorded for lifecycle, capability, preview,
  commit, operation detail, and history.
- Test IDs that map the required manual/Vesper, lifecycle/governance, and history
  journeys to automated and device evidence.

Recommended code targets:

- Backend fixture builders under existing test fixture conventions.
- Frontend fixture additions under `constants/personas/planStateFixtures.ts` or
  dedicated itinerary target fixtures without replacing shipped mocks.
- Workspace contract snapshot and an implementation checklist in this document.

Exit gate:

- Every known mutation path has an owner and migration disposition.
- Every target state has a fixture or an explicit later-slice dependency.
- Both child worktrees are clean and isolated.
- No production behavior changes.

### IR-01 — Canonical lifecycle

Deliverables:

- Evolve `backend/core/trip_phase.py` into the single `TripLifecycle`
  projection, or replace it through a compatibility wrapper with one named owner.
- Return ideation, planning-early, planning-active, final-prep, live, and
  post-trip plus terminal completed/cancelled context.
- Include destination-local date, timezone and source, countdown/day number,
  dogfood override provenance, and optional disruption summary.
- Make Plan State and Map State consume the same projection in shadow first.
- Add parity logging for old/new derivations.

Tests:

- destination midnight and DST;
- missing timezone fallback;
- multi-city boundary fixture;
- dogfood override;
- raw status/date disagreement;
- completed/cancelled behavior.

Exit gate: one matrix supplies the same trip, timezone, and instant to every
consumer and receives the same lifecycle and day number.

### IR-02 — Additive schema foundations

Use additive Alembic migrations. Do not remove or repurpose legacy columns.

Recommended table/field groups:

1. Identity and concurrency:
   - `subject_lineage_id` on itinerary blocks;
   - itinerary day revisions;
   - immutable itinerary operations and operation transitions.
2. Scope and ownership:
   - explicit participation scope;
   - decision owner;
   - per-traveler participation/attendance/actual occurrence;
   - per-traveler Vesper delegation.
3. Structure and protection:
   - branch groups, branches, split/rejoin references;
   - normalized protected dependencies and provider state.
4. Lifecycle/history support:
   - Trip Shape;
   - private operation context;
   - viewer cursors, awareness, and typed write-back observations.

Migration requirements:

- deterministic constraints and indexes;
- immutable operation identity and idempotency key uniqueness;
- foreign-key/delete behavior reviewed for member/account deletion;
- no authority derived from mutable participant backfill;
- downgrade preserves legacy product operation, even if additive target data is
  abandoned.

Exit gate: schema migration and downgrade pass against representative production
fixtures; no read path changes and no existing itinerary bytes change.

### IR-03 — Backfill and compatibility projections

Deliverables:

- Backfill null/one/many participant cases according to the accepted contract.
- Map `locked` behavior to Review without deleting the legacy value.
- Backfill self-rooted lineage for every block.
- Preserve unknown provider changeability as unknown.
- Never infer branches from overlapping timestamps.
- Backfill operation history only where source and before/after identity are
  provable; retain ambiguous events as legacy read-only evidence.
- Emit counts for ambiguous owners, unknown protection, legacy occurrence, and
  history records that cannot be normalized.

Exit gate: legacy rendering and booking truth are unchanged; target projections
show explicit provenance and all ambiguous cases are measurable.

### IR-04 — Pure policy resolver

Recommended new backend ownership:

- a side-effect-free resolver module;
- typed resolver input/output models;
- generated matrix fixtures separate from DB adapters.

Resolver input includes actor, human principal, trip governance, lifecycle,
scope, owner, operation, affected people, protection, provider controller,
risk, privacy, delegation, and revision posture.

Resolver output includes outcome, reason code, decision owner, proposal policy,
confirmation reasons, protected dependencies, alternatives, predicted recovery,
and voluntary-proposal capability.

Exit gate: exhaustive matrix and invariant tests prove no attendee, agent, or
organizer can self-grant personal/subgroup authority and provider authority is
never inferred from itinerary authority.

### IR-05 — DB adapter, capabilities, and shadow mode

Deliverables:

- Load the pure resolver's facts through one DB-backed adapter.
- Fail closed on missing membership, principal, ownership, or provider-control
  evidence.
- Embed block/day capability projections in shadow Plan State.
- Compare new results with existing `resolve_edit_mode` and route-specific
  checks without changing behavior.
- Dashboard disagreement by operation, actor, scope, and reason code.

Exit gate: target fixtures resolve correctly and unexplained shadow disagreement
is below the agreed launch threshold before any write flag is enabled.

### IR-06 — Typed operation contract and preview

Add canonical endpoints:

```text
POST /api/trips/{trip_id}/itinerary/operations/preview
POST /api/trips/{trip_id}/itinerary/operations/commit
```

Preview normalizes:

- operation type and subject lineage;
- target entity provenance;
- placement/day/time/branch semantics;
- participation scope and owner;
- `plan_only` or `plan_and_provider` intent;
- ordered child operations for compound work;
- human principal and initiator/channel attribution;
- expected day revision;
- computed capability, consequences, and predicted recovery;
- a stable preview hash bound to the complete payload.

Recommended targets:

- new API route module rather than expanding legacy route files indefinitely;
- new core operation models/gateway package;
- OpenAPI generation through the workspace sync workflow.

Exit gate: equivalent fixtures from app, Map, Discover, Chat, and Vesper produce
the same normalized operation and preview hash.

### IR-07 — Transactional commit and minimal ledger

Deliverables:

- Commit revalidates principal, capability, revision, protection, provider
  facts, and the preview hash.
- Structural mutation and immutable operation evidence commit atomically.
- Idempotent retries return one operation and one visible result.
- Add, Move, Remove, attendance, and plan-only Replace gain typed handlers.
- Replace carries entity kind/id; Move carries day, anchors, time semantics, and
  branch; Remove never aliases attendance.
- Legacy endpoints become adapters to the gateway behind flags.

Exit gate: transaction fault injection proves no mutation without matching
operation evidence and no duplicate evidence on retry.

### IR-08 — Proposal convergence

Deliverables:

- Proposal creation persists the exact normalized operation and immutable
  creation-policy snapshot.
- Acceptance re-runs current authority, protection, provider, lifecycle, and
  revision checks.
- `accepted` and `applied` remain distinct.
- Stale intent rebases into a new attributed proposal rather than rewriting the
  old record.
- Withdraw wins only before resolution atomically starts.
- Existing proposal routes become operation adapters.

Exit gate: manual and Vesper proposals have identical operation, authority,
attribution, acceptance, stale, and withdrawal behavior.

### IR-09 — History and recovery

Deliverables:

- Canonical operation detail.
- Immediate, stop-lineage, and trip-history projections over one ledger.
- Live `OperationRecoveryCapability` computed from current authority, revision,
  dependency, provider state, and later operations.
- Atomic Undo where exact inverse evidence exists.
- Revert/new-change degradation when Undo is no longer truthful.
- Tombstone-to-successor navigation.
- Viewer-scoped privacy, seen cursors, and Needs-attention separation.

Hard rule: no UI or API advertises Undo for an operation until authority,
dependency, revision, idempotency, concurrency, and transaction fault tests pass
for that exact operation.

Exit gate: immediate receipt, stop history, trip history, and detail agree on
operation ID, delta, attribution, state, provider truth, and recovery.

### IR-10 — Provider saga

Deliverables:

- A general canonical provider-action saga whose first protected workflow is
  Replace-and-rebook and whose reference single-action proof is a held booking
  becoming confirmed.
- Stable provider-booking/dependency identity, linked itinerary subject or
  lineage, originating operation when applicable, controller, provider
  revision, and idempotency identity.
- Explicit Replace-and-rebook saga states.
- Separate plan and provider outcomes.
- Controller identity and confirmation boundaries.
- Durable partial state when cancellation/booking fails.
- Idempotent provider callback/retry handling.
- Typed provider continuation rather than generic Undo.
- One settled provider transition projects consistently into itinerary
  commitment metadata, contextual Needs attention, the Bookings index,
  provider detail, and canonical history without client-authored synchronization.
- Provider evidence changes expense/deposit/refund truth only when the provider
  supplies actual financial evidence; plan or booking transitions alone do not
  invent a charge.
- Attention clears from settled provider truth rather than a separate client or
  notification write, and a retried callback cannot duplicate history.

Exit gate: fault injection at every provider boundary yields either no committed
plan mutation or the exact durable partial state with a valid continuation. A
held-to-confirmed transition and every Replace-and-rebook terminal/partial state
produce one canonical provider record, one history transition, consistent
itinerary/Bookings/attention projections, and no inferred provider success.

### IR-11 — Compound operations

Deliverables:

- Atomic Optimize/Replan as ordered child operations.
- Explicit parallel split, branches, participant assignments, branch owners,
  organizer-owned topology, and rejoin in one compound operation.
- One preview, decision, operation identity, landed result, and recovery action.
- Governance/owner changes force re-resolution while preserving draft intent.

Exit gate: partial child application is impossible; recovery is one atomic
operation or degrades truthfully to Review revert/new change.

### IR-12 — Coherent read models

Deliverables:

- Versioned Plan State additions for lifecycle, revisions, explicit scope,
  ownership, participation, branches, protection, capabilities, pending work,
  and landed/recovery state.
- Map consumes the same day/block/branch projection.
- `details-state` owns the fixed identity, people, stay, transport, costs,
  bookings, Changes/History, and settings summaries used by full-screen Trip
  Details. Each row carries a typed destination, one factual calm/attention/
  absence status, viewer-safe visibility, and server-authored capabilities.
- Calm, Needs-attention, and Sparse Details variants are contract fixtures;
  organizer and member projections cannot leak actions or private/provider
  facts that the viewer cannot use.
- Plan/Details projections expose stable typed identities and edges for
  itinerary event, stay, transport leg, provider booking, expense, place, and
  operation/history records. They do not collapse linked subjects into one
  ambiguous canonical object.
- A contextual entry and a comprehensive Details/index entry resolve to the
  same object identity where applicable; event-to-booking or event-to-expense
  navigation is an explicit transition between linked objects.
- One Needs-attention projection feeds itinerary notices, Details row status,
  Bookings grouping, provider continuation, and Changes Needs attention.
- History endpoints support trip, subject lineage, stable compound cursors, and
  seen advancement.
- The read-model envelope can carry server-authored completed-record/Memory
  readiness and a recommended fresh-entry face without requiring a client-side
  post-trip algorithm; IR-16 owns enabling that recommendation.
- Folio compatibility adapter retains lifecycle, urgency, facets, source status,
  partial-data semantics, and Memory handoff until parity is proven.

Exit gate: List, Map, Trip Details, Chat attachment, and Changes agree after
every canonical operation and on member/deletion visibility. Both contextual
and comprehensive object routes resolve stable identities, and a provider
transition updates all attention/booking/history observers from one versioned
projection.

### IR-13 — Read-only frontend shell

Build the target shell without enabling unsupported writes:

- itinerary-first trip entry with a light resting Ledger, not a Folio or second
  dashboard;
- Ledger identity/dates/people and the Trip Details entrance at rest, then a
  safe-area-correct compact header on scroll;
- full-screen, vertically scrollable Trip Details using the fixed Details State
  order and returning to exact prior context;
- compact identity truncation and a deliberate 393pt priority among Back,
  identity/current day, Chat, the single face switch, and rare-action overflow;
- Chat and stable List/Map control;
- shared trip/day/selection/return context;
- inspect-first rows and Map peek, with generic events opening event inspection,
  unambiguous stay/flight anchors opening typed domain detail, and multi-linked
  events exposing explicit booking/expense/place destinations;
- direct contextual entrances that bypass Trip Details and comprehensive routes
  through Trip Details/domain indexes, both over the same typed identities;
- undated Trip Shape and first-draft read state;
- accessible semantic actions, Dynamic Type, device safe areas, real scrolling,
  and 393pt layout;
- server-authored lifecycle and capabilities only.

Recommended targets:

- evolve `TripItineraryViewContext.tsx` into the trip-scoped continuity owner;
- introduce target components beside, not inside, the current large Plan screen;
- keep current routes available behind the old flag;
- do not duplicate Plan/Map adapters in the new component tree.

Exit gate: read-only dogfood users can enter, switch List/Map, inspect, open
Details/Chat, and return to exact day/selection/scroll/camera state. On-device
golden paths prove (1) event -> linked expense -> event -> exact itinerary and
itinerary -> Ledger -> Details -> Costs -> the same expense -> exact itinerary;
and (2) stay anchor -> stay -> exact itinerary and itinerary -> Ledger ->
Details -> Stay index -> the same stay -> exact itinerary. Every target is a
keyboard/screen-reader-reachable action rather than a pointer-only wrapper.

### IR-14 — Low-risk operation UX

Implement inspect → Change → construct → preview → resolver ending → landed
state for low-risk solo/direct Add, Move/Reorder, Replace, and Remove.

- Search/select real entities for Add and Replace.
- Preserve current stop and itinerary context through Replace.
- Structured and gesture reorder create the same operation.
- Render server capability and server recovery without inference.
- Preserve drafts through detail, Map, Chat, stale refresh, and return tokens.
- Preserve the complete semantic return stack when Change begins after a
  contextual or comprehensive object entrance; a linked expense/provider action
  never aliases structural itinerary Change.

Exit gate: manual and Vesper low-risk paired journeys converge on identical
backend operations, receipts, history, and recovery.

### IR-15 — Collaboration and branches

Deliverables:

- Direct/Confirm/Propose/Denied endings over the same construction UI.
- Review Stack remains the ordinary decision inbox; Changes remains history.
- Personal attendance and occurrence operations.
- Personal/subgroup ownership and explicit decision owner.
- Parallel split/branch/rejoin presentation and editing.
- Organizer transfer and traveler departure behavior.
- People and Settings summaries remain viewer-scoped and do not expose an
  organizer/provider action that predictably fails for a member.

Exit gate: solo, Open, Review, personal, subgroup, and branch journeys pass with
two-account and privacy/deletion fixtures.

### IR-16 — Vesper, provider, replan, and lifecycle completion

Deliverables:

- Vesper recommends/prepares and opens the canonical operation rather than
  reproducing a second editor in chat.
- Protected booking/provider continuations.
- Contextual destination/date Replan.
- Disruption overlay, live Now/Next, offline reading, completed/cancelled entry,
  hybrid completed-record/Memory readiness, and factual corrections.
- Immediately after completion, and whenever Memory is thin, missing, or still
  processing, fresh entry opens the completed itinerary record with planned
  versus happened truth; structural editing is unavailable and authorized
  occurrence/attendance correction remains possible.
- A later fresh entry may default to Memory only when a meaningful Memory is
  ready. The final itinerary remains explicitly reachable and an explicit face
  choice persists for the session.
- Cancelled trips always open the retained itinerary record with refund,
  provider, and cost closure; they never fabricate happened state or Memory.
- Entry recommendation and Memory readiness are server-authored/backend-real,
  not inferred from device time, raw status, or the presence of media on one
  client.
- Proportional awareness keyed to operation ID.
- Typed, confidence-scored, correctable write-back observations.

Exit gate: paired Vesper/manual journeys, provider partials, lifecycle edges,
offline reconciliation, and write-back correction pass with backend-real data.
Completion-session, ready-Memory, thin/not-ready Memory, and cancelled-entry
fixtures each open the truthful face and preserve explicit navigation to the
other available record.

### IR-17 — Rollout and retirement

- Flag by dogfood cohort/trip and independently by read model and operation type.
- Shadow lifecycle and policy before read or write flips.
- Dual-read old/new projections; route writes through the gateway as early as
  safely possible and avoid permanent dual-write.
- Roll out read-only shell, low-risk solo, Open/Review, branches/attendance,
  Vesper, protected/provider, then replan/post-trip.
- Keep additive schema and compatibility adapters until evidence is clean.
- Retire `locked`, participant-derived authority, title-only Swap, raw-status
  lifecycle authority, direct mutation bypasses, and fragmented recent changes
  only after the compatibility window.

Rollback disables flags and restores compatibility reads. It never requires a
destructive schema rollback.

## Feature-flag matrix

Names may adapt to the existing flag framework, but separation is mandatory.

| Capability | Suggested flag | Initial state |
|---|---|---|
| Lifecycle projection read | `itinerary_lifecycle_v2` | shadow |
| Resolver/capabilities | `itinerary_policy_v2` | shadow |
| Operation preview | `itinerary_operations_preview_v2` | dogfood-only |
| Operation commit | `itinerary_operations_commit_v2` | off |
| History projection | `itinerary_history_v2` | dual-read |
| Details State | `trip_details_state_v2` | dogfood-only |
| Target shell | `itinerary_shell_v2` | dogfood-only |
| Individual operation types | `itinerary_op_<type>_v2` | off separately |
| Provider saga | `itinerary_provider_saga_v2` | protected cohort |
| Branch operations | `itinerary_branches_v2` | selected trips |
| Vesper gateway | `itinerary_vesper_gateway_v2` | off until parity |
| Hybrid completed-trip entry | `itinerary_completed_entry_v2` | off until IR-16 backend-real readiness proof |

Do not use one umbrella flag to enable an unproven stack of behaviors.

## API and OpenAPI workflow

Every route/model change follows the workspace contract:

1. Implement and test in `travel-agent`.
2. Run the workspace type-sync workflow.
3. Review `docs/openapi.json` explicitly.
4. Review `travel-app/utils/api/schema.gen.ts` explicitly.
5. Fix frontend type breakage before the slice is complete.

Do not hand-maintain duplicate TypeScript versions of generated backend models.

## Required evidence matrix

| Layer | Merge evidence |
|---|---|
| Lifecycle | Destination midnight, DST, fallback timezone, dogfood override, multi-city, completed/cancelled parity |
| Migration | Null/one/many participants, lineage, legacy occurrence, unknown booking, locked policy, overlaps, member deletion |
| Policy | Exhaustive actor × governance × scope × operation × lifecycle × protection matrix and invariants |
| Preview/commit | Cross-entry preview hash, revision binding, stale revalidation, idempotency, no mutation without evidence |
| Proposal | Immutable authored intent, acceptance re-resolution, stale rebase, Withdraw race, failed apply |
| Recovery | Exact inverse proof per advertised Undo, dependency invalidation, Revert degradation, provider partials, version pruning |
| Read models | List/Map/Details/Chat/receipt/history parity, typed object/link identity, contextual/comprehensive route parity, provider/attention projection, pagination, unseen vs attention, tombstones, privacy/deletion |
| Frontend | Manual/Vesper pairs, event/expense and Stay golden paths, lifecycle/governance journeys, safe-area 393pt compact shell, Dynamic Type, screen reader, Reduced Motion, offline, exact return state |
| Rollout | Shadow disagreement, capability-to-403, stale rate, saga failures, history duplication, List/Map mismatch, latency |

## Observability and launch gates

Instrument before enabling behavior:

- old/new lifecycle disagreement;
- old/new resolver disagreement by reason code;
- advertised capability followed by 403/409;
- preview-to-commit stale rate;
- idempotency collision or duplicate visible operation;
- mutation without history evidence;
- proposal accepted but not applied;
- provider saga partial/failure/retry state;
- Undo/Revert failure and degradation reason;
- List/Map/Details/history version disagreement;
- unseen/attention cursor anomalies;
- awareness duplication;
- Folio-to-target field parity and first-paint latency;
- contextual/comprehensive object identity or return-stack disagreement;
- provider transition versus itinerary/Bookings/attention/history disagreement;
- completed-entry recommendation versus Memory-readiness disagreement;
- write-back correction/supersession failures.

Numerical launch thresholds must be recorded in IR-00 after current baselines are
measured; do not invent thresholds without baseline data.

## Rollback principles

- Schema stays additive until retirement.
- Read flips are reversible independently of write routing.
- Operation types enable independently.
- A failed target write does not silently fall through to a legacy write after
  the user reviewed a target preview; preserve the draft and report failure.
- Provider partial state is durable evidence, not rolled back visually.
- Rollback preserves canonical operation/history records already committed.
- Old clients receive compatibility projections during the declared window.

## Explicit v1 deferrals

Unless the accepted contracts change, do not expand this program to include:

- co-organizer consensus or arbitrary voting as the default decision model;
- permanent traveler swimlanes;
- speculative branch inference from overlapping times;
- agent authority beyond the requesting principal;
- generic provider automation without explicit controller/confirmation;
- exact Undo where inverse evidence is unavailable;
- destructive replacement of old schemas before cohort evidence;
- a second chat-native itinerary editor.

## First implementation slice recommendation

Start with **IR-00**, then allow **IR-01** and additive **IR-02** to proceed in
parallel.

The first code PR should not be the visual shell. It should establish:

1. isolated clean worktrees;
2. mutation-path inventory and golden fixtures;
3. flag and telemetry scaffolding;
4. frozen lifecycle/capability/operation contract models;
5. no production behavior change.

The first behavior-bearing PR should be canonical lifecycle in shadow mode. It
has a narrow blast radius, proves the rollout mechanics, and removes a source of
cross-surface disagreement without prematurely exposing unimplemented recovery
or authority states.

## Program definition of done

The redesign is implemented only when:

- trip entry uses the itinerary-first shell for the enabled cohort;
- the resting Ledger, compact-on-scroll header, and full-screen Trip Details pass
  safe-area, 393pt, Dynamic Type, and exact-return evidence;
- List and Map share one canonical projection and editing context;
- contextual and comprehensive entrances preserve typed object identity and
  distinguish event, provider booking, expense, place, stay, and transport;
- every structural entry point uses one policy resolver and typed gateway;
- manual and Vesper paths converge;
- solo, Open, Review, personal, subgroup, and branch authority is server-authored;
- provider and plan truth remain independently inspectable;
- receipts, stop history, operation detail, and Changes agree;
- every visible recovery action is currently valid and fault-proven;
- undated, planning, live, completed, cancelled, and post-trip journeys pass;
- completed fresh entry follows backend-real record/Memory readiness rather than
  an unconditional Memory default;
- old clients remain compatible through the declared window;
- shadow/dual-read telemetry is clean;
- legacy mutation, policy, lifecycle, and recent-change paths are retired;
- the target design's meaningful contrast and accessibility requirements are
  implemented in production components and verified on device.

## Execution log

| Date | Slice | Status | Evidence / decision |
|---|---|---|---|
| 2026-07-13 | IR-00–17 independent adversarial review | implementation findings closed; rollout gates remain | Routed remaining occurrence and concierge writes through canonical authority; hardened current-policy proposal resolution, affected-member voting, cross-trip constraints, immutable evidence, privacy/deletion, stable history cursors, tombstones, and day-aware recovery; converged booking/expense invalidation, completed-entry availability, and canonical Map identity/order; completed frontend history, attention, typed-object, provider-continuation, rollout-guard, and generated-contract convergence. Backend commits `a216d5158` and `15da92baa`; frontend commits `bc58c7c0`, `bc77e8ab`, and `c54c6380`. Verification: 110 focused backend tests; broader review run 352 passed with one unrelated pre-existing expired-hold mock expectation; migration down/up; 9 frontend suites/56 tests; TypeScript, ESLint, Ruff, pre-commit integrity gates, and 360-path OpenAPI contract parity passed. No rollout stage advanced and no compatibility path retired. Evidence: `itinerary-redesign-adversarial-review-remediation-2026-07-13.md`. |
| 2026-07-13 | Trip-shell convergence amendment | complete | Preserved the IR-00–17 dependency graph and current IR-10 sequence. Locked the resting Ledger/compact shell, full-screen Trip Details, typed linked-object entrances, two exact-return golden paths, canonical provider-transition propagation, and hybrid completed-record/Memory entry. Updated IR-10, IR-12, IR-13, IR-14, IR-15, IR-16, flags, evidence, observability, and program definition of done. Governing UX/business/surface/system documents were synchronized and the documentation gate was cleared; implementation evidence gates remain. |
| 2026-07-13 | IR-17 rollout controls | implementation complete; exposure/retirement gated | Added fail-closed stage + trip/canonical-dogfood selection + independent capability resolution; per-operation server gates; trip-scoped dual reads and mobile compatibility fallback; compatibility-path telemetry across app/concierge legacy producers; and executable baseline/threshold/retirement/rollback evidence gates. No numerical threshold was invented and no compatibility path/schema/record was destructively retired. Focused backend tests: 197 passed; frontend rollout tests: 2 passed; TypeScript/Ruff/compile/diff checks passed. Production stage advance remains blocked on current-schema CI, measured IR-00 thresholds, selected-cohort evidence, and a rollback drill. Evidence: `itinerary-redesign-ir17-rollout-retirement-evidence-2026-07-13.md`. |
| 2026-07-13 | Planning | complete | Product paradigm approved; target design reviewed through 66-artboard artifact; implementation plan created. |
| 2026-07-13 | IR-00 | complete | Created clean coordinated worktrees at `travel-agent--itinerary-foundation` and `travel-app--itinerary-foundation`, both on `codex/itinerary-foundation`. Added the governed mutation inventory; strict lifecycle/capability/normalized-operation contracts; independently default-off flags; executable manual/Vesper parity and lifecycle fixtures; non-runtime target-state fixtures covering all required scenarios with explicit later-slice dependencies; stable telemetry events and privacy-safe labels without emission; semantic preview/commit/detail/history lock; and durable evidence ID families. Validation: 74 focused backend tests plus Ruff, 4 frontend Jest tests plus ESLint and full TypeScript passed. No routes, emitters, reads, writes, or shipped persona mocks changed. Next: IR-01 canonical lifecycle in shadow mode; IR-02 additive schema may proceed independently. |
| 2026-07-13 | IR-01 | in progress | Added one pure destination-calendar lifecycle projection with explicit timezone source, planning detail, final-prep boundary, current day, terminal completed/cancelled context, dogfood provenance, and compatibility mapping. Plan State and Map State call the same owner only when `ITINERARY_LIFECYCLE_V2` is enabled, emit typed old/new comparison telemetry, and continue returning unchanged legacy payloads. Added a read-only, aggregate-only lifecycle audit with checked classification and representative-coverage gates. At `2026-07-13T18:45:00Z`, 13 canonical dogfood trips had 100% Plan/Map legacy agreement and zero errors/unclassified differences, but covered only planning/post-trip, lacked cancelled, and had six destinations missing timezone. A broader mixed local corpus evaluated 1,847/1,847 with zero errors/unclassified differences; Plan agreed 92.96%, Map 66.70%, and all 745 disagreements were classified legacy status/calendar behavior. Read flip remains ineligible. Validation: 157 focused lifecycle/audit/Plan/Map/foundation tests and Ruff passed. Next: remediate dogfood lifecycle/timezone coverage, run real Plan/Map shadow reads, and re-audit; IR-02 may proceed without waiting. |
| 2026-07-13 | IR-02a | in progress | Added the first additive identity/concurrency migration: positive revisions on itinerary days and blocks, nullable block subject lineage for IR-03 backfill, immutable normalized operation roots, append-only sequenced transitions, inverse/parent links, preview hashes, and trip-scoped partial idempotency uniqueness. Added matching SQLAlchemy metadata and offline contract tests. Existing readers/writers do not reference the new substrate. Alembic single-head/contract tests passed; a full upgrade to `ir02a001` and downgrade to `7acaba807562` were verified in a disposable PostgreSQL database, which was removed afterward. Next: scope/ownership/participation, protected dependencies/provider state, explicit branch topology, and Trip Shape in separately reviewable additive migrations. |
| 2026-07-13 | IR-02b | in progress | Added nullable explicit participation scope, decision owner, and structural role to itinerary blocks while preserving the legacy `participants` array unchanged for IR-03 parity/backfill. Added normalized per-block/per-user state that separates planned inclusion, attendance intention, and actual occurrence. Account/block deletion behavior is explicit through foreign keys, and nullable ownership preserves ambiguity for measured remediation rather than inventing authority. Matching metadata and offline contracts pass. Verified `ir02a001 -> ir02b001 -> ir02a001` against a disposable PostgreSQL database; IR-02a substrate remained intact after the boundary downgrade and the temporary database was removed. Next: protected dependencies/provider truth, branch topology, and Trip Shape. |
| 2026-07-13 | IR-02c | in progress | Added normalized protected reservation/ticket/stay/transport/payment dependencies with provider state, changeability, controller, provider revision, source provenance, and positive revisions. Added append-only sequenced provider transitions linked to canonical operations. Existing `booking_ref`, booking offers, and accommodation rows remain untouched and authoritative until IR-03/IR-10. Verified `ir02b001 -> ir02c001 -> ir02b001` in a disposable PostgreSQL database; earlier substrate survived the boundary downgrade. |
| 2026-07-13 | IR-02d | in progress | Added explicit branch groups, topology owner, split/rejoin anchors, ordered branches, revisions, and nullable block-to-branch membership. No topology is inferred from overlapping timestamps. Verified `ir02c001 -> ir02d001 -> ir02c001` in a disposable PostgreSQL database. |
| 2026-07-13 | IR-02e | in progress | Added one versioned Trip Shape per trip plus ordered zero/many destinations, optional date windows, timezone override, public-only context, and materialized-itinerary linkage. The shape supports undated ideation and multi-destination planning without changing legacy trip fields. Corrected the materialize-operation contract to accept place/custom destination identity rather than venue identity. Verified `ir02d001 -> ir02e001 -> ir02d001` in a disposable PostgreSQL database. Remaining IR-02 foundations: viewer cursors/awareness, private operation context, typed write-back observations, and any accepted Vesper delegation substrate; then run representative-data migration/downgrade evidence before IR-03. |
| 2026-07-13 | IR-02f | complete | Added viewer unseen cursors separately from per-channel operation awareness; owner-scoped private-context source references and safe labels without duplicated raw private values; typed attendance/occurrence/plan/provider write-back observations with supersession; and per-user/per-operation Vesper delegation capped at suggest, prepare preview, or request confirmation—never direct commit authority. Verified `ir02e001 -> ir02f001 -> ir02e001` in a disposable PostgreSQL database. |
| 2026-07-13 | IR-02 | complete | The six additive migrations now cover lineage/revisions/immutable operations, scope/ownership/participation, protected/provider truth, explicit branch topology, Trip Shape, and viewer/privacy/write-back/delegation substrate. A disposable database at the pre-IR-02 head was seeded with null/one/many participants, planned/happened/skipped legacy occurrence, confirmed and unknown booking JSON, and existing itinerary content. Upgrade through `ir02f001` preserved every selected legacy byte, left provenance-sensitive target backfills explicitly empty, and initialized only positive revisions. Downgrade to `7acaba807562` again preserved every selected legacy byte and removed the additive substrate. No runtime reader or writer uses it. Validation: 179 focused foundation/lifecycle/Plan/Map/migration tests, Ruff, diff checks, and the Alembic single-head check passed; head is `ir02f001`. Next: IR-03 provenance-aware backfill and compatibility projections in shadow/dual-read mode. |
| 2026-07-13 | IR-03 | complete | Added typed, deterministic legacy projections and nullable provenance columns for self-rooted lineage, null/empty/one/many participation scope, membership-snapshot versus explicit planned inclusion, and legacy block occurrence. Participant evidence never grants decision ownership. Added a compatibility projection that maps legacy `locked` behavior to Review without rewriting the stored value. Booking JSON is normalized only for an explicit provider-state allowlist; changeability remains unknown, and unrecognized evidence stays measurable. The aggregate-only dry-run found 416 blocks, 758 projected participation rows, zero missing participant references, 416 ambiguous owners, 52 ambiguous booking objects, three overlap pairs that create no branches, and 661 history events retained as legacy evidence because none proves a one-to-one canonical operation with complete identity. A guarded apply command refuses remote databases. In a disposable PostgreSQL database, first apply wrote the expected 3 lineage, 3 scope, 5 participation, and 1 protected-dependency rows; second apply wrote zero; legacy bytes stayed identical; no branch or operation was invented; and `ir03a001 -> ir02f001` preserved legacy bytes. The temporary database was removed. Shared state and runtime reads remain unchanged. Next: IR-04 pure policy resolver. |
| 2026-07-13 | IR-04 | complete | Added a side-effect-free typed resolver with no DB, route, clock, flag, or telemetry dependencies. It consumes explicit principal/membership, governance, lifecycle, scope/owner/affected people, operation/risk, protection/provider controller, privacy, delegation, and revision facts, and returns the locked Direct/Confirm/Propose/Denied capability contract with stable reasons, owner/policy, confirmations, alternatives, protected dependencies, recovery prediction, and voluntary-proposal capability. It fails closed on missing or inconsistent facts; organizer status never overrides personal/subgroup ownership; Open whole-group authority comes from governance; Review routes to the named owner; attendance is self-only; post-trip allows factual correction only; system/provider initiators cannot borrow a principal; Vesper never receives Direct; and provider authority is independently explicit. Named `IR-GV-01..09` fixtures plus 216 generated combinations prove the core authority invariants. Validation: 157 focused tests, Ruff, single-head, and diff checks passed. No runtime reader/writer changed; Alembic head remains `ir03a001`. Next: IR-05 DB adapter, server capabilities, and shadow comparison. |
| 2026-07-13 | IR-05 | complete | Added the explicit V1 shared-itinerary decision owner with provenance, block-owner provenance, and subgroup `needs_owner_review`. Compatibility remediation uses the sole solo member; otherwise the creator when currently an organizer, or exactly one organizer; genuinely ambiguous cases stay null. Whole-group blocks use the shared owner, personal blocks use their sole participant, and subgroups use a temporary shared owner with review required. The fail-closed DB adapter now resolves block and day capability sets and runs under the default-off Plan shadow gate without changing payloads or writes. All 12 frontend target fixture IDs have executable backend policy evidence. A privacy-minimized copy of the live local corpus was migrated and backfilled in a disposable DB: 169 trips, 432 blocks, 788 participation rows, 29 subgroup review flags, zero unresolved block owners, and 789 member/block Move evaluations. There were 710 authority matches and 79 classified post-trip structural denials; unexplained disagreement was zero. The database was removed and shared state remained untouched. Validation: 171 focused tests, Ruff, diff check, and single-head passed; head is `ir05a001`. Next: IR-06 typed operation preview. |
| 2026-07-13 | IR-00–05 adversarial review | complete | Closed every review finding before IR-06. Trip-owner backfill now covers trips with zero blocks; new trips dual-write their owner; owner removal, demotion, and account deletion atomically transfer shared authority; adapters reject departed owners. Normalized operations now enforce operation-specific target/day/lineage/precondition, participant, topology, timezone, child-trip, Vesper-principal, and provider-intent invariants. Partial date windows cannot become indefinitely Live, and lifecycle fixtures enforce the accepted 4–14 day active-planning boundary. IR-02 now rejects cross-trip operation, dependency, provider-transition, branch, Trip Shape, cursor, and write-back links at the database boundary; Trip Shape destinations require exactly one identity; private-context dedup treats null source IDs as equal; metadata matches the migration. Account deletion anonymizes embedded operation/write-back/evidence UUIDs while retaining group-safe structural history. A disposable PostgreSQL database passed full upgrade, `ir05a001 -> 7acaba807562 -> ir05a001`, guarded backfill with four trip owners across only three block-bearing trips, adversarial constraint probes, membership transfer, and account-erasure evidence; it was removed after validation. Focused validation: 225 offline backend tests, 10 PostgreSQL ownership/account-deletion tests, Ruff, diff check, and one Alembic head. IR-06 may proceed. |
| 2026-07-13 | IR-06 | complete | Added the default-off, read-only canonical `POST /api/trips/{trip_id}/itinerary/operations/preview` gateway. The strict request carries one normalized typed operation plus retry correlation; the response binds the normalized operation, exact preconditions, current capability, consequences, predicted recovery, expiry/revalidation instruction, and stable semantic preview ID/hash. Hash semantics include the authenticated human principal and complete typed intent but exclude operation/request IDs and entry-channel attribution, so executable Plan, Map, Discover, Chat, and Vesper fixtures converge while retaining distinct evidence. The DB gateway loads lifecycle, membership/governance, explicit ownership/participation, delegation, protected/provider facts, and shape/trip/day/branch/block/proposal/provider/compound revision posture; referenced users, catalog entities, target days, anchors, branches, and compound children are trip-proven, provider refs are redacted, provider-changing intent requires provider revision evidence, missing facts fail closed, and stale facts return a denied capability without legacy fallback. Commit remains unregistered until IR-07. A disposable current/stale PostgreSQL proof wrote zero ledger rows. Validation: 136 focused offline tests, one PostgreSQL gateway test, Ruff, route-auth scan, fresh OpenAPI, generated frontend-type parity, and TypeScript passed. Full offline audit had 11,448 passes and 20 unrelated pre-existing failures. Next: IR-07 transactional commit and minimal ledger. |
