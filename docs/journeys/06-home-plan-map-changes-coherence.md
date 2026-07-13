# 06 - Itinerary, Map, Details, Chat, And Changes Coherence

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-26  
> Primary phase: pre-trip / live-trip truth (projection invariant layer)

## Product Promise

The same trip truth should appear consistently wherever the traveler looks:
Itinerary List, Map, Trip Details, Chat, and Changes. The transitional Folio/Home
adapter must agree during migration but is not a target destination.

## Canonical User Story

As a traveler, I want the itinerary, map, trip details, conversation context,
and change history to agree, so that I can trust the app during planning and
while traveling.

## Why This Journey Matters

- The app is deceptively complex because every surface is a different projection of the same trip state.
- Read-model drift is one of the easiest ways to lose trust.
- Dogfooders may report "something feels off" without knowing which model is stale.

This journey is the **invariant checker** that runs after any mutation from Journey 05 (proposal apply/revert **or** direct edit-preview/commit), Journey 08 live actions, or Journey 10 booking writeback. It does not own the mutation workflow — only whether all read models agree afterward.

## Starting State

- Persona: organizer or member.
- Trip state: itinerary with placed and unplaced blocks, open decisions, and at least one recent change.
- Fixture: `trip-lisbon-26` plus open proposal/recent change.
- Permissions: location optional for live/current-position checks.

## Primary Surfaces

- Routes: target trip entry/Itinerary List, in-place Map face, Trip Details,
  `/(tabs)/trips/[tripId]/changes`, and `/(tabs)/trips/[tripId]/chat`.
- App docs: [Trip Itinerary contract](../../travel-app/docs/surfaces/trip-itinerary/contract.md),
  [Itinerary UX audit](../../travel-app/docs/audits/itinerary-interaction-ux-audit-2026-07-12.md),
  and [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md).
- Reliability trace: [Itinerary, Map, Details, Chat, And Changes Coherence](../reliability/traces/home-plan-map-coherence.md).
- Existing anchors: `__tests__/data/planState.test.ts`, `__tests__/utils/tripMapStateParity.test.ts`, `__tests__/utils/invalidateTripReadModels.test.ts`, `__tests__/screens/plan.smoke.test.tsx`, `__tests__/screens/map.smoke.test.tsx`.

## Canonical Steps

1. Open the trip directly into Itinerary and note current/next/highest-attention item.
2. Inspect the affected day/block in List.
3. Switch in place to Map and inspect the corresponding spatial pin or unplaced state.
4. Open Trip Details and Changes; inspect canonical summary/history truth.
5. Apply or revert a change **or** complete a direct edit commit (Journey 05 Track B).
6. Revisit Itinerary List, Map, Trip Details, Chat, and Changes. During migration,
   verify the Folio compatibility adapter as an additional projection.
7. Confirm all surfaces agree after invalidation/refetch — including `applied_block_map` id transitions after proposal apply.
8. Dismiss a non-critical home card and confirm Tier 1 trip truth remains visible.

## Expected Outcome

- User-visible state: no surface contradicts another about time, place, status, or decision state.
- Data state: shared ids line up across home cards, plan blocks, map pins, proposals, and change events.
- Cross-surface coherence: changed blocks are visible everywhere or explicitly unplaced/unmapped.
- Trust state: dismissed cards do not erase critical trip truth.

## Must Never Happen

- Itinerary/List, Map, Details, Chat attachment, Changes, or the transitional
  Folio adapter claim different current/next truth.
- Map crashes or hides unplaced items.
- Plan applies a change but Map stays stale.
- Changes screen reverts an item that Plan cannot identify.
- Dismissing noncritical attention hides an urgent/open decision.

## AI Trace Prompt

```text
Trace the trip read models feeding Itinerary List, Map, Trip Details, Chat attachments, Changes, and the transitional Folio adapter. Pick one block id and follow it across hooks, API calls, mock data, backend endpoints, invalidation paths, and compatibility-cache behavior. Run after BOTH proposal apply/revert AND direct edit-commit. Report mismatched ids, applied_block_map drift, stale caches, and missing tests.
```

## First Automation Target

Build a deterministic parity assertion:

- every mapped plan block has compatible map state
- every open proposal affecting a block appears in plan state
- every recent change can route back to proposal/detail or affected block
- invalidation runs after apply/revert
