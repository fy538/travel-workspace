---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-08-15
last_updated: 2026-08-15
last_verified: 2026-08-15
expires: 2026-09-14
why_new: Codebase research for two founder kit galleries of the recently revamped Trips Home and Places Workspace surfaces. Follows the native gallery plan: labeled production specimens with existing mock fixtures, not fake fully-loaded homes.
promotes_to: travel-app /dev kit galleries for trips-home and places-workspace, then the design-system hub menu
supersedes: []
related:
  - native-design-gallery-founder-pain-2026-08-15.md
  - native-design-gallery-research-and-direction-2026-08-14.md
  - ../../travel-app/docs/surfaces/trips-home/contract.md
  - ../../travel-app/docs/surfaces/places-workspace/contract.md
  - ../../travel-app/docs/surfaces/discover-home/contract.md
  - ../../travel-app/docs/Task Intake.md
---

# Home-kit galleries — Trips Home and Places Workspace

> **Implemented plan and verification receipt.** The two kits shipped in the
> local app history and were re-reviewed against production truth on 2026-08-15.
> The final corrective commit is `f6f006a5`. Durable rules still belong in the
> surface contracts and native gallery memo, not here.

## Implementation status

Slices C0–C2 are complete:

- `/dev/trips-home-kit` mounts labeled production modules and now shares the
  canonical `TripsHomeFallback` renderer with `TripsHomeBody`;
- `/dev/places-workspace-kit` mounts production card views and section
  treatments from grounded fixtures;
- `/dev/surface-census` records the nested-surface decisions and now shows the
  current private-reflection lifecycle instead of the retired debrief form;
- the shared hub/DevFab menu names Discover honestly and links all three routes;
- the day-map specimen uses a bundled deterministic source, not a Mapbox token
  or network request; and
- `.maestro/polish/native-design-workbench.yaml` captures selected specimens
  from the M1, Trips, Places, and census scrolls.

The two boundaries remain deliberate: the kits prove production leaves and
state coverage; the real Trips and Places tabs prove composition and rhythm.
The Maestro lane is registered but has only been dry-run in this receipt, so it
does not yet provide visual evidence.

## Direct answer

The implementation provides **two labeled family scrolls**, the same object as `/dev/m1-signatures`,
scoped to the two recently revamped homes:

| Route | Object |
| --- | --- |
| `/dev/trips-home-kit` | Every Trips Home module and chrome specimen, using production components |
| `/dev/places-workspace-kit` | Every Places feed card kind and section treatment, using production renderers |

Do **not** mount a fake “fully loaded” Trips or Places page that concatenates
every section as if one traveler owned all of them. Those surfaces are
existence-gated and posture-driven. The real tabs with mock personas remain
the proof of a composed page. The kits are the proof of the kit.

This is **Slice C** of the native gallery plan: after the complete hub
(Slice A) and the M1 signature scroll (Slice B). It is not Storybook, not a
`NativeGalleryEntry` registry, and not Discover.

## Intake

| Question | Answer |
| --- | --- |
| Label | `safe-frontend` (dev galleries) + `founder-only` (new `app/dev` files; route architecture already uses `Stack.Protected`) |
| Domain | Trips Home and Places Workspace visual kits |
| Mock enough? | Yes. Extract cards/modules from existing mock personas and unit fixtures. |
| Contract / routes / context? | Adds two protected `/dev` routes and two hub/DevFab links. Does not change production tab composition. |
| Registered surface? | The kits are grouped under the doctrine-judged `native-design-workbench` dev-fixture surface for capture. Real-tab acceptance remains on `trips-home` / `places-workspace`; a kit capture cannot pass their composed-page rhythm. |
| Docs that go stale | Hub menu note that Discover cold start is “Places empty composition” (wrong today). This working note. |

## 1. Why the real homes are not enough

Trips Home membership comes from `buildTripsHomePagePlan` →
`buildTripsHomePageSectionPlan` → `adaptTripsHomePagePlanForBody` →
`TripsHomeBody`. The body never invents sections.

Places membership comes from `GET /api/places/feed` →
`buildPlacesPresentationModel` → `buildPlacesFeedRenderPlan` →
`PlacesSectionFeed`. Sections are existence-gated by posture and grounded
facts.

