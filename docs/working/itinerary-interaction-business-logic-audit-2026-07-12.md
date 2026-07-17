---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-07-12
last_verified: 2026-07-16
why_new: Establish itinerary action, permission, risk, group-governance, and agent-authority rules before redesigning the interaction in Claude Design.
supersedes: []
source_of_truth_for: [itinerary-interaction-business-logic-audit]
expires: 2026-08-11
---

# Itinerary Interaction Business-Logic Audit

## Executive finding

The itinerary should be redesigned, but the visual and interaction handoff must wait until the underlying business rules are explicit.

The codebase already implements meaningful parts of the required model:

- solo versus group detection;
- organizer and member roles;
- `open`, `review`, and `locked` plan-editing settings;
- direct, proposal, and denied edit outcomes;
- low-risk agent apply versus consequential preview versus group proposal;
- voting, lazy consensus, and active approval;
- booking and terminal-state protections;
- post-trip edit denial;
- undo, revert, idempotency, and optimistic concurrency.

These rules are distributed across frontend posture checks, REST endpoints, concierge tools, proposal automation, trip settings, and prompt instructions. Some paths disagree, some concepts are overloaded, and several user-facing settings imply distinctions the backend does not currently enforce.

The deeper implementation trace originally found that the current Replace,
Move, Remove/Undo, Add, and Optimize contracts were not yet semantically
trustworthy enough to serve as the fixed foundation for a redesign. The direct
future-unbooked Remove → Undo slice was implemented and fault-injection-proven
on 2026-07-13; the remaining Replace, Move/Optimize, Add, proposal/replan, and
provider-side gaps below remain pre-design business-logic blockers, not visual
polish issues.

Before Claude Design receives a new itinerary brief, product and engineering need one canonical answer to:

> Given this actor, trip, block, action, initiator, risk, and phase, may the change apply directly, require confirmation, become a proposal, or be denied?

## Relationship to the UX audit

The companion frontend document is:

- `travel-app/docs/audits/itinerary-interaction-ux-audit-2026-07-12.md`

That document diagnoses the user experience and proposes an interaction-design investigation. This document owns the business rules that must constrain that design.

### Document authority and precedence

For itinerary redesign decisions, use this order when documents disagree:

1. the company Product Thesis and What We Believe define the durable product
   purpose;
2. the founder rulings and accepted business contracts in this document define
   itinerary domain truth, authority, operation, provider, and recovery rules;
3. the itinerary interaction UX audit defines navigation, hierarchy, gesture,
   continuity, and journey behavior within those rules;
4. the Trip Itinerary surface contract defines the executable frontend and
   visual-QA acceptance boundary;
5. older Trip Plan, Trip Map, Trip Folio, Change Studio, page-spec, journey, and
   Claude Design documents describe shipped behavior or reusable reference only
   where they do not conflict with the first four authorities.

An older document retaining `source of truth` metadata does not override a newer
explicit redesign ruling. Those documents must be marked transitional or
superseded as part of this closure pass.

The intended sequence is:

```text
business-logic audit
→ founder/product rulings
→ canonical action-resolution contract
→ Claude Design interaction prototype
→ implementation plan
```

## Founder rulings: 2026-07-12

The following product decisions are accepted for the redesign:

### Trip information architecture

- Before and during a trip, **Itinerary is the default single-trip surface**, not
  a secondary workspace reached through an immersive Trip Folio.
- The current full-bleed Folio hero is a transitional shipped treatment, not the
  target design canon for the trip interior.
- Itinerary has two continuous faces: **List** for temporal truth and **Map** for
  the same truth spatially. Day, stop, candidate, and edit context persist when
  switching faces.
- Time-and-place facts belong in the itinerary. Cross-trip facts belong in a
  full-screen factual **Trip Details** index. Conversation routes to Chat with its originating
  trip context preserved.
- Stays, major transport, check-in/out, local connectors, and relevant booking
  state appear in the itinerary where they affect the day. Full stay, transport,
  cost, people, booking, and trip-setting summaries remain available through
  Trip Details.
- Post-trip begins on the destination-local day after the trip ends. A fresh
  completed-trip entry leads with the completed record until server-authored
  readiness says Memory is meaningful; the final Itinerary remains available
  and an explicitly selected face is retained for the current session. A
  cancelled trip always leads with its retained record and outstanding
  booking/cost closure work; it does not fabricate a memory state. IR-16 owns
  post-trip routing exposure.
- Before dates exist, the trip still opens through the itinerary-first shell,
  but it shows an **undated Trip Shape**—destination intent, anchors, loose
  regions, and the next useful planning action—not fabricated calendar days.
  Dated itinerary days materialize only after destination and dates are
  confirmed.
- Changing destination or dates after a dated itinerary exists is a
  consequential trip-context revision. It previews the day/timezone remap,
  protected anchors, proposals, and provider consequences and never silently
  shifts the plan.
- In a group trip, the header Chat action opens the group room; in a solo trip
  it opens the private trip-scoped Vesper thread. Stop-level **Ask Vesper** is
  always private by default, while **Discuss** opens the group composer with a
  structured attachment and never auto-sends.

### Shared-plan governance

- The organizer is the default decision owner for the shared itinerary.
- Group editing has two modes:
  - **Open:** members may make ordinary changes directly.
  - **Review:** members construct complete suggestions; the organizer decides.
- The current trip-wide **Locked** mode should not be carried into the redesign.
- Organizer edits normally apply directly. The organizer may voluntarily ask the
  group, while protected bookings and broad consequential changes require an
  explicit confirmation step.
- “Suggest to group” means organizer review by default. Voting is an explicit
  trip preference or an action-specific exception, not the default interaction
  for every shared change.
- Open/Review governs human authority over whole-group structure. It does not
  erase explicit ownership of personal or subgroup structure. A subgroup
  decision owner controls its branch content in either mode; the organizer
  controls the shared split/rejoin topology and may propose to, but not silently
  overrule, another subgroup owner.
- Governance changes apply to new resolution attempts. They do not retroactively
  apply an open proposal, erase a landed operation, or silently upgrade an
  unsent draft. Open drafts and commits re-resolve against current policy;
  submitted proposals retain an immutable creation-policy snapshot for
  authorship/audit while acceptance still revalidates current authority and
  safety. A stale proposal is rebased or withdrawn and resubmitted, never
  silently rewritten.
- V1 has exactly one itinerary organizer/decision owner even if other members
  hold administrative capabilities elsewhere. Organizer transfer is atomic,
  explicitly reassigns unresolved organizer-review tasks, and never rewrites
  historical attribution. Future co-organizer resolution requires a new policy;
  multiple admin-like roles must not be inferred as multiple decision owners.

### Personal, subgroup, and parallel plans

- A traveler may opt out of an activity without removing it for everyone.
- Personal attendance state is separate from shared block/event truth.
- The itinerary must support **parallel events**: two or more personal/subgroup
  activities may occur at the same time.
- Parallel events should remain visible in the shared trip artifact, with clear
  participant labels and a legible point where the group separates and rejoins.
- Subgroup attendance alone must not implicitly grant edit authority. A
  subgroup item needs explicit decision ownership in addition to participants.
- A branch group has an explicit topology owner—the trip organizer in v1—and
  each branch retains its own content decision owner. Creating a split,
  assigning travelers, changing branch membership, and setting the rejoin are
  one typed compound operation so the day cannot land in a half-split state.

The canonical day model is therefore not always a single sequence:

```text
shared spine
→ split into simultaneous personal/subgroup branches
→ each branch carries participants + decision owner
→ rejoin the shared spine
```

The redesign must make parallelism readable without presenting each traveler as
an entirely separate itinerary. The shared trip remains the primary artifact.

### Vesper authority

- Vesper may advise and prepare exact changes freely.
- Vesper may apply only trivial, reversible changes at a traveler's explicit
  request and only with that traveler's existing authority.
- Meaningful solo changes require confirmation.
- Shared structural changes become organizer-reviewed proposals unless an
  explicit, approved low-risk agency policy permits otherwise.
- Vesper never silently changes bookings or broadly replans a group trip.
- Vesper delegation is a **per-traveler, per-trip trust preference**, not a
  trip-wide grant of shared authority. The trip's Open/Review policy and the
  target's decision owner remain hard ceilings on that personal delegation.

### Canonical action distinctions

- **Replace plan stop** changes the itinerary entity and all derived plan/map
  truth, but does not claim that an external reservation changed.
- **Replace and rebook** is a separate protected workflow covering cancellation,
  fees, availability, confirmation, and the new booking.
- Tapping an itinerary row primarily inspects the stop. A clear **Change** action
  enters editing; the row itself should not silently become an editor.
- Swipe may be added later as a shortcut for obvious low-risk actions, never as
  the only accessible route.

### Interaction depth

- Quick sheet: Skip/attendance, simple Remove, mark attended.
- Structured sheet: Move and straightforward Add.
- Full-screen choice flow: Replace, search, and refinement.
- Full-screen review: Optimize day, broad replan, and booking consequences.

These rulings settle the product posture. The accepted object and operation
contracts later in this document now define parallel-track ordering, decision
ownership, rejoin behavior, and per-traveler attendance. Remaining work is to
implement, migrate, and validate those contracts.

## Canonical amendment: adversarial-review closure — 2026-07-13

The independent review exposed six decisions that were still ambiguous. The
following rulings are accepted and take precedence over earlier wording in this
document:

1. **Trip Shape is shared governed truth.** An undated Trip Shape is not a
   private Vesper draft once it is shown as the trip's current shape. It has a
   revision, an organizer decision owner in v1, and the same Open/Review and
   proposal rules as dated shared structure. Private traveler inputs may inform
   a suggestion but may not silently rewrite the shared shape.
2. **Whole-group scope is snapshotted, then reconciled.** A whole-group block
   records the active-member snapshot and membership revision used when it was
   created or last reconciled. Join, leave, and organizer-transfer events do not
   silently rewrite planned participation; they produce an explicit, attributed
   reconciliation that may be quiet only when it has no protected, capacity,
   cost, privacy, or branch consequence.
3. **Optimistic preconditions are discriminated by operation.** There is no
   universal `expected_day_revision`. Each operation carries the revisions of
   the truth it can invalidate: shape, trip context, day/branch, block lineage,
   proposal, and/or provider dependency. Preview and commit bind and revalidate
   the same typed precondition set.
4. **A submitted proposal is frozen in authorship, current in safety.** Its
   normalized operation, public rationale, attribution, and creation-policy
   snapshot never mutate in place. Acceptance re-evaluates current membership,
   decision ownership, trip phase, protection/provider state, and optimistic
   preconditions. A stale or newly unauthorized proposal is rebased or replaced
   by a new attributed proposal; it is never applied under obsolete permission.
5. **Plan-only Replace preserves provider binding honestly.** The successor
   becomes the chosen itinerary entity, while any unchanged reservation remains
   bound to its original provider subject and is surfaced as an unresolved
   provider continuation. The reservation must not be silently attached to the
   replacement, hidden, or described as changed. `Replace + rebook` is the only
   workflow that may transition both truths.
6. **Vesper leads within authority; the itinerary owns operational truth.**
   Vesper should decide and prepare a strong recommendation instead of dumping
   options, but it pauses at human authority, protected-provider, privacy, and
   irreversible boundaries. Group Chat is the primary shared social and
   coordination surface; Itinerary is the primary shared operational record.
   Neither surface is allowed to become a second mutation authority.

## Scope

This audit covers structural itinerary actions:

- inspect;
- add;
- move or reorder;
- replace;
- remove;
- optimize a day;
- full or scoped replan;
- undo, withdraw, revert, and recover.

It evaluates those actions against:

- solo and multi-person trips;
- organizer and member roles;
- trip editing policy;
- personal, subgroup, group, booked, live, and historical blocks;
- traveler-, Vesper-, and system-initiated changes;
- action risk and reversibility;
- group approval and voting rules;
- trip phase.

It does not redesign the interface and does not authorize implementation.

## Current business objects

### Trip settings

Current persisted trip-level controls include:

| Setting | Values | Current purpose |
|---|---|---|
| `plan_editing` | `open`, `review`, `locked` | Whether a member edits directly or proposes |
| `voting_enabled` | boolean | Whether group proposal modes can use vote/deadline automation |
| `autonomy_level` | `L1_links`, `L2_decide`, `L3_cart` | Primarily booking/execution posture, despite being shown under Vesper autonomy |

Conversation-level controls separately include:

- group agency mode: `reactive` or `proactive`;
- proactivity threshold: `low`, `medium`, or `high`;
- per-user and group-room mute/agency controls.

These settings answer different questions and should not be conflated:

- Who may edit?
- How does a group decide?
- When may Vesper speak?
- When may Vesper prepare or apply a structural change?
- How much booking execution may Vesper perform?

The current product does not expose a single clear setting for Vesper's itinerary-mutation authority.

### Human roles

Persisted trip roles are currently:

- `organizer`;
- `member`.

The frontend contains some compatibility checks for `admin`, but the backend role vocabulary is `organizer | member`.

The system also encounters non-member states that matter to interaction even though they are not trip roles:

