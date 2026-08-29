---
doc_type: working
status: active
owner: founder / product / architecture / AI systems / mobile
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Converts the accepted Chat-as-agentic-interface direction into twelve comparable cross-surface turn contracts that can generate context, capability, authority, artifact, owner, and return requirements.
promotes_to: null
supersedes: []
related:
  - ../decisions/2026-08-29-close-whole-product-v1-wave-0.md
  - chat-as-agentic-interaction-layer-research-2026-08-29.md
  - ../systems/contribution-and-consequence.md
  - chat-artifact-closed-loop-optimization-plan-2026-08-16.md
  - canonical-artifact-projection-and-visual-system-execution-plan-2026-08-23.md
  - life-object-and-lens-fixture-pack-2026-08-29.md
  - ../../travel-agent/docs/product/Product Model.md
  - ../../travel-agent/docs/product/Vesper Expression, Medium, and Projection Canon.md
  - ../../travel-agent/docs/architecture/plan-occasion-lifecycle-contract-2026-08-22.md
---

# Agentic Chat cross-surface fixture pack

## Question or outcome

What does one complete agentic Vesper experience look like when Chat can begin
from any root, accept new contribution, operate across canonical owners, and
return a verified consequence without making the transcript or an artifact the
source of truth?

This pack makes twelve turns comparable. It is a product and architecture
probe, not a visual specification and not authorization to implement a generic
agent framework.

## Executive decision

The fixtures support one product role:

> **Vesper is the agent. Chat is its conversational operating surface. Home,
> Places, Life, Plan, and Occasion expose durable or current projections of the
> world the agent can interpret and operate.**

The input loop and agentic action loop are one compound loop:

```text
contribute or select context
  -> receive immediate value
  -> inspect, compose, propose, act, monitor, or repair
  -> reconcile through the canonical owner
  -> project the consequence across relevant surfaces
  -> retain only the authorized residue
  -> improve a later turn, opening, or silence decision
```

The itinerary is not the fixture grammar. A multi-day Trip may still use the
existing itinerary writer during migration, but the fixtures reason in Plan,
Occasion, Commitment, Place, Source, Moment, Occurrence, Outcome, provider
state, and receipt. An artifact or instrument projects those authorities; it
does not replace them.

## 1. Shared turn contract

Every fixture must resolve the following internal fields even when none are
shown as form fields:

```yaml
agentic_turn:
  origin:
    surface: chat | home | places | life | plan | occasion | push
    object_refs: []
    selection: null
    return_target: null
  immediate_job: understand | compare | explore | shape | coordinate |
    operate | monitor | repair
  contribution:
    gesture: ask | point | bring | keep | share | decide | act | correct
    use:
      mode: none | current_job | named_purpose
      purposes: []
      consumers: []
    retention:
      source: none | transient | reference_only | retained_private |
        retained_shared_projection
      claims: none | turn_candidate | session_working | scoped_governed
      projections: none | cached_recomputable | published_snapshot
    inference:
      mode: none | current_job | source_bound | admitted_learning
      semantic_scope: null
      target: none | world | product | situation | person | relationship
      level: L0 | L1 | L2 | L3 | L4
    audience:
      mode: private | named_people | occasion | public
      recipient_refs: []
      occasion_ref: null
      affected_principal_refs: []
      may_name: false
      may_contact: false
      may_show: false
    action:
      mode: advise | prepare | propose | commit | mandate
      owner_ref: null
      authority_source: null
      mandate_ref: null
      protected_consequence_ref: null
      threshold: null
      delivery_destination: null
      expires_at: null
  context_scope:
    moment_ref: null
    resource_refs: []
    participant_scope: []
    excluded_context: []
  operation:
    phase: inspect | compose | propose | commit | monitor | reconcile
    capability_ids: []
    target_owner_refs: []
    expected_postconditions: []
  response:
    prose_job: null
    primary_projection: none | artifact | instrument | direct_state
    lead_medium: evidence | sequence | comparison | spatial | prose | instrument
    owner_destination: null
    return_behavior: stay | update_origin | open_owner | continue_monitoring
  residue:
    admitted_refs: []
    rejected_inferences: []
    resurfacing_policy: none | owner_only | eligible_opening
```

The runtime may execute several phases in one turn. The fixture declares one
primary human job and one canonical terminal consequence.

## 2. Shared oracles

### 2.1 Value oracle

- The first response solves or materially advances the immediate job.
- No classification, filing, reflection, or profile-maintenance task precedes
  value.
- The response adds information, judgment, coordination, or capability the
  person did not already supply.

### 2.2 Context oracle

