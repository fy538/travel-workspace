# Area Audit: Trip Home, Plan, Map, And Read-Model Coherence

Date: 2026-05-21  
Agent: Cursor Cloud agent auditing as Codex  
Scope: Home feed/card generation and dismissal lifecycle; itinerary, plan-state, map-state backend read models; frontend trip home, Plan v2, Map v2, proposal sheet, cache invalidation hooks, mock/map fixtures, and area docs.  
Mode: Audit only. No product-code changes unless explicitly noted.

## Executive Summary

- Dogfood risk: Medium
- Highest-risk finding: Home's backend TTL cache can serve stale pending-decision cards after proposal resolution or card dismissal, so Home can contradict Plan for up to 60 seconds even when the app invalidates React Query.
- Checks run: `make doctor` -> pass; `make contract-check` -> pass; `make api-coverage-check` -> pass; `make mock-real-parity` -> pass; `make golden-path-qa` -> pass; targeted backend and frontend home/plan/map tests -> pass.
- Residual uncertainty: No live backend, LLM, production services, or external APIs were called; findings are based on static analysis plus deterministic offline tests.

## Findings

### P1 - Backend Home Feed Cache Can Re-Surface Stale Decisions After Mutations

Status: Confirmed  
User impact: A dogfood tester can accept/reject a proposal or dismiss a Home card, then return to Home and still see the old "Weigh in" or dismissed card until the 60-second backend cache expires. Plan can show the accepted/recent-change truth while Home still asks for a vote.  
Product promise affected: plan coherence / concierge trust / stale-cache path

References:

- `Travel Agent/backend/home/feed.py:84` - declares an in-process 60-second feed cache keyed only by `(trip_id, user_id)`.
- `Travel Agent/backend/home/feed.py:96` - `_get_cached_feed` returns the cached full `HomeFeed` without re-checking dismissals or proposal state.
- `Travel Agent/backend/home/feed.py:508` - `assemble_home_feed` returns the cached feed before loading trip, proposals, itinerary, bookings, or dismissed keys.
- `Travel Agent/backend/home/feed.py:593` - dismissed keys are read only on a cold compose.
- `Travel Agent/backend/home/feed.py:912` - dismissal filtering happens only before `_put_cached_feed`, so the cached value bakes in the old dismissal/proposal state.
- `Travel Agent/backend/api/routes/home.py:121` - dismiss route writes the dismissal row but does not clear the in-process feed cache.
- `Travel App/utils/invalidateTripReadModels.ts:17` - frontend correctly invalidates `trip-home-cards` after plan/proposal mutations, but the backend can still answer that refetch from its stale in-process cache.

Why it matters:

This is the most direct contradiction in the audited area. The frontend has a good shared invalidator for itinerary, map, plan-state, and home cards, but the server-side cache sits behind it. A React Query invalidation after proposal acceptance can fetch the same old backend feed, making Home lag behind Plan exactly when the trust loop is most visible.

Minimal trace:

```json
{
  "state_before": "Home feed is cold-composed with pending_decision ref_id=proposal-1 and cached for (trip_id,user_id). Plan shows the block as proposed.",
  "action": "Organizer accepts proposal-1, app invalidates trip read models, then user opens Home immediately.",
  "state_after": "Plan-state refetch can show proposal accepted/recent change, but GET /home_cards can return the cached pending_decision until the 60s TTL expires."
}
```

Repro or deterministic test idea:

1. Unit-test `assemble_home_feed` with `_feed_cache` cleared and patched producers returning a `pending_decision`.
2. Call `assemble_home_feed` once to populate the cache.
3. Patch `get_trip_proposals` to return no open proposals and/or patch `list_dismissed_keys` to include the card.
4. Call `assemble_home_feed` again before TTL expiry.
5. Expected: no pending/dismissed card.
6. Current likely/observed: cached pending/dismissed card is returned.

Suggested fix direction:

Cache only the expensive anchor voice line, or add a narrow `invalidate_home_feed_cache(trip_id, user_id | None)` helper and call it from dismiss/undismiss plus proposal, booking, capture, and relevant itinerary mutation paths. If caching the full feed stays, the cache key needs an input version for dismissals/proposals/booking events, not just trip and user.

