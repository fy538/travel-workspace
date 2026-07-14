# Atlas Overhaul — Implementation Doc

**Status:** implementation substantially complete; final state-system design approved and implementation alignment pending · **Created:** 2026-07-12 · **Home clarification:** 2026-07-12 · **Final design adjudication:** 2026-07-13 · **Scope:** the Atlas tab (`travel-app/app/atlas/*`, `app/(tabs)/atlas/*`, `components/atlas/*`) + the "Your Memory" surface in Trust & Controls · plus tagged backend/launch items.

> **Read §0 fully before touching code.** A fresh agent has none of the design-session history that produced this. Everything you need is here or cited to a design file you can open. The latest design canon owns visual execution; the recorded product rulings in this doc own hierarchy, eligibility, data honesty, and surface behavior.

---

## 0. Orientation

### 0.1 What Atlas is, and what this overhaul does
Vesper is a place-aware travel concierge (React Native / Expo app in `travel-app/`, Python backend in `travel-agent/`, two independent git repos under `~/travel-workspace/`). **Atlas is the 4th tab** (tabs are Trips · Vesper · Discover · Atlas) — and it stays a top-level tab named "Atlas" (this was decided; do not rename or demote it).

The overhaul reframes Atlas from what it currently ships — **a "composition engine / year-recap product" that opens on a Vesper-composed "featured reading," dark and empty for new users** — into a **warm, place-first "living atlas of places"**: your relationship with places (been · loved · want · your takes · your home city), populated from day one, where composed "readings" are things you *open*, never the home's front door.

Atlas serves three related purposes, in this order: **personal place memory is the foundation; interpretation is the intelligence layer; durable authored Readings are the output.** All three belong in Atlas, but they must not compete as equal front doors. The Home keeps a stable place-first backbone while gaining depth as the corpus grows.

Four doctrines drive everything:
1. **Place-first, populated from day one.** The home leads with *you and your places* (taste + saved/seeded places), not with an authored composition. A brand-new user must see a warm, alive, honest page — never "a reading is gathering."
2. **Composition is plumbing, not a destination.** Readings/artifacts are OUTPUT you consume (a card you open) or that arrive proactively ("Vesper made you this"). The **words "composition engine" (or any backend system name) NEVER appear in the UI** — users see "readings" and "views."
3. **Warm and honest.** Warm paper, daylight, the app's normal light palette. Evidence-first ("Water keeps appearing · 14 shores," never "you're a water person"); never fabricate; a tap is a weak, overridable *prior*, never a verdict.
4. **Conversational when cold; archival when mature.** An early Atlas may use a small number of temporary, low-friction learning cards so it is useful before the user has trips. As evidence grows, those cards recede and the surface becomes calmer, flatter, and more editorial.

### 0.2 The design canon (pixels = source of truth)
The canon is an exported Claude Design bundle at **`~/Downloads/vesper <NNN>/project/`** — a user-local path. **Always use the highest-numbered reviewed Atlas bundle.** The final state-system bundle reviewed and approved for this implementation is **`vesper 173`**. A later export does not silently replace it: review the newer Atlas section and update this receipt before implementing from it.

**How to read it (it is NOT normal HTML):** each top-level `Vesper *.html` is canvas-mode — the visible page is empty; the real content is the JSX file named in its `<script src="...jsx">` tag. **Open the `.jsx`, not the `.html`.** These are prototypes: match the visual output, recreate in RN idioms that fit the codebase; don't copy prototype structure. Do NOT implement from files in `archive/` (e.g. `atlas-app-spine-fold.jsx` — the *reverted* dark aesthetic; see guardrails).

