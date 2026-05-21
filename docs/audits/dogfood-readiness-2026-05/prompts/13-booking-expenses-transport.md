# Prompt 13 — Booking, Expenses, Transport, And Provider Boundaries

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Booking, expenses, transport, provider-backed flows, and scaffolded domains that may appear in the app.

Output:
docs/audits/dogfood-readiness-2026-05/areas/13-booking-expenses-transport.md

Product promise:
Partially scaffolded provider domains should not create false confidence, irreversible actions, stale UI, or broken dogfood paths. Expense flows should be reliable enough for real groups.

Inspect:
- Travel Agent booking_agent, booking routes, provider ABCs, booking offers/session context, live canaries, fallback behavior.
- Expenses routes, settlement, receipt upload/OCR, currency/exchange logic.
- Transport roadmap/gap callouts.
- Travel App booking session detail, accommodations, expenses, settlement, transport callouts.

Start with:
- Travel Agent/backend/booking_agent/FEATURE.md
- Travel Agent/backend/expenses/FEATURE.md
- Travel Agent/docs/working/State of Booking 2026.md
- Travel Agent/docs/working/Booking Live Provider Audit.md
- Travel Agent/docs/working/Transport Roadmap.md
- Travel App/docs/page-specs/booking-group-semantics.md

Audit questions:
1. Are live-provider paths clearly disabled/gated until credentials and canaries pass?
2. Can booking dates, prices, currencies, or provider IDs silently default wrong?
3. Are booking pushes/events idempotent and privacy-safe?
4. Does delegation/autonomy consent gate any booking-like action?
5. Are expense split/settle flows idempotent, currency-safe, and resilient to API errors?
6. Does receipt upload respect auth, size limits, and safe paths?
7. Does UI distinguish scaffolded/not-yet-live provider behavior from real booking success?

Run if cheap:
- targeted booking/expense tests
- make contract-check

Deliver:
Focus on real-world harm: false booking confirmation, wrong settlement, duplicate charges/pushes, or provider routes exposed too early.
```

