---
doc_type: working
status: active
owner: founder / design / frontend
created: 2026-08-01
expires: 2026-08-31
why_new: The engine plan owns the Vesper Home envelope, producers, and selection. The world row it names already exists as an unfed branch inside VesperWorkbench, and a design study now settles what that row should look like. Comparing the settled design against the shipped schema exposed missing line-two facts; repository and primary-source research now resolves how each producer supplies them. This note owns the world row's presentation spec, that field mapping, and the coupled edits a row-height change forces.
promotes_to:
  - travel-app/docs/surfaces/vesper-home/contract.md
supersedes: []
depends_on:
  - docs/working/vesper-home-engine-implementation-plan-2026-07-30.md
  - docs/working/vesper-home-list-kinds-scope-2026-07-29.md
source_of_truth_for:
  - vesper-home-world-row-presentation
  - vesper-home-world-row-field-mapping
---

# Vesper Home — the world row, presentation spec

> **The row exists, has no data, and renders its edge twice.**
>
> This note does not re-open the envelope or selection rule. It specifies what
> the world row renders, records the line-two facts each producer must ground,
> and lists the files a row-height change forces in lockstep. The corresponding
> producer-contract decisions are also recorded in the engine plan so the two
> documents do not become competing sources of truth.

## Outcome

The world branch of `WorkbenchRow` becomes a two-line row carrying
**name · edge · grounded line two**, with its vertical metrics derived in
React Native rather than copied from the design canvas, and its per-kind,
font-scale-aware height reflected in the desk-density model.

At the end of this work:

- one row shell serves `season`, `route` and `here`, with kind-specific slot
  mapping inside that shell;
- the row stops printing `edge_label` twice;
- every eligible world row carries a grounded second line; a candidate without
  the required line-two evidence is omitted rather than rendered as a
  plausible one-line fallback;
- the reason line is clamped at default type and released at accessibility
  sizes;
- the density ladder receives the selected row kind and font scale rather than
  treating `SESSION_ROW_HEIGHT` as a universal list-row constant;
- no row invents a fact the producer did not emit.

## Scope boundary

| Concern | Owner |
|---|---|
| Envelope, wave split, generated types | engine plan |
| Producer implementation for season / route / here | engine plan |
| Selection, one-kind rule, edge sort, caps | engine plan |
| World-row interaction (informational in V1) | engine plan |
| Caching, privacy, observability | engine plan |
| **What the world row renders, and how** | **this note** |
| **Presentation-to-schema field mapping** | **this note + engine plan** |
| **Row height's coupling to desk density** | **this note** |

Three things the design study raised are **already ratified** in the engine
plan and are not re-argued here: the producer strategy (versioned catalog,
`season → route → here`, route dark until a canonical origin contract
exists), the interaction ruling (informational in V1, no invented tap
destination), and one-band/one-kind.

## The design source

