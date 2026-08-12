---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-08-11
decided: 2026-08-11
why_new: Settle what "entity" and "place" each mean, so the question stops being re-litigated per surface, and record the vocabulary consolidation and site page that followed from the answer.
supersedes: []
source_of_truth_for: [entity-page-archetype, entity-type-vocabulary]
---

# Entity and place are two axes, not two categories

## Context

"Is a neighbourhood an entity or a place?" had been asked and answered
differently in at least ten places, and the disagreement was shipping:

- `EntityRef` and the governed substrate (`entity_fact_claims`,
  `entity_external_identities`, `entity_semantics`, `entity_readiness_certificates`)
  said `place` **is** an entity type.
- `TakeEntityType` excluded `place` but included `neighborhood`.
- The Places screen implemented neighbourhood as `place` at finer grain via a
  `hood` param — a container, not an object.

All three were shipping simultaneously. The vocabulary itself had fractured
into 26 hand-typed definitions — 10 SQL `CheckConstraint` strings and 16
Python `Literal`/`frozenset` declarations — and no two agreed on the same set.

The most visible consequence: **`site` had no page.** Museums, monuments,
viewpoints, parks and gardens are `sites`. They had a table, dossiers, saves,
itinerary blocks, trip-map pins, narration and search hits — and no detail
endpoint and no route. Every surface routed around the hole independently;
`app/guide/[slug].tsx` shipped a comment explaining why a museum row was
deliberately not tappable. You could save a museum, plan a museum, and be
narrated at a museum. You could not open one.

This decision complements
[2026-08-08-place-identity-and-provenance](./2026-08-08-place-identity-and-provenance.md),
which settled the identity axis and remains authoritative for it. Nothing here
changes `EntityRef`.

## Decision

### 1. The two axes

**Entity and place are not two categories on one axis. They are one category
viewed on two axes**, and the codebase used the word "place" for both.

**Identity axis** — a place *is* an entity. `place` is a member of
`ENTITY_TYPES`, exactly as the 08-08 decision established for `EntityRef`.
This governs references, resolution, external identity, and fact provenance.

**Page-mechanic axis** — a place *contains*; an object *is visited*.

| | Object | Container |
|---|---|---|
| What it is | a bounded thing you go to | a region that holds things |
| Earns a Take | yes | no |
| Has hours / price / duration | yes | no |
| Recurses into itself | no | yes (`places.parent_id`) |
| Page | `ObjectPageShell` — plate · title · facts · Take · foot | lens spine + aggregation rooms |
| Table | `venues` / `sites` / `accommodations` / `experiences` | `places` |

Both statements are true at once, and neither system was wrong. **A
neighbourhood is an entity by identity AND a container by mechanic.** The
question was unanswerable as posed, which is why it kept coming back.

### 2. The adjudication test

When a new kind is not obviously one or the other: **does it have opening
hours, and does it deserve a verdict?**

Piazza Navona does not → `place`. Villa Borghese (gates, ticketing, a
two-hour visit) does → `site`.

This resolves a live inconsistency in the seed schemas, where `PlaceType`
contains `square` while `SiteType` contains `park`, `garden` and
`neighborhood_walk` — the same kind of bounded outdoor public space sorted
into opposite bins with opposite page mechanics. The test governs; the
existing rows are not retroactively migrated (see Non-goals).

### 3. One vocabulary, and subsets are capabilities

`backend/core/entity_types.py` is the single source of truth. Every
downstream vocabulary is a **derivation** of `ENTITY_TYPES` filtered by a
capability, never an independent literal.

Subsets are named after what an entity can **do** (`PLANNABLE`, `NARRATABLE`,
`TAKEABLE`, `EDITORIAL`, `CATALOG`, `GEOCODED_CATALOG`), not after the module
that consumes them. Two modules needing `{venue, site, experience}` need the
same thing, and giving that set one name is what stops a 27th copy.

It lives at `backend/core`, **not** under `core/db/`: `backend.core.models` is
a pure Pydantic layer that imports without SQLAlchemy, and routing the
vocabulary through `core.db.tables` would make it depend on the DB layer to
name a venue. `core.db.tables` re-exports every symbol.

`scripts/check_entity_type_parity.py` enforces it in pre-commit and CI —
Literal mirrors, bound `CheckConstraint`s, and the live DB.

