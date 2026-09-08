---
doc_type: decision
status: accepted
owner: founder / Capture / Integration / Life
created: 2026-09-08
decided: 2026-09-08
why_new: Records founder approval of candidate-owned anchor lifecycle option A; an execution receipt cannot establish this cross-repository authority choice.
supersedes: []
source_of_truth_for:
  - capture-candidate-anchor-lifecycle-ownership
---

# Capture owns candidate lifecycle; graph anchors remain projections

## Decision and provenance

The founder approved option A after the September 8 Strategy review of the
[integration checkpoint](../working/integration-execution-checkpoint-2026-09-07.md).
Extend Capture's existing candidate lifecycle and durable delivery rather than
create a graph-owned lifecycle stream. The current
`ExperienceAnchorProjection` is explicitly non-authoritative; this decision
preserves that ownership while authorizing the missing lifecycle implementation.

Capture owns confirmed candidate identity and lifecycle truth. Source/submission
custody remains distinct. Graph and Life consume governed projections; neither
becomes an independent authority for the underlying candidate.

## Required implementation properties

1. Preserve stable candidate identity separately from submission/source identity.
2. Use an owner-issued, monotonically ordered candidate revision. Event hashes
   and timestamps alone must not stand in for this ordering.
3. Commit the owner mutation and durable event atomically through existing
   delivery machinery. Retries preserve identity and do not duplicate effects.
4. Identify the candidate authority explicitly; do not disguise its changes as
   source revisions. Integration owns the precise versioned envelope, partition
   mapping and compatibility treatment, coordinated with Capture and Life.
5. Recheck current owner, source eligibility and applicable permissions before
   applying or serving a projection. Stale/out-of-order events cannot resurrect
   withdrawn state. Candidate ordering does not replace source revocation checks.
6. Withdraw affected dependent projections without deleting independent records
   or overwriting deliberate user controls.
7. Restoration requires a new explicit owner-authorized transition and newer
   revision. It does not restore expired grants, deleted sources or user exclusions
   by implication; all current eligibility checks still apply.

Necessary scoped models, migrations, producer/consumer adapters and tests are
authorized implementation work under this decision. Integration owns the exact
contract and reviewed landing; Life owns its consumer. Preserve current event
consumers during migration, or explicitly retire them with replacement evidence.

## Why not a graph-owned stream

Option B would add a lifecycle authority at a projection layer and require
reconciliation with Capture without an established independent responsibility.
Reusing delivery does not mean reusing an inaccurate owner identity. This choice
permits a precise candidate handoff within existing machinery, not a second
queue, universal event bus or duplicate truth store.

## Acceptance and exclusions

Exercise confirmation/correction, duplicate and reordered delivery, withdrawal,
explicit restore, concurrent owner changes and source-access loss against a
disposable database and current-authority reads. Verify independent neighbors
and user controls survive. Report actual revisions and consumer evidence.

This decision does not certify implementation, authorize inferred attendance or
personal meaning, widen retention/audience, adopt Social policy, activate Source
production or indexed Life serving, retire Atlas, or authorize remote publication.
The [Contribution and Consequence contract](../systems/contribution-and-consequence.md)
continues to govern all five authority axes. Implementation details and evidence
belong in existing owner contracts and lane receipts, not additions to this ADR.
