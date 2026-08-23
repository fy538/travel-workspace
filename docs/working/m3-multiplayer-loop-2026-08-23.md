---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the end-to-end M3 addressed-place multiplayer loop and its explicit release boundary.
supersedes: []
promotes_to: null
source_of_truth_for: [m3-multiplayer-loop]
---

# M3 addressed-place multiplayer loop

## Closure boundary

This receipt closes the first M3 engineering loop, not the entire long-term
multiplayer program. The loop is the smallest coherent product unit that
turns a place-bound personal observation into a shared human context and then
returns to separate personal meaning:

1. A sender addresses a source-bound place observation through an explicit pair
   authority (recipient, existing pair conversation, or pair Circle).
2. The recipient receives a private Chat card whose source identity is safe,
   whose actions are server-authorized, and whose revision is current.
3. `open_together` creates one shared overlap Occasion and accepts the
   recipient into it atomically.
4. Home/Places/Chat consume the viewer-relative graph projection and join the
   Occasion back to an existing Places reader only through the authorized
   typed `canonical_entity_ref`.
5. Each participant can record a distinct private encounter Outcome, retain
   source-object lineage, and correct that Outcome independently with a
   revision guard. Shared visibility requires an explicit Occasion context.

The opening does not create a Trip, booking, public post, or social Circle as
a side effect. A later explicit plan attachment is the only path to Trip
membership.

## Implementation receipts

### Backend

- UUID relationship handoffs are persisted with sender/recipient scope,
  source authorization, idempotency, immutable events, and a durable addressed
  message/card.
- The opening application command binds the handoff transition, Occasion
  creation, invitation acceptance, and handoff-to-Occasion identity in one
  transaction.
- Occasion invitation, decision, lifecycle, and outcome commands remain
  receipt-backed and revision-safe. Encounter outcomes are private by default;
  shared encounter outcomes require active Occasion membership.
- The public graph projection redacts graph-local UUIDs from mobile-facing
  identity joins and emits the reviewed canonical entity reference instead.
- A regression now asserts that a relationship opening leaves
  `occasion_plan_links` empty; place context never infers Trip membership.

Backend commits in this pass:

- `e086f352` — `test(m3): prove place openings stay outside Trips`

### Mobile

- `selectOccasionsForCanonicalEntity` joins graph context to the existing
  Places/venue/site reader contract without using graph UUIDs, slugs, or copy
  as identity.
- `routeForCanonicalEntityRef` delegates route validation to the existing
  exhaustive entity router and returns `null` for `custom`, transport hubs,
  and malformed catalog IDs.
- Encounter outcome actions now include an explicit correction mutation; the
  caller supplies the expected revision and idempotency key.
- Mock mode persists relationship-created Occasions and personal Outcomes,
  projects them by viewer, and reads back corrections. It no longer returns a
  successful transport response while leaving the graph empty.

Mobile commits in this pass:

- `e859da5d` — `feat(m3): expose canonical graph navigation and outcome correction`
- `18ee8cd9` — `test(m3): make mock multiplayer graph read back outcomes`
- `fef6aa38` — `feat(m3): mount sender place handoff action`
- `25ebf836` — `feat(m3): add private occasion outcome composer`
- `a81a9bc5` — `test(m3): certify two-account private outcome loop`

The sender action is intentionally narrow: it is shown on graph summaries with
a resolved world entity and a confirmed pair Circle, then sends through the
same addressed-handoff transport used by the recipient card. The recipient
surface can write a private note after a lived Occasion and can reopen that
note for revision-guarded correction. A canonical Place detail does not yet
carry the graph world UUID, so this is not a claim that every Place reader has
the sender doorway.

## Evidence

- Backend focused relationship/graph suite: **58 passed**.
- Backend relationship route suite with the controlled flag explicitly enabled:
  **14 passed**; the same suite includes the default-off route assertion.
- Mobile targeted mock, graph/action, and summary-card suites: **17 passed**.
- Mobile ESLint and TypeScript checks: **passed**.
- Maestro flow syntax: **passed**. The repository-wide governance validator
  remains blocked by 16 pre-existing `artifact-gallery` subflows that have no
  metadata headers; those files are unrelated to this M3 surface.
- The explicit two-account mock certification proves shared Occasion readback,
  recipient-only private Outcome visibility, correction revision advancement,
  and stale-replay rejection. It is automated evidence, not a device receipt.
- Parent commit `353106a` adds the local-only launcher
  `make m3-demo-backend`; no `.env`, dogfood, or production configuration was
  changed. The serving flag remains default-off everywhere else.

The Postgres acceptance test remains available but was not promoted to a cloud
environment in this pass. No production feature flag was enabled.

## Explicit release boundary

`RELATIONSHIP_UUID_HANDOFFS_ENABLED` remains the serving gate. The remaining
work is certification and expansion, not a hidden dependency in this loop:

- two-account device walk with real receipts and stale/replay/denial checks;
- complete the sender doorway on canonical Place detail once the graph UUID
  bridge is available;
- Occasion mute/read-attention policy and richer responsibility/task claims;
- explicit decision-policy semantics for constraints, vetoes, expertise, and
  delegation;
- an explicit Trip attachment adapter when a user chooses to promote a shared
  Occasion into a plan.

Until those are certified, this slice should be treated as an internal,
flagged capability with automated end-to-end evidence—not as a production
multiplayer launch. No M3-specific live device receipt was produced in this
pass: the existing physical runner covers J04/J10 and requires two real
dogfood identities, while this new UUID handoff surface has no dedicated
Maestro flow yet.
