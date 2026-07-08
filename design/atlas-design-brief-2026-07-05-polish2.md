# Atlas Design Canon — Polish Session 2: Time Mode + Moment Grammar (2026-07-05)

Scope: five items. Two are fixes to Polish Session 1 (a visual reversal + residual bugs), one syncs the Implementation Spec (which coding agents read FIRST — unsynced rulings get missed), and two are new: a genuine revision of the weakest screen in the file, and a moment-level interaction grammar that doesn't exist anywhere yet but is required for the "decompose and rearrange" thesis to be real, not just written.

Working set: `Atlas - Canonical Experience Board.dc.html` (primary), `Atlas Implementation Spec.dc.html` (v6).

Governance rule: same as Polish 1 — every ruling gets a dated entry in the §13 Rulings Log, and any contract change gets mirrored into the Implementation Spec in the same pass (this was skipped for two of Polish 1's rulings — catch those up here too, see item 3).

---

## 1. REVERSAL — Time mode gets the flat-material treatment (not a signature texture)

Polish Session 1 ruled that the polaroid-stack-with-drop-shadow treatment on Timeline should be RESERVED as the Time-mode signature. On reflection, that ruling was wrong, and this item reverses it.

Why: the polaroid stacks are the only skeuomorphic object in an otherwise flat, editorial, hairline-bordered system. They don't read as an intentional signature — they read as a screen imported from a different app. The "analog warmth" instinct (which is real and validated — see Spotify Wrapped 2025 going scrapbook/analog and winning) should be expressed through TONE and COPY, not through literal tilted-photo skeuomorphism.

Do:
- Replace the tilted polaroid stacks with the same flat woven-plate material used everywhere else in Atlas (home mosaic, board plates) — square corners or the app's standard small radius, hairline border, no drop shadow (or at most the same subtle lift Board plates use).
- **Fix the beat rhythm**: every beat gets the same fixed height regardless of photo count (1 photo, 2 photos, or 3 photos all occupy the same footprint — extra photos become a small `+N` overlap chip on the lead plate, not a taller stack).
- **Promote the sentence over the metadata**: the serif memory sentence ("A ramen counter you ducked into out of the rain") becomes the visually dominant line; the mono metadata line (`FIRST · TOKYO · '24 · 3`) drops in size/weight below it — the memory is the content, the metadata is the footnote.
- **Anchor the provenance glyphs to the rail, larger.** The ○ first · ◑ returned · ● kept · ◎ now glyphs currently float small and disconnected. Make the glyph itself sit ON the rail at a size where it reads as the spine's actual joint — each beat visually hangs off its glyph, not beside it.
- Give the left plate column less width relative to the caption column — the plates are supporting evidence, not the headline.
- Update §13: date this as a reversal of the [Polish 1 date] ruling, with the one-line reason above.

## 2. Fix the two Polish-1 render collisions

Two visual bugs from the last export, both simple layout fixes:
- **Home screen, "Ways back in" list**: rows are overlapping near the bottom of the list (the "markets with Maya" row and the "Atlas is learning" module collide — text from one bleeds into the other). Add proper vertical spacing/clearance between the last list row and the learning-signal module below it.
- **Compose flow, consent line**: the permanent consent sentence at the foot of the dark sheet ("Nothing is analyzed until you ask. Nothing leaves Atlas unless you share it.") is rendering garbled/overlapping with adjacent text. Give it its own clear line with adequate top margin, smallest permitted mono/caption size per the microtype floor from Polish 1.

## 3. Sync the Implementation Spec (catch-up from Polish 1)

Three Polish-1 rulings changed contracts but were not mirrored into the Impl Spec, which is the primary document coding agents read. Fix in this pass:
- **Keep state machine**: Impl Spec still needs its Keep description updated to match the canonical board — Keep is invoked FROM WITHIN an opened reading, not from the home hero. Confirm/update the `aperture.closed → ... → ready` state table and the P0 component list accordingly.
- **`matchedCounts` on compose.heard**: add the live matched-evidence count (e.g. "41 moments · 6 places · 2 years match") to the `compose.heard` data contract in §7, matching what's now drawn on the canonical board.
- **Material-per-state note**: add one line to §7 stating the compose flow's dark-sheet-until-ready material assignment (input + heard on dark; cream returns only at `ready`), so an implementing agent doesn't default to alternating materials per state.
- Also timestamp/date the `compose.finding_shape`-stays-cream decision if it isn't already dated in §13 (confirm during this pass; add the date if missing).

## 4. NEW — Moment-level interaction grammar (long-press on any moment)

This is new ground: nothing in the file today lets a user act on a SINGLE moment inside a reading — only whole-reading actions (Keep/Steer/Dismiss) exist. Per Atlas's own doctrine ("user correction overrides all inference" — Memory Truth Rule) and the pattern that killed Google's Ask Photos (users need to see AND correct what was matched), a per-moment control is required, not optional polish.

Draw one small board, "Moment Actions":
- **Trigger**: long-press (or a small affordance revealed on tap) on any single moment/plate inside an opened reading — works the same in Read, Time, and Places arrangements (design it once against the shared plate primitive, not per-mode).
- **The sheet** (small, Interaction-Surfaces-style bottom sheet): four actions —
  - **Why this is here** — shows the moment's evidence line in plain language (e.g. "Receipt confirmed · Aug 2025 · matched 'bowls & soup'"). This is the provenance-on-demand pattern; keep it one line, evidence-first per doctrine (never a confidence score, never " 87% match").
  - **Hide from this view** — removes the moment from THIS composed reading only, recomposes immediately (small transition, not a full reload), and the reading's evidence count updates live (echoing the heard-screen's matched-count pattern from item 3).
  - **Pin to this view** — the inverse: locks the moment in even if future recompositions would drop it (a small pin glyph appears on the plate afterward).
  - **This isn't right** — routes to the same correction/dispute pattern as the existing Learning Signal ("Is this right?" — reuse that component, don't invent a new one), and per doctrine, a correction here suppresses this moment from ALL future compositions, not just this one.
- **Empty consequence state**: if hiding a moment empties the reading below the honest-composition threshold, fall through to the existing `compose.thin` "This is more of a list than a story" state rather than showing a broken/empty reading.
- Record ownership in §13 and add the four actions + the fall-through rule to the Impl Spec's component list (§8).

## 5. Small — visible "recompose in progress" micro-state

Related to item 4: since Hide/Pin now trigger live recomposition inside an open reading (not just at the top-level compose flow), add one small transition treatment — a brief, quiet loading pulse on the affected plate(s) only (not a full-screen loader), so the moment-level action feels immediate and local rather than triggering a jarring full reload. One small annotated frame, not a full state board — this piggybacks on the existing State System vocabulary (reference it, don't invent a new loading treatment).

---

## Explicitly OUT of this session

- The true moment-store migration (backend), the DNA-vs-doctrine adjudication, `/your-map`/`/dna-card`, and the 36-route ownership table remain separate sessions.
- No new arrangement modes beyond Read/Time/Places/Reel.
- Don't touch Board, Compose.input/ready, or Ways Back In — those are settled from Polish 1.

## Definition of done

Time mode uses flat plates + fixed beat rhythm + promoted sentence + rail-anchored glyphs, ruling dated as a reversal · both render collisions fixed · Impl Spec §7/§8 synced with Polish 1 + this session's contracts · Moment Actions sheet drawn once and shown working across Read/Time/Places · thin-fallback and recompose-pulse states covered · export a fresh handoff.
