---
doc_type: working
status: active
owner: founder / product / design / Components and Plan
created: 2026-09-04
last_verified: 2026-09-06
expires: 2026-10-04
why_new: Gives Claude Code and Claude Design a composition-led visual exploration brief that reconciles the September 4 arrangements discussion, consumer research, and the existing editorial itinerary instead of replacing it with an operational status dashboard.
supersedes: []
source_of_truth_for: []
---

# Claude Code → Claude Design handover: Vesper — Plans in Real Life

## 0. Start here

**Current assignment — September 6, content and continuation cleanup.** Continue the existing **Vesper — Plans in Real Life** project. Read §0.8 first; it reviews the September 6, 11:50 export against §0.7. Preserve the reduced family and the improvements already made. Refine D3's message-first hierarchy, J2f's social assumption, F1's prominence of reported experience, and the precise consequence of I1's prepared message. Keep detailed recovery/coverage/prototype material in appendices 90–92. Earlier sections remain provenance and engineering evidence, not a cumulative screen checklist. No new project, operation-screen expansion, adjacent-root redesign, or production implementation is requested.

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

**Review-stage note:** this records the preceding export. See §0.5 for the subsequent corrections, remaining findings, and current assignment; do not reintroduce work already completed.

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

### 0.5 Latest export review: better judgment, lighter completion, dependable recovery

**Review-stage note:** these findings concern the 11:39 export. §0.6 records the subsequent fixes and current journey-coverage assignment. Retain the regression cases without treating their original failures as still outstanding.

**Evidence — September 5, export files dated 11:39 local.** The review read boards 09/10 and `kit/proto.js`, rendered the revised journey compositions, and exercised the runtime in an isolated JavaScript harness with stubbed DOM and controlled timers. The harness checked state transitions and input-field behavior, not real browser navigation, native gestures, keyboard behavior, a production backend, or participant usability. No design or application code was changed during the review. This section refines the existing assignment, not the accepted ownership, audience, or lifecycle contracts.

#### Confirmed progress to preserve

- The ordinary correction no longer triggers “Remember this about her?”
- J2g now presents the unfinished draft, its context, and Discard without a retention-policy paragraph. J3c's hypothetical outcome is now an annotation rather than customer copy.
- J2f names the crowd-avoidance tradeoff and accurately reads back Isuien at about 12:30. It no longer describes timing compatibility alone as a successful experiential resolution.
- In the exercised sequence, a pending save allowed Home navigation and return; a blocked second mutation retained its input; the first request completed. A failed request could be dismissed into a draft and restored with the original words. These address specific §0.4 defects, not every recovery or multiplayer case.

#### A. J2f: permissible is not necessarily helpful

The prominent “Go early myself” action solves an authorization problem—only change the requester's participation—but not necessarily the human concern. The exchange began with whether the user's mother would enjoy the visit, then her dislike of crowds. Her attendance has not been established; sending the user alone does not inherently address her experience.

**Authority constrains the solution; it should not determine which solution Vesper recommends.** Preserve the useful observation about Ben's move. Do not make splitting up the primary recommendation without supporting context. Consider a quieter alternative or help discussing the timing with Ben, choosing the strongest continuation from what the exchange actually supports. Do not assume the mother is attending, that she follows the user's participation change, or that Ben should be moved automatically. A private reason remains private unless its disclosure is separately authorized.

Show one well-founded recommendation through the existing interaction family. Do not resolve this critique by introducing a profile questionnaire, a new decision screen, or a menu of every theoretically permissible action. A solo option remains valid when it genuinely fits the expressed intention.

#### B. J2f: completion should feel complete

The rendered result combines a success receipt, Ben's change, an alternative, “Go early myself,” “Say something to Ben,” “Undo mine,” and “See Isuien.” Individually useful elements have accumulated into a small task panel above the itinerary.

Refine the hierarchy toward **brief result → useful observation → strongest optional continuation**. This is a hierarchy, not a compulsory three-part template or a universal one-button limit. Keep Undo available but subordinate; make seeing Isuien ordinary navigation rather than another equally prominent decision. Further conversation remains accessible through contextual Vesper. An ordinary successful addition should not leave the person feeling that they acquired four more tasks. Preserve the readable day and its editorial character; no new family of result screens is needed.

#### C. J2e: unknown must not read as confirmed unchanged

The board says “Checking whether that saved” and then “nothing on Monday has changed yet.” Board 10 has the same contradiction. If the effect is unknown, the app cannot promise that nothing changed. The distinction is whether execution is pending, confirmed failed, or awaiting reconciliation—not three variations of reassuring copy.

Illustrative replacement:

> Checking whether Isuien was added. Your request is still here.

Use “nothing changed” only for a known non-application. Keep retry unavailable where it could duplicate an unresolved request, and preserve the authored request without requiring the user to understand the reconciliation mechanism.

#### D. Remaining prototype defects: exact reproductions and expected behavior

