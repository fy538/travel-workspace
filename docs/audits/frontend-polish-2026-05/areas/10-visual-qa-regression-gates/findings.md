# Visual QA and Regression Gates Findings

## Summary

No P0 issues found. Travel App has the right ingredients for repeatable visual QA: deterministic mock mode, skip-auth local boot, rich Lisbon/Tokyo/Barcelona fixtures, and existing cross-repo reliability scripts. The missing piece is a practical screenshot lane that treats "the screen is the eval" as an engineering gate, not a one-off manual review.

Recommended path: add a small native screenshot workflow first, using the existing Expo/EAS simulator profile plus a lightweight UI automation runner such as Maestro. Add Expo web only as a low-cost internal review target after web dependencies and native-only module fallbacks are made explicit. Defer Storybook until components need isolated state-matrix coverage; it is not the lowest-friction dogfood gate for full-screen polish.

## Findings

### P1 - Visual QA is absent from the app and workspace gates

The app's scripts cover start, lint, typecheck, generated types, and Jest, but no screenshot or visual review command (`Travel App/package.json:5-24`). Workspace gates similarly stop at contract checks, typecheck, Jest, backend tests, and reliability (`Makefile:37-76`; `scripts/offline-qa.sh:19-50`; `scripts/golden-path-qa.sh:19-47`). Travel App CI mirrors that: lint, typecheck, Jest, and API type freshness, with no visual artifact upload (`Travel App/.github/workflows/ci.yml:17-70`, `Travel App/.github/workflows/ci.yml:72-105`).

That conflicts with Vesper's own workflow doctrine: "the screen becomes the eval" (`Travel App/docs/Design Workflow.md:7-18`) and Round 1 should render the current substrate at full visual fidelity (`Travel App/docs/Design Workflow.md:52-56`). The result is predictable dogfood risk: typography regressions, cramped small-device layouts, private/group substrate drift, and touch-target misses can merge even when the offline QA ladder is green.

### P1 - Expo web is advertised but not currently a dependable visual review target

`npm run web` exists (`Travel App/package.json:5-10`) and `app.json` has a web favicon (`Travel App/app.json:68-70`), but the dependency list includes `react-dom` and omits the Expo web dependencies `react-native-web` and `@expo/metro-runtime` (`Travel App/package.json:58-70`, `Travel App/package.json:72-82`). The top-level audit README already records that an attempted Expo web boot failed because `react-native-web` was missing (`docs/audits/frontend-polish-2026-05/README.md:50`).

Expo web is still worth adding because it can make internal visual review cheap, shareable, and scriptable, but it should not be treated as the first dogfood regression gate until maps, media, secure storage, notifications, Clerk branches, and native-only flows have explicit web fallbacks. Expo's current docs say web support starts by installing `react-dom react-native-web @expo/metro-runtime` and running `npx expo start --web`: [Expo web docs](https://docs.expo.dev/workflow/web/).

### P1 - Native simulator screenshots have a clear opening, but no automation surface yet

The repo already has a development EAS profile that builds for the iOS simulator with mock API and skip auth (`Travel App/eas.json:7-19`), while dogfood/preview are real-backend device builds (`Travel App/eas.json:21-47`). Root routing makes mock/skip-auth boots deterministic by redirecting straight to Trips (`Travel App/app/index.tsx:18-24`), and the API facade defaults mock mode on unless explicitly set false (`Travel App/utils/api/index.ts:14-27`).

What is missing is the automation layer: no Maestro/Detox/Storybook/Playwright setup appears in app scripts or repo structure (`Travel App/package.json:72-82` plus no `.maestro`, `e2e`, `.storybook`, or screenshot directory found), and production app/components expose only three `testID` anchors (`Travel App/app/(tabs)/trips/[tripId]/plan.tsx:264`; `Travel App/components/trip-plan/PlanDaySection.tsx:96`; `Travel App/components/trip-map/TripMapStopList.tsx:61`). There are many accessibility labels, which is good for users, but screenshot flows need stable selectors for tab hops, critical CTAs, and scroll anchors.

### P2 - Existing mock data is useful but not yet scenario-addressable enough for screenshots

The mock data already covers the right dogfood spine: live Lisbon, planning Tokyo, completed Barcelona (`Travel App/constants/mocks/trips.ts:6-23`, `Travel App/constants/mocks/trips.ts:25-61`, `Travel App/constants/mocks/trips.ts:63-94`); private concierge and group chat with itinerary/voting/voice content (`Travel App/constants/mocks/chat.ts:6-75`, `Travel App/constants/mocks/chat.ts:79-169`); rich itinerary days with openers, transit, energy rationale, and interludes (`Travel App/constants/mocks/itinerary.ts:77-121`, `Travel App/constants/mocks/itinerary.ts:122-188`); Discover feed variations (`Travel App/constants/mocks/discover.ts:12-19`, `Travel App/constants/mocks/discover.ts:64-90`); and post-trip memory/story content (`Travel App/constants/mocks/memory.ts:7-81`, `Travel App/constants/mocks/memory.ts:97-161`).

For visual regression, though, screenshot seeds need stable scenario names and fixed clocks. Two mock openings use `new Date().toISOString()` (`Travel App/constants/mocks/chat.ts:175-195`), which makes snapshots noisier. More importantly, the current fixtures are domain mocks, not screenshot fixtures: there is no single "dogfood-critical state pack" that says "capture private first-contact, private long reply, group vote pending, live trip home, plan day with conflict, map fallback, memory story, permissions, offline/error."

### P2 - Accessibility and small-device review need to be part of the visual lane

