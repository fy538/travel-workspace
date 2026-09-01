---
doc_type: working
status: active
owner: product / design / engineering
created: 2026-08-31
last_verified: 2026-09-01
expires: 2026-09-30
why_new: Converts the accepted Life behavior rulings into a bounded handoff for the next design and implementation phase.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md
---

# Life Next Behavior Prototype Handoff

**Date:** 2026-08-31  
**Audience:** Claude Design and Claude Code  
**Status:** Working handoff for the next Life design/prototype phase  
**Design project:** `/Users/feihuyan/Downloads/vesper-life-anchors`  
**Workspace:** `/Users/feihuyan/travel-workspace`

## Executive decision

The philosophical foundation of Life is sufficiently resolved. Do not begin
another broad exploration of root metaphors, visual themes, cards, Pass
variants, Return families, or dossier organs.

The next phase tests **behavior**, not more grammar.

Life's working promise is:

> **A person's life becomes more findable, intelligible, and useful over time
> without requiring them to maintain a journal, construct a profile, or turn
> living into homework.**

The cross-surface relationship is:

```text
Chat receives, answers, shapes, and corrects with minimal friction.
Life preserves the governed record and its durable addresses.
Vesper recompiles eligible evidence when a material reason exists.
Home and Places deliver present-tense value.
Chat, Plan, and Occasion may shape or apply an optional consequence.
Life receives a causal receipt only when something materially changed.
```

The performed real-photography composition is **tabled**. The photography law
may remain adopted and the visual proof explicitly pending. It is not a gate
for the four workstreams in this handoff.

The next four workstreams, in priority order, are:

1. **Together as a complete consumer experience**
2. **Human refinding as an interactive experience**
3. **Return arbitration and scarcity**
4. **One contribution through its complete lifecycle**

Together and refinding may begin in parallel. Return arbitration should use
their concrete results. The contribution lifecycle should then integrate the
whole product loop rather than inventing a fifth grammar.

## 1. What is settled

The following decisions are inputs, not open questions.

### 1.1 Life's role

Life is the durable continuity layer of Vesper. It is not:

- a scrapbook;
- a journal the person must maintain;
- a quantified-self dashboard;
- a social profile;
- a personality dossier;
- an ingestion inbox;
- a recommendation feed;
- a second Home;
- a records-management product in consumer language; or
- an AI-written autobiography.

Life should feel like:

> **My life, held without being frozen.**

The emotional contract is:

> **Recognized, not analyzed. Held, not judged. Connected, not categorized.
> Useful again, without becoming homework.**

### 1.2 One corpus, four lenses

Time, Places, Threads, and People are perspectives over one governed corpus,
not four databases and not one product grammar per tab.

```text
                         one governed life
                                |
              +-----------------+-----------------+
              |                 |                 |
            Time              Places            People
              |                 |                 |
              +-------------- Threads ------------+
```

A Journey, Occasion, Artifact, Place relationship, or shared episode may be
entered through several lenses without acquiring several owners. Correction
of the governed state must reconcile every projection.

### 1.3 Stable record versus Return

- A **record** states what exists, what happened, what remains supported, and
  where it came from.
- A **Return** uses governed material to provide value again.
- An **Opening** is one possible Return: a grounded possibility available now.
- A Return may instead be a reconstruction, explanation, comparison,
  juxtaposition, or experiential re-entry that ends on view.
- Ignoring a Return creates no task, debt, negative signal, or preference.
- Repeated viewing and dwell do not become identity evidence.

Life may deliver record-native understanding, reconstruction, and re-entry.
Present-tense possibilities belong primarily to Home or Places. Chat, Plan,
and Occasion own shaping and commitment. Life preserves foundation, lineage,
and any later receipt.

### 1.4 Contribution and authority

Value precedes classification or continuation work.

Every durable or external consequence independently resolves:

1. **Use**
2. **Retention**
3. **Inference**
4. **Audience**
5. **Action**

`Addressed to you` establishes audience only. It does not silently grant
retention, inference, operational reuse, resharing, persistence, or action.

### 1.5 Social philosophy

The social unit is an attributed contribution or governed shared episode, not
a post competing for attention.

- Shared occurrence may converge.
- Human contribution lanes remain attributed.
- Personal and relational Outcomes remain separately authored.
- Being in one Occasion never merges private meaning.
- People must not be ranked by inferred closeness or intimacy.
- Withdrawal removes or recompiles every dependent projection without leaving
  a substitute paraphrase.
- Blocking and later unblocking do not silently restore grants.
- No reply is required merely because another person's material became useful.

### 1.6 Absence is not an ask

No prototype may use:

- completion meters;
- missing-item prompts;
- mandatory filing;
- “finish this memory” language;
- automatic reflection questions;
- Thread closure chores;
- social response debt;
- empty Return placeholders; or
- maintenance badges.

Thin records remain short. Correct silence remains silent.

## 2. Governing references

Read these before producing new boards or code recommendations:

1. `docs/working/life-anchors-fresh-design-audit-and-correction-brief-2026-08-30.md`
   - especially Sections 17 and 18;
