---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-11
expires: 2026-09-10
why_new: Extends the July architecture-simplification audit with a point-in-time structural measurement, an adversarial review of research on coding-agent velocity, and a proposed private replay evaluation.
promotes_to: null
supersedes: []
related:
  - ../../travel-agent/docs/working/demo-world-program-2026-08-12.md
---

# Codebase Architecture Quality and Agent-Velocity Research

**Date:** 2026-08-11
**Last revised:** 2026-08-12

> Execution status: supporting specification. Through Demo World Program Phase
> 6, the [Demo World Program](../../travel-agent/docs/working/demo-world-program-2026-08-12.md)
> and its machine-readable registry are the sole active execution backlog. This
> document remains authoritative for the evidence, detailed acceptance criteria,
> and non-goals of A0–A6; it must not be operated as a parallel schedule.

## Question and conclusion

Two questions, asked in sequence:

1. Is the backend/frontend architecture structurally sound?
2. Should we restructure the codebase to make AI coding agents faster, and what does the evidence actually support?

The architecture is broadly sound and already has more enforcement than the first audit recognized. It also has real pressure points: deferred cross-boundary dependencies, a live import cycle, large mixed-responsibility packages, and verification loops whose speed and trustworthiness have not been measured cleanly.

The evidence does **not** justify a broad restructuring program whose primary goal is agent velocity. It does justify a narrower sequence:

1. establish a reproducible private replay evaluation;
2. preserve and ratchet the dependency boundaries already enforced;
3. improve trusted, fast verification;
4. test leaner repository instructions and structural code indexing in controlled A/B trials; and
5. refactor only seams that repeatedly cause localization, change-spread, or dependency failures.

This updates the original recommendation materially: recent fixed-harness evidence makes structural indexing worth testing, but not worth adopting without a local trial.

---

## Scope, provenance, and limitations

The original structural measurements were taken on 2026-08-11 from the working trees under `/Users/feihuyan/travel-workspace`. The base commits now recorded for provenance are:

| Repository | Base commit |
|---|---|
| Workspace | `0cd17045742be646a528b5f868716ef8cd7fe08c` |
| Backend (`travel-agent`) | `a29b92d96a5840a1e7590c27a2705706823afecb` |
| Frontend (`travel-app`) | `05e429d06a9bdb0b7366a464fa0e922709105cfb` |

The measurements described below came from ephemeral scripts and may also have observed uncommitted working-tree state. The commits identify the repository bases; they do not make the original counts independently reproducible. Before any count is promoted into a durable invariant, the parser, exclusions, input commits, and output artifact must be committed and rerun.

This note is also not the first cross-repository architecture review. It should be read alongside [`architecture-simplification-2026-07.md`](./architecture-simplification-2026-07.md), which already documents the generated-contract workflow and several of the same structural seams.

---

## Part 1 — Local structural audit

### Original method and measurements

The original audit used `find`/`wc` for sizing and an AST parser for backend imports. It resolved relative and absolute imports, distinguished module-level from function-body imports, computed strongly connected components with Tarjan's algorithm, and simulated hoisting deferred imports. Because the scripts were not retained, the following numbers are diagnostic observations rather than durable facts.

| | Backend (`travel-agent`) | Frontend (`travel-app`) |
|---|---:|---:|
| Files counted | 4,056 `.py` | 2,553 `.ts`/`.tsx` |
| LOC counted | 1,033,308 | 505,495 |
| Backend modules in graph | 1,458 | — |
| Tests reported | 19,043 collected | 1,038 test files |

### What appears healthy

**Frontend**

- React Query is the dominant server-state mechanism; there is no competing Redux/Zustand/MobX-style application store.
- API access is concentrated under `utils/api` and guarded by existing scripts such as `check-api-boundaries.mjs`, `check-query-key-ownership.mjs`, and `check-mutation-key-ownership.mjs`.
- Feature-oriented component directories give the application a recognizable macro-structure.

**Backend**

- `core.models` and `core.exceptions` behave like low-level foundations.
- `api.routes` primarily points inward, as expected for an outer delivery layer.
- The original AST graph found one top-level import cycle across 1,458 modules and 4,247 top-level edges: the four-file `home/concierge_feed` component.
- Backend enforcement already exists. On 2026-08-11, both `scripts/check_imports.py --ci` and `scripts/check_lazy_imports.py --ci` passed. The latter found 60 cross-boundary lazy imports, all allowlisted, with no new or stale entries. Both checks are wired into pre-commit, CI, and Make targets.

### Pressure points worth investigating

1. **`core/` and `concierge/` are broad namespaces.** The audit counted 194 loose Python files under `core/` and 128 under `concierge/`. That increases naming and navigation entropy, but file count alone is not evidence that moving files will improve delivery or agent success. Split only around a demonstrated responsibility boundary.

2. **Deferred imports hide architectural pressure.** The original parser counted 2,030 function-body imports. Its counterfactual suggested that only 33 would create a cycle if hoisted, while hoisting everything would create large strongly connected components. Calling the remaining imports "cargo cult" was an unsupported inference: hoistability does not reveal the author's reason or the runtime cost of hoisting. The useful result is the smaller set of load-bearing deferred edges, which should be reproduced and tracked explicitly.

3. **There are genuine low-to-high dependencies.** Examples recorded by the audit include `core/db/atlas.py` reaching into `atlas.projector` and related feature modules, `core/db/trips/crud.py` reaching into `atlas`, `digest`, and `concierge`, and `core/tools/registry.py` loading research-agent tools. These are candidates for explicit ports or orchestration ownership if they repeatedly enlarge changes.

4. **Projection delivery has mixed semantics, not merely mixed syntax.** Some projections are invoked directly while others use `core/event_bus.py`. The bus is explicitly fire-and-forget, does not propagate subscriber failures, can drop async work, and relies on startup-time subscriber registration. Routing database projections through it is therefore not a mechanical cleanup; it could change persistence and failure semantics or silently do nothing in scripts. Do not standardize on the event bus without first choosing the required delivery guarantees.

5. **Frontend contract truth is not simply duplicated.** `utils/api/types.ts` already imports `components` from `schema.gen.ts` and contains roughly 200 generated-schema references, plus adapters, refinements, and UI-only types. `utils/api/interface.ts` also imports the generated schema and has multiple active importers. The earlier claim that 102 names represented two independent hand-maintained truths, and that `interface.ts` was dead, was false. The remaining useful task is narrower: detect genuinely hand-copied wire types and ensure they derive from the generated schema where appropriate.

6. **The cited red baseline is stale.** The named test, `TestProposeChangeExecution::test_bounded_opening_persists_a_valid_local_wall_time_add`, passed on 2026-08-11 (`1 passed in 0.66s`). A full-suite runtime and baseline failure inventory were not measured, so the earlier estimate of a 30-minute suite and the assertion of a known red baseline should not drive prioritization.