1. **Discard leaves the restored words in the composer.** Inject failure → submit “add the bookstore” → resolve failure → Not now → open Ask → Discard. `draft` becomes empty, but the restored input still contains “add the bookstore.” Discard should remove the matching restored draft from state and its field; do not erase a different or newly edited input by indiscriminately clearing every composer. Reopening must not resurrect discarded text.
2. **Undo reverts another person's independent response.** Nora applies the café alternative → switch to Sam → Sam joins dinner → switch to Nora → Undo. The tested result restores the walk but also returns Sam's response to `unknown`, because Undo restores a whole-state snapshot. Repair only Nora's relevant change and preserve Sam's response and independent edits. This needs a bounded prototype correction, not production persistence architecture or another approval workflow.
3. **Private request state crosses viewpoints.** Nora starts a slow bookstore addition → switch the research viewer to Maya. Nora's authored request remains in global `req_text`, and Maya's save display binds that same state. Model private request/draft/receipt ownership separately from the shared plan, so viewpoint switching does not expose someone else's private exchange or offer recovery controls for their request. Show the shared accepted result only where appropriate. This is a defect in the simulated multi-viewer artifact, not a claim of a production data leak.

Keep the existing explicit-send boundary and the navigation/input fixes. A global shared state object is acceptable for a prototype only if its projections and repair accurately demonstrate these distinctions; additional screens are not the remedy.

#### Bounded next pass

Keep the composition family and refine the existing boards and runtime. Deliver J2f with a contextually justified recommendation and lighter action hierarchy, consistent uncertainty wording across boards 09/10, and regression checks for the three reproductions above alongside the now-working pending-navigation and failed-input cases. Update the friction log to distinguish fixed, outstanding, illustrated, and exercised behavior. Native and participant validation remain unclaimed.

**The next improvement should make Vesper's help more perceptive and dependable—not make the interface more elaborate.** This is a refinement of a coherent product direction, not a request to reopen the entire design or turn the broader system into a narrow proof gate.

### 0.6 End-to-end journeys, coverage, and engineering implications

**Historical assignment note:** this section records the 13:39 export before the accepted subtraction. §0.7 governs the current pass. Retain the owner/dependency analysis and regression evidence; do not restore removed recommendation controls, deferred peer-authority proposals, or appendix journeys merely to satisfy this earlier coverage brief.

**Assessment.** The central flow makes sense. The family is more complete as a way to read and adapt an arrangement than as an end-to-end experience covering everything around it. Keep it as the Plan/Occasion design north star, not as proof that every product responsibility or implementation seam is resolved. The next work should complete missing transitions, not reopen the visual system.

**Evidence and limits — September 5.** The latest review inspected the local export dated 13:39, including A9–A10, C/D/E, J1–J3 and prototype source; rendered the revised journey composition; and exercised selected state/input transitions in an isolated JavaScript harness. Follow-on investigation inspected Product Thesis, Product Model, Multiplayer Product Strategy, the [lightweight-arrangements implementation handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md), and relevant code at app `c03f909f8` / backend `424e2d23a`. Findings are hypothetical walkthroughs plus bounded code evidence, not observed user friction, an exhaustive repository audit, production test results, or native visual acceptance. Reinspect current code before implementation.

**Closed findings from §0.5.** J2f now offers “Ask Ben about 10:15” rather than assuming solo participation, with lighter hierarchy, subordinate Undo, and an inline navigation door. J2e no longer promises unchanged state while the result is unknown. Harness checks passed for matching-draft discard without resurrection, preserving different edited input, Undo retaining Sam's independent response, private request-state separation on viewer switch, deferred results assigned to the original requester, pending navigation, and retaining a blocked second input through reconciliation. These are specific passing cases, not comprehensive privacy, concurrency, or native certification. The export itself still identifies retry-identity and illustrated-versus-wired limitations.

#### A. Six journey traces: keep the strengths, finish the transitions

**J-A — A thought becomes something useful later.** Chat → grounded jazz possibility → Keep → sparse Saturday page → optional adjustment → later return through Home, Chat, Places, or Life.

The value-before-organization pattern is strong. The remaining question from the person's perspective is: “Did I save a place, make a plan, or save this conversation—and where is it tomorrow?” Show recognizable identity and current state across entry and return. The immediate result should open the retained thing; later refinding should not require remembering the original conversation. Release “Saturday” without losing an independently retained Corner Note relationship. Do not add a naming form, mandatory Trip, storage explanation, or tutorial. Engineering must support stable lightweight intent, optional timing, owner references and scoped release. A saved card is not the complete capability.

**J-B — Understand, follow up, and adapt in context.** Inspect Tōdai-ji → ask about mother → correct the answer → request Isuien → receive the actual result → optionally discuss timing with Ben.

This is the strongest illustrated flow. Preserve the active field and carried target. Older A4 still puts further expression behind “Something else…” after a proposed alternative; align such examples with the later J2 continuation pattern. “That works, but can we get lunch first?” should be an ordinary follow-up, not navigation to another operation. Expand the same active surface when useful; remove conversational chrome when returning to the resting plan. A transfer to Chat carries target, unresolved intent and conversation continuity instead of requiring a new briefing. This is shared interaction/session work with the Chat lane, not authorization to create a second assistant or conversation store.

