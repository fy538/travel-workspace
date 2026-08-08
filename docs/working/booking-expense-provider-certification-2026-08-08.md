---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-08
last_verified: 2026-08-08
expires: 2026-09-03
why_new: Record the provider, device, and cross-system gates for the booking-to-expense trust seam.
source_of_truth_for: [booking-provider-expense-certification]
---

# Booking → Provider → Expense Certification Gate

This is the release record for the high-stakes booking seam. The implementation
is wired end to end, but live provider booking remains dark until the provider
and real-device gates below pass. A green unit suite is not a substitute for a
provider reconciliation or a multi-member walk.

## Invariant matrix

| Invariant | Implemented authority | Automated evidence | Release state |
|---|---|---|---|
| One traveler is responsible for transacting | Booking session controller; observer UI is read-only | Booking controller/observer tests and route membership guards | Ready for device proof |
| Provider accepts but the response is lost | Durable provider operation ledger plus read-only reconciliation | Checkout/reconciliation focused tests | Ready for provider sandbox proof |
| Retry cannot create a second provider operation | Operation identity and idempotency keys; unknown state blocks retry | Provider operation and cancellation retry tests | Ready for provider sandbox proof |
| Cancellation requires a fresh quote and human approval | Quote fingerprint bound to the confirmation request | Cancellation quote/approval tests | Ready for device proof |
| Provider truth fans out once | Canonical `booking.truth_changed` event with deterministic fact version | Booking truth and concierge subscriber tests | Ready for event replay proof |
| Itinerary and receipt projections do not invent confirmation | Projection consumes canonical provider truth; raw provider payload is not the group contract | Booking writeback and receipt tests | Ready for device proof |
| Booking becomes a cost only after explicit opt-in | Organizer-only `booking_opt_in`; confirmed offer and trip ownership are server-checked | Expense opt-in/idempotency tests | Ready for device proof |
| Refund/fee evidence is append-only | `booking_expense_adjustments`, unique idempotency key, original expense untouched | Migration, booking truth, and expense projection tests | Ready for device proof |
| Settlement is paused while cancellation cost is unresolved | Server mutation capability and settlement guard | Expense review/settlement tests; Costs UI test | Ready for device proof |
| Currency provenance survives the seam | Adjustment carries source currency, optional settlement amount/currency, rate, and rate source | Expense currency and adjustment tests | Cross-currency provider proof required |
| Group sees useful state, not private payment input | Booking receipt and expense serializers expose only group-safe facts | Projection/privacy tests | Device privacy walk required |

## Gates run on 2026-08-08

The following checks passed in the current worktrees:

```text
backend: 17 focused booking/expense tests passed
frontend: 7 focused expense/provider-adjustment tests passed
frontend: npx tsc --noEmit passed
workspace: api_contract_audit.py --json passed (438 active, 1 dark, 56 retiring)
backend: alembic heads passed (bookingadjust01 is the single head)
```

The full API import/test bootstrap is still unavailable in this environment
because route registration imports the missing `json_repair` package. That is a
test-environment blocker, not evidence that the live provider seam is safe.

## Required provider/device evidence before enabling live booking

1. In a provider sandbox, create a checkout whose response is intentionally
   dropped after provider acceptance. Confirm that the UI says **check status**,
   reconciliation finds the existing provider operation, and a second submit is
   unavailable until failure is proven.
2. In a sandbox, request a cancellation, drop the confirmation response, and
   repeat the read-only reconciliation. Confirm that a changed quote or unknown
   outcome cannot reuse the old approval or create a duplicate cancellation.
3. With three real trip members on two devices, verify controller, observer, and
   declined/pending consent projections. Only the controller can select, pay,
   release, or cancel; observers converge after background/resume.
4. Confirm a provider-confirmed cancellation with an explicit booking Cost opt-in.
   Verify the original expense and shares remain unchanged, the adjustment is
   visible with currency/rate provenance, settlement stays paused until review,
   and the same webhook/reconciliation replay produces one adjustment.
5. Exercise a cross-currency refund and a provider fee. The UI must label a
   missing conversion as unavailable rather than inventing a rate; no displayed
   refund may silently change the settlement graph.
6. Kill and resume the app during checkout, cancellation, expense opt-in, and
   review resolution. Each surface must show cached/stale/reconciling state and
   offer a read-only retry path instead of claiming success.

## Release posture

Keep both halves of live booking disabled until every required evidence row has
a dated device/provider receipt:

- `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED=false`
- `EXPO_PUBLIC_LIVE_BOOKING_ENABLED=false`

The dark cancellation-quote operation is governed by the same mobile flag. A
future promotion must update this record with sandbox IDs, device receipts, and
the exact commit that was tested.
