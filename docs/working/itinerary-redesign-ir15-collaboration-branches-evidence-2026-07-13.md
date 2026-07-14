---
doc_type: working
status: active
owner: frontend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record IR-15 frontend adoption of canonical proposals, participation, ownership, and parallel branches.
source_of_truth_for: [itinerary-redesign-ir15-collaboration-branches-evidence]
---

# IR-15 — Collaboration and branches evidence

Date: 2026-07-13
Lane: `itinerary-foundation`
Status: implementation complete behind dogfood flags; paired two-account device exposure remains

## Outcome

IR-15 extends the IR-14 Change path without creating another editor or policy
model. Direct, Confirm, Propose, and Denied all render from the same server
preview. Direct and Confirm commit through IR-07; Propose persists the exact
normalized operation through the IR-08 native proposal gateway; Denied remains
terminal and performs no write.

Review Stack remains the current-decision inbox. A proposed operation does not
appear as a landed plan change, and the proposal result routes to the existing
proposal review surface. Changes remains settled history and exceptional
attention/recovery, backed by IR-09.

## Exposure flags

The frontend additions are independently default-off:

- `EXPO_PUBLIC_ITINERARY_COLLABORATION_V2`
- `EXPO_PUBLIC_ITINERARY_ATTENDANCE_V2`
- `EXPO_PUBLIC_ITINERARY_BRANCHES_V2`

They compose with the IR-13 read shell and IR-14 operation-family flags. Native
proposal dogfood also requires backend `ITINERARY_OPERATION_PROPOSALS_V2`;
parallel writes require backend `ITINERARY_BRANCHES_V2`; preview and commit
gates remain independent.

## Resolver and proposal convergence

- One preview body renders all four server outcomes.
- Confirm sends hash-bound confirmation evidence for the exact preview.
- Propose sends the exact normalized preview operation to
  `POST /api/trips/{trip_id}/itinerary/operations/proposals` with a stable
  idempotency key and group-safe summary.
- A directly authorized operation exposes “Ask group instead” only when the
  server sets `can_voluntarily_propose`.
- Proposal creation clears the local draft only after durable proposal truth is
  returned, invalidates Review/Plan/Details/Map projections, and opens the
  existing Review surface by stable proposal identity.
- No IR-15 path submits provider-changing intent or infers recovery.

## Participation, occurrence, and ownership

- `set_attendance` changes only the authenticated traveler’s intention and
  retains the shared stop.
- `mark_occurrence` is a separate factual operation and cannot alias Remove or
  personal attendance.
- The new read shell routes live Skip/Done entrances into canonical Change
  instead of calling legacy block writers.
- Add may explicitly construct personal, subgroup, or whole-group
  participation. Every payload names its planned participants and decision
  owner before preview.
- Object detail presents the viewer-safe IR-12 participation scope, planned
  travelers, decision owner, and branch owner. Missing/deleted roster identity
  renders as “Former traveler”; raw identifiers are not exposed.

## Parallel branches

- Plan renders one compact group-split band per stable branch group, with the
  split anchor, each branch, participants, explicit branch owner, and rejoin.
- Creation constructs one atomic `create_parallel_plan` containing both branch
  block sets, planned participants, branch decision owners, organizer topology
  owner, split, and rejoin, bound to the day revision.
- Editing constructs one atomic `update_parallel_plan`, preserving branch and
  branch-group identities and binding the group/day revisions.
- A traveler may move their participation between existing branches without
  being granted ownership. Moving the current branch owner is disabled because
  this UI does not silently transfer ownership.
- Branch construction uses the roster only to name required stable identities;
  preview/commit still resolve actual authority on the server.

## Organizer transfer, departure, People, and Settings

The existing settings flow already requires an organizer to hand off before
leaving, changes the role first, and then performs departure. The backend
foundation handoff retains the atomic owner-reconciliation and departed-owner
fail-closed proofs. IR-15 consumes the resulting current roster and canonical
branch projection; it neither rewrites historical attribution nor treats
multiple admin-like roles as multiple itinerary owners.

People and Settings remain viewer-scoped factual entrances. Existing member
rows expose management only to the current organizer, and non-organizer trip
information controls remain disabled or descriptive. The new object and branch
surfaces expose no organizer/provider mutation based on client role; every
itinerary mutation ends at server preview.

## Exit-gate fixtures

Frontend fixtures cover:

- solo/direct IR-14 regression;
- Open-member direct attendance;
- Review-member exact proposal creation;
- voluntary organizer/group review;
- Confirm evidence bound to preview hash;
- Denied with no commit/proposal action;
- personal and subgroup Add with explicit owner;
- atomic branch create/update with stable identities and revisions;
- two-account organizer/member naming;
- departed/deleted member rendering without raw identity disclosure;
- expense/provider objects never aliasing structural Change.

The committed IR-04/05 resolver, IR-08 proposal, IR-11 compound branch, and
IR-12 viewer-scoped read-model suites remain the backend authority for Open,
Review, transfer/departure, privacy/deletion, and atomic topology behavior.

## Verification

- TypeScript (`npm run typecheck`) — pass
- IR-13/14/15 focused and Plan smoke tests — 39/39 pass
- Fully flagged Plan smoke — 13/13 pass
- Resolver/proposal/attendance/branch component fixtures — 6/6 pass
- `npm run state-ownership` — pass
- `npm run api-boundaries` — pass
- `npm run accessibility-governance` — pass
- `npm run qa:flags:test` — pass
- Focused ESLint — zero errors
- `git diff --check` — pass

The remaining exposure check is a two-device organizer/member dogfood pass over
one Open direct edit, one Review proposal/accept/apply, one attendance change,
and one parallel split/rejoin. It should compare both accounts’ Review, Plan,
Details, and Changes projections and exercise organizer handoff/departure. This
is rollout evidence, not permission to broaden into IR-16 provider, Replan,
Vesper-entry, or lifecycle work.
