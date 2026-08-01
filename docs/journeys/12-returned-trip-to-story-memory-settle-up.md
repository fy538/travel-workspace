# 12 - Returned Trip To Itinerary, Story, And Settle-Up

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-08-01
> Primary phase: post-trip

## Product Promise

After a trip, the ordinary itinerary should remain the traveler’s stable trip
record, with explicit Story and settle-up doors where those capabilities exist.

## Canonical User Story

As a traveler who just got back, I want to reopen the same itinerary, optionally
read or share its Story, and settle any money without learning a new post-trip
workspace.

## Why This Journey Matters

- It connects planning to durable product value.
- The itinerary remains useful after return instead of being displaced by a
  separately designed Memory product.
- The app has strong returned-trip fixtures, so this can become a high-signal dogfood path quickly.

## Starting State

- Persona: Dev "Just back" or returned traveler.
- Trip state: completed trip within 14 days, itinerary/story/expenses available.
- Fixture: completed Athens/Barcelona/Amalfi style trips; post-trip notifications and Atlas candidate.
- Permissions: photo permissions optional for find-photos flow.

## Primary Surfaces

- Routes: `/(tabs)/trips`, `/(tabs)/trips/[tripId]/plan`, `/(tabs)/trips/[tripId]/story`, `/trip-expenses?tripId=`, `/(tabs)/atlas`.
- Compatibility: `/(tabs)/trips/[tripId]/memory` immediately redirects to the itinerary; it is not a product surface.
- App docs: [Trip Itinerary Contract](../../travel-app/docs/surfaces/trip-itinerary/contract.md), [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Atlas Home](../../travel-app/docs/page-specs/atlas-home.md).
- Reliability trace: [Memory And Post-Trip Loop](../reliability/traces/memory-and-post-trip-loop.md).
- Existing anchors: `__tests__/data/memory.test.ts`, `__tests__/data/memory-hooks.test.ts`, `__tests__/components/memory/TripStorySectionCard.test.tsx`, `__tests__/components/memory/ShareStorySheet.test.tsx`, `__tests__/screens/story.smoke.test.tsx`.

## Canonical Steps

1. Open Trips Home in returned state.
2. Tap returned trip or Atlas postcard hero.
3. Confirm the completed trip opens the same Itinerary shell and day spine used
   before/during travel, with structural editing denied by server capability.
4. Open Story only from an explicitly labeled Story action and share/regenerate if available.
5. Ask Vesper privately from Story footer.
6. Open Atlas only from an explicitly labeled Atlas action.
7. Open settle-up/expenses.
8. Return to Trips and confirm post-trip state still makes sense.

## Expected Outcome

- User-visible state: returned trip retains its ordinary itinerary and exposes
  explicit Story, Atlas, and settle-up paths without a second trip dashboard.
- Data state: itinerary occurrence evidence, story sections, expenses, and Atlas candidates have source metadata.
- Cross-surface coherence: Itinerary, Story, Atlas, and Expenses agree about the completed trip.
- Trust state: user can inspect learning and avoid forced debrief forms.

## Must Never Happen

- General trip entry redirects away from Itinerary based on retrospective readiness.
- A retired Memory link dead-ends instead of redirecting to Itinerary.
- Story regenerate destroys content without confirmation or fallback.
- Atlas or Story claims Vesper learned facts without receipt/provenance.
- Settle-up shows private booking totals without opt-in.
- Returned trip state disappears because dates/timezone are miscomputed.

## AI Trace Prompt

```text
Trace the returned-trip loop from Trips Home through canonical Itinerary entry,
Trip Details, explicit Story, Atlas, and Costs. Confirm the retired Memory route
redirects to Itinerary. Identify lifecycle timezone logic, source metadata,
notification entry points, exact-return navigation, photo permission fallbacks,
itinerary ordering, and mock-real drift.
```

## First Automation Target

Post-trip mock walkthrough:

- returned Trips Home renders returned hero
- Story route opens and share sheet works
- retired Memory route redirects to the ordinary itinerary
- settle-up routes to expenses with trip id
- Atlas candidate/artifact state matches the completed-trip evidence
