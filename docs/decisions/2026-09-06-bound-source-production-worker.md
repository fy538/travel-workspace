---
doc_type: decision
status: accepted
owner: backend / product / cross-repo architecture
created: 2026-09-06
decided: 2026-09-06
last_verified: 2026-09-06
expires: 2026-12-06
why_new: Names the future execution owner and activation boundary for optional Home/Places Source contribution production without adding a queue or model work to ordinary root reads.
source_of_truth_for:
  - bounded Source contribution production worker ownership
  - production-trigger and deployment boundary
depends_on:
  - ../working/complete-system-integration-roadmap-2026-09-05.md
  - ../working/live-engine-owner-path-matrix-2026-09-05.md
  - ../systems/four-root-loop-object-surface.md
  - ../../travel-agent/backend/workers/FEATURE.md
---

# Bounded Source production worker decision

## Decision

When optional Source contribution production is eventually enabled, it will run
as a dedicated job function in the existing Arq worker entry point:

```text
accepted signal / explicit warm request
  -> content-free production work item
  -> existing WorkerSettings (audio_jobs process)
  -> claim root_source_contribution_attempts lease
  -> bounded canonical owner reads
  -> bounded producer call
  -> admitted production stored in root_source_contributions
  -> Home / Places consume the precomputed handoff
```

This uses the existing worker deployment and queue. It does not create a second
scheduler, a root-specific daemon, an all-account event bus, or a new model
service. The eventual job module may be named
`backend/workers/root_source_contribution_jobs.py`, but no job is added by this
decision alone.

## Activation boundary

The worker remains dark until all of the following exist and are locally
tested:

1. A versioned, content-free work-item contract with `viewer_id`, concrete
   root/situation/audience, represented-at clock, timezone, policy/compiler
   versions, an optional canonical context reference, trigger reason, and
   idempotency key.
2. One named trigger owner. Acceptable triggers are an authorized signal,
   source correction/recomposition request, or explicit user-requested warm
   action. A routine Home/Places GET, tab focus, app launch, or generic
   background tick is not a trigger.
3. A durable enqueue/outbox handoff whose retry and deduplication behavior is
   visible without including private source text or generated prose.
4. The existing attempt lease is claimed before owner reads or provider work;
   lease loss, source revocation, audience change, and expiry prevent storage
   or delivery of late output.
5. Serving and production telemetry records latency, queue delay, read count,
   provider count, reuse, outcome, cost class, and suppression without logging
   source content or claims.

Until those gates are met, `ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED` may
only govern an explicitly injected/precomputed handoff or a controlled test;
it must not be interpreted as permission for ordinary root GETs to enqueue or
produce work.

## Why this owner

The repository already has one worker entry point, Arq registration, retries,
job identity, and deployment guidance. Reusing it keeps operational ownership
legible and prevents a second background runtime from acquiring different
timeout, retry, or shutdown semantics. The existing Source contribution
attempt and retained-production tables already provide the semantic lease and
short-lived output store; the missing piece is a durable trigger envelope, not
another persistence authority.

The worker owns execution only. It does not become the owner of Source truth,
audience grants, relationship membership, Home ranking, Places context, or
Life continuity. Canonical owner readers, the deterministic compiler, and
existing correction/invalidation paths remain authoritative.

## Explicit non-decisions

- No always-on watch, location monitor, push notification, or scheduler is
  implied.
- No provider/model call is permitted on the ordinary Home/Places response
  path.
- No generated expression becomes a durable user fact or intent merely because
  the worker produced it.
- No new universal event bus or cross-root cache is justified.
- A future worker must not enqueue itself recursively to simulate a watch.

## Roadmap consequence

I2's “production worker decision” is now owner-bound but implementation-gated.
The work-item/trigger contract now includes deterministic identity construction
(`travel-agent` commit `1ccd27a02`); equivalent requests deduplicate without
including source text or generated prose. The next implementation package is
the durable enqueue/outbox handoff plus one fake-worker lease/expiry test. Only
after that should a job function be registered. The current roadmap therefore
remains partial: no queue, scheduler, deployment flag, or production cohort is
activated by this document.
