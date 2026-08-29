---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-28
expires: 2026-09-27
why_new: Synthesizes current HCI research across seven cross-cutting relationship, memory, initiative, sensemaking, situated, multiplayer, adaptive-interface, and longitudinal-evaluation seams that no single product canon or system contract can resolve independently.
promotes_to: null
supersedes: []
depends_on:
  - travel-agent/docs/product/Product Thesis.md
  - travel-agent/docs/product/Product Model.md
  - travel-agent/docs/product/Product Architecture Principles.md
  - travel-agent/docs/product/Vesper Editorial and Content Canon.md
  - travel-agent/docs/product/Vesper Expression, Medium, and Projection Canon.md
  - docs/decisions/2026-08-28-adopt-four-product-moves.md
  - docs/working/vesper-experience-constitution-and-interaction-grammar-2026-08-22.md
---

# Relational HCI for the Lived World — Architecture Research Round 1

## Question and status

Vesper is not merely a tool someone invokes, a travel planner, a recommender,
or an AI companion. Its ambition is to become a permissioned, longitudinal
intelligence across a person's relationships with the physical world, other
people, prior experience, and future action. What should human-computer
interaction research require of that relationship before product surfaces and
architecture harden around it?

This memo investigates seven architecture-bearing topics:

1. the relational contract and the boundary between contextual and synthetic
   intimacy;
2. memory, forgetting, personalization, and contextual integrity;
3. mixed initiative, receptivity, no-homework interaction, and earned autonomy;
4. sensemaking, epistemic agency, curiosity, and substantive user value;
5. situated interaction with Places, time, energy, movement, and real-world
   conditions;
6. plural agency, social authorship, common ground, and ambient sociality; and
7. adaptive interfaces and longitudinal evaluation.

It is research, not a new source of product truth. Existing canon wins where
the evidence is consistent. Findings marked as design implications or
hypotheses require a later decision before they authorize schemas, services,
surfaces, telemetry, or autonomous action.

## Executive verdict

The research strengthens Vesper's current direction, but it also makes the
product obligation stricter.

A research-level product definition emerges:

> **Vesper is the governed relational layer that turns authorized lived
> evidence and current reality into better understanding, open possibility,
> workable human and world consequences, and continuity across time.**

It can span travel, ordinary local life, media, memory, relationships, and
provider action because those are evidence and consequence domains for the same
transformation. It becomes unfocused when any domain appears as an independent
capability rather than participating in that causal spine.

The most coherent relationship model is **contextual intimacy without synthetic
intimacy**. Vesper may become unusually familiar with the authorized context of
a person's life, learn how to collaborate, remember what can improve a later
occasion, and prepare useful action. It should not simulate reciprocal need,
claim privileged authority over the person's identity, maximize emotional
attachment, or substitute itself for the people and world it is meant to help
the person inhabit.

The relationship succeeds when Vesper becomes:

- more contextually capable without becoming more possessive of attention;
- more proactive without becoming more presumptuous;
- more personalized without freezing the person into a profile;
- more operational without obscuring human authority;
- more socially useful without impersonating human effort;
- more adaptive without becoming structurally unpredictable; and
- more valuable over time without making dependence, engagement, or retention
  the definition of success.

The strongest concise formulation is:

> **Vesper should know the context more intimately while performing intimacy
> less. Its relationship with the person is justified by richer relationships
> with the lived world, other people, and future possibility.**

This is not only a tone rule. It implies separate architectural authorities for
memory, inference, audience, initiative, action, projection, and evaluation.

## 1. Method and evidence standard

### 1.1 Vesper evidence reviewed

The local review used the current Product Thesis, Product Model, What We
Believe, Product Vision and Scope, Product Architecture Principles, Editorial
and Content Canon, Expression/Medium/Projection Canon, the accepted four-move
decision, the recent experience constitution, and the recent place,
multiplayer, consequence, Home, and adaptive-composition investigations.

The Strategy task's preceding sixty hours supplied the concrete design
failures and stories against which research was interpreted:

- Rome in August made context, heat, energy, and experienced reachability
  inseparable from recommendation quality.
- The Colosseum/Aeneas/Odyssey example distinguished a retrieved personal
  connection from a genuinely new explanatory contribution.
- The Granola analogy established that the person supplies lived evidence and
  directed attention while the system performs reconstruction and intellectual
  work.
- The post-return New York work established that retrospective continuity must
  re-enter a life already moving forward.
- The Rome/Paris friend example made social perspective valuable when it
  changes understanding, not when it reports activity.
- Home was established as an output of accumulated attention and system work,
  not a questionnaire or reflection assignment.
- Home / Chat / Places / Life became stable root postures with adaptive
  interiors rather than one behavior or feature per tab.

### 1.2 External evidence hierarchy

The research prioritizes 2025–2026 CHI, CSCW, UIST, IUI, SIGIR/CHIIR,
RecSys, AIES, and peer-reviewed journal work. Older HCI, cognitive-science,
privacy, and CSCW research appears where it supplies a foundational construct
that the recent work still uses.

Claims in this memo use four evidence postures:

| Posture | Meaning |
| --- | --- |
| **Supported constraint** | Several empirical or mature theoretical sources justify treating this as a design boundary. |
| **Supported direction** | Research makes a mechanism plausible but does not validate Vesper's exact expression. |
| **Emerging signal** | Recent work is relevant but early, small-sample, preprint, workshop, or domain-specific. |
| **Vesper hypothesis** | A product inference to test; external work does not establish it. |

Laboratory task gains do not prove longitudinal benefit. Product adoption does
not prove a particular interaction mechanism. Higher engagement is not treated
as relationship quality. Fluent output is not treated as evidence of correct
interpretation.

## 2. One relational HCI model for Vesper

The seven topics are not independent. They form one interaction system:

```text
authorized lived evidence
        ↓
memory and purpose-limited context compilation
        ↓
situated judgment about value, receptivity, initiative, and authority
        ↓
make sense / open possibility / help it work / carry forward / silence
        ↓
root-native expression or governed action
        ↓
human/world/social consequence
        ↓
plural outcome, correction, forgetting, or bounded later reuse
```

Four separations are essential:

1. **Knowing is not authorizing.** Context can improve judgment without
   granting action authority.
2. **Remembering is not defining.** Retained evidence can support continuity
   without becoming a personality verdict.
3. **Adapting is not rearranging.** The system can choose a more fitting native
   expression while preserving navigation, ownership, and control.
4. **Relationship is not attachment.** Longitudinal trust and collaboration do
   not require simulated reciprocity or dependence.

## 3. Topic 1 — The relational contract

### 3.1 Relationship effects do not wait for a relationship label

Longitudinal memory, availability, adaptation, tone, and initiative create
relationship-like expectations even when a product calls itself only a tool.
Recent studies complicate any simple claim that AI companionship is either
inherently beneficial or inherently harmful. Outcomes differ by intensity of
use, anthropomorphic framing, disclosure, prior vulnerability, and what the AI
displaces. The evidence is not causal or mature enough to validate Vesper's
relationship model, but it is strong enough to prohibit accidental design.

The relevant boundary is not warmth versus coldness. It is:

| Contextual intimacy | Synthetic intimacy |
| --- | --- |
| Uses relevant authorized history to reduce work | Uses history to manufacture emotional obligation |
| Supports connection with people, Places, and activity | Competes with people and the world for attachment |
| States what it knows, did, cannot verify, or needs | Claims worry, longing, loneliness, pride, or lived memory |
| Adapts to a bounded purpose and situation | Turns familiarity into a global identity claim |
| Ends when the contribution or consequence is complete | Generates conversation to preserve engagement |
| Shows care through competence, restraint, and repair | Performs reciprocal need or fictional self-disclosure |

RECALLbot is a useful counterexample rather than a model for Vesper. Synthetic
biography, a constructed “We Memory,” and reciprocal disclosure increased
trust and disclosure in a laboratory study. That demonstrates the power of
these mechanisms, not their suitability for a world-facing product. Other
current research links intensive companion use and deep disclosure with
smaller social networks or lower wellbeing, while longitudinal controlled work
also finds that anthropomorphism and user differences mediate effects. Vesper
should not make attachment the mechanism by which it earns cooperation.

> **Care is a product responsibility, not a fictional inner state.**

### 3.2 The value is transitive and outward-facing

Vesper's relationship is justified when it improves a person's relationship
with something beyond Vesper: a Place becomes more intelligible; a weekend
becomes more possible; a friend receives a more thoughtful opening; a group
coordinates with less burden; a later occasion benefits from earlier evidence;
or the person learns to notice without assistance.

This makes **relational outwardness** a constitutional success condition. A
warm exchange with Vesper may be appropriate, but engagement with Vesper is
not the terminal outcome. The best contribution often ends with the system
receding.

### 3.3 Proposed relational contract

The product should make the following commitments operational:

1. **Purpose:** use context only for a current authorized job or a legible
   continuity purpose.
2. **Role legibility:** the person can predict what Vesper knows, may infer,
   may say, and may do.
