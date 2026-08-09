---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-09
expires: 2026-09-08
why_new: Records the independent post-integration code review of the August Places and Trips home-surface implementation lanes.
---

# Places and Trips Home Surfaces — Integration Code Review

**Date:** 2026-08-09

**Review type:** Independent static/source and focused-test review

**Release conclusion:** Not ready for backend-real or device acceptance

**Canonical design authority:** External bundle at `/Users/feihuyan/Downloads/vesper-home-surfaces`; no design source was copied into a repository

## 1. Executive conclusion

The integration established useful foundations, but it did not yet reach the architecture or correctness floor described by the engineering roadmap.

The most important issue is divided authority. The new Trips section plan and Places presentation model exist, but the page roots still independently decide renderability, fallback state, semantic membership, side-data selection, spacing, and telemetry identity. The same content can therefore be considered valid by one layer and unrenderable by another. This produces blank Trips states, potentially wrong-trip actions, contradictory weather, silent module loss, repeated Places impressions, and exposure records that cannot reliably drive item-level fatigue.

The backend has a parallel form of the same problem. Places producer outcomes distinguish `available`, `empty`, and `unavailable` internally, but the wire contract discards the distinction. Its isolation helper catches `RuntimeError` and timeout, while ordinary database failures are SQLAlchemy/DBAPI exceptions. The code therefore claims independent degradation while a normal database outage can still fail the whole feed.

The current work should remain described as **static/mock integration**. TypeScript and typography gates pass, and focused tests are substantial, but:

- there is no backend-real canary or physical-device evidence;
- the canonical mock/persona lane cannot produce three of the four new Trips module families;
- size, containment, and spacing gates are red;
- the governance validator rejects any future `V=verified` state, so the documented device-acceptance path is not executable.

No new private-to-group data leak, parallel proposal writer, or unreceipted home-surface mutation was proven in this review. The new People route reads canonical trip detail data, proposal actions continue through the existing resolver, and Dreams learning copy remains gated by the recorded receipt. Those are meaningful passes, but they do not offset the state and rendering defects below.

## 2. Exact review scope

### 2.1 Repositories and revisions

| Lane | Branch | Reviewed head | Home-surface commits in scope |
|---|---|---|---|
| Frontend | `codex/home-surfaces-app-integration` | `220739aa` | `0ce6374a`, `1de051c8`, `10d4972c`, `3b9bf942`, `5ba0b960`, `6f80b043`, `51991c40`, `2500e18f`, `225225ba`, `1145e8b0`, `9a2ac692`, `5a9f1f39`, `ce90e3d2`, `9f18bd0d`, `220739aa`, `b841d8c2` |
| Backend | `codex/home-surfaces-backend-integration` | `421d1ff3` | `57b1592c`, `44b30c40`, `ced9643f`, `1560b15d`, `421d1ff3` |
| Workspace | `codex/home-surfaces-coordination` | `f42e6c9` before this report | authority, inventory, schema, audit, roadmap, and execution-evidence commits from `aea4009` through `f42e6c9` |

Unrelated concurrent commits and untracked workspace directories were not treated as home-surface work and were not modified.

### 2.2 Review dimensions

The review traced:

1. canonical design and adoption claims;
2. backend producer and projection behavior;
3. generated transport contracts;
4. pure presentation/section planning;
5. root rendering, page rhythm, and responsive existence gates;
6. destination and mutation ownership;
7. impression/engagement identity and lifecycle;
8. fixture, mock, backend-real, and device evidence;
9. architecture and design-system debt gates; and
10. governance paths used to promote an item from static evidence to acceptance.

Severity means:

- **P1:** blocks a correct production or rolling-deploy path, can present the wrong state/action/data, or makes a required acceptance gate impossible;
- **P2:** material telemetry, performance, architecture, or evidence defect that should be resolved before new card families expand the surface;
- **P3:** bounded hardening or documentation issue without a currently demonstrated user-facing failure.

## 3. P1 findings

### P1-01 — Trips has two crown authorities; a rejected crown suppresses valid modules

**Evidence**

