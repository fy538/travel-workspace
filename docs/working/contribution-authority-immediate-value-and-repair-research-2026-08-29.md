---
doc_type: working
status: active
owner: founder / product / architecture
created: 2026-08-29
expires: 2026-09-28
why_new: Researches the connected input-system questions of contribution authority, immediate differentiation from current general-assistant memory, and interpretation receipt and repair; no existing document joins current external evidence to the implemented Admission and Intake seams.
promotes_to: null
supersedes: []
---

# Contribution authority, immediate value, and repair research

## Question or outcome

What should happen when a person gives Vesper a question, observation, artifact,
invitation, or intention in Chat?

This investigation focuses on three connected questions:

1. **Authority:** what may Vesper create or retain automatically, what requires
   confirmation, and when is a receipt plus correction or Undo sufficient?
2. **Immediate differentiated value:** what can current ChatGPT memory already
   do, and what must Vesper return in the same interaction to be meaningfully
   different rather than a specialized chatbot with memory?
3. **Interpretation, receipt, and repair:** how should Vesper show what it
   understood, distinguish evidence from inference, and let a person correct the
   exact mistake without repairing the system's ontology for it?

Persistent value on Home and Places is intentionally not the primary subject.
Those surfaces are downstream consumers of a trustworthy contribution. This
note studies the contribution transaction that makes them possible.

## Executive conclusion

The repo already contains most of the right internal ideas, but not yet one
simple user-facing input contract.

The product should not ask permission before every useful act, nor treat every
message as permission to build a biography. It should distinguish the human
gesture:

- **Ask** authorizes use for an answer. It does not normally create a durable
  Life object.
- **Point, Bring, or Import** is an intentional contribution gesture. It can
  authorize private custody and a low-authority, source-bound interpretation
  with a quiet receipt and immediate repair. It does not prove occurrence,
  preference, meaning, audience, or action authority.
- **Keep, Share, Invite, Decide, or Act** authorizes only the named consequence
  when actor, object, owner, audience, and reversibility are clear. Social,
  external, financial, public, or weakly reversible boundaries still require
  the affected principal or an explicit mandate.

Internally, retain the canon's five permission axes and seven consequence modes.
Externally, reduce them to three treatments:

| Treatment | What the person experiences | Appropriate boundary |
| --- | --- | --- |
| **Answer or prepare privately** | Immediate value; no workflow | No durable consequence, or ephemeral private preparation |
| **Apply privately, then receipt** | Useful result first; compact “what changed” plus Correct/Undo | Expected, self-owned, reversible, source-bound consequence |
| **Preview the material boundary** | One concrete proposal and one decision | New audience, affected person, spend, provider contact, public action, sensitive inference, or weak reversal |

The most important competitive finding is equally clear: **persistent memory is
not Vesper's differentiation.** ChatGPT's current memory automatically
synthesizes context from chats, files, and connected apps, exposes a memory
summary and response-level sources, and supports conversational correction.
Vesper must instead create an immediate **object-and-consequence delta**:

```text
understand the immediate job
  + resolve what this source or statement is
  + situate it among Place, Moment, people, Occasion, Plan, and prior evidence
  + contribute a new explanation, distinction, reconstruction, or capability
  + make the smallest authorized consequence available
  + leave inspectable lineage and precise repair
```

The compact strategic sentence is:

> A general assistant may remember what you told it. Vesper must know what this
> contribution is in your lived world, add something you did not already have,
> and make the smallest appropriate consequence available now.

That sentence describes the target advantage, not current shipped proof. The
repository has a strong custody, lineage, candidate-authority, receipt, and
context foundation, but the source-bound first-turn interpretation and
consequence experience remain incomplete.

## 1. What the repository already establishes

### 1.1 Product doctrine

The current [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md)
and [Product Model](../../travel-agent/docs/product/Product%20Model.md) establish
the right starting posture:

- accept before organizing;
- solve the immediate job first;
- infer possibilities without authoring identity or fact;
- reconcile consequences through their durable owner;
- preserve only what can change a later experience; and
- treat memory as substrate rather than product outcome.

