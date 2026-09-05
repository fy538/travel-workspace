---
doc_type: working
status: active
owner: founder / Home orchestration
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Plans the connected-prototype and cross-lane engineering feasibility phase after the Home-only composition iterations; the design handoff owns visual critique while this companion owns sequencing, integration questions, deliverables, and completion criteria.
supersedes: []
---

# Home — connected experience and implementation-readiness plan

## 1. Outcome and scope

Turn the Revision 3 Home composition into **one connected prototype plus an
evidence-backed implementation map**. The question is now whether useful Home
material leads into coherent experiences and returns correctly, not whether we
can invent more types of Home cards.

This is the next phase of the [Home design handoff](claude-design-vesper-home-generous-value-handoff-2026-09-04.md).
It sits within the [HPL productization program](home-places-life-productization-program-2026-09-04.md);
it does not replace the broader product roadmap or establish a new canon.

**Current authorization:** detailed planning and documentation. The work below
is proposed execution; no tasks have been dispatched, paid data acquired, app
code changed, flags enabled, or prototype implemented by writing this plan.

Keep Home / Chat / Places / Life. Preserve Revision 3's richer scroll, selective
cards, readable type roles, authored social content, and value-first sample.
No new root, generic social platform, booking flow, or duplicate owner store.

The four journeys below exercise one system across solo possibility, social
value, shared consequence, and contribution. None becomes the product's
exclusive loop or a prerequisite for designing the others.

## 2. Starting evidence — bounded inspection, not readiness certification

On September 4, the planning inspection observed backend main at `d10fafd86`
and mobile main at `ec09c0f41`. Adjacent tasks are active; recheck branch, status,
and commits before implementation. These references date the inspection and
are not instructions to reset any repository.

| Inspected foundation | Evidence | Planning implication / still to verify |
| --- | --- | --- |
| Home v2 serving and interaction orchestration | [HomeRootExperience](../../travel-app/components/home-root/HomeRootExperience.tsx) | Reuse typed projection consumption, source inspection, confirmation, expiry handling, and compatibility fallback. It does not establish that the Claude compositions are implemented. |
| Home renderer and layout restoration | [HomeRootV2Screen](../../travel-app/components/home-root/HomeRootV2Screen.tsx) | Existing regions and unit offsets can support composition and return. Audit fit before making another root renderer. |
| Destination routing | [rootProjectionNavigation](../../travel-app/utils/rootProjectionNavigation.ts) | Entity and Places-context paths exist. Generic resource handling sends several prospective kinds to Chat; Life-targeted destinations currently resolve to its root. Trace the actual capability-specific path before claiming exact arrangement or record opening. |
| Return registry | [rootProjectionReturnRegistry](../../travel-app/utils/rootProjectionReturnRegistry.ts) | Viewer/revision/unit context and exact-versus-recomposed resolution exist. Registry is in-memory with a 30-minute lifetime, not durable product memory or guaranteed restoration after restart. |
| Places presentation ancestry | [placesRouteFamily](../../travel-app/utils/placesRouteFamily.ts) | Reuse Home-depth versus Places-root navigation instead of duplicating Places screens. |
| Consequence boundary | [useRootConsequenceConfirmation](../../travel-app/hooks/useRootConsequenceConfirmation.ts) | Inspect which actions already preview/resolve and which new arrangement commands are unsupported. Do not route read-only exploration through confirmation. |
| Projection reads | [rootProjections data hooks](../../travel-app/data/rootProjections.ts) | Home v2 is flag-gated, with refresh/revalidation behavior. A refetch is not evidence of a generation call; trace both separately. |
| Backend composition | [root projection feature contract](../../travel-agent/backend/root_projection/FEATURE.md) | Existing bounded owner reads, selection, semantic composition, and domain-owned consequences are the reuse baseline. |
| Source contribution production | [pipeline](../../travel-agent/backend/root_projection/v2/source_contribution_pipeline.py), [producer](../../travel-agent/backend/root_projection/v2/source_contribution_producer.py) | Authority/material checks and per-call budgets exist. Account-level economics and result-reuse coverage require a separate trace. |
| Life records and retained originals | [record adapter](../../travel-agent/backend/life_projection/record.py), [root routes](../../travel-agent/backend/api/routes/root_projections.py) | Recent code exposes canonical artifact/trip paths and retained intake originals without inventing occurrence dates. Earlier claims that Life only has a shallow generic root are stale; verify the specific intake-to-record journey against current code. |
| Adjacent Plans design | [execution report](claude-design-plans-in-real-life-execution-report-2026-09-04.md) | A contextual Ask Vesper pattern and scripted shared-Saturday prototype are reported. Reuse their proposed destination behavior; neither report nor scripted recognizers prove backend implementation. |

