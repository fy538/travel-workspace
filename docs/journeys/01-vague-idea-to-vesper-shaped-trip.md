# 01 - Vague Idea To Vesper-Shaped Trip

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: cold start / ideation

## Product Promise

A traveler can arrive with only a fuzzy wish and leave with useful momentum: a private Vesper thread, a coherent trip direction, and optionally a draft trip, without the app pretending the plan is more concrete than it is.

## Canonical User Story

As a traveler, I want to say "maybe Portugal in September with friends" and have Vesper shape the idea, so that I can begin without filling a form or knowing exact dates.

## Why This Journey Matters

- It protects the first meaningful product moment.
- It tests whether Vesper and Trips agree on when a trip exists versus when an idea is still exploratory.
- Mock mode can make this look easy because prefilled prompts and seeded trips hide real conversation/session edge cases.

## Starting State

- Persona: new or low-history user, no substantive upcoming trip.
- Trip state: cold Trips Home or no selected current trip.
- Fixture: cold/default mock trip state, plus saved places if testing the saved-places bridge.
- Permissions: no location required.

## Primary Surfaces

- Routes: `/(tabs)/trips`, `/trip-begin`, `/(tabs)/concierge`, `/(tabs)/concierge/chat`.
- App docs: [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Concierge Home](../../travel-app/docs/page-specs/concierge-home.md), [Agent Chat](../../travel-app/docs/page-specs/agent-chat.md).
- Existing anchors: `__tests__/offline/goldenPath.test.ts`, `__tests__/screens/concierge-home.smoke.test.tsx`, `__tests__/screens/concierge-chat.smoke.test.tsx`, `__tests__/utils/conversationSeed.test.ts`.

## Canonical Steps

1. Open Trips Home in cold/default state.
2. Tap `+` and land on `/trip-begin`.
3. Choose "Talk it through with Vesper" or a shape tile.
4. Land in private Vesper chat with a meaningful prefill or seed.
5. Ask a vague planning question.
6. Optionally promote the conversation into a draft trip.
7. Return to Trips and confirm the idea is represented honestly as ideation/draft, not as a committed itinerary.

## Expected Outcome

- User-visible state: private chat opens with context; Vesper can continue the planning thread; any created trip is marked as ideation/draft.
- Data state: conversation id and optional trip id are stable; promoted trip appears in trip list.
- Cross-surface coherence: Trips Home, Vesper Home, and chat history agree on the latest thread/trip.
- Trust state: no group-visible workspace is created until the user explicitly creates or promotes one.

## Must Never Happen

- Creating an exploratory chat silently creates a real trip with misleading dates/place.
- The user lands in group chat for a private ideation question.
- Back navigation strands the user on `/trip-begin`.
- A starter tile opens chat with an empty or generic prompt.
- A promoted trip does not show up in Trips.

## AI Trace Prompt

```text
Trace the cold-start ideation path from Trips Home through trip-begin into Vesper chat. Identify the route helpers, prefill/ConversationSeed behavior, createTrip/promoteConversation behavior, mock fallback, and real-backend drift risks. Verify that exploratory chat does not accidentally create a committed trip.
```

## First Automation Target

Static trace plus a mock API test proving:

- shape tile/prefill opens private concierge chat
- conversation promotion returns a stable trip id
- promoted trip appears in `getTripsForUser`
- created trip status is ideation/draft

