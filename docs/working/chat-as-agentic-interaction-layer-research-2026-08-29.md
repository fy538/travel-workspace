---
doc_type: working
status: active
owner: founder / product / architecture / AI systems
created: 2026-08-29
expires: 2026-09-28
why_new: Researches Chat as Vesper's cross-surface agentic interaction layer and reconciles that role with the contribution loop, current HCI evidence, and the implemented control-plane and artifact seams.
promotes_to: null
supersedes: []
related:
  - ../systems/concierge-vesper.md
  - ../systems/contribution-and-consequence.md
  - agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - agentic-capability-and-tool-cutover-plan-2026-08-29.md
  - chat-artifact-closed-loop-optimization-plan-2026-08-16.md
  - vesper-experience-constitution-and-interaction-grammar-2026-08-22.md
  - contribution-authority-immediate-value-and-repair-research-2026-08-29.md
---

# Chat as Vesper's agentic interaction layer

## Question

How can Chat be both the lowest-friction contribution path into Vesper and the
agentic interface through which a person asks, understands, plans, routes,
coordinates, acts, monitors, and repairs work across Home, Places, and Life?

The concern is valid. If Chat is described mainly as the first step of the
input loop, the product becomes a collection box. If Chat owns every object,
screen, and workflow, the product becomes an undifferentiated chatbot or a
super-app operated by prompts. Neither is the intended product.

## Executive conclusion

**Vesper is the agent. Chat is its primary conversational operating surface.**

The input loop is a compounding product loop, not the job description of the
Chat tab. Chat has two directions:

1. it helps a person contribute intent, attention, evidence, correction, and
   authority to Vesper; and
2. it lets the person interrogate and operate the lived-world model that those
   contributions, current reality, other people, and external systems make
   possible.

The synergy is strongest when these are not separate modes. A single turn can
use a contribution to improve the current job, complete that job through the
right owner, and admit only the authorized residue for future value.

```text
surface or conversation context
  + current human contribution
  + current Moment and relevant world state
        |
        v
compile immediate job, usable evidence, authority, and target owner
        |
        v
make sense / open possibility / help it work / carry forward
        |
        v
answer, compose, propose, act, monitor, reconcile, or route
        |
        v
canonical owner readback + compact receipt + return path
        |
        v
Home, Places, and Life reflect the new truth; authorized evidence compounds
```

Chat therefore should be neither a feed nor a second copy of every domain UI.
It is the **intent, composition, and coordination layer** over stable objects
and owners elsewhere in the app.

## 1. The role distinction that keeps the product focused

| Product element | Primary role | Must not become |
| --- | --- | --- |
| **Home** | Current value, openings, consequences, and what matters now | An inbox of requests for more input |
| **Places** | Spatial intelligence: what is here, why it matters, and what can work | A map-shaped clone of generic search |
| **Life** | Durable evidence, artifacts, people, places, Occasions, episodes, and continuity | A raw transcript or memory settings page |
| **Chat** | Interpret intent, compose across objects, operate capabilities, coordinate, and repair | The canonical database, a universal feed, or the only route to simple actions |

The distinction is not “output tabs versus input tab.” Home and Places can
launch actions; Life can be directly corrected and organized; Chat can return
substantial value. The distinction is:

- **stable surfaces expose inspectable objects and domain structure;**
- **Chat expresses open-ended intent and composes operations across them.**

That makes the four-root model stronger. Home, Places, and Life prevent the
agent's work from collapsing into a linear transcript. Chat prevents their
fixed interfaces from limiting what a person can ask or accomplish.

## 2. Why contribution and agency reinforce one another

### 2.1 Contribution is part of almost every useful turn

When a person says, “This dinner is for six, Nina cannot do dairy, and I want
somewhere we can linger,” the utterance is simultaneously:

- a request to find or shape something;
- evidence relevant to one immediate activity;
- a possible update to an Occasion or Plan;
- a possible private constraint with an audience boundary; and
- not automatically a durable global fact about Nina.

