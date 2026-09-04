---
doc_type: working
status: active
owner: founder / product / design / backend / frontend
created: 2026-09-03
last_verified: 2026-09-04
expires: 2026-10-03
why_new: Preserves the execution-shaped object-page design and fixtures while its proposed API and composition contracts receive founder and engineering review.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/working/object-page-rebuild-implementation-handoff-2026-09-03.md
  - docs/working/entity-system-next-program-2026-09-03.md
  - docs/systems/four-root-loop-object-surface.md
---

# Object Page Rebuild — Build Brief (execution-shaped proposal, 2026-09-03)

**Status:** reference implementation brief, not an authorization to change the API or ship a new object-page contract. **For:** a coding agent working in the entity worktrees. **From:** the design handoff `docs/working/object-page-rebuild-implementation-handoff-2026-09-03.md` (rev 4, the *why*) and the Claude Design lab `dd48304b` (board 06 = the page). This brief is the proposed *what and how*. Where this brief and the handoff differ, the difference is an open contract question; neither overrides the accepted entity-system program until a founder gate records the decision.

**Fixtures:** `docs/working/object-page-rebuild/fixtures.json` — every state on the boards, in wire shape, with expected-render assertions. Build against them; do not invent data.

## 0. Scope, branch, boundaries

- **Reference worktrees:** `/Users/feihuyan/travel-workspace/travel-app-entity` (mobile) and `/Users/feihuyan/travel-workspace/travel-agent-entity` (backend), both on `codex/entity-shell-resolution`. Those entity branches are already included in the local `main` integration; any follow-on implementation must branch from the current local `main` after the contract gate. No pushes without the founder.
- **In scope:** one object page component for venue · site · experience · neighbourhood-as-entity · spot; the container page shares chrome and inputs with the map as its plate. The candidate-origin harness from the resolution brief.
- **Out of scope (concurrency fence from the resolution brief §5):** `backend/root_projection/v2/**`, `root_composition.py`, source-contribution / known-to-person producers, owner reads, Home root UI, `PlacesWorkspace.tsx`, Places root feed/arbitration/navigation. Accommodation keeps its own screen.
- **Backfill fence:** the identity-seed language in the handoff is a proposal for a reviewed, bounded source lane; it does not override the accepted entity-system program's no-broad-backfill non-goal.
- **Mock flag:** `.env.example` defaults `EXPO_PUBLIC_USE_MOCK_API=true`, while the current local `.env` is `false`. Every visual check must use real mode or an explicit fixture harness; otherwise you are reviewing the mock.
- **Stub, don't resolve** (behind flags): the identity seed and dedupe; the owner-shell promotion rule; the share contract for owner-private shells; provider photo policy per provider. Each has a TODO owner in §9.

## 1. The deliverable, as acceptance tests (run against `fixtures.json`)

| # | Test | Fixture |
|---|---|---|
| T1 | Renders in this order and nothing else: plate?, kicker, name, byline?, pair, body, sources?, verbs, closing row, where?, end | all |
| T2 | Sparse page ends above 812pt at default text size; no element says "no notes", "be the first", "hours unknown grid" | `cafe_aurora.t0` |
| T3 | Rich page: the pair and the verbs are above 812pt | `hortus.arrival` |
| T4 | Removing one input (e.g. `people_lines: []`) removes exactly its byline face and its cited sentences; nothing else moves | `hortus.arrival` minus each input |
| T5 | A null never occupies the pair; the ranker output matches the table in §6 for the four situations | `hortus.arrival`, `hortus.planning`, `cafe_aurora.t0`, `museu.known` |
| T6 | Plate resolver: kept photo → permitted provider photo with credit → none; never an illustration; friend's photo only in the sheet | `hortus.arrival` (yours), `aurora_bar.matched` (provider), `cafe_aurora.t0` (none) |
| T7 | Every sentence with a marker resolves to a source in the sources list; friends' quotes are byte-equal to `people_lines[].text`; no sentence claims a fact absent from inputs | `hortus.arrival`, `hortus.many` |
| T8 | Opening the page triggers no Take generation and no synchronous research call | all |
| T9 | Arrival: when `research_brief` transitions null → present, only the body, sources and the "just now" line change; plate/name/byline/pair bounding boxes are identical before and after | `cafe_aurora.t0` → `cafe_aurora.t40` |
| T10 | Large text (1.3×): pair and closing row become one column; kickers/source lines keep 9pt; nothing truncates | `hortus.arrival` |
| T11 | Verbs: Keep in the top bar; Ask + Leave for someone as text; Tonight? present iff `viewer.occasion_live`; never an Add-to-trip ladder | `hortus.arrival` vs `hortus.planning` |
| T12 | Face tap opens the sheet under the byline; body stays; sheet shows line verbatim, grant, date, photo if any, USEFUL / KEEP FOR ME / REPLY | `hortus.arrival` |
| T13 | Withdrawn / blocked / outside-grant lines are absent from byline and body with no residue and no count | `hortus.withdrawn`, `hortus.blocked` |
| T14 | Where: address + map thumb honouring `display_policy.map_surface`; Directions opens the provider handoff | `hortus.arrival`, `cafe_aurora.t0` |

