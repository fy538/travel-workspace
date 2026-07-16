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
- **Claim before restaurant contact** — a restaurant voice attempt must atomically move from `pending` to `in_progress` before any Bland POST. Only that transaction's winner may contact the provider.
- **Unknown is not retryable** — a timeout, provider 5xx, malformed success response, missing provider reference, or local persistence failure after provider acceptance is `manual_action_required`. It remains `in_progress` and must not expose Retry. Only an explicit provider rejection, `failed`, or `no_answer` can enter the atomic retry path.
- **Cancellation is claimed before submission** — one durable offer claim owns the provider cancellation. A timeout or local-finalization failure remains pending and reconciles through provider reads; it is never presented as a confirmed cancellation and never resubmitted automatically.
- **Manual recovery is not an override** — an operator may resolve an active restaurant attempt only after automatic reconciliation is explicitly complete. The attempt number, current attempt status, and offer status are locked and rechecked; a late webhook or conflicting terminal state wins.
- **Signed voice callbacks are one terminalization boundary** — Bland HMAC-SHA256 signs the raw callback body. Signed metadata must equal the URL's `attempt_id` plus `attempt_number`, and the signed `call_id` must equal the durable provider reference before parsing. Attempt status, normalized offer status, provider-outcome event, and confirmation writeback queue then commit atomically. Negative attempt outcomes normalize to offer `failed`.

## Failure modes
- Provider error → circuit breaker opens, search degrades to remaining providers; a dead provider doesn't cascade.
- Provider cancellation outcome unknown → keep the booking locally confirmed with durable pending cancellation evidence, block another cancellation submission, and reconcile by provider GET until cancelled or manual attention.
- Non-Duffel `create_order` → raises `NotImplementedError` by design (handoff-only); resolves to a deep-link, never a fabricated confirmation.
- Lapsed pay-later hold → `tasks/expiration.py` atomically sweeps it to `expired` and releases its block marker. If a canonical provider saga owns the hold, the same transaction also cancels the protected dependency and records terminal saga/provider/history evidence; a payment-claimed `held` row is excluded.
- Restaurant voice provider 4xx → explicit dispatch failure, safe to retry through the guarded retry API. Timeout, transport error, provider 5xx, or ambiguous 2xx → outcome unknown, retain `in_progress`, preserve reconciliation evidence, and wait for a late webhook/operator check rather than contacting the venue twice. A legacy SMS/WhatsApp attempt is quarantined locally before contact and cannot be retried.
- Operator resolution write fails after either state update → the entire transaction rolls back, including attempt, offer, and audit event; the same resolution id can be retried safely.
- Confirmation commits but itinerary/receipt projection crashes → durable per-attempt writeback state retains completed steps; the supervised loop reclaims an expired lease and resumes without contacting the restaurant or changing provider truth.
- Signed restaurant callback audit write fails → attempt, offer, and projection queue all roll back. Provider retry can safely re-run the same callback; concurrent duplicates produce one event.

## Maturity & validation
- Serves journey: 10 (booking / stay / expense / trust loop).
- **No category transacts money today.** Every provider except Duffel hits `NotImplementedError` at `create_order`. **Duffel is the only transactional path and it is gated DARK** (`BOOKING_DUFFEL_LIVE_BOOKING_ENABLED=false`, with a prod boot guard). Pay-later **holds are gated off** behind the same flag. Restaurant automated voice exists through Bland.ai but its live provider path is **unproven**. SMS/WhatsApp are traveler handoffs, not automated bookings.
- Revenue dark: `BOOKING_MONETIZATION_MODE=free_affiliate`; Viator `pid`/`mcid` default `""`; travel-insurance referral URL unconfigured.
- DoD state: trip-lifecycle wiring + Propose UX + venue-brief v1 (BE + FE receipt) ✅ · **live provider/channel validation ❌ · any verified end-to-end in-app booking ❌**.