- `app/(tabs)/trips/index.tsx:442` builds the renderable crown through destination parsing and can return `null`.
- `app/(tabs)/trips/index.tsx:497` passes the raw projection to `buildTripsHomePresentation`.
- `utils/tripsHomePresentationModel.ts:68-85` treats any raw JSON crown as present and therefore returns `ready` / `fallback: none`.
- `app/(tabs)/trips/index.tsx:1213-1537` nests Now, Crown, Countdown, Conditions, Group, and Queue inside the `stackCrown` branch.

**Failure mode**

A ranked projection with an unknown or malformed crown destination and otherwise valid modules yields `stackCrown === null`, while presentation remains `ready`. The root renders neither the crown nor any valid planned modules and has no fallback.

**Why tests missed it**

Destination rejection and presentation status are tested independently. No screen test combines a rejected crown with valid modules.

**Required correction**

Use one renderability result as the state authority. The pure plan should own crown acceptance/rejection and the root should render independent valid sections even when the crown is unavailable. Add a screen-level regression for a rejected crown plus valid modules and queue.

### P1-02 — Valid empty and persisted pre-contract projections can render a blank “ready” hero

**Evidence**

- `utils/tripsHomePresentationModel.ts:136-140` degrades only `projection_state === "ranked"` without a crown. An empty projection with committed trips falls through to `ready`.
- `utils/tripsHomePresentationModel.ts:80-85` assigns a fallback only for `degraded`.
- `app/(tabs)/trips/index.tsx:1537-1571` renders only the `starter` fallback; the modeled `unranked` fallback has no render branch.
- `utils/queryPersistence.ts:7-24` retains the unchanged v2 query cache for twelve hours, so restored payloads from before `projection_state` was introduced are a real compatibility case.

**Failure mode**

`projection_state=empty` with committed trips, or a persisted old projection without `projection_state`, can produce no crown, no fallback, and a blank hero. A ranked crownless response with committed trips produces `fallback: unranked`, which is also not rendered.

**Required correction**

Define the full state table before rendering: pending, ranked/renderable, ranked/rejected, empty-with-trips, empty-without-trips, unavailable-with-cache, and unavailable-without-cache. Render every declared fallback and migrate or invalidate incompatible persisted projections.

### P1-03 — The Now module can open a different trip than the module identifies

**Evidence**

- `app/(tabs)/trips/index.tsx:818-827` prioritizes the independently selected `liveTripId` and `liveSituation` without comparing them with `row.item.trip_id`.
- Only when that side data is absent does the callback honor the module row destination.

**Failure mode**

With two live trips, or an urgent crown and a Now module for another trip, pressing the Now band can select and open the wrong trip’s block.

**Required correction**

Key live situation data by the module’s trip identity, or move the coherent destination/side-data receipt into the produced module. Add a two-trip regression where the global live trip differs from the Now module trip.

### P1-04 — Conditions can combine present-location weather with another trip’s forecast copy

**Evidence**

- `app/(tabs)/trips/index.tsx:1374-1406` passes ambient/current-location weather into the trip-specific Conditions module.
- `components/trips/TripsConditionsBand.tsx:58-67` renders that temperature/glyph beside the module’s produced title and row line.
- The existing component test uses a matching Lisbon fixture and cannot expose locality disagreement.

**Failure mode**

A traveler currently in New York with a Rome trip can see New York’s temperature beside copy such as “Rain in Rome tomorrow.” This is plausible but false composed data.

**Required correction**

Do not join unkeyed ambient weather into a trip module. Produce or fetch a trip/destination-keyed weather receipt, and render an explicit unavailable state when it is absent.

### P1-05 — The required old-server Trips adapter was not retained

**Evidence**

- `utils/tripsHomeSectionPlan.ts:92-124` creates dedicated D2 sections only from `modules`.
- `utils/tripsHomeSectionPlan.ts:126-153` maps old `rows` only into the generic queue.
- `__tests__/utils/tripsHomeSectionPlan.test.ts:78-93` intentionally codifies no legacy row mining.
- The roadmap requires a temporary old-server adapter and allows deletion only after backend rollout, minimum-client, and device gates (`home-surfaces-engineering-roadmap-2026-08-09.md:325,684`).

**Failure mode**

During a rolling deploy, an old backend payload loses Now, Countdown, Conditions, and Group compositions and demotes those facts to generic queue rows. The intended migration compatibility path does not exist.