Vesper should not interrupt the job to ask the person to classify each clause.
It should compile a contribution-use grant, use the information for the current
purpose, produce value, and retain only what the gesture and consequence
contract permit.

### 2.2 Agency gives contributions immediate consequence

The contribution loop feels worthwhile when what the person gives changes the
quality of the current result immediately:

- a ticket can locate the relevant trip, recover the flight, update the travel
  state if authorized, and make the arrival usable in Home;
- “we are fading” can change a live route into one nearby stop and a ride home;
- a photo of a dish can identify it, connect it to a place and Occasion, and
  help find a credible version in New York;
- “compare this with Maya's Paris weekend” can retrieve only authorized shared
  evidence and produce a juxtaposition without exposing Maya's private model;
- “move Saturday dinner later and tell the group” can prepare or execute two
  owner-specific consequences, with the audience and action boundaries kept
  separate.

The user does not need an “ingest, then use” ritual. Contribution is a natural
byproduct of working with the agent; authorized durable value is a natural
byproduct of a useful turn.

### 2.3 The two permissions must remain independent

One utterance can grant information use without granting action, or grant an
action without granting broad retention.

| Contract | Governing question | Example |
| --- | --- | --- |
| **Contribution use** | What may Vesper use, infer, retain, learn, or expose from this contribution? | Use Nina's dairy constraint for this dinner; do not add a global profile fact |
| **Action authority** | What may Vesper change, send, spend, book, publish, or otherwise cause? | Prepare the group message; do not send until the named boundary is authorized |

Success at one contract never implies success at the other. Booking a table
does not authorize permanent preference learning. Keeping an artifact does not
authorize sending it to a friend.

## 3. A turn is an activity, not an intake event

The current internal `INTAKE | CONVERSATION | PROACTIVE` turn taxonomy is too
coarse for the product now emerging. It describes how a thread began, not what
the person and agent are doing.

A better turn compiler should represent these orthogonal dimensions:

| Dimension | Examples |
| --- | --- |
| **Immediate job** | understand, compare, explore, shape, coordinate, operate, monitor, repair |
| **Origin** | clean Chat, Home opening, Place, Life artifact, Occasion, Plan, notification |
| **Scope** | current object, current Moment, named episode, named people, account-wide search |
| **Target owner** | none, Place, Plan, Occasion, Life object, provider, relationship/audience system |
| **Agency ceiling** | read, privately compose, propose, commit, monitor/reconcile |
| **Contribution grant** | ephemeral, source-bound private, durable private, named audience, named action |
| **Return contract** | answer here, update origin, open owner, keep monitoring, notify on change |

These are internal semantics, not seven questions shown to the user. Most are
inferred from the entry object, language, existing authority, and current
Moment. Ask only at a material boundary or when two plausible interpretations
would produce meaningfully different consequences.

### 3.1 One turn may move through several phases

User-facing language should stay simple, while the runtime distinguishes:

1. **Inspect** — read canonical state and answer.
2. **Compose** — synthesize, compare, simulate, or privately prepare.
3. **Propose** — show a consequential candidate or exact delta.
4. **Commit** — execute an authorized, idempotent change.
5. **Monitor** — wait for or track a condition after the immediate turn.
6. **Reconcile** — read back owner/provider truth, surface uncertainty, and
   repair or recover.

This is not a six-item menu. It is a lifecycle. A request such as “find a good
dinner near the theater, move our plan, and let Alex know” may inspect Places,
compose alternatives, propose one choice, commit the Plan mutation, prepare or
send a message at the correct authority boundary, then reconcile both owners.

## 4. The agentic turn contract

### 4.1 Inputs

Every entry into Chat should carry a structured context envelope when one is
available:

```text
origin_surface
origin_object_refs[]
origin_view_or_selection
return_target
current_moment_ref
participant_and_audience_scope
existing_grants_or_mandates
```

The text box should not be responsible for reconstructing information the app
already knows. “Ask about this,” “compare,” “change,” “route around,” and
“invite” become intelligible because the selected objects arrive with the
turn.

### 4.2 Compilation

