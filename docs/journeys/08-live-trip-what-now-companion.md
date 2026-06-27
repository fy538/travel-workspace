# 08 - Live Trip What-Now Companion

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-26  
> Primary phase: live trip + Vesper Home live mode

## Product Promise

During a trip, the app should answer "what now?" with time, place, weather, route, and group context that is immediately useful.

## Canonical User Story

As a traveler already on the trip, I want Vesper to help me understand the next move, nearby options, and urgent changes, so that I do not have to manually stitch together plan, map, and chat.

## Why This Journey Matters

- Live-trip value is where the product either feels like a companion or a planning archive.
- It crosses Vesper Home, Trip Folio live mode, Trip Map, Plan, notifications, and location permission.
- Existing docs list several live/on-trip affordance no-ops that dogfooders will hit.

## Starting State

- Persona: member on active trip.
- Trip state: live trip with current day, current block, next block, stay, and route.
- Fixture: `trip-lisbon-26`.
- Permissions: location allowed, denied, and unset variants should all be tested.

## Primary Surfaces

- Routes: `/(tabs)/concierge`, `/(tabs)/trips`, `/(tabs)/trips/[tripId]`, `/(tabs)/trips/[tripId]/map`, `/(tabs)/trips/[tripId]/plan`, `/(tabs)/trips/[tripId]/chat`.
- App docs: [Concierge Home](../../travel-app/docs/page-specs/concierge-home.md), [Trip Map](../../travel-app/docs/page-specs/trip-map.md), [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md).
- Existing anchors: `__tests__/hooks/useAmbientWeather.test.ts`, `__tests__/hooks/useNarrationGeofence.test.ts`, `__tests__/screens/map.smoke.test.tsx`, `__tests__/utils/tripMapStateParity.test.ts`.

## Canonical Steps

1. Open Vesper Home (concierge tab) during an active trip — live/urgent cards, capture nudges, and trip-less fallback must not appear.
2. Open Trips Home global tab — live tile / NOW / TONIGHT routing when persona is on-trip.
3. Open Trip Folio live mode for the active `tripId` (route param, not `currentTrip` alone).
4. Inspect live/urgent card and its primary action.
5. Open the active day in Plan; confirm Now Mode reflects in-progress vs upcoming block.
6. Open Map focused on current/next stop.
7. Ask Vesper "what should we do now?" from Map or live card.
8. Handle location permission allowed/denied/undetermined.
9. Dismiss or act on a nudge and confirm state updates.

### Deferred in this journey (see README deferrals)

- On-location voice guide walk (`/guide/[slug]`) — smoke only unless voice enters dogfood scope.
- Full narration/geofence loop — optional hook tests, not a promotion gate.

Journey 06 owns read-model agreement after a live-trip mutation; this journey owns live UX usefulness.

## Expected Outcome

- User-visible state: current/next stop, stay, route, and urgent cards are aligned.
- Data state: live mode derives from date/time and trip blocks; map focus uses valid ids.
- Cross-surface coherence: Vesper/Home/Plan/Map/Chat agree on what is next.
- Trust state: denied location gracefully degrades to plan/place context.

## Must Never Happen

- On-trip visible CTA does nothing.
- Urgent "other things" appears tappable but is not interactive.
- Location denied creates blank map or broken chat context.
- Vesper gives a now-answer disconnected from current trip/day.
- Live card points to stale or completed block.

## AI Trace Prompt

```text
Trace live-trip state from date/time and trip plan into Vesper Home, Trip Folio, Plan, Map, notifications, and Ask Vesper seeds. Identify no-op CTAs, permission fallbacks, currentTripId assumptions, and map focus risks.
```

## First Automation Target

Mock-mode screen walkthrough with fixture `trip-lisbon-26`:

- open Vesper Home live mode
- tap every visible live/urgent CTA
- open Trip Folio live thread
- open Map from live context
- verify no dead taps and no stale next-stop mismatch

