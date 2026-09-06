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

Backend commit `70762af24` closes the accepted copy/consumer expiry seam in
the Intake v2 normalizer. URL retrieval and audio transcription now re-check
the owner submission's custody and transient deadline immediately before a
derived source can be bound. The URL path also performs a preflight before
returning an already-existing derivative, so a retry cannot reuse a child
after the source's ephemeral window has ended. Explicit
`source_and_derived` retention remains durable by contract; invalid custody,
expired custody, and malformed clocks fail closed.

The package changes no Chat history rule, retention policy, Life row, API
schema, or product owner. The existing final-normalization check remains in
place as the second boundary after a provider call.

## Evidence

- `tests/inbound/test_intake_v2_web_lineage.py`
- `tests/inbound/test_intake_semantic_jobs.py`
- `tests/inbound/test_intake_v2_retention.py`
- Focused offline result: **15 passed, 3 deselected**.
- Ruff, compile, and `git diff --check` passed for the owned files.

The focused mobile useful-first path was rerun by explicit test path against
the current `travel-app` checkout: **23 tests passed** across Share Capture,
audio capture, and resumability. This confirms the existing “Already useful”
result precedes optional interpretation controls; it is not native-device,
real-transport, or generated-content acceptance.

## Receiving-lane status

The parallel Life worktree (`codex/life-owner-delivery`, commit
`b4d87161f`) contains the receiving-side shadow delivery implementation:
current-authority rebuild, owner-revision CAS, withdrawal, explicit restore,
stale/out-of-order handling, and viewer-scope validation. Its focused unit
rehearsal is **39 passed** across the change-event, delivery, index, broadcast,
and retained-source suites.

That result is receiver evidence only. It does not yet prove a real
Outcome-source mutation through the shared outbox, Postgres delivery worker,
Life index readback, and correction in one environment. The Life lane owns
that projector/index work; Capture must not write Life rows or merge the
parallel branch implicitly.

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

Record the Postgres/worker evidence in the Life owner matrix before treating
Outcome delivery as ready for serving or broad cutover. After that checkpoint,
the next Capture package is CC-4's complete useful-first journey with real
content and native evidence. History-specific Chat-image policy, remaining
writer families, intention/social/expense owner commands, and release/transport
evidence remain separately gated.