**Required correction**

Either implement the bounded compatibility adapter with a dated removal gate or change the deployment plan to an explicitly incompatible cutover with cache invalidation and minimum-version enforcement. The roadmap and tests must agree with the chosen strategy.

### P1-06 — Ordinary database failures escape Places producer isolation

**Evidence**

- `backend/places/feed_orchestration.py:57-72` converts only `RuntimeError` and `TimeoutError` to `UNAVAILABLE`.
- `backend/places/sections.py:114-190` runs multiple database-backed producers through `asyncio.to_thread` inside one `gather`.
- `backend/core/db/engine.py:103-118` passes SQLAlchemy connection/execute failures through; it does not translate them to `RuntimeError`.
- `backend/places/saves.py:55-56,91-92` performs ordinary SQLAlchemy reads.
- Tests model source outage only as `RuntimeError` (`tests/places/test_feed_orchestration.py:28-49`) and model programmer/schema propagation separately (`:117-133`).

**Failure mode**

A normal SQLAlchemy/DBAPI operational failure propagates out of `gather` and fails the entire Places feed, contradicting the independent optional-producer degradation contract.

**Required correction**

Define an explicit recoverable operational-exception boundary that includes database and approved I/O failures without swallowing validation/programming defects. Test with the actual exception classes raised by each adapter.

### P1-07 — Places timeouts bound response waiting, not underlying resource use

**Evidence**

- `backend/places/feed_orchestration.py:59` applies `asyncio.wait_for` to the producer awaitable.
- Many producers are blocking `asyncio.to_thread` calls (`backend/places/sections.py:115-151` and composed producers).
- Cancelling `asyncio.to_thread` does not stop the already-running function/thread.
- The timeout test at `tests/places/test_feed_orchestration.py:69-81` uses cancellable `asyncio.Event.wait()`, not a blocking DB operation.

**Failure mode**

The request returns after the timeout, but the database thread continues. Repeated slow requests can accumulate abandoned work and exhaust the thread executor or DB pool. A propagated programmer/schema error can also leave sibling work running.

**Required correction**

Use driver/query timeouts and bounded concurrency at the adapter/resource layer. Treat request timeout as only one layer of the budget. Add a blocking-producer characterization proving the chosen resource behavior.

### P1-08 — Places can resolve from loading with a permanently zero viewport

**Evidence**

- `components/places/PlacesWorkspace.tsx:57` initializes viewport height to zero.
- The loading branch at `components/places/PlacesWorkspace.tsx:440-447` omits `onViewportLayout`.
- The resolved branch adds the callback at `:457-465` to the same reconciled `ScreenScaffold`/native scroll view.
- `components/places/PlacesSectionFeed.tsx:84` treats height `<= 0` as never visible.

**Failure mode**

React Native guarantees layout callbacks on mount or layout change, not because a callback prop was added. If the native viewport size does not change when loading content is replaced, the height can remain zero and all Places impressions remain disabled for the session.

**Required correction**

Measure the viewport in every branch or own the measured scroll container above the state branch. Add a native/component loading-to-resolved transition test rather than mocking the scaffold.

### P1-09 — Search toggling can log the same Places sections repeatedly

**Evidence**

- `hooks/useSectionExposureBoundary.ts:46` owns dedupe in a boundary-local `Set`.
- `components/places/PlacesWorkspace.tsx:577-622` replaces the feed with search results and remounts it after Cancel.
- `components/places/PlacesWorkspace.tsx:225-231` makes this a normal repeated interaction.

**Failure mode**

Each feed remount creates fresh boundary-local dedupe state. Opening and canceling search repeatedly logs the same unchanged section after every 800 ms dwell, inflating exposure and fatigue signals.

**Required correction**

Move session/user/content dedupe to a root-owned registry that survives conditional leaf unmounts. Test unmount/remount, not only rerender of the same boundary instance.

### P1-10 — Places distinguishes unavailable internally, then collapses it to empty on the wire

**Evidence**

