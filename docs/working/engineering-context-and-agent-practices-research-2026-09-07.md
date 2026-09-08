---
doc_type: working
status: active
owner: founder / engineering
created: 2026-09-07
expires: 2026-10-07
why_new: Reassesses engineering instruction design using research through September 7 and a fresh three-repository audit; the August architecture report retains its distinct A0-A6 experiment specifications and historical results.
supersedes: []
related:
  - codebase-architecture-and-agent-velocity-research-2026-08-11.md
---

# Engineering context and agent practices: September 2026 research

**Research cutoff:** September 7, 2026. **Audience:** Vesper founder and engineering agents.
**Decision:** Which repository instructions and supporting engineering mechanisms should change to improve speed, reliability, and context?
**Status:** Research and proposed edits, not adopted instructions or a new execution backlog. The [workspace index](../README.md) identifies current product, execution, and evidence authorities.

## Executive answer

**Updated after three research and inspection passes on September 7.** The highest-value next step is to restore working, correctly configured CI and reproducible setup, then make verification trustworthy and instructions easier to navigate. Vesper has strong foundations in generated contracts, architecture checks, risk-based intake, and structured evidence. The third pass verified live GitHub configuration and found that workspace/backend Actions is disabled and their required check names do not match their primary workflows. Local probes also found fresh-bootstrap and checker-failure defects.

I recommend this order:

1. **Restore the actual delivery path:** reconcile GitHub Actions settings and required checks per repository; repair bootstrap, environment prerequisites, and change-trigger coverage.
2. **Repair misleading verification paths:** isolate offline setup, preserve checker/eval failures, protect visual judgment provenance, and bind evidence to the intended revisions and environment.
3. **Correct and consolidate instructions:** accurate transaction APIs, commands, dependency/hook setup, paths, and generated-type ownership; one shared source with verified tool-specific discovery. These factual repairs need no productivity experiment.
4. **Make context and review task-dependent:** locate the owning contract, representative implementation, and relevant proof. Diagnose retrieval, implementation, environment, and validation failures separately.
5. **Measure accepted delivery across successive changes:** correctness, human review and repair, elapsed time, and cost. Validate important checkers against legitimate cases, representative violations, and execution failures; avoid test-count or blanket mutation-score targets.

The combined finding is that editing AGENTS.md alone cannot repair a test fixture that writes before its isolation guard, a passing eval command with failed checks, or a visual judgment carried across a changed design reference. The detailed findings below identify the existing owner and a bounded repair for each.

These are evidence-informed recommendations, not a demonstrated productivity gain for this codebase. The public research does not establish a universal AGENTS.md template, line limit, or AI productivity multiplier.

## What the current evidence actually says

### Instruction files can change behavior without improving correctness

