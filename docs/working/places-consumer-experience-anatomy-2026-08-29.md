---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Resolves the stable consumer anatomy of Places after reconciling the authoritative vesper-home-surfaces 2 canvas, the current Places implementation, the four-root contract, and the five-world Home and Places fixtures.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/systems/four-root-loop-object-surface.md
  - docs/working/home-and-places-underexplored-value-research-2026-08-29.md
  - docs/working/home-and-places-five-world-fixture-pack-2026-08-29.md
  - docs/working/hci-rebased-home-composition-contract-2026-08-28.md
  - travel-agent/docs/product/Product Model.md
  - travel-agent/docs/product/Place Relationship Surface.md
  - travel-agent/docs/product/Place Interpretation and Content Intelligence.md
  - travel-app/docs/Design Language.md
---

# Places Consumer Experience Anatomy

## Decision

Places should become one navigable world surface with three stable consumer
states and one cross-cutting reduction:

1. **World Field** — no Place is selected; the person is orienting among a
   finite set of spatially meaningful possibilities.
2. **Place Focus** — one Place is selected; stable world truth, current
   affordance, the person's relationship, and meaningful perspectives are
   composed around that Place.
3. **Place Path** — one question, connection, route, comparison, or hidden
   system is being followed from the focal Place.
4. **Live Reduction** — when time, conditions, or burden become decisive, any
   of the three states compresses toward feasibility, alternatives, and one
   stable next step.

These are interaction states, not tabs, permanent page sections, content
types, or backend owners. A person should experience them as one continuous
Place encounter:

```text
World Field
  -> select a Place
Place Focus
  -> follow one meaningful edge
Place Path
  -> act, continue, or return with context preserved
```

The stable product promise is:

> **Places makes the world around a Place intelligible, usable, and connected
> to the rest of the person's life.**

The immediate implementation target is not a visual redesign or a generalized
graph. It is a semantic prototype contract that can be rendered in a dedicated
design tool after the interaction model is accepted.

## 1. Why the current shape feels incomplete

The corrected `vesper-home-surfaces 2` bundle is substantially richer than a
generic recommendation feed. It already explores:

- data-gated sections mixed within a posture rather than one fixed mode;
- nearby sets, editorial readings, experiences, saved Places, memories,
  changes, and friend activity;
- one Place expressed through recommendation, verdict, apparatus, change,
  caveat, and personal-history registers;
- a map and a sequence as two renderings of the same composed route;
- multiple readings of one Place;
- return, belonging, personal record, and social co-sign concepts; and
- density taper as a way to let a long page wind down.

The bundle also names its own decisive gap: none of its whole pages shows
**one Place in depth**, because no reason emits a one-card Place section. Its
pages remain ranked stacks of server-produced reasons. The result is a strong
content inventory without a complete consumer navigation model.

The current code has the same split:

- the Places root is a server-authored section feed;
- search can replace the feed;
- map is a separate route and workspace;
- city and neighbourhood detail is a separate lens-led page;
- venue detail has identity, current situation, Take, relationship, facts,
  and Ask; and
- none of those views shares one explicit path model or preserves a Home
  proposition as the person moves through them.

This is why Places can feel simultaneously rich and catalog-like. The parts
exist, but the person is still navigating containers and features rather than
following a legible relationship with the world.

## 2. What to keep from the authoritative canvas

### 2.1 Keep posture as a modifier, not an information architecture

The canvas correctly observes that postures mostly set **length**, while
producers remain data-gated. A person between trips can still have local
events, saved Places, a changed venue, and a useful human trace.

Preserve this principle:

> **Situation changes selection, prominence, density, and available action;
> it does not switch Places into a different product.**

Do not create separate permanent Starter, Between, Planning, Ready, Live,
Returned, Trip, and Quiet page architectures.

### 2.2 Keep medium variety

The canvas is right to use different forms for different jobs:

- map fragment for spatial relationship;
- numbered walk for temporal order;
- then/now diff for a changed fact;
- dated stub for an event;
- editorial cover or lens switcher for interpretation;
- source apparatus for a claim;
- friend strip or co-sign for attributed human evidence;
- log for personal history; and
- compact rows for alternatives and doors.

This is not decorative variety. The medium should expose the structure of the
value being returned.

### 2.3 Keep the one-Place registers

