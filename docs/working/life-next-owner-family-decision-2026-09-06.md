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

## Execution result

The Plan recommendation is implemented as a shadow-only package in
`travel-agent` commits `7b6e97d7f` and `f12dca534`. Canonical owner-private Plan
create, update, and lifecycle mutations now journal Life changes; the Plan
projector re-reads current authority and proves integer-revision CAS,
withdrawal, stale replay, and explicit restoration. The focused combined
Life/Plan/Occasion suite passes 60 tests. Serving remains gated.

The first Outcome contract seam is now implemented as a pure audience resolver
and content-free event-envelope builder in `travel-agent` commits
`134bb021b`, `4ef82cce8`, and `9aa75ff3d`. It distinguishes owner-private Outcomes,
Occasion-scoped encounter Outcomes, and participant-scoped Commitment Outcomes;
it provides deterministic audience revisions, before/after viewer unions, and
withdrawal envelopes for erasure. The expanded focused suite passes 73 tests.
The two-token Life index CAS seam is now implemented in `travel-agent` commit
`66f378fc1`; the shadow Outcome consumer is `ba9463c2a`; and direct Occasion
join/leave encounter repair is `fd66f9f1f`. These packages do not change the
Together reader or enable Life serving. Account-erasure withdrawal and
surviving encounter-audience repair are now implemented in `329060a88`, and
Commitment-participant audience repair is implemented in `afb13c6fa`; the
focused run includes the PostgreSQL proofs for both scopes. No current
reconciler mutates either audience set; broader race coverage is the next
gate.

## Recommendation

Keep **existing owner-private Plans** as the completed bounded owner-family
proof, then continue Outcome shadow hardening. Do not implement loose pre-Plan
intention, shared arrangement material, or a Life serving cutover in this
package.

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

## Why Outcome required a separate package

Outcome is not merely another private integer-revision row:

- `personal_outcomes.visibility` can be `shared`.
- Shared visibility may be authorized through an Occasion or through a shared
  Commitment's participant set.
- The current graph reader has separate authorization paths for owner-private,
  Occasion-shared, and Commitment-participant outcomes.
- Owner deletion, Occasion departure, Commitment participant changes, and
  outcome visibility corrections would need an explicit before/after viewer
  union and withdrawal/restore contract.

The existing owner matrix correctly keeps Outcome shadow-only. The audience
contract, two-token CAS, direct Occasion repair, and account-erasure repair
for both encounter and Commitment Outcomes are now designed and tested;
cross-viewer comparison and broader race coverage must land before any
`supports_delta_delivery` change. Do not solve it by
broadcasting every graph viewer or by letting Life infer grants from a
presentation record.

## Plan package boundary (landed)

The landed Plan package includes only:

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

## Contract changes made

The Life owner matrix now declares Plan `supports_delta_delivery=True` and
`supports_audience_rechecks=True` while retaining `availability=SHADOW_ONLY`.
The projector enforces viewer scope as exactly one owner-private viewer; a
client-supplied arbitrary viewer list is invalid.

The package adds a single graph producer module and a single Plan projector. It
reuses the existing Life outbox, event envelope, current graph projection,
index writer, and worker rather than introducing a Plan-specific queue or a
second corpus.

## Plan exit condition

The Plan package is complete for shadow delivery: an owner-private Plan can be
created, updated, transitioned, withdrawn, and explicitly restored in shadow
storage; stale events cannot overwrite a newer revision; worker repair
delivers missed events; and no shared or pre-Plan semantics were introduced.
Outcome now has a shadow proof beyond Plan, including account-erasure repair
for both audience shapes, but Plan remains only an owner-private comparison
point. The next exit condition is cross-viewer shadow comparison plus broader
race coverage; no reader cutover follows automatically. Any future
reconciliation writer must reuse the accepted audience-repair helpers.
