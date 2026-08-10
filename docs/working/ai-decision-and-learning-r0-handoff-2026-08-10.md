---
doc_type: working
status: active
owner: AI systems / convergence integration
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Records the exact AI-R0 handoff and the current A-D integration gate so the separate AI-DL workstream can resume without guessing at moving branch state.
source_of_truth_for:
  - ai-decision-and-learning-r0-handoff-2026-08
related:
  - ai-decision-and-learning-r0-fixture-manifest-2026-08-10.md
  - ai-decision-and-learning-r0-baseline-inventory-2026-08-10.md
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
---

# AI-R0 handoff and A–D integration gate

## 1. Handoff verdict

AI-R0 has produced and committed:

- the research agenda and separate engineering plan;
- the fixture/corpus manifest;
- the baseline inventory and reproducible offline results;
- an isolated backend contract package;
- a deterministic bounded-action baseline;
- focused tests and lint/format receipts.

AI-R1 runtime integration is **not ready to start**. The four convergence lanes
remain separate branches with independent commits, and at least one lane has
dirty workspace state. The AI-DL package therefore remains isolated and must not
be imported by production agents yet.

## 2. AI-DL commits

### Workspace repository

| Commit | Scope |
| --- | --- |
| `b435ceb` | research agenda + separate engineering plan |
| `1db4e14` | AI-R0 fixture/corpus manifest |
| `b926491` | existing evaluation baseline inventory |

### Isolated backend repository

Worktree:
`/Users/feihuyan/travel-agent--ai-decision-learning-r0`

Branch: `codex/ai-decision-learning-r0`

| Commit | Scope |
| --- | --- |
| `dc14417db` | frozen contracts and deterministic validators |
| `c790157d9` | machine-readable seven-corpus AI-R0 manifest |
| `516d33e0f` | conservative deterministic Decision Set baseline |

These commits are intentionally based on the backend revision available when
the isolated worktree was created. The integration owner must rebase/cherry-pick
them onto the recorded A–D integration SHA after that SHA exists; do not merge
the AI-DL branch directly into a moving convergence lane.

## 3. A–D observed branch state

Observed 2026-08-10 from the four active workspace worktrees:

| Lane | Workspace HEAD | Backend HEAD | Mobile HEAD | Gate observation |
| --- | --- | --- | --- | --- |
| Evidence integrity | `bc97fa1` | `84930858f` | `5b32842b` | workspace clean; separate commits ahead of origin |
| Home truth | `fec425a` | `603957607` | `b720ba18` | workspace has dirty inventory/status and untracked brand doc |
| Context trust | `6fb04af` | `96107859` | `f7549bd7` | backend commits ahead; workspace/mobile remain at baseline heads |
| Map/projection | `6fb04af` | `babe47052` | `fa1a275b` | backend/mobile commits ahead; workspace remains at baseline |

These are lane observations, not claims that the underlying work is complete.
They are included so a later integration owner can compare exact ancestry and
re-run the evidence report.

## 4. Required integration record

Before AI-R1 runtime work begins, record one integration candidate containing:

```yaml
integration_candidate:
  workspace_sha: null
  backend_sha: null
  mobile_sha: null
  evidence_lane_commit: null
  home_lane_commit: null
  context_lane_commit: null
  map_lane_commit: null
  contract_check: not_run
  evidence_report: not_run
  dirty_worktrees: []
  deferred_lanes: []
  integration_owner: null
```

The candidate is invalid until:

- all three base SHAs are recorded;
- A–D landed or explicitly deferred commits are named;
- generated backend/mobile contract parity passes;
- evidence status and device-proof semantics are known;
- no dirty file is silently included;
- the AI-DL branch is rebased or cherry-picked onto these exact heads;
- the AI-DL focused tests and the relevant existing offline suite pass.

## 5. Current AI-R0 validation receipt

On the isolated AI-DL backend branch:

```text
PYTHONPATH=. <backend-venv>/bin/python -m pytest \
  tests/eval/test_ai_decision_learning_contracts.py -q
12 passed

ruff check eval/ai_decision_learning tests/eval/test_ai_decision_learning_contracts.py
All checks passed

ruff format --check eval/ai_decision_learning \
  tests/eval/test_ai_decision_learning_contracts.py
6 files already formatted
```

The package has no runtime-agent, database, notification, group-composer, or
mobile imports. This is M/A-adjacent offline contract evidence only; it is not
B, D, V, C, or a product release claim.

## 6. Next owner action

The next engineering session should:

1. keep the AI-DL worktree isolated;
2. wait for the A–D integration record;
3. rebase/cherry-pick the three backend AI-DL commits onto that record;
4. run the existing offline suite and contract checks;
5. only then begin AI-001 adapter work against the landed scope/evidence
   contracts.

If a convergence lane is deferred, mark the dependent AI-DL phase unavailable.
Do not create a local substitute for relationship/experience scope, Home truth,
map freshness, or evidence certification.
