---
doc_type: working
status: active
owner: founder / product / design
created: 2026-08-27
last_verified: 2026-08-27
expires: 2026-09-26
why_new: Recovers the strongest pre-pivot Home and Places surface thinking, distinguishes compositional richness from feed density, and translates it into a fuller four-root direction where active Occasions remain visible in Home and Life.
source_of_truth_for:
  - home-surfaces-pre-pivot-recovery-2026-08-27
  - fuller-home-places-life-composition-direction-2026-08-27
---

# Fuller Home Surfaces — Pre-Pivot Recovery and Post-Pivot Direction

## Executive conclusion

The product should not interpret **calm** as **absence**.

The pre-pivot redesign contains a better starting point than a sparse,
single-instrument Home. Its best work made the product feel full by composing
several different registers—act, understand, imagine, relate, and return—under
one clear attention order. Its weakest work made the product feel like a feed
by repeating the same candidate/card grammar down the page.

The governing distinction should be:

> **One dominant thing does not mean one visible thing. Quiet does not mean
> empty. Adaptive emphasis does not require an adaptive page skeleton.**

The current four-root constitution already permits this. It says rich roots
may compose several jobs while establishing a clear attention order. The
surface redesign should therefore preserve a stable, fuller anatomy and adapt
which part is dominant—not continually collapse the entire page to one cue.

The immediate product implication is also clear: an active Occasion must remain
visible in Life. “Do not ask for reflection while it is happening” is a sound
rule; “Life stays quiet while it is happening” is not. A live Occasion is
already accumulating shared state, participation, decisions, contributions,
and boundaries. Life should show that relational field without fabricating a
recap or inferred outcome.

## What was investigated

This recovery used four layers of local evidence:

1. the July Trips Stack Model and Vesper Workbench proposals;
2. the Vesper 405 Places workspace and card-family studies;
3. the August `vesper-home-surfaces` Page boards, Whole Page studies, handoff,
   and post-pivot implementation audit;
4. the current React Native root navigation and composition code.

Primary sources:

- `docs/working/trips-home-promotion-model-2026-07-27.md`
- `docs/working/vesper-home-workbench-2026-07-28.md`
- `docs/working/places-build-plan-2026-07-28.md`
- `docs/home-surfaces-audit-2026-08-09.md`
- `docs/working/vesper-experience-constitution-and-interaction-grammar-2026-08-22.md`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/HANDOFF.md`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Trips - The Page.dc.html`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Places - The Page.dc.html`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Trips - Whole Pages.dc.html`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Places - Whole Pages.dc.html`
- `travel-app/components/trips/TripsHomeBody.tsx`
- `travel-app/components/places/PlacesWorkspace.tsx`
- `travel-app/components/places/PlacesSectionFeed.tsx`
- `travel-app/app/(tabs)/concierge/index.tsx`

The checked-in screenshots were treated as historical design evidence rather
than current implementation authority.

## 1. The strongest pre-pivot idea: a full page with a temporal argument

The July Trips Stack Model was not merely a stack of cards. It had a fixed
six-part grammar:

1. **The Stack** — what needs attention now;
2. **Companion** — a situated editorial reading;
3. **The Table** — grounded future possibility;
4. **Your People** — social presence and openings;
5. **Connect** — a standing invitation door;
6. **Trail / Bridge** — return and memory.

Its page-level argument moved from present to future to past. The top item
bloomed into a voiced crown, compact rows handled administration, and lower
sections changed register rather than repeating more priority cards.

Three parts remain particularly valuable:

- **Stable anatomy, variable existence.** Sections held their conceptual order
  but disappeared without chrome when they had nothing true to say.
- **Cards for seduction, rows for administration.** Containment expressed the
  kind of attention or action being requested rather than visual variety.
- **A temporal field wider than the current task.** The screen could say what
  matters now while still revealing future possibility, people, and continuity.

This is why the quiet Trips composition did not feel empty. “Nothing needs
you” remained the dominant read, but a Companion and a grounded future sketch
made the product's continuing intelligence visible.

### What not to recover from it

- A trip-centric ranked queue should not become the universal Home model.
- The six old sections should not be copied literally into a new root.
- The hero should not promote whichever generic feed item won a global ranker.
- Every capability should not be forced into a card or a trip.
- Future ideas should not become engagement bait or unsupported inspiration.

The transferable asset is the **compositional grammar**, not the old domain
ownership.

## 2. Vesper Workbench: actuality plus visible potential

The Vesper Workbench correctly established a sharp ownership line:

> Trips owns objects; Vesper owns sessions.

Its page showed a situated read, a sunken band of grounded facts and open work,
ghost prompts, and a universal composer. That made Vesper's range visible even
before a person knew what to ask.

The good principle is that a root can expose **potential** without turning
potential into buttons, recommendations, or fake unfinished tasks. The ghost
prompts demonstrated modalities and jobs while the workbench preserved one
main interaction.

The weak edge is its quiet state. One sentence, five faded prompts, and a
composer can read as confident only if the rest of the product already feels
inhabited. As a primary proof of product power, it risks looking unfinished.
The original workbench document named this risk explicitly.

Vesper should remain open and capable, but it should not bear the entire burden
of showing what the product is. Home, Places, and Life need their own visible
depth.

## 3. Places: rich domain inventory, weak page cadence

The pre-pivot Places work recognized that Place understanding has many valid
registers:

- one Place in depth: recommendation, verdict, apparatus, change, caveat, log;
- several Places: candidates, pairs, sets, rails, doors;
- composed experience: map fragment, walk, stretch, sequence;
- reading: covers, angles, lenses, extracts;
- memory and return;
- people and co-signs;
- personal record and familiarity.

This is a strong product claim. Places should make the physical world
spatially, practically, culturally, socially, and personally legible. It
should not be reduced to a route card, a search result list, or a generic map.

The current/root-feed direction narrowed that potential into a server-produced
sequence of four to eight sections. The canonical Whole Page study described
the resulting cadence accurately: past roughly five sections, the repeated
marker-rule-content rhythm reads as a list. The current implementation also
places Search, Saved, and Map inside a search door rather than allowing the root
to feel natively spatial.

The lesson is not “show fewer Places sections.” It is:

> Several Places jobs need to coexist, but they cannot all arrive as equal
> sections in one vertical feed.

The Page boards also surfaced a particularly important contradiction: Places
was the only mapless home surface even though it is the root whose human
question is spatial. A map or spatial field should not be ornamental, but
spatial reasoning must be visible on the root.

## 4. The August redesign had much more product range than the shipping roots

The August audit counted 56 Trips frames across 11 groups and 42 Places frames
across 7 groups. Frame counts are not a roadmap, but the inventory reveals the
range the redesign was trying to express.

Especially relevant pre-pivot surfaces included:

- local Plans and individual local occasions;
- Occasions without Plans;
- hosting;
- This Week and This Weekend;
- saved but unplaced material;
- people, empty seats, and group state;
- open loops and comparisons;
- a reading Companion;
- Today, mapped and other spatial compositions;
- returns and “since you last looked”;
- Place memory, people, and familiarity.

The pivot should not erase this breadth. It should redistribute it under
clearer root questions and canonical objects.

## 5. Current product state and why it can feel empty

The visible app still has three roots:

- **Plans** (`/trips`), an authored page dominated by a ranked crown and typed
  modules;
- **Vesper** (`/concierge`), a session workbench and universal composer;
- **Places**, a produced section feed.

Life is not yet a visible root, and Home is still effectively Plans. Current
Trips code can render a mast, Now band, crown, open loops, countdown,
conditions, group, queue, local plans, map, Companion, dreams, Trip Feel,
trail, and footer. That sounds full, but many of those modules are gated,
trip-shaped, dark, or reached through truncated projections. The actual page
often communicates a narrower product than the code inventory suggests.

Places can render a broad set of produced card families, but its root remains
a mast followed by a uniform server-ordered feed. Its spatial canvas and
personal collections are secondary doors. It communicates breadth through
quantity rather than through a clearly legible workspace.

This creates two different kinds of emptiness:

1. **literal sparsity** — a quiet state has very little visible material;
2. **capability opacity** — the app may be powerful, but the root gives no
   stable indication that those capabilities exist.

The redesign must solve both.

## 6. Product laws for fuller surfaces

### 6.1 Dominant is not solitary

Each state should have one unmistakable answer to “what matters now?” The rest
of the surface can still show the person's current world in quieter registers.

### 6.2 Quiet is a posture, not a content count

Quiet means no claim deserves interruption or urgent action. It does not mean
there are no ongoing occasions, people, places, horizons, or continuity.

### 6.3 Keep the page skeleton stable; adapt emphasis inside it

The roots should not shapeshift into unrelated layouts every time the resolver
changes its mind. Stable regions help the person learn where things live. The
system may change dominance, treatment, density, or instrumentation within
those regions.

### 6.4 Fullness comes from different registers, not more examples

Three cards that all recommend a place are repetition. One spatial field, one
grounded perspective, and one personal relationship to that Place demonstrate
three different powers.

### 6.5 Existence-gate evidence, not capability

Do not fabricate content to fill a slot. But an empty evidence region can still
make a capability legible through a truthful door, field, or invitation. A
Map, “All plans and occasions,” Mine/Together scope, or Vesper composer can be
stable furniture without claiming that a new event exists.

### 6.6 Durable objects may project across roots

The same Occasion may appear on Home as current attention, in Places as spatial
context, in Vesper as open work, and in Life as a shared relational field. The
projection changes; the object and authority do not.

## 7. Proposed fuller Home anatomy

Home should become an editorial field with five stable regions. Not every
region must contain a large card, but the order should remain learnable.

### 1. Now — the dominant opening

One current opening, active Occasion, invitation, material change, or truthful
quiet read. This is the only region allowed to dominate the screen.

It may use a live instrument, a voiced crown, a bounded invitation, or a calm
statement that nothing needs action.

### 2. In motion — durable things already underway

A compact view of active and upcoming Occasions, Plans, open shared decisions,
and consequential work. This is not a generic queue: it is a bounded set of
owned objects with an obvious **All plans and occasions** door.

### 3. Horizons — the nearby and the becoming

Grounded local possibility, an upcoming time window, a Place horizon, or a
saved cluster that could become an Occasion. This recovers the best function
of The Table and This Weekend without manufacturing recommendations.

### 4. With people — participation and openings

Invitations, an empty seat with real authority, something waiting for the
person's contribution, or one relationship opening. This should express the
social field without becoming an activity feed.

### 5. Continuity — return and what changed

A return, a second-occasion continuation, “since you last looked,” or one
relevant artifact. This is not a memory carousel; it closes the temporal arc
and proves that the product compounds.

### Home posture behavior

| Posture | Dominant region | Supporting field |
|---|---|---|
| Available | Now | In motion + With people |
| Planning | In motion | Horizons + With people |
| Live | Now | compact In motion + spatial door + participants |
| Returned | Continuity | people + relevant Place return |
| Quiet | truthful Now read | Horizons + Continuity + stable doors |
| Cold | invitation/potential | Places horizon + Vesper input + obvious object doors |

Urgent is the only posture allowed to suppress most of the supporting field.
That matches the pre-pivot insight that withholding the rest can itself be the
right composition when a material consequence is lapsing.

## 8. Proposed fuller Places anatomy

Places should be a spatial workspace with a stable canvas and several lenses,
not a page made solely of feed sections.

### 1. Spatial field

A map, route field, or place-area composition occupies a persistent part of
the root whenever honest spatial anchors exist. It shows relations—near/far,
clusters, crossings, gaps, and reachable areas—not decorative pins.

### 2. Context and scope

The current Place, city, Occasion, or “around me” scope remains visible and
changeable without opening a generic search mode first. Search is still a
door, but Map and Saved should not be conceptually buried behind Search.

### 3. Focused Place depth

The selected Place can be read through the one grounded register the evidence
supports: practical recommendation, caveat, change, source apparatus, log, or
personal relationship. Do not compress all registers into a free-text reason.

### 4. Ways through the world

Walks, stretches, sequences, experiences, and readings provide composed ways
to experience a scope. This is where a live Occasion route belongs as one
spatial projection, not as the entire Places root.

### 5. Personal and plural relationship

Saved, familiar, returned-to, shared by someone, connected to an Occasion, or
part of a personal Place history. These are relationship layers, not generic
ranking signals.

The design should use a spatial canvas plus one dominant lower register, with
the remaining lenses available as quiet shelves, overlays, or scope changes.
This avoids both an empty one-card Places root and an eight-section metronome.

## 9. Proposed fuller Life anatomy

Life should be longitudinal and relational, but it must also represent the
present. “Accumulating” begins before an Occasion ends.

### Mine

- current personal Encounters and artifacts;
- private contributions or notes attached to an active Occasion;
- emerging but revisable patterns;
- correction, forgetting, and privacy controls;
- returns and second-occasion continuity.

### Together

- active and upcoming shared Occasions;
- people and circles relevant now;
- participation state and who is expected/present;
- shared decisions and contributions the viewer may see;
- addressed handoffs and plural outcomes;
- remembered continuity after the Occasion.

### Live Occasion rule

During a live Occasion, Life should show a compact relational field:

- Occasion identity and phase;
- authorized roster and participation state;
- settled shared commitments and still-open decisions;
- contributions or handoffs that exist now;
- privacy and leaving/authority boundaries where relevant.

It should **not**:

- prompt for a recap while people are still living it;
- infer attendance, enjoyment, or outcomes;
- manufacture a shared story;
- ask the user to perform the moment for the product.

The correct live message is therefore not “Life stays quiet.” It is closer to:

> **This Occasion is alive here. Nothing needs to be turned into a memory yet.**

## 10. Implications for adaptive experience composition

Adaptive composition should operate at three levels:

1. **Select dominance** — which current object or opening leads;
2. **select an instrument** — what treatment best serves the current job;
3. **tune supporting density** — which grounded secondary registers remain
   visible and how quiet they become.

It should not ordinarily select an entirely different root skeleton. That
would make intelligence legible only as UI instability.

A good formal rule is:

```text
stable root anatomy
  + grounded existence gates
  + one adaptive dominant region
  + bounded supporting registers
  = full but composed
