# Code Alignment — Batch F2: Changes Surface + Ask-the-Organizer Pattern (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `changes-kit.jsx`, `changes-screen.jsx`, `changes-states-board.jsx`, `ask-organizer-pattern.jsx` (read-only, all in the canon mirror). Wedge-critical: this is where the group sees and reacts to what changed.

Standing rules: git status first · snap rule · one commit per task · typecheck+tests green · no push without approval.

## Task F2-1 — SourceChip component (missing entirely)
Canon `changes-kit.jsx §SourceChip` (lines 31-42): four chip types — Vesper (gold), member (initial avatar), group (people icon), Atlas (map icon) — 26×26 badges rendered left of each timeline row title. Code's `components/trip-plan/ChangeTimelineRow.tsx` currently shows only author name as text, no badge. Build the `SourceChip` component and wire it into every timeline row.

## Task F2-2 — VoteInPlace inline voting (currently detail-only)
Canon `changes-kit.jsx §VoteInPlace` (lines 75-78): the votes-in-place block shows two tappable vote-option buttons directly in the timeline (e.g., "Kamogawa Table" / "Keep the plan") — voting happens inline, without leaving the Changes screen. Code (`changes.tsx:221-224`) only shows a "Review" label + chevron that routes to the Proposal Detail screen. Build the inline voting buttons so the common case (a simple binary vote) can be resolved without navigating away; keep the "Review" path for anything that needs the full Proposal Detail view (multi-option, needs discussion, etc. — use existing routing logic to decide which cases stay detail-only).

## Task F2-3 — Read/unread state + fade
Canon `changes-screen.jsx §ChangeRow` (lines 16-18): unread = gold dot + full opacity; read = checkmark + 0.55 opacity fade. Code has no read/unread distinction — all rows render identically. Wire a read/unread flag (reuse whatever "seen" tracking exists elsewhere, e.g., notifications' `is_read` pattern) into `ChangeTimelineRow.tsx`, add the opacity fade and checkmark/dot swap.

## Task F2-4 — Bucket labels + empty copy (small, batch with above)
- Collapse "Today/Yesterday/Earlier" (`changes.tsx:34`) to canon's two buckets: "TODAY" / "EARLIER" (uppercase). Yesterday's items fold into Earlier.
- Empty-state copy: "No changes yet." → canon's "Nothing has changed yet."

## Task F2-5 — Build the Ask-the-Organizer pattern (net-new; two audits independently found this unbuilt)
Canon `ask-organizer-pattern.jsx`: three intensities for organizer-only controls encountered by a non-organizer member: (a) **locked-invisible** — member never sees the control (already achievable by conditional rendering, verify it's used for genuinely destructive actions); (b) **locked-visible-explained** — control renders but explains why it's blocked (e.g., "Only Maya can change dates"); (c) **request-flow — Ask** — a one-tap affordance that drops a pre-written request into the group chat ("Ben would like to move the dates — @Maya").

Current code state: `components/chat/GroupAgencySheet.tsx:128-133` has a static "Ask the organizer →" text with **no onPress handler** — this is the only lookalike in the whole app, and it does nothing. ~8-10 call sites gate on `isOrganizer`/`is_organizer` across trip-settings, permissions, trip-info, trip-accommodations, trip-proposal, `ProposalControlMatrix.ts`, StayCompare, chat, `ProposalDetailScreen.tsx` — these are the candidates for intensity (b)/(c).

Build:
1. A shared `BlockedActionRow` (or similar) component implementing intensity (b): explains who can do the action, in the app's existing blocked/locked visual language.
2. Wire the "Ask" tap-through: reuse `tripChatPrefill` infra (confirmed to already exist per the Trip Settings audit) to drop a pre-written request into the group chat naming the organizer and the requested action.
3. Fix `GroupAgencySheet.tsx:128-133`'s dead Ask string to use the new real handler.
4. Apply the pattern to at least the highest-traffic organizer-only controls first: trip dates (trip-settings), member removal, and stay/proposal decisions — the rest can follow in a later pass; report which sites were converted vs. left for later.

## Done
SourceChip built + wired · inline voting works for binary votes · read/unread fade live · bucket labels + empty copy fixed · Ask-the-organizer pattern built with at least 3 real call sites converted and the dead GroupAgencySheet string fixed · report remaining organizer-gated sites not yet converted.