2. `docs/working/life-root-production-spec-2026-08-30.md`;
3. `docs/decisions/2026-08-30-adopt-life-consumer-anatomy.md`;
4. `docs/systems/contribution-and-consequence.md`;
5. `docs/working/life-refinding-query-benchmark-2026-08-29.md`;
6. `docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md`;
7. `docs/working/life-object-and-lens-fixture-pack-2026-08-29.md`;
8. `docs/working/life-canonical-post-return-new-york-experience-manuscript-2026-08-29.md`;
9. the current authority map and canonical boards in
   `/Users/feihuyan/Downloads/vesper-life-anchors/project`.

When the design project conflicts with the production spec, the production
spec wins. When the production spec conflicts with the correction brief, the
correction brief wins until the documents are reconciled explicitly.

Treat historical, rejected, tabled, and exploration boards as provenance, not
implementation authority.

## 3. Operating model for Claude Design and Claude Code

The two agents should work from the same fixtures but answer different
questions.

### 3.1 Claude Design owns

- complete consumer behavior and composition;
- what appears before and after an interaction;
- hierarchy, density, wording, state changes, and navigation continuity;
- how authority and uncertainty become understandable without ontology
  lessons;
- the difference among mine, theirs, shared, generated, and current-world;
- the optionality of Continue paths;
- honest absence, failure, withdrawal, and degradation states; and
- prototype-level interaction between canonical surfaces.

Claude Design must create complete experiences, not another collection of
component options.

### 3.2 Claude Code owns

- repository and implementation-feasibility investigation;
- current object, API, state, writer, read-model, and causal-lineage mapping;
- identifying reusable substrate versus non-conforming seams;
- renderer-neutral fixture and projection-envelope contracts;
- deterministic state transitions and test oracles;
- feasibility risks that should change the design before implementation;
- proposed prototype seams and isolated implementation slices; and
- eventual native prototype work only after a founder checkpoint authorizes
  it.

Claude Code must not turn the current design project into a repository-wide
noun migration or generalized architecture rewrite.

### 3.3 Shared responsibilities

Both agents must preserve:

- the same fixture identities;
- source roles and occurrence truth;
- authorship and audience;
- the five authority axes;
- one canonical owner per material consequence;
- causal dependencies across projections;
- reason-for-surfacing and freshness;
- correction and withdrawal behavior;
- no-work, no-debt, and correct-silence states; and
- vocabulary consistency with the authority map.

Neither agent may mark a workstream `DONE`. Use:

- **Architecture resolved**
- **Projection modules composed**
- **Consumer flow proven at fixture scale**
- **Canonically integrated**
- **Implemented**
- **Shipped**

These are distinct claims. Authority status, design maturity, and
implementation status should not be collapsed into one ladder.

## 4. Shared fixture portfolio

Use a small controlled portfolio so differences among workstreams remain
visible.

### F1 — Nice to Rome Journey

- Returned August 27, 2026.
- Chapters: overnight flight, coast, Rome, rerouted return.
- Evidence includes passes, booking mail, photographs, conversations, Place
  relations, and occurrence corrections.
- The pasta question remains nested and answered as far as it asked.
- The Aeneas question is a separate qualifying line of attention.

### F2 — Brooklyn dinner Occasion

- Feihu hosts Maya and Alex.
- Maya contributes a dessert statement and a table photograph.
- Alex contributes a receipt.
- Shared occurrence may converge.
- Each person retains separate private Outcomes.
- One shared reconstruction may exist from shared-core evidence.
- One private return may additionally use Feihu-private state.

### F3 — Rome and Paris

- Feihu's Rome heat note and route evidence remain his lane.
- Maya's Paris heat note and fountain-loop evidence remain her lane.
- Maya explicitly addresses bounded material to Feihu.
- Any operational use requires a scoped use/inference grant in addition to
  audience.
- The comparison is not consensus and creates no intimacy claim.

### F4 — Ordinary New York week

- Dinner, a book, a call, a bakery, running shoes, and an ordinary Saturday.
- No travel requirement.
- No forced Return.
- Useful refinding remains possible.
- Register stays casual; the app does not manufacture significance.

### F5 — Incomplete-cue refinding

- “The bar after meeting Teodora.”
- “What did Alex bring to dinner?”
- “The flight that got cancelled.”
- “That pasta place in Sorrento.”
- “The photograph from the ferry.”
- “The book Maya mentioned.”

### F6 — Contribution inputs

- a restaurant photograph;
- a movie ticket;
- a voice observation;
- a friend's addressed note;
- a forwarded booking email; and
- one Ask using a Source that should not persist.

## 5. Workstream A — Together as a complete consumer experience

**Priority:** 1  
**Primary owner:** Claude Design  
**Code partner:** Claude Code  
**Suggested board family:** `17 Together Consumer Arc`

### 5.1 Question

What does it feel like for another person's contribution and a shared episode
to enrich Life without becoming a social feed, a shared database, inferred
intimacy, or governance homework?

### 5.2 Required end-to-end arc