## 2. Token map (board size → app variant)

| Element | Board | App variant | Action |
|---|---|---|---|
| Name | sans 600 24/27 −0.6 | `typography.objectTitle` | reuse |
| Kicker (cuisine · town) | mono 700 9 ls 1 | — | **add** `typography.objectKicker`: `fontFamily.mono_bold`, 9, letterSpacing 1, `colors.surface.mute` (9pt labels are allowed on instruments by founder ruling; kickers never scale) |
| Byline label | sans 12.5 mute | `caption` | reuse |
| Pair label | mono 9 | `objectKicker` | reuse new |
| Pair value | sans 600 18/24 −0.3 tabular | — | **add** `typography.pairValue` (sans 600 18/24, `fontVariant: ['tabular-nums']`) |
| Pair source line | mono 9 muteSoft | `objectKicker` + `colors.surface.muteSoft` | reuse new |
| Body | EB Garamond 400 16.5/24 | — | **add** `typography.objectBody` (`fontFamily.serif`, 16.5, 24). Note: `serifBody` is 15/22 and stays for cards |
| Body, friend's quote | serif italic 16.5/24 | `vesperVoiceItalic` face | reuse the italic face; size from `objectBody` |
| Citation marker (web) | mono 8.5 in a 14×min14 chip, radius 4, ink 6% | — | **add** `ObjectMarker` component; text `fontFamily.mono_bold` 8.5 |
| Citation marker (person) | 15px disc, ink; umber for viewer | `avatar` size ladder: nearest = 16 | reuse `people-monogram-colors` rule: viewer = umber, others = ink |
| Sources list | mono 9 muteSoft, rows | `objectKicker` | reuse new |
| Verbs | sans 600 13, umber; secondary mute | `itineraryReviewAction` (12.5/16) | **reuse**, colour `colors.surface.warmUmber`/`mute` |
| Closing row label / value | mono 9 / sans 13 | `objectKicker` / `bodySmReading` | reuse |
| Address, Directions | sans 12.5 / sans 600 12.5 umber | `caption` / `itineraryReviewAction` | reuse |
| Rhythm | page padding 16; section gap 8; paragraph gap 12; hairline `withAlpha(ink,0.10)` | `layout.pagePadding`, `spacing.md/lg` | reuse |
| Plate | 230pt, square corners | `OBJECT_HERO_HEIGHT` | **change** bottom radius 28 → 0 in `ObjectPageShell` |
| Large text | body 21/30; name 30/34; pair 22/28 | `useFontScale` | scale `objectBody`, `objectTitle`, `pairValue` only; clamp kickers |

## 3. Components (props are the contract)

- `ObjectPage({ presentation, research, people, viewer })` — the one page. Renders `<ObjectPageShell>` chrome and the sequence below. Replaces the body of `app/venue/[venueId]`, `app/site/[siteId]`, `app/experience/[experienceId]`.
- `PlateResolver(presentation, viewer) → {kind: 'yours'|'provider'|'none', url?, credit?}`; `Plate` renders `kind`; `none` renders nothing (title under the warm bar — existing absence contract).
- `Kicker({ categories, lineage })` → "GARDEN RESTAURANT · SORRENTO"; town is a `Pressable` to `routes.place(slug)`.
- `PresenceByline({ people, viewer })` → faces (recency order, viewer last, umber) + label; `null` when no one. Tap face → `onOpenFace(line_id)`.
- `FactPair({ ranked })` + `ClosingRow({ ranked })` from `rankFacts(facts, viewer)` (§6).
- `ObjectBody({ paragraphs })` where paragraphs come from `composeBody(research, dossier, today)` (§5). Each paragraph: `{ text: RichText, markers: MarkerRef[] }`.
- `SourcesList({ sources })`.
- `Verbs({ viewer })` → `[Tonight?]`, `Ask Vesper` (→ `routeForPrivateAsk(seed)`), `Leave for someone` (→ addressed-handoff composer, dark today: stub behind `FLAG_LEAVE_FOR_SOMEONE`).
- `WhereRow({ address, lat, lng, display_policy })` → `StayLocationMap` thumb 96pt with `mapSurface = display_policy.map_surface`, address, `Directions` → `openDirections`.
- `FaceSheet({ line })` — the only section; under the byline; USEFUL (author-only signal), KEEP FOR ME, REPLY (→ Chat anchored to the Place).
- `ArrivalLine({ research })` — shown once when `research.generated_at` is newer than `viewer.last_open_at`; not persisted.
- `CandidateRow` (in-card resolving with idempotency key) and `OriginStopCard({ retryable })` — from the resolution brief; unchanged.

