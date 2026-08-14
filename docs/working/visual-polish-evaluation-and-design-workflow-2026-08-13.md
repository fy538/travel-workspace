---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-08-13
expires: 2026-09-12
why_new: Focused synthesis of the August 13 discussion about why functional evals can pass while the mobile product still feels visually unfinished, how current visual-evaluation practices work, the role of Maestro and test environments, Claude Design versus Figma, useful Codex capabilities, and the smallest high-ROI operating model for improving polish without overengineering.
promotes_to: a frontend visual-certification contract and a small canonical visual-checkpoint registry if the proposed pilot proves useful
supersedes: []
related:
  - product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md
  - ../../travel-app/docs/Frontend Engineering Loop.md
  - ../../travel-app/docs/Design Workflow.md
  - ../../travel-app/docs/research/Product-Quality AI Design QA Loop.md
  - ../../travel-app/docs/research/Frontend Engineering Loop with AI Agents and Screenshot QA.md
---

# Visual polish, evaluation, and design workflow

> **Working synthesis, not product canon or a claim that every proposed gate is
> already implemented.** This records the conclusions of the August 13 visual
> polish discussion. Current commands, device lanes, design artifacts, and
> implementation status must be re-verified before action. Durable rules should
> be promoted into the appropriate frontend contract or runbook rather than
> leaving this note as a second source of truth.

## 1. Why this discussion happened

The triggering problem was a recurring mismatch:

> An engineering or coding agent says that the evals passed, but the screen on
> the device still looks plainly unfinished: spacing rhythm is wrong, typography
> feels off, components do not belong together, the first viewport has weak
> composition, and the app lacks a coherent product feel.

That experience is not evidence that all evaluation is useless. It means the
word **eval** has been collapsing several different claims into one reassuring
green result.

The discussion asked:

1. What do the current evals actually test: product logic, visual quality, or
   both?
2. Can screenshot automation detect the kinds of polish problems a founder or
   design lead notices immediately?
3. What is state of the art in 2026, including AI-assisted visual review?
4. What are the common failure modes, especially evaluator leniency?
5. What should Maestro inspect, capture, and prove?
6. Which environments should execute which parts of the loop?
7. Which Codex plugins, MCP servers, or skills are useful?
8. Should the design workflow stay in Claude Design or move to Figma?
9. What is the smallest implementation with the highest return?

## 2. Executive conclusion

The product does not need one omniscient visual test. It needs a short chain of
independent instruments, each making a narrow claim:

```text
product intent and accepted visual reference
        ↓
deterministic scenario and state
        ↓
functional and state assertions
        ↓
native journey execution
        ↓
canonical screenshot capture
        ↓
deterministic visual checks
        ↓
independent AI visual critique
        ↓
small, calibrated human acceptance step
```

The highest-return operating model is:

- define a small number of product loops and golden journeys across Trips,
  Vesper, and Places;
- select only 10–15 canonical visual checkpoints within those journeys;
- keep Claude Design as the high-velocity exploration and substrate-diagnostic
  environment;
- store an immutable accepted reference, contract, fixture, and implementation
  owner for each checkpoint;
- use Maestro to execute the actual React Native journey and capture evidence;
- run deterministic checks before probabilistic judgment;
- require an independent visual reviewer to return localized defects rather
  than a generous binary pass;
- calibrate that reviewer against founder-labeled examples; and
- keep Figma as a bounded pilot for accepted visual contracts and production
  component mappings, not as a migration of the entire design archive.

This is not primarily a call for more tools. It is a call to make “passed” mean
one precise thing at each layer.

## 3. Logic quality and visual quality are different targets

### 3.1 What logic-oriented evals can prove

Logic and journey evals can prove valuable things:

- the intended route opened;
- the user can complete an action;
- a response has the expected shape or meaning;
- an accepted proposal changes canonical state;
- retries do not duplicate a mutation;
- Trips, Vesper, and Places reconcile after a change;
- the correct persona, fixture, audience, and privacy state were used;
- empty, loading, error, and stale states remain reachable; and
- the product does not crash, hang, or silently fail.

These checks are necessary. A beautiful screenshot of incorrect state is not a
successful product.

### 3.2 What they generally do not prove

They do not, by default, prove:

- good spacing rhythm;
- a convincing first viewport;
- correct font loading and optical type hierarchy;
- harmonious component proportions;
- appropriate information density;
- on-brand color, image, icon, or material treatment;
- a clear visual anchor and scan path;
- premium or crafted feel;
- consistency across screens; or
- that individually acceptable components compose into a coherent whole.

A semantic assertion such as `Trips tab is visible` says nothing about whether
the tab bar, typography, hero, cards, and surrounding space feel like the same
product.

### 3.3 Screenshot existence is not screenshot judgment

There are three separate visual capabilities:

1. **Capture:** a screenshot exists for the intended state.
2. **Change detection:** the current image differs from an accepted image in a
   controlled way.
3. **Design critique:** the current image has good hierarchy, rhythm, fit, and
   product character.

Maestro taking a screenshot accomplishes the first. Pixel or perceptual diffing
can accomplish parts of the second. A calibrated vision model plus human taste
is needed for the third.

## 4. What “visual polish” should mean for Vesper

Visual polish is not ornamental pixel adjustment after the real work. It is the
perceived coherence of the product’s decisions.

A product-quality screen should meet all of the following:

### 4.1 Hierarchy and first-viewport composition

- The user understands what the screen is and why it matters within seconds.
- The eye lands on the correct anchor first.
- Primary and secondary actions do not compete.
- The viewport suggests continuation without creating a false floor.
- The screen has an intentional beginning, middle, and transition to what comes
  next.

### 4.2 Spacing rhythm and grouping

- Related elements are bound by proximity.
- Sections are separated using a stable rhythm rather than arbitrary local
  gaps.
- Screen gutters and component padding belong to one scale.
- Empty space feels deliberate and useful, not like missing content.

### 4.3 Typography and copy presentation

- The intended fonts actually loaded on the native platform.
- Text roles are semantic and limited rather than a collection of raw sizes.
- Headline, body, label, metadata, and action roles remain distinguishable.
- Line length, wrapping, truncation, and paragraph density are comfortable.
- Dynamic Type and longer content do not destroy hierarchy.

### 4.4 Component and material fit

- Cards, rows, sheets, controls, icons, and images feel like members of the same
  family.
- Components are chosen because they fit the content and interaction, not
  because cardification is the default.
- Shape, border, radius, elevation, image treatment, and state styling use a
  coherent system.
- Controls look actionable and use native mobile ergonomics.

### 4.5 Product-language and emotional fit

- The screen feels recognizably Vesper rather than like a generic AI dashboard,
  component gallery, or slide deck.
- It expresses the desired attributes explicitly: calm, intelligent, warm,
  situated, confident, and editorial where appropriate.
- Trips, Vesper, and Places retain distinct jobs without feeling like three
  separate applications.

### 4.6 Native and adaptive integrity

- Safe areas, keyboard behavior, scrolling, touch targets, and home indicators
  are correct.
- Layout holds across representative widths, long content, and larger text.
- iOS and Android are reviewed where system typography or platform behavior can
  differ.
- Web prototype fidelity is never treated as automatic React Native fidelity.

## 5. The appropriate acceptance ladder

One global “eval passed” result should be replaced by explicit acceptance
states.

| State | Claim | Required evidence |
| --- | --- | --- |
| **Captured** | The intended screen and state rendered. | Correct route/persona/state plus screenshot receipt. |
| **Functionally correct** | The journey and data state are right. | Assertions and, where material, backend postconditions. |
| **Visually intact** | No obvious rendering, clipping, safe-area, font, or accessibility failure. | Deterministic checks plus screenshot inspection. |
| **Product-quality** | Hierarchy, rhythm, component fit, and product feel meet the release bar. | Independent visual critique with no blocker or major defects. |
| **Matches accepted intent** | The native implementation preserves the approved reference’s priorities. | Reference comparison plus documented acceptable adaptations. |
| **Human accepted** | A responsible human is willing to ship the experience. | Fast first-impression and side-by-side acceptance record. |

Each report should say which state was reached. “Captured” must never be
rendered as “product-quality.”

## 6. What current 2026 practice can and cannot automate

### 6.1 Deterministic checks

These are high-confidence and should run before AI judgment:

- expected screenshots exist and are fresh;
- the intended screen, persona, state, commit, fixture, and device are bound to
  the receipt;