No runtime test suite, native acceptance run, or cost benchmark was executed for
this planning document. Links identify where the follow-up audit should begin.

## 3. Workstreams and ownership

| Workstream | Owner | Deliverable | May proceed without |
| --- | --- | --- | --- |
| Connected Home artifact | Claude Home design agent | Clickable journeys grounded in Revision 3, with existing owner destinations reused or explicitly stubbed | Final API schema and every adjacent visual detail |
| Feasibility and implementation map | Home engineering lane | Current path traces, keep/adapt/add decisions, missing contracts, test plan, cost model | Final photography, polished copy, universal design-system agreement |
| Arrangement seam | Components and Plan lane | Intent/arrangement destination, contribution/edit distinction, retain/adopt behavior | Home's final section names or card shadows |
| Object seam | Entity lane | Canonical object identity, opening/return, supported contextual assistance | Home's composition schedule |
| Intake/continuity seam | Contribution and Capture plus Life lanes | Ask/Bring boundary, retained original/interpretation, exact record destination and repair | Completed Home prototype |
| Integration decisions | This orchestration task + founder | A small decision register and whole-journey review | Routine component choices, copy changes, internal refactors in owned lanes |

No automatic messages or assignments are implied. When execution is requested,
give each lane its bounded assignment and the same fixture/journey identifiers.
Use isolated worktrees for overlapping code changes; explicitly stage owned
files and follow each repository's instructions.

## 4. Sequence and dependency gates

| Package | Work | Depends on | Completion evidence |
| --- | --- | --- | --- |
| P0 — Baseline and shared fixture | Preserve Revision 3, apply two remaining corrections, define one consistent world and shared references | This plan | Named baseline, fixture/source manifest, gesture/destination table |
| P1-D — Connected design | Compose and connect J1–J4 using the same owners and fixture | P0 | Runnable artifact, complete interactions and meaningful alternative states |
| P1-E — Engineering feasibility | Trace J1–J4 through current code and classify production | P0; runs alongside P1-D | Evidence-linked implementation map, unknowns and seam decisions |
| P2 — Integration review | Reconcile design and code findings; resolve only shared seams | First complete P1-D/P1-E drafts | Recommended coherent experience; bounded deltas accepted or assigned |
| P3 — Implementation-ready handback | Finalize scoped packages, interface changes, tests, rollout/rollback plan | P2 | Design-to-code matrix with explicit dependencies; founder decision on implementation |

Use these gates rather than an artificial 48-hour freeze. Design and engineering
can exchange early findings before their drafts are complete. A missing deep
destination may remain a labeled prototype stub while its owner resolves it;
do not call that journey fully connected or implementation-ready yet.

## 5. P0 — establish the shared specimen

### Two corrections, then hold the composition steady

- Remove hollow circles that resemble radio buttons from alternatives. Keep
  the option titles, grouping, and meaningful opening behavior; reading an option
  does not select or schedule it.
- Correct H5's causal cooking headline. A photograph may suggest an integrated
  finish; it does not establish what that kitchen did. Give useful practical
  advice without turning a hypothesis into a known cause.

These do not require reopening the whole card/type system. Revision 3 remains
a working reference, not formally promoted design authority or public readiness.

### One fixture world, two account states

Use a consistent ordinary New York week with one supplied commitment, one loose
afternoon, one shared arrangement, and two differently scoped human contributions.
Use a separate new-account state for onboarding, then a controlled transition
after one contribution. Reuse the same relevant places and objects across paths.

Assign fixture identifiers to person, Source, Place, option, arrangement,
commitment, share, and generated result as applicable. These are test identities,
not a new production schema. Explicitly mark absent owners rather than inventing
backend objects to fill the manifest.

For each source record: origin/URL or supplied file, rights/permission, relevant
date/time, viewer scope, supported claim, and whether it is real, simulated, or
demonstration-only. Request founder-supplied private photographs if needed;
otherwise use licensed material clearly labeled as an illustration. Never
present stock imagery as Maya's actual photograph or real people as participants.

