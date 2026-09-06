---
doc_type: working
status: active
owner: founder / Life design
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Deliverable of the 09-06 "Life over time" follow-up (02-life-anchors.md §September 6): four connected walkthrough boards, their implementation notes, the release/deletion reconciliation, and the decision/delta list.
depends_on:
  - claude-design-integration-2026-09-04/02-life-anchors.md
  - life-organization-and-composition-engine-system-design-2026-09-05.md
  - life-unfolding-decision-docket-2026-09-04.md
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-09-05-adopt-the-plan-in-seven-sentences.md
supersedes: []
---

# Life Over Time — Walkthroughs and Deltas (2026-09-06 pass)

Design project **Vesper — Life & Anchors** (`f524c7f0`). New boards **35–39**;
amended boards **31** (release wording), **32** (frame C, gap 3), **00A**
(labeled 30–39 arc section, verified date). Status of all walkthrough
behavior — EXPERIENCE: fixture-composed, pending founder review. BUILD:
unimplemented (the org-engine design's U1/U2 receipts are the engineering
state of record).

## The four walkthroughs

| Board | Covers |
| --- | --- |
| **35 · A Week That Gains Its Past** | Gap 1 (highest) + gap 5. Late Sorrento photos land by capture time in the coast segment; the current NYC week doesn't move; a fragment joins Sunday's episode as a count, not a reorder; an undated article rests unplaced for months and is then simply used; originals stay available while enrichment settles (one voice-register fact line — no meter, no inbox). |
| **36 · Two Dinners, One Sentence** | Gap 2. "These were two different dinners" → split + receipt + Undo; old links resolve through a bounded resolution entry ("This evening is now two"); "keep this photo, but…" → detach with a durable anti-rejoin memory; "call this our summer cooking experiments" → a YOURS-stamped title that survives enrichment; frame 7 draws the three untouchables (arrangement, original, audience). |
| **37 · Lilia, Before the First Visit** | Gaps 3 + 4. The pre-visit relationship shows the material that exists (note, keep, arrangement) with "0 visits" exactly true; the five primary-destination defaults in ordinary use; Back restores query + lens + position; secondary doors wear ordinary names; the visit enriches the same page rather than replacing a placeholder. |
| **38 · The Saved Piece and the Living Record** | Gap 6. New material enriches the record and only *offers* the piece a distinct V2 (explicit refresh door); a factual correction marks the affected generated clause with date, never rewriting the person's caption; a withdrawn photo goes legibly absent inside the frozen version; "Make my version" sketched in one later-phase frame, explicitly not a shipping prerequisite. |

## Implementation notes (beside the design, not customer copy)

### W1 (board 35)
- **Stable identity:** journey handle (owner-derived); week period IDs (calendar+tz policy); episode row identities; article source handle. None derives from labels or member sets (D5).
- **Changed relationships:** coast-segment membership +14 (capture-time basis); Sunday episode +1; article — custody only, no organization.
- **Update behavior:** silent, additive, scoped to the historical groups the material belongs to (§7.3); counts and factual descriptions change; rows, titles, order, reader anchor do not. Contextual explanation owed only where a change would confuse — nowhere here.
- **Human choices that survive:** reading position; the choice not to organize the article.
- **Navigation anchor:** row identity + existing reading-position storage.
- **Owner boundary:** source custody = intake/core owners; capture-time truth = source metadata; Life owns derived membership and the coverage line. Unresolved: none.

### W2 (board 36)
- **Stable identity:** the pre-split evening ID persists as a resolution entry with recorded aliases (§6.4); descendants get registry identities; the canonical-anchored descendant (the Mirage show) keeps primacy.
- **Changed relationships:** memberships repartitioned per-item by their own basis; one rejected membership persisted (anti-rejoin); one rename persisted as a durable control (LifeControl shape).
- **Update behavior:** each sentence = one owner-scoped command + readback + valid-inverse Undo; enrichment reads controls before proposing (§6.2 step 3).
- **Human choices that survive:** split, detach + anti-rejoin, YOURS-stamped title — durable inputs to every rebuild; raw sources cannot recreate them.
- **Navigation anchor:** old deep links resolve via the resolution entry; citing compositions render the disambiguation, never a dead door.
- **Owner boundary:** Occasion/participation/audience owners untouched by all four commands. Unresolved: none.