3. **Honest asymmetry:** Vesper can be warm and attentive without claiming a
   human biography, needs, feelings, or reciprocal vulnerability.
4. **First-person responsibility:** “I” may name system work and limits—“I
   compared,” “I could not verify,” “I changed the route”—not invented
   interiority—“I missed,” “I worried,” “I remember how we felt.”
5. **Epistemic modesty:** evidence and bounded interpretation remain distinct
   from personal identity and meaning.
6. **Memory custody:** retained context has source, scope, purpose, audience,
   expiry, correction, and forgetting semantics.
7. **Human authority:** familiarity, trust, confidence, permission, and action
   authority remain separate.
8. **Withdrawal:** every relationally salient behavior has a stopping or
   receding condition; silence and disengagement incur no debt.
9. **Repair:** a violation changes system state and dependent projections, not
   only apology prose.
10. **Commercial integrity:** intimate context may not silently become a
    persuasion or partner-targeting asset.

This contract permits a recognizable Vesper voice. It prohibits needy
notifications, jealousy, exclusivity, simulated reciprocal disclosure,
fictional shared memories, and fallback conversation generated solely to keep
the person present.

### 3.4 Repair must restore calibrated reliance

Trust should not be maximized. Appropriate distrust after a privacy, authority,
or interpretation failure is rational. The recovery protocol should classify
the failure, stop dependent work, acknowledge the concrete consequence,
explain the source or rule that failed, correct or revoke it, invalidate
downstream projections, show a repair receipt, and reduce initiative in the
affected domain until it is explicitly or behaviorally re-earned.

Current repair studies favor explanatory or system-accountable repair over
rote apology; asking the person to help repair the AI did not improve trust in
one controlled experiment. The Vesper implication is direct:

> **Repair is accountable operational change, not emotionally elaborate
> prose.**

### 3.5 Open questions

- Should Vesper use “companion” if the term creates expectations of mutuality?
- How much stable voice can it have without implying a human-like self?
- How should voice, ambient presence, and location awareness tighten this
  contract?
- How can the product detect harmful displacement without moralizing frequent
  use or surveilling relationships?
- Can partner-supported commerce coexist with contextual intimacy without a
  hard separation between fulfillment and persuasion?

## 4. Topic 2 — Memory, forgetting, personalization, and contextual integrity

### 4.1 Memory is relationship-forming infrastructure

Users form expectations not only about what an agent stores, but how remembered
material will later be interpreted, combined, exposed, and acted upon. Recent
memory studies show both perceived relational gain and privacy strain. The
governing principle is contextual integrity: an inference can be accurate and
non-sensitive yet still be impermissible because its purpose, audience, role,
or downstream use violates the context in which the evidence was supplied.

Vesper's five permission axes—use, retention, inference, audience, and
action—are therefore more important than a binary memory preference. Quiet
learning should be **quietly legible**, not invisible:

- do not narrate every retention event;
- make first durable retention visible;
- make first cross-occasion reuse legible in context;
- require stronger visibility for cross-person, public, or third-party use;
- attach “why this?” and a real correction control to material
  personalization; and
- provide a deeper Life-level memory index without making routine governance
  homework.

### 4.2 Correct a current doctrine conflict

The as-built system charter currently says, “a dwell/visit signal outweighs a
stated interest.” That cannot remain a universal invariant. A visit can reflect
desire, obligation, convenience, group compromise, lack of alternatives, or
Vesper's own earlier recommendation.

The stronger rule is:

> **Evidence authority depends on the question. Behavior can confirm occurrence
> and outcome; the person remains the highest authority on current intent,
> preference, and meaning. Behavioral inference stays scoped, contestable, and
> lower-authority unless corroborated.**

This is not a claim that behavior is unimportant. It separates what behavior
can prove from what only a person can author. The existing global Personal
Memory narrative should likewise become a derived, purpose-limited projection,
not the canonical preference authority. Coherent prose can hide contradiction,
overstate confidence, and propagate one mistaken synthesis across many jobs.

### 4.3 The canonical unit is a governed claim, not a biography

A consequential memory claim needs at least:

```text
subject and dimension
value or hypothesis
source evidence and evidence type
explicitness and inference lineage
scope: domain / Place / companion / Occasion / time
confidence, valid time, and expiry
sensitivity and permitted purposes
audience, egress, and inference policy
status: active | disputed | retired
correction, supersession, and reactivation criteria
applications and dependent projections
```

The system should keep semantic distinctions among source evidence, hard
constraints, user-authored statements, derived claims, authored meaning,
exposure history, known-to-person receipts, current situational state,
authority, actions, and outcomes. They may share infrastructure, but they must
not collapse into one narrative or “what Vesper knows about you.”

Before cross-session admission, resolve source, subject, exact inference,
scope, sensitivity, purpose, expiry, allowed consumers, correction behavior,
and whether Vesper itself caused the behavior being interpreted. The last item
guards against endogeneity: selecting one of three Vesper-supplied restaurants
is not independent evidence of durable taste.

### 4.4 Familiarity is a vector, not an authority ladder

The product must reject this progression:

```text
more observations → more familiarity → more confidence
                  → more initiative → more authority
```

Instead retain independent values for domain/scope familiarity, evidence
reliability, present relevance, permission to use, sensitivity, initiative
earned through successful outcomes, and action authority. Extensive restaurant
history does not authorize social outreach. Repeated travel use does not prove
reliability about grief, accessibility, or relationships.

### 4.5 Forgetting is causal and semantic

A person may need to delete raw evidence, keep an artifact but stop learning
from it, retire a derived claim, expire a temporary fact, stop proactive recall,
remove a shared projection, revise authored meaning, or trigger a full
dependency-cascade deletion. These are different operations.

Correction or forgetting must invalidate dependent Home units, summaries,
suggestions, notifications, group-safe projections, provider jobs, and exports.
A visible deletion that leaves active derivatives is not forgetting. Valid
contradictions should remain representable: a person can like dense itineraries
and want rest on one trip, or value a Place in one relationship and avoid it in
another.

### 4.6 First-person authority and memory language

Vesper may interpret world evidence and bounded situations unsolicited when
grounded. Identity interpretation should normally remain a question,
hypothesis, or invited co-authorship.

| Attribution | Meaning |
| --- | --- |
| **You said** | explicit self-statement |
| **This happened** | observed or provider-grounded occurrence |
| **You kept** | explicit retention or authorship action |
| **Vesper noticed** | system-derived bounded pattern |
| **A possible pattern** | contestable interpretation |
| **Your meaning** | person-authored significance |

Prefer “From the Rome conversation…” over “our Rome memories.” The first names
evidence provenance; the second invents reciprocal lived experience.

### 4.7 Anti-patterns and open questions

Reject global “Who They Are” narratives, inferred identity as Home content,
click/save/visit preference inference without alternatives and constraints,
cross-companion leakage, transparency without effective controls, deletion
that leaves derivatives active, and a memory center requiring routine
maintenance.

Open questions include where first retention becomes visible, which
low-sensitivity attention traces may persist by reversible default, how one-time
evidence can influence later work, whether displaying a model of the person
anchors self-understanding, and how custody and portability work across
providers.

## 5. Topic 3 — Mixed initiative, receptivity, no-homework interaction, and earned autonomy

### 5.1 Initiative is not autonomy

The architecture-bearing unit should be an **epistemic or operational
contribution delivered under a bounded initiative contract**, not an agent
turn, recommendation, card, or automated task.

Vesper's initiative has several separable dimensions:

| Dimension | Strong default |
| --- | --- |
| Initiate private investigation | Vesper may do this broadly within purpose and custody limits |
| Interpret and compare evidence | Vesper, with provenance and uncertainty |
| Select what might matter | Vesper, explicitly compared with silence |
| Prepare a contribution or consequence | Vesper |
| Express it to the person | Conditional on value, receptivity, and demand |
| Execute a world-changing action | Human authority or a narrow active mandate |
| Monitor owner or provider state | Vesper within the requested or mandated domain |
| Reconcile, recover, and recede | Vesper, with honest limits and receipts |

This explains the desired relationship better than either “copilot” or “agent.”
Vesper can have high autonomy in research, preparation, monitoring, and
reconciliation while retaining narrow autonomy in communication, spending,
provider commitment, public expression, or action affecting another person.

The resulting law is:

> **Relevance earns eligibility. Receptivity earns treatment. Authority earns
> action.**

### 5.2 No homework means preserving the right human work

Recent HCI experiments distinguish full automation from guided collaboration.
GuidedCopilot produced greater control, utility, and learning for exploratory
work, while fuller automation remained useful for simple bounded tasks. Other
research found that forward-looking support integrated better into a person's
reasoning than complete recommendations, although requiring explicit rationale
entry added new burden.

Vesper should absorb **instrumental effort**:

- transcription, classification, reconstruction, comparison, and research;
- assembling context, checking constraints, and tracing dependencies;
- preparing alternatives, exact diffs, fallbacks, and action receipts;
- routing, monitoring, coordination, reconciliation, and recovery; and
- recalling evidence the person has already contributed.

