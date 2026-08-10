---
doc_type: working
status: active
owner: frontend / backend / product
created: 2026-08-09
expires: 2026-09-08
why_new: Reconciles the post-consolidation Places and Trips implementation, the August external design authority, and the latest read-only code-review findings into one executable engineering plan.
source_of_truth_for:
  - home-surfaces-post-consolidation-engineering-plan
---

# Home Surfaces — Post-Consolidation Engineering Plan

## 1. Purpose

This document records the next engineering program for the Places and Trips
home surfaces after the August 9 consolidation. It combines:

- the external `vesper-home-surfaces` design bundle;
- the current consolidated frontend and backend source;
- the machine-readable composition inventory;
- the most recent state, full-stack, typography, card-rhythm, action, privacy,
  and telemetry code review;
- the project's MVP evidence rules.

The immediate objective is not to add more speculative card families. It is to
make the currently adopted surface honest, deterministic, polished, maintainable,
and provable before selecting another design family.

This is a working execution plan, not a claim that either surface has passed
backend-real or physical-device acceptance.

## 2. Review baseline

The investigation that produced this plan was read-only and pinned to:

| Repository / authority | Revision or identity |
|---|---|
| Frontend | `travel-app` at `f7549bd7` |
| Backend | `travel-agent` at `43ba3e4e` |
| Workspace composition inventory | `home-surfaces-composition-v1`, as of 2026-08-09 |
| External design authority | `vesper-home-surfaces-2026-08-09` |
| External bundle | Operator-owned `/Users/feihuyan/Downloads/vesper-home-surfaces` |

The external bundle remains outside the repositories. CI and production source
must not import or copy it. Local design review supplies it through
`HOME_SURFACES_CANON_DIR` and validates the registered content hashes.

The investigation found that the core consolidation work is present, but the
existing audit, roadmap, ledger, and inventory documents lag the final merged
implementation. Phase 0 below reconciles that documentation before it becomes
the basis for further dispatch.

## 3. Current implementation state

### 3.1 Inventory status

The current machine inventory has 33 rows:

| Adoption state | Count |
|---|---:|
| Adopted | 13 |
| Unresolved | 19 |
| Relocated | 1 |

Its evidence boundary is still static/source-only:

| Evidence layer | Current result |
|---|---|
| Fixture/visual, `F` | 33 not verified |
| Backend-real, `B` | 31 not verified, 2 not applicable |
| Physical device, `V` | 33 not verified |
| Immutable evidence receipts | 0 |

Several inventory rows combine implemented and missing variants. For example,
`trips-b-time` combines shipping Now and Countdown modules with an absent
temporal strip. These rows must be split before the inventory can accurately
drive implementation or adoption decisions.

### 3.2 What is implemented

#### Trips

- Thin route boundary into a controller and pure presentation/composition
  chain.
- Route-safe crown, dedicated Now, Countdown, Conditions, and Group modules.
- One bounded aggregate Also in Play queue.
- Physical page plan and exhaustive body-render phases.
- Standing Ask, Local Plans, Day Map, Companion, Dreams, Trip Feel, Trail,
  footer, and floating create entries with their current gates.
- Typed destinations and canonical proposal resolution paths.
- Section exposure boundaries and content revisions.

#### Places

- Server-produced, server-ordered section feed.
- Pure presentation and responsive render plans.
- Strict card kind/payload renderability guards.
- Candidate, editorial, experience, memory, social, notice, and prompt families.
- Conviction, single, fork, and choice client treatments; conviction remains
  intentionally unproduced.
- Responsive fork and experience-rail degradation.
- Viewport/focus/foreground/dwell-aware exposure handling.
- Grounded candidate reasons and compact collection counts.
- Typed handoffs for place details, reader, map, saved collections, private
  debrief, and Trips-owned add-to-day preview/commit.

### 3.3 What is not implemented end to end

- `saved_unvisited` and the Places raised-return composition: no trustworthy
  visit signal.
- Places conviction: no non-proximity confidence signal.
- Singular Places lead-versus-peer hierarchy: the existing `lead=true` means
  equal complete treatment for both gap alternatives.
- `reachable_cluster`: declared map story kind without a producer and without
  complete composition-coherence validation.
- Expanded map selectors/compositions over crossings, neighborhoods,
  destinations, and members.
- Durable Trip Feel persistence, resumption, reduced, and contrast states.
- Several new return, personal-record, hosting, evidence/decision, temporal,
  and social compositions represented in Page or Prototype boards.