- invited but not joined;
- viewer through a public/shared surface;
- removed member with stale local state;
- signed-out invite recipient.

### Current edit outcomes

`backend/core/edit_policy.py` defines:

```text
EditMode:
  direct
  propose
  denied

AgentCommit:
  apply
  preview
  propose
```

These are a strong foundation. The missing layer is a unified action capability that considers block scope, booking protection, phase, initiator, and action-specific risk before the UI renders.

## Current human edit resolver

The current pure resolver behaves as follows:

| Trip/actor state | Result |
|---|---|
| One member | `direct` |
| Actor is organizer | `direct` |
| Group + `open` | `direct` |
| Group + `locked` | `propose` |
| Group + `review` + actor owns personal block | `direct` |
| Group + `review` + ordinary shared block | `propose` |
| Post-trip | `denied` |

### Current strengths

- Solo trips avoid group ceremony.
- Organizers retain decisive control.
- Members are not simply denied; they can propose.
- A personal-block exception exists in the core model.
- Post-trip content is protected from structural rewriting.
- The resolver is pure and testable.

### Current ambiguities

#### `review` and `locked` are effectively the same for ordinary members

Both settings resolve a member's shared-block edit to `propose`.

Current settings copy says:

- Review: “Members suggest; you approve.”
- Locked: “Members can only suggest changes.”

Those descriptions communicate the same effective behavior. A real locked mode might mean:

- members cannot create structured proposals;
- members can only message the organizer;
- or protected blocks are fully non-proposable.

Alternatively, the product may only need Open and Review. This requires a product ruling.

#### Organizer always edits directly

The backend treats organizer authority as direct regardless of `plan_editing`. The edit-commit endpoint allows a direct editor to voluntarily downgrade to `propose`, but that preference is not consistently exposed across all frontend/menu/direct endpoint paths.

Required ruling:

- Should organizers always have an “Ask the group” option?
- Are some group-wide or identity-sensitive changes required to go to the group even when initiated by an organizer?

#### Personal-block ownership is incompletely propagated

`actor_owns_block` is honored in edit preview and edit commit when the block's participants list contains only the actor.

Several direct REST endpoints and concierge mutation paths call the resolver without block ownership, so the same personal block may be direct through one path and proposal-only through another.

Required ruling:

- Is personal/subgroup block ownership a real v1 policy or an unfinished future exception?
- How is ownership represented when `participants` is null, incomplete, or contains a subgroup?

#### Frontend posture duplicates the backend incompletely

`plan.tsx` independently derives:

- `canEditDirectly`;
- `canSuggestToGroup`;
- `isSolo`.

It does not model:

- the personal-block exception;
- action-specific booking protection;
- server-only denial reasons;
- all role vocabulary consistently;
- different risk/confirmation requirements.

The frontend should eventually consume server-authored capabilities rather than recreating the policy.

## Current agent commit resolver

The core agent grader currently behaves as follows:

```text
If human edit mode is propose:
  agent result = propose

Else if irreversible, wide-blast, or low-confidence:
  agent result = preview

Else:
  agent result = apply
```

In the concierge proposal tool:

- booked affected blocks count as irreversible;
- more than two affected blocks count as group blast;
- low-risk direct-context changes become `auto_approve`;
- consequential direct-context changes become `active_approval` used as a user confirmation gate;
- proposal-context agent changes are prevented from auto-applying;
- member delegation/consent can downgrade auto-apply to a proposal;
- voting-disabled trips reject voting modes except the special direct-preview path.

### Current strengths

- The agent does not have unlimited authority.
- Human edit authority constrains the agent.
- Booked and wide-blast edits receive more friction.
- Member consent can prevent silent auto-apply.
- Proposals carry before/after evidence.
- Low-risk direct changes can remain lightweight and reversible.

### Current ambiguities and overload

#### `active_approval` represents two different products

The same value can mean:

- a solo/direct-context confirmation preview;
- a group proposal requiring majority approval.

The UI distinguishes these using surrounding context, but the business concept is overloaded. Claude Design should not inherit `active_approval` as user language.

The canonical product concepts should be separate even if storage remains compatible:

```text
confirmation_required
group_approval_required
```

#### Agent authority is partially derived from the requesting user

Direct concierge edit tools receive a `user_id` and generally consult that user's edit mode. This is directionally correct: Vesper should not inherit organizer power when acting for a member.

The provenance needs to remain explicit:

- applied by the traveler directly;
- applied by Vesper at the traveler's request;
- proposed by a traveler through Vesper;
- proactively proposed by Vesper;
- automatically applied by Vesper under an enabled policy.

#### “Vesper autonomy” does not currently mean itinerary autonomy

`autonomy_level` is framed around booking links, recommendations, and cart/execution. Conversation agency controls when Vesper speaks. Neither setting cleanly owns whether Vesper may auto-apply a structural itinerary change.

Required ruling:

- Reuse/expand an existing setting, or add a separate itinerary agency posture such as Advise / Propose / Act?

#### Risk classification is too coarse

Current agent grading uses three booleans:

- irreversible;
- group blast;
- low confidence.

This misses important dimensions:

- price or cancellation cost;
- booking/payment ownership;
- affected participants;
- trip phase and time pressure;
- privacy-sensitive rationale;
- action type;
- magnitude of time/location change;
- whether a fixed anchor is displaced;
- whether the change is user-commanded or proactive.

## Current group decision rules

Persisted proposal modes are:

| Internal mode | Current behavior |
|---|---|
| `auto_approve` | Apply immediately; later objection may escalate |
| `lazy_consensus` | Accept at deadline if nobody rejects; rejection escalates |
| `active_approval` | Majority of eligible voters approves or rejects; no majority escalates |

Additional rules include:

- proposer is excluded from eligible-voter denominator because proposing implies consent;
- unanimous yes from all eligible members can resolve early;
- organizers control manual resolution/revert paths;
- voting modes require `voting_enabled`, except solo confirmation preview;
- missing voter identities are privacy-restricted on group surfaces.

### Open product questions

- Is lazy consensus appropriate for a dinner swap, or only for timing/low-cost changes?
- Does a change affecting two of five travelers require the whole group, affected travelers, or organizer approval?
- Should an organizer be able to override a rejection?
- What happens when the organizer is unavailable during a live trip?
- Does `voting_enabled=false` mean organizer decides, no proposals, or reaction-only feedback?
- Is majority voting desirable for a small friend trip, or does it make Vesper feel like governance software?

## Current mutation entry points

Structural itinerary truth can currently change through multiple paths:

### Human/app paths

- plan edit preview + edit commit;
- direct block PATCH;
- direct block Move endpoint;
- Add block endpoint;
- proposal accept/apply;
- optimize-route followed by multiple Move calls;
- mark happened/skipped;
- planning revision and revision undo.

### Concierge/agent paths

- `generate_plan` / planning output persistence;
- scoped or full replan;
- `propose_change`;
- direct itinerary block update/move/add tools;
- `pin_experience`;
- booking writeback to an itinerary block;
- proposal automation at a deadline;
- future dark proactive producers such as venue-disruption swaps.

### System paths

- booking confirmation/handoff state;
- feasibility repair during plan generation;
- event-state transitions;
- proposal apply/revert;
- plan-version restoration.

This breadth makes a single capability gateway important. A visual redesign cannot assume all structural changes originate from the itinerary screen.

## Deep implementation audit: redesign blockers

The first pass established the intended policy model. A second pass traced the
actual write paths through the current backend and mobile working trees. The
result is more serious than “the controls are hard to find”: several canonical
verbs do not yet perform the business operation their labels promise, and some
permission and history guarantees can be bypassed.

This means the redesign is ready for exploratory interaction work, but it is
**not ready to be handed to Claude Design as an implementation-faithful canon**.
Design can help compare navigation patterns, information hierarchy, and gesture
models. It should not freeze final action copy, confirmation flows, or group
states until the P0 rulings below are settled.

### Prioritized verified findings

| Priority | Finding | Why it blocks a truthful redesign |
|---|---|---|
| P0 | Replacement selection commits only `new_title`, not the selected venue | “Replace” leaves the old entity, map location, provenance, and booking attachment underneath the new name |
| P0 | `participants` can be PATCHed without the structural edit gate | A review-mode member can make a shared block appear personal, then gain the personal-block direct-edit exception |
| P0 | Full/scoped replan and `pin_experience` do not use the edit resolver | A member or Vesper path can structurally replace/add plan content outside the group policy used by the itinerary UI |
| P0 — direct path closed 2026-07-13 | Remove advertised Undo, but the Undo route rejected cancelled blocks | Direct future-unbooked Remove now commits inverse evidence atomically and restores cancelled blocks through scoped, stale-safe, idempotent Undo; proposal/provider destructive paths remain open |
| P0 | Optimize applies multiple concurrent append-style Move requests | The operation can partially apply, race, or land in an order different from the preview while immediately showing success |
| P0 | Shared `event_state` is writable by any member | “I skipped this” and “the group skipped this” are the same database fact; solo/subgroup attendance is not representable |
| P1 | “Swap” and “Move” have conflicting meanings across contracts | The UI, preview endpoint, commit endpoint, and planner cannot share one mental model or one diff object |
| P1 | Human Add has no proposal-capable commit spine | Review-mode members can see Add affordances and choose a day, then receive a direct-endpoint failure instead of a structured suggestion |
| P1 | Proposal creation/resolution behavior varies by producer | Human edit proposals, chat proposals, auto-approved proposals, and confirmation previews use different creation, voting, deadline, and dedup rules |
| P1 | Destination-local phase truth is not consistently enforced | A focused edit-policy suite currently fails its Honolulu last-local-day test |
| P1 | Preview, mutation, ledger, and receipt are not one atomic contract | A mutation can land without its promised receipt/Undo evidence; proposal apply uses compensation rather than database atomicity |
| P1 | Map remains a read/launch surface | It cannot yet support the “Plan and Map are two editors over one plan” promise in the existing north-star spec |

### Canonical verb audit

#### Replace is currently a title rename, not an entity replacement

The Alternatives endpoint returns a meaningful candidate:

```text
venue_id
name
venue_type / cuisine
price estimate and cost delta
distance
neighborhood
fit line
```

The mobile picker passes only the candidate's `name` into
`POST /plan/edit-commit`. `PlanEditCommitRequest` has only `new_title` for a
swap, and the direct apply updates only `itinerary_blocks.title`.

Consequences:

- the old `venue_id` remains attached;
- Plan can show the new name while Map and venue detail still point to the old place;
- old price, location, hours, and provenance remain authoritative;
- the action cannot truthfully record which candidate was chosen;
- a confirmed booking remains attached to a block now bearing a different name.

The current booked-swap screen says that swapping means cancelling the current
reservation and warns about fees. The commit neither cancels nor replaces the
booking; it renames the block and leaves the booking reference in place. This is
a trust-critical mismatch.

There are also two incompatible internal meanings of `swap`:

- edit preview: exchange the times/positions of two itinerary blocks using
  `swap_with_block_id`;
- edit commit from Alternatives: replace one block's displayed title using
  `new_title`.

The agent proposal apply path has a third, more complete behavior: a `swap`
proposal may update `venue_id` from its first alternative option. The human UI
proposal path stages `proposal_type="modify"` and again changes only the title.

Required canonical split:

```text
REPLACE_ENTITY(target_block, chosen_entity)
SWAP_POSITIONS(first_block, second_block)
```

They must not share one ambiguous `swap` payload.

#### Move changes time but does not reliably change position

Same-day edit commit calls `update_block` with new timestamps and leaves
`sort_order` unchanged. The plan read model orders blocks by `sort_order`, so a
stop moved from evening to morning can remain visually below later activities.

Cross-day edit commit uses `move_block` without a relative target and appends to
the destination day. The public REST Move request has no `after_block_id` or
target index even though the lower-level database helper and concierge tool
already support `after_block_id`.

The product needs separate, composable move dimensions:

```text
target day
target time window
target relative position
```

The server must decide or validate all three. A time change must either derive a
stable chronological order or explicitly preserve a user-authored non-time
order; it cannot leave that relationship accidental.

#### Add is not one cross-surface operation

Current Add behavior depends on where the traveler starts:

- a direct editor can add a gap suggestion, custom activity, free-time block, or
  venue;
- a review-mode member has no structured Add-to-proposal path;
- some gap affordances still open for a non-direct member, then the direct Add
  endpoint returns 403;
- Venue detail uses the direct Add endpoint and therefore fails for the same
  member after they select a trip and day;
- Experience detail uses `pin_experience`, which bypasses edit policy and can
  succeed in that same trip.

The result is especially confusing because two visually equivalent “Add to
plan” actions have opposite permission outcomes.

Add also always appends. It accepts timestamps but does not validate that their
calendar date matches the selected itinerary day, that they lie within the trip,
or that they do not overlap another block. Gap suggestions are context-aware,
but the mutation boundary itself does not preserve those invariants.

#### Remove and Skip represent different facts but are not consistently separated

The north-star spec distinguishes:

- future block: remove it from the plan;
- past/live block: mark that it did not happen and retain the record.

