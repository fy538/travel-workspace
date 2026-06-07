# Journey Status Matrix

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Source of truth for: journey readiness, dogfood promotion, and next engineering action

This matrix turns the 12 canonical journeys into an operating board. A journey is not dogfood-ready because the one-pager exists; it becomes dogfood-ready when route/API tracing, mock-mode walking, deterministic tests, and any required real-backend checks have all been made explicit.

## Status Legend

| Mark | Meaning |
|---|---|
| `not started` | No journey-specific validation has been run yet. |
| `partial` | Some existing tests/docs cover the journey, but not the full user flow. |
| `blocked` | A known issue prevents credible dogfood validation. |
| `ready` | Good enough for the next promotion step. |
| `required` | This journey needs a real-backend or live canary pass before dogfood confidence. |
| `optional` | Real-backend pass is useful, but mock/static validation can cover most risk. |

## Matrix

| # | Journey | Static trace | Mock walk | Deterministic tests | Real backend | Known blockers / risks | Next action | Dogfood ready |
|---|---|---|---|---|---|---|---|---|
| 01 | [Vague Idea To Vesper-Shaped Trip](01-vague-idea-to-vesper-shaped-trip.md) | ready | not started | partial | required | Fixed: forced home-conversation promotion path and prefill wait. Remaining: mock/real promotion response shapes drift and missing prefill/promotion regression tests. | Add prefill/promotion regression tests and align mock/real promotion response shape. | no |
| 02 | [Concrete Trip Creation And Invite](02-concrete-trip-creation-and-invite.md) | ready | not started | partial | optional | Fixed: pending invite follow-up preserves `tripId`. Remaining: mock invite tokens are not bound to created trip; invite mint does not refresh organizer pending list. | Fix mock token/member mutation and add screen-level mock walkthrough. | no |
| 03 | [Cold Trip Setup To Useful Workspace](03-cold-trip-setup-to-useful-workspace.md) | partial | not started | partial | optional | Fixed: known trip-home info/expenses CTAs preserve `tripId`. Remaining: place setup is chat/LLM-mediated; patched dates/place can drift from TripContext-backed Folio mode in mock mode; mock accommodation persistence is non-real. | Add deterministic blank -> patch dates/place -> reload -> pre workspace test, or mark place resolution as live canary. | no |
| 04 | [Private Constraint To Group-Safe Plan](04-private-constraint-to-group-safe-plan.md) | ready | not started / blocked by fixture gap | partial | required | Fixed: booking notes and notification fan-out copy now pass deterministic private-signal redaction, and privacy audit renders redaction/private-constraint-use proof events without raw private values. Remaining: plan private-influence flag exists but is not emitted; no full deterministic group-chat/proposal leak fixture yet. | Add deterministic private-constraint fixture across group chat, proposal, notification, booking, plan badge, and Atlas/privacy receipt. | no |
| 05 | [Group Planning To Proposal To Plan Mutation](05-group-planning-to-proposal-to-plan-mutation.md) | ready | partial | partial | ready | Fixed: pending-vote notifications route to proposal review; proposal writes send idempotency keys; backend proposal detail and plan-event ledger now carry structured receipt payloads; canonical mock accept/revert mutates visible read models; real-backend canary now accepts/applies/reverts and verifies proposal detail, Plan/Changes source read model, Home, Map, Notifications, and chat receipts agree. Remaining: app-level UI walk still needs to prove the visible Changes surface against the backend canary fixture. | Promote the proposal canary into the dogfood/CI gate and add an app-level Changes surface walk on top of the backend recent-changes assertion. | no |
| 06 | [Home, Plan, Map, Changes Coherence](06-home-plan-map-changes-coherence.md) | ready | partial | partial | optional | Fixed: canonical Lisbon proposal/block ids now align across mock itinerary, plan-state, map-state, home cards, pending-vote notifications, proposals, and recent changes, with regression tests for Plan, Changes, Home, Map, and Notifications. Remaining: non-canonical mock proposals and chat preview invalidation are incomplete. | Expand parity beyond the canonical Lisbon proposal and add chat preview invalidation coverage. | no |
| 07 | [Discover To Contextual Vesper To Trip Action](07-discover-to-contextual-vesper-to-trip-action.md) | ready | not started | partial | required | Fixed: conversation-scoped backend streams preserve seed metadata. Remaining: search fallbacks are prompt-only; trip context propagation is inconsistent. | Add CTA-to-seed tests and close remaining entity/trip-context gaps. | no |
| 08 | [Live Trip What-Now Companion](08-live-trip-what-now-companion.md) | partial | not started | partial | required | Live CTA affordance risks; route/currentTripId drift in Folio and Chat; mock Lisbon is not actually live in situation/plan mocks; no current/next-stop test. | Fix or de-afford Vesper live/urgent CTAs, align tripId/seed grounding, and make `trip-lisbon-26` a real active mock fixture. | blocked |
| 09 | [Notifications And Proactive Routing](09-notifications-and-proactive-routing.md) | ready with gaps | not started | partial | required | Feed tap routing is mostly covered, but OS push tap routing lacks the journey-priority matrix; social route drifts from `/atlas/companions`; proactive read-state invalidation is incomplete. | Add PushRegistrar routing matrix tests and make push routing share feed routing semantics. | no |
| 10 | [Booking, Stay, And Expense Trust Loop](10-booking-stay-expense-trust-loop.md) | ready | not started | partial | required | Fixed: booking route preserves `tripId`, backend session ownership is enforced, and confirm no longer auto-logs shared expenses. Remaining: stay authorization, stay-write semantics, refresh 501, and thin mocks. | Add organizer/member stay authorization, booking route tests, and opt-in expense UX tests. | no |
| 11 | [Atlas Candidate To Memory Control](11-atlas-candidate-to-memory-control.md) | ready | partial | partial | required | Fixed: privacy self-loop, mislabeled receipt CTA, `/api/atlas/places`, mock approve 409 parity, inbox dismiss pruning, timeline/almanac projection (V1–V4), dedup + restore canary, `archive_reason`, removed-moments API + screen, inbox/receipt/journey-11 mock-walk smoke tests. Remaining: candidate detail + learned-signal screen tests; map year spine (Direction 03 deferred). | Run Postgres canary + projection v4 spot-check in staging; expand candidate/signal screen tests. | no |
| 12 | [Returned Trip To Story, Memory, And Settle-Up](12-returned-trip-to-story-memory-settle-up.md) | ready | not started | partial | required | Fixed: settlement closeout preserves `tripId`. Remaining: Memory route depends on `currentTrip`; mock story/summary/Atlas fixtures drift from real post-trip behavior; date logic mixes local/server/UTC. | Add Journey 12 route test and fix route-param handling for Memory before live returned-trip dogfood. | no |

