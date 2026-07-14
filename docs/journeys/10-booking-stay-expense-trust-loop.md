# 10 - Booking, Stay, And Expense Trust Loop

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-26  
> Primary phase: booking / stay / money

## Product Promise

Booking and stay details should feel group-aware and trustworthy: one person transacts, the group sees the right public state, and private financial details stay private until shared.

## Canonical User Story

As an organizer, I want Vesper to help choose or confirm a stay, share the useful details with the group, and optionally settle the cost, so that booking does not become a separate messy thread.

## Why This Journey Matters

- Booking/accommodations are partially mock-safe but require real checks.
- Provider sessions, confirmation payloads, and payment visibility are easy to fake in mocks.
- Money and booking confirmations are high-trust, low-tolerance surfaces.

## Starting State

- Persona: organizer and non-organizer member variants.
- Trip state: planning trip with lodging need; optional booking session created by chat.
- Fixture: stay/accommodation mock data, booking session route.
- Permissions: external browser/deeplink available.

## Primary Surfaces

- Routes: `/trip-accommodations?tripId=`, `/accommodation/[accommodationId]`, `/booking/[sessionId]`, `/trip-expenses?tripId=`, `/(tabs)/trips/[tripId]/chat`, `/(tabs)/trips/[tripId]/plan`.
- App docs: [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md), [Per-Person Stays](../../travel-app/docs/page-specs/per-person-stays.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md).
- Existing anchors: `__tests__/screens/booking-confirm.test.tsx`, `__tests__/screens/accommodation-detail.smoke.test.tsx`, `__tests__/hooks/useStaySummary.test.ts`, `__tests__/components/expense/AddExpenseSheet.test.tsx`, `__tests__/hooks/useCreateExpenseIdempotency.test.tsx`.

## Canonical Steps

1. Open trip stay facet from Trip Folio.
2. Open accommodations list and accommodation detail.
3. Ask Vesper about the stay or add it to plan.
4. Open a booking session created by chat.
5. The proposal's assigned booker selects or confirms the offer (organizer by default; delegation may assign another member).
6. App routes back to trip detail with a success receipt.
7. Member sees public stay state, not private payment details.
8. Organizer optionally shares total for expense settling.
9. Expense ledger entry appears with booking source.
10. **Hold path:** confirm pay-later hold with `terms_accepted` + `final_human_approval` in request body (`POST /booking/holds/{offer_id}/settle`) — verify `http.ts` sends body matching OpenAPI `SettleHoldRequest`.
11. **Hold expired:** 410 surfaces actionable copy, not generic toast.

## Cross-repo seam checks (2026-06-25 audit)

| Check | Risk if broken |
|---|---|
| `settleBookingHold` sends `SettleHoldRequest` body | Every hold confirm → HTTP 422 |
| Booking nested ids scoped to path `trip_id` | Cross-trip IDOR |
| Expense `paid_by` / share `user_id` validated | Financial identity spoofing |
| UI "Booked" only after provider-confirmed state | Overclaimed trust |

## Expected Outcome

- User-visible state: the assigned proposal owner can transact; other members, including an unassigned organizer, see the appropriate quiet/group state and converge on its terminal result.
- Data state: booking session, selected offer, provider receipt, optional hotel stay writeback, and opt-in expense source ids are stable.
- Cross-surface coherence: stays, chat, plan, booking receipt, and expenses agree.
- Trust state: total paid, payment method, provider confirmation number, and cancellation details remain private until opt-in.

## Must Never Happen

- Non-organizer sees organizer-only payment details.
- Booking confirmation strands the user.
- Provider/deeplink failure renders as booked.
- Expense sharing happens automatically without organizer opt-in.
- Booking proposal leaks private constraints in public justification.

## Current Semantics

- Booking checkout is explicit-consent only. Without `checkout_consent`, cart confirm records an in-app confirmation but does not create a provider order.
- Duffel flight checkout uses provider order creation only after terms acceptance, idempotency claim, passenger references, and exact payment-total validation.
- Provider receipts are receipt-only for flights. They do not create trip stays or shared expenses.
- Confirmed hotel offers may write a `trip_accommodations` row only through the booking accommodation writeback hook, and only when the normalized hotel payload has enough stay/date/location data.
- Shared trip-base stays are organizer-controlled. Members can manage their own personal stay slot; organizers can manage any stay slot.
- Booking proposal decisions are owner-controlled: `proposal.user_id` may confirm or reject, same-outcome retries are idempotent, opposite terminal decisions conflict, and other open cards reconcile while the proposal is pending.
- Expenses remain opt-in. Manual and receipt-derived expenses validate that `paid_by` and every split user are members of the trip before money rows are written.
- Offer refresh is wired through provider `get_price`; Duffel refresh reads the latest offer before checkout so stale search prices are not treated as bookable truth.

## AI Trace Prompt

```text
Trace booking/stay flow from trip accommodations through accommodation detail, group/private chat handoff, booking session, cart confirm, hold settle (verify request body against openapi.json), confirmation, trip return, stay writeback, and opt-in expense sharing. Identify provider-session assumptions, privacy serializer boundaries, organizer/member UI differences, and mock-real drift. Flag any UI state that claims booked before provider confirmation.
```

## First Automation Target

Deterministic tests for:

- booking confirmation route returns to trip
- organizer/member confirmation visibility differs
- expense creation is idempotent, opt-in, and trip-member validated
- accommodation Ask/Add routing preserves trip id
- shared stay mutation requires organizer; personal stay mutation requires self or organizer
- provider refresh updates the persisted offer instead of returning 501
