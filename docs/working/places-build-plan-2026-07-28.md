---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-07-28
expires: 2026-08-27
why_new: The Places design is complete and adjudicated across 19 canvas sections, but no document maps it against the code that would implement it. This is the first note to audit both repos for Places specifically — establishing that the tab is 47 lines of bridges over 1,561 borrowed ones, that there is no Places API at all, and that unified-ingestion Phase 0 already shipped the place-identity model Places needs — and to sequence the work as tracks with the five open design rulings closed inline.
promotes_to: a `docs/systems/places.md` charter once Track C's projection exists, plus a canon export of PLACES - CORE.html when the surface is built
supersedes: []
source_of_truth_for:
  - places-build-sequencing-and-track-ownership-2026-07
  - places-design-rulings-2026-07-28
---
# Places — Build Plan (debt-free posture)

**Date:** 2026-07-28
**Design source of truth:** `PLACES - CORE.html` (Claude Design → Vesper), 19 sections
**Posture:** the same ruling taken for ingestion on 2026-07-27
(`unified-ingestion-research-2026-07-27.md` §12.5) — pre-launch, no users, no
compatibility constraints, take the larger refactor, carry no deliberate
dead-end states.

---

## 0. Picking this up cold

**This file is the handover.** Read it first, then open the canvas — the plan
sequences the work, the canvas *is* the spec.

**The design lives in the Claude Design project "Vesper"**
(`project_id: 551f400f-3da1-42ab-be7f-35f2d28e7c75`), not in this repo and not
in the canon mirror. Two pages matter:

| Page | What it is |
|---|---|
| `PLACES - CORE.html` | **The spec.** 19 sections, 74 artboards. Screens, states, contracts, rulings, cut ledger. Banner says EXPLORATION — that is accurate, it has never been exported to the canon mirror. |
| `PLACES - COMPONENT MAP.html` | **The parts catalogue.** All 49 components rendered live, in 8 layers, each stamped with its ship tier — plus every state unrolled full-height with the 852px fold marked. Where it and CORE's inventory table disagree, the map is right. |

Its modules are `places-foundation-kit.jsx` (the Pass 4 shell, layer 1, consumed
unchanged) and `places-core-*.jsx` (layers 2–7 + the doc boards).

**Do not touch:** `PLACES - COMPONENT POLISH PASS 3.html`, `... PASS 4.html`,
`... PASS 5.html` are version history. `Vesper Places.html` is real canon for
venue detail and is consumed as-is — every row on every Places surface ends
there.

**Start at A1** (§3, Track A). It is one line plus a save path, it is the only
irreversible decision in the plan, and every list on every surface is broken
until it lands. Everything else is additive or a deletion.

**Also registered:** `design/surface-manifest.yaml` → "Places Tab (root browse
surface)". Deliberately `canon: []` — do not drift-check it until a canon export
exists.

---

## 1. What is actually true today

Verified in the code on 2026-07-28, not assumed. Several claims carried in
earlier notes were wrong and are corrected here.

### Frontend

| | |
|---|---|
| `app/(tabs)/places/*` | **47 lines total.** All four routes are thin bridges. |
| `index.tsx` | → `components/places/PlacesWorkspace.tsx` (14 KB). Real, but its own docstring calls it a "temporary composition bridge". |
| `saved.tsx` | → `app/atlas/saved-places.tsx` · `SavedIndexScreen` (269 lines) |
| `been.tsx` | → `app/atlas/long-view.tsx` · `AtlasLongViewScreen` (720 lines) |
| `map.tsx` | → `app/(tabs)/discover/map.tsx` · `DiscoverMapScreen` (572 lines) |
| Borrowed total | **1,561 lines**, against 47 of Places' own routing. Confirmed. |
| Tabs | 3 visible — `trips`, `concierge`, `places`. `discover` and `atlas` are `href: null`. Matches the canvas. |