- `backend/places/feed_orchestration.py:27-40` defines `AVAILABLE`, `EMPTY`, and `UNAVAILABLE` and explicitly says the state is absent from the wire model.
- `backend/places/sections.py:213-235` converts unavailable values to empty lists, zero totals, default content, or `None`.
- The frontend therefore receives absence for both “no evidence exists” and “producer failed.”

**Failure mode**

The UI and telemetry cannot distinguish a genuinely empty personalized feed from a partial data outage. This violates the roadmap’s explicit honest empty/unavailable state requirement and can make stale/partial behavior look like product truth.

**Required correction**

Project a bounded availability envelope or feed-level partial-unavailability receipt through the generated contract. Do not expose internal stack traces or fabricate placeholder cards; render a scoped unavailable/stale state.

### P1-11 — The governance validator makes device verification impossible to record

**Evidence**

- `docs/status/home-surfaces-composition-inventory.json:7` says later evidence receipts can promote evidence.
- `docs/governance/home-surfaces-design-authority.json:104` defines `V=verified` as requiring a physical-device receipt.
- `scripts/check_home_surfaces_governance.py:146-147` rejects every inventory item whose `V` is `verified`.
- The schema has no evidence-receipt reference field for F, B, or V.

**Failure mode**

Even after a valid physical-device run, the governed inventory cannot represent acceptance without failing CI. Conversely, the validator does not require a receipt when other evidence layers become verified.

**Required correction**

Add typed evidence-receipt references and validate that `F`, `B`, or `V=verified` has an appropriate immutable artifact. Permit verified states only when their receipt validates.

## 4. P2 findings

### P2-01 — The Trips plan is an identity adapter, not yet the promised composition authority

`utils/tripsHomeSectionPlan.ts:25-47` owns identifiers and raw items, but the root still:

- selects semantic roles with `.find` (`app/(tabs)/trips/index.tsx:463-481`);
- recomputes existence (`:830-837`);
- hardcodes order, containment, and rhythm (`:1215-1455`); and
- never consumes or logs `sectionPlan.rejections`.

Distinct modules with duplicate semantic roles pass the plan and the root silently first-wins. The execution ledger’s “pure Trips section plan landed” statement is accurate only for the adapter layer, not the roadmap’s membership/order/render-state/action/exposure/rhythm seam.

**Correction:** make the plan exhaustive for semantic slots and render state, reject or deliberately compose duplicate roles, and make rejections observable.

### P2-02 — Crown/queue overlap is not rejected

`utils/tripsHomeSectionPlan.ts:88-90` seeds duplicate detection with module identities, not `crown.id`; the queue overlap check at `:138-143` therefore allows the same content to render as crown and queue. The current overlap test includes an intervening module with the crown ID, so it does not test direct crown/queue duplication.

**Correction:** include the accepted crown identity in content dedupe and add a direct crown-plus-queue regression.

### P2-03 — Trips exposure identity is not a real content revision and is discarded before persistence

- Backend module `content_id` is the stable item ID (`backend/home/trips_stack.py:899-905`).
- Mutable facts such as group unread count can change while the item ID stays stable.
- The app passes the stable ID as `contentRevision` (`app/(tabs)/trips/index.tsx:1222-1226,1410-1415`).
- `utils/tripsHomeTelemetry.ts:30-57` persists only the authored `sectionId` as `entity_id`.
- `backend/core/db/exposure.py:95-110,197-235` folds exposure by that entity ID.

The local boundary may not recognize materially changed visible content, while the backend cannot distinguish which crown or queue content was shown or engaged. Queue items have stable per-item identities in the plan but collapse to `sectionId: "queue"` at `app/(tabs)/trips/index.tsx:1477-1506`.

**Correction:** decide the actual exposure unit—section composition, content item, or revision—and carry that identity end to end. A revision should change when the visible fact set materially changes, without including private content in telemetry.

### P2-04 — Valid empty Trips projections inflate the crownless-defect metric

`app/(tabs)/trips/index.tsx:676-683` logs every null crown as `backend_null`, including the contractually valid `projection_state === "empty"`. Existing tests use mock auth or non-UUID users and do not assert the real telemetry call.

**Correction:** log only contract violations as defects; give valid empty states a separate product-state metric if needed.

### P2-05 — Viewport math counts content hidden under floating chrome

