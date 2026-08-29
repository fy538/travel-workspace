---
doc_type: working
status: active
owner: founder / product / architecture / AI systems / backend / mobile
created: 2026-08-29
expires: 2026-09-28
why_new: Audits the implemented agent and Chat architecture after the product pivot, distinguishes reusable runtime machinery from the legacy Trip-and-itinerary worldview, and defines an adapter-first migration that preserves proven engineering threads.
promotes_to: null
supersedes: []
related:
  - ../systems/concierge-vesper.md
  - ../systems/contribution-and-consequence.md
  - chat-as-agentic-interaction-layer-research-2026-08-29.md
  - agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - agentic-capability-and-tool-cutover-plan-2026-08-29.md
  - contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - ../../travel-agent/docs/architecture/Agent Control Plane Refactor.md
  - ../../travel-agent/docs/architecture/Conversation System Architecture.md
  - ../../travel-agent/docs/product/Product Model.md
  - ../../travel-agent/backend/concierge/FEATURE.md
  - ../../travel-agent/backend/inbound/FEATURE.md
  - ../../travel-agent/backend/notifications/FEATURE.md
  - ../../travel-app/docs/page-specs/agent-chat.md
---

# Current agent and Chat architecture: repurpose audit

## Question

How much of Vesper's current agent and Chat system can survive the strategic
pivot, which parts are merely expressed in the wrong product vocabulary, and
which parts would quietly pull the new product back toward a Trip, itinerary,
and feature-card worldview if left intact?

This is an architecture salvage audit, not a claim that the current agent
already realizes the new product. It traces the implemented turn from entry to
owner mutation and mobile delivery; inventories current capabilities; checks
authority, privacy, context, memory, multiplayer, proactive behavior, and
specialist systems; and separates runtime maturity from semantic fit.

## Executive verdict

The agent is **not obsolete**, and it does **not** need a ground-up rewrite.
The strongest conclusion from the code is more specific:

> **Vesper has a mature conversational execution substrate inside a legacy
> semantic operating system. Preserve the execution substrate. Replace the
> model-facing worldview through typed, owner-aligned adapters.**

The reusable center is substantial:

- generic personal and group conversations, including conversations with no
  Trip;
- durable turn identity, persistence, idempotency, concurrency control,
  interruption, recovery, and completion after a client disconnect;
- a common async agent loop with budgets, deterministic tool ordering,
  bounded recovery, and safe handling of consequential work;
- a typed control plane with permitted effects, action envelopes, authority
  evidence, postconditions, execution receipts, and verification;
- a declarative tool registry with eligibility, contextual retrieval, input
  and output validation, retry policy, and owner gateways;
- selective context loading with privacy scope, freshness, token accounting,
  and content-free traces;
- group privacy composition and human-only group messaging;
- Intake custody, Experience Graph Occasions, relationship/place handoffs,
  notification delivery, planning reconciliation, place research, and booking
  recovery at adjacent owner seams;
- a hardened mobile streaming client and a bounded native-card protocol whose
  actions are resolved by the server at use time.

The obsolete center is also substantial:

- `INTAKE / CONVERSATION / PROACTIVE` is too crude a description of the job;
- the first turn is assumed to be travel intake and is prevented from
  committing even when the user supplied valid authority;
- lifecycle, prompts, context fields, capability names, and many tools assume
  a Trip and itinerary are the normal universe;
- presentation and maintenance are exposed as model tools;
- memory is partly model-curated through automatic observation and reflection
  rather than admitted through the contribution contract;
- proactive production is mostly Trip momentum, booking, and itinerary
  maintenance rather than a general monitor over lived-world commitments;
- structured client attachments and returned cards encode far fewer post-pivot
  objects than the owner systems now support.

The migration is therefore neither “change the prompt” nor “replace the
agent.” It is a **semantic inversion on top of proven rails**:

```text
current reality
  model chooses Trip/itinerary/feature operations
  and often chooses presentation

target reality
  runtime compiles job + ResourceRefs + usable evidence + authority + return target
        ↓
  model selects stable human capability and canonical owner operation
        ↓
  existing writer, specialist, or new owner executes behind an adapter
        ↓
  owner readback + verified receipt determines truth
        ↓
  runtime selects prose, instrument, artifact, owner navigation, or silence
```

This lets Vesper keep most of its difficult engineering work while changing
what that machinery means.

## 1. Method and evidence

The audit covered the workspace and both child repositories, with special
attention to code and documents changed since August 14, 2026.

### 1.1 Backend paths traced

- public conversation REST and SSE routes;
- turn preparation, persistence, replay, retry, and cancellation;
- session cache and per-conversation serialization;
- context compilation, entry seeds, location, and privacy policy;
- prompt construction and modular prompt skills;
- capability eligibility, contextual retrieval, and tool registry;
- action authority, shared agent loop, postconditions, and receipts;
- memory, Intake, Experience Graph, Places, planning, booking, research,
  notifications, proactive turns, and voice integration;
- group participation, strict group composition, reactions, votes, and
  relationship/Occasion cards.

### 1.2 Mobile paths traced

- the generic Chat surface and trip-linked Chat entry;
- composer text, voice, image, location, and typed-context inputs;
- SSE transport, smoothing, queuing, reconnect, foreground recovery, retry,
  cancellation, and card arrival;
- message attachment mapping and the native attachment renderer;
- composed-card schemas, opaque action resolution, owner handoffs, and
  navigation return behavior.

### 1.3 Characterization tests run

The following focused existing suites passed without code changes:

| Layer | Result | What it characterizes |
| --- | ---: | --- |
| Backend | **1,138 passed** | Authority binding, tool eligibility and retrieval, generated tool contracts, postconditions and receipts, group privacy composition, stream reconciliation, and entry seeds |
| Mobile | **106 passed** | Card-blueprint validation, backend-message mapping, delivery lifecycle, and composed-card rendering |

Thirteen backend warnings identify tests already listed in the repository's
Postgres leak baseline, all in group-compose coverage. They are not failures,
but they remain operational debt. Mobile message-mapping tests intentionally
emit schema-mismatch warnings for malformed compatibility fixtures and still
pass their fallback assertions.

These results do not prove the live product. They do establish that the
candidate substrate has unusually dense characterization and should not be
discarded casually.

## 2. The current turn, end to end

The actual architecture is more general than the old product language implies.

```text
Home / Places / Life / Chat / share / notification / card action
        ↓ selected context, optional images, GPS, entry seed
generic conversation admission
        ↓ authenticated participant + participation policy + idempotency
persist user message + pending agent message
        ↓ one serialized turn per conversation
parallel context compiler
        ↓ typed packets + privacy/freshness/selection trace
deterministic eligibility + contextual capability retrieval
        ↓ immutable permitted tool set
prompt + model + shared async tool loop
        ↓ ActionEnvelope before dispatch
canonical owner / specialist / compatibility writer
        ↓ output validation + postcondition readback
ExecutionReceipt + canonical semantic result
        ↓ SSE text/progress/card/terminal reconciliation
native Chat message, instrument, receipt, or owner handoff
        ↓
Home / Places / Life reread owner truth
```

The current implementation completes most of this path. The missing post-pivot
work is concentrated at four seams: what the turn is understood to be, which
owner-level capabilities the model sees, what durable use the contribution
permits, and what semantic result surfaces receive.

### 2.1 Entry and admission

The generic conversation API already supports:

- personal or group rooms;
- an optional Trip rather than a required Trip;
- text and voice turns;
- up to four images;
- up to three typed context attachments;
- a cached GPS reading that can accompany a turn without blocking time to
  first token;
- server-owned conversation seeds and entry metadata;
- durable retry against the original user message;
- human-to-human group messages with `trigger_agent=false`;
- Vesper participation controlled by group agency, room mute, personal mute,
  and proactivity threshold.

This means the post-pivot Chat does not need a new transport simply to escape
Trip. It needs a richer `InteractionEntry` contract over the generic route.

The current weakness is vocabulary. Typed attachments largely name place,
venue, experience, accommodation, dossier, and itinerary entities. The server
can resolve a few newer Experience Graph references, but the shared public
contract does not yet treat Person, Relationship, Source, Occasion, Plan,
Commitment, Moment, Outcome, Activity, or owner projection as first-class
`ResourceRef`s.

### 2.2 Persistence and turn lifecycle

`ConciergeSession` treats the database as source of truth and memory as a
performance cache. It persists the human message and an agent placeholder
before model work, transitions that placeholder through pending and streaming
states, and preserves a durable identity across retries.

Important reusable properties include:

- an in-process lock and distributed per-conversation turn serialization;
- validated replay, cached completion, and in-flight retry behavior;
- history reload that avoids replay duplication;
- canonical failure persistence rather than a lost half-turn;
- background completion when the mobile SSE connection disappears;
- active-turn cancellation with explicit race handling;
- quota and provider failure behavior;
- content grounding, privacy, private-markup, and UUID leakage guards;
- terminal reconciliation when streamed prose differs from the canonical
  recorded result;
- detailed turn, delivery, latency, tool, reasoning, and AI-run telemetry.

This is hard-won product infrastructure. The pivot should make more kinds of
work flow through it, not create a parallel agent runtime.

### 2.3 Context compilation

The context compiler is already selective rather than a raw memory dump. It
loads slices in parallel and records, for each packet:

- source;
- privacy scope;
- loaded, empty, skipped, or unavailable state;
- selection reason;
- freshness and `as_of` time;
- token budget and estimate;
- content-free error and trace metadata.

It can currently load social state, preference profiles, group legibility,
Trip and itinerary state, planning briefs, member briefs, observations,
constraints, familiarity, prior Trip briefs, intent scratchpad, shared
observations, user facts, current location, spatial situation, experience
scope, loved places, and affect.

The privacy choices are often sound:

- observations are retrieved progressively instead of injected wholesale;
- facts and constraints are selected based on cues and scope;
- GPS is loaded only when the turn earns it;
- a Trip-less group room does not receive the speaker's private location;
- loved places remain private;
- entry references are reloaded from server truth rather than trusted from
  client text.

The compiler should survive. Its current collection of special-purpose fields
should evolve into a smaller number of typed packets:

```text
JobContext
SelectedResourceContext[]
MomentContext
RelationshipContext
SourceEvidenceContext
AuthorityContext
ConversationContext
OwnerStateContext[]
ReturnContext
```

The target is not one giant “user context.” It is purpose-selected evidence
with owner, scope, freshness, and permitted use preserved.

### 2.4 Turn planning and capability selection

The typed control plane already declares:

- actor, conversation, and optional Trip;
- turn intent;
- agency level: respond, propose, or commit;
- context policy snapshot;
- model route;
- immutable permitted tools and effects;
- latency and privacy mode.

Before the model sees tools, deterministic eligibility filters the registry by
channel, lifecycle, prerequisites, feature readiness, and context. Contextual
retrieval then selects from the eligible set using capability descriptions,
examples, and recent language while retaining foundational tools.

