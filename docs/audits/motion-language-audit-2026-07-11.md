---
doc_type: working
status: active
owner: frontend / design
created: 2026-07-11
expires: 2026-08-10
why_new: Preserve the point-in-time Phase 0 evidence and migration classification without making implementation debt part of the durable motion doctrine.
promotes_to: docs/systems/motion-language.md
supersedes: []
---

# Motion Language Phase 0 Audit — 2026-07-11

## Outcome

The app does not lack motion foundations. It has a coherent but incompletely
governed foundation: centralized durations/easings, shared Reanimated presets,
press feedback, card lift, deck motion, and Reduced Motion support. The main debt
is distribution and ownership: at least 52 files participate in motion-related
behavior, native modal defaults coexist with shared presentation primitives, and
Atlas plus a few expressive components carry local timing dialects.

The durable product decision has been promoted to
[`docs/systems/motion-language.md`](../systems/motion-language.md). This document
is evidence and migration input, not ongoing canon.

## Sources inspected

- Current Vesper design export: `/Users/feihuyan/Downloads/vesper 146/project/`
  (active canon only; `archive/` was excluded from decision authority).
- Frontend motion tokens and helpers: `travel-app/constants/motion.ts`,
  `travel-app/utils/motion.ts`, `travel-app/hooks/useAnimatedLoop.ts`.
- Shared interaction surfaces under `travel-app/components/ui/` and
  `travel-app/components/focus-home/`.
- Motion-bearing application and component files found with static searches for
  Reanimated, React Native `Animated`, `LayoutAnimation`, navigation animation,
  and native `Modal` presentation behavior.
- Existing animation QA: `travel-app/scripts/polish-qa/run-animation-qa.mjs`.

## Design evidence from Vesper 146

| Evidence | Durable implication |
|---|---|
| Home hero uses `0.32s` house-ease fade/rise; rail uses `0.26s`; rise is `7px` | Soft Reveal has base, emphasized, and promoted levels with small displacement |
| Cards press to `0.97` over roughly `0.15s` | Substantial targets share restrained immediate press acknowledgment |
| Search specifies bottom/field rise or fade and no full-screen scrim | Full-screen workspace transition differs from a focused overlay |
| DecisionSheet is opened by cards needing deliberation | Sheets represent bounded editing/decision work |
| Card ownership canon assigns stack/deck motion to the card shell and orchestration to Home | Mechanics and product invocation have separate owners |
| Itinerary routes empty, booked, live, past, proposed, conflict, route, and reservation states to different destinations | Presentation follows intent/state rather than one universal modal |
| Trip canon says the eye lands on “Now” with no animation needed | Stable emphasis is preferable to ambient attention motion |
| State system omits progress when work is effectively instant | Animation must represent real work, not fabricate waiting |
| Atlas says the surface fills in and does not flip from empty to rich | State Settle and spatial continuity govern accumulating surfaces |

The export does **not** specify a canonical shared-element/card-to-detail morph or
exact deck-advance choreography. Those remain implementation opportunities, not
design authority. Static design-canvas tool chrome and archived experiments were
not treated as product motion.

## Current implementation inventory

### A. Canonical foundations — retain and consolidate

| Area | Files | Finding |
|---|---|---|
| Tokens | `constants/motion.ts` | Strong base: 120/150/200/240/260/320ms, house ease, loop timings, press spring, `0.97` scale |
| Declarative presets | `utils/motion.ts` | Strong base: list enter/exit/layout, card enter, soft enter/exit, cached Reduced Motion policy |
| Press | `components/ui/Tap.tsx` | Canonical press implementation; should become the underlying mechanic for shared actionable controls |
| Sheet | `components/ui/BottomSheet.tsx` | Canonical sheet foundation including backdrop, gesture dismissal, and Reduced Motion handling |
| Focus overlay | `components/ui/CardLift.tsx` | Matches the design language: scrim plus `32px` lift over `240ms`, faster dismissal |
| Deck | `components/focus-home/Deck.tsx` | Matches the same spatial family: scrim plus `40px` lift, no native modal animation |
| State/layout | chat, notifications, trip plan/story/proposal files using `maybeDisable(listItem*)` | Correct shared vocabulary; retain while centralizing invocation rules |
| Selection | `components/ui/SegmentedIndicator.tsx` | Uses shared timing and explicit Reduced Motion behavior |
| Receipt | `components/receipts/VesperReceipt.tsx` | Uses canonical base timing/ease; classify as Soft Reveal/State Settle |