It should preserve **constitutive effort**:

- directing attention;
- forming and revising judgment;
- deciding what is meaningful;
- expressing desire, care, identity, disagreement, or repair;
- choosing an audience;
- committing oneself or a group; and
- granting authority where another principal is affected.

This corrects a possible misreading of frictionless design. The goal is not to
remove all human effort. It is to remove clerical and coordinative labor around
the effort that constitutes a person's life.

> **Remove friction around thinking; preserve the thinking, authorship, and
> commitment that belong to the person.**

### 5.3 Receptivity is multidimensional

A contribution can be true, personalized, and potentially useful while still
deserving silence because the moment is wrong.

- **Operational receptivity:** a constraint changed or an action is becoming
  time-sensitive.
- **Cognitive receptivity:** the person has enough attention for explanation,
  curiosity, or comparison.
- **Relational receptivity:** a social opening is appropriate for the
  relationship, audience, and moment.

Current proactive-assistant studies show that aligned timing and conservative
initiative can improve usefulness and dependability, while persistent
suggestions can attract interaction yet be substantially less preferred. The
transferable principle is strong; invasive sensing methods are not. Vesper
should begin with sparse evidence such as active travel state, current Plan,
time pressure, user invocation, explicit deferral, calendar boundary, recent
interaction, and quiet expectations rather than physiological, gaze, or
continuous surveillance.

Proactivity can also threaten competence. Research on unsolicited AI help found
that it could lower satisfaction by undermining competence-based self-esteem.
That risk is amplified in a product close to taste, identity, and relationships.
Vesper should offer completed work rather than diagnose the person:

- prefer “Two plans still work after the delay”;
- avoid “You seem to be struggling with the change.”

### 5.4 Earned autonomy is local, scoped, and revocable

Vesper should not acquire one global autonomy level. A mandate must be bounded
across:

- verb and object;
- audience or provider;
- Place, Plan, Occasion, or context;
- financial and temporal limits;
- affected principals;
- expiry;
- reversibility class; and
- revocation mechanism.

Repeated acceptance may justify offering a mandate. It must not silently create
one. Confidence never grants permission.

Preview and confirmation should also be proportional. Plan-preview research
shows that review can improve inspectability but can also mislead when a
plausible plan is wrong and burden people with lengthy verification.

| Consequence | Default treatment |
| --- | --- |
| Local, reversible, self-owned | Apply only under authority; show honest receipt and undo |
| Material but bounded | Show the exact consequential diff |
| Affects another principal | Route the decision to that principal or the temporary constitution |
| Public, financial, provider-side, or weakly reversible | Require exact authorization |
| Material ambiguity remains | Ask one necessary question |
| No authority or insufficient value | Prepare privately, offer, or remain silent |

Uniform confirmation is not safety. It transfers the system's uncertainty into
human homework.

### 5.5 Architecture implications

The initiative contract should be able to represent:

```text
initiative origin: asked | detected | anticipated
intervention class: epistemic | operational | relational
receptivity basis + confidence
demand and interruption cost
competence / identity sensitivity
authority domain + mandate reference
affected principals
reversibility: local undo | compensatable | irreversible
temporal expectation + expiry
invalidation dependencies
reason silence loses
```

Authority enforcement remains deterministic and separate from model judgment.
A bounded-mandate registry should express verb × object × audience × context ×
limits × expiry × revocation. A model may propose an action inside the mandate;
the policy layer determines whether it actually fits.

The system must also separate three judgments:

1. **Contribution admission:** is the work grounded, new, and useful?
2. **Treatment:** does it deserve Home, Chat, Places, Life, Push, or silence?
3. **Authorization:** may any proposed consequence cross the relevant boundary?

A strong contribution can lose to silence because the person is unreceptive. A
weak contribution must not be rescued by good timing.

### 5.6 Anti-patterns and open questions

Reject:

- a global autonomy slider or confidence-based authorization;
- mandates inferred from repeated acceptance;
- confirmation before every reversible step;
- proactive help framed as diagnosis, competence correction, or identity;
- “undo” after another person or provider has already observed an irreversible
  consequence;
- asking the person to classify, summarize, or justify before value appears;
- persistent resurfacing after deferral or dismissal; and
- treating engagement with a proactive intervention as evidence that the
  intervention was appropriate.

Open questions include what sparse evidence may support receptivity without
surveillance, when undo remains honest after social exposure, what natural
language counts as a bounded mandate, and how proactive norms vary across
cultures, accessibility needs, and neurotypes.

## 6. Topic 4 — Sensemaking, epistemic agency, curiosity, and substantive value

### 6.1 The unit of value is a semantic or capability delta

Fluency, personalization, relevance, and surprise do not establish that Vesper
contributed value. Sensemaking requires a **representational gain**: after the
contribution, the person can notice, understand, distinguish, explain, decide,
converse, or act in a way that was not previously available.

The Editorial Canon's operations—restructure, explain, differentiate, and
transfer—provide a strong admission vocabulary. Every candidate should identify:

1. what evidence or premise the person supplied;
2. what Vesper has already exposed;
3. the new grounded relation, mechanism, distinction, or capability;
4. why the delta matters in the current Place, relationship, or Moment; and
5. what becomes perceptible or possible afterward.

A fluent restatement, emotional paraphrase, personality reading, or personalized
headline fails this test. Current tools-for-thought research similarly argues
that useful generative AI should augment the representations through which
people think while protecting memory, metacognition, creativity, and critical
engagement.

### 6.2 Complete-on-view value can preserve epistemic agency

The strongest Home unit should reveal its proposition, evidence, and important
relation before requiring a tap or response. Optional depth may let the person
inspect sources, challenge the connection, or act. It must not contain the
substance withheld by a curiosity-gap headline.

This is neither a passive feed nor an assignment. It is a finished cognitive
contribution whose interpretation and consequence remain human. Claim-level
uncertainty and provenance are preferable to generic disclaimers or an audit
wall: research on LLM search found that compact uncertainty cues improved
error detection, although they did not eliminate overreliance.

### 6.3 Forward support is stronger than doing the person's judgment

Recent CHI research found that feedback extending a person's reasoning could
integrate better than complete recommendations. Complete answers felt novel and
low-effort, but also shifted outcome attribution to the AI and created
verification work. Related workplace research associates higher confidence in
GenAI with lower self-reported critical-thinking effort; this is correlational,
not proof of cognitive decline, but it clarifies the stewardship burden that
automation can create.

For Vesper:

- perform the research and synthesis;
- expose the missing relation, mechanism, contrast, tradeoff, or consequence;
- do not manufacture the person's final meaning;
- do not require a rationale worksheet to unlock help; and
- let the next act of attention, judgment, or authorship remain theirs.

### 6.4 Personalization chooses a doorway; evidence earns the claim

The desired curiosity structure is:

```text
recognizable premise
  + non-obvious relation or mechanism
  + enough proof to trust it
  + important differences or limits
  + optional aperture or consequence
```

Research on inspiration with LLMs found that unexpectedness alone was
insufficient; useful inspiration also required specificity, feasibility,
reasonableness, and explainability. BioSpark is particularly relevant to
Vesper's cross-domain aspirations: useful transfer came from identifying a
deep mechanism, mapping it across domains, and exposing tradeoffs, rather than
from a surface analogy.

Thus “Sorrento has cliffs like another place” is not enough. A transfer should
show the shared structure, consequential differences, evidence for each side,
the analogy's limitation, and the new perception or action the comparison
makes possible.

### 6.5 Serendipity is experienced enrichment, not profile distance

Recent recommender-system research characterizes serendipity as an unplanned
encounter experienced as fortuitous, refreshing, and enriching. Novelty and
unexpectedness are enabling conditions, not the outcome.

Vesper should therefore not optimize serendipity as randomness, semantic
distance from a taste profile, unusual headlines, or click-through on strange
content. The outcome is that attention, understanding, or later behavior is
enriched.

AiGet supplies a relevant early signal. Its short real-world studies found that
contextual knowledge could increase observation and curiosity about immediate
surroundings; one valuable possibility was later noticing without assistance.
The studies were small, short, and used sensing too invasive for Vesper's
default. The important hypothesis is **capability transfer**:

> **Vesper's highest-value contribution may make Vesper less necessary the
> next time.**

### 6.6 Evolving representations, not frozen profiles or transcript retrieval

Emerging work such as MindTrellis and ThinkFlow suggests that editable
knowledge structures and reusable cognitive workflows can support evolving
human–AI common ground better than either static preferences or rigid
workflows. This aligns with Vesper's Life and Place-relationship direction.

The durable layer should preserve evolving claims, relationships, provenance,
correction, and causal lineage—not only chat history or a fixed taste profile.
This is a semantic requirement, not automatic authorization for a graph
database.

### 6.7 Architecture and evaluation implications

A `ContributionBrief` or equivalent semantic receipt should represent:

```text
premises and evidence
known-to-person estimate
previously exposed claims
new grounded claim
editorial operation
structural relation or mechanism
uncertainty and provenance
capability or perception opened
why now
smallest adequate medium
optional consequence
expiry and invalidation
```

Feedback should repair the contribution without becoming labor. Useful controls
include “I already knew this,” “wrong context,” “not now,” “do not use this
evidence,” and “do not act this way again.” Passive dwell, silence, or dismissal
must not become proof of knowledge, agreement, or preference.

Evaluate sensemaking through blind comparisons among factual report, poetic
interpretation, evidence-led synthesis, structural transfer, prepared
consequence, and silence. Measure novelty-to-person, grounding,
representational gain, five-second comprehension, correction, and delayed
transfer. A particularly important test asks whether the person later notices,
explains, distinguishes, or applies the mechanism in a new situation without
Vesper.

Reject personalized paraphrase, poetic identity claims, unsupported “aha”
connections, generic popular recommendations with personal decoration,
curiosity-gap headlines, randomness labeled serendipity, and artifacts created
before the contribution itself passes admission.

## 7. Topic 5 — Situated interaction with Places and real conditions

### 7.1 Situated and social context are one affordance problem

The strongest unifying question is:

> **What is possible now, for these people, under these conditions, without
> violating the context that makes the possibility meaningful?**

Affordance research treats a possibility as relational between an actor and an
environment, not as an attribute stored on an object. Current mapping research
makes this concrete. People using different mobility devices disagree
meaningfully about the same sidewalk barriers; cycling routes change with
purpose and companions; and shortest-path logic can badly misrepresent walking
experience under heat. “Accessible,” “nearby,” “recommended,” and “worth it”
cannot be universal Place properties.

Vesper's experienced-reachability direction is therefore correct, but it must
be implemented as a candidate-relative, viewer-relative, expiring assessment:

```text
affords(subjects, move/action, place-or-route, moment,
        constraints, social constitution)
  -> assessment + tradeoffs + unknowns + expiry + fallback
```

It should not become a user trait, attachment score, or one ranking number.

### 7.2 Interpret the environment before diagnosing the person

Proactive sensing research suggests that context-aware timing can improve
support. It also makes agency and privacy risks sharper when the classifier
works. Vesper must separate:

- world observation: 91°F, steep grade, 25-minute walk, last train;
- explicit current bound: “not tonight,” “stairs will not work,” “we are
  splitting up”; and
- sensed or inferred state: possible fatigue, difficulty, or attention shift.

“It is 91°F; this shaded route adds seven minutes” is grounded and contestable.
“You seem tired” is an intimate claim, may be wrong, and implies surveillance.
Inferred state should be ephemeral, low-authority, correctable, and excluded
from durable identity unless the person explicitly authors a lasting need.

Every high-salience possibility should state a concrete why-now fact and show
the relevant tradeoff in the medium of action: heat, shade, grade, duration,
rest, access, route, last train, group split, or rejoin. When useful, Vesper
should prepare one alternative that preserves the experiential intent rather
than hiding burden behind an optimum.

### 7.3 Vesper participates in placemaking

Digital representations do not merely retrieve fixed Place meaning; maps,
images, routes, recommendations, and narratives help produce what a Place
becomes to someone. That makes Vesper an editorial participant in placemaking.
It should preserve the distinctions among world fact, what the person noticed,
Vesper's interpretation, and later consequence rather than claiming to have
detected attachment or mastered “meaningful places.”

A Place should retain:

- a stable world face;
- a current affordance face;
- a viewer-relative relationship face; and
- a sparse typed horizon of spatial, causal, operational, historical,
  cultural, biographical, relational, or counterfactual connections.

In-place interpretation should terminate in an observable thing or action and
return the person's eyes to the world. Optional authored reflection can support
remembrance, but travel-storytelling and journaling studies also demonstrate
substantial authoring burden. Home should deliver reconstruction, connection,
and possibility first; reflection becomes an invited deeper mode.

### 7.4 Temporal transitions re-compose; they do not create a mode

A return from a trip changes which evidence is timely. It does not turn the
person into a “post-trip user.” Home can reconstruct transportation, food,
photos, places, or open questions from France and Italy while still leading
with an active life in New York and this weekend's possibilities.

The four horizons—right now, unfolding soon, open future, and carried
forward—should compete in one portfolio. Temporal-boundary evidence changes
composition priority; it must not seal the person inside a retrospective
lifecycle.

### 7.5 Proposed situated-affordance contract

A `SituatedAffordanceAssessment` should include:

```text
subject principals
Place / route / Move / candidate
Moment / Occasion / temporal horizon
world conditions with per-field freshness
current constraints and capabilities with provenance:
  explicit_user | provider_observed | sensed | system_inferred
social configuration, commitments, and hard bounds
feasible alternatives and explicit tradeoffs
authority, audience, and purpose
confidence, unknowns, expiry, and fallback
observable evidence and why-now
```

Compile context per job or candidate family. Continue using ephemeral context
values and content-free manifests. Do not create one ambient universal context
or silently promote a situational inference into profile memory.

### 7.6 Anti-patterns and hypotheses

Reject proximity as proof of relevance, a universal accessibility or meaning
score, person-state diagnoses, persistence of temporary burden as identity,
sealed trip modes, forced post-event reflection, and a route whose richer story
silently overrides safety or physical cost.

Test whether candidate-relative reachability outperforms distance-first
recommendations on actual completion and fit; whether concrete world-framed
adaptation feels less creepy than person-state claims; whether a current-life-
first transition Home reduces emptiness and homework; and whether a cue produces
later unaided noticing rather than only immediate engagement.

## 8. Topic 6 — Plural agency, social authorship, and ambient sociality

### 8.1 The social unit is a temporary constitution, not a group profile

Vesper multiplayer is best understood as independent private relationships
with one intelligence entering a bounded shared world. Personal loops compose
temporarily into an Occasion; they do not merge into a group self.

Common-ground theory sharpens the model. Common ground is the mutually
warranted knowledge sufficient for the present joint purpose, not everything
Vesper knows about every participant. Vesper can privately compile more context
than it reveals, but a shared consequence should expose only the minimum facts,
choice, authority, commitments, and unresolved matters that participants can
mutually rely on.

“Works for everyone” is generally too strong. When a hidden constraint shapes a
choice, Vesper can give a truthful public reason—“This keeps the evening nearby
and leaves an easy exit”—without exposing the private rationale or claiming
shared preference.

### 8.2 Relationship-aware coordination is not preference averaging

A 482-person CHI experiment found that individual personalization widened an
in-group/out-group cooperation gap, while relationship-aware style support
raised out-group cooperation without changing message content. The important
product implication is that optimizing each person's isolated preference can
degrade a joint outcome.

Vesper should preserve hard private bounds, model the relationship and
temporary decision constitution, prepare tradeoffs, and improve the sequence
and language of coordination. It should not average personal scores or optimize
independent recommendation satisfaction.

The minimum social system therefore keeps separate:

- private understanding;
- group-safe reason;
- mutually grounded fact or choice;
- temporary decision and action authority;
- one shared occurrence;
- participant-specific outcomes; and
- optional shared meaning.

### 8.3 Vesper is a process instrument, not another participant

Early 2026 research on small teams found that an AI teammate could become the
most talkative and self-cohesive participant while contributing the least new
information, decreasing human-human responsiveness, belonging, and status.
CSCW work also shows multiple agents can create social pressure and move human
opinions. AI talk changes group topology; brevity alone is not enough.

In group contexts, Vesper should be silent by default and speak only for an
authorized coordination job with material new value. The architecture needs an
AI participation budget:

```text
permitted job
novelty / materiality / urgency threshold
maximum turns and words
human speaking-ratio guard
exit condition
recovery behavior
```

Multiple simulated Vesper voices must never stand in for plural human
perspective or social proof. Prefer a durable proposal, comparison, mandate, or
receipt over taking conversational floor. Success is more human-human
responsiveness and better consequence, not a more central or humanlike AI.

### 8.4 Authorship depends on the speech act

AI mediation changes what a message communicates about its sender. Current
research finds that an AI-assisted label can weaken a message's reputational
diagnosticity, and writers' sense of authenticity depends on the process of
self-construction, not merely approving a polished result.

Vesper should vary assistance by speech act:

| Speech act | Appropriate Vesper role |
| --- | --- |
| Logistics and operational coordination | Substantial composition, grounded facts, provider state, action under mandate |
| Proposal or comparison | Prepare structure and tradeoffs; human or constitution decides |
| Invitation intent, gratitude, apology, repair, “why you,” or meaning | Retrieve context, offer fragments/questions, edit wording; human supplies and confirms semantic core |

A final tap does not establish human authorship if Vesper invented the meaning.
Domain roles should distinguish material source, human meaning author, AI
editor/composer, sender, decision principal, executor, audience, and visible
speaker.

### 8.5 Connection comes from reciprocal human response

