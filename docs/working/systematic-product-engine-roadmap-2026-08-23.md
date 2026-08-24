---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Defines the minimum reusable authorities, artifact-native product surfaces, dependency order, representative slices, cancellation policy, and completion gates required to implement the August product grammar without reproducing the prior screen and workflow sprawl.
supersedes: []
promotes_to: null
source_of_truth_for: []
---

# Systematic Product-Engine Roadmap

> Status: active working execution plan
>
> This document proposes the engineering structure and migration sequence for
> the August product grammar. It does not by itself authorize production
> exposure, deletion of legacy authorities, a database reset, or promotion of
> the four-root shell.
>
> **Founder direction, 2026-08-23:** capability does not imply a standalone
> screen. The active product should contract around a few legible roots and a
> typed, dynamic artifact language inside Chat. Proposal, voting, booking, and
> expense capabilities may retain reliable domain truth while their legacy
> workflow screens are canceled, redirected, externalized, or deleted.

## 1. Purpose

The product now has eighteen canonical product-design journey families, from
bringing an artifact to immediate value through multiplayer coordination,
later continuity, correction, and forgetting. Implementing those journeys one
at a time as independent vertical products would reproduce the fragmentation
the August pivot is intended to resolve. Building a generalized engine and a
dedicated screen for every durable noun would reproduce the same fragmentation
at a different architectural layer.

The goal is therefore not:

```text
build CJ01
then build CJ02
then build CJ03
...
```

The goal is:

```text
preserve the few trust and truth invariants that must hold across the portfolio
  -> cancel presentation surfaces that no longer express the product
  -> build representative human-experience loops through typed Chat artifacts
  -> promote shared engines only after more than one real loop needs them
  -> mount a few coherent viewer-relative roots and focused workspaces
  -> retire duplicate presentation early and duplicate authorities safely
```

The roadmap therefore distinguishes **capability preservation** from **surface
preservation**. Provider reconciliation, decision policy, receipt truth, or
expense evidence may remain available as headless capabilities without keeping
a Booking workspace, Proposal Detail screen, Decision Deck, or Costs ledger in
the active product. Git history is the archive; canceled source should not stay
inside the active tree where it continues to tax agents, dependencies, QA, and
the design system.

This roadmap operationalizes three existing decisions:

- the [Experience Constitution and Interaction Grammar](vesper-experience-constitution-and-interaction-grammar-2026-08-22.md);
- the [Canonical Product Journey Families](canonical-product-journey-families-2026-08-22.md); and
- the accepted decision to [separate systematic architecture from product proof](../decisions/2026-08-23-separate-architecture-from-product-proof.md).

It also incorporates the implementation findings and migration constraints in
the [Thesis Migration Register](thesis-migration-register-2026-08-21.md) and
the target ontology in the backend
[Clean-Break Experience Graph](../../travel-agent/docs/architecture/clean-break-experience-graph-2026-08-21.md).

## 2. Roadmap thesis

The engineering thesis is:

> One durable authority per canonical product noun, shared engines for
> interpretation and action where repeated use earns them, and a small number
> of viewer-relative projections expressed primarily through roots and typed
> conversational artifacts.

A movie ticket, menu, dinner invitation, disrupted Trip, local walk, shared
photo, and prior book passage should invoke different combinations of the same
engines. They must not create seven custody paths, seven memory stores, seven
group models, or seven receipt grammars.

The target product sentence remains:

```text
An Initiator causes a Person to perform a Verb
on an Object for an Immediate Job,
within a Moment, Scope, and relationship context.

Vesper chooses a Treatment,
which may produce an authorized Consequence,
an inspectable Receipt,
and an optional future Continuation.
```

The target runtime sentence is:

```text
source or question
  -> authorized context
  -> judgment and treatment
  -> optional command
  -> canonical consequence
  -> durable receipt and owner readback
  -> occurrence and personal outcome
  -> later relevant continuation or deliberate silence
```

## 3. Architectural laws

These laws apply across every milestone and workstream.

### 3.1 One durable owner

Every durable noun has exactly one canonical writer. Several surfaces may
project or link to the object, but no surface owns a shadow copy.

### 3.2 Surfaces project; commands mutate

Home, Vesper, Places, Life, Chat cards, notifications, and direct links are
projections and interaction surfaces. Mutations go through capability-checked
domain commands or application gateways.

### 3.3 Vesper interprets and facilitates; it does not own all truth

Vesper may resolve ambiguity, assemble private context, propose action, and
invoke authorized commands. It must not directly write domain tables or become
the durable owner of Places, Plans, Occasions, Commitments, or Outcomes.

### 3.4 Context is field-scoped and expiring

Every contextual field has provenance, audience, freshness, and purpose. The
absence of authorized context remains unknown rather than being inferred.

### 3.5 Authority is task-scoped

Approving an option does not imply permission to contact, commit, pay, retry,
publish, remember, or infer. Each consequential step names its authority.

### 3.6 Shared truth does not erase plural truth

An Occasion or Commitment may have one shared status. Personal constraints,
interpretations, and Outcomes remain viewer-relative unless explicitly shared.

### 3.7 Every mutation is replayable and inspectable

Commands are revision-checked, capability-checked, idempotent, and
receipt-backed. Cross-domain delivery uses an outbox or an equally durable
repair mechanism.

### 3.8 Correction crosses projections

A correction to Place identity, artifact interpretation, participation,
occurrence, outcome, visibility, or authority must invalidate every projection
that derived from the incorrect claim.

### 3.9 Silence is a valid result

Unknown, defer, expire, withdraw, and deliberate silence are first-class
outputs. Relevance alone does not justify an Opening or notification.

### 3.10 Architecture, implementation, human value, and release remain separate

A coherent schema is not a shipped experience. A passing test is not human
value. A successful human study is not production safety. Each gate retains its
own evidence.

### 3.11 A capability does not earn a screen

A durable object, API, state machine, or provider integration does not by
itself justify a route or workspace. The default projection for a bounded
question, proposal, invitation, decision, provider handoff, status, or receipt
is a typed artifact in the relevant conversation. An artifact may expand in
place or into a focused sheet while retaining one canonical resource identity.

A standalone screen must pass at least one admission test:

- sustained spatial navigation is intrinsic to the job;
- the person repeatedly manages many durable objects at once;
- safe action requires dense comparison that cannot remain legible in an
  artifact or focused sheet;
- the surface owns important account, privacy, correction, or recovery
  controls; or
- the surface is an approved primary product root.

Absent one of these conditions, new routes are denied by default.

### 3.12 Artifacts carry experience; authorities carry truth

Chat artifacts are durable, viewer-relative projections over canonical state,
not unstructured AI output or miniature shadow applications. Every actionable
artifact names a canonical `ResourceRef`, current revision, allowed actions,
audience, lifecycle state, and receipt/readback identity. Actions invoke domain
commands; refreshed artifacts read canonical owner state.

Avoid a universal server-driven UI schema. Start with a small typed family—such
as Place, Plan/Occasion, invitation, decision, provider handoff/status,
receipt, and correction—and add a type only when a real journey cannot compose
the existing grammar.

## 4. Current implementation baseline

The codebase currently contains four architectural layers:

```text
1. Mature travel operating system
   Trip · itinerary · proposals · booking · expenses · maps · movement
   provider reconciliation · notifications · memory · social circles

2. Mature conversational doorway
   Vesper Chat · text/images · pending-turn outbox · agent tools
   durable conversations · streaming · typed cards · action resolver

3. New experience substrate
   Intake v2 · custody · semantic candidates · graph anchors
   Plan/Occasion/Commitment graph · relationship handoffs · graph receipts

4. August product doctrine
   Home / Vesper / Places / Life
   immediate job -> treatment -> consequence -> receipt -> continuation
   multiple multiplayer modes · governed custody · second occasions
```

The newer systems are not completely isolated. A partial directed chain exists:

```text
custodied artifact
  -> graph anchor/projection
  -> Plans or Places summary
  -> Vesper context seed
  -> durable multiplayer card/action
  -> graph mutation and surface invalidation
```

However, runtime truth is still split. The principal seams are:

- Vesper input and OS-share Intake are separate admission systems;
- the clean graph created a second `world_entities` identity system without a
  mounted bridge to the existing Place authority;
- Trip proposals, Social Circles, standalone conversations, graph Occasions,
  and relationship handoffs provide overlapping multiplayer authorities;
- mature booking/provider truth does not update graph Commitments;
- mature notification delivery does not consume graph Openings as typed
  destinations;
- profile memory, saved Places, Atlas-compatible memory, Social Circles, and
  graph Outcomes are not one Life/continuity read model;
- server graph receipts and local cross-surface consequence banners do not
  share one durable readback identity; and
- the August four-root shell is not mounted. The app still exposes Plans,
  Vesper, and Places.

The roadmap must converge these authorities through adapters before deleting
working systems.

### 4.1 Presentation and attention burden

The mobile repository currently contains 188 route files, including 155 outside
the development-only route tree, and 58 registered visual-QA surfaces. Several
legacy workflow families impose disproportionate product and maintenance cost:

- the standalone Booking route is roughly 1,487 lines before its components,
  tests, fixtures, design references, and galleries;
- the expense route family is roughly 1,181 lines before its component and QA
  systems;
- Booking, Expense, Proposal Detail, and Decision Deck contain 46 dedicated
  component files; and
- hidden compatibility routes remain visible to search, agents, route
  ownership, component catalogs, dependency updates, and design audits even
  when they are absent from the tab bar.