7. **Frontend housekeeping remains real but low leverage.** The overlapping `trip*` directories and root-level screenshot assets may create navigation noise. Resolve them when a product or ownership boundary is being changed, not as an agent-specific reorganization project.

### Corrections to the first audit

- Pairwise grep overstated cycles because it counted deferred imports as top-level edges; the AST analysis found one top-level cycle.
- Hoistability was initially interpreted as proof of poor import discipline. It shows only that many imports are not cycle-preventing.
- Backend import enforcement was incorrectly described as missing. It already exists and passes.
- The generated API schema was incorrectly described as a parallel, unused source of truth. It is already imported extensively by the frontend adapter layer.
- `utils/api/interface.ts` was incorrectly described as dead.
- A direct-to-event-bus migration was presented as behavior-preserving when the two paths have different delivery and failure guarantees.
- The document claimed no previous cross-repository architecture note existed; the July architecture-simplification audit predates it.
- The named failing test now passes.

---

## Part 2 — Independent research review

The question is not whether clean architecture is beneficial. It is whether changing this production architecture *for agents* will improve accepted, shipped work enough to justify the cost and risk. Evidence was ranked roughly as: controlled within-harness ablation or randomized field experiment; multi-model public benchmark; observational telemetry; vendor benchmark; practitioner report.

