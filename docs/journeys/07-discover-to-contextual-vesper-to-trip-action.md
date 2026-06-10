# 07 - Discover To Contextual Vesper To Trip Action

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: inspiration / place-aware planning

## Product Promise

Discover should not be a browse-only magazine. A traveler can find a place, ask Vesper with context, and turn discovery into a trip action.

## Canonical User Story

As a traveler browsing Lisbon, I want to open a venue or dossier, ask Vesper about it, and save, compare, book, or add it to my trip without re-explaining context.

## Why This Journey Matters

- Discover is a major tab but is not covered by the original six reliability paths.
- ConversationSeed is the connective tissue between editorial/place surfaces and Vesper.
- Real content sparsity, missing ids, and venue/dossier shape drift can hide behind polished mocks.

## Starting State

- Persona: traveler with or without an active trip.
- Trip state: no trip for solo inspiration variant; planning trip for add-to-plan variant.
- Fixture: Discover feed with dossier, venue, guide, event, and friend cards.
- Permissions: no location required, but place search/network state matters.

## Primary Surfaces

- Routes: `/(tabs)/discover`, `/venue/[venueId]`, `/place/[placeSlug]`, `/dossier/[dossierId]`, `/guide/[slug]`, `/angle/[angleId]`, `/(tabs)/concierge/chat`, `/(tabs)/trips/[tripId]/chat`.
- App docs: [Discover](../../travel-app/docs/page-specs/discover.md), [Conversation Seed Standard](../../travel-app/docs/conversation-seed/Standard.md), [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md).
- Existing anchors: `__tests__/data/discover.test.ts`, `__tests__/utils/discoverFeed.test.ts`, `__tests__/screens/discover.smoke.test.tsx`, `__tests__/screens/venue-detail.smoke.test.tsx`, `__tests__/screens/place-home.smoke.test.tsx`.

## Canonical Steps

1. Open Discover.
2. Search or select a place context.
3. Tap a dossier, venue, guide, event, or friend card.
4. Ask Vesper from the detail surface.
5. Confirm chat opens with ConversationSeed context.
6. If in a trip, add to plan or ask the group.
7. If not in a trip, save, find similar, or continue private planning.
8. Return to Discover/place and confirm saved/context state persists.

## Expected Outcome

- User-visible state: Vesper knows what object/place the user came from.
- Data state: seed carries entity or clientContext; add/save action has stable ids.
- Cross-surface coherence: venue/place/dossier/chat/trip all preserve context.
- Trust state: no generic answer when the user asked from a specific object.

## Must Never Happen

- Ask Vesper opens empty chat from a detail page.
- Add to plan loses trip id or routes solo users into group chat.
- Share-with-group no-ops without rendering disabled or alternative path.
- Guide angle/entity cards look tappable but are not wired.
- Real Discover empty state reads like broken plumbing.

## AI Trace Prompt

```text
Trace Discover card navigation and Ask Vesper handoff for dossier, venue, guide, event, friend, and sample cards. Verify ConversationSeed construction, trip-aware routing, save/add/book actions, mock data shape, and backend Discover endpoint assumptions.
```

## First Automation Target

Create a route/seed test matrix:

- every Discover card kind has expected destination
- every detail Ask Vesper path includes entity/clientContext
- trip context chooses group chat only for social trip actions
- no-trip context chooses private concierge

