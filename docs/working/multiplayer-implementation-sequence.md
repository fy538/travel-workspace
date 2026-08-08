---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-08
updated: 2026-08-08
why_new: Execute the accepted multiplayer evolution in bounded, verifiable commits.
expires: 2026-09-07
---

# Multiplayer implementation sequence

This is the execution plan for extending the current trip-scoped multiplayer
system into a durable, relationship-aware shared world. It preserves the
accepted cohort-one decisions in
[`2026-07-10-multiplayer-propagation-v1.md`](../decisions/2026-07-10-multiplayer-propagation-v1.md):
the shared-object path remains primary, the canonical itinerary mutation path
remains authoritative, and we do not add a second always-on realtime channel,
fluid authority, selective draft propagation, or per-vote push without a
revisit decision.

## Current baseline

- Backend multiplayer canary suites: green.
- Frontend multiplayer and journey mock suites: green.
- Live two-account/two-device certification: still pending for J04/J05/J10.
- Durable trip membership, group room, group-safe composition, proposal/vote/
  receipt flow, cross-device invalidation, and workflow observation already
  exist.
- Persistent circle identity, cross-trip relationship memory, shared workflow
  control, and a complete world-event-to-group-action loop do not yet exist.

Automated evidence and device evidence must remain separate claims. A phase is
not live-certified until the required real-account device walk is recorded.

## Execution status (2026-08-08)

- Foundation certification remains pending on the real two-account/two-device
  run; no device claim is being promoted from the automated suites.
- Explicit circle identity is partially implemented: durable circle/member/
  trip-link/event storage, owner authorization, cursor reads, mobile transport,
  an explicit pair-confirmation flow, and a read-only detail route are live in
  the code path. Mock mode stays empty/live-only and never fabricates circles.
- Unified sync is partially implemented: circle events use a monotonic sequence
  and cursor replay with membership checks. There is deliberately no new
  realtime channel yet; the client refetches durable state.
- Shared-agent context is behind `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED` (off by
  default). When enabled, only bounded kind/member-count/revision facts enter
  the group trip context; member names, IDs, event payloads, and private memory
  remain excluded. The group-action/weather vertical slice is not complete.
- Availability and location are not blank-slate systems: the codebase already
  has canonical block attendance (`attending` / `maybe` / `not_attending` /
  `undecided`) through the itinerary operation gateway, explicit local-Plan
  invite RSVP (`in` / `maybe` / `out`), and trip-scoped location disclosure
  (`off` / `coarse` / `precise`) with revocation, expiry, terminal-trip gates,
  and mutual-grant ambient coincidence checks. The remaining step-6 gap is
  product composition and certification, not a calendar or location-history
  model: no inferred free/busy, no persistent status toggle, and no automatic
  promotion of presence into relationship memory.

## Architecture rules

1. Durable domain state is server-authoritative and ledgered.
2. Presence and current activity are ephemeral, expiring projections; they are
   never relationship memory.
3. CRDT/local-first state is reserved for low-risk drafts and annotations. Plan,
   booking, expense, privacy, and authority mutations use the existing
   proposal/receipt path.
4. Every memory, recommendation, and proactive candidate carries scope,
   provenance, confidence, validity, consent, and evidence references.
5. Group-visible text must pass through `group_compose.py` or an equivalent
   explicit privacy boundary.
6. Push is an invalidation hint. The client refetches durable state and does not
   treat delivery or ordering as truth.
7. Every command is idempotent, revision-checked, authorization-checked, and
   observable.

## Commit sequence

### 1. Foundation certification and evidence reconciliation

Run the existing multiplayer backend and frontend suites, then execute the
screen-level mock journeys and the two-device runbook. Fix only regressions
found in the current shared-object path. Do not add platform primitives in this
step.

Exit gate:

- J02 invite and J04/J05 shared-object mock walks are green.
- The two-device run records whether J04/J05/J10 pass or where they fail.
- No claim is promoted above its actual validation layer.

### 2. Explicit circle identity

Add an explicit, user-confirmed circle layer above trips. A repeated roster may
produce a suggestion, but the product never silently labels a relationship.
Existing trip memories remain trip-scoped until explicitly promoted.

Initial tables:

- `social_circles`
- `social_circle_members`
- `social_circle_trip_links`
- `social_circle_events`
- `social_circle_memory_versions`

Circle memory must store evidence IDs, validity, visibility, confidence, and
correction/supersession links. A private member fact cannot be promoted without
an explicit disclosure grant or privacy-safe aggregation.

Exit gate: a second trip with the same confirmed circle can use group knowledge
without exposing any private member evidence.

### 3. Shared-agent control, behind an explicit revisit gate

Do not ship fluid authority during cohort one. First extend the durable workflow
model behind a feature flag and an explicit founder decision.

The control-plane design is:

- workflow revision and current controller;
- `agent_workflow_commands` for steer, pause, resume, cancel, and handoff;
- `agent_workflow_decisions` for approvals tied to an operation diff;
- compare-and-swap revision checks and idempotency keys;
- group-safe workflow summaries, with private inputs retained privately;
- receipts for every state-changing command.

Exit gate: two members can observe the same workflow and safely recover after a
disconnect without duplicate or unauthorized itinerary mutations.

### 4. Unified event and sync protocol

Keep the existing Postgres outbox and SSE/polling strategy for cohort one. Add a
single ordered event envelope with space ID, sequence, aggregate revision,
privacy scope, and provenance. Clients resume from a cursor, deduplicate, detect
gaps, and refetch a snapshot when history is unavailable.

Presence remains a separate short-TTL projection. A WebSocket/room coordinator
is only considered after measured connection or latency evidence justifies it.

### 5. World-event-to-group action vertical slice

Start with weather rescue because the app already has weather, itinerary, route,
Map, proposal, and receipt primitives.

Pipeline:

`world observation → affected-plan matcher → private impact evaluation →
group-safe composition → relevance/attention policy → suggestion or proposal →
canonical mutation → receipt → outcome`

Every candidate records its evidence, freshness, policy version, suppression
reason, and delivery/outcome state.

Exit gate: one real weather conflict produces a safe, reviewable, reversible
Plan + Map change on two observers.

### 6. Explicit availability and spatial sessions

Implement explicit availability windows and occasion RSVP before calendar
inference. If calendar integration is later justified, store normalized free/busy
intervals only. Implement location as expiring, purpose-bound sharing sessions
with precision and viewer controls. Do not turn physical presence into durable
relationship memory automatically.

### 7. Low-friction guest participation

Add scoped, expiring capability links for RSVP, bounded proposal voting, one
private constraint, and decision receipts. Keep private data out of URLs and
upgrade guest participation into authenticated membership without losing
attribution.

## Validation required for every commit

- focused backend tests;
- focused frontend/mock tests;
- authorization matrix and privacy adversarial tests where group visibility is
  involved;
- duplicate, retry, reconnect, and stale-revision tests for mutations;
- explicit notation of whether evidence is static, mock, backend canary, or
  live-device;
- explicit filename staging so unrelated worktree changes are never committed.

## Success milestone

The first investor-grade multiplayer proof is not more messaging. It is:

> Vesper recognizes a confirmed group, notices a real place/weather change,
> privately reasons about member impact, proposes a group-safe adaptation, lets
> the group steer or approve it, updates the shared Plan and Map, emits a
> receipt, and learns from the outcome.
