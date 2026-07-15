# Expenses / Settlement — System Charter

> Surface: Trips
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-07-15

## Purpose
Track shared trip costs and compute deterministic settle-up — who owes whom —
so booking and post-trip closeout don't become a separate messy thread. Serves
belief #27 (Monetization Strategy): money is a high-trust, low-tolerance surface
that stays private until the payer **opts in** to share.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/expenses/`](../../travel-agent/backend/expenses/FEATURE.md) (`settlement.py::compute_settlement`, `exchange_rates.py`, `accommodation_cost.py`, `receipt_ocr.py`) + `api/routes/expenses.py` + `concierge/tool_handlers/expenses.py` (chat-initiated log/settle).
- Frontend: `app/trip-expenses?tripId=`, `app/trip-expenses/[expenseId]/edit`, `app/trip-expenses/balance`, expense add/edit/detail sheets.
- Tables of record: `expenses`, `expense_shares`, `settlement_payments` (the clearing ledger), `receipts` (OCR status + parsed fields).

## Public interface (what other systems may call / read)
- **Entry points:** `settlement.py::compute_settlement(expenses, shares, user_names, settlement_currency, trip_id, *, payments=)` (pure, deterministic) · `exchange_rates.py::compute_settlement_fields[_sync]` (the one place rate-lookup + conversion happens — every writer goes through it) · `receipt_ocr.py` (image → parsed expense, writes back `ocr_status`).
- **Inbound writes:** manual add-expense (FE sheet), explicit organizer booking share (`booking_offer_id`, `source="booking_opt_in"`), receipt-derived expense, chat-initiated `log_expense`/`settle_expense_shares` (concierge tool_handlers), and the accommodation-cost sync (below) — every path validates `paid_by` and every split `user_id` against trip membership before a money row is written.
- **Consumes:** trip membership; booking confirmations *only* when the organizer explicitly opts to share a total (no automatic ingestion) — **except** the accommodation-cost sync, a narrow, intentional exception (see Invariants).
- **Never:** create an expense from a non-accommodation booking/provider receipt automatically; write a money row for a non-member `paid_by` or split user; let anything but a recorded `settlement_payment` clear debt from the balance graph.

## Owns (source of truth)
Trip expense rows, their splits, the `settlement_payments` ledger, and receipt
OCR state. The **settlement computation is deterministic** — it is derived
from expenses/shares/payments, never persisted as authoritative "who owes
whom" that could drift from the underlying rows.

## Invariants (must always be true)
- **`settlement_payments` is the SOLE debt-clearing mechanism.** Every share always contributes its full debit to the balance graph regardless of `is_settled` — only a recorded payment nets it out (symmetrically: reduces the payer's debt and the receiver's credit by the same amount). `is_settled` is **display-only** metadata (the per-share checkmark), written atomically alongside the payment that clears it. This replaced an older mechanism where `is_settled` directly removed a share's debit — that broke for any net, already-simplified transfer spanning multiple shares/expenses (a chained hotel+dinner settle could leave a phantom debt on an unrelated expense right after the UI declared everyone even). See `settlement.py`'s module + `compute_settlement` docstrings for the full incident.
- **Payments are append-only; a void marker is the only correction path.** A mis-recorded payment is never deleted or amount-edited — `void_settlement_payment` marks it (`voided_at`/`voided_by`, both-or-neither via a CHECK constraint), it stays visible in `GET /settlements` history as voided, and drops out of the balance graph immediately. Voiding a per-share payment un-settles its linked share in the same transaction, so the checkmark and the ledger can never disagree.
- **Masked expenses never enter the settlement graph, for anyone — including the payer.** A masked expense (a surprise/gift the payer covers fully) is validated to only ever carry the payer's own share; counting it as the payer's credit with no offsetting debit would leak its existence/rough size through a distorted transfer amount to someone else, even with the amount itself hidden. Amount, title, description, `block_title`, and `receipt_id` are all redacted for a non-payer viewer (`_is_masked_from_viewer`/`_redact_masked_expense`) — hiding only the amount defeats the point.
- **OPT-IN ONLY, with one scoped exception.** General booking/provider-receipt auto-logging (`auto_log.py`) was removed 2026-06-26 and must not be reintroduced. A general booking enters Costs only when an organizer explicitly submits `booking_offer_id`; the API proves that offer belongs to the path trip and has `status="confirmed"`, derives its itinerary block, rejects masked linkage, stamps `source="booking_opt_in"`, and uses the server-owned key `booking-opt-in:{offer_id}`. One partial unique index permits at most one opt-in expense per offer. Session `status="confirmed"` is not sufficient booking truth. The **accommodation-cost sync** (`accommodation_cost.py`, `source="accommodation_auto"`) remains the narrow exception scoped only to stays.
- **Trip-member validation is mandatory** — `paid_by` and every split user must be trip members, or no row is written (guards financial identity spoofing, journey 10 seam check). This applies uniformly across the HTTP routes, receipt-derived creation, and the concierge tool handlers.
- **A `split_type` change requires resending shares.** There is no way to derive per-share percentages/exact-amounts/item-labels from an existing split under a different type — the update route 400s a `split_type` change with no `shares` payload rather than silently leaving shares with no data for the new type. The edit sheet treats split type as display-only for this reason.
- **`rate_source` provenance is always recorded** alongside `settlement_amount`/`exchange_rate` — `same_currency` / `live` / `stale` / `sentinel` / `repaired`. A `sentinel` row (Frankfurter unreachable, no cached rate) carries a silently-wrong `settlement_amount` until `scripts/repair_sentinel_exchange_rates.py` fixes it; the provenance is what makes that queryable/fixable at all instead of indistinguishable from a real rate.
- **An expense with live (unvoided) payments can't be deleted** — `DELETE` 409s with a "void the payments first" message rather than orphaning the payments' context.
- **Settlement is deterministic** — same expenses + shares + payments always yield the same who-owes-whom; no LLM in the settle path (the concierge tools call the same deterministic writers, never compute money themselves).
- **Idempotent creation** — repeated add-expense / record-payment calls (e.g. a retried client request) do not double-write, via `idempotency_key`. Expense retry equivalence includes booking provenance, block, split type, and the computed share allocation; a changed financial body conflicts rather than silently returning the old row.

## Failure modes
- **Exchange rates degrade gracefully** — Frankfurter (ECB) rates live in a bounded 512-pair cache with a 1h *freshness* window that is **not** an eviction trigger: on a provider outage the last-known-good rate is kept indefinitely (`stale` provenance) and conversion **never raises**; with no cached rate at all it falls back to 1.0 (`sentinel` provenance) rather than failing the whole expense write.
- Receipt OCR failure → `ocr_status` reflects the error; the user falls back to manual entry; no fabricated amounts.
- A currency without full ISO decimal-precision data (rare) falls back to 2 decimal places in `formatMoney` rather than crashing.

## Maturity & validation
- Serves journeys: 10 (booking/stay/expense trust loop), 12 (returned trip → settle-up).
- DoD state: idempotency + opt-in + member-validation + settlement-ledger + void-marker + currency-truth FE tests ✅ (backend: `tests/expenses/`, `tests/api/test_expenses_api.py`, `tests/concierge/test_expense_tools_db_parity.py`, real-Postgres e2e in `tests/expenses/test_settlement_payments_e2e.py`; FE: `__tests__/components/expense/`, `__tests__/hooks/`, `__tests__/utils/costsViewModel*.test.ts`, `__tests__/utils/formatMoney.test.ts`) · **live settle-up walk ❌**.
- FEATURE.md maturity is **"scaffolded"** — code hardening is well ahead of on-device validation; this remains the gap.

## Canonical docs
- why → `product/Monetization Strategy.md` · how (privacy boundary) → `page-specs/booking-group-semantics.md` · what(be) → `backend/expenses/FEATURE.md` · what(fe) → `page-specs/per-person-stays.md`.
- Tests: see Maturity & validation above.

## Open risks / known gaps
- **Opt-in boundary is the headline trust risk** — any path that resurrects general automatic expense creation from booking (beyond the scoped accommodation-cost exception) violates journeys 10 and 12. Guard against re-introduction.
- "Scaffolded" maturity: the settle-up surface — including the payments-history/void UI and the currency-truth fixes — has not been walked end-to-end against live multi-currency data; the code-level behavior is well-tested in isolation but unverified on-device.
- Booking → opt-in-share → ledger-entry is now code- and contract-tested across the repo seam, including organizer authorization, confirmed-offer/trip ownership, durable source/link, stable idempotency, and explicit payer/splits. A live multi-member on-device walk remains outstanding.
- `settlement.py::compute_settlement`'s `payments` param defaults to `None`/`[]` for callers that don't have payment data — any NEW caller that forgets to thread real payments through will silently see gross (un-netted) balances. There's no runtime guard against this; it relies on callers following the pattern in `get_settlement_data_with_currency`.
