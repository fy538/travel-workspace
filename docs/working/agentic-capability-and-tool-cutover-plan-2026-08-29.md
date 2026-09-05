---
doc_type: working
status: active
owner: founder / product / architecture / AI systems / backend
created: 2026-08-29
expires: 2026-09-28
why_new: Derives a post-pivot agent capability and model-tool architecture from the twelve cross-surface fixtures, audits the current itinerary-centric registry, and defines an adapter-first retirement path that preserves canonical action safety.
promotes_to: null
supersedes: []
related:
  - agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - chat-as-agentic-interaction-layer-research-2026-08-29.md
  - systematic-product-engine-roadmap-2026-08-23.md
  - chat-artifact-closed-loop-optimization-plan-2026-08-16.md
  - ../../travel-agent/docs/architecture/Agent Control Plane Refactor.md
  - ../../travel-agent/docs/working/Tool Surface Consolidation Plan.md
  - ../../travel-agent/docs/working/flexible-plans-occasions-and-personal-projections-2026-08-21.md
  - ../../travel-agent/docs/architecture/plan-occasion-lifecycle-contract-2026-08-22.md
---

# Agentic capability and tool cutover plan

## Question

How should Vesper's model-visible tools change now that Chat is a cross-surface
agentic interface, Trip/itinerary is no longer the universal product grammar,
and flexible artifacts and instruments project a broader owner model?

## Executive decision

The current tools should not receive another mechanical namespace cleanup.
They need a semantic cutover.

The target is:

> **Model-visible tools express stable human jobs and canonical owner
> operations. Legacy handlers remain behind adapters until the newer Plan,
> Occasion, Commitment, Source, Place, Occurrence, Outcome, provider, monitor,
> and receipt authorities can replace them safely. Presentation is resolved
> after tool execution rather than invoked as a model tool.**

The itinerary is being deprecated as the universal interaction and reasoning
model, not deleted immediately as a proven writer. Flexible artifacts are not
its replacement authority. The replacement stack is:

```text
human job and selected ResourceRefs
  -> contextual capability retrieval
  -> semantic model-facing operation
  -> policy and CommandEnvelope
  -> canonical owner or compatibility adapter
  -> verified ActionReceipt / ResourceRef
  -> semantic result and projection hints
  -> native artifact, instrument, direct state, or prose
```

This avoids two bad migrations:

1. renaming `itinerary_block_update` to a vague `artifact_update` while keeping
   the old ontology underneath; or
2. turning every generated card into a model-selected tool and a competing
   state owner.

## 1. Current code audit

### 1.1 Registry snapshot

The audited `TOOL_REGISTRY` currently contains **73 model-visible tools**:

| Measure | Count |
| --- | ---: |
| Read effects | 35 |
| Propose effects | 4 |
| Commit effects | 34 |
| Durable execution class | 2 |
| `requires_trip` policy | 31 |
| `requires_itinerary` capability | 17 |
| Trip + itinerary + planning namespaces | 28 |
| Excludes the `no_trip` lifecycle | 36 |

The raw count is not itself the central problem. Contextual retrieval can
support a large underlying catalog. The problem is that lifecycle, eligibility,
names, examples, required inputs, postconditions, and presentation side effects
teach the model that a Trip and itinerary are the normal structure of work.

### 1.2 What is already strong

The code has useful substrate that should survive the product pivot:

- one immutable `ToolRegistry` joins schema, handler, capability, effect,
  authority, retry, timeout, verification, and postcondition metadata;
- `CapabilityDeclaration` supports bundles and contextual retrieval;
- deterministic eligibility is separated from relevance ranking;
- `TurnPlan` limits tools and effects per turn;
- `ActionEnvelope` and `ExecutionReceipt` create pre-dispatch authority and
  post-dispatch verification seams;
- itinerary mutations already pass through revisioned operation gateways and
  can be adapted rather than reimplemented;
- group composition, provider actions, and memory operations already have
  specialized policy paths.

This is not a tool-system rewrite. It is a change in the semantic interface
presented to the model and the context used to retrieve that interface.

### 1.3 Product-model mismatches