Hiding is therefore not retirement. A canceled surface must leave the active
route tree, registries, tests, fixtures, design references, and component graph.
Its required capabilities may remain behind typed ports until they are adopted
or retired separately.

## 5. Durable domain authorities

Durable domain authorities own facts and lifecycle. They should remain modular
packages inside the current FastAPI/Postgres application unless operational
evidence later justifies a service boundary.

### 5.1 World authority

**Owns**

- canonical Place/world-entity UUID;
- external identities and redirects/merges;
- geometry and spatial hierarchy;
- source-bound facts and observations;
- entity readiness and evidence quality; and
- current provider/world conditions through typed observations.

**Does not own**

- personal familiarity;
- a person's interpretation of a Place;
- group commitment to visit;
- provider reservation state; or
- editorial projection for a particular surface.

**Primary journeys:** CJ02-CJ05, CJ14, CJ17-CJ18.

**Current assets:** existing Place/entity resolution, venues/sites, CityPack,
Mapbox/routing, weather, availability, source observations.

**Required convergence:** decide whether existing Place identity remains
canonical or define a real bidirectional identity bridge. Do not allow the
clean graph's `world_entities` to remain an ungoverned parallel identity.

### 5.2 Source authority

**Owns**

- artifact/source identity;
- byte and payload custody;
- hashes and idempotency;
- scanning and normalization;
- source observations and evidence locators;
- interpretation candidates and user correction;
- retention, expiry, deletion, and custody receipts; and
- lineage from source to derived claims.

**Does not own**

- whether an interpretation becomes a Plan, Occasion, Commitment, or memory;
- whether an artifact implies attendance, preference, or authorship; or
- who may see a projection beyond the explicitly granted audience.

**Primary journeys:** CJ01, CJ05-CJ06, CJ09, CJ16-CJ18.

**Current assets:** Intake v2, share capture, screenshot ingestion, URL
retrieval, audio transcription, email forwarding, semantic review, graph-anchor
projection.

### 5.3 Relationship authority

**Owns**

- people and relationship references;
- pair and recurring-circle identity;
- addressability and audience membership;
- relationship-scoped capabilities;
- invitation reachability where it precedes an Occasion; and
- viewer-relative relationship projections.

**Does not own**

- Occasion participation merely because someone belongs to a Circle;
- private relationship scoring;
- synthetic group personality; or
- shared Outcomes.

**Primary journeys:** CJ07-CJ13, CJ17-CJ18.

**Current assets:** contacts/people, follows, Social Circles, pair
conversations, relationship handoffs, Trip membership adapters.

### 5.4 Plan authority

**Owns**

- one person's sparse horizon of intent;
- Plan kind and lifecycle;
- relations among personal Plans; and
- references to possible Places, Occasions, and Commitments.

**Does not own**

- shared status;
- provider truth;
- occurrence; or
- another person's horizon merely because two Plans overlap.

**Primary journeys:** CJ06, CJ10, CJ14-CJ15, CJ17.

**Current assets:** clean graph Plan plus mature Trip/itinerary projections.

### 5.5 Occasion authority

**Owns**

- bounded lived context;
- purpose, horizon, and lifecycle;
- membership, roles, and participation status;
- invitations;
- decisions and decision policy;
- responsibilities and organizer transfer;
- links to sources, Plans, Commitments, and occurrences; and
- the shared portion of an Occasion's aftermath.

**Does not own**

- every participant's private constraint;
- personal meaning or memory;
- a recurring relationship or Circle by default; or
- provider execution state.

**Primary journeys:** CJ08, CJ10-CJ14, CJ16-CJ17.

**Current assets:** graph Occasions/invitations/decisions, Trip rooms and
proposals, local Occasion experiments, composed cards.

### 5.6 Commitment authority

**Owns**

- the smallest authorized shared consequence;
- subject, Place, time, participants, controller, and revision;
- authorization envelope;
- execution and provider state references;
- dependencies and recovery posture; and
- one canonical shared status.

**Does not own**

- a person's intent before commitment;
- provider facts without evidence;
- attendance, enjoyment, or personal meaning.

**Primary journeys:** CJ10, CJ13-CJ16.

**Current assets:** Trip operation gateway, proposal apply engine, booking
provider sagas, graph Commitments and provider-evidence commands.

### 5.7 Lived-reality authority

**Owns**

- occurrence claims and evidence;
- happened, changed, missed, unfinished, unknown, and disputed states;
- Encounters;
- personal Outcomes;
- Place familiarity derived from authorized Encounters;
- correction of attendance, occurrence, and interpretation; and
- source-bound lineage into later continuity.

**Does not own**

- provider confirmation as proof of attendance;
- one group Outcome;
- automatic memory admission; or
- current interruption policy.

**Primary journeys:** CJ05-CJ06, CJ14, CJ16-CJ18.

**Current assets:** occurrence reconciliation, encounter outcomes, profile and
memory systems, Place relationships, graph Outcomes.

### 5.8 Attention authority

**Owns**

- Opening identity and lifecycle;
- initiator and evidence;
- intended recipient and audience;
- priority, expiry, urgency, and interruption eligibility;
- available reactions;
- response state; and
- the durable decision to defer, withdraw, or remain silent where evidence is
  required.

**Does not own**

- notification delivery mechanics;
- canonical Place, Occasion, or Commitment state;
- the content of every response; or
- permanent personalization merely because an Opening was shown.

**Primary journeys:** CJ03, CJ07-CJ08, CJ14, CJ17-CJ18.

**Current assets:** clean graph openings, Lived Experience OpeningRequest and
treatment contracts, proactive decisioning, notification/Activity outcomes.

## 6. Cross-domain product engines

Cross-domain engines compose authorities into useful journey sentences. They
use typed ports, domain commands, and outbox events. They must not introduce
parallel durable nouns.

### 6.1 Universal Admission Engine

**Purpose:** accept whatever already has the person's attention, determine the
immediate job, establish safe custody, and create only the continuity the person
authorizes.

**Inputs**

- text and questions;
- photographs and screenshots;
- tickets, menus, receipts, reservations, and generic files;
- URLs;
- voice;
- invitations and messages;
- provider records; and
- explicit Place or location context.

**Canonical sequence**

```text
input
  -> stable admission identity
  -> custody and normalization
  -> immediate-job determination
  -> context request
  -> treatment
  -> optional retention, action, or continuation
```

**Required contracts**

- `SourceRef`: stable source/submission/artifact identity shared by Intake,
  Chat, anchors, commands, and receipts;
- `AdmissionEnvelope`: actor, origin, audience, source kind, idempotency key,
  immediate context, and requested handling;
- `ImmediateJob`: answer, decode, orient, compare, act, preserve, address,
  reconcile, or clarify;
- `AdmissionResult`: answer/treatment, custody state, proposed consequence,
  continuation, correction entry, and expiry; and
- a durable client/server admission outbox for process-death recovery.

**Build or converge**

- bind Vesper pending turns to Intake submissions/source objects;
- make first-turn tool selection sensitive to attachments, not only text;
- add stable idempotency for raw text and audio share intents;
- reopen the originating Vesper context after OS share capture;
- ensure immediate answer and later retention reuse one admitted source; and
- separate immediate utility from optional semantic organization.

**Must never happen**

- upload becomes filing homework;
- classification is required before useful help;
- Chat and Intake process the same bytes into unrelated source records;
- custody implies memory, attendance, preference, or sharing; or
- a failed client render loses an already-admitted source.

**Journey coverage:** CJ01-CJ02, CJ05-CJ06, CJ09, CJ16-CJ18.

### 6.2 Context and Situation Engine

**Purpose:** assemble only the fresh, authorized context capable of changing
the present answer or action.

**`ContextManifest` fields**

- viewer, actor, initiator, and audience;
- current Place and confidence;
- time, local time, and temporal horizon;
- movement and route state;
- weather, heat, accessibility, energy, and crowd conditions;
- people present, participating, or addressed;
- active Occasion and Commitments;
- relevant prior Encounters or Outcomes;
- fresh provider facts;
- attention state and interruption budget; and
- provenance, TTL, visibility, and purpose for every field.

**Provider ports**

- World/Place resolver;
- location and movement;
- routing and spatial-cost policy;
- weather and environmental conditions;
- provider availability/state;
- relationship and audience projection;
- Plan/Occasion/Commitment projection; and
- continuity admission.

**Design rules**

- unknown remains unknown;
- private context may affect feasibility without entering the explanation;
- stale provider facts are labelled or withheld;
- a ContextManifest is bounded to one treatment/command purpose; and
- the AI sees the minimum fields required for the job.

**Journey coverage:** CJ02-CJ05, CJ07, CJ10, CJ12, CJ14-CJ17.

### 6.3 Judgment and Treatment Engine

**Purpose:** decide the appropriate kind, timing, depth, and consequence of
help. It is not merely a response generator.

**Treatment vocabulary**

- answer directly;
- orient or route;
- reveal one useful distinction;
- ask a clarifying question;
- render a compact artifact;
- propose keeping or connecting;
- propose a Move, Plan, Occasion, or Commitment;
- privately suggest addressing someone;
- create an Opening;
- defer or withdraw; and
- deliberately remain silent.

**Treatment decision record**

- immediate job;
- authorized evidence/context used;
- treatment and depth;
- why this treatment and why now;
- intended audience;
- consequence capability;
- owner destination;
- expiry; and
- silence/defer alternative.

**Convergence responsibility**

