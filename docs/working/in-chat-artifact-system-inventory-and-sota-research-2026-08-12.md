---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-12
expires: 2026-09-11
why_new: Inventories Vesper's current in-chat artifact system, evaluates it against current human-AI interaction research, and grounds a phased post-pivot artifact and onboarding execution plan in the current codebase.
promotes_to: null
supersedes: []
related:
  - onboarding-and-entry-point-product-investigation-2026-08-12.md
  - onboarding-claude-design-experiment-brief-2026-08-12.md
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - ../Card Catalog.md
  - ../decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md
  - ../../travel-app/docs/surfaces/vesper-chat/contract.md
  - ../../travel-agent/docs/product/Product Model.md
---

# In-chat artifact system: code inventory and SOTA research

> **Working investigation, not implementation authority.** This document
> records source and research evidence observed on August 12, 2026 and a
> code-grounded execution plan. It does not itself authorize a replacement
> component architecture. Product canon owns the
> durable thesis; the cross-repo card contracts and source own current behavior;
> accepted changes should be promoted into the appropriate decision, system,
> or surface contract.

## 1. Executive answer

Yes, a deep investigation is warranted—but not because Vesper lacks in-chat
artifacts. It has a surprisingly mature artifact substrate: 20 registered
attachment types, several non-attachment conversational objects, durable text
fallbacks, typed arrival envelopes, privacy-aware rendering, canonical action
paths, proposal and booking authority checks, lifecycle handling, telemetry,
and a bounded declarative card pilot.

The current risk is **semantic fragmentation**:

- several components perform variations of compare, choose, propose, or
  receipt work without one user-facing artifact grammar;
- lifecycle exists at multiple layers, but a traveler cannot always tell what
  is provisional, actionable, committed, stale, or owned elsewhere;
- durable messages are strong, while durable *meaning* is uneven—some cards
  reconcile with Plan, Place, proposal, or booking truth; other useful results
  remain transcript furniture;
- correction and steering affordances are bespoke, and generic follow-up chips
  favor “tell me more” over artifact-specific correction;
- provenance is strong in selected route, booking, receipt, and conversation
  flows but is not a consistent interaction layer;
- current telemetry measures exposure and action mechanics more reliably than
  loop closure, correction, owner handoff, reuse, or return;
- the accepted retirement of Atlas has not reached the chat registry or its
  active producer, so product strategy and artifact inventory currently
  disagree.

The research does **not** support replacing this with unconstrained generative
UI. It supports Vesper's existing direction of native, bounded, validated
structures. It also supports going further in three product dimensions:

1. combine language with direct manipulation so users can steer without
   authoring another prompt;
2. make consequential artifacts easy to inspect, verify, correct, and confirm;
3. turn valuable chat output into a durable object with a visible owner,
   lifecycle, and return path.

The emerging product model is:

```text
conversation names intent and supplies judgment
        ↓
artifact makes the current object inspectable and steerable
        ↓
explicit action changes or creates canonical state
        ↓
receipt proves what happened and where it now lives
        ↓
Trips / Places / Vesper owns the next useful return
```

Chat is therefore not merely a list of messages and cards. It is Vesper's
**mixed-initiative workbench**. The artifact is the temporary shared object
through which a user and Vesper inspect, steer, decide, and hand work to its
durable owner.

## 2. Scope, revisions, and evidence labels

This pass covers:

- `travel-app` artifact types, mapping, rendering, actions, lifecycle,
  telemetry, tests, and surface contracts;
- `travel-agent` producers, schemas, persistence, authority, receipts,
  privacy, and recent artifact-related history;
- the workspace product model, card catalog, August IA decision, onboarding
  investigation, and current working branches; and
- primary HCI/recommender-system research plus official current product
  documentation for market patterns.

It does not include fresh device screenshots, a visual-polish verdict, user
testing, or production analytics. Section 17 proposes an incremental migration
and evaluation sequence; accepted changes still belong in product, surface,
system, journey, and decision authority rather than remaining authoritative in
this working document.

Evidence labels:

- **Verified** — observed in source, contracts, tests, Git history, or an
  accepted decision.
- **In-flight** — present on the current `codex/conversation-convergence`
  branch but not on `main` at the time of inspection.
- **Inference** — a product interpretation of verified facts.
- **Research implication** — a design conclusion derived from cited evidence,
  not proof that the same effect will occur in Vesper.

Revision boundary:

| Repo | Inspected HEAD | `main` | Relationship |
| --- | --- | --- | --- |
| `travel-app` | `8d8caa50` | current local `main` | 21 commits ahead on `codex/conversation-convergence` |
| `travel-agent` | `c39145fee` | current local `main` | 24 commits ahead on `codex/conversation-convergence` |
| workspace | `9ff4bcb` | `origin/main` | 9 commits ahead on `main` |

Both child repos contained active uncommitted work from concurrent sessions.
The backend and mobile changes add a participant-safe shared-room brief to the
room information surface; they were inspected as **in-flight**, not treated as
landed authority. This investigation kept both child repos read-only.

## 3. Product lens: what an in-chat artifact is for

The canonical Product Model says chat, voice, map, itinerary, and proactive
surfaces are interfaces to the same intelligence—not separate products. A
consequential output must reconcile with the object that owns the truth:

- Trips owns Plans, shared commitments, execution, and history;
- Places owns place identity, evidence, and place relationships;
- Vesper owns interpretation, judgment, private work, and orchestration;
- You owns inspectable preferences, people, privacy, and memory controls.

This implies a useful definition:

> An in-chat artifact is a structured, inspectable conversational object that
> helps a person understand, steer, decide, execute, verify, or resume a real
> job. It is not justified by richer visual presentation alone.

An artifact can be ephemeral while the decision is forming, but its
consequences cannot remain ambiguous. It should either:

1. expire without durable clutter;
2. remain a transcript record with an honest status; or
3. create/update a canonical Trip, Place, proposal, booking, preference, or
   other owned object and point to that owner.

## 4. Current architecture trace

The implemented path is intentionally more constrained than an LLM emitting
arbitrary interface code:

```text
sanctioned tool / workflow / system producer
        ↓
persisted message row
  message_type + metadata.card_type + plain-text fallback
        ↓
SSE card envelope reserves geometry; history remains durable authority
        ↓
messageMapping validates and creates a typed MessageAttachment
        ↓
private note or group coordination-object renderer
        ↓
AttachmentRenderer → native specialized component or bounded CardBlueprint
        ↓
typed client handler or server-resolved action
        ↓
canonical domain read/write + receipt / refetch / history reconciliation
```

### 4.1 Contract and ownership layers

| Layer | Current authority | What it protects |
| --- | --- | --- |
| Product meaning | Product Model, three-root IA decision | Which surface owns durable truth |
| Registry | `docs/contracts/chat-card-types.json` and `docs/Card Catalog.md` | Supported discriminators, lifecycle, arrival behavior |
| Persistence | backend message type constraint and structured writers | Durable history and idempotency |
| Shared payload proof | generated card registries and selected shared schemas | Cross-repo drift for card identity and pilot payloads |
| Client parse | `utils/chat/messageMapping.ts` | Fail-closed conversion from metadata to typed objects |
| Presentation | `AttachmentRenderer` and `VesperChatCardKit` | Native layout, accessibility, motion, shared visual language |
| Consequence | domain APIs, proposal/booking workflows, server-resolved composed actions | Authorization, current state, idempotency, safe destinations |
| Interaction lifecycle | `cardInteractionState.ts` plus domain status | Acting, committed, uncertain, superseded, dismissed |
| History compatibility | text fallback and `RetiredCardFallback` | Old messages remain understandable after retirement |
| Measurement | `ChatCardTelemetryBoundary` and domain events | Exposure and action lifecycle without transcript capture |

### 4.2 What is structurally strong

- **Persisted, typed history.** Cards are durable message rows, not client-only
  bubbles. Unknown or invalid payloads fail closed instead of crashing a turn.
- **Fallbacks are treated as product behavior.** Every structured message has
  meaningful text for older clients, search, and retirement.
- **Arrival does not pretend to be truth.** SSE envelopes reserve the right
  footprint; the durable row and history reconciliation supply the payload.
- **Native presentation stays bounded.** Even `CardBlueprintV1` permits only a
  small block grammar. It cannot ship styles, routes, callbacks, or mutation
  payloads.
- **Actions are increasingly re-authorized.** The composed-card pilot stores
  an opaque action reference and resolves it against membership and current
  artifact availability at tap time.
- **Consequential domains retain specialized paths.** Booking, proposal,
  itinerary, and receipt mutations have not been collapsed into the generic
  blueprint pilot.
- **Group privacy is a first-class rendering concern.** Shared decisions,
  public questions, system facts, dignified exceptions, and private handoffs
  are not flattened into a generic bubble.
- **Uncertainty is represented for writes.** The shared interaction vocabulary
  distinguishes retryable failure from an uncertain consequence requiring
  reconciliation.
- **The test surface is broad.** Card mapping, retirement, actions, proposal
  races, receipts, accessibility, contrast, arrival, planning recovery, and
  screen smoke paths all have dedicated test files. This source-level pass did
  not execute the child-repo test suites.

## 5. Inventory: registered message attachments

All 20 rows below are present on `travel-app/main` and are marked `active` in
the generated registry as of this audit. “Active” means the contract permits
rendering; it does not prove production traffic, release exposure, or
post-pivot product endorsement.

