# Code Alignment — Interaction Surfaces: Scrim-Weight Taxonomy (2026-07-08)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/vesper-interaction-surfaces-app.jsx` (+ `Vesper Interaction Surfaces.html` shell) — read-only. Scope: `components/ui/BottomSheet.tsx`, `components/ui/ConfirmDialog.tsx`.

## Context

The Interaction Surfaces canon is a large taxonomy (13 sections: overlay types, snap presets, header variants, field states, pickers, confirmation/destructive, toast, 17 domain flows, layering, migration mapping, primitive alignment, QA matrix, plus two newer additions — ConsequenceBanner and the Ask-the-organizer 403 pattern). Most of it is **already faithfully built**: `SheetHeader.tsx`, `StickySheetActionBar.tsx`, `ConsequenceBanner.tsx`, `BlockedActionRow.tsx`/`PermissionRationale.tsx` all match canon composition and copy, and are broadly adopted (`dismissOnBackdrop`/`isDirty`/`onDirtyDismiss` are wired at 15+ call sites; the "Ask the organizer" mapping table's six role-gated actions are each wired to a real screen). The two `presentationStyle="pageSheet"` raw-`Modal` uses that canon's Migration Mapping table (section 10) would otherwise flag are pre-adjudicated, in-code-documented exceptions ("H2-5 audit: sanctioned bespoke") — not fresh drift.

One real gap survives against the two files actually in scope for this pass: **the scrim-opacity taxonomy is not implemented as a taxonomy at all — it's a single hardcoded value, and that value doesn't match the codebase's own documented "standard modal backdrop" token.**

Canon (Overlay Taxonomy, section 01, and Layering Model, section 09) defines scrim weight as a deliberate signal of how blocking an overlay is, keyed to overlay class:

| Overlay class | Canon scrim |
|---|---|
| Peek sheet | 0.20 |
| Chooser sheet | 0.28 |
| Form sheet | 0.28 |
| Permission rationale | 0.28 |
| Chat-attached sheet | 0.20 |
| Center dialog | **0.40** (heaviest of the interactive-overlay set) |
| Voice overlay | 0.50 |
| Photo lightbox | 0.85 |

This is presented as a rule, not decoration — section 09's "Interaction rules" explicitly ties scrim weight to blocking behavior (dialog freezes the sheet beneath it; toast does not).

## Task 1 — BottomSheet: scrim opacity doesn't vary by `snap`, and its default isn't the app's own "standard modal backdrop" token
`components/ui/BottomSheet.tsx:123` — `backdropColor = colors.tint.photoScrim` is a single flat default (rgba(0,0,0,0.35), see `constants/colors.ts:322`) applied regardless of the `snap` prop (`peek`/`chooser`/`form`/`full`). The component already threads `snap` through to `snapFraction()` (`BottomSheet.tsx:293-306`) for height — it has everything needed to key scrim weight off the same prop but doesn't.

Separately, `constants/colors.ts:314` documents `colors.tint.modal` (0.45) as: *"Standard modal backdrop. Use everywhere a semi-transparent black veil sits behind a sheet/modal."* `BottomSheet`'s actual default (`photoScrim`, 0.35) is not that token. A grep across the app for `backdropColor=` turns up exactly one call site overriding it (`components/atlas/AtlasTimelineEntryMenu.tsx:82`, using `colors.tint.modal`) — meaning every other sheet in the app (peek, chooser, form, full alike) renders at the same 0.35 weight the primitive happens to default to, not the app's own documented standard, and with zero differentiation by snap class.

- Add a scrim-weight lookup keyed by `snap`, mirroring the existing `snapFraction()` pattern — e.g. `snapScrimOpacity(snap)`: peek/chat→0.20, chooser/form/permission→0.28 (or reuse `colors.tint.modal`≈0.45 as the more conservative single-tier fallback if a full 3-tier taxonomy is judged out of scope for this pass — flag which choice was made and why).
- `maxHeightFraction`/`scrimOpacity`/`backdropColor` explicit props must continue to win when passed (existing override precedence at `BottomSheet.tsx:135-140` — extend the same pattern for scrim).
- Do not change any call site's explicit `scrimOpacity`/`backdropColor` (e.g. `AddExpenseSheet.tsx:700`, `EditExpenseSheet.tsx:220` pass `scrimOpacity={0.35}` deliberately) — only change the *default* used when neither is passed.

## Task 2 — ConfirmDialog: scrim is the lightest in the system, not the heaviest
`components/ui/ConfirmDialog.tsx:106` — `backgroundColor: colors.tint.overlay` (rgba(0,0,0,0.3), `constants/colors.ts:310`). Canon's Center Dialog row is the single most blocking overlay class defined (0.40 — heavier than every sheet snap, and the only overlay type with "Scrim dismiss forbidden" + "Nav: Disabled"). The current value (0.30) is lighter than several sheet call sites already use for less-blocking overlays (e.g. `AddExpenseSheet`'s form sheet at 0.35), inverting the intended hierarchy where the fully-blocking, no-scrim-dismiss dialog should read as visually heaviest.
- Swap `ConfirmDialog`'s backdrop to `colors.tint.modal` (0.45) or add a dedicated dialog-scrim token at 0.40 to match canon exactly — pick one and document the choice in a comment (the existing "Standard modal backdrop" comment on `colors.tint.modal` suggests that token was already intended for this use and just wasn't applied here).
- No dismiss-affordance change needed — `ConfirmDialog` already correctly has no backdrop-press-to-dismiss (canon: "Cancel button only"), this task is scrim-value only.

## Explicitly not in scope (verified already aligned or already adjudicated)
- Snap-preset height fractions (`peek`=0.34, `chooser`=0.58, `form`=0.82, `full`=0.94) — canon's pixel examples are drawn on a fixed-height mockup canvas, not directly comparable to screen-fraction values; no mismatch found.
- Missing 5th `full-screen-edit` snap variant on `BottomSheetSnap` — the two real full-screen-edit-class flows in the app (`FindPhotosSheet.tsx`, `ProposalDetailScreen.tsx`) already use a documented, pre-adjudicated bespoke `Modal`+`pageSheet` exception ("H2-5 audit"), not silent drift. Not re-litigating that call here.
- `ConfirmDialog`'s typed-confirmation mismatch has no red-border/error-state feedback (canon's `Field` shows oxblood border on error) — real but sub-cosmetic; primary button already correctly stays disabled until the string matches. Judged too minor to warrant a task; flagging here only so it isn't silently lost.
- `SheetHeader`, `StickySheetActionBar`, `ConsequenceBanner`, `BlockedActionRow`/`PermissionRationale` (Ask-the-organizer + permission rationale patterns) — all checked against canon sections 03/06/09/13b/13c and found faithful in composition, copy, and state handling.
- No backend-gated fields found in this surface — scrim opacity and dialog chrome are pure frontend design tokens, nothing here requires flagging as BE-gated.

## Done
BottomSheet's default scrim opacity varies by `snap` (or documented single-tier decision) instead of one flat hardcoded value · ConfirmDialog's scrim uses the heaviest/standard-modal token instead of the lightest value in the system · both changes preserve existing explicit-prop overrides at every call site · typecheck + tests green · report which scrim tiering approach was chosen (full 3-tier vs. single conservative default) and why.

---

**Standing rules:** git status first (branch from `main` — note: repo currently sits on `design-align/costs` with uncommitted changes; branch a fresh one from `main`, don't stack on that WIP) · one commit per task · typecheck + tests green · no push without approval · flag backend-gated items, don't fake data (none applicable to this brief).