Before tool execution, Vesper compiles:

```text
AgenticTurnPlan
  immediate_job
  origin_refs
  target_owner_refs
  contribution_use_grant
  privacy_and_audience_scope
  permitted_capabilities
  agency_ceiling
  expected_postconditions
  return_contract
```

This should extend the existing `TurnPlan`, not create a competing orchestrator.
Capability retrieval then selects a narrow set of tools from the broad
registry. Narrow retrieval is appropriate; a universal first-turn intake lane
is not.

### 4.3 Execution

Each consequential tool call retains the existing action discipline:

- action envelope before dispatch;
- exact actor, scope, parameters, authority evidence, and idempotency key;
- expected postconditions;
- owner or provider execution;
- canonical readback;
- verified, failed, or honestly uncertain receipt.

### 4.4 Output

The default response has three possible parts, not a dashboard:

1. concise prose that answers or interprets;
2. at most one primary structured artifact when state, choice, progress,
   uncertainty, or control benefits from it; and
3. a compact receipt or owner link only when something changed or continues.

The artifact is a projection of an owned object or activity. It should support
direct manipulation where that is clearer than another prompt. Natural
language supplies intent and composition; controls supply visibility,
precision, feedforward, and repair.

## 5. Cross-surface synergy

### 5.1 Home and Chat

Home gives value without requiring conversation. Chat becomes useful when the
person wants to redirect, deepen, combine, or act on that value.

| From Home | Chat receives | Chat can do | Return |
| --- | --- | --- | --- |
| “A credible piece of the Amalfi coast in New York this weekend” | opening, evidence, time/place constraints | explain provenance, compare candidates, shape outing, invite, route | updated opening or Occasion; compact receipt |
| Live disruption | affected Plan segment, people, current location | explain, find alternatives, coordinate, mutate authorized plan | Home reflects resolved next step |
| Generated article or podcast | source set, claims, relevant life threads | interrogate, challenge, connect, keep, share | media remains in Home/Life with lineage |

Home should not merely say “Ask Vesper.” It should expose a few object-specific
verbs such as **Work this out**, **Compare**, **Plan around**, or **Use this**.

### 5.2 Places and Chat

Places supplies spatial scope and direct manipulation. Chat handles fuzzy
intent, tradeoffs, multi-object composition, and cross-domain consequences.

| From Places | Chat receives | Chat can do | Return |
| --- | --- | --- | --- |
| Selected area or cluster | viewport, selected places, time, companions | explain pattern, compare, build a route, find a missing stop | route/Place/Plan owner |
| One place | canonical Place plus relationship/evidence | answer why it fits, contrast, plan around it, send to someone | Place state or addressed handoff |
| “What works now?” | location, availability, weather, energy, commitments | produce one feasible next move and execute bounded consequences | Home/Place status updates |

Simple save, hide, vote, and map operations remain directly manipulable. Chat
earns the turn when intent is ambiguous, compositional, or spans owners.

### 5.3 Life and Chat

Life gives durable structure to what Chat would otherwise flatten into history.

| From Life | Chat receives | Chat can do | Return |
| --- | --- | --- | --- |
| Artifact | source, claims, custody, episode links | explain, correct, connect, reuse, share | repaired artifact or new authorized relation |
| Episode or Occasion | time/place/people/evidence graph | reconstruct, compare, continue, plan a recurrence | episode interpretation, new Occasion, or Home opening |
| Person/place relationship | viewer-relative authorized projection | find shared threads, prepare a cold opener, coordinate | private answer or named-audience consequence |

Conversation history is evidence, not the user's Life structure. Chat should
resume a durable object by reference rather than require reposting or
renarrating it.

### 5.4 Chat root

The clean Chat surface should remain calmer than Home or Places. It should not
be a second feed or capability catalog. Its entry state can show two to four
concrete, contextual affordances derived from:

- the current Moment;
- recent or selected objects;
- unfinished or monitoring work; and
- a broad, low-friction composer for text, voice, photo, file, link, location,
  or share-sheet input.

