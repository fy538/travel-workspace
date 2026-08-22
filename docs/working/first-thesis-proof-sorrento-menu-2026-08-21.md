---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-21
expires: 2026-09-20
why_new: Shapes a bounded personal-doorway evidence program and reference integration slice for immediate utility, custody, capability, and optional continuity across both child repositories.
promotes_to: null
source_of_truth_for: [personal-doorway-evidence-program]
supersedes: []
---

# Personal Doorway Evidence Program: A Menu Becomes a Doorway

## Bet

When a person asks Vesper about an imperfect menu photograph in a real place,
Vesper can answer the practical question immediately, open one grounded way of
noticing the place, preserve uncertainty and agency, and withdraw. If the
person explicitly keeps part of the interaction, it can improve one later
occasion without becoming a permanent taste label.

This proof is deliberately narrower than the company thesis and longitudinal
product simulation. It investigates the personal doorway, custody, capability,
and optional-continuity path. It tests multiplayer safety around companion
context, but it does **not** prove differentiated multiplayer value. It is one
high-leverage evidence program and reference integration slice. It neither
defines nor gates the generalized architecture for capture, memory, Occasions,
proactivity, or multiplayer, and it cannot establish the whole thesis alone.

## 1. Why this proof is high-leverage

The scenario tests three product promises directly and one multiplayer safety
boundary:

| Promise | Observable behavior |
|---|---|
| See more | One source-bound cultural, culinary, or regional distinction changes what the person can notice. |
| Live it well | The answer helps the person order, ask a better question, or avoid a practical mistake now. |
| Carry it forward | Retention is optional; if kept, the prior attention changes a later answer or action. |
| Multiplayer safety boundary | Companion context remains bounded; sharing later does not retroactively create shared memory. This is not yet proof that Vesper improved a shared experience. |

It also has a low consequence ceiling. Vesper can deliver value without booking,
location tracking, Plan creation, public content, or group mutation. That makes
it a cleaner value test than a fully operational ferry/proposal-day scenario.

The adjacent [Rome Couple Evening proof](second-thesis-proof-rome-couple-evening-2026-08-22.md)
must test whether two people's distinct perspectives and current states produce
a better shared outcome. The menu proof must not be stretched to stand in for
that evidence.

## 2. Person and situation

Fei is having dinner in Sorrento with his girlfriend. He opens the Vesper
composer, takes an imperfect photograph, and asks:

> What are these two dishes? Is either one especially Sorrentine?

He wants help now. He has not agreed to journal, create a Plan, identify the
restaurant, contribute public content, or teach a taste profile.

## 3. The capability delta

Success is not “the OCR was correct.” The intended delta is:

- before: the menu is partially illegible or culturally opaque;
- after: the person can distinguish the dishes, make a more informed choice,
  notice one locally meaningful distinction, or ask a better question; and
- then: Vesper leaves attention with the meal and companions.

The smallest successful response has three layers:

1. **Literal:** what the relevant words say.
2. **Practical:** what the dishes likely are and what uncertainty matters.
3. **World-opening:** at most one grounded distinction worth noticing here.

It must not manufacture personal meaning, recite a travel essay, or turn the
answer into a retention prompt before utility arrives.

## 4. Assumptions to test before production migration

| Assumption | Risk | Cheapest test | Pass signal |
|---|---|---|---|
| A situated opening is more valuable than generic OCR/translation. | Value | Compare concise translation-only and layered responses with prospective users. | The person can name what the extra layer changed in perception or choice. |
| One opening feels illuminating rather than performative. | Usability/mediation | Observe reading and interruption in a live or realistically staged meal context. | The person engages or moves on without feeling assigned homework. |
| Uncertainty increases trust without making the response cumbersome. | Trust | Deliberately use ambiguous or imperfect menu photographs. | The person can tell what is known, likely, and worth asking staff. |
| A small non-retention receipt is reassuring rather than distracting. | Agency/usability | Show it after the answer, never before. | The person understands what was retained without losing the conversational flow. |
| Some interactions deserve continuity, but most should expire. | Value/ethics | Offer keep/delete only after value and ask why the person chooses. | “Keep” reflects a future use, not guilt or collection instinct. |
| Prior attention can improve a later judgment without becoming a profile label. | Longitudinal value | Replay a second coastal menu or cooking moment. | The later answer is more precise or needs less explanation and cites the earlier source. |