Replace especially prominent placeholders first: the human share, selected
place, and sample ticket. Ground one useful explanatory item and one practical
fact. A fake four-degree street prediction is not a requirement; omit exact
precision if the available evidence does not support it. Do not start a city
content factory or commission new data integrations for this specimen.

## 6. Four connected journeys

### J1 — a possibility becomes inspectable, not automatically a plan

**Start:** a complete Home option, such as an afternoon around a place.

1. Tap the option; inspect its actual shape and useful context.
2. Open a Place or entity without losing the originating option.
3. Inspect an alternative or ask a contextual question; return an answer or
   preview without changing what is kept or planned.
4. Optionally keep the idea through an explicit gesture. If retaining a loose
   intention is not yet supported, mark the seam; do not silently create a Plan
   or substitute a different kind of save.
5. Return to Home with the correct option and position when still valid.
6. On later entry, distinguish a kept possibility from an adopted arrangement.

**Alternative states:** simply leave without keeping; Place data unavailable;
conditions change while the detail is open; correction invalidates the suggestion.

**Owners:** Home for selection; Places/entity for spatial/object depth; Plan/Life
for the agreed retention semantics. No second Home-owned arrangement store.

**Pass:** the user can explore without commitment and later find exactly what
they intentionally retained. Retain, adopt, and participate remain distinct.

### J2 — a friend's contribution delivers value before social work

**Start:** Maya's authorized original or Dana's addressed contribution on Home.

1. Enjoy the actual words/media without opening a conversation.
2. Inspect the original and its relevant Place context; preserve attribution.
3. Browse more deliberately shared material through the agreed destination.
4. Optionally respond or use it in an arrangement. Show the destination audience
   before sending; reading or private saving is not permission to widen sharing.
5. Return to the same Home context or its honest recomposition.

**Alternative states:** ignore with no debt; original expires or is withdrawn
while open; source retained privately but not authorized for group reuse.

**Owners:** share/source and entity owners; Life People for durable relationship
records; arrangement owner for shared use. A present-tense browse surface remains
a separate explicit decision, not something this prototype silently installs.

**Pass:** social consumption is complete without responding; intentional browsing
is discoverable; no stale quote or derivative survives lost access.

### J3 — an arrangement opens into the same shared truth

**Start:** an arrangement card or justified change on Home.

1. Open the existing Plans-in-Real-Life arrangement composition, not an unrelated
   Chat thread or new Home detail workspace.
2. Inspect useful context before being offered editing controls. Reuse the
   destination lane's contextual Ask Vesper direction where appropriate.
3. Add an attributed suggestion as a contributor; it does not change accepted
   arrangements or become a task the owner must review.
4. In a separate authorized-editor/owner branch, make a bounded change. Where
   another person's commitment or external effect is affected, show the actual
   consequence boundary rather than a universal confirmation for every edit.
5. Read back the owner's accepted state; return to Home with the material change.
6. Reopen as another participant and show that the shared fact agrees while
   private context and available actions remain viewer-specific.

**Alternative states:** dismissal; permission changes while open; concurrent
edit makes the proposal stale; offline submission never appears committed;
participant leaves or attends only part without cancelling everyone else's plan.

**Owners:** Plan/Occasion and command owners, with Home consuming projections.
External reservations remain externally controlled; no booking/rebooking UI.

**Pass:** contribution, editing, agreement, and attendance are distinguishable,
and all surfaces refer to the same accepted consequence.

### J4 — a sample leads to immediate value and appropriate continuity

**Start:** new-account Home with a labeled, prepared demonstration and modest
nonpersonal value; no assumed workplace, location, friendship, or history.

1. Inspect the demonstration; nothing personal is written.
2. Choose Try with yours; open the existing capture/Chat boundary with useful
   intent and return context, not a new composer designed in the Home lane.
3. Deliberately bring a ticket, or ask about it without requesting retention.
   Show the two meanings where the actual gesture differs; attachment alone
   must not imply a durable memory write.
4. Receive an immediate useful result. For clear authorized Bring, show the
   scoped receipt and Undo after value; for answer-only, avoid a fake kept state.
5. Return to Home and see the relevant real result, not a permanent setup task.
6. Open the exact retained original/record in Life when retention occurred.
7. Reopen later with no new input; retain useful world value and do not infer
   event attendance, enjoyment, or a permanent preference from the ticket.

**Alternative states:** cancel intake; ambiguous date/venue; extraction pending;
answer available but durable interpretation pending; source failure; Undo or
correction. Preserve what was actually accepted and do not fabricate completion.