Related bug class:

Server-side stale cache bypassing client invalidation

Confidence: High

### P2 - Stay And Booking Mutations Refresh Local Screens But Not All Surfaces That Read The Same State

Status: Confirmed  
User impact: A tester can create/update a stay or confirm a booking and see that screen update, while Plan's cross-trip rail, Home booking cards, or Map base context remain stale or absent. The user has to navigate away, wait for refetch behavior, or hit a different surface before the trip "truth" catches up.  
Product promise affected: plan coherence / map coherence / cross-surface read-model freshness

References:

- `Travel App/data/booking.ts:85` - creating a booking session invalidates only `bookingSessions`.
- `Travel App/data/booking.ts:141` - confirming the booking cart invalidates only the individual booking session.
- `Travel App/data/accommodations.ts:35` - create accommodation invalidates only the accommodations list.
- `Travel App/data/accommodations.ts:58` - update accommodation invalidates only the accommodations list.
- `Travel App/data/accommodations.ts:74` - delete accommodation invalidates only the accommodations list.
- `Travel App/utils/invalidateTripReadModels.ts:9` - shared invalidator exists for itinerary, map-state, plan-state, and home cards, but these hooks do not call it.
- `Travel Agent/backend/core/db/plan_state.py:583` - Plan-state reads booking sessions.
- `Travel Agent/backend/core/db/plan_state.py:595` - Plan-state also reads trip accommodations into `cross_trip.accommodation`.
- `Travel App/components/trip-plan/PlanCrossTripRail.tsx:15` - Plan visibly renders accommodation and booking-session state from `planState.cross_trip`.
- `Travel Agent/backend/core/map_state/builder.py:101` - Map base is derived only from accommodation-shaped itinerary blocks with coordinates.
- `Travel Agent/backend/core/map_state/builder.py:193` - Map-state iterates itinerary blocks; it does not include `trip_accommodations`.

Why it matters:

Plan v2 treats cross-trip commitments as trip truth. The backend already aggregates booking sessions and trip accommodations into plan-state, and the frontend has a single read-model invalidator for exactly this coherence problem. The mutations that most obviously change stay/booking truth do not use it.

Minimal trace:

```json
{
  "state_before": "Plan cross-trip rail says no stay or shows an old booking-session status. Map has no base unless an accommodation block exists in the itinerary.",
  "action": "User creates a stay from the accommodations screen, or confirms a booking cart.",
  "state_after": "The local accommodations/booking screen refreshes, but plan-state/home/map queries are not invalidated; Plan can keep stale cross-trip state and Map can still lack a base."
}
```

Repro or deterministic test idea:

1. Add a frontend unit test around `useCreateAccommodation`, `useUpdateAccommodation`, `useDeleteAccommodation`, and `useConfirmBookingCart` with a mocked `QueryClient`.
2. Assert that `invalidateTripReadModels(queryClient, tripId)` or equivalent invalidations fire.
3. Add a backend map-state test where `trip_accommodations` has a primary stay but the itinerary has no accommodation block.
4. Expected: Plan and Map can reflect the same primary stay source, or the product explicitly documents Map as itinerary-block-only.
5. Current likely/observed: only local accommodation/booking queries are invalidated; map-state cannot project trip accommodations.

Suggested fix direction:

Use `invalidateTripReadModels` from accommodation and booking mutations that change trip-visible truth. For Map, either project primary `trip_accommodations` into `TripMapState.base` when coordinates are available or document and test that Map only trusts itinerary accommodation blocks. The product spec points toward the former.

Related bug class:

Sibling read-model invalidation gap

Confidence: High for frontend invalidation gap; Medium for Map base behavior because it may be an intentional phase boundary, but it is not documented as such in the audited trace.

### P2 - Proposal Detail Uses Raw Affected Block IDs While Plan-State Uses Resolved Current IDs

