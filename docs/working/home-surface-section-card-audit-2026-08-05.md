---
doc_type: working
status: active
owner: founder / product / backend / frontend
created: 2026-08-05
expires: 2026-09-04
why_new: The Trips, Vesper, and Places roots have each recently consolidated, but no single audit inventories their current section and card taxonomies, identifies contract drift, or tests whether new multiplayer, provenance, ambiance, and artifact ideas require new card families.
promotes_to:
  - a root-surface projection taxonomy decision
  - targeted Trips crown and Places renderer follow-up work
supersedes: []
depends_on:
  - docs/working/cross-surface-ranking-coherence-2026-08-03.md
  - docs/working/trips-crown-receipt-audit-2026-08-03.md
  - docs/working/places-section-contract-2026-08-01.md
source_of_truth_for:
  - home-surface-section-and-card-inventory-2026-08
  - root-surface-taxonomy-recommendations
---

# Home surfaces — section and card audit

> Audit date: 2026-08-05. Read against the current shared workspace, both child repositories, the root-surface contracts, and the latest stored iOS captures. This is a product and implementation audit, not an approval to change product shape without founder review.

## Verdict

The three roots have coherent but intentionally different composition models:

| Surface | Composition model | Current assessment |
| --- | --- | --- |
| Trips | Ranked crown plus a finite continuity trail | Strongest first impression; most accumulated taxonomy and duplication |
| Vesper | One calm workbench with a homogeneous rotating band | Most conceptually disciplined |
| Places | Server-ranked, posture-driven section feed | Cleanest formal card/section contract |

The fact that semantic content types outnumber visual treatments is generally healthy. A `weather` item and a `planning_brief` should not require unrelated card designs. The risks are incomplete mappings, duplicate calls to action, and new mechanics being expressed as new cards instead of richer content inside established projection roles.

| Surface | Section model | Semantic content types | Actual visual families |
| --- | --- | ---: | ---: |
| Trips | Fixed composition plus ranked stack | 25 stack kinds, 10 receipt kinds, 8 legacy postures | ~7 |
| Vesper | Fixed workbench slots | 4 list kinds, 5 fact kinds, 2 seam kinds | 2 row families |
| Places | Server-ordered feed, maximum 4 sections | 16 section reasons, 4 treatments, 9 card kinds | ~7 |

## Trips Home

### Active section inventory

The active root composition, in display order, is:

1. standfirst / mast;
2. one ranked crown;
3. `ALSO IN PLAY` ranked queue;
4. standing Ask Vesper card;
5. optional Companion Reading;
6. `ON THE TABLE` trip sketch and saved-city seeds;
7. `TRIP FEEL` selector;
8. `CONNECT`;
9. conditional `WHILE YOU'RE HERE` or `NEAR YOU` rows;
10. all-trips footer.

The root composes these regions in `travel-app/app/(tabs)/trips/index.tsx`. Its primary first-viewport grammar is sound: authored mast, one dominant trip, Vesper's grounded judgment, proof, and one clear next move. The stored quiet-state capture shows this hierarchy working rather than reading as a dashboard.

### Card inventory

The visible families are:

- the universal Trips crown;
- universal ranked rows inside `ALSO IN PLAY`;
- quiet utility panels: `ALSO IN PLAY`, Ask Vesper, Connect, and the seed sketch;
- Companion Reading, a flat reading object;
- saved-city seed cards and Trip Feel selectors;
- compact contextual trail rows.

The backend's `ConciergeHomeCardKind` currently contains 25 stack item kinds: `live_trip`, `urgent_trip_action`, `daily_brief`, `constraint_alert`, `capture_nudge`, `planning_brief`, `trip_retrospective`, `settlement_closeout`, `imminent_trip`, `trip_thread`, `saved_cluster`, `memory_echo`, `weather`, `near_you`, `local_take`, `starter`, `pre_trip_prep`, `atlas_homecoming`, `stay_compare`, `group_room`, `agent_work`, `audio_tour`, `intake_offer`, `invite_seat`, and `location_sharing`.

This many semantic kinds resolving into a single crown and a single row family is good consolidation. The user should experience attention and context, not a catalogue of internal event types.

### Finding 1 — receipt union is not exhaustively rendered

