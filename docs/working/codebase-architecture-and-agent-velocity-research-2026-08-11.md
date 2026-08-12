---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-11
expires: 2026-09-10
why_new: Extends the July architecture-simplification audit with a point-in-time structural measurement, an adversarial review of research on coding-agent velocity, and a proposed private replay evaluation.
promotes_to: null
supersedes: []
---

# Codebase Architecture Quality and Agent-Velocity Research

**Date:** 2026-08-11
**Last revised:** 2026-08-11

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

## Action items — executable work plan

Ranked by evidence quality, decision value, cost, and reversibility. Estimates are one-engineer elapsed working time and exclude unattended model runtime. A named person must replace each role-level DRI before work starts.

### Execution order and dependencies

| Workstream | Item | May start when | Blocks |
|---|---|---|---|
| Immediate engineering | A1 contract derivation | An isolated frontend/backend worktree lane exists | Nothing; may run beside A0 |
| Immediate engineering | A2 verification baseline | Dependencies are installed on a clean, named commit | A2 fast-path implementation |
| Immediate engineering | A3 SCC ratchet | An isolated backend worktree lane exists | A6 architectural comparison |
| Agent-velocity evaluation | A0 replay harness | A DRI, spend ceiling, and working pinned Codex CLI exist | A4 and A5 trials |
| Agent-velocity evaluation | A4 instruction trial | A0 pilot passes | Instruction decision |
| Agent-velocity evaluation | A5 indexing trial | A0 pilot passes and an intervention qualifies | Indexing decision |
| Conditional architecture | A6 targeted refactor | A0 is complete and identifies a qualifying failure cluster | Any agent-specific restructuring |

### Rules shared by every item

- Run `make status` before starting. Do not implement in a canonical child checkout that contains another session's work.
- Use `./scripts/new-worktree.sh <lane>` or its `--agent-only`/`--app-only` form. Use one descriptive branch per child repository and stage explicit filenames only.
- Record the exact input commit, command, tool version, start/end time, and pass/fail result in the named evidence artifact.
- Do not weaken an existing full gate to make a fast gate pass. Fast paths supplement `make verify`; they do not replace the merge/pre-push gate until separately approved.
- Treat source, prompts, diffs, and trajectories as private. Do not commit credentials, CLI authentication, raw model transcripts containing secrets, or hidden verifier patches into an agent-visible task checkout.
- An item is complete only when its deliverables exist, its acceptance criteria pass, and its non-goals remain untouched.

### A0 — Build a private historical-task replay evaluation *(first research item)*

- **Confidence:** high that measurement is required; results unknown.
- **DRI:** workspace evaluation owner.
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

> **Re-checked 2026-08-12: still failing, identical `ENOENT`.** A0 remains blocked — not attempted. A1/A2/A3 above were executed without it, per the execution-order table's own dependency graph (none of them depend on A0). A4/A5/A6 remain correctly blocked on A0's pilot/report and are likewise not attempted. Repairing the CLI, assigning a DRI, and approving a spend ceiling are still open, and none of them are something to fabricate or route around.

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

> **Executed 2026-08-12** on branch `codex/agent-velocity-hardening` (all three repos), not yet
> merged. `travel-app` commit `46b25f4a` (`check-schema-bridge.mjs` + manifest + tests),
> `travel-agent` commit `50e6585fb` (removal), workspace commit `23c7d48` (contract-check.sh
> wiring). Found real, previously-unknown contract drift while building the manifest — see the
> commit message for `TripStatus`/`ProposalResolveStatus`/two `DossierExemplar` enums, each
> recorded with an unassigned owner rather than a fabricated name. 87 of 340 exports landed as
> `unmodeled_wire` needing human review before their expiry (2026-09-11).

- **Confidence:** high; contract single-source-of-truth is valuable independent of agents.
- **DRI:** frontend/API-contract owner.
- **Repositories:** `travel-app`, with removal of the superseded checker/hook in `travel-agent`.
- **Effort:** 2–4 engineering days.
- **Depends on:** no A0 dependency; use an isolated cross-repository lane.

#### Starting point

`travel-agent/scripts/check_schema_bridge.py` already compares annotated frontend field names with `schema.gen.ts` and is wired into pre-push. It currently passes but covers only two `@schema` annotations (`StayCandidate` and `AtlasFacetSuggestions`), scans `types.ts` and `travel-app/types/*.ts`, does not scan `utils/api/interface.ts`, and validates field names rather than full TypeScript compatibility.

#### Deliverables

1. Add `travel-app/scripts/schema-bridge-manifest.json`. Inventory every exported interface/type in `utils/api/types.ts` and `utils/api/interface.ts` with:
   - symbol and source file;
   - classification: `generated_alias`, `schema_projection`, `adapter`, `ui_only`, or `unmodeled_wire`;
   - generated schema name when applicable;
   - route and method for `unmodeled_wire`;
   - rationale; and
   - owner plus expiry for every `unmodeled_wire` exception.
