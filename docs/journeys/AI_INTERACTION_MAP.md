---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-07-14
last_verified: 2026-07-14
why_new: Map the existing canonical product journeys onto one testable cross-cutting contract for every user interaction with Vesper.
supersedes: []
source_of_truth_for: [vesper-ai-interaction-journey-map]
---

# Vesper AI Interaction Journey Map

> Status: canonical cross-cutting map
> Owner: founder / engineering
> Last updated: 2026-07-14
> Source of truth for: how a user enters, converses with, delegates to, and
> recovers work with Vesper across the canonical product journeys

This document is the AI-specific lens over the canonical journey registry. It
does **not** create a second product-journey system and it does not renumber
J01–J19. The numbered journey owns the product promise and durable outcome;
this map owns the interaction contract from the user's first AI entry point
through context, response, action, persistence, and recovery.

Use it to answer a narrower question than the main journey set:

> Can a traveler interact with Vesper naturally and safely in every context,
> and can they trust what happens while Vesper is responding or acting?

Canonical inputs:

- [Canonical journey index](README.md)
- [Journey promotion board](STATUS.md)
- [Vesper system charter](../systems/concierge-vesper.md)
- [Agent Chat page spec](../../travel-app/docs/page-specs/agent-chat.md)
- [Trip Group Chat page spec](../../travel-app/docs/page-specs/trip-group-chat.md)
- [Vesper Chat surface contract](../../travel-app/docs/surfaces/vesper-chat/contract.md)
- [Concierge behavior spec](../../travel-agent/docs/product/Concierge%20Behavior%20Spec.md)
- [Agent control-plane baseline](../../travel-agent/docs/architecture/Agent%20Control%20Plane%20Phase%200%20Baseline.md)
- [Agent control-plane refactor](../../travel-agent/docs/architecture/Agent%20Control%20Plane%20Refactor.md)

## The User's Relationship With Vesper

The complete AI journey is a loop, not a single chat screen:

1. **Enter with intent** from Vesper Home, Trips, Discover, a trip object,
   Atlas, a notification, or a live-trip surface.
2. **Understand the room**: private, private-and-trip-scoped, or group-visible.
3. **Say something naturally** without first translating it into product
   structure.
4. **Receive useful acknowledgment** while the system assembles only the
   context needed for this turn.
5. **Read a progressively delivered response** or see calm, truthful progress
   while Vesper performs longer work.
6. **Review or authorize an action** when the request changes shared, costly,
   private, or destructive state.
7. **See the durable result** in the canonical object—not only in chat prose.
8. **Return later and continue** with the correct conversation, scope, and
   committed state.
9. **Correct, retry, undo, forget, or recover** without duplication, leakage,
   fake success, or loss of the latest turn.

The interaction is successful only when the conversational promise and the
durable product state agree.

## AI Interaction Modes

| Mode | Typical entry | Conversation scope | Context Vesper may use | Primary exit |
|---|---|---|---|---|
| General private Vesper | Vesper Home, Trips ideation | Private, not trip-linked by default | Current user, allowed memory, explicit seed, recent private thread | Continue privately, save an idea, or explicitly create/promote a trip |
| Trip-scoped private Vesper | Private CTA inside a trip, private notification | Private to the traveler, explicitly scoped to one trip | That trip's public state plus the traveler's permitted private context | Advice, private clarification, or a privacy-safe proposed action |
| Trip group room | Trip group chat, group notification | Visible to trip members | Group-visible messages and trip state; private inputs only through safe derived influence | Public answer, reaction, proposal, vote, or shared receipt |
| Context-seeded conversation | Discover, venue, dossier, stay, Story, Map | Private or group according to the initiating CTA | Stable entity seed plus the chosen conversation scope | Save, add, ask group, propose, book, or return to the source object |
| Live-trip companion | Vesper Home live mode, Itinerary, Map, live card | Usually trip-scoped; private/group depends on CTA | Current trip/day/block, time, allowed location/weather, recent changes | A useful now-answer or an explicit live-plan action |
| Proactive Vesper | Home queue, push, notification feed | Determined by outcome ownership and privacy | The minimum context needed to explain and route the event | Smallest useful private, group, proposal, plan, booking, or memory surface |
| Post-trip and memory Vesper | Story, Memory, Atlas candidate/receipt | Private unless the user explicitly shares an artifact | Provenanced observations, kept artifacts, allowed cross-trip taste | Story, kept/dismissed memory, correction, forget, export, or deletion |

