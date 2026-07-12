---
doc_type: working
status: active
owner: frontend / backend / design
created: 2026-07-11
expires: 2026-08-10
why_new: Coordinate the Deck's frontend, backend, fallback, and dogfood-data rollout.
supersedes: []
---

# The Vesper Deck — Full-Stack Plan (frontend · backend · fallback · dogfood data)

**Status:** ready to execute · **Created:** 2026-07-11 · **Scope:** the "Vesper Home Deck" end-to-end across both repos + seed data. Design canon is settled (this is a build/data plan, not a design pass).

> **Read §0–§2 before touching anything.** They are self-contained: a fresh agent (frontend, backend, or data) gets the full architecture, the current-state map, and the root causes here, with file:line anchors into both repos. §3 is the phased work. §4 is "definition of done."

---

## 0. What the Deck is and how it works today (self-contained architecture)

The **Deck** is the dark "N TO CLEAR" modal that opens from Vesper Home when you tap a card. It is a stack of **decision cards** you triage one at a time (Pick a restaurant, settle a debt, break a vote tie, confirm a held booking). Canon calls each card shape a **face**.

### 0.1 The end-to-end data path
```
[dogfood seed / real DB]                         travel-agent
   venues, saves, expenses, proposals, bookings
        │
        ▼
  GET /api/concierge/home   backend/api/routes/concierge_home.py:229
        │  assemble_concierge_home_feed()  backend/home/concierge_feed/producers.py:121
        │    ├─ 7 producer groups → candidate cards (each a kind, e.g. saved_cluster, near_you, settle…)
        │    ├─ face builders  backend/home/deck_payloads.py  (attach focus/structured IF substrate is rich enough)
        │    ├─ Pick judgment (grounded Haiku)  backend/home/pick_judgment.py   ← the only generated take line
        │    ├─ rank + twin-suppress  backend/home/concierge_feed/ranking.py
        │    └─ slot: hero → now_card, next 4 → next_moves
        ▼
  ConciergeHomeFeed { now_card, next_moves[], voice_register, lead_note }   models.py:407
        │
        ▼                                          travel-app
  useConciergeHomeFeed()  data/conciergeHome.ts:60
  mapBackendCard()  app/(tabs)/concierge/index.tsx:1033   ← parses focus/structured into the card
        │
        ▼
  Deck.tsx  (dispatch by face)  ─────────────────────────────┐
    focus.layout==='pick'    → DeckPickFace.tsx               │
    focus.layout==='call'    → DeckCallFace.tsx (held/conflict/reschedule)
    focus.layout==='brief'   → DeckBriefFace.tsx              │  run-through:
    focus.layout==='compare' → DeckCompareFace.tsx  (FE only) │  utils/deckRunthrough.ts
    structured.layout==='vote|settle|readiness|flight' → DeckStructuredFace.tsx
    neither                  → HeroCardFace → CardLive/CardSignal/… (glance fidelity — the FALLBACK)
```