- no crash, blank screen, loading corruption, or unexpected debug chrome;
- expected text or semantic elements are present;
- font-family and token inventories are valid where code can establish them;
- text or controls do not cross known bounds;
- safe-area, contrast, touch-target, and selected accessibility invariants hold;
- image dimensions and masks are stable enough for comparison; and
- perceptual or pixel diffs stay within an appropriate reviewed threshold.

Pixel comparison is useful for stable components and stable content. It should
not be the sole screen-quality criterion for a content-rich, adaptive native
application.

### 6.2 Perceptual visual regression

Modern visual testing can ignore insignificant rendering noise and identify
meaningful changes in layout or regions. It is most useful when:

- the fixture, clock, image assets, device, and font environment are fixed;
- volatile regions are masked deliberately rather than opportunistically;
- expected changes require review rather than automatically rewriting the
  baseline; and
- the baseline represents an accepted state, not merely the first image ever
  captured.

Its primary question is **what changed?**, not **is this good?**

### 6.3 AI visual critique

A multimodal model can identify and explain problems such as:

- weak hierarchy;
- awkward spacing and grouping;
- inconsistent component language;
- excessive cardification;
- dense or ragged typography;
- unclear CTA prominence;
- image/copy imbalance;
- generic or template-like appearance; and
- drift from an accepted reference.

This is possible in 2026, but it remains probabilistic. Vision models are most
useful as strict, evidence-producing reviewers, not as an unquestioned release
oracle.

### 6.4 Design-aware agents

The important 2026 shift is that an agent no longer has to judge from a
screenshot alone. Through design-system synchronization, MCP, component maps,
and repository context, it can receive:

- the accepted reference frame;
- structured layers and layout properties;
- component and variant identity;
- tokens and variables;
- the corresponding production component;
- the intended user job and visual focal point;
- the native screenshot; and
- the code diff that produced it.

This makes feedback more actionable and reduces the amount of inference the
reviewer must perform. It still does not remove the need for calibration.

## 7. Why coding agents are often too lenient

The leniency problem has several causes.

### 7.1 Correlated implementation and judgment

An agent that wrote the screen understands what it meant to build. It can
mentally complete missing hierarchy or excuse awkward rendering because the
implementation intent is familiar. The end user has no such context.

**Countermeasure:** implementation may self-check, but a fresh-context reviewer
must make the product-quality judgment.

### 7.2 Binary prompts invite generic reassurance

“Does this look good?” encourages a holistic and polite answer.

**Countermeasure:** require defects by category, severity, location, evidence,
and likely owning layer. Permit `uncertain`; prohibit unsupported praise.

### 7.3 Release context biases the judge

Telling a reviewer that the team worked hard, fixed everything, or needs the
gate to pass can bias it toward rationalizing the result.

**Countermeasure:** provide the artifact and contract without emotional or
release-pressure framing.

### 7.4 The reference itself can anchor judgment

A reviewer comparing against a mockup may say “close enough” even when both the
mockup and implementation feel weak in native context.

**Countermeasure:** use two passes:

1. critique the screenshot on its own product-quality merits;
2. compare it against the accepted design intent.

### 7.5 No learned definition of taste

Words such as “premium,” “polished,” and “coherent” are too underspecified by
themselves.

**Countermeasure:** create a small founder-labeled calibration set containing
screens that are `ship`, `ship with minor issues`, `block`, and `clearly
unacceptable`, with annotations explaining why.

## 8. Common failure modes and efficient countermeasures

