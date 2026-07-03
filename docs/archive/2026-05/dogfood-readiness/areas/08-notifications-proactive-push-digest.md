# Area Audit: Notifications, Proactive Turns, Push Routing, Quiet Hours, Daily Digest

Date: 2026-05-21  
Agent: Codex dogfood-readiness audit  
Scope: `Travel Agent/backend/notifications/`, `Travel Agent/backend/digest/`, notification/feed/preferences/device routes, targeted notification tests, `Travel App/data/notifications.ts`, `Travel App/components/auth/PushRegistrar.tsx`, `Travel App/app/notifications/index.tsx`, push utilities/tests, reliability docs.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: private group-interjection decisions are encoded with `target`, but the proactive routing layer only honors `target_audience`, so a private re-engagement turn can be persisted to the group conversation.
- Checks run: `PYTHONPATH=. pytest tests/notifications/test_gates.py tests/notifications/test_push.py tests/notifications/test_state_updater.py tests/notifications/test_group_interjection.py tests/api/test_notification_outcomes.py -q` -> pass, 97 passed
- Checks run: `npm test -- --runTestsByPath __tests__/data/notifications.test.ts __tests__/screens/notifications.routing.test.tsx __tests__/utils/push.test.ts --runInBand` -> pass, 28 passed
- Checks run: `make mock-real-parity` -> pass
- Residual uncertainty: no live Expo/APNs/FCM push, live LLM, provider API, or Postgres concurrency repro was run.

## Findings

### P1 — Private Group-Interjection Targets Fall Back To Group Chat

Status: Confirmed  
User impact: A quiet traveler can be privately nudged by triage, but the resulting proactive Sonnet turn is routed through the shared trip conversation, potentially exposing private preference/social context to the group.  
Product promise affected: privacy / concierge trust

References:

- `Travel Agent/backend/notifications/prompts.py:201` — group-interjection triage is explicitly allowed to choose a private target for one member.
- `Travel Agent/backend/notifications/group_interjection.py:524` — `_fire_interjection()` builds `triage_metadata`.
- `Travel Agent/backend/notifications/group_interjection.py:529` — metadata uses `"target": decision.target`, not `"target_audience"`.
- `Travel Agent/backend/concierge/triggers.py:67` — private proactive turns must not persist into the shared group conversation.
- `Travel Agent/backend/concierge/triggers.py:75` — routing only checks `triage_metadata["target_audience"]`.

Why it matters:

This is the highest-risk notification bug for dogfood because it hits the exact private-to-group boundary the product is built around. The prompt encourages private interjection when one person should be re-engaged without being put on the spot, but the execution layer cannot see that private intent.

Repro or deterministic test idea:

1. Unit-test `_fire_interjection()` with `InterjectionDecision(target="private", target_user_id=<member>)`.
2. Patch `run_proactive_turn` and assert it receives `triage_metadata["target_audience"] == "private"`.
3. Add an integration-style test around `run_proactive_turn()` that asserts private metadata calls `get_or_create_session_for_personal_trip()`, not `get_or_create_session_for_trip()`.
4. Current likely/observed: metadata carries `target`, so `run_proactive_turn()` treats it as group.

Suggested fix direction:

Normalize group-interjection metadata to the same contract as notification triage: `target_audience`, `target_user_id`, `conversation_id`, and `channels` if needed. Add a regression test that fails when private interjection metadata can fall back to group routing.

Related bug class:

private-data leak / sibling contract drift

Confidence: High

### P1 — Proactive Push/In-App Taps Lack A Reliable Conversation Target

Status: Confirmed  
User impact: A user tapping a proactive notification can land nowhere from an OS push, or land in the group trip chat from the in-app feed even when the proactive turn was private and stored in a personal trip conversation.  
Product promise affected: push routing / concierge trust / privacy

References:

- `Travel Agent/backend/concierge/session.py:733` — proactive side effects read target metadata.
- `Travel Agent/backend/concierge/session.py:738` — `record_notification_dispatch()` is called without `self.conversation_id`.
- `Travel Agent/backend/notifications/state_updater.py:51` — `on_notification_sent()` can accept a `conversation_id`.
- `Travel Agent/backend/notifications/state_updater.py:145` — private dispatch calls `on_notification_sent()` without passing any conversation id.
- `Travel Agent/backend/notifications/channel_dispatch.py:449` — Expo push payload includes `conversation_id` only if metadata has it.
- `Travel App/components/auth/PushRegistrar.tsx:116` — tap routing only handles generic concierge pushes when `conversation_id` is present.
- `Travel App/app/notifications/index.tsx:217` — in-app proactive trip notifications always route to `routes.tripChat(trip_id)`.

Why it matters:

During a real trip, proactive turns are only useful if the tap lands where the message exists. Private proactive turns should open the personal trip conversation; group turns should open the group trip chat or a concrete action surface. Today the backend drops the conversation id before delivery, while the app assumes every proactive trip notification belongs in group chat.

Repro or deterministic test idea:

1. Create a proactive private turn in a personal trip session with push channel selected.
2. Inspect the resulting `notification_deliveries.metadata_` and Expo payload: expected `conversation_id` for the personal conversation.
3. Simulate `subscribeToNotificationTaps()` with `{ outcome_id, trip_id, conversation_id: null, intent: "side_quest" }`.
4. Expected: navigates to the existing conversation or a safe trip activity surface.
5. Current likely/observed: OS tap has no matching route branch; in-app row opens group trip chat.

