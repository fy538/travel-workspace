---
doc_type: working
status: active
owner: founder / product / design
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Add the journey, authority, implementation-posture, terminology, and current-artifact correction requirements omitted from the Claude Design itinerary redesign prompt without rewriting that prompt.
supplements: claude-design-itinerary-redesign-prompt-2026-07-13.md
supersedes: []
---

# Claude Design itinerary redesign — gap addendum

Use this document as a companion to `claude-design-itinerary-redesign-prompt-2026-07-13.md`. It does not replace or restate that prompt. Its only purpose is to close requirements that are explicit in the accepted business, UX, and surface contracts but missing or ambiguous in the Claude Design handoff.

## Canonical precedence

The redesign prompt overrides conflicting behavior in the old Claude canvas, but the prompt is a derived execution brief rather than the highest product authority. If this addendum, the prompt, or an existing design is ambiguous, use this order:

1. Product Thesis and What We Believe.
2. Accepted founder rulings and business contracts in `itinerary-interaction-business-logic-audit-2026-07-12.md`.
3. `itinerary-interaction-ux-audit-2026-07-12.md`.
4. The Trip Itinerary surface contract.
5. This addendum and the Claude Design redesign prompt as execution instructions.
6. Existing Claude canvases and components as visual and shipped-state reference.

Do not use this addendum to reopen settled product rulings or to preserve behavior merely because it already has a component.

## Design posture and truth labels

The canvas is an exploratory target interaction prototype. It is not evidence that every target capability is implemented.

Audit and correct every existing artboard so it is labeled **Shipped**, **Implementation-required**, or **Later extension**. Default redesign behavior to **Implementation-required** unless current implementation evidence proves that exact state is shipped. In addition:

- Use **server-proven** only when current implementation evidence supports the exact capability shown.
- Most Add, Move/Reorder, Replace, proposal, Optimize/Replan, parallel-topology, and provider recovery states remain implementation-required.
- Direct future-unbooked Remove is the currently proven atomic Undo slice. Do not generalize that proof to other operations.
- A predicted recovery shown during preview is not the landed recovery control.
- Do not represent a generic Undo merely to complete a visual flow. Show the operation's truthful current capability: Undo, Withdraw request, Review revert, provider action, Make another change, or none.

## Current redesign correction pass

Apply this addendum to the redesign that already exists in **`Vesper Itinerary Redesign.html`**. Preserve and extend that tab and its companion redesign source files. Do not restart the investigation, overwrite `Vesper Itinerary.html`, or create another itinerary-redesign tab.

Before adding supplemental journeys, correct the current board:

1. **Truth labels:** audit every existing screen. Most redesign screens are target behavior and must not inherit `Shipped` from a default component value. Use `Implementation-required` unless exact shipped evidence is known; reserve `Later extension` for genuinely deferred behavior.
2. **Recovery evidence:** remove every statement that Move Undo is currently `server-proven`, including Move receipts, authority comparisons, stop history, and trip-wide Changes. For current-evidence Move fixtures, show the truthful current continuation—such as `Make another change` or none. A hypothetical future Move Undo may appear only as an explicitly implementation-required capability variant and must not be described as proven.
3. **Map geometry and material:** place route geometry and pins in one coordinate system so every pin sits on its route and no pin is displaced by applying the header offset twice. Remove unintended decorative gradients and preserve the established restrained Map material.
4. **Protected replan:** resolve the contradiction between protected items labeled `Blocks` and a CTA that still confirms the shift. If an item blocks plan commit, resolve it first or end in Denied. If a plan-only re-date may commit while provider truth remains unresolved, label the item as an unresolved post-commit obligation rather than a blocker. Never describe internal resolution obligations as queued provider success.
5. **Review Stack versus Changes:** remove open-proposal counts and badges from the `Changes / History` Trip Details row. Ordinary pending proposals belong to Review Stack and the affected itinerary context. Changes owns settled operations plus exceptional provider/recovery obligations.
6. **First-draft reaction:** add visible in-device actions for keeping the first dated draft, reshaping it, or opening a day. Do not rely on an artboard caption to express the primary reaction model.
7. **History depth:** complete the existing history section with a canonical operation-detail screen, removed-stop tombstone and successor navigation, Review-revert continuation, provider-obligation detail, and an honest no-recovery state. Do not represent these only as compact ledger tags.
8. **Lifecycle and degradation:** add compact proofs for disruption as an overlay, completed-trip entry to Memory with retained Itinerary, cancelled-trip entry to retained Itinerary and closure work, and loading/offline/unknown outcomes that never masquerade as success.
9. **Design-file status:** register `Vesper Itinerary Redesign.html` in the project index as **Target / Exploration**, not Canon. Keep implementation routing on the currently approved surface until the redesign passes review; do not leave the new tab undiscoverable or imply that its target states are already canonical.

