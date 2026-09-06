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
including source text or generated prose. The durable handoff now reuses the
existing `agent_workflows` lease/idempotency fence (`travel-agent` commit
`d0f3b395b`), including a current-clock gate for the future worker. A dark
worker adapter is now implemented and locally tested (`travel-agent` commit
`b4a2b4f91`): it claims through that fence, rejects stale work before and after
execution, requires canonical readback for produced or reused output, and
records only content-free outcomes. It remains unregistered and cannot be
reached from ordinary Home/Places GETs. The canonical executor now exists as an
injection-only adapter; the deployment envelope is explicit and locally tested
(`travel-agent` commits `08505058d` and `7f88e0f08`): policy/compiler versions,
Home/Places scope, lease duration/renewal, execution timeout, retry budget, and
dark-versus-controlled cohort are all bounded before a worker can be registered;
sync executor calls use a dedicated fixed pool rather than the process-wide
default executor.
The canonical owner seam is now also explicit in `travel-agent`:
`SourceContributionCanonicalExecutor` (`travel-agent` `467be5711`) delegates to the existing continuity
path, resolves only an injected context owner, and verifies a post-write
canonical readback before reporting produced/reused success. Its continuity
readback hook fails closed on a missing or mismatched durable result; 17 focused
contract/continuity tests pass. The adapter is still injection-only: no
provider, context repository, queue registration, or production cohort is
activated by this document. Before an Arq job can be registered, the product
must name the concrete context/readback owners and bind this adapter to a
controlled cohort with real cost/latency evidence.

The production/readback owner is already concrete: the existing
`root_source_contributions` store and its `get_current_source_contribution` /
`complete_source_contribution_attempt_with_production` gateways. The context
owner is now clock-preserving as well: `travel-agent` `64230fb0e` extends the
Places handle reader with an explicit `now` and exposes
`resolve_canonical_places_context`, which accepts only a `places_context` ref,
revalidates the handle, and returns the existing `PlacesContext`. The current-
context loader remains a different Opening-result owner and is not substituted.
Controlled registration still requires an explicit injected resolver/producer
binding and real cost/latency evidence.
