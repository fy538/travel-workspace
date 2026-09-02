---
doc_type: working
status: active
owner: founder / product / architecture / backend / frontend
created: 2026-08-31
last_verified: 2026-09-02
expires: 2026-09-30
why_new: Records the code-audited current state, target architecture, selective demolition plan, Chat/Life dependency boundaries, implementation sequence, and promotion gates for the post-pivot Home and Places roots.
source_of_truth_for: []
depends_on:
  - ../decisions/2026-08-30-adopt-home-and-places-consumer-anatomy.md
  - ../decisions/2026-08-29-close-four-root-experience-to-contract-convergence.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/artifact-expression-and-composition.md
  - ../systems/contribution-and-consequence.md
  - home-and-places-build-manifest-2026-08-30.md
  - design-kernel-extraction-2026-08-29.md
  - places-consumer-experience-anatomy-2026-08-29.md
  - minimum-four-root-projection-and-owner-read-contracts-2026-08-29.md
related:
  - ../decisions/2026-08-30-adopt-life-consumer-anatomy.md
  - ../decisions/2026-08-29-adopt-life-continuity-and-return-contract.md
  - life-root-production-spec-2026-08-30.md
  - life-return-arbitration-policy-2026-09-01.md
  - chat-as-agentic-interaction-layer-research-2026-08-29.md
  - agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - claude-design-interaction-kernel-lab-v2-controlled-comparison-handoff-2026-08-31.md
  - life-next-behavior-prototype-handoff-2026-08-31.md
  - home-and-places-root-implementation-status-2026-08-31.md
---

# Home and Places Root Implementation Program

## Executive decision

Proceed with the Home and Places architectural transformation now. Do not wait
for every Chat and Life visual or interaction lane to settle.

Home and Places are semantically closed enough to build their durable
foundation:

- Home's stable responsibility, anatomy, postures, demand laws, and bounded
  unit union are accepted;
- Places' stable responsibility, encounter states, scope law, social forms,
  and bounded unit union are accepted;
- the four-root ownership model, contribution-and-consequence authority model,
  canonical-owner rule, and push/return law are already cross-root contracts;
  and
- the new roots remain feature-gated, so the replacement can be constructed
  without forcing a premature production migration.

Chat and Life still matter. They constrain several shared seams and will change
some destination behavior. They do **not** require Home and Places to postpone
their candidate model, bounded reads, authority gates, root-specific compilers,
typed projections, native root anatomies, or Home↔Places movement.

The correct strategy is therefore:

> **Build Home and Places behind stable cross-root contracts; keep Chat and
> Life behind typed, replaceable boundaries; defer only the behaviors whose
> correctness depends on their unsettled consumer design.**

This is not a repository-wide rewrite and not a narrow single-loop proof. It
is a selective replacement of the root orchestration layer across a complete
Home/Places situation matrix, while retaining canonical owners and mature
domain infrastructure.

## 1. Scope and stop lines

### 1.1 In scope

- Home and Places backend read portfolios;
- candidate generation from existing canonical owners and mature producers;
- shared truth, authority, novelty, repetition, feasibility, burden, and
  silence gates;
- separate Home and Places selection compilers;
- typed Home and Places unit unions and projection envelopes;
- Home's fixed editorial anatomy;
- Places' World Field, Place Focus, Place Path, and Live Reduction states;
- Home↔Places pushed depth and exact return;
- existing-owner actions, readback, receipts, correction effects, and root
  invalidation where the owner contract already exists;
- compatibility adapters and eventual deletion of replaced Home/Places
  orchestration; and
- native, real-data, degraded-state, accessibility, and performance evidence.

### 1.2 Out of scope for this program

- redesigning or changing the Chat root;
- redesigning or changing the Life root;
- deciding Chat's final empty-state, composer, hybrid form, or transcript
  treatment;
- implementing Life's lenses, dossier, Vault, Together layer, or custody UI;
- inventing a generalized Monitor owner;
- replacing Plan, Occasion, Commitment, Place, provider, Source, Claim,
  relationship, or receipt owners;
- persisting Home ranking, Place Horizon relevance, or other root-relative
  candidate assessments as canonical truth; and
- exposing server-selected React components, layout trees, or geometry.

### 1.3 Required discipline

Home and Places may emit a typed continuation toward Chat or Life, but this
program must not implement the destination surface. Until those destinations
settle, such a continuation is a contract and compatibility route—not license
to encode the destination's presentation assumptions in the origin projection.

## 2. Canonical product requirements

### 2.1 Whole-product law

The roots are four orientations over one governed lived-world model:

| Root | Orientation | Primary responsibility |
| --- | --- | --- |
| Home | Now | Return the most valuable current composition across the person's world |
| Chat | Dialogue and agency | Receive contribution and intent; compose, operate, coordinate, and repair |
| Places | World | Make spatial truth, affordance, relationship, human perspective, and possible movement intelligible |
| Life | Continuity | Preserve and organize governed evidence, episodes, relationships, and durable handles |

The implementation program protects this allocation. It does not make Home an
inbox, Places a feed, Chat a universal owner, or Life the generator of present
possibility.

### 2.2 Home law

Home is an editorial field with a stable anatomy:

1. orientation;
2. `week_shape`;
3. Now;
4. In motion;
5. Horizons; and
6. Continuity.

People are a cross-cutting evidence reservoir. A visible people chapter appears
only when the gathering itself is the subject.

Home owes:

- exactly one dominant when a dominant exists;
- at most one unresolved primary decision;
- initial value without required response;
- complete-on-view units by default;
- urgent as the only suppressive posture;
- a quiet floor that can remain rich while demand remains zero;
- new value rather than paraphrase of what the person already supplied;
- an inspectable basis for every consequential projection; and
- present and near-future value that prevents retrospection from consuming the
  person's whole current life.

### 2.3 Places law

Places is one navigable encounter:

```text
World Field -> Place Focus -> Place Path
                   |
                   +-> Live Reduction when circumstance requires compression
```

These are interaction states, not tabs. Scope narrows and persists. Search, map,
and editorial composition are transformations of one admitted world set.

Places owes:

- one lead, a bounded number of branches, compact doors, and an honest end;
- spatial truth and practical judgment, not generic recommendations;
- no repetition of the originating Home proposition;
- a Place Path only when the relation earns structured depth;
- the four admissible social forms only: attributed evidence, relational
  relevance, plural comparison, and participation consequence;
- degradation that removes unsupported dependents rather than filling the page;
  and
- no current-world claim disguised as fresh when its provider state is stale or
  unknown.

### 2.4 Cross-root law

- One object retains one canonical identity across roots.
- Root projections are views, not duplicate owners.
- Cross-root depth is a push within the origin stack.
- Only an explicit in-view Door switches the selected root tab.
- Exact origin, selected resources, audience, represented moment, owner state,
  and return position survive the handoff.
- Consequential changes return through owner/provider readback, not assistant
  assertion or optimistic projection truth.

## 3. Code-audited current state

The current work established an important vertical spine, but it remains a
bridge between the legacy product and the accepted consumer anatomy.

### 3.1 What has progressed

Backend:

- typed `GET /api/root-projections/home` and
  `GET /api/root-projections/places` endpoints exist;
- a generated OpenAPI transport crosses the repository boundary;
- `RootProjectionEnvelopeV1` carries identity, revision, freshness, source
  revisions, degradation slots, and Home/Places payloads;
- `FourRootReturnEnvelopeV1` defines an exact semantic handoff contract;
- Home has deterministic ordinary, returned, quiet, and urgent behavior over
  Experience Graph owners; and
- Places preserves the existing canonical viewer-relative feed rather than
  fabricating a parallel dataset.

Native app:

- the four-root shell is feature-gated and Home/Places can run internally;
- Home renders a stable anatomy with `WorldRead`, `WeekShape`, four regions,
  one dominant, degradation, Doors, and a Rest Close;
- native Returned and Urgent fixture flows exist;
- Places can consume the root envelope while retaining the current production
  workspace; and
- Chat experimentation was reverted and Life was not changed.

This is useful progress: transport, flags, generated types, native primitives,
and compatibility routing are proven.

### 3.2 Home's present limitation

The current Home compiler reads the generic `ExperienceProjection` and chooses
roughly the first qualifying object in this order:

1. urgent Commitment;
2. current Commitment;
3. Occasion;
4. Plan;
5. Opening; or
6. newest Outcome.

It does not yet arbitrate:

- new value versus paraphrase;
- personal and social authority;
- evidence dependencies and correction effects;
- current consequence and practical feasibility;
- repetition across roots;
- attention burden and demand budget;
- medium selection;
- quiet richness;
- multiple candidate families competing for one region; or
- the complete 31-kind Home union.

It also ignores available occurrence evidence, uses broad generic owner paths,
and treats an entire Experience Graph read as one all-or-nothing dependency.

The real-data Home is therefore much less expressive than the accepted fixture
Home. Extending the current first-object selection function would create a
large conditional ranker on the wrong input abstraction.

### 3.3 Places' present limitation

The current Places root wraps the legacy `PlacesFeed`. The existing feed is
mature and valuable, but its primary abstraction is still ranked sections and
section reasons.

On the app, `PlacesRootExperience` supplies the root feed as initial data to
`PlacesWorkspace`, which then starts the old `usePlacesFeed` query again. The
workspace also reads Experience Graph context separately and injects an
`ExperienceGraphSummaryCard` outside server admission.

Consequences:

- two cache authorities can represent the same root;
- client composition can bypass server ordering and existence gates;
- root failure silently collapses into legacy feed behavior;
- invalidation targets the old feed but not the root query;
- World Field is not yet a distinct projection model;
- Place Focus, Place Path, and Live Reduction are absent from the root; and
- old section reasons still define presentation instead of serving as candidate
  evidence.

Places has substantial real functionality but has not yet undergone the new
product-grammar transformation.

### 3.4 Shared limitations

- The seven generic semantic-result families are useful primitives but are not
  the accepted 31 Home and 34 Places kind unions.
- Typed return exists in backend tests but does not drive native navigation.
- Resource destinations often collapse to generic Chat, Places, or Life routes.
- Root query keys are literal and outside centralized mutation invalidation.
- The current surface-ownership registry covers only a few legacy content
  families and uses the old Trips/Vesper vocabulary.
- Grant, correction, revocation, and causal dependency propagation are not yet
  part of root compilation.
- Home and Places use different broad context paths rather than one bounded,
  deadline-controlled root-read architecture.

## 4. Architectural diagnosis

Home and Places are mismatched in opposite directions:

- **Home's semantic ambition is ahead of its real inputs and compiler.**
- **Places' real inputs and functionality are ahead of its new grammar.**

The principal tech-debt risk is to keep extending Home over
`ExperienceProjection` and Places over `PlacesFeed`. That would preserve two
generations of:

- candidate vocabulary;
- ranking policy;
- cache identity;
- navigation behavior;
- degradation;
- social treatment;
- exposure tracking; and
- root composition.

The new roots are still internal and comparatively small. This is the cheapest
time to replace their orchestration cleanly.

## 5. Target architecture