```text
Maya deliberately addresses a bounded Paris contribution to Feihu
  -> immediate value appears without filing work
  -> Shared with Maya gains an attributed contribution
  -> an eligible relational composition becomes visible
  -> a scoped grant optionally permits a private Home projection
  -> Feihu may reply, contribute, or do nothing
  -> a Brooklyn dinner adds shared occurrence and separate contribution lanes
  -> the shared record becomes richer without merging private Outcomes
  -> Maya narrows or withdraws one contribution
  -> every dependent projection reconciles without leaking a paraphrase
  -> independent history remains
```

### 5.3 Claude Design deliverables

Compose one navigable consumer prototype containing:

1. **People root at rest**
   - substantial enough to open;
   - no relationship ranking;
   - no ambient friend-status feed;
   - clear distinction among shared records, addressed contributions, and
     people merely encountered.
2. **Shared with Maya**
   - first scroll answers why this shared record is worth opening now;
   - “your account,” “Maya's contribution,” and “held in common” are legible
     without displaying the ontology;
   - shared episodes, contribution lanes, governed sources, and relational
     Returns have different visual roles.
3. **Addressed contribution arrival**
   - immediate value before any retention or classification request;
   - author, audience, purpose, and expiry understandable;
   - no notification or reply debt merely because it arrived.
4. **Brooklyn dinner shared episode**
   - shared occurrence;
   - Maya's photograph;
   - Alex's receipt;
   - separate private Outcomes;
   - one shared reconstruction that uses shared-core evidence only.
5. **Optional reply or contribution**
   - human-authored reason to respond;
   - Chat continuation receives the relevant envelope;
   - nothing is sent, persisted, or expanded without authority.
6. **Withdrawal and narrowing**
   - the affected comparison and snippets visibly recompile;
   - independent material remains;
   - no substitute paraphrase leaks the withdrawn lane.
7. **Departure, block, and later reconciliation**
   - enough consumer treatment to prove the state differences;
   - do not reproduce the entire C5 state catalogue as policy cards.

### 5.4 Claude Code deliverables

Audit and document:

- current Person, relationship, Occasion, Invitation, participant, audience,
  grant, source, receipt, and block-state models;
- current viewer-relative read paths;
- whether author, subject, custodian, audience, purpose, expiry, use,
  inference, and action can be represented independently;
- how withdrawal propagates through Life, Home, Chat, Places, saved
  compositions, search, caches, and pending actions;
- the owner of the shared core versus each person's private Outcome;
- whether unblock restores any grant implicitly;
- whether current memory synthesis launders shared evidence into person-level
  narrative; and
- the smallest renderer-neutral fixture contract needed by the design
  prototype.

Write the audit to:

`docs/working/life-together-consumer-arc-code-audit-2026-09-01.md`

Do not implement the full Together architecture during this workstream.

### 5.5 Acceptance gates

The workstream passes only if:

- another person's contribution creates immediate value without a reply ask;
- the user can tell what is theirs, the other person's, and held in common;
- private Outcomes never merge into shared consensus;
- a shared record feels warmer and more useful than a permissions ledger;
- withdrawal has visible causal effect without revealing removed content;
- block and later unblock do not revive old social paths automatically;
- the People root is useful when no social event is urgent; and
- no screen ranks intimacy, friendship strength, or social activity.

### 5.6 Hard failures

- friend activity presented as an ambient feed;
- “people near you” or implicit location broadcasting;
- shared Occasion treated as blanket permission;
- Vesper speaking in Maya's voice;
- private meaning merged into a group summary;
- a reply box as the primary value;
- withdrawal that removes only the source page but leaves snippets or
  interpretations elsewhere; or
- relationship state inferred from silence, dwell, or frequency.

## 6. Workstream B — Human refinding as an interactive experience

**Priority:** 2  
**Primary owner:** Claude Design  
**Code partner:** Claude Code  
**Suggested board family:** `18 Human Refinding Flow`

### 6.1 Question

Can a person recover something they remember incompletely without knowing
whether Vesper considers it an Artifact, Source, Place, Episode, Journey,
Occasion, held question, or conversation?

### 6.2 Required loop

```text
incomplete human cue
  -> governed target or bounded candidate set
  -> why it matched
  -> smallest useful Around this trail
  -> durable object or dossier when wanted
  -> optional correction or Continue
  -> natural return to the prior Life context
```

Search wording and exploration remain session-local unless the person
explicitly corrects, keeps, names, or authors something.

### 6.3 Queries to prototype

At minimum:

1. “The bar after meeting Teodora.”
2. “What did Alex bring to dinner?”
3. “The flight that got cancelled.”
4. “That pasta place in Sorrento.”
5. “The photograph from the ferry.”
6. “The book Maya mentioned.”
7. one no-result query;
8. one two-candidate ambiguity;
9. one permission-limited social query;
10. one query whose premise is wrong but gently corrected by occurrence truth.

### 6.4 Claude Design deliverables

Compose a clickable flow showing:

- entry from each Life lens;
- natural-language query initiation;
- direct answer when governed truth safely supports one;
- source-first, episode-first, relationship, and historical-plus-current result
  forms;
- a two-candidate result without fake confidence precision;
- `Around this` expanded only on request and limited to three useful
  landmarks;