2. Add `travel-app/scripts/check-schema-bridge.mjs` using the installed TypeScript compiler API rather than regex parsing. It must read and validate the manifest, enumerate exports from both facade files, reject unclassified exports, reject missing generated schema names, and fail stale `unmodeled_wire` exceptions.
3. Add `travel-app/scripts/check-schema-bridge.test.mjs` covering every classification, multiline/nested declarations, aliases, missing models, duplicate entries, stale exceptions, and useful error locations.
4. Add `schema-bridge` and `schema-bridge:test` package scripts, include `schema-bridge` in `verify:fast`, and invoke it from the workspace `contract-check` path.
5. For `schema_projection`, replace copied field declarations with aliases or `Pick`/`Omit`/intersection derivations from `components["schemas"]` when that preserves semantics. Keep deliberate UI refinements and adapters explicit.
6. Once the new AST-based checker passes on the same known annotations and the complete manifest, remove `travel-agent/scripts/check_schema_bridge.py` and its backend pre-push hook in the same cross-repository change. Do not leave two canonical implementations.

#### Acceptance criteria

- Every exported interface/type in the two API facade files is classified exactly once.
- No `generated_alias` or `schema_projection` independently copies a complete generated wire shape.
- Every remaining `unmodeled_wire` item names a route, owner, reason, and unexpired removal date.
- Intentional adapters and UI-only types remain source-compatible; wholesale deletion of `types.ts` or `interface.ts` is prohibited.
- These commands pass from the workspace root:

```bash
make sync-types-snapshot
make contract-check
make typecheck
(cd travel-app && npm run schema-bridge)
(cd travel-app && npm run schema-bridge:test)
(cd travel-app && npm run verify:fast)
```

The generated snapshots and `schema.gen.ts` must have no unexplained diff. A1 is complete when the reviewed manifest and checker make any new unclassified wire-like export fail CI.

**Non-goals:** renaming unrelated frontend domain types, changing API behavior, or replacing deliberate frontend adapters with raw generated types at every call site.

### A2 — Measure and improve the trusted verification loop *(immediate engineering)*

> **Executed 2026-08-12** on the workspace repo, branch `codex/agent-velocity-hardening`
> (commits `26c7f3b`, `f4f941e`), NOT merged. Tools built and tested in full (53 tests total);
> baseline measurement is **partial** — 1 of the required 3 repetitions, 4 of the required 20
> historical diffs. Full gaps and current numbers: [`docs/reliability/test-loop-baseline.md`](../reliability/test-loop-baseline.md).
> Headline: `make -C travel-agent ci` and `npm run verify:full` are both currently red on `main`
> for two unrelated pre-existing reasons (flagged separately, not fixed here); the 17,776-test
> offline suite underneath them is itself green in ~7.4 minutes.

- **Confidence:** high on the mechanism; current baseline unknown.
- **DRI:** workspace test-infrastructure owner, with backend and frontend reviewers.
- **Repositories:** workspace plus both child repositories only where a new target is required.
- **Effort:** 1–2 days for measurement; 3–5 days for a conservative fast path.
- **Depends on:** installed dependencies and a clean, named commit in isolated worktrees.

#### Baseline deliverables

- `scripts/measure_verification.py` that records command, commit IDs, environment class, wall time, exit status, collected/passed/failed/skipped counts when available, and log path.
- `scripts/tests/test_measure_verification.py` for timeout, nonzero exit, JSON schema, and partial-result behavior.
- `docs/reliability/test-loop-baseline.json` as machine-readable evidence.
- `docs/reliability/test-loop-baseline.md` summarizing the reference machine, exclusions, failures, flakes, and slowest lanes.

Run the following three times on the same clean commits, with no source edits between repetitions:

```bash
make doctor
make -C travel-agent ci
make contract-check
cd travel-app && npm run verify:full
```

Measure `make test-backend-postgres` separately against a disposable database. List API-key, dogfood, device, and live-service suites as separate coverage lanes; never describe the measured set as the "full suite" while one is excluded. If any nominally deterministic command changes outcome across three runs, run it ten times, record the failing test IDs, and fix or quarantine with an owner and expiry before optimizing selection.

#### Fast-path deliverables

- A root `make verify-changed BASE_REF=<ref>` target implemented by `scripts/verify-changed.sh` or an equivalently tested script.
- A dry-run mode that prints changed files, selected commands, and the reason for each selection.
- Unit tests for every path class and for unknown-path fallback.
- A decision table in `docs/reliability/test-loop-baseline.md` mapping path classes to commands.

Minimum routing rules:

- Unknown paths, shared test configuration, `conftest.py`, migrations, dependency manifests, workspace scripts, API models/routes, `docs/openapi*.json`, or generated-schema tooling select `make verify`.
- Frontend `.ts`/`.tsx` changes run `npm run verify:fast` and Jest `--findRelatedTests` for the changed files. If Jest finds no tests for production code, select the full frontend Jest lane.
- Backend changes always run import/lazy-import/SCC gates plus lint. Until a tested dependency-to-test mapper exists, uncertain backend changes select `make -C travel-agent ci`.
- Documentation-only changes run the existing documentation governance/link gates; executable examples additionally run their referenced checker tests.
- The script must exit nonzero when `BASE_REF` is missing or unresolved; it may not guess `main` in a dirty concurrent worktree.

