# Code Alignment — Batch 1: KILL/FOLD Surfaces (2026-07-05)

You are working in `~/travel-workspace/travel-app` (React Native / Expo, expo-router) with backend at `~/travel-workspace/travel-agent`. The product's design canon (Claude Design bundle, governance file `Vesper Canon Consolidation & Ownership.html`) has adjudicated several code surfaces as KILL or FOLD. Your job is to execute those removals so the upcoming design-alignment passes have less surface to align. This is subtraction work — remove cleanly, do not redesign anything.

## Before you start

1. `git status` in travel-app FIRST. Other sessions may have WIP in this repo. If there is uncommitted work you didn't create, work on a fresh branch from main and do not touch unrelated WIP files.
2. Run the existing test suite once before changes to know the green baseline.
3. Do each task below as its own commit. Do NOT push without explicit user approval.

## Task A — KILL: ExplanationSheet + FeedbackSheet (concierge card sheets)

Design decision: the canon deliberately removed the "why this ▾" explanation affordance from the home hero; the explanation and feedback sheets are not part of the designed product.

- Components: `components/concierge/` — the ExplanationSheet and FeedbackSheet (exact filenames may vary; locate them). **Do NOT remove ConciergeCardDecisionSheet — it stays.**
- Find every entry point (buttons, card actions, long-press menus, deck actions) that opens these two sheets and remove the affordances along with the sheets.
- FE-only: leave backend feedback endpoints alone (they may serve other surfaces).
- Remove now-dead styles, hooks, analytics events, and tests that exist solely for these sheets. Update any snapshot/journey tests that referenced the affordances.

## Task B — FOLD: SwapBlockSheet → Change Studio

Design decision: swap is an action row inside Change Studio, not a standalone sheet (already spec'd that way in the Itinerary canon).

- Component: `components/trip-plan/SwapBlockSheet.tsx` (verify path).
- Find all launch sites for the standalone swap sheet and reroute the swap action through `ChangeStudioSheet`'s existing action path. If Change Studio lacks a swap action row in code, add the minimal wiring (it is designed as an ActionRow there — no new UI patterns).
- Delete the standalone sheet once nothing references it.

## Task C — FOLD: TripDebriefSheet → Trip Document memory settle

Design decision: the post-trip debrief folds into the memory-mode settle module; no standalone debrief sheet exists in the canon.

- Component: `components/trips/TripDebriefSheet.tsx` (verify path).
- INVESTIGATE FIRST: map who opens it, what data it writes, and whether the memory surface (`/trips/[tripId]/memory` and its settle prompt) already covers the same job. 
- If the memory settle path already covers it: remove the debrief entry points + sheet.
- If the debrief writes something the memory path does not (e.g. a rating or reflection the backend expects): migrate that minimal piece into the memory settle module, then remove the sheet.
- If the fold is genuinely ambiguous or large, STOP and report options instead of implementing.

## Task D — KILL-or-fold: `/trip-place` route (conversation-first decision)

Design decision (2026-07-04): trip creation is canonically conversation-first — there is no standalone destination-picker screen in the creation flow. `/trip-dates` stays (it belongs to Trip Settings & Admin's dates-edit flow); only `/trip-place` is affected.

- Route: `app/trip-place.tsx`.
- INVESTIGATE FIRST: find all navigations to `/trip-place` (likely from `/trip-begin`, trips home, or trip-info). 
- If callers can capture destination through the existing conversational creation flow (trip-begin → chat capture) or through trip-info editing: reroute them, delete the route, and add a safe redirect for any stale deep links.
- If `/trip-place` is load-bearing for an edit context (not creation), fold it to a thin sheet variant owned by trip-info/settings rather than a creation screen, and note that in your report.
- If removal is heavy or risky, STOP and report options.

## After each task

- Typecheck (`tsc`) and run the test suite; fix or update tests that referenced removed surfaces (do not weaken unrelated tests).
- Grep for dangling references (component name, route string, analytics event names) — zero hits before committing.
- If a FEATURE.md or doc references the removed surface, update it in the same commit (pre-push doc-sync guards will fail otherwise).

## Definition of done

Four commits (or fewer if a task legitimately no-ops), green typecheck + tests, zero dangling references, a short report listing: what was removed, what was reroutered, anything you stopped on with options, and any backend endpoints now orphaned (flag only — do not remove backend code in this batch).