```

This also changes how the existing resolver work should be judged. A resolver
that successfully chooses one treatment can still produce an impoverished
product if the surface discards the rest of the person's world.

## 11. What should be recovered, revised, and retired

### Recover

- the present → future → past temporal arc;
- stable page anatomy with existence-gated content;
- one crown/anchor with quieter supporting registers;
- cards for consequential or seductive objects, rows/fields for navigation;
- grounded future possibility;
- visible people and social openings;
- map and spatial reasoning as a first-class surface capability;
- return and second-occasion continuity;
- potential made legible without fake tasks.

### Revise

- replace trip ownership with canonical Occasion, Place, relationship, and
  artifact projections;
- move active shared continuity into Life, including during the Occasion;
- make Home a world-level editorial field rather than Plans with broader copy;
- replace Places' repeated section cadence with canvas + focus + lenses;
- let adaptive composition tune hierarchy within stable roots.

### Retire

- a universal ranked card queue;
- trip-only definitions of Home fullness;
- quiet states that are visually indistinguishable from unfinished product;
- equal-weight vertical section feeds;
- hidden spatial capability on Places;
- the assumption that Life begins only after an Occasion ends;
- recap prompts and inferred outcomes during live participation.

## 12. Recommended next design step

Do not patch only the current Rome Life screen. Redesign the Rome lifecycle as
a **full-surface composition study** across Home, Places, and Life while keeping
Vesper as the workbench.

For each lifecycle phase—opening, shaping, committed, live, returned, and
second occasion—draw:

1. the dominant region;
2. the supporting regions that remain visible;
3. the canonical object projected into each root;
4. what disappears because it is ungrounded;
5. what remains as stable capability furniture;
6. the cross-root transition doors.

The first revised frame should be **live Rome**, because it forces the three
hardest corrections at once:

- Home must be focused without becoming empty;
- Places must remain a real spatial workspace, not only a route card;
- Life must show the active Occasion without demanding reflection.

Once that frame works, derive quiet and cold states from the same stable
anatomy. That is a stronger test than starting from emptiness.
