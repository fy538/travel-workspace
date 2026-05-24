# Modal, Sheet, And Keyboard Polish Findings

## Summary

Runtime inspection was unavailable: `xcrun simctl list devices booted` showed no booted iOS devices, and no Expo/Metro process for Travel App was running. This is therefore a static sheet/keyboard-risk audit from code.

Overall, chat keyboard handling looks intentionally maintained, but sheet behavior is fragmented. The app mixes native `pageSheet` modals, custom absolute overlays, and transparent bottom sheets with different heights, handles, close affordances, safe-area handling, and validation behavior. No P0 issues found. The dogfood-first polish target should be `AddExpenseSheet`, because it combines the most text entry, keyboard pressure, inline expansion, validation ambiguity, receipt permission flow, and a non-native overlay implementation.

Apple HIG comparison anchors: [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Modality](https://developer.apple.com/design/human-interface-guidelines/modality), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), and [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).

## Overlays Reviewed

- `Travel App/components/trip/ProposalReviewSheet.tsx`
- `Travel App/components/expense/AddExpenseSheet.tsx`
- `Travel App/components/memory/ShareStorySheet.tsx`
- `Travel App/components/trip/FindPhotosSheet.tsx`
- `Travel App/components/discover/ExperienceDetailSheet.tsx`
- `Travel App/components/chat/ComposerBar.tsx`
- `Travel App/app/(tabs)/concierge/chat.tsx`
- `Travel App/app/(tabs)/trips/[tripId]/chat.tsx`
- `Travel App/app/trip-expenses/index.tsx`
- `Travel App/app/_layout.tsx`
- `Travel App/app/venue/[venueId]/index.tsx`
- `Travel App/app/venue/[venueId]/angles.tsx`

## Findings

### P1 - Add expense is a custom overlay, not a native modal, and is the riskiest keyboard/form surface

`AddExpenseSheet` renders as an absolutely positioned `KeyboardAvoidingView` with a backdrop and `zIndex: 100`, not a React Native `Modal` (`Travel App/components/expense/AddExpenseSheet.tsx:355`, `Travel App/components/expense/AddExpenseSheet.tsx:359`, `Travel App/components/expense/AddExpenseSheet.tsx:692`). It is conditionally mounted inside the expenses screen (`Travel App/app/trip-expenses/index.tsx:321`), while the expenses route itself is registered as a normal screen, not a modal (`Travel App/app/_layout.tsx:243`).

This increases dogfood risk versus native sheet behavior: parent content may remain part of the same accessibility tree, dismissal/back behavior depends on the screen tree, and the overlay needs to own every safe-area/keyboard edge case itself. It does use bottom inset padding (`Travel App/components/expense/AddExpenseSheet.tsx:360`) and a 90% max height (`Travel App/components/expense/AddExpenseSheet.tsx:701`), but it does not get the platform's built-in modal containment.

### P1 - Add expense validation is mostly disabled-button driven, so invalid forms can feel stuck

The form computes `canSubmit` from title, amount, category, selected members, custom shares, and busy state (`Travel App/components/expense/AddExpenseSheet.tsx:335`). The submit button is disabled whenever `canSubmit` is false (`Travel App/components/expense/AddExpenseSheet.tsx:674`). That means the specific toast validation in `handleSubmit` (`Travel App/components/expense/AddExpenseSheet.tsx:238`, `Travel App/components/expense/AddExpenseSheet.tsx:243`, `Travel App/components/expense/AddExpenseSheet.tsx:247`, `Travel App/components/expense/AddExpenseSheet.tsx:252`) is unreachable for many invalid states.

This is especially brittle for the percentage/exact split modes, where per-person inputs appear far below the primary amount field (`Travel App/components/expense/AddExpenseSheet.tsx:617`) and the only visible percentage constraint is a caption (`Travel App/components/expense/AddExpenseSheet.tsx:663`). For dogfood, a disabled button at the bottom of a long, keyboard-covered form is likely to feel broken even when the logic is correct.

### P1 - Revert change applies immediately without a confirmation step

`ProposalReviewSheet` exposes organizer revert as a secondary button that directly calls `onRevert` (`Travel App/components/trip/ProposalReviewSheet.tsx:777`, `Travel App/components/trip/ProposalReviewSheet.tsx:779`, `Travel App/components/trip/ProposalReviewSheet.tsx:785`). The mutation immediately calls `api.revertProposal` and closes on success (`Travel App/components/trip/ProposalReviewSheet.tsx:237`, `Travel App/components/trip/ProposalReviewSheet.tsx:242`).

This is not P0 because it is not a common text-entry blocker, and copy says it only undoes this proposal. But Apple guidance expects destructive or data-changing actions to be visually distinguished and confirmed when they can surprise people. The nested force-revert flow does use a danger button plus explanatory warning (`Travel App/components/trip-plan/RevertConflictSheet.tsx:83`, `Travel App/components/trip-plan/RevertConflictSheet.tsx:92`), so the immediate revert path is the inconsistent one.

### P2 - Sheet presentation is inconsistent across core flows

The reviewed overlays use several different patterns:

- `ProposalReviewSheet`: native `Modal` with `presentationStyle="pageSheet"`, no grab handle, close X (`Travel App/components/trip/ProposalReviewSheet.tsx:286`, `Travel App/components/trip/ProposalReviewSheet.tsx:288`, `Travel App/components/trip/ProposalReviewSheet.tsx:292`).
- `FindPhotosSheet`: native `pageSheet`, full-screen grid, close X, no grab handle (`Travel App/components/trip/FindPhotosSheet.tsx:306`, `Travel App/components/trip/FindPhotosSheet.tsx:323`).
- `ExperienceDetailSheet`: native `pageSheet`, styled as a full-height sheet (`Travel App/components/discover/ExperienceDetailSheet.tsx:217`, `Travel App/components/discover/ExperienceDetailSheet.tsx:223`, `Travel App/components/discover/ExperienceDetailSheet.tsx:479`), with a handle only in the gradient fallback hero (`Travel App/components/discover/ExperienceDetailSheet.tsx:243`, `Travel App/components/discover/ExperienceDetailSheet.tsx:249`), not when a photo hero exists (`Travel App/components/discover/ExperienceDetailSheet.tsx:225`).
- `ShareStorySheet`: custom transparent bottom sheet with 88% max height, handle, Done button, and backdrop (`Travel App/components/memory/ShareStorySheet.tsx:235`, `Travel App/components/memory/ShareStorySheet.tsx:243`, `Travel App/components/memory/ShareStorySheet.tsx:245`, `Travel App/components/memory/ShareStorySheet.tsx:530`).
- `AddExpenseSheet`: custom non-Modal bottom overlay with 90% max height and handle (`Travel App/components/expense/AddExpenseSheet.tsx:355`, `Travel App/components/expense/AddExpenseSheet.tsx:360`, `Travel App/components/expense/AddExpenseSheet.tsx:701`).

Individually these are defensible. Together, they make it hard for dogfood users to predict whether a surface is swipe-dismissable, backdrop-dismissable, full-screen, half-sheet, or modal-task. Apple HIG encourages modality to focus people on a distinct task; the current variety makes modality itself feel like an implementation detail.

### P2 - Nested sheets are possible in proposal conflict resolution

`ProposalReviewSheet` can open `RevertConflictSheet` while the proposal sheet remains mounted (`Travel App/components/trip/ProposalReviewSheet.tsx:443`). `RevertConflictSheet` is another native `Modal` using `presentationStyle="formSheet"` (`Travel App/components/trip-plan/RevertConflictSheet.tsx:42`). This creates modal-on-modal behavior for a high-stakes plan-change recovery flow.

Apple HIG advises displaying only one sheet at a time from the main interface. The nested flow is not automatically wrong, but it should be intentionally verified on iPhone and iPad because stacked modal dismissal can confuse users about which layer they are closing and whether the underlying proposal state changed.

### P2 - Share story lacks explicit bottom safe-area handling

`ShareStorySheet` uses a transparent modal and custom bottom sheet (`Travel App/components/memory/ShareStorySheet.tsx:235`, `Travel App/components/memory/ShareStorySheet.tsx:245`), but it does not read `useSafeAreaInsets`. Its sheet relies on fixed `paddingBottom: spacing.xxxxl` (`Travel App/components/memory/ShareStorySheet.tsx:530`). By contrast, `AddExpenseSheet`, `FindPhotosSheet`, and `ExperienceDetailSheet` all use safe-area insets for bottom padding (`Travel App/components/expense/AddExpenseSheet.tsx:86`, `Travel App/components/trip/FindPhotosSheet.tsx:51`, `Travel App/components/discover/ExperienceDetailSheet.tsx:103`).

This is likely only P2, but share settings include primary share/update actions and destructive revoke actions near the lower part of the sheet (`Travel App/components/memory/ShareStorySheet.tsx:478`, `Travel App/components/memory/ShareStorySheet.tsx:515`). It should be verified on home-indicator devices and small iPhones.

### Positive finding - Chat keyboard handling is comparatively strong

Private and group chat both wrap their screens in `KeyboardAvoidingView` with iOS padding and derived offsets (`Travel App/app/(tabs)/concierge/chat.tsx:708`, `Travel App/app/(tabs)/concierge/chat.tsx:717`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:267`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:275`). Both message lists use `keyboardDismissMode="interactive"` and `keyboardShouldPersistTaps="handled"` (`Travel App/app/(tabs)/concierge/chat.tsx:862`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:309`).

`ComposerBar` also accounts for bottom safe area (`Travel App/components/chat/ComposerBar.tsx:245`), keeps the text input at a 44pt minimum (`Travel App/components/chat/ComposerBar.tsx:495`, `Travel App/components/chat/ComposerBar.tsx:509`), allows a taller multiline composer before internal scrolling (`Travel App/components/chat/ComposerBar.tsx:503`), and keeps the composer interactive during streaming (`Travel App/app/(tabs)/concierge/chat.tsx:948`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:427`). This is the most native-feeling part of the audited set from static code.

## Evidence

- No booted iOS simulator was available, so no screenshot/video evidence was collected.
- The app has no shared sheet primitive in the reviewed files; each sheet owns its own modal, height, handle, inset, and close treatment.
- Text-entry-heavy `AddExpenseSheet` has the greatest combination of risk factors: custom overlay containment, many `TextInput`s, inline-expanding sections, receipt permission flow, disabled-button validation, and bottom-positioned submission.
- The strongest existing pattern is chat: KAV + safe-area + interactive keyboard dismissal + bottom composer inset are already in place.

## Suggested Fix Direction

1. Polish `AddExpenseSheet` first. Convert it to a native modal/sheet or a shared app sheet primitive, add inline validation/error affordances, and make invalid submit explain what needs attention.
2. Create a shared `AppSheet` taxonomy: `taskFullScreen`, `bottomForm`, `mediaPicker`, and `detailSheet`, with consistent handle, close, height, backdrop, insets, and accessibility containment.
3. Keep chat keyboard behavior as the reference implementation. Any form sheet with text inputs should get equivalent safe-area and keyboard persistence rules.
4. Add confirmation before immediate plan-changing revert actions, matching the stronger force-revert confirmation pattern.
5. Avoid modal-on-modal unless the second layer is a native alert/action sheet or an explicitly designed confirmation step.

## Verification Ideas

- On iPhone SE and a notched iPhone, open `AddExpenseSheet`, focus every field, switch split modes, type enough rows to reach the bottom, and verify the active input and submit button remain reachable.
- With keyboard open in `AddExpenseSheet`, tap chips, member avatars, receipt remove, and submit. Confirm taps are handled on first press.
- On iPhone and iPad, open `ProposalReviewSheet`, trigger partial revert conflict, then test swipe-down, close X, and force-revert flows.
- On a home-indicator device, open `ShareStorySheet` with an existing share and verify `Share link`, `New link`, and `Stop sharing` clear the home indicator and feel safely separated.
- In both private and group chat, focus the composer, attach an image, stream a long response, scroll up, and verify the keyboard/composer/list do not jump.
