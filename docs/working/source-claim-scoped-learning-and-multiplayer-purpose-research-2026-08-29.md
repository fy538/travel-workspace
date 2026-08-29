---
doc_type: working
status: active
owner: founder / product / architecture / research / privacy
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: "Resolves three architecture-bearing seams left open by the Contribution and Consequence Contract: independent Source and claim retention, learning from Outcomes without unauthorized identity inference, and purpose-bounded multiplayer information flow."
promotes_to: null
supersedes: []
---

# Source, Claim, Scoped Learning, and Multiplayer Purpose

## Research question

The accepted [Contribution and Consequence Contract](../systems/contribution-and-consequence.md)
already distinguishes Use, Retention, Inference, Audience, and Action. Three
questions remain too underspecified to implement safely:

1. What exactly persists when a person asks with, points to, brings, keeps, or
   shares a Source?
2. What may Vesper learn from behavior and Outcomes without converting a
   situation into an unauthorized claim about a person?
3. What may a multiplayer contribution *do*, beyond the simpler question of
   who can see it?

These are not three independent permission systems. They are different parts
of one information-flow contract. A contribution needs a Source lifecycle, a
claim lifecycle, a bounded learning target, and a named purpose before it can
power a future projection or consequence.

## Evidence discipline

This document separates three kinds of support:

- **Repository evidence** describes what current code and canon already do.
- **Research evidence** describes findings from cited HCI, privacy,
  recommender-systems, and multi-user work.
- **Product recommendation** is the proposed Vesper default inferred from both.

Research does not determine exact copy, expiry durations, or every consent
boundary. Those require product choices and later human research. Legal and
regulatory sources establish risk and useful design constraints; this document
is not legal advice.

## Executive finding

The current five authority axes are directionally correct, but two are too
coarse:

- **Retention** currently compresses Source custody and semantic claim
  retention into values such as `derived_only` and `source_and_derived`.
- **Use** asks what may shape a response, but does not yet name the downstream
  purpose or eligible consumers that a contribution may power.

The smallest correction is not a sixth universal object or more confirmation
dialogs. It is to make two axes structured:

```yaml
authority:
  use:
    immediate_job: understand
    allowed_purposes: [current_answer, private_continuity]
    allowed_consumers: [chat, private_home_projection]
  retention:
    source: retained_private
    source_expires: null
    claims: scoped_governed
    claim_scope: place_relationship
    projections: recomputable
```

The integrated product law is:

> A contribution may power only the smallest named purpose supported by its
> Source, authorship, scope, and affected-person authority. Visibility,
> relevance, confidence, repetition, and successful outcomes do not widen that
> purpose.

This produces an effortless product default: do the useful low-risk work
quietly, leave a legible receipt, and interrupt only when the next information
flow changes audience, affected-person standing, public consequence, spend,
provider contact, sensitive inference, or reversibility.

## 1. Source retention and claim retention are different decisions

### 1.1 Why the distinction matters

A plane ticket, photograph, voice note, and typed observation can each support
several layers of state:

```text
raw Source bytes
  -> Source identity, custody, and provenance
  -> literal extraction or observation
  -> interpretation
  -> governed claim
  -> generated composition or projection
```

Deleting, expiring, correcting, sharing, or retaining one layer does not imply
the same treatment for every other layer.

Examples:

- A person may ask what a menu says without wanting the photograph retained.
- They may deliberately add a ferry ticket to Life while never claiming they
  boarded the ferry.
- They may keep a photograph while rejecting Vesper's interpretation of what
  it meant.
- They may delete the original image but retain a user-authored note, provided
  that the note does not falsely claim the image remains available as evidence.
- They may share a redacted projection of a group photograph without granting
  every viewer the original file or private interpretations derived from it.

Microsoft's *Beyond Total Capture* argues that memory-support systems should
support distinct memory activities and selective cues rather than treat total
recording as memory itself. Recent work on personal-agent memory similarly
argues for typed evidence, provenance, audit, and rollback rather than an
undifferentiated chat cache. OmniQuery demonstrates the value of integrating
multiple captured media while retaining references back to the memories that
support an answer. The 2026 *AI Memory Gap* study adds a user-facing reason for
the distinction: in mixed AI workflows, people can misremember whether content
or ideas came from themselves or the AI. Vesper therefore needs visible
authorship and evidence boundaries, not only technically correct storage.

### 1.2 Repository evidence

