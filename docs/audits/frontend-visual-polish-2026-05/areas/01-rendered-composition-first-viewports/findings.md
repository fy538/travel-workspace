# Rendered Composition And First Viewports Findings

## Summary

Screenshots were not available in this local pass. `react-native-web` is not installed, no iOS simulator was booted, `maestro` was not on `PATH`, and no prior dogfood screenshots were present in the repo beyond app icons. This report is therefore a static composition-risk audit from code, with references to the existing Maestro visual QA flows.

Overall: the app has real design momentum, but the first viewport still risks feeling more assembled than composed on several high-traffic screens. Trips list and private Vesper chat are closest to the doctrine. The biggest dogfood polish gaps are Discover, Me, and the trip workspace header/plan stack, where useful content competes with persistent chrome, peer tabs, filters, and many same-weight modules.

Severity: no P0. Highest issues are P1 because they affect trust and premium feel during first-week dogfooding.

## Screens/Surfaces Reviewed

- Trips list: `Travel App/app/(tabs)/trips/index.tsx`, `Travel App/components/trip/TripCard.tsx`
- Trip home / plan landing: `Travel App/app/(tabs)/trips/[tripId]/index.tsx`, `Travel App/components/trip/TripHeader.tsx`
- Private Vesper chat: `Travel App/app/(tabs)/concierge/chat.tsx`, `Travel App/components/chat/PrivateVesperNote.tsx`
- Group trip chat: `Travel App/app/(tabs)/trips/[tripId]/chat.tsx`, `Travel App/components/chat/group/GroupThreadItem.tsx`, `Travel App/components/chat/group/VesperNote.tsx`
- Plan timeline: `Travel App/app/(tabs)/trips/[tripId]/plan.tsx`, `Travel App/components/trip-plan/PlanDaySection.tsx`, `Travel App/components/trip-plan/PlanBlockRow.tsx`
- Discover: `Travel App/app/(tabs)/discover/index.tsx`, `Travel App/components/discover/FeedItemRenderer.tsx`
- Me: `Travel App/app/(tabs)/me/index.tsx`, `Travel App/components/me/TravelDNACard.tsx`

## Findings

### P1 - Trip workspace first viewport carries too much chrome before the page can declare a focal point

The trip workspace header stacks safe-area chrome, back/settings, trip switcher, avatar stack, and a full segmented control before the plan landing content begins. `TripHeader` renders the header row plus `NavPills` at `Travel App/components/trip/TripHeader.tsx:98` and `Travel App/components/trip/TripHeader.tsx:134`; the styles add top safe-area padding, horizontal/vertical header padding, and a separate pill row at `Travel App/components/trip/TripHeader.tsx:151` and `Travel App/components/ui/NavPills.tsx:150`. The plan landing then opens with `LiveTodaySection`, `ConciergeAttentionSection`, cross-trip thread, and For This Trip preview before Days at `Travel App/app/(tabs)/trips/[tripId]/index.tsx:193`, `Travel App/app/(tabs)/trips/[tripId]/index.tsx:211`, `Travel App/app/(tabs)/trips/[tripId]/index.tsx:232`, and `Travel App/app/(tabs)/trips/[tripId]/index.tsx:244`.

This may be functionally justified, and the comment acknowledges the navigation dependency at `Travel App/app/(tabs)/trips/[tripId]/index.tsx:14`, but visually it risks a project-workspace feel before the user sees the trip's actual story. Apple HIG layout guidance emphasizes respecting platform structure while keeping content primary; Vesper's own doctrine asks for quiet hierarchy and less dashboard energy.

### P1 - Discover opens as a browse console, not an opinionated place-aware surface

Discover leads with an absolute fixed header containing search plus six peer pills: `Angles`, `Friends`, `For you`, `Events`, `Trending`, `Guides` at `Travel App/app/(tabs)/discover/index.tsx:53` and `Travel App/app/(tabs)/discover/index.tsx:700`. The header is overlaid and content is pushed down by `headerHeight + 8` at `Travel App/app/(tabs)/discover/index.tsx:784`, while the first content block is a small "The index for" label, city row, Near Me button, subtitle, view toggle, then angle cards at `Travel App/app/(tabs)/discover/index.tsx:790`, `Travel App/app/(tabs)/discover/index.tsx:801`, and `Travel App/app/(tabs)/discover/index.tsx:933`.