| Current assumption | Where it appears | Why it is now wrong |
| --- | --- | --- |
| A no-trip first turn is intake | first-turn selector and `TurnIntent.INTAKE` | The first job may be compare, explain, plan, invite, operate, or monitor |
| Lifecycle is `NO_TRIP/PRE_TRIP/ACTIVE_PLANNING/DURING_TRIP/POST_TRIP` | capability catalog | Local life, Occasions, Sources, Places, monitors, and relationships do not share a Trip lifecycle |
| Itinerary block is the primary action unit | 17 itinerary tools | Commitment, participation, occurrence, route, and provider state are distinct owners |
| Creating a structured message is a domain postcondition | `post_*`, `present_*` tools | Persisting a card proves presentation, not that the human job or owner consequence succeeded |
| Memory write is a discretionary agent action | `observe`, `fact_remember`, maintenance tools | Contribution authority and admitted evidence must gate retention and inference separately |
| Trip metadata and trip brief organize intent | `update_intent`, `trip_brief_update`, `trip_patch` | Intent may belong to a turn, Plan, Occasion, Opening, relationship, or current Moment |
| Booking hangs off a Trip | booking capability requires Trip | Provider action can protect any Commitment and may occur in a local Occasion |
| Chat chooses whether group privacy composition runs | `compose_group_message` model tool | Privacy egress should be mandatory runtime policy, not an optional model choice |

## 2. Tool design laws

### 2.1 Tools describe operations, not UI

Remove model tools whose primary job is “post a card,” “present options,” or
“post a route.” The model should return or create semantic state with stable
identity. A projection resolver decides whether Chat needs a comparison,
instrument, spatial projection, receipt, direct state, or prose.

### 2.2 Tools target owners, not containers

A tool targets a canonical `ResourceRef` or deterministically resolves one.
`commitment_update` can currently adapt to an itinerary block operation, but
the model should reason about changing a Commitment, not manipulating the
implementation container that happens to project it.

### 2.3 Capabilities describe human jobs

Capability retrieval should index jobs such as inspect, compare, shape,
coordinate, operate, monitor, reconcile, repair, and continue. Namespace and
operation names then identify the owner and action.

### 2.4 One tool is one consequential operation

Do not create a monolithic `vesper_action(op=...)` or `artifact_update` tool.
Stable, namespaced operations provide clearer selection and separate schemas,
effects, authority, idempotency, and postconditions.

### 2.5 Reads, proposals, commits, and monitoring remain distinct

Analysis does not mutate. Proposal does not imply acceptance. Commit requires
authority. Monitoring is durable continuation with scope and expiry, not a
promise in assistant prose. Reconciliation reads back reality after action.

### 2.6 Background maintenance is not a user-facing capability

Projection refresh, event acknowledgement, memory compaction, duplicate
reconciliation, and message privacy guards should run deterministically around
the agent. Exposing them as optional model tools makes system correctness depend
on model selection.

### 2.7 Artifacts are results and controls over owners

An artifact can inspect, choose, authorize, correct, undo, or open an owner.
Those actions resolve to semantic tools or commands. The existence of a card
family does not justify a matching model tool.

## 3. Target capability architecture

### 3.1 Five layers

| Layer | Responsibility | Existing substrate |
| --- | --- | --- |
| **Interaction entry** | Origin refs, selection, audience, return target, current contribution | `workbench_entry_ref`, turn metadata |
| **Turn compiler** | Immediate job, scope, contribution grant, target owners, agency ceiling | `TurnPlan`, context policy |
| **Capability catalog** | Eligible semantic operation bundles and retrieval text | `CapabilityDeclaration`, eligibility/retrieval |
| **Action gateway** | Authority, idempotency, revision, execution, readback | `ActionEnvelope`, `CommandEnvelope`, receipts |
| **Projection resolver** | Semantic role, medium hint, density, owner destination | canonical artifact projection and native renderer |

Tool handlers belong below the capability catalog. A target operation may call
a new owner directly or use a compatibility adapter over an existing handler.

### 3.2 Capability metadata v2

Extend the current declaration with product-model semantics:

```yaml
capability:
  id: commitment.update
  namespace: commitment
  human_jobs: [operate, coordinate, repair]
  operations: [commitment_update]
  allowed_channels: [personal, occasion, group]
  accepted_origin_kinds: [plan, occasion, commitment, opening, chat]
  required_resource_kinds: [commitment]
  optional_resource_kinds: [plan, occasion, provider_commitment]
  owner_kind: commitment
  effect_ceiling: commit
  authority_boundary: affected_commitment
  evidence_provided: [commitment.revision, action.receipt]
  freshness: canonical_readback
  return_contracts: [update_origin, open_owner]
  compatibility_adapter: itinerary_operation_gateway
```