The code already contains the beginning of the right split:

- `backend/inbound/semantic_contract.py` requires non-unknown observations to
  bind to a Source and evidence locator. Semantic candidates cannot grant
  themselves effective retention or capabilities.
- `retention_mode_for_admission()` keeps raw Source bytes ephemeral until a
  separately authenticated retention choice, while derived candidates have an
  independent lifecycle.
- `backend/core/models/admission.py` carries Source references rather than raw
  bytes in the admission envelope.
- `backend/concierge/ambient_intent.py` persists only deterministic bare Place
  labels and exact time windows as narrow private working state.

The missing piece is representational. Both `AdmissionRetention` and
`RetentionAuthority` still collapse multiple lifecycle questions into one
enum. Ordinary Concierge memory paths are less disciplined and can convert
conversation into agent-authored observations that later synthesis treats as
personal truth.

### 1.3 Recommended retention contract

Treat **Retention** as a structured policy over three independent layers:

| Layer | Useful states | Meaning |
| --- | --- | --- |
| **Source** | `none`, `transient`, `reference_only`, `retained_private`, `retained_shared_projection` | Whether original bytes or a resolvable Source remain in custody, for whom, and until when |
| **Claims** | `none`, `turn_candidate`, `session_working`, `scoped_governed` | Whether literal observations or semantic claims may survive, at what truth state and scope |
| **Projections** | `none`, `cached_recomputable`, `published_snapshot` | Whether generated cards, stories, maps, summaries, or social views persist, and whether they must recompute after repair |

`reference_only` should not become a loophole for indefinite shadow retention.
It means the minimal receipt, hash, provider identifier, or tombstone needed to
explain lifecycle and prevent resurrection. It must not preserve enough
content to recreate a deleted Source.

Claims must additionally retain:

- author and subject;
- truth mode and uncertainty;
- evidence dependencies;
- context and temporal scope;
- permitted purpose and consumers;
- expiry and revocation;
- correction path; and
- invalidation behavior when a dependency disappears.

### 1.4 Gesture defaults

| Gesture and situation | Source default | Claim default | Product behavior |
| --- | --- | --- | --- |
| **Ask** with an attachment | Transient processing | No durable new claim | Answer completely; show citations when useful; do not make an ingestion receipt |
| **Point**: “The pasta here tastes different” | No Source unless one was provided | Retain the authored observation privately when the gesture is clear; no taste trait | Add immediate substance, then a quiet `Kept with this place · Correct` receipt if continuity was created |
| **Bring / Import** through an explicit add or share affordance | Retain the Source privately | Literal extraction may persist; interpretation remains provisional | Deliver value first; no visit, preference, meaning, or Occasion by implication |
| **Keep** a named Source or interpretation | Retain only the named layer | Admit only the named claim and its evidence | State what was kept, not “I’ll remember everything” |
| **Share / Address** | Personal custody does not automatically change | Create a viewer-specific projection under a named purpose | Do not copy the private Source and its entire claim graph into another person's memory |
| **Correct / Forget** | Delete, retain, or tombstone Source as requested | Supersede or remove dependent claims independently | Recompute projections and cancel dependent pending consequences |

The product should not ask people to classify every layer. It should infer the
low-risk default from the gesture and invoked affordance, expose scope in a
compact receipt, and ask only when plausible interpretations create materially
different consequences.

## 2. Learn from Outcomes without manufacturing identity

### 2.1 “Learning” has several targets

Current product language risks collapsing five distinct updates into “Vesper
learned about you”:

1. **World model:** the restaurant was closed; the ferry was delayed.
2. **Product-performance model:** this opening was saved, dismissed, or led to
   an action in this context.
3. **Current situation:** this group changed route; the person has ninety
   minutes; rain made the outdoor plan unsuitable.
4. **Person claim:** the person dislikes long tasting menus or cares about
   ancient founding myths.
5. **Relationship claim:** two people tend to enjoy wandering together or one
   person often carries coordination work.

The first three can often improve immediate value without asserting the fourth
or fifth. That is Vesper's main escape from the false choice between “never
learn” and “silently build a personality dossier.”

### 2.2 Research evidence

Implicit behavior is useful but semantically weak. Google's People + AI
Guidebook warns that a click or other interaction can reflect temporary
curiosity, dismissal, or social communication rather than a durable request
for more of the same. Recommender-systems research finds that exposure and
position shape clicks, that non-interaction is not equivalent to irrelevance,
and that post-click signals add information but remain context-dependent.
Session-based recommendation offers the constructive alternative: adapt to a
current session or situation without requiring a permanent profile.