Both `hooks/useSectionViewportRegistry.ts:11-20` and `components/places/PlacesSectionFeed.tsx:74-88` intersect sections with the full scroll viewport. `components/ui/RootFloatingHeader.tsx:101-108` overlays that viewport absolutely. A short section fully behind the header can dwell and emit an impression. Bottom floating chrome has the same class of problem.

**Correction:** pass effective top/bottom occlusion insets or measure the unobscured viewport. Add fully occluded section tests for both roots.

### P2-06 — App backgrounding can complete a false dwell

The roots gate exposure on navigation focus, but the shared boundary has no `AppState === active` input. Navigation focus normally remains true when the app backgrounds. A timer started just before backgrounding can therefore complete while the surface is not visible.

**Correction:** make surface activity include app foreground state and test background/foreground transitions during dwell.

### P2-07 — Places scroll telemetry rerenders the full card tree at scroll frequency

`components/places/PlacesWorkspace.tsx:57-65` stores every distinct scroll Y in React state, while `scrollEventThrottle={16}` at `:465` can update each frame. `PlacesSectionFeed.tsx:424-545` then remaps the image/card-heavy feed. Trips already uses a ref-backed registry that updates React state only when the visible ID set changes.

**Correction:** use one shared ref-backed viewport registry and publish only visibility-set changes. Add render-count or profiler coverage for a representative feed.

### P2-08 — Canonical mock/persona QA cannot render most new Trips modules

`constants/personas/tripsHomeStackFixtures.ts:18-81` and `utils/api/mock/trips.ts:4022-4032` emit only crown plus legacy rows. Since the new plan uses only `modules` for D2, default persona/mock screenshots cannot show Countdown, Conditions, or Group; Now appears only in a hand-authored test payload.

This weakens the execution ledger’s static/mock evidence language. Leaf/component tests prove isolated rendering, not canonical whole-page fidelity or state rhythm.

**Correction:** add canonical generated-contract fixtures for every adopted module/state combination and drive whole-page screenshots from them.

### P2-09 — The backend wire model does not enforce module identity and semantic uniqueness

`backend/home/trips_stack.py:579-604` validates empty/ranked crown state but does not enforce unique module IDs, content IDs, roles, or queue/module disjointness. Correctness currently depends on the one builder implementation. That is unsafe for cached data, alternate producers, future migrations, or malformed responses, especially because the app first-wins duplicate roles.

**Correction:** enforce transport invariants at model construction and retain defensive client rejection/telemetry.

### P2-10 — Architecture debt gates are red before new design families begin

Current checks report:

- `TripListScreen`: 1,504-line function; function budget is 800;
- `PlacesSectionFeed.tsx`: 2,383-line renderer/dispatcher hot file;
- containment: 166 hand-rolled containers vs. baseline 162;
- spacing: 363 raw declarations vs. baseline 361.

The reviewed branch added 383/removed 135 lines in the Trips root and added 197/removed 68 in `PlacesSectionFeed`. The roadmap’s G3 gate requires size, containment, spacing, typography, and design-evidence checks to pass before new family work. Typography passes, but the architecture gate as a whole does not.

**Correction:** finish the planned extraction before adding new Page-board variants. Split Trips controller/plan/render families and Places family registries with single-writer hot-file ownership; reduce ratchets rather than increasing baselines.

## 5. Design and implementation status after review

The original post-pivot audit remains directionally correct: most new compositions in `Places - The Page` and `Trips - The Page` are not implemented. This integration primarily improved the architecture substrate and made existing/newly projected D2 content reachable. It did not implement the majority of proposed registers, arrangements, or whole-page states.

### 5.1 Trips full-stack status

| Layer | Status | Review result |
|---|---|---|
| Backend projection | Partial | Dedicated modules are selected before the generic queue, but the model lacks uniqueness invariants and content revisions are stable item IDs. |
| Generated contract | Implemented/static | Additive schemas are generated and typecheck passes. Rolling-deploy compatibility is unresolved. |
| Pure plan | Partial | Identity/dedupe adapter exists; semantic membership, state, action, rhythm, and rejection observability remain in the root. |
| Root render | Partial/defective | D2 modules render in happy-path fixtures, but crown rejection/empty/unranked states can blank the hero. |
| Side data | Unsafe for two families | Now can select a different trip; Conditions can mix localities. |
| Destinations/mutations | Mostly canonical | Typed destinations and existing proposal writers are retained; malformed crown handling is not coherent. |
| Exposure | Partial | Viewport dwell exists; occlusion, foreground state, content revision, and persisted identity remain incomplete. |
| Mock/fixture proof | Insufficient | Canonical persona lane lacks most modules. |
| Backend-real/device | Not verified | No claim permitted. |