This two-stage structure is exactly right for a broad product: a large
underlying capability catalog does not require exposing every operation on
every turn.

The current planner is nevertheless semantically insufficient:

- `INTAKE / CONVERSATION / PROACTIVE` describes transport origin, not the
  human job;
- `RESPOND / PROPOSE / COMMIT` describes action depth but not contribution
  treatment, audience, owner, time horizon, or return target;
- any first turn is classified as intake;
- first-turn commits are suppressed even when an exact structured action or
  contribution grant could make one safe;
- Trip lifecycle determines too much eligibility.

The planner should be extended, not replaced, into an `AgenticTurnPlan` that
contains at least:

| Dimension | Examples |
| --- | --- |
| Human job | understand, explore, compare, compose, coordinate, decide, act, monitor, reconcile, correct |
| Product move | make sense, open possibility, help it work, carry forward; zero or more, not a forced sequence |
| Gesture | Ask, Point, Bring, Keep, Share, Decide, Correct |
| Contribution treatment | transient, source-bound, proposed durable, durable |
| Learning scope | none, source, episode, place, relationship, person |
| Audience | private, named people, Occasion, group, public |
| Target owners | Source, Place, Occasion, Plan, Commitment, provider, Life index, monitor |
| Selected resources | versioned, purpose-bound `ResourceRef`s |
| Action depth | read, propose, commit |
| Return target | originating surface, object, scroll anchor, or thread |
| Privacy/latency | existing modes plus connected-source purpose limits |

The existing immutable permitted-tool and permitted-effect fields remain
valuable outputs of that richer compilation.

### 2.5 Model loop and execution

The shared async agent loop is one of the clearest keep decisions.

It already:

- runs independent read tools in parallel;
- serializes consequential and unknown-effect calls in provider order;
- captures action envelopes before dispatch;
- synthesizes receipts after execution;
- buffers commit prose until receipts exist;
- withholds unverified claims of success;
- blocks unsafe automatic retries and repeated tool signatures;
- classifies tool errors and enforces a recovery budget;
- enforces iteration, token, and wall-clock budgets;
- re-anchors a wandering model;
- supports cacheable calls and durable workflows;
- can return deterministic stale-state outcomes without asking the model to
  paraphrase them.

The loop is not inherently a travel loop. It is a generally useful execution
kernel. The central dispatcher is still a large switch and several owner
systems are lazily imported, but the registry already provides the seam for
handler adaptation.

### 2.6 Authority, postconditions, and receipts

The current authority system binds server-issued evidence to:

- actor;
- action type;
- conversation and optional Trip;
- exact parameter fingerprint;
- optional source fingerprint;
- single use within the turn.

It refuses client-forged `structured_action` metadata and fails closed on
ambiguous, negated, or hypothetical text. The loop creates `ActionEnvelope`s
with idempotency keys and expected postconditions, then records
`ExecutionReceipt`s with changed objects, versions, verification results,
failure category, and a content-free result fingerprint.

This is the right action skeleton. Its policy vocabulary is still narrow:

- only a few operations require structured actions;
- conversational evidence is recognized for a small set of Trip patch,
  expense, constraint, and fact operations;
- many model-managed memory, presentation, and maintenance writes require no
  explicit authority;
- authority is tool-specific rather than derived from the five contribution
  axes and an owner command.

The target should compose two independent grants:

1. `ContributionUseGrant`: what may be retained, learned, inferred, shown, and
   for what purpose;
2. `ActionAuthority`: what exact owner or external action may execute now.

Supplying information for an answer must not imply either a durable write or a
provider action. Executing an action must not imply broader memory or audience
rights.

### 2.7 Output, presentation, and mobile delivery

The mobile transport is also ahead of the current product semantics. It
supports optimistic messages, idempotency, streaming text, reasoning and tool
progress, text smoothing, queued sends, interruption, durable retries,
foreground recovery, card arrival, socket reconnection, and completion while
backgrounded.

The native attachment renderer has many old travel card types. Those card
types are not the asset to preserve. The asset is `CardBlueprintV1`:

- a bounded declarative block grammar rather than server-delivered UI code;
- a required artifact reference;
- compact intents such as glance, shortlist, comparison, receipt, handoff, and
  collaboration;
- opaque action references;
- server-side re-authorization and current-state resolution at tap time;
- a durable message-body fallback when a future payload is invalid;
- client ownership of React, styles, routes, and callbacks.

The server has already extended artifact references to Occasion, Commitment,
Outcome, and place memory. This is a credible base for semantic results across
the new product.

The current agent should stop calling model-visible presentation tools such as
“post card,” “present options,” or “post map.” Instead, it should return a
`SemanticResultEnvelope`:

```text
answer or result kind
grounded claims and source refs
owner refs and versions
options / status / receipt / handoff semantics
available opaque actions
urgency, density, and interaction hints
return target
```

A deterministic projection resolver can then choose prose, a compact native
instrument, an artifact, direct owner navigation, or no extra presentation.
This preserves flexible expression without making the model a UI compositor.

## 3. Current capability truth

### 3.1 Registry inventory

The current immutable registry exposes **73 model-visible tools**:

| Measure | Count |
| --- | ---: |
| Read effects | 35 |
| Propose effects | 4 |
| Commit effects | 34 |
| Durable execution class | 2 |
| Requires a Trip | 31 |
| Requires an itinerary | 17 |

The catalog includes strong underlying functions: conversation search,
experience and venue search, route and distance checks, location, Trip
snapshots, itinerary reads and feasibility checks, accommodation and transport
search, web and angle research, narration resume, expenses, memory recall,
group composition, proposals, planning generation, booking confirmation, and
owner mutations.