- The person does not restate selected objects, current location, named
  participants, or the origin view.
- Retrieved context is purpose-limited and field-scoped.
- Chat history is evidence, not the only representation of the activity.

### 2.3 Authority oracle

- Contribution use, retention, inference, audience, and action are evaluated
  independently.
- A read result never becomes action authority.
- A successful action never becomes broad memory authority.
- New audience, affected-person, provider, spend, public, sensitive-inference,
  or weak-reversal boundaries stop at preview unless an explicit mandate
  already covers the exact consequence.

### 2.4 Owner oracle

- Every durable consequence names one canonical owner and revision.
- Artifacts, prose, cards, and the Chat transcript do not become competing
  writers.
- The terminal state is verified through owner or provider readback, or is
  reported as honestly pending, degraded, or failed.

### 2.5 Interaction oracle

- At most one primary structured projection appears in a turn.
- Simple, visible, low-risk object actions remain directly manipulable.
- Chat handles ambiguity, composition, negotiation, cross-owner action,
  monitoring, and repair.
- A completed turn preserves a return path and can later resume the same
  `ResourceRef` without reposting it.

## 3. Fixture register

| ID | Origin | Primary job | Main owners | Critical architecture question |
| --- | --- | --- | --- | --- |
| A01 | clean Chat | shape | Plan / Occasion | Can a first turn do real work without intake mode? |
| A02 | clean Chat + ticket | understand + operate | Source / Commitment / Plan | Can one contribution produce value and a bounded consequence? |
| A03 | Home Opening | shape + coordinate | Opening projection / Occasion / Plan | Can Chat preserve origin and return after cross-owner work? |
| A04 | Places selection | compare + operate | Place / Route / Plan | Can language and direct manipulation share one state model? |
| A05 | Life artifact | repair | Source / anchor / Occurrence | Can correction target one relation and invalidate dependents? |
| A06 | live Moment | adapt + act | Moment / Commitment / provider | Does the live engine feel like the same agent? |
| A07 | group Chat | coordinate | Occasion / decision / private constraints | Can Vesper help without leaking or dominating? |
| A08 | personal Chat | commit + communicate | Commitment / Plan / audience delivery | Can one utterance cross two independent authority boundaries? |
| A09 | Home disruption | operate + reconcile | provider / Commitment / Opening | Can a mandate remove homework without hiding action truth? |
| A10 | clean Chat | monitor | monitor / provider / Home delivery | Can work continue outside the transcript coherently? |
| A11 | Place | understand | Place / Opening projection / evidence | Can the agent explain selection without inventing biography? |
| A12 | Life episode | make sense + open | Source / Outcome / Place / Opening | Can accumulated life create a genuinely new world opening? |

## 4. A01 — Shape Saturday with Maya from clean Chat

### Situation

It is Thursday evening in New York. The person opens a brand-new private Chat
and says: **“What should Maya and I do Saturday?”** Vesper knows the person is
home, Maya is an existing relationship, both are in New York this weekend, and
there is no Plan or Occasion yet. It does not assume that past travel interests
define the outing.

### Turn compilation

```yaml
origin: {surface: chat, object_refs: [], return_target: chat}
immediate_job: shape
gesture: ask
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience: {mode: private}
  action: {mode: advise}
context:
  include: [current_moment, maya_relationship_ref, shared_availability,
    local_conditions, authorized_recent_context]
  exclude: [maya_private_memory, broad_personality_summary]
phases: [inspect, compose]
target_owner: none
```

### Expected experience

Vesper returns one opinionated Saturday shape grounded in real conditions and
two meaningful alternatives inside the same comparison or sequence. It may say
why each works for the pair without revealing private reasons. It offers one
continuation: **Make this an Occasion** or **Adjust it**. It does not create a
Plan, message Maya, or ask onboarding questions.

If the person says “the first one—ask Maya,” that later turn creates an
Occasion opening and drafts an invitation at the audience boundary.

### Required capabilities

- relationship-safe context read;
- availability and current-condition read;
- Place/event search and comparison;
- sparse Plan/Occasion preparation;
- invitation draft, not send.

### Projection and return

- lead medium: comparison or sequence;
- one primary projection: Saturday shape;
- owner: none until accepted; prepared candidate is ephemeral;
- return: stay in Chat;
- admitted residue: none unless the person creates or keeps it.

### Forbidden behavior

- first-turn `update_intent` as the only operation;
- “tell me your budget, vibe, neighborhood, and preferred time” before value;
- automatic Plan or Occasion creation;
- silently reading Maya's private profile;
- five unrelated recommendations.

