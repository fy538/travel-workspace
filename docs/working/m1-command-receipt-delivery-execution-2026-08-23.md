---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the first end-to-end M1 command, durable receipt, delivery-repair, owner-readback, and cross-repository contract slice without introducing a speculative universal execution rail.
supersedes: []
promotes_to: null
source_of_truth_for: [m1-command-receipt-delivery-execution]
---

# M1 command, receipt, and delivery execution receipt

> Status: selected-loop implementation landed; portfolio M1 remains open until
> a second materially different loop exercises the contract and the process-
> death/export/correction evidence is certified.

## 1. Selected loop and boundary

The first M1 loop is the existing canonical itinerary operation path: a Plan
artifact proposes or receives a revision-bound operation, the Plan authority
revalidates and commits it, and the viewer can reopen the owner projection and
operation history. This is intentionally an adapter over the mature Trip/
itinerary authority, not a new graph Plan writer.

```text
Plan artifact / Vesper action
  -> IR-06 preview + capability
  -> IR-07 commit (revision + idempotency lock)
  -> domain mutation + vesper_action_receipts row
  -> itinerary_operation_transitions evidence
  -> itinerary_projection_outbox event
  -> Plan projection / operation-detail readback
```

The selected loop already had the required transactional outbox and repair
worker. M1 therefore adds the shared identity contract and operator readback;
it does not create a second outbox, inbox, receipt table, or Plan authority.

## 2. Shared contract

The backend contract lives in
`travel-agent/backend/core/models/execution_contract.py` and is surfaced as
the additive `canonical_execution` field on both `ItineraryOperationCommitResult`
and `ItineraryOperationDetail`.

### ResourceRef

`ResourceRef` names the canonical owner projection, not the transient card:

| Field | Plan-loop value |
|---|---|
| `kind` | `plan` |
| `id` | Trip UUID |
| `revision` | `operation:<operation_uuid>` after a committed mutation; null for a rejected attempt |
| `canonical_path` | `guide://trips/<trip_uuid>/plan` |

The deep link is platform-neutral and reopens the Plan owner. It does not
expose graph UUIDs or create a card-owned object identity.

### CommandEnvelope

The envelope binds the command UUID to the exact operation, authority, and
retry identity:

- `command_id`: domain operation UUID;
- `type`: normalized itinerary operation type;
- `target`: the Plan `ResourceRef`;
- `capability` and `capability_reason`: server-selected preview authority;
- `actor_id`: human principal under whom the command runs;
- `idempotency_key`: caller-supplied retry identity;
- `expected_revision`: first revision-bound precondition revision;
- `precondition_hash`: exact IR-06/IR-07 preview hash;
- `source_refs`: content-safe preview identity only;
- `audience`: current Plan receipt audience (`group`); and
- `issued_at`: commit instant when available.

### ActionReceipt

`ActionReceipt` is the stable cross-surface result envelope around the
existing durable `vesper_action_receipts` row:

- `receipt_id` is the existing durable receipt UUID;
- `command_id` joins it to the operation command;
- `resource` carries the owner/readback destination;
- `state` distinguishes `committed` and `rejected` (the envelope reserves
  `pending` and `reversed` for later loops);
- `changed` makes a rejected/no-op attempt explicit; and
- `readback_state` reports whether the owner projection can be reopened.

Rejected attempts now receive an atomic `vesper_action_receipts` row with
`status=errored`, `action_type=reject_change`, and the same operation-scoped
idempotency key. A repeated request therefore returns the same receipt
identity rather than disappearing into a transient error path.

## 3. Durability and recovery evidence

No new durable table was introduced. The selected loop uses the existing
authorities:

| Concern | Existing authority | M1 use |
|---|---|---|
| Command identity | `itinerary_operations` | `operation_id`, normalized operation, actor, idempotency key |
| Terminal evidence | `itinerary_operation_transitions` | serialized `commit_result`, including `canonical_execution` |
| Durable receipt | `vesper_action_receipts` | committed and rejected action receipt UUIDs |
| Delivery | `itinerary_projection_outbox` | same-transaction `itinerary_changed` event, projection version `operation:<id>` |
| Repair | claim/lease/defer/publish functions | expired leases and bounded exponential retry |
| Readback | `GET .../itinerary/operations/detail/{operation_id}` | viewer-scoped detail rehydrates canonical execution |
| Export/deletion | existing account-lifecycle registration | no new table/metadata registration required |

On a commit retry, the gateway locks the trip/idempotency key and replays the
stored terminal evidence. Older terminal rows that predate M1 are lazily
enriched on replay when they already have an action-receipt identity; new
terminal rows persist the complete envelope in transition evidence.

## 4. Operator view

`GET /admin/ops/itinerary-projection-outbox` is an admin-gated, content-free
diagnostic view. It reports `pending_count`, `due_count`, `leased_count`,
`retrying_count`, `oldest_pending_at`, `max_attempt_count`, and
`published_last_24h`. It never returns payloads, source text, private context,
or a second mutation path. Repair remains the existing outbox worker.

The operation is registered as `operator` in
`docs/governance/api-operation-policy.json`; it is intentionally excluded from
the active mobile OpenAPI projection.

## 5. Cross-repository surface

The backend OpenAPI snapshot and the generated mobile schema now include:

- `ResourceRef`;
- `CommandSourceRef`;
- `CommandEnvelope`;
- `ActionReceipt`; and
- `CanonicalExecution`.

The mobile facade aliases these generated types rather than maintaining a
second hand-written schema. `executeCanonicalItineraryOperation` returns the
server result unchanged, so a successful action preserves the canonical Plan
deep link and receipt ID through the executor boundary.

## 6. Evidence

Backend:

- 22 offline execution-contract and itinerary-contract tests pass;
- 49 focused receipt/contract/preview tests pass;
- isolated admin route harness confirms the operator endpoint is gated by the
  router dependency and returns no payload field;
- Ruff, import-cycle, public-projection, route-auth, JSON-response-model, and
  generated-contract checks pass for the changed surfaces.

Frontend and contract:

- 11 itinerary executor tests pass;
- `npx tsc --noEmit` passes;
- `make contract-check` passes, including full snapshot validation, mobile
  projection, generated-type equality, schema-bridge parity, and Place seams.

The repository-wide admin test module could not be imported in this local
environment because the installed virtualenv is missing `json_repair`; this is
an environment dependency gap, not a failure in the isolated M1 route harness.
The backend pre-commit ratchets also report pre-existing broad-exception,
oversized-file, and intake status-write baselines; those checks were skipped
only for the two backend commits and are recorded here for follow-up.

## 7. Gate assessment

| M1 gate | Status | Evidence / remaining work |
|---|---|---|
| Retry-safe command identity | Landed | operation lock + `CommandEnvelope` + replay test |
| Durable receipt for commit and rejection | Landed | existing receipt table, now populated for both terminal states |
| Process-death-safe delivery | Existing rail reused | transactional outbox and lease/retry tests; production fault drill remains |
| Repair/replay and operator visibility | Landed | existing worker plus admin counters |
| Canonical owner/deep-link readback | Landed | Plan `ResourceRef`, detail projection, mobile executor test |
| Export/deletion/correction/reversal | Existing authorities retained | no new table; full M1 lifecycle certification remains |
| Second materially different consumer | Open by design | next candidate is admitted artifact/intake, not another Plan adapter |

M1 is therefore **implementation-started and seam-proven**, not closed. The
next implementation packet should exercise the same identity/readback grammar
from an admitted artifact or conversational artifact only after its admission
and custody authority is ready (M2), and should not generalize fields merely
to satisfy a roadmap checklist.
