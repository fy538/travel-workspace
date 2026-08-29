---
doc_type: working
status: active
owner: founder / product / architecture / AI systems / backend
created: 2026-08-29
expires: 2026-09-28
why_new: Converts the post-pivot agent and Chat architecture audit into a reversible, implementation-ready shadow engineering package with exact contracts, compatibility mappings, fixtures, telemetry, PR boundaries, rollout gates, and exit criteria.
package_status: proposed
scope: backend shadow architecture; no product-serving cutover
decision_class: founder-only architecture
promotes_to: null
supersedes: []
related:
  - current-agent-chat-architecture-repurpose-audit-2026-08-29.md
  - agentic-capability-and-tool-cutover-plan-2026-08-29.md
  - agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - contribution-contract-fixture-pack-2026-08-29.md
  - chat-as-agentic-interaction-layer-research-2026-08-29.md
---

# Agentic Semantic Facade engineering package

## The decision

The next engineering package should **not** rewrite the Concierge agent, expose a
new tool set, or start implementing the new Home experience through isolated
features.

It should build a **shadow-only Agentic Semantic Facade** beside the existing
Concierge runtime.

For every eligible turn, this facade will compile the information the system
already possesses into the post-pivot product grammar:

1. where the person came from and what is in scope;
2. the immediate human job;
3. the contribution gesture and five authority axes;
4. the canonical owners that may be read or affected;
5. the semantic operations and phases that would satisfy the job;
6. the maximum agency permitted by current authority;
7. the expected projection, destination, return behavior, and residue; and
8. the mismatch between this target frame and what the legacy runtime actually
   selected, called, changed, and verified.

The existing prompt, tool selection, model loop, action authority, owner
gateways, receipts, and client output remain authoritative throughout this
package.

The output is not a new user-facing feature. It is an executable architectural
instrument that tells us, turn by turn, how much of the new product already
exists, which legacy capabilities can be adapted, and where the actual missing
owners and operations are.

This is the right first package because it changes the system at the **semantic
seam** without prematurely changing behavior. It lets the large product become
concrete as a coherent architecture rather than as a pile of new feature
branches.

## Executive scope

### This package does

- introduce frozen, provider-neutral contracts for contribution and target
  agentic-turn semantics;
- normalize existing `ConversationSeed`, composer attachments, pending-turn
  Admission, conversation scope, and structured actions;
- reuse canonical `ResourceRef` values only after server-side resolution;
- represent unresolved client hints honestly as locators rather than fabricated
  owner references;
- define a reviewed target semantic-operation catalog and explicit legacy
  compatibility mappings;
- compile the twelve cross-surface product fixtures into exact machine-readable
  frames;
- dark-run the compiler beside real Concierge turns behind a default-off flag;
- compare the target frame with current selected tools, executed actions, and
  receipts;
- persist only bounded, content-free metrics in `ai_quality_events`; and
- produce an operator readout with explicit readiness and blockage reasons.

### This package does not

- change any system prompt or skill prompt;
- change the tools served to the model;
- add target tool schemas to the provider request;
- execute a target semantic operation;
- add a new database table;
- change Intake custody or contribution retention behavior;
- replace `TurnPlan`, `ActionEnvelope`, `ExecutionReceipt`,
  `CommandEnvelope`, or `ActionReceipt`;
- expose `InteractionEntry` through OpenAPI;
- change the mobile Chat, Home, Places, or Life UI;
- make the first-turn lane stop behaving as Intake;
- rename Trip/itinerary nouns across the repository;
- implement the generalized monitor owner;
- make Home or Places render new artifacts; or
- claim that unavailable Life, Opening, relationship, or monitor operations
  already exist.

### Package exit

This package is complete when the facade is inert with the flag off, the
provider surface remains exact, all twelve agentic product fixtures compile,
the semantic catalog reports missing and partial capabilities honestly, and
the operational reader is available for a later stabilization phase.

Runtime shadow collection and dogfood are **not** part of the current package
exit. The product surfaces are too unstable for live behavior to answer an
architecture-bearing question. The facade remains off and serves as an offline
conformance harness until the whole-product and surface stability gates in
`whole-product-v1-conformance-workbook-2026-08-29.md` pass.

It is **not** complete only when the facade is allowed to enforce. Read cutover,
proposal/commit cutover, contribution enforcement, client entry changes, and
legacy-tool retirement are separate packages with their own approval gates.

---

## 1. Why this is a facade, not a replacement runtime

The current system already contains mature execution machinery:

- canonical pending-turn admission and message persistence;
- a rich turn loader and context compiler;
- deterministic eligibility plus contextual capability retrieval;
- a canonical `TurnPlan`;
- provider-neutral action envelopes;
- system-owned authority evidence;
- durable workflows, idempotency, postconditions, and receipts;
- conversation, Trip/itinerary, place, provider, Experience Graph, relationship,
  and Intake owner gateways at different levels of maturity; and
- content-free shadow telemetry patterns with operational readouts.

The mismatch is primarily semantic:

- entry is reduced into prompt prose rather than retained as a typed turn
  contract;
- `TurnIntent` is still `INTAKE | CONVERSATION | PROACTIVE`;
- the model-visible vocabulary is dominated by itinerary, presentation-card,
  and internal maintenance tools;
- contribution authority is fragmented across Admission, prompts, handler
  policies, and memory/observation writers;
- target owners such as general Life, Opening, and monitoring are incomplete;
  and
- Chat can act across systems, but the runtime does not yet describe those
  actions through the post-pivot product grammar.

Replacing the runtime would discard strong machinery and multiply risk.
Changing the prompt first would make the model speak the new worldview while it
still operates the old one. Adding target tools first would make owner and
authority gaps executable before we understand them.

The facade makes the current and target systems comparable:

```text
mobile/source event
        │
        ├── current path ──> Admission / prompt context / tool eligibility
        │                         │
        │                         └──> TurnPlan ──> model loop
        │                                           │
        │                                           └──> ActionEnvelope
        │                                                   │
        │                                                   └──> owner handler
        │                                                           │
        │                                                           └──> receipt
        │
        └── shadow facade
              │
              ├── normalize entry and resolved owner references
              ├── resolve contribution policy
              ├── compile human job, phase, agency ceiling, and return
              ├── select target semantic operations
              └── compare target frame with current plan/actions/receipts
                                      │
                                      └──> content-free quality event
```

Only the upper path serves the user during this package.

---

## 2. Research findings that change the earlier proposal

The repository audit supports the facade direction, but it changes several
details from the initial target-architecture sketch.

### 2.1 Do not create a second generic resource reference

`backend/core/models/execution_contract.py` already defines `ResourceRef` with:

- owner `kind`;
- stable `id`;
- optional `revision`; and
- required app or guide `canonical_path`.

That is already the right contract for a **server-resolved canonical owner**.
Creating another generalized `ResourceRefV2` would introduce an avoidable
migration and eventually require a third convergence.

The missing type is narrower: an untrusted or unresolved identity hint from a
client seed. Call that `ResourceLocator`.

The invariant is:

```text
ResourceLocator = “the caller indicated this object”
ResourceRef     = “the server resolved an authorized canonical owner”
```

A locator must never acquire a canonical path, revision, authority, or mutation
eligibility merely because the client supplied an ID.

### 2.2 Do not replace Admission

`AdmissionEnvelope` and `AdmissionResult` already provide retry-stable source
custody, immediate-job, retention, correction, and consequence fields.

