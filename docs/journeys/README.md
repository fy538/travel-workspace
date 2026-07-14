# Canonical Journeys

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-28
> Source of truth for: the first production/dogfood journey set for Vesper

These one-pagers define the canonical journeys we should protect before expanding TestFlight and real dogfood: **J01–J12** are the lifecycle golden path; **J13–J19** extend coverage to the dimensions the golden path misses (failure, solo, destructive, account/data, cross-trip, distribution, social/search). They sit above the existing reliability traces: a journey describes the user-facing promise across screens; a trace proves specific contracts and invariants underneath it.

Use these when asking Codex, Claude Code, QA, or a human dogfooder to inspect the app. The goal is to catch the boring deterministic failures first: broken routes, stale read models, mock/real drift, no-op CTAs, privacy leaks, and fake-success states.

**Promotion board:** [STATUS.md](STATUS.md) · **AI interaction map:** [AI_INTERACTION_MAP.md](AI_INTERACTION_MAP.md) · **Archived static findings:** [STATIC_TRACE_PUNCH_LIST.md](../archive/2026-07/retired-live/STATIC_TRACE_PUNCH_LIST.md) · **Logic QA:** [travel-app/docs/logic-qa/README.md](../../travel-app/docs/logic-qa/README.md)

## Research Inputs

- [Interaction Surfaces Doctrine](../../travel-app/docs/design/interaction-surfaces-doctrine.md)
- [Offline First QA](../../travel-agent/docs/operations/Offline%20First%20QA.md)
- [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md)
- [Mock vs Real Parity](../../travel-app/docs/Mock%20vs%20Real%20Parity.md)
- [Domain Status](../../travel-app/docs/Domain%20Status.md)
- [Agent Chat Spec](../../travel-app/docs/page-specs/agent-chat.md)
- [Change Proposals Spec](../../travel-app/docs/page-specs/change-proposals.md)
- [Discover Spec](../../travel-app/docs/page-specs/discover.md)
- [Atlas Home Spec](../../travel-app/docs/page-specs/atlas-home.md)
- [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md)
- [Me/Account → Atlas trust investigation](../archive/2026-07/retired-live/me-account-atlas-trust-investigation-2026-06-25.md)
- [Cross-repo seam audit](../archive/2026-07/retired-live/cross-repo-seam-audit-2026-06-25.md)

## Journey Set

| # | Journey | Main risk protected |
|---|---|---|
| 01 | [Vague Idea To Vesper-Shaped Trip](01-vague-idea-to-vesper-shaped-trip.md) | Cold start, Trips Home phases, first-session onboarding handoff |
| 02 | [Concrete Trip Creation And Invite](02-concrete-trip-creation-and-invite.md) | Shared workspace and invite membership correctness |
| 03 | [Cold Trip Setup To Useful Workspace](03-cold-trip-setup-to-useful-workspace.md) | Trip Folio state machine, empty states, and setup slots |
| 04 | [Private Constraint To Group-Safe Plan](04-private-constraint-to-group-safe-plan.md) | Privacy contract across private, group, proposal, notification, and booking surfaces |
| 05 | [Group Planning To Proposal To Plan Mutation](05-group-planning-to-proposal-to-plan-mutation.md) | Advise → Propose → Act loop **and** direct Change Studio edits |
| 06 | [Itinerary, Map, Details, Chat, and Changes Coherence](06-home-plan-map-changes-coherence.md) | Read-model consistency after **any** trip mutation |
| 07 | [Discover To Contextual Vesper To Trip Action](07-discover-to-contextual-vesper-to-trip-action.md) | ConversationSeed, place context, and add-to-trip routing |
| 08 | [Live Trip What-Now Companion](08-live-trip-what-now-companion.md) | Active-trip usefulness, Vesper Home live mode, map/location context |
| 09 | [Notifications And Proactive Routing](09-notifications-and-proactive-routing.md) | Push/feed routing, cadence, read state, and privacy-safe copy |
| 10 | [Booking, Stay, And Expense Trust Loop](10-booking-stay-expense-trust-loop.md) | Provider/session drift, hold-settle contracts, opt-in expense sharing |
| 11 | [Atlas Candidate To Memory Control](11-atlas-candidate-to-memory-control.md) | Memory provenance, trust hub, and Atlas navigation |
| 12 | [Returned Trip To Story, Memory, And Settle-Up](12-returned-trip-to-story-memory-settle-up.md) | Post-trip loop, durable memory, story, and settlement |

### Holistic-coverage extension (J13–J19)

J01–J12 are the lifecycle golden path. These cover the *dimensions* the golden path doesn't: failure, the non-group user, destructive mutations, account/data rights, the repeat-user loop, distribution, and breadth surfaces. See [STATUS.md](STATUS.md) for which are certified vs visible-skip (each has a real blocker noted in its doc's First Automation Target).

| # | Journey | Main risk protected |
|---|---|---|
| 13 | [Failure And Recovery](13-failure-and-recovery.md) | Unhappy path — honest errors + recovery, never fake success |
| 14 | [Solo Trip End-to-End](14-solo-trip-end-to-end.md) | Single-member trip never drops into group chrome/routing |
| 15 | [Destructive And Reversible Actions](15-destructive-and-reversible-actions.md) | Leave/remove/delete/cancel cascade correctly; undo restores |
| 16 | [Account And Data Lifecycle](16-account-and-data-lifecycle.md) | Privacy controls take effect; deletion purges private data |
| 17 | [Returning Traveler (Cross-Trip Recall)](17-returning-traveler-cross-trip.md) | Second trip recalls taste without leaking another trip's context |
| 18 | [Signed-Out Join-By-Invite](18-signed-out-join-by-invite.md) | Invite token survives the auth detour → correct membership |
| 19 | [Social Loop And Cross-Entity Discovery](19-social-loop-and-discovery.md) | Search/profiles route live; public taste leaks no private data |

