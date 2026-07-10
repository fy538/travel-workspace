---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-05-01
last_verified: 2026-07-09
why_new: Promote the existing workspace index into the canonical documentation entry point.
supersedes: []
source_of_truth_for: [workspace-docs-navigation]
---

# Workspace Documentation

This workspace coordinates **Travel Agent** (backend and orchestration) and
**Travel App** (Expo client) for Vesper. Start with the eight documents below;
everything else is a contract, supporting reference, active working note, or history.

## Canonical spine

| Question | Entry point | Owns |
|---|---|---|
| Why this product? | [Product Thesis](../travel-agent/docs/product/Product%20Thesis.md) | `travel-agent/docs/product/Product Thesis.md` — core promise and strategy |
| What principles guide it? | [What We Believe](../travel-agent/docs/product/What%20We%20Believe.md) | `travel-agent/docs/product/What We Believe.md` — durable product beliefs |
| What ships first? | [V1 Scope](working/mvp-scope-and-flag-manifest-2026-06-30.md) | `docs/working/mvp-scope-and-flag-manifest-2026-06-30.md` — bounded release scope |
| What exists now? | [Current State](status/current-state.md) | `docs/status/current-state.md` — derived implementation signals |
| Can users complete the journeys? | [Journey Status](journeys/STATUS.md) | `docs/journeys/STATUS.md` — certification evidence |
| What must each system guarantee? | [Systems Index](systems/README.md) | `docs/systems/README.md` — cross-repo contracts |
| What needs a human or external account? | [Owner Actions](Owner%20Action%20Items.md) | `docs/Owner Action Items.md` — founder/external blockers |
| Why was a durable choice made? | [Decision Index](decisions/README.md) | `docs/decisions/README.md` — decisions and supersession |

The machine-readable catalog is `docs/governance/spine.yaml`. A document outside
this spine may be useful, but it must not silently become a competing source of truth.

## Supporting layers

- `systems/`, `journeys/`, and `operations/` hold living contracts and runbooks.
- `working/` holds expiring investigations and execution plans.
- `launch/`, `reliability/`, and `flags/` support specific operational concerns.
- `audits/` and `archive/` are evidence and history, not current truth.
- `openapi.json` and `child-repos.ci-lock.json` are machine artifacts; do not hand-edit them.

Lifecycle and admission rules live in [Documentation Governance](governance/README.md).
Run `make docs-check` before pushing; use `make docs-status-sync` after changing a
registry represented in Current State.
