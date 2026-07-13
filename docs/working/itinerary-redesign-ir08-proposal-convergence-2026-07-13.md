---
doc_type: working
status: active
owner: backend / frontend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Document IR-08 proposal convergence, durable transitions, privacy boundary, and verification evidence.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir08-proposal-convergence]
---

# Itinerary redesign IR-08 — proposal convergence handoff

Date: 2026-07-13
Branch: `codex/itinerary-foundation`
Repositories: `travel-agent`, generated OpenAPI types in `travel-app`

## Outcome

IR-08 now gives itinerary proposals one canonical executable identity. A new
proposal persists the exact `NormalizedItineraryOperation`, its server-authored
creation-policy snapshot, and the preview identity that produced that policy.
The proposal's intent fields are protected by a PostgreSQL immutability trigger.

Acceptance and application are separate durable transitions:

1. accept atomically stamps `resolution_started_at` and `accepted_at`;
2. apply re-runs current operation preview and the IR-07 commit gateway;
3. only a successful commit stamps `applied_at` and `applied_operation_id`.

This preserves the existing product truth that “accepted” does not imply “the
plan changed.”

## Canonical persistence

Migration `ir08a001_itinerary_operation_proposals.py` adds
`itinerary_operation_proposals`, linked one-to-one to the existing
`change_proposals` group-facing read model.

Immutable creation evidence:

- `operation_id`
- `normalized_operation`
- `creation_policy_snapshot`
- `creation_preview_id`
- `creation_preview_hash`
- `creation_idempotency_key`
- `created_at`

Mutable resolution evidence:

- `resolution_started_at`
- `accepted_at`
- `applied_at`
- `withdrawn_at`
- `resolution_actor_id`
- `applied_operation_id`
- `rebased_from_proposal_id`
- `rebased_to_proposal_id`
- monotonic `revision`

Database checks prevent apply-before-accept and withdraw-after-resolution-start.
Trip-scoped creation idempotency is unique. A trigger rejects updates to the
operation, creation policy, preview identity, idempotency identity, trip, or
creation timestamp.

## Gateway behavior

`backend/core/itinerary_proposal_gateway.py` is the proposal state-machine
choke point.

- Creation authenticates the human principal, applies the group-copy privacy
  gate, runs a fresh preview, rejects currently denied intent, and atomically
  inserts the legacy read model plus canonical evidence.
- Manual and Vesper creation use the same gateway and operation contract.
  Vesper still carries `initiator=vesper`, the requesting human in both human
  attribution fields, and must have current preview delegation.
- Acceptance requires a current organizer/admin and re-runs the complete
  preview policy: membership/authority, lifecycle, protection/provider facts,
  and revisions.
- Apply re-runs preview again under locks and commits through IR-07. An
  accepted proposal is the only internal authorization that can satisfy a
  current `propose`/`confirm` outcome without fabricating direct authority.
- The commit gateway verifies that the proposal is accepted, matches the exact
  operation, and is being executed by a current organizer/admin.
- Withdrawal uses the same locked row and a conditional
  `resolution_started_at IS NULL` update. Accept/withdraw races therefore have
  exactly one winner.

## Stale intent

Revision-stale acceptance or application never rewrites the stored operation.
The gateway:

1. reads current block/day revisions;
2. creates a new operation ID with refreshed preconditions;
3. runs a new preview and persists a new attributed proposal;
4. links old and new proposal IDs in both directions.

If staleness is found during acceptance, the old proposal becomes
`superseded` and the replacement remains `open`. If it is found after an
already-durable acceptance, the original remains accepted but unapplied with
`apply_error=revision_stale_rebased`, and the replacement remains open. This
keeps acceptance history honest.

## API and adapters

Default-off flag: `ITINERARY_OPERATION_PROPOSALS_V2`.

Native routes:

- `POST /api/trips/{trip_id}/itinerary/operations/proposals`
- `POST /api/trips/{trip_id}/itinerary/operations/proposals/{proposal_id}/accept`
- `POST /api/trips/{trip_id}/itinerary/operations/proposals/{proposal_id}/apply`
- `POST /api/trips/{trip_id}/itinerary/operations/proposals/{proposal_id}/withdraw`

The existing proposal resolve endpoint detects canonical records behind the
flag and delegates accept/apply/withdraw/reject/supersede to the new gateway.
The current accept response remains the legacy `ProposalDetail`, preserving
client compatibility. Proposal automation likewise detects canonical records,
resolves under a current organizer, and uses the same accept/apply sequence.

The plan edit-commit propose path now translates legacy move/swap/remove intent
into an exact operation and creates a canonical proposal behind the same flag.
The legacy direct-write behavior remains unchanged while the flag is off.

The broad Concierge `propose_change` tool and proactive suggestion producers
remain legacy creation producers while the flag is off. IR-16 still owns their
complete typed-input translation (especially add/modify shapes that do not yet
carry enough placement/entity detail). They must move to this gateway before a
chat-wide flag flip; the IR-08 manual/Vesper parity proof covers the canonical
gateway with both attribution modes, not every legacy producer.

The native endpoints are listed as built-but-dark in route coverage until the
itinerary shell adopts their distinct state transitions.

## Verification

Focused disposable-PostgreSQL proof:

```text
16 passed
```

This covers:

- manual/Vesper semantic parity and attribution;
- immutable creation policy/operation evidence;
- accepted-before-applied durability;
- accepted proposal commit through current policy;
- stale acceptance rebasing without mutation;
- sequential and truly concurrent accept/withdraw arbitration;
- IR-07 transaction/idempotency regression cases;
- native route default-off and accept/apply separation.

Migration proof:

```text
upgrade -> ir08a001
downgrade -> ir05a001
re-upgrade -> ir08a001 (head)
```

Additional results:

```text
IR-08/legacy proposal focused offline: 228 passed
automation/flags/schema/route focused: 105 passed
auth coverage: 14 passed
frontend TypeScript: clean
frontend focused Jest: 54 passed
OpenAPI snapshot: fresh
generated schema.gen.ts: fresh
compatibility ledger: clean
ruff: clean
mypy (new gateways/routes): clean
```

The full offline backend audit initially finished with:

```text
11,463 passed, 21 failed, 2 skipped, 599 deselected, 1 xpassed
```

The one newly exposed failure was the route-auth ratchet not recognizing a
factored membership helper. The native routes now call the standard membership
guard directly; the auth suite then passed `14/14`. The full audit was not
rerun for another three minutes after that isolated fix. The remaining 20 are
the same unrelated baseline families reported in IR-07: the unmigrated shared
database, search auth fixture, booking/tool-contract cases, Farout reads, and
postcard actor fixtures. IR-08's focused and disposable-database suites are
green. The disposable database was removed.

## Rollout and IR-09 handoff

Keep `ITINERARY_OPERATION_PROPOSALS_V2` off until a dogfood client explicitly
uses native create/accept/apply/withdraw or the legacy proposal adapter is
enabled for a selected trip cohort. Preview and commit flags remain independent.

IR-09 can now project proposal acceptance, application, stale rebase links, and
the committed operation from one evidence chain. It should add recovery/history
projections without collapsing accepted into applied, and should treat the
rebased proposal as a new change rather than an edit to historical intent.
