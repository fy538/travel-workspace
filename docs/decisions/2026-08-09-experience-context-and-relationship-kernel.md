---
title: Experience, context, and relationship kernel
status: accepted
owner: founder / engineering
created: 2026-08-09
decided: 2026-08-09
last_reviewed: 2026-08-09
doc_type: decision
why_new: Establish shared ownership and migration boundaries before expanding Plans, multiplayer, relationship memory, and proactive projections.
supersedes: []
source_of_truth_for: [experience-context-relationship-kernel]
---

# Experience, context, and relationship kernel

Status: accepted for implementation

Date: 2026-08-09

## Decision

The product will generalize around a small set of contracts rather than by
introducing one universal Plan table, memory table, event store, or agent.

The existing domains remain authoritative:

| Concern | Authoritative owner | Responsibility |
| --- | --- | --- |
| Experience identity | `ExperienceScope` | Identifies ambient work, a local Plan, or a Trip without creating a product object. |
| Pre-commit intent | `conversation.intent_state` | Conversation-scoped sketch that may be promoted. |
| Committed planning | Trip aggregate and itinerary operation ledger | Canonical Plan/Trip state, commitments, attendance, and mutations. |
| Confirmed relationships | Social-circle membership | Consent, membership lifecycle, and relationship scope. |
| What happened | Per-person occurrence and outcome feedback | Evidence about participation, place fit, and companion fit. |
| Evidence selection | Context Compiler | Purpose-, audience-, privacy-, and revision-bound context. |
| Current relevance | Situation compiler | Surface-neutral snapshot of what matters now. |
| Delivery | Domain transactional outboxes | Durable, retryable propagation to projections. |

`TripWorldModel` and prompt-specific spatial situation remain compatibility
adapters while their consumers migrate to the Context Compiler and Situation
boundary. They are not new sources of truth.

## Shared contracts

The next additive kernel consists of:

1. `ExperienceScope`, already present, attached to AI runs, context requests,
   situations, attention candidates, and action receipts.
2. `RelationshipScope`, a content-free reference to no relationship, a
   confirmed social circle, or the current Trip roster.
3. A typed Situation envelope containing experience scope, relationship scope,
   current place/time/world facts, attention state, and one specialized
   payload (`TripSituation`, `LocalSituation`, or `AmbientSituation`).
4. A common projection envelope containing event identity, domain and aggregate
   identity, source revision or sequence, actor, audience/privacy class,
   provenance, and schema version.

These contracts are adapters around existing storage. They do not authorize
direct AI writes to read models or projections.

## Relationship and memory rules

An active relationship is mutually confirmed. New circle members therefore
enter as `invited` until they accept. Existing rows that were already exposed
as active are backfilled as confirmed; the migration must not silently revoke
existing access.

Relationship memory is not copied from a Trip or inferred from membership. It
is promoted only from explicit member-authored shared statements or confirmed
per-person outcomes. `relationship_memory_claims` is the source of truth; a
bounded group-safe memory version is only a projection. Claims carry source
references, scope, visibility, confidence, and correction state. The first
outcome adapter writes private personal claims atomically with the outcome;
sharing one into a confirmed circle is a separate, explicit consent action.

## Propagation rules

Domain outboxes stay domain-specific because their payloads and ordering
semantics differ. Lease, retry, fencing, and acknowledgement mechanics may be
shared internally after the current hardening is stable. Delivery is
at-least-once; consumers must be idempotent. In-process events are optional
local consequences and never the sole durable path.

Behavioral `user_events` remains an interaction/telemetry log. New durable
domain truth must use its owning table and outbox. Social activity is a
consent-filtered projection, not an arbitrary view over every behavioral
event.

## Execution order

1. Certify existing outbox leasing and two-device synchronization.
2. Add the shared contracts and ownership telemetry without behavior changes.
3. Correct social-circle invitation, acceptance, pair identity, and lifecycle.
4. Expose companion-fit outcome capture and emit authoritative outcome events.
5. Add the governed relationship-memory claim ledger and projection. **Done:**
   private outcome claims are append-and-supersede, Context Compiler reads the
   active private projection, and circle sharing requires a confirmed-member
   action with an auditable circle event.
6. Migrate context consumers and retire redundant read paths incrementally.
7. Prove one end-to-end pair Plan → occurrence → outcome → memory → proactive
   recommendation slice before expanding multiplayer behavior.

Every phase uses expand → backfill → shadow → compare → cut over → contract.
No legacy path is deleted until parity, privacy, latency, replay, and rollback
checks pass in production-like tests.

## Non-goals

- Replacing Trips with a universal Plan schema now.
- Creating a universal event or memory table.
- Treating social membership as attendance or outcome evidence.
- Making private behavioral telemetry socially visible by default.
- Adding a new cache until source revisions and invalidation are explicit.