Trip lifecycle becomes one optional domain condition, not the top-level
capability lifecycle. General eligibility uses:

- channel and audience;
- origin and available `ResourceRef` kinds;
- owner lifecycle and current state;
- contribution-use and action grants;
- actor capability and affected principals;
- provider connection and feature availability;
- required facts and freshness;
- current Moment; and
- operation effect and reversibility.

### 3.3 Target semantic operation families

This is a design catalog, not a requirement to expose every operation in every
turn or ship all at once.

#### Context and conversation

| Operation | Effect | Job |
| --- | --- | --- |
| `conversation_search` | read | Find permission-scoped prior discussion |
| `conversation_read_window` | read | Inspect exact surrounding discussion |
| `resource_resolve` | read | Resolve a selected or named object when deterministic entry context cannot |

`resource_resolve` must not become semantic search over all private life by
default. It receives purpose, allowed kinds, and scope from the turn compiler.

#### Source, artifact, and Life

| Operation | Effect | Owner |
| --- | --- | --- |
| `source_inspect` | read | Source custody and claims |
| `source_retain` | commit | Source custody under explicit grant |
| `source_correct` | commit | Source metadata or claim relation owner |
| `source_release` | commit | Source custody/revocation |
| `life_search` | read | viewer-safe Life read models |
| `life_read` | read | episode, artifact, person, Place, or composition projection |
| `life_compare` | read | sourced cross-episode comparison |
| `outcome_record` | commit | personal or authorized shared Outcome |
| `outcome_correct` | commit | Outcome/meaning owner and dependent invalidation |

There is no generic `artifact_write`. Canonical artifact projection is a read
adapter. A substantial generated composition may later earn a named
`composition_create` operation over Source/ResourceRefs, but only after its
custody, lifecycle, correction, and reuse owner are decided.

#### Place, world, and route

| Operation | Effect | Owner |
| --- | --- | --- |
| `place_search` | read | canonical Place/world search |
| `place_read` | read | Place identity, facts, perspectives, conditions |
| `place_compare` | read | consistent-axis comparison over named refs |
| `route_evaluate` | read | route/reachability/current margins |
| `condition_read` | read | weather, hours, crowd, transport, provider status |
| `experience_search` | read | scheduled/bookable event inventory |
| `place_contribute` | commit | governed Place contribution path |

Restaurant, activity, stay, transport, and web providers can remain specialized
behind `place_search`, `experience_search`, and provider-specific capability
bundles when their schemas or evidence differ materially. The goal is semantic
coherence, not one universal search endpoint.

#### Plan and Plan relations

| Operation | Effect | Owner |
| --- | --- | --- |
| `plan_search` | read | personal Plan inventory across local and travel contexts |
| `plan_read` | read | viewer-relative current shape and dependencies |
| `plan_compose` | read/propose | ephemeral sparse shape, no write by default |
| `plan_create` | commit | Plan owner |
| `plan_shape_update` | commit | Plan owner / compatibility operation gateway |
| `plan_relation_update` | commit | overlap, join, split, containment relation owner |
| `plan_analyze` | read | gaps, conflicts, timing, route, alternatives |
| `plan_lifecycle_transition` | commit | explicit Plan lifecycle command |
| `command_undo` | commit | original command/operation owner |

`plan_compose` replaces the assumption that generation writes a full itinerary.
It may return a one-anchor local shape, several options, or a detailed Trip
projection according to consequence—not according to which tool was called.

#### Occasion, participation, and social consequence

| Operation | Effect | Owner |
| --- | --- | --- |
| `occasion_read` | read | Occasion projection |
| `occasion_create` | commit | Occasion owner |
| `occasion_invite_prepare` | propose | invitation owner |
| `occasion_invite_send` | commit | invitation/delivery owner |
| `occasion_contribute` | commit | Occasion relation over ResourceRef or typed contribution |
| `occasion_decision_propose` | propose | decision owner |
| `occasion_decision_resolve` | commit | decision owner under constitution |
| `occasion_participation_update` | commit | membership/participation owner |
| `occasion_lifecycle_transition` | commit | Occasion owner |
| `relationship_search` | read | viewer-owned relationship space |
| `handoff_prepare` | propose | addressed handoff |
| `handoff_send` | commit | audience/delivery owner |

