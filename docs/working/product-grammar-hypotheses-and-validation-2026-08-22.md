---
doc_type: working
status: active
owner: founder / product / research / design
created: 2026-08-22
last_verified: 2026-08-22
expires: 2026-09-21
why_new: Separates the empirical claims and proof program behind the August product grammar from product canon, journey definitions, and implementation-readiness evidence.
supersedes: []
source_of_truth_for: []
---

# Product Grammar Hypotheses and Validation Register

> Status: active working register
>
> This document does not declare product behavior shipped or the thesis proven.
> It names the claims that must survive behavioral evidence before the
> [Experience Constitution](vesper-experience-constitution-and-interaction-grammar-2026-08-22.md)
> and [product journey families](canonical-product-journey-families-2026-08-22.md)
> are promoted.

## 1. Proof standard

The product is not validated because a response is impressive, a connection is
pleasing, an itinerary is accepted, or a user saves an artifact.

Evidence should demonstrate one or more human deltas:

```text
practical relief
changed perception
increased capability
better shared action
greater mutual understanding
reduced organizer labor
appropriately calibrated trust
better later occasion
```

Measure each participant separately. Group acceptance can hide the least-served
participant, private discomfort, organizer burden, or unwanted exposure.

## 2. Claims under evaluation

| ID | Claim | Current status | What would weaken or falsify it |
|---|---|---|---|
| H01 | People will naturally bring fragments when Vesper solves the immediate job before organization | Supported by adjacent mobile-information and screenshot research; unproven for Vesper | People rarely bring natural fragments, cannot predict what will happen, or perceive intake as filing work |
| H02 | Attention-aware mediation is more valuable than maximal relevant explanation | Research-aligned; unproven intervention policy | Users prefer generic full answers across live contexts, or silence/defer decisions feel unreliable |
| H03 | One truthful bridge from prior cultural life can make unfamiliar material more legible | Psychologically plausible; direct product effect unproven | Connections feel contrived, creepy, distracting, or do not change later recall, perception, or action |
| H04 | Practical openings can create durable interest without a stored prior preference | Research-aligned; product transfer unproven | Users experience the opening as coursework or show no later independent discrimination or action |
| H05 | Landmark-grounded assistance can preserve immediate navigation while improving later spatial capability | Supported in bounded studies; Vesper behavior unproven | Immediate success worsens or later unaided orientation shows no material difference |
| H06 | Private plural input can produce a better shared experience than preference aggregation | Research-aligned; central multiplayer thesis unproven | Group-safe synthesis feels manipulative, organizer labor rises, or the thinnest participant receives less value |
| H07 | Borrowed perception and shared attention can deepen relationships without forcing consensus | Psychologically grounded; Vesper mechanism unproven | Vesper competes with conversation, perspectives feel exposed or stereotyped, or nominal sharing produces no relational value |
| H08 | Addressed openings create more meaningful social value than broadcast-like sharing | Research-aligned; audience and frequency unknown | Users prefer passive feeds, openings create pressure, or recipient relevance is routinely wrong |
| H09 | Reducing topic friction while preserving authorship makes connection easier and still authentic | Research-aligned; Vesper intervention unproven | AI involvement lowers perceived effort or authenticity even when the human writes the message |
| H10 | Task-scoped delegation earns more appropriate trust than blanket authority or confirmation at every step | Research-aligned; real-world willingness unproven | Users rubber-stamp, cannot understand the envelope, or refuse consequential delegation altogether |
| H11 | Provider-neutral experiential intent can survive handoffs without exposing private context | Architectural hypothesis | Providers cannot execute from minimum-safe projections, or reconciliation becomes less reliable than direct provider use |
| H12 | Earned continuity improves a second occasion without making Vesper feel clingy | Core compounding hypothesis | Resurfacing is merely pleasing, feels creepy, or produces no later capability, action, or relationship delta |

## 3. Research-grounded design constraints

