---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-09
expires: 2026-09-08
why_new: Records the post-pivot source and design audit that the home-surfaces build roadmap depends on.
---

# Places and Trips Home Surfaces — Post-Pivot Audit

**Date:** 2026-08-09  
**Status:** Triple-checked static/source audit; no post-pivot device certification  
**Scope:** Places root and Trips root, including section composition, card families, full-stack production, reachability, state, rendering, telemetry, architecture, and visual direction

**Verification revision:** 2026-08-09, second pass. The canonical HTML was served directly from Downloads and visually inspected; current frontend/backend code and focused tests were rechecked against it.

**Execution roadmap:** [`home-surfaces-engineering-roadmap-2026-08-09.md`](./home-surfaces-engineering-roadmap-2026-08-09.md)

## 1. Executive conclusion

The product and design pivot is materially ahead of the implementation.

The earlier Build Manifest makes the surfaces appear more complete because it mainly counts existing reasons, routes, component shells, and renderable data paths. The two canonical Page boards count a different—and more demanding—thing: distinct registers, arrangements, compositions, and whole-page states.

A renderer being importable does not mean the designed composition is:

1. produced by backend data;
2. reachable through the real projection;
3. wired to an honest destination or mutation;
4. faithful to the canonical visual treatment;
5. verified using backend-real data; or
6. observed on a device.

At the Page-board level, most of the new work is not implemented.

| Surface | Canonical inventory | Explicitly as-built | Proposed/new |
|---|---:|---:|---:|
| Trips | 56 frames across 11 groups | 9 | 31 |
| Places | 42 frames across 7 groups | 7 | 34 |

Frames include variants and compositional studies, so they should not be converted directly into engineering tickets. The counts nevertheless establish the central conclusion: the new boards are not descriptions of the current product.

The second pass strengthened that conclusion and found additional debt:

- the new Places Group A register system has **no shipping lead**; the existing generic candidate row is reusable anatomy, not an implemented register composition;
- Trips mounts four D2 sections inside unconditional large-margin wrappers, so a child that returns `null` can still leave phantom vertical space;
- the Trips countdown component cannot render the canonical day pips because the row projection carries no itinerary-day receipt;
- Places executes a redundant saved-count query and then overwrites one of the two results;
- design-governance tooling and operating contracts still point to older `vesper 378/401/405` authorities and in-repo screenshots;
- the current size, containment, spacing, and design-evidence guardrails are already failing even before the new compositions are added.

## 2. Canonical design authority

The design authority for all work following this audit is the external bundle at:

- `/Users/feihuyan/Downloads/vesper-home-surfaces`
- `HANDOFF.md`
- `project/Canon - Home Surfaces.dc.html`
- `project/Places - The Page.dc.html`
- `project/Trips - The Page.dc.html`
- the corresponding `As Built` files where the canonical bundle uses them to document current state

Design references and screenshots stored inside `travel-app` are historical implementation evidence only. They must not:

- become the target for new work;
- override the Downloads boards;
- be copied forward as the canonical design;
- be used to claim fidelity to the August pivot.

Implementation fixtures may be stored in the codebase, but they should be derived application states, not copies of the canonical design files.

The handoff's source-authority rule remains important: when a visual board and current code disagree about what is presently built, source code is the implementation fact. The external Page boards remain the design target.

That distinction is necessary even inside the canonical bundle. For example, some Trips proposal captions still say a D2 kind is `INVISIBLE`, while the same Page file's final inventory says it `ships (D2)` and current source contains the component. The board is authoritative for design intent, grouping, and adopted visual direction—not a substitute for inspecting source when reporting current implementation status.

### 2.1 Audited source fingerprints

These hashes identify the exact external files used in this audit without copying them into the repository:

| Source | SHA-256 |
|---|---|
| `HANDOFF.md` | `95f473c7612b196870555953ec245cbed6446f4715bc30e847f37de245f8274c` |
| `Places - The Page.dc.html` | `150ddea633181d8a4633a7722db438de3ff77d7c0bc6b2287f2773cf1dc0ad3c` |
| `Trips - The Page.dc.html` | `2ed150f782098f89ad3da070246fa305fc691518ca912edead5d235a3676e746` |
| `Build Manifest - Both Surfaces.dc.html` | `a0baaab269b2cf1ddb240bc8562cd15283062baaa06b1260af6d087dce8edcc4` |

Code revisions inspected:

- workspace: `df02388f99ab87be78e9875df15ae5376cd8e878`
- frontend: `34707ce28822ba81b04370bb6e2c7dd7110dd427`
- backend: `c19c2b2d251126fe06db1f4a7826f8a6c6fdc2a9`

The backend worktree also contained unrelated uncommitted changes. During the second pass, a concurrent session added an in-flight `editorial_evidence_refs` migration/model and dossier-detail provenance read. That work is not part of the commit hash, is not projected into the Places root feed, and is not counted as implemented or reachable here.

### 2.2 Current design-governance drift

The repository does not yet encode the user's new authority decision:

| Location | Current stale assumption |
|---|---|
| `travel-app/Makefile` | Defaults `DESIGN_CANON_DIR` to `/Users/feihuyan/Downloads/vesper 378/project` |
| `travel-app/scripts/polish-qa/surfaces.mjs` | Treats the old Trips Stack Model and checked-in screenshots as the Trips canon |
| `travel-app/docs/surfaces/trips-home/contract.md` | Names the July `vesper 401` Stack Model as composition authority |
| `travel-app/docs/surfaces/places-workspace/contract.md` | Still specifies at most four sections and an italic thesis role |
| `travel-agent/backend/core/models/places_sections.py` | Header comment points to a `vesper 405` design source |
| `travel-app/constants/typography.ts` and Trips root comments | Still describe the Stack Model as design canon |