Admission is narrower than the full contribution contract, but that is a
feature: it is the custody boundary for an inbound source. The contribution
resolver should consume Admission plus current instruction, channel, source,
owner, and authority evidence. It should not redefine ingestion.

`requested_retention` is evidence of a request, not final system authority. The
server-owned contribution decision remains the authority.

### 2.3 Do not merge the two receipt layers yet

The codebase has two legitimate levels:

- `ActionEnvelope` and `ExecutionReceipt` describe a model tool-call attempt in
  the Concierge control plane;
- `CommandEnvelope` and `ActionReceipt` describe a canonical owner command and
  its viewer-safe durable result.

One model tool call may invoke a canonical command, but those identities are
not interchangeable. The first package should observe and correlate both. A
later owner adapter can project the canonical command/receipt into the semantic
result.

### 2.4 Do not create another ambiguous capability catalog

`backend/concierge/capability_catalog.py` already governs the reviewed bundles
behind current model-visible tools. The new facade should therefore use:

```text
backend/concierge/agentic_facade/semantic_catalog.py
```

That catalog describes target semantic operations and their compatibility with
current capabilities. It does not become a second serving registry.

### 2.5 Keep the public API unchanged first

The mobile `ConversationSeed`, composer attachments, Admission metadata, and
authenticated conversation scope already contain enough information to compile
an internal `InteractionEntry` in shadow.

The first version should therefore be internal. Once shadow data shows which
entry and return fields are stable and actually useful, expose a reviewed
public version through OpenAPI and regenerate mobile types. This avoids
codifying an untested entry ontology in the client contract.

### 2.6 Four product roots and seven origin families are different concepts

The product has four root surfaces:

```text
Home | Chat | Places | Life
```

Turns can still originate from a Plan, Occasion, notification/push, or legacy
surface. Those are origin families or owner contexts, not additional permanent
tabs.

The facade must therefore keep both:

- `product_root`: `home | chat | places | life | unknown`;
- `origin_surface`: `chat | home | places | life | plan | occasion | push | legacy`.

This avoids accidentally rebuilding the old Trip tab in the control plane.

### 2.7 The existing tool baseline is currently red

Before adding new shadow comparisons, the current provider surface must be made
trustworthy again.

The focused baseline test currently reports:

| Surface | Reviewed | Current | Difference |
| --- | ---: | ---: | ---: |
| full | 74 tools / 113,264 B | 73 / 112,664 B | -1 tool / -600 B |
| first turn | 2 / 6,992 B | 2 / 6,992 B | exact |
| planning read | 32 / 66,229 B | 32 / 66,305 B | +76 B |
| planning edit | 43 / 74,612 B | 43 / 74,688 B | +76 B |
| during trip | 31 / 64,892 B | 31 / 64,968 B | +76 B |
| post trip | 21 / 46,425 B | 21 / 46,425 B | exact |

The history explains the drift:

- `d4fca6c37` removed `post_atlas_draft` from the registry and provider schema
  on August 13 without updating the reviewed snapshot;
- `44ae57023` added proposal copy limits and edited schema descriptions on
  August 14; and
- `1eb60ceba` tightened group-safe proposal rationale schema copy on August 14.

The latter two account for the +76-byte change on surfaces that include
`propose_change`.

This is not a facade bug. It is a prerequisite. PR 0 must explicitly explain
and reconcile these accepted changes before any new target-versus-current
metric is trusted.

---

## 3. Package architecture

### 3.1 Modules

The package should introduce this bounded structure:

```text
travel-agent/backend/core/models/contribution.py
travel-agent/backend/core/contribution_policy.py
travel-agent/backend/core/models/agentic_turn.py

travel-agent/backend/concierge/agentic_facade/
├── __init__.py
├── entry_adapter.py
├── compiler.py
├── semantic_catalog.py
├── selector.py
├── comparison.py
├── shadow.py
└── operational_evidence.py

travel-agent/scripts/agentic_facade_shadow_report.py

travel-agent/tests/core/
├── test_contribution_policy.py
└── test_agentic_turn_contract.py

travel-agent/tests/concierge/
├── fixtures/agentic_turn_portfolio.json
├── test_agentic_entry_adapter.py
├── test_agentic_turn_compiler.py
├── test_agentic_semantic_catalog.py
├── test_agentic_semantic_selector.py
├── test_agentic_facade_comparison.py
├── test_agentic_facade_shadow.py
└── test_agentic_facade_operational_evidence.py
```

If the generic lexical ranker is extracted, keep that in its own prerequisite
PR:

```text
travel-agent/backend/core/lexical_capability_ranking.py
travel-agent/tests/core/test_lexical_capability_ranking.py
```

No file in the facade may import provider SDK types, call an LLM, query a
database, or invoke an owner handler.

### 3.2 Layer ownership

| Layer | Owns | Must not own |
| --- | --- | --- |
| core contribution contract | five axes, tier, scope, decision, receipt shape | prompt, mobile surface names, tool names |
| contribution policy | deterministic authorization/treatment resolution | semantic interpretation by model, owner mutation |
| entry adapter | normalization and authorized ref resolution inputs | product consequence, prompt rendering |
| turn compiler | target semantic frame | execution, persistence, provider schemas |
| semantic catalog | target operations and compatibility truth | current serving selection |
| selector | structured eligibility and bounded relevance | authority elevation |
| comparison | target/current mismatch codes | user-facing judgment or copy |
| shadow sink | bounded event scheduling | turn latency, content retention |
| operational evidence | scalar aggregation and readiness | raw metrics JSON, prompts, IDs |

---

## 4. Contract design

All new contracts should be strict, frozen, and versioned. Enum values are
lowercase stable API-like tokens even while the contracts remain internal.

### 4.1 `ResourceLocator`

`ResourceLocator` belongs in `backend/core/models/agentic_turn.py` because it is
an entry-normalization type, not an execution contract.

Proposed fields:

```python
class ResourceLocator(StrictFrozenModel):
    locator_version: Literal["resource-locator-v1"]
    kind: ResourceKind
    external_id: str | None
    slug: str | None
    parent_ids: tuple[LocatorParent, ...]
    source: Literal["conversation_seed", "attachment", "admission", "structured_action"]
```

Rules:

- at least one identity field must exist;
- no canonical path or revision is accepted from the client;
- values are never traced;
- authorization failure, invalidity, and absence have different bounded reason
  codes; and
- a failed locator remains unresolved rather than being coerced into a
  `ResourceRef`.

### 4.2 Contribution contracts

`backend/core/models/contribution.py` should implement the already documented
contract rather than invent a Chat-specific memory policy.

#### Gesture

```text
ask | point | bring | keep | share | decide | act | correct
```

`Import`, `Address`, `Invite`, `Release`, `Monitor`, and `Contribute` can remain
adapter labels that normalize into these stable gestures plus axis values. Do
not grow the primary enum for every UI verb.

#### Five axes

```text
use:       none | current_job | named_purpose
retention: none | source_bound | durable_private | named_shared
inference: none | current_job | source_bound | admitted_learning
audience:  private | named_people | occasion | public
action:    advise | prepare | propose | commit | mandate
```

#### Treatment tier

```text
T0 = answer or prepare privately; no durable consequence
T1 = narrow private apply, then compact receipt/correction
T2 = exact preview at a material boundary
```

The tier is a user-treatment policy, not a replacement for
`AgencyLevel`, `ToolEffect`, `AuthorityRequirement`, or execution class.

#### Candidate and decision