The older Lived Experience decision and treatment contracts should become a
bounded application-level judgment engine. They should not remain a third
canonical source of Plans, Openings, or receipts.

**Journey coverage:** CJ01-CJ08, CJ10, CJ12, CJ14, CJ17-CJ18.

### 6.4 Action and Consequence Gateway

**Purpose:** provide one authorization, idempotency, revision, execution, and
receipt boundary for consequential changes.

**`CommandEnvelope`**

```text
command_id
actor and viewer scope
target ResourceRef
command type
required capability
expected revision
idempotency key
source/evidence references
audience
authorization scope
reversibility/recovery policy
```

**`ActionReceipt`**

```text
receipt_id
command_id
actor and audience
canonical target ResourceRef
what changed
before/after revision
source/evidence references
execution state
reversibility/recovery state
owner destination
delivery/readback state
created/settled timestamps
```

**Adapters rather than rewrites**

- Trip operation gateway;
- proposal resolution and consensus apply;
- graph commands;
- Occasion collaboration commands;
- booking/provider operations;
- relationship handoffs; and
- occurrence reconciliation.

Vesper, Chat cards, Home, Places, Life, and notifications may invoke the
gateway. None may bypass the canonical domain writer.

**Journey coverage:** CJ06, CJ09-CJ18.

### 6.5 Attention and Delivery Engine

**Purpose:** decide whether an authorized Opening should reach a person now,
later, in a quieter surface, or not at all, then deliver it through existing
infrastructure.

**Opening contract**

- initiator: person, Vesper, provider, or changing world;
- evidence and reason;
- intended recipient/audience;
- Place, Moment, and Occasion relevance;
- urgency and interruption eligibility;
- available actions;
- expiry and freshness;
- status: proposed, eligible, visible, opened, snoozed, dismissed, muted,
  withdrawn, expired, or acted; and
- canonical target and receipt references.

**Delivery arbiter outputs**

```text
show now in current surface
project on Home
append to Activity
deliver into private/group Chat
send push
wait for a better moment
expire or withdraw silently
```

**Required convergence**

- graph openings;
- Lived Experience treatments;
- proactive decisioning;
- notification delivery and outcomes;
- Activity;
- Home projection; and
- composed Chat cards.

Typed notification destinations must exist for Opening, Occasion invitation,
decision, relationship handoff, Commitment, and receipt—not only generic Chat.

**Journey coverage:** CJ03, CJ07-CJ08, CJ11-CJ12, CJ14, CJ17-CJ18.

### 6.6 Multiplayer Facilitation Engine

**Purpose:** help people share attention, participate, decide, and coordinate
without flattening private information, distinct perspectives, or decision
rights.

**Supported modes**

- co-present shared attention;
- borrowed perception;
- asynchronous addressed attention;
- host-mediated attention;
- governed joint decision; and
- living ritual.

**Decision-policy vocabulary**

- ordinary preference;
- hard feasibility constraint;
- safety constraint;
- veto;
- expertise-weighted input;
- organizer authority;
- delegated authority;
- unanimous commitment; and
- advisory input.

**Required capabilities**

- pair, group, Circle, and Occasion audiences;
- addressed handoff creation and recipient action;
- invitations and tentative participation;
- private constraints and group-safe synthesis;
- decisions and current-vote resolution;
- task claims, ownership, and transfer;
- organizer nomination/transfer;
- personal variations; and
- separate personal Outcomes after shared action.

**Reuse**

- Trip membership and capability projections;
- proposals and voting;
- Social Circles;
- private/group conversations;
- composed-card resolver;
- graph Occasion invitations/decisions; and
- relationship handoffs.

**Required convergence**

- one canonical audience/relationship reference;
- declared adapters among Circle, Trip, conversation, and Occasion membership;
- sender-side product journeys, not receiver-only transport;
- one durable Together projection; and
- no synthetic group personality as authority.

**Journey coverage:** CJ07-CJ15, CJ17-CJ18.

### 6.7 Continuity and Reactivation Engine

**Purpose:** decide when authorized prior experience may materially improve the
present job without turning retention into compulsory resurfacing.

**Admission rule**

```text
authorized prior Encounter or Outcome
  + semantic relevance
  + current situational relevance
  + a present job it can materially change
  = admissible reactivation
```

**Separate controls**

- retain raw source;
- retain interpretation;
- permit future inference;
- connect to Place/person/Occasion;
- record personal Outcome;
- share selected Outcome;
- allow reactivation;
- enter dormancy;
- correct; and
- forget/release.

**Required convergence**

This engine must adapt or converge profile memory, saved Places, Place
familiarity, Atlas-compatible memory, Social Circle shared claims, and graph
Outcomes. It must not create a fifth accumulation store.

**Journey coverage:** CJ05-CJ06, CJ08, CJ16-CJ18.

### 6.8 Projection, Artifact, and Destination Engine

**Purpose:** render canonical facts for the current viewer and give every
durable object an inspectable owner projection without assuming that every
object deserves a standalone screen.

**Canonical `ResourceRef` kinds**

- Place;
- source/artifact;
- person/relationship/Circle;
- Plan;
- Occasion;
- Commitment;
- Opening;
- Encounter/Outcome; and
- receipt.

**Four-root projections**

| Root | Human question | Projection responsibility |
|---|---|---|
| Home | What matters now? | Openings, active Occasions, invitations, returns, actionable changes, and intentional quiet |
| Vesper | What can I ask, show, or work through? | Universal admission, private/group interpretation, facilitation, proposals, and compact receipts |
| Places | What is around me and how can I experience it? | Canonical Place identity, spatial exploration, terrain/conditions, practical and cultural legibility, familiarity, and horizons |
| Life | What is accumulating for me and between us? | Mine/Together Encounters, artifacts, threads, Outcomes, people, Occasions, correction, forgetting, and privacy |

Plans and Occasions remain canonical destinations reachable from all four roots.
They need not remain a fifth root. Home must expose an obvious “All plans and
occasions” destination before the current Plans root is removed.

The owner projection may be one of:

- an artifact anchored to its canonical conversation;
- an inline-expanded artifact or focused sheet;
- a compact owner-state projection on Home or Life;
- a primary-root workspace such as Places when the task needs spatial depth;
- an account/privacy control surface; or
- an external provider handoff with a durable return receipt.

Deep links target the resource and preferred projection, not an implementation
assumption that the resource owns a page. Opening a Decision may navigate to
the group conversation and focus its decision artifact; opening a provider
status may focus the relevant handoff receipt. Summary-to-Chat is not a lossy
fallback when the anchored artifact is itself the canonical viewer-relative
projection over durable owner state.

**Initial typed artifact family**

- answer/opening;
- Place or situated distinction;
- Plan/Occasion summary;
- invitation and participation;
- decision and bounded vote;
- provider handoff/status;
- action/correction receipt; and
- personal or shared Outcome.

These artifacts share a small interaction grammar—inspect, choose, authorize,
correct, undo, open owner, or hand off—without sharing one undifferentiated
payload or allowing the renderer to mutate domain state directly.

**Journey coverage:** all CJ families.

### 6.9 Receipt, Correction, and Evidence Engine

**Purpose:** provide one user-facing and operational truth about what was
attempted, changed, delivered, observed, corrected, or reversed.

**Must converge**

- graph action receipts;
- legacy Vesper/Plan receipts;
- Intake lifecycle receipts;
- notification outcomes;
- provider operation receipts;
- occurrence/outcome receipts; and
- local consequence banners.

The same receipt identity should survive:

```text
command
  -> transaction
  -> outbox
  -> delivery/card
  -> owner-surface readback
  -> Activity
  -> account export
  -> reversal, correction, or terminal recovery
```

The engine also owns content-safe whole-loop telemetry. Operational tracing may
record identifiers, states, timing, and bounded reason codes; it must not log
private message or artifact contents.

**Journey coverage:** CJ01, CJ06-CJ07, CJ09-CJ18.

## 7. Shared platform rails

Every domain authority and application engine uses the same rails.

### 7.1 Authority and privacy rail

- authentication and canonical owner identity;
- actor/viewer/initiator/audience distinction;
- capability projection;
- membership epochs and stale-membership rejection;
- private constraints and minimum-safe shared projection;
- retention, inference, sharing, and reactivation scopes;
- account export and deletion;
- correction, release, and revocation; and
- residual-reference and blob/vector cleanup.

### 7.2 Transaction and event rail

- expected revisions;
- idempotency keys;
- transactional outbox;
- consumer inbox and deduplication;
- repair/replay workers;
- canonical `ResourceRef`;
- cross-domain event vocabulary;
- schema/metadata registration; and
- bounded saga state for provider operations.

### 7.3 Contract and reachability rail

- registered routes;
- generated OpenAPI and mobile types;
- explicit data-facade consumers;
- mounted production surfaces;
- typed deep-link destinations;
- mock honesty; and
- retirement/unreachability proof.

Contract governance must distinguish five separate gates:

```text
persisted model
registered route
generated client contract
production caller
mounted/reachable surface
```

Passing an API audit does not imply the final two gates.

### 7.4 Evidence and rollout rail

- registered and enforced flags only;
- environment/cohort rollout state;
- exposure and mutation telemetry;
- product-proof and assurance-journey linkage;
- deployment/release hash;
- rollback posture;
- device and two-account evidence; and
- human outcome evidence kept separate from implementation evidence.

## 8. Journey-to-engine coverage matrix

Legend: **P** = primary engine, **S** = supporting engine.

