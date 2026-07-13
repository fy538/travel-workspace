---
doc_type: working
status: active
owner: founder / product / design
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Provide a self-contained execution prompt combining the accepted itinerary redesign brief, gap addendum, and component-alignment audit.
supersedes_for_execution:
  - claude-design-itinerary-redesign-prompt-2026-07-13.md
  - claude-design-itinerary-redesign-prompt-gap-addendum-2026-07-13.md
---

# Claude Code prompt — revise the Vesper Itinerary Redesign

Paste everything below this line into Claude Code with its working directory set to the Vesper design project containing `Vesper Itinerary Redesign.html`.

---

Revise the existing **`Vesper Itinerary Redesign.html`** and its companion `itinerary-redesign-*.jsx` files. This is a correction, completion, and component-consolidation pass over the current redesign—not a clean-sheet redesign.

Do not create another itinerary-redesign page. Do not overwrite `Vesper Itinerary.html`. Do not refer to earlier numbered exports or assume any context outside this prompt. Inspect the current board before editing, preserve work that already satisfies the contract, and correct or complete it in place. If a requirement is already represented correctly, do not duplicate it in a new section.

The final result must be a renderable design canvas with complete device sequences and concise annotations. Do not stop at an audit report, component inventory, or written recommendation.

## 1. Read the project in the canonical order

Read these sources before changing the canvas:

1. `Vesper Design Canon Index.html`
2. `Vesper Canon Consolidation & Ownership.html`
3. `Vesper Itinerary Redesign.html` and every `itinerary-redesign-*.jsx` file it imports
4. `Vesper Itinerary.html` and `itinerary-canon.jsx`
5. The relevant companion and owner surfaces:
   - `Vesper Productive Type & Material.html`
   - `Vesper Header System.html`
   - `Vesper Header Audit.html`
   - `Vesper Button Decisions.html`
   - `Vesper Row System.html`
   - `Vesper Route & Transport.html`
   - `Vesper Cards.html`
   - `Vesper Trust & Controls.html`
   - `Vesper Changes System.html`
   - `Vesper Universal Search.html`
   - `Vesper People and Collaboration.html`
6. The active shared component sources imported by those pages, especially:
   - `productive-header.jsx`
   - `buttons.jsx`
   - `sheet-atoms.jsx`
   - `sheet-header.jsx`
   - `sheet-field.jsx`
   - `status-pill.jsx`
   - `avatar.jsx`
   - `row-system.jsx`
   - `vesper-cards-kit.jsx`
   - `universal-search-app.jsx`

Do not treat an orphaned JSX file as design truth merely because it exists. Top-level canonical pages define ownership; their active imported sources provide the reusable implementation.

## 2. Precedence and design posture

Use this precedence when sources disagree:

1. Product Thesis and What We Believe.
2. Accepted founder rulings and business contracts.
3. The accepted itinerary interaction and UX contract encoded in this prompt.
4. Current canonical surface owners and companion systems.
5. The current redesign as an exploratory implementation.
6. The older itinerary canvas as visual and shipped-state reference.

The redesign is **Target / Exploration**, not Canon and not proof that the target behavior is implemented. Keep implementation routing on `Vesper Itinerary.html` until review explicitly promotes the redesign.

Every artboard must label its posture as one of:

- **Shipped**
- **Implementation-required**
- **Later extension**

Default redesigned Add, Move/Reorder, Replace, proposal, Optimize/Replan, parallel topology, and provider-recovery states to **Implementation-required** unless exact current implementation evidence proves otherwise. The currently proven atomic Undo slice is direct removal of a future, unbooked stop. Do not generalize that proof.

## 3. Product goal

Design Itinerary as Vesper’s primary single-trip operational surface before and during travel: the calm place where a traveler understands the trip, inspects a stop, reshapes the plan, handles group authority, and sees what actually happened without losing context.

List and Map are two faces of the same itinerary route and editing session. The shell remains recognizable across ideation, planning, final preparation, live travel, disruption, and post-trip states. Emphasis and capabilities may change; the product’s identity should not.

The first viewport must communicate the trip. It must not become a governance dashboard, agent feed, history screen, settings page, card feed, or generic AI interface.

## 4. Preserve the successful itinerary language

Preserve and refine:

