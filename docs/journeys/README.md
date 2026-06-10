# Canonical Journeys

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Source of truth for: the first production/dogfood journey set for Vesper

These one-pagers define the first 12 canonical journeys we should protect before expanding TestFlight and real dogfood. They sit above the existing reliability traces: a journey describes the user-facing promise across screens; a trace proves specific contracts and invariants underneath it.

Use these when asking Codex, Claude Code, QA, or a human dogfooder to inspect the app. The goal is to catch the boring deterministic failures first: broken routes, stale read models, mock/real drift, no-op CTAs, privacy leaks, and fake-success states.

## Research Inputs

- [Golden Paths](../reliability/Golden%20Paths.md)
- [Offline First QA](../../travel-agent/docs/operations/Offline%20First%20QA.md)
- [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md)
- [Mock vs Real Parity](../../travel-app/docs/Mock%20vs%20Real%20Parity.md)
- [Domain Status](../../travel-app/docs/Domain%20Status.md)
- [Agent Chat Spec](../../travel-app/docs/page-specs/agent-chat.md)
- [Change Proposals Spec](../../travel-app/docs/page-specs/change-proposals.md)
- [Discover Spec](../../travel-app/docs/page-specs/discover.md)
- [Atlas Home Spec](../../travel-app/docs/page-specs/atlas-home.md)
- [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md)

## Journey Set

| # | Journey | Main risk protected |
|---|---|---|
| 01 | [Vague Idea To Vesper-Shaped Trip](01-vague-idea-to-vesper-shaped-trip.md) | Cold start creates useful momentum without fake certainty |
| 02 | [Concrete Trip Creation And Invite](02-concrete-trip-creation-and-invite.md) | Shared workspace and invite membership correctness |
| 03 | [Cold Trip Setup To Useful Workspace](03-cold-trip-setup-to-useful-workspace.md) | Trip Folio state machine, empty states, and setup slots |
| 04 | [Private Constraint To Group-Safe Plan](04-private-constraint-to-group-safe-plan.md) | Privacy contract across private, group, proposal, notification, and booking surfaces |
| 05 | [Group Planning To Proposal To Plan Mutation](05-group-planning-to-proposal-to-plan-mutation.md) | Advise -> Propose -> Act loop |
| 06 | [Home, Plan, Map, Changes Coherence](06-home-plan-map-changes-coherence.md) | Read-model consistency after trip changes |
| 07 | [Discover To Contextual Vesper To Trip Action](07-discover-to-contextual-vesper-to-trip-action.md) | ConversationSeed, place context, and add-to-trip routing |
| 08 | [Live Trip What-Now Companion](08-live-trip-what-now-companion.md) | Active-trip usefulness, map/location context, and urgent cards |
| 09 | [Notifications And Proactive Routing](09-notifications-and-proactive-routing.md) | Push/feed routing, cadence, read state, and privacy-safe copy |
| 10 | [Booking, Stay, And Expense Trust Loop](10-booking-stay-expense-trust-loop.md) | Provider/session drift, confirmation visibility, and opt-in expense sharing |
| 11 | [Atlas Candidate To Memory Control](11-atlas-candidate-to-memory-control.md) | Memory provenance, user control, and Atlas navigation |
| 12 | [Returned Trip To Story, Memory, And Settle-Up](12-returned-trip-to-story-memory-settle-up.md) | Post-trip loop, durable memory, story, and settlement |

## Cross-Cutting Checks For Every Journey

- Auth detours must return to the intended destination.
- 401/403 states must be explained, not silent.
- Offline or slow-network states must not produce fake success.
- Every visible CTA must either work or clearly render as disabled.
- Mock data must not hide a real-backend contract requirement.
- Private facts must not leak into group, notification, booking, or share surfaces.
- The app must never strand the user after accept, confirm, share, or dismiss actions.

## How To Use These With AI Agents

Start with a static trace before spending live product tokens:

```text
Read docs/journeys/<journey>.md and trace the journey through Travel App and Travel Agent. Report route wiring, components, hooks, API calls, mock behavior, backend endpoints, missing tests, and likely real-backend drift. Do not call live LLM-backed endpoints.
```

Then promote to mock-mode UI driving:

```text
Launch Travel App in mock mode and walk docs/journeys/<journey>.md. Report broken navigation, no-op CTAs, empty states that should not be empty, stale UI after mutations, and any mismatch against the Expected Outcome section.
```

Only after those pass should a journey become a live dogfood canary.

