# Area 04 — Cross-Surface State Coherence

**Scope:** Home, Plan, Map, Concierge chat — the four surfaces a tester will flip
between when they say "the agent edited the trip in chat but the Map doesn't
know yet." Backend read models (`plan-state`, `map-state`, `home_cards`,
itinerary, conversations) and the frontend cache/invalidation layer that ties
them together. Plus the destination-identity handoff between Discover's trip
creation and the server-side trip row.

**Posture:** READ-ONLY. No code changed, no fixes attempted.

---

## Summary

Backend read models are healthy: `plan-state`, `map-state`, and `home_cards` all
derive from the same primitives (`itineraries` + `change_proposals` +
`trips.place_id` + `trips.trip_summary`). The single-source-of-truth invariant
holds — there is no read path that recomputes block placement or proposal
status independently. The proposal apply path (`/proposals/{id}/resolve`)
writes a `proposal_applied` / `proposal_apply_failed` event into `plan_events`
and updates `change_proposals.apply_status`, so the ledger is honest about
what actually committed.

The frontend cache layer is where the cross-surface incoherence lives. Three
real, demo-blocking issues:

1. **Home cards are never invalidated after a proposal apply/revert.** The
   shared helper `invalidateTripReadModels` covers `itinerary` + `trip-map-state`
   + `trip-plan-state` but **not** `trip-home-cards`. Combined with Home's
   `staleTime: 60_000`, the `pending_decision` banner on Home can lag the
   organizer's accept by up to a minute *and* the user has to leave/return to
   the tab to trigger the refetch.

2. **Destination/trip identity splits between `trip_summary.destination` and
   `trip.place_id`.** Discover's "start a trip from this card" path
   passes only the destination *string* — never `place_id` — so the server
   persists `trip_summary={"destination":"Paris"}` with `place_id=NULL`.
   Discover's For-This-Trip rail reads `trip_summary.destination` (works);
   Map's read model uses `trip.place_id` (broken — shows the no-destination
   placeholder); Home's `place_context` / `happening_nearby` cards are gated
   on `trip.place_id is not None` (broken — never appear). The tester sees a
   "Paris trip" everywhere except Map and Home, where it looks like a blank
   ideation trip.

3. **The plan-mutating tool allowlist in chat is a hardcoded `Set` of tool
   names.** A backend tool addition (or rename) silently disables Plan/Map
   invalidation on the chat path. There is no contract test pinning this list
   to the backend's actual mutating tools. Pair this with the mid-stream SSE
   failure path which never invalidates read models at all, and a flaky
   network during a `propose_change` turn produces a trip where the proposal
   exists in the backend but is invisible on Home, Plan, and the proposals
   list until manual refresh.

There are five additional P1/P2 issues across the optimistic-vote chat path,
the resolve modal's missing trust-status display, the in-flight 409 retry
ignoring read models, the Home `staleTime` floor on cross-surface lag, and the
fact that three separate invalidation callsites have drifted (each calls a
different subset of queries).

Mock-vs-real drift: useTripMapState seeds its placeholder with
`tripMapStateFromLegacyDays(tripId, mockItineraryDays)` (Lisbon mock pins),
so a brand-new real trip can briefly render Lisbon's mock pins on Map until
the real fetch resolves; everything else is symmetric.

---

## Findings

### [P0] — `invalidateTripReadModels` does not invalidate Home cards

**References:**
- `Travel App/utils/invalidateTripReadModels.ts:11-18` — the helper invalidates `itinerary`, `trip-map-state`, `trip-plan-state` only
- `Travel App/utils/queryKeys.ts:81` — `tripHomeCards(tripId) => ['trip-home-cards', tripId]` is the canonical key
- `Travel App/data/home.ts:81-85` — `useTripHomeCards` runs on `['trip-home-cards', tripId]` with `staleTime: 60_000`
- `Travel App/components/trip/ProposalReviewSheet.tsx:179-184` — call site for accept/revert/vote/forceRevert
- `Travel App/data/proposals.ts:49-60` — `useRevertProposal.onSuccess` calls `invalidateTripReadModels` and forgets Home
- `Travel App/hooks/useConciergeChat.ts:643-650` — agent-driven plan mutations call the same helper and also miss Home
- `Travel Agent/backend/home/feed.py:626-633` — `pending_decision` card in the active zone is derived from `get_trip_proposals(status='open')`

