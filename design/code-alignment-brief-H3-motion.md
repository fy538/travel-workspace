# Code Alignment — Batch H3: Motion Migration (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: Session-W Motion Stance (in the canon mirror). Tokens live in `constants/motion.ts` + `utils/motion.ts`. **E6 already did the heavy lift** — toast 200/150, Skeleton opacity-pulse, house-curve as default, Tap spring clamped (ζ≈0.73). This batch is the straggler sweep. Smallest of the three H batches; **lead with the two accessibility defects (H3-1) — those are user-facing, the rest is token hygiene.**

Standing rules: git status first · snap rule · one commit per task · typecheck+tests green · no push without approval.

## Task H3-1 — Reduce-motion accessibility guards (DEFECT — do first)
Two animations bypass the reduce-motion guard entirely (canon Motion Stance requires all motion honor `useReducedMotion`):
- `components/discover/DiscoverMapCanvas.tsx` — Mapbox cluster zoom `animationDuration: 300` with no guard. Wrap it so it's instant (duration 0 / no camera animation) under reduced motion.
- `components/voice/VoiceOverlay.tsx` — the `Animated.spring` slide-in has no guard. Gate it like the modern presets in `utils/motion.ts` do.

## Task H3-2 — VoiceOverlay underdamped spring
`components/voice/VoiceOverlay.tsx` uses `Animated.spring {tension: 65, friction: 11}` — underdamped, overshoots (canon: "never bounces"). Retune to a critically-damped config matching the house spring used in `Tap.tsx` (ζ≈0.73). Fold this into H3-1's VoiceOverlay commit if touching the same file.

## Task H3-3 — DecisionSeal hardcoded durations → tokens
`components/ui/DecisionSeal.tsx` hardcodes 9 numeric durations (100/120/140/200/220/360/420/460/560/620ms) — the single biggest cluster of stray literals. Map each to the nearest `motion` duration token; if a beat genuinely needs a bespoke value (DecisionSeal is one of the canon's 3 reserved bespoke motion moments — verify against the stance), keep it as a named `const` with a comment, not a bare literal.

## Task H3-4 — Remaining hardcoded loops/timings → tokens (batch together)
Small strays, one commit: `components/voice/VoiceOrb.tsx` (1200ms loop), `components/places/SpotTake.tsx` (520ms loop ×2), `components/chat/OrganizerInviteNudge.tsx` (200ms ×2), `components/chat/ErrorBanner.tsx` (200ms ×2). Point them at `loop.*` / `duration.*` tokens. Where no exact token exists, prefer the nearest rather than adding new tokens (keep the token set tight).

## Done
Both reduce-motion accessibility gaps closed · VoiceOverlay spring critically damped · DecisionSeal + the four loop/timing files reference tokens (or named bespoke consts with rationale) · no new tokens invented unless a real gap · report any beat that legitimately needs a bespoke value so it's recorded as sanctioned, not flagged again next audit.

## Explicitly NOT in scope (already done — do not touch)
Toast durations (E6: 200/150 ✓) · Skeleton opacity-pulse (E6 ✓) · house-curve default positioning (✓) · Tap.tsx spring (already ζ≈0.73 ✓). The ~26 `Animated.timing` calls the stale backlog flagged are mostly already token-backed (CardLift, Deck, CardStates, CardLive, FocusHome) — only the H3-3/H3-4 files are real strays; do not "migrate" the compliant ones.
