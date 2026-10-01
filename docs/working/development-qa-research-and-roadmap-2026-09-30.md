---
doc_type: working
status: active
owner: founder / engineering
created: 2026-09-30
last_verified: 2026-09-30
expires: 2026-10-30
why_new: Combines the September 30 three-session trace audit with mobile testing and agent verification research into a bounded QA improvement proposal; the September 7 instruction audit is historical, the native-quality plan owns product presentation, and the CI runbook must describe adopted operations rather than absorb research.
supersedes: []
source_of_truth_for: []
---

# Faster development with trustworthy QA

**Decision:** What should Vesper change about building, testing and reviewing work?
**Research cutoff:** September 30, 2026. **Status:** findings and proposed roadmap;
no runtime, required check, test obligation or lane assignment changes here.

**Second research pass:** the [deeper evidence review](#second-research-pass-defect-detection-and-the-cost-of-review)
adds recent mobile/GUI studies and industrial test-selection and mutation-testing
evidence. It strengthens the case for testing whether QA catches important
defects before expanding autonomous review or caching.

## Recommendation

Vesper has useful verification machinery, but the observed workflow spends too
many attempts recovering the test environment and repeating broad verification.
Screenshot review also finds real defects. The right improvement is to make the
environment dependable and match verification to the changed behavior, while
retaining deeper review for shared foundations and coherent product milestones.

The first investment should be **a reliable native QA entry point and a clear
small-change path**. Preserve the current Maestro, Jest, pytest, contracts and
measurement tools. Add caching or another QA agent only after measurements show
that simpler repairs leave a material bottleneck.

The second pass adds a concrete safeguard to that simplification: require
observable outcomes for critical actions, and replay a small set of known defects
plus clean cases to check the QA process itself. Navigation success, screenshot
capture, test-count growth and line coverage are insufficient substitutes.

This also supports the product direction: verify that an original remains
accessible, a collection remains coherent and an audience receives exactly what
was shared. Those durable outcomes matter more than the number of screenshots
or the elegance of one generated answer. Model upgrades should be assessed
against those outcomes and a separate quality sample.

## 1. What the repository and traces establish

### Scope and limits

Canonical checkouts were clean before this documentation change:

| Repository | Inspected main revision |
| --- | --- |
| Workspace | `7b02b2bfe5d36e53060eee5f9fee6f8b5fd4d399` |
| Backend | `3c170d21fc0ca9231b956f2b9de7f9f195231768` |
| App | `87eceee24512d9086962eea5b844cef9d7bffbeb` |

The app declares Expo `~55.0.31` and React Native `0.83.10`. Source inspection
covers the current tooling and contracts; it does not certify the running app.
The session audit covers **September 30, 00:00–18:34:27 America/New_York**
(`04:00:00–22:34:27 UTC`), including unmerged work in the three active lanes.
Later progress is outside that sample.

Local Codex trace records were deduplicated by command-execution identity and
classified by the requested shell operations. Counts below are **command
bundles**, not individual screenshots, inner retries or elapsed QA time. An
earlier command in a bundle can fail before the requested operation starts.
Native GUI actions are excluded. A failed command is not a product-defect verdict.

| Session | Capture bundles | Failed capture bundles | Device/preflight bundles | Failed preflight bundles |
| --- | ---: | ---: | ---: | ---: |
| Orchestration | 12 | 10 | 17 | 13 |
| Strategy | 49 | 24 | 20 | 18 |
| Strategy Technical | 0 | 0 | 0 | 0 |

Separately, the classifier found 35 repository-gate bundles in Strategy and 72
in Strategy Technical. These include legitimate reruns after changes and failed
setup; the counts do **not** establish how many were redundant. No comparable
Orchestration gate count is asserted from this filter.

The diagnostic extract is local at
`/private/tmp/vesper-qa-audit-20260930.json`; it is temporary, not a repository
dependency. Trace identities are recorded in the appendix so the sample can be
reconstructed without committing private session transcripts.

### Findings

| Finding | Evidence and implication | Confidence |
| --- | --- | --- |
| Native setup is a major source of repeated attempts. | Traces contain simulator-service failures, unavailable Metro, lock-directory write failures, a native/JavaScript Worklets mismatch, and a run using the default device instead of its reserved device. These need runtime repair, not more visual judging. | High for occurrence; time share unmeasured. |
| Some visual QA is clearly valuable. | Strategy's large-text pass found clipping in the shared artifact reader and displaced source actions. A responsive fix followed. Removing that check would remove useful coverage. | High for this case; no aggregate defect-yield estimate. |
| Completing a capture command does not establish the intended behavior. | A supposed cold-state capture contained content; separate gesture captures had identical image hashes despite issued gestures. Keep, navigation, pan, pinch and assistive interaction need observable outcomes. | High for the sampled cases. |
| The preferred wrapper can widen the requested work. | `qa:surface` parses flags but does not forward a selected `--flow` to its capture child. The lower-level runner supports flow selection. An apparently targeted invocation can therefore capture the whole surface. | High, source-inspected. |
| Review instructions contain avoidable ceremony and contradictions. | The verdict protocol asks for at least two findings per persona, with a special explanation for zero. Its older perceptual-hash carry section conflicts with its later exact-input rules and implementation. | High, source-inspected. |
| Change-aware gates already exist, but broad fallback remains common. | App selection intentionally expands shared mocks, API files, deleted/unknown inputs and configuration changes. Repeated selection against an old integration base keeps those earlier changes in scope. Narrow final checks cannot simply ignore them. | High for selection mechanics; redundant runtime unmeasured. |
| QA inventory size is not evidence of executed overhead. | Main contains 47 registered surfaces, 406 tracked Maestro flow/helper YAML files and 933 screenshot declarations. They are not all run for every change. | High for the dated inventory. |

The 47 surfaces already have differentiated obligations: 10 showcase, 15 shared
systems, 9 utility, 10 compatibility and 3 development fixtures. There are also
11 baseline definitions, 6 animation definitions and 70 committed verdict JSON
files across 30 surfaces. Historical verdicts are not a current readiness score;
fresh lane evidence may not yet be on main.

Owning sources: [surface index](../../travel-app/docs/surfaces/README.md),
[registry](../../travel-app/scripts/polish-qa/surfaces.mjs),
[surface wrapper](../../travel-app/scripts/polish-qa/run-surface-qa.mjs),
[verdict protocol](../../travel-app/docs/surfaces/_agent-verdict-protocol.md),
[carry implementation](../../travel-app/scripts/polish-qa/judgment-inputs.mjs)
and [app test selector](../../travel-app/scripts/merge-scope.mjs).

## 2. How building something works today

The intended process is already reasonably structured:

1. Establish the lane and current revisions; use the documentation index,
   affected Task Intake and owning contract to locate constraints.
2. Implement a coherent behavior and run focused tests while iterating.
3. For backend wire changes, regenerate and review the API snapshot, mobile
   projection, generated types and consumers together.
4. For relevant UI changes, run the registered native surface path: scenario
   validation, design-reference checks, device preflight, capture, comparison,
   capture-health checks where configured, and a completed visual verdict.
   Applicable contracts allow a documented manual fallback.
5. Run change-aware local merge preflight with explicit bases for all three
   repositories. Hosted required checks remain authoritative. Full regression
   belongs to the configured main/nightly/release stages and deliberate diagnosis.

Sources: [workspace instructions](../../AGENTS.md),
[app Task Intake](../../travel-app/docs/Task%20Intake.md),
[backend Task Intake](../../travel-agent/docs/operations/Task%20Intake.md), and
[Reliability CI](../reliability/CI%20Plan.md).

The September 30 CI work has already introduced scoped merge checks and records
hosted cutover evidence. This report does not repeat the September 7 finding
that CI was disabled as if it were current. It also does not independently
recheck GitHub protection settings, secrets or hosted runs. Workflow definitions
and dated execution receipts establish different things.

The remaining friction is between the intended tiers and actual execution:
broad UI triggers meet a substantial verdict process; setup failures cause
repeated recovery; and long-lived changes keep selecting broad test families.
The solution is to finish making the existing tiers usable, not invent another
mandatory verification framework.

## 3. What current external research supports

There is no single established “SOTA” workflow or credible universal screenshot
quota. The strongest transferable practice combines mature testing principles
with newer mobile-build reuse and selective agent exploration. The evidence
below distinguishes official tool capabilities from vendor experiments.

| Area | What the source actually supports | Implication for Vesper |
| --- | --- | --- |
| Test layers | React Native recommends user-visible component assertions and reserves slower, more fragile device E2E coverage for vital flows. JavaScript component tests do not establish native behavior. [React Native 0.83 testing](https://reactnative.dev/docs/0.83/testing-overview) | Put state/permission logic in deterministic tests; retain native proof for rendering, gestures and critical integrated flows. |
| Local build reuse | Expo development clients can load changing JavaScript; adding native code requires rebuilding the client. [Expo development builds](https://docs.expo.dev/develop/development-builds/use-development-builds/) | A layout edit should normally reuse a compatible installed client. A native mismatch should produce a specific rebuild reason. |
| Native compatibility | Expo's SDK 55 fingerprint represents native-relevant inputs, but raw config-plugin functions have documented hashing limitations. [SDK 55 Fingerprint](https://docs.expo.dev/versions/v55.0.0/sdk/fingerprint/) | Use a version-compatible fingerprint plus explicit coverage for local plugins/configuration. Unknown identity must require a rebuild. |
| QA without Metro | Expo Repack produces a new installable artifact from an existing compatible native build and fresh JavaScript/assets. It is intended for internal testing; production store submissions should use the full pipeline. [Expo Repack](https://docs.expo.dev/build-reference/repack/) | Pilot a bundled simulator app for repeatable QA. This is a candidate optimization, not a proven drop-in for our SDK/configuration. |
| Reproducible screenshots | Playwright warns that rendering differs across environments and recommends matching the baseline environment. It supports stabilizing volatile content. This is web tooling, not native certification. [Visual comparisons](https://playwright.dev/docs/test-snapshots) | Transfer the principle: fix device/OS, text size, locale, time, fixture and build identity. Do not compare live generated prose as a pixel baseline. |
| Deterministic UI checks | Maestro's ordinary visibility assertions wait for the expected element. Its AI visual assertion is experimental and optional by default because responses can be unstable. [assertVisible](https://docs.maestro.dev/reference/commands-available/assertvisible), [assertWithAI](https://docs.maestro.dev/reference/commands-available/assertwithai) | Use normal assertions for known outcomes; calibrated vision review adds evidence where structure cannot express the requirement. |
| Native accessibility | Apple supports automated accessibility audits from XCTest, including diagnostics for descriptions and contrast. The audit inspects the current view. [Apple accessibility audits](https://developer.apple.com/videos/play/wwdc2023/10035/) | Preserve large-text and assistive-navigation evidence. Explore a small audit pilot only if it reduces repeated manual work; do not introduce a second full E2E suite now. |
| Agent-driven mobile QA | A Callstack engineering example hosted by Expo separates deterministic installation/launch from agent exploration and reuses native builds. It is a working pattern, not comparative reliability evidence. [Expo/Callstack QA agent](https://expo.dev/blog/build-an-ai-qa-agent-for-expo-apps-with-eas-workflows-in-minutes-today) | Make bootstrap predictable first. Later trial bounded exploratory QA around a coherent feature; retain explicit acceptance criteria from our contracts. |
| Agent workflow simplification | Anthropic removed harness components one at a time as model capability improved; in its experiment, evaluation moved from every sprint to the end of a run. Evaluators still helped on difficult work. [Harness design, March 24, 2026](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Test a lighter small-change review path. Do not infer that all independent evaluation is waste or that its reported gains transfer here. |
| Evidence reuse | Bazel documents reuse based on declared inputs, tools and environment, and warns about uncontrolled inputs and concurrent source changes. [Hermeticity](https://bazel.build/basics/hermeticity), [remote caching](https://bazel.build/remote/caching) | Reuse requires a complete identity and an unchanged execution boundary. Adopt that principle without migrating these repos to Bazel. |
| AI product quality | Anthropic distinguishes deterministic, model and human graders; model graders need calibration. Capability evaluation and regression protection answer different questions. [Agent evals, January 9, 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Evaluate useful artifacts and research quality separately from native layout and authority invariants. A model upgrade can improve one dimension while harming another. |
| Delivery feedback | DORA recommends fast automated feedback, developer ownership and continuous test-suite improvement. Its under-ten-minute guidance is not a guarantee for Vesper. [Test automation](https://dora.dev/capabilities/test-automation/) | Measure the existing under-five-minute ordinary merge-readiness objective; include setup, queueing, repairs and later defects. |

All sources were accessed September 30, 2026. Documentation proves advertised
mechanisms, not our local integration. Vendor case studies motivate experiments;
they do not establish causal productivity gains in this repository.

### Second research pass: defect detection and the cost of review

This pass examined primary research beyond vendor usage guides. The results
below are evidence about particular systems, datasets and model versions, not a
benchmark of our current coding agent. The existing local trace window remains
unchanged; no new product defect or runtime result is claimed.

**1. A capable app operator is not automatically a capable tester.**
GUITester, published in ACL Findings in July 2026, studies mobile exploratory
testing with 143 tasks around 26 defects. The inspected January manuscript
reports its best F1 as 48.90 under a three-attempt setting, compared with 33.35
for its strongest baseline. These are benchmark detection scores, not release
reliability percentages. Its analysis describes agents working around anomalies
to complete tasks or attributing defects to their own execution errors. The
evaluation uses selected models and a model judge; it does not establish the
capabilities of every September 2026 agent.
[Published paper record](https://aclanthology.org/2026.findings-acl.946/),
[inspected manuscript and evaluation](https://arxiv.org/html/2601.04500v1).

**Vesper implication:** “opened the reader” should not close an acceptance case
that requires zooming, returning to the same original, or retaining a correction.
State the expected result before execution and observe it afterward. Do not let
an alternate successful path erase a broken intended path.

**2. Combining ordinary automation with selective visual reasoning has direct
mobile evidence.** VLM-Fuzz, published in February 2026, uses conventional GUI
exploration and invokes a vision model for complex screens. It evaluates 59
benchmark Android apps and separately reports 52 distinct crashes in 12 of 80
store apps. The authors distinguish real bugs from crashes caused by the test
environment and acknowledge weaknesses with non-visible interactions such as
long presses. These Android crash/coverage results do not establish iOS visual
quality, and the comparator setup limits broad superiority claims.
[VLM-Fuzz, methods, results and limitations](https://link.springer.com/article/10.1007/s10664-026-10816-4).

**Vesper implication:** retain deterministic launch, fixture selection, navigation
and ordinary assertions. Use visual reasoning for layout and genuinely ambiguous
states. Keep explicit gesture tests; a screenshot cannot establish every action.

**3. Change-aware exploration is promising, but its findings need triage.**
RippleGUItester compares pre/post-change behavior using the change's stated intent.
Across four desktop applications, its Table 1 lists 148 true and 171 false-positive
reports, or 46.4% precision. A nearby prose sentence inconsistently calls 111 the
true-positive count; 111 is the table's PR count. The authors report an average
54.8 minutes per PR and, among 26 newly reported cases still present in current
versions, 16 fixed and 2 confirmed. This is a preprint with selected desktop
changes, not a cost or accuracy estimate for our app.
[RippleGUItester, March 2026, Tables 1 and cost analysis](https://arxiv.org/html/2603.03121v1).

**Vesper implication:** explore adjacent behavior when a shared component changes,
but make exploratory reports advisory until reproduced. An always-running visual
judge can move the bottleneck into reviewing false alarms. Measure confirmed
findings and triage effort, not raw report volume.

**4. Clear expected outcomes help more than another broad “looks good” review.**
WebTestPilot translates requirements into assertions over successive GUI states.
Its inspected revision reports 96% precision and recall on injected bugs across
100 cases in four web apps. The benchmark deliberately constructs requirements
and faults; the approach assumes complete, self-contained requirements. The
score cannot be transferred to open-ended mobile exploration or incomplete specs.
[WebTestPilot, benchmark construction and limitations](https://arxiv.org/html/2602.11724v3).

**Vesper implication:** make acceptance concrete without creating longer specs.
For example: after adding an original to a collection, reload it and verify the
same original is still present; after removing an audience member, verify the
owner's access rules at the server boundary. “The collection screen renders” is
a narrower claim. These are proposed cases, not newly observed repository bugs.

**5. Captioning a visual difference is not judging product correctness.**
The July 2026 WUICC study explores describing screenshot changes in language.
Its limitations matter: synthesized HTML pages, one controlled change per pair,
caption-similarity metrics, and only two relatively small open vision models as
zero-shot general-purpose baselines. It does not establish that a modern frontier
vision judge can safely approve native UI changes. Even an accurate description
of changed text does not decide whether that change is intended.
[Beyond Pixel Diffs, dataset and validity discussion](https://arxiv.org/html/2607.01728v1).

**Vesper implication:** a visual-diff summary could reduce reviewer effort, but
must remain tied to the contract and changed behavior. Pilot it as assistance,
not automatic baseline approval. Preserve whole-screen context when examining
small crops, particularly for hierarchy, clipping and displaced actions.

**6. Test selection should be evaluated by missed regressions, not just speed.**
Meta's 2018 deployment report describes running roughly one-third of dependent
tests while detecting regressions in over 99.9% of problematic changes, trained
from extensive history and paired with exhaustive testing before deployment.
This is an industrial report, not a guarantee for another selector.
[Meta predictive test selection](https://engineering.fb.com/2018/11/21/developer-tools/predictive-test-selection/).

A contrasting Google 2026 publication abstract reports catching regressions in
40% of failing commits with a 2,000-test budget on ten highly connected libraries,
at 0.9% of reported execution cost. Only the official abstract was available in
this review; its full methodology was not inspected. The different setting and
budget make the two results unsuitable for a direct comparison.
[Google regression test selection](https://research.google/pubs/regression-test-selection-at-scale-3/).

**Vesper implication:** retain conservative fallback for shared/unknown changes.
Compare selected runs with broader results on a bounded pilot and retain the
first missed regression as a routing test. Do not build a predictive ML selector
before ordinary dependency selection and measurements demonstrate a need.

**7. A useful test should distinguish correct behavior from a relevant fault.**
Meta's 2025 mutation-guided testing paper reports 571 generated tests against
previously uncaught simulated faults; 277 would have been discarded by a criterion
requiring increased line coverage. In its developer trials, acceptance and privacy
relevance were different measures. Catching a generated fault is evidence of
that test's sensitivity, not a guarantee against all real bugs.
[Meta mutation-guided test generation](https://arxiv.org/html/2501.12862v1).

Google's practical mutation-testing work deliberately limits analysis to changed
code and filters unhelpful mutations to control cost and developer attention.
This supports targeted evaluation of tests, not a new repository-wide mutation
score mandate. The official research summary was inspected for this finding.
[Google practical mutation testing](https://research.google/pubs/practical-mutation-testing-at-scale-a-view-from-google/).

**Vesper implication:** for high-consequence boundaries, occasionally demonstrate
that the relevant test fails when a known bad behavior is reintroduced in an
isolated test environment. Use existing incidents and fixtures first. Keep fault
injection out of shared development data and production, and avoid manufacturing
large new suites solely to increase a score.

**8. More agent-authored tests do not establish better integration coverage.**
A January 2026 observational study of 2,168 repositories found mocks added in
36% of agent-authored test commits versus 26% of other test commits. Its within-repo
effects were smaller, and its identifier/commit-attribution methods have limits.
It measures mocking activity, not whether those mocks were inappropriate or
whether the tests caught fewer bugs.
[Over-mocked tests study, methods and limitations](https://arxiv.org/html/2602.00409v1).

**Vesper implication:** sample important tests to see whether they exercise the
boundary they claim to prove. A mocked reader can establish rendering behavior;
it cannot establish that collection persistence or access control works. Do not
ban mocks or infer a defect in this repository from that study.

#### Roadmap changes resulting from this pass

Keep Packages 1 and 2 first. Add the following acceptance work to existing
packages, rather than creating another process or standing reviewer:

| Existing package | Refinement | Evidence needed |
| --- | --- | --- |
| 1: reliable native QA | Record whether failure occurred during setup, action execution, assertion, capture or review. Do not classify every failed command as an app defect. | Known setup faults receive the right diagnosis; a genuine app failure remains visible. |
| 2: proportional review | Add explicit before/action/expected-after conditions and a small known-defect/clean-case replay set. | The lighter path detects important known defects and does not invent findings on clean or intentional-change cases. |
| 3: candidate verification | During the pilot, compare selected coverage with broader regression results and track misses. | Selection retains important defect detection; shared/unknown changes cannot silently receive a narrow certificate. |
| 4: reuse | Keep build reuse separate from test and judgment reuse; defer automatic semantic visual approval. | Saved time survives the added compatibility checks and triage work. |
| 5: product outcomes | Sample whether tests prove persistence, original identity and audience behavior across the real owning boundaries. | A broken outcome fails even if every rendered screen looks plausible. |

An initial replay sample can remain small: the observed large-text clipping;
wrong-state capture; a no-op gesture/action; and proposed injected faults in
original identity, collection persistence and audience access. Add an intended
visual change and a clean case to expose false alarms. These are pilot inputs,
not a new mandatory matrix for every edit. Reject a narrower rule if it misses
an important replay; diagnose that specific gap before broadening all QA.

For any future exploratory agent trial, record confirmed defects, false reports,
reproduction success, review minutes, execution cost and defects found later.
Use comparable tasks and a fixed budget. A ten-change pilot is useful for finding
process faults but cannot establish a precise rare-defect miss rate. Adopt the
trial only if its useful findings justify the total implementation and review
cost. Current screenshots/tests are not removed by this research update.

## 4. Proposed everyday development path

The developer or agent should make one short acceptance statement, implement,
get focused feedback, inspect the affected native behavior when relevant, then
run the final candidate's required checks. Most changes should not require a
new planning document or a complete persona-by-persona critique.

| Change | During iteration | Acceptance before landing |
| --- | --- | --- |
| Prose or isolated backend logic | Documentation checks or focused behavioral tests. | Applicable change-aware gates; no new screenshot obligation. |
| Local copy/layout/state | Focused component tests where behavior changes, plus the affected native state. | Targeted visual receipt; include long/empty/error content and large text when the change can affect them. |
| Shared reader, typography, navigation or gesture | Representative consumers and relevant interaction tests. | Family-level native matrix, small screen/large text as relevant, and actual transition/gesture evidence. Broaden for affected consumers. |
| API, storage, audience or authority | Owning integration/negative tests and generated-contract checks. | Applicable database/cross-repo proof and a receiving journey; screenshots alone cannot establish persistence or authorization. |
| Prompt, model, retrieval or research quality | Existing replay/quality cases and invariant checks. | Versioned quality comparison plus sampled real outputs; native review only if presentation changes. |
| New product milestone or substantial redesign | Iterate with the paths above. | Full relevant surface review and complete journey through the real ownership boundaries. |

**This table proposes a refinement to the current Task Intake, not an exemption
from it.** Route uncertain/shared changes broadly. Final merge selection still
covers every outstanding change against its real integration base. A narrower
iteration comparison cannot become a misleading merge certificate.

For visual review, propose a compact receipt for a local change: affected
surface/state, before/after when informative, native runtime identity, what was
checked, findings and remaining limitations. Full structured judgments remain
useful for a new surface, shared family or milestone. Zero findings is a valid
result after inspection; a finding quota is not a quality measure.

## 5. Improvement roadmap

Sequence these as small engineering packages within existing ownership. There
is no new standing lane or automatic assignment. Start the next package only
after its prerequisite is demonstrated; calendar estimates would be premature
without a runtime baseline.

### Package 1 — Make native QA start reliably

**Priority:** first. **Proposed owner:** current mobile/runtime tooling owner,
coordinated with the workspace lane owner.

Extend the existing surface entry point to resolve the selected lane's device,
ports, output directory and installed app identity once. Forward supported
selection flags explicitly; reject unknown flags rather than silently widening
the run. Make preflight identify simulator, permission, Metro and native-version
failures before capturing. Use one shared retry budget across wrapper and runner:
after a repeated identical infrastructure failure, retain diagnostics and repair
that cause before another attempt. The result remains blocked/unverified.

**Existing targets:**
[surface wrapper](../../travel-app/scripts/polish-qa/run-surface-qa.mjs),
[runner](../../travel-app/scripts/polish-qa/run-polish-qa.mjs),
[preflight](../../travel-app/scripts/polish-qa/preflight.mjs),
[device lock](../../travel-app/scripts/polish-qa/run-lock.mjs), and
[workspace runtime script](../../scripts/dev.sh).

**Acceptance:** a selected flow runs only that flow on the reserved device;
missing device, denied output directory, wrong native build and missing server
each produce the correct diagnostic without a retry storm. A valid warmed app
completes a real capture in its intended managed worktree. Include both working
and failing cases; mocked command tests alone do not establish simulator access.

### Package 2 — Make review proportional to the change

**Priority:** next; documentation reconciliation can start alongside Package 1.
**Proposed owner:** mobile QA/surface owner with product review for altered
acceptance obligations.

Reconcile Task Intake, AGENTS guidance and lifecycle classes into the table above.
Offer targeted capture/review through the existing command. Remove the finding
quota and the obsolete perceptual-hash carry instructions; retain exact-input
provenance. Pilot on a reader fix and a Home/Places fix. Reuse registered fixtures
and surfaces instead of adding a parallel registry.

**Existing targets:** app [AGENTS](../../travel-app/AGENTS.md),
[Task Intake](../../travel-app/docs/Task%20Intake.md),
[surface index](../../travel-app/docs/surfaces/README.md),
[verdict protocol](../../travel-app/docs/surfaces/_agent-verdict-protocol.md),
and the existing verdict validator/scaffolder beside the surface wrapper.

**Acceptance:** an isolated copy/layout fix receives bounded review; a shared
reader change still selects representative consumers and accessibility cases.
Replay the observed large-text clipping and a wrong-state capture: both must be
detected or explicitly left unverified. A clean case can pass without invented
findings. If the pilot misses an important defect, expand the affected rule and
record why rather than adding a blanket review round.

### Package 3 — Separate iteration from candidate verification

**Priority:** after the selection/review boundary is clear.
**Proposed owner:** workspace CI owner with backend and app selector owners.

Expose the selected tests and reason for broad fallback before expensive work.
During iteration, run the affected behavior's tests; run the integration-base
preflight when a coherent candidate is ready. Consolidate duplicate checks within
one job and reuse their result there. Keep full main/nightly regression and
hosted requirements. Prefer smaller coherent landings to accumulating unrelated
broad-trigger changes in one lane.

**Existing targets:** [workspace selector](../../scripts/verify_changed.py),
[backend selector](../../travel-agent/scripts/merge_scope.py),
[app selector](../../travel-app/scripts/merge-scope.mjs), their tests,
repository workflows and [CI Plan](../reliability/CI%20Plan.md).

**Acceptance:** routing tests cover local, shared, deleted and unknown inputs;
tool failure never becomes an empty passing selection. A candidate with an
earlier shared change still receives broad final coverage after later local
edits. Measure complete real runs before claiming improvement. Changing required
hosted checks remains a separate, explicitly evidenced cutover.

### Package 4 — Pilot a bundled QA app and cautious reuse

**Priority:** conditional on remaining build/Metro cost after Package 1.
**Proposed owner:** mobile build owner. **Dependency:** reliable runtime identity.

Keep the reusable development client for fast local editing. Separately pilot
SDK-compatible fingerprinting and repacking of an embedded-JavaScript simulator
app for repeatable captures. Reuse the current nightly/PR native workflow rather
than replacing it with a new platform. Pin and validate the chosen tool versions.

Treat test-result reuse as a later, separate decision. Initially restrict it to
deterministic tasks with complete input identities. Native build compatibility,
test execution and visual judgment are three different cache keys. Do not cache
live-service, database-state or model-provider success as though it were immutable.
The current visual input hash includes `gitSha`; do not simply delete it to get
more hits. First prove dependency coverage, preserve tested revision, original
judgment time and provenance, and invalidate on relevant contract/reference/data
or code changes.

**Existing targets:** native workflow files, app build configuration,
[judgment inputs](../../travel-app/scripts/polish-qa/judgment-inputs.mjs) and
[measurement tool](../../scripts/measure_verification.py). Keep the exact-current
rules until a separately reviewed implementation establishes safe equivalence.

**Acceptance:** a JS-only change appears in the repacked app with Metro stopped;
a native dependency or local config-plugin change forces rebuilding. Record the
binary, JS bundle, fixture and tool identities. Compare first-run success and
end-to-end time with the existing path. Fall back to full native builds if
compatibility is uncertain; this pilot does not change store-release builds.

### Package 5 — Put quality effort into the product loop

**Priority:** ongoing within the existing three product lanes, after basic QA
friction is controlled. **Proposed owners:** each lane owns its outcomes;
Strategy Technical owns model/research evaluation integration.

Keep a small representative acceptance portfolio drawn from existing contracts
and defects: preserve/open an original, collect and retrieve it, share to the
intended audience, correct it without losing provenance, and present useful
research with sources and uncertainty. Check forbidden audience access and
unauthorized side effects deterministically. Check native interaction separately.
Evaluate usefulness/grounding with explicit rubrics and periodic human calibration.

Start by mapping these cases to the existing
[product proofs](../../travel-agent/eval/product_proofs/),
[artifact quality](../../travel-agent/eval/artifact_quality/) and
[authority evals](../../travel-agent/eval/consequence_authority/), plus existing
journey and native fixtures. Add only missing cases. Keep deterministic fixture
rendering distinct from live-model quality and real-backend persistence.

**Acceptance:** a model/prompt change can be compared with the previous version
for usefulness, grounding, latency and cost while hard authority checks remain
intact. A visually attractive artifact with a broken original, wrong audience or
unsupported claim fails its relevant acceptance. No new global numeric “quality
score” substitutes for those separate outcomes.

## 6. How to tell whether this helped

Use [measure_verification.py](../../scripts/measure_verification.py) and existing
QA manifests. Add missing fields to those records only as needed. Its current
environment record is coarse and its Git record includes HEAD plus dirty state;
that is useful for timing but insufficient as a safe result-cache identity.

For the next ten ordinary changes, record change class and the whole path from
first verification to accepted candidate: setup/queue/execution, failed attempts,
repair/review time, repeat checks and material defects found. Treat this as a
diagnostic pilot, not a statistically powered productivity experiment. Compare
similar changes, report sample sizes and spread, and retain failed runs. Do not
sum overlapping concurrent durations as human time lost.

Track first-attempt native setup success, time to first useful native result,
ordinary merge-readiness time, review false alarms, and later regressions/rework.
The existing under-five-minute merge target remains an objective; no new timing
target is claimed as achieved here. Screenshot count and test count are workload
descriptors, not success metrics.

After the pilot, retain changes that improve delivery with adequate defect
detection; repair or revert weak selection/reuse rules. Full-suite comparisons,
known-defect replay and sampled deeper review are controls during the pilot,
not permanent extra gates on every change.

## 7. Boundaries and decisions

Keep generated contracts, ownership/authority tests, real native interaction,
large-text coverage and honest evidence limits. Do not replace deterministic
assertions with a vision model, bulk-delete flows to hit a quota, auto-approve
changed baselines, or add another standing judge layer before measuring need.

The recommended first implementation is Packages 1 and 2. Packages 3–5 extend
existing CI and product work; Package 4 is conditional. This proposal does not
change the [program roadmap](vesper-program-roadmap.md) or message its owners.
Adopted operational changes should update their existing owner documents; close
or archive this research note by October 30.

## Appendix: evidence and continuity

Earlier related work:
[September 7 engineering research](engineering-context-and-agent-practices-research-2026-09-07.md)
and [native-quality consolidation](content-to-native-quality-consolidation-plan-2026-09-15.md).
They retain their dated findings and distinct scope.

Trace files inspected for the bounded sample, relative to
`/Users/feihuyan/.codex/sessions/`:

- Orchestration: `2026/09/29/rollout-2026-09-29T23-58-14-01a072c6-2735-7152-94ea-bb6958ead53d_01a0f076-86a0-7d43-9b95-d25fd11c54a8.jsonl`.
- Strategy: `2026/09/29/rollout-2026-09-29T22-00-03-01a08d4e-3ee2-7d80-9add-a5179aaf3b8e_01a0f00a-51bd-7620-8ee8-66bb78a5a4b4.jsonl`.
- Strategy Technical: `2026/09/12/rollout-2026-09-12T19-43-02-01a09800-c3f9-7133-82a8-5d345ce863dd.jsonl`.

Useful Strategy trace anchors: `21:03:47Z` wrong-device recapture report;
`21:22:12Z` fixture-native matrix report; `21:37:30Z` large-text clipping report.
These are transcript observations, not independently repeated device tests.

Repository inspection used `python3 scripts/session-context.py`, Git status,
branch/worktree/revision reads, tracked-file inventories and targeted source
reads. This research did not execute product suites, a simulator, a live-model
comparison or a hosted-CI audit. Documentation-check results belong to the
delivery receipt for this note, not to product readiness.