### B. Intentional special behavior — retain but formally bound

| Area | Files | Disposition |
|---|---|---|
| Consequential completion | `components/ui/DecisionSeal.tsx` | Keep as Completion Seal only; expressive local choreography is an approved exception, not reusable default motion |
| Atlas composition | `components/atlas/AtlasTasteBoard.tsx` | Preserve composition-specific spatial semantics; migrate common fades/layout to shared patterns and document the dive exception |
| Atlas reel | `components/atlas/AtlasBoardReel.tsx`, `AtlasMemoryReel.tsx` | Preserve authored reel/crossfade behavior; require manual/static Reduced Motion and stop auto-advance there |
| Live state | `components/vesper-cards/faces/CardLive.tsx`, `components/places/SpotTake.tsx` | Pulse/caret allowed only while the state is genuinely live or streaming |
| Voice | `components/voice/VoiceOrb.tsx`, `VoiceOverlay.tsx` | Built-dark/non-MVP; retain as bounded future exception, do not let its spring/loop define general language |
| Plan attention | `components/trip-plan/HighlightPulse.tsx` | Short, event-triggered orientation aid; never a persistent “Now” pulse |

### C. Vocabulary drift — normalize during Phases 2–6

| Finding | Sites | Required migration |
|---|---|---|
| Raw `160ms`/`120ms` fades | `components/chat/ScrollBottomFab.tsx` | Use `softEnter`/`softExit` and Reduced Motion helper |
| Raw `220ms` image fade | `components/atlas/RisoSlotImage.tsx` | Map to the nearest semantic token rather than retaining a local step |
| Local Atlas fade pairs (`80/160ms`) | `components/atlas/AtlasMemoryReel.tsx` | Treat as documented reel exception or map to instant/fast after device review |
| Local Atlas dive (`220ms`, local ease) | `components/atlas/AtlasTasteBoard.tsx` | Document composition exception or express through a semantic preset |
| Bespoke Home entrance | `components/focus-home/FocusHome.tsx` | Replace with Soft Reveal semantic primitive |
| Bespoke chat banners/nudges | `components/chat/ErrorBanner.tsx`, `OrganizerInviteNudge.tsx` | Replace with shared state/reveal primitive and common interruption behavior |
| Platform `LayoutAnimation` default | `components/places/SpotFacts.tsx` | Replace with State Settle so timing, easing, and Reduced Motion are governed |
| Navigation literal fades | `app/_layout.tsx` Atlas board/reel routes | Keep only as Workspace Transition semantics; centralize route preset if repeated |

### D. Presentation bypasses — adjudicate and migrate

The shared sheet/lift primitives coexist with feature-owned native modals. Some are
legitimate full-screen or page-sheet destinations; others are structural bypasses
until explicitly classified.

| Presentation class | Current sites | Classification |
|---|---|---|
| Shared governed | `BottomSheet`, `CardLift`, `Deck`, `ConfirmDialog`, `PermissionRationale`, `TextInputModal` | Retain; align mechanics and decision matrix |
| Sanctioned full-screen/page-sheet | `PhotoIntakeSheets` lightbox, `ProposalDetailScreen`, `FindPhotosSheet` | Retain as Workspace Transition only if origin/dismissal and Reduced Motion pass device review |
| Feature-owned overlay needing migration review | Atlas artifact/board menus, `AtlasTimelineEntryMenu`, `GroupAgencySheet`, Discover `ExperienceDetailSheet`, costs/accommodation overlays | Decide popover vs Deliberation Sheet vs Card Lift; route through the winning shared primitive |
| Dev-only | `components/dev/DevFab.tsx` | Excluded from product canon; no migration priority |
| Built-dark voice | `MicPrivacyDisclosure`, `VoiceOverlay` | Defer with voice surface; must comply before activation |

