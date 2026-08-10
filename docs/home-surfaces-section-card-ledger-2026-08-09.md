---
doc_type: working
status: active
owner: frontend / backend
created: 2026-08-09
expires: 2026-09-08
why_new: Source-derived trace ledger for the currently rendered Places and Trips home-surface sections.
---

# Home surfaces — current section/card ledger

This ledger is derived from the shipped source and generated schema, not from
the external design bundle. It records only sections and card families that
have an implementation path today. A dark type is deliberately not a build
instruction.

## Common authority chain

| Surface | Transport | Pure model | Membership and order | Exposure identity | Evidence |
|---|---|---|---|---|---|
| Trips | `TripsHomeStackProjection` | `utils/tripsHomeSectionPlan.ts` -> `tripsHomeSectionRenderModel.ts` | backend ranked projection; the plan rejects incoherent entries | backend content id + revision, with typed-payload fallback hash | projection fixtures, focused Jest, registered polish flows |
| Places | `PlacesFeed` | `utils/placesPresentationModel.ts` | backend `sections[]`; client never invents a reason | reason + fact key + card IDs + stable payload hash | producer/unit tests, Places feed tests, registered polish flows |

The app consumes generated OpenAPI types in `utils/api/schema.gen.ts`. Neither
surface accepts a backend-provided component name or style bag.

## Trips

| Section | Backend/read source | Frontend renderer/containment | Action owner | State and fixture path |
|---|---|---|---|---|
| Crown | `backend/home/trips_stack.py::project_trips_home_stack`; ranked concierge feed | `TripsStackCrown`; crown containment | typed destination; proposal resolution remains the canonical proposal writer | `ranked` / `empty`; crown, receipt, and rejection fixtures |
| Now | dedicated `live_trip` module in the Trips projection | `TripsNowBand`; module containment | typed trip destination | ready only today; absent is honest absence; module-unavailable is rejected by the plan |
| Countdown | dedicated `imminent_trip` module | `TripsCountdownCard`; module containment | typed trip destination | ready only; no module means no allocated section |
| Conditions | dedicated `weather` module | `TripsConditionsBand`; module containment | typed trip destination | ready only; no cross-trip client join permitted |
| Group | dedicated `group_room` module | group renderer in `TripsHomeBody`; module containment | canonical group-room destination | ready only; roster stays projection-grounded |
| Queue / Also in Play | `queue`, then legacy `rows` fallback | `TripsHomeTable` / views; queue containment | typed destination | entries are rejected when duplicate, crown-overlapping, or module-overlapping |

Trips plan states are `pending`, `empty`, and `ranked`; each render entry is
ready only after identity, role, and content-overlap checks. `unavailable` and
`dark` are recognized vocabulary but have no fabricated card path.

## Places

The backend's `PlacesSectionReason` is the sole section identity. Family
rendering is exhaustively mapped in
`components/places/renderers/placesCardRegistry.ts`; Workspace owns query,
scope, chrome, and viewport integration, while the feed owns family routing.

| Reason / producer | Cards and renderer family | Action owner | Grounding/state |
|---|---|---|---|
| `gap` / `gaps.py` | candidate place cards | itinerary-day handoff | verified open trip window; absent when no qualified gap |
| `expiry`, `group_waiting` / `urgency.py` | notice/prompt | notice/proposal domain owner | bounded urgency facts; no generic acknowledgement writer |
| `nearby_set` / `nearby.py` | candidate place cards | place detail/save handoff | quiet-posture taste-floor result; no conviction claim |
| `neighbourhood` / `section_projection.py::area_section` | editorial area cards | map/area destination | canonical area descendants; qualified total drives count door and note |
| `anniversary` / `anniversary.py` | memory | Atlas/place destination | strongest qualified private memory only |
| `unfinished_guide` / reading page + projection | editorial angle cards | reader destination | approved reading inventory; two angles are a fork, not a ranking claim |
| `friend_activity` / `friends.py` | social | source-authorized destination | passive relationship activity only |
| `changed`, `harvest` / `returns.py` | notice/prompt | notice or private debrief owner | recipient-owned change / ended-trip evidence |
| `starter` / `starter.py` | editorial city cards | canonical city context | starter posture and approved coverage only |
| `guide` / `section_projection.py::guide_section` | editorial angle card | reader destination | approved dossier preview only |
| `experiences` / `section_projection.py::experience_section` | experience rail/stack | experience detail/save handoff | authorized trip scope + temporal overlap |
| `saved` / `section_projection.py::saved_section` | candidate place cards | place detail/save handoff | canonical personal saves, including authorized destination scopes |

`saved_unvisited` has no producer and remains dark. `conviction` is a valid
transport treatment but deliberately has no producer because no grounded,
non-proximity confidence signal exists. Missing, empty, and unavailable are
distinct: unavailable producer names travel in the bounded
`unavailable_producers` envelope; they do not create plausible empty cards.

## Card ownership and containment rules

| Family | Current kinds | Local owner | Outer-spacing owner |
|---|---|---|---|
| Candidate | `place` | candidate renderer family | section feed / plan frame |
| Editorial | `city`, `angle`, `area` | editorial renderer family | section feed / plan frame |
| Experience | `experience` | experience renderer family | section feed / plan frame |
| Memory | `memory` | memory renderer family | section feed / plan frame |
| Social | `friend` | social renderer family | section feed / plan frame |
| Notice/prompt | `notice`, `prompt` | notice/prompt renderer family | section feed / plan frame |

## Required proof before changing an entry

1. Preserve the backend membership/order authority.
2. Preserve the generated-contract discriminator and update the source model
   before regenerating types if a wire change is needed.
3. Prove a rejected, empty, or unavailable entry allocates neither false
   space nor exposure telemetry.
4. Trace a mutation to its existing canonical writer and durable receipt; a
   Places card is a handoff, not an itinerary/proposal/booking writer.
5. Record mock, backend-real, and device evidence separately. A mock
   screenshot is not device acceptance evidence.
