---
doc_type: working
status: active
owner: backend / frontend
created: 2026-07-13
last_verified: 2026-07-16
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

Those endpoints and the canonical ledger are now the unconditional product
authority. The historical route tables below remain the IR-00 audit baseline;
the closeout ledger in this document governs their current disposition.

## Executable persistence boundary

The point-in-time route inventory below is now backed by four ratcheting static
manifests across the two repositories:

- `check_itinerary_writer_boundary_baseline.tsv` classifies **121 stable direct
  writer sites / 141 current write occurrences**: 97 canonical writers, 11
  named integrity exceptions, 27 seed/scenario cleanup writes, 5 migration
  utility writes, and **1 finite legacy-product acknowledgement writer**.
- `check_itinerary_legacy_consumer_boundary_baseline.tsv` classifies **19
  retained imports**: 8 replace, 7 delete, and 4 rename. These are physical
  lifecycle/projection dependencies, not unclassified product readers.
- The backend and frontend semantic compatibility-reader baselines are both
  **zero**. Folio, legacy recent-change/raw-status behavior, locked governance,
  planner `persisted_version`, and mobile compatibility fallbacks have no
  approved production consumers.

All four checks use stable keys without line numbers. A classified occurrence or
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
maintenance. Their five callable entry points are restricted to the named
account-deletion, trip-archival, member-removal, planner-warning, and internal
owner-reassignment importers; a normal itinerary route importing one fails CI.
The current full structural gate and canonical itinerary certificate cover that
reachability plus authorization and lifecycle behavior (**319 + 280 passed** on
2026-07-16). Workstream 0's inventory/regrowth boundary is complete; physical
retirement still follows the evidence gates below.

## Retained compatibility disposition ledger (2026-07-16)

| Structure | Current purpose and consumers | Owner | Disposition / next review |
|---|---|---|---|
| `change_proposals` physical table | Temporary group-facing decision projection used by proposal reads/votes/deadlines and maintained atomically by the canonical proposal gateway; account deletion, archival, member departure, and deterministic seed cleanup preserve lifecycle integrity. It owns no itinerary mutation authority. | `itinerary_decision_projection` + canonical proposal gateway | Rename or replace only after deployed decision consumers and lifecycle cleanup are certified. Review **2026-07-23**; physical removal remains gated by B2/B3/D4. |
| `plan_events` physical table | Frozen historical ledger retained only for privacy/archive lifecycle, invariant checks, and deterministic fixture cleanup. No product writer or reader exists. | data lifecycle / archive | Drop after deployed artifact/caller absence and retention sign-off. Review **2026-07-23**; gated by B2/B3/D1. |
| `itinerary_edit_log` | Finite historical preference-drain input. Preference inference may read unprocessed rows and the sole legacy-product writer may only acknowledge them as processed; it cannot alter itinerary truth. | Preference Engine | Remove reader, acknowledgement writer, table, and writer allowlist row after deployed backlog is zero for the signed observation window. Review **2026-07-23**; this is the only remaining product-writer closeout. |
| `legacy_itinerary_version` exports | Version-shaped materialized reads still used by planner/proposal/story consumers while canonical authority owns writes and history semantics. They are not compatibility behavior readers. | Trips read authority | Replace with explicitly named plan/history projections, then rename/delete the module. Review **2026-07-23**; no new consumers allowed. |
| `backfill_itinerary_redesign.py` | One-off migration utility for already-deployed rows; never reachable from product routes. | itinerary migration owner | Delete after Fly backup, migration verification, and reset/reseed evidence are signed. Review **2026-07-23**; gated by C-deployed. |

All independently reachable legacy mutation routes, planner persistence
fallbacks, proposal mutation engines, Folio assembly, and app compatibility
readers were removed locally by **2026-07-16**. The rows above are the complete
retained set relevant to B4; their dates are review dates, not fabricated
deletion licenses.

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
| Proposal creation | `backend/core/itinerary_proposal_producer.py`; `backend/core/itinerary_proposal_gateway.py` | **Canonical:** exact normalized operation and immutable policy snapshot; `change_proposals` is a read projection only | Keep canonical; delete unreachable legacy constructors in B3 lane 3 | IR-08 |
| Proposal acceptance/apply | `backend/api/routes/proposals.py::resolve_proposal`; `backend/core/itinerary_proposal_gateway.py` | **Canonical:** accepted is durable before the stored operation is re-resolved and committed | Keep canonical; delete unreachable legacy route/apply body in B3 lane 3 | IR-08 |
| Proposal Withdraw | `backend/api/routes/proposals.py::withdraw_proposal` | **Canonical:** atomic withdrawal only before resolution begins | Keep canonical | IR-08/09 |
| Proposal Revert | `backend/api/routes/proposals.py::revert_proposal`; `backend/core/itinerary_proposal_gateway.py::revert_applied_itinerary_operation_proposal` | **Canonical:** one idempotent typed inverse of the exact applied operation | Keep canonical; delete unreachable version-restore body in B3 lane 3 | IR-09 |
| Proposal automation | `backend/concierge/proposal_automation.py` | **Canonical:** current policy resolver drives stored-operation resolution/application | Keep canonical | IR-08/16 |
| Proactive proposal producer | `backend/concierge/proactive.py`; `backend/core/itinerary_proposal_producer.py` | **Canonical:** feasibility and disruption signals mint exact operations or fail closed | Keep canonical | IR-08/16 |
| Planning proposal producer | `backend/concierge/tool_handlers/planning/_propose_present.py`; `backend/core/itinerary_proposal_producer.py` | **Canonical:** exact typed operation and attribution | Keep canonical | IR-08/16 |
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
- [x] Legacy recent-changes and compatibility-column readers are ratcheted across both repos.
- [x] IR-07 records the 2026-07-16 local retirement date for independently
      reachable legacy writes and a dated review/trigger for every retained
      structure. The finite edit-log acknowledgement remains explicitly open
      until deployed drain evidence licenses deletion.
