---
doc_type: working
status: active
owner: founder / product / architecture / research
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Resolves the missing seams among shared and personal Plan/Occasion projections, lightweight prospective structure, bounded dynamic artifacts, social circulation, contribution value, and the personal-world model after the August product pivot.
source_of_truth_for: []
---

# Plan, Occasion, Projection, and Consumer Architecture — Research Round 3

## Question and status

The prior two HCI rounds established Vesper's relational posture, first-person
authority, governed memory, mixed initiative, plural Outcomes, stable roots,
and adaptive projections. This round does not reopen those decisions. It asks
what additional architecture and consumer behavior are required to make the
following product coherent:

- a Plan or Occasion can contain common operational truth while appearing
  differently to each person;
- lightweight prospective material need not become an itinerary block or
  Commitment prematurely;
- dynamic operational compositions can replace a rigid itinerary screen
  without becoming generated UI soup;
- a small contribution can earn immediate and later value without becoming
  homework;
- social material can circulate through the product without becoming a feed;
  and
- evidence across time, Place, people, and episodes can improve later life
  without becoming a synthetic profile.

This is research and a decision docket. It does not itself authorize schema,
API, migration, ranking, or surface changes.

## Executive verdict

The six research programs converge on one architecture:

> **One governed world of evidence and consequences; one common operational
> ground for shared action; private and audience-scoped lanes around it; many
> viewer-, moment-, root-, and purpose-relative projections; one typed command
> path; and one causal record of what actually changed.**

The key product laws are:

1. **Personalize the lens, never the social fact.** Accepted time, Place,
   Decision, Commitment, provider state, and Occurrence cannot vary by viewer
   at the same owner revision. Ordering, explanation, density, preparation,
   private relevance, and available actions may vary.
2. **Structure rises with consequence.** A fragment may end after immediate
   value, become an Experience Anchor, open an expiring possibility, enter one
   person's Plan as a lightweight item, or become a Commitment. It does not
   traverse every stage automatically.
3. **Day, night, Shape, and itinerary are normally projections.** They earn
   durable identity only when independent audience, lifecycle, authority,
   history, or consequence requires it.
4. **The agent composes semantic intent, not application components.** Vesper
   should use a bounded family of native projections and instruments rather
   than model-authored React trees or a universal card DSL.
5. **Value precedes classification and reflection.** The person supplies a
   direction of attention, not finished documentation. The system owes an
   additive return before asking for custody, meaning, organization, or more
   work.
6. **Social material lands in the object it changes.** A friend's Place trace
   belongs in Places, its timely consequence may appear on Home, its shared
   commitment belongs to an Occasion, and a response begins in Chat. It does
   not need a generic activity feed.
7. **The personal world is evidence- and episode-first, not profile-first.**
   Narrative Personal Memory and Traveler Card can remain useful derived
   caches; neither should become the authority for the person.

The research does not support six new services. It supports a shared semantic
and causal spine used by existing owners.

## 1. What was already settled

The following remain in force from
[Round 1](relational-hci-for-the-lived-world-architecture-research-round-1-2026-08-28.md)
and
[Round 2](operationalizing-relational-intelligence-hci-research-round-2-2026-08-28.md):

- contextual intimacy without synthetic intimacy;
- Vesper's value points outward toward people, Places, understanding,
  capability, and lived action;
- the person owns personal meaning;
- governed scoped Claims, not profile prose, own memory authority;
- relevance earns eligibility, receptivity earns treatment, and authority
  earns action;
- one Occurrence may produce plural Outcomes;
- stable Home, Chat, Places, and Life roots with adaptive content and medium;
- deterministic authority, audience, freshness, and must/must-not policy before
  model selection;
- no generated component tree or universal card owner; and
- longitudinal consequence, correction, withdrawal, and capability matter more
  than clicks or session time.

Round 3 adds the missing object, projection, circulation, and value-loop
decisions. It should not be cited to reintroduce profile inference, shared group
meaning, engagement feeds, or unconstrained generated UI.

## 2. One integrated model

