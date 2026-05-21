# Area Audit: Booking, Expenses, Transport

Date: 2026-05-21  
Agent: Cursor Cloud area 13 audit  
Scope: Booking agent docs/routes/CRUD/graph/capability/providers, concierge booking and transport handlers, expenses routes/CRUD/settlement/OCR/auto-log, Travel App booking session/proposal/confirmation UI, expense hooks/tests/docs, transport roadmap/gap callouts.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: High
- Highest-risk finding: Booking REST routes do not consistently prove that nested session, offer, attempt, or itinerary IDs belong to the path trip before reading or mutating them.
- Checks run: `make contract-check` -> pass; `PYTHONPATH=. pytest tests/api/test_api_booking.py tests/api/test_expenses_api.py -q` -> pass, 68 passed.
- Residual uncertainty: I did not run live provider canaries, OCR LLM calls, Postgres-backed E2E tests, Expo UI smoke tests, or any external provider/API calls.

## Findings

### P1 — Booking Routes Allow Cross-Trip Session And Offer Mutations

Status: Confirmed  
User impact: A dogfood user or buggy client that has access to any trip can read or mutate booking sessions/offers from a different trip if it has or reuses those UUIDs. The riskiest path is cart confirmation: it marks the foreign session confirmed, emits a booking event on the path trip, and can auto-create expenses in the wrong trip from offers belonging to another session.  
Product promise affected: concierge trust, false booking confirmation, expense integrity, privacy

References:

- `Travel Agent/backend/api/routes/booking.py:97` — `create_booking_session` checks only path-trip membership, then stores `body.itinerary_id` without verifying that itinerary belongs to the path trip.
- `Travel Agent/backend/api/routes/booking.py:203` — `get_booking_session` fetches by `session_id` and returns it without checking `row.trip_id == trip_id`.
- `Travel Agent/backend/api/routes/booking.py:224` — `list_offers` fetches offers by `session_id` without validating that session belongs to the path trip.
- `Travel Agent/backend/api/routes/booking.py:241` — `select_offer` updates `offer_id` directly and ignores both `session_id` and `trip_id` ownership.
- `Travel Agent/backend/api/routes/booking.py:281` — `get_cart` loads a session but does not reject `session.trip_id != trip_id`.
- `Travel Agent/backend/api/routes/booking.py:314` — `confirm_cart` updates `session_id` directly and emits `booking.cart_confirmed` for the caller-supplied path trip.
- `Travel Agent/backend/api/routes/booking.py:326` — the same path calls `auto_create_expenses_from_booking(trip_id, session_id)`, mixing path trip members with whatever offers are attached to the supplied session.
- `Travel Agent/backend/expenses/auto_log.py:48` — auto-log looks up only `booking_sessions.initiated_by` by `session_id`, not the session trip.
- `Travel Agent/backend/expenses/auto_log.py:75` — auto-log splits the foreign session's selected offers across members of the caller-supplied trip.
- `Travel Agent/backend/api/routes/booking.py:355` and `Travel Agent/backend/api/routes/booking.py:373` — restaurant attempt list/retry also operate by session/attempt ID without proving trip ownership.

Why it matters:

Booking is explicitly a trust loop. A stale route param, shared deep link, optimistic client bug, or leaked UUID should not be enough to confirm or retry work in another trip. The current route pattern is inconsistent with the proposal endpoint, which does correctly check `proposal.trip_id != trip_id` before returning.

Repro or deterministic test idea:

1. Create trip A and trip B; make the actor a member of trip A only.
2. Insert a booking session and selected offer for trip B.
3. Call `POST /api/trips/{trip_a}/booking/sessions/{session_b}/cart/confirm`.
4. Expected: 404 or 403 before mutation.
5. Current likely/observed from static path: `booking_sessions(session_b).status` is set to `confirmed`, a `booking.cart_confirmed` event is emitted for trip A, and auto-log attempts to create trip A expenses from session B offers.

Suggested fix direction:

Add shared booking route guards that load and validate the parent resource before every nested read/mutation: itinerary belongs to path trip on session creation; session belongs to path trip on all session/cart/offer/attempt routes; offer belongs to session; attempt belongs to a session offer. Keep the successful proposal route's `proposal.trip_id` check as the local pattern.

Related bug class:

Nested-resource authorization gap / cross-trip IDOR / false booking confirmation

Confidence: High

### P1 — Booking UI Claims “Booked” Or “AI Books Directly” Before Any Provider Booking Exists

Status: Confirmed  
User impact: A dogfood tester can reasonably believe Vesper has actually booked or will directly book an API/L3 item, even though the backend currently only creates a session, selects offers, or marks a cart confirmed internally. This creates the real-world failure mode of users showing up without a reservation or assuming money was spent when no provider order exists.  
Product promise affected: concierge trust, provider-backed flow honesty, false booking confirmation

References:

- `Travel Agent/docs/working/Booking Live Provider Audit.md:34` — the live-provider audit documents that L3 does not call provider `book()` or `create_order()`.
- `Travel Agent/docs/working/Booking Live Provider Audit.md:48` — no provider has a `book()` / `create_order()` method in the current ABC.
- `Travel Agent/backend/booking_agent/agents/booking_graph.py:377` — `auto_select_best` only auto-selects the best offer and builds a cart.
- `Travel Agent/backend/booking_agent/agents/booking_graph.py:479` — `persist_offers` writes selected/available offer rows; it does not execute a provider order.
- `Travel App/components/chat/BookingConfirmationCard.tsx:31` — `METHOD_LABEL.api` renders as `Booked`.
- `Travel App/components/chat/BookingConfirmationCard.tsx:53` — the rendered header uses that label even when `isAgentHandled` means the card is only showing an in-progress session.
- `Travel App/app/booking/[sessionId].tsx:70` — successful cart confirmation shows `Booking confirmed!`.
- `Travel App/app/booking/[sessionId].tsx:322` — L3 is labeled `Auto — AI books directly`.