Do not solve this by copying the Downloads bundle into `travel-app`. Introduce one lightweight source record for these two surfaces containing the external bundle name/date, file hashes, superseded authorities, and status vocabulary. Runtime code should cite stable semantic rules or the local implementation contract—not a personal filesystem path. Local audit commands may accept the Downloads path as an explicit input; CI should not depend on it.

The bundle itself also contains implementation-status statements that current source has overtaken:

- `PlacesSection.note` and `.count` are now set by some producers despite the handoff saying none set them.
- Trips section-impression vocabulary and hooks now exist, but their visibility semantics are incorrect.
- D2 components exist even where an earlier caption in the Page board still calls the corresponding kind invisible.
- `TripDayMapCard` exists, but its release gate is not enabled by any declared build profile.

These are documentation corrections, not reasons to reject the new design direction.

## 3. Evidence and status vocabulary

Every section or card should be scored using the following independent fields.

| Level | Meaning |
|---|---|
| D — Designed | Present in the canonical Page board |
| C — Component | A component or render branch exists |
| P — Produced | Backend or local producer emits the required grounded payload |
| R — Reachable | The real API projection can deliver that payload to the component |
| A — Actionable | Its navigation, mutation, dismissal, and error lifecycle are wired |
| F — Faithful | A deterministic fixture has been reviewed against the canonical board |
| B — Backend-real | Verified against real projection data rather than a fabricated component fixture |
| V — Device | Observed and accepted on a supported device/platform |

Avoid a single `implemented` boolean. In particular:

- `C` without `P/R` is a dark renderer.
- `P` without `R` is dormant substrate.
- `R` without `A` is a visible but incomplete experience.
- `F` without `V` is not device-certified.
- Green backend or component tests do not establish visual or device fidelity.

No new August 9 Page composition currently has post-pivot device certification.

### 3.1 Current data flow at a glance

Trips today:

```text
Concierge Home producers
  → ranked ConciergeHomeFeed
  → project_trips_home_stack
  → crown + rows[:2]
  → generated OpenAPI projection
  → root selectors + legacy trip/situation/weather/reading side data
  → authored JSX order
  → typed navigation or canonical domain surface
```

The principal defect sits between projection and composition: specialized modules are rediscovered from the already-truncated generic rows, then joined to side data independently inside the root.

Places today:

```text
context + posture
  → independent evidence producers
  → optional section candidates
  → cross-surface fact deferral
  → spine/floor ranking + posture target
  → generated PlacesFeed
  → Workspace request/search state
  → treatment + card-kind dispatch
  → typed navigation or canonical domain surface
```

The principal Places defect is expressiveness: `reason × treatment × kind` describes why a section exists, its broad cardinality, and its payload identity, but not the new register or arrangement the canonical design requires.

## 4. Shared visual direction

### 4.1 Containment is semantic

The core rule is that an edge is a claim:

> A card marks something the user can complete here. A row takes the user somewhere else.

The shared material ladder should mean:

| Step | Material | Intended claim |
|---|---|---|
| 0 | Uncarded section/row | Ordinary record or navigation |
| 2 | Paper banded | Top and bottom hairlines; grouped editorial material |
| 3 | Paper outline | Bounded object without fill |
| 4 | Quiet paper | Warm fill, hairline, minimal lift |
| 4− | Flat paper object | Same warm fill and hair-thin border, but no lift; currently used by Companion |
| 5 | Crown | The single raised lead object on the page |

Nothing should bleed outside the page gutters. Negative-margin or full-bleed explorations are not shipping directions.

The inline consequence banner's transparent gold left rule is a marginal editorial mark, not another rung on the enclosure ladder. Do not force every set-apart treatment into `CardSurface` merely to make the system numerically complete.

The existing `travel-app/constants/cardSurface.ts` foundation is broadly compatible with this system. The main risk is using containment for visual variety rather than meaning.

### 4.2 Typography

The font families are coherent and should remain:

- EB Garamond for Vesper voice and editorial prose;
- system sans for UI, card titles, facts, labels, and actions;
- JetBrains Mono for dates, stamps, and compact metadata.

The audit does not recommend changing the families. It does recommend fixing role drift:

- `MemoryFeedCard` reuses a 13px italic itinerary role, below the declared 17px italic floor.
- A Trips degraded-table caption uses 13.5px serif, below the declared 15px Roman-serif floor.
- Board mono uses a lighter weight than the ordinary app token, making application stamps potentially heavier than the canonical canvas.
- Highly tracked 8–9px mono labels require dynamic-type and device testing; they can quickly become decorative noise.
- System sans will differ across iOS and Android, so both platforms need visual review.

Serif should not leak into ordinary object titles merely because the product is editorial. In the new direction, card titles are normally sans; serif is reserved for voice, prose, and genuinely editorial passages.

## 5. Places — section and card audit

### 5.1 Group A: one place, multiple registers