Recommendation, verdict, apparatus, change, caveat, and personal log are not
six unrelated cards. They are six possible answers to:

> **What is useful to say about this Place right now?**

That is the right semantic collapse. The current evidence and question choose
the register. The UI must not show all six as a menu or checklist.

### 2.4 Keep the density taper

The bundle's rhythm study finds that only the taper controls both emphasis and
page height: the strongest material is fully expressed, middle material is
compressed, and the tail becomes compact doors.

Adopt that semantic rule without adopting exact geometry:

```text
one full lead
  -> two or three standard paths
  -> compact continuity doors
  -> stop when the marginal value no longer beats silence
```

### 2.5 Keep explicit absence

The canvas is right that a short page is not an error and should not be padded.
Places may show one strong composition, a small set, or nothing beyond stable
orientation. Silence protects the credibility of future contributions.

## 3. What must change

### 3.1 The root cannot remain a ranked section feed

`reason`, `treatment`, and producer rank are useful server concepts. They
should not define the person's mental model. A root assembled as eight
unrelated sections still reads as a feed even if every section is good.

The composition unit must become a **spatially anchored path from a current
scope**, not a section reason looking for a card renderer.

### 3.2 A mast cannot explain the product on every open

The canvas places a posture-specific mast on every page. This consumes the
highest-attention position to describe Places rather than return value.

Use a mast only when the scope itself needs orientation, such as true cold
start or a newly entered city. In ordinary use, lead with the strongest true
composition or the focal Place identity.

### 3.3 Search and map cannot feel like adjacent products

Search is a utility for naming or narrowing the world. Map is a medium for
understanding geometry. Neither should replace the semantic state.

- Search should preserve the current scope and question.
- Map and list/composition views should be transformations of the same result
  set or path.
- Selecting a pin, row, social trace, or Home opening should converge on the
  same Place Focus.

The current separate map route may remain during implementation, but it must
receive and return the same typed context envelope.

### 3.4 Editorial lenses cannot be the Place's primary navigation grammar

The current city page leads with fixed editorial lens labels. Multiple
perspectives are valuable, but the user should not need to understand an
internal lens taxonomy before understanding a Place.

The current question should select the perspective. Labels such as source,
stance, or read time may remain as provenance. `Why here`, `Insider`,
`Tension`, and related lens names should not become six permanent navigation
tabs.

### 3.5 Social material must escape trip-only scope

The corrected canvas notes that friend activity currently renders only when
the context is a trip and the viewer is a member. That is an implementation
boundary, not the target multiplayer philosophy.

Places needs authorized human evidence whenever it materially changes a Place
understanding or possibility:

- what a friend noticed here;
- a Place they shared directly;
- a contemporaneous contrast from another Place;
- a prior group outcome that changes what works now; or
- a bounded invitation or contribution attached to an Occasion.

This must remain trace-first, attributed, audience-governed, and sparse. It is
not a friend-activity feed or ambient location surveillance.

### 3.6 Personal relationship cannot remain a late catalog section

Saved items, return history, memories, prior companions, learned distinctions,
and repeated outcomes are not one more shelf behind events and editorial
content. They change how the whole Place should be read.

Relationship is therefore a projection input throughout Place Focus and Place
Path, not a permanent `Your history` module at the bottom.

## 4. The three stable states

### 4.1 World Field — orient among meaningful possibilities

### User question

> **What is possible in the world I am looking at, and where should I look
> more closely?**

### Entry conditions

- opening the Places root;
- returning from a Place or path;
- searching a city, neighbourhood, category, or need;
- opening a shared set or Occasion geography; or
- switching from map to composition view without one focal Place.

### Stable anatomy

1. **Scope handle**
   - names the actual scope: current area, searched place, planned area,
     shared set, or saved world;
   - exposes freshness or location basis when relevant;
   - allows search and scope change without resetting the whole experience.
2. **Spatial field**
   - shows the geometry necessary to understand the lead set;
   - may be a map, route fragment, neighbourhood field, distance relation, or
     spatially ordered list;
   - does not require a full-screen map when geometry is not material.
3. **Lead opening**
   - the strongest complete-value proposition in the scope;
   - may be one Place, a pair, a route, an event, or an explanatory path;
   - states why it belongs here without asking the user to assemble the value.