- The `393 × 852` iPhone 16 Pro canvas.
- Warm productive material: `#EFEAE0` background, `#F9F5ED` sheet, `#F4EFE4` / `#FBF7EC` cards, and `#1B1714` ink.
- DM Sans for productive UI and JetBrains Mono for time/data/micro-labels.
- EB Garamond italic only for a short, materially useful Vesper observation—not actions, sheet instructions, or decorative calm filler.
- The compact date rail, time column, itinerary spine, state nodes, travel connectors, ticket band, and restrained situation treatment.
- At-rest row grammar: time, node, title of at most two lines, no more than one supporting line, no more than one meaningful state treatment, and one quiet discoverable Change affordance.
- Row tap for inspection. Details and consequences belong in progressive layers, not expanded inline cards.
- State color doctrine: amber for pending/live/Vesper, oxblood for conflict or destructive consequence, blue for confirmed/changed, green for done, and muted gray for skipped/gaps.
- Full-screen focused itinerary workspace with no global tab bar and no persistent itinerary bottom bar.
- The new List/Map face control, relative Move language, selected/candidate/split/tombstone states, and portable operation model when they satisfy the contracts below.

Do not turn the surface into a card-heavy project timeline. Avoid badge stacks, permanent traveler swimlanes, oversized editorial cards, gradients, generic AI glow, and decorative “all clear” modules.

## 5. Component alignment and surface ownership

The current redesign is visually Vesper-like but redefines too many app-wide primitives locally. Correct that without flattening the itinerary’s legitimate domain-specific grammar.

Apply this decision rule to every visible element:

1. If an exact shared component exists, consume it.
2. If the element belongs to itinerary grammar, extend the existing itinerary component and add only the required variants.
3. If the interaction is genuinely new, create a clearly named Plan-specific component and document why it is distinct.
4. If an adjacent surface owns the visual canon, consume that owner’s language instead of redrawing it locally.
5. Do not replace a domain-specific itinerary primitive with a generic component when doing so loses required meaning or interaction density.

Add a compact **Component alignment and ownership** appendix outside the device frames. For each primitive family, show: current redesign element, canonical owner, disposition (`reuse`, `extend`, `replace`, or `sanctioned Plan exception`), and the reason. Keep prototype metadata outside phones so it cannot be mistaken for production UI.

### 5.1 Itinerary-owned components to preserve or extend

Preserve `DateRail`, `SpineRow`, travel bands/connectors, day-spine sections, gap rows, split branches, rejoin treatments, and the List/Map face control as itinerary-owned grammar. Consolidate them with the existing itinerary primitives rather than leaving a second unnamed copy.

New selected, split, candidate, tombstone, proposal, and changed states may be sanctioned variants. Do not force these into a generic Row System timeline row if that weakens the itinerary’s time/node/spine semantics.

Rename generic local primitives so their ownership is explicit. For example, a genuinely distinct multiline itinerary commit control should be `PlanOperationButton` or `OperationCTA`, not a second app-wide `Btn`.

### 5.2 Map must use Route & Transport’s visual canon

Retain the itinerary’s List/Map state model, selected day, selected stop/candidate, preserved draft, list position, and camera position. Redraw the Map face using the visual canon owned by `Vesper Route & Transport.html`:

- confirmed stop: ink-filled numbered circle;
- selected stop: amber-filled circle with amber halo;
- tentative stop: parchment marker with dashed ink border;
- no-pin state: parchment marker with amber border;
- confirmed day route: solid 3 px ink;
- dashed treatment only for missing transport, uncertainty, or gaps;
- canonical map background/tile material and peek/sheet geometry.

Remove the conflicting teardrop-pin family, black selected teardrop, state-outline invention, and amber dotted confirmed route. Put route geometry and pins in one coordinate system so pins sit on routes and header offsets are not applied twice.

### 5.3 Header should extend the focused itinerary header

Treat the three-row Plan shell as an evolution of the canonical focused itinerary header, not an unrelated generic `Header` primitive.

- Back returns to **Trip**, not **Trips**.
- Keep trip identity/dates, Chat, day navigation, and immediate List/Map access.
- Chat and persistent List/Map may be documented Plan-specific extensions.
- Rare trip actions must not become an invented catch-all menu.
- Validate compact and scrolled treatments at 393 points. Do not assume Back, identity, dates, Chat, actions, day navigation, and List/Map all fit without prioritization.
- Preserve visible trip identity and an immediate path back to List on the Map face.

### 5.4 Classify sheets versus pushed task screens

