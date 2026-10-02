---
doc_type: working
status: active
owner: founder / Eng Efficiency
created: 2026-09-30
last_verified: 2026-10-02
expires: 2026-10-30
why_new: Combines the September 30 trace audit and engineering research with this lane's improvement sequence; the September 7 instruction audit is historical, the native-quality plan owns product presentation, and the CI runbook describes adopted operations rather than pending work.
supersedes: []
source_of_truth_for: []
---

# Faster development with trustworthy QA

**Decision:** What should Vesper change about building, testing and reviewing work?
**Research cutoff:** October 1, 2026, with October 2 targeted code, hosted-run
and upstream-advisory rechecks. **Planning and execution update:** October 2,
following the founder’s request for independently executable overnight goals. [Section 5](#5-improvement-roadmap) remains the
single execution queue. Begin with the next measured verification bottleneck;
fix obsolete assumptions when they obstruct current work and retire an old
implementation family only when its maintenance burden justifies the work.
Keep the existing native QA and same-coverage test improvements; unfinished
infrastructure awaiting product design is not an obsolete-code candidate.

The historical October 1 integration landed at workspace
`7018d055c6635b0edb5726612375c03f2c785520`; roadmap-only PRs #42/#43 advanced the
inspected workspace main to `0b8792793fc25eceb8967edf7b832fe0f0194934`.
That historical child pair was backend `0a1fdf224aaf59ca713eec5eba79a34321f038a9`, and app
`acf5bd837fe3725b00d9744727f513a601fb2498`, landed through central integration
[workspace PR 41](https://github.com/fy538/travel-workspace/pull/41),
[backend PR 241](https://github.com/fy538/travel-agent/pull/241), and
[app PR 212](https://github.com/fy538/travel-app/pull/212). Workspace PR 40's
changes are included and it is now merged. App PRs 209/210/211 and backend
PRs 239/240 are merged. The final sharding trial
[run 36931263750](https://github.com/fy538/travel-app/actions/runs/36931263750)
passed after stabilization; its earlier failed baseline remains evidence, and
no repeatable speedup or default sharding adoption is claimed. Package 1 has
one passing targeted native capture; Package 2's original Home/Places
wrong-state replay remains unverified.

Git cleanup retired six completed lanes (17 checkouts), 15 local branches and
seven remote branches. The four execution lanes and product-direction checkout
remain. All canonical main checkouts are current and clean. Uncommitted owner
work, five experiment measurements and ignored evidence were preserved in
local recovery snapshots, not silently promoted to main or product acceptance.
An updated roadmap does not prove that obsolete assumptions have been removed.

**Second research pass:** the [deeper evidence review](#second-research-pass-defect-detection-and-the-cost-of-review)
adds recent mobile/GUI studies and industrial test-selection and mutation-testing
evidence. It strengthens the case for testing whether QA catches important
defects before expanding autonomous review or caching.

**Third research pass:** [repository efficiency](#8-repository-efficiency-and-a-shorter-delivery-path)
adds direct hosted step timings, documentation inventory, remaining CI duplication
and a revised execution order. App test execution dominated that pass's app-only
sample; the completed integration below establishes a larger workspace bottleneck.

**Completed integration review:** [September 30 landing evidence](#9-completed-integration-review)
adds the final three-repository merge tuple and critical-path timings. Reliability
improved, but faster end-to-end delivery is not yet demonstrated. This evidence
reorders section 5 without removing the native-quality work.

## Recommendation

Vesper has useful verification machinery, but the observed workflow spends too
many attempts recovering the test environment and repeating broad verification.
Screenshot review also finds real defects. The right improvement is to make the
environment dependable and match verification to the changed behavior, while
retaining deeper review for shared foundations and coherent product milestones.

The first integration investments—faster workspace flow validation, early
prerequisite checks, deterministic app tests and less repeated execution—have
landed with the evidence limits above. Section 5 now prioritizes a bounded trial
against observed feedback cost. The earlier cleanup-first order had weaker
benefit evidence: already-skipped tests incur no execution cost, and moving
documents alone has not demonstrated faster delivery. Cleanup remains useful
where an active task encounters conflicting ownership or repeated legacy work.
Choosing evidence for the changed behavior and making targeted native QA reliable
remain required work, but do not block these device-independent improvements.
Screenshots primarily establish visual state and support failure diagnosis;
persistence, permissions and interaction outcomes need their own checks.
Preserve the current Maestro,
Jest, pytest, contracts and measurement tools. Shorten task-specific reading,
remove duplicated execution and land smaller coherent changes. Prioritize
measured execution costs over a new build platform or additional reviewer agents.

The second pass adds a concrete safeguard to that simplification: require
observable outcomes for critical actions, and replay a small set of known defects
plus clean cases to check the QA process itself. Navigation success, screenshot
capture, test-count growth and line coverage are insufficient substitutes.

This also supports the product direction: verify that an original remains
accessible, a collection remains coherent and an audience receives exactly what
was shared. Those durable outcomes matter more than the number of screenshots
or the elegance of one generated answer. Model upgrades should be assessed
against those outcomes and a separate quality sample.

## Execution status — October 1, 2026

The following records describe earlier checkpoints on that date. Their pending
PR states are historical; the accepted baseline and current queue above and in
section 5 supersede them. Keep their failure and acceptance evidence intact.

**Package 3C — CI sharding and early checks:** workspace [PR #38](https://github.com/fy538/travel-workspace/pull/38)
merged as `bc69d6d03eeb069eb8705953463b4ddc8a808e6d`. Three hosted runs validated
the complete 408-flow syntax inventory. Required-check critical paths ranged
from 5m46s to 7m38s, versus 23m18s on the serial baseline; summed runner time
rose by 9.3% to 34.9%. The Maestro Cloud PR smoke remains skipped because the
service is not configured. The samples support faster feedback with higher
runner use, not a stable percentile or lower resource cost.

**Package 1 — targeted native QA:** implementation is published in app PR #209
and workspace PR #39. Exact-flow selection, device/port binding, readiness
diagnostics and one shared retry budget passed the focused and broader QA
checks. The first real capture attempt used the wrong shell configuration,
showed the legacy Plans screen and failed the `home-v2-screen` assertion before
capturing product images. The assertion correctly caught an environment error.

The corrected run used the assigned iPhone SE (3rd generation), UDID
`E5200CAA-0A20-4D67-B5C6-A418603A5FEC`, Maestro 2.6.1, Java 17, Metro port
`57436`, and installed app `com.fyan.vesper` version `1.0.0`. Expo was bound to
IPv4 localhost with `NODE_OPTIONS=--dns-result-order=ipv4first`; the documented
mock/auth, four-root, projection, Places/Life and internal-build flags were set.
`HOME_SURFACES_CANON_DIR=/Users/feihuyan/Downloads/vesper-home-surfaces npm run qa:surface -- home-root --flow=polish/home-root-returned --after`
passed 1/1 and captured `home-root-returned-top.png` and
`home-root-returned-close.png`. This is one reviewed Home return-state capture;
it does not prove persistence, permissions or the separate Home/Places
wrong-state replay, which remains unverified.

**Package 3B — CI execution ownership:** the corrected backend workflow is
published in PR #240. Its first run failed closed after the two-minute scope job
cancelled a full-history checkout; the current run's scope checkout and
selection passed in 14 seconds. At the latest status read, the selected offline
tests and database checks passed, as did the `Merge ready` aggregate. Run
[36894505540](https://github.com/fy538/travel-agent/actions/runs/36894505540)
is fully green, and PR #240 is clean and mergeable. Workspace PR #40 and app PR
#210 also have green required checks. The full local engineering-efficiency
preflight passed in 287.010 seconds; this is one candidate measurement, not a
hosted speedup claim.

After installing the locked app dependencies in the isolated lane, the complete
`qa:polish:test` target passed, including the existing suite and the new focused
tests. On October 1, `make verify-changed` passed against workspace base
`4febe0d`, backend base `bd1a683`, and app base `e7bdc66`: app fast checks,
selected merge tests and workspace links/spine/canon checks all passed. The
first sandboxed attempt could not write the ignored Expo lint cache and exposed
one stale retry-count contract expectation. The rerun used only the lane's
ignored cache write access, and the corrected contract now passes.

Package 1's implementation is in app [PR #209](https://github.com/fy538/travel-app/pull/209).
Package 2's targeted-capture isolation, exact-input judgment carry, and
proportional review guidance are implemented in that PR. Workspace tracking is
in [PR #39](https://github.com/fy538/travel-workspace/pull/39), and backend
selector transparency is in [PR #239](https://github.com/fy538/travel-agent/pull/239).

The earlier coordinated `make verify-changed` passed for workspace base
`4febe0d461a62d204ba4dee9eaad7813c7c1509c`, backend base
`bd1a683b8656c3f4091e16abb64f57897fa7fc42`, and app base
`e7bdc660501eaa19234e6b45bda033658edaa2d4`. App fast checks passed; the full
app suite passed (1,289 suites, 9,178 tests, one snapshot). Backend static
checks passed; the offline suite passed (22,084 passed, 14 skipped, 1 expected
failure, 52 expected passes). Workspace tests passed (119), followed by contract
and documentation checks. The first publisher attempts exposed a missing
lane-local Python 3.13 dependency environment; installing the committed
`requirements-dev.txt` in `.venv` allowed the final coordinated run to pass. A
fresh rebase onto the merged PR #38 base also passed the local coordinated
preflight; its hosted rerun is pending publication.

**Post-rebase PR #39 preflight (October 1).** The measured command
`make verify-changed WORKSPACE_BASE_REF=bc69d6d03eeb069eb8705953463b4ddc8a808e6 AGENT_BASE_REF=bd1a683b8656c3f4091e16abb64f57897fa7fc42 APP_BASE_REF=e7bdc660501eaa19234e6b45bda033658edaa2d4`
passed in 415.124 seconds on workspace `b0a50dc3197c7fc49a9768ba93aef68532615549`,
backend `2c115ac72edcd490c7cc6a80b8f0a480baf73cdc`, and app
`49e8379047176100ff13d8b1245b7abd06d97a65`, all clean. Jest passed 1,289
suites, 9,178 tests and one snapshot; one worker required forced exit. Backend
passed 22,086 tests with 14 skipped, 53 expected passes and one warning.
Workspace tests passed 142 cases; contract and documentation checks passed.
The log is
`/private/tmp/vesper-pr39-post-rebase-logs/native-qa-pr39-post-rebase-20261001T165646Z.log`.
The local offline run does not replace hosted disposable-database checks.

Package 1 has **one passing targeted native capture** on the assigned simulator;
the wider setup-failure matrix and other surfaces are outside this capture.
Package 2 is **implementation in PR, acceptance in progress**. The observed
shared-reader large-text defect was found in the trace
and fixed in `travel-app` commit `c704fc997`. The committed verdict
`20260930T222931Z` records four passing largest-text/source-return assertions
against app revision `05d81a9df`, an ancestor of this lane head; the reader code
has not changed since that capture. The referenced PNG files are not tracked in
Git, so this is a carried verdict rather than a fresh pixel review. The
Home/Places wrong-state replay remains unverified; the initial wrong-shell
attempt never reached the intended Home state and is not evidence for that
defect. The later successful capture validates one Home presentation only.

The October 1 task-context pass shortened four app/backend owner and intake
documents while retaining the workspace guidance as the single cross-repository
owner. Across the five instruction docs considered, the current word count is
4,641 versus 5,043 at this lane's base (402 fewer, 8.0%). Routing exercises
followed a bounded Home returned-state copy/layout change from the app owner
instructions through the local-change evidence row to the
[Home Root contract](../../travel-app/docs/surfaces/home-root/contract.md)
and `polish/home-root-returned` flow; no full-surface recapture is implied. The
shared artifact-reader typography fix (`c704fc997`) routes through the shared
reader/accessibility evidence row, its
[contract](../../travel-app/docs/surfaces/canonical-artifact-reader/contract.md),
representative family tests, and the registered large-text capture set. An
Intake correction or audience change routes through the
[contribution-and-consequence contract](../systems/contribution-and-consequence.md),
backend risk label, and [Inbound owner feature](../../travel-agent/backend/inbound/FEATURE.md),
with negative/readback integration evidence at that boundary and screenshots
only if presentation changes. These are task-routing checks against real
contracts and changes, not elapsed-time measurements.
Package 2 remains in progress: its Home/Places wrong-state replay is unverified.
The fresh native evidence now covers one Home return-state flow only.

Package 5's P03-03 grader now requires the exact
`trip_photo:private-late-set-photo` evidence reference and matching non-empty
before/after source revisions. Missing, malformed, or changed revision evidence
fails closed. Backend commit `681c518c8` adds this check and valid, missing,
malformed, and changed-revision cases. The measured focused command
`PYTHONDONTWRITEBYTECODE=1 ./.venv/bin/python -m pytest -p no:cacheprovider
tests/eval/test_product_proof_eval.py tests/eval/test_consequence_authority.py
tests/atlas/test_artifact_quality_eval.py -q` passed **38 tests** on Python
3.13.0 in 4.269 seconds; the recorder ran on host Python 3.14.6. This is a
single harness measurement, not a productivity comparison. Ruff check and format
check passed. The grader still consumes adapter-supplied trace fields; the tests
do not prove that a live adapter reads the canonical source owner or that an
original's content stayed unchanged.

**Package 3 — iteration and candidate selection:** selector transparency passed
the coordinated gate above. App plans expose full-suite reasons and print
related test paths before running Jest; backend plans expose selected test
directories and broad-fallback reasons. Workspace, app and backend routing tests
passed (12, 7 and 15 tests respectively), including cumulative shared-change
coverage after a later local edit. No latency improvement is claimed.

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

The current order is consolidated in [section 5](#5-improvement-roadmap).
Retain these acceptance refinements within those packages:

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

The developer or agent should make one short acceptance statement naming the
expected outcome and the cheapest evidence that can detect its failure, implement,
get focused feedback, inspect the affected native behavior when relevant, then
run the final candidate's required checks. Select screenshot scope before starting
a capture environment. Most changes should not require a new planning document
or a complete persona-by-persona critique.

| Change | During iteration | Acceptance before landing |
| --- | --- | --- |
| Prose or backend logic with no visible impact | Documentation checks or focused behavioral tests. | Applicable change-aware gates; no screenshot requirement introduced merely because code changed. |
| Local copy/layout or visible state presentation | Focused component tests where behavior changes, plus the affected native state. | Targeted visual receipt; include long/empty/error content and large text only where they add relevant coverage. |
| Shared reader or visual design component | Representative consumers and relevant interaction tests. | A bounded family-level visual sample covering affected layouts and relevant small-screen/large-text risks; avoid every combination of every state. |
| Navigation, gestures or timing | Execute the action and assert the expected transition or resulting state. | Actual native interaction evidence; recording/performance evidence when timing matters. Screenshots supplement visible-state checks and do not establish motion or responsiveness alone. |
| API, storage, audience or authority | Owning integration/negative tests and generated-contract checks. | Applicable database/cross-repo proof and receiving behavior; add visual evidence when presentation is affected. A saved/shared label is not proof of persistence or authorized access. |
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

### Screenshot purpose and selection

Every required screenshot should answer a concrete visual question, such as
whether a reader title is clipped, an action is obscured or the hierarchy remains
usable with large text. Record that question in the existing acceptance statement
or expected checks; do not introduce another form or registry. Capture alone is
not a passing test. Compare against reviewed intent or an appropriate baseline,
and distinguish an intended difference from a regression.

Google's [screenshot testing guidance](https://developer.android.com/training/testing/ui-tests/screenshot)
recommends minimizing captures while retaining distinct regression coverage,
especially avoiding redundant combinations of themes, font sizes and screens.
That guidance is for Android; our application is the selection principle, not a
proposal to adopt Compose tooling in the Expo app. Prefer an existing isolated
native fixture for a rendering question and a real journey for an integration
question. Keep device, font scale, fixture and build identity known.

For example, a Keep test should perform the action, reopen or reload the record
and verify the same original at the owning persistence boundary. A screenshot
can separately establish that its title and source action render correctly.
Audience restrictions need server-side denial tests. Accessibility semantics and
focus order need accessibility/interaction checks. Screenshots can support these
investigations without replacing their acceptance evidence.

AI review remains assistance with a stated visual question. Maestro's
[AI assertion documentation](https://docs.maestro.dev/reference/commands-available/assertwithai)
describes experimental visual judging that is nonblocking by default because
responses can be unstable; this is a tool limitation, not a measurement of our
current judge. Preserve deterministic assertions for known outcomes and calibrate
visual review on known defects and clean cases. Retain failure captures when they
help diagnosis; diagnostic capture does not imply a new baseline or approval gate.

## 5. Improvement roadmap

**Delivery owner:** Eng Efficiency, working within the mobile, backend and
workspace ownership boundaries. This section is the single implementation queue
for this lane; package numbers remain stable references rather than execution
order. The research sections explain the evidence, not additional queues.

**Current state:** the dated implementation and failure receipts below remain
historical evidence. Packages 3A/3B/3C and targeted native-QA tooling have landed
in the accepted tuple above. Existing gains have their stated sample limits;
there is no measured overall engineering productivity gain. Central integration
owns compatible handoff review, shared conflicts, dependency pins and landing;
Eng Efficiency owns its implementations, focused evidence and adoption receipts.
Do not start a new integration or cleanup queue alongside this section.

| Order | Work | Status and dependency | First beneficiaries |
| --- | --- | --- | --- |
| 1 | Package 3A/3B/3C: reduce measured feedback and integration cost | The isolated advisory workflow, unrelated-label guard and early preflight checks are merged. PR #54 is the first natural eligible post-isolation sample (`n=1`); required checks remain authoritative. Keep the pilot advisory and continue the natural ten-change sample before any wider adoption or claim of savings. | All integrations |
| 2 — independently when needed | Package 1: reliable targeted native QA | One targeted Home capture passed; broader Home/Places wrong-state replay remains open. Prioritize a specific native blocker for the current Artifact/Orchestration assignments when the assigned device is available. | Orchestration and Artifact |
| 3 | Package 2: proportionate review and shorter task context | Tooling landed; changed review scope still requires clean cases and known-defect detection, including the unresolved replay. | All lanes, especially mobile work |
| As encountered | Package 6: reconcile obsolete operating assumptions and active documentation | The central four-roadmap reconciliation resolves stale integration ownership, baselines and producer availability. Fix remaining contradictions in affected owners; do not repeat a global inventory or archive pass without an observed navigation cost. Three earlier archive migrations are complete. | All lanes |
| Conditional | Package 7: retire one verified obsolete code, API or dependency family | Select a family with demonstrated repeated tracing/rework cost, current replacement and no unresolved consumer. The 62 retiring API operations are candidates, not approved deletions. | Lanes repeatedly touching compatibility paths |
| Conditional | Package 4: build reuse and measured setup optimizations | Existing checkout improvements are landed with limited before/after evidence. Native reuse requires a measured remaining setup bottleneck and safe environment identity. | Mobile and build owners |
| Ongoing | Package 5: product-outcome acceptance | Remains with product lanes. Cleanup preserves their infrastructure, authority and acceptance requirements while design continues. | Product users |

**Observed completion checkpoint — October 2:** the unrelated-label
cancellation repair landed in
[workspace PR #51](https://github.com/fy538/travel-workspace/pull/51), merge
`a483be795b6b32b0b2778be6dea64b50fda46e09`. At head `ced324fd`, pilot run
[36973924420](https://github.com/fy538/travel-workspace/actions/runs/36973924420)
was active from 06:31:05Z to 06:31:33Z. The unrelated `documentation` label
arrived at 06:31:10Z and its pilot job skipped in
[run 36973934794](https://github.com/fy538/travel-workspace/actions/runs/36973934794);
the active pilot completed successfully. The opened Reliability
[36973727972](https://github.com/fy538/travel-workspace/actions/runs/36973727972)
and Merge ready
[36973728084](https://github.com/fy538/travel-workspace/actions/runs/36973728084)
checks remained intact and passed. An earlier successful run, 36973749570,
was not observed during execution; the later overlapping event supplies the
race evidence. The downloaded plan was `scope=full`, `eligible=false`; its
synthetic tested workspace was `d8a5826d4a08d3702f9284dbc2f4414e5932b528`,
backend `355a8c11d`, app `acf5bd837`. Central local preflight passed 176
workspace tooling tests plus selected contracts in 45.422s.

The post-merge PR #53 event check and its limit are recorded below. PR #49's
synchronize event and PR #46's cancelled required attempt plus explicit rerun
remain in their dated receipts. The first natural eligible post-isolation
sample now exists in PR #54 (`n=1`); its timing and candidate tuple are recorded
below. These separate cases establish the bounded repair and its failure
handling, not an overall engineering speedup.

The bounded app-blocker recheck confirmed `node-forge@1.4.0` also lies on the
production dependency path `expo-updates@55.0.30` →
`@expo/code-signing-certificates@0.0.6` → `node-forge`. The actual audit uses
`npm audit --omit=dev`; this is not a dev-only classification. The
[reviewed advisory](https://github.com/advisories/GHSA-86w9-cpqp-85rv) still
lists no patched version, and
[upstream PR #1152](https://github.com/digitalbazaar/forge/pull/1152) remains
unreleased. No supported compatible released remedy was found in this bounded
pass. Keep app #213/#214 blocked; no override, crypto fork or audit exception
was applied. Do not repeat open-ended upstream polling. Remaining event/scope
adoption evidence should accompany natural work, while central lands the
independent completed backend handoffs.

**Early governance preflight handoff — October 2:** the next concrete integration
failure was a missing mobile feature-flag registration followed by stale generated
Current State. Both escaped the selected local preflight and surfaced during
publication of the Artifact reader. Eng Efficiency commits `8a55cac9` and
`cb3378f6` now select the existing registry and generated-state gates from their
actual inputs, run them before broader suites, and declare their Python dependency.
Ordinary app component edits do not select flag discovery. Checker startup failure
remains an error, while later selected checks still run; required hosted checks
are unchanged.

The focused clean/violating/tool-failure and ordering cases pass 29/29. The owner's
first full run had a missing Python dependency and four denied loopback binds;
the dependency-correct run retained those four runtime failures with 181 passes.
Central verification of clean `cb3378f65377157050d66a222c381f08ea6c8cc0`, backend
`eda35d6de90ac8c4056dec93630206a2cb6ffa96`, app
`acf5bd837fe3725b00d9744727f513a601fb2498` passed all 186 tooling tests, contracts
and docs checks in 41.824s with approved local socket access, Python 3.13.0,
Node 24.13.0 and matching locked dependencies. No tests were skipped. The exact
explicit-base command and original failed attempts remain in
`docs/reliability/test-loop-baseline.json`. Protected workspace
[PR #53](https://github.com/fy538/travel-workspace/pull/53) merged normally at
`799cf00a9a36954b6a486ed7d95b86d0d5958402`. Full Reliability
`36981170634`, all four syntax shards and Merge readiness `36981170641`
passed; configured Cloud smoke was skipped because the service is unavailable.
The one already-started additional label sequence on this ordinary mixed change
also passed (`36981553687`) with the unrelated-label run skipped (`36981600793`),
leaving the original Reliability run intact. Its plan remained `eligible=false`,
`scope=full`; it adds no naturally eligible sample. No extra events were run. It establishes earlier defect feedback,
not a measured overall speedup. Further advisory event and natural-change samples
belong with ordinary eligible work; do not generate commits just to exercise CI.

**Current bounded follow-on — October 2:** Connectivity's assigned-device
capture now has a concrete Package 1 setup blocker: two attempts at
`polish/life-intake-source-continuity` stop at the Expo developer-menu/tutorial
overlay before app readiness, with 0/1 captured. Diagnose the existing
runner/launch configuration and repair only the reproduced cause. Connectivity
retains exclusive QA SE control; Eng Efficiency supplies the setup diagnosis or
isolated tooling candidate, and coordinates a concrete execution instruction.
Acceptance requires the intended readiness/native case to work and an incorrect
product state to remain rejected, with exact environment, focused evidence and
a clean committed handoff. A concrete external blocker is a valid stop. No
weakened assertions, broader native portfolio, repeated pilot events, security
exception or open-ended retry loop is included.

**Package 1 correction handoff — October 2, 12:44 UTC:** the specific Expo
tutorial guard is committed at Eng `89f7bae1d`, Connectivity `3b97eb5b3` and
central app `a20195808`. It conditionally closes only the observed tutorial,
asserts that overlay is gone, and retains the exact seeded mock/persona/clock
readiness checks. Central final-head explicit-base preflight passed 9,276 app
tests, lint/types and contracts in 102.743s; four focused readiness tests and
the pinned changed-flow parser passed. The earlier broad preflight on Eng
`26dd6102d` and interrupted all-flow syntax sweep remain separate receipts.
Connectivity's device trial was blocked by the locked Mac before execution:
tutorial-present, tutorial-absent and genuine wrong-state rejection are unrun,
not passed. Eng's implementation handoff is complete; Connectivity resumes the
bounded native cases when local access is available. No further headless replay
can close this boundary. Required app Security remains unresolved independently.

**Current evidence and follow-up — October 2: measure the advisory pilot.**
The shared security blocker review, workflow repair and first post-isolation
natural sample are complete. PR #46's cancelled duplicate had to be rerun
despite a passing same-head attempt; its three attempts consumed 53m16s of
Reliability job occupancy for one change. Preserve that cost and the required
full gate when comparing later observations.

1. **Shared app blocker — bounded review complete.** The app PRs #213/#214
   still fail only their required `Security audit`. The reviewed
   [node-forge advisory](https://github.com/advisories/GHSA-86w9-cpqp-85rv)
   has no supported patched release as of October 2. No override, crypto fork
   or audit exception was applied. Recheck only after a compatible Expo or
   `node-forge` release changes the locked dependency chain.
2. **Workflow repair — merged and hosted.** PR #49 isolated the advisory pilot;
   PR #51 separated unrelated-label events; PR #53 moved flag and generated-
   state checks earlier in preflight. Hosted opened, opt-in-label and unrelated-
   label outcomes are recorded above. PR #51 includes an unrelated label during
   the pilot's active interval; PR #53 later reconfirmed skip behavior after its
   pilot had completed. PR #49's synchronize run and PR #46's cancelled required
   attempt plus explicit rerun remain separate evidence. All required checks
   remain unchanged and authoritative.
3. **Natural eligible change — first sample recorded, `n=1`.** PR #54's
   advisory run took 1m42s from creation; its required gate took 5m49s, and its
   recorded PR checks used 24m42s of runner occupancy. The pilot result came
   2m55s before the final required check, but the PR merged 37s after that
   check. Before isolation, PR #46's first eligible
   attempt produced a signal in 1m42s and completed the required gate in 6m54s,
   with 27m57s of Reliability runner occupancy. Its later cancellation and
   retry brought all-attempt Reliability occupancy to 53m16s. After isolation,
   PR #54 produced the signal in 1m42s, completed the required gate in 5m49s,
   and used 22m32s of Reliability occupancy (24m42s across its recorded PR
   checks). These are distinct candidates, not a controlled comparison; do not
   attribute their differences to the workflow change. PR #54 merged 37s after
   its required gate, and there is no comparable pre-change measurement that
   isolates check-to-merge latency. Continue collecting only naturally
   occurring candidates and preserve each run, attempt, rejection, failure and
   cancellation. Do not manufacture another prose PR or change required-check
   policy to increase the sample.

**Finish:** retain the pilot as advisory while the natural sample is small.
The current evidence shows an earlier scope signal on one post-isolation
candidate, confirms that required checks remained authoritative, and does not
establish lower merge latency, lower runner occupancy or an overall productivity
gain. Reassess wider adoption only after the prospective sample supports it.
No default narrow required scope, protection change or security waiver is
included. The ten-change sample uses real work rather than fabricated prose
commits. Central integration remains the landing owner; this task does not
become an indefinite cross-lane watcher.

**Independent follow-on:** if a current lane is blocked by native QA setup,
fix one reproduced cause under Package 1 and show both its recovered intended
case and a real product failure still failing. Otherwise hand off the completed
workflow milestone. Broader cleanup, semantic visual approval and app sharding
remain conditional on their existing evidence gates.

**Previous assignment and baseline rationale:** the roadmap-prose selector is
already implemented. The following original baseline and pilot protocol remain
historical comparison evidence; current execution order is the October 2
assignment above. Packages 3A/3B/3C are not instructions to replay landed work.

**Observed baseline, October 1:** both PRs below changed only working-roadmap
Markdown, with unchanged backend `0a1fdf224aaf59ca713eec5eba79a34321f038a9`
and app `acf5bd837fe3725b00d9744727f513a601fb2498`. Times use GitHub UTC
timestamps; workflow duration is creation to final update, not human time lost.

| Prose-only candidate | Reliability workflow window | Workspace job | Total job occupancy | Selected repeated steps |
| --- | --- | --- | --- |
| PR #42, `b03c08dd87ad0b2127d3e309962abe5291c05e66`; [run 36940383017](https://github.com/fy538/travel-workspace/actions/runs/36940383017) | 23:21:40–23:27:15, 5m35s | 5m09s | 22m58s across six jobs | Backend install 51s, frontend install 23s, journey mocks 64s, database migration 4s, goldens 25s; all four syntax shards also ran |
| PR #43, `ef8abf84009a0ba40ff35e8d1578f1549984b251`; [run 36942761248](https://github.com/fy538/travel-workspace/actions/runs/36942761248) | 23:48:40–23:54:01, 5m21s | 4m55s | 24m37s across six jobs | Backend install 47s, frontend install 21s, journey mocks 63s, database migration 4s, goldens 24s; all four syntax shards also ran |

GitHub reported zero billable minutes for both runs because this is a public
repository; job occupancy is a separate resource measure. The earlier window (#35–#44) matched three of ten merged PRs (#42–#44).
At 2026-10-02 04:29:59Z, the ten most recently merged workspace PRs were
#39–#48. Four matched the path-and-body-only shape: [#42](https://github.com/fy538/travel-workspace/pull/42),
[#43](https://github.com/fy538/travel-workspace/pull/43), [#44](https://github.com/fy538/travel-workspace/pull/44),
and [#46](https://github.com/fy538/travel-workspace/pull/46). The three
earlier matches predate the classifier; #46 is the only classifier-era
candidate. This 4/10 retrospective rate is clustered around roadmap and
integration work, not a representative frequency estimate. There were no
open workspace PRs at that audit time, so the prospective classifier sample
remained n=1. Continue with ordinary workspace changes; do not create a PR
solely to grow the sample.

Trial only an explicit narrow set of working-roadmap prose inputs, preserving
their metadata, link, governance and referenced-checker obligations. Require the
unchanged immutable child tuple and a known successful integration baseline.
Contract, policy, pin, workflow, checker, source and unknown changes take the
full path; unavailable history or verification identity must not yield a narrow
pass. Keep the required aggregate always reported and fail closed on missing,
failed or cancelled required work. Follow the existing staged
[CI Plan](../reliability/CI%20Plan.md): demonstrate valid, violating, tool-error
and cancellation cases plus exact hosted candidate behavior before adopting a
new scope. Keep full integration diagnostics on the appropriate code changes
and main/nightly/manual paths. This roadmap changes no workflow, protection
setting or required-check obligation.

**October 1 implementation candidate:** the opt-in `roadmap-scope-pilot` job in
the workspace Reliability workflow admits only body edits to the four documents
listed above. It checks exact current-main and immutable child identities,
requires clean child checkouts and unchanged lifecycle metadata, and reuses the
existing documentation selector and referenced-checker tests alongside the
governance, inventory, generated-status and child-document checks. Missing or
uncertain evidence falls back to full scope. The pilot job is label-gated and
is not a dependency of `Contract and golden paths`; the required full workspace
suite and all four Maestro syntax shards remain unchanged and authoritative.

This candidate cannot yet reduce the required end-to-end wait or runner use:
the full required gate still runs during the trial, and the optional job adds
runner work when explicitly enabled. An eligible roadmap-only PR must carry the
`roadmap-scope-pilot` label to produce the plan artifact and hosted timing. Keep
the artifact, full-gate result, total workflow time and runner minutes together;
record a rejection, checker failure or cancelled run as such. This is evidence
for reviewing whether a later additive-to-required cutover is justified, not an
adoption or speedup claim. Any protection or required-check change remains a
separate, authorized rollout decision.

**Local validation boundary, October 1 EDT / October 2 UTC:** the classifier and
aggregate contracts passed 53 tests in 32.005 seconds. Documentation inventory,
status, child governance, links, spine and canon checks passed; the new-document
guard found zero new documents. The final
`make verify-changed` passed in 66.377 seconds on workspace
`93301ec311b32ef72a39d090b59819b9ad12c589`, backend
`0a1fdf224aaf59ca713eec5eba79a34321f038a9`, and app
`acf5bd837fe3725b00d9744727f513a601fb2498`. It passed 173 workspace tooling
tests, cross-repository contract/API/compatibility checks, and links/spine/canon
checks; backend and app product suites were not selected for this workspace
change. The exact commands, environment, timings and logs are recorded in the
[verification baseline](../reliability/test-loop-baseline.json).

**Hosted scope-rejection trial, October 2 UTC:** [PR #45](https://github.com/fy538/travel-workspace/pull/45)
published the workflow and classifier candidate at head
`eac09fb6405c67efd4daf8ee7b9ccde32130b63d`, against base
`93301ec311b32ef72a39d090b59819b9ad12c589`; it merged as
`f8ae68e075a634bc75f97fe3839013f4bcfc44ec`. The label-triggered
[plan artifact](https://github.com/fy538/travel-workspace/actions/runs/36957506694)
reported `eligible: false`, `scope: full`, reason “Only modifications to
existing roadmap files are eligible,” and selected no narrow commands. Its
changed-path inventory included the workflow, classifier, tests, runbook and
measurement receipt. The accompanying candidate-tuple artifact recorded tested
workspace merge SHA `0136f969ad19dec9d4ecf85c4a762b5a90d7353c`, backend
`0a1fdf224aaf59ca713eec5eba79a34321f038a9`, and app
`acf5bd837fe3725b00d9744727f513a601fb2498`; tested and candidate revisions
matched.

Adding the label cancelled the first Reliability run
([36957506676](https://github.com/fy538/travel-workspace/actions/runs/36957506676))
12 seconds after creation. Its required aggregate failed after 7 seconds because
the required dependencies were cancelled. The replacement
([36957506694](https://github.com/fy538/travel-workspace/actions/runs/36957506694))
completed successfully: the advisory job took 25 seconds, `Reliability checks`
took 5m48s, the four Maestro syntax shards took 4m01s, 4m41s, 4m48s and 5m26s,
and `Contract and golden paths` passed at 02:57:03Z, 6m10s after run creation.
Its completed jobs used 25m14s of runner occupancy; the cancelled run added
13 seconds, for 25m27s across both runs. The run API reported creation and start
at the same time, while the first job started 13 seconds later. Backend
dependency installation took 63 seconds, Node setup 8 seconds, frontend
dependency installation 26 seconds, Journey mock-walk 72 seconds and Golden
path QA 28 seconds. GitHub reported no billable minutes for this public
repository. The additive `Merge ready` check passed in 2m55s; Maestro Cloud PR
smoke was skipped.

This hosted case confirms full-scope rejection, tuple matching, visible
cancellation failure and a successful full required gate. It is not an eligible
prose-only run and gives no evidence that the narrow checks are sufficient or
faster. The subsequent evidence update supplied the positive case below.

**Hosted positive-selection receipt, October 2 UTC:**
[PR #46](https://github.com/fy538/travel-workspace/pull/46) changed only this
roadmap's body prose at head `fc5ba8154465f72c5285744ccc8b4a0d939a7e90`,
base `f8ae68e075a634bc75f97fe3839013f4bcfc44ec`, and the unchanged child pair
above. Both successful attempts produced `eligible=true`,
`scope=working-roadmap-prose`, and plan SHA-256
`fd8326fa451a9546301c97222bbf8a41a46ce2e4f57d828f7646b70487e18b0a`.
Their tuple artifacts matched hosted workspace merge candidate
`788456a3b1f595b4f8762077ec1019e4ebf9068a` and both pinned children.

The selected commands were the new-document guard at the explicit base;
`make docs-inventory-check docs-status-check docs-child-governance-check`;
`make docs-links-check docs-spine-check docs-canon-check`; and
`python3 -m pytest scripts/tests/test_preserved_doc_governance.py`, selected for
a checker referenced by this document. The first advisory job took **1m42s**:
about 23s from job start through planning, 66s installing backend development
dependencies, 10s executing selected checks, and the remaining upload/cleanup.
The run API reported zero creation-to-start queue time; its first job began
13s after creation. These are GitHub API job/step windows, not developer effort.

| Reliability run / attempt | Outcome | Advisory job | Required aggregate completion from attempt creation | Completed-job runner occupancy |
| --- | --- | --- | --- | --- |
| [36958809900 / 1](https://github.com/fy538/travel-workspace/actions/runs/36958809900) | Full and narrow paths passed | 1m42s | 6m54s | 27m57s |
| [36958809950 / 1](https://github.com/fy538/travel-workspace/actions/runs/36958809950/attempts/1) | Cancelled; aggregate failed on cancelled dependencies | Cancelled before execution | Failed at 10s | 10s |
| [36958809950 / 2](https://github.com/fy538/travel-workspace/actions/runs/36958809950/attempts/2) | Full and narrow paths passed after explicit rerun | 1m39s | 5m42s | 25m09s |

GitHub initially refused an ordinary merge despite the successful first run;
the cancelled duplicate retained a failed required result. Auto-merge was also
unavailable because the repository disables it. Rerunning the cancelled
workflow on the same commit cleared the policy blocker without an admin bypass
or protection change. The retry API's start timestamp precedes its creation
timestamp by one second; its required gate finished 5m43s after that start.
Do not interpret that timestamp discrepancy as negative queue time. PR #46
merged at 03:23:56Z as `ceb040abd16750b0b014b7e1929b83f54a3c7964`.

Across both run IDs and all three attempts, Reliability used **53m16s** of
runner occupancy. The separate `Merge ready` job added 27s and the cloud
configuration check 2s; Maestro Cloud PR smoke remained skipped. Both plan
artifacts and their tuple records are retained under their respective runs;
all required Reliability jobs remained active. The original positive run's full
required completion was 6m54s, and first PR-run creation to merge was 15m46s,
including diagnosis and the retry. The advisory result arrived earlier for
this one input, but required merge time did not shrink and the duplicate/run
retry defeats any runner-cost saving claim. Two attempts of one change are
still **n=1** for change frequency and acceptance. Recommendation after the first hosted trial: revise the demonstrated
label-trigger cancellation behavior by running the optional pilot in its
own workflow and concurrency group. Keep all required checks unchanged and
do not adopt the exception as a replacement yet. The eligible result arrived
in 1m42s versus 6m54s for the required aggregate, a potential 5m12s earlier
signal on one change, but it did not reduce merge wait. All attempts used
53m16s of Reliability runner occupancy. The 4/10 retrospective shape count
is clustered, and the prospective classifier sample remains n=1. The
classifier, its regression suite and CI wiring have real maintenance cost;
maintenance hours have not been measured. The demonstrated cancellation
defect is fixed and its post-fix rejection case passed, but the isolated
workflow has not yet had a natural eligible prose candidate. Keep the full
required checks authoritative and the pilot advisory until that candidate
and the prospective ten-change sample provide evidence for a separate
rollout review.

### Hosted trigger isolation recheck, October 2 UTC

[PR #49](https://github.com/fy538/travel-workspace/pull/49), head
`64af4b3ae8a265e08228edf999916899bbd4d7ca`, changed the required workflow's
label trigger and moved the advisory pilot into its own workflow and
concurrency group. The opened event ran the full required set: [Reliability
run 36967417902](https://github.com/fy538/travel-workspace/actions/runs/36967417902),
[Merge ready run 36967417922](https://github.com/fy538/travel-workspace/actions/runs/36967417922),
and the [Maestro Cloud PR gate](https://github.com/fy538/travel-workspace/actions/runs/36967417900).
All four syntax shards, `Reliability checks`, `Contract and golden paths`
and `Merge ready` passed. The full required aggregate finished at 05:12:59Z,
7m05s after the Reliability workflow was created at 05:05:54Z. Maestro Cloud
smoke was skipped by its existing configuration gate. The separate pilot
workflow's opened-event job was skipped because the opt-in label was absent.

After the required aggregate finished, adding `roadmap-scope-pilot` produced
[pilot run 36967975701](https://github.com/fy538/travel-workspace/actions/runs/36967975701),
which completed successfully in 27s. Its uploaded plan had SHA-256
`7ac9cbe6e2560968de73091d5e26e6255f6aaae30ba63f20d9f369823ad92f46`,
`eligible: false`, `scope: full`, reason “Only modifications to existing
roadmap files are eligible,” and no narrow commands. The candidate-tuple
artifact recorded workspace merge candidate
`1ba1d0eaafcf04476da82931e07b6dd4abbf346c`, backend
`355a8c11df54fee27f8de3b86196b606a64a071c`, and app
`acf5bd837fe3725b00d9744727f513a601fb2498`; tested and candidate child
revisions matched. The label event started no new Reliability or Maestro
workflow, and the original required checks stayed green.

PR #49's next commit, `c16871daebb39d353bb8f55cbe280e3c76f11e5a`, was
committed at 05:18:14Z and received new pull-request runs at 05:18:26Z:
[Reliability 36968341906](https://github.com/fy538/travel-workspace/actions/runs/36968341906),
[Merge ready 36968341851](https://github.com/fy538/travel-workspace/actions/runs/36968341851),
and [pilot 36968341865](https://github.com/fy538/travel-workspace/actions/runs/36968341865).
All required Reliability jobs, all four syntax shards, `Contract and golden
paths`, and Merge ready passed on that exact head. The final required gate
completed at 05:24:02Z, 5m36s after run creation; the pilot job completed in
30s. Its uploaded plan SHA-256 was
`7ac9cbe6e2560968de73091d5e26e6255f6aaae30ba63f20d9f369823ad92f46` and
conservatively reported `eligible: false`, `scope: full`, with no commands.
The candidate and tested tuple matched at workspace
`ac697020d6c13981ff60459006e3ed49c6f278be`, backend
`355a8c11df54fee27f8de3b86196b606a64a071c`, and app
`acf5bd837fe3725b00d9744727f513a601fb2498`. Maestro Cloud configuration
passed and its PR smoke remained skipped by the existing configuration gate.
This proves the newer commit received its own full required gate; it is not an
additional natural eligible sample.

The Reliability run's six completed jobs used 25m29s of runner occupancy;
`Merge ready` used 3m16s, the cloud configuration check used 4s, and the
label-triggered pilot used 27s. The label run came after full verification, so
this rejection case offers no merge-wait or runner saving estimate. The
positive classifier result in PR #46 predates the split; post-isolation
eligible hosted sample size remains zero. Do not count repeated runs of this
same implementation PR as additional natural candidates.

Compare elapsed feedback time and runner use with equivalent prose changes,
and record how frequently that class occurs in the existing ten-change pilot.
Two docs-only samples do not establish the dominant cost of ordinary product
development. If the scope cannot be classified safely or its frequency does
not justify implementation/maintenance cost, retain the full path and select
the next evidenced bottleneck. Do not build a general result-cache platform
for this slice. Hand over the bounded implementation and evidence, or the
specific rejected hypothesis, before expanding the assignment.

### Unrelated-label cancellation guard candidate, October 2 UTC

The follow-up candidate in branch `codex/pilot-label-event-guard-20261002`
keeps `opened`, `synchronize` and `reopened` events plus the exact opt-in label
event in one per-PR concurrency group. Other `labeled` events get a separate
group keyed by the unrelated label name, and the job condition permits a
labeled event only when that event adds `roadmap-scope-pilot`. This prevents an
unrelated label from colliding with an active pilot even if GitHub reserves
workflow concurrency before evaluating the job condition. The full required
Reliability workflow remains separate and unchanged.

`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider
scripts/tests/test_merge_readiness_workflows.py -q` passed 33 tests, and
`make docs-check` passed. The explicit-base
`make verify-changed WORKSPACE_BASE_REF=origin/main
AGENT_BASE_REF=origin/main APP_BASE_REF=origin/main` preflight exited 2 after
171 workspace tests passed and five environment failures: one cross-repository
fixture could not import SQLAlchemy, and four runtime tests could not bind
local sockets in the sandbox. The follow-up contract command also stopped at
the missing SQLAlchemy import. The environment was macOS 25.5 arm64 with
Python 3.14.6; the workspace setup calls for Python 3.13. The measured records
and logs are retained in the [verification baseline](../reliability/test-loop-baseline.json)
and `/private/tmp/vesper-efficiency-lane-20261002/`. The focused test result
does not replace the incomplete merge preflight.

**Central preflight receipt — October 2 UTC:** the current-base integration
with workspace base `e5a929cdec71c74b0b7179bb099b0f47ba373707`, backend
`355a8c11df54fee27f8de3b86196b606a64a071c` and app
`acf5bd837fe3725b00d9744727f513a601fb2498` passed in **45.422s** with
Python 3.13.0, matching dependency locks and authorized local loopback access.
All 176 workspace tooling tests passed, along with the selected cross-repository
contract/API/compatibility and documentation checks. The recorded result
supersedes the earlier missing-dependency/socket-denial blocker for this
integration boundary; it does not establish hosted event behavior.

At the original handoff, no hosted unrelated-label event had exercised the new concurrency key.
The merged guard was later exercised on
[workspace PR #53](https://github.com/fy538/travel-workspace/pull/53): the
opened-event pilot skipped in
[run 36981170611](https://github.com/fy538/travel-workspace/actions/runs/36981170611),
the opt-in label started
[run 36981553687](https://github.com/fy538/travel-workspace/actions/runs/36981553687),
and a later unrelated-label event produced a skipped pilot job in
[run 36981600793](https://github.com/fy538/travel-workspace/actions/runs/36981600793).
The opt-in candidate was rejected conservatively as `eligible: false`,
`scope: full`; it completed in 26s. The unrelated-label event did not start a
second required Reliability or Maestro run. It followed the pilot's completion,
so this PR #53 repeat confirms filtering but does not itself prove overlap
protection. PR #51's unrelated label arrived during the active pilot, as recorded
in the observed completion checkpoint above. PR #53's opened-event required
[Reliability run 36981170634](https://github.com/fy538/travel-workspace/actions/runs/36981170634)
and [Merge ready run 36981170641](https://github.com/fy538/travel-workspace/actions/runs/36981170641)
passed. A failed or cancelled required-check rerun remains a failure and must
stay in the attempt record.

### First eligible post-isolation sample, October 2 UTC

Workspace [PR #54](https://github.com/fy538/travel-workspace/pull/54), head
`76911e8edd575eb12b5430505d770587baf2dc88`, was the first natural candidate
whose only changed files were admitted roadmap body prose with unchanged
lifecycle front matter. The opened-event pilot check skipped in
[run 36983897512](https://github.com/fy538/travel-workspace/actions/runs/36983897512).
Adding `roadmap-scope-pilot` started
[run 36984013226](https://github.com/fy538/travel-workspace/actions/runs/36984013226),
attempt 1, which passed with
`eligible: true`, `scope: working-roadmap-prose` and reason “only admitted
roadmap prose changed over the current protected-main child tuple.” The uploaded
plan SHA-256 is
`81f8a4c59663b404ac2825be6a778fcdcdaa185cf8e997f3cc080449e47ab451`.
The selected checks were new-document governance, inventory/status/child
policy, documentation links/spine/canon and the preserved-governance regression
test.

The artifact's candidate and tested tuples matched exactly: workspace
`ad3addd9de8308954f94672a54582d547dbb0582`, backend
`0e7048120414c1f18c5a0e39c50c10afc9fc24f7`, app
`acf5bd837fe3725b00d9744727f513a601fb2498`. The Reliability run
[36983897491](https://github.com/fy538/travel-workspace/actions/runs/36983897491)
was created at 08:24:59Z; its final required `Contract and golden paths` check
completed at 08:30:48Z, a 5m49s creation-to-final-check window. All required
Reliability checks and four Maestro syntax shards passed. The separate
[Merge ready run 36983897448](https://github.com/fy538/travel-workspace/actions/runs/36983897448)
passed; Maestro Cloud smoke was skipped by its existing configuration gate.

The pilot run was created at 08:26:12Z, and its job ran from 08:26:15Z to
08:27:53Z: 98s of runner occupancy and 102s from run creation to completion.
Its result preceded the final required check by 2m55s. PR #54 merged at
08:31:25Z, 37s after that final required check, so the earlier advisory signal
did not shorten merge time. The Reliability jobs occupied 22m32s in aggregate;
adding Merge ready (28s), the cloud-configuration check (4s), and the advisory
pilot (98s) gives 24m42s across these completed PR checks. The optional pilot
added runner occupancy while the full gate remained required; this sample shows
no runner saving. It is one accepted eligible candidate (`n=1`), not evidence
for changing branch protection or claiming an overall delivery-speed gain.
Continue the natural ten-change sample and record every attempt; do not create
another PR solely to obtain a positive result.

### Bounded app security blocker review, October 2 UTC

Both [app PR #213](https://github.com/fy538/travel-app/pull/213) and
[#214](https://github.com/fy538/travel-app/pull/214) have a failing required
`Security audit` on [GHSA-86w9-cpqp-85rv](https://github.com/advisories/GHSA-86w9-cpqp-85rv)
(CVE-2026-85393). The app lockfile resolves `node-forge` 1.4.0 through
both `expo@55.0.31` → `@expo/cli@55.0.36` → `node-forge@1.4.0` and
`expo-updates@55.0.30` → `@expo/code-signing-certificates@0.0.6` →
`node-forge@1.4.0`. `npm ls node-forge --omit=dev --all` on app revision
`a2019580869688fb09f9a8012a4c2f129c5f9a18` confirms both paths remain in the
production dependency graph. Vesper does not import `node-forge` directly.

The affected JavaScript call sites are Expo tooling: `@expo/cli` reads
certificates from the local macOS keychain, and `@expo/code-signing-certificates`
parses certificates/CSRs and verifies signatures generated by its signing
helpers. The vulnerable case is narrower than ordinary certificate parsing:
`node-forge` accepts a forged RSA PKCS#1 v1.5 signature when a crafted nested
`DigestAlgorithm` contains extra ASN.1 elements and verification uses a
low-exponent key (the upstream reproduction uses `e=3`). Expo's iOS and Android
update clients implement signature verification natively (Swift and Kotlin),
not through this JavaScript package. The checked-in app config has an OTA URL
and runtime version but no `codeSigningCertificate` or `codeSigningMetadata`;
remote EAS build settings were not inspected. This establishes a production
install-graph finding and Expo tooling exposure, not that `node-forge` is
included in the shipped JavaScript bundle or that a Vesper signed-update key is
currently vulnerable. It also does not make deleting `expo-updates` safe: the
app's OTA update support is configured, and removing Expo's signing tooling
would impair future signed-update setup.

As of the official advisory review on October 1, affected versions are `<=1.4.0`
and there is no patched release. npm's version listing still reports `1.4.0` as
latest. The upstream [proposed fix PR #1152](https://github.com/digitalbazaar/forge/pull/1152)
is still open; it proposes the `1.4.1` fix but is not a released dependency.
Expo's current certificate package still accepts `node-forge@^1.3.3`, so
updating that wrapper alone does not fix the lockfile. A source override,
backport, disabled OTA client or broad audit waiver is not an acceptable
supported remediation for this lane.

The first local `npm audit --omit=dev --json` attempt at candidate app head
`a2019580869688fb09f9a8012a4c2f129c5f9a18` used Node `v24.13.0` and npm
`11.6.2`, but could not reach `registry.npmjs.org` (`getaddrinfo ENOTFOUND`).
That attempt was unverified, not a pass. Central then captured a fresh
production audit with approved registry access at
`/private/tmp/vesper-lane-integration-evidence/current-production-audit.json`:
audit report v2, 20 findings (15 moderate, 5 high, 0 critical). The five high
package rows are the same single `node-forge` source `1240912`, propagated
through `node-forge`, `@expo/code-signing-certificates`, `@expo/cli`,
`expo-updates`, and `expo`; the advisory URL is the exact GHSA above and its
affected range is `<=1.4.0`. No other high advisory was present. The prior
required hosted result and this fresh report agree that the gate blocks the
current app graph. The JSON contains no Git revision, so it proves the reported
dependency graph only; the hosted check for each pinned PR revision remains the
merge evidence.

npm's `fixAvailable` suggestion is `expo-updates@0.11.7` for the code-signing
chain and `expo@44.0.6` for the Expo CLI chain, each marked semver-major. The
affected app uses Expo 55 (`expo@55.0.31`, `expo-updates@55.0.30`); neither
suggestion is a compatible supported repair. The checker must keep malformed
or unavailable audit results as errors. Do not repeat the same registry probe
without changed dependency or advisory evidence.

**Approved decision, October 2:** `fy538` explicitly approved temporary risk
acceptance for one row in `travel-app/scripts/security-audit.mjs`'s existing
`EXCEPTIONS` map, keyed by source `1240912`. Its exact match identity is advisory
URL `https://github.com/advisories/GHSA-86w9-cpqp-85rv`, package `node-forge`,
installed lockfile version `1.4.0`, affected range `<=1.4.0`, and severity `high`.
Owner and expiry/removal owner: `fy538`. It is valid through `2026-10-09` UTC,
and fails closed from 2026-10-10T00:00:00Z. Every identity field and installed
node version must match; a changed range, URL, package or severity stays
blocking. Every other high/critical advisory and malformed or unavailable audit
remains failing; moderate findings retain the existing nonblocking policy.
The map applies to every app audit invocation during this window. This is
bounded risk acceptance for Expo signing tooling pending a supported upstream
fix, not a patched dependency or release/deployment authorization. Central
integration applies the concrete candidate and requires real audit and hosted
checks before landing. Prior failed checks remain historical failures; they
are not retroactively passes. The operational record is in the
[CI Plan](../reliability/CI%20Plan.md#shared-app-security-audit-blocker--october-2-2026).

[DORA's work-visibility guidance](https://dora.dev/capabilities/work-visibility-in-value-stream/)
supports directing improvement at observed constraints in the delivery path.
[SPACE](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/)
warns against treating activity or a single efficiency metric as productivity.
The application here is a measured trial with preserved defect detection, not
a promised productivity percentage or a reason to keep all lanes busy.

**Conditional retirement candidate, not the first assignment:** the nine skipped
Step 7 card-feedback/lifecycle tests in backend
`tests/api/test_concierge_home.py`. The current file separately asserts that
`/cards/feedback`, `/cards/lifecycle` and `/cards/restore` return 404; current
mobile transport has no callers for those retired writes, and the app legacy
boundary test rejects their reintroduction. This supports reviewing the dead
test block, not removing the active concierge feed, current memory correction
or other live Home contracts. Trace each old invariant to its current owner
before retiring its test. Because these tests are already skipped, their
removal cannot be advertised as faster test execution. Choose another family
if this one has no meaningful tracing/maintenance burden. The 62 retiring API
operations still require their own consumer and removal evidence.

Use the existing ten-change measurement pilot for subsequent changes across
the four lanes; a completed comparable pilot has not yet been observed.
Recent interrupted integration turns repeatedly chased moving main revisions
and reran broad gates; central landing and a stable committed handoff address
that mechanism. Compare similar subsequent slices before claiming an overall
speed gain. Required-check waiting, runner cost, retries and acceptance rework
remain separate measurements.

**October 1 Package 4 local preflight receipt.** The corrected checkout scope
passed `make verify-changed` in 320.740 seconds against workspace base
`bc69d6d`, backend base `bd1a683`, and app base `e7bdc66`. The workspace was at
`3d224590` with the corrected workflow and regression test in its working tree;
backend and app were `05dcc914` and `906c5d5`. The run passed all 9,180 app
tests, 22,085 backend tests (14 skipped, 53 xpassed, one warning), 145 workspace
tooling tests, and the selected contract, API and documentation checks. The
[verification baseline](../reliability/test-loop-baseline.json) records the
command, full revisions, environment and log path. The hosted syntax-shard
pilot passed all four exact-checkout assertions and syntax partitions. The
required Reliability workflow continues to own end-to-end validation.

**October 1 implementation receipt (local checks at 08:54 UTC; hosted evidence through 09:15 UTC).**
The coordinated `make verify-changed` passed on workspace `632c8ff`, backend
`2c115ac`, and app `4c5caa9`, against bases `4febe0d`, `bd1a683`, and `e7bdc66`.
The app suite passed (1,289 suites, 9,178 tests, one snapshot); lint reported 167
warnings and no errors. The backend suite passed (22,086 passed, 14 skipped, one
xfail, 52 xpassed, one warning); workspace tests passed (119), and contract,
API and documentation checks passed.

Hosted checks are now established for the four open implementation PRs. PR 38's
required checks pass; its Maestro Cloud smoke is skipped because the service is
not configured. Workspace PR 39's checks pass with the same smoke skip. App PR
209's scope, fast/static, contract and full-test checks all pass. Backend PR
239's checks also pass after one bounded retry of `package-smoke`: the first
Docker build reached its 20-minute job timeout while downloading runtime
dependencies, while the retry built the image and passed the operator-entrypoint
import in 2m05s. Two earlier package-smoke runs took about two minutes. This
sample supports a transient download slowdown, not a timeout or coverage change.
The latest query at 09:15 UTC found PR 38 open and mergeable, with all required
checks passed, `origin/main` at `4febe0d`, and no review decision recorded. The
Maestro Cloud PR smoke remains skipped because the service is not configured.
The second hosted run,
[36839535177](https://github.com/fy538/travel-workspace/actions/runs/36839535177),
passed reliability checks in 4m51s, the four Maestro syntax shards in 4m50s,
4m49s, 5m12s and 5m38s, and the required aggregate in 8s. The resulting
critical path was about 5m46s; summed job runtime was 25m28s. Compared with the
23m18s serial baseline, this second sample shortened the critical path by about
75.2% while using 9.3% more runner time. The first sample shortened it by 73.3%
while using 10.6% more runner time. Both runs preserve the full flow inventory;
these two hosted samples established faster feedback with a modest runner-time
cost, not a stable percentile or a claim of lower resource use. The third run,
[36840575936](https://github.com/fy538/travel-workspace/actions/runs/36840575936),
also passed: reliability took 7m31s, syntax shards took 4m58s, 5m32s, 6m50s and
6m28s, and the aggregate took 7s. Its critical path was about 7m38s and summed
job runtime 31m26s, or 67.2% less critical-path time and 34.9% more runner time
than the serial baseline. All three runs validate the full flow inventory; the
spread shows material hosted variability. At that time Package 3A was gated on
Package 3C landing; PR 38 has since merged as `bc69d6d`.

**Package 3A local receipt (October 1).** The candidate
is based on workspace `b95e2e0040033c2f58f5a60bebc7f1bcf487678e` (merged with
`origin/main` at `bc69d6d`), backend `bd1a683b8656c3f4091e16abb64f57897fa7fc42`,
and app `e7bdc660501eaa19234e6b45bda033658edaa2d4`. Focused Invite and Place
tests passed 34/34; the complete Place-home file passed ten runs at 17/17 each.
The selected app merge path retained 99 suites and 754 tests in both the
two-worker and four-worker trials. Measurement-wrapper wall times were 14.458s
and 14.509s at two workers, and 8.521s and 7.655s at four; the medians were
14.484s and 8.088s. The candidate selector's bounded CPU-derived budget ran the
same selection at 7.959s. These trials ran locally on macOS 25.5/arm64 with
Node 24.13.0, npm 11.6.2 and 14 reported CPUs. The app `node_modules` link
pointed to the active native-QA lane, whose `package-lock.json` had the same
SHA-256 as this lane; hosted Node 20 and runner resource costs remain untested.

The full coverage command
`npm --prefix travel-app test -- --ci --coverage --coverageDirectory=/private/tmp/vesper-eng-eff-measurement/eng-eff-3a-coverage-report --coverageReporters=text --coverageReporters=lcov`
exited 0 after 160.614s and passed 1,289 suites, 9,180 tests and one snapshot;
the report was successfully written outside the shared checkout. Jest still
reported a worker that failed to exit gracefully and was force-exited. Preserve
that cleanup warning as open diagnosis. The earlier attempt that wrote coverage
inside the checkout also passed the tests but emitted an `EPERM` report-write
error; it is not the clean coverage evidence. The 160.614s figure is a local
wall measurement, not a hosted comparison or a speed claim.

The repository preflight then passed on workspace `b95e2e0`, backend
`bd1a683`, and app `e7bdc66`, against workspace base `bc69d6d` and the two
unchanged child bases. `make verify-changed WORKSPACE_BASE_REF=origin/main
AGENT_BASE_REF=origin/main APP_BASE_REF=origin/main` completed in 127.567s;
the change-aware app selector deliberately chose its full fallback because
the selector itself changed. It passed the same 1,289 app suites and 9,180
tests, Expo lint (167 existing warnings, no errors), 557 living-document link
checks, the ten-entry documentation spine, and the canon word budget. The
first preflight attempt exited 2 because the managed worktree denied creation
of Expo's ignored `.expo/cache/eslint`; rerunning with that routine cache
directory writable passed. The measured run used the lane's Python 3.13
environment on macOS 25.5/arm64. Database-backed hosted requirements and the
Node 20 runner remain outside this local result. Measurement record and full
log: `/private/tmp/vesper-eng-eff-measurement/eng-eff-package-3a-verify-changed-cache-write-20261001T140905Z.log`.

Four app/backend instruction documents were shortened and the workspace
cross-repository instructions retained as the single shared owner. Across the
five instruction documents considered, the word count fell from 5,043 to 4,641
(402 fewer, 8.0%). Routing checks used a bounded Home returned-state edit, the
shared artifact-reader large-text fix (`c704fc997`), and an Intake correction
that crosses into the authority contract and backend owner. These checks show
which contract and evidence path each task reaches; they do not measure time
saved. The existing large-text verdict is carried from an ancestor revision and
its PNGs are not tracked. On app revision `6b9d204`, exact-flow selection and
failure classification passed 12 focused tests. The documented short slug
completed a dry-run and selected only `polish/home-root-returned`; the partial
suffix `returned` failed closed. The dry-run produced 0 screenshots. The
Home/Places wrong-state screen replay therefore remains unverified.

The native doctor passed on the assigned iPhone SE with Maestro 2.6.1, Java 17,
Metro port `57436`, and installed app `com.fyan.vesper` version `1.0.0`, but this
proves only bundle ID and marketing version. The first selected
`polish/home-root-returned` capture produced 0/1 product images. Its Maestro
failure frame shows the iOS development-client error for
`http://127.0.0.1:57436`; Metro was bound to IPv6 loopback (`::1`) while Expo
advertised IPv4 loopback. Setting `REACT_NATIVE_PACKAGER_HOSTNAME=localhost`
aligned the advertised hostname with Metro's bind address, and the next run
successfully bundled 5,348 modules. The app then displayed a Worklets runtime
error: JavaScript `0.7.4` versus native `0.11.3`. The installed app's bundle ID
and marketing version match, but its native module is stale. A rebuild was not
available because `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` is unset and no existing
installable app bundle was found. Maestro's failure hierarchy does not expose
the Worklets message; the runner therefore still reports generic app-readiness
for that historical frame and allows its one bounded retry. That attempt
remains a recorded 0/1 diagnostic run, not the current capture verdict. The new
failure-frame reader does classify the earlier explicit Metro URL as
infrastructure and retains the exact URL; unit tests also cover Worklets
diagnosis when the message is present in failure diagnostics.
A LAN-bound Expo start was rejected by automatic approval review because
local-network devices could reach the development server and source/config; no
workaround was attempted. The later selector and classifier checks were
non-native; they did not repeat capture. This first-attempt status was superseded
by the documented-flag `home-root-returned` capture recorded above; the original
Home/Places wrong-state replay remains open.

**Package 3A hosted receipt (October 1, 14:29 UTC).** Workspace PR
[40](https://github.com/fy538/travel-workspace/pull/40) passed Merge ready,
Reliability, `Contract and golden paths`, and all four Maestro syntax shards;
the required aggregate took 7m08s and the shards took 7m01s, 5m04s, 5m24s, and
5m42s. App PR [210](https://github.com/fy538/travel-app/pull/210) passed Merge
ready scope, static, and selected tests, plus the existing required Lint,
Frontend governance, Security audit, Visual evidence contracts, Type check, API
types freshness, QA tooling contracts, and Design alignment gate. Its selected
test job passed in 9m36s. The broad main/nightly Test and Logic QA jobs were
skipped on the PR by their configured conditions. Workspace Maestro Cloud PR
smoke was skipped because that service is not configured. This establishes the
candidate's hosted checks; it is not a comparison of hosted test speed or total
runner cost.

**Package 3A sharding experiment receipt (October 1).** App PR
[211](https://github.com/fy538/travel-app/pull/211) adds a non-required pilot
that compares the existing two-worker full Jest run with two isolated shards.
Its first hosted attempt failed because the jobs lacked the pinned workspace
catalog inputs; the workflow was corrected to use the same immutable workspace
checkout as app merge readiness. On corrected run `36922474210`, both shards
passed: shard 1 ran 645 suites and 4,439 tests in 255.748 seconds, and shard 2
ran 644 suites and 4,739 tests in 282.763 seconds. The union check confirmed all
1,289 current test files exactly once. The full baseline ran for 8m36s before
`__tests__/screens/place-home.smoke.test.tsx` failed its
`Place exact reading mounted lifecycle` case at Jest's five-second timeout;
1,288 suites and 9,177 tests passed, with one test failing. That case passed in
shard 2 and in one isolated local file rerun (17/17 tests; file completed in
5.386 seconds). These isolated passes do not establish stability under the
full-suite load. Treat the hosted comparison as invalid, retain the original
full-suite required check and all 1,289 files, and make no sharding speed claim.
A comparable successful hosted baseline is still needed before deciding whether
the optional experiment is useful. The rerun could not be requested in this
session because the GitHub API was unreachable; the failed evidence remains
visible rather than being converted into a pass.

The final local change-aware preflight also passed on workspace `a04ffaf0`
(docs staged in the working tree), backend `bd1a683b`, and app `321fb1cb`, with
explicit bases `bc69d6d0`, `bd1a683b`, and `e7bdc660`. Its selector correctly
fell back to all app tests because the merge-scope selector itself changed:
1,289 suites, 9,180 tests and one snapshot passed. App lint reported 167
existing warnings and no errors; workspace tooling passed 141 tests in 17.83s;
contract, API, compatibility, living-document link, spine, canon and inventory
checks passed. The first sandboxed attempt is retained as a failed run: Expo
could not write its ignored cache, one Jest worker segfaulted (1,288/1,289
suites passed), and four workspace fixtures could not bind ephemeral localhost
sockets. The same preflight passed when rerun with those normal local test
permissions enabled. Full log:
`/private/tmp/vesper-efficiency-package6-preflight-20261001.log`.

**Package 3B owner map and implementation (October 1).** The required check
names remain those in the [CI runbook](../reliability/CI%20Plan.md), and no
branch-protection setting changed. App `Merge ready` static now runs the unique
merge-scope selector contract only. Required `Lint`, `Frontend governance`, and
`Type check` continue to own the fast lint/native/API/schema, icon-integrity,
Home-budget, and TypeScript contracts. The icon check is in required `Lint`;
selected unit tests and the `Merge ready` aggregate remain unchanged.

Backend `Merge ready` static now runs only the broad-exception ratchet and
world-catalog runway, the two checks without an equivalent required PR owner.
Ruff/format, import and route analysis, and mypy stay in required `lint`,
`import-boundaries`, and `typecheck`; all structural checks, including route
shadowing, remain in their existing required owners. The selected database job
still applies migrations to prepare its isolated runtime suite, loads fixtures,
runs change-selected DB tests and itinerary canonical certification. Migration
lifecycle, schema drift, CHECK constraints, event/entity parity and supported
rollback now execute once in required `test-db-migrate`.

Workspace `Merge ready` now resolves the change-aware workspace plan before
dependency installation. Its plan names whether selected commands need backend
or app dependencies; documentation-only work installs neither, workspace test
and contract paths request the dependencies they use, and selected child paths
request their own. Both child checkouts and exact-revision assertions remain.
The actual current PR diff selects workspace tooling and cross-repository
contracts, so it still needs both dependency sets. Synthetic selection tests
show a prose-only workspace change needs neither. The root `Merge ready` remains
an additive early-feedback path alongside required `Contract and golden paths`;
the overlap's fail-fast benefit versus extra runner time has not been measured.

Local evidence: workspace workflow and selector tests passed 46 cases; app
selector tests passed 5 cases, its new workflow-ownership tests passed, and
`npm run brand:icons:check` passed. Backend ownership tests pass in the repo's
development environment; `make merge-ready-static` passed the broad-exception
ratchet at 1,190/1,190 and validated five season plus four Here catalog entries.
An earlier attempt forced the system Python and could not import SQLAlchemy;
rerunning with the lane's `.venv` passed. Backend PR 240's hosted candidate
passed on run 36894505540. No latency or runner-time improvement is claimed
from that single check result.

**Package 3B delivery receipt (October 1).** Workspace PR 40 and app PR 210
passed their hosted required checks. Backend PR 240's first hosted run cancelled
while full-history checkout exceeded the two-minute scope-job timeout; the
fail-closed `Merge ready` aggregate reported that cancellation. No selector or
test failed. The backend workflow now fetches depth 2 for `pull_request` runs,
where GitHub checks out the synthetic merge ref with the recorded base as a
parent, and depth 0 for `workflow_dispatch`, which accepts an arbitrary base.
A synthetic shallow-clone reproduction retained the exact merge base and
changed-file list. The focused workflow contract test passed 3/3, the
change-aware offline suite passed 22,085 tests with 14 skipped and 53 expected
passes, and `make ci-static` passed. The first concurrent static attempt
produced a mypy internal error; isolated mypy and the full static rerun both
passed across 1,893 source files. Hosted run 36894505540 then passed the
selected offline tests, isolated database tests, static checks and `Merge
ready`; its scope job completed in 14 seconds. This is one hosted check result,
not a comparable full-run latency or runner-time measurement.

The latest bounded local cross-repo preflight completed in 287.010 seconds on
workspace `9e553648815d05ed110952dcd6d2ddf1e505dac5` (exact command and tuple
are in the verification baseline),
backend `05dcc9144a2cb997c5cf4bb75161f842c60e03e4`, and app
`906c5d5a4719da504ddb492bf4e2fd85c8caabc2`. Its log is
`/private/tmp/vesper-efficiency-postfix-preflight-logs/engineering-efficiency-3b-post-fix-preflight-20261001T164505Z.log`;
Jest passed 9,180 tests, backend passed 22,085 tests with 14 skipped and 53
expected passes, and workspace passed 144 tests. This single local measurement
does not establish a stable productivity or hosted speedup.

The checkout choice follows GitHub's documented `pull_request` merge-ref
behavior and checkout depth semantics:
[event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows),
[checkout history options](https://github.com/actions/checkout#fetch-all-history-for-all-tags-and-branches).

**Package 3C hosted checkout trial (October 1).** Workspace PR 40 run
36905253965 passed the reliability job, all four Maestro syntax shards and the
required aggregate on workspace `91f991eaf13b168d65ff5796997574faee6b024e`.
Each syntax shard asserted the same pinned child revision tuple and passed its
partition. Compared with the full-history run 36897425346, combined child
checkout time across the four syntax jobs fell from 744.538s to 51.194s
(93.1%, or 11m33s less runner time); the slowest syntax job fell from 10m03s
to 5m05s. This is a paired hosted CI measurement for those checkout steps, not
an end-to-end or developer-productivity result.

The passing run also exposed the remaining critical path: `workspace-checks`
spent 345s checking out Travel Agent and 16s on Travel App, then finished in
10m56s. Its full child history existed only so new-document governance could
list two historical baseline trees. The next bounded trial checks out each
pinned child at depth 1, then fetches its configured baseline commit with
`--filter=blob:none --depth=1` before governance runs. The checker reads tree
names from those commits and file contents only from the current checkout.
The [checkout action supports shallow fetches](https://github.com/actions/checkout#fetch-all-history-for-all-tags-and-branches),
and [Git's blobless filter](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---filterltfilter-specgt)
omits historical file contents. A local shallow-clone reproduction passed the
production governance checker on all 405 post-baseline documents while keeping
the current HEAD shallow and unchanged.

**Baseline-only history hosted receipt (October 1).** The follow-up on PR 40,
workspace `ddef43ff7c2464bb17e54138b8fd6b06c825d4e0`, passed Reliability run
[36908354919](https://github.com/fy538/travel-workspace/actions/runs/36908354919),
all four syntax shards and the required aggregate. The child checkout and
baseline fetch steps in `workspace-checks` took 11s combined (Agent 5s, App
5s, historical-tree fetch 1s), compared with 361s for the two full-history
checkouts in run 36905253965. The Reliability job fell from 10m56s to 5m30s
in this paired comparison. The historical tree fetch and child-document
governance passed on the pinned candidate. This is one before/after hosted
pair, so repeatability and broader end-to-end improvement remain unproven.
The Maestro Cloud PR smoke was skipped because that service is unconfigured;
the separate configuration check passed. This provides no native-device visual
QA evidence.

The measured local preflight for the shallow-baseline candidate completed in
376.152s with exit 0. It used workspace `91f991eaf13b168d65ff5796997574faee6b024e`
with the workflow, helper, tests and docs changes present; backend
`05dcc9144a2cb997c5cf4bb75161f842c60e03e4`; and app
`906c5d5a4719da504ddb492bf4e2fd85c8caabc2`. App passed 9,180 tests; backend
passed 22,085 with 14 skipped, one expected failure, 52 expected passes and
one warning; workspace passed 150 tests. The exact command, dirty flags and
log path are recorded in `docs/reliability/test-loop-baseline.json`. This local
preflight does not substitute for the hosted workflow run.
The helper's focused contract suite then passed 38 tests, including malformed
baseline SHAs, a successful blobless fetch that preserves both shallow HEADs,
and an unavailable remote that fails closed without moving HEAD; that command
and result are also recorded in the measurement file.

An offline iOS JavaScript export with internal/mock flags completed in 25.4s,
bundling 5,443 modules, 503 assets and a 23 MB Hermes bundle. This proves JS
packaging only. The worktree has no generated iOS project, and `app.config.js`
reports `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` unset; no native build or capture was
attempted from this export.

### Efficiency lane setup

Eng Efficiency owns `codex/engineering-efficiency` in all three independent
repositories in the coordinated `engineering-efficiency` worktree. The lane was
created with `scripts/new-worktree.sh
engineering-efficiency --base origin/main` from the exact landed workspace,
backend and app revisions recorded above. The owner is Codex thread
`01a0f2f0-0917-71b0-a150-030d05b2f680`; `.workspace-lane.json` records the bases,
owner and delivery outcome.

The revised roadmap was copied from Orchestration's uncommitted draft at
`travel-workspace--home-value-delivery`, retaining its integration measurements
and our screenshot-purpose guidance. Both source checkouts and their drafts
were preserved. This lane's copy is the working plan for efficiency execution;
Orchestration continues to own the program roadmap.

Runtime inspection reports Compose project `vesper-engineering-efficiency`,
Postgres port `63924`, Qdrant ports `63925`/`63926`, API port `63927` and Expo
port `63928`. No services were started and no device is assigned. These ports
must be rechecked at startup. Dependency installation and product/native tests
remain unrun; they are not prerequisites for this branch-and-document setup.

The setup receipt was committed as `cef7ac55af49`; Package 3C is committed as
`b1c174b7`. That slice owns the reliability workflow, workspace Maestro targets,
the deterministic partition helper and their existing workflow tests. It
preserves the required `Contract and golden paths` result name. CI behavior has
been exercised on the remote branch; branch-protection settings were not changed.

**Hosted pilot receipt (September 30 local time; October 1 UTC).** The published
workspace branch is [PR 38](https://github.com/fy538/travel-workspace/pull/38),
at workspace commit `d298cafc2210b5e5052227a5263d28ff4e08554b`; the backend and
app remained at their recorded base revisions. Reliability workflow run
[36811769199](https://github.com/fy538/travel-workspace/actions/runs/36811769199)
passed its full reliability job, all four Maestro syntax shards, and the
`Contract and golden paths` aggregate. The job durations reported by GitHub
were 6m07s for reliability, 4m12s / 4m57s / 5m05s / 5m19s for the syntax shards,
and 6s for the aggregate. On those reported durations, the required-job
critical path was approximately 6m13s, excluding queue time. Summed job runtime
was 25m46s, about 2m28s (10.6%) above the prior 23m18s single required job. The
critical path fell by about 17m05s (73.3%), while measured runner work increased.
This is a favorable first sample for feedback speed with a real resource cost;
it does not establish lower runner cost or stable percentiles. Keep the pilot
visible for review and do not claim generalized efficiency until comparable
future runs confirm it. PR review/landing and the separate Merge readiness
workflow status are not established by this Reliability run receipt.

### Start and adoption checkpoints

Before code changes, inspect fresh Git state and `make worktrees` against the
landed tuple above. The merge is complete; do not repeat its broad tests merely
to establish ownership. New changes still need their own applicable checks.
Reuse an appropriate coordinated tooling lane or create one under the existing
workspace lifecycle; record its exact bases and runtime assignment here. Resolve
the bounded writer for shared tooling under the
[program's shared-file rule](vesper-program-roadmap.md#code-boundaries-and-shared-files).
This plan does not repurpose another session's checkout or device.

Each delivery follows **baseline → implement one improvement → verify → land →
adopt in the affected product lane → measure**. Land a usable increment before
accumulating the next package. An adoption receipt records the revision tuple,
actual command/environment, result and evidence limit in this document; update
the operational owner doc when behavior changes. Do not create another tracker.

Product lanes continue independent work in parallel. A task needs to wait only
when it depends on an unlanded tooling/interface change or the same reserved
runtime. Same-coverage test optimization does not depend on native capture.
Changed review rules depend on demonstrated detection, and CI consolidation
depends on preserving every required guarantee. The timing pilot continues
across deliveries; it does not hold a proven fix until ten tasks are complete.

For each complete slice, collect the inexpensive check failures, repair them
together and publish one stable candidate. Run focused feedback while editing;
keep final coverage based on the whole integration diff. Avoid successive tiny
pushes that cancel jobs before they report. Independent lanes need not wait for
each other, but changes sharing a contract must land as a coherent compatible
set. Central integration lands child candidates after their applicable required
checks pass, then records the accepted immutable tuple for workspace validation.
Do not repin solely to identical-tree merge commits.

Use one bounded watcher per active verification set and consolidate failure
diagnosis rather than repeatedly reopening unchanged logs. Keep product-required
progress communication concise; a status update is not verification. These
operating changes require no new tracker, monitoring service or approval layer.

### Package 1 — Make native QA start reliably

**Queue:** second in the current order; independent after baseline
preparation and eligible earlier when it unblocks product work.
**Delivery owner:** Eng Efficiency; mobile/runtime
and workspace tooling own the affected implementation boundaries.

First apply the evidence selection in section 4 to the existing intake and
surface entry point: behavior/integration checks for nonvisual outcomes,
targeted captures for changed presentation, broader visual review only for
affected shared designs or milestones. Keep this selection concise in the existing
task receipt. Implement the corresponding owner-document refinement with
this package; Package 2 then simplifies the remaining review machinery and
reading path. This roadmap edit itself does not bypass current obligations.

Extend the existing surface entry point to resolve the selected lane's device,
ports, output directory and installed app identity once. Forward supported
selection flags explicitly; reject unknown flags rather than silently widening
the run. Make preflight identify simulator, permission, Metro and native-version
failures before capturing. Use one shared retry budget across wrapper and runner:
after a repeated identical infrastructure failure, retain diagnostics and repair
that cause before another attempt. Any unresolved repeated infrastructure
failure remains blocked/unverified rather than receiving a product pass.

**Existing targets:** app [Task Intake](../../travel-app/docs/Task%20Intake.md)
and [surface index](../../travel-app/docs/surfaces/README.md), plus
[surface wrapper](../../travel-app/scripts/polish-qa/run-surface-qa.mjs),
[runner](../../travel-app/scripts/polish-qa/run-polish-qa.mjs),
[preflight](../../travel-app/scripts/polish-qa/preflight.mjs),
[device lock](../../travel-app/scripts/polish-qa/run-lock.mjs), and
[workspace runtime script](../../scripts/dev.sh).

**Acceptance:** the pilot routes a nonvisual backend change to its behavioral
checks, a local rendering fix to targeted visual evidence, a shared visual change
to representative consumers, and a persistence/gesture change to observed
outcomes. It must still catch the known reader clipping and must not accept a
saved label or unchanged gesture screenshots as sufficient functional proof.
A selected flow runs only that flow on the reserved device;
missing device, denied output directory, wrong native build and missing server
each produce the correct diagnostic without a retry storm. A valid warmed app
completes a real capture in its intended managed worktree. Include both working
and failing cases; mocked command tests alone do not establish simulator access.

### Package 2 — Make review proportional to the change

**Queue:** third; documentation reconciliation is independent of device access.
**Delivery owner:** Eng Efficiency within mobile QA/surface and task-intake
ownership. Preserve founder review for unresolved product/authority choices.

Build on Package 1's evidence selection and reconcile the remaining AGENTS,
Task Intake, verdict and lifecycle guidance with section 4. Review current
capture sets for duplicated visual coverage, retaining states with distinct
failure risks; do not cut them to a numerical quota.
Offer targeted capture/review through the existing command. Remove the finding
quota and the obsolete perceptual-hash carry instructions; retain exact-input
provenance. Pilot on a reader fix and a Home/Places fix. Reuse registered fixtures
and surfaces instead of adding a parallel registry.

**Existing targets:** app [AGENTS](../../travel-app/AGENTS.md),
[Task Intake](../../travel-app/docs/Task%20Intake.md),
[surface index](../../travel-app/docs/surfaces/README.md),
[verdict protocol](../../travel-app/docs/surfaces/_agent-verdict-protocol.md),
and the existing verdict validator/scaffolder beside the surface wrapper.

Shorten the ordinary task-reading path in existing workspace/child AGENTS and
Task Intake documents: retain non-obvious invariants and direct owner pointers,
remove duplicate summaries, and distinguish local maintenance from work needing
broader product/design context. Reuse familiar context only while its relevant
inputs remain current. Keep the product canon available and preserve escalation
to authority, audience, contract and shared-design owners.

**Acceptance:** an isolated copy/layout fix receives bounded review; a shared
reader change still selects representative consumers and accessibility cases.
Replay the observed large-text clipping and a wrong-state capture: both must be
detected or explicitly left unverified. A clean case can pass without invented
findings. If the pilot misses an important defect, expand the affected rule and
record why rather than adding a blanket review round.
For task routing, compare a bounded local fix and a shared/authority-sensitive
change: both find the correct owner and evidence obligations with less repeated
reading. A shorter document alone is not acceptance evidence.

### Package 3 — Separate iteration from candidate verification

**Delivery owner:** Eng Efficiency within workspace CI and child selector
ownership. The original 3C → 3A → 3B implementation sequence and its receipts
below are historical; the remaining measured assignment is in section 5.
The lettered names remain stable references, not a request to rebuild landed work.

**3C — Workspace critical path, original first implementation.** The completed workspace
check took 23m18s, including 16m55s of flow validation. The current wrapper starts
the pinned Maestro semantic parser separately for each of 408 non-config flow
files. This is syntax validation, not 408 device journeys.

Trial four isolated CI jobs over a deterministic partition of the same flow
inventory. Each job retains the full checkout needed to resolve referenced flows
and scripts, uses the same pinned CLI and validates its assigned files serially.
Do not simply increase `MAESTRO_CHECK_JOBS` in one shared environment: the wrapper
documents a logger-state race. Separate runners are the initial isolation
mechanism; no custom parser or replacement test platform is needed.
[GitHub matrix jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
support this arrangement; the
[pinned Maestro command](https://github.com/mobile-dev-inc/Maestro/blob/cli-2.6.1/maestro-cli/src/main/java/maestro/cli/command/CheckSyntaxCommand.kt)
takes one file.

Move cheap credentials, tuple/input, registry/document and database-readiness
checks ahead of long work where their prerequisites permit it. Independent flow
validation and real-database journeys should not be serially dependent merely
because they currently share one job. Keep the existing required aggregate name
and make it require every expected result; a missing, cancelled or failed
partition must fail. If a required-check name or policy must change, use the
existing separately evidenced cutover process.

**3C acceptance:** the partition union equals the original full inventory with
no duplicates or omissions; nested references remain resolvable; valid flows
pass; malformed syntax, missing inputs/CLI, a failed worker and an absent shard
cannot produce a green aggregate. Prove dependency/setup failures surface before
long validation. Measure complete hosted latency and runner-minutes on equivalent
inputs, retaining the serial route if the pilot is not better. Do not narrow
flow coverage or bulk-delete flows to meet a time target.

**Local implementation receipt (October 1; hosted comparison pending).** Commit
`b1c174b7` splits the prior workspace job into the existing required aggregate,
the full reliability suite, and four isolated Maestro syntax jobs. The inventory
helper matches the former recursive shell selection exactly, including `.yaml`,
`.yml`, and the existing config exclusion. Every partition uses the full sibling
checkout; CLI calls stay serial inside a shard. A missing or empty shard, missing
CLI, failed/cancelled/skipped job, or absent aggregate input cannot pass the
tested local boundary.

The focused command
`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider -q scripts/tests/test_partition_maestro_flows.py scripts/tests/test_merge_readiness_workflows.py`
passed 39 tests. `make docs-check`, `make maestro-flow-inventory-check`,
`make journey-registry-check`, and the moved flag, compatibility, card-arrival,
chat-card-type and API coverage checks passed. Maestro CLI 2.6.1 passed all 408
flows: four concurrent isolated local runs each returned 102 successful syntax
results. On macOS 25.5 arm64, the slowest shard took 187.552 seconds; summed
shard command time was 747.119 seconds. These are local measurements with a
different runner and setup from hosted CI, so they do not establish reduced
hosted latency. The raw command measurements and logs remain under
`/private/tmp/vesper-maestro-run/` for this working session.

The initial
`make verify-changed WORKSPACE_BASE_REF=4febe0d461a62d204ba4dee9eaad7813c7c1509c AGENT_BASE_REF=bd1a683b8656c3f4091e16abb64f57897fa7fc42 APP_BASE_REF=e7bdc660501eaa19234e6b45bda033658edaa2d4`
run on workspace commit `37f2bea3e3da` with Python 3.14.6 reported 136 passed
and 5 environment failures: one checker could not import SQLAlchemy because
backend dependencies were absent, and four worktree-runtime tests could not
bind local sockets in the sandbox. The final
`make verify-changed WORKSPACE_BASE_REF=4febe0d461a62d204ba4dee9eaad7813c7c1509c AGENT_BASE_REF=bd1a683b8656c3f4091e16abb64f57897fa7fc42 APP_BASE_REF=e7bdc660501eaa19234e6b45bda033658edaa2d4`
run on workspace commit `b55ff407d612`, with Python 3.13.0, Node 24.13.0 and
local socket access, exited 0. All 141 workspace tests passed in 16.13 seconds.
The full OpenAPI snapshot and mobile projection, generated schema equality,
10×2 place-identity seams, 376-type schema bridge, API audit, compatibility,
card-arrival, chat-card-type, and selected documentation checks passed. The
contract run used temporary ignored links to the cached locked tools
`openapi-typescript` 7.13.0 and TypeScript 5.9.3 because the app dependency tree
was absent; the links were removed after the run. The app test suite was not
selected because the app had no changed files. Hosted CI and the equivalent
hosted latency comparison remain required before claiming Package 3C acceptance.

The repository-defined no-publish landing gate,
`make land-worktree NAME=engineering-efficiency`, also passed from the canonical
workspace on candidate `b9d0bc35e999`. It fetched all three live `origin/main`
refs, confirmed they still equal the recorded base tuple, and reran the complete
change-aware preflight successfully. The gate did not publish the lane or run
hosted CI; the local candidate is ready for review and publication.

**3A — App test determinism and execution, second in the queue.** At final
candidate `21fdb724f`, the first hosted test job failed two unchanged tests;
the retry passed 1,289 suites and 9,178 tests in 434.846s of Jest execution.
The earlier 401.584s run at `6b3066aa5aa1` is a separate candidate, not proof of
a speed trend.

The invite readiness race is repaired in the current candidate. Its shared-plan
test now waits for the RSVP control to become enabled and covers immediate,
delayed and rejected `AsyncStorage` reads while keeping the exact submission
assertion. This follows a controlled 500ms delayed-read reproduction that
previously pressed while the control was disabled and observed zero submission
calls; that demonstrated a test readiness race, not a user-visible bypass.

The Place-reader timeout was traced to the test harness. That describe uses fake
timers while TanStack Query publishes the resolved query through a timer-backed
notification. The test now flushes the zero-delay notification inside `act`
before its existing reader assertion. The timeout and product assertion remain
unchanged. Ten consecutive runs of the full Place-home test file passed 17/17.
This bounds the observed issue on this machine; it does not prove there are no
other intermittent failures.

The same selected merge inventory (99 suites, 754 tests) passed with both two
and four Jest workers. On the local 14-CPU Mac, the four-worker runs took 8.521s
and 7.655s by the measurement wrapper, versus 14.458s and 14.509s at two workers;
the measured medians are 8.088s and 14.484s respectively. The selector now
chooses a bounded worker budget from available parallelism (two to four), and
the actual selector candidate passed the same inventory in 7.959s. This is a
local result only; Node 20 hosted timing and runner-minute effects remain open.

After these fixes, the full app coverage command with its report directed to a
writable temporary directory passed 1,289 suites and all 9,180 tests locally in
160.614s. Jest printed one open-handle/worker cleanup warning; the command
exited successfully and wrote its report. An earlier run reported the same test
pass in 106.802s but failed to write its coverage report inside this checkout,
so it is not clean coverage evidence. A preceding no-cache full run on the
pre-fix candidate failed only the Place initial-reading timeout (1,288 suites
passed, one failed; 9,179 of 9,180 tests passed), so its 361.159s duration is
not a comparable timing sample. Asset aggregation and a lightweight convention
setup were tested and discarded because they were slower or failed to retain
exact assertions. Keep the current setup unless a comparable full run
demonstrates a benefit. The scoped path's blanket convention family still
merits later impact mapping; do not remove it without preserved coverage.

**3B — Verification ownership, third in the queue.** Map overlapping calls from
`verify:fast`, regular PR CI and merge readiness, then give each guarantee one
execution owner. Select workspace-only prerequisites before installing both child
dependency sets when the changed inputs do not need them. Preserve test/checker
coverage and the aggregate's failure, cancellation and intentional-skip handling.
Any hosted required-check cutover needs its own executed evidence.

Expose the selected tests and reason for broad fallback before expensive work.
During iteration, run the affected behavior's tests; run the integration-base
preflight when a coherent candidate is ready. Consolidate duplicate checks within
one job and reuse their result there. Keep full main/nightly regression and
hosted requirements. Prefer smaller coherent landings to accumulating unrelated
broad-trigger changes in one lane.

**Existing targets:** [workspace reliability workflow](../../.github/workflows/reliability.yml),
[Maestro syntax wrapper](../../travel-app/scripts/maestro/check-syntax.sh),
[flow inventory validator](../../scripts/validate-maestro-flows.py), their existing
workflow/inventory tests, app test setup and convention/asset tests,
[workspace selector](../../scripts/verify_changed.py),
[backend selector](../../travel-agent/scripts/merge_scope.py),
[app selector](../../travel-app/scripts/merge-scope.mjs), their tests,
repository workflows and [CI Plan](../reliability/CI%20Plan.md).

**Acceptance:** 3A reproduces or bounds the intermittent failures, verifies any
repair with controlled delayed/error cases and repeated representative runs,
retains the selected inventory, detects representative known violations and
reports lower complete-run latency on comparable measured inputs. A finite
passing repetition is not proof that flakiness is impossible; retain the first
failure and retry evidence. Failed tools or shards remain failures. Keep the original route if an experiment
does not improve the result. For 3B, routing tests cover local, shared, deleted and unknown inputs;
tool failure never becomes an empty passing selection. A candidate with an
earlier shared change still receives broad final coverage after later local
edits. Measure complete real runs before claiming improvement. Changing required
hosted checks remains a separate, explicitly evidenced cutover.

### Package 4 — Pilot a bundled QA app and cautious reuse

**Priority:** conditional on remaining build/Metro cost after Package 1.
**Delivery owner:** Eng Efficiency within mobile build ownership.
**Dependency:** reliable runtime identity.

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

The child-history trial above is a separate CI checkout experiment; keep its
baseline-tree dependency explicit and fail closed if it cannot be fetched. A
pinned uv installer using the current requirements locks, or one verified
unused-code/dependency family are likewise conditional experiments. Pick one
only after its remaining cost is established; no whole-repo build-system
migration or automatic dead-code deletion is scheduled.

### Package 5 — Put quality effort into the product loop

**Priority:** ongoing within the existing three product lanes; it does not wait
for this tooling queue to finish. **Owners:** each lane owns its outcomes;
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

The first mapping confirms that these tools measure different layers:

| Product outcome | Current evidence owner | What the current evidence establishes and what remains open |
|---|---|---|
| Preserve and reopen an exact original | App [Canonical Artifact Reader](../../travel-app/docs/surfaces/canonical-artifact-reader/contract.md), especially J11.B06 and registered source-open flows | The committed September 30 carried verdict records source open/return and largest-text assertions passing on fixture data. Native photo gestures, VoiceOver activation, and live owner-source readback are separate evidence. |
| Keep a useful collection and find it again | Workspace [Journey 11](../journeys/11-atlas-candidate-to-memory-control.md), especially J11.B03/J11.B05; backend P04 | J11 names keep/shelf/return and hide/restore paths. The current product-proof status matrix still shows no promoted P04 contract, database, or AI-eval receipts, so branch descriptions and test anchors do not establish current product-proof completion. |
| Share to the intended people without leaking private context | Backend consequence-authority corpus and multiplayer snapshots; P01–P04/P06 privacy tasks | The authority harness covers 80 cases and 21 state snapshots; the product-proof grader checks forbidden shared text. Offline tests validate those harnesses, not live model decisions or recipient experience. P05 thin-participant handoff remains explicitly dark. |
| Correct an interpretation while retaining its source | Backend P03 correction task; Journey J11.B04/J27; app reader correction contract | P03-03 now requires a named photo source plus equal before/after revisions; synthetic grader tests fail closed on missing or changed values. This does not establish owner-backed revision readback: the current `trip_photos` row exposes `photo_record` and occurrence evidence exposes `source_ref`, but neither defines a content revision. No live adapter or promoted receipt exists. J27 remains the source-preservation journey owner. |
| Give useful research with sources and honest uncertainty | Backend P02 provenance/freshness tasks, P04 uncertainty task, five [artifact-quality fixtures](../../travel-agent/eval/artifact_quality/), and workspace P08 contract | P02 is spatial/operational grounding, not a general cited-research proof. P08 specifies sourced interpretation, unknowns, privacy, and human outcome but remains dark; do not report it as shipped acceptance or activate it from this QA lane. |

The original October 1 offline backend harness run passed on Python 3.13.0 and
backend revision `cbe7ff908`: `PYTHONDONTWRITEBYTECODE=1 ./.venv/bin/python
-m pytest -p no:cacheprovider tests/eval/test_product_proof_eval.py
tests/eval/test_consequence_authority.py tests/atlas/test_artifact_quality_eval.py
-q` → **36 passed**. These tests exercise graders, schemas, fixtures, and mock
composition only; they do not execute an agent, call a model, prove persistence,
or promote product-proof receipts. Its first invocation exited with a pytest-cache
write error, so only the cache-disabled rerun is counted as passed. After the P03
grader change, the same command passed **38 tests** on backend revision
`681c518c8` (parent `cbe7ff908`); this is the current focused harness result.

`make journey-registry-check` passed structurally (28 journeys, 82 branches, 8
proof definitions, 4 governed runners); `make journey-evidence-report` reported
no journey evidence receipts. Neither check certifies product behavior. No
`TEST_DATABASE_URL` is configured and Docker access is unavailable in this
lane, so database and live-source evidence remain unrun.

The product-proof task bank contains 24 cases across P01–P04 and P06. P05 and
P08 are dark in the canonical proof spine; keep them visible as future gaps and
do not add tasks that imply their surfaces are available. The P03 task now
expresses the unchanged-revision invariant, but its adapter and source-owner
boundary remain undefined: `trip_photos` has no explicit content revision, and
the grader's synthetic records do not bind revisions to owner readback. The
other actionable gap is to reconcile J11 branch claims with the currently empty
promoted P-level receipt matrix. Package 5 remains **mapping in progress** until
active owners establish the real source revision and readback, decide which
missing checks belong in existing proofs, and record revision-bound product
evidence.

**Acceptance:** a model/prompt change can be compared with the previous version
for usefulness, grounding, latency and cost while hard authority checks remain
intact. A visually attractive artifact with a broken original, wrong audience or
unsupported claim fails its relevant acceptance. No new global numeric “quality
score” substitutes for those separate outcomes.

### Package 6 — Retire completed working documentation

**Queue:** as encountered in active work, after the completed central roadmap
reconciliation; not a new global cleanup pass. **Delivery owner:** Eng Efficiency within workspace documentation
governance; product owners retain their current contracts and unresolved choices.

First reconcile conflicting instructions in the affected owner documents: the
central landing responsibility, actual accepted revision tuple, completed
versus pending work, and obsolete setup or product assumptions. Preserve each
rule's rationale and distinguish genuinely unresolved decisions. Do not shorten
instructions by dropping non-obvious safety or authority invariants.

Choose a bounded set of completed or superseded working plans whose current
owners already preserve their durable decisions. Use the existing expiry and
inventory data to find candidates, then check incoming links and unique evidence.
Archive the complete history where needed, repair live navigation and update the
existing inventory. Narrow ordinary task searches to current owners while keeping
historical evidence explicitly discoverable. Expiry alone never authorizes deletion.

**Existing targets:** [documentation index](../README.md),
[governance inventory](../governance/inventory.yaml), reviewed working documents
and their current owner links. Follow the existing lifecycle rather than adding
another permanent report or required cleanup gate.

**Acceptance:** affected operating rules agree on ownership and current state;
current tasks reach one active owner for each migrated topic,
historical rationale remains accessible, and link/inventory checks pass. Record
the removed live navigation/read burden; do not claim faster compilation or
smaller Git history from moving Markdown files.

**October 1 receipt:** moved the already archived Interaction Kernel Lab V2
execution report from `docs/working/` to
[`docs/archive/2026-09/claude-design-interaction-kernel-lab-v2-execution-report-2026-08-31.md`](../archive/2026-09/claude-design-interaction-kernel-lab-v2-execution-report-2026-08-31.md).
Updated both V2.1 provenance records and the controlled-comparison handoff,
preserved the full report and archival rationale, and changed its inventory
disposition to `archive`. Verification passed: 556 living Markdown links, 667
inventory entries with zero transitional dispositions, all ten spine entries,
and the canon word budget. This removes one archived report from the living
working-document set; it does not shrink Git history or establish faster builds.
The candidate-wide `make verify-changed` preflight and inventory check passed
after the move; the initial sandbox permission failures and successful rerun
are recorded in the Package 3A receipt above.

**October 1 second Package 6 receipt.** The August 12 product-loop and QA
synthesis expired September 11. Its own exit plan says to archive it if its
recommendations are not promoted; its nine listed open decisions remain
proposals. The current product canon, Journey contracts, mobile reliability
owners, and this CI roadmap now own the relevant direction and operating
requirements. The complete source and open-question history are preserved at
[`docs/archive/2026-10/product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md`](../archive/2026-10/product-loop-coherence-maestro-and-environment-strategy-2026-08-12.md);
no proposal is adopted by the move. Eight inbound references in six working
documents now point to the archive, and the stale inventory override was
removed. The source's relative implementation links were adjusted for its new
location. The explicit-base `make verify-changed` preflight also exited 0 against
workspace base `bc69d6d03eeb069eb8705953463b4ddc8a808e6d`, backend base
`bd1a683b8656c3f4091e16abb64f57897fa7fc42`, and app base
`e7bdc660501eaa19234e6b45bda033658edaa2d4`, on workspace `4eaa5b5` with this
docs change, backend `05dcc9144a2cb997c5cf4bb75161f842c60e03e4`, and app
`906c5d5a4719da504ddb492bf4e2fd85c8caabc2`. It passed all 1,289 app suites
(9,180 tests and one snapshot), all 22,085 backend tests (14 skipped, one
expected failure, 52 expected passes), and 151 workspace tooling tests, along
with contract, API, compatibility and documentation checks. App lint had 167
warnings and no errors; Jest force-exited one worker. The hosted database and
required action checks remain authoritative. This removes one expired synthesis
from living working docs; it does not claim a faster build or smaller Git
history.

**October 1 third Package 6 receipt.** The August 13 visual-polish and
screenshot-QA synthesis expired September 12. Current app Task Intake owns
frontend validation scope, the Frontend Engineering Loop owns screenshot-QA
operations, and Design Workflow owns the design handoff; the September QA
roadmap now specifies proportionate screenshot selection and AI review limits.
The September 15 content-to-native plan explicitly treats the August note as
historical research with expired execution assumptions. Its nine open choices
and full research history remain preserved at
[`docs/archive/2026-10/visual-polish-evaluation-and-design-workflow-2026-08-13.md`](../archive/2026-10/visual-polish-evaluation-and-design-workflow-2026-08-13.md);
no proposed gate, checkpoint quota, Figma pilot, or evaluator threshold is
adopted by the move. Four inbound references in four working documents now
point to the archive, including one stale absolute path converted to a
repository-relative path. The stale inventory override was removed and the
source's relative links were adjusted for its archive location.
The explicit-base `make verify-changed WORKSPACE_BASE_REF=origin/main
AGENT_BASE_REF=origin/main APP_BASE_REF=origin/main` preflight exited 0 against
workspace base `bc69d6d03eeb069eb8705953463b4ddc8a808e6d`, backend base
`bd1a683b8656c3f4091e16abb64f57897fa7fc42`, and app base
`e7bdc660501eaa19234e6b45bda033658edaa2d4`, on workspace `ef048c47c6791a10a81f0e5f9cec2007c6ffe359` with this docs change, backend
`05dcc9144a2cb997c5cf4bb75161f842c60e03e4`, and app
`906c5d5a4719da504ddb492bf4e2fd85c8caabc2`. App verification passed with
1,289 suites, 9,180 tests and one snapshot; lint reported 167 warnings and no
errors, and Jest force-exited one worker. Backend static checks and 22,085 tests
passed (14 skipped, one xfailed, 52 xpassed, one warning); workspace tooling
passed 151 tests. Contract, API, compatibility and documentation checks passed.
The initial sandboxed invocation could not write local caches; rerunning with
normal worktree cache access passed. Hosted database and required action checks
remain authoritative.

### Package 7 — Retire verified obsolete implementation families

**Queue:** conditional on demonstrated maintenance burden. **Delivery owner:** Eng Efficiency proposes and implements
bounded engineering retirement within existing app/backend/workspace owners;
product owners retain unresolved design and authority choices.

Start with one family that repeatedly adds tracing, adaptation, duplicated tests
or compatibility work. Trace source callers, Expo route/config entrypoints,
server/non-mobile consumers and applicable operation-registry removal criteria.
A grep miss, unused-code report, retiring label or incomplete product UI is not
proof of disuse. Infrastructure for the ongoing product design remains in scope
for delivery and must not be removed merely because presentation is withheld.

For that family, pair implementation and test disposition. The nine backend
concierge tests skipped for the retired Step 7 behavior are investigation
candidates: establish current replacement coverage before removal. Quarantined
or intermittent tests require separate diagnosis; repair meaningful safeguards
rather than deleting them to obtain a green result. Preserve contracts that
still govern current behavior.

Retire verified dead compatibility adapters, operations and dependencies in a
small coherent slice. Update the existing lifecycle registry and owner docs,
regenerate API projections/types if wire contracts change, and run required
coverage and focused behavioral checks. Do not hand-edit generated types,
rewrite old database migrations or mass-delete all retiring endpoints. Required
merge checks remain authoritative.

**Acceptance:** no current caller or required behavior is lost; the old and
replacement paths have explicit dispositions; contracts and relevant valid,
violating and failure cases pass. Record the tracing/rework or verification
burden removed in existing receipts and compare similar subsequent tasks.
Removed files, fewer lines and fewer tests are secondary inventory measures,
not proof of engineering efficiency. Stop expanding the slice when the family
is resolved; continue with the next measured bottleneck.

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

For assumption retirement, also record obsolete-owner detours, compatibility
paths touched and avoidable rework on comparable changes. Preserve failed runs
and actual acceptance scope; use the existing receipts rather than a new gate
or scorecard.

Track first-attempt native setup success, time to first useful native result,
ordinary merge-readiness time, review false alarms, and later regressions/rework.
For screenshot work, record the visual question, distinct defects found, false
alarms and capture/review time in existing receipts. Evaluate duplicate captures
by the evidence they add, preserving known-defect detection as scope shrinks.
Track candidate-first-pass rate, superseded/cancelled runs and intermittent-test
retries as well as first useful failure time. Separate runner-minutes from the
elapsed critical path and distinguish implementation/repair time from a stable
candidate's verification time.

The objectives are **under five minutes for ordinary scoped changes** and,
initially, **under ten minutes for a stable broad integration candidate**, from
publication to required merge readiness. Track total time from first verification
separately so repair is not hidden by resetting the clock. These are targets, not
achieved results or new timeout settings. Screenshot and test counts describe
workload, not success.

After the pilot, retain changes that improve delivery with adequate defect
detection; repair or revert weak selection/reuse rules. Full-suite comparisons,
known-defect replay and sampled deeper review are controls during the pilot,
not permanent extra gates on every change.

## 7. Boundaries and decisions

Keep generated contracts, ownership/authority tests, real native interaction,
large-text coverage and honest evidence limits. Do not replace deterministic
assertions with a vision model, bulk-delete flows to hit a quota, auto-approve
changed baselines, or add another standing judge layer before measuring need.

The founder-requested planning update consolidates the implementation queue in
[section 5](#5-improvement-roadmap). It does not itself waive current checks,
change product policy or dispatch messages to its owners. The accompanying
[program roadmap](vesper-program-roadmap.md) clarification reconciles its merge
rule with the already accepted central integration ownership.
Adopted operational changes should update their existing owner documents; close
or archive this research note by October 30.

## 8. Repository efficiency and a shorter delivery path

### What this additional audit measured

This pass inspected clean canonical checkouts at workspace `0a39e27362a5`,
backend `bd1a683b8656` and app `87eceee24512`, plus named lane refs and hosted
run records. Backend integration had landed by this observation; app/workspace
integration was still active. These are dated observations, not completion claims
for the three-lane merge. The proposed changes below were not implemented.

**Hosted app execution is an established bottleneck.** Two successful merge
workflow samples show:

| Run and local start time | Creation to Merge ready completion | Test command step | Dependency installation in test job |
| --- | ---: | ---: | ---: |
| [36658191461](https://github.com/fy538/travel-app/actions/runs/36658191461), September 29 at 22:05 EDT | 10m53s | 8m14s | 35s |
| [36802747792](https://github.com/fy538/travel-app/actions/runs/36802747792), September 30 at 21:47 EDT, `6b3066aa5aa1` | 8m25s | 6m45s | 28s |

The second run selected `full`: 1,289 suites and 9,178 tests passed; Jest reported
401.584 seconds. This is a broad candidate, not a sample of an isolated copy fix.
Two observations cannot establish a percentile or a general throughput trend.
They do establish that removing dependency-install time alone cannot make these
runs meet the existing five-minute objective. Concurrent job times must not be
added as elapsed developer waiting time. The in-progress/retried integration run
`36804986907` was excluded from this earlier comparison; its completed attempts
are recorded in section 9.

**The scoped path still contains substantial fixed work.** At the inspected app
revision, [merge-scope.mjs](../../travel-app/scripts/merge-scope.mjs) adds all
93 convention-test files to every nonempty related-test selection and uses two
Jest workers. This protects source-reading tests that the import graph misses,
but means scoped does not necessarily mean cheap. Both broad and scoped paths
use the shared Expo test setup.

One concrete candidate is
[tripCrownAssets.test.ts](../../travel-app/__tests__/conventions/tripCrownAssets.test.ts):
it decodes crown images, walks their pixels and invokes an expectation for each
border pixel. That suite took 15.511s in the second hosted sample;
`productStateIllustrationContract.test.ts` took 7.071s. Preserve their geometric
assertions while benchmarking aggregated border checks with useful failure
coordinates. For source/asset-only tests, trial a separate lightweight Jest
configuration that omits unrelated React Native setup. Do not assume changing
the environment annotation alone removes shared setup, or that these two suites
explain all 401 seconds.

**CI still runs overlapping static checks.** App
[merge readiness](../../travel-app/.github/workflows/merge-ready.yml) calls
`verify:fast`, which repeats lint, production typecheck, selected test typecheck,
API-boundary, schema-bridge, native-compatibility and Home-budget checks also
present in [regular CI](../../travel-app/.github/workflows/ci.yml). The duplicate
fast block took 69s and 94s in the samples above, while tests took much longer.
Removing duplication can reduce runner work and maintenance; it cannot be
credited with saving those whole durations on the critical path. Retain the
actual assertions and required-result handling when consolidating execution.
Workspace merge readiness also installs both child dependency sets before its
workspace-only selector, including for prose changes; select required inputs
before expensive setup, with explicit error handling and a safe fallback.

**The documentation lifecycle has accumulated a real backlog.** A tracked-file
inventory, counting whitespace-separated words rather than model tokens, found:

| Scope | Markdown files | Approximate words |
| --- | ---: | ---: |
| Workspace `docs/working/` | 380 | 1,925,771 |
| Workspace `docs/`, excluding archive/attic path segments | 557 | 2,153,901 |
| Backend `docs/`, same exclusion | 347 | 830,586 |
| App `docs/`, same exclusion | 257 | 389,018 |

The first row is a subset of the second. These are storage/search inventories,
not amounts automatically loaded into an agent. Backend corpus Markdown and
golden test prompts are excluded from the documentation rows. Of the workspace
working files, 359 have frontmatter status `active`; 193 have an explicit expiry
before September 30. Expiry is a review signal, not proof their content can be
deleted. The [governance checker](../../scripts/check_doc_governance.py) validates
the allowed interval between creation and expiry, but does not enforce that
today is before expiry. A green docs check therefore does not mean this backlog
has been retired.

The cold UI reading path through workspace/app instructions, the workspace
index, app Task Intake, Product Thesis, Product Model and Design Language totals
12,760 words before the surface contract and verdict protocol. That is a linked
first-read footprint, not a measured per-task token bill or a reason to remove
the product model. Make familiar, unchanged context reusable and route local
maintenance directly to its owner; reserve broader product reading for changes
that need it. Test that routing on real tasks before claiming faster execution.

**Integration batches are also large.** The inspected artifact app branch
`5d56ef5ff` differed from its main merge base in 74 files, with 7,894 inserted
and 335 deleted lines; Home `21fdb724f` differed in 157 files, with 10,976 inserted
and 797 deleted lines. Each includes generated schema and docs, and Home includes
integrated work from other lanes. The counts overlap and must not be summed as
independent output. They show why the final candidate exercises broad checks;
they do not establish that every change was unnecessarily batched.

### What the additional research supports

- **Minimal, useful agent instructions.** The February 12
  [AGENTS.md study, version 1](https://arxiv.org/html/2602.11988v1) evaluated four
  agent/model combinations on Python tasks. Generated context usually increased
  cost and slightly hurt completion; developer-written context modestly helped
  completion while increasing work. It did not evaluate Vesper, current models,
  native QA or all safety/maintainability outcomes. Our inference is to preserve
  non-obvious invariants and task routing while removing duplicated summaries and
  blanket work obligations. It does not justify deleting AGENTS.md.
- **Small changes must stay small through integration.**
  [DORA](https://dora.dev/capabilities/working-in-small-batches/) identifies
  regrouping small changes into a large downstream test/release batch as a
  failure mode. For Vesper, deliver complete backward-compatible slices against
  a recorded three-repo tuple, integrate them promptly, and distinguish code
  integration from founder-controlled feature activation. This is an operating
  recommendation, not a causal estimate of our savings.
- **Optimize existing test execution first.**
  [Jest 29.7](https://jestjs.io/docs/29.7/cli#--shard), matching our declared major,
  supports sharding and worker limits. Pilot two shards for genuinely broad
  candidates, or reduced per-suite setup, before narrowing coverage. A shard
  aggregate must require all expected shards and prove their union matches the
  original selection. Measure installation/queue overhead and runner-minutes as
  well as elapsed time. More workers are not automatically faster.
- **Dependency caches are not installed environments.**
  [GitHub setup-node](https://github.com/actions/setup-node#caching-global-packages-data)
  caches package-manager data, not `node_modules`. Existing npm cache settings
  therefore do not eliminate repeated installation. Keep compatible setup work
  together when it reduces measured latency, but avoid serializing independent
  long tests merely to save installs. The app's `postinstall` applies patches;
  any environment reuse must include those patches in its identity.
- **Lighter installation is an incremental option.**
  [uv's GitHub Actions guide](https://docs.astral.sh/uv/guides/integration/github/#using-uv-pip)
  supports installing existing requirements files and caching those inputs.
  A pinned installer pilot can retain our pip-tools lock sources; a wholesale
  dependency-manager migration is unnecessary. Backend install timing was not
  measured in this earlier pass; section 9 records the final workspace sample.
  It remains smaller than the flow-validation and app-test costs.
- **Reduce transferred data only where it is unused.**
  [actions/checkout](https://github.com/actions/checkout) supports filtered and
  sparse checkout. Our app tests already sparsely fetch workspace contracts.
  Extend that pattern where inputs are explicit. A history-light selector still
  needs the real merge base; never substitute the last commit or return an empty
  pass when history is missing. Moving files into an archive does not shrink Git
  history or prove faster clone/build time.
- **Unused-code reports are candidates for review.**
  [Knip](https://knip.dev/guides/handling-issues) documents false positives from
  unresolved/dynamic imports. A bounded app audit must account for Expo routes,
  native registration, scripts and config-driven entrypoints before removal.
  Start with one verified obsolete component/dependency family, not automatic
  deletion or a new required full-repo gate.
- **Profile compiler work before reorganizing types.**
  [TypeScript's performance guide](https://github.com/microsoft/TypeScript/wiki/Performance#extendeddiagnostics)
  provides compiler timing diagnostics. The generated app schema is about 1.8 MiB,
  but size alone does not establish a typechecking bottleneck. A local config
  probe could not run because this canonical checkout has no installed
  TypeScript package. No compiler speedup or faulty config is claimed.

### Revised implementation sequence

The findings in this pass are incorporated into the single queue in
[section 5](#5-improvement-roadmap). The completed-integration review below
superseded the initial ordering. After those CI changes landed, the October 1
research recheck in section 5 sets the current order: the next measured feedback
cost, with obsolete-assumption repairs where encountered and implementation
retirement conditional on actual maintenance burden.
Native QA and lighter review/context remain in scope. Build reuse
and other setup experiments remain conditional. Package details, statuses and
adoption checkpoints are maintained there rather than duplicated in this evidence
section.

Smaller integration batches apply throughout this sequence. A lane should own
one independently verifiable behavior through landing and leave a compact
receipt in its existing roadmap: outcome, revision tuple, evidence, remaining
dependency. A completed slice should not wait for unrelated slices merely to
produce one large combined delivery. Cross-cutting changes still need a coherent
integration checkpoint; splitting a change must not split its invariants.

The desired ordinary path is: **locate the owner → implement one behavior →
focused feedback → proportionate acceptance → one candidate preflight → land**.
Measure time to first useful feedback and accepted behavior, broad-fallback
frequency, first-attempt native success and rework. The existing ten-change pilot
is sufficient to start; another research framework or a fleet of reviewer agents
would add work before demonstrating a benefit.

### Audit reproducibility and limits

Inventory used `git ls-files` separately in each independent repo, file byte
sizes and whitespace word counts; archive exclusion was by exact path segment.
The local diagnostic is `/private/tmp/vesper-efficiency-inventory-20260930.json`;
it includes the general tracked inventory, not every derived table above.
Working expiry/status counts came from frontmatter at the same workspace HEAD.
Lane counts used each lane's merge base with main and `git diff --numstat`,
excluding binary line totals. No cleanup or history rewriting was performed.

Hosted evidence was read with `gh run view <run-id> --repo fy538/travel-app
--json conclusion,createdAt,updatedAt,jobs` and, for the second sample,
`gh run view 36802747792 --repo fy538/travel-app --job 110180576312 --log`,
extracting selection mode, slow-suite lines and the test summary. GitHub's
second-resolution job timestamps and Jest's reported execution duration are
different measurements. These reads did not trigger, rerun or modify workflows.
No product, native, dependency-install or compiler benchmark was executed here.

## 9. Completed integration review

### Verified landing and evidence boundaries

The September 30 integration completed at 22:41 EDT with required checks passing:
[workspace PR 37](https://github.com/fy538/travel-workspace/pull/37),
[backend PR 238](https://github.com/fy538/travel-agent/pull/238), and
[app PR 208](https://github.com/fy538/travel-app/pull/208). Section 5 records their
merge commits. Workspace candidate `15da6d37762e` tested backend
`33a000e97ed4` and app `21fdb724ff71`; those child candidates became ancestors
of the respective main merge commits with identical trees. No bypass or
feature activation followed. The working-document edits here are not runtime
implementation or a claim of native visual acceptance.

| Measurement | Observed result | Boundary |
| --- | ---: | --- |
| Final merge turn | 73m04s, September 30 21:29:27–22:42:31 EDT | Includes repair, coordination and waiting; excludes earlier integration preparation |
| First combined candidate publication to workspace merge | About 55m | Includes subsequent candidate changes, not one unchanged CI run |
| Final workspace required job | 23m18s | Includes setup, contracts, flow validation and journeys |
| Flow validation within that job | 16m55s, about 73% | Semantic parsing of 408 non-config flow files, not device execution |
| Final app candidate, first test attempt | 9m45s job; 8m36s command step | Failed two tests; 1,287 suites passed |
| Same app candidate, successful retry | 8m34s job; 7m17s command step; 434.846s Jest execution | All 1,289 suites and 9,178 tests passed; no source change between attempts |

Hosted sources: [workspace final run](https://github.com/fy538/travel-workspace/actions/runs/36805139539),
[earlier workspace failure](https://github.com/fy538/travel-workspace/actions/runs/36669218050),
and [app run with both attempts](https://github.com/fy538/travel-app/actions/runs/36804986907).
The earlier workspace job took 22m48s and failed at Golden path QA after 17m12s
of flow parsing; the final job took 23m18s and passed. This establishes repaired
infrastructure and successful landing, not reduced gate latency or a general
productivity trend.

The final workspace job spent 60s installing backend dependencies and 35s
installing frontend dependencies. Disposable journey migrations took 6s and
Golden path QA took 28s. These observations favor early prerequisite checks and
parallel flow validation over dependency-manager replacement. They are one
hosted sample, not stable percentiles.

Do not sum overlapping durations. App retry succeeded before the workspace
finished, so eliminating that retry alone would not have advanced the final
three-repository merge in this run. It still consumed runner work and diagnosis.
A faster app path becomes material once the larger workspace bottleneck is
removed.

### What improved and what remains inefficient

The private child checkouts and disposable database path worked; all committed
lane work landed while concurrent edits were preserved. Later local verification
used bounded deltas, and the hosted retry reran failed jobs rather than successful
static jobs. These are real control and reliability improvements.

Late contract, fixture-type, generated-status, design-governance and security
findings still required repair after publication. Two small app follow-ups within
four minutes superseded running checks. Earlier source-location assertions broke
after a valid extraction, illustrating why implementation-text tests need
review against the behavior they are intended to protect. Some checks caught
real issues; this is not evidence for deleting tests indiscriminately.

The final turn's retrieved trace contained 34 commentary updates and 63 command
bundles reading status or log tails. Those counts are not elapsed overhead or
token-cost measurements; they support simplifying coordination, not a quantified
savings claim. Fix the critical path and candidate readiness before introducing
another monitoring layer.

### Research implications and next execution

The [syntax wrapper](../../travel-app/scripts/maestro/check-syntax.sh) invokes
the CLI once per file and defaults to serial execution because shared logger
state has raced. Upstream's pinned command takes one file. Package 3C therefore
starts with isolated matrix jobs and unchanged coverage, not unsupported batch
arguments or unvalidated same-environment parallelism.

[Jest sharding](https://jestjs.io/docs/29.7/cli#--shard) and
[GitHub matrix jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
support the proposed partitions; neither source establishes a Vesper speedup.
[GitHub failed-job reruns](https://cli.github.com/manual/gh_run_rerun) support
bounded recovery. [pytest's flakiness guidance](https://docs.pytest.org/en/stable/explanation/flaky.html)
explains why reruns do not replace diagnosis. The specific invite readiness
hypothesis and unresolved Place timeout remain explicit in Package 3A.

[DORA's small-batch guidance](https://dora.dev/capabilities/working-in-small-batches/)
warns against recombining independently completed work into a large downstream
batch. For this roadmap, land useful compatible slices promptly, but finish a
repair batch's inexpensive checks before publishing another candidate. This is
engineering cadence, not a narrower product vision or permission to split
cross-repository invariants.

Section 5 remains the only execution queue. The October 1 planning update
supersedes this review's earlier ordering: validate the next measured feedback
bottleneck, continuing the existing ten-change pilot and unresolved native QA.
Repair conflicting assumptions when encountered; an obsolete implementation
family needs demonstrated maintenance burden before retirement. Package numbers
remain stable references. Landed tooling and earlier receipts retain their exact
boundaries; Git cleanup and successful tests do not establish an overall speed
gain. The sharding experiment is merged and passed its final run, while default
adoption remains conditional on comparable elapsed and runner-time evidence.
No new dashboard, standing agent fleet or broad test-deletion project is needed.

### Reproducing the integration measurements

Read workflow job and step timestamps with `gh run view <id> --repo <repo>
--json jobs`. Read app attempt 1 separately through
`gh api repos/fy538/travel-app/actions/runs/36804986907/attempts/1/jobs`;
the latest run view alone reports the successful retry's test job. Jest duration
and totals come from that job's log. Count the same recursive non-config YAML
inventory as the syntax wrapper at app `21fdb724f`.

The turn-duration boundary comes from Orchestration turn
`01a0f514-aa53-7fd3-acab-b990a88861ab`, not the long-lived workspace PR's
creation date. User-facing times above are America/New_York; GitHub timestamps
are UTC. This review read existing results; it did not execute a speed benchmark.

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
reads. This research did not execute product suites, a simulator or a live-model
comparison. The third pass added read-only hosted-CI timing inspection as described
above; it did not independently verify all branch protection settings.
Documentation-check results belong to the
delivery receipt for this note, not to product readiness.