The June 23 revision of Gloaguen et al. tested four agent/model configurations on 300 SWE-bench Lite tasks and 138 CTXbench tasks. Neither generated nor developer-authored files significantly changed success relative to no file; developer-authored files did outperform generated ones. Generated files increased inference cost by about 20–23%. The study also found no clear general relationship between file length and outcomes. This supersedes simplistic February headlines about instructions universally hurting success. The evaluation is Python-focused and measures test-defined resolution, not all maintainability, security, or product requirements. [Gloaguen et al., revised June 23, 2026](https://arxiv.org/html/2602.11988v2)

Positive evidence also exists, but measures different things. Lulla et al. compared 124 small PR tasks across ten repositories using GPT-5.2-Codex. Median runtime fell 28.64% and output tokens 16.58% with instructions. Tasks were limited to 100 changed lines and five files; only 50 outputs received a manual sanity check. This is evidence of efficiency in that setting, not proof of equal correctness or shorter end-to-end delivery. [Lulla et al., January 28, 2026](https://arxiv.org/html/2601.20404v1)

A June study refined guidance from synthetic bug-fix probes. Across four Qwen trials on 500 SWE-bench Verified tasks, resolution rose from 25.5% without guidance to 33.0% with refined guidance. However, it used a custom scaffold and restricted 16k context; self-tuning hurt another model, and transferring guidance across models performed particularly poorly. Failure-informed tuning is worth testing; the reported gain should not be transferred to today's frontier agents or our repositories. [Shepard and Albrecht, revised June 19, 2026](https://arxiv.org/html/2606.20512v2)

A July ablation across three repositories and 15–17 tasks also found no significant correctness effect. Its 288 runs do not erase the small number of independent task clusters, and selective retrieval differed in both content and delivery. This further weakens claims that one presentation strategy is universally best. [Khatri, July 28, 2026](https://arxiv.org/html/2607.27250v1)

**Our inference:** preserve specific, non-obvious constraints and accurate commands. Test changes to mandatory reading, workflow, and review effort. Reducing bytes alone is not a sufficient objective.

### The promising practice is engineering the execution environment

OpenAI's February account describes a small AGENTS.md navigation layer backed by repository knowledge, mechanically enforced architecture boundaries, actionable check failures, and application/observability access. Its reported speedup is a team estimate from one internal product, not a controlled comparison. The transferable ideas are inspectable state and quick correction loops; its minimal merge gates are an environment-specific tradeoff. [Ryan Lopopolo / OpenAI, February 11, 2026](https://openai.com/index/harness-engineering/)

Anthropic's March account adds a useful qualification: parts of an agent workflow became unnecessary as the model improved. The team removed components one at a time and inspected the effect. A separate evaluator helped at the edge of model capability, but added overhead on easier tasks. This supports selective review and periodic simplification, rather than making multiple agents or repeated review rounds mandatory. [Prithvi Rajasekaran / Anthropic, March 24, 2026](https://www.anthropic.com/engineering/harness-design-long-running-apps)

For behavioral evaluations, deterministic checks, calibrated model judgments, and human review establish different kinds of evidence. Capability discovery and regression protection also need different task sets. [Anthropic, January 9, 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Our inference:** improving a failing checker, fixture, reproduction path, or ownership boundary can remove more future work than adding another instruction paragraph. Use independent review where the change's risk justifies it; a second agent's approval is not execution evidence.

### Productivity is an outcome of the whole delivery process

DORA's 2025 report frames AI as amplifying existing organizational conditions. It reports associations with increased throughput and instability; this is survey research, not randomized evidence. Its published errata also correct a stability/instability typo in the platform discussion. The latest annual report located at this cutoff is 2025; 2026 supplementary guidance is not a new annual sample. [DORA 2025 report](https://dora.dev/research/2025/dora-report/), [official errata, updated November 24, 2025](https://dora.dev/research/2025/errata/), [research archive](https://dora.dev/research/)

Two randomized findings illustrate why context matters. METR's 2025 trial found 16 experienced contributors took 19% longer on 246 familiar-repository tasks when allowed contemporary AI tools, despite believing they benefited. A separate three-company study of 4,867 developers estimated 26.08% more completed tasks with coding-assistant access. The populations, tools, outcomes, and work differ; neither estimates September 2026 agent effectiveness here. The latter publication summary was available, but its linked full preprint was not inspected successfully. [METR, July 10, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [Cui et al. / Microsoft Research, June 2025](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/)

METR's February 2026 follow-up does not establish a clean reversal: both reported confidence intervals cross zero, and participation, task selection, and concurrent-agent timing complicate interpretation. Its May survey of 349 technical workers reports perceived value gains of 1.4–2× and speed gains of 3×, but uses a convenience sample and self-reported counterfactuals. These are separate evidence classes. [METR, February 24, 2026](https://metr.org/blog/2026-02-24-uplift-update/), [METR, May 11, 2026](https://metr.org/blog/2026-05-11-ai-usage-survey/)

Review capacity deserves explicit measurement. A July observational preprint covering 802 developers and 196,212 PRs at one company reports 2.09× throughput alongside roughly doubled reviewer load. The authors do not claim exact causal attribution; steady revert rates are not comprehensive quality evidence. Only its abstract and submission record were inspected for this report. [He et al., July 2, 2026](https://arxiv.org/abs/2607.01904)

**Our inference:** optimize time to an accepted useful change. Include human review, repair, waiting, and later regressions. PR volume, generated lines, and token consumption are diagnostic inputs, not the objective.

### Instructions need maintenance and verified discovery

An August preprint examined instruction histories across 1,867 repositories; among multiversion repositories, growth was more common than shrinkage. Its controlled maintenance experiments suggest recording a rule's rationale can reduce unnecessary accumulation, but they do not establish coding-productivity gains. Its observational design and instruction-matching limitations also constrain causal claims. [Chakrabarti, August 11, 2026](https://arxiv.org/html/2608.11095v1)

Tool loading differs. Codex builds an instruction chain from the project root toward the working directory, takes at most one recognized file per directory, and has a default combined 32 KiB limit. Its documented discovery does not automatically make arbitrary .claude/rules files shared instructions. For independent Git repositories, verify the actual launch root rather than assuming the parent workspace is included. [Official OpenAI documentation, accessed September 7, 2026](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Claude's official documentation recommends importing AGENTS.md from CLAUDE.md when sharing guidance. Imports load eagerly; moving a long manual behind an import does not reduce startup context. Path-specific loading and ordinary navigational links serve different purposes. The documentation's suggested file-size target is vendor guidance, not a scientifically established optimum. [Claude Code documentation, accessed September 7, 2026](https://code.claude.com/docs/en/memory)

**Our inference:** maintain a shared rule once, verify it loads in the entry points we actually use, and keep long specialist procedures outside the standing instructions.

### What the second research pass adds

**Diagnose context acquisition before buying more context machinery.** Agent Retrieval Bench contains 427 cases across 25 repositories, including cases with no relevant repository file. Its 45-task controlled seed pilot found lexical and embedding context can help file selection, with method rankings depending on task and budget. It measured context acquisition, used one trajectory per task/arm, and did not test completed patches. This supports keeping ordinary lexical search as a baseline and evaluating any index against actual task outcomes. [Qin and Xie, Agent Retrieval Bench, July 27, 2026](https://arxiv.org/html/2607.24882v1)

ContextBench provides 1,136 issues across 66 repositories and distinguishes retrieved context from the final context submitted for patch generation. More exploration does not automatically mean better localization or repair. Its “utilized” context is observable submitted material, not a direct measurement of internal reasoning. **Our proposed diagnosis:** required information absent; present but not found; found but implemented incorrectly; or implementation inadequately verified. Each calls for a different intervention. [Li et al., ContextBench, revised February 11, 2026](https://arxiv.org/html/2602.05892v3)

**Evaluate the evaluator and the environment.** A July study found ground-truth exposure, specification problems, and tool failures in agent benchmarks. Automated transcript scanners helped locate problems, but performance varied substantially: the reported tool-failure F1 was only 0.27 for GPT-5.4. An unflagged trace is therefore weak assurance. Sample successful and failed runs for human inspection; do not replace acceptance evidence with reviewer-model consensus. [Mohl et al., Automated Transcript Analysis, July 29, 2026](https://arxiv.org/html/2607.27518v1)

Anthropic varied resources while holding the model and harness constant and observed a six-percentage-point Terminal-Bench gap between its least- and most-resourced settings. This is a particular experiment, not a universal correction factor. **Our implication:** record CPU/RAM limits, concurrency, timeouts, dependencies, and relevant service state when comparing instructions. Simultaneous work in a dirty shared checkout is useful engineering activity but an uncontrolled performance experiment. [Segato / Anthropic, Quantifying infrastructure noise, February 5, 2026](https://www.anthropic.com/engineering/infrastructure-noise)

**Measure maintenance instead of assuming AI necessarily increases it.** Sawada et al. compared 508 agent-created and 508 human-created files across 100 repositories over six months. Agent files received fewer and smaller later changes; humans performed most maintenance. The study is observational, uses early agent data, excludes Codex, and does not match away task complexity or usage. Fewer changes can mean stability, avoidance, or low use. Track repair effort and later defects here; neither presumed technical debt nor presumed stability is established. [Sawada et al., revised May 9, 2026](https://arxiv.org/html/2605.06464v2)

Needle in the Repo offers a useful evaluation design: combine functional checks with architectural/structural checks and follow-on changes. Its 21 small authored C++ repositories and restricted agent tools limit transfer. An inconsistency between its headline structural-failure count and detailed results prevents using that headline rate here. We retain the design idea, not a prevalence estimate. [Zhu et al., March 29, 2026](https://arxiv.org/html/2603.27745v1)

**Instruction maintenance is normal; frequent editing is not itself a success metric.** The August revision of Agent READMEs describes 2,303 context files from 1,925 repositories and a qualitative edit sample dominated by substantive changes. It is descriptive, not evidence that editing more often improves delivery. Keep rule rationale and ownership, review it when its implementation changes, and remove duplication deliberately. [Chatlatanagulchai et al., revised August 9, 2026](https://arxiv.org/html/2511.12884v2)

## What the codebase audit found

The inspection covered root and child instruction files, task intake and onboarding, contract generation, CI/Make targets, architecture checkers, verification routing, worktree scripts, documentation governance, and the journey evidence model. It sampled implementation and tests at contract boundaries. It is not an exhaustive product-code review.

### Strengths to preserve

- **Generated contract chain:** [sync-types.sh](../../scripts/sync-types.sh) exports the full backend schema offline, derives the mobile projection, and generates app types. [Reliability CI](../../.github/workflows/reliability.yml) checks immutable child refs and schema freshness for the pinned tuple. The second pass below qualifies which revision that certifies.
- **Executable architecture boundaries:** backend import, lazy-import, and SCC checks already exist. They all passed during this audit. The SCC check scanned 1,848 modules and found the permitted four-module cycle; this is an observed snapshot, not a new architecture target.
- **Frontend boundary enforcement:** [check-api-boundaries.mjs](../../travel-app/scripts/check-api-boundaries.mjs) supports the existing data-layer boundary; [package.json](../../travel-app/package.json) exposes verification tiers and additional ownership checks. Their presence was inspected; the frontend suites were not run.
- **Risk-based validation:** both [backend Task Intake](../../travel-agent/docs/operations/Task%20Intake.md) and [frontend Task Intake](../../travel-app/docs/Task%20Intake.md) already classify changes by contract, behavior, streaming, and architecture risk.
- **Evidence with defined limits:** the [journey evidence model](../journeys/EVIDENCE_MODEL.md) distinguishes contract, database, device, staging, physical, and AI-eval evidence. The app's [AGENTS.md](../../travel-app/AGENTS.md) already rejects treating a dry run or typecheck as visual proof.

### Concrete gaps and their consequences

| Finding | Local evidence | Recommended response |
|---|---|---|
| Root instructions name missing paths and an old absolute workspace location. | [Root AGENTS.md](../../AGENTS.md) uses Travel Agent/ and Travel App/; this checkout contains travel-agent/ and travel-app/. | Correct literal paths; describe commands relative to the verified workspace root. Retain display names where useful. |
| The same operation has contradictory setup instructions. | Root AGENTS.md, root CLAUDE.md Quick Reference, and the Makefile help text describe type sync as requiring a running backend; [the script](../../scripts/sync-types.sh) defaults to offline export. | Explain offline default, snapshot-only mode, and explicit live mode once. |
| Generated-type ownership is contradicted by older advice. | [Backend CLAUDE.md](../../travel-agent/CLAUDE.md) calls schema.gen.ts a hand-bridge. Its [actual header](../../travel-app/utils/api/schema.gen.ts) says generated; [the generator](../../travel-app/scripts/generate-api-types-snapshot.mjs) uses openapi-typescript and defaults to openapi.app.json. | Replace the obsolete warning while preserving the requirement to use workspace sync. Correct app docs that say snapshot generation reads the full schema. |
| Broad testing mandates conflict with risk-based intake and current commands. | Backend AGENTS.md and CLAUDE.md say run the entire unfiltered suite after code changes. Root AGENTS.md calls make test-backend offline, while [Makefile](../../Makefile) configures it as a local-Postgres canary. | Route iterative validation through intake; name prerequisites accurately; keep required integration and pre-push gates explicit. |
| Specialist rules are unevenly discoverable across tools. | Useful PATCH semantics live in [patch-routes.md](../../travel-agent/.claude/rules/patch-routes.md); other database and test rules live under .claude/rules. | Add explicit path/task routing from shared instructions. Audit rule scoping against the installed tool's documented format. |
| Startup reading repeats and expands. | App CLAUDE.md → [Kickoff Prompt](../../travel-app/docs/Agent%20Kickoff%20Prompt.md) → [Onboarding](../../travel-app/docs/Onboarding.md) → Task Intake repeats broad reading. Six root/child instruction files total 62,511 bytes at inspection. | Turn startup guidance into one conditional map. This byte count is not automatic prompt size or measured latency. |
| Worktree isolation can be undermined by fixed generator paths. | [new-worktree.sh](../../scripts/new-worktree.sh) creates child lanes; sync-types.sh still targets literal travel-agent/ and travel-app/ beneath its own workspace. | Record all three checkout paths and revisions before generation. A child-only lane is not automatically a coordinated cross-repo workspace. |
| Old research describes repaired tooling as unfinished. | August A2 describes incomplete repo discovery and swallowed recorder exits. Current [router](../../scripts/verify_changed.py) reads all three repos, and [recorder](../../scripts/measure_verification.py) propagates failures. Their 32 focused tests passed; the second pass found an additional inherited-Git-environment gap. | Update status from present code and evidence before scheduling repairs. Keep performance validation separate from functional repair. |
| The documentation gate is currently red in the shared working tree. | make docs-check failed before this report was added: metadata/child governance, 45 unclassified docs, canon budget, generated release/status, and one living-link issue. | Triage through existing owners; recover an actionable baseline without indiscriminate exemptions or bulk status promotion. These are observations of a dirty, changing checkout, not claims about a clean main CI run. |

A further maintenance detail matters: root CLAUDE.md treats committed Git state as the whole current truth. In this shared workspace, the branch, worktrees, staged changes, unstaged changes, and generated outputs also matter. A commit identifies a baseline; it does not describe another session's uncommitted work.

## Second-pass inspection: trace the instruction through the implementation

This pass followed the chain **instruction → command → code path → checker → claimed evidence**. “Reproduced” below means an isolated local probe of actual code, with synthetic data or stubbed I/O. It does not mean a production incident was observed. Static findings are identified separately.

### Backend: transaction ownership and test isolation

**The database rule contradicts the transaction API.** [Backend AGENTS.md](../../travel-agent/AGENTS.md), [shared-db.md](../../travel-agent/.claude/rules/shared-db.md), and [core FEATURE.md](../../travel-agent/backend/core/FEATURE.md) prescribe get_connection for all access. [engine.py](../../travel-agent/backend/core/db/engine.py) reserves it for reads and supplies get_tx for writes, committing before registered callbacks execute. The enforced [transaction ratchet](../../travel-agent/scripts/check_get_tx_ratchet.py) currently reports zero manual commit sites in its production scope. Following the older instruction can introduce a ratchet violation or an uncommitted write. This is a direct source contradiction, not a speculative style preference.

Proposed replacement in the existing database owner, routed from backend AGENTS.md:

~~~markdown
Use get_connection / get_async_connection for reads and get_tx /
get_async_tx for writes. Preserve caller-owned transaction boundaries and
post-commit effects. Before changing transaction lifecycle behavior, inspect
backend/core/db/engine.py and tests/core/test_db_engine.py.
~~~

**Offline marker selection does not isolate fixture setup.** [tests/conftest.py](../../travel-agent/tests/conftest.py), lines 171–278, defines autouse cleanup that checks whether the configured database is reachable, deletes test-pattern rows, updates itinerary references, and commits. The undeclared-Postgres guard explicitly depends on that cleanup and starts afterward. This contradicts the side-effect-free interpretation of [tests.md](../../travel-agent/.claude/rules/tests.md). No configured database was contacted during this inspection; production reachability was not established.

Repair the fixture and its environment contract together: offline setup must attempt no real database access; DB cleanup must require an explicitly selected disposable test target. Merely editing the marker command does not fix this. Acceptance should include a stubbed database factory that fails if an offline test's setup touches it, plus bounded disposable-database cleanup tests.

**The flaky-test quarantine can absorb a new deterministic regression.** [flaky_order_baseline.txt](../../travel-agent/tests/flaky_order_baseline.txt) contains whole-file and class prefixes, while conftest applies xfail(strict=False) to every matching node. An isolated AST probe gave a fabricated new test in test_error_handlers.py that nonblocking mark. The baseline's stated “only shrink” rule cannot prevent this implicit expansion. Narrow the quarantine to justified cases, provide explicit unquarantined focused proof, and retain an owner/removal condition. A blanket strict-XPASS change would not address the underlying issue.

### Behavioral and frontend checks: what a pass actually establishes

**The generic eval workflow has two different command defects.** [eval.yml](../../travel-agent/.github/workflows/eval.yml) omits --fail-on-checks from concierge and retrieval invocations. [The CLI](../../travel-agent/tools/eval/cli.py) intentionally returns nonzero for failed checks only with that option; [its existing tests](../../travel-agent/tests/eval/test_cli_run_gate.py) document the default. Planning and research invocations also omit both required selectors, --config and --all, so their code path exits before scenarios run. This is static command-to-implementation evidence; no live eval was run. Existing [live](../../travel-agent/.github/workflows/ai-live-canary.yml) and [red-team](../../travel-agent/.github/workflows/ai-redteam-canary.yml) canaries demonstrate the correct selector and failure behavior. Repair the generic workflow and name exploratory versus acceptance commands in Task Intake.

**Visual auto-carry can attach a new design reference to an old judgment.** [refresh-stale.mjs](../../travel-app/scripts/design-alignment/refresh-stale.mjs), lines 136–166 and 248 onward, checks app screenshot hashes, copies prior gates/assertions, then substitutes the current canon hash and capture time. The probe held app hashes constant and changed old-canon to new-canon. Actual exported functions produced a carried verdict with unchanged intent passes and new provenance; the actual surface validator accepted it. No screenshot or committed verdict was written. This demonstrates a false-freshness path, not misuse in a specific historical receipt.

The visual tooling and [verdict protocol](../../travel-app/docs/surfaces/_agent-verdict-protocol.md) must agree that unchanged app pixels alone do not establish unchanged design intent. Carry only the judgments whose required inputs are unchanged; preserve last-judged provenance separately from last-captured provenance. Changes to design references, contracts, doctrine, or relevant data context require the applicable re-judgment.

**Multiple captures of one persona lose regression identity.** [diffVerdicts](../../travel-app/scripts/polish-qa/verdict-schema.mjs) keys by persona alone; later captures overwrite earlier ones. The supported vesper-chat input includes several states for the same persona. A two-capture probe introduced visual/spacing failures in the first capture, left the last unchanged, and retained an already-mixed overall status. The real diff returned no regressions. Individual verdict validation can still show the failure; the lost evidence is its change over time. Use a shared persona-plus-capture identity across comparison and recording, with this case as a regression test.

**Mock UI has a direct notification transport path outside the advertised boundary.** [LeaveByHintStrip](../../travel-app/components/trip/LeaveByHintStrip.tsx) and [TripMapStopPeekCard](../../travel-app/components/trip-map/TripMapStopPeekCard.tsx) call standalone notification exports without a mock guard. [notifications.ts](../../travel-app/utils/api/notifications.ts) performs authenticated fetch and explicitly says these calls are never mocked. The current [API-boundary checker](../../travel-app/scripts/check-api-boundaries.mjs) recognizes the api binding, not these transport exports, and passed. Executing the actual transpiled notification module with mock mode enabled and stubbed fetch recorded one POST. No real network or account mutation occurred. PushRegistrar has its own mock guard and is excluded from this finding. Put these UI writes behind the existing data layer and mock/real selection, and test that mock mode cannot reach real transport.

**Two command labels overstate their local/CI coverage.** [Mock vs Real Parity.md](../../travel-app/docs/Mock%20vs%20Real%20Parity.md) says qa:parity includes backend contracts; [mock-real-parity.sh](../../travel-app/scripts/mock-real-parity.sh) runs TypeScript and six offline frontend test files. CI separately invokes qa:logic, so this is not a claim that CI lacks backend tests. Separately, schema-bridge is in [local verify:fast](../../travel-app/package.json) and [workspace contract-check](../../scripts/contract-check.sh), but is absent from the app's enumerated [PR CI checks](../../travel-app/.github/workflows/ci.yml). Describe command coverage precisely and put intended PR protections in the PR workflow. The bridge checker currently passes; this is an enforcement-timing gap.

### Workspace: revision identity, isolation, and landing

**A child-triggered reliability run tests the lock file, not necessarily the triggering child commit.** [reliability.yml](../../.github/workflows/reliability.yml) prints source_sha but checks out [locked child revisions](../child-repos.ci-lock.json). Those pins resolve to July 17 and July 19 commits at inspection. A dispatch therefore requests a rerun of that tuple; it cannot itself certify the triggering revision. This is workflow inspection, not a claim about a remote green run or branch-protection configuration. Keep immutable pins, but explicitly assemble and report the intended workspace/backend/frontend candidate tuple and identify trigger-versus-tested mismatches. Do not replace reproducibility with floating latest branches.

**Git environment can misidentify both children as the workspace.** [verify_changed.py](../../scripts/verify_changed.py) and [measure_verification.py](../../scripts/measure_verification.py) change cwd for Git calls without clearing inherited repository-selection variables. Synthetic repositories had distinct child HEADs in the control; setting GIT_DIR to the synthetic workspace made both tools resolve the workspace HEAD for both children. This qualifies the first pass: normal three-repo discovery and exit propagation are repaired, while this hook-environment case remains. [check_child_doc_governance.py](../../scripts/check_child_doc_governance.py) already clears the relevant variables. Git's official hook documentation explicitly requires clearing local Git environment when addressing a foreign repository. Reuse a tested resolver and add this negative case. [Git githooks documentation, accessed September 7](https://git-scm.com/docs/githooks)

**Worktree scripts reject valid linked checkouts and landing lacks an explicit coordinated pre-push gate.** In synthetic linked worktrees, Git recognized the repositories, but [doctor.sh](../../scripts/doctor.sh) rejected the workspace and [new-worktree.sh](../../scripts/new-worktree.sh) rejected child repos because they require .git to be a directory. Linked worktrees legitimately use a .git file. [land-worktree.sh](../../scripts/land-worktree.sh) repeats this check, pushes children, and only afterward suggests make certify-fast. It relies on installed repo hooks; the inspected frontend checkout had no installed pre-push hook. No fetch, push, landing, or remote inspection was performed. Resolve repositories with Git, bind generation to the intended child lanes, and execute the applicable coordinated gate before landing effects. [Git worktree documentation, accessed September 7](https://git-scm.com/docs/git-worktree)

### Instruction discovery and checker credibility

**Audit the complete instruction surface.** Root [.claude/rules/cross-repo.md](../../.claude/rules/cross-repo.md) and [sync-types command](../../.claude/commands/sync-types.md) repeat obsolete paths and full-schema-only generation claims. Six backend .claude/rules files use globs frontmatter; official Claude rules use paths, and rules without paths load unconditionally. The frontend design-system rule already uses paths. This is a mismatch with documented semantics; no fresh Claude session was launched to observe the loaded instruction set. [Claude memory documentation, accessed September 7](https://code.claude.com/docs/en/memory)

The tracked [.codex/hooks.json](../../.codex/hooks.json) runs relative child Git logs on every prompt. Running that exact read-only command from the workspace produced six lines; from docs/ it produced none and exited 128 with suppressed errors. A local Claude hook uses fixed canonical paths, which can describe a different lane. Actual hook enablement/trust was not verified. The official Codex hook documentation says commands run in the session cwd. Resolve the actual lane before orientation and report labeled branches, revisions, and dirty state; avoid injecting misleading or irrelevant logs each turn. [Official OpenAI hooks documentation, accessed September 7](https://learn.chatgpt.com/docs/hooks)

The [verify-finding command](../../.claude/commands/verify-finding.md) always requests three skeptics, maps uncertainty to refuted, and uses majority vote. Replace that decision model with supported / refuted / unresolved, concrete counterevidence, and reproduction where possible. Keep independent review proportional to risk. This command was inspected, not invoked; the research delegation used here had distinct research questions.

**Checker registration and checker scope need their own evidence.** The backend [registration checker](../../travel-agent/scripts/check_guard_registration.py) accepted a comment-only TODO reference as “wired” in an isolated probe. Its [import checker](../../travel-agent/scripts/check_imports.py) detected one prohibited absolute-import spelling but missed equivalent namespace/relative spellings. No existing forbidden imports in those alternate forms were found in the targeted search. Successful checks remain useful within their scope; presence and naming do not establish complete enforcement. Extend the current guards with positive/negative probes and verify actual command invocation, trigger, and nonzero exit propagation.

Also reconcile the [LLM rule](../../travel-agent/.claude/rules/llm-calls.md) with current structured, streaming, tool-loop, provider-adapter, and explicitly registered bypass paths in [the wrapper](../../travel-agent/backend/core/llm.py), [surface registry](../../travel-agent/backend/core/surfaces/definitions.py), and [surface checker](../../travel-agent/scripts/check_surface_keys.py). Preserve SDK bans and accounting obligations while routing agents to the correct call-shape owner. A simplistic two-function mandate can provoke unnecessary rewrites of deliberate bridges.

## Third pass: setup, actual CI enforcement, and tests that detect failures

The third pass extends the audit beyond local workflow files to authenticated, read-only GitHub settings and recent run metadata. It also checks fresh setup behavior and packaged environments. This changes the immediate priority: establish a functioning, correctly configured delivery gate before treating additional checks as protection.

### Additional research: quality of evidence and successive changes

**Evaluate changes across several tasks on the same resulting code.** SlopCodeBench's May revision contains 36 problems, 196 checkpoints, and 15 agents. Agents repeatedly extend their own prior solutions; the Python experiments measure duplication and complexity concentration. Quality-oriented prompts improved initial structural scores but did not stop later degradation and reduced strict correctness in the prompting comparison. These are author-written greenfield problems with hidden evaluation feedback and static quality proxies, not measured maintenance costs in a mature product. Our inference is to add successive-change tasks to the instruction trial, not to import its complexity thresholds into CI. [Orlanski et al., revised May 7, 2026](https://arxiv.org/html/2603.24755v2)

**More generated tests do not automatically establish better engineering.** Chen et al. changed test-writing behavior substantially across four models on 500 SWE-bench tasks each, without a statistically significant paired change in resolution rate. Nonsignificance is not equivalence, and the study does not measure retained regression protection. It challenges a test-volume mandate, not running existing tests or preserving useful regression cases. [Chen et al., revised April 9, 2026](https://arxiv.org/html/2602.07900v2)

Google's August revision provides a more useful distinction. Across 120 internal bugs in six languages, it evaluated jointly generated fixes and reproduction tests. A candidate test must fail before the fix and pass after it; stronger validation also tests it against an independent reference fix. Candidate-test presence was more informative than merely having tests, but predicted plausible fixes with only 0.44 precision in the freeform setting. Review the assertions and failure reason independently; fail-before/pass-after alone is not certification. Results depend on small patches, one model, and a proprietary environment. [Cheng et al., revised August 21, 2026](https://arxiv.org/html/2601.19066v3)

**Use targeted negative cases and mutation feedback.** A six-year Google study examined 14.7 million mutants and found associations between mutation feedback, added tests, and fewer surviving mutants. Its nonrandomized groups limit causal interpretation. Its practical approach focuses on covered changed lines and useful findings, rather than demanding a whole-repository mutation score. This supports seeded violations for our consequential checkers before making them merge gates. [Petrović et al., ICSE 2021](https://arxiv.org/html/2103.07189v1)

Test the legitimate cases too. MR-Coupler's validation reduced false alarms, but removing that validation detected 24 selected historical bugs instead of 22, while increasing false alarms from 5.50% to 9.44%. The benchmark specifically selected Java bugs amenable to this testing technique; these are not general detection rates. The transferable lesson is to measure false rejections alongside missed defects. [Xu et al., revised April 17, 2026](https://arxiv.org/html/2604.10126v2)

### GitHub configuration is a separate source of truth

At approximately **23:33 UTC on September 7**, authenticated REST reads returned the following. The account had ADMIN visibility, so these were successful settings reads, not inferences from an unavailable API. Source endpoints were actions/permissions, branches/main/protection, and rules/branches/main for each repository.

| Repository | Actions setting | Required main checks compared with its primary workflow |
|---|---|---|
| travel-workspace | Disabled | Requires the ten frontend names, including Lint, Type check, and Visual evidence contracts. Its reliability job is named Contract and golden paths. |
| travel-agent | Disabled | Requires the same ten frontend names. Its CI jobs include lint, typecheck, test, test-db, and eval-replay, rather than that frontend check set. |
| travel-app | Enabled | The ten required names match its primary CI jobs, but that workflow excludes docs-only changes. |

The branch-rules endpoint returned no active ruleset rules; legacy branch protection is present, including required review and administrator enforcement. This audit does not determine why the settings were chosen or inventory external status publishers. It establishes that the workspace/backend settings do not provide the automatic repository-workflow protection their local documentation suggests. GitHub documents repository-level Actions disabling separately from workflow definitions. [GitHub Actions settings documentation, accessed September 7](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)

Recent workflow-specific metadata reinforces the distinction. The latest returned backend CI run was still queued from August 8; workspace Reliability last ran July 11 and failed. Recent Dependabot maintenance runs are different workflows and do not certify these gates. The inspected [September 7 app CI run](https://github.com/fy538/travel-app/actions/runs/34120618861), at 6252274be7bd5b04131fd4fbaa1002fe82ca6776, failed multiple checks. Three jobs stopped at Check out travel-agent before their backend-dependent validation; the workspace dispatch was skipped. These results concern that remote revision, not the current local working tree. Checkout failure causes were not established from logs.

Repair ownership belongs in the existing [CI Plan](../reliability/CI%20Plan.md) and workflow/setup owners: choose the intended required checks per repository, restore execution prerequisites, and verify a current candidate actually runs them. Do not claim that adding YAML alone restores enforcement, or loosen protection just to clear a blocked PR. No remote settings were changed by this research.

**Docs-only changes include executable contracts.** The app's [CI filter](../../travel-app/.github/workflows/ci.yml) excludes docs/**, even though its jobs validate route-owner YAML, canon fingerprints, and committed verdict JSON there. Parsed workflow probes showed that isolated changes to route-owners.yaml, canon.fingerprint.json, or a vesper-chat verdict trigger neither primary CI nor the narrower [Design System Contracts workflow](../../travel-app/.github/workflows/design-system-contracts.yml). With the observed protection settings, required checks can remain pending and block such a PR. This is absent validation and a blocked delivery path, not a demonstrated false-green merge. Make every supported change class produce the appropriate terminal required-check outcome. [GitHub required-check semantics, accessed September 7](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)

### Fresh setup and runtime isolation

**Bootstrap produces a layout that doctor rejects.** [bootstrap-repos.sh](../../scripts/bootstrap-repos.sh) still clones into Travel Agent/ and Travel App/. Current [doctor](../../scripts/doctor.sh), dev, and Make targets require travel-agent/ and travel-app/. A copied-script probe with stubbed Git returned bootstrap success, created the two spaced-name directories, then failed doctor with travel-agent missing. This is more than stale prose: the documented fresh-start sequence fails. Repair the script, README, and [Workspace Repo Setup](../Workspace%20Repo%20Setup.md) together; verify both fresh and already-populated layouts without creating duplicate checkouts.

**The dev launcher masks an API process failure.** [dev.sh](../../scripts/dev.sh) starts prefixed background pipelines and ends with a bare wait. With all service/migration commands stubbed, the API stub exited 42; the unchanged launcher printed All services launched and exited zero. Make startup success depend on the intended process becoming ready, preserve child failure status, and test cleanup using owned synthetic processes. This probe did not start Docker, contact a database, or launch the application.

**A Git worktree is not a complete runtime environment.** The backend [Compose file](../../travel-agent/docker-compose.yml) fixes both container names and Qdrant host ports; Postgres has a shared default port. The workspace launcher fixes API port 8000 and the standard Expo entry point. The worktree creator allocates source directories and branches, not these runtime resources. Separate checkout paths therefore do not establish independent services or datasets. Docker project names support separate environments, but custom container names and shared host ports must also be handled. [Docker project naming](https://docs.docker.com/compose/how-tos/project-name/), [Compose service names](https://docs.docker.com/reference/compose-file/services/#container_name)

Extend the existing lane/setup contract to identify checkout paths, service endpoints, database/vector-store targets, and any exclusive device. Support either isolated runtime resources or an explicitly shared stack with coordinated ownership. This is a configuration finding; no actual collision was induced.

### Reproducibility includes tools and compatibility

**Backend runtime dependencies are pinned; developer tools are not equivalently locked.** [requirements-dev.txt](../../travel-agent/requirements-dev.txt) and [Makefile dependency generation](../../travel-agent/Makefile) leave ten direct developer dependencies unconstrained by runtime pins, including pytest/plugins and mypy. Fresh CI installs can therefore resolve a different check toolchain from a developer's existing environment. Preserve pip-tools and generate a developer lock layered on the runtime lock. Record versions in verification evidence. Controls worth retaining: Python 3.13 agrees across Docker/CI, runtime dependencies have exact versions, and the Ruff hook/CI pins agree. This is potential environment drift, not a reproduced dependency-resolution failure.

**The app lock is reproducible but contains an incompatible declared pair.** [package.json](../../travel-app/package.json) and [package-lock.json](../../travel-app/package-lock.json) select Reanimated 4.6.0 and Worklets 0.11.4, while Reanimated's recorded peer contract requires Worklets 0.12.x. An isolated semver check rejected the pair; the vendor's August release notes agree. [Software Mansion, August 21, 2026](https://swmansion.com/changelog/reanimated-4-6-0/)

The repo's [.npmrc](../../travel-app/.npmrc) disables peer-contract enforcement globally, and its Expo configuration excludes both packages from version validation. npm and Expo document those mechanisms. [npm configuration](https://docs.npmjs.com/cli/v11/using-npm/config/#legacy-peer-deps), [Expo package configuration](https://docs.expo.dev/versions/latest/config/package-json/)

Jest replaces the native animation runtime with stand-ins, so passing those tests would not resolve the incompatibility. Select a supported pair, regenerate the lock, add a focused compatibility check independent of broad exclusions, and validate a clean native build. The exact build/runtime failure was not tested; neither an install nor a native build was attempted.

**Hook stages and hook installation are different.** The [app hook config](../../travel-app/.pre-commit-config.yaml) documents pre-commit install, but defines pre-push-only TypeScript/dead-client checks without default_install_hook_types. The [backend setup target](../../travel-agent/Makefile) also installs only the default hook and tolerates a missing pre-commit executable. That default installs pre-commit, not pre-push. Specify both hook types and verify installation in a disposable checkout. This explains a gap in the documented setup path; it does not imply every developer lacks manually installed hooks. [Official pre-commit documentation](https://pre-commit.com/#top_level-default_install_hook_types)

### A broken checker must not produce a pass

Two additional executable probes demonstrate why checking a checker's failure path is valuable:

| Checker | Isolated result | Required repair |
|---|---|---|
| Backend [mypy_gate.sh](../../travel-agent/scripts/mypy_gate.sh), used by the Claude Stop hook | A stubbed mypy traceback with exit 2 becomes zero counted errors and exit 0. Missing mypy also skips successfully. | Classify subprocess status before applying the diagnostic baseline. Missing/crashed/configuration-failed tooling must remain unverified/error. Direct mypy in Make/CI preserves status, although backend Actions is currently disabled. |
| App [security-audit.mjs](../../travel-app/scripts/security-audit.mjs), used in CI | A stubbed npm endpoint error with parseable JSON becomes an empty vulnerability map and a success message. Malformed JSON and a normal high advisory correctly fail. | Validate the expected report shape and distinguish audit findings from endpoint/authentication/tool failures. Preserve valid expiring exceptions. |

The audit error shape is corroborated by [npm's own implementation](https://raw.githubusercontent.com/npm/cli/latest/lib/utils/audit-error.js). These probes establish possible false passes, not that a historical successful audit experienced them. No real npm audit or mypy execution occurred in the probes.

**Test the actual packaged environment.** Two static findings illustrate limits of checkout-only checks. Backend CI still health-checks Qdrant v1.17.1 with wget, whereas local Compose already records and fixes that image's lack of wget/curl; the [official image Dockerfile](https://github.com/qdrant/qdrant/blob/v1.17.1/Dockerfile) corroborates the minimal runtime. Separately, the [backend Dockerfile](../../travel-agent/Dockerfile) copies tools/dogfood but excludes tools/seed/world_foundry.py. The included [policy-activation command](../../travel-agent/tools/dogfood/content/activate_place_content_policies.py) imports a module that unconditionally requires that omitted file. The existing [deploy-config test](../../travel-agent/tests/dogfood/test_deploy_config.py) checks COPY strings, not dependency closure. Neither an image build nor container failure was observed. Validate service probes against their declared images and smoke-test supported packaged entry points without services; do not infer an API-startup defect from this operator-command finding.

### What this should change in our meta instructions

Add a short setup/verification rule to the relevant AGENTS.md and route details through existing Task Intake, setup, and CI owners:

~~~markdown
For setup or verification changes, prove the command in its intended
execution environment. Record relevant checkout and tool versions, required
services, and packaged inputs. Distinguish a defined check, an executed check,
and a required merge check. Preserve checker failure and unavailable-tool
states. For consequential checks, exercise representative valid inputs,
violations, and checker failures before relying on their result.
~~~

Do not expand this into a mandatory test suite for every documentation edit. For checker changes, the focused acceptance matrix is: legitimate input accepted; intended violation rejected; tool/configuration failure surfaced; correct revision/environment checked; relevant change classes invoke it. For behavioral repairs, add a requirement-grounded regression where useful and verify its failure reason. For instruction experiments, add a few successive changes to the same resulting code and measure human repair and review, alongside correctness and cost.

The immediate owner order is now: **CI execution/configuration → bootstrap and environment correctness → trustworthy checkers → concise instruction ownership → controlled context/review experiments.** These are proposed repairs, not adopted policy or changes to remote settings.

## The instruction design I recommend

### Keep existing authorities; assign each kind of knowledge a home

| Location | Keep here | Move or route elsewhere |
|---|---|---|
| Workspace AGENTS.md | Repository separation, real paths, cross-repo contract workflow, concurrency, validation/evidence routing. | Machine setup detail to README/runbooks; current product and schedule claims to the workspace index. |
| Child AGENTS.md | Repository-specific invariants, task-intake pointer, specialized rule map, representative entry points. | Long product narrative, operational schedules, temporary incidents, and complete onboarding sequences to existing owners. |
| CLAUDE.md in each repo | A shared-source import plus genuinely Claude-specific behavior. | Move unique shared content before replacing the file; do not discard backend Landmines, eval discipline, or lazy-import rationale. |
| Existing Task Intake docs | Change classification, relevant acceptance evidence, quick feedback versus required gates, delivery summary. | Avoid a second competing verification matrix in a new ENGINEERING.md. |
| Existing FEATURE.md / surface contracts | Ownership, relevant implementation and test entry points, domain invariants. | Keep runtime status and release certification in their existing evidence registries. |
| Existing governance/runbooks | Rule rationale, lifecycle, operating prerequisites, exceptions and repair procedures. | Keep one-off task narration out of permanent standing instructions. |

A rule deserves standing context when it prevents a plausible non-obvious failure or resolves an ambiguity that code search does not cheaply answer. A repeated deterministic violation usually deserves a test or checker with a useful repair message. A one-time environment problem usually belongs in its runbook.

For example, the PATCH guide explains absent-versus-null semantics and a legacy exception. That is valuable context because changing an apparently similar model-dump idiom can change behavior. Syntax and formatting already enforced by tooling generally do not need lengthy duplicate prose.

### Proposed workspace block

The following is proposed text to integrate into AGENTS.md after correcting its paths and reconciling overlapping sections. It is not an additional mandatory planning artifact, and it does not replace existing Git, product-authority, or release rules.

~~~markdown
## Task context and verification

1. Establish the actual workspace and child-repo paths, current branches,
   HEADs, worktrees, and dirty changes before substantive edits.
   Use an isolated lane when another session owns the same files.
2. Use docs/README.md to find the authority relevant to the task.
   Read the affected repo's instructions and Task Intake, then its owner
   contract and nearest relevant implementation/tests. Treat onboarding as
   setup guidance; expand context when the task or an explicit rule needs it.
3. State the intended behavior, owning layer, and acceptance evidence
   before changing behavior. For a small task, one sentence is sufficient.
4. Run focused checks during iteration. Preserve each task's required
   contract, integration, behavioral, and visual checks, including the
   documented make verify requirement. Verify actual enforcement separately;
   verify-changed remains experimental.
5. For API changes, run scripts/sync-types.sh from a coordinated workspace
   containing this task's travel-agent/ and travel-app/ checkouts.
   It exports offline by default. Review openapi.json, openapi.app.json,
   generated schema.gen.ts, and affected consumers together.
6. Report the checked repo revisions, environment, exact commands, and
   evidence boundary: executed, failed, blocked, unrun, or stale. Name
   quarantines and skipped checks. A mocked test, carried verdict, or
   another agent's approval proves only its stated boundary.
7. When a defect exposes missing context, update the existing owner doc
   or executable check. Preserve the failure rationale; do not append
   a permanent global rule for every local incident.
~~~

### Proposed child and tool-adapter changes

**Backend:** reconcile Task Intake with the fixture-isolation and eval findings before replacing the unconditional unfiltered-test mandate with its validation map. Retain backend CI and applicable integration gates. Add a short task-to-rule map: API PATCH changes → patch-routes.md; DB changes → shared-db.md and migrations; LLM/prompt changes → the LLM wrapper, prompt rules, and eval discipline. Preserve the privacy and contribution contracts.

**Frontend:** replace the repeated kickoff/onboarding chain with one task map. Ordinary component work needs its surface contract and targeted tests; data/adapter changes need explicitly identified offline seam checks and applicable real-backend evidence; streaming needs real-backend evidence; visible changes retain the registered visual-QA path. Move the long QA procedure to its existing protocol/runbook and link from AGENTS.md after proving the route preserves evidence requirements.

**Claude adapter:** after migrating unique shared instructions, use an actual import, not just a link:

~~~markdown
@AGENTS.md

# Claude-specific setup
Keep only behavior that depends on Claude Code here.
~~~

The import syntax is documented by Anthropic; it deduplicates ownership rather than lazily loading its target. Do not leave a reverse “read CLAUDE.md for shared rules” dependency in AGENTS.md. Verify discovery from the workspace, each child repo, and a representative worktree. Do not assume an AGENTS.md file's physical location alone guarantees inclusion in every tool.

**Authorization wording:** preserve founder review for unresolved product, authority, and architectural choices. Clarify that an already-authorized task does not require the same permission again merely because its implementation touches a named file. Do not expand an implementation request into authority to publish, deploy, or change product policy.

### Exact instruction owners to update

| Existing owner | Specific instruction change | Proof needed beyond prose |
|---|---|---|
| Workspace setup docs and CI Plan, bootstrap/dev scripts, GitHub configuration | Fresh layout, runtime ownership, actual required checks and trigger coverage. | Disposable bootstrap/startup probes; correct terminal checks on a current candidate. |
| Backend dependency/setup owners and app dependency configuration | Reproducible toolchain, supported native pairs, explicit hook installation. | Locked clean setup, compatibility validation, installed-hook verification, and appropriate native/artifact smoke. |
| Workspace AGENTS.md, root CLAUDE.md, cross-repo rule, sync-types command | One accurate path/contract workflow; actual lane identity; distinguish trigger and tested revisions. | Linked-worktree and inherited-Git-environment probes; candidate-tuple assertion. |
| Backend AGENTS.md, shared-db rule, core FEATURE.md | Read/write transaction APIs, caller ownership, after-commit effects. | Existing engine tests and zero-manual-commit ratchet. |
| Backend tests rule and Task Intake | Offline setup isolation; disposable DB prerequisite; qualified quarantine evidence. | No DB factory access during offline setup; new tests cannot inherit broad quarantine silently. |
| Backend Task Intake and eval workflow | Exact acceptance selector, model/provider policy, failing checks as nonzero exit, result artifact. | Stubbed CLI/workflow checks before any paid live run; then the required behavioral evidence. |
| App AGENTS.md, parity document, visual verdict protocol | Accurate offline/real coverage; mock transport boundary; carry conditions and last-judged provenance. | Mock transport, changed-reference carry, and same-persona multi-capture regression cases. |
| Tool adapters, scoped rules, orientation hooks, verify-finding command | Shared-source import, supported paths scoping, lane-aware orientation, unresolved review outcome. | Actual discovery from supported launch contexts; bounded read-only orientation smoke. |

These are owner edits and focused repairs, not a proposal for another permanent ENGINEERING.md, a new agent framework, or a parallel evidence registry.

## Improve the engineering loop around the files

**Make the first useful check easy to find.** DORA recommends reliable developer-owned tests and fast local/CI feedback, with ten minutes as a guidance target. Its small-batch guidance favors independently testable changes. Those are starting points for our measurements, not a reason to delete slow but necessary database, device, or behavioral evidence. [DORA test automation, updated July 17, 2025](https://dora.dev/capabilities/test-automation/), [DORA small batches, updated December 8, 2025](https://dora.dev/capabilities/working-in-small-batches/)

Reuse the existing intake docs to name the fastest detecting test and required follow-up lanes. Preserve failures and distinguish product defects, flaky checks, and missing environment prerequisites. Do not declare a full pass from a narrow green run.

**Keep changes reviewable by behavior.** Prefer one coherent outcome with its contract and verification. A cross-repo behavior change can legitimately span all three repositories; splitting its schema, client, and evidence into unrelated work would make review harder. Write review context around the trigger, resulting behavior, ownership, and evidence.

**Make reproductions inspectable.** For difficult integration defects, retain the minimal fixture, exact revisions, command, and relevant sanitized trace. Link to existing journey/visual receipts rather than inventing a competing proof format. Browser or simulator access is helpful where it tests actual behavior; it does not replace database/authority checks.

**Restore documentation trust through the existing machinery.** Use the current lifecycle, inventory, and link checks; first identify which failures are concurrent work and which are persistent baseline debt. Fix generator/owner drift at the source. Avoid adding another catalog that also needs maintenance. If repeated friction is traceable to the admission workflow itself, improve that workflow with evidence.

**Review costly rules when the environment changes.** Record why a rule exists, its owner, and the check or incident that supports it in the appropriate existing document. Reconsider obsolete rules after the model, tooling, or relevant architecture changes. Age alone is not evidence a privacy or integrity rule is safe to remove.

## How to know whether the changes helped

Keep factual corrections separate from workflow experiments. Correcting an invalid directory or an obsolete claim does not require a productivity RCT. Changing required reading, validation depth, or review structure does need an evidence-based adoption decision.

Reuse the August report's [A0–A6 specifications](codebase-architecture-and-agent-velocity-research-2026-08-11.md) where they remain applicable, after reconciling their historical Demo Program status with the [current execution map](../README.md). This report does not reactivate that program or claim its conditions have been met.

A practical evaluation sequence:

1. **Inventory and discovery smoke:** identify the active rule sources for workspace, backend, frontend, and worktree launches. Check that critical unique rules survive the proposed consolidation.
2. **Small calibration set:** include a backend fix, API change, client parity change, streaming issue, visual change, and concurrent-worktree scenario. Use it to debug the evaluation, not to announce a statistically established speedup.
3. **Controlled comparison:** freeze task commits, model/tool versions, permissions, environment, acceptance oracles, and instruction hashes. Compare one change at a time with randomized order and repeated runs. Hide reference solutions and use held-out tasks.
4. **Measure the whole outcome:** accepted-correct completion, human review/repair minutes, elapsed time, first useful feedback, regressions/authority violations, and model/tool cost. Keep failed, blocked, and timed-out runs visible; report correctness separately from speed among successful runs.
5. **Adopt narrowly:** require preserved critical invariants and a useful measured benefit. If results are mixed, retain only factual repairs and targeted improvements supported by the failure analysis. Recheck when the agent or task mix changes.

The [existing timing baseline](../reliability/test-loop-baseline.md) remains partial. Passing router/recorder tests establishes functional behavior; it does not establish historical-diff coverage, a full-suite median, or fast-path performance.

## Proposed implementation order

| Priority | Bounded change | Completion evidence |
|---|---|---|
| First | Restore intended GitHub Actions execution and repository-specific required checks; repair bootstrap and setup prerequisites. | Current remote candidate runs the intended checks; docs-only contracts receive a terminal outcome; fresh setup produces the supported layout. |
| First | Repair offline fixture isolation, checker/eval failure behavior, visual carry/diff, and mock notification transport. Correct their owner instructions alongside the code. | Focused negative cases described above; required integration evidence retained. |
| First | Bind cross-repo checks to the intended tuple; repair Git environment handling and linked-worktree detection; put the coordinated gate before landing. | Distinct synthetic repo identities, linked checkout support, candidate-mismatch rejection, no landing after failed checks. |
| Alongside | Correct paths, sync mode, transaction API, type ownership, and actual verification coverage. Triage documentation baseline failures. | Source-to-command review and scoped governance; revision-identified remaining debt without blanket exemptions. |
| Next | Consolidate shared instruction ownership, specialist scoping, and conditional context/review routing. | Unique-rule coverage plus actual discovery from supported launch contexts. |
| Conditional | Trial leaner startup context or improved retrieval; measure accepted delivery and human effort. | Controlled representative tasks with trustworthy oracles and environment identity; no gain claimed from word count or retrieved-file count alone. |

I would not start with broad package moves, a new repository-wide agent framework, automatic self-editing instructions, or mandatory reviewer agents on every task. This audit did not demonstrate that those investments address the observed failures.

## Audit provenance and limits

Observed base revisions:

| Repository | Branch | HEAD at recorded inspection |
|---|---|---|
| Workspace | main | 2e46e1fe869c52c35e5f90dfc6bd0fc2ec67ba32 |
| Backend | main | 92b8b4594abc3caaed5eb57e760b75cc2c15bf13 |
| Frontend | codex/entity-object-design-completion | c201457d36adfb68402b016a5b7b418c3e805b83 |

All three checkouts had unrelated uncommitted work and active worktrees. These revisions identify the inspected bases; they do not make the complete working-tree state reproducible or establish release readiness.

Executed in the first pass, before adding this report:

- Verification router and timing-recorder tests: **32 passed in 2.96 seconds**.
- Backend import boundary, lazy-import, and SCC checks: **passed**; 60 documented lazy exceptions and one accepted four-module cycle.
- Workspace documentation gate: **failed** on the existing working-tree issues described above.

First-pass exclusions: full backend/frontend suites, make verify, live services, device QA, remote CI inspection, and a local instruction A/B experiment. The third pass subsequently inspected remote CI settings and run metadata read-only. No active AGENTS.md/CLAUDE.md rules, product code, generated contracts, deployments, or runtime settings were changed for this research.

Research used bounded primary-source discovery followed by targeted checks of methods, versions, contradictory results, and loading semantics. Core claims were spot-checked against original sources. June revisions and July/August preprints are included; living documentation was checked on September 7. Full DORA PDF access and the full methods of the Microsoft and July enterprise studies were limited as noted, so no additional estimator or quality claims are made from them.

The stopping point is evidence convergence: the actionable gaps have direct local support, competing empirical findings are bounded by their methods, and another broad search is unlikely to determine our local effect size. That remaining question requires our own measured trial.

### Second-pass provenance and verification

Second-pass base revisions were workspace main at b56712eec36874c4c2bc356c7dd8954e7372f036, backend main at 92b8b4594abc3caaed5eb57e760b75cc2c15bf13, and frontend codex/entity-object-design-completion at b479c3289657abe7a6b982a7db622a7893b264a3. The shared checkouts remained dirty; the first-pass table above is intentionally retained as historical provenance.

Executed in the second pass:

- Synthetic Git-repository probes reproduced linked-worktree rejection and inherited-GIT_DIR identity contamination. Existing orientation commands were tested read-only from different working directories.
- In-memory frontend probes reproduced changed-canon auto-carry accepted by the real validator, lost earlier-capture regression, and a mock-mode notification POST intercepted by a stub. API-boundary and schema-bridge checks passed despite the bounded gaps described above.
- Isolated backend probes reproduced prefix-quarantine expansion, comment-only checker registration, and alternate-import-spelling gaps. Backend import, lazy-import, transaction-ratchet, and registration checks passed; those outcomes do not contradict the probes.

The coordinator independently inspected the consequential implementation paths and primary research sources. In the second pass, repository-wide suites, configured databases, live model/provider calls, devices, remote Actions history, and actual fresh-agent instruction loading were not exercised. No product incident, performance improvement, clean-main status, or historical receipt misuse is inferred from these probes.

The second online wave targeted retrieval/process benchmarks, evaluator validity, infrastructure confounding, subsequent maintenance, instruction-file evolution, and official Git/tool loading semantics. It added six primary papers and a controlled first-party infrastructure experiment, plus targeted official documentation. One benchmark's inconsistent headline count was excluded from quantitative conclusions. Further broad source collection is unlikely to resolve these local executable gaps; targeted repairs and held-out evaluation are the next evidence needed.

### Third-pass provenance and verification

Third-pass starting bases: workspace main at 732507726ba245238c8962aa292b3d7d5d1c8eed; backend main at b7df20cdc0fe6444db29daf8b586444e5635e0a4; frontend codex/entity-object-design-completion at b479c3289657abe7a6b982a7db622a7893b264a3. Concurrent work continued during inspection. Claims about local source, remote main workflow definitions, and individual CI runs are intentionally separate.

Executed: copied-script bootstrap/doctor and dev-launcher probes with all external commands stubbed; isolated mypy-result and npm-audit-result probes; parsed workflow-selection, semver, dependency-manifest, and packaged-source analysis. Read GitHub repository settings, remote workflow definitions, and bounded recent run/job metadata with authenticated read-only API calls. The coordinator independently reviewed consequential code paths and original research. No actual source installs, full repository suites, service/container starts, image/native builds, configured database access, provider calls, or instruction A/B experiments were run. No remote settings, active instructions, or product code were changed.

The third online wave added five empirical studies, including an August revision and an older industrial mutation-testing study, plus official GitHub, dependency, image, and hook documentation. Initial discovery was followed by targeted version/method checks and counterevidence. GNU Bash documentation retrieval remained unavailable; launcher behavior is supported by the direct isolated reproduction instead. Research stopped when setup findings had direct evidence and research implications had bounded support; further broad browsing would not establish the local productivity effect or repair these defects.

Artifact verification: report metadata, inventory registration, relative links, fenced examples, and Markdown structure passed scoped checks. No rendered visual review was performed; a Markdown renderer was unavailable in the checked Python runtime.