Consequence: Elif never shows Mara’s gap/notice kit; Ana never shows Dev’s
memory/prompt kit; a live Carmen home hides On The Table. A founder sitting
on one persona cannot see the kit.

Existing `/dev` coverage is leaf-shaped, not page-kit-shaped:

| Already exists | Covers | Gap |
| --- | --- | --- |
| `/dev/trip-crown-gallery` | Crown receipt matrix | Not Also In Play, D2 modules, trail, chrome |
| `/dev/trip-shape-mood-gallery` | Mood art only | Not the full On The Table section |
| `/dev/m1-signatures` | Crown + non-home M1 objects | Not Trips Home as a kit |
| `/dev/trip-creation-card` | Chat trip-creation artifact | Not Trips Home |
| `/dev/discover-cold-start` | Empty **Discover** cover | Not Places Workspace. Hub copy currently mislabels it “Places empty composition.” |
| Places polish flows | Persona-realistic full pages | Capture evidence, not a browse scroll |

That gap is now closed by `/dev/trips-home-kit` and
`/dev/places-workspace-kit`. The table above remains the historical rationale
for why those routes were added.

## 2. What to build vs what not to build

**Build:** two `/dev` scrolls. Each family is a labeled stage: representative,
one extreme, one absence where the contract already names absence. Production
components. Existing fixtures. NOOP navigation.

**Do not build:**

- A stuffed home that shows every section at once as one product state
- `NativeGalleryEntry`, tags, capture tiers, Storybook
- New product data (gaps, visits, confirmed times, friend activity, conviction)
- Discover cover cards inside the Places kit
- Map canvas, Saved/Reading collection screens, Place/Experience object pages
- Atlas / YOUR PEOPLE (contract-forbidden on Trips root)
- Field Note / READING ROOM (contract prose; not in `TripsHomeBody`)
- Maestro catalogs of 89 modules

New `app/dev` files are allowed here because Slice C is a new increment.
`Stack.Protected` already maps `DEV_STACK_SCREEN_NAMES`. Add the two names
there. That is still not an IPA exclusion proof.

## 3. Trips Home kit — inventory and specimens

Physical order on a crowned page (from the page plan, not a gallery order):

`notices → mast → [now] → crown → [open_loops|countdown|conditions|group] → [queue] → [inline-voice] → standing-ask → [local-plans|day-map] → [companion] → [dreams] → [trip-feel] → trail → footer` + floating create + morph header.

Mount **components**, not `useTripsHomeScreenController`. Gallery-safe types
are the same ones the body already passes.

### 3.1 Include (production families)

| Family | Component | Fixture source | Representative | Extreme | Absence |
| --- | --- | --- | --- | --- | --- |
| Crown | `TripsStackCrown` | `TRIP_CROWN_PREVIEWS` | Lisbon default | Long voice / urgent Porto | No specimen of an empty crown — show starter or unranked fallback instead |
| Now | `TripsNowBand` | D2 test row with `row_line` | Live fact line | Long `row_line` | Blank/null → labeled absent (`isTripsNowRenderable`) |
| Open loops | `TripsOpenLoopsCard` | `__tests__/components/trips/TripsOpenLoopsCard.test.tsx` `planned` | Checklist module | Overflow checklist if the test fixture already has extra rows | Rejected/absent — do not invent a live mock producer; mock `projectDedicatedModules` does not emit `open_loops` today |
| Countdown | `TripsCountdownCard` | D2 / imminent_trip projection | Days-out + line | Do **not** invent pip `days` (body does not pass them) | Missing/past start_date |
| Conditions | `TripsConditionsBand` | Concierge `weather` → `conditions` | Titled weather row | Long title + `row_line` | Missing title |
| Group | `TripsGroupSection` | D2 travelers on the row’s trip | Facepile + title | Many travelers | No travelers |
| Also In Play | `AlsoInPlayCard` | Persona stack `queue` (max 2) | Two calm rows | One needs-you (`tier <= 2`) + depth `· N OPEN` | Empty queue — labeled absent |
| Standing ask | `StandingAskCard` | `TRIPS_HOME_STANDING_ASK_QUESTIONS` | `planning` question | `live` + local-plan door copy | `urgent` hides the card — labeled absent |
| Companion | `TripCompanionCard` | `mockTripReadings['persona-elif-rome']` | Collapsed Lisbon/Rome reading | Expanded section rows | Null reading |
| On The Table | `DreamsInTasteSection` | `TasteCity` from ana-saves / between; mood still in `/dev/trip-shape-mood-gallery` | Sketch + ≤2 seeds | Long place names / many anchors | No saved cities |
| Trail | `TripsHomeTrail` | Connect is static copy | Connect available | `between` Near You **only if** existing `NearYouContext` fixture; live ambient **only if** `AMBIENT_ENABLED` fixture exists | Connect unavailable; Near You suppressed |
| Footer | `TripsFooter` | `count: number` | “See all N trips” | Large N | Zero trips — labeled absent |
| Mast | `TripsHomeStandfirstVoice` | `tripsHomeMast(posture)` | `planning` | `urgent` / `live` | n/a (always voiced when page shows) |
| Morph header | `TripsRootMorphHeader` | Rest vs urgent eyebrow | Rest | Urgent + badge | n/a |
| Loading | `LoadingTrips` | None | Shimmer crown | n/a | n/a |
| Hero fallbacks | inline in `TripsHomeBody` | Copy already in body | Starter door | Unranked / empty projection | These **are** the absence of crown |

