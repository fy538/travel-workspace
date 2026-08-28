---
doc_type: working
status: active
owner: founder / product / design / research
created: 2026-08-27
last_verified: 2026-08-28
expires: 2026-09-26
why_new: The adaptive-composition lab established a bounded implementation contract, but it did not answer whether the product direction is worth building or which decisions can be resolved before product-specific testing. This memo evaluates those questions through a-priori reasoning, HCI research, and adjacent-product evidence.
promotes_to: null
supersedes: []
source_of_truth_for: []
---

# Adaptive Experience Composition: A-Priori and Adjacent-Product Research

> This is a product-strategy research memo, not a production decision, a new
> architecture authority, or evidence that adaptive composition has produced
> user value in Vesper.

## 1. Executive verdict

**The broad direction is worth designing. More resolver infrastructure is not
yet worth building.**

We can answer a substantial part of the question before another product test:

1. Different immediate jobs deserve different representations. Spatial,
   temporal, comparative, social, and consequential relationships are not
   equally legible in prose or in a generic card.
2. The object must remain stable while the representation changes. Identity,
   revision, audience, provenance, authority, and correction cannot be inferred
   anew by each surface.
3. Adaptation should happen at intelligible job or lifecycle boundaries, not by
   continuously rearranging familiar controls.
4. Automatic adaptation is most defensible for high-confidence operational
   state. User invocation or confirmation is safer for ambiguous intention,
   personal meaning, social expression, and consequential action.
5. A bounded native vocabulary is preferable to arbitrary generated UI. The
   host must retain geometry, accessibility, navigation, fallback, and action
   authority.
6. Silence and an ordinary host-native response are valid outcomes. The system
   should compose only when a different representation materially reduces work
   or makes a relationship perceptible.

These conclusions are supported by established representation and mixed-
initiative research and recur in successful products including Partiful,
Google Maps, Flighty, Polarsteps, Airbnb, Notion, and ChatGPT.

What cannot be answered a priori is narrower but important: Vesper's exact job
taxonomy, the correct intervention threshold, which root should show which
projection, whether users understand a transition, and the size of any benefit.
Those questions justify later product evidence. They do not justify treating
the entire concept as unknowable until it is built.

The current lab should therefore be treated as **a useful construction proof,
not a value proof**. Keep its semantic and safety principles. Pause expansion of
the resolver and shadow machinery. Use the research to redesign one complete
cross-root experience first.

## 2. The question we are actually answering

The weak framing is:

> Will people like an AI that dynamically changes the interface?

That framing combines several different ideas and invites an expensive,
uninformative experiment.

The stronger framing is:

> When one real-world object acquires a different immediate job, phase,
> audience, or consequence, can Vesper expose the smallest appropriate native
> instrument while preserving the object's truth and the person's control?

This is primarily an **experience-architecture and interaction-design
question**. AI may help infer a job or choose among bounded treatments, but AI
is not the reason a route should be spatial, a choice comparative, a flight
time-sensitive, or an event social.

## 3. Evidence standard

The memo separates three kinds of evidence:

| Evidence | What it can establish | What it cannot establish |
| --- | --- | --- |
| A-priori constraint reasoning | Logical, cognitive, safety, and authority requirements; contradictions in a proposed design | Demand, effect size, delight, retention, or the correct threshold |
| Adjacent-product evidence | Mechanism plausibility; recurring product patterns; commercial relevance of the underlying job | That the same mechanism caused another product's success or will transfer unchanged to Vesper |
| Vesper-specific behavioral evidence | Comprehension, transition quality, timing, threshold, changed action, and comparative benefit | Universal design law from one scenario or cohort |

Adoption, ratings, awards, and growth are treated as **success signals**, not
causal identification. Public product evidence rarely isolates one interface
mechanism from brand, distribution, network effects, data quality, pricing, or
execution.

## 4. What can be inferred a priori

### 4.1 Representation should match the operation

