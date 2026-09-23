---
doc_type: working
status: active
owner: founder / design orchestrator / mobile and content owners
created: 2026-09-15
last_verified: 2026-09-21
expires: 2026-10-15
why_new: Defines a bounded cross-repository implementation plan connecting generated and direct content to reusable native patterns and current-app improvement; the design-language brief owns Claude consolidation, the earlier polish note owns historical QA research, and the program roadmap must remain a concise priority register rather than absorb this technical plan.
supersedes: []
source_of_truth_for: []
---

# Content-to-native quality consolidation

**September 21 parallel-lane planning:** [section 13](#13-september-21-native-presentation-lane-execution-plan)
turns the existing Q0–Q5 packages into a proposed native presentation lane
alongside Orchestration. It records the newer functional candidate, useful
presentation work on a divergent receiving branch, explicit file ownership,
three delivery waves and separate functional/visual completion evidence.
This update is planning only: no lane has been dispatched, no active ownership
has transferred, and no integration, publication or activation has resumed.
Earlier implementation receipts below remain dated evidence, not the baseline
to clone blindly or a claim that those changes exist in every candidate.

## 1. Outcome and decision

**Quality is core product functionality. The outcome is a more polished current
app whose ordinary future development also produces coherent results with less
manual correction.** This is not a tooling project whose benefit is deferred
until a later restyling sprint.

The founder requested this detailed plan after September 15 research into
full-stack content and visual quality. Documentation and a first bounded
implementation slice are authorized. Packages below are execution units, not
claims that the entire quality program has landed. Existing work continues
under its current owners.

**Second review, September 15:** the direction survived product-contract,
external-practice and adversarial-case review, with corrections below. There is
no single established “SOTA polish stack.” Current agent engineering reports,
validated HCI guidance and native platform guidance support different parts of
this plan; none certifies our product quality. Key corrections are preserving
depth and wanted participation, resolving contradictory older instructions,
testing against capable alternatives, explicit accessible instruments, and
adopting improvements during construction rather than after a tooling phase.

There are two inseparable success conditions:

1. **Current experience improves:** useful content, hierarchy, reading density,
   native typography, instrument legibility, states and interactions improve in
   the actual mounted app against selected designs.
2. **Improvement compounds:** shared patterns and content agreements absorb
   ordinary variation, so a new consumer does not require repeated local
   typography, copy-shortening, spacing and interaction decisions.

Neither more components nor more tests is an adequate substitute for these
outcomes. A package that builds infrastructure but leaves its selected current
consumer unchanged is incomplete unless explicitly scoped as preparation.

### First execution cut — September 15

The isolated `codex/quality-comparison-2026-09-15` mobile lane committed
`d030ab384` from mobile base `73e966e9d`. The selected current consumer is the
ordinary New York Places field's Red Hook arrival/return comparison. Its native
case rows previously joined values without naming their **Arrival** and
**Return** axes. The shared Places lead anatomy now shows each axis and value
as a compact paired metric, keeps the currentness limit visible, and announces
the full case with both axes to assistive reading. Home's presentation path is
unchanged. A fixture-backed consumer test and existing Places root tests cover
the receiving boundary; this is a small Q0/Q1/Q2/Q4 adoption cut, not a new
quality framework.

The mobile Design Language and Claude design-system rule were narrowly
reconciled with the current Product Thesis: everyday usefulness is an
independent entrance, evidence-led comparisons are allowed, substantial depth
may follow a quick first return, the limited shared italic role actually
exists, and new semantic compositions do not inherit a blanket legacy
storage-clamp/frontend-mirror requirement. The backend Source contribution
prompt and semantic validator already require an additive first-screen claim,
a relevant comparison axis, limits, and exact Source bindings; no producer or
wire change was justified for this case. Their live-model quality remains
unproved by deterministic fixture tests.

Evidence at this cut: mobile typecheck, 50 focused tests across anatomy,
renderer, Places presentation and mounted-root units, mobile doc checks, native
dependency compatibility, and selected design-reference resolution passed.
The feed refactor landed as `5d7eef682`; the active mobile task guidance
alignment landed as `036d92462`. The first mobile `verify:pr` run exposed a pre-existing
`components/places/PlacesSectionFeed.tsx` size budget failure (565 lines
against 332). A second isolated, behavior-preserving slice moved server-authored
mixed page ordering into `placesPageRenderItems.ts` and the local time spine
into `PlacesTimedWindowCue.tsx`; the feed now contains viewport/render framing
at 331 lines. The unchanged budget passes, and all 53 feed tests pass (103
focused tests across both slices). The
next `verify:pr` run reached the lint-warning ratchet and failed at 170 warnings
against baseline 169, a debt count already observed before this refactor; its
new files have no lint warnings. Independent parity checking also fails in
pre-existing Chat/data query-key ownership findings; component-catalog checking
reports three already-unregistered UI files outside this cut. Do not silently
raise ratchets or add registry entries solely to call this lane green. Native
capture is **unverified**:
an isolated iOS simulator showed a first-launch “Open in Travel App?” prompt,
and the locked Mac prevented dismissing it through the UI. A fixture test is
not a screenshot or real-backend readback. Reattempt the registered
`places-workspace-ordinary-nyc` capture after unlock; compare the full scroll,
source/read depth and large-text layout to the pinned Places reference before
promoting visual acceptance. No main or child branch was published by this cut.

### Locked-Mac offline portfolio — September 15

This portfolio extends the existing backend Source-contribution and Places
runtime tests plus the mounted mobile field/reader tests. It is an execution
receipt, **not** another scenario registry, screenshot authority, or a claim
that all rows share one producer. The Red Hook mobile material is hand-authored
deterministic mock supply; backend Source rehearsals use their own deterministic
producer; a live provider result has not been evaluated here.

Mobile adoption/test commit: `492cbee36` on the isolated quality lane. The
ordinary New York practical mock no longer claims an unsupported positive fit
or exposes fixture machinery in its user-facing basis. The shared receiving
preview no longer calls an unverified sender a travel companion. Focused
mobile evidence: 111 tests across eight mounted suites, typecheck, changed-file
lint, Places scenario IDs and externally verified design-reference bindings.
Focused backend evidence: 60 offline Source contribution, rehearsal,
original-adapter and Places runtime tests using the receiving lane's dependency
venv with `PYTHONPATH=.` verified to import **this** isolated backend checkout.
That interpreter reuse does not replace a clean lane environment or `make ci`.
The isolated mobile `npm run verify:pr` advanced through lint, typecheck,
API boundaries, schema bridge, surface budgets and test-contract typecheck,
then stopped at the repository lint-warning ratchet: **170 warnings against a
baseline of 169**. Changed-file lint for this slice was clean. This is a
failed broad gate, not a visual or producer-to-receiver acceptance verdict;
the warning debt must be attributed and resolved before publication. Native
visual QA remains unrun while the Mac is locked, and no branch was merged or
published.

| Case and owner | Value before tap; omission that should fail | Offline boundary |
| --- | --- | --- |
| **Public Red Hook, no history** — current public ferry/MTA/Parks material, Places field selection | A usable asymmetric arrival/return reading with both comparison axes and current-service limit. No inferred personal history, friend material, or request for input. | `test_source_contribution_rehearsal.py` proves a *single* public Source is insufficient for governed editorial synthesis and returns selection silence; `PlacesSemanticField.test.tsx` proves the separately hand-authored public Places field still returns practical value. Silence in one lane must not be mistaken for an empty product. |
| **Maya's Red Hook original** — Relationships delivery `ordinary-nyc-maya-red-hook`, revision 2 | Her exact note appears as attributed human value, not Vesper prose, and opens the exact owner reader. Withdrawal or a wrong recipient removes the material without fabricating a social insight. | `test_original_delivery_adapters.py` checks backend viewer-safe candidate shape; `PlacesOriginalDelivery.consumer.test.tsx` checks exact mock recipient read, sender withdrawal, and stale-unit/wrong-recipient refusal. `RootOriginalDeliveryPreview.loading.test.tsx` keeps an unverified sender unnamed and removes travel-only framing. |
| **Valentino Pier visit, 90 minutes** — explicit Places visit request with public route shape | A conditional ferry/harbor possibility and visible **unknown** return fit; no supported timing claim or Add-to-Day consequence without a current route-owner read. The existing map door remains available. | `test_places_runtime.py` proves the practical request participates in server-authored field order; `PlacesSemanticField.test.tsx` checks hand-authored mock copy, assessment state, typed map capability and absence of a supported fit. `PracticalAssessmentDisplayExpiry.test.tsx` already withdraws expired prose and accessibility with its label. The mock does not prove live service or use the exact request clock in its copy. |
| **Selective prior reachability** — same public Red Hook world plus authorized Sorrento observation | The public lead remains capable unchanged; one additional structural reading transfers a useful access distinction without declaring the person's travel style or reusing old attention as a current schedule. | `test_source_contribution_rehearsal.py` proves one governed private/public pairing can earn separately bounded editorial value; `PlacesSemanticField.test.tsx` checks the mock variation against the identical cold public lead. These are not the same Source identities and do not establish model quality. |

The intentional regression targets are: remove both axes from the compact
comparison; replace the cold field with a teaser; label an unknown visit as a
supported fit; expose Maya's original to a non-recipient; or promote a stale
sender name before its owner read. The mounted tests detect these specific
failures. Semantic interestingness, route correctness, optical fidelity,
whole-scroll composition, assistive navigation and real-backend readback remain
separate acceptance questions. The established controlled Pier 11 Source
rehearsal can later connect owner-backed producer to real Home/Places receiving
in one identity, but it requires a selected disposable local DB/runtime and
native acceptance; this offline portfolio does not impersonate it.

### Product constraints to preserve

- Home and Places return substantive value; they do not become sparse specimen
  galleries or demand further input to earn their output.
- Home remains a generous, prioritized whole scroll. Optimizing one card must
  not remove the page's richness or make all units equally prominent.
- Places preserves spatial understanding, scope, map/list identity and useful
  depth rather than becoming another Home feed.
- Chat and Life retain their own jobs. Shared pattern adoption is not permission
  to redesign either root or overtake their owners' active work.
- Make sense / Open possibility / Help it work / Carry forward are value moves,
  not four mandatory card templates or a one-move-per-tab mapping.
- Human originals, direct facts and practical state do not need AI-written
  commentary to qualify as value. Editorial novelty requirements apply to
  Vesper's added claims, not to every useful thing shown.
- Preserve selected compositions and consolidate obvious inconsistencies.
  This is not a fresh aesthetic search or another six-project redesign.
- Adapt to the desired benefit and present purpose, not just the topic. Preserve
  wanted choosing, making and exploring. Less unwanted work is the objective;
  fewer interactions is not universally better.
- Initial value means a substantive preview or usable object, not that every
  article, map, audio work or reconstruction must be consumed inside Home.
  Opening depth is legitimate; an empty teaser or withheld basic answer is not.
- Ignoring a result creates no obligation and is not evidence of dislike or a
  durable preference. Optional correction/dismissal uses existing scoped owner
  mechanisms; no new per-card feedback ritual or silent learning grant follows.

## 2. Authority, location and evidence boundary

The [program roadmap](vesper-program-roadmap.md) remains the single cross-lane
priority queue. The [integration roadmap](complete-system-integration-roadmap-2026-09-05.md)
owns technical integration and landing. This document is a supporting package
plan to be scheduled there, not a second orchestrator or permanent registry.

Read these owners when implementing their respective changes:

- [Artifact, expression and composition](../systems/artifact-expression-and-composition.md):
  semantic/native separation and distinct result families.
- [Contribution and consequence](../systems/contribution-and-consequence.md):
  input, human authorship, audience, commands, repair and receipts.
- [Mobile Design Language](../../travel-app/docs/Design%20Language.md), affected
  surface contracts and mobile Task Intake: native roles and verification.
- Backend product editorial and expression canons, current producer contracts
  and backend Task Intake: usefulness, evidence and production responsibilities.
- [Shared design-language consolidation](vesper-shared-design-language-consolidation-2026-09-10.md):
  accepted Stage 1 selection and design/native translation history.
- [Stage 2 instruments](claude-design-instrument-language-stage-2-handoff-2026-09-13.md):
  bounded exploration; candidates are not automatically required runtime families.

Historical implementation paragraphs in contracts and this plan are dated
observations. Reconcile them with current code and later accepted decisions;
do not use an old status paragraph to undo newer completed work.

### Research baseline

Research inspected the active receiving checkout at
`/Users/feihuyan/travel-workspace--receiving-completion-2026-09-10`, separately
from canonical `main`:

| Repository | Inspected HEAD |
| --- | --- |
| Receiving workspace | `3465b83a8f5f1e4032b3cfbc05ebd83168650c41` |
| Receiving mobile | `4c86ee380d4e6abb8af951fcb3c8d03c6680a03c` |
| Receiving backend | `7c56b8fd7b8dd5be0fb9a5fbe0b2c0acf4fa4130` |
| Workspace containing this plan | `6ab90baaae84cbd30136526511c20e791abb8989` |

Canonical child `main` revisions are older than that receiving baseline. Do not
implement against them assuming they contain the inspected changes. Receiving
roadmap edits and, by the documentation follow-up, Home composition, original
receiving, Places cards and capture-flow edits were concurrent and uncommitted.
They were not modified by this task. Establish fresh status, worktrees and file
ownership before implementation; HEAD alone does not identify dirty evidence.

### Concrete authority conflicts to reconcile before affected work

The mobile `docs/Design Language.md` in both canonical main and the inspected
receiving lane still contains “not a comparison table” (§2.1), a general
comparison-table anti-pattern (§11), a response-under-five-seconds rule (§2.4),
and group-travel-wedge wording (§1). The newer
[Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md),
[Product Model §4.1](../../travel-agent/docs/product/Product%20Model.md),
[expression canon](../../travel-agent/docs/product/Vesper%20Expression%2C%20Medium%2C%20and%20Projection%20Canon.md)
and [editorial canon §16](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md)
support everyday purpose-sensitive assistance, meaningful comparisons and
substantial depth. These are concrete instruction conflicts, not proof the
current implementation follows the older rule.

Q0 must give the affected mobile owner a narrow reconciliation: distinguish
unnecessary choice burden from an explanatory comparison; distinguish fast
recognition of initial value from a maximum reading duration; remove obsolete
wedge guidance from the affected owner instructions using accepted strategy.
Do not turn this into a repository-wide canon rewrite. This plan records the
conflict and its product grounding; it does not claim those child docs are fixed.

Research was source/document/history inspection and external literature review.
It did not execute native captures, live model production, user testing or
performance measurements. It does not establish the cause of every historical
design-to-app mismatch. The plan's tests and measurements are required future
evidence, not completed results.

## 3. What exists; what needs strengthening

Paths below are relative to the named child in the inspected receiving lane.
They are implementation starting points, not an instruction to duplicate files.

| Existing foundation | Evidence location | Remaining question |
| --- | --- | --- |
| Shared font families and semantic text roles | Mobile `constants/fonts.ts`, `constants/textVariants.ts`, `components/ui/Text.tsx` | Do the actual roles match selected native references across supported environments? |
| Bundled font loading and fallback boot | Mobile `hooks/useAppFonts.ts`, `hooks/useAppBootReady.ts` | Is fallback distinguishable in QA, and is typography stable during startup and large-text use? |
| Shared semantic anatomy and specialized Home forms | Mobile `components/root-projection/RootCompositionRenderer.tsx`, `RootCompositionAnatomy.tsx`, `components/home-root/HomeRootV2Composition.tsx` | Do all supported densities preserve useful meaning and qualifications without redundant copy? |
| Bounded generated proposals and semantic admission | Backend `backend/root_projection/v2/source_contribution_producer.py`, `source_contribution_prompts.py`, `semantic_composition.py` | Does valid content reliably fit its actual consumer rather than merely satisfy broad schema bounds? |
| Typed anatomy | Backend `backend/core/models/composition_v1.py` | Which existing semantic roles suffice, and where is a real producer/consumer distinction missing? |
| Selected design references and capture workflow | Mobile `docs/surfaces/home-root/design-refs/manifest.json`, `docs/surfaces/places-workspace/design-refs/manifest.json`, `scripts/polish-qa/` | Are producer, reference and native evidence evaluating the same case? |

Specific findings, not blanket defect claims:

- The producer asks for short first-screen copy, while schema bounds permit
  substantially more text. `root_composition_from_brief` maps `text_fallback`
  into `substance`. Broad transport limits are not a mobile presentation budget.
- Home has prose-sensitive qualifier de-duplication helpers. Recent corrections
  preserve qualifications unless their meaning is already visible. Preserve
  those fixes; investigate whether existing structured roles can remove the
  need to infer presentational redundancy from wording.
- Home's specialized sequence treatment preserves step details. Do not assume
  all compact treatments drop detail from reading a generic renderer alone.
- Typography and QA are already centralized. Starting replacement registries,
  another font system or another screenshot service would duplicate ownership.
- The current program already assigns Home/Places construction and C5a/I6
  content preparation. This plan supplies common quality improvements to those
  outcomes; it must not reassign their producer or surface responsibilities.

## 4. Architecture: improve agreements, preserve owners

The intended path is:

**Owner facts / permitted material → direct result or bounded generation →
semantic admission → native pattern → complete root experience → exact depth
and return.** Evidence cases should follow this same path.

| Layer | Owns here | Must not acquire |
| --- | --- | --- |
| Domain and Source owners | Identity, currentness, rights, actions and correction | UI geometry or a duplicate visual truth store |
| Content producer | Useful bounded claims, explanation, evidence and suitable semantic form | Component names, pixel sizes, routes or authority expansion |
| Admission/compiler | Supported structure and semantic invariants | A claim that schema validity proves intellectual or visual quality |
| Native shared patterns | Typography, grouping, adaptive layout, source treatment, interaction/accessibility mechanics | Inferring missing facts, silently rewriting originals or authorizing actions |
| Root owner | Page hierarchy, density selection, mixed content, selection and return | A fork of shared primitives for every card |
| QA | Traceable cases, structural checks, native inspection and bounded judgments | New product truth or a model score that overrides selected design intent |

Do not add a universal card, a generic server-authored UI tree, a new content
service, a cross-domain artifact writer or a rendering-specific persistence
owner. Adopt a new field or abstraction only after identifying the current
consumer that cannot be expressed clearly through existing contracts.

## 5. Reusable pattern agreements

A pattern is more than colors and padding. Its agreement includes meaning,
anatomy, behavior, variation and examples. Record these alongside existing
components/surface contracts; this table is a starting inventory, not a new
runtime taxonomy.

| Pattern | Required value | Variation and failure cases | Current-app outcome |
| --- | --- | --- | --- |
| Attributed original | Original material, author, relevant context, exact opening | Long text, portrait/landscape image, unavailable media, withdrawal, no added commentary | Recognizable human contribution without excessive framing or rewritten authorship |
| Comparison | Legible common axis, meaningful differences, explanatory payoff and relevant limit | Long labels, multiple axes, large text, unequal evidence, no image | Insight survives the compact form; tables do not become unexplained columns |
| Method / sequence | Ordered useful steps and essential instructions | Timed versus untimed, alternatives, longer essential detail, interrupted plan | A person can use it without opening depth to discover the crucial instruction |
| Reading / explanation | Useful substance on view, source identity and optional deeper reading | Short/long contribution, missing image, repeated opening, removed source | Editorial richness without a wall of duplicated headings and metadata |
| Spatial relationship | Place identity, supported relationship and correspondence to map/list | No map token, sparse data, out-of-scope place, long names, non-spatial material | Useful place understanding even when the richer map is unavailable |
| Practical update / instrument | Current owner-supported state, consequence and permitted next step | Unknown/stale state, no change, partial failure, preview versus applied change | Operational ability feels like useful help, not a management dashboard |

For every adopted pattern document:

1. The human job and when a simpler fact/original is better.
2. Essential meaning, optional depth, attribution and meaning-changing limits.
3. Supported anatomy and the existing semantic fields used to express it.
4. Compact/ordinary/depth variants only where consumers actually require them.
5. Layout response to longer content and accessibility settings.
6. Opening, focus, loading, unavailable and return behavior.
7. Selected reference, real consumer, owner and representative cases.

Character and item bounds protect production, but should not become universal
fixed heights. Avoid line clamping essential meaning. A short complete result
may stand alone; a longer complete result may legitimately take more space.
Do not generate a long essay, add a second summarization call for every card,
then rely on client truncation to make the system usable.

### Instruments and accessible depth are functional, not decorative

For selected instrument consumers, extend the existing pattern agreement with:

- What a position, length, color or mark means; units, time zone, comparison
  scale, unknowns and freshness where they affect interpretation. Missing data
  is not zero, and a decorative curve must not imply measured dynamics.
- A useful resting interpretation and an equivalent nonvisual reading of the
  relationship. Raw values alone may not convey the comparison or sequence.
- Explicit distinction between inspecting/selecting a value, previewing a
  proposal and committing an owner change. Dragging a mark does not imply an
  authorized mutation; provide an accessible alternative to precise dragging.
- Dynamic Type reflow, VoiceOver/TalkBack order, control role/value/state,
  focus restoration, non-color cues, sufficient targets and reduced-motion
  behavior. Follow supported platform standards; do not invent local numeric
  thresholds or disable scaling to match a screenshot.
- Long or unfamiliar place names, diacritics, missing glyphs, locale-sensitive
  dates/numbers and time zones. These are lived-world requirements even before
  a full multilingual launch; RTL expansion remains a separately scoped choice.

Audio/deeper formats remain within the product's expressive vocabulary, not new
implementation commitments in this package. When an existing selected consumer
uses them, preserve a useful preview, accessible alternative, playback/reading
continuity and exact return. Do not manufacture missing media for a quality test.

## 6. Implementation packages and order

Use dependency checkpoints, not a speculative day-by-day schedule. Parallel
work is allowed where file and semantic ownership are independent. Broad
architecture is considered throughout; incremental landing does not narrow
the product to one behavior loop.

**These are work packages, not six sequential gates.** Q0 resolves the baseline
for an affected pattern, not every pattern in the app. Its first owned defect
can immediately proceed through Q1/Q2 with Q4 adoption and existing QA. Q3
extends coverage alongside that work; completing new tooling or the full case
inventory is not a prerequisite for a safe, verifiable current-app improvement.
Q5 consolidates results as each coherent group lands. For a chosen pattern,
prefer one outcome assignment through agreement, implementation and adoption
over separate teams handing off each numbered package.

### Q0 — bind existing work and capture the improvement baseline

**Owner:** Design/quality coordinator with current receiving owners.

- Confirm current revisions, dirty ownership, selected designs and mounted
  consumers. Resolve live Claude sources through Design Sync; pin their
  revision/canvas/dependencies. Use saved exports only as dated fallbacks.
- Map the six pattern families above to existing implementations and supplier
  paths. Classify reuse, bounded repair, missing consumer and exploration.
- Choose a compact case portfolio spanning Home and Places first, including
  direct state and human material, not only generated editorial cards.
- Capture existing native behavior through the registered workflow when a
  device slot is available. Without it, continue source/contract work but leave
  visual baseline unverified.
- Record concrete defects and expected improvements, not a generic beauty score.
- Resolve the specific conflicting instructions in §2 for the affected pattern
  and pin its selected design/native contract. Do not require global document
  reconciliation before unrelated construction can continue.

**Exit:** named consumers, exact references, owned files, paired cases and
prioritized defects. No new standalone dashboard or six-project re-audit.

### Q1 — align content and native pattern agreements

**Owner:** Content/backend owner and native pattern owner jointly; one writer
per affected shared contract.

- Trace title, first-screen substance, anatomy, qualification and source roles
  from producer through admission to actual rendering.
- Resolve redundant versus essential copy with explicit examples. Use existing
  fields first. A changed schema needs a demonstrated failing consumer case.
- Add pattern-specific prompt guidance and deterministic structural checks
  where appropriate. Semantic quality still needs evaluated examples.
- Preserve originals exactly. Derived framing must remain separately authored.
- Define bounded treatment of malformed, overlong or low-value output: existing
  safe fallback, omission, or explicitly budgeted repair. Do not invent endless
  generation retries or remove necessary limits to fit the design.
- Retain each root's purpose rather than cloning the same expression everywhere.
- Compare a capable current-evidence result with selective authorized context
  while holding subject, geography and available evidence constant. Also test
  changed purpose and an over-personalized result. A no-history result may win;
  the producer must not add callbacks merely to demonstrate memory.

**Exit:** a current producer and native consumer agree on the same cases;
essential instructions, limits and attribution survive every adopted density.
If wire changes are necessary, generated contracts and consumers are verified
together before landing.

### Q2 — calibrate and repair shared native foundations

**Owner:** one mobile shared-pattern writer; root owners review affected uses.
May overlap Q1 after agreeing the pattern/content cases.

- Compare identical content in selected design and native rendering: actual
  font face/weight, apparent size, wrapping, line height, spacing and containment.
- Reuse `VText`, existing tokens and primitives. Make optical corrections at
  the semantic role or shared pattern where justified, not by scattered overrides.
- Check startup font fallback separately from normal loaded rendering. Do not
  assume a font embedding migration is required before measuring the problem.
- Resolve section/component header competition, source-strip weight, grouped
  spacing, image aspect/crop/fallback and touch feedback in real consumers.
- Preserve complete methods, comparison labels and practical currentness.
- Verify shared changes against sibling consumers and large text. Platform
  differences may require deliberate variants rather than identical pixels.
- Verify the instrument and accessibility conditions in §5 with actual controls
  and assistive navigation, not just screenshots or accessibility-label presence.
- Keep one production token/role authority and its existing exports. Design
  proposals become reviewed native changes, then exports are refreshed; do not
  independently edit parallel token files to make each project look aligned.
  Inventory consumers before removing a variant and preserve a scoped fallback
  for older content/client combinations when their lifecycle requires it.

**Exit:** paired native before/after evidence demonstrates improvements in
selected current consumers, with no known semantic or interaction regression.
A gallery-only implementation is not sufficient.

### Q3 — connect content cases to the existing quality workflow

**Owner:** mobile QA/tools contributor with producer owner. Tool-only files may
proceed alongside Q1/Q2; capture runtime remains exclusively scheduled.

- Bind case identity, material/owner revisions, production policy and expected
  semantic properties to the matching native fixture and selected reference.
- Distinguish hand-authored showcase, deterministic producer fixture and actual
  model output. None may impersonate the others.
- Extend existing scenario/reference infrastructure; do not start another
  visual registry or duplicate the authoritative data in screenshot metadata.
- Check missing essential content, unsupported actions, bad asset states and
  wrong destinations before subjective visual review.
- Review whole scroll and depth/return as well as individual components.
- Keep deterministic capture runs offline where possible. Separately authorize
  any metered model/provider run and record its input/output revision and cost.
- Keep tuning examples distinct from held-back quality cases. Pin evaluator
  rubric/model versions, calibrate against human-labeled good and bad examples,
  and inspect disagreements rather than averaging away a serious defect.
- Separate deterministic regression from sampled generative capability checks.
  Where model quality is measured, use repeated trials within an approved budget
  and report variation; one excellent generation does not establish reliability.
- Use synthetic or explicitly authorized/redacted personal material in captures
  and evaluator inputs. Screenshots can expose private friends, location or
  artifacts; fixture convenience is not permission to export them to a judge.

**Exit:** the same case can be traced through content and native evidence, and
an intentional meaningful regression is detected. New checks need a valid
case, violating case and tool-failure case; unavailable tools cannot report pass.

### Q4 — adopt into current root experiences

**Owner:** existing Home and Places owners first; Life/Entity/practical/social
owners take compatible adoption slices without changing their product scope.

- Use Q1/Q2 improvements inside the selected Home full scroll and Places mixed
  field/depth. Preserve worthwhile breadth, hierarchy and exact return.
- Remove duplicate local styling or compatibility branches only after their
  real consumers have migrated and tests prove the intended boundary.
- Validate original receiving, practical information and generated explanations
  together. Individually attractive cards can still compose into a poor page.
- Inventory shared changes' effects on Chat/Life without redesigning those
  roots. Their dedicated owners schedule intentional adoption.
- Do not fill thin supply with new decorative cards, invented social activity
  or empty generated commentary. Route supply gaps to the existing Content lane.

**Exit:** visible improvement in current mounted Home and Places experiences,
not just component screenshots, plus a disposition for affected sibling uses.
There is no requirement to migrate every root before landing a coherent unit.

### Q5 — close, measure and promote only what proved useful

**Owner:** coordinator and affected code owners.

- Compare the same native cases before/after; record what improved, regressed
  or remains uncertain. Separate design fidelity from functional correctness.
- Compare follow-on development using the patterns: remaining local overrides,
  repeated decisions, repair rounds, elapsed effort and founder intervention.
  Use `scripts/measure_verification.py` for verification measurements. Fewer
  files or tests does not by itself prove productivity improvement.
- Promote durable guidance to existing native and producer owners. Retire
  obsolete duplication after use has ended, not merely after it looks old.
- Close/archive this working plan or renew a bounded unresolved portion before
  expiry. Do not leave another permanent cross-lane queue behind.

**Exit:** current-app benefit, reusable behavior and remaining debts are explicit.
Do not claim measured efficiency before a comparable follow-on task exists.

## 7. Variation and acceptance portfolio

Select cases by distinct risk, not every possible combination. A small-device
large-text long-label comparison deserves a combined case; every font size
crossed with every source state does not automatically deserve a separate run.

| Dimension | Required representative evidence |
| --- | --- |
| Content origin | Direct fact, exact human original, authored editorial fixture; actual model output evaluated separately |
| Context | Little history, ordinary life, upcoming/practical situation; no-friends value remains complete |
| Length | Short, realistic ordinary, long-but-valid, and invalid/unsupported input |
| View | Whole root scroll, selected unit, exact detail and return |
| Environment | Supported narrow phone, ordinary phone, large text; platform parity reported separately |
| Media | Loaded, absent, loading/error and differing aspect ratios where supported |
| Time/state | Fresh, stale/changed, withdrawn/unavailable; repeated open without gratuitous movement |
| Interaction | Resting value, source opening, permitted action, no-change/failure and restored position |

### Product-grounded counterexamples

These are case intentions derived from the product canon and founder stories,
not new factual claims, fabricated friends or evidence of implemented support.

| Case | What it tests | A polished-looking failure |
| --- | --- | --- |
| Sorrento cliffs / Rome connection already supplied by the person | New supported understanding beyond a known observation; appropriate silence if no additive evidence | Renamed recap with an impressive diagram |
| Pasta curiosity becomes “help me cook tonight” | Changed benefit and wanted participation with the same topic | An elegant history essay instead of a usable method; or removing enjoyable choices |
| Returned to New York, looking toward the weekend | Present and future value alongside the trip; page-level marginal usefulness | A coherent but overwhelmingly retrospective travel magazine |
| Friend's authorized Paris photograph | Asymmetric effort, exact authorship, a worthwhile receiving experience | AI rewriting the friend's voice, fabricated social connection, or a required reply |
| A changed practical condition | Owner-backed timing, preparation and a complete no-change/unavailable answer | Attractive numbers with stale meaning or controls that imply an unperformed action |
| A substantial article/map/audio work | Useful preview plus worthwhile depth | Either an empty teaser or forced compression that destroys the deeper experience |

Compare complete pages, including a deletion test: does removing a unit actually
lose value, or improve clarity? Repeat with the same person's changed purpose
and a later open. Preservation of a stable item being read is compatible with
avoiding gratuitous repeated editorial resurfacing; neither authorizes silently
rewriting a retained original or saved expression.

Acceptance asks five independent questions:

1. **Value:** what does the person receive without additional homework?
2. **Meaning:** did useful detail, author, scope or uncertainty change in rendering?
3. **Visual quality:** does hierarchy, type, density and rhythm match the selected
   intent at native scale, including the entire page?
4. **Behavior:** can the person inspect, act where authorized and return without
   losing context? Are loading and unavailable states complete?
5. **Reuse:** did the repair improve a shared mechanism, or merely add a local
   exception? A justified root-specific composition is not itself a defect.

Do not invent numerical acceptance thresholds before measuring current cases.
Hard failures include clipping essential content, unreadable contrast, wrong
source/identity, hidden required qualification, unusable controls and unsupported
actions. A documented intentional native adaptation is not automatically a
failure because browser pixels differ.

Source quality, semantic correctness and authority are hard constraints; a high
aesthetic score cannot compensate for a false or invasive result. Conversely,
passing those constraints does not establish enjoyment. Use short voluntary
comprehension/task observations when claiming consumer usability, and report
founder/design review separately from newcomer evidence. Clicks, dwell time,
scroll depth and use frequency are not proxies for satisfaction or the goal of
Vesper. No habitual rating or reflection burden is added to gather evidence.

An AI visual reviewer should return a localized discrepancy, evidence and a
bounded proposed correction against selected intent. It is not authorized to
invent a new aesthetic to raise its own score. End iteration when required
defects are resolved or a genuine decision needs an owner; keep the best verified
result rather than assuming the last iteration is best.

## 8. Content economics and runtime stability

Content quality and polish also depend on when work occurs, not just how it
looks. Follow current lifecycle/cache/permission owners; do not add a second
generation scheduler here.

- Direct state and exact human material normally need no editorial model call.
- Generate or prepare bounded content through existing authorized paths, not
  on every render, scroll, revisit or density change.
- Separate semantic content versions from local responsive layout. A narrower
  phone should usually adapt the same admitted meaning, not regenerate it.
- Reuse retained work only under its existing viewer, source, policy, purpose,
  currentness and permission constraints. This plan grants no cross-user reuse.
- Render loading, image completion and changed state without unnecessary scroll
  jumps or surprise replacement of the thing being read. Respect owner-required
  withdrawal/currentness changes rather than freezing unsafe content for polish.
- Existing Source-contribution budgets include bounded sources, input, output,
  timeout and attempts. Do not raise them to hide a poor content agreement.
- Measure rejection, repair, fallback, accepted useful yield, latency and cost
  per delivered useful result where actual production is authorized. Token count
  alone does not measure benefit; generated volume is not a success metric.

## 9. Parallel execution and handoff discipline

**One coordinator, existing owners, bounded whole outcomes.** Research and
preparation can run alongside Orchestration. Execution starts only after the
current program owner schedules packages and resolves file ownership.

| Work | Parallel boundary |
| --- | --- |
| Pattern inventory and source/reference reconciliation | Read-only alongside any lane |
| Content examples and producer agreement | Alongside native work on disjoint files; shared wire semantics agreed first |
| Native shared patterns | One writer for shared typography/renderers; root owners adopt agreed revisions |
| Quality-tool extensions | Disjoint tooling files; no competing device/Metro/port ownership |
| Home and Places adoption | Separate owners only where files are disjoint; shared primitives/navigation have one writer |
| Life, Entity, practical and social adoption | Existing owner slots; no duplicate redesign or new policy grant |

Before dispatch, name the receiving checkout, reference revisions, owner files,
dependencies, allowed changes and finish evidence. Use isolated coordinated
worktrees for overlapping ownership, respecting separate child repositories.
Do not write into another lane's dirty working files.

Each assignment should own diagnosis, implementation, self-review, focused
tests, native evidence and a concise handback. Report at a substantial working
result, consequential blocker or final handoff—not after every small step.
Resolve ordinary technical problems within scope without repeated founder
approval. Escalate changes to product promise, authority, selected design or
cross-owner schema meaning.

Integrate at coherent contract/consumer boundaries, not every tiny correction.
Do not batch incompatible API changes until the end. Check the current lane
baseline at handoff; integration, publication and activation remain governed by
their existing authorities. This plan authorizes none of them by implication.

### Reassessment points

- **After Q0:** are the biggest defects content, typography, pattern anatomy,
  page composition, supply or runtime? Adjust effort to observed causes.
- **After Q1/Q2's first adopted patterns:** did shared work actually improve
  current consumers? Remove unnecessary abstraction before expanding it.
- **After Q4 Home/Places adoption:** does the whole product feel more coherent
  and useful, or have locally cleaner pieces made it flatter?
- **At Q5:** did follow-on work become easier? Continue only the improvements
  supported by evidence; route remaining supply and product decisions correctly.

## 10. Verification and evidence reporting

Implementation owners must read the current Task Intake and affected contracts
before selecting exact test commands. This plan does not replace those gates.

- Backend: focused producer/compiler/owner contract tests; deterministic fixture
  tests separately from any model-quality evaluation. Database tests require
  the documented disposable environment.
- Wire changes: lane-root `./scripts/sync-types.sh`, review both snapshots,
  generated app types and consumers; run `make api-coverage-check` when adopting,
  adding or retiring operations. Never hand-edit generated wire types.
- Mobile: focused component/adapter/convention tests and typecheck; inspect
  adjacent consumers after shared role or primitive changes.
- Native: registered scenario/reference checks, doctor, canonical captures and
  verdict workflow from mobile AGENTS/Task Intake. Read the verdict protocol
  before claiming visual acceptance. No newly invented pass based on screenshots
  merely existing or another agent saying they look good.
- Runtime: inspect release-like performance where relevant, not only development
  mode. Record device/OS/font state, fixture, selected source hash, revisions,
  feature posture and producer mode with each meaningful comparison.
- Delivery: preserve `make verify` as the coordinated pre-push gate. Unrun,
  failed, stale or unavailable checks are named explicitly, not treated as pass.

## 11. External research and limits

These sources support recommendations, not proof that Vesper has implemented
them or that a particular tool will improve its outcomes. Accessed September 15,
2026. Prefer existing mechanisms before adopting new dependencies.

| Source | Relevant finding | Application and limit |
| --- | --- | --- |
| [NN/G: Content Standards in Design Systems](https://www.nngroup.com/articles/content-design-systems/) — May 2024 | Content guidance belongs with reusable interface patterns and realistic examples, with both global and format-specific rules. | Supports Q1; does not prescribe Vesper's copy length or prove generative quality. |
| [NN/G: Lean Design-System Teams](https://www.nngroup.com/articles/lean-design-system-teams/) — May 2026 | Practitioner accounts emphasize integrated work, focused scope and contributions by consuming teams. | Supports bounded shared ownership, not a claim that more agents or fewer people automatically increase velocity. |
| [GOV.UK: Component lifecycle statuses](https://design-system.service.gov.uk/community/component-lifecycle-statuses/) | Trial versus stable communicates confidence and likely change. | Distinguish instrument explorations from established native patterns; do not copy an external promotion timetable. |
| [Atlassian design tools](https://atlassian.design/tools) | Design resources are accompanied by linting and development tooling for adoption. | Strengthen existing Vesper conventions rather than rely only on prose; their web tooling is not a drop-in native solution. |
| [Expo: Fonts](https://docs.expo.dev/develop/user-interface/fonts/) | Native font loading/embedding and naming need platform-aware handling. | Verify real font behavior; does not establish fonts as the cause of current mismatches. |
| [React Native Storybook: Testing](https://storybookjs.github.io/react-native/docs/intro/testing/) | Component testing and device-level visual testing are separate capabilities. | Reuse native capture infrastructure; a gallery alone does not establish app quality. |
| [Anthropic: Harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps) — March 2026 | Calibrated separate evaluation helped their frontend experiments; later iterations were not always preferable and complexity could grow. | Use bounded discrepancy repair against selected intent. Vendor engineering experience is not a controlled productivity result for this repo. |
| [Google: A2UI introduction](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) — December 2025 | Agent-driven interfaces can retain client-controlled rendering through approved vocabularies. | Directionally relevant; Vesper's existing semantic contracts are narrower. No protocol or server-component-tree adoption follows. |
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — January 2026 | Distinguishes outcomes from traces, trials from tasks, capability from regression, and code/model/human grading. | Supports separate evidence boundaries and repeated generative trials; vendor practice is not proof of human usefulness. Held-back cases here are a plan recommendation, not a measured Vesper result. |
| [Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/) — CHI 2019 research | Validated guidance covers contextual relevance, efficient correction/dismissal and cautious adaptation over time. | Older foundational evidence complements recent agent practice. Apply existing scoped controls; do not copy every guideline into mandatory feedback UI. |
| [Apple: Get started with Dynamic Type](https://developer.apple.com/videos/play/wwdc2024/10074/) — WWDC 2024 | Shows layout adaptation and prioritization of essential content as text grows, with accessibility auditing. | Supports native reflow instead of fixed screenshot geometry; SwiftUI examples require appropriate React Native implementation. |
| [W3C WAI: Complex images](https://www.w3.org/WAI/tutorials/images/complex/) | Meaningful alternatives describe represented values, scales, relationships and trends, not merely the presence of a chart. | Applies to equivalent understanding in Vesper instruments; HTML techniques do not establish native accessibility conformance. |

The [August polish note](visual-polish-evaluation-and-design-workflow-2026-08-13.md)
is historical supporting research. Its older root names, proposed tool pilots
and expired execution assumptions are not current instructions. This plan adds
the current content-to-native implementation boundary, not another visual-QA
platform. At promotion, update existing owners rather than declaring either
working note a permanent design canon.

## 12. September 15 handoff — historical scheduling

Give Orchestration this plan and ask it to **schedule Q0 plus compatible Q1/Q3
preparation against its current receiving baseline**, while keeping existing
Home/Places owners building their selected experiences. Q2 should use one shared
native writer after Q0 identifies measured defects. Q4 is consumer adoption in
those owners' work, not a late separate beautification lane.

Do not redispatch completed design-language consolidation, wait for all Stage 2
instruments, or block current feature construction on this plan. The first
implementation handback must say both **what became better in the current app**
and **what will no longer need to be solved repeatedly**.

## 13. September 21 native presentation lane execution plan

### 13.1 Outcome and observed baseline

**Build a reusable native presentation system and adopt it in current Home and
Places while Orchestration continues functional delivery.** The lane owns
legibility, hierarchy, adaptive anatomy, media/attribution, action presentation
and native finish. It is neither a fresh product redesign nor a collection of
independent card makeovers. Sections 4–10 remain the architecture and quality
agreement; the waves below schedule that work, not a new parallel framework.

The September 21 investigation inspected these distinct candidates:

| Candidate | Observed revision / evidence | Implication |
| --- | --- | --- |
| Active functional lane, `travel-workspace--functional-implementation-2026-09-20` | Workspace `27266586c4f4f7c202d7c6ac9ad1471045fc1446`; app `242d309f01f3dd47db30b0470a6671e6689d89f2`; backend `9d52e71b38217b52e9bd50b5b8613ea449dd6f57` with staged Source-worker implementation/tests at observation | Preserve its latest functional contracts and ongoing repairs. This is not an immutable clean three-repo tuple. |
| Receiving lane, `travel-workspace--receiving-completion-2026-09-10` | App `fe1de89ac8b56c156ec91dbdcc3a50d241f1da6f`, clean at observation | Contains richer `HomeRootV2Composition`, `CompositionSourceList`, responsive anatomy and design-guidance repairs absent from the functional candidate. |
| Isolated September 15 quality work | App `d030ab384` and `036d92462`; related receiving commits include `d5cd91904` and `b7d051b91` | Review equivalent changes before reuse; related commits are not instructions to cherry-pick both versions. |
| Canonical app main | `e2e792913b1902007ad237b05a3a58784a80332c` | Too old to stand in for either candidate. |

The functional and receiving app branches had 80 and 154 unique commits
respectively at inspection, with merge base `930ecee68`. Neither directory
name nor a later timestamp establishes that one supersedes the other. A full
merge, blanket file replacement or reimplementation of already useful work is
not the default starting action. These counts are orientation, not progress
metrics; recompute current status before execution.

The inspected native Home/Places full-scroll captures and flows demonstrate
receiving behavior, not a visual pass. Flow 89 scrolls to named units, asserts
content and captures the final viewport; it does not judge the complete page.
The functional candidate's `home-root` registration has empty `designRefs`
and doctrine-only judging; its seven older mock posture flows cannot certify
governed v2. No committed Home-root verdict directory was found, and the checked-in
Places-workspace verdict is dated July 29. This is an evidence gap for these
paths, not a claim that no visual work has happened anywhere in the repository.

### 13.2 Lane ownership and activation

Use one accountable native presentation owner alongside the existing
Orchestration owner. The program roadmap remains the queue. Before dispatch,
Orchestration acknowledges a coherent mobile handoff revision and the file
reservation below in its current roadmap. Do not silently impose ownership on
a running writer by updating this working plan.

| Area | Proposed writer | Boundary |
| --- | --- | --- |
| Backend supply, semantic admission, permissions, persistence, workers, currentness and practical assessment | Orchestration | No native geometry or design-token decisions in backend payloads. |
| Generated schemas, `types/rootProjectionV2.ts`, data/hooks and consequence/navigation controllers | Orchestration | Announce incompatible contract changes before consumer edits; schema generation keeps one owner. |
| Home/Places semantic rendering and root layout | Presentation lane after handoff | Reserve `HomeRootV2UnitRenderer.tsx`, `HomeRootV2Screen.tsx`, `RootCompositionRenderer.tsx`, `RootCompositionAnatomy.tsx`, `PlacesSemanticUnitCard.tsx` and its styles. Preserve supplied ordering, callbacks and exact return behavior. |
| Selected reused/new pattern modules, scoped typography/material/row/action fixes | Presentation lane | Inventory real consumers; no global retheme, blanket token replacement or forced migration of unrelated roots. |
| Existing original reader, Places feed wrappers, notices and navigation chrome | Explicit per-wave reservation | These files mix behavior and presentation. Assign one writer for the complete file; other owners supply requirements/tests rather than concurrent patches. |
| Functional Maestro rehearsals and backend-real fixtures | Orchestration | Existing passing journeys remain regressions; do not alter expected values merely to accommodate a visual change. |
| Selected visual scenarios, design bindings, comparison evidence and verdicts | Presentation lane | Extend existing registry and QA tools; preserve distinct real/mock evidence and do not build another runner. |
| Program/integration roadmap state | Orchestration | This plan is the supporting execution brief, not a second live status queue. |

The native lane may make ordinary in-scope implementation and craft decisions
without asking about each adjustment. Product meaning, audience/retention,
unsupported capabilities, new surface composition or unselected design changes
remain consequential decisions. A disputed component blocks its own adoption,
not all independent work in either lane.

Start an isolated coordinated workspace from the agreed functional candidate,
using the existing worktree tooling after checking its current base options.
Record each child's actual base, not just a workspace branch name. Bring over
only the required reviewed design inputs and selected donor changes, preserving
the histories of the three repositories and the functional lane's dirty work.
No worktree is created by this planning update.

### 13.3 Short startup: reconcile rather than restart (Q0)

Complete this inside the first implementation assignment, not as a separate
open-ended audit project:

1. Compare the relevant functional and receiving implementations and their
   tests. Give each donor change a disposition: **reuse**, **adapt**, **already
   equivalent**, or **do not adopt**, with the dependency/reason. Start with
   `HomeRootV2Composition`, `CompositionSourceList`, responsive comparison
   anatomy, source-qualification safeguards and typography guidance.
2. Preserve functional improvements made since the branches diverged: exact
   destinations, grouped reading navigation, revoked/stale handling, recipient
   checks and restoration. A richer donor renderer does not prove compatibility
   with the selected payload, owner semantics or latest fixes.
3. Select the applicable Home/Places full-scroll references and shared Stage 1
   components from the existing reviewed design snapshot and later accepted
   amendments. Map exact screens/variants and hashes into the existing surface
   registry. Downloads exports are comparison inputs, not automatic authority.
4. Reconcile only relevant contradictory instructions. Examples: Home's sans
   section-heading rule versus the archive-mono `SectionHeader` consumer; the
   font module's existing limited italic role versus an older rule denying it;
   and explanatory comparisons versus obsolete blanket comparison prohibitions.
   Reuse the prior accepted corrections where compatible.
5. Capture a reproducible baseline with actual selected routes, flags, content
   and font state. Keep a controlled fixture baseline for visual comparisons
   and a separate owner-backed rehearsal for behavior. Record a small prioritized
   defect list in the existing surface findings/verdict workflow.

**Startup exit:** agreed file ownership, exact candidate/design bindings,
donor dispositions and an executable capture case. Missing runtime access is
reported narrowly; source/test work may continue, but visual completion cannot
be declared. Do not wait for every design project or every instrument to settle.

### 13.4 Target implementation shape

Preserve the existing chain: typed owner result → native presentation adapter
→ reusable anatomy → Home/Places composition → exact destination and return.
Do not add a server-authored component tree or a new persistence family.

The missing middle layer should own repeated decisions once:

- Identity and title roles; required versus optional supporting text.
- Human attribution versus Vesper authorship versus machine facts.
- Source/currentness/qualification placement without repeating the same prose.
- Navigation, inspection and consequential-action appearance, using existing
  typed effects and owner handlers rather than action array position alone.
- Medium-specific bodies: reading, comparison, sequence/evidence, spatial
  relationships, original material and supported practical state.
- Variants actually required by consumers: ordinary, lead, compact or depth;
  host-width/font-scale reflow; missing-media and unavailable states.

Keep root-specific composition outside those bodies. Home can emphasize a
reading differently from Places without duplicating its comparison cells or
source-access logic. Keep distinct author/original, command and navigation
semantics; a universal `Card` with dozens of booleans is not the objective.

Use existing `CardSurface`, text roles, row registers, `ActionGroup`, `Door`,
state patterns and image primitives where their semantics fit. First inspect
the donor implementations above. Extract a new shared component only when its
actual consumers justify it; splitting a large file alone does not prove a
better abstraction. The reviewed component catalog and owner contracts should
explain which pattern to choose without another catalogue of one-off cards.

### 13.5 Three delivery waves

Each wave includes Q1/Q2 work, immediate Q4 adoption, Q3 evidence and Q5 review.
The ordering is pragmatic sequencing, not a narrow product-scope decision.

| Wave | Complete outcome | Main implementation work | Exit evidence |
| --- | --- | --- | --- |
| **1 — Reading/comparison and page hierarchy** | Existing supplied Home and Places material is legible and meaningfully structured through shared patterns | Reconcile/adapt donor anatomy; correct heading/register selection; place the useful medium appropriately rather than always appending it below paragraphs; preserve source access and meaningful limits; consolidate repeated followups; repair the observed status-bar/scroll interaction if reproduced | Same-content native before/after in both roots, long-label/large-text comparison, exact depth and return, unchanged supported actions and functional regressions |
| **2 — Human originals, practical state and compact continuity** | Mixed pages distinguish people, operational help and doors without local style inventions | Apply attributed-original pattern and supported media fallback; avoid rendering human prose as machine metadata; distinguish neutral reopening from genuine urgency; consolidate practical notes and command/navigation roles; compose saved/continuity rows with appropriate existing registers | Mixed Home/Places scrolls with original, reading, saved object and state change; withdrawal/expiry and unknown/failure behavior; accessible controls; no forced reply, save or contribution |
| **3 — Whole-page coherence and durable quality loop** | Adopted patterns remain coherent as content, device and circumstance vary | Tune root rhythm and emphasis; verify loaded/absent media, cold/populated and practical situations; repair scroll/return, keyboard/sheet and perceived-performance defects found; remove migrated duplicates; bind reviewed native examples and correct stale visual assertions | Registered page/selected-depth visual verdicts, sibling regression checks, relevant owner-backed journeys and a second ordinary content example composed without another bespoke card |

Wave 1 is deliberately more than a shared component specimen: it must improve
the actual Home and Places consumers. Wave 2 must preserve that first-wave
quality when unlike material appears beside it. Wave 3 does not postpone visual
testing; it expands already reviewed work to page-level variation and closes
the selected package. Life/Chat/Entity are inspected as shared-component
consumers but are not redesigned or blanket-migrated by these waves.

At each wave boundary ask: did the current app improve; did an ordinary second
consumer benefit; did we preserve valuable detail; and did shared work reduce
repeated local decisions? If not, revise the abstraction before extending it.
No unsupported percentage-complete or calendar guarantee follows from this plan.

### 13.6 Functional and visual acceptance are separate gates

Retain the functional lane's tests and add visual review at the layer where
appearance is decided. Do not rewrite a passing flow to hide missing material.
Some old assertions may encode an unreviewed presentation choice—such as
requiring the prose body to display “One supporting claim.” Replace such an
assertion only after agreeing the user-facing treatment, while retaining tests
that the supporting evidence and essential qualification remain accessible.

| Case | What must remain correct | What native inspection must establish |
| --- | --- | --- |
| Public reading, little/no history | Same supported claims, exact source/entity and depth | Substantive first return, clear title/body/source hierarchy, no obligatory input |
| Comparison/sequence with long valid content | All essential axes, steps and limits remain usable | Meaningful structure, width-aware reflow and readable large text, not compressed columns or indiscriminate truncation |
| Authorized human original, with and without media | Original wording/custody, sender, audience, revocation | Recognizable authorship, graceful fallback, no extra AI framing or reciprocation requirement |
| Practical result: supported/unknown/stale/failed | Owner state, time qualification and action eligibility | Useful uncertainty, appropriate urgency, readable facts, no status dump or misleading button |
| Mixed root and exact detail/return | Supplied order/dominance, identity and restored context | Full-scroll rhythm, containment, top/bottom chrome, stable reading and usable back behavior |
| Representative shared-component sibling | Existing Chat/Life/Entity behavior | No incidental typography, touch-target, sheet or media regression from adopted primitives |

Choose a small risk-based portfolio rather than the Cartesian product of every
state. Include ordinary device/default text, narrow device/long labels and
large text; exercise reduced motion and screen-reader interaction for affected
patterns. Assess release-like scrolling/image behavior when claiming performance
improvement. State exactly which platforms and cases were not exercised.

Use existing `qa:polish:scenarios`, `qa:design:check`, the surface doctor,
`qa:surface`, comparisons and the structured verdict path. Correct the selected
v2 bindings before relying on older mock posture flows. Capture the first
viewport, meaningful scroll positions/page close and selected depth, not one
terminal screenshot called a whole-page judgment. A valid reference hash or
an existing PNG is not a visual pass.

For design-sensitive completion, obtain a distinct reviewer pass against the
actual reference and capture. Findings should name the location, defect and
desired correction; an agent's positive opinion is not evidence by itself.
Preserve artifact provenance, revisions, OS/device/text scale, flags and data
mode. Missing screenshots/reference/assistive checks remain unverified rather
than being replaced by Jest. Required broad gates still apply before publishing.

**Wave completion requires:** passing scoped behavior checks; no unresolved
blocker/major visual defect in the selected cases; reviewed design alignment or
an explicit approved adaptation; at least one current consumer visibly improved;
and a disposition for affected sibling consumers. User preference and production
supply quality remain separate from this native acceptance.

### 13.7 Runtime, integration and economical coordination

- A worktree isolates files, not simulator/API/Metro state. Check the lane runtime
  manifest and `scripts/dev.sh --print-runtime`; reserve a device/build/session
  or use agreed time windows. Never restart Orchestration's services to capture
  the presentation lane. Identify the actual installed bundle and API mode.
- Use provider-free deterministic fixtures for repeated visual iteration; do
  not regenerate content to change spacing or font scale. Run the required
  owner-backed native rehearsals at meaningful functional/consumer boundaries,
  with explicit disposable data/service ownership and cleanup.
- Integrate compatible presentation work at substantial pattern/adoption
  boundaries, not after every card or receipt. Exchange compact revision and
  interface summaries. Incompatible generated schema changes need early
  coordination; ordinary backend work need not wait for a visual review.
- Keep the functional branch's fixes when adapting donor work. Do not merge
  154 historical commits to obtain one useful composition component. Reconcile
  dependency-bearing changes explicitly and preserve separate repo histories.
- Maintain one shared-component writer. If authorized later, bounded read-only
  review or disjoint fixture work may run in parallel; do not create a hierarchy
  of coordinators. This planning turn dispatches no agents or tasks.
- Report at the first substantial working result, consequential blocker and
  verified handback. Handback includes revisions, changed owners, before/after
  evidence, behavior tests and unverified boundaries—not a new standalone
  receipt for every minor adjustment.
- End or redirect a repair cycle when the selected quality bar is met or a real
  product decision is needed. Retain the best verified implementation, not
  necessarily the latest visual experiment. New skills/dependencies are optional;
  building a skill pack or replacing QA infrastructure is not a prerequisite.

### 13.8 Ready-to-schedule assignment

**Assignment:** reconcile the selected receiving/native work with Orchestration's
current functional candidate, then execute Wave 1 through visible Home/Places
adoption, regression tests and native review. Preserve the approved designs,
exact ownership/permissions and supplied meaning. Resolve routine defects within
scope; escalate incompatible semantics or an unselected design change. Deliver
one coherent result and the remaining bounded queue for Waves 2 and 3.

**Before sending the assignment:** record the accepted baseline and donor
dispositions, reserve shared files/runtime with Orchestration, and add a concise
link to this section in its active program roadmap. That dispatch is the
operational start. This document update does not create a goal/session, transfer
live file ownership, change the active lane's priorities, resume the paused
Integration lane, or authorize publication.