**`PlacesScope` exists** (`utils/placesWorkspace.ts`, 96 lines) — an earlier note
saying otherwise was a bad grep, not a real gap. But it is:

- **three kinds** (`all | city | trip`), where the design needs six (adds Home,
  Around me, and distinguishes Anywhere from "all my saves");
- **client-side only** — rehydrated from route params each mount, never
  persisted, so the design's "scope survives search, map, detail and tabs" is
  not implementable against it;
- **city scopes derived from saved cities only** — you cannot scope to a city
  you have never saved in, which makes the design's "Selected city" screen
  unreachable;
- already correct on one hard rule: `defaultPlacesScope` carries the comment
  *"Never invent a home location."*

### Backend

**There is no Places API.** No `backend/api/routes/places.py`. The taste ranker
`discover_nearby_ranked` is reachable from exactly one place —
`api/routes/concierge_home.py:352,363` — at the home feed's limit of 3.

| Claim | Verdict |
|---|---|
| Live-provider places have `id: None` | **True, and it is one line**: `places/discovery.py:88`, in `_nearby_to_row`, commented `# not in our corpus`. |
| `entity_saves` has no `trip_id` | **True but not a gap.** The schema comment is explicit: *"a save is user-scoped ('I value this place'); a commitment is trip-scoped"* — `trip_venue_commitments` is the trip-scoped table. Scoping saves is a **join**, not a missing column. |
| Home is split across two stores | **True.** `traveler_profiles.profile_summary` JSONB (`home_city`, `home_neighborhood`) *and* `user_facts["home:primary"]`. No lat/lng in either. |
| Been has no producer | **True.** No visited model in `core/db`. |
| Dossiers are city-scoped | **False.** `dossiers` keys on `venue_id` / `site_id` / `accommodation_id` — **place-keyed**. `get_dossiers_for_place_ids` exists; nothing resolves a *city or trip* to its dossiers. The Reading destination needs a join that does not exist. |
| A canonical meal vocabulary exists | **False.** `home/feed.py:340` has an ad-hoc food-word set; `planning_agent/restaurant_schemas.py` has `meal_type: Literal[...]`. Two vocabularies, neither canonical. |

### The thing that changes the plan

**Phase 0 of the unified-ingestion refactor is already shipped.** `venues` and
`sites` both carry `origin` (`server_default='curated'`,
`_tables/venues.py:114,255`) and `verification_status`. The corpus filter
`verification_status == "verified"` is installed at **18 read sites across 5
files** — `core/db/search.py` (7), `planning_agent/db_provider.py` (4),
`core/db/entities.py` (3), `core/db/content/_briefs.py` (2),
`core/db/content/_brief_state.py` (2) — so browse, planner *and* brief-authoring
paths are all already gated. `create_provisional_venue_in_tx` and
`create_provisional_site_in_tx` exist with owner-scoped idempotent dedup that
reuses the existing `uq_venues_external_source_id` constraint.

Places does not need to invent a place-identity model. It needs to **use the
one that landed three weeks early**.

---

## 2. Decided: how a live-provider result becomes addressable

> **Ruled 2026-07-28: Option A.** Recorded with the rejected alternatives
> because the reasoning is the thing worth keeping.

**The problem.**

`requireId` in the design throws on a place with no stable id — deliberately, so
a duplicate can never reach the traveler. `_nearby_to_row` emits `id: None`.
Those two cannot both ship.

**Option A — namespaced provider id, materialise on save** ✅ **CHOSEN**
Provider rows carry `id = "provider:{name}:{external_id}"`. Stable, dedupable,
routable; detail opens against the provider. The first time a traveler *saves*
one, it materialises into a provisional `venues` row and the save rewrites to
the real id.
*For:* no catalog pollution from results nobody touched; promotion path exists
(save is the promotion); corpus filter untouched.
*Against:* a second id namespace exists in the read path, which is the shape —
though not the substance — of the `atlas_kept_place` debt §12.5 warns about.
The difference is that this one has a resolution path and that one never did.