**Owners:** Capture/Chat, retained Source/intake, Life record, Home projection.
Use [Contribution and Consequence](../systems/contribution-and-consequence.md)
for Ask/Bring, T0/T1/T2, owner readback, and causal repair.

**Pass:** one deliberate contribution yields a concrete benefit without another
assignment, and the user can find or undo the correct retained material.

## 7. Shared interaction contract — specify before polishing transitions

For every meaningful control, record outside the phone:

`origin unit → user intent → target owner/ref → read or command → visible result
→ persistence/audience effect → return behavior → failure behavior`

Do not prescribe new DTOs in the design artifact. Engineering should map these
semantics onto existing typed destinations, ResourceRefs, actions, and receipts.

Default interaction principles:

- Cards/options open understanding; they do not silently select, save, or act.
- Ask Vesper is contextual assistance, not a separate assistant identity or a
  mandatory detour for every object action.
- Private discussion and a message to other people are distinguishable before
  sending. Do not append private context to an unrelated existing conversation.
- Back restores the originating item when still valid; changed/withdrawn data
  causes honest recomposition, not forced resurrection. Define a graceful root
  fallback after restart or expired return context.
- A request in progress, a preview, and an owner-confirmed result are visibly
  different; dismissing a preview changes nothing.

Prototype these transitions with shared fixture state and stable object IDs.
Scripted behavior is acceptable when labeled; do not imply arbitrary natural
language understanding. Unsupported requests preserve the words and show an
honest limitation rather than silently accepting them.

## 8. P1-E — engineering feasibility work package

Produce one matrix, not four disconnected architecture essays. For each step
in J1–J4, trace the rendered control through destination/action handling, route,
data hook, API operation, owner read or command, and resulting projection.

Each row must include:

- Current file/symbol and operation evidence, with repository commit.
- Status: **present and verified**, **present but unverified**, **adapt**,
  **missing**, or **blocked on owner decision**.
- Keep/adapt/remove/add recommendation and why reuse is or is not sufficient.
- Read/write authority, relevant source and revision, audience, refresh signal,
  resulting owner, return behavior, and missing tests.
- The accountable lane and the exact dependency it needs—not “wait for Life.”

Investigate these seams specifically:

1. **Destination precision:** generic Chat or Life-root fallback versus exact
   arrangement, contribution, and retained-record opening. Inspect actual call
   sites before changing shared routing globally.
2. **Loose retention:** preserve a possibility without requiring a named Plan;
   coordinate with the Plan/Life storage decision instead of inventing a store.
3. **Shared originals:** authorized source/media retrieval and a discoverable
   browse destination, including withdrawal of derivatives.
4. **Contextual assistance:** target identity, private/shared channel, and Chat
   continuation ownership. Consume the adjacent pattern, do not implement another
   conversation system inside Home.
5. **Owner readback:** contribution versus accepted edit and Home refresh after
   a change; handle stale revisions and duplicate submission.
6. **Intake continuity:** original, extraction/interpretation, Life record, and
   Home result can become ready at different times; no “all done” fiction.
7. **Return:** test current in-memory behavior and choose a minimal restart/expiry
   fallback; persistence of navigation is not a prerequisite for durable artifacts.
8. **Composition fit:** map R3's cards, alternatives, rows, and media onto current
   renderer families; do not let fixtures force a parallel envelope or client ranker.

### Production and economic feasibility

Trace two scenarios: an unchanged repeat open and a meaningful source change.
Count root reads, source/provider calls, model invocations, retries, and cache
or stored-result hits separately. An HTTP refetch does not itself prove model
work; an apparently cached card does not prove its upstream inputs are free.

Use three measurements/states: cold result creation, unchanged reuse, and
incremental refresh. Include personalized synthesis and the no-new-generation
fallback. Where no instrumentation exists, propose it; do not report estimates
as measurements or run paid experiments without authorization.

The planning cost model is:

`period cost = new-result processing + incremental refresh + retrieval/provider
usage + media/storage delivery`, including retries and shared costs apportioned
by actual reuse. Benchmark latency and useful-result yield alongside cost.

Do not create a city-wide mechanism library, new model registry, or always-on
research scheduler just to satisfy the prototype. Reuse existing content paths
where appropriate and record what remains unavailable.

## 9. What can proceed, and what needs coordination

**Proceed locally:** card composition, grounded examples, navigation stubs,
read-only path audit, media preparation with permitted sources, semantic fixture
IDs, return-state sketches, and testing plans.