### 3.2 Include only if fixtures already exist — do not invent

| Family | Flag | Rule |
| --- | --- | --- |
| Local plans | `LOCAL_PLAN_DOGFOOD_ENABLED` | Use a real local-occasion `TripWithMembers[]` from journey tests if one exists. Otherwise one labeled “flag-dark / no fixture” absence. |
| Today Mapped | `TRIP_EDITORIAL_MAP_ENABLED` | Use `TripEditorialMapCard` from `TripDayMapCard.test.tsx`. If the Mapbox URL builder fails in gallery, show the card chrome and label image absence. |
| Trip Feel | `TRIP_FEEL_STATIC_EXPLORATION_ENABLED` | Authored pairs in `utils/tripFeel.ts` are local-only and gallery-safe. Show default pair + dismissed. Flag-off → absence. |
| Inline voice | `VOICE_ENABLED` | `VoiceAskCard` needs `VoiceOverlayProvider`. If that is heavy, one chrome specimen with the provider already used by DevFab’s host, or skip and keep Standing Ask as the ask door. |

### 3.3 Keep off this kit

- `/dev/trip-creation-card` (chat artifact)
- TableCard/ListRow atom shelf (they appear inside On The Table and Trail)
- Retired `OnTheTable` rail / DraftRow
- Device weather mixed into Conditions (contract forbids)
- Full `TripsHomeBody` controller

### 3.4 Gallery order (founder sitting, not page plan)

1. Chrome: morph header, mast, loading, create mark (static)
2. Hero stack: fallbacks, crown, now, open loops, countdown, conditions, group, also-in-play
3. After hero: standing ask, companion, on the table, trip feel (if flagged), local plans / day map (if fixtures)
4. Trail + footer

Reuse `Section` / `Specimen` from `/dev/m1-signatures` (extract those two
wrappers to `components/dev/galleryStage.tsx` so three scrolls share chrome
without route-to-route imports).

## 4. Places Workspace kit — inventory and specimens

Places Workspace ≠ Discover. Discover is an editorial cover board
(`DiscoverCoverHome`). Places is a posture-driven section feed
(`PlacesWorkspace` → `PlacesSectionFeed` → `PlacesFeedCardView`).

Wire unions (`utils/api/schema.gen.ts`):

```text
PlacesCardKind = place | angle | friend | memory | notice | prompt | city | experience | area
PlacesSectionTreatment = conviction | single | fork | choice
PlacesSectionReason = gap | expiry | group_waiting | nearby_set | neighbourhood
  | anniversary | unfinished_guide | friend_activity | saved_unplaced | changed
  | harvest | starter | guide | experiences | saved | register
PlacesFeed.posture = starter | between | planning | ready | urgent | live | returned | quiet
```

Client layout (not wire): `stack` | `fork` | `rail` | uncarded notice/prompt
rhythm. `conviction` has **no honest mock producer** — schema and client both
treat it as dark. Do not specimen a raised conviction card.

