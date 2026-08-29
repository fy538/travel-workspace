---
doc_type: contract
status: active
owner: founder / product / architecture / engineering
created: 2026-08-29
last_verified: 2026-08-29
why_new: Defines one cross-repository boundary from human contribution through immediate value, retention, consequence, projection, receipt, and causal repair across Chat, Intake, Occasions, Home, Places, and Life.
supersedes: []
source_of_truth_for:
  - contribution-envelope
  - contribution-authority-resolution
  - contribution-consequence-treatments
  - contribution-receipt-and-repair
  - legacy-memory-conformance-boundary
---

# Contribution and Consequence — Cross-Repository Contract

## Purpose

Turn a question, observation, artifact, invitation, correction, or changing
situation into immediate value and the smallest justified consequence without
creating classification homework, hidden memory, false lived truth, or
unauthorized audience and action.

This charter implements the accepted [contribution-contract
decision](../decisions/2026-08-29-adopt-contribution-and-consequence-contract.md),
the accepted [structured contribution-use-grant
decision](../decisions/2026-08-29-adopt-contribution-use-grants.md),
the product [Interaction Grammar](../working/vesper-experience-constitution-and-interaction-grammar-2026-08-22.md),
and [Product Model](../../travel-agent/docs/product/Product%20Model.md).

## Owns—and does not own

This contract owns the boundary that every input path crosses before it may
retain evidence, create an inference, widen an audience, mutate canonical
state, or trigger an external consequence.

It does **not** own Person, Place, Source, Occasion, Plan, Commitment,
Occurrence, Outcome, provider, or publication truth. Their existing domains
remain sole mutation authorities. `ContributionEnvelope`, interpretation
candidates, and prepared consequences are storage-neutral coordination
contracts unless a later implementation decision promotes a durable shape.

## 1. The contract in one view

```text
human or world event
  -> resolve gesture + immediate job
  -> compile only authorized context
  -> establish Source custody and evidence roles when needed
  -> contribute immediate value
  -> choose: stop | private reversible consequence | material boundary
  -> apply only through the canonical owner
  -> authoritative readback
  -> quiet receipt, correction, Undo, or silence
  -> project to Home / Chat / Places / Life / Occasion only under owner authority
```

The order is binding: **value precedes classification or continuation work**.
An answer may end. A source may persist without a person-level inference. A
prepared consequence may expire without becoming a durable object.

## 2. Gesture and immediate job

The medium does not determine the gesture. A photograph can support an Ask,
constitute a Bring, accompany a Point, or be explicitly Shared. Resolve the
human job from language, invoked UI, channel, and current context.

| Gesture | Default contract |
| --- | --- |
| **Ask** | Use authorized context for the answer; no new durable personal state |
| **Point** | Preserve the person's explicit observation as private source-bound attention when clear and useful; do not promote it into identity or preference |
| **Bring / Import** | Admit the deliberately supplied Source under its custody policy; interpret provisionally; create no Occurrence or meaning claim by implication |
| **Keep** | Retain the named Source, interpretation, intention, or Outcome under the stated owner and scope |
| **Share / Address / Invite** | Prepare a bounded audience consequence; preserve author and audience; cross the boundary only under resolved authority |
| **Decide / Act** | Apply the named consequence through its canonical owner when authority and reversibility permit |
| **Correct / Release** | Supersede or remove the named relation and invalidate its dependent state |

One turn may contain several gestures. “What does this ticket say?” is normally
Ask with a supporting Source. “This is the ferry I used—add it to my August
journey” combines Point, Bring, and Keep, but the explicit occurrence claim
still belongs to the person rather than to the ticket.

Immediate jobs remain separate: answer, understand, orient, compare, explore,
decide, coordinate, act, address, preserve, document, correct, or continue.
Two identical files may therefore receive different retention and consequence
decisions.

## 3. Five independent authority axes

Every path resolves these axes before a durable or external effect:

1. **Use:** which immediate job, named purposes, and eligible consumers may use
   the contribution?
2. **Retention:** may the Source, governed claims, and generated projections
   persist independently—and for how long?