### 5.2 Places full-stack status

| Layer | Status | Review result |
|---|---|---|
| Producers | Partial/defective | Concurrent optional producers exist, but ordinary DB failures escape and timed-out threads continue. |
| Availability contract | Missing | Empty and unavailable collapse before transport. |
| Ranking | Existing substrate | Server-owned order remains; exposure quality is undermined by duplicate/false impressions. |
| Presentation model | Partial | Pure modeling exists, but viewport and search lifecycle state remain controller-local. |
| Renderer architecture | Incomplete | Existing families render, but the 2,383-line switch/renderer hot file is not the intended exhaustive family registry. |
| New Page-board registers | Mostly absent | Existing candidate/editorial/memory/social anatomy is not implementation of the new Group A and other proposed compositions. |
| Exposure | Partial/defective | Dwell and engagement ownership exist; initial measurement, remount dedupe, occlusion, foreground, and scroll performance remain open. |
| Backend-real/device | Not verified | No claim permitted. |

### 5.3 Aesthetic direction

The integration did not reveal a reason to change the chosen font families:

- EB Garamond remains appropriate for Vesper/editorial voice;
- system sans remains appropriate for UI, facts, and object titles;
- JetBrains Mono remains appropriate for stamps and compact metadata.

Typography automation currently passes: 99 reviewed raw-size exceptions, 78/78 declared roles used, and the Roman/system/mono face check is green. That does **not** close the visual review. The adopted memory card still carries a typography-role correction blocker in the composition inventory, highly tracked 8–9 px mono requires device/dynamic-type review, and system sans must be checked on both iOS and Android. No post-pivot whole-page capture has been accepted.

## 6. What passed review

The following should be preserved while correcting the findings:

1. **Design authority:** the external `vesper-home-surfaces` bundle is governed by hashes and is not copied into the repositories.
2. **Generated schema ownership:** transport changes flow through workspace OpenAPI snapshots and generated frontend types rather than handwritten shadow models.
3. **Backend selection order:** dedicated Trips modules are projected before the capped generic queue.
4. **Typed destination direction:** new routes use typed destination adapters; the defect is split renderability authority, not a return to arbitrary strings.
5. **Canonical mutation ownership:** the reviewed home changes did not add a competing proposal, booking, expense, or itinerary writer.
6. **Privacy:** no new path was found that interpolates private member facts into a group-visible card or message.
7. **Dreams receipt honesty:** “saved privately / learns” copy remains gated by the recorded receipt rather than a tap alone.
8. **Static quality:** frontend `tsc --noEmit` passes; the reviewed diffs pass `git diff --check`; typography budget, role usage, and Roman-only face checks pass.
9. **Focused tests:** independent agents ran 26 Places-focused and 76 Trips-focused tests successfully. Backend execution evidence recorded by the integration lane remains static/offline evidence only.

## 7. Evidence limits and misleading claims to avoid

Do not say:

- “renderer cutover complete” without qualifying that Trips semantic planning and Places family extraction remain in their roots;
- “mock-verified D2 page” while the canonical persona fixtures cannot produce most D2 modules;
- “producer failures are isolated” until actual DB/I/O exceptions and resource cancellation are tested;
- “empty and unavailable are distinct” while the wire collapses them;
- “viewport-aware impressions are correct” until lifecycle, occlusion, and foreground regressions pass; or
- “device-ready” or “accepted” until the governance receipt path exists and named iOS/Android scenarios have physical-device evidence.

The execution ledger correctly avoids claiming shipment and explicitly names missing backend-real/device gates. It should nevertheless be amended after fixes so its architecture and mock-evidence wording matches the narrower truth identified here.

## 8. Recommended remediation order and parallel lanes

### Batch A — state and data correctness

