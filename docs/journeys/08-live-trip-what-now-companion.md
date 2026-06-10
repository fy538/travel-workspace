# 08 - Live Trip What-Now Companion

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: live trip

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

1. Open Vesper Home during an active trip.
2. Inspect live/urgent card and its primary action.
3. Open Trip Folio live mode.
4. Open the active day in Plan.
5. Open Map focused on current/next stop.
6. Ask Vesper "what should we do now?" from Map or live card.
7. Handle location permission allowed/denied.
8. Dismiss or act on a nudge and confirm state updates.

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