Good prompts reveal breadth through situated verbs, not generic examples:

- “Work out Saturday with Maya”
- “Use this ticket”
- “Compare these two places”
- “What changed with tonight?”

## 6. When Chat should and should not mediate

### Chat is the better interface when

- the person knows the outcome but not the sequence of app operations;
- intent is underspecified and benefits from shared context;
- several objects, people, times, places, or systems must be composed;
- tradeoffs require explanation or negotiation;
- an operation needs monitoring, reconciliation, or recovery;
- the person wants to interrogate why the app surfaced something; or
- the existing GUI does not have a stable, frequently used interaction.

### Direct UI is better when

- one visible object has one familiar, low-risk action;
- precise selection or spatial manipulation is easier by touch;
- the person needs to scan or compare stable structure;
- repeated actions should be fast and predictable; or
- the agent would add latency without reducing effort.

The product should support movement in both directions. A direct selection can
become Chat context; a Chat result can become a directly manipulable object.

## 7. Mixed initiative without interruption

Agentic does not mean maximally proactive. Initiative should be allocated by
expected value, interruption cost, confidence, reversibility, audience, and
time sensitivity.

| Situation | Preferred behavior |
| --- | --- |
| Low value or low confidence | stay quiet; perhaps improve later ranking |
| Useful but not urgent | place value in Home or Places; do not interrupt Chat |
| Helpful while the person is already working | inline suggestion or one compact option |
| Material, reversible, self-owned action | apply only under an existing mandate; receipt and Undo |
| New audience, affected person, spend, provider contact, or weak reversal | stop at a concrete preview or action guard |
| Long-running work | visible status only while active; notify on material state change |

In a group conversation, the bar for unsolicited participation is higher. The
agent should know who addressed it, where a response belongs, whose information
may be used, and whether its contribution adds enough value to justify taking
social space.

## 8. What current research contributes

### 8.1 Interaction alone is insufficient

Wang and Lu's 2025 human-agent framework separates an **Interaction Layer**
from a persistent, inspectable **Process Layer** and executable
**Infrastructure Layer**. It argues that chat histories flatten evolving work
into turns and that agent plans are often hidden and brittle. It also proposes
that the same process may be projected as conversation, timeline, workflow, or
spatial workspace. For Vesper, this supports Chat as one projection over
durable Place, Plan, Occasion, Moment, relationship, and artifact state—not as
the place where all state lives.

This framework is conceptual rather than a validated consumer-app recipe. Its
value here is architectural: preserve a semantic activity layer between the
conversation and the tools.

### 8.2 Context should be structured and manipulable

Li et al.'s 2026 Mixed-Initiative Context work identifies the problem of
flattening context into a chronological sequence and proposes explicit,
structured, manipulable context with both human and AI initiative. That maps
directly to origin objects, scope, audience, target owner, and return contracts.
The app should let a person see or change the operative object when ambiguity
matters; corrections should modify structured context rather than merely add
another contradictory chat message.

The available publication is a recent preprint and should be treated as
directional evidence, not settled consensus.

### 8.3 Language and direct manipulation are complementary

Cao, Jiang, and Xia's CHI 2025 Jelly system uses an evolving task-driven data
model beneath both natural-language changes and direct manipulation. The model
then drives the interface. This supports Vesper's typed owner objects and
bounded artifacts: language can express composition, while stable controls
edit the same underlying state.

Dynamic Prompt Middleware research at CHIWORK 2025 similarly found that
context-specific inline controls increased perceived control and encouraged
exploration, although participants still struggled to predict the effects of
generated controls. Vesper's implication is to use a small, typed operation
vocabulary with visible postconditions—not arbitrary model-invented controls.
Both studies are small and task-specific, so they justify probes and fixtures,
not universal claims.

### 8.4 Oversight is a lifecycle, not one confirmation dialog

Research on human oversight of software agents identifies a priori control,
co-planning, real-time monitoring, and post-hoc review. Magentic-UI likewise
studies co-planning, co-tasking, action guards, and memory as ways to make human
involvement effective without requiring constant supervision. Earlier
human-agent communication research emphasizes common ground about both goals
and process, plus monitoring and correction before irreversible actions.