The backend defines ten typed receipt variants for the crown:

- `ledger`
- `checklist`
- `people`
- `shape`
- `diff`
- `call`
- `candidates`
- `spine`
- `waveform`
- `conditions`

The frontend only recognizes `shape`; all other receipt variants collapse to a generic title plus `row_line` treatment. This discards richer, already-grounded evidence that could make the crown feel earned: money relationships, readiness loops, a real group-seat situation, a before/after proposal, candidates, plan shape, audio readiness, or weather conditions.

This is the clearest current gap. Before adding more crown concepts, make the frontend renderer exhaustive over the existing receipt union.

Relevant sources:

- `travel-agent/backend/home/trips_stack.py` — typed receipt union;
- `travel-app/components/trips/TripsStackCrown.tsx` — only `shape` is explicitly rendered.

### Finding 2 — below-hero invitation duplication

Several standing sections invite the traveler to begin work with Vesper:

- Ask Vesper;
- On the Table;
- Trip Feel;
- Connect;
- create/voice affordances;
- Vesper root itself.

Each has a plausible individual rationale, but `ON THE TABLE` and `TRIP FEEL` have particularly overlapping jobs: both create desire for hypothetical future travel. The former begins with accumulated evidence — real saved places — and is more aligned with the relationship-with-places thesis. The latter is a generic rotating mood choice.

Recommendation: keep a single future-desire section. Treat Trip Feel as a possible input to a Vesper conversation or a conditional variation within the Table, rather than permanent peer furniture.

`CONNECT` similarly duplicates an existing crown affordance when the crowned trip already shows participants and an empty-chair invitation. Its strongest use is a cold, solo, or explicitly collaborative state rather than a permanent generic acquisition card.

### Finding 3 — two generations of Trips Home remain

The ranked stack is canonical, but the root still carries a broad legacy hero cascade (`between`, `urgent`, `live`, `ready`, `returned`, `frequent`, `planning`) for degraded or crownless compatibility. That is sensible while operational evidence is gathered, but it leaves two competing vocabularies in the root:

- 25 stack kinds for the ranked attention model;
- 16 older trip-home card archetypes for per-trip card feeds;
- 8 legacy hero postures.

The older card feed still supplies some active ambient trail material, so this is not dead-code deletion territory. It is, however, a reason to avoid adding new features to both pathways.

The Trips contract also describes `YOUR PEOPLE`, `CONNECT`, and an Atlas bridge as a standing lower-home sequence, while the implementation now states that People and Atlas are dedicated destinations and renders Connect plus contextual trail rows. Decide which direction is current and update the contract; the implementation's narrower trail is the cleaner root composition.

## Vesper Home

### Section inventory

Vesper is intentionally a workbench rather than a feed. Its slots are:

1. situated context label and authored read;
2. up to two grounded facts;
3. one optional urgent seam;
4. one homogeneous selected list band;
5. ghost prompts attached to the composer shelf;
6. the composer.

The list kinds are `sessions`, `route`, `season`, and `here`. They reduce to two visible row families:

- a session row, including optional group facepile and canonical activity;
- a world row, shared by route, season, and here.

This is a good boundary. Route, Season, and Here differ in data but not enough to deserve separate card grammars. An urgent seam suppresses the list rather than becoming another peer card, preserving focus.

### Product implication

Protect this narrow model. A casual plan with friends should first appear as a session row, perhaps with a group facepile and a more specific state. It should not create another occasion-card band competing with sessions, routes, seasons, and here.

The current well is already dense when it carries a read, two facts, and three rows. Memory, provenance, and multiplayer should enrich session copy, proof, and people context here; they should not become standalone Vesper Home cards.

## Places Home

### Contract inventory

Places has the strongest typed boundary:

- maximum four sections;
- emitted section list is the only ordering authority;
- empty sections cannot render;
- at most one conviction section;
- server-owned treatment;
- validated treatment cardinality;
- validated card-kind-to-payload consistency.

The declared section reasons are:

- `gap`, `expiry`, `group_waiting`;
- `nearby_set`, `neighbourhood`, `anniversary`, `unfinished_guide`;
- `friend_activity`, `saved_unvisited`, `changed`, `harvest`;
- `starter`, `guide`, `experiences`, `areas`, `saved`.