**Option B — materialise on discovery**
Every provider row becomes a provisional `venues` row at discovery time.
*For:* exactly one id namespace, everywhere, forever.
*Against:* writes rows for every result scrolled past; needs a third `origin`
value (`provider_discovered`) and turns the clean `verification_status` filter
into a two-clause predicate; unbounded catalog growth keyed on provider
coverage, not traveler intent.

**Option C — drop the provider merge.** Corpus-only lists. Rejected on sight, but
worth recording: the corpus is city-seeded, so this empties Places everywhere you
have not seeded. Naming it clarifies that **the provider merge *is* the
global-coverage feature**, and the id problem is its price.

**Why A.** The save is genuine intent, so materialising on intent is the honest
trigger. B writes a row for every result scrolled past — at 8 candidates per list
load the catalog becomes a mirror of the provider's index, keyed on *their*
coverage rather than travelers' interest. A → B is a backfill; B → A is a delete
with referential checks. And §12.5's warning is about *dead-end* states: A has a
promotion path, which is exactly what `atlas_kept_place` never had.

**Carried in with it — the dedup fingerprint.** Corpus/provider dedup today is
casefolded **name matching** (the `seen` set in `discovery.py`). That is too weak
to keep: "Ramiro" and "Cervejaria Ramiro" are one place, and two Court Street
Grocers shops are two. Give it the same `dedup_fingerprint` treatment the
provisional writer already uses. This is part of A1, not a follow-up.

---

## 2b. Decided: what fills the highlight slot in v1

> **Ruled 2026-07-28.** The ship-split table said "all three variants, safe to
> defer"; the grammar board said GuidePreview was promoted; there are now four
> variants. Both boards were stale. This is the resolution.

**Ship the slot, with `GuidePreview` as its only occupant.**

The canvas justified promoting Guide on coherence — "a guide is *also* a set of
places, so it feeds the scan instead of competing with it." The stronger reason
is **cost**: it is the only variant whose data exists today (621 published
dossiers), and with exactly one variant, eligibility degenerates to an
**existence check** rather than a scorer (see C8). Almost nothing to build.

That matters because the thing you cannot retrofit is the slot's **absence**
state. One variant proves the entire mechanism — eligibility, dedup, backfill,
absent-not-empty — at close to zero cost, and every later variant drops into a
position whose behaviour is already established and tested.

The queue behind it:

| Variant | When | Gated on |
|---|---|---|
| `GuidePreview` | **v1** | nothing — dossiers exist |
| `SharedPlacesPreview` | **variant two** | the per-save privacy gate for friend saves |
| `GapPreview` | with **C7** | trip projection distinguishing "no dinner" from "we don't know" |
| `PlaceCarousel` | **deferred indefinitely** | — |

`SharedPlacesPreview` is next specifically because it is the only one of the four
that renders the multiplayer loop, which is the wedge. `PlaceCarousel` stays
deferred because a group of places you already loved, shown above a list of
places, is the closest of the four to what the eligibility rule itself warns
against — "a second reading of one list".

---

## 3. Tracks

Tracks A–C are backend and gate everything. D is frontend. E is content.
Within a track, items are ordered; across tracks, A → C → D is the critical path.

### Track A · The place identity spine

**A1. Kill `id: None`.** Rewrite `_nearby_to_row` to emit a namespaced provider
id (per §2 Option A). Add `requireId`'s equivalent server-side: a discovery row
without an id is a bug, not an edge case — raise, don't pass through.

**A2. Materialise-on-save.** `POST /api/saves` accepts a provider-namespaced id;
resolves it through `create_provisional_venue_in_tx`; persists the save against
the real venue id. Reuses the shipped Phase-0 writer — no new table, no new
dedup strategy.

**A3. Audit the read surfaces.** Phase 0 installed the corpus filter at 18 sites
across browse, planner and brief-authoring. Places adds read paths; each one
states explicitly whether it includes provisional rows. Provider/provisional rows
appear **only** in a scoped list that asked for them, never in editorial, planner
or Qdrant retrieval. The filter is already thorough enough that the failure mode
is a *missing* filter on a new Places query, not a leak through an old one.

