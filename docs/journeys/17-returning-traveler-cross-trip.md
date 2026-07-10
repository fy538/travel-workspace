# 17 - Returning Traveler (Cross-Trip Recall)

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-29
> Primary phase: cross-trip (second-trip-benefits-from-first)

## Product Promise

The second trip is better because of the first: prior-trip taste, saved places, and place affinity surface as the traveler plans again — without leaking another trip's private group context.

## Canonical User Story

As a returning traveler, I want the app to remember what I liked and where I've been, so that planning trip two feels like the app knows me — while keeping each trip's private group details separate.

## Why This Journey Matters

- No journey proves the cross-trip value loop (place affinity, taste recall, "your map") — the substrate is built but largely dark (`ATLAS_SIGNALS_TO_MEMORY` gated, `traveler_place_affinity` recall wired but quiet).
- This is the place-relationship thesis: the product is a relationship with places over time, not a single-trip planner.
- The privacy risk is real: cross-trip recall must not surface another trip's private group context.

## Starting State

- Persona: a traveler with at least one completed/kept prior trip (affinity + saved places + Atlas memory) and a new second trip.

## Primary Surfaces

- Routes: `/(tabs)/trips/[tripId]` (new trip), `/(tabs)/discover`, `/(tabs)/atlas`, `/your-map`, `/(tabs)/concierge/chat`.
- App docs: [Atlas Home](../../travel-app/docs/page-specs/atlas-home.md), Place-affinity + taste-store memory.

## Canonical Steps

1. With a completed prior trip, start a second trip → planning surfaces prior-trip affinity / taste signals.
2. Discover / Ask Vesper in the new trip → recommendations reflect the returning traveler's known taste.
3. Open `/your-map` → cross-trip "everywhere you've been" aggregates correctly.
4. Confirm the new trip's context never surfaces another trip's private group constraints or members.

## Expected Outcome

- The second trip surfaces prior-trip affinity/taste recall.
- Cross-trip identity (`your-map`, DNA) aggregates across trips.
- Strict isolation: no private group context leaks between trips.

## Must Never Happen

- A second trip surfaces a prior trip's private group constraints, members, or messages.
- Cross-trip recall attributes the wrong trip's taste/affinity.
- "Your map" mixes trips incorrectly or shows trips the user isn't on.

## AI Trace Prompt

```text
Trace cross-trip recall: prior-trip affinity/taste/saved-places into a second trip's planning + Discover + your-map. Verify recall surfaces correctly AND that no private group context (constraints, members, messages) leaks from one trip into another.
```

## First Automation Target

> NOTE: cross-trip recall substrate is currently DARK (signals→memory gated). Until lit, this certifies as a visible skip. When enabled: persona-cert (lived) — seed/confirm a prior kept trip + a second trip for the same persona; assert prior-trip affinity surfaces in the second trip's context, and that no other trip's private fields appear.

The cached cross-trip-thread backend and typed app client exist, but a dedicated
Trip Home “from your prior trip” card is deferred until cohort evidence shows that
silent personalization is insufficient. J17 certifies the recall and privacy loop;
it does not require that extra explanatory surface for V1.