```text
Canonical owners
Experience Graph · Places/world · providers · receipts · social grants
        |
        v
Bounded root read portfolio
viewer-safe · time/count bounded · deadline controlled · partially degradable
        |
        v
Internal RootCandidate
identity · owner · evidence · novelty · consequence · burden · authority
        |
        v
Shared hard gates
truth · audience · grant · freshness · repetition · feasibility · demand
        |
        +-------------------------+
        v                         v
Home compiler                Places compiler
fixed regions                encounter state
one dominant                 field/focus/path/live
posture + demand             scope + density taper
        |                         |
        +------------+------------+
                     v
Typed RootProjectionEnvelope v2
                     |
                     v
Native kind renderers
                     |
                     v
Push -> owner action -> readback -> invalidation -> exact return
```

### 5.1 Canonical owner adapters

Adapters translate canonical owner reads into root candidates. They do not
become owners themselves.

Required adapter families:

- current Moment and location/context;
- Experience Graph Plans, Occasions, Commitments, Occurrences, Outcomes, and
  Openings;
- legacy Home operational signals during migration;
- Places world, relationship, map, search, route, and current-condition reads;
- provider and receipt readback;
- Source, Claim, and evidence lineage;
- social relationship and contribution-use grants; and
- exposure and prior-projection state.

Each adapter must be:

- viewer-safe at the query boundary;
- bounded by time, count, or selected resource portfolio;
- revisioned;
- independently degradable;
- free of presentation components; and
- incapable of granting itself authority.

### 5.2 Internal `RootCandidate`

`RootCandidate` is a storage-neutral internal model. It is recomputed; it is
not a new database table or universal owner.

Minimum fields:

```text
candidate identity and revision
eligible root, region, and state
bounded unit kind
dominant job and material trigger
evidence-dependency cluster and surface seat identity
represented resources
canonical owner references
Source and Claim references
audience, use, inference, retention, and action authority
truth status, freshness, confidence, and expiry
new-value / novelty statement
current consequence and practical feasibility
attention demand and interaction burden
social attribution and naming permissions
semantic role, composition identity, and expression version
one lead-medium hint plus at most one supporting-medium hint
ephemeral, candidate-to-save, saved, shared, or live lifecycle intent
persistence policy and dependency manifest when durable
typed kind payload
```

Generated editorial work may arrive as a candidate only with inspectable
Sources, Claims, and novelty. The candidate never becomes evidence merely
because Vesper generated it.

### 5.3 Shared hard gates

Candidates pass an ordered, deterministic pipeline:

1. **Owner gate** — canonical owner and viewer access are valid.
2. **Authority gate** — use, retention, inference, audience, and action axes
   allow this exact projection and consequence.
3. **Truth gate** — corrected, deleted, retracted, expired, disputed, and
   unresolved states constrain the claim honestly.
4. **Freshness gate** — current-world and action claims are fresh enough for
   their promised precision.
5. **Novelty gate** — the unit contributes beyond retrieval, paraphrase, or
   repetition of what the person already supplied.
6. **Cluster gate** — substantially overlapping evidence candidates are
   merged when one composition can carry both jobs without degrading either;
   otherwise they compete for one surface seat under the current dominant job.
7. **Ownership/exposure gate** — another root has not already completed the
   same job, and the candidate is not an unauthorized echo.
8. **Feasibility gate** — practical claims and operations remain viable.
9. **Demand gate** — unresolved demand is proportionate to the root and
   posture.
10. **Silence gate** — the candidate beats omission at the available density.

The system should log suppression reasons for evaluation and debugging without
shipping a consumer-facing explanation of every rejected candidate.

### 5.4 Separate root selectors

Home and Places share candidates and hard gates, but they must not share one
universal ranker.

Home selects for current consequence, usefulness, legibility, being-held,
receptivity, novelty, and attention cost. It fills a fixed temporal anatomy.

Places selects for spatial intelligibility, current affordance, relationship,
practical difference, and possible movement. It resolves an encounter state
and applies a density taper.

A universal score would recreate a generic feed and force both roots toward the
lowest common denominator.

### 5.5 Projection envelope v2

The public wire contract should carry:

- schema version, projection identity, and revision;
- viewer, audience, represented time, and scope;
- source and owner revisions;
- degradations;
- a bounded root-unit discriminated union;
- represented and owner resources;
- inspectable `why_this` lineage;
- typed continuation destinations;
- origin and exact return context when pushed; and
- no native component or geometry choices.

The full accepted kind union can be typed before every producer is implemented.
A kind becomes server-emittable only after its owner adapter, compiler rule,
native renderer, and contract tests land together. Unsupported kinds produce
no candidate; they do not produce placeholders.

### 5.6 Native renderers

Native code owns anatomy, typography, geometry, motion, accessible order, and
interaction affordances.

Use a compile-time kind registry rather than a single generic renderer that
gradually accumulates root-specific exceptions. Shared visual instruments can
remain reusable, but root composition stays explicit.

During an AI-assisted shaping episode, the renderer must preserve semantic
identity, the selected object, and enough spatial continuity that the person
experiences one malleable composition rather than a stream of replacement
cards. Touch may supply the referent and language may supply nuance, but both
must compile into the same typed owner or projection command. Final Chat-side
choreography remains outside this program.

Home keeps one root component over a fixed region skeleton. Places should use
state-specific components over shared map/search/detail primitives rather than
one 700-line section-feed workspace with expanding conditional behavior.

### 5.7 Action, readback, and invalidation