## 4. Data contracts

**Existing (use as-is):**
- `GET /api/me/entities/{type}/{id}/presentation` and `/presentation-v2` → `EntityDetailPresentation` / `EntityDetailPresentationV2`. Use `entity.name`, `entity.lineage`, `categories[]`, `facts[] {label, value, source_mode, observed_at, expires_at}` (**keep provenance — the current mapper drops it**), `relationship`, `take` (persisted only), `entity.status {operating, open_now, hours, as_of, sources}`, `entity.photo_urls`, and `entity.display_policy.map_surface` (**this exists on the wire — the earlier note that map_surface was missing is stale; use it, never infer from catalog_state**). V2 carries canonical relationship/capabilities; live situation remains a separate no-store route.
- `POST /api/me/entity-resolutions` and the existing entity routes. A generalized exact-photo route is proposed below; it does not exist on local `main` yet.

**Landed read slice (2026-09-04):**

- `GET /api/entities/{type}/{id}/research` returns a sanitized
  `EntityResearchBrief` from an existing completed brief. The app treats 404
  as sparse state. It never starts a provider/model call, queue job, or write.
- The mobile `ObjectPageRebuild` and deterministic `rankObjectFacts` projector
  are internal-build-only; public builds keep the existing page until the
  remaining body, people, and action contracts land.

**Proposed (backend, not landed on local `main`):**

The following endpoints and models are design proposals only. They are not in
the current OpenAPI contract and must not be added to generated types or
consumers until their source, privacy, cost, and ownership contracts are
reviewed:

- `POST /api/me/entities/{type}/{id}/research-requests` enqueues (idempotent per entity); triggered by the page open, never awaited. Cache shared across viewers; TTL 30 days; regenerate on explicit "read up". This remains gated on provider terms, cost ceiling, source retention, and job ownership.
- `GET /api/me/entities/{type}/{id}/people-lines` → `PeopleLine[] { id, author {id, display, monogram}, grant_kind: 'left_for_you'|'circle'|'city_precision', precision: 'place'|'city', made_at, text, photo?: {url}, thread_ref?, used_in?: {occasion_id, label}, can_take_back: boolean }`. **Viewer-relative resolution is server-side:** blocked, outside audience, wrong precision, withdrawn are simply absent. City-precision lines appear only on the container page.
- `viewer` context assembled client-side: `{ location?: {lat,lng, explicit_once: true}, local_time, occasion_live?: {id, label}, last_open_at, text_scale }`.

The current entity branch provides canonical identity, presentation v2,
bounded situation reads, a read-only persisted research projection, and an
internal guarded object-page renderer. It does **not** yet provide
`people_lines`, a generalized photo endpoint, addressed-handoff UI, or the
research request/refresh job. Those remain follow-on contracts, not hidden
capabilities of the existing API.

## 5. The body — composition template (`composeBody`)

Paragraph jobs, in order; each 2–4 lines at default scale; drop a job when its inputs are empty; never pad:

1. **What it is** — `research.text_paragraphs[0..1]` verbatim (model output, cached); markers = the research source numbers already attached server-side.
2. **Today** — template, no model: `"Open until {status.hours.close} tonight."` when known → marker = listing (`status.sources[0]`, `as_of`); `"{walk} on foot from {you|anchor}."` from the ranker. Omitted when both facts are already in the pair (they usually are — this paragraph exists for the planning posture).
3. **Who has been** — template: for each `people_lines[]` (max 3, recency): `"{Author} was here in {month} and left a line for you: “{text}”"` → marker = face. Then `"You kept it {when} for {your_line?}."` → your face. Quotes are inserted byte-for-byte; never paraphrased.
4. **What to do** — `dossier.verdict_sentence` if a governed dossier/angle touches the place. A model-derived fallback is a later option **only if it is precomputed in an owned research job** and uses cited sentences exclusively; it is not eligible for synchronous read-path generation under the current entity-system law. Uncited by design; at most one.