The CHI 2019 Guidelines for Human-AI Interaction recommend remembering recent
interactions, updating cautiously, encouraging granular feedback, conveying
future consequences, and scoping services when intent is uncertain. Google's
guide likewise recommends making implicit collection visible, allowing people
to inspect and edit it, and connecting feedback to recognizable product
effects.

The 2025 study of agent-memory expectations found that people were surprised
by mundane facts and inferred personality retained from task conversations;
participants wanted awareness, transparency, correction, and memory scoped by
task, project, domain, or activity stage. This was a small preliminary study,
so it supports the shape of the problem rather than a universal UI rule.

### 2.3 A scoped-learning ladder

| Level | May update | May consume it | Expiry | Must not become |
| --- | --- | --- | --- | --- |
| **L0 — service telemetry** | Aggregate reliability, latency, safety, and feature metrics | Product evaluation | Bounded operational policy | Personalized content or individual truth |
| **L1 — turn/session state** | Current referents, temporary interests, recent comparisons, working constraints | Current Chat response and in-session ranking | Turn or session | Durable preference or identity |
| **L2 — Occasion/Plan state** | Participation, decisions, current route, weather, load, owned commitments, observed operational Outcomes | Current Occasion, Home, Places, and live engine within that context | Occasion lifecycle plus bounded archive | Cross-context taste or relationship trait |
| **L3 — governed evidence** | Explicitly authored preference, constraint, correction, intention, meaning, or well-supported Occurrence/Outcome | Named private or shared capabilities | Until expiry, correction, or release | Unscoped global identity |
| **L4 — derived projection** | Familiarity, affinity, generated summaries, rankings, stories, and openings recomputed from L1–L3 | Viewer- and surface-specific presentation | Recompute or expire | Independent authority or evidence |

This is a scope ladder, not a confidence ladder. Repeating an L1 behavior does
not automatically promote it to L3. Repetition may justify a low-cost opening
or a request for a narrow mandate; it does not become permission by accumulation.

### 2.4 Outcome admission test

Before an Outcome affects future behavior, the system should resolve:

1. **Target:** is this evidence about the world, the recommendation, the
   current situation, the person, or a relationship?
2. **Authorship:** who reported or performed it?
3. **Causality:** did Vesper actually contribute to the outcome, or did the
   event happen independently?
4. **Observation:** what is known—save, booking, attendance, completion,
   correction—and what is merely inferred?
5. **Context:** which Place, Occasion, companions, time, and constraints bound
   it?
6. **Alternative explanations:** exposure, position, price, weather, fatigue,
   social obligation, or lack of alternatives.
7. **Future use:** which named consumer will improve, and can it improve using
   situation state rather than a person claim?
8. **Repair:** what happens if the person says the event did not occur or the
   interpretation was wrong?

### 2.5 Default signal policy

| Signal | Safe default use | Prohibited default inference |
| --- | --- | --- |
| View, dwell, or read receipt | Session ranking and product diagnostics | “Interested in this topic” |
| Silence or ignored suggestion | No person update; possibly lower interruption pressure in the same situation | Dislike, consent, personality, or emotional state |
| Search or question | Answer and short-term referent continuity | Durable taste |
| Save | Persist relation to the object and improve related openings in the named scope | “This defines you” or blanket category preference |
| Explicit correction | Supersede the named claim and update the responsible decision rule | Generalized aversion beyond the correction |
| Vote in an Occasion | Resolve the Decision and improve current group coordination | Global personal preference |
| Booking or deliberate action | Update Plan/Commitment and operational expectations | Attendance, satisfaction, or meaning |
| Confirmed attendance | Admit Occurrence under its Source and context | Liking or personal significance |
| Explicit “I loved this because…” | Governed authored Outcome and possibly a scoped preference | Public profile or other-audience sharing |
| Repeated context-matched choices | Rank cautiously or offer a narrow setting/mandate | Silent durable trait or autonomous action grant |

### 2.6 What makes Vesper's learning differentiated

A general chatbot can reuse conversation history. Vesper's stronger immediate
advantage is not “more memory.” It is typed, situated continuity:

- the same object can be a Source, planned commitment, lived Occurrence,
  personal Outcome, and later Opening without those states collapsing;
