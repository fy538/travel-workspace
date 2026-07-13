---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the completed IR-05 policy shadow baseline and ownership remediation.
supersedes: [itinerary-redesign-ir05-shadow-adapter-progress-2026-07-13.md]
source_of_truth_for: [itinerary-redesign-ir05-shadow-baseline]
---

# Itinerary redesign IR-05 shadow baseline

Date: 2026-07-13
Status: IR-05 complete; capability payload/read flip remains owned by IR-12

## Ownership remediation

The accepted V1 governance contract has one explicit shared-itinerary decision
owner. Migration `ir05a001` adds that owner and its provenance to trips, plus
block-owner provenance and `needs_owner_review`.

Compatibility defaults are deterministic:

- a solo trip uses its sole member;
- when the trip creator is a current organizer, that organizer is the shared
  owner even if other administrative roles exist;
- otherwise, exactly one current organizer may become the shared owner;
- zero organizers, or multiple organizers without the creator among them,
  remain unresolved;
- whole-group blocks use the shared owner;
- a personal block uses its sole legacy participant;
- a subgroup uses the shared owner temporarily and sets
  `needs_owner_review=true` until explicitly reassigned.

These are compatibility defaults with queryable provenance. Participant
attendance never independently grants authority.

## Block and day adapter

The DB adapter loads and fails closed on normalized membership, governance,
scope, owner, affected people, revision, privacy, protected dependency, and
provider-controller evidence. It resolves:

- block inspect, Add relative, Move, Replace, Remove, own attendance,
  occurrence, and booking change;
- day inspect, Add, Reorder, Optimize, and Replan using the explicit shared
  owner and day revision.

Plan State runs these only under the default-off `ITINERARY_POLICY_V2` shadow
gate. It does not add fields to or otherwise alter the returned payload.

## Target fixtures

All 12 frontend target fixture IDs have corresponding executable backend policy
evidence, covering undated solo, booked solo, Open and Review whole-group,
personal/subgroup ownership, parallel structure, provider continuation, stale
revision, live disruption, completed/cancelled, and departed-member privacy.

## Migrated corpus baseline

The current local itinerary corpus was copied without human text or booking
payloads into a disposable PostgreSQL database. The database was upgraded
through `ir05a001`, backfilled, resolved through the real DB adapter, and then
removed. The shared database was not mutated.

| Measure | Count |
|---|---:|
| Trips | 169 |
| Blocks | 432 |
| Trip owners written | 169 |
| Block owners written | 432 |
| Participation rows written | 788 |
| Subgroup temporary owners needing review | 29 |
| Unresolved block owners | 0 |
| Member/block Move evaluations | 789 |
| Authority matches | 710 |
| Classified mismatches | 79 |
| Unexplained mismatches | 0 |

All 79 mismatches were post-trip structural edits that legacy policy would
allow but the accepted lifecycle contract denies. Confirm is treated as the
same underlying commit-authority class as legacy Direct while preserving the
new confirmation requirement.

Typed shadow telemetry supports governance, scope, actor posture, operation,
outcome, comparison, and reason dimensions. Missing facts emit Unknown/Denied;
unexpected adapter failures emit `adapter_error` and never affect legacy Plan
State availability.

## Verification

- Real migration/backfill fixtures proved whole-group, personal, and subgroup
  owner mapping, provenance, review flags, idempotence, and boundary downgrade.
- A real migrated Review fixture proved member Move → Propose to the named
  owner.
- 171 focused tests passed.
- Ruff, diff check, and Alembic single-head passed; head is `ir05a001`.

IR-05 is complete. No client capability payload is exposed and no canonical
write is enabled; those remain later gated slices.

## Adversarial review hardening

The IR-00–05 review was closed before IR-06. Owner backfill now evaluates all
trips independently of block presence, and new-trip creation, membership-role
changes, member removal, and account deletion preserve one current shared
owner transactionally. The DB adapter rejects an owner who is no longer a
current member.

The normalized operation and lifecycle contracts now reject mismatched target,
placement, lineage, precondition, participant, child-trip, timezone, and phase
facts. The additive database foundation rejects cross-trip references for
operations, dependencies, provider transitions, branches, materialized Trip
Shapes, viewer cursors, and write-backs; destination identity and nullable
private-context dedup are also enforced physically. Account erasure replaces
embedded account UUIDs with an anonymous structural tombstone while preserving
permitted shared history.

A disposable PostgreSQL database passed upgrade, boundary downgrade/re-upgrade,
zero-block-trip owner backfill, adversarial constraint probes, ordinary owner
transfer, and account-deletion anonymization. Focused evidence was 225 offline
tests plus 10 PostgreSQL ownership/account-deletion tests.
