# Code Alignment — Atlas Batch E: Polish-to-Canon + Perf (2026-07-06)

Repos: `~/travel-workspace/travel-app` (FE mostly; one BE contract change in E1). Branch main. Follows A+B+C+D. Theme: the code catches up to the Atlas design-polish rulings (handoffs 18–21) that never reached implementation, plus the P2 FE-perf backlog. From the PM journey audit (docs/atlas/atlas-user-journeys-2026-07-06.md).

Process: `git status` first. Branch from main. One commit per logical group. No push without approval. After each: `tsc` + FULL `TZ=UTC npx jest` / BE `pytest`+`mypy` (E1 only). Ground in the design canon `~/Downloads/atlas-memory-composition-vision 23`.

---

## E1 — Provenance glyphs (○ first · ◑ returned · ● kept · ◎ now) reach the plates

**Gap (structural):** the entire canon's evidence-state vocabulary (§12/§12.5) never renders — because `AtlasBoardMoment` (`types/atlas.ts:288-300`) has **no `provenance` field**. `AtlasEvidencePlate` (`AtlasEvidencePlate.tsx:34-43`) shows place + year only. Every plate, hero, and arrangement is missing the glyph the whole memory-spine doctrine is built on.

**Fix:**
- BE: add a per-moment provenance field to the composition `moment` output — the evidence-state (first/returned/kept/now) computable from the affinity row's `first_seen_at`/`last_signal_at` + kept-artifact match (the same signals significance already reads). Keep it a small enum, NOT a confidence score.
- FE: add `provenance` to `AtlasBoardMoment`, render the matched glyph on every plate (ComposedMomentTile, MomentCard, TimelineMomentRow, MapMomentNode) and the hero evidence plate, at the canon size/weight (Polish-3 unified the glyph vocabulary — ○ open ring for "first", matched weights).
- Honest absence: no provenance data → no glyph (never a fabricated state).
- Tests: glyph renders per state; absent when no data.

## E2 — Ways Back In freshness states (not a static "LIVE")

**Gap:** every kept row renders a hardcoded `LIVE` badge + "updates live" (`boards.tsx:210-214`, home `index.tsx:605`) regardless of actual state. Canon §6 defines four: ● live / ↑ updated / active / thin. The `AtlasSavedBoard` shape carries no `status`/`updated`/`isLive` distinction, so "updated since kept" and "thin" can never surface — the Impl-Spec's "saved views becoming static folders" risk.

**Fix:**
- BE: the kept-board read (`atlas_threads`) should compute a freshness state — compare the board's current recompose against `lastComposedAt`/last-seen to detect "updated" (new moments since kept) vs "live" (unchanged) vs "thin" (dropped below board threshold).
- FE: render the four-state legend per row (canon §6) instead of the static LIVE.
- Tests: a kept view with new matching moments shows "updated"; unchanged shows "live"; degraded shows "thin".

## E3 — Home + compose polish (Polish-1/naming rulings)

Small FE alignments to already-decided canon rulings:
- **Hero single CTA:** remove the redundant Keep button from `AtlasHomeBoardHero.tsx:90-107` — canon Polish-1 ruling 02 is "one CTA on the hero: Open this reading → only; Keep moves inside the opened reading" (Keep already exists inside the reading). Remove `onKeep`/`keepHeroBoard` wiring from the host (`index.tsx:216-231,466`).
- **Cold-state honest absence:** remove the decorative 4-tile "signal grid" (`compositionSignalGrid`, `index.tsx:732-737`) — canon §10 forbids empty/ornamental tiles in cold state; render honest absence per canon Variant B ("One trip in. Still gathering.").
- **ASK label:** replace the `ASK ATLAS` sub-label in compose (`compose.tsx:199`) — canon "avoid in UI" lists "Ask / Ask Atlas" explicitly. The eyebrow `ATLAS · COMPOSE` (190) is correct; drop/rename the ASK sub-label.
- **Quiet/thin home states:** add the missing canon Variant C ("Nothing new needs ceremony" → last reading quietly) and Variant D (thin) home treatments (currently everything non-ready falls to "A reading is gathering"). Optional if time; note if deferred.

## E4 — Reel as an in-place arrangement (or record the divergence)

**Gap:** Reel is `active={false}` always and `router.push`es to a separate screen (`AtlasTasteBoard.tsx:683-697`, `board.tsx:259-284`), and re-fetches an already-resolved composition (`reel.tsx:54-55`). Canon: Read/Time/Places/Reel are "different views of the same memory set," not a nav-away.

**Fix (pick one, record the call):** either (a) make Reel an in-place `viewMode` like Time/Places (no refetch, no nav) — truest to canon; or (b) if the full-screen immersive player genuinely needs its own screen, at minimum pass the already-resolved board to it (kill the refetch + the ReelBridge double-load) and record that Reel-as-route is an accepted divergence. Recommend (b)-with-no-refetch as the pragmatic call; (a) if the in-place immersive works.

## E5 — FE performance (P2)

- **Virtualization:** Time and List layouts render all moments via `.map` in the parent ScrollView (`AtlasTasteBoard.tsx:1591-1596,785-793`); the inbox likewise (`inbox.tsx:166-238`, `AtlasInboxReview.tsx:87`). Convert the unbounded lists to `FlatList` windowing. (Composed/Places self-cap at 5/6 — leave.)
- **Main-thread clustering:** `clusterPhotos` (`utils/atlasCluster.ts:86`) runs synchronously over the full library on the JS thread — multi-second stall at 20k photos. Chunk via `InteractionManager`/batched yields so the `ScanProgressCard` animates and the UI stays responsive.
- **Home hook churn:** the Atlas home fires ~7 parallel hooks + `useFocusEffect` refetch-on-every-focus (`index.tsx:121-133`). Audit for redundant refetches; gate the focus refetch behind a staleness check.
- **Unmemoized computes:** `firstDivable`, `boardSubtitle`, `mapSummary` (`AtlasTasteBoard.tsx:462,619-639,1002-1007`) recompute every render/mode-switch — memoize.
- **Image crossfade:** no reserved-aspect crossfade when a real photo replaces a riso plate (`RisoSlotImage`/`AtlasEvidencePlate`) — canon §12.5 "no re-layout, no flash." Add a reserved-aspect placeholder + fade.

---

## Explicitly OUT of Batch E
- Anything requiring the moment-store L-move. Re-engagement flag flips. The seam affinity-edge (Batch C).

## Definition of done
E1: provenance glyphs render per state on all plates + hero, honest absence, contract added. E2: four freshness states on kept rows. E3: hero single-CTA, honest cold state, no ASK label (Variant C/D optional). E4: Reel no longer double-fetches (in-place, or route-with-passed-board + recorded divergence). E5: Time/List/inbox virtualized, clustering off the main thread, home refetch churn reduced, key computes memoized, image crossfade. Green tsc + FE jest (full) + BE pytest/mypy (E1/E2). Report: the E4 call, and any E3 Variant C/D deferral.