- **Bundle:** `~/Downloads/vesper 404/project/VESPER HOME - Well Density Study.html`
- **Durable link:** [Claude Design — The World Row](https://claude.ai/design/p/551f400f-3da1-42ab-be7f-35f2d28e7c75?file=VESPER+HOME+-+Well+Density+Study.html)
- **Row + metrics in the bundle:** `vesper-world-two.jsx`
- **Spec, open list, build blockers:** `vesper-world-spec.jsx`

§1 is the spec, §2 the build blockers, §3 evidence, §4 open design questions,
§5 what was deleted. The bundle is an HTML/CSS prototype — a description of
intent, **not a source to port**. See *Canvas → React Native* below for the
specific way copying it goes wrong.

## Current state

There is no `WorldWindowRow.tsx`. The world row is the first branch of
`WorkbenchRow`, forked on `item.kind !== 'sessions'`:

- `travel-app/components/vesper-workbench/VesperWorkbench.tsx:433-467` — the
  world branch (a plain `View`, no press handler, no accessibility role)
- `:470-518` — the session branch, wrapped in `Tap`
- `:688-754` — the row and heading styles
- The well itself is inline at `:265-371`, gated by
  `hasWell = Boolean(seam) || Boolean(list?.items.length)` at `:122`

It renders **three lines** today:

| Line | Source | Type |
|---|---|---|
| 1 left | `origin_iata → destination_iata` (route) or `place_label` | `capsMicro`, ls overridden to 0.8 |
| 1 right | `observed_fare ?? edge_label` | `monoStamp`, size overridden to 8.5 |
| 2 | `title`, `numberOfLines={2}` | `labelMd` — sans 15 / 500 / lh 20 |
| 3 | `edge_label`, `numberOfLines={1}` | `bodySm` + `workbenchRowState` — 12.5 / lh 17.5 |

**The redundancy the design study found is real in shipped code.** When
`observed_fare` is absent, `edge_label` renders as both the line-1 stamp and
the whole of line 3. That is the "line one carries the edge twice" finding,
independently confirmed.

**The stamp is not aligned to the title at all.** It sits on the meta row
above it. Moving it beside the title is a structural change to
`threadMeta` / `threadTitleRow`, not a style tweak.

**No producer emits a world row.** `assemble.py:151-159` hardcodes all three
producers disabled and passes an empty world list to `select_workbench_list`;
the mock marks them `status: 'disabled'`. In practice `list.kind` is always
`'sessions'` or the list is `null`. The branch is real code behind a closed
door — which makes this a low-risk rework, and also means **no device
evidence exists for any world row today.**

## What is settled

Two lines, three facts. `here` and `route` move place/origin scope to the list
cap, which already names it (`in new york`, `leaving new york`). `season` is
different: its current cap is `this season`, and a single band may contain
rows for different places. Season therefore retains `place_label` as the
prefix of line two.

```text
Restaurant Week                             through aug 16
600+ restaurants · $30 / $45 / $60 prix fixe
```

| Slot | Type | Content |
|---|---|---|
| Line 1 left | sans 15 / 19 · w500 · ink | the name. One line, ellipsis, never wraps |
| Line 1 right | mono 8 caps · mute | the edge — `season` and `here` |
| Line 1 right | mono 15 · w500 · ink | the fare — `route` only, at title size |
| Line 2 left | sans 12.5 / 1.4 · inkBody | `here`: reason · `season`: place + reason · `route`: provider-derived route detail. Clamped; released at accessibility sizes |
| Line 2 right | mono 8 caps · mute | the duration — `route` only |

**Route uses a two-column grid.** Fare beside the name, duration beside the
reason, so the right column occupies space the row already had. A rejected
variant stacked both in the right column and pushed the reason line down.

**Per-kind variation is safe** because the list rule is one band, one kind —
`route`'s two-item right column never appears beside `here`'s one-item
column. Put that reasoning in the code comment, or a later cleanup will
"fix" it into uniformity and break route.

**Why the fare is at title size.** It was an 8.5pt stamp, which put the
decision inputs in the smallest type on the row under a title reading
`Lisbon` — a word the traveller already knows. Mono is a family rule for
machine facts and carries no size implication; `constants/typography.ts`
already has mono roles at several sizes.

## Resolved field gap — how every kind earns line two

Comparing the settled row against the shipped schema
(`travel-app/utils/api/schema.gen.ts:24365-24578`):

```text
WorkbenchSeasonItem  kind id title place_label? starts_on ends_on edge_at edge_label source_as_of?
WorkbenchHereItem    …same, plus required place_id place_label
WorkbenchRouteItem   kind id title origin_iata destination_iata
                     travel_starts_on travel_ends_on edge_at edge_label
                     observed_fare? observed_at
```

| Row slot | Schema field | Status |
|---|---|---|
| name | `title` | present |
| edge stamp | `edge_label` | present |
| fare | `observed_fare` | present, optional |
| **reason / route detail (line 2)** | — | **add as required on all three item types** |
| **route outbound duration** | — | **add as required on eligible route rows** |
| **route outbound stops** | — | **add as required on eligible route rows** |

The design fixture invented `Coldest month, emptiest month` and
`384 rooms, prix fixe, most take walk-ins`. Those exact claims remain
prohibited unless a reviewed source supports them. The decision is not to
delete line two; it is to make line-two evidence an eligibility requirement.

### Decision

Every eligible world item emits a required `reason`. The meaning is typed by
kind rather than generated by the renderer:

| Kind | `reason` source | Additional required facts |
|---|---|---|
| `season` | reviewed catalog copy backed by a primary source | non-null `source_as_of`; `place_label` remains in line two |
| `here` | reviewed editorial-window copy backed by an official organizer or public source | non-null `source_as_of` |
| `route` | deterministic summary of one concrete hydrated flight offer, e.g. `nonstop from JFK` or `1 stop via LIS` | `outbound_duration_minutes`, `outbound_stops`, fare and `observed_at` from that same offer |

If the producer cannot ground those fields, it omits the candidate. The client
does not compose a substitute from a description, stale search result, travel
window, or generic source name.

The exact `reason` character budget is set after the right-column width is
measured on device. The backend schema may carry a broader safety maximum, but
the catalog/producer validator owns the tighter presentation budget.

### Season provenance

Extend the engine plan's reviewed repository catalog with `reason`,
`source_label`, `source_url` and `source_as_of`, alongside its existing
`source_note`, `reviewed_at` and `expires_at`. Climate claims can be derived
from official NOAA/WMO climate normals; phenomenon-specific claims use the
relevant primary authority. `emptiest month` is not a climate claim and needs
separate visitation or occupancy evidence.

- [NOAA U.S. Climate Normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)
- [WMO Global Climate Normals](https://www.ncei.noaa.gov/products/wmo-climate-normals)

### Here provenance

V1 uses a dedicated editorial-window catalog, not raw vendor descriptions from
the general `experiences` table. The table has useful future substrate — genre,
venue, price, description and dates — but current ingesters do not guarantee a
reliable end (`Ticketmaster` makes it optional; `Bandsintown` writes
`ends_at=None`), and current inventory and provider terms are not yet strong
enough to make generic event search the first Here producer.

Official city and organizer sources already support useful grounded copy. For
example, NYC Tourism's Summer 2026 Restaurant Week announcement supplies its
dates, 600+ restaurants, 45 cuisines, 70 neighborhoods and $30/$45/$60
prix-fixe tiers; NYC's official Event Calendar API and agency pages provide a
public-source path for city-sponsored windows.

- [NYC Restaurant Week Summer 2026](https://www.business.nyctourism.com/press-media/press-releases/nyc-restaurant-week-summer-2026)
- [NYC Event Calendar API](https://api-portal.nyc.gov/)
- [NYC Summer Streets](https://www.nyc.gov/html/dot/html/pr2026/summer-streets-to-return-to-all-five-boroughs.shtml)

The reviewed fixture line becomes, for example,
`600+ restaurants · $30 / $45 / $60 prix fixe`; `most take walk-ins` remains
absent because the cited source does not establish it.

### Route provenance

Flight Inspiration Search is discovery only. Its response supplies a
destination, dates, a discovery price and a `flightOffers` link; it does not
supply the concrete itinerary needed for the row. After discovery, hydrate a
bounded set of winning candidates through Flight Offers Search, select one
offer, and take the displayed fare, outbound duration, stops and observation
time atomically from that offer.

The repository already has the needed provider substrate:

- `AmadeusFlightProvider.normalize` parses itinerary duration and stops;
- `DuffelProvider.normalize` parses slice duration and stops;
- `NormalizedOffer` already carries `duration_minutes` and `stops`.

Do not reuse those aggregate fields blindly. Both current normalizers sum all
itineraries/slices, so a round trip becomes outbound plus return. The workbench
contract needs the first/outbound itinerary specifically. The shared
`parse_iso_duration` also accepts only `PT…`; harden it before trusting a valid
day-bearing duration such as `P1DT2H`.

- [Amadeus Flight Inspiration specification](https://github.com/amadeus4dev/amadeus-open-api-specification/blob/main/spec/yaml/FlightInspirationSearch_v1_swagger_specification.yaml)
- [Amadeus Flight Offers specification](https://github.com/amadeus4dev/amadeus-open-api-specification/blob/main/spec/json/FlightOffersSearch_v2_swagger_specification.json)
- [Duffel Offer Requests](https://duffel.com/docs/api/v2/offer-requests)

Route remains dark until the engine plan's canonical-origin and provider
approval gates pass. Duration sourcing is resolved; those rollout gates are
unchanged.

## Canvas → React Native

The study's five metrics are **canvas-only and must not be shipped.**

They were derived from canvas `TextMetrics` against web CSS line-box
behaviour. The error they correct for — a `<span>` wrapper inheriting
`font-size: 16`, building a 16px strut, and baseline-aligning its small child
inside it — **cannot occur in React Native**, which has no inline formatting
context. Android instead adds `includeFontPadding`, which the web lacks.

The method transfers; the numbers do not.

| Canvas construct | React Native | Note |
|---|---|---|
| `white-space: nowrap` + `text-overflow` | `numberOfLines={1}` + `ellipsizeMode="tail"` | RN has neither property |
| `display: flex` on stamp wrappers | not needed | no strut to remove |
| `STAMP_NUDGE 4.27`, `PRICE_NUDGE 2.38`, `DURATION_MT 8.65` | re-derive | see below |
| clamp release above 1.8× | `PixelRatio.getFontScale()` | no mechanism on this surface yet |

### Deriving the alignment in the app

The stamp's **cap top** must meet the title's. Do not eyeball it — three
attempts were lost to eyeballing in the study, and the third failed for a
reason no nudge could reach.

1. Set `includeFontPadding: false` on Android before measuring.
2. Measure each face's ascender-to-cap distance in the runtime.
3. Offset by `titleCapTop − stampCapTop`.
4. Record the derivation beside the constant, not just the value.

Any change to the title's size or line height invalidates the offset.

### Dynamic Type

Vesper Home has **no font-scale mechanism** — zero hits for `PixelRatio`,
`getFontScale` or `allowFontScaling` across `components/vesper-workbench/`,
`utils/vesperWorkbench*` and `data/vesperHome.ts`. The pattern to copy exists
elsewhere: `components/ui/ActionGroup.tsx:72`,
`components/discover/DiscoverCoverHome.tsx:147-149`,
`components/chat/GroupComposerContextBar.tsx:34-35`.

This matters beyond the clamp: `vesperWorkbenchDeskDensity.ts` estimates row
heights in fixed points, so at large system type the density model
under-counts, and `correctWorkbenchDeskDensityForMeasurement` adjusts ghosts
and scroll but **passes `rowCount` through unchanged**.

**Decision:** release the line-two clamp at accessibility sizes and make the
density input aware of both selected list kind and font scale. A single fixed
height cannot truthfully model a wrapped reason. Post-measurement correction
must be allowed to reduce visible rows before it unlocks scroll; preserving
`rowCount` unconditionally is not sufficient for the released-clamp state.

## Coupled edits

A row-height change is not local. These move together:

| File | What |
|---|---|
| `VesperWorkbench.tsx:433-467` | the world branch |
| `VesperWorkbench.tsx:688-754` | row and heading styles |
| `constants/layout.ts:298-314` | `workbenchWell` geometry tokens |
| `constants/typography.ts:199-262` | the eight `workbench*` roles |
| `utils/vesperWorkbenchDeskDensity.ts:22-27` | replace universal `SESSION_ROW_HEIGHT = 96` use with a selected-kind/font-scale row-height input; keep `LIST_HEADING_HEIGHT` coupled |

**`SESSION_ROW_HEIGHT` is the trap.** Session and world rows do not have to
share a height. Changing the constant to match the new world row would merely
make the session estimate wrong in the opposite direction. Because one band
contains one kind, resolve a per-kind estimate once for the selected list and
pass it into the density calculation. At accessibility sizes, scale that
estimate conservatively and let measured correction reduce `rowCount` before
scroll is enabled.

Two pre-existing hazards to fix or route around while in here — neither
caused by this work:

- **Color shadowing.** `VText` composes `[variantStyle, color && {color}, style]`
  (`components/ui/Text.tsx:26`), so any `styles.*` carrying a `color` beats
  the `color=` prop. `rowState`, `factValue`, `factSub`, `seamTitle` and
  `doorLabel` all do.
- **Duplicate type names.** `WorkbenchList` / `WorkbenchListItem` are declared
  twice with incompatible shapes — `data/vesperHome.ts:14-15` (the schema
  union, what renders) and `utils/vesperWorkbenchModel.ts:155-165` (a dead
  `{kind,title,days}` model). A file importing both gets whichever it named
  last. The dead TS selector also keys on synthetic `days` while the schema
  carries `edge_at`, so the two selectors are not on the same data shape.

## Implementation sequence

Ordered by dependency. The product and sourcing decisions are now recorded;
implementation starts by encoding them in the canonical contract.

| # | Step | Notes |
|---|---|---|
| 1 | Add the producer fields and sync the API contract | Required `reason` on all world kinds; required outbound duration/stops on route; required freshness on emitted season/here rows. Run the workspace type-sync workflow. |
| 2 | Build and validate the reviewed Season/Here catalogs | Every candidate needs primary-source provenance, review/expiry stamps and the final measured copy budget. |
| 3 | Re-slot the world branch to two lines | `title` moves to line 1; season keeps `place_label` as the line-two prefix; the duplicate `edge_label` line goes. |
| 4 | Move the stamp beside the title and derive the offset | Structural change to `threadMeta`/`threadTitleRow`, not a style tweak. |
| 5 | Make density kind/font-scale aware | Replace universal row-height use; let measured correction reduce rows before scroll. Ten existing tests cover the ladder and need kind/scale cases added. |
| 6 | Add the clamp and its accessibility release | Introduce the font-scale hook and prove the released state on both platforms. |
| 7 | Re-measure the reason character budget | The right column narrows the left; set the producer/catalog budget before final copy is accepted. |
| 8 | Route's two-column grid and hydration projection | Only after origin/provider gates pass; fare, reason, outbound duration and stops must come from the same offer. |

Extracting `WorkbenchWell` / `WorkbenchList` / `SessionRow` / `WorldWindowRow`
per the engine plan's frontend architecture is **optional for this work** and
better done as its own diff — the row change is legible inside the existing
branch, and combining them makes both harder to review.

## Evidence

- **`VesperWorkbench.test.tsx:215-227` will break.** It greps the source for
  the literals `workbenchWell`, `variant="capsMicro"`,
  `typography.workbenchFactValue`, `typography.workbenchDoor`,
  `typography.workbenchMonoMicro`. Update the contract deliberately rather
  than deleting the assertion.
- **`:119-153` pins world rows inert.** Keep it — the engine plan ratifies
  informational-only for V1.
- **Add:** one row per kind at default type, at the clamp boundary, and at the
  accessibility release; a `route` row proving the grid does not push the
  reason line down; a multi-place `season` band proving place remains visible;
  an assertion that `edge_label` renders **once**.
- **Add:** backend model/OpenAPI projection tests for the required fields plus
  producer tests proving an item is omitted when its reason, source freshness,
  outbound duration or stops are absent. TypeScript compilation alone does not
  prove the producer supplied meaningful content.
- **Add:** route fixtures for round trips, connections, day-bearing ISO
  durations, and atomic fare/duration selection from one offer.
- **Add:** density cases for session versus world kinds, default versus
  accessibility font scale, and measured overflow that must reduce `rowCount`.
- **Add:** a test that the alignment offset is computed, not literal — one
  that fails if someone pastes `4.27`.
- **Device:** iOS and Android, default and 135% type. Android specifically,
  because `includeFontPadding` is the difference the canvas cannot show. No
  world row has ever been captured on device.

## Open

Carried from the study's §4, not resolved here:

- **`route`'s edge is invisible** — and the code makes it literal: `stamp`
  is `observed_fare ?? edge_label`, so a route row with a fare shows no
  deadline at all, while being sorted by one.
- **Opening versus shutting is conflated.** `through sunday` and
  `opens thursday` are opposite urgencies rendered identically, in both
  `here` and `season`. Probably the largest undesigned thing left; one fix
  covers both kinds.
- **`HORIZON` is 21 days** and the second fact resolves to `edge` only inside
  it, so when `season` (21/35/44) or `route` (26/26) wins the band the fact
  strip falls through. Never drawn.
- **Session rows are not covered.** They reach two lines only by hoisting a
  shared trip kicker into the cap, which works when every open session
  belongs to one trip and not otherwise.

Two structural proposals in the study's §4 are **undecided and out of scope**:
that the well should show either the list or the seam but never both, and
that the seam and ambient weather may not belong on Vesper at all. Both
answer "the page is a wall of text", which this row improves but does not
resolve. Both need a founder ruling; the second needs a cross-surface one
with Trips.

## Exit

Before `expires`, one of:

- promote the row spec into `travel-app/docs/surfaces/vesper-home/contract.md`
  once built and device-verified;
- keep this note and the engine plan paired through the OpenAPI/type-sync and
  device-evidence work;
- archive if the engine plan absorbs this scope directly.