| CJ | Admission | Context | Treatment | Action | Attention | Multiplayer | Continuity | Projection | Receipt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CJ01 Bring a fragment | P | S | P | S |  |  | S | S | P |
| CJ02 Ask about lived world | S | P | P |  |  |  | S | S | S |
| CJ03 Explore |  | P | P |  | P |  | S | P | S |
| CJ04 Orient and move | S | P | P | S | S | S | S | P | S |
| CJ05 Notice/gain capability | P | P | P | S | S | S | P | S | S |
| CJ06 Keep/connect | P | S | S | P |  |  | P | S | P |
| CJ07 Receive/react |  | S | S | S | P | S |  | P | P |
| CJ08 Address a person | S | S | P | S | P | P | S | S | P |
| CJ09 Share/publish/contribute | P | S | S | P | S | P | S | P | P |
| CJ10 Shape minimum structure | S | P | P | P | S | P |  | P | P |
| CJ11 Invite/join/leave |  | S | S | P | S | P |  | P | P |
| CJ12 Decide together |  | P | P | P | S | P |  | P | P |
| CJ13 Coordinate/delegate |  | S | S | P | S | P |  | P | P |
| CJ14 Live/adapt |  | P | P | P | P | S | S | P | P |
| CJ15 Execute/reconcile |  | P | S | P | S | S |  | P | P |
| CJ16 Mark what happened | S | P | S | P | S | S | P | P | P |
| CJ17 Earned return |  | P | P | S | P | S | P | P | P |
| CJ18 Correct/release/forget | S | S | S | P | P | S | P | P | P |

This matrix is a design check, not an implementation claim. Each engine earns
its existence by serving several journeys or by protecting a cross-cutting
invariant such as privacy, authority, identity, or correction.

## 9. Dependency graph

```text
M-1 Surface cancellation + attention reset
  |
  v
M0 Authority and trust truth
  |
  v
M1 Minimum command / receipt seam exercised by one artifact loop
  |                      |                      |                      |
  +----------------------+-----------+----------+----------------------+
  |                      |                      |                      |
  v                      v                      v                      v
M2 Admission +       M3 Relationships +     M4 Attention +       M5 Optional
   Context              Occasions              Delivery              execution adapter
                                     |
                                     v
                          M6 Coherent projections
                   roots / anchored artifacts / focused sheets
                                     |
                                     v
                  M7 Continuity + authority retirement
```

The arrows describe the recommended *future* sequencing, not a historical
dependency. M0 authority and trust work was deliberately executable
independently of surface contraction and is already landed in the workspace;
M-1 is the next product-surface decision that should shape subsequent product
and architecture work. M-1 removes obsolete presentation before it can shape
later architecture. M2-M4
may proceed in parallel after one real M1 artifact loop proves the minimum
shared seam. M5 is optional until a retained experiential loop requires first-
party execution. M6 projection components are exercised incrementally during
M2-M4, but the root-shell cutover waits until their authorities and destinations
are real.

## 10. Milestone roadmap

The milestones are dependency-ordered, not calendar commitments. Staffing and
the number of safe parallel worktrees determine elapsed time.

### M-1 — Contract the surface area and reset engineering attention

**Objective:** remove product destinations that no longer express the August
direction before their assumptions, fixtures, and polish requirements shape
the new architecture.

This milestone may delete presentation while preserving headless capability.
It does not authorize destructive database or backend-authority deletion.

**Surface classification**

Every non-development route is classified as exactly one of:

```text
root
focused_workspace
artifact_or_sheet
external_handoff
compatibility_redirect
retire
```

Extend the existing route-ownership and canonical-entry registries with this
lifecycle instead of creating another independent surface inventory.

**Initial disposition**

| Surface family | Product disposition | Capability disposition |
|---|---|---|
| Proposal Detail | Retire after deep links reliably focus the group-chat decision artifact | Keep decision policy, revisions, voting, mutation, and receipts |
| Decision Deck | Retire as product direction; remove the dev gallery after retained artifact primitives have coverage | Extract only primitives used by the typed artifact family |
| Booking workspace | Replace with provider handoff/status artifacts and external checkout; retain only a bounded compatibility redirect during cutover | Keep provider adapters, task-scoped authority, ambiguous-state reconciliation, and receipts |
| Expense ledger, balance, add/edit, and detail screens | Retire from the active product unless a later founder decision makes shared money management core | Keep receipt understanding or source evidence only when a retained artifact uses it; quarantine the rest |
| Trip/Plan operational workspace | Keep temporarily as a focused workspace while Plan/Occasion projection is decided | Keep the current canonical writer until a tested replacement exists |
| Home/Vesper/Places/Life hypotheses | Develop only through approved roots and representative artifacts; do not generate one page per noun | Read canonical viewer-relative projections |

**Deliverables**

1. Create and push an archive tag for the pre-contraction app state. Do not move
   canceled source into `archive/`, `legacy/`, `attic/`, or another active-tree
   folder.
2. Add lifecycle, replacement, retained-capability, and deletion-gate fields to
   route ownership.
3. Redirect proposal, booking, push, search, and notification entries to the
   appropriate conversation artifact, focused workspace, or external provider.
4. Delete canceled route registration, screens, components, screen-specific
   hooks, visual-QA entries, goldens, fixtures, Maestro flows, design references,
   component-catalog rows, and tests that no longer protect retained behavior.
5. Preserve or rewrite tests for headless authority, artifact rendering, action
   mutation, readback, recovery, privacy, and correction.
6. Add CI guards for route budget, retired route existence, imports from retired
   component families, and retired surfaces remaining in design/QA registries.
7. Record one compact tombstone per retired family: archive ref, replacement,
   retained capability, and reintroduction criterion.
8. Recalculate the required M1-M7 engines after surface contraction; remove
   engines or deliverables that no retained human-experience loop exercises.

### M-1 execution status and closure — 2026-08-23

| Work item | Status | Evidence / boundary |
|---|---|---|
| Product classification fields | Landed | `travel-app/scripts/polish-qa/surfaces.mjs`, canonical entry-point inventory, and route-owner metadata now share the six-class vocabulary. |
| Mechanical reintroduction guard | Landed and freshness-bound | `travel-app/scripts/check-surface-contraction.mjs` now runs the route generator in `--check` mode before evaluating ownership, so a newly mounted route cannot be hidden by a stale committed inventory. |
| Decision Deck presentation | Retired | `/dev/deck-gallery`, gallery fixtures, baselines, Maestro flows, gallery-only test, and active design/QA rows removed; retained Deck primitives and headless tests remain. |
| Proposal Detail | Compatibility redirect | Normal deep links focus the group-chat decision artifact; inspect/recovery remains bounded and receipt-backed. |
| Booking | External handoff | Booking remains during cutover as a bounded provider utility; replacement is a provider handoff/status artifact plus external checkout. |
| Expenses | Compatibility redirect | Existing writers and screens remain until an artifact replacement or explicit founder-approved money-management decision. |
| Archive / tombstone | Landed and published | App tag `m1-pre-contraction-2026-08-23` is published on `fy538/travel-app`; [M-1 register](m1-surface-contraction-register-2026-08-23.md) records the tombstone and reintroduction rule. |

#### Exit-gate receipt

| Exit criterion | Status | Evidence |
|---|---|---|
| Every production route has an approved classification | **Pass** | Generated inventory contains 181 routes; every route is owned or explicitly exempt, and `npm run surface:contraction:check` first rejects a stale inventory. The canonical artifact reader is explicitly `artifact_or_sheet`. |
| Proposal/voting uses the Chat artifact normally | **Pass** | `routes.tripChatProposal`, `/trip-proposal` inspect/recovery behavior, and `trip-proposal-inspect`, shared-proposal, and journey tests. |
| No canceled surface remains in active polish/design work | **Pass** | Decision Deck gallery route, fixtures, baselines, Maestro flows, screen test, contract, and registry rows are removed; the guard rejects their return. |
| Booking and Expenses have explicit dispositions | **Pass** | Booking is `external_handoff`; all Expense routes are `compatibility_redirect` with replacement, retained capability, and deletion-gate metadata. |
| Deep links and in-flight operations fail safely | **Pass for retained cutover paths** | Proposal inspect fallback, booking return-token/provider-saga routes, notification destinations, and journey 03/22 tests pass. |
| No retained domain writer was deleted | **Pass** | M-1 changed the mobile presentation and workspace governance only; no backend authority or writer was removed. |
| CI prevents reintroduction | **Pass** | Reliability workflow runs `surface:contraction:check`; guard checks routes, retired assets, and active QA/design registries. |

M-1 is closed. The next milestone is M1: prove the minimum command, receipt,
and delivery seam through one retained artifact loop. Booking and Expenses are
intentionally still present as bounded cutover surfaces; closing M-1 does not
claim their future replacement is complete.

**Exit gate**

- every production route has an approved surface classification;
- proposal/voting uses the chat artifact as its normal destination;
- no canceled surface remains in active visual-polish or design-system work;
- booking and expense presentation have an explicit retire, redirect, or
  founder-approved keep decision;
- deep links and in-flight operations fail safely through replacements;
- no retained domain writer was deleted merely because its screen disappeared;
  and
- CI prevents accidental reintroduction of canceled routes and imports.

### M0 — Restore authority and trust truth

**Objective:** remove contradictions that make expansion unsafe or make runtime
state differ from governance claims.