The candidate carries proposed semantics and source provenance. The decision
contains only system-owned allowed semantics:

```python
class ContributionDecision(StrictFrozenModel):
    contract_version: Literal["contribution-decision-v1"]
    gesture: ContributionGesture
    axes: ContributionAxes
    treatment: ContributionAuthorityTier
    scope: ContributionScope
    owner_kind: str | None
    reason_codes: tuple[ContributionReason, ...]
    required_preview: bool
    correction_path: str | None
    expires_at: datetime | None
```

The model may propose a `ContributionCandidate`. It may never construct or
modify a `ContributionDecision`.

### 4.3 Internal `InteractionEntry`

This is a compiled server-owned view, not a new public request body.

```python
class InteractionEntry(StrictFrozenModel):
    contract_version: Literal["interaction-entry-shadow-v1"]
    product_root: ProductRoot
    origin_surface: OriginSurface
    locators: tuple[ResourceLocator, ...]
    resource_refs: tuple[ResourceRef, ...]
    unresolved: tuple[UnresolvedLocator, ...]
    selection: SelectionRef | None
    audience: InteractionAudience
    return_contract: ReturnContract
```

`SelectionRef` means the user explicitly selected one or more already-visible
objects. It is not permission to mutate them.

### 4.4 Human job and operation phase

Use the vocabulary already fixed by the cross-surface fixture pack:

```text
human job:
understand | compare | explore | shape | coordinate | operate | monitor | repair

operation phase:
inspect | compose | propose | commit | monitor | reconcile
```

Several phases may be eligible. The frame still declares one primary job and
one maximum terminal phase.

### 4.5 `AgenticTurnFrame`

The shadow frame is a target-semantic projection of an existing `TurnPlan`, not
a permanent parallel control plane.

```python
class AgenticTurnFrame(StrictFrozenModel):
    schema_version: Literal["agentic-turn-shadow-v1"]
    policy_version: Literal["contribution-policy-v1"]
    catalog_version: Literal["semantic-catalog-v1"]
    turn_id: UUID
    entry: InteractionEntry
    immediate_job: AgenticJob
    contribution: ContributionDecision
    context_scope: ContextScopeManifest
    phases: tuple[OperationPhase, ...]
    terminal_phase: OperationPhase
    agency_ceiling: AgencyLevel
    capability_ids: tuple[str, ...]
    target_owner_kinds: tuple[str, ...]
    expected_postcondition_kinds: tuple[str, ...]
    response: ResponseContract
    residue: ResidueContract
```

Important boundaries:

- the frame can narrow or flag current authority but never raise it;
- owner kinds are safe to trace; owner IDs are not;
- context scope lists admitted packet keys and source families, never values;
- capability IDs are reviewed constants, never model-generated strings;
- response declares medium/projection/destination semantics, not presentation
  copy; and
- residue declares whether anything may persist or resurface, not whether a
  legacy background writer happened to run.

### 4.6 Response and return

The response contract should preserve the fixture grammar:

```text
primary projection: none | artifact | instrument | direct_state
lead medium: evidence | sequence | comparison | spatial | prose | instrument
return behavior: stay | update_origin | open_owner | continue_monitoring
```

The shadow default is `stay`, because current Chat does not consistently send a
typed return target. The compiler must not fabricate a route from a prompt
block. `update_origin` or `open_owner` requires either a resolved `ResourceRef`
or a typed server-issued return target.

### 4.7 Versioning policy

- schema versions change when serialized fields or enum meanings change;
- policy versions change when the same facts resolve to a different
  contribution decision or agency ceiling;
- catalog versions change when semantic operation meaning or compatibility
  status changes;
- telemetry always records all three;
- machine fixtures pin all three; and
- do not use `V2` as a synonym for “post-pivot.” Version only actual contracts.

---

## 5. Entry normalization

### 5.1 Source precedence

Normalize entry information in this order:

1. authenticated request and conversation scope;
2. server-issued structured action;
3. pending-turn `AdmissionEnvelope` and `AdmissionResult`;
4. validated composer context attachments;
5. validated `ConversationSeed` identity hints;
6. legacy metadata fallback; and
7. conservative Chat/unknown defaults.

Higher-precedence inputs do not erase lower-precedence provenance. They control
authority and resolution.

### 5.2 Current seed-to-origin mapping

| Current seed surface | Product root | Origin surface |
| --- | --- | --- |
| `home_card` | home | home |
| `venue`, `site`, `accommodation`, `place`, `places_map`, `dossier`, `angle`, `experience` | places | places |
| `trip_story`, `trip_feel`, `trip_debrief`, `me`, `atlas_search` | life | life or legacy for `atlas_search` |
| `trip_map`, `trip_block`, `plan` | life | plan |
| Experience Graph `occasion` entity | life | occasion |
| `notification` | derived from return target, else chat | push |
| `guide`, `generic`, missing | chat | chat |
| `discover` | places | legacy |

This is a compatibility map, not final information architecture. It makes the
four-root model explicit without pretending the old client has already
adopted it.

### 5.3 `AIRunSurface` compatibility

`AIRunSurface` currently supports `VESPER`, `TRIPS`, `PLACES`, and `LEGACY`.
Do not expand or reinterpret it in the first package. It is operational
execution telemetry used beyond the facade.

The shadow frame records product root and origin separately. A later telemetry
migration can add `HOME` and `LIFE` only after all AI entry points and dashboards
are audited.

### 5.4 Authorized resolution

The adapter should not repeat the existing prompt renderers. It should use or
extract the same owner authorization and resolution primitives underneath:

- place/venue/site/accommodation/dossier resolution;
- Trip membership guard;
- Experience Graph scope resolution;
- workbench freshness check;
- source/Intake custody lookup; and
- conversation and participant scope.

If a current resolver only returns Markdown, extract an internal typed resolver
and let the existing Markdown renderer consume it. Do not parse the Markdown
back into structured identity.

### 5.5 Unresolved reasons

Use a closed low-cardinality enum:

```text
missing_identity
invalid_identity
unsupported_kind
not_found
not_authorized
stale
conflicting_scope
legacy_only
resolver_failed
```

Only kind and reason are traceable. Never trace IDs, slugs, labels, paths, or
client context prose.

---

## 6. Contribution resolution

### 6.1 Policy precedence

The pure resolver follows the documented order:

1. current explicit instruction;
2. narrow standing mandate or setting;
3. current channel, Plan, or Occasion authority;
4. gesture default; and
5. conservative fallback.

### 6.2 Safe defaults

| Situation | Default decision |
| --- | --- |
| ordinary question | Ask, T0, current-job use, no retention, no inference, private, advise |
| explicit private observation | Point, at most T1 source-bound; no identity/preference inference |
| verified source given to the app | Bring, immediate use; at most source-bound T1 if custody is valid |
| “remember/keep this” with clear object | Keep, private T1 if reversible and non-sensitive |
| named share/invite | Share, T2 before audience boundary unless an exact server-issued confirmation already binds it |
| plan decision | Decide, propose or commit only within current authority and owner revision |
| provider/spend/public action | T2 and exact `AuthorityEvidence` |
| correction of a named relation | Correct, narrow repair; invalidate dependents and provide receipt |
| ambiguous semantics with no material consequence | deliver immediate value under T0 and retain nothing |
| ambiguity that changes truth, audience, spend, or irreversible consequence | one bounded clarification or exact preview |

### 6.3 Authority ceiling

The facade must derive an agency ceiling from the contribution decision and
current `ActionAuthorityResolver` evidence:

| Contribution action | Maximum agency without additional evidence |
| --- | --- |
| advise | respond |
| prepare | respond or propose, depending on owner |
| propose | propose |
| commit | commit only with current exact authority evidence |
| mandate | bounded by stored mandate, owner, parameters, expiry, and revision |

If the current `TurnPlan` permits a broader effect than the target ceiling, the
facade records a conflict. It does not block the turn during shadow.

If the current plan is narrower, that is a capability gap, not an authority
failure.

### 6.4 Admission compatibility

Map current Admission jobs conservatively:

| Admission job | Target job |
| --- | --- |
| `answer`, `decode`, `orient`, `clarify` | understand |
| `compare` | compare |
| `act`, `address` | operate or coordinate, bounded by authority |
| `preserve` | understand plus a Keep candidate; does not authorize retention alone |
| `reconcile` | repair |

Do not widen the public Admission enum in this package. The internal target job
can be more expressive while the compatibility map is evaluated.

---

## 7. Job compilation

Job compilation must be deterministic and explainable. It can consume a
model-proposed semantic candidate later, but the first package should use
structured evidence and existing narrow classifiers.

### 7.1 Precedence

1. exact structured action;
2. exact correction/undo/release action;
3. active monitor or monitoring request;
4. provider or owner commit request;
5. group coordination/audience consequence;
6. explicit selected-object comparison;
7. shaping/composition request;
8. grounded exploration request;
9. understand; and
10. conservative understand fallback.

### 7.2 Ambiguity rule

Ambiguity must never select a stronger consequence. It may select a weaker
human job and record `job_ambiguous`.

The facade should not ask the user to classify their input as Ask, Point, or
Bring merely to make the compiler happy. The product principle remains:
deliver immediate value first and ask only when an unresolved distinction
changes material truth or consequence.

### 7.3 Language relevance

The existing contextual retrieval module contains useful deterministic query
construction and BM25 ranking, but it is tied to the current tool registry.

If target semantic selection needs lexical relevance, extract only the pure
ranking primitives into `backend/core/lexical_capability_ranking.py` and prove
exact parity before the target selector uses them.

Do not duplicate the tokenizer, stop-word set, history weighting, or BM25
implementation inside the facade.

The extraction must preserve:

- current message weighting;
- terse retry handling;
- exclusion of assistant prose;
- stable sorting;
- relative score floor; and
- the current place-anchor and web-search policy ceilings in the legacy
  wrapper.

Structured eligibility always precedes lexical relevance.

---

## 8. Target semantic catalog

### 8.1 Purpose

The semantic catalog answers:

> If the post-pivot product were fully implemented, which owner operation would
> satisfy this human job, and how much of that operation can the current system
> truthfully provide?

It does not answer:

> Which JSON tool schema should be sent to the model on this turn?

That remains the current registry and selector until a later cutover.

### 8.2 Declaration

Each semantic operation should declare:

```python
class SemanticOperation(StrictFrozenModel):
    operation_id: str
    owner_kind: str
    effect: ToolEffect
    human_jobs: frozenset[AgenticJob]
    phases: frozenset[OperationPhase]
    accepted_origins: frozenset[OriginSurface]
    accepted_resource_kinds: frozenset[str]
    authority_boundary: AuthorityRequirement
    evidence_kinds: frozenset[str]
    postcondition_kinds: tuple[str, ...]
    return_modes: frozenset[ReturnMode]
    readiness: OperationReadiness
    compatibility_lane: CompatibilityLane
    legacy_capability_ids: tuple[str, ...]
    legacy_tool_names: tuple[str, ...]
    limitation_codes: tuple[str, ...]
```

Readiness:

```text
mapped | partial | unavailable
```

Compatibility lane:

```text
legacy_tool | runtime_context | owner_reader | missing
```

### 8.3 Initial read/compose catalog

The first catalog contains reads, analysis, composition, and status operations.
It may describe missing target commits, but it must not select them as
executable.

| Target operation | Owner | Current compatibility | Initial readiness |
| --- | --- | --- | --- |
| `conversation.history.search` | conversation | `conversation.history.read` bundle | mapped |
| `conversation.history.read_window` | conversation | current read window | mapped |
| `source.inspect` | Intake/Source | pending Admission plus multimodal ingestion/inspection paths | partial |
| `place.search` | place discovery | current venue/place/experience discovery capabilities | mapped |
| `place.read` | Place | place/venue/site detail and status readers | mapped/partial by kind |
| `place.compare` | Place | current comparisons and deterministic evidence | partial |
| `route.evaluate` | route/spatial | `check_distance`, route analysis, itinerary route optimization | mapped with Trip specialization |
| `plan.search` | Plan | account Trip find/similarity as compatibility | mapped with Trip specialization |
| `plan.read` | Plan | Trip snapshot and itinerary reads | mapped with Trip specialization |
| `plan.analyze` | Plan | conflicts, slots, route, feasibility | mapped with Trip specialization |
| `occasion.read` | Occasion | Experience Graph occasion/participation readers | partial |
| `commitment.read` | Commitment | itinerary blocks, booking/proposal projections | partial |
| `relationship.search` | Relationship | relationship handoff/context seams | partial |
| `life.search` | Life | fragmented Trip, Atlas, source, and outcome reads; no general owner | unavailable/partial |
| `life.read` | Life | fragmented projections, no canonical general read | unavailable/partial |
| `life.compare` | Life | no general semantic comparison owner | unavailable |
| `research.start` | Research | web, angle, journey research pathways | partial |
| `research.read` | Research | existing research artifacts/results | partial |
| `moment.read` | Moment/Situation | spatial situation, whereabouts, current conditions | partial |
| `opening.read` | Opening | Lived Experience and Experience Graph shadow projections | partial |
| `receipt.read` | execution owner | current execution and owner receipts | partial |

“Trip specialization” is not an error. It means the current owner is useful but
too narrow to be the permanent product noun.

### 8.4 Catalog invariants

Tests must prove:

- semantic operation IDs are unique and stable;
- every referenced current capability ID exists;
- every referenced legacy tool exists in `TOOL_REGISTRY`;
- a legacy tool maps to only one primary semantic operation unless an explicit
  reviewed multi-operation exception exists;
- presentation tools are not misclassified as semantic owner operations;
- maintenance tools are not misclassified as user value operations;
- every operation declares owner, effect, authority, evidence, postconditions,
  and return behavior;
- an unavailable operation has no executable adapter or fake tool binding;
- a partial operation declares limitation codes; and
- no target commit is served or dispatched by importing this module.

### 8.5 Presentation and maintenance tools

The comparison layer should classify current tools into:

```text
semantic_read
semantic_propose
semantic_commit
presentation
maintenance
ingestion
provider_operation
unknown
```

Examples such as posting cards or updating internal intent may remain necessary
for compatibility, but their presence must not inflate target semantic
coverage.

---

## 9. Compiler behavior

### 9.1 Pure inputs

The compiler receives already-loaded or structural information only:

- `TurnContext` structural fields and metadata;
- authenticated conversation type and IDs;
- optional current `Trip` scope;
- pending Admission envelope/result;
- typed entry-resolution result;
- redacted `LoadedTurnState.context_manifest()`;
- existing `TurnPlan`;
- currently selected tool names;
- exact structured action metadata, if any; and
- semantic catalog version.

The compiler itself receives no prompt blocks and performs no reads.

### 9.2 Compile stages

