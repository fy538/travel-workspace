# 14 - Solo Trip End-to-End

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-07-16
> Primary phase: cross-cutting (solo variant of the whole lifecycle)

## Product Promise

A traveler going alone gets a first-class experience — plan, live, memory — without ever being dropped into group chrome: no group chat routing, no votes, no "waiting on members."

## Canonical User Story

As a solo traveler, I want the app to feel built for one, so that group-coordination UI (consensus, delegation, member waiting) never intrudes on a trip that has only me.

## Why This Journey Matters

- The canonical set is group-wedge-weighted; "solo" appears only as a routing *variant* inside J07, never as an owned end-to-end journey.
- Chat-destination and consensus logic make mis-routing a solo user into group chrome a real, easy-to-miss regression.
- Solo is a large real-world segment and the cleanest demo of the single-user value loop.

## Starting State

- Persona: a single-member trip owner (mara on a solo trip, or a fresh solo persona).
- Trip state: one trip, one member (the owner, organizer role), planning then live.

## Primary Surfaces

- Routes: target trip entry/Itinerary, in-place Map face, private trip-scoped
  Vesper, `/notifications`, and `/(tabs)/atlas`.
- App docs: [Trip Itinerary](../../travel-app/docs/surfaces/trip-itinerary/contract.md), [Concierge Home](../../travel-app/docs/page-specs/concierge-home.md).

## Canonical Steps

1. Create/open a single-member trip → Itinerary/Trip Shape shows solo chrome
   with no group header, avatar row, or “waiting on N.”
2. Shape the Itinerary → no vote affordances or group proposal step; ordinary
   edits apply directly and consequential ones confirm.
3. Ask Vesper in chat → routes to a personal/solo conversation, never a group thread.
4. Live mode → "what now" reads for one; no group-coordination cards.
5. Notifications → personal cadence only; no group-activity rows.
6. Post-trip → Atlas memory is the solo user's own, no shared-with-group framing.

## Expected Outcome

- Every surface renders solo chrome for a single-member trip.
- Conversation routing resolves to personal/solo, not group.
- No consensus / vote / delegation / member-waiting UI appears anywhere.

## Must Never Happen

- A solo trip routes the user into a group chat.
- Vote / "waiting on members" / consensus UI renders for a one-member trip.
- Plan edits require a group-proposal step when there is no group.
- A solo trip's memory/Atlas implies other members.

## AI Trace Prompt

```text
Trace a single-member trip through Itinerary List/Map, Trip Details, chat
routing, notifications, completed Memory, and Atlas. Identify any surface that
renders group chrome (votes, consensus, member-waiting, group chat) or routes a
solo user into a group conversation.
```

## First Automation Target

Persona-cert (lived): create a single-member trip as the seeded persona; assert the trip has exactly one member, plan-state exposes no consensus/vote affordances, and chat routing resolves to a personal/solo conversation — not group.
