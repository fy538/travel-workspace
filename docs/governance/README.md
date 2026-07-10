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

## Enforcement

Run:

```bash
make docs-governance-check
```

The local pre-commit hook checks newly staged Markdown files. Workspace CI
checks files added since the push or pull-request base. Existing documents and
edits to existing documents are intentionally grandfathered during Phase 1.