## Canonical docs
- why → `product/Concierge Behavior Spec.md` (belief #1) · strategy → `product/Booking Product Strategy.md` · journey → [`journeys/10-booking-stay-expense-trust-loop.md`](../journeys/10-booking-stay-expense-trust-loop.md) · what(be) → `backend/booking_agent/FEATURE.md`.
- Tests: `tests/booking_agent/*` (graph nodes, holds lifecycle, readiness report, venue brief).

## Open risks / known gaps
- The signature feature (venue briefing) has BE + an FE receipt but **no live provider/channel validation** — until a restaurant call actually carries the brief, the moat is unproven.
- Flipping Duffel live is a money-moving change behind a boot guard + final-human-approval; the dark→live transition is the highest-risk path to verify.
- `readiness.py` is the machine-readable launch gate (Viator attribution, insurance URL, and Bland API key/signing secret/public callback URL are blocking config checks; restaurant Twilio messaging is explicitly dark and nonblocking) — trust it over ad-hoc judgments of "is booking ready."

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

### Restaurant automated voice and messaging handoffs

- Automated voice dispatch is a two-boundary operation: first win the atomic
  local claim, then make exactly one Bland POST. Concurrent workers that lose the
  claim exit without contacting Bland.
- Bland Send Call does not document a provider-side idempotency token. Therefore
  the database claim—not an assumed provider feature—is the primary
  duplicate-contact boundary.
- A Bland `call_id` is durable evidence and is retained whenever available.
  Missing or unpersisted evidence after submission is ambiguous, not failed.
- Outbound voice now normalizes the provider number to E.164 and states the
  exact requested datetime and party size in the task. The privacy-safe venue
  brief is included, voicemail hangs up without leaving traveler details, audio
  recording is disabled, and call duration is capped at five minutes by default.
- Block analysis now carries the venue phone number into the analyzed block and
  then into the voice attempt. This closes the former gap where a venue phone was
  selected from storage and silently discarded before dispatch.
- Retry atomically accepts only terminal `failed` or `no_answer` attempts,
  increments `attempt_number`, clears the prior provider reference, and appends a
  bounded reconciliation history. Pending, active, ambiguous, confirmed,
  declined, or concurrently-reset attempts return conflict and spawn no worker.
- The app polls while an attempt is active. It displays explicit failed/no-answer
  as retryable, declined as a replacement decision, and ambiguous/stale active
  contact as “check, do not contact again.”
- A supervised read-only worker now atomically claims active voice attempts that
  have an exact provider reference, then performs Bland Call Details. Legacy
  message attempts that already carry an exact Twilio Message SID retain a
  read-only Message fetch for recovery even though no new automated message can
  be dispatched. Claims carry a recoverable lease, refreshes retain a bounded
  history, and the final write is guarded by both `attempt_number` and active
  status so a late terminal webhook always wins the race.
- Transport truth is deliberately narrower than reservation truth. Bland
  `no-answer`/`busy` are explicit retryable failures. Bland `completed` proves
  only that contact ran; it cannot confirm a table without the signed outcome
  webhook.
- Transcript interpretation is also fail-closed. A confirmation lands only when
  the parsed transcript contains the exact requested datetime (minute-level) and
  exact party size; a different/alternative time cannot be silently accepted and
  a decline requires an explicit reason. Empty, unparsable, or
  otherwise ambiguous signed callbacks atomically preserve the normalized
  transcript, retain the active offer, set durable manual attention, and append
  `booking.restaurant_provider_review_required`. They never expose Retry.
- Plain Programmable Messaging inbound webhooks identify the inbound message and
  sender/recipient but do not reliably carry the exact outbound booking Message
  SID. WhatsApp's replied-message SID is conditional, so it cannot be the sole
  destructive mutation key. Phone/time matching is unsafe when attempts overlap.
  Consequently new SMS/WhatsApp capabilities render `sms:` or `wa.me` traveler
  handoffs. Any legacy automated messaging attempt fails before a Twilio POST
  with `twilio_exact_reply_correlation_unavailable`; retry remains disabled.
- A future automated messaging channel must be implemented as a separate durable
  provider saga with exact thread identity (for example, a recoverable Twilio
  Conversations adapter), signed callbacks, reconciliation, and fault-injection
  coverage. Twilio credentials alone do not make that surface ready.
- Missing provider references are not searched by phone number, venue, or time.
  That destructive-recovery branch remains manual because a fuzzy match could
  attach another call/message to the wrong request.
- Automatic reads are bounded (30 refreshes by default). Exhaustion, provider
  auth failure, unreadable truth, or provider `unknown` becomes durable manual
  attention without exposing another contact action.
- Provider-terminal ambiguity can be closed through
  `POST /admin/booking/restaurant-attempts/{attempt_id}/resolve`. The route is
  secure-by-default behind `ADMIN_API_TOKEN` and requires an opaque operator id,
  a resolution UUID, `expected_attempt_number`, a structured evidence type and
  reference, and an outcome-bound reason code. It does not accept free-form
  notes or raw transcript text.
- Allowed outcomes are `confirmed`, `declined`, `failed`, and `no_answer`.
  Confirmation requires an explicit confirmed datetime; confirmation fields are
  rejected for negative outcomes. The matching offer becomes `confirmed` or
  `failed` in the same transaction as the attempt and append-only
  `booking.restaurant_operator_resolved` event.
- Replaying the same resolution UUID with the same decision is an idempotent
  read. Reusing it with different operator identity, evidence, or outcome is a
  conflict. Stale attempt numbers, still-running automatic reconciliation, and
  terminal offer contradictions are also conflicts.
- The shared admin token establishes the current internal trust boundary; the
  separately recorded `operator_id` is asserted by that trusted caller, not an
  independently authenticated human principal. Before a multi-operator support
  console is exposed, replace this with per-operator identity and least-privilege
  authorization. This limitation does not weaken atomicity, but it limits the
  attribution strength of the audit record.
- Real-Postgres fault injection proves that an audit-event failure rolls back
  the prior attempt and offer writes and that retry succeeds. A four-connection
  race proves exactly one applied decision and one event; all other callers
  receive idempotent replay.

### Restaurant confirmation projection recovery

- Every first transition to `restaurant_booking_attempts.status=confirmed`
  queues `confirmation_details.confirmation_writeback` in the same transaction.
  The immediate hook is only a low-latency attempt; correctness does not depend
  on that process surviving.
- The supervised booking loop leases due confirmed attempts and records
  `block`, `receipt`, and `event` progress independently. A 180-second lease is
  reclaimable after process death. Transient failures retry with exponential
  backoff capped at one hour.
- Block stamping is idempotent by `attempt_id`. A cancelled or deleted block is
  an intentional no-op because a delayed provider result must not resurrect it.
  A block confirmed by another booking becomes `manual_action_required` and is
  never overwritten automatically.
- Confirmation receipts use database-enforced idempotency key
  `restaurant-confirmation:{attempt_id}`. Their metadata contains only the
  confirmation number/time, confirmed party size, special notes, and shared
  venue brief; internal operator evidence, provider reconciliation, and lease
  state are excluded. The normal 24-hour chat idempotency-key cleanup preserves
  this reserved prefix, keeping replay protection durable across long outages.
- The durable `booking.restaurant_confirmed` event and its completed-step marker
  commit atomically. The in-process event-bus broadcast happens afterward and is
  best-effort; itinerary state, receipt, and the append-only event remain the
  durable product truth.
- Real-Postgres crash tests cover both non-atomic boundaries: receipt committed
  before its marker, and event inserted before its marker update. Replay yields
  exactly one receipt and one event, while the injected event transaction rolls
  back completely before retry.
- Provider evidence reviewed 2026-07-15:
  [Twilio inbound-message webhooks](https://www.twilio.com/docs/messaging/guides/webhook-request),
  [Twilio Message resource](https://www.twilio.com/docs/messaging/api/message-resource),
  [Twilio outbound-status tracking](https://www.twilio.com/docs/messaging/guides/track-outbound-message-status),
  [Twilio Conversations overview](https://www.twilio.com/docs/conversations-classic/overview),
  [Twilio conversation-scoped webhooks](https://www.twilio.com/docs/conversations-classic/api/conversation-scoped-webhook-resource),
  [Bland Send Call](https://docs.bland.ai/api-v1/post/calls), and
  [Bland Get Call](https://docs.bland.ai/api-v1/get/calls-id).

### Restaurant signed outcome terminalization

- Callback parsing is deliberately outside the transaction; applying parsed
  truth is not. The apply boundary locks the attempt joined to its offer and
  session, then rechecks the contact attempt number before changing state.
- The attempt preserves channel-specific outcomes (`confirmed`, `declined`,
  `failed`, `no_answer`). The parent offer uses its smaller legal vocabulary:
  `confirmed` for confirmation and `failed` for every negative outcome. A
  callback can no longer attempt to write invalid offer status `declined`.
- Bland dispatch embeds both `attempt_id` and `attempt_number` in callback URL,
  request data, and metadata. The route implements Bland's documented
  `X-Webhook-Signature` HMAC-SHA256 verification over the exact raw body. Because
  Bland signs the body rather than the URL, the handler additionally requires
  the signed metadata to match the URL identity and requires signed `call_id` to
  equal the durable provider reference before transcript parsing. A valid body
  replayed to another URL, an old retry callback, or a mismatched call is ignored.
- The legacy Twilio inbound-reply parser still enforces the same two-part identity
  and signature boundary, but no production dispatcher can create the required
  per-attempt callback identity with plain Programmable Messaging. The route is
  dormant compatibility code, not a live product path. Automated SMS/WhatsApp is
  quarantined before contact; no phone/time fuzzy fallback is permitted.
- The first terminal result wins for one attempt version. Exact duplicates are
  idempotent; negative callbacks cannot overwrite confirmation; a callback for
  another attempt number/reference or any other terminal attempt is an
  acknowledged no-op. A conflicting terminal offer is a hard conflict, never a
  partial attempt-only write.
- During rollout, an exact signed replay may find the attempt already terminal
  but its offer still active because the legacy two-transaction handler crashed
  between writes. That one recognizable partial state is repaired atomically
  and marked `repaired_legacy_partial` in the outcome event; contradictory
  terminal states are not guessed or overwritten.
- `booking.restaurant_provider_outcome` is inserted in the same transaction and
  excludes transcript and confirmation number. Confirmations also queue durable
  block/receipt/event projection work before commit; the immediate writeback is
  only a latency optimization after transaction success.
- Real-Postgres fault injection proves an audit insertion failure rolls back the
  attempt, offer, and queued projection, and a retry then succeeds. A
  four-connection duplicate race proves one terminal transition and one audit
  event; the other callers receive idempotent acknowledgement.
- The same transaction rule covers inconclusive callbacks: transcript/manual
  review state and its append-only event land together. Injecting failure at the
  event write rolls the review state back so a provider replay can retry safely.
- Provider contract re-reviewed 2026-07-15:
  [Bland webhook signing](https://docs.bland.ai/tutorials/webhook-signing),
  [Bland Send Call](https://docs.bland.ai/api-v1/post/calls),
  [Bland post-call webhook payload](https://docs.bland.ai/tutorials/post-call-webhooks),
  and [Bland Call Details](https://docs.bland.ai/api-v1/get/calls-id).
