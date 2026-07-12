# Code Alignment Brief — Buttons / CTA Adoption

Date: 2026-07-11  
Branch: `polish/buttons-adoption`  
Canon checked: `/Users/feihuyan/Downloads/vesper 146/project/buttons.jsx`, `Vesper Button Decisions.html`, `Vesper Component Consolidation Audit.html`  
Prior audit: `/Users/feihuyan/travel-workspace/design/component-consistency-audit-2026-07-09.md`  
Intended workspace copy path: `/Users/feihuyan/travel-workspace/design/code-alignment-brief-2026-07-11-buttons-adoption.md`

## Canon Re-Check

`components/ui/Button.tsx` already matches the current VBtn variant map on `origin/main` for the mechanically important variants:

- `primary`: solid ink / white label.
- `ghost`: transparent with a hairline border.
- `amber`: soft gold wash + gold label.
- `destructive`: solid oxblood / white label.
- `warning`: solid terracotta caution gate.
- `sage`: soft sage wash + sage label.

The old audit findings for missing `amber`, missing ghost border, and filled destructive are stale on current `origin/main`. The remaining problem is adoption: local surfaces still re-type pill CTA geometry.

## Migrated In This Pass

- `components/discover/reader/ReaderFooterActions.tsx`: replaced local `Tap` + `Text` pill buttons with shared `Button`.
  - Ask Vesper -> `variant="amber"`, `fullWidth`, `icon="sparkles-outline"`.
  - Save -> `amber` when selected, `tint` otherwise.
  - Add to trip -> `sage` when selected, `tint` otherwise.
  - Share -> `ghost`.
- `components/ui/Button.tsx`: added `accessibilityState` forwarding so selected saved / in-trip states survive migration while the Button still owns disabled/loading state.
- `__tests__/conventions/buttonAdoptionContract.test.ts`: added a narrow ratchet for the audited golden-path CTA files.

Already migrated on current `origin/main` before this pass:

- `components/trip-plan/PlanEmptyDay.tsx`: Add / Free time compose `Button`.
- `components/trip-plan/ConflictResolutionSheet.tsx`: Fix it composes `Button`.
- `components/voice/MicPrivacyDisclosure.tsx`: primary mic CTA composes `Button` with the auth CTA size exception.

## Deferred / Do Not Sweep

- `components/trip-plan/ConflictResolutionSheet.tsx` Keep it: intentionally left local. It is a flat muted-fill action (`colors.background.secondary`) that maps neither to `tint` nor `secondary`; needs a design ruling before migration.
- `components/trip-plan/OptimizeRouteSheet.tsx`: Apply / Discard are mutation-review sheet actions. Good follow-up candidate, but needs itinerary mutation-flow review, not blind button cleanup.
- `components/trip-plan/NowModeStrip.tsx`: compact live-mode action grid. Likely a different density species; review against itinerary/route canon before migrating.
- `components/voice/VoiceOverlay.tsx`: live mic end button and status rail controls. Treat as voice-specific live-session chrome, not generic CTA.
- `components/voice/NarrationLeaseConflict.tsx`: inline banner action pill is dense and embedded; likely closer to InlineChip/action-row grammar than VBtn.
- `components/discover/DiscoverCoverHome.tsx`: cover CTAs include on-dark / editorial card treatment; canon explicitly says on-dark photo pills are a local exception until a second use earns a variant.
- Auth 52px CTA: keep as Button `size="auth"` unless product/design reopens the canon exception.
- Booking tone-pills, People role/action pills, icon-only controls, and Costs receipt buttons remain deliberate exceptions. Do not migrate without a brief that adjudicates their shape species first.

## Follow-Up Recipe

1. Run the narrow convention test:

   ```sh
   npm test -- --runInBand __tests__/conventions/buttonAdoptionContract.test.ts
   ```

2. Find new high-confidence candidates:

   ```sh
   rg "backgroundColor:\s*colors\.action\.primary|borderRadius:\s*radius\.(full|input)" components app --glob '*.{ts,tsx}'
   ```

3. Only migrate when the local control is:

   - text-label CTA, not icon-only;
   - 44px-ish pill/stadium, not a dense chip;
   - primary/secondary/ghost/amber/sage/destructive in meaning;
   - not one of the canon-documented exceptions above.

4. Prefer extending `Button` only for recurring, canon-backed needs. One-off geometry should stay local and be documented.