### 4. `neighborhood` is `place`, and is not collapsed yet

`neighborhood` is not a seventh entity type. It is `place` narrowed by
`place_type`, and **the data already agrees**: `backend/core/takes/context.py`
emits `entity_type="neighborhood"` with `entity_id=str(place_id)` — a
`places.id`. `takes/backfill.py` maps it to `briefs.place_id`.
`place_affinity.py` states it in prose.

Recorded in `ENTITY_TYPE_ALIASES`. **Not collapsed in this pass**: live rows
in `entity_saves` and the takes cache are keyed on the string, so folding it
needs a data migration — plus a product call on whether a *city* should also
be saveable and takeable. Today it is not, and that asymmetry is the real
question hiding behind the alias.

### 5. Every place-like entity resolves through one router

`utils/entityRoute.ts` (`routeForEntity`) replaces eleven independent
`switch (entity_type)` blocks that had already drifted — Discover handled
`guide` but not `place` or `site`; universal search handled `place` but
dropped `guide`, `site` and `angle`, each through a silent
`default: return null`.

The deduplication is not the point. **`assertNever` is**: the union is
exhaustive, so adding an entity kind is a compile error in one file rather
than a row that quietly stops being tappable on one surface.

A `null` return is a legitimate answer meaning "this kind has no page", and
callers must render the row as non-tappable. `transport_hub` returns null by
design: it is a routing primitive with no editorial, no Take, and nothing a
page would show.

Mappings that are **not** navigation — save targets, telemetry refs,
conversation seeds, result icons — deliberately stay with their callers.
Several correctly handle kinds that have no page, which would be a bug in a
router.

### 6. Sites get a page

`GET /api/sites/{site_id}` and `app/site/[siteId]`, the third face on
`ObjectPageShell`. The shell's own docstring already named this case; this is
the first proof it generalizes past the two faces it was extracted from.

**Kind picks slots, never chrome.** A site is the shared plate with a
different per-kind tail (period, significance, admission) and without the
venue tail (cuisine, dietary, group comfort). The venue polish pass found the
real difference is DENSITY, not category — a viewpoint is a museum with less
— so every block renders only with real data and a sparse site degrades to
identity plus map.

Two divergences from the venue face, both forced by data rather than taste:

- The hero is `EntityImage` (the riso waterfall), not `PlacesMedia`.
  `PlacesMedia` gates on `claim_scope` from a resolved provider lookup and
  `sites` has no `google_place_id` to make one against. A site therefore
  always gets a plate; the illustration pool is a deliberate brand answer,
  not a gap.
- `accessibility` renders as the curated free text it is. `sites` has no
  `wheelchair_accessible` boolean, and coercing prose into a yes/no would be
  a fabricated fact.

### 7. Amendment to the 08-08 identity decision

`EntityRefType` in code carries `transport_hub`, which the 08-08 decision's
written contract omits. The code is correct and the doc is behind; this
records the seventh member rather than changing anything.

## Non-goals

- **Not** collapsing `neighborhood` into `place` — needs a migration and a
  product call (§4).
- **Not** narrowing `entity_takes`, whose CHECK permits `trip_story` because
  it was hand-copied from `entity_saves`. Preserved as
  `TAKE_CACHE_ENTITY_TYPES` with the gap declared. Tightening a live CHECK
  needs proof no such rows exist, and "nothing produces them" is a weaker
  claim than "none exist".
- **Not** re-sorting existing `square` / `park` rows. The test in §2 governs
  new kinds; a migration is separate work.
- **Not** unifying the four catalog tables. `venues`, `sites`,
  `accommodations` and `experiences` share a near-identical column spine and
  diverge only in their tails, but merging them is a schema decision this
  does not make.
- **Not** giving `transport_hub` a page.

## Consequences

- A museum is openable. Sites are tappable in guides, dossier exemplars and
  search.
- Adding an entity type is a compile error in `entityRoute.ts` and a parity
  failure in CI, instead of a silent per-surface omission.
- The next person asking "is X an entity or a place?" has a test to apply
  rather than ten precedents to choose between.
- The remaining consolidation — one entity read contract over
  `entity_fact_resolutions`, so facts and judgment stop coming from two
  parallel systems — is unblocked but not done.
