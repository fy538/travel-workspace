---
doc_type: working
status: active
owner: founder / entity frontend / Integration / Life
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Turns the source-level comparison with the restored entity design lab into bounded visual-completion and owner-integration packages, distinguishing executable UI work from unadopted product contracts.
supersedes: []
depends_on:
  - entity-system-acceptance-plan-2026-09-05.md
  - object-page-rebuild-implementation-handoff-2026-09-03.md
  - object-page-rebuild/build-brief-2026-09-03.md
  - complete-system-integration-roadmap-2026-09-05.md
  - ../systems/contribution-and-consequence.md
---

# Entity object page: design-completion and integration overhaul

## 1. Outcome and scope

Make the existing venue, site and experience pages faithfully express the
chosen object-page design, using actual authorized inputs. Then connect that
page to the existing Home, Places, Chat, Life and arrangement owners without
creating a competing place history, plan, receipt or social system.

This is a proposed execution plan, not an implementation or activation receipt.
It adds a focused design-completion batch to the existing entity acceptance
program; it does not restart its already-landed correctness packages or replace
the Integration/Life coordination model.

Three separate milestones prevent an ambiguous "done":

| Milestone | Meaning | Does not imply |
| --- | --- | --- |
| M1: designed core | Boards 06/06B represented by a tested native implementation and deterministic fixtures; visual acceptance tracked separately if device testing remains deferred | Production media/content coverage or completed social actions |
| M2: connected page | Approved entry contexts, exact returns and existing-owner actions/readbacks work across real reads | Adoption of loose-intention storage or a generalized arrangement implementation |
| M3: accepted internal experience | Current-build reference comparisons, real-backend journeys, accessibility/privacy evidence and capability-specific rollout packet accepted | Public enablement, paid operations or backfill |

### Scope fences

- No identity, catalog, hours, photos, research, embeddings or opinion backfill.
  No Life population run is part of this entity package either.
- No provider/model calls on base page reads, autonomous research, refresh
  scheduler, location monitoring, provider transaction or production write.
- Keep core, research and people flags independently off by default. Media
  capability must have an explicit policy boundary; do not enable it by proxy.
- Venue, site and experience only. Accommodation, containers/towns and
  person-made spots are a separate expansion decision.
- No generic Add-to-trip ladder; no automatic visit, taste, participation,
  sharing or memory consequence from opening a page.
- Home/Places root composition, Life organization/indexing, Capture custody,
  arrangement commands and relationship grants remain with their owners.
- Planning does not adopt a new schema, API integration, prompt or permission.
  Such deltas get a concrete review packet before implementation.

## 2. Inspected baseline and reusable work

Source inspection on September 7:

| Repository | HEAD | Working-tree condition |
| --- | --- | --- |
| App | `c8d88437f` | Clean; local main ahead of origin/main |
| Backend | `3f7e25da6` | Concurrent Integration changes in root composition, owner reads and value composition; leave untouched |
| Workspace | `dc3fea5` | Concurrent design, strategy and governance edits; leave untouched |

The prior comparison turn ran seven focused app suites: **90 tests passed**.
That is behavioral evidence at the inspected baseline, not a visual verdict.
The reference check found zero registered image comparison pairs. Native
preflight stopped on Metro :8081. These are dated observations, not permanent
blockers or fresh evidence from this planning document.

The September 6 acceptance assignment defers app/device tests for current
engineering. Preserve native acceptance as an open gate and schedule it when
that deferral is lifted; do not start a device session as a planning side effect.

### Execution ledger — 2026-09-07

The first implementation batch is on the dedicated app branch
`codex/entity-object-design-completion` and is intentionally not a public flag
or main-branch merge:

| Commit | Package | Evidence |
| --- | --- | --- |
| `53197236f` | Shell kicker, lighter fact pair, wrapping text verbs, two-column closing facts | 6 focused suites / 87 tests at the slice boundary |
| `6b52bacf1` | Safe source-owned reservation continuation | Projection + page tests; TypeScript clean |
| `ec9c6ae0a` | Object-only 96px location variant and typed body blocks | Citation mapping retained across filtered paragraphs |
| `abc0a0996` | Compact Where row integration | Map policy and location fallback tests |
| `bd5112e5a` | Authorized exact-place line quotes | Withdrawal removes quote and selected sheet |
| `46eadd5d0` | Ephemeral research-arrival/source-count treatment | Queued → ready arrival test |
| `9121c8546` | Unsafe booking URLs suppressed at projection boundary | HTTP(S)-only reservation action test |
| `50190881f` | Detail save origin envelopes for venue/site/experience | Route smoke tests; bounded `surface` + optional `trip_id` only |
| `c03677948` | Reset ephemeral research-arrival state on entity replacement | Prevents an old page’s arrival treatment surviving a reused route |
| `6f0aa5319` | Compact map forwarding coverage | EntityLocationMap policy remains unchanged |
| `3f199d470` | Review fixes: reservation action merge, research arrival correlation/timer, save trip-ID validation, compatibility map restoration and external-link failure feedback | 8 focused suites / 109 tests; TypeScript passed; targeted lint had no errors |

The latest recorded route-level evidence is 8 focused suites / 109 tests plus a clean
TypeScript check. The branch remains internal and feature flags remain off by
default. Native screenshot comparison, design-reference registration, owned
media retrieval, exact Life record destination, arrangement standing and
optional useful/keep-words/reply actions remain gated by the dependencies below;
no backfill has been run.

QA evidence correction: Metro preflight and the Entity Object Page doctor passed
once the local bundler was started. The capture run reached the first Maestro
journey and was stopped after a retry began. The cause of the incomplete capture
was not established; this does not demonstrate an unavailable simulator/device
and does not count as native visual acceptance. The later review's doctor stopped
specifically because Metro was not running on port 8081.

The full app Jest run completed with **1,192 suites / 8,132 tests passing and
17 suites / 21 tests failing**. The failures are outside the entity-page
surface (Life/navigation, chat payloads, card/convention ratchets and mock
fixtures); the entity rebuild, shell, projection, map and venue/site/experience
route suites all passed. Those failures were not reproduced on the pre-change
baseline, so their location alone does not prove they are unrelated regressions.
The focused result above is scoped evidence, not a whole-app green result.

Retain:

- V2 canonical presentation and full `{type, id}` action identity.
- Existing loading/error/not-found shells, capability guards, private sharing
  constraints and Save reconciliation.
- Research request/status correlation, deliberate retry identity, bounded
  polling, foreground/offline controls and artifact-generation refresh.
- Viewer-keyed people reads, fail-closed validity, account eviction, custody
  rechecks and selected-sheet withdrawal behavior.
