---
doc_type: working
status: active
owner: frontend / backend / product
created: 2026-08-09
expires: 2026-09-08
why_new: Defines the component, section, card-polish, consolidation, and backend-plumbing program that must precede new canonical home-surface families.
---

# Home Surfaces — Engineering Foundation and Polish Plan

**Date:** 2026-08-09

**Design authority:** external hash-pinned `vesper-home-surfaces` bundle

**Frontend base:** `codex/home-surfaces-app-next` at `77fd99cd`

**Backend base:** `codex/home-surfaces-backend-next` at `8aa85d3b`

**Workspace base:** `codex/home-surfaces-coordination` at `fd8a602`

**Program boundary:** existing Places and Trips sections, components, cards,
states, and their required read plumbing. New unresolved design families are out
of scope until this foundation exits.

## 1. Outcome

Before adding another canonical design family, make the two existing home
surfaces easy to reason about, safe to extend, visually consistent, and provable
with real data.

The engineering foundation exits when:

1. every currently rendered section has one membership/state authority;
2. every card belongs to one renderer family with local props and local styles;
3. every outer gap and containment edge comes from the section plan/feed frame
   and named `CardSurface` recipes;
4. no screen component receives an unbounded controller prop bag;
5. Trips module side data is coherent with the module's trip/locality;
6. Places producers populate existing reason/note/count fields only from
   grounded evidence;
7. backend projection and producer hot files have stable extraction seams;
8. mock and real contracts are generated from the same OpenAPI projection;
9. current sections have deterministic state fixtures and structured visual
   verdicts; and
10. group-visible data and card mutations still use their privacy-safe,
    canonical domain paths.

This is engineering enablement, not authorization to build all 98 board frames.

## 2. Current engineering baseline

### 2.1 Frontend

| Surface | Current seam | Current debt |
|---|---|---|
| Trips | `TripsHomeController` -> `TripsHomeBody` | Controller file 833 lines, body 842 lines, and the body destructures roughly 80 controller fields. Renderability is partly in the pure plan and partly in controller booleans. |
| Trips | `TripsHomeSectionPlan` + `TripsHomeSectionRenderModel` | Good membership and identity foundation, but unavailable/dark states, leaf existence, containment, and all adjacency rhythm are not fully owned by the plan. |
| Trips | `TripsHomeStyles.ts` | 1,483-line shared style namespace used by Views, Table, and Trail; containment audit finds nine hand-rolled card shapes in this file. |
| Trips | Crown | `TripsStackCrown.tsx` is 516 lines and `TripsCrownReceiptBody.tsx` is 655 lines; receipt dispatch is typed but visual and action shells remain concentrated. |
| Places | `PlacesPresentationModel` -> `PlacesSectionFeed` | Good pure adapter and exhaustive renderer-family switch. The feed is now 498 lines, but still owns section boundary, presentation selection, and family wiring together. |
| Places | Renderer family modules | Candidate, editorial, experience, memory, social, and notice/prompt components exist. Family styles still live primarily in one 380-line `placesFeedStyles.ts` imported by eight modules. |
| Places | `PlacesWorkspace` | 769 lines and still owns chrome, search, request-state branches, viewport, scope, and feed integration. |
| Shared | Exposure | Seventeen `SectionExposureBoundary` call sites across the two roots repeat identity/layout/dwell wiring. The primitive is sound; surface-specific adapters are missing. |
| Shared | Design budgets | Spacing and typography gates pass. Containment is 166 against a 162 floor; Trips Home contributes the largest named cluster. Global size gates remain red for unrelated legacy files, so this program must use local no-regression budgets rather than claiming a global fix. |

### 2.2 Backend

