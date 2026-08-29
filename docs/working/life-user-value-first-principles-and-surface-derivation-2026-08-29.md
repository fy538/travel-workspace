---
doc_type: working
status: active
owner: founder / product / design / editorial / research
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Reframes Life from an information architecture and rendering problem into a user-value problem, ranks the value that accumulated lived evidence can create, and derives surface responsibilities and evaluation gates from those outcomes.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/decisions/2026-08-29-adopt-life-continuity-and-return-contract.md
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
  - docs/working/life-behavior-research-round-3-2026-08-29.md
  - docs/working/operationalizing-relational-intelligence-hci-research-round-2-2026-08-28.md
  - docs/working/life-composition-and-continuity-lab-execution-plan-2026-08-29.md
  - travel-agent/docs/product/My World, Encounters, and Private Place Memory.md
  - travel-agent/docs/working/platform-memory-and-human-remembering-2026-08-21.md
  - travel-agent/docs/product/Vesper Editorial and Content Canon.md
---

# Life User Value: First Principles and Surface Derivation

> Status: active research and product-definition correction
>
> This document does not finalize Life navigation, visual design, or a
> production projection. It establishes the value test those decisions must
> pass.

## Executive correction

The current Life work is conceptually coherent but not yet sufficiently
compelling. We moved too quickly from continuity doctrine into information
architecture. Timeline, periods, episodes, categories, Map, Sources, search,
scope, and restoration are useful mechanisms. They are not, by themselves,
reasons to use Vesper.

The stronger product premise is:

> **Your history becomes useful.** What you have lived and deliberately given
> Vesper can return as a clearer account, a connection you had not seen, a
> capability you can reuse, a shared thread with someone, or a better opening
> into what comes next.

The history is not the product. **Compounding usefulness is the product.**

Life is therefore not primarily where Vesper stores or organizes a person's
past. It is where the person can inspect, revisit, and use the value that their
history has earned. Its architecture should be derived from those outcomes,
not the other way around.

## 1. What the existing work already says

The value-first direction is not a new pivot. It was already present in the
strongest internal documents, but it became obscured by the recent Life
composition work.

### 1.1 The canonical internal claim

`My World, Encounters, and Private Place Memory` states:

- the unit of compounding value is not a memory stored;
- it is a later experience that opens differently because authorized prior
  evidence was relevant;
- capability comes before archive;
- the system should help someone perceive, understand, navigate, discuss, or
  do something differently; and
- Vesper must make an experience useful enough to revisit before making it
  beautiful enough to share.

`Platform Memory and Human Remembering` makes the same distinction in process
terms:

```text
notice
  -> occasion
  -> selective continuity
  -> fitting cue
  -> recognition, reconstruction, or correction
  -> future application
  -> consequence
```

`Three-entry Longitudinal Product Simulations` gives the clearest experiential
test: accumulated value is a grounded realization the person did not already
recognize, followed by an adjacent curiosity or consequence.

### 1.2 What Life is allowed to own

The existing four-root work remains useful:

- **Home** owns time-sensitive outward consequence: what matters now and what
  possibility is ready to open.
- **Chat** owns low-friction contribution, inquiry, direction, correction, and
  action.
- **Places** owns the world through place relationships, nearby relevance,
  transfer, and spatial possibility.
- **Life** owns durable, inspectable continuity across time, place, people,
  evidence, and episodes.

This means Life does not need to hoard every benefit created by history. It
should make the compounding system legible and revisitable while Home, Places,
and Chat project its timely consequences.

### 1.3 Where the current work drifted

Recent Life work correctly solved difficult enabling questions:

- stable episode identity;
- contextual refinding;
- Mine and Together authority;
- claim-level source identity;
- correction, deletion, and revocation;
- continuity across lenses; and
- safe generated compositions.

But the proposed compositions began with the mechanism: a timeline, a route,
an index, a cluster, a comparison, or a source treatment. The user was left to
infer why any of it mattered. That produces diagrams such as “intended versus
supported” which may be semantically correct but offer no immediate human
payoff.

## 2. Research synthesis: what remembering is for