- `ConversationSeed`, `useBringPhotoToEntity`, public share owner sheet and
  existing owner-confirmed consequence receipts.
- Places result-set identity, `placesMapReturn`, root return tokens and Life
  reading-position/target work. Do not introduce a second return registry.

### Source-to-gap map

| Surface / file | Existing capability | Planned change |
| --- | --- | --- |
| `travel-app/components/places/ObjectPageShell.tsx` | 230-point square-corner plate, warm no-photo chrome, shared title | Kicker before name through an additive slot; isolate any geometry change from compatibility consumers |
| `travel-app/components/places/ObjectPageRebuild.tsx` | Pair, body, sources, people, text verbs, closing facts, map | Split presentation from orchestration; match the chosen composition |
| `travel-app/components/places/objectPageProjection.ts` | Deterministic ranking and persisted body strings | Typed reading segments, provenance-bearing actions, contextual facts and stable arrival |
| Three entity routes | Canonical V2 reads and Save/Ask/Bring | Thin canonical adapters; explicit context and media input |
| `travel-app/data/venues.ts` | Venue-only live exact-photo hook | Keep disabled on base rebuild reads; introduce only an approved explicit media path |
| `travel-app/components/places/StayLocationMap.tsx` | Full-width 128-point rounded stay map | Reuse map internals in an object-only 96-point thumbnail; do not change stay geometry globally |
| `travel-app/components/places/PeopleLineSheet.tsx` | Read-only exact-place note | Inline reading integration first; owner-authorized richer actions later |
| `travel-agent/backend/core/models/entity_presentation.py` | Facts have source mode and timestamps; capabilities have owner/destination | Review only missing precise source/action fields; do not create presentation-v3 reflexively |
| `travel-agent/backend/core/models/entity_envelope.py` | Venue already carries `booking_url`, website and phone | Consume honest existing continuation; do not invent a new booking owner |
| `travel-agent/backend/core/models/entity_situation.py` | Request-only origin, expiring typed route and capabilities | Feed an explicitly requested route into the ranker; never parse prose for duration |

## 3. Design authority and decisions to record

The restored source is
`/Users/feihuyan/Downloads/vesper-entity-object-handoff-lab/project/`.

- **06 / 06B:** chosen core composition, no-photo state, research arrival,
  large-text behavior. Primary implementation target.
- **02 / 04 / 05:** absence, people and candidate-resolution behavior. Reconcile
  against current authority contracts rather than copying historical promises.
- **09–12:** entry contexts, intent, Life and useful edges. Design proposals
  needing the named receiving owners where they introduce new consequences.
- **13:** a September 4 ledger, not current code or deployment evidence.
- **Z1–Z5:** history only.

The current surface contract and contribution rules win on privacy, data,
accessibility and action authority. Record these concrete design adaptations:

| Decision | Recommended treatment | Gate |
| --- | --- | --- |
| "Square" plate | Square corners, full width, chosen 230-point height; not a 1:1 aspect ratio | Baseline agreement |
| Tiny source rows/face markers vs 44-point targets | Keep compact reading visuals; use a clearly accessible Sources control and a sheet with full-size links where independent compact targets cannot fit. No overlapping hit areas or silent target-floor exception | Design/accessibility review in O0 |
| Labels at large text | Preserve hierarchy with reflow; do not disable scaling or lower contrast simply because the board freezes 9-point labels | Current accessibility contract; any exception reviewed explicitly |
| Italic friend quotes | Preserve verbatim words and attribution; use only an approved semantic typography role, otherwise Roman quotation treatment | Design-system owner; no ad hoc italic override |
| Live provider plate | Owned permitted media can be read; provider retrieval requires an explicit gesture under current rules | Media policy/affordance decision; do not restore automatic lookup |
| Town as a door | Link only when an exact supported Places destination exists; otherwise plain locality | Places navigation owner; no new container page implied |
| "Been here" byline | Requires actual eligible occurrence evidence. A note alone means "left a line," not a visit | Existing truth contract |
| Keep with a date | Existing Save works now; optional dates require adoption of the retained-intention proposal | Components/Plan D1, unadopted |
| Tonight / arrangement-first verb | Requires an eligible owner context, actual destination and current capability | Integration + arrangement owner; no ambient-trip heuristic |
| Rich people acts | Viewing a line does not authorize keeping, forwarding, replying or feedback | Relationship/source owner contract |

O0 must produce a short adopted/deferred decision ledger. Do not silently treat
every pixel of a non-canonical board as an override of current contracts.

## 4. Target implementation shape

Keep the architecture small: route adapter → controller → pure view model →
presentational components. This is a decomposition of the existing page, not a
server-driven UI system.

Proposed local modules under `travel-app/components/places/object-page/`:

- `ObjectIdentity`: kicker, name, byline and one bounded relationship/context line.
- `FactPair` and `ClosingFacts`: one fact model, two placements.
- `ObjectBody`: typed paragraphs/runs and resolvable citations.
- `ObjectSources`: compact source presentation and accessible inspection.
- `ObjectVerbs`: wrapping actions with honest availability/pending state.
- `ObjectWhere`: 96-point map thumb, location and provider continuation.
- A media resolver/view, and an inline people detail treatment if approved.

Keep `ObjectPageRebuild` as the existing entry point while extracting modules.
Move research lifecycle into a narrowly scoped controller hook without changing
its semantics. Data access still goes through `data/`; do not duplicate backend
models in TypeScript.

The view model should carry stable IDs, not only paragraph array positions:

- **Reading segment:** kind, text/runs, source references, visibility dependency,
  optional expiry. Kinds distinguish public research, current fact, authored
  person quote, own authored line and governed editorial judgment.
- **Fact:** semantic key, value/unknown state, source mode/ref, observed/expiry
  times, optional owner-bound action. Pair placement is separate from fact truth.
- **Entry context:** origin plus opaque owner/ref/return handles. Resolve
  authorization and current display copy from owners; URL text is not authority.
- **Media:** exact entity, source kind, permitted slot, attribution, expiry and
  display/custody policy using the existing media-envelope family.

These are proposed UI-local concepts. API gaps are separately reviewed additive
contracts, not an instruction to persist these view models.

## 5. Execution packages

### O0 — Freeze references and establish a reproducible baseline

**Work**

1. Register the selected source/version and decisions above. The current HTML
   lacks stable `data-screen-id` capture roots; prepare screen-addressable
   reference wrappers/exports without restyling the supplied board.
2. Keep original hashes and an adaptation log. Store approved references in
   `travel-app/docs/surfaces/entity-object/design-refs/`; do not make QA depend
   on an absolute Downloads path. Keep unrelated external Home/Places canon out.