#### Acceptance criteria

- Baseline artifacts identify exact commits and contain all three repetitions, including failures and skips.
- `verify-changed --dry-run` is deterministic for the same diff.
- Every unrecognized or high-risk change falls back to `make verify`.
- On a reviewed sample of at least 20 historical diffs, the fast path selects every test/gate that caught the historical defect; misses are blocking.
- On the reference machine, the median low-risk fast-path run is at most five minutes and at most 50% of the median `make verify` duration. If it misses either target, retain the measurements but do not market the target as a fast loop.
- `make verify` remains the required pre-push/merge gate until a separate decision changes that policy.

**Non-goals:** auto-generating tests, skipping flaky failures, or claiming coverage for marker/live/device lanes that were not run.

### A3 — Ratchet existing architecture enforcement *(immediate engineering)*

> **Executed 2026-08-12** on branch `codex/agent-velocity-hardening` (`travel-agent` commit
> `dc80d75e5`), not yet merged. Real baseline against the current graph reproduces the original
> 4-file `home/concierge_feed` cycle (1,471 modules, 4,287 top-level edges — close to but not
> identical to the original scratch-script counts, as expected since exclusion rules are now
> exact rather than approximate). 23 tests. Wired into `lint`, `ci`, the cert-db gate,
> pre-commit, and GitHub Actions.

- **Confidence:** medium-high.
- **DRI:** backend architecture owner.
- **Repository:** `travel-agent`.
- **Effort:** 2–3 engineering days.
- **Depends on:** isolated backend lane; no dependency on A0.

#### Deliverables

1. Add `travel-agent/scripts/check_import_scc.py`. Parse every `backend/**/*.py` file with Python AST, resolve internal relative/absolute imports, and include module-scope imports only. Exclude `TYPE_CHECKING` and function/class-body imports from the top-level graph, but report their counts separately.
2. Add `travel-agent/scripts/check_import_scc_baseline.json` containing:
   - schema version;
   - source commit;
   - explicit inclusions/exclusions;
   - sorted module and edge counts;
   - sorted member lists for every SCC with more than one module; and
   - a SHA-256 of the canonicalized SCC list.
3. Add `--write-baseline <path>` and `--ci` modes. `--ci` must fail on a new, removed, enlarged, shrunk, or membership-changed SCC so every change requires deliberate baseline review; an improvement is not silently discarded.
4. Add `travel-agent/tests/scripts/test_check_import_scc.py` covering relative imports, aliases, multiline imports, `TYPE_CHECKING`, deferred imports, syntax errors, deterministic ordering, baseline drift, and two disjoint cycles with the same scalar count.
5. Wire `--ci` into `travel-agent/Makefile` `gates`/`ci`, `.pre-commit-config.yaml`, and `.github/workflows/ci.yml` beside `check_imports.py` and `check_lazy_imports.py`.
6. Document the exact baseline-update command and architectural justification requirement in `travel-agent/AGENTS.md` or the checker help text, not both unless one links to the other.

#### Acceptance criteria

- Two runs against the same commit produce byte-identical baseline JSON.
- The current graph's SCC membership is reproduced; any discrepancy with the original four-file observation is documented rather than forced to match it.
- A fixture that swaps one SCC member while preserving cycle count fails, proving this is not a scalar-count gate.
- Existing checks still report no top-level boundary violations and exactly the current allowlisted lazy-import inventory with no new or stale items.
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

- **Confidence:** medium-low because published findings conflict.
- **DRI:** A0 evaluation owner; workspace maintainer approves treatment content.
- **Repository:** workspace evaluation variant only until the decision gate passes.
- **Effort:** 1 day to author/review the variant, then A0 runtime and review.
- **Depends on:** A0 pilot passing.

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

- **Confidence:** medium; transferability unknown.
- **DRI:** A0 evaluation owner with security/privacy reviewer.
- **Repositories:** evaluation harness only until the decision gate passes.
- **Effort:** up to 2 days for qualification/integration, then A0 runtime and review.
- **Depends on:** A0 pilot passing and one intervention qualifying below.

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

- **Confidence:** low until A0 identifies a repeated failure cluster.
- **DRI:** owner of the selected backend/frontend domain, with architecture reviewer.
- **Repositories:** whichever child repositories the selected seam genuinely spans.
- **Effort:** 3–10 engineering days after a scoped design review.
- **Depends on:** completed A0 report and completed A3 SCC tooling.

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

Before `expires` (2026-09-10), choose one:

- **Promote** the reproducible import-graph/SCC checks and any validated generated-contract rule into durable tooling;
- **Record a decision** to run or decline A0, including the task set, fixed conditions, and decision threshold;
- **Archive** this review after its verified local findings are incorporated into the July architecture note or superseded by private replay results; or
- **Extend** the expiry only if A0 is actively running and has a named owner.

Default if untouched: archive the point-in-time structural counts as non-reproducible observations and retain the research synthesis as a decision record. Do not promote the original counts into invariants without rerunning a committed analysis artifact.