| Failure mode | False conclusion | Efficient countermeasure |
| --- | --- | --- |
| Screenshot exists | “Visual QA passed.” | Report capture separately from judgment. |
| Correct text is visible | “The screen is correct.” | Verify scenario identity and durable postconditions. |
| Mock lane is green | “The real system works.” | Run the same small outcome contract through local real stack and an isolated cloud canary. |
| Retry passes | “The feature is reliable.” | Preserve first-attempt failure and report flaky separately. |
| Optional Maestro action skips | “The journey passed.” | Avoid optional commands on load-bearing behavior. |
| Coordinate taps work | “The UI is stable.” | Prefer semantic IDs, visible text, and relational selectors. |
| Pixel diff is small | “The design is good.” | Add hierarchy and product-quality critique. |
| Pixel diff is large | “The design regressed.” | Separate legitimate adaptive/content changes from invariant violations. |
| One happy state looks good | “The component is polished.” | Capture long, thin, empty, loading, error, stale, and large-text states selectively. |
| Agent compares to its own work | “Independent QA passed.” | Use a separate reviewer context/model. |
| AI returns a high score | “Human taste is encoded.” | Measure false negatives against a human gold set. |
| Baseline was updated | “The change was approved.” | Require explicit review and provenance for baseline replacement. |
| Claude Design HTML looks good | “React Native will match.” | Capture the actual native implementation; translate intent, not web components literally. |
| Every design page is canon | “We have comprehensive documentation.” | Maintain a narrow accepted checkpoint registry and retain the rest as exploration/history. |
| Figma is adopted | “Design-code drift is solved.” | Connect accepted components/tokens to code and keep the registry current. |
| Shared cloud DB is convenient | “E2E results are reproducible.” | Use isolated state, deterministic seeds, namespaces, and cleanup/TTL. |
| Visual score improves | “Core loop improved.” | Keep product outcome and return-value measures beside visual measures. |

## 9. What the evaluator should inspect

The answer is not only screenshots and not only code.

### 9.1 Before execution

Read:

- the surface or journey contract;
- product job and expected first-value moment;
- accepted reference and adaptation rules;
- fixture/persona/state definition;
- relevant tokens and components; and
- the code diff or implementation ownership map.

### 9.2 During execution

Observe:

- navigation and transition behavior;
- loading and settling;
- taps, scrolling, keyboard, sheets, and back behavior;
- whether the intended state is actually reached;
- response content and action receipts; and
- cross-tab reconciliation where the journey spans roots.

### 9.3 After execution

Inspect:

- canonical screenshots;
- semantic assertions;
- logs and failure stage;
- backend postconditions or revision receipts;
- screenshot/reference comparison;
- screenshot-only product critique; and
- whether the defect is owned by content, a token, a shared component, screen
  composition, native rendering, or underlying substrate.

Reading responses matters because weak AI content can make a correct layout
look wrong. Reading code matters because the same visual symptom may originate
in one shared primitive. Screenshots matter because neither response schemas nor
code structure reveal the final native composition.

## 10. The role of Maestro

Maestro is the repeatable experimental apparatus, not the taste model.

For a data-science analogy:

- fixture and seed = controlled input data;
- flow = experimental protocol;
- simulator/device = execution apparatus;
- assertions = measured variables;
- screenshot and logs = raw observations;
- backend verifier = outcome validation;
- visual reviewer = annotator/judge;
- run receipt = reproducibility record.

### 10.1 Maestro should own

- launching/resetting the app;
- selecting the intended deterministic persona and state;
- following the golden journey through the actual native UI;
- checking critical semantic elements;
- capturing screenshots at named checkpoints;
- exposing timing, retries, and failure stage;
- recording video/logs where useful; and
- handing evidence to deterministic and AI reviewers.

### 10.2 Maestro should not be asked to own by itself

- whether spacing feels premium;
- whether the font choice has the right character;
- whether the whole composition feels coherent;
- whether an AI response is insightful rather than merely present;
- whether a change improves product stickiness; or
- whether a web design transferred faithfully into native interaction.

Maestro’s experimental AI assertion capability can be supplementary, but the
qualitative layer should remain explicit, freshness-bound, and calibrated.

## 11. Environment strategy

No single environment should carry every claim.

### 11.1 Fast deterministic lane

Use for every relevant change:

- production application code;
- native simulator rendering;
- deterministic fixture/persona world;
- fixed clock and stable images where practical;
- stubbed nondeterministic external services;
- curated or recorded AI outputs;
- mock or in-memory data only where the test claim is visual/interaction shape;
- Maestro capture at canonical checkpoints.

This is the primary visual-polish loop because it is fast, repeatable, and
reviewable.

### 11.2 Local real-stack lane

Use for the small number of golden journeys whose value depends on real state:

- real backend application code;
- disposable local Postgres state;
- isolated Qdrant namespace;
- deterministic seed and actor identities;
- governed commands and backend postcondition checks;
- the same visual checkpoints where possible.

