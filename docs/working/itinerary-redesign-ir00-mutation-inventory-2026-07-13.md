---
doc_type: working
status: active
owner: backend / frontend
created: 2026-07-13
last_verified: 2026-07-14
expires: 2026-08-12
why_new: IR-00 requires an explicit inventory and migration disposition for every itinerary mutation producer before the canonical gateway can replace path-specific policy and persistence.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir00-mutation-inventory]
---

# Itinerary Redesign IR-00 — Mutation-Path Inventory

## Purpose

This inventory is the control list for migration to the canonical itinerary
operation gateway. A path is not retired merely because the new UI stops calling
it. Each producer must either construct the same normalized operation, become a
read-only continuation, or be explicitly retired.

The target endpoints are:

```text
POST /api/trips/{trip_id}/itinerary/operations/preview
POST /api/trips/{trip_id}/itinerary/operations/commit
```

Until those endpoints and their ledger are real, all target write flags remain
off.

## Executable persistence boundary

The point-in-time route inventory below is now backed by two ratcheting static
manifests in `travel-agent/scripts/`:

- `check_itinerary_writer_boundary_baseline.tsv` classifies **112 stable direct
  writer sites / 132 current write occurrences**. The current occurrence split
  is 72 canonical writer/recovery, 28 legacy product mutation, 6 named integrity
  exceptions, 21 seed/scenario setup, and 5 one-off migration utility writes.
- `check_itinerary_legacy_consumer_boundary_baseline.tsv` gives **105 current
  legacy imports** an executable disposition: 68 replace, 22 delete, and 15
  rename. The rename rows are the current group-facing `change_proposals`
  projection consumers; they do not preserve proposal mutation authority.

Both checks use stable keys without line numbers. A classified occurrence or
import may disappear or decrease, but a new site or count increase fails CI.
The production scan covers `backend/`, `tools/`, and `scripts/`. Disposable test
fixture setup remains the sole directory-scoped direct-write exception; live
journey, dogfood, and scenario setup are included and must migrate to canonical
replay.

The source-level boundary proves ownership and regrowth prevention, not SQL
transactionality. The canonical fault-injection proof now verifies that
materialized block/day revisions, operation rows, transitions and their embedded
mutation evidence, the temporary `plan_events` mirror, and projected operation
history all roll back together. The six integrity writer keys are also a closed
code-level allowlist, so a TSV row cannot relabel a new product writer as
maintenance. The remaining Workstream 0 boundary work is (1) extending the
consumer manifest beyond backend module imports to legacy recent-changes and
compatibility-column readers, including frontend call sites, and (2) focused
reachability/semantic certification for the six integrity exceptions.

## Backend mutation inventory

