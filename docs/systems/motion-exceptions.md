---
doc_type: contract
status: active
owner: frontend / design
created: 2026-07-12
last_verified: 2026-07-16
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
| `components/atlas/AtlasReadingCanvas.tsx` | Atlas reading dive, authored sequence, and spatial recomposition | One current owner coordinates the reel and board states whose spatial evidence cannot be represented as a generic row transition. | Stops automatic travel and spring layout; shows or crossfades the current composition. |
| `components/trip-plan/HighlightPulse.tsx` | One-time plan-change locator cue | A brief cue helps identify the itinerary block changed by an explicit action; it is not ambient attention-seeking. | No pulse; the changed block remains visibly marked. |

The registry is intentionally not a backlog. If a sequence becomes routine, it
must be absorbed into a shared primitive or removed.