- Place, time, people, Occasion, and live conditions bound what evidence means;
- the live engine can change a recommendation using current reality without
  rewriting personal identity;
- provenance and correction can causally repair Home, Places, Life, social
  projections, and pending action; and
- a new contribution can immediately connect to the person's governed life
  graph rather than merely retrieve a similar sentence from chat history.

The differentiated value is therefore **consequence-bearing continuity**, not
maximal recollection.

## 3. Multiplayer needs purpose, not only audience

### 3.1 Visibility is not permission to reuse

Audience answers “who may see this projection?” It does not answer:

- whether a group message may train a private preference model;
- whether an Occasion photo may appear in a friend's Home;
- whether a private constraint may explain a group recommendation;
- whether an addressed recommendation may become a public Place contribution;
- whether a person shown in a photograph has standing over publication; or
- whether a shared decision may create a relationship-level claim.

Contextual-integrity research describes appropriate information flow through
the sender, recipient, subject, information type, and transmission principle.
Privacy-in-action research adds an implementation warning: models that can
state a privacy rule still violate it under task pressure, while a separate
privacy gate substantially reduces leakage. Vesper should therefore enforce
purpose and affected-person policy structurally, not rely on the response model
to “be careful.”

Purpose should usually be made legible through stable product modes and compact
receipts, not a constant stream of permission dialogs. A 2025 contextual-
integrity study of ChatGPT users found widespread sensitivity and reluctance
around cross-service data integration; in its vignettes, procedural safeguards
such as consent, anonymization, and removal of identifying information changed
judgments more reliably than a purpose label alone. The implication is not that
purpose is unimportant. It is that naming purpose internally must be paired
with real constraints and understandable controls.

### 3.2 Interdependent privacy

Multi-party photo research shows that the uploader and other people depicted
can disagree about the appropriate audience, while mainstream controls often
give one uploader all-or-nothing authority. Research on social-network privacy
also shows that other people's posts, mentions, friend lists, and aggregation
can reveal relationships or attributes that a person did not disclose.

Vesper consequently needs at least three roles:

- **contributor:** who supplied or authored the material;
- **subject / affected principal:** whose identity, location, relationship,
  constraint, or experience the consequence affects; and
- **custodian / owner:** who controls the Source or canonical object.

They may be the same person, but the contract cannot assume that they are.

### 3.3 Purpose modes

| Mode | Permitted purpose | Default boundary |
| --- | --- | --- |
| **Private contribution** | Current answer, private continuity, private Home/Places/Life projections | No social visibility or other-person claim |
| **Addressed contribution** | Deliver a specific authored item to named recipients | Attribution preserved; no recipient-profile write or public reuse |
| **Occasion contribution** | Coordinate, decide, synthesize, or remember inside the bounded Occasion | No durable personal trait; personal Outcomes remain separately authored |
| **Ambient friend activity** | Open possibility through an explicitly shared status or artifact projection | May rank socially relevant material; may not infer the friend's private experience or the viewer's taste |
| **Co-owned material** | Private custody and bounded group use | Wider publication, identity, location, or relationship disclosure needs affected-person policy; redaction/abstraction may reduce the boundary |
| **Public Place contribution** | Help an allowed public or community Place surface | Separate explicit act; never inherited from private or Occasion sharing |
| **Provider/action payload** | Complete the named external action | Data minimization; cannot be repurposed for social or personal inference |

An audience grant does not imply every purpose in the row. For example, a
group-visible message can participate in the current Decision while remaining
ineligible for durable preference synthesis.

### 3.4 Recommended purpose fields

```yaml
information_flow_grant:
  contributor: person_a
  subjects: [person_a, person_b]
  custodian: person_a
  context: occasion_rome_weekend
  information_type: shared_photo_projection
  recipients: [occasion_participants]
  allowed_purposes: [occasion_coordination, occasion_recap]
  allowed_consumers: [occasion_chat, shared_life_occasion]
  forbidden_purposes: [public_place_contribution, private_trait_inference]
  transform: faces_visible_to_participants_only
  expires: occasion_archive_policy
  revocation: remove_future_projection_and_recompute
  evidence_refs: [source:photo_123]
```

