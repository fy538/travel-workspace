---
doc_type: working
status: active
owner: backend / workspace API contract
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: IR-06 freezes the canonical typed-operation preview contract and its cross-entry semantic identity before transactional commit or frontend mutation wiring begins.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir06-operation-preview]
---

# Itinerary redesign IR-06 — typed operation preview

## Outcome

IR-06 is complete. The backend now exposes a default-off, read-only canonical
preview endpoint:

```text
POST /api/trips/{trip_id}/itinerary/operations/preview
```

The commit endpoint is intentionally not registered. IR-07 must first provide
transactional mutation, immutable ledger evidence, idempotency, and commit-time
revalidation.

This is a `contract-sensitive` backend/API change. It does not change shipped
Plan reads, replace any legacy writer, or enable a frontend mutation path.

## Contract

The request carries one strict `NormalizedItineraryOperation` and a bounded
`client_request_id`. The latter is retry correlation only; it does not grant
commit idempotency.

The response includes:

- the canonical normalized operation and exact bound precondition;
- current server-authored capability, reason code, confirmation requirements,
  protected dependencies, and predicted recovery;
- a group-safe effect summary and provider consequence;
- a stable semantic preview ID and SHA-256 preview hash;
- an explicit ten-minute expiry and instruction that commit must revalidate
  current facts.

The hash binds operation type, target/lineage, payload, placement/day/time and
branch semantics, scope/participants/owner, provider intent, ordered compound
children, every typed precondition, and the authenticated human principal.
It excludes operation ID, client request ID, initiator, requested-by evidence,
and entry channel. Those remain present in the returned normalized operation as
attribution evidence, but do not make equivalent Plan, Map, Discover, Chat, and
Vesper intent semantically different.

Set-like participant and branch-block fields are canonicalized before the
normalized operation is returned. Ordered compound children remain ordered.

## Read-only gateway

The gateway loads current trip membership/governance, explicit decision owner,
participation, lifecycle, protected dependencies, provider controller,
delegation, and durable revision facts. It fails closed when any required fact
is unavailable.

Revision checks cover shape, trip context/itinerary head, day, branch, block,
provider, proposal, and compound preconditions. Existing integer revisions
accept raw, `rN`, or typed `day-rN`/`block-rN` forms during the compatibility
window. A stale revision returns a denied capability with
`reason_code=revision_stale`; it never falls through to a legacy mutation.
Referenced members, catalog entities, destination days, placement anchors,
branches, parallel blocks, and child-operation targets are also proven against
the same trip before policy resolves. Provider references are redacted from the
preview while typed protection consequences remain visible.

Vesper preview requires an authenticated human principal and a live,
non-revoked operation-specific delegation. Provider intent fails closed when
no protected dependency exists, and `plan_and_provider` requires an explicit
provider revision precondition. Whole-group Add must name every current member.

## Exposure and parity

`ITINERARY_OPERATIONS_PREVIEW_V2` remains default-off. Disabled requests return
`403 itinerary_operation_preview_disabled`. Enabled requests authenticate the
user, verify trip membership, bind the path trip and human principal, and run
DB resolution off the event loop. Successful dogfood previews emit only the
reserved privacy-safe telemetry vocabulary.

Executable fixtures prove that Plan (`itinerary`), Map, Discover, human Chat,
and Vesper Chat produce the same semantic preview hash and ID for equivalent
intent while preserving their distinct attribution. The shared OpenAPI
snapshot and generated frontend TypeScript now contain the frozen IR-06 shape;
the app route is intentionally dark until IR-13/14.

## Validation evidence

- 136 focused lifecycle, operation, policy, adapter, parity, route/auth, and
  schema tests passed offline.
- A freshly migrated disposable PostgreSQL database proved current revisions
  resolve direct, stale revisions resolve denied, and neither preview writes an
  `itinerary_operations` row.
- Full offline-suite audit: 11,448 passed, 17 skipped, 574 deselected, one
  expected-suite xpass, and 20 unrelated pre-existing failures. The failures
  are in legacy auth/mocking, stale local-schema route tests, time-sensitive
  booking/home tests, and postcard/concierge mocks; none touch the IR-06 route
  or gateway.
- Ruff and focused formatting checks passed.
- Route-auth scan reports zero violations.
- OpenAPI freshness, frontend generated-type parity, and TypeScript typecheck
  passed.
- Backend route coverage no longer reports the IR-06 endpoint. Eleven
  unrelated pre-existing uncovered endpoints remain in that repository-wide
  check.
- Alembic remains at the single `ir05a001` head. `alembic check` reports only
  the repository's known unrelated global metadata drift (legacy search/GiST
  indexes and one historical hard-constraint relationship); IR-06 adds no
  schema or migration drift.

The disposable database was removed after final migration checks. No shared
database is migrated or backfilled for IR-06.

## IR-07 handoff

IR-07 may consume `preview_id`, `preview_hash`, the normalized operation, and
bound preconditions. Commit must recompute semantic identity and revalidate
principal, authority, revisions, protection, provider facts, and confirmation
evidence inside the same transaction that writes both structural state and
immutable operation evidence.