Group-safe composition remains a mandatory output policy around any group-bound
operation. It should not be a model-selected tool.

#### Commitment and occurrence

| Operation | Effect | Owner |
| --- | --- | --- |
| `commitment_read` | read | Commitment coordination/provider/occurrence projection |
| `commitment_change_preview` | read/propose | exact delta and conflicts |
| `commitment_propose` | propose | decision/Commitment proposal |
| `commitment_update` | commit | coordination state and shape |
| `commitment_cancel` | commit | coordination state |
| `occurrence_reconcile` | commit | occurrence state and evidence |

These operations absorb itinerary block edits by meaning. “I am sitting this
one out” is participation or occurrence reconciliation, not a block update.
“Move dinner” is a Commitment change that may project as an itinerary edit in
a Trip.

#### Provider and real-world execution

| Operation | Effect | Owner |
| --- | --- | --- |
| `provider_search` | read | provider inventory |
| `provider_prepare` | propose | exact provider action preview/handoff |
| `provider_execute` | commit | provider-backed Commitment |
| `provider_status` | read | current provider truth |
| `provider_cancel` | commit | provider-backed Commitment |

Provider operations receive a protected Commitment, mandate, budget, exact
parameters, and recovery policy. They are not gated on the existence of a Trip.

#### Moment, monitors, Openings, and delivery

| Operation | Effect | Owner |
| --- | --- | --- |
| `moment_read` | read | current situation compiler |
| `monitor_create` | commit/durable | monitor job |
| `monitor_read` | read | monitor state and last verified condition |
| `monitor_update` | commit | threshold, delivery, or protected consequence |
| `monitor_stop` | commit | monitor lifecycle |
| `opening_read` | read | Opening and its selection reason |
| `opening_transition` | commit | snooze, dismiss, act, withdraw, expire |
| `delivery_prepare` | propose | exact audience/channel payload |
| `delivery_send` | commit | delivery owner |

Location sharing is an audience-scoped relationship/permission operation, not
merely a Trip location tool. It should receive its own explicit grant operation
if retained.

#### Receipts and recovery

| Operation | Effect | Owner |
| --- | --- | --- |
| `receipt_read` | read | action receipt |
| `command_retry` | commit | original command under retry policy |
| `command_undo` | commit | original command and reversal owner |

The agent loop should automatically receive current-turn receipts. These tools
exist for later inspection or explicit recovery, not to make every successful
turn perform another lookup.

## 4. Current-to-target migration map

### 4.1 Preserve or lightly adapt

| Current tools | Target treatment |
| --- | --- |
| `conversation_search`, `conversation_read_window` | Preserve; attach purpose and ResourceRef scope |
| `search_experiences` | Adapt to `experience_search`; remove Trip framing |
| `search_restaurants`, `search_activities` | Preserve as specialized Place-search adapters or expose under `place_search` bundles |
| `get_venue_details`, `get_venue_status`, `check_distance` | Adapt to `place_read`, `condition_read`, `route_evaluate` semantics |
| `search_accommodations`, `search_transport`, `search_web` | Keep as provider/source adapters; retrieve by current job rather than Trip phase |
| `expense_log`, `expense_summary`, `expense_settle` | Preserve domain operations; target Commitment/Occasion rather than require Trip |
| `whereabouts` | Adapt to `moment_read` with explicit person/audience scope |

### 4.2 Replace model semantics; reuse handlers behind adapters

