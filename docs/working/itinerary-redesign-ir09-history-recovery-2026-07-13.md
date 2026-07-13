---
doc_type: working
status: active
owner: backend / frontend API contract
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the IR-09 one-ledger history projections, live recovery resolver, and exact move Undo proof boundary.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir09-history-recovery]
---

# Itinerary redesign IR-09 — history and recovery

## Outcome

IR-09 projects immediate receipts, canonical operation detail, stop-lineage
history, and trip history from `itinerary_operations` plus its append-only
transition evidence. These surfaces share operation identity, normalized intent,
before/after delta, attribution, terminal state, provider transitions, receipt,
committed revisions, and live recovery truth.

The guarded surface is:

- `GET /api/trips/{trip_id}/itinerary/operations/history`
- `POST /api/trips/{trip_id}/itinerary/operations/history/seen`
- `GET /api/trips/{trip_id}/itinerary/operations/detail/{operation_id}`
- `POST /api/trips/{trip_id}/itinerary/operations/detail/{operation_id}/undo`

`ITINERARY_HISTORY_V2` remains default-off. The endpoints are built-dark until
IR-12 read-model convergence and a dogfood client explicitly adopt them.

## Recovery truth

`OperationRecoveryCapability` is recomputed from current membership and
governance, exact post-operation revisions, later sibling or block mutations,
protected dependencies, provider intent, existing inverse operations, and a
fresh policy preview of the typed inverse.

Only `move` currently advertises executable Undo. It does so only when the
inverse preview is direct and the exact source/destination day, block, ordering,
time, and branch evidence still match. Add, Replace, Remove, and attendance
currently degrade to `new_change`, `review_revert`, or `provider_action`; their
preview-era optimistic labels are not returned by committed receipts.

Undo creates a normal typed Move through the IR-07 transactional commit spine,
then links it with `inverse_of_operation_id` in the same transaction. It uses a
source-operation advisory lock, supports idempotent replay, and has no separate
mutation path.

## Viewer and navigation projections

- Stable opaque pagination is ordered by `(created_at, operation_id)`.
- A lineage filter projects stop history from the same rows as trip history.
- Private-context safe labels are returned only to their owner; group history
  never joins another viewer's private references.
- Seen state uses a monotonic per-viewer cursor. It does not clear or redefine
  Needs-attention, which is derived separately from operation/provider truth.
- Cancelled blocks project a tombstone and, when present, the current active
  block with the same subject lineage as the successor.

## Verification

Disposable PostgreSQL migrated through `ir08a001`:

```text
IR-09 gateway proofs: 6 passed
IR-07/IR-08/IR-09 PostgreSQL regression: 16 passed
IR-06..IR-09 focused backend: 104 passed
route-auth coverage: 14 passed
```

The IR-09 proofs cover cross-surface identity/delta/receipt/recovery parity,
trip and lineage pagination, private-label omission, monotonic seen cursors,
Needs-attention separation, remove tombstones, exact Move Undo, idempotent
replay, stale-revision degradation, current-authority denial, protected-provider
degradation, rollback fault injection, and a two-writer race with exactly one
winner.

Generated contract verification:

```text
OpenAPI snapshot: fresh
frontend schema.gen.ts: regenerated
frontend TypeScript: clean
frontend focused Jest: 51 passed
```

The backend route-coverage audit recognizes the four IR-09 endpoints as
built-dark. Its remaining ten uncovered routes are the pre-existing unrelated
baseline.

## IR-10 / IR-12 handoff

IR-10 may append provider transitions without changing the history identity or
collapsing plan and provider truth. IR-12 should consume these projections rather
than assemble activity from notifications, chat delivery, or legacy plan events.
Additional operation types may enter the executable Undo allowlist only after
the same authority, dependency, revision, idempotency, concurrency, and fault
proofs pass for that exact inverse.
