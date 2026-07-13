---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the executable IR-11 atomic compound-operation contract, exit evidence, and IR-12 handoff.
source_of_truth_for: [itinerary-redesign-ir11-compound-operation-evidence]
---

# IR-11 — Atomic compound-operation evidence

IR-11 extends the accepted operation, proposal, history, and provider spine. It
does not add a frontend surface or begin IR-12. Optimize Day, Replan, and
parallel topology changes now share the same preview, policy, transaction,
operation identity, terminal evidence, idempotency, and recovery boundaries as
the existing canonical operations.

## Ordered Optimize/Replan contract

- Optimize Day and Replan contain an ordered list of validated atomic child
  operations. The parent compound precondition must exactly repeat those child
  preconditions in order.
- Each child is resolved against its own target, revision, scope, owner,
  participants, and protected dependencies. A denied child denies the parent;
  proposal children must converge on one decision owner.
- Duplicate block targets and child proposal/provider/compound wrappers are
  rejected by the normalized contract.
- Commit executes the ordered children inside one database transaction and
  stores one parent operation with two terminal-history transitions. Stable,
  deterministic child identities exist only inside the parent mutation
  evidence; they do not create independently landed ledger operations.
- A fault after any child rolls back all plan mutations and all operation
  evidence. An identical successful replay returns the original landed result.

## Explicit parallel topology

- A branch group stores its creating operation, day, organizer topology owner,
  split anchor, rejoin anchor, and revision.
- Each stable branch stores a decision owner. Explicit branch-participation rows
  define its planned participants; database triggers require current trip
  membership, require the owner to participate, and require the topology owner
  to remain an organizer at every write.
- Create and update lock the group, branches, affected day blocks, block
  participation, and branch participation before mutation. Blocks cannot be
  silently stolen from another branch group.
- Updating a topology preserves supplied branch IDs. A block removed from the
  branch set truthfully rejoins the main whole-group plan under the organizer,
  with planned participation reset to current trip members.
- The committed evidence contains before/after group, branch, branch
  participation, and block snapshots. A fault after topology mutation rolls
  back the group, branches, assignments, participation, and root operation.

## Authority and recovery

Preview and commit re-resolve every child using current governance and owner
facts. The executable proof changes Open governance to Review after preview:
commit rejects the stale authority path as proposal-required, preserves the
exact normalized parent draft, and lands no child.

Compound and branch history never advertise a partial child Undo. The truthful
recovery is one `review_revert` action; if current authority is absent, history
still reports Review rather than claiming executable reversal. Denied drafts
remain a new-change path.

## Rollout boundary

The existing global preview and commit gates remain required. Branch writes,
Optimize Day, and Replan additionally require independent default-off gates:

- `ITINERARY_BRANCHES_V2`
- `ITINERARY_OP_OPTIMIZE_DAY_V2`
- `ITINERARY_OP_REPLAN_V2`

No travel-app component, generated client, target-shell route, or UI contract is
changed by IR-11. UI adoption remains with IR-13, IR-15, and IR-16.

## IR-12 handoff

IR-12 can project compound and branch truth without reconstructing intent from
individual block diffs:

- the parent operation and ordered child evidence provide one landed/history
  identity and one recovery state;
- branch group and branch revisions provide versioned topology identities;
- explicit branch owners and participant rows provide viewer-scoped branch
  membership;
- block `branch_id`, canonical scope/owner, and planned participation provide
  the shared List/Map substrate; and
- split/rejoin anchors and stable branch IDs support the same typed graph in
  Plan State, Map parity, Details State, and Changes/History.

IR-12 must keep this compound identity intact. It must not emit children as
independent recent changes or infer branch membership from legacy participant
arrays.

## Verification

- Fresh PostgreSQL upgrade from an empty database through `ir11a001` passed.
- `ir11a001 -> ir10a001 -> ir11a001` passed.
- Atomic fault, successful commit, idempotent replay, governance re-resolution,
  explicit topology, stable update, and main-plan rejoin proofs passed.
- Final focused IR-07–IR-11 API, operation, preview, commit, proposal, history,
  provider, schema, flag, and telemetry suite: 155 tests passed.
- Ruff and `git diff --check` pass on the backend slice.