3. Reuse `docs/working/object-page-rebuild/fixtures.json`, validating it against
   the actual current generated contracts. Fixture facts stay test-only.
4. Register isolated screens for rich owned-photo, provider-photo, no-photo,
   people-open, research arrival and large text. Add venue/site/experience
   examples and a narrow viewport. Start at the chosen 393-point reference.
5. Extend the existing `entity-object` QA surface/flows; no second QA harness.

**Exit:** every target screen maps to an identified reference, fixture and
expected assertion; accepted deviations are explicit. No pixel-pass claim
until actual comparisons are inspected.

### O1 — Complete the core visual anatomy

**Work**

1. Add a kicker slot above the name in the shared shell; preserve old callers
   that currently pass metadata beneath the title. Inventory all shell users.
2. Match object-specific inset/rhythm to the selected reference using named
   tokens. Do not change global page padding to fix this one surface.
3. Use the light two-column pair: remove the unintended central/bottom borders
   and excess cell padding. Preserve source readability and large-text stacking.
4. Render text verbs in a wrapping row with full accessible targets; unavailable
   verbs remain absent or honestly explained, never decorative dead links.
5. Render closing facts in the selected two-column arrangement, stacking at
   large text. Avoid rendering the same semantic fact in pair and closing.
6. Build object-only `WhereRow`: 96-point square-corner thumbnail beside a
   compact location and Directions. Eliminate duplicate WHERE/WHERE IT PUTS YOU
   headings. Preserve `map_surface=none/provider_map/mapbox` policies.
7. Tighten byline geometry and collapse redundant relationship metadata into
   one legible read. Do not remove facts merely to make a screenshot fit.

**Exit:** rich, sparse and long-name fixtures have the intended order and
geometry; no-photo has no empty hero; no generic planning ladder; compatibility
venue/site/experience and accommodation map layouts are unchanged.

### O2 — Complete useful facts and honest external actions

**Work**

1. Normalize status and presentation facts once. Support owned hours shapes,
   closed/unknown/stale values and explicit local-time basis; never derive an
   entity's evening from the phone timezone when the place timezone is unknown.
2. Preserve exact provenance where available. A source-mode label alone is not
   a provider citation. Add a narrow source ref only if the owner can supply it.
3. Feed typed `EntitySituationResponse.route` into distance display after an
   explicit one-shot position request. Keep coordinates memory/request-only;
   reject stale/inaccurate origins; mark degraded routes honestly.
4. Rank planning versus arriving using validated current context. Missing
   values cannot win the pair. No made-up distances, price precision or access.
5. Consume the existing venue `booking_url` when safe and permitted. Attach
   Reserve to the fact/action model rather than rendering "Reserve ahead" as
   if it were an actionable booking control. No URL means no Reserve link.
6. Use faithful reservation copy: false `reservation_required` is not evidence
   that a walk-in table is currently available. For museums, use supported
   admission/access information without restaurant-specific labels.
7. Keep location text at its supported precision; adding an address requires a
   canonical owned field, never reverse-geocoding on open or parsing a photo.
8. Reuse current Integration cache-backed practical-fact reads where applicable;
   request a narrow adapter if missing. Do not build another provider cache.

**Exit:** the same place has deterministic arrival/planning pairs; expiry removes
current claims; Reserve/Directions open only supported destinations; returning
from an external app does not change booking/visit/plan truth.

### O3 — Build the sourced reading body and quiet research arrival

**Work**

1. Replace string-only composition with stable typed segments. Preserve the
   explicit `paragraph_sources` mapping when trimming/filtering paragraphs;
   never infer citation numbers from their display position.
2. Compose persisted public research, permitted deterministic current facts,
   eligible authored lines and an optional governed editorial judgment.
   Omit missing inputs; do not generate connective prose on page open.
3. Keep a source registry shared by inline references and the source inspector.
   Distinguish research, listing, self and other authors. No guessed citation
   for an old persisted Take whose evidence is not actually present.
4. Insert friend text byte-for-byte. Preserve author and line dependencies so
   withdrawal removes exactly that quote, face and citation without residue.
5. Sparse pages may use bounded identity copy from known fields, but may not
   claim "nobody you know has been" when social data is disabled or unavailable.
6. When an explicitly requested brief arrives, update body and sources in place
   and show the small arrival/source-count treatment once for that generation.
   Use ephemeral session presentation state; no new person memory or read receipt.
7. Freeze rank/order during a passive research arrival so identity/byline/pair
   do not jump. A newly learned candidate fact may rank on next open or explicit
   refresh. Expired/revoked truth must still disappear immediately; layout
   stability never justifies keeping unsafe content visible.
8. Preserve the current request-ID, account, entity, foreground, retry and poll
   guards during extraction. Stale/failed/status-unknown remain distinct.

**Exit:** every marker resolves; no private line enters public research/share;
removing one input removes only its contribution; shell→ready does not move
the upper-page anchors; ready, stale, failed and unknown are all evidenced.

### O4 — Connect photography without hidden provider work

**Work**

1. Inventory the existing selected/kept media owner and its exact-entity link,
   current custody, permitted projection and source revision. Bringing a photo
   is not by itself approval to make it the hero or proof of a visit.
2. Add a cheap authenticated read adapter for an eligible already-retained own
   photo if an existing owner supports it. If absent, submit the minimal owner
   read contract; do not create an entity-owned copy of photo storage.
3. Resolve: eligible own photo → explicitly acquired permitted provider photo
   → no plate. A friend's image remains behind her authorized line, never the
   shared/global hero.
4. Propose the smallest clear explicit photo-fetch affordance alongside existing
   photo controls. Keep Bring's current Intake ownership and distinguish the
   two jobs. Do not simply re-enable `useVenueExactPhoto` on mount.
5. Reuse `PlacesResolvedMedia` slot/lineage/attribution rules. Reject wrong-place,
   missing-rights, expired and unavailable media; respect no-store in app caches,
   logs and persistence. Preserve source links and provider-required credits.
6. Generalize beyond venue only if the supported provider/owner contract is
   approved. Sites/experiences may correctly remain no-photo until then.
7. Clear media on account/entity replacement, source release and expiry. A late
   image cannot migrate onto the next page. Do not shift the reading position
   because an unsolicited provider request completed.

**Exit:** owned-photo, explicit-provider-photo, denied/failed/expired/wrong-entity
and no-photo states work on the route, not only in the isolated component.
Opening the route alone makes zero new provider photo requests.

### O5 — Connect one canonical page to five origins

**Work**

1. Extend the existing route/context adapters, preserving root return tokens,
   Places result-set revision, query, selected pin, route family and map state.
   Private note prose and precise viewer coordinates do not enter URL params.
