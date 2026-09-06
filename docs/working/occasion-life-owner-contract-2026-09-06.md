---
doc_type: working
status: active
owner: Integration / Life lanes
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
source_of_truth_for:
  - Occasion-to-Life owner event contract
  - Occasion audience revision and viewer fan-out
why_new: "The next Life owner candidate needs an explicit audience revision before any producer is wired."
---

# Occasion → Life owner contract — 2026-09-06

## Decision boundary

Occasion is the next eligible Life owner candidate, but it is not yet an
incremental producer. The canonical owner is the pair
`experience_graph.occasions` + `experience_graph.occasion_members`; neither Life
nor a UI surface may infer membership from a card, invitation, or cached graph
projection.

The owner event must represent both content revision and audience revision.
`occasions.revision` alone is insufficient: accepting an invitation, leaving,
or transferring the organizer can change viewer eligibility without changing
the Occasion row's revision.

## Event identity

Every mutation that can change an Occasion's Life representation emits one
durable `life_projection_outbox` event inside the same owner transaction:

| Field | Contract |
| --- | --- |
| `owner_kind` | `occasion` |
| `owner_id` | Occasion UUID |
| `owner_revision` | Opaque digest of the current Occasion row revision plus the ordered active-member tuple `(user_id, member.revision, role, visibility)` |
| `change_kind` | `occasion_created`, `occasion_membership_changed`, `occasion_lifecycle_changed`, or `occasion_deleted` |
| `policy_revision` | Explicit audience-policy version, initially `life.v1` |
| `payload.viewer_ids` | Union of viewers before and after the mutation; this includes a viewer who just left so their row can be withdrawn |
| `affected_refs` | Identifier/revision-only Occasion and member refs; never invitation text or private notes |

The digest is recomputed from the canonical owner rows after the mutation. It
is not a timestamp guessed by the producer and is not the member revision of a
single actor. Retries reuse the same event key and digest.

## Required producer coverage

The producer is not complete until every path below either emits the event or
proves that it cannot change the Life representation:

1. `create_occasion_tx` — create the organizer-only initial row.
2. `respond_to_occasion_invitation` — emit after acceptance; declined/deferred
   responses do not alter the member audience and need no Life event.
3. `leave_occasion` — emit before/after viewer union; organizer closure is one
   event, not two independent writes.
4. `transfer_occasion_organizer` — emit because role and audience metadata are
   part of the owner projection.
5. `transition_occasion_lifecycle` — emit after each accepted lifecycle change.
6. Any account-deletion or administrative reassignment path — emit or provide
   a transactionally equivalent withdrawal event.

Invitation creation alone is not an Occasion audience change. Decision votes,
plan links, and ordinary invitation metadata remain outside this producer until
they alter the Life record or its audience.

## Current-authority reader

The projector must use a narrow reader, not the full graph projection:

`read_occasion_owner(viewer_id, occasion_id, represented_at)`

It must lock or consistently read the Occasion row and active membership rows,
reject a viewer without an active membership, return the current owner and
audience digest, and return `None` after deletion/closure policy withdraws the
record. It must not trust title, member IDs, or audience data carried in the
event payload.

## Life shadow projection

The initial projector writes only the existing `life.v1` shadow index:

- `record_id = occasion.{occasion_id}`;
- `owner_kind = occasion` and `owner_id = occasion_id`;
- `owner_revision = audience digest`;
- private audience for an organizer-only Occasion, group audience only when
  active participant membership proves it;
- `TIME` lens always; `PEOPLE` only when multiple active participants are
  represented; Places requires an independently authorized world-entity ref;
- withdrawal on missing membership, deletion, or stale audience digest;
- explicit restore only after the current reader proves the viewer is active and
  the existing row is withdrawn at the exact digest.

No Occasion event may switch Life serving, create a second Occasion owner, or
publish invitation/message content into the cross-root event bus.

## Acceptance evidence before implementation

- Pure digest tests prove deterministic ordering, membership removal, role
  transfer, and unchanged-row stability.
- Producer tests cover every mutation path and assert the before/after viewer
  union.
- PostgreSQL tests prove owner mutation and Life outbox insertion commit or
  roll back together, while the existing action receipt remains independent.
- Projector tests prove stale audience events cannot reauthorize a departed
  viewer, and explicit restore cannot insert a row without a withdrawal
  tombstone.
- The owner matrix may change Occasion from `SHADOW_ONLY` only after these
  tests, current-authority reads, and shadow comparison pass. Indexed serving
  remains gated.

## Not yet decided

- Whether a closed Occasion remains in Life indefinitely or follows the
  existing retention/expiry policy.
- Whether member role changes affect the People lens or only audience grants.
- Whether an Occasion with no active members is withdrawn immediately or kept
  as a private organizer record until explicit deletion.

Until those choices are adopted, do not wire a generic Occasion producer or
reuse the retained-source envelope. The next implementation package should
start with the digest/read-model helpers and pure contract tests.