These constraints have stronger external grounding than the specific Vesper
product claims, but they still require local behavioral validation.

### 3.1 Multiplayer

- Groups over-discuss common information and underuse unique private
  information, supporting private caucus before public advocacy.
- No universal aggregation rule fits safety constraints, ordinary preferences,
  expertise, vetoes, and delegated decisions.
- Joint attention and shared reality are not identical to shared preference.
- Nominally sharing an experience does not guarantee increased enjoyment or
  closeness; human attention and response must actually occur.

References: [hidden-profile research](https://www.sciencedirect.com/science/article/pii/074959789290049D),
[joint attention and bonding](https://pmc.ncbi.nlm.nih.gov/articles/PMC4849556/),
[shared-experience boundary conditions](https://pmc.ncbi.nlm.nih.gov/articles/PMC6472755/).

### 3.2 Situated attention

- Heat, fatigue, motion, crowds, navigation, and conversation compete with app
  interaction.
- Relevance and receptivity are separate decisions.
- Digital interpretation can support or displace companion interaction depending
  on timing and form.

References: [heat-stress meta-analysis](https://pubmed.ncbi.nlm.nih.gov/17915603/),
[walking dual-task experiment](https://pubmed.ncbi.nlm.nih.gov/30009681/),
[Sotto Voce](https://arxiv.org/abs/cs/0205053).

### 3.3 Continuity and capability

- Prior schemas, self-reference, curiosity, and insight can improve learning or
  recall.
- Situational interest can precede stable individual interest.
- Guided perceptual attention can help novices notice distinctions, but excessive
  analysis can damage the lived experience.

References: [four-phase interest model](https://doi.org/10.1207/S15326985EP4102_4),
[self-reference effect](https://pubmed.ncbi.nlm.nih.gov/909043/),
[insight and memory](https://pubmed.ncbi.nlm.nih.gov/26280758/).

### 3.4 Relationships and authorship

- People may underestimate how much others appreciate an unexpected reach-out,
  how much conversation partners like them, and the positive effect of a
  compliment.
- Assistance that appears to outsource meaningful relational effort can reduce
  perceived authenticity or satisfaction.
- Responsiveness means feeling understood, validated, and cared for; message
  frequency is not an adequate proxy.

References: [Surprise of Reaching Out](https://www.apa.org/pubs/journals/releases/psp-pspi0000402.pdf),
[liking gap](https://www.psychologicalscience.org/journals/psychological-science/0956797618783714/),
[AI assistance and relational effort](https://doi.org/10.1177/02654075231189899).

### 3.5 Delegation and trust

- Information acquisition, analysis, action selection, and implementation can
  have different automation levels.
- Users may prefer consequential software agents that require approval before
  completion over agents that act autonomously.
- Broad permission scopes cannot express task-specific transaction authority.

References: [levels of automation](https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf),
[travel-arrangement delegation experiment](https://doi.org/10.17705/1thci.00058),
[OAuth Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html).

## 4. Validation program

### V01 — Ten-day fragment and receptivity diary

**Participants:** 12-15 people living normal days.

**Method:** collect natural screenshots, photographs, tickets, links, questions,
invitations, voice fragments, and moments when help was desired but no app was
opened.

**Measure:** immediate job, artifact-intent mismatch, attention context, desired
treatment, desired consequence, privacy expectation, abandonment, and expiry.

**Decides:** H01, parts of H02, and the `immediate_job` vocabulary.

### V02 — Rome pair field study

**Participants:** 8-12 pairs across couples, close friends, and family where
practical and safeguarding constraints permit.

**Conditions:** ordinary chat plus Maps; generic personalized recommendation;
plural Vesper synthesis.

**Stressors:** heat, changing energy, asymmetric interests, private objection,
one cultural doorway, and deliberate silence.

**Measure separately:** practical success, organizer labor, least-satisfied
participant, felt exposure, perspective borrowing, conversation, and desire for
a later shared Occasion.

**Decides:** H06 and H07.

### V03 — Situated mediation study

**Conditions:** normal answer; action-first micro-answer; look-first shared cue;
silence or deferred treatment.

**Measure:** practical success, screen time, companion conversation, homework
feeling, depth requests, interruption regret, and delayed recall.

**Decides:** H02 and provides treatment-selection evidence.

### V04 — Spatial capability crossover

**Conditions:** conventional turn-by-turn; landmark-grounded directions;
progressively reduced assistance.

**Measure:** immediate arrival, wrong turns, unaided reversal, landmark
recognition, sketch-map quality, confidence calibration, and second-visit
navigation.

**Decides:** H05.

### V05 — Second-occasion continuity proof

**Method:** participants bring a movie, book, menu, conversation, or Place
encounter. Within 7-14 days, one source-grounded reactivation must change a real
observation, question, conversation, choice, or action.

**Failure condition:** resurfacing produces recognition or delight but no
present delta.

**Decides:** H03, H04, and H12.

### V06 — Addressed sharing and custody trial

**Conditions:** named recipient, recurring circle, and broadcast-like audience;
simple visibility controls versus explicit custody and resharing controls;
AI-written message versus structural prompt versus blank human-authored handoff.

**Measure:** initiation, recipient relevance, response freedom, authenticity,
comprehension, regret, correction, forwarding assumptions, and later contact.

**Decides:** H08 and H09.

### V07 — Delegated-action simulation

**Scenarios:** dinner reservation, train change, and flight booking across
escalating stakes.

**Conditions:** blanket authorization; confirmation at every step; task-scoped
authority with approval at the last responsible moment.

**Branches:** provider timeout, price change, substitute option, private group
constraint, duplicate attempt, expired authority, cancellation, and unknown
outcome.

**Measure:** comprehension, rubber-stamping, completion time, intervention,
duplicate action, recovery, trust calibration, and willingness to delegate again.

**Decides:** H10 and parts of H11.

## 5. Shared measurement vocabulary

### Immediate value

- task completed or friction reduced;
- time and attention cost;
- user-rated appropriateness of depth and timing;
- whether silence would have been preferable.

### Capability delta

- noticed a distinction independently;
- navigated or acted with less assistance;
- explained or applied the local logic;
- transferred understanding into another context.

### Multiplayer value

- independent benefit for each participant;
- least-served participant outcome;
- organizer labor;
- learned how the other person saw something;
- felt understood without being averaged or exposed;
- shared action quality despite different private meanings.

### Relational integrity

- human authorship remained recognizable;
- recipient felt free not to respond;
- outreach arose from a genuine referent rather than guilt;
- no relationship score or frequency target was inferred;
- Vesper withdrew when human conversation could carry itself.

### Trust and custody

- audience and authority comprehension;
- correction, dismissal, and release success;
- false occurrence or meaning claims;
- duplicate or unauthorized external action;
- provider and lived-outcome reconciliation;
- honest revocation and copy-retention expectations.

### Continuity

- present delta on the second occasion;
- source and reactivation basis understood;
- resurfacing regret or creepiness;
- evidence that the person or relationship became more capable rather than more
  dependent.

## 6. Explicit non-metrics

Do not use these alone as evidence of product value:

- screen time;
- content consumed;
- artifacts retained;
- places checked off;
- itinerary acceptance;
- message volume;
- social reciprocity frequency;
- notification opens;
- generated actions attempted;
- recognition or delight without a human consequence.

## 7. Decision and promotion log

For every completed study, record:

```text
revision and prototype
participants and relationship composition
conditions and journey families exercised
per-person outcomes
privacy or authorship failures
which hypotheses strengthened, weakened, split, or closed
grammar change required
journey change required
canon promotion explicitly authorized or denied
```

No single positive demonstration promotes the entire grammar. Promotion should
follow repeated evidence across personal, multiplayer, ordinary local, travel,
and consequential-action contexts.
