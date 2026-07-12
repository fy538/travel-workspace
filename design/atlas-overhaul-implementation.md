# Atlas Overhaul — Implementation Doc

**Status:** design complete, ready to build · **Created:** 2026-07-12 · **Scope:** the Atlas tab (`travel-app/app/atlas/*`, `app/(tabs)/atlas/*`, `components/atlas/*`) + the "Your Memory" surface in Trust & Controls · plus tagged backend/launch items.

> **Read §0 fully before touching code.** A fresh agent has none of the design-session history that produced this. Everything you need is here or cited to a design file you can open. The design canon (pixels) is the source of truth; this doc is the map + the intent + the guardrails.

---

## 0. Orientation

### 0.1 What Atlas is, and what this overhaul does
Vesper is a place-aware travel concierge (React Native / Expo app in `travel-app/`, Python backend in `travel-agent/`, two independent git repos under `~/travel-workspace/`). **Atlas is the 4th tab** (tabs are Trips · Vesper · Discover · Atlas) — and it stays a top-level tab named "Atlas" (this was decided; do not rename or demote it).

The overhaul reframes Atlas from what it currently ships — **a "composition engine / year-recap product" that opens on a Vesper-composed "featured reading," dark and empty for new users** — into a **warm, place-first "living atlas of places"**: your relationship with places (been · loved · want · your takes · your home city), populated from day one, where composed "readings" are things you *open*, never the home's front door.

Three doctrines drive everything:
1. **Place-first, populated from day one.** The home leads with *you and your places* (taste + saved/seeded places), not with an authored composition. A brand-new user must see a warm, alive, honest page — never "a reading is gathering."
2. **Composition is plumbing, not a destination.** Readings/artifacts are OUTPUT you consume (a card you open) or that arrive proactively ("Vesper made you this"). The **words "composition engine" (or any backend system name) NEVER appear in the UI** — users see "readings" and "views."
3. **Warm and honest.** Warm paper, daylight, the app's normal light palette. Evidence-first ("Water keeps appearing · 14 shores," never "you're a water person"); never fabricate; a tap is a weak, overridable *prior*, never a verdict.