Larkin and Simon showed that informationally equivalent representations can
have very different computational efficiency because a diagram can make
relationships explicit and reduce search. This supports the basic Vesper claim:
putting route geometry, temporal dependencies, or option tradeoffs into prose
or a universal vertical card imposes unnecessary cognitive work.

This does not mean "make everything visual." It means choose a representation
whose native operations match the current job.

Source: [Larkin and Simon, *Why a Diagram Is (Sometimes) Worth Ten Thousand Words*](https://onlinelibrary.wiley.com/doi/10.1111/j.1551-6708.1987.tb00863.x).

### 4.2 Automation and direct control should be interwoven

Horvitz's mixed-initiative work rejects the false choice between autonomous
agents and direct manipulation. A system may infer, prepare, and bring forward
the useful instrument while people retain inspection and control of meaningful
action.

Source: [Horvitz, *Uncertainty, Action, and Interaction*](https://www.microsoft.com/en-us/research/publication/uncertainty-action-interaction-pursuit-mixed-initiative-computing/).

For Vesper, this implies:

- infer and prepare when context is strong;
- expose the reason and source when it matters;
- let the person steer, correct, dismiss, or return to the durable owner; and
- stop at the appropriate authority boundary.

### 4.3 Hidden rearrangement is not the same as useful composition

Research on adaptive menus is cautionary. In one controlled comparison,
user-adaptable menus performed best on both performance and satisfaction; an
automatically rearranged split menu was less efficient than expected and
degraded when selection frequency changed. The problem was not adaptation in
the abstract. It was movement that damaged predictability and spatial memory.

Source: [Park et al., *Adaptable versus adaptive menus on the desktop*](https://www.sciencedirect.com/science/article/pii/S0169814107000893).

This produces a hard distinction:

- **Good candidate:** the same trip becomes a route when the person needs to
  move and a timeline when the person needs to follow commitments.
- **Bad candidate:** familiar controls or navigation items silently move because
  the system predicts that they may be useful.

### 4.4 AI behavior must be legible across time and error

The 18 Guidelines for Human-AI Interaction were validated with 49 design
practitioners against 20 AI-infused products. They cover initial expectation,
in-interaction relevance, failure and correction, and behavior over time.
Microsoft's implementation guidance further warns that explanation itself can
inflate trust and create automation bias.

Sources: [Amershi et al., *Guidelines for Human-AI Interaction*](https://doi.org/10.1145/3290605.3300233),
[Microsoft HAX guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/),
and [HAX explanation guidance](https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-why-the-system-did-what-it-did/).

The implication is not to display a rationale panel everywhere. Vesper should
make a reason available in proportion to uncertainty, novelty, consequence,
and potential harm.

### 4.5 Feedback must produce recognizable control

Google PAIR recommends balancing automation with control, allowing people to
edit or turn off AI output, making data use visible, and supporting changing
preferences. It explicitly notes that real-world context and the person's
relationship to a task determine when automation is welcome.

Source: [Google PAIR, Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/).

This supports Vesper's correction, dismissal, release, and reset requirements.
It also argues against treating taps as an invisible training signal for
interface morphology.

### 4.6 Native stability is compatible with contextual form

Apple's HIG treats consistency as the use of familiar platform conventions
while interfaces adapt across displays. Material Design similarly recommends
building on a small set of canonical layouts rather than inventing arbitrary
structures for every state.

Sources: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines?lang=en)
and [Material Design canonical layouts](https://m3.material.io/foundations/layout/canonical-examples/overview).

The transferable law is: **adapt the content composition and semantic
instrument; preserve the platform interaction language.**

## 5. Adjacent-product teardowns

### 5.1 Partiful — one social object across an event lifecycle

**Durable object:** an event and its bounded participant world.

**Morphology:**

```text
possible event
  -> time poll
  -> invitation and RSVP
  -> guest questions and social context
  -> reminders and host updates
  -> live attendance context
  -> shared photos and continued connection
```

The same shareable event page supports date polling, RSVPs, guest questions,
comments and reactions, reminders, updates, and post-event photos. Host
settings control guest approval, +1s, guest-list visibility, audience, and
ticketing. Guests can enter through a link rather than first adopting the whole
product.

Sources: [Partiful product page](https://partiful.com/),
[why use Partiful](https://help.partiful.com/en-us/articles/15525594-why-use-partiful),
and [event settings](https://help.partiful.com/en-us/articles/15525301-what-features-are-available-to-change-in-my-event-settings).

**Success signal:** TIME reported that user activity rose 600% in 2024, the
product added more than 2 million new users in Q1 2025, and it reached people in
more than 100 countries. TechCrunch, citing Appfigures, reported fourfold weekly
download growth during 2024 and Google's Best App of 2024 recognition.

Sources: [TIME100 Companies 2025](https://time.com/collections/time100-companies-2025/7289589/partiful)
and [TechCrunch](https://techcrunch.com/2024/11/18/partiful-is-googles-best-app-of-2024/).

**What the case supports:** social coordination becomes easier when invitation,
attendance, communication, and afterglow remain attached to one legible social
object. Role and phase change what is available without changing what the event
is.

**What it does not prove:** Partiful does not demonstrate that an AI should
infer the event's interface or that a universal event model transfers to all
Vesper objects. Its growth also benefits from link distribution and event
network effects.

**Vesper transfer:** Occasion is more important than a social treatment card.
The Occasion should be the stable core; polling, audience, route, coordination,
receipt, and afterglow should be phase- and authority-specific instruments over
that core.

### 5.2 Google Maps — a place or journey changes with the physical job

**Durable objects:** Place, route, and journey.

**Morphology:**

```text
place possibility
  -> search and comparison
  -> route alternatives
  -> turn-by-turn navigation
  -> arrival, parking, and final walking leg
  -> contribution or history
```

Google Maps moves among place discovery, questions about place qualities,
route comparison, lane-level navigation, traffic/weather anticipation, and
arrival guidance. It does not insist that a place detail card perform the work
of a navigation surface.

**Success signal:** Google reported more than 2 billion monthly Maps users. Its
20-year retrospective reports 1 trillion kilometers of directions in 2024 and
500 million annual contributors.

Sources: [Google Maps and Gemini update](https://blog.google/products-and-platforms/products/maps/gemini-google-maps-navigation-updates/)
and [Google Maps at 20](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/).

**What the case supports:** a physical-world product can retain object identity
while letting the current operation dominate. Navigation is automatic and
stateful where the goal is explicit; browsing and choice remain explorable.

**What it does not prove:** Maps' success is inseparable from coverage, data,
distribution, and utility. It does not prove that more proactive or
conversational behavior is always better.

**Vesper transfer:** Places should own spatial morphology. Chat may initiate or
interpret a route, but it should not miniaturize the whole route into a generic
chat card when movement is the job.

### 5.3 Flighty — state-machine adaptation around one high-stakes object

**Durable object:** a flight.

**Morphology:**

```text
future flight
  -> morning-of and check-in assistance
  -> airport and gate state
  -> delay/cancellation explanation
  -> Live Activity and progress
  -> connection assistance
  -> historical passport
```

Flighty attaches notifications, delay prediction, gate changes, inbound-aircraft
explanation, Live Activities, connection checkpoints, and later travel history
to the same flight. The form is driven mainly by time and operational state,
not by speculative personalization.

Sources: [Flighty App Store listing](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008)
and [Flighty product philosophy](https://flighty.com/about).

**Success signal:** Flighty reports millions of users and won a 2023 Apple
Design Award; its US App Store listing currently shows a 4.8 rating across
roughly 148,000 ratings.

Source: [Flighty press information](https://flighty.com/press).

**What the case supports:** the strongest automatic composition occurs when a
canonical object has an explicit state machine, the immediate job is clear, and
latency or omission has a real cost.

**What it does not prove:** travel inspiration, interpersonal meaning, and
ambiguous intent do not have flight-like state certainty.

**Vesper transfer:** automate confidently around commitments and provider
changes; remain conservative around interpretation, relationship, and memory.

### 5.4 Polarsteps — one trip from intention to lived trace to memory

**Durable object:** a trip.

**Morphology:**

```text
planned itinerary
  -> mapped route and stays
  -> automatic trip tracking
  -> photos, video, and authored steps
  -> audience-scoped following
  -> recap, reel, statistics, and physical book
```

Polarsteps explicitly spans planning, tracking, sharing, reliving, and a
physical keepsake. The trip's representation changes from prospective plan to
live route to retrospective story without requiring separate user-created
objects for each phase. Audience can be limited to the person, friends and
family, or the public.

**Success signal:** Polarsteps reports more than 22 million travelers and a 4.7
rating across roughly 370,000 ratings.

Source: [Polarsteps product page](https://www.polarsteps.com/).

**What the case supports:** continuity can be a product loop rather than an
archive. A single trip may legitimately become plan, live spatial trace,
social update, recap, and keepsake.

**What it does not prove:** capture can easily become the experience, and
retrospective media production is not Vesper's thesis. The case demonstrates a
continuity mechanism, not the desired attention ethic.

**Vesper transfer:** Life should show transformation and earned continuity, not
a reverse-chronological dump. Preserve the distinction among intended,
occurred, personally meaningful, and publicly shared.

### 5.5 Airbnb — a reservation becomes a group trip context

**Durable objects:** listing, reservation, and trip.

**Morphology:**

```text
search and map
  -> collaborative wishlist and votes
  -> booking and reservation
  -> Trips itinerary and check-in
  -> group messages and shared pins
  -> in-stay services/experiences
  -> review and continued connection
```

Airbnb's 2025 app redesign changes emphasis after booking: the app suggests
services and experiences based on where the person is staying and who is with
them, then presents check-in information and a day-by-day itinerary on arrival.
Collaborative wishlists support notes, votes, dates, and guest count. Joined
travelers gain scoped access to reservation details, group messages, and shared
map pins; removing a traveler removes their access and pins from the shared
itinerary.

Sources: [Airbnb 2025 Summer Release](https://news.airbnb.com/airbnb-2025-summer-release/),
[collaborative wishlists](https://www.airbnb.com/help/article/1236),
[group reservation access](https://www.airbnb.com/help/article/1175),
and [shared itinerary pins](https://www.airbnb.com/help/article/4192).

**Success signal:** Airbnb reported more than 2 billion cumulative guest
arrivals when it launched the redesigned app.

**What the case supports:** the same travel object can expose different
capabilities before booking, before arrival, during a stay, and afterward;
membership and access must travel with the object.

**What it does not prove:** the new lifecycle features are recent, and public
evidence does not isolate their incremental effect. Airbnb is also extending a
transactional marketplace, not demonstrating Vesper's broader lived-experience
model.

**Vesper transfer:** membership, audience, shared messages, spatial pins, and
operational truth should be scoped by Occasion participation rather than copied
into independent surface cards.

### 5.6 Notion — stable semantics, multiple user-legible views

**Durable objects:** block, page, data source, and database item.

Notion stores heterogeneous front-end forms through a consistent block model.
Its databases let people view the same data as a table, board, list, calendar,
timeline, gallery, form, chart, map, or dashboard. Views own filters, sorting,
and layout while the underlying records remain the same.

Sources: [Notion's block model](https://www.notion.com/blog/building-and-scaling-notions-data-lake)
and [Notion view documentation](https://developers.notion.com/guides/data-apis/working-with-views).

**Success signal:** Notion reported passing 100 million users in August 2024.

Source: [Notion, *100 Million of You*](https://www.notion.com/blog/100-million-of-you).

**What the case supports:** stable semantics plus several purposeful views is a
proven product architecture. Crucially, the view is visible and generally
chosen by the user; Notion does not continually hide or rearrange the database
because it predicts a different job.

**Counterevidence from the same company:** Notion initially expected people to
use AI primarily for first-draft generation. Alpha behavior showed that people
more often highlighted existing text and used AI to revise it; "Improve
Writing" became the dominant command, prompting a redesign.

Sources: [Notion AI launch learning](https://www.notion.com/blog/notion-ai-is-here-for-everyone)
and [Notion's retrospective](https://www.notion.com/blog/lessons-we-learned-from-launching-notion-ai).

**Vesper transfer:** the architecture of canonical truth plus projections can
be decided before launch. The frequency and salience of particular jobs cannot.
Let users explicitly enter ambiguous views; reserve automatic selection for
high-confidence context.

### 5.7 ChatGPT — a stable conversational substrate with specialized instruments

**Durable objects:** conversation/thread, user inputs, assistant outputs, tool
activity, tasks, and artifacts.

The observable product pattern is a stable conversational entry point that can
coordinate different workflows and specialized work surfaces instead of
forcing every result to remain plain text. Official OpenAI documentation for
ChatKit distinguishes user and assistant messages, widget payloads, client tool
calls, tasks, and task groups inside one thread. OpenAI's use-case library also
presents one shell spanning research synthesis, dashboards, documents, code,
browser action, and connected-app workflows.

Sources: [OpenAI ChatKit thread items](https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/threads/methods/list_items)
and [ChatGPT use cases](https://learn.chatgpt.com/use-cases).

**What the case supports:** conversation can be the universal intake and
coordination layer without being the only visual or durable owner. A bounded
widget or task surface can coexist with the transcript.

**What it does not prove:** official OpenAI documentation reviewed here does
not establish how much specialized work surfaces caused ChatGPT's adoption or
retention. ChatGPT is therefore a strong design precedent but weak causal
evidence for this particular mechanism.

**Vesper transfer:** Chat should move a person into the right Place, Occasion,
Plan, comparison, route, or receipt. It should not become a universal container
that miniaturizes every product surface.

## 6. Cross-case synthesis

### 6.1 The recurring architecture

Across the cases, successful morphology looks like:

```text
durable domain object
  + explicit lifecycle state
  + current job
  + viewer role and audience
  + fresh operational truth
  -> one recognizable native instrument
  -> action or understanding
  -> return to the same durable object
```

The products differ in category, but the recurring move is not "AI invents a
screen." It is **one object, several disciplined projections**.

### 6.2 Where automation is strongest

Automatic transition is best supported when:

- the object is unambiguous;
- the lifecycle state is externally or temporally observable;
- the immediate job follows directly from that state;
- the treatment is reversible or read-only;
- delay or omission has a meaningful cost; and
- the fallback preserves the same truth.

Examples include an approaching flight, a changed gate, a live route, a check-
in window, or an accepted event whose reminder time has arrived.

### 6.3 Where invocation or confirmation is stronger

User-led transition is better supported when:

- intent is exploratory or ambiguous;
- several representations are honestly useful;
- the action expresses taste, meaning, or authorship;
- the audience may change;
- a shared decision affects other principals; or
- the consequence is expensive, public, or weakly reversible.

Examples include choosing a Notion view, writing an event message, interpreting
why a place matters, publishing a trip memory, or authorizing a group change.

### 6.4 Success comes from compression, not morphing itself

The adjacent cases each compress a fragmented real-world job:

| Product | Fragmentation compressed |
| --- | --- |
| Partiful | invitation, RSVP, guest coordination, reminders, and afterglow |
| Google Maps | discovery, spatial comparison, routing, navigation, and arrival |
| Flighty | schedule, operational truth, alerts, airport action, and flight history |
| Polarsteps | planning, tracking, sharing, reflection, and keepsake creation |
| Airbnb | search, group choice, booking, check-in, itinerary, and host communication |
| Notion | data storage and several task-specific operational views |
| ChatGPT | natural-language intake and heterogeneous knowledge-work instruments |

This is the economically relevant proposition. Users do not value an interface
because it changed shape. They value reduced coordination, search, recall,
interpretation, and action cost.

## 7. What this means for Vesper

### 7.1 The opportunity is plausible

Vesper's thesis identifies a real fragmentation problem across search, saves,
routes, itineraries, messages, reservations, invitations, and memories. The
adjacent cases show strong demand for products that unify subsets of this
fragmentation around an event, place, flight, trip, reservation, or workspace.

Vesper's distinctive hypothesis is that a permissioned compilation of person,
relationship, Place, Moment, Occasion, Commitment, Source, and Outcome can
choose a better immediate instrument and carry consequences across those
objects.

That hypothesis is **plausible enough to justify serious design work**.

It is not yet plausible enough to justify a universal composition engine. Every
successful adjacent product is narrower than Vesper at its center. Breadth is
the opportunity and the primary failure risk.

### 7.2 The design center should be the object, not the resolver

The current lab begins conceptually with:

```text
primary job -> treatment
```

The adjacent research suggests a richer and safer order:

```text
canonical domain object
  -> lifecycle and truth state
  -> viewer role, audience, and authority
  -> current attention and job
  -> root-native projection
```

The resolver can later implement a bounded part of this chain. It should not
become the conceptual center of the product.

### 7.3 Root-native projection is supported

The four-root hypothesis becomes more credible when roots are treated as stable
operations over shared truth:

| Root | Native operation |
| --- | --- |
| Home | Attend to one dominant current consequence while composing a bounded, diverse possibility field around it |
| Chat / Vesper | Ask, interpret, negotiate, prepare, and recover |
| Places | Orient, inspect spatial feasibility, and encounter Place |
| Life | Inspect earned continuity, plural outcomes, and relationships over time |

The same object may appear in several roots, but the root should not merely
restyle an identical card. It should expose the operation that root exists to
support.

### 7.4 The strongest Vesper cases are not equally certain

| Case | Prior confidence | Reason |
| --- | --- | --- |
| Commitment becomes sequence/receipt as reality changes | High | Flighty, Airbnb, and Maps show strong state-driven precedent |
| Place or route becomes spatial when movement is the job | High | Representation theory and Maps strongly support it |
| Occasion becomes social/comparative as participation changes | Medium-high | Partiful and Airbnb support the object and authority pattern |
| Trip becomes plan, live trace, and retrospective continuity | Medium-high | Polarsteps and Airbnb support lifecycle transformation |
| Vesper infers interpretive or relational form without invocation | Medium-low | Intent and meaning are ambiguous; trust and authorship costs are high |
| One generic resolver governs every object and root | Low | No adjacent product establishes this breadth; predictability risk is high |

## 8. Reassessment of the current lab and resolver

### 8.1 Stable decisions to retain

- canonical identity, revision, audience, authority, provenance, freshness,
  correction, and owner remain stable across projections;
- server/application layers do not send arbitrary component trees, styling,
  coordinates, gestures, or navigation;
- the native client owns geometry, accessibility, interaction, fallback, and
  platform conventions;
- a bounded component/treatment catalog is safer than generated code;
- quiet and host-native sufficiency are complete outcomes;
- environmental degradation changes presentation, not meaning;
- one dominant job should organize a surface; and
- direct manipulation of a projection must not silently mutate durable truth.

### 8.2 Decisions that should return to provisional status

- the exact seven-job taxonomy;
- the claim that eight treatments cover the whole product;
- a universal maximum of two supporting instruments;
- fixed supporting-treatment priority across all objects and roots;
- `contextConfidence` as a three-value universal input;
- treatment selection before explicit object lifecycle and role state; and
- the Places shadow lane as evidence that the product direction deserves
  visible rollout.

These may remain useful fixture constraints. They are not established product
laws.

### 8.3 What the shadow lane proves—and does not prove

The Places/orient shadow lane can prove that two implementations make the same
deterministic decision under scrubbed inputs. It can help catch policy drift and
privacy mistakes.

It cannot show:

- that the spatial instrument improves orientation;
- that Places should be selected automatically;
- that users understand the transition;
- that the same policy generalizes to another object or root;
- that adaptive composition improves retention or willingness to pay; or
- that the broader product is worth building.

Do not expand shadow coverage until another root/job pair has first earned a
clear product rationale through design.

## 9. Recommended product decision

### Adopt now

Adopt this design doctrine:

> Vesper preserves durable domain truth and exposes the smallest root-native
> instrument that materially reduces the current person's work. Automatic form
> changes require explicit object state and high-confidence context. Ambiguous
> meaning, audience, and consequence remain human-steered.

### Pause now

Pause:

- additional resolver inputs;
- new shadow lanes;
- production telemetry for treatment choice;
- attempts to certify the eight-treatment vocabulary across the full product;
- universal composition schemas; and
- optimization around taps, time on surface, or engagement.

### Design next

Design one reference object all the way through its lifecycle and roots. The
best candidate is the Rome group Occasion because it exercises the strongest
adjacent precedents without requiring a universal model:

1. **Before:** fragment or invitation enters through Chat; Occasion core is
   established with explicit membership and authority.
2. **Prepare:** Home shows one current commitment; Places owns route and heat-
   aware spatial feasibility; Chat owns interpretation and negotiation.
3. **Decide:** a bounded comparison exposes honest axes and affected principals;
   authorization returns a receipt to the Occasion.
4. **Live:** temporal and spatial instruments respond to explicit commitment and
   provider/world state; silence wins when no action is required.
5. **After:** Life distinguishes shared occurrence from plural outcomes and
   offers only earned continuity.
6. **Return:** a later occasion must become materially different because of
   authorized prior evidence, or continuity has not earned its cost.

The artifact should be a screen-by-screen product composition with transitions,
copy, control, and fallback—not another resolver or test harness.

## 10. Remaining empirical questions

After that design exists, evidence should focus only on uncertainties research
cannot settle:

1. Do people recognize that the object is the same when its representation
   changes roots or phase?
2. Does the instrument reduce reconstruction work compared with the current
   product?
3. Is the reason for the transition legible without explanation clutter?
4. Can people predict where durable truth and correction live?
5. Does automatic composition appear only when the job is genuinely clear?
6. Does the interface recede quickly enough once the job is complete?
7. In multiplayer cases, can every participant distinguish shared occurrence,
   private context, authority, and personal outcome?
8. Does authorized continuity materially improve a second occasion?

These are design questions with behavioral consequences. They should be
answered through a small number of comparative, realistic scenarios—not a
broad instrumentation program.

## 11. Final answer to “can we know whether it is worth building?”

We cannot infer the ROI or final product-market fit of adaptive experience
composition from first principles.

We **can** infer enough to make a responsible product decision:

- the underlying problem is real and repeated across successful adjacent
  categories;
- task-appropriate representations have a strong cognitive basis;
- stable objects with lifecycle-specific instruments are a recurring product
  architecture;
- bounded, native, user-legible composition has a stronger evidence base than
  arbitrary adaptive UI;
- Vesper already possesses domain truths whose relationships are poorly served
  by a universal chat card; and
- the remaining uncertainty concerns the quality and value of a specific
  experience, not whether the entire direction is intellectually plausible.

Therefore the correct commitment is neither “build the platform” nor “test the
idea indefinitely.” It is:

> **Commit to the design direction; withhold commitment to the universal
> resolver; produce one exceptional end-to-end object lifecycle before further
> implementation.**

## 12. Source notes and limitations

- Product pages and help centers are primary evidence for behavior but are
  marketing sources for quality claims.
- Company-reported user counts, ratings, awards, guest arrivals, and usage are
  success signals, not audited causal evidence for an interface mechanism.
- TIME, TechCrunch, and Appfigures-derived Partiful figures are secondary
  reporting and should not be treated as internal metrics.
- Official OpenAI documentation establishes the heterogeneous thread and
  workflow pattern used in this memo; it does not attribute ChatGPT's adoption
  to specialized surfaces.
- No public source reviewed establishes that invisible, AI-selected interface
  morphology is itself a durable growth driver. The strongest evidence supports
  stable objects, phase-aware instruments, clear control, and work compression.