2. Resolve a bounded context line from current owner data. Incoming context may
   change the context line, pair ranking and first verb; it cannot rewrite the
   canonical identity or turn a source claim into current truth.
3. Treat stale/invalid context as an honest ordinary entity page. Do not retain
   stale arrangement standing or another account's context after replacement.
4. Implement origin-specific adapters and tests against the matrix below.
5. For Life, consume an exact eligible relationship-record destination from
   its reader/navigation owner. Do not link "Your history here" to a generic
   corpus page that cannot select this entity's record. If the exact destination
   is unavailable, omit that door and report the narrow receiving gap.
6. Arrangement-first Ask names the current arrangement and uses the existing
   private conversation seed. It does not add an option, choose a venue or
   widen the conversation audience by navigation alone.
7. Preserve the existing candidate-resolution boundary from board 05: resolving
   stays at the initiating surface; known/matched results open their canonical
   ref; an explicitly created owner-private shell stays visibly unverified and
   unshareable. Retryable failure and denied/unsupported outcomes remain at an
   honest origin stop. Reuse `data/entityResolution.ts` and its current callers;
   do not materialize a candidate on passive render or add a new admission kind.

| Origin | Allowed addition | Required return proof |
| --- | --- | --- |
| Home | Current eligible context; Tonight? only with owner-resolved live Occasion and handler | Same composition/anchor, with honest refresh after owner changes |
| Places map/list | Explicit location/result context; no gratuitous origin label | Same result set/revision, query, pin, viewport and sheet detent where supported |
| Chat addressed note | Authorized note context; no pre-opened face sheet or read receipt | Exact conversation and preserved position |
| Life | One relationship read and exact record door | Same lens/filter/query/record anchor; reverse door reads the same canonical entity |
| Arrangement | Owner-confirmed "option/not chosen" standing; contextual question | Exact arrangement, not an arbitrary active trip |

**Exit:** five entry fixtures open the same canonical object; origin changes
alone do not mutate it. Back, deep-link fallback, changed/deleted origin,
account switch and process restoration have defined behavior through existing
navigation owners. No new root or entity family is introduced.

### O6 — Finish owner-bound receipts and useful edges

**Existing-owner work that can proceed**

- Keep remains the Save owner. Add the chosen quiet success/readback treatment
  with exact pending/error/Undo behavior using existing receipt primitives.
  Avoid a duplicate toast plus inline success announcement.
- Directions and Reserve explain the external destination/consequence using
  the smallest approved handoff treatment. Cancellation/failure stays honest;
  no Vesper booking, hold, payment or navigation-execution claim.
- Bring/forward a confirmation through Capture's current source workflow.
  Project a reservation only when a booking/arrangement owner supplies an exact
  eligible confirmation ref, state and revision. An email alone is not a new
  entity-owned reservation. Link to its source/owner.
- Basic face opening retains existing fail-closed grants, date and exact words.
  Adopt the designed inline-under-byline versus modal treatment in O0; preserve
  body position and accessibility focus when opening/closing it.

**Conditional work, not silently included in ordinary UI execution**

| Feature | Prerequisite | Implementation after prerequisite |
| --- | --- | --- |
| Optional No date / Sometime / Saturday | Adopt D1 retained-intention owner and generated command/read contract | Invoke that owner; private readback; releasing the date preserves an independent Save; no auto-Plan or watch |
| Consider for an arrangement | Adopt/implement the arrangement's option command and authority adapter | Exact one-effect preview only when needed; owner readback; option remains distinct from decision/attendance |
| Useful | Relationship owner defines receipt audience, capability and retry semantics | Explicit feedback to the allowed recipient only; no public tally or taste inference |
| Keep her words | Source/relationship owner supplies retention permission, copy/reference semantics and revocation dependency | Distinct command and receipt from Keep place; withdrawal invalidates the permitted derivative |
| Reply / Send onward | Exact conversation/delivery target plus current audience and forwarding authority | Separate acts with attributed preview where material; no assumed forwarding permission from visibility |
| Friend photo in detail | Media custody and permitted slot bound to the current line/grant | Expiring display only; withdrawal removes photo and words together |

**Exit:** every visible act has an actual owner/capability, meaningful error and
authoritative readback. Missing owner commands are omitted, not simulated in
local state. Optional branches can remain dark without blocking core completion.

### O7 — Accessibility, continuity and acceptance

**Automated / isolated checks**

- Pure composer/ranker tests; no-null pair; source matching; no duplicate facts;
  scope/expiry; stable segment IDs and quote withdrawal.
- Component order/style assertions and route-level flag-on/flag-off cases.
- Candidate known/matched/private-shell/retry/denied cases preserve the original
  explicit gesture and return route; resolution does not quietly seed a catalog.
- Canonical alias/cross-kind action identity, real-account isolation, late
  async responses and Save failure/retry/readback.
- Research lifecycle selection retained and expanded for arrival geometry,
  generation changes and status-unknown behavior.
- No provider enrichment, photo lookup, route calculation, model work, queueing
  or new durable personal mutation caused by base page open. Any permitted map
  tile rendering has its own explicit display-policy treatment; it is not
  permission to fetch new operational facts or provider imagery.
- Real-backend cheap-mode tests use an explicitly isolated disposable database
  and test-only sources. Do not run catalog or production fixture seeding.

**Native/reference checks, when device work is resumed**

- iOS and Android; default and large text; narrow viewport; long names; focus,
  screen-reader traversal, accessibility escape, Reduce Motion and contrast.
- Rich, no-photo, sparse/private shell, loading, error, not found, offline,
  research queued→ready/stale/failed/unknown, one/several/no people, selected
  line withdrawal, image failure and supported map-policy cases.
- Pairwise lifecycle coverage rather than a huge Cartesian product: foreground,
  reconnect, account/route replacement, process restart and return restoration.
- Compare matching fixture/source versions at matching viewport/font scale.
  Measure the core header/pair anchor positions before/after research arrival.
  Review real-corpus thin pages separately from deliberately rich fixtures.
- Inspect first viewport and full scroll; do not truncate content to satisfy
  the historical above-fold aspiration. Record an honest native adaptation
  if source length or accessible target sizes change that aspiration.

The people visibility lease remains a separate privacy-owner decision. Existing
maximum-60-second unobserved remote revocation is not instant revocation; richer
body/media rendering must not widen that bound.

**Exit:** record per-capability code, backend, native, design and enablement
status. A deferred device gate stays open. An old screenshot or flag-off page
does not certify the rebuilt current build.

### O8 — Bounded rollout and compatibility retirement

1. Produce an updated release manifest with exact commits, contracts, fixtures,
   references, reviewed screens, data limitations and optional capability gates.
2. Keep renderer acceptance distinct from available content. No backfill is
   required, and a sparse existing catalog is not a failed photo/research job.
