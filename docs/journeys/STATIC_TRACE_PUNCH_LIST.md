# Static Trace Punch List

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Source of truth for: consolidated findings from 12 parallel journey traces

This report consolidates read-only static traces for all 12 canonical journeys. Agents traced each journey through app routes, components, hooks, API methods, mock fallbacks, and backend endpoints. No live LLM-backed product endpoints, push sends, provider calls, or photo-library actions were used.

## Fix Pass - 2026-06-06

Completed in the first bug-elimination pass:

- Journey 07: backend conversation streaming now accepts and forwards client `metadata`, including `metadata.conversation_seed`.
- Journey 10: booking session routes now preserve `tripId`; backend booking session, offer, cart, restaurant-attempt, and refresh routes enforce `session.trip_id == trip_id`; cart confirm no longer auto-creates shared expenses.
- Journey 01: real-mode concierge prefill waits for a trip id or conversation id before auto-sending; forced conversation promotion can explicitly crystallize a home conversation.
- Journey 02/03/12: trip-home CTAs for pending invites, legacy group state, and settlement closeout now preserve `tripId`.
- Journey 11: Atlas privacy no longer self-loops; the receipt screen no longer labels a Travel Identity link as another full receipt.

Still open after this pass: privacy redaction for booking/notification copy, proposal deep-links/idempotency/read-model coherence, live-trip CTA contracts, mock read-model parity, and full mock walks for all 12 journeys.

## Fix Pass - 2026-06-06, Tranche 2

Completed in the privacy/proposal/mock-coherence pass:

- Journey 04: added deterministic private-signal redaction for notification preview/fan-out content and booking proposal notes before they are stored or handed to booking sessions.
- Journey 05: pending vote notifications now carry `proposal_id` and route into the trip proposal review entry point instead of generic trip detail.
- Journey 05: proposal vote/resolve/revert calls now send idempotency keys from both hook-based flows and the proposal review sheet.
- Journey 06: mock proposal detail, itinerary, map-state, plan-state, open decisions, and recent changes now share the same canonical Lisbon block/proposal ids for accept/revert flows.

Still open after tranche 2: richer privacy receipt/audit events for private-constraint use, backend proposal notification payloads beyond pending-vote feed rows, live-trip CTA contracts, and full mock UI walks.

## Fix Pass - 2026-06-06, Tranche 3

Completed in the privacy-proof/proposal-receipt/cross-surface regression pass:

- Journey 04: privacy audit now renders `private_detail_redacted` and `private_constraint_used` proof events from the existing privacy warehouse without echoing raw private values.
- Journey 04: redacted notification previews and booking proposal notes now write privacy-proof events with surface/count metadata.
- Journey 05: proposal detail responses and plan-event ledger entries now include structured `proposal_receipt` payloads for accepted, applied, failed-apply, rejected, withdrawn, superseded, and reverted outcomes.
- Journey 05/06: mock Home cards and notification pending votes now follow the canonical proposal status, so accept/revert coherence is visible across Home, Plan-state, Map-state, Changes, and Notifications.
- Journey 05/06: added regression coverage for Plan recent-change chips, Changes rows, Home needs-you/deep-linked proposal review, Notifications proposal routing, Map read-model parity, and cross-surface mock accept/revert.

Still open after tranche 3: full deterministic private-constraint fixture across every group-visible surface, real-backend proposal accept/apply/revert canary, live-trip CTA contracts, and non-canonical proposal parity.

## Fix Pass - 2026-06-06, Tranche 4

Completed in the real-backend proposal canary pass:

- Journey 05: added a Postgres-backed dogfood canary that seeds a real group trip/proposal, accepts/applies/reverts through the production proposal API, and verifies proposal detail receipts, Plan open decisions/recent changes, Home pending-decision cards, member pending-vote notifications, Map stop timing/block ids, and group-chat apply/revert receipts stay coherent.
- Journey 05/06: the canary explicitly asserts the post-apply `applied_block_map` old-id to current-id transition, which is the hidden source of many Plan/Map/Changes mismatches after itinerary forking.
- Journey 05: the current backend assertion covers the Changes surface through the Plan recent-changes read model; the remaining promotion step is an app-level walk proving the visible Changes screen renders the same backend truth.

Still open after tranche 4: full deterministic private-constraint fixture across every group-visible surface, app-level Changes walk for the real proposal canary, live-trip CTA contracts, and non-canonical proposal parity.

## Fix Pass - 2026-06-06, Tranche 5 (Trips home + live companion)

Completed in the global Trips home / J08 grounding pass:

- **Trips home P4:** PlanningPiece tiles, While-you're-here / HomeNearYou rows, live tile routing, Save a moment → Memory, `conciergeSeed` on trip-begin, Maestro state pack (live/cold/planning/returned/between/urgent personas).
- **J01:** `PromoteToTripResponse` mock/real contract alignment + offline promotion tests.
- **J08/J12:** Trip folio + Memory screens ground phase/content on route `tripId`; LiveHome CTA offline walk; global `happening_nearby` opens `ExperienceDetailSheet`.
- **Backend:** `GET /api/me` exposes `home_city` / `home_neighborhood` from traveler profile summary.

Still open after tranche 5: Vesper Home live-mode walk, Map-from-live focus walk, workspace chat/map sub-routes that still prefer `currentTrip`, Journey 01 prefill-wait screen test, HomeNearYou editorial fallback row routing, and full mock UI walks for all 12 journeys.

## Executive Read

The app is not blocked by one giant missing feature. It is blocked by a set of cross-surface trust failures:

- Context is often held in `currentTrip` instead of route params or structured seeds.
- Mock data frequently proves a nicer world than real backend contracts support.
- Several privacy-sensitive copy paths bypass deterministic redaction.
- Proposals, notifications, Atlas, booking, and post-trip surfaces do not always invalidate or route back to the same object.
- Some CTAs are visually promising more than they can do.

## Highest Priority Blockers

| Priority | Journey | Finding | Why it matters |
|---|---|---|---|
| P0 fixed | 07 Discover | ConversationSeed metadata is sent by the app but dropped by backend conversation-stream request parsing. | Ask Vesper from Discover/detail can reach the agent as generic chat. |
| P0 fixed | 10 Booking | Booking session route drops `tripId`, and backend booking session/offer/cart routes lack session-trip ownership checks. | Booking can be stranded or cross-trip unsafe. |
| P0 fixed | 10 Booking | Cart confirmation auto-logs shared expenses without organizer opt-in. | Violates the booking/privacy promise around financial sharing. |
| P0 fixed | 01 Cold Ideation | `/trip-begin` Vesper starts use home conversation, while backend promotion rejects home conversations. | Vague idea -> promoted trip can fail in the core first-use journey. |
| P0 fixed | 01 Cold Ideation | Real-mode prefill can be swallowed before home conversation id resolves. | User taps a starter and lands in chat with no sent prompt. |
| P1 fixed | 04 Privacy | Booking proposal notes and notification previews lack deterministic redactor boundaries. | Private constraints can leak through booking/notification copy. |
| P1 fixed backend / UI follow-up | 05 Proposals | Proposal notifications/receipts now deep-link/carry structured payloads, and the real-backend accept/apply/revert canary passes across backend read models. | Remaining risk is the visible app Changes surface, which still needs a backend-backed UI walk. |
| P1 | 08 Live Trip | Live/on-trip CTAs and route grounding on global Trips home + folio/Memory largely fixed (2026-06-06 tranche 5). Remaining: Vesper Home live mode, Map focus from live context, chat sub-route drift. | Live trip use can feel broken exactly when stakes are highest. |
| P1 fixed | 11 Atlas | Atlas privacy/receipt routes self-loop or route to generic portraits; `/api/atlas/places` was missing. | Fixed 2026-06-06: receipt/identity routing and `GET /api/atlas/places` backend route. |
| P1 partial | 12 Post-Trip | Settlement closeout drops `tripId`; Memory depended on `currentTrip`. | Memory route grounding fixed 2026-06-06; Story route + post-trip fixtures still drift. |

## Per-Journey Findings

### 01 - Vague Idea To Vesper-Shaped Trip

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06: forced promotion can crystallize a home conversation when the user explicitly chooses to promote it.
- Fixed 2026-06-06: real-mode prefill waits until a trip id or active conversation id exists before auto-sending.
- Mock `promoteConversationToTrip` returns an `APITrip`, while real backend returns `{ trip_id, conversation_id, place_resolution, members_copied }`.
- Promotion metadata invalidates chat history/conversation messages but not the full user conversation list/history.
- Missing tests: real-mode prefill wait, starter -> private chat prompt, streamed `promoted_trip_id` handling, backend promotion response contract.

Next action: add prefill/promotion regression tests and align mock/real promotion response shape.