| Surface | Current seam | Current debt |
|---|---|---|
| Trips | `backend/home/trips_stack.py` | 1,234 lines combine public models, receipt models, projection, posture, content revisions, destination mapping, and receipt construction. |
| Trips | `backend/home/concierge_feed/producers.py` | 3,219 lines contain orchestration plus group, readiness, settlement, invite, saved, memory, weather, nearby, local, and starter producers. New home-card work would intensify a single-writer hotspot. |
| Trips | Dedicated module contract | Modules are typed and revisioned, but `availability` can only be `available`. The model comment explicitly acknowledges that unavailable side receipts require a later typed view model. |
| Places | `backend/places/sections.py` | 646 lines combine request orchestration, optional producer handling, saved reads, and pure section/card projection helpers. |
| Places | Card supporting copy | `PlacesCard.reason` is rendered by the app but populated by no producer. `PlacesSection.note` and `.count` are sparsely populated. |
| Places | Reliability | Optional producer isolation, bounded blocking work, end-to-end response timeout, partial availability, and producer metrics now exist. The next work should build on those seams, not replace them. |

## 3. Architecture boundaries

### 3.1 Shared only where semantics are truly shared

The two pages do not become one generic feed engine.

Shared code may cover:

- design tokens and `CardSurface` recipes;
- section exposure/dwell plumbing;
- action-adapter conventions;
- state-fixture and visual-verdict tooling;
- content-revision helpers; and
- generated transport types.

Trips remains an authored sequence. Places remains a server-produced ranked
feed.

### 3.2 Frontend layers

```text
data bridge
  -> generated contract adapter
  -> pure page/section model
  -> surface section boundary
  -> family renderer
  -> leaf card/component
```

Rules:

- leaf cards receive presentation data and local actions, not query objects;
- renderers do not fetch;
- screens and UI components read backend data only through `data/`;
- outer spacing is absent from cards;
- family styles live with the family;
- no generic `metadata`, style bag, or backend-provided component name; and
- a leaf returning `null` cannot leave a section wrapper gap.

### 3.3 Backend layers

```text
domain readers / canonical writers
  -> grounded family producer
  -> card/section projection
  -> ranking and availability envelope
  -> generated OpenAPI contract
```

Rules:

- producer failures are unavailable, not empty truth;
- supporting copy names its evidence basis or stays absent;
- no private 1:1 constraint is interpolated into group-visible copy;
- Places routes to Trips/booking/proposal writers and never duplicates them;
- accepted/rejected mutations produce their canonical durable receipts; and
- new projection fields are additive and discriminated.

## 4. Work packages

## EF-0 — Baseline, locks, and ledgers

### EF-0A · Make visual runs single-owner

**Risk:** safe tooling

**Files:** `scripts/polish-qa/`, its tests, and surface manifests only

Work:

- add a per-simulator/UDID run lock with stale-owner detection;
- create the run directory before scenario preflight so failed attempts retain
  a diagnosable receipt;
- refuse a second simultaneous run on the same simulator;
- keep retry screenshots attempt-local;
- add tests for collision, stale lock, failed preflight, and retry cleanup.

Exit:

- one runner cannot silently contend with another;
- a failed run cannot be mistaken for fresh screenshot evidence; and
- `qa:polish:test`, doctor, and dry-run paths pass.

### EF-0B · Freeze current section/card inventory

**Risk:** static trace

**Files:** workspace inventory/ledger only

For every current section record:

- producer/read source;
- generated contract type;
- pure-model entry;
- renderer family;
- containment recipe;
- action owner;
- exposure identity;
- fixture scenarios; and
- evidence layer.

This is a source-derived inventory. It does not copy design HTML or screenshots.

Exit: every currently rendered section is in the ledger, including dark and
unavailable states, and every entry names an importer.

## EF-1 — Frontend consolidation seams

### EF-1A · Trips screen contract

**Risk:** parity-sensitive, founder review if order changes

**Owned files:** `TripsHomeController.ts`, new Trips screen-model files, focused
tests

Create a bounded `TripsHomeScreenModel` with four top-level domains:

```ts
type TripsHomeScreenModel = {
  page: TripsHomePageModel;
  sections: TripsHomeSectionRenderEntry[];
  actions: TripsHomeActions;
  chrome: TripsHomeChromeModel;
};
```

Work:

- stop returning raw queries, router, hooks, and dozens of duplicate leaf
  booleans to the body;
- group actions by domain rather than one callback per leaf;
- keep refresh/chrome orchestration in the controller;
- move display-ready state into pure builders;
- remove dead returned values such as unused loading aliases; and
- preserve current rendering exactly in this package.

