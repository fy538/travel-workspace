---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-11
expires: 2026-09-10
why_new: First holistic structural read of both repos, paired with three adversarial rounds of external research on agent-friendly codebases. No existing note covers cross-repo architecture quality or evaluates the evidence behind agent-velocity investments.
promotes_to: null
supersedes: []
---

# Codebase Architecture Quality and Agent-Velocity Research

**Date:** 2026-08-11

## Question or outcome

Two questions, asked in sequence:

1. Is the backend/frontend architecture structurally sound?
2. Should we restructure the codebase to make AI coding agents faster, and what does the evidence actually support?

The short answers: **yes, the architecture is sound but unguarded**, and **no, the evidence does not support restructuring for agents** — only one of the five candidate actions survives scrutiny, and it survives because it was good engineering independent of agents.

---

## Evidence

All measurements taken 2026-08-11 against the working tree at `~/travel-workspace`. Point-in-time, not durable state.

### Part 1 — Structural audit

**Method.** Package/file sizing via `find`/`wc`. Import graph built with an AST parser over all 4,056 backend `.py` files, resolving relative and absolute imports to a module map, recording top-level and function-body (deferred) imports separately, then Tarjan SCC for cycles. Counterfactual run: hoist each deferred import to module top and test whether the target already reaches the source. Analysis scripts were ephemeral (session scratchpad); method described here is sufficient to reproduce.

**Scale.**

| | Backend (`travel-agent`) | Frontend (`travel-app`) |
|---|---|---|
| Files | 4,056 `.py` | 2,553 `.ts`/`.tsx` |
| LOC | 1,033,308 | 505,495 |
| Modules in graph | 1,458 | — |
| Tests | 19,043 collected | 1,038 test files |

**Frontend: structurally sound.**

- One state paradigm — react-query in 89 files, context in 28, zero Redux/zustand/jotai/recoil/mobx.
- One data layer — 238 files import `utils/api`, 42 use raw `fetch`.
- Feature-organised components, 46 subdirectories, real nesting.
- Existing boundary enforcement: 58 checker scripts including `scripts/check-api-boundaries.mjs`, `check-query-key-ownership.mjs`, `check-mutation-key-ownership.mjs`.

Blemishes: 8 overlapping `trip*` component directories (`trip/`, `trips/`, `trip-details/`, `trip-plan/`, `trip-map/`, `trip-itinerary/`, `trip-settings/`, `trip-creation/`) — a boundary never decided. 479 entries at repo root, mostly screenshot PNGs.

**Backend: correct macro shape, no enforcement.**

Good, and worth protecting:

- `core.models` — 623 fan-in / 9 fan-out. Textbook foundation leaf.
- `core.exceptions` — 73 fan-in / 0 fan-out. Pure leaf.
- `core.db` fan-out is ~90% internal (378 `core.db`, 117 `core.models`, 15 `core.exceptions`).
- `api.routes` — 686 out / 90 in. Correct direction for a top layer.
- **Exactly one import cycle** across 1,458 modules and 4,247 top-level edges: `home/concierge_feed` (4 files). At this scale that is rare and valuable.

Problems:

1. **`core/` is a second application layer, not a kernel.** 191,458 LOC (37% of backend), **194 loose `.py` files** at its top level, 55 of them named after features (`booking_approval.py`, `booking_consent.py`, `atlas_unpacked_share.py`, `ambient_judgment.py`). It has no definition, so it cannot reject anything. `concierge/` has the same shape: 73,519 LOC, 128 loose files.

2. **The acyclic graph is accidental.** 2,030 deferred (in-function) imports exist. Counterfactual test: **1,997 of 2,030 (98%) could be hoisted to module top with no cycle created.** Only 33 are load-bearing. The habit is cargo-cult, not analysis — meaning nothing defends the DAG. Hoisting everything yields 10 cycles across 258 files; the largest is a 221-file component spanning `core.db` (38), `concierge.tool_handlers` (26), `booking_agent.tasks` (8).

3. **Real dependency inversion at the bottom.** `core/db/atlas.py` imports `backend.atlas.projector` at 8 call sites plus `atlas.geography`, `atlas.dedup`, `atlas.kept_place_affinity`, `atlas.place_labels`. `core/db/trips/crud.py:222,856,911` reaches into `atlas.projector`, `digest.engine`, `concierge.reflection`. `core/tools/registry.py` pulls 5 of 8 tools from `research_agent.tools.*`. Almost all deferred, which is what keeps the cycle count at one.

