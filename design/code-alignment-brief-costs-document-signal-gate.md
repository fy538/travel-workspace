# Code Alignment — Costs: Trip-Document Signal Gate (2026-07-08)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/costs-screens.jsx` + `costs-system.jsx` + `Vesper Costs.html` (read-only). The Costs surface itself — `CostsHeader`, `CostsLedgerRow`, `CostsBalanceSheet`, `CostsEmptyState`, `AddExpenseSheet`, `ExpenseDetail` — is a faithful, in places more capable, implementation of the kit (row grammar, six header balance states, settled-is-quiet, private/masked semantics, receipt/OCR flow all present and correctly avoid fabricating data). The one confirmed gap is at the Trip Document integration point, not the Costs screen itself.

## Task 1 — Gate the Trip-Document "COSTS" section on a real signal

Canon's explicit render rule (`costs-screens.jsx:349`, `FlowNotes`, under "NEVER ITS OWN PAGE / SUPPRESS"):

> "No Costs module on the Trip Document unless there's a real signal: unpaid balance, pending split, reimbursement, or a logged-spend summary."

`components/trip/TripFolioHome.tsx:721-757` (`CostsDocumentSection`) is called unconditionally in all three document branches — `live` (`:452`), `post` (`:477`), and `pre`/`imminent` (`:528`) — each time wrapped in its own `<DocumentRule />` divider, with no gate comparable to the `showStayDocument` check (`:325`) that already exists for the Stay section.

`TripFolioCostSummary` (`:125-132`) already carries every field needed to test for a real signal: `loggedCount`, `balanceLine`, `hasEstimate`, `isSettled`. But the call sites never test them — `costSummary` is passed straight through, and when there is nothing logged and no estimate, `CostsDocumentSection`'s internal fallback (`:730-740`) renders anyway with filler copy such as *"Nothing logged yet — I'll keep the tab once spending starts."* (`costsLineFor`, `:714-719`). This is precisely the "module with nothing to say" case canon says must not appear.

Confirmed at the data layer (`app/(tabs)/trips/[tripId]/index.tsx:156-186`): `costSummary` is `null` only when `currentUserId` is missing. For any real trip — including a brand-new cold-start trip with zero expenses and zero cost estimate — it resolves to `{ loggedCount: 0, balanceLine: null, hasEstimate: false, isSettled: false, ... }`. There is no code path today where the section is actually suppressed.

- Add a `hasSignal` predicate — true when `costSummary.loggedCount > 0 || costSummary.hasEstimate || costSummary.balanceLine != null` — and gate all three `CostsDocumentSection` call sites on it, the same way `showStayDocument` already gates `StayDocumentSection`.
- When `hasSignal` is false, render nothing (no section, no `<DocumentRule />` either — an orphaned divider with nothing above/below it is its own visual defect).
- Do **not** change `CostsDocumentSection`'s internal rendering for the signal-present cases — the `hasLogged` / `estimateLabel` / `balanceLine` branches (`:730-740`) are correct and should stay exactly as they are; this task is purely about not mounting the section when none of those branches would have anything real to show.
- Verify the `isSettled` case still renders (a settled trip has a real "logged spend summary" — it's exactly the canon-sanctioned quiet case, not a suppress case). Only the true-empty / no-estimate / no-balance combination should suppress.

## Done
`CostsDocumentSection` is only mounted (in `live`, `post`, and `pre`/`imminent` document branches) when `costSummary` shows a real signal — logged spend, an estimate, a balance line, or a settled summary — matching the `showStayDocument` gating pattern already used for Stay · verified a cold-start trip with zero expenses and zero estimate shows no "COSTS" section and no orphaned `DocumentRule` on the Trip Document · settled trips continue to show the quiet logged-spend summary (not suppressed) · typecheck + tests green.

---

## Standing rules
- `git status` first; branch from `main`. (Note: at audit time `main` already carries unrelated uncommitted WIP across many files from a concurrent session — do not fold this task's diff into that WIP; keep the Costs-gate change isolated to `TripFolioHome.tsx`, and coordinate before touching any of the already-modified files.)
- One commit per task.
- Typecheck + tests green before considering the task done.
- No push without approval.
- Flag backend-gated items; do not fake data. (Not applicable here — this task is purely a client-side rendering gate over data the client already has in `costSummary`; no backend field is missing.)