The current redesign hand-rolls sheet chrome and frequently uses a back chevron inside a sheet. Correct every state by classifying it:

- A real bottom/action sheet uses the canonical `VSheet`, handle, and `SheetHeader`, with close or a clear action. It does not pretend to be a pushed screen.
- A full-screen search, compare, replan, or complex editor uses the appropriate full-screen productive/focused header.
- Inspection → Change replaces the sheet instead of stacking another sheet. Back from Change returns to inspection with the original context intact.
- If a nested Plan sheet navigator is genuinely unavoidable, document it as a sanctioned exception with a demonstrated need; do not silently make back-chevron sheets a new generic pattern.

Align sheet radius, handle metrics, safe-area behavior, header spacing, close/action placement, and scroll behavior with the canonical atoms. Convert the local two-column fact row into a thin itinerary wrapper around the canonical sheet-field metrics, or explicitly document why its anatomy differs.

### 5.5 Use the shared receipt and consequence systems

Remove bespoke black “landed receipt” cards. Applied-change feedback must use one of:

- a compact, fading in-context consequence treatment when the changed itinerary is already visible; or
- the shared Trust/Transact `ReceiptFace` anatomy for durable operation evidence and history detail.

Immediate receipt, stop history, trip-wide Changes, and operation detail must show the same operation identity, before/after, attribution, plan truth, provider truth, and current recovery capability. The current capability may be Undo, Withdraw request, Review revert, provider action, Make another change, or none.

### 5.6 Use productive rows, icons, search, and avatars

- Rebuild Trip Details with the canonical productive settings-row anatomy and proper bare line SVG icons. Remove Unicode stand-ins and rounded-square utility icon wells.
- Render settled Changes through the canonical flat `ChangesLedgerRow` anatomy or a documented operation-specific extension—not a stack of bespoke rounded cards.
- Base Add/Replace search on the Universal Search field behavior, including real input, clear/cancel behavior, scope, and empty/loading states. Do not use a small decorative pseudo-input.
- Use the productive tinted avatar/monogram species owned by the app for people, ownership, and proposal rows. Do not introduce a third solid-monogram avatar family.
- Use shared status pills only for true statuses. Do not convert every piece of metadata into a pill.

### 5.7 Adjudicate buttons instead of normalizing blindly

The shared stadium `VBtn` is correct for ordinary primary, secondary, and ghost actions. A square or multiline itinerary operation CTA may remain distinct when it needs to carry consequence or commit-supporting copy.

For every button species:

- name its owner and intended use;
- use the shared component where exact;
- reserve the Plan-specific operation button for operations that earn the distinction;
- include default, pressed, disabled, loading/applying, and destructive states;
- preserve a minimum 44 pt target, and at least 52 pt for primary actions with supporting copy;
- use explicit outcome labels such as `Move stop`, `Confirm change`, `Send to Ana`, `Replace in itinerary`, `Continue to rebook`, `Withdraw request`, and `Resolve booking`.

Avoid ambiguous `Apply`, `Done`, or `Suggest to group` when the result is not obvious.

### 5.8 Correct semantic contrast

`muteSoft` is decorative-only and must not carry meaningful text. Replace it with the readable `mute` token for help, recovery explanations, return behavior, provider information, unchanged-state explanations, Changes introductions, and other copy a traveler must understand. Reserve `muteSoft` for dividers, placeholders, and details that may safely disappear.

## 6. Canonical task model

Retire these incorrect assumptions wherever they remain:

- Row tap does not jump directly into Change Studio; it inspects the scheduled stop.
- Do not preserve an overloaded Change Studio menu or a `Just for me / Suggest to group` scope toggle. Personal attendance, structural scope, and commit authority are different facts.
- Group changes do not automatically require group approval, lazy consensus, or voting.
- Never show votes unless voting is explicitly enabled for that decision. Silence is not consent.
- Review sends one complete operation to the named decision owner—organizer by default in the initial policy—not vaguely “the group.”
- Organizer status does not grant universal edit authority over personal or subgroup-owned branches.
- Recovery is server-authored per landed operation. Never infer Undo from action type or a timer.
- Optimize/Replan requires one atomic before/after review and one commit; never sequential per-row apply.
- An undated trip is Trip Shape, not a blank dated calendar.
- Overlapping timestamps are not a parallel plan. Parallel topology requires an explicit split, branches, and rejoin.