4. **Two mechanisms for one job.** `atlas.projector` is called directly from 5 files (`core/db/atlas.py`, `core/db/trip_templates.py`, `core/db/trips/crud.py`, `api/routes/itinerary_operations.py`, `api/routes/atlas.py`) while `itinerary_projection.ready` and `memory_projection.ready` route through `core/event_bus.py`. The bus is the right primitive (136 LOC, `emit`/`subscribe`) but adoption stalled: ~12 distinct event types, most emitted once.

5. **Frontend contract truth is duplicated.** `utils/api/schema.gen.ts` (generated, 43,287 lines, 1,352 component types, 65 importers) and `utils/api/types.ts` (hand-written, 320 types, 162 importers) **both define 102 of the same type names**. The hand-maintained copy has 2.5x the adoption of the generated one, and nothing syncs them. A backend field change regenerates one, leaves the other stale, and the app still typechecks. Also: `utils/api/interface.ts` is 3,113 lines with 2 importers (dead); 17,883 LOC of mock fixtures are imported by 15 non-test files.

6. **Verification signal is not trustworthy.** 19,043 tests. A targeted run surfaced a failure on main (`tests/concierge/test_change_proposals.py::TestProposeChangeExecution::test_bounded_opening_persists_a_valid_local_wall_time_add`), consistent with the known red baseline. 213 tests took 27.9s with 14,553 deselected; extrapolated full-suite runtime is on the order of 30 minutes (estimate, not measured).

**Corrections made during the audit** — recorded so the reasoning is auditable:

- An initial pairwise grep suggested widespread cycles (`concierge↔notifications`, `home↔places`). AST analysis showed **one** cycle. The grep counted deferred imports as edges.
- A first pass framed 46% deferred imports as evidence of tangled boundaries. The counterfactual showed 98% are freely hoistable — the tangle is 33 edges, not 491.
- A recommendation to add import-boundary CI was partly redundant: the **frontend already has it** (`check-api-boundaries.mjs`). The gap is backend-only.

### Part 2 — External research, three adversarial rounds

Round 1 gathered supporting material. Rounds 2 and 3 attacked it. Summary of where each claim landed:

| Claim | Source | Verdict |
|---|---|---|
| Agents degrade sharply with codebase size | RepoMod-Bench (independent): 91.3% pass <10K LOC vs 15.3% >50K LOC, 76-point collapse | **Direction confirmed.** Task is cross-language translation, harder than feature work; thresholds do not transfer |
| 400K LOC is the threshold where grep-based navigation fails | Sourcegraph CodeScaleBench | **Weak.** Single vendor source; the Tessl post restates it, it is not a second source |
| +0.259 reward / 96→5 tool calls from code intelligence | Sourcegraph CodeScaleBench | **Conflicted.** The evaluated tool is Sourcegraph's own MCP; only agent tested was Claude Code + Haiku 4.5, the configuration most helped by external retrieval. Benchmark and traces are public, which is better than most vendor work |
| Harness/tooling investment improves agent quality | "Don't Blame the LLM": 35 sequential Qwen Code CLI releases, fixed model, 50 SWE-bench Verified tasks | **Disconfirming.** Resolve rate flat at ~30.5%, no significant improvement; tokens +70%. Context Management was among the highest-regression-risk components. Measures a vendor's harness, not our repo |
| False premises drive 30.7% of decisive errors; median failure at step 7, hidden ~10 steps; 57.9% epistemic | "Failure as a Process" preprint — 1,794 trajectories, 21 scaffold×model combos, human annotation κ 0.78–0.94 | **Good study, wrong domain.** Runs on Terminal-Bench: 240 containerised CLI tasks. Authors state it covers "benchmark tasks rather than real-world repositories" |
| Verification gives 2-3x quality | Boris Cherny, repeated across interviews | **Practitioner claim, not a measurement.** Direction corroborated by Spotify (judge vetoes ~25% of sessions, half self-correct) |
| AI makes experienced devs 19% slower | METR RCT: 16 devs, 246 tasks, repos averaging 1M+ LOC | **Real but dated.** Tested Cursor Pro + Claude 3.5/3.7, Feb–Jun 2025 — a tooling generation before agentic CLIs. Devs believed they were 20% faster; perception was inverted |
| METR's follow-up reverses that | METR, Feb 2026 | **Compromised.** They redesigned the experiment because adoption broke recruitment. Late-2025 range spans 18% speedup to 4% speedup, wide CIs, heavy selection bias. METR's own words: "only very weak evidence" |
| AI raises throughput but hurts stability; review becomes the bottleneck | DORA 2025 (throughput +2–18%, stability down); Faros AI 2026 (median PR review time +441%, PR size +51.3%, 22,000 devs) | **Directionally supported, magnitude unreliable.** Faros is telemetry not survey, but compares low- vs high-adoption periods within orgs — not causal. Another source reports +91% for the same metric |
| Salesforce output +151.3% | Search summary | **Unverified.** Passed through without provenance check; do not cite |

