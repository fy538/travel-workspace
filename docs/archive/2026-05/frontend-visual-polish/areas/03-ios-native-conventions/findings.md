# iOS Native Conventions Findings

## Summary

Static audit only. I checked for booted iOS simulators with `xcrun simctl list devices booted`; no devices were booted, so I could not verify runtime screenshots, keyboard geometry, sheet detents, or edge-swipe behavior on-device.

Overall, the app is moving in the right direction: it uses Expo Router native stacks, has a standard four-item bottom tab bar, handles top safe areas in the custom headers, uses `KeyboardAvoidingView` for chat, and has several explicit comments showing prior native-polish fixes. The remaining dogfood risk is not that Vesper ignores iOS; it is that a few high-touch surfaces use custom chrome where native affordances should carry more of the interaction burden.

Severity notes: no P0 findings. The most important issues are P1/P2 dogfood polish risks around form-sheet dismissal, nested navigation semantics, and touch-target consistency.

## Native Conventions Reviewed

- Navigation, tab bars, nested stacks, and back behavior against Apple's [Navigation](https://developer.apple.com/design/human-interface-guidelines/navigation) and [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) guidance.
- Safe-area/layout behavior against Apple's [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) guidance.
- Sheets and modals against Apple's [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) guidance.
- Keyboard/input behavior against Apple's [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) and [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) guidance.
- Touch targets, Dynamic Type, and accessibility basics against Apple's [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) guidance.

## Findings

### P1 - Expense sheets are custom overlays, not native modals, and can dismiss a long form by tapping the backdrop

`AddExpenseSheet` is rendered conditionally inside the trip-expenses screen rather than inside a native `Modal`: `Travel App/app/trip-expenses/index.tsx:321`. The sheet itself uses an absolutely filled `KeyboardAvoidingView` overlay and a backdrop `Pressable` that immediately calls `onClose`: `Travel App/components/expense/AddExpenseSheet.tsx:355`, `Travel App/components/expense/AddExpenseSheet.tsx:359`, `Travel App/components/expense/AddExpenseSheet.tsx:360`. The form is long and stateful, with receipt scan, title, amount, currency, payer, itinerary link, category, split type, members, custom split inputs, and submit all in one scroll view: `Travel App/components/expense/AddExpenseSheet.tsx:361`, `Travel App/components/expense/AddExpenseSheet.tsx:411`, `Travel App/components/expense/AddExpenseSheet.tsx:425`, `Travel App/components/expense/AddExpenseSheet.tsx:458`, `Travel App/components/expense/AddExpenseSheet.tsx:483`, `Travel App/components/expense/AddExpenseSheet.tsx:537`, `Travel App/components/expense/AddExpenseSheet.tsx:567`, `Travel App/components/expense/AddExpenseSheet.tsx:586`, `Travel App/components/expense/AddExpenseSheet.tsx:616`.

Why this feels less iOS-native: iOS sheets/modals give users a predictable presentation boundary, modal accessibility isolation, and familiar dismissal behavior. For a multi-minute form, accidental backdrop dismissal without a dirty-state confirmation feels fragile during dogfood, especially after scanning a receipt or entering custom splits.

### P2 - Trip workspace pills look like a segmented control but behave like navigation stack pushes

The trip workspace hides native headers and renders a custom sticky `TripHeader` above a nested `Stack`: `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:75`, `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:77`, `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:79`. The pill control is visually implemented as an iOS-style segmented control with a sliding thumb: `Travel App/components/ui/NavPills.tsx:49`, `Travel App/components/ui/NavPills.tsx:76`, `Travel App/components/ui/NavPills.tsx:81`, `Travel App/components/ui/NavPills.tsx:89`. But selecting a pill pushes a route onto the stack: `Travel App/components/trip/TripHeader.tsx:81`, `Travel App/components/trip/TripHeader.tsx:87`, `Travel App/components/trip/TripHeader.tsx:92`, `Travel App/components/trip/TripHeader.tsx:94`, while the child stack disables transition animation: `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:80`.

Why this feels less iOS-native: segmented controls usually switch views in place; tab bars switch peer sections; push navigation creates a new destination with back affordance. This hybrid can make back behavior feel surprising: after tapping Plan, Map, Photos, and Chat, the back button may traverse internal mode history rather than return to the trip list. That may be intentional for Vesper, but the visual control currently communicates "mode switch," not "navigation history."

### P2 - Custom sheet close placement does not consistently follow iOS sheet toolbar conventions