| Composition | Current status | Engineering assessment |
|---|---|---|
| Invariant register anatomy | Substrate only | The ordinary uncarded candidate row provides reusable plate/title/fact/action anatomy, but Group A itself has no shipping lead or register selector. It must not be counted as an implemented Group A composition. |
| Recommendation | C only | The conviction renderer exists, but there is deliberately no honest producer. Proximity, a user save, or itinerary fit is not sufficient evidence for an editorial recommendation. |
| Verdict | D only | No typed Order/Skip/Go payload, producer, or root renderer exists. Detail-page substrate does not make this a feed composition. |
| Apparatus/citations | D only at the root; in-flight substrate | The committed feed contract has no per-claim source model. A concurrent uncommitted backend change is adding editorial evidence refs to dossier detail, but it has no Places-root projection, producer, or renderer and is not yet counted as available. |
| Change | P/R as notice only | `changed` currently produces a scalar notice such as a permanent closure. It does not implement the canonical Then/Now register. |
| Caveat | D only | No discriminated caveat payload or producer. |
| Log/history | D only | Encounter/relationship substrate exists, but no root history-log contract or composition exists. |

The board's statement that some registers are "legal today" means the containment is semantically permitted, not that implementation exists.

Four descriptive registers are legal with the current uncarded `single` treatment, but each still needs a grounded content selector and a renderer. Apparatus additionally lacks per-claim source data, while recommendation lacks the required non-proximity confidence signal.

`PlacesCard.reason` is present in the contract but no producer populates it. That is a material plumbing gap, but the six registers should not all be compressed into one free-text `reason` field. Verdict, apparatus, change, caveat, and log require distinct evidence structures.

### 5.2 Group B: several places

| Composition | Current status | Engineering assessment |
|---|---|---|
| Candidate rows | C/P/R/A | Strongest ordinary list family. |
| Lead + siblings | Partial | Backend emits `lead` in at least one path; frontend explicitly gives it no visible effect. |
| Two side by side | Partial | The editorial angle fork exists. A general place comparison/pair arrangement does not. |
| Set behind a door | C/P/R/A | Count-door navigation exists, but the proposed quiet-panel grouping is not implemented. |
| Physical stack | D only | Totals exist in some projections; stack composition/material does not. |
| Experience rail | C/P/R/A | Real, with responsive stacking at higher font scale. |
| Ticket stub | Substrate only | Time, availability, duration, and price data can exist; no stub renderer/composition. |
| Editor's note | C/P/R | Current source now emits notes/counts for some producers. The handoff's contrary statement is stale. |

### 5.3 Group C: composed plan

| Composition | Current status | Engineering assessment |
|---|---|---|
| Root map fragment | Selector only | `select_places_area_story` exists and is tested, but has no feed API or frontend consumer. |
| Numbered walk | D only | Generic mapping infrastructure is not a Places-root composition. |
| Stretch sequence | D only | No typed section or renderer. |
| Day/trip cross-reference | Assigned elsewhere | Canonical direction places mapped day/trip ownership primarily on Trips. |

### 5.4 Group D: reading

| Composition | Current status | Engineering assessment |
|---|---|---|
| Editorial cover | C/P/R/A | Real and adaptable across city, area, and angle content. |
| Existing angle fork | C/P/R/A | Real, including responsive stacked degradation. |
| New mirrored spine | D only | No matching contract or component. The old stacked fork is not the new adopted arrangement. |
| Lens switcher | Substrate only | `travel_lens` exists in the domain but is not projected into `PlacesReadingItem`. |
| Deck preview | Partial | Generic preview/deck exists. |
| Quote/extract registers | D only | No distinct structured payloads. |
| Overlay lens | D only | Geometry concepts exist elsewhere, but no root overlay/scrim contract or renderer. |

The word `lens` currently risks referring to both editorial reading semantics and an overlay behavior. These should be renamed before implementation if they remain separate concepts.

### 5.5 Group E: memory

| Composition | Current status | Engineering assessment |
|---|---|---|
| Anniversary memory | C/P/R/A | Routes to the relevant artifact or trip. |
| Postcard memory | D only | Related visual precedent elsewhere does not make it implemented here. |
| Shelf/postcard row | D only | No root producer or renderer. |
| Go back | Partial | A destination can exist, but the explicit return composition and selection logic do not. |

### 5.6 Group F: people

| Composition | Current status | Engineering assessment |
|---|---|---|
| Friend strip | C/P/R | Privacy-gated to legitimate trip relationships. It is passive because no honest target exists. |
| Co-sign | D only | Existing payload is one person to several places; the design needs several people to one place. This requires a new aggregate read model. |
| Again? | D only | Requires a trustworthy recurrence/mutuality signal. |
| Trip marker | Partial | `in_trip` and `loved` can render as generic evidence, but no dedicated marker treatment is implemented across producers. |

### 5.7 Group G: personal record

| Composition | Current status | Engineering assessment |
|---|---|---|
| Belonging ladder | D only | Individual encounter counts exist; no grouped ladder or trustworthy full visit history. |
| Tally | Substrate only | `saved_total` exists; visit and return totals do not. |
| Rhythm | D only | No computation or producer. |
| The Rest | D only | This should be a feed-level state, not a fabricated empty section. |

### 5.8 Places full-stack production

The real feed currently covers:

- `gap` → place choice → typed itinerary-day handoff;
- `expiry` → notice → booking session;
- `group_waiting` → notice → proposal;
- `nearby_set` → place choice, quiet posture only;
- `neighbourhood` → area cards, note/count, and count door;
- `anniversary` → memory;
- `unfinished_guide` / `guide` → reading cards and fork/door behavior;
- `friend_activity` → passive friend strip;
- `changed` → closure/change notice and clear action;
- `harvest` → private trip-debrief prompt;
- `starter` → city choice, starter posture only;
- `experiences` → experience rail/row;
- `saved` → place rows and door.

There are 15 declared reasons and 14 producers. `saved_unvisited` is declared and ranked but not produced.

### 5.9 Places defects and contradictions

1. **"No ceiling" is not the implemented behavior.** Non-spine floor sections are sliced to posture targets of 4–8. Only the urgent spine can exceed the target.
2. **The urgent mast can make a false containment claim.** Copy says the raised card is the next useful decision even though conviction has no producer and urgent objects are generally notices or prompts.
3. **Surface ownership is unresolved.** The Page board moves gap, expiry, group waiting, and debrief pressure toward Trips; the current Places feed still emits them.
4. **Producer failure is not modeled separately from empty evidence.** Independent producers can fail the whole request instead of reporting `available`, `empty`, or `unavailable` under a time budget.
5. **The old `/api/places` projection still has frontend artifacts but is not the current root path.** The root uses `/api/places/feed`; the older client projection is architecture debt.
6. **Saved counts are loaded twice.** `_load_saved_items` already returns the scoped total while `build_places_feed` concurrently calls `count_saved_venues` again; the latter result is then overwritten when the tuple is unpacked.
7. **Independent producers are partly serialized.** Gap, friends, urgency, returns, reading, and nearby are awaited sequentially after the first gather. Latency is additive and any uncaught producer error can collapse the feed instead of producing an honest partial result.
8. **The model header names an obsolete design source.** `places_sections.py` still points to a `vesper 405` export, which invites future work to follow the wrong design authority.

## 6. Trips — section and card audit

### 6.1 Group A: crown

| Composition | Current status | Engineering assessment |
|---|---|---|
| Crown shell | C/P/R/A | Strongest section family. |
| Call, diff, candidates, checklist, ledger, spine, people, conditions, waveform, stamp | C/P/R/A | Receipt variants dispatch structurally and have legitimate data paths. |
| Shape | C/P/R/A | Separate crown branch. |
| Near You | Partial | No dedicated receipt; falls back to generic copy. |

The crown family is the closest existing example of data identity, receipt vocabulary, action, and containment being aligned.

### 6.2 Group B: time

| Composition | Current status | Engineering assessment |
|---|---|---|
| Now | C/P, unreliable R | Has a crown/live-situation fallback, but ordinary selection depends on capped rows. |
| Countdown | C/P, unreliable R and partial F | Null-renders if its row is absent. Its canonical pips require real itinerary days, but the row contract carries no receipt/day data, so the root never supplies them. |
| Temporal strip | D only | No component or producer path. |

### 6.3 Group C: people

| Composition | Current status | Engineering assessment |
|---|---|---|
| Room/group | C/P, unreliable R | Depends on capped rows and loaded traveler data. |
| Trail/Connect | C/P/R/A | Real. |
| Invite seat | Partial and incorrectly routed | Can appear in crown/generic forms; no dedicated section. Frontend discards the `people` destination. |
| Your People | D only | No dedicated composition. |

### 6.4 Group D: evidence and comparison

| Composition | Current status | Engineering assessment |
|---|---|---|
| Conditions | C/P, unreliable R | Queue-cap limited. |
| Work receipt | Crown substrate | Agent-work facts can appear in a crown receipt, not as the proposed standalone composition. |
| Compare foot | Crown/generic substrate | No dedicated comparison resolution composition. |
| Open loops | D only | Missing. |
| Price ladder | D only | Missing; required columns are not projected into the root feed. |
| Comparison table | D only | Missing. |

### 6.5 Group E: below crown

| Composition | Current status | Engineering assessment |
|---|---|---|
| Also in Play | C/P/R/A | Real generic queue treatment. |
| Depth | Partial | Depth exists as metadata, not as the proposed independent composition. |
| Draft shelf | D only | Missing. |

### 6.6 Group F: what counts as a plan

| Composition | Current status | Engineering assessment |
|---|---|---|
| Local Plans | C/P/R, internal | The code and persistence path exist behind internal/dogfood gating. |
| Individual local plan | D only | Missing treatment. |
| Occasions without plans | D only | Missing. |
| Hosting | D only | Also lacks a proper underlying entity. |

### 6.7 Group G: before it starts

| Composition | Current status | Engineering assessment |
|---|---|---|
| Companion | C/P/R/A | Real. |
| This Week | D only | Missing dedicated composition. |
| This Weekend | D only | Missing dedicated composition. |
| Saved Unplaced | D only | Some substrate may appear generically; dedicated composition is missing. |

### 6.8 Group H: return

| Composition | Current status | Engineering assessment |
|---|---|---|
| Return/story | D only | Retrospective data can reach crown or rows, but no dedicated return section. |
| Since You Last Looked | D only | Missing. |

Story destinations currently route back toward Plan rather than a finished story experience. This should remain visibly incomplete until the destination exists; a plausible-looking shell would violate the project's no-stub invariant.

### 6.9 Group I: page voice

| Composition | Current status | Engineering assessment |
|---|---|---|
| Mast | C/R | Real. |
| Standing ask | C/R/A | Real. |
| Voice ask | C/R, internal | Dogfood-gated. |
| Offer | Partial | A live Vesper destination exists; no separate canonical composition. |