**J-C — Invite, contribute, and participate without a planning committee.** Host describes dinner → previews actual invitation and recipients → sends → guest receives useful details → responds or contributes → authorized collaborator edits within scope.

The roles are well distinguished, but the thin guest is better designed as an RSVP recipient than as a contributor. C4 shows Dana's photo and Sam's dessert contribution after arrival; it does not fully trace how a non-app guest supplies them. Cover “I can get there at 7:30,” “Can I bring Alex?”, “I'll bring dessert,” a practical question, and one photo/link contribution through a minimal family—not five screens. A reply to the host must be distinguishable from a private question to Vesper. Contributions need not become arrangement edits, and viewing a link alone does not grant contribution rights. Guest delivery, bounded identity/access, authorship, media custody and later access changes are real engineering dependencies; an RSVP endpoint does not implement all of them.

**J-D — A change cannot work for everyone.** Maya asks for eight → owner sees implications → sends the changed time → reservation mismatch remains → Sam responds → provider evidence may arrive.

The designed success path is useful but assumes eventual accommodation. Continue with “Sam can't do eight” and, separately, “The restaurant can't move the table.” Recording the objection is not the same as helping the experience work. Depending on expressed priorities and practical facts, Vesper might help keep seven with Maya joining later, retain eight with Sam explicitly opting out, or prepare another feasible arrangement. Show one supported continuation rather than all alternatives at once. Do not restore everyone's agreement from organizer intent, imply that sending equals delivery, or assume delivery equals acceptance. The needed intelligence is consequence-aware coordination, not a new vote/approval dashboard. This is a substantive live-engine responsibility, not peripheral error handling.

**J-E — A conditional plan meets an ambiguous day.** “Beach, or the Whitney if it rains” → one conditional row → Saturday has intermittent showers → useful recommendation or authorized resolution → each participant sees their relevant result.

Keep A10's compact expression. Distinguish a held backup from an explicit instruction to select it under a condition. A forecast changing does not universally authorize Vesper to choose a shared plan. Where judgment remains necessary, expose the useful recommendation in context, not a branching editor. The implementation needs condition meaning, evidence freshness, dependencies and action scope. It must preserve uncertainty instead of pretending “the weather settled” is a universal binary event.

**J-F — The day ends and something carries forward.** Passed occasion → refind the actual material → correct a factual relation or voluntarily contribute → a later relevant occasion benefits.

The current project is thin here. Define what happens to an unfulfilled possibility, how planned differs from happened, where contributed photos belong, and how a later return can reuse useful material without recreating the arrangement. Do not infer attendance from time passing or append an after-action questionnaire. Show one ordinary voluntary contribution/correction and one later reactivation. The Plan page connects to Life and Place owners; it does not absorb their organization, media, or memory responsibilities. Personal outcomes need not converge into one shared story.

**A9 refinement.** An untimed collection is already a complete useful state. Remove the routine “Say a day and one of these becomes Saturday's page” instruction. Keeping possibilities does not incur a scheduling obligation. Contextual asking remains available; Home/Places can surface a justified opening when it becomes useful.

#### B. Coverage is not a claim that Plan contains the whole app

| Use-case family | Current evidence | Remaining responsibility |
| --- | --- | --- |
| Structured Trip and upcoming logistics | Strong compositions | Integrate with existing canonical travel truth and native navigation |
| Loose local possibility | Strong sparse layout | Retention, identity, later refinding, temporal release |
| Read-only place understanding | Strong illustration | Grounded content and an actual contextual exchange |
| Comment, suggestion, authorized edit | Strong role examples | Consistent entry, target persistence, scoped grants and repair |
| Dinner-only, skip and rejoin | Useful examples | Continue after changed participation or reunion constraints |
| Disruption and practical rescue | Good first response | Incompatible responses, infeasible provider outcome, delivery uncertainty |
| Untimed and conditional arrangements | Useful A9–A10 treatment | Conditional authority, ambiguous conditions, no scheduling homework |
| Photos, knowledge, food, labor, care | Contribution results illustrated | Lightweight author/guest creation and correction paths |
| Guest without installation | Value-first recipient page | Delivery, safe identity, bounded contribution and continued access |
| Recurrence and later continuity | Mostly adjacent scope | Define handoffs and one later-return journey, not a Plan archive redesign |
| Expense understanding/accounting | Not covered here | Adjacent assisted experience; preserve deterministic calculations where promised |
| Cultural connections, rich media, broader Home/Places value | Adjacent responsibilities | Compatible references and return paths, not additional mandatory Plan sections |
| Booking execution | Intentionally excluded | Retain useful external handoff and supplied reservation evidence |

The [Product Model](../../travel-agent/docs/product/Product%20Model.md) and [Multiplayer Product Strategy](../../travel-agent/docs/product/Multiplayer%20Product%20Strategy.md) include private caucus, meaningful contribution, repair, recurrence and later reactivation. The present boards cannot be described as complete coverage of that larger vision. Deliberate scope boundaries are not missing screens; an unowned handoff or unfinished outcome is a genuine gap.

