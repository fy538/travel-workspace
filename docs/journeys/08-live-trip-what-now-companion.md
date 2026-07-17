# 08 - Live Trip What-Now Companion

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-16
> Primary phase: live trip + Vesper Home live mode

## Product Promise

During a trip, Vesper should answer the traveler's unstated question—**"are we
okay, and what happens next?"**—using the live itinerary, place, weather, route,
group, and relationship context. When reality changes, it should carry one
coherent response toward action rather than merely report the disruption.

## Canonical User Story

As a traveler already on the trip, I want Vesper to help me understand the next move, nearby options, and urgent changes, so that I do not have to manually stitch together plan, map, and chat.

## Why This Journey Matters

- Live-trip value is where the product either feels like a companion or a planning archive.
- It crosses Vesper Home, itinerary live mode, the in-place Map face,
  notifications, Chat, and location permission.
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
3. Open the active trip directly into Itinerary live mode for the route `tripId`.
4. Inspect the one contextual live/urgent state and its primary action.
5. Confirm Now Mode reflects in-progress versus upcoming blocks.
6. Switch in place to Map focused on current/next stop.
7. Ask Vesper "what should we do now?" from Map or itinerary context; the answer
   preserves the current day and opens the canonical action when a change helps.
8. Handle location permission allowed/denied/undetermined.
9. Dismiss or act on a nudge and confirm state updates.

### Deferred in this journey (see README deferrals)

- On-location voice guide walk (`/guide/[slug]`) — smoke only unless voice enters dogfood scope.
- Full narration/geofence loop — optional hook tests, not a promotion gate.

Journey 06 owns read-model agreement after a live-trip mutation; this journey owns live UX usefulness.

## Expected Outcome

- User-visible state: current/next stop, stay, route, and urgent cards are aligned.
- Data state: live mode derives from date/time and trip blocks; map focus uses valid ids.
- Cross-surface coherence: Vesper Home, Itinerary, Map, Chat, Details, and
  Changes agree on what is next.
- Trust state: denied location gracefully degrades to plan/place context.
- Emotional state: the traveler feels calm and oriented; Vesper communicates
  whether there is time, what can be skipped, and when no action is needed.
- Product proof: **Vesper helped at the right moment** and any accepted adjustment
  improved the itinerary without breaking the rest of the day.

## Must Never Happen

- On-trip visible CTA does nothing.
- Urgent "other things" appears tappable but is not interactive.
- Location denied creates blank map or broken chat context.
- Vesper gives a now-answer disconnected from current trip/day.
- Live card points to stale or completed block.

## AI Trace Prompt

```text
Trace live-trip state from the canonical lifecycle and itinerary into Vesper Home, Itinerary List/Map, notifications, and Ask Vesper seeds. For a delay/weather/closure case, trace notice → traveler/group impact → coherent proposal → authority → operation commit → relevant-member awareness. Identify no-op CTAs, permission fallbacks, currentTripId assumptions, and stale next-stop risks.
```

## First Automation Target

Mock-mode screen walkthrough with fixture `trip-lisbon-26`:

- open Vesper Home live mode
- tap every visible live/urgent CTA
- open the active trip directly into Itinerary live mode
- open Map from live context
- verify no dead taps and no stale next-stop mismatch