3. **Inference:** what semantic distance, learning target, and learning level
   may affect later judgment, and at which Source, Place, Occasion, person, or
   relationship scope?
4. **Audience:** who contributed, who is a subject or affected principal, who
   has custody, and who may see which projection, in whose voice, under which
   expiry and revocation rules?
5. **Action:** may Vesper advise, propose, prepare, apply a reversible owner
   command, contact, commit, transact, publish, or do nothing—and through which
   canonical owner?

Authority is resolved in this order:

```text
explicit instruction in the current turn
  -> existing narrow mandate or setting
  -> current channel / Occasion constitution
  -> gesture default
  -> conservative fallback
```

Confidence, relevance, repetition, model judgment, organizer convenience, and
silence never expand authority. Current explicit intent may narrow or revoke a
prior grant.

### 3.1 Retention is a three-layer lifecycle

Retention is not one `derived_only` versus `source_and_derived` choice. Policy
resolves three independent layers:

| Layer | Policy states | Meaning |
| --- | --- | --- |
| **Source** | `none`, `transient`, `reference_only`, `retained_private`, `retained_shared_projection` | Whether original material or a resolvable Source remains in custody, for whom, and until when |
| **Claims** | `none`, `turn_candidate`, `session_working`, `scoped_governed` | Whether an observation or interpretation survives, with truth, evidence, scope, purpose, and repair |
| **Projections** | `none`, `cached_recomputable`, `published_snapshot` | Whether a card, map, story, summary, status, or social view persists and how it responds to correction |

`reference_only` is the minimum receipt, hash, provider identifier, or
tombstone needed to explain lifecycle and prevent resurrection. It must not
retain enough content to recreate a deleted Source.

Generated projections never become evidence or independent authority. They
either recompute from their governed dependencies or remain an explicitly
authored/published snapshot with honest correction limits.

### 3.2 Gesture and affordance resolve Ask versus Bring

Use language and the invoked affordance together:

| Entry | Default |
| --- | --- |
| Source accompanying a question | **Ask:** transient Source processing, no new durable claim |
| Source deliberately sent alone in Chat | **Point/Bring:** private reversible Source custody after immediate value |
| Share sheet, forwarded message, or explicit Add affordance | **Bring:** private Source custody plus literal extraction; provisional interpretation |
| “Keep this” or explicit authored claim | **Keep:** admit only the named Source or claim |
| Ambiguous pasted item inside an active conversation | T0 unless retention is the invoked job or later language makes it clear |

No classification prompt precedes useful interpretation. A private T1 write
leaves a compact scope plus Correct/Undo. If plausible interpretations would
change Occurrence, audience, affected-person standing, public consequence, or
external action, prepare privately and use T2.

### 3.3 Expiry follows lifecycle before elapsed time

Natural completion, Moment end, Occasion end, provider deadline, correction,
revocation, or loss of present usefulness is the primary expiry event. A TTL is
a conservative backstop. Storage and eligibility for future influence remain
separate decisions.

V1 defaults:

| State | Default |
| --- | --- |
| Raw Source used only for Ask | Delete after processing; technical retry custody may last no more than 24 hours |
| Turn/session working state | Expire after 24 hours of conversational inactivity |
| Unapplied Opening or recommendation | Expire when its Moment, availability, or practical relevance ends |
| Prepared provider consequence | Provider deadline, otherwise no more than seven days |
| Live Occasion operational state | Occasion end plus a 72-hour reconciliation window |
| Occasion inference | Discard after reconciliation unless admitted as separately governed evidence |
| Featured Status | Seven days by default; author may replace, extend, or withdraw |
| Unconfirmed semantic candidate | Seven days unless necessary to interpret a retained Source |
| Explicitly retained Source or authored Outcome | No arbitrary expiry; remains revisable until deletion, release, correction, or declared scope end |
| Location or availability | Current Moment or active Occasion only; use the shortest operationally sufficient window |

These values are product defaults, not evidence that longer retention is
authorized. Operational evidence may tune a backstop without widening purpose.

### 3.4 Learning names its target and level

“Vesper learned” is incomplete. Every update names one target:

1. **world** — a venue closed, a ferry was delayed, or a fact changed;
2. **product** — a treatment was exposed, saved, dismissed, or led to an action;
3. **situation** — the current route, group, energy, weather, or decision state;
4. **person** — a governed claim about one individual; or
5. **relationship** — a scoped claim about particular people together.

Learning also resolves a level:

| Level | Scope | Default consumers | Must not become |
| --- | --- | --- | --- |
| **L0** | Aggregate service telemetry | Reliability and product evaluation | Personalized truth |
| **L1** | Turn/session working state | Current response and ranking | Durable preference or identity |
| **L2** | Occasion/Plan operational state | Current Occasion, Home, Places, and live engine | Cross-context person or relationship trait |
| **L3** | Governed evidence | Named authorized capabilities | Unscoped global identity |
| **L4** | Derived projection | Viewer- and surface-specific expression | Independent authority or evidence |

Views, dwell, read receipts, silence, ignored suggestions, and unanswered
prompts default to L0–L2 product or situation use. They do not become L3 person
or relationship claims. Repetition may justify cautious ranking or an offer of
a narrow mandate; it does not promote itself into permission.

### 3.5 Outcome learning preserves causality

Keep this ladder explicit:

```text
Opening surfaced
  -> exposure
  -> deliberate save, proposal, or selection
  -> Commitment or provider confirmation
  -> supported Occurrence
  -> authored or governed Outcome
```

No stage proves the next. Booking does not prove attendance; attendance does
not prove liking; liking does not prove identity or public contribution.

Before an Outcome affects later behavior, resolve its target, author, causal
link to Vesper, directly observed state, context, alternative explanations,
eligible consumers, and repair path. Product and situation learning can proceed
without a person-level claim. Personal and relational learning requires an
authored statement, correction, narrow mandate, or independently supported
governed evidence.

Do not append routine review questions. Personal meaning should emerge through
voluntary contribution, correction, or a later consequential ambiguity—not a
mandatory after-action survey.

### 3.6 Purpose is distinct from audience

Human verbs establish legible default purpose:

| Verb or mode | Default permitted purpose |
| --- | --- |
| **Ask** | Current answer only |
| **Bring / Keep** | Private custody and authorized continuity |
| **Send / Address** | Delivery to named recipients with attribution |
| **Contribute** | Bounded Occasion coordination, synthesis, or memory under that Occasion |
| **Feature as Status** | Human-authored audience projection for a limited time |
| **Publish to Place** | Governed wider Place contribution |
| **Act** | Complete the named provider or external consequence |

An audience grant never implies every purpose. A group-visible message may
support the current Decision without entering personal preference synthesis. A
Status may open a social possibility without granting ambient location,
invitation, messaging, or public Place use.

Every multiplayer flow preserves distinct roles for contributor, subject or
affected principal, custodian, recipient, and canonical owner. One person may
hold several roles; policy may not assume they always coincide.

### 3.7 Co-owned material separates custody from projection

A contributor may retain their private original without acquiring unilateral
authority to publish another person's identity, location, relationship, or
experience. Occasion contribution creates an Occasion-bounded projection, not
automatic ownership by every participant.

An affected person can narrow future Vesper projections that identify or
locate them without ordinarily deleting the contributor's private original.
When authorities conflict, use the least permissive applicable rule for the
wider projection. Prefer omission, crop, blur, abstraction, or private-only
custody to a negotiation workflow. Public Place or Status use is a separate
boundary from Occasion sharing.

### 3.8 Inspect evidence and consequence, not personality

Consequential Home and Places projections must offer an inspectable “Why
this?” grounded in concrete Sources, Occurrences, Outcomes, permissions, and
current conditions. Life exposes those elements inside their episodes,
Occasions, Places, and relationships with controls to:

- correct what happened;
- detach material from an episode;
- exclude it from resurfacing;
- release an interpretation;
- change audience; or
- delete or revoke the original.

Global settings own connectors, mandates, retention controls, protected
constraints, and complete Source access. Life must not become a universal
inferred biography, personality dashboard, or maintenance queue.

### 3.9 Connected services are narrow adapters

