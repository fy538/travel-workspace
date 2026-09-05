---
doc_type: working
status: active
owner: founder / product / design / Components and Plan
created: 2026-09-04
last_verified: 2026-09-05
expires: 2026-10-04
why_new: Gives Claude Code and Claude Design a composition-led visual exploration brief that reconciles the September 4 arrangements discussion, consumer research, and the existing editorial itinerary instead of replacing it with an operational status dashboard.
supersedes: []
source_of_truth_for: []
---

# Claude Code → Claude Design handover: Vesper — Plans in Real Life

## 0. Start here

**Current assignment — September 5, connected-journey refinement:** continue the existing **Vesper — Plans in Real Life** project. Read §0.4 first: the new board 09 substantially advances §0.3's journey brief. Preserve its value-first visits, natural follow-up, and explicit social sharing; refine intent-aware adaptation, remove process-heavy customer copy, and make the prototype demonstrate the recovery it illustrates. §0.1–0.3 retain the contraction, assistance-first, and consequence requirements; older defect descriptions are historical where §0.4 records a correction. Do not create another project, expand the operation-screen inventory, or implement production changes for this revision.

This is a **design exploration**, not production implementation, a schema decision, or a new app-wide design system. The original handover preceded project creation; the subsequent [execution report](claude-design-plans-in-real-life-execution-report-2026-09-04.md) records the existing [Plans in Real Life project](https://claude.ai/design/p/cd2e1f82-9786-4ae6-993e-c0dfbe8d6302). The reviewed local export is `/Users/feihuyan/Downloads/vesper-plans-in-real-life/project`. Inspect the current live version before syncing; this revision does not independently certify that it matches the export. Do not invent integration commands or claim a sync succeeded without checking the live project.

The receiving agent is expected to investigate detailed code and design language, not just implement a written sketch. This brief gives a starting position and boundaries, **not an exact final wireframe**. Exercise design judgment over composition, spatial relationships, hierarchy, and interaction.

### The central brief

> Preserve the pleasure and clarity of our editorial itinerary while expanding it to support loosely imagined, personally shaped, shared, and changing real-world plans. Reduce the work of maintaining the experience without removing the reassurance of seeing it clearly.

Working design description: **a readable editorial plan, with Vesper available to help understand, explore, and adapt what is ahead**. This is a description of the experience, not a required customer-facing label or a proposal for generic document infrastructure. “Act on” does not mean making every field or relationship independently editable.

The outcome should let a person feel: “I can see something worth doing; it fits together; I know what matters; and I can change it without managing a system.”

### 0.1 Review revision: do not turn the readable plan into an operations console

**Provenance and precedence.** This section incorporates the founder's review of the exported A3 “Direct adjustment” and B4 “Inspect and move” boards, followed by the objection that making the plan a “directly manipulable object” recreates too many operations. It supersedes the earlier recommendation to make all relevant properties directly editable. It governs this design exploration; it does not amend accepted backend authority contracts or certify a tested interaction model.

**The revised direction:** the plan is primarily for understanding, anticipation, and coordination. Contextual Vesper interaction supports questions, exploration, and changes; it is not an editing-only assistant. Direct controls are selective conveniences when the choice is already clear—not a comprehensive editing vocabulary. A complete underlying system does not require a complete visible operations console. §0.2 refines how this should appear after reviewing the first implementation of this direction.

#### A. Readable plan, contextual request—not a second chat product

- Preserve the continuous editorial resting page. Do not expose an editor toolbar, independently tappable field system, scheduling form suite, or permission dashboard by default.
- Provide a discoverable, lightweight way to ask about or change the current plan or selected stop. Prefer a recognizable contextual Vesper entry over a dominant editing-only “Change something…” prompt; recommend placement and final copy under §0.2. Carry the selected target into the interaction so the person does not have to restate it.
- Do not require a persistent composer under every plan. The export's A2/A4 composer and user bubbles are a proposal, not a settled requirement. Recommend one contextual entry/expansion pattern that preserves reading space and works with text as well as optional voice.
- A short request may resolve in context. Once resolved, the page shows the current arrangement; transient conversation and acknowledgments do not accumulate into its normal reading surface. This is presentation cleanup, not deletion of history or loss of repair access.
- Longer discussion can continue in Chat with the relevant object and unresolved intent carried along. Specify the handoff and return behavior; coordinate thread/history ownership with the Chat lane rather than inventing a second conversation store here.
- Private assistance and shared discussion must be distinguishable before submission. “Ask Vesper” stays private for owners, editors, and contributors alike; editing rights must not switch its audience. A deliberately opened shared discussion remains shared, and its comments do not silently edit the arrangement. Resolve the entry's meaning visibly without redesigning the Chat root.

#### B. A3: finite performance choices are useful; invented time flexibility is not

The fixture has performances at 8:30 and 10:30. Choosing one of those can remain a compact direct action: it is a real bounded choice, not an arbitrary restriction. Keep the practical fit explanation and the ability to leave the option loose. Do not build a general schedule editor around it.

But “I want to go at 10” might mean **arrive at 10 for the 10:30 set**, not change the performance time. Let a contextual request express that distinction. Ask a short clarification only when the intent cannot be safely resolved. Never invent a 10:00 performance or silently alter provider facts. Keep the arrival intention and performance time distinct in meaning, but do not require separate rows: one jazz entry can say “Aim to arrive at 10 · late set starts 10:30.” Surface departure guidance when useful rather than automatically manufacturing another planning element.

#### C. B4: suggestions are shortcuts, not the limits of the product

The first reviewed sheet offered 11:00, Tuesday morning, and Skip. Unlike the jazz performances, these are not an exhaustive set of real-world choices. Keep a suggested move only when it delivers useful judgment in response to an intention or relevant problem; tapping a place alone is not a request to move or remove it. Do not generate a larger menu containing every day/time combination.

The primary general-purpose continuation should accept a scoped request such as “Wednesday at 10” or “Wednesday morning; leave the time open.” Preserve the requested precision. Do not require a date picker, a time picker, a confirmation, and a receipt screen for every adjustment. A picker may be offered within the interaction when it genuinely helps someone choose, but is not the default architecture or a mandatory step.

The first reviewed Tuesday option also implied taking the train on Tuesday. That expands a stop adjustment into moving an outing and touches a Monday seat reservation. If that scope is unresolved and matters, ask one specific question—for example, whether the person means the temple visit or the Nara outing. Do not silently move dependent items, invent a compatible train, or claim a reservation changed. Deliver any known practical implication alongside the question; do not hand the whole dependency analysis back as homework.

#### D. A small action vocabulary, not a hidden command-language exam

Obvious actions such as choosing an available set, keeping an option, joining dinner, or adopting a shown alternative can remain direct. The criterion is that the action is easier to understand and perform than describing it—not that every backend operation deserves a button. Exact wording should not be required for a language request.

The half-sheet itself is not rejected. Use the existing overlay language for a focused inspection or contextual exchange when appropriate. Avoid a sheet that doubles as place detail, scheduling editor, action catalog, and group discussion. Do not replace it with a permanent collection of operation-specific screens.

Keep control of the result legible: what the request targets, what actually changed, and how to correct it. Preserve the user's words and current state if interpretation fails. Never make unsupported input look successful. An optional structured aid is preferable to forcing repeated rephrasing, but do not solve prototype limitations by exposing a full editor.

#### E. The system owns complexity; authority does not disappear

Language and buttons resolve through the same existing owner and authority boundaries. A clear, authorized, private reversible instruction may apply with quiet readback and truthful Undo; it does not need a proposal ceremony just because it arrived as language. Exploration such as “could we make this less rushed?” can return a useful alternative without applying it. Consequential ambiguity requires clarification; material effects require the appropriate boundary, not a blanket confirmation for every edit.

Owner-only editing remains the default, with owner-controlled scoped grants. An authorized collaborator's ordinary in-scope edit does not require redundant owner approval. A non-editor can contribute or suggest without changing the plan. Editing an arrangement does not change another person's attendance or consent, and an edit grant does not authorize autonomous AI changes. “I'm skipping this” must not become cancellation for everyone. Imported reservations and external provider actions remain separate.

#### F. Required next revision and stress cases

Revise A3, B4, the A2/A4 resting-to-request-to-result transition, and board 07's “Read vs act” recommendation. Check C/D and the interactive prototype for the same assumptions; adapt the shared pattern without starting another full composition redesign. Preserve the typography, paper, time gutter, density, and complete-day overview specified below.

Demonstrate these cases through the same small interaction family, not one bespoke operation screen per case:

1. “Arrive at 10 for the 10:30 show”: arrival and performance remain different facts.
2. “Move this visit to Wednesday at 10”: the requested day/time is expressible, with any consequential ambiguity resolved rather than silently guessed.
3. “Wednesday morning, but don't pin down a time”: no fabricated exact timestamp.
4. “Move the whole Nara outing, not just the temple”: show the actual scope and unchanged reservation boundary.
5. “I'm skipping this; everyone else can still go”: personal participation, not a shared deletion.
6. The same request from an owner, an authorized editor, and a contributor: preserve the different effects without three permission workflows.

Show at least one simple request resolving without a preview, one exploratory alternative, and one necessary clarification. Include dismissal without mutation, a failed/unsupported request, and re-entry after success. Research annotations may explain internal mechanics; the customer surface should not.

The inspected Saturday prototype uses scripted recognizers and selected outcomes; it does not demonstrate arbitrary date/time understanding. Label that limitation and do not count additional hard-coded phrases as validation of a general-purpose interpreter.

Return one recommended pattern with resting, active, and resolved states, plus a short account of controls and ceremonies removed or retained. The success criterion is **less work to express and achieve an intention while retaining a dependable overview**—not minimum button count, maximum conversational turns, or the illusion of flexibility from three curated choices.

### 0.2 Second export review: assistance first, not editing first

**Evidence and scope.** This section records the second export review, before the subsequent export addressed most of these corrections. That review inspected revised A3/B4, board `08 Contextual Request - Resting, Active, Resolved`, shared scenarios, and scripted prototype sources, and rendered board 08's resting page and active sheet. It did not verify the live Claude project, arbitrary language interpretation, or native behavior. These requirements supersede narrower presentation guidance in §0.1 where necessary, not accepted authority contracts. See §0.4 for the current baseline and next assignment.

**Keep the progress:** no permanent composer or accumulated user bubbles on resting plans; one contextual assistance family; actual jazz-set choices; exact and loose timing; personal participation distinct from shared deletion; the readable editorial itinerary. Do not restart the composition family.

> Open the plan to understand what's ahead. Open a stop to discover what matters about it. Ask Vesper in context when you want help—including changing things.

#### Required refinements to the current export

1. **P1/P2: one recognizable assistant, not several kinds of talking.** The header's ASK, floating “Change something…” pill, and “Continue in Chat” currently divide one capability into competing entries. Recommend a coherent contextual Vesper entry and an optional expansion into the longer conversation. Do not mandate one physical button for the whole app; object context may justify local access. But users should not have to choose which assistant can answer versus edit. Test questions such as “Why is this temple worth visiting?”, “Would my mother enjoy this?” using only authorized context, and “Where could we have lunch nearby?” The entry must invite more than plan maintenance.

2. **B4/P2: inspection is value before adjustment.** Tapping Tōdai-ji should lead with useful recognition, place detail, or relevant practical context—not immediately offer “11:00 instead” and “Skip it.” Keep contextual assistance available in that same surface; do not create a second mandatory inspection screen. Scheduling shortcuts should follow expressed intent or a real relevant problem. Retain A3's genuinely bounded set choices where appropriate, rather than applying a universal no-buttons rule.

3. **P9a: keep private assistance stable across roles.** Do not open the same Vesper entry privately for an owner but in shared-suggestion mode for a contributor. Someone without edit rights can explore privately and then explicitly choose to send a suggestion to the named people. An expressly opened shared-discussion door can start shared. Make the eventual effect legible without requiring a permissions workflow or redundant owner approval for an already authorized editor. Rights constrain mutations; they do not select the audience of an otherwise identical private ask.

4. **P7: two facts need not mean two rows.** Compose arrival and performance together in one jazz entry when that is clearer. Separate timing semantics underneath do not require a separate “Arrive at Corner Note” object on the reading surface, plus a departure connector, plus the show. Expand the timing detail when useful. This corrects an overly literal reading of §0.1's earlier “separately” wording, not the distinction between user intention and provider fact.

5. **P3–P6: show ordinary flexibility as well as the difficult case.** Keep the Wednesday airport-train conflict and the outing-scope question as useful stress cases. Also show “Wednesday at 10” succeeding directly in a separately labeled, internally consistent fixture where it is unambiguous, authorized, and compatible with the rest of the plan. Do not solve this by deleting the departure fact from the existing conflict fixture. The simple case should end in a localized result and truthful recovery, not another sequence of conversational hurdles. Clarifications are conditional consequences, not required stages in the interaction template.

6. **P10/P11: deliver the supported value without a compulsory Chat transfer.** Vesper does not book hotels, but a request for one can receive the useful supported part—relevant accommodation options and external booking links—in context. State the execution boundary briefly; do not stop at a refusal plus navigation when the answer can be useful here. Expand into Chat for space or continuity when warranted or chosen, not because the contextual assistant is arbitrarily less capable. Distinguish a prototype recognizer's limitation from the product's genuine booking-execution boundary. Do not fabricate retrieval results to demonstrate this; use clearly labeled fixtures.

#### Revision delivery and acceptance

- Update A3/B4 and the affected P1/P2/P3–P7/P9a/P10/P11 examples through the same small family. Check C/D and board 10 for inconsistent entry, audience, or result behavior; do not build a new screen for every question above.
- Include a read-only question delivering useful substance without a mutation or receipt, one ordinary change, one necessary clarification, and private exploration by a contributor followed by optional explicit sharing. Show dismissal and return to the same clean plan.
- Update board 07's recommendation **and reuse/contraction map**. The reviewed map still says `PlanStopInspectSheet → the three-move sheet`, which contradicts the revised boards. Remove stale claims that B4 merely hides a picker or that every stop should open an adjustment sheet.
- Preserve the existing type/material language and dependable overview. Do not equate richer understanding with more rows, more disclaimers, or more user work.
- Board 10 still uses scripted recognizers; its Chat continuation is unimplemented in the reviewed export. Record what is illustrated versus mechanically demonstrated. Additional hard-coded phrases do not establish general language support, and a static handoff frame is not a working cross-surface continuation.

**Review standard:** the person can receive value without changing anything, express a change without discovering an operation, and stay oriented about audience and result. The next revision is about removing the editing-first posture—not reopening the full itinerary redesign.

### 0.3 Research-backed journey review: reduce the work between the screens

**Assessment at this review stage.** The export reviewed before board 09 had one Ask Vesper entry, value-first stop inspection, a read-only answer, an ordinary successful Wednesday move in fixture B′, one composed jazz entry, private contributor exploration followed by explicit sharing, and accommodation options delivered in context. Board 07's reuse map agreed with that direction. Preserve these corrections. The concern was no longer principally the screen taxonomy: we may have reduced visible operations while shifting work into prompting, interpretation, checking, recovery, and social coordination. See §0.4 for the subsequent journey-board review and current assignment.

**Evidence limits.** The source and rendered-canvas review plus the online research below inform a hypothetical user walkthrough. No participants were observed using Vesper, and no native usability verdict is claimed. Distinguish observed design/code inconsistencies from predicted friction. Findings from older mobile studies, general AI research, and language-model evaluations are not direct validation of this product.

#### Journey requirements

**1. Open the plan: receive orientation before needing a prompt.** A Sunday-evening browse and a Monday-morning departure are different visits to the same plan. Preserve the stable editorial overview, but let a small contextually justified line elevate the next useful fact, such as the exact departure/platform already supported by the fixture. A leave-by suggestion requires adequate location, timing, and route evidence; do not invent precision or an ambient-monitoring promise. No new live dashboard, wholesale reorder, or always-dominant crown card is required. A useful glance and exit is a successful journey.

**2. Inspect a stop: translate information into an experience.** Keep P2's value-first composition. Where context supports it, go beyond a generic guidebook summary: what is worthwhile on a short visit, what effort it involves, or what the person can reasonably leave out. Select what matters rather than adding all of these as mandatory fields. The founder's Rome-in-the-heat story is a useful stress case: understanding a place must not become cultural homework. Let the user read and close without an obligatory Keep, review, or planning action.

**3. Ask: reduce the briefing burden.** Name the selected target. Briefly expose the relevant remembered context when it materially shapes the answer, without a biography or an authority disclaimer wall. If the mother's preferences in P2b are not available, give a useful conditional answer or ask only for information needed to resolve a consequential uncertainty. Do not force a profile questionnaire. Contextual example questions may help discoverability, but are optional aids rather than a command vocabulary or a prompt carousel every time.

**4. Follow up: active assistance is not the resting plan.** P2b replaces the field with answer-specific buttons and “Something else…”. Make it easy to continue with words such as “She's fine walking; it's crowds she dislikes” without navigating an escape branch. Keep lightweight text/optional voice access during the active exchange; remove persistent conversation chrome when returning to the plan. Lead answers with the useful judgment and main qualification rather than packing every alternative into a paragraph. Distinguish correcting the current answer, correcting an enduring memory, and changing the plan: the same input surface does not imply the same mutation. A situational correction must not silently become a durable preference.

**5. Change: make execution and its result understandable.** Retain P6b's low-ceremony success path. Also cover a slow response, failed execution, repeated submit, interrupted execution, and another person's intervening change. Keep the request and target available during latency; do not present a proposed edit as accepted owner state. Disable duplicate submission or otherwise prevent duplicate effects. Read back the smallest relevant result with supported recovery, keeping unrelated content stable. If the moved stop is offscreen, expose a way to see its destination without a disorienting automatic jump. Clarify genuine scope uncertainty; do not reconfirm an already clear, authorized private reversible instruction merely because it used language. A submitted request whose outcome is unknown must be reconciled before offering retry as if nothing happened.

**6. Interrupt and resume: a clean plan must not be amnesiac.** Define the difference between closing a read-only answer, leaving an unsent draft, dismissing an unadopted alternative, and leaving after an accepted change. Preserve unfinished work only within its authorized custody/retention scope; do not silently create a durable artifact or personal claim to achieve resume. Reopening should recover the relevant target and unfinished exchange where allowed, not require restating everything. Accepted changes remain accepted; merely closing a sheet does not undo them. Where drafts expire or are deliberately discarded, make that behavior understandable. Show return from Maps, an external provider page, and app backgrounding using the same rules.

The half-sheet is an entry treatment, not a rigid container for all future activity. Show keyboard-open, expanded, scrolled, and dismissed states. Provide an accessible visible close control and platform-appropriate Back behavior. Avoid nested sheets; let the current surface expand or continue into the existing conversation when warranted. Do not create a separate route/editor per operation. The actual native keyboard and navigation behavior remain to be verified later.

**7. Coordinate: preserve the sender's meaning through the recipient's view.** Show the exact outgoing authored suggestion or proposed wording and named recipients next to the explicit send; no separate compulsory wizard is needed. Do not silently paraphrase a casual comment into an official plan change. An optional contribution may simply enrich the experience; the recipient need not process it as a pending decision. Retain ordinary authorized editing without redundant owner approval and independent participation/Commitment boundaries.

#### Inconsistencies recorded at this review stage — see §0.4 for resolution status

- **P9a → P9b:** the sender example discusses 4:00, but the receiver shows Dana suggesting 4:30. Preserve the exact suggestion through one connected journey, or label separate events explicitly. It is not evidence of continuity as currently presented.
- **`kit/proto.js`, Maya dinner request:** the bookstore route offers a separate send, but `maya_ask8` directly sets the owner-facing request and receipt when reached from Maya's private language route. Apply the same private preparation/explicit send distinction there. This is a prototype inconsistency, not approval to change production policy or proof that the proposed model fails.
- **Board 10 fidelity:** the inspected assistance region is in document flow (`position: static`), the recognizers support selected outcomes, and value-first inspection, read-only answers, retrieval, and Chat continuation are not all mechanically implemented. Do not use its success claims to certify the illustrated half-sheet, keyboard handling, free-form continuation, or cross-surface journey. Either implement the bounded prototype behavior needed for the walkthrough or state exactly which parts are simulated.

#### Research basis and limits for this revision

- **Prompting can relocate effort rather than remove it.** CHI 2024 research synthesizes the demands of expressing goals, judging outputs, and choosing when to rely on generative AI. Our inference: audit mental work across the journey, not merely button/screen count. This is a research framework, not a Vesper trial. [Tankelevitch et al., The Metacognitive Demands and Opportunities of Generative AI](https://www.microsoft.com/en-us/research/publication/the-metacognitive-demands-and-opportunities-of-generative-ai/).
- **Relevant timing, understandable capability, and efficient correction matter.** Microsoft's CHI 2019 guidelines were evaluated with design practitioners across AI products. They support contextually timed help and easy invocation, dismissal, and correction; they do not prescribe a particular sheet or prove our composition works. [Human–AI interaction guidelines](https://www.microsoft.com/en-us/research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/).
- **Overlays have a recovery and orientation cost.** NN/G reports mobile usability problems with ambiguous dismissal, lost position/work, and stacked overlays. Its guidance favors clear dismissal and short contextual interactions. Our inference: preserve resume, test Back and keyboard behavior, and do not force long multi-step exploration into nested half-sheets. These are general mobile findings, not evidence that every Vesper sheet is inappropriate. [Bottom sheets](https://www.nngroup.com/articles/bottom-sheet/), [Accidental overlay dismissal](https://www.nngroup.com/articles/accidental-overlay-dismissal/).
- **Clarification needs multi-turn evaluation.** Google's ICLR 2025 work evaluates models' selection of conversational actions in information-seeking tasks. It reinforces the need to evaluate when to clarify rather than guess; it does not establish an ideal number of questions for travel or validate automatic plan mutations. [Learning to Clarify](https://research.google/blog/learning-to-clarify-multi-turn-conversations-with-action-based-contrastive-self-training/).

#### The next deliverable: three connected journeys, not more disconnected screens

1. **Receive value without doing anything:** open a plan in a relevant moment → inspect a stop → understand something useful → close. No required prompt, save, or receipt.
2. **Ask, correct, and adapt:** inspect → ask → follow up freely → request a change → encounter an interruption or bounded failure → return to the correct state. Include an ordinary successful path as well as the adverse case; do not force every user through a clarification.
3. **Explore privately, coordinate explicitly:** contributor asks privately → sees the actual proposed message → optionally sends → recipient sees the same contribution → recipient may adopt or leave it → sender can understand the outcome without a new status dashboard. Include an authorized editor contrast without repeating an entire permission workflow.

Use these journeys to expose the remaining design decisions across the family, not as a narrow product-proof gate that delays the rest of the architecture. Reuse the existing designs, fixtures, materials, and small set of interaction patterns. Keep simulation controls and failure injection outside customer frames. Leave production implementation and changes to adjacent Chat/Entity ownership contracts out of this assignment.

For subsequent formative sessions, give people goals rather than instructions to tap a named control. Observe whether they can find value without prompting, identify the request's target, continue naturally, explain what changed and who sees it, and resume without repeating themselves. Record hesitation, rephrasing, unintended exits, misunderstood outcomes, and recovery effort alongside completion—not just tap counts or preference ratings. Recruiting or running participant research is a later step, not something this handoff claims has happened.

Return the connected artifact, a concise journey-friction log, board/code inconsistencies fixed, and explicit illustrated-versus-tested limits. **Design for someone distracted, uncertain, changing their mind, and sharing a day with others—not only an articulate user who completes the scripted exchange uninterrupted.**

### 0.4 Connected-journey export review: preserve the intention, not just the schedule

**Evidence and precedence — September 5.** This review inspected the new `09 Journeys - Value, Adapt, Coordinate.dc.html`, the updated `10 Interactive - Saturday, Shared.dc.html`, and `kit/proto.js` in the local export, with rendered inspection of board 09. These are synthetic design fixtures and source-level findings, not observed participant behavior, verified travel facts, native testing, or certification of the live Claude project. This section updates the next assignment; it does not amend the [Contribution and Consequence contract](../systems/contribution-and-consequence.md), authorize production changes, or settle draft-storage architecture.

#### Preserve the progress; do not restart the family

- **J1: value without a request.** A departure visit elevates useful supported information; an evening visit can remain about anticipation. Stop inspection explains the experience and practical effort. Reading and closing is a complete successful visit, with no mandatory Keep or receipt.
- **J2: natural continuation.** The active field remains available for “She's fine walking; it's crowds she dislikes,” followed by a plan request. Preserve this without returning a permanent composer to the resting page.
- **J3: sender-to-recipient continuity.** The new journey carries the same 4:00 suggestion through private preparation, explicit send, and the recipient's view. This addresses the earlier inconsistency in the new journey; keep corresponding older examples consistent too. Ordinary authorized editing remains distinct from a contributor's suggestion.
- **Prototype correction:** `maya_ask8` now prepares privately and `maya:send_ask8` performs the explicit send. Preserve this fix; the older §0.3 defect is not still outstanding in the inspected code.

#### A. J2f: temporal compatibility is not experiential compatibility

The exchange recommends visiting before 11 because the user's mother dislikes crowds. The user then asks to add Isuien afterward, around noon. While the user is away, Ben moves Tōdai-ji to 11; the design shifts Isuien to 12:30 and describes the changes as composed without conflict. The times may fit, but the new arrangement defeats the stated reason for going early. Its receipt also says “around noon” while its detail says 12:30.

Revise this journey so Vesper notices the changed experience, not merely the next available slot. Illustrative private copy, using the fixture's assumptions:

> Ben moved the temple to 11—the busier time we were trying to avoid. Isuien still fits afterward.

Pair that observation with useful help, such as exploring a quieter order, rather than a generic conflict warning. Show one coherent branch with an unambiguous state: either the requested addition remains unapplied while a material mismatch is resolved, or a permissible applied result is read back accurately with the changed tradeoff. Do not claim both “added around noon” and an unexplained substituted time. Do not present every small timing adjustment as material; use the expressed purpose, requested precision, dependencies, and actual authority to determine significance.

Ben's authorized edit remains his edit. Vesper must not silently reverse it, move the whole outing, or disclose the mother's private preference in a shared explanation. A relevant constraint does not itself authorize an autonomous mutation or a new audience. “Undo mine” must preserve independent edits. No new conflict dashboard, approval queue, or universal confirmation ceremony is required.

**Design principle:** preserve the purpose that made an arrangement useful, within its authorized scope—not only its chronological validity. This is current-context reasoning, not permission to infer an enduring personality or preference.

#### B. Keep system mechanics out of ordinary customer copy

- **J2b memory prompt:** remove the routine “Remember this about her?” offer after an ordinary situational correction. Use the correction within authorized current context; do not silently promote it into enduring memory. Explicit requests to remember or correct enduring information remain possible through the same interaction. Distinguishing effects does not require offering all effects after each answer.
- **J2g restored draft:** prefer “Draft from 12 minutes ago,” the actual unfinished words, and an available Discard. Move device/custody/expiry explanations into research annotations or appropriately discoverable details. The board's local-only, plan-only, one-day rule is a design proposal, not a newly accepted storage policy; reconcile it with the existing lifecycle contract and Chat ownership. Do not replace that paragraph with an unlimited-retention promise.
- **J3c sender outcome:** show the actual current arrangement and supported attribution. Move “If Nora had left it…” into the annotation; a customer should not read hypothetical branches of the specification. An ignored optional suggestion still creates no follow-up obligation.
- **J2e recovery:** “Checking whether that saved” can carry the immediate meaning. Explain duplicate-prevention mechanics in the specification, while keeping the actual relevant controls and uncertainty legible.

Keep enough explanation to understand a material effect or recover from a problem. This is not an instruction to conceal failures, recipients, or changed scope. Prefer useful judgment over categorical claims about what the user will or will not enjoy; the fixture's travel assertions are not research-verified advice.

#### C. Make the prototype support the recovery described by the boards

The new simulations are useful, but source inspection found two gaps in `kit/proto.js`:

1. **Pending state blocks unrelated navigation.** The early guard in `commit()` rejects all actions during `pending` or `unknown`, including close/navigation and research reset. Restrict duplicate-effect prevention to relevant mutations; permit leaving and returning to inspect the same in-flight request. Closing is not cancellation. If a cancel control is illustrated, demonstrate only the cancellation the simulated execution stage supports.
2. **The user's words are not recoverably retained in the request UI.** A recognized route returns success and clears the field before execution succeeds; `save_label` holds a generated action label, not the authored request. The research log containing the text is not a user recovery path. The route can also report success after the pending guard rejected its action, clearing another request. Keep authored text, target, and execution identity available within permitted temporary custody; do not clear unaccepted input or make “Not now” silently destroy recoverable work contrary to the chosen resume behavior. Unknown-outcome reconciliation must refer to the original request before any retry can duplicate it.

These are bounded prototype corrections, not a request to implement production persistence or build an editor suite. The drawn keyboard on board 09 does not verify native keyboard behavior; the board 10 in-flow assistance region does not validate the illustrated modal sheet. Continue reporting those limits explicitly.

#### Next delivery and acceptance

Refine the existing three journeys and interactive artifact; add no new screen family. Update the friction log and corresponding older boards where necessary. Demonstrate:

1. A useful glance/inspection and exit without prompting or mutation.
2. A correction followed by adaptation that preserves its stated purpose—or clearly exposes the material tradeoff without unauthorized action.
3. A slow save during which the user can leave and return; a failed request with recoverable original words; and an unknown result reconciled without duplicate effects or loss of a second unaccepted input.
4. Exact private preparation → explicit send → recipient continuity, plus the authorized-editor contrast. Preserve independent contributions during repair.

Report what is illustrated, simulated, and mechanically exercised separately, with native and participant testing still unclaimed. Keep the editorial page, restrained materials, and small contextual interaction family. **The target remains a beautiful, useful plan with capable assistance—not an itinerary management system with a conversational front door.**

## 1. Why this project, and why now

The earlier interaction-kernel work asked how direct controls, conversational expression, shared objects, previews, and consequences should work. That remains valuable. This project asks a different question:

**What does the complete experience look and feel like when those behaviors become one coherent consumer product?**

Do not assume the kernel lab contains only component specimens. A newly available [V2.3 execution report](claude-design-interaction-kernel-lab-v2-3-arrangements-execution-report-2026-09-04.md) reports complete F1–F4 journeys and board 96. Inspect them before duplicating work. The new project is justified by a new composition/aesthetic question, not by pretending that work does not exist.

### Recent conversation progression — provenance, not reconstructed quotations

This summarizes the recent discussion available in the parent session; it is not a claim to have independently retrieved every message in a timed five-hour archive.

1. **Contraction:** stop treating booking, itinerary editing, changes, permissions, and expense as an expanding collection of mini-apps. Reduce compulsory management and frontend burden, without discarding useful competence.
2. **Lightweight arrangements:** an idea may remain loose; a contribution need not become a decision; joining dinner does not mean joining someone's entire afternoon.
3. **Dynamic collaboration:** owner edits by default; explicitly named collaborators can receive scoped editing rights. Comments and suggestions remain possible without structural editing.
4. **Comparison with current itinerary:** the current system has useful timing, spatial, participation, change, and recovery behavior. Do not rebuild that competence under new nouns or discard its readable overview.
5. **Founder correction:** the founder still likes the current itinerary's modern, editorial, sleek appearance. Simplifying product responsibilities does not imply replacing this visual language.
6. **Psychology research:** planning can relieve mental work; overly precise leisure scheduling can feel like work. More loose choices can burden users rather than free them. Beauty and anticipation can be meaningful parts of the value.
7. **Visual/code review:** the continuous document, serif activity titles, compact timing, chapters, and restraint are assets. Tiny essential labels, truncated prose, and unreliable day orientation are not assets to preserve.
8. **New exploration:** carry the itinerary's strongest qualities into complete loose, structured, shared, and changing experiences. Do not expose the internal arrangement model as the page's section taxonomy.

### The correction to our earlier direction

“Less itinerary maintenance” does **not** mean less itinerary usefulness, less information, or less visual character. “More flexible” does **not** mean a feed of unresolved choices. “AI-native” does **not** mean routing every action through a chat transcript; nor does user control require a comprehensive direct editor. Follow §0.1–0.2: contextual assistance for understanding, exploration, and changes, with selective direct conveniences for already clear choices.

The app should do the assembly work where helpful. It can offer a coherent afternoon or trip while preserving the person's ability to leave parts open, ignore an option, or change direction.

## 2. Version and authority checks before drawing

### Preserve and inspect the existing lab

- Known live project, from the V2.3 report: [Vesper — Interaction Kernel Lab](https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c).
- The report says the Downloads export was V2.1 while the live project had progressed through V2.2 to V2.3. This handover has **not independently verified** the live state or the report's test results.
- The last local inspection could not find `/Users/feihuyan/Downloads/vesper-interaction-kernel-lab` at that exact path. Resolve the current location; do not treat absence as permission to reconstruct or overwrite the project.
- Inspect F1 Saturday Jazz, F2 Ordinary Shared Evening, F3 External Reservation, and board 96. Inspect F4 Expense only for adjacent seams; do not expand this project into an expense redesign.
- Preserve the existing project/export. Reuse useful components, fixtures, and interaction reasoning deliberately. Do not clone its entire research apparatus into the consumer experience.
- The earlier [integration index](claude-design-integration-2026-09-04/00-handoff-index.md) instructed existing lanes to continue in place. The subsequent request for this **separate focused visual exploration** is a bounded exception, not authorization to restart all design lanes.

### Authority order

1. Explicit latest founder direction in this brief and subsequent messages governs this exploration's scope.
2. Accepted product/behavior contracts govern meaning, ownership, contribution, participation, and consequences.
3. Current shared tokens/components establish the implementation baseline, not unquestionable ideal design.
4. Native captures show observed behavior in a particular build/fixture, not every production state.
5. Claude prototypes and execution reports are design proposals/evidence with stated limits. They cannot silently amend product contracts.

Where sources disagree, record the disagreement and recommend a resolution. Do not label a speculative resolution “canonical.” Do not import stale blanket rules merely because the document has a canonical header.

### Required reading, in this order

Paths are relative to `/Users/feihuyan/travel-workspace`. Child repos remain independent repositories. Read their own `AGENTS.md` / `CLAUDE.md` before working there.

**Product and recent decisions**

- [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md) and [Product Model](../../travel-agent/docs/product/Product%20Model.md).
- [Multiplayer Product Strategy](../../travel-agent/docs/product/Multiplayer%20Product%20Strategy.md), especially §5.1 and §5.2.
- [Lightweight arrangements handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md), especially §1–3 and §4's unresolved architecture distinctions.
- [Plan/Occasion lifecycle](../../travel-agent/docs/architecture/plan-occasion-lifecycle-contract-2026-08-22.md).
- [Contribution and consequence](../systems/contribution-and-consequence.md).
- [Surface contraction investigation](product-surface-contraction-investigation-2026-09-04.md) for responsibility boundaries, not an instruction to delete code.
- [Kernel integration assignment](claude-design-integration-2026-09-04/03-interaction-kernel.md) and [V2.3 report](claude-design-interaction-kernel-lab-v2-3-arrangements-execution-report-2026-09-04.md).

**Visual language and actual implementation**

- [Design Language](../../travel-app/docs/Design%20Language.md), [Type and Material Doctrine](../../travel-app/docs/design/type-material-doctrine.md), and the [itinerary surface contract](../../travel-app/docs/surfaces/trip-itinerary/contract.md).
- [Fonts](../../travel-app/constants/fonts.ts), [typography](../../travel-app/constants/typography.ts), [text variants](../../travel-app/constants/textVariants.ts), [colors](../../travel-app/constants/colors.ts), [layout](../../travel-app/constants/layout.ts).
- [Card materials](../../travel-app/constants/cardSurface.ts), [header chrome](../../travel-app/constants/headerChrome.ts), [overlay materials](../../travel-app/constants/overlayMaterial.ts), [row geometry](../../travel-app/components/ui/rows/rowTokens.ts).
- `travel-app/app/(tabs)/trips/[tripId]/plan.tsx`: actual composition and conditional branches, not just component inventory.
- [TripPlanHeader](../../travel-app/components/trip-itinerary/TripPlanHeader.tsx), [TripEntry](../../travel-app/components/trip-itinerary/TripEntry.tsx), [ItineraryDateRail](../../travel-app/components/trip-itinerary/ItineraryDateRail.tsx), [PlanDaySection](../../travel-app/components/trip-plan/PlanDaySection.tsx), [ItineraryChapterHeader](../../travel-app/components/trip-plan/ItineraryChapterHeader.tsx).
- [PlanPreSpineContext](../../travel-app/components/trip-plan/PlanPreSpineContext.tsx), [TravelSegmentRow](../../travel-app/components/trip/TravelSegmentRow.tsx), [ParallelPlanSummary](../../travel-app/components/trip-itinerary/ParallelPlanSummary.tsx), [PlanStopInspectSheet](../../travel-app/components/trip-plan/PlanStopInspectSheet.tsx).
- [CurrentShapeSurface](../../travel-app/components/trip-itinerary/CurrentShapeSurface.tsx) and [feature flags](../../travel-app/constants/featureFlags.ts). Its existence is not approval of status-grouped composition; the Plan Shape flag defaults false in checked-in code.

Read these as a connected surface, then follow only relevant references. Do not stall on an exhaustive repository reread.

## 3. Visual evidence to carry into Claude Design

### Fresh native captures from the September 4 review

Local-only QA run: `travel-app/.maestro/runs/20260904T232754Z-trip-itinerary/`.

- `screenshots/full/plan-day-top.png`: opening Kyoto day, full header, date rail, undecided stay, evening chapter, timed stops, beginning of the next day.
- `screenshots/full/plan-day-scrolled.png`: later-day navigation and the observed context mismatch.
- `manifest.json`: source checkout recorded as `47735f406`, Ready Kyoto mock scenario, capture time `2026-09-04T23:27:54.985Z`.

The registered `04-plan` flow captured both images after a retry. Scenario validation, reference validation, and doctor passed. This was **not** a completed all-state visual acceptance verdict, participant study, or verification of live backend correctness. A checkout SHA in the manifest is not independently attested binary provenance. Attach the actual images to the receiving project when accessible; otherwise recapture through the registered QA path. Do not substitute a newly invented mockup and call it current app evidence.

Older isolated references: [reference manifest](../../travel-app/docs/surfaces/trip-itinerary/design-refs/manifest.json), [resting list](../../travel-app/docs/surfaces/trip-itinerary/design-refs/s-list.png), [live state](../../travel-app/docs/surfaces/trip-itinerary/design-refs/s-live.png). These were exported July 14 from the approved vesper 162 redesign. They help explain provenance; they are not a pixel-accurate representation of today's screen.

### What to preserve from the observed composition

- One continuous paper document rather than a stack of independent cards.
- A strong orientation heading followed by progressively quieter information.
- The experience/place name leading each row; time in a predictable hanging rail.
- Temporal chapters when they help reading, not mandatory empty sections.
- A warm but restrained material/color system.
- Compact, familiar navigation into map, conversation, people, and detail.
- Detail available without requiring every attendee, receipt, reason, and action to be visible at rest.
- A complete overview that still works without imagery for every stop.

### What not to preserve just because it exists

- Chapter copy cut off mid-sentence by `numberOfLines={2}`. Write a complete short opener or offer deliberate expansion; clipping is not editing.
- A selected-day heading above the previous day's trailing rows. The fresh later-day capture exhibits this; investigate whether selection/scroll/overlay timing causes it. Do not infer the underlying fix from one screenshot.
- Essential times treated as decorative microtype.
- Overlap or excessive visual weight from floating controls when they obscure reading.
- Ambient completion prompts becoming pressure to log every activity.
- Every undated item, loose evening, or empty day framed as unfinished setup.

## 4. Specific visual language for this exploration

### 4.1 Identity: warm editorial clarity, not decorative nostalgia

Use the existing paper / ink / ochre identity. The useful analogy is a carefully typeset city notebook or an inviting itinerary, not a scrapbook full of ornaments and not a software administration dashboard.

“Modern” here means confident hierarchy, crisp alignment, readable controls, responsive behavior, and restraint. It does not require cold white, generic sans-only cards, gradient AI badges, or excessive glass. “Editorial” means selection and composition; it does not require paragraphs, italics everywhere, or a photo on every row.

Create one main typographic/material treatment across all four scenarios. Change density and emphasis with the task, not the brand identity.

### 4.2 Typography — baseline and deliberate experiments

| Role | Inspected implementation baseline | Direction for Claude Design |
| --- | --- | --- |
| Primary day heading | `itineraryHeaderTitle`: EB Garamond semibold, 31/33, tracking -0.7 | Preserve a confident editorial heading; make long dates/titles and large text reflow |
| Short header context | `itineraryHeaderThesis`: EB Garamond Roman, 15/20 | One useful, complete line or short passage, not mandatory narration |
| Activity/place title | `itineraryEntryTitle`: EB Garamond medium, 17.5/21, tracking -0.2 | Preserve the reading-first activity register; no need to convert all rows to sans |
| Timing | `itineraryEntryTime`: JetBrains Mono, 10.5/13 | Baseline to compare, not a recommended accessibility floor; explore readable 12–13pt timing without inflating the entire row |
| Operational support | System Sans semantic body/caption roles | Plain, compact, legible; use for actions, warnings, changes, attendance, provider facts |
| Chapter/time stamps | JetBrains Mono; current `monoStamp` roles are 10pt with 1.3 tracking | Keep short; test meaningful labels at larger readable sizes; do not use mono for sentences or CTAs |
| Authored aside | Current code contains Roman and narrowly named italic roles | Use sparingly, see conflict note below; no wholesale italic treatment |

Web translation: load the actual approved EB Garamond and JetBrains Mono faces when available. Use a platform system-sans stack for utility. Do not silently substitute another fashionable serif. Record font fallback if the design environment cannot load a face. CSS px at a 393px-wide web phone are a design approximation to native points, not proof of native parity.

**Known type-source conflict:** older doctrine says no italic faces; current `fonts.ts` and `textVariants.ts` include `vesperVoiceItalic` at 17/24. There is also an itinerary-specific `itineraryChapterThesis` at **13/18 italic**, despite comments elsewhere describing a 17pt italic floor. The current native capture contains italic chapter prose. Record this explicitly. Do not propagate the 13pt exception into new general-purpose roles, silently claim “Roman-only,” or globally remove existing typography.

Recommend a readable short Roman aside as the first exploration baseline; a bounded italic comparison is permissible if it materially helps. Show both at actual phone scale if proposing an exception. Any new role needs a semantic name, not an isolated size tweak. Final token changes need separate review.

### 4.3 Palette — use resolved tokens, not old prose values

Snapshot from `constants/colors.ts`; recheck on entry:

| Use | Token | Value |
| --- | --- | --- |
| Continuous page | `surface.paper` | `#EFEAE0` |
| Ordinary quiet card, only when needed | `surface.card` | `#F7F2E7` |
| Primary ink | `surface.ink` | `#1B1714` |
| Softer reading ink | `surface.inkSoft` | `#2C2622` |
| Meaningful secondary text | `surface.mute` | `#6E6862` |
| Decorative/inactive only | `surface.muteSoft` | `#B5AFA5` |
| Ochre accent | `surface.gold` / `surface.goldDeep` | `#B0853A` / `#8A6628` |
| Functional Vesper signature | `surface.signatureGold` | `#856020` |
| Planning/route ink | `surface.planningInk` | `#3D5066` |
| Genuine conflict | `surface.oxblood` | `#7A2E2E` |
| Solid primary action | `action.primary` | `#4A3428` |
| Fine rules | `surface.hairline` / `surface.hairThin` | Ink at 10% / 6% alpha |

Gold is not an instruction to color every active control. Use no general purple “AI” register here. Preserve semantic color but do not turn ordinary optionality into warning amber. Meaningful content must pass contrast checks in its actual combination; a token name alone is not certification. The `ghostAnchor` exception is not permission to make all metadata faint.

### 4.4 Material, spacing, and row rhythm

- Paper is the page, not an obligation to wrap every item in another paper card.
- Ordinary itinerary content should remain flat rows or sections when grouping already works through alignment, proximity, and rules.
- When containment genuinely helps—an attached contribution, preview, or bounded object—start with the shared **Quiet Paper** recipe. No perceptible lift for ordinary cards.
- Elevation belongs primarily to floating controls, menus, sheets, and deliberate spatial overlays. Reuse the overlay vocabulary rather than making everything tactile.
- Current `radius.surfaceCard` is **14**. Older prose lists competing 8/12 values. Resolve from the actual recipe/token; do not create a new global radius system to reconcile old text.
- Structural spacing starts with 4/8/12/16/24/32. Preserve named intermediate/optical spacing where the current itinerary uses it. Avoid anonymous almost-equal values throughout the prototype.
- Current timed rows use a 44pt leading time column and a 60pt minimum row height; `TripEntry` supplies additional vertical rhythm. These are baseline measurements, not a demand that every loose intention occupy a timed row.
- Keep date, time, and content alignment disciplined. Do not widen the time gutter merely to accommodate a paragraph of status copy.
- Allow a sparse day to be finished and useful. Do not manufacture rows or empty-hour slots to fill the screen.
- Show realistic full scrolls. A fine first viewport that degenerates into repeated oversized gaps below the fold is not a complete composition.

### 4.5 Chrome and motion

The current header has an orientation mode and floating compact mode. Preserve accessible entry to conversation, map, people, and details without forcing the exact existing icon arrangement.

- Header foundation currently uses 44pt targets, 20pt glyphs, 12pt soft-square and 16pt capsule radii. Read `headerChrome.ts` and overlay material before reproducing them.
- A shrinking header must not obscure rows or claim the wrong day. Day identity should match what the person is reading, or clearly distinguish selection from the visible date.
- Use stable object positions during local changes. Show an understandable transition from old to new rather than regenerating the whole page.
- Do not silently reorder the accepted experience because fresh suggestions arrived.
- Animate a deliberate move, expansion, or returned result; do not choreograph every scroll into a performance.
- Provide Reduce Motion and Reduce Transparency alternatives. Do not rely on animation alone to communicate what changed.

### 4.6 Imagery and editorial substance

The itinerary's ability to feel rich without constant photography is an asset. Keep it. Use a photo, map excerpt, ticket, or friend's contributed image when it improves recognition, orientation, anticipation, or understanding—not as filler.

A small number of meaningful media moments can vary the rhythm. Avoid adding an image to every stop or turning every contribution into a large social card. Let a dish photo remain a small, relevant contribution near dinner when that is sufficient.

Use matte/frame/scrim treatments where needed. Do not wash out evidence or make details unreadable to match the parchment palette. Essential text should not sit on busy imagery.

**Copy bar:** specific, useful, non-diagnostic. “The later set leaves time for dinner and the walk” is useful if supported by fixture timing. “You experience travel through transitions” is not. Do not repeat a connection the user already supplied as if it were new insight. Do not use “What do you want to do?” as a replacement for doing useful work.

## 5. Meaning to preserve without exposing the machinery

These are behavior constraints from our discussion and accepted contracts. They are **not a mandatory list of visible sections**.

| Distinction | Show the consequence naturally | Avoid |
| --- | --- | --- |
| Possibility vs retained intention | A useful option can be read and ignored; deliberate Keep changes later availability | Every option demanding Accept/Reject |
| Current intent vs shared agreement | A loose afternoon and an agreed dinner coexist | Presence on the page implying everyone agreed |
| Comment vs suggestion vs edit | A friend's words remain theirs; adoption changes the relevant plan | Every comment becoming an AI turn or proposal queue |
| Ownership vs editing rights | Owner can name editors and scope from the object or clear language | A permanent permissions dashboard |
| Participation vs authorship | Dinner-only and nonattending helpers are ordinary | Editing granting attendance; leaving deleting contributions |
| Private preview vs adopted change | “Less walking” shows a concrete alternative before adoption | Exploring silently changing the group plan |
| Personal fixed point vs agreement vs reservation | Show the practical distinction only when it matters | One generic “locked” state pretending these are identical |
| Local repair vs external correction | Undo only when supported; already sent messages cannot be unsent by local rollback | Blanket Undo that erases other people's work or claims an external reversal |

Default: owner edits; others invited to contribute. The owner may explicitly permit named people to edit all or part of this arrangement. No need for owner reapproval of every ordinary edit within that grant. Changing an agreed meeting, spending, disclosure, membership, or provider state remains a separate consequence.

“Let Maya help with the afternoon; keep dinner fixed” should be understandable without a matrix. Make the resolved people and scope inspectable. Do not default to a questionnaire collecting every authority dimension before anyone can help.

The existing lab reportedly treats some shared time updates as quiet feedthrough and proposes “no Undo past Send.” Reuse neither as a universal rule. Inspect the specific scenario: changing uncommitted material differs from changing a time people have accepted or are already acting on. A send cannot be magically retracted, but a later correction or repair may remain possible. Flag any disagreement with accepted contracts before adopting it.

## 6. Four complete situations — one coherent visual proposal

All people, venues, timings, weather, reservations, and messages used below are labeled synthetic fixtures in the research layer. Never present them as actual current recommendations or the founder's friends' activities. Reuse a coherent fixture set; do not mix incompatible example times across screens.

The first deliverable is one recommended composition family across all four situations. It is not four competing design systems, one grammar per tab, or a test gate that delays consideration of the whole system. Compact local comparisons are welcome where there is a real unresolved design decision.

### A. A loose Saturday in New York

**Intent:** “Maybe jazz Saturday. Keep that option; don't build the day around it.” There may be a separately established dinner at seven. The person has not created or named a Trip/Plan for the jazz idea.

**Value at rest:** show enough to make the possibility attractive and practical: the actual option, why it fits, its relation to dinner, and any genuinely useful alternative. No intake before value. The sparse composition should feel complete, not an empty itinerary waiting to be filled.

Show:

1. Reading the possibility before retention.
2. Keeping it without a container-creation flow or implied attendance.
3. A genuinely bounded choice such as selecting an available set, plus contextual requests for arrival time or “make it less rushed,” following §0.1. Do not add a general timing editor.
4. A private preview that preserves dinner and makes the practical difference visible.
5. Deliberate adoption, quiet result, and truthful recovery.
6. Returning after unrelated chat: current intent is immediately inspectable.
7. Releasing Saturday while independently keeping the place, where the fixture established both.

**Design question:** when is a short composed page enough, and when does a temporal sequence help? Do not force a date rail onto a single loose intention. No “three open tasks,” completion percentage, or scheduled morning/afternoon/evening placeholders.

### B. A carefully planned multi-day trip

Use the current Kyoto fixture or an internally consistent equivalent. Include an arrival day, a dense day, a loose day, one exact transport departure, one confirmed reservation, and one unresolved but useful intention.

**Value at rest:** a beautiful, navigable trip overview and day sequence. This is where the current itinerary should remain recognizable. Preserve the capacity to understand what happens next, how places connect, and what deserves anticipation.

Show:

1. Opening a day, reading its full scroll, and navigating to another day.
2. List/map switching with day and selected-place context retained.
3. A loose interval beside a genuine exact-time dependency; neither becomes the other's visual model.
4. Inspecting a stop for useful value without implying a change, then optionally expressing a change in context, including a day/time not offered by the suggestions. Resolve only meaningful uncertainty; do not require a dedicated move form or make every property editable. Follow §0.1–0.2's B4 revision.
5. One itinerary-aware alternative with a concise practical difference, not an exhaustive diff.
6. Scrolled/compact header behavior and a long title at larger text size.

**Design question:** what is the minimum structure that makes this trip dependable? Do not hide useful transfer information solely because it is operational, and do not expose every walking connector by default. Preserve access to practical detail without making the user maintain a second plan.

### C. A shared afternoon and dinner

The owner has afternoon intent and a bounded dinner Occasion. Maya can contribute; Sam joins dinner only; another friend can help without attending.

**Value at rest:** a legible evening with just enough social context to make it feel shared. Not a committee workspace. The host's and guest's views share agreed facts but need not contain identical private context.

Show:

1. Owner initiating the shared dinner naturally, reviewing the actual invitation, and explicitly sending it.
2. A guest opening a bounded invitation and seeing useful when/where/context before being asked to participate. Reuse the existing thin-guest pattern if applicable; label its production dependencies.
3. Maya commenting or suggesting a bookstore without changing the afternoon.
4. A dish/place/photo contribution attached at an appropriate scale, without an activity-feed obligation.
5. Owner granting Maya afternoon editing, keeping dinner fixed; Maya makes an ordinary allowed edit without an unnecessary second owner approval.
6. Sam choosing dinner-only without deleting the afternoon or generating failed-consensus UI.
7. A quiet catch-up on return and revocation of future editing without erasing contributions or attendance.

**Design question:** how do people appear in the experience without every stop acquiring avatars, RSVP controls, attribution, and comment counts at rest? Explore contextual attribution and bounded expansion. A suggestion no one adopts must be allowed to remain socially unremarkable.

### D. The day changes while people are moving

Start from C or a shared segment in B, rather than a disconnected emergency dashboard. Dinner at seven is accepted; imported reservation evidence also says seven; a traveler is already on the way. A change to eight is proposed. Include a lower-stakes rain alternative for comparison.

**Value at rest:** identify what is affected, what remains intact, and the useful next action. The whole app should not become an alarm panel.

Show:

1. Rain changes an optional afternoon possibility: a scoped alternative, no group-wide approval ceremony by default.
2. A proposed change to the relied-upon dinner: an appropriate preview and affected-person response/coordination state.
3. Who has received or responded, only where it matters; silence is not acceptance.
4. An updated meeting arrangement while the reservation still says seven. One legible practical mismatch, not a state-machine exposition.
5. External provider link and return, with no claim that opening the link changed the reservation.
6. Forwarded new confirmation if the fixture includes it; evidence changes the corresponding fact, not everyone's consent.
7. Returning to a stale alternative after another accepted change: preserve the person's intent and explain the localized conflict.

**Design question:** can live assistance feel like the same calm product becoming timely, instead of a separate operations application? Precise help is part of the promise; admin-heavy presentation is not.

### Secondary stress case, not a fifth redesign

Two travelers overlap in Portugal for only part of their separate stays; one skips a museum and rejoins dinner. Show a compact adaptation of C/B that preserves separate personal horizons and a readable shared reunion. Avoid permanent traveler swimlanes or a new subgroup Occasion for every divergence. See S3 in the arrangements handoff for meaning.

## 7. Composition decisions the designs should resolve

Return an opinionated recommendation for each; do not postpone all of them to implementation.

1. **Primary organization:** when do sequence, meaningful chapters, and a short undated composition each help? Do not default to Settled / Flexible / Open / Changed / Unknown sections. Internal status is not automatically the user's reading order.
2. **Current vs possible:** how do optional ideas sit near a composed experience without becoming either clutter or hidden second-class material?
3. **Read vs act:** how does a readable plan provide contextual access to Vesper for understanding, exploration, and changes without becoming another chat feed or comprehensive editor? Follow §0.1–0.2. Retain direct controls for obvious bounded choices; do not allocate a visible operation to every mutable field or make inspection adjustment-first. Keep private assistance stable across roles, distinguish shared discussion, and explain optional conversation expansion and return to the clean resting page.
4. **Precision:** how do “afternoon,” an estimated fit, an agreed time, and a provider departure look different without a legend?
5. **People:** where are shared scope, personal attendance, authored contribution, and editing capability most legible with the least persistent chrome?
6. **Change:** how does the relevant difference become visible without replacing the whole page with a diff or receipt feed?
7. **Continuity:** where does this inspectable experience rest, and what does opening it from Home, Places, Chat, or Life preserve? Show destination and return, not new root designs.
8. **Aesthetic density:** how much content can be useful on a phone before hierarchy fails? Compare at equal visual quality; do not make the new design win by degrading the old reference.

## 8. Relation to the four roots and adjacent design work

The app remains **Home / Chat / Places / Life**. Product moves remain **Make sense. Open possibility. Help it work. Carry forward.** Neither is a mandatory four-step funnel.

| Entry | What to illustrate here | What stays with the adjacent lane |
| --- | --- | --- |
| Home | A useful current/anticipated experience opens the relevant current arrangement | Full Home feed composition, ranking, editorial portfolio |
| Chat | Input or a result can open/act on the same current owner; return preserves the conversation | Chat root layout, composer system, conversation redesign |
| Places | A place/route can enter this experience at a known scope | Place detail/entity redesign, discovery feed, global map design |
| Life | The person can refind retained/planned/shared material and open current detail | Life root organization, timelines, categories, map/archive architecture |

A Home projection can carry real value and a bounded action; it need not be a content-free pointer. A historical chat message is not a second editable copy of current truth. This project should show coherent entry/return without taking over every root or introducing an Arrangements tab.

## 9. Practical scope boundaries

- No Vesper checkout, payment collection, hotel booking funnel, provider hold/cancel/rebook execution, or merchant-call UI. External links and supplied confirmation evidence can be integrated into the experience.
- Do not remove exact transport times or imported tickets because booking execution is out of scope.
- Expense is adjacent. At most show a contextual receipt/cost continuation if needed to make a dinner coherent. No balances dashboard, category form suite, collection workflow, or assumption that AI replaces deterministic arithmetic.
- No global permissions center, general shared-document editor, live cursors, branch-management UI, new universal object schema, or new microservice proposal.
- Do not convert every possible plan into a Trip, create hidden pseudo-Plans, or invent exact times merely to satisfy a renderer.
- Do not require confirmation for every private reversible adjustment. Equally, do not erase meaningful consent or external consequences to make the prototype look effortless.
- No production code, feature-flag, contract, or canonical design-token changes as a side effect of this assignment.

## 10. Research basis — use as design guidance, not proof

These sources were researched in the parent conversation. The implications are design inferences. Most studies concern websites, short leisure activities, or laboratory tasks—not Vesper. Do not label the finished prototype psychologically validated.

| Finding | Implication to explore | Limit / counterweight |
| --- | --- | --- |
| Precise leisure scheduling can reduce free-flowing enjoyment; rough scheduling removed the effect in the reported studies | Let loose activity remain loose around real fixed anchors | Not an argument to hide a ferry departure or eliminate planning. [Tonietto & Malkoc](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/d/37041/files/2016/12/Tonietto-and-Malkoc-JMR-2016-2b6lj4e.pdf) |
| Specific plans reduced intrusive goal-related thoughts/interference in laboratory studies | Preserve a dependable assembled experience; do not give all coordination work back as options | Not a travel-app trial or proof that more schedule detail is always better. [Masicampo & Baumeister](https://pubmed.ncbi.nlm.nih.gov/21688924/) |
| Choice overload depends on complexity, decision difficulty, uncertain preferences, and effort goals | Curate a coherent recommendation and meaningful alternatives | No universal ideal number of options. [Chernev et al.](https://myscp.onlinelibrary.wiley.com/doi/10.1016/j.jcps.2014.08.002) |
| Experiential anticipation can itself be pleasurable | The plan may be something worth looking forward to, not only a control panel | Does not establish that a serif itinerary causes anticipation. [Waiting for Merlot](https://journals.sagepub.com/doi/10.1177/0956797614546556) |
| Aesthetic assessment includes simplicity, diversity, colorfulness, and craftsmanship | Preserve controlled variation and coherent composition, not just emptiness | Website assessment framework, not a universal palette/style recipe. [VisAWI](https://www.uni-muenster.de/OWMS/uploads/drafts_thielsch/pdf/moshagen_2010.pdf) |
| Low visual complexity and familiar patterns improved early aesthetic ratings in website experiments | Keep familiar day/map/sequence structures while intelligence evolves | First impressions are not task success or retention. [Tuch et al.](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) |
| A 2026 meta-analysis found a positive average aesthetics/performance effect, with substantial heterogeneity | Treat craft as consequential, not expendable polish | It does not validate our particular design. [Schlamann et al.](https://www.tandfonline.com/doi/full/10.1080/10447318.2026.2664081) |
| Weak interaction signifiers increased effort in an eye-tracking comparison | Quiet controls must still reveal what can be acted on | Not a requirement to use prominent buttons everywhere. [NN/G](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/) |
| Productive and expressive typography can coexist when matched to the task | Editorial reading with practical action controls | Design-system guidance, not an experimental result. [Carbon](https://carbondesignsystem.com/elements/typography/style-strategies/) |
| Apple emphasizes text hierarchy, scaling, and legibility; lists 11pt recommended minimum for iOS/iPadOS | Reassess small time/stamp roles and test larger text | Web rendering is not native accessibility certification. [Apple typography](https://developer.apple.com/design/human-interface-guidelines/typography?changes=_5) |

Research could disconfirm our proposal: if users cannot see a complete day, find fixed details, change something, or understand others' participation as easily as in the current itinerary, visual simplification has failed. Do not treat fewer screens, fewer words, or fewer visible controls as success by themselves.

## 11. Execution and Code ↔ Design synchronization

### Phase A — establish the actual baseline

1. Check branches/status in any repo you inspect or touch. Preserve other sessions' work. Read the local instructions.
2. Inspect the sources above and the current live kernel project. Record project ID, version, active boards, and stale exports. Read board 96 before rebuilding F journeys.
3. Open the native images and design references. Where unavailable, state the limit and obtain a current export/capture through supported tools.
4. Create a concise baseline board: current screenshot, strengths to preserve, observed issues, reusable components, source conflicts, and open behavioral questions.
5. Continue the existing Plans in Real Life project identified in §0. Preserve the separate kernel lab. Record the current live version and reconcile it with the reviewed export before editing; do not create a duplicate project or overwrite newer live work. Existing results remain design evidence, not canon.

### Phase B — compose one complete family

1. Start from the editorial itinerary's visual language. Work through A–D together before deeply polishing only one situation.
2. Produce full-scroll resting states and coherent transitions, with research annotations outside the phone frames.
3. Choose a recommended composition. Use a small alternate only when it resolves a specific question such as temporal vs short-form arrangement, or contribution placement.
4. Include the overlapping-travel stress case as an extension, not another standalone product.
5. Explicitly show what the person receives before supplying more information. Audit every ask: is it truly necessary to deliver this consequence?

For this review iteration, preserve the existing complete family and board 09's connected journeys. Prioritize §0.4's intent-aware adaptation, lighter customer copy, and executable recovery, retaining §0.1–0.3's contraction and assistance requirements. The original broad composition brief is context, not an instruction to restart all four situations.

### Phase C — make the visual consequences interactive

- Selective direct controls and supported contextual language examples must change the same fixture state or fail honestly. Do not make arbitrary input appear understood by advancing to a predetermined success screen. Implement §0.1's stress cases through the same interaction family, not six separate editors.
- Identify scripted recognizers outside the consumer frame. Unsupported inputs should preserve current state and offer a supported continuation.
- Keep actor/viewpoint and world-event controls in research chrome, not the customer interface.
- Re-entry must show the current state; navigation Back must not undo an edit.
- Keep, preview, adopt, contribute, participate, grant/revoke, and external handoff must have distinguishable effects even when their UI is small.
- Let ordinary interactions feel ordinary. Do not add a receipt card for every tap merely to expose correctness to the researcher.
- Follow §0.3 for active follow-up access, contextual no-mutation answers, interruption/resume, execution uncertainty, and consistent private preparation before explicit sharing; apply §0.4's updated correction and acceptance criteria. Keep prototype recognizer limitations separate from the product's supported capabilities and genuine execution boundaries.

### Phase D — verify the design, then hand back the decisions

- Render at 393px phone width; also test 320px and enlarged text (at least 135%, plus a stronger large-text stress case where supported). These checks do not substitute for native Dynamic Type/VoiceOver testing.
- Inspect full scrolls, long names/titles, sparse and dense days, missing imagery, and the view of a dinner-only participant.
- Interactive hit areas should be at least 44×44 in the design coordinate system; a small icon may have a larger invisible target without crowding the page.
- Verify essential text contrast, no horizontal overflow, no clipped primary controls, meaningful keyboard/focus labels, and a reduced-motion treatment.
- Recheck date identity after navigation and every adopted change. Do not allow presentation mode changes to create different underlying facts.
- Run the prototype's actual interaction tests if available; separate scripted mechanical success from usability findings.
- Review screens in the live Claude project **after sync**, not just local source. Record changed files/boards, version, screenshots, and limits. Do not overwrite a newer live version with a stale local export.

The receiving agent should create a compact token/component mapping for the prototype. Use semantic CSS variables/roles that map to the repo; avoid a new untraceable style vocabulary. New visual roles are proposals with rationale, not immediate production tokens. Reuse existing state machinery if suitable without copying its research vocabulary into the UI.

No production implementation is requested. If the founder later approves implementation, use the child repo's surface QA and API-contract workflow. Never claim native parity from a browser prototype or typecheck.

## 12. Required delivery back to the founder

Deliver:

1. **Project URL and active-board map**, with the original kernel lab clearly separate.
2. **One recommended complete design family**: four full-scroll situations plus the small overlap extension.
3. **Essential interaction paths**: the three connected journeys in §0.3, refined under §0.4 and incorporating the §0.1 stress cases and §0.2 baseline. Explicitly cover value without mutation, free follow-up, intent-aware adaptation, ordinary change, conditional clarification, interruption/recovery with original words, and exact sender-to-recipient continuity. Report illustrated, simulated, and mechanically tested portions separately.
4. **A visual baseline comparison** using the current itinerary at equal scale and comparable content. Explain what was preserved, changed, and intentionally removed.
5. **Type/material mapping**, including exact reused tokens, proposed exceptions, font loading/fallback, and unresolved old-doc conflicts.
6. **A concise decision log**: accepted behavior preserved; design recommendations made; architecture-bearing questions still open; contract amendments proposed, if any.
7. **Reuse/contraction map**: existing components to retain/adapt; ceremonies removed from the proposed experience; no claim that runtime code was retired.
8. **Evidence and limitations**: rendered sizes, tested transitions, screenshots, scripted language limits, no-op/overflow findings, and what was not verified.

Do not return only a component library, philosophy essay, long list of choices, or dozens of disconnected polished screens. The result should make it possible to judge whether this is a desirable and comprehensible product in use.

### The review questions that matter most

- Is this something I want to open, not merely something I can operate?
- Do I immediately receive a useful experience or understanding, rather than another request for input?
- Can I see the whole day when that is useful, and hold one loose intention without pretending it is a trip?
- Can I identify what is fixed, what is flexible, and who is joining without decoding a status system?
- Can a friend enrich this without joining a planning committee?
- Can I express an unanticipated change without discovering an operation, use an obvious shortcut when helpful, and see what actually happened—without operating a comprehensive editor or accumulating another chat feed?
- Can I correct or qualify an answer, get interrupted, and resume without reconstructing my intent or mistaking an unresolved request for an applied change?
- Can a contributor predict exactly what will be sent, and can the recipient receive value without being obliged to process another decision?
- Does live assistance feel like the same product becoming useful at the right moment?
- Does the visual richness survive sparse data, practical constraints, and large text?

**Final standard: preserve the beauty and legibility of the itinerary, expand the kinds of life it can hold, and reduce the work required to keep it useful.**
