---
doc_type: working
status: active
owner: founder / product / design / architecture / research
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Pressure-tests form-first, chat-only, and hybrid shared-object interaction against five canonical Vesper situations before the product commits to editing surfaces, Plan or Occasion UI, or a generalized agent workflow.
source_of_truth_for: []
depends_on:
  - docs/working/ai-native-effortless-editing-and-composition-research-2026-08-31.md
  - docs/working/whole-product-v1-conformance-workbook-2026-08-29.md
  - docs/working/hci-rebased-home-four-situation-fixtures-2026-08-28.md
  - docs/working/consequence-arbitration-and-cross-surface-blueprints-2026-08-26.md
  - docs/systems/contribution-and-consequence.md
  - docs/systems/artifact-expression-and-composition.md
  - docs/systems/four-root-loop-object-surface.md
  - docs/working/plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md
---

# Form, Chat, or Shared Object? — Comparative Interaction Research

## Question and status

Vesper wants to make creating, reshaping, coordinating, and acting on a day,
night out, journey, social Occasion, or live disruption feel lightweight. The
tempting answer is to declare the product “AI-native” and replace conventional
screens with conversation. That is not enough.

This study asks a narrower and more falsifiable question:

> **For the same Vesper job, what becomes easier or harder when the primary
> interaction is form-first, chat-only, or a hybrid shared object?**

It applies the three paradigms to five canonical situations already grounded
in Vesper's August product work:

1. a solo New York weekend;
2. a Brooklyn dinner with friends;
3. an Italy trip reconstruction and forward projection;
4. a flight disruption; and
5. a post-trip return to New York.

This is an **expert comparative walkthrough**, not a completed participant
study. The interaction sequences and ratings below are design hypotheses
derived from the repository's fixed fixtures and external HCI evidence. They
identify what to prototype and measure; they do not claim observed Vesper user
behavior.

## Executive verdict

The hybrid hypothesis survives, but in a more disciplined form:

> **Vesper should not be a form product with an AI assistant, or a chat product
> with cards. It should keep the thing being shaped visible, allow touch and
> language to address the same semantic state, and introduce one explicit
> checkpoint only where a change crosses a human or real-world boundary.**

The hybrid wins all five situations at the whole-experience level, but **not
every moment inside them**:

- conversation wins when intent is vague, relational, cross-object, or hard to
  encode in fields;
- direct manipulation wins when the referent is visible and the change is
  local, exact, binary, spatial, temporal, or easily reversible;
- structured review wins when exact provider, money, audience, or delivery
  consequences must be verified;
- authored surfaces win when Vesper's job is to give value without requiring a
  request; and
- persistent object views win when current truth must be scanned, re-found,
  shared, or corrected later.

This means the target is not a permanently split `canvas + copilot` UI. In many
moments the best hybrid is **ninety percent visible object and ten percent
language**; in others it is a clean conversation that resolves into a small
native object only when stable state has earned one.

The most important finding is therefore:

> **Hybrid is a state and control architecture, not a visual composition.**

## 1. Research correction: optimize collaboration effort, not speed

Recent comparative evidence sharpens the criterion.

