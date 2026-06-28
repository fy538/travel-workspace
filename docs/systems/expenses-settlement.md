# Expenses / Settlement — System Charter

> Surface: Trips
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-06-27

## Purpose
Track shared trip costs and compute deterministic settle-up — who owes whom —
so booking and post-trip closeout don't become a separate messy thread. Serves
belief #27 (Monetization Strategy): money is a high-trust, low-tolerance surface
that stays private until the payer **opts in** to share.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/expenses/`](../../travel-agent/backend/expenses/FEATURE.md) (`settlement.py::compute_settlement`, `exchange_rates.py`, `receipt_ocr.py`) + `api/routes/expenses.py`.
- Frontend: `app/trip-expenses?tripId=`, expense add/share sheets, settle-up view.
- Tables of record: expense rows, splits, `receipts` (OCR status + parsed fields).

## Public interface (what other systems may call / read)
- **Entry points:** `settlement.py::compute_settlement(expenses, participants)` (pure, deterministic) · `exchange_rates.py` (multi-currency conversion) · `receipt_ocr.py` (image → parsed expense, writes back `ocr_status`).
- **Inbound writes:** manual add-expense and receipt-derived expense — both validate that `paid_by` and every split `user_id` is a member of the trip before any money row is written.
- **Consumes:** trip membership; booking confirmations *only* when the organizer explicitly opts to share a total (no automatic ingestion).
- **Never:** create an expense from a booking/provider receipt automatically; write a money row for a non-member `paid_by` or split user.

## Owns (source of truth)
Trip expense rows, their splits, and receipt OCR state. The **settlement
computation is deterministic** — it is derived, never persisted as authoritative
"who owes whom" that could drift from the underlying rows.

## Invariants (must always be true)
- **OPT-IN ONLY.** Expenses are never auto-created. Auto-expense (`auto_log` from booking confirmations) was **removed 2026-06-26** — booking/provider receipts are receipt-only and create no shared expense. Sharing a booking total requires organizer opt-in (journey 10 / 12 "must never happen").
- **Trip-member validation is mandatory** — `paid_by` and every split user must be trip members, or no row is written (guards financial identity spoofing, journey 10 seam check).
- **Settlement is deterministic** — same expenses + participants always yield the same who-owes-whom; no LLM in the settle path.
- **Private until shared** — total paid, payment method, confirmation number stay private to the payer until opt-in; settle-up never surfaces private booking totals without it (journey 12).
- **Idempotent creation** — repeated add-expense calls (e.g. retried client request) do not double-write.

## Failure modes
- **Exchange rates degrade gracefully** — Frankfurter (ECB) rates live in a bounded 512-pair cache with a 1h *staleness* window that is **not** an eviction trigger: on a provider outage the last-known-good rate is kept indefinitely and conversion **never raises**.
- Receipt OCR failure → `ocr_status` reflects the error; the user falls back to manual entry; no fabricated amounts.

## Maturity & validation
- Serves journeys: 10 (booking/stay/expense trust loop), 12 (returned trip → settle-up).
- DoD state: idempotency + opt-in + member-validation FE tests ✅ (`AddExpenseSheet.test.tsx`, `useCreateExpenseIdempotency.test.tsx`) · settlement unit coverage ✅ · **live settle-up walk ❌**.
- FEATURE.md maturity is **"scaffolded"** — this is the least-hardened of the wired Trips systems.

## Canonical docs
- why → `product/Monetization Strategy.md` · how (privacy boundary) → `page-specs/booking-group-semantics.md` · what(be) → `backend/expenses/FEATURE.md` · what(fe) → `page-specs/per-person-stays.md`.
- Tests: `__tests__/components/expense/AddExpenseSheet.test.tsx`, `__tests__/hooks/useCreateExpenseIdempotency.test.tsx`.

## Open risks / known gaps
- **Opt-in boundary is the headline trust risk** — now that `auto_log` is gone, any path that resurrects automatic expense creation from booking violates both journeys 10 and 12. Guard against re-introduction.
- "Scaffolded" maturity: the settle-up surface has not been walked end-to-end against live multi-currency data; exchange-rate staleness behavior is sound in code but unverified on-device.
- No proof that the booking → opt-in-share → ledger-entry chain preserves `paid_by` / split identity across the repo seam (journey 10 audit flagged it).