At audit time, structural remove soft-cancelled the block while
`/itinerary/blocks/{id}/undo` loaded only active blocks. The cancelled block was
rejected before its manual-edit event could be reversed. Human direct paths
could also remove happened/skipped blocks while the concierge precondition
layer rejected those terminal event states.

Resolved for the direct path on 2026-07-13: Plan edit commit, the legacy block
PATCH, and the concierge update tool now converge on one transactional Remove
primitive. It refuses historical blocks and protected booking states, writes the
exact before/after status plus a privacy-safe post-remove row fingerprint in the
same transaction, and keeps the cancelled block addressable to Undo. Remove cannot
be combined with hidden field updates. Proposal-applied Remove remains on the
proposal fork/revert contract and is not covered by this direct-path proof.

#### Optimize is neither atomic nor ordered as advertised

The preview computes one day-level route. Apply loops over every suggestion with
`forEach` and fires multiple `moveBlock` mutations immediately; despite the code
comment, these are not awaited sequentially.

Each REST Move independently:

- rechecks permission;
- calculates an append position;
- commits its own transaction;
- writes its own history event;
- can fail independently.

The sheet closes and shows “Applied · Day N reordered” without waiting for all
requests. Multiple requests can race on the same destination order. The user has
no one-step Undo for the action they actually approved.

Optimize should become one server-side operation with:

- a preview revision/token;
- expected plan head/version;
- an ordered list of block placements;
- one permission/risk decision;
- one atomic commit;
- one receipt and one Undo.

### Group and participation model audit

#### `participants` currently mixes scope, display, and authority

Raw itinerary blocks store participant user IDs. The Plan read model converts
those IDs into display-name strings before returning `PlanBlock.participants`.
This makes rows readable, but the field no longer has stable identity semantics.
For example, the transport filter compares those name strings with traveler
IDs, so subgroup filtering cannot match reliably.

More importantly, `participants` influences authority: exactly `[actor_id]`
grants the personal-block direct-edit exception in Review mode. But the generic
block PATCH route does not classify `participants` as structural and does not
validate that supplied IDs are current trip members. A member can therefore:

```text
PATCH participants = [self]
→ block is now treated as actor-owned
→ edit commit resolves DIRECT
```

This is both a permission defect and evidence that one field cannot safely own
all of these concepts:

- who plans to attend;
- who owns the decision;
- who may edit the block;
- which names to render.

Recommended conceptual split:

```text
attendance_scope: whole_group | subgroup | personal
participant_ids: stable member IDs
decision_owner_ids: who may decide for this item
participant_labels: read-only presentation data
```

#### Event state is global, but real group attendance is individual

`event_state` (`planned`, `happened`, `skipped`) lives once on the shared block.
It is intentionally outside the structural edit gate, and any member may mark a
block happened/skipped or reset it.

That works only if the entire group always moves together. It cannot express:

- one traveler skipped while four attended;
- a subgroup attended;
- the organizer marked their own completion only;
- Vesper inferred presence for one traveler;
- a traveler corrected their memory without rewriting everyone else's trip.

This affects more than display. Happened/skipped state drives conflict
suppression, memory/story construction, and place-affinity signals. The redesign
needs an explicit ruling between:

1. group event truth plus per-traveler attendance; or
2. per-traveler event truth with a derived group summary.

The current single field should not be presented as “your” completion state on
a group trip without that ruling.

#### Notes are described as personal but persisted as shared block state

The generic PATCH gate groups `notes` with personal annotations, yet notes live
on the shared itinerary block and are returned to every plan viewer. Product
must distinguish shared trip notes from private traveler notes before the edit
surface offers a generic note action.

### Permission and agent-authority audit

#### The personal-block exception is currently privilege-bearing mutable data

Until the participants issue above is fixed, personal ownership must not grant
authority. Ownership should be server-derived from a separately governed
assignment/attendance operation, not accepted as an unguarded block patch.

#### `denied` is not handled as a first-class result everywhere

Some paths explicitly reject `EditMode.denied`; others only test whether the
mode equals `propose`, allowing `denied` to fall through as if it were direct.
Examples include concierge direct-edit checks and some undo/revision paths.
Separate endpoint-local date checks hide part of this problem but use different
time truth.

Every caller should exhaustively handle:

```text
direct
propose
denied
```

An unknown or failed resolver result should never become direct authority.

#### Replan is a larger bypass than any individual block tool

The `generate_plan` handler can persist a generated or preservation-safe replan,
create a new current itinerary version, and withdraw open proposals. It receives
the requesting user for context and telemetry but does not resolve that user's
edit authority before persistence.

A member whose block edit would become a proposal can therefore ask Vesper for a
day or full replan through a path capable of changing far more of the itinerary.
The broadest mutation currently has a weaker authority boundary than a single
Move.

Required ruling:

- initial generation authority;
- scoped replan authority;
- full replan authority;
- whether the result is a draft, confirmation preview, proposal, or applied
  version for each actor/setting/phase.

#### Agent policy failures currently fail open in direct tools

The concierge direct-edit helper returns “allowed” when
`resolve_edit_mode_for_trip` raises. Downstream database constraints protect
some state transitions but do not reconstruct group authority. The safe fallback
for structural agent actions is `PROPOSE` or `DENIED`, not direct apply.

#### `pin_experience` has no human principal

The handler receives trip context but not the requesting user, so it cannot
evaluate role, personal scope, or edit policy. Provenance and duplicate checks
prove that the selected experience is real; they do not prove permission to
write it.

### Proposal and decision audit

#### The “one creation path” invariant is currently false

The system charter requires chat and UI proposals to use
`build_and_persist_proposal`. Human edit commit does. The concierge
`propose_change` handler performs its own privacy/quality logic and then calls
`create_change_proposal` directly.

Consequences include drift in:

- superseding prior open proposals on the same block;
- redaction audit behavior;
- creation semantics and future invariant checks;
- race/dedup behavior.

The two paths should share one durable builder after their producer-specific
copy validation.

#### Human edit proposals have no explicit decision policy

`_stage_proposal` does not set `approval_mode` or a deadline. Automation treats
a missing mode like lazy consensus, but deadline sweeps only see proposals with
a deadline. Therefore these suggestions generally wait for organizer resolution
unless a narrow early-consensus rule fires.

The group-size behavior is surprising:

- proposer cannot vote;
- in a two-person trip there is only one eligible voter;
- early unanimous acceptance requires at least two approve votes;
- no deadline exists to settle the suggestion.

So a two-person member suggestion cannot auto-resolve through voting even when
the other traveler approves; an organizer must manually resolve it. If that is
the intended Review model, the UI should say “Send to organizer,” not imply a
general group vote.

#### `auto_approve` is apply-now, not object-later

Auto-approved proposals are immediately moved to `accepted` and applied. Voting
on a resolved proposal returns a conflict, so the documented idea that a later
rejection can escalate is not an available interaction. Recovery is Revert, and
only organizers can perform it.

Product should choose honest language:

```text
apply now + organizer can revert
```

or implement a real objection window before application.

#### Direct-context confirmation and group voting share storage but not authority

`active_approval` is used both for a direct actor's high-risk confirmation and
for majority group approval. This becomes especially ambiguous for an ordinary
member on an Open trip: they have direct human authority, but an agent-created
high-risk “confirmation” is stored as a proposal whose manual resolve endpoint
is organizer-only and whose proposer cannot vote.

Confirmation needs its own actor-scoped lifecycle rather than relying on a group
proposal state with contextual UI interpretation.

#### Accepted and applied are separate states

The current implementation correctly records `apply_status="failed"` when an
accepted proposal cannot mutate the itinerary, but the proposal remains
accepted. The redesign needs an explicit recovery state such as “Approved, not
applied — organizer action needed,” rather than treating accepted as plan truth.

### Concurrency, history, and recovery audit

#### The preview token is an idempotency key, not a bound preview

Edit commit accepts any non-empty token and does not load or verify the preview
payload it supposedly consumes. Menu actions mint local tokens without calling
preview. A caller can also change the action parameters after preview while
reusing its token.

That may be acceptable as retry idempotency, but it should not be described as a
proof that the exact before/after was reviewed. A real preview contract needs a
server-stored or signed action payload/hash plus an expected plan head.

#### Optimistic concurrency is optional and path-specific

`expected_updated_at` is optional at the API level. Current Change Studio flows
usually pass it, but legacy Add/Move/PATCH, agent tools, proposal apply, and
multi-block optimize do not share one expected-version contract.

There are also two concurrency levels:

- block revision: did this block change?
- plan head/version: did another action change ordering, dependencies, or the
  surrounding day?

A correct reorder, optimize, or broad replan needs plan/day-level concurrency,
not only one block timestamp.

#### Mutation, ledger, and receipt are not atomic

Ordinary direct `update_block`/`move_block` still commit the itinerary mutation,
then emit the plan event and invalidate read models. Edit commit writes its
visible action receipt after the mutation as best effort. A ledger or receipt
failure therefore does not roll back those ordinary changes.

Direct Remove is now the deliberate exception: the cancelled row and its exact
inverse evidence share one database transaction, and the restoration and its
one-time `undo_of` marker share another. A failed ledger write rolls back the
corresponding state mutation. User-facing receipt projection remains best effort
and is not the recovery source of truth.

Proposal apply forks the itinerary, performs per-block transactions, and uses a
best-effort compensation routine if a later block fails. This is a thoughtful
saga, but it is not the all-or-nothing database transaction promised by the
system charter; compensation can itself fail.

Product can accept best-effort receipts only if the UI does not promise Undo
until durable undo evidence exists. The stronger preferred invariant is:

```text
mutation + canonical history event commit together
→ projections/notifications may remain best effort
```

#### Direct Undo ownership is hardened; Move dependencies remain incomplete

As audited, `undo_last_block_edit` selected the latest un-undone manual event
without requester ownership and let repeated calls walk backward through older
history. It could restore state before persisting its marker.

The 2026-07-13 implementation now locks the current-head block and latest manual
event in one transaction, authorizes the initiating actor or organizer for
shared structure and only the owner for a personal block, verifies the current
field values, and makes retry return current truth without traversing history.
For Remove specifically, any later row update or itinerary-head revision makes
one-tap Undo unavailable and requires reviewed Revert.

That proof uses the legacy personal-versus-shared model. It does not yet prove
the target distinction between subgroup content ownership and organizer-owned
split/rejoin topology.

Move Undo can still restore sibling sort orders from a snapshot without proving
that each sibling is unchanged. That remaining dependency should be surfaced as
a conflicted Revert rather than one-tap Undo before Move recovery is called
fully proven.

### Implementation closure: direct future-unbooked Remove recovery (2026-07-13)

The proved boundary is intentionally narrow and explicit:

- all current direct entrances use `remove_block_with_undo`;
- Remove and immutable inverse evidence commit or roll back together;
- Undo restoration and its one-time marker commit or roll back together;
- cancelled remains terminal to ordinary PATCH/update callers; only the proven
  recovery validator may restore `tentative` or `confirmed`;
- happened/skipped blocks and held, held-for-payment, handed-off, confirmed,
  booked, or in-progress booking dependencies cannot enter direct Remove;
- a privacy-safe full-row fingerprint catches later writes even when a legacy
  writer misses `updated_at`; any row change or new itinerary revision demotes
  Undo to reviewed Revert;
- current legacy whole-group recovery belongs to the initiating actor or
  organizer; a personal block belongs only to its owner. Target subgroup-owner
  recovery remains implementation-required with the canonical scope migration;
- sequential and concurrent retries are idempotent and create one inverse
  marker.

Postgres fault injection proves both rollback directions: failure to persist the
Remove evidence leaves the block active, and failure to persist the Undo marker
leaves the block cancelled. Route and concierge tests prove that cancelled rows
reach this recovery path and legacy direct entrances cannot bypass it.

### Time, phase, and data-invariant audit

#### Destination-local post-trip enforcement currently fails a focused test

The Plan read model derives today/phase in the destination timezone. The core
edit resolver falls back to server-local `date.today()`, and several REST routes
repeat the same comparison independently.

Focused audit result on 2026-07-12:

```text
98 relevant backend tests passed
1 failed:
TestPostTripEditGuardDestinationTimezone::
test_west_of_utc_trip_still_editable_on_its_last_local_day
```

The failing scenario is 00:05 UTC on July 11 while Honolulu is still on the
trip's July 10 final day. The resolver denies editing too early.

#### Proposed reschedule time loses timezone semantics

Human edit proposals serialize only `new_time` as `HH:MM`. Proposal apply
normalizes the existing timestamp to UTC, then replaces its UTC hour with that
clock value. A destination-local 19:00 proposal can therefore apply at a
different local time in a non-UTC destination even though the direct path uses
the full offset-aware datetime.

Proposal impact must store a full zoned/offset datetime or a local date + local
time + destination timezone, not a context-free clock string.

#### Protected booking state is not one canonical predicate

Different paths treat different sets as protected:

- remove guards: confirmed, booked, in-progress, handed-off;
- Undo-add guard additionally includes held-for-payment;
- booked Swap UI gates only confirmed/booked;
- agent risk grading treats any non-null booking reference as irreversible.