### Scope resolution is a trust boundary

Scope must be resolved before context assembly or message submission:

1. Explicit route and CTA intent wins.
2. An explicit `conversationId` wins over inferred history.
3. An explicit `tripId` scopes the interaction but does not by itself make a
   private interaction group-visible.
4. Group scope requires an explicit group destination or group-owned object.
5. `currentTrip` is fallback context only; it must never silently attach a
   general Vesper conversation to a trip.
6. A single-member trip remains private/solo and never inherits group chrome,
   consensus, or participant assumptions.

## Canonical AI Turn Lifecycle

Every AI-enabled surface should implement the same conceptual lifecycle even
when its visual treatment differs.

| Stage | What the user should understand | System contract | Must never happen |
|---|---|---|---|
| 1. Entry | Where they are and whether this is private or shared | Resolve destination, seed, trip, conversation, and participant scope before send | A generic Home turn silently inherits a recent trip; a private CTA opens group chat |
| 2. Local send | Their exact message was captured | Render the local turn immediately and preserve the draft until accepted | Keyboard/composer covers the message; prefill disappears while identity resolves |
| 3. Acceptance | The message reached Vesper | Assign stable turn/message identity and distinguish accepted work from a local send | `Sending…` remains after the server has accepted the message or while AI work is already visible |
| 4. Context | Vesper understands the relevant situation | Assemble minimum necessary user, trip, entity, moment, and memory context with provenance and scope filters | Dump every available context source into every turn; leak another trip or member's private context |
| 5. First response | Vesper is present and the request is progressing | Ordinary chat targets first text within 3,000 ms; live surfaces provide semantic feedback before the four-second silent-wait ceiling | Blank waiting, fake typing on a cache hit, or an extra blocking model call merely to classify an ordinary turn |
| 6. Response/work | Whether Vesper is writing, doing meaningful work, or needs input | Smooth prose delivery; reviewed action language; stable action identity; bounded completion trail | Raw tool names, chain-of-thought, flickering status, token-by-token accessibility announcements |
| 7. Authorization | What will change and whether consent is required | Apply authority policy for shared, financial, private, consequential, or destructive actions | Prose implies completion before authorization or before the write is verified |
| 8. Commitment | What actually changed | Persist the canonical object and return ids, receipts, postconditions, and idempotency identity | A chat-only success with no durable mutation; retry duplicates the action |
| 9. Reconciliation | Where the result now lives | Invalidate/refetch all affected read models and route to the smallest useful object | Plan, Map, Chat, booking, notification, or Atlas contradict the accepted result |
| 10. Resume/recovery | Whether work completed, failed, or remains unknown | Reconnect by stable turn/workflow identity; recover accepted work; offer safe retry, correction, or undo | Foregrounding replaces a newer turn, cancellation fabricates failure, or an unknown outcome is labeled successful |

## AI Interaction Arcs

These eight arcs are the smallest complete AI-specific certification set. They
reuse existing journeys rather than competing with them.

### AI-01 — First Contact And Honest Scope

**User goal:** Start with an idea, question, greeting, or contextual prompt and
feel that Vesper understands why they arrived.

**Canonical path:**

1. Enter from Vesper Home, Trips ideation, or a context-seeded surface.
2. Confirm the destination is private unless the user explicitly chose a group action.
3. Submit before or after conversation identity is established.
4. See the message locally, then a useful first response within the ordinary-chat budget.
5. Reopen the thread and find the same scope and conversation identity.
6. Create or promote a trip only after explicit user intent.

**Critical variants:** no history, returning user, greeting, vague intent,
concrete intent, Discover seed, single-member trip, slow conversation creation.

**Durable proof:** stable conversation/message ids; optional explicit draft trip.

**Owned by:** J01, J07, J14. Auth and invite detours are supported by J02 and J18.

### AI-02 — Multi-Turn Understanding And Correction

**User goal:** Continue naturally across turns without restating everything,
while being able to correct Vesper when assumptions change.

**Canonical path:**