### Pass condition

The first turn produces a usable local shape and makes the next consequence
available without treating a new conversation as intake.

## 5. A02 — “Use this” on a flight ticket

### Situation

The person sends a flight ticket or confirmation into a clean private Chat and
says **“Use this.”** The source identifies an upcoming return to New York. A
matching Plan may or may not already exist. Provider status has not yet been
checked.

### Turn compilation

```yaml
origin: {surface: chat, object_refs: [new_source_ref], return_target: chat}
immediate_job: understand
gesture: bring
contribution_grant:
  use: {mode: current_job}
  retention:
    source: retained_private
    claims: scoped_governed
    projections: cached_recomputable
  inference: {mode: source_bound, target: situation, level: L2}
  audience: {mode: private}
  action: {mode: prepare, owner_ref: source_ref}
phases: [inspect, compose, propose]
candidate_owners: [source, commitment, plan]
```

### Expected experience

Vesper first resolves what the ticket establishes and tells the person the
useful consequence: departure/arrival, airport transition, conflict or pickup
implication, and whether it matches an existing Plan. It does not merely say
“I saved your flight.”

If the source unambiguously matches a self-owned Plan and current policy allows
reversible source-bound association, Vesper may attach it privately and show a
quiet receipt with Undo. Creating a new Commitment, changing a Plan, enabling
monitoring, or sharing arrival details remains an explicit continuation unless
the exact mandate already exists.

### Required capabilities

- source inspect and type resolution;
- provider/flight identity and status read;
- Plan/Commitment search by time and provider identity;
- source-bound attachment;
- conflict and transition calculation;
- monitor preparation.

### Projection and return

- lead medium: instrument with supporting evidence;
- owner: Source, then existing Commitment if linked;
- return: stay in Chat; Home may update only after an owned consequence;
- residue: source and extracted claims only within the Bring grant.

### Forbidden behavior

- treating the ticket as proof the flight occurred;
- inventing a Trip because none exists;
- enabling location sharing or notifications automatically;
- learning a general airline or airport preference;
- showing an upload-success card without operational value.

### Pass condition

The source changes the person's present capability immediately and any durable
association is source-bound, repairable, and owner-verified.

## 6. A03 — Make a Home Opening work for four

### Situation

Home shows a complete-on-view opening: a Southern-Italy-related event and
dinner possibility in New York this weekend. The person taps **Work this out**
and says **“Make this work for four.”** The opening already carries its Place,
time window, evidence, and why it was surfaced.

### Turn compilation

```yaml
origin:
  surface: home
  object_refs: [opening_ref, place_refs]
  return_target: home/opening_ref
immediate_job: coordinate
gesture: ask
contribution_grant:
  use: {mode: named_purpose, purposes: [shape_home_possibility_for_group]}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience: {mode: private}
  action: {mode: advise}
phases: [inspect, compose, propose]
candidate_resources: [opening_projection, occasion, plan, commitment]
```

`propose` here means a private candidate composition, not a canonical owner
proposal or authority to create/contact.

### Expected experience

Chat knows what “this” means. It checks capacity, timing, route, and plausible
companions already in the person's authorized relationship space. It returns
one workable composition and names the one unresolved choice, if any. It can
prepare an Occasion and invitee selection without forcing a planning form.

When the person approves the composition and names people, Vesper creates the
Occasion and drafts or sends invitations according to the explicit audience
authority. Home replaces the opening with the active Occasion or its current
next step; it does not leave a stale duplicate.

### Required capabilities

- Opening read and status transition;
- current availability and Place feasibility;
- relationship search scoped to the user's own network;
- Occasion create and invite preparation;
- sparse Plan/Commitment proposal;
- origin refresh and readback.

### Projection and return

- lead medium: sequence or instrument;
- owner: no durable owner before acceptance; the Opening keeps ephemeral
  projection lineage, and Occasion owns accepted shared state;
- return: update the originating Home unit, then offer Open Occasion;
- residue: accepted Occasion/Plan state, not the exploratory alternatives.

### Forbidden behavior

- asking the person to paste the Home card into Chat;
- treating “for four” as authority to select or contact three people;
- making the opening and Occasion compete on Home;
- converting the experience into a day-by-day itinerary.

### Pass condition

One cross-root interaction transforms a Home possibility into a governed,
inspectable Occasion while preserving origin, authority, and return.

## 7. A04 — Compare selected Places and build the easiest route

### Situation

In Places, the person selects two restaurants and one event, then invokes Chat:
**“Compare these, then build the easiest route.”** The current map viewport,
selected canonical Place refs, Saturday time window, and transit conditions are
already attached.