Budget:

- body consumes no more than four top-level props/models;
- no raw React Query result enters a leaf renderer;
- no new direct `hooks/` data import from a screen/component.

### EF-1B · Trips section plan v3

**Risk:** parity-sensitive

**Owned files:** `utils/tripsHomeSectionPlan.ts`,
`utils/tripsHomeSectionRenderModel.ts`, tests

Promote the plan to own:

- authored order;
- section existence and render state;
- containment recipe/step;
- adjacency rhythm role;
- content identity/revision;
- typed action/passivity;
- grounding and rejection reason; and
- telemetry identity.

Remove controller-owned `showNowSection`, `showCountdownSection`,
`showConditionsSection`, and `showGroupSection` decisions once their exact leaf
requirements are represented in the plan.

Exit: the body iterates/render-switches over accepted entries; a rejected or
empty entry cannot allocate space or telemetry.

### EF-1C · Trips renderer and section boundaries

**Risk:** safe frontend after EF-1A/B

**Owned files:** `components/trips/home/` new modules, `TripsHomeBody.tsx`

Create surface-specific boundaries and renderers:

```text
TripsPlannedSectionBoundary
TripsHeroSectionRenderer
TripsDedicatedModuleRenderer
TripsQueueSectionRenderer
TripsSupportingSectionRenderer
```

The boundary owns exposure layout/dwell wiring for a plan entry. Renderers own
only the switch from semantic entry to leaf component. Leaf cards retain their
existing local actions.

Exit:

- repeated exposure boilerplate is removed from the body;
- the authored sequence remains obvious in one small file; and
- adding a current section state does not require editing controller, body,
  telemetry, and spacing independently.

### EF-1D · Places workspace/feed contract

**Risk:** parity-sensitive

**Owned files:** `PlacesWorkspace.tsx`, `PlacesSectionFeed.tsx`,
`placesPresentationModel.ts`, focused tests

Work:

- keep request/search/scope/chrome state in Workspace;
- pass one bounded `PlacesFeedViewModel` plus action and viewport adapters to
  the feed;
- move section exposure wiring to `PlacesFeedSectionBoundary`;
- keep the renderer-family switch exhaustive;
- represent responsive fork/rail mode in presentation data rather than
  recomputing it across leaves; and
- retain backend order as the only membership order.

Exit: Workspace does not know leaf card kinds, and the feed does not know query
or scope-fetch mechanics.

## EF-2 — Style, material, and component ownership

### EF-2A · Trips style strangler

**Risk:** visual polish

Split `TripsHomeStyles.ts` by current owner without changing values first:

- `TripsHomeViews.styles.ts`
- `TripsHomeTable.styles.ts`
- `TripsHomeTrail.styles.ts`
- crown/receipt family styles
- small shared geometry/tokens only where two or more components intentionally
  use the same named rule

After the mechanical split:

- delete unused rules;
- replace the nine hand-rolled Trips Home containers with the correct named
  recipe or document why a shape is not containment;
- remove per-card outer margins; and
- preserve exact spec values when no token fits instead of rounding.

Exit:

- no catch-all Trips Home style namespace;
- home-surface containment count decreases rather than raising the floor;
- spacing and typography budgets remain green; and
- source recipes match the canonical containment meaning.

### EF-2B · Places family style ownership

**Risk:** visual polish

Replace the shared `placesFeedStyles.ts` dependency with:

- section/header/frame styles;
- candidate family styles;
- editorial family styles;
- experience family styles;
- memory/social styles; and
- notice/prompt styles.

Keep `cardGeometry.ts` as the explicit cross-family geometry comparison point.
Do not build a generic card theme object.

Exit: each renderer imports only its family styles and shared primitives; a
candidate polish change cannot silently alter memory, editorial, or experience
cards.

### EF-2C · Crown and receipt decomposition

**Risk:** parity-sensitive; mutation paths present

Split shell, identity header, authored voice, receipt dispatcher, confirmation
control, and action footer into explicit components. Preserve these roles:

- identity block opens the trip;
- primary action opens the typed card destination;
- receipt is proof and not a hidden tap target;
- confirm/reject uses the canonical proposal resolver; and
- missing grounded voice remains absent rather than templated.

Exit: each receipt can be fixture-tested and polished independently without
changing crown navigation or confirmation behavior.

## EF-3 — Existing section/card polish

Polish happens after the ownership splits so fixes land in their permanent
home. Every batch uses current sections only.

### Trips batches

| Batch | Sections/cards | Primary review |
|---|---|---|
| TR-P1 | Consequence, location disclosure, mast, crown shell, all current receipts | hierarchy, grounding, action separation, 320/393 width, Dynamic Type |
| TR-P2 | Now, countdown, conditions, group, Also in Play | containment sequence 2 -> 5 -> 3 -> 2 -> 0, fact coherence, section collapse, queue depth action |
| TR-P3 | Standing Ask, Local Plans, Today Mapped, Companion | feature-gate honesty, destination truth, private conversation boundary, no duplicated hero |
| TR-P4 | Dreams in Taste, current Trip Feel, Connect, contextual trail, Near You, footer, create FAB | page rhythm, private learning receipt, bottom-nav clearance, no pressure/count inflation |

### Places batches

| Batch | Sections/cards | Primary review |
|---|---|---|
| PL-P1 | Candidate/place, area, city, section door | plate geometry, title/meta/reason hierarchy, lead treatment, save/add-to-day actions |
| PL-P2 | Editorial cover and fork | Roman editorial hierarchy, deck/preview distinctness, reader destination, responsive stack |
| PL-P3 | Experience rail/stack | media fallback honesty, timing/availability, horizontal-to-stacked policy, save/detail actions |
| PL-P4 | Memory and friend | source authorization, passive social treatment, destination truth, bounded personal history |
| PL-P5 | Notice and prompt | urgency material, acknowledgement owner, irreversible-looking copy, retry/error states |
| PL-P6 | Mast, scope, search, loading, empty, partial, offline, floating nav | first viewport, state honesty, viewport measurement, search remount exposure, final-section clearance |

### Per-card polish checklist

Every leaf review answers:

1. Which semantic renderer family owns it?
2. Which named containment recipe and why?
3. Who owns its outer spacing?
4. Which typography roles, with what Dynamic Type behavior?
5. What exact evidence grounds title, meta, reason, count, and note?
6. What happens for empty, unavailable, stale, and error?
7. Which action owner receives a tap?
8. Is the action passive, navigational, or mutating?
9. If mutating, where are the canonical writer and visible receipt?
10. What is the stable exposure identity and content revision?
11. Which mock, backend-real, and device scenario proves it?

## EF-4 — Backend consolidation

### EF-4A · Split Trips projection contracts from projection logic

**Risk:** contract-sensitive

Extract from `backend/home/trips_stack.py` into stable modules:

```text
trips_stack_models.py       public Pydantic wire models
trips_stack_receipts.py     grounded receipt construction
trips_stack_projection.py   ranking-to-projection mapping and posture
trips_stack.py              compatibility imports/public entry point
```

Preserve OpenAPI component names and public imports. Do not combine this
mechanical move with a wire change.

Exit: tests and exported OpenAPI are byte-equivalent except for intentionally
irrelevant ordering; `trips_stack.py` becomes a small compatibility facade.

### EF-4B · Strangle the Concierge producer monolith

**Risk:** contract-sensitive and privacy-sensitive

Extract one producer family per commit from
`backend/home/concierge_feed/producers.py`:

```text
producers/group.py          group room and invite seat
producers/readiness.py      readiness, agent work, stay compare
producers/lifecycle.py      live, imminent, settlement, return
producers/ambient.py        weather, nearby, local take, starter
producers/saved_memory.py   saved cluster and memory
```

The original assembler remains the single orchestration entry point. Each move
is behavior-preserving and keeps tests beside the extracted family. Group copy
must retain the existing privacy/redaction path; no new free-text composer is
introduced.

Exit: independent card families can be owned by different agents without all
editing one 3,219-line file.

### EF-4C · Split Places orchestration from pure projection

