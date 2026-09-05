---
doc_type: working
status: active
owner: capability-retirement / Contribution and Capture / Integration
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Converts the surface-contraction recommendation into a bounded expense result, deterministic-owner, and migration contract while preserving exact money and participant semantics.
supersedes: []
depends_on:
  - product-surface-contraction-investigation-2026-09-04.md
  - ../systems/contribution-and-consequence.md
  - ../../travel-agent/backend/core/models/expenses.py
  - ../../travel-agent/backend/expenses/settlement.py
source_of_truth_for:
  - assisted-expense-contraction-scope
---

# Assisted expenses: small result, exact ledger

## Recommendation

Expense should become an assisted understanding and correction capability,
not a second accounting application. A person can share a receipt or say what
they paid; Vesper should return a compact, useful interpretation immediately.
Only an explicit supported instruction creates or changes shared debt. The
ledger remains deterministic and inspectable underneath the lighter surface.

The first implementation stays within the existing **Trip expense owner**.
Receipt understanding without a Trip can be prepared as a private source
result, but shared non-Trip debt is blocked until its owner, participant, and
authority contract is chosen through the Integration/Plan lane. Do not create a
pseudo-Trip to satisfy the current API.

No new accounting model, automatic debt, provider booking dependency, or
repository-wide form rewrite is authorized by this brief.

## What exists today

| Existing capability | Code evidence | Constraint to preserve |
| --- | --- | --- |
| Receipt OCR | `backend/expenses/receipt_ocr.py`, `ReceiptOcrResult` | OCR facts are suggestions; unreadable/partial quality stays explicit |
| Expense owner | `backend/core/db/expenses.py`, `backend/api/routes/expenses.py` | `ExpenseCreate` is Trip-scoped and validates members, receipts, blocks and authority |
| Receipt-to-expense | `POST /api/trips/{trip_id}/receipts/{receipt_id}/create-expense` | Amount is user-confirmed; OCR total never silently becomes persisted money |
| Conversational entry | `backend/concierge/tool_handlers/expenses.py` | `expense_log`, summary, and settle currently require Trip context; equal split only in the tool |
| Settlement | `backend/expenses/settlement.py`, `money.py`, `exchange_rates.py` | Deterministic rounding, original currency, payment/void semantics, rate provenance |
| Mobile treatments | `AddExpenseSheet`, `ExpenseDetail`, `CostsBalanceSheet`, five `trip-expenses` routes | Useful detail, payment lock, dispute/review and dense balance history remain reachable |
| Booking-linked cost | `accommodation_cost.py`, `booking_offer_id`, adjustments | Booking cancellation/refund cannot silently rewrite a settled ledger |

The current surface is larger than the owner contract needs. That is a reason
to consolidate treatments, not to remove exact correction and payment history.

## The result grammar

| User input / job | Immediate result | Consequence |
| --- | --- | --- |
| Receipt alone | Merchant, amount, currency, date/line items when legible; quality and missing fields visible | Private source custody; no allocation or debt |
| “I paid $126; split equally among the three of us” | Payer, named participants, `$42` each, source/context, exact scope | Apply only under current authority; ask once for a material missing fact |
| “What do we owe?” | Compact current balance with exact currency and unresolved-rate warning | Read deterministic ledger; no generated arithmetic |
| “That was $140, not $126” | Proposed correction with source and affected shares | Existing owner mutation, payment lock and append/void semantics apply |
| “Remove the dessert gift from what they owe” | Masked/private treatment preview | No shared debt from masked gifts; preserve payer’s private evidence |
| Cancelled booking or refund | Dated provider adjustment and current ledger effect | Existing booking/expense owner decides; no automatic invented repayment |

Generated prose may explain the result. It cannot create participants, authorize
a split, round money, clear debt, or claim a payment succeeded.

## Exact invariants

- Preserve original amount/currency and settlement amount/currency separately.
- Use the existing currency precision and deterministic remainder placement.
- Require named, current Trip members for a shared split; no inferred guests.
- Keep equal/exact/percentage semantics distinct; the concierge tool must not
  silently downgrade an unsupported split to equal.
- Keep payment recording append-only; void is the correction path.
- A live payment locks unsafe edit/delete operations and exposes its existing
  recovery affordance.
- A masked gift is excluded from other viewers’ debt while remaining available
  to the payer under the existing privacy rules.
