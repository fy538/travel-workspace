---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-05-01
last_verified: 2026-09-07
why_new: Promote the existing workspace index into the canonical documentation entry point.
supersedes: []
source_of_truth_for: [workspace-docs-navigation]
---

# Workspace Documentation

## Start here — product, execution and evidence

Use the authority appropriate to the question. Product direction, current work
and a bounded milestone are not interchangeable.

| Question | Answer | When you ask it |
|---|---|---|
| **What product are we building?** | [Product Thesis](../travel-agent/docs/product/Product%20Thesis.md) → [Product Model](../travel-agent/docs/product/Product%20Model.md) → [accepted consumer strategy](decisions/2026-09-06-reconcile-consumer-strategy.md) | understanding direction and boundaries |
| **What matters next across the whole product?** | [Vesper program roadmap](working/vesper-program-roadmap.md) — current priorities, accountable tasks, dependencies and system checkpoint | coordinating independent lanes without reconstructing task history |
| **How do we implement and integrate it?** | [Complete-system integration roadmap](working/complete-system-integration-roadmap-2026-09-05.md) and the program's linked lane plans | shared technical sequencing, scoped implementation and landing under existing contracts |
| **What must the M1 demo establish?** | [M1 — Plan Repair](release/m1-plan-repair.md) | executing or certifying that bounded operational-alpha milestone |
| **What evidence supports completion?** | Current owner/package receipts for local progress; [`evidence-attestations.json`](journeys/evidence-attestations.json) for promoted journey evidence | distinguishing implementation progress from certification |
| **What must I not break?** | [V1 scope](release/v1-scope.md) for dark surfaces · [Journey Status](journeys/STATUS.md) for the regression floor | shipping work |

M1 owns its four-act demo, required proof, flags and rollback. It does not define
the whole product, architecture order or complete evidence portfolio. Work
outside M1 may still be necessary under the integration roadmap and accepted
product strategy; it simply does not count toward that milestone by implication.

Three things follow from that table and are worth stating once:

- **A green test is not done.** A test name proves coverage is *defined*. Only a
  promoted receipt at the layer named in
  [the evidence model](journeys/EVIDENCE_MODEL.md) certifies the corresponding
  journey claim. Local tests can establish their stated implementation boundary,
  not consumer preference or release readiness.
- **Intent, evidence, and regression stay separate.** The applicable roadmap or
  milestone names required outcomes; its receipts and the attestation index
  record evidence at different scopes; the J replay floor checks regressions.
  A research specimen or supported-offer candidate is not an execution receipt.
- **Lighting a flag outside its declared `gate:` is a scope change**, not a
  config change.

The program roadmap owns cross-lane coordination; Integration owns shared
technical execution and landing; lane plans own their current implementation
queues and receipts. These working plans do not replace product, permissions,
generated current-state signals or release authorities. Read the relevant owner
contract before changing it. Older Integration assignment tables are historical;
use the program's dated baseline and verify Git before starting work.

## Current strategy review

- [Accepted September 7 refinement](decisions/2026-09-06-reconcile-consumer-strategy.md#5-september-7-refinement-complete-benefits-selective-context-and-voluntary-choice):
  complete benefits, selective context and voluntary choice; no new retention
  agreement, price or launch readiness follows.
- [Strategy reading map and chronological audit](working/vesper-audience-offer-and-market-strategy-research-2026-09-06.md#current-reading-map):
  research provenance, revised recommendations and evidence limits.
- [V1 supported-offer candidate](working/vesper-v1-supported-offer-2026-09-07.md):
  proposed inclusion boundaries and independent entrances, not shipping scope.
- [Pending decision packets](decisions/README.md#pending-decision-packets--not-adopted):
  unresolved agreements stay separate from accepted direction.

These links make the current reasoning discoverable without promoting working
research into canon or replacing generated release intent.

## Company orientation

This workspace coordinates **Travel Agent** (backend and orchestration) and
**Travel App** (Expo client) for Vesper. The documents below are an
**authority registry**, not a required cover-to-cover reading list. Everything
else is a contract, supporting reference, active working note, or history.

For a company orientation, read [Product Thesis](../travel-agent/docs/product/Product%20Thesis.md)
→ [Product Model](../travel-agent/docs/product/Product%20Model.md) →
[Current State](status/current-state.md). Product and design readers can then add
Product Vision and the app Design Language; engineers can add Architecture
Principles, Unified Context Graph, and the relevant system charter.

## Canonical spine

| Question | Entry point | Owns |
|---|---|---|
| What must M1 establish? | [M1 — Plan Repair](release/m1-plan-repair.md) | `docs/release/m1-plan-repair.md` — the bounded operational-alpha milestone, its four demo acts, and exit criteria |
| Why this product? | [Product Thesis](../travel-agent/docs/product/Product%20Thesis.md) | `travel-agent/docs/product/Product Thesis.md` — core promise and strategy |
| How does the product model fit together? | [Product Model](../travel-agent/docs/product/Product%20Model.md) | `travel-agent/docs/product/Product Model.md` — governed owners, four recurring moves, four root orientations, real-world consequence, and continuity |
| What principles guide it? | [What We Believe](../travel-agent/docs/product/What%20We%20Believe.md) | `travel-agent/docs/product/What We Believe.md` — durable product beliefs |
| What ships first? | [V1 Scope](release/v1-scope.md) | `docs/release/v1-scope.md` — generated bounded release intent |
| What exists now? | [Current State](status/current-state.md) | `docs/status/current-state.md` — derived implementation signals |
| Can users complete the journeys? | [Journey Status](journeys/STATUS.md) | `docs/journeys/STATUS.md` — certification evidence |
| What must each system guarantee? | [Systems Index](systems/README.md) | `docs/systems/README.md` — cross-repo contracts |
| What needs a human or external account? | [Owner Actions](Owner%20Action%20Items.md) | `docs/Owner Action Items.md` — founder/external blockers |
| Why was a durable choice made? | [Decision Index](decisions/README.md) | `docs/decisions/README.md` — decisions and supersession |

The machine-readable catalog is `docs/governance/spine.yaml`. A document outside
this spine may be useful, but it must not silently become a competing source of truth.

## Supporting layers

- [Content-to-native quality consolidation plan](working/content-to-native-quality-consolidation-plan-2026-09-15.md):
  proposed shared-pattern/content implementation packages with current-app polish
  as a required outcome; scheduling stays with the program roadmap.
- `systems/`, `journeys/`, and `operations/` hold living contracts and runbooks.
- `working/` holds expiring investigations and execution plans.
- `launch/`, `reliability/`, and `flags/` support specific operational concerns.
- `audits/` and `archive/` are evidence and history, not current truth.
- `openapi.json` and `child-repos.ci-lock.json` are machine artifacts; do not hand-edit them.

Lifecycle and admission rules live in [Documentation Governance](governance/README.md).
Run `make docs-check` before pushing; use `make docs-status-sync` after changing a
registry represented in Current State.
