# Journey Status Matrix

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-28 (Logic QA MVP: J01-J12 green)
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

## Matrix

| # | Journey | Static trace | Mock walk | Deterministic tests | Real backend | Known blockers / risks | Next action | Dogfood ready |
|---|---|---|---|---|---|---|---|---|
| 01 | [Vague Idea](01-vague-idea-to-vesper-shaped-trip.md) | ready | ready | ready | ready | Logic QA MVP green: blank draft dedupe, private planning-intent bootstrap, explicit promotion into the existing draft slot, trip/conversation linkage, Trips list visibility, and no fabricated itinerary. | Live promotion canary and frontend onboarding controls. | no |
| 02 | [Create + Invite](02-concrete-trip-creation-and-invite.md) | ready | ready | ready | ready | Logic QA MVP green: invite accept creates membership, consumes once, same-user retry is OK, stranger reuse rejected. | Optional live invite-accept canary. | no |
| 03 | [Cold Setup](03-cold-trip-setup-to-useful-workspace.md) | ready | ready | ready | ready | Logic QA MVP green: blank ideation trips render honestly, organizer PATCH hydrates Trip/Plan/Folio immediately, cold→pre Folio mode is coherent, and non-organizer setup mutation is rejected. | Live setup-slot/navigation prefill walk. | no |
| 04 | [Private → Group-Safe](04-private-constraint-to-group-safe-plan.md) | ready | ready | ready | ready | Logic QA MVP green: private phrase redacted from group-visible proposal copy and privacy event audited. | Live dogfood leak walk. | no |
| 05 | [Proposal → Plan](05-group-planning-to-proposal-to-plan-mutation.md) | ready | ready | ready | ready | Logic QA MVP green: accept/apply/revert, reject preservation, and vote retry idempotency. | CI gate canary; live revert walk. | no |
| 06 | [Coherence](06-home-plan-map-changes-coherence.md) | ready | ready | ready | ready | Logic QA MVP green: Plan, Map, Home, Folio, and Changes agree on block ids before/after proposal apply; unplaced map items remain visible; unrelated dismissals do not hide open decisions. | Live cross-surface canary (optional). | no |
| 07 | [Discover → Vesper](07-discover-to-contextual-vesper-to-trip-action.md) | ready | ready | ready | ready | Logic QA MVP green: Discover venue context grounds Vesper seed copy, private saves persist without trip leakage, trip-aware venue commits mutate idempotently, and non-members are rejected. | Live discover canary. | no |
| 08 | [Live Companion](08-live-trip-what-now-companion.md) | ready | ready | ready | ready | Logic QA MVP green: live trip phase, current-day plan state, map stop parity, Folio live spine, and Vesper seed context agree on active/next blocks. | Device GPS heartbeat and live "what now" canary. | no |
| 09 | [Notifications](09-notifications-and-proactive-routing.md) | ready | ready | ready | ready | Logic QA MVP green: proactive feed payloads preserve private/group target audience, read state persists, ownership is enforced, cadence preferences persist, and quiet hours suppress push while preserving in-app. | Live device/push provider canary. | no |
| 10 | [Booking / Stay / Expense](10-booking-stay-expense-trust-loop.md) | ready | ready | ready | ready | Logic QA MVP green: stay privacy, organizer-controlled shared stays, explicit expense opt-in, booking approval boundaries, wrong-trip/expired-hold handling, and no fabricated expense on local cart confirmation. | Real provider sandbox smoke; pending UX remains a visual/device gate. | no |
| 11 | [Atlas Memory](11-atlas-candidate-to-memory-control.md) | ready | ready | ready | ready | Logic QA MVP green: candidate submission/review/approval, artifact reflection/provenance, timeline/almanac projection, hide/restore control, artifact signal-state control, and ownership isolation. | Real photo-library scan, staging checklist, profile TOC polish. | no |
| 12 | [Post-Trip](12-returned-trip-to-story-memory-settle-up.md) | ready | ready | ready | ready | Logic QA MVP green: cached story, settlement transfer, memory highlight, story/settle home cards. | Live closeout canary; story generation remains async/eval territory. | no |

## Summary (2026-06-26 trace)

| Metric | Count |
|---|---|
| Static trace ready | 12 / 12 |
| Mock walk ready | 12 / 12 (all committed + green, 2026-06-27) |
| Logic QA MVP green | 12 / 12 (`J01`-`J12`) |
| Blocked on mock walk | 0 (P0s fixed 2026-06-26) |
| Dogfood ready | **0 / 12** (mock walks + backend slices done; still gated on visual QA and live dogfood) |

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

**Remaining P1:** None — static-trace blockers addressed. Mock walks done (12/12 committed + green, 2026-06-27). Logic QA MVP is green for all 12 journeys. Next: run visual screenshot certification and live dogfood gates.

## Promotion Rules

Unchanged — see [README.md](README.md). None of the 12 meet all gates.

## Open Questions (resolved for this pass)

| Question | Answer |
|---|---|
| J08 include voice? | Defer — optional smoke only |
| J10 real provider deeplinks? | Fix expense opt-in + pending UX first; sandbox smoke second |
| Atlas photo scan in J11? | Yes — manual-pick in scope |