### Turn compilation

```yaml
origin:
  surface: places
  object_refs: [place_a, place_b, event_c]
  selection: map_selection_v1
  return_target: places/current_view
immediate_job: compare
gesture: ask
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience: {mode: private}
  action: {mode: prepare}
phases: [inspect, compose]
target_owner: none
```

### Expected experience

Vesper compares on consistent axes that matter now—timing, travel friction,
reservation risk, group fit, and what each changes about the evening. It then
prepares one route using the selected winner or asks one consequential choice
if the winner cannot be inferred. The route appears as an interactive spatial
projection that returns to the same Places selection.

If the person taps **Use this route**, Vesper creates or updates the appropriate
sparse Plan/Commitments through their owners. The map selection remains a view,
not a hidden itinerary writer.

### Required capabilities

- canonical Place/event reads;
- current route, opening-window, and availability evaluation;
- structured comparison;
- route preparation;
- optional Plan/Commitment proposal.

### Projection and return

- lead medium: comparison, then spatial superseding the same result lineage;
- owner: Place refs and route calculation until committed; Plan thereafter;
- return: Places with route overlay and preserved selection;
- residue: no new Place preference from comparison alone.

### Forbidden behavior

- searching unrelated candidates before evaluating the selection;
- restating map facts without judgment;
- posting a map card into Chat whose route cannot reopen in Places;
- creating itinerary blocks merely to render a route.

### Pass condition

Direct manipulation supplies nouns and scope; Chat supplies intent, judgment,
and composition; both operate on the same canonical refs.

## 8. A05 — Correct a Life artifact without repairing the ontology

### Situation

Life shows a dinner artifact linked to the Italy trip. The person opens it in
Chat and says **“This wasn't my meal—fix it.”** The original photograph is
valid and may have been contributed by a friend; the incorrect relation is the
viewer-to-meal/occurrence interpretation.

### Turn compilation

```yaml
origin:
  surface: life
  object_refs: [artifact_projection_ref, source_ref, occasion_ref]
  return_target: life/artifact_projection_ref
immediate_job: repair
gesture: correct
contribution_grant:
  use: {mode: named_purpose, purposes: [correct_false_meal_relation]}
  retention:
    source: reference_only
    claims: scoped_governed
    projections: cached_recomputable
  inference: {mode: none, target: none, level: L0}
  audience: {mode: private}
  action:
    mode: commit
    owner_ref: outcome_relation_ref
    authority_source: current_instruction
phases: [inspect, propose, commit, reconcile]
target_owner: outcome_relation
```

### Expected experience

Vesper identifies the smallest correction: preserve the photograph and its
author, preserve the shared dinner if independently supported, remove the claim
that it depicts the viewer's meal, and invalidate downstream personal
compositions that depended on that claim. If “my meal” could mean authorship,
presence, ordering, or consumption, Vesper asks one concrete disambiguation
using the known candidate relations.

After correction, it returns a concise before/after receipt and reopens the
updated artifact. It does not ask the person to choose database concepts.

### Required capabilities

- artifact and source inspection;
- claim lineage and dependency read;
- relation-specific correction proposal;
- causal invalidation;
- owner readback and projection refresh.

### Projection and return

- lead medium: comparison or direct state receipt;
- owner: occurrence/outcome relation, not the artifact renderer;
- return: updated Life artifact and affected compositions;
- residue: the correction itself is durable; no new inferred meaning.

### Forbidden behavior

- deleting the original photo;
- rewriting source history;
- fixing only the displayed sentence;
- converting the correction into a global food preference;
- requiring the person to understand Source versus Outcome.

### Pass condition

The exact mistaken relation is repaired once and all dependent projections stop
asserting it while independent evidence survives.

## 9. A06 — Adapt a live evening when the group is exhausted

### Situation

During an active Occasion or Trip, the person says: **“We're exhausted; get us
home after one more stop.”** Vesper has current location, the group's accepted
Commitments, transport state, lodging/base, and permission to use—not retain—
this situational energy signal for the live job.

### Turn compilation

```yaml
origin: {surface: chat, object_refs: [active_occasion, current_plan], return_target: chat}
immediate_job: operate
gesture: act
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience:
    mode: occasion
    occasion_ref: active_occasion
    affected_principal_refs: [occasion_members]
    projection_rule: minimum_safe_effect
  action: {mode: propose, owner_ref: commitment_ref}
phases: [inspect, compose, propose, commit, reconcile]
candidate_owners: [commitment, route, provider]
```

### Expected experience