| Finding | Evidence and limitations | Decision implication |
|---|---|---|
| Repository exploration and dependency understanding constrain multi-file repair | [SWE-Explore](https://arxiv.org/abs/2606.07297) reports that localization metrics track downstream repair; [DependEval](https://aclanthology.org/2025.findings-acl.373/) finds substantial gaps in dependency understanding across 2,683 repositories and more than 25 models. These are benchmarks, not measurements of this workspace. | Measure task-relevant dependency span and localization, not total LOC alone. |
| A structural code index can improve localization and resolution | In a fixed-harness, fixed-model, three-seed ablation, [Code Isn't Memory](https://arxiv.org/abs/2606.22417) reports localization `acc@5` improving from 44.3% to 84.5% and resolution from 41.9% to 50.4%, without a per-cell cost penalty. It uses one open-source harness, one model, and public benchmarks; the authors built the evaluated tool. | Upgrade indexing from "do not buy" to a controlled local A/B trial, especially for multi-file tasks. Do not assume transferability. |
| Functional success can conceal architectural damage | [Needle in the Repo](https://arxiv.org/abs/2603.27745) evaluates 23 configurations and reports that 13.3% of outcomes passed functional tests but failed a structural oracle. Dependency control and responsibility decomposition were the hardest categories. Its probes are small controlled codebases. | Keep independent architectural oracles alongside functional tests. |
| More always-on repository context may hurt | [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) finds no general success improvement and more than 20% higher inference cost across generated and developer-authored context files. A smaller [AGENTS.md efficiency study](https://arxiv.org/abs/2601.20404) reports lower median runtime and token use. Task mix and instruction quality differ. | Keep instructions minimal, stable, and non-inferable; A/B test this workspace's manifest rather than generalizing either result. |
| Generic harness evolution does not guarantee improvement | [Don't Blame the LLM](https://arxiv.org/abs/2607.03691) holds the model fixed across 35 Qwen Code CLI releases and finds a flat average resolution rate while token use rises. It studies one evolving vendor harness on 50 SWE-bench Verified tasks. | Require focused component ablations; do not treat "better tooling" as one undifferentiated intervention. |
| Agent evaluation is noisy | [On Randomness in Agentic Evals](https://arxiv.org/abs/2602.07150) uses 60,000 trajectories and finds that single-run pass@1 estimates vary by 2.2–6.0 percentage points. | Run multiple independent attempts per task and report uncertainty, not one headline score. |
| Existing tests can accept wrong patches | [UTBoost](https://arxiv.org/abs/2506.09289) reports insufficient tests in 36 SWE-bench tasks and 345 erroneous patches classified as passing. [Needle in the Repo](https://arxiv.org/abs/2603.27745) independently shows functional/structural divergence. | Use hidden tests plus structural checks and human adjudication for the private evaluation. |
| Human productivity results are heterogeneous | A Microsoft study combining three field experiments and 4,867 developers reports [26.08% more completed tasks](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/). METR's randomized study of 16 experienced developers and 246 tasks found [early-2025 tools made work 19% slower](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); its [2026 update](https://metr.org/blog/2026-02-24-uplift-update/) calls the newer evidence very weak because of selection effects. | Measure this team, tool generation, and task mix. Output volume, perceived speed, and accepted delivery are different outcomes. |
| Public benchmark performance may not transfer | [SWA-Bench](https://proceedings.mlr.press/v267/vergopoulos25a.html) finds substantially lower success on application-level tasks than on SWE-bench-style maintenance. [SWE-rebench](https://arxiv.org/abs/2505.20411) documents contamination and benchmark-staleness concerns. | Historical private tasks are more decision-relevant than public leaderboard scores. |

### Synthesis

No source above provides clean causal evidence that broadly reorganizing an existing production repository improves agent-assisted delivery. Some sources show that larger or more distributed change surfaces are harder, but their task domains and thresholds do not transfer directly.

The more defensible mechanisms are:

- faster and more accurate localization;
- smaller task-relevant dependency spans;
- concise, relevant repository constraints;
- trusted executable feedback;
- structural checks that catch maintainability regressions; and
- measurement of accepted or shipped outcomes rather than generated LOC, tokens, or tool calls.

This supports normal architectural work at demonstrated high-change-spread seams. It does not support splitting `core/`, `concierge/`, or the frontend trip directories merely because they are large.

---

## Action items — supporting engineering specification

The items remain ranked by evidence quality, decision value, cost, and
reversibility. Estimates are one-engineer elapsed working time and exclude
unattended model runtime. A named person must replace each role-level DRI before
work starts. During the Demo World Program, only mapped registry tasks may
execute; the mapping controls owner, priority, timing, and shared-surface locks,
while the sections below control technical completion.

### Integrated execution authority

| Source item | Canonical program task | Execution decision through Demo Phase 6 |
|---|---|---|
| A1 generated-contract derivation | `DEMO-ENG-01` | Active after a named API-contract DRI is assigned. Complete before Phase 5 entry through serialized `contract-sync` windows. |
| A2 verification-router repair | `DEMO-ENG-02` | Active after a named test-infrastructure DRI is assigned. Root-only work may run beside demo definition/product work. |
| A2 Home ratchet dependency | `DEMO-ENG-03` | Demo Home lane owns the product change. A2 may verify it but may not make a competing edit. |
| A3 SCC ratchet | `DEMO-ENG-04` | Already shipped; remains a continuous backend merge gate. |
| A2 repeated baseline and historical validation | `DEMO-ENG-05` | Run only on frozen clean commits, away from cloud rehearsal. Defer after Phase 6 if no credible measurement window exists. |
| A0, then optionally A4/A5 | `POST-DEMO-01` | Deferred until Phase 6 closes; no demo critical-path people, cloud state, or canonical checkout use. |
| A6 targeted refactor | No active task | Do not execute independently during the demo. A demo-blocking seam requires a new approved `DEMO-ENG-*` task; otherwise A6 remains gated by A0. |

The Demo Program's Sections 12.2–12.4 define the registry records, protected
surfaces, lock handoffs, and integration cadence. Do not duplicate or override
those decisions here. When a mapped item changes materially, update the registry
and both documents in one integration change.

### Current execution status

Verified 2026-08-12 against workspace `53993f6`, backend `3618081a8`, and frontend `7bac31ea`. Status means the item satisfies its own acceptance criteria, not merely that code was written.

| Item | Status | Verified state | Canonical next action |
|---|---|---|---|
| A0 private replay evaluation | **DEFERRED UNTIL POST-DEMO; ALSO BLOCKED** | No harness/protocol artifacts exist; `codex exec --help` still fails with the same bundled-binary `ENOENT` | `POST-DEMO-01`: do not start before Demo Phase 6 closes. Then assign a named DRI, budget, governed harness, pinned working CLI, and isolation smoke before reactivation. |
| A1 generated-contract derivation | **READY AFTER OWNER ASSIGNMENT** | Enforcement is merged and green: 340/340 exports classified; contract check, typecheck, and 23 checker tests pass | `DEMO-ENG-01`: name the DRI, register the app-only lane, and adjudicate the 87 `unmodeled_wire` entries through serialized `contract-sync` windows before Phase 5. |
| A2 verification router | **COMPLETE — EXPERIMENTAL FAST PATH ONLY** | `DEMO-ENG-02` now discovers committed/staged/unstaged/untracked changes in all three independent repositories; per-repository base refs are validated; selected checker tests execute; recorder failure propagates | `make verify` remains the required pre-push/merge gate. `DEMO-ENG-05` owns clean-commit repetition, historical-diff, and timing evidence. |
| A2 Home ratchet dependency | **READY; DEMO-OWNED** | Frontend `verify:fast` is red because `utils/tripsHomeSectionPlan.ts` is 285 lines against a 267-line ratchet | `DEMO-ENG-03`: the Demo Home DRI makes the reviewed product/budget decision; the verification owner only remeasures afterward. |
| A3 SCC architecture ratchet | **COMPLETE / CONTINUOUS GATE** | Merged on backend `main`; import, lazy-import, SCC, and 23 SCC tests pass; exact four-module SCC is ratcheted | `DEMO-ENG-04`: keep the gate green on every backend change; review any baseline membership change explicitly. |
| A2 repeated baseline and historical validation | **BLOCKED BY ROUTER, HOME, AND CLEAN-COMMIT FREEZE** | Only one baseline repetition, four of twenty historical diffs, no disposable-Postgres measurement, and no external-lane inventory exist | `DEMO-ENG-05`: measure only after `DEMO-ENG-02/03` on fixed clean commits; defer post-demo rather than collect incomparable timings. |
| A4 lean instruction trial | **DEFERRED; BLOCKED BY A0** | No treatment artifact or trial exists | `POST-DEMO-01`: reconsider only after A0's pilot and power check pass. |
| A5 indexing/repository-map trial | **DEFERRED; BLOCKED BY A0** | No qualified intervention or trial exists | `POST-DEMO-01`: begin qualification only after the A0 pilot passes. |
| A6 targeted refactor | **DEFERRED; GATED BY A0** | No qualifying failure cluster or refactor decision record exists | No active program task. Create a reviewed `DEMO-ENG-*` exception only for a demo-blocking seam; otherwise wait for qualifying A0 evidence. |

### Program dependencies and phase gates

| Canonical task | May start when | Blocks or gates |
|---|---|---|
| `DEMO-ENG-01` / A1 | Named reviewer, registered app-only lane, and no conflicting `contract-sync` holder | Demo Phase 5 entry and contract-facade certification |
| `DEMO-ENG-02` / A2 router | Complete | An experimental fast path is available; `make verify` remains authoritative |
| `DEMO-ENG-03` / Home ratchet | Named Demo Home DRI and product scope agreed | Demo Phase 5 entry and credible frontend baseline measurement |
| `DEMO-ENG-04` / A3 | Complete; run continuously | Every backend merge and any later architecture comparison |
| `DEMO-ENG-05` / A2 measurement | `DEMO-ENG-02/03` complete and all three repository commits frozen and clean | Verification-loop optimization decisions; it may be deferred rather than block Phase 6 |
| `POST-DEMO-01` / A0→A4/A5 | Demo Phase 6 closed, plus A0 DRI, budget, harness, pinned CLI, and isolation smoke | A4/A5 trial decisions |
| A6 | A0 qualifies a seam, or the Demo Program approves a new blocking-seam exception | Any agent-specific restructuring |

### Rules shared by every item

- Confirm that the item has a canonical registry ID and named DRI before work.
  Items mapped to `POST-DEMO-01` or “no active task” must not start during the
  demo program.
- Acquire the Demo Program surface lock before writing protected files and
  release it only after the linked evidence and integration result are recorded.
- Run `make status` before starting. Do not implement in a canonical child checkout that contains another session's work.
- Use `./scripts/new-worktree.sh <lane>` or its `--agent-only`/`--app-only` form. Use one descriptive branch per child repository and stage explicit filenames only.
- Record the exact input commit, command, tool version, start/end time, and pass/fail result in the named evidence artifact.
- Do not weaken an existing full gate to make a fast gate pass. Fast paths supplement `make verify`; they do not replace the merge/pre-push gate until separately approved.
- Treat source, prompts, diffs, and trajectories as private. Do not commit credentials, CLI authentication, raw model transcripts containing secrets, or hidden verifier patches into an agent-visible task checkout.
- An item is complete only when its deliverables exist, its acceptance criteria pass, and its non-goals remain untouched.

### A0 — Build a private historical-task replay evaluation *(first research item)*

- **Program mapping:** `POST-DEMO-01`; deferred until Demo Phase 6 closes.
- **Confidence:** high that measurement is required; results unknown.
- **DRI:** workspace evaluation owner — **unassigned**.
- **Repositories:** workspace implementation; read-only historical worktrees from both child repositories.
- **Effort:** 5–8 engineering days for harness/task preparation, plus model runtime and two independent human review passes.
- **Depends on:** assigned DRI, approved spend ceiling, installed dependencies, and working Codex CLI.

#### Harness selection and transferability

The protocol currently pins `codex exec`. Day-to-day agent work in this workspace also runs through other harnesses, and [Don't Blame the LLM](https://arxiv.org/abs/2607.03691) is direct evidence that harness identity and version change outcomes at a fixed model. A result measured on one harness therefore does not transfer to another by default, and an A4/A5 decision taken on the wrong harness governs a workflow it never observed.

Before the pilot, the DRI must record which harness the decision is intended to govern and choose exactly one:

- measure the harness actually used for the work the decision will change;
- treat harness as a blocking stratum and run both arms on both harnesses, accepting roughly double the runtime and review cost; or
- record explicitly that the findings apply only to the measured harness and may not be generalized.

Whichever is chosen, pin harness name, version, model ID, and reasoning level in the variant manifest, verify them at run time alongside the prompt and variant hashes, and report results per harness. Never pool results across harnesses into a single headline number.

#### Current prerequisite blocker

On 2026-08-11, local `codex exec --help` failed because the installed package could not find its bundled native binary (`ENOENT`). Before building the harness, reinstall or repair the CLI, pin and record `codex --version`, and demonstrate one disposable smoke run. Do not silently switch between the desktop app, a different CLI release, or another model during an experiment.

**Status verified 2026-08-12: DEFERRED UNTIL POST-DEMO AND BLOCKED, not started.** `codex exec --help` still fails with the identical `ENOENT`; `scripts/agent_velocity_eval.py` and `docs/reliability/agent-velocity/protocol.md` do not exist. Do not consume demo critical-path reviewers, cloud state, or canonical checkouts to clear these prerequisites.

At the `POST-DEMO-01` reactivation checkpoint, complete these prerequisites in
order:

1. Replace “workspace evaluation owner” with a named DRI in this document.
2. Record the maximum model spend and maximum human-review time in the protocol stub.
3. Make and record the harness-scope choice described above.
4. Repair or reinstall the CLI; record the installation source and `codex --version`.
5. Run one non-scored, disposable `codex exec --ephemeral` smoke task inside the proposed isolation boundary and retain its command, exit status, JSONL, patch, and cleanup evidence.

Do not create the scored task manifest or begin A4/A5 until all five are complete. A1–A3 are independent of this blocker; A4–A6 are not.

Official OpenAI documentation supports `codex exec` for non-interactive runs, `--ephemeral` to avoid persisted rollout files, `--ignore-user-config`/`--ignore-rules` for controlled automation, `--json` for JSONL events, and `--sandbox workspace-write` for unattended work confined to the workspace. Use those explicit flags rather than deprecated `--full-auto`. See [non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) and the [CLI flag reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

#### Files to create

- `scripts/agent_velocity_eval.py` — `validate`, `pilot`, `run`, `verify`, `score`, and `report` subcommands.
- `scripts/tests/test_agent_velocity_eval.py` — fixture, leakage, manifest, command-capture, and scoring tests.
- `docs/reliability/agent-velocity/protocol.md` — frozen protocol, reviewer rubric, security rules, and approved decision thresholds.
- `docs/reliability/agent-velocity/task-manifest.json` — immutable, agent-safe scored-task manifest; no reference commits or hidden verifier locations.
- `docs/reliability/agent-velocity/task-manifest.schema.json` — schema enforced by `validate`.
- `docs/reliability/agent-velocity/score.schema.json` — run and adjudication output schema.
- `docs/reliability/agent-velocity/prompts/<task-id>.md` — problem statements reconstructed without solution details.
- `docs/reliability/agent-velocity/variants/` — treatment definitions, hashes, and tool configuration; no hidden tests.
- `docs/reliability/agent-velocity/results-summary.json` and `report.md` — sanitized aggregate output. Raw JSONL, patches, and hidden verifiers stay under a `mktemp -d` artifact directory outside the repository.

#### Task manifest requirements

Select 18–24 accepted tasks: 6–8 backend-only, 6–8 frontend-only, and 6–8 cross-repository/API-contract tasks. Across the full set, include at least six historical one-file changes, six two-to-three-file changes, and six four-or-more-file changes.

Every committed, agent-safe task entry must contain:

- stable task ID and category;
- workspace, backend, and frontend base commits;
- prompt path and SHA-256;
- allowed repositories and required services;
- time limit and maximum attempts;
- historical change-size bucket, without listing solution files in the agent-visible prompt;
- public regression-command identifiers, but not hidden verifier contents or paths;
- exclusions and reason; and
- human-adjudication rubric version.

Keep reference commits, solution diffs, hidden verifier commands, and hidden patch locations in a separate evaluator-private manifest outside the repository. Commit only that private manifest's SHA-256 to the protocol before scored runs. The agent process must run in a dedicated container or VM that mounts the historical task workspace but cannot read the controller checkout, private manifest, reference repository, verifier, or prior-run artifacts. Validate that boundary with a canary file during the pilot; `workspace-write` alone is not the leakage boundary.

Include a task only when its user-visible request can be reconstructed without the reference diff and its outcome can be checked deterministically. Exclude tasks requiring live production data, unrecorded manual UI judgment, unavailable API keys, or external services that cannot be replaced by a fixture. A database task is eligible only with a disposable database at the historical migration head.

Freeze the manifest in review before scored runs. The runner must refuse a task when a base commit, prompt hash, variant hash, verifier, or required dependency is missing.

#### Isolation and run procedure

For each task and repetition, the runner must:

1. create a new temporary workspace with `mktemp -d`;
2. add detached worktrees at the task's three base commits, preserving the sibling `travel-agent`/`travel-app` layout, then expose only that temporary workspace to the agent container/VM;
3. install or attach dependencies before model credentials enter the process environment;
4. overlay only the selected treatment variant;
5. invoke the pinned model, reasoning level, CLI version, approval policy, sandbox, prompt, and time limit;
6. capture the complete argv, JSONL event stream, final message, wall time, token usage, exit status, and binary patch;
7. remove model credentials before running repository-controlled verification;
8. apply the produced patch to a separate verifier checkout, then add the hidden test patch there; and
9. run hidden checks, regression checks, contract checks, and structural checks without exposing their content to the agent checkout.

The runner's generated invocation must be equivalent to:

```bash
codex exec \
  --ephemeral \
  --ignore-user-config \
  --ignore-rules \
  --sandbox workspace-write \
  --ask-for-approval never \
  --json \
  --model "$MODEL_ID" \
  --config "model_reasoning_effort=$REASONING_EFFORT" \
  --cd "$EVAL_WORKSPACE" \
  --output-last-message "$RUN_DIR/final.txt" \
  "$PROMPT"
```

The actual expanded argv—not only this template—must be stored with every run. Authentication must follow the official automation guidance and the selected isolation design. Never expose an API key or saved authentication file to agent-invoked repository processes; if the approved runner cannot enforce that boundary, A0 remains blocked. Redact secret-valued environment variables from captured metadata.

#### Experiments and repetitions

- Use three non-scored tasks to pilot fixture creation, timeout handling, patch capture, and blind review.
- Run instruction and indexing experiments separately; never change two interventions in one arm.
- Randomize arm order within each task.
- Run three independent repetitions per task and arm.
- Blind the two human reviewers to arm and repetition. Resolve disagreements by a third reviewer or a pre-named adjudicator.

#### Scoring and decision rule

A run is **accepted-correct** only when all hidden required checks pass, no regression command fails, no new architecture/contract violation appears, and human review records no blocking semantic or maintainability defect.

Primary metric: accepted-correct runs divided by attempted runs. Secondary metrics: task-level success in at least two of three repetitions, wall time, reported token usage, cost if available, time to first edit of a reference-relevant file, files inspected, changed-file count, rework attempts, and human review findings.

Use a paired bootstrap resampled by task—not by individual run—to report 95% confidence intervals. Preserve failures and timeouts in the denominator. Report all tasks and exclusions; do not remove a hard task after seeing results.

The generic adoption rule for A4/A5 is:

- **quality win:** at least an 8 percentage-point increase in accepted-correct rate, with no increase in blocking maintainability findings; or
- **efficiency win:** at least a 15% reduction in median wall time or measured cost, while the task-clustered 95% interval for correctness excludes a loss worse than 5 percentage points and structural/contract violations do not increase.

If neither condition is met, the result is inconclusive or negative and the current workflow remains unchanged.

#### Statistical power

The 8-point threshold has not been shown to be detectable at the planned sample size. [On Randomness in Agentic Evals](https://arxiv.org/abs/2602.07150) reports single-run pass@1 varying by 2.2–6.0 percentage points. With 18–24 tasks, three repetitions, and resampling clustered by task, the 95% interval may straddle 8 points, which would make "inconclusive" the most likely reported outcome regardless of whether the intervention has a real effect. That failure mode is expensive: it consumes the full harness build, model runtime, and two blinded review passes before revealing that the design could not answer the question.

Before the first scored run, the DRI must:

- estimate run-level and task-level variance from the three pilot tasks;
- compute the minimum detectable effect at the planned task count, repetition count, and clustering, and record it in the protocol beside the adoption rule; and
- if the minimum detectable effect exceeds 8 points, choose one of: raise the task count; restrict the primary analysis to the four-or-more-file and cross-repository strata where the mechanism predicts the largest effect and which A5 already reports separately; raise the adoption threshold to the detectable level; or pre-register the trial as descriptive rather than decisive.

Report the point estimate and interval for every experiment, not only pass/fail against the threshold. "Inconclusive" is a pre-declared outcome that requires a named owner and a recorded next step — widen the sample, change the stratum, or stop — and may not be resolved by rerunning the same design until it clears the threshold.

#### Commands and acceptance criteria

After implementation, the following interface is required:

```bash
python3 scripts/agent_velocity_eval.py validate
python3 -m unittest scripts.tests.test_agent_velocity_eval
python3 scripts/agent_velocity_eval.py pilot --experiment instructions
python3 scripts/agent_velocity_eval.py run --experiment instructions --repetitions 3
python3 scripts/agent_velocity_eval.py run --experiment indexing --repetitions 3
python3 scripts/agent_velocity_eval.py score
python3 scripts/agent_velocity_eval.py report
```

A0 is complete when the harness tests pass; the frozen manifest has 18–24 eligible tasks; every scored cell has three attempts or a retained timeout/failure record; two blinded reviews exist per patch; the sanitized report can be regenerated from raw artifacts; and another engineer can reproduce one selected cell from the protocol.

**Non-goals:** changing production architecture, using public benchmark scores as local results, comparing different models, or making either A4/A5 adoption decision before the complete report.

### A1 — Audit and enforce generated contract derivation *(immediate engineering)*

- **Program mapping:** `DEMO-ENG-01`; W5, required before Demo Phase 5 entry.
- **Status:** **SHIPPED ENFORCEMENT; REMEDIATION READY AFTER OWNER ASSIGNMENT.** Human contract adjudication is not complete.
- **Merged commits:** frontend `46b25f4a`, backend `50e6585fb`, workspace `23c7d48`; all are reachable from the current `main` branches through the 2026-08-12 hardening merges.
- **Verified 2026-08-12:** `make contract-check`, `make typecheck`, `npm run schema-bridge`, and all 23 schema-bridge tests pass.
- **Inventory:** 340 exports = 147 `generated_alias`, 56 `schema_projection`, 50 `ui_only`, and 87 `unmodeled_wire`.
- **Blocking gap:** all 87 exceptions use a placeholder/unassigned owner; 46 also have no route or method. The manifest expires these exceptions on 2026-09-11.

- **Confidence:** high; contract single-source-of-truth is valuable independent of agents.
- **DRI:** frontend/API-contract owner — **unassigned; a named reviewer is required now.**
- **Repositories:** `travel-app`, with removal of the superseded checker/hook in `travel-agent`.
- **Remaining effort:** 2–4 engineering days for the 87-entry human review and resulting type changes.
- **Depends on:** no A0 dependency; register an app-only review lane and acquire the Demo Program's `contract-sync` lock before writing any protected contract surface. Demo API changes own the announced integration windows; A1 rebases afterward.

#### Shipped implementation

The merged TypeScript-AST checker replaced `travel-agent/scripts/check_schema_bridge.py`, inventories every exported type in both API facade files, runs in `verify:fast` and `contract-check`, and fails for unclassified exports, missing generated models, malformed entries, and expired `unmodeled_wire` exceptions.

#### Shipped deliverables

1. `travel-app/scripts/schema-bridge-manifest.json` inventories every exported interface/type in `utils/api/types.ts` and `utils/api/interface.ts` with symbol, source file, classification, generated schema name when applicable, and rationale. All 87 `unmodeled_wire` entries have an expiry and placeholder owner; 41 have route/method evidence. The placeholder owners and remaining 46 evidence gaps are intentionally tracked as unfinished work below.
2. `travel-app/scripts/check-schema-bridge.mjs` uses the installed TypeScript compiler API rather than regex parsing.
3. `travel-app/scripts/check-schema-bridge.test.mjs` has 23 passing tests across the required classifications and failure modes.
4. `schema-bridge` runs from frontend `verify:fast` and workspace `contract-check`.
5. The superseded backend regex checker and hook are removed; there is one canonical implementation.

#### Remaining work — next owner executes this

1. Assign one named API-contract reviewer and replace the placeholder owner on every `unmodeled_wire` entry.
2. Review all 87 entries at their population and consumption call sites—not from field similarity alone—and choose exactly one outcome:
   - convert a wire copy to `generated_alias` or `schema_projection` and update the TypeScript declaration;
   - reclassify a deliberate frontend transform as `adapter` with its source and transformation rationale;
   - reclassify a frontend-only concept as `ui_only`; or
   - retain `unmodeled_wire` temporarily with a named owner, concrete removal plan, and unexpired date.
3. For the 46 entries lacking route/method evidence, add the route and method or document the parent generated schema/consumer chain when the type is nested and has no direct endpoint. Extend the checker and tests so a null route/method without that explicit nested-type evidence fails.
4. Resolve the known `TripStatus`, `ProposalResolveStatus`, and two `DossierExemplar` enum findings as part of this review; do not merely renew their expiry.
5. Run the commands below, review the generated diff, and update the inventory totals and status table in this document.

#### Acceptance criteria

- [x] Every exported interface/type in the two API facade files is classified exactly once.
- [x] The AST checker and its 23 tests are wired into the normal contract/fast gates.
- [x] Intentional facade layers remain source-compatible; neither `types.ts` nor `interface.ts` was deleted wholesale.
- [ ] Every `unmodeled_wire` entry has been human-reviewed and has a named—not placeholder—owner if retained.
- [ ] Every retained exception has route/method evidence or an explicitly checked nested-type alternative, a concrete rationale, and an unexpired removal date.
- [ ] The four recorded status/enum drift findings have an explicit resolution.
- These commands pass from the workspace root:

```bash
make sync-types-snapshot
make contract-check
make typecheck
(cd travel-app && npm run schema-bridge)
(cd travel-app && npm run schema-bridge:test)
(cd travel-app && npm run verify:fast)
```

The generated snapshots and `schema.gen.ts` must have no unexplained diff. **A1 is complete only when every unchecked box above is satisfied; the currently green checker alone is not completion because placeholder owners and null route evidence still pass.**

**Non-goals:** renaming unrelated frontend domain types, changing API behavior, or replacing deliberate frontend adapters with raw generated types at every call site.

### A2 — Measure and improve the trusted verification loop *(immediate engineering)*

- **Program mapping:** router repair `DEMO-ENG-02`; Home dependency `DEMO-ENG-03`; repeated measurement and historical validation `DEMO-ENG-05`.
- **Status:** **IN PROGRESS. `DEMO-ENG-02` is complete; `DEMO-ENG-05` remains blocked on the Home lane and a clean-commit freeze. `make verify` is still the safety gate.**
- **Merged commits:** workspace `26c7f3b` and `f4f941e`, reachable from current `main` through `6fd16bf`.
- **Verified 2026-08-12:** the measurement and router suites pass (53 tests). The recorded backend CI recheck passed in 493.34 seconds with 17,784 offline tests passing; this is one observation, not a median.
- **Current frontend state:** `npm run verify:fast` is red because `utils/tripsHomeSectionPlan.ts` is 285 lines against a 267-line ratchet. Contract check, typecheck, API boundaries, and schema bridge pass before that failure.
- **Evidence gap:** only one repetition per baseline command, four of twenty required historical diffs, no disposable-Postgres measurement, no external-lane inventory, and no valid `make verify` median.
- **Router repair verified 2026-08-12:** change discovery now independently reads all three Git repositories and prefixes paths; each base ref is resolved only in its own repository; referenced checker tests become executable commands; the recorder propagates a completed command's nonzero exit. 32 targeted tests cover the router/recorder, including three temporary independent repositories and committed, staged, unstaged, and untracked child changes.

- **Confidence:** high on the mechanism; baseline evidence is partial and not yet decision-grade.
- **DRI:** Feihuyan — workspace test-infrastructure owner, with backend and frontend reviewers.
- **Repositories:** workspace plus both child repositories only where a new target is required.
- **Remaining effort:** 3–5 engineering days across the router and Home lanes, plus approximately three full repetitions of the measured gates after both land.
- **Depends on:** named owners, installed dependencies, registered isolated lanes, and—for `DEMO-ENG-05` only—one frozen set of clean commits in all three repositories.

#### Baseline deliverables

- [x] `scripts/measure_verification.py` records command, commit IDs, environment class, wall time, exit status, parsed test counts when available, and log path.
- [x] `scripts/tests/test_measure_verification.py` covers timeout, nonzero exit, JSON schema, and partial-result behavior.
- [x] `docs/reliability/test-loop-baseline.json` and [`test-loop-baseline.md`](../reliability/test-loop-baseline.md) contain the partial evidence and chronology.
- [ ] Three comparable repetitions exist for every required command on the same clean commits.
- [ ] Postgres and excluded live/device/API-key/dogfood lanes are measured or explicitly inventoried.

Run the following three times on the same clean commits, with no source edits between repetitions:

```bash
make doctor
make -C travel-agent ci
make contract-check
cd travel-app && npm run verify:full
```

Measure `make test-backend-postgres` separately against a disposable database. List API-key, dogfood, device, and live-service suites as separate coverage lanes; never describe the measured set as the "full suite" while one is excluded. If any nominally deterministic command changes outcome across three runs, run it ten times, record the failing test IDs, and fix or quarantine with an owner and expiry before optimizing selection.

#### Fast-path deliverables

- [x] A root `make verify-changed` target, dry-run output, classification rules, unit tests, and a documented decision table are merged.
- [x] Change discovery reads the workspace, backend, and frontend Git repositories independently and prefixes their paths before classification.
- [x] The CLI accepts and validates an explicit base ref for each repository; it must not apply one repository's commit ID to another repository.
- [x] Referenced checker tests are real executable commands, not skipped `<run ...>` hints.
- [x] The measurement command propagates the measured command's completed nonzero exit; it is now safe to use as a gate recorder.
- [x] Integration tests create three temporary independent Git repositories and prove committed, staged, unstaged, and untracked child-repository changes are discovered.

Minimum routing rules:

- Unknown paths, shared test configuration, `conftest.py`, migrations, dependency manifests, workspace scripts, API models/routes, `docs/openapi*.json`, or generated-schema tooling select `make verify`.
- Frontend `.ts`/`.tsx` changes run `npm run verify:fast` and Jest `--findRelatedTests` for the changed files. If Jest finds no tests for production code, select the full frontend Jest lane.
- Backend changes always run import/lazy-import/SCC gates plus lint. Until a tested dependency-to-test mapper exists, uncertain backend changes select `make -C travel-agent ci`.
- Documentation-only changes run the existing documentation governance/link gates; executable examples additionally run their referenced checker tests.
- The repaired script must exit nonzero when any required repository base ref is missing or unresolved; it may not guess `main` in a dirty concurrent worktree.

#### Remaining work — execute in this order

1. Complete `DEMO-ENG-03` in its Demo Home lane; it owns the line-budget product decision. Do not change that source file from verification infrastructure.
2. After both the Home lane and its full gate are green, freeze one clean set of three repository commits for `DEMO-ENG-05`. Do not edit source or run this workload concurrently with a W6 cloud rehearsal.
3. Run three back-to-back recorded repetitions of `make doctor`, `make -C travel-agent ci`, `make contract-check`, `npm run verify:full`, and `make verify`. Preserve every failure.
4. Measure `make test-backend-postgres` against a disposable database and inventory the API-key, dogfood, device, and live-service lanes with owners and commands. Never point this measurement at Demo Program runtime state.
5. Validate routing against at least twenty preselected historical diffs, including known defects and cross-repository contract changes. Any missed historical detecting test is blocking.
6. Measure representative low-risk fast paths and compare their medians to the completed `make verify` median. Update both baseline artifacts, the Demo Program registry evidence, and this status table. If a stable measurement window is unavailable before Phase 6, mark `DEMO-ENG-05` deferred rather than collecting incomparable evidence.

Use the recorder explicitly for each run, for example:

```bash
python3 scripts/measure_verification.py \
  --label verify-r1 \
  --append-to docs/reliability/test-loop-baseline.json \
  --timeout 3600 \
  -- make verify
```

Inspect the recorded `exit_code`; until `--propagate-exit` exists, the recorder process returning zero does not prove the measured command passed.

#### Acceptance criteria

- [ ] Baseline artifacts identify exact clean commits and contain all three repetitions, including failures and skips.
- [ ] `verify-changed --dry-run` is deterministic and complete across all three Git repositories.
- [ ] Every unrecognized or high-risk change falls back to `make verify`, and every selected checker test actually executes.
- [ ] On at least 20 reviewed historical diffs, the fast path selects every test/gate that caught the historical defect; misses are blocking.
- [ ] On the reference machine, the median low-risk fast-path run is at most five minutes and at most 50% of the median `make verify` duration. If it misses either target, retain the measurements but do not market the target as a fast loop.
- [x] `make verify` remains the required pre-push/merge gate.

**A2 is complete only when every unchecked box is satisfied. Merged scripts and passing unit tests are not enough because the current repository-discovery defect can yield an empty or incomplete change set.**

**Non-goals:** auto-generating tests, skipping flaky failures, or claiming coverage for marker/live/device lanes that were not run.

### A3 — Ratchet existing architecture enforcement *(immediate engineering)*

- **Program mapping:** `DEMO-ENG-04`; continuous backend merge gate.
- **Status:** **COMPLETE.** Backend commit `dc80d75e5` is merged into `main` through `6fb382237`.
- **Verified 2026-08-12:** 1,471 modules, 4,287 top-level edges, and the exact four-module `home/concierge_feed` SCC match the committed ratchet; the import and lazy-import checks pass with 60 documented lazy exceptions and no new/stale entries; all 23 SCC tests pass.
- **Operational rule:** the existing SCC is accepted debt, not a target count. Any membership change—including an improvement—requires an intentional baseline review so the artifact records what changed.

- **Confidence:** medium-high.
- **DRI:** backend architecture owner.
- **Repository:** `travel-agent`.
- **Remaining effort:** none for A3; cycle removal is separate work.
- **Depends on:** no A0 dependency.

#### Shipped deliverables

1. `travel-agent/scripts/check_import_scc.py` parses every `backend/**/*.py` file with Python AST, resolves internal relative/absolute imports, and includes module-scope imports only. It excludes `TYPE_CHECKING` and function/class-body imports from the top-level graph while reporting their counts separately.
2. `travel-agent/scripts/check_import_scc_baseline.json` contains:
   - schema version;
   - source commit;
   - explicit inclusions/exclusions;
   - sorted module and edge counts;
   - sorted member lists for every SCC with more than one module; and
   - a SHA-256 of the canonicalized SCC list.
3. `--write-baseline <path>` and `--ci` modes ratchet exact SCC membership.
4. `travel-agent/tests/scripts/test_check_import_scc.py` covers the required parser and drift cases.
5. The gate is wired into backend `lint`, `ci`, the certificate gate, pre-commit, and GitHub Actions.
6. The checker documents the intentional baseline-update procedure.

#### Acceptance criteria

- [x] Two runs against the same commit produce byte-identical baseline JSON.
- [x] The current graph reproduces the exact four-file SCC.
- [x] A fixture that changes SCC membership while preserving scalar cycle count fails.
- [x] Existing checks report no top-level boundary violations and exactly 60 allowlisted lazy imports with no new or stale entries.
- These commands pass:

```bash
cd travel-agent
PYTHONPATH=. .venv/bin/python scripts/check_imports.py --ci
PYTHONPATH=. .venv/bin/python scripts/check_lazy_imports.py --ci
PYTHONPATH=. .venv/bin/python scripts/check_import_scc.py --ci
PYTHONPATH=. .venv/bin/pytest tests/scripts/test_check_import_scc.py -q
make ci
```

**Non-goals:** immediately eliminating the live SCC, rejecting all deferred imports, or changing package ownership rules inside this ticket.

### A4 — Test a lean root instruction manifest *(controlled trial)*

- **Program mapping:** `POST-DEMO-01`; no active demo task.
- **Status:** **DEFERRED UNTIL POST-DEMO AND BLOCKED BY A0.** No lean treatment file or trial result exists.
- **Confidence:** medium-low because published findings conflict.
- **DRI:** the named A0 evaluation owner; workspace maintainer approves treatment content.
- **Repository:** workspace evaluation variant only until the decision gate passes.
- **Effort:** 1 day to author/review the variant, then A0 runtime and review.
- **Depends on:** A0 pilot passing.
- **Next action:** none until Demo Phase 6 closes and A0's isolation smoke, pilot, and minimum-detectable-effect calculation pass. Then create only the treatment artifact below; do not edit the production root `AGENTS.md` before the result.

#### Treatment definition

- Control: the root `AGENTS.md` at the task's workspace base commit; child `AGENTS.md` files remain unchanged.
- Treatment: `docs/reliability/agent-velocity/variants/lean-root-AGENTS.md`, capped at 60 nonblank lines.
- Preserve only non-inferable constraints: separate child repositories, API schema/type-sync workflow, canonical verification commands, dirty-worktree/concurrent-session safety, explicit staging, and links to child rules.
- Remove prose that only inventories discoverable files or repeats child documentation.
- Record SHA-256 for both files in the variant manifest. The runner must verify the hashes before every run.

#### Acceptance and rollout

Run all A0 tasks, three repetitions per arm, randomized and blinded. Apply A0's generic adoption rule. Additionally, the treatment must have zero violations of repository separation, explicit-staging, or API contract workflow rules.

If it wins, update only the root `AGENTS.md`, run `make verify`, and retain the old file plus trial report in the evaluation evidence. If it is negative or inconclusive, keep the current file. Do not opportunistically edit child instructions from this result.

**Non-goals:** testing a model prompt rewrite, changing child rules, or reducing instructions merely to minimize token count.

### A5 — Trial structural indexing or a deterministic repository map *(controlled trial)*

- **Program mapping:** `POST-DEMO-01`; no active demo task.
- **Status:** **DEFERRED UNTIL POST-DEMO AND BLOCKED BY A0.** No product/configuration has qualified and no repository-map treatment exists.
- **Confidence:** medium; transferability unknown.
- **DRI:** the named A0 evaluation owner with a named security/privacy reviewer.
- **Repositories:** evaluation harness only until the decision gate passes.
- **Effort:** up to 2 days for qualification/integration, then A0 runtime and review.
- **Depends on:** A0 pilot passing and one intervention qualifying below.
- **Next action:** none until Demo Phase 6 closes and A0's pilot passes. Then time-box qualification to one day and record pass/fail against every criterion below before integrating anything.

#### Qualification gate

Time-box tool selection to one day. A structural index qualifies only if it:

- exposes a real enabled/disabled toggle with the same model and harness;
- can pin its version and configuration;
- records indexing time and query/tool usage;
- does not upload private source outside an approved processor/data policy;
- can index detached historical worktrees without seeing later commits; and
- can be fully removed from the treatment workspace between runs.

If no product qualifies, use a deterministic repository-map treatment generated from AST/export/import metadata. Name the experiment `repository-map`, not `indexing`, because prompt injection of a map is a different intervention. Store the generator, tests, version, map hash, generation time, and byte/token size under the A0 harness.

#### Acceptance and rollout

Run all A0 tasks, three repetitions per arm, with special reporting for four-or-more-file and cross-repository tasks. Apply A0's generic adoption rule. Index construction time, maintenance cost, and any recurring license/service cost count against the efficiency result.

Adopt only the pinned configuration that was tested. Add a removal command and verify that disabling/removing the tool restores the control environment. If negative or inconclusive, remove the integration and retain only the report. Do not purchase an annual plan or organization-wide license before the local result.

**Non-goals:** comparing models, granting the treatment extra tools unrelated to navigation, or treating a generated map as proof about a commercial index.

### A6 — Refactor one measured hot seam, then replay *(conditional)*

- **Program mapping:** no active task. A demo-blocking exception requires a new approved `DEMO-ENG-*` registry item; otherwise A6 remains post-demo.
- **Status:** **DEFERRED AND GATED, NOT STARTED.** No A0 report, qualifying failure cluster, or refactor decision record exists.
- **Confidence:** low until A0 identifies a repeated failure cluster.
- **DRI:** owner of the selected backend/frontend domain, with architecture reviewer.
- **Repositories:** whichever child repositories the selected seam genuinely spans.
- **Effort:** 3–10 engineering days after a scoped design review.
- **Depends on:** completed A0 report and completed A3 SCC tooling.
- **Next action:** none during Demo Phases 1–6 unless the Demo Program approves a new blocking-seam exception. Otherwise wait until A0 crosses the entry threshold below. If it does not, close A6 as “not justified”; do not select a seam by architectural intuition alone.

#### Entry gate

A seam qualifies only when at least three distinct A0 tasks, or at least 20% of the applicable multi-file task stratum, exhibit the same localization, change-spread, or dependency failure and blinded review attributes the failure to that seam. Record the cluster and competing explanations in `docs/decisions/<date>-agent-velocity-refactor-<seam>.md`.

The decision record must specify:

- old and proposed dependency direction;
- synchronous/asynchronous, transaction, delivery, retry, and failure semantics;
- behavior-preserving test/contract surface;
- exact files/packages in scope and explicit non-goals;
- migration steps and rollback commit;
- affected A0 task IDs; and
- why a tool, documentation, or test improvement is insufficient.

#### Implementation and comparison

Create equivalent control and refactor branches from the same base. Add characterization tests before moving production code. Run A3 and `make verify` on both branches. Replay only the predeclared affected-task subset, three repetitions per branch, with the same A0 configuration and blinded review.

For a `core.db` → `atlas.projector` seam, the default candidate is an explicit synchronous port owned by an orchestration layer. The current fire-and-forget event bus is not behaviorally equivalent unless the decision record redesigns and tests registration, delivery, retry, transaction, and exception semantics.

#### Merge/stop rule

Merge only when:

- all characterization, regression, contract, and structural gates pass;
- no affected task loses accepted-correct status;
- median time to accepted correctness improves by at least 15% **or** median changed-file count for the affected tasks falls by at least 20%;
- the SCC set and lazy-import allowlist do not grow; and
- normal engineering review finds the resulting ownership boundary clearer independent of agents.

If the comparison fails, archive the decision and measurements, delete or abandon the refactor branch, and stop treating that seam as an agent-velocity project. A normal product or reliability justification may still support separate future work.

**Non-goals:** repository-wide package moves, renaming-only churn, combining several seams in one trial, or introducing eventual consistency where callers require synchronous persistence.

### Explicitly not recommended

- Splitting packages based only on LOC or files per directory.
- Routing synchronous persistence work through the current event bus as a cleanup.
- Deleting frontend type layers based only on overlapping names.
- Purchasing or adopting indexing solely from a vendor benchmark or one public paper.
- Evaluating interventions with one run per task, visible reference patches, or agent-written tests alone.
- Using generated LOC, token consumption, or tool calls as the primary velocity metric.

---

## Exit

Before `expires` (2026-09-10), make and record these decisions:

- **`DEMO-ENG-01` / A1:** the Demo Program registry names the API-contract DRI and records either completed adjudication of all 87 exceptions before their 2026-09-11 expiry or an explicitly reviewed smaller batch and re-scoped remainder. Do not bulk-renew placeholder exceptions.
- **`DEMO-ENG-02/03` / A2:** the registry names the test-infrastructure and Demo Home DRIs. Repair the unsafe router or remove/disable `verify-changed`; resolve the Home ratchet through the demo-owned lane; retain `make verify` as the required gate until the repaired path passes acceptance.
- **`DEMO-ENG-05` / A2 evidence:** complete comparable measurements on frozen commits or record a named post-demo owner and dated checkpoint. Do not turn partial or concurrent measurements into a performance claim.
- **`DEMO-ENG-04` / A3:** no new implementation decision is required; retain the promoted SCC invariant and record any intentional baseline exception in the Demo Program.
- **`POST-DEMO-01` / A0, A4, A5:** keep the item explicitly deferred through Demo Phase 6. At the post-demo checkpoint, name the DRI/budget/harness and reactivate A0, or decline/defer the research again. A4/A5 never become independently actionable.
- **A6:** keep it without an active task unless A0 qualifies it or the Demo Program records a reviewed demo-blocking exception with its own `DEMO-ENG-*` ID.
- **Document state:** archive this note only after the mapped demo tasks are complete or durably transferred and `POST-DEMO-01` has a recorded decision. Extend the expiry only with named owners and dated checkpoints.

Default if untouched: do **not** infer approval for A0, A4, A5, or A6. The Demo
Program remains the execution authority. Keep A3's shipped invariant, treat A1's
exceptions and A2's router as open program risk, archive the point-in-time
structural counts as non-reproducible observations, and retain the research
synthesis plus detailed acceptance criteria as a supporting decision record.