M0 is an independent trust prerequisite, not a gate on the M-1 surface reset.
It was executed in parallel with the documentation and product-surface
reconciliation work above; its exit gate is met. The M-1 ordering shown in the
dependency graph governs what we do next, not whether the completed M0 work was
valid.

**Deliverables**

1. Enforce owner privacy in legacy Trip receipt queries and serialization.
2. Add Experience Graph and Relationships metadata to account export,
   deletion, residual-reference auditing, and tests.
3. Define shared Occasion deletion and organizer-transfer policy.
4. Decide canonical Place identity and record an ADR.
5. Audit and repair the graph-to-Place identity seam.
6. Remove, implement, or enforce the phantom `SOCIAL_CIRCLES_ENABLED` policy.
7. Register every runtime feature flag and classify its audience/owner.
8. Refresh current-state generated counts and stale feature documents.
9. Repair the stale Lived Experience family-count expectation.
10. Create the canonical authority register for World, Source, Relationship,
   Plan, Occasion, Commitment, Lived Reality, Attention, and Receipt.
11. Add a CI reachability report covering the five contract gates.

### M0 execution status — 2026-08-23

| Work item | Status | Evidence |
|---|---|---|
| Legacy Trip receipt viewer privacy | Landed | `backend/core/db/action_receipts.py`, route viewer scoping, focused tests |
| Graph/relationship account lifecycle registration | Landed and membership-traversed | Registry integration plus explicit Commitment-participant traversal: exports include membership-owned Commitment/evidence rows, solo Commitments cascade, shared Commitments detach the departing person and transfer external-link control, and issued personal capabilities are destroyed. |
| Shared graph Occasion creator succession | Landed and Postgres-proven | `account_deletion.py` successor policy plus graph/relationship export/deletion fixture |
| Lived Experience family-count drift | Landed | gateway registry test now covers all nine declared routes |
| Social Circle policy flag | Landed | registered default-on kill switch, router dependency, fail-closed API test |
| Runtime flag registry truth | Landed | five previously unregistered/deprecated symbols classified; flag gate green |
| Current-state generated signals | Landed | `docs/status/current-state.md` refreshed from registries |
| Place/graph identity authority | Landed and focused-tested | `identity_bindings.py`, `xgraph16_identity_binding_ledger.py`, projection/anchor public reads hide graph UUIDs and expose canonical refs/status |
| Canonical authority register | Landed as working authority | [authority register](canonical-authority-register-2026-08-23.md) |
| Five-gate reachability report | Landed | `make m0-reachability-report` |

The M0 trust gate is met. The next hardening work belongs to M1: backfill only
reviewed high-confidence bindings, add deep-link/correction parity tests for
each canonical consumer, extend the Postgres lifecycle fixture as graph tables
land, and keep the reachability report wired to the CI workflow that owns the
cross-repo verification gate. The authority seam itself is no longer pending:
unresolved graph candidates fail closed at public projection and anchor reads.

**Exit gate**

The M0 decision and register artifacts are now tracked in the [canonical Place
authority bridge ADR](../decisions/2026-08-23-canonical-place-authority-bridge.md)
and the [canonical authority register](canonical-authority-register-2026-08-23.md).
The five-gate executable report is `make m0-reachability-report`.

- private receipts cannot cross viewer boundaries;
- every new-domain user record appears in export/deletion tests;
- shared Occasion deletion behavior is explicit and tested;
- one Place identity is authoritative or a tested bridge has been accepted;
- every claimed rollout flag exists and is enforced; and
- every canonical noun has one declared durable writer.

### M1 — Prove the minimum command, receipt, and delivery seam

**Objective:** make one representative conversational artifact compose through
a trustworthy authority and reliability boundary, then generalize only the
parts required by a second materially different loop.

M1 is not permission to build a universal platform rail in anticipation of all
CJ01-CJ18 journeys. Existing gateways remain valid adapters until an exercised
loop proves that a smaller shared contract should replace them.

**Deliverables**

1. Canonical `ResourceRef` vocabulary and resolver.
2. Canonical `CommandEnvelope`.
3. Canonical durable `ActionReceipt`.
4. Transactional outbox and consumer inbox/deduplication only for the selected
   loop where existing delivery cannot satisfy the recovery contract.
5. Repair/replay behavior and a minimal operator view for that loop.
6. Artifact anchor or other owner projection and readback state.
7. Capability/revision/idempotency helpers extracted from real adapter use.
8. Shared metadata/account-lifecycle registration for each new durable record.
9. One end-to-end adapter selected from an active human-experience loop; do not
   prebuild adapters for every legacy domain.
10. Cross-repo artifact, command, receipt, and deep-link types for the selected
   loop.

**Execution receipt (2026-08-23):** The seam is implemented over two existing,
materially different authorities. The first is the canonical itinerary
operation gateway: `ResourceRef`, `CommandEnvelope`, and `ActionReceipt` are
persisted through terminal operation evidence, backed by the existing
`vesper_action_receipts` row and transactional `itinerary_projection_outbox`.
The second is custody-first Intake v2: admission and owner deletion now expose
the same additive `canonical_execution` contract while retaining the existing
`intake_submissions`, lifecycle readback, source-scrub, and processing-outbox
authorities. Plan and share-capture owner readback, mobile generated types,
expired-lease repair/stale-worker fencing, and the admin-gated content-free
outbox diagnostic at `GET /admin/ops/itinerary-projection-outbox` are covered
by focused tests. See the detailed [M1 execution receipt](m1-command-receipt-delivery-execution-2026-08-23.md).

M1 is closed for local implementation. This proves the minimum shared seam,
not a universal platform rail: deployed process-death drills, worker cadence,
and live provider delivery remain operational evidence. M2 admission/context
work can proceed without adding another generic adapter.

**Exit gate**

One representative artifact command must be safely retryable; survive API/app
process death; repair delivery where delivery is durable; reappear at its
canonical conversation anchor or owner projection; retain a stable receipt
through readback; participate in export, deletion, correction, and reversal;
and expose content-safe telemetry. No additional generic rail is accepted
without a named second consumer.

### M2 — Unify admission and situated context

**Objective:** make one natural input power immediate utility and any later
authorized continuity.

**Deliverables**

1. Bind Vesper pending turns to Intake submissions/source objects.
2. Make first-turn multimodal selection attachment-aware.
3. Add stable idempotency and resumability for text/audio share intake.
4. Define and implement `AdmissionEnvelope`, `SourceRef`, `ImmediateJob`, and
   `AdmissionResult`.
5. Add `ContextManifest` and typed context-provider ports.
6. Route existing Place, time, movement, weather, people, Commitment, and
   provider context through the manifest.
7. Continue an OS share in the originating or newly created Vesper thread.
8. Show exact custody, interpretation, retention, and correction state.
9. Ensure immediate answer and later graph consequence share the same source
   lineage.
10. Mount bounded correction/release directly from the result and source
    destination.

**Execution receipt (2026-08-23):** M2 is closed for the first admitted-source
conversation seam. `AdmissionEnvelope`, `AdmissionResult`, and content-free
`SourceRef` transport ride the existing Intake v2 and pending-chat-turn
authorities. The pending route verifies actor-owned source refs; canonical send
materializes verified Intake images and follows verified audio parents to the
existing `derived_transcript` without a second Intake submission; the mobile
`from_chat=1` path stages the same source before entering Vesper; accepted,
cancelled, and expired rows retain only content-free receipts; and the
generated OpenAPI/mobile contract is synchronized. See the detailed
[M2 admission and situated-context receipt](m2-admission-situated-context-2026-08-23.md).

The existing `LivedExperienceEngine.compile_authority_context` and canonical
provider registry remain the single `ContextManifest` authority for a later
family opening. Generic pending chat intentionally carries source lineage but
does not fabricate a family or experience scope before that opening exists.
The next work is consequence-specific context, correction projection, and
deployed process-death/worker-cadence evidence—not another generic admission
rail.

**Portfolio coverage**

- screenshot or menu -> immediate answer;
- movie/book ticket -> identify and interpret without claiming attendance;
- ordinary situated question;
- practical distinction and optional keep;
- wrong interpretation correction; and
- answer-only expiry.

**Primary CJs:** CJ01-CJ06, CJ16, CJ18.

**Exit gate**

- the same admitted source powers answer and optional consequence;
- bytes are not independently re-ingested through Chat and Intake;
- process death does not duplicate or lose the admission;
- saving/retaining remains optional and scoped; and
- every result has a correction and expiry posture.

### M3 — Converge relationships, Occasions, and multiplayer

**Objective:** make addressing, participation, shared decisions, and
responsibility coherent across pairs, Circles, groups, and Occasions.

**Deliverables**

1. Canonical audience/person/relationship/Circle references.
2. Declared adapters among Circle, Trip, conversation, and Occasion membership.
3. Mounted sender-side relationship handoff.
4. Occasion creation from Vesper, Place, source, and relationship handoff.
5. Invitation inspection, tentative participation, accept/decline, leave,
   mute, and rejoin.
6. Decision-policy engine with explicit constraint/veto/expertise/delegation
   semantics.
7. Private-input and group-safe-synthesis contract.
8. Responsibilities, task claims, and organizer transfer.
9. Durable card-delivery outbox and repair.
10. One viewer-relative Together projection.
11. Two-account, stale-membership, replay, denial, and correction coverage.

**Portfolio coverage**

- “this made me think of you” addressed handoff;
- lightweight dinner invitation;
- local Occasion without a Trip;
- group choice with a private constraint;
- organizer delegation/transfer;
- late join, leave, and rejoin; and
- one shared action with separate personal Outcomes.

