---
doc_type: working
status: active
owner: founder / product / design / backend / frontend / data
created: 2026-07-31
expires: 2026-08-30
why_new: The current cold-start experience frames the absence of travel as an empty state, while the product thesis increasingly depends on earning trust through a user's relationship with their home city, turning nearby discovery into coherent local plans, and demonstrating how taste improves both everyday life and future travel. No existing document owns that product promise and its full-stack implementation boundary.
promotes_to:
  - travel-agent/docs/product/Product Thesis.md
  - travel-agent/docs/product/Product Vision and Scope.md
  - travel-app/docs/surfaces/trips-home/contract.md
  - travel-app/docs/surfaces/vesper-home/contract.md
  - a new canonical local-group-plan journey after founder ratification
supersedes: []
depends_on:
  - docs/working/home-surfaces-program-2026-07-28.md
  - docs/working/trips-home-promotion-model-2026-07-27.md
  - docs/working/vesper-home-workbench-2026-07-28.md
  - docs/working/vesper-home-engine-implementation-plan-2026-07-30.md
  - docs/working/places-build-plan-2026-07-28.md
  - travel-agent/docs/product/Product Thesis.md
  - travel-agent/docs/product/Product Vision and Scope.md
  - travel-agent/docs/architecture/Events Strategy and Architecture.md
source_of_truth_for:
  - proposed-cold-start-product-model-2026-07-31
  - proposed-everyday-places-experience-mvp
  - proposed-local-group-plan-full-stack-slice
---

# Cold Start and the Everyday Places Experience MVP

> **Working proposal, not shipped canon.** This document consolidates the
> product discussion through 2026-07-31 and a read-only audit of the current
> backend and mobile code. It intentionally distinguishes vision, proposal,
> existing capability, and certified behavior. Nothing described as proposed
> here should be read as implemented or device-proven.

## 1. Executive decision

The cold start should not communicate:

> You have no trip, therefore there is nothing here yet.

It should communicate:

> Vesper is about your relationship with places. It can help you notice where
> you are, understand what you like, turn an ordinary pocket of time into a
> coherent experience, bring friends into that experience, and carry what it
> learns into every future trip.

The product should prove this before asking a new user to imagine a distant
vacation. A user should be able to get meaningful value in the city they
already know, including requests as ordinary and important as:

- “Plan my weekend in New York.”
- “Give me a fun Friday night with friends.”
- “Dinner, a bar, and then somewhere to dance.”
- “I have four free hours. What would feel like me?”
- “Show me something in Brooklyn I somehow still do not know.”

This is not a generic nearby feed and not merely a higher-volume source of
recommendations. The product's differentiated loop is:

```text
place curiosity
      ↓
taste-aware discovery
      ↓
coherent sequencing
      ↓
private + group coordination
      ↓
an executable plan
      ↓
live adaptation
      ↓
memory and preference learning
      ↓
better local moments and better future travel
```

The cold start should stage the first credible version of that loop.

## 2. Why this belongs in the experience MVP

### 2.1 It establishes what the app is actually about

If the first screen contains only trip creation, the user reasonably concludes
that Vesper is another travel-planning application used a few times per year.
That underrepresents the intended product.

The broader proposition is a persistent relationship with place:

- where the user lives;
- where the user has been;
- where the user may go;
- what repeatedly catches the user's attention;
- which places work for this specific group;
- how time, weather, energy, budget, and geography change what is right now.

Cold start is therefore not just an empty-state design problem. It is the first
explanation of the product's category.

### 2.2 Familiar places are the highest-trust evaluation environment

A recommendation for Rome may sound plausible to a user who does not know
Rome. A recommendation for the user's own neighborhood is immediately
auditable. The user already knows:

- what is overhyped;
- what is actually open;
- which neighborhoods fit together;
- how long moving between them really takes;
- whether a suggestion is interesting or merely popular;
- whether Vesper understands their taste or is producing travel copy.

If Vesper delights someone in their home city, it earns the right to guide them
in an unfamiliar city. Local usefulness is therefore both a value proposition
and a continuous quality test.

### 2.3 Everyday use creates a stronger taste model

Travel is relatively sparse. Local decisions happen weekly:

- the restaurant that won over the prestigious alternative;
- whether the group preferred one long dinner or several stops;
- how far they were actually willing to travel;
- the event they saved but did not attend;
- the neighborhood they return to;
- whether they consistently choose intimate rooms, energetic crowds, quiet
  walks, counter seats, live music, or late nights.

Those choices provide richer evidence than a one-time onboarding quiz. The
world model becomes useful because it learns through real decisions, not
because it asks the user to describe a personality in the abstract.

### 2.4 The local group problem is structurally the travel group problem

A Friday night with friends has the same hard social structure as a group
trip, compressed into several hours:

- one person carries the organizer burden;
- people self-censor around cost, accessibility, energy, and preferences;
- the group chat accumulates links but struggles to make a decision;
- one loud preference can dominate;
- availability changes;
- the plan needs to survive real-world disruption.