Before design names a state “booked,” “held,” or “safe to change,” Booking and
Itinerary need one protected-commitment classifier with action-specific
consequences.

### Cross-surface interaction audit

The current surfaces do not yet implement “two doors, one room”:

| Surface | Current structural behavior |
|---|---|
| Plan / Change Studio | Richest edit path; direct users get Replace/Move/Remove, proposal-only users mainly get a chat handoff plus a generated recommendation path |
| Gaps / empty day | Direct Add; some gap entry points remain visible to members who cannot commit it |
| Venue detail / Discover | Direct Add to selected day; no group-proposal fallback |
| Experience detail | Pin path can bypass group edit policy |
| Map | Directions, Ask, and Open; no reorder, replace, add, or optimize commit surface |
| Chat | Can propose, directly edit, pin, or broadly replan through different authority contracts |
| Now Mode | Move/remove suggestions reuse Change Studio, but live event-state and group-participation semantics remain global |

The redesign therefore defines a portable action object and portable capability
response before applying the accepted interaction grammar: inspection/quick
sheets, explicit Change, handle-only reorder drag, no structural row swipe in
v1, and full-screen consequential choice/review. Those are presentations over
the same operation, not separate business flows.

### Additional product cases not yet represented

- A traveler opts out of one group activity without removing it for everyone.
- Two subgroups do different things at the same time and later reunite.
- A traveler joins after blocks were assigned, or leaves after proposing/editing.
- Multiple organizers disagree or concurrently resolve/revert.
- A booking payer differs from the organizer and the block's attendees.
- A replacement changes price, cancellation liability, neighborhood, travel
  chain, and accessibility fit at once.
- A venue closes while one member is offline and the group is already en route.
- A user wants to correct post-trip factual history without reopening the plan.
- A plan has untimed blocks whose authored order should not be chronological.
- A provider cancellation changes booking truth before itinerary truth updates.
- The app retries an action after reconnecting after the plan head advanced.
- Vesper's rationale uses private evidence while the exact operational change is
  group-visible.

These should become business scenarios and contract tests before the redesign is
declared complete.

### Documentation and validation drift

The existing canon explains why the current UI can feel like a jumble even
though many individual pieces look considered.

The north-star itinerary-editing spec defines a strong shared model—one
`EditIntent`, one `CandidateSet`, one resolver, Plan and Map as twin editors—but
also says only Phase 0 is committed. The codebase now contains partial work from
later phases (permissions, Move/Add, conflicts, Optimize, booked gates) without
the shared operation object that was supposed to keep them coherent. The result
is later-phase surface area attached to Phase-0 mutation primitives.

The workspace system charters currently state invariants that the implementation
does not satisfy:

- only Change Studio/edit commit writes itinerary blocks;
- every accepted change has a visible reversible receipt;
- mutation and ledger rollback atomically;
- chat and UI proposals use one creation path;
- Plan and Map remain coherent after every change.

Those are still the right target invariants, but they should be labeled target
rather than current truth until contract tests prove them.

The trip-itinerary visual surface contract focuses on density, hierarchy,
screenshots, and visual states. It does not require behavioral evidence for the
exact action lifecycle. A visually passing Change Studio screenshot can
therefore coexist with a title-only replacement, failed Remove Undo, or an Add
permission dead end.

The current automated coverage also proves components more strongly than
cross-surface truth:

- direct-swap tests explicitly assert that only the title updates;
- direct Remove → Undo now has focused route, authority, stale/revision,
  concurrency, idempotency, protected-dependency, and Postgres fault-injection
  coverage; proposal/provider destructive recovery does not yet have equivalent
  proof;
- Optimize component tests do not prove all network mutations complete in the
  previewed order;
- proposal and edit unit tests do not prove a Venue-detail Add, Experience pin,
  Plan Add, Map view, and Chat action resolve authority identically;
- system charters still mark on-device generation, mock walk, live group walk,
  and Journey-06 mutation parity as unvalidated.

The redesigned feature needs a behavioral contract alongside the visual canon.
For each verb, acceptance should prove:

```text
same chosen operation
same capability outcome
same persisted entity/time/order truth
same attribution
same Plan/Map/Home/Chat projection
working recovery
```

## Accepted canonical itinerary object model

The redesign must stop using one block row and a nullable `participants` array
as the model for schedule, attendance, ownership, authority, booking protection,
and history. Those are independent axes.

### 0. Undated Trip Shape precedes dated itinerary truth

An itinerary-first trip does not imply invented calendar precision. Before both
destination and dates are confirmed, the trip interior renders an undated
planning object:

```ts
interface TripShape {
  destination_intent?: PlaceRef;
  duration_nights?: number;
  anchors: TripShapeAnchor[];
  loose_regions: TripShapeRegion[];
  source_revision: string;
  decision_owner_id: UserId;
  membership_revision?: string;
}
```

Trip Shape may express “arrival,” “one food-focused day,” “keep an afternoon
open,” or a protected known booking. It does not emit `ItineraryDay` or
fabricate dates, but shared-shape revisions do enter structural operation
history. In v1 the organizer owns the shared shape; Open/Review determines
whether another member applies or proposes a revision. Once destination and
dates are confirmed, one attributed materialization operation turns the
accepted shape into dated itinerary days. Later destination or date changes use
a consequential `replan` operation with explicit context remapping and provider
consequences.

### 1. Trip governance

```ts
interface TripItineraryGovernance {
  editing_mode: 'open' | 'review';
  organizer_id: UserId;
  voting_enabled: boolean;
}

interface TravelerItineraryDelegation {
  trip_id: TripId;
  user_id: UserId;
  itinerary_agency: 'advise' | 'propose' | 'act';
}
```

- `locked` is retired. Existing `locked` trips migrate behaviorally to `review`.
- `open` lets trip members make ordinary shared changes directly.
- `review` lets members construct exact shared changes but routes them to the
  organizer without changing current plan truth.
- Voting is a proposal-resolution mechanism, not an editing mode.
- Vesper agency is per traveler and trip. It never grants more authority than
  the governing human principal, trip editing policy, or target decision owner.
- A governance change affects future resolution attempts. Submitted proposals
  retain their recorded creation-policy snapshot, while acceptance still
  revalidates current authority and safety; unsent drafts re-resolve before
  commit.

### 2. Day structure is a graph, not always one list

```ts
type ItineraryNode = ItineraryBlock | ItineraryBranchGroup;

interface ItineraryDay {
  id: DayId;
  date: LocalDate;
  nodes: ItineraryNode[];
  revision: string;
}

interface ItineraryBranchGroup {
  id: BranchGroupId;
  branch_ids: BranchId[];
  topology_owner_id: UserId;
  starts_after_block_id?: BlockId;
  rejoins_before_block_id?: BlockId;
}

interface ItineraryBranch {
  id: BranchId;
  label?: string;
  block_ids: BlockId[];
  planned_participant_ids: UserId[];
}
```

The ordinary day remains a shared ordered spine. A branch group is an explicit
node on that spine containing simultaneous ordered branches. It is not inferred
merely because two timestamps overlap.

Branch invariants:

- every branch has at least one block and one planned participant;
- a traveler cannot be planned into two branches whose time windows overlap;
- each branch block still carries its own scope and decision owner;
- the organizer owns v1 split/rejoin topology; a branch decision owner controls
  content within that branch;
- the rejoin is optional only when the split ends the day;
- branches return to one shared spine immediately after the rejoin;
- private reasons are never stored in group-visible branch labels or notes.
- creating or changing a split, branch membership, and rejoin commits as one
  compound operation; it cannot leave partial branch topology.

### 3. Block scope, role, and phase are separate axes

```ts
type ParticipationScope = 'personal' | 'subgroup' | 'whole_group';
type StructuralRole = 'ordinary' | 'anchor' | 'soft_suggestion';
type TemporalPosture = 'future' | 'live' | 'historical'; // derived

interface ItineraryBlockGovernance {
  scope: ParticipationScope;
  planned_participant_ids: UserId[];
  decision_owner_id: UserId;
  structural_role: StructuralRole;
  membership_revision?: string;
}
```

- **Personal** means exactly one planned participant, who is also the decision
  owner.
- **Subgroup** means an explicit proper subset of active trip members and an
  explicit decision owner. Attendance alone never grants edit authority.
- **Whole group** means planned participants are snapshotted from active trip
  membership at creation or reconciliation; the organizer is the v1 decision
  owner. Later membership changes create an explicit reconciliation rather than
  silently changing the block.
- **Anchor** describes operational importance—stay, transport, ticket, fixed
  reservation—not who participates.
- **Live/historical** is derived from destination-local time and occurrence
  truth; it is not participation scope.

Compatibility ruling: current `participants = null` means **whole group**, as
the existing table and API already document. New canonical reads must emit an
explicit scope. An empty participant array is invalid. New writes may not use a
participant list to imply ownership.

For subgroup blocks, the UI may recommend the creator as decision owner, but the
write must carry the choice explicitly. Legacy subgroup blocks without one fall
back to the trip organizer until migrated.

### 4. Plan truth, attendance, and actual occurrence are independent

```ts
interface BlockTruth {
  commitment_state: CommitmentState;
  occurrence_state: 'planned' | 'happened' | 'did_not_happen';
}

interface TravelerParticipation {
  block_id: BlockId;
  user_id: UserId;
  intention: 'attending' | 'not_attending' | 'undecided';
  actual: 'unknown' | 'attended' | 'did_not_attend';
}
```

- Opting out updates only the traveler's participation; it does not skip,
  cancel, move, or remove the shared block.
- A shared event can happen while one traveler does not attend.
- `did_not_happen` is block truth; `did_not_attend` is personal truth.
- A personal block can be cancelled without changing another branch.
- Group-visible projections show workable participation, never private reasons.

The current block-wide `event_state='skipped'` cannot represent this distinction.
It remains a compatibility field until occurrence and per-traveler participation
are first class.

### 5. Protection and provider control are first-class

```ts
interface ProtectedDependency {
  type: 'reservation' | 'ticket' | 'stay' | 'transport' | 'payment';
  provider_state: 'held' | 'confirmed' | 'paid' | 'cancelled' | 'unknown';
  changeability: 'flexible' | 'fee' | 'nonrefundable' | 'external_only' | 'unknown';
  controller_user_id?: UserId;
  provider_ref?: string;
}
```

- Structural role `anchor` does not by itself prove a provider booking.
- Provider authority is separate from itinerary decision authority. The trip
  organizer may control plan truth without controlling another traveler's
  provider account or ticket.
- Unknown provider state is treated as consequential; the product must not imply
  cancellation, rebooking, or refund.
- **Replace** changes plan truth only. **Replace + rebook** is a protected
  continuation with provider reconciliation and separate receipts.

### 6. Notes and rationale are typed by visibility

```ts
type ItineraryAnnotation =
  | { visibility: 'trip'; text: string }
  | { visibility: 'personal'; owner_id: UserId; text: string }
  | { visibility: 'vesper_private'; owner_id: UserId; text: string };
```

The current shared `notes` field may continue as the `trip` annotation during
migration. Personal or private Vesper reasoning must never be written into it.

### 7. Actor, initiator, and human principal are distinct

```ts
interface ActionAttribution {
  initiator: 'human' | 'vesper' | 'system' | 'provider';
  human_principal_id?: UserId;
  channel: 'itinerary' | 'map' | 'discover' | 'chat' | 'background' | 'provider';
  requested_by_user_id?: UserId;
}
```

- A human action has that human as principal.
- User-commanded Vesper acts under the requesting human's authority.
- Proactive Vesper with no human principal may create only a soft suggestion or
  an organizer-ready proposal; it may not mutate structural trip truth.
- System/provider actors may reconcile externally proven factual state. They may
  not use that permission to replan the itinerary.
- If principal or authority resolution fails, mutation fails closed. Agent-tool
  availability is not a reason to bypass policy.

### Current-to-canonical mapping

| Current field/concept | Canonical destination |
|---|---|
| `participants = null` | `scope=whole_group`; planned participants derived from active trip membership |
| `participants = [one]` | `scope=personal`; explicit decision owner; separate attendance |
| `participants = [many]` | `scope=subgroup`; explicit decision owner; separate attendance |
| block `event_state` | block occurrence compatibility field; no longer personal attendance |
| `status` / `commitment_state` | block plan/commitment truth |
| `booking_ref` / `booking_state` | normalized protected dependencies plus provider state |
| `actor_type` | durable action attribution; never block authority |
| `sort_order` plus timestamp overlap | shared spine order; explicit branch group for intentional parallelism |
| `plan_editing=locked` | migrate to `review` |

## Accepted canonical itinerary operation

Every entry point constructs the same typed operation before policy resolution:

```ts
interface ItineraryOperation {
  id: string;
  type:
    | 'materialize_shape'
    | 'add' | 'move' | 'reorder' | 'replace' | 'remove'
    | 'set_attendance' | 'mark_occurrence'
    | 'create_parallel_plan' | 'update_parallel_plan'
    | 'optimize_day' | 'replan';
  target: OperationTarget;
  payload: OperationPayload;
  attribution: ActionAttribution;
  precondition: OperationPrecondition;
  provider_intent?: 'plan_only' | 'plan_and_provider';
}

type OperationPrecondition =
  | { kind: 'shape'; expected_shape_revision: string }
  | { kind: 'trip_context'; expected_trip_revision: string; expected_itinerary_head?: string }
  | { kind: 'day'; day_id: DayId; expected_day_revision: string }
  | { kind: 'branch'; branch_group_id: BranchGroupId; expected_branch_revision: string; expected_day_revision: string }
  | { kind: 'block'; subject_lineage_id: string; expected_block_revision: string; expected_day_revision?: string }
  | { kind: 'proposal'; proposal_id: string; expected_proposal_revision: string; operation: OperationPrecondition }
  | { kind: 'provider'; dependency_id: string; expected_provider_revision: string; operation: OperationPrecondition }
  | { kind: 'compound'; all: OperationPrecondition[] };
```

- `replace` carries chosen entity identity, not only a new title.
- `materialize_shape` turns one accepted undated shape revision into the first
  dated itinerary and preserves known anchors/provenance.
- `move` carries day, relative order, and time semantics together.
- `add` carries placement, participant scope, and decision owner.
- `remove` never doubles as personal Skip/Opt out.
- `create_parallel_plan` atomically carries split position, branch blocks,
  planned participants, branch decision owners, topology owner, and rejoin.
- `update_parallel_plan` atomically changes branch membership/content or rejoin
  while preserving the no-overlap and ownership invariants. A traveler moving
  from the shared event into a branch updates their attendance and branch
  membership in the same operation.
- `optimize_day` and `replan` contain ordered child operations and apply
  atomically or not at all.
- A preview is bound to the exact normalized operation and its discriminated
  precondition set.

## Accepted canonical action resolver

### Inputs and outputs

```text
resolve_itinerary_action(
  governance,
  operation,
  principal_membership,
  target_governance,
  trip_phase,
  affected_people,
  protected_dependencies,
  computed_risk,
  user_preference
)
```

```text
DIRECT
  may apply now; show landed attribution and Undo when safely reversible

CONFIRM
  principal has authority, but must review the named consequence before apply

PROPOSE
  exact operation goes to the named decision owner/policy; no mutation yet

DENIED
  operation cannot be performed; return reason and safe next action
```

`CONFIRM` describes the semantic final review; it does not require an extra
modal after an editor that already presents the full consequence clearly.

The resolver additionally returns:

```ts
interface ActionResolution {
  outcome: 'direct' | 'confirm' | 'propose' | 'denied';
  reason_code: string;
  decision_owner_id?: UserId;
  proposal_policy?: 'organizer_review' | 'affected_member_vote';
  confirmation_reasons: string[];
  protected_dependencies: ProtectedDependency[];
  allowed_alternatives: string[];
  predicted_recovery: 'undo' | 'withdraw' | 'review_revert' | 'provider_action' | 'new_change' | 'none';
  can_voluntarily_propose: boolean;
}
```

### Resolution order

1. Validate the typed operation, target provenance, and expected revision.
2. Authenticate the human principal and current trip membership.
3. Enforce hard temporal/state barriers: historical structural rewrites,
   in-progress immutable anchors, invalid branch membership, or foreign targets.
4. Resolve scope authority from decision ownership and Open/Review policy.
5. Resolve provider authority independently from plan authority.
6. Compute affected people, privacy posture, blast radius, and risk from data.
7. Apply agent-agency limits when the initiator is Vesper/system/provider.
8. Return the strongest required posture: hard barrier → `DENIED`; missing shared
   decision authority → `PROPOSE`; authorized consequential action → `CONFIRM`;
   otherwise → `DIRECT`.
9. A directly authorized actor may voluntarily downgrade `DIRECT` or `CONFIRM`
   into `PROPOSE`; preference can never upgrade authority.

A proposed protected operation stores its future confirmation requirement. When
the organizer accepts it, provider consequences are still confirmed before the
plan claims the operation applied.

### Computed risk dimensions

Risk is deterministic policy input assembled from domain evidence, not a label
chosen by a UI or language model. The resolver considers:

- reversibility and whether durable recovery exists;
- participation scope and number of affected travelers;
- material time, route, day, and downstream-order changes;
- destructive removal or broad child-operation count;
- anchor and protected-provider dependencies;
- cost, fee, refund, and availability uncertainty;
- live/in-progress or historical posture;
- privacy-sensitive rationale or audience;
- Vesper confidence and whether a human explicitly requested the exact action.

These dimensions collapse to `trivial`, `low`, `moderate`, `high`, or
`protected` for policy and analytics. `protected` is additive: a simple-looking
Move can still require provider confirmation.

### Scope-authority matrix

| Target | Personal owner | Organizer | Open member | Review member | Non-member |
|---|---|---|---|---|---|
| Own attendance | Direct | Only own attendance direct | Only own attendance direct | Only own attendance direct | Denied |
| Another traveler's attendance | Denied/request them | Denied/request them | Denied/request them | Denied/request them | Denied |
| Personal block | Direct/Confirm by risk | Propose to owner unless organizer is owner | Propose to owner | Propose to owner | Denied |
| Subgroup block: decision owner | Direct/Confirm | Direct/Confirm | Direct/Confirm if this member is owner | Direct/Confirm if this member is owner | Denied |
| Subgroup block: other member | — | Propose to owner unless organizer is owner | Propose to named owner | Propose to named owner | Denied |
| Parallel split/rejoin topology | — | Direct/Confirm | Propose to organizer | Propose to organizer | Denied |
| Whole-group block | — | Direct/Confirm | Direct/Confirm for ordinary edits | Propose to organizer | Denied |
| Provider booking | Controller only | Only if organizer is controller | Controller only | Controller only | Denied |

The organizer retains structural responsibility for whole-group truth and the
shared split/rejoin topology, but explicit subgroup decision ownership remains
meaningful in Open as well as Review. The organizer does not gain the right to
rewrite another traveler's personal plan, silently replace another subgroup
owner's content, or operate another person's provider account.

### Action matrix after authority is established

| Operation/state | Default outcome | Required behavior |
|---|---|---|
| Inspect/read | Direct | Privacy-filter the projection |
| Materialize first dated draft | Direct after minimum context confirmation | Preserve accepted shape/anchors, explain day placement, create one tentative attributed itinerary head, and never overwrite an existing dated plan |
| Set own future attendance | Direct | Does not change block truth; show protected-ticket consequence if present |
| Record own actual attendance | Direct | Factual personal correction, separately attributed |
| Add ordinary unprotected block | Direct | Recommended placement; landed receipt and Undo |
| Create/update parallel plan | Confirm or Propose | Atomic split/branches/rejoin; name participants, branch owners, topology owner, and route consequences |
| Move/reorder ordinary flexible block | Direct | Preserve relative position/time truth; landed receipt and Undo |
| Materially move a shared block | Confirm | Name affected people, route/time conflicts, and protected anchors |
| Replace unbooked block | Confirm | Show chosen entity and decisive deltas; replace identity atomically |
| Remove future unbooked block | Confirm | Distinguish Remove from personal opt-out; recovery must be real |
| Change a protected anchor | Confirm or Denied | Confirm when changeable and controller-authorized; deny with provider handoff otherwise |
| Replace a booked block: plan only | Confirm | Replace plan identity, keep the reservation bound to its original provider subject, and surface the unresolved continuation |
| Replace + rebook | Confirm | Protected provider continuation; separate plan/provider truth and receipts |
| Optimize day | Confirm | One ordered preview, atomic apply, one atomic Undo/Revert |
| Broad/scoped replan | Confirm | Atomic typed child operations; never bypass ordinary authority |
| Change trip dates/destination with a dated plan | Confirm | Preview day/timezone remap, protected anchors, proposals, and provider consequences as one contextual replan |
| Edit live future item | Direct/Confirm by ordinary rules | Urgency shortens presentation, never expands authority |
| Move/remove in-progress immutable anchor | Denied | Offer running-late, attendance, provider, or support continuation |
| Structural edit to historical block | Denied | Offer factual correction or Memory path |
| Correct historical occurrence/attendance | Direct/Confirm by ownership | Preserve prior fact in history |
| Stale expected revision | Denied for this attempt | Refresh/rebase while preserving draft; never silently overwrite |

### Trip-policy matrix

| Context | Ordinary unprotected shared action | Consequential/protected action |
|---|---|---|
| Solo human | Direct | Confirm |
| Group organizer | Direct; may Ask group | Confirm; may Ask group; provider controller still governs external work |
| Open member | Direct with attribution | Confirm if authorized; otherwise provider/owner handoff |
| Review member | Propose exact operation to organizer/owner | Propose; acceptance may still require organizer/controller confirmation |
| Personal owner in any trip mode | Direct on own personal structure | Confirm when consequential/protected |
| Subgroup decision owner in any trip mode | Direct on owned subgroup structure | Confirm when consequential/protected |

No group language appears on a solo trip.

### Proposal resolution

- `voting_enabled=false` means structured member proposals use
  `organizer_review`.
- `voting_enabled=true` makes voting available; it does not automatically turn
  every proposal into a vote.
- `affected_member_vote` is used only when the organizer explicitly asks the
  group or a trip rule explicitly names that action class. Silence is not
  approval by default.
- Organizer review acceptance authorizes plan mutation only; protected provider
  confirmation remains separate.
- Rejection closes the proposal without mutation. A later organizer override is
  a new attributed operation with an explicit “group declined this” consequence,
  not a relabeling of the rejected proposal.
- Live urgency may shorten a deadline and escalate to the organizer; it does not
  convert silence into consent or expand authority.

### Vesper/system matrix

| Initiator | Principal | Allowed result |
|---|---|---|
| Vesper advice | None | No mutation; recommendation only |
| Vesper first-draft materialization | Confirmed minimum trip context | Create only the first tentative dated itinerary; never overwrite existing plan truth |
| Vesper at human request | Requesting human | Same scope authority as human, then stricter agency/risk grading |
| Proactive Vesper | None | Soft suggestion or organizer-ready proposal; never direct structural mutation |
| System/provider reconciliation | External proof | Update only proven provider/factual state; no replanning |

Vesper may directly apply only a trivial, reversible, high-confidence action
when the principal has direct authority, itinerary agency is `act`, no protected
dependency or privacy disclosure exists, and durable Undo is available.
Meaningful structural Add/Move/Replace/Remove operations are confirmed for an
authorized solo/organizer principal or proposed under Review. Broad replans never
silently apply. Resolver failure fails closed to no mutation.

Initial draft materialization is the narrow exception to proactive structural
mutation: after the organizer or solo traveler explicitly confirms minimum
context (destination and dates), Vesper may create the first tentative dated
itinerary because no existing plan truth is displaced. The exception cannot
regenerate, replace, or replan an existing dated itinerary.

### Recovery authority

- Immediate Undo belongs to the initiating human principal and the target's
  governing decision owner when no later dependent change exists: organizer for
  whole-group/split-rejoin topology, subgroup owner for subgroup content, and
  personal owner for personal content.
- The organizer may not use recovery to bypass another subgroup/personal
  owner's decision authority; they may propose a Revert to that owner.
- Once another operation depends on the result or the previewed revision is no
  longer current, Undo becomes a new Revert operation and runs through this same
  resolver.
- A proposed action exposes Withdraw to its proposer until resolution.
- Optimize/replan exposes one atomic recovery action, never a sequence of
  independent best-effort moves.

## Accepted server-authored capability contract

The frontend must not infer permissions from member count, role, or participant
arrays. One backend policy service computes capabilities for Itinerary, Map,
Discover/Search Add, Chat/Vesper, proposals, and proactive producers.

```ts
interface ItineraryBlockCapabilities {
  inspect: ActionCapability;
  add_relative: ActionCapability;
  move: ActionCapability;
  replace: ActionCapability;
  remove: ActionCapability;
  set_own_attendance: ActionCapability;
  mark_occurrence: ActionCapability;
  booking_change: ActionCapability;
}

interface ActionCapability {
  outcome: 'direct' | 'confirm' | 'propose' | 'denied';
  reason_code: string;
  decision_owner_id?: string;
  proposal_policy?: 'organizer_review' | 'affected_member_vote';
  confirmation_reasons: string[];
  protected_dependencies: ProtectedDependency[];
  allowed_alternatives: string[];
  predicted_recovery: 'undo' | 'withdraw' | 'review_revert' | 'provider_action' | 'new_change' | 'none';
  can_voluntarily_propose: boolean;
}
```

`predicted_recovery` is planning guidance at preview time. It must never be used
as the landed recovery control. Once an operation exists, every surface renders
the current `OperationRecoveryCapability` from canonical operation state,
revision, dependency, authority, and provider truth.

## Accepted contract versus current implementation

