---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No record showed what the merged baseline actually renders and does on a device in the default shell, the internal four-root build and against a real local backend, so the product map had design intent without runtime ground truth.
promotes_to: null
supersedes: []
---

# Build Map — Runtime Inventory of the Merged Baseline

This is the runtime half of the Design Atlas × Build Map. I ran the merged
baseline in an isolated lane on an iPhone 16 simulator and recorded what every
reachable surface renders and does. The runs covered:

- **Pass 1:** the internal four-root build (Home · Chat · Places · Life), mock API.
- **Pass 2:** the default/legacy shell (Plans · Vesper · Places · Life), mock API.
- **Pass 3:** the internal build against a real lane-local backend, as a fresh user.

Screenshots referenced below are relative to this file, under `screens/`.

## 0. Bottom line

1. **The four-root shell works as a navigable product rehearsal.** Home renders all 7 registered postures, Places is rich across personas, Life and the rebuilt object page are reachable. The data is mock fixtures; the real local backend supplies only a thin cold-start read.
2. **Chat's composer is missing on both roots.** The Chat/Vesper root renders an **empty composer panel** in every build tried (internal, legacy, real-local). The input node is absent from the view hierarchy. Threads opened elsewhere have a working composer.
3. **Four flows are broken:**
   - **Life:** all four lenses show the same single entry, and opening it says "That record entry is no longer available".
   - **Original reader (mock):** it raises a red-box error (a `mock://` URL fetch) and hangs on "Opening original…".
   - **Legacy Plans, Dev persona:** the mock plan builder crashes with a **render error**, persistently.
   - **Home → Chat:** handoff loses origin context (a generic new chat).
4. **Promised items are missing.** The adopted design shows three things the baseline does not have:
   - received originals or friend notes on Home (not in any baseline mock; the scenarios live only in the unmerged home-value-delivery lane);
   - Home's "Today, in order" sequence;
   - Life's reflections and windows.

   On the entity page, the plate, byline and closing row are missing, and the verbs are misaligned.
5. **Naming is inconsistent in the four-root build.** Copy still says Trips, Atlas, Discover and Vesper where the roots are Home/Chat/Places/Life: "Ask Vesper", "The itinerary stays in Trips", search chip "Atlas", notification filters "Trips / Vesper", "Ready for Atlas", "the context you carried from Discover".
6. **The QA harness has rotted.** Many registered polish flows boot-wait on retired tab labels ("Discover", "Trips", "Plans", "Vesper"), and some assert superseded screens (Trip settings, the itinerary day spine under `PLAN_SHAPE`). The registry cannot currently certify either shell as registered. I used boot-label-patched scratch copies to see the surfaces.
7. **Setup notes.** The requested 09-26 dev client **does not match** the merged JS (worklets 0.7.4 vs 0.12.1); I used the 09-22 build. The baseline backend **cannot start offline** without a placeholder `ANTHROPIC_API_KEY` and a `DEFAULT_DEV_USER_ID`; the fix is unmerged. Maps are blank everywhere because no Mapbox token was used.

## 1. Environment, commands and evidence boundary

### 1.1 Revisions, device and tools

| Item | Value |
|---|---|
| Lane | `/Users/feihuyan/travel-workspace--product-map-inventory`, branch `codex/product-map-inventory` in all three repos (merged baseline) |
| Workspace / travel-agent / travel-app HEAD | `6ef3dca` / `c8c9f5785` / `43225df35` (all PR merges of `codex/home-human-opening-recovery-2026-09-23`) |
| Lane runtime | Compose project `vesper-product-map-inventory`; Postgres 61185, Qdrant 61186/61187, API 61188, Metro 61189 (`scripts/dev.sh --print-runtime`) |
| Device | iPhone 16 simulator `8F8C549C-950C-47D2-AA98-483A91EFEA24`, iOS 18.2; recorded as `runtime.device` in the lane's gitignored `.workspace-lane.json`. No other simulator was touched |
| Host | macOS 26.5, Xcode 26.5, Node 24.13.0, npm 11.6.2, Maestro 2.6.1, OpenJDK 21.0.5, Python 3.13.0, Docker 27.4.0 |
| App JS deps | `npm ci` in lane `travel-app` (1581 packages; `patch-package` applied `metro-runtime`) |
| Backend deps | `python3.13 -m venv .venv && pip install -r requirements-dev.txt` in lane `travel-agent` |

### 1.2 Native binary: the 09-26 build does not match the merged JS

The suggested 2026-09-26 17:37 dev client
(`DerivedData/TravelApp-angxhoejyrnhvheftxcnyqfsfzsz`) was built from
`travel-workspace--home-value-delivery/travel-app/ios`. That checkout has an
**uncommitted** `package.json`/`Podfile.lock` change that pins
`react-native-worklets` 0.7.4 and `react-native-reanimated` 4.2.1. The embedded
version strings in `TravelApp.debug.dylib` are `0.7.4`. The merged baseline JS is
worklets **0.12.1** / reanimated **4.6.0**, so that binary is not valid for this
lane.

The 2026-09-22 15:02 build (`TravelApp-fltftocqdpqxckffuohgyezouvsg`, built from
the since-removed `functional-implementation-2026-09-20` lane) embeds
worklets `0.12.1`, reanimated `4.6.0`, RN `0.83.10`. The only `package.json`
change since 09-20 is `ef86daa75 fix(deps): patch parser vulnerabilities without
native upgrades`, and `modules/`, `ios/`, `app.json`, `app.config.js` are
unchanged since 09-20. I uninstalled the stale 08-13 app on the iPhone 16 and
installed the 09-22 build. No native rebuild was attempted (it needs the
unavailable Mapbox download token).

### 1.3 Metro configurations (environment only; no repo file changed)

The lane has no `.env`; every flag was passed as a process environment variable.
Metro always ran from the lane `travel-app` with `npx expo start --dev-client
--port 61189 --clear` and was reachable on `127.0.0.1:61189` (it listened on
`*:61189`). The dev client was pointed at it with
`xcrun simctl openurl <udid> "exp+travel-app://expo-development-client/?url=http%3A%2F%2F127.0.0.1%3A61189"`.

| Pass | Flags |
|---|---|
| **P1 internal four-root (mock)** | `EXPO_PUBLIC_USE_MOCK_API=true`, `EXPO_PUBLIC_SKIP_AUTH=true`, `EXPO_PUBLIC_IS_INTERNAL_BUILD=true`, `EXPO_PUBLIC_FOUR_ROOT_SHELL=true`, `EXPO_PUBLIC_ROOT_PROJECTION_V2=true`, `EXPO_PUBLIC_PLACES_ROOT_V2_RENDERER=true`, `EXPO_PUBLIC_LIFE_ROOT_V1=true`, `EXPO_PUBLIC_RELATIONSHIP_UUID_HANDOFFS_ENABLED=true`, `EXPO_PUBLIC_OBJECT_PAGE_REBUILD_ENABLED=true`, `EXPO_PUBLIC_PLAN_SHAPE_ENABLED=true`, `EXPO_PUBLIC_LIFE_REFIND_LANE=true`, `EXPO_PUBLIC_API_URL=http://127.0.0.1:61188` (unused in mock) |
| **P2 default / legacy (mock)** | `EXPO_PUBLIC_USE_MOCK_API=true`, `EXPO_PUBLIC_SKIP_AUTH=true`, `EXPO_PUBLIC_API_URL=http://127.0.0.1:61188`. No internal or rollout flags. `__DEV__` (dev client) still registers `guide://dev/*` routes |
| **P3 real local (internal four-root)** | P1 flags with `EXPO_PUBLIC_USE_MOCK_API=false` against the lane API |

`EXPO_PUBLIC_MAPBOX_TOKEN` was deliberately **not** set: the only token on disk
is in the canonical checkout's `.env.local` and belongs to a real account. Every
map therefore renders its no-token fallback. Map emptiness below is an
environment limit, not a product finding.

