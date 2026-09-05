# Entity Objects — lane response (2026-09-04)

**Brief:** `05-entity-objects.md`. **Project:** *Vesper — Entity Object Handoff Lab* (`dd48304b`; the Downloads export is a 09-04 13:30 snapshot of it). **Status:** design deliverables complete in the project as boards 09–13; boards 05, 06, 06B and the two workspace docs corrected for the research trigger. No production code, seeding, research, permission or entity-kind change was made or is authorised by this response.

## Active-board map

| Board | Role | Status |
|---|---|---|
| 00 Read Me | map | updated |
| 01 Audit · 02 Law · 03 Kinds · 04 People slot · 05 Five paths · 06 The Page · 06B Arrival + large text | the page and its rules | current (05/06/06B corrected: explicit Read up) |
| 07 Handoff (rev 3.1) · 08 Build brief | engineering mirrors | corrected: research trigger |
| **09 One place, five doors** | WP A | new |
| **10 Intent beyond Tonight** | WP B | new |
| **11 Places and Life** | WP C | new |
| **12 Useful edges** | WP D | new |
| **13 Status and deltas** | evidence ledger + decision log | new |
| Z1–Z5 | archive | not directions |

## Research trigger — resolved from current evidence

The lab's earlier boards said opening a page queued research. Local main (09-04) and the roadmap's Phase 0 ruling say otherwise: a base read never enqueues, calls a provider or spends; research runs only on an explicit **Read up** (`POST …/research-requests`, idempotent, flag `ENTITY_RESEARCH_REQUESTS_ENABLED`), with queued / failed / stale states. Boards 05, 06, 06B, the handoff doc §0.2/§3/§5 and the build brief T8/T9/§4/§7/§9 are corrected to this. Automatic research is not restored.

## Compact context matrix (WP A)

| Origin | Context changes | Never changes | Back returns to | Opening implies |
|---|---|---|---|---|
| Home possibility | one context line; pair ranks for now; Tonight? present iff an Occasion is live | identity, plate, facts, body, sources, people | the Home composition, same scroll | nothing |
| Places map sheet | pair uses the explicit one-shot position | same | the sheet at the same detent | nothing |
| Friend's addressed note (Chat) | context line names the note; sheet not pre-opened; nothing marked read | same | the thread | nothing |
| Life kept material | relationship line first; pair ranks for planning | same | the drawer, same scroll | nothing |
| Arrangement where it is an option | context line names the arrangement and its standing; first verb = the arrangement's question | same | the arrangement | nothing |

## Proposed verbs and navigation (WP B, D)

- Verbs on the page: **Keep** (top bar) · **Ask Vesper** · **Leave for someone** · **Read up** (sparse, flag) · the arrangement's question (e.g. "Saturday?") as first verb only while an arrangement is in context; **Tonight?** only while an Occasion is live (design-only; no route passes it today). No Add-to-trip ladder.
- Intent without ceremony: (1) Keep = T1 receipt with optional when-chips (no date / sometime / Saturday); (2) "keep loosely for Saturday" = the same receipt with one chip — an intention without a named Plan, **labelled proposal, owned by Components & Plan**; (3) "would this work for Maya's dinner?" = Ask; the answer offers one bounded "consider it for …" preview (T2, affects others), and asks which of two relevant arrangements only when the choice changes who sees it.
- Cross-root doors: the page's "Your history here" → Life; Life's "Open the place" → the page; each returns to where it was tapped. Directions and Reserve leave Vesper with an interstitial that says Vesper does not navigate / book / hold / pay; returning changes nothing; a forwarded confirmation belongs to the arrangement and is projected on the page with its source.
- Face-opened sheet: keep the place (bookmark, T1) · keep her words (permitted private copy under her grant, T1; she is not told) · send onward (addressed handoff, T2). Never one button.

## Reused components

`ObjectPageRebuild`, `objectPageProjection` (ranker, body), `EntityLocationMap` + `display_policy.map_surface`, `RelationshipPlaceNoteAction` (Leave for someone), `ConversationSeed` (Ask), people byline + sheet (board 04), the relationship readback (470b8af10), `PlaceShareOwnerSheet` (unchanged).

## Changed data needs

A viewer context that can carry an origin and an arrangement standing (client-assembled); an Occasion-live signal (owner: Home); a "keep her words" act and receipt (grant contract has the axes); a confirmation projection read from the arrangement/source owner; the when-chip on Keep only if Components & Plan adopts the intention proposal. No new entity kinds; the address stays off until an owned catalog field exists.

## Status (refreshed against local main 09-04)

Implemented behind flags: one page for venue/site/experience; photo-or-nothing plate; ranker; body + markers from `paragraph_sources`; read-only brief + explicit Read up; people byline; relationship line + readback; situation summary; Ask; Leave-for-someone doorway; where row; large-text stacking. Design-only: Tonight?, context line, arrangement-first verb, "consider it" preview, when-chips, Life door labels, interstitials, confirmation projection, face-sheet acts. Unresolved (owners named on board 13): intention storage, Occasion-live signal, keep-her-words act, confirmation owner, spot admission, shell promotion, photo endpoint beyond venues.

## Unresolved cross-lane assumptions

1. Life lane: the door labels ("Your history here" / "Open the place") and whether Life's relationship view is a lens or a page.
2. Components & Plan: whether a loosely dated intention is stored at all, and what the arrangement's "option" standing is called.
3. Home lane: the Occasion-live signal the page reads for Tonight?.
4. Interaction lane: the confirmation-forwarding path that produces the projection on board 12.
