# Code Alignment — Batch H2: Interaction Surfaces Conformance (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: the interaction-surface rules across the kit boards (sheets/scrims/toasts/confirms). The primitives are strong — ONE `BottomSheet` family with canon props, `Alert.alert` count is 0, Ask-the-organizer shipped in F2-5, typed-confirm got its first caller in F3. This batch closes the adoption gaps. **Lead with the two user-facing ones (H2-1 swipe-to-dismiss, H2-2 dirty-dismiss) — the rest is hygiene.**

Standing rules: git status first · snap rule · one commit per task · typecheck+tests green · no push without approval.

## Task H2-1 — Swipe-to-dismiss in the BottomSheet primitive (canon-required, currently 0)
Canon requires pan/swipe-to-dismiss on `peek`/`chooser`/`form` sheets. Zero sheets have it — `components/ui/BottomSheet.tsx` has a `disableSwipeDismiss` prop documented as "reserved for variants with pan-to-dismiss" but there is **no `PanGestureHandler`/`GestureDetector` in the primitive at all** — the prop gates nothing.
- Implement the gesture in the primitive (drag-down past a threshold dismisses; respect `disableSwipeDismiss` to opt out for sheets that shouldn't, e.g. destructive-confirm sheets).
- Honor reduced-motion for the dismiss animation (reuse the motion tokens).
- This is one primitive change that lights up all consumers at once — verify a couple of representative sheets (a form, a chooser) actually dismiss on drag afterward.

## Task H2-2 — Dirty-dismiss on high-stakes forms (2/~30 today)
Only `trip-info` and `GroupAgencySheet` pass `onDirtyDismiss`; ~28 form sheets let a backdrop tap / back gesture silently discard unsaved edits. Do NOT wire all 28 — target the ones where losing input actually hurts:
- `components/expense/AddExpenseSheet.tsx` + `EditExpenseSheet.tsx` (a half-typed expense).
- Any itinerary/plan edit sheet with free-text (verify which exist).
- Wire `isDirty` + `onDirtyDismiss` → a discard-confirm, reusing the exact pattern already in `trip-info/index.tsx`. Report which sites you converted and which you judged low-stakes enough to skip.

## Task H2-3 — Snap-preset adoption (6/24 today)
18 sheets pass raw `maxHeightFraction` (0.5–0.9) instead of the canon snap presets (`peek`/`chooser`/`form`/`full`). Map each to a preset **where it fits** — a form sheet → `form`, a short chooser → `chooser`, etc. Some may legitimately need a custom height (verify against the preset heights before forcing); leave those, but comment why. Goal is coverage of the ones that clearly map, not 24/24 for its own sake.

## Task H2-4 — Scrim token cleanup (small)
`components/ui/ConfirmDialog.tsx` hardcodes `rgba(27,23,20,0.32)` for its scrim — point it at a `colors.tint.*` token. Verify the two `scrimOpacity={0.35}` overrides in the expense sheets are intentional (they match the `photoScrim` default — if so they're redundant and can drop the prop; if deliberate, leave). Keep the distinct-scrim-value count at canon's ~6.

## Task H2-5 — Raw Modal cleanup (migrate the real offenders only)
11 raw RN `Modal` instances exist; **most are sanctioned exceptions — DO NOT touch these**: `CardLift.tsx` (deliberate alternate primitive), `PermissionRationale.tsx` + `MicPrivacyDisclosure.tsx` (pre-permission rationale pattern), `board.tsx` ReelBridge (transient loading bridge), `DevFab.tsx` (dev-only). Migrate only the genuine offenders to `BottomSheet`/`CardLift`:
- `components/trip/FindPhotosSheet.tsx`, `components/photo-intake/PhotoIntakeSheets.tsx` (2), `components/trip/proposal-detail/ProposalDetailScreen.tsx`, `components/voice/VoiceOverlay.tsx`, `components/focus-home/Deck.tsx`.
- Verify each before migrating — if one turns out to be a deliberate full-screen takeover (like the experience detail's `presentation="screen"` pattern), leave it and note why.

## Done
Swipe-to-dismiss live in the primitive + verified on a form and a chooser · dirty-dismiss on the high-stakes forms (expenses + any free-text plan sheet), skips reported · snap presets adopted where they map, custom heights justified · ConfirmDialog scrim tokenized · real raw-Modal offenders migrated, sanctioned exceptions left with a one-line note each · report final counts (snap adoption, dirty-dismiss, raw Modal remaining).

## Note — toast tiers
The stale backlog flagged "no 5s error tier." Current toast tiers are 3.5s / 4.5s-with-action / 8s-undo, and the audit judged the 3.5s error baseline acceptable. Confirm against the canon toast board before adding a tier — likely a no-op. Toast swipe-dismiss can piggyback on H2-1's gesture work if cheap, otherwise defer.
