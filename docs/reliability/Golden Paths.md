# Golden Paths

These are the MVP journeys that reliability work should protect first. Each
journey should have deterministic tests, offline traces, or both before it
graduates to live LLM canaries.

## 1. Create Trip And Invite Group

User story: an organizer creates a trip, invites people, and sees the trip
become a shared workspace.

Invariants:

- Creating a trip returns a stable trip id and organizer membership.
- Invite creation returns a tokenized link without exposing hidden user data.
- Accepting an invite attaches the traveler to the correct trip.
- The app can render the trip from mock mode without backend calls.

Current offline anchors:

- `Travel App/__tests__/offline/goldenPath.test.ts`
- `Travel App/__tests__/screens/invite-landing.smoke.test.tsx`
- `Travel Agent/tests/api/test_invites_api.py`
- `Travel Agent/tests/api/test_invite_landing.py`

## 2. Private Input To Group-Safe Context

User story: each traveler can share private tastes or constraints and the
concierge can use them without leaking them to the group.

Invariants:

- Private facts are scoped to the owner unless explicitly shareable.
- Group-facing copy omits private leak phrases.
- Privacy audit surfaces what was used and why.
- Preference synthesis can run against fakes in offline tests.

Current offline anchors:

- `Travel Agent/tests/eval/test_concierge_checks.py`
- `Travel Agent/tests/eval/test_planning_checks.py`
- `Travel Agent/tests/eval/test_restaurant_checks.py`
- `Travel App/__tests__/data/privacy.test.ts`
- `Travel App/__tests__/screens/privacy-audit.smoke.test.tsx`

## 3. Proposal Review And Plan Mutation

User story: Vesper proposes a change, the group can vote or resolve it, and the
accepted change is visible instead of silently mutating the plan.

Invariants:

- Proposals have a status, reason, affected ids, and resolution path.
- Voting and resolution are idempotent enough for retries.
- Accepted or rejected proposals produce visible recent-change state.
- Plan v2 exposes open decisions on affected blocks.

Current offline anchors:

- `Travel Agent/tests/api/test_proposals_api.py`
- `Travel Agent/tests/api/test_proposal_apply.py`
- `Travel Agent/tests/api/test_plan_state.py`
- `Travel App/__tests__/data/proposals.test.ts`
- `Travel App/__tests__/components/plan/ProposalReviewSheet.test.tsx`

## 4. Home, Plan, And Map Coherence

User story: the same trip state appears consistently across the dashboard,
plan timeline, and map.

Invariants:

- Home cards, Plan blocks, and Map pins reference compatible trip/block ids.
- Plan state exposes commitment, open decisions, and recent changes.
- Map state can render placed and unplaced items without crashing.
- Dismissed cards do not erase Tier 1 critical trip state.

Current offline anchors:

- `Travel Agent/tests/api/test_home.py`
- `Travel Agent/tests/api/test_home_group_state.py`
- `Travel Agent/tests/api/test_trips_api.py`
- `Travel App/__tests__/data/planState.test.ts`
- `Travel App/__tests__/utils/tripMapStateParity.test.ts`
- `Travel App/__tests__/screens/plan.smoke.test.tsx`
- `Travel App/__tests__/screens/map.smoke.test.tsx`

## 5. Notifications And Proactive Help

User story: the concierge can nudge at useful moments without becoming noisy or
exposing private context.

Invariants:

- Notification preferences and cadence overrides are respected.
- Proposal-deadline nudges only reference visible proposal state.
- Channel dispatch can be tested without sending real SMS, push, or email.
- The app can route notification taps into the right trip surface.

Current offline anchors:

- `Travel Agent/tests/notifications/`
- `Travel Agent/tests/api/test_notification_outcomes.py`
- `Travel App/__tests__/data/notifications.test.ts`
- `Travel App/__tests__/screens/notifications.smoke.test.tsx`
- `Travel App/__tests__/screens/notifications.routing.test.tsx`

## 6. Memory And Post-Trip Loop

User story: the trip leaves behind useful memory without feeling creepy or
unreviewable.

Invariants:

- Captured trip moments create observations with source metadata.
- Personal memory is inspectable from the app.
- Post-trip character read can be generated from deterministic inputs.
- Users can understand or retire remembered facts.

Current offline anchors:

- `Travel Agent/tests/tasks/test_post_trip_character_read.py`
- `Travel Agent/tests/api/test_trips_debrief.py`
- `Travel App/__tests__/data/memory.test.ts`
- `Travel App/__tests__/screens/personal-memory.smoke.test.tsx`

## Offline Trace Shape

Use this structure when asking Codex or Claude Code to trace a journey:

```json
{
  "scenario": "proposal_review_and_plan_mutation",
  "state_before": "Open trip with itinerary block and private constraints",
  "action": "Concierge proposes swapping dinner",
  "tool_or_api_calls": [
    "create_change_proposal",
    "get_trip_plan_state",
    "get_trip_map_state"
  ],
  "state_after": "Open proposal visible in Plan and Home; Map still renders",
  "invariants": [
    "group copy omits private constraints",
    "affected block exposes open_decision_ids",
    "proposal can be accepted or rejected offline"
  ]
}
```

## Promotion Rule

A journey is ready for a live canary only when:

- The relevant contract check is green.
- Backend or frontend deterministic tests cover the main invariant.
- Mock mode covers the user-facing path.
- The live canary has a clear pass/fail rubric before it runs.

## Trace Files

- [Create Trip And Invite Group](./traces/create-trip-and-invite-group.md)
- [Private Input To Group-Safe Context](./traces/private-input-to-group-safe-context.md)
- [Proposal Review And Plan Mutation](./traces/proposal-review-and-plan-mutation.md)
- [Home, Plan, And Map Coherence](./traces/home-plan-map-coherence.md)
- [Notifications And Proactive Help](./traces/notifications-and-proactive-help.md)
- [Memory And Post-Trip Loop](./traces/memory-and-post-trip-loop.md)
