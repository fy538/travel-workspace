# 09 - Notifications And Proactive Routing

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: proactive help / re-entry

## Product Promise

Notifications should bring the traveler back to the right surface, at the right level of privacy, without being noisy or misleading.

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

## Expected Outcome

- User-visible state: every notification tap lands on the smallest useful surface.
- Data state: read state persists; badge count and feed partition agree.
- Cross-surface coherence: notification object maps to valid trip/conversation/proposal/social destination.
- Trust state: private notification copy and destination do not expose private facts to group.

## Must Never Happen

- Private outcome routes to group chat.
- Social/trip/personal badge counts disagree with the feed opened by the bell.
- Read state updates locally but reappears after refresh.
- Push tap with missing trip id strands the user.
- Quiet hours/cadence settings are ignored for proactive noncritical nudges.

## AI Trace Prompt

```text
Trace notification feed, ownership, routing priority, read-state mutation, badge counts, push payload handling, and preference/cadence controls. Verify private-vs-group destinations and list every fallback when ids are missing.
```

## First Automation Target

Route-priority test matrix:

- `outcome_id + trip_id + private` -> private concierge
- `outcome_id + trip_id` -> group chat
- concierge category + trip -> group chat
- invite answer -> trip info
- generic trip -> trip detail
- social -> companions
- fallback -> private concierge

