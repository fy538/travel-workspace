# Area Audit: Proposal Lifecycle, Plan State, Apply/Revert

Date: 2026-05-21  
Agent: Cursor Cloud / Codex audit session  
Scope: Proposal routes, proposal apply/revert logic, plan_events ledger, Plan state read model, ProposalReviewSheet, voting cards/hooks, mock proposal API, invalidation helpers, proposal docs/tests.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: Accepted proposals can still be reported as applied when the apply helper forks a new itinerary version but applies zero block mutations.
- Checks run: `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; targeted backend proposal/plan-state tests -> pass; targeted frontend proposal tests -> pass; `make golden-path-qa` -> pass.
- Residual uncertainty: I did not run a live Postgres end-to-end accept/revert sequence; the findings below are static/control-flow confirmed and should get small regression tests.

## Findings

### P1 — Apply can succeed after zero proposal mutations

Status: Confirmed  
User impact: A tester accepts a stale or malformed proposal, sees "Applied to Plan", but the intended block time/venue/title did not change. The backend may still fork an itinerary version, making the ledger look busy while the artifact truth is unchanged.  
Product promise affected: proposal trust loop / plan coherence

References:

- `Travel Agent/backend/core/db/proposal_apply.py:191` — maps proposal `affected_block_ids` to the forked version.
- `Travel Agent/backend/core/db/proposal_apply.py:200` — falls back to title/entity matching when affected IDs do not resolve.
- `Travel Agent/backend/core/db/proposal_apply.py:250` — apply helpers can run with an empty `affected_new_ids` list.
- `Travel Agent/backend/core/db/proposal_apply.py:266` — computes `affected_summary`, but does not fail when it is zero.
- `Travel Agent/backend/core/db/proposal_apply.py:332` — returns `new_version` unconditionally after the apply attempt.
- `Travel Agent/backend/api/routes/proposals.py:401` — route treats any non-`None` version as `apply_status="succeeded"`.

Why it matters:

This is the exact "accepted means Plan changed" trust boundary. The current code distinguishes `None` and exceptions, but not "forked successfully, changed nothing." Stale proposal IDs are plausible after intervening itinerary forks; `plan_state.py` has a forward-chain reader for that case, but `apply_accepted_proposal()` does not use it.

Repro or deterministic test idea:

1. Build an accepted `reschedule` or `modify` proposal whose `affected_block_ids` do not exist in the current itinerary and whose title fallback does not match any current block.
2. Mock `fork_itinerary_version()` and `get_full_itinerary()` to return valid original/forked itineraries.
3. Assert `update_block()` is not called.
4. Expected: `apply_accepted_proposal()` returns `None` or marks `apply_status="failed"`.
5. Current likely/observed: returns the new itinerary version, so the route writes `apply_status="succeeded"`.

Suggested fix direction:

Have `apply_accepted_proposal()` compute a concrete mutation count and return failure when non-add proposals affect zero blocks, or when add proposals create zero blocks. Consider reusing the plan-state forward-chain logic before title fallback so old proposal IDs can resolve across intervening forks.

Related bug class:

Invisible mutation / wrong apply status / stale block-id drift

Confidence: High

### P1 — Revert reports success even when no revert was performed

Status: Confirmed  
User impact: An organizer taps revert, the proposal becomes `withdrawn`/reverted, and Plan recent changes can say the change was reverted even if the backend could not restore anything.  
Product promise affected: reversibility / proposal trust loop

References:

- `Travel Agent/backend/core/db/proposal_apply.py:888` — version-restore fallback returns `None` when the trip has fewer than two itinerary versions.
- `Travel Agent/backend/core/db/proposal_apply.py:843` — revert can also return `None` when the proposal cannot be loaded or restored.
- `Travel Agent/backend/api/routes/proposals.py:509` — route calls `revert_accepted_proposal_v2()`.
- `Travel Agent/backend/api/routes/proposals.py:512` — `None` is converted into `revert_mode="version_restore"`.
- `Travel Agent/backend/api/routes/proposals.py:520` — proposal metadata is marked `was_reverted=True`.
- `Travel Agent/backend/api/routes/proposals.py:535` — proposal status is moved from `accepted` to `withdrawn`.

Why it matters:

`revert_accepted_proposal_v2()` documents `None` as "couldn't be reverted at all" for cases like no prior version. The route currently treats that as a successful version restore and flips the proposal lifecycle. This breaks the psychological safety promise of undo.

Repro or deterministic test idea:

1. Patch `get_change_proposal()` to return an accepted proposal.
2. Patch `revert_accepted_proposal_v2()` to return `None`.
3. POST `/api/trips/{trip_id}/proposals/{proposal_id}/revert`.
4. Expected: 409 or `revert_failed`/no status transition.
5. Current likely/observed: route proceeds to metadata patch and `withdrawn`.

Suggested fix direction:

Treat `None` from `revert_accepted_proposal_v2()` as a failed revert. Preserve `status="accepted"` and return a conflict/error payload the app can render as "Could not revert safely."

Related bug class:

Irreversible action mislabeled as reversible

Confidence: High

### P1 — Retrying accept without an idempotency header can apply twice

Status: Confirmed  
User impact: A slow-network retry or double tap on "Accept change" can fork/apply the same accepted proposal again. For add proposals, this risks duplicate itinerary blocks; for modify/reschedule, it can create duplicate version churn and duplicate receipts.  
Product promise affected: idempotency / plan coherence

References:

- `Travel Agent/backend/core/db/change_proposals.py:260` — `resolve_proposal()` only updates rows matching `from_status=("open",)`.
- `Travel Agent/backend/core/db/change_proposals.py:314` — when no row matches, it returns the existing proposal instead of signaling "already resolved."
- `Travel Agent/backend/api/routes/proposals.py:351` — route has an idempotency guard only when `X-Idempotency-Key` is present.
- `Travel Agent/backend/api/routes/proposals.py:381` — any returned proposal plus `body.status=="accepted"` runs apply side effects.
- `Travel App/utils/api/http.ts:790` — `resolveProposal()` does not accept or send an idempotency key.
- `Travel App/components/trip/ProposalReviewSheet.tsx:224` — organizer accept calls `api.resolveProposal()` with only `{ status }`.

Why it matters:

The API advertises retry safety, but the default frontend path does not send the header. The backend should still be side-effect safe once a proposal has already left `open`; returning the existing accepted row and then re-running apply is the unsafe part.

Repro or deterministic test idea:

1. Mock `backend.core.db.change_proposals.resolve_proposal()` to return an already-accepted proposal on a second call.
2. Call the route twice without `X-Idempotency-Key`.
3. Expected: second call returns existing detail without invoking `apply_accepted_proposal()`.
4. Current likely/observed: second call invokes `apply_accepted_proposal()` again.

Suggested fix direction:

Have the route detect whether the DB transition actually happened, or have `resolve_proposal()` return a transition result rather than the existing row on stale status. Also thread stable idempotency keys through `voteOnProposal`, `resolveProposal`, and `revertProposal` from the app.

Related bug class:

Retry/idempotency side-effect duplication

Confidence: High

### P2 — Delegation downgrade can create a non-resolving voting flow when trip voting is off

Status: Confirmed  
User impact: If a member has `group_proposals="ask"` and Vesper chooses `auto_approve` on a trip with voting disabled, the backend downgrades to `lazy_consensus` after the voting-enabled gate has already run. It can then post a vote widget even though voting is off, and deadline automation will not resolve it.  
Product promise affected: delegation consent / proposal lifecycle clarity

References:

- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:124` — rejects lazy/active modes when `trips.voting_enabled` is false.
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:150` — later downgrades `auto_approve` to `lazy_consensus` when any member requires explicit ask.
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:171` — adds a deadline to the downgraded proposal.
- `Travel Agent/backend/concierge/tool_handlers/planning/_propose_present.py:341` — posts a vote widget for lazy/active modes.
- `Travel Agent/backend/core/db/change_proposals.py:387` — deadline auto-resolution only fetches proposals for trips where `voting_enabled` is true.
- `Travel App/components/trip/ProposalReviewSheet.tsx:739` — detail UI says voting is off and organizer must resolve manually.