1. Ask an ordinary question using recent conversational context.
2. Add a constraint, correction, or changed date/participant fact.
3. Retrieve deeper trip, place, or memory context only when the request needs it.
4. Resume after leaving and reopening the app.
5. Verify the latest correction governs later recommendations and actions.

**Critical variants:** context-light greeting, deep planning follow-up, explicit
correction, stale cached context, cross-trip recall, background/foreground.

**Durable proof:** turn history, context-source trace, corrected canonical state
or observation, and no use of superseded facts.

**Owned by:** J01, J06, J11, J17.

### AI-03 — Private Truth To Group-Safe Help

**User goal:** Tell Vesper something candidly and still receive useful group
planning help without exposing the private fact.

**Canonical path:**

1. Enter trip-scoped private Vesper.
2. Share a private constraint or preference.
3. Receive a candid private acknowledgment.
4. Ask Vesper to help the group or allow the signal to influence a proposal.
5. Inspect the group message, proposal, plan, notification, and booking copy.
6. Inspect provenance and retire or forget the private signal.

**Critical variants:** accessibility, dietary, budget, relationship, energy, and
organizer-stress signals.

**Durable proof:** owner-scoped private source, public-safe derived rationale,
privacy receipt, and persisted control state.

**Owned by:** J04, with routing in J09 and control in J11/J16.

### AI-04 — Group Facilitation To Shared Decision

**User goal:** Ask Vesper in a shared room, understand the recommendation,
coordinate lightweight input, and know exactly what the group decided.

**Canonical path:**

1. Ask a public trip question in group chat.
2. Vesper responds in concise group-safe language.
3. Vesper creates a structured proposal when a shared decision is required.
4. Members react/vote or the authorized person resolves it.
5. Vesper reports the accepted, rejected, or still-open result truthfully.
6. Another participant joining mid-turn reconstructs current activity.
7. The final decision persists in Plan and Changes.

**Critical variants:** parallel tool actions, two calls to the same tool,
observer joins mid-turn, rejected proposal, duplicate vote/retry, participant
backgrounding.

**Durable proof:** proposal, votes, resolution, affected ids, action ids, plan
mutation, and public receipt.

**Owned by:** J05; postcondition coherence is owned by J06.

### AI-05 — Tool-Backed Action And Verified Outcome

**User goal:** Ask in natural language and get a real travel task completed
without mistaking confident prose for a committed result.

**Canonical path:**

1. Ask Vesper to search, shape, change, save, add, hold, book, or settle.
2. Receive early prose or calm action progress while longer work continues.
3. Review the structured object and authorize when policy requires it.
4. Execute with stable action and idempotency identities.
5. Verify postconditions against the canonical object.
6. Show a receipt and reconcile every affected read model.
7. Retry or undo safely when supported.

**Critical variants:** read-only lookup, direct low-risk edit, group proposal,
financial confirmation, stale write, destructive action, provider timeout,
unknown result.

**Durable proof:** tool invocation/action id, authority decision, persisted
object id, provider receipt where applicable, postcondition, and undo/reversal
record.

**Owned by:** J05, J06, J07, J08, J10, J13, J15.

### AI-06 — Proactive And Live-Trip Companion

**User goal:** Get timely, situational help without being spammed or receiving
advice detached from the current trip moment.

**Canonical path:**

1. Enter during an active trip or from a proactive notification.
2. Vesper identifies current trip/day/block and allowed moment context.
3. Ask “what now?” or act on one useful proactive card.
4. Degrade gracefully when location or network context is unavailable.
5. Route private outcomes privately and group-visible outcomes publicly.
6. Dismiss, snooze, or act and see the proactive state update.

**Critical variants:** location allowed/denied/undetermined, stale next block,
quiet hours, missing route id, private versus group outcome.

**Durable proof:** source event/outcome id, routing decision, read/dismiss/action
state, and any resulting trip mutation.

**Owned by:** J08 and J09; projection agreement remains J06.

### AI-07 — Learning, Recall, Explanation, And Control

**User goal:** Benefit from Vesper knowing them over time without the experience
becoming mysterious, creepy, incorrect, or irreversible.

**Canonical path:**

