---
doc_type: contract
status: active
owner: frontend / design
created: 2026-07-12
last_verified: 2026-07-12
why_new: Record the deliberately bespoke motion that is allowed outside the shared semantic primitives.
supersedes: []
source_of_truth_for: [motion-exceptions]
---

# Motion Exceptions

This is the short allowlist for choreography that cannot be expressed by the
shared Press, Soft Reveal, State Settle, Sheet, Lift, Deck, or Workspace
primitives. Every entry must name its purpose, owner, and Reduced Motion
behavior. Adding one requires a design review and a matching update to
`travel-app/scripts/check-motion-governance.mjs`.

| Owner | Purpose | Why the shared primitive is insufficient | Reduced Motion |
|---|---|---|---|
| `components/ui/DecisionSeal.tsx` | Consequential settled/confirmed ceremony | It is the one sanctioned completion beat: seal impact, one ring, then copy. | Static seal and copy; no scale, rotation, ring, or displacement. |
| `components/atlas/AtlasBoardReel.tsx` | Atlas’s bounded memory-reel composition | The reel represents a deliberate authored sequence, rather than ordinary content arrival. | Stops automatic progression; shows the current composition without travel. |
| `components/atlas/AtlasTasteBoard.tsx` | Atlas board recomposition and spatial reading | Arrangement changes preserve the board’s authored spatial evidence and cannot be a generic row transition. | Crossfade/static arrangement; no lift or layout travel. |
| `components/trip-plan/HighlightPulse.tsx` | One-time plan-change locator cue | A brief cue helps identify the itinerary block changed by an explicit action; it is not ambient attention-seeking. | No pulse; the changed block remains visibly marked. |

The registry is intentionally not a backlog. If a sequence becomes routine, it
must be absorbed into a shared primitive or removed.
