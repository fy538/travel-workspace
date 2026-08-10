---
doc_type: working
status: blocked
owner: AI systems / evaluation / product
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Records the exact AI-R1 implementation boundary so offline/dark work is not mistaken for a live AI rollout.
related:
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
  - ai-decision-and-learning-research-agenda-2026-08-10.md
  - intentional-convergence-engineering-plan-2026-08-10.md
---

# AI decision-and-learning R1 execution status

## Integration base and ownership

This work ran in the dedicated AI-DL lane required by the engineering plan.
It did not modify the four A–D convergence worktrees or add a mobile consumer.

| Repository | Base revision | AI-R1 branch |
| --- | --- | --- |
| Workspace | `5d7c60ff573c575834a1760d57692ba8c427afe4` | `codex/ai-decision-learning-r1` |
| Travel Agent | `b3fd6b4125106f8193f0b4e12da13fff93a32a17` | `codex/ai-decision-learning-r1` |
| Travel App | `aba00ae32946d279411836a0337f2df0d41c2cde` | `codex/ai-decision-learning-r1` |

The app worktree is intentionally unchanged: no AI-DL phase has satisfied the
private device or group multi-device prerequisites for a mobile surface.

## Implemented boundary

| Phase/package | Implemented now | Evidence and boundary |
| --- | --- | --- |
| AI-0 / AI-001–003 | Frozen schema contracts, product-proof adapter, deterministic hard validators, corpus manifest, trial reports, versioned artifact registry, and human-anchor schema | Offline S/M contracts and fixture tests. No real human-anchor review has been recorded. |
| AI-1 / AI-004–006 | Deterministic Decision Set baseline, typed structured-response adapter, policy comparison runner, adaptive routing policy, content-free ledger adapter | The ledger helper has no production caller. No provider was invoked and no shadow decision has been recorded against a real concierge turn. |
| AI-2 / AI-007–008 | Conservative promotion/retrieval projection; correction/temporal/active applicability checks; exact companion-roster retrieval guard | No new candidate store or runtime learning writer was created. The existing relationship-memory authority remains the writer. |
| AI-3 / AI-009–010 | Group aggregation baselines, counterfactual privacy predicate, group-composer hard gate | Offline-only. No group composition, proposal, or mutation path is invoked by AI-DL. |
| AI-4 / AI-011–012 | Private-only eligibility assessment, no-send/propensity validation, content-free shadow receipt adapter, sample-size assumption helper | No runtime eligibility consumer, study protocol, consent enrollment, or delivery log exists. |
| AI-5 / AI-013 | Canary guard validates private/reversible/device-receipt preconditions | Not implemented as a canary: no physical-device receipt, approved cohort, or study authorization exists. |
| AI-6 / AI-014–015 | Travel Injection Suite aggregator, final-state validators, evaluator calibration and human-gated promotion recommendation | Fixture-only. A clean result is at most eligible for human review, never automatically approved. |
| AI-7 / AI-016 | Group guardrails and offline evaluator support only | Not implemented: the required privacy, canonical path, consent, and multi-device gates are not satisfied. |

## Backend commits

The backend branch is a linear, reviewable series:

1. `40fb0148e` — product-proof `EvalTrial` adapter and evidence-aware report.
2. `13081585a` — deterministic shadow routing and governed claim projection.
3. `9ed624910` — Group/Proactive/Security offline labs.
4. `61000b544` — content-free append-only shadow decision receipt adapter.
5. `bafa9d0c6` — immutable artifact registry and human-anchor contract.
6. `c0a7b0330` — Decision Set runner and baseline comparison.
7. `f03cc9f97` — stale-evidence and irreversible-action hard gates.
8. `d16df3fbd` — exact companion roster retrieval guard.
9. `847b3fd40` — private proactive eligibility and pre-study power assumptions.
10. `3d6ed13cf` — injection suite and human-gated evaluator promotion.
11. `3349de7ad` — typed, copy-free structured policy adapter.

## Verification performed

- Focused AI-DL and shadow-ledger tests: **44 passed** on the Travel Agent
  AI-R1 branch.
- Ruff checks and formatting passed for every changed file.
- Each commit passed the repository pre-commit checks.

These are S/M-level implementation checks. They do not establish backend-real
shadow coverage (B), device behavior (D/V), human-anchor agreement (H), or
causal impact (C).

## Gate before any runtime shadow consumer

Do not connect `record_shadow_decision` or the structured adapter to concierge
serving until all of the following are recorded:

1. A narrow private Decision Set family, allowlisted surface, and policy/model
   revisions are selected by product and AI systems.
2. The frozen human anchor set is adjudicated and the candidate is compared
   with the deterministic baseline under the declared metrics.
3. Privacy/security approve the content-free shadow telemetry retention and
   review scope.
4. Backend observability confirms shadow latency/cost limits and the ledger
   failure path remains non-blocking.
5. The integration owner explicitly enables a registered, independently
   kill-switchable shadow-only consumer.

## Gates before a canary or group-visible behavior

AI-5 needs an approved private cohort, no-send holdout, delivery/deep-link /
dismissal/cooldown/kill-switch physical-device receipts, and a causal analysis
protocol. AI-7 additionally needs accepted roster-revocation, viewer-safe
projection, group-composition and canonical-proposal evidence, explicit group
consent, and a physical multi-member device script.

Until then, the appropriate product behavior is unchanged: use the existing
serving path, make no additional proactive delivery, create no durable inferred
claim, and send no group-visible AI-DL output.
