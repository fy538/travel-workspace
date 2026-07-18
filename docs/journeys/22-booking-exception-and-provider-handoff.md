---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Provider, human, payment, and app states require a dedicated exception lifecycle beyond the happy booking loop.
source_of_truth_for: [journey-J22]
---

# 22 — Booking Exception and Provider Handoff

## Product Promise

The traveler always knows what Vesper, the provider, and the human have actually
completed—and how to continue when those states diverge.

## Canonical User Story

As the assigned booker, I want held, expired, uncertain, confirmed, and cancelled
states described honestly, so that I never mistake preparation for a reservation.

## Starting State and Surfaces

- Selected, held, provider-confirming, confirmed, expired, or unknown offer.
- Routes: `/booking/[sessionId]`, booking cards in Chat, itinerary booking object.
- J10 remains the commercial spine; J15 owns destructive confirmation patterns.

## Canonical Steps

1. Open the booking session from its originating context.
2. Review controller, provider truth, price freshness, and next human action.
3. Confirm, settle, release, retry, cancel, or continue externally.
4. Receive an honest terminal or recoverable receipt.
5. Return to the exact itinerary/chat context; observers converge on group-safe status.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J22.B01` | Assigned booker versus read-only observer | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B02` | Settle unpaid hold with terms and approval | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B03` | Release unpaid hold without cancellation overclaim | `FE`, `BE`, `VIS` |
| `J22.B04` | Expired/stale price refresh and retry | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B05` | Provider unknown/failure remains unresolved | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B06` | Confirmed provider receipt and optional writeback | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B07` | Cancellation boundary and provider responsibility | `FE`, `BE`, `VIS`, `LIVE` |
| `J22.B08` | Exact return and observer reconciliation | `FE`, `VIS`, `LIVE` |

## Must Never Happen

- Selected, held, session-confirmed, or provider-unknown renders as Booked.
- A non-controller can transact under the controller's authority.
- Releasing a hold claims a booked reservation was cancelled.
- External handoff strands the traveler or loses the trip context.

## First Automation Target

One deterministic offer state table covering held, expired, provider-unknown,
confirmed, released, and cancelled, with controller/observer projections.