Every Add, Move/Reorder, Replace, Remove, attendance change, Optimize, and Replan is one typed operation. One policy resolver ends the same fully constructed intent in one of four outcomes:

- **Direct** — authorized, low-risk, unprotected, lifecycle-eligible, and provider-safe; can apply now.
- **Confirm** — the actor may commit, but a meaningful, broad, protected, or consequential effect requires deliberate review.
- **Propose** — route the exact operation to the named decision owner.
- **Denied** — explain why and offer only a safe continuation.

The construction path stays substantially the same across solo, Open group, and Review group. Authority changes the ending, not the traveler’s ability to describe the intended change.

Direct, Confirm, Propose, and Denied are policy results, not execution states. Separately represent draft, previewing, waiting for confirmation, waiting for owner, applying, applied, stale/rebase required, offline/waiting to send, failed before mutation, partially completed, provider uncertain, withdrawn, reverted, and no longer recoverable.

An operation resolved as Direct may later fail or become stale. An accepted proposal may still require provider resolution. Do not collapse these truths into one status badge.

## 7. Domain truths and vocabulary

Keep visibly distinct when relevant:

- event structure and affected scope;
- planned participants;
- one traveler’s attendance;
- decision owner;
- edit authority;
- provider/booking controller;
- whether the event actually occurred.

Use unambiguous language:

| User intent | Preferred language | Must not imply |
|---|---|---|
| One traveler will not attend | `I'm not joining` / personal attendance | The event was removed or skipped for everyone |
| Remove shared plan structure | `Remove stop for everyone` or explicit affected scope | A personal opt-out |
| Record what occurred | `Mark as attended` / `Mark as skipped` with occurrence context | A future structural edit |
| Change plan truth only | `Replace in itinerary` | The provider reservation changed |
| Continue provider work | `Continue to rebook` / `Resolve booking` | Provider success without evidence |

Do not use `Skip` as shorthand for attendance, structural Remove, and actual occurrence.

## 8. Canonical shell and information architecture

Keep the timeline dominant. The focused header contains:

- Back to Trip;
- trip identity and dates, opening Trip Details;
- Chat;
- only supported rare trip actions;
- day navigation;
- persistent List/Map control.

Trip Details is a stable index, not a second home. Use rows in this order: Identity, People, Stay, Transport, Costs, Bookings, Changes/History, Settings. It may open as a medium sheet and expand when necessary. Closing it returns to the exact face, day, stop, scroll/camera, and operation draft.

Do not show open-proposal counts or Review Stack badges on Changes/History. Ordinary pending proposals live in Review Stack and the affected itinerary context. Changes owns settled operations plus exceptional provider/recovery obligations.

For group trips, header Chat opens the group room. For solo trips, it opens a private trip-scoped Vesper thread. Stop-level `Ask Vesper` is private. `Discuss` opens a group composer with a structured stop/change attachment and never auto-sends.

## 9. Interaction depth and continuity

Use proportional depth:

- **Inspection sheet:** schedule, attendance, plan state, booking truth, notes, and explicit Change entry. A place dossier is a deeper continuation.
- **Quick sheet:** personal opt in/out, simple eligible Remove, mark attended/skipped.
- **Structured task sheet:** Move/Reorder and straightforward Add.
- **Full-screen choice:** Replace/search/refine/compare.
- **Full-screen review:** Optimize, broad Replan, destination/date change, or protected-booking consequences.

Move begins in human relative language such as `after the show`, `before dinner`, or another day. Do not force time calculation first. Explicit reorder mode has a visible drag handle, preserves booked/protected anchors, shows travel ripple during manipulation, and has an equally capable structured non-drag path. Long press may accelerate to the same actions. Row swipe has no structural meaning.

Gap tap begins Add at that exact position. Day Add uses recommended placement. Discover, Place, Map, and Chat construct the same portable Add operation while preserving source context.

Map pin tap selects a stop and opens a compact peek. Peek tap opens the same inspection used by List. Map Change opens the same operation. Switching faces preserves selected day, selected stop/candidate, operation draft, list scroll, and map camera.

## 10. Protected bookings and provider truth

Design two unmistakably different Replace paths:

1. **Replace in itinerary** changes plan truth while stating that the original reservation remains active and needs resolution.
2. **Replace and rebook** continues to Booking with the candidate and current reservation context preserved, then returns to the originating stop.

