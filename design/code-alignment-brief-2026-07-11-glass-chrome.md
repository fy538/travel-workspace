# Glass Chrome Alignment Brief

Date: 2026-07-11  
Scope: travel-app header chrome consolidation Phases 0-2

## Landed

- Phase 0 guard: added a Jest convention test that fails on route-level raw
  `Ionicons name="chevron-back"` under `app/**/*.tsx` unless a documented
  allowlist entry accounts for it. The current allowlist is limited to
  non-page controls: onboarding step-back and the trip-dates calendar month
  previous button.
- Phase 0 taxonomy: added `components/ui/HEADER_CHROME.md` with the six-family
  header map and glass variant matrix.
- Phase 0 bell fix: `NotificationBell` now has first-class `variant` support,
  so Trips home asks for `variant="paper"` instead of wrapping the bell in
  `floatingGlassIconButtonStyle('paper')`.
- Phase 1 glass-entry destinations: Notifications, Atlas voice logs, and
  narration history now use floating `EditorialMasthead` paper-glass chrome.
  Notifications keeps the `Mark read` affordance; voice logs keeps search with
  search-open content clearance.
- Phase 2 chat chrome: `FloatingChatHeader` keeps its public props but now
  builds its circular back/options controls on `FloatingGlassIconButton`
  (`paper`) and uses the shared paper-glass surface for the optional text pill.

## Verified Skips

- Phase 3/4 ProductiveHeader migrations that were already on main from PR #66
  were left alone: trip-dates page chrome, trip begin, invite code, Atlas
  boards/shared links, PlanFocusedHeader, Experience dark glass, and
  TripHeader/PageChrome alignment.
- `ReaderChrome` was intentionally not changed to glass.
- Dark glass was not added to parchment task screens.

## Leftovers

- Phase 5 hardening: expand the convention guard to catch bespoke
  `borderRadius: radius.full` back circles outside `FloatingGlassIconButton`
  and the documented header primitives.
- `MemoryStoryHeader` remains parked for the Trip Story J2 pass.
- Device dogfood remains needed before calling these surfaces visually shipped:
  Notifications, Trips home bell entry, Atlas voice logs, narration history,
  concierge chat, trip chat, and conversation-create chat.
