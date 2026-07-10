---
doc_type: archive
status: archived
archived: 2026-07-09
owner: founder / engineering
created: 2026-07-09
why_new: Preserve the complete source after its durable content was consolidated into an authoritative owner.
---

# Atlas — User Journeys (2026-07-06)

> Archived 2026-07-09 after the two Atlas subspines were consolidated into canonical Journey 11.

Traced from live code (`main`, both repos) + the design canon (`atlas-memory-composition-vision 23`). Companion to the full-stack architecture trace in memory (`atlas-canon-state`).

## The vision (grounding)

Atlas is the app's **retrospective memory surface** — the counterpart to Discover. Discover is prospective ("what's worth my attention here?"); Atlas is retrospective ("what has my life in places become?"). Doctrine:

- **A private memory instrument, not a dashboard.**
- **Opens with meaning, not input.** "If Atlas opens on a blank field, the design has failed."
- **Evidence-first, never confident inference.** "Never say 'you are a water person.' Always say 'water keeps appearing · 14 shores.'" Never a confidence score in the UI.
- **Memory Truth Rules:** a suggestion is not a visit; a planned item is not a memory until confirmed; a receipt confirms presence, not salience; **user correction overrides all inference.**
- **Honest thin states:** thin material becomes an honest list ("more of a list than a story"), never a faked reading.
- **The loop:** Ask → Compose → Rearrange → Keep → return via living views that recompose over time.

## The two spines (the key structural fact)

Atlas runs on two nearly-separate pipelines that only touch via a name-match:

- **Read spine** — composing/steering *readings* over your taste graph (`traveler_place_affinity`). Live, affinity-backed, live-LLM-or-grounded copy, real riso art.
- **Memory spine** — turning photos into kept *artifacts/postcards* (`atlas_artifacts` blob). Mock composer by default (`ATLAS_LLM_ENABLED` dark).

**They barely meet:** completing a trip / keeping memories does not visibly enrich readings — the only link is a +0.05 `artifact_presence` name-match tie-breaker on `kept` artifacts. Closing that seam is the deferred "L-move."

## Entry points (verified)

| From | Lands on | Route |
|---|---|---|
| Atlas tab (4th) | Composed home | `(tabs)/atlas` — primary |
| Trips home "work card" | Latest artifact / pending candidate / postcards | `openAtlasWork` |
| Concierge home | An artifact | `atlasArtifact` |
| Trip chat "add memories" | Scan flow | `atlasScan` |
| Memory screen | Receipt | `atlasReceipt` |
| Notifications | Long View (time) / Unpacked(year) | both pushes **dark** |
| Deep links | Any Atlas route | registered in `_layout` |

---

## SPINE 1 — The Read spine

### J1 · Cold start (new user, zero memories)
- **Entry:** opens Atlas tab, no affinity data.
- **System:** `register:'empty'` → home hero degrades to "a reading is gathering"; empty board = *"It will not invent a board before there is a shape."*
- **Two doors:** Compose a view (→ aperture) · Saved places (→ scan/saved).
- **Exit:** aperture (J3) or scan (J6). Honest "nothing to fake yet" state.

### J2 · Lean-back read (dominant journey)
- **Entry:** opens Atlas tab, has memories.
- **Actions (passive):** Featured Reading hero (evidence line + read line + 3-plate compression; live copy, real art) → scroll past On This Day, Starting Points, Discovery Reflection, Loved Places, Ways Back In strip, Long View doorway, Desk postcard.
- **Decision:** stop (most sessions) or tap "Open this reading →".
- **Exit:** full `board.tsx` screen (J4), or leave having read.

### J3 · Aperture / compose (active)
- **Entry:** aperture / "Compose a view" (`/atlas/compose`).
- **Actions:** type "Show me… bowls and soup, any city, since 2024" → `POST /parse` → editable facet chips (LLM-first, deterministic fallback) → edit chips (each re-composes preview) → "Compose this view" → `board` reading (J4).
- **Honest-fail:** no match → "Nothing matched '…'. Atlas builds from places you've kept."
- **Exit:** composed reading, or back.

### J4 · Reading & steering (core interaction)
- **Entry:** a `board` reading open (J2/J3/J5).
- **Arrangement switch** (`BoardModeStrip`): Read (editorial + Vesper prose) / Time (chronological rail) / Places (relational pseudo-map, honestly labeled) / Reel (→ J-Reel). Same moments, zero refetch.
- **Moment Actions** (long-press any plate, one primitive across arrangements): Why this is here (grounded receipt, no score) · Hide (→ `exclude_ids`, local pulse, live count) · Pin/Unpin (→ `pin_ids`, glyph) · This isn't right (optimistic exclude + server dispute).
- **Keep** — saves the living query with current exclude/pin state.
- **Decision points:** hide that empties → honest thin-fallback `list`; unresolvable pin → `dropped_pins` toast.
- **Exit:** Keep (→ J5) or leave; steering persists only if kept.

