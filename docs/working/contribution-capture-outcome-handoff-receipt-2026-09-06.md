---
doc_type: working
status: active
owner: founder / Contribution and Capture
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Records the source-owner Outcome → Life handoff package and its remaining receiving-lane and policy gates.
supersedes: []
depends_on:
  - contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - complete-system-integration-roadmap-2026-09-05.md
  - ../systems/contribution-and-consequence.md
---

# Contribution/Capture → Life Outcome Handoff Receipt

**Date:** 2026-09-06  
**Owner lane:** Contribution and Capture  
**Backend commit:** `37c3f93bf` (`feat(life): emit Outcome owner handoffs`)

## Delivered

The existing Experience Graph Outcome commands now emit the already-adopted,
content-free Life owner envelope in the same transaction as the canonical
Outcome mutation:

- Commitment Outcome record and correction use the current Commitment
  participant rows as the shared audience.
- Encounter Outcome record and correction use active Occasion members only
  when the Outcome is explicitly shared inside an Occasion.
- Private Outcomes remain owner-only and do not read membership as a grant.
- Corrections carry the prior audience as `before_viewer_ids`, so a viewer who
  loses access still receives a withdrawal-capable refresh.
- Owner revision and `outcome:<id>:<change>:<revision>` event identity are
  stable across retry; registration goes through the shared Life outbox and
  never writes Life projection rows from the source owner.
- The event payload remains identifier/revision metadata only; Outcome meaning,
  source object ids, and other source content do not cross the handoff.

The pure audience contract and envelope builder remain separate from the
transactional adapter in
`travel-agent/backend/domains/experience_graph/outcome_life_events.py` and
`outcome_life_propagation.py`.

## Evidence

- `tests/domains/experience_graph/test_outcome_life_events.py`
- `tests/domains/experience_graph/test_outcome_life_contract.py`
- `tests/domains/experience_graph/test_outcome_life_producers.py`
- `tests/domains/experience_graph/test_outcome_life_producers_postgres.py`
- `tests/core/test_experience_graph_commands.py`

Focused result: **48 passed**, including **2 PostgreSQL transaction tests**.
The Postgres cases prove shared Encounter before/after fan-out and prove that a
shared Commitment Outcome does not widen to an unrelated Occasion member.
Ruff, formatting, compile, and `git diff --check` passed for the package.

The connected regression portfolio subsequently passed **139 offline tests**
and **7 PostgreSQL tests** across Capture, Graph, Life broadcast/propagation,
retention, memory-writer conformance, and owner contracts. A repository-wide
offline collection was attempted but remains environment-blocked by the
checkout's pre-existing missing optional packages (`openai`, `json_repair`,
`shapely`, and `redis`); no failure was attributed to this package.

## Boundaries preserved

- Life still owns its projector, index, readback, and correction application;
  this package only emits source-owner metadata.
- No Chat redesign, conversation-history policy, retained-intention owner,
  social command, expense owner, or synthetic Plan was introduced.
- No new API/schema migration was required.
- The envelope supports withdrawal, but no new product-level Outcome delete or
  erasure command was invented. Account-erasure fan-out remains a separate
  owner-policy package.

## Remaining action register

1. **Life receiving rehearsal:** run the event through the canonical Life
   projector and verify owner readback, correction, stale replay, and
   withdrawal for both Outcome families. Do not mark serving/index cutover
   complete from this source-side receipt.
2. **Account-erasure policy:** decide and implement the existing owner’s
   explicit fan-out for Outcomes whose owner or audience is erased; preserve
   the same before/after audience semantics.
3. **CC-2:** ordinary Chat versus Ask-image history/expiry semantics remain
   proposal-gated; do not enable them from this receipt.
4. **CC-3/CC-4/CC-6:** remaining writer-family receipts, full useful-first
   journeys, and real transport/native/generated-content evidence remain
   separately gated as recorded in the contribution and integration roadmaps.