#### C. Engineering: reusable presentation, substantial domain integration

**Assessment:** moderate presentation work, substantial integration/domain work. Reducing the frontend's operations inventory remains valuable, but it transfers responsibility into reliable interpretation, authoritative commands and coherent readback. Relative complexity below is a planning judgment, not a calendar estimate.

| Area | Relative complexity | Why |
| --- | --- | --- |
| Editorial page and sparse variants | Moderate | Reuse header, row, time gutter, rail, chapter and sheet primitives |
| Contextual assistance and Chat continuity | High | Target context, conversation ownership, streaming, expansion, interruption and return |
| Lightweight intent without a Trip | High | Stable identity/owner, optional timing, retention, association and release |
| Contributions and scoped collaboration | High | Different command effects, authorship, grants, revocation and concurrent writes |
| Participation and changed agreements | High | Individual decisions coexist with one shared consequential fact |
| Grounded adaptation/conditional plans | High | Model judgment plus deterministic feasibility, evidence and dependency checks |
| Recovery across roots | High | Retry identity, stale actions, causal repair, readback and cache invalidation |
| Non-app guest contribution/delivery | High | Bounded identity, access, delivery and response continuity |

Concrete reusable foundations and gaps from the inspected code:

- [LocalPlanScreen](../../travel-app/components/trip-plan/LocalPlanScreen.tsx) already composes a lighter local page, but still takes `tripId` and Trip state. [planShape](../../travel-app/data/planShape.ts) is also Trip-scoped. Sparse presentation is not yet evidence of Trip-independent material ownership.
- [Plan graph models](../../travel-agent/backend/core/models/experience_graph.py) provide owner, horizon, lifecycle and Commitment references. [update_plan and graph commands](../../travel-agent/backend/domains/experience_graph/commands.py) provide owner checks, expected revisions and idempotent receipts, plus invitation/decision facilities. The inspected Plan update is metadata mutation, not a complete lightweight-material/scoped-collaborator editor.
- [Plan Shape compilation](../../travel-agent/backend/core/plan_shape.py) supplies viewer-relative participation logic over canonical itinerary data. Reuse its useful guarantees, not its status buckets as page organization.
- [PlanStopInspectSheet](../../travel-app/components/trip-plan/PlanStopInspectSheet.tsx) still offers details/change operations; the [main Plan route](../../travel-app/app/%28tabs%29/trips/[tripId]/plan.tsx) also enters contextual entity inspection. Resolve one deliberate integration with the entity lane instead of adding another competing detail or assistant surface.
- [Root consequences](../../travel-app/data/rootConsequences.ts) provide server-resolved actions, repair and broad read-model invalidation. Extend the appropriate owner adapters and validate new cache dependencies rather than duplicating actions on each root.
- The [Trip bridge](../../travel-agent/backend/domains/experience_graph/trip_adapter.py) explicitly preserves legacy execution ownership. A new design does not authorize competing graph and block writers or deletion of guarantees before cutover.

AI can interpret intention, compare grounded alternatives and explain outcomes. It must not replace authoritative state, deterministic time/route constraints, permission enforcement, or expense arithmetic with generated prose. New schema/auth choices and migration remain separately approval-bearing. Reuse the existing implementation handoff's A0–A4 dependency sequence; this design supplement does not approve it for execution or supersede its owners.

#### D. Next deliverable: journey-to-system coverage, not another broad visual brief

Add a compact coverage specification to the receiving agent's existing report. For J-A–J-F record:

1. Starting evidence/state and the person's expected value.
2. What is delivered before asking for additional input.
3. Entry, target, current result, and return/refinding path.
4. Canonical owner; what changes, remains private, and stays untouched.
5. Interruption, disagreement, non-application and later-return behavior.
6. Existing component/service/command to reuse, or a precisely named engineering gap.
7. Evidence status: illustrated, wired in the artifact, simulated/tested, existing runtime, or proposed.

Prioritize five missing continuations: Keep without a Plan → refind → release only timing; thin guest → question/contribution; incompatible participant/provider response → useful resolution; ambiguous conditional day → appropriate recommendation/action; ended occasion → later useful continuity. Apply the J-B follow-up consistency correction across older examples too. Illustrate only the transitions necessary to expose these decisions using existing patterns, with detailed visual judgment left to Claude Design. Do not turn each case into a bespoke operation screen, new service, schema noun, or root redesign.

Coordinate stable targets, session/history ownership, evidence custody and return behavior with Chat, Entity and Home/Places/Life. Where their contract is unresolved, name the question and owner; do not silently decide it in a mock. Update stale board-07 descriptions of routine memory offers and settled draft retention so they agree with the later rulings. Keep participant/native validation unclaimed.

**Completion criterion for this assignment:** the designer and engineer can trace the full representative portfolio through a small interaction family, know who owns each effect, and see where genuine behavior or contract decisions remain. Architecture should cover the system; delivery can follow dependencies. No single-loop proof gate, universal Plan container, or claim of complete product coverage is implied.