The problem is not the size of the registry. It is the semantic distribution:

- 28 tools sit directly in Trip, itinerary, or planning namespaces;
- lifecycle still centers `NO_TRIP / PRE_TRIP / ACTIVE_PLANNING /
  DURING_TRIP / POST_TRIP`;
- 34 tools can commit, including several presentation, ingestion, reflection,
  and maintenance operations;
- only four operations are explicitly proposal effects;
- stable post-pivot capabilities such as Source admission, general Plan and
  Commitment operations, Occasion composition, Life retrieval, relationship
  coordination, durable monitoring, and owner reconciliation are absent or
  reachable only through internal seams.

### 3.2 The model-facing capability set should change

The target catalog should be organized around owner capabilities, not screen
features:

| Target capability | Existing implementation to reuse first |
| --- | --- |
| `Conversation.Search` / `ReadWindow` | Existing conversation history tools |
| `Source.Inspect` | Current image/vision answer plus Intake interpretation |
| `Source.Admit` / `Correct` | Intake v2 custody and proposal-decision flow |
| `Place.Search` / `Read` / `Compare` | Existing discovery, venue, distance, route, dossier, and status handlers |
| `Place.Relate` | Loved-place, place-memory, relationship handoff, and Lived Experience adapters |
| `Plan.ReadSnapshot` | Existing Trip snapshot and itinerary read adapters |
| `Plan.ProposeDelta` | Existing proposal and planning-agent operations |
| `Plan.ApplyDelta` | Existing preservation-first itinerary operation gateway for Trip-backed plans |
| `Commitment.Read` / `Propose` / `Confirm` | Booking, attendance, invitation, and provider session machinery |
| `Occasion.Read` / `Compose` / `Invite` / `Decide` | Experience Graph Occasion, invitation, decision, and composed-card flows |
| `Relationship.Compose` / `Coordinate` | Group context, privacy compiler, pair-room and handoff mechanisms |
| `Life.Find` / `ReadEpisode` / `ReadArtifact` | Conversation, Source, Trip, Occasion, Outcome, place-memory, and emerging Life-index reads |
| `Research.Start` / `Read` | Existing quick/deep research agents and lazy-research handoff |
| `Monitor.Create` / `Read` / `Cancel` | Notification scheduler, candidate ledger, delivery spine, and outcome updater after adding a general monitor owner |
| `Action.Reconcile` / `Repair` | Current receipts, version readback, stale-state and recovery machinery |

Trip and itinerary remain valid specializations behind `Plan` adapters. This
prevents the pivot from throwing away the most production-hardened writer
while ending its role as universal product grammar.

## 4. The pivot has already reached the edges

It would be inaccurate to say no agent-adjacent engineering changed after
August 14. The model-facing center stayed mostly stable, but several new owner
and delivery seams appeared:

### 4.1 Intake custody

The new inbound path is custody-first. It creates a Source, uploads and
finalizes content, performs owner-scoped interpretation, supports correction
and proposal decisions, and does not let the client assert truth, memory,
audience, or action authority.

Chat screenshot ingestion now defaults to that path: the model can deliver
immediate vision value while Intake owns durable custody. This is almost the
exact post-pivot separation needed for Ask versus Point/Bring. The missing
piece is a shared contribution admission decision for every modality, not a
new upload stack.

### 4.2 Experience Graph and Occasion collaboration

New composed cards support private invitations and group decisions. Membership,
revision, status, option validity, and expiry are rechecked when an action is
used. The card contains opaque symbolic actions; it is not its own authority.

This is an exemplary post-pivot vertical slice:

```text
owner truth → safe projection → opaque action → server re-authorization
            → owner mutation → refreshed projection
```

Chat should generalize this pattern rather than invent agent-owned social
objects.

### 4.3 Relationship and place handoffs

Place and relationship cards can hand a person into a private or pair context
without treating the card as truth. These are early implementations of the
cross-surface return contract and social opening grammar.

### 4.4 Lived Experience adapters

Decision-frame and producer adapters can already ingest content-free turn and
owner references into the Lived Experience harness. Most families remain
shadow or abstain because required owner readbacks and grounded openings are
missing. That is useful, honest readiness infrastructure; it is not yet a
visible agent capability.

### 4.5 Situated notification judgment

The notification stack now has deterministic gates, semantic admission,
arbitration, delivery, an append-only ledger, and outcomes. The general runtime
exists, while its producers remain dominated by Trip schedules, booking,
weather, disruption, planning momentum, and group interjection.

This asymmetry is favorable. The product pivot has begun building the owners
and policy surfaces that the existing agent can orchestrate. The next phase is
to expose them coherently through the control plane rather than reimplement
them inside prompts.

## 5. Reuse classification

### 5.1 Keep as foundational machinery

These threads are semantically general and should survive with minimal change:

| Engineering thread | Why it survives |
| --- | --- |
| Generic conversation records and participant policy | Already supports personal, group, Trip-linked, and Trip-less rooms |
| Durable message and turn identity | Necessary for retries, receipts, monitors, and cross-surface continuity |
| Per-conversation serialization | Prevents conflicting multi-sender and multi-action turns |
| REST/SSE convergence | Keeps blocking and streaming semantics aligned |
| Background completion and reconnect | Required for real mobile agent work |
| Cancellation and queued sends | Required for fluid conversational control |
| Shared async agent loop | General tool-use execution kernel |
| Immutable registry | Single join point for schema, handler, policy, eligibility, verification, and telemetry |
| Deterministic eligibility before retrieval | Scales a broad capability catalog safely |
| Contextual capability retrieval | Lets the product remain broad without feeling like a super-app menu |
| Tool input/output validation | Owner and model boundary protection |
| Action envelopes and exact parameter fingerprints | Stable authorization and idempotency seam |
| Postcondition readback and receipts | Prevents model prose from declaring false success |
| Context packet traces | Privacy-safe debuggability for selective context |
| Grounding and private-output guards | Cross-domain safety requirements |
| Strict group privacy compiler | Critical multiplayer infrastructure |
| Human-only group messages and agency knobs | Vesper can participate without colonizing the room |
| Intake custody and correction | Correct Source ownership and provenance |
| Experience Graph owner actions | Correct Occasion and collaboration authority |
| Planning versioning, CAS, repair, and undo | Proven Plan specialization for travel |
| Booking consent, session, reconciliation, recovery | Valuable commitment/provider substrate despite limited live transaction coverage |
| Notification ledger, gates, delivery, outcomes | General proactive substrate |
| Native semantic-card protocol | Bounded rich response and safe action handoff |
| Mobile Chat transport hooks | Mature delivery and recovery behavior |
| Turn and delivery telemetry | Necessary for shadow migration and operational proof |

### 5.2 Adapt behind a new semantic interface

These systems remain useful but must stop defining the product ontology:

| Current thread | Adaptation |
| --- | --- |
| `TurnPlan` | Add job, gesture, contribution treatment, learning scope, audience, owner targets, selected resources, and return target |
| Trip lifecycle | Replace eligibility input with Moment, active owners, job, channel, and resource readiness; retain Trip phase as one specialization |
| Context compiler | Preserve packet machinery; replace many special fields with typed owner/resource packets |
| Prompt skill selector | Select by job and owner capability, with Trip planning as an optional specialist overlay |
| Itinerary reads/writes | Route through `Plan.*` compatibility adapters |
| Booking tools | Route through `Commitment.*` and provider adapters |
| Discovery and research | Separate Place truth, possibility generation, and durable research workflow |
| Conversation intent scratchpad | Replace with typed activity/job state; never make it canonical owner truth |
| Card output | Derive from `SemanticResultEnvelope`; do not expose presentation calls to the model |
| Group composition | Make mandatory runtime egress for group-bound model text rather than an optional model-selected read tool |
| Notification triggers | Add a general monitor owner and compile candidates from Plan, Commitment, Occasion, Place, people, and external state |
| Voice | Keep modality and deferred execution; remove Trip-phase quota semantics and prove live configuration |
| Deep research agent | Expose as durable `Research` operation with Source and return contracts |
| Lived Experience harness | Bind to real owner readbacks and make readiness explicit before visible behavior |

### 5.3 Quarantine until policy is rebased

These mechanisms should not silently keep writing under the old assumptions:

- automatic `observe` calls based on what the model finds memorable;
- observation-count-triggered synthesis;
- post-session reflection that writes Trip-linked memory;
- model-visible prune, event-processing, and refresh maintenance tools;
- first-contact travel intake and its mandatory question sequence;
- free-form `intent_state` as a durable interpretation of the person;
- Planning Autopilot as a universal measure of product momentum;
- Trip-specific digest semantics presented as general carry-forward value;
- taste-DNA and Atlas interpretations that turn evidence into personality
  claims without the new editorial and contribution standards;
- proactive copy paths that have not passed the new contextual-integrity and
  value-before-workflow gates.

Quarantine means retain the code and tests, disable or shadow its durable or
visible effect, and route it only after its owner, evidence, purpose, and repair
contract are explicit.

### 5.4 Retire from the model-visible surface

The following categories should disappear as model choices even when their
underlying handlers remain:

- `present_*`, `post_*`, and other UI-composition tools;
- model-selected group egress;
- maintenance operations that belong to a worker or owner;
- direct itinerary nouns where a stable `Plan` operation is sufficient;
- direct Trip creation or mutation where an Occasion, Plan, or Commitment
  command better expresses the job;
- generated artifacts used as mutation authority;
- prose-only “success” without owner readback.

This reduces apparent capability sprawl without reducing what Vesper can do.

## 6. Multiplayer and social capability

The current multiplayer system is stronger than a typical chatbot room, but
its pieces need to be composed into the new grammar.

### 6.1 What exists

- group conversations may exist without a Trip;
- participants can talk without invoking Vesper;
- a room can be reactive or proactive, with separate notification cadence;
- personal and room-level muting are distinct;
- strict group composition receives only authorized, group-safe inputs;
- identity and private-constraint leak checks run before delivery;
- uncertain output can degrade to a dignified private handoff;
- votes, reactions, invitations, pair rooms, Occasion decisions, and place
  handoffs exist;
- proactive group interjection requires opt-in and an exact human source
  message.

### 6.2 What should change

Multiplayer should not be represented as a separate “social feature” tool
namespace. Relationship, Occasion, Plan, Commitment, and Source owners should
carry the social meaning. The turn compiler should know:

- whose information is being used;
- which audience may receive which projection;
- whether Vesper is speaking to one person, composing for a group, or helping
  people coordinate without speaking;
- whether the result changes only a private view, a shared Occasion, a Plan,
  or an external commitment;
- who can correct, withdraw, supersede, or resolve it.

The existing privacy compiler then becomes a mandatory egress policy for any
group-bound semantic result, not a special tool the model may forget to call.

## 7. Immediate value and contribution

The new contribution philosophy changes the agent more deeply than adding
memory controls.

### 7.1 What current Chat can already do

When a person attaches an image or points to a place, the current system can:

- inspect the current material immediately;
- combine it with location and selected conversation context;
- search places or the web;
- compare routes, venues, and constraints;
- answer in the same turn;
- persist the raw Source through Intake v2 in supported flows;
- hand off to an owner-backed card.

That is enough machinery for “give value now, then carry forward only what was
authorized.”

### 7.2 What violates the target contract

The current prompts and memory tools still encourage the model to infer what
is worth observing and to convert repeated observations into durable profiles.
An Ask may therefore leave more residue than the user intended. Conversely,
the route does not yet carry a normalized five-axis contribution grant, so
safe Point, Bring, Keep, Share, Decide, and Correct behavior is inconsistent
across modalities.

### 7.3 Target admission sequence

```text
1. Inspect transiently for the immediate job.
2. Deliver useful grounded value.
3. Compile gesture and explicit/structural contribution grant.
4. Admit only permitted source, claim, projection, learning, and audience layers.
5. Execute an independently authorized owner action if requested.
6. Return owner readback and a compact, reversible receipt.
7. Make correction, withdrawal, and scope repair reachable later.
```

This admission step belongs between context compilation and owner mutation. It
must not be left to prompt interpretation or individual tool handlers.

## 8. Proactive, monitoring, and the live engine

The current notification system is credible infrastructure for “help it work,”
but it is not yet the general live engine envisioned by the product.

### 8.1 Strong substrate

- deterministic quiet hours, cooldowns, and caps;
- candidate-level source and scope metadata;
- semantic admission and arbitration;
- send, defer, downgrade, or suppress decisions;
- one mandatory delivery path;
- append-only delivery ledger;
- multi-channel fanout;
- outcome and state updates;
- the ability to invoke the same Concierge session path for a proactive turn;
- strict private/group target resolution.

### 8.2 Legacy semantics

Current producers mostly reason about Trip deadlines, booking state,
disruptions, weather, pre-Trip drip, itinerary planning gaps, and group
interjection. Planning Autopilot measures progress toward a Trip itinerary.
Digest output is similarly Trip-specific.

### 8.3 Missing owner

The product needs a durable `Monitor` or `Watch` authority with:

- subject and owner refs;
- triggering condition;
- data source and refresh policy;
- start, expiry, and cancellation;
- audience and delivery channel;
- urgency and interruption budget;
- allowed action depth;
- last evaluation, outcome, and receipt.

The current scheduler, ledger, delivery, and outcome machinery can execute this
owner. Chat should expose `Monitor.Create / Read / Change / Cancel`, while the
model never schedules ad hoc background work outside that authority.

## 9. Specialist systems that can be retained

### 9.1 Planning

The planning agent has preservation-first scoped replans, version checks,
compare-and-swap, feasibility validation, deterministic repair, bounded model
repair, receipts, and undo. It is the most mature Plan specialization in the
system.

Do not delete it because itinerary is no longer the product grammar. Put it
behind `Plan.ReadSnapshot`, `Plan.ProposeDelta`, `Plan.ApplyDelta`, and
`Plan.Reconcile` for Trip-backed plans. New flexible Plan owners can later
implement the same interface.

### 9.2 Booking and providers

Booking has controller, consent, provider-session, reconciliation, and recovery
machinery. It is not yet a broadly transacting product: provider support is
mostly planning or handoff, and no category should be pitched as generally
bookable in-app.

Retain the machinery behind `Commitment` and provider capabilities, and expose
only operations whose readiness and action authority are truthful.

### 9.3 Place and research

Venue search, distance, route, accommodation, transport, web research, angle
search, dossiers, and lazy research provide a useful intelligence base. Today
they are split between synchronous Chat reads, background agents, and
presentation cards.

Rebase them around:

- Place identity and current truth;
- relationship-to-place evidence;
- possibility generation;
- cited research Sources;
- durable research activity with a return target;
- a semantic result independent of one card type.

### 9.4 Voice

The voice service already connects speech-to-text, the Concierge session, and
text-to-speech, with deferred delivery for slower tool work. It is gated off,
unconfigured for production, and its quota logic is tied to Trip phase.

Voice is therefore a reusable modality thread, not a present product
capability. Rebase its policy and validate the live path after the semantic
facade stabilizes.

## 10. Target architecture

The new architecture should add a thin set of general contracts around the
current runtime.

### 10.1 `InteractionEntry`

Normalizes where the turn began and what the user selected:

```text
entry_id
actor and conversation
origin surface and route
selected ResourceRefs + versions
return target and visual anchor
current modality and transient attachments
server-issued structured action, if any
location and Moment pointers, if earned
```

Home, Places, Life, Chat, share, notification, and cards should all enter
through this contract.

### 10.2 `ResourceRef`

A versioned, owner-resolvable reference for Person, Relationship, Place,
Source, Occasion, Plan, Commitment, Moment, Outcome, Activity, monitor, and
provider state. It carries identity, not a client-authored truth payload.

### 10.3 `AgenticTurnPlan`

Extends the current `TurnPlan` with human job, product moves, gesture,
contribution use, audience, target owners, selected resources, action depth,
and return target. It retains current model route, privacy, latency, permitted
effects, and immutable capability selection.

### 10.4 `ContributionUseGrant`

The system-owned compiled representation of source retention, scoped learning,
inference, audience, purpose, treatment, expiry, and repair. Model calls may
consume it but may not manufacture or broaden it.

### 10.5 Owner capability adapter catalog

Maps stable model-visible operations to current handlers or new owner APIs:

```text
semantic operation
  → eligibility and readiness
  → input schema and referenced owners
  → contribution and action requirements
  → compatibility handler or canonical owner
  → postconditions and verifier
  → result schema
```

