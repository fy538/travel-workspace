# Journey Status Matrix

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-26 (post full adversarial trace)
> Source of truth for: journey readiness, dogfood promotion, and next engineering action

Evidence: [STATIC_TRACE_PUNCH_LIST.md](STATIC_TRACE_PUNCH_LIST.md) — 2026-06-26 four-agent re-trace of all 12 journeys.

## Status Legend

| Mark | Meaning |
|---|---|
| `not started` | No journey-specific validation has been run yet. |
| `partial` | Some existing tests/docs cover the journey, but not the full user flow. |
| `blocked` | A known issue prevents credible dogfood validation. |
| `ready` | Good enough for the next promotion step. |
| `required` | Real-backend or live canary needed before dogfood confidence. |
| `optional` | Real-backend pass useful; mock/static can cover most risk. |

## Matrix

| # | Journey | Static trace | Mock walk | Deterministic tests | Real backend | Known blockers / risks | Next action | Dogfood ready |
|---|---|---|---|---|---|---|---|---|
| 01 | [Vague Idea](01-vague-idea-to-vesper-shaped-trip.md) | ready | ready | partial | required | Trips Home phases + Phase 0 push only on group chat; mock stream may not emit `promoted_trip_id`; legacy `handleNewChat` eager-creates trip. | Live promotion canary. | no |
| 02 | [Create + Invite](02-concrete-trip-creation-and-invite.md) | ready | ready | partial | optional | Mock token + invite list refresh **fixed**. Accept lands on trip folio **fixed**. | Live invite-accept canary (optional). | no |
| 03 | [Cold Setup](03-cold-trip-setup-to-useful-workspace.md) | ready | ready | partial | optional | PATCH → folio coherence **fixed** (`invalidateTripReadModels` + `useTrip` on folio landing). `trip-info` deep link **fixed**. | Blank → patch → reload live check (optional). | no |
| 04 | [Private → Group-Safe](04-private-constraint-to-group-safe-plan.md) | ready | ready | partial | required | Card egress guards **fixed**. `PRIVATE_PHRASE` fixture test added (BE) + FE leak-phrase mock walk. | Live dogfood leak walk. | no |
| 05 | [Proposal → Plan](05-group-planning-to-proposal-to-plan-mutation.md) | ready | ready | partial | ready | Backend canary passes. Idempotency **fixed**. `journey-05-mock-walk` test committed. | CI gate canary; live revert walk. | no |
| 06 | [Coherence](06-home-plan-map-changes-coherence.md) | ready | ready | partial | optional | `invalidateTripReadModels` exists. Home dismiss invalidates server feed cache **fixed**. Block-id parity now covered by J06 mock walk (read-model layer). | Live cross-surface canary (optional). | no |
| 07 | [Discover → Vesper](07-discover-to-contextual-vesper-to-trip-action.md) | ready | ready | partial | required | Experience seed + mock social event types **fixed**. Mock walk realigned to deep-link routing. | Live discover canary. | no |
| 08 | [Live Companion](08-live-trip-what-now-companion.md) | ready | ready | partial | required | Composer preserves live trip scope **fixed** 2026-06-26. Plan/map/tiles OK. Heartbeat body missing presence fields. | Live "what now" canary. | no |
| 09 | [Notifications](09-notifications-and-proactive-routing.md) | ready | ready | partial | required | Feed routing + `story_ready` fixed. Routing SSOT (`notificationDestination.ts`) pinned + private/group split. Quiet hours E2E unverified. | Live device canary. | no |
| 10 | [Booking / Stay / Expense](10-booking-stay-expense-trust-loop.md) | ready | ready | partial | required | Hold-settle body + IDOR **fixed**. Auto expense on confirm **removed** 2026-06-26 (opt-in only). Pending provider may still success-navigate. | Honest pending UX; explicit expense opt-in endpoint. | no |
| 11 | [Atlas Memory](11-atlas-candidate-to-memory-control.md) | ready | ready | ready | required | Core loop + dedup canary strong; facets seam **fixed**. Mock walk realigned to settings-row privacy screen. | Optional staging checklist; profile TOC polish. | no |
| 12 | [Post-Trip](12-returned-trip-to-story-memory-settle-up.md) | ready | ready | partial | required | Surfaces wired; `journey-12-mock-walk` committed (tripId-preserving closeout + phase + story provenance). | Align returned-trip fixtures; live closeout canary. | no |

## Summary (2026-06-26 trace)

| Metric | Count |
|---|---|
| Static trace ready | 12 / 12 |
| Mock walk ready | 12 / 12 (all committed + green, 2026-06-27) |
| Blocked on mock walk | 0 (P0s fixed 2026-06-26) |
| Dogfood ready | **0 / 12** (mock walks done; gated on real-backend canaries + live dogfood) |

### P0 fix order — **completed 2026-06-26**

1. ~~**J08** — stop `clearTrip()` on Vesper Home composer during live trip~~
2. ~~**J02** — mock invite token → trip mapping~~
3. ~~**J10** — reconcile auto expense log with opt-in semantics~~

### P1 fix order — **mostly completed 2026-06-26**

4. ~~**J04** — close card egress bypass paths (venue/shapes/plan-ready)~~
5. ~~**J02/J03** — `trip-info` works with `?tripId=` only~~
6. ~~**J06** — home feed cache invalidation on dismiss~~
7. ~~**J05** — stable idempotency in ProposalReviewSheet~~
8. ~~**J09** — push destination fallback when payload incomplete~~
9. ~~**J07** — experience Ask Vesper carries `tripId`~~

**Remaining P1:** None — static-trace blockers addressed. Mock walks done (12/12 committed + green, 2026-06-27). Next: real-backend canaries + live dogfood.

## Promotion Rules

Unchanged — see [README.md](README.md). None of the 12 meet all gates.

## Open Questions (resolved for this pass)

| Question | Answer |
|---|---|
| J08 include voice? | Defer — optional smoke only |
| J10 real provider deeplinks? | Fix expense opt-in + pending UX first; sandbox smoke second |
| Atlas photo scan in J11? | Yes — manual-pick in scope |