Permission to change the itinerary is not permission to change a provider booking. Never claim that a reservation was cancelled, changed, refunded, or queued successfully without provider evidence. A partial provider failure produces a typed continuation such as `Resolve booking`, not generic Undo.

Correct any protected-Replan contradiction:

- If a protected item truly `Blocks`, it must be resolved before plan commit or the flow ends Denied.
- If plan-only re-dating may commit while provider truth remains unresolved, call it an unresolved post-commit obligation—not a blocker and not provider success.

## 11. Proposals, concurrency, and recovery

A pending proposal preserves the author’s exact operation and authored policy snapshot. At acceptance, revalidate current authority, current plan revision, protected facts, membership, branch ownership, and provider facts. Show stale, rebase, and review outcomes honestly. Never silently apply an old proposal to a changed plan.

Show a mid-draft change to governance or membership—for example Open → Review, a changed organizer/decision owner, a traveler joining/leaving, or changed branch ownership. Preserve authored intent and inputs, rerun policy and protected checks, explain the changed result, and update the final CTA. Do not silently apply or discard the draft.

Recovery controls come only from the landed operation’s current capability:

- Undo;
- Withdraw request;
- Review revert;
- provider action;
- Make another change;
- no recovery action.

Preview may describe expected recovery. The landed state may show only the current server-proven capability. Remove every claim that Move Undo is currently server-proven. A future Move Undo may be shown only as an explicitly implementation-required variant.

## 12. Lifecycle and group states

Use one recognizable shell for:

- **Undated Trip Shape:** destination intent, known anchors, loose regions/themes, and missing dates. No fabricated days. Confirming destination and dates creates one attributed first-draft operation.
- **Dated planning/final preparation:** day rail and full editing grammar.
- **Live:** focus today and now/next with compact operational actions.
- **Disruption:** weather/closure/delay as an overlay on the existing lifecycle, not a separate alarm product.
- **Completed:** fresh entry defaults to Memory while retaining the final itinerary.
- **Cancelled:** fresh entry defaults to retained itinerary plus closure work; never fabricate memories.

Trip Shape is governed shared trip truth. Show who may confirm destination/dates, what a non-owner may construct or send for review, protected-anchor effects, and visible in-device actions to keep the first draft, reshape it, or open a day. Do not rely on an artboard caption for the reaction model.

For parallel plans, keep one shared spine, split into compact simultaneous branches, label attendees and each branch’s decision owner, and visibly rejoin at the next shared stop. Do not duplicate the whole day by traveler. Split, branch membership/ownership, content, and rejoin are one atomic compound operation. Include a screen-reader-friendly linear reading-order annotation.

Personal attendance does not mutate shared plan truth. `I'm not joining` must not remove, move, or mark the event skipped for everyone.

## 13. Required complete journeys

Use realistic names and trip content consistently within each sequence. Show transitions, preserved context, execution state, and next action. Build complete device journeys, not isolated specimens.

### 13.1 Canonical shell and first sight

Show:

- ordinary dated planning day in List;
- the same context in Map using Route & Transport’s canon;
- stop inspection;
- compact Trip Details;
- live now/next;
- Undated Trip Shape and first dated draft;
- compact and scrolled header behavior at 393 points.

### 13.2 Move — “Put this after that”

Show inspect dinner → Change → Move → relative placement after the show → timing/travel ripple preview → Direct or Confirm ending → return to the same day → landed highlight/consequence → current server-authored recovery.

Also show:

- a structured accessible equivalent to drag;
- booked/protected anchor behavior;
- stale revision/rebase;
- a current-evidence landed state that does not falsely claim proven Move Undo.

### 13.3 Replace — “Find a better replacement”

Show inspect → Change → Replace → real search/refine/compare → choose a candidate → distinguish itinerary-only from replace-and-rebook → consequence review → landed plan/provider truth → valid recovery or provider continuation.

Retain itinerary chrome, day, originating stop, and draft context throughout.

### 13.4 Add from itinerary and another surface

Use the same portable Add operation to show:

- gap tap and insertion at that exact position;
- Add beginning in Discover, Place, Map, or Chat and targeting a precise trip day/position;
- construction, consequence, authority result, landed or proposed state, and return behavior;
- itinerary-originated Add landing in place;
- cross-surface success remaining on its source with `Added to Day 3 · View`, or proposal success with `Sent to Ana · View request`;
- proposal-capable travelers completing the same construction rather than hitting a direct-route failure.

### 13.5 Proven future-unbooked Remove

