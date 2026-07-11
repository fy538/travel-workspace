# Vesper Canon — Micro-Session: Trip-Map Route Mapping Update (2026-07-05)

One small governance edit — no artboards, no redesign.

Context: the codebase implemented Route & Transport's existing doctrine ("Map is the second face of the itinerary — not a separate screen. A single icon flips the view."). As of 2026-07-05, `/trips/[tripId]/map` in the app is a REDIRECT-ONLY alias: it forwards to the Plan screen with `?face=map`, preserving focus/layer params. List and map share one state (active day, selection, gap indicators). The code cites the canon in its docstring — this is compliance, not drift. Only the governance route-mapping table is stale.

In `Vesper Canon Consolidation & Ownership.html`:

1. **§02b route mapping, the `/(tabs)/trips/[tripId]/map` row**: change from "Route & Transport (PRODUCTIVE)" standalone-route framing to: "REDIRECT ALIAS → `/trips/[tripId]/plan?face=map` (implemented 2026-07-05 per Route & Transport second-face doctrine). Vesper Itinerary owns the face-toggle mechanics and shared list/map state; Vesper Route & Transport owns the map face's visual canon (9 map artboards, pin/route-line/chrome tokens, suppress rules)."
2. Add one line to the ownership notes of BOTH Vesper Itinerary and Vesper Route & Transport recording the same split, so neither page's reader infers a standalone map screen.
3. Log the adjudication as a dated row in the 02d Ownership Adjudications table, status APPLIED (code already conforms — this entry records the bookkeeping).

Done = the three edits above; export a handoff.