1. Complete a trip or create a meaningful preference signal.
2. Review a candidate, artifact, learned signal, or receipt.
3. Keep, correct, dispute, dismiss, or forget it.
4. Begin another trip and receive relevant taste recall.
5. Verify recall is attributed to the user and does not expose another trip's
   private group context.
6. Export or delete personal data and confirm downstream behavior changes.

**Critical variants:** weak observation, hard constraint, duplicate candidate,
cross-trip affinity, retired signal, memory reset, account deletion.

**Durable proof:** source provenance, confidence/status, kept or retired artifact,
privacy audit entry, and deletion/anonymization result.

**Owned by:** J11, J12, J16, J17.

### AI-08 — Failure, Interruption, And Trustworthy Recovery

**User goal:** Understand whether Vesper heard, completed, failed, or is still
working—and recover without repeating risky actions.

**Canonical path:**

1. Interrupt transport, background the app, expire auth, or trigger a provider/tool failure.
2. Preserve the accepted user turn and any durable server-side workflow.
3. Reconnect using stable turn/action/workflow identity.
4. Reconstruct active and recently completed work without raw execution logs.
5. Classify the outcome as completed, failed, canceled, retryable, or unknown.
6. Retry idempotently, re-authenticate, refresh conflict state, or return later.

**Critical variants:** disconnect before acceptance, disconnect after acceptance,
partial text stream, post-text agent work, 401/403/409/410/429/503, app
backgrounding, process loss, duplicate retry, newer turn already started.

**Durable proof:** persisted message/turn, lifecycle events, action/workflow
state, last acknowledged event, error class, and idempotent recovery result.

**Owned by:** J13 and cross-cutting Must Never Happen checks in every AI-enabled journey.

## Journey-To-AI Coverage

| Journey | AI role | AI arcs |
|---|---|---|
| J01 | Core conversational cold start, ideation, explicit trip promotion | AI-01, AI-02 |
| J02 | Supporting auth/invite handoff and correct shared destination | AI-01 |
| J03 | Supporting trip context once an explicit draft exists | AI-02, AI-05 |
| J04 | Core private-context and public-composition boundary | AI-03 |
| J05 | Core group facilitation, proposal, authority, and mutation | AI-04, AI-05 |
| J06 | Core postcondition and cross-surface truth after AI action | AI-02, AI-04, AI-05, AI-06 |
| J07 | Core entity-seeded conversation and contextual action | AI-01, AI-05 |
| J08 | Core live-trip situational assistance | AI-05, AI-06 |
| J09 | Core proactive ownership, privacy, and routing | AI-03, AI-06 |
| J10 | Core booking/expense tool action and financial trust | AI-05, AI-08 |
| J11 | Core memory provenance and user control | AI-02, AI-03, AI-07 |
| J12 | Core post-trip reflection and handoff into durable memory | AI-07 |
| J13 | Core failure and recovery contract | AI-05, AI-08 |
| J14 | Core solo/private scope invariant | AI-01, AI-06 |
| J15 | Core authority, confirmation, idempotency, and reversal when AI acts | AI-05, AI-08 |
| J16 | Core downstream privacy, export, reset, and deletion controls | AI-03, AI-07 |
| J17 | Core cross-trip recall and isolation | AI-02, AI-07 |
| J18 | Supporting signed-out handoff into the intended shared context | AI-01, AI-08 |
| J19 | Supporting social/entity seed and public/private data boundary | AI-01, AI-03 |

## Cross-Cutting AI Invariants

Every AI arc must prove all applicable invariants:

- **Scope:** general private, trip-private, solo, and group conversations never
  collapse into one inferred “current trip” path.
- **Privacy:** private facts may influence a safe outcome but never appear in
  group prose, notifications, booking rationale, shared receipts, or another trip.
- **Context discipline:** context is retrieved because the turn needs it, not
  because it exists; every sensitive source has scope and provenance.
- **Latency:** ordinary chat first text remains at or below 3,000 ms; no mandatory
  classifier/composer call is inserted before a normal response.
- **Perceived progress:** the user can distinguish local sending, server
  acceptance, prose streaming, meaningful action, completion, and failure.
- **No internal leakage:** action copy comes from a reviewed product vocabulary;
  raw tool names, prompts, provider payloads, and chain-of-thought stay hidden.