Vesper chooses one nearby stop that preserves the spirit of the evening, shows
the travel margin home, and identifies which accepted commitment would change.
It does not tell the group that someone is exhausted. If the speaker has the
required authority or the group constitution permits live adaptation, Vesper
applies the reversible Plan change and prepares the route. Otherwise it sends
one group-safe proposal to the required decision owners.

The final projection is **now → one stop → home**, with the changed commitment
and fallback visible. Home and the Occasion update from the same receipt.

### Required capabilities

- Moment and group-safe constraint compilation;
- Place/route/current-condition read;
- Commitment dependency analysis;
- change proposal or authorized mutation;
- provider/transport preparation;
- occurrence reconciliation later.

### Projection and return

- lead medium: sequence plus instrument;
- owner: Commitment/Plan and provider state;
- return: active Home/Occasion state, not a detached chat card;
- residue: operational change and receipt; fatigue expires.

### Forbidden behavior

- narrating a private constraint to the group;
- producing five options in a live, low-energy moment;
- claiming transport is arranged before provider confirmation;
- storing “user dislikes long evenings.”

### Pass condition

The live engine reduces work and preserves trust while remaining visibly the
same Vesper agent used before and after the Occasion.

## 10. A07 — Group-safe coordination without agent domination

### Situation

In an Occasion group Chat, someone says: **“Find something that works for
everyone tomorrow.”** Members have private constraints, different participation
windows, and unequal decision rights. Some people have not addressed Vesper.

### Turn compilation

```yaml
origin: {surface: occasion, object_refs: [occasion_ref], return_target: occasion/chat}
immediate_job: coordinate
gesture: ask
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience:
    mode: occasion
    occasion_ref: active_occasion
    affected_principal_refs: [occasion_members]
  action: {mode: propose, owner_ref: occasion_decision}
phases: [inspect, compose, propose]
target_owner: occasion_decision
```

### Expected experience

Vesper compiles only constraints authorized for group-safe synthesis, considers
all affected members, and returns one recommended direction plus at most one
meaningful alternative. Its explanation names shared fit, not private reasons.
If a decision is needed, it creates one bounded decision artifact addressed to
the appropriate participants. It does not answer every side comment or fill
the room with process narration.

Each participant retains a private Chat path for clarification or constraints.
The group projection shows the common consequence and unresolved votes without
manufacturing a group preference or shared meaning.

### Required capabilities

- Occasion membership and constitution read;
- private constraint to group-safe feasibility compilation;
- Place/time/Commitment search;
- decision proposal and current state read;
- private caucus and group composition.

### Projection and return

- lead medium: comparison or decision instrument;
- owner: Occasion decision and resulting Commitment;
- return: Occasion/group Chat with owner-backed state;
- residue: decision and Commitment; private reasons remain private.

### Forbidden behavior

- exposing which person caused an exclusion;
- treating majority taste as authority over hard constraints;
- speaking when not addressed unless value and urgency clear a high threshold;
- creating a synthetic group personality;
- turning coordination into a workspace setup task.

### Pass condition

The group reaches or advances one fair decision with less coordination burden,
while each person's privacy and agency remain legible.

## 11. A08 — Move dinner and tell the group

### Situation

In private Chat, the organizer says: **“Move dinner to 8 and tell the group.”**
There is an accepted dinner Commitment at 7, a provider reservation, and an
Occasion group. The organizer may have Plan-edit authority but not automatic
provider-change or message-send authority.

### Turn compilation

```yaml
origin: {surface: chat, object_refs: [commitment_ref, occasion_ref], return_target: chat}
immediate_job: operate
gesture: act
contribution_grant:
  use: {mode: named_purpose, purposes: [move_dinner_and_notify]}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: none, target: none, level: L0}
  audience:
    mode: occasion
    occasion_ref: occasion_ref
    affected_principal_refs: [occasion_members]
    may_contact: true
  action:
    mode: commit
    owner_ref: commitment_ref
    authority_source: current_instruction
phases: [inspect, propose, commit, reconcile]
targets: [commitment_ref, provider_reservation_ref, occasion_delivery]
```

### Expected experience

Vesper decomposes the sentence into three consequences:

1. test whether 8 works for the Plan and affected people;
2. change or prepare changing the provider reservation;
3. communicate the verified result to the group.

It applies each only under its own authority. If the provider cannot be changed
automatically, it prepares the handoff and does not mutate the Plan to a false
confirmed state. The group message describes the verified state—changed,
pending, or proposed—not the user's private rationale.

The terminal receipt lists each owner and status without forcing the user to
manage three workflows.

### Required capabilities

