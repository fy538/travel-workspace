# 01 - Vague Idea To Vesper-Shaped Trip

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-16
> Primary phase: cold start / ideation / first session

## Product Promise

A traveler can arrive with only a fuzzy wish and leave with useful momentum: a private Vesper thread, a coherent trip direction, and optionally a draft trip, without the app pretending the plan is more concrete than it is.

## Canonical User Story

As a traveler, I want to say "maybe Portugal in September with friends" and have Vesper shape the idea, so that I can begin without filling a form or knowing exact dates.

## Why This Journey Matters

- It protects the first meaningful product moment.
- It tests whether Vesper and Trips agree on when a trip exists versus when an idea is still exploratory.
- Mock mode can make this look easy because prefilled prompts and seeded trips hide real conversation/session edge cases.

## Boundary With Journey 03

- **Journey 01 ends** when the user is still ideating OR has just promoted/created a draft trip but has not yet filled workspace facets (place, dates, people).
- **Journey 03 starts** when a `trip_id` exists and Itinerary shows an honest
  undated Trip Shape with setup actions to complete.

## Starting State

- Persona: new or low-history user, no substantive upcoming trip.
- Trip state: cold Trips Home, between-trips, or no selected current trip.
- Fixture: cold/default mock trip state; also exercise `between`, `urgent`, and low-history personas where Trips Home hero differs.
- Permissions: no location required; push permission may be requested at first trip-chat send (Phase 0).

## Phase 0 — First Session (embedded, cross-journey)

Trace these when the persona is net-new:

1. Auth: `/(auth)/sign-in` or skip-auth dev path.
2. Onboarding: `/onboarding`, `/onboarding-safety` when shown.
3. Planning-intent bootstrap if enabled.
4. First land on Trips Home **or** Vesper Home — hero must match phase (cold / between / urgent).
5. Push permission gate at first meaningful chat send (if applicable).

Journey 02 owns invite auth detours; this journey owns cold first open.

## Primary Surfaces

- Routes: `/(tabs)/trips`, `/trip-begin`, `/(tabs)/concierge`, `/(tabs)/concierge/chat`, `/onboarding`, `/onboarding-safety`.
- App docs: [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Concierge Home](../../travel-app/docs/page-specs/concierge-home.md), [Agent Chat](../../travel-app/docs/page-specs/agent-chat.md).
- Existing anchors: `__tests__/offline/goldenPath.test.ts`, `__tests__/screens/concierge-home.smoke.test.tsx`, `__tests__/screens/concierge-chat.smoke.test.tsx`, `__tests__/utils/conversationSeed.test.ts`.

## Canonical Steps

1. Open Trips Home in cold/default state — confirm TripHero phase (cold, between, or urgent) matches persona and does not fake a committed trip.
2. Open Vesper Home (concierge tab) — confirm global state is honest when no trip is selected.
3. Tap `+` on Trips and land on `/trip-begin`.
4. Choose "Talk it through with Vesper" or a shape tile.
5. Land in private Vesper chat with a meaningful prefill or seed (`conciergeSeed` / `ConversationSeed`).
6. Ask a vague planning question; confirm prefill is not swallowed before conversation id resolves.
7. Optionally promote the conversation into a draft trip.
8. Return to Trips and confirm the idea is represented honestly as ideation/draft, not as a committed itinerary.
9. If promoted, hand off to Journey 03 for facet setup — do not re-test blank-trip facets here.

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
Trace the cold-start ideation path: Phase 0 auth/onboarding (if applicable), Trips Home TripHero phases, Vesper Home with no trip, trip-begin, private chat prefill/ConversationSeed, createTrip/promoteConversation, mock vs real PromoteToTripResponse, and first-session push gate. Verify exploratory chat does not accidentally create a committed trip. Stop before Journey 03 facet setup.
```

## First Automation Target

Static trace plus a mock API test proving:

- shape tile/prefill opens private concierge chat
- conversation promotion returns a stable trip id
- promoted trip appears in `getTripsForUser`
- created trip status is ideation/draft
