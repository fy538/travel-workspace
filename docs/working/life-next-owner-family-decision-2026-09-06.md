---
doc_type: working
status: active
owner: Life lane / Experience Graph lane
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: "Selects the next shadow owner family after retained-source and Occasion delivery without reopening the product grammar."
source_of_truth_for:
  - next Life shadow owner-family scope
---

# Life next owner-family decision — 2026-09-06

## Recommendation

Implement **existing owner-private Plans** as the next Life shadow owner
family. Do not implement loose pre-Plan intention, shared arrangement
material, or Outcome delivery in the same package.

This is an engineering sequencing decision, not permission to cut over Life
serving. The package should prove that the same outbox → event bus →
current-authority read → revision-CAS index path works for an integer-revision
graph owner whose audience is exactly its owner.

## Why Plan is the next bounded family

The canonical graph already supplies the required evidence:

- `experience_graph.plans` has an integer `revision`, owner identity, and
  guarded create/update/lifecycle commands in
  `backend/domains/experience_graph/commands.py` and
  `backend/domains/experience_graph/lifecycle_commands.py`.
- `get_experience_projection(viewer_id=...)` already exposes Plans only to
  their owner in `ProjectionMode.my`.
- `life_read_from_experience` and `build_life_corpus_snapshot` already know how
  to render a Plan as a Life record; no new record grammar is required.
- A private Plan has no cross-viewer grant fan-out. Account erasure can remove
  the owner's derived row through the existing owner cascade; no shared
  audience handoff is implied.

This makes Plan a useful second owner-family proof without depending on the
unadopted retained-intention owner proposal or on the arrangement lane's
future command/readback work.

## Why Outcome is not next

Outcome is not merely another private integer-revision row:

- `personal_outcomes.visibility` can be `shared`.
- Shared visibility may be authorized through an Occasion or through a shared
  Commitment's participant set.
- The current graph reader has separate authorization paths for owner-private,
  Occasion-shared, and Commitment-participant outcomes.
- Owner deletion, Occasion departure, Commitment participant changes, and
  outcome visibility corrections would need an explicit before/after viewer
  union and withdrawal/restore contract.

The existing owner matrix correctly keeps Outcome shadow-only, but its
`supports_delta_delivery=False` declaration should remain until that audience
contract is designed and tested. Do not solve it by broadcasting every graph
viewer or by letting Life infer grants from a presentation record.

## Plan package boundary

The eventual Plan package may include only:

1. Producer events for canonical Plan create, owner update, and lifecycle
   transition, emitted inside the Plan transaction with the owner as the sole
   viewer.
2. A current-authority Plan projector that re-reads the owner-private Plan,
   checks the integer revision, and uses the existing index CAS/withdrawal/
   explicit-restore writers.
3. Pure and PostgreSQL tests for create/update/lifecycle, stale replay,
   withdrawal when the Plan is no longer readable, and explicit restoration.
4. Subscriber registration and worker repair coverage.

It must not include:

- a loose intention table or automatic Plan creation;
- shared Plan editing, grants, or arrangement participation;
- Plan relation fan-out unless the relation changes the canonical Plan
  revision and has a separately declared Life consequence;
- reader cutover, Atlas retirement, or a generalized owner framework.

## Contract changes required before coding

Before implementation, update the Life owner matrix for `plan` from
`supports_delta_delivery=False` to the exact private-owner capability that the
projector proves. Keep `availability=SHADOW_ONLY` until the shadow package and
its replay/withdrawal evidence land. The contract must state that viewer scope
is `[plan.owner_id]`; a client-supplied arbitrary viewer list is invalid.

The package should add a single graph producer module and a single Plan
projector. It should reuse the existing Life outbox, event envelope, current
graph projection, index writer, and worker rather than introduce a Plan-specific
queue or a second corpus.

## Exit condition

The Plan package is complete when an owner-private Plan can be created,
updated, transitioned, withdrawn, and explicitly restored in shadow storage;
stale events cannot overwrite a newer revision; worker repair delivers missed
events; and no shared or pre-Plan semantics were introduced. At that point the
team can make a deliberate Outcome decision with evidence from a second
integer-revision owner, rather than treating Plan as proof that social audience
semantics are solved.