| Attachment | Primary user job | Main behavior and durable owner | Current assessment |
| --- | --- | --- | --- |
| `venue_card` | Inspect one committed place recommendation | Shows named venue/take and opens exact venue when identity exists; Place owns the entity | Useful recommendation object, but correction/shortlisting is mostly outside the card |
| `reaction_card` | Give a low-commitment pulse | Selects one or more compact group options with optimistic update/rollback | Clear low-risk mechanic; overlaps conceptually with other choice artifacts |
| `trip_shapes` | Compare early trip directions | Chooses a shape, then selects a planning rhythm that can materialize Plan | Strong “direction before detail” artifact; large and domain-specific |
| `vote_widget` | Make or resolve a shared decision | Votes on a proposal; solo `active_approval` renders a preview/edit gate; proposal and Plan own truth | Consequential and appropriately specialized; current branch improves capability-aware chat-first resolution |
| `notification_card` | Notice and follow an ambient update | Opens a typed destination or validated external URL | Broad carrier; needs strict admission so it does not become a miscellaneous card |
| `taste_dna_reflection` | Inspect/correct what Vesper inferred | Shows learned phrases and allows dispute; You/personal model should own truth | Valuable co-learning seam; product name and consequence messaging need post-pivot clarity |
| `change_applied` | Verify a landed Plan change | Shows before/after, version/operation context, undo or uncertain state | One of the strongest closed-loop artifacts |
| `plan_ready` | Review and continue generated Plan work | Renders a durable itinerary snapshot, work receipt, continuation/revision/undo, then opens Plan | Strong canonical-owner handoff; risks becoming a mini itinerary inside chat |
| `map_route` | Inspect spatial evidence | Renders placed stops, route quality, approximation truth, and opens Plan's Map face | Good evidence object; explicit stale/derived-fact withholding is a trust strength |
| `comparison_card` | Compare saved stays | Shows grounded candidates and vote state, then opens canonical Stay comparison | Correctly does not invent live facts; overlaps with shortlist/decision family |
| `atlas_draft` | Review a pending memory candidate | Opens owner-scoped Atlas review | **Strategy conflict:** Atlas is an accepted retired concept, yet this type, producer, copy, and destination remain active |
| `error_recovery` | Understand and continue after workflow failure | Shows retry/revised-request state for background planning | Good path-forward intent; recovery semantics are bespoke rather than shared across jobs |
| `booking_confirmation` | Verify provider commitment | Shows provider receipt and appropriate link/call/session continuation | Consequential receipt with strong privacy distinctions; group view intentionally collapses settled fact |
| `booking_proposal` | Review and authorize booking intent | Fetches live proposal, then confirm/decline through booking workflow | Correctly specialized; large component and separate visual primitives increase consistency cost |
| `document_edit` | Review a proposed document/Plan change | Shows exact before/after and routes to exact day where available | Conceptually overlaps with solo proposal preview and itinerary operation |
| `narration` | Listen to and inspect a narrated place/route | Plays audio, shows cited narration and feedback | Distinct multimodal artifact; heavy enough that ownership and later retrieval matter |
| `trip_creation_proposal` | Cross from conversation into a real Trip/local Plan | Shows versioned evidence, permits field correction, creates idempotently, then opens Trip | Excellent commitment-boundary pattern and directly relevant to onboarding |
| `itinerary_operation` | Inspect a typed prospective itinerary mutation | Carries normalized operation and opens canonical itinerary review | Strong semantic substrate; current catalog notes still hedge producer maturity |
| `lazy_research` | Mark a live research answer and its risk | Keeps prose visible, adds status, and may accompany one safe Place handoff | Honest companion pattern; the badge/card split can feel duplicative without a clear visual hierarchy |
| `composed_card` | Present a bounded read-oriented view over grounded artifacts | Renders validated blocks; currently the proven writer is a private lazy-research companion with server-resolved Place action | Good constrained pilot, not evidence that specialized consequential cards should be replaced |

### 5.1 Body ownership

Some attachments replace the message body; others accompany prose. The client
currently maintains this in a separate hard-coded set:

- body-owning: narration, reaction, notification, document edit, trip shapes,
  trip creation proposal, comparison, Atlas draft;
- composed card: controlled by `body_mode='card' | 'message'`;
- all others: render in addition to the durable prose.

This prevents duplicate content but is a second semantic registry that can
drift from the cross-repo catalog. More importantly, body ownership is a
presentation decision standing in for a product question: is the prose the
answer and the artifact supporting it, or is the artifact the answer and prose
only the human lead-in?

## 6. Inventory: conversational objects outside the attachment registry

The attachment union is not the whole artifact system.

| Object | Current role | Assessment |
| --- | --- | --- |
| Vesper prose / native Markdown | Human judgment, explanation, transition, and conversation | Necessary connective tissue; should introduce rather than duplicate a structured object |
| `RecommendationBlock` | Move, why for group/person, what to notice/skip, timing, phone/deadline actions | Rich and privacy-aware, but useful reasoning is not independently versioned or owned |
| Suggested follow-ups | Up to three tap-to-fill prompts derived from recommendation fields | Reduces blank-composer burden, but generic labels such as “Tell me more” do little direct steering |
| Conversation citations | Opens the exact prior conversation/message used as personal-history evidence | Strong provenance pattern; currently covers conversation memory, not every factual claim family |
| Composer context receipt | Confirms which Place, venue, dossier, or itinerary item the user deliberately sent | Strong intent and privacy continuity primitive |
| Voice segment | Collapsible completed spoken-turn transcript | Makes multimodal history inspectable; separate from narration output |
| Assistant action strip | Copy, share, report a settled prose response | Useful message mechanics, not artifact correction or domain action |
| Public question | Explicit group-wide request for input | Correctly distinct from a rhetorical question in prose |
| Group event line | Quiet settled system/Plan/booking fact | Keeps ambient truth from competing with required actions |
| Dignified exception/private handoff | Explains that a shared request continued privately and opens exact seeded conversation | Strong privacy seam with durable routing identity |
| Planning stale recovery | Proves the newest Plan was preserved and offers review/recompose | Strong failure honesty; deliberately avoids blind retry |
| Agent activity / card-arrival placeholder | Shows bounded work state and reserves future geometry | Good latency behavior; it should not be confused with an actual artifact or success proof |
| Plan-build / pending workflow UI | Shows long-running planning progress and ownership | Important for resumption; sits between transient activity and durable Plan artifact |
| Group thread object type | Classifies decision, reaction, notification, booking decision, plan fact, system line, or Vesper note | Strong evidence that semantic object type matters more than generic card chrome |

## 7. Lifecycle is present, but split across four meanings

The code uses “lifecycle” for different things that should remain technically
separate but feel coherent to the traveler:

1. **Type lifecycle:** `active → deprecated → retired` protects historical
   compatibility.
2. **Interaction lifecycle:** `ready → acting → committed`, retryable failure,
   uncertain/reconciling, superseded, dismissed.
3. **Domain lifecycle:** proposal, booking, planning, Trip, Move, and memory
   objects each have their own states.
4. **Conversational lifecycle:** streaming, arrival, durable history handoff,
   interruption, pending workflow, and resumption.

The implementation is right not to flatten these into one enum. The product
gap is that the rendered artifact does not consistently answer four simple
questions:

- What is this now?
- What, if anything, can I do?
- Did the consequence land?
- Where does the current truth live?

`change_applied`, booking receipts, stale Plan recovery, and the in-flight
proposal convergence work answer these well. Informational recommendations,
research companions, and some generic notifications answer them less clearly.

## 8. Recent 10–12 day direction

Recent work has moved the artifact system toward semantic convergence rather
than visual novelty.

### 8.1 August 2–5: bounded composition and canonical handoff

- Added `CardBlueprintV1` as a small, validated, native grammar.
- Kept tool execution, grounded artifacts, and presentation separate.
- Preserved prose for companion cards with `body_mode`.
- Added server-resolved read actions and lifecycle telemetry.
- Consolidated Plan-ready and Trip-creation handoffs toward canonical Trips.

### 8.2 August 6–11: evidence, receipts, and causal identity

- Added or hardened local Plan/outcome surfaces, proposal and booking identity,
  why-this receipts, privacy-safe projections, itinerary convergence, route
  integrity, Plan work receipts, and outcome capture.
- Withheld stale route facts and labeled straight-line approximation rather
  than letting polished presentation overstate route truth.
- Added card retirement fallback without deleting historical discriminators.

### 8.3 August 12 in-flight convergence

The current branches make shared decisions more chat-first while preserving
proposal/Plan authority:

- one open proposal remains one central object in the trip room;
- viewer capabilities determine who may vote, resolve, or withdraw;
- organizer resolution moves into the object instead of requiring a parallel
  detail-sheet control path;
- a closed proposal stays a compact outcome while the separate applied-change
  message owns the durable receipt;
- standalone group rooms receive durable participant/update behavior and can
  promote into Trips under current authority.

This is coherent with the product thesis: chat owns the live coordination
moment, the proposal owns the decision, and Plan/history owns the landed
change. Deployment was not verified; these are in-flight branch facts.

## 9. Research synthesis: what current best practice actually supports

### 9.1 Structured output is valuable when it constrains meaning, not just layout

Google's CHI 2024 study of 51 experienced industry professionals found needs
for both low-level output constraints—format and length—and high-level semantic
constraints such as style and non-hallucination. The implication for Vesper is
that a schema is useful only if it protects a user job and truth boundary, not
because structured JSON is easier to render.

