# Create Trip And Invite Group

## Purpose

The launch wedge is a real group trip. The first reliability requirement is
that an organizer can create a trip, invite people, and land everyone in the
same shared workspace without auth, schema, or mock drift surprises.

## Trace

```json
{
  "scenario": "create_trip_and_invite_group",
  "state_before": {
    "organizer": "signed-in or dev-bypass user",
    "trip": "none for this new plan",
    "invitees": "not yet members"
  },
  "action": "organizer creates a trip and sends an invite link",
  "tool_or_api_calls": [
    "POST /api/trips",
    "POST /api/trips/{trip_id}/invites",
    "GET /api/invites/{token}",
    "POST /api/invites/{token}/accept",
    "GET /api/trips/{trip_id}/members"
  ],
  "state_after": {
    "trip": "has stable id, title, destination shell, organizer membership",
    "invite": "has tokenized URL and active status",
    "member": "accepted invite attaches traveler to the correct trip",
    "app": "trip appears in mock or real trip list"
  }
}
```

## Invariants

- Trip creation returns a stable trip id and organizer role.
- Invite URLs contain only tokenized invite state, not private user facts.
- Accepting an invite is idempotent enough for retry-safe mobile UX.
- Active invites can be listed without leaking unrelated invites.
- Mock API supports create, view, accept, and list invite flows offline.

## Current Anchors

- `Travel App/__tests__/offline/goldenPath.test.ts`
- `Travel App/__tests__/screens/invite-landing.smoke.test.tsx`
- `Travel Agent/tests/api/test_invites_api.py`
- `Travel Agent/tests/api/test_invite_landing.py`
- `Travel Agent/tests/api/test_members_api.py`

## Gaps To Hunt

- Add a deterministic test for expired or consumed invite handling in the app.
- Add a mock/real parity assertion for invite answer visibility.
- Add a golden trace that verifies organizer role survives trip patching.

## Canary Readiness

This canary should not need a live LLM. Use live canary budget only if the
concierge is asked to explain or orchestrate invites conversationally.