- Backend-real and physical-device acceptance for every inventory row.

These gaps are not all an implementation backlog. Some are deliberately dark,
exploratory, signal-blocked, or awaiting an adoption decision.

## 4. Confirmed review findings

All findings below were rechecked against the consolidated source rather than
copied forward from an older audit.

### 4.1 P1 — state and product-truth defects

#### HS-P1-01 — Trips assembly failure becomes authoritative empty

The Concierge Home delivery boundary catches assembly exceptions and returns a
quiet empty fallback. Trips projects that feed as `projection_state="empty"`,
discarding the degradation distinction. The client can therefore show “nothing
needs attention” during a producer or database outage.

Required behavior:

- Concierge Home may retain its quiet, usable fallback.
- Trips Stack must expose a retryable failure/degraded read, never an
  authoritative empty projection.
- Cached ranked content remains visible when available.
- Without ranked cache, committed trips remain reachable through an explicit
  unranked/degraded state.

#### HS-P1-02 — weather inputs are absent from the query identity

`precipitation_mm` and `wind_kph` affect backend weather production and ranking
but do not participate in the frontend query key. A material weather change can
therefore leave an older crown or nearby ordering cached under the same key.

#### HS-P1-03 — offline Trips can remain in initial loading

The page-state reducer checks a pending stack before returning the cached/offline
state. A user with cached committed trips but no stack projection can remain on
“Vesper is reading your trips” indefinitely while offline.

The implementation currently conflates:

- cached trip-list content;
- cached ranked-stack content;
- placeholder content from a previous ambient key.

These must become separate state inputs.

#### HS-P1-04 — Day Map uses the wrong feature gate

`TRIP_EDITORIAL_MAP_ENABLED` has no production consumer. Day Map membership is
tied to `LOCAL_PLAN_DOGFOOD_ENABLED`, while its endpoint is queried even when the
map surface is dark.

#### HS-P1-05 — zero-renderable partial Places feed becomes a blank page

Any unavailable producer currently makes a feed `partial`, even when no section
has a renderable card. Workspace then says “Showing what’s available” and mounts
an empty feed instead of showing an honest unavailable/retry state.

### 4.2 P2 — action, cache, telemetry, and polish defects

#### Trips

- Terminal proposal cache subtraction filters legacy `rows` but not the current
  `queue`.
- Previous-location placeholder projection data can appear current during
  ambient re-keying.
- Standing Ask follows legacy `heroKind` rather than authoritative server
  posture.
- Loading shows a gold `See all N trips →` label that has no interaction and is
  hidden from accessibility.
- Local Plans and Day Map share a wrapper without a child gap, creating
  touching/doubled outlined borders.
- A disabled Ambient surface still triggers its real trip-home feed query and
  potential LLM-composed work.
- Aggregate queue exposure uses revision bundles as identity rather than stable
  fact/content IDs.
- A Day Map image failure can return `null` after the parent has already
  allocated cluster rhythm.

#### Places

- Loading visibly renders transport copy as the Vesper standfirst even though
  the surface contract requires transport copy to remain accessibility-only.
- Full-width editorial supporting previews use 12pt System Sans caption rather
  than the approved bounded serif reading role.
- Partial-producer and failed-refresh notices can render simultaneously.
- Door routing is non-exhaustive; a future `guide` target falls through to Map.
- A candidate with `verb=save` can label its detail-navigation tap as Save even
  though the actual save is a separate control.
- The new two-line grounded reason has static bounds but no device evidence for
  the longest title/meta/kicker/reason/action combination.

### 4.3 P3 — architecture and governance debt

- `PlacesWorkspace.tsx` is 768 lines against a 769-line ratchet and owns query,
  location, search, root states, mast, navigation, and feed wiring.
- `TripsHomeController.ts` is 809 lines against an 825-line ratchet.
- `TripsHomeBody.tsx` remains a large physical dispatcher at 745 lines.
- The legacy `utils/placesWorkspace.ts` is test-only and preserves an older
  client-owned scope model.
- The composition inventory and execution ledgers do not reflect all merged
  work or the latest review findings.

## 5. Non-negotiable boundaries

### 5.1 Design authority

- Read the external Build Manifest first.
- Use `Canon - Home Surfaces` for vocabulary, not current implementation state.
- Use `Places - The Page` and `Trips - The Page` for the composition under
  review.
