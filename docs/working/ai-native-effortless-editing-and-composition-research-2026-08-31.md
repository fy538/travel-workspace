---
doc_type: working
status: active
owner: founder / product / design / architecture / research
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Investigates how Vesper can let people create, reshape, coordinate, and act through dynamic Plans, Occasions, and compositions without forms, prompt engineering, permission dashboards, or chat-only interaction.
source_of_truth_for: []
depends_on:
  - docs/working/vesper-experience-constitution-and-interaction-grammar-2026-08-22.md
  - docs/systems/contribution-and-consequence.md
  - docs/systems/artifact-expression-and-composition.md
  - docs/systems/four-root-loop-object-surface.md
  - docs/working/plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md
---

# AI-Native, Effortless Editing and Composition — Research Round 4

## Question and status

Vesper increasingly treats an itinerary, a night out, a day, a live recovery,
or a post-trip reconstruction as a bounded dynamic composition over canonical
truth—not as a rigid form or itinerary-block worksheet. If that direction is
correct, how should a person create and change these things?

The desired experience is unusually demanding:

- a person should be able to speak naturally instead of filling many fields;
- direct touch should remain faster than language for obvious local changes;
- Vesper should absorb structure without silently absorbing authority;
- the same object should remain coherent across Home, Chat, Places, Life, and
  its own owner surface;
- social coordination should be easier than maintaining a shared document;
- correction should be local, legible, and cheap; and
- the experience should feel like shaping life with a capable intelligence,
  not supervising an agent or completing administrative work.

This memo studies the interaction model before authorizing UI, schema, or
service changes. It deliberately optimizes for **lightweight and effortless**.
It is not an argument for more control surfaces.

## Executive verdict

The research supports a clear interaction architecture:

> **The primary editing surface is the visible thing itself. Touch supplies
> context, language supplies nuance, Vesper absorbs translation and structure,
> one typed command changes the canonical owner, and the result appears where
> it happened with proportional readback and repair.**

This is neither chat-only nor form-first. It is a **shared-object, mixed-
initiative model**:

```text
visible object + current selection + brief human expression
  -> inferred semantic intent
  -> smallest justified typed command
  -> apply or preview at the actual authority boundary
  -> localized visible consequence
  -> compact readback + precise Undo/Correct
```

The most important correction is conceptual:

> **Effortless does not mean zero friction. It means the system removes work
> that exists only to satisfy the system, while preserving the brief moments
> of human judgment that constitute authorship, consent, social obligation, or
> real-world commitment.**

Accordingly, Vesper should eliminate:

- schema selection;
- field-by-field entry;
- manual classification and filing;
- restating visible context in prompts;
- repeated confirmations for reversible private changes;
- permission configuration before an actual boundary exists;
- whole-object regeneration to correct one local mistake; and
- hunting through chat history to determine current state.

It should preserve or introduce brief friction only when a change:

- affects another principal;
- changes audience;
- contacts a provider;
- spends money;
- publishes or discloses protected material;
- creates a socially meaningful expectation; or
- is difficult to reverse accurately.

The product implication is not “build an AI editor.” It is:

> **Make every useful Vesper object naturally addressable by both touch and
> language, while keeping structure, policy, and command routing behind the
> experience.**

## 1. What “effortless” should mean

### 1.1 Optimize total collaboration cost, not tap count

A one-command agent can still feel laborious if the person must write a precise
prompt, wait, inspect a large result, discover what changed, repair collateral
damage, and reconstruct state from a transcript.

For Vesper, total interaction cost is better understood as:

```text
expression cost
+ orientation cost
+ representational cost
+ verification cost
+ coordination cost
+ correction cost
+ consequence risk
```

An interaction is lightweight when the sum falls—not merely when a form has
been replaced by a text box.

### 1.2 Friction taxonomy

| Friction | Meaning | Vesper posture |
| --- | --- | --- |
| **Mechanical** | taps, typing, copying, navigating, repetitive entry | Eliminate aggressively |
| **Representational** | choosing schemas, object types, fields, ranks, permissions, or workflows | Let Vesper absorb it |
| **Orientation** | figuring out what the app can do or where current truth lives | Reduce through visible objects and contextual actions |
| **Verification** | checking whether AI understood and changed the right thing | Compress into local deltas, provenance, and state readback |
| **Commitment** | deciding whether to spend, book, invite, promise, publish, or cross a weakly reversible boundary | Preserve at the exact boundary |
| **Social** | understanding who is affected, what they can see, and whose decision it is | Preserve, but express through the shared object rather than a permission dashboard |
| **Reflective** | thinking because the decision or authorship genuinely benefits from thought | Preserve only when it serves the person, never to improve Vesper's dossier |