- target-first reading order;
- visible source, author, truth, and audience when material;
- plan-versus-occurrence correction;
- a permission-limited result;
- correction, detach, exclusion, or release where appropriate;
- a valid Continue to Chat, Places, or the durable object; and
- back-navigation that preserves the person's search context.

The prototype must demonstrate retrieval utility, not merely design a search
results page.

### 6.5 Claude Code deliverables

Use the fifty-query benchmark to audit:

- existing search and retrieval paths;
- searchable identities and embeddings;
- truth and source-role availability;
- viewer-relative authority checks at read time;
- Place/person/episode relation traversal;
- plan-versus-occurred state;
- candidate ranking signals and uncertainty representation;
- raw-query telemetry and retention;
- direct-answer safety;
- current-world refresh handoff; and
- correction propagation from a result.

Produce:

1. a query-to-current-code coverage matrix;
2. a renderer-neutral result envelope;
3. a deterministic fixture runner proposal; and
4. a smallest native prototype recommendation.

Write the audit to:

`docs/working/life-human-refinding-code-audit-2026-09-01.md`

### 6.6 Acceptance gates

- The requested target appears before a recap or essay.
- The result explains why it matched without revealing hidden private context.
- The person never needs to learn Vesper's ontology.
- A wrong premise is corrected gently and specifically.
- Ambiguity stays bounded; the system does not hallucinate certainty.
- Social and blocked material is filtered at read time.
- Query wording does not become durable interest evidence.
- Current-world truth is refreshed separately from historical truth.
- Search remains retrieval and orientation, not another feed or Chat clone.

### 6.7 Hard failures

- returning a trip summary before the requested object;
- manufacturing one answer from ambiguous evidence;
- using search as evidence of preference or identity;
- exposing why a blocked or private result was suppressed in a way that leaks
  the hidden relation;
- storing every query by default;
- hiding plan-versus-occurred disagreement; or
- forcing Chat when a deterministic answer already exists.

## 7. Workstream C — Return arbitration and scarcity

**Priority:** 3  
**Primary owner:** Shared  
**Suggested board family:** `19 Return Arbitration Lab`

### 7.1 Question

When the same evidence can support several valid Returns, how does Vesper
deliver the smallest number of compositions that creates the greatest
nonredundant value?

The current Rome–Paris–New York evidence can support:

- a relational juxtaposition;
- an epistemic explanation;
- a possibility transfer;
- a factual recap;
- a practical Home composition;
- a human-authored reason to reconnect; or
- silence.

Individually valid candidates must not become concurrent duplicate content.

### 7.2 Proposed law to test

> **Among eligible Returns that substantially share evidence, surface or
> compose the smallest set whose dominant jobs provide nonredundant value under
> current evidence, authority, freshness, and circumstance. Merge compatible
> value; suppress weaker duplication; allow a later material trigger to
> recompile the dominant job.**

Engagement probability is not a material trigger. More available space is not
permission to fill it.

### 7.3 Required scenarios

1. Only one candidate clears evidence and novelty gates.
2. Two candidates overlap and should merge.
3. A relational Return surfaces when Maya addresses her contribution.
4. A later heat forecast recompiles the same cluster into a possibility
   transfer for Home.
5. The older relational Return disappears rather than coexisting redundantly.
6. Home suppresses a weaker Life projection while preserving lineage.
7. Maya withdraws her contribution before delivery.
8. The remaining Rome-only evidence either recompiles or falls below the bar.
9. The person suppresses the subject without deleting its record.
10. Correct silence wins over all candidates.

### 7.4 Claude Design deliverables

Create a decision-and-experience board, not an internal scoring dashboard.
Show:

- the candidate set as design evidence;
- the admitted consumer composition;
- what the user does **not** see;
- merge versus suppress behavior;
- transition from relational to present-tense value;
- disappearance after expiry or authority change;
- the visible material reason;
- one layer-level suppression control; and
- the resulting root density before and after arbitration.

Use at least one Time-root frame and one Home frame with surrounding content so
the scarcity decision can be judged in context.

### 7.5 Claude Code deliverables

Map or propose:

- candidate identity and evidence-dependency sets;
- material-trigger identity;
- dominant job;
- novelty and nonredundancy checks;
- authority and freshness gates;
- surface owner and density eligibility;
- merge, suppress, expire, invalidate, and recompile transitions;
- user suppression separate from source deletion;
- why-this-appeared lineage; and
- deterministic test cases for candidate collisions.

Do not begin with a general-purpose recommender or ranking model. Start with a
small explicit admission policy over the controlled fixtures.

### 7.6 Acceptance gates

- No two surfaced Returns substantially repeat the same evidence and value.
- The winning composition has one dominant job.
- A later material trigger may change the dominant job without creating a new
  durable identity claim.
- Authority loss causes recomposition before delivery.
- The user can suppress resurfacing without deleting the underlying record.
- Silence is a first-class result.
- The policy is explainable through material facts, not engagement scores.
- Root density remains calm even when the engine generates many candidates.

### 7.7 Hard failures