Current couple studies show that supported disclosure deepens connection when
it elicits human need support or reciprocal response; an AI-generated summary
of two people is not itself a relational outcome. Vesper should help create the
conditions for human response when explicitly wanted, then recede.

Place or artifact can be a **common third thing** around which contact forms
without forced disclosure. A Rome/Paris juxtaposition becomes socially valuable
when it provides a concrete, permissioned perspective that changes how one
person sees a question, not when it merely announces that a friend traveled.

### 8.6 Ambient sociality should be an aperture, not a feed

Queue Player's small six-week deployment suggests that finite, slow,
source-attributed common objects can sustain anticipation and connection without
an infinite feed. Longitudinal social-media research also observes movement
toward private, selective, smaller-circle sharing and greater audience control.

This supports Status, addressed handoff, recipient-controlled place pull, and
`Open together` when they remain:

- bounded in audience;
- explicit about source, sender, and what Vesper added;
- finite and complete on view;
- free of reply obligation;
- expiring and revocable;
- absent popularity or engagement metrics; and
- controlled by the recipient at opening.

`Keep`, dismiss, silence, and nonresponse are all complete outcomes. Native
Vesper social space should own durable objects ordinary chat cannot—proposal,
vote, mandate, receipt, consequence—while human conversation may stay in
existing channels.

### 8.7 Social custody and grounding contracts

The current runtime's coarse `private/group/system` visibility is insufficient.
Audience and custody need exact principals, Occasion roster revision,
relationship or circle scope, purpose, copy/reshare/inference limits, expiry,
and revocation. A roster change invalidates prior audience assumptions and may
invalidate the temporary constitution.

A consequential shared action also needs a `GroundingReceipt`:

```text
mutually established facts and choice
decision rule and constitution revision
decision principal and executor
affected principals
unresolved or contested items
action state and receipt
```

It must not preserve private rationales. Relationship relevance never grants
messaging, invitation, location, or action authority. Recipient location must
not flow backward to a sender merely because place pull was permitted.

### 8.8 Anti-patterns and hypotheses

Reject a friend activity feed, automatic group memory, merged profile, polling
everyone before Vesper prepares anything, inferred consensus, AI-authored
intimate expression, simulated plural agents, attendance as consent, ambient
location sharing, public fairness debt, and post-event recap as a substitute
for mutual exchange.

Test relationship-aware coordination against isolated preference matching;
silent/bounded facilitation against an active teammate; addressed handoff and
place pull against broadcast feeds; human semantic authorship against full AI
drafting; and plural context-specific memory against a merged group profile on
the second Occasion.

## 9. Topic 7 — Adaptive interfaces with a stable mental model

### 9.1 Research synthesis

Recent generative-interface work supports moving beyond a universal chat log
for structured, information-dense, exploratory, and interactive jobs. Chen and
colleagues' generative-interface system used an intermediate representation of
interaction flows and finite-state component behavior; human evaluators favored
the generated interfaces over conversational baselines for many structured and
interactive tasks. Cao and colleagues similarly generate malleable interfaces
from task-driven data models rather than treating unconstrained generated code
as the durable source of interaction truth.

The transferable finding is not that every response should become a generated
screen. It is that structured intermediate semantics can let the representation
match the job while keeping generation more controllable. Chen and colleagues
explicitly identify straightforward explanations as cases where conversation
can remain competitive and note that their system generated interfaces even
when interaction was unnecessary.

Current personalization work also preserves an old HCI warning: automatic
rearrangement may reduce effort while damaging control, privacy, and learned
spatial expectations. A 2026 CHI interview study found participants preferred
system-initiated visual personalization suggestions they could inspect and
adjust, rather than either raw data alone or fully hidden adaptation. Its
recommended changes were gradual. This is an emerging signal rather than a
general law—the study used twelve participants and hypothetical design probes—
but it reinforces the distinction between *prepared adaptation* and *silent
interface mutation*.

Research on user mental models adds another caution. Better structural
explanation of an AI system does not guarantee better oversight: in one CHI
2026 study, participants primed with a stronger structural mental model rated
an AI writing system as more usable yet allowed more injected grammatical
errors into their final work. Legibility therefore cannot be reduced to an
explanation panel. The interface must make the right verification, correction,
and consequence behavior usable at the moment it matters.

### 9.2 Vesper alignment and correction

The existing Vesper direction is well aligned:

- Home / Chat / Places / Life remain stable roots.
- Canonical objects retain identity and revision across projections.
- The model selects among sanctioned semantic expressions rather than
  producing arbitrary component trees.
- The native client owns geometry, accessibility, interaction, navigation,
  and degraded fallbacks.
- Canonical domains own truth and actions.
- One lead medium expresses the actual cognitive or practical job.

HCI sharpens that direction in five ways.

First, the adaptation input should begin with **object, lifecycle state,
viewer, authority, present job, and environment**. A psychographic user model
should not be the primary resolver input.

Second, adaptation should usually change emphasis, density, medium, supporting
evidence, and available continuation—not stable root placement, canonical
ownership, or familiar consequential controls.

Third, the output grammar should be closed enough to test. Generative breadth
belongs in the semantic contribution and composition, while the interaction
language remains bounded and native.

Fourth, a materially new adaptive behavior needs gradual exposure, a stable
fallback, and correction or reversion. Invisible optimization against clicks or
time on surface would conflict with the product's attention doctrine.

Fifth, accessibility equivalence is an invariant, not a post-generation check.
A map, visual comparison, audio brief, or interactive instrument must have a
complete alternative that preserves meaning, authority, and consequence.

### 9.3 Proposed projection contract

```text
canonical owner + revision
  + lifecycle and truth state
  + viewer, audience, and authority
  + current job and product move
  + attention and environmental constraints
  + admitted semantic contribution
  -> sanctioned lead medium
  -> compact / standard / immersive density
  -> root-native native component family
  -> complete accessible alternative
  -> optional continuation, receipt, or silence
```

The resolver may rank or select. It may not manufacture facts, widen audience,
grant authority, duplicate ownership, or send arbitrary code and layout.

### 9.4 Adaptive-interface anti-patterns

- A home page whose navigation, object locations, or action positions drift
  because the model predicts likely use.
- A universal server-generated component tree with no native accessibility or
  state guarantee.
- Rendering an interface for every AI answer merely because generation is
  available.
- Explaining a wrong or weak adaptation instead of making it easy to dismiss,
  correct, or fall back.
- Treating engagement with a generated unit as evidence that its medium or
  interpretation was correct.
- Personalizing layout from inferred identity traits when situation and current
  job would explain the need more safely.
- Letting the same object appear as several independent cards with different
  truth and actions.

### 9.5 Open questions

1. Which projection decisions can remain deterministic client rules, which
   require model judgment, and which should require explicit user choice?
2. How much visual continuity is needed for a person to recognize one object
   across Home, Chat, Places, Life, and an Occasion?
3. Which adaptive changes are safe to make silently because they are
   reversible presentation choices, and which require preview or explanation?
4. How should explicit format preferences interact with the medium native to
   the current job?
5. What exposure record prevents repetitive composition without converting
   passive viewing into an asserted belief or preference?
6. How should degraded connectivity, missing sensors, large text, VoiceOver,
   motion reduction, and one-handed use constrain the resolver before render?

## 10. Longitudinal evaluation is part of the architecture

### 10.1 Why conventional evaluation is insufficient

Current HCI and AI-safety research increasingly argues that static output
tests miss effects created by repeated interaction: overreliance, social
substitution, anthropomorphic escalation, manipulation, trust drift, and
changing user strategies. AIES 2025 work on interaction harms explicitly calls
for ecologically valid scenarios, human-impact measures, diverse participants,
and evaluation over interaction rather than isolated model output. A 2025
four-week randomized chatbot study likewise found that usage intensity and
individual differences related to psychosocial outcomes in ways not reducible
to one modality or prompt condition.

The same logic applies to positive value. A five-second comprehension test can
show whether a Home projection communicates. It cannot show whether Vesper
becomes better calibrated, whether people learn to rely on it appropriately,
whether remembered evidence improves a later occasion, or whether the product
increases capability instead of dependence.

### 10.2 Seven evaluation layers

| Layer | Core question | Representative measures |
| --- | --- | --- |
| **Truth and policy** | Was the output or action grounded, scoped, permitted, and current? | factual validity, provenance, freshness, audience, authorization, reversibility |
| **Projection** | Did the chosen medium make the value perceptible with minimal burden? | five-second comprehension, information clarity, accessible equivalence, expected owner |
| **Interaction** | Could the person steer, correct, refuse, recover, and predict consequence? | correction success, undo success, authority comprehension, reliance calibration |
| **Encounter** | Did the person's real-world perception, ability, decision, or burden change? | capability delta, coordination relief, route/action success, attention returned to world |
| **Occasion** | Did shared action remain coherent and fair while subjective outcomes stayed plural? | affected-principal understanding, participation burden, hidden privacy leakage, plural satisfaction |
| **Relationship** | Did memory and co-adaptation improve a later situation without increasing harmful dependence? | second-occasion delta, repeated-explanation reduction, trust repair, creepiness, dependency signals |
| **Portfolio** | Does the whole product remain coherent across roots, situations, and people? | root prediction, cross-root identity, cumulative demand, silence quality, subgroup differences |