- Commitment and dependency read;
- provider availability/change preview;
- Plan/Commitment mutation;
- provider execution or handoff;
- group-safe message compose and send;
- multi-owner receipt aggregation.

### Projection and return

- lead medium: sequence or multi-step instrument;
- owners: Commitment, provider reservation, delivery/message;
- return: Chat with links to changed Commitment and provider status;
- residue: only verified changes and delivery receipt.

### Forbidden behavior

- treating Plan-edit authority as provider or audience authority;
- telling the group before the new time is real or clearly marked pending;
- collapsing partial success into “done”;
- updating only an itinerary block while provider truth remains stale.

### Pass condition

One natural-language request orchestrates several owners while preserving
independent authority and honest partial outcomes.

## 12. A09 — “Handle it” under an existing mandate

### Situation

Home reports that the booked ferry is cancelled. Earlier, the organizer granted
Vesper a narrow mandate: choose and book a refundable alternative under a
specific price and delay threshold for these travelers. The user opens the
disruption and says **“Handle it.”**

### Turn compilation

```yaml
origin:
  surface: home
  object_refs: [disruption_opening, commitment_ref, provider_ref]
  return_target: home/disruption_opening
immediate_job: operate
gesture: act
contribution_grant:
  use: {mode: named_purpose, purposes: [recover_cancelled_ferry]}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: none, target: none, level: L0}
  audience:
    mode: occasion
    occasion_ref: affected_occasion
    affected_principal_refs: [affected_participants]
    may_contact: true
  action:
    mode: mandate
    owner_ref: provider_commitment_ref
    authority_source: standing_mandate
    mandate_ref: ferry_recovery_mandate
phases: [inspect, compose, commit, monitor, reconcile]
target_owners: [provider_commitment, plan_commitment, delivery]
```

### Expected experience

Vesper checks mandate scope, evaluates eligible alternatives, selects the best
one, executes the provider action, updates the canonical Commitment only after
provider confirmation, and communicates the verified consequence. It interrupts
the user only if no option fits the mandate or an irreversible boundary lies
outside it.

Home changes from disruption to the resolved next step. Chat contains a compact
receipt and explanation on demand, not a long transcript of tool activity.

### Required capabilities

- mandate and authority inspection;
- provider status and alternative search;
- deterministic eligibility and tradeoff evaluation;
- provider execute/cancel as authorized;
- Commitment reconciliation;
- affected-audience delivery;
- recovery and refund monitoring.

### Projection and return

- lead medium: operational instrument;
- owner: provider Commitment plus Plan Commitment;
- return: updated Home state; Chat remains available for inspection;
- residue: receipts, provider truth, and revised Commitment only.

### Forbidden behavior

- asking for confirmation already covered by the mandate;
- hiding why an option was within scope;
- updating the Plan before provider confirmation;
- narrating raw internal steps as oversight;
- expanding the mandate from one disruption to future travel generally.

### Pass condition

The agent removes work precisely because scope was granted in advance, while
verification and recovery remain inspectable.

## 13. A10 — Monitor a flight and notify only on material change

### Situation

The person says in a new private Chat: **“Track UA123 and let me know if pickup
needs to change.”** They supply the date and identify the pickup plan. No active
Trip thread is required.

### Turn compilation

```yaml
origin: {surface: chat, object_refs: [flight_or_commitment_ref], return_target: chat}
immediate_job: monitor
gesture: act
contribution_grant:
  use: {mode: named_purpose, purposes: [protect_pickup_commitment]}
  retention:
    source: reference_only
    claims: scoped_governed
    projections: cached_recomputable
  inference:
    mode: current_job
    semantic_scope: pickup_materiality
    target: situation
    level: L1
  audience: {mode: private}
  action:
    mode: mandate
    owner_ref: monitor_job
    authority_source: current_instruction
    protected_consequence_ref: pickup_commitment
    threshold: pickup_plan_must_change
    delivery_destination: private_notification
    expires_at: flight_arrival_plus_reconciliation
phases: [inspect, propose, commit, monitor]
target_owners: [monitor_job, pickup_commitment]
```

### Expected experience

Vesper resolves the flight, identifies what pickup consequence is being
protected, proposes a concrete material-change rule, and starts monitoring once
that rule is clear. It does not require the user to keep Chat open.

The monitor has an owner projection with current state, next check, threshold,
expiry, notification destination, and Stop control. Home shows it only while
relevant; a notification occurs only when the pickup consequence materially
changes or the monitor cannot continue reliably.

### Required capabilities