| Producer / entry point | Current implementation | Current posture | Target disposition | Slice |
|---|---|---|---|---|
| Change Studio preview | `backend/api/routes/plan_edit_preview.py` | Move/Swap/Remove/Fill subset; route-local risk and commit mode | Compatibility adapter to normalized preview; remove route-local authority | IR-06 |
| Change Studio commit | `backend/api/routes/plan_edit_commit.py` | Direct mutation or proposal staging; partial stale/idempotency checks | Adapter to canonical commit; no independent mutation | IR-07/08 |
| Direct block update | `backend/api/routes/trips.py::update_itinerary_block` | PATCH writes structural fields through route-specific policy | Construct typed operation or factual/provider operation; retire raw structural PATCH | IR-07 |
| Mark booked | `backend/api/routes/trips.py::mark_itinerary_block_booked` | Route-specific provider/booking truth update | Provider/factual transition linked to canonical operation/dependency | IR-09/10 |
| Direct block-edit Undo | `backend/api/routes/trips.py::undo_itinerary_block_edit` | Path-specific inverse | Adapter to live `OperationRecoveryCapability`; remove action-type inference | IR-09 |
| Planning-revision Undo | `backend/api/routes/trips.py::undo_planning_revision` | Version-oriented recovery | Atomic Replan/Optimize recovery or Review revert | IR-09/11 |
| Direct Move | `backend/api/routes/trips.py::move_itinerary_block` | Separate day/time mutation; relative order is not canonical everywhere | Typed `move` with day, anchor, time semantics, branch, and day revision | IR-07 |
| Direct Add | `backend/api/routes/trips.py::add_itinerary_block` | Direct day write | Typed `add` with entity/custom truth, placement, scope, owner, and provenance | IR-07 |
| Experience pin | `backend/api/routes/trips.py::pin_experience_to_itinerary` | Independent Add-like write | Typed `add` with Discover provenance | IR-07 |
| Optimize day | `backend/api/routes/trips.py::optimize_day_route` | Suggestion/independent move behavior | Atomic `optimize_day` with ordered child operations and one recovery | IR-11 |
| Trip identity/date patch | `backend/api/routes/trips.py::patch_trip` | May change destination/dates outside itinerary operation semantics | Plain metadata only when no dated-plan consequence; otherwise contextual `replan` | IR-11 |
| Full planner generation | `backend/concierge/tool_handlers/planning/_plan.py` | Persists complete itinerary/version | First draft becomes `materialize_shape`; later output becomes atomic `replan` | IR-07/11 |
| Replan merge | `backend/planning_agent/replan_merge.py` | Produces diff/full-version substrate outside canonical resolver | Produce ordered Replan child operations; no direct persistence | IR-11 |
| Concierge update tool | `backend/concierge/tool_handlers/itinerary_edit.py::_execute_itinerary_block_update` | Agent-specific principal/policy checks and direct write | Typed operation under explicit human principal; fail closed | IR-07/16 |
| Concierge Move tool | `backend/concierge/tool_handlers/itinerary_edit.py::_execute_itinerary_block_move` | Agent-specific Move path | Same normalized `move` and preview hash as app | IR-07/16 |
| Concierge Add tool | `backend/concierge/tool_handlers/itinerary_edit.py::_execute_itinerary_block_add` | Agent-specific Add path | Same normalized `add` and capability as app/Discover | IR-07/16 |
| Concierge Undo tool | `backend/concierge/tool_handlers/itinerary_edit.py::_execute_itinerary_block_undo` | Path-specific recovery | Invoke live recovery capability by operation ID | IR-09/16 |
| Concierge experience pin | `backend/concierge/tool_handlers/itinerary.py::_execute_pin_experience` | Separate Add-like path | Same typed `add` with channel/provenance | IR-07/16 |
| Proposal creation | `backend/core/db/change_proposals.py::{create_change_proposal,build_and_persist_proposal}` | Multiple producers persist proposal-shaped intent | Persist exact normalized operation and immutable creation-policy snapshot | IR-08 |
| Proposal acceptance/apply | `backend/api/routes/proposals.py::resolve_proposal`; `backend/core/db/proposal_apply.py::apply_accepted_proposal` | Proposal-specific fork/apply engine | Re-resolve and commit the stored operation; accepted remains distinct from applied | IR-08 |
| Proposal Withdraw | `backend/api/routes/proposals.py::withdraw_proposal` | Proposal state transition | Atomic Withdraw capability until resolution begins | IR-08/09 |
| Proposal Revert | `backend/api/routes/proposals.py::revert_proposal`; `backend/core/db/proposal_apply.py::revert_accepted_proposal_v2` | Proposal-specific inverse/version restore | Canonical Revert operation or new-change degradation | IR-09 |
| Proposal automation | `backend/concierge/proposal_automation.py` | Applies accepted proposals through current proposal engine | Consume canonical proposal operation and gateway | IR-08/16 |
| Proactive proposal producer | `backend/concierge/proactive.py` | Creates proposal directly | Soft suggestion or organizer-ready normalized proposal; never direct mutation | IR-08/16 |
| Planning proposal producer | `backend/concierge/tool_handlers/planning/_propose_present.py` | Creates proposal from planning output | Persist exact typed operation and attribution | IR-08/16 |
| Booking/provider callbacks | booking routes, agents, and event subscribers | Provider truth may update separately from plan change identity | Link immutable provider transitions to dependency and originating operation | IR-10 |

