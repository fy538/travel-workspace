---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-09-03
last_verified: 2026-09-03
expires: 2026-10-03
why_new: Preserves the object-page design handoff and its unresolved engineering decisions without promoting design fixtures into canonical runtime authority.
source_of_truth_for: []
supersedes: []
---

# Object Page Rebuild — Implementation Handoff (2026-09-03, rev 3)

**Status:** design handoff from the Claude Design project *Vesper — Entity Object Handoff Lab* (`dd48304b`), boards 01–14. Rev 3: **board 14 is the page** (founder, 2026-09-03: "probably the best we have so far"); §2 is rewritten to it. Rev 2's rulings (§0) still hold. The entity-resolution brief's Part I rules (identity, privacy, source use, no Take on open) stay locked. Non-canonical until diffed into canon.

## 0. Rulings of 2026-09-03 (founder, in chat)

1. **Seed identity, not opinion.** Seed lightweight canonical entities broadly — name, kind, coordinates, address, provider ids — from open datasets (Foursquare OS Places, Overture, OpenStreetMap; never Google). "No backfill" in the brief was a fence around one engineering slice, not product law. The named cost is dedupe: two sources for one place must become one `EntityRef` before pins can land on it.
2. **Web search on demand, never on the read path.** Opening a page queues research for that one place (the person acted, so this is not backfill). The result lands seconds to a minute later as a persisted, sourced brief with an as-of, cached for everyone, refreshed on a TTL. It describes; it does not judge. The provider-only row becomes the long tail; the brief's three destinations collapse to **known / matched / made**.
3. **The interpretation is a composition.** One paragraph block in Vesper's voice built from: the cached web brief (LLM); Vesper's dossier or angle when one touches the place (governed, optional input; the only source of a verdict); and *today* (deterministic, per viewer, no model): open-until with source and as-of, your keep and line, friends' lines by grant, whether it is in tonight's Occasion. **Cite, never absorb:** friends' words appear verbatim, attributed; today-facts and quotes are injected by code, not generated. No inferred taste, ever. This retires the stored-Take-per-(entity, mode) model and its mode-key defect.
4. **The plate, square, and one blob.** Adopt board 03's plate with the riso illustration full-bleed at the top and **square corners**. No sections: the page is the plate, the name, **one readable body of generated text split into short paragraphs**, a strip of faces for who has been, the verbs as text, the metadata rows, stop. Sections were "too messy"; board 08 (restyled sections) was rejected, board 09/10 (the blob) accepted.
5. **No "Add to trip".** The trip picker / day picker / review sheet is the travel-app grammar and does not belong on the object page. Verbs: **Keep** (top bar; a kept place is the pin) · **Ask Vesper** (Chat) · **Leave for someone** (the directed act; the dark addressed-handoff) · **Tonight?** only while an Occasion is live on Home. No primary button. The in-plan state becomes a sentence in the body ("it's in tonight"), not a strip.
6. **Citations inline, mixed.** The body cites the way a good answer does: small inline markers after the sentence they support, mixing web sources and people — `[1] [2]` for the web, a face for a friend, an umber face for you — with a sources line under the body listing them. A marker opens its source (the page, or the friend's line verbatim with its grant).

## 1. What is being replaced

Three implementations of one object: the bespoke venue route (18 render units, 4 action ladders), `EntityObjectPage` (site only; no verbs, no hours), `ExperienceDetail` (rail last, no status, no not-found). Accommodation stays outside by decision. The rebuild is one page component for venue · site · experience · neighbourhood-as-entity · spot, with the container page sharing chrome and carrying the map as its hero.

## 2. The page (board 14) — the spec

```
plate        your kept photo if you have one → a permitted provider photo → the riso illustration; full-bleed, square corners
top bar      back · Keep (bookmark) · share  (share absent on an owner-private shell)
kicker       CUISINE/KIND · TOWN   (town is the door to the container page)
name         System Sans 600 24/27
byline       faces of who has been (people ink, you umber) + one label, e.g. "Dana and you have been here"; absent when no one
the pair     the two most relevant facts, two columns over one hairline: value 17–18px, mono label, mono source line with as-of
body         2–4 line paragraphs at 16.5/24 serif, one thing each; inline citations: numbers = web sources, faces = people; friends' words verbatim in italics; the last paragraph is the only uncited one
sources      the numbered list + the people cited (may fold to one line)
verbs        text: [Tonight? · only while an Occasion is live] Ask Vesper · Leave for someone
the rest     one two-column row of the demoted facts (PRICE · TABLE with a Reserve link when real; HOURS; ACCESS when known)
where        address · map snippet (96px thumb beside the address on the entity page; full-width strip on the container page) · Directions → provider surface
end          paper
```

**Dynamic facts.** Facts are one ranked list, not fixed slots. The pair takes the two most relevant to the situation; the closing row takes the rest; nulls are demoted as honest unknowns ("not checked" + the live check; "unknown") or dropped; a null never occupies the pair. Ranking is a table on three signals the page already has — near the place (explicit one-shot location), open now / evening, Occasion live — with no model in the loop:

| Fact | Arriving (here, evening) | Planning (elsewhere) | Null |
|---|---|---|---|
| Open until | pair | below, as the week's hours | below: not checked + live check |
| From you | pair | below, from the town's anchor | absent |
| Price | below | pair | below: unknown |
| Table | below (+link) | pair (+link) | absent |
| Where | closing row | closing row | pair when little else is known |
| Access | below when known | below when known | absent |

**Rules that survive from the law (board 02):** each input has one owner; absent stays absent; nothing generated on the read path; the sparse page ends above the fold; removing one input removes exactly its sentences and its marker. Today-facts and quotes are injected verbatim by code, never by the model; markers are attached by the code that placed the sentence.

**Rejected on the way here (kept as record):** board 08 (restyled sections), board 13's refinements (the founder preferred board 12's variant 2 as the base), the map strip on the entity page, "Add to trip".