| Contract area | Current implementation | Status for redesign |
|---|---|---|
| Open/Review governance | `trips.plan_editing` still accepts Open/Review/Locked | Migration required; map Locked to Review |
| Personal/subgroup/whole-group scope | Nullable block `participants`; null already means everyone | Read/write model migration required |
| Decision ownership | Organizer role plus a narrow single-participant ownership inference in some edit paths | New first-class field/service required |
| Per-traveler attendance and actual occurrence | One block-wide `event_state` | New durable relation/read model required |
| Parallel branch/rejoin structure | Flat day blocks with `sort_order`; overlap is only temporal | New branch-group structure required |
| Protected dependencies/controller | `booking_ref` JSON and several booking-state predicates | Normalize behind one protection service |
| Typed operation gateway | Preview/commit handles Move/Swap/Remove; Add, direct routes, agent tools, pin, and replan use other paths | Consolidation required |
| Replace entity identity | Human commit can persist only `new_title` | Typed entity replacement required |
| Move position/time | Some paths update time without relative order; direct route appends target order | Canonical position payload required |
| Optimize/replan atomicity | Optimize can issue independent moves; replan has separate policy behavior | Atomic child-operation transaction required |
| Server capabilities | Frontend and individual routes infer portions of posture | New policy projection required |
| Human principal/agent attribution | Partial requester checks, `actor_type`, proposal flags, and plan-event sources | Unify into durable attribution |
| Revision-bound preview | Optional per-block `expected_updated_at` on one commit path | Required day/operation revision binding |
| Recovery | Direct future-unbooked Remove is atomic and fault-injection-proven; proposal Remove/Revert, Move/Optimize/replan, and provider-affecting recovery remain path-specific | Direct Remove may promise scoped Undo; keep broader destructive recovery contract-dependent |

This table is the boundary: the object model and matrix are accepted product
truth, while every row marked migration/consolidation/new remains implementation
work. Claude Design may illustrate those target states but should label them as
contract-dependent until the corresponding backend work lands.

## Attribution requirements

Every structural change should preserve:

- initiator: traveler, Vesper, system/provider;
- human principal: whose authority the action used;
- channel: itinerary, Map, Discover, chat, background producer;
- outcome: direct, confirmed, proposed, auto-resolved;
- rationale visibility: public/group-safe versus private;
- undo/revert owner and expiry.

User-facing examples:

- “Moved by you · Undo”
- “Moved by Vesper at your request · Undo”
- “Suggested by Ana through Vesper · Waiting for review”
- “Vesper suggests this because the venue is closed”
- “Updated automatically: travel time only · Undo”

## Canonical operation-history contract

The change log is an append-only projection of canonical itinerary operations,
not a second event system assembled from UI receipts, chat messages, proposal
rows, and provider callbacks. Immediate receipts, stop history, and trip-wide
Changes must resolve from the same operation id and status.

Each material operation record requires:

```text
operation id · trip id · stable subject lineage id
normalized operation + exact before/after
requester · human principal · initiator · decision actor · applying actor
source channel · group-safe rationale · private rationale reference
plan outcome · provider outcome
before/after day revisions
proposal/provider/dependency links
reverses/supersedes/compensates links
viewer visibility policy
created/decided/applied timestamps
current Undo/Withdraw/Revert capability and expiry
```

The stable subject lineage survives Replace, proposal-apply block forks, and
provider-id reconciliation so stop inspection can retrieve the history of the
scheduled thing rather than only the latest database row.

Status transitions append immutable transition records, from which current
status is derived; they never rewrite the historical before/after.
Undo and Revert are linked inverse operations. Proposal resolution and provider
completion link to the originating operation. An idempotent retry cannot create
a second visible history item.

Viewer-scoped history is server-authored. Shared structural operations are
trip-visible; personal/private details are owner-scoped; provider secrets and
private constraint rationale never enter the group projection. A failed preview
or rejected pre-mutation commit is not user-facing history unless an approved
decision, possible provider side effect, or required recovery remains.

### Accepted operation projection and lifecycle rules

The canonical operation exists independently of any one UI projection. Product
surfaces consume it as follows:

| Projection | Includes | Excludes |
|---|---|---|
| Affected stop/day | Current pending, landed, partial, or recovery state for that context | Unrelated trip activity |
| Review Stack | Unresolved proposals and decisions requiring the viewer | Settled chronology |
| Changes → Needs attention | Accepted/applying/provider/recovery exceptions with a viewer action | Ordinary open votes and nudges |
| Changes → History | Settled material operations and resolved proposal outcomes | Reads, drafts, retry chatter, transient technical stages |
| Operation detail | Immutable lifecycle transitions plus derived current truth | Raw agent reasoning, provider secrets, internal tool traces |

One visible history item represents one human intention, even when its execution
contains multiple block writes or plan/provider transitions. Optimize/Replan
therefore groups its ordered child operations; Replace + Rebook groups separate
plan and provider outcomes. A provider transition updates the originating
operation unless it is itself an independent factual action.

Accepted lifecycle states are:

```text
prepared locally (not durable shared history)
waiting_for_decision
approved_not_applied
applying
applied | partial | failed_after_approval
declined | withdrawn | superseded
reverted | partially_reverted
```

State is derived from immutable transitions. Undo/Revert is a linked inverse
operation; it does not mutate or delete the original operation. The original
can derive `reverted` after the inverse lands while the inverse retains its own
chronological position and attribution.

### Accepted recovery-duration policy

Recovery is state-based rather than governed by one arbitrary global timer:

- the local visual receipt remains emphasized for roughly 10–15 seconds, or
  long enough for its accessibility announcement, without controlling the
  semantic capability;
- Undo remains available from stop/trip history while the server proves the
  exact inverse is authority-valid, dependency-safe, revision-current, and
  provider-safe;
- a later dependency, revision, protection, or provider transition changes the
  capability to `review_revert` with a reason and preview requirement;
- Withdraw remains available until proposal resolution has atomically begun;
- provider cancellation/change is a separately typed provider operation;
- history remains inspectable after recovery becomes unavailable.

The response contract for every material operation therefore requires a
server-authored recovery object rather than a client-side event-type lookup:

```ts
interface OperationRecoveryCapability {
  kind: 'undo' | 'withdraw' | 'review_revert' | 'provider_action' | 'new_change' | 'none';
  available: boolean;
  owner_ids: string[];
  reason_code?: string;
  explanation?: string;
  preview_required: boolean;
  provider_continuation?: { kind: string; reference: string };
}
```

### Accepted seen, attention, and notification policy

Seen state is viewer/trip state, not operation age. Maintain a durable compound
cursor per viewer so multiple devices converge even when operations share a
timestamp. The initiating traveler's successful operation is seen for that
traveler. Material operations by another traveler, Vesper, system, or provider
may be unseen; routine transitions do not create engagement noise.

`unseen` and `needs_attention` are independent. Viewing an operation advances
the viewer cursor but does not resolve a provider exception, vote, or recovery
task. Counts and badges come from a viewer-scoped server projection. A frontend
rule such as “older than six hours means read” is invalid.

Shared-change awareness is proportional and server-authored:

| Change | Default awareness |
|---|---|
| Personal attendance with no protected consequence | Quiet attendee-list update; no group chat post or push |
| Ordinary Open-mode shared edit | Unseen itinerary/history state for affected travelers; no automatic chat message |
| Material shared time/place/branch change | Unseen state plus one grouped trip notification; optional group-safe chat receipt only when coordination is time-sensitive |
| Review proposal | Named organizer task; other members see contextual waiting state without duplicate nudges |
| Live disruption or protected/provider consequence | Targeted notification to the decision owner/controller and affected travelers; Needs attention when action is required |

The same operation id deduplicates itinerary state, push, and any chat receipt.
The awareness layer never copies private rationale into a shared notification.

### Accepted itinerary write-back policy

Itinerary interactions are product signals as well as operational edits, but
history evidence must not be naively treated as preference truth.

- plan structure, provider state, and operation outcome always update Trip
  Context;
- explicit personal attendance and actual occurrence may update Traveler
  Identity with their stated meaning;
- Replace, Remove, Revert, reorder, keep-open, and branch choices create
  confidence-scored observations, not unconditional likes/dislikes;
- group decisions update Group State only with group-safe outcome and decision
  context; they do not expose which private constraint influenced the result;
- entity-specific place signals require stable chosen/replaced identity and
  provenance; a title-only or ambiguous custom block cannot update Place taste;
- provider failure, closure, price, timing, and route reasons are operational
  evidence, not negative taste;
- Undo/Revert links to and corrects the earlier observation rather than leaving
  contradictory permanent signals;
- every write-back stores source operation id, subject, owner/audience,
  confidence, and correction/supersession link.

No additional form is required merely to capture these signals. When intent is
ambiguous, Vesper may ask a lightweight optional follow-up, but declining it
does not block the itinerary action.

### Accepted membership, deletion, and retention policy

- Current members receive a server-authored group-safe projection appropriate
  to their role and recovery authority.
- A new member receives current shared truth. Earlier history is disclosed only
  as needed to explain that truth, with pre-membership personal attribution and
  rationale redacted by policy.
- A removed member loses access immediately; possession of an old route,
  cursor, cache entry, or operation id grants nothing.
- On departure, remaining members retain minimal group-safe structural
  continuity and may see `Former traveler` rather than a retained identity.
- Account deletion removes private/verbatim payload and identifying references.
  Where data-retention policy permits, an anonymized structural operation
  survives so a shared itinerary mutation remains explainable.
- A public share receives neither history, actor details, seen state,
  attention state, nor recovery capabilities.

This requires group-safe operation fields to be stored separately from private
source material. A personal chat quote or private constraint cannot be copied
into the shared ledger and later “redacted” only in the client.

Shared-plan ownership is governance history, not an itinerary edit. Every
user-initiated ownership transfer—manual transfer, owner demotion, membership
removal, or organizer handoff—must append exactly one
`itinerary.owner_transferred` event in the same database transaction as the
authority mutation. The event records the previous and new owner, initiating
actor when known, affected traveler, whether the successor was promoted, and a
bounded reason code. A failed or rolled-back transition creates no ownership
event. Account erasure remains governed by the stricter anonymization and
retention policy above; it must not preserve a newly identifying audit payload.

The itinerary Changes surface remains the normalized operation ledger: it must
not mix role, membership, invitation, or ownership administration into the
count of plan changes. A future inspectable people/governance activity surface
may project the durable trip audit, but it must label that history separately
instead of making an organizer handoff look like a Move, Replace, or Remove.

Durable human-readable before/after evidence survives itinerary-version
pruning. Pruning may make an exact restore unavailable; it changes recovery to
`new_change` or `review_revert` and never removes the historical explanation.

### Accepted offline and asynchronous contract

- The MVP has no itinerary mutation outbox. An action attempted while offline
  is blocked before mutation, is not shared history, and is explicitly labeled
  as not sent. The traveler retries after reconnecting; the app must not promise
  automatic delivery. An editor may preserve local input, but that is not a
  queued operation.
- Once accepted by the server, operation status is queried by stable operation/
  idempotency identity after timeout or reconnect.
- Unknown response means unknown, not success. Duplicate retries cannot create
  multiple operations or receipts.
- A successful plan mutation with provider work pending reports one operation
  with distinct plan/provider lanes.
- A pre-mutation validation failure stays local unless an approved decision,
  provider uncertainty, or recovery obligation requires durable closure.
- An approved action that fails to apply and any possible provider side effect
  enter Needs attention with a named owner and safe continuation.

### Focused current-to-target history delta

The current code cannot satisfy this target by visual restyling:

- Plan State truncates `recent_changes` to a 72-hour window and at most 50 rows;
- direct changes may be synthesized from the current block `updated_at` rather
  than one canonical operation, so removed or replaced subjects are fragile;
- current `PlanChange` lacks before/after, principal/initiator distinction,
  provider outcome, transition links, and server recovery capability;
- the Changes client infers “read” from six hours of age;
- the Changes row infers Undo from event type and first affected block id;
- some mutation writers treat `plan_events` as best-effort after the primary
  mutation, so a visible change can exist without durable evidence;
- account deletion currently removes an author's entire plan-event row to
  purge verbatim payload, demonstrating why private source data and minimal
  group-safe structural evidence must be separated.

The target is therefore a canonical operation aggregate plus immutable
transitions and viewer-scoped read models, not an extension of
`TripPlanState.recent_changes`.

## Business decisions required before Claude Design

### Human permissions

- [x] Reduce group editing modes to Open and Review; retire trip-wide Locked.
- [x] Organizer actions normally apply directly, with an optional Ask group path.
- [x] Protected bookings and broad consequential changes require organizer confirmation.
- [x] Personal-block direct editing by its owner is a v1 rule in every trip mode.
- [x] Subgroup blocks require explicit decision ownership; attendance does not grant authority.
- [x] A member may change their own participation without moving/removing the shared block.
- [x] Attendance is separate from decision ownership and edit authority.
- [x] Preserve shared event truth plus per-traveler attendance/happened/skipped state.
- [x] Support simultaneous personal/subgroup events as parallel branches in one shared day.
- [x] Parallel branches are explicit branch-group nodes with ordered branch blocks and an optional end-of-day rejoin omission.
- [x] Notes are explicitly typed as trip-shared, personal, or Vesper-private.
- [x] Open/Review governs whole-group editing and does not erase personal or subgroup decision ownership.
- [x] Parallel branch creation/update is one compound operation with organizer-owned split/rejoin topology and branch-owned content.
- [x] Governance changes re-resolve drafts and future commits without retroactively applying or rewriting existing proposals.
- [x] V1 has one itinerary organizer/decision owner; transfer atomically reassigns unresolved tasks without rewriting history.

