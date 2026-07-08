# Code Alignment — Batch B: Concierge Deck & Home (2026-07-05)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only). Same standing rules as Batch A (git status first, snap rule, commit-per-task, tests green, no push).

## Task B1 — Three missing structured deck faces: Flight, Proposal, Comparison
Canon: `vesper-home-deck.jsx` → `DeckFlight` (~88), `DeckProposal` (~132), `DeckCompare` (~151) — dark full-screen deck cards. Code: `components/focus-home/DeckStructuredFace.tsx` + `hooks/useConciergeHomeState.ts` render structured faces only for vote/settle/readiness (+pick/call/brief); Flight/Proposal/Comparison cards fall back to prose today. Build the three faces per canon layout (snap values to tokens). Wire the card-kind → face mapping so backend cards of those kinds get structured rendering. The deck is officially 12 faces per the taxonomy board (`deck-readiness-taxonomy.jsx`) — after this task, all 12 render structured.

## Task B2 — Verify the readiness face against its new canon artboard
`readiness` shipped before it had canon; session 6 drew it (`deck-readiness-taxonomy.jsx` → `DeckReadiness`). Diff code's readiness face against the artboard; align divergences (snap rule). Likely small.

## Task B3 — Home-state mapping conformance (Single-item + Calm)
Canon: the taxonomy mapping board (`deck-readiness-taxonomy.jsx` → `TaxonomyMappingBoard`) rules which canon board governs each code `FocusState` kind, and keeps **Single-item** (rail collapses when only one card exists) and **Calm** (queue-empty vibe read) as build intent. Code: `components/focus-home/` has no rail-collapse branch and no explicit calm treatment. Build: (a) single-item state — rail collapses per the canon board (`vesper-home-states-dyn.jsx`); (b) verify code's `starter`/`prepared` states visually match the Calm board's read — align if not. **Juggling was trimmed to a post-dogfood note — do NOT build it.**

## Task B4 — Whisper dead-code removal
Quiet mode was adjudicated KILL (canon archived it; code already removed the UI). Remove the dead `whisper` member from the VoiceRegister union (`components/focus-home/types.ts` ~28-33) and any dead branches/styles referencing it. The canonical register list is now 5.

## Done
Four commits · all 12 deck faces render structured · readiness matches canon · single-item rail collapse works · whisper gone from the type union · report token mismatches.
