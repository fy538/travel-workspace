# Journey Status Matrix

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-28 (QA streamlining: merged J02/J06 tests, certify-visual, dogfood-status)
> Source of truth for: journey readiness, dogfood promotion, and next engineering action

Evidence: [STATIC_TRACE_PUNCH_LIST.md](STATIC_TRACE_PUNCH_LIST.md) — 2026-06-26 four-agent re-trace of all 12 journeys.
Visual gate: [visual-certification-matrix.md](../../travel-app/docs/logic-qa/visual-certification-matrix.md) pairs screenshots/device checks with the Logic QA journeys.

## Status Legend

| Mark | Meaning |
|---|---|
| `not started` | No journey-specific validation has been run yet. |
| `partial` | Some existing tests/docs cover the journey, but not the full user flow. |
| `blocked` | A known issue prevents credible dogfood validation. |
| `ready` | Good enough for the next promotion step. |
| `required` | Real-backend or live canary needed before dogfood confidence. |
| `optional` | Real-backend pass useful; mock/static can cover most risk. |
| `pending` | Gate exists but not yet run green on device / live. |

## Matrix

| # | Journey | Static | Mock-walk | Logic | Maestro | Live | Certified |
|---|---|---|---|---|---|---|---|
| 01 | [Vague Idea](01-vague-idea-to-vesper-shaped-trip.md) | ready | ready | ready | optional | optional | no |
| 02 | [Create + Invite](02-concrete-trip-creation-and-invite.md) | ready | ready | ready | pending (24) | optional | no |
| 03 | [Cold Setup](03-cold-trip-setup-to-useful-workspace.md) | ready | ready | ready | optional | optional | no |
| 04 | [Private → Group-Safe](04-private-constraint-to-group-safe-plan.md) | ready | ready | ready | optional | required | no |
| 05 | [Proposal → Plan](05-group-planning-to-proposal-to-plan-mutation.md) | ready | ready | ready | pending (25) | required | no |
| 06 | [Coherence](06-home-plan-map-changes-coherence.md) | ready | ready | ready | partial (25) | optional | no |
| 07 | [Discover → Vesper](07-discover-to-contextual-vesper-to-trip-action.md) | ready | ready | ready | optional | optional | no |
| 08 | [Live Companion](08-live-trip-what-now-companion.md) | ready | ready | ready | optional | optional | no |
| 09 | [Notifications](09-notifications-and-proactive-routing.md) | ready | ready | ready | optional | optional | no |
| 10 | [Booking / Stay / Expense](10-booking-stay-expense-trust-loop.md) | ready | ready | ready | optional | required | no |
| 11 | [Atlas Memory](11-atlas-candidate-to-memory-control.md) | ready | ready | ready | optional | optional | no |
| 12 | [Post-Trip](12-returned-trip-to-story-memory-settle-up.md) | ready | ready | ready | optional | optional | no |

**Certified** = mock-walk + logic + Maestro + live all green for that journey (none yet).

## Summary

| Metric | Count |
|---|---|
| Static trace ready | 12 / 12 |
| Mock-walk ready | 12 / 12 |
| Logic QA MVP green | 12 / 12 (`J01`–`J12`) |
| Maestro wedge flows (24/25) | pending device run |
| Dogfood ready | **0 / 12** |

## Certify ladder (workspace)

| Tier | Command | What it runs |
|---|---|---|
| Fast (daily / PR) | `make certify-fast` | `contract-check` → journey Jest → offline backend pytest |
| Logic (pre-merge) | `make certify-logic` | `pytest tests/scenarios/ -m requires_postgres` (J01–J12 + J05 plan-edit) |
| Visual (wedge) | `make certify-visual` | Maestro 24 + 25 |
| Substrate | `make dogfood-status` | Manifest validate + scenario/pack summary |
| Full offline | `make offline-qa` | doctor, contract, api-coverage, boundaries, backend, journeys, typecheck, test:offline |

Live dogfood (S4 seed + two-account walk) is human/ops — see `docs/working/wedge-journey-02-05-path-to-dogfood.md`.

## Promotion Rules

Unchanged — see [README.md](README.md). None of the 12 meet all gates.