This resembles the dynamic access-control direction in *Collaborative Memory*:
private and selectively shared tiers, provenance, retrospective permission
checks, and filtered read views. That paper is a technical preprint, so it
supports an architecture pattern rather than proving user acceptance.
GroupGPT offers useful separation between intervention timing, privacy
transformation, and response generation, but sanitizing group conversation is
not sufficient for Vesper: a sanitized message can still be used for an
unauthorized purpose.

### 3.5 Relationship and follow boundaries

The repository's Relationship Edge Decision Note already supplies an important
default: `follows` is directional ranking interest, not permission. A mutual
relationship or visibility grant remains a separate directional edge, and
relational state is scoped by person, Place, and companion.

Therefore:

- following may make an eligible public/status projection rank higher;
- following may not reveal location, membership, private artifacts, or a
  friend's inferred Place relationship;
- appearing together may create a candidate co-presence relation only under
  supported Occurrence and affected-person policy;
- group agreement may produce a Decision without producing a single group
  preference; and
- “people you know liked this” must be grounded in shareable authored or
  governed Outcomes, not inferred from silent behavior.

## 4. One integrated contract

The three research areas collapse into one **Contribution Use Grant**. The
existing `ContributionEnvelope` remains the coordination boundary; it does not
need to become a universal database table.

```yaml
contribution_use_grant:
  source_policy:
    custody: transient | reference_only | retained_private
    expires: null
    owner: null
  claim_policy:
    state: none | candidate | session_working | scoped_governed
    truth_mode: null
    scope: null
    evidence_refs: []
  learning_policy:
    target: none | world | product | situation | person | relationship
    level: L0 | L1 | L2 | L3 | L4
    eligible_signals: []
  flow_policy:
    contributor: null
    subjects: []
    recipients: []
    allowed_purposes: []
    allowed_consumers: []
    forbidden_purposes: []
    transform: null
  action_policy:
    authority: advise | propose | prepare | apply_reversible | explicit_external
    owner: null
  lifecycle:
    receipt: null
    correction_paths: []
    invalidates: []
```

### 4.1 Revised interpretation of the five axes

The five-axis vocabulary can remain stable if its internal meaning is sharpened:

1. **Use:** immediate job plus named purposes and consumers.
2. **Retention:** independent Source, claim, and projection lifecycle.
3. **Inference:** semantic distance and learning target/level.
4. **Audience:** recipients plus contributor, subject, custodian, and affected
   principals.
5. **Action:** externality, owner, materiality, and reversibility.

This is preferable to adding many user-facing modes. The complexity belongs in
policy and fixtures; the visible interaction remains T0 answer, T1 private
apply plus receipt, or T2 preview at a material boundary.

## 5. Scenario matrix

| Case | Retain | Learn | Permitted future use | Boundary |
| --- | --- | --- | --- | --- |
| “Translate this menu” + photo | Transient image; no durable claim | L1 referent only | Current answer | None |
| Share-sheet a ferry ticket into Life | Private Source + literal route/time extraction | L3 Source facts; no boarding claim | Journey organization, prospective/live logistics if relevant | T1 receipt |
| “I took this ferry” | Existing Source + authored Occurrence claim | L3 Occurrence in named journey | Life timeline, journey map, later sourced composition | T1 receipt |
| “The pasta tastes different here” | Authored observation scoped to dish/Place | L3 observation; no global taste trait | Immediate explanation, Place relationship, related openings | T1 receipt if retained |
| Ask about cliffs in Sorrento | No new durable state | L1 current curiosity | Current answer and session comparison | None |
| Save a generated cliffs comparison | Named generated artifact and its dependencies | Object relation; cautious scoped ranking | Home/Life continuity and related openings | T1 receipt |
| Dismiss a Home card | Optional L1/L2 suppression for that card/context | Product/situation target | Stop or reduce repetition of that treatment | No dislike claim |
| Book a restaurant Vesper proposed | Plan/Commitment and causal receipt | Product + situation; no satisfaction claim | Logistics, live adaptation, current Occasion | Action boundary based on spend/provider authority |
| Attend the restaurant | Governed Occurrence if supported | L3 Occurrence | Life, Place history, operational continuity | No liking claim |
| Vote “no” in group dinner decision | Decision contribution in Occasion | L2 Occasion state | Resolve current group choice | No global cuisine preference |
| Send Paris artifact directly to a friend | Personal Source; addressed projection | No recipient-profile or public learning | Delivery, reply, permitted private continuity | Attribution + revoke |
| Post “back from Nice and Sorrento” status | Explicit status projection with expiry | No hidden location history release | Ambient friend opening and ranking | Audience/expiry chosen or established |
| Add photo containing friends to an Occasion | Private or Occasion Source projection | L2 shared Occasion evidence | Occasion conversation/recap | Wider use blocked; affected-person handling |
| Friend's Paris experience appears in Home | No copy of private Source; eligible projection only | Viewer session ranking at most | Juxtaposition or social opening | Original purpose/audience/expiry preserved |
| Private dietary constraint shapes group options | Private governed constraint | L2 situation filtering | Minimum-safe group synthesis | Do not reveal the constraint or its owner |
| Correct “I bought it but did not take it” | Retain ticket; supersede Occurrence | Repair world/person graph | Recompute map, story, counts, openings | Quiet causal receipt |

