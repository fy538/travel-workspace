# Code Alignment — Batch F3: Trip Settings Destructive Actions (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `vesper-trip-settings-app.jsx` (read-only mirror). Depends on F2's Ask-the-organizer pattern landing first if you want to reuse `BlockedActionRow` here too (recommended — same pattern applies to the settings screens this batch touches).

Standing rules: git status first · snap rule · one commit per task · typecheck+tests green · no push without approval.

## Task F3-1 — Delete/cancel trip end-to-end (biggest gap: currently absent entirely)
Canon's 6-action end-state matrix (archive/restore/cancel/leave/delete-draft/delete-with-content) exists as a designed contract; code implements only 2 of 6 (archive, leave). There is currently **no way to delete or cancel a trip in the app at all.**
- `components/ui/ConfirmDialog.tsx` already has `typedConfirmation` (phrase-match, submit disabled until exact) — it has zero callers anywhere in the codebase. Use it here.
- Build cancel-trip and delete-trip actions in `app/trip-settings/index.tsx`, gated to organizer-only, using typed confirmation (canon: type the trip name or "delete" to confirm) for the destructive ones.
- Distinguish delete-draft (a trip with no real content — lighter confirmation) from delete-with-content (typed confirmation required, matching canon's harsher treatment).

## Task F3-2 — Trip name becomes editable
`app/trip-info/index.tsx` currently has no name field — the "Trip name" row in Trip Settings routes to a screen that can't actually edit the name. Build a `TripInfoEdit` form (title field + save) with a dirty-dismiss guard (reuse the existing `BottomSheet` `onDirtyDismiss` prop — already built, just needs a caller here).

## Task F3-3 — Fix member role-gating leaks
`app/trip-settings/index.tsx:173-312` — non-organizer members can currently tap Trip rows and Archive even though those are organizer-only actions. Gate these behind the role check (reuse the pattern from wherever permissions are already correctly gated, e.g., the dates/members screens) so members see either nothing (locked-invisible) or the new `BlockedActionRow` from F2 (locked-visible-explained) — decide per-action which intensity applies; default to locked-invisible for Archive/Delete (genuinely destructive), locked-visible-explained for anything a member might reasonably want to request (e.g., viewing why a setting is locked).

## Task F3-4 — Small state fixes (batch together)
- **Remove-member dialog**: add the unsettled-cost risk banner (canon expects a warning if the removed member has open balances) — `app/trip-info/index.tsx:458-478`.
- **Dates conflict check**: currently only checks itinerary blocks; extend to also check stay/booking coverage before allowing a date change, and add a live-trip caution state (canon: changing dates mid-trip needs extra confirmation) — `app/trip-dates/index.tsx:160`.
- **ConnectedSystems rows**: currently static copy ("Lodging workspace") regardless of real state — wire live status (unsettled balance amount, hold-expiring countdown, or a quiet/settled state) using data already available from the Stay/Costs surfaces.
- **Trip-unavailable / failed-save states**: currently toast-only or returns null. Add a proper inline state using the shared State System components (don't invent local treatments).

## Done
Delete + cancel trip work end-to-end with typed confirmation for the harsher cases · trip name is editable with dirty-dismiss guard · member role-gating leaks fixed (Trip rows + Archive no longer tappable by non-organizers) · remove-member risk banner + dates conflict/live-caution + ConnectedSystems live status + trip-unavailable state all land · report if any destructive-action backend endpoint doesn't yet exist (this batch assumes the API supports cancel/delete — verify before building the UI, flag if missing rather than stubbing).
