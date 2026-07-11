# Code Alignment — Batch E: Rulings, Strings & Motion Retune (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only mirror). This batch is entirely mechanical — string/token swaps and small removals, no new UI. Adjudications from `design/adjudication-brief-2026-07-06-pre-batch-e.md` are assumed accepted (recommendations as written) unless the user told you otherwise.

## Standing rules
1. `git status` first — check for other sessions' WIP, branch from main if anything unexpected is present.
2. Snap rule: match canon layout/intent; app tokens remain the value source of truth.
3. One commit per task; typecheck + tests green after each; no push without approval.

## Task E1 — Contrast: the one-line mute fix
`constants/colors.ts:82` — change `mute: '#86807A'` → `mute: '#6E6862'`. That's it; `colors.atlas.mute`/`colors.vesper.mute` are aliases and inherit automatically. Confirm no hardcoded `#86807A` stragglers exist (audit found none) and run a snapshot check (audit found zero snapshot fallout, but verify).

## Task E2 — Global Chrome: remove tab badges (canon violation)
Canon recorded "NO badge on the tab bar — Notifications owns unread awareness." Remove `tabBarBadge` from all four tab configs in `app/(tabs)/_layout.tsx` (lines ~83, ~95, ~106, and the fourth) and the badge render block in `components/nav/FloatingTabBar.tsx:~144`. Unread counts stay computed (other consumers may use them) — only the tab-bar badge UI goes.

## Task E3 — Copy-ruling fixes (all string-literal swaps, ~17 sites)
- **Trip surface naming**: `components/trip/TripFolioHome.tsx:2477` — `"the folio is ready"` → `"the trip is ready"` (or equivalent non-Folio phrasing).
- **Itinerary label → "Plan"**: `app/(tabs)/trips/[tripId]/plan.tsx` fallback title (~1041) and eyebrows (~1045, ~1586) currently default to `'Itinerary'`/`'ITINERARY'` — align to `'Plan'`/`'PLAN'` matching the `document` mode's existing correct usage. Also `app/(tabs)/trips/[tripId]/story.tsx:247` (`'Itinerary stop'` → `'Plan stop'` or similar) and `app/trip-settings/index.tsx:275` (`"Itinerary permissions"` → `"Plan permissions"`).
- **Add-verb → "Add to trip"** (adjudication #4: no Places exemption): `components/discover/ExperienceDetailSheet.tsx:638` (`'Add to plan'` + `'Added to your plan ✓'`), `components/places/SpotActions.tsx:88`, `components/places/SpotPlanningRail.tsx:88` (visible + a11y labels), `components/booking/BookingCheckoutPanels.tsx:277` (`'Save to the plan'` → `'Add to trip'`).
- **Voting verb**: `components/trip/proposal-detail/ProposalDetailScreen.tsx:864` — `"Reject"` → `"Decline"`.
- **Undo → Revert** (these buttons call `revertProposal`/act on applied group changes, not the user's own immediate action): `components/trip-plan/BlockChangedBanner.tsx:87` and `components/trip-plan/ChangeTimelineRow.tsx:126` — both `label="Undo"` → `label="Revert"`. Also normalize `components/chat/ChangeAppliedCard.tsx:190` (currently says "Undo" but its own outcome copy at :109 says "Reverted" — pick Revert for consistency).
- **Third-person voice-line fixes** (adjudication #6: only these 4, not the status/meta chrome): `app/(tabs)/trips/[tripId]/story.tsx:658` ("Vesper will compose a fresh version…" → first person), `app/(tabs)/trips/[tripId]/changes.tsx:274` ("Vesper will record edits here." → first person), `components/search/UniversalSearchOverlay.tsx:541` ("Vesper will search and compare options" → first person), `app/(tabs)/atlas/index.tsx:726` (same treatment).

## Task E4 — Costs: remove the forecast-card substrate violation
`app/trip-expenses/index.tsx:288,357-378` — the "Estimated trip shape" card projects a spend forecast with no substrate backing it (violates the standing no-forecast ruling, and it's IN CODE, not just a stale design artifact). Remove the card. While in this file: fix the settled-state copy drift ("Settled · €0 between you." → canon "Settled Oct 19"-style quiet line, date-driven) and delete the dead legacy `components/expense/SettleSummary.tsx` (contains the forbidden "All settled up!" celebration card, confirmed unused).

## Task E5 — Trust & Controls: sign-out and export copy + italic default
- `app/atlas/account.tsx:315` — sign-out dialog: switch from destructive-typed `ConfirmDialog` to the routine (non-destructive) confirm pattern; copy → "You can sign back in anytime — nothing is deleted" (currently "You'll leave this Vesper session on this device").
- `app/atlas/account.tsx:284` — export copy → "Prepared on this device — save or share it wherever you like" (currently "A full export, shared from this device").
- `components/trust/TrustControlsKit.tsx:507` — `TrustContract` is italic-by-default; canon's 2026-07-06 compliance pass ruled roman-by-default with explicit `italic={true}` opt-in only for genuine Vesper voice lines. Flip the default; audit the ~3 loading-line callers ("Reading the ledger…", "Loading your preferences…", memory-receipt hero body) — none are Vesper voice, so they should render roman.

## Task E6 — Motion: retune values + kill shimmer (adjudications #1, #2)
- `constants/motion.ts`: retune `fast` 160→150; align `slow`/sheet-adjacent values to the canon 260/320 pair; remove or repurpose `shimmer: 1200` once E6b lands.
- `components/ui/Skeleton.tsx`: replace the `LinearGradient` shimmer sweep with an opacity pulse (~1.1s cycle, no gradient sweep) per the canon Motion Stance ("reads glossy, not paper"). This touches every skeleton consumer visually — spot-check 3-4 screens after the change (trips home, plan, chat, notifications).
- Promote the house curve `cubic-bezier(0.2,0.7,0.2,1)` (currently demoted to `easing.lift`) to the default entrance easing in `utils/motion.ts`.
- Toast durations in `context/ToastContext.tsx:81-82`: 220/180 → 200/150 (align to canon enter/exit values; the 3.5s/8s dwell tiers already match, leave those).

## Task E7 — Fixture typo + minimal persona additions (adjudication #3)
- Fix the "Casa da Mar" typo → "Casa do Mar" in `utils/api/mock/expenses.ts:197-206` and the frozen test assertion in `__tests__/utils/costsViewModel.test.ts:84,115` (update both together so the test still passes against corrected fixture data).
- Add `theo` and `mara` as new dev personas in `constants/personas/` (following the existing persona file pattern — see `ana.ts`/`ben.ts` for shape) so canon-shaped demo trips are reproducible. Do NOT rename the default mock world or touch existing persona dates — this is additive only, per the demo-slice decision.

## Done
Seven task groups, each its own commit(s) · typecheck + tests green throughout · report any string site the grep-based audit may have missed (these were audit-derived, not exhaustive) · report which motion sites still need manual verification after the shimmer/easing change.