- one candidate per Return family rendered concurrently;
- filling a quota of cards;
- engagement probability as the primary ranking signal;
- separate durable objects for every projection;
- resurfacing ignored material because the user viewed it;
- hiding why a winner appeared; or
- allowing the same friend's contribution to be paraphrased into several
  apparently independent insights.

## 8. Workstream D — One contribution through its complete lifecycle

**Priority:** 4  
**Primary owner:** Shared  
**Suggested board family:** `20 Contribution Lifecycle`

### 8.1 Question

Does casually giving something to Vesper feel worthwhile because it changes
what Vesper can later give back—without asking the person to file, classify,
or maintain it?

### 8.2 Required loop

```text
Ask / Point / Bring / Keep / Address in Chat
  -> immediate value
  -> only authorized durable consequence
  -> quiet placement in Life
  -> connections to existing objects
  -> later admitted value in Home or Places
  -> optional shaping in Chat / Plan / Occasion
  -> authoritative readback
  -> causal receipt only if something changed
  -> later refinding, correction, release, or withdrawal
```

### 8.3 Inputs to compare

1. **Restaurant photograph**
   - Point: “This texture is what I meant.”
   - May support the pasta question without becoming a preference.
2. **Movie ticket**
   - Bring: proves attendance, not opinion or interest.
   - May later support a cross-medium connection.
3. **Voice observation**
   - Point: preserves explicitly authored attention when clear.
   - Must not become personality.
4. **Friend's addressed note**
   - Share/Address boundary with independent authority axes.
5. **Forwarded booking email**
   - Source custody and occurrence truth remain distinct.
6. **Ask with a Source**
   - “What does this ticket say?” should answer without durable memory by
     default.

### 8.4 Claude Design deliverables

For each input, show:

- the first Chat turn;
- immediate value before any classification;
- whether anything persists and why;
- the quiet receipt or correct absence of one;
- where it becomes findable in Life;
- one later consequence or correct non-use;
- the optional continuation;
- correction, release, or withdrawal; and
- what changes everywhere else afterward.

At least one input must stop after answering. At least one must persist as a
Source but produce no inference. At least one must later create material value.
At least one social input must withdraw and reconcile.

### 8.5 Claude Code deliverables

Audit all writers reachable from:

- ordinary Chat;
- inbound share;
- Occasion chat;
- import/Bring;
- proactive turns;
- reflection;
- memory synthesis; and
- correction/release.

For each writer, record:

- gesture and immediate job;
- proposed and effective authority;
- Source custody;
- truth mode and evidence roles;
- target owner;
- retention layers;
- inference distance and scope;
- audience and social principals;
- action tier;
- receipt and Undo;
- causal consumers; and
- conformance with `contribution-and-consequence.md`.

Pay particular attention to existing paths that convert ordinary conversation,
silence, mood, personality, or repeated topics into durable memory.

Write the audit to:

`docs/working/life-contribution-lifecycle-code-audit-2026-09-01.md`

### 8.6 Acceptance gates

- Every input provides immediate value.
- The user is never asked to classify ordinary material.
- Ask remains no-write unless explicitly combined with another gesture.
- A Source may persist without a person-level inference.
- Movie attendance never becomes movie preference.
- A photograph's meaning comes from the authored Point, not the pixels alone.
- Every durable or external consequence has one owner and resolved authority.
- Correction or withdrawal visibly repairs dependent projections.
- The later value makes contribution feel worthwhile rather than extractive.

### 8.7 Hard failures

- generic “save to memory?” after every contribution;
- immediate filing or category selection;
- ticket equals attendance equals interest;
- photo equals preference;
- ordinary Ask silently writes memory;
- Vesper-generated interpretation presented as the person's meaning;
- a receipt for something that did not change; or
- correction isolated to one surface.

## 9. Cross-workstream prototype requirements

Every prototype must include:

### 9.1 Complete value before effort

The first visible treatment must answer, orient, reconstruct, compare, or
otherwise provide value. A button, reply field, reflection prompt, or “tell me
more” is not the value.

### 9.2 Truth roles remain distinct

Do not collapse:

- planned;
- occurred;
- captured;
- authored;
- generated;
- inferred;
- current-world; and
- unresolved.

### 9.3 One owner, many projections

The same identity may appear at different densities. A projection is not a new
canonical object merely because it renders on another root.

### 9.4 Human language outside, ontology inside

User-facing language should say:

- “what Maya shared”;
- “why this is here”;
- “what happened”;
- “what changed”;
- “keep this searchable”;
- “do not show this again”; or
- “nothing changed.”

Avoid exposing:

- projection envelopes;
- authority axes;
- dependency graphs;
- inference scope IDs;
- return families; or
- resolver terminology.

### 9.5 No creepy interpretation

The product may state supported behavior and authored meaning. It must not
convert behavior into a personality verdict.

Prefer:

> “Your Rome notes and routes show that the two long unshaded legs were where
> the plan changed.”

Avoid:

> “You experience cities through transitions.”

If a causal statement depends on a person's interpretation—“the day broke,”
“this mattered,” “the best hour”—include the authored observation or concrete
outcome that supports it. Vividness is not permission to overclaim.