- **Stable identity:** turn, message, action, proposal, and workflow identities
  survive reconnects and concurrent work.
- **Authority:** Vesper may advise freely but must earn authority to mutate shared,
  costly, private, consequential, or destructive state.
- **Truthful completion:** visible success requires verified postconditions, not
  model confidence or a tool call merely returning without an exception.
- **Idempotency:** retries cannot create duplicate messages, votes, proposals,
  bookings, expenses, itinerary changes, memories, or notifications.
- **Projection coherence:** after a mutation, Chat, Itinerary, Map, Details,
  Changes, Notifications, Booking, and Atlas agree or explicitly show stale/error state.
- **Recovery:** disconnect, cancellation, foregrounding, and re-authentication do
  not overwrite a newer turn or fabricate a terminal outcome.
- **Control:** users can correct assumptions and can inspect, dispute, forget,
  undo, revoke, export, or delete where the underlying product promise allows it.
- **Accessibility:** streaming and activity announce milestones rather than
  tokens; keyboard, reduced motion, large text, and focus behavior remain usable.

## Certification Matrix

Each AI arc is certified cumulatively at five layers:

| Layer | What it proves | Minimum AI-specific evidence |
|---|---|---|
| 1. Static contract | Entry, scope, context, tools, authority, and postconditions are traceable | Route/CTA → conversation scope → context sources → agent/tool contract → durable object |
| 2. Deterministic client | Interaction states and navigation behave without a live model | Composer/keyboard, optimistic send, streaming reducer, progress lifecycle, reconnect, error and structured-object rendering |
| 3. Backend scenario | Persistence, privacy, idempotency, authority, and recovery are real | Stable ids, scoped fixtures, lifecycle events, postcondition checks, duplicate retry, private-egress assertions |
| 4. Live transport | Provider, streaming, deployment, and environment wiring work | TTFT, first meaningful feedback, complete/partial stream, tool lifecycle, provider failure and reconnect traces |
| 5. On-device journey | The experience is actually calm and comprehensible | Real auth, background/foreground, poor network, two-device group observer, keyboard, scrolling, accessibility, final-object reconciliation |

An arc is not certified because one happy-path LLM answer looked good. It is
certified only when the user-visible interaction and durable outcome pass every
required layer.

## Minimum Release Set

Before broader dogfood, run these concrete scenarios end to end:

1. **Cold private first turn:** no trip auto-link, stable thread, first text under
   three seconds, smooth stream, reopen continuity.
2. **Context correction:** multi-turn planning, explicit correction, leave and
   return, later answer/action uses corrected state.
3. **Private-to-group safety:** private constraint influences a group proposal;
   inspect group chat, notification, plan, receipt, and forget control.
4. **Group action with observer:** proposal creation and acceptance while a second
   device joins mid-turn; both devices converge on the same plan and activity.
5. **Long tool-backed turn:** early response, meaningful action state, app
   background/foreground, verified durable result, idempotent retry.
6. **Provider/recovery matrix:** partial stream plus 401/409/429/503 and unknown
   outcome; no fake success, lost latest turn, duplicate action, or raw error leak.
7. **Live what-now:** allowed and denied location variants, current-block truth,
   useful degradation, route into the correct trip object.
8. **Memory loop:** keep/correct/forget a signal, start another trip, verify useful
   recall and strict cross-trip privacy, then exercise export/deletion.

## Trace Prompt For AI-Specific Audits

```text
Read docs/journeys/AI_INTERACTION_MAP.md and the numbered journeys mapped to
<AI-ARC>. Trace the user interaction through Travel App and Travel Agent.

Default verdict: REFUTE until evidence proves the complete arc.

For every turn stage report:
- entry route and CTA intent
- resolved conversation scope and identity
- allowed context sources and privacy filters
- local-send, accepted, streaming, action, and terminal UI states
- model/director/tool/workflow path
- authority and idempotency decision
- durable object and verified postconditions
- invalidation/reconciliation targets
- reconnect/retry/undo behavior
- latency and accessibility evidence
- deterministic test, backend scenario, live trace, and device evidence

Check every Cross-Cutting AI Invariant. Do not count polished prose, a mock-only
path, or a successful tool return without postcondition verification as proof.
```