Run these in parallel with separate hot-file owners:

| Owner | Scope | Exit tests |
|---|---|---|
| Trips state owner | Unify crown renderability/presentation state; render empty/unranked/rejected states; decide rolling-deploy adapter | Screen tests for rejected crown + valid modules, empty with/without trips, persisted old payload, ranked crownless |
| Trips coherence owner | Key Now and Conditions side data to module trip/destination | Two-live-trip Now test; current-city vs trip-city weather test; explicit unavailable state |
| Places backend owner | Catch defined operational failures; introduce resource-layer budgets; preserve unavailable on transport | Actual SQLAlchemy/DBAPI exception test; blocking producer budget test; generated availability contract |
| Places lifecycle owner | Measure loading branch; root-owned dedupe; foreground/occlusion handling | Loading→resolved native layout, search unmount/remount, background dwell, header occlusion |

### Batch B — contract and telemetry coherence

1. Add backend Trips uniqueness invariants and defensive client rejection telemetry.
2. Define exposure unit and revision semantics; carry non-sensitive identity end to end.
3. Separate valid empty metrics from contract failures.
4. Add evidence receipt references and make `V=verified` representable.
5. Run the single schema train after backend contract changes.

### Batch C — architecture gate

1. Promote Trips plan to the one authority for membership, render state, action, exposure identity, and rhythm role.
2. Extract Places renderer families behind an exhaustive typed registry.
3. Replace Places per-frame scroll state with the shared ref-backed viewport registry.
4. Add canonical persona fixtures for all adopted whole-page states.
5. Make size, containment, and spacing checks green without raising baselines.

### Batch D — evidence and design acceptance

1. Run backend-real canaries for exact Trips and Places state fixtures.
2. Capture named iOS and Android widths, dynamic type, offline/stale/unavailable, and scroll/occlusion scenarios.
3. Review page rhythm against the external Page boards without copying them into the repository.
4. Attach immutable F/B/V receipts to the inventory and record the explicit acceptance verdict.

## 9. Verification performed during this review

| Check | Result |
|---|---|
| Frontend `git diff --check` across reviewed lane | Pass |
| Backend `git diff --check` across reviewed lane | Pass |
| Frontend `npm run typecheck` | Pass |
| `npm run typography-budget` | Pass: 99 reviewed exceptions |
| `npm run typography-role-usage` | Pass: 78/78 roles used |
| `npm run typography-roman-only` | Pass |
| External canon check for Trips and Places | Pass: 7/7 Trips pairs, 6/6 Places pairs, both against the Downloads bundle |
| Frontend API boundary / surface index | Pass: zero component escape hatches; 40 registered surfaces |
| `npm run size-budgets` | Fail: existing app debt plus reviewed Trips root at 1,504 lines |
| `npm run containment-budget` | Fail: 166 vs. baseline 162 |
| `npm run spacing-budget` | Fail: 363 vs. baseline 361 |
| Independent Places focused tests | Pass: 26; missing native lifecycle/occlusion/perf cases |
| Independent Trips focused tests | Pass: 76; missing cross-layer and canonical persona cases |
| Home-surface governance / living-doc links | Pass: authority + 33 compositions; 209 living Markdown files |
| Full docs inventory | Fail on four pre-existing unrelated unclassified working documents; this review is explicitly classified |
| Backend-real Postgres canary | Not run / not verified |
| Simulator or physical device | Not run / not verified |

## 10. Review verdict

Keep the integration branches as reviewable static/mock work, but do not promote them to backend-real or device acceptance. Correct Batch A before implementing more Page-board card families. Then close the plan/registry architecture gate and debt budgets so new composition work does not deepen the two hot roots.

The decisive target is not more components. It is one coherent chain per visible section:

```text
grounded producer
  → validated typed contract with honest availability
  → one composition/state authority
  → one render existence decision
  → one coherent destination or canonical mutation
  → one non-sensitive exposure identity
  → deterministic fixture
  → backend-real receipt
  → device acceptance
```

Until that chain exists, component presence should continue to be reported separately from production, reachability, actionability, fidelity, backend-real proof, and device proof.

## 11. Remediation update — 2026-08-09