Several sheets use `presentationStyle="pageSheet"` or `formSheet`, which is the right family of presentation, but close controls are custom `X` buttons rather than a leading Cancel/Done toolbar pattern. `ProposalReviewSheet` presents as a page sheet and puts an `X` on the trailing side: `Travel App/components/trip/ProposalReviewSheet.tsx:286`, `Travel App/components/trip/ProposalReviewSheet.tsx:288`, `Travel App/components/trip/ProposalReviewSheet.tsx:292`. `ExperienceDetailSheet` presents as a page sheet and floats a close `X` over the hero image: `Travel App/components/discover/ExperienceDetailSheet.tsx:217`, `Travel App/components/discover/ExperienceDetailSheet.tsx:220`, `Travel App/components/discover/ExperienceDetailSheet.tsx:232`, `Travel App/components/discover/ExperienceDetailSheet.tsx:250`.

Why this matters: Apple's sheet guidance calls out familiar toolbar placement for single-view sheets. Vesper can intentionally use editorial hero close chrome in media/detail sheets, but operational sheets like proposal review should probably follow the native Cancel/Done mental model more closely.

### P2 - Touch-target enforcement exists, but custom header/action buttons still bypass it

The app has a good `IconButton` primitive that guarantees a 44x44 target: `Travel App/components/ui/IconButton.tsx:1`, `Travel App/components/ui/IconButton.tsx:84`. `TripHeader` uses it for its back and settings icons: `Travel App/components/trip/TripHeader.tsx:101`, `Travel App/components/trip/TripHeader.tsx:124`. However, `Tap` defaults to no minimum target: `Travel App/components/ui/Tap.tsx:33`, `Travel App/components/ui/Tap.tsx:39`, `Travel App/components/ui/Tap.tsx:53`. `ScreenHeader` action icons use only `padding: spacing.md` around a 22pt icon, about 38pt before hit slop: `Travel App/components/ui/ScreenHeader.tsx:95`, `Travel App/components/ui/ScreenHeader.tsx:97`, `Travel App/components/ui/ScreenHeader.tsx:103`, `Travel App/components/ui/ScreenHeader.tsx:130`. The private chat mic button similarly wraps a 20pt icon with 8pt padding, about 36pt: `Travel App/app/(tabs)/concierge/chat.tsx:754`, `Travel App/app/(tabs)/concierge/chat.tsx:756`, `Travel App/app/(tabs)/concierge/chat.tsx:761`, `Travel App/app/(tabs)/concierge/chat.tsx:995`.

Why this matters: Apple accessibility guidance recommends comfortable, accessible controls and the design docs explicitly set a 44pt floor. The app already has the primitive; the polish gap is inconsistent adoption.

### P2 - Several picker-like choices are rendered as horizontal chips where native menus/pickers would be more predictable

`AddExpenseSheet` renders currency as a horizontal scroll of radio chips: `Travel App/components/expense/AddExpenseSheet.tsx:425`, `Travel App/components/expense/AddExpenseSheet.tsx:427`, `Travel App/components/expense/AddExpenseSheet.tsx:430`. It also renders payer selection as horizontal chips: `Travel App/components/expense/AddExpenseSheet.tsx:458`, `Travel App/components/expense/AddExpenseSheet.tsx:460`, `Travel App/components/expense/AddExpenseSheet.tsx:467`. Category and split type are wrap-chip groups: `Travel App/components/expense/AddExpenseSheet.tsx:537`, `Travel App/components/expense/AddExpenseSheet.tsx:541`, `Travel App/components/expense/AddExpenseSheet.tsx:567`, `Travel App/components/expense/AddExpenseSheet.tsx:569`.

Why this feels less iOS-native: chips are fine for quick, visible preference signals, but currency, payer, and split mode behave more like structured inputs. On iOS, menus, pickers, or focused selection sheets can reduce horizontal-scroll friction and make VoiceOver ordering clearer. Vesper should keep chip-like reaction UI where it is doctrine-aligned; expense bookkeeping should lean more native and utilitarian.

### P3 - Root and tab navigation are broadly native-compatible, with a few areas to verify at runtime

