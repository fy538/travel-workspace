---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-16
decided: 2026-08-16
why_new: Freeze the content-free references that let every surface identify one Plan revision and the temporary constitution governing shared decisions without replacing Trip or proposal authority.
supersedes: []
source_of_truth_for: [plan-revision-reference, group-decision-constitution]
---

# Reference one Plan revision and project one group constitution

## Context

Trip itinerary mutation, proposal resolution, membership, delegation, and
readback are individually strong. Cross-surface consumers do not yet carry one
small reference proving which Plan revision they judged, and multiplayer policy
is distributed across organizer checks, proposal policy, membership, and
domain-specific authorization.

The company model generalizes Trip to Plan, but the current implementation must
not weaken Trip guarantees or invent a universal Plan table.

## Decision

Add two frozen, content-free contracts in `backend/core`:

1. `PlanRevisionRef` identifies the canonical Plan specialization and exact
   revision used by a read, judgment, proposal, or receipt.
2. `GroupDecisionConstitution` is a read-only projection of current membership,
   roles, delegation, and domain policy for that Plan revision.

The initial supported `plan_kind` is `trip`. New kinds require a registered
authority adapter and proof entry; callers may not synthesize generic Plan IDs.

### `PlanRevisionRef` v1

Required fields:

- `contract_version=1`;
- `plan_kind="trip"`;
- `plan_id`;
- `revision_kind="itinerary_version"`;
- non-negative `revision`;
- `authority="itinerary_commit_gateway"`;
- `observed_at`.

The owning type belongs in `backend/core/models/plan_references.py`. The
projection adapter belongs beside the canonical itinerary read gateway. It is
a reference, not a copied itinerary and not proof that a later command applied.

### `GroupDecisionConstitution` v1

Required fields:

- `contract_version=1` and `plan_ref`;
- `relationship_scope` and exact `roster_revision`;
- actor-role assignments for organizer, member, and bounded delegate;
- per-domain policies for `propose`, `resolve`, `spend`, `commit`, `undo`, and
  `share_memory`;
- privacy rule version;
- projection time and expiry.

The owning type belongs in
`backend/core/models/group_decision_constitution.py`; the projector belongs in
`backend/core/group_decision_constitution.py`. V1 is derived from canonical
membership, proposal policy, and delegation state. It has no independent writer
or table.

Engagement, expertise, and social power may influence whom Vesper asks. They do
not silently change welfare weight or authorization.

## Migration

1. Add types and projectors with characterization tests.
2. Attach `PlanRevisionRef` to new cross-domain judgments and artifacts.
3. Compare constitution results in shadow against existing domain checks.
4. Move authorization callers only after parity receipts are exact.
5. Retire direct policy reconstruction per caller after production-zero
   compatibility evidence.

Existing itinerary and proposal writers remain authoritative throughout.

## Rollback and compatibility

Adapters are additive. A rollback removes the new projections and restores the
existing direct checks; it never rewrites itinerary history. Historical
artifacts without a reference remain readable but are explicitly classified as
compatibility records and cannot authorize a new consequential action.

## Proof gates

- stable reference across Plan, Map, Home, Chat, and proposal readback;
- stale revision rejection after a concurrent itinerary mutation;
- roster-change and delegation-revocation invalidation;
- private input never appears in group-safe constitution output;
- existing organizer/member authorization parity before migration;
- no new Plan table and no change to itinerary commit semantics.

## Non-goals

- Generalizing local Plans before an authority adapter exists.
- Replacing proposal state machines or itinerary commit gateways.
- Encoding private preferences in the constitution.
- Treating a reference as completion evidence.