### 9.6 Arbitration precedes rendering

Do not design a page that renders every eligible object, connection, Return,
and social contribution. Show the result of admission, scarcity, and
nonredundancy decisions.

### 9.7 Accessibility and physical interaction

At prototype scale, account for:

- dynamic type pressure;
- touch-target size;
- screen-reader reading order;
- reduced motion;
- color-independent state communication;
- long names and translated copy;
- one-handed reach for frequent actions; and
- preserved context after back-navigation.

This does not require a separate visual redesign. It prevents the proposed
behavior from depending on tiny typography or hidden gestures.

## 10. Evaluation rubric

Score each complete flow from 0 to 2 on each dimension:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Immediate value | asks for work first | partial value | complete value before effort |
| Novelty | replay/paraphrase | modest addition | substantive new contribution |
| Truth | collapsed/overclaimed | limits implied | roles and uncertainty explicit |
| Authority | hidden or expanded | partially legible | scoped, attributed, revocable |
| Surface ownership | duplicated/unclear | handoff implied | one owner and coherent projections |
| Effort | workflow/homework | optional friction | effortless or skippable |
| Social integrity | merged/inferred | mostly separated | plural, attributed, withdrawal-safe |
| Refinding | ontology required | target found with effort | human cue restores target and context |
| Scarcity | feed/quota | some redundancy | smallest nonredundant set |
| Repair | local or invisible | partial propagation | causal reconciliation everywhere |
| Ordinary-life fit | travel-dependent/solemn | works narrowly | casual and useful beyond travel |
| Emotional fit | analyzed/judged | neutral | recognized, held, and in control |

A workstream is not consumer-proven unless:

- every hard failure is absent;
- no dimension scores `0`;
- Immediate value, Truth, Authority, Effort, and Surface ownership score `2`;
- the ordinary or silence state remains complete; and
- the flow survives one correction or withdrawal transition.

## 11. Sequence and checkpoints

### Round 1 — parallel foundation

**Claude Design**

- compose Workstream A Together;
- compose Workstream B Refinding.

**Claude Code**

- audit Together substrate and non-conforming seams;
- audit the fifty-query refinding benchmark against current code;
- provide renderer-neutral envelopes and deterministic fixture gaps.

**Checkpoint 1**

Founder reviews complete consumer flows, not isolated screens. Decide:

- whether Together feels warm and useful;
- whether refinding is target-first and effortless;
- which design assumptions code evidence invalidates; and
- whether either workstream is ready for canonical integration.

### Round 2 — arbitration

Use the accepted Together and refinding compositions to build Workstream C.

**Checkpoint 2**

Founder reviews:

- what surfaced;
- what was suppressed;
- why the dominant job won;
- whether the root remains calm; and
- whether authority changes recompile before delivery.

### Round 3 — contribution lifecycle

Use accepted owners, authority envelopes, and arbitration rules to compose
Workstream D.

**Checkpoint 3**

Founder judges whether the complete loop makes giving things to Vesper feel
worthwhile without creating maintenance work.

### Round 4 — native prototype decision

Only after the three checkpoints choose one native prototype slice. Good
candidates are:

- one Together shared-with-Maya flow;
- one incomplete-cue refinding flow; or
- one Bring-in-Chat to later-Home-value lifecycle.

Do not implement all four workstreams simultaneously.

## 12. Deliverable ledger

### Claude Design

- `17 Together Consumer Arc`
- `18 Human Refinding Flow`
- `19 Return Arbitration Lab`
- `20 Contribution Lifecycle`
- updated `00A Canon and Open Arcs` statuses after each founder ruling;
- no modification of historical boards except unmistakable status stamps; and
- no real-photography gate.

### Claude Code

- `docs/working/life-together-consumer-arc-code-audit-2026-09-01.md`
- `docs/working/life-human-refinding-code-audit-2026-09-01.md`
- `docs/working/life-contribution-lifecycle-code-audit-2026-09-01.md`
- one Return arbitration policy proposal with deterministic fixtures;
- one cross-repo owner/read/write map;
- no production implementation before Round 4 approval.

### Shared convergence artifact

After each checkpoint, append a short decision receipt to this document or a
dated companion document containing:

- evidence reviewed;
- accepted behavior;
- rejected behavior;
- remaining uncertainty;
- status by workstream;
- changed canonical boards or docs;
- code assumptions confirmed or invalidated; and
- next authorized scope.

## 13. Compact handoff to Claude Design

> Treat the current Life philosophy, roots, lenses, object grammar, Return
> anatomy, and authority model as settled inputs. Do not create more visual
> directions or component variants. Compose four complete behavioral arcs in
> order: Together, human refinding, Return arbitration, and contribution
> lifecycle. Begin with Together and refinding in parallel. Use the controlled
> fixtures and acceptance gates in this handoff. Show complete value before
> effort, preserve human contribution lanes, keep absence silent, and render
> the result of arbitration rather than every candidate. Label architecture
> proofs honestly. The real-photography composition is tabled.

## 14. Compact handoff to Claude Code

