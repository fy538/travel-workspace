---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Define branch-level journey ownership and evidence so one happy-path file cannot certify an overloaded customer journey.
---

# Branch-Level Journey Certification Model

## Decision

Vesper protects customer behavior at three levels:

1. **Customer journey (`JNN`)** — one motivation, meaningful state transition,
   outcome, and return point that a traveler would recognize.
2. **Required branch (`JNN.BNN`)** — a materially different authority,
   lifecycle, failure, privacy, or recovery path inside that journey.
3. **Evidence (`FE`, `BE`, `VIS`, `LIVE`)** — proof attached to a branch, not
   inferred from the existence of one file for the parent journey.

The existing J01–J19 identifiers stayed stable during the coverage refresh.
After the ownership inventory and ID collision audit completed on 2026-07-18,
the approved customer outcomes were allocated J20–J28.

## What qualifies as a customer journey

A numbered journey must have all of the following:

- a user motivation stated without naming a screen;
- a starting state a fixture or dogfood persona can reproduce;
- at least one meaningful decision or persisted transition;
- an outcome visible to the traveler;
- a stable place to return or continue;
- a distinct trust or product promise not already owned elsewhere.

A route, component, empty state, persona, or API mutation is not automatically
a journey.

## What belongs in a branch

Create a required branch when the path changes because of at least one of:

- **Authority:** organizer, member, owner, payer, initiator, or public viewer.
- **Lifecycle:** empty, planning, held, confirmed, live, returned, archived.
- **Cardinality:** solo, group, leave, rejoin, or organizer handoff.
- **Trust:** private versus shared, provider versus app responsibility, or
  memory provenance.
- **Recovery:** offline, stale, expired, denied, retry, partial failure, or
  idempotent replay.
- **Return:** the action must reconcile on another surface or after reopening.

Cosmetic layouts and equivalent content variants stay in component or visual
regression tests rather than becoming branches.

## Required evidence

| Code | Evidence | Proves |
|---|---|---|
| `FE` | Frontend contract/mock walk | Route, copy, controls, local convergence, mock honesty |
| `BE` | Backend scenario | Persistence, authorization, privacy, idempotency, cascade |
| `VIS` | Native device/simulator walk | Interaction hierarchy, pixels, confirmation, return path |
| `LIVE` | Seeded persona or deployed walk | Real auth, transport, multi-account behavior, provider/LLM seams |

Evidence requirements are declared per branch. `BE` is legitimately `n/a` for
a presentation-only return branch; `VIS` is not `n/a` for a user-visible trust
decision; `LIVE` may be `dark` only when the product capability itself is
explicitly rollout-gated.

## Branch manifest

The eventual machine-readable registry should use this shape:

```yaml
branches:
  - id: J10.B03
    title: Booking initiator releases an unpaid provider hold
    requirement: required # required | optional | deferred
    starting_state: held_for_payment
    actor: booking_initiator
    trigger: release_hold
    outcome: hold_released_without_booking_cancellation_claim
    return_point: booking_session
    invariants:
      - no payment is submitted
      - provider reservation cancellation is not implied
      - retry is idempotent
    surfaces:
      - /booking/[sessionId]
    evidence:
      FE: required
      BE: required
      VIS: required
      LIVE: optional
```

The first implementation may keep branches in each journey document. Move them
into `journeys.yaml` only after the audit proves the schema on J06, J10, and J11.

## Status calculation

Binary file presence is not certification.

- A fidelity cell displays a fraction such as `4/6` required branches proven.
- `✅` means every required branch for that fidelity has passing evidence.
- `◐` means at least one but not all required branches pass.
- `—` means no evidence is required or registered, with a recorded reason.
- `⤵️ dark` means the product branch is intentionally unavailable.
- `🔴` means a required branch failed.

Parent status is the minimum status of its required branches. Optional branches
never turn a journey green; deferred branches remain visible debt.

## Promotion gates

| Gate | Requirement |
|---|---|
| `defined` | Journey contract and required branch manifest exist |
| `traced` | Every required branch has route, handler, API, invariant, and fixture ownership |
| `local-certified` | Required `FE`, `BE`, and `VIS` evidence passes |
| `lived-certified` | Required `LIVE` branches pass against the intended environment |
| `dark` | Capability is deliberately unavailable and de-afforded in product |

No higher gate substitutes for a lower one. A live happy path cannot erase a
missing authorization test, and a backend test cannot certify clipped or
misleading confirmation UI.

## Cross-cutting assurance packs

Some current numbered entries describe dimensions rather than a single customer
motivation. During migration they remain stable but are labeled assurance packs:

- J06 — cross-surface read-model coherence;
- J13 — failure and recovery;
- J14 — solo/cardinality behavior;
- J15 — destructive/reversible trust boundaries.

Their branches should be referenced by the customer journeys they protect. The
refresh will decide whether each remains numbered, becomes a generated assurance
view, or narrows to one customer outcome. No ID is retired without preserving
historical evidence links.

## Identifier safety

Global `JNN` IDs belong only to `docs/journeys/journeys.yaml`. Subsystem docs use
namespaced IDs such as `J-A1`; branches use `JNN.BNN`; test-only scenarios use a
descriptive prefix rather than inventing the next global journey number.

An adjacent backend checkout previously used test labels J22–J27 for archive,
membership epochs, cardinality transitions, organizer handoff, active authority,
and group agency. On 2026-07-18 those files and test names were changed to
descriptive scenario names and retained as evidence for J14/J15 and the proposed
governance journey. Global J20+ allocation is now unambiguous.

## Migration sequence

1. Inventory current routes, domains, promises, and evidence against J01–J19. **Complete.**
2. Write branch manifests for overloaded J06, J10, and J11. **Complete.**
3. Classify J06/J13/J14/J15 as customer journeys or assurance packs. **Complete.**
4. Resolve unregistered J22–J27 backend labels. **Complete 2026-07-18.**
5. Approve the true ownership gaps and allocate new IDs. **Complete: J20–J28.**
6. Teach the registry guard and status generator to calculate branch coverage. **Trial complete for J06/J10/J11.**
7. Migrate evidence incrementally; do not manufacture green cells during the transition.