### Discovery appetite

Use a maximum of five working days and 5-8 prospective users for the first
research round. Use the current composer vision path, a scripted prototype, or
a human-in-the-loop response; this study does not require new schema. Its timing
neither blocks nor authorizes the systematic architecture program, which is
governed by the full behavior portfolio and cross-journey invariants.

Record:

- the original question and source quality;
- time to useful answer;
- literal/practical errors;
- the opening offered;
- what the person noticed, asked, chose, or rejected;
- whether the response competed with companions or the place;
- whether retention was wanted and why; and
- the person's language for the value, not only a satisfaction score.

## 5. Current implementation trace

### Composer path

```text
ComposerBar
  -> useConciergeHomeConversationEntry.startConversationWithImages
  -> pending chat turn contains inline image payload
  -> conversation session writes message + chat_images
  -> the model receives the image and answers immediately
  -> optional inbound_screenshot tool copies it into legacy inbound processing
```

Strength: immediate conversational value already exists.

Weaknesses:

- the raw image is not admitted through intake-v2 custody first;
- persistence is best-effort and conversation-specific;
- the optional tool rehosts/reinterprets the same image through the legacy
  inbound pipeline;
- the current answer and later artifact candidate do not share one source
  identity; and
- expiry, correction, and deletion are not composed into the answer receipt.

### Share-sheet path

```text
share-capture
  -> intake-v2 submission
  -> secure upload / scan / finalize
  -> normalization and semantic interpretation
  -> source-bound artifact candidate
  -> confirm / reject / delete
```

Strength: this is the right trust and custody boundary.

Weaknesses:

- it does not answer the user's practical question;
- the user note/question is not part of the semantic interpreter's immediate
  job;
- its classification prompt is artifact-oriented rather than designed for a
  concise world-opening response;
- `Done` returns to Trips, encoding the older product center; and
- confirmation copy can imply a durable private Thread that does not exist.

### Existing later-loop support

Plan Shape, Occasion capsules, contextual-value fixtures, occurrence/outcome
models, and second-occasion tests provide strong contracts. They are not yet a
production menu loop and should not be made prerequisites for the immediate
answer.

## 6. Reference integration slice

This slice should conform to the accepted cross-portfolio architecture and make
one path concrete. It must not become the source from which the ontology is
inferred or the gate that prevents other journey families from being designed.

```text
Vesper composer
  -> one image + question
  -> intake-v2 creates owner-scoped source envelope
  -> upload, scan, and verify
  -> pending personal turn references submission + source object
  -> conversation reads the admitted source and answers
  -> small exact receipt
       answered
       source retention/expiry
       no Place, Plan, Occasion, or memory created
  -> optional delete or keep interpretation
  -> canonical readback of the actual consequence
```

This is a branch-by-abstraction migration. The old inline-image/chat-image path
remains the fallback until admitted-source history rendering, retry, and latency
are proven. Once all consumers read the admitted source reference, delete the
duplicate raw-source ownership and the legacy screenshot re-ingestion tool.

## 7. Product behavior contract

### 7.1 Before the answer

- The person takes/selects a photograph and writes a normal question.
- No workflow, artifact type, Place, Occasion, or retention classification is
  requested.
- A compact “receiving securely” state may appear only for the time required to
  admit the source.
- If custody fails, the question and local image draft remain recoverable for a
  retry; the UI does not imply the source was retained.

### 7.2 The answer

The answer:

- addresses only the relevant menu items;
- separates translation from interpretation;
- marks ambiguous OCR or dish identification;
- uses coarse Place context only if authorized and material;
- offers no more than one grounded opening;
- gives an immediately useful next question or choice when appropriate; and
- ends without an engagement hook unless the person asked for more.

Illustrative structure, not final copy:

> **Scialatielli ai frutti di mare** is thick local pasta with mixed seafood.
> **Gnocchi alla sorrentina** is baked gnocchi with tomato, mozzarella, and
> basil; that is the more specifically Sorrento-linked dish. The seafood mix
> varies, so ask about shellfish if that matters.
>
> One thing to notice here: a creamy texture may come from emulsifying pasta
> water and fat rather than cream.