**Why it matters to a real tester:**
Organizer opens the ProposalReviewSheet from the Home `pending_decision`
banner, taps "Accept change", the modal closes. The user navigates to Home.
The same `pending_decision` card is still sitting there saying "Vote on
swapping dinner" even though the proposal is `accepted`/`applied`. Home stays
stale for the full 60s `staleTime` window, or until the user backgrounds and
reopens the app. This is the *exact* scenario the
`home-plan-map-coherence.md` trace was written to catch.

**Repro / deterministic test idea:**
A jest test using a mocked `queryClient` that records every
`invalidateQueries` call, then asserts that after calling
`invalidateTripReadModels(qc, tripId)` the call list includes
`['trip-home-cards', tripId]`. Alternatively, the existing
`__tests__/components/plan/ProposalReviewSheet.test.tsx` can grow an
assertion that on `resolveMutation` success, `queryKeys.tripHomeCards(tripId)`
is in the invalidated set.

**Suggested fix direction:**
Add one line — `queryClient.invalidateQueries({ queryKey: ['trip-home-cards', tripId] });` — to `invalidateTripReadModels`. Since `home_cards` derives from `proposals` + `itinerary` + `digests`, anywhere that invalidates Plan/Map after a mutation has the same need for Home. Keep the helper as the single chokepoint; do not push the call up into each callsite (the three current callsites already diverge — see TECH-DEBT below).

**Confidence:** High

---

### [P0] — Destination identity splits between `trip_summary.destination` and `trip.place_id`

**References:**
- `Travel App/app/(tabs)/discover/index.tsx:458-478` — destination-card create passes `{ title: destination, destination }`; never `place_id`
- `Travel App/context/TripContext.tsx:252-348` — `createTrip` action; only forwards `destination` string to `api.createTrip`
- `Travel Agent/backend/api/routes/trips.py:86-92` — `CreateTripRequest.destination` is the only destination-shaped field accepted
- `Travel Agent/backend/api/routes/trips.py:391` — persisted as `trip_summary={"destination": body.destination}`; `place_id` stays NULL
- `Travel App/components/for-this-trip/ForThisTripPreview.tsx:68` — Discover/For-This-Trip reads `currentTrip.trip.trip_summary.destination` (works in this surface)
- `Travel Agent/backend/api/routes/trips.py:884-892` — Map endpoint uses `trip.place_id` exclusively; when NULL, returns `destination=None`
- `Travel Agent/backend/core/map_state/builder.py:144-186` — produces the "Map improves once this trip has a destination." spatial note when `place_id is None`
- `Travel Agent/backend/home/feed.py:534-541,859-907` — `destination_name`, `happening_nearby`, and `place_context` cards all gated on `trip.place_id is not None`

**Why it matters to a real tester:**
Tester taps a "Paris" destination card on Discover → app routes into the new
trip's concierge chat → the trip header says Paris, the For-This-Trip rail
fills with Paris angles. They open Map: "Map improves once this trip has a
destination." They open Home: no Paris context card, no Paris happening-nearby
ambient. The trip *looks like* a Paris trip on one surface and an undestined
ideation trip on two others. This is the most visible cross-surface
incoherence in the audit because it ships on the *first impression* of every
destination-card-originated trip.

**Repro / deterministic test idea:**
Add to `__tests__/utils/tripMapStateParity.test.ts` (or a new
`destinationParity.test.ts`): create a trip via `api.createTrip({ destination: 'Paris' })`,
then assert that `getTripMapState(tripId).destination` is non-null when the
trip has *either* `place_id` set *or* `trip_summary.destination` set. Will
fail today on the second case. A backend-side fix is the natural place — the
endpoint should fall through to a slug-based `place` lookup when `place_id`
is NULL but `trip_summary.destination` is set.