Show the currently proven Undo slice end-to-end:

1. Inspect a future, unbooked stop.
2. Choose explicit `Remove stop` with affected scope.
3. Preview what leaves the shared plan and confirm there is no booking/provider state.
4. Resolve authority and commit the typed Remove.
5. Return to the originating day with one attributed tombstone/consequence.
6. Show server-proven Undo.
7. Undo through one linked inverse operation and return to the restored stop without duplicate visible history.

Keep this distinct from `I'm not joining` and `Mark as skipped`. Do not imply Undo proof for any other operation family.

### 13.6 Split up and rejoin

Show shared spine → create two branches → assign participants and explicit decision owners → preview the next shared rejoin → commit atomically → landed split/rejoin → one traveler changes only personal attendance.

### 13.7 Same intent, different authority ending

Use the same Move or Replace fixture and show concrete actor, scope, governance mode, risk, protected state, decision owner, and result:

- authorized low-risk Open/solo operation: Direct;
- meaningful or protected authorized operation: Confirm;
- Review-mode non-owner: `Send to Ana`;
- private/denied scope: truthful reason and safe continuation.

Then show organizer review, author withdrawal, stale/rebase, optional explicit voting, and accepted/rejected outcomes. Do not show voting in the default organizer-review state. Ownership alone must not guarantee Direct.

### 13.8 Manual and Vesper parity

For each family below, pair manual construction with Vesper-mediated construction over the same fixture:

1. Inspect.
2. Move/Reorder.
3. Replace.
4. Add.
5. Parallel split/rejoin.
6. Personal attendance.
7. Review-mode proposal.
8. Undo, Withdraw, Review revert, or stale recovery.

Each pair converges on the same typed operation, resolver result, landed state, attribution, provider truth, and recovery semantics. Vesper may advise and prepare but cannot gain authority unavailable to the human principal. Chat must not become a second editor.

### 13.9 Atomic Optimize and contextual Replan

Show one full-screen before/after review with every affected stop, protected anchor, travel delta, participant effect, provider implication, and one atomic Confirm. Include destination/date change over an existing protected plan. No sequential per-row apply and no partially landed topology.

### 13.10 Shared-edit awareness

Show an authorized Open-group direct edit from two perspectives:

- actor sees the landed result and attribution;
- affected traveler sees proportional, deduplicated awareness tied to the same operation and current stop.

Itinerary/history remains plan truth even if push or chat delivery fails. Do not use chat spam as the collaboration model or render one operation as unrelated notices.

### 13.11 Receipts, history, privacy, and reconciliation

Show one operation continuously across immediate in-context consequence, stop history, trip-wide Changes, and canonical operation detail. Include:

- plan-only Replace;
- provider partial failure and obligation detail;
- removed-stop tombstone and successor navigation;
- Withdraw;
- Review revert;
- honest no-recovery state;
- viewer-specific history projection for owner, current member, organizer, new member, departed member, and public viewer;
- membership/account deletion without leaking private rationale, constraints, payment data, or provider secrets;
- offline and cross-device reconciliation without presenting unknown as applied;
- post-trip factual correction of attendance/occurrence without reopening structural editing;
- durable unseen state based on viewer cursor, distinct from Needs attention.

One travel intention is one operation, not several disconnected feed items.

### 13.12 Lifecycle and degraded states

Add compact complete proofs for disruption overlay, completed-trip Memory entry with retained Itinerary, cancelled-trip retained Itinerary and closure work, and loading/offline/stale/unknown/failure outcomes that do not masquerade as success.

## 14. Adjacent-surface boundaries

- Itinerary owns the List/Map mechanics and operation session; Route & Transport owns map visuals and route-quality language.
- Changes owns settled-operation ledger anatomy; Review Stack owns ordinary pending decisions.
- Trust/Cards owns durable receipt anatomy.
- Universal Search owns search-field behavior; Replace may consume Discover/Places content without redesigning Discover.
- Trip Details may route to Transport, Bookings, Costs, Stay, and Settings, but this task must not invent those complete destination surfaces.
- Demonstrate the Memory/retained-Itinerary entry decision without redesigning Memory itself.
- `Rare trip actions` is not permission to invent unsupported behavior.

## 15. Annotation and fidelity requirements

Every artboard must identify:

- lifecycle;
- governance mode;
- actor and affected scope;
- owner/decision owner where relevant;
- policy outcome;
- execution state;
- `Shipped`, `Implementation-required`, or `Later extension`.