- Treat `As Built` boards as implementation history.
- Do not implement superseded or exploratory boards as accepted product.
- Preserve Places page-rhythm variant A. Variants B–H remain explorations.
- Source material recipes in `constants/cardSurface.ts` win over inaccurate
  visual approximations in a board.

### 5.2 Product truth

- No plausible stub may look live.
- Empty, unavailable, degraded, stale, and offline are distinct states.
- Places never mutates an itinerary directly.
- A private constraint never enters group-visible copy or projection data.
- Proposal, itinerary, booking, and expense writes remain on their canonical
  ledgered paths.
- Component presence is not the same as production reachability or acceptance.

### 5.3 Completion language

Static tests, mock walks, backend-real canaries, and physical-device evidence
are separate layers. No family is “accepted,” “complete,” or “certified” until
the exact claimed layer has an immutable receipt.

## 6. Target architecture

### 6.1 Trips

```text
route
  -> controller/orchestration
    -> exact server/query snapshots
      -> pure presentation model
        -> physical page plan
          -> exhaustive body render plan
            -> leaf renderer
```

The page plan owns membership, order, state, action/passivity, identity,
containment, and adjacency rhythm. A leaf must not silently return `null` after
the plan has allocated a section. Runtime resource failures, such as a map image
failure, return to the page plan as typed availability.

### 6.2 Places

```text
server producers and ranking
  -> generated PlacesFeed
    -> strict renderability projection
      -> presentation model
        -> responsive render plan
          -> section/exposure executor
            -> exhaustive card-family renderer
```

The client never introduces a second semantic order, promotes attrition into
conviction, or interprets a wide payload as a component/style instruction.

### 6.3 Shared infrastructure

Trips and Places may share:

- semantic text primitives;
- containment/material vocabulary;
- viewport/exposure infrastructure;
- evidence receipts and state vocabulary.

They must not share one page engine. Trips is an authored physical sequence;
Places is a server-produced feed.

## 7. Engineering roadmap

### Phase 0 — reconcile baseline and inventory

Work:

1. Wait for concurrent consolidation/cleanup to leave clean child branches.
2. Re-run frontend, backend, generated-contract, and governance baselines on one
   immutable revision.
3. Split mixed inventory rows:
   - Now/Countdown versus temporal strip;
   - current editorial reading versus new reading registers;
   - Today Mapped versus expanded maps;
   - current Trip Feel question versus persistence/resumption.
4. Record the current producer, contract, renderer, action, and reachability for
   every independently adoptable composition.
5. Add HS-P1/P2/P3 findings to the active ledger.
6. Retain `F/B/V=not_verified` until real receipts exist.

Exit:

- clean repositories;
- current generated contracts;
- one inventory row per independently adoptable composition;
- exact baseline commands and results recorded.

### Phase 1 — state and data honesty

#### Package TR-HONEST-1 — backend degradation

Recommended compatibility-safe implementation:

- Add an internal/excluded delivery-state marker to `ConciergeHomeFeed`.
- Mark `degraded_home_feed()` explicitly.
- Keep Concierge Home's quiet 200 response.
- Make `/trips-stack` return a retryable service failure when its source feed is
  degraded instead of projecting `empty`.

This reuses the existing frontend projection-error fallback and avoids adding a
new public projection enum that old clients may mishandle.

Tests:

- main Home fallback remains usable;
- Trips Stack does not return `empty` after assembly failure;
- promotion reads do not convert the failure into ranked truth;
- endpoint error remains authorization-safe and contains no exception detail.

#### Package TR-HONEST-2 — offline and ambient identity

- Add rounded precipitation and wind inputs to `homeFeedKeyParams`.
- Model cached trip list, cached ranked projection, and placeholder projection
  separately.
- Use TanStack's `isPlaceholderData` as a presentation input.
- Preserve non-location content while clearly marking refresh.
- Suppress location-sensitive modules from a previous key.
- If the placeholder crown is weather/Near You-derived, render the explicit
  unranked fallback until the exact projection arrives.
- Render offline-unranked trips when committed trips exist but the stack does
  not.

Required matrix:

| Network/query state | Expected result |
|---|---|
| Offline + cached projection | Cached ranked content + offline notice |
| Offline + committed trips only | Unranked trips + offline notice |
| Offline cold | Offline empty/error posture with retry |
| Ambient re-key + ordinary crown | Clearly stale/refreshing content |
| Ambient re-key + ambient crown | Ambient crown/module withheld |
| Refresh error + ranked cache | Cached content + one stale notice |

