# Code Alignment Brief — Close Polish Family Gaps (2026-07-12)

**Status:** G1–G4 implemented on feature branches · G5 bookkeeping done · **device dogfood still open**  
**Scope:** `travel-app` leftovers after header geometry (#66), StatusPill (#67), Sheets/handles (#68), Buttons reader CTA (#69), Glass chrome 0–2 (#70)  
**Canon:** `~/Downloads/vesper 146/project/` + prior briefs under `design/code-alignment-brief-2026-07-11-*.md`  
**Repo state:** work from `origin/main`; pathspec commits only (local trees are dirty with concurrent WIP)

### Branch tips (pre-merge)

| PR | Branch | SHA |
|---|---|---|
| G1 | `polish/g1-local-button-budget` | `087523ed` |
| G2 | `polish/g2-glass-phase-5` | `55ad981c` |
| G3 | `polish/g3-status-pill-hygiene` | `d6fb7f0b` |
| G4 | `polish/g4-sheet-handle-ratchet` | `7817423a` |

Refresh `design/surface-manifest.yaml` `code_verified_at` values to squash-merge SHAs after landing.

---

## TL;DR

Primitives are mostly good. Remaining debt is **adoption + hardening**, not redesign.

Close gaps in **five landable PRs**. Do not open a sixth mega-pass.

| PR | Track | Goal | Size | Risk |
|---|---|---|---|---|
| **G1** | Buttons | Clear local-button budget → 0 (or documented exceptions) | M | Low–med |
| **G2** | Headers/glass | Phase 5: component-level back chrome + guard expand | S–M | Med (visual) |
| **G3** | StatusPill hygiene | Rename wrapper + adoption ratchet | S | Low |
| **G4** | Sheets | Handle ratchet + 1–2 high-value Modal→BottomSheet | M | Med |
| **G5** | Bookkeeping + dogfood | Manifest bumps + device checklist | S | Low |

**Definition of done for this campaign:** G1–G3 merged; G4 at least ratchet + one Modal migration; G5 notes + dogfood list executed (or explicitly deferred with owners).

---

## Explicit OUT of scope

- Discover / Atlas full surface re-audits (still deferred in manifest).
- Voice full-screen Calm Listening (D24 deferred by product).
- Booking tone-pills, People `RolePill`, auth 52px species (separate species).
- On-dark Discover cover CTAs (canon local exception until second use).
- Merging header families into one mega-header.
- Blind Button migration of every `action.primary` fill (chips, nav pills, radio dots are not VBtn).

---

## Adjudications needed before / during coding

Resolve in the PR description (or a one-line manifest note) — do not silently invent variants:

1. **`ConflictResolutionSheet` “Keep it”** — muted `colors.background.secondary` fill. Options: (a) new `Button` variant `muted`/`tintSoft`, (b) keep local + allowlist in button budget with reason, (c) map to existing `tint` if visually acceptable.
2. **`CostsReceiptButton`** — still a plain pill; either implement ticket silhouette or document as normal pill exception (kill false “silhouette” rationale).
3. **`DeckCallFace` / `AtlasLearningSignal`** — dense dual CTAs may be a different species than VBtn 44px; adjudicate before forcing `Button`.
4. **`PublicHeader`** — public/external-share chrome: bare `PageChromeIconButton` vs glass paper. Default proposal: **bare** (parchment public entry), not dark glass.

---

## PR-G1 — Local-button budget → zero

**Why first:** CI already ratchets this (`scripts/check-local-button-budget.mjs`). Clearing it is measurable and prevents new forks.

**Current baseline:** `6` files (script prints the list; was 7, AtlasYearStepper already gone).

Expected offenders (re-run script before editing):

| File | Likely action |
|---|---|
| `app/trip-accommodations/index.tsx` | Migrate cancel/save-style CTAs to `Button`; leave non-CTA “GROUP ROOM” card row alone |
| `components/places/SpotPlanningRail.tsx` | Add / Book / Ask Vesper → `Button` (`primary` / `secondary` or `ghost` / `amber`) — mirrors reader footer |
| `components/chat/ErrorBanner.tsx` | Retry → `Button` `size="sm"` ghost/secondary |
| `components/ui/TextInputModal.tsx` | Secondary/submit → `Button` |
| `components/atlas/AtlasLearningSignal.tsx` | Looks right / Not quite → `Button` **or** allowlist if adjudicated as chip pair |
| `components/focus-home/DeckCallFace.tsx` | Primary/quiet pair → `Button` **or** allowlist if deck-face species |

**Also pull if cheap in same PR:**

- `components/trip-plan/OptimizeRouteSheet.tsx` Apply/Discard → `Button` (deferred from #69, high confidence).
- Do **not** force “Keep it” until adjudication #1.

**Acceptance:**

1. `node scripts/check-local-button-budget.mjs` → `0/0` **or** `N/N` with `BASELINE` lowered and each remaining file listed in script header as sanctioned exception with reason.
2. Expand `__tests__/conventions/buttonAdoptionContract.test.ts` golden-path list to include every migrated file.
3. `npx tsc --noEmit` + targeted jest for touched surfaces.

---

## PR-G2 — Glass / header Phase 5

**Why:** Phases 0–2 shipped (#70); leftover is component-level page backs the route-only guard cannot see.

| Item | Change |
|---|---|
| `components/external-share/PublicHeader.tsx` | Raw Ionicons → `PageChromeIconButton` (bare; see adjudication #4) |
| `components/trip/TripFolioHome.tsx` cold draft | `IconButton` back → `PageChromeIconButton` bare (parchment cold header, not hero glass) |
| Convention expand | Extend `headerChromeContract.test.ts` (or sibling) to scan `components/**` for page-chrome-shaped raw `Ionicons name="chevron-back"` with allowlist: `ReaderChrome`, onboarding step-back if any, calendar steppers, inline row chevrons |
| Optional | Flag bespoke `borderRadius: radius.full` + back icon outside `FloatingGlassIconButton` / `PageChromeIconButton` (Phase 5.1) — start as warn/allowlist if noisy |

**Skip:** `MemoryStoryHeader` — already thin `ProductiveHeader` wrapper on main.  
**Skip:** `EditorialMasthead` `backLabel` Ionicons branch unless a call site is wrong family.

**Acceptance:**

1. No production page chrome uses raw Ionicons back except allowlisted exceptions with reasons.
2. Device/visual check: public share header, cold trip draft, notifications glass entry, chat floating header (regression).

---

## PR-G3 — StatusPill hygiene (small, parallelizable)

| Item | Change |
|---|---|
| `ProposalDetailScreen.tsx` | Rename local `StatusPill` → `ProposalStatusPill` (still wraps `ui/StatusPill`) |
| Convention test | Assert Trip Settings + Proposal Detail import `ui/StatusPill`; fail if a third status-like h22 shell appears without import (keep narrow — do not ban every `pill` style) |

**Out:** ExpenseDetail / accommodations status-ish chips unless they literally duplicate h22/r11 StatusPill metrics.

**Acceptance:** ProposalDetailScreen tests green; new convention test green.

---

## PR-G4 — Sheets follow-through (narrow)

Do **not** boil the ocean of 14 Modal bypasses.

1. **Ratchet:** Add `scripts/check-sheet-handle-budget.mjs` (or extend an existing check) — fail if a production sheet re-types `width: 36` / `height: 4` grabber instead of `SheetHandle` / `SheetHeader`. Allowlist: `TripMapRouteSheet` (44×5 tappable), Discover map third-party indicator, DevFab.
2. **Migrate 1–2 high-value raw Modals** onto `BottomSheet` / `ConfirmDialog` where anatomy already matches:
   - Prefer: `GroupAgencySheet`, `FindPhotosSheet` (if structure fits)
   - Defer: `VoiceOverlay`, `ProposalDetailScreen` sheet mode, Deck Modal (known H2-5 gap)
3. Lower `scripts/check-sheet-bypass-budget.mjs` `BASELINE` when counts drop.

**Acceptance:** Handle ratchet green; bypass baseline tightened; migrated sheets keep dismiss/safe-area behavior in smoke tests.

---

## PR-G5 — Manifest + dogfood

### Manifest (done 2026-07-12)

Updated `design/surface-manifest.yaml` FOLLOW-ON notes + provisional `code_verified_at` for:

- Header system ← G2 (+ glass #70 already noted)
- Buttons (family) ← G1
- Sheets (family) ← G4 (+ handle atom #68)
- Proposal & Decision Detail ← G3 StatusPill hygiene

Status remains `partial` until device dogfood and post-merge sha refresh.

### Device dogfood checklist (layer-4 — pending device)

Do not claim visual ship until checked on a booted simulator/device after G1–G4 merge:

- [ ] Notifications opened from Trips home bell (paper glass masthead; Mark read)
- [ ] Atlas voice logs + narration history (floating paper glass)
- [ ] Concierge chat + trip chat floating chrome (shared glass circles)
- [ ] Spot planning rail Add / Book / Ask Vesper (shared Button)
- [ ] Discover reader footer CTAs (regression from #69)
- [ ] Cold trip draft back (bare PageChromeIconButton)
- [ ] Public share header back (bare PageChromeIconButton)
- [ ] Group agency discard confirm (ConfirmDialog, not raw Modal)
- [ ] Trip accommodations cancel/save CTAs if exercised in dogfood persona

### Deferred leftovers (tracked — do not rediscover as new)

Recorded in `design/reaudit-2026-07-open-findings.md` polish-gap section:

- ConflictResolutionSheet “Keep it” muted-fill adjudication
- CostsReceiptButton ticket-silhouette honesty
- Remaining sheet-bypass Modal sites (VoiceOverlay, ProposalDetail, Deck, FindPhotos native pageSheet)
- On-dark Discover cover CTAs / booking tone-pills / People RolePill (separate species)

---

## Suggested sequencing

```
G1 (buttons)  ─┬─► G5 (manifest/dogfood)
G3 (StatusPill)┘
G2 (glass P5) ───► G5
G4 (sheets)   ───► G5   (can parallel G1/G2 after G3)
```

- **Parallel OK:** G1 ∥ G2 ∥ G3 (no file overlap expected).
- **G4 after G1** if the same engineer; otherwise parallel with care on sheet-heavy files.
- Use isolated worktrees; never `git add -A` on dirty main.

---

## Verification commands (every PR)

```bash
cd travel-app
node scripts/check-local-button-budget.mjs
node scripts/check-sheet-bypass-budget.mjs
npx jest --runInBand __tests__/conventions/buttonAdoptionContract.test.ts __tests__/conventions/headerChromeContract.test.ts
npx tsc --noEmit -p .
```

Add new ratchets to CI the same way existing budget scripts are wired (`package.json` / reliability workflow — follow existing pattern; do not invent a second gate).

---

## Success metric

| Metric | Before (2026-07-12) | After campaign |
|---|---|---|
| Local-button budget | 6 | 0 (or sanctioned exceptions only) |
| Route raw Ionicons back | allowlisted only | + component page chrome cleaned |
| StatusPill canon consumers | 2 wrappers, opaque naming | clear names + ratchet |
| Sheet handle forks | informal | CI ratchet |
| Manifest Header/Buttons/Sheets | `partial`, stale sha | notes + sha bumped |

Campaign is **closed** when G1–G3 merge and G5 dogfood is done or consciously deferred — not when every Modal in the app dies.
