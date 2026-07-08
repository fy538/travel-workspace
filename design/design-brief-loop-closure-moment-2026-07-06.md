# Design Brief — The Loop-Closing Moment (2026-07-06)

For a Claude Design session. Canon grounding: `Vesper Trip Creation.html` + `create-screens.jsx` (`CreateEntry`, `NewTrip`, `OnboardingResume`), `Vesper Trips Home.html` + `trips-home-canon-screens.jsx` (trail-section vocabulary). Read those before this brief — it assumes their vocabulary.

## Why this exists

The team's monetization thesis has one unvalidated load-bearing bet: the multiplayer invite loop must *compound* — a joiner needs to eventually start their own trip and invite their own group, not just accept one invite and stop. A 2026-07-06 investigation found the **inbound** half of this loop (organizer invites → joiner lands on a real, trip-selling peek → joins) is genuinely well-designed and built. The **outbound** half — anything that turns a joiner into an organizer — was completely absent: no surface, no copy, no analytics event, and the app's one existing viral prompt (`OrganizerInviteNudge`, in trip chat) is structurally invisible to joiners by construction (gated to `isOrganizer && travelers.length <= 1`).

A same-day code fix shipped a stopgap: a new Trips Home trail row, **"Plan one of your own,"** shown to any user whose entire trip history is trips they joined, tapping through to the existing generic `routes.tripBegin()` entry. This closed the functional gap (a joiner now has *something* to tap) but was built from pattern-matching against existing trail-row conventions, not from an actual design pass — and re-reading the canon surfaced two problems with it.

## What's wrong with the stopgap

**1. It duplicates the one-primary-affordance rule.** `Vesper Trip Creation.html` §01 and `CreateEntry`'s own code comment (`create-screens.jsx:21`, *"the begin-a-trip entry — the single, primary creation affordance"*) are explicit: Trips Home has ONE calm "Begin a trip" entry, not several competing ones. The stopgap adds a second, lower-key entry point elsewhere on the same screen. That's the exact pattern this whole alignment effort has been correcting in other surfaces (calm hero demoted to a receipt chip, a decision buried under a generic label) — done here by accident, in the thing meant to fix a demotion problem elsewhere.

**2. The destination doesn't know who just arrived.** Tapping the row lands on `NewTrip` — the same "How should we start it?" hierarchy (Talk to Vesper / saved places / a shape / blank trip) every cold user sees. Nothing acknowledges that this specific person has been inside other people's trips before. Canon already has the right idea for this, just built for a different trigger: **State D, `OnboardingResume`** (`create-screens.jsx:137-156`) — *"I remember the shape of this one,"* the trip's shape and companions (`Stack ppl={['Y','A','T']}`, "You, Ana & Theo") shown whole, asking only for the one missing piece. That's what a substrate-aware entry looks like in this design system. A joiner-conversion entry should probably borrow that grammar (Vesper naming *whose* trips you've been part of, maybe who you'd likely travel with again) rather than routing to the blank hierarchy.

## What the session needs to resolve

**Q1 — One entry or two?** Either (a) fold the joiner case into the *existing* `CreateEntry`/"Begin a trip" affordance — its copy/subtitle changes contextually when the tapping user has only ever joined trips (no new row, no duplication, matches the one-affordance rule) — or (b) keep it as a distinct second surface, but justify why this case earns an exception to that rule (the trail-section precedent — Friends/Saved/Vesper-noticed also coexist with the primary entry — may or may not extend to something this consequential). Recommend starting from (a) and only falling back to (b) if the contextual copy can't carry enough weight in the primary entry's fixed shape.

**Q2 — Does the destination personalize?** If yes, design the joiner-arrival variant of `NewTrip` (or a new State, sibling to D) using the `OnboardingResume` grammar — what does Vesper honestly know here? At minimum: which trip(s) they were part of, who else was on them. Be honest about what's real vs. what would be invented (this codebase's own discipline — see `assemblers.ts`'s "receipt is populated ONLY where the data is real" rule — should hold here too: don't fabricate a "you'd probably want to go to Lisbon" inference the substrate doesn't support).

**Q3 — Dosage.** However this resolves, it should read as an *invitation*, not a nag — this is a single person who's shown one specific pattern (only ever joined), not an urgent state. Whatever visual weight it gets should stay in the "calm register" family, not borrow the amber "needs you" treatment from the decision-promotion fix shipped alongside this stopgap.

## Explicitly out of scope

Don't reopen the general Trip Creation flow — States A/B/C/E/F/G/H (shapes, saved-bridge, promotion, blank trip, errors) are fine as-is and canon-locked. This is narrowly the entry-affordance question (Q1) and, if warranted, one new or modified State for the joiner-arrival case (Q2). Don't touch chat or notifications — this investigation didn't check whether they need an equivalent nudge, and that's a separate question if it comes up later.

## Handoff

Once resolved, this becomes a small, focused code-alignment brief (same shape as Batch E–H) to replace the current stopgap: either retire the "Plan one of your own" row and add contextual copy to the existing `CreateEntry`, or keep the row but redesign its destination. Either way, the current code (`components/trips/TripsHomeTrail.tsx`'s `showStartOwnTrip` row, `hasOnlyJoinedTrips` signal already computed in `app/(tabs)/trips/index.tsx`) is a reasonable data foundation to build the real version on — the substrate check doesn't need to change, only what's shown and where it leads.