This is exactly where Vesper's private intake, group-safe synthesis, proposals,
and shared plan can differentiate it from a discovery feed.

## 3. Product thesis and sequencing tension

The existing product canon already contains both sides of the decision.

The near-term wedge remains: four people coordinate a real trip in Vesper
instead of their group chat. The product thesis explicitly warns against
grading the early wedge as though the full ambient vision must already exist.

At the same time, the same thesis says the larger product expands into resident
discovery and everyday “what should we do?” moments. The product vision goes
further and describes a location-aware Saturday with friends as a central
ambient use case.

This proposal does **not** recommend abandoning or delaying the group-travel
wedge. It recommends adding one deliberately narrow local loop to the
experience MVP because that loop:

1. demonstrates the larger category immediately;
2. reuses the group-travel moat rather than bypassing it;
3. increases the number of meaningful planning episodes;
4. produces taste evidence that compounds into travel;
5. exposes quality failures in a place the user can judge.

The local loop should be a focused extension of the wedge, not a parallel
consumer-discovery product.

## 4. The cold-start promise

Within the first session, a new user should understand four things:

1. **Vesper understands places.** It can reveal something worthwhile about
   the city around them.
2. **Vesper learns taste through evidence.** Saves, reactions, choices, and
   completed experiences make future guidance more specific.
3. **Vesper makes plans, not lists.** It can turn places into a geographically
   and temporally coherent sequence.
4. **Vesper helps groups decide.** Friends can join, express needs safely, and
   converge on a plan without exposing private boundaries.

The first session does not need to demonstrate every capability. It must make
the model legible and deliver one grounded result.

## 5. What the cold start should contain

The page should feel inhabited before the user has a trip. It may use four
classes of material, each with different truth requirements.

### 5.1 A situated hero

The hero should acknowledge the user's present context when permission and
fresh data allow it:

- current city or neighborhood;
- day and time;
- weather only when fresh;
- a realistic pocket of available time;
- one invitation appropriate to that moment.

Examples of the intended register:

- “Friday is still open.”
- “A warm evening in Brooklyn.”
- “Three hours, close to home.”
- “There is more of New York left for you.”

The hero may invite action:

- `Plan tonight near me`
- `Shape the weekend`
- `Give me one surprising place`
- `Make a plan with friends`

It must not invent current weather, opening status, events, user availability,
or social intent. When location is unavailable, the hero should ask for a city
or remain place-agnostic rather than pretending to be situated.

### 5.2 Familiar-city editorial value

The cold experience should surface a small amount of genuinely interesting
material about the user's home city:

- one place with a strong story;
- one neighborhood pattern;
- one timely opening, exhibition, or event;
- one connection to something the user saved or stated they enjoy;
- one “you may have walked past this” local detail.

This material earns attention even when the user does not want a plan. It also
teaches that Vesper is about seeing places more deeply, not merely optimizing
an itinerary.

The quality bar is high. A generic list of nearby restaurants actively weakens
the proposition. Grounded absence is better than low-quality abundance.

### 5.3 Plausible local plans

The product may sketch plans that help the user picture an experience:

- a slow Saturday morning;
- an afternoon built around one exhibition;
- dinner, drinks, and a music event;
- a neighborhood walk with two meaningful stops;
- a rain-proof evening;
- a low-energy plan within a tight radius.

These are not fake bookings or claims about the user's calendar. They are
clearly labeled possibilities derived from fresh place and event data.

A plan should normally contain two to four stops, not a travel-style catalog.
It should show why the sequence works:

- geographic compactness;
- opening and event times;
- transition time;
- energy arc;
- cost shape;
- a useful fallback.

### 5.4 Dreaming beyond home

The cold start should still support travel imagination. The hero or secondary
material can sketch plausible trips from:

- real saved-place clusters;
- stated interests;
- available calendar windows, if authorized;
- reachable destinations;
- seasonal fit;
- prior place affinities.

The difference is narrative priority. A distant trip is one expression of the
relationship with places, not the only proof that the app has value.

## 6. Cold-start states and fallback ladder

“Cold” is not one state. The app should model the evidence actually available.

| State | Available evidence | Appropriate experience | Must not do |
|---|---|---|---|
| C0 — truly cold | No location, saves, history, or taste | Explain the proposition; offer city entry, nearby permission, one taste seed, and open-ended Vesper chat | Fabricate personalization or a home city |
| C1 — situated | Fresh location, no taste | Show one or two editorially strong nearby possibilities; invite a lightweight reaction | Claim the picks match the user's taste |
| C2 — taste-seeded | Location plus onboarding interests or saves | Explain why each suggestion connects to explicit evidence | Turn a weak onboarding chip into a confident identity claim |
| C3 — place-rich | Saves and/or Atlas history, no active plan | Read back recurring place patterns; offer a local plan or a grounded travel sketch | Reduce the user to one simplistic preference label |
| C4 — socially seeded | Friends or prior companions plus local context | Offer a group-initiated plan and a clear invite path | Reveal one person's private constraint to another |
| C5 — returning between plans | Rich history, no current trip | Emphasize continuity: local openings, remembered taste, unfinished curiosities, and the next useful session | Describe the state as empty because nothing is booked |

