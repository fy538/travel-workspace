# Places — the truth layer

**Status:** plan only, nothing built. Written 2026-08-01.

**Why it exists:** Places looks unpolished. Diagnosing the actual screenshots
showed that most of what reads as "bad design" is the surface faithfully
rendering wrong or missing data. A redesign would reproduce every one of these
problems in a nicer frame.

**The rule this plan follows:** the surface may not claim something it does not
know. That is already the canon's own discipline (§11 "what is backed, and what
writes back"; the marker-provenance rule; "absent, not empty"). Every fix below
is an application of it.

**Sequencing claim:** the §14 sectioned-browse question and any redesign should
stay on hold until this lands. You currently cannot tell whether the list reads
as undifferentiated because the *design* is flat or because every row shows the
same distance, the same picture, and a raw lowercase category. Fix the inputs,
then judge the design.

---

## Root cause: 52% of the corpus has placeholder coordinates

Measured on the dev DB, 2026-08-01:

| table | verified rows | sitting exactly on the city centroid |
|---|---|---|
| `venues` | 4,419 | **2,292 (51.9%)** |
| `sites` | 2,977 | **1,542 (51.8%)** |

Worst cities: Copenhagen 288/327, Tokyo 265/389, Brooklyn 234/279, Kyoto
194/225, Istanbul 147/176, Amalfi Coast 92/92, Rome 112/250.

Confirmed against the screenshot: Æede, Comptoir de France, Cuscus and Fior di
Luna all sit at `41.9028, 12.4964`, which **is** the Rome centroid. `ST_Distance`
correctly returns 0, and the row renders **"0 m away."** The UI is not buggy
here — it is honestly reporting a fake number.

This one fact explains, at minimum:
- "0 m away" on every row
- the map card showing ~3 pins for "20 places in view" (they are stacked)
- any distance-ordered ranking being meaningless for half the corpus

### Provenance, and why the fix is constrained

Every one of the 2,289 affected verified venues came from
`external_source = 'cursor_import'`. Of those:
- **0** have an `external_id`
- **0** have a `wikidata_id`
- the `venues` table has **no address column at all**

`grep -rn "cursor_import"` across the whole workspace returns **nothing** — no
script, no doc, no comment. This was an undocumented bulk import that produced
over half the corpus with no re-resolvable identity.

So the only re-geocoding key available is **name + city**. That makes the data
fix lossy and slow, which is exactly why it is sequenced last below — and why
the *truth* fix must not wait for it.

### This contaminates an earlier measurement

