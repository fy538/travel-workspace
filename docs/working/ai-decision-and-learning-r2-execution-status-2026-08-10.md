---
doc_type: working
status: active
owner: engineering / AI systems / product / evidence
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Reconciles the post-cleanup AI architecture audit with the implemented source-only control-plane slices, without promoting offline or dark-path checks to device, human, causal, or release evidence.
related:
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
  - ai-decision-and-learning-research-agenda-2026-08-10.md
  - convergence-and-ai-decision-next-execution-plan-2026-08-10.md
  - intentional-convergence-engineering-plan-2026-08-10.md
  - thesis-to-experience-convergence-audit-2026-08-09.md
  - home-surfaces-post-consolidation-engineering-plan-2026-08-09.md
  - cross-slice-engineering-coherence-audit-2026-08-09.md
  - ../../travel-agent/docs/working/profile-system-and-relationship-views-2026-08-09.md
---

# AI decision and learning R2 execution status

## Purpose

This is the execution companion to the [AI decision and learning engineering
plan](ai-decision-and-learning-engineering-plan-2026-08-10.md). It records
what is now implemented in source, which architecture gaps were closed, and
which gates cannot be satisfied by a coding session.

It also preserves the causal dependency on the four pivot audits:
[thesis to experience](thesis-to-experience-convergence-audit-2026-08-09.md),
[Home surfaces](home-surfaces-post-consolidation-engineering-plan-2026-08-09.md),
[profile and relationship views](../../travel-agent/docs/working/profile-system-and-relationship-views-2026-08-09.md),
and [cross-slice coherence](cross-slice-engineering-coherence-audit-2026-08-09.md).
Those documents establish the product truth, scope, and projection contracts
that the AI layer consumes; this work does not replace their authorities.

## Source implementation completed in this round

| Slice | Implemented boundary | Commit |
| --- | --- | --- |
| Typed private shadow | Build the frame only after loaded, authorized turn state; schedule a disabled, allowlisted, fail-open observer | `55231adb7` |
| Learning admission | Content-free evidence envelope and store policy kernel; inferred behavior cannot request durable promotion | `6a6eb2b9c` |
| Tool authority | Every commit-capable concierge tool has a closed semantic mutation class | `7345efc28` |
| Root identity | Proactive turns establish an `AIRunContext` root around the existing delivery call | `6c933401d` |
| Release posture | Explicit surface manifest and deterministic/shadow/canary eligibility contract | `1ad7e365b` |
| Decision source/outcome joins | One scope-bound source snapshot generates evidence and causal dependencies; outcome joins are content-free | `08a1e45f7` |
| Runtime/eval vocabulary | Closed runtime-record to offline-eval action mapping fails on vocabulary drift | `d41f66b86` |
| Proactivity treatment ledger | Existing arbitration receipt carries a content-free send/no-send decision, chosen arm, and propensity | `6f5459fbd` |
| Architecture | Canonical control-plane lifecycle, authority, evaluation, release, and change rules | `6a627bbf3` |

All commits are on the backend branch `codex/ai-suite-coherence` at the time
of this record. The mobile repository is intentionally unchanged: no private
or group AI-DL surface has earned a device-facing implementation.

## Coherent current architecture

```text
existing domain truth / context / scope / freshness
  -> AIRunContext + DecisionSourceSnapshot
  -> ephemeral DecisionFrame + deterministic family veto
  -> content-free DecisionRecord
  -> existing canonical executor and receipt (only when independently authorized)
  -> DecisionOutcomeLink
  -> LearningEvidenceEnvelope -> existing owning store

offline evaluator <--- content-free vocabulary adapter --- runtime record
```

The important invariant is directionality. The model may choose only among
authorized bounded actions. It does not create a parallel writer for itinerary,
proposal, booking, expense, profile, relationship memory, or notification
truth. Private frame data is never a durable telemetry payload, and group text
continues to require the sanctioned group composer.

## Phase disposition

| Engineering phase | Code disposition | Evidence still required before the next posture |
| --- | --- | --- |
| AI-0 evaluation spine | Implemented; frozen contracts, validators, corpus/anchor/promotion machinery exist | Human anchors and calibration are still H, not source evidence |
| AI-1 bounded private policy/shadow | Implemented dark and disabled; first family deterministically abstains when grounded options are unavailable | Retention/privacy approval, real shadow observations, latency/cost report, named allowlist approval |
| AI-2 governed learning | Admission kernel and exact-roster relationship-memory revocation are implemented | Store-specific audited producer, correction/forgetting behavior on the final consumer, user-facing provenance/device proof if surfaced |
| AI-3 group lab | Offline aggregation, group composer gate, and privacy counterfactuals exist | Approved narrow use case, direct/inferential privacy review, canonical proposal evidence, multi-member device script and consent |
| AI-4 proactive instrumentation | Existing arbiter now writes explicit treatment/no-send/propensity semantics | Study protocol, eligibility/exclusion reconciliation, delivery and negative-outcome joins, privacy/product approval |
| AI-5 private canary | Deliberately not enabled | Cohort/consent, stable randomization, physical-device receipt, cooldown/kill-switch proof, predeclared causal analysis |
| AI-6 injection and adaptive routing | Fixture suite, adaptive route selector, and evaluator promotion controls exist | Broader attack corpus/runner execution, human calibration, category budgets, security review |
| AI-7 group-visible canary | Deliberately not implemented | All AI-3 prerequisites plus Plan/Map revision and multi-device evidence |

`Implemented dark` means only that the source boundary and its S/M tests are
present. It does not mean shadow-verified, device-validated, causally
supported, or release-approved.

## Verification recorded for this execution pass

- Focused decision source/outcome, decision contract, and private-shadow tests:
  **14 passed**.
- Focused runtime/evaluation vocabulary and AI-DL contract/proactivity adapter
  tests: **40 passed**.
- Focused proactive arbitration/incrementality adapter tests: **47 passed**.
- Documentation headers, links, status, symbol, and drift checks passed; the
  repository emitted only pre-existing stale-draft warnings.
- Every source commit above passed the repository pre-commit hooks.

These are implementation checks. They do not produce physical-device, human
review, live provider, or causal receipts.

## Operating sequence from here

1. Keep global/policy shadow flags off until the named private family has an
   approved retention and observation protocol.
2. Run and freeze human-anchor adjudication and the provider/structured-policy
   comparison on a pinned source revision. Record failures and exclusions.
3. If shadow is explicitly authorized, allowlist one private trip and observe
   only content-free decisions; verify latency, cost, ledger non-interference,
   and missing-context rates before considering a canary.
4. Treat private proactivity and all group-visible behavior as separate
   experiments. Neither is unlocked by the shadow adapter or offline suite.
5. For a canary, gather exact device/build/deploy receipts and execute the
   predeclared causal analysis. A pleasant transcript or backend test is not a
   substitute.

The canonical implementation details are in the backend architecture document:
[AI Decision and Learning Control Plane](../../travel-agent/docs/architecture/AI%20Decision%20and%20Learning%20Control%20Plane.md).