Positive evidence: root Stack uses native modal presentation for venue, guide, invite, onboarding, and DNA flows: `Travel App/app/_layout.tsx:197`, `Travel App/app/_layout.tsx:203`, `Travel App/app/_layout.tsx:207`, `Travel App/app/_layout.tsx:215`, `Travel App/app/_layout.tsx:234`, `Travel App/app/_layout.tsx:238`. The bottom tab bar has four stable top-level tabs with standard icons and labels: `Travel App/app/(tabs)/_layout.tsx:52`, `Travel App/app/(tabs)/_layout.tsx:68`, `Travel App/app/(tabs)/_layout.tsx:79`, `Travel App/app/(tabs)/_layout.tsx:91`, `Travel App/app/(tabs)/_layout.tsx:102`. Chat screens use `KeyboardAvoidingView`, interactive keyboard dismissal, and handled taps: `Travel App/app/(tabs)/concierge/chat.tsx:708`, `Travel App/app/(tabs)/concierge/chat.tsx:862`, `Travel App/app/(tabs)/concierge/chat.tsx:863`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:267`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:309`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:310`.

Runtime verification still matters because keyboard offsets are hand-derived from header chrome: `Travel App/app/(tabs)/concierge/chat.tsx:717`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:275`, and the composer adds bottom safe-area padding internally: `Travel App/components/chat/ComposerBar.tsx:245`, `Travel App/components/chat/ComposerBar.tsx:264`. This is reasonable code, but it needs device screenshots on notched iPhones, SE-class devices, and landscape.

## Evidence

- Runtime inspection unavailable: no booted simulator was listed by `xcrun simctl list devices booted`.
- Strong native-aligned patterns already present:
  - Four-item bottom tab bar: `Travel App/app/(tabs)/_layout.tsx:68`, `Travel App/app/(tabs)/_layout.tsx:79`, `Travel App/app/(tabs)/_layout.tsx:91`, `Travel App/app/(tabs)/_layout.tsx:102`.
  - Root modal presentations for overlay/detail flows: `Travel App/app/_layout.tsx:203`, `Travel App/app/_layout.tsx:207`, `Travel App/app/_layout.tsx:215`, `Travel App/app/_layout.tsx:234`.
  - Safe-area-aware custom headers: `Travel App/components/ui/ScreenHeader.tsx:44`, `Travel App/components/ui/ScreenHeader.tsx:50`, `Travel App/components/trip/TripHeader.tsx:57`, `Travel App/components/trip/TripHeader.tsx:99`.
  - Chat keyboard avoidance and interactive dismiss: `Travel App/app/(tabs)/concierge/chat.tsx:708`, `Travel App/app/(tabs)/concierge/chat.tsx:862`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:267`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:309`.
  - Native destructive confirmations are generally used for high-stakes deletes/sign-out: `Travel App/app/(tabs)/me/account.tsx:155`, `Travel App/app/(tabs)/me/account.tsx:230`, `Travel App/components/expense/ExpenseDetail.tsx:101`, `Travel App/app/trip-info/index.tsx:207`.

## Suggested Fix Direction

- Promote expense add/edit to real `Modal` page sheets or a shared bottom-sheet primitive with native presentation, accessibility isolation, dirty-state confirmation, and keyboard-tested detents.
- Decide whether trip workspace pills are segmented-control state or sub-route navigation. If state, use replace/in-place switching and make back leave the workspace. If navigation, style them less like a segmented control and preserve native transition semantics.
- Standardize sheet headers: operational sheets use leading Cancel/Done or a clear toolbar; editorial detail sheets may keep immersive hero close controls if verified.
- Make `IconButton` the only bare icon path. Change `ScreenHeader` actions and chat header mic to `IconButton`, or make `Tap minTarget="auto"` the default for icon-like controls.
- Use native-ish menus/pickers for structured bookkeeping choices such as currency and payer. Keep chips for reaction cards, quick preference signals, and Vesper-specific conversational affordances.
- Preserve intentional Vesper breaks: private Vesper prose can be editorial instead of standard chat bubbles; warm parchment chrome can replace default white system surfaces; purple agent presence is a brand convention. Follow iOS closely for navigation, dismissal, keyboard, destructive actions, safe areas, and accessibility.

## Verification Ideas

- Run iOS screenshots on iPhone SE, iPhone 16/17 class notched device, and landscape for private chat, group chat, trip workspace, proposal sheet, experience sheet, and add expense.
- In chat, focus the composer with suggestions and image previews visible; verify the composer hugs the keyboard without double bottom inset or tab-bar collision.
- On trip workspace, tap Plan -> Map -> Photos -> Chat, then use the visual back button and the iOS edge-swipe gesture. Confirm whether the observed behavior matches the intended mental model.
- Open Add Expense, enter data, scan or attach a receipt, then tap outside the sheet. Verify whether data is lost and whether VoiceOver focus remains inside the sheet.
- Enable larger accessibility text sizes and inspect `ScreenHeader` actions, chat mic, proposal close, composer send/stop, and expense chips for 44pt target compliance and text clipping.