### 7.3 The receipt

For the default ephemeral path:

```text
Answered · original expires within 24 hours
No Place, Plan, Occasion, or memory created
[Delete now]
```

If policy or the owner retains the source, use the exact owner and duration.
Do not say “thread,” “memory,” “Encounter,” or “part of your world” until such an
object really exists and can be opened, corrected, and deleted.

### 7.4 Optional continuity

Continuity is offered after utility, quietly and only when the interaction has a
plausible future use:

```text
Keep this distinction with the source?
[Keep] [Let it expire]
```

For the first production slice, one of two honest outcomes is acceptable:

1. retention remains an intake-owned confirmed interpretation with precise
   copy; or
2. a typed, source-bound private Encounter/cue is created through a named domain
   writer with correction and deletion.

Do not introduce a generic Thread aggregate merely to satisfy the copy.

### 7.5 Sharing and companions

- Companion presence may improve tone or practical framing only when known
  through authorized context.
- A private source and interpretation do not become shared because another
  person is physically present.
- Sending the answer to a friend shares exactly that message or projection; it
  does not grant access to the underlying source or create a shared Occasion.

## 8. Authority and truth matrix

| Claim/action | Default authority | Required evidence | Forbidden shortcut |
|---|---|---|---|
| Read visible menu text | Advise | Source image region | Treat OCR as verified restaurant truth. |
| Explain a dish | Advise | Source text plus grounded public source/model knowledge | Present a disputed regional claim as settled. |
| Use current city/area | Advise | Authorized fresh location or explicit conversation context | Infer exact restaurant from a menu image alone. |
| Infer restaurant candidate | Candidate only | Menu name, reservation, location/time, or explicit confirmation | Auto-create canonical Place. |
| Infer occurrence | Unknown/plausible by default | Fused time, place, dwell, reservation, and conversation evidence | Treat photograph as attendance. |
| Retain original | Policy/owner | Explicit retention mode and expiry | Hide indefinite retention behind “keep.” |
| Create private continuity | Owner-confirmed | Source-bound candidate and named writer | Let model-granted capability write memory. |
| Share with companion/group | Explicit | Audience choice and group authority | Use physical co-presence as consent. |
| Create Plan/commitment | None in this proof | Explicit or provider-backed commitment | Convert a dining image into a Plan. |
| Send push later | None in first slice | Separate interruption-value proof | Treat retained content as notification consent. |

## 9. Engineering work packets

### Packet A — human-value prototype

**App/code:** no required production changes.

**Deliverables:** response rubric, 5-8 sessions, evidence register, decision to
proceed/reshape/stop.

**Exit:** situated layer demonstrates a capability delta beyond generic vision
Q&A.

### Packet B — admitted-source conversation seam

**Primary surfaces:**

- `travel-app/components/chat/ComposerBar.tsx`
- `travel-app/hooks/useConciergeHomeConversationEntry.ts`
- `travel-app/data/inboundItems.ts`
- `travel-agent/backend/api/routes/intake.py`
- pending-chat-turn transport and conversation admission
- conversation image/source read adapter

**Change:** upload through intake v2 and bind identifier-only source references
to the pending personal turn. Keep the inline image implementation behind a
fallback flag.

**Non-goals:** multiple files, group conversations, audio, email, camera roll,
Place matching, Occasion creation, and new model orchestration.

**Exit:** idempotent resume after app/background/network interruption; verified
source is the image used by the answer and by later correction.

### Packet C — world-opening response contract

**Change:** add a bounded evaluation contract for literal, practical,
uncertainty, one opening, and withdrawal. Reuse the existing conversation model
path; do not create a second “world-opening agent.”

**Evidence:** a small menu corpus with clean, ambiguous, non-menu, allergen,
privacy-sensitive, and unsupported-regional-claim cases. Human review remains
required because rubric conformance does not prove value.

**Exit:** no fabricated ingredient/allergen certainty, no more than one opening,
and answer remains useful when Place is unknown.

### Packet D — exact receipt and correction

**Primary surface:** the conversation turn and/or a compact source receipt, not
a new root.

**Change:** show custody status, retention/expiry, actual consequence, delete,
and correction. Remove the inaccurate private-Thread copy in share capture.

