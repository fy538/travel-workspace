---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Defines the first bounded M5 slice that joins retained provider capability to Commitment truth without turning the product back into a first-party Booking workspace.
supersedes: []
promotes_to: null
source_of_truth_for: [m5-provider-evidence-return-receipt]
---

# M5A provider evidence and return receipt

## Decision and boundary

M5 is optional until a retained experiential loop needs more than an external
handoff. The first increment therefore proves the return side of that seam:
trusted provider or reconciliation workers can append provider evidence to one
canonical Commitment, advance its provider revision, and receive a durable
action receipt. The user-facing product still hands work off to the provider;
it does not become a booking workspace.

```text
explicit Commitment
  -> external handoff / retained provider operation
  -> scoped server callback
  -> provider evidence + revisioned Commitment projection
  -> durable receipt / read projection
  -> occurrence reconciliation remains a separate decision
```

This is deliberately not a payment, contact, retry, attendance, or enjoyment
authority. A provider confirmation is evidence about the provider object only;
it never writes occurrence or personal Outcome truth. A missing or timed-out
callback is represented by the existing `unknown` path and does not trigger an
automatic retry.

## What exists before M5A

- The clean graph already owns Commitment coordination, provider, and
  occurrence vocabularies with independent revisioned state machines.
- `record_provider_evidence` already validates provider authority, source
  lineage, expiry, confidence, idempotency, and revision CAS, and writes the
  shared action receipt.
- The retained itinerary/provider saga already owns direct provider execution,
  controller checks, stale-revision handling, manual recovery, and external
  handoff projections.
- The graph projection already separates provider state from occurrence and
  personal Outcomes.

The missing production seam was transport: the provider command had no mounted
server-only route, and no dedicated token separated provider callbacks from
location/occurrence reconciliation.

## M5A implementation

### Backend

1. Add `EXPERIENCE_GRAPH_PROVIDER_TOKEN` and a secure-by-default dependency.
2. Mount `POST /api/experience-graph/provider-evidence` behind that dependency.
3. Keep the request server-owned (`owner_id`, Commitment/evidence IDs,
   provider state/reference, source objects, observed/expiry timestamps,
   confidence, authority, expected revision, and idempotency key).
4. Preserve the existing provider command as the only durable writer; the
   route is transport, not a second lifecycle implementation.
5. Add a pure itinerary-to-graph provider-state adapter. It maps `paid` to
   provider `confirmed`, keeps unsupported/ambiguous provider values out of
   the clean state machine, and never maps a provider state to occurrence.

### Contract and governance

- Classify the route as server-only and active in the API operation policy.
- Regenerate the full OpenAPI snapshot and the active-mobile projection. The
  provider callback is not an app mutation and therefore must not introduce a
  mobile transport or UI dependency.
- Keep the existing `/reconciled-occurrence` route on its separate
  reconciliation token; provider evidence and lived occurrence are distinct
  trust boundaries.

## Exit evidence for M5A

- [x] Service token is absent-by-default and rejects missing/invalid values.
- [x] Provider evidence route binds the server payload to the existing command.
- [x] Provider authority, provider-state mapping, ambiguity handling, and
      route payload validation are regression-covered; database transition,
      revision, replay, and source-ownership cases remain in the existing
      command integration lane.
- [ ] Provider evidence can be read through the existing viewer-relative graph
      projection without implying occurrence or personal meaning.
- [ ] Existing retained itinerary/provider saga tests remain green.
- [ ] The OpenAPI and operation-policy snapshots agree across both repositories.

## Explicitly deferred after M5A

1. A durable legacy Trip/block-to-graph Commitment identity link and its one
   selected Trip/Occasion adapter.
2. Task-scoped capability issuance, revocation, and per-operation retry budget
   for a real provider account.
3. Provider sandbox or multi-account production evidence.
4. Occurrence reconciliation and shared-Occurrence/personal-Outcome UI proof.
5. Any first-party payment, messaging, booking workspace, or broad provider
   automation.

Those are the next M5 increments only if a retained human journey justifies
them; they are not implied by this transport seam.