**Coordinate before implementing:**

| Decision | Recommended starting position | Decision owner |
| --- | --- | --- |
| What does Keep retain? | Exact source/possibility, not an automatic Plan; distinguish keep from adopt | Plan + Life + Capture |
| Where does an arrangement open? | Canonical arrangement destination, not generic Chat | Plan + Home navigation |
| Where is Everything shared with you? | Reuse Life People if it genuinely serves the browsing intent; label any present-tense extension | Life + Home + founder |
| What owns an in-object assistant exchange? | Same assistant, preserved target and channel; no duplicate history owner | Chat/Capture + Plan/Entity |
| What happens on return after changes? | Revalidate; restore exactly if valid, otherwise preserve orientation without stale content | Home + destination owners |
| What justifies generation or a refresh? | Source/consequence change or explicit exploration, not automatic rewriting on open | Home/backend production |

A lane can continue with an explicitly provisional interface while a seam is
resolved. Do not call its dependent behavior complete until that decision and
integration are checked. No requirement for every design lane to settle first.

## 10. Completion and verification

### Design artifact completion

- J1–J4 are navigable, not a sequence of unrelated screenshots.
- Every prominent control has a defined outcome; any unimplemented branch is
  labeled in research chrome and listed as a limitation.
- Same objects remain recognizable across roots, with correct viewer context.
- Normal phone width and larger-text screens are inspected; no tiny metadata
  or clipped controls used to make the scroll look shorter.
- A no-action visit is satisfying; extended use remains optional.
- Real/simulated content and private/sample identities are distinguishable.
- Withdrawal, changed facts, cancellation, and unavailable depth are shown.

### Engineering feasibility completion

- All four journey traces have evidence-backed dispositions and owners.
- Shared decisions have a recommended answer or a precise unresolved dependency.
- Each proposed implementation package has tests, dependencies, and rollback scope.
- Economic assumptions distinguish measured, estimated, and unknown values.
- No prototype behavior is called shipped merely because a similar code path exists.

### Later implementation verification — not performed by this plan

Reuse current frontend tests for HomeRootExperience, rootProjectionNavigation,
rootProjectionReturnRegistry, root consequence confirmation, and Life records;
extend them for the new exact routes and state transitions. Add owner/contract
tests for the affected backend operations, authority, source correction, and
idempotency. Run local tests in proportion to the changes.

Backend API changes require workspace `scripts/sync-types.sh`, snapshot review,
generated mobile types, and typecheck. Do not hand-maintain duplicate schemas.
Native intent validation follows the mobile repository's registered surface
workflow. Check/promote design references through the applicable authority
process; Downloads files alone are not canonical native test references.
Keep rollout gates and compatibility paths until explicit acceptance; no public
flag change or booking restoration is part of this phase.

## 11. Implementation handback structure

P3 should propose dependency-ordered packages covering the system:

1. **Shared navigation and owner contracts:** exact destinations, context,
   retention decision, and readback/return semantics needed across J1–J4.
2. **Home presentation adaptation:** reuse the renderer and components for R3;
   keep domain data and ranking out of layout code.
3. **Owner integrations:** retain/read, contribution, arrangement action,
   intake-to-Life, and Home refresh through the relevant lanes.
4. **Production lifecycle:** reuse, invalidation, bounded generation, source
   freshness, and useful degraded composition with cost/latency observation.
5. **Whole-journey verification and controlled rollout:** all four paths plus
   changed/withdrawn/offline/thin states, native evidence, and rollback rehearsal.

Do not promise exact package boundaries before P1-E exposes the actual gaps.
Independent owner integrations may proceed concurrently once their interfaces
are clear; packages are not permission to rewrite the repository.

## 12. Founder and orchestration cadence

The founder should review **one complete draft spanning all four journeys**,
then one corrected integration pass. Bring explicit seam decisions rather than
daily galleries of new cards. Routine visual refinements stay in Claude Design;
owner internals stay with their lanes.

This task maintains the joint decision register and asks three questions:

1. Does the same product remain recognizable before and after each transition?
2. Are we reusing owner truth and infrastructure rather than multiplying systems?
3. Is each remaining gap a design decision, engineering implementation, content
   supply issue, or validation need—and who owns the next action?

The next implementation decision is made from the connected artifact and code
map together. Neither a beautiful prototype nor an extensive backend is enough
to substitute for the other.