**The Atlas design files** (all in the bundle's `project/`):
| File | Owns |
|---|---|
| `atlas-home-final.jsx` | **Canonical Atlas Home implementation source:** truthful blank, cold, accumulating, mature, loading, and stale/error states; the dynamic-hero register; canonical section order; warm timely returns; saved-versus-visited grammar; and the restrained Whole Atlas entrance. |
| `atlas-memory-final.jsx` | **Canonical Your Memory and Memory Receipt implementation source:** synthesis-first hierarchy, learned evidence and provenance, learning/photo states, correction controls, honest empty/loading/stale states, and receipt correction context. |
| `Vesper Atlas.html` | Canvas-level adjudication. The section titled **“Atlas Home — final state system · CANONICAL”** wins over every older Home composition. Every other section carries `CANONICAL`, `SUPPORTING`, `SUPERSEDED`, or `DEFERRED` status. |
| `atlas-app.jsx` | The place-first HOME: header (monogram→Settings + search), the stage model (Stage-0 true-empty → Cold → Accumulating → Mature), the historical Ways Back In treatment (superseded by the Readings shelf), Long View / Unpacked strips, proactive-drop + reading cards, and the seed wiring. |
| `atlas-seed.jsx` | The COLD-START seed pool: two card families + the state-driven selection/rotation doctrine. |
| `atlas-reader.jsx` | The READING READER: thesis + evidence tiles (provenance + source), arrangement modes (Read/Time/Places, Reel deferred), Steer, the long-press moment primitive, Keep→Readings shelf, freshness states, and the evidence + media-degradation doctrine. |
| `atlas-artifacts.jsx` | The OUTPUT LAYER: Atlas Unpacked (year recap + owner share + recipient landing/invite loop), artifact/postcard detail, the style taxonomy + picker. |
| `atlas-complete.jsx` | Memory Inbox, the warm compose flow, State System coverage boards, the home-composition/attention-order board, P0 motion. |
| `trust-screens.jsx` | The "Your Memory" surface (photo permission, learning toggle, render toggle, memory receipt/provenance, correct/forget) — lives under Trust & Controls. |
| `Vesper Canon Consolidation & Ownership.html` → `vesper-canon-consolidation-app.jsx` | Governance: the §03 "Vesper Atlas" ownership row, §02b `/atlas/*` route mapping, and the §06d changelog. When boards seem to disagree, its tables win. |

**Product rulings override unresolved prototype details.** In particular, the Home clarification recorded in §3.1–§3.2 overrides any board that (a) removes the place-first backbone in mature states, (b) presents passive taste chips as permanent Home furniture, (c) shows unsupported `loved`/relationship claims, or (d) treats every Home section as a card. Claude Design should visualize this resolved grammar; it must not be asked to choose the product hierarchy from conflicting boards.

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

**Tab layout:** `app/(tabs)/atlas/_layout.tsx` + `index.tsx` — Atlas is tab 4. Home now opens on the place-first identity and saved/seeded-place lead; the featured-board hero has been retired.

**Routes present** (`app/atlas/*.tsx`): `account, artifact/[id], board, boards` *(compatibility)*, `candidate/[id], companions, compose, constraints, data-receipt, delegation, feedback, inbox, learned/[id], long-view, narration-history, notifications, phone, postcards, privacy, profile, readings/index, readings/[id], receipt, reel, removed, saved-places, scan, search, shared-links, unpacked, unpacked-card, voice-logs`.
Already correctly gone (design supersessions the code executed): `almanac`, `map`, `timeline`, `following`, `your-map`. *(A few dead backend endpoints + stale Stack.Screen registrations may remain — see §5.)*

**Key components** (`components/atlas/*`): `AtlasPlaceFirstLead`, `AtlasTasteBoard` (the Reading renderer; internal rename still pending), `AtlasInboxReview`, `AtlasLearningSignal`, `AtlasDiscoveryReflection`, `AtlasOnThisDay`, `StylePickerSheet`, `MakePostcardButton`, `ScanProgressCard`, `ProvenanceGlyph`, `RisoSlotImage`, `SavedBoardCover` (legacy persistence adapter), `composition/`, and `risoManifest.ts`. Home-only Starting Points, active-trip, Loved Places, and Desk components are retired.

**Flags** (FE `constants/featureFlags.ts`): `POSTCARDS_ENABLED=false`, `VOICE_ENABLED` (dark), `DOSSIER_VOICE_STUB=false`. (Backend flags in §6.)

**What's already right:** the settings cluster (`account/privacy/notifications/phone/profile/data-receipt/receipt/constraints/delegation`) is Trust & Controls, and `saved-places` is Saved & Collections — both correctly hosted under `/atlas/*` as a named exception; leave their ownership alone (but see §3.8 for the "Your Memory" reconcile). `search` = Universal Search (scope=atlas). `companions` = People & Collaboration.

---

## 2. Surface-by-surface design spec → code target

Each subsection: the design intent (open the cited `.jsx` for pixels), the code target, and the guardrails. Build to the design file; this is the map.

### 3.1 The place-first HOME  — `app/(tabs)/atlas/index.tsx`, `components/atlas/*`
**Design:** `atlas-home-final.jsx` (canonical pixels and states). Use `atlas-app.jsx` and `atlas-complete.jsx` only where the final section explicitly marks their supporting concepts as still valid.
- **Header:** monogram (opens Settings/Trust & Controls) + search. Warm glass chrome.
- **Stage model:** Stage-0 (true-empty) → Cold → Accumulating → Mature. The SAME surface fills in; it never flips empty→rich. Lead content = identity/taste + places/seed. Atlas remains place-first at every stage; maturity adds interpretation and authored output without replacing the place layer.
- **Attention-order rule (load-bearing):** the dynamic hero ALWAYS leads. Actionable review follows it when present and precedes passive places/editorial content; otherwise Your Places or the truthful blank-state entrance follows directly. Readings/Unpacked/proactive drops are strips/cards BELOW this backbone, never the hero. Implement one priority/eligibility resolver so modules do not fight for the top.
- **Guardrail:** replace `AtlasHomeBoardHero` — the home must NOT open on a composed featured reading.

#### 3.1.1 Canonical Home section grammar
The eligibility order is:
1. **Dynamic Atlas hero.** A concise interpretation of the user's travel identity. It may temporarily respond to a recent meaningful action (save, accepted trip, completed Reading, correction), then returns to the stable identity. It must not repeat a module below or make an unsupported claim.
2. **Needs your attention** *(conditional).* A quiet Inbox/review entry only when unresolved work exists. Workflow takes precedence over passive, celebratory, or editorial modules.
3. **Your places.** A flat canonical-list preview with an Add action. Saved intent and visited history are distinct concepts. A place may carry an explicit, editable relationship (`loved`, `been`, `want to go`); never infer `loved` from a save or visit.
4. **Readings** *(conditional).* The latest durable authored Reading plus entry to its shelf. A Reading is a revisitable artifact with source evidence, not a disposable insight card.
5. **One timely return** *(conditional; max one).* On This Day, Unpacked, or one recent grounded discovery/reflection. These need freshness, expiry/dismissal, and sufficient-evidence rules. Live-trip operations do not belong here; Trips owns active travel.
6. **Places you've been** *(conditional).* A compact visited-history/map preview, separate from saved places, once accepted history exists.
7. **The Whole Atlas** *(conditional).* One restrained archive row exposing Places, Been, Readings, and Taste once there is enough real material to browse.
8. **Learning** *(conditional and occasional).* A mature trust prompt for one specific, evidence-backed claim. Once confirmed, corrected, or dismissed, it leaves Home and updates the Taste/Your Memory record.

Only the hero and the place/seed layer are structural constants. The page must not render every eligible module merely because data exists. When actionable work exists it follows the hero and precedes passive place/editorial content. Otherwise cap a normal visit at **one timely return and no more than two prominent editorial cards**.

#### 3.1.2 Card taxonomy and flattening rule
Cards have two valid jobs:
- **Learning cards:** temporary, interactive cold-start prompts; one or two taps; optional; retired once answered.
- **Artifact cards:** durable or time-bounded authored objects such as a Reading, On This Day, or Unpacked.

Everything else stays visually flatter: saved-place lists, Inbox actions, archive links, Add actions, map entrances, Long View, and mature Learning confirmation. Do not place the whole saved list inside a heavy enclosing card. Do not render several unrelated rounded surfaces with equal emphasis.

The following do **not** belong on Home: active-trip management, a multi-card Starting Points dashboard, an independently surfaced saved-boards stack, Desk/Postcard, duplicate return sections, or generic "Across your trips" claims with no clear evidence/action. Authored output lives in Readings; legacy saved-board records are an internal persistence detail. Postcards fold into Readings.

#### 3.1.3 Stage composition contract
| Stage | Must appear | May appear | Must not appear |
|---|---|---|---|
| **Truly blank** | Truthful welcome hero; place search; one combined home-area/nearby entrance; at most one optional learning entrance | Photo recovery **or** one quick taste question, selected by eligibility | Invented home context; simultaneous photo + taste prompts; Readings; map; Long View; mature Learning; return shelf; Desk |
| **Cold / first saves** | Provisional hero; 1–3 saved places; Add another; at most one optional question | Inbox when actionable; place-based relationship question | Empty visited-history section; Readings without accepted evidence; annual summaries; On This Day; persistent insight cards; Desk |
| **Accumulating** | Taste hero; saved preview; accepted visited history when present | Inbox; first grounded Reading; one timely return; Whole Atlas once its archive destinations are useful | Active-trip cards; Starting Points stack; unsupported Learning; Desk |
| **Mature** | Condensed taste hero; saved preview; Readings shelf; visited-history entry; Whole Atlas | Inbox; one timely return; one recent receipt; one mature Learning prompt | Permanent taste chips; duplicate return sections; Desk; active-trip operations |

The stage name alone does not decide composition. Stage, workflow, recent action, temporal opportunity, and trust prompts are separate axes, so implement one explicit precedence/eligibility resolver rather than allowing independent modules to accumulate down the page.

#### 3.1.4 Hero and Compose entrance
The hero may be dynamic while the Home backbone remains stable:
- default → established taste identity;
- after save → what the place adds, stated provisionally;
- after accepted trip → what changed in the evidence;
- after a completed Reading → its central idea and a route back;
- after correction → acknowledge the revised understanding;
- after inactivity/expiry → return to the stable identity.

Compose remains discoverable without becoming Atlas's purpose. Before the first Reading, offer a contextual **"Make something from these places"** action only when enough source material exists. After the first Reading, expose **New Reading** inside the Readings shelf. The header sparkle may open an intelligence/action menu, but must not drop a cold user into an empty editor. Entrances from trips, selected places, or collections should pre-attach their source context.

#### 3.1.5 Whole Atlas archive
"The whole Atlas" resolves to four explicit views rather than an ambiguous feed:
- **Places** — saved places and relationship filters;
- **Been** — visited history and map;
- **Readings** — durable authored artifacts;
- **Taste** — current interpretation, evidence, and correction history.

Trips may appear as provenance/evidence, but Atlas must not duplicate the operational Trips surface.

### 3.2 Cold-start SEED  — the Stage-0 state
**Design:** `atlas-home-final.jsx` `HomeStage0` / `BlankEntrances`; `atlas-seed.jsx` remains supporting doctrine for the optional prompt pool.
- **Three-part blank composition:** (1) persistent primary search ("a place you love"); (2) one combined location row that opens Set Home Area or Use Current Location; (3) at most one optional learning entrance.
- **Selection doctrine:** photo recovery appears when past-trip recovery is relevant; otherwise one concrete Family-B taste question may appear. Search is always present. Photo recovery and the taste question never appear together. Rotate eligible questions for a returning-empty user, but never render a wall of hooks.
- **Honesty:** Family-B taps are weak priors ("noted," not a verdict; correctable via Your Memory's one-correction-model); `known around {city}` tags are chosen on save (want/been/loved), never hardcoded "loved."
- **Low-friction doctrine:** cold-start cards exist to help the user teach Atlas before a trip corpus exists, not to simulate authored content or fill space. Every prompt is optional, dismissible, answerable in one or two taps, and immediately reflected in the user's understanding/receipt.
- **Ask concrete tradeoffs, not personality quizzes:** e.g. neighborhood wandering vs major landmarks; market breakfast vs quiet café vs early museum; atmosphere vs food vs history; anchor planning vs leaving the day open. As real places arrive, replace generic prompts with grounded questions such as "Would you return here?", "Loved or useful?", or "Been or want to go?"
- **Retire answered cards:** a completed prompt leaves Home and becomes provenance in Taste/Your Memory. Do not keep passive answer chips under the hero. Early Atlas is conversational; accumulating Atlas asks evidence-based distinctions; mature Atlas shows only rare correction/nuance prompts.
- **No permanent hero chips:** the current passive taste chips are removed from Home, especially in mature states. Their concepts may live in the Taste detail/editing surface where users can inspect and correct them. If Atlas needs nuance, ask one meaningful grounded question rather than displaying a row of labels.

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
- **Postcards shelf ruling:** postcards **fold into Readings** — not a standalone gallery. `postcards.tsx` redirects to `/atlas/readings`.

### 3.6 MEMORY INBOX  — `app/atlas/inbox.tsx`, `components/atlas/AtlasInboxReview.tsx`
**Design:** `atlas-complete.jsx` `MemoryInbox`/`InboxRow`. A returnable, batched, **multi-kind review queue** (never a notification firehose): past-trip candidates (the scan's "Keep them?" is one item-type here) · noticed patterns (evidence-first: Looks-right / Not-quite / Hide) · place-clusters to name · readings/postcards ready · corrections. Each row = one light action. Honest empty ("Nothing to review — your atlas is up to date"). Entry = a quiet "N to review" home affordance (no red-badge firehose). Corrections here ARE the one-correction-model.

### 3.7 The warm COMPOSE flow  — `app/atlas/compose.tsx` (REPLACE the dark aperture)
**Design:** `atlas-complete.jsx` `ComposeIntent`/`ComposeFindingShape`/`ComposeThin`. The **demoted, warm, place-first** replacement for the killed dark query aperture: a light intent capture with a few warm suggested-angle chips ("places I keep returning to," "everywhere I've had the seafood," "my Lisbon") → a warm progressive "finding the shape…" (no dark sheet, no full-screen spinner) → the reading reader opens. Thin result falls to an honest list, never a faked story. Most readings arrive as proactive drops; this is the quiet "I want to make one" path.

### 3.8 "YOUR MEMORY" (Trust & Controls)  — one canonical memory center
**Design:** `atlas-memory-final.jsx`. The "What Vesper knows" Settings zone opens into ONE control center at `/atlas/memory`. Its hierarchy is: **what Vesper understands** (synthesis) · **learned evidence and provenance** · **photo access** · **how Vesper learns** · subordinate record/correction controls · isolated destructive reset. An empty learned state keeps learning ON unless the user explicitly disabled it. Launch-gated capabilities collapse into a quiet note instead of looking like broken switches. Artifact-specific learned signals live inline on `/atlas/artifact/[id]`, beside the memory that produced them. Historical `/atlas/receipt` and `/atlas/learned/[id]` URLs are compatibility aliases only. Constraints, privacy, and the data-use receipt remain linked specialist records, not competing memory homes. **One correction model, two contexts:** the in-reading/artifact "This isn't right" and Your Memory soften/forget are the SAME system — corrections suppress permanently. Do not build a second correction UI.

### 3.9 Cross-cutting: STATE COVERAGE + MOTION
**Design:** `atlas-complete.jsx` `StateCoverage` + `MotionBoard`.
- **State System (warm, per surface, using the app's State canon — no local invention):** reader (composing/skeleton · error+retry · offline-cached · thin→honest list) · Long View (loading · empty · offline) · Unpacked (loading · thin-year · error · not-yet-available) · artifact (loading · render-in-progress · render-failed-retryable · offline) · inbox (loading · empty · offline). **The output layer currently has none — this is where "unfinished" shows.**
- **P0 motion (each with an instant-cut reduced-motion fallback):** home → open reading (fade ~300ms) · Read↔Time↔Places (tiles migrate, continuous ~500ms) · Keep → Readings shelf (row appears on return) · compose → reading (warm progressive reveal, no dark/spinner) · scan-in-progress (non-blocking). "Calm, physical, warm — never the dark transition."

---

## 4. Final alignment implementation plan

Phases 1–9 of the original overhaul are substantially implemented. The remaining work is a final canon-alignment sequence. Land each slice independently; verify end-to-end + `/code-review` before the next.

- **Slice 1 — Adopt the final canon. ✅** Updated this doc, Home/Memory/Receipt contracts, design receipts, and the pre-design audit/brief to the approved final state system.
- **Slice 2 — Centralize Home composition. ✅** Split hero, saved places, and seed entrances into independent components; `resolveAtlasHomeComposition` now owns ordered eligibility, including hero → actionable attention → places.
- **Slice 3 — Implement final blank and cold states. ✅** One search entrance, one combined location entrance, one optional learning entrance; provisional cold hero; no empty visited section; durable prompt retirement/provenance.
- **Slice 4 — Implement accumulating and mature composition. ✅** Dynamic hero circumstances now resolve from expiring save/trip/Reading/correction/return evidence; recent consequences fold into the hero instead of duplicating it; accepted visited history is a distinct canonical row preview; and Whole Atlas is one restrained archive doorway with Places · Been · Readings · Taste grammar. Existing actionable attention, saved rows, durable Readings, one timely return, and rare learning remain under the central composition resolver.
- **Slice 5 — Align Your Memory and Memory Receipt.** Synthesis first, evidence second, controls third; honest nothing-learned versus learning-off states; no duplicate Current Read or confidence-pill hierarchy.
- **Slice 6 — Cleanup and certify.** Remove obsolete Home branches/components, audit unused compatibility fields, regenerate contracts if required, run focused tests, and refresh the registered state captures.

The bundled `AtlasPlaceFirstLead` boundary has been removed. Keep final-state work on the split components and the central resolver; do not reintroduce local section-order booleans in the screen.

---

## 5. Current implementation mismatches

- **Home composition boundary — resolved.** `AtlasHomeHero`, `AtlasSavedPlacesSection`, and `AtlasSeedEntrances` are independent; `resolveAtlasHomeComposition` owns eligibility and section order. Actionable attention now follows the hero before passive places.
- **Blank and cold states — resolved.** Stage 0 now uses one primary search, one combined home-area/current-location entrance, and at most one optional photo-recovery entrance. Cold uses a provisional hero, one to three canonical saved rows, Add another, and one optional binary prompt that retires durably and records source-attributed weak-prior provenance in Personal Memory.
- **Hero behavior — resolved.** Stable, recent save, accepted trip, completed Reading, recent correction, and meaningful-return circumstances now resolve from bounded evidence and expire back to stable. Save/correction consequences are absorbed rather than repeated below the hero.
- **Visited and Whole Atlas — resolved.** Accepted trips and user-kept memories produce a distinct Places You've Been preview; saved intent and drafts are excluded. Whole Atlas uses one canonical flat archive row with Places · Been · Readings · Taste grammar.
- **Your Memory hierarchy.** Photo access and feature availability currently precede learned synthesis/evidence. The final design reverses that priority and collapses unavailable future capabilities.
- **Receipt hierarchy.** The current receipt still exposes `CURRENT READ` and qualitative confidence pills. The final design uses synthesis → evidence/provenance → correction → subordinate technical receipt, with no confidence UI competing with evidence.
- **Legacy contract residue.** After UI parity, audit unused `AtlasHome` letter/room/shelf/postcard compatibility fields and remove only those proven unconsumed. Do not combine that contract cleanup with the visual refactor.

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
- Cold-start shows a warm, populated, honest page (never "a reading is gathering") — place search/location/photo recovery when blank, then one to three real saved rows and at most one prior-not-verdict question after the first saves.
- Cold-start choices are optional, answerable in one or two taps, reflected in Taste/Your Memory, and removed after answering; passive taste chips do not remain on Home.
- Saved places and Places You've Been remain separate; `loved` / `been` / `want to go` are explicit editable relationships, never inference shortcuts.
- A normal Home visit shows at most one timely-return module and no more than two prominent editorial cards; independent eligible modules do not accumulate into a dashboard.
- Active-trip operations stay in Trips; Starting Points stacks, standalone boards, and Desk/Postcard do not appear on Home.
- Readings are **evidence-first** (provenance markers + source labels; never a confidence score; never "you are a X person"); private moments never leak (safety plates, never blur).
- Corrections (in-reading "This isn't right" and Your Memory soften/forget) are **one system** and suppress permanently.

### 7.1 Final design adjudication and implementation handoff — 2026-07-13

The implementation now has registered Home captures for stage 0, cold,
accumulating, mature, loading, and stale/error states. The audit corrected
persona-wide fake facts, fabricated cold receipt DNA, maturity based on planned
trips, Discover saves counted as accepted memory, duplicate timely-return slots,
and the missing Readings entrance.

The focused visual-design pass is complete. The approved implementation source is the `Vesper Atlas.html` section titled **“Atlas Home — final state system · CANONICAL”** in the reviewed `vesper 173` bundle, plus `atlas-home-final.jsx` and `atlas-memory-final.jsx`.

Use:

- `travel-app/docs/audits/atlas-home-state-audit-2026-07-13.md`
- `travel-app/docs/surfaces/atlas-home/design-refs/vesper-173-atlas-source.md`
- `.maestro/runs/_pairs/atlas-home/after` (7/7 state captures)
- `.maestro/runs/_pairs/atlas-receipt/after`

The historical Claude Design brief is retained only as provenance. Do not reopen the section hierarchy while implementing. When older boards conflict with the final canonical section, the final section wins.

## Provenance
Built from a 2026-07-12 functional gap audit of Atlas (code+backend vs the vesper-153 design canon), the implementation cleanup through 2026-07-13, and the final `vesper 173` Atlas state-system adjudication. The composition-first "spine fold" was explored and reverted; the older Atlas Home and postcard explorations remain visible only with explicit status labels. The final `atlas-home-final.jsx` and `atlas-memory-final.jsx` boards are the pixel source of truth — this doc is the intent, map, and guardrails. **Verify current code before editing** (§0.5).