> Treat the current Life design as a hypothesis to audit against the existing
> backend and mobile code, not as permission for a repository-wide rewrite.
> Read the governing references and each repository's local instructions.
> Investigate Together authority and causal repair, human refinding coverage,
> Return arbitration requirements, and the full contribution writer/read path.
> Produce renderer-neutral contracts, deterministic fixtures, current-owner
> maps, and feasibility findings for Claude Design. Do not implement the full
> architecture or migrate nouns. Native prototype work begins only after the
> founder approves a Round 4 slice. The real-photography composition is tabled.

## 15. Final standard

This phase is successful when Life no longer exists only as a coherent design
philosophy. It must prove four consumer truths:

1. **Another person can enrich my Life without becoming a feed or invading my
   private meaning.**
2. **I can recover something from my life using the incomplete way I actually
   remember it.**
3. **Vesper can choose one valuable composition without overwhelming me with
   everything it could say.**
4. **Giving something to Vesper is worthwhile because it later makes my life
   more intelligible, possible, or workable—without creating homework.**

Those four proofs are the next design and prototype milestone.


---

## Checkpoint 1 decision receipt — 2026-08-31

**Evidence reviewed:** boards `17`/`17A–17G` (Together consumer arc) and
`18`/`18A–18C` (human refinding) in the design project;
`life-together-consumer-arc-code-audit-2026-09-01.md`;
`life-human-refinding-code-audit-2026-09-01.md`.

**Accepted behavior (founder ruling, "sounds good on all"):**

- Workstreams A and B: **Consumer flow proven at fixture scale.**
- Arrival salience law: Life carries an addressed contribution as a quiet
  stamp; Home may admit it when it earns present attention (Multiplayer
  canon §9); push requires prospective authority.
- Withdrawal renders one visible causal acknowledgment, never content.
- MET ALONG THE WAY stays in the People root; encountered people must
  become queryable identities (refinding requires it).
- Fixture chronology ratified: dinner Sat Aug 29 → Maya's note Sun Aug 30
  → today Mon Aug 31.
- "Ask Maya" doors stay; drafting reframed so the person is the author.
- Fixture-scale demonstration is acceptable for the Together gate; the
  revocation bus is its own workstream.
- **The 13-field grant record is the durable promotion of
  `ContributionAxes`**, owned by a grants domain adjacent to the
  experience graph, and is the named owner of the "graph-owned sharing
  authorization" the projection transport awaits. The renderer-neutral
  fixture contract is its spec.
- **Truth-lane ruling:** refinding read models build over the
  experience-graph lane; revision lineage ports into it; no new
  investment in the legacy itinerary lane.
- Four safety-class fixes authorized ahead of the migration order
  (cross-user observe hole; personality/mood observation prompts;
  settlement masking bypass; durable query-hash retention). Applied
  uncommitted; product-behavior fixes deferred to the Round 4 slice.

**Rejected behavior:** none rejected at this checkpoint.

**Remaining uncertainty:** epochs-vs-hard-delete (audit Q1) not yet
ruled; real-photography composition remains tabled; Round 4 slice
leaning refinding (seven-query read-model prototype) but not yet chosen.

**Status by workstream:** A consumer-proven (fixture scale) · B
consumer-proven (fixture scale) · C authorized, in flight (boards 19) ·
D not started.

**Changed canonical boards/docs:** 17C/17E amended (salience law,
authorship framing); 00A statuses updated; both audit docs annotated
with applied fixes.