The fallback order should be:

```text
fresh, personally grounded local value
  → fresh, editorially grounded local value
  → grounded saved-place travel sketch
  → transparent teaching prompt
  → honest open invitation
```

Never fall back from missing evidence to synthetic confidence.

## 7. The flagship local scenario

The MVP should optimize for one memorable, legible scenario:

> It is Friday afternoon in New York. The user wants dinner, a bar, and then a
> rave with three friends. The group prefers a compact route, wants to spend
> less than $100 per person, and does not want a generic tourist night.

The target flow:

1. The user opens Vesper or Trips and sees `Shape Friday night`.
2. Location is requested in context, or the user selects New York manually.
3. Vesper asks at most one high-value question if essential context is absent.
4. Vesper searches restaurants, bars, and fresh event inventory.
5. Vesper proposes one coherent evening and one meaningful alternative—not a
   long recommendation list.
6. The user taps `Bring friends in`.
7. Friends join the planning conversation before or during plan commitment.
8. Vesper gathers sensitive constraints privately.
9. Vesper publishes a group-safe plan without explaining whose constraint
   shaped it.
10. The group accepts or changes the plan through the existing proposal path.
11. The plan becomes a compact shared object with time, place, map, transitions,
    and links for reservations/tickets.
12. If a venue closes or the event is canceled, Vesper proposes a replacement
    through the same ledgered, reversible mutation system.
13. Afterward, reactions and outcomes become transparent taste evidence.

This scenario demonstrates discovery, taste, sequencing, collaboration,
execution, adaptation, and learning in one small episode.

## 8. The product object model

Three different objects are involved and should not be collapsed in the UI.

### 8.1 Ambient read

A read is ephemeral, informational, and does not imply commitment.

Examples:

- “Two things nearby you may care about.”
- “A new exhibition connects to the small design museums you keep saving.”
- “The weather makes the waterfront unusually good tonight.”

It may start a private Vesper session. It is not yet a plan.

### 8.2 Local plan

A local plan is durable and executable:

- explicit date or time window;
- current city or neighborhood as its spatial frame;
- one or more sequenced stops;
- optional companions;
- shared discussion and change history;
- live state while the outing is happening;
- completion and memory afterward.

The user-facing language may be “Tonight,” “Friday,” “Weekend,” “Plan,” or the
plan's own title. It should not need to call itself a trip.

### 8.3 Travel plan

A travel plan retains the current trip lifecycle:

- destination away from home;
- broader date range;
- accommodation and transportation;
- multi-day structure;
- departure and return arcs;
- booking and expense depth.

Both local and travel plans should reuse the same underlying coordination and
itinerary machinery wherever their invariants are identical.

## 9. Recommended architectural decision

### 9.1 Decision

Do not create a parallel `outings` stack for the MVP.

Generalize the existing durable planning aggregate with an explicit semantic
discriminator, provisionally:

```text
plan_kind = travel | local
```

The existing trip record, itinerary graph, member model, group conversation,
proposal system, plan-event ledger, map, and live situation engine can remain
the canonical implementation underneath. The UI and read models should project
the correct language and capabilities for each kind.

The exact field name requires schema review. The important ruling is that the
kind is explicit rather than inferred from duration. A single-day excursion
away from home can be travel; a weekend in the home city can be local.

### 9.2 Why not a second domain

A separate outing domain would duplicate or fork:

- membership and invitations;
- private intake and group-safe composition;
- itinerary writes;
- proposals, votes, receipts, and reverts;
- Plan/Map synchronization;
- event and venue pinning;
- live current/next logic;
- proactive routing;
- completion and memory.

That creates parallel writers and drift risk. The project invariant is one
canonical mutation path per mutation type.

### 9.3 Kind-specific capability policy

| Capability | Travel | Local |
|---|---:|---:|
| Sequenced itinerary | Yes | Yes |
| Group membership/chat | Yes | Yes |
| Private constraints | Yes | Yes |
| Proposals and voting | Yes | Yes |
| Map/current-next | Yes | Yes |
| Accommodation | Yes | Hidden by default |
| Intercity transport | Yes | Hidden by default |
| Flights | Yes | Hidden |
| Expenses | Yes | Optional, later |
| Voice/audio guide | Yes | Eligible where content exists |
| Departure countdown | Yes | Replaced by time-until-start |
| Post-plan memory | Yes | Yes, lighter weight |

## 10. Current full-stack reality

### 10.1 What already exists

The underlying substrate is stronger than the current experience suggests.

#### Flexible trip creation

- destination and dates can be absent during ideation;
- loose windows such as “next weekend” can resolve into dates;
- a private conversation can be promoted after explicit confirmation;
- conversation participants can become plan members on promotion.

#### Planning engine