#### Package PL-HONEST-1 — Places availability

- Permit a feed-backed presentation model to classify `unavailable`.
- Derive availability from both unavailable producers and renderable section
  count.
- When nothing is renderable and any producer is unavailable, show one honest
  unavailable/retry state.
- Introduce a pure notice-precedence adapter:
  `offline > failed refresh with cache > partial producer failure`.
- Never render two state banners for one snapshot.

Phase 1 parallelism:

- backend degradation owner;
- Trips query/state owner;
- Places presentation/state owner.

The Trips and Places root hot files remain single-owner within their lanes.

### Phase 2 — actions, gates, cache, and telemetry

#### Package TR-GATES-1

- Gate Day Map membership with `TRIP_EDITORIAL_MAP_ENABLED`.
- Disable the editorial-map query while the gate is dark.
- Disable the trip-home/Ambient query while `AMBIENT_ENABLED` is dark, unless a
  separate visible consumer is explicitly introduced.
- Derive Standing Ask membership and copy from authoritative projection posture.
- Make the loading “See all” affordance a real accessible action or remove its
  door styling.

Hot-file lock: one owner for `TripsHomeController.ts`,
`tripsHomePageComposition.ts`, and `TripsHomeBody.tsx`.

#### Package TR-CACHE-1

- Subtract resolved proposals from `queue`, `rows`, and crown.
- Add mixed current/legacy projection fixtures.
- Preserve authoritative refetch while ensuring stale actionable UI disappears
  immediately.

#### Package TR-TELEMETRY-1

- Build aggregate queue content identity from stable item content IDs.
- Keep content revision as a separate stable hash of IDs and revisions.
- Specify whether an aggregate impression means the queue frame was visible or
  each individual row was visible.
- Do not add a backend fatigue consumer until that semantic decision is explicit.

#### Package PL-ACTIONS-1

- Replace door fallthrough with an exhaustive generated-union switch.
- Decide whether `guide` maps to the existing reading collection or is removed
  from the currently unproduced contract.
- Assert exhaustiveness in tests; remove invalid legacy `map` fixture values.
- Separate candidate navigation labeling from save verb labeling.

### Phase 3 — polish the adopted baseline

Do not redesign the whole page rhythm in this phase.

#### Package PL-POLISH-1

- Keep Places loading standfirst geometry without visibly typing transport
  status as authored voice.
- Retain transport copy in the progress accessibility label.
- Render full-width editorial supporting previews in the approved bounded Roman
  serif role; keep compact forks within their measured content envelope.
- Exercise the longest title/meta/kicker/reason/action candidate at 320, 360,
  and 393pt, normal and approximately 1.35 font scale.
- Review candidate copy height against the fixed 92pt plate.

#### Package TR-POLISH-1

- Add plan-owned separation between Local Plans and Day Map.
- Feed map image availability back into the body render plan so a failed image
  removes the section and its rhythm together.
- Verify Crown -> Conditions -> Group -> queue adjacency with long real copy.
- Verify footer and floating-create clearance above both tab implementations.

#### Blocked package PL-LEAD-1

Do not style `lead=true` as a singular winner. The current gap producer assigns
it to both alternatives to mean equal complete treatment. If product adopts a
lead/peer hierarchy, add a new explicit server-owned semantic such as
`presentation_role: lead | peer`; do not reinterpret the existing boolean.

### Phase 4 — architecture headroom

Correctness and bounded visual changes land before these behavior-preserving
extractions.

#### Places extraction

Split `PlacesWorkspace` into:

- query/context/location controller hook;
- pure root-state presentation adapter;
- search-door composition;
- notice/state frame;
- existing feed executor.

Delete or formally retire the test-only legacy `utils/placesWorkspace.ts`.
Ratchet file sizes only after the extraction passes characterization tests.

#### Trips extraction

Extract from the controller:

- ambient/editorial-map/reading ancillary queries;
- stable action/navigation adapters;
- local resource-availability state;
- telemetry adapters.

Extract from the body:

- phase renderers that own no state discovery;
- typed cluster renderers;
- runtime unavailable-to-plan reconciliation.

Target at least 20% headroom below root/controller ratchets before adding a new
family. Line count is not the architecture goal; singular responsibility and
stable ownership are.

### Phase 5 — product decision packet

Resolve the unresolved inventory in six packets:

1. Places registers, lead/peer semantics, doors, comparison/stack/stub.
2. Places root maps, return, friend/co-sign, and personal record.
3. Trips Near You, temporal strip, and Your People.
4. Trips evidence/decision, draft shelf, Local Plans extensions, hosting,
   pretrip, and return.
5. Today Mapped versus expanded map concepts.
6. Trip Feel persistence, resumption, reduced, and contrast states.

Every decision records:

- adopted, exploratory, deferred, rejected, or relocated;
- evidence required to render honestly;
- producer and schema owner;
- destination or canonical mutation owner;
- privacy/audience classification;
- next review date.

Recommended near-term rulings:

- Adopt the existing Places count door independently from speculative quiet
  panel variants.
- Adopt existing Now and Countdown independently from the missing temporal
  strip.
- Decide whether Today Mapped is production, internal dogfood, or dark.
- Decide Trip Feel persistence before adding more tile states.
- Defer saved-unvisited, raised return, conviction, and reachable cluster until
  their missing signals exist.

### Phase 6 — new vertical slices

Only begin after the adopted baseline has backend-real and device evidence.

Recommended order:

1. Today Mapped, because most producer/contract/renderer/action plumbing exists.
2. One deliberately adopted Places reading register using existing dossier
   identity and a real reader destination.
3. Trip Feel persistence/resumption, if adopted.
4. A dedicated Near You receipt and composition.
5. Return or personal-record families only after their signals and destinations
   exist.

Continue to defer:

- visit-dependent saved-unvisited and raised return;
- non-proximity conviction;
- reachable cluster;
- hosting;
- co-sign, Again, belonging, tally, and rhythm;
- expanded multi-person maps.

### Phase 7 — backend-real and device acceptance

#### Backend-real matrix

- Trips source degradation.
- Ambient weather re-ranking.
- Offline/cached stack behavior.
- Fully unavailable and partially unavailable Places feed.
- Proposal resolution removing queue content.
- Private reasoning and friend-sharing boundaries.
- Day Map membership, authorization, and no-data behavior.
- Canonical mutation destinations and durable receipts.

#### Device matrix

- iOS and Android.
- 320/360/393-equivalent widths.
- Normal and large Dynamic Type.
- Loading, empty, partial, stale, offline-cached, offline-cold, and error.
- Map image failure and permission denial.
- Background/foreground exposure dwell.
- Long and short canonical pages.
- Bottom navigation and floating affordance clearance.

Every accepted inventory row receives separate F/B/V receipts with the design
hash, fixture or backend state, platform, width, font scale, date, and reviewer.

## 8. Parallel dispatch model

Use at most three implementation workers plus one integration coordinator.

| Wave | Worker A | Worker B | Worker C | Serialized handoff |
|---|---|---|---|---|
| 0 | Frontend baseline | Backend baseline | Inventory/governance | Coordinator records exact SHAs |
| 1 | Backend degradation | Trips state/query | Places availability | Cross-repo behavior gate |
| 2 | Trips root/gates | Cache/telemetry utilities | Places actions | Root hot-file integration |
| 3 | Trips polish | Places polish | Responsive/state fixtures | Visual characterization |
| 4 | Trips extraction | Places extraction | QA/evidence harness | Architecture and budget gate |
| 6+ | One backend/schema family | One Trips or Places frontend family | QA/canary | Schema sync then vertical integration |

### Hot-file locks

The following files may have only one owner in a wave:

- `components/trips/TripsHomeController.ts`
- `components/trips/TripsHomeBody.tsx`
- `utils/tripsHomePageComposition.ts`
- `components/places/PlacesWorkspace.tsx`
- `components/places/PlacesSectionFeed.tsx`
- `utils/placesPresentationModel.ts`
- workspace OpenAPI snapshots and generated frontend schema

Workers stage explicit filenames only and report:

- base SHA;
- touched paths;
- tests and exact results;
- compatibility statement;
- evidence receipts created;
- known remaining risks.

## 9. Validation gates

### 9.1 Frontend static/mock

Focused suites include:

- `homeSurfaceStateMatrix.test.ts`
- `tripsHomePresentationModel.test.ts`
- `tripsHomePageComposition.test.ts`
- `tripsHomePageSectionPlan.test.ts`
- `tripsHomeBodyRenderPlan.test.ts`
- `invalidateHomeProjections.test.ts`
- `placesPresentationModel.test.ts`
- `PlacesWorkspaceState.test.tsx`
- `PlacesWorkspaceLoading.test.tsx`
- `PlacesSectionFeed.test.tsx`
- `placesWorkspaceFeedNavigation.test.ts`