| Current tools | Target semantic operations | Compatibility path |
| --- | --- | --- |
| `trip_find`, `trip_find_similar`, `trip_read_snapshot` | `plan_search`, `life_search`, `plan_read`, `life_read`, `life_compare` | current Trip readers and Plan Shape compiler |
| `itinerary_read*` | `plan_read`, `commitment_read` | itinerary read-model gateway |
| `itinerary_*alternatives`, `*better_slots`, `*move_check`, `*gap_suggestions`, `*conflicts`, `*optimize_route` | `plan_analyze`, `commitment_change_preview`, `route_evaluate` | current deterministic itinerary analysis services |
| `itinerary_block_update`, `itinerary_block_move`, `itinerary_block_add` | `commitment_update`, `plan_shape_update` | itinerary operation gateway |
| `itinerary_attendance_set` | `occasion_participation_update` or `occurrence_reconcile` | attendance operation adapter |
| `itinerary_parallel_plan_set` | `plan_relation_update`, `occasion_participation_update` | current parallel-plan operation |
| `itinerary_block_undo` | `command_undo` | operation ledger |
| `pin_experience` | `commitment_update` or `plan_shape_update` | pin operation adapter |
| `propose_change`, `get_proposal_state` | `commitment_propose`, `commitment_read`, `occasion_decision_read` | proposal gateway |
| `get_reaction_state`, `stay_candidate_vote`, `stay_candidate_add` | Occasion decision/participation and provider candidate operations | current reaction/stay tables |
| `generate_plan` | `plan_compose` then explicit `plan_create`/`plan_shape_update` | planning workflow plus itinerary writer adapter |
| `research_trip_directions`, `generate_trip_shapes` | `plan_compose` and research capabilities | trip-shape workflow during compatibility |
| `trip_accommodation_set` | `commitment_update` plus provider relation | current Trip accommodation writer |
| `propose_trip_creation`, `promote_to_trip` | `plan_create` / Plan lifecycle; Trip specialization only when guarantees required | current creation gateway |
| `trip_patch`, `trip_brief_update` | explicit Plan/Occasion/Commitment operations | field-specific adapters; no generic intent blob |
| `propose_booking`, `confirm_booking` | `provider_prepare`, `provider_execute` | booking gateway |
| `set_location_sharing` | explicit relationship/audience grant operation | current location-sharing writer |
| `search_angles`, `plan_from_angle`, `get_take` | Life/Place research, comparison, and composition operations | Atlas readers only while evidence remains canonical |

### 4.3 Remove from the model-visible surface

| Current tools | New location / reason |
| --- | --- |
| `post_venue_card` | projection resolver after Place semantic result |
| `post_map_route` | projection resolver after route semantic result |
| `post_stay_comparison` | comparison/decision projection after candidate result |
| `present_options` | projection resolver after proposal/decision result |
| `present_trip_shapes` | projection resolver after `plan_compose` |
| `compose_group_message` | mandatory group-bound output/privacy pipeline |
| `inbound_screenshot_submit` | Admission pipeline invoked by transport before reasoning |
| `update_intent` | turn/Plan/Occasion-specific context and commands; no universal scratchpad writer |
| `observe` | governed contribution admission and scoped-learning pipeline |
| `memory_events_read`, `memory_events_mark_processed`, `memory_refresh`, `memory_observations_prune`, `memory_gaps_check` | deterministic/background maintenance or explicit account-control services |

`fact_remember`, `fact_forget`, `memory_constraint_set`, and
`memory_constraint_remove` should not be mechanically retained as general
agent tools. Map explicit user requests to Source/evidence, constraint, and
revocation authorities under the Contribution and Consequence contract.

## 5. Tool result contract

Model tools should return semantic result envelopes rather than user-facing
cards:

```yaml
tool_result:
  capability_id: commitment.update
  operation: commitment_update
  state: committed | proposed | pending | rejected | degraded
  primary_resource: {kind: commitment, id: ..., revision: ..., canonical_path: ...}
  related_resources: []
  receipt_ref: {kind: receipt, id: ..., revision: ..., canonical_path: ...}
  evidence_refs: []
  changed_fields: []
  unknowns: []
  available_operations: []
  projection_semantics:
    semantic_role: canonical_state | operational_instrument | receipt
    dominant_move: help_it_work
    job: monitor | repair | choose | other
    evidence_shape: temporal | spatial | mixed
  return_contract: {mode: update_origin, target: ...}
```

The server may suggest semantic role and evidence shape. The native client owns
lead medium, geometry, component, accessibility, and animation. A successful
projection write is not the domain postcondition.

## 6. Capability retrieval v2

### 6.1 Retrieval query

Build capability retrieval from structured turn state plus bounded language:

```text
immediate_job
+ origin surface and ResourceRef kinds
+ named/selected objects
+ target owner candidates
+ channel and audience
+ contribution and action grant
+ current Moment and owner lifecycle
+ explicit user language
```

Do not retrieve from language alone. “Move this later” is unambiguous when the
origin is a Commitment and unsafe when the origin is a generated article.

### 6.2 Eligibility before relevance

Deterministic eligibility removes operations that violate:

- actor capability;
- membership and audience;
- owner lifecycle;
- missing required ResourceRefs;
- contribution/action grants;
- provider availability;
- feature flags;
- privacy mode; or
- effect ceiling.

Semantic retrieval ranks only the eligible set. Dispatch checks authority
again.