For Vesper, confirmation is only one tool. The full design must include:

- clear scope and authority before action;
- concise progress for long-running work;
- verified owner readback afterward;
- uncertainty when verification is incomplete; and
- specific correction, Undo, revoke, or recovery paths.

### 8.5 Social initiative needs explicit controls

Houde et al.'s IUI 2025 studies found that groups benefited from an AI agent but
often preferred reactive behavior and disliked dominating, distracting
proactivity. Participants wanted control over when, what, where, and how the
agent contributed. For Vesper, a group room is not merely private Chat with
more recipients. Addressing, contribution threshold, audience, placement,
length, and private-to-group composition require explicit policy.

## 9. What the repository already has

The implementation is substantially more agentic than an “input Chat” framing
suggests.

### Existing substrate to keep

- Concierge's system charter already gives Chat Ask, Point, Bring,
  coordination, correction, action, tool use, streaming, consequence
  preparation, and owner handoff.
- The backend exposes roughly seventy named tool schemas across search,
  account/trip reads, planning, itinerary mutation, booking proposals and
  confirmation, expense operations, group proposals and reactions, location
  sharing, conversation retrieval, and memory administration.
- `TurnPlan` already records the selected tool/effect boundary, agency level,
  privacy mode, context slices, model route, and latency class.
- `ActionEnvelope` binds action type and parameters to authority evidence,
  idempotency, effect, and expected postconditions before execution.
- `ExecutionReceipt` records changed objects, versions, verification,
  uncertainty/failure, and user-visible summaries after execution.
- The shared agent loop buffers consequential prose, runs independent reads in
  parallel, and withholds unverified commit claims.
- Workbench entry references are the beginning of object-aware surface-to-Chat
  entry.
- The in-chat artifact contract already treats artifacts as compact state,
  control, or receipt projections with owner, operation, postcondition,
  uncertainty, and return path.

These are the right bones for a conversational operating layer.

### Current legacy assumptions to remove

1. `TurnIntent` is only `INTAKE | CONVERSATION | PROACTIVE`. It conflates thread
   position with the person's current job.
2. A private no-trip first turn is described in `_tools_select.py` as “an
   intake conversation, not a planning execution surface” and is normally
   restricted to `update_intent` plus a few exceptions.
3. `control_plane_adapter.py` refuses to classify a first-turn request as
   `COMMIT`, even when commit tools and explicit action language are present.
4. Contextual entry exists, but there is no general cross-root contract that
   carries origin object references, selection, audience, and return target.
5. Agency levels omit monitoring/reconciliation as explicit phases, even
   though receipts and postconditions begin to support them.
6. Tool and owner coverage remains heavily trip-shaped. The new Home / Chat /
   Places / Life model needs object-oriented capability retrieval across the
   whole lived-world graph.
7. Four owner-surface artifact journeys remain uncertified; presentation
   readiness is not closed-loop product proof.

The first-turn restriction may have been sensible for a narrow trip-intake
product. It is now architecture-bearing debt. A person's first message can be
“Where is my Saturday plan?”, “compare these,” “invite Maya,” or “track this
flight.” Safety should come from capability selection, contribution grants,
action authority, and postconditions—not from assuming the first turn is
onboarding.

## 10. Recommended architecture changes

### 10.1 Extend, do not replace, the current control plane

Add an agentic turn compilation layer to `TurnPlan` or an adjacent typed
contract:

- `immediate_job`
- `origin_refs`
- `target_owner_refs`
- `contribution_use_grant_ref`
- `agency_ceiling`
- `interaction_phase`
- `return_contract`

Keep `RESPOND | PROPOSE | COMMIT` as a coarse effect/agency boundary if useful,
but do not make it carry activity semantics it cannot express.

### 10.2 Replace first-turn intake with capability-grounded routing

A clean new conversation should begin with the full table-stakes ability to:

- read named or contextually selected objects;
- answer grounded questions;
- privately compose or compare;
- propose relevant owner changes; and
- execute only actions supported by authority policy.

Do not expose every tool. Retrieve the smallest capability set from the
immediate job, origin objects, target owners, privacy, and agency ceiling.

### 10.3 Generalize object entry and return

Evolve `workbench_entry_ref` into a bounded, typed cross-root context envelope.
Every participating surface needs:

- `open_in_chat(object_refs, suggested_verb, return_target)`; and
- an owner refresh/readback path after a verified action.

Chat needs a stable `ResourceRef` vocabulary shared with action receipts so a
later turn can resume the object and a completed turn can return the person to
the right representation.

### 10.4 Keep one source of action truth

Unify or explicitly bridge the current contribution grant, `TurnPlan`, action
envelope, execution receipt, owner object reference, and UI artifact lifecycle.
Do not let mobile callback success, tool return text, or assistant prose become
separate claims about whether an action happened.

### 10.5 Add monitor and reconcile as first-class runtime outcomes

Some jobs do not complete within one request. The runtime needs explicit
continuation state, material-change notification policy, and owner/provider
reconciliation. Chat can show active work while it is active, but Home or the
owning object should carry ongoing consequences without turning Chat into an
activity feed.

## 11. Experience fixtures required before implementation

The next design work should use a compact matrix of complete turns, not a
generic Chat mockup.

| Fixture | Origin | Request | Primary job | Consequence / owner | Critical proof |
| --- | --- | --- | --- | --- | --- |
| A1 | clean Chat | “What should Maya and I do Saturday?” | open + shape | private composition, optional Occasion | first turn is not trapped in intake |
| A2 | clean Chat + ticket | “Use this” | resolve + operate | Trip/Life state as authorized | value before classification; source-bound grant |
| A3 | Home opening | “Make this work for four” | shape + coordinate | Occasion/Plan | origin and return survive Chat |
| A4 | Places selection | “Compare these, then build the easiest route” | compare + operate | Place/Plan route | NL plus direct manipulation share one model |
| A5 | Life artifact | “This wasn't my meal—fix it” | repair | artifact/episode | precise causal repair, no transcript patch |
| A6 | active trip | “We're exhausted; get us home after one more stop” | adapt + act | Plan/route/provider | live engine appears as the same agent |
| A7 | group Chat | “Find something that works for everyone” | coordinate | private context to group-safe proposal | no private leakage; agent does not dominate |
| A8 | personal Chat | “Move dinner and tell the group” | commit + communicate | Plan plus audience system | two independent authority boundaries |
| A9 | Home disruption | “Handle it” under existing mandate | act + reconcile | provider/Plan/Home | visible scope, postcondition, recovery |
| A10 | clean Chat | “Track UA123 and let me know if pickup changes” | monitor | Situation/Home notification | continues outside transcript without feed clutter |
| A11 | Place | “Why did you show me this?” | inspect + explain | none | evidence and selection rationale, no forced mutation |
| A12 | Life episode | “Find the version of this feeling in New York” | make sense + open | Home/Places opening | differentiated graph value, not memory recall |

For every fixture, record:

- context the person should not need to restate;
- contribution-use grant;
- capability set and agency ceiling;
- canonical owner and postcondition;
- prose versus structured artifact choice;
- confirmation, receipt, Undo, or recovery treatment;
- destination of durable value; and
- what the next turn can resume without repetition.

## 12. Product rules to promote if accepted

1. **Vesper is the agent; Chat is its conversational operating surface.**
2. **The input loop is a product loop, not Chat's sole function.**
3. **Every Chat entry may begin from structured app objects and must preserve a
   return path.**
4. **Chat composes across owners but never replaces canonical owner truth.**
5. **Contribution authority and action authority are independent.**
6. **Natural language and direct manipulation operate on the same typed state.**
7. **Simple, frequent, visible actions stay direct; ambiguous, compositional,
   and cross-domain work earns Chat.**