4. **Finite branch set**
   - two to four meaningfully different paths, alternatives, or areas;
   - differences are explicit; generic similarity is not enough.
5. **Continuity doors**
   - compact doors into saved Places, prior episodes, people, or a broader map;
   - appear only when the relationship is relevant to this scope.

### World Field is not

- an infinite recommendation feed;
- a generic map covered in pins;
- a dashboard of saved counts;
- a posture report;
- a list of every content producer; or
- a prompt asking what the person wants.

### Selection rule

Every visible item must answer at least one of:

- why this Place or path matters in this scope;
- what becomes possible here;
- what changed;
- what the person can understand here that was previously opaque;
- what a trusted person or prior outcome adds; or
- where this leads next.

### 4.2 Place Focus — understand one Place as world and relationship

### User question

> **What is this Place, what does it afford now, what is my relationship to
> it, and what is worth following from here?**

### Stable anatomy

1. **Place identity**
   - the most specific true name and spatial scope;
   - stable identity and geometry;
   - image, illustration, map, or text treatment chosen by evidence and job,
     not by a mandatory hero template.
2. **Current read**
   - the single most useful register now: verdict, current condition, change,
     caveat, source-grounded interpretation, or recommendation;
   - includes freshness and important uncertainty when material.
3. **Relationship trace**
   - the smallest useful expression of the viewer's prior evidence: saved,
     planned, lived, returned, contributed, or learned;
   - never turns relationship stages into badges, progress homework, or
     inferred personality.
4. **Plural perspective**
   - one or two genuinely different readings when disagreement, human
     perspective, or stance improves understanding;
   - names author/source and audience rights;
   - does not manufacture balance when the evidence is not plural.
5. **Horizon doors**
   - two to four typed, directional connections to another Place, person,
     mechanism, event, route, or future possibility;
   - each states the relation, the useful similarity, and the important
     difference;
   - generic `more like this` is rejected.
6. **Action seam**
   - inspect feasibility, start a route, add to a Plan or Occasion, ask in
     Chat, contribute a situated Artifact, share a bounded projection, or
     correct the record;
   - action appears after value, not as a substitute for it.

### Progressive depth

Place Focus should follow:

```text
cue
  -> Vesper take
  -> evidence or source
  -> deeper perspective
  -> action or horizon
```

The first screenful must stand on its own. The person should not need to open
an article, expand six lenses, or answer a question to receive the core value.

### 4.3 Place Path — follow one connection without losing the Place

### User question

> **Show me how this connection works, what supports it, and what it changes
> for me.**

### Path types

- **Spatial** — nearby, along the way, ends near, reachable from, inside;
- **Temporal** — then/now, recurring, seasonal, open during, returns when;
- **Causal or hidden-system** — geology, infrastructure, ecology, economics,
  craft, policy, supply chain, or social practice;
- **Cultural or interpretive** — story, text, film, ritual, artwork, debate,
  or historical inheritance;
- **Practical transfer** — a distinction learned elsewhere that changes what
  the person can notice or do here;
- **Human** — an authorized observation, contrast, co-sign, dissent, or prior
  outcome from another person; and
- **Future** — an event, return, route, Occasion, or possibility that becomes
  newly actionable.

### Stable anatomy

1. **Origin** — focal Place and the exact cue that opened the path.
2. **Relation statement** — the typed, directional connection in plain
   language.
3. **Substance** — the new mechanism, distinction, contrast, route, or human
   evidence; never a restatement of what the person already supplied.
4. **Evidence apparatus** — Claims, Sources, freshness, uncertainty,
   disagreement, and audience scope at the grain the claim requires.
5. **Consequence** — what the connection changes in understanding,
   perception, feasibility, or next action.
6. **Branches** — at most two or three honest next paths, each materially
   different.
7. **Return** — back to the same Place Focus or World Field position with the
   followed path visibly retained.

### Path lifecycle

A Place Path is initially a read projection, not a universal durable graph
object. It may be recomposed from a two-to-four-edge `HorizonPath` brief.
Persist the authoritative Sources, Claims, Artifacts, actions, Outcomes, and
corrections. Promote a path itself only when repeated fixtures expose a stable
ownership need.

## 5. Live Reduction

Live is not a fourth Place page. It is a reduction applied when time,
conditions, burden, or an existing commitment dominate.

### Trigger