Status: Confirmed  
User impact: After an itinerary fork, Plan can correctly highlight the current affected block for an open proposal, while the proposal review sheet opened from Home/Plan falls back to vague copy like "1 block on the itinerary (IDs will match once the live plan is loaded)." The tester sees one surface know the affected block and another surface fail to name it.  
Product promise affected: stable identifiers / plan coherence / proposal trust loop

References:

- `Travel Agent/backend/core/db/plan_state.py:710` - plan-state builds a forward chain for block IDs across accepted proposal forks.
- `Travel Agent/backend/core/db/plan_state.py:724` - plan-state maps open proposal IDs to current-version block IDs for block-level decorations.
- `Travel Agent/tests/api/test_plan_state.py:415` - backend test explicitly covers open proposal decoration surviving an intervening fork.
- `Travel Agent/tests/api/test_plan_state.py:504` - test asserts the open decision lists the current affected ID, not the stale pre-fork ID.
- `Travel Agent/backend/api/routes/proposals.py:628` - proposal detail response returns `affected_block_ids=proposal.affected_block_ids` directly.
- `Travel App/components/trip/ProposalReviewSheet.tsx:162` - proposal sheet builds its affected set from the raw proposal detail IDs.
- `Travel App/components/trip/ProposalReviewSheet.tsx:167` - proposal sheet matches those IDs against the legacy itinerary blocks.
- `Travel App/components/trip/ProposalReviewSheet.tsx:392` - when matches fail, the sheet shows only a generic affected block count.

Why it matters:

This is a stable-identifier contradiction rather than a missing feature. The backend plan-state path already solved stale block IDs after forks, but the proposal detail path and sheet do not consume that resolution. Home cards route by proposal id, Plan blocks decorate by current block id, and the sheet can lose the bridge between them.

Minimal trace:

```json
{
  "state_before": "Proposal A is open against block v1. Proposal B is accepted and applies, forking the itinerary to a current block ID.",
  "action": "User opens Plan, then opens Proposal A from the Home pending-decision card or Plan decision affordance.",
  "state_after": "Plan-state highlights the current block for Proposal A; ProposalReviewSheet receives raw v1 affected_block_ids and cannot name the affected current block."
}
```

Repro or deterministic test idea:

1. Reuse the backend fixture pattern from `test_open_proposal_block_decoration_survives_intervening_fork`.
2. Add a proposal detail or frontend sheet test where proposal detail has old `affected_block_ids` and plan-state/open decision has current IDs.
3. Expected: sheet names the current day/time/title using resolved affected IDs.
4. Current likely/observed: sheet falls back to the generic affected block count.

Suggested fix direction:

Add resolved/current affected IDs to `ProposalDetail`, or make `ProposalReviewSheet` consult `TripPlanState.open_decisions` by `proposalId` and use `decision.affected_block_ids` for current-plan matching. Keep raw IDs available only as provenance.

Related bug class:

Stale identifier across sibling read models

Confidence: High

## Non-Findings / Things Ruled Out

- Map null-coordinate handling is intentionally safe: backend emits stops with `point=null` and day-level unplaced notes, while the frontend filters markers to placed points and still renders list rows for unplaced stops.
- Tier-1 Home cards are protected from dismissal at the route layer: `booking_event` is tier 1 in policy and `POST /home_cards/dismiss` returns 409 for tier-1 archetypes.
- Heavy read models are generally offloaded from the event loop: plan-state uses `asyncio.to_thread`, map-state uses `run_in_executor`, and home feed DB helpers go through `_to_async`.
- Contract drift was not observed: OpenAPI snapshot, generated app types, HTTP coverage, mock/real parity, golden-path QA, and targeted home/plan/map tests all passed.

## Suggested Follow-Up Checks

- Add a backend regression test for Home feed cache invalidation across dismissal and proposal-resolution state changes.
- Add frontend mutation tests asserting booking and accommodation mutations invalidate `trip-plan-state`, `trip-map-state`, `trip-home-cards`, and `itinerary` where applicable.
- Add a cross-fixture test comparing `TripPlanState.days[].blocks[].id` to `TripMapState.days[].points[].block_id`, including one unplaced block and one open proposal.
- Add a proposal-review test proving affected block names still render when the proposal's raw affected IDs predate an itinerary fork.