Every production card kind is already reachable across mock personas
(`__tests__/utils/placesProjectionMock.test.ts`):

`angle, area, city, experience, friend, memory, notice, place, prompt`

Extract cards from `tripsApi.getPlacesFeed` with the persona + context handle
the test already uses. Do not hand-author new gap/friend/memory payloads.

### 4.1 Card-kind specimens

| Kind | Renderer | Persona / fixture | Representative | Extreme | Absence |
| --- | --- | --- | --- | --- | --- |
| `place` | `PlaceFeedCard` | Grounded `saved`; Mara `gap` for `add_to_day` | Saved place, `choice` | Mara gap lead + `add_to_day` (Mara fixture only) | Non-openable / missing duration — only if that card already exists |
| `angle` | `AngleFeedCard` | Grounded `guide` (Lisbon 501 / Rome 601) | Single guide | Long preview | Fork of two angles is **tests only** — mount the test fixture, labeled “test fixture, not a persona” |
| `city` | `CityFeedCard` | Ana Anywhere `starter` | 2–4 cities | High `guide_count` kicker | n/a (starter absence is empty Places, below) |
| `area` | `AreaFeedCard` | Grounded neighbourhood | One area | Overflow door (≥5) if grounded set is that large | Temporary area context — labeled absent |
| `experience` | `ExperienceFeedCard` | Lisbon confirmed fado; Rome unconfirmed walks | Rail, confirmed | Unconfirmed `TIME TBC` | Do not invent confirmed times |
| `friend` | `FriendFeedCard` | Mara `mock-dao-consented-save` | Display-only strip | n/a | No press target is the product, not a bug |
| `memory` | `MemoryFeedCard` | Dev returned `mock-anniversary` | Years-ago kicker | Long title | Glyph plate, no photo — that is representative, not absence |
| `notice` | `NoticeOrPromptCard` | Mara expiry + group decision | Expiry hold | Group-waiting proposal handoff | Malformed action → no false handoff (test fixture) |
| `prompt` | same, prompt branch | Dev returned harvest | Debrief prompt | n/a | After debrief submitted — labeled absent |
| register | `PlaceRegisterFeedCard` | **Tests only** today | One test verdict/change/log | n/a | Empty without evidence keys — do not invent a persona producer |

### 4.2 Section chrome and treatments

Mount `PlacesSection` + `PlacesSectionFeed` via the same path production uses:
`buildPlacesPresentationModel` → `buildPlacesFeedRenderPlan`. Do **not** import
`testing/placesSectionFeedHarness.tsx` from `app/dev` (test-only bridge).

| Treatment / layout | How to get it | Notes |
| --- | --- | --- |
| `single` | Most Mara/Dev sections | Default |
| `choice` | Saved, gap, starter, neighbourhood | 2–4 cards |
| `fork` | Angle pair from render-plan tests | Label as test fixture |
| `rail` | Experience section where every card has `experience` | Also show stacked rail at fontScale ≥ 1.35 if cheap |
| Door overflow | Saved / neighbourhood when count > visible | Production door copy |
| `conviction` | — | **Dark.** One labeled “no honest producer” note, no fake raised card |

Section reasons with production mocks: `gap, expiry, group_waiting,
friend_activity, harvest, anniversary, starter, guide, saved, experiences,
neighbourhood`.

Reasons that stay labeled “tests only / no persona”: `nearby_set,
unfinished_guide, saved_unplaced, changed, register`.

### 4.3 Places chrome (root states, not feed cards)

Include as small specimens, not a second Places tab:

| State | Component |
| --- | --- |
| Mast postures | `placesHomeMast` + `RootStandfirstVoice` (`starter`, `planning`, `live`, `returned`, `urgent`) |
| Loading | `PlacesWorkspaceLoading` |
| Empty | `EmptyHero` in `PlacesWorkspace` |
| Unavailable / error / cold-offline | `PlacesWorkspaceStateScreen` |
| Stale/offline/partial | `PlacesFeedNotice` |

Keep off this kit: Mapbox canvas, Saved/Reading collection lists, search
session UI, Place Home / Experience detail, Ask Vesper blocks.

### 4.4 Honesty rules (do not violate)

