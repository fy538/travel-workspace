---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: "Records the bounded M5 completion: retained Trip execution can be represented by a durable graph Commitment, external handoff can be scoped and revoked, provider evidence can be read back, and lived reality remains a separate reconciliation path."
supersedes: []
promotes_to: null
source_of_truth_for: [m5-execution-and-reality-closure]
---

# M5 execution and reality closure

## Decision

M5 closes at the external-handoff boundary. The product now has one durable
identity seam from a retained itinerary block to a clean-graph Commitment, one
explicit task-scoped capability for that handoff, a separate provider return
receipt/read path, and a separate occurrence/outcome reconciliation path.

The product does not become a first-party booking, payment, messaging, or
provider-workspace product. The legacy Trip/provider stack remains the
execution authority until a later journey proves that a deeper adapter is
worth its operational and trust cost.

```text
retained Trip block
  -> explicit graph Commitment + external identity link
  -> one issued handoff task (single attempt, revocable, expiring)
  -> provider operation / callback
  -> append-only provider evidence + Commitment revision
  -> participant-scoped provider history
  -> separately reconciled occurrence
  -> separately authored personal Outcome
```

## What shipped

### 1. Durable Trip/block identity

`commitment_external_links` stores the owner, legacy Trip, itinerary block,
source revision, and a small immutable source snapshot. It is a bridge, not a
copy of the Trip model. The source block remains authoritative for itinerary
execution and provider sagas.

`POST /api/experience-graph/commitments/from-trip-block` requires an explicit
authenticated member action. The adapter:

- accepts only a real Trip member and an existing block;
- rejects free-time/transit/interlude, skipped, cancelled, unknown, or
  untitled blocks;
- maps planning/coordination state to `proposed` or `accepted` only;
- preserves participants and time window when present; and
- never infers provider confirmation, attendance, or enjoyment.

The source block is unique in the bridge, so two graph Commitments cannot
silently represent the same retained operation.

### 2. Task-scoped external execution

`commitment_execution_tasks` is the smallest capability object needed to hand
one retained Commitment to an external executor. It is linked to the source
identity row and participant owner, has an expiry and revision, and supports
explicit revocation.

`POST /api/experience-graph/commitments/{commitment_id}/execution-tasks`
issues a task. `POST /api/experience-graph/execution-tasks/{task_id}/revoke`
revokes it. The database and command contract enforce `max_attempts = 1`:
retry is never inferred from a timeout or failure; a human must issue a new
task after reviewing the current state.

The task scopes only `external_handoff` or `provider_observation`. It grants
no payment, contact, booking, attendance, or personal-meaning authority.

### 3. Provider return and readback

The existing server-only provider route remains the only provider-evidence
writer. It now optionally accepts a task ID and rejects revoked, expired, or
unrelated capabilities before appending evidence. The provider command still
owns revision CAS, source custody, transition validation, idempotency, and
action receipts.

`GET /api/experience-graph/commitments/{commitment_id}/provider-evidence`
returns append-only provider observations only to a Commitment participant.
The regular graph projection exposes the current provider state/revision; the
history endpoint exposes evidence details without adding occurrence or
personal meaning.

### 4. Lived reality and personal meaning stay separate

The existing reconciliation command and server-only route remain separate from
provider callbacks. A provider `confirmed` state does not write occurrence
evidence. `record_reconciled_occurrence` is source-backed, revisioned, and may
advance a linked Occasion only when the episode was already planned. A
participant's `personal_outcome` is a separate, private-by-default write and
is never synthesized from provider or shared occurrence evidence.

## State and recovery invariants

- one shared Commitment has one revision and one provider projection;
- provider `unknown`, `failed`, or expiry is evidence, not an automatic retry;
- provider confirmation is not attendance, and attendance is not enjoyment;
- revocation prevents a callback from using the task capability;
- source identity collisions fail rather than fork graph truth; and
- correction uses append-only evidence lineage and revisioned receipts so
  provider, occurrence, and personal projections converge independently.

## Verification

- 152 focused graph/API/lifecycle tests pass, including adapter, migration,
  execution-task, provider-auth, provider-state, occurrence, and command
  guards.
- Ruff passes on every M5 production/test file.
- Alembic has one head at `xgraph19` (`intakev204 -> xgraph18 -> xgraph19`).
- Full OpenAPI snapshot: 557 paths / 619 operations / 1,292 schemas.
- Active mobile projection remains 424 paths / 469 operations / 1,140 schemas;
  the new M5 transport is intentionally server-only until a reviewed mobile
  journey consumes it.
- `make contract-check` passes, including API policy, place identity, schema
  bridge, and occasion behavior contracts.

## Explicit non-goals

No first-party provider account, payment, contact, booking workspace, or
automatic retry was added. Provider sandbox and multi-account evidence remain
conditional on choosing a direct execution journey; the current product
boundary is an external handoff with a durable return receipt.