### 0.7 Post-subtraction refinement: simplify the machinery, preserve the help

**Review-stage note:** §0.8 records the subsequent September 6 export and governs the current bounded assignment. Keep the research and boundaries below; do not repeat corrections that the later review marks as addressed.

**Verdict and provenance — September 5.** The founder accepted the preceding research-backed recommendation to retain the simplified direction and refine effort within it. The reviewed export has files dated 15:25: reduced main boards, seven sentences on board 07, and engineering appendices 90–92. This is a credible Plan/Occasion design direction, not validated usability or complete product coverage. This update draws on the local design/source review and online research; no participant study, new native acceptance test, production implementation, or live-design sync was performed for this handover update.

**Precedence.** Read the [accepted seven-sentence decision](../decisions/2026-09-05-adopt-the-plan-in-seven-sentences.md), [kernel §11.15](design-kernel-extraction-2026-08-29.md), and [execution report §3l–3o](claude-design-plans-in-real-life-execution-report-2026-09-04.md). Preserve their subtraction and owner-default direction. The founder has requested this refinement brief; it does not silently rewrite the accepted decision. Where the recommendations below relax literal rules—mandatory “Or say…”, no recommendation buttons, or silent pending—label the difference in the design/report as a proposed amendment. A subsequent canonical change needs a new decision, as the accepted record requires. Do not revive PR-1/PR-2 or expand authority through copy changes.

**One governing aim, not another grammar:** reduce the work required to receive value and reach an understandable result. Fewer screens, words, or controls are not sufficient if people must instead invent prompts, repeat context, reconcile facts, or carry messages manually.

#### A. Preserve the design we have reached

- Keep the continuous editorial page, warm paper, serif hierarchy, compact time gutter, sparse untimed states and full-day legibility. Use the existing typography, spacing, material and overlay roles in §4; no new visual language is requested.
- Keep one contextual Vesper interaction family for understanding, exploration and changes. Preserve the active field and optional voice; no permanent conversation feed on the resting plan and no input field under every row.
- Keep owner-default changes, scoped grants, independent participation, voluntary contributions, and the distinction between private assistance and explicit messages to people.
- Keep useful finite controls, external provider doors, truthful recovery and retention of the person's words. Appendix placement does not remove engineering obligations.
- Keep temporal release, voluntary after-day contributions and useful continuity. A loose possibility is already a valid result; no scheduling obligation or post-event questionnaire.

#### B. The actual changes to make

**1. Let an answer be complete.** Audit the “Or say…” lines on 08 P2b/P3/P4/P9a, 09 J2a and 02 A4 against the current live version. Remove the requirement to append a suggested instruction after every answer. Keep a contextual example only where it reveals a useful, otherwise non-obvious capability or resolves likely uncertainty. Preserve the active field so “She's fine walking; it's crowds she dislikes” remains easy. Do not replace the removed line with a chip carousel, engagement prompt or “Something else…” branch. Proposed amendment to sentence 2's discoverability addendum: guidance is selective, not compulsory.

**2. Carry context instead of repeatedly asking for it.** Opening from dinner already supplies dinner as the target. Use that context for “move this to ten” or “Wednesday morning, leave the time open.” Clarify only consequential ambiguity: moving the temple versus the whole outing may require a question; choosing the object again after explicit selection generally does not. Retain exact provider facts and the arrival-versus-performance distinction. Do not add scope forms or rely on exact scripted phrasing as the real product contract.

**3. Reduce repetition on I1 before adding anything.** The current top thesis still says dinner is with Maya and Sam while the row says Sam cannot do eight. Correct the summary from the same current state. Give the top line the unresolved implication, the dinner row the current arrangement/participation, and the attached contribution Sam's actual words when useful. Do not repeat the same objection at every level or add a status region to explain it.

**4. Allow useful judgment without taking over.** I1's compact facts are useful but should not be the ceiling of Vesper's assistance. An illustrative supported possibility is: “Keeping seven preserves the reservation. Maya could join after the reading, if a staggered dinner works for you.” This is not a claim that seven works for Sam, that Maya agrees, or that the reservation has changed. Use the fixture's evidence and expressed priorities; name the tradeoff, do not invent feasibility. Similarly, J2f should relate the changed timing to the expressed crowd concern, not merely recite the new schedule. One relevant implication or possibility can replace repetitive facts; no compulsory recommendation section, scolding, or menu of alternatives. Recommendation, adoption, and execution remain separate effects—not three new screens. Consequence-aware recommendations are deferred in the accepted decision: any illustrated refinement must be labeled proposed, not quietly promoted to a shipped or approved capability.

**5. Keep obvious selections easier than describing them.** The real 8:30/10:30 set choice, RSVP, Keep, Send and supported Undo remain useful. Do not add comprehensive Move/Replace/Skip menus. Conversely, do not remove an already-clear selection solely because it follows an AI recommendation and force “yes, choose that” to be retyped. Where a single direct adoption would materially reduce effort, show at most a small proposed treatment within the existing family and record the explicit exception to sentence 6's no-button rule. Do not silently restore the former J2f/I1 chips. No new full-screen variant is needed to discuss this exception.

