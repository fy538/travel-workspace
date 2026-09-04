---
doc_type: working
status: active
owner: founder / product / design / architecture
created: 2026-09-02
last_verified: 2026-09-02
expires: 2026-10-02
why_new: Tests whether Vesper needs an intentional present-tense social-world aperture in addition to object-native multiplayer projection and Life's durable People record, without presupposing a fifth root, friend feed, or live-location map.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - ../../travel-agent/docs/product/Multiplayer Product Strategy.md
  - ../../travel-agent/docs/product/MVP Social Loop.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-08-30-adopt-life-consumer-anatomy.md
  - ../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md
  - claude-design-multiplayer-prominence-exploration-brief-2026-09-01.md
  - life-next-behavior-prototype-handoff-2026-08-31.md
  - plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md
  - source-claim-scoped-learning-and-multiplayer-purpose-research-2026-08-29.md
---

# Claude Design / Claude Code Handoff — Social Aperture and Shared World

**Date:** September 2, 2026

**Audience:** Claude Design and Claude Code

**Workspace:** `/Users/feihuyan/travel-workspace`

**Reference design projects:**

- `/Users/feihuyan/Downloads/vesper-home-places 2`
- `/Users/feihuyan/Downloads/vesper-life-anchors 2`

**Suggested new Claude Design project:**

```text
/Users/feihuyan/Downloads/vesper-social-aperture
```

The project name is intentionally provisional. Do not encode `Together` as a
new root or `People` as a generic social graph before the information
architecture has earned either conclusion.

## 0. Assignment

Create a fresh, comparative product-design investigation that answers:

> **Does Vesper need an intentional present-tense way to enter, understand,
> and browse the user's permissioned social world in addition to distributed
> multiplayer value in Home and Places and durable shared continuity in Life?**

Do not begin by designing a social feed or assuming the answer is a new page.
The assignment is to compare complete experiences under the same fixture world
and decide which architecture makes multiplayer legible, useful, and
distinctive without duplicating Life, fragmenting the four-root model, or
turning ordinary relationships into content production.

The investigation must preserve three bodies of already-valuable work:

1. **Home and Places multiplayer projection** — how another person causally
   changes understanding, possibility, action, or spatial judgment;
2. **Life People and Together continuity** — how shared records, attributed
   contributions, plural episodes, withdrawal, and relationship history are
   held over time; and
3. **Occasion multiplayer** — how a bounded group forms, coordinates, adapts,
   contributes, ends, and possibly recurs.

The missing question is not whether Vesper has multiplayer mechanics. It is
whether a person can intentionally orient to multiplayer as a lived part of
the product rather than waiting for Home's compiler to select one social
opening or remembering which Place, person, or Occasion to open.

This is a design and architecture investigation. It does **not** authorize:

- production implementation;
- a fifth root;
- a public follower graph;
- a generic friend-activity endpoint as the new product contract;
- ambient location collection or live-location sharing;
- engagement ranking, streaks, badges, or reciprocity pressure;
- a redesign of accepted Home, Places, Chat, or Life programs; or
- schema promotion before fixture comparison and founder review.

## 1. Executive diagnosis

### 1.1 What has already been designed

Vesper has not actually forgotten the multiplayer page. It has designed one
important half of it inside **Life → People**.

The current Life project contains:

- `03E8 Life Page - People.dc.html` — an at-rest People lens organized around
  `Shared with Maya`, `Shared with Alex`, and people encountered;
- `06D Person - Maya.dc.html` — a complete shared-record dossier with episodes,
  kept artifacts, photographs, conversations, Places, and what is held in
  common;
- `17A People Root At Rest.dc.html` — a substantial ordinary Monday with no
  event pending and no intimacy ranking;
- `17B Shared With Maya.dc.html` — attributed shared episodes, Maya's granted
  contributions, the viewer's private account, and an earned relational Return;
- `17C Addressed Arrival.dc.html` — a quiet contribution arrival through a
  person row rather than a notification or inbox;
- `17D Dinner Shared Episode.dc.html` — one governed shared occurrence with
  plural private accounts;
- `17E–17G` — optional reply, withdrawal, departure, block, unblock, and
  reconciliation; and
- `21 Together 1to1 Sequence.dc.html` — the whole six-state consumer sequence
  across the same owning surfaces.

This program answers:

> **Who has been part of my life, what have we shared, what remains held
> between us, and how can it be retrieved or repaired?**

That is already a dedicated multiplayer **continuity** experience. It must not
be replaced by a conventional friend profile, activity history, or relationship
score.

The Home and Places multiplayer project separately contains:

- MP1 — a person-to-person Place handoff;
- MP2 — a relational opening changing Home prominence;
- MP3 — `for me`, `with Maya`, and `for Friday dinner` Places scopes;
- MP4 — an Occasion expressed through Places;
- MP5 — withdrawal, narrowing, and block propagation; and
- MP6 — component and composition dispositions.

This program answers:

> **How does another person change the value Vesper returns in the object and
> root where that value matters?**

It is strong projection work. It does not test whether the user needs an
intentional cross-person orientation.

### 1.2 What remains unresolved

No accepted experience clearly answers:

> **What is currently available through my people, what do we have in motion,
> and what could their deliberately shared lives open for me now?**

Examples of currently unowned or weakly owned intentions:

- “What have people I care about deliberately made available to me lately?”
- “What are my friends noticing in Paris, Brooklyn, Shanghai, and Rome?”
- “Show me the Places that currently matter through them.”
- “What do Maya, Alex, and I have in motion across unrelated Occasions?”
- “What have I made visible, to whom, and for how long?”
- “Where are my friends, at the precision they deliberately chose to share?”
- “I have no task. Let me browse my social world and find one real opening.”