Why it matters:

The consent gate correctly prevents silent auto-apply, but the fallback path lands in a lifecycle the trip has not enabled. Users may see contradictory surfaces: a group vote widget exists, but proposal detail says voting is off and cron will never resolve by the deadline.

Repro or deterministic test idea:

1. Create a trip with `voting_enabled=false`.
2. Set one member's delegation preference to `group_proposals="ask"`.
3. Call `propose_change` with `approval_mode="auto_approve"`.
4. Expected: create an organizer-only open proposal, return an explicit "organizer must resolve" result, or reject with instructions.
5. Current likely/observed: `approval_mode` becomes `lazy_consensus`, a vote widget is posted, and deadline automation ignores it.

Suggested fix direction:

After delegation downgrade, re-run the voting-enabled gate. For voting-disabled trips, use an explicit organizer-only proposal mode/copy instead of lazy consensus, or return a tool error telling the agent to ask the organizer.

Related bug class:

Delegation consent / lifecycle dead-end / mock-real drift risk

Confidence: High

### P2 — Proposal detail shows stale affected block IDs after itinerary forks

Status: Confirmed  
User impact: A tester opens a proposal from Plan, but the review sheet cannot name the affected block after an intervening apply fork. Plan inline state can point at the right current block, while the proposal detail says the IDs will match once the live plan loads.  
Product promise affected: affected blocks visibility / plan coherence

