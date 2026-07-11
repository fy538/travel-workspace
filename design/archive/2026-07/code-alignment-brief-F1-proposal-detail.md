# Code Alignment — Batch F1: Proposal & Decision Detail Parity (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/vesper-proposal-detail-app.jsx` + `revert-conflict-sheet.jsx` (read-only). This is the weakest wedge surface found in the full alignment audit (~13/18 canonical states, group-visible voting layer roughly half-built). Wedge-critical: this screen is where group members see and act on decisions — the core mechanic dogfood needs to prove.

Standing rules: git status first (branch from main) · snap rule (app tokens are value truth) · one commit per task · typecheck+tests green · no push without approval.

## Task F1-1 — Verb fixes (if not already done by Batch E — verify, don't duplicate)
`components/trip/proposal-detail/ProposalDetailScreen.tsx:860-903` — member button "Reject"→"Decline" (Batch E task E3 covers this; skip if already landed). Additionally here: organizer button says "Accept change" → canon ruling is "Approve & apply to Plan". Decide the fate of the "Neutral" vote option (~line 880) — it's off-canon; either fold it into Decline-with-comment or remove it and record the decision.

## Task F1-2 — Build ProposalVoteRows (missing contract, the biggest single gap)
Canon's `ProposalVoteRows` component (17-contract list) shows: voter avatar stack, per-option vote counts, and a "Waiting on X" line naming un-voted members. Code's `VoteReceipt` (`ProposalReceipt.tsx:163`) currently renders bare tallies with no avatars or names. Build the full contract: reuse `AvatarStack`/People & Collaboration tokens for the avatar row, add per-option counts, and the waiting-on line (member roster is already available via existing trip-member hooks — this is presentation, not new data plumbing for the standard vote case).

## Task F1-3 — RevertConflictSheet: build out to 3 canon states
`components/trip-plan/RevertConflictSheet.tsx` currently implements 1 of 3 states. Canon states: (a) clean-revert confirm, (b) conflict — per-item Keep/Discard list of later edits that depend on the reverted change, (c) partial-keep result summary. Also: canon's WAS/NOW diff uses stacked rows with WAS struck through (Changes' ReskinnedSheet chrome); this sheet currently shows a generic conflict list, not that diff grammar. Per the campaign's own adjudication (K1, sanctioned): the *inversion* of NOW-struck-side-by-side was accepted as a deliberate revert-mode variant with recorded rationale — confirm that rationale is followed consistently (don't "fix" it back to Changes' grammar; build out the 3 states using the sanctioned inverted-diff pattern). Add the canon grab-handle (currently `showHandle={false}`).

## Task F1-4 — Receipt states: lazy-consensus, booking-hold, conflict
- **Lazy-consensus** (`ProposalReceipt.tsx:86`): add the countdown element + "Approve now"/"Object" buttons (canon state A/lazy-consensus).
- **Booking-hold** (`ProposalReceipt.tsx:97`): currently a generic stub. Build the venue/time/party/reference ledger + expiry banner + Confirm/Release actions (this overlaps Booking surface work — reuse existing hold-receipt components from `components/booking/` if the shapes match).
- **Conflict state C** (`ProposalReceipt.tsx:116`): canon's conflict state is a schedule-overlap with an hour-track visualization + Fix-it/Keep-both/Alternatives flow. Code's "conflict" today = apply-failure only. Build the real overlap-conflict receipt as a distinct state from apply-failure.

## Task F1-5 — Closed/recovery states
- **Expired + Superseded**: currently both fall through to a generic "Closed" pill (`ProposalDetailScreen.tsx:148-150`, "Replaced" label). Build the canon `ProposalClosedState` contract distinguishing Expired vs Superseded, each with its own explanatory copy.
- **Author withdraw button**: `api.withdrawProposal` mutation already exists in `data/proposals.ts:175` — just unwired in the UI. Add the withdraw affordance for the proposal's author.
- **Organizer recovery actions**: after apply-failed, canon expects Retry / Review-conflict actions for the organizer — currently missing (`ProposalDetailScreen.tsx:611`).
- **Offline-stale banner**: canon state L includes an offline/stale banner — add via the shared State System `StateNotice` (tone="stale"), don't invent a local treatment.
- **AffectedPlanRows**: `ProposalDetailScreen.tsx:386` currently plain text lines — add Changed/Removed tags and tap-through to the affected plan block, matching the contract.

## Done
5 task groups, each committed separately · ProposalVoteRows contract built and used by the open-vote state · RevertConflictSheet has all 3 states with the sanctioned diff grammar · lazy-consensus/booking-hold/conflict receipts built out · expired/superseded/withdraw/organizer-recovery/offline-stale/affected-rows all present · report anything that needed backend data not currently exposed (flag, don't fake).
