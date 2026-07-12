---
doc_type: contract
status: active
owner: founder / design / frontend
created: 2026-07-11
last_verified: 2026-07-11
why_new: Establish one cross-cutting interaction-motion doctrine so each surface does not invent timing, spatial behavior, and presentation semantics independently.
supersedes: []
source_of_truth_for: [interaction-motion-language, motion-presentation-semantics, reduced-motion-contract]
---

# Motion Language — Cross-Cutting Doctrine

> Status: ratified 2026-07-11
> Applies to: Vesper, Trips, Discover, Atlas, and shared application chrome
> Consumed by: every interactive frontend surface and shared UI primitive
> Last updated: 2026-07-11

## Purpose

Vesper moves with **quiet physicality**: acknowledge the touch, preserve spatial
context, move with purpose, then settle. Motion explains hierarchy, continuity,
or a change in state. It is not decoration and must never delay useful work.

This is a companion doctrine, not a new product surface. It governs motion and
presentation choices across existing systems. Point-in-time implementation debt
lives in the [Phase 0 audit](../audits/motion-language-audit-2026-07-11.md), not
in this durable contract.

## Brand stance

1. **Touch is acknowledged immediately.** An actionable object responds before
   or while navigation begins; animation must not create perceived latency.
2. **Objects retain an origin.** A focused card, sheet, or workspace should make
   clear where it came from and where dismissal returns.
3. **Entrances are calm; exits are quick.** Content may arrive deliberately but
   should get out of the way promptly.
4. **State accumulates rather than flips.** Preserve object identity and position
   when saved, booked, applied, enriched, or completed.
5. **Nothing bounces by default.** Ordinary entrances and layout changes use
   timing and the house ease. Spring is reserved for direct press response.
6. **“Now” is stable.** Current, urgent, or anchoring information uses hierarchy
   and contrast, not ambient movement.
7. **Ceremony is scarce.** Expressive motion is reserved for consequential,
   successfully completed commitments.
8. **Reduced Motion preserves meaning.** Remove displacement, scaling, rotation,
   radiating effects, and nonessential loops; retain hierarchy and an immediate
   or short crossfade state change.

## Canonical vocabulary

### 1. Press

Immediate tactile acknowledgment for buttons, cards, rows, and other substantial
targets.

- Scale target: `0.97`.
- Response: the shared press spring; release settles to `1`.
- Optional light haptic only when it reinforces a real selection or commitment.
- Disabled or non-actionable objects do not perform an actionable press response.
- Reduced Motion: no scale; visual pressed state may change instantly.

### 2. Soft Reveal

Ordinary content entrance: fade plus a small rise, approximately `7px`.

- Ordinary content: `200ms`.
- Emphasized content: `260ms`.
- Promoted hero: `320ms`.
- House ease: `cubic-bezier(0.2, 0.7, 0.2, 1)`.
- Do not replay when an unchanged screen regains focus.
- Reduced Motion: immediate appearance or short opacity-only transition.

### 3. Card Lift

Focuses one object while preserving its surrounding context.

- The source card remains conceptually anchored.
- A scrim separates focus from context without making the origin disappear.
- The focused surface rises approximately `32–40px` over `240ms`.
- Dismissal is approximately `120–150ms` and returns to the source context.
- It is not a generic modal entrance and not permission to place arbitrary cards
  over another workspace.
- Reduced Motion: focused state appears without displacement.

### 4. Deliberation Sheet

Bottom-origin surface for editing, comparing, resolving, confirming, or making a
bounded choice.

- Entrance: `240–260ms`; dismissal: `120–150ms`.
- The underlying context remains legible when that context informs the decision.
- One active presentation layer at a time; do not nest sheets.
- Keyboard insets are part of the contract: the active field and primary action
  remain visible above the keyboard.
- Reduced Motion: present without travel or with opacity only.

### 5. Workspace Transition

Navigation into a genuinely separate, full-screen destination.

- Use the platform navigation relationship or a restrained fade/push in
  `200–260ms`.
- Full-screen search may rise from its field or the bottom, or fade in; it does
  not require a scrim.
- Do not simulate workspace navigation with a floating card.
- Reduced Motion: platform reduced-motion behavior or immediate replacement.

### 6. State Settle

The same object changes state without becoming a visually unrelated object.

- Crossfade and/or layout adjustment around `200ms`.
- Preserve position when possible; nearby content may settle around it.
- Optimistic state must reverse honestly on failure.
- Success appearance may not precede the underlying success boundary.
- Reduced Motion: immediate state replacement, preserving position.

### 7. Deck Focus

Triage a bounded collection of first-class cards.

- Darken the desk, retain evidence of the stack, and lift one active card.
- Advancing preserves the user's place and reveals the next card without
  theatrical swipe physics.
- Closing returns to the deck's invoking context.
- The deck is an explicitly invoked workspace, not a passive content injection.
- Reduced Motion: static focused-card replacement with persistent stack cues.

### 8. Completion Seal

A scarce ceremonial response after a consequential commitment has succeeded.

- Appropriate examples: booking confirmed, consequential proposal applied, trip
  finalized, or meaningful memory deliberately kept.
- Inappropriate examples: ordinary save, toggle, message send, navigation, or
  background refresh.
- It may be more expressive than the base vocabulary but must settle into the
  normal interface and remain dismissible.