**Code assumptions confirmed/invalidated:** truth substrate stronger
than design assumed (compose, don't invent); S05 withdrawal not honestly
wireable today (prototype binds to the fixture contract); no person
entity, no block state, no durable grant record, no revocation bus.

**Next authorized scope:** Workstream C (Return arbitration, board
family 19) using accepted A/B compositions, plus the arbitration policy
proposal with deterministic fixtures. No production implementation.


---

## Checkpoint 2 decision receipt — 2026-08-31

**Evidence reviewed:** boards `19`/`19A–19D` (Return Arbitration Lab);
`life-return-arbitration-policy-2026-09-01.md`.

**Accepted behavior (founder ruling, "all make sense"):**

- The §7.2 arbitration law as rendered: one seat per cluster per surface;
  merge as a composition act distinct from suppression; dominant-job
  recompilation on material triggers only; identity preserved across
  recompiles (no new durable object).
- The admission pipeline and its precedence (person suppression above
  all boundary layers; surface-ownership yield; the demotion ladder
  root → dossier organ → search-only).
- The ten deterministic scenario fixtures and zero-count invariants as
  the arbitration test oracle.
- Policy §7 proposals adopted: partial-overlap suppression binds cluster
  identity only (future overlapping candidates disclose the suppressed
  sibling in lineage); no losing-candidate browsing UI (the Why-this
  door names merged/yielded siblings only).

**Rejected behavior:** none.

**Remaining uncertainty:** policy §7 Q1 (cross-cluster seat arithmetic
for the 0–3 root region) stays open for the build phase.

**Status by workstream:** A consumer-proven · B consumer-proven ·
C decision-and-experience proven at fixture scale (policy proposal
accepted) · D authorized, in flight (boards 20).

**Next authorized scope:** Workstream D (contribution lifecycle, board
family 20) + the contribution-lifecycle writer audit. No production
implementation.


---

## Checkpoint 3 decision receipt — 2026-08-31

**Ruled by delegation** (founder: "use your own judgements, and then
let's move to round 4").

**Evidence reviewed:** boards `20`/`20A–20F`;
`life-contribution-lifecycle-code-audit-2026-09-01.md` (80 writers:
38/28/14); safety batch 2 + daily-digest extension (applied, green).

**Judgment — Workstream D: CONSUMER FLOW PROVEN AT FIXTURE SCALE**
(design). Against the §10 rubric at fixture scale: no hard failure
present on any board; Immediate value, Truth, Authority, Effort, and
Surface ownership each score 2 across the six inputs; the silence/null
state is complete (20A); the flow survives a withdrawal transition
(20E). The writer audit records the implementation distance — most
critically that Ask is not no-write on any reachable lane and that chat
contributions produce exhaust, not addressable objects. Design proof
and code conformance are different rungs; both are now honestly
labeled.

**Adopted by delegation:**
- The migration order's named first target: **chat contributions become
  addressable objects through the contribution envelope** (the missing
  §8.2 middle; converges with the Checkpoint-1 grant record).
- Group-memory attribution (writer-audit A8): the whole-document group
  memory is EXCLUDED from the Together shared-core story until items
  carry authors — conservative branch.
- Daily digest fixed under the batch-2 precedent (same defect class);
  chat-image TTL and the silence-row reflection read remain deferred to
  the migration (gesture-dependent retention; operational-vs-narrative
  read separation).

**Round 4 decision — the native slice is REFINDING**, exactly as the
refinding audit §6 specifies: queries Q01/Q05/Q08/Q20/Q21/Q22/Q23 over
one `refind_sources` read model returning `life-refind-result.v1`
envelopes; the `did_not_happen` write fix; truth chips + one Around-this
block in the existing mobile search overlay; client-side `query_hash`
removal. Fixture proof via L01/L03 manifests + a
`tools/eval/plugins/life_refinding/` deterministic runner (built first).
Done means: the seven scenarios score ≥13/16 with zero hard failures
under the runner — Consumer flow proven at fixture scale, nothing more.

**Lane-ruling interpretation (recorded to prevent drift):** the
Checkpoint-1 truth-lane ruling (experience-graph lane wins) governs the
durable direction. This slice's read model binds its CONTRACT (the v1
envelope) as the stable thing and reads the legacy itinerary/booking
rows where the required truth states live today; the substrate swaps to
the experience graph as the migration ports revision lineage. The
contract, not the substrate, is what mobile and the runner depend on.

**Status by workstream:** A consumer-proven · B consumer-proven ·
C decision-and-experience proven · D consumer-proven (design) ·
Round 4 slice authorized and in flight.


---

## Round 4 completion record — 2026-08-31

**The refinding native slice is built and proven.**

- Backend: `refind_sources` read model + `life-refind-result.v1` envelope
  + `POST /api/life/refind`; the `did_not_happen` reject fix (through the
  canonical occurrence-operation ledger); L01/L03 dogfood manifests (two
  new collections: `occurrence_marks`, `occurrence_proposals`); the
  `tools/eval/plugins/life_refinding/` deterministic runner with the
  eight benchmark dimensions as registered checks and a no-raw-query
  telemetry assertion. **All seven scenarios (Q01/Q05/Q08/Q20/Q21/Q22/
  Q23): 16/16, zero hard failures**, real seeded runs; the Q23
  correction loop verified end-to-end and rerun-deterministic.
- Mobile: `LifeRefindLane` in the universal search overlay (target-first
  rows on the canon row primitive; truth chips preserving "no evidence"
  ≠ "didn't happen"; cancelled/unused rendered with truth labels;
  why-matched caption; Around-this collapsed by default). Flag
  `EXPO_PUBLIC_LIFE_REFIND_LANE`, default OFF, dev/internal-fenced.
  Hand-written envelope type (no OpenAPI regen). Client `query_hash`
  emission removed; Atlas `raw_text_hash` removed same-class.
- Verification: backend — 20 new tests + 955 eval + 532 dogfood green,
  lint/mypy/ruff clean. Mobile — tsc clean, 63 targeted tests green,
  row-ratchet and lifecycle gates pass. Pre-existing shared-tree red
  (three unregistered ui files; a concurrent session's uncommitted
  portfolio) is recorded as not-from-this-slice.

**Status: Consumer flow proven at fixture scale AND implemented (dark,
flag-gated).** Not shipped. Everything uncommitted per the repo rule.

**Known deviations (recorded in the build records):** Around-this rows
display-only for now (continues advise_only); `governed_answer` renders
as full result rows rather than a summary line; the openapi snapshot
deliberately not refreshed.

**The four consumer truths (§15) now each have a proof artifact:** 1 →
boards 17 + the Together audit's fixture contract; 2 → the built
refinding slice; 3 → boards 19 + the arbitration policy; 4 → boards 20 +
the writer audit + the named migration target. The handoff's milestone is
met at its own defined bar.