### 10.3 Counterfactuals

Every meaningful test should compare the candidate against the relevant
alternative, not against an empty screen by default:

- deliberate silence;
- direct canonical state;
- the host/infrastructure product alone;
- a concise conversational or prose answer;
- a static root-native projection;
- a prepared but human-authorized action; and
- the same situation without prior Vesper memory.

This prevents rich generation from winning merely because it contains more
material.

### 10.4 Proposed longitudinal field program

**Phase A — scenario and interaction evaluation.** Use realistic evidence
fixtures to test comprehension, medium choice, novelty, privacy, authority,
correction, and silence before live deployment.

**Phase B — instrumented founder dogfood.** Capture exposure, continuation,
correction, undo, action receipt, and owner transition while collecting short
event-contingent notes. Do not introduce daily reflection homework.

**Phase C — multi-person Occasion studies.** Observe one bounded group arc from
private input through shared consequence and plural Outcome. Interview people
separately so consensus presentation does not erase divergent experience.

**Phase D — multi-occasion longitudinal study.** Follow repeated local and
travel situations long enough to observe expectation formation, memory reuse,
staleness, trust rupture and repair, dependence, and whether a second occasion
is materially better.

**Phase E — portfolio review.** Evaluate the four roots together under ordinary,
urgent, post-return, sparse-evidence, multiplayer, and deliberate-silence
states. The system is the unit, not one card or artifact.

### 10.5 Metrics that must not become goals alone

- session length;
- daily active use;
- notification opens;
- content depth opens;
- number of stored artifacts;
- number of inferred memories;
- percentage of suggestions accepted; and
- self-reported trust without calibration against system performance.

These can diagnose behavior. Optimizing them directly could make Vesper more
attention-seeking, deferential, repetitive, or overconfident.

### 10.6 Relationship-quality measures to develop

The product needs a small Vesper-specific measurement set:

1. **Attention dividend:** useful consequence or understanding relative to the
   attention and input the person supplied.
2. **Representational gain:** whether Vesper added a relationship, mechanism,
   distinction, or reconstruction the person did not already possess.
3. **Capability delta:** whether the person can later notice, understand,
   navigate, decide, coordinate, communicate, or act more effectively.
4. **Calibrated initiative:** whether intervention occurred when useful and
   silence occurred when value did not clear interruption cost.
5. **First-person authority:** whether the person feels able to reject Vesper's
   interpretation without contesting a system-authored identity claim.
6. **Plural-agency integrity:** whether people can distinguish personal input,
   shared occurrence, collective consequence, and separate Outcomes.
7. **Earned continuity:** whether retained evidence creates a material later
   improvement within its purpose and audience boundaries.
8. **Relational outwardness:** whether Vesper increases engagement with people,
   Places, and activity outside the app rather than becoming the destination.

## 11. Cross-topic architecture seams

The research does not support seven new feature systems. It supports a small
set of explicit contracts around the existing product engine.

| Seam | Owns | Must not own |
| --- | --- | --- |
| **Relational behavior policy** | role, first-person rules, withdrawal, vulnerability handling, commercial boundary, repair posture | memory truth, action authority, product voice as fictional biography |
| **Memory claim ledger and lifecycle** | evidence lineage, scoped claims, validity, contradiction, correction, forgetting, dependency invalidation | global identity, audience grants, current relevance |
| **Purpose-limited context compiler** | minimum context for one job, provenance, privacy class, freshness, missingness, authority references | universal ambient profile, permanent inferred situation |
| **Contribution and editorial admission** | semantic delta, evidence, known-to-person estimate, operation, uncertainty, why-now, capability opened | surface layout, interruption, authorization |
| **Situated-affordance assessment** | viewer/candidate-relative feasibility, experienced reachability, conditions, tradeoffs, fallback, expiry | durable Place score, body or personality diagnosis |
| **Initiative and receptivity arbiter** | eligibility against silence, present demand, treatment, interruption cost, competence/identity sensitivity | authority to cross a boundary, truth of the contribution |
| **Mandate and consequence engine** | affected principals, bounded authority, exact diff, execution, reconciliation, receipt, recovery | inferred permission, social meaning, provider truth duplication |
| **Social custody and constitution compiler** | exact audience, roster revision, common ground, decision rule, authorship roles, grounding receipt, AI participation budget | merged group profile, private rationale in shared state |
| **Projection resolver and native client** | sanctioned medium, density, root-native expression, accessibility equivalence, stable controls and fallback | canonical truth, new actions, arbitrary generated code |
| **Interaction and outcome lineage** | exposure, correction, continuation, action and real-world outcome needed for longitudinal evaluation | engagement as meaning, passive viewing as agreement |

### 11.1 One causal spine, three clocks

These seams should compose along one causal spine rather than seven pipelines:

```text
evidence
  → governed claim / current fact
  → purpose-limited context
  → admitted contribution or situated affordance
  → initiative + treatment judgment
  → projection or authorized consequence
  → world / social outcome
  → correction, continuity, or forgetting
```

Three clocks coexist:

1. **World clock:** weather, availability, movement, provider state, and other
   expiring conditions.
2. **Occasion clock:** roster, decision constitution, commitments, action, and
   plural outcome.
3. **Relationship clock:** evidence, memory, trust calibration, correction,
   continuity, and change across occasions.

The architecture should not force them into one lifecycle. A Place fact may
expire in minutes, an Occasion in days, and a memory claim remain useful for
months while still being corrected independently.

### 11.2 Existing implementation foundations

The code already contains useful parts of this target shape:

- the lived-experience context compiler requests declared dependencies, keeps
  values ephemeral, and emits content-free manifests with provenance,
  missingness, authority, privacy, and expiry;
- Occasion projections separate host-authored invitation intent,
  recipient-private orientation, fresh operational facts, the live Occasion,
  and personal/shared afterglow;
- relationship handoffs preserve sender, recipient, world entity, source,
  permissions, expiry, revision, delivery mode, and event lineage; and
- recipient-controlled `open_together` can create a bounded pair Occasion
  without returning to Trip as the social container.

The immediate architectural gaps are not a missing generalized “AI engine.”
They are the claim lifecycle beneath Personal Memory, richer audience/custody
than `private/group/system`, a candidate-relative affordance assessment,
minimum shared grounding, speech-act-sensitive authorship, bounded mandates,
and an explicit contribution/initiative/projection lineage.

### 11.3 Concepts that must remain separate

Do not introduce a universal user profile, relationship score, relevance score,
autonomy level, card type, or engagement objective to bridge the seams. In
particular:

- evidence is not a claim;
- a claim is not identity;
- familiarity is not permission;
- relevance is not receptivity;
- receptivity is not authority;
- private influence is not shared rationale;
- participation is not continuity;
- one occurrence is not one outcome;
- semantic contribution is not presentation;
- presentation is not canonical ownership; and
- software undo is not necessarily social or provider reversibility.

## 12. Consolidated principles and anti-principles

### 12.1 Proposed principles

1. **Contextual intimacy without synthetic intimacy.** Know authorized context
   deeply; do not manufacture reciprocal need or attachment.
2. **Relational value points outward.** Improve the person's relationship with
   people, Places, activity, understanding, and future possibility.
3. **Care is competence, restraint, and repair.** It is not a claimed emotion.
4. **The person retains first-person authority.** Vesper can interpret evidence,
   events, mechanisms, and bounded situations; the person authors what they
   mean about them.
5. **Memory is a governed claim system, not biography.** Purpose, scope,
   audience, validity, correction, and forgetting are first-class.
6. **Evidence authority depends on the question.** Behavior can establish
   occurrence without authoring current preference, intent, or meaning.
7. **Prepare broadly; act narrowly.** Investigation and preparation may be
   expansive within purpose; consequences require exact authority.
8. **Relevance earns eligibility; receptivity earns treatment; authority earns
   action.** Confidence substitutes for none of them.
9. **Remove instrumental effort; preserve constitutive effort.** Do the research
   and coordination, not the person's care, judgment, or commitment.
10. **Value is a semantic or capability delta.** Personalized paraphrase and
    generic relevance are insufficient.
11. **Personalization chooses the doorway; evidence earns the claim.**
12. **Affordance is relational and expiring.** Experienced reachability belongs
    to a person or group, action, Place, Moment, and constitution.
13. **Interpret the environment before diagnosing the person.**
14. **Common ground is minimum mutual warrant, not shared memory.** Private
    context can improve a public consequence without becoming public evidence.
15. **AI should strengthen human-human responsiveness while reducing its own
    social footprint.**
16. **Human authorship means semantic authority, not tap-to-approve.**
17. **Ambient sociality is bounded, attributed, finite, and free of response
    debt.**