```text
1. normalize entry
2. resolve contribution candidate
3. apply deterministic contribution policy
4. derive primary human job
5. derive admitted context families and exclusions
6. derive candidate owner kinds
7. calculate agency ceiling
8. select eligible target semantic operations
9. derive phases and terminal phase
10. derive response projection, destination, return, and residue
11. validate cross-field invariants
12. emit frozen AgenticTurnFrame
```

### 9.3 Cross-field invariants

- `commit` phase requires a commit action axis and current authority evidence;
- `monitor` requires a monitor target, scope, expiry/stop condition, and
  notification policy candidate;
- `named_people`, `occasion`, or `public` audience cannot be paired with an
  implicit private-only source consequence;
- `open_owner` requires a resolved owner reference;
- `continue_monitoring` requires a durable monitor identity;
- `eligible_opening` residue requires admitted retention/inference authority;
- T0 cannot declare a durable owner mutation;
- T1 cannot widen audience;
- T2 declares the exact boundary needing preview or exact prior authority;
- unavailable capabilities are reportable but never executable; and
- a legacy Trip owner may satisfy a Plan operation only with an explicit
  specialization limitation.

### 9.4 Compiler failure

Compiler failure is always fail-open for the current turn.

The event should include only:

- failure stage;
- bounded reason code;
- schema/policy/catalog version; and
- compile duration.

Do not serialize exceptions, request metadata, IDs, or source values into the
quality event.

---

## 10. Twelve architecture fixtures

The current prose fixtures should become a machine-readable portfolio. They are
compiler conformance tests, not fabricated live-owner tests.

| ID | Primary pressure | Expected job family | Principal owners | Important architectural test |
| --- | --- | --- | --- | --- |
| A01 | shape Saturday with Maya from clean Chat | shape + coordinate | relationship, Plan/Occasion, Place | no Trip dependency; prepare before commit |
| A02 | “use this” on a flight ticket | understand/operate | Source, Commitment, Plan | immediate source value; attendance not inferred |
| A03 | make a Home Opening work for four | coordinate | Opening, Occasion, Relationship | Home-origin object remains in scope; group boundary explicit |
| A04 | compare selected Places and build easiest route | compare + shape | Place, route, Plan | selection survives Chat; reads before composition |
| A05 | correct a Life artifact | repair | Source, Life projection, dependents | repair relation, not ontology homework; invalidate projections |
| A06 | adapt a live evening when group is exhausted | operate | Moment, Plan, Occasion, Place | situated context; propose/commit boundary remains explicit |
| A07 | group-safe coordination | coordinate | Occasion, Relationship, group conversation | preserve private inputs, author, audience, plural outcomes |
| A08 | move dinner and tell the group | operate | Plan/Commitment, Occasion, conversation | exact action and audience authority; receipt/readback |
| A09 | “handle it” under mandate | operate | Commitment, provider, Plan | mandate is scoped, expiring, parameter-bound, and revocable |
| A10 | monitor flight for material change | monitor | Monitor, Commitment, provider evidence | missing general monitor owner is visible, not faked |
| A11 | explain why a Place appeared | understand | Opening, Place, evidence | causal evidence, no personality dossier |
| A12 | Rome episode into New York opening | explore/understand | Life, Place, Opening, Relationship | substantive new connection; past evidence opens future possibility |

For each fixture, pin:

- internal entry;
- contribution candidate and decision;
- human job;
- context scope;
- owner kinds;
- phases and terminal phase;
- agency ceiling;
- semantic operation IDs and readiness;
- response projection and medium;
- return behavior;
- residue; and
- expected compatibility/mismatch codes.

### 10.1 Fixture implementation

Store JSON, not YAML, because the contracts are strict Pydantic JSON models and
the repository already uses JSON fixtures for exact snapshots.

Each case should have:

```json
{
  "case_id": "A01",
  "inputs": { "...": "structural fixture only" },
  "expected_frame": { "...": "complete frozen frame" },
  "expected_legacy_comparison": { "...": "bounded codes" }
}
```

Do not place prose prompts, names, ticket details, or private context in the
runtime telemetry fixture. Synthetic text may exist in tests only where needed
to characterize deterministic classification.

### 10.2 Why not live LLM eval all twelve yet

Some target owners do not exist. An LLM eval cannot prove a nonexistent Life or
Monitor owner and would reward plausible prose over architecture.

When semantic reads actually become model-visible, add live Concierge evals
first for:

- A01 clean Chat shaping;
- A02 source inspection;
- A04 selected Place comparison/route; and
- A11 Opening/Place explanation.

Those are the highest-value read/compose cutover probes. Proposal and commit
fixtures follow only after owner adapters and authority gates exist.

---

## 11. Current-versus-target comparison

The comparison has a pre-turn and post-turn half.

### 11.1 Pre-turn comparison

Compare target frame with:

- current `TurnIntent`;
- current agency level and permitted effects;
- selected legacy tool count;
- selected current capability IDs;
- selected presentation and maintenance tool counts;
- required-Trip tool count;
- target semantic operation readiness; and
- unresolved owner kinds.

A commit tool being available to the model is not itself proof that a commit
occurred. Record exposure separately from execution.

### 11.2 Post-turn comparison

Compare with actual:

- `ActionEnvelope` count and effects;
- authority requirement/evidence presence;
- `ExecutionReceipt` status and verification;
- canonical command/receipt correlations where available;
- user-authored ingestion calls;
- model-managed memory/observation calls;
- presentation/maintenance calls;
- provider calls;
- changed object kinds;
- owner readback availability; and
- final continuation/return metadata, if present.

### 11.3 Initial conflict codes

```text
first_turn_intake_mismatch
job_ambiguous
owner_unresolved
capability_unavailable
trip_specialization
legacy_presentation_exposed
legacy_maintenance_exposed
legacy_presentation_called
legacy_maintenance_called
durable_write_without_contribution_grant
action_depth_exceeds_ceiling
unclassified_actual_commit
authority_evidence_missing
group_egress_not_structural
return_target_missing
owner_readback_missing
monitor_owner_missing
model_memory_write_observed
```

The codes must distinguish expected compatibility limitations from safety
conflicts. `trip_specialization`, for example, is useful migration evidence,
not automatically a defect.

---

## 12. Runtime wiring

### 12.1 Flag

Add one source of truth to `backend/concierge/config.py`:

```python
agentic_facade_mode: Literal["off", "shadow"] = Field(
    default="off",
    validation_alias="CONCIERGE_AGENTIC_FACADE_MODE",
)
```

Do not add `enforce` in this package. Do not mirror the same flag in
`backend/core/feature_flags.py`.

### 12.2 Compile seam

The narrowest integration seam is immediately after:

```python
selected_tools, turn_plan = _select_tools_and_build_turn_plan(...)
```

At that point the runtime has:

- loaded context and redacted manifest;
- entry metadata;
- current model route;
- selected current surface; and
- canonical current `TurnPlan`.

Pseudocode:

```python
facade_observation = None
if concierge_settings.agentic_facade_mode == "shadow":
    facade_observation = compile_agentic_facade_shadow(
        turn=turn,
        conversation=conversation,
        pending_admission=loaded.pending_intake,
        context_manifest=loaded.context_manifest(),
        turn_plan=turn_plan,
        selected_tool_names=tuple(tool["name"] for tool in selected_tools),
    )
```

`compile_agentic_facade_shadow` must be synchronous, pure, bounded, and catch
all internal errors into a failure observation.

### 12.3 Final comparison seam