**A4. Been is CUT for v1 — the destination, the entry point and the marker.**
*(Ruled 2026-07-28.)* There is no visited model, and the cheap derivation —
a block with a `venue_id` on a past day of a trip you were in — is **dishonest**:
a *planned* block is not a *visited* place. That is a defaulted claim, which is
precisely what the surface's own rule forbids ("unverified must arrive as
unverified"). That rule is what makes every other claim on the page trustworthy;
spending it on a low-traffic retrospective feature is a bad trade. Honest Been
needs explicit confirmation or photo/location evidence, and neither is on the
critical path.

Three things this pays for:
- **−720 lines** from D1's un-borrow scope (`AtlasLongViewScreen` is no longer
  reached at all), taking borrowed code from 1,561 → **841**.
- What ships there today is Atlas's *reflective* voice, which the design says
  explicitly must not carry over — so the current implementation was wrong
  regardless.
- The marker grammar drops **six markers → five**, so the honesty gap on the
  provenance board narrows from 4-of-6 unbacked to 3-of-5.

Delete `app/(tabs)/places/been.tsx`. Do not leave a bookmark that opens an empty
room — the Saved-visibility rule already forbids it.

### Track B · Scope, position and anchor as three server facts

The design's `PositionModel` board is unambiguous that these are three separate
values. Today there is one client-side union that conflates them.

**B1. One Home.** Collapse `profile_summary.home_city` + `user_facts["home:primary"]`
into a single authoritative store carrying **lat/lng**, written once at
onboarding. Two stores for one fact is precisely the debt this posture kills.
Nominatim-per-request goes away with it.

**B2. Persisted scope.** A resolved scope is server state, not route params.
Six kinds. Survives search, map, detail, tab switches and cold start.

**B3. Position and anchor separately.** Position: known-here / known-elsewhere /
unknown, plus an age. Anchor: live / stay / home-precise / home-area /
destination / unavailable — and the projection **states which anchor it used**
rather than emitting a bare distance. A permission change alters precision,
never which scopes exist.

**B4. City scopes stop depending on saves.** A city you have never saved in must
be selectable, or the "Selected city" screen is unreachable.

**Implementation status (2026-07-28): B1–B4 landed in backend commit
`db2fd449`.** `users.home_location` is now the sole authoritative Home;
`users.places_scope` persists all six scope kinds; the resolver reports
position and the explicit anchor it chose; and city scopes accept either a
corpus place id or explicit coordinates, independent of saves. Historical
`home:primary` facts remain provenance only. The migration upgraded cleanly
from an empty database through the single Alembic head, and the fresh-schema
offline run passed 14,669 tests; its two failures were unrelated existing
venue/site field-consistency gaps for unified-ingestion columns.

> **More load-bearing than it looks.** B4 is not a scope-picker nicety — it is
> the entire reachability story for 621 dossiers. See E1: once any city is
> selectable, any city's content is one scope-change away, which is what closes
> the hole the three-tab ruling appeared to open.

### Track C · The Places projection

**C1. `GET /api/places`** — one endpoint returning the seven-section projection
for a resolved scope: map summary, the optional scored highlight, the ranked
list, experiences, the reading door, areas. Existence-gating happens **here**, so
"absent, never empty" is a property of the payload rather than a rule each client
re-implements.

**C2. Expose the ranker.** `discover_nearby_ranked` currently escapes only
through the home feed at limit 3. Give it a real paginated scoped call.

**C3. Relationship + provenance projection.** **Five** markers after Been is cut
(A4), of which two have producers. Ship the two, and have the projection say
which of the other three are *unknown* rather than *absent* — the honesty rule
from the marker-backing board.

**C4. Operational truth with a freshness contract.** Unverified hours must
**arrive** unverified. A projection that defaults unknown to closed makes
`StatusText` lie, and that component is on every row on every surface.

