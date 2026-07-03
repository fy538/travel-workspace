# Summary

Static audit only. I did not edit product code and did not run large-text screenshots: iOS simulators are installed but none were booted, and the Maestro CLI was not available on PATH in this session. The codebase has clear accessibility intent in recent primitives (`IconButton`, `Badge`, `Button`, `ListRow`, `NavPills` trip variant), but the adoption is uneven. The main dogfood risk is not a single P0 blocker; it is that large text and reduced color perception will expose older compact controls, one-line truncation, faint tertiary text, and color-only selected states on high-traffic screens.

External comparison anchors: Apple HIG expects accessible layouts, Dynamic Type support, sufficient contrast, and comfortable controls; the app's own design language sets a 44 pt touch target floor. WCAG 2.2 gives useful floors for contrast and target size, but Vesper should hold itself to the stronger iOS/mobile bar.

# Accessibility Conditions Reviewed

- Static review of typography, color, touch target, truncation, absolute positioning, and selected/disabled states across the requested focus files.
- Contrast spot-checks against app tokens: `colors.text.tertiary` (`#9C9A90`) is about `2.82:1` on white and `2.39:1` on the parchment canvas, below WCAG normal-text contrast. `colors.text.secondary` is much safer at about `5.51:1` on white and `4.65:1` on canvas.
- Runtime inspection with larger text was unavailable in this pass. Screens most in need of large-text screenshot review are listed below.

# Findings

## P1 - Some tappable controls still miss the 44 pt floor

`Tap` has a good `minTarget="auto"` mode, but it defaults to no enforcement (`Travel App/components/ui/Tap.tsx:32`, `Travel App/components/ui/Tap.tsx:39`, `Travel App/components/ui/Tap.tsx:53`). `IconButton` solves this for bare icons (`Travel App/components/ui/IconButton.tsx:1`, `Travel App/components/ui/IconButton.tsx:84`), but many local controls still hand-roll compact hit areas.

Concrete risk examples:

- `ScreenHeader` icon actions are `22 pt` icons with `8 pt` padding and no `minTarget`, making the visual/control frame roughly `38 pt` (`Travel App/components/ui/ScreenHeader.tsx:95`, `Travel App/components/ui/ScreenHeader.tsx:99`, `Travel App/components/ui/ScreenHeader.tsx:130`).
- `NotificationBell` uses a `22 pt` icon with `8 pt` padding and an absolutely positioned badge (`Travel App/components/ui/NotificationBell.tsx:31`, `Travel App/components/ui/NotificationBell.tsx:38`, `Travel App/components/ui/NotificationBell.tsx:54`, `Travel App/components/ui/NotificationBell.tsx:58`).
- Chat/location banners use compact action pills and close controls: `GeofenceBanner` action padding is only `2 pt` vertical and the close icon is a `Pressable` with hit slop rather than a guaranteed 44 pt frame (`Travel App/components/chat/GeofenceBanner.tsx:54`, `Travel App/components/chat/GeofenceBanner.tsx:64`, `Travel App/components/chat/GeofenceBanner.tsx:100`); `ContentGraphBanner` has the same pattern (`Travel App/components/chat/ContentGraphBanner.tsx:50`, `Travel App/components/chat/ContentGraphBanner.tsx:58`, `Travel App/components/chat/ContentGraphBanner.tsx:106`).
- Discover event filters use small horizontal pills (`Travel App/app/(tabs)/discover/index.tsx:1290`, `Travel App/app/(tabs)/discover/index.tsx:1315`, `Travel App/app/(tabs)/discover/index.tsx:263`) and the search clear button is only a small icon plus hit slop (`Travel App/app/(tabs)/discover/index.tsx:1282`).
- `BlockWhyRow` collapsed state is a small inline tap with `paddingVertical: 3` (`Travel App/components/trip/BlockWhyRow.tsx:56`, `Travel App/components/trip/BlockWhyRow.tsx:97`).

This is a P1 because it affects repeated, high-traffic controls and motor-accessibility polish, but it is not access-blocking: many controls are labeled and some have hit slop.

## P1 - Meaningful tertiary text remains too faint in several surfaces

The color tokens already document that `text.tertiary` is decorative-only and metadata should use `colors.metadata.default` (`Travel App/constants/colors.ts:128`, `Travel App/constants/colors.ts:135`; `Travel App/constants/typography.ts:232`). Several meaningful labels still use tertiary, which will look especially thin with larger text, bright environments, low vision, or photo/canvas variation.

Examples:

- Default `NavPills` inactive labels use tertiary (`Travel App/components/ui/NavPills.tsx:170`), and this component is used for Discover's six top-level modes (`Travel App/app/(tabs)/discover/index.tsx:722`, `Travel App/app/(tabs)/discover/index.tsx:734`).
- Venue recommendation type metadata uses tertiary (`Travel App/components/chat/VenueCard.tsx:67`, `Travel App/components/chat/VenueCard.tsx:106`).
- Live-trip timeline text uses tertiary for done times/titles, free-day copy, "View full day", and quiet group copy (`Travel App/components/trip/LiveTodaySection.tsx:349`, `Travel App/components/trip/LiveTodaySection.tsx:359`, `Travel App/components/trip/LiveTodaySection.tsx:390`, `Travel App/components/trip/LiveTodaySection.tsx:401`, `Travel App/components/trip/LiveTodaySection.tsx:467`).
- Transport rows render travel mode and notes in tertiary (`Travel App/components/trip/TravelSegmentRow.tsx:96`, `Travel App/components/trip/TravelSegmentRow.tsx:100`).
- Proposal history timestamps and conflict details use tertiary (`Travel App/components/trip/ProposalReviewSheet.tsx:889`, `Travel App/components/trip/ProposalReviewSheet.tsx:1023`).
- Discover near-me metadata and masonry stats use tertiary (`Travel App/app/(tabs)/discover/index.tsx:1722`, `Travel App/app/(tabs)/discover/index.tsx:1862`).

## P1 - Large text will pressure one-line and absolute-positioned content

The app generally lets native text scale, but several high-value surfaces constrain content to one or two lines inside compact or positioned layouts. At accessibility text sizes, these are likely to truncate important context or collide visually.

Highest-risk examples:

- Trip postcards put title/date over the hero image with absolute positioning and a two-line cap (`Travel App/components/trip/TripCard.tsx:136`, `Travel App/components/trip/TripCard.tsx:137`, `Travel App/components/trip/TripCard.tsx:261`). Long trip names at large text can cover too much of the image or crowd the date.
- `MemoryMomentCard` overlays photo captions absolutely and caps them at two lines (`Travel App/components/trip/MemoryMomentCard.tsx:35`, `Travel App/components/trip/MemoryMomentCard.tsx:131`), and the hero image has fixed `220` height (`Travel App/components/trip/MemoryMomentCard.tsx:147`).
- Proposal diffs force before/after labels to one line (`Travel App/components/trip/ProposalReviewSheet.tsx:471`, `Travel App/components/trip/ProposalReviewSheet.tsx:473`, `Travel App/components/trip/ProposalReviewSheet.tsx:477`), so large text can hide the actual changed item.
- Location/content banners are single-line by design (`Travel App/components/chat/GeofenceBanner.tsx:45`; `Travel App/components/chat/ContentGraphBanner.tsx:43`, `Travel App/components/chat/ContentGraphBanner.tsx:46`).
- Live-trip pulse truncates traveler activity to one line (`Travel App/components/trip/LiveTodaySection.tsx:247`, `Travel App/components/trip/LiveTodaySection.tsx:249`), and today's block titles cap at two lines (`Travel App/components/trip/LiveTodaySection.tsx:100`, `Travel App/components/trip/LiveTodaySection.tsx:107`).
- The composer mitigates long input with `maxHeight: 200` (`Travel App/components/chat/ComposerBar.tsx:495`, `Travel App/components/chat/ComposerBar.tsx:503`), but suggestions are forced to one line with `maxWidth: 280` (`Travel App/components/chat/ComposerBar.tsx:272`, `Travel App/components/chat/ComposerBar.tsx:283`, `Travel App/components/chat/ComposerBar.tsx:453`, `Travel App/components/chat/ComposerBar.tsx:460`).

## P2 - Selected states are often visual-only and not consistently exposed

Some core primitives do this well: `NavPills` sets `accessibilityState.selected` (`Travel App/components/ui/NavPills.tsx:40`, `Travel App/components/ui/NavPills.tsx:95`), and `RadioOption` uses role/state plus a shape change (`Travel App/components/ui/RadioOption.tsx:49`, `Travel App/components/ui/RadioOption.tsx:53`). Other repeated controls rely mostly on background/border/color changes.

Examples:

- `Chip` has a `selected` prop but does not expose `accessibilityState.selected` and has no non-color selected mark (`Travel App/components/ui/Chip.tsx:14`, `Travel App/components/ui/Chip.tsx:31`, `Travel App/components/ui/Chip.tsx:35`).
- `ReactionCard` and `VoteWidgetCard` selected options change tint/border/text color but do not set selected state or add a checkmark/selected label (`Travel App/components/chat/ReactionCard.tsx:63`, `Travel App/components/chat/ReactionCard.tsx:65`, `Travel App/components/chat/VoteWidgetCard.tsx:122`, `Travel App/components/chat/VoteWidgetCard.tsx:124`).
- Discover filters use active color inversion but no selected state (`Travel App/app/(tabs)/discover/index.tsx:1297`, `Travel App/app/(tabs)/discover/index.tsx:1315`, `Travel App/app/(tabs)/discover/index.tsx:1337`, `Travel App/app/(tabs)/discover/index.tsx:1359`).

