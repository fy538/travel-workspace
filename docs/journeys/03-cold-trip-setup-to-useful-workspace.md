# 03 - Cold Trip Setup To Useful Workspace

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: early planning

## Product Promise

A blank trip should become a useful workspace through lightweight setup: place, dates, people, stay intent, costs, and first planning moves.

## Canonical User Story

As a traveler with a new trip draft, I want to fill in just enough structure for the trip page to become helpful, so that planning can continue naturally.

## Why This Journey Matters

- Trip Folio Home is a state machine with cold, pre, live, and post modes.
- Bugs here often look like empty states, dead facets, or stale mode transitions.
- Dogfooders may not notice if a seeded trip works but a fresh blank trip is incoherent.

## Starting State

- Persona: organizer.
- Trip state: blank/draft trip with missing place, dates, and members.
- Fixture: blank trip utility and mock createTrip path.
- Permissions: no location required.

## Primary Surfaces

- Routes: `/(tabs)/trips/[tripId]`, `/trip-place?tripId=`, `/trip-dates?tripId=`, `/trip-info?tripId=`, `/trip-accommodations?tripId=`, `/trip-expenses?tripId=`, `/(tabs)/trips/[tripId]/chat`.
- App docs: [Trip Page](../../travel-app/docs/page-specs/trip-page.md), [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md).
- Existing anchors: `__tests__/utils/blankTrip.test.ts`, `__tests__/screens/trip-workspace.smoke.test.tsx`, `__tests__/hooks/useTripSettings.test.ts`.

## Canonical Steps

1. Create or open a blank/draft trip.
2. Confirm cold Trip Folio renders setup slots for place, dates, and people.
3. Select or enter a place.
4. Select date shape or dates.
5. Add/invite at least one traveler.
6. Use "Build the trip" to open group chat with prefill.
7. Open stay and costs facets once they become relevant.
8. Return to Trip Folio and confirm it now reads as a useful pre-trip workspace.

## Expected Outcome

- User-visible state: setup slots disappear or update as fields are filled; pre-trip surfaces appear when dates/place exist.
- Data state: patched trip fields persist and hydrate after reload.
- Cross-surface coherence: Trip title/header, Home facets, chat context, and trip settings agree.
- Trust state: incomplete setup is honestly labeled, not covered by fake itinerary content.

## Must Never Happen

- A draft trip shows committed itinerary UI before required data exists.
- Setup slot tap drops `tripId`.
- Updated place/dates appear in one surface but not another.
- "Build the trip" opens private chat when the move is visibly group planning.
- A non-organizer can mutate organizer-only setup without permission.

## AI Trace Prompt

```text
Trace the cold Trip Folio setup path. For each setup slot and facet, identify route params, hooks, patchTrip behavior, mock persistence, organizer permissions, and mode transition logic. Report any display-only affordances that look tappable.
```

## First Automation Target

Mock-mode journey test:

- create blank trip
- patch place and dates
- reload trip
- verify mode changes from cold toward pre
- verify setup links preserve `tripId`