Add concise transition captions for trigger, preserved context, and next state. Keep those design annotations outside the device or unmistakably separated from product UI.

Also enforce:

- minimum 44 pt interactive targets;
- at least 52 pt for primary actions with supporting copy;
- correct safe-area and bottom spacing;
- no global bottom navigation in accepted itinerary screens;
- no dev/mock overlays inside accepted phones;
- no clipped sheets or obscured first actions;
- no false success during loading, offline, stale, partial, or provider-unknown states;
- calm at-rest rows, with authority, receipts, attendee management, and provider consequences moved to the correct progressive layer.

## 16. Implementation approach

Before broad edits, make a private inventory of the current local redesign primitives and their usage. Map each to its canonical owner and decide reuse, extension, replacement, or sanctioned Plan exception. Then revise in this order:

1. Shared tokens, contrast, headers, sheet anatomy, buttons, rows, icons, avatars, search, receipt/consequence treatments, and Map canon.
2. Shell, first sight, inspection, Move, and Replace.
3. Add, proven Remove, List/Map continuity, and cross-surface return tokens.
4. Manual/Vesper parity and Direct/Confirm/Propose/Denied endings.
5. Provider truth, receipts, history, privacy, reconciliation, and recovery.
6. Parallel topology, governance transitions, shared-edit awareness, and lifecycle/degraded edges.
7. Component-alignment appendix and final full-canvas QA.

Prefer importing or adapting active shared component sources to copying their code. If a shared component is close but cannot express a real itinerary need, add a narrow variant or Plan wrapper and document it. Do not modify an app-wide primitive in a way that breaks its existing consumers merely to make this board render.

Keep the redesign entry file renderable after every phase. Do not delete unrelated project files or alter other canonical product pages except for a minimal index/status correction if the redesign’s Target / Exploration registration is missing or inaccurate.

## 17. Verification

Before declaring completion:

1. Load `Vesper Itinerary Redesign.html` and inspect the full canvas for runtime errors.
2. Verify every imported script resolves and no global component name collides.
3. Inspect representative phone frames at actual size, including shell List, shell Map, inspection, Move preview/landed, Replace, Add, Remove/Undo, split/rejoin, Optimize/Replan, Trip Details, Changes, history detail, Trip Shape, live, completed, cancelled, and degraded states.
4. Check route/pin alignment, header crowding, sheet clipping, safe areas, button targets, readable contrast, and consistent icon/avatar treatment.
5. Confirm `muteSoft` is not used for meaningful text.
6. Confirm no sheet uses pushed-screen chrome without a documented exception.
7. Confirm no custom landed receipt competes with the canonical receipt/consequence systems.
8. Confirm the Map face follows Route & Transport’s marker and route families.
9. Confirm ordinary proposals are absent from Changes counts/badges.
10. Confirm only future-unbooked Remove is labeled with currently server-proven Undo.
11. Confirm every required journey has a visible trigger, preserved context, truthful ending, and continuation.
12. Confirm prototype annotations remain outside product UI.

## 18. Definition of done

Do not finish with prose alone. Modify the canvas and leave it renderable.

The revision is ready for review only when a first-time traveler can, without instruction:

1. inspect a stop without accidentally editing it;
2. move it using relative trip language;
3. find and compare a real replacement;
4. add from an exact gap or another surface and understand where it landed;
5. distinguish personal attendance, shared removal, and actual occurrence;
6. understand a split/rejoin day;
7. know whether an operation applied, needs confirmation, was sent to a named owner, was denied, failed, became stale, or remains provider-uncertain;
8. distinguish plan truth from booking/provider truth;
9. recover only through a truthful current capability;
10. understand Trip Shape and react to the first dated draft;
11. switch List/Map or enter another surface and return without losing selection, position, camera, or draft;
12. recognize the same Vesper headers, sheets, buttons, rows, icons, avatars, maps, receipts, and search behaviors used across the rest of the app;
13. identify any intentionally distinct Plan component and why it exists.

The board itself must make clear which behavior is shipped, implementation-required, or later. It must preserve the strong itinerary task model while eliminating unnecessary local component forks.

At the end, report concisely:

- files changed;
- substantive journey gaps closed;
- canonical components reused or extended;
- Plan-specific exceptions retained and why;
- any remaining blocked decisions;
- verification performed and any known rendering limitations.