## Promotion Rules

A journey can move from `no` to dogfood-ready only when:

- Static trace is `ready`.
- Mock walk is `ready`.
- Deterministic tests are `ready` or the missing coverage is explicitly accepted.
- `required` real-backend checks have a pass/fail rubric and at least one clean run.
- Known blockers are fixed or deliberately de-afforded.

## Current Priority Order

1. **Finish privacy proof end-to-end:** Journey 04 full deterministic leak fixture across group chat, proposal, notification, booking, plan badge, and Atlas/privacy receipt.
2. **Promote proposal coherence beyond the backend canary:** Journey 05 canary now passes; next is making it a standing dogfood/CI gate and adding an app-level Changes surface walk.
3. **Make mock mode useful instead of flattering:** Journey 08 live Lisbon fixture, Journey 10 booking/stay/expense mocks, Journey 12 returned-trip fixtures, plus non-canonical Journey 06 proposal parity.
4. **Fix or de-afford remaining misleading CTAs:** Journey 08 live/urgent affordances, Journey 07 no-trip share action, and Atlas routes beyond the fixed self-loop.
5. **Backfill deterministic route/API tests for the P0 fixes:** Journey 01 prefill/promotion, Journey 07 CTA seed matrix, Journey 10 booking route/ownership/expense opt-in.
6. **Promote to mock UI walks only after deterministic route/API tests land.**

## First Static Trace Batch

Run these three first because they carry the largest trust and dogfood risk:

```text
Read docs/journeys/04-private-constraint-to-group-safe-plan.md and trace the journey through Travel App and Travel Agent. Report route wiring, components, hooks, API calls, mock behavior, backend endpoints, redactor boundaries, missing tests, and likely real-backend drift. Do not call live LLM-backed endpoints.
```

```text
Read docs/journeys/05-group-planning-to-proposal-to-plan-mutation.md and trace the proposal lifecycle through Travel App and Travel Agent. Report route wiring, components, hooks, API calls, mock behavior, backend endpoints, idempotency, read-model invalidation, missing tests, and likely real-backend drift. Do not call live LLM-backed endpoints.
```

```text
Read docs/journeys/09-notifications-and-proactive-routing.md and trace feed rendering, push/deep-link handling, read state, badge counts, routing priority, notification preferences, privacy-safe copy, missing tests, and likely real-backend drift. Do not send real notifications.
```

## Open Questions

- Should Journey 08 include voice/narration in the first dogfood pass, or keep voice as a later specialized journey?
- Should booking dogfood use real provider deeplinks immediately, or first validate a fake-provider confirmation payload against real backend serialization?
- Should Atlas photo scan be in Journey 11 now, or split into its own journey once real photo-library dogfood starts?