References:

- `Travel Agent/backend/api/routes/proposals.py:637` — proposal detail returns raw `proposal.affected_block_ids`.
- `Travel Agent/backend/core/db/plan_state.py:371` — Plan state has helper logic to resolve old affected IDs to current block IDs.
- `Travel Agent/backend/core/db/plan_state.py:830` — open decisions use translated current IDs.
- `Travel App/components/trip/ProposalReviewSheet.tsx:162` — sheet builds a set from raw proposal detail IDs.
- `Travel App/components/trip/ProposalReviewSheet.tsx:167` — sheet matches raw IDs against current itinerary blocks.
- `Travel App/components/trip/ProposalReviewSheet.tsx:401` — fallback copy claims IDs will match once the live plan is loaded.

Why it matters:

The backend already solved this for Plan state, but the proposal detail surface still uses the stale IDs. The inspectable artifact should be where the user understands what changes; this makes the detail sheet less trustworthy precisely when concurrent proposal churn happens.

Repro or deterministic test idea:

1. Create proposal A against block v1.
2. Accept proposal B so the itinerary forks and block v1 becomes v2.
3. Open proposal A detail from Plan.
4. Expected: sheet shows the current affected block/day.
5. Current likely/observed: Plan inline can show it, but `ProposalReviewSheet` cannot match raw v1 IDs to current itinerary blocks.

Suggested fix direction:

Expose translated affected block IDs in `ProposalDetail`, or have `ProposalReviewSheet` read the matching `open_decisions` entry from plan-state and use those current IDs for block matching.

Related bug class:

Sibling inconsistency / stale identifier read model

Confidence: High

## Non-Findings / Things Ruled Out

- Backend proposal route tests, apply tests, plan-state tests, diff-safe revert tests, and plan_events tests all pass in the targeted run.
- Plan-state now distinguishes `proposal_apply_failed`, `proposal_reverted`, and `proposal_accepted`; this is covered in `Travel Agent/tests/api/test_plan_state.py`.
- Frontend invalidation after ProposalReviewSheet vote/resolve/revert includes proposal list/detail, group chat, itinerary, map-state, plan-state, and home cards via `invalidateTripReadModels()`.
- Chat vote handlers invalidate Plan/Home/Map read models after votes, so the older "chat votes do not update Plan v2" gap appears closed.
- OpenAPI snapshot, generated frontend types, API coverage, mock-real parity, and golden-path QA are all green.

## Suggested Follow-Up Checks

- Add a backend regression test where `apply_accepted_proposal()` resolves zero current blocks and must mark apply failed.
- Add a backend route test where `revert_accepted_proposal_v2()` returns `None` and the route must not mark the proposal reverted.
- Add a backend route test for duplicate accept without `X-Idempotency-Key` proving apply side effects run at most once.
- Add a frontend/API test that proposal accept/reject/vote/revert calls send stable `X-Idempotency-Key` values.
- Add a ProposalReviewSheet test using plan-state translated IDs after a fork so the affected block still renders by name.