### J5 · Return to a kept view (Ways Back In)
- **Entry:** home "Ways Back In" strip card, or `/atlas/boards`.
- **Actions:** kept view **recomposes live** (may show new moments; freshness shown) → re-enter J4; a different hide/pin state saves as a *new* kept view, not an overwrite.
- **Exit:** browse, or re-steered reading.

### J-Reel · Immersive playback
- **Entry:** Reel from mode strip → full-screen `AtlasBoardReel` (same moments, Ken Burns riso frames, Wrapped-style ticks; Reduce-Motion static).
- **Exit:** back to reading.

---

## SPINE 2 — The Memory spine (photos → kept artifacts)

Runs on the blob pipeline; mock composer by default.

### J6 · Manual scan
- **Entry:** `/atlas/scan` (home add, Long View, inbox, trip chat "add memories").
- **Actions:** grant photos → `clusterPhotos` client-side (min 15/cluster) → `geocodeClustered` → submit `atlas_candidates` (opaque IDs + centroids only; **photos never leave the device**) → inbox (J8).

### J7 · Auto-candidate (dark)
- **Entry:** none — daily `trip_lifecycle` fires `trip.completed` (when end date passes) → auto-candidate subscriber + backfill loop. **Dark** (`ATLAS_AUTO_CANDIDATE_ENABLED`).
- **When lit:** the magic "your trip became memories" moment via the home **Inbox nudge**. Today requires manual scan.

### J8 · Review & keep
- **Entry:** Inbox / home nudge.
- **Actions:** review clustered candidates → dismiss, or open candidate detail ("draft on your desk"), or Keep-all. **Approve** composes an artifact (*mock copy unless `ATLAS_LLM_ENABLED`*) + `derived_signals`.
- **State trap:** single approve → `state='composed'`; only Keep-all + background job → `state='kept'`; only `kept` nudges taste-board significance.
- **Exit:** kept artifact (→ Trips work-card, Concierge, postcards); `learned/[id]` shows "what this taught Vesper." Signal→Personal-Memory bridge **dark**.

---

## SUPPORTING journeys

### J9 · Browse the whole corpus (Long View)
- **Entry:** home "Since {year} · The whole Atlas →" doorway, or notification.
- **Index register** (flat, no Vesper voice): Time (year chapters → drill) / Places (city nodes → drill) / People+Theme inactive "SOON". Separate timeline pipeline — counts entries, doesn't compose.

### J10 · Recap (Unpacked)
- **Entry:** Almanac/Long View footer with a year, or seasonal push (**dark**). Swipeable "Wrapped" year deck. Share `STORY_SHARE_ENABLED`-gated (**dark**).

### J11 · Re-engagement (all dark)
- On This Day strip renders, but anniversary push dark. Unpacked seasonal dark. **Atlas is a place you visit, not one that calls you back.**

### J12 · Correction & privacy
- **Entry:** J4's "This isn't right," Learning Signal "Is this right?", or Receipt.
- **Actions:** dispute → `user_state='disputed'` (suppressed); forget; hide → `removed.tsx`; Receipt shows "what Vesper knows." Corrections honored in future compositions.

---

## Two punchlines

1. **The two spines barely meet.** Keeping trip memories doesn't visibly enrich readings. A user who diligently curates photos won't *feel* their taste-board get richer — only the +0.05 name-match. Closing this is the journey-level reason the L-move matters.
2. **Re-engagement is all dark.** For a retrospective surface whose value compounds over time, the biggest unflipped activation lever is the set of cadence pushes (On This Day, seasonal) — a flag decision, not engineering.

---

# Staff-PM Analysis (2026-07-06)

3-agent audit of code vs. design canon vs. vision; every P0/P1 headline hand-verified. **The interaction grammar is strong and canon-faithful where built** — Moment Actions work identically across all arrangements, "why this is here" is evidence-first with zero confidence scores anywhere, thin material honestly degrades to a list, kept views reopen live. The problems are (a) two honesty-violating bugs, (b) required canon components simply unbuilt, (c) a memory flywheel that's dark or nonexistent, and (d) design-polish rulings (Atlas handoffs 18–21) that mostly never reached code.

## P0 — Dogfood-blockers / journey-breakers

