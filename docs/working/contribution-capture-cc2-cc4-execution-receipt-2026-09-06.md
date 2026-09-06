---
doc_type: working
status: active
owner: founder / Contribution and Capture
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Records the accepted derivative-expiry gate and the current source, Life, and mobile evidence boundary for the next cross-root rehearsal.
supersedes: []
depends_on:
  - contribution-capture-outcome-handoff-receipt-2026-09-06.md
  - contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - complete-system-integration-roadmap-2026-09-05.md
---

# Contribution/Capture CC-2 → CC-4 Execution Receipt

**Date:** 2026-09-06
**Owner lane:** Contribution and Capture

## Delivered source-side package

Backend commits `70762af24` and `7966cdb9f` close the accepted copy/consumer
expiry seam in the Intake v2 normalizer. URL retrieval and audio
transcription now re-check the owner submission's custody and transient
deadline before reading source bytes or binding a derived source. The URL path
also performs a preflight before returning an already-existing derivative, so
a retry cannot reuse a child after the source's ephemeral window has ended.
Explicit
`source_and_derived` retention remains durable by contract; invalid custody,
expired custody, and malformed clocks fail closed.

The package changes no Chat history rule, retention policy, Life row, API
schema, or product owner. The existing final-normalization check remains in
place as the second boundary after a provider call.

## Evidence

- `tests/inbound/test_intake_v2_web_lineage.py`
- `tests/inbound/test_intake_semantic_jobs.py`
- `tests/inbound/test_intake_v2_retention.py`
- Focused offline result: **15 passed, 3 deselected** after both commits.
- Ruff, compile, and `git diff --check` passed for the owned files.

The focused mobile useful-first path was rerun by explicit test path against
the current `travel-app` checkout: **23 tests passed** across Share Capture,
audio capture, and resumability. This confirms the existing “Already useful”
result precedes optional interpretation controls; it is not native-device,
real-transport, or generated-content acceptance.

## Receiving-lane status

The Life receiver is now landed on the shared backend branch. Outcome shadow
delivery re-reads current graph authority, carries a separate audience
dependency token, and uses the existing Life index CAS/withdrawal/restore
writers. Direct Occasion membership changes and account erasure emit repair
events for both Encounter and participant-scoped Commitment Outcomes. The
implementation is in commits `ba9463c2a`, `fd66f9f1f`, `329060a88`,
`afb13c6fa`, `6c42c92f7`, and `68e72d3f7`.

The joint source → outbox → Life shadow-index rehearsal now passes **6
PostgreSQL tests** in
`tests/life_projection/test_outcome_projector_postgres.py` and
`tests/domains/experience_graph/test_outcome_life_producers_postgres.py`.
It covers shared Encounter and Commitment readback, member departure
withdrawal, stale replay non-resurrection, explicit rejoin restoration, owner
erasure withdrawal, and surviving-audience repair. Life remains shadow-only;
this does not authorize reader serving or cutover.

Life withdrawal hardening has since landed in `travel-agent` commit
`1faa8a49c`: withdrawal carries the exact owner revision and prior audience
dependency token, and the index writer applies both as optional CAS predicates.
The focused Outcome/index suite now passes **25 tests**, including a PostgreSQL
proof that an old audience token cannot revoke a later restoration. The
first-insert-after-deletion interleaving still requires an owner-side
publication fence before historical fan-out or serving cutover.

The canonical inline retained-source capture boundary now emits its
content-free Life owner event in `travel-agent` commit `5a6fce1f2`, aligning
direct Share Capture with the existing upload/finalize path. Its focused
PostgreSQL proof reaches Life readback and owner deletion withdrawal. This
does not promote the retained-source projector to serving, and the separate
representation/unrepresentation repair extension remains outside this
committed package until its ordering and current-authority proof are green.

## Next connected checkpoint

Run one joint Life rehearsal for each Outcome family:

1. Record a shared Commitment Outcome and a shared Encounter Outcome.
2. Consume the content-free source-owner event through the durable Life
   outbox and shadow projector; verify owner readback for every authorized
   viewer.
3. Correct the Outcome to private or remove a member; verify the audience
   union withdraws the former viewer while retaining the owner's record.
4. Replay the old revision out of order; verify CAS prevents resurrection.
5. Re-run the current revision only through an explicit owner-authorized
   restore path.

The Postgres/worker evidence is now recorded in the Life handoff and roadmap.
The next Capture package is CC-4's complete useful-first journey with real
content and native evidence; the next Life hardening gate is broader
cross-viewer/race comparison while keeping Outcome serving disabled.
History-specific Chat-image policy, remaining writer families,
intention/social/expense owner commands, and release/transport evidence remain
separately gated.
