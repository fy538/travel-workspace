# Booking — System Charter

> Surface: Trips
> Maturity (for MVP): Built-dark
> Status: partial/dark
> Last updated: 2026-06-27

## Purpose
The multi-provider booking spine — searches flights, hotels, restaurants, transit,
cars, and activities, ranks offers, and **proposes** (never silently acts) a booking
to the group. Serves belief #1 and journey 10. The moat is not the transaction —
deep-links capture affiliate revenue — it's the **venue briefing**: party of 6, one
quiet vegetarian, it's Sarah's birthday.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/booking_agent/`](../../travel-agent/backend/booking_agent/FEATURE.md) — `agents/booking_graph.py` (LangGraph state machine), `subscribers.py` + `tasks/session_dispatcher.py` (event handoff + polling claim), `venue_brief.py` (the briefing), `holds.py` (pay-later lifecycle), `capability.py`, `readiness.py`, `providers/*`.
- Frontend: the Propose UX — `DeckCallFace`, `BookingProposalCard`, the booking confirmation card (renders `venue_brief_shared_text` as a "Shared with restaurant" receipt), Call-held surface.
- Tables of record: `booking_sessions`, `booking_offers` (+ `normalized`, holds), restaurant attempts; write-through to `trip_accommodations`.

## Public interface (what other systems may call / read)
- **Inbound (FE/agent → BE):** Concierge `propose_booking` / `confirm_booking` / `book_now` tools (via `capability.py`) · `GET /api/trips/{trip_id}/booking/readiness` (after trip-membership check) · `GET /api/trips/{trip_id}/booking/affiliate-links/travel-insurance`.
- **Inbound (event):** `itinerary.committed` → `subscribers._on_itinerary_committed` warms a pending session (idempotency key `concierge:{itinerary_id}:{autonomy}`) → dispatcher polls every 5s and runs the graph.
- **Consumes:** Planning/Itinerary (the blocks it searches against), Group/Social (party composition for the brief), the shared resilience decorators.
- **Never:** add a new provider until restaurants + venue briefing are real (provider freeze, per Booking Product Strategy); never mark a deep-link offer "confirmed" automatically.

## Owns (source of truth)
The booking session lifecycle, normalized offers, and the pay-later hold state. It
write-throughs a confirmed hotel into `trip_accommodations` and posts booking
receipts, but the itinerary blocks remain owned by Planning/Itinerary.

## Invariants (must always be true)
- **Propose, not Act (human-in-the-loop)** — the system surfaces a proposal; money never moves without explicit final human approval. Both Duffel order creation and held-order settlement gate on `final_human_approval` checks.
- **One person transacts (group-aware)** — a group booking is completed by a single actor; the brief shares group needs **without naming which traveler created them** (anonymized dietary/accessibility).
- **All providers return `NormalizedOffer`** — never raw API responses; resilience decorators (`@retry_with_backoff` + `@with_circuit_breaker`) are mandatory to prevent cascade failures.
- **Deep-link offers never auto-confirm** — `booking_method="deep_link"` (Viator, Rome2Rio, Amadeus hotels) is filtered out of L3 auto-cart; the user completes on the provider site.
- **Idempotent handoff** — the `concierge:{itinerary_id}:{autonomy}` key + `FOR UPDATE SKIP LOCKED` claim make session warming safe across multiple instances.

## Failure modes
- Provider error → circuit breaker opens, search degrades to remaining providers; a dead provider doesn't cascade.
- Non-Duffel `create_order` → raises `NotImplementedError` by design (handoff-only); resolves to a deep-link, never a fabricated confirmation.
- Lapsed pay-later hold → `tasks/expiration.py` sweeps it to `expired` so a dead hold never surfaces on the Call-held surface.

## Maturity & validation
- Serves journey: 10 (booking / stay / expense / trust loop).
- **No category transacts money today.** Every provider except Duffel hits `NotImplementedError` at `create_order`. **Duffel is the only transactional path and it is gated DARK** (`BOOKING_DUFFEL_LIVE_BOOKING_ENABLED=false`, with a prod boot guard). Pay-later **holds are gated off** behind the same flag. Restaurant voice/SMS (Bland.ai + Twilio) exists but provider accounts are **unprovisioned**.
- Revenue dark: `BOOKING_MONETIZATION_MODE=free_affiliate`; Viator `pid`/`mcid` default `""`; travel-insurance referral URL unconfigured.
- DoD state: trip-lifecycle wiring + Propose UX + venue-brief v1 (BE + FE receipt) ✅ · **live provider/channel validation ❌ · any verified end-to-end in-app booking ❌**.

## Canonical docs
- why → `product/Concierge Behavior Spec.md` (belief #1) · strategy → `product/Booking Product Strategy.md` · journey → [`journeys/10-booking-stay-expense-trust-loop.md`](../journeys/10-booking-stay-expense-trust-loop.md) · what(be) → `backend/booking_agent/FEATURE.md`.
- Tests: `tests/booking_agent/*` (graph nodes, holds lifecycle, readiness report, venue brief).

## Open risks / known gaps
- The signature feature (venue briefing) has BE + an FE receipt but **no live provider/channel validation** — until a restaurant call actually carries the brief, the moat is unproven.
- Flipping Duffel live is a money-moving change behind a boot guard + final-human-approval; the dark→live transition is the highest-risk path to verify.
- `readiness.py` is the machine-readable launch gate (Viator attribution, insurance URL, restaurant dispatch creds are blocking config checks) — trust it over ad-hoc judgments of "is booking ready."