## Required supplemental journey coverage

Add the following behavioral proofs to the redesign investigation. They may be compact, but they must show complete transitions rather than isolated specimens.

### 1. Add from itinerary and another surface

Show one portable Add operation through both entry points:

- tap an itinerary gap and add at that exact position;
- begin from Discover, Place, Map, or Chat and target a precise trip day and position.

Show construction, authority result, consequence preview, landed or proposed state, and return behavior. A cross-surface success stays on its source with a precise continuation such as `Added to Day 3 · View` or `Sent to Ana · View request`. An itinerary-originated Add lands in place. The same Add construction must remain available to a proposal-capable traveler instead of ending at a direct-route failure.

### 2. Proven future-unbooked Remove

Show the currently proven atomic Undo slice as one complete end-to-end journey:

1. Inspect a future, unbooked stop.
2. Open explicit Change and choose `Remove stop` with the affected scope named.
3. Preview what leaves the shared plan and confirm that no booking/provider state is attached.
4. Resolve authority and commit the typed Remove operation.
5. Return to the originating day with an attributed tombstone/receipt.
6. Show server-proven Undo as the landed recovery capability.
7. Undo through one linked inverse operation and return to the restored stop without creating duplicate visible history.

Keep this separate from `I'm not joining` and from post-event `Mark as skipped`. Do not use the proven Remove fixture to imply Undo proof for Add, Move, Replace, Optimize/Replan, proposals, parallel topology, or provider work.

### 3. Manual and Vesper parity

For each of the eight canonical journey families, pair the manual construction with a Vesper-mediated construction over the same fixture:

1. Inspect a stop.
2. Move/reorder.
3. Replace.
4. Add.
5. Parallel subgroup split/rejoin.
6. Personal attendance.
7. Review-mode member proposal.
8. Undo, Withdraw, Review revert, or stale recovery.

Each pair must converge on the same typed operation, authority result, landed state, attribution, provider truth, and recovery semantics. Vesper may recommend and prepare the operation, but chat must not become a second editor and Vesper must not gain authority unavailable to its human principal.

### 4. Governance or membership change while a draft exists

Show a traveler constructing a complete change, then changing one relevant condition before commit:

- Open changes to Review;
- the organizer or subgroup decision owner changes;
- a relevant traveler joins or leaves; or
- branch ownership changes.

Preserve the authored intent and draft inputs, re-resolve current authority and protected facts, and change the final CTA truthfully. Never silently apply the old draft or discard it without explanation.

### 5. Shared-edit awareness

Show an authorized Open-group direct edit from both perspectives:

- the actor sees the landed result and attribution;
- an affected traveler sees proportional, deduplicated awareness tied to the same operation and current stop.

Itinerary/history remains plan truth even if a push notification or chat receipt fails. Do not use chat spam as the collaboration model, and do not render the same operation as several unrelated notices.

### 6. Missing history and privacy proofs

Supplement the receipt/history sequence with compact proofs for:

- viewer-specific history projection for owner, current member, organizer, new member, departed member, and public viewer;
- membership or account deletion without leaking private rationale, constraints, payment information, or provider secrets;
- offline and cross-device reconciliation without presenting an unknown outcome as applied;
- post-trip factual correction of attendance or occurrence without reopening structural itinerary editing;
- durable unseen state based on the viewer cursor, distinct from Needs attention.

These may share one history board, but each must identify whose view is shown and which information is intentionally omitted.

## Authority interpretation correction

Interpret the prompt's `solo/Open owner: Apply now` example narrowly. Direct apply is appropriate only when the actor is authorized and the operation is low-risk, unprotected, lifecycle-eligible, and within provider constraints.

Ownership does not by itself guarantee Direct. The final outcome still comes from the canonical resolver:

- **Direct** for an authorized, low-risk, unprotected operation;
- **Confirm** for a meaningful, broad, protected, or consequential operation the actor is allowed to commit;
- **Propose** when the exact operation must go to the named decision owner;
- **Denied** when no safe commit or proposal path exists.

Use a concrete actor, scope, governance mode, risk level, and protected-state fixture on every authority comparison. Do not use organizer status as shorthand for universal edit authority.

## Vocabulary boundaries

Keep these verbs and facts visibly separate:

| User intent | Preferred language | Must not imply |
|---|---|---|
| One traveler will not attend | `I'm not joining` / personal attendance | The event was removed or skipped for everyone |
| Remove shared plan structure | `Remove stop for everyone` or another explicit affected scope | A personal opt-out |
| Record what actually occurred | `Mark as attended` / `Mark as skipped` with occurrence context | A future structural edit or attendance preference |
| Change itinerary truth only | `Replace in itinerary` | The provider reservation changed |
| Continue provider work | `Continue to rebook` / `Resolve booking` | Provider success without evidence |

Do not use `Skip` as an ambiguous shortcut for personal attendance, structural Remove, and actual occurrence.

## Resolver outcomes versus execution states

Direct, Confirm, Propose, and Denied describe the policy result for a constructed intent. They are not substitutes for execution state.

Separately design truthful execution states when relevant: draft, previewing, waiting for confirmation, waiting for owner, applying, applied, stale/rebase required, offline/waiting to send, failed before mutation, partially completed, provider uncertain, withdrawn, reverted, and no longer recoverable.

An operation can therefore be resolved as Direct and later fail or become stale. A proposal can be accepted and still require provider resolution. Do not collapse these distinctions into one status badge.

## Adjacent-surface boundaries

- `Rare trip actions` is not permission to invent a new catch-all menu. Show only actions supported by the accepted contracts or label the slot without defining speculative behavior.
- Trip Details may show the fixed Transport and Bookings rows, including honest implementation-required or absence states, but this investigation must not invent the complete Transport, Booking, Costs, Stay, or Settings destination screens.
- Demonstrate the post-trip entry decision between Memory and retained Itinerary, but do not redesign Memory itself.
- Replace may use Discover/Places content while retaining trip chrome; it must not become a redesign of the Discover product.

## Trip Shape governance proof

The undated Trip Shape and first dated draft are shared governed trip truth, not a private generative toy.

Show:

- who may confirm destination and dates;
- what a non-owner can construct or send for review;
- that materialization creates one attributed first-draft operation;
- how travelers react to the draft without starting from an empty dated calendar; and
- how protected anchors or ownership affect later destination/date revision.

## Small-screen shell validation

At 393 points wide, explicitly validate how Back, trip identity/dates, Chat, rare actions, day navigation, and List/Map remain reachable without crowding the first viewport. Show the compact and scrolled header treatments rather than assuming every control fits simultaneously.

Preserve a visible trip identity and an immediate List/Map path on the Map face. Do not make Back the only way to return to List.

## Review sequence

Develop and review the canvas in behavioral slices even if all slices live in one design file:

1. Shell, first sight, inspection, Move, and Replace.
2. Add, proven future-unbooked Remove, List/Map continuity, and return-token behavior.
3. Manual/Vesper parity and Direct/Confirm/Propose/Denied endings.
4. Provider truth, landed receipts, history, and recovery.
5. Parallel plans, governance transitions, awareness, and lifecycle edges.

Do not treat later-slice polish as compensation for unresolved comprehension in an earlier slice. The first review gate is whether Move and Replace are obvious on a device without instruction.

## Supplemental completion check

The redesign handoff is complete only when reviewers can also verify that:

1. Add works from an exact itinerary gap and from another surface.
2. Future-unbooked Remove demonstrates the currently proven atomic Undo without generalizing that proof.
3. Manual and Vesper entry produce the same operation semantics.
4. A mid-draft authority or membership change preserves intent and changes the CTA safely.
5. An affected traveler can understand a direct shared edit without relying on chat.
6. Personal attendance, shared removal, and actual occurrence cannot be confused.
7. Resolver outcome, execution state, plan truth, and provider truth remain distinct.
8. History does not leak private information across viewer or membership boundaries.
9. Offline, stale, partial, and unknown states never masquerade as success.
10. Trip Shape exposes shared governance and attributed first-draft materialization.
11. The compact shell remains usable at the target device width.
