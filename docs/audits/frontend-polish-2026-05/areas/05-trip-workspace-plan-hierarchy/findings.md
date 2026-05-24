# Trip Workspace Plan Hierarchy Findings

## Summary

No P0 issues found. The trip workspace is functional and has several brand-aligned pieces, especially the Vesper anchor and letterpress day rows. The dogfood polish risk is hierarchy: the user enters a trip through a globally tabbed app, then immediately gets a persistent trip header, a persistent segmented rail, and multiple section-level modules that all ask to be treated as navigation or attention surfaces.

The result makes Plan feel less like the primary trip workspace and more like one equal mode among Chat, Map, Photos, and Memory. This conflicts with Vesper's own doctrine of restraint and with mobile platform guidance to concentrate on primary content, limit onscreen controls, and keep touch targets comfortably sized.

## Findings

### P1 - The first viewport is over-chromed before the trip content can breathe

The workspace layout always renders `TripHeader` above every trip sub-screen, then the app-level bottom tabs remain present underneath the trip stack. `TripHeader` itself contains a back control, trip switcher, avatar stack, settings control, and a second row of navigation pills.

Evidence: `Travel App/app/(tabs)/_layout.tsx:52` renders the global `Tabs` shell; `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:72` renders `TripHeader` before the nested `Stack`; `Travel App/components/trip/TripHeader.tsx:97` through `Travel App/components/trip/TripHeader.tsx:147` renders the top row plus `NavPills`; `Travel App/components/ui/NavPills.tsx:149` through `Travel App/components/ui/NavPills.tsx:157` adds a full-width segmented control band.

Why it matters: Vesper's doctrine says "Silence is a design decision" and calls for minimal chrome during live trip moments (`Travel App/docs/Design Language.md:37`, `Travel App/docs/Design Language.md:57`). Apple HIG's current iOS guidance similarly recommends helping people focus by limiting onscreen controls and making secondary actions discoverable with minimal interaction: [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios). In the current structure, the first viewport starts as a navigation system before it starts as a trip.

### P1 - Plan is split between two surfaces, so it does not read as the canonical workspace

The code and comments say the trip detail landing is Plan, but the route graph also has a separate `/plan` screen. Different controls point to different "Plan" destinations: the header Plan pill routes to the trip detail index, while the Vesper anchor and empty-state actions route to `/plan`.

Evidence: `Travel App/utils/routes.ts:13` through `Travel App/utils/routes.ts:15` defines `tripDetail` as the locked Plan landing; `Travel App/utils/routes.ts:23` through `Travel App/utils/routes.ts:28` defines a separate `/plan` route; `Travel App/components/trip/TripHeader.tsx:31` through `Travel App/components/trip/TripHeader.tsx:35` maps `Plan` to `null`, and `Travel App/components/trip/TripHeader.tsx:86` through `Travel App/components/trip/TripHeader.tsx:94` sends `null` to `routes.tripDetail`; `Travel App/components/trip-home/ConciergeAttentionSection.tsx:525` through `Travel App/components/trip-home/ConciergeAttentionSection.tsx:528` sends the anchor to `routes.tripSubPage(tripId, 'plan')`; `Travel App/app/(tabs)/trips/[tripId]/index.tsx:400` through `Travel App/app/(tabs)/trips/[tripId]/index.tsx:407` does the same in the empty state.

Why it matters: the Plan landing file explicitly notes that Plan is home and that the header pills are redundant once the landing carries the workspace destinations (`Travel App/app/(tabs)/trips/[tripId]/index.tsx:4` through `Travel App/app/(tabs)/trips/[tripId]/index.tsx:20`). With both `index.tsx` and `plan.tsx` acting plan-like, users can land in different plan mental models depending on which control they tapped.

### P2 - Persistent low-frequency controls compete with trip tasks

Several controls remain persistent or repeated even though they are likely low-frequency in dogfood use: the back-to-trip-list button, duplicated settings affordances, activity link, per-card dismiss buttons, and "Suggest a change" under every legacy itinerary block.

Evidence: the header back button and settings button are always in the trip header row (`Travel App/components/trip/TripHeader.tsx:100` through `Travel App/components/trip/TripHeader.tsx:132`); tapping the title switcher and the settings icon both open the same `TripSettingsPanel` (`Travel App/components/trip/TripHeader.tsx:109` through `Travel App/components/trip/TripHeader.tsx:145`); the trip home attention section repeats an `activity ->` link in its header (`Travel App/components/trip-home/ConciergeAttentionSection.tsx:503` through `Travel App/components/trip-home/ConciergeAttentionSection.tsx:522`); every dismissable home card gets an overlapping close control (`Travel App/components/trip-home/CardShell.tsx:91` through `Travel App/components/trip-home/CardShell.tsx:104`); each legacy plan block repeats `Suggest a change` (`Travel App/app/(tabs)/trips/[tripId]/plan.tsx:368` through `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:384`).

Why it matters: premium workspace apps keep context persistent but move infrequent actions into contextual overflow, swipe/list actions, or sheet-level affordances. Here, repeated secondary actions make the trip feel more like a dashboard than "a leather travel journal" (`Travel App/docs/Design Language.md:57`).

### P2 - Some navigation and dismissal targets fall below the app's own premium touch target bar

The design system says `minTouchTarget 44pt` is non-negotiable, but several controls rely on text size, icon size, or small hit slop rather than explicit 44pt targets.