### Group resolution

- [x] `voting_enabled=false` routes member proposals to organizer review.
- [x] Organizer review is the default decision mechanism for member proposals.
- [x] Voting is explicit trip policy or an action-specific exception, not the default.
- [x] Affected-member voting occurs only when the organizer explicitly asks or a trip rule names the action class.
- [x] Rejection closes that proposal with no mutation.
- [x] An organizer override is a new confirmed, attributed operation—not a relabeled rejected proposal.
- [x] Live urgency may shorten/escalate a deadline but never turns silence into approval.

### Agent authority

- [x] Use explicit Advise / Propose / Act itinerary agency.
- [x] Vesper may apply only trivial, reversible changes at an explicit user request and within that user's authority.
- [x] Vesper does not proactively apply shared structural changes by default.
- [x] Vesper fails closed to no mutation when principal/authority resolution fails.
- [x] Meaningful solo changes confirm; shared structural changes route to organizer review.
- [x] Broad group replans never silently apply.
- [x] Live urgency permits the same future-item actions with compressed presentation; it does not expand authority or permit silent protected changes.
- [x] Vesper delegation is per traveler and trip, separate from Open/Review and capped by the human principal's authority.

### Protected state

- [x] Protected dependencies explicitly carry type, provider state, changeability, controller, and provider reference; anchor is a separate structural role.
- [x] The provider controller governs external changes; itinerary authority alone is insufficient.
- [x] Replacing a plan stop does not claim to change its provider booking.
- [x] Replace and rebook is a distinct protected workflow.
- [x] Confirmation and receipt language separately states the plan delta,
  provider outcome, relevant actor/principal, and truthful recovery; exact
  microcopy may vary within that anatomy.
- [x] Replace updates chosen entity identity and derived plan projections atomically; provider booking truth changes only in Replace + rebook.

### Undo and history

- [x] Immediate Undo belongs to the initiating principal and the governing target owner—organizer for whole-group/topology, subgroup owner for subgroup content, personal owner for personal content—when no dependent edit exists.
- [x] Another traveler or organizer cannot use recovery to bypass subgroup/personal ownership; they use a new Revert request to the owner.
- [x] Undo becomes Revert when the revision changed or a later operation depends on the result.
- [x] Optimize-day is one atomic operation with one atomic Undo/Revert.
- [x] Receipt emphasis is approximately 10–15 seconds; Undo is available while the server proves an exact safe inverse, Withdraw until resolution begins, and later recovery becomes Review revert/new change rather than expiring silently.
- [x] Durable history must exist before the UI promises Undo.
- [x] The server checks expected revision and dependent operations before restoring order.
- [x] Immediate receipt, stop history, and trip-wide Changes are projections of one canonical operation record.
- [x] Replace/fork/reconciliation preserves a stable subject lineage for stop-level history.
- [x] History is append-only, viewer-scoped, privacy-filtered, and reports plan/provider truth separately.
- [x] Review Stack owns ordinary unresolved decisions; Changes contains settled history plus exceptional Needs-attention recovery states.
- [x] Seen state uses a durable per-viewer cursor and remains distinct from server-authored Needs attention.
- [x] Removed/replaced stops retain historical snapshots and safe lineage navigation without dead current-block links.
- [x] Membership/deletion rules preserve only the minimum group-safe structural continuity and never leak private source payload.
- [x] Preview-time predicted recovery is distinct from the current landed operation recovery capability.
- [x] Every operation that advertises Undo requires atomic inverse evidence and fault-injection proof, regardless of whether the verb is labeled destructive.

### Trip phase

- [x] Lifecycle uses one server-authored destination-local projection: early planning >14 days, active planning 4–14, final prep 1–3, live start-through-end inclusive, post-trip beginning the day after end.
- [x] Future live-trip blocks use ordinary rules; in-progress immutable anchors deny structural Move/Remove and offer safe continuations.
- [x] Post-trip structural rewrites are denied while occurrence and attendance corrections use a separately attributed factual path.
- [x] Undated trips use Trip Shape rather than fabricated dated itinerary days.
- [x] Destination/date changes over an existing itinerary are consequential contextual replans with explicit day/timezone/provider remapping.
- [x] Shared-change awareness is proportional, deduplicated by operation id, and privacy-filtered.
- [x] Itinerary write-back uses typed, confidence-scored, correctable observations rather than treating every edit as preference truth.

## Engineering audit actions after product rulings

These are investigation/fix candidates, not authorized changes:

1. Inventory every itinerary mutation path and require the canonical resolver.
2. Replace the title-only replacement payload with a typed chosen-entity operation.
3. Guard and validate participation changes; remove their ability to self-grant edit authority.
4. Close the `pin_experience` and full/scoped replan edit-policy bypasses.
5. Enforce fail-closed/no-mutation behavior for agent authority errors and handle `denied` as a first-class result.
6. Remove frontend permission inference in favor of server capabilities.
7. Implement per-traveler attendance/event truth for group and subgroup blocks.
8. Make Move carry day, time, and relative position consistently.
9. Make optimize-day an atomic preview/commit/undo operation.
10. Repair destructive Remove Undo or stop promising it.
11. Separate actor confirmation from group active approval at the product-contract level.
12. Route every proposal producer through one creation spine and explicit decision policy.
13. Bind previews to exact action payloads and a plan/day revision.
14. Commit structural mutation and canonical history evidence atomically.
15. Verify all phase boundaries and proposed times use destination-time truth consistently.
16. Add cross-entry-point contract tests: app, chat, Map, Discover Add, proactive producer.
17. Separate Review Stack/current decision state from settled Changes history and exceptional recovery attention.
18. Replace elapsed-time read inference with durable per-viewer compound cursors and independent attention state.
19. Separate group-safe structural history from private source context so membership/account deletion can re-project safely.
20. Replace the 72-hour recent-changes adapter with paginated operation history, canonical detail, lineage tombstones, and current-successor navigation.
21. Add undated Trip Shape and a single attributed shape-to-dated-itinerary materialization boundary.
22. Implement compound parallel-plan operations and enforce branch/topology ownership independently.
23. Split trip Open/Review governance from per-traveler itinerary delegation and re-resolve safely when either changes.
24. Project proportional per-viewer awareness from the canonical operation id rather than posting duplicate chat/push receipts.
25. Emit typed, confidence-scored, privacy-scoped write-back observations with Undo/Revert correction links.
26. Give the existing Folio read model an explicit decomposition/retirement adapter so lifecycle, attention, source degradation, and partial-data semantics are preserved rather than discarded.

## Sequenced backend and read-model migration plan

This is the implementation order, not authorization to change production in
this documentation pass. The sequence keeps schema migration, policy, mutation,
read projection, frontend, and rollout independently reversible.

### Dependency chain

```text
W0 lifecycle source of truth
→ W1 additive domain schema + safe backfill
→ W2 canonical policy/capability service
→ W3 typed operation gateway + proposal convergence
→ W4 atomic history/recovery
→ W5 itinerary/details/map read models
→ W6 frontend trip shell + interaction grammar
→ W7 shadow rollout, migration completion, old-path retirement
```

W0 and additive parts of W1 may proceed in parallel. W6 must not expose target
mutation states until W2–W5 support them server-side.

### W0 — One lifecycle source of truth

Build one backend `TripLifecycle` projection from dates, destination timezone,
terminal status, and the dogfood date override.

Required behavior:

- emit `ideation | planning | final_prep | live | post_trip` plus planning
  detail, optional `completed | cancelled` terminal state, destination-local
  date, timezone/source, countdown/day numbers, and optional disruption summary;
- use early >14 days, active 4–14, final prep 1–3, live inclusive dates, and
  post-trip the following destination-local day;
- make Plan State, Map State, Home/Folio compatibility reads, Concierge context,
  notifications, edit policy, and voice/modality consume the same projection;
- remove raw-status lifecycle shortcuts from Map and client-side phase authority;
- keep the frontend helper only as a compatibility adapter until all reads carry
  lifecycle, then remove it as a policy source.

Primary hotspots:

- `travel-agent/backend/core/trip_phase.py`
- `travel-agent/backend/core/world_model/types.py`
- `travel-agent/backend/core/db/plan_state.py`
- `travel-agent/backend/core/map_state/builder.py`
- `travel-app/utils/helpers.ts`

Exit gate: one matrix test feeds the same trip/timezone/instant to every consumer
and asserts identical phase, local date, and day number, including DST edges and
the hours around destination midnight.

### W1 — Additive canonical domain schema

Add target fields/tables without deleting current columns:

```text
trip_shapes
  trip id · destination intent · duration · anchors · loose regions · revision
  · decision owner id · membership revision

traveler_itinerary_delegation
  trip id · user id · advise/propose/act · updated_at

itinerary_blocks
  subject_lineage_id
  participation_scope
  decision_owner_id
  structural_role
  occurrence_state

itinerary_block_participation
  block_id · user_id · intention · actual · updated_by · updated_at

itinerary_branch_groups / itinerary_branches
  day · topology owner · split/rejoin references · ordered block membership

itinerary_annotations
  block_id · visibility · owner_id · text

itinerary_protected_dependencies
  block_id · type · provider_state · changeability · controller · provider_ref

itinerary_day_revisions
  day_id · revision

itinerary_operations
  subject lineage · normalized operation · group-safe before/after · attribution
  resolution · plan/provider outcome · revisions · visibility policy

itinerary_operation_transitions
  operation id · transition type · actor · immutable evidence · occurred_at

itinerary_operation_private_context
  operation id · owner/audience · private source reference or encrypted context

itinerary_history_viewer_state
  trip id · user id · last_seen_created_at · last_seen_operation_id · updated_at

itinerary_operation_awareness
  operation id · viewer id · channel · state · dedup key · delivered/seen timestamps

itinerary_writeback_observations
  operation id · model target · owner/audience · signal · confidence · correction link
```

Migration rules:

| Legacy data | Additive target backfill |
|---|---|
| `participants IS NULL` | `scope=whole_group`; snapshot active members + membership revision; organizer decision owner |
| one participant | `scope=personal`; that traveler decision owner |
| multiple participants | `scope=subgroup`; organizer temporary owner plus `needs_owner_review=true` until explicitly assigned |
| `event_state=planned` | block occurrence `planned`; do not infer individual attendance |
| `event_state=happened` | block occurrence `happened`; individual actual remains unknown |
| `event_state=skipped` | block occurrence `did_not_happen` with `legacy_block_skip` provenance; do not infer who opted out |
| shared `notes` | trip-visible annotation |
| `booking_ref` | best-effort protected dependency; unknown changeability stays unknown |
| existing block | create a self-rooted `subject_lineage_id`; Replace/fork successors inherit it |
| current plan event | best-effort backfill to one operation when source and diff prove identity; otherwise retain as legacy read-only history with unknown fields, never invent attribution |
| timestamp overlaps | no branch inference; intentional parallel structure requires explicit grouping |
| `plan_editing=locked` | behavior/read projection maps to `review` before the enum is retired |

Do not derive authority from mutable participant backfill. Backfill decisions are
compatibility defaults and must be visible in migration telemetry.

Exit gate: migration fixtures preserve current itinerary rendering and booking
truth byte-for-byte while new projections expose explicit scope, lineage, and
provenance. A Replace fixture proves predecessor and successor resolve to one
stop-history lineage. A departure/deletion fixture removes private payload while
preserving only permitted anonymized group-safe structural continuity.

### W2 — Canonical resolver and server capabilities

Implement one pure resolver over the accepted action matrix and one DB-backed
adapter that loads membership, target governance, lifecycle, protection, risk,
and revision.

Deliverables:

- `Direct | Confirm | Propose | Denied` plus reason, named decision owner,
  proposal policy, confirmation reasons, protected dependencies, alternatives,
  recovery posture, and voluntary-proposal capability;
- human principal separate from Vesper/system initiator;
- explicit personal/subgroup/whole-group authority;
- provider controller separate from itinerary authority;
- fail-closed no-mutation behavior when policy/principal loading fails;
- block/day capabilities embedded in read models;
- a temporary shadow mode comparing current `resolve_edit_mode` with the new
  resolver without changing outcomes.

Exit gate: generated matrix tests cover every actor × editing mode × scope ×
operation × lifecycle × protection combination, with invariant tests proving
no agent or participant mutation can self-grant authority.

### W3 — Typed operation gateway and proposal convergence

Introduce one normalized gateway:

```text
POST /api/trips/{trip_id}/itinerary/operations/preview
POST /api/trips/{trip_id}/itinerary/operations/commit
```

The preview binds normalized payload, target provenance, human principal,
expected day revision, computed capability, and consequences. Commit revalidates
all of them.

Operation requirements:

- Replace carries entity kind/id and refreshes derived place/map/cost/hour truth;
- Move carries target day, before/after anchor, time semantics, and branch;
- Add carries entity/custom truth, placement, participation scope, owner, and
  source provenance;
- Create/Update Parallel Plan carries the complete split, branch memberships,
  branch owners, topology owner, and rejoin as one compound operation;