### 0.2 The four layers (your four pillars)
- **Frontend** — `travel-app/components/focus-home/` (Deck.tsx, DeckPickFace, DeckCallFace, DeckBriefFace, DeckStructuredFace, FocusHome.tsx), dispatch + run-through. Consumes the feed via `data/conciergeHome.ts`.
- **Backend** — `travel-agent/backend/home/` (producers, deck_payloads, pick_judgment, ranking) + route `backend/api/routes/concierge_home.py`. Produces the cards and attaches faces.
- **Fallback** — two independent layers: (a) **backend** fail-open — `degraded_home_feed()` + `_starter_cards()` + per-producer best-effort + LLM fail-open (never 500s, always returns a body); (b) **frontend** local templates — `hooks/useConciergeHomeState.ts` builds prose cards when the backend feed is empty. **Key fact:** FE local template cards **never** carry `focus`/`structured`, so they can only ever render a glance/prose card, never a rich Deck face.
- **Dogfood data** — `travel-agent/tools/dogfood/content/` (manifests/*.yaml, scenarios.yaml, corpus_governance.py) seeds each persona's world; `travel-app/constants/personas/*.ts` are the FE mock worlds (a parallel, richer set — see §2.4).

### 0.3 Design canon (settled — build to it)
**Canon bundle: `~/Downloads/vesper 146/project/`** (a user-local path — if missing, ask the user for the latest `vesper NNN`; always use the highest number). Canvas-mode HTML → **open the named `.jsx`, not the `.html`** (the `.html` page is empty; content is in the JSX in its `<script src="…jsx">`). The Deck lives in:
- `vesper-home-deck.jsx` — **all faces**, incl. (as of vesper 146) the currency-aware Pick gauge and the new `DeckNearYou` ambient face.
- `deck-readiness-taxonomy.jsx` — the FocusState-kind → face mapping.
- `vesper-deck-entry.jsx` — the rail entry (`DeckEntryRail`).
- `Vesper Canon Consolidation & Ownership.html` → `vesper-canon-consolidation-app.jsx` **§03b "Deck Content Contract"** — the per-face render contract (min substrate, field provenance, take line, currency, suppress-when-thin) added in vesper 146. **This is the spec every face is held to — read it first.**

The **canonical face set** (each = one decision shape with a strong Vesper take line + specific in-card verbs): Pick · Call (held/conflict/reschedule) · Brief · Vote · Settle · Readiness · Comparison · Flight · **Near-You** (new in 146). Reference contract (Pick, `vesper-home-deck.jsx`): kicker (trip+timing) · meta ("DECIDE SOON") · take ("Kikunoi's the one to book first.") · hero option {name, "I LEAN", currency-aware price tier, facets, *why*} · shortlist rows {name, facets, tier, *why-not* — sheds at ≥4} · synthesis line · actions.

### 0.4 Ground rules for execution (read before writing code)
1. **Two repos, both under `~/travel-workspace/`:** `travel-app/` (Expo client) and `travel-agent/` (Python backend), independent git repos. Work in whichever the item's tag points to.
2. **Branch per phase** — don't work on `main`. One branch per phase (e.g. `deck/d1-currency`). Keep phases landable independently.
3. **Verify before editing** — every `file:line` here is from a 2026-07-11 read; code moves. Open the file, confirm the thing still exists, then change it. If reality contradicts this doc, trust the code and note the drift.
4. **Atlas is out of scope** — don't touch `app/atlas/*`, `components/atlas/*`, `travel-agent`'s atlas surfaces.
5. **How to see the deck** (verify steps assume this): run the app (`make dev` from `~/travel-workspace`, or the app's run tooling / the `/run` skill), switch to a dogfood persona via the in-app dev persona switcher (`travel-app/app/dev/persona-switcher.tsx`, deep-link `guide://dev/persona-switcher`), open the Vesper (concierge) tab → tap a home card to open the deck. Backend: `make dev-backend`; dogfood seed targets live in `~/travel-workspace/dogfood.mk` (see `make dogfood-status`).
6. **Gates before landing:** `make typecheck` + `make test-frontend` / `make test-backend` from `~/travel-workspace`; run the `/verify` skill to exercise the actual flow (not just tests); run `/code-review` after each phase — AI UI code duplicates/drifts and a reviewer pass catches it.
7. **Tags:** **[FE]** travel-app · **[BE]** travel-agent · **[DATA]** dogfood seed · **[DESIGN]** design canon (all deck design is DONE in vesper 146 — no open design items remain; these tags now mean "build to the canon board named").

---

## 1. Current state — the truthful map

Every canon face **has a frontend component**. The gaps are in what feeds them. This table is the heart of the plan:

| Face | Canon | FE face built? | Backend emits it? | Content source | Take line? | Status |
|---|---|---|---|---|---|---|
| **Pick** | yes | ✅ DeckPickFace | ✅ `focus=pick` (saved_cluster, near_you ≥2 venues) | **real** `venues.name` from DB | ✅ grounded Haiku (`pick_judgment.py`) | **WIRED** — best-developed face |
| **Call** held/conflict/reschedule | yes | ✅ DeckCallFace (3 variants) | ✅ `focus=call` (booking hold, constraint, the Catch) | real booking/proposal data | ⚠️ templated `stakes` | **WIRED**, no generated voice |
| **Brief** | yes | ✅ DeckBriefFace | ✅ `focus=brief` (drafted day themes) | real itinerary themes | ⚠️ templated | **WIRED**, no generated voice |
| **Vote** | yes | ✅ DeckStructuredFace | ✅ `structured=vote` (open proposals) | real proposal/votes | ❌ none | **WIRED**, no voice, thin seed (§2.4) |
| **Settle** | yes | ✅ DeckStructuredFace | ✅ `structured=settle` | real creditor+**currency** | ❌ **no take-line field at all** | **WIRED but thinnest** (§2.1) |
| **Readiness** | yes | ✅ DeckStructuredFace | ✅ `structured=readiness` (≤7d + open) | real gap counts | ❌ templated | **WIRED**, suppressed on all-clear |
| **Comparison** | yes | ✅ DeckCompareFace | ❌ **never emits `compare`** | — | — | **ORPHAN** — parked in canon 146 §03b (awaiting BE producer) |
| **Flight** | yes | ✅ DeckStructuredFace | ❌ **never emits `flight`** | (only a readiness row) | — | **ORPHAN** — parked in canon 146 §03b (awaiting BE producer) |
| **near_you / "right now"** | ✅ **DeckNearYou (new, canon 146)** | ✗ (still borrows `CardLive` glance) | ✅ `near_you` (focus=pick if ≥2 venues, else prose) | real venues, or nothing outside seeded cities | canon has one now | **FACE DRAWN, NOT BUILT** (§2.3, D4) |

**Run-through:** built (`utils/deckRunthrough.ts`, `advanceDeckAfter` at `FocusHome.tsx:230`) — cards advance; only the primary CTA + Ask Vesper close the deck. The "N TO CLEAR" counter is honest. *(This corrects an earlier audit that said run-through was missing.)*

---

## 2. Root causes (why the shipped deck reads underbaked)

The deck's **structure is sound and correctly wired to real data**. Four things make it look thin, root-caused across the stack:

### 2.1 The content contract is incomplete — only Pick gets a generated voice
Only `focus=pick` cards get a grounded take line (`pick_judgment.py`). **Settle has no take-line field in its backend model at all** (`DeckStructured`, `vesper_cards.py:62`) and `DeckSettleFace` never renders `card.body` — so it's structurally the flattest ("2 shares still open" with no Vesper read). Call/Brief/Vote/Readiness carry only templated `stakes`/copy. Canon gives every face a voice; the stack gives it to one.

### 2.2 Currency: the ¥ gauge is a hardcoded FE glyph, not currency
`DeckPickFace.tsx:46` renders the `¥` character in a fixed 1–5 gauge **regardless of city** (docstring: "a fixed 1-5 ¥ gauge … not a live number"). The backend `DeckPickCandidate` model has **no currency field** — just a price-symbol string + integer tier (`vesper_cards.py:79`). Rome seed stores **EUR** throughout; the ¥ is injected purely by the FE. (Settle *is* currency-correct — `deck_payloads.py:465` maps EUR→€.) Canon's own gauge uses ¥ **because its example is Kyoto** — so "is the tier gauge currency-aware or a neutral mark?" is a genuine open design question, not just a bug.

### 2.3 Two faces are orphaned; one card kind has no face
- **Compare** and **Flight** faces exist in FE but the backend never emits those layouts (the literals don't exist in `vesper_cards.py`). FE has UI the backend can't drive.
- **near_you** ("What fits near Jersey City") has no dedicated deck face — when it can't form a Pick (< 2 venues) it falls through to `CardLive`, a *one-line glance card* blown up full-screen, so it reads ~90% empty. Outside the ~40 seeded corpus cities near_you has **no venues at all** and can only offer to open a chat (Jersey City = the dev's real GPS, zero seeded venues nearby).

### 2.4 The dogfood seed is QA-scaffolding, and there are two parallel worlds
The shipped deck is **elif@dogfood.local / `elif-rome` pack**. Findings:
- **"Da Enzo-Style Warm Trattoria" is deliberate, not a bug.** `corpus_governance.py` rejects seed venues that name a real *bookable* place ("roscioli" fails; "roscioli-style-reservation" passes). The "-Style" names are governance-safe stand-ins, each bridged to a real editorial venue (`elif-rome-slug-bridge.yaml`). The Pick face reads `venues.name` straight through, so it shows the stand-in.
- **The FE mock (`constants/personas/elif.ts`) uses the REAL names + real €** (Roscioli €€€, Da Enzo al 29 €€) — but the mock world is never wired to the backend deck producer. So: **backend-seed world (governance-safe "-Style", the deck's actual source) vs FE-mock world (real names/€, unused by the deck).**
- The **"Sarah €60" settle** is real settlement *mechanics* on a `seeded_expense_demo` planning-*hold* row (a QA scaffold), not organic post-meal spend.
- **Real content is abundant** — 322 Rome venue dossiers exist (`content/staging/rome/`), 40 cities total. The constraint is seeding/governance, not data scarcity: real un-styled names *do* pass the gate (`flavio-al-velavevodetto`, `trapizzino-testaccio` are seeded in the same pack).

---

## 3. The plan

Tags: **[FE]** travel-app · **[BE]** travel-agent · **[DATA]** dogfood seed · **[DESIGN]** needs a canon board/ruling first. Each item names files and a verify step.

### Phase 0 — Decision gate — SETTLED 2026-07-11
The five rulings the rest of the plan depends on. All decided:
1. **Price gauge = currency-aware.** Localize the tier gauge to the venue's currency (€€€ Rome, ¥¥¥ Kyoto, $$$ NYC). No more fixed ¥. *(Drives D1. Canon DONE — vesper 146 `vesper-home-deck.jsx` `CUR_GLYPH` + per-candidate `cur`.)*
2. **Suppress-when-thin.** The deck shows **only decision-grade cards.** A card that can't form its rich face is **dropped**, not downgraded to a prose/glance card. Genuinely-empty state uses honest quiet cards ("Nothing needs you"), never a starved rich face. *(Drives D2, D4. Canon DONE — vesper 146 §03b rule.)*
3. **Take line on every face.** Extend the grounded take-line generator (today Pick-only) to every face, **Settle first**, then Call/Brief, then Vote/Readiness. NOTE: canon's Settle face *already* shows a take line (`DKTake` "Lisbon's settled, nearly…") — a code/backend build to match existing canon, **not** a canon gap. *(Drives D2.)*
4. **near_you gets a real ambient deck face.** *(Drives D4. Canon DONE — vesper 146 `DeckNearYou` in `vesper-home-deck.jsx`; it is NOT rail-only.)*
5. **Reseed ALL dogfood personas from real content.** Rewrite the dogfood seed so every persona's world uses **real venue names + real currency + decision-grade substrate** (real votes, real settles, real held bookings) — not just elif/mara. Seed saves/venues from the real editorial corpus (which passes governance because those venues are real, not fabricated booking claims); where a needed real name still trips `corpus_governance`, fix the rule for display-name use. *(Drives D5. Pure data — no canon.)*

### Phase D1 — Currency & gauge correctness *(small, high-visibility; do first)*
- **[BE]** Add a `currency` / `currency_symbol` field to `DeckPickCandidate` (`backend/core/models/vesper_cards.py:79`); populate from the venue's locale. Normalize `venues.price_range` (today a free `Text` column — "$$$" vs "mid-range" is inconsistent and `price_tier` returns None for word values) into a structured {tier, currency}.
- **[FE]** Make `PriceGauge` (`DeckPickFace.tsx:36–51`) **currency-aware** (decision 1) — render the tier gauge in the candidate's currency glyph from the new backend field; stop hardcoding `¥`. Fix the "Shape from saves" CTA truncation (`useConciergeHomeState.ts:809` value vs button width).
- **Verify:** open elif's Rome deck; the saved-places Pick shows €, and a Kyoto deck shows ¥ — never the wrong currency.

### Phase D2 — Complete the content contract *(the core work)*
- **Spec:** build every face to the **Deck Content Contract — canon 146 §03b** (`vesper-canon-consolidation-app.jsx`, the per-face table: min substrate · field provenance · take line · currency · suppress-when-thin). This is the contract; the [BE]/[FE] items below implement it.
- **[BE]** Extend the grounded-judgment layer beyond Pick: add take-line generators for **Settle** first (then Call/Brief, then Vote/Readiness), mirroring `pick_judgment.py` (schema-enforced Haiku, grounded strictly in real card data, fail-open to template). Register the new surfaces in `backend/core/surfaces/definitions.py`. *(Canon already shows the Settle voice line — no canon work, just build.)*
- **[BE]** Add a take-line field to `DeckStructured` (`vesper_cards.py:62`) so Settle/Vote/Readiness can carry a voice; have `DeckSettleFace` stop discarding `card.body`.
- **[FE]** Render the take line in `DeckStructuredFace` (`DeckSettleFace` at `DeckStructuredFace.tsx:195`).
- **[BE]** Implement **suppress-when-thin** (decision 2): add a card-level gate that **drops** `saved_cluster`/`near_you`/etc. when its face builder returns None (e.g. `build_pick_focus` at `deck_payloads.py:113`) rather than emitting a prose fallback. Keep the honest quiet-state cards only for a genuinely empty queue.
- **Verify:** the Settle card reads "You owe Sarah €60 — Rome's nearly settled" (voice), not a bare row; a thin saved-cluster produces **no card**, not a starved glance.

### Phase D3 — Orphaned faces: Compare & Flight *(wire or formally park)*
*(Canon 146 §03b already records both as "ORPHAN — canon-ready, awaiting a backend producer." This phase is the code side of that.)*
- **Comparison [BE/DATA]:** the FE `DeckCompareFace` is built but no backend emits `layout='compare'`. Wire a producer that emits Compare when there's a genuine two-option decision (e.g. two stay candidates in a vote) — needs the stay candidate/vote substrate to exist (§D5). If not prioritized, mark the FE face dormant with a comment so it doesn't read as a live-but-broken path.
- **Flight [BE][GATED]:** FE face + a readiness *row* exist; no `layout='flight'` producer. This needs flight schedule-change data (booking G2–G4, backend, currently gated dark). Either build the producer behind that gate or keep flight as a readiness row only. Tag and defer; don't leave it looking shippable.

### Phase D4 — The near_you / ambient deck face *(decision 4 = build a real face)*
- **Spec:** build to canon 146 `DeckNearYou` (`vesper-home-deck.jsx`) — real nearby venues + walk time + why-it-fits + grounded take line ("Ramiro's a 6-minute walk…"), near-you actions (Take me there / Save / Ask), suppress-when-thin (no card without ≥1 nearby venue).
- **[BE]** Give `near_you` its own face payload (not a borrowed Pick) carrying the ambient substrate (top nearby venues, walk distance, meal-window/weather fit, saved/loved boosts already computed in `ranking.py:589`). Add a take line per decision 3.
- **[FE]** Build the new face in `components/focus-home/` and dispatch it in `Deck.tsx` (today near_you falls to `CardLive` at `FocusHome.tsx:523`).
- **[DATA]** near_you is dead outside the ~40 corpus cities. Handled in D5 (reseed) — for dogfood, ensure each persona has seeded venues near their test location; per suppress-when-thin (decision 2), near_you with no venues produces **no card**.
- **Verify:** near_you in a seeded city renders the real ambient face; with no nearby venues it produces no card (not a starved glance).

### Phase D5 — Reseed ALL dogfood personas *(decision 5 — the fourth pillar)*
Rewrite the dogfood seed across **every** persona (elif, mara, dao, reza, mike, sarah, nadia — `tools/dogfood/content/manifests/*.yaml` + `scenarios.yaml`), not just elif/mara. Goal: every persona's deck is decision-grade from real data.
- **[DATA]** **Real venue names everywhere.** Seed each persona's `saves`/`venues` from the real editorial corpus (`content/staging/<city>/*.md` — Rome 322, Lisbon 333, Kyoto 582, etc.), so names are real (Da Enzo al 29, Roscioli) with **real currency** per city. Retire the "-Style" governance-safe stand-ins. Bring the backend seed up to the FE mocks' realism (`constants/personas/*.ts` already carry real names + currency). Where a needed real name still trips `corpus_governance.py`, **fix the rule** so real names are allowed for display (a saved-place name is not a booking claim) while fabricated bookable fixtures stay blocked.
- **[DATA]** **A real group Vote** per group world: seed a `change_proposal` with `alternative_options` + real member votes (mara's Lisbon is the primary; add one wherever a group trip exists) so the Vote face lights up with genuine tension.
- **[DATA]** **Realistic Settles:** replace `seeded_expense_demo` planning-holds with ≥1 organic post-activity expense per trip (a paid meal, uneven split) so settle cards read like real debt.
- **[DATA]** **A real held booking** on a live trip (reza's Rome-LIVE cascade S11) with a genuine `payment_required_by`, so `DeckCall` held fires from real data.
- **[DATA]** **near_you substrate:** ensure each persona has seeded venues near their test location so the new ambient face (D4) has something to show.
- **Verify:** run the deck for **every** persona — every face shows real names, real currency, real stakes; no "-Style" strings; no QA-scaffold rows.

### Phase D6 — Fallback & entry polish
- **[FE]** Build the **deck entry rail** (canon `vesper-deck-entry.jsx` `DeckEntryRail`): the aggregated "N in motion · votes, a stay… RUN ›" line under the rail; today only per-card taps open the deck. *(Verify current — not re-traced.)*
- **[FE]** Audit the FE fallback (`useConciergeHomeState.ts` local templates): they can only render glance/prose (never a rich face), so ensure they read as honest quiet cards, not starved decision-card imposters. Confirm the backend `degraded_home_feed` + `_starter_cards` paths also read as calm, not broken.
- **Verify:** with the backend feed forced empty, the home shows honest quiet fallback cards; with it populated, rich faces.

---

## 4. Definition of done — a dogfood-grade deck
A tester logged in as elif or mara, in a seeded city, sees a deck where:
1. Every card is **decision-grade** — real venue/person names, a real stake, correct **currency-aware** price (€ for Rome, ¥ for Kyoto), and a Vesper **take line on every face** (not just Pick).
2. **No orphans** — no face renders that the backend can't fill; Compare/Flight are either wired to real substrate or formally parked.
3. **near_you** renders its own **real ambient face** in a corpus city; with no nearby venues it produces **no card**.
4. **Suppress-when-thin holds** — a card that can't form its rich face is dropped, never shown as a starved glance/prose card.
5. The **run-through** clears N real cards; the "N TO CLEAR" counter is true.
6. **Fallback** (backend degraded + FE templates) reads as calm quiet cards, never broken or empty-rich-face.

## 5. File index (jump-in points)
- **FE faces/dispatch:** `travel-app/components/focus-home/{Deck,DeckPickFace,DeckCallFace,DeckBriefFace,DeckStructuredFace,FocusHome}.tsx`; run-through `utils/deckRunthrough.ts`; feed `data/conciergeHome.ts`; mapper `app/(tabs)/concierge/index.tsx:1033`; FE fallback `hooks/useConciergeHomeState.ts`.
- **BE producer:** `travel-agent/backend/api/routes/concierge_home.py:229`; assembler `backend/home/concierge_feed/producers.py`; face builders `backend/home/deck_payloads.py`; models `backend/core/models/vesper_cards.py` + `backend/home/concierge_feed/models.py`; ranking/held/Catch `backend/home/concierge_feed/ranking.py`; Pick LLM `backend/home/pick_judgment.py`; surfaces `backend/core/surfaces/definitions.py`; venue query `backend/core/db/entities.py:782`.
- **Dogfood data:** `travel-agent/tools/dogfood/content/manifests/elif-rome.yaml` (+ `elif-rome-slug-bridge.yaml`), `scenarios.yaml`, `corpus_governance.py`; real dossiers `travel-agent/content/staging/<city>/*.md`.
- **Canon:** `~/Downloads/vesper 146/project/` — faces `vesper-home-deck.jsx` (incl. currency-aware Pick gauge + `DeckNearYou`), mapping `deck-readiness-taxonomy.jsx`, rail entry `vesper-deck-entry.jsx`, and the **Deck Content Contract in `vesper-canon-consolidation-app.jsx` §03b**. (Use the highest `vesper NNN` present if a newer bundle exists.)

## Provenance
Built from four parallel 2026-07-11 investigations (design canon, frontend faces, backend producer, dogfood seed), each read directly with file:line evidence, then reconciled against design canon **vesper 146** (currency-aware gauge · new `DeckNearYou` face · §03b Deck Content Contract — all shipped, no open design items). Verify current before editing — code moves. The deck's architecture is sound; this plan is about **filling the faces with real, contracted content and matching seed data**, not rebuilding the deck.