**C5. Scoped saves.** A join, not a column (per §1). Precedent already exists:
`traveler_place_affinity` denormalizes `entity_city` *"so the read path can match
against a trip's destination without walking the entity"* — reuse that shape.

**C6. Scoped dossiers.** Dossiers are place-keyed. The Reading destination needs
city/trip → dossiers. New query, plus the `>1 dossier` count that gates the
entry point.

**Implementation status (2026-07-28): C1–C6 landed.**
Backend commits `b05be32d`, `17c0cf5d`, `84ccc496`, `e859f0e5`, and
`b95f97de` publish the authenticated seven-position projection, paginate the
shared ranker, batch-project cache freshness without provider fanout, page
explicit personal saves, resolve membership-safe dossier doors, and persist
authorized scope changes. Backend `d15cb49e` closes C3 with honest marker
knowledge. Root commits `6ed14cf`, `63395a2`, and `c7df72b` publish the GET,
PUT, and marker contracts. The focused Places backend suite passes 180/180.

The C3 source was recovered from
`Downloads/vesper 400/project/places-core-backing.jsx` and
`places-core-kit.jsx`: after Been is cut, the exact priority is `In trip`,
`Loved`, `From <trip>`, `From your <guide>`, `Saved by <friend>`. The first two
batch-read real commitments and the canonical affinity bucket. The other three
serialize as explicit `unknown` and remain display-ineligible; friend
provenance additionally stays blocked on the missing per-save privacy gate.
The complete Places suite passes 180 tests. Backend main currently has another
session's staged index, so the backend commit and regenerated shared snapshots
await a clean landing window rather than disturbing that work.

**C7. Gap detection.** One canonical meal-slot vocabulary — the third time this
codebase has needed one, and the event-type consolidation already set the
pattern. Must distinguish *"no dinner on Thursday"* from *"we do not know what is
on Thursday"*, or `gapMeta`'s honest-absence rule is unimplementable.

**C8. NOT NEEDED IN v1 — highlight eligibility scoring.** *(Ruled 2026-07-28,
see §2b.)* With one variant in the slot, eligibility degenerates to an existence
check — "does a guide for this scope contain at least one place in scope". No
scorer, no floor, no type-priority arbitration until variant two.

**C9. Constraint extraction for Ask.** Structured constraints, each marked
applied or unapplicable. A client that parses the sentence itself would guess,
and a guessed constraint printed as a fact is the one failure the ask design
cannot absorb.

### Track D · Frontend

**D1. Un-borrow, don't re-wrap.** With `discover` and `atlas` permanently
`href: null`, `DiscoverMapScreen` is no longer *borrowed* — it is orphaned code
filed under a dead owner. **Move** it to Places ownership and delete the bridge.
`SavedIndexScreen` (269) is replaced outright by the §18 destination, not
adapted. `AtlasLongViewScreen` (720) is **not touched at all** — A4 cuts Been, so
nothing reaches it. Scope: 1,561 → **841 lines**, of which only 572 move.

**D2. The component layer.** 49 components, 8 layers, catalogued in
`PLACES - COMPONENT MAP.html`. Layer 1 (shell/scope, 17 parts) is consumed from
Pass 4 unchanged. Layers 2–7 are the build.

**D3. `CoreSurface` as the only composition.** Seven positions, fixed order,
existence-gated. Every screen is one call with different props — that is what
makes the order a fact of the code rather than a rule people remember.

**D4. The two destinations** (§18) under one contract — Saved and Reading, seven
states each, differing only in which component fills the list.

**D5. The fourth entry and the offline root** (§19).

**D6. `SectionHeading` → the mono eyebrow (`VKicker`).** *(Ruled 2026-07-28.)*