**Primary CJs:** CJ07-CJ13, CJ17-CJ18.

**Execution receipt (2026-08-23):** The bounded addressed-place multiplayer
loop is closed in code and mock read-after-write. Mobile joins viewer-relative
graph occasions to the existing Places/venue/site reader contract through the
backend-authorized typed `canonical_entity_ref`; it exposes revision-bound
private outcome correction; and the mock exercises handoff → shared Occasion
→ personal Outcome → correction. The backend regression proves that a place
opening does not infer Trip membership. See the detailed [M3 multiplayer loop
receipt](m3-multiplayer-loop-2026-08-23.md) and the [canonical place-reader
packet](m3-canonical-place-reader-2026-08-23.md).

This closes the first differentiated multiplayer product loop, not production
release. The dedicated mock/device Maestro flow now proves the mounted sender
composer, recipient private Outcome capture/correction, and sender privacy
boundary; serving flags remain off pending a signed-in two-account device walk.
Occasion attention/mute, responsibility claims, richer decision policy, and
explicit Trip promotion remain the next M3 program increments.

**Exit gate**

A sender can create an addressed opening; the recipient can inspect and act;
the shared mutation is revision-safe and durable; both participants see current
authorized shared truth; and no private rationale leaks into the shared
explanation.

### M4 — Unify Openings, delivery, and deliberate silence

**Objective:** create one attention runtime across proactive reasoning, graph
state, Chat, Home, Activity, and notifications.

**Deliverables**

1. One canonical Opening contract and lifecycle.
2. Migration/adapter plan for graph openings and Lived OpeningRequest.
3. Mounted accept, modify, snooze, dismiss, mute, release, and “why this”
   actions.
4. Treatment-versus-silence arbiter.
5. Typed notification destinations for Opening, Occasion invitation, decision,
   handoff, Commitment, and receipt.
6. Home and Activity projections over the same Opening authority.
7. Freshness, expiry, withdrawal, and stale-payload behavior.
8. Integration of location/provider/world change signals through typed ports.
9. Exposure, action, delivery, and owner-readback telemetry bound to the
   canonical receipt.
10. Interruption-level and lock-screen privacy review.

**Portfolio coverage**

- explore without a fully formed query;
- heat/weather/closure adaptation;
- provider disruption;
- relational opening;
- invitation or decision return;
- later relevant continuity; and
- deliberate quiet.

**Primary CJs:** CJ03, CJ07-CJ08, CJ11-CJ12, CJ14, CJ17-CJ18.

**Execution receipt (2026-08-23):** The first foreground attention loop is
closed in code and mock read-after-write. Home and Places graph summaries now
let the viewer inspect why an owner-scoped Opening reached them and choose to
open it, stay quiet, or dismiss it through the existing receipt-backed Opening
status command. The mock lane proves the silenced Opening leaves current
attention without creating a Commitment, Occasion, Trip, or notification
delivery. See the detailed [M4 Opening and deliberate-silence loop receipt](m4-opening-attention-loop-2026-08-23.md).

The first foreground loop and the graph/Lived vocabulary adapter are now
implemented, and typed Opening/occasion/decision/handoff/Commitment/receipt
destinations flow through the backend schema and mobile router. This is still
not notification launch: one persisted Opening authority, cross-surface
modify/snooze/mute/release, stale-owner resolution, receipt-bound telemetry,
and physical OS presentation remain explicit follow-on gates. See the detailed
[M4 Opening and deliberate-silence loop receipt](m4-opening-attention-loop-2026-08-23.md).

**Exit gate**

Every Opening identifies initiator, evidence, urgency, audience, available
actions, and expiry; the user can control future delivery; stale Openings do not
survive as current truth; and the system records either owner-state readback or
an explicit quiet/withdrawal outcome.

### M5 — Connect retained Commitments to external execution and lived reality

**Objective:** when a retained human-experience loop requires execution, join
the smallest necessary Trip/provider capability to Commitment and occurrence
truth without rebuilding provider infrastructure or preserving a first-party
Booking workspace.

M5 is not launch-critical by default. Provider execution may remain an external
handoff with a durable return receipt. Promote a deeper first-party adapter only
when it materially improves the experiential loop and cannot be supplied by
Maps, a marketplace, messaging, a calendar, or the provider itself.

**Deliverables**

1. Canonical Commitment state machine and controller model.
2. Adapter from one retained Trip or Occasion operation to Commitments.
3. Adapter from one retained provider handoff or operation to Commitment
   provider evidence, if direct execution is approved.
4. Task-scoped authorization, revocation, retry, and recovery.
5. Ambiguous provider-outcome handling.
6. Execution monitoring and provider-handoff receipts.
7. Occurrence reconciliation preserving planned/provider/lived distinctions.
8. Separate shared occurrence from personal Outcome.
9. Repair propagation into all affected projections.
10. Provider sandbox and multi-account evidence for any retained direct
    execution path.

**Portfolio coverage**

- hand off, reserve, or book after explicit authority where retained;
- delegate a bounded responsibility;
- reroute or repair after disruption;
- provider-confirmed but attendance-unknown;
- incomplete/ambiguous provider operation; and
- one shared Occasion with distinct personal Outcomes.

**Primary CJs:** CJ10, CJ13-CJ16, CJ17-CJ18.

**Exit gate**

- an option approval never implies payment/contact/retry authority;
- a timeout never becomes false failure or automatic retry;
- provider confirmation never becomes attendance or enjoyment;
- every shared Commitment has one status/revision; and
- recovery and correction converge every projection.

### M5 completion status — 2026-08-23

The bounded M5 exit is now implemented in the [M5 execution and reality
closure receipt](m5-execution-and-reality-closure-2026-08-23.md), building on
the [provider evidence and return receipt slice](m5-provider-evidence-return-receipt-2026-08-23.md).
One block from the latest retained Trip itinerary can be explicitly adopted as
one graph Commitment via a durable external identity link. Adoption requires
the caller's expected source revision, locks the source block and membership,
and creates the Commitment/link in the same transaction. The adopting
controller can issue one expiring, single-attempt task and revoke it through a
revisioned receipt. Provider callbacks remain on the secure server-only
boundary, require a `provider_observation` task, atomically consume it once,
and persist its ID on provider evidence. Raw provider references are visible
only to the controller; other participants receive bounded shared state.
Existing source-backed occurrence reconciliation and separate personal
Outcomes preserve the planned/provider/lived distinction.

M5 is closed at the external-handoff boundary. First-party payment, contact,
booking, automatic retry, provider accounts, and provider sandbox evidence
remain conditional follow-ons rather than hidden product commitments.

### M6 — Mount the coherent product shell

**Objective:** let the application feel like one product organized around the
August grammar rather than a collection of legacy and graph summaries.

Projection components should be developed during M2-M5. Root-shell cutover
occurs only after their canonical destinations and mutations are real.

**Deliverables**

1. Home: current Openings, active Occasions, invitations, actionable changes,
   earned returns, and intentional quiet.
2. Vesper: universal multimodal admission, private/group interpretation,
   facilitation, proposals, and compact durable receipts.
3. Places: canonical Place navigation, spatial orientation, conditions,
   practical/cultural legibility, familiarity, and Place-scoped openings.
4. Life: Mine/Together continuity, people, sources, Encounters, Outcomes,
   Occasions, correction, forgetting, and privacy.
5. Canonical inspectable projections for Plan, Occasion, Commitment, Opening,
   source, Outcome, relationship, and receipt. Prefer conversation anchors,
   artifact expansion, focused sheets, roots, and external handoffs over a
   standalone route per noun.
6. Typed direct links from Chat, push, Activity, and cross-surface cards.
7. Durable owner-state consequences replacing local fifteen-minute banners.
8. “All plans and occasions” destination before removal of the Plans root.
9. Query persistence/offline policy for each projection.
10. Navigation and naming cleanup for Home, Plans, Life, Together, Opening,
    Place, and Receipt.

**Exit gate**

- one canonical object appears coherently in several roots without duplicate
  ownership;
- bounded decisions, invitations, provider state, and receipts remain complete
  inside their artifact or focused-sheet grammar without hidden workflow
  screens;
- every displayed action has a real command and owner readback;
- restart does not erase consequences or their explanation;
- Home can remain intentionally quiet;
- Life is not an archive dump or static profile; and
- the mounted roots match their documented contracts.

### M7 — Earned continuity and safe authority retirement

**Objective:** prove compounding value and remove duplicate runtime authorities
without discarding mature operational capability. Presentation retirement does
not wait for M7; M-1 removes canceled screens once their entries are redirected.
M7 governs data owners, writers, compatibility facades, and retained substrates.

**Deliverables**

1. Continuity admission engine and inspectable admission reasons.
2. Place familiarity and cross-Occasion thread projections.
3. Adapters/migration for profile memory, saved Places, Atlas-compatible
   memory, Circle claims, and graph Outcomes.
4. Portfolio parity across the retained launch loops: local, travel, pair or
   group, correction, and quiet, plus provider execution only if retained.
5. Resolve or remove duplicate graph World identity.
6. Isolate/delete the dead Atlas destination implementation after consumer
   proof.
7. Retire graph/legacy routes and facades with zero required consumers.
8. Remove Trip-specific authority only after Commitment/Occasion parity.
9. Remove duplicated receipt and consequence stores.
10. Rebuild Qdrant from canonical Postgres truth and verify parity.
11. Produce a clean baseline migration only after retained schema authorities
    are decided.