### 0.2 The design canon (pixels = source of truth)
The canon is an exported Claude Design bundle at **`~/Downloads/vesper <NNN>/project/`** — a user-local path. **Always use the highest-numbered bundle** (Atlas design was completed at vesper 153; if it's missing, ask the user for the latest `vesper NNN`).

**How to read it (it is NOT normal HTML):** each top-level `Vesper *.html` is canvas-mode — the visible page is empty; the real content is the JSX file named in its `<script src="...jsx">` tag. **Open the `.jsx`, not the `.html`.** These are prototypes: match the visual output, recreate in RN idioms that fit the codebase; don't copy prototype structure. Do NOT implement from files in `archive/` (e.g. `atlas-app-spine-fold.jsx` — the *reverted* dark aesthetic; see guardrails).

**The Atlas design files** (all in the bundle's `project/`):
| File | Owns |
|---|---|
| `atlas-app.jsx` | The place-first HOME: header (monogram→Settings + search), the stage model (Stage-0 true-empty → Cold → Accumulating → Mature), Ways Back In / Long View / Unpacked strips, proactive-drop + reading cards, and the seed wiring. |
| `atlas-seed.jsx` | The COLD-START seed pool: two card families + the state-driven selection/rotation doctrine. |
| `atlas-reader.jsx` | The READING READER: thesis + evidence tiles (provenance + source), arrangement modes (Read/Time/Places, Reel deferred), Steer, the long-press moment primitive, Keep→living-view, Ways Back In states, the evidence + media-degradation doctrine. |
| `atlas-artifacts.jsx` | The OUTPUT LAYER: Atlas Unpacked (year recap + owner share + recipient landing/invite loop), artifact/postcard detail, the style taxonomy + picker. |
| `atlas-complete.jsx` | Memory Inbox, the warm compose flow, State System coverage boards, the home-composition/attention-order board, P0 motion. |
| `trust-screens.jsx` | The "Your Memory" surface (photo permission, learning toggle, render toggle, memory receipt/provenance, correct/forget) — lives under Trust & Controls. |
| `Vesper Canon Consolidation & Ownership.html` → `vesper-canon-consolidation-app.jsx` | Governance: the §03 "Vesper Atlas" ownership row, §02b `/atlas/*` route mapping, and the §06d changelog. When boards seem to disagree, its tables win. |

### 0.3 The HARD GUARDRAILS (what the design deliberately reverted — do NOT build these)
A "meaning-first, composition-led" Atlas was explored and **reverted by design call** (archived at `archive/atlas-app-spine-fold.jsx`). Do not reintroduce any of it:
- **NO dark liminal surfaces.** No `#15110D` (or any dark compose/aperture sheet). Everything renders on **warm paper, daylight** — the reader, Long View, Unpacked, compose, all of it. There is no dark→cream "a shape was found" moment.
- **NO featured-reading home hero.** The Atlas home leads **place-first** (taste + places/seed). Readings, Unpacked, and proactive drops are strips/cards *below* the lead — never the top. A composed reading is something you OPEN, never the home's front door. (The shipped `AtlasHomeBoardHero` violates this — it must be killed; see §5.)
- **NO query aperture.** Composition is a *demoted, warm* "compose a view" flow (§3.7), not a dark full-screen query aperture. (The shipped `compose.tsx` is the archived aperture — replace it.)
- **Honesty invariants:** the string "composition engine" (or any backend name) never appears in UI; never fabricate a reading from an empty corpus; a single tap is a weak overridable prior ("noted," never "you love X"); never pre-assert "loved" for a place merely recognized; evidence-first, never a confidence score.

### 0.4 Register & tokens
Warm paper. Three type families only: **EB Garamond** (serif — the one authored/voice line per surface), **DM Sans** (UI/rows/controls), **JetBrains Mono** (dates/counts/codes). Palette: ink `#1B1714` / gold `#B0853A` / deep gold `#8A6628`; the warm paper ramp. The design already adopted app token canon — "Atlas is a tab, not a sub-brand; distinctiveness lives in the provenance glyphs and the memory spine, not typefaces." Reuse the app's shared primitives (`components/ui/*`: BottomSheet, SheetHeader, state kit, rows) and the State System — do not invent local treatments.

### 0.5 Ground rules for execution
1. **Verify before editing.** Code file/line references here reflect a 2026-07-12 snapshot of `main`; code may have moved. Open the file, confirm, then change. If reality contradicts this doc, trust the code and note the drift.
2. **Branch per phase.** Don't work on `main`. One branch per phase.
3. **Warm-only, place-first.** Every Atlas screen is warm daylight and leads place-first. If a piece only works in the reverted dark/composition aesthetic, it's wrong — check §0.3.
4. **Verify end-to-end, not just typecheck.** Use `/verify` to drive the flow and `/run` to see it; `make typecheck` / `make test-frontend` from `~/travel-workspace` before landing; `/code-review` after each phase.
5. **`[BACKEND]` / `[LAUNCH-GATE]` / `[DECISION]` tags** mark items a frontend agent can't finish alone — surface them (§6), don't fake them.

---

## 1. Current code state (what exists today)

**Tab layout:** `app/(tabs)/atlas/_layout.tsx` + `index.tsx` — Atlas is tab 4. The tab home `index.tsx` currently opens on `AtlasHomeBoardHero` (a Vesper-composed featured-board hero) — **this is the guardrail violation to fix first.**

**Routes present** (`app/atlas/*.tsx`): `account, artifact/[id], board, boards, candidate/[id], companions, compose, constraints, data-receipt, delegation, feedback, inbox, learned/[id], long-view, narration-history, notifications, phone, postcards, privacy, profile, receipt, reel, removed, saved-places, scan, search, shared-links, unpacked, unpacked-card, voice-logs`.
Already correctly gone (design supersessions the code executed): `almanac`, `map`, `timeline`, `following`, `your-map`. *(A few dead backend endpoints + stale Stack.Screen registrations may remain — see §5.)*

**Key components** (`components/atlas/*`): `AtlasHomeBoardHero` (KILL), `AtlasTasteBoard` (the board/reader), `AtlasBoardReel` (Reel), `AtlasInboxReview`, `AtlasLearningSignal`, `AtlasLovedPlaces`, `StylePickerSheet`, `MakePostcardButton`, `ScanProgressCard`, `ProvenanceGlyph`, `RisoSlotImage`, `composition/`, `risoManifest.ts`, plus legacy `AtlasLetterHero`, `AtlasMemoryReel`, `AtlasStartingPoints`, `AtlasOnThisDay` (likely retired — verify).

**Flags** (FE `constants/featureFlags.ts`): `POSTCARDS_ENABLED=false`, `VOICE_ENABLED` (dark), `DOSSIER_VOICE_STUB=false`. (Backend flags in §6.)

**What's already right:** the settings cluster (`account/privacy/notifications/phone/profile/data-receipt/receipt/constraints/delegation`) is Trust & Controls, and `saved-places` is Saved & Collections — both correctly hosted under `/atlas/*` as a named exception; leave their ownership alone (but see §3.8 for the "Your Memory" reconcile). `search` = Universal Search (scope=atlas). `companions` = People & Collaboration.

---

## 2. Surface-by-surface design spec → code target

Each subsection: the design intent (open the cited `.jsx` for pixels), the code target, and the guardrails. Build to the design file; this is the map.

### 3.1 The place-first HOME  — `app/(tabs)/atlas/index.tsx`, `components/atlas/*`
**Design:** `atlas-app.jsx` (stages + strips) + `atlas-complete.jsx` `HomeComposition` (the attention-order board).
- **Header:** monogram (opens Settings/Trust & Controls) + search. Warm glass chrome.
- **Stage model:** Stage-0 (true-empty) → Cold → Accumulating → Mature. The SAME surface fills in; it never flips empty→rich. Lead content = identity/taste + places/seed. Below: Ways Back In (kept living views), a quiet Long View strip ("Since 2023 · The whole Atlas →"), an Unpacked strip (year-end), proactive-drop cards, reading cards, and a quiet "N to review" Memory Inbox entry.
- **Attention-order rule (load-bearing):** identity + taste + places/seed ALWAYS lead; readings/Unpacked/proactive drops are strips/cards BELOW, never the hero. Implement a priority/attention order so modules don't fight for the top — this is what prevents the featured-hero from creeping back.
- **Guardrail:** replace `AtlasHomeBoardHero` — the home must NOT open on a composed featured reading.

### 3.2 Cold-start SEED  — the Stage-0 state
**Design:** `atlas-seed.jsx`.
- **Two card families:** (A) *seed-a-place* — persistent search ("a place you love"), the standing photo scan ("Let Atlas find your past trips"), `known around {city}`, `your everyday place`, `cities you've been`, `somewhere you're dreaming of` (→ tags **want**). (B) *get-to-know-you* — `set your home` (structural, top priority when unset), `what kind of food`, `your pace`, `what pulls you in`.
- **Selection doctrine (show the best 1–2):** home city UNSET → lead "Set your home"; onboarding taste SKIPPED (the truly-blank user) → lead a light Family-B card; else → lead a Family-A place-seed. Always keep search + scan available. **Rotate** the pool so a returning-empty user sees a fresh angle. Cap at 1–2 hook cards — never a wall.
- **Honesty:** Family-B taps are weak priors ("noted," not a verdict; correctable via Your Memory's one-correction-model); `known around {city}` tags are chosen on save (want/been/loved), never hardcoded "loved."

### 3.3 The READING READER  — `app/atlas/board.tsx` (+ `artifact/[id]` for kept artifacts, §3.5)
**Design:** `atlas-reader.jsx`.
- **A reading contains:** a thesis (one serif voice line) + evidence tiles, each with a **provenance marker** (○ first · ◑ returned · ● kept · ◎ now · + supporting) and a mono **source label** (receipt/photo/suggested/saved/planned/corrected/private) + an evidence-count line. Keep + Steer live *inside* the opened reading.
- **Arrangement modes** (a warm switcher — same memory set, different views): **Read** (canonical editorial) · **Time** (the memory spine / timeline; subtle warm polaroid tactility Time-only) · **Places** (map; color=place, glyph=evidence-state) · **Reel** (deferred — greyed in the switcher, not built in v1).
- **Long-press moment primitive** (identical in Read/Time/Places): Why this is here · Hide from this view (local recompose; if it empties below threshold, fall to an honest list) · Pin to this view · This isn't right (= the one-correction-model, §3.8).
- **Media degradation** (warm): no media → deterministic theme plate (food→rust · water→teal · market→moss · night→deep-tobacco · unknown→tobacco); photo → real photo replaces the plate on load; private → safety plate, never blur. The keep→render riso view lives under this doctrine.
- **Route note:** design calls this `/atlas/readings/[id]`; code ships `/atlas/board`. Reconcile naming (rename or alias).

### 3.4 LONG VIEW  — `app/atlas/long-view.tsx`
**Design:** `atlas-reader.jsx` Long View board. Warm whole-corpus browse INDEX (not a reading — no thesis, no authored voice). Facets: **Time** (year chapters) · **Places** (whole-corpus city nodes) active; **People / Theme** deferred (shown inactive). Time absorbs any Almanac/standalone-timeline browse. A quiet home strip, never the hero.

### 3.5 The OUTPUT LAYER  — `app/atlas/unpacked.tsx`, `unpacked-card.tsx`, `artifact/[id].tsx`, `StylePickerSheet`, `postcards.tsx`
**Design:** `atlas-artifacts.jsx`.
- **Atlas Unpacked** (the year recap — the ONE sanctioned *more-expressive* surface, but still warm, never dark): honest entry strip (+ thin-year "A quieter year" variant, never a faked montage); the swipeable warm editorial recap deck (shape-of-year counts · authored pattern thesis · map · kept highlights w/ provenance · closing); **owner share controls** (copy/rotate/pause/revoke/preview/stats — consuming External Sharing's link-state taxonomy); and the **recipient landing (public web)** drawn as a first-class **invite loop** — read-only warm view + honest "start your Atlas" (private moments never leak; safety plates for redacted). This is a growth surface — treat the landing/invite as first-class.
- **Artifact / postcard detail** (`artifact/[id]`): a single kept composed thing (distinct from a multi-evidence reading). The artifact (riso-rendered if enabled, else warm plate per media doctrine) + its editable one-line "read" + actions (share · render · delete-with-confirm) + "what this taught Vesper" (the DNA/learning toggle = the one-correction-model).
- **Style taxonomy** (canonical set, reconciled FE↔BE): **Postcard** (riso single) · **Spread** (thesis + tiles) · **Mosaic** (gridded journal) · **Lineage** (the Time-spine pattern) · **Year** (Unpacked). Plus a **light style picker** (moment-of-intent, never homework; sensible default).
- **Postcards shelf ruling:** postcards **fold into the kept/Readings shelf** (Ways Back In) — not a standalone gallery. `postcards.tsx` should redirect/absorb.

### 3.6 MEMORY INBOX  — `app/atlas/inbox.tsx`, `components/atlas/AtlasInboxReview.tsx`
**Design:** `atlas-complete.jsx` `MemoryInbox`/`InboxRow`. A returnable, batched, **multi-kind review queue** (never a notification firehose): past-trip candidates (the scan's "Keep them?" is one item-type here) · noticed patterns (evidence-first: Looks-right / Not-quite / Hide) · place-clusters to name · readings/postcards ready · corrections. Each row = one light action. Honest empty ("Nothing to review — your atlas is up to date"). Entry = a quiet "N to review" home affordance (no red-badge firehose). Corrections here ARE the one-correction-model.

### 3.7 The warm COMPOSE flow  — `app/atlas/compose.tsx` (REPLACE the dark aperture)
**Design:** `atlas-complete.jsx` `ComposeIntent`/`ComposeFindingShape`/`ComposeThin`. The **demoted, warm, place-first** replacement for the killed dark query aperture: a light intent capture with a few warm suggested-angle chips ("places I keep returning to," "everywhere I've had the seafood," "my Lisbon") → a warm progressive "finding the shape…" (no dark sheet, no full-screen spinner) → the reading reader opens. Thin result falls to an honest list, never a faked story. Most readings arrive as proactive drops; this is the quiet "I want to make one" path.

### 3.8 "YOUR MEMORY" (Trust & Controls)  — reconcile the scattered memory-config routes
**Design:** `trust-screens.jsx` `YourMemory`. The "What Vesper knows" Settings zone opens into ONE control center that unifies today's scattered routes (`receipt`, `constraints`, `learned/[id]`, `privacy`, `data-receipt`): **photo access** status + grant/revoke (with the on-device privacy line) · the **learning toggle** ("Learn from what you keep" — the FE control for the dark `ATLAS_SIGNALS_TO_MEMORY` loop) · the **render toggle** ("Render your photos into views") · **what Vesper has learned** (memory receipt + provenance filter: from photos / past trips / chats) · **correct/forget** (soften · forget-a-fact · reset-all). **One correction model, two surfaces:** the in-reading "This isn't right" and this soften/forget are the SAME system — corrections suppress permanently. Do not build a second correction UI.

### 3.9 Cross-cutting: STATE COVERAGE + MOTION
**Design:** `atlas-complete.jsx` `StateCoverage` + `MotionBoard`.
- **State System (warm, per surface, using the app's State canon — no local invention):** reader (composing/skeleton · error+retry · offline-cached · thin→honest list) · Long View (loading · empty · offline) · Unpacked (loading · thin-year · error · not-yet-available) · artifact (loading · render-in-progress · render-failed-retryable · offline) · inbox (loading · empty · offline). **The output layer currently has none — this is where "unfinished" shows.**
- **P0 motion (each with an instant-cut reduced-motion fallback):** home → open reading (fade ~300ms) · Read↔Time↔Places (tiles migrate, continuous ~500ms) · Keep → Ways Back In (row appears on return) · compose → reading (warm progressive reveal, no dark/spinner) · scan-in-progress (non-blocking). "Calm, physical, warm — never the dark transition."

---

## 4. Phased implementation plan

Land each phase independently; verify end-to-end + `/code-review` before the next.

- **Phase 1 — Kill the reverted aesthetic + retire dead code.** Replace `AtlasHomeBoardHero` (featured hero) so the home no longer opens on a composed reading. Replace `compose.tsx`'s dark aperture with the warm flow (§3.7). Retire dead backend endpoints (`/atlas/almanac`, `/atlas/map`) + stale Stack.Screen registrations; confirm `your-map` redirects to Long View. *Foundational — unblocks the warm home.*
- **Phase 2 — The warm place-first home** (§3.1): stage model + header + the attention-order composition. This is the make-or-break surface.
- **Phase 3 — Cold-start seed** (§3.2): two families + the state-driven selection + rotation.
- **Phase 4 — The reading reader** (§3.3): thesis/evidence/provenance + Read/Time/Places modes + Steer + moment primitive + media degradation. (Reel stays deferred — see §5.)
- **Phase 5 — Long View** (§3.4).
- **Phase 6 — Output layer** (§3.5): Unpacked (+ share + landing/invite) · artifact detail · style taxonomy/picker · postcards fold.
- **Phase 7 — Memory Inbox + warm compose** (§3.6, §3.7 if not done in Ph1).
- **Phase 8 — "Your Memory" reconcile** (§3.8): unify the memory-config routes into one surface + the one-correction-model.
- **Phase 9 — State coverage + motion pass** (§3.9) across every surface.

Suggested order rationale: Phase 1 removes what contradicts the design; Phase 2 establishes the warm home everything hangs off; 3–7 build the surfaces; 8 unifies controls; 9 is the finishing hygiene that makes it feel done.

---

## 5. Mismatches & kills (code ships what design reverted/deferred)

- **`AtlasHomeBoardHero` (featured-reading home hero) → KILL.** Design guardrail: no featured hero; home leads place-first. Replace in `app/(tabs)/atlas/index.tsx`. (Phase 1.)
- **`compose.tsx` (dark query aperture) → REPLACE** with the warm compose flow (§3.7). (Phase 1/7.)
- **Reel (`app/atlas/reel.tsx`, `AtlasBoardReel`) → design DEFERS it (greyed, not v1); code ships it live.** `[DECISION]`: either hide/deprecate Reel for v1 to match design, or the user rules to keep it live. Don't silently keep both positions.
- **Dead backend endpoints** `GET /api/atlas/almanac` (+ `almanac_generator/*`) and `GET /api/atlas/map` (+ `map_compose.py`) — FE consumers deleted; retire the endpoints once confirmed unused. Remove stale `Stack.Screen` registrations for deleted routes and any "opened from the Almanac footer" residue.
- **Route-name drift:** `/atlas/board` (code) vs `/atlas/readings/[id]` (design) — reconcile.

---

## 6. Not-frontend / needs an owner (surface these; don't fake them)

- **`[BACKEND]` + `[LAUNCH-GATE]` `ATLAS_SIGNALS_TO_MEMORY`** (backend `feature_flags.py`, default OFF) — the "learn from what you keep" loop (kept photo-memories → durable taste). Fully coded incl. revocation, but dark. The learning toggle (§3.8) is its UI. **Flipping it is a founder/privacy launch call.**
- **`[BACKEND]` + `[LAUNCH-GATE]` render loop** — `postcard_render_enabled` + `ATLAS_LLM_ENABLED` (both dark) power the riso img2img render + real-prose composition. The render toggle (§3.8) is its UI. Cost/launch gated.
- **`[LAUNCH-GATE]`** `POSTCARDS_ENABLED` (FE, false), `VOICE_ENABLED` (dark), and **Unpacked public share** (ships after the story-share/J19 privacy cert). Design is complete; going live is a product call.
- **`[BACKEND]` `ATLAS_AUTO_CANDIDATE_ENABLED`** (dark) — server-side auto-candidate generation for the Memory Inbox.
- **`[DECISION]`** (record, don't guess): learning-toggle default at launch (lean OFF); whether render ships v1; **whether a Family-B taste tap *also* seeds places** (or stays a pure prior); Reel keep-live vs defer.
- **Low-priority / dark:** `voice-logs`, `narration-history` archives — undesigned Atlas records, both flag-dark; defer.

---

## 7. Verification (per surface + global honesty invariants)

After each phase, drive the surface (`/verify`, `/run`) and check the **honesty invariants** hold — these are the load-bearing ones:
- The string "composition engine" (or any backend system name) appears **nowhere** in Atlas UI.
- **No dark surfaces** anywhere in Atlas; every screen is warm daylight.
- The Atlas home **never opens on a composed reading** — it leads place-first; readings/Unpacked/proactive-drops are below.
- Cold-start shows a warm, populated, honest page (never "a reading is gathering") — 1–2 seed cards, priors-not-verdicts, `known around {city}` tags chosen on save.
- Readings are **evidence-first** (provenance markers + source labels; never a confidence score; never "you are a X person"); private moments never leak (safety plates, never blur).
- Corrections (in-reading "This isn't right" and Your Memory soften/forget) are **one system** and suppress permanently.

## Provenance
Built from a 2026-07-12 functional gap audit of Atlas (code+backend vs the vesper-153 design canon) plus the design-session history that produced the warm, place-first Atlas (the composition-first "spine fold" was explored and reverted; see `archive/atlas-app-spine-fold.jsx`). The design canon (the `atlas-*.jsx` boards) is the pixel source of truth — this doc is the intent, the map, and the guardrails. Every code path here reflects that snapshot — **verify current before editing** (§0.5).