Evidence: `Tap` does not enforce a minimum target by default (`Travel App/components/ui/Tap.tsx:55` through `Travel App/components/ui/Tap.tsx:66`); trip segmented cells use `minHeight: 36` (`Travel App/components/ui/NavPills.tsx:202` through `Travel App/components/ui/NavPills.tsx:208`); header icon buttons have only margins, no explicit 44pt box (`Travel App/components/trip/TripHeader.tsx:163` through `Travel App/components/trip/TripHeader.tsx:165`); card dismiss buttons are 32x32 with `hitSlop={10}` and visually overlap the tappable card (`Travel App/components/trip-home/CardShell.tsx:94` through `Travel App/components/trip-home/CardShell.tsx:104`, `Travel App/components/trip-home/CardShell.tsx:126` through `Travel App/components/trip-home/CardShell.tsx:134`); the activity text link is 10px text with `hitSlop={6}` (`Travel App/components/trip-home/ConciergeAttentionSection.tsx:511` through `Travel App/components/trip-home/ConciergeAttentionSection.tsx:519`).

External baseline: Apple accessibility guidance lists 44x44 pt as the default iOS/iPadOS control size and emphasizes spacing between controls: [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Material guidance recommends touch targets of at least 48x48 dp and notes that visual icons can be smaller when padded to a larger target: [Material Accessibility](https://m2.material.io/design/usability/accessibility.html). WCAG 2.2's 24x24 CSS px target-size criterion is a web minimum, not a premium mobile bar: [WCAG 2.2 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum).

### P2 - Map, Photos, and Memory add local navigation/action chrome on top of the global trip chrome

The secondary trip surfaces each introduce their own always-visible or repeated controls while still sitting under `TripHeader` and the trip nav pills. Map adds day chips floating over the map plus a bottom sheet; Photos adds per-group add controls and bottom add/find actions; Memory adds a consent banner, personal-memory link, and floating add-photos button.

Evidence: Map renders day chips over the map and a bottom sheet in the same viewport (`Travel App/components/trip-map/TripMapScreen.tsx:267` through `Travel App/components/trip-map/TripMapScreen.tsx:309`, styled at `Travel App/components/trip-map/TripMapScreen.tsx:330` through `Travel App/components/trip-map/TripMapScreen.tsx:368`); Photos renders a confirm banner, per-group add button, and bottom action row (`Travel App/app/(tabs)/trips/[tripId]/photos.tsx:258` through `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:313`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:405` through `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:430`); Memory renders a consent banner, a personal-memory row, and a floating add button (`Travel App/app/(tabs)/trips/[tripId]/memory.tsx:141` through `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:155`, `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:226` through `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:270`).

Why it matters: these surfaces are valuable, but when each carries local controls plus global trip controls, the nested navigation feels heavy. Apple's HIG overview emphasizes clear hierarchy where controls elevate the content beneath them, not compete with it: [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines).

## Evidence

Internal doctrine and implementation:

- Vesper doctrine: "Silence is a design decision" and the app should feel like "a leather travel journal, not a SaaS dashboard" (`Travel App/docs/Design Language.md:37`, `Travel App/docs/Design Language.md:57`).
- Purple and agent presence are reserved for AI/concierge surfaces (`Travel App/docs/Design Language.md:61`, `Travel App/docs/Design Language.md:84`).
- App touch target floor is 44pt (`Travel App/docs/Design Language.md:153` through `Travel App/docs/Design Language.md:154`).
- The audit README already flags trip workspace layered chrome as a dogfood polish risk (`docs/audits/frontend-polish-2026-05/README.md:176` through `docs/audits/frontend-polish-2026-05/README.md:195`).

External guidance:

- [Apple HIG - Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios): limit onscreen controls so people can concentrate on primary tasks and content.
- [Apple HIG - Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): default iOS/iPadOS control size is 44x44 pt, and spacing between controls matters.
- [Material Design - Accessibility](https://m2.material.io/design/usability/accessibility.html): 48x48 dp touch targets, with padding allowed to make small visual icons easier to tap.
- [WCAG 2.2 - Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum): 24x24 CSS px minimum target size for pointer inputs, with exceptions.

## Suggested Fix Direction

Make the trip detail index the canonical workspace. Rename the mental model from "Plan tab" to "Trip home / Plan workspace" in code and navigation, then reserve `/plan` for a clearly named timeline/detail view or fold it into the landing.

Collapse the persistent trip header after the first scroll or after entering secondary surfaces. Keep the trip title as context, but move settings, activity, and member details into a contextual menu or a single trip info sheet. Let native back behavior carry return navigation instead of keeping a prominent back-to-list button in every trip sub-screen.

Demote Chat, Map, Photos, and Memory from equal persistent pills to contextual actions from the trip workspace: Map from location/route modules, Photos from Memory/live capture modules, Memory after completion, Chat from Vesper/group coordination cards. If a rail remains, treat it as a compact overflow or phase-specific switcher, not a permanent second tab bar.

Standardize icon/text-only action targets through an `IconButton` or enhanced `Tap` target mode so header icons, dismiss controls, day chips, and text links all meet at least 44pt without each caller hand-rolling hit slop.

Convert repeated low-frequency controls into contextual actions: card dismiss via swipe/long-press or an overflow affordance, activity inside trip info/history, and `Suggest a change` as a revealed row action or sheet option after selecting a block.

## Verification Ideas

Run screenshot QA on small iPhone, standard iPhone, and large Dynamic Type for: trip home first viewport, Map, Photos empty/populated, Memory empty/populated, and Plan timeline. Check how many controls appear before the first trip-specific content line.

Add a temporary touch-target debug overlay or accessibility test pass to verify TripHeader icons, segmented cells, card dismiss buttons, activity links, map day chips, photo add buttons, and memory FAB meet the 44pt app floor.

Dogfood task script: "open a live trip, find tonight's plan, inspect the route, add a photo, then return to the plan." Count taps, note moments where two navigation systems offer similar destinations, and verify that back behavior returns within the workspace rather than ejecting the user unexpectedly.