- Remove is structural and never aliases personal attendance;
- Optimize/Replan carries ordered child operations;
- attendance and occurrence are their own operations;
- `provider_intent=plan_only | plan_and_provider` is explicit.
- Trip Shape materialization and later destination/date changes use the same
  attributed revision/preview discipline; contextual replans cannot bypass the
  gateway because they originate in Trip Details.

Adapt current app routes, direct block endpoints, agent tools, Discover pin/Add,
Map actions, Chat proposals, proactive producers, and replan behind this gateway.
During migration they may be compatibility adapters, but none may independently
resolve authority or write structural fields.

Proposals persist the exact normalized operation, public rationale, attribution,
creation-policy snapshot, and future confirmation/provider requirements. Those
authored facts are immutable. Acceptance re-runs current authority, safety,
provider, phase, and revision checks; accepted does not automatically mean
applied, and stale work is rebased into a new attributed proposal rather than
mutating the old one.

Exit gate: the same operation fixture submitted from Itinerary, Map, Discover,
Chat, and Vesper produces the same preview hash, capability, persisted truth,
attribution, and proposal behavior.

### W4 — Atomic history, Undo, Revert, and provider sagas

Mutation and canonical operation history commit in one transaction. A successful
response never depends on a best-effort later ledger/receipt write.

Required capabilities:

- operation record contains before/after, affected block/day ids, stable subject
  lineage, revisions, requester/principal/initiator/decision/applier attribution,
  source channel, group-safe rationale, viewer visibility, provider intent, and
  dependency references;
- group-safe structural evidence is stored separately from private source
  context so account deletion and viewer redaction do not require client-side
  filtering of verbatim payload;
- immutable transition evidence links proposal resolution, application,
  provider reconciliation, compensation, Undo, and Revert to the originating
  operation; idempotent retries never duplicate visible history;
- current operation status is derived from transitions, and one user intention
  aggregates multi-block/provider stages into one visible history operation;
- the server returns the current typed recovery capability, owner, reason, and
  preview requirement; the client never infers Undo from event type;
- Undo verifies initiator/organizer authority, current revision, protection,
  provider state, and absence of dependent operations;
- dependency, revision, protection, or provider change converts Undo into a new
  Revert/new-change preview;
- Withdraw is available only before proposal resolution atomically begins;
- Optimize/Replan applies and recovers atomically;
- Replace + rebook is a saga with explicit plan/provider states and compensating
  recovery, never a generic optimistic Undo;
- plan-only Replace retains honest orphaned/unchanged provider truth.
- no verb may advertise Undo until its exact inverse evidence and one-time
  marker pass authority, dependency, stale/revision, idempotency, concurrency,
  and transaction fault-injection tests;
- awareness projections and model write-back key off the committed operation id;
  delivery or learning-pipeline failure cannot falsify mutation/history truth,
  and retry cannot duplicate a user-visible receipt or observation.

Exit gate: fault-injection tests fail at every transaction/saga boundary and
prove the user sees either no mutation or the exact partial provider state with
a recoverable continuation. The immediate, stop-level, and trip-wide projections
must agree on operation id, attribution, delta, status, and recovery capability.
Version-pruning tests preserve human-readable history while safely degrading an
unavailable exact inverse to Review revert/new change.

### W5 — Coherent read models

Evolve Plan State additively with a schema version rather than forcing all
existing consumers to switch routes at once.

`plan-state` target additions:

- undated Trip Shape or dated itinerary discriminator;
- canonical lifecycle;
- day revisions;
- explicit scope, owner, participation, occurrence, branch/rejoin structure;
- normalized protection;
- server capabilities;
- pending normalized operation/proposal state;
- durable landed/recovery state.

History projections:

```text
plan-state block summary
  last material operation + current landed/pending/recovery state

GET /api/trips/{trip_id}/itinerary/history
  viewer-scoped settled trip chronology + exceptional Needs attention
  stable compound cursor pagination + unseen/attention summary

GET /api/trips/{trip_id}/itinerary/history?subject_lineage_id={id}
  stop-level material history including historical tombstone/current successor

POST /api/trips/{trip_id}/itinerary/history/seen
  advance this viewer through an exact returned compound cursor
```

These read the canonical operation ledger. They do not join ad hoc client events
or reconstruct before/after from current blocks. Ordinary open decisions remain
in Review Stack/current stop state; resolved decisions enter history. Unseen and
Needs attention are separately derived. Membership, join time, departure,
deletion, private ownership, and recovery authority are enforced in every item
projection and operation-detail fetch.

Map State consumes the same day/block/branch projection rather than independently
mapping raw status and stop actions.

Add a trip-details read model so the client does not assemble cross-trip truth
from many partially loaded routes:

```text
GET /api/trips/{trip_id}/details-state
identity · people · stay · transport · costs · bookings · history · settings
```

Also add:

- major Transport summary/index over fixed anchors, tickets, and handoff gaps;
- Bookings index over sessions, held/expired/failed states, and provider proof;
- canonical deep links from each summary to block/provider/ledger truth.

Decompose the current Folio deliberately rather than deleting its useful
backend behavior with the hero-led UI:

| Current Folio responsibility | Target owner |
|---|---|
| lifecycle/mode | canonical `TripLifecycle` |
| itinerary spine | versioned `plan-state` / Trip Shape projection |
| ranked urgent “what matters now” | one itinerary Needs-attention/Now projection |
| stay/transport/cost/booking facets | `details-state` summaries plus timeline anchors |
| recent changes | canonical operation history/unseen projection |
| source-status and partial-data diagnostics | shared read-model envelope used by Plan/Details |
| discovery candidates | Discover/Add/Replace supply |
| keepsake/memory | post-trip Memory |

Keep `/folio` as a compatibility adapter during dual-read rollout. Measure field
parity and first-paint latency, then retire the endpoint only after every useful
responsibility has a named target owner and old-client compatibility window.

Exit gate: List, Map, Trip Details, Chat attachment, and Changes agree on block
ids, order, lifecycle, scope, provider state, pending decision, and last landed
operation after every mutation.

### W6 — Frontend trip shell and interaction migration

Build one trip-scoped client editing context:

```text
trip · lifecycle · face · day · block/gap · candidate · placement
scope/owner · capability · expected revision · draft · return token
```

Ship in reversible slices:

1. compact itinerary-first shell, title/date Trip Details, Chat, List/Map;
2. undated Trip Shape/first-draft state and read-only Trip Details using
   `details-state`;
3. inspect-first row and Map peek with explicit Change;
4. Add/Move/Replace through the typed gateway for solo/direct users;
5. immediate receipts, canonical operation detail, stop history, trip-wide
   Changes/Needs attention, per-viewer seen cursor, tombstones, and proven
   Undo/Revert;
6. Review proposals, personal attendance, subgroup owner, and parallel branches;
7. Vesper parity and protected continuation over the same history contract;
8. server-authored completed-record/Memory readiness and factual correction paths;
9. destination/date contextual replan, governance transitions, proportional
   shared awareness, and operation-linked write-back verification.

Cross-surface source stays mounted or restores through the return token. Dirty
drafts survive place detail, Map, Chat, provider handoff, and stale rebase.

Exit gate: the eight low-fidelity manual/Vesper journey pairs and four lifecycle/
governance/awareness journeys in the UX audit pass on device with backend-real
data, accessibility alternatives, offline/read
behavior, and exact return-position assertions. The twelve end-to-end
change-history journeys additionally prove provider partials, membership and
deletion projection, removed-stop navigation, cross-device convergence, and
post-trip factual correction.

### W7 — Shadow rollout and retirement

- Feature-flag by dogfood cohort/trip, not by loosely related component.
- Run lifecycle and policy resolvers in shadow first; record disagreements.
- Dual-read old/new projections during migration; avoid permanent dual-write by
  routing writes through the operation gateway as soon as W3 is ready.
- Start with read-only shell/Trip Details, then low-risk solo operations, Open/
  Review, branches/attendance, Vesper, and protected workflows.
- Monitor capability-to-403 mismatches, stale rebase rate, proposal apply
  failures, partial provider sagas, Undo/Revert failures, List/Map disagreement,
  lifecycle disagreement, Folio-to-target field parity, first-paint latency,
  duplicate awareness delivery, and write-back correction failures.
- Keep schema changes additive until migrated rows, shadow comparisons, and
  backend-real journeys are clean. Then remove `locked`, participant-derived
  ownership, title-only Swap, raw-status Map phase, direct mutation bypasses,
  and frontend lifecycle authority.

Rollback disables the new read/interaction flag and compatibility adapters keep
old clients functional; it never requires destructive schema rollback.

### Test and evidence matrix

| Layer | Required evidence |
|---|---|
| Lifecycle | Destination-midnight, DST, missing timezone, dogfood pin, status/date disagreement, completed/cancelled entry behavior, multi-city boundary fixture |
| Migration | Null/one/many participants, legacy skip, shared notes, unknown booking, locked policy, overlapping blocks, Replace lineage inheritance |
| Policy | Exhaustive matrix plus principal/agent/provider authority invariants |
| Operations | Cross-entry preview hash parity, idempotency, stale revision, atomic child operations, shape materialization, parallel-plan topology, destination/date contextual replan |
| Recovery | State-based typed Undo/Revert, proposal Withdraw race, every Undo-advertising verb under transaction faults, provider saga faults, version-pruning degradation, immutable inverse links |
| Read models | Immediate/stop/trip/operation-detail parity; stable cursor pagination; unseen versus attention; tombstone/successor navigation; membership/deletion/privacy projections |
| Frontend | Eight paired itinerary journeys, four lifecycle/governance/awareness journeys, plus twelve history journeys; Dynamic Type/screen reader/Reduced Motion; offline and cross-device reconciliation; exact return focus |
| Rollout | Shadow disagreement dashboard; Folio field/latency parity; awareness dedup; write-back correction; backend-real dogfood receipts/screenshots |

## Claude Design handoff gate

Do not hand off the redesign as canonical until:

- [x] Editing-mode semantics are settled.
- [x] Human roles and block scopes are settled.
- [x] Agent action classes and authority are settled.
- [x] Risk tiers and protected commitments are settled.
- [x] Proposal resolution semantics are settled.
- [x] One action-resolution matrix is approved.
- [x] The expected capability contract is documented.
- [x] Replace, Move, Add, Remove, and Optimize each have one canonical typed operation.
- [x] Participation, attendance, ownership, and decision authority are separate concepts.
- [x] Undated Trip Shape and dated itinerary truth are separate concepts.
- [x] Parallel split/branch/rejoin is a first-class compound operation, not only a display object.
- [x] Trip Open/Review and per-traveler Vesper delegation are separate governance axes.
- [x] Immediate receipt, stop history, and trip-wide Changes share one operation-history contract.
- [x] Changes is separated from the ordinary decision inbox; only exceptional recovery work appears in Needs attention.
- [x] One visible operation aggregates its immutable proposal, apply, provider, and recovery transitions.
- [x] Operation detail, state-based recovery, seen cursor, tombstone navigation, membership/deletion, offline/partial states, long-history grouping, and accessibility are specified.
- [x] Twelve end-to-end history journeys are required in addition to the eight paired itinerary journeys.
- [x] Direct future-unbooked Remove has atomic ledger-backed Undo with authority,
  stale/revision, idempotency, concurrency, and fault-injection proof.
- [ ] Every operation that advertises Undo—including Add, Move/Reorder,
  plan-only Replace where reversible, proposal Remove/Revert, Optimize/Replan,
  and parallel-plan topology—has equivalent atomic recovery proof, not only
  recovery copy. Provider-affecting Replace + rebook instead proves its typed
  saga/compensation continuation and never advertises generic Undo.
- [x] Full/scoped replan is contractually required to use the same authority and
  risk resolver as block edits; implementation is sequenced in W3.
- [x] The UX brief distinguishes shipped behavior, accepted target behavior,
  implementation-required states, and later extensions.
- [x] Shared-change awareness, governance transitions, Folio decomposition, and
  operation-linked preference write-back have accepted target contracts.

Claude Design should receive eight paired manual/Vesper behavioral journeys:

1. Inspect a stop.
2. Move/reorder a stop.
3. Find and choose a replacement.
4. Add from a gap or another surface.
5. Create a parallel subgroup branch and rejoin.
6. Change one traveler's attendance without changing the shared event.
7. Send a complete Review-mode member proposal to the organizer.
8. Undo, withdraw, revert, or recover from a stale change.

Every journey must demonstrate:

```text
intent construction
→ capability/outcome communication
→ consequence preview proportional to risk
→ apply / confirm / propose / deny
→ landed attribution
→ undo / withdraw / recovery
```

## Desired final business contract

The audit is complete when the product can answer this sentence without referring to a particular screen:

> A traveler or Vesper may construct any precise itinerary change; one canonical policy service decides whether it applies, requires confirmation, becomes a proposal, or is denied based on authority, affected scope, trip phase, risk, privacy, and protected commitments, and every landed action is attributable and reversible according to one consistent history model.

That contract—not the current Change Studio component—is what the new itinerary interaction design should express.