**Exit gate**

- prior experience is admitted only when it changes a present job;
- correction/forgetting propagates through continuity;
- CJ01-CJ18 execute through declared canonical authorities;
- every legacy writer is either an explicit adapter or proven unreachable; and
- deletion/cutover has target-bound rollback and recovery evidence.

## 11. Parallel engineering workstreams

After M-1, M0, and one exercised M1 artifact seam, the relevant lanes may
progress in parallel. A lane exists only while it has an approved experiential
loop; the roadmap does not require all four lanes to remain staffed.

### Lane A — Sources, World, and Context

Owns:

- Universal Admission;
- Source authority;
- canonical World/Place identity;
- ContextManifest and provider ports;
- immediate utility; and
- source/identity correction.

Likely first milestone: M2.

### Lane B — Relationships, Occasions, and Multiplayer

Owns:

- Relationship authority;
- audience grammar;
- Occasion lifecycle and membership;
- invitations, decisions, constraints, and delegation;
- sender/recipient handoffs; and
- Together projection.

Likely first milestone: M3.

### Lane C — Commitments, Execution, and Reality

Owns:

- Commitment authority;
- Trip/proposal adapters;
- booking/provider adapters;
- occurrence reconciliation;
- personal Outcomes; and
- execution recovery.

Likely first milestone: M5, with M1 adapter work beginning earlier.

This lane remains quarantined if external handoff supplies the product need. It
does not own a Booking or Expense screen.

### Lane D — Attention, Projection, and Evidence

Owns:

- Attention authority;
- judgment/treatment convergence;
- notifications and Activity;
- canonical destinations;
- Home/Vesper/Places/Life projections;
- durable receipts and readback; and
- whole-loop evaluation.

Likely first milestone: M4, with M1 receipt work beginning earlier.

### Cross-lane integration rules

1. A lane may not introduce a durable noun owned by another lane.
2. Cross-domain mutations use M1 commands/outbox events, not table imports.
3. Every event names its source authority and canonical `ResourceRef`.
4. Surface components consume viewer-relative projections, not raw cross-domain
   joins.
5. A new route must pass the screen-admission test, name its intended production
   consumer, and declare its retirement posture. A durable noun or API is not a
   sufficient reason.
6. A new flag must be registered before code merges.
7. A schema change must include export, deletion, correction, and residual
   reference analysis.
8. A multiplayer change must include two-account and stale-membership cases.
9. A provider change must include ambiguous outcome and retry safety.
10. A projection change must include fresh owner readback, not only mutation
    success.

## 12. Portfolio integration slices

Trust invariants are checked against the full portfolio. Implementation
proceeds through several slices, and common engines are promoted from repeated
needs rather than constructed exhaustively in advance. No convenient first case
becomes the permanent ontology, but hypothetical parity does not block removal
of an obsolete presentation surface.

### S1 — Menu or practical photo

```text
photo
  -> immediate translation/ordering help
  -> one useful sensory or local distinction
  -> optional private keep
  -> later Place relevance or silence
  -> correction/release
```

Exercises Admission, Context, Treatment, World, Continuity, Projection, and
Receipt. Primary CJs: CJ01, CJ02, CJ05, CJ06, CJ17, CJ18.

### S2 — Movie ticket or book passage in Rome

```text
artifact
  -> identify work and evidence state
  -> immediate cultural orientation
  -> current Place connection
  -> private relational opening
  -> human-addressed handoff
  -> optional shared Occasion
  -> separate Outcomes
```

Exercises Sources, World, Continuity, Attention, Relationships, Occasions, and
multiplayer. Primary CJs: CJ01, CJ05-CJ08, CJ10-CJ12, CJ16-CJ18.

### S3 — Dinner invitation with private constraints

```text
invitation
  -> inspect people/purpose/time/commitment
  -> provide private constraint
  -> join tentatively
  -> group-safe decision
  -> responsibility and Commitment
  -> occurrence
  -> plural personal Outcomes
```

Exercises Context, Multiplayer, Occasion, Commitment, Reality, and Receipt.
Primary CJs: CJ07, CJ10-CJ16, CJ18.

### S4 — Heat, closure, delay, or fatigue adaptation

```text
changing world/person state
  -> treatment-versus-silence decision
  -> inspectable Opening
  -> repair/reroute/defer
  -> shared projection convergence
  -> occurrence reconciliation
```

Exercises World, Context, Attention, Commitment, Delivery, and Reality. Primary
CJs: CJ04, CJ07, CJ12-CJ16, CJ18.

### S5 — Optional provider handoff or authorized execution

**Status:** quarantined unless a retained product loop requires more than an
external handoff and return receipt.

```text
decide or ask Vesper to prepare the next step
  -> grant task-scoped authority
  -> hand off externally or execute through one approved adapter
  -> monitor
  -> ambiguous/confirmed/cancelled provider truth
  -> occurrence remains separate
  -> reconcile/recover/revoke
```

When activated, exercises Action Gateway, Commitment, a bounded provider
adapter, Receipt, and Reality. Primary CJs: CJ13-CJ16, CJ18. It does not require
a first-party Booking workspace.

### S6 — Second Occasion continuity

```text
authorized prior Encounter
  -> current Place/job relevance
  -> admitted continuity or silence
  -> changed perception, conversation, action, or capability
  -> inspect/correct/release
```

Exercises Continuity, Context, Treatment, Attention, Projection, and Evidence.
Primary CJs: CJ05-CJ06, CJ08, CJ14, CJ17-CJ18.

### S7 — Correction across the graph

```text
wrong Place / attendance / interpretation / audience / authority claim
  -> inspect lineage
  -> correct or revoke
  -> invalidate derived projections
  -> repair shared state without leaking rationale
  -> durable correction receipt
```

Exercises every platform rail and most authorities. Primary CJs: CJ06-CJ07,
CJ09, CJ11, CJ16-CJ18.

## 13. Definition of done for an engine

An engine is not complete because its models, tables, routes, generated types,
mocks, or unit tests exist. It must demonstrate:

### Authority

- one declared durable writer;
- actor/viewer/audience distinctions;
- capability and revision enforcement;
- idempotency and replay safety;
- no bypass writer;
- unknown/quiet branch; and
- explicit ownership of correction and deletion.

### Runtime integration

- real writer;
- authorized reader;
- generated contract;
- production data-facade caller;
- mounted/reachable surface;
- canonical conversation anchor, focused projection, root, or external handoff;
- durable receipt;
- restart-safe owner readback; and
- delivery repair after partial failure.

### Privacy and lifecycle

- denial cases;
- private/shared projection tests;
- stale-membership tests where relevant;
- retention/expiry policy;
- correction/release/revocation;
- account export;
- account deletion and residual-reference audit; and
- blob/vector cleanup where relevant.

### Operational evidence

- bounded telemetry without private content;
- latency/error/retry measurement;
- outbox backlog and repair observability;
- rollout flag and cohort posture;
- rollback plan; and
- deployed environment evidence before release claims.

### Portfolio evidence

- at least two materially different journey consumers, except for a
  cross-cutting trust invariant;
- one failure/recovery branch;
- one correction branch;
- two-account proof where multiplayer is involved;
- provider ambiguity where execution is involved;
- device proof for mounted surfaces; and
- human value evidence kept separate from conformance evidence.

## 14. Evidence and evaluation plan

Each integration slice should maintain four independent evidence columns:

| Gate | Required question | Evidence examples |
|---|---|---|
| Architecture coherence | Do ownership, plurality, truth, correction, and silence hold across the portfolio? | authority register, scenario matrix, ADRs, adversarial review |
| Implementation conformance | Do real writers/readers/projections obey those contracts? | database tests, replay tests, contract checks, two-account tests, integration receipts |
| Human product value | Did the person receive relief, capability, shared value, or better later judgment? | observed use, comparative trials, participant-specific outcomes |
| Release readiness | Is it safe, operable, understandable, reversible, and monitored? | physical device, provider sandbox, deployment, privacy review, rollback proof |

Whole-loop traces should be able to answer, without storing private content:

```text
Was the source admitted?
Was immediate utility delivered?
Was retention explicitly authorized?
Did a graph/authority object change?
Was an Opening eligible, delivered, or silenced?
Did a person act?
Did the canonical owner surface show the result?
What actually happened later?
Was prior continuity ever admitted again?
Was correction or release honored everywhere?
```

## 15. Migration and retirement policy

### 15.1 Reuse through adapters

Prefer adapting these mature capabilities:

- Trip operation gateway and proposal application;
- booking provider sagas and reconciliation;
- notification registration, delivery, privacy, and outcome handling;
- Mapbox, location, movement, routing, and weather;
- private/group Chat and pending-turn admission;
- composed-card rendering and server action resolver;
- Social Circle membership and shared claims where semantics fit;
- generated OpenAPI/app contracts;
- rollout and compatibility ledgers; and
- account/privacy infrastructure after metadata coverage is repaired.

### 15.2 Converge deliberately

These currently overlap and require explicit authority decisions:

- existing Place/entity identity vs graph `world_entities`;
- Trip/itinerary Plan vs clean graph Plan;
- Trip/local occasion models vs graph Occasion;
- Lived OpeningRequest vs graph Opening;
- Trip/group/Circle/Occasion membership;
- profile/Atlas/Place memory vs graph Outcomes;
- graph, legacy, provider, notification, and local receipts; and
- Plans root/Trips Home vs doctrinal Home and Life.