**Suggested fix direction:**
Two complementary paths, both small:
1. *Frontend*: in `discover/index.tsx`, resolve the slug to a `place_id` via
   the existing `places` lookup before calling `createTrip`. The slug is
   already in hand (`tripPlaceSlug` is derived two lines above the create
   call's caller). When `place_id` is in the request body, the bug
   disappears.
2. *Backend* (defense in depth): in `get_trip_map_state` and the Home feed's
   destination-resolution path, fall back to
   `get_place_by_slug(trip.trip_summary.get("destination"))` when
   `trip.place_id is None`. This catches every trip whose
   `trip_summary.destination` came from a non-Discover surface
   (concierge promote, intent_tracking, manual title entry).

**Confidence:** High

---

### [P1] — Hardcoded plan-mutating tool allowlist in chat invalidation

**References:**
- `Travel App/hooks/useConciergeChat.ts:622-650` — `_PLAN_MUTATING_TOOLS` Set is the gate that decides whether to call `invalidateTripReadModels`
- The Set's members: `add_stop, remove_stop, update_stop, reorder_stops, add_to_plan, update_plan, update_itinerary, schedule_activity, propose_change, apply_proposal, create_booking, confirm_booking, cancel_booking`
- `Travel Agent/backend/concierge/tools.py` — actual mutating-tool registry on the backend
- `Travel Agent/backend/concierge/tool_handlers/planning.py:~950` — `generate_plan` writes plan state via the planning handoff

**Why it matters to a real tester:**
The agent gains a new mutating tool (or an existing one is renamed) — say
`update_block_time`, `swap_block_venue`, or `pin_experience` if it ever lands
plan rows. The FE's Set falls out of sync silently. The chat returns
"Updated your Tuesday afternoon", the chat history refetches and shows the
agent's reply, but Plan/Map don't refetch and the user sees the old block
until they refocus a tab. There is no test pinning this list to the backend.
The trace's `proposal_apply` / `propose_change` are in the list today, so the
common path works, but the moat is paper-thin.

**Repro / deterministic test idea:**
A workspace-level script (akin to `scripts/api-coverage-check.py`) that
introspects backend `tools_schema.py` (or whatever registers tool names + the
"mutating" flag) and asserts every tool flagged mutating appears in
`_PLAN_MUTATING_TOOLS` on the FE. Fails on drift.

**Suggested fix direction:**
Short-term: move the Set into a generated module (`utils/api/mutatingTools.gen.ts`) emitted alongside `schema.gen.ts`. Long-term: have the backend stamp `metadata.plan_mutated: true` on the SSE metadata frame whenever the turn called *any* mutating tool, and have the FE branch on that single flag instead of pattern-matching tool names.

**Confidence:** High

---

### [P1] — `useConciergeChat.voteOnProposal` only invalidates chat history; misses proposals, plan, home

**References:**
- `Travel App/hooks/useConciergeChat.ts:890-906` — chat-vote handler calls `api.voteOnProposal` then `invalidateQueries({ queryKey: queryKeys.chatHistory(tripId) })`
- `Travel App/components/trip/ProposalReviewSheet.tsx:186-221` — the *other* vote path invalidates correctly via `invalidateProposalQueries` (proposals list + detail + chat history + read models)
- `Travel Agent/backend/api/routes/proposals.py:40-44` — `VoteRequest` endpoint; votes update `change_proposals.votes` which is read by Plan v2 `open_decisions[].votes` and by Home's `pending_decision` card

**Why it matters to a real tester:**
A user has both Plan and a `vote_widget` inline card in chat open. They tap
"Approve" on the chat card. The chat history refetches and shows the
acknowledgement. They switch to Plan: the open-proposals banner still shows
the old tally. They switch to Home: the `pending_decision` card still says
"needs your vote". They switch back to chat and re-tap, confused. The
ProposalReviewSheet path handles this correctly; the chat path doesn't. Two
vote surfaces, two different invalidation contracts.

**Repro / deterministic test idea:**
Mock the chat hook in a jest test, fire `voteOnProposal('prop_1', 'approve')`,
assert the invalidated keys include `tripProposals(tripId)`,
`tripProposalsOpen(tripId)`, `tripPlanState(tripId)`, `tripHomeCards(tripId)`.

**Suggested fix direction:**
Have `voteOnProposal` (and the analogous `reactToMessage` for structured
cards that mutate state) delegate to the same `invalidateTripReadModels` +
proposal-prefix invalidation that `ProposalReviewSheet` uses. The right
shape is a shared `invalidateAfterProposalMutation(qc, tripId, proposalId)`
helper that the two callsites and the SSE metadata branch all consume.

**Confidence:** High

---

### [P1] — Mid-stream SSE failure or aborted turn never invalidates plan/map/home even when the backend committed the mutation

**References:**
- `Travel App/hooks/useConciergeChat.ts:707-723` — hard `onError` branch marks messages failed; no `invalidateTripReadModels` call
- `Travel App/hooks/useConciergeChat.ts:724-781` — `onDone` no-metadata fallback marks both bubbles failed; also no read-model invalidation
- `Travel App/hooks/useConciergeChat.ts:668-705` — `in_flight` 409 retry loop polls `chatHistory` / `conversationMessages` only
- `Travel App/hooks/useConciergeChat.ts:834-861` — `stopStreaming` (user-initiated abort) does not invalidate anything

**Why it matters to a real tester:**
User asks the concierge to swap a venue. The backend turn runs, the planner
calls `propose_change`, the proposal row is written, and the `proposal_created`
plan_event lands. *Then* the SSE connection drops before the `metadata` frame
hits the device — flaky cafe wifi, app backgrounded, the user tapped Stop.
The UI marks the bubble failed and exits the streaming state. The user pulls
to refresh on Plan: nothing new (because Plan never re-fetched and the
backend write only emitted the proposal_event, not the metadata frame).
Home: no `pending_decision` card. Proposals list: empty. The user concludes
the agent didn't do anything and tries again; the second turn either dedupes
via the idempotency key or duplicates the proposal.

**Repro / deterministic test idea:**
Mock streamSSE to fire `onError('Connection dropped', 'error')` after
`onToolStatus` but before `onMetadata`. Assert the test fixture's
`queryClient.invalidateQueries` call log includes `['trip-plan-state', tripId]`
(it won't today). Same test with `onDone` without a preceding `onMetadata`
call to cover the no-metadata fallback.

**Suggested fix direction:**
In every failure branch where the turn could have completed server-side
(`in_flight`, `timeout`, mid-stream onError, no-metadata onDone, user abort
*after* `tool_started`), call `invalidateTripReadModels(queryClient, tripId)`
+ proposals prefix invalidation. The cost is one extra background fetch on
recovery; the alternative is a silently-divergent client. Pair with finding
#4's shared helper so the contract is in one place.

**Confidence:** High

---

### [P1] — `resolveMutation` closes the modal before the apply outcome is visible to the organizer

**References:**
- `Travel App/components/trip/ProposalReviewSheet.tsx:223-230` — `resolveMutation.onSuccess` invalidates and immediately calls `onClose()`
- `Travel App/components/trip/ProposalReviewSheet.tsx:331-338,499-521` — the `TrustStatusBanner` that distinguishes "Applied to Plan" vs "Needs organizer review" requires the modal stay open to render
- `Travel Agent/backend/api/routes/proposals.py:372-422` — server can set `apply_status='failed'` with an error message; the FE has full UI for this state but the user never sees it

**Why it matters to a real tester:**
Organizer taps "Accept change" → spinner → modal closes → user sees the trip
home screen. The proposal was accepted but `apply_accepted_proposal` raised
or returned no new itinerary version, so `apply_status='failed'` and the
itinerary did NOT actually change. The user has no signal anything went
wrong — Plan looks the same as before (because nothing changed), Home's
`pending_decision` card is gone (because the proposal is no longer `open`).
The organizer believes the change shipped to the group and only learns
otherwise when a member asks why the dinner spot hasn't moved.

**Repro / deterministic test idea:**
In `__tests__/components/plan/ProposalReviewSheet.test.tsx`, mock
`api.resolveProposal` to return a proposal with
`status: 'accepted', apply_status: 'failed', apply_error: '…'`. Assert that
the modal stays visible long enough to surface the failure banner — today
the test will catch the modal closing immediately.

**Suggested fix direction:**
On `resolveMutation.onSuccess`, branch on `data.apply_status`: if
`'succeeded'` close immediately (current behavior, correct); if `'failed'`
leave the modal open so `TrustStatusBanner` renders the
`applyFailedBanner` block with the actionable "Try again, or revert and
re-propose" copy. Even a toast on close ("Plan update needs review — re-open
the proposal") would close the loop.

**Confidence:** High

---

### [P2] — `staleTime: 60_000` on Home cards is the floor on cross-surface lag

**References:**
- `Travel App/data/home.ts:83` — `useTripHomeCards` uses `staleTime: 60_000`
- `Travel App/data/proposals.ts` — `useOpenTripProposals` has no staleTime (default 0; refetches on focus)
- `Travel App/data/planState.ts` — `useTripPlanState` has no staleTime (default 0)
- `Travel App/data/map.ts` — `useTripMapState` has no staleTime (default 0)

**Why it matters to a real tester:**
Even when the P0 finding above is fixed and Home invalidation is plumbed in,
`staleTime: 60_000` means a subsequent focus *within the window* will read
stale cache instead of refetching — invalidation only marks the query stale,
it doesn't force the next read to wait. The four read models are now on
different freshness contracts (3 zero, 1 sixty seconds), so the worst-case
cross-surface lag for a Home refetch is bounded by 60s in the common
"tap accept → switch tab" case.

**Repro / deterministic test idea:**
Render the Home screen, fire a mutation that should invalidate
`trip-home-cards`, advance jest fake timers by 30s, re-mount the Home query
client consumer. Today, the refetch fires only because invalidate marked it
stale AND mount triggers a network call. In a real session where the
consumer is already mounted and the tab is just being re-shown, `staleTime`
will silence the refetch.

**Suggested fix direction:**
For surfaces that need to be coherent with mutations (Home, Plan, Map),
drop `staleTime` to the default (0). The cost is a refetch on every focus —
real, but small (`home_cards` is the most expensive due to the LLM-composed
anchor; this is exactly what the `staleTime: 60_000` was paying for).
Alternative: keep the `staleTime` but pair every `invalidateQueries` with
`refetchQueries({ queryKey, type: 'active' })` so an active consumer
re-fetches immediately rather than waiting for stale.

**Confidence:** Medium

---

### [P2] — `useTripMapState` placeholder shows mock Lisbon pins for any tripId during the first real fetch

**References:**
- `Travel App/data/map.ts:48-58` — `mockSnapshot` is `tripMapStateFromLegacyDays(tripId, mockItineraryDays)` regardless of which trip is loading
- `Travel App/constants/mockData.ts` — `mockItineraryDays` is the canonical Lisbon mock with hard-coded pins

**Why it matters to a real tester:**
User creates a brand-new trip (real mode) and immediately taps Map. Between
mount and the real fetch resolving, the map renders the placeholder built
from `mockItineraryDays` — which are Lisbon's pins. For ~200-800ms the
tester sees Lisbon markers on a "Paris" trip. The error branch correctly
clears (`emptyTripMapState`), the loading branch doesn't.

**Repro / deterministic test idea:**
A jest test that mounts `TripMapScreen` with a never-resolving
`api.getTripMapState` (manual control over the promise). Assert that no
markers from `mockItineraryDays` appear in the initial render.

**Suggested fix direction:**
Use `emptyTripMapState(tripId)` as the placeholder in real mode and reserve
the `tripMapStateFromLegacyDays(...)` snapshot for mock mode only. The
`useData` mock/real toggle (`hooks/useData.ts:42`) already has the
information needed to branch.

**Confidence:** Medium

---

### [TECH-DEBT] — Three invalidation callsites for the same logical event, each with a different coverage set

**References:**
- `Travel App/utils/invalidateTripReadModels.ts:11-18` — covers itinerary, map, plan (misses home, proposals)
- `Travel App/components/trip/ProposalReviewSheet.tsx:179-184` — covers trip-proposals, trip-proposal (detail), groupChatHistory, then delegates to the shared helper
- `Travel App/data/proposals.ts:49-60` — `useRevertProposal` covers trip-proposals, all-trip-proposal-details, then delegates to the shared helper
- `Travel App/hooks/useConciergeChat.ts:643-650` — covers chatHistory, conversationMessages, trip-proposals, then delegates to the shared helper

**Why it matters to a real tester:**
Today these three callsites *almost* invalidate the same set but each is
missing different things (no Home anywhere; chat path misses proposal
detail; sheet path misses open-only proposals key). A future bug fix to
one callsite (e.g. "we forgot to invalidate Foo") has to be re-applied at
three sites, with high probability of drift. This is the structural reason
findings 1, 4, and 5 above all exist — the contract is implicit and
duplicated.

**Repro / deterministic test idea:**
A unit test that, for each of the three callsites, asserts the union of
invalidated keys matches a single canonical set. Today they don't.

**Suggested fix direction:**
Introduce `invalidateAfterPlanMutation(qc, tripId, opts?)` and
`invalidateAfterProposalMutation(qc, tripId, proposalId, opts?)` as the
canonical two helpers, each covering the full read-model surface (itinerary,
map, plan, home, proposals list + detail, chat history). Delete the
three ad-hoc invocations in favor of one of these two. Test the canonical
set once; every callsite is then provably correct by construction.

**Confidence:** High

---

## Known / Accepted

These are documented gaps from the Known Gaps Register and the
`home-plan-map-coherence.md` / `proposal-review-and-plan-mutation.md` traces
that this audit explicitly does NOT escalate. Each is either intentionally
deferred or non-blocking for dogfood.

- **O-9 (Tier 3 eval mocks DB writes)** — accepted design tradeoff
  (2026-05-16). Cross-surface coherence is enforced by the backend pytest
  suite + the frontend invalidation helpers, not the eval harness. The eval
  patching `create_change_proposal` / `proposal_automation._do_resolve`
  means the eval cannot regression-gate the chain "agent calls `propose_change`
  → `change_proposals` row exists → Plan banner shows it" end-to-end; the
  jest tests in `__tests__/data/proposals.test.ts` and the API tests in
  `tests/api/test_proposal_apply.py` cover the two ends separately. Accept
  the gap.

- **Cross-fixture Plan ↔ Map id assertion (trace gap)** —
  `home-plan-map-coherence.md` lists "Add one cross-fixture test that compares
  Plan block ids to Map item ids." Not yet wired. Out of scope for this
  read-only audit; the recommendation stays in the trace.

- **Multi-client SSE push** — There is no push channel for Plan / Map / Home
  updates between members of a group trip. If Alice accepts a proposal, Bob's
  device only learns when Bob refocuses a tab (`refetchOnWindowFocus`) or
  sends a chat message himself. Out of scope for single-client surface
  coherence; flagged here so it is not mistaken for a finding above. Backend
  SSE is currently `chat`-only and `narration`-only
  (`backend/api/routes/chat.py:308`, `backend/api/routes/narration.py:592`).

- **`useTripHomeCards` LLM-composed anchor latency** — the 60s `staleTime` on
  Home was chosen because the anchor voice line is composed by Haiku at
  request time. Finding [P2] above recommends dropping it; the tradeoff
  (Haiku cost per focus event) is the explicit reason that staleTime was set.
  Mention the tradeoff in any fix PR; do not drop staleTime without the cost
  conversation.

- **`apply_status='failed'` recovery (P1-6 from previous audit)** — backend
  already records the failure honestly (`apply_status: 'failed'`,
  `apply_error: '…'`) and `TrustStatusBanner` renders the actionable UI. The
  P1 finding above ([resolveMutation closes the modal]) is the *new* gap on
  top of this — the backend half is healthy, the frontend orchestration
  defeats it.

- **G-9 (concierge routes disruption replans to `search_restaurants`)** —
  separate concern about which tool the agent chose, not about cross-surface
  invalidation. When `generate_plan` *does* run, the existing FE
  invalidation chain handles it correctly (it's in `_PLAN_MUTATING_TOOLS`).
  The G-9 stochasticity has no cross-surface coherence component.