3. Prepare a reviewed internal flag-on build only after the relevant acceptance
   gates; do not change public/default flags as a cleanup step.
4. Use approved content-free telemetry for read failures, explicit action
   outcomes, research status and media failure; never log private prose, photos,
   viewer coordinates or provider payloads to establish visual coverage.
5. Preserve rollback to the compatibility renderer until evidence and owner
   approval allow retirement. Remove only proven dead entity-route code, with
   explicit caller inventory; accommodation/shared utilities are not collateral.

**Exit:** a named reviewer can say which capability is safe to expose, for which
build and data scope, and how to disable it independently.

## 6. Dependency order and reviewable commits

O0 → O1 → O2/O3 establishes the designed core. O4 media can follow its owner
decision independently of research. O5 connects owner contexts; O6 contains
independent existing-owner work and decision-gated branches. O7 accumulates
evidence throughout; O8 follows acceptance, never merely code completion.

Proposed commit boundaries (split further when a review becomes too large):

| Commit | Package / content | Dependency |
| --- | --- | --- |
| 01 | Reference inventory, design decisions and fixture/capture mapping | O0 |
| 02 | Typed view model and presentation extraction, no behavior change | 01 |
| 03 | Kicker/name/byline and core spacing | 02 |
| 04 | Pair, wrapping verbs and closing layout | 03 |
| 05 | Object-only map thumbnail and location row | 03 |
| 06 | Fact normalization, stale/unknown behavior and safe Reserve continuation | 04–05 |
| 07 | Explicit situation context → typed route/distance → ranker | 06; Integration adapter agreement |
| 08 | Typed body, source registry and accessible source inspection | 02; O0 source-target decision |
| 09 | Permitted people quotes and atomic citation/face withdrawal | 08; existing people contract |
| 10 | Quiet research arrival and stable layout/lifecycle tests | 08 |
| 11 | Existing-owned media read/projection or approved minimal contract | O4 owner decision |
| 12 | Explicit photo acquisition, provenance and route wiring | 11; media policy decision |
| 13 | Entry-context adapter and existing return-token integration | 07; receiving owners |
| 14 | Exact Life relationship door and reverse entity door | 13; Life exact reader |
| 15 | Existing Save receipt, provider handoff and available confirmation readback | 06/13; relevant owner |
| 16 | Cross-entry/backend regression matrix and evidence receipt | Available packages above |
| 17 | Native reference comparisons, accessibility review and accepted deltas | Device deferral lifted |
| 18 | Capability-specific release packet and approved dead-code cleanup | Required acceptance gates |
| Conditional A | Loose-date Keep | D1 adoption + owner implementation |
| Conditional B | Arrangement option/question/readback | Arrangement owner/capability |
| Conditional C | Rich people feedback/retention/reply/onward/media acts | Each relevant grant/command contract |

Backend model/route commits precede contract export and app adoption. For every
API delta, run workspace `./scripts/sync-types.sh`, review both OpenAPI files
and `travel-app/utils/api/schema.gen.ts`, then fix all induced type breakage.
Do not hand-maintain a second TypeScript backend model. Serialize this shared
generation step with adjacent work.

Suggested execution lanes: descriptive `codex/entity-object-design-completion`
worktree for app changes; a separate narrowly named backend worktree only when
an approved owner delta is necessary. Check branch/status before each package
and commit. Stage explicit filenames; never sweep unrelated working-tree edits.
The proposed commit list is not an instruction to commit this planning turn.

## 7. Validation commands and reporting

Use current repository scripts; verify paths/options when execution resumes.

```bash
# From travel-app, for scoped implementation verification
npx jest --runInBand \
  __tests__/components/places/ObjectPageRebuild.test.tsx \
  __tests__/components/places/objectPageProjection.test.ts \
  __tests__/components/places/ObjectPageShell.test.tsx \
  __tests__/components/places/ObjectPageStateShell.test.tsx \
  __tests__/screens/venue-detail.smoke.test.tsx \
  __tests__/screens/site-detail.smoke.test.tsx \
  __tests__/screens/experience-detail.smoke.test.tsx
npm run typecheck
npm run test:typecheck:contracts
npm run lint
npm run qa:polish:scenarios
npm run qa:design:check -- entity-object
```

Add the existing research/people hook tests and new media/composition/context
suites as their packages change. Select backend tests from
`tests/places/test_entity_presentation_read.py`, `test_entity_situation.py`,
`tests/api/test_entity_people_lines.py`, `test_entity_research_requests.py` and
`test_venue_exact_photo_route.py`, plus exact owner tests for any owner delta.

When design capture/device testing is authorized again:

```bash
# First prepare an approved screen-addressable reference HTML
npm run qa:design:export -- --html="<approved-screen-reference.html>" --surface=entity-object
npm run qa:design:check -- entity-object
node scripts/polish-qa/run-polish-qa.mjs entity-object --doctor
npm run qa:surface -- entity-object --after
```

Follow `docs/surfaces/_agent-verdict-protocol.md` before filling/committing a
verdict. Inspect comparison sheets, expected checks, actual screenshots and
data context. A dry run with zero PNGs remains harness evidence only. Record
whole-repository failures separately from scoped passes; never infer release
green from a selected suite.

Every execution receipt should state: source SHA, owner/contract delta,
fixture/reference version, changed files, test commands/results, capability
flags, uncovered cases, native/design status and next receiving checkpoint.

## 8. Recommended immediate batch

The following was the initial batch recommendation. The ledger records the
subset actually implemented; **section 10 now owns the next execution slice**.
Do not treat every package below as completed by the previous implementation.

Initial recommendation: commits **01–06, 08–10**: references, component extraction, faithful
layout, honest facts/actions, sourced body, people read composition and research
arrival. This gives a coherent core using current sources and synthetic test
fixtures, with no backfill and no dependency on a new Plan/intention owner.

Resolve media and exact-context interfaces alongside that batch through the
existing owners. Then implement commits 07 and 11–16 where those interfaces are
available. Defer only their missing branches, not the entire page. Do not add
intention chips, a new Tonight workflow or rich people actions merely to make
the rich specimen look finished.

## 9. Reference provenance

September 7 source hashes (SHA-256); original Downloads files were not edited:

| Board | Hash |
| --- | --- |
| 06 | `718468d92f0f457afca26f64b8929a71a110af09682974dad17589461d56bd24` |
| 06B | `50329e556c63d89990d2afb79f58fab7dc3df4eeef779b419bafc46aefb2088c` |
| 09 | `f405f14c9aa53a4a6a9a4033e218264c9f2d9c0f618c566e2074742fecd80479` |
| 10 | `03dbcd265d2514e2ce41707586c332363230cf41311121b490f4a22c48215913` |
| 11 | `49f8676437bd941b97ce44161f04f3163662040f8c81a923d7f97dbac6aac02c` |
| 12 | `7ed7c5bd4709f5c36ae16e1d9814b58a8dd9c176bab59aec0a91a924183613c3` |

