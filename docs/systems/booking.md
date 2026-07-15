# Booking — System Charter

> Surface: Trips
> Maturity (for MVP): Built-dark
> Status: partial/dark
> Last updated: 2026-07-15

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
- **Claim before restaurant contact** — a restaurant attempt must atomically move from `pending` to `in_progress` before any Bland or Twilio POST. Only that transaction's winner may contact the provider.
- **Unknown is not retryable** — a timeout, provider 5xx, malformed success response, missing provider reference, or local persistence failure after provider acceptance is `manual_action_required`. It remains `in_progress` and must not expose Retry. Only an explicit provider rejection, `failed`, or `no_answer` can enter the atomic retry path.

## Failure modes
- Provider error → circuit breaker opens, search degrades to remaining providers; a dead provider doesn't cascade.
- Non-Duffel `create_order` → raises `NotImplementedError` by design (handoff-only); resolves to a deep-link, never a fabricated confirmation.
- Lapsed pay-later hold → `tasks/expiration.py` atomically sweeps it to `expired` and releases its block marker. If a canonical provider saga owns the hold, the same transaction also cancels the protected dependency and records terminal saga/provider/history evidence; a payment-claimed `held` row is excluded.
- Restaurant provider 4xx → explicit dispatch failure, safe to retry through the guarded retry API. Timeout, transport error, provider 5xx, or ambiguous 2xx → outcome unknown, retain `in_progress`, preserve reconciliation evidence, and wait for a late webhook/operator check rather than contacting the venue twice.

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

## Provider reconciliation boundary

- A transport error after order submission is `manual_action_required`, never
  proof of failure. The offer remains held and cannot be submitted again.
- Automatic retry exhaustion performs a final provider GET. A late confirmation
  wins; an unresolved result remains Needs attention rather than becoming a
  false failure.
- The traveler-facing status check and operator canary perform provider reads
  only. They do not create an order, place or settle a hold, submit payment, or
  cancel.
- Local sandbox search connectivity passed on 2026-07-14. A live read-only order
  reconciliation remains gated on an operator-supplied existing sandbox order
  id; no order id or final payment approval was configured during this slice.

### Restaurant call and message dispatch

- Dispatch is a two-boundary operation: first win the atomic local claim, then
  make exactly one provider POST. Concurrent workers that lose the claim exit
  without contacting Bland or Twilio.
- The regular Twilio Message API and Bland Send Call API do not document a
  provider-side idempotency token for these requests. Twilio's duplicate-message
  guidance says duplicates almost always mean the application made multiple
  POSTs. Therefore the database claim—not an assumed provider feature—is the
  primary duplicate-contact boundary.
- A provider reference (`call_id` or message `sid`) is durable evidence and is
  retained whenever available. Missing or unpersisted evidence after submission
  is ambiguous, not failed.
- Retry atomically accepts only terminal `failed` or `no_answer` attempts,
  increments `attempt_number`, clears the prior provider reference, and appends a
  bounded reconciliation history. Pending, active, ambiguous, confirmed,
  declined, or concurrently-reset attempts return conflict and spawn no worker.
- The app polls while an attempt is active. It displays explicit failed/no-answer
  as retryable, declined as a replacement decision, and ambiguous/stale active
  contact as “check, do not contact again.”
- A supervised read-only worker now atomically claims active attempts that have
  an exact provider reference, then performs Bland Call Details or Twilio
  Message fetches. Claims carry a recoverable lease, refreshes retain a bounded
  history, and the final write is guarded by both `attempt_number` and active
  status so a late terminal webhook always wins the race.
- Transport truth is deliberately narrower than reservation truth. Bland
  `no-answer`/`busy` and Twilio `failed`/`undelivered` are explicit retryable
  failures. Bland `completed` and Twilio `delivered` prove only that contact ran
  or arrived; neither can confirm a table without the signed outcome webhook.
- Missing provider references are not searched by phone number, venue, or time.
  That destructive-recovery branch remains manual because a fuzzy match could
  attach another call/message to the wrong request.
- Automatic reads are bounded (30 refreshes by default). Exhaustion, provider
  auth failure, unreadable truth, or provider `unknown` becomes durable manual
  attention without exposing another contact action.
- Provider evidence reviewed 2026-07-15:
  [Twilio Message resource](https://www.twilio.com/docs/messaging/api/message-resource),
  [Twilio outbound-status tracking](https://www.twilio.com/docs/messaging/guides/track-outbound-message-status),
  [Twilio duplicate-message guidance](https://www.twilio.com/docs/messaging/guides/debugging-common-issues),
  [Bland Send Call](https://docs.bland.ai/api-v1/post/calls), and
  [Bland Get Call](https://docs.bland.ai/api-v1/get/calls-id).
