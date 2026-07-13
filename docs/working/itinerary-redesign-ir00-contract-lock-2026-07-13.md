---
doc_type: working
status: active
owner: backend / frontend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Lock itinerary operation vocabulary and evidence boundaries before runtime implementation.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir00-contract-lock]
---

# Itinerary redesign IR-00 contract lock

Date: 2026-07-13
Status: semantic contract locked; runtime endpoints remain unregistered and all
target flags remain off.

## Purpose

This record fixes the vocabulary and evidence boundaries that later slices must
implement. It is not an API launch and does not alter existing itinerary reads
or writes. Generated OpenAPI schemas become authoritative only when their routes
land in IR-06, IR-09, and IR-12; those schemas must preserve the semantics here
or record an explicit contract amendment.

## Canonical concepts

- Lifecycle is `ideation | planning(early|active) | final_prep | live |
  post_trip`, with `completed | cancelled` terminal context only in post-trip.
- Every action carries one human principal. Vesper may initiate on that
  principal's request but may not acquire broader authority.
- Scope is `personal | subgroup | whole_group`; decision ownership and planned
  participants are explicit.
- Plan truth and provider truth are separate. Provider intent is `plan_only` or
  `plan_and_provider` and never implies success.
- Revision preconditions are typed by shape, trip context, day, branch, block,
  proposal, provider dependency, or an explicit compound of those facts.
- A normalized operation has one stable identity, operation type, target,
  typed payload, attribution, precondition, and optional provider intent.
- Recovery is a current server-authored capability, never inferred from an
  operation label or UI age.

The executable backend source of truth is
`travel-agent/backend/core/models/itinerary_operations.py`.

## Request and response contract boundaries

The following is the minimum semantic shape. Field names may be refined before
route registration only if the generated OpenAPI review records the mapping.

### Lifecycle projection

Required: phase, destination-local date, timezone, timezone provenance, and
dogfood-override provenance. Planning requires early/active detail. Countdown,
current day, terminal state, and disruption summary are present only when
meaningful; clients must not derive them from device time or raw trip status.

### Capability projection

Required: outcome (`direct | confirm | propose | denied`), stable reason code,
predicted recovery, and whether voluntary proposal is allowed. When applicable,
include decision owner, proposal policy, confirmation reasons, protected
dependencies, and allowed alternatives. The server response is authoritative;
the client may hide controls but may not broaden authority.

### Preview

Request semantics:

- one normalized typed operation candidate;
- authenticated human principal binding;
- all revision/provider/proposal preconditions required by the operation;
- client request identity suitable for retry correlation, without granting
  idempotent commit by itself.

Response semantics:

- canonical normalized operation;
- current capability and reason code;
- stable preview identity and preview hash;
- exact preconditions bound into that hash;
- visible plan effect summary and protected/provider consequences;
- confirmation requirements and current recovery prediction;
- expiry/revalidation instruction.

Manual and Vesper entry must produce the same canonical operation semantics and
preview hash when target, payload, principal, and preconditions are equal.
Attribution channel and operation/request identities remain distinct evidence
and are excluded from semantic parity comparison.

### Commit

Request semantics:

- preview identity and hash;
- the same authenticated human principal;
- explicit idempotency key;
- confirmation evidence when preview required confirmation.

Response semantics:

- immutable operation identity and terminal/current transition state;
- committed plan revision(s) or a typed stale/rejected/failure result;
- immediate receipt projection;
- current recovery capability;
- provider transition when provider intent was requested;
- links/identifiers for canonical operation detail and affected stop lineage.

Commit must re-resolve policy and revisions. A stale or denied commit never
silently falls through to a legacy mutation and never loses the user's draft.

### Operation detail and history

All history surfaces project one immutable ledger identity. Operation detail,
immediate receipt, stop-lineage history, and trip-wide Changes must agree on:

- operation identity, type, attribution, and occurred-at time;
- typed target and before/after evidence;
- plan revision and provider transition truth;
- proposal/compound/inverse relationships;
- current recovery capability and degradation reason;
- tombstone/successor navigation for removed or replaced stops;
- viewer-specific omission of private context.