18. **One occurrence, plural outcomes, optional shared meaning.**
19. **Stable shell, adaptive projections.** Adapt contribution, medium, density,
    and continuation while preserving roots, owners, controls, and accessibility.
20. **Longitudinal evaluation is architecture.** Repeated use, dependence,
    correction, transfer, and second-occasion value are product behavior, not
    post-launch analytics.

### 12.2 Negative constitution

Vesper is not:

- a friend simulator, replacement relationship, or engagement-maximizing
  conversational destination;
- a global personality profile that turns traces into identity;
- a recommendation score for Places or people;
- a life feed, friend-activity feed, follower graph, or public-performance
  system;
- an AI teammate that dominates group conversation;
- an invisible autonomous actor whose confidence expands permission;
- a universal generated UI whose structure changes beneath the person;
- a reflection assignment after every life event;
- a marketplace or booking clone; or
- a bundle of unrelated travel, social, memory, content, and agent features.

It may connect to mapping, booking, ticketing, messaging, media, and commerce
infrastructure. Its differentiated layer is the governed transformation from
lived evidence to understanding, possibility, workable consequence, and
continuity.

## 13. Research and design sequence

This should not become a “prove one loop first” program. The research confirms
that optimizing one isolated loop could harden exactly the wrong abstractions:
a Home-card schema instead of contributions, a trip profile instead of claims,
or group preferences instead of plural agency. The next phase should freeze a
cross-product constitution and then prototype a representative portfolio.

### Phase 1 — Resolve the constitutional contradictions

1. Decide the relational contract, including whether “companion” remains the
   public category word.
2. Replace the universal behavior-over-claims rule and declare Personal Memory
   a derived projection.
3. Ratify the separations among relevance, receptivity, authority,
   familiarity, confidence, audience, and authorship.
4. Define the negative constitution for synthetic intimacy, identity claims,
   group merging, surveillance, and engagement optimization.

These should become small canonical amendments or decisions, not a wholesale
noun migration.

### Phase 2 — Specify the compositional contracts

Write thin contracts and adversarial fixtures for:

- governed memory claims and forgetting;
- ContributionBrief and editorial admission;
- SituatedAffordanceAssessment;
- initiative/receptivity plus bounded mandate;
- audience/custody, authorship roles, temporary constitution, and
  GroundingReceipt;
- projection resolution and accessibility equivalence; and
- interaction/outcome lineage for evaluation.

Validate that the contracts compose across Home, Chat, Places, Life, an
Occasion, and provider execution. Do not require every contract to be a new
service or database table.

### Phase 3 — Build one comparable experience portfolio

Use the same evidence base to compose complete experiences across at least four
situations:

1. quiet ordinary New York with no urgent event;
2. post-return transition with a current weekend ahead;
3. live hot, mobile, time-constrained Rome;
4. a pair or small-group Occasion with private constraints and one shared
   consequence.

Each portfolio should include all four product moves where they genuinely
apply, deliberate silence, multiple lead media, one consequence, correction,
and carry-forward. Evaluate the four roots together; do not assign one grammar
move to one tab.

Detailed visual exploration should happen in a dedicated design tool. The
research prototype must still preserve native component families, stable root
roles, semantic receipts, and accessible alternatives so that attractive
screens do not evade the architecture questions.

### Phase 4 — Shadow and Wizard-of-Oz evaluation

Before live autonomous action:

- compare candidates against silence and simpler infrastructure alternatives;
- test value-on-view, representational gain, why-now, creepiness, and
  correction;
- shadow initiative and mandate decisions;
- red-team private-to-shared egress, roster change, expiry, stale context,
  irreversible “undo,” and derived-memory deletion; and
- compare silent tool, bounded facilitator, and active AI participant in group
  conditions.

### Phase 5 — Longitudinal field work

Run founder dogfood followed by a six-to-eight-week multi-occasion study across
ordinary life, travel, and social use. Include accessibility variation,
relationship change, sparse evidence, and people for whom AI might displace
human contact. Evaluate the second Occasion, unaided capability, repair,
forgetting, screen-time displacement, and whether Vesper creates outward life
rather than more Vesper use.

## 14. Decisions, hypotheses, and unresolved questions

### 14.1 Findings ready for a decision pass

- Adopt contextual intimacy without synthetic intimacy as the relational
  doctrine.
- Make transitive, outward-facing value the relationship's north-star test.
- Replace behavior-over-claims with question-dependent evidence authority.
- Move canonical personalization from global narrative toward scoped governed
  claims; keep narratives as derived projections.
- Add explicit contribution, situated-affordance, grounding, authorship, and
  AI-participation semantics to the target architecture.
- Evaluate Home/Chat/Places/Life as one adaptive system across multiple
  situations, not as feature silos.

### 14.2 Highest-value falsifiable hypotheses

1. Scoped claims can feel at least as personal as a global profile while
   reducing creepiness and misrepresentation.
2. Quietly legible memory use outperforms both invisible learning and constant
   memory narration.
3. A complete-on-view semantic contribution produces more representational gain
   and less burden than either a factual recap or a reflection prompt.
4. Structural transfer creates more delayed independent capability than a
   personalized surface association.
5. Concrete environment-framed adaptation feels more respectful and performs
   better than person-state diagnosis.
6. Candidate-relative experienced reachability outperforms distance-first or
   generic “best place” recommendation on real completion and fit.
7. Relationship-aware coordination outperforms isolated preference matching
   on cooperation and plural outcome without creating group profiles.
8. Bounded, finite social apertures create connection with less performance
   pressure and reply debt than a friend-activity feed.
9. A job-bounded, low-footprint Vesper increases human-human responsiveness
   more than an active AI teammate.
10. The second Occasion improves through governed continuity without increasing
    session length, dependence, or explanation burden.

### 14.3 Unresolved product and architecture questions

1. What is the public category language if “companion” implies too much
   reciprocity and “travel app” implies too little scope?
2. Which attention traces may be retained by reversible default, and when must
   first retention or cross-context reuse become visible?
3. Which sparse signals may inform receptivity without surveillance?
4. Which situation inferences may persist, for how long, and for which future
   jobs?
5. How much private context may shape a group-safe consequence while its public
   reason remains truthful and useful?
6. What is the minimum comprehensible interface for audience, authorship,
   expiry, copying, and revocation?
7. When does software undo cease to be honest because another person or
   provider already observed the consequence?
8. Which projection choices are deterministic, which use model judgment, and
   which need explicit user preference?
9. How can the system detect dependency or human-contact displacement without
   moralizing use or creating invasive monitoring?
10. Which failures require a hard block or human review rather than
    conversational repair?

### 14.4 Evidence limits

Most 2025–2026 studies here are short-term, single-task, prototype, small-N, or
domain-specific. Stronger controlled evidence supports some relational and
accessibility claims, but none validates Vesper's complete product thesis. The
document therefore supplies constraints, architecture hypotheses, comparative
conditions, and negative oracles—not proof of market demand or long-term
benefit.

## 15. Sources

### Relational contract, memory, privacy, and repair