### Phase 0 (cross-journey, not numbered)

Auth and first-session onboarding are **not** a standalone journey yet. They are embedded checks that every cold-start trace must cover:

- Clerk sign-in / sign-up and invite auth detour return (see Journey 02)
- `onboarding` + `onboarding-safety` screens
- Planning-intent bootstrap and push permission at first trip-chat send
- First land on Trips Home or Vesper Home after auth

When TestFlight starts cold for every tester, consider promoting Phase 0 to a numbered journey. Until then, **Journey 01** owns the first-session path; **Journey 02** owns auth detours.

## Journey Boundaries (avoid double-tracing)

| Boundary | Journey A ends / owns | Journey B starts / owns |
|---|---|---|
| Ideation vs draft trip | **01** — no committed trip, home conversation, promotion | **03** — `trip_id` exists, blank/draft facets to fill |
| Proposal workflow vs read-model truth | **05** — create, vote, apply, revert, direct edit | **06** — do Home/Plan/Map/Changes agree after the mutation? |
| Live UX vs projection invariants | **08** — "what now?", permissions, urgent CTAs | **06** — same block ids across surfaces |
| Atlas control vs post-trip narrative | **11** — provenance, dispute, trust hub | **12** — story compose, settlement, returned-phase Folio |
| Privacy leak vs notification routing | **04** — private text must not appear in group surfaces | **09** — tap opens the right private vs group destination |

## Deferred Surfaces (intentionally outside the 12)

Do **not** add numbered journeys for these until they enter dogfood scope. Track them here instead.

| Surface | Why deferred | Where to smoke-check today |
|---|---|---|
| Voice / on-location guide / narration | Experimental; Domain Status marks unstable contract | Optional steps in Journey 07 (guide cards), Journey 08 (narration strip) |
| Cross-trip explanation card | Deferred from V1; backend/client substrate exists | [Decision](../decisions/2026-07-10-defer-cross-trip-explanation-card.md) |
| Social graph (follow, profiles, story share) | Secondary to group-trip wedge | Journey 07 friend cards; Journey 09 social notification routing |
| Content graph search quality | Eval/canary domain, not a UX journey | Seeded-city live canary under Journey 07 |
| Maestro / screenshot visual QA | Owned by separate agent loop | Complements static trace; does not replace it |

## Cross-Cutting Checks For Every Journey

- Auth detours must return to the intended destination.
- 401/403 states must be explained, not silent.
- Offline or slow-network states must not produce fake success.
- Every visible CTA must either work or clearly render as disabled.
- Mock data must not hide a real-backend contract requirement.
- Private facts must not leak into group, notification, booking, or share surfaces.
- The app must never strand the user after accept, confirm, share, or dismiss actions.
- Route params (`tripId`, `conversationId`) must win over `currentTrip` when both exist.

## How To Use These With AI Agents

**Layer 1 — static trace** (default; no live LLM):

```text
Read docs/journeys/<journey>.md and trace the journey through Travel App and Travel Agent.
Default verdict: REFUTE (broken until proven).
For each Canonical Step report: route, component, hook, API method, BE endpoint, mock behavior, invariant, risk, evidence (file:line).
Check every "Must Never Happen" bullet.
Do not call live LLM-backed endpoints.
Output: findings table + top 3 missing deterministic tests.
```

**Layer 2 — mock walk** (Jest smoke / scripted navigation, not Maestro):

```text
Walk docs/journeys/<journey>.md in mock mode.
Report broken navigation, no-op CTAs, empty states that should not be empty, stale UI after mutations, and mismatches against Expected Outcome.
```

**Layer 3 — backend canary** (Postgres, no LLM where possible):

```text
Run or extend the journey's real-backend checklist / dogfood canary tests.
Report pass/fail with fixture ids.
```

## Certification ladder

Certification is cumulative; a higher layer never substitutes for a lower one:

1. Registry and static-contract checks prove the journey is named and traceable.
2. Mock walks prove navigation, surface states, and deterministic client behavior.
3. Backend scenario tests prove persistence, privacy, idempotency, and reversal.
4. Live API checks prove deployed transport and environment wiring.
5. On-device walks prove the real auth, pixels, and multi-device interaction.

Verdicts are `pass`, `fail`, or `blocked` with named evidence. “Implemented” is not
a certification result. `STATUS.md` is the promotion board; individual run logs are
dated evidence and belong in the archive when superseded.

**Layer 4 — live dogfood** (Maestro, device, real providers):

Only after Layers 1–3 are green or risks are explicitly de-afforded.

**Orthogonal slice tracers** (run on PRs touching API seams, not instead of journeys):

- [Cross-repo seam audit](../archive/2026-07/retired-live/cross-repo-seam-audit-2026-06-25.md) — `openapi.json` → `http.ts` → mock shape drift
- Backend scenario tests — lifecycle transitions, idempotency, and orphan detection
- [Privacy invariant trace](../archive/2026-07/retired-live/privacy-trace-run-latest.md) — private egress boundaries
- [Mock-real parity auditor](../reliability/prompts/mock-real-parity-auditor.md)

Only after static and mock layers pass should a journey become a live dogfood canary.
