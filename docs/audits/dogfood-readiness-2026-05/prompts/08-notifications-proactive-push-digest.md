# Prompt 08 — Notifications, Proactive Help, Push, And Digest

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Notifications, proactive turns, push routing, quiet hours, daily digest.

Output:
docs/audits/dogfood-readiness-2026-05/areas/08-notifications-proactive-push-digest.md

Product promise:
Vesper can nudge usefully without becoming noisy, violating notification preferences, or exposing private context in group/public channels.

Inspect:
- Travel Agent notification gates, triage, dispatch, digest, notification_state, push device registration, proactive concierge turns.
- Travel App notification feed, read state, tap routing, badge counts, device token lifecycle, push deep links.

Start with:
- docs/reliability/traces/notifications-and-proactive-help.md
- Travel Agent/backend/notifications/FEATURE.md
- Travel Agent/backend/digest/FEATURE.md
- Travel Agent/tests/notifications/
- Travel Agent/tests/api/test_notification_outcomes.py
- Travel App/__tests__/data/notifications.test.ts

Audit questions:
1. Are pause_all, quiet hours, daily caps, and per-user/per-trip cooldowns respected?
2. Can private proactive turns land in group chat, notifications, home cards, or digest?
3. Are push notifications idempotent enough to avoid duplicate sends?
4. Does member removal clear notification state and device targeting?
5. Do notification taps route to an existing trip/surface after cold launch?
6. Are read/unread counts consistent across backend and app?
7. Does digest generation have safe fallbacks when LLM/provider paths fail?

Run if cheap:
- targeted notification tests
- targeted frontend notification tests
- make mock-real-parity

Deliver:
Focus on noisy, private, duplicate, or misrouted notifications during a real dogfood trip.
```