### 02 - Concrete Trip Creation And Invite

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06: pending invite follow-up cards route to `/trip-info?tripId=...`.
- Invite accept routes to group chat, while the journey automation target expected trip detail; product/docs/tests need alignment.
- TripInfo invite mint opens share sheet but does not refresh the pending invite list.
- Mock invite tokens encode a trip id, but mock view/accept ignore it and return the first mock trip.
- `activeOnly` contract says expired invites are omitted, while backend/mock only filter revoked/consumed.
- Missing tests: create trip -> invite -> landing -> accept -> member count -> final route; auth detour return; expired/consumed invite handling.

Next action: fix mock token/member mutation and tripId-preserving invite-management routes, then add the screen-level mock walkthrough.

### 03 - Cold Trip Setup To Useful Workspace

Static trace: partial. Dogfood ready: no.

- Trip Folio renders from `TripContext.currentTrip`, while `useTripSettings` updates React Query caches; mock mode can leave cold mode stale after setup.
- Place setup is chat/LLM-mediated, not deterministic `patchTrip`.
- Fixed 2026-06-06: the known trip-home `tripInfo()` / `tripExpenses()` CTAs now preserve `tripId`.
- Mock accommodations do not persist realistic stay mutations.
- Missing tests: blank -> patch dates/place -> reload -> pre workspace; setup links preserve `tripId`; stay facet persistence.

Next action: make Journey 03 deterministically mockable or explicitly mark place resolution as a real-backend canary.

### 04 - Private Constraint To Group-Safe Plan

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06 tranche 2: booking proposal notes are deterministically scrubbed before persistence/handoff.
- Fixed 2026-06-06 tranche 2: notification snippets and channel fan-out content use deterministic private-signal redaction.
- Plan UI can display `private_constraint_influenced`, but backend read-model generation does not appear to emit it.
- Private concierge trip scoping depends on selected trip/conversation, not a route `tripId`.
- `composition_failed` SSE transparency is not clearly persisted/rehydrated into history.
- Privacy audit currently focuses on sensor/privacy events, not “private constraint used in group-safe planning.”
- Missing tests: private constraint fixture across group chat, proposal, notification, booking, plan badge, Atlas/privacy receipt.

Next action: add privacy receipt/audit events for “private constraint used safely” and broaden fixtures across group chat, proposal, notification, booking, plan badge, and Atlas.

### 05 - Group Planning To Proposal To Plan Mutation

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06 tranche 2: pending-vote notifications carry `proposal_id` and route to the trip proposal review entry point.
- Group-chat notification cards pass `reference_id`, but chat parses only numeric venue ids.
- Fixed 2026-06-06 tranche 2: frontend proposal vote/resolve/revert calls send idempotency keys.
- Fixed 2026-06-06 tranche 2: mock accept/revert mutates proposal status plus canonical itinerary, plan-state, map-state, and recent changes around `block-1` / `MOCK_PROPOSAL_A`.
- Fixed 2026-06-06 tranche 3: backend proposal details and plan-event ledger entries carry structured lifecycle receipt payloads.
- Fixed 2026-06-06 tranche 4: real-backend canary accepts/applies/reverts a reschedule proposal through the production API and verifies proposal detail, Plan/Changes source read model, Home, Map, Notifications, and chat receipts agree.
- Group-chat votes are no-ops in mock mode.
- Proposal read-model invalidation does not include notification feed.
- Missing tests: app-level backend-backed Changes screen walk, group-chat vote behavior in mock mode, notification-feed invalidation around non-canonical proposals.

Next action: promote the real-backend proposal canary into the standing dogfood/CI gate, then layer an app-level Changes screen walk over the same lifecycle.

### 06 - Home, Plan, Map, Changes Coherence

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06 tranche 2: canonical mock proposal/read-model ids now align for the main Lisbon proposal flow.
- Fixed 2026-06-06 tranche 2: mock `getTripPlanState` now returns days/blocks/open decisions/recent changes derived from the same itinerary/proposal state.
- Fixed 2026-06-06 tranche 2: mock proposal accept/revert mutates the read models users see.
- Home fetches backend `home_cards`, but visible Home CTA uses open proposals directly.
- Map no-native-Mapbox fallback says “Use the stop list below” but returns before rendering it.
- Unplaced focused map blocks silently fail to move the camera.
- Changes rows without proposal source have no deterministic route back to affected block/map focus.
- Missing tests: fixture parity `PlanBlock.id <-> MapStop.block_id <-> PlanChange.affected_block_ids`; mock read-model coherence; route-back for changes.

Next action: expand parity beyond the canonical proposal to remaining mock proposals, Home cards, and route-back behavior for changes.