Why it matters:

The docs are honest that live booking is scaffolded. The mobile UI is less honest at exactly the moment users need precision. “Booked” and “AI books directly” are stronger than the backend can currently guarantee.

Repro or deterministic test idea:

1. Render `BookingConfirmationCard` with `{ booking_method: "api", handoff_only: false, session_id: "..." }`.
2. Expected: header says something like “Booking in progress” or “Ready to review”, not “Booked”.
3. Current observed from code: header label is `Booked` while the secondary text says “Agent is handling this booking”.
4. Render booking session screen for `autonomy_level='L3_cart'`.
5. Expected: label says auto-select/review, or feature disabled unless live booking is truly enabled.
6. Current observed from code: label says `Auto — AI books directly`.

Suggested fix direction:

Reserve “booked/confirmed” for provider-confirmed states with a provider confirmation reference. Rename current API/L3 states to “booking in progress”, “selected for review”, or “handoff ready”; gate direct-booking copy behind the same future live-booking flag/canary criteria used for providers.

Related bug class:

Scaffolded-domain UI honesty gap / false success state

Confidence: High

### P1 — Expense Create Paths Trust Client-Supplied Payer And Share User IDs

Status: Confirmed  
User impact: A trip member or buggy client can create a ledger item that says another user paid, or can include non-trip users in shares. Settlement balances can become wrong or include people who are not in the trip, undermining the “reliable enough for real groups” expense promise.  
Product promise affected: expense reliability, financial trust, group safety

References:

- `Travel Agent/backend/api/routes/expenses.py:110` — `create_expense` only verifies the actor is a trip member.
- `Travel Agent/backend/api/routes/expenses.py:145` — the route persists `paid_by=body.paid_by` without checking that `paid_by` is the actor, organizer-authorized, or a trip member.
- `Travel Agent/backend/api/routes/expenses.py:143` — shares are computed from `body.shares` before any trip-membership validation.
- `Travel Agent/backend/api/routes/expenses.py:882` — `_compute_shares` copies `si.user_id` directly into share rows.
- `Travel Agent/backend/api/routes/expenses.py:310` — update can replace shares with `body.shares` without validating that new share users are trip members.
- `Travel Agent/backend/api/routes/expenses.py:793` — receipt-to-expense only verifies path-trip membership before using the body.
- `Travel Agent/backend/api/routes/expenses.py:834` — receipt-to-expense persists `paid_by=body.paid_by` and `shares=share_dicts` from the caller-supplied body.
- `Travel Agent/backend/api/routes/expenses.py:559` — comments have the same identity smell: a member can create a comment with `body.user_id` instead of `actor.id`.

Why it matters:

Expense settlement is social and financial state. The API already fixed “who can edit/delete/settle” in comments around B6/B7, but creation still lets the client define who paid and who owes. That can make the ledger look authoritative while attributing debt or payment to the wrong person.

Repro or deterministic test idea:

1. In a trip with Alice and Bob, authenticate as Alice.
2. POST `/api/trips/{trip_id}/expenses` with `paid_by=<bob_id>` and shares containing Alice, Bob, and a random UUID.
3. Expected: reject unless Bob is the actor or organizer-approved, and reject all share users that are not active trip members.
4. Current likely/observed from static path: route computes and persists those IDs because only `require_trip_member(trip_id, actor)` and block ownership are checked.

Suggested fix direction:

Add a trip-member validation helper for `paid_by`, `shares[*].user_id`, and comment authors. For normal member-created expenses, default `paid_by` and comment `user_id` to `actor.id`; if organizer-created-on-behalf is allowed, make it explicit and tested. Apply the same validation to create, update-share replacement, receipt-to-expense, and booking auto-log.

Related bug class:

Financial identity spoofing / membership validation gap

Confidence: High

## Non-Findings / Things Ruled Out

- Receipt upload has explicit content-type allowlisting, a 15 MB max, trip-scoped storage paths, idempotency response caching, and path-trip checks before image retrieval.
- Settlement single and batch endpoints now enforce payer-or-self-only authorization before mutating shares.
- Transport live search is feature-flagged off by default through `CONCIERGE_SEARCH_TRANSPORT_ENABLED`; disabled mode returns advisory/operator links and tests assert providers are not called.
- Contract snapshot and generated frontend API types are in sync.
- Targeted booking and expense API tests pass; the findings above are missing invariants, not currently failing covered tests.

## Suggested Follow-Up Checks

- Add booking API tests that pass a valid actor for trip A and session/offer/attempt IDs from trip B, asserting 403/404 and no status/event/expense mutation.
- Add expense API tests for create/update/receipt-to-expense with non-member `paid_by` and non-member share IDs.
- Add a frontend test for API booking confirmation cards that asserts API/L3 sessions do not render `Booked` until a provider-confirmed state exists.
- Add a small static route review for every nested `/api/trips/{trip_id}/.../{resource_id}` endpoint: load resource, assert resource trip, then mutate.