- A root opens a typed owner projection or continuation.
- The owner API performs the mutation.
- Provider or owner readback establishes terminal truth.
- A receipt reports per-owner current state and recovery.
- A centralized impact result invalidates affected Home/Places projections.
- The returning root recompiles from owner truth.
- Corrections, deletion, expiry, grant narrowing, and revocation invalidate
  every dependent projection through typed causal lineage.

Do not use a client-authored optimistic card as the final truth of a
consequential operation.

## 6. Retain, adapt, replace, and delete

### 6.1 Retain

Backend:

- Experience Graph owners and privacy compiler;
- Places context, map, search, entity, venue, and detail readers;
- provider, booking, hold, action, and receipt gateways;
- exposure ledger and cross-worker invalidation substrate;
- contribution-and-consequence models;
- ResourceRef and existing canonical operation/readback identities; and
- valuable Home/Places producer logic that reads real conditions.

App:

- generated API transport;
- four-root feature flag;
- `WorldRead`, `WeekShape`, `Door`, `MediaPlate`, `RouteStrip`, map canvases,
  status, receipt, and consequence primitives;
- existing map, search, venue, site, and entity interactions; and
- native performance, accessibility, state-transition, and fixture harnesses.

### 6.2 Adapt

- Experience Graph reads into bounded root portfolios;
- old Home producers into temporary candidate adapters;
- Places section producers into candidate adapters;
- the exposure/ownership registry into root-vocabulary arbitration;
- current root transport into the v2 envelope;
- Home and Places mock fixtures into golden compiler fixtures using the real
  contract; and
- existing owner mutations into root-impact invalidation.

### 6.3 Replace

- the current first-object Home compiler;
- `PlacesFeed` as the new Places root payload;
- generic canonical-path routing for root depth;
- the seven-family-only root rendering contract as the final unit taxonomy;
- literal root query keys outside central invalidation; and
- client-side root composition and reranking.

### 6.4 Delete after cutover

- root projection v1 models and compiler;
- legacy Trips Home controller, body, presentation model, and render-plan
  machinery;
- Trips stack endpoint and models after its consumer graph is empty;
- the Places root wrapper that seeds and then refetches the old feed;
- PlacesWorkspace's root-level section-feed composition and client-injected
  Experience Graph unit;
- duplicate Home/Places cache authorities; and
- compatibility adapters whose source owner now has a direct bounded reader.

### 6.5 Explicitly do not delete yet

- Concierge Home feed infrastructure still used by Chat or notifications;
- the old Places feed endpoint while a released compatibility client still
  requires it;
- map, search, detail, provider, receipt, and owner APIs; or
- any Chat or Life component or route.

Deletion is an acceptance condition of the relevant migration package, not an
indefinite cleanup backlog.

## 7. Chat and Life dependency analysis

### 7.1 What is already stable across all four roots

The following seams are sufficiently settled to build against now:

- canonical owner identity and revision;
- Source, Claim, Composition, Instrument, Direct State, Receipt, and Projection
  distinctions;
- the five independent authority axes;
- viewer-relative audience and grant checks;
- owner/provider readback;
- correction, deletion, expiry, and revocation propagation;
- represented Moment and scope;
- origin and selected resource refs;
- push rather than tab-switch for depth;
- exact return;
- Home as present temporal delivery;
- Places as present spatial delivery;
- Chat as conversational composition and operation; and
- Life as governed continuity, custody, re-finding, and record-native return.

These are architecture-bearing. They should be encoded without waiting for
later visual design.

### 7.2 How Chat may still affect Home and Places

Chat's unsettled work can change:

- how a continuation is visually presented;
- whether a job stays conversational or opens a structured owner view;
- how hybrid form/chat review appears;
- which object-specific verbs appear at the origin;
- how multi-owner proposal, confirmation, partial failure, takeover, and repair
  are displayed; and
- how a long-running monitor is represented.

Chat should **not** be allowed to change:

- the identity of the origin projection;
- selected resources and canonical owners;
- the five authority axes;
- expected postconditions;
- owner/provider readback;
- exact return; or
- Home/Places admission after the consequence.

Therefore Home and Places can implement a typed continuation contract now, but
should defer final Chat verbs, Chat artifact composition, complex multi-owner
interaction, and Monitor-specific UI.

### 7.3 How Life may still affect Home and Places

Life's stable decisions already sharpen Home/Places architecture:

- Life holds governed evidence and lineage; it does not generate current
  openings as an owner.
- Present-tense possibility belongs to Home, or Places when primarily spatial.
- Life's Places lens owns the person's held history with a place, not current
  hours, reachability, or world affordance.
- Present coordination never migrates into Life.
- A generated composition becomes durable only under an explicit retention or
  sharing trigger.
- A root Return can stand down while Home or Places delivers the current value,
  without deleting its record or lineage.
- Revocation and suppression must recompile every dependent projection.

Life's unsettled work can still change:

- cross-cluster seat arithmetic when several unrelated Return clusters all
  qualify for a bounded root region;
- lens, dossier, search, and Everything-kept destinations;
- production implementation of Together and frozen historical shared state;
- the destination density of a carried-forward receipt; and
- Life's internal correction and custody interactions.

Home and Places should therefore carry evidence dependencies, surface owner,
return identity, suppression state, and durable destination refs now. They
should not hard-code Life lens paths, dossier geometry, Returns seat counts, or
Together presentation.

### 7.4 Dependency classification

