---
doc_type: working
status: active
decision_status: proposed
owner: founder / Life / Integration
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Separates Outcome content revision from audience revision before a shared Outcome producer can safely write Life rows.
supersedes: []
---

# Decision proposal: Outcome audience CAS in Life

## Status and recommendation

**Contract accepted for the Life writer, but not a serving cutover.** The
Outcome audience resolver/event envelope remains a shadow-only producer
dependency; this document does not authorize a migration, a Life serving
cutover, or a change to the canonical Experience Graph owner.

**Recommendation:** retain the canonical integer
`personal_outcomes.revision` as `owner_revision`, and use the existing derived
index `dependency_fingerprint` as a second, explicit compare-and-swap token for
audience/dependency authority. Do not hide the audience hash inside the
integer owner revision, and do not treat `dependency_fingerprint` as an
unconditional replacement for owner revision.

This keeps two facts separate:

- **content revision:** the Outcome's own correction/visibility revision; and
- **audience revision:** the active Occasion-membership or Commitment-
  participant state that determines who may see the derived row.

The current Life index already stores `dependency_fingerprint`, but its writer

### Implementation receipt (2026-09-06)

The writer/readback seam is now implemented in `travel-agent` commit
`66f378fc1`:

- `read_life_index_owner_state` reads both `owner_revision` and
  `dependency_fingerprint`;
- upsert and explicit restore accept an optional, identity-complete
  `expected_dependency_fingerprint_by_identity` map;
- SQL compares the dependency token when supplied while preserving owner-only
  behavior for legacy families; and
- restore checks both tokens before attempting to reauthorize a withdrawn row.

The focused index contract/projector/readback/shadow suite passes **28 tests**
and `ruff check` passes for the touched files. This proves the writer contract
and its compatibility boundary only; the Outcome producer/projector still must
provide and use the audience token before any serving decision.

The first shadow consumer is now also landed in `travel-agent` commit
`ba9463c2a`. It forwards the typed audience token across the event bus,
re-reads current graph authority, and writes the token through the two-token
CAS seam. Its focused Outcome/Life-index/event-bus suite passes **63 tests**.
This is still shadow delivery: no reader cutover or production activation is
implied, and PostgreSQL race proofs remain outstanding.

Direct Occasion join/leave now emits encounter audience-repair events in
`travel-agent` commit `fd66f9f1f`; Commitment Outcomes remain scoped to their
participant set. Account erasure now emits owner withdrawal before deletion
and repairs surviving encounter audiences in `329060a88`; `afb13c6fa` adds
the equivalent repair for surviving Commitment Outcomes, and `68e72d3f7`
keeps the viewer-relative Together predicate participant-scoped for linked
Commitment Outcomes. The
focused Outcome/account-lifecycle run now covers 27 tests, including the
PostgreSQL proofs. No current reconciler mutates the audience sets; a future
reconciliation writer must reuse these producer seams. Broader race coverage
remains a separate checkpoint.

## Why one owner revision is insufficient

An Outcome can remain at revision `3` while an authorized viewer leaves an
Occasion or a Commitment participant is removed. The canonical Outcome row has
not changed, but the viewer-relative Life row must be withdrawn. Conversely, a
viewer can be reauthorized at the same Outcome revision and the row may be
explicitly restored. A CAS over the integer alone cannot distinguish these
states.

The event envelope now carries both pieces of evidence:

- `owner_revision` — the integer Outcome revision;
- `payload.audience_revision` — the deterministic
  `outcome-audience:v1:*` token; and
- `payload.viewer_ids` — the before/after fan-out union.

The derived row must retain the audience token used to materialize it and
compare it on every audience-sensitive write.

## Proposed write contract

Extend the Life index writer/readback contract, without changing the canonical
Experience Graph schema:

```text
read_owner_state(...) ->
  owner_revision,
  dependency_fingerprint,
  status / suppression / deletion state

upsert(entry,
  expected_owner_revision,
  expected_dependency_fingerprint)

restore(entry,
  expected_owner_revision,
  expected_dependency_fingerprint)
```

The SQL guard becomes:

```text
current.owner_revision = expected_owner_revision
AND current.dependency_fingerprint = expected_dependency_fingerprint
```

For owner families that do not yet publish a dependency token, the existing
owner-only CAS behavior remains available. Outcome's shared adapter must always
provide one. A missing token for a shared Outcome is a fail-closed error, not a
wildcard.

The entry keeps `owner_revision` as the integer string and stores the audience
token in `dependency_fingerprint`. The token is an authorization/dependency
fingerprint, not user content and not a new source of truth.

## Producer/projector obligations after adoption

1. Outcome create/update events include both tokens and the before/after viewer
   union.
2. Occasion membership and Commitment participant changes emit Outcome repair
   events with the new audience token, even when the Outcome integer revision
   did not change.
3. The projector reads current graph authority for each viewer, builds the
   current audience token, and writes only when both CAS dimensions match.
4. A withdrawn row is never restored by an old event. Explicit reauthorization
   must supply the current owner and audience tokens.
5. Account erasure emits a withdrawal event using the prior audience token (or
   an identifier-only erasure repair) before the owner row disappears, and
   repairs surviving encounter and Commitment Outcomes after their membership
   sweeps.

## Acceptance fixtures

The writer change is ready only when these cases pass:

1. Same Outcome revision + same audience token is idempotent.
2. Same Outcome revision + changed audience token updates an active row and
   withdraws a departed viewer.
3. Older audience token cannot overwrite a newer token at the same owner
   revision.
4. Newer Outcome revision with the old audience token still updates content
   safely.
5. Withdrawn rows require both current tokens for explicit restore.
6. Private owner-only Outcomes preserve existing owner-revision behavior.
7. Shared Commitment and Occasion Outcomes use distinct audience tokens and do
   not widen one another's audience.
8. Non-Outcome owner families retain their current CAS behavior in regression
   tests.

## Sequencing

1. **Complete:** accept this contract and update the Life index writer/readback
   types (`66f378fc1`).
2. Add pure and PostgreSQL CAS proofs, including same-owner-revision audience
   changes and restore.
3. **Complete in shadow:** update the Outcome adapter/projector to store the
   event's audience token as its dependency fingerprint (`ba9463c2a`).
4. **Complete for direct Occasion membership:** add the canonical encounter
   audience-repair producer and PostgreSQL proof (`fd66f9f1f`).
5. **Complete for account erasure:** owner withdrawal plus surviving encounter
   and Commitment repair producers and PostgreSQL proofs landed in
   `329060a88` and `afb13c6fa`. No current reconciliation writer mutates
   membership audiences; any future one must call these helpers and add
   stale-replay/withdrawal/restore proofs.
6. Only then consider any serving experiment. Keep
   `supports_delta_delivery` false until the database race package is complete.

Related records:

- [Outcome shared-audience and revocation proposal](life-outcome-shared-audience-decision-2026-09-06.md)
- [Life owner-change handoff](life-owner-change-delivery-handoff-2026-09-06.md)
- [Life complete-system roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md)