- a bounded interval is active;
- a Place is currently reachable or about to close;
- weather, transit, crowding, accessibility, inventory, or provider state is
  material;
- a route must end near a commitment;
- the person is already moving; or
- recovery from disruption matters more than discovery.

### Reduction rule

```text
stable identity stays
current facts rise
feasibility becomes explicit
alternatives shrink to meaningful branches
evidence remains inspectable
editorial depth recedes
one stable next step may lead
```

### Live anatomy

1. current position or selected Place;
2. available interval and end constraint;
3. strongest feasible path;
4. one meaningful alternative or fallback;
5. exact conditions and freshness;
6. burden: time, walking, heat, cost, booking, accessibility, or coordination;
7. action seam into route, Plan, Occasion, provider, or Chat; and
8. monitoring or expiry state when acting now would be premature.

Live Reduction must not silently book, publish, contact, or mutate shared
state. It follows the existing consequence contract.

## 6. Home-to-Places handoff

Home should never send the person to generic Places and make them rediscover
why they tapped.

### Required context envelope

- origin Home contribution and focal object;
- focal Place or spatial scope;
- immediate job;
- interval and end constraint;
- current conditions and freshness;
- selected Sources and Claims;
- known-to-person posture;
- human note with author and audience scope;
- unresolved tradeoff;
- action-authority ceiling;
- return destination; and
- expiry and correction lineage.

### Destination selection

| Home proposition | Places destination |
| --- | --- |
| “This waterfront afternoon still fits before dinner.” | Place Path with route geometry, branches, burdens, and end-near evidence |
| “A Place you saved changed.” | Place Focus with the change register leading |
| “Your friend's Paris observation changes how to read Rome.” | Place Path with attributed comparison, shared structure, and important difference |
| “The pasta distinction from Italy is useful in New York.” | Place Path with mechanism, candidate Places, and transfer limits |
| “This Place is worth returning to now.” | Place Focus with current affordance and prior relationship trace |

The destination owns depth and action. Home retains the compact proposition
and refreshes from canonical readback when the person returns.

## 7. Map, list, article, social, and operational media

The surface does not assign one medium to one state. Medium follows the job.

| Job | Lead medium | Supporting medium |
| --- | --- | --- |
| Understand proximity or route | Map or spatial diagram | ordered rows, burden receipt |
| Compare two honest branches | paired comparison or split path | compact map, reasons |
| Understand a hidden system | annotated explanation, flow, or article extract | sources, relevant Places |
| Understand current change | then/now diff | freshness, action consequence |
| Use a practical distinction | annotated evidence or short guide | candidate Places, limits |
| Follow human perspective | attributed note, juxtaposition, or co-sign | source Place, audience, dissent |
| Understand personal continuity | compact log, map, or timeline | episode and Artifact doors |
| Act under constraints | operational instrument | alternatives, receipt, monitoring |

An article, podcast, map, or generated guide may be surfaced in Places when it
is the best medium for the spatial question. It is not a separate content
shelf by default. The contribution must remain complete enough to provide
value before the person opens the long-form object.

## 8. Social anatomy

Social value in Places has four admissible forms:

1. **Attributed evidence** — what a person actually noticed, contributed, or
   experienced here.
2. **Relational relevance** — why this person's trace is useful to the viewer
   in this Place or question.
3. **Plural comparison** — how two authorized experiences reveal a meaningful
   difference without collapsing either person into a taste profile.
4. **Participation consequence** — what a contribution changed in a shared
   Place, route, Plan, Occasion, or later Outcome.

### Social admission tests

Social material renders only when:

- may-use permits this purpose;
- may-name permits the displayed attribution;
- the trace is relevant to the current Place or path;
- it adds information or possibility rather than social decoration;
- nonresponse creates no debt;
- live location is not inferred from stale travel history; and
- revocation or correction can recompile the projection.

### Rejected patterns

- friends-nearby surveillance;
- global friend activity feed;
- popularity counts as authority;
- `Mara saved this` without why that matters;
- synthetic claims about what a friend would like;
- social proof that pressures a decision; and
- private contribution silently converted into public expertise.

## 9. Admission and hierarchy compiler

Every candidate composition should be evaluated before a renderer is chosen.

### 9.1 Required brief