### 6.10 Group J: maps

| Composition | Current status | Engineering assessment |
|---|---|---|
| Today Mapped | C/P/R, release-dark | Frontend card, API, and selector exist. No declared EAS profile enables the required editorial-map environment flag. |
| Unroutable leg | Partial substrate | No independent selector/card. |
| Crossing | D only | Missing. |
| Whole trip | D only | Missing. |
| Member stays | D only | Missing. |
| Neighbourhood wash | D only | Missing. |
| Photos | D only | Missing. |
| Reachable now/cluster | Declared only | Vocabulary exists; coherent producer/renderer does not. |

### 6.11 Group K: Trip Feel

| Composition | Current status | Engineering assessment |
|---|---|---|
| Full question | C/R/A | Local selected state and private conversation creation exist. |
| Resumed | D only | Existing conversation is not used to choose this arrangement. |
| Full with contrast seam | D only | The adopted `or` seam is missing. |
| Reduced/already asked | D only | No exposure-aware reduced state. |

Current UI always presents two full tiles and forgets the section's local state on remount. It does not implement the adopted stateful family.

### 6.12 Trips critical defects

#### Four dedicated modules are mined from two rows

The root searches `projection.rows` for four dedicated D2 families: Now, Countdown, Conditions, and Group. The backend slices `rows` to two before returning the projection.

Consequences:

- at most two dedicated families can be available at once;
- if a relevant fact becomes the crown, it may be absent from rows;
- only Now has an independent fallback;
- D2 rows are removed from Also in Play after server truncation;
- a D2 row can consume a queue slot, disappear from the queue, and prevent the third-ranked item from backfilling.

Tests fabricate a three-row projection and therefore do not prove reachability under the real default contract.

#### Invite-seat destination is discarded

The backend and generated schema support:

- `details_section: "bookings"`
- `details_section: "people"`

Invite seat is emitted with `people`. The handwritten frontend shadow type permits only `bookings`, and the router hardcodes Bookings for every trip-details destination.

#### Null children leave phantom rhythm

The root always renders four `alsoInPlayWrap` views for Now, Countdown, Conditions, and Group whenever a crown exists. Each child can independently return `null`, but the wrapper remains and contributes `spacing.xxxl` top margin. On the real capped projection, missing D2 rows are common, so invisible modules can create visible blank gaps.

Section existence must be resolved before layout wrappers are emitted. This is another reason to have a pure section plan rather than letting leaf components decide membership with `return null`.

#### The valid crownless contract can produce a blank hero

`TripsHomeStackProjection` permits `crown=null`. The presentation model classifies crownless state as `empty` only when there are no committed trips; crownless plus existing trips can resolve as `ready` with `fallback="none"`. Backend comments describe that state as unreachable, but the frontend type does not encode the invariant. Either make the projection a discriminated non-empty/empty union or render an explicit degraded state.

#### D2 view models are assembled from inconsistent side channels

The four D2 components do not consume one coherent module payload:

- Now mixes a stack row with live-situation fallback;
- Countdown mixes a row with client trip dates and has no real day receipt;
- Conditions mixes a row with ambient location weather;
- Group mixes a row with the separately loaded trip roster.

This is why component tests can pass while the page cannot prove the full composition. The server should project module identity and grounding; a pure client adapter may join already-authorized cached data, but that join must happen once and return an explicit view model.

#### Map is code-built but release-dark

Today Mapped has a selector, endpoint, hook, and component. It still requires both an internal build and an environment flag that is absent from declared EAS profiles. It should be reported as dark, not shipped.

#### Dreams makes an honesty claim it cannot guarantee

The UI says Vesper learns either way. The client ignores the API's `recorded` result, while the backend legitimately records nothing when learning is disabled globally or by the user. The observation is private (`shared=False`), so this is not a group leak; it is a copy and lifecycle honesty defect. Dismissal is also local-only and can reset on remount.

#### Small but revealing root debt

The Trips root is 1,538 lines and its main screen function is 1,266 lines. It also contains an empty effect keyed by `urgentLeadKey`. The active `TripsHomeStyles.ts` is another 1,483 lines, is imported by Table, Trail, and Views, and contains nine hand-rolled containers identified by the containment audit. These are not merely style issues: obsolete state, dead styles, and no-op lifecycle hooks are difficult to distinguish from real page policy at this scale.

## 7. State and rendering architecture

### 7.1 Current problem

Both pages currently distribute membership and rendering policy across:

- backend posture and ranking;
- request/cache state;
- feature flags;
- ad hoc selectors;
- component-level `return null` branches;
- local interaction state;
- separately maintained telemetry lists.

This makes the page difficult to audit because there is no single artifact answering: "What renders, in what order, why, with which treatment, and in which state?"

### 7.2 Orthogonal state axes

The target model should keep these axes separate:

1. **Resource:** `initial_loading | fresh | refreshing_cached | offline_cached | error_empty`
2. **Travel posture:** `starter | between | quiet | planning | ready | urgent | live | returned`
3. **Local mode:** `browse | search | selection`
4. **Familiarity:** `new | shown | engaged | resumed`
5. **Capability:** `production | dogfood | dark | unavailable`
6. **Producer state:** `available | empty | unavailable`

`empty`, `failed`, and `dark` are different truths and must not collapse into the same blank UI.