Scattering every social cause into Home, Places, Life, Chat, and Occasion is
semantically clean but can create three product risks:

1. **Multiplayer invisibility.** The system is structurally multiplayer but is
   perceived as personal AI with occasional collaboration.
2. **Compiler dependence.** The user can only see social value when Home's
   ranking chooses it; there is no pull-based alternative.
3. **No social mental model.** The user cannot explain who is present in
   Vesper, what is shared, what is active, or how their relationship-place
   world accumulates.

### 1.3 The precise product hypothesis

The working hypothesis is **not** “Vesper needs a social tab.” It is:

> **Object-native circulation may need a bounded, user-invoked social aperture
> that makes the currently permissioned social world inspectable without
> becoming its own engagement economy.**

The opposite hypothesis remains credible:

> **Life People, person-specific shared records, Occasion owners, and stronger
> cross-root entry points may already be sufficient; a cross-person aperture
> may only duplicate information and blur the product.**

The new project exists to decide between these hypotheses through complete
compositions—not rhetoric.

## 2. Canonical product laws

Treat these as fixed inputs unless the project produces concrete evidence that
requires a founder ruling.

### 2.1 Four roots remain the control

```text
Home    What matters now?
Chat    What do I want to give, ask, shape, or do?
Places  What does the world afford here or next—and why?
Life    What exists across my life, and what remains true and usable?
```

People, relationships, Status, handoffs, Plans, Occasions, generated media,
and monitors are objects, capabilities, or focused owner views until they prove
a fifth durable human orientation.

### 2.2 Multiplayer spans the four product moves

```text
Make sense       plural but authorized understanding
Open possibility human perspectives and invitations without response debt
Help it work     governed coordination, commitment, repair, and action
Carry forward    shared occurrence, plural outcomes, and relationship continuity
```

Do not reduce multiplayer to either social discovery or group planning.

### 2.3 The compounding unit

```text
person × relationship × Place × situation × Outcome
```

The person is valuable because of a situated contribution, shared history,
current participation, or deliberate availability—not because an avatar makes
a card feel social.

### 2.4 Social material remains object-native

```text
timely consequence       → Home
spatial perspective      → Places
negotiation or response  → Chat
bounded shared action    → Occasion / Plan
durable shared record    → Life / People
```

Any social aperture is an **index, lens, or composition over these owners**.
It must not become a second owner of the same Place, Occasion, contribution,
message, or relationship record.

### 2.5 Social value precedes social labor

Opening the surface must not immediately ask the user to:

- post;
- reply;
- complete a profile;
- invite contacts;
- classify relationships;
- rank friends;
- approve a list of memories;
- clear an inbox; or
- maintain a streak.

It should first return something worth seeing: a human perspective, a new
connection, a spatial opening, a useful shared state, a vivid shared record, or
a currently possible experience.

### 2.6 AI mediates relevance, not intimacy

Vesper may:

- connect separately authored traces on a bounded axis;
- adapt an authorized handoff to the viewer's situation;
- explain why a Place, person, or Occasion is relevant now;
- prepare a route, comparison, or optional starting point; and
- preserve attribution and limits.

Vesper must not:

- claim people are close, compatible, drifting apart, or “meant” to connect;
- infer availability from location, silence, calendar gaps, or app behavior;
- speak in a friend's voice;
- send an intimate message autonomously;
- convert co-presence into friendship; or
- merge several people's experiences into one group personality.

### 2.7 Sharing has independent axes

For every visible social unit, preserve at least:

- author;
- subject;
- custodian;
- audience;
- purpose;
- precision;
- expiry;
- permitted use;
- inference boundary;
- action authority; and
- withdrawal or correction behavior.

Do not expose these as a settings worksheet on every card. The consumer
surface should express the important boundary in human language while the
fixture and architecture retain the complete envelope.

## 3. Research synthesis

This section summarizes relevant product and HCI precedents. These are
mechanisms to learn from, not products to imitate wholesale.

### 3.1 Apple Shared with You: distributed value plus source-specific recovery

Apple routes content received in Messages into the app that can use it: links
into Safari, music into Music, photos into Photos, and so on. It keeps the
sender attribution near the content, lets the recipient continue the
conversation, allows pinning, and lets a person disable Shared with You for a
specific conversation or app. The conversation detail also provides a
person-specific index across photos, links, documents, locations, and other
media.

Sources:

- [Use Shared with You on iPhone and iPad](https://support.apple.com/en-au/102197)
- [Share content in Messages on iPhone](https://support.apple.com/en-il/guide/iphone/iphb66cfeaad/ios)

**Lesson for Vesper:** object-native delivery and a relationship-specific
index are complementary. A centralized engagement feed is not required.
Vesper already approximates the relationship-specific half through `Shared
with Maya`; the open question is whether a finite cross-person aperture adds
enough value beyond stronger source labels and person doors.

**Do not borrow:** automatic projection merely because a sender is a contact.
Vesper's material may be more sensitive and more inferential than a link.
Audience alone does not grant model use, inference, retention, or action.

### 3.2 Beli and Google Maps lists: social value anchored to a domain object

Beli's public promise combines restaurant tracking, sharing, and a restaurant
map rather than presenting friendship as a separate content category. Google
Maps lets people create and follow lists whose Places appear on the map, and
supports collaborative shortlists tied to the group decision at hand.

Sources:

- [Beli product site](https://beliapp.com/beli-home)
- [Google Maps shared lists](https://blog.google/products-and-platforms/products/maps/keep-track-your-favorite-places-and-share-them-friends/)
- [Google Maps collaborative group planning](https://blog.google/products-and-platforms/products/maps/all-together-now-group-planning-google-maps/)

**Lesson for Vesper:** a social map is most coherent when pins represent a
clear semantic act—shared list, handoff, active plan, or authored Status—not
generic “friend activity.” The Place remains the object; the person provides
provenance, perspective, or temporary relevance.

**Do not borrow:** broad voting as the default resolution method. Vesper's
multiplayer doctrine is to resolve rather than poll after it has gathered
private constraints and narrowed the choice.

### 3.3 Locket and Airbuds: ambient awareness works when the signal is narrow

Locket constrains the product to a small existing-friend audience and one
concrete medium: direct photographs. Airbuds turns one behavior—listening—into
an ambient friend signal and lets people choose which friends appear in a
widget. Both reduce the ambiguity of “what belongs here” by narrowing the
content type and social scope.

Sources:

- [Locket product explanation](https://help.locket.com/en/articles/14225418-my-teen-asked-me-to-get-locket-what-is-it)
- [Airbuds custom friend widgets](https://help.airbuds.fm/en/articles/10-how-to-install-a-widget-for-one-friend-or-more)

**Lesson for Vesper:** an ambient surface needs a legible signal contract.
Vesper cannot pour photographs, tickets, listening, bookings, saves, Places,
generated essays, plans, messages, and location traces into one stream and
expect coherence. Admission must be based on a small number of human meanings,
not media types or event volume.

Candidate meanings are:

- someone deliberately addressed something to me;
- someone deliberately featured something for this audience;
- we share an active bounded consequence;
- a Place or Occasion we share materially changed; or
- a relationship-place continuity has become newly useful.

**Do not borrow:** automatic behavior as automatic expression. Background
listening, passive location, saves, dwell, and inferred interest are not
self-authored Status.

### 3.4 Spotify Jam and Partiful: multiplayer attaches to a shared object

Spotify Jam makes a live listening queue the common object. People can join,
add songs, see authorship, receive recommendations, and leave; the host retains
bounded control. Partiful makes the Occasion the social container: guest list,
updates, comments, practical questions, payments, and shared photographs all
derive their meaning from one event.

Sources:

- [Spotify Jam](https://newsroom.spotify.com/2023-09-26/spotify-jam-personalized-collaborative-listening-session-free-premium-users/)
- [Partiful product](https://partiful.com/)

**Lesson for Vesper:** most shared agency should stay inside an Occasion, Plan,
or other common object. A social aperture should summarize or route to active
shared objects; it should not reproduce their complete controls.

**Do not borrow:** guest-list spectacle, public comment pressure, or broad
preference questionnaires. Vesper must preserve private caucus, flexible
participation, and low-response-pressure exits.

### 3.5 Snap Map and location-sharing products: useful visibility can become surveillance

Snap Map keeps location sharing off by default, offers selected audiences and
Ghost Mode, and distinguishes while-using from background updates. Google Maps
similarly exposes who can see real-time location, allows hiding another
person, and lets the sharer stop access. These controls demonstrate the level
of explicitness necessary when the product claims to show where a person is.

Sources:

- [Snap Map location sharing](https://help.snapchat.com/hc/en-us/articles/7012309470740-How-do-I-share-my-location-on-Snap-Map)
- [Snap Map privacy and safety](https://help.snapchat.com/hc/en-gb/articles/24547077410580-Snap-Map-Privacy-Safety-Reminder)
- [Google Maps real-time location sharing](https://support.google.com/maps/answer/15437054?hl=en-uk)

**Lesson for Vesper:** “friend map” is dangerously underspecified. The design
must distinguish at least:

1. live device location;
2. authored present Status at a chosen precision;
3. a recently shared Place or handoff;
4. a Place in an active shared Occasion;
5. historical shared Place continuity; and
6. a Vesper-generated possibility involving a person's authorized trace.

Only the second through fifth are appropriate default material for this
exploration. Live device location remains out of scope.

### 3.6 Social translucence: social systems need legibility, not maximal exposure

Erickson and Kellogg's social-translucence framework emphasizes visibility,
awareness, and accountability. A social system must make socially significant
state sufficiently visible for people to understand what is happening and act
coherently; “translucence” does not mean revealing everything.

Source: [IBM Research — Social Translucence](https://research.ibm.com/publications/social-translucence-designing-social-infrastructures-that-make-collective-activity-visible)

**Lesson for Vesper:** the current doctrine may under-provide visibility in
its effort to avoid social pressure. If the user cannot tell who contributed,
what is available, what is shared, or whether an Occasion is active, consent
may be technically correct while the social product remains illegible.

The solution is not more activity. It is visible, attributable, bounded social
state.

### 3.7 Selective sharing and networked privacy

Research on selective sharing found that people organize audiences around life
facets, tie strength, and interests, balancing relevance and privacy. Research
on interpersonal disclosure emphasizes that privacy is collectively managed:
one person's photograph or account can implicate several people, so burden
cannot sit entirely with the uploader after publication.

Sources:

- [Talking in Circles: Selective Sharing in Google+](https://research.google/pubs/talking-in-circles-selective-sharing-in-google/)
- [We're in It Together: Interpersonal Management of Disclosure](https://researchportal.tuni.fi/fi/publications/were-in-it-together-interpersonal-management-of-disclosure-in-soc/)
- [unFriendly: Multi-Party Privacy Risks](https://research.google/pubs/unfriendly-multi-party-privacy-risks-in-social-networks/)

**Lesson for Vesper:** audience must be understandable at expression time,
and subjects or co-participants need meaningful objection and correction
paths. A shared-world surface must never imply that the author alone can
publish another person's identity, attendance, photograph, or private Outcome.

### 3.8 Attentional agency: preserve a pull-based alternative to Home ranking

Recent work on attentional agency distinguishes what a system pushes toward a
person from what the person deliberately pulls or seeks. Research on teachable
feeds also finds that centralized ranking can obscure the nuanced signals
people use to judge relevance.

Sources:

- [Push and Pull: A Framework for Measuring Attentional Agency](https://arxiv.org/pdf/2405.14614)
- [Mapping the Design Space of Teachable Social Media Feed Experiences](https://arxiv.org/abs/2401.14000)

**Lesson for Vesper:** Home may select one relationship-place opening without
becoming the only way to access current social material. A user-invoked view
can preserve agency even if it is finite, composed, and non-chronological.

## 4. The content model: do not call everything “activity”

The existing application has a legacy `Your people` screen and a backend
follow-feed endpoint. Its events include saves, loves, Plan additions,
bookings, shared itineraries, and published stories. This substrate is useful
as evidence of existing code, not as product authority.

The new exploration must separate the following semantic families:

| Family | Human meaning | Canonical owner | Eligible for aperture? |
| --- | --- | --- | --- |
| **Authored Status** | “I chose to make this available to you for a while” | person / share projection | Yes, under explicit audience and expiry |
| **Directed handoff** | “This made me think of you” | addressed contribution + affected object | Yes, as arrival/door; not as popularity event |
| **Shared motion** | “We have something consequential in progress” | Occasion / Plan / Commitment / Decision | Yes, summarized with owner navigation |
| **Shared Place perspective** | “This person's situated judgment changes this Place for me” | Place relationship / handoff | Yes, primarily through Places and map |
| **Shared occurrence** | “This happened among authorized participants” | Life / Occasion record | Only if newly useful; otherwise Life |
| **Relationship continuity** | “What we carried together remains available” | Life / People / relationship-place record | As a stable door, not changing activity |
| **Public Place contribution** | “This attributed perspective is available to an allowed public” | Place commons | Horizon only in this phase |
| **Operational update** | “The shared consequence changed” | Occasion / Plan / live engine | Yes when viewer-affected |
| **Private behavior** | Save, dwell, search, route, booking, listening, or inferred presence | private owner | No, unless separately authored for sharing |
| **Platform event** | Followed, viewed, reacted, joined, opened | relationship/platform telemetry | No default consumer content |

The aperture admits **humanly meaningful shared state**, not database events.

## 5. Competing information architectures

Use the same fixture evidence and current-world state for every alternative.
Do not make one option artificially empty or visually inferior.

### IA-0 — Distributed-only control

No new owner surface.

- Home admits at most one earned current relationship-place opening.
- Places shows attributed handoffs, scopes, and shared Place layers.
- Occasion holds shared action.
- Life People holds shared continuity and person-specific arrivals.
- Chat receives and routes social intent.

**Question:** Can stronger entry points, person labels, and cross-root doors make
multiplayer sufficiently legible without an aggregate social destination?

**Success condition:** a participant can answer the six orientation questions
in §1.2 without hunting and can explain Vesper's multiplayer value after one
session.

**Failure signature:** everything is semantically correct but the user says,
“Where do I see my friends?” or perceives Vesper as single-player.

### IA-1 — Life People with one present-tense aperture

Keep Life's stable People record. Add one finite, clearly separated doorway or
opening into current material; do not turn the root into a changing feed.

Possible treatment:

```text
Life · People
  stable shared records
  met along the way
  fixed windows
  one bounded door: Available from people now →
```

**Question:** Can Life provide discoverability while preserving its fixed,
record-first posture?

**Success condition:** the present layer feels like an optional door from the
record, not a second Home embedded above it.

**Failure signature:** current Statuses and active Plans dominate the stable
record, making Life reorganize on every visit.

### IA-2 — Focused Shared World owner view

A non-root, user-invoked surface entered from Home, Places, Life People, a
person, or an Occasion.

Candidate responsibilities:

- what people deliberately made available to this viewer;
- what the viewer currently shares outward;
- active shared motion across several Occasions;
- a permissioned people-and-Places map;
- stable doors into `Shared with Maya`, circles, and relationship-place records;
- visible source, audience, expiry, and precision boundaries; and
- person search or invitation as secondary infrastructure.

**Question:** Does a finite cross-person composition create enough unique
orientation value to justify its own owner view?

**Success condition:** it is worth opening with no task, makes the product
unmistakably multiplayer, and routes rather than duplicates owner actions.

**Failure signature:** it becomes a heterogeneous card feed, notification
inbox, people directory, or second Home.

### IA-3 — Fifth-root Together counterfactual

Give the social world navigation parity with Home, Chat, Places, and Life.
Compose it honestly, including what would move or compress elsewhere.

**Question:** Is “What exists among my people now?” a fifth durable human
orientation, or a domain slice already covered by Now, World, Dialogue, and
Continuity?

**Success condition:** the fifth root materially reduces confusion and has a
distinct recurring job that cannot be expressed by a focused owner view.

**Failure signature:** users cannot distinguish Home from Together, Places
from the friend map, or Life People from relationship history in Together.

### IA-4 — Places-led social world

No cross-domain Together page. Places gains an intentional `From people` or
relationship scope, with active Occasion and authored Status layers only when
spatially meaningful. Life People remains the durable non-spatial index.

**Question:** Is Vesper's differentiated social center specifically people
giving one another access to Places, making Places the natural social
orientation?

**Success condition:** the map is compelling, semantically clean, and still
useful when friends share non-location artifacts or active Occasions.

**Failure signature:** non-spatial social contribution and shared action are
forced into geography; Places becomes a people map rather than a world model.

## 6. Current recommendation to pressure-test

The leading hypothesis before visual comparison is:

1. keep the four root tabs;
2. preserve Life People as the durable shared record;
3. preserve Home and Places object-native multiplayer projection;
4. preserve Occasion as the bounded owner of shared action; and
5. explore one focused, non-root **Shared World** aperture for present social
   availability and cross-person orientation.

This is not a decision. IA-0, IA-1, and IA-4 remain credible and must receive
equally complete treatments.

The likely division, if IA-2 wins, is:

| Surface | Social question it answers |
| --- | --- |
| **Home** | What involving another person matters now? |
| **Places** | How do human perspectives and shared histories change this world? |
| **Shared World** | What is currently available and in motion across my people? |
| **Occasion** | What are these particular people doing or deciding together? |
| **Life → People** | What have we held together, and what remains true? |
| **Chat** | What do I want to give, ask, send, invite, or repair? |

## 7. Shared fixture world

Use one evidence world across every IA alternative so hierarchy—not content
advantage—determines the result.

### 7.1 Principals

**Feihu**

- returned to New York after Nice → Sorrento → Amalfi → Rome;
- lives in Brooklyn;
- has a recurring waterfront thread and a pasta-mechanism question;
- hosted a dinner with Maya and Alex;
- has personal Rome heat evidence and independent New York plans.

**Maya**

- shared episodes with Feihu since 2019;
- was in Paris during part of Feihu's Europe trip;
- deliberately addressed a city-level Paris heat note to Feihu;
- contributed a photograph to the Brooklyn dinner;
- later narrows or withdraws one contribution;
- has no inferred availability or live location.

**Alex**

- shares five episodes with Feihu;
- contributed a wine-shop receipt to the dinner;
- has an upcoming birthday Occasion;
- may leave one shared record without withdrawing his prior contribution.

**Dana**

- recently returned from Nice and Sorrento;
- explicitly featured one Status for a selected audience;
- does not share precise itinerary, current location, or private artifacts.

**Theo**

- contributed one Red Hook Place handoff;
- participates in Friday dinner but has no durable circle with Feihu;
- is not ranked as close merely because the handoff becomes useful.

### 7.2 Monday current state

- Nothing is urgent.
- Maya's Paris note arrived yesterday and is available to Feihu.
- Dana's Status is still active for twelve hours.
- Alex's birthday Occasion is Saturday; Feihu has accepted but owes no task.
- Friday dinner with Maya and Theo is forming; no final Place is committed.
- Theo's Red Hook handoff is still valid at neighborhood precision.
- Feihu's current Home has independent personal value unrelated to these
  people.
- No live location is shared by anyone.

### 7.3 Thursday current state

- Heat makes a waterfront possibility timely.
- Friday dinner now needs one decision.
- Maya's Status has expired, but her addressed handoff remains under its own
  grant.
- Dana narrowed a Status from Place to city precision.
- One planned venue closes and the Occasion requires repair.

### 7.4 Governance transitions

- Maya withdraws the dinner photograph; dependent derivatives recompile.
- Theo's handoff expires without becoming relationship memory.
- Alex leaves one recurring circle; the prior epoch remains correctly
  attributed.
- Feihu blocks and later unblocks Maya; no grant or proactive opening restores
  itself.
- Dana changes the audience of her current Status; removed viewers lose every
  dependent projection before the next read.

### 7.5 Sparse and dense variants

**Sparse:** only Maya and Alex; one active Occasion; one addressed note; no
Status. The surface must still be useful without growth prompts dominating.

**Dense:** twenty-four people in Life, six currently authored Statuses, three
active Occasions, eight recent handoffs, and several historical shared records.
The surface must remain finite and comprehensible without pretending all
people deserve equal attention.

## 8. Required experience boards

Create complete phone-scale compositions and the navigation between them. Do
not submit isolated card specimens as the primary result.

### S0 — Authority and ownership map

Before visual exploration, map the existing owners:

```text
Status projection
Directed handoff
Place relationship
Person/shared record
Occasion
Plan/Decision/Commitment
Message/Chat
Home projection
Places projection
Life projection
```

For each, name canonical identity, writer, viewer projection, expiry,
withdrawal path, and where the user opens the complete object.

### S1 — The control: no new aperture

Show the same Monday world across:

- ordinary Home;
- Places World Field;
- Life People at rest;
- Shared with Maya;
- active Friday dinner Occasion; and
- Chat entered from one social cause.

Add only the minimum navigation affordances required to discover the social
material. This is IA-0's strongest version.

### S2 — Life People extension

Compose IA-1 at rest and with several active shares. Demonstrate exactly how
current material remains subordinate to the stable record. Include the return
after an authored Status expires.

### S3 — Shared World at rest

Compose IA-2 on ordinary Monday. It must deliver value without urgency,
pending requests, or a demand to post.

Candidate semantic regions to test—not mandatory chapters:

- available from people;
- in motion together;
- the shared world map;
- relationship continuities; and
- what you currently share.

Do not place every region on the page merely because it is listed here. The
composition must establish a real hierarchy.

### S4 — Shared World in motion

Compose Thursday with one active decision, one timely human perspective, one
expired Status, and one Place disruption. Show which item may dominate and
which owner receives the action.

### S5 — Permissioned people-and-Places map

Render these claim types distinctly:

- authored city-level Status;
- addressed Place handoff;
- active Occasion Place;
- historical `our Place`;
- person's shared list or cluster; and
- model-suggested connection using permitted evidence.

The map must show why a person appears and must not imply live presence when
the claim is a Status, handoff, or history.

Create at least three precision states:

```text
city only
neighborhood
specific Place
```

Create expiry and withdrawal states. No device dot is permitted.

### S6 — Relationship continuity door

Enter `Shared with Maya` from:

- the cross-person aperture;
- a Place handoff;
- an active Occasion; and
- Life People.

The destination identity must be one record. Entry context may change the
opening emphasis but not facts, counts, or authority.

### S7 — Authored Status creation and inspection

Show the lowest-friction path from Chat or an existing Artifact to:

```text
Keep private
Send to Maya
Share with selected people
Feature as Status
Contribute to Occasion
Contribute to Place
```

Do not show all choices before social intent exists. For Status, make audience,
precision, expiry, subject rights, and withdrawal understandable in one
material preview—not a policy wizard.

Also show the viewer side and `What you share` inspection. The author must be
able to answer, at a glance, what is visible, to whom, and until when.

### S8 — Occasion as owner, aperture as router

Show Friday dinner summarized in the aperture, then opened in its complete
Occasion owner. The aperture must not reproduce the whole decision system,
guest state, contribution history, or repair controls.

### S9 — Sparse, dense, and silent social worlds

Compose:

1. two people, almost no current sharing;
2. a healthy ordinary network;
3. dense current material;
4. no social graph at all; and
5. everything suppressed by expiry or authority.

No state may turn into contact-import homework, an invite wall, or synthetic
social proof.

### S10 — Withdrawal, narrowing, block, and no restoration

Reuse the Life 17F/17G truths across every IA alternative. Show the actual
consumer surface before and after each transition. No withdrawn title,
thumbnail, paraphrase, map pin, route, snippet, count, or ranking residue may
remain.

### S11 — Fifth-root counterfactual

Give IA-3 its best complete treatment. Redesign navigation honestly and show
what happens to Home, Places, and Life when Together becomes a root. Do not
merely place a fifth icon under the IA-2 page.

### S12 — Comparative verdict

For IA-0 through IA-4, score and explain:

- unique human job;
- immediate consumption value;
- multiplayer legibility;
- pull-based agency;
- duplication of canonical owners;
- Home overlap;
- Places overlap;
- Life People overlap;
- social pressure;
- authority comprehensibility;
- sparse-network usefulness;
- dense-network resilience;
- technical complexity; and
- expected product differentiation.

Do not average the scores into false precision. Name the decisive tradeoffs.

## 9. Interaction and composition laws

### 9.1 One social cause, one primary destination

A unit may preview several effects, but its primary action must route to the
owner of the user's current job.

Examples:

- `See why this Place changed` → Places;
- `Choose Friday's Place` → Occasion / Decision;
- `Reply to Maya` → Chat;
- `See what you share` → share/grant owner;
- `Return to the shared summer` → Life / Shared with Maya.

### 9.2 The aperture is consumption-first

At rest, the first meaningful gesture should normally be opening value, not
creating content. Expression remains readily available but does not dominate
the empty or ordinary state.

### 9.3 Finite by design

Do not create infinite scroll. The surface should have an explicit end and
bounded admissions. Dense state should use meaningful grouping, scopes,
compression, and doors—not pagination disguised as endless content.

### 9.4 No generic chronological stream

Recency may break ties or establish freshness. It is not sufficient reason to
surface. A save, follow, check-in, booking, photograph, or opened message does
not become social content simply because it happened recently.

### 9.5 Rank situations and shared consequences, not people

Never expose:

- closest friend;
- relationship strength;
- most compatible;
- people you interact with most;
- who cares more;
- who always compromises; or
- inferred availability.

An Occasion decision may dominate because it is consequential. Maya does not
therefore become the top-ranked person.

### 9.6 Human-authored expression remains visibly human

Statuses, notes, observations, photographs, handoffs, and messages should keep
the author's voice and attribution. Vesper's connective or operational layer
must use its own register and state what it added.

### 9.7 Nonresponse is complete

No unread counts, reply debt, streak repair, “Maya is waiting,” or repeated
resurfacing after ignore. Pending state belongs only to a real shared
consequence with a defined decision rule or deadline.

### 9.8 Shared map is semantic, not biometric

The map shows authored or governed claims about relationships to Places. It
does not visualize people as trackable moving objects.

Every person-bearing mark should answer:

- Is this where they are, where they were, what they shared, or what is in a
  Plan?
- Who authored the claim?
- At what precision?
- For which audience?
- Until when?
- What happens when it expires or is withdrawn?

If those answers cannot be carried by the mark and its immediate detail, use a
safer non-map treatment.

### 9.9 Life remains durable

Do not make Life People reorder from visit behavior, algorithmic engagement,
or momentary Status volume. The shared record changes when the record changes.
Present delivery belongs to Home, Places, or an explicitly separated
aperture.

## 10. Negative oracles

Reject any proposal that produces one of these outcomes:

1. A conventional feed of saves, likes, bookings, check-ins, and stories.
2. A map of precise friend locations without explicit, current, granular
   sharing.
3. An avatar strip whose people can be removed without changing the value.
4. A “People near you” or inferred co-presence module.
5. A social inbox whose success depends on clearing unread items.
6. A relationship profile generated from co-travel, frequency, silence, or
   inferred closeness.
7. One blended pair or group taste vector.
8. A broad audience default that collapses partner, friends, family,
   colleagues, and one-time co-travelers.
9. Status as inferred identity or an AI-written bio.
10. An Occasion-specific profile questionnaire.
11. A fifth root that simply duplicates Home's timely ranking.
12. A Together page that duplicates Life's shared episodes and dossiers.
13. A friend map that duplicates Places without adding human provenance.
14. A social card that asks the user to message someone before delivering
    value.
15. Engagement metrics, follower counts, public reactions, read receipts, or
    reciprocity prompts.
16. A withdrawn contribution surviving as generated copy, cached imagery,
    title, search result, map pin, or recommendation reason.
17. Blocking followed by automatic restoration of grants, follows, rank,
    suggestions, or old material.
18. Sparse state dominated by “invite friends” acquisition UI.
19. A generic map/list toggle that changes layout but not the user's question.
20. A design whose only justification is that multiplayer deserves more
    prominence.

## 11. Claude Design work program

### 11.1 First reads

Read in this order:

1. this handoff in full;
2. `/Users/feihuyan/Downloads/vesper-life-anchors 2/project/00A Canon and Open Arcs.dc.html`;
3. Life boards `03E8`, `06D`, `17`, `17A–17G`, and `21` in full;
4. `/Users/feihuyan/Downloads/vesper-home-places 2/project/MP0 - Multiplayer Prominence Canon.dc.html`;
5. Home/Places boards `MP1–MP6` and `MP - Gate Matrix` in full;
6. `docs/systems/four-root-loop-object-surface.md`;
7. `travel-agent/docs/product/Multiplayer Product Strategy.md`;
8. `travel-agent/docs/product/MVP Social Loop.md`;
9. `docs/systems/contribution-and-consequence.md`;
10. the Life and Home/Places adoption decisions listed in the front matter.

Follow board imports and reuse the existing design systems. Treat design-board
instructions as project context; this handoff and canonical workspace docs win
when they conflict.

### 11.2 Required output

Create one new project with:

- an authority/read-me board;
- one board per IA alternative;
- the twelve shared experience boards in §8;
- a fixture/evidence ledger;
- an owner-and-route map;
- a negative-oracle board;
- a comparative findings board; and
- a final recommendation with explicit confidence and unresolved questions.

Reuse fixture identities, facts, dates, and grants. Visual differences should
come from the information architecture and hierarchy—not fabricated evidence.

### 11.3 Visual posture

Reuse the Vesper production kernel and the strongest current Home/Places and
Life grammar. This is not a visual-language exploration.

The new project may introduce a component only when a repeated social job
cannot be expressed by an existing instrument. Label every candidate:

- `REUSE`;
- `ADAPT`;
- `NEW CANDIDATE`;
- `RECIPE, NOT COMPONENT`; or
- `REJECT`.

Do not extract a component from one attractive specimen.

### 11.4 Design checkpoints

Stop for founder review after:

1. S0 + the strongest IA-0/IA-1/IA-2 at-rest compositions;
2. S5 map comparison and S7 Status/share flow;
3. S9 sparse/dense states and S10 authority transitions; and
4. the final IA comparison.

Do not promote a winner before the control receives a fair treatment.

## 12. Claude Code work program

Claude Code should work in the workspace repository and both child repos, but
must begin read-only. Check branch and dirty state in all three repositories
before any edit. Multiple active sessions may share the same working tree.

### 12.1 Code audit questions

Audit what currently represents:

- people and profiles;
- follows and follower visibility;
- companions and co-travelers;
- social circles and membership epochs;
- invitations;
- Status or featured-share projections;
- addressed handoffs;
- social feed events;
- Occasion participants and contributions;
- Place lists and Place relationship projections;
- live or historical location;
- audience and visibility grants;
- expiry, revocation, block, and withdrawal;
- shared-record and person-level Life reads;
- Home admission and ranking; and
- cross-root projection envelopes.

### 12.2 Known legacy substrate to treat carefully

Current code includes:

- `travel-app/app/you/people.tsx` — legacy `Your people` view with invitations,
  circles, companions, following, and recent activity;
- `travel-agent/backend/api/routes/follows.py` — a follow activity-feed route;
  and
- `travel-app/data/social.ts` — mapping database events into social activity
  strings.

Do not infer that these shapes should survive. Evaluate each as:

- reusable identity/relationship substrate;
- adapter candidate;
- legacy presentation only;
- incompatible authority model; or
- deletion/migration candidate.

### 12.3 Renderer-neutral fixture contract

Before recommending new APIs, express the §7 world as projections with:

```text
projection_id
canonical_owner
canonical_object_id
viewer_id
author_id
subject_ids
audience_basis
purpose
precision
valid_from
expires_at
source_revision
owner_revision
dependency_revisions
provenance_mode
social_semantic_family
current_state
available_actions
withdrawal_behavior
block_overlay
freshness
why_visible
```

The contract must support IA-0 through IA-4 without introducing a separate
database object for each visual option.

### 12.4 Feasibility report

For every winning design requirement, report:

- existing code path;
- missing semantic or authority field;
- canonical writer;
- read-model/composer owner;
- invalidation and withdrawal path;
- cache/search/media propagation risk;
- migration or adapter requirement;
- smallest implementation seam; and
- test oracle.

Do not implement until the founder has chosen an IA direction and explicitly
authorized a build phase.

## 13. Comparative evaluation protocol

Use task-based comprehension rather than taste questions.

### 13.1 Five-second orientation

After five seconds on the composition, ask the participant:

- What kind of place is this in the app?
- Why is Maya visible?
- Is Maya currently there, or did she share something about there?
- Is anything expected from you?
- Where would you go to see what you and Maya share over time?

### 13.2 Pull journeys

Ask participants to:

1. see what friends have deliberately made available;
2. find the Place Maya shared without remembering her name;
3. see what is happening with Friday dinner;
4. inspect what they currently share outward;
5. revisit the summer shared with Maya;
6. understand why a social item disappeared; and
7. browse for value with no intention to message or plan.

Measure path clarity, interpretation errors, perceived pressure, perceived
creepiness, and whether the result felt worth opening.

### 13.3 Forced comparisons

Compare:

- object-native only versus object-native plus aperture;
- Life doorway versus separate owner;
- authored Status versus inferred activity;
- city-level Status versus precise Place versus live-location language;
- chronological stream versus semantic grouping;
- one socially timely Home opening versus a pull-based social view;
- person-centered index versus Place-centered map; and
- sparse versus dense network.

### 13.4 Success bar

A direction may be recommended only if it demonstrates:

1. unique value beyond Home, Places, and Life;
2. immediate consumption value before contribution;
3. no generic feed dependency;
4. correct interpretation of presence, Status, history, and handoff;
5. legible authorship and audience without policy-heavy UI;
6. usefulness in sparse and dense states;
7. clean owner navigation with no duplicate state;
8. no response debt or inferred intimacy;
9. complete withdrawal and block behavior; and
10. a sentence a new user can use to explain why this exists.

## 14. Decision questions for founder review

The design project should make these decisions concrete:

1. Is cross-person present social orientation a durable user intention or an
   occasional query?
2. Does it deserve an owner view, a Life doorway, a Places scope, or only
   stronger distributed entry points?
3. If there is an owner view, what is its one-sentence job?
4. Is `Shared World`, `Together`, `People`, or another term understandable
   without implying a feed or group-only product?
5. Should a social map lead, support, or exist only as a mode?
6. Which claims may appear spatially without being read as live presence?
7. What is the smallest meaningful Status contract?
8. Can current shares coexist with durable relationship records without
   confusing time and authority?
9. How does the user inspect outward sharing without encountering a privacy
   dashboard?
10. What is the maximum social density Home should admit if a pull surface
    exists?
11. Does the aperture strengthen the product's `person × relationship × Place
    × situation × Outcome` thesis or make it look like a super-app?
12. What evidence would justify revisiting the four-root navigation decision?

## 15. Expected handback

Claude Design should return:

1. the complete project path;
2. a list of boards created;
3. a concise verdict for IA-0 through IA-4;
4. the recommended architecture and the decisive evidence;
5. components reused, adapted, proposed, and rejected;
6. unresolved questions requiring founder judgment;
7. claims that remain fixture-only or unvalidated; and
8. any proposed canon amendments, written as narrow diffs rather than silent
   reinterpretations.

Claude Code should return:

1. the read-only code audit;
2. the renderer-neutral fixture contract;
3. the current-versus-required capability matrix;
4. migration and authority risks;
5. the smallest non-regrettable implementation sequence for the winning IA;
6. tests and negative oracles; and
7. an explicit list of what should remain unimplemented.

Neither agent should claim `consumer-proven`, `build-ready`, `implemented`, or
`shipped` merely because a board exists.

## 16. Copy-paste kickoff prompt

```text
Create a new Claude Design exploration for Vesper's social aperture / shared
world question. Start by reading this handoff in full:

/Users/feihuyan/travel-workspace/docs/working/claude-design-social-aperture-and-shared-world-exploration-handoff-2026-09-02.md

Then read the required Life People/Together boards in
/Users/feihuyan/Downloads/vesper-life-anchors 2 and the multiplayer MP0–MP6
boards in /Users/feihuyan/Downloads/vesper-home-places 2, following the exact
read order in Section 11.1.

The assignment is not to assume Vesper needs a social feed, fifth root, friend
map, or new page. Compare the five information architectures in Section 5
using the same fixture world. Preserve Life People as the durable shared
record, Home and Places as object-native value surfaces, Occasion as the owner
of bounded shared action, and Chat as the place for contribution and response.

Produce complete phone-scale experiences, not isolated cards. Give the
distributed-only control a fair treatment. Explicitly distinguish authored
Status, directed handoff, active shared consequence, historical relationship
continuity, and live location. Live device location is out of scope. Apply the
negative oracles and stop at the four founder checkpoints before promoting a
winner.

Treat this as a product-information-architecture investigation using the
existing Vesper visual system, not a visual-theme exploration and not a
production implementation task.
```

## 17. Working conclusion

Vesper already has:

- the **continuity of multiplayer** in Life;
- the **causal projection of multiplayer** in Home and Places;
- the **bounded action of multiplayer** in Occasion and Plan; and
- the **expression and negotiation of multiplayer** through Chat.

What it may still lack is the **intentional orientation of multiplayer**: a
place—or a sufficiently legible distributed path—where the user can pull on
their currently permissioned social world without waiting for the system to
push one ranked opening.

The next project should determine whether that missing orientation is:

- already satisfied after stronger connective tissue;
- a bounded doorway from Life People;
- a Places-led social scope;
- a focused non-root Shared World owner; or
- genuinely a fifth root.

Do not solve “multiplayer feels secondary” by adding social volume. Solve it by
making people causally valuable, socially legible, and intentionally
reachable—while keeping their boundaries intact.