Related owner plans: [entity acceptance](entity-system-acceptance-plan-2026-09-05.md),
[Integration coordination](complete-system-integration-roadmap-2026-09-05.md),
[Life reader/continuity roadmap](life-complete-system-and-atlas-replacement-roadmap-2026-09-05.md),
[retained-intention proposal](retained-intention-before-plan-decision-proposal-2026-09-06.md),
[entity design integration response](claude-design-integration-2026-09-04/05-entity-objects-response-2026-09-04.md),
and the app [entity surface contract](../../travel-app/docs/surfaces/entity-object/contract.md).

## 10. Next slice — complete the existing place reader

### 10.1 Outcome, baseline and scope

Make three existing entity routes deliver a complete, trustworthy read and one
useful continuation: a restaurant, a museum, and an activity. A person should
understand which place this is, what supports its description, what is known
about visiting, their bounded relationship to it, and what the next tap does.
Rich and sparse versions must both work. This is a bounded continuation of
O0–O3 and the available portions of O4–O7, not a new entity program.

Planning inspection, September 7:

| Repository | Inspected state | Consequence for execution |
| --- | --- | --- |
| App | Clean `codex/entity-object-design-completion`, `3f199d470`; local main `8860a34bd` | Start from the reviewed entity branch. Main contains separately landed root changes; do not assume commit ancestry or duplicate them. |
| Backend | Main `778494b62`; concurrent product-content document edit | Integration owns shared practical reads and their landing. Isolate any agreed entity adapter change. |
| Workspace | Main `789dc45`; concurrent strategy, Life, Integration, governance and design edits | Extend this plan only; do not stage or rewrite the other task's work. |

No product tests or device sessions were run in this planning pass. The 109-test result
above is the previous implementation's evidence. It does not cover every new
case specified below: notably all three routes' origin payload assertions,
late reservation-link failure, account replacement during arrival, and complete
status-before-artifact arrival/readback sequences still need explicit coverage.

**Included:** contract-correct fixtures/references, lifecycle decomposition,
fact freshness, explicit one-shot distance, supported photo display/acquisition,
sourced reading, existing-owner action feedback and return continuity.

**Held outside this slice:** new entity families, catalog/media/research backfill,
provider-cache replacement, root redesign, Life indexing, arrangement commands,
loose-date Keep, Useful/Keep words/Reply, production flags, paid/live verification
and public release. Native acceptance remains deferred under the current
September 6 assignment. Preparing references and native flows can proceed.

### 10.2 Three concrete acceptance stories

| Story | Successful experience | Required negative case |
| --- | --- | --- |
| Restaurant: considering dinner | Canonical name and locality; truthful reservation/price information; source-backed reading; valid Reserve destination; optional explicit walking estimate; Keep and return to the originating list | Unknown reservation requirement, expired open-now claim, unsafe/failed booking URL, no photo, denied location |
| Museum: deciding whether to visit | Same page family with admission/duration/access facts when supported, persisted interpretation and source inspection; Directions or private Ask; no restaurant-specific Table label | Admission/hours absent, long translated name, large text, source missing, no research capability or artifact |
| Activity: understanding an experience | Canonical activity identity and supported duration/type; permitted description/media; Keep, Ask and exact return; experience-specific capability absence stays honest | No fixed coordinates, no photograph, research unavailable for this type, removed origin, account change |

Use the existing mock venue/site/experience routes and deterministic fixture IDs
valid for their real contracts. Design names can be reused as synthetic examples;
their hours, prices, sources and photos are not assertions about the live places.
No existing catalog row is modified to match a specimen.

### 10.3 N0 — Establish a trustworthy specimen and reference baseline

**Files:** workspace `docs/working/object-page-rebuild/fixtures.json` and
`fixture-contract-audit-2026-09-04.md`; app
`docs/surfaces/entity-object/contract.md`, `scripts/polish-qa/surfaces.mjs`,
existing entity flows and a proposed `docs/surfaces/entity-object/design-refs/`.

1. Reconcile boards 06/06B against current generated V2 types and the surface
   contract. Keep the original Downloads hashes; create isolated capture roots
   and an adaptation log without changing the source board's authored design.
2. Keep the historical design JSON identifiable as a design specimen. Its
   `fx-*` identities, `reservation_url`, legacy source-number shape, inferred
   social claims and unsupported entity families must not become runtime
   contract fixtures. Put typed execution fixtures in the app's existing test
   fixture convention and record the correspondence in the audit.
3. Define six primary specimens: rich restaurant, sparse restaurant, museum,
   activity, research arrival, and large text. Use pairwise fault variants
   instead of maintaining a separate full screen for every combination.
4. Specify the intended 393-point/default-text composition and a narrow/large-
   text variant. Record deviations needed for 44-point actions and source
   inspection. Preserve the square-corner 230-point plate and square-corner
   96-point object map target; accommodation and compatibility geometry stay
   independently covered.
5. Register fixture/version/ref/expected-state pairs in the existing QA system.
   A reference manifest with no real pairs is not this package's exit.

**Exit:** all six specimens have valid typed inputs, isolated source references
and explicit expected behavior. This proves reference readiness, not native
visual parity. Museum/activity adaptations absent from boards 06/06B must be
labelled adaptations and reviewed, not attributed to an unprovided reference.

### 10.4 N1 — Extract lifecycle and presentation without losing guards

**Existing files:** `components/places/ObjectPageRebuild.tsx`,
`objectPageProjection.ts`, `data/entities.ts`, `hooks/useInteractionLifetime.ts`,
`hooks/useUnexpiredValue.ts`, `utils/accountSessionLifetime.ts`.

**Proposed local modules:** `components/places/object-page/` for fact, reading,
source, verb and Where components; a narrowly scoped research controller hook.
Keep the existing `ObjectPageRebuild` entry point and data-facade imports.

1. Lock behavior before extraction: explicit receipt/request ID, status ID,
   artifact generation, account, canonical entity and visit lifetime remain
   separate inputs. Do not duplicate backend research types.
2. Move request/poll/arrival orchestration out of the render component. Clear
   ephemeral state on account or entity replacement, including A→B→A; late
   completions must be inert. Timer ownership must survive artifact rerenders.
3. Cover status-before-artifact and artifact-before-status orderings, fast
   completion without an intermediate queued render, failed/unavailable/unknown
   status, polling exhaustion and retry. A fetched ready brief may update the
   reader without falsely announcing a completion for another request/viewer.