## 6. Architecture implications

### 6.1 Reuse

- Preserve the Source → Observation → candidate/Claim separation in Intake v2.
- Preserve proposed versus effective capability separation.
- Use deterministic ambient intent as the model for narrow L1/L2 working state.
- Reuse canonical domain owners for Place, Occasion, Plan, Commitment,
  Occurrence, Outcome, and social relations.
- Reuse receipts and causal lineage; extend them across Source, claim, purpose,
  and projection invalidation.

### 6.2 Correct

- Replace single retention enums with a structured retention decision at the
  policy boundary; compatibility adapters may still emit legacy enums during
  migration.
- Put a policy gate before legacy `observe()`, reflection, memory synthesis,
  recommendation-event processing, and social projection.
- Require every behavioral producer to declare a learning target, scope,
  expiry, eligible consumers, and prohibited person inference.
- Treat implicit signals as L1/L2 by default. Only explicit authored claims,
  corrections, supported Occurrences/Outcomes, or narrow mandates enter L3.
- Add purpose and affected-principal checks to shared reads as well as writes.
  Retrieval-time checks matter because permissions, membership, and audience
  can change after storage.
- Render viewer-specific social projections from an authorized Source/claim;
  do not duplicate the whole contribution graph into each viewer's memory.

### 6.3 Do not build yet

- No universal `contributions` table merely because the envelope is shared.
- No permanent personality profile derived from event aggregation.
- No all-purpose “friends can see this” toggle that conflates audience and use.
- No model-prompt-only privacy enforcement.
- No generalized machine-unlearning project. Vesper first needs graph-level
  correction, revocation, deletion, and projection invalidation. Model-weight
  unlearning is a different technical and legal problem.

## 7. What research resolves—and what remains genuinely open

### Resolved enough for canon

1. Source custody and claim retention must be independent.
2. Generated projections cannot become their own evidence or authority.
3. Implicit behavior defaults to temporary context, product learning, or
   situation learning—not durable identity.
4. Outcome learning must name its target and causal basis.
5. Audience does not imply purpose; purpose and eligible consumers require a
   structural policy gate.
6. Contributor, subject/affected principal, recipient, and custodian must remain
   distinct in multiplayer.
7. Low-risk private consequences can remain effortless through T1 receipts;
   material information-flow changes use T2.

### Still open

1. **Ask versus Bring legibility.** When a person invokes a generic share sheet
   with no language, which affordance or immediate output makes the retention
   default predictable without asking them to classify it?
2. **Expiry durations.** Research supports bounded scopes, not the correct
   number of hours or days for session, Occasion, status, or candidate state.
3. **Outcome causality.** The code needs a reliable way to distinguish “Vesper
   suggested it,” “the person acted,” “the event occurred,” and “the person
   valued it.”
4. **Co-owned artifact conflict.** Face/location detection can identify a
   possible affected principal, but cannot decide who has standing or how
   disagreement should resolve.
5. **Derived-profile inspectability.** Life needs a useful correction surface
   for governed claims and consequences without becoming a creepy dossier or
   a maintenance queue.
6. **Purpose comprehension.** Users may understand stable modes such as direct,
   Occasion, status, and public better than abstract purpose language; this
   needs scenario-based formative research.
7. **Cross-service use.** Connecting Maps, messages, calendars, bookings, or
   health signals introduces source-specific expectations and potentially
   legal obligations not resolved by this general contract.

These are research and fixture questions, not reasons to delay the structural
contract. Exact defaults should be tested with scenarios and prototypes rather
than benchmarking current ChatGPT or the pre-pivot Vesper implementation.