| Dependency | Status | Home/Places treatment |
| --- | --- | --- |
| Canonical owners and ResourceRef | Stable | Build now |
| Source/Claim lineage | Stable | Build now |
| Five-axis authority and grants | Stable | Build now |
| Correction/revocation propagation | Stable requirement | Build now, incrementally certify adapters |
| Root roles and surface ownership | Stable | Build now |
| Origin/return envelope | Stable | Build now |
| Home↔Places pushed depth | Stable | Build now |
| Chat continuation payload | Stable minimum | Type now; keep destination replaceable |
| Chat visual/composer/form behavior | Unsettled | Wait |
| Chat multi-owner execution presentation | Unsettled | Wait, except existing-owner readback paths |
| Generalized Monitor owner | Explicitly deferred | Wait |
| Life record and current-value boundary | Stable | Build now |
| Life destination identity | Stable minimum | Carry owner refs now |
| Life lens/dossier/Vault routes and UI | Separate Life lane; semantically advanced but not a Home/Places dependency | Do not encode destination geometry or internal routing into root v2 |
| Life Return arbitration core | Accepted at fixture scale | Build shared cluster identity, material-trigger, merge, surface-yield, and demotion fields now; keep each root's selector independent |
| Cross-cluster Life seat arithmetic | Open for build phase | Do not hard-code Life's unresolved 0–3 selection policy into Home/Places |
| Life Together consumer flow | Proven at fixture scale; production substrate incomplete | Reference the durable grant contract and gate data correctly; do not implement Life destination UI |
| Life refinding | Dark native slice built in a concurrent lane | Do not duplicate or overwrite it; use its target-first truth envelope as an adjacent precedent, not a Home/Places dependency |

### 7.5 Decision: do not wait for all lanes

Waiting for all four designs would be counterproductive:

1. Home and Places already have accepted semantic anatomy and authorized native
   implementation.
2. Their largest current problems are code-shape problems independent of Chat
   and Life visuals: broad reads, wrong candidate abstractions, duplicate
   caches, old feed orchestration, shallow selection, and missing invalidation.
3. Building the stable seams will give Chat and Life a better integration
   target rather than forcing those lanes to negotiate with legacy feed types.
4. The feature flag makes replacement reversible until promotion.
5. Delay would encourage more compatibility code to accumulate around v1.

The condition is that no package silently expands into Chat or Life
implementation. Cross-root contracts are dependencies; destination UX remains
owned by its lane.

### 7.6 Parallel-lane alignment — 2026-08-31

The Artifacts and Life lanes advanced after this program's first draft. Their
findings refine the implementation boundary without reversing the sequence.

**Artifacts / interaction kernel:**

- one generated Composition and one live Instrument now form a required
  compatibility gate beside the A2/B2/D2 controlled interaction comparisons;
- one semantic identity must survive root-native density, medium, action, and
  persistence changes;
- generated value must be complete on view;
- a Composition uses one lead medium and at most one supporting medium;
- deliberate save freezes an expression version and dependency manifest;
- Instrument expiry removes stale controls but preserves owner truth and
  receipts; and
- no universal Artifact card, server-authored component tree, or general UI
  DSL may emerge from the experiment.

**Life behavior program:**

- Together and human refinding are consumer-proven at fixture scale;
- the 13-field grant record is the accepted durable successor to the temporary
  `ContributionAxes` fixture, although its production domain and revocation bus
  remain unbuilt;
- the experience-graph lane is the durable truth direction; new root work must
  not deepen the legacy itinerary lane except through a temporary adapter;
- Return arbitration's one-seat-per-cluster, merge, material-trigger
  recompilation, surface-yield, demotion, and suppression laws are accepted at
  fixture scale;
- contribution lifecycle is consumer-proven in design, and its first migration
  target is addressable Chat contributions through the contribution envelope;
  Home/Places must not compensate by excavating transcript text; and
- the refinding slice is implemented dark and flag-gated in a concurrent lane,
  with production integration and commits still outside this program.

**Program consequence:** Packages 0 and 1 remain unblocked. Package 2 may
implement semantic contracts and existing native primitives, but final
generated-Composition editing treatment must pass the artifact compatibility
gate before renderer promotion. Life's accepted arbitration core should inform
candidate fields and shared gates now; its unresolved cross-cluster arithmetic
and destination UI remain outside Home/Places.

## 8. Implementation packages

Packages are dependency-ordered architectural increments, not calendar weeks
and not isolated feature loops. Each package must cover its relevant situation
matrix and remove the obsolete path it replaces.

### Package 0 — Architecture freeze and characterization

Deliver:

- accept this implementation program;
- amend the build manifest's recommendation that the new admission compiler
  permanently wrap the old Concierge feed ranker;
- define the complete Home and Places kind unions;
- define `RootCandidate`, gate results, typed destinations, and projection v2;
- align Composition and Instrument lifecycle fields with the Artifact,
  Expression, and Composition contract;
- reference the accepted grant record rather than copying its thirteen fields
  into root-owned storage;
- document the precise consumer graph of Trips Home, Concierge feed, Trips
  stack, Places feed, Places workspace, and existing root v1;
- add characterization fixtures for valuable legacy signals; and
- establish central root query keys and invalidation entry points.

Why the ranker amendment is necessary:

The existing ranker contains valuable production knowledge, but its numeric
priorities, card kinds, and feed posture encode the old product. Reuse producer
inputs, exposure/fatigue concepts, and characterization cases. Do not make the
old rank output the permanent ordering authority of the new roots.

Exit gates:

- every legacy Home card family and Places reason has a retain, migrate,
  replace, retire, or defer disposition;
- no accepted unit kind lacks a declared payload owner and evidence gate;
- generated Composition, saved expression, live Instrument, Direct State, and
  Receipt remain distinct lifecycle families;
- v2 types contain no component or route strings; and
- concurrent Chat/Life work is not staged or modified.

### Package 1 — Bounded read portfolio and candidate substrate

