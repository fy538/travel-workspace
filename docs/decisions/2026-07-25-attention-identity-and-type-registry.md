---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-07-25
decided: 2026-07-25
why_new: Preserve the accepted cross-surface attention identity, type registry, and projection ownership boundaries.
supersedes: []
source_of_truth_for: [attention-identity-and-type-registry]
---

# Attention identity and type registry

**Date:** 2026-07-25
**Status:** accepted

## Decision

Use one exhaustive `notification_type` registry for policy-bearing product
vocabulary. Keep model-authored `intent` as free-text telemetry, never as a
rendering, interruption, privacy, or projection-policy selector.

Persist recipient-relative `attention_cases` only when a subject needs
cross-producer, cross-time, or cross-surface lifecycle. Identity is unique on:

```text
(notification_type, subject_type, subject_id, recipient_id)
```

Domain systems continue to own truth. An attention case owns awareness/work
state and projection correlation, not proposal, itinerary, booking, expense, or
membership state.

Each registered type declares its decision mode, attention class, lifecycle,
audience rule, urgency/interruption ceiling, allowed projections, Home rendering
and owner, expiry, dedupe, destination, and cancellation strategy. Invalid
cross-axis combinations fail startup validation.

## Projection ownership

Only one active `home.primary` projection may exist per recipient attention
case. The registry names its owner. For the feasibility Catch and venue
disruption, the canonical change proposal is the subject and the proposal read
model owns `home.primary`; the notification announcement may create inbox or
remote projections but not a competing Home card.

The Catch key is:

```text
feasibility_catch:change_proposal:<proposal_id>
```

Every recipient has a distinct case row for that key. Proposal resolution
completes those cases and expires linked durable projections in the proposal
transaction.

## Consequences

- Independent producers converge through a database uniqueness constraint
  rather than timing or shared in-memory state.
- Inbox, push, and Home can route and reconcile using the same type, case, key,
  and subject identity.

## Follow-on policy rulings

Adjudicated on 2026-07-26:

- The badge counts feed entries that are unread or still require action.
  Visibility does not complete open work.
- Email is an asynchronous delivery class. It retains preferences, truth,
  dedupe, expiry, and outcomes, but does not consume the push/SMS interruptive
  cap or inherit mobile quiet-hours timing.
- Live-travel experiments remain outside the MVP release gate until physical
  iOS/Android and accessibility proof is complete.
- Learned arbitration optimization remains dark until trustworthy exposure
  data, causal holdouts, sample-size requirements, and rollback thresholds
  exist.
- Ambient request-time opportunities remain ephemeral only when they cannot
  duplicate a durable projection and need no cross-surface lifecycle.
- `candidate_type` remains temporarily as a persistence compatibility field;
  new policy code uses `notification_type`.
- This decision does not yet replace the existing fan-out implementation with
  the Phase 2 delivery spine, and it does not constitute device certification.