### E. Reduced Motion coverage

Reduced Motion is explicitly considered in the shared presets and approximately
three dozen application/component files, which is a meaningful foundation. Gaps:

- Native `Modal` animation types do not consistently derive from the preference.
- `RisoSlotImage`, `ScrollBottomFab`, and some feature-owned modal fades bypass the
  shared helper.
- `AtlasTasteBoard` has at least one layout animation without the nearby reduced
  guard.
- The module-level asynchronous cache in `utils/motion.ts` can allow an early
  first animation before the preference resolves.
- QA currently depends on manually enabling iOS Reduce Motion.

These are migration requirements, not reasons to discard the existing approach.

### F. QA and enforcement

Existing strengths:

- `qa:polish:animation` records a deterministic animation beat and generates a
  contact sheet plus verdict.
- The verdict explicitly checks entrance, hold, dismissal, tap-to-dismiss, and a
  Reduced Motion pass.
- The repo already enforces visual-system budgets for colors, radii, spinners,
  sheets, and local buttons, providing a natural model for a motion budget.

Current gap: the animation registry is centered on the Decision Seal rather than
covering the eight canonical patterns, and no static check prevents raw duration,
curve, spring, modal, or loop invention.

## Surface interaction map

| Surface | Core interactions | Canonical patterns | Highest-risk drift |
|---|---|---|---|
| Vesper | composer/send, messages arriving, result cards, deck, errors/progress | Press, Soft Reveal, State Settle, Card Lift, Deck Focus | keyboard occlusion; cards occupying composer chrome; streamed layout jitter; competing overlays |
| Trips | hero, itinerary blocks, proposals, booking, live/past states | Press, Deliberation Sheet, Workspace Transition, State Settle, Completion Seal | one modal treatment for different intents; animating “Now”; optimistic success ceremony |
| Discover | search, filters, map/list, detail, save | Press, Workspace Transition, Deliberation Sheet/Card Lift, State Settle | over-animating map/results; detail sheet bypass; save item teleporting |
| Atlas | first save, board/reel, scan, keep/render, readings accretion | Soft Reveal, State Settle, Workspace Transition plus bounded reel/composition exceptions | bespoke timings/eases; auto-advance under Reduced Motion; surface flipping instead of filling |
| Shared chrome | buttons, rows, tabs, toggles, headers, dialogs | Press, State Settle, Workspace Transition | controls bypassing `Tap`; local modal defaults; animation replay on focus |

## Ratification decisions

Phase 1 ratified eight patterns: Press, Soft Reveal, Card Lift, Deliberation
Sheet, Workspace Transition, State Settle, Deck Focus, and Completion Seal.

It also ratified these boundaries:

1. Popovers answer quick contextual questions; sheets host bounded deliberation;
   lifts focus one object; decks triage collections; screens are workspaces.
2. No unsolicited hero or generic card may occupy the space immediately above the
   chat composer.
3. Progress animation represents real ongoing work and is omitted for effectively
   instant work.
4. “Now” remains visually stable.
5. Expressive completion animation occurs only after consequential success.
6. Existing Atlas/reel and live-state behavior may remain only as named, bounded
   exceptions with Reduced Motion behavior.

## Migration priority

1. Consolidate semantic tokens and Reduced Motion resolution.
2. Make shared actionable controls inherit Press.
3. Consolidate sheet, lift, deck, and workspace ownership.
4. Fix Vesper composer/card/keyboard boundaries.
5. Normalize State Settle and progress behavior.
6. Migrate Trips, Discover, then Atlas exceptions.
7. Expand animation QA and add static budgets.
8. Remove superseded helpers, local timing dialects, and modal bypasses.

## Exit

Phase 0 evidence is complete and Phase 1 has been promoted into the durable motion
doctrine. Archive this audit after the migration ledger has absorbed all remaining
items or by its expiry date; do not update it into a second current-state registry.