This proves that the attractive screen corresponds to correct durable behavior.

### 11.3 Isolated cloud-preview lane

Use for production-like certification:

- exact candidate commit;
- ephemeral backend deployment;
- isolated database branch or equivalent disposable state;
- isolated vector namespace;
- test auth identities;
- managed simulator/device execution;
- complete, hash-bound evidence receipt.

This should cover a deliberately small set of vital journeys rather than every
screen.

### 11.4 Shared dogfood and production

Use for emergent behavior, real provider variance, long-lived state, and human
taste. These environments are valuable but unsuitable as the primary
deterministic visual baseline because content, state, time, and external systems
change continuously.

## 12. Claude Design versus Figma

The tools now overlap substantially. Claude Design supports conversational
generation, direct canvas editing, design-system import, interactive
prototyping, organizational sharing, standalone HTML export, Claude Code
handoff, and an MCP interface. Figma now supports AI/MCP access to structured
frames, components, variables, Auto Layout, and code mappings.

The useful distinction is their center of gravity.

### 12.1 Claude Design is strongest as the product-design laboratory

Advantages for Vesper:

- very high founder and PM iteration bandwidth;
- broad product concepts can become working prototypes quickly;
- realistic content, edge states, and interaction can coexist in one artifact;
- codebases, page specs, screenshots, and design-system context can inform the
  generation;
- competing visual paradigms can be explored without manually constructing
  every frame; and
- the rendered screen can act as a diagnostic for content or substrate shape,
  which is the core method documented in the existing Design Workflow.

Costs and risks:

- current output is web-oriented and still requires visual translation into
  React Native;
- large HTML/JSX projects can accumulate authority ambiguity;
- prompts, chats, exports, pages, modules, and accepted decisions can drift;
- simultaneous multi-person editing remains less mature than Figma’s;
- comment persistence and large-project reliability have known limitations;
- generative iterations can subtly alter previously accepted details; and
- the same model family can become producer, interpreter, and overly generous
  judge.

The current Vesper Claude Design estate demonstrates both sides: it enabled
substantial visual exploration, but reached 66 top-level HTML pages and 215 JSX
modules with incomplete governance and stale/red audits. The correct diagnosis
from the consolidation work is: **the design file is not inherently
disorganized; it is insufficiently audited and its authority boundaries are
too implicit.**

### 12.2 Figma is strongest as the accepted visual contract

Advantages:

- mature structured components, variants, variables, modes, libraries, and
  Auto Layout;
- exact inspection of layout, typography, assets, tokens, and interactions;
- clearer Ready for Dev status, annotations, version history, review, and
  branching;
- stronger real-time human collaboration;
- Code Connect can map Figma components and properties to actual React Native
  components;
- Figma MCP can give coding agents structured design context and write native
  Figma content; and
- a stable frame is a useful external visual reference for screenshot review.

Costs and risks:

- more manual design-system and file maintenance;
- slower whole-product exploration for a founder-led, AI-native team;
- designs can become a polished museum detached from real content and runtime
  state;
- introducing Figma now could create a third competing truth alongside Claude
  Design and code;
- prototypes may be less faithful to complex AI and backend behavior; and
- advanced Code Connect and governance features have plan/seat implications.

### 12.3 Recommended division of responsibility

| Artifact | Recommended authority |
| --- | --- |
| Divergent product and visual exploration | Claude Design |
| Behavior-rich prototype and substrate diagnosis | Claude Design |
| Accepted visual checkpoint | Repo manifest plus immutable reference capture |
| Shared tokens and production primitives | React Native repository |
| Optional structured design contract for stable surfaces | Small Figma pilot |
| Runtime behavior and durable state | Production code/backend |
| Journey execution and capture | Maestro |
| Visual judgment | Independent calibrated reviewer plus human acceptance |

Do not migrate the historical Claude Design project. If Figma is piloted, start
with Trips Home, Vesper Home, Places Home, and roughly 10–15 shared primitives.
Continue only if it measurably reduces ambiguity and implementation defects.

## 13. Useful Codex capabilities

The useful Codex stack is similarly layered.

### 13.1 Custom `travel-visual-review` skill

This is likely the highest-return Codex extension because it can encode the
team’s rubric, accepted-screen examples, output schema, severity rules, and
review sequence. It should:

- locate the relevant checkpoint contract and reference;
- verify screenshot provenance and freshness;
- perform screenshot-only critique;
- perform screenshot/reference comparison;
- produce localized defects and implementation ownership;
- refuse to call capture-only evidence a visual pass; and
- track calibration results over time.

This should be a small workflow skill, not an autonomous visual-design platform.

### 13.2 Computer Use

Computer Use is useful for operating the simulator and visually inspecting the
actual app when a CLI or Maestro flow cannot expose the relevant behavior. It is
particularly valuable for:

- transitions and gesture feel;
- keyboard/sheet interactions;
- native font and safe-area issues;
- screenshots that need human-like navigation; and
- exploratory review after deterministic gates identify a suspicious surface.

It should not replace repeatable Maestro flows for canonical journeys.

### 13.3 Figma plugin/MCP

The available Figma plugin becomes valuable if Figma is selected for the
bounded canon pilot. It can provide structured nodes, variables, components,
Auto Layout, screenshots, and Code Connect context directly to the coding or
review agent. It should not be installed merely because it is available; the
design-authority decision comes first.

### 13.4 Browser control

Browser control is useful for inspecting Claude Design exports, web references,
internal evidence viewers, and browser-rendered artifacts. It is not a substitute
for the native simulator where typography, navigation, and platform behavior
matter.

### 13.5 Expo and Xcode-oriented integrations

Expo/EAS tooling can help build artifacts, run managed Maestro workflows, and
collect recordings and screenshots. Xcode-oriented MCP or tooling may later
improve native build, simulator, accessibility-tree, and test diagnostics. These
are second-stage conveniences; they should follow a stable checkpoint and
receipt model rather than define it.

## 14. The visual-review output contract

The evaluator should not lead with praise and should not reduce its output to a
single score.

Recommended report:

```yaml
checkpoint_id: places-home-returning
run_id: 20260813T...
verdict: pass | mixed | fail | uncertain
confidence: high | medium | low
capture_valid: true
functional_state_valid: true
reference_fresh: true
ship_blocking: true
first_impression: "..."
top_defects:
  - severity: blocker | major | minor | nit
    category: hierarchy | spacing | typography | component_fit | color_material | content_fit | native_integrity | design_language
    region: "top hero / primary action"
    observation: "..."
    evidence: "..."
    reference_delta: "..."
    why_it_matters: "..."
    likely_owner: token | shared_component | screen_composition | content | fixture | native_rendering | substrate
    recommended_fix: "..."
would_design_lead_block: true
human_review_required: true
```

Suggested hard rule for a product-quality `pass`:

- zero blockers;
- zero majors;
- no missing or invalid evidence;
- no unresolved uncertainty on the primary job or first viewport; and
- only a small number of minors that do not reduce product coherence.

## 15. Calibration: the efficient answer to evaluator leniency

Build a founder-labeled set of approximately 20–30 screenshots spanning:

- ship;
- ship with minor issues;
- block;
- clearly unacceptable; and
- ambiguous/needs discussion.

Annotations should identify concrete causes such as:

- wrong or unloaded font;
- weak type hierarchy;
- inconsistent screen gutters;
- poor section rhythm;
- generic cards or controls;
- awkward image crop;
- overly dense copy;
- unclear primary action;
- components that are individually fine but compositionally incoherent;
- platform integrity problem; and
- acceptable intentional adaptation from the design reference.

Measure:

- AI/human agreement by category;
- false negatives, especially AI-pass/human-block;
- false positives;
- repeated-review stability;
- reference-order bias;
- severity agreement;
- model/prompt version drift; and
- cost and latency per capture.

Initially, AI review should be advisory. Promote only narrow, demonstrated
criteria into blocking automation.

## 16. Highest-ROI implementation order

### P0 — Define the product journeys being protected

Select 3–5 golden journeys spanning the three roots:

1. onboarding → relevant place → save;
2. saved place → create or enrich a trip;
3. trip uncertainty → ask Vesper → accept/correct action;
4. Vesper recommendation → inspect place → commit; and
5. return trigger → useful update → next action.

Document first value, commitment, cross-tab handoff, durable mutation, and
return trigger. Visual polish without a clear product job can optimize a screen
that should not exist or should not be prominent.