Repository gates:

```bash
npm run typecheck
npm run test:typecheck:contracts
npm run api-boundaries
npm run home-surface-budgets
npm run verify:fast
npm test -- --ci --runInBand --no-cache
HOME_SURFACES_CANON_DIR=/absolute/path/to/vesper-home-surfaces \
  npm run qa:design:check -- places-workspace
HOME_SURFACES_CANON_DIR=/absolute/path/to/vesper-home-surfaces \
  npm run qa:design:check -- trips-home
```

### 9.2 Backend

Focused suites include:

- `tests/api/test_concierge_home.py`
- `tests/home/test_trips_stack_projection.py`
- `tests/home/test_trips_stack_projection_identity.py`
- `tests/places/test_feed_orchestration.py`
- `tests/places/test_sections_contract.py`
- `tests/places/test_supporting_copy.py`

Then run the complete relevant offline and Postgres-backed gates with the
repository virtual environment, plus Ruff and formatting checks.

### 9.3 Cross-repo contract

For every backend schema or route change:

1. Change backend source and tests.
2. Run the workspace type-sync workflow.
3. Review `docs/openapi.json`.
4. Review `docs/openapi.app.json`.
5. Review `travel-app/utils/api/schema.gen.ts`.
6. Fix frontend type and behavior fallout.
7. Deploy additive backend compatibility before client reliance.

The recommended Trips degradation solution avoids a new public enum and may not
require generated-type changes, but the contract check still runs.

### 9.4 Evidence

```bash
npm run qa:polish:scenarios
npm run qa:surface -- trips-home --after
npm run qa:surface -- places-workspace --after
```

A dry run proves only the harness. It is not visual or device evidence.

## 10. Commit and merge boundaries

Recommended narrow commits:

1. Backend degraded-source truth.
2. Trips offline/placeholder/query identity.
3. Places unavailable state and notice precedence.
4. Trips feature gates and dark-query suppression.
5. Proposal queue reconciliation.
6. Trips exposure identity.
7. Places exhaustive door routing and accessibility semantics.
8. Places loading and typography polish.
9. Trips Local Plans/Day Map rhythm and runtime failure handling.
10. Places root extraction.
11. Trips controller/body extraction.
12. Inventory and evidence receipts.

Do not mix:

- schema generation with unrelated UI work;
- route centralization with visual layout changes;
- architecture extraction with behavior fixes;
- design-adoption decisions with implementation commits;
- evidence-only changes with source behavior.

## 11. Definition of success

The immediate program—Phases 0 through 3—succeeds when:

- no backend failure appears as authoritative empty truth;
- offline, placeholder, stale, partial, unavailable, and empty states are
  distinct and covered;
- dark features do not fetch or incur model work;
- actions and doors are exhaustive, accessible, and owned by their canonical
  destination;
- current adopted card typography and rhythm match the August direction at
  representative widths and text scales;
- focused and broad automated gates are green on one immutable revision;
- the inventory accurately separates implemented, unresolved, gated, and
  signal-blocked work.

The broader program succeeds only when adopted families also have backend-real
and physical-device receipts. Another component existing in the source tree is
not a completion criterion.

## 12. Source landmarks

### Authority and status

- External `HANDOFF.md`
- External `Build Manifest - Both Surfaces.dc.html`
- External `Places - The Page.dc.html`
- External `Trips - The Page.dc.html`
- `docs/status/home-surfaces-composition-inventory.json`
- `docs/home-surfaces-section-card-ledger-2026-08-09.md`

### Frontend

- `components/trips/TripsHomeController.ts`
- `components/trips/TripsHomeBody.tsx`
- `utils/tripsHomePageComposition.ts`
- `utils/tripsHomePageSectionPlan.ts`
- `utils/homeSurfaceStateMatrix.ts`
- `data/conciergeHome.ts`
- `components/places/PlacesWorkspace.tsx`
- `components/places/PlacesSectionFeed.tsx`
- `utils/placesPresentationModel.ts`
- `utils/placesFeedRenderPlan.ts`

### Backend

- `backend/api/routes/concierge_home.py`
- `backend/home/concierge_feed/fallback.py`
- `backend/home/concierge_feed/models.py`
- `backend/home/trips_stack.py`
- `backend/core/models/places_sections.py`
- `backend/places/`
