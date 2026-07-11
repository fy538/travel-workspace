# Vesper Canon Hygiene Pass — Operations Log (2026-07-05)

Applied locally to a copy of handoff 96 at `~/travel-workspace/design/vesper-canon-anchor/` (now the canonical local anchor for coding agents). To replicate inside Claude Design, paste this log and ask it to apply the same operations — or treat the local anchor as truth and let the Claude Design project lag on hygiene (it only matters if you keep designing there).

## 1. Deleted (17 orphans — zero HTML imports, verified before rm)
vesper-chat-scaffold, places-brief-modal, trip-itinerary-final, trip-itinerary-living, trip-itin-rich, trip-itin-refined, trip-block-tap, trip-popover-variants, places-place-v2, places-spot-v2, places-zoned, places-modern, places-take-cards, places-take-states, places-take2, places-place, places-spot (.jsx)

## 2. Archived to project/_archive/ (36 files)
- 11 chat orphans: vesper-chat-app/thread/fullscreen/group/grouppriv/in-thread/states/switch/voicemix/cross/expand
- 3 trip orphans: trip-home-kit, trip-learn-more, trip-place-page
- 18 dead Discover files (script tags stripped from Vesper Discover.html first): discover-read, read-heroes/-2/-3, read-pov/-2, shapes-room, immersive, sources, feed, feed-variants, feed-paced, discover-1, search, search-b, search-blend, issue, shapes. Discover live set is now exactly: kit, illus, reading-room, dossier-types, cover, feed-states.
- 4 Trips Home legacies (after extraction, below): trips-home-states, trips-home-expand, trips-home-between, trips-home-gaps. trips-home-system KEPT (live HomeSystem artboard).
- KEPT deliberately: vesper-chat-kit/sections/cards-a/cards-b (imported by Vesper Cards.html, not Chat).

## 3. Extractions (dependency closure before archiving Trips Home legacies)
Moved into trips-home-canon.jsx (né trips-v2.jsx): TableCard, RowGlyphs, ListRow, Avatars, OnTheTable, AtlasBridge, BPassage, FriendRow, DraftRow, TableSection — all added to its window export.
Moved into trips-home-canon-screens.jsx: HomeLoading (rescued from trips-home-gaps; still UNMOUNTED — mount or redraw via State System during alignment; comment marks it).

## 4. Renames (all HTML src references updated; zero dangling)
- vesper-chat-v2.jsx → vesper-chat-canon.jsx
- trip-document-unified.jsx → trip-document-canon.jsx
- trips-v2.jsx → trips-home-canon.jsx · trips-v2-screens.jsx → trips-home-canon-screens.jsx
- onboarding-v2-{core,flow,invite,seams}.jsx → onboarding-canon-{core,flow,invite,seams}.jsx
- itinerary-plan.jsx → itinerary-canon.jsx
- v3-shared.jsx → shared-visual-primitives.jsx (8 consuming pages updated — it was never Trips-Home-only)

## 5. Font-import unification (34 pages rewritten)
All pages now load one line: EB Garamond 0,400/0,500/0,600/1,400/1,500 + DM Sans opsz 400–700 + JetBrains Mono 400/500/700. This fixes the 6 pages that loaded Garamond italic-400 only (roman serif could not render) and the 4 missing roman-400.

## 6. Georgia cover fix (17 SVG attrs across the bundle)
`font-family="Georgia, serif"` and `"Georgia,serif"` in inline SVG covers → `"'EB Garamond', Georgia, serif"`. Also fixed the doubled `"EB Garamond", "EB Garamond"` stack in design-system.jsx. Remaining "Georgia" mentions are governance prose only.

## 7. DocImminent landmine defused
Removed the shadowed duplicate `DocImminent` from trip-document-canon.jsx (~line 467). The rendered IMMINENT artboard is trip-imminent.jsx's copy (load order silently won); a tombstone comment marks the removal.

## 8. Banners: 21 → 38 of 41 pages
Added data-canon-banner to 5 CANON pages (Chat, Places, Auth & Invite, Notifications, Universal Search — green) and 12 COMPANION pages (Trip Settings, Proposal Detail, Trip Story, Discover Detail, Discover Map, External Sharing, Guide Reader, Interaction Surfaces, People & Collab, Photo Intake, Saved & Collections, State System — blue). Exempt: Canon Index + Canon Consolidation (the governance pair).

## Deferred (needs design judgment — NOT done)
- **Token-fork consolidation** (16 forks incl. session 5's GC): forked palettes drifted intentionally in places; consolidating changes rendered colors → do in Claude Design with the ranked list (chat → search → notifications → auth/people → settings → proposal → reader/sharing tail → system boards).
- Home dead exports (HistoryBoard, RailEdge/Scene/Bare) — files also contain live components; prune exports only, low value.
- trips-home-system.jsx keep-or-cut (renders a live HomeSystem board).

## Verification (post-pass)
41 HTML pages · 118 live jsx (was 171) · 36 archived · 17 deleted · zero dangling script srcs · zero mount-level unresolved components (Illustration's `Comp` is a destructured local, not a gap) · Trips Home + Discover full dependency-closure verified.