Pass the content-free observation into `_finalize_turn_observability`. After
the current control-plane trace is recorded, compare it with:

```python
loop_result.action_envelopes
loop_result.execution_receipts
loop_result.tool_calls
```

Schedule exactly one best-effort event per turn.

### 12.4 Inertness requirements

With the flag `off`:

- compiler imports do not occur on the hot path if avoidable;
- no facade object is built;
- no event is scheduled; and
- provider request, selected tools, reply, actions, receipts, and timings are
  unchanged.

With the flag `shadow`:

- provider request and selected tool schemas remain byte-identical;
- prompt and messages remain identical;
- no new DB, network, LLM, embedding, or owner read occurs;
- compilation failure cannot change the reply or terminal delivery;
- event scheduling cannot block the turn; and
- the event contains no source text, prompt text, tool parameters, result
  payloads, names, labels, IDs, slugs, paths, or coordinates.

---

## 13. Telemetry contract

### 13.1 Event

Reuse `ai_quality_events`:

```text
check_type = agentic_facade_shadow
outcome    = observed | failed
origin     = production | dogfood
latency_ms = pure compile + comparison time
```

No schema migration is required.

### 13.2 Allowed metrics

#### Version and entry

- schema version;
- contribution policy version;
- catalog version;
- product root;
- origin surface;
- audience category;
- locator count bucket;
- resolved owner-kind counts;
- unresolved kind count and reason counts; and
- selection present.

#### Target semantics

- primary job;
- gesture;
- T0/T1/T2;
- five axis enum values;
- owner kinds;
- phases and terminal phase;
- agency ceiling;
- target semantic operation IDs;
- mapped/partial/unavailable counts;
- response projection;
- lead medium;
- return mode; and
- residue mode.

#### Current plan and execution

- current intent;
- current agency level;
- first-turn flag;
- selected current tool count;
- current capability count;
- Trip-required, presentation, and maintenance counts;
- executed read/propose/commit counts;
- ingestion/provider/presentation/maintenance call counts;
- model-managed memory-write count;
- receipt success/failure/pending counts;
- verification passed/failed/not-run counts; and
- owner readback available/pending/degraded counts where correlated.

#### Comparison and performance

- conflict/reason code counts;
- compiler stage on failure;
- compile duration bucket;
- comparison duration bucket; and
- total duration in `latency_ms`.

### 13.3 Forbidden metrics

- message or prompt text;
- generated reply text;
- attachment name, MIME-derived user label, or raw source content;
- user, conversation, Trip, source, place, resource, action, or receipt ID in
  `metrics`;
- canonical path or return URI;
- tool inputs or outputs;
- context values;
- inferred traits or preference labels;
- place names or coordinates;
- participant names; and
- raw exceptions.

The table may continue to use its existing relational actor/conversation/Trip
columns for scoped operational joins. Those IDs must not be copied into the
JSON metrics payload.

### 13.4 Trace policy

The full `AgenticTurnFrame` contains IDs and is not safe to stamp wholesale
onto Langfuse metadata. Add only the same bounded projection used by the event.

---

## 14. Operational evidence

### 14.1 Reader

`operational_evidence.py` should follow the context-compiler shadow pattern:

- issue one SQL query with an explicit scalar JSON projection;
- never select complete `metrics` JSON;
- whitelist origins and enum values;
- bound all counts and timings;
- aggregate unknown values separately; and
- return a strict frozen readout.

### 14.2 Dormant CLI

```bash
./.venv/bin/python scripts/agentic_facade_shadow_report.py \
  --window-days 14 \
  --origin dogfood
```

Output sections:

1. sample/failure/latency health;
2. product-root and origin coverage;
3. job and contribution-treatment distribution;
4. semantic operation readiness;
5. current compatibility lanes;
6. authority and execution conflicts;
7. unresolved owner/resource reasons;
8. first-turn and Trip-specialization pressure;
9. return/monitor gaps; and
10. verdict with exact reasons.

The CLI is retained for the later stabilized-surface phase. It should not be
run as evidence for the current product definition or used to manufacture a
dogfood sample from legacy/unstable surfaces.

### 14.3 Current offline package readiness gates

These gates mean “safe and useful offline architecture substrate,” not “ready
to enable shadow or enforce”:

| Gate | Threshold |
| --- | --- |
| compiler fixtures | 12/12 exact |
| contribution fixture core subset | all selected T0/T1/T2 cases exact |
| compiler failure | 0 in deterministic fixtures and tests |
| privacy/authority broadening | 0 |
| unclassified actual commits | 0 |
| actual commit correlation | 100% have action envelope and receipt; canonical owner correlation reported where available |
| hot-path I/O | 0 calls |
| pure compile p95 | <= 5 ms |
| measurable TTFT regression | not applicable while facade remains off; benchmark remains available |
| live sample | deliberately deferred until four-root surface stability |
| tool-serving parity | exact with facade off; shadow parity remains test-only |
| baseline health | provider tool baseline and manifest green |

Semantic mapping coverage is not required to reach 100%. Known missing owners
are the point of the measurement. The report must distinguish “missing owner”
from “compiler failed.”

---

## 15. Detailed PR sequence

Each PR should be reviewable and revertible on its own. No PR changes both
semantic policy and served behavior.

### PR 0 — Repair the current provider-surface baseline

**Purpose:** restore confidence in the current comparison oracle.

Files:

- `tests/concierge/test_tool_surface_baseline.py`;
- `tests/concierge/fixtures/tool_surface_baseline.json`;
- optional new `tests/concierge/fixtures/tool_surface_manifest.json`; and
- optional read-only manifest generator under `scripts/`.

Work:

1. document the August 13 removal of `post_atlas_draft`;
2. document the August 14 `propose_change` schema-copy and `maxLength` changes;
3. update the aggregate snapshot only after explaining each delta;
4. add stable ordered tool names and per-tool schema digests or byte sizes so a
   removed tool cannot hide behind aggregate byte growth elsewhere; and
5. keep re-baselining an explicit review action.

Acceptance:

- aggregate and exact-name/digest gates pass;
- current registry and `ALL_TOOLS` remain identical;
- no provider schema changes are introduced by the PR; and
- no production code behavior changes.

Estimated solo-founder size: **0.5 day**.

### PR 1 — Core contribution and agentic-turn contracts

**Purpose:** make the product grammar executable without wiring it to Chat.

Files:

- `backend/core/models/contribution.py`;
- `backend/core/contribution_policy.py`;
- `backend/core/models/agentic_turn.py`;
- `tests/core/test_contribution_policy.py`;
- `tests/core/test_agentic_turn_contract.py`; and
- a focused subset of synthetic contribution fixtures.

Work:

1. implement strict frozen enums and models;
2. implement pure policy precedence and conservative defaults;
3. map Admission fields into contribution candidates;
4. calculate treatment and agency ceiling without importing Concierge;
5. validate cross-field invariants; and
6. prove the model/candidate can never raise authority.

Acceptance:

- no database, provider, prompt, route, or mobile imports;
- deterministic serialization;
- invalid T0/T1/T2 combinations are rejected;
- current authority evidence remains the commit gate; and
- all policy tests pass offline.

Estimated size: **1–2 days**.

### PR 2 — Entry adapter, compiler, and A01–A12 portfolio

**Purpose:** compile current structural inputs into the target semantic frame.

Files:

- `backend/concierge/agentic_facade/__init__.py`;
- `backend/concierge/agentic_facade/entry_adapter.py`;
- `backend/concierge/agentic_facade/compiler.py`;
- `tests/concierge/fixtures/agentic_turn_portfolio.json`;
- `tests/concierge/test_agentic_entry_adapter.py`; and
- `tests/concierge/test_agentic_turn_compiler.py`.

Work:

1. normalize every current `ConversationSeed` surface and entity kind;
2. normalize every `ComposerContextAttachment` kind;
3. adapt pending Admission and structured actions;
4. distinguish locators from resolved `ResourceRef`s;
5. compile all twelve architecture fixtures exactly;
6. expose unresolved and specialization reasons; and
7. keep the compiler callable only from tests at this stage.

Acceptance:

- 12/12 exact frames;
- every current seed/attachment kind covered;
- unauthorized or failed resolution never creates a `ResourceRef`;
- no prompt-block parsing;
- no runtime wiring; and
- no fake owner path for Life, Opening, or monitoring.

Estimated size: **1.5–2 days**.

### PR 3A — Extract provider-neutral lexical ranking with parity

**Purpose:** avoid duplicating relevance infrastructure.

This PR is required only if structured selection alone leaves the live shadow
too often at generic `understand`.

Files:

- `backend/core/lexical_capability_ranking.py`;
- minimal adaptation of `backend/concierge/contextual_tool_retrieval.py`;
- `tests/core/test_lexical_capability_ranking.py`; and
- existing contextual-retrieval tests.

Work:

1. extract tokenizer and BM25 primitives;
2. retain Concierge-specific query history and policy ceilings in the wrapper;
3. compare every current test query before/after;
4. compare current ordering on all 41 Concierge YAML eval messages; and
5. prove selected tool names and order remain exact.

Acceptance:

- byte-identical provider schemas;
- exact current selection ordering;
- exact trace projection except for intentionally documented internal version;
- no target semantic behavior yet.

Estimated size: **1–1.5 days**.

### PR 3B — Semantic catalog and selector

**Purpose:** map target jobs/owners to reviewed semantic operations without
serving them.

Files:

- `backend/concierge/agentic_facade/semantic_catalog.py`;
- `backend/concierge/agentic_facade/selector.py`;
- `tests/concierge/test_agentic_semantic_catalog.py`; and
- `tests/concierge/test_agentic_semantic_selector.py`.

Work:

1. declare the initial read/compose catalog;
2. add compatibility mappings to current capability IDs/tool names;
3. mark mapped, partial, and unavailable truthfully;
4. implement structured eligibility before optional lexical relevance;
5. compile target selections for A01–A12; and
6. add catalog drift/invariant tests against `TOOL_REGISTRY`.

Acceptance:

- unavailable operations have no handler;
- current registry is not mutated;
- target operations are not converted to provider schemas;
- current tool serving remains exact; and
- fixture selection is stable and explainable.

Estimated size: **1–2 days**, plus PR 3A if required.

### PR 4 — Dark runtime wiring and comparison telemetry

**Purpose:** observe the real mismatch without changing user behavior.

Files:

- `backend/concierge/config.py`;
- `backend/concierge/agentic_facade/comparison.py`;
- `backend/concierge/agentic_facade/shadow.py`;
- small reviewed edits in `backend/concierge/agent.py`;
- `tests/concierge/test_agentic_facade_comparison.py`; and
- `tests/concierge/test_agentic_facade_shadow.py`.

Work:

1. add `off | shadow`, default `off`;
2. compile after the current turn plan;
3. compare after current actions/receipts exist;
4. emit one content-free event;
5. test failure isolation and scheduling failure; and
6. prove serving parity with the flag both ways.

Acceptance:

- no provider request/prompt/tool diff;
- no I/O in compile/compare;
- no user-visible output diff;
- all compiler errors fail open;
- strict forbidden-field telemetry tests pass;
- compile p95 in benchmark <= 5 ms; and
- current full agent characterization suite passes.

Estimated size: **1.5–2 days**.

### PR 5 — Operational readout, dormant until surface stability

**Purpose:** make later evidence actionable without making live observation a
current product gate.

Files:

- `backend/concierge/agentic_facade/operational_evidence.py`;
- `scripts/agentic_facade_shadow_report.py`;
- `tests/concierge/test_agentic_facade_operational_evidence.py`; and
- an appended signed observation section in this document or a dated status
  artifact.

Work:

1. implement scalar-only SQL projection;
2. implement aggregation and verdict reasons;
3. keep the runtime mode off;
4. verify the reader against synthetic bounded telemetry fixtures;
5. use the whole-product conformance workbook—not live sample frequency—to
   choose the next owner/read-adapter package; and
6. retain the CLI for a later explicit surface-stability decision.

Acceptance:

- no full JSON or prose reads;
- thresholds computed deterministically;
- report calls out missing owners rather than averaging them away;
- zero authority broadening/unclassified commits; and
- founder signs any future runtime-observation package explicitly.

Estimated engineering size: **1 day**. Observation is outside this package.

### Total package size

Approximately **6.5–10 founder-days**, depending on whether lexical extraction
is needed and how much typed owner-resolution logic must be extracted from the
current Markdown entry resolvers.

This is deliberately larger than one feature slice because it is
architecture-bearing. It remains bounded because it does not implement owners,
tools, UI, prompts, or serving cutover.

---

## 16. Test and verification matrix

### 16.1 Contract tests

- strict extra-field rejection;
- stable JSON serialization;
- enum exhaustiveness;
- cross-field invariants;
- version pinning;
- locator/ref distinction;
- contribution candidate cannot masquerade as decision; and
- no model/provider dependencies.

### 16.2 Policy tests

- explicit instruction beats standing mandate;
- standing mandate is owner/parameter/expiry bounded;
- private source-bound Bring can become T1;
- plain Ask is T0;
- audience, provider, spend, public, sensitive inference, and weak reversal
  become T2;
- correction is narrow and invalidates dependents;
- ambiguous non-material input remains T0;
- ambiguous material input cannot commit; and
- agency ceiling never exceeds current authority.

### 16.3 Adapter tests

- every mobile seed surface;
- every seed entity kind;
- every context attachment kind;
- duplicate seed/attachment de-duplication;
- Admission precedence;
- structured action precedence;
- Trip membership denial;
- Place and Experience Graph authorization;
- stale workbench reference;
- unknown/legacy source;
- safe fallback; and
- no IDs in trace projection.

### 16.4 Compiler tests

- A01–A12 exact;
- every job;
- every phase;
- every return mode;
- T0/T1/T2;
- missing Life owner;
- missing Monitor owner;
- Trip specialization;
- group-safe scope;
- no return target fabrication; and
- deterministic ordering of refs, owners, and capabilities.

### 16.5 Catalog/selector tests

- current capability and tool references exist;
- no duplicate operation IDs;
- no undocumented multi-map;
- partial operation has limitations;
- unavailable operation has no handler;
- presentation/maintenance excluded from semantic coverage;
- structured eligibility precedes relevance;
- assistant prose cannot steer retrieval; and
- all current retrieval behavior remains exact if ranker extraction occurs.

### 16.6 Shadow tests

- mode off is inert;
- shadow produces no provider request diff;
- compiler exception does not fail turn;
- event scheduling exception does not fail turn;
- one event per turn;
- forbidden content keys and values rejected;
- all metrics low-cardinality;
- actual calls classified separately from selected tools;
- authority conflict detection;
- receipt correlation;
- no event in test origin under existing sink behavior; and
- latency benchmark.