The [Experience Constitution and Interaction
Grammar](vesper-experience-constitution-and-interaction-grammar-2026-08-22.md)
already distinguishes five permission axes—use, retention, inference, audience,
and action. The [consequence arbitration
blueprints](consequence-arbitration-and-cross-surface-blueprints-2026-08-26.md)
already define seven authority modes, including bounded natural-language
authorization for reversible self-owned action and explicit boundaries for
affected principals, mandates, providers, spend, and public action.

The [Editorial and Content
Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md)
adds the semantic bar: Vesper must not paraphrase the person's input, turn
attention into a personality claim, or ask the person to supply the missing
value. It must restructure, explain, differentiate, or transfer.

These are compatible. The missing layer is not another ontology. It is a
legible default contract for the contribution gesture.

### 1.2 Implemented foundation

The code is more advanced on custody and policy than on the visible return:

- `AdmissionEnvelope` binds actor, origin, audience, source kind, immediate
  job, source references, and requested retention.
- The current from-Chat share path chooses `answer_only` and preserves durable
  source identity through the pending turn.
- Intake v2 separates raw custody, normalization, source-bound observations,
  semantic candidates, proposals, and canonical activation.
- A semantic candidate cannot grant itself effective retention or action
  authority. It begins private and advice-only; proposed capabilities stay
  blocked for policy review.
- Claims carry truth mode, confidence, evidence references, and expiry.
- The dogfood artifact grammar already names precise corrections such as wrong
  Place, wrong time, not my artifact, did not go, detach from Occasion, change
  audience, forget interpretation, delete original, and delete derived state.
- Intake deletion can cancel linked workflows; M1 receipts support idempotent
  admission, owner readback, and reversal.

This is unusually strong groundwork. It means the next product work can be a
thin policy-and-experience layer over real seams, not a greenfield memory
system.

### 1.3 Current gaps and tensions

1. **`answer_only` is too blunt for all from-Chat shares.** It is correct for a
   question. It may undercut the product when someone deliberately points at or
   imports an artifact expecting it to become part of their lived-world record.
   The immediate job and the human gesture need to jointly determine retention.
2. **Legacy `needs_review` can manufacture homework.** The older ingestion
   strategy raises ambiguity and multi-candidate results into review. The newer
   principle should be: ask only when ambiguity changes a material consequence;
   otherwise preserve a provisional private interpretation with correction.
3. **“Permanent envelope, always” is no longer acceptable doctrine.** The July
   ingestion research proposed permanent envelopes even for dismissed and
   failed inputs. Intake v2's bounded raw retention and deletion lineage are
   more consistent with current contextual-integrity and causal-forgetting
   work. Retention needs a purpose and lifecycle.
4. **The internal receipt is richer than the visible repair.** The mobile
   receipt components can show public reasons, sources, degraded state, and
   private-context use, but the generic “Why Vesper suggested this” treatment
   is action-centric and sometimes narrates the product. The rendered detail
   path does not yet expose the full underlying Undo/correction vocabulary.
5. **Interpretation is not yet the first-turn product.** M2 correctly closes
   custody-to-conversation admission without claiming situated interpretation.
   The next boundary remains family-specific, source-bound immediate utility
   through the existing context engine.

## 2. Area one: authority and progressive autonomy

### 2.1 What the external evidence says

Human-AI guidance converges on a contextual model rather than blanket consent
or blanket automation:

- Microsoft's validated human-AI guidelines recommend efficient invocation,
  dismissal, and correction; scoping when uncertain; explaining why; cautious
  adaptation; visible consequences; and global controls. See [Guidelines for
  Human-AI Interaction](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/).
- Google PAIR warns that interaction does not necessarily express preference,
  asks products to explain what is collected and how it changes the experience,
  and recommends strategic, minimal requests with easy dismissal and reset.
  See [Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/).