### 6.3 Foundational capabilities

A new private Chat should always be able to:

- answer without tools;
- resolve named or attached Sources/objects;
- search the person's authorized Plans/Life when explicitly asked;
- read selected owners;
- use current Place/world search;
- privately compose and compare; and
- prepare an authorized proposal.

No universal write tool should be foundational. Commit operations become
eligible from explicit language, structured actions, existing mandates, and
resolved owner scope—not from being the first or fifth turn.

### 6.4 Surface budget

Do not optimize for a fixed global number such as fifteen tools. Optimize for:

- one to three relevant capability bundles;
- usually six to fourteen model-visible operations in a turn;
- zero presentation and maintenance tools;
- no semantically overlapping operation names in one bundle;
- inclusive fallback retrieval when confidence is low; and
- a traceable reason each operation was included or excluded.

The historical tool-consolidation work showed that removing tools can change
model behavior even when those tools were never called. Rollout therefore needs
shadow selection, scenario replay, live paired comparisons, privacy checks,
and response-quality adjudication—not only schema and unit tests.

## 7. Adapter-first migration sequence

### Phase 0 — Freeze and measure the current surface

1. Export the 73-entry registry with namespace, capability, effect, eligibility,
   required inputs, postconditions, handler, and observed call rate.
2. Add the twelve fixture IDs to turn traces and evaluation configuration.
3. Record current selected tools, calls, latency, result, privacy, and owner
   readback for any fixture the present runtime can approximate.
4. Ban new itinerary- or card-presentation model tools without an explicit
   compatibility note.

### Phase 1 — Land the cross-root turn compiler

1. Add `InteractionEntry` with origin refs, selection, audience, and return.
2. Extend `TurnPlan` with immediate job, owner candidates, grant ref, agency
   ceiling, phase, and return contract.
3. Remove `first_turn -> INTAKE` and first-turn commit suppression behind a
   shadow/flagged policy.
4. Keep current tools, but trace target job and owner semantics beside them.

### Phase 2 — Remove presentation and maintenance from model choice

1. Move `post_*` and `present_*` behavior into the semantic projection pipeline.
2. Make group-safe composition a mandatory group egress path.
3. Move inbound admission and memory/event maintenance out of the model surface.
4. Verify identical or better artifact arrival, privacy, and terminal receipts.

This phase reduces conceptual noise before changing domain writes.

### Phase 3 — Add semantic read adapters

Land read-only target operations first:

- `life_search`, `life_read`;
- `source_inspect`;
- `place_read`, `place_compare`, `route_evaluate`, `condition_read`;
- `plan_search`, `plan_read`, `plan_analyze`;
- `occasion_read`, `commitment_read`;
- `opening_read`, `receipt_read`; and
- `moment_read`.

Implement them over current authoritative readers and projection compilers.
Shadow old/new results and require identity, revision, privacy, and unknown-state
parity.

### Phase 4 — Add semantic command adapters

Expose target commands through `CommandEnvelope` while reusing proven writers:

- `commitment_update` -> itinerary operation gateway;
- `occurrence_reconcile` -> attendance/occurrence adapter;
- `command_undo` -> operation ledger;
- `plan_create/plan_shape_update` -> current planner and Trip writer where
  required;
- `occasion_*` -> graph/Occasion collaboration commands;
- `provider_*` -> booking/provider gateways; and
- `source_correct/release` -> contribution and causal invalidation owners.

Require exact owner readback and target-semantic postconditions. Do not certify
an adapter merely because the legacy handler returned success.

### Phase 5 — Add monitors and multi-owner orchestration

1. Create durable monitor jobs with thresholds, expiry, delivery, and Stop.
2. Add an orchestration receipt that references multiple independent commands
   without becoming another writer.
3. Prove partial success, pending provider truth, retry, recovery, and audience
   sequencing with A08-A10.

### Phase 6 — Retire itinerary-facing model semantics

Stop exposing old itinerary names only after:

- all P0 fixtures retrieve target operations;
- adapter results preserve revision/authority/idempotency guarantees;
- no production/eval caller requires the old schema for the signed window;
- owner projections and deep links work without itinerary-specific client
  assumptions; and
- rollback can restore old selection without undoing new canonical writes.

The itinerary writer can remain behind adapters longer than the itinerary tool
surface. Backend authority retires only when a tested general Plan/Commitment
writer owns equivalent guarantees.

