---
doc_type: working
status: active
owner: founder / product / design
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Capture the self-contained Claude Design prompt for the canonical itinerary interaction redesign.
supersedes: []
source_of_truth_for: [claude-design-itinerary-redesign-prompt]
---

# Claude Design prompt — Vesper Itinerary canonical interaction redesign

Use this prompt inside the Claude Design project that contains the existing Vesper itinerary and shared design-system files.

---

This is an evolution of the current itinerary design, not a clean-sheet redesign.

## Start from the actual current design

Open **`Vesper Itinerary.html`** first. Read that file and all of its local imports completely before changing the canvas:

- `itinerary-canon.jsx`
- `design-system.jsx`
- `design-canvas.jsx`
- `tab-bar.jsx`

Use the existing components, type, material, spacing, rail, node, row, sheet, and state grammar as the visual baseline. Do not invent a new Vesper aesthetic.

Create a new Claude Design tab named exactly **`Vesper Itinerary Redesign.html`**. Do not overwrite or add redesign sections to `Vesper Itinerary.html`; keep it intact as the visual reference. Build the new redesign in the new tab, preferably with a companion source named `itinerary-redesign-canon.jsx`, while importing and reusing the existing shared design-system and design-canvas files.

## Precedence

The new behavioral contract in this prompt overrides conflicting interaction assumptions in the existing itinerary canvas. The existing canvas remains authoritative for visual language and useful state treatments, but it is not authoritative for permissions, proposals, provider consequences, recovery, or interaction sequencing.

When there is a conflict, use this order:

1. The behavioral contract in this prompt.
2. The useful visual and component grammar in `Vesper Itinerary.html` and `itinerary-canon.jsx`.
3. The shared productive type/material system.

Do not merely restyle or add actions to the existing Change Studio. Redesign the task model and prove complete journeys.

## Product goal

Design Itinerary as Vesper’s primary single-trip operational surface before and during travel: the calm place where a traveler understands the trip, inspects a stop, reshapes the plan, handles group authority, and sees what actually happened without losing context.

List and Map are two faces of the same itinerary route and editing session. The shell stays stable as the trip moves from ideation to planning, final prep, live travel, disruption, and post-trip; the emphasis and available capabilities change, not the identity of the product.

The first viewport must communicate the trip—not governance machinery, an agent feed, history, or every available fact.

## Preserve from the current Vesper itinerary

Preserve and refine these established qualities:

- iPhone 16 Pro canvas: `393 × 852`.
- Warm productive material: `#EFEAE0` background, `#F9F5ED` sheet, `#F4EFE4` / `#FBF7EC` cards, `#1B1714` ink.
- DM Sans for productive UI; JetBrains Mono for time and micro-labels.
- EB Garamond italic only for one short, useful Vesper observation when it materially helps. Never use it for actions, sheet copy, or calm filler.
- Compact date rail, time column, itinerary spine, state nodes, travel connectors, ticket band, and restrained situation treatment.
- At-rest row grammar: time, node, title (maximum two lines), at most one supporting line, at most one meaningful state treatment, and one quiet discoverable Change affordance.
- Row tap opens inspection; details and action consequences live in progressive layers, not expanded inline cards.
- State color doctrine: amber for pending/live/Vesper, oxblood for conflict/destructive consequence, blue for confirmed/changed, green for done, muted gray for skipped/gaps.
- Full-screen focused itinerary workspace. Hide the global app tab bar and do not add a persistent itinerary bottom bar.
- Calm loading, stale, conflict, empty-day, live-now, and WAS/NOW language where still truthful.

Do not turn the first viewport into a dashboard, settings page, card feed, project-management timeline, or generic AI interface. Avoid badge stacks, permanent traveler swimlanes, oversized editorial cards, gradients, generic AI glow, and decorative “all clear” modules.

## Explicitly retire these existing assumptions

- A row tap must not jump directly into Change Studio. It inspects the scheduled stop.
- Replace the overloaded Change Studio menu and its `Just for me / Suggest to group` scope toggle. Personal attendance, structural scope, and commit authority are different things.
- Do not assume every group change requires group approval, lazy consensus, or voting.
- Do not show votes unless voting is explicitly enabled for that decision. Silence is never consent.
- Review mode routes a complete proposal to the named decision owner—organizer by default in v1—not vaguely “the group.”
- Do not imply that an organizer can silently edit a personal or subgroup-owned branch merely because they organize the trip.
- Do not offer generic or timer-derived Undo. Recovery is server-authored per landed operation.
- Do not let Optimize immediately “Apply optimized order.” It requires one atomic before/after review and one commit.
- Do not use a blank dated calendar for an undated trip.
- Do not treat overlapping timestamps as a parallel plan; use an explicit split, branches, and rejoin.
- Ignore the stale bottom-bar doctrine in old reference notes. The resolved focused itinerary has no persistent bottom bar.