Vesper's design language declares 44pt minimum touch targets as non-negotiable (`Travel App/docs/Design Language.md:153-154`) and the component docs describe `Tap` as the consistent hit-area primitive (`Travel App/docs/Components.md:31-34`). In implementation, `Tap` wraps `Pressable` but does not enforce minimum width/height or hit slop (`Travel App/components/ui/Tap.tsx:55-64`), and `Button` sizes rely on padding rather than explicit `minHeight` (`Travel App/components/ui/Button.tsx:113-135`).

This does not prove any one button is too small, but it means visual QA should include a touch-target overlay pass plus text-size review. Apple HIG recommends comfortable iOS/iPadOS controls and spacing, with 44x44 pt as the default control size in Accessibility guidance: [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility). Android accessibility guidance points to 48x48 dp targets, often via padding around smaller visuals: [Android touch target size](https://support.google.com/accessibility/android/answer/7101858). WCAG 2.2's web floor is lower, 24x24 CSS px with exceptions, so it should be treated as a minimum floor rather than Vesper's premium native target: [WCAG 2.2 Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum).

## Evidence

- Vesper doctrine: the app is a place-aware concierge relationship, not a generic trip planner (`Travel App/docs/Design Language.md:7-10`); the aesthetic target is leather travel journal, not SaaS dashboard (`Travel App/docs/Design Language.md:55-64`); article scale and UI scale are explicitly split (`Travel App/docs/Design Language.md:116-131`).
- Design workflow: rendered screens are the diagnostic instrument (`Travel App/docs/Design Workflow.md:7-18`), and failure modes should be first-class (`Travel App/docs/Design Workflow.md:120-131`).
- Existing validation: mock mode is considered strong for layout, spacing, typography, visual hierarchy, navigation, empty/loading/error states, and local interaction feel (`Travel App/docs/Mock vs Real Parity.md:33-40`).
- Platform baselines: [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Apple HIG Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [Android touch target size](https://support.google.com/accessibility/android/answer/7101858), [WCAG 2.2 Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum).
- Tooling baselines: Expo documents web setup and export at [Expo web docs](https://docs.expo.dev/workflow/web/); Expo supports simulator builds for iOS via EAS profiles: [Expo simulator builds](https://docs.expo.dev/build-reference/simulators); Maestro's `takeScreenshot` command writes PNG artifacts from automated flows: [Maestro takeScreenshot](https://docs.maestro.dev/api-reference/commands/takescreenshot).

## Suggested Fix Direction

Lowest-friction answer to question 1: create a native, mock-mode screenshot lane around the existing iOS simulator development build. Use `EXPO_PUBLIC_USE_MOCK_API=true` and `EXPO_PUBLIC_SKIP_AUTH=true`, boot to `/ (tabs)/trips`, drive a small set of stable routes, and save PNGs to an ignored local artifact directory plus CI artifacts when the lane runs in CI.

Answer to question 2: add simulator screenshot scripts first. Add Expo web second as a review accelerator, not the canonical gate, because web support is currently incomplete. Defer Storybook until reusable component state matrices become painful; it is useful for `TripCard`, `MessageBubble`/future private renderer, `PlanBlockRow`, `CardShell`, `ComposerBar`, and permission/error components, but it will not validate route chrome, safe areas, keyboard, tab bars, map fallbacks, or native text scaling as quickly as simulator screenshots. A custom screenshot route can be helpful later, but start with real routes so navigation, headers, safe areas, and tab state are part of the evidence.

Answer to question 3: seed a `visual-qa` scenario pack with fixed time and fixed IDs. Required seeds: live trip, planning trip, completed trip, empty/no-trip state, private first-contact, private long Vesper note, private streaming/loading state, group chat with vote/proposal, plan day with confirmed/tentative/cancelled/conflict blocks, map with route and map-unavailable fallback, Discover feed with sparse/rich items, Memory story with missing photos, notification unread/read/error, permission rationale, offline banner, and form/error states for expenses/settings.

Answer to question 4: capture these before dogfood:

- Trips tab: list with live/planning/completed cards; empty state.
- Trip workspace: home, chat, plan, map, memory/story, photos, expenses, settings.
- Concierge: conversation home, private first-contact, long reply, streaming, failed send/offline, attachment/voice segment.
- Discover: main feed, place detail, venue detail, angle detail, sparse content.
- Me: profile home, what Vesper knows, constraints/privacy, account, feedback.
- System states: auth/skip-auth entry, notification permission, location/microphone/photo permission, offline/error banners, small-device keyboard composer state.

Answer to question 5: run cheap deterministic checks in CI and richer review locally before release. CI should run lint/typecheck/Jest as today, then a small screenshot smoke on one simulator size only, upload artifacts, and optionally compare against approved baselines once the UI stabilizes. Local pre-release should run the full screenshot matrix across at least iPhone SE-sized width, 390pt iPhone width, large iPhone, one Android emulator, default text size, and large accessibility text. Manual dogfood release review should inspect the artifact gallery rather than relying on memory.

## Verification Ideas

- Add `make visual-qa` as a local-only first step, then wire `visual-qa-smoke` into CI artifact upload after it is reliable.
- Use stable selectors for route tabs, trip cards, composer controls, primary CTAs, and scroll anchors; keep accessibility labels user-facing and add `testID` only where automation needs non-copy selectors.
- Freeze time for visual runs so date labels and "Today" states remain stable; replace screenshot-fixture `new Date()` usage with a fixed QA clock.
- Capture at least two viewport widths before dogfood: small iPhone/SE-class and 390pt-class. Add large text-size captures for private chat, plan, trip home, settings, and composer.
- Include a manual accessibility pass with iOS Accessibility Inspector or Android Accessibility Scanner for touch targets and contrast before any internal release build.