### 7.3 Trips target

Trips should remain an authored surface with named slots. Introduce a pure `TripsHomeSectionPlan` that consumes the projection, supporting data, feature availability, familiarity, and request state and emits ordered entries such as:

```ts
type TripsHomeSectionPlanEntry = {
  id: string;
  family: TripsSectionFamily;
  containment: Containment;
  emphasis: Emphasis;
  grounding: GroundingReceipt;
  action: TripsHomeDestination | null;
  exposureKey: string;
  renderState: "ready" | "empty" | "unavailable" | "dark";
};
```

The root should render this plan. Telemetry should read the same plan.

Keep this plan deliberately small. It is not a remote-layout engine and the server must not send React component names, spacing values, or arbitrary visual configuration. The plan should select from a closed TypeScript union of known semantic modules.

The backend projection should separate:

- `crown`;
- a deliberately capped generic `queue`;
- independently addressable typed `modules` or `satellites`;
- per-module availability.

A semantic module must be selected before the generic queue is capped.

Prefer a typed `modules` collection over one optional field per visual card. Each module should carry semantic identity and grounded data, while the client section plan owns whether it appears above/below the crown and which native component renders it. The server should not own Trips spacing or page order.

### 7.4 Places target

Places should remain a server-produced feed. Do not force it into the authored Trips slot model.

Replace the broad optional-payload object with either:

- a true discriminated content union; or
- explicit orthogonal fields for semantic treatment and composition family/arrangement.

The lower-risk migration is additive rather than a big-bang contract rewrite:

1. add an optional, typed section composition descriptor for newly adopted arrangements;
2. add a discriminated register payload only for the new one-place family;
3. keep existing validated kind payloads working unchanged;
4. migrate old families only when a real design requirement needs it;
5. remove wide optional legacy slots after all producers and generated clients have moved.

Do not add a generic `Record<string, unknown>` metadata bag. It would make the API easier to extend briefly and much harder to reason about permanently.

Split `PlacesSectionFeed.tsx` into:

- a small exhaustive feed dispatcher;
- a renderer registry;
- candidate family;
- editorial/reading family;
- experience family;
- memory family;
- social family;
- notice/prompt family;
- shared section frame and responsive helpers;
- action adapters.

The feed root should only preserve server order, select deterministic responsive degradation, and dispatch.

Do not create a component for every design frame. Model the stable axes and let frames become fixtures or configurations where appropriate.

For Group A specifically, preserve the board's rule that the register is selected by grounded data rather than by whichever producer happened to run. A server-side one-place composer should inspect eligible evidence and emit one discriminated register payload. `reason` continues to answer why the section is present; `register` answers how one place is editorially expressed. They are not the same axis.

### 7.5 Debt-minimizing implementation boundaries

The refactor should reduce decisions, not redistribute the current monolith into many files:

1. **Generated transport types at the edge.** Never duplicate an OpenAPI union in handwritten TypeScript. Convert generated wire models into small view models once.
2. **Pure policy in one place.** Membership, order, containment, and availability are decided in a pure composer/section plan, not in JSX and not again in telemetry.
3. **Closed renderer families.** Use an exhaustive typed registry over stable families. Do not build a plugin system or accept server-provided component names.
4. **Leaf components are presentational.** A leaf should not fetch, rank, decide membership, or silently null-render after its parent allocated rhythm.
5. **Actions remain domain-owned.** Cards carry typed destinations or canonical mutation commands; renderers never invent routes or writers.
6. **One section identity.** Give every emitted section a stable ID plus content revision/fact key. React keys, exposure, dismissal, and QA fixtures should share it.
7. **Availability is data.** `ready`, `empty`, `unavailable`, and `dark` are explicit. Exceptions do not masquerade as empty evidence.
8. **Responsive degradation is deterministic.** The server owns semantics; the client owns a small documented mapping for width and font scale.

This is enough architecture. Avoid a universal card DSL, a server-driven UI schema, per-frame components, or a second design-token layer.

### 7.6 Safe strangler sequence

Do not rewrite either root wholesale. A low-debt migration is:

1. Add failing contract tests for the known defects: two-row/four-module reachability, `details_section="people"`, phantom wrappers, crownless projections, and viewport impressions.
2. Extract pure selectors/composers from the existing roots without changing rendered output.
3. Make the current JSX consume the pure plan; delete duplicated exposure and membership gates.
4. Extract one stable Places family at a time, moving its styles and tests with it. Delete dead styles during extraction rather than copying the 1,483/2,253-line style and renderer surfaces into new files.
5. Add the new discriminated register/arrangement fields through the backend OpenAPI workflow and regenerate frontend types.
6. Implement one adopted composition family at a time behind deterministic fixtures, then add backend-real and device evidence.

Internal producer availability does not automatically need to become API payload. Keep it server-side unless the UI has a product reason to distinguish partial evidence from an ordinary shorter feed. This avoids exposing operational plumbing as product state.

Debt guardrails for every implementation slice:

- no new handwritten transport union;
- no new raw containment recipe;
- no increase to spacing, containment, or serif-floor exception baselines;
- no component decides page membership by `return null` after a parent allocates spacing;
- no separate telemetry membership list;
- no new mutation writer;
- no status claim above the evidence layer actually run;
- net deletion or reduction in the touched monolith whenever practical.

### 7.7 Shared infrastructure, not a shared page engine

Trips and Places should share:

- typography and spacing tokens;
- containment materials;
- action conventions;
- viewport telemetry;
- fixture/gallery infrastructure;
- validation vocabulary.

They should not share one generic page compositor. Trips is authored; Places is produced.

## 8. Telemetry and exposure

Both impression hooks currently start an 800ms timer for every mounted section while the route is focused. A `ScrollView` can mount off-screen children, so this is not evidence that the section entered the viewport.

This can corrupt product behavior:

- Places demotes sections after repeated apparent impressions even when the user may never have seen them.
- Trips records an incomplete, manually duplicated list of section gates.
- Trips ignores the hook's `noteEngaged` callback.
- Places omits engagement handling for friend, notice, and prompt branches.
- Changed content under a reused section reason/id can be treated as already seen.

Create one shared section boundary that owns:

- viewport entry and exit;
- dwell threshold;
- stable content identity;
- section/card/surface identifiers;
- engagement wrapping;
- resets when user or content identity changes.

Rendering and telemetry must consume the same section plan or registry so their gates cannot drift.

## 9. Full-stack and MVP invariants

### 9.1 Privacy

Current audited friend/memory behavior is directionally privacy-safe. The Dreams signal is stored privately. Any future co-sign, group decision, or people-oriented summary must still prove that private constraints cannot reach a group-visible composition.

No new group-visible free text should bypass the canonical group composition/redaction path.

### 9.2 Mutations

The principal Places and Trips actions generally route to typed destinations, review flows, or canonical mutation writers. New cards must not introduce parallel proposal, booking, itinerary, or expense writers.

A proposed composition is incomplete if its mutation does not:

- use the canonical writer;
- produce a ledger event;
- show an honest receipt;
- preserve rejection/original-state visibility;
- remain coherent across every surface that displays the mutation.

### 9.3 No plausible stubs

Built-dark selectors, missing destinations, or absent signals should remain visibly unavailable or unreachable. They should not be represented by synthetic prose that looks like live evidence.

### 9.4 Validation

The validation ladder is:

1. static trace;
2. mock walk;
3. backend canary;
4. live device/dogfood.

This audit is layer 1. Existing tests and historical captures provide evidence for parts of the older grammar, but do not certify the post-pivot surfaces.

### 9.5 Verification results from the second pass

Focused checks run against the inspected revisions:

| Check | Result | What it proves—and does not prove |
|---|---|---|
| Frontend focused Jest | 71/71 passed | Existing component and selector expectations pass. Does not model the real two-row backend projection or parent-wrapper rhythm. |
| Backend focused pytest | 126/126 passed | Current Places/Trips producer and ranking assertions pass. One test named “no ceiling” explicitly asserts nine qualified floor sections become eight, preserving the semantic contradiction. |
| TypeScript typecheck | Passed | Internal types are consistent. It cannot catch the People destination because the handwritten shadow type incorrectly excludes that valid generated value. |
| Size budget | Failed | Trips main function is 1,266 lines versus an 800-line limit. |
| Containment budget | Failed | 166 hand-rolled card containers versus a baseline of 162; nine are in reachable `TripsHomeStyles.ts`. |
| Spacing budget | Failed | 363 raw numeric spacing declarations versus a baseline of 361. |
| Typography guardrails | Passed ratchets | Existing exceptions remain baselined; passing does not make the 13px italic Places memory use semantically correct. |
| Design evidence check | Failed | The generated production typography snapshot is stale and `typography.amount` disagrees with the canonical text variant. |

These results are important because they demonstrate that more component tests alone will not control the pivot's debt. Contract-reachability tests, plan tests, and visual/device evidence are required.

## 10. Page rhythm observations

Rhythm should be addressed after section truth and state planning are stable.

The canonical bundle explicitly leaves this decision open: Places Whole Pages variant A documents the current rhythm; B–H are explorations, not adopted specifications. This audit therefore records defects and structural causes but does not choose a replacement rhythm.

Current risks:

- Trips gives many sections nearly the same large top margin, producing an evenly spaced vertical list rather than an authored sequence.
- Missing D2 children can leave those large margins behind as literal empty space.
- Places repeats label → hairline → rows frequently enough to become mechanical.
- Adding more outlined or quiet-paper containers would create a card tunnel and weaken the crown.
- Repeating small mono eyebrows on every section can make the hierarchy noisy.

Rhythm should be derived from:

- evidence density;
- containment step;
- semantic relationship between adjacent sections;
- whether a section continues or interrupts the current thought;
- posture;
- familiarity/exposure state.

Avoid solving rhythm with local margins inside each card. The section plan should choose spacing relationships between adjacent entries.

## 11. Prioritized remediation

### P0 — correctness and product honesty

1. Replace the old Places/Trips design-authority pointers in the Makefile, QA registry, operating contracts, and code comments with an external-canonical source record for `vesper-home-surfaces`. Do not copy the canonical files into the repository.
2. Separate Trips dedicated modules from the capped two-row generic queue.
3. Preserve generated `details_section` values and route invite-seat to People.
4. Remove phantom D2 wrappers by resolving section existence before rendering layout.
5. Replace mounted-section impressions with viewport-aware telemetry and wire engagement consistently.
6. Make Dreams learning copy conditional on the actual `recorded` result; decide whether dismissal persists.
7. Resolve Places-versus-Trips ownership for gap, expiry, group waiting, and debrief pressure.
8. Decide and document the real Places page-length rule; remove the misleading "no ceiling" claim or the implementation cap.