8. **Agentic work includes inspect, compose, propose, commit, monitor, and
   reconcile—not merely answer versus execute.**
9. **First turn is not synonymous with intake.**
10. **A consequential turn ends in canonical readback, honest uncertainty, or
    recovery—not confident prose.**
11. **Proactivity is allocated by value and interruption cost; group
    participation has a higher threshold and explicit audience controls.**
12. **The transcript is not the durable representation of the person's life or
    the agent's work.**

## 13. Recommended next step

Do not begin by adding more tools or redesigning the Chat root in isolation.
First compose the twelve fixtures above as complete cross-surface turn
contracts. Use them to settle:

- the minimal `AgenticTurnPlan` fields;
- the cross-root entry/return envelope;
- the default direct-UI versus Chat allocation;
- the capability retrieval rules that replace first-turn intake;
- monitor/reconcile lifecycle behavior; and
- the exact presentation and owner readback for each consequence class.

Then promote the stable rules into the interaction grammar, Concierge charter,
contribution contract, artifact contract, and backend control-plane plan. That
sequence advances the whole product architecture without pretending the UI is
already designed.

### Execution output — 2026-08-29

The recommended next step is now specified in two bounded working artifacts:

- [Agentic Chat cross-surface fixture
  pack](agentic-chat-cross-surface-fixture-pack-2026-08-29.md) composes all
  twelve turns with context, contribution authority, capabilities, owners,
  postconditions, projection, return, residue, forbidden behavior, and pass
  conditions.
- [Agentic capability and tool cutover
  plan](agentic-capability-and-tool-cutover-plan-2026-08-29.md) audits the
  current 73-tool registry, separates semantic operations from presentation
  and maintenance, maps legacy itinerary handlers behind owner-oriented
  adapters, and defines phased retirement gates.

The main refinement is that itinerary is deprecated as the universal agent and
interaction grammar, while artifacts remain projections rather than replacement
authority. Flexible Plan, Occasion, Commitment, Source, Place, Occurrence,
Outcome, provider, monitor, and receipt owners replace the old organizing
model.

## Sources

- Yun Wang and Yan Lu, *Interaction, Process, Infrastructure: A Unified
  Framework for Human–Agent Collaboration* (2025):
  https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/Human_Agent_Framework.pdf
- Haichang Li et al., *Mixed-Initiative Context: Structuring and Managing
  Context for Human-AI Collaboration* (2026 preprint):
  https://arxiv.org/abs/2604.07121
- Yining Cao, Peiling Jiang, and Haijun Xia, *Generative and Malleable User
  Interfaces with Generative and Evolving Task-Driven Data Model* (CHI 2025):
  https://doi.org/10.1145/3706598.3713285
- Ian Drosos et al., *Dynamic Prompt Middleware: Contextual Prompt Refinement
  Controls for Comprehension Tasks* (CHIWORK 2025):
  https://www.microsoft.com/en-us/research/publication/dynamic-prompt-middleware-contextual-prompt-refinement-controls-for-comprehension-tasks/
- Hussein Mozannar et al., *Magentic-UI: Towards Human-in-the-loop Agentic
  Systems* (2025):
  https://www.microsoft.com/en-us/research/publication/magentic-ui-report/
- Shipi Dhanorkar, Samir Passi, and Mihaela Vorvoreanu, *Human oversight of
  agentic systems in practice*:
  https://www.microsoft.com/en-us/research/publication/human-oversight-of-agentic-systems-in-practice-examining-the-oversight-work-challenges-and-heuristics-of-developers-using-software-agents/
- Gagan Bansal et al., *Challenges in Human-Agent Communication*:
  https://www.microsoft.com/en-us/research/wp-content/uploads/2024/12/HCAI_Agents.pdf
- Stephanie Houde et al., *Controlling AI Agent Participation in Group
  Conversations: A Human-Centered Approach* (IUI 2025):
  https://doi.org/10.1145/3708359.3712089
- Saleema Amershi et al., *Guidelines for Human-AI Interaction*:
  https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- Google PAIR, *Feedback + Control*:
  https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/