```text
focal Place or scope
user job
new value beyond known input
current consequence
world / affordance / relationship / human-horizon roles needed
Claims and Sources
freshness and uncertainty
known-to-person posture
audience and use authority
lead medium
action burden and authority
expiry or monitoring condition
return destination
```

### 9.2 Hard gates

Reject or degrade when:

- the focal spatial relationship is missing;
- the content merely repeats the person's contribution;
- an infrastructure app already provides the whole value more directly;
- a current fact lacks adequate freshness;
- a social trace lacks purpose or audience authority;
- a claim would require unsupported certainty;
- the unit asks the person to perform Vesper's synthesis;
- the next action is more burdensome than the likely value;
- the same object is already foregrounded more usefully in Home; or
- silence is better.

### 9.3 Ranking

Rank by:

1. current consequence or feasibility;
2. substantive novelty to this person;
3. spatial explanatory power;
4. relationship continuity;
5. credible human or plural value;
6. horizon quality;
7. evidence and freshness;
8. receptivity and burden; and
9. fit with the current state and scope.

Do not rank by predicted engagement, inventory volume, provider margin,
social popularity, or renderer availability.

### 9.4 Density

- one lead composition at most;
- two to four standard branches at most;
- compact doors only after the standard branches;
- one Place may be deep; many Places must be comparatively light;
- every deeper branch displaces something else; and
- the page ends when the next unit does not beat silence.

## 10. Degradation rules

| Missing or weak input | Correct degradation |
| --- | --- |
| No personal history | World and current affordance remain; relationship disappears without a cold-start lecture |
| No current location | Use explicit searched, planned, saved, or Home-provided scope; do not infer proximity |
| Stale hours or conditions | Label age, remove action claim, retain stable identity and interpretation |
| No attributable sources | Omit apparatus and soften or remove the claim |
| Human use allowed but naming denied | Use only if an honest anonymous form remains materially useful; otherwise omit |
| No meaningful horizon | End at Place Focus; never fill with generic similarity |
| No strong lead | Show a balanced finite field or one orientation state, not an invented recommendation |
| Offline with cache | Preserve last-known field and relationship; mark stale current facts and disable unsupported operations |
| Offline without cache | Offer stable saved or previously opened Places only if locally present; otherwise show a small honest unavailability state |
| Excessive live burden | Reduce to recovery, fallback, monitoring, or silence |

## 11. Four complete situation tests

### 11.1 Ordinary local browse, no selected Place

**World Field** opens on an explicit New York scope. It leads with one complete
weekend proposition or spatial pattern grounded in current conditions and the
person's existing evidence. A compact map explains the geometry. Two or three
branches state their real differences. A saved-world door and one relevant
human trace may follow.

It does not open with eight categories, ask `What are you in the mood for?`,
or lead with a recap of the recent Europe trip.

### 11.2 One selected Place after a prior observation

The person opens Sorrento after having noticed its cliffs. **Place Focus** does
not repeat `Sorrento has cliffs`. It leads with a supported mechanism,
consequence, or practical distinction the person did not already supply. A
relationship trace shows the originating observation without interpreting it
as personality. Horizon doors may connect to another coast, geology, movement
pattern, or New York waterfront only when the relation and important
difference can be stated.

### 11.3 Rome through a friend's Paris trace

Home previews the timely juxtaposition. Places opens a **Place Path** anchored
in Rome, identifies the authorized Paris contribution and author, explains
the shared structure and meaningful divergence, and exposes sources or
uncertainty. It may return to Rome Place Focus or follow Paris as a new focal
Place.

The friend is a source in a bounded path, not a unit in an activity feed.

### 11.4 Four live hours in Lisbon before dinner

**Live Reduction** leads with a feasible arc that ends near the existing
commitment. Map and sequence are transformations of the same path. Walking,
grade, weather, hours, reservation status, and freshness are visible. One
meaningful alternative handles the dominant failure mode. Deeper editorial
material recedes but remains reachable from Place Focus.

Accepting the path may create or modify a Plan through the owning capability.
Ignoring it creates no durable task.

## 12. Migration from current implementation

### 12.1 Preserve

- backend-produced grounded section data;
- current context-handle mechanism;
- search and offline state handling;
- map canvas, pin peek, and reachability work;
- city, neighbourhood, venue, dossier, saved, memory, and experience data;
- existing renderers for candidate rows, editorial material, experiences,
  notices, memories, and friend traces;