The existing immutable registry can host this catalog during migration.

### 10.6 `SemanticResultEnvelope`

Separates what happened and what it means from how it is rendered. It contains
grounded content, ResourceRefs, receipts, possible next actions, lifecycle,
urgency, and return behavior. A projection resolver chooses the medium.

### 10.7 `Activity` and return contract

Long-running research, planning, monitoring, provider, and repair work needs a
common activity identity and status. Every surface-originated job should be
able to return to the originating surface or open its canonical owner with
fresh readback.

## 11. Migration sequence

The next step should not be a prompt rewrite, a generalized Occasion rewrite,
or a frontend redesign. It should be a **shadow semantic facade** across the
existing turn.

### Phase 0 — lock the behavior we intend to preserve

1. Retain the focused characterization suites used in this audit.
2. Map the twelve cross-surface agentic fixtures to current routes, selected
   tools, owner calls, receipts, and outputs.
3. Add missing characterizations for Trip-less groups, Intake image custody,
   disconnected completion, structured card actions, and proactive target
   resolution.
4. Record current latency, selected-tool count, tool failure, receipt
   verification, privacy fallback, and reconnect baselines.

This is not “proving one behavior loop.” It is protecting the runtime while a
systematic architecture migration proceeds.

### Phase 1 — introduce the semantic facade in shadow

1. Add `InteractionEntry` and a generalized `ResourceRef` while translating
   existing attachment and seed types into them.
2. Add optional post-pivot fields to `TurnPlan` or introduce a versioned
   `AgenticTurnPlanV2`; do not break current dispatch.
3. Compile gesture, contribution use, human job, owner targets, and return
   target for every fixture in shadow.
4. Add a target capability-adapter catalog whose first operations route to
   unchanged existing handlers.
5. Persist content-free comparison telemetry between legacy and target plans.

No visible behavior needs to change in this phase. Its purpose is to prove
that the new philosophy can compile into concrete runtime decisions.

### Phase 2 — cut over reads and semantic results

1. Expose owner-aligned read capabilities first: Conversation, Source, Place,
   Plan, Occasion, Commitment, Life, and Research.
2. Hide presentation and maintenance tools from the model.
3. Return `SemanticResultEnvelope` alongside the legacy response envelope.
4. Resolve composed cards and navigation from semantic results.
5. Compare relevance, schema size, selected-tool count, latency, and fixture
   fidelity before removing old read names.

Read-first cutover changes the worldview without risking mutations.

### Phase 3 — cut over proposals and commits

1. Enforce `ContributionUseGrant` before any durable personal or social write.
2. Map `Plan.*` to existing itinerary/planning gateways for Trip-backed plans.
3. Map `Occasion.*` to Experience Graph owners.
4. Map `Commitment.*` to booking, invitation, and attendance owners.
5. Require exact owner readback and receipts for all commits.
6. Move group composition from optional tool to mandatory egress.
7. Quarantine legacy automatic observation and reflection.

### Phase 4 — general monitoring and cross-owner activity

1. Add the monitor owner over existing notification infrastructure.
2. Add activity status and return behavior for research, provider, planning,
   and repair workflows.
3. Introduce a bounded saga/reconciliation contract for jobs that touch more
   than one owner.
4. Let Home, Places, and Life consume the same owner truth and activity state;
   do not make Chat copy its result into each surface.

### Phase 5 — retire the old worldview

1. Remove Trip phase as a universal prompt and capability selector.
2. Delete model-visible presentation and maintenance operations.
3. retire first-contact travel intake and free-form durable intent scratchpad;
4. remove legacy tool names after fixture and telemetry equivalence;
5. rebase voice, digest, and proactive producers on the new plan.

## 12. The recommended first engineering package

The highest-leverage next package is:

> **Agentic Semantic Facade — shadow compilation and compatibility catalog**

It should contain four bounded deliverables:

1. **Versioned entry and turn types**
   - `InteractionEntryV1`
   - generalized `ResourceRefV1`
   - `AgenticTurnPlanV2` fields beside current `TurnPlan`

2. **Contribution compilation**
   - structural Ask/Point/Bring/Keep/Share/Decide/Correct inputs;
   - five-axis `ContributionUseGrant` in shadow;
   - no durable behavior change yet.

3. **Compatibility capability catalog**
   - begin with read operations for Conversation, Source, Place, Plan,
     Occasion, Commitment, and Research;
   - map each target operation to current handlers and verifiers;
   - mark readiness and legacy dependencies explicitly.

4. **Fixture and telemetry harness**
   - compile all twelve cross-surface fixtures;
   - compare old and new selected capabilities, authority, owners, and return
     targets;
   - persist content-free mismatch codes;
   - fail CI on schema, registry, or verifier drift.

This package produces a step change because it makes the product philosophy an
executable control-plane contract. It also minimizes risk: no owner rewrite,
no UI dependency, no premature itinerary deletion, and no new agent runtime.

## 13. Principal risks and unresolved decisions

### 13.1 Conversation continuity

The code supports one personal home conversation, many personal activity
threads, group rooms, and Trip-linked rooms. Product canon still needs to say
when work remains in the main Chat timeline versus receiving an Activity or
owner-specific thread. The runtime can support either; leaving the choice
implicit will make Life refinding and Chat history incoherent.

**Recommendation:** keep one primary personal Chat timeline, create explicit
Activity identities for durable jobs, and allow owner projections to reopen
the relevant message window rather than proliferating hidden conversations.

### 13.2 Cross-owner atomicity