- flight/provider resolution;
- Commitment dependency read;
- monitor create/read/update/stop;
- material-change evaluation;
- notification/delivery policy;
- provider and Commitment reconciliation.

### Projection and return

- lead medium: instrument;
- owner: monitor job plus protected Commitment;
- return: stay in Chat initially; Home/Push carry later changes;
- residue: monitoring mandate and receipts expire with the job.

### Forbidden behavior

- treating a one-time monitor as a general flight preference;
- notifying on every status poll;
- hiding monitoring failure;
- storing the monitor only as an assistant promise in the transcript;
- requiring an itinerary or Trip container.

### Pass condition

The work persists, remains controllable, and affects the right surface without
turning Chat into an activity feed.

## 14. A11 — Explain why a Place appeared

### Situation

Places surfaces an unfamiliar restaurant. The person opens Chat from that Place
and asks: **“Why did you show me this?”** The recommendation was driven by
current location, opening hours, a route corridor, and an authorized prior
Outcome—not by a stable identity claim.

### Turn compilation

```yaml
origin:
  surface: places
  object_refs: [place_ref, opening_or_ranking_ref]
  return_target: places/place_ref
immediate_job: understand
gesture: ask
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: none, target: none, level: L0}
  audience: {mode: private}
  action: {mode: advise}
phases: [inspect, compose]
target_owner: none
```

### Expected experience

Vesper explains the smallest causal set: what is true about the Place now,
what current condition made it useful, and which prior evidence was applied.
It distinguishes **“you said,” “the record shows,” “Vesper inferred,”** and
**“current conditions indicate.”** It does not produce a flattering personality
story.

The person can correct the applied evidence, hide this kind of resurfacing, or
return to the Place. Asking why does not strengthen the recommendation signal.

### Required capabilities

- Place and ranking/opening evidence read;
- applied-context trace inspection;
- source/Outcome inspection;
- causal explanation;
- correction or return-policy control.

### Projection and return

- lead medium: concise prose with supporting evidence;
- owner: Place; the Opening/ranking trace is inspectable projection lineage;
- return: Place projection;
- residue: none unless the person corrects or changes return policy.

### Forbidden behavior

- “because it matches your vibe”;
- exposing private social inputs;
- citing every available signal rather than the decisive ones;
- learning from the explanation request itself;
- making explanation a permanent profile editor.

### Pass condition

The selection becomes intelligible and correctable without overclaiming who
the person is.

## 15. A12 — Turn a Rome episode into a new New York opening

### Situation

In Life, the person opens the Rome episode containing a Colosseum visit, notes
about Aeneas, a film ticket, movement records, and other trip evidence. They
ask: **“Find the version of this feeling in New York.”** The app must not simply
repeat the connection the person already made between the film and Rome.

### Turn compilation

```yaml
origin:
  surface: life
  object_refs: [rome_episode_refs, film_source_ref, colosseum_source_refs]
  selection: authored_attention_thread
  return_target: life/rome_episode
immediate_job: explore
gesture: ask
contribution_grant:
  use: {mode: current_job}
  retention: {source: transient, claims: turn_candidate, projections: none}
  inference: {mode: current_job, target: situation, level: L1}
  audience: {mode: private}
  action: {mode: advise}
phases: [inspect, compose]
candidate_reads: [place, opening_projection]
```

### Expected experience

Vesper identifies the deeper transferable structure in the evidence—such as a
city using inherited stories to legitimate itself, ruins embedded in ordinary
urban life, or myth functioning as civic infrastructure—then researches a
specific New York analogue the person has not already named. It may produce a
sourced comparison, a spatial walk, a concise article, or one event/Place
opening depending on the evidence.

The compact result is complete on view. **Go deeper**, **See on map**, or **Make
this a Saturday** are optional consequences. No continuation is required.

### Required capabilities

- Life/Source/episode retrieval with claim lineage;
- known-to-person and novelty check;
- external research and canonical Place resolution;
- source-grounded comparison or editorial composition;
- optional Opening preparation and Places handoff.

### Projection and return

- lead medium: comparison, prose, spatial, or sequence selected by job;
- owner: composition manifest over Source/Outcome/Place refs; Opening only if
  explicitly admitted;
- return: Life for depth, Places for spatial continuation, Home only if the
  result earns current admission;
- residue: no new preference or Plan unless explicitly continued.

### Forbidden behavior

- repeating “the Colosseum connects to the movie you watched”;
- asserting a psychological trait from one trip;
- turning every connection into a recommendation;
- treating generated prose as evidence;
- creating a New York itinerary from a curiosity question.

### Pass condition

