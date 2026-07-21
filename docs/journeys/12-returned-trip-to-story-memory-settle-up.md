# 12 - Returned Trip To Story, Memory, And Settle-Up

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-16
> Primary phase: post-trip

## Product Promise

After a trip, Vesper should help the traveler remember, share, learn, and close the loop without turning the trip into a chore.

## Canonical User Story

As a traveler who just got back, I want to see my trip story, inspect what Vesper learned, and settle any money, so that the trip becomes useful memory.

## Why This Journey Matters

- It connects planning to durable product value.
- Memory/post-trip surfaces are partially mock-safe but require real data ordering/completeness checks.
- The app has strong returned-trip fixtures, so this can become a high-signal dogfood path quickly.

## Starting State

- Persona: Dev "Just back" or returned traveler.
- Trip state: completed trip within 14 days, story/memory/expenses available.
- Fixture: completed Athens/Barcelona/Amalfi style trips; post-trip notifications and Atlas candidate.
- Permissions: photo permissions optional for find-photos flow.

## Primary Surfaces

- Routes: `/(tabs)/trips`, `/(tabs)/trips/[tripId]`, `/(tabs)/trips/[tripId]/memory`, `/(tabs)/trips/[tripId]/story`, `/trip-expenses?tripId=`, `/(tabs)/atlas`, `/atlas/dna`, `/atlas/postcards`.
- App docs: [Memory Surface Brief (archived)](../../travel-app/docs/archive/briefs/Memory%20Surface.md), [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Atlas Home](../../travel-app/docs/page-specs/atlas-home.md).
- Reliability trace: [Memory And Post-Trip Loop](../reliability/traces/memory-and-post-trip-loop.md).
- Existing anchors: `__tests__/data/memory.test.ts`, `__tests__/data/memory-hooks.test.ts`, `__tests__/components/memory/TripStorySectionCard.test.tsx`, `__tests__/components/memory/ShareStorySheet.test.tsx`, `__tests__/screens/story.smoke.test.tsx`.

## Canonical Steps

1. Open Trips Home in returned state.
2. Tap returned trip or Atlas postcard hero.
3. Confirm the server-authored entry decision: final Itinerary remains the
   completed record; meaningful Memory may be recommended as the initial face.
4. Open Story from Memory or Trip Details and share/regenerate/edit if available.
5. Ask Vesper privately from Story footer.
6. Open Memory and inspect learned DNA.
7. Open Atlas from post-trip CTA.
8. Open settle-up/expenses.
9. Return to Trips and confirm post-trip state still makes sense.

## Expected Outcome

- User-visible state: returned trip retains its final itinerary and exposes
  Story, Memory, Atlas, and settle-up paths without a second trip dashboard.
- Data state: memory observations, story sections, expenses, and Atlas candidates have source metadata.
- Cross-surface coherence: Trip post mode, Story, Memory, Atlas, and Expenses agree about the completed trip.
- Trust state: user can inspect learning and avoid forced debrief forms.

## Must Never Happen

- Post-trip notification lands in generic chat instead of memory/story destination.
- Story regenerate destroys content without confirmation or fallback.
- Memory claims Vesper learned facts without receipt/provenance.
- Settle-up shows private booking totals without opt-in.
- Returned trip state disappears because dates/timezone are miscomputed.

## AI Trace Prompt

```text
Trace the returned-trip loop from Trips Home through server-authored
Itinerary/Memory entry, final Itinerary, Trip Details, Story, Memory, Atlas, and
Costs. Identify lifecycle timezone logic, readiness, source metadata,
notification entry points, exact-return navigation, photo permission fallbacks,
memory ordering, and mock-real drift.
```

## First Automation Target

Post-trip mock walkthrough:

- returned Trips Home renders returned hero
- Story route opens and share sheet works
- Memory route opens and links to Atlas DNA
- settle-up routes to expenses with trip id
- Atlas candidate/artifact state matches trip memory
