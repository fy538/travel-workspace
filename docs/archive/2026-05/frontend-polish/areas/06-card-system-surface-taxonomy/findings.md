# Card System & Surface Taxonomy Findings

## Summary

The app currently has at least **14 visually distinct card-like surface families** in the audited paths: generic white `Card`, `LetterpressCard`, trip postcard/compact/memory cards, trip-home `CardShell` anchor/card variants, chat bubbles, chat attachment cards, chat decision/reaction letterpress cards, group Vesper prose/question cards, Discover angle/feed/event/search/masonry cards, Me identity cards, settings/form cards, dashed prompts/placeholders, skeleton cards, bottom action bars, and small chip-like cards.

Only a few are product-defining: `LetterpressCard`, `TripCard`, trip-home `CardShell`, group `VesperNote`/`PublicQuestion`, and possibly `TravelDNACard`/`CrossTripThreadCard` once converted to the same editorial primitive. The rest are useful utility/list/form surfaces, but they are currently styled with the same generic white-card language as editorial and concierge surfaces. This blurs Vesper's doctrine: "leather travel journal, not a SaaS dashboard."

External baseline used: [Apple HIG Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) for 44x44 pt hit regions, [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) for hierarchy/grouping, [Material Cards](https://m2.material.io/components/cards) for card containment/single-subject rules, [Android touch target guidance](https://support.google.com/accessibility/android/answer/7101858?hl=en) for 48dp targets, and [WCAG 2.2 Target Size](https://www.w3.org/TR/WCAG22/#target-size-minimum) for the 24px AA floor / 44px AAA target.

## Findings

### P1 - There is no enforceable distinction between editorial cards and generic utility cards

The canonical card primitive is plain white with a hairline border (`components/ui/Card.tsx:15`), while the brand primitive says it should replace generic hairline cards on brand-aligned surfaces (`components/brand/LetterpressCard.tsx:1`, `components/brand/LetterpressCard.tsx:33`). Product-defining trip cards do use letterpress (`components/trip/TripCard.tsx:54`, `components/trip/TripCard.tsx:99`, `components/trip/TripCard.tsx:128`), but high-traffic Discover, Concierge, Me, and chat modules still recreate generic white cards locally (`components/angles/AngleCard.tsx:100`, `components/chat/VenueCard.tsx:87`, `app/(tabs)/concierge/index.tsx:225`, `app/(tabs)/me/index.tsx:627`, `app/(tabs)/discover/index.tsx:1580`).

Dogfood impact: first-week users see the signature trip card, then many adjacent modules look like ordinary mobile dashboard rows. That weakens trust and premium feel without breaking task completion.

### P1 - Concierge and memory surfaces use sacred purple but not the sacred surface

Vesper/AI memory modules often use purple accents inside plain white cards: `TravelDNACard` is a white card with purple border/icon (`components/me/TravelDNACard.tsx:74`, `components/me/TravelDNACard.tsx:113`), `CrossTripThreadCard` mirrors that treatment (`components/trip-home/CrossTripThreadCard.tsx:49`, `components/trip-home/CrossTripThreadCard.tsx:96`), and private chat AI still renders a purple bubble plus badges (`components/chat/MessageBubble.tsx:84`, `components/chat/MessageBubble.tsx:99`, `components/chat/MessageBubble.tsx:263`). Meanwhile trip-home already has the better product pattern: sacred-tint `CardShell` for Vesper speaking (`components/trip-home/CardShell.tsx:17`, `components/trip-home/AnchorCard.tsx:40`).

Dogfood impact: purple signals "Vesper is here," but the surface often feels like a tag applied to generic chrome rather than the agent's own material.

### P2 - Discover has the highest card-taxonomy drift

Discover mixes angle editorial cards, feed cards, event cards, venue teasers, rec rows, search rows, masonry destination cards, guide cards, prompt cards, and bottom CTA bars in one screen file. Examples include `AngleCard` (`components/angles/AngleCard.tsx:40`, `components/angles/AngleCard.tsx:99`), feed `Card` wrappers (`components/discover/FeedItemRenderer.tsx:52`, `components/discover/FeedItemRenderer.tsx:307`, `components/discover/FeedItemRenderer.tsx:343`), local teaser styles (`components/discover/FeedItemRenderer.tsx:425`, `components/discover/FeedItemRenderer.tsx:452`, `components/discover/FeedItemRenderer.tsx:470`), search/nearby cards (`app/(tabs)/discover/index.tsx:1580`, `app/(tabs)/discover/index.tsx:1665`), and masonry cards (`app/(tabs)/discover/index.tsx:1407`, `app/(tabs)/discover/index.tsx:1808`).

Dogfood impact: the tab is supposed to be an opinionated index of place intelligence, but its card styles read like accumulated feed modules. Material's card guidance says cards should be single-subject, independent, and easy to scan; Discover currently has too many card dialects for users to learn quickly.

### P2 - Cards are sometimes nested or visually over-framed

The plan screen highlights an entire day section with a white bordered wrapper, then places a `Card` timeline inside it (`app/(tabs)/trips/[tripId]/plan.tsx:260`, `app/(tabs)/trips/[tripId]/plan.tsx:285`, `app/(tabs)/trips/[tripId]/plan.tsx:447`). Events wrap a full `EventCard` in an outer `Tap`, so the touch/action layer and visible card are separate (`app/(tabs)/discover/index.tsx:1358`, `app/(tabs)/discover/index.tsx:1365`). `ExperienceDetailSheet` uses card-shaped subpanels inside a sheet (`components/discover/ExperienceDetailSheet.tsx:357`, `components/discover/ExperienceDetailSheet.tsx:615`, `components/discover/ExperienceDetailSheet.tsx:685`). These are not catastrophic, but they make hierarchy feel noisier and less native.

Dogfood impact: over-framing makes Vesper feel more like admin software, especially in itinerary and event workflows where the user needs calm hierarchy.

### P2 - Small card controls do not consistently meet the app's own target-size floor

The design tokens define `a11y.minTouchTarget` as 44 (`constants/layout.ts:57`), matching Apple HIG's 44x44 pt baseline and exceeding WCAG's 24px AA minimum. Some card controls remain visibly and structurally smaller: `CardShell` dismiss is 32x32 (`components/trip-home/CardShell.tsx:94`, `components/trip-home/CardShell.tsx:126`), `TravelDNACard` dispute is 22x22 plus hitSlop (`components/me/TravelDNACard.tsx:85`, `components/me/TravelDNACard.tsx:154`), `FeedItemRenderer` dismiss is a small icon/padding target (`components/discover/FeedItemRenderer.tsx:123`, `components/discover/FeedItemRenderer.tsx:417`), and `CaptureNudgeCard` uses a text send control with padding but no min dimension (`components/trip-home/CaptureNudgeCard.tsx:168`, `components/trip-home/CaptureNudgeCard.tsx:239`).

Dogfood impact: these are exactly the card-edge controls users tap while moving. Misses feel cheap even when the underlying action works.

### P3 - Form/list/settings surfaces are correctly generic, but the primitive name encourages overuse

Settings and form screens sensibly use plain cards for dense grouped controls (`app/(tabs)/me/account.tsx:314`, `app/(tabs)/me/account.tsx:339`, `app/(tabs)/me/constraints.tsx:188`, `app/(tabs)/me/constraints.tsx:319`, `app/(tabs)/me/phone.tsx:178`). The problem is naming: `Card` sounds like the default for all surfaces, even though Vesper's brand card is `LetterpressCard`. This encourages new product modules to reach for generic white cards unless reviewers catch it.

## Evidence

- **Product-defining surfaces already know the right direction:** `LetterpressCard` implements the locked pressed-paper treatment (`components/brand/LetterpressCard.tsx:1`), trip cards route all variants through it (`components/trip/TripCard.tsx:50`, `components/trip/TripCard.tsx:95`, `components/trip/TripCard.tsx:123`), and trip-home `CardShell` wraps active/ambient Vesper cards with explicit emphasis/tint axes (`components/trip-home/CardShell.tsx:17`, `components/trip-home/CardShell.tsx:51`).
- **Generic utility cards dominate many secondary surfaces:** chat attachments use white card shells (`components/chat/VenueCard.tsx:87`, `components/chat/ItineraryCard.tsx:55`, `components/chat/MapCard.tsx:173`), Concierge lists use white conversation/suggestion cards (`app/(tabs)/concierge/index.tsx:225`, `app/(tabs)/concierge/index.tsx:269`), and Me uses white rows/cards for activity, saved venues, bottom links, and voice previews (`app/(tabs)/me/index.tsx:338`, `app/(tabs)/me/index.tsx:616`, `app/(tabs)/me/index.tsx:627`).
- **Some object cards already use a better middle tier:** `ReactionCard`, `VoteWidgetCard`, and group `PublicQuestion` use `letterpress.cardBg` and `letterpress.shadow` while staying action-oriented (`components/chat/ReactionCard.tsx:92`, `components/chat/VoteWidgetCard.tsx:180`, `components/chat/group/PublicQuestion.tsx:48`).
- **Skeleton and placeholder surfaces are separate but visually adjacent to cards:** `InlinePlaceholder` uses dashed scaffolding (`components/ui/InlinePlaceholder.tsx:58`) and `SkeletonCard` defines loading card shapes (`components/ui/Skeleton.tsx:152`). These should remain non-content surfaces, not become another content-card style.

## Suggested Fix Direction

Enforce this taxonomy before dogfooding:

1. **EditorialCard / LetterpressCard:** product-defining content, Vesper-authored prose, trip memory, trip identity, place theses, Travel DNA, cross-trip threads. Use letterpress background/shadow, article typography when reading matters, and sacred purple only for Vesper attribution.
2. **ActionModule:** decisions, reactions, votes, approval cards, pending prompts, capture nudges. Use `CardShell` or a generalized `ActionModuleShell`; whole-card primary action, supplemental actions limited and consistently placed.
3. **UtilityPanel:** settings, forms, constraints, account, phone verification, dense configuration. Plain `Card` is allowed here.
4. **ListRow:** conversation previews, search results, saved venues, history sessions, bottom links. These should not pretend to be editorial cards; use row primitives with 44pt minimum height and minimal border.
5. **MediaCard:** trip postcards, friend moments, destinations, guides. Must have real/destination-aware imagery or honest illustration fallback, not arbitrary gradient placeholders.
6. **InlineScaffold:** skeletons, empty inline placeholders, dashed upload slots. Never use for real content.
7. **SheetSection:** subpanels inside sheets. Prefer dividers and full-width sections over card-in-sheet framing unless the section is independently actionable.

Specific migrations:

- Convert `TravelDNACard` and `CrossTripThreadCard` to `LetterpressCard` or a new `EditorialMemoryCard`.
- Keep `Card` but rename/re-document it as `UtilityPanel` or add a lint/review rule: generic `Card` is allowed only in forms/settings/dense utility.
- Move Discover card styles into named primitives: `AngleEditorialCard`, `FeedTeaserRow`, `EventListRow`, `MasonryMediaCard`, `SearchResultRow`.
- Replace private `MessageBubble` AI rendering with the envelope/editorial substrate already described in the design docs; reserve bubbles for user and group participant speech.
- Add an `IconButton`/`CardDismissButton` primitive that guarantees 44x44 iOS / 48dp Android targets while preserving small visual icons.

## Verification Ideas

- Static check: fail new uses of `colors.white + layout.cardRadius + hairline border` outside `components/ui/Card.tsx`, `UtilityPanel`, and approved list-row primitives.
- Snapshot inventory: generate a "surface zoo" screen rendering every taxonomy primitive in default, pressed, disabled, loading, and error states.
- Accessibility pass: inspect card-edge controls for at least 44x44 pt on iOS and 48dp on Android; treat WCAG 2.2's 24px AA target as a floor, not Vesper's bar.
- Design review checklist: every new card-like surface must declare one taxonomy role and one primary action. If it has more than two supplemental actions, redesign as a sheet or row list.