Permission to retrieve from Maps, email, calendar, photos, messaging, booking,
location, or health services does not authorize retention, inference, sharing,
or write-back. Each adapter declares Source custody, requested fields, purpose,
eligible consumers, expiry, action capability, and correction.

Adoption order:

1. user-directed import or forwarding;
2. invoked narrow retrieval for a current job;
3. Plan- or Occasion-bounded monitoring; then
4. ambient ingestion only after its narrow value, comprehension, and controls
   are established.

Begin with forwarded reservation email rather than a full inbox, selected
photos rather than camera-roll scanning, shared Places rather than complete
location history, availability rather than all calendar content, and derived
live state rather than raw health history. Search, prepare, hold, authorize,
execute, and reconcile remain separate provider transitions.

## 4. Contribution envelope

Every ordinary Chat, share/intake, Occasion, proactive, correction, or provider
input must be representable by one envelope before retention or consequence:

```yaml
contribution_envelope:
  id: null
  initiator:
    actor: null
    kind: person | companion | vesper | provider | world_change
    channel: private_chat | shared_chat | share_sheet | occasion | proactive | system
  gesture: ask | point | bring | import | keep | share | address |
    invite | decide | act | correct | release
  immediate_job: answer | understand | orient | compare | explore | decide |
    coordinate | act | address | preserve | document | correct | continue
  authored_payload:
    text: null
    source_refs: []
    author: null
    inherited_audience: []
  context_scope:
    place: null
    moment: null
    occasion: null
    plan: null
    relationship: null
  authority:
    use:
      immediate_job: null
      allowed_purposes: []
      allowed_consumers: []
    retention:
      source: none | transient | reference_only | retained_private |
        retained_shared_projection
      claims: none | turn_candidate | session_working | scoped_governed
      projections: none | cached_recomputable | published_snapshot
    inference:
      semantic_scope: null
      learning_target: none | world | product | situation | person | relationship
      learning_level: L0 | L1 | L2 | L3 | L4
    audience:
      contributor: null
      subjects: []
      custodian: null
      recipients: []
    action:
      authority: null
      owner: null
    basis: null
    expires: null
  evidence_roles: []
  truth_boundary:
    allowed: []
    forbidden: []
    unresolved: []
  immediate_contribution:
    operation: null
    claim_refs: []
    trust_footprint: []
  prepared_consequence:
    owner: null
    command: null
    affected_principals: []
    materiality: null
    reversibility: null
    authorization_mode: null
  treatment: T0 | T1 | T2
  correction_paths: []
```

The envelope may be compiled incrementally. The interpreter may propose
classification, truth, and authority; it cannot grant effective retention,
audience, or action to itself. Policy resolves authority and the domain owner
persists truth.

## 5. Evidence and truth chain

Use the narrowest chain needed:

```text
Source
  -> Observation
  -> Interpretation
  -> governed Claim
  -> canonical owner mutation, if any
  -> viewer-relative Projection
  -> Receipt
```

- **Source:** authored or observed material with custody, provenance, scope, and
  reuse rights.
- **Observation:** what the Source directly supports, preserving author and
  evidence locator.
- **Interpretation:** a bounded relation or explanation whose uncertainty and
  source dependencies remain visible.
- **Claim:** a typed assertion admitted for a named use and owner.
- **Mutation:** the owner-accepted state change; assistant prose is not proof.
- **Projection:** a surface- and viewer-relative expression over owner truth.
- **Receipt:** authoritative readback, scope, and repair—not a claim that the
  assistant intended to act.

The truth ladder remains non-transitive:

```text
noticed -> asked about -> considered -> intended -> planned -> shared
        -> occurred/visited -> liked/disliked -> personally meaningful
        -> publicly contributed
```

No state implies the next. Tickets prove purchase or schedule, not boarding.
Photographs prove an image and possible scene, not authorship, consumption,
preference, visit, or meaning. A question proves current interest in an answer,
not durable taste.

## 6. Three visible treatments

