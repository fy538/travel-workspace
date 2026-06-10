# 06 - Home, Plan, Map, Changes Coherence

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: pre-trip / live-trip truth

## Product Promise

The same trip truth should appear consistently wherever the traveler looks: Home, Plan, Map, Chat, and Changes.

## Canonical User Story

As a traveler, I want the trip dashboard, itinerary, map, and change history to agree, so that I can trust the app during planning and while traveling.

## Why This Journey Matters

- The app is deceptively complex because every surface is a different projection of the same trip state.
- Read-model drift is one of the easiest ways to lose trust.
- Dogfooders may report "something feels off" without knowing which model is stale.

## Starting State

- Persona: organizer or member.
- Trip state: itinerary with placed and unplaced blocks, open decisions, and at least one recent change.
- Fixture: `trip-lisbon-26` plus open proposal/recent change.
- Permissions: location optional for live/current-position checks.

## Primary Surfaces

- Routes: `/(tabs)/trips/[tripId]`, `/(tabs)/trips/[tripId]/plan`, `/(tabs)/trips/[tripId]/map`, `/(tabs)/trips/[tripId]/changes`, `/(tabs)/trips/[tripId]/chat`.
- App docs: [Trip Map](../../travel-app/docs/page-specs/trip-map.md), [Trip Plan](../../travel-app/docs/page-specs/trip-plan.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md).
- Reliability trace: [Home, Plan, And Map Coherence](../reliability/traces/home-plan-map-coherence.md).
- Existing anchors: `__tests__/data/planState.test.ts`, `__tests__/utils/tripMapStateParity.test.ts`, `__tests__/utils/invalidateTripReadModels.test.ts`, `__tests__/screens/plan.smoke.test.tsx`, `__tests__/screens/map.smoke.test.tsx`.

## Canonical Steps

1. Open Trip Folio Home and note current/next/highest-attention item.
2. Open Plan and inspect the affected day/block.
3. Open Map and inspect the corresponding spatial pin or unplaced state.
4. Open Changes and inspect recent/open changes.
5. Apply or revert a change.
6. Revisit Home, Plan, Map, Chat, and Changes.
7. Confirm all surfaces agree after invalidation/refetch.

## Expected Outcome

- User-visible state: no surface contradicts another about time, place, status, or decision state.
- Data state: shared ids line up across home cards, plan blocks, map pins, proposals, and change events.
- Cross-surface coherence: changed blocks are visible everywhere or explicitly unplaced/unmapped.
- Trust state: dismissed cards do not erase critical trip truth.

## Must Never Happen

- Home says one next stop while Plan/Map show another.
- Map crashes or hides unplaced items.
- Plan applies a change but Map stays stale.
- Changes screen reverts an item that Plan cannot identify.
- A dismissed noncritical card hides an urgent/open decision.

## AI Trace Prompt

```text
Trace the trip read models feeding Home, Plan, Map, Chat, and Changes. Pick one itinerary block and one proposal/change id and follow them across hooks, API calls, mock data, backend endpoints, and invalidation paths. Report mismatched ids, optional params, stale caches, and missing tests.
```

## First Automation Target

Build a deterministic parity assertion:

- every mapped plan block has compatible map state
- every open proposal affecting a block appears in plan state
- every recent change can route back to proposal/detail or affected block
- invalidation runs after apply/revert