- Reduced Motion: static seal and copy; no impact, rotation, overshoot, or ring.

## Presentation decision matrix

| User intent | Canonical presentation | Not this |
|---|---|---|
| Quick contextual information | Popover or anchored menu | Sheet or full-screen workspace |
| Edit, compare, resolve, or confirm | Deliberation Sheet | Unsolicited overlay card |
| Focus one object while keeping context | Card Lift | Generic modal fade |
| Triage a bounded collection | Deck Focus | Cards injected into chat or page chrome |
| Enter a separate destination | Workspace Transition | Floating card pretending to be a screen |
| Show the same object changing state | State Settle | Remove-and-reinsert screen flip |
| Confirm consequential completed work | Completion Seal | Routine success animation |

### Composer boundary

The chat composer is workspace chrome, not a card host. No hero, recommendation,
or generic card may appear immediately above it merely because data exists. A card
may occupy that region only inside an explicitly invoked Deck Focus or Card Lift
presentation whose source, dismissal, and focus state are clear. Keyboard opening
must keep the current input and latest relevant conversation content visible.

## Timing and easing contract

The frontend implementation source of truth is `travel-app/constants/motion.ts`.
Semantic use is:

| Intent | Token | Value |
|---|---|---:|
| Exit / dismiss | `duration.instant` | 120ms |
| Toggle / small flip / ambient fade | `duration.fast` | 150ms |
| Ordinary entrance / state / layout | `duration.base` | 200ms |
| Emphasized content / sheet content | `duration.slow` | 260ms |
| Card focus | `duration.cardLift` | 240ms |
| Hero promotion | `duration.promote` | 320ms |
| Small set stagger | `duration.stagger` | 40ms |

Entrances and layout use the house ease. Exits accelerate away. Loops use the
symmetric easing and are allowed only while they communicate real ongoing work or
live state. New raw durations, curves, and springs require an explicit canon
exception rather than local invention.

## Progress and ambient motion

- Work completing in under approximately `500ms` changes state directly.
- Longer work may use restrained worker progress tied to real ongoing work.
- Indeterminate shimmer, pulse, caret, or breathe loops stop when the work or live
  condition stops.
- Never animate a stable “Now” anchor merely to attract attention.
- Auto-advancing media must pause or become manual under Reduced Motion.

## Haptics

Haptics reinforce semantics, not every tap. A light selection response may
accompany a deliberate choice. Stronger feedback is reserved for consequential
success or warning and must occur at the true state boundary. Haptics do not
compensate for unclear visual state.

## Ownership and exceptions

- Shared primitives own mechanics: press, sheet, lift, deck, state transition,
  progress, and completion seal.
- Product surfaces own when a pattern is invoked and the content it presents.
- Navigation owns workspace transitions.
- A feature may not reproduce a shared primitive locally for visual convenience.
- Sanctioned exceptions document purpose, owner, Reduced Motion behavior, and why
  a canonical pattern is insufficient.

## Executable implementation

The current shared implementation is intentionally small:

- Semantic intents and the numeric scale: `travel-app/constants/motion.ts`.
- Declarative reveal/state presets: `travel-app/utils/motion.ts`.
- System preference boundary: `travel-app/hooks/useMotionPreference.ts`.
- Press: `travel-app/components/ui/Tap.tsx` and semantic
  `MotionPressable.tsx`.
- Soft Reveal and State Settle: `SoftReveal.tsx` and `StateTransition.tsx`.
- Progress threshold: `ProgressGate.tsx`, composed around the appropriate
  loading or worker-progress content.
- Deliberation Sheet, Card Lift, and Deck Focus: `BottomSheet.tsx`,
  `CardLift.tsx`, and `components/focus-home/Deck.tsx`.
- Workspace options: `travel-app/utils/navigationMotion.ts`.
- Completion ceremony: `DecisionSeal.tsx`.
- Local QA events: `useMotionInstrumentation.ts` and
  `motionInstrumentation.ts`. These are opt-in local observers and do not send
  interaction telemetry remotely.

Feature code chooses a pattern and invokes its shared implementation. It does not
import Reanimated merely to reproduce one of these mechanics.

## Enforcement

The app CI runs `npm run motion-governance`. The guard is intentionally a
reviewable ratchet rather than a universal animation ban:

- direct Reanimated ownership is an explicit file allowlist, so a new owner is
  a conscious design-system decision;
- ordinary imperative animation must import the canonical motion tokens and may
  not introduce a raw non-zero timing literal;
- bespoke sequences are a four-entry allowlist with an owner and defined
  Reduced Motion behavior; their human-readable rationale lives in
  [Motion Exceptions](motion-exceptions.md).

This protects the canon without preventing the few motions that genuinely need
bespoke choreography.

## Acceptance criteria

Every new or changed interaction must answer:

1. Which named pattern applies?
2. What object or workspace is the spatial origin?
3. What happens on interruption, rapid repeat, dismissal, and failure?
4. What is the Reduced Motion equivalent?
5. Does animation communicate real state without delaying action?

Device review covers normal and Reduced Motion modes, keyboard open/closed where
relevant, interrupted gestures, slower supported hardware, and offline/failure
states. Automated enforcement is migration work following this doctrine; until
then, review against this contract is required.
