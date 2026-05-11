# Proposal Review And Plan Mutation

## Purpose

The concierge should not silently mutate a group trip. Proposed changes should
be visible, reviewable, resolvable, and reflected consistently across Plan,
Home, and Map.

## Trace

```json
{
  "scenario": "proposal_review_and_plan_mutation",
  "state_before": {
    "trip": "shared group trip with organizer and members",
    "plan": "at least one itinerary block exists",
    "decision_state": "no accepted mutation yet",
    "privacy_state": "private traveler constraints may exist"
  },
  "action": "concierge proposes a dinner swap or timing change",
  "tool_or_api_calls": [
    "create_change_proposal",
    "GET /api/trips/{trip_id}/proposals",
    "GET /api/trips/{trip_id}/plan-state",
    "GET /api/trips/{trip_id}/home_cards",
    "GET /api/trips/{trip_id}/map-state"
  ],
  "state_after_open": {
    "proposal": "open decision has title, reason, affected_block_ids, impact, votes",
    "plan": "affected blocks expose open_decision_ids and has_open_proposal flag",
    "home": "active zone can surface pending_decision card",
    "map": "existing pins/routes still render"
  },
  "state_after_resolution": {
    "accepted": "recent_changes includes proposal_accepted and block state updates",
    "rejected": "recent_changes includes proposal_rejected without mutating plan",
    "revert": "revert path is explicit when supported"
  }
}
```

## Invariants

- A proposed trip change must create a durable proposal record before changing
  group-visible plan state.
- Open proposals must have a status, proposal type, title, description,
  affected ids, created timestamp, and approval mode.
- Plan v2 must expose open decisions on affected blocks.
- Resolution must be visible as recent change state.
- Rejected proposals must not mutate itinerary blocks.
- Group-facing proposal copy must not expose private constraint phrases.

## Current Anchors

- `Travel Agent/tests/api/test_proposals_api.py`
- `Travel Agent/tests/api/test_proposal_apply.py`
- `Travel Agent/tests/api/test_plan_state.py`
- `Travel Agent/tests/concierge/test_change_proposals.py`
- `Travel App/__tests__/data/proposals.test.ts`
- `Travel App/__tests__/components/plan/ProposalReviewSheet.test.tsx`
- `Travel App/__tests__/data/planState.test.ts`
- `Travel App/__tests__/screens/plan.smoke.test.tsx`

## Gaps To Hunt

- Add a cross-surface deterministic assertion that an open proposal id appears
  in both proposal list data and Plan v2 `open_decision_ids`.
- Add a negative privacy fixture with a private phrase that may appear in
  reasoning but must not appear in group-facing proposal copy.
- Add a Map assertion that proposal churn does not drop unrelated placed pins.

## Canary Readiness

Run a live canary only after `make golden-path-qa` is green. The live canary
should ask the concierge to propose one low-risk plan change, then verify that
the response points the group toward review rather than silently claiming the
trip has changed.