**6. Keep the host in control without making them a courier.** In D3/G1/J3, carry the known change into a prepared message with the actual recipients and outgoing words visible beside Send. Let the person edit before sending; distinguish prepared wording from words they already authored. Avoid a separate mandatory messaging workflow or retyping the change. Never treat a private question as permission to send, rewrite an authored suggestion silently, or imply another person's acceptance. This is preparation in the existing exchange, not autonomous communication.

**7. Quiet resting page, legible active response.** A submitted request needs a small acknowledgment in the active interaction. Preserve words and prevent duplicate effects while its outcome is unresolved; do not show the change as completed. No permanent progress/status panel is needed. Unknown is not failure or confirmed non-application. Proposed clarification to sentence 7: “pending is silent” should govern resting-page clutter, not erase acknowledgment of a person's submission. Likewise, per-day bundling is a nonurgent default to review, not permission to suppress a distinct urgent change. Keep detailed delivery/recovery cases in the appendix.

**8. Preserve planned versus happened in F1.** “We went to the river, not the café” reports an occurrence; it is not automatically an instruction to rewrite the original plan. Keep the supplied account distinguishable from the earlier intention without exposing an outcome editor. Resolve custody with the Life/contribution lane; do not manufacture attendance from midnight passing or force everyone's personal account into one story.

#### C. Research basis: support the direction without turning evidence into absolute rules