Research on autobiographical memory commonly identifies three functions:
directing behavior, supporting social bonds, and sustaining self-continuity.
It also identifies emotion regulation as a plausible additional function. The
evidence base is meaningful but not absolute: much of it is correlational or
self-reported, and usefulness depends on the situation and goal. Life should
therefore enable these functions without claiming that a generated reading is
psychologically true.

The personal-informatics literature adds an important distinction. Collection
and integration are not the endpoint; reflection and action are later stages.
The lived-informatics model also warns against assuming that every person is
trying to optimize or change behavior. Curiosity, understanding, record, and
periodic return can be legitimate outcomes, and lapses are normal.

Sellen and Whittaker's critique of lifelogging is directly relevant: complete
capture is not equivalent to a useful memory system. Selectivity must be
designed around the jobs people are trying to accomplish.

Adjacent products expose the opportunity and the gap:

- photo systems are strong at passive capture, retrieval, resurfacing, and
  lightweight reconstruction;
- personal archives are strong at trustworthy custody and search;
- recap products are strong at compression, ritual, surprise, and sharing;
- social products are strong at distributing perspectives among people; and
- assistants are strong at interpretation and action but usually weak at
  governed longitudinal evidence.

Google's Ask Photos is a useful benchmark: it can answer contextual questions
such as what someone ate on a trip and locate relevant evidence. That is real
utility, but it remains predominantly a photo-library capability. Vesper's
opportunity is to join heterogeneous evidence, lived attention, places,
people, occasions, and future action—without pretending to narrate the person.

### Research implications for Vesper

1. **Record is necessary, not sufficient.** Factual reconstruction earns trust
   and prevents the system from becoming fiction.
2. **Novelty must be consequential.** A surprising statistic or pattern is
   weak unless it improves understanding, connection, perception, or action.
3. **Directive value is not taskification.** A memory may silently improve a
   recommendation or open an immediately useful possibility; the person does
   not need to complete reflective homework.
4. **Social value is not a feed.** The important unit is an attributed
   perspective, missing piece, shared history, borrowed lens, or easier second
   occasion—not ambient performance.
5. **Self-continuity requires restraint.** Vesper may show evidence and change
   over time. It should not pronounce personality traits or identity claims.
6. **The absence of output can be correct.** Not every period, artifact, or
   trip earns interpretation or resurfacing.

## 3. Ranked user-value model

The ranking below weighs felt benefit, differentiation, fit with Vesper's
evidence, and ability to compound. Frequency is considered separately; a
high-frequency utility can still be strategically less distinctive.

| Rank | User value | What becomes better for the person | Strategic role | Failure mode |
| --- | --- | --- | --- | --- |
| 1 | **Future opening** | A present or future experience becomes easier, richer, or newly possible because prior evidence was used | North-star proof of compounding | Nostalgic recap with no outward consequence |
| 2 | **Capability and perception transfer** | The person can notice, understand, compare, choose, navigate, discuss, cook, host, or act differently | Deepest differentiated value | Generic advice weakly attached to history |
| 3 | **Relational continuity** | Shared history, different perspectives, and prior outcomes improve connection or a later occasion | Multiplayer advantage | Friend activity feed or involuntary shared biography |
| 4 | **New understanding** | Vesper reveals a grounded mechanism, contrast, or connection the person had not already made | Editorial advantage and immediate delight | Restating what the person supplied; creepy trait inference |
| 5 | **Accurate reconstruction** | Scattered tickets, photos, places, conversations, and outcomes become a coherent, correctable account | Trust-building practical value | Flat chronology or unsupported synthesis |
| 6 | **Contextual retrieval** | The person can recover an item, detail, place, source, or episode using natural cues | Frequent utility and table stake | Filing system disguised as a product |
| 7 | **Recognition and celebration** | The person can enjoy a factual, well-composed return to a period or occasion | Affective value and ritual | Generic nostalgia, vanity metrics, or annual-only spectacle |
| 8 | **Custody and control** | The person can see provenance, correct errors, separate scopes, revoke access, and forget | Non-negotiable trust substrate | Governance controls presented as the primary experience |

The order does not mean Life should hide retrieval or control. It means those
capabilities support the promise; they are not the promise.