Source: [“We Need Structured Output”: Towards User-centered Constraints on Large Language Model Output](https://research.google/pubs/we-need-structured-output-towards-user-centered-constraints-on-large-language-model-output/).

**Fit:** Vesper's schemas, fail-closed mapping, native blocks, artifact refs,
and specialized mutations are strong. The 20-type registry still describes
implementation discriminators more clearly than a small set of user jobs.

### 9.2 Language and direct manipulation are complementary

Microsoft Research's CHI 2026 Interaction-Augmented Instruction work argues
that text is convenient but weak for precise, referential intent; combining it
with clicking, brushing, and other GUI interaction produces a richer composite
instruction. An emerging generative-interface study likewise reports strong
preference for structured interactive responses in information-dense,
exploratory, and multi-step tasks, though that work is newer and should be
treated as directional rather than universal proof.

Sources:

- [Interaction-Augmented Instruction](https://www.microsoft.com/en-us/research/publication/interaction-augmented-instruction-modeling-the-synergy-of-prompts-and-interactions-in-human-genai-collaboration/)
- [Generative Interfaces for Language Models](https://arxiv.org/abs/2508.19227)

**Fit:** reaction choices, trip shapes, proposal controls, field correction,
and planning continuations already embody this. Generic follow-ups and most
recommendation corrections still route through another prose turn.

**Onboarding implication:** the preferred chat-plus-panels direction is
evidence-aligned. The panel should change the artifact or instruction directly,
not merely paste decorative text into the composer.

### 9.3 Significant work should graduate from the transcript

Current product leaders converge on a threshold: when an AI output is
self-contained, reusable, editable, shareable, or likely to outlive the turn,
it becomes a durable artifact beside or beyond chat.

- Claude Artifacts uses a dedicated window, versions, targeted editing, and a
  separate collection for substantial standalone work.
- Microsoft Copilot Pages turns a response into an editable, persistent,
  shareable canvas while preserving chat beside it.
- Gemini Canvas supports direct editing, selection-based revision, preview,
  and export.

Sources:

- [Claude Artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Microsoft 365 Copilot Pages](https://support.microsoft.com/en-US/Microsoft-365-Copilot/how-microsoft-365-copilot-pages-works)
- [Gemini Canvas](https://blog.google/products-and-platforms/products/gemini/gemini-collaboration-features/)

**Research implication:** Vesper does not need a desktop side-by-side canvas.
Trips and Places already supply the durable owner surfaces. Chat artifacts
should be compact working projections into those objects, and substantial work
should open the canonical owner with context preserved.

### 9.4 Verification must be designed, not delegated to user vigilance

Microsoft's co-audit work notes that complex AI output becomes harder—not
easier—for users to check. Its appropriate-reliance synthesis warns that
citations and polished formatting can increase perceived trust even when
sources are bad. Useful interfaces make the questionable claim or consequence
easy to inspect, draw attention at the right risk threshold, and permit review,
editing, and confirmation.

Sources:

- [Co-audit tools](https://www.microsoft.com/en-us/research/publication/co-audit-tools-to-help-humans-double-check-ai-generated-content/)
- [Fostering appropriate reliance on GenAI](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/Appropriate-Reliance-Lessons-Learned-Published-2025-3-3.pdf)

**Fit:** Vesper is strong where it shows before/after, route quality, exact
source conversation, provider truth, proposal impact, or stale-write outcome.
It is weaker when a polished “why for you” or recommendation is not paired
with inspectable evidence or an easy correction.

### 9.5 Friction should scale with consequence

The validated Microsoft Human-AI Interaction guidelines emphasize clear
capabilities, contextually relevant timing, efficient invocation/dismissal,
correction, explanation, and global controls. Magentic-UI operationalizes the
same idea through editable plans, take-over, action guards, and learned reusable
plans. Research on cognitive forcing also warns that mandatory review can
reduce overreliance while increasing time and effort.

Sources:

- [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)
- [Magentic-UI](https://www.microsoft.com/en-us/research/blog/magentic-ui-an-experimental-human-centered-web-agent/)

**Research implication:** one-tap steering is right for low-commitment taste
signals and reversible Moves. Preview/confirm or group governance is right for
Plan and booking consequences. Requiring equal confirmation everywhere would
make Vesper tedious; omitting it everywhere would make Vesper unsafe.

### 9.6 Visible and immediate consequence improves feedback quality

Research on personalized recommendations found that allowing people to preview
the impact of feedback and visibly highlighting the resulting changes improved
reported transparency, preference, and selectivity. Google PAIR similarly
recommends explaining how feedback will affect the experience and when.

Sources:

- [Impact of transparent recommendation interfaces](https://www.microsoft.com/en-us/research/publication/the-impact-of-more-transparent-interfaces-on-behavior-in-personalized-recommendation/)
- [PAIR Mental Models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/)

**Fit:** before/after receipts and Travel DNA disputes are aligned. A generic
reaction or “not quite” affordance is insufficient if the user cannot tell
whether it changed this result, the Plan, or Vesper's future model.

### 9.7 Shortlists are useful thinking objects, not merely saved lists

Recommender-system research found that shortlists reduce cognitive load,
support better decisions, and create useful implicit feedback as a by-product
of real exploration. This is especially relevant to travel, where a person
often needs to hold two or three possibilities before committing.

Source: [Using Shortlists to Support Decision Making and Improve Recommender System Performance](https://www.microsoft.com/en-us/research/publication/using-shortlists-support-decision-making-improve-recommender-system-performance/).

**Fit:** trip shapes, stay comparison, and reaction cards approximate
shortlisting inside specific flows. A general place recommendation often jumps
from “Vesper's pick” to open/save without a visible “still in play” object that
can cross into Places or Trips.

### 9.8 Explainable personalization must also be scrutable

Natural-language user models can make personalization understandable and
correctable rather than hiding inference behind item-level behavior. This is
the deeper value of Travel DNA / preference reflections—not a decorative
personality summary, but a governable model the user can inspect and change.

Sources:

- [Transparent, Scrutable and Explainable User Models](https://research.google/pubs/transparent-scrutable-and-explainable-user-models-for-personalized-recommendation/)
- [Natural Language User Profiles for Transparent and Scrutable Recommendation](https://research.google/pubs/on-natural-language-user-profiles-for-transparent-and-scrutable-recommendation/)

**Post-pivot implication:** retain the capability under You/personal memory;
do not preserve Atlas as a competing artifact owner.

### 9.9 Dynamic UI has a trust boundary

PAIR explicitly warns that unpredictable layout changes can break habituation.
The stronger interpretation of generative UI is therefore not “let the model
invent the interface.” It is “select and fill a bounded interaction grammar
appropriate to the current job.”

Sources:

- [PAIR Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/)
- [Interaction-Augmented Instruction](https://www.microsoft.com/en-us/research/publication/interaction-augmented-instruction-modeling-the-synergy-of-prompts-and-interactions-in-human-genai-collaboration/)

**Fit:** the current blueprint's native blocks and server-owned actions are a
better foundation than runtime-generated React. Specialized high-consequence
cards should remain specialized until evidence proves a safe common grammar.

## 10. Current system against the research-derived quality bar

| Dimension | Current verdict | Evidence |
| --- | --- | --- |
| Bounded structure | **Strong** | Typed union, generated registry, schemas, native blueprint, no executable server UI |
| Plain-text fallback/history | **Strong** | Persisted fallback, retirement path, fail-closed mapper |
| Canonical ownership | **Strong for consequential flows; mixed elsewhere** | Plan, proposals, booking, route, and Trip creation reconcile; some recommendations remain transcript-only |
| Direct steering | **Mixed** | Excellent in trip shapes, reactions, proposals, and Trip creation; generic follow-ups are weak |
| Consequence-calibrated authority | **Strong** | Specialized booking/proposal flows, group capabilities, privacy handoffs, uncertain-write handling |
| Verification/provenance | **Mixed-to-strong** | Route quality, receipts, citations, provider truth; inconsistent across recommendation and personalization claims |
| Correction | **Mixed** | Field correction, disputes, vote changes, revision; no common artifact-specific correction affordance |
| Lifecycle legibility | **Mixed** | Rich backend/client states; user-facing questions are answered inconsistently across cards |
| Durability and return | **Mixed** | Messages durable; canonical handoff good for Plans/bookings, weak for reusable exploratory output |
| Privacy/audience | **Strong** | Default-fail private rationale, group projections, dignified exception, private composed-card restriction |
| Failure/path forward | **Strong in planning; mixed globally** | Stale recovery and uncertain writes are excellent; error semantics remain per-flow |
| Product-strategy alignment | **Mixed** | Three-root ownership is emerging; active Atlas artifact contradicts accepted retirement |
| Loop measurement | **Weak-to-mixed** | Exposure/tap/action events exist; artifact correction, owner convergence, reuse, and return are not the primary grammar |
| Visual-system reuse | **Mostly strong** | Most chat artifacts use `VesperChatCardKit`; narration, Travel DNA, Trip creation, booking proposal, and vote composition retain bespoke substrates |

## 11. Important failure modes to avoid

### 11.1 The card zoo

Every new capability receives a new component and discriminator, while users
must relearn whether a tap selects, opens, mutates, approves, or merely fills
the composer. The current overlaps among reaction, trip shapes, comparison,
vote, document edit, and operation review make this a real risk.

### 11.2 The universal-card trap

A generic schema becomes a second application runtime, erasing domain
authority and making consequential actions look as safe as read-only links.
The current `CardBlueprintV1` avoids this by remaining narrow; expanding it
without evidence would reverse that strength.

### 11.3 Polished but unauditable judgment

A beautiful “why this fits” block can cause more overreliance if its evidence,
freshness, or inferred preference is not inspectable. Citations are not a cure
unless the source supports the exact claim.

### 11.4 Conversation as the only owner

Useful shortlists, comparisons, and plans disappear into scrollback. The user
cannot find, share, resume, or observe updates without rediscovering the turn.

### 11.5 Canonical surface as a context reset

An artifact opens Trips or Places but loses the selected option, proposed
change, source message, or return location. Navigation technically succeeds;
the loop still feels broken.

### 11.6 Generic “tell me more” as steering

The user is offered another prompt instead of direct control over the exact
assumption, constraint, option, or consequence that needs correction.

### 11.7 Premature success telemetry

`ChatCardTelemetryBoundary.runAction` records a fulfilled handler as
`committed` even when the action is navigation or when the handler's promise
does not prove a durable domain mutation. This is acceptable as UI mechanics
telemetry only if it is never interpreted as product-loop completion.

### 11.8 Strategy retirement without producer retirement

Hiding a tab while leaving `atlas_draft` active preserves a competing product
owner in prompts, tools, payloads, copy, routes, and analytics. The accepted
decision requires migration or explicit compatibility status, not merely a
navigation change.

### 11.9 Too much embedded product in a mobile transcript

Plan-ready, narration, booking, and proposal artifacts can become mini pages.
If every state and field is rendered inline, chat loses rhythm and the owning
surface becomes redundant. Progressive disclosure and exact handoff matter
more on a narrow screen than visual richness.

### 11.10 Feedback with an invisible consequence

A reaction, dispute, correction, or save is collected, but the user cannot see
what changed now or what Vesper will remember later. This spends trust and
creates noisy learning data.

## 12. Research-derived evaluation lens for the next phase

Before a card is kept, changed, generalized, or retired, answer these questions
with a real fixture and state trace:

1. **Job:** What user job becomes materially easier than prose alone?
2. **Moment:** Why should the artifact appear now rather than remain prose or
   live on its owner surface?
3. **Grounding:** Which exact source or canonical object supports each
   consequential field?
4. **Audience:** Is this private, shared, public, or differently projected by
   viewer capability?
5. **State:** Is it an observation, possibility, draft, proposal, commitment,
   receipt, or stale historical record?
6. **Steering:** Can the user correct the important assumption without writing
   a prompt from scratch?
7. **Consequence:** What exactly happens on each action, and how much friction
   should that consequence require?
8. **Verification:** Can a traveler efficiently check what matters without
   treating polish or citation count as proof?
9. **Owner:** If accepted, where does current truth live—Trips, Places,
   Vesper, or You?
10. **Return:** Can the user resume the same object later, including after
    notification, auth, or another device?
11. **Failure:** Does uncertainty, expiration, conflict, or partial failure
    leave an honest path forward?
12. **Learning:** If this interaction teaches Vesper, can the person see and
    govern the effect?
13. **Measurement:** What event proves progress beyond exposure or a tap?
14. **Retirement:** Can the producer stop while historical messages remain
    understandable?

## 13. Conclusions before architecture work

### 13.1 What the evidence confirms

- The onboarding direction of chat plus selectable panels is sound.
- Artifact polish is central product work, not ornamentation.
- Vesper's bounded native composition approach is directionally correct.
- Specialized consequential artifacts should remain specialized.
- Chat-first group decisions can increase coherence when proposal and Plan
  truth remain canonical.
- The strongest artifacts already follow the loop:
  **judgment → direct steer/review → consequence → receipt → owner**.

### 13.2 What the evidence disproves

- Chat alone is not enough for precise, low-effort steering.
- A large catalog of individually polished cards does not by itself form a
  coherent product language.
- A generic “generate any UI” runtime is not required for SOTA behavior.
- Citations, confidence copy, or a polished explanation alone do not create
  appropriate trust.
- Persisting a message does not automatically make the underlying work a
  durable product artifact.
- Retiring Atlas visually while continuing to emit Atlas artifacts is not a
  completed pivot.

### 13.3 The bounded next question

The next phase should not begin with React component consolidation. It should
derive a small product grammar from real user loops and then map the existing
inventory onto it. The likely jobs are visible—glance, explore, compare,
decide, execute, verify, and resume—but this document intentionally does not
declare the final taxonomy or migration.

The immediate design-research task is to apply the 14-question lens to a small
set of pivotal fixtures:

1. onboarding fragment → first judgment → one correction → Trip/local Plan;
2. place recommendation → shortlist/steer → Places or Trip handoff;
3. group proposal → vote/resolve → applied Plan receipt;
4. stale or failed Plan work → honest recovery;
5. recommendation → governed preference reflection; and
6. substantial generated Plan → compact chat projection → canonical owner.

Only after those traces are coherent should the team decide which components
share a semantic primitive, which remain specialized, and which artifacts or
producers should retire.

## 14. Primary code and contract evidence

Workspace:

- `docs/Card Catalog.md`
- `docs/contracts/chat-card-types.json`
- `docs/contracts/card-arrival.json`
- `docs/decisions/2026-08-12-retire-discover-and-atlas-product-surfaces.md`

Travel App:

- `types/chat.ts`
- `utils/chat/messageMapping.ts`
- `utils/chat/cardBlueprint.ts`
- `utils/chat/chatCardTypes.generated.ts`
- `utils/cardInteractionState.ts`
- `components/chat/AttachmentRenderer.tsx`
- `components/chat/VesperChatCardKit.tsx`
- `components/chat/ComposedChatCard.tsx`
- `components/chat/bodyOwning.ts`
- `components/chat/ChatCardTelemetryContext.tsx`
- `components/chat/PrivateVesperNote.tsx`
- `components/chat/group/GroupThreadItem.tsx`
- `components/chat/group/classifyGroupMessage.ts`
- `components/chat/RecommendationBlock.tsx`
- `components/chat/SuggestedFollowUps.tsx`
- `components/chat/CardArrivalPlaceholder.tsx`
- `docs/surfaces/vesper-chat/contract.md`

Travel Agent:

- `backend/concierge/structured_messages.py`
- `backend/concierge/structured_card_tool_schemas.py`
- `backend/concierge/_prompts_skill_cards.py`
- `backend/concierge/composed_cards.py`
- `backend/concierge/receipt_composer.py`
- `backend/concierge/planning_workflow.py`
- `backend/api/routes/composed_card_actions.py`
- `backend/api/routes/conversations.py`
- `backend/api/routes/proposals.py`

## 15. Second online validation pass: is this actually a well-trodden path?

This pass tested the proposed next step against recent 2025–2026 HCI work,
current general-purpose AI products, and current place/travel products. It also
looked for evidence against the direction rather than treating market activity
as validation by itself.

### 15.1 Verdict

**Yes—with an important qualification.** The well-trodden direction is not
“put more cards in chat,” and it is not “invent one universal generative UI.”
The converging pattern is a three-layer interaction architecture:

```text
conversation
  captures ambiguous intent, context, and negotiation
        ↓
manipulable working artifact
  makes options, state, evidence, and corrections visible
        ↓
durable domain object
  owns committed state, collaboration, later use, and return
```

That is almost exactly the direction inferred from Vesper's code. Recent
research supports hybrid language-plus-interface interaction, task-derived
models, direct manipulation, visible plans and progress, consequence-scaled
approval, and persistent outputs. Shipped products independently converge on
turning valuable chat output into editable, shareable, revisitable state.

The exact Vesper grammar—whether it has five, six, or seven roles, and which of
the 20 current attachment types map to each role—is **not** externally proven.
That must be derived from Vesper's actual journeys. The recommendation to trace
fixtures before consolidating components is therefore strengthened, not
weakened, by the research.

| Proposed direction | Validation | Confidence | Necessary refinement |
| --- | --- | --- | --- |
| Trace complete user journeys before redesigning components | Recent workflow and task-model research explicitly starts from tasks, information entities, relationships, and micro-decisions | High | Trace user-visible state and ownership, not only render paths |
| Combine chat with native interactive artifacts | Multiple recent studies find language and direct manipulation complementary for open-ended or exploratory work | High | Plain conversation should remain available for simple or low-consequence turns |
| Derive a small lifecycle grammar | Current research uses structured representations and task/state models; current products repeatedly expose draft, refine, approve, persist, share, and revisit stages | High for the principle; medium for Vesper's exact roles | Treat the first grammar as a testable hypothesis, not a new ontology to defend |
| Graduate valuable work from chat into Trips or Places | Copilot Pages, Claude Artifacts, Gemini Canvas, Wanderlog, Ask Maps, and Yelp all connect conversation to a durable or actionable product surface | High as market convergence; medium as causal evidence | The handoff must preserve context and show a receipt/return path |
| Use bounded native components rather than arbitrary generated code | Structured-output and task-model work supports schemas and constrained mappings; arbitrary code generation is harder to inspect and iteratively control | High | Allow flexible composition inside a stable interaction contract |
| Make every useful response an artifact | Counterevidence warns about over-scaffolding, excess process, and unnecessary user effort | Low / rejected | Artifact weight should scale with information density, persistence, collaboration, and consequence |

### 15.2 What has converged across research and products

#### A. Conversation is becoming the control plane, not the final container

The 2026 *Generative Interfaces for Language Models* work argues that linear
chat becomes inefficient for information-dense, exploratory, multi-turn work.
Its proposed interfaces use structured representations, dependencies, and
iterative refinement rather than treating every answer as another text block.
The result is strongest in domains where visual organization and interaction
reduce cognitive load; it is not evidence that every query needs a generated
interface.

The CHI 2025 Jelly system reaches a related result from another direction. It
uses a task-driven data model—entities, relationships, data, and dependencies—
as the stable substrate, then lets the user change the result through both
language and direct manipulation. This is strong support for deriving
Vesper's artifact grammar from the underlying travel task and canonical state,
not from the current renderer names.

Current products exhibit the same separation. Microsoft Copilot Pages turns a
chat response into a persistent side-by-side page that can be directly edited,
updated through chat, shared without exposing the conversation, and revisited
later. Gemini Canvas similarly separates an interactive editing space from the
prompt thread. Claude Artifacts makes created output independently viewable,
shareable, and remixable. These are different products, but they all distinguish
the negotiation history from the object being worked on.

**Implication for Vesper:** Vesper can remain conversational while Trips and
Places remain the durable product. The artifact between them is a working
projection of the current decision—not a fourth permanent top-level surface.

#### B. “Do it with me” beats “do it for me” for exploratory judgment

A CHI 2025 study compared a fully automated copilot with a guided copilot that
automated trivial steps while exposing stepwise visual guidance. In its small
study, the guided version produced greater perceived control, software utility,
and learnability, particularly for exploratory and creative tasks; full
automation saved time for simpler tasks. This is unusually close to travel
planning, where the work is subjective and constraints emerge during
exploration.

Microsoft's Magentic-UI operationalizes the same principle for agentic work:
users can edit a plan before execution, observe progress, interrupt and steer,
approve consequential actions, and save a successful plan for reuse. It also
acknowledges that plan review adds upfront cost. The point is not to expose a
plan for every restaurant question; it is to expose the right control object
when the agent is about to do consequential or multi-step work.

**Implication for Vesper:** the strongest artifact is not a polished answer.
It is a shared object with cheap correction. A user should be able to remove a
place, prefer one option, change a constraint, resolve a proposal, or confirm a
mutation without composing a new prompt. Vesper can still infer and automate
low-risk details.

#### C. Durable state is part of the value proposition

The product pattern is remarkably consistent:

- Copilot Pages converts an ephemeral response into an editable, persistent,
  shareable object with its own return path.
- Gemini Canvas makes a generated draft an interactive work surface.
- Claude Artifacts separates created content from the conversation and lets it
  be shared or remixed.
- Wanderlog's AI assistant lets people add suggested places directly into the
  trip plan on the same page; collaboration, reservations, map, and itinerary
  live in the durable plan rather than the assistant transcript.
- Google Ask Maps answers local questions conversationally, but the product
  actions are native Maps actions: save a place to a list, share it, book it,
  or use it in the map context.
- Yelp Assistant sits on a business page, offers contextual starter prompts,
  and, in its services flow, combines free-form answers with one-click choices
  before asking the user to review and approve the project request it sends.

The last two examples matter for Vesper's ambient home-city thesis. This
pattern is not inherently trip-first. A conversation about tonight, a nearby
place, or a friend's recommendation can close into a saved Place, a small list,
a reservation/action, or a shareable object without manufacturing a Trip.

**Implication for Vesper:** “graduate from chat” should mean “move into the
smallest canonical object appropriate to the user's intent.” Sometimes that is
a Trip; often it is a Place, preference, shortlist, proposal, or completed
action. Onboarding should demonstrate this with tappable starter material, not
require the user to invent a trip or type a good prompt.

#### D. Collaboration requires controls, not a louder agent

IBM's IUI 2025 work on AI agents in group conversation found that participants
benefited from and preferred agent participation, but disliked the agent
dominating the conversation and wanted control over when, what, and where it
responded and who could control it.

**Implication for Vesper:** group chat should not become a stream of Vesper
opinions. The group proposal is the right kind of artifact because it creates a
bounded object around which humans can vote, edit, resolve, and apply. Vesper's
role is to synthesize and advance the object while preserving group agency.

### 15.3 Counterevidence and limits

The evidence does not justify a broad artifact rewrite without experiments.

1. **Market convergence is not causal proof.** Large AI products shipping
   canvases shows a repeated product strategy, not that the pattern improves
   Vesper retention or travel decisions.
2. **Recent studies are often prototypes with small samples.** Jelly's user
   evaluation, for example, is evidence of feasibility and useful interaction
   patterns, not production-scale validation. The guided-copilot study is also
   small and uses feature-rich software rather than travel.
3. **The headline results are conditional.** The reported gains for generative
   interfaces concern information-dense structured domains. They should not be
   generalized to greetings, simple facts, or quick local questions.
4. **Over-scaffolding is a real failure mode.** The 2025 Tools for Thought
   synthesis warns that too much imposed process can interfere with users'
   own reasoning. It distinguishes process-oriented support—which can maintain
   situation awareness—from end-to-end output that makes people reason
   backward from an answer and can increase overreliance. The correct degree of
   structure depends on familiarity, complexity, creativity, and learning.
5. **Visible control has a cost.** Plans, approval steps, evidence, and receipts
   all add time. They earn that cost only when the task is consequential,
   ambiguous, collaborative, persistent, or expensive to reverse.
6. **Dynamic interfaces can destroy learnability.** If controls, labels, and
   behaviors change with every answer, users cannot form a stable mental model.
   Vesper should generate content and composition within stable native
   semantics, not generate a novel product on every turn.

These limits argue for a **graduated interaction model**:

| Turn shape | Default response |
| --- | --- |
| Simple, reversible, transient | Plain conversational response or a compact preview |
| Exploratory and preference-heavy | Small options/shortlist artifact with direct steering |
| Multi-step or stateful | Editable plan/proposal with status and owner |
| Consequential mutation | Preview, explicit confirmation where needed, then an honest receipt |
| Durable or collaborative output | Compact chat projection plus canonical Places/Trips owner and return path |
| Failure, staleness, or conflict | Recovery artifact that preserves work and explains the next safe action |

### 15.4 Refined next step

The next step proposed in section 13 remains correct, with four refinements:

1. **Trace the object, not just the screens.** For each pivotal fixture, record
   the user's intent, Vesper's inferred state, artifact state, permitted direct
   manipulations, canonical write, receipt, owner, and later return.
2. **Compare against a plain-chat baseline.** Do not assume an artifact wins.
   Keep it only if it reduces correction burden, makes state clearer, enables a
   meaningful direct action, supports collaboration, or creates reusable state.
3. **Derive roles from lifecycle responsibility.** A plausible first test set
   is preview/recommendation, working set/shortlist, proposal/decision,
   plan/progress, receipt, and recovery. These are hypotheses; the fixtures may
   combine or split them.
4. **Gate new attachment types.** Until the grammar is tested, a new type should
   identify which lifecycle role it serves, what canonical object it reads or
   writes, how a user corrects it, and how the loop closes. Otherwise it should
   reuse an existing primitive or remain conversational.

The first three fixtures remain the highest-leverage set:

1. onboarding fragment or tappable starter → first useful local judgment → one
   correction → saved Place/local working set or Trip;
2. place recommendation → shortlist/direct steer → Places or Trip handoff →
   visible receipt and return; and
3. group proposal → human discussion/vote → resolve → applied Plan receipt.

They cover cold start, ambient local value, subjective judgment, direct
manipulation, individual persistence, group agency, canonical handoff, and
receipt semantics without designing the whole 20-type inventory at once.

### 15.5 What to measure in the experiment

“Coherent,” “trustworthy,” and “sticky” are background concepts, not metrics.
Recent GenAI evaluation work cautions against jumping directly from an abstract
concept to an ad hoc score. For these fixtures, define observable measures
before prototype comparison:

- time and user inputs to first meaningful value;
- typed characters and conversational turns required to express/correct intent;
- whether the user can correctly state what is proposed versus committed;
- correction success and accidental mutation rate;
- whether the user knows where the result now lives;
- success resuming the same object in a later session;
- percent of suggestions that become a save, shortlist decision, proposal,
  applied plan change, share, booking/action, or explicit rejection;
- evidence/provenance inspection when it is relevant, not raw citation taps;
- group participation distribution and whether Vesper dominates; and
- subjective control, effort, confidence, and usefulness, kept separate rather
  than collapsed into one “quality” rating.

A coding agent can trace contracts, state transitions, and scripted fixtures
continuously. It should not be the sole judge of desirability. The efficient
evaluation stack is: deterministic contract assertions first, adversarial
fixture-based agent review second, and a small number of human sessions only
for the residual questions of comprehension, agency, taste, and felt value.

## 16. Research source index

- [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)
- [PAIR Mental Models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/)
- [PAIR Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/)
- [“We Need Structured Output”](https://research.google/pubs/we-need-structured-output-towards-user-centered-constraints-on-large-language-model-output/)
- [Interaction-Augmented Instruction](https://www.microsoft.com/en-us/research/publication/interaction-augmented-instruction-modeling-the-synergy-of-prompts-and-interactions-in-human-genai-collaboration/)
- [Generative Interfaces for Language Models](https://arxiv.org/abs/2508.19227)
- [Co-audit tools](https://www.microsoft.com/en-us/research/publication/co-audit-tools-to-help-humans-double-check-ai-generated-content/)
- [Fostering appropriate reliance on GenAI](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/Appropriate-Reliance-Lessons-Learned-Published-2025-3-3.pdf)
- [Magentic-UI](https://www.microsoft.com/en-us/research/blog/magentic-ui-an-experimental-human-centered-web-agent/)
- [Impact of transparent recommendation interfaces](https://www.microsoft.com/en-us/research/publication/the-impact-of-more-transparent-interfaces-on-behavior-in-personalized-recommendation/)
- [Using Shortlists to Support Decision Making](https://www.microsoft.com/en-us/research/publication/using-shortlists-support-decision-making-improve-recommender-system-performance/)
- [Transparent, Scrutable and Explainable User Models](https://research.google/pubs/transparent-scrutable-and-explainable-user-models-for-personalized-recommendation/)
- [Natural Language User Profiles for Transparent and Scrutable Recommendation](https://research.google/pubs/on-natural-language-user-profiles-for-transparent-and-scrutable-recommendation/)
- [Claude Artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Microsoft 365 Copilot Pages](https://support.microsoft.com/en-US/Microsoft-365-Copilot/how-microsoft-365-copilot-pages-works)
- [Gemini Canvas](https://blog.google/products-and-platforms/products/gemini/gemini-collaboration-features/)
- [Tools for Thought: Research and Design for Understanding, Protecting, and Augmenting Human Cognition with Generative AI](https://arxiv.org/abs/2508.21036)
- [Generative and Malleable User Interfaces with Generative and Evolving Task-Driven Data Model](https://doi.org/10.1145/3706598.3713285)
- [Do It For Me vs. Do It With Me](https://arxiv.org/abs/2504.15549)
- [Controlling AI Agent Participation in Group Conversations](https://research.ibm.com/publications/controlling-ai-agent-participation-in-group-conversations-a-human-centered-approach)
- [Evaluating Generative AI Systems Is a Social Science Measurement Challenge](https://arxiv.org/abs/2411.10939)
- [Wanderlog AI trip-plan assistant](https://wanderlog.com/trip-plan-assistant)
- [Google Ask Maps](https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/)
- [Yelp Assistant: conversational local discovery](https://blog.yelp.com/news/fall-product-release-2025/)
- [Yelp Assistant: one-click responses and request approval](https://blog.yelp.com/news/spring-product-release-2024/)

## 17. Current-codebase pass and detailed execution plan

This section reflects one more code pass at the current workspace revisions,
including the newest conversation-convergence commits and the active—but not
yet committed—shared-room brief work. It turns the research direction into an
ordered plan. It does not authorize editing the two dirty child repositories
until their concurrent work has settled.

### 17.1 Architectural verdict

The product thesis and implementation are **coherent at the substrate and
object-model level, but not yet coherent at the first-use and cross-surface
experience level**.

The three visible roots now form a defensible product model:

| Root | User question | Canonical responsibility | Current strength |
| --- | --- | --- | --- |
| Trips | What are we actually doing? | Plans, commitments, group decisions, execution, and history | Strongest closed loops, especially proposal → resolution → Plan receipt |
| Vesper | What should I make of this, and what should happen next? | Interpretation, judgment, orchestration, private work, and conversation | Strong agent and chat substrate; useful outputs do not always become manipulable or durable state |
| Places | What is my relationship to this place? | Place identity, evidence, saves, exploration, and return | Strong object pages and save truth; chat-to-Places handoffs currently require too many indirect steps |

`You` remains the authority for identity, preferences, memory, privacy, and
controls, but it does not need to be a fourth primary tab. Standalone shared
rooms are a collaboration state that may precede a Trip; they are not a fourth
top-level product.

The principal gap is therefore not “connect AI to every feature.” Vesper
already reaches many features. The gap is **explicit stateful connective
tissue**:

1. Vesper makes a bounded judgment.
2. The user can inspect or correct that judgment without writing a better
   prompt.
3. An explicit action creates or changes the smallest appropriate canonical
   object.
4. A receipt says what changed and who owns it now.
5. The user can return to that object later, including on a second occasion.

More model access without these steps would create more fluent seams, not
fewer seams.

### 17.2 What the pivotal loops do today

| Loop | Current entry and artifact | Correction/action | Canonical owner and receipt | Verdict |
| --- | --- | --- | --- | --- |
| Organic onboarding | Cover → forced `trip` or `dreaming` fork. Trip captures where/when/who; dreaming captures broad interest/pace and offers a diary. | Trip users may “talk it through”; dreaming users choose fixed signals. There is no visible first judgment to correct. | Trip path creates a Trip or private thread after auth. Dreaming routes into You/diary behavior and still invokes Atlas-era scan concepts. | Structurally careful handoff, strategically pre-pivot. It explains a planning app better than an ambient place-aware Vesper. |
| Vesper place recommendation | `venue_card` plus optional `RecommendationBlock`. | Chat card can open the venue; phone/deadline actions exist. Save, dismiss, compare, “more like this,” and add-to-Plan require another surface or another prompt. | Venue detail owns Save, Share, Add to plan, Book, and Ask Vesper. The write paths are real, but the chat projection does not show completion in place. | The ingredients are strong; the loop is indirect. |
| Group proposal | `vote_widget` in the canonical group room; Trips Home now routes to the exact message with `focus_proposal_id`. | Members vote; organizer can Apply to Plan or Keep current plan; authorized users can withdraw or revert where supported. | Accepted proposals apply through the canonical itinerary gateway and emit a durable `change_applied` receipt with diff/version/Plan handoff. | The reference closed loop. Preserve and copy its semantics, not necessarily its component. |
| Local occasion | Internal Trips doorway seeds a local request; backend supports `trip_kind=local`, local Plan projection, spatial context, outcomes, and second-occasion evidence. | Chat can shape the Plan; Local Plan screen can return to chat and later confirm/correct an outcome under internal flags. | Local Plan and private outcome models are canonical. P01–P04 tests exist. | A real dark vertical, not a speculative feature. The public entry and device proof are missing. |
| Standalone shared room | Human-led room chat, invite lifecycle, durable turns, event stream, ownership controls, and trip promotion exist on the convergence branch. | People can talk without invoking Vesper. The in-flight room-info work exposes a participant-safe shared brief derived from reviewed intent state. | Conversation is canonical before promotion; Trip becomes canonical after explicit promotion. | Promising pre-Trip collaboration substrate. The current golden test stops at invite/handoff, and the brief is in-flight rather than landed. |

Two testing facts matter:

- The focused current-state suites passed: 42 mobile tests across proposal,
  cross-surface, standalone-room, composed-card, receipt, and onboarding
  surfaces; 21 backend tests across blueprints, actions, proposal mutation,
  local occasions, transport, and local-Trip creation.
- Those passes do not certify the product loops. The main J05 Maestro flow
  still opens the older proposal-detail route, and the local-Plan device flow
  explicitly proves only the doorway and first seeded chat turn.

### 17.3 Strategy residue to repair before adding more artifact behavior

This is small work with high leverage because it prevents new code and tests
from treating retired concepts as authority.

| Residue | Current conflict | Required repair |
| --- | --- | --- |
| `atlas_draft` is active in `docs/contracts/chat-card-types.json` | Atlas is an accepted retired product surface | Stop active production, mark lifecycle deprecated then retired after checking durable rows, and preserve the historical text fallback |
| Atlas feature flags remain active in `docs/flags/registry.yaml` | The registry suggests future activation rather than retirement | Resolve or explicitly reclassify each Atlas flag; do not delete historical entries |
| J07 and J25–J28 plus README language still present Discover/Atlas as product surfaces | The J registry is allowed to preserve regression history, but its prose still reads as current IA | Rename current Place-owned behavior, label retained Atlas journeys historical/compatibility, and keep route-regression coverage separate from product proof |
| Product proof prose says P05–P07 are dark while `product-proofs.yaml` marks P06 active; P08 exists outside the spine table | Machine and human authorities disagree | Reconcile status and include P08 in the proof-spine index or explicitly keep it as a separately admitted dark proof |
| `app/(tabs)/_layout.tsx` still describes four bottom tabs | Visible IA has three roots | Correct the comment and any generated surface inventory that still counts hidden compatibility routes as roots |
| `docs/status/current-state.md` predates the convergence branch | Generated status understates shared-room and proposal work | Regenerate only after current branches land and evidence receipts are revision-bound |
| Production PostHog secret is unset according to the owner action ledger | Activation events can be correct in code and still be dropped | Configure the external secret before relying on an onboarding experiment; verify one non-content canary event end to end |

This is a reconciliation pass, not a deletion pass. Compatibility routes,
historical messages, and historical regression tests stay available until
their retention contract says otherwise.

### 17.4 Adopt a small responsibility grammar, not a universal card ontology

The grammar should classify why an artifact exists. Visual layout, domain
object, and lifecycle state remain separate dimensions.

| Responsibility | User need | Typical direct manipulation | Example canonical owner |
| --- | --- | --- | --- |
| Judgment preview | Understand Vesper's bounded recommendation and why | Open, save, reject this direction, ask for a nearby alternative | Place relationship or no write yet |
| Working set | Compare and progressively narrow a few options | Keep/remove, choose leaning, compare, request a changed constraint | Message-scoped state initially; Places save or proposal when committed |
| Decision gate | Know exactly what is proposed versus committed | Vote, approve, reject, withdraw, edit before apply | Proposal / booking / Trip-creation proposal |
| Execution state | Understand multi-step work and intervene safely | Pause, retry, review, continue | Workflow, research job, itinerary operation |
| Receipt and handoff | Verify what changed and where it lives | Open owner, undo/revert when allowed | Plan, Place relationship, booking, shared room |
| Recovery | Preserve work when state is stale, failed, or unauthorized | Retry, refresh, repair, choose a safe fallback | Original domain object plus error/recovery record |

Every artifact also needs five explicit attributes:

1. **audience** — private or group;
2. **lifecycle state** — suggested, active, awaiting decision, committed,
   superseded, failed, or expired;
3. **canonical owner** — none yet, conversation, Place relationship, Plan,
   proposal, booking, or outcome;
4. **permitted operations** — inspect, steer, mutate, confirm, revert, or open;
5. **return path** — where the same object can be resumed later.

`composed_card` should remain a validated native **composition carrier**. It
should not become the canonical object or absorb every specialized renderer.
The current v1 schema is intentionally private and read-only; mutation must not
be smuggled through its opaque action field. Specialized proposal and booking
components should remain specialized while they carry distinct authority and
failure semantics.

### 17.5 Execution principles

1. Close one complete vertical before consolidating renderers.
2. Use the group proposal loop as the semantic reference: exact object,
   authority, explicit state, canonical write, honest receipt, return.
3. Use existing Places saves and Plans before inventing a durable shortlist
   table.
4. Ask for authentication when persistence, personalization, or multiplayer
   requires it—not before the user can understand the offer.
5. Do not request location as an onboarding prerequisite. A tappable city or
   typed place can establish context; location can be requested at the moment
   it materially improves the answer.
6. “Not this” is a turn-level steer by default, not a permanent negative taste
   claim. Durable learning requires a separate explicit contract.
7. A screen capture proves visual presence and comprehension affordances; it
   does not prove a database mutation, authorization boundary, or AI quality.
8. Plain chat is the baseline. An artifact must reduce effort, improve
   comprehension/control, create reusable state, or support collaboration.

### 17.6 Phase 0 — settle the baseline and repair authority

**Goal:** make the accepted product direction, current branch, contracts, and
evidence registry agree before feature work begins.

**Sequence:**

1. Let the current `codex/conversation-convergence` work land or move the new
   work into clean worktrees based on its final commits. Do not edit the
   currently dirty conversation files in parallel.
2. Run the strategy-residue repairs in section 17.3 as explicit, small commits
   in the owning repository.
3. Update the card catalog with the responsibility grammar and an inventory
   field for role, lifecycle, canonical owner, producer, correction, receipt,
   and return path. Keep `chat-card-types.json` as the wire allowlist; do not
   turn it into a product ontology.
4. Configure and verify PostHog delivery before experiment assignment begins.
5. Capture revision-bound baseline receipts for the already-green focused
   contract/database tests. Do not promote a device or staging result from
   these local test runs.

**Exit gate:** one human-readable and one machine-readable authority agree on
active proof status, retired surfaces, and attachment lifecycle; concurrent
branches are no longer an ambiguous base.

### 17.7 Phase 1 — certify the reference loop on the current chat-first path

**Goal:** make J05 the calibration example for every later artifact loop.

**Mobile work:**

- Rewrite the primary proposal Maestro journey to enter Trips Home, tap the
  open-decision crown, land in group chat, locate the exact focused
  `vote_widget`, vote/resolve there, observe `change_applied`, open Plan, and
  exercise revert where the fixture authorizes it.
- Keep the direct proposal-detail route as compatibility/regression coverage,
  not as the primary user journey.
- Add assertions for proposed-versus-committed language, organizer/member
  permissions, stale state, double taps, and exact return after opening Plan.

**Backend work:**

- Retain the current proposal gateway, authorization, idempotency, apply, push,
  and durable receipt paths.
- Add no generic mutation resolver. Instead document this path as the worked
  example for a consequential artifact.

**Evaluation work:**

- Add an adversarial static trace using the existing “refute until proven”
  journey prompt.
- The oracle is proposal row + Plan diff/version + durable receipt + second
  reader agreement. A screenshot of “Decision applied” is supplementary.

**Exit gate:** the current chat-first route has contract, database, device-mock,
and—when the existing two-account prerequisite is repaired—staging evidence.

### 17.8 Phase 2 — run one more onboarding design iteration as a stateful loop

**Goal:** decide the smallest first-value interaction before writing the new
onboarding implementation.

The next Claude Design iteration should not generate more welcome screens. It
should render one complete state board using the accepted Vesper design
language already included in the onboarding brief:

1. organic entry with a composer plus four tappable starter fragments;
2. zero-typing selection of a local starter;
3. typed or tapped context clarification only if needed;
4. first bounded place judgment;
5. direct “keep / not this / compare” steering;
6. “Saved to Places” or “Added to local Plan” receipt;
7. Places or Trips owner screen;
8. later return/resume state.

Recommended starter set:

- **Somewhere good tonight** — local, time-bounded value;
- **A place someone sent me** — paste/share/deep-link entry;
- **Show a friend my city** — ambient and multiplayer without inventing a
  Trip;
- **I have a trip in mind** — preserves the strong travel wedge;
- composer — permits any other opening without making typing mandatory.

Prototype comparisons:

| Variant | Purpose |
| --- | --- |
| Current | Control: existing trip/dreaming fork |
| Hybrid single judgment | Tests whether one decisive recommendation creates earlier comprehension and value |
| Hybrid working set | Tests whether 2–3 options plus direct steering improve control without feeling like a form |

Do not prototype an unauthenticated live-agent backend yet. Capture intent
before auth, then request auth immediately before the first personalized live
response or canonical save. This preserves low perceived friction without
creating a second unauthenticated conversation system.

**Exit gate:** five to eight moderated or founder-led comparisons can answer
which artifact weight is understandable, which starter is compelling, whether
people know what Vesper does, and whether they know where the result went. This
is a design selection, not retention proof.

### 17.9 Phase 3 — implement the organic first-value vertical

**Goal:** a new organic user can reach a useful local judgment without typing,
correct it, create a canonical result, and know where it lives.

**Entry routing:**

- Preserve specialized priority: invite token → shared-room or Trip join;
  inbound Place/share link → exact Place context; explicit trip campaign/deep
  link → trip seed; ordinary organic launch → hybrid Vesper first-value flow.
- Reuse the current pre-auth draft/idempotency machinery in
  `app/onboarding.tsx`, `utils/onboardingIntent.ts`, and
  `utils/onboardingProgress.ts` rather than rebuilding auth handoff.
- Replace the generic dreaming/diary branch. Keep any photo-memory work behind
  an explicit later feature; do not present Atlas or a diary as the organic
  explanation of the product.

**Conversation handoff:**

- Introduce a small typed seed such as occasion kind, optional place/city,
  available time, companion posture, and free text. This is provisional input,
  not inferred permanent preference.
- After auth, create or resume the private ambient conversation using the
  existing durable pending-turn/idempotency path.
- The first assistant turn should return one bounded recommendation or small
  working set, not an essay followed by generic chips.

**First canonical action:**

- For a place-led opening, `Keep` writes through the existing Place save
  endpoint and changes the card to a query-backed “Saved to Places” receipt
  with an Open Places action.
- `Not this` records a message/turn-level steer and prepares a constrained
  follow-up; it must not silently write a negative global preference.
- `Add to plan` initially hands off to the existing venue detail/day picker or
  a review-first proposal. It must not bypass the itinerary gateway.
- A time-bounded occasion may promote into `trip_kind=local`; a general place
  save must not manufacture a local Plan or Trip.

**Required failures:** no city/location, denied location, no grounded candidate,
network loss after auth, save retry, stale venue, and app termination between
save and receipt.

**Exit gate:** P01 gains a real organic-entry device-mock anchor; the user can
complete the flow without typing; a relaunch resolves the saved state from
canonical Places truth.

### 17.10 Phase 4 — make place judgment steerable without creating a new subsystem

**Goal:** close recommendation → correction → Places/Plan for ordinary Vesper
turns, not only onboarding.

Recommended minimal implementation:

1. Extend `venue_card` for the one-place case with query-backed Save/Open and a
   structured turn-level rejection/alternative action.
2. Extend the existing comparison/option presentation for a 2–4 place working
   set. Each option carries a canonical venue id; the client does not execute
   model-authored routes or mutation payloads.
3. Use existing Places save truth as the first durable “keep.” A temporary
   working set remains message-scoped until usage demonstrates that a named,
   durable shortlist is valuable.
4. Keep `composed_card.v1` read-only. If interactive option items cannot be
   represented safely in the existing specialized cards, design a reviewed v2
   contract; do not loosen v1 validation in place.
5. Preserve the Venue detail page as the rich owner for Share, Book, Ask, and
   itinerary placement. The chat artifact should make the common first action
   immediate, not duplicate the full object page.

**Canonical receipt behavior:**

- Save → inline saved state derived from Places, plus Open Places.
- Unsave → explicit reversal, not a disappearing optimistic state.
- Add/propose to Plan → proposal or itinerary receipt, then Open Plan.
- Stale/deleted candidate → recovery state, no fallback to a generic root.

**Exit gate:** a J07 successor starts from Places or Vesper rather than
Discover, preserves typed Place context, supports one direct correction, and
ends in Places or a Plan with a verifiable receipt and return path.

### 17.11 Phase 5 — connect standalone rooms to the same object lifecycle

**Goal:** prove that human-led collaboration can gradually become a Plan
without Vesper dominating the room or leaking private context.

After the current room-brief work lands:

- Treat the participant-safe brief as a projection of reviewed shared intent,
  not a hidden model memory and not a replacement for the transcript.
- Decide through prototype whether its primary home is room info, a compact
  pinned chat projection, or both. Avoid showing the same large artifact twice.
- Add a golden journey: create room → invite/accept → ordinary human messages →
  optional Vesper invocation → inspect/correct shared brief → explicit Trip or
  local-Plan promotion → create/resolve proposal → Plan receipt visible to both
  members.
- Assert that the brief contains no private conversation, location, memory, or
  unreviewed inferred constraint.
- Measure Vesper participation and silence. A room that works only when the
  agent responds to every exchange fails the multiplayer thesis.

**Exit gate:** the standalone-room test no longer stops at invite handoff, and
the promotion boundary proves canonical ownership moves from Conversation to
Trip exactly once.

### 17.12 Phase 6 — migrate the attachment inventory by evidence

Do not mass-rewrite 20 types. Use the completed verticals to decide which
semantics repeat.

| Attachment | Preliminary disposition | Reason/gate |
| --- | --- | --- |
| `vote_widget` | Keep specialized | Consequential group authority and proposal lifecycle |
| `change_applied` | Keep; align with receipt envelope | Reference canonical mutation receipt |
| `booking_proposal`, `booking_confirmation` | Keep specialized | Provider, payment, expiry, and masking semantics |
| `trip_creation_proposal` | Keep specialized | Explicit Conversation → Trip promotion authority |
| `itinerary_operation` | Keep pending consolidation | Review/progress/receipt behavior remains domain-specific |
| `error_recovery` | Keep | Recovery is a first-class responsibility, not presentation noise |
| `narration` | Keep outside decision consolidation | Modality object, not a recommendation lifecycle |
| `venue_card` | Extend in the first vertical | Smallest useful Place judgment projection |
| `reaction_card` | Keep as an interaction primitive | It is not itself a lifecycle role; constrain what a reaction means |
| `trip_shapes` | Candidate working-set migration | Compare against the onboarding working-set experiment first |
| `comparison_card` | Candidate working-set carrier | Add canonical option ids and bounded operations only after contract review |
| `map_route` | Keep as preview/handoff | Spatial receipt and map owner have distinct evidence needs |
| `plan_ready` | Candidate receipt/handoff consolidation | Migrate only if Plan owner/version/return remain explicit |
| `taste_dna_reflection` | Keep until You-owned replacement is proven | Preference correction/provenance must survive migration |
| `notification_card` | Freeze new generic uses | It is a carrier, not a product responsibility; narrow producers over time |
| `document_edit` | Audit durable use, then deprecate or give one owner | Registry notes no dedicated backend writer |
| `lazy_research` | Deprecate active production | The current worker already has a bounded `composed_card` companion; preserve historical fallback |
| `atlas_draft` | Retire active production | Conflicts with the accepted Atlas retirement |
| `composed_card` | Keep as bounded composition carrier | Native validated blocks, never arbitrary generated UI or canonical state |

For every deprecation: query historical production rows, stop writers, mark
`deprecated`, verify fallback, then mark `retired`. Never remove the union arm
or renderer before the retention window is understood.

### 17.13 Telemetry and experiment contract

The current events are a solid mechanical base—exposed, tapped, action
started/committed/failed, and resolver outcomes—but labels and taps do not say
whether a loop closed.

Add content-free semantic context gradually:

- `loop_kind`: onboarding_local, place_decision, group_proposal,
  standalone_room_promotion;
- stable `loop_id` and `artifact_id` or privacy-safe hashes;
- `artifact_role`, `lifecycle_state`, `audience`, and `owner_kind`;
- stable `action_kind` rather than display copy;
- `canonical_write_kind` and success/failure/unchanged;
- `receipt_exposed`, `owner_opened`, `resumed`, and `second_occasion_used`;
- elapsed time from entry to first judgment, correction, canonical write, and
  owner open.

Never log chat text, place identity, private reflection, raw action refs, or
member context merely to make the funnel easier to debug.

Primary measures:

1. time and number of inputs to first bounded judgment;
2. zero-typing completion rate;
3. first correction success and accidental mutation rate;
4. percent reaching save, explicit reject, proposal, or applied Plan—not just
   card tap;
5. proposed-versus-committed comprehension;
6. owner-location comprehension (“where does this live now?”);
7. later resume of the same object;
8. second relevant occasion with less repeated input;
9. group contribution distribution and agent share of messages.

### 17.14 Efficient evaluation stack and environments

| Layer | Environment | What it should judge | What it must not claim |
| --- | --- | --- | --- |
| Schema/unit | Pure fixtures and mocks | Parsing, lifecycle transitions, capability matrices, rendering permutations | Real persistence, auth, realtime, or AI quality |
| Contract/device-mock | Expo mock with deterministic fixture | Navigation, interaction availability, optimistic/error states, visual hierarchy, proposed/committed comprehension | Backend mutation or cross-account convergence |
| Database/persona replay | Local Postgres + Qdrant where required, deterministic/replay AI | Authorization, idempotency, canonical writes, invalidation, receipts, privacy, second-occasion provenance | Production provider behavior or physical-device usability |
| Staging | Isolated seeded accounts, cloud DB, real HTTP/SSE/push/auth; providers only where the proof requires them | Multi-account convergence, deep links, auth detours, push, deployment config, provider freshness | Broad desirability or retention |
| Physical | Internal build on real device, against an explicitly named mock/staging profile | Keyboard/composer feel, card density, scroll focus, permission timing, notifications, accessibility, return | Database truth unless paired with a backend receipt |
| Production dogfood | Opt-in people plus privacy-safe telemetry | Actual openings, completion, return, silence, second occasion | Causal product success from tiny uncontrolled samples |

Agent review should be deliberately strict:

1. deterministic assertions decide facts first;
2. an agent reads the actual response, screenshot, and state diff against an
   explicit positive and negative oracle;
3. missing or ambiguous evidence is `UNRUN`/`BLOCKED`, never a soft pass;
4. the agent must cite the artifact or file that supports each verdict;
5. humans judge residual taste, agency, comprehension, and felt value;
6. a second judge is reserved for high-consequence disagreement, not run on
   every trivial state.

Screenshots answer “is the state visible and understandable?” Response reads
answer “did Vesper make a grounded, bounded judgment?” Database/API receipts
answer “did the intended state actually change?” No one evidence type replaces
the others.

### 17.14a Implementation follow-through — 2026-08-12

The following safe slices have now been implemented in isolated
`feat/artifact-loop-execution` worktrees. This record deliberately separates
code landed on those branches from evidence that still needs a real device,
backend fixture, or production configuration.

| Slice | Implemented result | Verification completed | Still not claimed |
| --- | --- | --- | --- |
| Authority / retired Atlas draft | New server tool selection no longer offers `atlas_draft`; historical rows retain a renderer and deprecated contract state. | Backend selector and card-allowlist tests; generated app contract sync. | Historical-row retention-window decision and production query. |
| J05 reference path | Primary Maestro path starts from Trips Home and reaches the group-chat vote widget before observing the applied result. | Maestro structural validator and focused J05/J06 Jest coverage. | Two-account/device and staging evidence. |
| Artifact telemetry | Every attachment receives a content-free role, lifecycle, and owner; raw action labels are reduced to a small approved vocabulary. Canonical writes and owner opens are now explicit events. | Focused telemetry/privacy tests and TypeScript. | PostHog production secret, canary delivery, experiment assignment, and aggregate analysis. |
| Organic first-use shell | The post-cover screen is now a composer plus four starters. A starter or voluntary typed thought is stored as an `ambient` handoff, survives sign-up, and opens the existing private Vesper thread. No new pre-auth agent, city claim, Place, or Trip is fabricated. | Onboarding intent, retry, zero-typing, typed-context, TypeScript, and Maestro-reference tests. | The post-auth grounded judgment/replay fixture, first correction, and device visual comparison. |
| Chat venue action closure | A venue recommendation can save through the canonical save gateway, renders `Saved to Places` only after success, and exposes a Places-owner return. Detail navigation remains available. | Venue-card, save-hook, telemetry, and TypeScript tests. | A first-class `Not this` steer, review-first add-to-plan path, relaunch proof, and local-Plan graduation. |
| Standalone room promotion | Reviewed current code rather than rewritten: transcript-native proposal confirmation already carries `trip_kind`, reconciles lost responses from the canonical conversation read, pivots ownership before refresh, and has local-kind tests. | Existing card and promotion-hook tests rerun. | Two-reader result receipt and staging/device certification. |

The implementation branches are intentionally not auto-landed into dirty
primary worktrees. Landing must wait until concurrent design/doc work is ready
for a fast-forward or an explicit integration review.

### 17.15 Proposed commit/PR sequence

Each slice should be independently reviewable and should use explicit file
staging because concurrent sessions are normal.

1. **Workspace authority repair:** retired-surface language, proof-status
   reconciliation, card lifecycle, flag registry, and current-state generation.
2. **Mobile J05 route evidence:** chat-first focus, resolve, receipt, Plan open,
   and stale/revert Maestro coverage.
3. **Cross-repo telemetry contract:** semantic action/owner/receipt fields,
   PostHog canary, and privacy tests.
4. **Design-only onboarding decision:** complete state board and selected
   single-judgment versus working-set variant.
5. **Mobile onboarding shell:** starter panels + composer + existing auth/draft
   handoff; no backend behavior change yet.
6. **Backend first-value turn:** typed seed, private durable conversation,
   grounded local judgment, replay fixture, and failure behavior.
7. **Place action closure:** Save/steer, query-backed receipt, Places return,
   local Plan handoff where explicitly requested.
8. **Standalone-room closure:** safe brief after the current work lands,
   explicit promotion, proposal loop, and two-reader receipt.
9. **Attachment deprecations:** `atlas_draft`, redundant `lazy_research`, then
   only the types whose replacements have production-equivalent evidence.
10. **Experiment and promotion:** device-mock → database/replay → isolated
    staging → small production dogfood; promote only revision-bound receipts.

Do not combine the onboarding shell, a generic card rewrite, proposal changes,
and Atlas deletion in one branch. Their failure domains and rollback needs are
different.

### 17.16 Definition of done for a closed artifact loop

A loop is closed only when all of these are true:

- the entry preserves acquisition intent and auth/deep-link state;
- the artifact states its responsibility, audience, lifecycle, and owner;
- the user can perform the primary correction without composing a new prompt;
- any write uses the canonical domain gateway and is idempotent;
- proposed, working, committed, superseded, and failed states are visibly
  distinct;
- a receipt says what changed, what did not, and where it lives;
- the owner surface resolves the same state after relaunch or from another
  authorized member;
- a negative oracle proves no privacy leak, fake success, duplicate write, or
  stale action;
- telemetry records semantic progress without private content;
- required evidence exists at the layer named by the existing P/J registry;
- a later session can resume the object; for the product thesis, a second
  occasion can use permitted prior evidence with less repeated work.

### 17.17 Recommended immediate move

The next implementation should **not** begin with a card-system refactor. Once
the current conversation-convergence work settles:

1. repair the small authority inconsistencies;
2. make the current group chat decision loop the fully certified reference;
3. run the stateful onboarding design comparison;
4. build one place-led organic vertical from starter → judgment → correction →
   Save to Places → return;
5. then generalize only the lifecycle semantics that repeat.

This is the shortest path from a group of strong features to a coherent
product: prove one ambient first-value loop, reuse the already-strong
decision/receipt spine, and let the shared grammar emerge from working
verticals rather than from a speculative universal component.