A turn may admit a Source, update a Plan, create a Commitment, notify a person,
and start a monitor. Current receipts cover individual tool execution better
than a multi-owner transaction.

**Recommendation:** use a saga-style Activity with ordered owner receipts and
compensation/reconciliation; do not attempt distributed database atomicity.

### 13.3 Trip-less group personalization

The compiler correctly avoids loading private member context merely because a
speaker is in a Trip-less group. It still needs an explicit, aggregate-safe
mechanism when the job genuinely requires group accommodation.

**Recommendation:** owners produce authorized group-safe projections; Chat
does not fetch raw individual profiles into the group prompt.

### 13.4 Monitor versus notification

Notification is delivery; monitor is durable intent and evaluation. Conflating
them would make “watch this” disappear into scheduler internals.

**Recommendation:** create a monitor owner and let notification remain its
delivery and outcome substrate.

### 13.5 Immediate image use versus durable Source custody

The current screenshot flow can answer immediately and separately create
custody. Other image routes may still blur those concerns.

**Recommendation:** all modalities share transient inspection first and Intake
custody only when the gesture grants it. Preserve one upload where possible,
but keep the authorities distinct.

### 13.6 Capability breadth and latency

A broader owner catalog can increase prompt schema size and retrieval error.

**Recommendation:** keep deterministic eligibility first, contextual retrieval
second, and foundational operations small. Measure selected schema tokens and
misrouting against the twelve fixtures before broadening visible capabilities.

### 13.7 Live evidence

The system charter remains accurate: the backend is heavily tested, but live
on-device Chat, release-profile SSE, voice, provider execution, and several
adaptive/Lived Experience paths are not fully certified.

**Recommendation:** do not confuse unit maturity with production proof. Preserve
the test base during the facade work, then certify the target path on device
before calling it shipped.

## 14. Architecture-level answer

The current product can retain far more engineering than its old nouns suggest.
The clean boundary is:

```text
KEEP
conversation + transport + persistence + context packet mechanics
+ eligibility/retrieval + agent loop + authority/receipt machinery
+ canonical owner writers + mobile semantic rendering

CHANGE
turn interpretation + contribution admission + lifecycle
+ model-visible capability vocabulary + owner targeting
+ semantic result and cross-surface return contracts

QUARANTINE
model-curated memory + first-contact Trip intake + itinerary momentum automation
+ model-selected presentation/maintenance + unrebased proactive interpretations
```

The app's strategic pivot is therefore technically plausible without losing
the core engineering threads. In fact, the safest way to realize the pivot is
to make those threads more explicit and more general: Chat becomes the
conversational operating surface over canonical owners, while its current
runtime continues to provide the difficult guarantees around latency,
continuity, privacy, authority, execution, and recovery.

The next architectural move is not to make the old concierge more eloquent.
It is to make the new product grammar compile into the old runtime's proven
control points—and then progressively remove the old worldview from what the
model can see.

## Evidence index

### Backend

- `travel-agent/backend/api/routes/conversations.py`
- `travel-agent/backend/api/routes/_message_flow.py`
- `travel-agent/backend/concierge/session.py`
- `travel-agent/backend/concierge/agent.py`
- `travel-agent/backend/core/agent_loop.py`
- `travel-agent/backend/core/control_plane.py`
- `travel-agent/backend/concierge/control_plane_adapter.py`
- `travel-agent/backend/concierge/turn_loader.py`
- `travel-agent/backend/concierge/turn_context.py`
- `travel-agent/backend/concierge/entry_context.py`
- `travel-agent/backend/concierge/prompts.py`
- `travel-agent/backend/concierge/tool_registry.py`
- `travel-agent/backend/concierge/capability_catalog.py`
- `travel-agent/backend/concierge/tool_eligibility.py`
- `travel-agent/backend/concierge/contextual_tool_retrieval.py`
- `travel-agent/backend/concierge/tool_io.py`
- `travel-agent/backend/concierge/action_authority.py`
- `travel-agent/backend/concierge/group_compose.py`
- `travel-agent/backend/concierge/composed_cards.py`
- `travel-agent/backend/concierge/experience_graph_cards.py`
- `travel-agent/backend/concierge/memory_tools.py`
- `travel-agent/backend/concierge/decision_frames.py`
- `travel-agent/backend/concierge/triggers.py`
- `travel-agent/backend/inbound/FEATURE.md`
- `travel-agent/backend/notifications/FEATURE.md`
- `travel-agent/backend/lived_experience/readiness.py`

### Mobile

- `travel-app/app/(tabs)/concierge/chat.tsx`
- `travel-app/hooks/useConciergeChat.ts`
- `travel-app/hooks/concierge-chat/`
- `travel-app/components/chat/ComposerBar.tsx`
- `travel-app/components/chat/AttachmentRenderer.tsx`
- `travel-app/components/chat/ComposedChatCard.tsx`
- `travel-app/utils/chat/cardBlueprint.ts`
- `travel-app/utils/chat/messageMapping.ts`
- `travel-app/utils/chat/deliveryLifecycle.ts`
- `travel-app/utils/sse.ts`

### Product and architecture contracts

- `travel-agent/docs/product/Product Model.md`
- `docs/systems/contribution-and-consequence.md`
- `docs/systems/concierge-vesper.md`
- `docs/working/chat-as-agentic-interaction-layer-research-2026-08-29.md`
- `docs/working/agentic-chat-cross-surface-fixture-pack-2026-08-29.md`
- `docs/working/agentic-capability-and-tool-cutover-plan-2026-08-29.md`
- `docs/working/contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md`