## Frontend mutation inventory

| Surface / hook | Current implementation | Target disposition | Slice |
|---|---|---|---|
| Plan route | `app/(tabs)/trips/[tripId]/plan.tsx` | Target shell host; stop owning route-local authority and mutation endings | IR-13/14 |
| Change Studio | `components/trip-plan/ChangeStudioSheet.tsx` | Decompose into typed construction/preview; same UI for Direct/Confirm/Propose/Denied | IR-14/15 |
| Block-row edit/Undo | `components/trip-plan/PlanBlockRow.tsx` | Inspect-first; explicit Change; render server capability/recovery only | IR-13/14 |
| Edit commit hook | `hooks/useEditCommit.ts` | Call canonical preview/commit and consume operation result | IR-14 |
| Direct Move hook | `hooks/useMoveBlock.ts` | Gateway adapter; optimistic state must remain pending until canonical commit | IR-14 |
| Direct Add hook | `hooks/useAddBlock.ts` | Gateway adapter with placement/scope/owner/entity provenance | IR-14 |
| Venue-detail Add | `app/venue/[venueId]/index.tsx` via `useAddBlock` | Same typed Add as Plan/Discover with return token | IR-14 |
| Experience pin | `hooks/usePinExperience.ts` | Same typed Add; no independent authority | IR-14 |
| Proposal detail actions | `components/trip/proposal-detail/ProposalDetailScreen.tsx` and `data/proposals.ts` | Render stored operation and canonical decision/apply transitions | IR-15 |
| Changes inline Undo | `app/(tabs)/trips/[tripId]/changes.tsx` | Invoke live operation recovery; Changes no longer synthesizes capability from proposal type | IR-09/14 |
| Map | `components/trip-map/TripMapScreen.tsx` | Read/inspect face; any later edit launches the same operation draft/context | IR-13/14 |
| Chat/Vesper | trip and concierge chat routes/hooks | Open canonical operation for review; never maintain a second editor | IR-16 |

## Missing target producers

These are not current paths to adapt; they require first-class implementation:

- Trip Shape revision and `materialize_shape`.
- Explicit `reorder` independent of clock-time translation.
- Real entity Replace and Replace-and-rebook provider continuation.
- Per-traveler `set_attendance`.
- Block-level `mark_occurrence` distinct from attendance.
- `create_parallel_plan` and `update_parallel_plan`.
- Atomic `optimize_day` and contextual `replan`.
- Operation-linked provider reconciliation.
- Canonical history seen cursor, tombstone/successor, and live recovery capability.

## Migration rules

1. A legacy route may temporarily call the gateway, but it may not retain its
   own authority resolution or structural persistence after migration.
2. The same intent from Plan, Map, Discover, Chat, Vesper, or a proactive
   producer must normalize to the same payload and preview hash.
3. No fallback legacy write occurs after a target preview fails or becomes
   stale; preserve the draft and return a truthful error.
4. Provider reconciliation never rewrites plan truth unless linked to an
   authorized canonical operation.
5. Old-client compatibility is a projection/adapter concern, not permission to
   keep two mutation authorities indefinitely.

## Inventory completion gate

- [x] Current backend route-level mutation paths identified.
- [x] Agent, proposal, proactive, planner, and provider producers identified.
- [x] Current frontend mutation hooks and surfaces identified.
- [x] Missing target-only operation families identified.
- [x] Every path has a migration disposition and target slice.
- [x] IR-06 adds executable parity tests proving equivalent normalization.
- [x] Every production direct writer has a ratcheted classification.
- [x] Every backend legacy proposal/event/version module import has a ratcheted disposition.
- [ ] Legacy recent-changes and compatibility-column readers are ratcheted across both repos.
- [ ] IR-07 records removal dates for each independent legacy write.
