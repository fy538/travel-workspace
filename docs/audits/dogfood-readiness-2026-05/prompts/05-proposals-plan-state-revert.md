# Prompt 05 — Proposals, Voting, Plan State, And Revert

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Proposal lifecycle, voting, apply/revert, plan_events ledger, Plan state read model.

Output:
docs/audits/dogfood-readiness-2026-05/areas/05-proposals-plan-state-revert.md

Product promise:
Vesper edits shared trip artifacts through visible, reviewable proposals. Users can approve, reject, understand, and revert changes without Home/Plan/Map drifting.

Inspect:
- Travel Agent proposal routes, apply/revert logic, plan_events, idempotency, delegation/autonomy checks.
- Plan state API and affected block IDs.
- Travel App ProposalReviewSheet, voting cards, plan timeline, chat change receipts, cache invalidation.

Start with:
- docs/reliability/traces/proposal-review-and-plan-mutation.md
- Travel Agent/docs/product/Product Vision and Scope.md section "Advise -> Propose -> Act"
- Travel Agent/tests/api/test_proposals_api.py
- Travel Agent/tests/api/test_proposal_apply.py
- Travel Agent/tests/api/test_plan_state.py
- Travel App/docs/page-specs/change-proposals.md

Audit questions:
1. Can proposal apply partially mutate state and report success?
2. Is revert actually reverting status and plan changes, not just UI labels?
3. Are retries/idempotency handled for accept/reject/apply?
4. Does delegation consent gate auto-approve paths?
5. Are affected blocks, recent changes, and conflicts visible to app surfaces?
6. Does frontend invalidate proposal/chat/itinerary/map/plan-state together?
7. Can mock mode assert a success path that real mode cannot support?

Run if cheap:
- make contract-check
- targeted proposal/plan-state backend tests
- targeted frontend proposal tests

Deliver:
Prioritize trust-loop breaks: invisible mutation, irreversible action, wrong apply status, stale Plan/Map after accept/reject.
```