## 3. Inputs → wire

| Input | Reads | Change needed |
|---|---|---|
| Identity | `entity.name`, `ref`, `lineage`, `categories` / `venue_type` | render city when neighbourhood absent; "also listed as …" provenance line for a matched candidate |
| Web brief | **new**: `research_brief {text, sources[{title,url,retrieved_at}], generated_at, ttl}` per entity, shared | research job queued on open; cached; exposed on the entity envelope |
| Dossier / angle | existing governed pipeline, `place_slug` link | optional input to composition; the only permitted source of a verdict |
| Today | `status {operating, open_now, hours, as_of, sources}`, `relationship {saved, encounters, active_trip}`, your line, **people_lines[]**, tonight's Occasion | deterministic template, per viewer; unify `status.hours` / `tail.hours` |
| People | **new**: `people_lines[] {author, grant_kind, precision, made_at, text, photo?, thread_ref?, used_in?}` resolved viewer-relative server-side (audience, block, precision) | needed before any friend appears; withdrawal recompiles the body |
| Metadata rows | `status` + venue tail `cuisine_type, price_range, price_per_person_estimate, avg_duration_minutes, reservation_required` + `presentation.facts[]` with `source_mode / observed_at` | render with provenance; stop dropping it at the mapper |
| Verbs | Occasion-live flag from Home; Chat seed; addressed-handoff create | remove itinerary ladders from the page |

## 4. Components

**Keep:** `ObjectPageShell` chrome (plate geometry now square), `SpotTopBar` (Save/Keep = reference verb; share constrained on owner-private), `ObjectPageStateShell`, `StayLocationMap` with `mapSurface` (for the instrument top), the title register (`objectTitle` sans 600 24/27), `PlaceShareOwnerSheet`.

**New:** `ObjectBody` (paragraphs + inline citation markers + sources) · `PresenceByline` · `FactPair` + `FactRanker` (the table above) · `ClosingRow` · `WhereRow` (address + snippet + directions handoff) · `InstrumentTop` (sparse hero fallback) · `CandidateResolvingRow` · `OriginStopCard` (retryable / honest) · `SpotPage` admission · `ProvenanceLine` · the research job + cache · plate source resolver (your photo → permitted photo → illustration).

**Delete from the page:** `SpotPlanningRail` and the trip/day/review ladder, `ItineraryStopStrip`, `WhyForYouCallout` and its route param, `OrderSkip`, the `Details` drawer, `WorldSection`, `AskVesperBlock` disc, `SpotTake` (streaming personal Take), the one-photo scroller, `CatalogEvidenceDisclosure` from the ordinary path, `EntityInterpretationBlock` (unwired; superseded by the composition).

## 5. Sequence

0. One page component; square plate; metadata rows with NOW first and provenance; text verbs. Zero new data. (Fixes buried hours, unrendered price/cuisine, three block orders.)
1. Lightweight identity seed for one city + dedupe rule; candidate paths collapse to known / matched / made.
2. Research job on open → `research_brief` cached; `ObjectBody` renders web + today (template) with inline markers; sparse page = three sentences.
3. Dossier as optional input; verdict only from it.
4. `people_lines` API behind grants; faces in the strip; friends cited inline; the mark-opened sheet.
5. Spot admission (person-made places) and owner-shell promotion.
6. Live-details check; share contract for owner-private; `map_surface` on the wire.

## 6. Open questions for engineering

- Dedupe/conflation across seed sources (Overture ids as the spine?).
- Research job cost/TTL; what "sources" may be shown for a given provider's terms.
- Temporary vs non-retryable taxonomy on `POST /api/me/entity-resolutions`.
- Owner-private shell promotion when a second person reaches the same external ref or a grant touches it.
- Whether a kept place and a pin are one record or two.
- The Occasion-live signal the page reads for "Tonight?".

## 7. Fixtures and boards

Hortus (real dinner; body, hours, prices fixture) · Café Aurora (brief fixture B) · Aurora Bar / Bar Aurora (C) · Museu do Azulejo (A) · Harbor Textile Archive (E) · Sorrento (container) · "The stairs at Marina Grande" (spot). Boards: 01 audit · 02 law · 03 languages · 04 kinds · 05 people slot · 06 five paths · 08 plate simplified (rejected) · 09 the blob · 10 typeset · 11 element order · 12 the pair · 13 refined (base not adopted) · **14 where + dynamic facts (the page)**. Raw code inventory: `social-aperture-generators/object-page-audit-raw.md`.
