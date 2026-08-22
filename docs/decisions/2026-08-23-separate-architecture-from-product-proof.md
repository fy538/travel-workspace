---
doc_type: decision
status: accepted
owner: founder / product / architecture
created: 2026-08-23
decided: 2026-08-23
last_verified: 2026-08-23
why_new: Separates systematic product architecture, implementation integration, human product evidence, and release claims so no single proof loop dictates the product ontology or blocks coherent architectural work.
supersedes:
  - 2026-08-09-experience-context-and-relationship-kernel.md#execution-order-item-7
source_of_truth_for:
  - architecture-proof-separation
  - architecture-behavior-portfolio
---

# Separate systematic architecture from product proof

## Context

Several August documents collapsed two valid disciplines into one rule:

1. product claims should be tested through concrete human behavior; and
2. implementation should land through inspectable, end-to-end slices.

That collapse produced the misleading instruction to prove one behavior loop
before designing, generalizing, or migrating the architecture. A single loop is
necessarily selective. Letting it determine the ontology creates tunnel vision:
the first convenient scenario can overfit ownership, lifecycle, privacy,
multiplayer, and persistence decisions that must remain coherent across the
whole product.

## Decision

Architecture and product proof are separate, parallel authorities.

### Systematic architecture

The architecture is derived from the complete product model, cross-cutting
invariants, and a representative behavior portfolio. It must reason across:

- answer-only and expiring interactions;
- source artifacts, custody, interpretation, and correction;
- personal, relational, group, and public scopes;
- Place identity, knowledge, familiarity, and situated capability;
- solo, pair, recurring-group, local, and travel experiences;
- Plans, Occasions, invitations, decisions, Commitments, and live adaptation;
- occurrence, plural Outcomes, memory, later application, and forgetting; and
- proactivity, withdrawal, expiry, unknown, and deliberate silence.

The architecture may introduce a generalized contract or replace a legacy
authority when this portfolio and its invariants justify the change. It does not
need to wait for one user experiment to discover an already-visible structural
requirement. Conversely, a resonant noun or one successful scenario does not by
itself justify a new aggregate, table, service, or surface.

### Implementation slices

Vertical slices remain useful for integration, migration, rollback, and
verification. They prove that several architectural owners compose correctly;
they do not define the architecture by themselves. Multiple slices may proceed
in parallel when their ownership boundaries are already decided and their
changes do not collide.

### Human product evidence

Behavioral proofs test whether people receive the intended value: immediate
utility, increased capability, multiplayer value, practical relief, trust,
continuity, and willingness to return or invite others. They can change product
priority, interaction design, language, and even challenge architectural
assumptions. They are not prerequisites for systematic architectural reasoning
and do not convert a prototype's local data shape into canonical ontology.

### Release and claims

Architecture completeness, local implementation, device proof, human value, and
production release remain separate evidence layers. A broad architecture does
not authorize broad product exposure. A successful human test does not prove
production safety. A passing fixture does not prove user value.

## Four independent gates

| Gate | Question | Evidence |
|---|---|---|
| Architecture coherence | Does the model preserve ownership, truth, authority, plurality, lifecycle, correction, and silence across the portfolio? | contracts, scenario matrix, adversarial review |
| Implementation conformance | Do real writers, readers, projections, migrations, and receipts obey that architecture? | tests, parity, replay, migration, integration receipts |
| Human product value | Do people become more capable, less burdened, better coordinated, or better served later? | observed use, comparison studies, follow-up outcomes |
| Release readiness | Is the behavior safe, operable, understandable, and reversible in its target environment? | device, provider, deployment, monitoring, rollback evidence |

Failure at one gate is diagnosed at that gate. It must not be disguised as
success at another.

## Consequences

- Replace “prove one loop before broadening the graph” with “design from the
  whole portfolio; integrate through slices; validate value through multiple
  behavioral proofs.”
- The Sorrento menu and Rome couple studies remain valuable evidence programs,
  but neither is the architectural source of truth or a prerequisite for the
  experience-graph ontology.
- Architecture work and human research should run in parallel and exchange
  findings through explicit assumption and contradiction registers.
- Release scope may remain narrow even when the architecture is intentionally
  broader.
- Deletion and irreversible cutover still require portfolio conformance,
  migration safety, and target-bound evidence; systematic design is not a
  shortcut around operational proof.

## Non-goals

- Building every capability represented by the ontology now.
- Treating document completeness or architecture breadth as traction.
- Creating a database object for every product noun.
- Allowing speculative abstractions to bypass ownership, consumer, or behavior
  analysis.
- Weakening privacy, authority, correction, idempotency, migration, or release
  gates.