- Hwang et al., [“How AI Companionship Develops: Evidence from a Longitudinal
  Study,” 2025](https://arxiv.org/abs/2510.10079).
- Guingrich and Graziano, [“A Longitudinal Randomized Control Study of
  Companion Chatbot Use,” AIES
  2025](https://doi.org/10.1609/aies.v8i2.36618).
- Zhang et al., [“Interaction with AI Companions and Psychological
  Well-Being,” *Nature Human Behaviour*,
  2026](https://doi.org/10.1038/s41562-026-02516-2).
- Yuan et al., [“Mental Health Impacts of AI Companions,” CHI
  2026](https://doi.org/10.1145/3772318.3790558).
- Jiang et al., [“RECALLbot: Designing Agentic Memory and Reciprocal
  Disclosure for Human–Chatbot Relationships,” CHI
  2026](https://doi.org/10.1145/3772318.3790714).
- Zhang et al., [“The Dark Side of AI Companionship,” CHI
  2025](https://doi.org/10.1145/3706598.3713429).
- Zhou et al., [“A Systematic Review and Meta-Analysis of Psychological and
  Behavioural Responses in Human-Agent vs. Human-Human Interactions,”
  *Communications Psychology*,
  2026](https://doi.org/10.1038/s44271-026-00466-z).
- Jones et al., [“Users' Expectations and Practices with Agent Memory,” CHI EA
  2025](https://doi.org/10.1145/3706599.3720158).
- Chen et al., [“Relational Gains, Privacy Strains: Exploring Users'
  Perceptions and Experiences with ChatGPT's Memory Feature,” CHI
  2026](https://doi.org/10.1145/3772318.3791635).
- Nissenbaum, [“Privacy as Contextual Integrity,” *Washington Law Review*,
  2004](https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/).
- Monteiro et al., [“When Are LLM Inferences Acceptable?”
  2026](https://arxiv.org/abs/2605.10013).
- Wu et al., [“Negotiating Shared Agency Between Humans & AI in Recommender
  System,” CHI EA 2025](https://doi.org/10.1145/3706599.3719900).
- Ashktorab et al., [“Who's Sorry Now: User Preferences Among Rote, Empathic,
  and Explanatory Apologies from LLM Chatbots,” *ACM TOCHI*,
  2026](https://doi.org/10.1145/3793679).
- Konopka and Wiesche, [“Can ‘AI’ Repair Trust? Comparing Human-Like and
  System-Like Repair Strategies,” ICIS
  2025](https://aisel.aisnet.org/icis2025/user_behav/user_behav/4/).
- Hall et al., [“LL.me: Supporting Identity Work through Human-AI Alignment,”
  CHI 2026](https://doi.org/10.1145/3772318.3790890).

### Initiative, sensemaking, and epistemic agency

- Khurana et al., [“Do It For Me vs. Do It With Me: How AI Collaboration Modes
  Shape User Experience,” CHI
  2025](https://doi.org/10.1145/3706598.3713431).
- Reicherts et al., [“AI, Help Me Think—but for Myself,” CHI
  2025](https://doi.org/10.1145/3706598.3713295).
- Chen et al., [research on proactive programming assistance, CHI
  2025](https://doi.org/10.1145/3706598.3714002).
- Liu et al., [“Sensing What Surveys Miss: Understanding and Personalizing
  Proactive LLM Support by User Modeling,” CHI
  2026](https://doi.org/10.1145/3772318.3791191).
- Diebel et al., [research on competence threat from proactive AI assistance,
  2025](https://doi.org/10.1007/s12599-024-00918-y).
- Kuilman et al., [research on meaningful human control in AI systems,
  2025](https://doi.org/10.1007/s13347-025-00976-4).
- He et al., [research on plan-then-execute agent interaction, CHI
  2025](https://doi.org/10.1145/3706598.3713218).
- Spatharioti et al., [research on user behavior and uncertainty in LLM search,
  CHI 2025](https://doi.org/10.1145/3706598.3714082).
- Lee et al., [“The Impact of Generative AI on Critical Thinking,” CHI
  2025](https://doi.org/10.1145/3706598.3713778).
- Tankelevitch et al., [“The Impact of Generative AI on Human Cognition: A
  Tools-for-Thought Perspective,” 2025](https://arxiv.org/abs/2508.21036).
- Su et al., [“Seeking Inspiration through Human-LLM Interaction,” CHI
  2025](https://doi.org/10.1145/3706598.3713259).
- Kang et al., [“BioSpark,” CHI
  2025](https://doi.org/10.1145/3706598.3714053).
- Binst et al., [research on experienced serendipity in recommender systems,
  UMAP 2025](https://doi.org/10.1145/3699682.3728325).
- Cai et al., [“AiGet: Transforming Everyday Moments into Hidden Knowledge
  Discovery with AI Glasses,” CHI
  2025](https://doi.org/10.1145/3706598.3713953).
- Li et al., [“MindTrellis,” DIS
  2026](https://doi.org/10.1145/3800645.3813045).
- Chen et al., [“ThinkFlow,” CHI
  2026](https://doi.org/10.1145/3772318.3791669).

### Situated and embodied interaction

- Gaver, [“Technology Affordances,” CHI
  1991](https://doi.org/10.1145/108844.108856).
- Li et al., [“Accessibility for Whom? Perceptions of Sidewalk Barriers Across
  Disability Groups and Implications for Designing Personalized Maps,” CHI
  2025](https://doi.org/10.1145/3706598.3713421).
- Hwang et al., [“BikeButler: A Personalized, Context-sensitive Bike Routing
  Tool,” CHI 2026](https://doi.org/10.1145/3772318.3791292).
- Ma et al., [“Active Route Choice to Minimize Pedestrian Thermal Discomfort in
  a High-Density Subtropical City,” *Sustainable Cities and Society*,
  2025](https://doi.org/10.1016/j.scs.2025.106697).
- Kotkov et al., [“Paths and Recreation: Inclusive Recommendation of Physical
  Activities in Your Neighbourhood,” CHIIR
  2025](https://doi.org/10.1145/3698204.3716473).
- Suzuki and Dillon, [“The Emergence of the Placial-Technical: Digital
  Placemaking as Information Practice,” 2025](https://doi.org/10.5206/cjils-rcsib.v48i2.23115).
- Yin and Xiao, [“TravelGalleria: Supporting Remembrance and Reflection of
  Travel Experiences through Digital Storytelling in Virtual Reality,” CHI
  2025](https://doi.org/10.1145/3706598.3713398).
- Hannan et al., [“LTJ: A Capability-based Digital Journaling Tool to Support
  Well-being of Newcomers in Life Transition,” CSCW
  2025](https://doi.org/10.1145/3757491).

### Plural agency, common ground, and social authorship

- Clark and Brennan, [“Grounding in Communication,”
  1991](https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf).
- Erickson and Kellogg, [“Social Translucence: An Approach to Designing Systems
  that Support Social Processes,” *ACM TOCHI*,
  2000](https://doi.org/10.1145/344949.345004).
- Beaudouin-Lafon, Bødker, and Mackay, [“Generative Theories of Interaction,”
  *ACM TOCHI*, 2021](https://doi.org/10.1145/3468505).
- Claggett, Kraut, and Shirado, [“Relational AI: Facilitating Intergroup
  Cooperation with Socially Aware Conversational Support,” CHI
  2025](https://doi.org/10.1145/3706598.3713757).
- Nixon et al., [“The Social Cost of an AI Teammate,”
  2026](https://arxiv.org/abs/2607.27179).
- Song et al., [“Multi-Agents are Social Groups: Investigating Social Influence
  of Multiple Agents in Human-Agent Interactions,” CSCW
  2025](https://doi.org/10.1145/3757633).
- Jiang et al., [“Scaffolded Vulnerability,” CHI
  2026](https://doi.org/10.1145/3772318.3791370).
- Jiang et al., [“Remini: Leveraging Chatbot-Mediated Mutual Reminiscence,” CSCW
  2025](https://doi.org/10.1145/3757650).
- Pinder et al., [“Queue Player: Investigating Distributed Co-Listening
  Experiences for Social Connection,” CHI
  2025](https://doi.org/10.1145/3706598.3714293).
- Khadpe et al., [“Explaining the Reputational Risks of AI-Mediated
  Communication,” AIES 2025](https://doi.org/10.1609/aies.v8i2.36641).
- Hwang et al., [“‘It was 80% me, 20% AI’: Seeking Authenticity in Co-Writing
  with Large Language Models,” CSCW 2025](https://arxiv.org/abs/2411.13032).
- Tran et al., [“Understanding Privacy Norms Around LLM-Based Chatbots: A
  Contextual Integrity Perspective,” AIES
  2025](https://doi.org/10.1609/aies.v8i3.36735).
- Jungselius and Weilenmann, [“Tracing Change in Social Media Use: A Qualitative
  Longitudinal Study,” CHI
  2025](https://doi.org/10.1145/3706598.3713813).

### Current HCI and adjacent research used in Topic 7 and evaluation

- Cao, Jiang, and Xia, [“Generative and Malleable User Interfaces with
  Generative and Evolving Task-Driven Data Model,” CHI
  2025](https://doi.org/10.1145/3706598.3713285).
- Chen et al., [“Generative Interfaces for Language Models,”
  2025](https://arxiv.org/abs/2508.19227).
- Lam et al., [“Just-In-Time Objectives: A General Approach for Specialized AI
  Interactions,” CHI 2026](https://arxiv.org/abs/2510.14591).
- Alves et al., [“Exploring the Role of Interaction Data to Empower End-User
  Decision-Making in UI Personalization,” CHI
  2026](https://doi.org/10.1145/3772318.3791022).
- Rismani et al., [“From Use to Oversight: How Mental Models Influence User
  Behavior and Output in AI Writing Assistants,” CHI
  2026](https://arxiv.org/abs/2604.05166).
- Kaur et al., [“Report on the First Workshop on Human-Centered Proactive and
  Personalized Agents for Interactive Information Access,” CHIIR
  2026](https://arxiv.org/abs/2608.18638).
- Ibrahim et al., [“Towards Interactive Evaluations for Interaction Harms in
  Human-AI Systems,” AIES
  2025](https://doi.org/10.1609/aies.v8i2.36631).
- Fang et al., [“How AI and Human Behaviors Shape Psychosocial Effects of
  Chatbot Use: A Longitudinal Randomized Controlled Study,”
  2025](https://arxiv.org/abs/2503.17473).
- Fang et al., [“AI-Wrapped: Participatory, Privacy-Preserving Measurement of
  Longitudinal LLM Use In-the-Wild,” CHI
  2026](https://arxiv.org/abs/2602.18415).

## Exit

Before expiry, review the supported constraints and choose among:

- promote durable relational principles into Product Thesis, What We Believe,
  Product Architecture Principles, or the interaction constitution;
- record consequential architecture choices as decisions;
- assign memory, initiative, social, projection, and evaluation details to
  their system or surface contracts; and
- archive this memo as the dated research basis rather than leaving it as a
  competing product authority.