“Delegating or Doing?” compared traditional-only, AI-first, and hybrid
interfaces across sixteen CRUD scenarios with 73 participants. AI assistance
significantly reduced clicks, navigation, and scrolling, but did **not** produce
a significant difference in completion time. Roughly half the variance in
delegation was attributable to individual differences rather than task type
(ICC = .50). The study also did not find that people systematically avoided
delegating nominally higher-risk CRUD operations.
([paper](https://arxiv.org/abs/2608.19551))

This matters for Vesper in four ways:

1. The core benefit may be less interaction labor, not faster stopwatch time.
2. The product should preserve doing and delegating as legitimate postures.
3. Safety cannot depend on people naturally choosing direct manipulation for
   risky actions; the action path must impose the correct boundary.
4. A forced conversational interface may burden people who prefer to act
   directly even when the agent could do the work.

A smaller controlled DIS 2026 study compared GUI-only, LLM-only, and hybrid
customization with 12 participants. Participants used prompts for rapid
high-level specification and discovery, but used the GUI for known operations
and refinement. The authors recommend GUI-first onboarding and
prompt-then-refine workflows; 83% identified GUI-only as most controllable in
that study, despite prompts often being faster. The study's small,
domain-specific sample limits generalization, but the pattern is useful.
([paper](https://doi.org/10.1145/3800645.3812986),
[author manuscript](https://cris.vub.be/ws/portalfiles/portal/272317734/valadez_DIS2026.pdf))

An exploratory 20-person comparison of an industrial dashboard and an
LLM-based conversational interface similarly found that conversation could
reduce interaction effort through direct access, while the dashboard remained
valuable for overview and verification. The domain differs from Vesper, but
the division of labor is consistent.
([paper](https://arxiv.org/abs/2605.31224))

NoTeeline offers a complementary pattern for input. In a within-subjects study
with 12 participants, people wrote 47% less text and completed notes 43.9%
faster when their short, situated “micronotes” were expanded using surrounding
context; the authors report 93.2% factual correctness under their evaluation.
The result should not be generalized from video notes to all lived evidence,
but it supports a useful Vesper direction: **ask the person for the signal only
they can supply, then use authorized context to do the expansion work**.
([paper](https://doi.org/10.1145/3708359.3712086),
[author manuscript](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2025/noteeline.pdf))

Two older HCI principles remain architecture-bearing. Workspace-awareness
research explains why collaborators need perceptible answers to who is here,
what others are doing, what has changed, and how actions affect the shared
workspace; an Occasion object can provide that “feedthrough” without requiring
coordination messages. Mixed-initiative correction guidance likewise favors
rich local editing, Undo, and correction in batches over forcing a person to
restart an AI interaction.
([workspace-awareness framework](https://collablab.northwestern.edu/CollabolabDistro/nucmc/GutwinGreenberg_FrameworkWorkspaceAwareness.pdf),
[HAX correction guidance](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-correction/))

The evaluation target for Vesper is consequently:

```text
not: fewest seconds or fewest screens

but:
human intent expressed once
+ current truth continuously legible
+ low schema and coordination labor
+ proportional verification
+ local repair
+ preserved authorship and consent
```

## 2. The three treatments

The comparison holds the underlying evidence, product capability, authority,
and desired outcome constant. Only the primary interaction paradigm changes.

### 2.1 Form-first

The user operates conventional object screens:

- explicit create flows;
- fields, selectors, sheets, menus, and save actions;
- visible lists, schedules, participants, and statuses;
- separate edit modes; and
- structured confirmation screens for external action.

This is the strongest possible version of forms, not a straw man. It may use
defaults, autocomplete, progressive disclosure, and good mobile design. It
does not receive free natural-language composition as the primary path.

### 2.2 Chat-only

The user creates, modifies, compares, coordinates, and corrects through a
conversation:

- the transcript is the primary surface;
- state is communicated through prose and assistant messages;
- follow-up turns supply context and correction; and
- external actions are proposed and confirmed in Chat.

Cards may summarize a result inside the transcript, but there is no independent
owner surface that can be directly manipulated or reliably re-entered.

### 2.3 Hybrid shared-object

The current object or authored projection remains visible. Touch, language,
voice, and object-native controls address one semantic state and one owner
command path.

- selection supplies nouns and scope;
- language supplies missing motive, ambiguity, relation, or tradeoff;
- Vesper prepares the smallest semantic change;
- the delta appears on the object that changed;
- a private reversible change may apply with Undo; and
- a human, audience, provider, money, or weakly reversible boundary receives
  one exact preview before commitment.

The hybrid treatment does **not** require both modalities to remain on screen.
It requires semantic continuity between them.

## 3. Evaluation rubric

Each walkthrough is evaluated on eight dimensions.

| Dimension | Question |
| --- | --- |
| **Value first** | Does the person receive a useful shape, answer, or state before doing setup or organization work? |
| **Expression burden** | Can the person express human intent without translating it into schema or prompt syntax? |
| **State legibility** | Can the person tell what is proposed, current, settled, open, shared, or externally true? |
| **Correction locality** | Can one mistaken relation or preference be corrected without recreating the whole result? |
| **Boundary clarity** | Is the exact audience, person, provider, spend, or world change clear at commitment? |
| **Refinding** | Can the result be found later without reconstructing a transcript or remembering a path? |
| **Social ease** | Can several people participate without profiles, permission administration, or coordination chatter? |
| **Ownership** | Does the result still feel authored and chosen by the people involved? |

Ratings use an intentionally coarse scale:

- `++` strong fit;
- `+` useful with manageable limitations;
- `0` mixed;
- `-` material friction or ambiguity; and
- `--` paradigm-level failure for the situation.

These are comparative design judgments, not measured scores.

## 4. Fixture A — solo New York weekend

### 4.1 Fixed situation

It is an ordinary week in New York. Saturday 2–8 PM is open. The person has
said “maybe jazz Saturday,” has two relevant saved Places, and has not decided
whether this is a plan at all. Weather changes before the weekend.

The required jobs are:

1. add a possibility without choosing an exact time;
2. make the evening less rushed;
3. compare two venues in the context of the whole afternoon;
4. keep one possibility privately; and
5. remove it without residue.

### 4.2 Form-first walkthrough

1. The person opens `New plan` or a Saturday planner.
2. The interface asks for a title, date, approximate or exact time, and perhaps
   a location before the idea has earned those properties.
3. The person searches for the first venue, adds it, repeats for the second,
   then places both into a schedule or candidate list.
4. To make the evening less rushed, the person manually edits times, transit
   gaps, or item order and checks the effect.
5. Comparison happens in a Place sheet or a separate compare view; the person
   must mentally reconnect each venue to the rest of Saturday.
6. Saving turns the emerging possibility into an explicit maintained object.
7. Removing the chosen venue may leave an empty Plan, draft, or saved shell to
   clean up.

**What works:** exact timing, ordering, and deletion are inspectable; the person
knows what was saved.

**Where it fails:** the form requires a representational decision—“this is a
Plan”—before the human decision exists. “Less rushed” becomes manual schedule
arithmetic. The system receives clean data by making the person do integration
work Vesper is supposed to absorb.

### 4.3 Chat-only walkthrough

1. The person says, “Maybe jazz Saturday.”
2. Vesper asks or infers location, time range, and relevant constraints.
3. It proposes an afternoon and evening in prose or a transcript card.
4. The person says, “Less rushed.”
5. Vesper regenerates the shape and explains the changes.
6. The person asks, “What about the other venue?” then clarifies which venue or
   scrolls back to re-establish the referent.
7. “Keep this” is ambiguous unless the assistant restates exactly what `this`
   means.
8. “Actually remove the jazz part” requires another interpretive turn and may
   produce a new whole version.

**What works:** vague intent can begin immediately; “less rushed” is natural;
the person does not create a schema.

**Where it fails:** current shape, alternatives, and superseded versions compete
inside a linear transcript. Reference and local correction become language
work. The person must verify a regenerated whole instead of one visible delta.

### 4.4 Hybrid shared-object walkthrough

1. Chat accepts “Maybe jazz Saturday” and returns a useful ephemeral Saturday
   shape, not an intake question or durable Plan.
2. The shape appears as a compact sequence or route with jazz deliberately
   loose, plus the current weather assumption.
3. The person touches the evening span and says, “Less rushed.” Selection
   supplies Saturday, time range, existing sequence, and affected entries.
4. Vesper shows one localized change: one venue removed or moved, a larger
   buffer, and the relevant transit consequence.
5. The person selects the two venue candidates; Places supplies an in-context
   comparison rather than requiring their names in a prompt.
6. `Keep Saturday` promotes the accepted shape into private Plan truth. Until
   that action, it remains ephemeral.
7. The person removes the jazz possibility directly. The item disappears with
   `Undo`; if it was the only durable content, the empty shell does not persist.

**Why it wins:** language handles a qualitative goal; touch handles reference,
comparison, and removal; the visible shape handles state. The user never has to
choose an object type or maintain an empty container.

### 4.5 Fixture A ratings

| Treatment | Value first | Expression | State | Repair | Boundary | Refinding | Social | Ownership |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Form-first | `-` | `--` | `+` | `+` | `+` | `+` | n/a | `0` |
| Chat-only | `+` | `+` | `-` | `-` | `0` | `-` | n/a | `+` |
| Hybrid | `++` | `++` | `++` | `++` | `+` | `+` | n/a | `++` |

### 4.6 Modality ruling

- **Chat wins:** initiating from vague desire; qualitative reshaping.
- **Touch wins:** selecting candidates, exact removal, ordering, explicit Keep,
  and Undo.
- **Visible object wins:** judging pace and understanding the whole Saturday.
- **No preview is needed:** for reversible ephemeral or private changes.

## 5. Fixture B — Brooklyn dinner with friends

### 5.1 Fixed situation

The host says, “Dinner at mine Friday. Invite Lena and Reza.” Maya has a private
dietary constraint. Luis contributes a restaurant or dish. One invitee is not
on Vesper. The group eventually needs one shared decision, while private
reasons and independent responses must remain private.

The required jobs are:

1. create the Occasion from ordinary language;
2. invite people without an Occasion-profile flow;
3. incorporate contributions in place;
4. produce a group-safe comparison without exposing private context;
5. settle one decision; and
6. let a person withdraw or correct cleanly.

### 5.2 Form-first walkthrough

1. The host opens `Create event` and enters title, date, time, location,
   visibility, participant list, and perhaps guest permissions.
2. The app asks how participants may contribute before anyone has tried.
3. The host resolves the off-platform invitee through a contact picker or
   manually enters contact information.
4. Maya records a dietary need in a profile, preference screen, poll, or
   message; the host must understand which parts are visible.
5. Luis adds a suggestion through an `Add option` form.
6. The group opens a poll or comparison screen and votes.
7. The host closes the poll and saves the winning state.
8. Corrections require editing a participant, response, option, or permission
   field in the right management screen.

**What works:** shared state and explicit fields can be scanned; a conventional
poll can make a narrow decision legible.

**Where it fails:** the Occasion becomes a miniature collaboration product.
Participation requires setup, classification, permissions, and unfamiliar
interaction conventions. The host carries administrative burden. A dinner
starts to feel like running a project.

### 5.3 Chat-only walkthrough

1. The host expresses the dinner naturally in Chat.
2. Vesper asks for the missing time only if it is materially required.
3. It proposes invitees and asks for confirmation before contacting them.
4. Contributions arrive as messages: “I'll bring tiramisu,” “after nine,” or a
   photograph.
5. Vesper summarizes current state in the room conversation.
6. It creates a comparison in prose, taking account of authorized private
   constraints without exposing them.
7. Each person replies in the transcript; Vesper declares or proposes a result.
8. Later participants must distinguish current truth from old suggestions,
   jokes, declined options, and superseded summaries.

**What works:** creation and contribution feel ordinary; people do not fill
profiles or learn artifact types.

**Where it fails:** conversation is a good contribution channel but a poor
shared constitution. Attribution, current commitments, participation windows,
one open decision, and the settled result become fragile transcript knowledge.
Correction may require an assistant restatement everyone trusts.

### 5.4 Hybrid shared-object walkthrough

1. The host says, “Dinner at mine Friday. Invite Lena and Reza.”
2. Vesper resolves known home Place and people, asks only for a materially
   missing time, and shows one audience preview naming the host, invitees,
   visible place precision, and message.
3. Confirmation creates the Occasion and invitations. The Occasion opens as a
   small shared object—not a dashboard—with settled facts, participation, one
   current open question, and ordinary conversation.
4. “I'll bring tiramisu” becomes an attributed Commitment with `Added · Undo`.
   “After nine” becomes an attributed participation window. Messages without a
   coordination consequence remain messages.
5. Luis's suggestion appears inside the active decision, not in a separate
   artifact feed.
6. Vesper prepares a group-safe comparison. It may say that one option works
   for all known constraints, but it does not disclose Maya's private reason.
7. People respond independently. The shared object shows responses and the
   authorized result; no synthetic group preference is inferred.
8. A withdrawal or correction updates the attributed lane and recomputes only
   dependent shared state. Other people's contributions remain intact.

**Why it wins:** Chat preserves effortless human contribution, while the
Occasion provides common ground. Private context changes the safe option space
without becoming shared explanation. One consequential audience crossing is
explicit; ordinary in-room contribution is reversible and lightweight.

### 5.5 Fixture B ratings

| Treatment | Value first | Expression | State | Repair | Boundary | Refinding | Social | Ownership |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Form-first | `0` | `--` | `+` | `+` | `+` | `+` | `-` | `-` |
| Chat-only | `+` | `++` | `-` | `0` | `-` | `-` | `0` | `+` |
| Hybrid | `++` | `++` | `++` | `++` | `++` | `++` | `++` | `++` |

### 5.6 Modality ruling

- **Chat wins:** creation, contribution, exceptions, and private nuance.
- **Touch wins:** selecting invitees, exact responses, withdrawing, opening the
  current decision, and Undo.
- **Structured object wins:** common ground, attribution, settled/open state,
  and later refinding.
- **One preview is required:** at the invitation or changed shared consequence,
  not for every reversible contribution.

## 6. Fixture C — Italy reconstruction and forward projection

### 6.1 Fixed situation

Vesper has flights, trains, ferry tickets, photographs, visited Places,
uncertain occurrences, restaurant and hotel evidence, and attention expressed
in Chat. The person wants a truthful day reconstruction, correction of one
false occurrence, and a useful opening from a past Place into present New York.

The required jobs are:

1. reconstruct a day without building an itinerary;
2. correct one false occurrence;
3. turn a past Place into a substantive New York opening;
4. reshape the composition without mutating evidence; and
5. save or share one exact expression.

### 6.2 Form-first walkthrough

1. The person enters a trip or timeline editor.
2. Tickets and photographs appear as unclassified imports or candidate events.
3. The person assigns dates, Places, categories, transport modes, confidence,
   and perhaps trip membership.
4. The app constructs an itinerary-like day.
5. To correct the ferry, the person finds the event and edits status, relation,
   or deletion behavior—without necessarily knowing whether the ticket Source
   should remain.
6. To create a New York opening, the person leaves the record, searches for an
   analogue, and makes a separate saved list or plan.
7. Sharing means choosing a report, album, trip, or export template.

**What works:** a timeline and map can make evidence inspectable; exact event
editing can be local if the data model is exposed well.

**Where it fails:** the person becomes archivist and ontology maintainer.
Scheduled transport is easily mistaken for lived occurrence. The past record
and future possibility become disconnected products. A rich life episode is
forced into itinerary structure.

### 6.3 Chat-only walkthrough

1. The person asks, “What did we do that day in Amalfi?”
2. Vesper synthesizes a narrative from documents, photos, time, and Places.
3. The person says, “We bought that ferry ticket but never took it.”
4. Vesper acknowledges the correction and regenerates the account.
5. The person asks for a New York connection or present possibility.
6. Vesper offers an explanation and perhaps a route in prose.
7. The person requests a shorter version, map, or shareable version.
8. Later, there is no stable guarantee that the factual correction reached the
   owning occurrence rather than only the conversational answer.

**What works:** correction and sensemaking can be expressed naturally; no one
must understand the internal distinction between Source and Occurrence.

**Where it fails:** evidence, inference, correction, and generated expression
are visually collapsed. The transcript does not prove what historical truth
changed. Re-finding the day, comparing evidence, or sharing one exact version
requires reconstructing conversational state.

### 6.4 Hybrid shared-object walkthrough

1. Life opens the Italy episode through an evidence-backed day composition:
   temporal sequence, spatial path, and provenance marks—not a complete
   itinerary or an invitation to organize it.
2. Vesper labels scheduled, inferred, and verified occurrence states
   differently. The person receives the reconstruction before any request to
   classify material.
3. The person selects the ferry occurrence and says, “Bought the ticket; we
   didn't take it.”
4. Vesper retains the ticket Source, corrects the Occurrence relation, and
   shows one local before/after receipt. Dependent route and day projections
   recompile.
5. The person selects the Sorrento cliff Place relationship and asks, “Open
   this into New York.” Places presents one mechanism-based local analogue or
   contrast with practical current conditions—not a repetition of the
   person's observation or a personality claim.
6. The person can change the expression—`Map`, `Day`, `Evidence`—without
   changing canonical history. Presentation and truth remain separate.
7. `Share this day view` previews the exact selected expression and audience;
   the private episode does not become broadly visible.

**Why it wins:** the visible episode makes evidence and historical state
inspectable; language handles the human correction and cross-life question;
the system repairs the smallest causal relation; expression can change without
rewriting truth.

### 6.5 Fixture C ratings

| Treatment | Value first | Expression | State | Repair | Boundary | Refinding | Social | Ownership |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Form-first | `--` | `--` | `+` | `+` | `+` | `+` | `0` | `-` |
| Chat-only | `+` | `++` | `--` | `-` | `0` | `-` | `0` | `+` |
| Hybrid | `++` | `++` | `++` | `++` | `++` | `++` | `+` | `++` |

### 6.6 Modality ruling

- **Authored surface wins:** the initial evidence-backed reconstruction.
- **Chat wins:** explaining a false relation and asking a cross-life question.
- **Touch wins:** identifying the exact occurrence, switching lenses, choosing
  the shareable expression, and opening provenance.
- **Structured review wins:** exact audience preview for sharing.

## 7. Fixture D — flight disruption

### 7.1 Fixed situation

A confirmed flight is delayed. A hotel, dinner, companion, pickup, and provider
alternatives are connected. The person cares about preserving dinner and
reducing walking. Some changes are private planning; others would contact a
provider, spend money, change a shared commitment, or notify another person.

The required jobs are:

1. prepare a coherent adaptation;
2. let the person change one preference;
3. distinguish private plan edits from provider action;
4. cross the external boundary once; and
5. recover usefully from partial failure.

### 7.2 Form-first walkthrough

1. A disruption center lists the delayed flight and provider alternatives.
2. The person opens each affected reservation or Plan item separately.
3. They compare new arrival, ground transport, dinner reservation, pickup, and
   hotel implications across tabs or screens.
4. They edit the proposed schedule, select a flight, update dinner, and choose
   whom to notify.
5. Each provider produces its own confirmation flow.
6. If one action fails after another succeeds, the person manually reconstructs
   the remaining viable state.

**What works:** provider-specific facts, prices, exact times, and commitments
are explicit. A conventional confirmation page is appropriate at the final
transaction boundary.

**Where it fails:** forms expose service boundaries instead of preserving the
human goal. The person coordinates the microservices. “Protect dinner, reduce
walking” is not a field; it becomes manual multi-screen optimization.

### 7.3 Chat-only walkthrough

1. Vesper announces the delay and proposes a new sequence in conversation.
2. The person says, “Keep dinner if possible, and less walking.”
3. Vesper revises its recommendation and describes the actions it could take.
4. The person says, “Do it.”
5. Chat narrates provider calls and messages.
6. One provider succeeds and another fails; Vesper describes partial state and
   next options.

**What works:** the person can express the integrated human objective once;
Vesper can coordinate service logic behind the scenes.

**Where it fails:** `Do it` is dangerously underspecified. A plausible plan can
look trustworthy while hiding the exact affected owners, provider truth,
audience, and irreversible steps. Progress messages are not the same as a
stable operational instrument. Partial failure is hard to scan in a transcript.

The concern is empirical, not theoretical. A 248-person CHI 2025 study of
plan-then-execute daily assistants found that high-quality plans plus necessary
human involvement could improve outcomes, but plausible-looking plans could
also be mistrusted or miscalibrated; involvement alone did not reliably
calibrate trust. The checkpoint must expose the real consequence, not merely a
fluent plan.
([paper](https://doi.org/10.1145/3706598.3713218),
[preprint](https://arxiv.org/abs/2502.01390))

### 7.4 Hybrid shared-object walkthrough

1. Home or the active Occasion elevates one disruption instrument because a
   verified change materially affects the person.
2. The instrument shows current provider truth, affected commitments, one
   prepared adaptation, and what remains protected. No action has occurred.
3. The person touches the walking-heavy leg and says, “Protect dinner; less
   walking.” Vesper recomputes the smallest coherent alternative.
4. Private prospective Plan changes can update as a reversible proposal. The
   provider reservation, shared dinner state, money, and notifications remain
   visibly uncommitted.
5. One review names the exact external consequences: chosen provider option,
   cost, dinner change, companion notification, affected people, and recovery
   limits.
6. One confirmation commits the authorized bundle. The operational instrument
   shows verified, pending, failed, and not-attempted state per owner.
7. If the flight change succeeds but the restaurant change fails, Vesper does
   not claim “done.” It offers the remaining safe recovery from the actual new
   state; successful actions remain visible and are not replayed.

**Why it wins:** language preserves the person's integrated objective; the
instrument preserves operational truth; structured review appears only at the
boundary where exactness matters. The user does not manage services, but can
still see which services changed.

### 7.5 Fixture D ratings

| Treatment | Value first | Expression | State | Repair | Boundary | Refinding | Social | Ownership |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Form-first | `+` | `-` | `++` | `+` | `++` | `+` | `0` | `0` |
| Chat-only | `++` | `+` | `-` | `-` | `--` | `-` | `-` | `0` |
| Hybrid | `++` | `++` | `++` | `++` | `++` | `++` | `+` | `+` |

### 7.6 Modality ruling

- **Chat wins:** integrated priorities, exceptions, and preference changes.
- **Direct control wins:** selecting the exact alternative, inspecting costs,
  stopping, and taking over.
- **Operational instrument wins:** current provider and per-owner state.
- **Conventional structured review wins:** the final external transaction.

Research on 400 real-user web-agent trajectories found four recurring human
postures—hands-off supervision, hands-on oversight, collaborative task-solving,
and full takeover—and that intervention often served error correction,
preference refinement, or assistive takeover. Vesper should therefore preserve
a path to inspect, intervene, or take over without treating a single autonomy
style as the normal user.
([paper](https://arxiv.org/abs/2602.17588))

## 8. Fixture E — post-trip return to New York

### 8.1 Fixed situation

The person has just returned from Nice, Sorrento, Amalfi, and Rome. Vesper has
tickets, routes, photographs, Places, restaurants, observations, and
permissioned social context. The coming New York weekend is open and a
Brooklyn dinner is already moving. There is no unresolved travel emergency.

The required jobs are:

1. Home must provide value without asking for reflection;
2. the recent trip must not monopolize the present;
3. a past element may open a substantive current possibility;
4. “make this work with Maya” must preserve origin context; and
5. a private possibility becomes social only at explicit intent.

### 8.2 Form-first walkthrough

1. Home offers a completed-trip summary, memory setup, saved list, or prompt to
   organize photos and tickets.
2. The person chooses categories, highlights, favorites, or what to remember.
3. To plan the weekend, they open a separate planning product or recommendation
   feed.
4. To involve Maya, they create an event or share a list.

**What works:** facts can be summarized; archival tasks can be made explicit.

**Where it fails:** the app returns from a data-rich trip by assigning more
work. Past and future are different modules. The product extracts reflection
instead of delivering compounded value from attention already given.

### 8.3 Chat-only walkthrough

1. Chat opens with “What do you want to remember?” or waits for the person to
   ask what to do this weekend.
2. If the person asks, Vesper can synthesize the trip and propose New York
   possibilities.
3. The person says, “Make this work with Maya.”
4. Vesper asks what `this` refers to or uses conversational recency.
5. It prepares a social proposal and asks permission to send.

**What works:** a motivated person can ask an open-ended question and receive
cross-life synthesis.

**Where it fails:** the person must know that value exists and formulate the
request. The trip evidence compounds only on demand. Current New York, social
context, practical state, and retrospective insight become prose volume in one
thread. Home has abdicated its output role.

### 8.4 Hybrid shared-object walkthrough

1. Home opens with present New York: one genuinely workable coming-weekend
   possibility, current Brooklyn dinner state, and perhaps one compact
   evidence-led transfer from the trip if it adds something new.
2. A factual trip unit may show a novel comparison, mechanism, route pattern,
   social juxtaposition, or practical continuation. It does not report artifact
   counts, repeat the person's own Colosseum connection, diagnose personality,
   or ask what should be remembered.
3. Every unit is complete on view. Ignoring it creates no task, preference, or
   unfinished thread.
4. The person selects the current opening and says, “Make this work with Maya.”
   The selected object supplies schedule, Place, evidence, and return context;
   Chat supplies the relational instruction.
5. Vesper prepares a private social shape first. Naming Maya does not contact
   her.
6. The person explicitly chooses `Ask Maya`; one preview shows the proposal and
   audience. Confirmation creates or updates the appropriate Occasion.
7. Life keeps only the underlying Sources, factual episode, accepted Plan or
   Occasion, and any composition that earns continuity. Ignored Home units do
   not become archive residue.

**Why it wins:** Home fulfills the product promise before asking for input;
Chat becomes a low-friction input and reshaping layer; Life retains earned
continuity; the social boundary remains explicit. The trip becomes a resource
for present life rather than the app's new mode.

### 8.5 Fixture E ratings

| Treatment | Value first | Expression | State | Repair | Boundary | Refinding | Social | Ownership |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Form-first | `--` | `--` | `0` | `+` | `+` | `+` | `-` | `--` |
| Chat-only | `+` | `+` | `-` | `0` | `0` | `-` | `0` | `+` |
| Hybrid | `++` | `++` | `++` | `++` | `++` | `++` | `++` | `++` |

### 8.6 Modality ruling

- **Authored Home wins:** unsolicited, complete-on-view output value.
- **Selection plus Chat wins:** turning one visible opening into a relational
  or cross-object shape.
- **Structured preview wins:** explicit social proposal.
- **Life wins:** factual depth, provenance, and later refinding.

## 9. Cross-fixture comparison

### 9.1 Aggregate pattern

| Situation | Form-first strength | Chat-only strength | Hybrid decisive advantage |
| --- | --- | --- | --- |
| Solo weekend | exact local manipulation | vague creation and qualitative reshaping | qualitative intent operates on a visible, ephemeral shape |
| Brooklyn dinner | scannable participant fields and a narrow poll | ordinary creation and contribution | conversation feeds attributed common ground without event administration |
| Italy reconstruction | inspectable timeline and map | natural correction and synthesis | evidence, history, expression, and forward opening stay distinct but connected |
| Flight disruption | exact provider review | integrated human objective | language composes; instrument verifies; one boundary commits |
| Return to New York | factual archive tooling | on-demand synthesis | Home gives compounded value, Chat reshapes, Life preserves earned continuity |

### 9.2 Why form-first loses the whole experience

Forms are not intrinsically bad. They lose when they force the person to make
representational commitments earlier than the human situation requires.

Across the fixtures they repeatedly introduce four kinds of product debt:

1. **Container debt** — choosing Plan, trip, Occasion, list, memory, or task.
2. **Precision debt** — specifying exact time, category, rank, or audience
   before the possibility requires it.
3. **Integration debt** — reconciling weather, people, Place, transport,
   schedule, and providers manually.
4. **Maintenance debt** — cleaning empty shells, stale options, participant
   fields, and superseded state.

Forms remain justified where every displayed field maps directly to an
imminent consequence: a provider transaction, exact audience, payment,
delivery, or a narrow shared decision. They should appear **at that boundary**,
not define the product's default ontology.

### 9.3 Why chat-only loses the whole experience

Conversation removes schema work but introduces five other burdens:

1. **Prompt burden** — knowing what is possible and how to ask.
2. **Reference burden** — restating the visible thing or disambiguating `this`.
3. **State burden** — separating current truth from proposals and old versions.
4. **Verification burden** — rereading a regenerated whole to find the change.
5. **Refinding burden** — reconstructing a durable object from conversation.

Chat is a particularly poor resting place for plural truth and partial external
execution. A fluent transcript can conceal whether a result is proposed,
accepted, provider-confirmed, shared, failed, or merely inferred.

### 9.4 Why hybrid can also fail

Hybrid is not automatically better. A careless implementation creates a
heavier super-interface:

- a full conventional UI plus an always-visible Chat panel;
- duplicate ways to change state with different semantics;
- generated cards that do not share an owner with direct controls;
- unclear precedence between typed commands and manual edits;
- prompts that operate on hidden or stale selection;
- conversational actions whose effects appear elsewhere without a return;
- excessive AI suggestion chrome around simple direct tasks; and
- a user forced to verify both the agent and the interface.

The hybrid only wins if both modalities compile to the same typed semantic
command and the changed owner becomes the visible readback.

## 10. The minimum reusable interaction kernel

The research does not justify a new menu of product verbs. It supports a small
mechanical kernel beneath the existing product grammar:

```text
FOCUS
  current root + visible owner/projection + selection + moment + authority

EXPRESS
  direct action, brief language, voice, or ordinary contribution

RESOLVE
  infer referent + semantic intent + smallest affected owner command

ACT
  private reversible: apply
  material boundary: preview once -> commit

REFLECT
  show changed state on its owner + compact receipt + return context

REPAIR OR LEAVE
  Undo, Correct, Stop, take over, or simply leave without setup debt
```

The person should experience this more simply:

> **Point at the thing. Say only what is missing. See what changed. Confirm
> only if another person or the world will be affected. Undo or leave.**

### 10.1 Small direct-control vocabulary

The visible object needs only a restrained set of dependable direct actions:

- select or focus;
- open depth;
- compare selected things;
- add or keep;
- move or reorder where spatial/temporal placement is meaningful;
- remove;
- choose or respond;
- inspect source or consequence;
- Undo; and
- Stop or take over during execution.

These are not exposed uniformly on every object. They appear only where the
current semantic type supports them.

### 10.2 Language's proper scope

Language should carry what a direct control cannot efficiently express:

- “less rushed”;
- “keep dinner if possible”;
- “something that works with Maya”;
- “we bought it but did not take it”;
- “compare these in the context of Saturday”;
- “use the trip as context, but don't make this about the trip”; or
- “same shape, less walking.”

Language is not required to restate visible dates, people, Places, selected
items, object identity, or current state.

### 10.3 Structured review's proper scope

A conventional structured review is the correct interface when it answers:

- exactly who will receive this;
- exactly what a provider will change;
- exact cost and refundability;
- which shared commitment changes;
- what becomes public;
- what cannot be undone; or
- which parts of a multi-owner action are verified, pending, failed, or not
  attempted.

This is not a retreat from AI-native design. It is where stable legibility has
more value than conversational flexibility.

## 11. Architecture implications

The benchmark supports a small set of architecture-bearing requirements.

### 11.1 One command path

Chat, voice, direct manipulation, and object-native controls should resolve to
the same typed owner command. Otherwise correction, authorization, receipts,
and cross-surface readback will drift.

```yaml
resolved_interaction:
  origin_root: home | chat | places | life | owner
  visible_owner: null
  selection: []
  moment: null
  expression: null
  semantic_intent: null
  affected_owner_commands: []
  authority_basis: null
  boundary_class: private_reversible | shared | audience | provider | spend | public
  return_envelope: null
```

This is an internal envelope, not a new universal persisted object.

### 11.2 Separate truth, proposal, expression, and execution

The five fixtures require four distinct planes:

- **canonical truth** — Sources, Occurrences, Commitments, Place and provider
  state, people, and accepted Occasion truth;
- **proposal** — an ephemeral candidate shape or pending change;
- **expression** — the map, sequence, comparison, article, instrument, or other
  bounded rendering; and
- **execution** — provider, delivery, monitor, spend, and reconciliation state.

A generated expression may change without changing truth. A private proposal
may change without contacting anyone. A provider action may fail after a Plan
projection has changed. These distinctions must survive every surface.

### 11.3 Selection is first-class context, not hidden UI state

Selection must travel with:

- origin owner and revision;
- selected identities and relations;
- active lens or expression;
- current Moment;
- audience and authority scope;
- unresolved question; and
- return destination.

This is what lets “this,” “these two,” “later,” and “with Maya” remain
lightweight without becoming unsafe.

### 11.4 Delta and receipt must be semantic

The result should report what changed in the human object, not merely what API
call succeeded:

```yaml
semantic_delta:
  owner: null
  owner_revision: null
  changed_relations: []
  affected_people: []
  audience_delta: null
  world_effect: null
  verification: proposed | applied | pending | verified | failed | partial
  undo_or_repair: null
```

### 11.5 Do not infer safety from modality

Because users do not consistently reserve delegation for low-risk tasks, both
touch and language must route through the same authority and consequence
classification. “Do it,” tapping a provider option, and choosing a suggested
action cannot bypass the exact external boundary.

## 12. Prototype recommendations

### 12.1 Prototype three end-to-end fixtures first

For interaction learning—not product thesis proof—the highest-yield prototype
set is:

1. **Solo New York weekend** — tests vague creation, visible shaping,
   comparison, ephemeral-to-durable promotion, and no-residue exit.
2. **Brooklyn dinner** — tests ordinary contribution, common ground, private
   constraints, plural authorship, invitation boundary, and correction.
3. **Flight disruption** — tests integrated intent, consequence-scaled review,
   multi-owner execution, partial failure, and takeover.

These three expose most of the interaction kernel. Italy reconstruction and
post-return Home should then verify that the same architecture supports
authored value, truth correction, expression, and longitudinal continuity
rather than only planning and operations.

This is a **research sequence**, not permission to narrow Vesper's product
architecture to three loops.

### 12.2 Build all three treatments honestly

Each fixture prototype should hold evidence and capability constant. Do not
make the form treatment intentionally bureaucratic or the Chat treatment
intentionally vague.

- Form-first gets sensible defaults, autocomplete, progressive disclosure,
  and excellent native controls.
- Chat-only gets strong grounding, concise answers, and useful transcript
  cards.
- Hybrid gets no bonus for simply adding both interfaces; it must prove lower
  total collaboration cost.

### 12.3 Measure more than completion time

For each task capture:

- time to first useful state;
- words, taps, screens, scroll distance, and clarification turns;
- number of times visible context must be restated;
- number of representational choices made only for the system;
- whether the person can predict the exact consequence before commitment;
- whether the person can identify the changed relation afterward;
- local repair success without whole-result regeneration;
- current-state accuracy after five minutes and one day;
- state-refinding path length;
- unnecessary confirmations and unnecessary questions;
- willingness to switch between direct action and delegation;
- perceived effort, control, ownership, and administrative burden;
- social messages required outside the product; and
- whether a person can leave without completing setup or cleaning residue.

### 12.4 Counterbalance and test modality preference

The study should counterbalance treatment order. GUI-first exposure may help
people recognize later agent errors, while individual delegation preference is
large enough to confound aggregate results. Capture a person's preferred
collaboration posture and test whether the interaction model lets them move
between:

- hands-off supervision;
- hands-on oversight;
- collaborative shaping; and
- full takeover.

The product should not reward only the person who enjoys prompting.

The executable Claude Code + Claude Design MCP handoff for this comparative
prototype is:
`docs/working/claude-code-design-mcp-interaction-kernel-lab-handoff-2026-08-31.md`.
It creates a separate interaction lab and deliberately leaves the semantically
closed Home/Places design project unchanged.

## 13. Decisions this research supports

### Strongly supported

1. The visible owner or authored projection is the primary surface whenever
   durable, shared, spatial, temporal, or operational state matters.
2. Chat is a cross-object expression and coordination layer, not the only place
   current state lives.
3. Selection and origin context should travel into Chat and back.
4. Direct manipulation and language must modify the same typed state.
5. Private reversible changes receive local readback and Undo, not ritual
   preview.
6. Shared, audience, provider, spend, public, and weakly reversible changes
   receive one exact boundary review.
7. Form-like UI is retained at exact consequence and verification boundaries.
8. Home's default is authored output value; it should not become a prompt or
   editing surface merely because Chat is powerful.
9. Occasion common ground is a compact shared object fed by ordinary language,
   not a profile, project, or permission-management product.
10. Presentation can be dynamically composed, but truth and controls retain
    stable semantic owners.

### Not yet supported

- a universal AI edit mode;
- an always-visible assistant on every surface;
- arbitrary generated mobile controls;
- whole-object regeneration as ordinary editing;
- automatic promotion from possibility to Plan or Occasion;
- a generic event builder or shared workspace;
- hidden provider execution behind “Do it”;
- one autonomy preference for every action family;
- deletion of all conventional controls; or
- a production architecture rewrite before comparative prototype evidence.

## 14. Open questions the prototype must answer

1. How does a person know what can be said about a selected object without a
   permanent action menu or capability tour?
2. How long does selection remain active when Chat opens, the app backgrounds,
   or another root intervenes?
3. When should a qualitative request apply immediately versus first appear as
   an ephemeral delta?
4. How should several simultaneous deltas be summarized without becoming a
   diff viewer?
5. When does an ephemeral shape earn a stable Plan or Occasion identity?
6. Can an Occasion remain legible with one dominant unsettled question and no
   management dashboard as participation grows?
7. What is the smallest useful visual state for partial external execution?
8. Can a person take over one provider action without taking over the entire
   adaptation?
9. Does direct manipulation actually preserve authorship, or can AI-generated
   starting shapes still make the person feel like an editor of Vesper's work?
10. Does Home-to-Chat-to-owner return feel continuous enough that the four
    roots read as one product?

The authorship question deserves explicit measurement. A CHI 2026 experiment
found model-led co-creation improved idea quality while reducing idea diversity
and perceived ownership. Vesper should let the model contribute substance
without turning the person's life into material they merely approve.
([paper](https://arxiv.org/abs/2510.23324))

## Closing judgment

The comparative result is not “hybrid is best” in the generic sense. It is more
specific:

> **Use AI to absorb translation and integration; use language for the human
> part of intent; use direct manipulation for the obvious local part; use a
> visible owner for current truth; and use structured review only where another
> person or the world will actually change.**

That division makes Vesper lightweight without making it vague. It allows the
app to be broad in capability while remaining narrow in interaction grammar.
The person need not become a database operator, prompt engineer, event manager,
or agent supervisor. They can point, express the missing intention, see the
consequence in place, and continue living.

## Sources

- Dizon et al., [“Delegating or Doing? Understanding User Behavior in Hybrid
  Human-Agent Interfaces”](https://arxiv.org/abs/2608.19551), 2026.
- Valadez, Avina, and Signer, [“A Hybrid GUI-LLM Interface Paradigm for 3D
  Scene Customisation”](https://doi.org/10.1145/3800645.3812986), DIS 2026;
  [author manuscript](https://cris.vub.be/ws/portalfiles/portal/272317734/valadez_DIS2026.pdf).
- Figliè et al., [“Comparing LLM-Based Conversational and Graphical Interfaces
  for Industrial Decision Tasks”](https://arxiv.org/abs/2605.31224), 2026.
- He, Demartini, and Gadiraju, [“Plan-Then-Execute”](https://doi.org/10.1145/3706598.3713218),
  CHI 2025; [preprint](https://arxiv.org/abs/2502.01390).
- Huq et al., [“Modeling Distinct Human Interaction in Web
  Agents”](https://arxiv.org/abs/2602.17588), 2026.
- Vaithilingam et al., [“Generative and Malleable User Interfaces with
  Generative and Evolving Task-Driven Data Model”](https://doi.org/10.1145/3706598.3713285),
  CHI 2025.
- Wang et al., [“Data Formulator 2”](https://arxiv.org/abs/2408.16119), 2024.
- Lupp et al., [“Exploring Mobile Touch Interaction with Large Language
  Models”](https://doi.org/10.1145/3706598.3713554), CHI 2025.
- Su et al., [“Natural Language Interfaces with Fine-Grained User
  Interaction”](https://www.microsoft.com/en-us/research/publication/natural-language-interfaces-fine-grained-user-interaction-case-study-web-apis/),
  SIGIR 2018.
- Horvitz, [“Principles of Mixed-Initiative User
  Interfaces”](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf),
  CHI 1999.
- Shipman and Marshall, [“Formality Considered
  Harmful”](https://people.engr.tamu.edu/shipman/viki/papers/tochi/tochi.html)
  and [“Incremental
  Formalization”](https://people.engr.tamu.edu/shipman/hos/hos-short.html).
- Maier, Schneider, and Feuerriegel, [“Partnering with Generative
  AI”](https://arxiv.org/abs/2510.23324), CHI 2026.
- Huq et al., [“NoTeeline: Supporting Real-Time, Personalized Notetaking with
  LLM-Enhanced Micronotes”](https://doi.org/10.1145/3708359.3712086), IUI
  2025; [author manuscript](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2025/noteeline.pdf).
- Gutwin and Greenberg, [“A Descriptive Framework of Workspace Awareness for
  Real-Time Groupware”](https://collablab.northwestern.edu/CollabolabDistro/nucmc/GutwinGreenberg_FrameworkWorkspaceAwareness.pdf).
- Microsoft HAX Toolkit, [“Support efficient
  correction”](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-correction/).
