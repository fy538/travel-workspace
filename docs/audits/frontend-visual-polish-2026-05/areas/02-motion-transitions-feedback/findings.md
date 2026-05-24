# Motion, Transitions, And Feedback Findings

## Summary

No P0 motion or feedback blockers found. The app already has good foundations: `Tap` gives immediate press opacity plus haptics, `useHaptic` defines a semantic vocabulary, chat streaming batches text deltas, and the composer exposes a stop action while Vesper is responding.

The main dogfood risk is inconsistency. A few important flows still feel either too silent after a meaningful action, too abrupt during surface changes, or too generic during loading. Runtime screenshots/video were unavailable: `CI=1 npx expo start --web --non-interactive` exited because web support is missing `react-native-web`, so this report is static/code-based.

## Interactions Reviewed

- Press feedback and haptics: `Travel App/components/ui/Tap.tsx`, `Travel App/components/ui/Button.tsx`, `Travel App/hooks/useHaptic.ts`
- Segmented navigation and route changes: `Travel App/components/ui/NavPills.tsx`, `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx`
- Chat composer, streaming, retry/error feedback: `Travel App/components/chat/ComposerBar.tsx`, `Travel App/components/chat/TypingIndicator.tsx`, `Travel App/hooks/useConciergeChat.ts`, `Travel App/app/(tabs)/concierge/chat.tsx`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx`
- Voice overlay and mic state: `Travel App/components/voice/*`
- Proposal and expense sheets: `Travel App/components/trip/ProposalReviewSheet.tsx`, `Travel App/components/expense/AddExpenseSheet.tsx`

## Findings

### P1 - Proposal voting is optimistic but too quiet on success/failure

`ProposalReviewSheet` optimistically updates votes, but `onError` only rolls the cache back and `onSuccess` only invalidates queries; there is no toast, haptic, or inline rollback explanation for the user. That makes a core group decision feel ambiguous under flaky dogfood networks. The pending state is also uneven: Approve gets `loading={votePending}`, while Neutral and Reject are only disabled, so the spinner appears on Approve even if the user tapped Reject.

Evidence: `Travel App/components/trip/ProposalReviewSheet.tsx:186`, `Travel App/components/trip/ProposalReviewSheet.tsx:212`, `Travel App/components/trip/ProposalReviewSheet.tsx:218`, `Travel App/components/trip/ProposalReviewSheet.tsx:729`, `Travel App/components/trip/ProposalReviewSheet.tsx:731`, `Travel App/components/trip/ProposalReviewSheet.tsx:733`

### P1 - Trip workspace tab changes animate the pill but teleport the content

`NavPills` has a 220ms sliding thumb for the trip segmented control, but the nested trip stack disables screen animation entirely with `animation: 'none'`. The result is likely a split signal: chrome says "smooth segmented control," while the body changes instantly. For Chat / Plan / Map / Memory, that can make the workspace feel unfinished rather than native and deliberate.

Evidence: `Travel App/components/ui/NavPills.tsx:66`, `Travel App/components/ui/NavPills.tsx:68`, `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:77`, `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:80`

### P1 - Add expense sheet is a custom instant overlay, unlike the native modal sheets

`AddExpenseSheet` is conditionally mounted from the expenses screen, but the sheet itself is a `KeyboardAvoidingView` with a `Pressable` backdrop and a `View` sheet; it is not wrapped in a `Modal`, has no enter/exit animation, no platform presentation style, and no drag/dismiss behavior. Proposal review uses `Modal animationType="slide" presentationStyle="pageSheet"`, so the app has two different sheet languages for important flows.

Evidence: `Travel App/app/trip-expenses/index.tsx:321`, `Travel App/components/expense/AddExpenseSheet.tsx:355`, `Travel App/components/expense/AddExpenseSheet.tsx:359`, `Travel App/components/expense/AddExpenseSheet.tsx:360`, `Travel App/components/trip/ProposalReviewSheet.tsx:286`

### P2 - Voice motion feels underspecified against Vesper's restrained doctrine

The voice sheet uses a spring (`Animated.spring`) even though the brand doctrine says no spring overshoots, and `VoiceOrb` pulses on a 2.4s loop regardless of session status. The doctrine calls for a slow ~4s presence pulse at rest and a faster, more visible active response. The current implementation is functional, but it does not yet encode the difference between presence, connecting, listening, and live voice.

Evidence: `Travel App/docs/Brand Identity.md:167`, `Travel App/docs/Brand Identity.md:173`, `Travel App/components/voice/VoiceOverlay.tsx:190`, `Travel App/components/voice/VoiceOverlay.tsx:191`, `Travel App/components/voice/VoiceOrb.tsx:16`, `Travel App/components/voice/VoiceOrb.tsx:19`, `Travel App/components/voice/VoiceOrb.tsx:31`

### P2 - Generic spinners remain in product-defining loading moments

The design doctrine says loading should avoid generic spinners and evoke anticipation. The repo has a warm `Skeleton` primitive, but key surfaces still use `ActivityIndicator`: proposal details, button loading, receipt scanning, chat "load earlier", and voice quick-send. Small button spinners are acceptable utility feedback, but proposal review and receipt OCR are product moments where Vesper can feel more specific.

Evidence: `Travel App/docs/Brand Identity.md:178`, `Travel App/docs/Design Language.md:324`, `Travel App/components/ui/Skeleton.tsx:1`, `Travel App/components/ui/Button.tsx:92`, `Travel App/components/trip/ProposalReviewSheet.tsx:302`, `Travel App/components/expense/AddExpenseSheet.tsx:375`, `Travel App/app/(tabs)/concierge/chat.tsx:873`, `Travel App/components/voice/VoiceOverlay.tsx:282`

### P2 - Reduce Motion and haptic opt-out are only partially covered

Reanimated list/card presets respect Reduce Motion through `maybeDisable`, which is good. RN `Animated` motion does not use that helper: `NavPills`, `TypingIndicator`, `ErrorBanner`, `VoiceOrb`, and `VoiceOverlay` continue animating. Haptics are also globally present through `Tap` by default, but there is no app-level haptic preference despite Apple guidance to make haptics optional.

Evidence: `Travel App/utils/motion.ts:36`, `Travel App/utils/motion.ts:76`, `Travel App/components/ui/Tap.tsx:52`, `Travel App/components/ui/NavPills.tsx:68`, `Travel App/components/chat/TypingIndicator.tsx:41`, `Travel App/components/chat/ErrorBanner.tsx:27`, `Travel App/components/voice/VoiceOrb.tsx:16`, `Travel App/components/voice/VoiceOverlay.tsx:190`

## Evidence

- Runtime inspection unavailable: Expo web exits because `react-native-web` is not installed. No simulator/device video or screenshots were captured in this pass.
- Vesper doctrine: motion should be restrained, page transitions subtle/native, loading states not spinners, and confirmations quiet (`Travel App/docs/Brand Identity.md:167`, `Travel App/docs/Brand Identity.md:177`, `Travel App/docs/Brand Identity.md:178`, `Travel App/docs/Brand Identity.md:179`).
- Apple guidance: [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) says haptics should be consistent, causal, complementary to visual feedback, not overused, and optional.
- Apple guidance: [Motion](https://developer.apple.com/design/human-interface-guidelines/motion) frames motion as a way to convey status and feedback, with custom motion adapting to accessibility settings.
- Material guidance: [Understanding motion](https://m2.material.io/design/motion/understanding-motion.html) describes motion as feedback that indicates action status and helps orient users through transitions.

## Suggested Fix Direction

Define a small motion spec before more implementation work continues:

- Proposal decision feedback: one pattern for optimistic vote, pending vote, rollback, and confirmed organizer resolution. Include success/error haptics and a quiet inline/toast message.
- Trip workspace transitions: keep the segmented thumb, but add a subtle body cross-fade or horizontal native-feeling transition that respects Reduce Motion.
- Sheet system: standardize bottom/page sheet entry, backdrop fade, close gesture, safe-area behavior, keyboard behavior, and haptic moments. Bring `AddExpenseSheet` onto that system first.
- Voice states: map `idle`, `fetching_token`, `connecting`, `live`, `closing`, and `error` to orb pulse speed/intensity and sheet copy. Avoid visible spring overshoot.
- Loading movement: reserve `ActivityIndicator` for tiny inline utility controls; use warm skeletons, reserved slots, or anticipation copy for proposal, OCR, and concierge-generated content.
- Accessibility controls: extend Reduce Motion handling to RN `Animated` primitives and add a user-visible haptics preference or at least a central flag in `useHaptic`.

## Verification Ideas

- Capture video on iPhone SE-size and large iPhone simulator for: opening a proposal, casting each vote, failing a vote in offline mode, switching Chat/Plan/Map/Memory, opening/closing Add Expense, receipt scan loading, starting/stopping voice, and a long concierge stream.
- Test with Reduce Motion enabled and confirm list/card, segmented control, typing dots, voice orb, error banners, and sheets all reduce to fade/no-motion alternatives.
- Test with haptics disabled once a setting exists; every flow should still have visual feedback.
- In mock mode, add deterministic slow/error states for proposal detail, vote rollback, receipt OCR, and chat stream so motion can be reviewed without real backend timing.