- `sentinel` or missing exchange-rate provenance is never presented as a
  definitive converted balance.
- A duplicate receipt or command reuses the existing idempotency identity.
- A source correction updates dependent presentation without rewriting the
  original evidence or another participant’s authored outcome.

## Surface contraction

Consolidate the five `trip-expenses` routes into a small set of owner-backed
treatments over time:

1. One compact receipt/result reader for ordinary understanding.
2. One expanded inspection for shares, source, rate, payment lock, comments and
   disputes when needed.
3. One balance treatment that expands dense history in place.
4. One focused correction/payment/review treatment, reached contextually from
   the reader rather than a standing administration hub.

Historical exact-ID links remain supported through adapters until callers are
measured. Do not hide privacy, account deletion, dispute, payment or departure
controls behind Chat. Do not recreate the five screens as five equally complex
sheets.

Home may surface a useful expense consequence when it affects the current day;
Life can retrieve the durable receipt/ledger record; Chat can accept a receipt
or correction and hand the result to the owner. None becomes a second expense
authority.

## Ownership and handoffs

| Boundary | Owner | This package may do |
| --- | --- | --- |
| Receipt custody and authored note | Contribution and Capture | Preserve source, note, retention and retry identity; expose a receipt-only result |
| OCR interpretation | Existing receipt OCR owner | Return legible facts and quality; never infer missing money |
| Trip expense/settlement | Expense owner | Keep deterministic create/read/correct/payment/dispute behavior |
| Shared non-Trip debt | Integration/Plan decision | Define an owner before any implementation; no pseudo-Trip |
| Chat composition | Contribution and Capture + Integration | Wire a result/command handoff; no second ledger or composer |
| Home consequence | Home | Render an accepted owner result when timely; no arithmetic or debt authority |
| Life continuity | Life | Store/refind source and exact ledger record; no automatic grouping here |
| Booking adjustment | Booking/expense owners | Preserve provider references and fact versions; no silent ledger rewrite |

## Implementation sequence

1. Freeze the result and inspection contract against the current expense models,
   APIs, settlement helpers and mobile primitives. Inventory every current add,
   edit, detail, balance, payment, dispute, booking-linked and deletion caller.
2. Add/read a receipt-only interpretation path that preserves source custody and
   never allocates debt. If it needs a new API field, have the owner review it
   and run the normal OpenAPI/mobile generation workflow.
3. Make the supported Trip command path reuse exact participant, split, currency,
   idempotency and payment-lock validation. Unsupported participant or split
   requests remain explicit, not silently downgraded.
4. Build one compact reader and one expanded inspection over existing owner
   data. Preserve exact source, rate provenance, ledger and correction actions.
5. Route historical links and contextual Home/Chat/Life openings to those
   treatments. Keep compatibility URLs until caller/recovery evidence permits
   removal.
6. Delete exclusive forms, route implementations, mocks and provider-coupled
   expense UI only after all retained jobs and exception paths are covered.

## Acceptance matrix

| Case | Must prove |
| --- | --- |
| Complete/partial/unreadable OCR | Useful facts and honest missing fields; no automatic debt |
| Receipt-only, no Trip | Private retained source or explicit unsupported state; no pseudo-Trip |
| Equal split | Exact payer/participants, rounding and remainder |
| Exact/percentage unsupported in Chat | Clear refusal or owner handoff; never equal fallback |
| Missing/ambiguous participant | One clarification or no mutation |
| Masked gift | Other viewers see no debt; payer can inspect |
| Stale/sentinel rate | Original amount retained; definitive conversion withheld |
| Duplicate/timeout | Existing idempotency and retry identity preserve one result |
| Correction after payment | Payment lock and void/append semantics remain intact |
| Booking cancellation/refund | Adjustment provenance and no invented repayment |
| Account departure/export/delete | Historical permissions and redacted export remain valid |

## Exit criteria

- The user can give a receipt and receive a useful result without filling a
  category/date/share form when those facts are already known.
- Shared debt changes only through an authoritative, explicit owner command.
- One compact reader plus focused inspection covers ordinary and exception jobs.
- Home, Chat and Life consume the same owner result, with no duplicate ledger.
- Existing exact links, correction, payment, dispute, privacy and export jobs
  remain usable during migration.
- Backend and mobile tests exercise identical numerical outcomes.
- No production shutdown, non-Trip debt, schema expansion or deletion is
  inferred from this local implementation brief.