```text
directed attention, intent, invitation, provider change, or human contribution
        │
        ▼
Source / evidence / authored material
        │
        ├── immediate value may complete the job and stop
        ▼
Experience Anchor or governed Claim
        │
        ├── expiring Opening
        ├── personal Plan item
        ├── audience-scoped human contribution
        └── direct Commitment or Occasion consequence
        │
        ▼
Plan · Occasion · Decision · Commitment · provider/world owners
        │
        ├── shared operational core
        ├── audience-scoped attributed lanes
        ├── viewer-private overlay
        └── provisional system assessment
        │
        ▼
projection compiler
viewer × root × moment × purpose × scope × authority × freshness
        │
        ▼
Direct State · Composition · Instrument · Receipt · Owner Link · Prose · Silence
        │
        ▼
bounded native family
Shape · Sequence/Day · Decision · Live · Whole Plan
        │
        ▼
typed action → owner command → authoritative readback → receipt
        │
        ▼
Occurrence · plural Outcomes · application receipt · correction / expiry
        │
        ▼
later understanding, possibility, preparation, relationship, action, or silence
```

Three distinctions prevent most conceptual collapse:

| Distinction | Rule |
| --- | --- |
| **Owner versus projection** | Truth, authority, lifecycle, and correction remain with the domain owner; a projection is a lawful rendering. |
| **Common ground versus personal experience** | Participants may rely on shared operational facts without sharing interpretation, enthusiasm, preference, or meaning. |
| **Evidence versus generated return** | Record, reconstruction, Vesper interpretation, human-authored meaning, and creative transformation remain technically and visibly distinct. |

## 3. Shared operational ground and personal projection

### 3.1 Do not call every agreement “shared reality”

