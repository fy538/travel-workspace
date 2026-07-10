---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-07-09
last_verified: 2026-07-09
why_new: Defines one cross-repo lifecycle and admission policy that no existing document owns.
source_of_truth_for:
  - documentation-lifecycle
  - new-document-admission
---

# Documentation Governance

This policy controls the growth and lifecycle of documentation in the Vesper
workspace. Its purpose is not to reduce documentation indiscriminately. It is
to prevent multiple documents from competing to describe the same truth.

Phase 1 establishes the admission rule for new workspace documents. Existing
documents are grandfathered until they are deliberately classified in a later
phase.

## The seven document types

Every governed document has exactly one type.

| Type | Answers | Expected lifetime | Required maintenance |
|---|---|---:|---|
| `canon` | Why do we believe this? | Years | Verify quarterly or after a product-direction decision. |
| `contract` | What must this system or surface do? | Months–years | Update with the behavior it governs. |
| `runbook` | How do we operate or release this? | Months | Re-run and verify on a dated cadence. |
| `decision` | Why was a consequential choice made? | Permanent | Immutable; supersede with another decision. |
| `current_status` | What is true right now? | Days–weeks | Prefer generated evidence; verify frequently. |
| `working` | What are we investigating or executing? | At most 30 days by default | Close, promote, or archive by `expires`. |
| `archive` | What historical context are we preserving? | Permanent, non-authoritative | Never present it as current truth. |

## Admission rule for a new document

Before adding a Markdown file, answer:

1. What action or decision will this document enable?
2. Which one document type is it?
3. Who owns its correctness?
4. Why can an existing document not absorb this material?
5. When does it expire or require verification?
6. What existing document does it supersede, if any?

If those questions do not have concrete answers, extend an existing document,
record the work in code or a task, or do not create the file.

New documents under `docs/` must begin with YAML frontmatter containing:

```yaml
---
doc_type: contract
status: active
owner: team-or-person
created: 2026-07-09
last_verified: 2026-07-09
why_new: The existing system charter cannot own this cross-system contract.
supersedes: []
source_of_truth_for:
  - example-contract
---
```

The validator enforces type-specific fields:

- `canon`, `contract`, `runbook`, and `current_status` require
  `last_verified`.
- `working` requires an `expires` date no more than 30 days after `created`.
- `decision` requires a `decided` date.
- `archive` requires an `archived` date.
- Every type requires `doc_type`, `status`, `owner`, `created`, and a concrete
  `why_new` explanation.

Use the files under `docs/templates/` as starting points. Template files are
excluded from metadata enforcement because their values are placeholders.

## Authority rules

- Canon explains **why**. It should not contain a manually maintained current
  implementation scorecard.
- Contracts explain **what must remain true**. Code and generated contracts
  establish whether it is true now.
- Current-status documents summarize executable sources such as OpenAPI,
  journey registries, feature flags, CI, deployment probes, and Git. They must
  not independently re-declare those facts in several places.
- Working notes are an inbox, not permanent navigation. At expiry they are
  promoted, archived, or deleted.
- Decisions are historical records. Do not rewrite an accepted decision to
  make it appear that the team always held the newer position.
- Archived documents are reference-only and must not be listed as a current
  source of truth.

## Repository ownership

- The workspace owns product canon, cross-repo journeys and systems, release
  state, and cross-repo decisions.
- `travel-agent` owns backend architecture, data/agent contracts, evals, and
  backend operations.
- `travel-app` owns surface contracts, navigation/interaction conventions,
  mobile operations, and visual QA.

Phase 1 enforces new files in the workspace `docs/` tree. The policy is already
cross-repo; equivalent child-repo enforcement should be added after this gate
has proven non-disruptive.

## Phase 2 inventory

`inventory.yaml` assigns every workspace Markdown file exactly one disposition:

- `keep_authoritative`
- `keep_reference`
- `merge`
- `archive`
- `delete_candidate`
- `investigate`

Folder rules classify stable trees such as `archive/`, `systems/`, and
`journeys/`. Top-level and `working/` documents are classified individually so
ambiguous material cannot hide behind a broad default. A `merge` entry must name
its consolidation target.

Phase 2 changes no existing document content or location. It only builds the
reviewed queue for later consolidation and cleanup.

## Phase 3 canonical spine

`spine.yaml` names exactly eight living entry points: thesis, beliefs, V1 scope,
current state, journey status, systems, owner actions, and decisions. The workspace
index must expose all eight, their paths must exist outside the archive, and each
workspace-owned entry must be classified `keep_authoritative` in the inventory.

`docs/status/current-state.md` is intentionally narrow. Its generated block reports
facts from executable registries instead of copying narrative readiness claims into
another document. Refresh it with `make docs-status-sync`; CI rejects drift.

## Phase 4 consolidation

Every Phase 2 `merge` candidate has been resolved. Durable rules now live in the
named authoritative target, while the complete source snapshot lives under
`archive/2026-07/consolidated/` with archive metadata. Consolidation does not delete
evidence and does not promote unresolved investigation claims into contracts.

The inventory must remain at zero `merge` entries during normal operation. A new
`merge` classification is a bounded migration task: name the target, extract only
durable content, repair live links, archive the source, then remove the override.

## Phase 5 archive cleanup

Reviewed `archive` items must physically leave living directories. Phase 5 moved
the remaining completed plans, audits, receipts, and working notes into
`archive/2026-07/retired-live/`, preserving their complete text and adding archive
metadata. The deprecated Golden Paths redirect was removed only after its remaining
live references were repointed to the canonical journey index and status matrix.

An archive classification is therefore a short-lived migration state, not permission
to leave historical material mixed with current truth. `delete_candidate` likewise
requires both an inbound-link check and confirmation that canonical owners preserve
the unique content. The inventory gate fails if an `archive` disposition appears
anywhere outside `docs/archive/`.

## Phase 6 adjudication

`investigate` is also a temporary state. Phase 6 verified every remaining item
against current code and executable registries, ratified Graph Legibility, extracted
three durable decisions, moved current risks into system charters, and archived the
complete investigation ledgers. The steady-state inventory now has zero ambiguous
dispositions: new investigations must name the evidence or decision that will close
them and follow the working-document expiry policy.

## Phase 7 steady-state ratchets

Normal CI requires the inventory's transitional queues (`merge`, `investigate`, and
`delete_candidate`) to remain empty and rejects broken relative links in living
workspace docs. Archive links are intentionally excluded because historical evidence
may name paths that existed at the time.

The same new-document metadata policy now covers `travel-agent/docs/` and
`travel-app/docs/`. `child-baselines.yaml` records immutable grandfather commits;
files present at those commits keep their native child-repo conventions, while every
later Markdown path must satisfy the workspace lifecycle schema. Do not advance a
baseline to bypass admission—the baseline is history, not a moving allowlist.

## Enforcement

Run:

```bash
make docs-governance-check
make docs-inventory-check
make docs-inventory-report
make docs-spine-check
make docs-status-check
make docs-child-governance-check
make docs-links-check
# or all gates together:
make docs-check
```

The local pre-commit hook checks newly staged Markdown files. Workspace CI
checks files added since the push or pull-request base. Existing documents and
edits to existing documents are intentionally grandfathered during Phase 1.