The site-density numbers in `places-sites-reachability-2026-07-31.md` ("Rome:
124 venues / 52 sites within 900m of its busiest point") were computed by
picking the venue with the most neighbours as an anchor. That anchor was almost
certainly the centroid pile-up itself. **Treat those density figures as
unreliable** and re-derive them after T6, on rows with real coordinates.

The *conclusion* that a quota is needed still holds — if anything it is
stronger, since a centroid pile-up starves genuine nearby sites even harder.
The specific numbers do not.

---

## T1 — Stop claiming a distance we do not have

**The bug:** a venue at the city centroid has *unknown* coordinates, not *zero*
distance. Rendering "0 m away" asserts precision we never had.

**Detection, no migration required:** `ST_Equals(v.geometry, p.centroid)`. At
full float precision a genuine coincidence is essentially impossible, and 2,289
exact matches is plainly systematic.

**Change:** `get_nearby_venues_simple` / `get_nearby_sites_simple` return
`meters = None` for a placeholder row rather than 0. The projection already maps
a missing distance to `None` cleanly.

**Watch out — the fallback is a non-sequitur.** `placeTruthLine`
(`PlacesCore.tsx`) falls through from a missing distance to **"Hours
unverified"**, which is a claim about *opening hours*, not location. Suppressing
the distance without fixing this just swaps one wrong statement for another. The
row needs an honest third state (or no line at all — "absent, not empty").

**Follow-up, not required for T1:** a real `coords_precision` column set at
ingest, so this is a stored fact rather than a read-time comparison.

## T2 — Stop rendering the same guide twice

**The bug:** in `CoreSurface`, the `ReadingDoor` under **WORTH READING FIRST**
is passed `projection.highlight.title` — the highlight's own title. It has no
title of its own, so **A GUIDE FOR THIS TRIP** and **WORTH READING FIRST**
render the identical object, by construction, 100% of the time.

This is not a dedup miss. There is nothing to dedup — one object is being drawn
twice.

**Change:** the reading door must carry its own subject, or the section must not
render when the only thing it could show is already in the highlight slot above
it. Note `CORRESPONDENCE.md` claims `dedupeById` is "not ported — deduplicated
server-side"; that claim does not hold for this pair.

Also in the same card: **"158 pieces"** appears twice (as the section action and
again as "158 PIECES FOR ROME"), and 158 reads as a database count rather than
an editorial promise.

## T3 — Stop showing raw enum values as categories

**The bug:** rows render `item.cuisine_type ?? item.venue_type` verbatim, so the
user sees `restaurant`, `cafe`, `bar` in lowercase — and, for the 518 venues
whose `venue_type` is literally `other`, the word **"other"**.

**Change:** a display mapper. `other` should render as nothing rather than as a
category; a place with no known category is not a place in the "other" category.

## T4 — Make the pictures mean something

**The bug (and a correction to work shipped 2026-07-31):**
`resolveEntityImage` tries the bundled **city** illustration (tier 2) *before*
the **category** pool (tier 3). `PhotoThumb` always passes a `forcedVariant`, so
for any bundled city tier 2 always resolves — and the category logic is **never
reached**.

Rome is bundled. So every Rome row gets one of 4 city images, cycled by a hash
of the venue *name*. A gelateria, a wine bar and a nightclub are visually
identical. This is the single biggest reason the list reads as a placeholder
screen.

The `imageClassFor*` fix committed on 2026-07-31 (`615f7cdd`) is therefore
**dead code for every bundled city**. It is still correct for unbundled cities;
it just does not do what the commit implied it would.

**Also a real bug at the same call site:** `placeVariantSeeded(name, venueType)`
passes `venue_type` into a parameter declared as `entityType`. The function's
`entityType === 'site'` branch can therefore never fire from `PhotoThumb`, so a
site can never get the `site` (heritage/cultural) variant.

**Change:** decide the precedence deliberately. A confident category match
(`museum`, `bar`, `cafe`) is more informative than generic city art and should
win; generic city art is the right fallback for a place we cannot classify —
i.e. roughly the inverse of today. Then fix the argument bug so sites can reach
the `site` variant at all.

## T5 — Remove the debug affordance and fix bottom clearance

- A floating **"D"** bubble is shipping in the UI.
- The floating tab bar **overlaps content** — "Garbatella / Jewish Ghetto /
  Monti" and "Enoteca Ferrara" are cut through. The scroll container needs the
  tab-bar clearance the other roots already apply.

## T6 — Re-geocode the 2,289 placeholder venues (the slow one)

Deliberately last: it is the only item here that cannot ship in a day, and T1
makes the surface honest *without* it.

**Constraint:** name + city is the only available key (no external_id, no
wikidata_id, no address column). `scripts/geocode_places.py` exists but handles
the `places` table, not `venues` — it is a reference for the Nominatim client
and rate-limiting, not a script to reuse directly.

**Open questions to settle before building:**
1. Geocode by name+city, or re-import these venues from OSM/Overpass (the
   `seed_venues` path) which carries real coordinates *and* a re-resolvable
   `external_id`? The second is more work but fixes provenance permanently.
2. What happens to a venue that cannot be resolved? It must keep an honest
   "location unknown" state, not silently revert to the centroid.
3. Should `sites` (1,542 affected, same 52%) be fixed in the same pass? Same
   root cause, likely the same import.
4. Is `cursor_import` still running anywhere? If it is, this refills as fast as
   it is drained — that must be answered before backfilling anything.

---

## Suggested order

**Ship first (days, mostly small):** T1, T2, T3 — every one removes a false
statement from the screen.
**Then (a design call inside it):** T4 — needs a deliberate precedence ruling.
**Cleanup, any time:** T5.
**Then, its own project:** T6.

**Only after that:** re-open the §14 sectioned-browse adjudication, and any
redesign conversation, against a Places tab that is telling the truth.