### 15.3 Quarantine rather than expand

Transport-only APIs, unused data facades, shadow workers, dogfood galleries,
and compatibility surfaces should remain dark unless a named roadmap milestone
adopts them. Do not expand a quarantined abstraction to make it appear useful.

### 15.4 Three retirement gates

Do not force presentation, client capability, and backend authority to share one
retirement date.

#### Presentation retirement

A screen, route, gallery, or visual-QA surface may be deleted when:

- the product has explicitly canceled it or named its replacement interaction;
- active navigation, search, push, notification, and deep links redirect safely;
- in-flight user work has an artifact, focused projection, external handoff, or
  bounded compatibility recovery path;
- retained behavior has moved to artifact/action/readback tests; and
- the pre-deletion implementation is preserved by a pushed git tag or archive
  branch.

Presentation retirement does **not** require backend authority parity.

#### Mobile capability retirement

Client hooks, view models, mocks, fixtures, and API facade methods may be
deleted when no retained root, artifact, sheet, compatibility path, or test
imports them and generated-contract governance confirms the consumer count.

#### Backend authority retirement

Delete an authority or compatibility layer only when:

- its replacement is named;
- all required writers and readers have migrated;
- portfolio parity includes failure, recovery, correction, privacy, and quiet;
- production reachability is zero or explicitly cut over;
- historical/export requirements are preserved;
- rollback has been tested against the target environment; and
- the deletion is a deliberate, reviewable change rather than incidental
  cleanup.

### 15.5 Archive and tombstone policy

Git is the source archive. Do not move canceled product source into an active-
tree `archive/`, `legacy/`, `attic/`, or hidden route family: agents, search,
dependencies, component catalogs, and design tooling would continue to treat it
as product material.

Before a material presentation teardown:

1. create and push a dated archive tag;
2. optionally retain an archive branch outside normal development;
3. delete the canceled implementation from the active tree; and
4. keep only a compact tombstone naming the archive ref, replacement,
   capabilities retained, and evidence required for reintroduction.

### 15.6 Route and surface budget

The active product has a finite attention budget. CI should generate and gate:

- production route count and approved classification;
- roots and focused workspaces;
- artifact and sheet families;
- compatibility redirects with owner and expiry;
- retired route/component imports;
- registered visual-QA surfaces; and
- screen-specific test and fixture families.

New routes require founder-approved admission. Removing a route should normally
remove its screen-specific QA and design obligations in the same packet.

## 16. Explicit non-goals and traps

Do not build:

- a pipeline per artifact type;
- another Place identity store;
- another generic receipt or consequence table;
- another undifferentiated group/member aggregate;
- a second booking/provider saga inside the graph;
- a universal AI agent that writes domain tables directly;
- Home as an engagement feed before Attention authority exists;
- Life as an archive dump, static profile, or universal settings panel;
- memory admission based only on semantic similarity;
- a group personality that replaces plural people;
- a surface-specific correction model;
- a standalone page merely because a canonical noun has durable state;
- first-party booking, voting, proposal, or expense workspaces when a typed
  artifact, focused sheet, or provider handoff satisfies the human job;
- an active-tree archive of canceled product surfaces;
- a new route with no intended production consumer; or
- a flag present only in documentation.

Do not mistake:

- table existence for authority;
- route registration for product capability;
- a generated TypeScript method for a mounted caller;
- a fixture gallery for runtime proof;
- a hidden route for retired product surface area;
- reliable backend truth for a requirement to expose a management screen;
- mutation success for owner readback;
- provider confirmation for occurrence;
- retention for permission to infer;
- sharing for permission to reuse; or
- a resonant demonstration for portfolio validation.

## 17. Decision register required before execution

The following decisions should be resolved in or before M0/M1:

| ID | Decision | Why it blocks |
|---|---|---|
| D01 | Which existing Place/entity authority is canonical, and what happens to graph `world_entities`? | World references, deep links, handoffs, imports, and correction cannot converge without one identity policy. |
| D02 | Is clean Plan authoritative immediately, or an additive projection over mature Trip/itinerary authority during migration? | Determines command adapters and prevents two writers. |
| D03 | How are Circle, conversation, Trip, and Occasion membership related? | Multiplayer privacy and capability cannot be inferred safely. |
| D04 | Which Opening model becomes canonical? | Graph and Lived/notification paths otherwise create two attention systems. |
| D05 | What is the canonical receipt schema and retention policy? | Cross-surface consequence, export, reversal, and evidence depend on it. |
| D06 | How is a shared Occasion preserved or transferred when its creator deletes their account? | Current clean schema may cascade shared state. |
| D07 | Is Plans a temporary Home projection, a permanent root, or a canonical destination beneath Home? | Determines navigation and projection ownership. |
| D08 | Does You evolve into Life, or is Life a new projection/root? | Determines continuity migration and prevents another accumulation surface. |
| D09 | What is the minimum relationship projection required for addressed attention? | Prevents Social Circle, pair, follow, and Occasion membership from collapsing together. |
| D10 | Which legacy systems remain canonical execution adapters after the graph reset? | Prevents rebuilding Booking, Notifications, and Trip operations. |
| D11 | Which current routes are roots, focused workspaces, artifacts/sheets, external handoffs, compatibility redirects, or retired? | Surface contraction cannot be systematic while hidden routes, QA registries, and design obligations remain ambiguously active. |
| D12 | Is first-party expense management canceled, and is provider booking limited to artifact-mediated external handoff by default? | Determines whether Costs and Booking remain product workstreams or only quarantined capabilities. |

Every decision should name:

- authority;
- data owner;
- writer and readers;
- migration adapter;
- correction/deletion behavior;
- rollout posture;
- adoption evidence; and
- retirement trigger.

## 18. Initial execution backlog

The first execution sequence should be:

1. Preserve the completed M0 trust work and finish its remaining graph-to-Place
   identity-binding seam; do not unwind privacy, account lifecycle, flag truth,
   authority registration, or reachability evidence.
2. Classify every production route through the M-1 surface taxonomy and record
   D11-D12.
3. Create and push the pre-contraction archive tag.
4. Make the existing group-chat decision artifact the sole normal proposal and
   voting destination; redirect external entries and remove Proposal Detail and
   Decision Deck presentation/QA families.
5. Replace the Booking workspace with provider handoff/status artifacts plus a
   bounded compatibility redirect; delete Booking screen/polish infrastructure
   after state and deep-link parity.
6. Remove the expense ledger, balance, add/edit, and detail presentation if D12
   confirms cancellation; retain only source/receipt capabilities exercised by
   the artifact grammar.
7. Add route-budget, retired-import, and retired-QA CI gates; refresh route,
   surface, component, and visual-evidence registries.
8. Recalculate the minimum engines and active lanes after teardown. Remove
   speculative M1-M7 deliverables with no retained experiential consumer.
9. Bind Vesper pending-turn admission to Intake `SourceRef`; make first-turn
   images custody-eligible and text/audio shares resumable.
10. Define the first `ContextManifest` provider set and deliver the S1/S2
    immediate-value artifact loop.
11. Prove one minimum `ResourceRef` / command / receipt / readback seam through
    that loop; generalize only when a second loop needs it.
12. Mount sender-side addressed handoff and the S3 multiplayer decision loop
    through durable conversational artifacts.
13. Mount initial Home and Life projections over real owner state without
    generating a standalone page per canonical noun.
14. Run the retained S1-S4 and S6-S7 slices as portfolio conformance; activate
    S5 only after a founder decision that external handoff is insufficient.

Items 1-8 contract and govern the product surface before new platform
construction. Items 9-12 build the first human-experience and multiplayer loops.
Item 13 begins shell convergence. Item 14 prevents one successful slice from
becoming the permanent ontology while keeping provider plumbing optional.

## 19. Roadmap completion condition

This roadmap is complete when the codebase can express the CJ01-CJ18 portfolio
through the minimum declared canonical authorities and shared engines actually
needed by retained product loops, while preserving private plurality, current
world truth, scoped authority, correction, unknown, and silence. Portfolio
coverage does not require every possible provider or management workflow to be
first-party UI.

Concretely, a zero-to-product environment must be able to:

- accept a natural fragment and solve its immediate job;
- retain only what the person authorizes;
- resolve one canonical Place across sources and projections;
- create personal Plans and bounded shared Occasions without making everything
  a Trip;
- address a person or group without broadening audience or inference;
- decide together without erasing private constraints or decision rights;
- create one authorized Commitment and, where the product has retained
  execution, hand it to a real provider or responsible actor with truthful
  return state;
- distinguish plan, provider truth, occurrence, and personal Outcome;
- deliver or silence an Opening through one attention runtime;
- make a later Occasion better only when continuity is admissible;
- show one durable, inspectable receipt at the canonical owner surface;
- render bounded proposals, invitations, votes, provider handoffs, and receipts
  through typed conversational artifacts without hidden workflow screens;
- correct, release, revoke, export, and delete data across all projections; and
- boot the mounted Home/Vesper/Places/Life product without duplicate legacy
  authorities masquerading as canonical truth.

The intended result is not maximal infrastructure or maximal surface coverage.
It is a coherent, world-facing product runtime in which conversation, custody,
multiplayer authority, movement, selective provider handoff, notifications,
privacy, and correction compose into the August experience grammar. The app
spends its design attention on a few roots and a reusable artifact language,
while infrastructure supplied well by Maps, marketplaces, messaging, payment,
calendar, and providers remains connected rather than weakly reimplemented.