## 8. Recommended next decision

Promote the following delta into the canonical Contribution and Consequence
Contract after founder review:

1. Retention becomes `{source, claims, projections}`.
2. Use becomes `{immediate_job, allowed_purposes, allowed_consumers}`.
3. Inference gains `{learning_target, learning_level}`.
4. Audience gains contributor, subject/affected-principal, recipient, and
   custodian roles.
5. Every retained or shared consequence gets a causal invalidation plan.

Then extend the existing fixture pack with the sixteen cases above. Do not
start implementation by designing tables. First certify that ordinary Chat,
share intake, Occasion contribution, Home/Places projection, behavioral event
processing, and correction can all produce and enforce the same policy
decision.

## Sources

### Memory, authorship, and provenance

- Sellen et al., [*Beyond Total Capture: A Constructive Critique of
  Lifelogging*](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/p70-sellen.pdf),
  Communications of the ACM, 2010.
- [*Users' Expectations and Practices with Agent
  Memory*](https://brennanjones.com/media/documents/publications/chiea25-666.pdf),
  CHI EA 2025.
- [*Mi-Memory: A Lifecycle Memory Framework for Personal
  AI*](https://arxiv.org/abs/2607.18975), 2026 preprint.
- [*OmniQuery: Supporting Complex Personal Memory Queries across
  Images, Screenshots, and Videos*](https://doi.org/10.1145/3706598.3713448),
  CHI 2025.
- [*The AI Memory Gap*](https://doi.org/10.1145/3772318.3791494), CHI 2026.

### Human–AI learning, feedback, and implicit signals

- Amershi et al., [*Guidelines for Human-AI
  Interaction*](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf),
  CHI 2019.
- Google PAIR, [*Feedback +
  Control*](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/),
  People + AI Guidebook.
- [*Preference Pollution: The Challenges of Implicit Feedback in
  Recommender Systems*](https://onlinelibrary.wiley.com/doi/10.1002/aaai.12055),
  AAAI 2023.
- Joachims et al., [*Effects of Position Bias on Click-Based Recommender
  Evaluation*](https://www.microsoft.com/en-us/research/publication/effects-of-position-bias-on-click-based-recommender-evaluation/),
  WSDM 2007.
- [*Leveraging Post-click Feedback for Content Recommendations*](https://doi.org/10.1145/3298689.3347037),
  RecSys 2019.
- [*A Survey on Session-based Recommender
  Systems*](https://www.sciencedirect.com/science/article/pii/S0925231224003291),
  Neurocomputing, 2024.

### Privacy, purpose, and multiplayer

- Nissenbaum et al., [*Operationalizing Contextual Integrity in
  Privacy-Conscious Assistants*](https://arxiv.org/abs/2408.02373), 2024.
- [*Understanding Privacy Norms Around LLM-Based Chatbots: A Contextual
  Integrity Perspective*](https://ojs.aaai.org/index.php/AIES/article/view/36735),
  AIES 2025.
- [*Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for
  LLM-Powered Agents*](https://arxiv.org/abs/2509.17488), 2025 preprint.
- [*Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic
  Access Control*](https://arxiv.org/abs/2505.18279), 2025 preprint.
- [*GroupGPT: An LLM-Based Assistant for Multi-Person
  Interaction*](https://arxiv.org/abs/2603.01059), 2026 preprint.
- Such et al., [*Photo Privacy Conflicts in Social Media: A Large-scale
  Empirical Study*](https://kclpure.kcl.ac.uk/portal/en/publications/photo-privacy-conflicts-in-social-media-a-large-scale-empirical-s/),
  CHI 2017.
- Thomas et al., [*unFriendly: Multi-Party Privacy Risks in Social
  Networks*](https://research.google/pubs/unfriendly-multi-party-privacy-risks-in-social-networks/),
  PETS 2010.
- European Data Protection Board, [*Opinion 28/2024 on certain data protection
  aspects related to the processing of personal data in the context of AI
  models*](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en).
- UK Information Commissioner's Office, [*Agentic AI: data protection and
  privacy risks*](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tech-horizons-and-ico-tech-futures/ico-tech-futures-agentic-ai/data-protection-and-privacy-risks/).
- US Federal Trade Commission, [*AI Companies: Uphold Your Privacy and
  Confidentiality Commitments*](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/01/ai-companies-uphold-your-privacy-confidentiality-commitments),
  2024.