### 3.1 Value versus mechanism

| Mechanism | It becomes valuable only when it enables... |
| --- | --- |
| Timeline | reconstruction, change over time, or a useful return |
| Categories and clusters | fast refinding or a non-obvious comparison |
| Map | spatial reconstruction inside a meaningful geographic scale, or an actionable nearby opening |
| Source list | verification, correction, re-use, or retrieval |
| Artifact gallery | recognition, reconstruction, creation, or sharing with intent |
| “Together” scope | attributed plural memory, relationship continuity, or a better future occasion |
| Generated article, podcast, map, or composition | new understanding or capability in the medium best suited to it |
| Search | direct recovery with context attached, not a results dump |
| Recap | a factual compression that reveals something worthwhile, not a report card |

## 4. A sharper promise for Life

### Product promise

> **Life turns what you have lived into something you can use again.**

Expanded:

> Life is Vesper's durable view of the places, people, occasions, sources, and
> discoveries that have mattered. It helps you recover what happened, see a
> connection you missed, carry forward something you learned, and understand
> how the past is improving what Vesper can do with you now.

### Human question

Replace the abstract question—“What is becoming true for me and between us
over time?”—with a more concrete pair:

> **What has my life made possible now?**
>
> **What can I find, understand, or use again?**

The first expresses the differentiated north star. The second preserves the
practical floor.

## 5. Work backward from value into the surface

The default Life view should not be organized first around artifact types,
months, or database objects. It should offer a stable way into value-bearing
products of the person's history, with the record always reachable.

### 5.1 Five surface responsibilities

#### A. Use again

Show capabilities, judgments, preferences with evidence, practical knowledge,
and unresolved possibilities that can improve a new situation. Timely
instances may be projected to Home or Places; Life preserves their history and
reason.

Examples:

- a ferry disruption becomes useful transfer knowledge for a future coastal
  route;
- attention to pasta texture becomes a grounded cooking or restaurant lens in
  New York;
- what worked at one dinner quietly improves preparation for a later occasion.

#### B. See across

Offer a bounded editorial composition when multiple pieces of evidence support
a connection the person did not already make.

Examples:

- a cross-place comparison that explains why Sorrento's cliffs produce a
  different urban and transport experience from another cliff city;
- a connection between a friend's simultaneous Paris experience and the
  person's Rome experience, with each perspective attributed;
- a place, idea, dish, book, film, or conversation reappearing across otherwise
  separate episodes.

#### C. Re-enter

Provide accurate, rich episode reconstructions. These can be useful without a
grand interpretation: what was intended, what happened, who was there, what
evidence exists, and what changed.

Examples:

- a Europe journey composed from plane, train, and ferry records, photos,
  places, and conversations;
- a dinner whose plan, contributions, lived moments, and later outcomes stay
  connected without collapsing private and shared meaning.

#### D. Find

Give direct access to a place, person, date, source, artifact, conversation,
occasion, or detail. Search should accept remembered context and return the
target first, then its episode and provenance.

#### E. Together

Make shared continuity useful without creating a follower feed. Surface
contributions, contrasting perspectives, relationship-specific threads, and
earned future openings only when the viewer is authorized.

### 5.2 Stable structure versus adaptive value

Life needs both:

- a **stable record spine** for orientation, trust, search, and return; and
- an **adaptive value layer** for new understanding, re-use, and continuity.

The stable spine may eventually use time, episode clusters, and contextual
lenses. It should sit behind or alongside the value—not masquerade as the
value. Conversely, adaptive compositions must never rewrite the record.

### 5.3 What should not lead the page

- raw counts such as “four places, twelve artifacts”;
- an abstract timeline diagram;
- a map of every place across countries;
- an “intended/supported” evidence visualization;
- generic retrospective prompts;
- broad AI identity interpretations;
- privacy and source administration; or
- a shuffled feed of memories.

Each may have a subordinate role. None establishes why Life deserves to
exist.

## 6. Admission test for any Life unit

A top-level unit must answer all of these:

1. **Payoff:** What becomes better for the person after seeing or using this?
2. **Delta:** What does Vesper add beyond replaying what the person supplied?
3. **Evidence:** Which authorized sources support every consequential claim?
4. **Placement:** Why is this durable Life value rather than timely Home,
   spatial Places, or conversational Chat value?
5. **Effort:** Does it deliver complete value before asking for reflection,
   correction, sharing, or action?
6. **Restraint:** Does it avoid identity claims, forced nostalgia, and false
   certainty?
7. **Counterfactual:** Is it meaningfully better than keeping the same material
   in Google Photos, Maps, notes, and a stateless AI chat?

If the counterfactual is unclear, the unit does not earn top-level placement.

## 7. Evaluation fixtures before further visual design

> **2026-08-29 resolution:** Round 4 resolved the memory-job, dividend,
> transfer, social-memory, resurfacing, and cold-start questions. The resulting
> [Life Outcome Storyboard
> Pack](life-outcome-storyboard-pack-2026-08-29.md) now owns the active value
> gate before visual composition.

The pack uses four complete outcomes over one evidence world:

1. **Recover:** a vague recollection retrieves the exact item and surrounding
   truth.
2. **Re-enter:** reconstruction and new understanding combine into one
   evidence-led experiential return.
3. **Carry:** a supported Europe mechanism improves a concrete New York
   possibility and may later produce a causal receipt.
4. **Together:** an authorized human contribution creates an attributed
   contrast or route to the person who knows.

The earlier `Reconstruct` and `Understand` labels are intentionally combined
inside Re-enter. A reconstruction that adds no new representational or
epistemic value is only a record; an explanation with no path back to the lived
evidence is not a Life return.

For each storyboard, compare:

```text
what the person already knows
what evidence Vesper has
what Vesper adds
what changes after the return
where the value is projected now
what remains durable in Life
what Vesper deliberately does not claim or ask
```

Only after these four outcomes are compelling should the team return to the
default Life composition. The page can then be shaped around proven kinds of
value instead of hypothetical content slots.

## 8. Product measures

The existing HCI research suggests measures that are closer to the thesis than
engagement:

- **representational gain:** did Vesper produce a more useful account than the
  original fragments?
- **epistemic gain:** did the person learn a grounded relation or mechanism
  they did not already know?
- **capability transfer:** did the return improve later perception, judgment,
  coordination, or action?
- **second-occasion benefit:** did a related later experience require less
  explanation or become meaningfully better?
- **retrieval success:** did the person recover the intended target from a
  natural contextual cue?
- **relational gain:** did plural evidence improve connection or an occasion
  without violating authority?
- **attention dividend:** was the value greater than the effort previously
  spent contributing and correcting evidence?
- **earned return rate:** when Life resurfaced something, did the person judge
  that return useful rather than merely accurate?

Time spent, feed depth, artifact count, and reflection completion are not
primary success measures.

## 9. Decision

Pause further visual composition of the Life index. Preserve the fixture,
authority, retrieval, and rendering research as enabling work. Insert a
value-definition gate before any founder selection of a page composition or
projection schema.

Life has earned a credible role in the four-root system, but not yet a final
page. Its existence will be justified when accumulated evidence creates
visible practical, epistemic, relational, and future value—not when the corpus
has been elegantly organized.

## Sources

- Sow and Janssen, “Developments in the functions of autobiographical memory:
  An advanced review,” *WIREs Cognitive Science* (2023):
  https://wires.onlinelibrary.wiley.com/doi/10.1002/wcs.1625
- Sedikides et al., “Self-Continuity,” *Annual Review of Psychology* (2023):
  https://www.annualreviews.org/content/journals/10.1146/annurev-psych-032420-032236
- Sellen and Whittaker, “Beyond Total Capture: A Constructive Critique of
  Lifelogging,” *Communications of the ACM* (2010):
  https://www.microsoft.com/en-us/research/publication/beyond-total-capture-a-constructive-critique-of-lifelogging-2/
- Epstein et al., “A Lived Informatics Model of Personal Informatics,”
  *UbiComp* (2015): https://pmc.ncbi.nlm.nih.gov/articles/PMC12435389/
- Google Photos Help, “Use Ask Photos to search, edit and get assistance”:
  https://support.google.com/photos/answer/15318661
