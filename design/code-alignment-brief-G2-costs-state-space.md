# Code Alignment — Batch G2: Costs State-Space Completion (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/costs-screens.jsx` + `costs-system.jsx` (read-only). Chassis, states model, and settle math are genuinely canon-shaped; empty-state is an exact match; the forecast card + SettleSummary were removed in E4. This batch closes the "last 30% render-only" gaps.

Standing rules: git status first (branch from main) · snap rule · one commit per task · typecheck+tests green · no push without approval · **flag backend-gated items, do not fake data** (masked + nudge below are BE-gated).

> **Adjudication baked in — see the response that accompanies this brief.** Two calls were made before writing:
> **A. Add/Detail screens vs. canon's sheets-over-ledger →** ACCEPT the current full-screen presentation; do NOT migrate to sheets. Precedent-consistent with the Trip-Creation cards-vs-screens ruling (accept the code's behaviorally-correct simplification, demote the artboards to reference). No task below touches this. If overridden, the migration is a separate ~M task using the existing `BottomSheet` family.
> **B. Backend-gated trio (masked / nudge) →** build FE where it degrades gracefully, keep BE-gated renderers dormant with a comment, flag the endpoints. Sequencing recommendation: nudge is wedge-relevant (chasing settle-up is a real group beat) → schedule BE now; masked is a privacy nice-to-have → defer.

## Task G2-1 — Balance drill-in: density-based navigation
`utils/costsViewModel.ts:418` computes `dense: rows.length > 3` but it never branches navigation — `components/expense/CostsBalanceSheet.tsx` always renders as a `BottomSheet` overlay regardless of group size. Canon (`costs-screens.jsx:336`) mandates a full drill-in for dense 4+ traveler groups, sheet for 2-3.
- Consume the `dense` flag: 2-3 travelers → keep the sheet; 4+ → route to a full balance drill-in screen (per-person owed/owe breakdown, transfer list).
- Reuse the existing balance-sheet content; the drill-in is the same data at screen scale, not a new computation.

## Task G2-2 — AddExpense amount hero
`components/expense/AddExpenseSheet.tsx:498-511` — the amount field lacks the canon hero treatment (`costs-screens.jsx:229`: large serif €-anchor, ~46px). Everything else (trip-day picker at 524-578, typography families) is canon-aligned. This is a focused typography/layout pass on the amount input — snap to the app's existing serif display role, don't hardcode 46px.

## Task G2-3 — Starters: real prefill + wire the tap [+ dead-code cleanup]
`components/expense/CostsEmptyState.tsx:14-18` hardcodes template amounts (`~€600`, `~€84`, `~€56`); `onStarterPress` (defined on the component) is never connected by the parent screen. Canon uses real amounts derived from merged trip data, and starters are tappable to prefill the Add form.
- Wire `onStarterPress` from `app/trip-expenses/index.tsx` so tapping a starter opens Add pre-filled.
- Replace the fake amounts with real derived figures where data exists; if no signal is available, drop the amount rather than showing a fabricated one (substrate rule — no invented numbers).
- Dead code: `utils/costsViewModel.ts:180-183` `hasTripHomeSignal` is computed but never read anywhere. Either consume it (it gates whether starters carry real amounts) or remove it. `buildEstimateModel` (`costsViewModel.ts:187-226`) is now dead after E4's forecast removal — delete it and its `estimate` field unless something still reads it (verify).

## Task G2-4 — Nudge: real affordance [BACKEND-GATED — flag]
`app/trip-expenses/index.tsx:188-191` — the nudge footer button fires a toast: `"Nudges are not wired yet, but the balance is ready."` Canon (`costs-screens.jsx:155,169`) expects a real "Send nudges" action with no stub copy.
- **There is no nudge/remind endpoint** in `data/` or `utils/api/`. **Flag it as backend work** (one endpoint likely serves both cost-settle nudges and the stay-vote nudge in G1-5 — coordinate the two).
- Build the FE affordance (confirm-who-gets-nudged, send, confirmation) behind the flag; keep it dormant with a comment until the endpoint lands. Replace the stub-copy toast so it doesn't ship as a visible "not wired yet."

## Task G2-5 — Masked expense rows [BACKEND-GATED — defer, flag]
`utils/costsViewModel.ts:371` hardcodes `masked: false` in `buildLedgerRow`; the renderer (`CostsLedgerRow.tsx:82`, lock-icon path) exists but has no data path — the `masked` field lives only in the FE viewModel type (`costsViewModel.ts:43`), not on the API expense model. Canon supports a masked/private-amount state (a surprise/gift expense whose amount is hidden from the group).
- **Flag as backend schema work** (add `masked` to the expense API model + the privacy control that sets it). Per adjudication B, this is the lower-priority BE item — deferrable past nudge.
- Leave the renderer in place, dormant, with a comment noting the field is BE-pending (match the flight-delay-dormant pattern). Do NOT fabricate masked state on the client.

## Done
Balance drill-in branches on density (sheet for 2-3, full drill-in for 4+) · AddExpense amount hero lands · starters tappable + real-or-omitted amounts, `hasTripHomeSignal`/`buildEstimateModel` dead code resolved · nudge flagged as BE-gated with FE prepped + stub-copy removed · masked flagged as BE-gated, renderer dormant with comment · report the exact endpoints/fields backend must expose (nudge endpoint, expense `masked` field) so they can be ticketed alongside G1's stay-vote work.