**Exit:** every action reads back from the canonical owner; deleting the source
does not falsely claim deletion until recorded.

### Packet E — optional consequence

Start only after Packets A-D pass.

**Change:** either keep the precise intake-owned interpretation or route one
`propose_encounter` consequence through a named private Place/relationship
writer. Generic intake proposal acceptance without domain application is not a
finished path.

**Exit:** accepted, rejected, corrected, separated, and deleted states have
canonical readback and no Plan/group side effects.

### Packet F — second occasion

Start as a separate bet.

**Scenario:** another coastal menu or a later cooking moment makes the earlier
regional/technique distinction materially relevant.

**Change:** the contextual engine may select an in-conversation application or
Silence. No push in this packet.

**Exit:** receipt cites prior source/evidence and says what changed in the
current judgment. “Content resurfaced” is insufficient.

## 10. Acceptance gates

### Deterministic contract

- one admitted source identity survives custody, conversation, correction, and
  deletion;
- retries do not duplicate submissions, messages, or consequences;
- the model cannot self-grant retention, sharing, Plan, or memory authority;
- an image alone never marks occurrence or creates a Place/Occasion;
- source deletion and derived-record behavior follow the declared policy;
- the fallback path remains usable during migration; and
- generated API types and operation governance remain synchronized.

### Model/evaluation

- answers the user's stated items and question;
- distinguishes literal text, inference, and broader interpretation;
- names consequential ambiguity;
- avoids unsupported allergens, ingredients, and regional certainty;
- offers zero or one grounded opening;
- does not demand reflection, rating, or retention; and
- remains useful with no location permission.

### Device

- camera and library entry;
- background/resume during upload and answer;
- slow/failing network;
- source rejected/quarantined;
- app killed after admission but before conversation navigation;
- delete and retry;
- accessibility and long-text behavior; and
- answer latency measured from send to first useful content.

### Human outcome

At least a majority of the small discovery cohort should demonstrate a concrete
capability delta in their own words or behavior. No more than a minority should
describe the opening as distracting, generic travel prose, or pressure to
perform meaning. These are shaping thresholds, not statistical launch claims.

## 11. Failure and kill criteria

Stop or reshape the bet if:

- users mainly want generic translation and the situated layer adds no observed
  value;
- the world-opening layer repeatedly competes with the meal or companions;
- accurate and sufficiently fast responses require an uneconomic provider or
  editorial pipeline at the wedge scale;
- custody admission makes first useful answer materially too slow and no
  streaming/direct-upload design resolves it;
- users cannot understand whether their source was retained;
- continuity requires broad identity inference rather than source-bound
  evidence; or
- the second occasion feels like engagement resurfacing rather than better
  judgment.

Failure should retire or reshape the solution, not weaken the thesis invariants
around evidence, privacy, and agency.

## 12. Boundaries of this evidence program

- no new root tab;
- no generic camera or camera-roll product;
- no automatic restaurant check-in;
- it does not decide whether the portfolio requires a generalized Occasion
  lifecycle or a full Plan Shape cutover;
- no group sharing by default;
- no public contribution flow;
- no generated personal narrative or taste label;
- no notification or anniversary reminder;
- no booking or menu-order transaction;
- no autonomous restaurant contact;
- no full Atlas/Discover retirement in this bet; and
- it neither authorizes nor prohibits a separately decided repository-wide
  migration or architecture program.

## 13. What this proof can support

If successful, it supplies human evidence for the following product and release
moves. Architecture authority remains separate:

1. support making intake v2 the canonical source boundary for conversational
   images once implementation-conformance checks also pass;
2. support retiring the duplicate legacy screenshot ingestion path after its
   consumers are migrated;
3. establish evidence that Vesper can be a credible first-use doorway beyond
   Plan creation;
4. test whether a source-bound private Encounter/cue creates useful continuity;
5. give the contextual engine one real producer and surface consumer;
6. contribute one result to the broader second-occasion evidence program; and
7. support onboarding language such as “ask or bring something” if observed
   value generalizes.

If it fails, the custody, evidence, correction, and silence foundations remain
valuable. That is why this is a good bounded bet: the experiment is narrow, the
learning is high, and the durable substrate does not depend on a positive
result. It is a good bounded evidence program, not the product architecture's
first or controlling bet.