**Risk:** contract-sensitive

Move pure guide/reading/experience/area/saved/cardinality builders from
`backend/places/sections.py` into `section_projection.py`. Keep context,
producer execution, availability, ranking, and the public `build_places_feed`
entry point in `sections.py`.

Exit: producer orchestration tests and pure projection tests are independent;
adding a new grounded card field does not require editing the orchestration
hot file.

## EF-5 — Backend data plumbing

### EF-5A · Grounded Places supporting-copy policy

**Risk:** contract-sensitive

Use the existing `PlacesCard.reason`, `PlacesSection.note`, and `.count` fields
before adding a new composition discriminant.

Work:

- define allowed evidence bases for each current producer;
- populate reason only when it adds a stored, attributable fact rather than
  repeating title/meta or promoting proximity into conviction;
- populate count only from qualified totals;
- populate note only from producer-owned editorial/context facts;
- carry no raw private input or unreviewed generated prose; and
- add producer characterization tests plus mock/real parity fixtures.

Potential typed addition, only if tests prove string-only provenance is
insufficient: a small `reason_basis` enum. Do not add generic metadata.

Keep `saved_unvisited` and conviction unproduced.

### EF-5B · Coherent Trips module side receipts

**Risk:** contract-sensitive

Characterize Now, conditions, and group modules with two trips and mismatched
locality/roster inputs. Then choose one additive availability contract:

- an available module carries coherent trip/locality identity and its receipt;
- a known failed dependency is represented as a bounded unavailable module or
  a content-free `unavailable_modules` entry;
- genuine absence remains distinct from dependency failure; and
- the client never joins ambient weather, live situation, or travelers from a
  different trip into a planned module.

Do not make unavailable modules satisfy required display fields with plausible
placeholder copy.

### EF-5C · Destination and mutation audit

**Risk:** canonical-journey impact

Trace every current card action:

- read-only destination;
- private conversation creation;
- notice acknowledgement;
- proposal resolve;
- add-to-day handoff;
- save toggle; and
- share/invite.

Verify one writer per mutation, durable/visible receipts, retry behavior,
reversal where applicable, and coherent reads afterward. Places remains a
handoff surface for itinerary/proposal/booking changes.

## EF-6 — Contract and parity train

Serialize generated artifacts under one coordinator:

1. land behavior-preserving backend extractions;
2. land any additive module/supporting-copy contract;
3. export backend OpenAPI;
4. regenerate the workspace app projection;
5. regenerate frontend types;
6. update real and mock adapters together;
7. run contract audit, typecheck, and focused screens; and
8. land frontend consumers only after the generated contract commit.

No agent hand-edits `schema.gen.ts` or keeps a temporary handwritten copy of a
Pydantic model.

## EF-7 — Whole-page proof

After component and plumbing batches land:

- run every registered current Trips and Places scenario;
- add the missing combinations: initial, cached refresh, partial producer
  failure, offline cached, error empty, crown rejection, empty projection,
  mismatched module side data, and search unmount/remount;
- capture iOS at narrow and standard widths;
- capture Android;
- test large Dynamic Type;
- run authenticated backend-real canaries; and
- record structured verdicts and evidence receipts.

Mock screenshots establish mock polish. Backend tests establish backend
behavior. Neither is a physical-device acceptance claim.

## 5. Dependency and parallel execution plan

```text
EF-0 baseline/locks
  -> EF-1A/B Trips model and plan
  -> EF-1C Trips render boundaries
  -> EF-2A/C Trips styles and crown
  -> TR-P1..P4 polish

EF-0 baseline/locks
  -> EF-1D Places workspace/feed
  -> EF-2B Places style ownership
  -> PL-P1..P6 polish

EF-0 inventory
  -> EF-4A/B/C backend extractions
  -> EF-5A/B/C data plumbing
  -> EF-6 schema train
  -> frontend parity consumers

all lanes -> EF-7 whole-page proof
```

### Parallel waves