From `utils/api/mock/placesFeed.ts` and the Places contract:

- Do not invent gaps, timing, visits, or itinerary write targets
- Conviction stays dark until an affinity signal exists
- Friend activity requires the consented Mara fixture
- Unconfirmed experiences stay unconfirmed
- Prompt must not grow inline chips (opens trip-debrief)
- `saved_unplaced` needs dual flags + typed destination — tests only

Implementation pattern: a small `constants/mocks/placesKitFixtures.ts` that
**calls** `getPlacesFeed` / `groundedMockPlacesSections` and picks named cards
by id. It does not clone payload literals.

## 5. Implementation slices

### Slice C0 — shared stage + hub honesty

1. Extract `Section` / `Specimen` from `app/dev/m1-signatures.tsx` into
   `components/dev/galleryStage.tsx`.
2. Fix hub copy: `/dev/discover-cold-start` note becomes “Discover empty
   cover,” not “Places empty composition.”
3. Add group entries (hard-coded, still no schema):

   - Other kits: `Trips Home kit` → `/dev/trips-home-kit`
   - Other kits: `Places Workspace kit` → `/dev/places-workspace-kit`

   Not Demo signatures. These are home kits, not M1 alpha objects.

### Slice C1 — Trips Home kit

New `app/dev/trips-home-kit.tsx`. Add `'dev/trips-home-kit'` to
`DEV_STACK_SCREEN_NAMES`. Smoke test: every listed family `testID` is present;
open-loops / local-plans / day-map may assert the labeled absence if fixtures
are missing.

Providers: `QueryClientProvider` only if a mounted card calls
`useSaveEntity` (Places will). Trips kit should stay props-only.

### Slice C2 — Places Workspace kit

New `app/dev/places-workspace-kit.tsx`. Add `'dev/places-workspace-kit'`.
Smoke test: all nine production card kinds render from extracted mock feed
cards; conviction is a labeled dark note; Discover is not imported.

Wrap with a real `QueryClient` because `PlaceFeedCard` / `ExperienceFeedCard`
call `useSaveEntity`. Navigation callbacks are NOOP. Do not hit itinerary
commit from the gallery.

### Slice C3 — operational follow-ups

- Device walk of real `trips-home` / `places-workspace` polish QA (already a
  registered-surface path)
- IPA / TestFlight exclusion audit (still required before shipping new
  `/dev` files in a store build)
- bounded Storybook/hosted-review experiments only if a measured bottleneck warrants them

The component-registry repair moved into the corrective implementation and is
complete at `f6f006a5`.

## 6. Mounting notes (so the implementer does not rebuild the homes)

**Trips:** import the leaf components listed in §3.1. Hand them the typed
fixtures. `onOpen*` = `() => undefined`. Do not render `TripsHomeBody`.

**Places:** for each named card, wrap `PlacesFeedCardView` with a stub
`PlacesFeedCardViewContext` (`scopeLabel`, `section.reason`, layout flags,
NOOP choose-city/area). For section treatments, build a one-section
`PlacesFeed`, run `buildPlacesPresentationModel` + `buildPlacesFeedRenderPlan`,
render `PlacesSectionFeed`.

**Do not** import `testing/placesSectionFeedHarness.tsx` from app code.

**Feature flags:** gallery screens may force-show a flagged component when a
fixture exists (Trip Feel, Local Plans) and must label the flag. They must
not enable flags globally.

## 7. Exit — achieved in code, pending device evidence

A founder can:

1. Open DevFab → Design system → Other kits → Trips Home kit and see every
   implemented Trips module without switching personas.
2. Open Places Workspace kit and see every production card kind plus honest
   section treatments, without a fake all-sections traveler.
3. Still use the real Trips and Places tabs (Elif, Mara, Ana, Dev) to judge
   composed-page rhythm.

That is “see all the cards we implemented.” It is not “one person has
everything.”

The code and structural-test exit is complete at app commit `f6f006a5`.
Remaining operational proof is one real `native-design-workbench` Maestro run,
skeptical screenshot inspection, and an external-build/deep-link audit. The
explicit preview/production internal-build flags and recursive protection test
are fail-closed safeguards; they are not a claim that route files are absent
from the release binary.