### 1.4 Capture harness

- **Doctor:** `VESPER_METRO_URL=http://127.0.0.1:61189 node scripts/polish-qa/run-polish-qa.mjs home-root --device="iPhone 16" --doctor` passed (Maestro 2.6.1, Java `/opt/homebrew/opt/openjdk@21`). `bootedDeviceUdid("iPhone 16")` resolved exactly `8F8C549C…`; the regex is anchored, so it cannot select "iPhone 16 Pro".
- **Registered runner:** `run-polish-qa.mjs <surface> --device="iPhone 16" --flow-timeout-ms=240000` for `home-root`, `places-workspace`, `you-portrait`, `trip-itinerary`, `proposal-detail`, `vesper-home`, `discover-home`, `universal-search`, `external-sharing`, `notifications-alerts` (run folders under the lane's `travel-app/.maestro/runs/20260926T22*`–`23*`).
- **Stale boot labels (harness finding):** many registered flows boot-wait on tab labels that no longer exist in *either* shell. Of 188 registered captures, flows for 20 surfaces wait on `"Discover"` (retired tab), 10/16 `vesper-chat` captures wait on `"Vesper"`, several wait on `"Trips"` or `"Plans"`, and `trips-home`, `entity-object` and some `header-system` flows require the legacy Trips Home ids. In the four-root build they fail before reaching the surface; `"Discover"` and `"Trips"` fail in the legacy build too.
- **Mini-runner:** to still see those surfaces, I copied `.maestro/` to the scratchpad and replaced only the boot `extendedWaitUntil: visible: "Discover"|"Plans"|"Vesper"|"Trips"` with `"Places"` (a label present in both shells). 130 boot waits in 98 files were patched; no assertion or navigation step was changed. A scratch `minirun.mjs` reproduces the runner's exact sequence (terminate → seed AsyncStorage `dev.mockModeOverride/activePersonaId/mockNowMs=1780502400000` → `assert-polish-mock-ready` → terminate → reseed → `maestro test --udid 8F8C549C…`). Repo files were not modified. Results from patched flows are marked **(patched boot)** below.
- Screenshots were copied at half resolution (JPEG q82, 590×1278) into `screens/`. Full-resolution originals remain in the lane run folders and the scratchpad for this session only.

### 1.5 Backend (Pass 3)

```sh
# lane travel-agent
COMPOSE_PROJECT_NAME=vesper-product-map-inventory POSTGRES_HOST_PORT=61185 \
  QDRANT_HOST_PORT=61186 QDRANT_GRPC_HOST_PORT=61187 \
  docker compose -p vesper-product-map-inventory up -d --wait
DATABASE_URL=postgresql://vesper:<local>@localhost:61185/vesper PYTHONPATH=. \
  AI_MODE=off WEB_SEARCH_MODE=off .venv/bin/python -m alembic upgrade head   # to irdelegationtypes01
AI_MODE=off WEB_SEARCH_MODE=off DISABLE_LLM_BACKGROUND_LOOPS=true SKIP_AUTH=true \
  DEFAULT_DEV_USER_ID=<synthetic lane user> ANTHROPIC_API_KEY=<non-secret placeholder> \
  QDRANT_URL=http://localhost:61186 .venv/bin/python -m uvicorn backend.api.main:app --host 127.0.0.1 --port 61188
```

Two startup gates blocked a plain offline start on this baseline:

1. `ANTHROPIC_API_KEY` is required even with `AI_MODE=off` (`backend/api/lifecycle.py:45`). The relaxation is backend `6c792ed8b`, which is **not merged** (it lives in the home-value-delivery lane). I set a non-secret placeholder string. `AI_MODE=off` blocks provider calls in `backend/core/ai_mode.py` before any key use.
2. `SKIP_AUTH=true` requires `DEFAULT_DEV_USER_ID`. I inserted one synthetic lane-only user (`product-map-inventory-qa@example.invalid`), recorded its id, and removed it at the end (see §9).

The API then reported `{"status":"ok"}`. Startup logged two non-fatal gaps: `sentence_transformers` is not installed (legacy embeddings) and the Qdrant collection `experience_briefs` does not exist in the empty lane Qdrant. No seed or eval fixtures were loaded.

### 1.6 What worked and what was blocked

- **Worked:**
  - lane isolation (own ports, compose project, simulator);
  - `npm ci`;
  - the backend venv;
  - compose up and migrations to `irdelegationtypes01`;
  - the polish-QA doctor;
  - the runner on its native terms;
  - the patched-boot mini-runner;
  - direct deep-link captures via `guide://dev/screenshot-mode?persona=…&to=…`;
  - the real local API as a fresh synthetic user.
- **Blocked or degraded:**
  - the 09-26 binary (version skew; §1.2);
  - native rebuild (no Mapbox download token);
  - maps (no public token used);
  - offline backend start without placeholders (§1.5);
  - registered flows on retired labels (§7);
  - registered legacy-pass flows, which were too slow (≈6 min per capture while another session's `make` and `maestro check-syntax` shared the machine), so Pass 2 used direct captures;
  - `dev/onboarding`, which reloads the bundle;
  - the original reader in mock mode (red box).

## 2. Capability → observed status

Status vocabulary:

- **works:** renders and the exercised interaction does what it says.
- **renders, defects:** usable, with the listed visual, copy or data problems.
- **broken:** the primary job fails.
- **empty:** renders an honest empty or fallback state only.
- **not reachable:** no built route or fixture leads to it in this baseline.
- **not built:** no implementation observed.

"Mock" means the in-app mock API. "Real-local" means the lane backend with a fresh synthetic user.

| # | Capability | Build | Data | Observed status | Evidence |
|---|---|---|---|---|---|
| 1 | Four-root tab shell (Home · Chat · Places · Life) | internal | mock | **works** | `home-root/*`, `explore-internal/ex-*` |
| 2 | Legacy shell (Plans · Vesper · Places · Life; Vesper FAB) | default | mock | **works**. Life is a tab in both shells | `default-shell/df-plans-*.jpg` |
| 3 | Home v2: 7 postures (available, planning, live, returned, quiet, cold, urgent) | internal | mock | **renders, defects**: fixed Sep 1 date, static week strip, incoherent live copy, "Canonical outcome" caption, placeholder cliff comparison | `home-root/home-root-*.jpg` |
| 4 | Home crown (one dominant) + labelled regions + rest close | internal | mock | **works** (one crown per posture; honest close) | same |
| 5 | Home "Today, in order" timed sequence (design Home 02) | — | — | **not built** (no owner contract, per Codex receipt) | — |
| 6 | Received original / friend's note on Home | internal | mock | **not reachable** (no baseline persona is the mock recipient; social scenarios unmerged) | §3.2, §3.8 |
| 7 | Original-delivery reader | internal | mock | **broken**: `mock://` content fetch → red box; stuck "Opening original…" | `explore-internal/ex-original-delivery-reader*.jpg` |
| 8 | Home → Places ("Open in Places") | internal | mock | **works** (opens Places) | `home-root-available.jpg` |
| 9 | Home → Life ("Open in Life") | internal | mock | **renders, defects**: lands on Life root, not the named outcome | `explore-internal/ex-life-time-from-home-open-in-life.jpg` |
| 10 | Home → Chat ("Ask Vesper") with origin context | internal | mock | **broken** (generic new chat, no context) | `explore-internal/ex-chat-from-home-ask-vesper.jpg` |
| 11 | Chat / Vesper root composer | both + real-local | mock/real | **broken**: empty panel, no input node | `vesper-home/internal-chat-*`, `default-shell/df-vesper-tab-*.jpg`, `real-local/rl-chat.jpg` |
| 12 | Chat root workbench (read line, NOW card, open threads) | both | mock | **renders, defects** (legacy "Trips" seam copy; "Day 115" counter with wall clock) | `vesper-home/*` |
| 13 | Private chat thread (opener, markdown, research companion, interrupted, failed, stale) | internal | mock | **renders, defects** (header has no backing, so text runs under it; duplicate failure copy) | `vesper-chat/*.jpg` |
| 14 | Group trip chat ("Message everyone…") | internal | mock | **works** | `vesper-chat/vesper-chat-trip-scoped.jpg` |
| 15 | Chat artifact gallery (place/plan/decision/reaction states) | — | mock | **not run** (flows need legacy Trips Home; not re-run in the legacy pass for time) | — |
| 16 | Place page → Ask Vesper with venue context | internal | mock | **works** (auto-sends prompt with "Venue context" chip; reply cites "Discover") | `explore-internal/ex-chat-from-place-ask-vesper.jpg` |
| 17 | Places workspace (governed runtime) across personas | internal | mock | **works** (rich); legacy "Trips" copy; empty media tiles | `places-workspace/*.jpg` |
| 18 | Places in default build | default | mock | **works** (same renderer and content as internal) | `default-shell/df-places-tab-default.jpg` |
| 19 | Places map | both | mock | **empty** (no Mapbox token): blank plus "Not much here yet" | `explore-internal/ex-places-map-default.jpg` |
| 20 | Places saved / reading lists | internal | mock | **works** (all "Hours unverified", pin placeholders) | `ex-places-saved-default.jpg`, `ex-places-reading-default.jpg` |
| 21 | City page `/place/lisbon` (hero + "Vesper on Lisbon · 4 lenses") | internal | mock | **renders, defects** (kicker in status-bar zone) | `explore-internal/ex-place-city-lisbon.jpg` |
| 22 | Entity object page rebuild (venue/site/experience) | internal | mock | **renders, defects**: verbs misaligned, "ADJUDICATED/CATALOG" exposed, no plate/byline/closing row; experience nearly empty | `entity-object/*.jpg`, `ex-place-open-from-places.jpg` |
| 23 | Legacy venue page (Add to trip, Peak / Great for / Not ideal) | default | mock | **renders**, "No dossier available." | `default-shell/df-venue-legacy.jpg` |
| 24 | Life root with 4 lenses (Time · Places · Threads · People) | both | mock | **renders, defects**: all lenses identical (1 entry), "1 RECORDS", not persona-aware | `explore-internal/ex-life-*-lens.jpg`, `ex-life-elif-time.jpg` |
| 25 | Life entry → record | internal | mock | **broken**: "That record entry is no longer available" above the same entry; row inert | `explore-internal/ex-life-entry-southern-italy.jpg` |
| 26 | Life reflections, windows, dossiers, Vault | — | — | **not built** in the root (lens row + one section + door only) | §3.7 |
| 27 | Life search (refind lane) / Life groups | internal | mock | **empty** (honest empty states) | `ex-life-find.jpg`, `ex-life-groups.jpg` |
| 28 | Life on real backend | internal | real-local | **empty** ("The record is still taking shape.") | `real-local/rl-life.jpg` |
| 29 | Plan page, internal Plan Shape | internal | mock | **renders, defects**: "deciding"/"nothing booked" counted SETTLED; multi-day list under Day 1; trip dates differ across surfaces | `trip-itinerary/internal-planshape-plan-day-top.jpg`, `ex-plan-lisbon-planshape.jpg` |
| 30 | Plan page, legacy day spine | default | mock | **works** (Lisbon Thu 15/Fri 16, PROPOSED block, DECISION row) | `default-shell/df-trip-lisbon-itinerary.jpg` |
| 31 | Legacy Plans home for Dev persona | default | mock | **broken**: Render Error `plan.canonical?.envelope.projection_version` (`utils/api/mock/tripsPlan.ts:1768`) | `default-shell/df-plans-dev.jpg`, `df-plans-error-boundary.jpg` |
| 32 | Legacy Plans home, other personas | default | mock | **works** (trip crown, Vesper line, also-in-play, connect) | `default-shell/df-plans-*.jpg` |
| 33 | Plans FAB → chat | default | mock | **works** (auto-sends "Help me start a new trip.") | `default-shell/df-plans-fab-tap.jpg` |
| 34 | Proposal detail + receipt family | internal | mock | **renders, defects** (inspect-recovery toast; title/body mismatch) | `proposal-detail/*.jpg` |
| 35 | Group vote on Porto decision | internal | mock | **broken** (vote actions absent; "no mock member authority" error) | Metro log; flow fail |
| 36 | Booking provider states (10 states) | internal | mock | **works** (dense; currency and party-size inconsistencies) | `booking/*.jpg` |
| 37 | Trip costs ledger / expense detail | internal | mock | **renders, defects** (no planning estimate for Elif; add/OCR flows fail) | `trip-costs/*.jpg` |
| 38 | Trip stay list / detail | internal | mock | **renders, defects** (blank map; split-stay fixture shows missing) | `trip-stay/*.jpg` |
| 39 | Trip settings / archive-blocked sheet | internal | mock | **works**; registered flows stale ("Trip settings" → "Settings") | `trip-settings-admin/*.jpg`, `ex-trip-settings.jpg` |
| 40 | Trip map (route preview) | internal | mock | **empty** (no-token fallback; header overlap) | `trip-map/trip-map-default.jpg` |
| 41 | Trip changes history | internal | mock | **empty** ("Nothing has changed yet.") | `trip-changes/*.jpg` |
| 42 | Trip creation | internal | mock | **works** | `trip-creation/*.jpg` |
| 43 | Trip story (memory) | internal | mock | **renders, defects** ("Ready for Atlas"; mismatched stock photo) | `trip-story/*.jpg` |
| 44 | Invite landing, manual code, invalid code | internal | mock | **works** | `auth-invite/*.jpg`, `external-sharing/external-sharing-invite.jpg` |
| 45 | Public / shared pages (story, unavailable, network, proposal and Unpacked doorways, owner controls) | internal | mock | **works** (story links on `travelagent.app`) | `external-sharing/*.jpg` |
| 46 | Notifications (global, trip updates, trip-scoped, personal) | internal | mock | **works**; legacy filter names | `notifications-alerts/*.jpg` |
| 47 | Universal search (results, trip scope, ask, no results, offline) | internal | mock | **works** 6/7; "Atlas" chip; blank empty state; Nearby missing | `universal-search/*.jpg` |
| 48 | You / profile | internal, real-local | mock/real | **works** | `you-portrait/*.jpg`, `real-local/rl-you.jpg` |
| 49 | Trust controls (account, privacy, constraints, data receipt, autonomy) | internal | mock | **works** | `trust-controls/*.jpg` |
| 50 | Onboarding | internal | mock | **renders, defects** (gift, permission and decline seen; earlier steps not captured because of a dev reload) | `onboarding/*.jpg` |
| 51 | Photo intake | internal | mock | **empty** on simulator; action-state gallery works | `photo-media-intake/*.jpg` |
| 52 | Share capture (`/share-capture`) | internal | — | **empty** ("Nothing to share"); share extension not exercised | `explore-internal/ex-share-capture.jpg` |
| 53 | Guide reader / dossier reader states | internal | mock | **renders, defects** (duplicate "Saved"; kicker overprint in error) | `guide-reader/*.jpg`, `discover-detail-reader/*.jpg` |
| 54 | Discover root | both | — | **not reachable** (redirects to Places) | `default-shell/df-discover-redirect.jpg` |
| 55 | Atlas root and readers | both | mock | **not reachable** (tab → Life); `/you/atlas/memory` still renders | `explore-internal/ex-atlas-tab-redirect.jpg`, `atlas-memory/*.jpg` |
| 56 | Home v2 on real backend (fresh user) | internal | real-local | **renders, defects**: "The week is open", crown = "Anywhere / Anywhere", partial-read banner | `real-local/rl-home.jpg` |
| 57 | Places v2 on real backend (fresh user) | internal | real-local | **empty/fallback**: "Nothing leads this field yet… No eligible World Field signal" | `real-local/rl-places.jpg` |
| 58 | Chat root on real backend | internal | real-local | **renders, defects**: "Reading your trips…" line; 3 US national-park seasonal rows; blank composer | `real-local/rl-chat.jpg` |
| 59 | Home/Places rehearsal preflight (dev) | internal | real-local | **empty**: "Expected fixture account required" | `real-local/rl-rehearsal.jpg` |
| 60 | Dev galleries (controls, profile system, workbench, canonical artifacts, headers, surface census, four-root portfolio) | internal | mock | **works** (canonical-artifact label overprint) | `control-system/`, `profile-system/`, `native-design-workbench/`, `canonical-artifact-gallery/`, `header-system/`, `explore-internal/ex-dev-*` |

## 3. Pass 1 — internal four-root build, mock API

All data in this pass is the in-app mock (`MOCK DATA — NOT THE REAL BACKEND`
banner unless a flow hides it). Registered-flow results use the runner's
definition of success: the flow passes *and* every declared screenshot exists.
Images are under `screens/<surface>/`; exploratory images are under
`screens/explore-internal/`.

### 3.1 Registered capture results (Pass 1)

| Surface (registry id) | Captured | How | Why the rest failed |
|---|---|---|---|
| `home-root` | **7/7** | runner | Quiet needed one retry (driver) |
| `places-workspace` | **8/8** | runner | — |
| `you-portrait` | **4/4** | runner | — |
| `entity-object` | **3/3** | patched boot | Registered flows wait for `"Plans"`; fail as registered in four-root |
| `external-sharing` | **7/7** | patched boot (runner got 5/7) | `"Discover"` boot label |
| `notifications-alerts` | **4/4** | patched boot (runner got 0/4) | `"Discover"` boot label |
| `auth-invite` | **3/3** | patched boot | — |
| `trip-creation` | **3/3** | patched boot | — |
| `trust-controls` | **5/5** | patched boot | — |
| `trip-changes`, `trip-map`, `trip-story`, `guide-reader`, `profile-system`, `control-system`, `native-design-workbench` | **1/1 each** | patched boot | — |
| `booking` | 10/11 | patched boot | provider-pending chat card: `"Provider pending"` not visible |
| `vesper-chat` | 11/16 | patched boot | 3 artifact-gallery flows need legacy Trips Home; `planning-progress` fixture text missing; `history` header id missing |
| `universal-search` | 6/7 | runner | Nearby: expected `Copenhagen Coffee Lab` row absent |
| `trip-stay` | 4/5 | patched boot (`Trips` label also patched) | Elif Rome: `trip-accommodations-screen` never appears |
| `discover-detail-reader` | 4/6 | patched boot | default dossier: boot needed `Places` inside a hidden-nav reader; not-found angle copy differs |
| `trip-costs` | 4/7 | patched boot | Elif estimate row id missing; add/edit actions and receipt OCR fixture text missing |
| `vesper-home` (Chat root) | 3/6 | runner | cold copy differs; keyboard: composer input missing; seam needs legacy Trips Home |
| `single-trip-interactions` | 2/4 | patched boot | Elif stay screen id missing; Porto vote actions absent (`Trip persona-urgent-porto has no mock member authority` error in Metro log) |
| `proposal-detail` | 1/2 | runner | lazy-consensus crop id missing (8/8 receipt-family images captured) |
| `places` | 1/2 | patched boot | `discover-trip-continuity`: `Add to trip` absent |
| `photo-media-intake` | 1/2 (23 images) | patched boot | retag sheet title differs |
| `onboarding` | 1/1 (7/8 images) | patched boot | dev route triggers a JS bundle reload, so 5 images are blank white or "Downloading 100%" |
| `illustration-product-states` | 0/5 (4 full images) | patched boot | art-crop ids missing; begin-orient (Discover) and arrive-settle not reached |
| `trip-settings-admin` | 0/10 (2 images) | patched boot | the screen is titled **Settings**; every flow waits for **Trip settings** |
| `trip-itinerary` | 0/6 (1 image) | runner | internal `PLAN_SHAPE_ENABLED` replaces the day spine the flows assert |
| `discover-home` | 0/3 | runner + patched | Discover is a redirect to Places; the flows assert the retired Discover screen |
| `saved-collections` | 0/1 (1 image) | patched boot | `Add to trip` absent |
| `canonical-artifact-gallery` | 0/1 (1/3 images) | patched boot | flow expects the dev-client launcher on port 8081 |
| `atlas-memory` | 1/1 | patched boot | — |
| `atlas-home`, `atlas-receipt`, `atlas-archive` | 0 | patched boot | Atlas tab redirects to Life; these ids no longer exist. `atlas-board/compose/kept/review` were not run |
| `header-system` | 8/14 (header gallery only) | patched boot | remaining header flows were not run (time) |
| `life-root`, `canonical-artifact-reader` | — | — | no registered captures exist |

### 3.2 Home (four-root "Home" tab) — `screens/home-root/`

Seven registered postures all render the same stable skeleton:

- a date kicker;
- a serif headline, the "world read";
- one crown card;
- a Mon–Sun week strip;
- zero or more labelled regions (`COMING UP`, `IN MOTION`, `WORTH KNOWING`, `CARRIED FORWARD`);
- a closing line, "That is everything that earns your attention here. The rest keeps."

This matches the contract's selective foreground: one crown, and no generic
recommendations. The fixtures have several defects:

- **Available** (`home-root-available.jpg`): crown "Saturday has a water route" → *Open in Places*; Worth knowing "Sorrento's cliff has a New York counterpoint" → *Open in Life*. The closing text is partly behind the floating nav in the capture.
- **Planning** (`home-root-planning.jpg`): crown "Brooklyn Saturday needs a meeting point" (PENDING) → *Ask Vesper*; Coming up repeats the water-route card.
- **Live** (`home-root-live.jpg`): headline "Brooklyn is the live edge of **tonight**", but the crown says "held for **Saturday** evening" on a page dated **Tuesday**. The temporal read is incoherent.
- **Returned** (`home-root-returned-top.jpg`, `home-root-returned-close.jpg`): crown "Recorded outcome — Nice, Sorrento, Amalfi, and Rome remain available for refinding" with the internal caption **"Canonical outcome"**, and the placeholder comparison "Sorrento's cliff has a New York counterpoint". Codex later removed both in unmerged commits `a963fa0b9` and `42cba2d30`/`7d7d5b762`.
- **Quiet** (`home-root-quiet.jpg`): ends with *NOTHING ELSE WAITS*. It still carries a second card, "An attention kept moving", that repeats the same connection.
- **Cold** (`home-root-cold.jpg`): one invitation, "Start with what is already near you", then the close. It is honest but very thin.
- **Urgent** (`home-root-urgent.jpg`): red headline "The ferry failed; the road alternative is held". The crown stacks two status labels, "Still taking shape" and "PENDING"; the close reads "Everything else can wait while this is repaired."
- **Across all postures:**
  - Every fixture is dated **Tuesday, Sep 1**, although the runner's mock clock is 2026-06-03.
  - The week strip is identical in all seven: Tue *home*, Thu *route*, Sat *dinner*. That includes the cold-start user with nothing planned. The strip is a static fixture, not posture-derived.
  - The CTA on the Home planning, live, cold and urgent crowns reads **"Ask Vesper"**, although the tab is named **Chat**.

Comparison with design intent: the adopted Home 02 "ordinary" board includes a
timed *Today, in order* sequence and a received note from a friend. Neither
exists in any built posture. Codex's receipt records the sequence as a missing
owner contract. **No received original or friend's note appears on Home in
the merged baseline.** The `home-root-social-*` scenarios and the
`home-original-recipient` fixture exist only in the unmerged home-value-delivery
lane.

### 3.3 Chat root (four-root "Chat" tab, `vesper-home`) — `screens/vesper-home/internal-chat-*`, `screens/explore-internal/ex-chat-root-*`

- **The composer is blank.** The docked "ask" band above the tab row renders as an empty glass panel. It has no input, placeholder or send button, both in every registered capture and after an ordinary tab tap (`ex-chat-root-tab.jpg`). Tapping the panel does nothing (`ex-chat-root-tap-composer.jpg`). The `vesper-home-keyboard` flow fails because `vesper-home-composer-input` does not exist. The contract's first Chat obligation ("one prominent multimodal composer") is therefore unmet in the four-root build. A Maestro hierarchy dump shows the `vesper-composer` container laid out at `[20,683][372,760]` with **no children**: the focus-scoped `dockAccessory` (`app/(tabs)/concierge/index.tsx:168–202` → `useFloatingNavDockAccessory`) never mounts into `FloatingTabBar`. The same blank panel appears on the legacy **Vesper** tab (§4) and against the real local API (§5), so the cause is not shell-specific. I did not determine whether it comes from the JS or from the 09-22 binary, because no fresh native build was possible.
- The page is a session workbench headed "A few threads are taking shape", with a "NOW Lisbon" card and an "OPEN WITH VESPER · 3 OPEN" thread list. Quiet shows "Your next trip is close." and five fading ghost prompts. The contract allows concrete, state-aware ways in, but this list leans toward an inbox.
- The seam state (urgent) still says "One thing needs you in **Trips**" / "Open in **Trips**" inside a shell that has no Trips root.
- With the wall clock (exploration), the header read "LISBON · **DAY 115**" for a Jun 4–10 trip. The day counter does not clamp to the trip.

### 3.4 Chat threads — `screens/vesper-chat/`

- Private thread (`vesper-chat-default.jpg`): header "Vesper · private", Vesper opener, user bubble, composer "Message Vesper…". Clean and calm.
- Planning shape, trip-scoped group room ("Lisbon" + avatars, composer "Message everyone…"), long markdown response, research companion card ("VESPER RESEARCH · LIVE — Explore this place"), interrupted ("You stopped me here — I kept what I'd written"), failed and retry, and stale-plan recovery ("Try from latest") all render. So do the XXXL and AX-medium Dynamic Type variants.
- **Visual bug:** the chat header has no backing surface. When a transcript is scrolled, message text runs under the back button and status bar (`vesper-chat-planning-shape.jpg`, `vesper-chat-long-response.jpg`, `ex-chat-thread-from-root.jpg`), and the "Latest" pill covers text.
- Failed and retry repeats the failure twice: "I couldn't finish that comparison." followed by the red "Vesper couldn't finish that reply."
- **Chat from an object:**
  - *Place page → Ask Vesper* (`ex-chat-from-place-ask-vesper.jpg`) opens a private thread. It auto-sends "What should I know before going?" with a **Venue context** chip. Vesper replies that it has Cervejaria Ramiro "in focus… the context you carried from **Discover**". Context is carried, but the copy names the retired Discover surface, and the prompt is sent without a review step.
  - *Home crown → Ask Vesper* (Ben planning, `ex-chat-from-home-ask-vesper.jpg`) opens a **generic** new private chat ("Hey — let's figure this out. Where are you thinking?"). It carries no reference to "Brooklyn Saturday needs a meeting point", which contradicts the §9 handoff contract that Home openings reach Chat with origin context.

### 3.5 Places (four-root "Places" tab) — `screens/places-workspace/`, `screens/places/`, `screens/explore-internal/ex-places-*`

- The governed Places workspace renders well across personas:
  - No trip (saved list): "Start with what pulls you."
  - Lisbon today: guide card, saved list, "In trip" badges.
  - Kyoto planning, Mexico City live.
  - Lisbon planning with "BOOKING HOLD EXPIRES SOON / Book" and "YOUR GROUP NEEDS YOUR DECISION / Open", then "OPEN TIME ON DAY 1 — Add to Day 1".
  - Rome returned: "How was Rome? Answer privately", plus an "On this day" memory.
  - Cold start: "4 to start with" editorial guides.
  - Depth sections: experiences, neighbourhoods.
  - Search loading skeleton.
- Places lead copy says "The itinerary stays in **Trips**" in the four-root build.
- Places without media get an empty pin tile (Inoda Coffee, Pompette, Mesa de Frades, and the entire Saved list).
- `places-workspace-lisbon-urgency` and `-lisbon-decision` are pixel-identical first viewports; the registry treats them as different scenarios.
- The Returned state asks for private reflection ("How was Rome?"). The contract excludes reflection prompts from Home, but it is silent on Places.
- **Map** (`ex-places-map-default.jpg`): with no Mapbox token the map is blank. It shows "Not much here yet — Vesper hasn't rated many places here", although six places are saved in Lisbon. The copy blames supply rather than the map.
- **City page** `/place/lisbon` (`ex-place-city-lisbon.jpg`): the art hero "Lisbon — 6 spots saved, a relationship in the making" is followed by "VESPER ON LISBON · 4 LENSES" reading cards (Insider, Your affinity, A ritual). The "YOUR PLACES" kicker sits in the status-bar/Dynamic Island zone.
- Captures that push a detail screen (`places-default.jpg`, `saved-collections-default.jpg`) caught the push mid-animation. The previous page is visible at the left edge. This is the same transition-timing artifact as `global-chrome-collapsed.jpg`, where Home appears twice side by side.

### 3.6 Place / entity object page (rebuild) — `screens/entity-object/`, `screens/explore-internal/ex-place-open-from-places.jpg`

`OBJECT_PAGE_REBUILD_ENABLED` routes `/venue/1`, `/site/…` and `/experience/…`,
and taps from Places, to the rebuilt page. Its layout:

- header glass chips: photos, bookmark (= Keep place, filled when saved), share;
- a kicker, "RESTAURANT · LISBON";
- a sans title and neighbourhood;
- a two-cell fact pair, "TABLE — Walk-ins usually work" / "NOW — Open now";
- provenance labels "CATALOG" and "**ADJUDICATED** · AUG 11", which expose backend vocabulary to the reader;
- serif body prose;
- two verbs, "Check a visit now" and "Ask Vesper →", which are **misaligned** (the second sits indented on its own line instead of in a verb row);
- a WHERE row with a tiny map thumbnail (no tiles; Mapbox logo and scale bar only).

The museum site page shows "Works in rain / Closed now" and an access line. The
experience page is nearly empty (title, one sentence, verbs, "Where: Lisbon").
Against design E06 (plate, kicker, byline, pair, verbs, closing row, where row),
the build has **no plate image, no byline and no closing row**, and the verbs
are not a rail.

### 3.7 Life (four-root "Life" tab; Life is visible in both shells) — `screens/explore-internal/ex-life-*`

- The root shows "What your record is holding now." with lens tabs Time · Places · Threads · People, then one section, a "The full record, by time → 1 RECORDS" door and "EVERYTHING ELSE STAYS IN THE RECORD".
- **All four lenses show the identical single entry**, "Southern Italy — A journey held in the record". They do not reorganise anything. The count reads "1 RECORDS".
- The same one entry appears for every persona tried: default Alex and Elif, whose Places are Istanbul-specific. The Life mock is not persona-aware.
- **Broken return:** tapping the entry opens *Life record* with the banner "THAT RECORD ENTRY IS NO LONGER AVAILABLE. The rest of your record is still here.", directly above the same entry (Aug 14–27, 2026 · 12 kept). Tapping that row does nothing. There is no way to reach a record detail.
- The record page orders lenses TIME · PLACES · **PEOPLE · THREADS**; the root orders them Time · Places · **Threads · People**.
- Home → *Open in Life* lands on the Life root (Time lens), not on the outcome the card named.
- *Life search* (`/you/life-find`, refind lane) renders a clear empty state: "Find an original", "Your originals", "Shared with you". *Life groups* shows "No groups yet".
- Design intent (Life 01–05): lenses with 4–5 deterministic digest blocks, a scroll door, reflections and fixed windows. The build has only the lens row, one section and the door. There are no reflections, no windows, and no difference between lenses. The design atlas also says Threads is not served.

### 3.8 Received original reader — `screens/explore-internal/ex-original-delivery-reader*.jpg`

`/original-delivery/00000000-0000-4000-8000-000000000043` (the only mock id)
opens "Shared original — FROM A TRAVEL COMPANION / A note from your companion"
and stays on **"Opening original…"**. The content fetch goes to
`mock://relationships/original-deliveries/…/content`, which React Native cannot
handle. The result is a **red-box error** ("No suitable URL request handler
found for mock://…"). The reader's revalidation keeps re-raising the red box on
later screens until the app is restarted. Codex's unmerged `2840a242` routes
exact-text reads through the API owner, and `04d4ed85c` guards the polling. No
baseline persona is the mock recipient (`demo-recipient`), so Home never
surfaces the original.

### 3.9 Plan page (internal Plan Shape) — `screens/trip-itinerary/internal-planshape-plan-day-top.jpg`, `screens/explore-internal/ex-plan-lisbon-planshape.jpg`

With `PLAN_SHAPE_ENABLED`, a trip opens to a "CURRENT SHAPE" card with an *Ask
Vesper* button, instead of the day-by-day spine. That is why all 6 registered
itinerary flows fail. Problems in the Plan Shape view:

- **Kyoto** (Ben/Sarah, "Day 1 of 8"): "21 settled · 0 flexible · 0 open". Items such as "Check in — ryokan or hotel (**deciding**)" and "Dinner — easy izakaya, **nothing booked**" are labelled **SETTLED**. Times from several days appear in one list under the Day 1 header, in the order 17:00, 18:30, 19:30, then 06:00 and 09:00.
- **Lisbon** (default): "Thursday, October 15 · Day 1 of 2". Elsewhere the same trip is Jun 4–10 (Chat, invite, stay) or Apr 10–14 (shared story). It shows "0 settled · 2 flexible · 0 open" and "LUX Fragil Closing Night 00:00–08:00". It also has "2 things need your decision — View".
- The card is inset more narrowly than the page header.

### 3.10 Other trip surfaces

- **Proposal detail** (`screens/proposal-detail/`):
  - A toast, "This decision isn't available in the group chat. Opening inspect/recovery.", then an INSPECT ONLY panel with *Open group chat* and *Review in Plan*.
  - The title, "Casa do Alentejo vs Mouraria for first dinner", does not match the body, "Swap dinner to an earlier slot so the group can catch live jazz".
  - The "decision sheet" capture is identical to the page.
  - The receipt family (applied, vote, booking hold, conflict, swap, reverted, change, lazy consensus) is consistent.
- **Booking** (`screens/booking/`):
  - Ten provider-truth states are clear: finish on provider, held stay, expired fare, unknown outcome ("Do not submit another booking"), restaurant contact unresolved, confirmed train, cancellation pending, and traveler consent ("Mike declined").
  - Amounts are shown twice in different formats ("€740" and "EUR 740.00").
  - Party size varies between "Party of 3" and "table for 4".
  - EST. SPEND shows €0.
- **Costs** (`screens/trip-costs/`): the Carmen MXN ledger and expense detail are good. Elif's Rome costs show "$0 · Nothing logged yet", with no planning estimate, which is the reason the flow fails. Ben's empty state is identical.
- **Stay** (`screens/trip-stay/`):
  - The booked Lisbon detail shows reference, dates and cancellation, but its "Where it puts you" map is a bare scale bar (no token).
  - The split-stay Porto fixture shows "No bed yet." rather than the two per-person bases the registry expects.
- **Trip settings** (`screens/trip-settings-admin/`, `ex-trip-settings.jpg`): the screen is "Settings", with Trip policy, Your preferences and Trip lifecycle sections. The archive-blocked sheet ("Finish booking work first") renders.
- **Trip map** (`screens/trip-map/`): the no-token fallback ("Map preview is unavailable here") shows dots and a line. The Trip/City/Day segmented control overlaps a truncated "Lisb…" title.
- **Trip changes**: an empty "History — Nothing has changed yet.", with the tab bar still visible on the pushed screen.
- **Trip creation**: "How should we start it?" — *Talk it through with Vesper*, or start from saves, a shape, or blank.
- **Trip story**: the kicker is "**READY FOR ATLAS**", and the "rain-slicked pavement" slot uses an unrelated stock portrait.
- **Invite** (`screens/auth-invite/`, `external-sharing-invite.jpg`): an organizer-first landing that keeps the private summary closed, plus manual code entry and invalid-code recovery.
- **External and public pages** (`screens/external-sharing/`): a shared story page ("Four Days in Lisbon — Made with Vesper"), generic unavailable and network pages, and signed-out proposal and Unpacked doorways. Owner controls show a story link on **travelagent.app**, even though `STORY_SHARE_ENABLED=false` in the client.

### 3.11 Cross-root utility surfaces

- **Notifications** (`screens/notifications-alerts/`): a clean ledger. The filters are "All / **Trips** / **Vesper** / Social", legacy root names, and every row is stamped "now".
- **Universal search** (`screens/universal-search/`): the scope chips are "All / Places / Nearby / **Atlas**". The copy reads "Nothing saved to your trips or **Atlas** yet", and the empty state is blank below the chips. The Ask Vesper row, trip-scoped Receipts/Costs/Actions and the offline banner work.
- **You** (`screens/you-portrait/`, `ex-you.jpg`): profile header, "Places you hold", public preview, settings. Loading and error states are clear.
- **Trust controls** (`screens/trust-controls/`): Account, Privacy, Constraints, Data receipt and Vesper autonomy (Suggest & confirm per decision area). "Google — Coming soon."
- **Atlas:**
  - The `/(tabs)/atlas` tab redirects to Life (`ex-atlas-tab-redirect.jpg`).
  - `/you/atlas/memory` still renders "Your Memory" with Correct and Forget (`screens/atlas-memory/`).
  - The Removed empty state names "Almanac or Timeline".
- **Guide reader**: every saved row shows both a "SAVED" label and a "Saved" label.
- **Dossier reader** (`screens/discover-detail-reader/`): loading, error, stale, empty and not-found states. In the error state the "FIELD NOTE" kicker overprints the title.
- **Photo intake**: "No trip photos surfaced" (the simulator has no library photos). The action-state gallery renders 11 of 12 states.
- **Onboarding** (dev route): the gift, permission and decline steps render. Earlier steps were blank because of a bundle reload. On the decline screen, "Keep going" looks disabled (grey).
- **Share capture** (`/share-capture` opened directly): "Nothing to share" empty state. The share extension was not exercised.
- **Dev galleries** render: control system, profile system, native workbench, canonical artifacts, header gallery, surface census and four-root portfolio. In the canonical artifact gallery the "SOURCE-BOUND" and "TICKETED" labels overprint.

## 4. Pass 2 — default / legacy shell, mock API — `screens/default-shell/`

Metro ran without internal or rollout flags. The shell is **Plans · Vesper ·
Places · Life**. There is a floating brown Vesper chat button on Plans, and the
dev-only DevFab "M" is visible. The mock banner is shown unless screenshot mode
hides it.

Running registered flows was too slow in this pass: the first two `trips-home`
captures took ~13 minutes, and both failed on fixture copy. I switched to
direct deep-link captures (`guide://dev/screenshot-mode?persona=…&to=…`).
**Registered flow results for the legacy shell are therefore unverified**, apart
from these partial `trips-home` results:

- `trips-home-starter`: fail, "The year's still unwritten. Where are we going?" not visible as a title;
- `trips-home-cold-saves-connect`: 3/4 images; "Bring someone with you." absent.

Plans home by persona (`df-plans-<persona>.jpg`):

- **default** (Alex): "You're here. What do you need?" Crown "LEAVING TOMORROW · Lisbon Jun 4–10", Vesper line "Tomorrow looks lighter — I adjusted for the ankle…", *Open plan*, "Also in play · 2 trips · 1 needs you".
- **ana / ana-saves** (cold): "Start with one idea." with the IN MOTION card "The year's still unwritten. Where ar…" (the title is truncated with an ellipsis, and the same sentence repeats in the quote box beneath it). "Start here" rows follow: *Find something good close by*, *Teach Vesper your taste*. The cold-saves variant adds "On the table — Copenhagen, already taking shape" (seed sketch) and "Connect — Start a trip together" (`p2-trips-home-*.jpg`).
- **ben / ready**: "Bring everyone in. Keep the trip moving." Kyoto 14 (ben) or 4 (ready) days out; "Yoramu or an easier night…".
- **carmen**: "NOW Casa Azul at 3:00 — Frida Kahlo", "LIVE · DAY 3 OF 7 Mexico City".
- **elif**: Rome return Nov 20–25; Istanbul "call now or lose".
- **quiet**: "Nothing needs you. Start when it pulls." (Kyoto holding steady).
- **urgent**: "PLANS · NEEDS YOU — One thing needs you. Clear the way." Porto vote, then *Review*.
- **mara**: the same crown pattern for a trip literally named "**Group taste demo**", which leaks fixture naming into the product.
- **dev** (just returned): **Render Error**. Plans lands in `TravelPlanScreen`, and the mock plan-shape builder throws "Cannot read property 'projection_version' of undefined" at `utils/api/mock/tripsPlan.ts:1768`. The fix is optional chaining on `envelope`. The crash persists across relaunches while Dev is the stored persona, and it breaks later persona switches until AsyncStorage is reseeded. This is a mock-layer defect, but it is what a founder demoing the Dev persona would see.

Other default-build observations:

- **Vesper tab** (`df-vesper-tab-default.jpg`, `df-vesper-tab-tapped.jpg`): the same workbench as Chat, with the same **empty composer panel**. It was reached both by deep link and by tapping the tab.
- **Places** (`df-places-tab-default.jpg`) and **Life** (`df-life-tab-default.jpg`) are visually identical to the internal build. Places uses the same workspace renderer; Life is always `LifeRootV1Screen`, with the identical one-entry projection.
- **Plan / itinerary** (`df-trip-lisbon-itinerary.jpg`): the legacy day spine works: "Thursday, October 15 · Day 1 of 2", day chips, "20:30 Dinner at Taberna da Rua das Flores — PROPOSED", "DECISION — Move dinner earlier", Day 2 "LUX Fragil Closing Night". The internal Plan Shape replaces this view (§3.9).
- **Venue page** (`df-venue-legacy.jpg`): the legacy page, with a serif body, "+ Add to trip", PEAK / GREAT FOR / NOT IDEAL, and "About this place — No dossier available." It has more concrete verbs than the rebuild ("Check a visit now / Ask Vesper").
- **Chat thread** (`df-concierge-chat.jpg`): the same header overlap bug when opened scrolled. A mock message claims "Fado's booked — … Confirmation sent to Sarah."
- **Plans FAB** (`df-plans-fab-tap.jpg`) opens a private chat and **auto-sends** "Help me start a new trip."; the mock reply streams.
- **Discover** (`df-discover-redirect.jpg`) redirects to Places. **Invite code** entry renders.

## 5. Pass 3 — real local backend, internal four-root build — `screens/real-local/`

The dev client ran against the lane API on `127.0.0.1:61188` with
`EXPO_PUBLIC_USE_MOCK_API=false`. The persisted `dev.mockModeOverride` was set
to `false`. The viewer was one freshly inserted synthetic user; no seed or eval
fixtures were loaded. Device-driven requests all returned 200:

- `/api/root-projections/v2/home`, `v2/places`, `v2/places/runtime`;
- `v1/life`, `v1/life/record`;
- `/api/concierge/home/workbench` and `/voice`, `/api/me`, `/api/me/home-bootstrap`;
- `/api/places/feed`, `/api/experience-graph/projection`, `/api/pending-chat-turns`.

The only non-200 was my own manual `GET /api/trips` (405).

- **Home** (`rl-home.jpg`):
  - "SATURDAY, SEP 26 — The week is open / Your recorded world stays ready when you need it."
  - The crown is the promoted Places aperture, rendered as "**Anywhere / Anywhere** — Open in Places". The label repeats, and there is no content.
  - The week strip is real-dated (Sat–Fri), with a "A PARTIAL READ — Some context is unavailable" banner from two `moment/conditions_unavailable` degradations, then "NOTHING ELSE WAITS".
  - The raw projection had `home_posture=quiet`, empty `now` / `in_motion` / `continuity`, and one `horizon_aperture_row`. The cold-start sample ticket that Codex's `bf1e5dadf` admits is **not** in this baseline.
- **Places** (`rl-places.jpg`): "NO TRIP YET", a partial-read banner, "Start with what pulls you.", then "WHAT STILL WORKS — Open field — Nothing leads this field yet… **No eligible World Field signal in the current scope.**" The last sentence is backend basis text shown to the user. Links: *Search this field*, *Open map*, *Open the source*.
- **Life** (`rl-life.jpg`): "The record is still taking shape." Lens row, "Everything else stays in the record", and zero entries (API `delivery_state: thin`, `total_entry_count: 0`).
- **Chat** (`rl-chat.jpg`): "WITH VESPER — Reading your trips, saves, and open conversations…" and a "THIS SEASON · 3" list: Elk bugling (Yellowstone), Acadia foliage, raptor migration (Grand Canyon). This generic US national-park seasonal content is not tied to the user or to New York. The composer is blank.
- **You** (`rl-you.jpg`): "Product Map QA · Since 2026", with an honest empty record line.
- **`/dev/home-places-rehearsal`** (`rl-rehearsal.jpg`): "Expected fixture account required". The rehearsal needs the synthetic fixture account that the unmerged runners create.
- **Backend log:**
  - 25 background warnings `experience_brief_embedding: Failed to scroll past experiences from Qdrant` (empty collection);
  - one misleading startup warning, "POSTGRES_HOST not set — Database will be unavailable", while `DATABASE_URL` was set and working;
  - one `llm_call_records` row: `vesper.home.workbench_voice`, `claude-haiku-4-5`, `status=failed`, `error_type=AIProviderBlockedError`, 0 tokens, 7.5 ms. **No provider call left the machine**; the workbench voice fell back to deterministic copy.

## 6. Cross-cutting findings

- **Root naming is not migrated.** In the four-root build, users see Home/Chat/Places/Life tabs, but the copy still uses:
  - "Ask Vesper" on CTAs;
  - "Vesper · private" in chat headers;
  - "Message Vesper…" in the composer;
  - "The itinerary stays in **Trips**" in Places;
  - "One thing needs you in **Trips**" / "Open in Trips" on the Chat seam;
  - "All / **Trips** / **Vesper** / Social" as notification filters;
  - the search chip "**Atlas**" and "Nothing saved to your trips or Atlas yet";
  - "READY FOR **ATLAS**" on the story;
  - "Almanac or Timeline" in the Removed state;
  - "context you carried from **Discover**" in chat.
- **Fixtures are not coherent across surfaces.**
  - The Lisbon trip is Jun 4–10 (Chat, stay, invite), Oct 15–16 (plan, chat transcript) and Apr 10–14 (shared story).
  - Home is always "Tuesday, Sep 1" with the same week strip.
  - Home and Life mocks ignore the persona: Elif's Home is Brooklyn while her Places are Istanbul.
  - Trip names leak fixture intent ("Group taste demo").
- **Backend vocabulary is exposed to users:** "Canonical outcome", "ADJUDICATED", "CATALOG", "No eligible World Field signal in the current scope", "Hours unverified" on every saved row.
- **Headers and overlays:**
  - chat headers have no backing surface, so scrolled text runs under the back button and status bar;
  - kickers collide with the status bar (city page), with titles (dossier error "FIELD NOTE") and with badges (canonical artifact);
  - the trip map segmented control overlaps the title;
  - captures taken during pushes show both pages side by side (`single-trip-interactions/global-chrome-collapsed.jpg`, `places/places-default.jpg`, `saved-collections/saved-collections-default.jpg`).
- **Auto-sent prompts.** The Plans FAB and the place page's *Ask Vesper* send a message on the user's behalf immediately; the Home crown's *Ask Vesper* opens an empty generic chat instead. Handoff behaviour is inconsistent.
- **Performance.** The first full JS bundle (empty cache) took 42 s; later `--clear` starts took 17 s (default and real-API Metro). After that each app launch fetched a cached bundle in ~0.2 s. Structural skeletons were hidden within budget (e.g. `loading_state_exposure` 336 ms; `cold_launch_to_first_meaningful_screen` 2002 ms against a 2500 ms budget on trips home). I saw no jank measurements beyond Metro breadcrumbs. The per-surface flow slowness in Pass 2 came from Maestro waits, not app rendering.
- **Metro errors (Pass 1).** Apart from dependency-cycle and Reanimated warnings, there was only `[QueryHealth] ["trip-access-state","persona-urgent-porto"] :: Trip persona-urgent-porto has no mock member authority`. Pass 2 added the plan render error; the exploration added the original-reader red box.

## 7. Harness findings (for the QA owner)

- The polish runner works on this lane when pointed at `VESPER_METRO_URL=http://127.0.0.1:61189` and `--device="iPhone 16"`. It needs no readiness change, because the dev client had already been connected once to the lane Metro.
- **Stale boot labels.** Registered flows wait for tab text that no longer exists:
  - `"Discover"` in 20 surfaces;
  - `"Vesper"` in 10/16 `vesper-chat` flows;
  - `"Trips"` in `trip-stay` and others;
  - `"Plans"` in `entity-object` and `places`.

  Legacy Trips Home ids are required by `trips-home`, `vesper-home-seam`, the chat artifact galleries and some header flows. Neither shell satisfies the whole registry as registered. Patching only the boot wait to `"Places"` recovered most shell-agnostic surfaces (e.g. notifications 0/4 → 4/4, external sharing 5/7 → 7/7).
- **Superseded screens:**
  - Trip settings is now titled "Settings" (0/10);
  - the itinerary flows assert the day spine, which `PLAN_SHAPE_ENABLED` replaces (0/6);
  - Discover flows assert a retired root (0/3);
  - Atlas flows assert ids that no longer exist because the tab redirects to Life.
- The `dev/onboarding` deep link triggers a bundle reload mid-flow, which leaves blank frames. `canonical-artifact-gallery` hard-codes the dev-client launcher on port 8081.
- `life-root` and `canonical-artifact-reader` have **no registered captures**, so Life has no registered native evidence at all.
- `places-workspace-lisbon-urgency` and `-lisbon-decision` produce identical frames.

## 8. What I did not verify

- **Physical-device behaviour:**
  - TestFlight/production builds, where `__DEV__` is false and dev routes are absent;
  - Clerk auth;
  - push notifications;
  - share-extension input;
  - photo-library content;
  - maps with a real token.
- **Registered legacy-shell capture set:** not run (Pass 2 used direct captures). The chat artifact galleries, `header-system` (except the header gallery) and `atlas-board/compose/kept/review` were not captured in either pass.
- **Seeded or dogfood real-backend data:** no eval or dogfood seed was loaded, so Pass 3 shows a fresh user only. The owner-backed original, social note and cold-sample flows from the home-value-delivery lane are unmerged.
- **Root causes:** the blank composer (JS vs the 09-22 binary) and the Life "no longer available" record mapping were observed but not diagnosed.
- **Coverage:** no `make verify`, unit tests or typecheck were run; this is observation only. The design comparisons use `docs/systems/four-root-loop-object-surface.md` and `design-atlas-home-places-life-plans.md` §3 as intent, not pixel parity.

## 9. Runtime cleanup performed

- Stopped all three Metro instances (internal, default, real-API) and the lane API.
- Ran `docker compose -p vesper-product-map-inventory down` **without `-v`**. The volumes `vesper-product-map-inventory_pgdata` and `_qdrant_data` are retained.
- Deleted the synthetic user `529d0eb3-…` and its rows: 6 `user_events`, 1 `atlas_scan_history`, 1 `user_email_aliases`, 1 `vesper_workbench_rotation_state`.
- Left in place: the migration-seeded `places`/`place_slug_aliases` rows (New York City) and the one blocked `llm_call_records` audit row (no user id).
- Shut down the iPhone 16 simulator. The Codex simulators `AF31B886…` and `EBEE500B…` stayed booted and untouched.
- The only lane file changed is the gitignored `.workspace-lane.json` (`runtime.device`). All three lane repos are clean. The lane `travel-app/.maestro/runs/2026092{6,7}T*` run folders (gitignored) hold the full-resolution runner captures.

## 10. Screenshot index

| Folder | Count | Contents |
|---|---|---|
| `screens/home-root/` | 8 | Four-root Home, 7 postures (+ returned close) |
| `screens/places-workspace/`, `screens/places/` | 11 + 1 | Places root and depth, all personas; city page |
| `screens/entity-object/` | 3 | Rebuilt venue / site / experience pages |
| `screens/vesper-home/` | 8 | Four-root Chat root (`internal-chat-*`), incl. blank composer crops |
| `screens/vesper-chat/` | 13 | Chat threads and Dynamic Type variants |
| `screens/explore-internal/` | 37 | Manual walk: Life lenses and record, Chat from objects, Places map/saved/reading, city page, original reader and red box, Plan Shape, settings, dev census/portfolio, Elif persona |
| `screens/default-shell/` | 26 | Legacy Plans per persona (incl. Dev render error), Vesper tab, Places, Life, legacy itinerary, legacy venue, chat, FAB, Discover redirect, invite |
| `screens/real-local/` | 6 | Real local backend: Home, Places, Life, Chat, You, rehearsal preflight |
| `screens/proposal-detail/`, `booking/`, `trip-costs/`, `trip-stay/`, `trip-settings-admin/`, `trip-itinerary/`, `trip-map/`, `trip-changes/`, `trip-creation/`, `trip-story/` | 10/20/9/8/2/1/1/1/3/1 | Trip-level surfaces |
| `screens/notifications-alerts/`, `universal-search/`, `you-portrait/`, `trust-controls/`, `auth-invite/`, `external-sharing/` | 8/6/4/6/3/11 | Cross-root utilities and public pages |
| `screens/onboarding/`, `photo-media-intake/`, `guide-reader/`, `discover-detail-reader/`, `saved-collections/`, `illustration-product-states/`, `single-trip-interactions/`, `atlas-memory/` | 8/19/1/5/1/3/4/2 | Secondary readers, states and compatibility routes |
| `screens/control-system/`, `profile-system/`, `native-design-workbench/`, `canonical-artifact-gallery/`, `header-system/` | 12/11/8/1/8 | Dev galleries |

All images are 590×1278 JPEG (half of native 1179×2556).