- **Prompting has a cost.** [Tankelevitch et al., CHI 2024](https://www.microsoft.com/en-us/research/publication/the-metacognitive-demands-and-opportunities-of-generative-ai/) synthesize metacognitive demands around expressing goals, evaluating outputs and managing workflows. This is a framework, not a Vesper trial. Our inference: evaluate total user effort, not only interface size.
- **Contextual guidance is useful; a mandatory next prompt is not established.** [Subramonyam et al., Gulf of Envisioning](https://arxiv.org/abs/2309.14459) analyze capability, language and intentionality gaps in LLM interaction. Our inference: reveal helpful possibilities where needed; do not presume every answer needs another suggested instruction.
- **Language and direct interaction can complement each other.** [Horvitz, CHI 1999](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) develops principles for coupling automated services with direct manipulation. It is not a modern mobile benchmark or evidence that tapping is universally “10× faster.” Keep only the controls that remove real work in these journeys.
- **Timing is contextual, not universally “after a problem.”** [Kuang et al., CHI 2024](https://emilykuang.github.io/lab/publication/chi24-ux-proactive-ca/) studied 24 UX evaluators analyzing usability recordings in a hybrid Wizard-of-Oz setup. They preferred suggestions after potential problems; timing did not significantly affect analytic performance. This does not establish a universal restriction for everyday assistance. [Chen et al., CHI 2025](https://www.microsoft.com/en-us/research/publication/need-help-designing-proactive-ai-assistants-for-programming/) report benefits and contextual nuances in a randomized programming-assistant study; it also is not direct evidence about travel or social coordination.
- **Make invocation, correction and consequences understandable.** [Microsoft's human–AI guidelines](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/) support contextual timing, short-term continuity, clarification under uncertainty, and efficient dismissal/correction. They explicitly involve tradeoffs, not a mechanical checklist or validation of a particular sheet.
- **A competitor convention is not an optimality result.** [Partiful's date/time documentation](https://help.partiful.com/en-us/articles/15525367-how-do-i-change-the-date-and-time-on-my-event) explicitly says guests are not notified automatically and the host must send a text blast. This supports a familiar human-authored communication model, not the conclusion that Vesper should require a separate manual communication chore.

Do not repeat “help is welcome only after a problem,” a universal five-notifications-per-week abandonment threshold, or a fixed tapping-versus-language speed multiplier as settled research. The current pass does not validate those generalizations. Keep product choices clearly separated from evidence; correct overclaims in the receiving report without silently rewriting accepted decision history.

#### D. Bounded delivery and stopping point

This section replaces the older broad composition/coverage requests for the current iteration. Return:

1. The same reduced design family, with the changed existing frames identified. Keep appendices 90–92 labeled as evidence; do not regenerate the earlier ~90-frame main family.
2. A short before/after effort log for loose Saturday, shared dinner and the changing day: where the revision removes a prompt, repeated context, duplicated fact, unnecessary navigation or manual coordination. Include a successful read-and-exit with no further action.
3. A concise amendment list separating changes compatible with the accepted seven sentences from proposed exceptions requiring a new decision. Do not create another sprawling rule system or silently change upstream authority.
4. Verification of affected rendered states and existing bounded prototype regressions where wired. Report illustrated, scripted, mechanically checked, native-unverified and participant-unverified portions separately. Do not claim live sync from local edits alone.

Stop when the existing family delivers useful orientation, allows natural continuation, and makes the result and audience understandable with less work. Further participant walkthroughs should use goals rather than button instructions and observe prompt invention, rebriefing, uncertainty and repetition. They can proceed alongside system implementation; this is not a single-loop proof gate or a request to halt adjacent architecture.

**Final direction for Claude: keep the page calm and the assistance capable. Remove the obligation to operate, prompt, or coordinate unnecessarily—not the substance that makes Vesper worth using.**

### 0.8 September 6 export review: finish the content and continuations, not another redesign

**Evidence and verdict.** The review inspected the local export with files dated September 6 at 11:50, compared its changed frames with §0.7 and execution report §3p, and rendered boards 05, 09 and 11 in the in-app browser. The direction is stronger and should be retained. This was a local artifact/source review, not a fresh live-project sync, native acceptance test, participant walkthrough, or production code audit. The new treatments remain illustrated; report §3p says the interactive prototype was not updated for this pass. Do not count its older regression results as execution evidence for the new message or recommendation paths.

#### A. Addressed findings: preserve these gains

- Routine “Or say…” lines were removed from 02 A4, 08 P3/P4 and 09 J2a. The field remains; selected contextual examples remain elsewhere. Do not restore compulsory follow-up nudges.
- D3 now prepares actual wording addressed to Maya and Sam, with Edit and explicit Send. Keep this reduction in composition work.
- I1 fixes the false “with Maya and Sam” summary and offers one useful staggered-dinner possibility instead of only reciting incompatible facts. The proposed shortcut is explicitly labeled as an exception, not quietly adopted canon.
- F1 now preserves the original planned material separately from Nora's account. No checkmarks or attendance inference appear merely because the day ended.
- The reduced main-board family remains intact. None of the refinements below requires restoring the earlier operations inventory.

#### B. D3 — make the outgoing message the center

**Observed friction.** D3 now reduces typing but asks for substantial reading: preview heading/time, separate Maya/Sam/table explanations, the outgoing message, prepared-versus-authored explanation, and correction-versus-unsending explanation. Several layers communicate the same change. This is predicted cognitive effort from the rendered composition, not measured participant behavior.

**Refinement.** Let the actual message and recipient names lead; retain the practical consequence not settled by sending. Illustrative content hierarchy, not an exact wireframe:

> **To Maya and Sam · Draft**
>
> Dinner's moving to eight, same place. Sam—does eight work for you?
>
> Your table is still reserved for seven.
>
> **Send to Maya and Sam** · Edit · Not now

Keep any additional information only if it changes the decision. Remove ordinary customer copy such as “it becomes yours when you send or edit it”; a Draft label, visible words and explicit Send establish the relevant expectation without explaining the internal authorship model. Preserve authorship and correction behavior underneath. Detailed unsend/repair limits can appear when relevant rather than as a permanent footer on every prepared message.

D3 follows an explicit owner instruction to move dinner. Make clear if its primary action both updates the arrangement and sends the announcement; where that is the actual intended effect, a label such as “Update & send” may be clearer than bare “Send.” Do not imply the restaurant changed, Sam agreed, or delivery succeeded merely because the message was submitted. Reuse the existing preview/receipt pattern; no second confirmation ceremony is requested.

#### C. J2f — preserve social intent, not merely individual scheduling freedom

**Observed inconsistency.** The customer sentence now says “10:15 is still yours to take if early matters,” while the annotation says neither going alone nor approaching Ben is recommended because who is coming was never established. The wording implicitly encourages a separate visit despite that limit.

Replace this with a grounded implication that leaves the relationship intact. For example:

> Ben moved the visit to eleven, after the quieter window we discussed. Going together at 10:15 would need his agreement.

This example concerns agreement to attend together, not a new requirement for owner approval on an otherwise authorized edit. Preserve scoped editing rights and independent participation. Use the supported fixture context; do not invent that Ben is available at 10:15 or that a companion is definitely attending. Keep the ordinary contextual field/pill available, with no forced follow-up, social-split recommendation, new button panel or implicit disclosure of private context. Align the annotation with the final customer wording.

#### D. F1 — retaining the original plan does not require it to dominate the later account

**Observed friction.** The structural correction is right, but the café still has the prominent activity title while the river—the experience Nora reports—appears as a subordinate correction. Someone returning to understand their day must reconstruct what happened from notes beneath things that did not happen.

Within the existing entry, explore giving the reported experience appropriate prominence while keeping the original intention available. For example:

> **An afternoon by the river**
>
> You said you went here instead of the café.
>
> Originally planned: Willow & Page café.

This is a source-attributed presentation, not permission to overwrite Plan truth, create a verified shared Occurrence, invent an exact river location/time, or assert that every named participant attended. If the surface is explicitly displaying the original itinerary, retain that reading; give the person's account a clear, useful treatment rather than silently switching the whole page into an authoritative history. Coordinate any later Life projection with its existing owner. Do not introduce an outcome editor, a new mode taxonomy, or a memory-maintenance task.

Remove “What was planned stays as it was” from routine customer copy. Keep that invariant in the design/engineering annotation. The user should receive the account, not a lesson in storage semantics.

#### E. I1 — define what “Prepare that for Maya and Sam” actually prepares

The shortcut is a useful reduction in retyping. Calling it a “door” rather than a “button” does not settle its consequence or exempt it from the proposed sentence-6 amendment.

**Recommended treatment for this fixture:** preparation does not change the eight-o'clock arrangement. Because I1 follows an optional suggestion rather than an explicit instruction to change the plan, prepare a proposal to the two people, for example: “Could we keep seven? Maya, would joining after the reading work for you? Sam, would seven work?” Show the actual recipients and editable wording. A clear “Send proposal” sends that message, not a plan mutation or an announcement of a settled decision. Silence is not acceptance.

Contrast D3, where the owner already instructed a move. If the owner instead explicitly asks from I1 to keep seven and tell both, the same interaction family may prepare an update-and-announcement, with that effect clearly named and owner-authorized. Do not make every owner edit depend on a new group approval workflow. The distinction comes from expressed intent and the outgoing effect, not from adding a new operation screen.

Show the immediate result of the selected I1 path using the existing outgoing/readback treatment: what was sent, whether the arrangement changed, and what remains unanswered. Canceling preparation must not change the plan or contact anyone. No provider change or acceptance by another person follows automatically. These are design expectations under the [Contribution and Consequence contract](../systems/contribution-and-consequence.md), not a claim that delivery or the command path is implemented.

#### F. Bounded delivery and stopping point

1. Refine the existing D3, J2f, F1 and I1 treatments; preserve typography, paper, spacing, full-day readability and the rest of the reduced family. Detailed visual composition remains Claude Design's job.
2. Trace I1's one chosen continuation into the existing outgoing-message/readback family, contrasted with D3's explicit change. Reuse an existing frame or interaction state where possible; do not create a proposal-management suite.
3. Update stale board annotations and the report so they match the illustrated behavior. Selective prompting is a relaxation of the accepted literal “after every answer” addendum; record that alongside the proposed recommendation/action and pending-feedback amendments rather than calling it unchanged canon. Do not rewrite the accepted decision history.
4. Verify the affected rendered states, recipient wording and meaningful action labels. If any continuation is wired, check preparation, dismissal, submission and return against the stated effects. Otherwise mark it illustrated, with prototype/native/participant limits explicit. Preserve unrelated existing work and inspect the live project before syncing.

**Stop after this content-and-continuation cleanup.** Do not add more conceptual rules, expand the main family to cover every appendix case, or start another composition exercise. The next gains should come from making these existing interactions natural in use, alongside the established engineering work—not from further growing the handover's screen inventory.

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

For this review iteration, follow §0.8's content-and-continuation cleanup, preserving §0.7's gains, the post-subtraction main family, reduced board 09, and A9–A10's lighter forms. Older coverage requests in §0.6 and broad composition steps above remain context and appendix evidence, not an instruction to restore removed frames, restart all four situations or redesign adjacent roots.

### Phase C — make the visual consequences interactive

- Selective direct controls and supported contextual language examples must change the same fixture state or fail honestly. Do not make arbitrary input appear understood by advancing to a predetermined success screen. Implement §0.1's stress cases through the same interaction family, not six separate editors.
- Identify scripted recognizers outside the consumer frame. Unsupported inputs should preserve current state and offer a supported continuation.
- Keep actor/viewpoint and world-event controls in research chrome, not the customer interface.
- Re-entry must show the current state; navigation Back must not undo an edit.
- Keep, preview, adopt, contribute, participate, grant/revoke, and external handoff must have distinguishable effects even when their UI is small.
- Let ordinary interactions feel ordinary. Do not add a receipt card for every tap merely to expose correctness to the researcher.
- Follow §0.8 for the current interaction refinement and retain §0.7's simplification boundaries. Keep §0.3–0.6's context, audience, uncertainty and recovery evidence in the appendix; exercise relevant existing regressions without turning the earlier coverage inventory into new main-board screens. Keep prototype recognizer limitations separate from the product's supported capabilities and genuine execution boundaries. Do not build production infrastructure merely to make an artifact appear complete.

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

**Current-iteration override:** deliver §0.8.F's bounded cleanup and continuation review, preserving §0.7's amendment distinctions. The original full-project inventory below is retained for provenance; reuse existing material rather than treating it as a fresh assignment or restoring pre-subtraction screens.

Original full-project delivery inventory:

1. **Project URL and active-board map**, with the original kernel lab clearly separate.
2. **One recommended complete design family**: four full-scroll situations plus the small overlap extension.
3. **Essential interaction paths and journey-to-system coverage**: preserve the §0.3–0.5 journeys and passing regression cases, then cover §0.6's entry/refinding, guest contribution, incompatible responses, ambiguous conditional resolution and later continuity. Supply the §0.6 coverage specification with owner boundaries, existing-code reuse, engineering gaps and adjacent-lane decisions. Report illustrated, wired, simulated/tested, existing runtime and proposed portions separately; do not claim every broader product use case is contained in Plan.
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