| Treatment | When | Product behavior |
| --- | --- | --- |
| **T0 — answer or prepare privately** | Ask, immediate relief, exploration, or no justified continuity | Deliver complete value; create no new durable personal state; optionally expose sources |
| **T1 — apply privately, then receipt** | Clear Point/Bring/Keep or reversible private owner update with bounded truth | Apply the smallest source-bound consequence, then show quiet scope plus Correct/Undo |
| **T2 — preview the material boundary** | Audience change, affected principal, provider contact, spend, public effect, sensitive inference, weak reversal, or unresolved consequential truth | Prepare one exact effect and ask once at the boundary |

T0–T2 are presentation treatments, not the complete authorization model. The
internal M0–M6 modes still distinguish no boundary, optional opening, expressed
language, one-tap confirmation, affected principals, bounded mandate, and
explicit external/public authorization.

Explicit natural language may authorize a bounded reversible owner command
without a second confirmation. It does not bypass protected data, spend,
provider, publication, affected-person, or weak-reversal boundaries.

## 7. Point and Bring ruling

Apply T1 without prior approval only when all are true:

1. the gesture is deliberate rather than merely a Source attached to an Ask;
2. actor, Source, private owner, and intended scope are clear;
3. retained state is the Source, an authored observation, or a bounded
   source-local interpretation;
4. the path does not assert Occurrence, preference, identity, personal meaning,
   another person's state, or wider audience without separate authority;
5. the change is private and cheaply reversible; and
6. immediate value appears before the receipt.

If Place, time, author, ownership, Occurrence, or Occasion is ambiguous, retain
only what custody policy permits and keep interpretation provisional. Clarify
only when resolving the ambiguity changes truth or a later consequence.

This ruling does not mean “create everything and make the person clean it up.”
It permits low-cost private continuity precisely because person-level inference
and wider consequence remain blocked.

## 8. Receipt and causal repair

A T1 or T2-applied consequence must read back from the owner and be able to
explain:

- what changed and what did not;
- which owner accepted it;
- which Source or explicit instruction authorized it;
- its truth state, scope, audience, and expiry;
- which projections changed; and
- what Correct, Undo, Release, or revocation will affect.

Repair targets relations, not entire histories. “I bought the ticket but did
not take the ferry” retains the ticket, invalidates the occurrence, recomputes
journey and story projections, cancels dependent pending consequences, and
preserves an independently sourced later hotel check-in.

Deletion or correction must propagate through content-addressed or typed causal
lineage. Hiding one card while leaving the same false claim in Home, Places,
Life, a story, memory projection, or pending action is non-conforming.

## 9. Surface responsibilities

| Surface | Contribution responsibility | Must not become |
| --- | --- | --- |
| **Chat** | Lowest-friction Ask/Point/Bring/Correct entry; immediate value; private preparation; compact receipts | A mandatory workflow, generic memory intake, or owner of all truth |
| **Home** | Current-life projection of admitted value and justified consequences | A request feed, recap report, or hidden-inference display |
| **Places** | Place-relative truth, relationship, horizon, practical state, and governed contribution | A save repository, review directory, or private-memory owner |
| **Life** | Durable owner navigation, Sources, Occurrences, Outcomes, journeys, Occasions, correction, and continuity | An ingestion queue or personality dossier |
| **Occasion / Plan** | Shared or prospective consequence under participant and commitment authority | A container that merges private meaning or silently enrolls people |
| **Push** | Material, time-sensitive projection whose interruption is justified | A curiosity prompt, reflection request, or memory announcement |

The same Source, claim, author, audience, correction, and owner must survive
projection. A surface may change density or medium; it may not reinterpret
authority.

## 10. Multiplayer rules

- An authored payload may inherit the audience of the channel into which the
  person deliberately sends it. Private derivatives and private context do not.
- An attributed contribution remains attributable through every projection.
- A friend's content can appear in another person's private mosaic only within
  its original audience and revocation scope.
- Minimum-safe private constraints may filter or shape a shared consequence,
  but the public reason cannot reveal the constraint and the constraint does
  not authorize the action.
- Invitations create independent pending/accepted/declined/deferred states;
  being named is not participation.
- Shared Occurrence may converge; personal and relational Outcomes remain
  separately authored.

## 11. Memory conformance

Durable memory admits evidence; it does not convert interaction exhaust into a
verdict about a person.