- scopes include `trip`, `day`, `period`, and `gap`;
- operations include create, extend, refine, and repair;
- the planner supports timed itinerary blocks, venue and experience IDs,
  transitions, energy rationale, warnings, and preservation-safe replanning;
- “Plan dinner tonight” is already a valid planning-task example.

#### Discovery and search

- GPS-backed nearby search exists;
- the backend merges a curated corpus with provider fallback;
- nearby ranking can use saves, loved categories, and stated interests;
- search covers restaurants, venues, activities, concerts, theater, festivals,
  food events, and nightlife;
- experience records support one-off, recurring, and on-demand availability.

#### Collaboration and execution

- conversation-scoped invitations exist before trip promotion;
- trip invitations, membership, group chat, proposals, votes, and plan mutation
  exist after promotion;
- accepted changes are ledgered and reversible;
- Plan, Map, current/next state, notifications, and voice-guide infrastructure
  exist for trip-scoped contexts.

#### Home and memory

- Trips Home can already project ambient `happening_nearby` and
  `place_context` material;
- Vesper Home owns persistent sessions;
- Places and Atlas provide saved, visited, historical, and place-reading
  substrate;
- the home feed has a taste-aware “near you” producer and honest empty behavior.

### 10.2 What is missing

#### No first-class local-plan semantic

The durable planner still refuses to run without `trip_id`. It can research
events in an ambient conversation, but it cannot persist a coherent,
collaborative evening until the system creates something understood as a trip.

#### Travel-only language at entry

Trips begins with `BEGIN A TRIP`. Its starter shapes are City, Beach, Mountain,
Road, and Festival. Vesper's cold prompts emphasize destinations, seasons, and
future travel. The system's local capabilities are therefore undiscoverable.

#### First-turn location race

Chat currently sends a cached location synchronously and warms GPS for the next
turn. On a first-ever request such as “plan tonight near me,” the location may
not reach the server until the following message.

#### Fragmented place resolution

Some nearby paths require both coordinates and a city slug. The location-aware
entry should resolve a canonical city/neighborhood once and carry that context
through search, planning, and display.

#### Pre-promotion invitation is not surfaced

The backend and API client support conversation invites, but the mobile product
does not expose that action in the planning experience. Collaboration starts
visibly only after promotion, even though the system can begin earlier.

#### Event inventory is uneven

Mainstream event infrastructure exists, but the exact “rave tonight” promise is
limited by inventory. Resident Advisor and DICE do not provide open consumer
APIs; curator submission, stronger underground coverage, music-taste
integration, and cross-source deduplication remain unfinished.

#### No canonical local journey

The journey registry certifies trip ideation, invitations, private constraints,
group proposals, live trips, and proactive routing separately. It does not
contain one end-to-end local group plan beginning in the user's home city.

## 11. Surface responsibilities

The three home surfaces should each express the local model without becoming
duplicates.

### Trips: durable commitments

Trips owns committed travel and local plans:

- tonight's accepted plan;
- this weekend's group plan;
- an upcoming trip;
- decisions and changes requiring action;
- history/archive access.

A local plan should render with local semantics and compact geometry. It should
not show flight, hotel, or departure chrome.

### Vesper: intent and relationship

Vesper owns:

- “What should we do?”
- starting with an incomplete desire;
- taste explanation;
- asking about a place;
- shaping a night or weekend;
- private intake;
- returning to an unfinished planning session;
- audio and conversational interaction.

The strongest cold-start CTA likely begins here even if Trips also exposes a
door.

### Places: the world and spatial evidence

Places owns:

- nearby places;
- saved and visited relationships;
- city/neighborhood exploration;
- maps and spatial context;
- venue and place detail;
- the evidence from which a local plan can begin.

Places should offer `Ask Vesper` / `Build around this` handoffs rather than
developing a second planning engine.

## 12. Location, permission, and privacy contract

### 12.1 Contextual permission

Do not ask for location only because the app launched. Ask when the value is
immediately legible:

> Use your location to shape something nearby tonight.

The user must be able to:

- deny or defer without losing the rest of the product;
- enter a city manually;
- understand whether a suggestion used live location, home city, or a selected
  place;
- revise the assumed place.

### 12.2 Location-sensitive first-turn preflight

For explicit nearby actions:

1. acquire foreground permission;
2. fetch a fresh reading;
3. resolve canonical city/neighborhood context;
4. attach provenance and freshness;
5. then begin the first planning turn.

Ordinary chat should not be delayed by this path.

### 12.3 Group privacy

One person's precise location, private budget, accessibility need, dietary
constraint, or reluctance must never be copied into group-visible prose.

Group-bound text must continue through the existing group-safe composition
boundary. Location should be expressed at the minimum useful granularity:

- “starting in the East Village” when the group explicitly shares that start;
- never “Maya is currently at [precise coordinate/address]” as planning
  rationale.

## 13. Taste model and explanation

Cold-start personalization must be calibrated to evidence strength.

### Evidence ladder