### 07 - Discover To Contextual Vesper To Trip Action

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06: backend conversation stream request exposes `metadata` and forwards it as turn metadata.
- Fixed 2026-06-07: `utils/discoverRouting.ts` centralizes card/search/detail → ConversationSeed handoffs; Discover no longer clears trip before Ask Vesper; search fallbacks carry entity/clientContext; dossier/guide/angle include `tripId`; share-with-group surfaces toast when no trip.
- Fixed 2026-06-07: venue take `ask_concierge` with active trip routes to group chat via `tripChatSeed` (structured venue entity + auto-send on mount); `useGroupChat.sendMessage` accepts metadata like private concierge.
- Fixed 2026-06-07: mock discover API — search returns venues/angles/dossiers/experiences/accommodations/sites; `listCollections`/`getCollection` wire to `mockGuides`; `getVenueBriefs` returns Lisbon venue excerpts.
- Fixed 2026-06-07: Discover full-stack parity — compose maps site/accommodation for-you rows; `POST /api/search` indexes angles/dossiers; experience cards open `ExperienceDetailSheet`; trending HTTP fetch retired; for-you dismiss/show wired on feed cards.
- Fixed 2026-06-07: `GET /api/discover/feed` accepts `exclude_surface_ids`; client passes dismissed surfaces and refetches instead of only client-filtering sections.
- Fixed 2026-06-07: Discover search overlay prefers API `angle`/`dossier` rows; client `matchDossiers` is mock-mode fallback only.
- Tests: `__tests__/utils/discoverRouting.test.ts` — card navigation, seed matrix, search handoffs, trip vs private channel split, group ask seed routing.
- Tests: detail surface smoke — `venue-detail`, `dossier-detail`, `guide-detail`, `angle-detail` assert seed/trip routing on Ask Vesper.
- Tests: `__tests__/journeys/journey-07-mock-walk.smoke.test.tsx` — feed dismiss, experience handoff, group-chat seed contract.
- Tests: `__tests__/components/DiscoverSearchOverlay.editorial.test.tsx` — API reads vs dossier fallback.
- Tests: `travel-agent/tests/discover/test_discover_feed_api.py` — `exclude_surface_ids` forwarded to compose; `travel-agent/tests/api/test_search_api.py` — editorial reads merge.
- Remaining: live-backend canary on seeded discover feed dismiss + editorial search; no-trip `share_with_group` still toast-only.

### 08 - Live Trip What-Now Companion

Static trace: partial. Dogfood ready: blocked.

- Vesper on-trip “Save a moment” routes to Atlas, not a capture flow.
- “Something else?”, urgent queue affordances, and “Reorder” are visually suggestive but incomplete.
- Backend card actions lack `open_map`, `open_today`, or `open_block`; live cards can lose intended routing.
- Group chat ignores route `tripId` and depends on `currentTrip`.
- Trip Folio fetches by route `tripId` but computes phase/live day from `currentTrip`.
- Private Vesper Chat parses `seed.tripId` but grounding still derives from selected trip.
- Mock `trip-lisbon-26` is not actually live in `getTripSituation`/plan-state, and mock itinerary is October 2026.
- Multiple surfaces disagree on current/next source of truth.
- Missing tests: live CTA action matrix, route `tripId` cold deep links, seed trip grounding, cross-surface current/next agreement.

Next action: fix/de-afford live CTAs, align tripId/seed grounding, and make the live mock fixture actually live.

### 09 - Notifications And Proactive Routing

Static trace: ready with gaps. Dogfood ready: no.

- Feed tap routing mostly implements the priority matrix; OS push tap routing does not.
- PushRegistrar ignores `outcome_id + trip_id` payloads without `conversation_id`.
- Social feed taps route through `routes.people()` / old Me route, not `/atlas/companions`.
- Push `booking_event` / `shares_settled` can route to `/trip-expenses` without `tripId`.
- Private proactive routing uses generic private chat, not explicit `conversation_id`.
- “Mark all as read” only covers unread concierge conversation ids.
- Proactive tap does not immediately invalidate the notifications query.
- OpenAPI/types lag backend proactive `conversation_id`.
- Missing tests: PushRegistrar route-priority matrix; proactive read invalidation; missing `trip_id` fallbacks.

Next action: add OS push routing tests and make push routing use the same priority matrix as feed taps.

### 10 - Booking, Stay, And Expense Trust Loop

Static trace: partial. Dogfood ready: blocked.