### W3 (board 37)
- **Stable identity:** the place relation is keyed to the canonical Place handle (Entity lab owns resolution); the relation page's identity precedes any occurrence.
- **Changed relationships:** pre-visit — note (audience-governed) + arrangement ref; post-visit — +1 occurrence, note re-labeled taken-up, nothing removed.
- **Update behavior:** the visit appends; earlier entries quiet to 62%; note withdrawal would recompile per board 33 F5 without touching the occurrence.
- **Human choices that survive:** the keep; the non-attribution of Maya to Alex (audience lane); any later rename.
- **Navigation anchor:** the primary-destination defaults (board 39 table); Back = query + lens + position.
- **Owner boundary:** entity page = Entity lab; arrangement page = Plan lane in the seven-sentences register (a page you read; change by saying it). Life owns the relation page and its doors only.

### W4 (board 38)
- **Stable identity:** composition handle + immutable version handles (V1; V2 with `based_on` lineage); stable block IDs across versions (§9.3).
- **Changed relationships:** record side +14 memberships; piece side none until an explicit refresh; correction adds a validity annotation to one dependent claim; withdrawal invalidates one media dependency.
- **Update behavior:** the three revision clocks stay distinct (D7): record enriches, synthesis annotates, human composition is never touched. Refresh = offered scoped diff, explicit only.
- **Human choices that survive:** caption wording and selection (protected fields); the choice to keep V1 as-is; exclusions in any V2.
- **Navigation anchor:** the piece reopens at its version identity; corrected/absent blocks keep their IDs so positions hold.
- **Owner boundary:** saved-composition custody owner is the org-engine §13 / R7 open choice — the walkthrough constrains behavior without selecting storage. Occurrence correction = claim owner; media grant = audience owner. **Unresolved, reported not invented:** that custody owner.

## Release vs deletion, reconciled (board 39)

RELEASE always means: *stops being held as live; the ledger remembers
honestly.* Contextual one-line readbacks carry the difference:

- Intention: "Released — it leaves Time and search; the ledger keeps that you
  let it go." (Board 31 amended to match.)
- Source: "Released — Vesper no longer holds the original; its line stays in
  the ledger." (10-family behavior, unchanged.)

DELETE remains the separate custody verb with the Vault's honest-deletion
readback. No lifecycle settings screen exists; the word is explained where it
acts.

## Decision / delta list

**Changed this pass:** boards 35–39 added; board 31 release receipt reworded;
board 32 frame C replaced (gap 3); board 00A gained the labeled 30–39 arc
section and a 09-06 verified date. No ruling was adjudicated; every pending
ruling stays pending.

**Would change if the walkthrough laws land:**
- `docs/contracts/life-v1-experience.md` — the split-resolution law (old
  handles resolve, never dead-end), detach's anti-rejoin durability, the
  saved-piece correction treatment (contextualize, never rewrite), the release
  readback shape, and the pre-visit-relationship rendering rule.
- `life-unfolding-decision-docket-2026-09-04.md` — its release wording is
  superseded by this reconciliation; D7 (25/26 regeneration) and D8 (dark-chip
  scale) remain open there.
- The org-engine design needed **no change**: the walkthroughs consumed
  §6.4, §7.3, §9.1–9.3 and D2–D7 as written, with no conflict found.

**Deliberately unresolved (reported, not settled):** the kept-intention owner
(Plan/Occasion lane; the seven-sentences decision does not resolve it), the
saved-composition custody owner (R7), and rulings R1–R6 of the 09-04 docket.

**Honored:** no new setup, filing step, reflection prompt, or review
obligation anywhere in 35–38; arrangement touchpoints stay in the
seven-sentences register; no Round-3 coordination mechanisms imported; board
05 untouched; no production change.
