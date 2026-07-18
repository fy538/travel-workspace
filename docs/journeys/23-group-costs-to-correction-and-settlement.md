---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Expense intake, correction, dispute, and payment form a durable money lifecycle independent of booking.
source_of_truth_for: [journey-J23]
---

# 23 — Group Costs to Correction and Settlement

## Product Promise

A group can turn a real cost into an understandable split, correct or dispute it,
and record settlement without duplicating or misdirecting money.

## Canonical User Story

As a traveler sharing costs, I want payer, participants, direction, and payment
state to remain clear from intake through settlement.

## Starting State and Surfaces

- Group trip with manual, receipt-derived, or provider-linked cost.
- Routes: `/trip-expenses/*`, booking Share in Costs continuation.
- J12 owns returned-trip closeout; J15 owns destructive confirmation/cascade.

## Canonical Steps

1. Add a manual/receipt/provider-linked cost and verify source.
2. Choose payer, currency, participants, and split.
3. Review ledger and balance direction as another participant.
4. Correct or dispute the cost without losing provenance.
5. Record partial/full settlement; reopen and confirm durable balances.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J23.B01` | Manual and receipt intake | `FE`, `BE`, `VIS`, `LIVE` |
| `J23.B02` | Payer/member validation and privacy | `FE`, `BE`, `VIS` |
| `J23.B03` | Equal, exact, percentage, and itemized split | `FE`, `BE`, `VIS` |
| `J23.B04` | Edit/delete authority with payment lock | `FE`, `BE`, `VIS` |
| `J23.B05` | Participant dispute and resolution | `FE`, `BE`, `VIS`, `LIVE` |
| `J23.B06` | Currency/rate and owed-direction truth | `FE`, `BE`, `VIS` |
| `J23.B07` | Partial/full settlement and payment retry | `FE`, `BE`, `VIS`, `LIVE` |
| `J23.B08` | Provider-linked opt-in deduplicates | `FE`, `BE`, `VIS`, `LIVE` |

## Must Never Happen

- A nonmember becomes payer or participant.
- A retry duplicates expense or settlement payment.
- “You owe” reverses direction across screens.
- Editing history erases a dispute, payment, or source receipt.

## First Automation Target

Three-member expense with itemized split, dispute, partial payment, retry, and
final settlement; prove ledger and balance screen agree after every transition.