4. Introduce stable UI segment IDs and explicit source dependencies. Use the
   original paragraph identity within a brief generation when the contract has
   no block ID; filtering empty paragraphs cannot shift citation ownership.
5. Keep initial fact ordering stable during passive research arrival. Expiry
   and withdrawal still remove unsupported facts or people material immediately.

**Exit:** focused old behavior remains green, lifecycle ordering tests pass,
and the page component delegates orchestration and sections rather than adding
another large block of effects. Extraction is complete only after unused inline
copies are removed.

### 10.5 N2 — Make practical facts current and useful

**App files:** `objectPageProjection.ts`, proposed fact components/controller,
`data/entities.ts`, `hooks/useUnexpiredValue.ts`, route fixture tests.

**Owner seam:** backend `backend/core/models/owner_read.py::PlaceOperationalFact`,
`backend/places/cache.py::get_cached_venue_statuses_sync`,
`backend/places/entity_presentation_read.py`,
`backend/core/models/entity_presentation.py` and `entity_status.py`.

1. Normalize each fact once: semantic key, display value, current-versus-durable
   meaning, source evidence, observation and expiry. Preserve reservation truth
   when attaching Reserve; an external action does not replace the authoritative
   reservation statement or imply available tables.
2. Filter expired or malformed current claims before ranking. Schedule the next
   expiry boundary and re-evaluate on foreground/reconnect. Do not extend truth
   merely because React Query still has the response or the screen stayed open.
3. `EntityPresentationFact` already carries `observed_at` and `expires_at`;
   consume them. The legacy status block has `as_of` but no per-field deadline.
   Its projection timestamp is not an open-now freshness lease. Do not invent
   a client TTL or infer open-now from stored schedule text.
4. Agree a narrow cache-only adapter with Integration to carry current venue
   evidence and field deadlines into the existing presentation. Reuse its
   provider/place identity checks. Never call `linker`, discover providers,
   enqueue refresh or repair the cache from a page read. A cache miss produces
   unknown. Sites/activities remain unknown where no supported supplier exists.
5. Prefer existing fact fields for the adapter. If exact evidence references,
   field identity or deadlines require an additive model field, document that
   delta and use the required OpenAPI → app projection → generated types sync.
   Do not invent presentation-v3 or a second operational-fact store.
6. Unknown place timezone prevents local-evening inference. A current open-now
   observation and a future-visit schedule answer are different facts. Show
   an exact closing time only with supported schedule/timezone evidence.

**Exit:** the same entity is covered with fresh/open, fresh/closed, unknown,
expired, wrong-provider-identity and independently expiring fields. Expiry drops
the current claim while durable description/price/relationship value survives.
If Integration's adapter is unavailable, local expiry behavior can land; mark
current-fact delivery partial until the adapter and receiving tests land.

### 10.6 N3 — Complete explicit distance and media acquisition

These are distinct user gestures with independent pending/error state and
capability gates. Neither is coupled to opening the page or to Keep.

**Distance files:** `utils/locationService.ts::requestLocationFix`,
`utils/entitySituationContext.ts`, `data/entities.ts::useEntitySituation`,
the three routes, proposed object controller and Where/fact components;
backend `backend/places/entity_situation.py` and its tests where needed.

1. Add one deliberate "Check from here" affordance for an eligible coordinate-
   backed destination. Use the shared one-shot service, no location watch:
   `maxAgeMs: 0`, no last-known fallback, bounded timeout and current OS fix.
2. Validate finite coordinates, observation time and usable accuracy. Proposed
   initial origin acceptance: at most 2 minutes old and accuracy ≤100 metres;
   encode and test the same rule at the entity situation boundary before using
   it. The existing backend accepts origins up to 15 minutes old and does not
   reject low precision beyond the broad model limit; that needs reconciliation.
3. Send origin only in the deliberate situation request. Replace the current
   serialized-coordinate query key for this path with an opaque request/session
   handle; keep origin out of routes, persistent query caches and telemetry.
   Disable automatic retry/focus/reconnect refetch for provider-backed origin
   requests. A retry or fresh route calculation follows a new visible tap.
4. Feed validated `situation.route` into the fact model using duration, resolved
   mode, degraded flag and response `valid_until`. Do not parse `summary` for a
   number. The explicit from-here posture may promote distance; a device clock,
   generic active trip or absent route must not masquerade as arrival context.
5. On denial, timeout, missing destination, poor fix or expired result, preserve
   the page and show a bounded explanation/retry. Directions remains a separate
   external continuation where supported by map policy.

**Media files:** `data/venues.ts`, `types/placesMedia.ts`,
`components/places/core/PlacesMedia.tsx`, `ObjectPageShell.tsx`, the three routes;
backend `backend/api/routes/venues.py` and `backend/media/contracts.py`.

1. Keep the compatibility `useVenueExactPhoto` behavior isolated. Add an explicit
   acquisition method through `data/` for the rebuilt venue route; a supported
   "View place photo" tap uses the existing exact-photo endpoint once, with
   no automatic focus/reconnect fetch or hidden paid retry. Return
   loading/available/unavailable/error explicitly where the endpoint supports it.
2. Bind each result to the requesting account/session, visit and canonical
   entity. `claim_scope=exact_place` alone is not a match to this entity. Reuse
   server-verified request-to-provider binding; if a wire identity is missing,
   propose the smallest additive canonical-ref response rather than parsing URLs.
3. Enforce eligible slot, expiry, required credit and cache directive before
   rendering. No-store bytes/URLs stay out of persistence; clear session media
   on leaving, account/entity replacement and expiry. An invalid or late image
   cannot become the next place's hero.
4. Retain Bring photo as the existing Capture gesture. Inventory eligible owned
   media through Source/Life owners first: current artifact-photo reads are
   artifact-addressed, and trip photos have their own audience/block bindings.
   Neither is automatically an authorized exact-entity hero reader.
5. Owned media handoff must specify exact entity, source/photo ID, viewer/audience,
   source revision, display purpose, expiry/revocation and attribution. Implement
   a read adapter only when that owner supports those guarantees. A proposal
   without an owner implementation is a documented gap, not media completion.
6. Sites/activities may remain no-photo in this slice. A future media adapter
   can serve them; do not send site/activity IDs to the venue-only endpoint or
   turn generic imagery into a documentary place photo.

**Exit:** route-level tests prove zero location/provider acquisition on open;
one explicit tap yields one bounded request; failure/expiry/wrong identity is
honest; permitted venue photo works end to end with a fake provider. No-photo
museum/activity specimens meet core acceptance independently of media supply.

### 10.7 N4 — Finish sourced reading and existing-owner actions