This distinction matters because removing the last three kinds indiscriminately
does not create ease. It creates uncertainty, accidental commitments, and loss
of ownership.

### 1.3 The old HCI warning is directly applicable

Shipman and Marshall observed that people often reject systems when the system
requires more explicit structure than their work naturally demands. Their
answer was **incremental and system-assisted formalization**: start informal,
add structure only when it becomes useful, and convert creation work into the
lighter work of accepting or correcting suggestions. The related Hyper-Object
Substrate explicitly argues that formalization should be demand-driven so that
people receive benefit before paying the structure cost.
([Formality Considered Harmful](https://people.engr.tamu.edu/shipman/viki/papers/tochi/tochi.html),
[Incremental Formalization](https://people.engr.tamu.edu/shipman/hos/hos-short.html))

For Vesper:

```text
“maybe jazz on Saturday”
  != complete a PlanItem form

photo + “this was the pasta”
  != classify Place / dish / occasion / memory / audience

“move dinner later” while looking at Saturday
  != restate Plan, day, item, participants, and time in Chat
```

The system may create internal semantic structure, but the person should not
maintain that structure unless a genuine decision requires it.

## 2. Why neither chat-only nor form-first is enough

### 2.1 Chat-only removes fields but creates prompt labor

Prompt-based interaction introduces a “gulf of envisioning”: people may not
know what the task should be, how to instruct the model, or what output to
expect. This is a capability and interaction problem, not a user education
failure. ([Bridging the Gulf of Envisioning](https://doi.org/10.1145/3613904.3642754))

Linear chat also performs poorly for evolving objects:

- the person has to name or describe what is already visible;
- current truth is buried among proposals and obsolete versions;
- branching alternatives collide in one transcript;
- local corrections often trigger broad regeneration;
- actions are difficult to discover without knowing what to ask; and
- a compact plan becomes verbose conversation about a plan.

Data Formulator 2 found text-only, one-turn description unrealistic for
iterative authoring. Its blended UI plus natural-language model let people
specify precise visible structure through UI while delegating transformation
to AI; iteration history prevented restarting from scratch.
([paper](https://arxiv.org/abs/2408.16119))

### 2.2 Form-first makes the user become the database adapter

Forms are valuable when every field is required for an imminent consequence.
They are inappropriate as the default representation of possibility,
attention, or an evolving social plan.

Form-first design prematurely asks:

- What object is this?
- Which day does it belong to?
- Is it tentative or confirmed?
- Who can see it?
- What exact time?
- Which category?
- What is its rank?
- Should this be a Plan, Occasion, trip, artifact, or task?

Those questions are often not yet meaningful to the person. Requiring answers
converts ordinary life into clerical maintenance.

### 2.3 Fully generated UI creates a different burden

Research systems such as Jelly show real promise in mapping both natural
language and direct manipulation into an evolving task model.
([Jelly](https://doi.org/10.1145/3706598.3713285)) Generative-interface work
also finds substantial preference for structured, interactive output over long
conversational responses in information-dense and exploratory tasks.
([Generative Interfaces for Language Models](https://arxiv.org/abs/2508.19227))

But “the model can generate an interface” does not imply that Vesper should
generate arbitrary mobile UI. Unbounded UI generation risks:

- spatial instability between visits;
- lost learned behavior;
- inaccessible or unsafe controls;
- ambiguous action authority;
- visually plausible but semantically false state;
- hard-to-reproduce bugs; and
- a new verification burden: understanding what interface the agent invented.

The correct adoption is **bounded malleability**: the model chooses semantic
intent, evidence, density, and a native expression family; the client retains
stable interaction grammar, geometry, accessibility, and action behavior.

## 3. The researched interaction model

### 3.1 One shared object, two complementary languages

Horvitz's mixed-initiative principles argue for an intentional coupling of
automation and direct manipulation, not a choice between them. The system
should provide genuine value-added automation, model uncertainty and cost,
use dialogue only for key uncertainties, make invocation and termination easy,
do less when uncertainty is high, and support efficient refinement.
([Principles of Mixed-Initiative User Interfaces](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf))

For Vesper, the two languages have different comparative advantages:

| Modality | Best at | Example |
| --- | --- | --- |
| **Touch / selection** | reference, scope, ordering, binary choice, spatial and temporal placement | tap Saturday, drag a loose possibility later, remove this stop |
| **Language / voice** | motive, ambiguity, exception, preference, tradeoff, relationship, desired effect | “make this less rushed,” “something Maya would actually enjoy,” “keep the museum but not first thing” |
| **Vesper inference** | translation, decomposition, structure, dependency evaluation, candidate generation | infer affected entries and find a lower-rush arrangement |
| **Native composition** | current truth, comparison, consequence, action, recovery | show the proposed localized change and its effect on travel time |

This enables under-specified but grounded commands:

```text
[person selects Saturday evening]
“Make this feel less packed.”

[person selects two Place rows]
“Which one works better after the show?”

[person opens an Occasion]
“Invite Maya and let her add ideas.”
```

The visible selection carries the context that otherwise becomes prompt
engineering.

### 3.2 Editing should happen on the owner, not in a detached change studio

The default choreography should be:

1. The person is looking at the current object or projection.
2. A tap, hold, drag, or Ask Vesper affordance establishes a referent.
3. The person expresses only the missing intent.
4. Vesper prepares the smallest semantically complete change.
5. The native owner view shows the delta in place.
6. The command applies or pauses according to consequence.
7. A compact receipt exposes Undo, Correct, or the affected owner.

A focused sheet is justified only when the material decision cannot be shown
legibly in place—for example, choosing between two consequential alternatives
or reviewing who will receive an invitation. It should not become the generic
home for every edit.

### 3.3 Chat is a universal address bar, not the only editor

Chat remains the lowest-friction place to begin when there is no visible
object, when the request spans objects, or when thought itself is
conversational. It should also receive origin context when opened from another
surface.

```text
origin root: Places
origin object: Roscioli
selection: Friday dinner possibility
user: “Could this work after the walk?”
```

Chat can return an answer, comparison, proposal, instrument, or action receipt.
If a command changes a Plan or Occasion, that owner changes directly; Chat does
not become a parallel copy of the plan. A return envelope takes the person back
to the exact object and selection.

## 4. Research findings across the twelve open topics

### 4.1 AI editing grammar

The grammar should describe **human intent**, not storage operations:

```text
Add · Remove · Move · Replace · Loosen · Tighten · Compare · Shape
Invite · Contribute · Decide · Adapt · Confirm · Correct · Undo
```

These verbs compile into typed owner commands. The user never needs to know
whether the system created a PlanItem, linked a Place, altered a projection
constraint, or prepared a Commitment.

The smallest useful command envelope is:

```text
actor + selected context + semantic intent + inferred scope
+ authority mode + expected owner revision + idempotency key
```

Do not expose this envelope as a form. It is an internal guarantee that touch
and Chat resolve through the same behavior.

### 4.2 Readback and semantic diffs

AI editing requires a semantic diff, but not a developer diff viewer.

For a private reversible edit, the readback can be one line:

> Dinner moved to 8:30. The walk still fits before it. **Undo**

For a consequential shared proposal:

> This will ask Maya and Luis to choose between 7:30 at Dhamaka and 8:00 at
> Semma. Nothing is reserved. **Send**

The minimum diff answers:

1. What changed?
2. What meaningful consequence changed with it?
3. Who can now see or act on it?
4. Has it applied, or is it still a proposal?
5. How do I reverse or correct it?

Prefer local highlighting and motion over a prose changelog. Apple explicitly
recommends predictable undo labels and highlighting the result so people know
what the reversal affected.
([Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo))

### 4.3 Stable, malleable compositions

The visual object needs stable identity even when its best projection changes.
The rule should be:

> **Stable landmarks, variable emphasis.**

Stable:

- root and owner identity;
- core interaction zones;
- source, audience, and state semantics;
- action placement conventions;
- accessibility behavior;
- return path; and
- current shared operational facts.

Malleable:

- ordering and emphasis;
- lead medium and density;
- which supporting evidence is visible;
- comparison or sequence treatment;
- personal explanation; and
- which contextually valid continuation is offered.

Ink & Switch's Embark is especially relevant because it explores travel plans
as dynamic documents that begin as informal notes, gradually gain mentions,
maps, calendars, routes, and weather, and remain useful at every degree of
formality. It also separates underlying data from the interface.
([Embark](https://www.inkandswitch.com/embark/))

Vesper should adopt the gradual-enrichment principle without adopting a text
outline as its universal UI or requiring users to author formulas and views.

### 4.4 Chat–composition choreography

The choreography should preserve deictic reference and state:

```text
object -> select -> ask/change -> local result -> owner readback -> return
```

Avoid:

```text
object -> generic Chat -> re-explain object -> long proposal
       -> hidden write -> search for changed object
```

Every object-native Chat entry should carry:

- owner ID and revision;
- selected semantic element;
- root and projection context;
- current audience scope;
- available bounded capabilities; and
- a return destination.

The model can then understand “this,” “later,” “with them,” and “make it
quieter” without the user reconstructing context.

### 4.5 Multimodal evidence without intake homework

NoTeeline demonstrates a powerful division of labor: people jot brief
“micronotes,” while the system uses surrounding source context to expand them.
In a 12-person within-subjects study, participants wrote 47% less text and
completed notes 43.9% faster than the manual baseline while retaining their
own attention as the seed.
([NoTeeline](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2025/noteeline.pdf))

The Vesper analogue is:

```text
human contribution: direction of attention
Vesper contribution: context, structure, connection, practical implication
```

Examples:

- a ticket supplies carrier, route, date, and travel dependency;
- a photo plus “the texture was different” supplies the user's observation,
  while Vesper may identify the dish and explain a supported mechanism;
- a voice fragment during a walk can retain the user's exact noticing while
  ambient Place and time resolve referents;
- “Maya would love this” can prepare a private relational opening but does not
  send or publish anything.

The system must not expand a micronote into invented preference, occurrence,
meaning, or identity. Expansion may add sourced context; it may not complete
the person's interior life.

### 4.6 Creation without premature commitment

The system needs an invisible **draft plane**, not a visible hierarchy of draft
objects.

```text
expression
  -> ephemeral candidate
  -> optional private possibility
  -> Plan-owned item when refinding or shaping requires it
  -> Commitment only at a real consequence boundary
```

“Maybe jazz Saturday” can immediately produce useful Place options and fit
information without first becoming durable. If the person says “keep the first
one for Saturday,” the smallest private Plan item may be created. If tickets
are purchased, a separate Commitment owns that truth.

Preparation must not masquerade as persistence, and persistence must not
masquerade as commitment.

### 4.7 Cross-root edit continuity

The four roots should not expose four editing systems. They are projections
over one governed object world:

| Root | Editing role |
| --- | --- |
| **Home** | Shape or act on the current consequence without maintaining the archive |
| **Chat** | Express cross-object, nuanced, or new intent; receive compact results and receipts |
| **Places** | Change spatial scope, alternatives, route, or Place-relative possibility |
| **Life** | Correct durable evidence, audience, occurrence, continuity, and retained expression |

An edit begun in one root updates the owner once and invalidates every affected
projection. The same identity and revision reappear elsewhere. No “send to
Chat,” “save back to itinerary,” or duplicated artifact state should be
required.

### 4.8 Lightweight multiplayer editing

Classic workspace-awareness research finds that visible action on shared
artifacts creates common ground and lets people communicate with less explicit
coordination. Feedthrough—seeing the object change—often carries more useful
awareness than a separate activity explanation.
([Gutwin and Greenberg](https://collablab.northwestern.edu/CollabolabDistro/nucmc/GutwinGreenberg_FrameworkWorkspaceAwareness.pdf))

For Vesper, multiplayer ease should come from the Occasion or shared object:

- attributed contributions appear where they matter;
- shared operational truth is identical at one revision;
- small changes visibly show who made them;
- private constraints can shape safe options without being disclosed;
- proposals show affected people and exact consequence;
- responses are independent, not one merged “group preference”; and
- participants do not maintain custom per-item permissions.

Avoid making Vesper an equal voting group member. A 2026 study of LLM-facilitated
group deliberation found that participants preferred facilitation even when it
did not improve consensus or participation equality, while facilitators still
steered some outcomes. Perceived inclusion and actual influence can diverge.
([Google DeepMind study](https://deepmind.google/research/publications/224297/))

Vesper should prepare, juxtapose, reveal constraints safely, and help the group
move. Human principals decide.

### 4.9 Undo, history, and repair

Undo must be semantic and causal:

- undo the dinner move, not “the last AI turn”;
- reverse the private Keep without deleting the original Source if separately
  retained;
- withdraw an invitation without erasing the Occasion;
- correct “visited” while preserving a purchased ticket;
- revert an AI batch as one logical unit or inspect its constituent changes;
- show which downstream projections will change.

Microsoft's HAX guidance recommends rich edits, undo of automated actions, and
batch correction when AI is partially wrong.
([Support efficient correction](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-correction/))

Repair should target the smallest false relation or unintended consequence.
Whole-composition regeneration is a fallback, not the basic correction model.

### 4.10 Capability discoverability

A blank composer does not communicate a broad product. A comprehensive command
menu communicates machinery rather than possibility.

PAIR recommends staged mental-model formation, describing benefits rather than
technology, introducing capabilities as they become relevant, and preserving a
non-AI way forward when the AI fails.
([Mental Models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/))

Vesper's capabilities should be learned through **contextual invitations on
real objects**:

- on a Place: Compare · Fit into Saturday · Ask Vesper;
- on a loose possibility: Shape this · Find an alternative · Let go;
- on an Occasion: Invite · Add something · Help us decide;
- on an imported ticket: See what this changes · Add to journey;
- on a disruption: Adapt this · Show fallback;
- after a correction: “I’ll use that only for this trip” with a direct scope
  affordance when true.

These are not permanent button rows. One or two actions appear when context
makes their value legible.

### 4.11 Earned autonomy by action family

Autonomy should not be one global slider. Trust in summarization does not imply
trust in invitations, bookings, audience changes, memory retention, or
rescheduling.

Vesper should learn collaboration posture by bounded action family and context:

```text
private organization
private Plan shaping
shared proposal preparation
social sending
provider contact
spend / booking
public contribution
memory retention and inference
```

PAIR recommends progressively increasing automation only under user guidance
and when trust is high or error risk is low.
([Explainability and Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/))

The visible product can remain simple. This does not require an autonomy
settings dashboard. Repeated, specific commands can grant a bounded mandate;
the receipt states what will happen next and offers a way to end it.

### 4.12 Emotional feel of co-creation

The target feeling is not “I operated an AI” or “the AI took over.” It is:

- **I was understood without writing a specification.**
- **The thing got better while remaining recognizably mine or ours.**
- **I can see what changed without auditing the system.**
- **The app did the administrative work and left the actual choice to us.**
- **I can interrupt, correct, or leave without losing the thread.**

Recent co-creation research is useful here. A large 2026 experiment found that
model-led rewriting improved idea quality but reduced diversity and perceived
ownership; reflective human-led modes improved quality while preserving both.
([Partnering With Generative AI](https://mcml.ai/publications/msf26/)) Other
research finds that shortcuts can reduce conceptual exploration even while
making generation easier.
([Prompt-mediated creativity](https://arxiv.org/abs/2312.00233))

Vesper should therefore automate **translation, preparation, synthesis,
coordination, and repair** more aggressively than it automates **meaning,
expression, commitment, and group choice**.

## 5. Clarification and confirmation doctrine

### 5.1 Ask according to expected regret, not uncertainty alone

A 2026 study models clarification as a tradeoff between uncertainty and the
cost of acting incorrectly: people seek clarification in proportion to the
loss they could suffer by acting now.
([Act or Clarify?](https://repositories.cdlib.org/uc/item/5kb446j5)) A separate
study found clarification can increase trust while also increasing cognitive
effort; its value rises with uncertainty and irreversibility.
([Ask Before or After?](https://doi.org/10.1145/3803784.3816856))

This supports the existing T0–T2 contract:

| Situation | Default behavior |
| --- | --- |
| No durable consequence | Answer or prepare; do not ask |
| Clear, private, reversible change | Apply the smallest change; show local readback + Undo |
| Unclear detail whose alternatives are similarly safe | Choose the narrower interpretation or remain provisional |
| Ambiguity changes truth, owner, audience, affected person, spend, provider action, or reversal cost | Ask one specific question or show one exact preview |

Never ask “What would you like to do?” if the system can offer a valuable
bounded result. Never ask a generic clarification when two concrete options
would resolve the material difference.

### 5.2 Confirmation belongs at the consequence, not at intent entry

Bad:

```text
user: “Move dinner later.”
system: “Would you like me to move dinner later?”
```

Good, when private and reversible:

```text
Dinner is now at 8:30. The walk still fits. Undo
```

Good, when it affects other people:

```text
Moving dinner to 8:30 changes Maya and Luis's shared plan.
Send the change?  [Not yet] [Send]
```

Good, when external action follows:

```text
8:30 is available. This will release the 7:00 table and book 8:30 for four.
[Keep 7:00] [Change reservation]
```

The person should encounter at most one material boundary per coherent action.

## 6. Architecture implications

### 6.1 Preserve the existing owner model

The research strengthens, rather than replaces, the current architecture:

- canonical domains own truth;
- PlanItem remains lightweight and Plan-owned;
- Commitment owns consequential external truth;
- Occasion owns bounded participation and shared consequence;
- Composition is an expression, not authority;
- Chat and touch use one typed command path;
- root-native clients render bounded semantic families; and
- readback comes from the owner after the command.

### 6.2 Add an interaction context envelope, not a UI schema

The missing seam is a small runtime context that lets the same command grammar
work from any surface:

```text
InteractionContextV1
  origin_root
  origin_projection_id
  owner_ref + expected_revision
  semantic_selection[]
  viewer + audience_scope
  available_capability_refs[]
  return_envelope
```

This is not persisted as user content and not shown as a configuration form.
It makes “this,” “there,” “later,” and “with them” resolvable.

### 6.3 Commands should return a displayable semantic delta

```text
CommandResultV1
  status: prepared | applied | partial | failed
  owner_revision
  changed_relations[]
  meaningful_effects[]
  affected_principals[]
  audience_delta
  recovery_capability
  return_envelope
```

The client renders this through the changed object and a compact receipt. It
does not need an AI-authored change screen.

### 6.4 Keep the draft plane cheap

Ephemeral preparation should not require a durable generic draft service at
the outset. A request-scoped or session-scoped candidate with expiry is enough
until fixtures prove cross-session refinding, collaboration, or audit needs.

### 6.5 Do not generalize authorization UI

The five-axis authority model remains internal. The person should see the exact
human consequence:

- “Only you”;
- “Maya and Luis will see this”;
- “This asks everyone, but does not change the plan”;
- “This contacts the restaurant”;
- “This will be public.”

Do not expose axes, policy names, role matrices, or per-item ACL controls unless
an actual edge case repeatedly requires them.

## 7. Comparative fixture research before production UI

The first expert comparative walkthrough is now recorded in
`docs/working/form-chat-hybrid-comparative-interaction-research-2026-08-31.md`.
It supports the hybrid shared-object hypothesis while identifying moments where
conversation, direct manipulation, authored output, or conventional structured
review should win. It is not participant evidence; the next prototype study
should compare interaction paradigms, not visual polish, using the same five
situations in three treatments:

1. **Form-first** — conventional fields, sheets, and explicit object setup.
2. **Chat-only** — every create/change request expressed in conversation.
3. **Hybrid shared-object** — direct selection plus brief language, local
   deltas, proportional confirmation, and semantic undo.

### Fixture A — solo New York weekend

Starting evidence: “Maybe jazz Saturday,” two saved Places, a weather change,
and no exact schedule.

Test:

- add a possibility without choosing a time;
- ask Vesper to make the night less rushed;
- compare two venues in context;
- keep one privately;
- remove it without residue.

### Fixture B — Brooklyn dinner with friends

Starting evidence: host expresses a dinner, Maya has a private dietary
constraint, Luis contributes a restaurant, one invitee is not on Vesper.

Test:

- create the Occasion from ordinary language;
- invite people without an Occasion-profile flow;
- incorporate a contribution in place;
- produce a safe shared comparison without exposing private context;
- make a shared decision with independent responses;
- withdraw or correct cleanly.

### Fixture C — Italy trip projection

Starting evidence: flights, trains, ferry tickets, photographs, visited Places,
uncertain occurrences, and attention expressed in Chat.

Test:

- reconstruct a day without building an itinerary;
- correct one false occurrence;
- turn a past Place into a New York opening;
- reshape the composition without changing the evidence;
- save or share one exact version.

### Fixture D — flight disruption

Starting evidence: confirmed flight, delay, hotel, dinner, companion, provider
alternatives.

Test:

- Vesper prepares a coherent adaptation;
- person changes one preference by touch or voice;
- system distinguishes private planning from provider action;
- one confirmation crosses the external boundary;
- partial failure produces a useful recovery state.

### Fixture E — post-trip return to New York

Starting evidence: Italy is recent, the coming weekend is open, friends have
nearby activity, and Home has new synthesis.

Test:

- Home provides value without requesting reflection;
- user selects an opening and says “make this work with Maya”;
- Chat receives exact origin context;
- a private possibility becomes a social proposal only at explicit intent;
- Life retains only what earns continuity.

## 8. Measures

The study should measure:

- time to first useful state;
- number of words, taps, screens, and clarification turns;
- fraction of user effort spent expressing human intent versus system schema;
- ability to predict what will change before consequential confirmation;
- ability to identify what changed after application;
- local correction success without whole-object regeneration;
- number of surface changes needed to complete or repair an action;
- rate of unnecessary confirmation and unnecessary clarification;
- state-refinding after five minutes and after one day;
- comprehension of owner, audience, proposal versus applied state, and Undo;
- perceived control, ownership, effort, and administrative burden;
- contribution burden relative to immediate and later value;
- multiplayer coordination messages outside Vesper; and
- whether people can leave the interaction without “finishing setup.”

Do not use message count, time in Chat, edit count, or number of created objects
as success metrics.

## 9. Strong recommendations

### Adopt for prototype research

1. **Hybrid shared-object editing** as the default model.
2. **Visible selection as prompt context**, so people can say “this.”
3. **One typed command path** for Chat, touch, voice, and object-native actions.
4. **Incremental formalization**: structure rises only with useful computation,
   refinding, collaboration, or consequence.
5. **Local semantic delta + Undo** for private reversible changes.
6. **One exact preview at a material boundary** for affected people, audience,
   provider, money, public effect, or weak reversal.
7. **Stable landmarks with variable emphasis**, not arbitrary generated UI.
8. **Object-native contextual capability cues**, not blank-chat dependence or
   permanent action menus.
9. **Common operational ground with attributed plural lanes** in multiplayer.
10. **Autonomy scoped by action family**, learned through use rather than a
    universal settings screen.

### Do not build yet

- a universal AI edit modal;
- a comprehensive Plan or Occasion form;
- a generic permission or role-management surface;
- an AI-generated component tree or arbitrary mobile layout runtime;
- a universal draft-object service;
- a second state store inside Chat;
- an activity feed for every shared edit;
- whole-composition regeneration as the normal correction path;
- global “always ask / never ask” autonomy settings;
- manual type, category, rank, or audience maintenance for every Plan item;
- a requirement to review AI structure before receiving value; or
- a production rewrite before the comparative fixtures expose actual seams.

## 10. The lightweight doctrine

The research can be compressed into ten product laws:

1. **Let people point before making them specify.**
2. **Let them say only what the visible context does not already say.**
3. **Give value before asking them to organize, classify, or reflect.**
4. **Add structure only when structure unlocks a real benefit or consequence.**
5. **Apply the smallest private reversible change and make Undo obvious.**
6. **Pause once, at the real human or world boundary—not before and after it.**
7. **Show change on the thing that changed.**
8. **Keep shared facts common and human contributions attributable.**
9. **Let stable native surfaces carry a dynamic semantic composition.**
10. **Automate the administration; preserve human meaning, relationship, and
    commitment.**

## Closing judgment

Vesper's opportunity is not to replace forms with chat. It is to make the
person's lived fragments, visible objects, ordinary language, and real-world
context sufficient for useful computation and coordinated action.

The experience should feel less like operating planning software and more like
working on the actual Saturday, dinner, journey, Place relationship, or shared
moment itself. The object stays in front of the person. Vesper does the
translation behind it. The world changes only as far as the person's authority
and intention justify.

That is the lightweight version of an ambitious product: not fewer
capabilities, but far less interface between attention and consequence.