| Wave | Agent lane A | Agent lane B | Agent lane C | Coordinator |
|---|---|---|---|---|
| 0 | QA runner lock/tests | Source-derived section/card ledger | Backend characterization tests | Base/status checks and hot-file locks |
| 1 | EF-1A/B Trips model/plan | EF-1D Places workspace/feed | EF-4C Places backend split | Review roots; preserve current output |
| 2 | EF-1C/2A Trips render/styles | EF-2B Places family styles | EF-4A Trips projection split | Integrate; run local budgets |
| 3 | EF-2C Crown decomposition | Places PL-P1/P2 polish | EF-4B producer extraction | Privacy/action review |
| 4 | Trips TR-P1/P2 polish | Places PL-P3/P4/P5 polish | EF-5A supporting-copy producers | Focused mock/backend tests |
| 5 | Trips TR-P3/P4 polish | Places PL-P6 state/chrome | EF-5B/C module/action plumbing | EF-6 schema train |
| 6 | Trips device scenarios | Places device scenarios | Backend-real canaries | EF-7 verdicts and evidence receipts |

No two agents edit the same root, style namespace, generated artifact, or
backend orchestration file in one wave.

## 6. Commit strategy

Each work package is one or more small, reviewable commits:

1. characterization/regression tests;
2. behavior-preserving extraction;
3. visual or contract change;
4. fixtures and evidence tooling; and
5. evidence receipt/doc update.

Backend contract commits land before workspace snapshots; workspace snapshots
land before frontend consumers. Files are staged explicitly. Mechanical moves
do not share a commit with behavioral changes.

## 7. Validation gates

### Frontend static and focused

```bash
npx tsc --noEmit
npx eslint <touched-files>
npx jest __tests__/utils/tripsHomeSectionPlan.test.ts \
  __tests__/utils/tripsHomeSectionRenderModel.test.ts \
  __tests__/utils/placesPresentationModel.test.ts --runInBand
npm run spacing-budget
npm run typography-budget
npm run typography-roman-only
npm run containment-budget
```

The global size gate has unrelated existing failures. Every home-surface package
must nevertheless prove that touched home-surface files/functions do not grow,
and the consolidation packages must reduce their declared local counts.

### Backend static and focused

```bash
ruff check backend/home backend/places tests
ruff format --check backend/home backend/places tests
PYTHONPATH=. pytest tests/home tests/places -q
```

Use the repository virtual environment. Add real exception, cancellation,
privacy, destination, and identity cases rather than only happy-path fixtures.

### Contract

```bash
python3 scripts/api_contract_audit.py \
  --openapi docs/openapi.json \
  --policy docs/governance/api-operation-policy.json \
  --app-root /Users/feihuyan/home-surfaces-app-next
python3 scripts/project_app_openapi.py \
  --openapi docs/openapi.json \
  --output docs/openapi.app.json \
  --app-root /Users/feihuyan/home-surfaces-app-next \
  --check
```

### Visual and device

```bash
HOME_SURFACES_CANON_DIR=/Users/feihuyan/Downloads/vesper-home-surfaces \
  npm run qa:design:check -- trips-home
HOME_SURFACES_CANON_DIR=/Users/feihuyan/Downloads/vesper-home-surfaces \
  npm run qa:design:check -- places-workspace
npm run qa:surface -- trips-home --after
npm run qa:surface -- places-workspace --after
```

Use the structured verdict protocol. A dry run proves only the harness path.

## 8. Engineering-foundation exit gate

The foundation is ready for new adopted family work when:

- the current branches are integrated and reproducible;
- QA runner contention is prevented;
- Trips body uses a bounded screen model and plan-owned section decisions;
- Places Workspace/feed responsibilities are separated;
- Trips and Places styles are family-owned;
- the Trips Home containment contribution is below its current baseline;
- crown receipts are independently testable without action drift;
- Trips/Places backend hot files have extraction seams;
- Places reason/note/count production is grounded;
- Trips side receipts cannot cross trip/locality identity;
- generated mock/real contracts agree;
- every current section has static, fixture, backend-real, and device evidence
  recorded at the layer actually achieved; and
- no new design family, fake signal, private-to-group copy path, or parallel
  mutation writer was introduced during consolidation.

Only after this gate should the canonical execution plan schedule a new
unresolved composition family.
