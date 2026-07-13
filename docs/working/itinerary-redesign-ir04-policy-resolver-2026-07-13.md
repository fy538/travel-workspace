---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Document the IR-04 pure itinerary policy resolver boundary, inputs, and invariants.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir04-policy-resolver]
---

# Itinerary redesign IR-04 policy resolver

Date: 2026-07-13
Status: pure resolver complete; no runtime adapter or behavior flip

## Ownership

The side-effect-free resolver is
`travel-agent--itinerary-foundation/backend/core/itinerary_policy.py`. It has
no database, route, clock, feature-flag, or telemetry dependency. IR-05 will
own loading facts and comparing its results with legacy behavior.

## Input boundary

Resolution requires explicit:

- attribution and one human principal;
- current membership and organizer role as facts, not grants;
- Solo, Open, or Review governance;
- canonical lifecycle and terminal context;
- personal, subgroup, or whole-group scope;
- decision owner and affected people;
- normalized operation type and risk;
- protected dependencies, provider intent, and provider controller;
- privacy posture, Vesper delegation, and revision posture.

Unknown membership, principal, privacy, ownership, revision, or provider
control fails closed.

## Authority rules

- Human and Vesper-requested actions are the only accepted initiators. System
  and provider initiators cannot borrow a human principal's plan authority.
- Personal structure requires its named owner. Another traveler or organizer
  cannot propose or commit it; an affected traveler may instead change only
  their own attendance.
- Subgroup structure requires its named owner for Direct/Confirm. An affected
  non-owner may Propose to that owner. An unaffected organizer is denied.
- Open whole-group structure grants authority to a current affected member due
  to governance, not organizer status.
- Review whole-group structure requires its named decision owner. Other
  affected members may Propose to that owner.
- Attendance is self-only. Occurrence correction requires current structural
  ownership. Post-trip permits attendance/occurrence correction but not
  structural reopening.
- Vesper with insufficient delegation is denied. With preview/confirmation
  delegation it may prepare the human's result, but never receives Direct.
- `plan_and_provider` requires an explicit provider controller. Plan ownership,
  Open governance, and organizer status do not imply provider authority.
- Protected, broad, meaningful, high-risk, irreversible, or provider actions
  require confirmation when the principal otherwise has commit authority.
  Materialize, parallel-plan, Optimize, and Replan operations have a minimum
  meaningful-change confirmation floor.
- Stale and missing revisions deny with a typed refresh-and-retry alternative;
  authored intent preservation remains the caller's responsibility in IR-06.

## Output boundary

Every result uses the locked capability contract:

- `direct | confirm | propose | denied`;
- stable reason code;
- decision owner and proposal policy when applicable;
- confirmation reasons and protected dependencies;
- truthful alternatives;
- predicted recovery;
- voluntary-proposal capability.

The resolver outcome remains distinct from later execution state.

## Evidence

`tests/fixtures/itinerary_policy/ir04_governance_matrix.json` names
`IR-GV-01..09` across Solo/Open/Review and
personal/subgroup/whole-group cases. The test generator additionally evaluates
216 governance × scope × actor × initiator × revision combinations.

Adversarial tests prove:

- organizers cannot override personal or subgroup ownership;
- an organizer omitted from a whole-group affected set cannot self-authorize;
- nonmembers and stale/missing revisions always fail closed;
- Vesper never resolves Direct;
- system/provider initiators cannot borrow a principal;
- malformed scope facts and missing owners fail closed;
- provider control is never inferred from plan authority;
- provider-aware proposals require the decision owner to control the provider
  action;
- post-trip factual correction does not reopen structure.

Validation: 157 focused foundation, lifecycle, backfill, operation-contract,
telemetry, and policy tests passed; Ruff, Alembic single-head, and diff checks
passed. Alembic head remains `ir03a001` because IR-04 is pure code.