The code itself flags this risk: the TODO at `Travel App/app/(tabs)/discover/index.tsx:722` says six peer pills make Discover read like a browse console before Vesper expresses an opinion. That is exactly the composition issue. It conflicts with the product doctrine that Vesper should be opinionated and place-aware, not a generic travel index.

### P1 - Discover and Me still lean on generic placeholder/color-block imagery where travel specificity should carry trust

Travel products need the first viewport to prove "real place, real light." Trips list is in better shape because `TripCard` uses destination-keyed honest illustration at `Travel App/components/trip/TripCard.tsx:50` and renders the hero illustration at `Travel App/components/trip/TripCard.tsx:134`. Discover and Me are weaker: Discover masonry cards use flat gradient/color blocks as image areas at `Travel App/app/(tabs)/discover/index.tsx:1443` and `Travel App/app/(tabs)/discover/index.tsx:1527`; feed cards use color dots and placeholder image blocks at `Travel App/components/discover/FeedItemRenderer.tsx:115`, `Travel App/components/discover/FeedItemRenderer.tsx:259`, `Travel App/components/discover/FeedItemRenderer.tsx:308`, and `Travel App/components/discover/FeedItemRenderer.tsx:344`. Me trip highlights similarly render a colored block with an image icon at `Travel App/app/(tabs)/me/index.tsx:238`.

This is a perceived-polish issue more than a correctness bug. Vesper's brand brief explicitly prefers photography-led, place-anchored editorial references and "real places, real light." Placeholder gradients make seeded dogfood data feel mock-like even when the content is useful.

### P1 - Me first viewport has a coherent intent but still reads like stacked identity modules

The Me tab has improved IA: profile, Travel DNA, an insight card, then Library and Settings groupings. But the first viewport is still a vertical sequence of center-aligned identity header, optional DNA card, and Vesper insight without one dominant composition. The screen header is at `Travel App/app/(tabs)/me/index.tsx:112`, the centered profile block at `Travel App/app/(tabs)/me/index.tsx:137`, Travel DNA immediately after at `Travel App/app/(tabs)/me/index.tsx:168`, and insight card at `Travel App/app/(tabs)/me/index.tsx:174`. Styles reinforce the module stack: page padding at `Travel App/app/(tabs)/me/index.tsx:501`, profile vertical margin at `Travel App/app/(tabs)/me/index.tsx:502`, card spacing at `Travel App/components/me/TravelDNACard.tsx:118`, and a plain insight row at `Travel App/app/(tabs)/me/index.tsx:511`.

This is not broken. It is just a little generic for a profile surface that should make the user's relationship with Vesper feel distinct and durable. The first viewport needs a stronger focal hierarchy: either the personal memory/DNA card is the hero, or the profile identity is.

### P2 - Plan timeline is information-rich but can become a dense card-inside-timeline stack

The deep Plan timeline opens with status rail, change strip, optional morning briefings, then day sections at `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:191`, `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:203`, and `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:247`. Each Plan v2 day wraps opener, blocks, closing copy, and decisions inside a card at `Travel App/components/trip-plan/PlanDaySection.tsx:173`, and each block adds timeline dots, badges, notes, flags, booking state, decision tags, why rows, changed banners, diff chips, suggestions, mark-done controls, and travel segments across `Travel App/components/trip-plan/PlanBlockRow.tsx:167`, `Travel App/components/trip-plan/PlanBlockRow.tsx:225`, `Travel App/components/trip-plan/PlanBlockRow.tsx:253`, `Travel App/components/trip-plan/PlanBlockRow.tsx:256`, `Travel App/components/trip-plan/PlanBlockRow.tsx:257`, `Travel App/components/trip-plan/PlanBlockRow.tsx:269`, `Travel App/components/trip-plan/PlanBlockRow.tsx:278`, `Travel App/components/trip-plan/PlanBlockRow.tsx:286`, and `Travel App/components/trip-plan/PlanBlockRow.tsx:294`.

The component is thoughtfully structured, but on a small first viewport the visible result can feel like operational density rather than a calm itinerary. This is a composition risk: too many inline controls and states can flatten priority unless the first day has a stronger visual lead.

### P2 - Chat surfaces are directionally right, but first viewport chrome and bars can crowd the conversation substrate

Private chat now follows the locked envelope pattern: AI turns route to `PrivateVesperNote` at `Travel App/app/(tabs)/concierge/chat.tsx:74`, and the note uses article-scale Fraunces with hairline attribution at `Travel App/components/chat/PrivateVesperNote.tsx:67` and `Travel App/components/chat/PrivateVesperNote.tsx:183`. That is a strong product-signature surface.