Deliver:

- a root-read coordinator with concurrent source deadlines;
- independent degradation records rather than all-or-nothing root failure;
- root-specific bounded Experience Graph queries;
- candidate adapters for Experience Graph, operational Home signals, Places
  producers, provider/receipt state, exposure, and grants;
- Source/Claim dependency manifests;
- deterministic hard gates; and
- compiler diagnostics available only to tests and internal evaluation.

Design constraints:

- no universal `get_context` endpoint;
- no `RootCandidate` persistence table;
- no transcript excavation as owner truth;
- no new durable investment in the legacy itinerary lane beyond a bounded
  migration adapter;
- no model-selected authority; and
- no unbounded viewer graph read simply because the final screen is bounded.

Exit gates:

- Home and Places migration selectors consume bounded candidate tuples rather
  than widening the v1 compiler's generic full read; final compiler cutover is
  Package 2 work;
- the v1 Places bridge remains the characterization carrier until the v2
  compiler owns ordering, partial failure, and typed state;
- each adapter has privacy, unknown, stale, correction, and unavailable tests;
- partial source failure preserves an honest root;
- no candidate can become visible without an owner and evidence path;
- overlapping-evidence candidates preserve one cluster identity and one seat
  per surface; and
- root candidates reference grants and expression manifests without becoming
  their canonical owners.

### Package 2 — Home v2 compiler and real-data root

Deliver:

- Home posture and lifecycle-modifier resolution;
- orientation selection and merge law;
- week-shape compiler;
- four-region admission with one dominant;
- demand budget and urgent suppression;
- social reservoir projection;
- why-this inspection data;
- kind-registry native rendering; and
- real-data scenarios for ordinary, available, planning, live, returned,
  quiet, cold, urgent, and degraded Home.

Initial producer coverage should prioritize architecture breadth:

- current Commitment or recovery Instrument;
- prepared possibility Move;
- Occasion and loose-end motion;
- one grounded editorial/mechanism Horizon;
- one generated Composition whose identity and evidence survive compact Home,
  optional Chat inspection, Places depth, and deliberate-save boundaries;
- one authorized social contribution form;
- one carried-forward or reconstructed Continuity return; and
- honest silence/quiet composition.

This is not a mandate to emit all 31 kinds immediately. The full union is the
contract; producer and renderer support advance together.

Exit gates:

- real and fixture Home use the same contract and renderer path;
- exactly one dominant law is mechanically enforced;
- initial value never requires input;
- urgent suppression, quiet richness, and no-padding rules pass golden tests;
- correction or grant withdrawal removes dependent material;
- the generated-Composition compatibility case passes complete-on-view,
  expression-version, medium-budget, expiry, and causal-repair checks before
  its renderer is promotion-eligible; and
- no legacy Trips Home model appears in the v2 wire payload.

### Package 3 — Places encounter compiler

Deliver in state order:

1. World Field;
2. Place Focus;
3. Place Path; and
4. Live Reduction.

Refactor legacy Places producers into candidate sources:

- `nearby_set`, `neighbourhood`, `starter`, `guide`, `experiences`, `saved`,
  `saved_unplaced`, and `changed` survive as World Field/Focus inputs;
- `gap`, `expiry`, `group_waiting`, and `urgency` move to Home;
- `reading` and `register` become Path media;
- `friend_activity` is replaced by the four social forms; and
- anniversary/harvest remain outside current Places delivery under the Life
  boundary.

Preserve:

- context resolution;
- map and search infrastructure;
- entity and venue detail;
- route and provider reads;
- exposure capture; and
- network/offline infrastructure.

Replace:

- section reasons as presentation;
- the duplicate root/feed query;
- client-injected Experience Graph cards;
- client-side root ranking; and
- silent v1 fallback once v2 is promoted.

Exit gates:

- one root query and one context handle govern the encounter;
- map and composition derive from one admitted set;
- Focus does not repeat World Field's sales pitch;
- Path appears only when structured relation is earned;
- social fixtures pass attribution, naming, audience, and withdrawal tests;
- current claims lose action before visibility when stale; and
- Places ends honestly when the next unit does not beat silence.

### Package 4 — Push, return, action, and causal refresh

Deliver:

- typed projection destinations;
- Home→Places pushed depth within the Home origin stack;
- explicit Places Door tab crossing;
- exact origin projection, revision, scope, selected refs, and scroll anchor;
- one representative existing-owner practical action;
- canonical readback and per-owner receipt;
- centralized root-impact invalidation; and
- correction, revocation, and superseded-origin behavior.

Do not require the final Chat or Life UI. For those destinations, preserve the
typed continuation and use compatibility routing until their lanes adopt it.

Exit gates:

- Home→Places→action→readback→Home preserves identity and exact return;
- no tab switch occurs from a depth tap;
- action success is never inferred from request dispatch;
- a superseded origin returns to an honest recomposed state; and
- a revoked Source cannot survive in cached Home/Places prose.

Implementation checkpoint — 2026-09-02:

- App commit `31a54cbbb` implements a native Home-stack Places route family and
  carries exact ephemeral return identity through map, Search, collections,
  card doors, and supported details while reusing the canonical Places owner.
- Existing owner-grant, verified readback, repair, invalidation, and semantic
  return packages provide the corresponding action boundary; this route package
  does not infer success from navigation or create a new writer.
- Backend commit `708b1b86c` and app commit `6a32beebf` make the return law
  executable rather than implicit. Home revalidates its canonical projection
  before scrolling; only the same viewer, stable semantic revision, unit,
  family, audience, and selected resource revisions restore. Every drift or
  unavailable/missing/consumed token keeps the fresh composition, and the
  one-shot renderer request cannot fire again later.