1. **Stated:** onboarding interest or direct request.
2. **Saved:** a place the user deliberately kept.
3. **Chosen:** an option accepted over alternatives.
4. **Experienced:** an attended/completed place or event.
5. **Repeated:** a pattern across several contexts.
6. **Socially contextual:** a preference specific to one companion or group.

The UI and Vesper's language should reflect this ladder:

- Weak: “You said you are interested in live music.”
- Stronger: “You keep saving small live rooms.”
- Strong: “Across three nights, you chose intimate venues over larger shows.”

Avoid identity declarations based on one tap. The user should be able to see,
correct, or forget consequential taste claims.

### Local-to-travel transfer

The key product payoff should become visible:

> Because you repeatedly choose compact neighborhoods, unhurried dinners, and
> small music rooms at home, Vesper can look for their equivalent in Lisbon.

This is stronger than “recommended for you.” It shows how the world model
translates taste across places while preserving context.

## 14. Content strategy

### 14.1 Two content jobs

Cold start needs both:

1. **Evergreen place understanding** — stories, neighborhood texture,
   distinctive venues, and reasons a place matters.
2. **Operational freshness** — what is open, what is happening, ticket status,
   weather viability, and whether the plan still works tonight.

Editorial depth without freshness produces beautiful but unusable plans.
Fresh listings without editorial judgment produce generic feeds. Vesper needs
both.

### 14.2 NYC pilot

The first local pilot should be intentionally bounded:

- New York City, with neighborhood-aware identity;
- a reviewed base of high-character places;
- reliable restaurants and bars;
- mainstream event ingestion;
- EDMTrain or equivalent permitted electronic-music coverage;
- manually reviewed recurring nights and selected venue calendars;
- clear outbound handoffs to ticket and reservation providers;
- freshness timestamps and honest unavailable states.

Global breadth should not precede local density and trust.

### 14.3 Curator layer

The most differentiated local material often does not live in mainstream APIs:

- small gallery openings;
- supper clubs and pop-ups;
- recurring scene nights;
- neighborhood rituals;
- places that become meaningful only through a curator's explanation.

The long-term moat is not merely an events API. It is structured local judgment
combined with the user's taste and the group's context.

## 15. Competitive frame

### Atlas Obscura

Atlas Obscura is adjacent on curiosity, editorial depth, hidden places, and
community-contributed local knowledge. Its official product emphasizes a large
map of unusual places, detailed backstories, custom lists, community
contributions, local experiences, and unusual guided trips.

Cold-start lesson:

- lead with wonder before logistics;
- give the user immediate value without requiring a trip;
- let a place have a story, not only utility;
- build an enduring corpus that makes “near me” interesting.

Differentiation for Vesper:

- personal and group taste rather than a universal catalog of curiosities;
- coherent time/geography sequencing rather than lists alone;
- private group alignment;
- an executable shared plan;
- live adaptation and a durable relationship across local life and travel.

Official references:

- [Atlas Obscura — About](https://www.atlasobscura.com/about)
- [Atlas Obscura app](https://app.atlasobscura.com/)

Funding/scale context: Atlas Obscura is not an early prototype operating only
on founder labor. Its own press archive links to the reported 2019 $20 million
Airbnb-led funding round, and its current materials describe a large community,
an extensive proprietary place catalog, editorial operations, experiences, and
commercial partnerships. That makes its corpus and brand difficult to reproduce
directly. The useful lesson is to compete through the Vesper relationship and
coordination loop, not by trying to out-publish an established media company.

- [Atlas Obscura press archive](https://press.atlasobscura.com/)

### Suna

Suna is more directly adjacent to the local cold-start proposition. Its current
official positioning includes personalized nearby recommendations, daily picks,
location-aware proximity alerts, mood/weather context, hidden places, and AI
itinerary generation for a free afternoon or a longer trip.

Cold-start lesson:

- “what should I do right now?” is understandable without education;
- a small daily set is more legible than an infinite feed;
- ambient/proximity value can make an app useful before travel;
- current location, weather, mood, and novelty are powerful first-session
  context.

Differentiation for Vesper:

- local discovery is only the opening move;
- Vesper should own group decision-making, private constraint collection,
  proposals, shared plan mutation, and live recovery;
- taste should transfer across companions and cities;
- the relationship should include intake, voice/audio, place understanding,
  itinerary change, memory, and future-trip continuity.

Suna appears to cover a meaningful slice of local discovery and itinerary
generation. It does not, from its public positioning, demonstrate the same
depth of group governance and trip collaboration Vesper is building. That
should be treated as a differentiation hypothesis to validate in product use,
not an absolute claim about every feature in the competitor's code.

Official references:

- [Suna official site](https://www.unaryx.com/)
- [Suna App Store listing](https://apps.apple.com/sg/app/suna-things-to-do-near-you/id6759053765)

Funding/scale context: no reliable public funding disclosure was found in
Suna's official materials during the 2026-07-31 review. The App Store lists an
individual developer, so the prudent working assumption is that it is a small,
fast-moving product—not that it is unfunded or that its internal capabilities
are trivial. Its narrow public proposition is useful evidence that local,
personalized discovery can be explained simply; it is not evidence that Vesper
should copy its product boundary.

## 16. Detailed MVP requirements

### 16.1 Frontend

- Add local starters to Vesper Home and the cold/between Trips experience.
- Replace absence-oriented cold copy with relationship-with-place framing.
- Add a contextual location preflight for nearby starters.
- Support manual city/neighborhood selection.
- Render local plan identity without travel chrome.
- Surface `Bring friends in` during the pre-commit conversation.
- Show one coherent plan and one meaningful alternative.
- Expose why a suggestion is grounded without exposing private inputs.
- Route place cards through existing canonical detail and Vesper handoffs.
- Keep the active local plan reachable from Trips, Vesper session history, and
  appropriate notifications.
- Provide honest loading, thin-data, denied-permission, stale-event, and
  no-results states.

### 16.2 Backend domain and API

- Add an explicit local/travel plan discriminator after founder schema review.
- Preserve one canonical membership, itinerary, proposal, and plan-event path.
- Allow same-day and weekend local promotion with explicit user confirmation.
- Project kind-appropriate capabilities and copy inputs.
- Resolve coordinate input to canonical place identity with provenance.
- Allow the planner to operate on a local plan through the existing planning
  contract.
- Suppress irrelevant travel requirements such as accommodation readiness.
- Ensure completion writes appropriate memory/taste evidence without treating
  every local plan as a major trip story.
- Keep all group-visible synthesis behind the group-safe composer.

### 16.3 Agent behavior

- Recognize local horizons: now, tonight, tomorrow, this weekend, and a free
  period.
- Distinguish a request for options from a request for a coherent plan.
- Ask no more than one blocking question when a reasonable grounded default is
  available.
- Prefer a small geographic footprint unless the user requests otherwise.
- Build around one anchor when appropriate.
- Include transition and timing logic.
- Verify time-sensitive facts or mark them unverified.
- Give one strong plan before offering breadth.
- State uncertainty without collapsing into generic advice.
- Route social coordination into the existing invitation and group-planning
  system.

### 16.4 Data and operations

- Define launch neighborhoods and minimum corpus density.
- Track place and event freshness separately.
- Add cross-source event deduplication.
- Add cancellation/closure verification where available.
- Measure provider coverage by category, neighborhood, date, and time window.
- Establish a reviewed local-curation workflow.
- Store provenance for every surfaced operational claim.
- Prevent stale or synthetic listings from appearing as current truth.

## 17. Suggested delivery sequence

### Phase 0 — Ratify the slice

- Ratify the flagship NYC Friday-night scenario.
- Ratify whether the experience MVP expands beyond the current travel wedge.
- Approve the explicit local/travel semantic.
- Register the proposed canonical journey and branch inventory.
- Define the initial content coverage floor.

### Phase 1 — Honest local entry

- Add `Plan tonight near me` and `Shape the weekend` entry points.
- Add contextual location preflight and manual fallback.
- Carry canonical place context into the first Vesper turn.
- Update cold-state copy so no-trip does not mean no value.

Outcome: Vesper can understand and research the local request without
pretending that a durable plan already exists.

### Phase 2 — First-class local plan

- Add the explicit kind discriminator.
- Reuse the existing promotion flow with local semantics.
- Generate a compact same-day itinerary through the canonical planner.
- Project local plan identity in Trips and Plan.
- Hide irrelevant travel modules.

Outcome: a user can create, reopen, and complete one local plan.

### Phase 3 — Collaboration before commitment

- Surface conversation invites.
- Accept friends into the planning context.
- Gather private constraints.
- Produce group-safe synthesis.
- Commit and revise through existing proposal and ledger paths.

Outcome: the local plan demonstrates Vesper's group advantage rather than
behaving like an AI recommendation generator.

### Phase 4 — NYC event and nightlife reliability

- Add the chosen permitted event sources.
- Seed and review nightlife coverage.
- Add deduplication, freshness, and cancellation states.
- Build the dinner → bar → event planning recipe.
- Validate outbound ticket/reservation handoffs.

Outcome: the flagship scenario is factually useful, not just structurally
possible.

### Phase 5 — Live local execution and learning

- Enable current/next and lightweight map mode.
- Support disruption replacement through canonical proposals.
- Capture transparent reactions and outcomes.
- Reflect learning in Places/Atlas and future Vesper explanations.

Outcome: the complete local-to-taste-to-future-travel loop becomes visible.

## 18. Proposed canonical journey

Provisional label: **J29 — Home City Intent to Shared Live Plan**. The number and
name are proposals until registered.

### Product promise

A person can turn an ordinary pocket of time in a familiar city into a
taste-aware, group-safe, executable plan, and Vesper can adapt that plan without
losing shared truth or exposing private constraints.

### Required branches

| Branch | Required proof |
|---|---|
| Location allowed before first turn | FE, BE, VIS, LIVE |
| Location denied; city entered manually | FE, VIS |
| Cold user with no taste | FE, BE, VIS |
| Taste-seeded user gets evidence-calibrated explanation | FE, BE, VIS, LIVE |
| Conversation invite before local-plan commitment | FE, BE, VIS, LIVE |
| Private constraint changes plan without leaking | FE, BE, VIS, LIVE |
| Event inventory empty or stale | FE, BE, VIS |
| Accepted group proposal mutates plan | FE, BE, VIS, LIVE |
| Event cancellation triggers replacement proposal | FE, BE, VIS, LIVE |
| Plan, Map, chat receipt, and notification converge | FE, BE, VIS, LIVE |
| Completion writes explainable taste evidence | FE, BE, VIS, LIVE |

### Must never happen

- First-turn “near me” planning silently uses no location or the wrong city.
- Location permission is mandatory for unrelated product value.
- A generic provider result is presented as a personal recommendation.
- An unverified event is presented as definitely happening.
- A private member constraint appears in group chat, a push, a plan rationale,
  or a booking/ticket handoff.
- A local change bypasses the canonical proposal/plan-event writer.
- Plan and Map disagree after an accepted or reverted change.
- The product claims the journey is complete based only on static or backend
  tests.

### Certification ladder

1. Static trace across frontend and backend.
2. Frontend mock walk covering every declared visible branch.
3. Real-Postgres backend scenario with disposable users and events.
4. Real-provider NYC content canary.
5. Two-device group walk with real auth.
6. Physical-device location and disruption walk.

The journey remains unshipped until the required device and live-provider
evidence exists.

## 19. Success metrics

### First-session comprehension

- Percentage of new users who correctly understand that Vesper works locally
  as well as for travel.
- Time to first grounded place value.
- Time to first coherent plan.
- Location-permission acceptance when requested contextually.
- Manual-location completion when permission is declined.

### Local value

- Local starter engagement.
- Plans created per situated session.
- Plans accepted or shared.
- Plans that reach at least one real-world handoff or completion signal.
- Repeat local planning within 7 and 30 days.

### Group moat

- Pre-commit invites created and accepted.
- Share of local plans involving more than one member.
- Time from invitation to group decision.
- Proposal acceptance/revision rate.
- Percentage of groups returning for another local or travel plan.

### Trust and quality

- Incorrect location reports.
- Stale/closed venue and canceled-event reports.
- Generic-result dismissals.
- User corrections to taste explanations.
- Privacy incidents, with a target of zero.
- Plan/Map/chat divergence incidents, with a target of zero.

### Compounding value

- Local evidence reused in later recommendations with visible provenance.
- Improvement in acceptance after several local interactions.
- Local users who later begin a travel plan.
- Travel groups whose collaboration graph began with a local plan.

## 20. Non-goals for the first release

- A global real-time event graph.
- A public social feed.
- Open creator monetization.
- Automatic reservations or ticket purchases without confirmation.
- Continuous background location as a prerequisite.
- Inferring a precise home address.
- Replacing Maps, Resy, OpenTable, DICE, or Resident Advisor.
- Supporting every local-plan archetype equally.
- Building a second itinerary, membership, or proposal stack.
- Claiming deep taste from one or two weak signals.

The MVP should own decision and coordination, then hand off cleanly to providers
for transactions it does not yet own.

## 21. Risks and countermeasures

| Risk | Countermeasure |
|---|---|
| Expansion distracts from the group-travel wedge | Ship one group-first local scenario, not a broad discovery roadmap |
| Cold start becomes visually busy | One situated hero, one local proof, one primary action; progressive disclosure afterward |
| Local recommendations feel generic | Editorial/corpus quality floor; provider results need taste evidence or explicit generic labeling |
| Event data is stale | Source timestamps, short TTLs, verification, and honest unavailable states |
| Local objects pollute Trips | Explicit kind, compact local projection, and separate capability policy |
| Location request feels invasive | Ask in context, foreground only, manual fallback, visible provenance |
| Group value arrives too late | Surface existing conversation invites before commitment |
| Private constraints leak | Preserve the canonical group-safe composition boundary and certify with adversarial fixtures |
| Local and travel planning fork | Reuse canonical planners, proposals, ledgers, and read models |
| Beautiful mock overstates reality | No synthetic personalization or fake live inventory; certify with real provider/device layers |

## 22. Open founder decisions

1. Is this local group loop officially part of the experience MVP, or an
   immediately following expansion?
2. What user-facing noun should represent a local durable object: `plan`,
   `night`, `weekend`, or contextual titles only?
3. What is the internal discriminator name: `plan_kind`, `trip_kind`, or a
   broader aggregate rename?
4. Does a committed local plan appear in Trips Home's ranked stack, or does it
   live primarily in Vesper until it becomes time-bound/actionable?
5. Is New York the sole content pilot?
6. Which event sources and manual-curation practices are legally and
   operationally acceptable for the pilot?
7. What minimum inventory/freshness threshold is required before the product
   may promise a rave or event-led night?
8. Is pre-commit friend invitation a launch requirement or may the first slice
   promote the local plan immediately before inviting?
9. Which local interactions are allowed to update durable taste automatically,
   and which require user confirmation?
10. What visual artifact will become the design source of truth for the cold,
    situated, local-plan, and local-live states?

## 23. Immediate next artifact

Before implementation, produce one end-to-end design and contract board with
these states side by side:

1. C0 truly cold, no location permission.
2. C1 situated in New York, no taste history.
3. C3 situated with saves/taste evidence.
4. Friday-night Vesper conversation before commitment.
5. `Bring friends in` and private intake.
6. Proposed dinner → bar → event plan.
7. Accepted local plan in Trips.
8. Live local plan and disruption replacement.
9. Completed plan with transparent taste learning.

For each state, the board should show:

- exact data requirements;
- honest fallback;
- primary action;
- destination route;
- group/private visibility;
- mutation owner;
- whether the state is mock-only, backend-real, provider-real, or device-proven.

That artifact should resolve the open founder decisions and become the visual
input to the canonical journey and implementation plan.

## 24. Bottom line

The app should not wait for a booked trip to become alive.

Cold start should let Vesper prove that it understands a place the user already
knows, convert that understanding into a plan the user could actually live,
help friends make the decision together, and explain how the resulting evidence
makes every later place recommendation better.

The existing stack already contains much of the difficult machinery. The work
is to expose it through a first-class local semantic, strengthen local content
quality, connect the invitation path, and prove the complete loop on devices
without weakening the privacy and mutation guarantees that make the group
product trustworthy.

## 25. Current-state evidence map

Use these anchors when converting the proposal into an implementation plan.
Line numbers describe the 2026-07-31 working-tree snapshot and may move.

| Claim | Evidence |
|---|---|
| The larger thesis includes resident discovery and everyday “what should we do?” moments | [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md#what-we-are-building-toward) |
| The ambient vision explicitly requires a group-in-place model that does not require a trip | [Product Vision and Scope](../../travel-agent/docs/product/Product%20Vision%20and%20Scope.md#the-ambient-layer-beyond-travel-to-everyday-group-life) |
| Current trip records allow nullable place and dates but have no local/travel kind | [Trip model](../../travel-agent/backend/core/models/trips.py) — `Trip` near line 306 |
| The planner supports day/period/gap scopes and “Plan dinner tonight” | [Planning request](../../travel-agent/backend/planning_agent/schemas.py) — `PlanningRequest` near line 98 |
| Durable plan execution currently requires trip context | [Planning handler](../../travel-agent/backend/concierge/tool_handlers/planning/_plan.py) — `_execute_generate_plan_once` near line 1093 |
| Ambient event search can work without a trip when it has a destination | [Concierge search handler](../../travel-agent/backend/concierge/tool_handlers/search.py) — `_execute_search_experiences` near line 124 |
| Conversation-scoped invites already exist before trip promotion | [Invite routes](../../travel-agent/backend/api/routes/invites.py) — conversation invites near line 496 |
| The frontend API exposes conversation invite creation but has no product callsite | [API interface](../../travel-app/utils/api/interface.ts) and [HTTP implementation](../../travel-app/utils/api/http.ts) |
| First-turn chat uses cached location and warms the next turn asynchronously | [useConciergeChat](../../travel-app/hooks/useConciergeChat.ts) — message location near line 736 |
| Nearby discovery is corpus-first with provider fallback | [Nearby discovery](../../travel-agent/backend/places/discovery.py) |
| Generic provider rows require taste evidence and may honestly return empty | [Taste ranking](../../travel-agent/backend/places/taste.py) |
| Current trip creation is explicitly framed as `BEGIN A TRIP` | [Trip begin](../../travel-app/app/trip-begin.tsx) — header near line 131 |
| Current Vesper cold prompts are dominated by future travel | [Vesper Workbench](../../travel-app/components/vesper-workbench/VesperWorkbench.tsx) — `GHOST_COPY` near line 52 |
| Current cold Trips language frames the year as blank | [Trips Home model](../../travel-app/components/trips/TripsHomeModel.ts) — `tripsStandfirst` near line 128 |
| Underground events, curator submission, dedup, proactive surfacing, and music-taste integration remain gaps | [Events Strategy and Architecture](../../travel-agent/docs/architecture/Events%20Strategy%20and%20Architecture.md) |
| Existing certification covers the travel journeys, not this local loop | [Journey status](../journeys/STATUS.md) and [Journey registry](../journeys/journeys.yaml) |

### Working-tree caveat

This audit was conducted while both child repositories contained pre-existing,
uncommitted work on Home and Trips surfaces. The findings describe the visible
working-tree snapshot, not only the last commit. Before implementation begins,
recheck both repositories' branches and status, then decide whether the local
plan work extends those changes or begins in isolated worktrees.