Fourteen currently have producers. `saved_unvisited` and `areas` appear to be dormant; area material is currently emitted as `neighbourhood`.

The declared treatments are `conviction`, `single`, `fork`, and `choice`. Only `single` and `choice` are currently emitted by production producers. `fork` and `conviction` are valid, supported future capacity rather than live product behavior.

All nine card kinds have producers:

- `place`
- `angle`
- `friend`
- `memory`
- `notice`
- `prompt`
- `city`
- `experience`
- `area`

They reduce to approximately seven visual families:

- place candidate / lead;
- editorial image card for angle, city, and area;
- experience rail or row;
- friend strip;
- memory row;
- private prompt;
- urgent notice.

This is strong consolidation. The stored Places capture reads as an editorial cover followed by useful place rows, not as nine unrelated component styles.

### Finding 4 — frontend dispatch should be exhaustive by card kind

`PlacesSectionFeed` does not switch on `card.kind`; it checks whichever optional payload is populated and defaults the remaining scalar-only case to the notice/prompt renderer. Backend validation makes this safe for today's kinds, but a future scalar-only kind could silently render as the wrong card family.

Recommendation: dispatch exhaustively on `card.kind`, with a `never` failure for unhandled types. Preserve payload validation, but do not make payload order the frontend's visual routing mechanism.

### Finding 5 — do not mistake declared capacity for live product

The Places taxonomy is deliberately broader than the currently emitted behavior. That is fine, but it should not lead design discussions to assume Conviction, Fork, `SAVE`, `AREAS`, or `SAVED_UNVISITED` are established surfaces. They are mostly contract capacity today.

Before more feature work, decide whether those dormant concepts are near-term planned product or residue. If they are capacity, retain them. If they are no longer part of the intended Places story, retire them deliberately rather than letting future producers revive them accidentally.

## Multiplayer, provenance, ambiance, and artifacts

The ingredients already exist but are fragmented:

| Need | Existing projections |
| --- | --- |
| People | Trips crown facepile / empty chair; Vesper group-session facepile; Trips `people` receipt |
| Provenance | Places `saved_by_friend` relationship marker; friend-activity strip; saved-place grounding |
| Memory | Places memory card; Trips retrospective / homecoming / story kinds; Atlas artifacts |
| Ambiance | Vesper-authored reason and place/area character; Trip Feel selector |

The missing abstraction is not another card. It is a shared projection fragment for people, provenance, group state, privacy-safe explanation, and artifact identity. Without one, every new mechanic will grow its own facepile, source line, and partial explanation.

Ambiance should remain authored context — a reason, occasion promise, or place character — rather than becoming an `AmbianceCard`. Likewise, stamps and artifacts should enrich the existing evidence/memory role rather than becoming a new root section by default.

## Recommended cross-home taxonomy

Standardize four semantic roles while allowing each root to retain its own geometry:

| Role | Examples |
| --- | --- |
| Judgment | Trips crown; Places editorial lead or future conviction; Vesper standfirst |
| Thread | Trips stack row; Vesper session; Places candidate/activity row |
| Evidence | Crown receipt; provenance marker; memory artifact; reading preview |
| Door | Open, settle, ask, share, answer privately |

Each projection can then carry bounded, reusable fragments:

```text
identity
state
authored read
facts / proof
people
provenance
primary destination
bounded action
privacy scope
```

New casual-outing, stamp, friend-suggestion, or ambiance work should normally populate these fragments. It should not automatically introduce a new section or card family.

## Priority order

1. Render all ten Trips crown receipts exhaustively.
2. Resolve the Trips contract drift and continue retiring the legacy path only when dogfood evidence permits.
3. Combine or demote Trip Feel so Trips has one standing future-desire module.
4. Make Places card dispatch exhaustive on `card.kind`.
5. Decide whether dormant Places reasons and treatments are intentional near-term capacity or taxonomy residue.
6. Define shared people/provenance/evidence fragments before implementing the next multiplayer, ambiance, or artifact features.

## Evidence limits

This audit used current source and contracts in both repositories and stored iOS captures for Trips, Vesper, and Places. It did not run a fresh simulator capture, so visual findings describe the latest stored evidence rather than certifying the exact current runtime build.