**Files:** extracted reading/source/verb components, `PeopleLineSheet.tsx`,
`hooks/useSaveEntity.ts`, `utils/saveEntityAction.ts`, `hooks/useValueMoment.ts`,
`utils/consequenceReceipts.ts`, `utils/placesMapReturn.ts` and the three routes.

1. Resolve inline markers and source inspection from one registry keyed by
   their actual source namespace. Public research citations and private person
   attribution remain distinct. Keep exact authored words and remove each line,
   face and selected detail together when its grant disappears.
2. Provide one accessible Sources entry/inspector with full-size source links;
   do not enlarge tiny inline marker hitboxes into overlapping targets. Return
   focus to the invoking control and preserve reading position after dismissal.
3. Keep reservation statement and Reserve action separately legible; propagate
   safe external-link feedback to both pair and closing placements. Cover
   successful open, failure, entity replacement and late failure after leaving.
4. Keep remains the Save owner. Confirm one pending/success/failure treatment,
   canonical identity, valid optional trip origin, subsequent owner readback and
   explicit removal through the existing save toggle. Do not add duplicate toast
   and inline success announcements.
5. Do not wire Undo to a generic toggle. The current deletion helper is addressed
   by user/type/entity, not immutable save revision; an old receipt could remove
   a newer save. Immediate Undo needs an owner-supported exact save/precondition
   contract. Until then provide the current explicit Remove action and record the
   precise owner gap rather than displaying an inert or unsafe Undo button.
6. Preserve exact Places/root return context and private Ask seed identity.
   Validate invalid/stale origin independently from canonical page loading.
   Consume an exact eligible Life destination only if its owner supplies it;
   omit the door otherwise. Arrangement standing and new social acts remain
   with their owning workstreams.

**Exit:** each of the three stories opens the same canonical object through its
supported origins, takes one supported action, reads back its result and returns
correctly. Withdrawal does not leak into public sharing or leave stale quote UI.

### 10.8 N5 — Verification and review packet

**Behavioral checks:** retain the eight existing page/projection/map/route suites;
add research-controller, situation, media, source inspector and save-owner tests
only where their behavior changes. Assertions must prove outcomes and request
budgets rather than merely checking that mocks received a prop.

| Boundary | Required proof |
| --- | --- |
| Base open | Correct canonical identity; zero location/provider/model acquisition; successful sparse render |
| Fact freshness | Per-field expiry, unknown/malformed input, provider mismatch, foreground expiry; no phone-timezone inference |
| Research | Correlated receipt/status/artifact; both response orderings; fast completion; failed/unknown/retry; account/entity A→B→A; timer cleanup |
| Location | Granted/denied/timeout/inaccurate/stale; typed resolved mode and degraded route; no precision in URL/query key/logs; no automatic refetch |
| Media | Explicit request only; required attribution; wrong place, revoked/expired source, no-store, late result and no-photo fallback |
| Keep and handoff | Valid/invalid/empty trip origin in all three routes; confirmed readback/removal; pair and closing Reserve; current versus late failure |
| Reading/people | Citation ownership survives filtering; inspector focus/escape; current grants; selected and inline withdrawal; no private share leakage |
| Navigation | Origin retained across Keep/Ask/map/source/photo; missing origin fallback; exact canonical type+ID after redirects |

Run targeted Jest, TypeScript, touched-file lint, API-boundary/schema checks and
`git diff --check`. For backend changes run their offline unit/API tests plus an
isolated disposable-database readback test where database behavior matters.
Use fake providers and synthetic test-only data; no production seeding, backfill,
research queue activation or external acquisition is a verification shortcut.
Every model/route delta requires workspace `./scripts/sync-types.sh`, review of
both OpenAPI snapshots and app generated types, and `make api-coverage-check`
when operation consumers change. Shared generated files must be serialized with
Integration's work, never staged as an incidental whole-tree change.

Run existing scenario and design-reference validation. Prepare the current-SHA
flag-on iOS/Android flows, but preserve native execution as deferred. Once resumed,
use the registered `entity-object` pipeline, matched reference/fixture/viewport,
full-scroll comparisons, narrow/default/large text and VoiceOver/TalkBack checks.
A mock screenshot or passing Jest suite does not establish native design parity.

**Deliverable:** update this ledger and the existing surface contract with exact
commits, fixture/reference versions, checks, unresolved owner contracts and
capability status. Separate these outcomes:

- code complete for the core three stories;
- reference-ready with real comparison pairs;
- current-build native/design acceptance pending or accepted;
- optional owned media / provider media / research / people acceptance;
- branch landed and internal/public enablement, each evidenced independently.

### 10.9 Commit sequence and owner handoffs

| Commit | Reviewable change | Dependency |
| --- | --- | --- |
| 1 | N0: typed fixtures, reference mapping and accepted adaptations | Reviewed entity branch baseline |
| 2 | N1: lifecycle tests and controller/section extraction | 1; preserve current route entry points |
| 3 | N2: local fact normalization, deadline observation and honest unknowns | 2 |
| 4 | N2: agreed cache-only practical-fact adapter, schema sync and mobile adoption | Integration contract; may land independently of 5 |
| 5 | N3: explicit origin acquisition, request-only situation adapter and typed distance | 2–3; backend accuracy/freshness alignment |
| 6 | N3: explicit venue-photo acquisition, eligibility and no-store lifecycle | 2; existing media policy; separate additive identity delta if necessary |
| 7 | N4: source inspector, reading/people consistency and action/return closure | 2–3; 5–6 where available |
| 8 | N5: cross-entry regressions, evidence and precise remaining gates | All implemented packages above |

Existing-owned photo display, exact Life door and revision-safe Undo are
separate follow-through commits only after their named owner contracts exist.
They do not block local fact/reading/route work and must not be marked completed
merely because their interfaces were proposed.

The first execution checkpoint is commits 1–3: six valid specimens covering the
three entity stories, a smaller controller, and expiry-correct practical facts.
Prepare the exact current-fact adapter request for Integration alongside that
work as a written contract proposal; do not send messages or start other tasks
without a user request. Content's world-supply
and Places-root design work remain outside this implementation. Provider policy
questions go to that existing supplier work rather than a duplicate research lane.

Planning acceptance means approving this bounded scope. Execution should commit
each coherent unit, preserve concurrent changes, and stop declaring overall
completion until the corresponding code, contract and evidence exits are met.

Planning-document validation: targeted lifecycle governance, all six relative
links and `git diff --check` pass. The workspace-wide link check reports one
pre-existing false positive in the interaction-kernel V2.3 execution report:
inline JavaScript array access followed by a function call is parsed as a
Markdown link. That report and the checker are unchanged by this plan.