In social psychology, *shared reality* refers to perceived sharing of an inner
state, not merely agreement about an operational fact. Audience-tuned
communication can also influence later memory. Vesper should therefore use
**common operational ground** for facts and commitments participants can
mutually rely on, and reserve shared meaning for material people explicitly
co-author or confirm. [Shared-reality research](https://www.psychologicalscience.org/journals/current-directions/0963721421992027/)

Clark and Brennan's grounding work supports reducing total collaborative
effort while preserving enough evidence that people can coordinate. Vesper
should not require every participant to maintain explicit state merely to make
the system legible. [Grounding in communication](https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf)

### 3.2 Adopt a relaxed shared-view model

Groupware moved beyond strict “what you see is what I see”: identical screens
block useful private work, while unrelated screens damage coordination.
Workspace-awareness research emphasizes stable objects, visible change, and
feedthrough from one participant's action into the shared work.
[Workspace awareness](https://collablab.northwestern.edu/CollabolabDistro/nucmc/GutwinGreenberg_FrameworkWorkspaceAwareness.pdf)

Vesper's four lanes should be explicit in architecture even when the UI uses
lighter language:

| Lane | Contents | May affect shared consequence? |
| --- | --- | --- |
| `shared_core` | accepted facts, Decisions, Commitments, revisions, unresolved shared state | Yes, through the owning command |
| `audience_lane` | attributed contribution visible to a defined audience | Only under its owner and grant |
| `personal_overlay` | private constraint, departure time, preparation, relevance, private note or possibility | No, until separately proposed or authorized |
| `system_assessment` | current ranking, feasibility, opening, suppression, or treatment decision | No; it is an expiring read judgment |

At a given owner revision, eligible viewers must not receive conflicting
values for accepted shared facts. They may receive different:

- ordering and elevation;
- explanation and density;
- medium and continuation;
- private preparation and relevance;
- visible audience-scoped contributions;
- available actions; and
- root admission.

Every shared projected item needs stable identity, semantic type, owner
revision, lane, source or actor, audience basis, and a human-refindable label.
“The third card” is not a valid shared reference when cards differ by viewer.

### 3.3 Feedthrough without notification pressure

An accepted shared change should produce compact feedthrough for affected
viewers: what is now established, what changed, who is responsible where
appropriate, what remains unresolved, and where to inspect or repair it. It
must not reveal the private reason that influenced the result.

This is a scoped application of social translucence—visibility, awareness, and
accountability—inside the legitimate audience rather than across the whole
network. [Erickson and Kellogg](https://smg.media.mit.edu/library/erickson2000.pdf)

## 4. Progressive structure and the missing prospective unit

### 4.1 Code reality

The clean graph already has Plan, Occasion, Commitment, invitations,
Decisions, Occurrence evidence, and Outcomes. It does not have a lightweight
non-consequential member inside a Plan:

- `Plan` has kind, lifecycle, horizon, revision, and Commitment links;
- `experience_anchors.proposed_plan_id` is a proposal hint, not accepted Plan
  membership;
- `OpeningCandidate` may refer to an Occasion but not a Plan;
- legacy itinerary blocks currently occupy the large space between an idea and
  a Commitment; and
- the Trip adapter correctly keeps legacy execution truth on one side while
  giving an adopted Commitment semantic identity on the other.

This is why a dynamic visual redesign alone cannot eliminate itinerary-block
weight: the domain model has no smaller accepted prospective unit to render.

### 4.2 Recommended boundary

Adopt **PlanItem as a lightweight child of exactly one personal Plan**, not as
a new aggregate, universal content wrapper, shared object, or public product
noun.

```text
Source / evidence
  → Experience Anchor
  → optional expiring Opening
  → optional Plan-owned PlanItem
  → optional Commitment
  → optional Occasion consequence
  → Occurrence
  → plural Outcomes
```

The path is optional at every step. An explicit consequential instruction may
create a Commitment directly. An Occasion may begin without a prior Plan. A
fragment may return value and expire.

Incremental-formalization research supports demand-driven, system-assisted
structure over structure imposed before it becomes useful.
[Shipman and Marshall](https://people.engr.tamu.edu/shipman/viki/papers/tochi/tochi.html)
DDD likewise supports durable boundaries because business invariants require
them, not because the UI needs another noun.
[Microsoft DDD guidance](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries)

A minimal first semantic contract is:

```text
PlanItem
  id
  plan_id
  revision
  state: active | promoted | removed
  subject
  optional place_ref
  optional time_hint
  optional origin_anchor_id / origin_opening_id
  optional promoted_commitment_id
  created_by
  creation_receipt_id
  created_at / updated_at
```

Do not initially add nested blocks, custom permissions, arbitrary hierarchy,
manual ranks, independent audience, provider state, participants, occurrence,
or group Decisions.

The required invariants are:

1. Keeping an Opening creates or links a PlanItem; it never turns evidence into
   intent silently.
2. Promotion creates a Commitment and preserves lineage; the PlanItem does not
   become the consequence owner.
3. Moving or removing a PlanItem cannot cancel or reschedule a linked
   Commitment.
4. A promoted item renders consequential state from the current Commitment,
   never a copied PlanItem field.
5. An Occasion never owns another person's PlanItem.
6. Sharing a PlanItem produces an Occasion proposal or contribution; it does
   not merge personal Plans.

iCalendar provides a useful precedent for stable identity, optional timing,
and explicit relation without requiring every prospective item to have a full
schedule. It is evidence for optional structure, not a schema to copy.
[RFC 5545](https://www.rfc-editor.org/rfc/rfc5545.html)

### 4.3 Projection or durable owner?

Use this test:

| Candidate | Default | Promote when |
| --- | --- | --- |
| Day / afternoon / weekend | time-window projection | no normal promotion |
| Night out | sequence projection | it gains independent participants, lifecycle, shared consequence, or refinding identity; then it may be an Occasion |
| Trip Shape | overview projection | never solely because it is visually useful |
| Whole itinerary | whole-Plan projection | never solely because it is editable |
| Birthday dinner | Occasion | it already has bounded people, purpose, time, and common consequences |
| Restaurant booking | Commitment | provider or interpersonal consequence exists |

Naming alone is insufficient. Independent identity plus lifecycle, audience,
authority, or consequence earns ownership.

## 5. Bounded dynamic-artifact runtime

### 5.1 Vocabulary

Current canon uses **Artifact** for a human-facing thing brought, captured,
received, or made, and **Composition** for Vesper's generated return. The
Claude-design use of “artifact” for a dynamically rendered operational
interface is understandable but architecturally overloaded.

Use these internal terms:

- **Composition** for generated explanatory, editorial, comparative, or
  reconstructive value;
- **Instrument** for current state plus manipulation or consequence;
- **Projection** for viewer-, root-, scope-, and moment-relative expression;
- **Artifact** for admitted source material in accordance with current canon.

The UI need not expose every noun.

### 5.2 Runtime shape

Retain the existing outer result family:

```text
Direct State · Composition · Instrument · Receipt · Owner Link · Prose · Silence
```

Inside Composition or Instrument, add a versioned Plan projection contract:

```text
PlanProjectionEnvelopeV1
  schema_version
  projection_key / projection_version
  family: shape | sequence | decision | live | whole_plan
  owner_ref + owner_revision
  viewer_ref
  scope: whole | time_window
  dependency refs and revisions
  generated_at / verified_at / expires_at
  freshness: current | revalidating | stale | offline | unknown
  typed semantic payload
  opaque action references
  complete text fallback
```

The family mapping is:

| User-facing form | Semantic runtime family |
| --- | --- |
| Shape | overview over Plan, Occasion, or Trip dependencies |
| Day | sequence within a local-day window |
| Night out | sequence scope unless Occasion identity is independently earned |
| Decision | instrument over a Decision or proposal owner |
| Live | instrument over current owner, provider, and world truth |
| Receipt | top-level immutable consequence result |
| Whole plan | composition over one owner and a dependency manifest |

A2UI and Adaptive Cards validate catalogs, schema/version negotiation, native
rendering, and accessible fallbacks. Vesper should stop one layer higher than
A2UI's component tree: the model selects semantic family and content; the app
owns composition grammar, geometry, focus, motion, accessibility, and native
interaction. [A2UI](https://a2ui.org/concepts/overview/),
[Adaptive Cards](https://learn.microsoft.com/en-us/adaptive-cards/)

The CHI 2025 Jelly system supplies the appropriate interaction model: natural
language and direct manipulation modify the same typed task representation.
For Vesper, dragging dinner to Saturday and saying “put dinner on Saturday”
must resolve to the same domain command. [Jelly](https://hci.ucsd.edu/papers/jelly.pdf)

### 5.3 Freshness, concurrency, and action

Use current-state tables plus append-only receipts and a transactional outbox,
not full event sourcing. CQRS can begin as separate command and read-projection
code over the same Postgres database; separate stores introduce consistency
costs before Vesper has proven the load or access pattern.
[CQRS guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

Rules:

- every write carries actor, expected owner revision, idempotency key, exact
  scope, and action capability;
- Chat and touch call the same typed command;
- a revision conflict returns fresh owner/projection state and bounded repair;
- editorial projections may use bounded stale-while-revalidate;
- Decision and Live controls visibly identify stale state and revalidate before
  consequence;
- offline may queue private reversible PlanItem drafts;
- offline may not silently replay spending, booking, cancellation, invitation,
  group resolution, or public/social commands; and
- accepted mutation triggers authoritative readback, receipt, and dependency
  invalidation.

Use a small provenance subset: projection `used` exact owner/source revisions,
`wasGeneratedBy` a compiler/policy version, human material
`wasAttributedTo` its author, and saved output `wasDerivedFrom` its dependency
manifest. This resembles W3C PROV without importing a universal ontology.
[PROV-O](https://www.w3.org/TR/prov-o/)

## 6. Contribution-to-value behavior

### 6.1 The Granola analogy, stated precisely

The transferable mechanism is not merely “AI makes better notes.” A person
makes sparse marks directing attention; the system has a richer supporting
record; it expands the marks into a better representation; and the original
and generated layers remain inspectable. Granola describes raw notes guiding
transcript enhancement and allows the transcript to remain available for
inspection. [Granola](https://docs.granola.ai/help-center/taking-notes/ai-enhanced-notes)

NoTeeline tested human-guided micronote expansion with 12 participants and
reported lower writing and time burden, while participants emphasized source
truth, control, and progressive complexity. This supports reduced production
burden, not yet long-term memory benefit.
[NoTeeline](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2025/noteeline.pdf)

Vesper's version is:

```text
sparse directed attention
  + broader authorized evidence
  + current world context
  → one additive transformation
  → inspectable source relationship
```

Unlike a recorded meeting, Vesper has no complete transcript of life. It must
therefore be more conservative about reconstruction, attribution, and meaning.

### 6.2 Burden is more than taps

Personal-informatics research shows that collection burden contaminates later
integration, reflection, and action; lived practices lapse and resume rather
than following a clean funnel. Some people resume by using old evidence instead
of collecting more. [Personal Informatics](https://personalinformatics.ianli.com/lab/model),
[Lived Informatics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12435389/)

```text
total contribution burden =
  motor effort
  + recall effort
  + interpretation effort
  + emotional and authorship labor
  + decision effort
  + uncertainty about downstream use
```

Therefore:

- one-tap reflection may still be homework;
- missing days are not incomplete history;
- the app should not create a backlog, recap debt, or streak repair;
- return begins with current value, not “catch up”; and
- daily active use is not the behavioral north star.

### 6.3 Selective attention over total capture

Lifelogging research distinguishes recollecting, reminiscing, retrieving,
reflecting, and remembering intentions, and warns that total capture is not
equivalent to useful memory support. [Beyond Total Capture](https://www.microsoft.com/en-us/research/publication/beyond-total-capture-a-constructive-critique-of-lifelogging-2/)

Architecture must distinguish evidence origin:

| Evidence | May support | Does not prove |
| --- | --- | --- |
| directed question, share, note, or deliberate photo | salience for this situation and immediate job | stable preference, enjoyment, identity |
| ambient location, calendar, or transaction | occurrence candidate and operational reconstruction | attention or meaning |
| authored meaning | what the author presently says | permanent identity |
| repeated governed Outcome | contextual pattern candidate | universal person rule |

### 6.4 Creepiness is often illegible authority

Recent research found that perceived profile accuracy can increase perceived
surveillance rather than erase it. Another 2026 study found that personalized
conversation signals both usefulness and data-practice risk, with privacy
concern dominating when perceived control is low.
[Profiling study](https://www.sciencedirect.com/science/article/pii/S0747563224004047),
[privacy-calculus study](https://www.sciencedirect.com/science/article/pii/S0747563226001585)

The visible reward should be a better result, not a demonstration of how
precisely Vesper has modeled the person. Personalize selection and preparation;
avoid pronouncing identity. Real controls—correct, hide, use here, keep
private, release, show less, choose another direction—matter more than soft
copy promising control.

### 6.5 Value jobs and metric

Every generated unit should name one completed job:

- practical relief;
- usable representation;
- retrieval;
- reconstruction;
- epistemic contribution;
- capability transfer;
- prospective simulation;
- relational routing;
- experiential return; or
- possibility expansion.

Avoid generic “insight.” It obscures whether Vesper added anything.

The core ratio is:

```text
experienced value returned
──────────────────────────────────────────────────
motor + cognitive + emotional + privacy burden
```

A candidate north-star measure is **qualified consequence rate**: the fraction
of governed contributions that solve an immediate job or later produce a
person-recognized practical, epistemic, experiential, relational, or
possibility dividend without correction, authority violation, or
disproportionate burden.

## 7. Social circulation without a feed

### 7.1 Object-native social distribution

Apple's Shared with You is a useful precedent: human-sent material appears in
the destination app where it is useful, preserves source attribution, supports
reply from context, and can be pinned, removed, or disabled.
[Apple Shared with You](https://support.apple.com/en-gb/102197)

For Vesper:

- Maya's Paris Place belongs in Places;
- the new comparison it enables for Feihu may appear on Home;
- her contribution to Saturday dinner belongs in the Occasion;
- its retained consequence belongs in Life; and
- reply, proposal, or further contribution begins in Chat.

> **Social material enters through a person but lands in the Place, Plan,
> Occasion, Source, or possibility it changes.**

If replacing the named person with “someone online” loses nothing, the social
attribution is decorative.

Collaborative Google Maps lists and Spotify playlists similarly show that a
bounded object can retain contributor attribution without requiring a general
social feed. [Google Maps](https://support.google.com/maps/answer/7280933?co=GENIE.Platform%3DAndroid&hl=en-en),
[Spotify](https://support.spotify.com/us/article/collaborative-playlists/)

### 7.2 Separate private payoff from social obligation

The recipient actions should remain distinct:

- **Keep for me** — retain privately; send no signal.
- **This was useful** — explicit private acknowledgment to the sender.
- **Respond** — human-authored message.
- **Open together** — propose a mutual consequence.
- **Contribute** — change a bounded shared object under its constitution.

Avoid public counts, comparative engagement, reciprocity prompts, read-pressure,
activity streaks, leaderboards, and interpreting silence as relationship state.
Research on social-media obligations suggests likes and comments can become
forced maintenance rather than connection.
[Social obligation research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8464110/)

### 7.3 Preserve distributed human knowledge

Hidden-profile research finds that groups over-discuss already shared
information and underuse uniquely held information. Vesper's private caucus
may improve feasible group options without exposing a participant's private
constraint or manufacturing consensus.
[Hidden-profile research](https://www.sciencedirect.com/science/article/pii/074959789290049D)

Transactive-memory research suggests that close groups benefit from knowing
who knows what. Vesper should retain situated attribution—who noticed, knows,
experienced, or can continue something—rather than flattening it into “the
group likes.” [Transactive memory](https://scholar.harvard.edu/files/dwegner/files/wegnererberraymond1991.pdf)

### 7.4 Audience is relational and multiparty

The current five-axis authority model is a strong base, but a legitimate social
projection also depends on sender, subject, recipient, information type,
purpose, transformation, roster epoch, expiry, and transmission norm.
[Contextual-integrity formalization](https://crypto.stanford.edu/~jcm/papers/barth-datta-mitchell-nissenbaum-2006.pdf)

Co-affected people need standing over broader projections that expose or
characterize them. Available transformations should include omit, crop, blur,
abstract, summarize without identifying, or retain privately without wider
projection. This is not identical to ownership of another person's private
original.

## 8. The personal-world model

### 8.1 Evidence- and episode-first

The recommended conceptual model is:

```text
Source / Evidence
  immutable, governed, attributed, event-time + learned-time
        │
        ├── Occurrence fact
        ├── authored claim or meaning
        ├── provisional system claim
        └── attention trace
                 │
                 ▼
Episode projection
time × Place × people × Plan/Occasion × Occurrence
                 │
        ┌────────┴────────┐
        ▼                 ▼
typed relationship      contextual pattern candidate
source and scope        recurrence, counterevidence,
preserved               consumer, expiry, retirement
        │                 │
        └────────┬────────┘
                 ▼
current Opening / application
ephemeral, viewer-relative, purpose-bound
                 │
                 ▼
Outcome + application receipt + correction lineage
```

Rules:

- an Episode is normally a projection over governed owners, not automatically
  another table;
- a relationship edge is a typed, scoped, source-linked hypothesis, not a
  universal closeness or affinity score;
- a pattern requires recurrence, counterevidence, named consumers, expiry, and
  retirement;
- an Opening is current computation, not durable memory;
- a Memory Application records where prior evidence changed a decision,
  rendering, route, preparation, or action;
- Outcome remains separate from exposure, selection, Commitment, provider
  state, and Occurrence;
- maintain event time and system/knowledge time;
- embeddings retrieve candidates but establish no truth; and
- generated output cannot become supporting evidence for its own inference.

No graph database is required initially. A relational evidence ledger, typed
edge table, temporal validity, dependency lineage, and task-specific projection
compiler are sufficient.

### 8.2 Past evidence earns differentiation by changing the future

Episodic-future-thinking research supports a relationship between memory and
future simulation, including prospective memory, decision-making, and spatial
navigation. It does not prove that Vesper will retrieve the correct analogy.
[Schacter, Benoit, and Szpunar](https://pubmed.ncbi.nlm.nih.gov/29130061/)

The target transfer is:

```text
source episode
  → shared structural mechanism
  → material difference in the target situation
  → bounded present use
  → observed Outcome or correction
```

“You liked Sorrento, so here is another cliff town” is surface similarity.
“Vertical separation made a visually close ferry terminal operationally
distant with luggage; this New York opening has the same last-mile risk, but
the elevator hours remove it” is a candidate capability transfer.

Serendipity research further suggests that experienced enrichment is not
captured by a simple novelty or diversity score. Vesper should prefer a legible
bridge, newly available dimension, current usefulness, and low-cost agency.
[Experienced serendipity](https://doi.org/10.1145/3699682.3728325)

### 8.3 Memory-media integrity

Human memory is socially distributed but also socially distortable. Preserve
individual contribution, private Outcome, and attributed cueing; never let a
Vesper-authored group reconstruction become shared truth.

AI-edited imagery has also been shown to increase false recollection in a
preregistered experiment. Record, reconstruction, Vesper interpretation,
human-authored meaning, and creative transformation need separate truth and
presentation states. [Synthetic Human Memories](https://arxiv.org/abs/2409.08895)

## 9. Canon and implementation findings

### 9.1 The itinerary contradiction

Current documents contain two superficially conflicting statements:

- the Product Model retains one living Trip itinerary as shared operational
  truth; and
- the Plan/Occasion lifecycle and experience-graph decisions say an itinerary
  is viewer-relative and never durable multiplayer authority.

Reconcile them as follows:

> **No itinerary presentation or generated composition is authority. During
> migration, the retained Trip itinerary store remains the compatibility write
> owner for Trip scheduling and execution. Shared consequence authority
> increasingly belongs to Plan, Occasion, Decision, Commitment, provider, and
> Occurrence owners. Itinerary is the high-resolution Trip projection over
> those truths, not the company ontology.**

The thread may render operational sequence and receipts. It cannot itself own
current truth; it re-reads the owner when opened or acted upon.

### 9.2 Artifact terminology is overloaded

The recent design exploration uses “artifact” for generated, dynamic UI while
the canonical Product Model uses Artifact for brought or captured source
material and Composition/Instrument for returned value. Preserve the canonical
engineering distinction. Decide later whether the consumer vocabulary needs a
more unified surface word.

### 9.3 Existing foundations worth preserving

- clean graph Plan, Occasion, Decision, Commitment, invitation, Occurrence,
  Outcome, and viewer-relative projection code;
- five-axis contribution authority and owner handoff;
- revision, idempotency, action receipt, and authoritative readback patterns;
- one-way Trip-to-graph adapter for consequential identity;
- fixture-only CompositionBrief, SemanticResultEnvelope, circulation, and
  adaptive projection work;
- native client ownership of root-specific rendering; and
- four-root placement and handoff contracts.

### 9.4 Important gaps

1. No accepted lightweight prospective member inside Plan.
2. No production Plan projection envelope with dependency revisions,
   freshness, opaque actions, and fallback.
3. Occasion projection lacks explicit lane semantics and distinct membership
   or constitution epochs for invalidation.
4. Legacy shared-memory documents lack per-item authorship, subject, audience,
   grant, and withdrawal.
5. Legacy observation and Personal Memory paths can still produce profile-first
   inference without the contribution gate.
6. Social audience is too coarse for co-affected subjects and transformed
   projections.
7. Human-rated additive value, creepiness, transfer, and lapse-return evidence
   remains largely uncollected.

## 10. Recommended implementation and research sequence

### Phase A — adjudicate semantics before schema

1. Accept or reject PlanItem as one Plan-owned child—not an aggregate.
2. Accept the four projection lanes: shared core, audience lane, personal
   overlay, and system assessment.
3. Accept that Day, Night, Shape, and whole itinerary are projection scopes.
4. Resolve itinerary wording in canonical docs.
5. Preserve Artifact/Composition/Instrument engineering terminology.

### Phase B — fixture contracts

1. Define `PlanEntryProjectionV1` as a tagged read union over candidate
   PlanItem, Commitment, and legacy Trip entry adapters.
2. Define `PlanProjectionEnvelopeV1` with owner/dependency revisions,
   freshness, lane, semantic family, actions, and text fallback.
3. Extend the Brooklyn Occasion fixture through host, guest with private
   constraint, contributing guest, and nonparticipant.
4. Extend the Maya-in-Paris social fixture through Places, Home, private Keep,
   acknowledgment, Open together, expiry, and revocation.
5. Trace twenty real evidence items through Source → Claim/Anchor → episode →
   relationship/pattern candidate → Opening/application → Outcome/correction.

### Phase C — smallest production semantics

Only after the fixtures require it:

1. add minimal `plan_items` persistence and revisioned Add, Update, Remove, and
   Promote commands;
2. keep legacy Trip blocks behind an adapter and never dual-write consequence;
3. productionize one read-heavy Shape/Sequence family;
4. productionize one authority-heavy Decision/Live family;
5. route Chat and direct manipulation through the same command layer; and
6. add dependency invalidation, stale treatment, readback, and receipt.

### Phase D — consumer studies

Run comparative studies rather than asking whether people “like Vesper”:

1. **Value-first capture:** useful return before retention versus review-first.
2. **Additive transformation:** paraphrase, factual report, evidence-led
   synthesis, identity interpretation, and silence.
3. **Projection legitimacy:** vary ordering, wording, omission, and available
   actions across viewers while preserving common ground.
4. **Creepiness grid:** event-level versus person-level inference, explicit
   versus passive evidence, visible versus hidden provenance, real versus
   cosmetic control.
5. **Social aperture:** object-native insertion versus generic activity feed.
6. **Structural transfer:** surface similarity versus mechanism-plus-difference
   versus present-only recommendation versus silence.
7. **Lapse and return:** current-value-first versus recap/catch-up after one
   day, one week, and one month.
8. **Dyadic memory:** attributed plural lanes versus merged AI group summary.

### Phase E — longitudinal proof

For 12–20 participants across at least two relevant occasions, measure:

- time to useful relief;
- additive value over the submitted fragment;
- contribution burden;
- later qualified consequence;
- second-occasion benefit;
- transfer success and negative transfer;
- source and authorship comprehension;
- correction propagation;
- perceived surveillance or creepiness;
- voluntary later contribution and lapse-neutral return; and
- human relationship consequence without response pressure.

Do not optimize on messages, uploads, stored Artifacts, Home opens, session
duration, streaks, or reflection responses except as diagnostics.

## 11. Do now, preserve, and defer

### Do now

- make the semantic decisions in Phase A;
- write the two projection contracts and multi-view fixtures;
- audit current Plan/Occasion projections for lane, audience, membership epoch,
  dependency, and freshness semantics;
- audit Personal Memory and Traveler Card as derived projections rather than
  person authority; and
- define the comparative behavioral protocol before production UI creates sunk
  cost.

### Preserve

- mature Trip itinerary execution and its operation gateway during migration;
- one-way graph adoption rather than bidirectional dual-write;
- current Contribution and Consequence authority;
- native root-owned visual composition;
- stable owner identity and revision; and
- silence, expiry, unknown, correction, decline, and withdrawal as valid
  outcomes.

### Defer

- generic server-driven UI or A2UI component trees;
- model-ranked renderer selection;
- full CQRS infrastructure or a separate projection database;
- event sourcing and CRDT collaboration;
- backfilling every itinerary block into the clean graph;
- nested PlanItem structure, custom permissions, and manual ranks;
- generalized public discovery or follower feeds;
- global relationship, familiarity, receptivity, or autonomy scores;
- automatic profile learning from passive behavior; and
- persisting every projection.

## 12. Decision docket

### Recommended for acceptance

1. **Common-ground rule:** shared operational facts remain identical at one
   owner revision; projections personalize lawful relevance and expression.
2. **Projection lanes:** shared core, audience-scoped attributed lane,
   personal overlay, and expiring system assessment.
3. **PlanItem boundary:** one lightweight, private-by-default child of one
   personal Plan; not an aggregate or social authority.
4. **Promotion rule:** promotion creates a linked Commitment; consequence is
   never copied back into PlanItem authority.
5. **Projection ruling:** Day, Night, Shape, and itinerary are scopes/families;
   Occasion identity is earned by independent audience, lifecycle, authority,
   or shared consequence.
6. **Runtime boundary:** semantic family and evidence-aware payload from the
   server; root-native rendering and accessibility in the client; one typed
   command path for Chat and touch.
7. **Social circulation:** contributions land in the domain object they change;
   private Keep is distinct from acknowledgment, response, proposal, and
   contribution.
8. **Personal-world posture:** evidence, episodes, typed relationships,
   application, and Outcomes are primary; profile prose is derived.
9. **Consumer loop:** directed attention → immediate dividend → optional
   custody → later qualified consequence → Outcome/correction.

### Keep genuinely unresolved

- Whether explicitly named private intervals need saved projection identity or
  a Plan subsection after repeated refinding demand.
- Whether manual ordering earns a rank token after time-based ordering.
- Whether whole-Plan compositions are frozen, refreshable, or mixed; the
  current recommendation is a frozen authored body plus visibly live
  operational sections.
- How much of the shared core must remain visible inside every personalized
  composition to sustain common ground.
- Which lane labels remain legible without becoming a permission dashboard.
- What senders learn about delivery or opening without creating reply pressure.
- Which historical access former Occasion members retain.
- Which low-sensitivity attention traces earn reversible retention without an
  additional prompt.
- Whether model-ranked projection selection beats deterministic authored
  policy.
- How to measure silent capability improvement and social displacement without
  surveillance.

## Closing principle

Vesper does not need one rigid itinerary, one uniform Occasion page, one
personalized feed, or one memory profile to remain coherent.

It needs a stronger invariant beneath all four roots:

> **A small human trace enters under explicit authority; canonical owners keep
> common facts and consequences coherent; Vesper returns a lawful projection
> that adds value for this person now; any action reconciles through its owner;
> and only the evidence, authorship, Outcome, and causal application that earn
> continuity carry forward.**

That is broad enough to support trips, weekends, dinners, local curiosity,
social contribution, live recovery, and later transfer without turning any one
surface or container into the product.
