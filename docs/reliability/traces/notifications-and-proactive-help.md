# Notifications And Proactive Help

## Purpose

Vesper should nudge at useful moments without feeling noisy, creepy, or stale.
Notifications must respect cadence and channel settings, point to visible trip
state, and avoid private context leaks.

## Trace

```json
{
  "scenario": "notifications_and_proactive_help",
  "state_before": {
    "trip": "active or pre-trip shared workspace",
    "preferences": "user-level and trip-level notification settings",
    "pending_items": "unread messages, votes, invite answers, or proactive cards"
  },
  "action": "system generates or fetches notification feed",
  "tool_or_api_calls": [
    "notification gates",
    "notification triage",
    "GET /api/users/{user_id}/notifications",
    "POST /api/notifications/{outcome_id}/mark-read"
  ],
  "state_after": {
    "feed": "items are sorted newest first and route to the right surface",
    "cadence": "quiet hours and pause settings are respected",
    "privacy": "copy references only group-visible state",
    "outcomes": "engagement can be recorded without duplicate sends"
  }
}
```

## Invariants

- Notification preferences and trip cadence overrides must gate non-critical
  sends.
- Proposal nudges must reference visible proposal state, not hidden reasoning.
- Channel dispatch can be tested without sending real SMS, push, or email.
- Feed items need stable ids so refetches do not create duplicate UI rows.
- Tap targets should route to the surface where the user can act.

## Current Anchors

- `Travel Agent/tests/notifications/`
- `Travel Agent/tests/api/test_notification_outcomes.py`
- `Travel Agent/tests/api/test_home.py`
- `Travel App/__tests__/data/notifications.test.ts`
- `Travel App/__tests__/screens/notifications.smoke.test.tsx`
- `Travel App/__tests__/screens/notifications.routing.test.tsx`

## Gaps To Hunt

- Add a deterministic test for quiet-hours behavior across in-app versus push.
- Add an app routing assertion for proposal-deadline notifications.
- Add a privacy fixture for proactive copy generated from private context.

## Canary Readiness

Live canaries should be rare here. Prefer deterministic tests with fake channel
providers. A live canary is only useful for the quality of proactive wording,
and it should never send a real external notification.