Accumulated evidence enables a novel, grounded, usable opening into the world
that a generic assistant with only transcript memory would be unlikely to
construct.

## 16. Comparative owner and consequence matrix

| Fixture | Starts without durable write | May create | Must never infer/create silently | Terminal truth |
| --- | --- | --- | --- | --- |
| A01 | yes | sparse Plan or Occasion after approval | relationship preference, invitation | ephemeral composition or Occasion readback |
| A02 | no for source custody under Bring | source relation, Commitment link, monitor | occurrence, global travel preference | Source/Commitment readback |
| A03 | yes | Occasion, invitations, Commitments | invitees or audience | Occasion and Home refresh |
| A04 | yes | route, Plan/Commitments after approval | preference from comparison | route or Plan readback |
| A05 | no; correction is durable | corrected relation and invalidations | new meaning | corrected owner revision |
| A06 | yes for fatigue signal | Plan/Commitment change | durable energy/personality claim | Plan/provider receipt |
| A07 | yes | decision and Commitment | group personality or exposed constraint | Occasion decision revision |
| A08 | no when exact action authorized | Plan, provider, and delivery changes | authority inheritance across owners | per-owner receipts |
| A09 | no under mandate | provider and Commitment mutations | broader mandate | provider-confirmed reconciliation |
| A10 | no after monitor mandate | monitor job and delivery | general notification preference | monitor owner state |
| A11 | yes | correction/return-policy change only if asked | stronger preference from asking why | explanation over trace |
| A12 | yes | composition or later Opening | identity, Plan, memory claim | sourced composition / optional Opening |

## 17. Capability coverage generated by the fixtures

The twelve cases require the following stable capability families. They do not
require itinerary-shaped model tools or one tool per visual component.

| Capability family | Fixtures |
| --- | --- |
| Source, claim, and artifact inspection/repair | A02, A05, A11, A12 |
| Life and cross-episode retrieval/comparison | A05, A12 |
| Place search, read, comparison, and routing | A01, A03, A04, A06, A07, A12 |
| Plan, Occasion, and Commitment shape/operations | A01, A03, A04, A06-A10 |
| Relationship/audience-safe coordination | A01, A03, A06-A09 |
| Provider preparation, execution, and reconciliation | A02, A06, A08-A10 |
| Monitor and material-change delivery | A09, A10 |
| Opening explanation, transition, and return policy | A03, A09, A11, A12 |
| Command authority, receipt, Undo, and recovery | A02-A10 |
| Projection and cross-root entry/return | all |

## 18. Cross-fixture architectural requirements

### P0

1. Replace first-turn intake routing with job- and object-aware capability
   retrieval.
2. Introduce a typed cross-root `InteractionEntry` carrying origin refs,
   selection, audience scope, and return target.
3. Extend `TurnPlan` with immediate job, origin/target refs, contribution-grant
   ref, agency ceiling, interaction phase, and return contract.
4. Make `ResourceRef` and owner revision common to context, commands, receipts,
   artifacts, and deep links.
5. Route all consequential operations through one command/authority/receipt
   gateway with canonical readback.
6. Replace itinerary terms in model-facing intent and capability selection with
   Plan, Occasion, Commitment, Occurrence, and provider semantics; keep legacy
   itinerary handlers behind adapters during migration.
7. Separate semantic result from presentation: the agent returns truth,
   operation state, and projection hints; the native resolver selects medium
   and component.
8. Add durable monitor jobs with explicit scope, threshold, expiry, delivery,
   Stop, and failure states.
9. Add causal correction and invalidation across Source, claim, relation,
   artifact, Life, Home, and Place projections.
10. Certify owner refresh and return behavior from every root.

### P1

1. Multi-owner orchestration receipts with partial-success truth.
2. Occasion constitution and group participation controls outside Trip.
3. Known-to-person and novelty checks for generated editorial connections.
4. Viewer-safe selection-rationale traces for Home and Places.
5. General Plan/Commitment writers independent of itinerary blocks.

## 19. Acceptance gate

The pack is ready to promote only when all twelve fixtures can answer, with no
hand-waving:

- what context enters and what is excluded;
- what the person receives before any workflow;
- which capabilities are eligible;
- which exact owner is read or changed;
- which authority and postcondition permit each action;
- what artifact, instrument, direct state, or prose is warranted;
- how the result returns to or updates the origin;
- what persists and what expires;
- how correction, Undo, uncertainty, and partial failure work; and
- how a later turn resumes the object without transcript reconstruction.

The pack fails if any fixture requires an itinerary merely because the current
backend has itinerary tools, or if any artifact becomes an ungoverned owner
merely because the current client can render it.