**The pattern across all three rounds:** every claim that specifically supports *"restructure your codebase for agents"* is vendor-produced, benchmark-bound, or unmeasured. The claims that survive are ones that were good engineering before agents existed.

**There is no clean causal measurement of the tools we actually use.** The only rigorous RCTs are METR's (dated, n=16, follow-up compromised) and older Copilot workplace trials. Anthropic has a randomized study underway with a 1,260-person baseline fielded early 2026; unpublished.

---

## Action items

Ranked by evidence quality × cost, not by appeal.

### A1 — Collapse frontend contract truth to one source *(do this)*

**Confidence: high — justified without any agent research.**

Delete the 102 hand-written type twins in `utils/api/types.ts`, re-point importers at `utils/api/schema.gen.ts`, delete `utils/api/interface.ts` (3,113 lines, 2 importers). Add a checker that fails when a hand-written type shadows a generated one — the `check-api-boundaries.mjs` pattern already exists to copy.

*Rationale:* two definitions of one contract will drift, and the drift typechecks green. True regardless of whether agents ever help. This is the only item that survived all three research rounds, because it never depended on contested evidence.

### A2 — Restore a green test baseline *(do this)*

**Confidence: high — same reasoning.**

Fix or explicitly quarantine the failing suites, starting with `tests/concierge/test_change_proposals.py`. A red baseline means "tests pass" cannot function as a signal for anyone, human or agent.

### A3 — Make the inner verification loop fast *(do this, after A2)*

**Confidence: medium.** Mechanism well-supported, multiplier unproven, and the harness-evolution study is a caution against assuming tooling gains.

Change-scoped test selection so verification is seconds rather than a ~30-minute full run. Cheap and sensible on its own terms.

### A4 — Backend import-direction checker *(do this)*

**Confidence: medium-high — protects a property we already have.**

Assert: `core.db` may not import feature packages at module top; total cycle count may not exceed 1 and must ratchet down; the 33 load-bearing deferred edges are an explicit, shrinking allowlist. Mirrors existing frontend checkers and the charter-invariant machinery.

### A5 — Finish the two half-migrations *(schedule)*

**Confidence: medium.**

Route `core/db → atlas.projector` calls through `core/event_bus.py`, or decide the bus is not the mechanism and remove it. A primitive at ~30% adoption is worse than either endpoint because every call site becomes a choice nobody documented. Same logic applies to generated types once A1 lands.

### A6 — Reduce navigation entropy *(schedule)*

**Confidence: medium.** Supported in direction by the independent size research; specific thresholds not transferable.

Split `core/` (194 loose files) and `concierge/` (128) into named subpackages. Decide the `trip*` frontend boundary. Move 479 root-level PNGs out of the frontend repo root. Untangle `home/concierge_feed` before more surfaces depend on it — it is the one live cycle and is the ranker earmarked for trips-home adoption.

### A7 — Code intelligence indexing *(do not buy on the literature)*

**Confidence: low.**

The benefit claim is vendor-sourced with an acknowledged conflict, and the one independent study of tooling evolution found no measurable gain across 35 releases. If pursued, run a time-boxed A/B on our own repo and measure it, rather than adopting on the published number.

### A8 — Instrument before and after *(do this alongside A1–A3)*

**Confidence: high — this is the item that makes the rest knowable.**

Track cycle time, PR size, time-to-first-review, and change failure rate before and after A1–A3. METR's most robust finding is that developer perception of AI speedup was measured pointing the *wrong way* — a 19% slowdown experienced as a 20% speedup. Our own instrumented numbers will be worth more than anything currently published.

**Explicitly not recommended:** restructuring the architecture primarily to serve coding agents. The evidence does not support a step change from codebase changes alone. A1–A6 are worth doing because they are correct engineering; any agent benefit is upside, and should be measured rather than assumed.

---

## Exit

Before `expires` (2026-09-10), choose exactly one:

- **Promote** A4's rule set into the charter-invariant checkers and A1's constraint into a frontend checker — that is the durable half of this note;
- **Record a decision** if we deliberately choose not to pursue agent-oriented restructuring, since the research supporting that choice is here and will not be re-derived cheaply;
- **Archive** the research table as historical evidence once A1–A3 land and our own measurements supersede published claims; or
- **Delete** if the checkers and instrumentation carry the truth in code.

Default if untouched: archive Part 2, promote Part 1's measurements into an audit record, since structural numbers will go stale within weeks of active work.
