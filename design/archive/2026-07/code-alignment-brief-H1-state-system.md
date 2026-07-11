# Code Alignment — Batch H1: State System Consolidation (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: State System board (kit maps 1:1; StateNotice covers Stale/Offline; SessionRecovery verified). The kit lives in `components/ui/state/` (StateNotice, ErrorRecovery, EmptyHero, ActionFailureInline, StateAction, stateTokens). Legacy siblings live one level up in `components/ui/` (ErrorState, EmptyState). **This is the largest H batch — but much smaller than the stale backlog's "50-file migration" implies.** Read the taxonomy note below before scoping anything.

Standing rules: git status first · snap rule · one commit per task · typecheck+tests green · no push without approval.

> **Taxonomy correction (do not skip).** The backlog framed `ErrorState` (34 uses) as legacy debt to migrate into `ErrorRecovery` (2 uses). **That is wrong — they are different tiers, not old-vs-new:**
> - `ErrorState` = **full-page load failure** (64px terracotta icon, h2, retry). Shown when a screen's whole query fails and there's nothing to render. The full-page peer of `EmptyHero`.
> - `ErrorRecovery` = **inline oxblood recovery panel** (minHeight 80, compact actions). Shown inside an otherwise-working screen when one section/action fails.
> Migrating 34 full-page errors into inline oxblood panels would be a regression. The real debt is that the kit is **forked across two folders** and one tier (full-page error) never moved into `state/`. Tasks below consolidate; they do NOT bulk-replace ErrorState's callers.

## Task H1-1 — Unify the state-kit folder + bless the full-page tiers
Establish the explicit 2-tier model in one place (`components/ui/state/`): full-page (`EmptyHero`, and a full-page error) + inline (`StateNotice`, `ErrorRecovery`, `ActionFailureInline`).
- Move `ErrorState` into `components/ui/state/` and retune it to `stateTokens` (it currently uses raw `constants/colors` terracotta + `typography` instead of the kit's `stateColors`/`stateRadii`/`stateSpacing`). Keep its full-page shape and behavior; this is a token+location pass, not a rewrite. Update the 34 import paths (mechanical).
- If canon names the full-page error tier something specific, rename to match; otherwise keep `ErrorState` and document it as the sanctioned full-page error tier so it stops getting flagged as legacy.

## Task H1-2 — EmptyState → EmptyHero (genuine same-tier migration, 9 files)
Unlike the error case, `EmptyState` (9 uses) and `EmptyHero` (6 uses) ARE the same tier (full-page empty) — this is a real migration. Verify the two are behaviorally equivalent, then migrate the 9 `EmptyState` callers to `EmptyHero` and delete `EmptyState`. Files: concierge chat/history, trips/all, atlas narration-history/saved-places/voice-logs, dev/gallery, venue/[venueId], your-map. (`dev/gallery` is dev-only — migrate or leave, low stakes.)

## Task H1-3 — ActionFailureInline: wire it or remove it (0 callers today)
`components/ui/state/ActionFailureInline.tsx` is defined but never used. It's the inline "that action didn't go through" tier. Either:
- (recommended) wire it into the sites that currently hand-roll inline action failures or fall back to toast-only errors (profile toast-only errors; the hand-rolled cards in H1-4), OR
- if nothing genuinely needs it, remove it so the kit has no dead members.
Decide based on H1-4's findings — if the hand-rolled patterns want an inline-failure component, this is it.

## Task H1-4 — Fold hand-rolled patterns into the kit (7 sites)
These bypass the kit with bespoke Views — replace with the matching kit component:
- `components/trip/TripFolioHome.tsx:2125-2138` (local error card → `ErrorState` or `ErrorRecovery` per tier).
- `components/booking/BookingProposalCard.tsx:345-351` (inline booking error → `ErrorRecovery`/`ActionFailureInline`).
- `components/discover/DiscoverCoverHome.tsx:1256-1258` (empty → `EmptyHero`).
- `components/trip-map/TripMapRouteSheet.tsx` (offline chip/footer → `StateNotice` tone="offline").
- `components/chat/ErrorBanner.tsx` (slim animated banner → `StateNotice`, or bless as chat-specific if canon wants a distinct chat treatment — verify).
- `components/trips/TripsHomeViews.tsx` `TripsOfflineBanner` (hand-rolled → `StateNotice`/`OfflineNotice`).
- `components/expense/CostsEmptyState.tsx` — likely a **legitimate** bespoke empty (starters composition, canon-exact per G2). Verify against canon; probably leave, don't fold.

## Task H1-5 — Centralize copy rules in stateTokens (small)
`stateTokens.ts` encodes colors/radii/spacing but no copy guidance — the oxblood color rule exists, copy is ad-hoc per component. Add the State System's copy rules (tone, tense, "no raw error text to users" — already the ErrorState convention) as a documented block or `stateCopy` helper so they're enforced in one place, not re-derived per surface.

## Done
State kit lives in one folder with an explicit full-page/inline 2-tier model · `ErrorState` moved in + token-retuned (callers' imports updated, behavior unchanged) · `EmptyState`→`EmptyHero` migration complete + legacy deleted · `ActionFailureInline` wired or removed (decision recorded) · 6 of 7 hand-rolled patterns folded (CostsEmptyState verified as sanctioned) · copy rules centralized · report the final legacy count (target: zero forked duplicates, ErrorState blessed as a tier not debt).

## Scope honesty
This is mostly-invisible refactor (error/empty screens keep working either way). The user-visible wins are the 7 hand-rolled patterns gaining kit consistency and the folder de-fork. If Batch H must be trimmed for dogfood timing, H1-4 (hand-rolled fold) is the keeper; H1-1's 34-import move is safe but low-signal and can trail. Flag if any consolidation surfaces a real broken state (not just stylistic drift).