- Android recommends minimizing broad permissions and using scoped, contextual
  alternatives such as pickers and one-time location controls. See [Minimize
  permission requests](https://developer.android.com/privacy-and-security/minimize-permission-requests).
- Google's agent-security work argues that an agent needs a human controller,
  limited powers, observable planning and action, and contextual, just-in-time,
  human-verifiable policy. See [Secure AI
  Agents](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/)
  and [Contextual Agent
  Security](https://research.google/pubs/context-is-key-for-agent-security/).
- A 2025 phone-automation study frames unnecessary questions and unauthorized
  action as the two sides of the same problem—and finds current models struggle
  to decide when interaction is needed. See [Agent-initiated interaction in
  phone UI automation](https://research.google/pubs/agent-initated-interaction-in-phone-ui-automation-2/).
- People are more willing to use an imperfect algorithm when they can modify
  its result, even when modification is tightly bounded. See [Dietvorst,
  Simmons, and Massey](https://faculty.wharton.upenn.edu/wp-content/uploads/2016/08/Dietvorst-Simmons-Massey-2018.pdf).

The design consequence is not “ask first.” It is **make the expected,
reversible private act easy to correct; interrupt only at a material boundary.**

### 2.2 The contribution gesture should carry narrow authority

Vesper should infer authority from the gesture only when the gesture is itself
deliberate and the inferred authority remains narrow.

| Gesture | Safe immediate authority | What it does not authorize |
| --- | --- | --- |
| Ask a question | Use supplied and already authorized context to answer | Durable artifact, broad memory update, preference claim, share, action |
| Point out an observation | Use now; create a private source-bound attention trace when the product has made this default legible | Occurrence, preference, identity, public contribution |
| Drop or share an artifact into Vesper | Private custody, extraction, provisional binding, immediate utility, receipt and correction | “Visited,” “liked,” personal meaning, Occasion audience, provider action |
| “Keep/remember this” | Named private retention, with readback and Undo | Broad inference or use for unrelated purposes |
| “Add this to Rome / Friday dinner” | Reversible self-owned mutation if owner and target are unambiguous | Changing another person's commitments or exposing private fields |
| Invite, share, publish, book, buy, cancel | Prepare the exact effect | Execution without the affected-principal, spend, provider, audience, or public boundary being authorized |

This is the critical distinction between **explicit contribution** and
**implicit telemetry**. Choosing Vesper in a share sheet, uploading a ticket,
or deliberately pointing at a dish is not the same as the app silently treating
a click or dwell as preference evidence. The former can authorize private
custody; the latter requires prior disclosure and should remain weak evidence.

### 2.3 Do not turn progressive autonomy into silent scope creep

Autonomy should be earned locally, not globally:

```text
repeated acceptance
  -> evidence that a specific bounded action may be welcome
  -> Vesper offers a named mandate
  -> person accepts, narrows, pauses, or declines
  -> every use remains inspectable and revocable
```

Repeated acceptance may justify offering “Automatically file my flight
confirmations privately.” It must not silently become “Use all email to infer
my travel, relationships, and preferences.” Familiarity increases prediction
confidence; it does not itself increase authority.

The mandate should bind:

- action family;
- source or channel;
- owner and audience;
- Place, Occasion, or time scope when relevant;
- spend or materiality ceiling;
- expiry or review point; and
- revocation and readback destination.

### 2.4 Recommended default input contract

The initial contract should be learned through use, not an onboarding wall:

> Ask anything for an answer. Bring something to let Vesper understand it and
> place it privately. Vesper will show what changed. Sharing with people or
> acting in the world stays a separate choice.

The contract needs a visible temporary/no-retention path, but it should not
occupy every turn. Current ChatGPT research and product behavior both show that
people need fresh-start contexts; recent ACL work additionally finds that
all-or-nothing memory use can create “memory anchoring,” and that explicit
control over how strongly past memory shapes a response can outperform rigid
memory inclusion or exclusion. See [Controllable Memory
Usage](https://aclanthology.org/2026.acl-long.670/).

Vesper should eventually support three memory-use postures at the point of
application, not as a universal personality slider:

- **fresh:** answer from this contribution and current world only;
- **situated:** use the relevant Occasion, Place, people, and current state;
- **continuity:** also use prior authorized outcomes and evidence.

The system should select a sensible default and expose the posture when it
materially changes the answer. It should not make the person configure it for
every request.

## 3. Area two: ChatGPT baseline and Vesper's immediate advantage

### 3.1 The 2026 baseline is much stronger than “saved facts”

OpenAI's current product documentation says ChatGPT memory:

- automatically synthesizes useful context from chats, files, and connected
  apps;
- maintains an automatically updated memory summary;
- can show which memories, past chats, files, or instructions helped
  personalize a response;
- lets users correct the summary or response-level memory source;
- can use a non-personalized Temporary Chat, or use existing personalization
  temporarily without writing new memories; and
- is moving from manually triggered saved memories to a background synthesis
  architecture designed for freshness, continuity, and relevance.

See OpenAI's current [Memory
FAQ](https://help.openai.com/en/articles/8590148-memory-and-controls-faq),
[Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq),
and [Dreaming memory architecture](https://openai.com/index/chatgpt-memory-dreaming/).

This eliminates several weak differentiation claims:

- “Vesper remembers you.”
- “Vesper uses past conversations.”
- “Vesper accepts files and tickets.”
- “Vesper makes personalized connections.”
- “Vesper shows why it remembered something.”

Those may be required capabilities. They are not a product thesis or moat.

### 3.2 What a general memory assistant is optimized to return

Based on documented behavior, current ChatGPT is positioned to retrieve
relevant past context and use it to produce a more personalized conversational
answer. It may remember that someone is in New York, recently visited Italy,
likes a kind of food, is planning a trip, or has a relevant file or email. It
can answer, synthesize, brainstorm, and use connected information without the
person restating it.

What the documentation does **not** establish is a durable, domain-governed
lived-world model with separate authorities for Source, Place, Moment,
Occasion, Plan, Commitment, Occurrence, Outcome, audience, and affected-person
action. Nor does it prove that every conversational memory is reconciled into
an authoritative operational object with causal correction and downstream
invalidation.

That is the opening for Vesper, but it remains a hypothesis until measured
against the actual product rather than against an outdated caricature.

### 3.3 The immediate Vesper return must contain a real delta

Vesper should be judged by six layers. Not every response needs all six visibly,
but its differentiated cases should combine more than fluent recall:

1. **Job resolution:** answer why the person brought this now.
2. **Object resolution:** identify what the source or statement is without
   inflating its truth state.
3. **Situating:** bind it to the relevant Place, Moment, people, Occasion, Plan,
   and current world truth.
4. **Contribution:** add a reconstruction, mechanism, contrast, relation, or
   capability that was not in the input or prior semantic receipt.
5. **Consequence:** privately prepare or apply the smallest authorized change
   through the object that owns it.
6. **Governance:** preserve source, author, audience, uncertainty, correction,
   and owner readback.

This is why the live engine matters even outside an active trip. It is not a
separate “travel rescue” product. It is the runtime that can ask what the input
changes **in this moment**—a nearby possibility, a commitment, a social opening,
a route, a future cue, or nothing.

### 3.4 Comparative examples

#### “Sorrento has cliffs”

A weak personalized assistant repeats or decorates the observation. A Vesper
return should add one source-backed relation: for example, distinguish
Sorrento's tuff terrace from the limestone relief of the Amalfi Coast and
compare the way settlement and transport meet each edge. If the observation
was deliberately pointed out to Vesper, the quiet consequence can be a private,
source-bound attention trace—not a personality claim that the user “loves
cliffs.”

#### A ferry ticket

A generic answer can extract route, date, and operator. A stronger Vesper return
resolves whether the ticket is evidence of a planned or completed leg, places it
in the correct journey without claiming the trip occurred, reconciles it with
other movement evidence, and says what changed now. If it closes a missing
transport transition, that is the immediate reconstruction. If a live schedule
or current commitment is affected, that is the operational consequence.

#### A pasta photograph

Identification alone is commodity. Vesper can separate what is visible from
what is inferred, explain the preparation mechanism that likely accounts for
the noticed texture, connect it to a relevant Place or later cooking possibility,
and preserve the photograph without asserting where it was taken, who ate it,
or whether they liked it.

#### A friend's Paris trace

A generic memory system can mention that both people were in Europe. Vesper's
social value begins only when the friend's permissioned evidence changes the
object: an attributed Rome–Paris contrast, a prepared private handoff, or a
shared Occasion consequence. It must preserve the friend's authorship and
audience and avoid manufacturing one shared interpretation.

### 3.5 Be honest about current product progress

The differentiated architecture is partially present:

- typed sources and evidence locators;
- source-bound observations and candidates;
- current-context compilation;
- blocked capability proposals;
- action receipts, idempotency, readback, deletion, and reversal;
- Place, Plan, group, and experience-graph owners.

The end-to-end differentiated **first return** is not yet broadly present. M2
explicitly stops at source-bound answer admission; family-specific situated
interpretation and authorized consequence are the next boundary. The product
should not claim “Vesper knows what this changes in your life” until the target
fixtures produce that result reliably in the actual app.

## 4. Area three: interpretation, receipt, and repair

### 4.1 The system must preserve the derivation chain

Use this conceptual chain even if implementation reuses existing tables:

```text
Source
  -> extracted Observation
  -> provisional Interpretation or Candidate
  -> governed Claim or binding
  -> canonical owner mutation, if authorized
  -> viewer-relative Projection
  -> Receipt
```

These stages answer different questions:

- What did the person actually provide?
- What did Vesper observe in it?
- What relationship did Vesper infer?
- Which truth did an owner accept?
- What did a particular viewer see?
- What changed, and how can it be repaired?

The W3C provenance model is useful as a structural analogy: entities,
activities, agents, derivation, attribution, revision, and invalidation form a
lineage rather than a flattened memory blob. Vesper does not need to adopt RDF
or PROV-O wholesale, but it should preserve those causal distinctions. See
[W3C PROV-O](https://www.w3.org/TR/prov-o/).

### 4.2 Confidence is not the primary user control

Model probability is often the wrong thing to show. A study of uncertainty
highlighting found that tokens likely to require human editing were more useful
than raw generation-probability highlights; users preferred uncertainty cues
that were granular, informative, interpretable, and not overwhelming. See
[Vasconcelos et al.](https://www.microsoft.com/en-us/research/publication/generation-probabilities-are-not-enough-exploring-the-effectiveness-of-uncertainty-highlighting-in-ai-powered-code-completions/).

For Vesper, expose uncertainty where the **repair choice changes**:

- “Matched to the Aug 19 Sorrento–Amalfi ferry from route and timestamp.”
- “Scheduled; not evidence that you boarded.”
- “Place match uncertain between two venues.”
- “Maya shared this with friends; not public.”

Avoid confidence dashboards and generic “82% sure.” The person needs to know
which claim may be wrong and what they can do about it.

Natural-language uncertainty can reduce overreliance, but wording matters. A
pre-registered study found that first-person uncertainty reduced agreement and
increased accuracy in its medical-question task. See [Kim et
al.](https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/).
Vesper should therefore state the uncertain proposition directly, not spread
vague hedging across the entire answer.

### 4.3 Three receipt tiers

The receipt should follow value, not replace it.

#### Tier A: micro-receipt

For expected, private, reversible organization:

```text
Added privately to Southern Italy · Correct · Undo
```

This is enough when the source, Place, and consequence are obvious and no
meaning or shared authority was inferred.

#### Tier B: interpretive receipt

When an inference materially shaped the result:

```text
Matched to the Aug 19 Sorrento–Amalfi ferry from the route and timestamp.
Kept as scheduled—not as proof you boarded. · Correct
```

The visible unit contains:

- the consequential interpretation;
- its evidence basis;
- the truth boundary;
- audience or owner when surprising; and
- the relevant repair.

#### Tier C: boundary preview and execution receipt

Before or after a social, external, financial, public, or weakly reversible
effect:

```text
Share this photograph and your caption with Maya only.
The Italy journey and private notes stay private. · Share
```

After execution, show authoritative readback and a real recovery path where
one exists.

### 4.4 Repair should match the person's objection

“Wrong” is not one event. Vesper should support distinct repairs:

| Person's objection | Repair operation |
| --- | --- |
| “That is not the right Place.” | Rebind Place; invalidate Place-dependent projections |
| “The time is wrong.” | Correct time; recompute sequence and current relevance |
| “This is not mine.” | Correct authorship/ownership; remove it from personal projections |
| “I had a ticket but did not go.” | Preserve artifact; retract Occurrence; recompute journey |
| “Don't treat this as a preference.” | Keep source/episode; revoke inference purpose |
| “Remove it from this dinner.” | Detach Occasion binding; preserve other valid scopes |
| “Maya can see it, but not the group.” | Change audience projection; revoke wider copies |
| “Forget the interpretation, keep the photo.” | Invalidate derived claims; retain Source |
| “Delete this.” | Delete or revoke Source under retention policy; invalidate dependent claims, projections, and pending work |
| “Undo what Vesper did.” | Reverse the canonical mutation when compensatable |

This is where Vesper can surpass a global memory editor. A person should be able
to correct the **relationship that is wrong** without deleting a valuable source
or understanding the database model.

### 4.5 Forgetting must be causal

Deleting an item from a list is insufficient if it continues to influence
ranking, Home, Places, a Plan, a social projection, or a pending provider job.
Correction and deletion should propagate through dependency lineage:

```text
correct / revoke / delete
  -> invalidate dependent observations or claims
  -> recompute or withdraw projections
  -> cancel or reauthorize pending consequences
  -> retain only the minimum audit tombstone required for safety or law
  -> show completion receipt
```

OpenAI's current memory documentation illustrates why causal deletion is hard:
fully deleting something may require removing it from every chat, file, memory
summary, and connected source where it appears. Vesper should make the causal
scope inspectable and execute the dependency cleanup as one user-level command
where its own authorities permit it.

### 4.6 Privacy evidence raises the bar for cross-context reuse

A 2025 survey experiment with 300 US ChatGPT users found that 82% rated chatbot
conversations sensitive or highly sensitive, while many still discussed health
and finances. Respondents were much more willing to let a chatbot use its own
chat history than to grant search, email, or device access; informed consent and
transmission safeguards were especially important to perceived appropriateness.
See [Understanding Privacy Norms Around LLM-Based
Chatbots](https://arxiv.org/abs/2508.06760).

The finding should not be universalized beyond that US sample, but it supports
three Vesper rules:

- chat intimacy is not evidence of broad reuse permission;
- crossing application, person, Occasion, or audience boundaries deserves
  stronger legibility than private same-context use; and
- the product must demonstrate recognizable value from connected data rather
  than assume people will trade access for abstract personalization.

Preliminary CHI 2025 research also found incomplete user mental models of what
agents remember and how memory affects behavior, along with a desire to organize
memory by user or task needs. See [Users' Expectations and Practices with Agent
Memory](https://doi.org/10.1145/3706599.3720158). This supports Vesper's
object- and Occasion-scoped governance over one opaque global profile.

## 5. One combined contribution transaction

The three research areas produce one product loop:

```text
Ask / Point / Bring / Import
  -> infer immediate job and narrow authority
  -> admit source under private custody or answer-only use
  -> resolve observations without inflating truth
  -> compile only the authorized situated context
  -> return immediate semantic or capability value
  -> prepare or apply the smallest consequence under policy
  -> show the quietest sufficient receipt
  -> allow exact repair, causal invalidation, or completion through silence
```

The loop is successful only if the person gets value before being asked to
classify, confirm, reflect, organize, or maintain the system.

### 5.1 The first-turn response anatomy

For an actual contribution, the target first turn is:

1. **Immediate answer or contribution** — the new substance.
2. **Resolved object or state** — only when structure improves comprehension or
   consequence.
3. **One consequence** — already applied if narrow and reversible, otherwise a
   concrete preview at the boundary.
4. **Quiet receipt** — what changed, scope, and relevant repair.
5. **Stop** — no trailing homework question.

A simple question may end at step one. An artifact may use all five. The
interface should not expose the same anatomy for every turn.

## 6. Decisions recommended now

1. **Adopt Ask versus Point/Bring as the primary retention distinction.** Do
   not use message versus file alone; infer the human job and gesture.
2. **Make Point/Bring private by default, not answer-only by default.** Permit
   source custody and provisional, source-bound interpretation; do not infer
   Occurrence, preference, identity, audience, or action.
3. **Keep the five permission axes internally.** Do not reduce the policy model
   to private/shared or remember/don't remember.
4. **Expose only three user-facing consequence treatments.** Answer/prepare,
   apply privately with receipt, or preview the material boundary.
5. **Treat learned autonomy as an explicit bounded mandate.** Repetition may
   trigger the offer, not silently create the grant.
6. **Replace generic review queues with provisional private state wherever
   ambiguity is non-material.** Ask only when the answer changes audience,
   authority, owner, or consequential truth.
7. **Build interpretation receipts, not just action receipts.** Show the claim
   boundary and the repair that matters; do not lead with system narration.
8. **Make correction causal.** Source, claim, binding, projection, and pending
   consequence dependencies must be invalidated together.
9. **Do not position memory as differentiation.** Position immediate structured
   judgment, situated consequence, multiplayer authority, and lived-world
   continuity as the advantage.
10. **Derive the advantage from the category structure, not a point-in-time
    product race.** Use current ChatGPT documentation to set the assistant-memory
    capability floor, current Vesper code to identify migration seams, and the
    complete fixture portfolio to prove that one contribution contract covers
    the intended product.

## 7. Structural derivation program

### 7.1 Capability-floor analysis

Use three distinct forms of evidence without pretending they are comparable
product conditions:

1. **Documented assistant capability floor:** what a current general assistant
   can already remember, retrieve, explain, draft, temporarily avoid retaining,
   or perform through tools. This prevents Vesper from mistaking memory or
   fluent personalization for differentiation.
2. **Current Vesper implementation envelope:** which existing contracts can be
   retained, which legacy assumptions conflict with the pivot, and where the
   migration seam actually lies. Current UX quality is not evidence against the
   target thesis because most of that thesis is not implemented yet.
3. **Target structural contract:** the objects, truth states, authority,
   consequences, projections, and causal repair required by the product vision.

Pressure the contract through at least these fixtures:

- plain practical question that should not persist;
- explicit observation such as “Sorrento has cliffs”;
- ferry or train ticket;
- restaurant or pasta photograph;
- movie ticket plus later Place question;
- reservation with a live inconsistency;
- friend-authored artifact with a bounded audience;
- invitation or group decision with one private constraint;
- correction: ticket existed, but the person did not go; and
- temporary exploration that must not influence future output.

For each fixture, derive:

- the immediate job and minimum useful first turn;
- which durable object, if any, must exist afterward;
- the allowed truth state and forbidden inference;
- the smallest authorized consequence;
- what changes on Home, Places, Life, an Occasion, or nowhere;
- the required provenance and correction path; and
- whether a general assistant can reproduce only the prose or also the governed
  state transition.

The critical test is structural substitutability. If copying the target prose
into a generic chatbot would preserve the product's value, the fixture is not
differentiated enough. If the value depends on durable typed objects, situated
projection, affected-person authority, or causal withdrawal across surfaces,
it belongs to Vesper's category thesis.

### 7.2 Permission derivation

The research is sufficient to choose the default architecture:

- **Ask:** answer with authorized continuity and create no new durable personal
  state unless the person explicitly asks to Keep.
- **Point / Bring:** create private, source-bound state and provide the value
  first when ownership is clear, the consequence is reversible, and no claim of
  occurrence, preference, identity, audience, or action is required.
- **Material ambiguity:** keep the source and a provisional interpretation, but
  ask only when resolving the ambiguity changes canonical truth or a downstream
  consequence.
- **Audience, affected-person, provider, spend, public, sensitive-inference, or
  weak-reversal boundary:** preview the prepared effect before crossing it.

This follows from three combined findings: confirmation before value creates
homework; silent person-level inference violates contextual expectations; and
reversible private organization has a materially smaller trust footprint than
sharing or action.

Later usability research may still ask:

- What do you think Vesper kept?
- What do you think it may use later?
- Who can see it?
- What do you expect to happen next?
- Did anything feel surprising or invasive?
- Would you rather correct this result or have been asked beforehand?

That research tunes receipt prominence, wording, and repair discoverability. It
does not reopen the underlying authority model unless it reveals a material
misunderstanding of who can see something or what real consequence occurred.

### 7.3 Repair drill

Seed one wrong relation at a time: Place, time, authorship, Occurrence,
preference inference, Occasion, audience, or source retention. Observe whether
the person can identify and repair it from the immediate response without
opening settings or knowing Vesper's nouns.

Then verify the downstream effect:

- Home and Places withdraw or recompute dependent units;
- Life preserves the valid source or record when requested;
- shared projections update for every affected viewer;
- pending actions cancel or require reauthorization; and
- the receipt describes the completed scope honestly.

## 8. Suggested next artifact

Do not immediately rewrite the whole canon. First produce a small, comparable
[**Contribution Contract Fixture Pack**](contribution-contract-fixture-pack-2026-08-29.md)
with ten inputs and, for each:

- the human gesture and immediate job;
- five-axis authority;
- expected first-turn value;
- source/observation/claim truth boundary;
- consequence treatment;
- visible receipt;
- repair paths;
- documented general-assistant capability floor;
- current Vesper code envelope and migration seam; and
- target Vesper contract and structural delta.

That pack can derive the shared input architecture and the next implementation
slice. Later usability work can refine presentation without making the current
products arbiters of the product thesis.

## Evidence

Local sources:

- [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md)
- [Product Model](../../travel-agent/docs/product/Product%20Model.md)
- [Vesper Editorial and Content Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md)
- [Experience Constitution and Interaction Grammar](vesper-experience-constitution-and-interaction-grammar-2026-08-22.md)
- [Consequence Arbitration and Cross-Surface Blueprints](consequence-arbitration-and-cross-surface-blueprints-2026-08-26.md)
- [Unified Ingestion Research](unified-ingestion-research-2026-07-27.md)
- [Work Receipt](work-receipt-2026-07-26.md)
- [M1 Command, Receipt, and Delivery](m1-command-receipt-delivery-execution-2026-08-23.md)
- [M2 Admission and Situated Context](m2-admission-situated-context-2026-08-23.md)
- `travel-agent/backend/core/models/admission.py`
- `travel-agent/backend/inbound/semantic_contract.py`
- `travel-agent/backend/inbound/FEATURE.md`
- `travel-app/app/share-capture/index.tsx`
- `travel-app/components/chat/ChatReceiptDisclosure.tsx`
- `travel-app/components/receipts/VesperReceipt.tsx`

External sources:

- [OpenAI Memory FAQ](https://help.openai.com/en/articles/8590148-memory-and-controls-faq)
- [OpenAI Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq)
- [OpenAI, Dreaming: Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/)
- [Microsoft, Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/)
- [Google PAIR, Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/)
- [Google, Contextual Agent Security](https://research.google/pubs/context-is-key-for-agent-security/)
- [Google, Agent-initiated Interaction in Phone UI Automation](https://research.google/pubs/agent-initated-interaction-in-phone-ui-automation-2/)
- [Huang et al., Controllable Memory Usage](https://aclanthology.org/2026.acl-long.670/)
- [Jones et al., Users' Expectations and Practices with Agent Memory](https://doi.org/10.1145/3706599.3720158)
- [Tran et al., Understanding Privacy Norms Around LLM-Based Chatbots](https://arxiv.org/abs/2508.06760)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [Kim et al., LLM Uncertainty Expression](https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/)
- [Vasconcelos et al., Generation Probabilities Are Not Enough](https://www.microsoft.com/en-us/research/publication/generation-probabilities-are-not-enough-exploring-the-effectiveness-of-uncertainty-highlighting-in-ai-powered-code-completions/)
- [Dietvorst, Simmons, and Massey, Overcoming Algorithm Aversion](https://faculty.wharton.upenn.edu/wp-content/uploads/2016/08/Dietvorst-Simmons-Massey-2018.pdf)

## Exit

Before expiry, use the fixture pack and structural evidence to:

- promote the contribution-gesture defaults and three visible treatments into
  the interaction grammar and consequence canon;
- create a scoped implementation plan for the source-bound first-turn
  contribution and interpretation-repair receipt;
- preserve later comprehension testing as a UI validation task rather than a
  strategy gate; and
- archive this note as point-in-time competitive and HCI evidence.
