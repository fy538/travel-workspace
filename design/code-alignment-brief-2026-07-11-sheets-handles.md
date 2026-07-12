# Code Alignment Brief: Sheets + Handles Polish

Date: 2026-07-11
App base: `travel-app` `f97d56d9`
Canon checked: `/Users/feihuyan/Downloads/vesper 146/project/`

## Result

Mechanical handle drift is now routed through one app atom:

- `components/ui/SheetHandle.tsx` is the shared grabber source: 36x4, radius 2, default neutral border tone.
- `components/ui/SheetHeader.tsx` now renders `SheetHandle` instead of carrying a second inline 36x4 implementation.
- `components/onboarding/CountryPickerSheet.tsx` no longer re-types its local grabber.

The already-landed fixes on `origin/main` were re-verified:

- `components/expense/CostsBalanceSheet.tsx` uses `SheetHeader size="dense"` and no longer carries the old 38px local handle.
- `components/expense/ExpenseDetail.tsx`, `components/people/MemberActionSheet.tsx`, and `components/voice/VoiceOverlay.tsx` already use `SheetHandle`.
- `components/trip-plan/RevertConflictSheet.tsx` already has all three `SheetHeader` calls on `size="dense"`.

## Canon Notes

`sheet-atoms.jsx` is the handle geometry authority for this pass: `VHandle` is 36x4 with radius 2. `sheet-header.jsx` still contains a 34px inline demo handle in vesper 146, but its surrounding comments continue to bless the app's `large`/`dense` ladder and modal Family E anatomy. For app code, the single shared atom keeps the 36x4 ruling stable.

`sheet-field.jsx` was re-read but remains a separate leftover: the app still lacks a direct `VSheetField` equivalent for borderless read-only display rows. That is not a handle drift fix and should be scoped as a follow-up sheet-field adoption pass.

## Deferred / Deliberate

- `components/trip-map/TripMapRouteSheet.tsx` stays distinct. Its handle is a tappable 44x5 height-cycling control, not a passive grabber atom, and should remain documented as a map route sheet variant.
- `components/dev/DevFab.tsx` still hand-types a dev-only modal handle. It is not production sheet chrome.
- `app/(tabs)/discover/map.tsx` uses `@gorhom/bottom-sheet`'s `handleIndicatorStyle`; this is third-party sheet chrome and Discover is deferred in the manifest.
- Several Atlas/card decorative widths surfaced in grep, but they are not bottom-sheet grab handles and were left alone.

## Suggested Follow-Ups

- Decide whether the Sheets family manifest row should move from `aligned_at: 135` to `146` after this branch lands; this pass re-checked the handle/header subset, not the full sheet family.
- Open a separate `VSheetField` brief if read-only sheet rows are still in scope.
- Revisit the `large`/`edit` title weight question from the prior audit; this pass did not change typography weights.