The correction work below is intentionally recorded separately from the
original audit. It distinguishes a fixed code-path from an accepted product
surface; no backend-real or physical-device acceptance is implied.

| Finding group | Result | Implementation/evidence |
|---|---|---|
| Trips projection and state (P1-01, P1-02, P2-02, P2-04, P2-08, P2-09) | Corrected in static/mock lanes | Backend rejects duplicate semantic/module/content identities, separates valid empty from integrity failure, fingerprints visible content, and exposes all module fixtures. The app renders rejected/missing crowns as degraded, retains an unranked fallback, keeps module-specific side data scoped, and treats route rejection as an observable integrity state. |
| Places producer outcomes (P1-03, P1-04) | Corrected in backend lane | Optional producer failures now produce a closed, content-free unavailable-producer list; bounded executor work cancels queued timeouts and contains defined operational failures without swallowing programmer errors. |
| Places exposure/lifecycle (P2-05, P2-06, P2-07) | Corrected in app lane | The shared viewport registry accounts for chrome occlusion and foreground activity, waits for post-load measurement, deduplicates across search remounts, and only publishes visibility-set changes rather than per-frame scroll state. |
| Evidence governance (P1-05) | Corrected in workspace lane | F/B/V verification now requires a typed receipt reference; verified visual/device states require an immutable capture receipt instead of being categorically impossible. |
| Trips composition authority (P2-01) | Corrected at the selection/render seam | `buildTripsHomeSectionPlan` is consumed through a pure render model. It owns the selected slots; the root no longer performs first-wins `.find` selection, and route adaptation cannot silently remove rejected content. |
| Places renderer architecture (P2-10) | Corrected at the family seam | A `satisfies Record<PlacesCardKind, PlacesCardRendererFamily>` registry makes every generated card kind choose exactly one renderer family at compile time. Candidate, editorial, and experience presentation rules are pure modules; the feed remains the only exposure/controller boundary. |
| API contract registry | Corrected | Two pre-existing unadopted planning/save routes are explicitly `retiring`, rather than being represented as active mobile journeys. The complete combined contract audit passes. |

### Commits

| Repository/lane | Commits |
|---|---|
| Workspace governance | `361e809`, `627c006` |
| Backend home surfaces | `b36eedb0`, `00bffa05`, `05b811ac`, `1ba6c993` |
| App home surfaces | `4e690f37`, `5d399fd5`, `6734ad2c`, `8e0874b8` |

### Completed schema integration

After the concurrent save-model change was committed, the schema train ran
from committed backend sources only. The complete projection contains `368`
paths, `406` operations, and `940` schemas. The generated app schema is
current, and the Places presentation now distinguishes an honestly empty feed
from a partial producer outage with a retryable, content-free notice. No
handwritten frontend wire model was added.

### Post-remediation verification

| Check | Result |
|---|---|
| Backend Trips projection tests | Pass: 36 focused tests |
| Backend Places offline tests | Pass: 393; full suite retains one pre-existing Postgres-schema failure (`itinerary_projection_outbox.lease_token`) |
| Frontend focused regression tests after integration | Pass: 49 tests across Trips plan/render and Places feed/registry suites |
| Schema-integrated focused regression tests | Pass: 65 tests across Trips plan/render and Places feed/registry/presentation/workspace suites |
| Generated schema check | Pass: app schema matches `docs/openapi.app.json` |
| Frontend full Jest suite | Not clean: six unrelated pre-existing/environment-sensitive failures (memory queue, Atlas mock export, persona fixture, navigation contract, concierge assertion, and workspace-doc path assumptions). The touched 65-test Trips/Places suite passes. React `act()` console warnings also remain. |
| Frontend typecheck and test-contract typecheck | Pass |
| API boundary and query/mutation ownership checks | Pass |
| API operation audit | Pass: current snapshot 454 active / 8 dark / 56 retiring; combined export 452 active / 8 dark / 58 retiring |
| External canonical design check | Pass: 2 operator-owned home-surface bundles verified from `/Users/feihuyan/Downloads/vesper-home-surfaces` |
| Design/size ratchets | Size, containment, and spacing still have baseline-wide unrelated debt; new Trips functions are under the 800-line limit. |
| Backend-real/device acceptance | Not run; still required before acceptance. |