The risk is first-viewport crowding. Private chat adds a custom header, privacy bar, optional error banner, permission banner, geofence banner, lease conflict, FlatList, and composer at `Travel App/app/(tabs)/concierge/chat.tsx:719`, `Travel App/app/(tabs)/concierge/chat.tsx:752`, `Travel App/app/(tabs)/concierge/chat.tsx:765`, `Travel App/app/(tabs)/concierge/chat.tsx:772`, `Travel App/app/(tabs)/concierge/chat.tsx:816`, `Travel App/app/(tabs)/concierge/chat.tsx:829`, `Travel App/app/(tabs)/concierge/chat.tsx:850`, and `Travel App/app/(tabs)/concierge/chat.tsx:941`. Group chat adds the workspace header above the screen, then its own group privacy bar at `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:277` before messages at `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:296`. These bars are useful, but they should be visually audited against the actual first message height on SE-class and Dynamic Type devices.

## Evidence

- Rendered screenshots unavailable: no booted simulator from `xcrun simctl list devices booted`; `npm ls react-native-web --depth=0` returned empty; `command -v maestro` returned empty; no local screenshot assets were found beyond app icons.
- Existing visual QA intent exists in `.maestro/01-trips.yaml`, `.maestro/02-trip-home.yaml`, `.maestro/03-concierge-private-chat.yaml`, `.maestro/04-plan.yaml`, `.maestro/05-discover.yaml`, and `.maestro/06-me.yaml`, with screenshot names for every focus surface.
- Vesper doctrine says the app should feel like a leather travel journal with warm parchment, generous whitespace, quiet hierarchy, and article scale for reading content at `Travel App/docs/Design Language.md:57`, `Travel App/docs/Design Language.md:62`, and `Travel App/docs/Design Language.md:125`.
- Purple is reserved for AI/concierge presence at `Travel App/docs/Design Language.md:84`; this strengthens the case for avoiding decorative purple and keeping AI surfaces visually special.
- The private/group chat substrate is explicitly locked at `Travel App/docs/Design Language.md:230`, and the implementation now follows that direction in `PrivateVesperNote`.
- Platform/accessibility guidance referenced: [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Apple HIG Typography](https://developer.apple.com/design/human-interface-guidelines/typography), [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), and [WCAG 2.2 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum). Apple currently recommends comfortable control sizing and spacing for iOS/iPadOS, while WCAG 2.2 SC 2.5.8 sets a web minimum target-size floor.

## Suggested Fix Direction

1. Start with Discover. Collapse the first viewport to one primary place thesis: destination, Vesper's editorial read, and one primary list of angles. Move Friends/For You/Trending/Guides below the fold or behind a single secondary control. Keep Events contextual, not a top peer mode.
2. Reduce trip workspace chrome only after adding alternate entry points for Chat/Map/Photos/Memory in the landing content. The existing comment is right: do not orphan navigation. But the first viewport should feel like "the trip" before it feels like "workspace tabs."
3. Give Me one hero. Prefer Travel DNA/personal memory as the visual anchor, with the avatar/name becoming supporting metadata. Avoid a profile-card plus DNA-card plus insight-card stack above the fold.
4. Add destination-specific real or honest visual assets to Discover and Me dogfood fixtures first. This will likely improve perceived polish more than another round of spacing tweaks.
5. For Plan timeline, create a calmer first-day treatment: one editorial day opener, fewer visible action links until hover/tap/long press or a contextual "more" row, and a clearer distinction between itinerary content and operational controls.
6. Keep private chat's envelope treatment. The next polish pass should tune its first empty/new-thread state and optional banners so the first Vesper note remains the focal point.

## Verification Ideas

- Run the existing Maestro flows on a booted simulator and capture screenshots: `npm run visual-qa`. Prioritize `trips-list-top`, `trip-home-plan`, `concierge-private-chat`, `trip-home-chat`, `plan-day-top`, `discover-feed-top`, and `me-profile`.
- Repeat screenshots on iPhone SE-class and Pro Max-class simulators, plus one Dynamic Type large accessibility setting.
- For each first viewport, mark the first visual focal point and count chrome rows above useful content. Fail if the focal point is a nav/filter row rather than trip/place/Vesper content.
- Add a visual QA checklist item: "Does this first viewport read as Vesper, or could it belong to any travel app?"
- Validate tap-target overlays for custom header/action controls against Vesper's documented 44pt floor and platform guidance before dogfood.