- server/client render-plan separation; and
- telemetry and exposure accounting.

### 12.2 Recompose before adding more renderers

1. Define a typed navigation envelope shared by root, map, Place detail,
   horizon path, Home, and Chat.
2. Introduce explicit `world`, `place`, and `path` semantic states above the
   current routes.
3. Add a composition resolver that chooses lead, branches, continuity doors,
   and density from grounded candidates.
4. Project the existing section feed into World Field rather than deleting it.
5. Rebase city, neighbourhood, and venue views onto one Place Focus contract.
6. Treat map as a rendering of a field or path with state preservation.
7. Add the typed Place Horizon read projection and fixture it before a graph
   UI or durable graph writer.
8. Expand human-trace eligibility beyond trip scope only after audience and
   purpose tests are enforced.

### 12.3 Do not start with

- a visual rewrite of all Places screens;
- a new universal `PlacePath` database table;
- one permanent module for each of the four Place faces;
- a generic personalized recommendation ranker;
- a public social layer;
- a fixed six-lens navigation system;
- a map-first redesign; or
- building every composition in the canvas inventory.

## 13. Evaluation

### Root clarity

- Can a new person say that Places helps them understand and use the world
  around a Place, rather than merely find venues?
- Does the same source feel timely and selective in Home but spatial and deep
  in Places?

### Returned value

- Does the first screenful provide substance without asking for input?
- Does it add a mechanism, distinction, option, human perspective, or
  consequence the person did not already provide?

### Navigation coherence

- Do row, pin, search result, social trace, and Home opening converge on the
  same Place Focus?
- Can the person follow a path and return without losing scope or position?
- Do map and composition views preserve the same selection and question?

### Evidence and trust

- Are world facts, personal evidence, Vesper synthesis, and human
  contributions distinguishable?
- Are freshness, uncertainty, disagreement, audience, and correction
  inspectable at the grain the claim requires?

### Real-world usefulness

- Under live conditions, can the person reach a stable next step with less
  assembly work?
- Does the product show burden, fallback, and monitoring rather than merely
  increasing option count?

### Attention

- Does the surface stop when value runs out?
- Does a Place remain deep without the root becoming an infinite feed?
- Are prompts, progress mechanics, and social pressure absent?

## 14. Recommended next artifact

Create one semantic Places fixture board in the dedicated design environment,
using the same evidence world in four frames:

1. World Field in ordinary New York browse;
2. Place Focus on one selected Place;
3. Place Path following one hidden-system or human connection; and
4. the same scope under Live Reduction.

The board should reuse the corrected canvas's real composition vocabulary but
must not reproduce its ranked posture pages. Its purpose is to test:

- whether the three states feel like one product;
- whether map and non-map media preserve identity;
- whether one Place can be deep without becoming an encyclopedia;
- whether social material reads as evidence rather than feed activity;
- whether Home entry preserves the proposition; and
- whether the density taper returns substantial value without overload.

## 15. Provenance and authority

This pass used the exact corrected design bundle:

- `/Users/feihuyan/Downloads/vesper-home-surfaces 2/README.md`;
- `/Users/feihuyan/Downloads/vesper-home-surfaces 2/project/Places - Whole Pages.dc.html`;
- its imported `/Users/feihuyan/Downloads/vesper-home-surfaces 2/project/support.js`;
- `Places - The Page.dc.html`;
- `Places - As Built.dc.html`;
- `Places - Proposed.dc.html`;
- `Canon - Home Surfaces.dc.html`;
- `Build Manifest - Both Surfaces.dc.html`; and
- the cross-surface whole-page and receipt-gap canvases where they clarified
  ownership or evidence.

The bundle is authoritative evidence for the Home-surface design exploration
and the implementation state it audited. Its own currency labels say that the
shared model remains canonical for vocabulary but not current state, while the
manifest wins on the implementation state it re-verified. The August 28–29
four-root, HCI, contribution, and five-world documents are newer product
doctrine. This anatomy therefore reconciles the bundle's concrete composition
work with the newer Places posture; it does not treat every canvas proposal as
adopted product canon.

No screenshot from the older repository design-reference folders was used as
an authority for this decision.

## Compact standard

> **Places is one navigable encounter with the world: orient among a finite
> field, focus one Place, follow a meaningful path, and reduce toward reality
> when the moment becomes live.**
