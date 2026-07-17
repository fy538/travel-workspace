# 09 - Notifications And Proactive Routing

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-16
> Primary phase: proactive help / re-entry

## Product Promise

Vesper should notice a consequential gap, understand its impact, prepare a useful
response, and reach the traveler through the smallest privacy-correct surface.
A notification is successful only when it reduces work or leads toward a real
trip outcome; routing alone is necessary but insufficient.

## Canonical User Story

As a traveler, I want a Vesper nudge or trip notification to open exactly where I can act on it, so that I do not have to hunt through the app.

## Why This Journey Matters

- Notifications are a high-drift domain: timing, read state, push payloads, and real routing can diverge from mocks.
- Routing is privacy-sensitive: private outcomes go to private chat; group-visible outcomes go to group surfaces.
- Poor proactive behavior can make dogfood feel spammy even if the core app works.

## Starting State

- Persona: organizer and member variants.
- Trip state: active planning trip with open proposal, invite answer, concierge outcome, social notification, and generic trip update.
- Fixture: notification feed with categories and trip ids.
- Permissions: push allowed/denied; quiet hours and cadence configured.

## Primary Surfaces

- Routes: `/notifications`, `/(tabs)/concierge/chat`, `/(tabs)/trips/[tripId]/chat`, `/(tabs)/trips/[tripId]`, `/trip-info?tripId=`, `/atlas/companions`, `/atlas/notifications`.
- App docs: [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Agent Chat](../../travel-app/docs/page-specs/agent-chat.md), [Atlas Home](../../travel-app/docs/page-specs/atlas-home.md).
- Reliability trace: [Notifications And Proactive Help](../reliability/traces/notifications-and-proactive-help.md).
- Existing anchors: `__tests__/data/notifications.test.ts`, `__tests__/screens/notifications.smoke.test.tsx`, `__tests__/screens/notifications.routing.test.tsx`, `__tests__/utils/notificationOwnership.test.ts`, `__tests__/utils/push.test.ts`.

## Canonical Steps

1. Open notification feed in All, Trips, and Personal modes.
2. Tap a private outcome notification.
3. Tap a group outcome/proposal notification.
4. Tap a concierge category with trip id.
5. Tap invite-answer notification.
6. Tap generic trip notification.
7. Tap social notification.
8. Change notification cadence/quiet setting and verify the feed respects it.
9. Mark read and confirm badge/feed state updates.
10. For one advisory candidate, verify the full intervention: evidence → impact
    on these travelers/this itinerary → prepared action → authority decision →
    itinerary or coordination outcome.
11. Dismiss or defer a low-urgency intervention and verify that Vesper quiets the
    relevant class without suppressing critical operational messages.

## Expected Outcome

- User-visible state: every notification tap lands on the smallest useful surface.
- Data state: read state persists; badge count and feed partition agree.
- Cross-surface coherence: notification object maps to valid trip/conversation/proposal/social destination.
- Trust state: private notification copy and destination do not expose private facts to group.
- Product state: an advisory nudge opens the exact itinerary/proposal context and
  offers the best available next action, not a generic information screen.
- Emotional state: the traveler experiences the intervention as timely help, not
  another feed item to manage.

## Must Never Happen

- Private outcome routes to group chat.
- Social/trip/personal badge counts disagree with the feed opened by the bell.
- Read state updates locally but reappears after refresh.
- Push tap with missing trip id strands the user.
- Quiet hours/cadence settings are ignored for proactive noncritical nudges.
- Weather, delay, closure, or group-state information is sent without explaining
  its trip consequence or offering a useful continuation.
- Notification delivery claims a plan/provider outcome that the canonical
  itinerary operation or provider evidence does not confirm.

## AI Trace Prompt

```text
Trace opportunity detection, need/accept arbitration, ownership, routing priority, read-state mutation, badge counts, push payload handling, and preference/cadence controls. Verify private-vs-group destinations, the canonical itinerary continuation for material actions, every fallback when ids are missing, and every path where silence should win.
```

## First Automation Target

Route-priority test matrix:

- `outcome_id + trip_id + private` -> private concierge
- `outcome_id + trip_id + group-visible proposal` -> proposal/itinerary context
- concierge category + trip -> smallest relevant trip or private Vesper context
- invite answer -> trip info
- generic trip -> canonical itinerary or named Trip Details continuation
- social -> companions
- fallback -> private concierge