### 16.7 Existing regression suites

At minimum run:

```bash
cd /Users/feihuyan/travel-workspace/travel-agent

./.venv/bin/pytest -q tests/core/test_control_plane.py
./.venv/bin/pytest -q tests/core/test_action_receipts.py
./.venv/bin/pytest -q tests/concierge/test_tool_registry.py
./.venv/bin/pytest -q tests/concierge/test_tool_surface_baseline.py
./.venv/bin/pytest -q tests/concierge/test_contextual_tool_retrieval.py
./.venv/bin/pytest -q tests/concierge/test_tool_eligibility.py
./.venv/bin/pytest -q tests/concierge/test_action_authority.py
./.venv/bin/pytest -q tests/core/test_agent_loop_control_plane.py
./.venv/bin/pytest -q tests/test_agent_loop.py
./.venv/bin/pytest -q tests/api/test_message_flow.py

./.venv/bin/ruff check \
  backend/core/models/contribution.py \
  backend/core/contribution_policy.py \
  backend/core/models/agentic_turn.py \
  backend/concierge/agentic_facade \
  tests/core/test_contribution_policy.py \
  tests/core/test_agentic_turn_contract.py \
  tests/concierge/test_agentic_*.py

./.venv/bin/ruff format --check \
  backend/core/models/contribution.py \
  backend/core/contribution_policy.py \
  backend/core/models/agentic_turn.py \
  backend/concierge/agentic_facade \
  tests/core/test_contribution_policy.py \
  tests/core/test_agentic_turn_contract.py \
  tests/concierge/test_agentic_*.py
```

Use actual repository test filenames when implementation begins; if a listed
characterization file has since been split, preserve equivalent coverage.

### 16.8 No frontend contract work in this package

Because the first facade is internal, do not run OpenAPI generation merely to
create churn.

If a later package exposes typed entry/return fields:

1. update backend models/routes/tests;
2. run workspace `make sync-types`;
3. review `docs/openapi.json` and `docs/openapi.app.json`;
4. review `travel-app/utils/api/schema.gen.ts`;
5. run frontend typecheck and Chat tests; and
6. certify compatibility with older clients.

---

## 17. Rollback and failure handling

### 17.1 Runtime rollback

Set:

```text
CONCIERGE_AGENTIC_FACADE_MODE=off
```

Because the facade owns no writes and changes no serving behavior, rollback is
immediate and requires no data repair.

### 17.2 Contract rollback

Contracts are additive and internal. Reverting them does not invalidate
canonical owner data. Quality events remain inert historical telemetry keyed by
their schema/policy/catalog versions.

### 17.3 Telemetry failure

- compile failure produces a bounded failed observation;
- sink failure logs operationally and ends;
- no retry runs on the user path;
- no backlog or durable workflow is created for shadow telemetry; and
- a broken readout cannot affect Chat.

### 17.4 Unexpected authority finding

If shadow finds a durable write beyond the calculated ceiling:

1. do not flip the facade to enforcement;
2. classify whether the target policy is wrong or the current path is
   under-governed;
3. inspect the existing action/receipt and owner gateway;
4. fix the current authority seam in its own security/behavior PR if needed;
5. add a regression fixture; and
6. continue shadow only after the discrepancy is explained.

---

## 18. Principal risks and mitigations

### Risk 1 — building a second control plane

**Mitigation:** the facade is a projection of current `TurnPlan` plus product
semantics. It cannot dispatch. Its long-term destination is to enrich/replace
fields in the canonical plan after cutover, not coexist forever.

### Risk 2 — creating parallel nouns

**Mitigation:** reuse `ResourceRef`, Admission, current action/receipt types, and
owner gateways. Add only the unresolved locator and missing semantic contracts.

### Risk 3 — shadow data that cannot drive a decision

**Mitigation:** ship the operator readout in the same package and define the
next cutover decision in advance.

### Risk 4 — lexical classification masquerading as authority

**Mitigation:** language may rank read/compose candidates. It cannot raise
contribution tier, audience, agency, or effect.

### Risk 5 — false coverage from legacy presentation tools

**Mitigation:** classify presentation and maintenance separately and never
count them as semantic operations.

### Risk 6 — false coverage from Trip specialization

**Mitigation:** retain useful Trip/itinerary adapters but always emit the
specialization limitation until a general Plan/Life owner exists.

### Risk 7 — privacy leakage through observability

**Mitigation:** strict telemetry model, forbidden-field tests, no complete
frame in traces, scalar-only readout, no raw metrics JSON query.

### Risk 8 — hot-path latency

**Mitigation:** pure bounded structures, no I/O/model calls, default off, p95
compile gate, asynchronous best-effort sink.

### Risk 9 — expanding scope into UI or prompt work

**Mitigation:** explicit non-goals and PR boundaries. The package ends at
evidence collection.

### Risk 10 — treating all missing owners as equally urgent

**Mitigation:** use frequency, product value, fixture criticality, and current
compatibility to rank the next adapter package.

---

## 19. Decision after the package

The whole-product conformance workbook and owner/capability matrix should choose
the next architectural cutover class, not one arbitrary behavior loop. A later
shadow report may reprioritize work only after the four-root surfaces are
stable enough for observed behavior to be meaningful.

Candidate next packages:

1. **Semantic read and result-envelope cutover** if current owners cover the
   majority of high-value read/compare turns;
2. **Life owner/search package** if Life gaps dominate A05/A12 and real turns;
3. **Opening/causal explanation package** if Home/Places explanation and
   forward-opening gaps dominate;
4. **general Monitor owner** if live operational requests are common and
   current notification machinery is too specialized;
5. **contribution enforcement package** if under-governed retention or memory
   writes are observed; or
6. **typed mobile entry/return contract** if unresolved origin/return state is
   the main blocker.

The choice is architectural: it should improve multiple situations and root
surfaces at once. It is not “prove one loop first.”

---

## 20. Founder execution order

The recommended order is:

```text
PR 0  baseline truth
  ↓
PR 1  core contribution + turn contracts
  ↓
PR 2  entry compiler + A01–A12
  ↓
PR 3  semantic catalog/selector
  ↓
PR 4  dormant runtime seam, default off
  ↓
PR 5  offline operational reader
  ↓
whole-product cases + owner/read contract choose the next package
```

Do not parallelize PR 1 and PR 2 across the same files. PR 2 depends on the
meaning of the core contracts. PR 3 can begin after the contract vocabulary is
stable, but it should not land before the portfolio proves what selection must
produce.

PR 0–PR 5 are now implemented. The next product-architecture action is the
whole-product conformance and owner/read-model package. There is no current
live-runtime action.

---

## Final recommendation

Build the **Agentic Semantic Facade** as a dark compiler and comparison layer.

It is the smallest package that operates at the correct altitude for the new
Vesper: not a Chat feature, not a Home card, not an itinerary rename, and not a
second runtime. It gives the current mature engineering system a new semantic
spine while preserving the infrastructure that already works.

The most important discipline is that target language must remain honest:

- a client hint is not a canonical owner;
- an Admission request is not retention authority;
- a selected tool is not an executed consequence;
- an action attempt is not a canonical owner receipt;
- a Trip specialization is not a general Life or Plan owner;
- a presentation tool is not semantic value;
- a plausible model response is not architecture; and
- a shadow frame is not enforcement.

Once this package is live, the next engineering decision will be based on
observed architectural pressure rather than intuition alone—without reducing
the product vision to a narrow loop.