**Implementation status (2026-07-28): D1 and the server-owned root/scope-rail
foundation landed and are device-proven.** App `8d676b4f` moves the 572-line
map to Places ownership. App `de15ec8f` adds the generated projection client,
replaces the temporary root composition, persists scope through the
authenticated write seam, registers an iPhone 16 Pro / iOS 18.2 Maestro proof
for the saved projection and scope chooser, and consumes the five-marker
priority without rendering unknown provenance. App `6181ceff` synchronizes the
generated marker contract. D2–D6 are not complete; this is the executable
foundation, not a claim that the 49-component canvas has been reproduced.

**Step-8 implementation update (2026-07-28):** app `23586ee1` lands the first
D2/D3/D6 slice: one fixed `CoreSurface`, mono `VKicker` section headings, and
the grounded map/guide/place/experience/reading/area component family with
independent open/save targets and explicit unknown-hours/time states. The mock
projection now preserves the real context contract across cold, future-trip,
live-trip, and persisted-scope states. Focused Jest passes 8/8; TypeScript and
surface registries pass; all four Places Workspace captures pass on iPhone 16
Pro / iOS 18.2 with a structured `pass` verdict. D2's remaining catalogue and
D4–D5 remain open, and E2 remains a decision gate before Reading is exposed.

The real defect was neither grammar: `SectionHeading` is **17px/600** and
`PlaceRow`'s name is **16px/600** — same weight, one pixel apart, so the heading
barely outranks its own content. Both candidate fixes resolve that ambiguity in
opposite directions (a mono eyebrow makes the label clearly subordinate; a larger
sans heading makes it clearly superior). What was broken was the middle.

Mono wins on four counts: it is canonical; `VKicker`'s docstring already names
Places as a consumer; it matches Trips, and splitting the type language by tab
was already ruled against when ScopeControl kept its serif. The decider is **fold
budget** — the gap-card measurement put position 4's heading 22px above the fold,
and a taller heading spends fold to solve what the quieter option solves for
free.

### Track E · Content

**E1. The corpus is an attribute of places. No browse-the-world surface.**
*(Ruled 2026-07-28.)* The hole is smaller than it first appeared: **B4 closes
most of it.** Once any city is selectable as a scope — not just cities you have
saved in — "we're thinking about Lisbon" resolves to *pick Lisbon → position 6
renders → its heading action opens the Reading index*. Any city's content is one
scope-change away.

What stays unreachable is **undirected** inspiration browsing — "I don't know
where, show me anything" — which is exactly the generic feed the canvas
deliberately cut, and it stays cut. No new surface to design.

**E2.** `AUTO_PUBLISH_GREEN_DOSSIERS` is `False` in prod; 621 dossiers were
published by hand. Decide the posture before the Reading destination makes
corpus size visible to users.

---

## 4. Sequencing

```
A1 ─ A2 ─┐
B1 ─ B2 ─┼─ C1 ─ C2 ─ C3/C4 ─┬─ D2 ─ D3 ─ D6 ─ D4 ─ D5
B3 ──────┘                   └─ D1 (parallel, independent)
B4 ─────────── C6 ─────────────── D4 (Reading destination)
                C5 ─────────────── D4 (Saved destination)
                C7 ─────────────── GapPreview  (variant three)
                C9 ─────────────── ask states
       privacy gate ─────────────── SharedPlacesPreview (variant two)

A4 ── deletes been.tsx ── shrinks D1
```

**A1 first, alone.** One line plus a save path, and every list on every surface
is broken until it lands.

**D1 is parallel and independent** — a move, not a rewrite.

**D6 before D3.** The heading grammar touches every section, so it lands before
the composition is assembled, not after.

**B4 gates C6 gates the Reading destination** — and therefore gates whether 621
dossiers are reachable at all. It is on the critical path for content, not just
for the scope picker.

**C7 and C9 gate features, not the surface.** The page ships without the gap card
and without ask; both are additive into a slot and a state that already exist.

---

## 5. Deliberately not in scope

- **Collection management** — folders, bulk edit, reordering, sharing. The
  durable library stays with You.
