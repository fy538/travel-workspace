---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the executable IR-10 provider-saga contract, exit evidence, and downstream read-model handoff.
source_of_truth_for: [itinerary-redesign-ir10-provider-saga-evidence]
---

# IR-10 — Canonical provider saga evidence

IR-10 continues the accepted operation and history spine. It does not introduce
a frontend surface. Replace-and-rebook remains the primary protected workflow;
the reference single-action proof is one linked held booking becoming confirmed.

## Durable contract

- `itinerary_provider_sagas` separates committed plan outcome, provider outcome,
  continuation, controller, source/replacement dependency, booking-offer links,
  expense link, provider revision posture, and creation idempotency.
- `itinerary_provider_saga_events` is append-only and unique by both sequence
  and callback idempotency key. Reusing a key with any changed callback field is
  rejected.
- Only one nonterminal saga may control a protected dependency. Successful
  provider results require a provider revision.
- Cross-table triggers reject operation, dependency, booking, replacement, and
  expense links outside the saga trip.
- The controller must still be a current trip member for continuation. User
  deletion detaches controller/actor identity without deleting group-safe saga
  history.

Replace-and-rebook explicitly covers source-cancellation pending/failure,
replacement-booking pending/failure, success, and manual-provider-action. Every
failure leaves a typed continuation; provider failure never rolls back the
already committed plan or claims provider success.

## Held-to-confirmed proof

One transaction changes the protected dependency and linked booking offer from
held to confirmed, appends exactly one canonical provider transition, appends
exactly one terminal operation-history transition, and settles the saga. Fault
injection after either provider write rolls the whole callback back. Replaying
the identical callback is a no-op; changing provider revision under the same
idempotency key is rejected.

The test retains the same block/lineage, dependency, booking-offer, expense,
saga-event, operation, and provider-transition identities across repeated
reads. The callback does not create or change an expense amount or currency.

## IR-12/13/16 handoff

`project_provider_truth_for_operation` is the single viewer-scoped provider
projection owner. It supplies:

- itinerary commitment metadata;
- Bookings grouping;
- contextual attention state and reason;
- stable event/lineage, dependency, booking-offer, expense, operation, and saga
  links;
- provider state/ref/revision for the authorized controller;
- masked-expense absence for unauthorized viewers; and
- separate plan, provider, and expense truth.

Canonical history consumes this projector instead of reconstructing provider
state. IR-12 should reuse it for versioned Plan/Details/Bookings/attention read
models. IR-13 and IR-16 own all shell, provider-detail, and continuation UI.

## Verification

- Fresh PostgreSQL upgrade through `ir10a001` passed.
- `ir10a001 -> ir08a001 -> ir10a001` passed.
- Final focused operation/preview/commit/proposal/history/provider/schema,
  foundation-flag, and telemetry suite: 135 tests passed.
- Ruff and `git diff --check` pass on the backend slice.
- Provider routes remain independently default-off and are registered as
  built-dark until IR-13/IR-16 adoption.

No travel-app component, route, generated client, or UI contract is changed by
IR-10.
