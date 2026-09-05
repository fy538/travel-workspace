---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Read-only static inventory for the capability-retirement package; records booking execution entry points, retained consumers, and the runtime evidence still required before shutdown.
supersedes: []
source_of_truth_for: []
---

# Capability retirement — static inventory

## Status

This is the source-inspection portion of CR-1 in the [capability-retirement
plan](product-surface-contraction-investigation-2026-09-04.md#14-dependency-ordered-engineering-packages).
It is deliberately separate from a production-obligation report: no database,
queue, provider account, or external service was queried. Counts below describe
committed source and generated contracts, not user adoption or live exposure.

The inventory is an execution aid, not an authorization to delete code. The
retirement plan requires a fresh environment-specific obligation check after
admission closes and before removing recovery paths.

## Static scope

| Area | Evidence inspected | Current finding |
| --- | --- | --- |
| Backend HTTP | `api/routes/booking.py`, `admin_booking.py`, `booking_webhooks.py`, `booking_confirmation_landing.py`, `itinerary_operations.py` | Session, offer, cart, hold, checkout, cancellation, restaurant recovery, confirmation sharing, coverage, readiness, and provider-saga routes coexist. |
| Concierge | `concierge/tools.py`, `capability_catalog.py`, `tools_schema.py`, `tool_handlers/booking_flow.py`, `tool_handlers/transport.py` | `propose_booking` / `confirm_booking` and transport search remain discoverable; L1 can hand off, while confirmation still branches into session creation for some capabilities. |
| Runtime | `api/lifecycle.py`, `core/event_subscribers.py`, `workers/booking_jobs.py`, `workers/audio_jobs.py`, `core/scheduled_tasks.py` | API lifespan, independent worker/cron registration, session dispatch, expiration, checkout reconciliation, and provider callbacks can restart or advance work. |
| Provider execution | `booking_agent/tasks/provider_checkout.py`, `itinerary_provider_executor.py`, `holds.py`, `providers/duffel.py`, restaurant dispatch/reconciliation | Duffel mutation is gated but implemented; held-order confirmation has a separate saga executor; restaurant contact has recovery machinery. |
| Mobile | `app/booking/[sessionId].tsx`, `app/venue/[venueId]/index.tsx`, booking hooks/components, `BookingConfirmationCard`, `HandoffReturnCatchPrompt`, route/data/API interfaces | The 1,487-line session route and related controls remain reachable; a venue action can create an L1 session; global return-catch state is persisted on device. |
| Retained readers | `life/refind_sources.py`, booking coverage, stays, expenses, account deletion/export, confirmation sharing | Historical/provider evidence is consumed outside checkout and must be migrated or retained. |

## Contract count

The committed `docs/openapi.json` snapshot contains **44 operations** whose path
contains `booking` or `provider-sagas` under the current API policy:

- 39 `active`;
- 4 `retiring`;
- 1 `dark`.

This includes retained reads, administrative recovery, and one booking-cost
operation. It is not the number of operations to delete. The policy's lifecycle
classification is not proof of runtime permission or production adoption.

The v1 release manifest already marks live transaction execution `out`, while
booking handoff/coverage remains partial. Retirement changes the underlying
responsibility boundary and therefore requires the manifest, policy, generated
release contract, and mobile route registry to be reconciled together.

## Disposition matrix

| Capability family | Current entry points | Proposed disposition | Required retained consumer / proof |
| --- | --- | --- | --- |
| Provider checkout, payment, cart, hold settlement | Booking session route/API, Duffel provider, provider checkout task, hold routes, itinerary held-confirmation saga | Retire admission and execution | No new create/pay/hold effect after closure; finite recovery only for identified submitted obligations |
| Provider cancellation/rebooking | Offer cancellation routes, cancellation reconciliation, admin review | Retire new execution; retain liability-reducing recovery only when needed | Existing external state remains distinguishable as cancelled, active, unknown, or manual attention |
| Automated restaurant contact | Restaurant dispatch, retry route, signed callback, operator resolution | Retire new contact and retry | Existing active attempts either resolve through bounded recovery or are explicitly absent |
| External venue/transport continuation | Capability resolver, deep links, OpenTable/Viator/Rome2Rio handoff | Keep, simplify, and make session-free where possible | Link opens without assignment, booking session, or return prompt; origin/context returns intact |
| Confirmation/ticket evidence | Intake/share/email paths, booking confirmation card, booking truth, coverage, Life refinding | Keep and decouple from execution | Supported confirmation can be understood and retrieved; no inferred attendance or live monitoring |
| Booking proposal language | Concierge schemas/catalog and booking cards | Rewrite to external continuation / evidence language | Retired tools cannot promise Vesper execution; stale calls fail with a truthful response |
| Booking readiness/monetization | Readiness route, affiliate links, canaries, strategy docs | Remove execution launch gates; retain optional referral only if independently justified | No provider credentials or marketplace roadmap required to support retained experience |
| Administrative settings | Booking autonomy, participant consent, cancellation/recovery controls | Remove controls belonging only to retired execution | Remaining privacy, Plan editing, sharing, delegation, and account controls remain reachable |

## Dependency edges that must be resolved

1. Places currently imports resilience through the booking provider compatibility
   module. The actual primitives already live in `backend/core/resilience.py`;
   redirect imports before removing the compatibility module.
2. Life refinding joins `booking_offers` and `booking_sessions`; preserve an
   explicit bounded legacy read adapter or migrate its evidence source.
3. Stay, expense/refund, account deletion, membership transfer, and booking
   coverage read booking records. Their retained facts cannot be removed with
   the checkout UI.
4. `core/event_subscribers.py`, API lifespan, `booking_jobs`, `audio_jobs`,
   scheduled tasks, provider outbox/sagas, and webhooks form independent runtime
   paths. Removing the REST route alone is insufficient.
5. The venue screen creates an L1 session even though an external link does not
   require one; the Chat L1 path has different handoff stamping behavior. These
   callers need coordinated replacement and stale-card handling.
6. `HandoffReturnCatchPrompt` and its AsyncStorage claim key are mobile state,
   not backend truth. Remove the behavior with a narrow local migration; do not
   convert old device claims into reservations.
7. Manual attestation requires an existing Trip block and prior handoff. An
   independent confirmation needs an approved Source/owner association seam
   before CR-3 can claim generalized support.

## Required environment audit (not performed)

Before CR-2 closure or CR-5 deletion, run a read-only audit separately for each
deployed environment. Return aggregate counts and redacted opaque identifiers
for:

- nonterminal sessions and offers;
- held or payment-ambiguous orders;
- pending cancellation claims;
- active restaurant attempts and exact provider references;
- provider sagas and scheduled/outbox tasks;
- uncompleted block/receipt/event write-back;
- undelivered refund or confirmation projections; and
- shared historical records required by deletion/export.

The audit must not claim an empty local database certifies production. It must
not call mutation-oriented claim, reconciliation, recovery, startup, or provider
POST functions. Re-run it after admission closure to catch work already in
flight. If access is unavailable, mark shutdown blocked and continue only with
source-level admission/replacement work.

## CR-1 exit criteria

- Every execution entry point, restart path, retained consumer, and operational
  requirement has a disposition.
- The environment audit is attached as a separate redacted receipt, or its
  absence is explicitly recorded as a blocker.
- No production data or secrets are committed.
- The next package can close new admission without deleting retained evidence.

The static portion is complete on 2026-09-05. The environment obligation audit
and any runtime shutdown remain outstanding.