Allowed with appropriate source and scope:

- explicitly authored preference, constraint, correction, intention, or
  meaning;
- independently supported Occurrence or Outcome;
- source-bound Place, Occasion, or relationship evidence;
- bounded behavior evidence whose future use does not claim preference or
  identity; and
- a narrow mandate explicitly granted by the person.

Not allowed as durable person inference by default:

- a question or search topic;
- ignored options, silence, response latency, dwell, view, or read receipt;
- an individual coordination vote generalized into taste;
- model-inferred personality, emotional investment, social role, or identity;
- a one-off selection generalized beyond its Occasion; or
- repetition treated as permission or autonomy.

Personal Memory, group profiles, affinity, and generated summaries are
projections over admitted evidence. They may not become a laundering layer that
erases source, truth type, scope, expiry, disagreement, or correction.

## 12. Current implementation alignment

### Reusable substrate

- Intake v2 separates custody, normalization, observation, semantic candidate,
  truth mode, evidence references, proposed versus effective authority, and
  correction paths.
- Conversation admission supports `answer_only` and bounded source references.
- Occasion, Invitation, Decision, Commitment, receipt, and causal-lineage
  substrates exist in varying levels of maturity.
- Chat and mobile already render compact receipt and correction primitives.

### Non-conforming or incomplete seams

- `travel-agent/backend/concierge/_prompts_skills.py` and
  `memory_tools.py` still encourage same-turn `observe()` writes for preference,
  personality, mood, emotional investment, and patterns of silence.
- `refresh_memory.py`, reflection, and Personal Memory synthesis can turn those
  observations into higher-authority narrative projections without the shared
  contribution gate.
- ordinary conversation does not expose a complete continuity-read/no-write
  posture equivalent to the contract's T0 promise.
- share capture currently leads with candidate review—“keep, correct, or
  remove”—before the target first-turn contribution proves value.
- causal correction across every Home, Places, Life, story, memory, social, and
  pending-action consumer is not certified.

Current code existence is implementation evidence, not conformance.

## 13. Migration order

1. Inventory every durable writer reached from ordinary Chat, inbound share,
   Occasion chat, proactive turns, reflection, and correction.
2. Add a storage-neutral contribution envelope and policy decision before those
   writers; do not begin with a universal contribution table.
3. Make Ask/no-write enforceable across observation, fact, note, reflection,
   exposure, and synthesis paths.
4. Permit T1 only through source-bound policy decisions with explicit repair;
   keep semantic candidates unable to self-grant authority.
5. Replace legacy Concierge memory instructions; stop preference, personality,
   emotion, and silence from becoming ungated observations.
6. Restrict synthesis to admitted evidence while preserving source, truth,
   scope, expiry, disagreement, and correction lineage.
7. Route canonical effects through existing domain owners and require
   authoritative readback.
8. Propagate correction, deletion, expiry, and revocation across every
   projection and pending consequence.
9. Move mobile capture from review-first to value-first, with T1 receipt or T2
   boundary appropriate to the gesture.
10. Validate the representative portfolio across ephemeral, continuity,
    operational, multiplayer, and causal-repair families.

## 14. Conformance portfolio

The canonical requirements matrix is the [Contribution Contract Fixture
Pack](../working/contribution-contract-fixture-pack-2026-08-29.md). It contains:

- table-stakes competence and no-write cases;
- continuity-bearing observation, food, and cultural cases; and
- architecture-bearing journey, operational, social, Occasion, and correction
  cases.

Conformance is structural. Copying target prose into a generic chat must not
preserve the value of an architecture-bearing case. The value must depend on
truthful object state, situated projection, governed authority, or causal
repair.

Later usability work may tune receipt prominence and repair language. It does
not authorize hidden retention or replace architecture review.

## Failure posture

When gesture, authority, or truth cannot be resolved safely, deliver whatever
bounded immediate value remains and stop before durable or external
consequence. Preserve the Source only under its custody policy, mark unresolved
interpretation honestly, and ask one question only if its answer changes a
material consequence. Never substitute a generic review queue, personality
inference, or trailing reflection prompt for missing value.