- Fixed 2026-06-06: `routes.bookingSession(tripId, sessionId)` preserves both params.
- Fixed 2026-06-06: backend booking session/offer/cart/restaurant-attempt endpoints verify `session.trip_id == trip_id`.
- Fixed 2026-06-06: cart confirmation no longer auto-logs shared expenses immediately.
- Stay create/update/delete are UI-gated by organizer, but backend only checks trip membership.
- Booking confirmation may not write hotel stay state because selected offers are not marked `confirmed`.
- Refresh offer CTA is wired to a backend 501.
- Mock accommodations/booking/offers/cart are too empty to test the trust loop.
- Backend expense create does not validate `paid_by`/share users as trip members.
- Missing tests: session-trip ownership, opt-in expense semantics, organizer/member stay authorization, booking route preserves `tripId`, booking confirmation writes/does not write stays intentionally.

Next action: add organizer/member authorization on stay mutations and confirm the intended booking -> stay/expense opt-in UX.

### 11 - Atlas Candidate To Memory Control

Static trace: ready, but dogfood remains blocked.

- Fixed 2026-06-06: Atlas Privacy's receipt CTA routes to `/atlas/receipt` instead of self-looping.
- Fixed 2026-06-06: Receipt screen's Travel Identity CTA is labeled as Travel Identity and routes via the Atlas identity helper.
- Taste “Edit” pushes old/hidden constraints route.
- Fixed 2026-06-06: `GET /api/atlas/places` is implemented in backend + OpenAPI.
- Fixed 2026-06-06: mock approve returns 409 when candidate is not `pending`.
- Fixed 2026-06-06: inbox dismiss prunes accumulated local rows after mutation.
- Signal/artifact mutations do not invalidate all Atlas read models.
- Atlas privacy mutates generic privacy/profile controls, not memory-specific Atlas controls.
- Missing tests: candidate approve/dismiss, signal keep/dispute/forget, receipt/map/postcards coherence.

Next action: fix Atlas self-loop/places contract, align mock approve semantics, and add candidate -> artifact -> signal regression tests.

### 12 - Returned Trip To Story, Memory, And Settle-Up

Static trace: ready. Dogfood ready: no.

- Fixed 2026-06-06: settlement closeout routes to `/trip-expenses?tripId=...`.
- Expenses can render zero-ish state if both route `tripId` and currentTrip are missing.
- Memory route depends on `currentTrip`, unlike Story/Expenses route params.
- Mock story always returns full story; real backend can return `202 composing`.
- Mock trip summary is always null while Memory/post-trip cards depend on it.
- Post-trip Atlas entries are global, not trip-scoped.
- Date/timezone logic mixes local date helpers, `new Date(end_date)`, server date, and UTC lifecycle tasks.
- Post-trip summary/story generation depends on background LLM flags and can be stale/empty in real dogfood.
- Missing tests: returned Trips -> post Folio -> Story -> Memory -> Atlas -> Expenses; settlement closeout preserves `tripId`; cold deep-link Memory/Expenses; mock returned-trip parity.

Next action: fix trip-scoped CTAs and route-param handling before live returned-trip dogfood.

## Recommended Engineering Sequence

1. Fix P0 context/contract blockers:
   - Journey 07 conversation metadata plumbing.
   - Journey 10 booking `tripId` + session ownership + opt-in expense semantics.
   - Journey 01 `/trip-begin` prefill/promotion contract.
2. Close privacy leak paths:
   - Journey 04 booking notes and notification preview redaction.
   - Journey 05 proposal receipt/deep-link and idempotency coverage.
3. Make mock mode useful instead of flattering:
   - Journey 06 coherent Lisbon block/proposal fixtures.
   - Journey 08 truly-live Lisbon fixture.
   - Journey 10 non-empty booking/stay/expense mocks.
   - Journey 12 returned-trip summary/story composing fixtures.
4. De-afford or fix visible no-op CTAs:
   - Journey 08 live/urgent CTAs.
   - Journey 11 Atlas self-loops and stale routes.
   - Journey 07 no-trip `share_with_group`.
5. Add journey-level deterministic tests before mock UI walks.

## Status Matrix Deltas

| Journey | Static trace | Mock walk | Dogfood |
|---|---|---|---|
| 01 | ready | not started | no |
| 02 | ready | not started | no |
| 03 | partial | not started | no |
| 04 | ready | not started / blocked by fixture gap | no |
| 05 | ready | not started | no |
| 06 | ready | blocked by mock ID drift | no |
| 07 | blocked | not started | no |
| 08 | partial | not started | blocked |
| 09 | ready with gaps | not started | no |
| 10 | partial | not started | blocked |
| 11 | ready | not started | blocked |
| 12 | ready | not started | no |