History pagination uses a stable cursor. Unseen state and attention-required
state are separate viewer projections. Notification/chat delivery is awareness
evidence, not the operation ledger.

## Golden fixtures and coverage

Backend executable fixtures:

- `travel-agent/tests/fixtures/itinerary_operations/ir00_golden_contracts.json`
  validates full lifecycle vocabulary and equivalent manual/Vesper Move
  semantics.

Frontend target-only fixtures:

- `travel-app/constants/personas/itineraryTargetFixtures.ts` covers undated
  solo; dated tentative/booked solo; Open and Review whole-group cases;
  personal/subgroup ownership; explicit split/rejoin; provider partial;
  stale/dependent operation; live disruption; completed/cancelled; and member
  departure/deletion with private context.
- The target fixtures are not registered in shipped persona mocks. Every record
  names its later-slice dependencies and required evidence.

## Telemetry vocabulary

No IR-00 code emits these events. Stable names are reserved in the existing
backend `Event` taxonomy:

| Event | Required/common labels |
|---|---|
| `itinerary.lifecycle_compared` | mode, trip_id, comparison_result, reason_code |
| `itinerary.policy_compared` | mode, trip_id, operation_type, outcome, comparison_result, reason_code |
| `itinerary.operation_previewed` | mode, trip_id, operation_id, operation_type, entry_channel, outcome |
| `itinerary.operation_committed` | mode, trip_id, operation_id, operation_type, entry_channel, provider_stage |
| `itinerary.operation_rejected` | mode, trip_id, operation_id, operation_type, failure_kind, reason_code |
| `itinerary.recovery_resolved` | mode, trip_id, operation_id, predicted_recovery, reason_code |
| `itinerary.provider_transitioned` | mode, trip_id, operation_id, provider_stage, failure_kind |
| `itinerary.projection_compared` | mode, trip_id, projection_surface, comparison_result, reason_code |

The strict label contract forbids uncontracted raw fields such as venue names,
addresses, human text, and provider references. Metric thresholds are not
invented in IR-00: each shadow slice must capture a representative baseline,
record the cohort/window/sample count, then amend the launch gate before its
behavior flag can advance.

## Evidence IDs

These IDs remain stable across automated tests, device runs, and launch review.

| ID family | Required proof |
|---|---|
| `IR-MV-01..12` | Manual/Vesper semantic parity for every normalized operation type |
| `IR-LC-01..09` | Lifecycle boundaries: undated, destination midnight, DST, fallback, multi-city, override, live, completed, cancelled |
| `IR-GV-01..09` | Solo/Open/Review × personal/subgroup/whole-group authority invariants |
| `IR-PR-01..06` | Preview hash, stale revalidation, idempotency, dependent operation, denied commit, draft preservation |
| `IR-HI-01..08` | Receipt/detail/stop/trip parity, inverse link, tombstone, pagination, unseen/attention |
| `IR-PV-01..07` | Owner/member/organizer/new/departed/deleted/public viewer privacy projections |
| `IR-PS-01..06` | Provider success, partial, retry, compensation, external-only, manual continuation |
| `IR-UI-01..10` | List/Map continuity, exact return state, Dynamic Type, screen reader, Reduced Motion, offline/degraded behavior |

An ID is not passing merely because a fixture exists. Later slices must link it
to a named automated test or dated device artifact.

## IR-00 closure checklist

- Mutation paths have an owner and migration disposition: complete.
- Strict lifecycle, capability, attribution, scope, protection, precondition,
  and normalized-operation vocabulary: complete.
- Golden executable parity/lifecycle fixture: complete.
- Target-state fixture coverage with explicit later dependencies: complete.
- Backend and frontend feature flags independently default off: complete.
- Stable metric names and low-cardinality label contract: complete; no emission.
- Semantic lifecycle/preview/commit/detail/history contract: complete.
- Stable cross-surface test ID families: complete.
- Production behavior change: none.