### P1 — architecture and existing substrate

1. Introduce the pure Trips section plan.
2. Split the Places renderer into an exhaustive registry and stable family modules.
3. Remove handwritten API shadow types in favor of generated contracts or exact adapters.
4. Model producer `available | empty | unavailable`, concurrency, and timeouts for Places.
5. Remove the redundant saved-count read and parallelize independent Places producers under explicit budgets.
6. Project Places reading lens and explicit register/arrangement identity.
7. Make crown-empty versus crown-present a discriminated Trips projection invariant.
8. Wire the dormant area-story selector only if the canonical product direction adopts the root map.
9. Decide whether Today Mapped should remain dark or be enabled in an intentional build profile.

### P2 — first complete post-pivot families

1. Implement Trip Feel as a complete stateful family: full, contrast seam, resumed, and reduced.
2. Implement the legally supportable Places one-place registers using typed evidence payloads.
3. Implement the adopted Places reading spine and lens states.
4. Add dedicated Trips people/seat and evidence/decision compositions where data and destinations already exist.
5. Implement return/since-last-looked only after the story destination is real.

### P3 — new domain truth

These should wait for trustworthy producers or entities:

- Places conviction/recommendation;
- co-sign and Again;
- belonging, tally, and rhythm;
- hosting;
- reachable cluster;
- richer crossing/whole-trip/member map compositions.

## 12. Validation and reference workflow

For each adopted card family or arrangement:

1. Record its D/C/P/R/A/F/B/V status in a machine-readable inventory.
2. Build deterministic in-app fixtures for each meaningful state.
3. Include backend-real projection examples where the producer exists.
4. Exercise 320, 360, and 393-point widths.
5. Exercise normal and approximately 1.35 font scale.
6. Review iOS and Android separately.
7. Compare against the canonical files in `/Users/feihuyan/Downloads/vesper-home-surfaces` without copying those files into the repository.
8. Capture real device evidence before describing the family as device-validated or complete.
9. Keep the external design hash in the audit/status metadata so later reviews can detect that the Downloads source changed, without making CI depend on a personal filesystem path.

## 13. Recommended working inventory

Maintain one row per adopted semantic composition with these columns:

| Field | Purpose |
|---|---|
| Surface/group/name | Stable product identity |
| Adoption state | Adopted, exploratory, relocated, rejected |
| Design source | Canonical Page-board frame/anchor |
| Evidence requirement | Facts required to render honestly |
| Producer | Backend/local producer and availability |
| Contract | Generated payload/discriminant |
| Reachability | Real projection route and feature gate |
| Renderer | Component family and arrangement |
| Action | Destination or canonical mutation path |
| Resource states | Loading, stale, offline, error, empty |
| Familiarity states | New, shown, engaged, resumed |
| Telemetry identity | Impression and engagement key |
| Validation | D/C/P/R/A/F/B/V status |
| Known gaps | Explicit blockers or decisions |

This inventory should replace “almost every section exists” as the shared status language.

The inventory should be small, declarative data—not a generated mirror of every design frame. It records product and validation status; the API schema and source code remain the contract for executable behavior.

## 14. Immediate decision log

Before implementation proceeds, product/design/engineering should explicitly decide:

1. Which Page-board frames are adopted versus exploratory?
2. Which urgent/spine subjects belong to Places and which belong to Trips?
3. Does Places truly have no length ceiling, or a posture-dependent floor budget capped at 4–8?
4. Is the Places root map adopted, and if so, what does it own that Trips mapping does not?
5. Are root experiences illustration-led or evidence-photo-led?
6. Which of the two `lens` concepts keeps that name?
7. Is “The Rest” an adopted feed-level state?
8. Should Trip Feel dismissal/resumption persist across sessions?
9. Is Today Mapped intended for production, dogfood, or continued dark status?
10. What constitutes the real destination for return stories and comparison resolution?

## 15. Source landmarks

### Canonical design

- `/Users/feihuyan/Downloads/vesper-home-surfaces/HANDOFF.md`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Places - The Page.dc.html`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Trips - The Page.dc.html`
- `/Users/feihuyan/Downloads/vesper-home-surfaces/project/Build Manifest - Both Surfaces.dc.html`

### Frontend

- `travel-app/app/(tabs)/trips/index.tsx`
- `travel-app/components/places/PlacesWorkspace.tsx`
- `travel-app/components/places/PlacesSectionFeed.tsx`
- `travel-app/utils/tripsHomeStackModel.ts`
- `travel-app/utils/tripsHomeDestination.ts`
- `travel-app/hooks/useTripsSectionImpressions.ts`
- `travel-app/hooks/usePlacesSectionImpressions.ts`
- `travel-app/constants/cardSurface.ts`
- `travel-app/constants/fonts.ts`
- `travel-app/constants/textVariants.ts`

### Backend

- `travel-agent/backend/home/trips_stack.py`
- `travel-agent/backend/places/sections.py`
- `travel-agent/backend/places/ranking.py`
- `travel-agent/backend/core/models/places_sections.py`
- `travel-agent/backend/core/editorial_map/places.py`
- `travel-agent/backend/core/editorial_map/trips.py`

## 16. Audit boundary

This document records a static, source-level audit. No production code was changed, and no post-pivot device run was performed as part of the audit. Existing tests and historical screenshots were used only to understand prior implementation evidence, never as the canonical visual target.