- **A polymorphic attachments table** — §12.5's conclusion stands.
- **Been, entirely** (A4) — no destination, no entry point, no marker, until an
  honest producer exists. Its reflective interpretation was never in scope
  either: that is Atlas's voice. Places answers *where*, Atlas asks *what it
  meant*.
- **The highlight eligibility scorer** (C8) — not needed while the slot has one
  occupant.
- **`PlacesEntries`** — the superseded Saved · Been shell row. Still exported,
  still renders, must not be wired.
- **The 200% shell** — Pass 4 scales its body only. Documented, deferred,
  device-gated.

---

## 6. Decisions taken 2026-07-28

All five open rulings are closed. Recorded here as an index; the reasoning lives
at each site.

| # | Decision | Where |
|---|---|---|
| 1 | Provider results get a **namespaced id, materialised on save**. Dedup fingerprint replaces name matching. | §2, A1–A2 |
| 2 | The highlight slot **ships with `GuidePreview` only**. No scorer in v1. | §2b, C8 |
| 3 | `SectionHeading` becomes the **mono eyebrow** (`VKicker`). | D6 |
| 4 | **Been is cut** — destination, entry point and marker. | A4 |
| 5 | The corpus is an **attribute of places**; no browse-the-world surface. B4 closes the reachability gap. | E1, B4 |

Net effect on v1: two decisions shrink scope (2 and 4), one is free (3), one is
the plan's single architectural commitment (1), and one turned out to be already
solved by an existing track item (5).

**Still genuinely open — but none of these block the build:** whether
`AUTO_PUBLISH_GREEN_DOSSIERS` flips before Reading makes corpus size visible
(E2), and the §7 contradictions below.

## 7. Contradictions — CLEARED 2026-07-28

- ✓ **`ScreenQuietCity` reading-above-the-list.** Fixed on the canvas, and the
  rule stood unamended: measured both ways, the door lands at 658–787 either way
  and the page ends at the same pixel. Position 4 additionally gained a
  **degradation rule** — ranked where there is signal, saved-only where there is
  not, heading stating which claim — which closes the gap that made the reorder
  tempting. The measurement, including the 20px that *does* sit under the
  floating tab bar, is recorded in the component so nobody re-does it.
- ✓ **§14 / §15 vs §4.** Both boards rewritten. The ownership row now states the
  gap amendment; the cut-ledger row reads "Planning gaps and urgency — ⚠ HALF
  REVERSED" and says which half. The ⚠ section flags became ✓ RECONCILED.
- ✓ **`ComponentInventory` 18 vs 49.** The board is a handoff summary and should
  stay short — the defect was its claim of completeness, not its row count. It is
  retitled, and §16 now states 49-across-8-layers and points at the component map
  as the exhaustive catalogue, with the map winning any disagreement.
- ✓ **Governance — partially, and honestly.** `design/surface-manifest.yaml`
  gains a **Places Tab (root browse surface)** row, distinct from the existing
  `Places` row (which is venue detail and real canon). `canon: []` deliberately,
  following the Atlas precedent: the CORE canvas is EXPLORATION and has never
  been exported to the mirror, so it must not be drift-checked. YAML validated;
  `scripts/canon-drift-check.py` still runs clean.

### Two governance items deliberately NOT done

- **The "canon route matrix" does not exist as a live artifact.** The only
  matching file is `docs/archive/2026-07/adjudicated/propagation-matrix-2026-07-09.md`,
  which is archived. The live registry is the surface manifest, now updated. The
  §17 RegisterBridge board still cites the route matrix as an open ruling gap and
  should be corrected at ratification.
- **No journey added.** `scripts/check_journey_registry.py` enforces a four-way
  registry (journeys.yaml → one-pager → README row → `JOURNEY_PERSONA_MAP`), and
  journeys are certified against *lived* dogfood flows. Adding journey 21 for a
  surface that is 47 lines of bridges would create a permanently-uncertifiable
  row. Add it when D3/D4 land, not now.