### P1 — Establish 10–15 canonical checkpoints

Include:

- the three tab homes;
- onboarding’s decisive moments;
- place discovery/detail;
- add-to-trip confirmation;
- Trip Home and a meaningful change;
- Vesper recommendation/action;
- representative empty/loading/error/thin-content states.

Each checkpoint needs:

```yaml
id: places-home-returning
journey: discover-to-save
design_source: claude-design | figma | accepted-native
design_project: ...
design_node_or_page: ...
reference_capture: ...
implementation_route: ...
fixture: ...
device_profile: ...
owner_components: [...]
status: accepted
approved_at: ...
```

### P2 — Make Maestro produce canonical evidence

For each selected journey:

1. reset to a known world;
2. execute the actual native path;
3. assert critical semantic state;
4. capture only named checkpoints;
5. verify material backend outcomes where relevant;
6. preserve first-attempt/flaky/failed classification; and
7. write an evidence receipt bound to commit, build, fixture, device, and
   reference.

### P3 — Introduce the strict visual report

Run deterministic checks first, then two qualitative passes:

1. screenshot-only product-quality critique;
2. screenshot-versus-reference intent critique.

Convert findings into implementation tasks ordered by severity and owning
layer. Re-capture after fixes.

### P4 — Build and score the calibration set

Use existing accepted and rejected screenshots before producing new examples.
Do not allow the visual judge to block merges until its false-negative behavior
is understood.

### P5 — Consolidate production primitives

Use defect frequency to identify high-leverage fixes in:

- typography roles and font loading;
- spacing scale and screen gutters;
- card/row/sheet geometry;
- image treatments;
- button and control families;
- empty/loading/error compositions;
- icon alignment; and
- navigation and transitions.

Shared primitive fixes have much higher return than repeated one-screen pixel
tweaks.

### P6 — Run the bounded Figma pilot

Only after the checkpoint/receipt model is working, test whether Figma improves
handoff for the three home surfaces and shared primitives. Measure time to
implement, visual defects, clarification cycles, and design-code drift. Expand
only on demonstrated benefit.

## 17. Things deliberately not to build yet

- Do not migrate all Claude Design pages and modules into Figma.
- Do not screenshot every route and every fixture.
- Do not make pixel identity the definition of adaptive native quality.
- Do not deploy an elaborate hosted visual platform before the rubric and
  calibration set are useful locally.
- Do not ask one agent to generate, implement, and certify its own work.
- Do not make live provider responses or shared cloud state the canonical
  visual baseline.
- Do not update screenshot baselines automatically after a failure.
- Do not require AI judgment for deterministic facts.
- Do not let visual polish substitute for core-loop value, correctness, or
  stickiness.
- Do not document all features equally; protect the journeys that make the
  product thesis legible.

## 18. Product and certification metrics

Visual QA is successful when it improves product quality efficiently, not when
it generates many reports.

Useful measures:

- time from implementation to first native evidence;
- percentage of golden checkpoints with fresh valid captures;
- first-attempt journey pass rate;
- visual defects per checkpoint by severity and owning layer;
- recurrence rate of previously fixed defect classes;
- time from defect to accepted recapture;
- AI-pass/human-block false-negative rate;
- proportion of visual fixes made in shared primitives rather than locally;
- design-reference ambiguity incidents;
- cross-platform or large-text defects caught before dogfood; and
- human minutes per accepted checkpoint.

Keep these beside product measures:

- time to first value;
- save/add/accept/correct progression;
- cross-root continuation;
- durable outcome completion;
- return-trigger activation; and
- evidence that subsequent recommendations improve.

## 19. Immediate recommended package

The smallest useful package is four artifacts and one pilot:

1. **Golden-journey registry** — which user loops matter.
2. **Canonical visual-checkpoint manifest** — exactly which states are accepted
   visual contracts.
3. **Maestro capture receipts** — repeatable native evidence for those states.
4. **Calibrated defect report** — strict, localized, independent visual review.
5. **One journey pilot** — recommended: Places → Vesper proposal → Trips durable
   result, including the three corresponding home or receipt checkpoints.

This closes the essential engineering loop:

```text
product intent
    ↓
golden journey
    ↓
known deterministic state
    ↓
native implementation
    ↓
Maestro execution and screenshots
    ↓
strict behavioral and visual review
    ↓
defects routed to content, token, component, screen, native layer, or substrate
    ↓
accepted evidence and reusable learning
```

## 20. Open decisions

1. Which 3–5 journeys are canonical for the current product pivot?
2. Which 10–15 screenshots should constitute the first accepted checkpoint set?
3. Who has final authority to label the calibration examples?
4. Which device widths and accessibility permutations are required initially?
5. Which current Claude Design pages are accepted references rather than
   exploration or history?
6. Should the first reference authority remain immutable Claude Design exports,
   or should the three home surfaces enter a Figma pilot immediately?
7. What AI false-negative rate is acceptable before any criterion becomes
   blocking?
8. Which local real-stack journey should be certified first?
9. Which visual defects recur frequently enough to justify a production
   primitive change?

## 21. Existing internal documents

- [Product-loop coherence, Maestro, and environment strategy](product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md)
  contains the broader product-loop, current Maestro-estate, evidence, and
  environment analysis.
- [Frontend Engineering Loop](../../travel-app/docs/Frontend%20Engineering%20Loop.md)
  is the existing operational source for AI-assisted frontend iteration,
  screenshot QA, and dogfood visual review.
- [Design Workflow](../../travel-app/docs/Design%20Workflow.md) explains the
  current Claude Design method: the screen as substrate diagnostic, Page Specs,
  friction triage, propagation, and the web-to-native limitation.
- [Product-Quality AI Design QA Loop](../../travel-app/docs/research/Product-Quality%20AI%20Design%20QA%20Loop.md)
  contains the detailed visual rubric, acceptance ladder, prompt templates, and
  research-derived anti-patterns.
- [Frontend Engineering Loop with AI Agents and Screenshot QA](../../travel-app/docs/research/Frontend%20Engineering%20Loop%20with%20AI%20Agents%20and%20Screenshot%20QA.md)
  contains the longer research treatment of tool roles, screenshot alignment,
  design-to-code contracts, component-level visual regression options, and the
  proposed operating model.
- [Vesper design-file consolidation plan](design-file-consolidation-2026-07-29.md)
  records the 66-page/215-module Claude Design inventory, existing audits, and
  design-authority diagnosis.

## 22. External research and current product documentation

- Anthropic documents Claude Design’s conversational canvas, design-system
  import, `/design-sync`, Claude Code handoff, exports, collaboration, MCP, and
  current beta limitations:
  [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design).
- Figma documents structured MCP access to frames, components, variables,
  layouts, code generation, and write-back:
  [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/).
- Figma Dev Mode provides inspection, comparison, annotations, assets, Ready for
  Dev status, and developer handoff:
  [Guide to Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode).
- Figma Code Connect maps design components and properties to production code,
  including React Native:
  [Code Connect](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect).
- Figma variables and modes provide a structured design-token substrate:
  [Variables, collections, and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes).
- Figma version history supports named, restorable, and shareable checkpoints:
  [File version history](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history).
- Maestro’s operating and selector model is documented in
  [How Maestro works](https://docs.maestro.dev/get-started/how-maestro-works)
  and [Selectors](https://docs.maestro.dev/api-reference/selectors).
- Maestro describes AI assertions as experimental:
  [assertWithAI](https://docs.maestro.dev/api-reference/commands/assertwithai).
- Expo documents managed Maestro execution and first-attempt/flaky/failure
  distinctions through
  [EAS E2E with Maestro](https://docs.expo.dev/eas/workflows/examples/e2e-tests/)
  and [Expo Maestro Insights](https://docs.expo.dev/eas-insights/maestro/).

## 23. Promotion and expiry

If the pilot succeeds:

1. promote the checkpoint schema and visual verdict schema into a durable
   frontend certification contract;
2. place the live checkpoint registry next to the existing surface/journey
   registry rather than inside this narrative note;
3. add the calibrated review workflow as a reusable Codex skill;
4. keep current execution state generated from receipts;
5. record the Figma/no-Figma decision in a short ADR; and
6. archive or expire this document once its decisions have durable owners.

If the pilot does not reduce manual review time or catch meaningful defects,
retain the useful reference and receipt improvements and remove the additional
AI ceremony.