Markers are attached by the composer to the sentence it placed; the model never emits markers. Sources list = research sources (numbered) + people (faces) + listing (numbered) in first-appearance order.

## 6. Fact ranker (`rankFacts`) — a table, not a model

Inputs: `near = viewer.location && distance ≤ 30 min walk`; `evening = local_time ≥ 17:00 || status.open_now`; `occasion = !!viewer.occasion_live`; fact presence.

| Fact | source | arriving (near) | planning (!near) | null |
|---|---|---|---|---|
| open_until | `status.hours/open_now` | pair | below as week hours | below: "Not checked" + check action |
| from_you | `viewer.location` → walk/drive | pair (walk · drive) | below: from town anchor | absent |
| price | `facts[label=price]` / tail | below | pair | below: "Unknown" |
| table | `reservation_required` + link | below (+link if url) | pair (+link) | absent |
| where | address + lat/lng | closing row | closing row | pair when < 2 others present |
| access | `wheelchair_accessible` | below when known | below when known | absent |

Pair = top two by that order; closing row = the rest (max 4); a null never enters the pair. Container pages: pair = `now` (time/light) + `from_you`.

## 7. State machines

- **Resolve** (from the brief): `idle → resolving(key) → {navigate(canonical) | shell(canonical) | fail(retryable) | stop(non_retryable)}`; retry reuses `key`; duplicate taps are no-ops.
- **Sheet:** `closed → open(line_id)` on face tap; `open → closed` on back/scrim; REPLY → push Chat and keep `open` for return; USEFUL → `sent(line_id)` (idempotent, author-only).
- **Arrival:** `research=null → present`: show `ArrivalLine` if `generated_at > last_open_at`; swap body in place; on next open, `last_open_at` updates and the line is not shown.
- **Live check:** `idle → checking → {success(as_of, source) | unavailable}`; success writes into the `open_until` fact for this session only.
- **Tonight?:** visible iff `occasion_live`; tap → the Occasion's question sheet (`Put it in` / `Not tonight`); page unchanged.

## 8. Delete safely

**Page-local removals (component survives elsewhere):** `SpotPlanningRail` (experience still uses it until step 0 lands there too), `ItineraryStopStrip` (itinerary owns it), `SpotTake` (Chat/other readers), `WhyForYouCallout` (feed), `StayLocationMap` (kept, reused as the thumb).
**True deletions after step 0:** `AskVesperBlock`, `OrderSkip`, the `Details` drawer, `WorldSection` + `WorldLinkRow` on object pages, `EntityInterpretationBlock` (unwired), the one-photo scroller, `CatalogEvidenceDisclosure` from the ordinary path, the `why_for_you` route param.

## 9. Steps (each a PR; each green on the tests it names)

0. **Landed behind `OBJECT_PAGE_REBUILD_ENABLED`:** shared skeleton on venue/site/experience with existing data only: provenance-bearing exact-photo plate (venue), kicker, name, deterministic pair + closing row, persisted body, text verbs, where row, and square plate. The v1/v2 compatibility paths remain available. Provider-photo policy and richer citation assertions stay gated.
1. **Read slice landed:** `EntityResearchBrief` projection + client hook read an existing completed brief and normalize 404 to sparse state. The queue, refresh request, inline markers, sources UI, and `ArrivalLine` still require a separately approved research owner, source policy, TTL, and generated-contract update; this read must not become read-path generation. T7–T9 remain open.
2. Dossier as optional input; paragraph 4. Mode-key row model retired for browse pages.
3. `people-lines` endpoint with server-side viewer resolution; byline, paragraph 3, `FaceSheet`, USEFUL/REPLY. T12–T13.
4. Large-text pass. T10.
5. Candidate origin harness + resolve states on the new page. (Brief's paths.)
6. Spot admission + owner-shell promotion (flagged); share contract; live check slice.

## 10. Open questions the agent must not resolve alone

Dedupe/conflation spine for the identity seed · provider photo terms per provider · research TTL/cost ceiling · the second-owner promotion rule · whether a kept place and a pin are one record · the Occasion-live signal's source on Home.