1. **Mock prose ships as authored "VESPER WROTE."** With `ATLAS_LLM_ENABLED` off (default), every single-approve produces generic mock copy (`composer.py:181-203`) rendered under a gold "VESPER WROTE" eyebrow (`artifact/[id].tsx:217`) with a "· kept by Vesper" header (`:185`); the only honesty badge is `__DEV__`-gated (`:187`), invisible in release. **Directly violates "never fake a story."** The single clearest Memory-spine blocker.
2. **Recompose is a full-screen reload, not a local pulse.** `useData` has no `keepPreviousData`, so every Hide/Pin/Dispute changes the query key → `isLoading` true → `board.tsx:305` swaps to a "Making your reading" spinner. The `isRecomposing` 0.55 dim only fires in mock mode. An in-code comment falsely claims compliance. Breaks the core steer→recompose feel. **Fix: `keepPreviousData`/`placeholderData` on the board query.**
3. **J7 auto-candidate is unbuilt (not dark).** `lifecycle.py:832` imports `backend.atlas.trip_candidate_backfill` — the module doesn't exist; no `trip.completed → candidate` subscriber exists. The "your trip became memories automatically" moment does not exist; users must manually re-scan forever, while the empty-inbox copy implies auto-surfacing.
4. **Learning Signal home module unbuilt.** `buildAtlasLearningSignal` is orphaned (0 importers). The pattern-level "Atlas is learning · Water keeps appearing · Is this right?" correction loop — a required canon P0 component and the primary evidence-first trust mechanism — is absent from the home. (Moment-level "This isn't right" exists.)

## P1 — Real friction / vision violations

5. **The kept/composed state trap.** Careful single-keep writes `state='composed'` (taste-**inert**); bulk "Keep all" writes `state='kept'` (taste-active); the UI universally says "kept." The careful path is silently the weaker one. Inverted, invisible, taste-corrupting.
6. **The seam: keeping memories doesn't enrich readings.** The Memory→Read link is one 0.05 name-match tie-breaker on `kept` artifacts (`significance.py:90`); it only re-orders, never adds, and `signal_memory.py` (which would close the loop) is dark. Breaks the "keep grows readings" thesis. Smallest fix: flip `ATLAS_SIGNALS_TO_MEMORY` so a kept place can *enter* a group, not just reorder within one.
7. **Opaque PHAsset photo IDs die on device change/reinstall.** No rehost of scanned photos, no warning — every artifact's imagery silently breaks to a placeholder. Fatal longevity risk for a keepsake product.
8. **Dispute/forget scopes Atlas readings only, not Discover/home** (`atlas.py:2118`, documented as intentional) — but the canon says "correction = permanent override." A forgotten place still drives Discover recs. Trust bug against the surveillance lesson.
9. **Long View silently under-counts "the whole corpus."** `count_timeline_entries_grouped` uses an unordered `.limit(2000)` (nondeterministic counts across refetches) and the FE ignores the `truncated` flag. Undated bucket drills to `year:0` → 422 dead-end.
10. **On This Day push deep-links to the generic index,** not the named memory (`notificationDestination.ts:70` vs the correct per-item route in `AtlasOnThisDay.tsx:29`). Will tank tap-through when the flag flips.
11. **Provenance glyphs (○◑●◎) absent everywhere** — structural: `AtlasBoardMoment` has no `provenance` field, so the evidence-state vocabulary the entire canon rests on never reaches a plate, in any mode or the hero.
12. **Ways Back In flattens all freshness to a static "LIVE" badge** (`boards.tsx:211`) — the canon's live/updated/active/thin distinction can't surface; the "living view" is honest that it reopens live but can't show *what changed*.
13. **Design-polish drift:** home hero shows a redundant Keep button (violates Polish-1's single-CTA ruling); cold home renders a decorative fake-tile "signal grid" (violates honest-absence); compose shows an `ASK ATLAS` label (violates the naming canon's explicit "avoid Ask/Ask Atlas"); Reel navigates away instead of being an in-place arrangement.
14. **Gift/full-scan bypasses consent.** The highest-confidence candidate is auto-approved server-side before the user opens it (`scan.tsx:426`); full-scan (the recommended path) skips the trust-contract screen. Breaks "nothing enters the record until you tap."

## The two systemic verdicts

**The flywheel is off.** All three re-engagement loops (anniversary, seasonal, auto-candidate) are dark or unbuilt, so Atlas — a surface whose entire value *compounds over time* — never calls users back. On This Day only appears if you already opened the tab. For a retrospective product this is the single highest-leverage gap, and it's part flag-flip (anniversary/seasonal, though On This Day routing is also broken) and part real build (auto-candidate).

**The instrument is beautiful; the loop is broken.** Atlas nails the *lean-forward* moment — ask, compose, steer, keep — with genuinely canon-faithful, evidence-first interaction. What it doesn't yet deliver is the *reciprocal* promise: that keeping memories visibly grows your Atlas, and that your Atlas reaches back out to you. Both the seam (#6) and the dark flywheel are the same underlying gap — the memory you put in doesn't come back to find you.

## FE optimization backlog (P2)
No virtualization on Time/List layouts or the inbox (all `.map` in a ScrollView); synchronous main-thread photo clustering on the full library (multi-second stall at 20k photos); ~7 parallel home hooks + refetch-on-every-focus; Reel refetches an already-resolved composition; unmemoized per-render computes on mode switch; no reserved-aspect crossfade when a real photo replaces a riso plate (layout-shift risk).