## Canonical information architecture

Use a compact focused header that keeps the timeline dominant:

- Back to Trips.
- Trip identity and dates; tapping identity opens Trip Details.
- Chat.
- Rare trip actions.
- Day navigation.
- Persistent List / Map face control.

Trip Details is a stable index—not a second home—with rows in this order: identity, People, Stay, Transport, Costs, Bookings, Changes/History, Settings. It should open as a medium sheet, expand when needed, and return to the exact face, day, stop, scroll/camera, and operation draft.

For group trips, header Chat opens the group room. For solo trips, it opens a private trip-scoped Vesper thread. Stop-level **Ask Vesper** is private. **Discuss** opens a group composer with a structured stop/change attachment and never auto-sends.

## Domain truths the UI must express

Keep these concepts visibly distinct when relevant:

- event structure and scope;
- planned participants;
- one traveler’s attendance;
- decision owner;
- edit authority;
- provider/booking controller;
- whether the event actually occurred.

Whole-group Open/Review governance does not erase personal or subgroup ownership.

Every Add, Move/Reorder, Replace, Remove, attendance change, Optimize, and Replan is one typed operation. One policy resolver ends the same constructed intent in one of four truthful outcomes:

- **Direct** — can apply now.
- **Confirm** — consequence requires a deliberate review and confirmation.
- **Propose** — send the exact operation to a named decision owner.
- **Denied** — explain why and offer only a safe continuation.

The construction flow should remain the same across solo, Open group, and Review group. Authority changes the ending—not the user’s ability to describe the intended change.

Vesper may advise and prepare freely, but may act only within the requesting traveler’s current authority. A meaningful solo change still requires confirmation. In Review mode, Vesper prepares the same organizer-ready proposal. It never silently performs provider work or a broad replan.

## Interaction grammar

Use proportional depth:

- **Inspection sheet:** row tap; schedule, attendance, plan state, booking truth, notes, and explicit Change entry. Place dossier is a deeper continuation, not the inspection itself.
- **Quick sheet:** personal opt in/out, simple eligible Remove, mark attended/skipped.
- **Structured sheet:** Move/Reorder and straightforward Add.
- **Full-screen choice:** Replace/search/refine/compare.
- **Full-screen review:** Optimize, broad Replan, destination/date change, or protected booking consequences.

Inspection → Change replaces the sheet rather than stacking another sheet. Back returns to inspection with context intact.

Move should begin in human relative language—“after the show,” “before dinner,” another day—not require the traveler to calculate a time first. Explicit reorder mode uses a visible drag handle, preserves booked/protected anchors, shows travel ripple during manipulation, and has an equally capable structured non-drag path. Long press may accelerate to the same actions. Row swipe has no structural meaning in v1.

Gap tap starts Add at that exact position. Day Add uses recommended placement. Add from Discover, Place, Map, or Chat constructs the same portable operation and preserves source context.

Map pin tap selects a stop and opens a compact peek. Peek tap opens the same inspection as List. Map Change opens the same canonical operation. Switching faces preserves selected day, stop/candidate, editing draft, list scroll, and map camera.

## Protected bookings and provider truth

Design two unmistakably different Replace paths:

1. **Replace in itinerary only** — changes plan truth while clearly stating that the existing reservation remains active at the original provider subject and needs resolution.
2. **Replace and rebook** — continues into Booking with the selected candidate and current reservation context preserved, then returns to the originating stop.

Permission to change the itinerary is not permission to change a provider booking. Never claim a reservation was cancelled, changed, or refunded without provider evidence. A provider partial failure produces a typed continuation such as **Resolve booking**, not generic Undo.

## Proposals, concurrency, and recovery

A pending proposal preserves the author’s exact operation and authored policy snapshot. At acceptance time, current authority, current revision, protected-state facts, membership, and provider facts are revalidated. Show stale/rebase/review outcomes honestly; do not silently apply an old proposal to a changed plan.

Recovery controls come only from the landed operation’s current capability. The possible treatments are:

- Undo;
- Withdraw request;
- Review revert;
- Provider action;
- Make another change;
- no recovery action.

Do not show a countdown-based Undo or infer recoverability from action type. Preview may describe expected recovery, but the landed receipt shows only the server-proven capability. Immediate receipt, stop history, and trip-wide Changes must agree on before/after, attribution, plan truth, provider truth, and recovery.

Open proposal decisions stay in Review Stack and in the affected itinerary context. Changes/History owns settled operations plus exceptional provider/recovery obligations, not a duplicate voting inbox.

## Lifecycle and group states

Design the following truths without changing the core shell:

- **Undated Trip Shape:** destination intent, known anchors, loose regions/themes, and missing dates. No fabricated days. Confirming destination and dates materializes one attributed Vesper-shaped first dated draft for reaction.
- **Dated planning / final prep:** day rail and full editing grammar.
- **Live:** focus today and now/next; preserve the compact live card and direct operational actions.
- **Disruption:** closure/weather/delay is an overlay on the current lifecycle, not a new alarm-style product.
- **Post-trip completed:** fresh entry defaults to Memory, with the final itinerary retained.
- **Cancelled:** fresh entry defaults to the retained itinerary plus closure work; do not fabricate memories.

For parallel plans, keep one shared spine, visibly split into simultaneous compact branches, label attendees and each branch’s decision owner, then visibly rejoin at the next shared stop. Do not duplicate the whole day by traveler. Split, branch membership/ownership, content, and rejoin are one atomic compound operation. Include a screen-reader-friendly linear reading order annotation.

Personal attendance is not plan truth: “I’m not joining” must not remove, move, or mark the event skipped for everyone.

## Required new canvas sections and journeys

Build real screen sequences with transition captions, not isolated component specimens.

### 1. Canonical shell and first sight

- Ordinary dated planning day in List.
- Same context in Map.
- Stop inspection sheet.
- Compact Trip Details sheet.
- Live now/next state.
- Undated Trip Shape and first dated draft.

### 2. North-star flow A — Put this after that

Show: inspect dinner → Change → Move → choose relative placement after the show → preview timing/travel ripple → Direct or Confirm CTA → return to the same day with landed highlight/receipt → server-proven recovery.

Provide the accessible structured equivalent to drag, and show a stale revision rebase variant.

### 3. North-star flow B — Find a better replacement

Show: inspect stop → Change → Replace → search/refine/compare real candidates → preserve itinerary chrome and day context → choose candidate → distinguish itinerary-only from replace-and-rebook → consequence review → landed plan/provider truth → valid recovery or provider continuation.

### 4. North-star flow C — Split up and rejoin

Show: shared spine → create two compact branches → assign participants and explicit decision owners → preview the next shared rejoin → commit atomically → landed split/rejoin → one traveler changes only their attendance.

### 5. Same intent, different authority ending

Using the same Move or Replace construction, show a compact matrix for:

- solo/Open owner: Apply now;
- meaningful/protected change: Review and confirm;
- Review-mode non-owner: Send to **Ana** (named owner);
- denied/private scope: truthful reason and safe continuation.

Then show organizer review, author withdrawal, stale/rebase, optional explicit voting, and accepted/rejected outcomes. Do not render voting in the default organizer-review state.

### 6. Atomic Optimize / contextual Replan

Show one full-screen before/after review with all affected stops, protected anchors, travel deltas, participant effects, provider implications, and one atomic Confirm. Include destination/date change over an existing protected plan. No sequential per-row apply and no partially landed topology.

### 7. Receipts and history continuity

Show one operation across:

- immediate landed treatment on the affected day;
- stop history;
- trip-wide Changes / operation detail.

Include plan-only Replace, provider partial failure, removed-stop tombstone/successor navigation, Withdraw, Review revert, and an honest no-recovery state. One travel intention must appear as one operation, not several disconnected feed items.

## Annotation and fidelity requirements

- Label every artboard with lifecycle, governance mode, scope/owner, capability outcome, and whether the state is shipped or implementation-required.
- Add concise transition arrows/captions showing trigger, preserved context, and next state.
- Use realistic trip content and names consistently across a journey.
- Make the principal CTAs explicit: `Move stop`, `Confirm change`, `Send to Ana`, `Replace in itinerary`, `Continue to rebook`, `Withdraw request`, `Resolve booking`, etc. Avoid vague `Apply`, `Done`, or `Suggest to group` where the outcome is ambiguous.
- Show failure, offline/unknown, stale, and loading states without falsely claiming success.
- Every interactive target should be at least 44 pt; primary actions with supporting copy should be at least 52 pt.
- No accepted screenshot may have global bottom navigation, dev/mock overlays, clipped sheets, obscured first actions, or unsafe bottom spacing.
- Keep at-rest rows calm. Put explanation, authority, receipts, attendee management, and provider consequences into the correct progressive layer.

## Definition of done

Do not finish with a written recommendation only. Modify the canvas and leave it renderable.

The redesign is ready for review when a first-time traveler can, without instruction:

1. inspect a stop without accidentally editing it;
2. move it using relative trip language;
3. find and compare a real replacement;
4. distinguish personal attendance from changing the shared event;
5. understand a split/rejoin day;
6. know whether a change applied, needs confirmation, was sent to a named owner, or is denied;
7. distinguish plan truth from booking/provider truth;
8. recover using only a truthful current capability;
9. understand an undated Trip Shape and the first dated draft;
10. switch List/Map or enter another surface and return without losing selection, position, or draft.

If an existing visual convention conflicts with this task model, preserve the Vesper material and redesign the interaction. Do not preserve incorrect behavior merely because an existing component already renders it.
