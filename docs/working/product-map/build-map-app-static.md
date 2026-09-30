---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: Evidence-based static map of what the mobile app actually builds (live, flagged, not built, legacy) at the merged Sep 26 baseline, to replace rough progress estimates in the product map.
promotes_to: null
supersedes: []
---

# Vesper mobile app — static build map (app `main` 43225df35)

This is a read-only static inventory of `travel-app`. It verifies and updates the 2026-09-25 inventory, which was taken at app `main` 23cff76f4, before the recovery PR merged.

## Evidence boundary

**Revisions read**
- **Baseline:** `/Users/feihuyan/travel-workspace--product-map-inventory/travel-app`, branch `codex/product-map-inventory`, which equals `origin/main` **43225df35** ("Merge pull request #201 … home-human-opening-recovery").
  - That merge brought in 43 commits: 247 files, +6,696 / −5,504.
- **Backend:** only spot-read, at `travel-agent` c8c9f5785 (the matching merge #233).
- **Codex lane:** `/Users/feihuyan/travel-workspace--home-value-delivery/travel-app`, branch `codex/home-value-delivery`, HEAD aa3e235d6 (it advanced from 48ee7ba88 while I was reading). Read only (section 6).

**What was executed.** All of these ran with node v24.13.0 against the baseline checkout, using the `node_modules` already present there. I installed and built nothing. All exited 0.
- `node scripts/check-size-budgets.mjs`
- `check-home-surface-budgets`
- `check-color-budget`
- `check-typography-budget`
- `check-spacing-budget`
- `check-local-button-budget`
- `check-component-lifecycle`
- `check-containment-budget`
- `check-muteSoft-budget`
- `check-border-radius-budget`
- `check-shadow-budget`
- `check-release-config`
- `check-surface-contraction`

**What was not run.** Jest, Maestro, typecheck, any device or simulator, and any backend.

**What cannot be seen from here.**
- EAS dashboard environment values (for example the production Clerk `pk_live` and Mapbox tokens).
- Fly secrets.
- Production data.

"Live" below means *on in the production/preview build configuration*. It does not mean real users have it: there is still no public release.

**Method for counts**
- Route and caller counts are grep- and import-graph-based.
- Dead-code detection is a static relative-import reachability walk from every `app/` route file. This app uses no path aliases (`tsconfig.json` extends `expo/tsconfig.base` only).
- Test counts are filename or content keyword matches. They are approximate by construction and say nothing about test quality.

---

## 0. One-screen summary

- **Every build profile resolves to posture `legacy`.**
  - The visible tabs are **Plans, Vesper, Places, Life**.
  - The four-root product (**Home, Chat, Places, Life**, with governed projections) is reachable only in an internal or dev binary started with four EXPO_PUBLIC flags set by process override. No `eas.json` profile sets them.
  - `releaseEligible` is hard-coded `false` (`utils/productSystemRollout.ts:69`).
- **Always-live new-product pieces.**
  - The **Life** root (`LifeRootV1Screen`) is live and unflagged in every build.
  - The unflagged share-sheet **intake** (`/share-capture`) is live.
- **New-product pieces that exist only in the internal governed rehearsal:**
  - Home (crown, 7 postures, 4 regions, 20 renderable kinds, human Place notes, received originals)
  - Places World Field and mixed order
  - The object-page rebuild (Keep / Tonight? / Ask Vesper / Read up / Leave for someone)
- **Legacy that the new vision retires is still live by default:**
  - trip-first Plans home
  - booking screens
  - vote widgets
  - Vesper as group-room facilitator
  - the public follow graph
  - Atlas and Discover redirects and orphan readers
- **Code volume.**
  - The app has about 433k LOC of TS/TSX outside `__tests__`: app 57.6k, components 151.6k, utils 145.0k, hooks 29.2k, constants 28.6k, data 17.5k, context 3.6k.
  - Tests add about 192k LOC.
  - 83 modules (about 11.9k LOC) are unreachable from any route. Another 65 modules (about 15.7k LOC) are reachable only from `app/dev/*`.
- **Codex lane (`codex/home-value-delivery`).** 17 commits, 57 files. They are Home polish, received-original fidelity and a Source-result round trip, all inside the governed rehearsal. No flag or profile change. The lane does pin **native dependency versions down**: `react-native-reanimated` 4.6.0 → 4.2.1 and `react-native-worklets` 0.12.1 → 0.7.4.

---

## 1. Build posture

### 1.1 How the shell resolves

**`utils/productSystemRollout.ts:36-73` — `resolveProductSystemRollout`**
- `shellEnabled` = `EXPO_PUBLIC_FOUR_ROOT_SHELL=true` AND (`__DEV__` OR `EXPO_PUBLIC_IS_INTERNAL_BUILD=true`).
- `governed_rehearsal` = shell AND internal build AND `EXPO_PUBLIC_ROOT_PROJECTION_V2` AND `EXPO_PUBLIC_PLACES_ROOT_V2_RENDERER` AND `EXPO_PUBLIC_LIFE_ROOT_V1`.
- Anything less, with the shell on, gives `compatibility`. Shell off gives `legacy`.
- `releaseEligible: false` always.

**`utils/fourRootShell.ts`** sets the tab titles:
- Shell on: Home / Chat / Places, with `lifeVisible` true.
- Shell off: Plans / Vesper / Places.
- `app/(tabs)/_layout.tsx:117-123` hard-codes the Life tab (`href: undefined`, title "Life"), so Life is visible in every posture. `lifeVisible` has no consumer.

**Route switches (four in total):**
- `app/(tabs)/trips/index.tsx:7` — `FOUR_ROOT_SHELL.enabled ? <HomeRootExperience/> : <TripsHomeBody …/>`
- `app/(tabs)/places/index.tsx:7` — `PlacesRootExperience` or `PlacesWorkspace`
- `components/home-root/HomeRootExperience.tsx:60` and `data/rootProjections.ts:215/274/321` — `ROOT_PROJECTION_V2.enabled`, which equals `homeGovernedProjectionEnabled`
- `components/places/PlacesRootExperience.tsx:75-76` — `ROOT_PROJECTION_V2.enabled && PLACES_ROOT_V2_RENDERER_ENABLED`

**How the flags actually get set.** The Home surface contract (`docs/surfaces/home-root/contract.md:214-221`) tells rehearsers to start the development bundle with all five flags (FOUR_ROOT_SHELL, ROOT_PROJECTION_V2, PLACES_ROOT_V2_RENDERER, LIFE_ROOT_V1, IS_INTERNAL_BUILD) as **process overrides**, not committed defaults.
- In the repo, only `scripts/polish-qa/surfaces.mjs:368` names `EXPO_PUBLIC_FOUR_ROOT_SHELL`, as a capture precondition.
- No `.env` in the canonical checkout or either lane sets any four-root flag. The canonical `travel-app/.env` sets only `USE_MOCK_API=false`, `SKIP_AUTH=false`, `API_URL` and `IS_INTERNAL_BUILD=true`.

**`LIFE_ROOT_V1` is only a rollout gate now.**
- `utils/lifeRootFlag.ts` `LIFE_ROOT_V1_ENABLED` has two consumers: the dead `AtlasIndex` function (`app/(tabs)/atlas/index.tsx:84`) and `app/dev/home-places-rehearsal.tsx`.
- The Life tab renders `LifeRootV1Screen` unconditionally (`app/(tabs)/life/index.tsx`).

### 1.2 Build profiles (`eas.json`)

| Profile | Internal | API | Auth | Feature env set | Posture |
|---|---|---|---|---|---|
| `e2e-test` | true | **mock** | skip | LOCAL_PLAN, OUTCOME_ARTIFACT, DEPTH_ENCOUNTER, GROUP_TRIP_MICRO_JOURNEY | legacy |
| `development` (dev client) | true | **mock** | skip | GROUP_TRIP_MICRO_JOURNEY | legacy. `__DEV__` means a local override of FOUR_ROOT_SHELL alone gives *compatibility*. |
| `dogfood` | true | fly (`vesper-backend.fly.dev`) | Clerk `pk_test` | LOCAL_PLAN, OUTCOME_ARTIFACT, DEPTH_ENCOUNTER, GROUP_TRIP_MICRO_JOURNEY, TRIP_EDITORIAL_MAP, TRIPS_NEAR_YOU, TRIP_FEEL_STATIC, PLACES_READING_SPINE, PLACES_SAVED_UNPLACED, **VOICE_ENABLED=true**, AI_IMAGE_FALLBACK=false, CRASH_CONSENT=false | legacy |
| `m1-dogfood` (extends dogfood) | true | fly | pk_test | keeps LOCAL_PLAN, OUTCOME_ARTIFACT, GROUP_TRIP_MICRO_JOURNEY. Sets **false**: DEPTH_ENCOUNTER, EDITORIAL_MAP, NEAR_YOU, TRIP_FEEL, READING_SPINE, SAVED_UNPLACED, VOICE | legacy |
| `billing-sandbox` (extends dogfood) | true | fly | pk_test | + REVENUECAT_ENABLED, TEST_STORE, PLACEMENTS, `COMMERCIAL_PAYWALL_MODE=internal` | legacy |
| `preview` | **false** | fly | pk_test | VOICE false, RevenueCat off, paywall off | legacy |
| `production` | **false** | fly | Clerk key from EAS env | VOICE false, RevenueCat off, paywall off | legacy |

**Production guards in `app.config.js:162-191`:** the config throws unless all of the following hold:
- the Clerk key starts with `pk_live_`
- `EXPO_PUBLIC_MAPBOX_TOKEN` starts with `pk.`
- `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` is present
- voice and dictation are off

These values live in the EAS environment and are not visible here. `node scripts/check-release-config.mjs` passes.

**`app/_layout.tsx:168-197`** fails closed if a non-dev, non-internal binary has mock mode or skip-auth set.

### 1.3 Every `EXPO_PUBLIC_*` name referenced by non-test source or `eas.json` (48)

"Registry" means `docs/flags/registry.yaml` in the baseline workspace (6ef3dca).

#### Rollout flags

| Flag | Default | Read at | Gates | Profiles that set it | Registry expiry |
|---|---|---|---|---|---|
| FOUR_ROOT_SHELL | false | `productSystemRollout.ts:76` | Home and Chat titles; Home and Places root swap | none | **2026-09-28** |
| ROOT_PROJECTION_V2 | false | `productSystemRollout.ts:78` | governed v2 Home/Places reads | none | **2026-09-28** |
| PLACES_ROOT_V2_RENDERER | false | `productSystemRollout.ts:81` | governed Places runtime (World Field) | none | 2026-10-01 |
| LIFE_ROOT_V1 | false | `productSystemRollout.ts:84`, `lifeRootFlag.ts:5` | rollout gate only (Life tab is unconditional) | none | 2026-10-30. Note is stale: it says Life "uses the reversible Atlas compatibility owner". |
| IS_INTERNAL_BUILD | false | `featureFlags.ts:23`, `_layout.tsx:114`, `galleryMenu.ts:335`, `lifeRootFlag`, `lifeRefindFlag`, billing, ErrorBoundary, DevFab, QueryHealthOverlay, `useActivePersonaHydration` | every internal-gated flag; `/dev/*` routes (`Stack.Protected`); DevFab; error alerts | e2e, development, dogfood, m1, billing | not registered (it is a build class) |

#### Plans, Places, Life, Chat and Social flags

| Flag | Default | Read at | Gates | Profiles that set it | Registry expiry |
|---|---|---|---|---|---|
| LOCAL_PLAN_DOGFOOD_ENABLED | false | `featureFlags.ts:30` | `LocalPlanScreen` (`plan.tsx:178-188`); local-plan chooser on Plans | e2e, dogfood, m1 | 2026-10-30 |
| TRIP_EDITORIAL_MAP_ENABLED | false | `:41` | "Today Mapped" `TripDayMapCard` | dogfood | 2026-10-30 |
| TRIPS_NEAR_YOU_DOGFOOD_ENABLED | false | `:52` | foreground Near You on Plans | dogfood | 2026-10-30 |
| PLACES_READING_SPINE_ENABLED | false | `:64` | Places reading-spine treatment | dogfood | 2026-10-30 |
| ADAPTIVE_PLACES_ORIENT_SHADOW_ENABLED | false | `:77` | shadow-only comparator on `places/map.tsx:189` | none | **2026-09-28** |
| DEPTH_ENCOUNTER_ENABLED | false | `:87` | dossier-to-Vesper encounter; the LOOP also needs OUTCOME_ARTIFACT | e2e, dogfood | 2026-10-30 |
| OUTCOME_ARTIFACT_ENABLED | false | `:99, :158` | post-occasion artifact (`plan.tsx:642`) | e2e, dogfood, m1 | 2026-10-30 |
| PLACES_SAVED_UNPLACED_ENABLED | false | `:110` | Places saved-unplaced section. The backend producer is also dark by default. | dogfood | 2026-10-30 |
| TRIP_FEEL_STATIC_EXPLORATION_ENABLED | false | `:121` | Trip Feel section | dogfood | 2026-10-30 |
| GROUP_TRIP_MICRO_JOURNEY_ENABLED | false | `:134` | "take somewhere" live doorway (`plan.tsx:1026`) | e2e, development, dogfood, m1 | 2026-10-07 |
| PLAN_SHAPE_ENABLED | false | `:140` | `CurrentShapeSurface` (`plan.tsx:538-544`) | **none** | 2026-10-30 |
| OBJECT_PAGE_REBUILD_ENABLED | false | `:176` | `ObjectPageRebuild` for venue, site and experience | **none** | 2026-10-07 |
| ENTITY_RESEARCH_REQUESTS_ENABLED | false | `:184` | "Read up" on the rebuild page | **none** | 2026-10-07 (backend entry) |
| RELATIONSHIP_UUID_HANDOFFS_ENABLED | false | `:193` | original sender; PeopleLine on the rebuild page; life-find "Shared with you" | **none** | **App half not registered.** The backend entry expires 2026-10-30. |
| LIFE_REFIND_LANE | false | `lifeRefindFlag.ts:12` | Life search goes to `/you/life-find` instead of universal search | none | 2026-11-30 |

#### Voice, chat and other feature flags

| Flag | Default | Read at | Gates | Profiles that set it | Registry expiry |
|---|---|---|---|---|---|
| VOICE_ENABLED / VOICE_AGENT_ENABLED | false | `voiceEnabled.ts:20`; `app.config.js:104` | LiveKit voice; mic; mic Info.plist string | dogfood only | 2026-10-04 |
| COMPOSER_DICTATION_ENABLED | false | `voiceEnabled.ts:24`; `app.config.js:107` | **No UI consumer.** Only the Info.plist injection reads it. | none | not registered |
| CHAT_STREAM_PRESENTATION_V2 | **true** | `utils/chat/streamPresentationFlag.ts:8` | buffered stream smoothing in concierge and group chat | none (default on) | not registered |
| CONTENT_GRAPH_GEOFENCE | false | `utils/api/index.ts:39` | **Exported, with no consumer** | none | backend entry only |
| LIVE_BOOKING_ENABLED | false | `booking/[sessionId].tsx:1370` | "AI books directly" label | none | 2026-10-04 |
| AI_IMAGE_FALLBACK | — | **No source reader** (only a test) | nothing | dogfood, preview, prod = "false" | not registered |

#### Billing flags

| Flag | Default | Read at | Gates | Profiles that set it | Registry expiry |
|---|---|---|---|---|---|
| REVENUECAT_ENABLED, _TEST_STORE_ENABLED, _PLACEMENTS_ENABLED, _IOS/ANDROID/TEST_STORE_API_KEY, _OFFERING_ID | off | `billing/revenueCatConfig.ts`, `upgradeConfig.ts` | RevenueCat SDK, paywall placements | billing-sandbox on; preview and prod explicit off | not registered |
| COMMERCIAL_PAYWALL_MODE | off | `billing/upgradeConfig.ts:23` | paywall ("internal" needs an internal build) | billing = internal; preview and prod = off | not registered |

#### Environment and infrastructure values (not feature flags)

| Name | Default | Read at | Gates | Profiles that set it |
|---|---|---|---|---|
| USE_MOCK_API | true (`.env.example`) | `utils/api` | in-memory mock API | e2e, dev = true; others false |
| SKIP_AUTH | per `.env.example` | `utils/api` | bypasses Clerk | e2e, dev = true |
| API_URL | localhost:8000 | `utils/api` | backend origin | dogfood, preview, prod = fly |
| APP_CHANNEL | — | DevFab, MockModeBanner | dev chrome labels | all |
| CLERK_PUBLISHABLE_KEY | — | `_layout.tsx:164`, `app.config.js:163` | auth | dogfood and preview use pk_test; prod comes from EAS env |
| SENTRY_DSN, CRASH_REPORTING_CONSENT | off | `_layout.tsx:464-468` | crash reporting | consent false everywhere |
| MAPBOX_TOKEN, MAPBOX_STYLE_URL | — | `nativeMapbox.ts`, `constants/mapbox.ts`, `shareMapUrl`, `editorialMapImageUrl` | maps | EAS env |
| ADMIN_API_TOKEN | — | `utils/api/opsStatus.ts` | DevFab ops panel | none |
| DOGFOOD_JWT | — | `utils/api/tokenStore.ts:49` | static dogfood token | none |
| MOCK_FAULTS, MOCK_LATENCY_MS | — | `utils/api/mock/helpers.ts` | mock-only | none |

#### Hard-coded constants (not environment)

| Constant | Value | Where | Consumer | Registry expiry |
|---|---|---|---|---|
| `POSTCARDS_ENABLED` | false | `featureFlags.ts:17` | `atlas/artifact/[id].tsx:266` | 10-04 |
| `AMBIENT_ENABLED` | false | `featureFlags.ts:20` | Trips home | 10-04 |
| `STORY_SHARE_ENABLED` | false | `featureFlags.ts:166` | — | 10-04 |
| `DOSSIER_VOICE_STUB` | false | `featureFlags.ts:197` | `dossier/[dossierId].tsx:458` | 10-04 |
| `AUTH_PHONE_ENABLED` | true | `featureFlags.ts` | auth | 10-11 |

#### Registry drift

- `PLACES_SECTIONS_FEED_ENABLED` is registered as `constants/featureFlags.ts:25`, default true, expiring 2026-10-30. **No such flag exists in the app.**
- `EXPO_PUBLIC_LIFE_ROOT_V1`'s note still describes an Atlas compatibility Life tab.
- Three client flags expire in two days (2026-09-28) with their promotion questions unresolved: FOUR_ROOT_SHELL, ROOT_PROJECTION_V2, ADAPTIVE shadow.

### 1.4 What each build actually shows

#### Production and preview (not internal)

**Tabs:** Plans / Vesper / Places / Life. Discover and Atlas are `href:null` redirect tabs.

**Plans.** `TripsHomeBody` is fed by the server stack (`backend/home/trips_stack.py`). It shows:
- NOW band, crown, open loops, countdown, conditions, group room, "also in play" queue
- standing ask
- ON THE TABLE (saved venues)
- CONNECT
- "See all N trips"

**Vesper.** `VesperWorkbench` (read line, ≤2 facts, one well) plus a docked `ComposerBar`. The composer offers photo library, camera and "Start together" (`app/(tabs)/concierge/index.tsx:186`).

**Places.** `PlacesWorkspace` backed by `GET /api/places/feed`, plus map, saved, reading and inline corpus search. Place pages use the legacy renderers.

**Life.** `LifeRootV1Screen` from `GET /api/root-projections/v1/life`, with four lenses: Time, Places, Threads, People.

**Everywhere:**
- the share-sheet intake
- the notifications inbox
- onboarding (ambient or trip fork, then Clerk)
- You portrait and settings
- the people / circles / follow screen
- the public profile with Follow
- trip invites
- booking screens (reachable)
- vote widgets
- Vesper as an @-mention facilitator in trip group chat

**Hidden or absent:**
- dev tools and routes
- voice
- paywall
- every internal flag above

#### Dogfood (internal, legacy posture)

Everything in production, plus:
- LocalPlan (Friday-night loop)
- outcome artifact
- depth encounter
- group-trip micro-journey
- Today Mapped
- Near You
- Trip Feel
- Places reading spine
- saved-unplaced, which is client-on but backend-dark unless a secret sets it
- **voice**
- the dev FAB, QueryHealthOverlay and JS error alerts
- all 36 `/dev/*` routes, including `home-root-preview`, `four-root-portfolio`, `instruments-gallery`, `occasion-crown-gallery`, `home-places-rehearsal` and `persona-switcher`

`m1-dogfood` drops the exploratory set and voice.

**Dogfood still does not show:** four-root Home, governed Places, the object-page rebuild, people lines, original or place-note send and receive, Plan Shape, Read up, or Life refind.

#### Internal binary with process-override flags

**With `FOUR_ROOT_SHELL` only (compatibility):**
- The tabs become **Home / Chat / Places / Life**.
- Home renders v1 `HomeRootScreen`: WorldRead, WeekShape and four regions of `SemanticResultRenderer`, from `GET /api/root-projections/home`.
- Places renders `PlacesRootExperience` over the v1 envelope (`/api/root-projections/places`).
- Chat is the same `VesperWorkbench` screen, renamed.

**With all five flags (`governed_rehearsal`):**
- Home renders `HomeRootV2Screen` from `GET /api/root-projections/v2/home?timezone=`, with:
  - world read
  - a crown in CardSurface
  - WeekShape
  - regions now / in_motion / horizons / continuity with benefit labels
  - the degradation notice, which comes after value
  - RestClose
- Places renders the governed runtime `GET /api/root-projections/v2/places/runtime`: World Field units interleaved with whole sections by `placesPageRenderItems`.
- Home-depth Places routes (`/(tabs)/trips/places*`) and `/source-contribution/[id]` become reachable.

**Additionally with `RELATIONSHIP_UUID_HANDOFFS` (app flag plus the backend flag):**
- received originals and addressed Place notes on Home
- joined human / Place openings
- the original sender on intake submissions
- life-find "Shared with you"
- PeopleLine on the rebuild page

---

## 2. Route inventory (198 route paths from 209 files; 11 `_layout` files)

**Classification legend**
- **NEW** — four-root or redesign product.
- **KEEP** — legacy that survives into the new vision (possibly reshaped).
- **RETIRE** — legacy the vision retires or contradicts: booking, voting, follow, Vesper facilitator, Atlas/Discover remnants, trip-first home.
- **DEV** — dev or QA only.

"Callers" means non-test files that call the `routes.*` builder or push the path string.

### 2.1 Home

| Path | Screen | Reached from | Gate | Class |
|---|---|---|---|---|
| `/(tabs)/trips` | `TripsHomeBody` + `useTripsHomeScreenController` | Tab 1 ("Plans"); `/` redirect; many `routes.trips()` | Default | **RETIRE** (trip-first home). Keep its data owners. |
| `/(tabs)/trips` | `HomeRootExperience` → `HomeRootV2Screen` or `HomeRootScreen` | Tab 1 ("Home") | FOUR_ROOT_SHELL (+ V2 flags) | **NEW** (internal) |
| `/(tabs)/trips/places`, `/map`, `/reading`, `/saved` | `PlacesRootExperience` / `PlacesMapExperience` / `PlacesCollectionScreen` (`routeFamily="home-depth"`) | Only `utils/placesRouteFamily.ts`, driven by Home v2 destinations | four-root only in practice | **NEW** (internal) |
| `/source-contribution/[workflowId]` | `SourceContributionResultScreen` | `HomeRootExperience` "source.inspect"; `usePlacesSemanticNavigation` | governed only; the backend worker is dark | **NEW** (internal) |

### 2.2 Chat / Vesper

| Path | Screen | Reached from | Gate | Class |
|---|---|---|---|---|
| `/(tabs)/concierge` | `VesperWorkbench` + docked `ComposerBar` | Tab 2 ("Vesper" / "Chat") | — | **KEEP** (to be reshaped to the Chat direction) |
| `/(tabs)/concierge/chat` | `ConciergeChatScreen` (994 LOC; function 817 lines under an 872-line budget exception) | workbench, history, every "Ask Vesper", standing asks | — | **KEEP** (direction-B gaps: §3.6) |
| `/(tabs)/concierge/history` | Conversations list | workbench header | — | KEEP |
| `/conversations/create` | private / privateTrip / group create; "Create shared room" | "Start together", history empty state, standing asks (5 callers) | — | KEEP |
| `/conversations/[id]/info` | Room info, "Vesper in this room" agency controls, invites | chat header | — | KEEP (room); agency is facilitator UI, so review it |
| `/(tabs)/trips/[tripId]/chat` | `GroupChatRoom` (1,908 LOC): `@Vesper` summons, VoteWidgetCard, booking cards, planning actions | Plan header, Plans group band, notifications (5 builders) | — | **RETIRE** the facilitator, vote and booking parts. KEEP the human room. |

### 2.3 Places root and browse

| Path | Screen | Reached from | Gate | Class |
|---|---|---|---|---|
| `/(tabs)/places` | `PlacesWorkspace` (765 LOC) | Tab 3 | default | KEEP (live Places) |
| `/(tabs)/places` | `PlacesRootExperience` | Tab 3 | FOUR_ROOT_SHELL (+ V2 for World Field) | **NEW** (internal) |
| `/(tabs)/places/map` | `PlacesMapExperience` (955 LOC) | nearby count door; `routes.placesMap` (2 callers) | — | KEEP (pocket/map) |
| `/(tabs)/places/saved`, `/reading` | `PlacesCollectionScreen` | count doors; You portrait | — | KEEP |
| `/(tabs)/discover` | Redirect to Places (passes placeSlug/placeName, **which the root ignores**) | old links, notifications | `href:null` | **RETIRE** (compat redirect) |
| `/your-map` | Redirect to Places | `routes.yourMap` (0 callers) | — | RETIRE |
| `/search` | Universal search overlay | 11 callers (Plans, Vesper, Life headers…) | — | KEEP |
| `/guide/[slug]` | Editorial collection reader (511 LOC) | **No live caller.** `routeForDiscoverTarget` is test-only. | — | **RETIRE** (Discover remnant; deep-link-only orphan) |
| `/dossier/[dossierId]` | Dossier reader (877 LOC) | Places ANGLE cards; 8 callers | DEPTH_ENCOUNTER (dogfood) for the encounter | KEEP |
| `/place/[placeSlug]` | Place home for a city or neighbourhood (1,209 LOC; `PlaceHomeScreen` is 799 lines) | Places AREA cards, venue neighbourhood link; 12 callers | — | KEEP |

### 2.4 Place and entity pages

| Path | Default renderer | Rebuild renderer | Gate | Class |
|---|---|---|---|---|
| `/venue/[venueId]` (2,018 LOC) | Legacy "Vesper Places" page (`VenueCompatibilityContent`): Save/Share/Bring photo, SpotTake, SpotPlanningRail (Add to trip / Reserve / Ask), facts, dossier, details, map, AskVesperBlock, **ungated `RelationshipPlaceNoteAction` (line 1765)**, neighbourhood, similar | `ObjectPageRebuild` | OBJECT_PAGE_REBUILD, or an exact reading or handoff param | KEEP (default) / **NEW** (rebuild, internal) |
| `/site/[siteId]` (307) | `EntityObjectPage` (313): Take, WhyThis, PracticalVisitCheck, map | `ObjectPageRebuild` | same | KEEP / NEW |
| `/experience/[experienceId]` (351) | `ExperienceDetail` (908) | `ObjectPageRebuild` | same | KEEP / NEW |
| `/accommodation/[accommodationId]` (895) | legacy stay detail | `ObjectPageRebuild`, only for an exact reading or handoff (no OBJECT_PAGE_REBUILD branch) | — | KEEP |
| `/public/venue/[venueId]`, `/public/place/[placeSlug]` | External share shell | Share on the venue and place pages (URLs use the `travelagent.app` apex, which is not an app-link host) | — | KEEP (external handoff); the link host is broken |
| `/(tabs)/trips/[tripId]/object/[kind]/[objectId]` (1,044) | Itinerary object page | — | — | See Plans |

### 2.5 Life

| Path | Screen | Reached from | Gate | Class |
|---|---|---|---|---|
| `/(tabs)/life` | `LifeRootV1Screen` (304) | Tab 4 | **none (every build)** | **NEW** (live) |
| `/you/life-record` (684) | Full paginated record by lens | Life archive icon and scroll door; plan screen; graph destinations | — | NEW (live) |
| `/you/life-groups` (197) | Organized groups | Life albums icon | — | NEW (live; likely empty) |
| `/you/life-find` (221) | Original-metadata refind + "Shared with you" | Life search icon only when LIFE_REFIND_LANE is on | LIFE_REFIND_LANE (+ RELATIONSHIP_UUID for "Shared") | NEW (internal) |
| `/you/intake-submissions/[id]` (842) | Private source reader + send-original | Life source rows, Home and Places source doors | send is gated by RELATIONSHIP_UUID | NEW (reader live; send internal) |
| `/you/memories/artifacts/[id]` (113) | Anchor / artifact reader | Life anchor rows | — | NEW (live) |
| `/original-delivery/[deliveryId]` (172) | Received exact original | Home unit, life-find, `resourceDestination` | backend `RELATIONSHIP_UUID_HANDOFFS` (404 otherwise) | NEW (internal) |
| `/you/history` | `LifeRecordScreen` when `?record=`, otherwise the legacy Long View | notifications (`atlasLongView`, 5 callers), `you/atlas/timeline` | — | KEEP for the record; **RETIRE** the Long View branch |

**Atlas remnants** (all **RETIRE** candidates):

| Path | What it is | How it is reached | Class |
|---|---|---|---|
| `/(tabs)/atlas` | Redirect to Life. The named `AtlasIndex` export (670-LOC file) is imported only by a test. | hidden tab | RETIRE |
| `/atlas/account`, `/companions`, `/constraints`, `/data-receipt`, `/delegation`, `/feedback`, `/notifications`, `/phone`, `/privacy`, `/profile`, `/voice-logs` | 11 one-line redirects to You routes | old links | RETIRE (compat) |
| `/atlas/artifact/[id]` (822) | Legacy artifact reader. Hosts the hard-false `POSTCARDS_ENABLED`. | `routes.atlasArtifact` (5 callers, incl. notifications, Places memory cards) | RETIRE (after reader migration) |
| `/atlas/candidate/[id]` (724), `/atlas/inbox` (259), `/atlas/compose` (306), `/atlas/scan` (666), `/atlas/memory` (799), `/atlas/removed` (309), `/atlas/readings` (539) and `readings/[id]` | Legacy memory review, compose and scan; "what Vesper knows"; readings | Via the `/you/memories/*` and `/you/memory` re-exports, notifications, onboarding diary scan | KEEP `memory` and `removed` (trust controls); **RETIRE** inbox, compose and candidate once intake replaces them |
| `/atlas/long-view` (720) | Legacy long view | `/you/history` fallback | RETIRE |
| `/atlas/unpacked` (389), `/unpacked-card` (316), `/shared-links` (197) | Year recap (Unpacked); share hidden | notifications (`atlasUnpacked`), `/you/history/recap*` | RETIRE or park (story share is off) |
| `/atlas/saved-places` (267) | Legacy saved list | **No caller** (`atlasSavedPlaces` maps to `/places/saved`) | RETIRE (orphan) |
| `/atlas/narration-history` (110) | Narration log | **No caller** (`narrationHistory()` maps to `/you`) | RETIRE (orphan) |
| `/atlas/whole` (60) | Legacy | `atlasWhole` → `/you` | RETIRE |
| `/you/atlas/*` (16 files) | Redirects | old links | RETIRE |
| `/you/memories`, `/you/memories/{[id],compose,inbox,readings,readings/[id],review/[id],scan}` | Redirect / re-exports of `app/atlas/*` | — | follows the atlas disposition |
| `/you/history/{recap,recap-card,shared-links}` | Re-exports of atlas unpacked | — | follows the atlas disposition |
| `/unpacked/[token]` (32) | Public sign-in handoff for Unpacked | web link | RETIRE with Unpacked |

### 2.6 Plans / Trips

| Path | Screen | Reached from | Class |
|---|---|---|---|
| `/(tabs)/trips/all` (294) | All trips | "See all N trips" | KEEP (Plans list) |
| `/(tabs)/trips/[tripId]` | Redirect to plan | — | compat |
| `/(tabs)/trips/[tripId]/plan` (2,139) | `TravelPlanScreen`: day rail, list/map faces, `PlanStopInspectSheet` (Ask, **Send proposal**), `ItineraryOperationSheet`, review panel. Also `LocalPlanScreen` (LOCAL_PLAN), `CurrentShapeSurface` (PLAN_SHAPE), outcome artifact (OUTCOME_ARTIFACT). | trip doors everywhere | **KEEP** (itinerary) / NEW (Shape and Local are internal or dogfood) |
| `/(tabs)/trips/[tripId]/map`, `/memory` | Redirects to plan | — | compat |
| `/(tabs)/trips/[tripId]/chat` | Group room | see §2.2 | mixed |
| `/(tabs)/trips/[tripId]/changes` (331) | Operation ledger + undo | Details > History | KEEP |
| `/(tabs)/trips/[tripId]/details` (227) and `details/[section]` (326) | Details index; people, transport and **bookings** sections | Plan header | KEEP (the bookings section is RETIRE) |
| `/(tabs)/trips/[tripId]/object/[kind]/[objectId]` (1,044) | Itinerary object page (organizer attendance invite via the OS share sheet) | plan stops | KEEP |
| `/(tabs)/trips/[tripId]/reading` (301) | Trip reading | Plans companion (`tripReading`, 1 caller) | KEEP |
| `/(tabs)/trips/[tripId]/story` (939) | Trip story (share off) | You portrait, notifications | KEEP (outcome artifact) |
| `/trip-begin` (717) | "How should we start it?" | CONNECT, crown, 5 callers | KEEP (reshape) |
| `/trip-dates` (488) | Dates and shapes | trip-begin, trip-info | KEEP |
| `/trip-info` (865) | General info, members, invite link | details, crown | KEEP |
| `/trip-settings` (671), `/notifications` (240), `/permissions` (599), `/privacy` (146) | Trip admin | details | KEEP |
| `/trip-expenses` (index 444, add 188, balance 267, `[expenseId]` 143, edit 139) | Costs and settlement | Details > Costs; returned crown | **RETIRE** candidate (vision: expenses are not core); utility today |
| `/trip-accommodations` (index = `StayWorkspace`, add, `[id]/edit`) | Stay | Details > Stay | KEEP (Plan-owned stay) |
| `/trip-photos/find` (63) | Find photos | TripMapScreen | KEEP |
| `/trip-debrief/[tripId]` (80) | Debrief to private reflection | Places harvest prompt card | KEEP |
| `/trip-story/share` (52) | Story share | 2 callers; dark (STORY_SHARE false) | RETIRE or park |
| `/trip-proposal/[proposalId]` (72) | Replaces into the chat proposal card | chat | RETIRE (proposal detail is compatibility) |
| `/trip-place` (20) | Redirect to trip-info | — | compat |
| `/booking/[sessionId]` (1,487; function 781 lines under a 1,022-line exception) | Booking session: offers, cart, confirm | Details bookings, chat booking cards, object page, notifications. **The app never creates sessions** (`useCreateBookingSession` has 0 callers). | **RETIRE** |
| `/p/[tripId]/[proposalId]` (48) | Sign-in wall for a proposal link | web link | RETIRE along with voting |

### 2.7 Social, originals and handoffs

| Path | Screen | Reached from | Gate | Class |
|---|---|---|---|---|
| `/you/people` (602) | Invitations, circles (pairs), companions, **SOCIAL following** (follow pills, suggestions, activity) | Settings, portrait | — | KEEP circles and companions; **RETIRE** the following zone |
| `/you/circle/[circleId]` (371) | Circle detail, link trip, share claims | people | SOCIAL_CIRCLES (backend default on) | KEEP (pair circles) |
| `/profile/[userId]` (583) | Public profile: **Follow pill**, "Plan something in <city>" | people, portrait, Home destinations | — | KEEP the page; **RETIRE** Follow. No friend state, message, thread or axis (NOT BUILT). |
| `/invite/[slug]` (1,431) | Trip invite landing, accept, attendance | universal link `vesper-backend.fly.dev/invite` | — | KEEP (trip-scoped) |
| `/invite-code` (122) | Paste link or code | onboarding | — | KEEP |
| `/stories/[slug]` (962) | Public story reader | universal link `/stories` | — | KEEP (existing links) |
| Originals and place notes | see §2.5 and §3.7 | — | internal | NEW |

### 2.8 You, profile and settings

All are **KEEP** and live.

- `/you` — `YouPortraitScreen`, 550 LOC.
- `/you/settings` — `YouHubScreen`.
- `/you/account` and `/you/account/phone`.
- `/you/appearance`.
- `/you/privacy`.
- `/you/notifications`.
- `/you/preferences/autonomy` and `/you/preferences/constraints`.
- `/you/data/receipt`.
- `/you/feedback`.
- `/you/email-import`. This is surfaced, but the backend DNS and SendGrid setup is reported blocked.
- `/you/memory`, a re-export of the atlas memory screen.
- `/you/removed`.
- Alias redirects: `/you/autonomy`, `/you/constraints`, `/you/data-receipt`, `/you/phone`.

### 2.9 Onboarding and auth

| Path | Screen | Class |
|---|---|---|
| `/` | Mock → `/(tabs)/trips`; else `AuthRedirect` | KEEP |
| `/onboarding` (1,471) | Cover → fork (free text, three ambient starters, "I have a trip in mind") → trip-where / when / who or ambient sign-up. **Orphan steps still rendered:** `taste-interest`, `taste-pace`, `gift`, `permission`, `decline-reframe` (reachable only via QA `?step=` or a resumed draft). | KEEP (retire the orphan steps) |
| `/onboarding-safety` (164) | Dietary and access chips | KEEP |
| `/(auth)/sign-in`, `/sign-up` (Clerk: Apple, Google, email, phone OTP), `/goodbye`, `/session-recovery` | — | KEEP |

### 2.10 Share capture and notifications

| Path | Screen | Class |
|---|---|---|
| `/share-capture` (1,108; function 770 lines) | Intake v2 custody receipt. Actions: Keep this interpretation, Not this / corrections, Ask Vesper about this, Delete private share, Done (goes to Plans). `LegacyCaptureReceipt` is split out. | **NEW** (live) |
| `+native-intent.ts` | Maps `dataUrl=` share markers and app-link paths | KEEP |
| `/notifications` (730) | In-app inbox | KEEP |

### 2.11 Dev and QA (all **DEV**)

There are 36 files under `app/dev/`, registered through `Stack.Protected guard={isDevToolsEnabled()}` (`app/_layout.tsx`). `isDevToolsEnabled` is `__DEV__ || IS_INTERNAL_BUILD` (`galleryMenu.ts:331-337`), so **they ship inside every dogfood binary**.

Notable routes:
- `four-root-portfolio`
- `home-root-preview`
- `home-places-rehearsal`
- `instruments-gallery`
- `occasion-crown-gallery`
- `occasion-behavior-gallery`
- `deck-qa` — the only live importer of the decision-deck faces
- `discover-cold-start` — the only importer of `DiscoverCoverHome`, 2,257 LOC
- `adaptive-composition`
- `adaptive-shadow-evidence`
- `persona-switcher`
- `screenshot-mode`
- `force-state`
- `surface-census`
- `trips-home-kit`
- `places-workspace-kit`
- `stay-kit`
- `billing-sandbox`
- `membership-epoch`
- `profile-system`
- `interpretation-dossier`
- `m1-signatures`
- galleries for chat artifacts, canonical artifacts, composer, control, header and design system

---

## 3. Capability map against the designed product

**Status legend**
- **LIVE-DEFAULT** — on in production and preview.
- **INTERNAL** — needs a flag no shipped profile sets.
- **DOGFOOD** — on in the dogfood profile.
- **PARTIAL**
- **NOT-BUILT**
- **LEGACY**

### 3.1 Home

**Overall:** The whole four-root Home is **INTERNAL**. Its only evidence is QA harness and Maestro rehearsals.

**Governed Home components**

| Capability | Status | Evidence | Notes and tests |
|---|---|---|---|
| Crown (dominant unit) | INTERNAL | `HomeRootV2Screen.tsx` renders `projection.dominant_unit_id` in a CardSurface "crown"; backend `selectors.py:_home_dominant` | Re-elected when suppressed (backend) |
| Postures (7) | INTERNAL | `RootHomePosture` = urgent / live / planning / available / returned / quiet / cold (`utils/api/schema.gen.ts:31202`) | Mock posture flows: `.maestro/polish/home-root-{available,cold,live,planning,quiet,returned,urgent}.yaml`. The contract says they cannot certify governed v2. |
| Regions and labels | INTERNAL | `HomeRootV2Screen.tsx:66-126`: "Needs you now" / "Coming up" / "Now"; "In motion"; "Worth knowing" / "The city this week"; "From the trip" / "Carried forward"; returned posture reorders continuity | "Nothing else waits" appears only in Quiet (`:517`) |
| WorldRead, WeekShape, RestClose | INTERNAL | `WorldRead.tsx` (101), `WeekShape.tsx` (233) | WorldRead is an owner-state sentence, not weather or news |
| Degradation notice after value | INTERNAL | merged 9372e154c | — |
| v1 compatibility Home | INTERNAL | `HomeRootScreen.tsx` (274), `/api/root-projections/home` | A cold user sees the literal "No owned current state clears Home's admission threshold." (prior inventory; unchanged file) |
| Why-this sheet | **NOT-BUILT** on Home | The server sends `why_this` (e.g. `home_human_openings.py:203`), but no Home component renders it. `why_this` is shown only on the takes / receipt surfaces and the dev deck. | — |
| Steering (not-this / less-like-this) | **NOT-BUILT** on Home | Home actions are capability refs only: `chat.continue`, `chat.open_plan_proposal`, `places.map`, `places.open_context`, `places.open_entity`, `places.open_friends`, `source.inspect` (`utils/rootProjectionNavigation.ts`) | — |
| **Live Home object crown / coupon tray** | **NOT-BUILT** | No `coupon`, `companion tray` or `object crown` anywhere in app code. The Live posture has only a text anchor and budget. | Design exploration only (`docs/working/design-gen/home/gen_live*.py`, untracked in the canonical workspace) |

**The 20 renderable kinds** (`utils/homeRootV2RendererRegistry.ts`, bodies from `HomeRootV2UnitRenderer.tsx:1237-1262`)

| Kind | Body | Notes |
|---|---|---|
| `now_commitment_instrument` | InstrumentBody | Status stamp + `payload.fallback` text; no drawn instrument |
| `now_recovery_instrument` | InstrumentBody | Same |
| `now_prepared_possibility` | GenericBody | — |
| `now_invitation` | GenericBody | — |
| `now_sample_demonstration` | SampleDemonstrationBody | `HomeV2SampleDemonstration.tsx` |
| `people_original_delivery` | OriginalDeliveryBody | "ORIGINAL FROM …" (the lane changes this to "FROM" + sender · time, §6); 30 s revalidation |
| `motion_occasion_row` | MotionUnit | Bypasses the registry body |
| `people_participants_row` | ParticipantsBody | — |
| `motion_loose_end_row` | MotionUnit | Bypasses the registry body |
| `motion_all_plans_door` | GenericBody | — |
| `horizon_editorial_passage` | EditorialBody | — |
| `horizon_mechanism_row` | MechanismBody | — |
| `horizon_aperture_row` | ApertureBody | — |
| `horizon_prepared_alternatives` | AlternativesBody | — |
| `people_note_door` | **HumanPlaceNoteBody** | New in the merge: sender anchor, human words in serif, muted Place basis, "See this place" door |
| `people_authored_region` | AuthoredRegionBody | — |
| `continuity_capability_field` | GenericBody | — |
| `continuity_since_you_looked` | GenericBody | — |
| `continuity_reconstruction` | GenericBody | — |
| `continuity_life_door` | GenericBody | — |

Any unregistered kind invalidates the envelope, and Home falls back to v1 (`rootProjectionV2Conformance`).

**Social and sample units**

| Capability | Status | Evidence | Notes and tests |
|---|---|---|---|
| Received originals | INTERNAL + backend flag | `OriginalDeliveryBody` (`:765+`), `components/inbound/ReceivedOriginalSurface`, `/original-delivery/[id]` | Maestro `87-home-original-delivery`, `86-life-original-delivery`, `88-life-original-sender-withdrawal` (local-owner rehearsals) |
| Addressed Place notes | INTERNAL + backend flag | `people_note_door` → HumanPlaceNoteBody | Maestro `79-home-real-social-send`; `run-home-real-joined-opening.sh` |
| **Joined human openings** (note + current Place opening on the same entity become one unit) | INTERNAL + backend flag | Backend `root_projection/v2/home_human_openings.py` (a `model_copy` of the note with the Place destination, role WORLD_OPENING); rendered by HumanPlaceNoteBody | Merged 09-26. Evidence is synthetic local-owner data. |
| Cold-start sample | INTERNAL, and backend-dark (needs ROOT_DELIVERY_* flags + secret) | `HomeV2SampleDemonstration.tsx` (130) | Prior finding: world-only supply can make the page Quiet instead of Cold and suppress the sample. The backend lane has "admit cold-start sample through value composition" (bf1e5dadf, unmerged). |
| Source inspection ("source.inspect") | INTERNAL + backend worker dark | `HomeRootExperience.tsx:196`, `useRootSourceInspection` | The lane completes the request/return loop (aa3e235d6, §6) |
| Instruments (DayBand, RhythmBars, BasisStrip, ProgressTrack, TideCurve) | DEV only | `components/instruments/*` (687 LOC) imported only by `app/dev/instruments-gallery.tsx` | — |
| Occasion crown prototype | DEV only | `components/occasion-crown/OccasionCrownPrototype.tsx` ← `app/dev/occasion-crown-gallery.tsx` | — |

**Legacy Plans home (what users get today): LIVE-DEFAULT, LEGACY**
- Files: `TripsHomeBody.tsx` (784), `TripsHomeController.ts` (703), `components/trips` (9.1k LOC, 37 files).
- The tripless crown shows "In motion" (`utils/tripsHomeStackModel.ts:349`).
- The merge deleted about 1.47k LOC of retired cascade styles (`TripsHomeStyles.ts` −1,295, `TripsHomeArtStyles.ts` −172).

**Tests.**
- About 29 jest files touch Home root / root-projection-v2: `__tests__/components/home-root/*` (2), `HomeRootV2Screen.smoke`, `HomeRootScreen.smoke`, `WeekShape.test`, plus utils tests.
- Legacy Trips home: about 58 jest files.
- Maestro Home: 7 polish posture flows plus 16 real/local-owner flows: `47–52` home-places, `77–81`, `87`, `89`, `91`. Trips-home Maestro: 10 numbered flows plus 12 polish flows.

### 3.2 Places

| Capability | Status | Evidence | Notes |
|---|---|---|---|
| Section feed by context and posture | LIVE-DEFAULT | `PlacesWorkspace.tsx` (765) → `GET /api/places/feed`; `PlacesSectionFeed.tsx` (323); card registry under `components/places/renderers/` | Starter / nearby / guide / reading / areas / saved / experiences / gap / harvest / changed / anniversary |
| **World Field** (semantic field units) | INTERNAL (governed) | `PlacesSemanticField.tsx`; runtime envelope `field_units` | `PlacesRootV2Screen.tsx` ("The world field") is **still orphaned**: imported only by its test |
| **Mixed order** (field units between whole sections, in server order) | INTERNAL | New `components/places/placesPageRenderItems.ts` (134); PlacesSectionFeed rewrite (merged 7e94c42a8) | With no projection units it falls back to today's layout |
| Pocket / map | LIVE-DEFAULT | `app/(tabs)/places/map.tsx` (955): layers All / Vesper / Saved / Trip; pin peek "Ask Vesper"; approximate trip-companion pins | Adaptive orient shadow is internal and shadow-only |
| Scope chooser | **NOT-BUILT** as a control | The root header shows a scope label only (`PlacesRootHeaderLeading.tsx`). Re-scoping happens only via starter city cards (`contextHandle=place:<id>`). `components/places/core/PlacesScopeControl.tsx` exists but is **dead** (no importer). | The root ignores `placeSlug` / `placeName` from the Discover redirect and Universal Search (`PlacesWorkspace.tsx:134-139` reads only `query`, `contextHandle`, `focusSection`, `rootReturnToken`) |
| "From friends" | PARTIAL / LIVE | "From your people" section is trip-scope only (backend `friends.py`). Place-pull cards need backend PLACE_HANDOFF_PULL. "X saved this" provenance: NOT-BUILT (producer is always unknown). Friends' saves on the map: NOT-BUILT. | Maestro `75-places-real-social-pull` (rehearsal) |
| Checks / visit-fit | PARTIAL | `PracticalVisitCheck` on the site page (`EntityObjectPage`) and the rebuild page | **Dead end by default:** site "Check a visit now" pushes `routes.places({practicalRequest})` (`site/[siteId].tsx:95-185`), but default `PlacesWorkspace` never reads it. It is answered only by the governed runtime. |
| Saved / reading collections | LIVE-DEFAULT (private) | `PlacesCollectionScreen.tsx` | No shared collections |
| Inline search | LIVE-DEFAULT (not in Home, Around-me or Saved scopes) | `PlacesWorkspace.tsx` | — |

**Tests.** About 74 jest files touch Places. There are 12 polish flows; the numbered flows are `75, 76, 83, 84, 90, 91` plus `47–52` shared with Home.

### 3.3 Place / entity page

| Capability | Status | Evidence |
|---|---|---|
| Default venue page | LIVE-DEFAULT, LEGACY renderer | `app/venue/[venueId]/index.tsx` (2,018) |
| ObjectPageRebuild | INTERNAL | `components/places/ObjectPageRebuild.tsx` (1,237); OBJECT_PAGE_REBUILD in no profile. Also used for exact-reading and handoff entries. |
| Verb **Keep** | INTERNAL (rebuild) | `referenceVerb="keep"` (`ObjectPageRebuild.tsx:881`). The legacy page says Save. |
| Verb **Ask** ("Ask Vesper") | LIVE-DEFAULT on legacy pages (AskVesperBlock); INTERNAL on the rebuild | `ObjectPageRebuild.tsx:1028` |
| Verb **Leave for someone** | INTERNAL on the rebuild (flag-gated). **Dead door on legacy** (next row). | `ObjectPageRebuild.tsx:1070-1080` |
| Verb **Tonight?** | INTERNAL (only when occasionLive) | `ObjectPageRebuild.tsx:1022` |
| Read up | INTERNAL + server canary | ENTITY_RESEARCH_REQUESTS |
| Purpose reading (discovery / explicit_visit / arrangement) | PARTIAL | Rebuild via `objectPageProjection.ts` (internal); site page arrangement summary live. The legacy venue page ignores `openingPurpose`, which the trip object page sends. |
| People lines (byline, quotes, sheet) | INTERNAL + backend flag | `PeopleLineSheet` is imported only by `ObjectPageRebuild` (`:573-578`) |

**Legacy dead door (verified at 43225df35).** `RelationshipPlaceNoteAction` renders without a flag check in three places:
- the venue page (`app/venue/[venueId]/index.tsx:1765`)
- `ExperienceGraphSummaryCard` (`:569`), which is mounted on Plans home (`TripsHomeBody.tsx:71`)
- the Places experience-graph door (`PlacesExperienceGraphDoor.tsx:7`)

Its only guard is exactly one confirmed active pair circle (`ExperienceGraphSummaryCard.tsx:84-101`). Pair circles are creatable in production (`/you/people`). The submit calls relationship routes that 404 unless the backend secret is set. This contradicts the rule written at `constants/featureFlags.ts:186-189`.

**Duplicate families.** Six-plus entity renderers:
- the venue legacy page
- `EntityObjectPage`
- `ExperienceDetail`
- the accommodation page
- `ObjectPageRebuild`
- the trip object page
- `PlaceHome` plus `/place/[placeSlug]`
- two public preview pages

**Tests.** About 23 jest files touch these pages. Maestro `54b`–`54g` cover venue, site and experience rebuilds and the entity state matrix.

### 3.4 Life

| Capability | Status | Evidence | Notes |
|---|---|---|---|
| Life root, lenses Time / Places / Threads / People | LIVE-DEFAULT | `LifeRootV1Screen.tsx:31` (`LENSES = time, places, threads, people`), `useLifeRootProjectionV1({enabled:true})` | Threads is nearly always empty: only Plans tied to an Occasion or Commitment (backend) |
| Dossier (per-record reading) | PARTIAL | Graph rows open `/you/life-record?record=`. Anchors open `/you/memories/artifacts/[id]`. Sources open `/you/intake-submissions/[id]`. | No dedicated Plan or Occasion page from Life |
| Refind | INTERNAL | `/you/life-find` behind LIFE_REFIND_LANE; otherwise the search icon opens universal search | Maestro `85-life-original-refind` |
| Originals ("Shared with you") | INTERNAL + backend | `life-find.tsx:156` | — |
| Photos | LEGACY path | Onboarding diary scan and `/atlas/scan`; drafts project into Life (backend) | No Life entry to review |
| "Everything kept" (full record) | LIVE-DEFAULT | Archive icon and scroll door to `/you/life-record` | Maestro `73-life-record-device-certification` |
| Returns (featured Return block) | **NOT-BUILT** (server) | The UI exists (`LifeRootV1Screen.tsx:233-249`), but backend `return_candidate` has **no producer**. Only the model field and compiler pass-through exist (`life_projection/compiler.py:88`, re-verified at backend c8c9f5785). | — |
| Threads (curiosity threads) | NOT-BUILT | — | — |
| Organized groups | LIVE route, likely empty | `/you/life-groups` | Maestro `82-life-organized-record` |
| Keep → Life gesture | NOT-BUILT | Keep reaches Life only implicitly through owners. Saves do not reach Life. | — |

**Tests.** About 18 jest files touch the Life root and record. The legacy Atlas surface still has about 63 jest files and about 20 polish flows (`atlas-*`), which capture redirected or compatibility surfaces.

### 3.5 Plans

| Capability | Status | Evidence |
|---|---|---|
| Itinerary rail (day rail, list/map faces, stop sheet) | LIVE-DEFAULT | `plan.tsx` (2,139; `PlanScreen` under a 1,118-line exception); `components/trip-plan` (7.95k LOC), `trip-itinerary` (4.4k), `trip-map` (5.8k) |
| Change sheets | LIVE-DEFAULT | `ItineraryOperationSheet` (commit or propose to group); `/changes` undo |
| **Seven-sentence page** | NOT-BUILT | No such surface. The Plan page is still the rail. |
| PlanStopAssistance / **Send proposal** | LIVE-DEFAULT | `components/trip-plan/PlanStopAssistance.tsx:122` "TO X · DRAFT", `:137` "Send proposal". This is a user-sent in-app message. |
| CurrentShapeSurface | INTERNAL (PLAN_SHAPE in no profile) | `plan.tsx:538-544`, `components/trip-itinerary/CurrentShapeSurface.tsx` |
| LocalPlan | DOGFOOD | `plan.tsx:178-188`, `components/trip-plan/LocalPlanScreen.tsx`. Without the flag: "This occasion is not available in this build". |
| Outcome artifact / group micro-journey | DOGFOOD | `plan.tsx:642, 1026` |
| Booking | LEGACY, reachable | `/booking/[sessionId]`; `components/booking` (3.2k); 148 jest files mention booking |
| Voting | LEGACY, live | `VoteWidgetCard` via `AttachmentRenderer.tsx:115`; the decision deck is dev-only |
| Expenses | LIVE-DEFAULT utility | `/trip-expenses/*` (1.2k LOC routes), `components/expense` (3.7k) |

**Tests.** About 190 jest files touch plan or itinerary; about 204 match the trips/booking/expense families. There are about 119 journey and trip Maestro flows.

### 3.6 Chat

| Capability | Status | Evidence |
|---|---|---|
| Header naming (design: no name) | NOT-BUILT | `utils/chat/conciergeHeaderModel.ts:30,39` titles "Vesper"; `PrivateVesperNote.tsx:27` `VesperAttribution` signature |
| Cards "only when earned, one per turn" | PARTIAL (prompt rule only) | 20 attachment types active and 1 deprecated (`atlas_draft`) in `utils/chat/chatCardTypes.generated.ts:79-100`. `booking_confirmation` and `booking_proposal` are still active. |
| Side chat | PARTIAL | Substrate `POST /api/trips/{id}/side-chat` (`utils/api/http.ts:2891`). No "Side chat" title, fold or room row. |
| Drafts NOT SENT ("you send") | NOT-BUILT in Chat | Only Copy / Share of a reply. The live analogue is the Plans "Send proposal". |
| Scope line from objects | PARTIAL | Header context "private · trip-linked" / "private · draft" (`conciergeHeaderModel.ts:41-49`); the object pages seed "Ask Vesper" |
| Group composer scope line | Dead code | `components/chat/GroupComposerContextBar.tsx` ("Everyone sees this · @Vesper to ask") has **no importer**. The group room uses a placeholder only (`trips/[tripId]/chat.tsx:1366`). |
| Attachments (photo library, camera) | LIVE-DEFAULT | Image paste or drop: NOT-BUILT |
| Queued turn ("UP NEXT") | LIVE-DEFAULT | `QueuedTurnTray` |
| Group facilitator | LEGACY, live | `@Vesper` summons, vote widgets, `compose_group_message` |

**Tests.** About 141 jest files touch chat. Maestro has 27 `vesper-*` polish flows plus numbered chat flows.

### 3.7 Social

| Capability | Status | Evidence |
|---|---|---|
| Send original | INTERNAL + backend | `/you/intake-submissions/[id]` sender (RELATIONSHIP_UUID) |
| Place notes | INTERNAL (rebuild) / dead door on legacy | See §3.3 |
| Receive (Home, Life, detail) | INTERNAL + backend | §3.1, §3.4 |
| Collections / "Shared with X" | NOT-BUILT | Only life-find "Shared with you" (internal). Saved is private. |
| Likes / comments / keep on social objects | NOT-BUILT | Only chat `ReactionCard` exists (a group poll-style card) |
| Audience controls | PARTIAL | Circle "Shared with this circle" claims (`you/circle/[circleId].tsx:78`); trip privacy settings |
| Guests | PARTIAL | Trip invite landing: LIVE. `/p/` proposal link is a sign-in wall. `routes.guestCapability` points at `/guest/…`, but **no `app/guest` route exists**. |
| Connecting (invite a friend to Vesper, not to a trip) | NOT-BUILT | "+ Invite someone to a trip" only goes to trips |
| Pair circles | LIVE-DEFAULT | `/you/people` "Name this pair" (`people.tsx:74-81`), `/you/circle/[id]` |
| Follow | LEGACY, live | `profile/[userId].tsx:113-133` Follow / Unfollow, `you/people.tsx` SOCIAL zone, `useToggleFollow` |

### 3.8 You

| Capability | Status | Evidence |
|---|---|---|
| Portrait | LIVE-DEFAULT | `YouPortraitScreen.tsx`. Sections: IN YOUR WORDS, THE RECORD, PLACES YOU HOLD, SAVED FOR LATER, WITH DIFFERENT PEOPLE, published. |
| Friend state / message / thread / shared axis on a person | NOT-BUILT | `profile/[userId].tsx` has only Follow and "Plan something". The backend Together projection is dark with no client. |
| Trust controls | LIVE-DEFAULT | autonomy, constraints, privacy, data receipt, notifications (`components/trust` is used by 16 You screens) |
| Memory ("What Vesper knows") | LIVE-DEFAULT (legacy atlas screen) | `/you/memory` → `app/atlas/memory.tsx` (799) |

**Tests.** About 27 jest files touch You. Maestro: 4 `you-*` and 5 `trust-*` polish flows.

### 3.9 Cross-cutting capabilities

| Capability | Status | Evidence |
|---|---|---|
| Share capture / intake | LIVE-DEFAULT | `expo-share-intent` plugin; `ShareIntentHandler` mounted unconditionally; `/share-capture`. A kept interpretation creates only a private anchor. |
| Notifications / push | In-app inbox LIVE; push registration LIVE (`PushRegistrar`, `PushAskHost`) | Remote delivery depends on backend `EXPO_PUSH_ENABLED` (unverifiable). Destinations are overwhelmingly trip / atlas (`utils/notificationDestination.ts`). |
| Onboarding | LIVE-DEFAULT | No home-city step. Taste and diary steps are orphaned. |
| Membership / paywall | INTERNAL (billing-sandbox only) | `BillingProvider` and `CommercialUpgradeProvider` are mounted but inert |
| Voice | DOGFOOD | `VoiceOverlayProvider` is always mounted; entry points need VOICE_ENABLED. `utils/voice/*` (6 files, 1.5k LOC) is **unreachable**. |
| Instruments | DEV | §3.1 |

---

## 4. Component and code health

### 4.1 Size by surface (components/, TS+TSX LOC, files)

| Directory | LOC | Files | Directory | LOC | Files |
|---|---|---|---|---|---|
| places | 18,372 | 85 | discover | 3,880 | 15 |
| chat | 17,350 | 92 | expense | 3,695 | 11 |
| ui | 16,600 | 130 | stay | 3,490 | 9 |
| trips | 9,063 | 37 | booking | 3,191 | 9 |
| atlas | 8,607 | 33 | home-root | 3,158 | 8 |
| trip-plan | 7,953 | 34 | you | 2,415 | 8 |
| trip | 5,991 | 20 | memory | 2,320 | 7 |
| trip-map | 5,838 | 24 | onboarding | 2,157 | 19 |
| decision-deck | 5,311 | 17 | root-projection | 1,406 | 11 |
| trip-itinerary | 4,363 | 20 | vesper-workbench | 1,172 | 2 |
| instruments | 687 | 6 | life | 304 | 1 |

**Largest functions** (from `check-size-budgets`; the limit is 800 lines, with pinned exceptions):

| Function | Lines | Exception |
|---|---|---|
| `ConciergeChatScreen` | 817 | exception 872 |
| `ComposerBar` | 800 | at the limit |
| `PlaceHomeScreen` | 799 | — |
| `ProposalDetailScreen` | 798 | — |
| `AddExpenseSheet` | 796 | — |
| `GroupChatRoom` | 791 | exception 800 |
| `TravelPlanScreen` | 784 | — |
| `BookingSessionScreen` | 781 | exception 1,022 |
| `ItineraryObjectScreen` | 780 | — |
| `ImportCaptureScreen` | 770 | — |

**Largest files:**

| File | Lines |
|---|---|
| `utils/api/mock/trips.ts` | 3,411 (exception 3,782) |
| `utils/api/http.ts` | 3,146 |
| `utils/api/interface.ts` | 3,000 |
| `components/atlas/AtlasReadingCanvas.tsx` | 2,679 |
| `utils/api/mock/atlas.ts` | 2,640 |
| `utils/api/mock/discover.ts` | 2,514 |
| `components/discover/DiscoverCoverHome.tsx` | 2,257 (dev-only) |

**Observations**
- The legacy families (atlas, discover, decision-deck, booking, expense, trips home) total about **39k component LOC**. That is about five times the new-product root code (home-root 3.2k, life 0.3k, and the Places governed pieces).

### 4.2 Duplicated or legacy component families

1. **Place / entity detail.** Nine renderers (§3.3). Only `ObjectPageRebuild` matches the designed verbs, and it is internal.
2. **Home.** Three coexist: `TripsHomeBody` (live), `HomeRootScreen` v1 (compatibility) and `HomeRootV2Screen` (governed). Plus the dead `AtlasIndex` and dev `home-root-preview`.
3. **Places root.** `PlacesWorkspace` is the renderer for both the legacy and governed postures. `PlacesRootV2Screen` is an orphan parallel renderer.
4. **Decisions.** `decision-deck` (14 files, 4.5k LOC, dev-only), `VoteWidgetCard`, `ProposalDetailScreen` (compatibility) and `collaboration/DecisionPrimitives` (live, shared).
5. **Memory and record.** The atlas readers (inbox / compose / candidate / artifact / long-view / readings / unpacked) sit in parallel with the Life record, intake-submission and artifact readers.
6. **Save vs Keep.** Save on the legacy pages and "keep" on the rebuild.

### 4.3 Design-system token usage

**Ratchets.** All passed, pinned at exactly their baselines, with zero headroom:
- raw hex 14/14 (`check-color-budget` scope)
- raw type sizes 77 exceptions
- raw spacing 359/359
- hand-rolled buttons 59/59
- hand-rolled cards 162/162 (migrate to CardSurface)
- `borderRadius` literals 210/210
- `muteSoft` 103/103
- `boxShadow` 6/6
- 62 stable components (lifecycle)
- M-1 surface contraction: 47 surfaces OK
- Home-surface budgets pass, with `tripsHomeSectionPlan.ts` at 263/267 and `placesPresentationModel.ts` at 231/232

**Adoption across 797 non-dev TSX files:**
- `VText` in 493 files
- `constants/colors` imported in 590
- `CardSurface` in 95
- `Tap` in 32
- raw `<Pressable` in 12
- react-native `Text` imported in 61

A broader grep finds 102 quoted hex literals and 77 `fontSize:` literals in `app` + `components`. The color budget counts a narrower scope.

### 4.4 Dead-code candidates (static reachability from all `app/` routes)

**83 modules, about 11.9k LOC, have no importer path from any route.**

| Group | Modules |
|---|---|
| Voice | `utils/voice/*` (interruptionController, liveAudioSessionProvider, liveNarrationPlaybackAdapter, narrationPlayback, sileroVadWrapper, vadOnsetDetector; 1.5k LOC); `hooks/useNarrationWithInterruption.ts` (568) |
| Concierge home | `hooks/useConciergeBookingCardActions`, `…HomeCardImpressions`, `…HomeCardVisibility`, `…HomePerformance`, `…NearYouActions`, `useDeckSettlementAction`; `utils/conciergeHomeFeedModel`, `conciergeHomeTelemetry` |
| Plans actions | `hooks/useMoveBlock`, `useApplyReschedule`, `useCommitPick`, `useCheckBlockMove`, `usePlanProposalUndo`, `useVoteProposal`, `useSettleOwedShares`, `useStaySummary`, `useTake`, `useNearMe`, `useDiscoverProximity`, `useReturnedTripStoryEntry` |
| Places | `PlacesRootV2Screen`, `core/PlacesBrowse`, `core/PlacesScopeControl`, `EntityInterpretationBlock`, `utils/placesWorkspace.ts` |
| Chat | `GroupComposerContextBar`, `GroupMemberAskingBanner`, `LazyResearchBadge`, `create/ConversationContextAttachment` |
| UI | `AnchorKindMark`, `LifeAnchorRow`, `LifeEpisodeGroup`, `LifeKeepsake`, `RouteStrip`, `Stack` |
| Trip | `BlockWhyRow`, `GroupAndLearnConsentSheet`, `LeaveByHintStrip`, `MemoryModeSections`; `trip-plan/BlockDiffChip`, `GapAffordance` |
| Semantic / composition utils | `semanticResultConformance` (508), `adaptiveExpressionProjection` (340), `artifactCirculation` (283), `homePortfolioComposition` (271), `atlasCompositionAdapter` |
| Mock fixtures | 5 files in `constants/mocks/*Fixtures` (1.9k) |
| Other | `home-root/RootDegradationNotice.tsx` (2-line shim), `root-projection/RootTreatmentExposureBoundary` |

**Caveat.** The walk sees only static relative imports. It does not count test-only use, and a few modules may be loaded by non-literal `require`. Treat these as candidates: confirm each with `tsc` and a jest run before deleting.

**65 modules, about 15.7k LOC, are reachable only from `app/dev/*`:**
- `components/decision-deck` (4.5k)
- `components/discover` (2.7k, incl. `DiscoverCoverHome`)
- `constants/mocks` (2.4k)
- `adaptive-composition` (955)
- `utils/compositionBrief.ts` (702)
- `instruments` (687)
- `semanticResultEnvelope` (683)
- `conciergeHomeInteraction` (499)
- `profile-system` (432)
- `experience` (273)
- `occasion-crown` (242)
- `vesper-cards` (110)

These ship in dogfood binaries.

### 4.5 Test coverage per surface (approximate, keyword-matched)

Totals: 1,253 jest files under `__tests__`, plus 64 `*.test.*` files elsewhere, and 346 Maestro flows excluding subflows. There are **no `.skip` / `xit` / `xdescribe` tests** (grep returned 0). jest ignores only `__fixtures__` and `.worktrees`.

| Surface | Jest files (approx.) | Maestro flows (approx.) | Comment |
|---|---|---|---|
| Home root (new) | ~29 | 7 polish + 16 local-owner | Rehearsal-grade; the contract says mock posture flows cannot certify governed v2 |
| Trips / Plans home (legacy) | ~58 | 10 numbered + 12 polish | Heavy coverage on a surface the vision retires |
| Plan / itinerary | ~190 | ~119 trip and journey | — |
| Chat / Vesper | ~141 | 27 polish + numbered | — |
| Places (+ entity) | ~74 (+23 entity) | 12 polish + ~14 numbered | — |
| Life (new) | ~18 | ~9 numbered | Thin relative to its live status |
| Atlas (legacy) | ~63 | ~20 polish + 7 journeys | Several polish flows target redirect routes (`polish/atlas-home` opens `/(tabs)/atlas`, `polish/discover-home` opens `/(tabs)/discover`) and are classed "compatibility" in `scripts/polish-qa/surfaces.mjs:96-104` |
| You / social | ~27 (+44 incl. people / invite) | 4 you + 5 trust | — |
| Share capture | ~7 | ~0 dedicated | The newest live intake path has little UI test coverage |
| Booking | ~148 mentions | 11 polish | Legacy with retirement pending |

---

## 5. Deprecation candidates (app)

**Risk key**
- **L** — no live importer; delete with a tsc and jest run.
- **M** — reachable, but only by deep link, notification or dev.
- **H** — live user path; needs a product decision and migration.

### 5.1 Remove now (L)

- **Unreachable modules** (§4.4): the voice runtime, the concierge-home hooks, the Plans action hooks, `PlacesRootV2Screen`, `PlacesScopeControl` and `PlacesBrowse`, `GroupComposerContextBar`, the `RootDegradationNotice` shim, and the fixture files.
  - Dependencies: their tests import some of them (for example the `PlacesRootV2Screen` test). Delete the tests together.
  - Before deleting the voice modules, confirm that live voice (dogfood) does not load them by name.
- **Dead `AtlasIndex` export** in `app/(tabs)/atlas/index.tsx`. Keep the default redirect. Update the `atlas-home.smoke` test. This removes the last consumer of `LIFE_ROOT_V1_ENABLED` outside dev.
- **`utils/discoverRouting.routeForDiscoverTarget`** (test-only).
- **Flags with no reader or no effect:**
  - `EXPO_PUBLIC_AI_IMAGE_FALLBACK` (set in three profiles, read nowhere)
  - `CONTENT_GRAPH_GEOFENCE` (exported, no consumer)
  - `COMPOSER_DICTATION_ENABLED` (no UI; keep only the Info.plist logic if dictation is planned)
- **Registry fixes:** delete the stale `PLACES_SECTIONS_FEED_ENABLED`, correct the `EXPO_PUBLIC_LIFE_ROOT_V1` note, and register the app half of `RELATIONSHIP_UUID_HANDOFFS`.

### 5.2 Remove after a small check (M)

- **Orphan legacy screens:** `/atlas/saved-places`, `/atlas/narration-history`, `/atlas/whole`, and `/guide/[slug]` (plus `components/guides`). These are reachable only by stale deep links.
  - Risk: old notifications might still point at them. Check `utils/notificationDestination.ts` (it does not reference these today).
- **Redirect-only routes:** the 11 `/atlas/*` → You redirects, the 16 `/you/atlas/*` redirects, `/your-map`, `/(tabs)/discover`, and `/trip-place`.
  - Retire after a telemetry window. The `surfaces.mjs` deletion gate is "telemetry or explicit route-retirement decision".
  - Note: the Discover redirect drops the place context anyway.
- **Hard-false flags and their dark UI:**
  - `POSTCARDS_ENABLED` (atlas artifact)
  - `AMBIENT_ENABLED` (Trips home "While you're here" and the controller's ambient query)
  - `DOSSIER_VOICE_STUB`
  - `STORY_SHARE_ENABLED` plus `/trip-story/share` and the recap share UI
  - Their registry entries expire 2026-10-04: decide then.
- **Expiring rehearsal flags:** `ADAPTIVE_PLACES_ORIENT_SHADOW_ENABLED` (09-28) together with `app/dev/adaptive-*` and `components/adaptive-composition`.
- **Dev-only legacy families:**
  - `components/decision-deck` (4.5k) plus `app/dev/deck-qa` and the `gallery` deck section
  - `components/discover/DiscoverCoverHome` (2.3k) plus `app/dev/discover-cold-start`
  - Dependency: `utils/vesperWorkbenchModel.ts` and ten other utils/hooks import `components/decision-deck/model` for **types**. Move `model.ts` first.
  - Keep `components/discover` pieces that live pages still use (the dossier reader, `WhyForYouCallout`, `FeedSaveButton`).
- **Onboarding orphan steps** (`taste-interest`, `taste-pace`, `gift`, `permission`, `decline-reframe`; rendered at `app/onboarding.tsx:563-650`, re-verified). Also check the persisted-draft resume path.
- **Polish flows capturing redirects** (`atlas-home*`, `discover-home*`). Mark them retired or re-point them at Life / Places.

### 5.3 Product decisions required (H)

- **Trip-first Plans home** (`TripsHomeBody` / Controller plus `components/trips`, 9k LOC).
  - Replacement: four-root Home.
  - Blockers: four-root shell cutover, and the flags expiring 09-28 with open promotion questions.
  - Dependencies: many `routes.trips()` callers (Done in share capture, the `/` redirect, You back-fallback).
- **Booking UI:** `/booking/[sessionId]`, `components/booking`, the Details "Booking activity" section, chat `booking_*` cards and `EXPO_PUBLIC_LIVE_BOOKING_ENABLED`.
  - Dependencies: notifications route to `bookingSession`; the card catalog marks booking cards "active". Flip them to "retired" to route to `RetiredCardFallback`.
- **Voting and the facilitator:**
  - `VoteWidgetCard`, `/trip-proposal`, `/p/[tripId]/[proposalId]` and `ProposalDetailScreen`
  - the `@Vesper` group-facilitator actions and the room agency controls
  - Dependency: the itinerary "propose to group" flow lands as a vote card in the group chat. It needs a replacement review path, such as Send-proposal-style human messages.
- **Follow graph:** `FollowPill`, `useToggleFollow` / `useFollowing`, the `/you/people` SOCIAL zone and the profile Follow pill.
  - Keep circles and companions.
  - Also fix the stale "Find people" → Discover copy.
- **Expenses and settlement.** Retire, or keep as a utility.
- **Legacy venue page vs `ObjectPageRebuild`.**
  - Promote the rebuild (OBJECT_PAGE_REBUILD expires 10-07), then retire `VenueCompatibilityContent`, `ExperienceDetail`, `EntityObjectPage` and the separate accommodation page.
  - **Immediate fix regardless of the decision:** gate `RelationshipPlaceNoteAction` on `RELATIONSHIP_UUID_HANDOFFS_ENABLED` in all three legacy mounts (§3.3).

---

## 6. What the active Codex lane adds

**Lane:** `/Users/feihuyan/travel-workspace--home-value-delivery/travel-app`, branch `codex/home-value-delivery`, HEAD aa3e235d6. Its merge-base is `origin/main` 43225df35, so it is current.
- 17 commits (09-25 to 09-26 18:07).
- 57 files, +2,135 / −249.
- **No change** to `eas.json`, `constants/featureFlags.ts`, `productSystemRollout.ts` or routes. Everything stays inside the INTERNAL governed Home.

| Commit | Change | Capability affected |
|---|---|---|
| 66e2c3c02, 122f4d2d6, e0bf0a7e3 | Received original shows the sharer and share time: "FROM" + `SENDER · <time>` attribution. New `utils/originalDeliveryTime.ts`; UTC fallback labelled. | Home received originals; `/original-delivery` |
| 8fc767355, 04d4ed85c | Restore the exact reading position on return from a unit, using viewport-Y-aware scroll restore (`homeRootReturnScrollOffset`, `rootProjectionReturnRegistry`). Coalesce the return refresh. | Home navigation continuity |
| 1b23ed891, 6489ef4c4 | Editorial hierarchy: the "A closer reading" kicker shows only when the passage is the crown; the "A few ways in" kicker is removed from alternatives. | Home editorial and alternatives units |
| a963fa0b9 | Drop the redundant canonical-source caption on Outcome continuity rows | Home continuity |
| 2840a2420, 7e7108d9e, 957fddde2 | Native fixture for a received original; accessibility label for the received note; photo aspect preserved (`OriginalMaterialView`) | Received originals |
| 58f53d3fb | Stop owner polling for originals when unfocused | Received originals (battery and network) |
| 37633c71c | Register the Home 02 / 03 design references as reference-only crops (`docs/surfaces/home-root/design-refs/manifest.json`) | QA and design evidence |
| 42cba2d30, 7d7d5b762 | Quiet-posture mock fixture: a substantive Sorrento-tuff-vs-Palisades-diabase "geology connection" | Mock and QA content only (`constants/mocks/rootProjectionV2.ts`) |
| 48ee7ba88 | `run-home-full-scroll.sh` targets the lane's assigned simulator UDID | Rehearsal tooling |
| aa3e235d6 | "Complete Home source result return loop". `useRootSourceInspection` now sends the unit's full `source_refs`, not only the private attachments. Adds Maestro `92-home-source-result-request`, `93-home-source-result-return` and `scripts/maestro/run-home-source-result-real.sh`, and updates the Places contract. It also changes `package.json`: `react-native-reanimated` 4.6.0 → 4.2.1, `react-native-worklets` 0.12.1 → 0.7.4, drops the `expo.install.exclude` block, and edits `scripts/native-compatibility*`. | Home Source inspection (INTERNAL; the backend worker is dark by default). **The native dependency downgrade affects every build** if merged. |

The lane's working tree was clean at the last read (18:07). Earlier uncommitted Source-result work became aa3e235d6.

**Companion lanes (context only):**
- **Workspace lane** (10 commits): evidence and roadmap docs such as "Record real owner-backed Home composition" and "Record Source workflow acceptance".
- **Backend lane** (3 commits):
  - bf1e5dadf "admit cold-start sample through value composition"
  - 8fbad4db7 "keep cold demo beside places door"
  - 6c792ed8b "offline API startup"

  The backend lane addresses the cold-start-sample suppression the prior inventory flagged. It is unmerged.

**Net effect.** The lane deepens the quality of the internal Home: originals, return continuity, editorial hierarchy and the Source-result loop. It does not change what any shipped or dogfood build shows, with one exception: the reanimated/worklets version change applies to all builds and needs native verification.

---

## Appendix A — Changes since the 09-25 inventory (23cff76f4 → 43225df35)

| Area | Change | Effect on shipped builds |
|---|---|---|
| Home | `people_note_door` gets HumanPlaceNoteBody; joined human/Place openings (backend); degradation notice after value | None: all internal |
| Places | `placesPageRenderItems` mixed order; `placesWorkspaceScope` / Styles extraction | None: governed only; the fallback equals today's layout |
| Venue page | Split into route orchestration + `VenueCompatibilityContent` | None. **The ungated note doorway is still present** (line 1765). |
| Life | `RootFloatingHeader` + `HeaderActionCapsule`; `ProductiveHeader` on the readers | Chrome only |
| Plans | Plan hook extraction; about 1.47k LOC of retired Trips-home styles deleted | None |
| Share capture | `useIntakeCaptureOrigin` hook, `LegacyCaptureReceipt` split | None |
| API | Generated schema projections replace copied enums; unused invitation and narration clients removed; query-key ownership centralized | None |

**Prior claims re-verified as still true at 43225df35:**
- every profile is legacy
- the Life tab is unconditional
- `PlacesRootV2Screen` is orphaned
- the Places root ignores `placeSlug`
- the site visit check is a dead end by default
- `useCreateBookingSession` has no callers
- the tripless crown shows "In motion"
- `PeopleLineSheet` is rebuild-only
- the Life Return block has no producer
- the chat header says "Vesper"
- the card catalog is unchanged

**Correction to the prior notes.** `GroupComposerContextBar` ("Everyone sees this · @Vesper to ask") is not rendered: it has no importer.