- The compiler now excludes rotating opaque consequence grants and
  presentation proofs from semantic revision identity while preserving them in
  the served unit. Therefore a fresh timestamp/authority rotation does not
  manufacture supersession, while visible candidate change still changes the
  revision.
- Code evidence passes 48 backend authority/revision tests and 54 app
  Home/Places suites / 363 tests, plus focused lint, both TypeScript gates,
  API boundaries, route/surface registries, core-tab review, and surface
  invariants.
- App commit `1c134d964` adds the PR-smoke native rehearsal
  `.maestro/47-home-places-semantic-return.yaml` and an explicit Home-depth
  Places return control. A pinned iPhone 16 Pro / iOS 18.2 simulator run proves
  that Home remains the selected tab, the shared Places owner opens as depth,
  and return restores the originating Home unit at its semantic offset after a
  canonical fresh read. The adjacent selection passes 33 suites / 251 tests.
- Package 4 now has native happy-path evidence, not merely code readiness.
  Promotion remains open on physical-device return, Android hardware back,
  nested map/Reading/detail/action token propagation, process-death and
  supersession degradation, real-backend owner readback, visual review, and a
  deliberate iOS edge-gesture decision. The simulator edge-swipe attempt did
  not unwind this nested headerless stack; the explicit back control is the
  currently proven path.
- App commit `a92401579` additionally proves Home → Places → Search utility →
  Saved → Places → exact Home return in PR smoke. The rehearsal caught and
  removed a duplicate-root defect: Saved now dismisses to an existing matching
  Places owner, or converges to it when opened cold, instead of unconditionally
  replacing itself with a second root. The corrected iOS simulator flow passes
  1/1 in 23 seconds; five focused suites / 37 tests and the relevant type,
  boundary, registry, surface, metadata, and lint gates pass.
- App commit `e3a2cf293` extends the same law through Reading/Dossier, Map, and
  one canonical mock-owner action. Dossier now dismisses to an existing
  serialized Reading owner or converges there cold; Map unwinds to the same
  Home-owned Places workspace; and an Experience save must emit its canonical
  success consequence, survive detail movement, read back as saved from the
  shared Saves owner, and still return to the exact Home unit. The three new
  PR-smoke flows pass individually in 30s, 25s, and 42s on iPhone 16 Pro / iOS
  18.2. The adjacent selection passes 31 suites / 256 tests, both TypeScript
  gates, API boundaries, surface and core-tab checks, metadata, and the full
  349-flow syntax sweep.
- The remaining Package 4 gate is no longer ordinary nested media or mock
  action continuity. It is physical-device and Android return, process-death
  and real concurrent supersession, real-backend action/readback, visual
  review, and a deliberate iOS edge-gesture/shell decision.

### Package 5 — Native convergence and deletion

Deliver:

- state-specific Places native components;
- exhaustive emitted-kind renderer registration;
- accessibility ordering and dynamic-type behavior;
- performance budgets and no duplicate root reads;
- native scenario evidence;
- default-on internal dogfood promotion; and
- deletion of replaced v1 and legacy orchestration.

Exit gates:

- scenario matrix passes with production-shaped data;
- real root loading, partial degradation, offline, stale, and empty behavior are
  visible and honest;
- no old Home or Places presentation model can influence v2 ordering;
- every removed system has no remaining consumer; and
- founder promotion is an explicit decision, separate from implementation
  completion.

## 9. Scenario matrix

### 9.1 Home

| Situation | Architectural requirement |
| --- | --- |
| Ordinary New York | Useful orientation and bounded field without manufactured urgency |
| Open weekend / Available | Prepared possibility delivers value before optional action |
| Planning | One unresolved decision; other material completes on view |
| Live | Current Commitment and conditions dominate without turning Home into an itinerary |
| Europe return | Past evidence projects forward and competes honestly with current New York life |
| Generated Composition | One identity, complete-on-view value, inspectable evidence, one lead plus at most one supporting medium, and deliberate-save boundary |
| Social Occasion | People change the relevant unit rather than appearing as an activity feed |
| Quiet | Zero demand with a true read, week shape, and earned consumable returns |
| Cold | Honest invitation without pretending context exists |
| Urgent disruption | One recovery Instrument suppresses unrelated editorial material |
| Degraded/offline | Owned identity remains; stale action claims disappear first |

### 9.2 Places

| Situation | Architectural requirement |
| --- | --- |
| New York World Field | One spatial lead, distinct branches, honest browse, scope persistence |
| Sorrento Focus | Durable identity, current truth, relationship trace, and practical horizons |
| Rome↔Paris Path | New structured juxtaposition without repeating the originating observation |
| Pasta mechanism Path | Practical/cultural mechanism supported by evidence, not similarity filler |
| Live New York/Lisbon | One protected intention, viable path, fallback, burden, and temporal posture |
| Social contribution | One of four admissible forms under complete grant checks |
| Social withdrawal | Dependent projection recompiles or yields without residue |
| Provider degradation | Identity and durable interpretation survive; unsupported current action does not |
| Expiring Instrument | Current controls disappear on expiry while owner truth, outcome, and receipt remain |

### 9.3 Cross-root

- Home unit pushes a Places projection without selecting the Places tab.
- An explicit Places Door selects the Places root.
- Back restores the exact origin and scroll anchor.
- A Place selection can be handed to Chat without Chat reconstructing context
  from prose.
- A Life-held Source can support Home/Places without Life owning current
  delivery.
- A consequence returns owner truth to the originating root.
- A correction, suppression, block, or revocation invalidates every dependent
  projection.