Suggested fix direction:

Thread `self.conversation_id` through `record_notification_dispatch()` into `on_notification_sent()` metadata. Extend app notification types to preserve `target_audience` and/or `conversation_id`, then route private proactive notifications to the personal conversation or a trip-scoped activity detail instead of assuming group chat.

Related bug class:

deep-link drift / private notification misrouting

Confidence: High

### P2 — Concurrent Expense Settlement Can Duplicate “Share Settled” Pushes

Status: Suspected  
User impact: The payer can receive duplicate push notifications for the same member settling the same share if two settle requests race or a mobile retry overlaps the first request.  
Product promise affected: notification noise / duplicate sends

References:

- `Travel Agent/backend/api/routes/expenses.py:394` — endpoint snapshots unsettled shares before mutation.
- `Travel Agent/backend/api/routes/expenses.py:400` — mutation runs after the pre-snapshot.
- `Travel Agent/backend/api/routes/expenses.py:414` — push is spawned for every user in the precomputed `newly_settling` list.
- `Travel Agent/backend/api/routes/expenses.py:511` — batch settle repeats the same precomputed push pattern.
- `Travel Agent/backend/core/db/expenses.py:756` — DB update is idempotent via `is_settled IS false`, but the rowcount is not returned to drive push fan-out.
- `Travel Agent/backend/notifications/push.py:105` — `send_shares_settled_push()` sends directly with a fresh UUID and no helper-level dedupe.

Why it matters:

This is lower severity than privacy routing, but duplicate device-facing pushes are one of the fastest ways for dogfooders to mute the app. The DB mutation is idempotent; the notification side effect is keyed off a stale pre-read rather than the rows actually updated.

Repro or deterministic test idea:

1. Seed one unsettled share.
2. Run two concurrent `POST /api/trips/{trip_id}/expenses/{expense_id}/settle` requests for the same `user_id`.
3. Patch `send_shares_settled_push()` and assert it is called once.
4. Current likely: both requests can compute `newly_settling` before either commits, so both spawn a push.

Suggested fix direction:

Have the settle DB helper return the set of user ids whose rows were actually updated, or add a durable notification idempotency key such as `shares_settled:{expense_id}:{settled_user_id}` before dispatch.

Related bug class:

side-effect race / idempotency gap

Confidence: Medium

### P2 — Unread Conversation Feed Uses Mock-Only `last_message_at`

Status: Confirmed  
User impact: Real unread conversation notifications can have `created_at=undefined`, making feed ordering unstable; mock tests still pass because mocks include the field the backend does not return.  
Product promise affected: read/unread consistency / mock-real parity

References:

- `Travel Agent/backend/api/routes/_notifications_feed.py:45` — backend `UnreadConversation` schema has no `last_message_at`.
- `Travel Agent/backend/core/db/conversations/_read_state.py:284` — unread-count helper documents the returned fields.
- `Travel Agent/backend/core/db/conversations/_read_state.py:394` — real rows include `latest_message` and `latest_sender_type`, but no timestamp.
- `Travel App/utils/api/types.ts:862` — frontend knowingly defines a UI-only feed shape instead of the generated backend refs.
- `Travel App/utils/api/types.ts:873` — frontend type requires `last_message_at`.
- `Travel App/data/notifications.ts:50` — app maps `created_at` from `c.last_message_at`.
- `Travel App/data/notifications.ts:101` — combined feed sorts by `created_at`.

Why it matters:

The bell badge count can still be correct, but the feed can present a real unread chat out of order relative to proactive notifications, votes, and invite answers. That is a dogfood trust issue: the user sees a notification list that does not reflect what just happened.

Repro or deterministic test idea:

1. Add a frontend data test using the generated `UnreadConversation` shape with no `last_message_at`.
2. Assert every mapped `AppNotification.created_at` is a valid ISO string or that missing timestamps get a deterministic fallback.
3. Add an API/feed test that either returns `last_message_at` or proves the app no longer expects it.

Suggested fix direction:

Either add `last_message_at` to backend `UnreadConversation` and OpenAPI, or switch the app to generated refs and sort unread conversations with a safe fallback. Avoid keeping this as a hand-maintained frontend shadow type.

Related bug class:

mock-real drift / hand-written contract copy

Confidence: High

## Non-Findings / Things Ruled Out

- `pause_all`, quiet hours, cadence caps, and per-user interruptive caps are meaningfully covered in deterministic gates and dispatch paths; targeted gate/push tests passed.
- Member removal clears `notification_state` in `remove_trip_member()`, which prevents removed members from remaining in group proactive fan-out.
- Push device registration/upsert and logout deregistration have deterministic tests, including cold-launch device id persistence.
- Digest rendering has safe parse-error/no-data fallbacks. Batch digest failures are logged and isolated per trip; no live provider fallback was tested.
- Booking-event pushes have a process-local `(proposal_id, status)` dedupe test; I did not treat cross-process dedupe as dogfood-blocking.

## Suggested Follow-Up Checks

- Add a regression test for private group interjection metadata and session routing.
- Add a push/in-app routing test for proactive notifications with `target_audience="private"` and a real `conversation_id`.
- Add a concurrency test around expense settlement push side effects.
- Add a generated-contract-based notification feed test so `UnreadConversation` drift cannot hide behind mock data.
