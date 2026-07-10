# Code Alignment — Batch CC1: Atom Adoption (2026-07-09)

Repo: `~/travel-workspace/travel-app`. Design canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only mirror of handoff 125 — implement FROM it, never edit it). Source ledger: `design/component-consistency-audit-2026-07-09.md`, family **atoms**. This batch is pure **adoption**: the shared primitives already exist (`ui/Button`, `ui/Badge`, `ui/Avatar`, `ui/SheetHeader` handle) — the drift is that golden-path surfaces re-type them. No new primitives.

## Standing rules (all CC batches)
1. `git status` first; other sessions may have WIP — branch from main, don't touch unrelated WIP.
2. **Snap rule:** match the canon's structure/metrics intent, but snap every color/size/font to existing app tokens. Never copy raw hex/px from canon jsx. If a canon value has no token, flag it in your report instead of inventing one.
3. One commit per task; typecheck + tests green after each; grep for dangling refs; update any touched FEATURE.md.
4. **CC0 — do this before Task 1 and commit it alone:** the fontSize and border-radius CI ratchets are currently RED on main (`scripts/check-typography-budget.mjs`, `scripts/check-border-radius-budget.mjs`). Re-green them first so this batch's changes don't leak more violations. If a ratchet is red because a *baseline* is stale (not a real new violation), lower the baseline and note it.
5. Do NOT push without user approval.

## Task CC1.1 — VBtn adoption on golden-path CTAs  ·  severity HIGH
Canon: `buttons.jsx:20-48` + Component Consolidation Audit §01 VBtn (one pill: r22/h44, `primary/ghost/amber/destructive/sage` variant map). Code: `components/ui/Button.tsx` is a real single source but only ~14 importers; primary CTAs are hand-rolled with **four different corner radii**. Migrate these onto `ui/Button` (add missing metric props rather than forking):
- `components/trip-plan/ConflictResolutionSheet.tsx:379-384` ("Fix it", radius 8)
- `components/trip-plan/PlanEmptyDay.tsx:370-378` ("Add", radius.full)
- `components/voice/MicPrivacyDisclosure.tsx:295-301` ("Got it", radius.input 20)
- `components/discover/reader/ReaderFooterActions.tsx:148-156` (radius.md)
- Then sweep the rest of `trip-plan/`, `voice/`, `discover/reader/` for local `btn`/`button` StyleSheet CTAs and adopt. Keep genuinely different species out (icon buttons, booking tone-pills — see CC2).
Report the before/after count of files with local button styles (this becomes a ratchet in CC4).

## Task CC1.2 — Status pill unification (Proposal Detail + Trip Settings)  ·  severity HIGH
Canon: `status-pill.jsx` + Consolidation Audit §01 VStatusPill — the two surfaces were merged onto one shell (h22/r11, 11px 600 sans); only the status→color map stays per-surface. Code hand-rolls two divergent shells and ignores `ui/Badge` (which exists to end one-off badges, 4 importers):
- `components/trip/proposal-detail/ProposalDetailScreen.tsx:636-662,1164-1172` (local `StatusPill`, minHeight 24, radius.chip 16)
- `components/trip-settings/TripSettingsKit.tsx:44-51,295-315` (local `TripStatusPill`, minHeight 28, radius.full, leading dot)
Build: pick one shell — extend `ui/Badge` with a tinted status variant at canon metrics (h22/r11) OR add a `StatusPill` to `ui/` — migrate both, keeping per-surface tone maps. **Record** whether the trip-settings leading dot is a sanctioned add-on or drops.

## Task CC1.3 — Collapse the two avatar cores  ·  severity MEDIUM
Canon: `avatar.jsx:7-16` — ONE monogram core; per-surface markers (vote badge, pending ring, sparkle) layer around it. Code has two cores that render the same person differently: `components/ui/Avatar.tsx` (1-char initial via `utils/avatarColor`) and `components/people/PeopleAvatar.tsx` (2-char via `constants/peopleCollaboration`). Color seeding is already unified (good) — the split is the initials function + text. Collapse onto one core (recommend `PeopleAvatar` as the survivor since it carries the marker layer), one initials function, markers as the add-on layer.
**Depends on D8 decision only for the sparkle glyph** — do the core-collapse now regardless; wire the final glyph in CC3. Serif-vs-sans monogram text: canon says serif, code is uniformly sans — leave sans and note it in your report as a likely-deliberate RN legibility call for the human to ratify (do NOT flip it blind).

## Task CC1.4 — Sheet-handle mop-up  ·  severity MEDIUM
Canon: `sheet-atoms.jsx:6-8` VHandle 36×4 r2, one source. `ui/SheetHeader` already renders it (21 importers), but 5+ sheets re-type it locally with width drift (one at 38px). Point them at `SheetHeader`'s handle (or extract a tiny `SheetHandle` if a sheet can't take the full header). Sites include `components/expense/ExpenseDetail*`, `components/people/MemberActionSheet*`, voice sheets — grep `width: 3` + `height: 4` in sheet components. (Overlaps CC4 Task 4.1; do whichever batch reaches them first, don't double-fix.)

## Task CC1.5 — Restore the Auth 52px CTA exception  ·  severity MEDIUM
Canon: Consolidation Audit records Auth `PrimaryButton` (52px CTA + spinner) as a **deliberate exception** — kept separate on purpose. Code flattened it the wrong way: auth now uses the shared 44px `ui/Button`. Restore the 52px auth CTA as its sanctioned local variant (or a `size="auth"` prop on `ui/Button` if cleaner). This is the one place the canon wants MORE separation, not less.

## Done
CC0 ratchets green · primary CTAs on one Button with one radius · both status pills on one shell · one avatar core · handles on the shared source · auth 52px restored · report lists: local-button file count before/after, any canon values with no token, the serif-monogram question flagged for the human.