- Two roots do not occupy the same evidence cluster with redundant value.
- A saved Composition preserves the chosen expression version and dependency
  manifest while later root projections may recompile.
- A transient Composition does not become a Life object merely because Home or
  Places rendered it.
- A withdrawn social Source removes only dependent claims and leaves unrelated
  history intact.

## 10. Verification and ratchets

Every package requires proportionate verification:

### Backend

- model and discriminator tests;
- privacy and authorization tests;
- deterministic candidate and compiler golden tests;
- bounded-query tests;
- deadline and partial-degradation tests;
- source-revision and causal-invalidation tests;
- action/readback/partial-failure tests; and
- no-v1-type-in-v2-payload ratchets.

### App

- generated-contract typecheck;
- exhaustive emitted-kind registry tests;
- one-root-query/no-duplicate-authority tests;
- navigation and exact-return tests;
- stale/offline/error/degraded state tests;
- accessibility order and dynamic type;
- native screenshot/flow evidence; and
- performance settlement without loading flashes or root replacement.

### Cross-repository

- regenerate and review OpenAPI and app projection;
- run backend tests, frontend tests, and typecheck;
- verify fixture and real-data paths share the same contract;
- stage commits explicitly by filename; and
- delete migrated compatibility code before declaring the package complete.

## 11. Recommended first execution slice

Do not begin with another Home card or another Places section.

Begin with the durable seam:

1. Amend the build manifest's ranker guidance.
2. Add the v2 kind unions and projection contract.
3. Add internal `RootCandidate` and gate-result types.
4. Add the bounded read-portfolio interface.
5. Convert one real Home operational signal and one real Places producer into
   candidate adapters.
6. Pass them through separate Home and Places selectors.
7. Generate the mobile contract.
8. Render the two emitted kinds through root-specific registries.
9. Prove partial degradation, centralized invalidation, and absence of duplicate
   Places fetching.
10. Run the generated-Composition and live-Instrument compatibility fixtures
    through the contract even if final interaction treatment remains in the
    design lab.
11. Widen producer coverage only after this path is mechanically sound.

The first slice is successful when it establishes the permanent spine, not
when it makes the largest visual change. The subsequent packages then add
sanctioned candidate sources and unit kinds without repeatedly redesigning how
the product is assembled.

## 12. Final recommendation

Home and Places can proceed relatively self-contained at the implementation
level because their product responsibilities and anatomies are now stable.
They are not independent of Chat and Life at the contract level.

Proceed now on:

- root reads;
- candidates;
- authority and evidence gates;
- surface ownership;
- Home and Places compilers;
- unit unions;
- native anatomies;
- Home↔Places movement;
- existing-owner readback; and
- causal invalidation.

Wait on:

- final Chat interaction and structured-review presentation;
- final Chat verbs and complex multi-owner workflows;
- generalized monitoring;
- Life lens/dossier/Vault rendering;
- production Life Together and revocation-bus implementation;
- cross-cluster Life seat arithmetic and Life destination presentation; and
- hard-coded destination geometry or routes owned by those roots.

The architecture should make those future designs easier to integrate. If a
later Chat or Life lane requires Home or Places to abandon canonical owners,
five-axis authority, exact return, surface ownership, or causal readback, that
would be a whole-product doctrine change—not an ordinary design refinement.

## 13. Real save-owner checkpoint — 2026-09-02

Backend commit `be675841c` proves the first ordinary Home/Places action loop
against real PostgreSQL rather than a fixture owner:

1. the Saves API creates a private venue save with durable idempotency;
2. replay returns the same canonical save rather than duplicating the write;
3. the Saves API and Places saved-venue read model independently recover that
   same row;
4. the final Home v2 response admits one continuity unit retaining both the
   `entity_save` and canonical venue references and a typed Places destination;
5. unsave removes the row from the owner list, Places, and a fresh Home
   projection without a second Home write.

This closes the backend half of the existing-owner readback requirement for
Save/Clear. It does not promote the roots and does not generalize one bookmark
into proof for provider booking, Plan mutation, encounter confirmation, or
their repair families. The dependency-ordered next step is to point the native
Home→Places save/detail/return rehearsal at the exact backend and app revisions,
then prove restart and supersession behavior. Chat and Life remain outside this
package.

## 14. Native-to-real save continuity checkpoint — 2026-09-02

Backend commits `b30f8b70c`, `08a14498d`, and `a9b0249a2`, plus app commits
`ea67fed6c` and `d5df71912`, complete the next dependency in section 13 on the
local real API:

- Home derives the saved Place's consumer identity from the canonical Place
  owner read while retaining the Save and Place as distinct references;
- an idempotent operator fixture creates no Trip, conversation, Opening, or
  projection row and therefore cannot make the test pass through duplicated
  Home state;
- the native flow removes the Save through Place detail, verifies that both
  the owner list and fresh Home projection retract it, restores the same Place
  through the canonical Save application service, and returns through the
  exact newly read Home unit;
- actionable Home cards expose nested source, destination, and action controls
  as separate accessibility elements, while structured degradation diagnostics
  remain available to operators rather than appearing as user copy; and
- bounded Home contention among Saves now follows canonical `saved_at` recency
  instead of random UUID ordering. This is a lane-local `why now` rule; Saves
  still remain below current-world and coordination value.

The real-backend simulator rehearsal and its focused tests pass. This closes
local native-to-real Save/Clear continuity only. Cold process restart,
concurrent supersession, physical iOS, Android, other owner/provider families,
visual acceptance, and public-shell promotion remain downstream gates. Chat
and Life remain outside this package.