### Phase 7 — Retire compatibility writers

This is a separate product and data migration. It requires:

- authoritative Plan, Occasion, Commitment, participation, provider, and
  occurrence schemas;
- backfill and dual-read parity;
- no split-brain writer;
- mobile and provider consumer migration;
- correction/undo/export/deletion parity;
- signed observation window with no compatibility-path use; and
- explicit irreversible cutover decision.

## 8. Fixture-to-tool acceptance matrix

| Fixture | Minimum target operations | Legacy adapters allowed initially |
| --- | --- | --- |
| A01 | `relationship_search`, `place_search`, `plan_compose` | Trip-direction/Place search readers |
| A02 | `source_inspect`, `plan_search`, `commitment_read`, `condition_read` | inbound/Trip snapshot/provider readers |
| A03 | `opening_read`, `occasion_create`, `occasion_invite_prepare` | graph opening and invite handlers |
| A04 | `place_read`, `place_compare`, `route_evaluate`, optional `plan_shape_update` | Place/distance/map + itinerary operation adapter |
| A05 | `life_read`, `source_inspect`, `source_correct` or `outcome_correct` | graph/source correction adapters |
| A06 | `moment_read`, `plan_read`, `commitment_change_preview`, `commitment_update`, `route_evaluate` | itinerary/current-condition gateways |
| A07 | `occasion_read`, `occasion_decision_propose`, `commitment_propose` | proposal/reaction/group compose systems |
| A08 | `commitment_change_preview`, `provider_prepare/execute`, `commitment_update`, `delivery_send` | itinerary, booking, group delivery adapters |
| A09 | `provider_status/search/execute`, `commitment_update`, `delivery_send`, `receipt_read` | provider and itinerary gateways |
| A10 | `condition_read`, `monitor_create/read/stop`, `delivery_send` | new monitor owner required; no transcript-only adapter |
| A11 | `place_read`, `opening_read`, `source_inspect` | Place/opening selection traces |
| A12 | `life_read`, `life_compare`, `place_search/read`, optional `opening_transition` | graph, Place, research, composition adapters |

## 9. Verification gates

### Contract

- every model tool has one owner kind, effect, authority boundary, evidence
  output, postcondition, and return contract;
- every commit accepts or resolves a canonical target `ResourceRef`;
- presentation and maintenance operations are absent from model-visible tools;
- old and new names cannot both be selected in one production turn;
- generated API types and mobile action registries agree after contract changes.

### Behavioral

- all twelve fixtures select sufficient operations without exposing irrelevant
  Trip/itinerary tools;
- first-turn A01, A02, and A10 are not routed into intake;
- simple reads do not call commit tools;
- contribution grants do not widen after successful action;
- group fixtures preserve privacy and participation control;
- silence and answer-only outcomes remain possible.

### Execution

- each commit produces verified, failed, or pending owner readback;
- duplicate retries create no duplicate domain consequence;
- partial multi-owner success remains partial in prose and projection;
- Undo targets the original command and owner revision;
- provider state never derives from Plan state;
- occurrence never derives from ticket, reservation, or location alone.

### Product

- the user can understand what Vesper can do from contextual entry verbs and
  successful consequences rather than a capability catalog;
- Chat remains calm and conversational;
- Home, Places, and Life receive value rather than workflow exhaust;
- local, social, live, and longitudinal cases work without a Trip container;
- detailed Trip operations retain their existing guarantees when needed.

## 10. First implementation slice

The first code slice should be **semantic read and entry infrastructure**, not a
new Plan writer:

1. add the typed `InteractionEntry` and return contract;
2. compile and trace `immediate_job`, origin refs, owner candidates, and agency
   ceiling;
3. stop treating first turn as intake in shadow mode;
4. introduce `plan_read`, `commitment_read`, `place_read`, `source_inspect`, and
   `life_search` as target read adapters;
5. move one presentation tool—preferably `post_map_route`—behind the projection
   resolver to prove semantic result versus UI separation; and
6. certify A01, A02, A04, and A11 before enabling target commands.

This slice changes the agent's worldview without risking canonical writes. The
next slice can adapt `commitment_update`, `occurrence_reconcile`, and
`command_undo` over the proven itinerary operation gateway.

## Closing principle

> The tool surface should teach Vesper how the person's world is structured
> now—not preserve the product ontology that happened to exist when the first
> agent was built.