This is mostly a polish/accessibility semantics issue rather than a pure visual failure, but the same primitive changes would help color-blind and VoiceOver users.

## P2 - Horizontal chrome needs large-text screenshot review

Horizontal navigation is common and mostly intentional, but several areas combine compact labels with fixed or full-width rows:

- Trip workspace can show up to five segmented tabs (`Chat`, `Plan`, `Map`, `Photos`, `Memory`) (`Travel App/components/trip/TripHeader.tsx:47`, `Travel App/components/trip/TripHeader.tsx:134`). The trip variant allows two lines and `adjustsFontSizeToFit` (`Travel App/components/ui/NavPills.tsx:99`, `Travel App/components/ui/NavPills.tsx:105`), which avoids overflow but also shrinks text below the user's requested scale.
- Discover's fixed header contains search plus six peer `NavPills` (`Travel App/app/(tabs)/discover/index.tsx:700`, `Travel App/app/(tabs)/discover/index.tsx:722`, `Travel App/app/(tabs)/discover/index.tsx:734`, `Travel App/app/(tabs)/discover/index.tsx:1579`). The default pill labels do not have a two-line/fitting fallback (`Travel App/components/ui/NavPills.tsx:36`, `Travel App/components/ui/NavPills.tsx:44`, `Travel App/components/ui/NavPills.tsx:158`).
- Discover's city row has a large place label, a chevron, and a "Near me" pill in one row (`Travel App/app/(tabs)/discover/index.tsx:801`, `Travel App/app/(tabs)/discover/index.tsx:812`, `Travel App/app/(tabs)/discover/index.tsx:1649`). Long city names plus large text are likely to compress the "Near me" action.

# Evidence

- Apple HIG accessibility overview: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Apple HIG typography/Dynamic Type guidance: https://developer.apple.com/design/human-interface-guidelines/typography
- Apple HIG layout/touch target guidance: https://developer.apple.com/design/human-interface-guidelines/layout
- WCAG 2.2 contrast guidance: https://www.w3.org/TR/WCAG22/#contrast-minimum
- WCAG 2.2 non-text contrast guidance: https://www.w3.org/TR/WCAG22/#non-text-contrast
- WCAG 2.2 target-size minimum: https://www.w3.org/TR/WCAG22/#target-size-minimum
- Local design target: `Travel App/constants/layout.ts:57` sets `a11y.minTouchTarget` to `44`.
- Local contrast intent: `Travel App/constants/colors.ts:128` says meaningful metadata should not use decorative tertiary.

# Suggested Fix Direction

- Make `Tap` default to the 44 pt floor for controls, or add a stricter `Tappable`/`InlineTap` split so compact inline links are explicit exceptions.
- Replace remaining bare `Tap`/`Pressable` icon controls with `IconButton`, especially header actions, notification bell, banner dismiss buttons, and small clear/remove buttons.
- Promote meaningful supporting text from `colors.text.tertiary` to `colors.metadata.default` or `colors.text.secondary`; keep tertiary for decorative rules, chevrons, and non-semantic dots only.
- Give `Chip`, `ReactionCard`, `VoteWidgetCard`, and Discover filter pills selected accessibility state plus a non-color selected cue such as a checkmark, leading mark, or "Selected" label in the accessible name.
- Create scaling-aware primitives for compact banners and pills: allow wrap to two lines, expand vertically, or collapse secondary copy before truncating the primary content.
- For photo/hero overlays, add large-text variants that move captions below imagery when text scale crosses a threshold.

# Verification Ideas

- Run iOS screenshots at default, Large, Extra Large, and Accessibility Extra Extra Large text sizes on iPhone SE and a Pro-sized device.
- Prioritize screenshots for: Trips list postcard cards, trip workspace header, Discover fixed header and filters, private Vesper chat composer, group chat vote/reaction cards, Plan timeline, ProposalReviewSheet, and Memory moment cards.
- Add a touch-target debug overlay or static check that flags tappables whose rendered/min dimensions are below `44x44`.
- Add a contrast lint/check for `colors.text.tertiary` usage in `Text` styles outside decorative allowlists.
- Add VoiceOver smoke checks for selected chips, vote/reaction choices, Discover filters, and tab/header icon controls.
