# Workspace Docs — Index & Lifecycle

Orientation for the `travel-workspace` documentation. This coordinates two repos:
**Travel Agent** (backend — Python/FastAPI, LLM orchestration) and **Travel App**
(frontend — React Native/Expo). The product is **Vesper**, an AI concierge for group
trips; **Atlas** is its memory/trust subsystem, not a separate product.

> **Start here:** read `systems/` (the contracts) and `journeys/` (what a user does).
> Everything else is planning, ledger, or history.

## Lifecycle model

New documents follow the full admission and metadata policy in
[`governance/README.md`](governance/README.md). The seven document types are
`canon`, `contract`, `runbook`, `decision`, `current_status`, `working`, and
`archive`.

The existing folder model remains the migration map for grandfathered docs:

| State | Meaning | Folders |
|---|---|---|
| **Canon** | Living contracts. Kept current, never archived. | `systems/`, `journeys/` |
| **Active** | In-flight plans & investigations. Graduates out when done. | `working/`, top-level `Plan …` docs |
| **Ledger / History** | Completed audits, shipped plans, finished sprints. Kept for the record, not maintained. | `audits/`, `archive/` |

**Hygiene rule:** when a `working/` investigation's header says `RESOLVED` /
`SUPERSEDED` / `COMPLETE`, move it to `archive/YYYY-MM/`. `working/` should only ever
hold what is genuinely live. Completed multi-file audit *sprints* live in `archive/`;
recent standalone audits live in `audits/`.

**Phase 1 admission rule:** every newly added Markdown file under `docs/` must
use a template from `docs/templates/` and pass `make docs-governance-check`.
Existing files and edits to existing files are grandfathered until the
classification phase.

## Folder map

| Folder | Files | State | Purpose |
|---|---:|---|---|
| `systems/` | 15 | Canon | System Charters — the contract layer (Purpose / Interface / Invariants / Failure modes) for each core system. Has its own `README.md`. |
| `journeys/` | 23 | Canon | Canonical user journeys + the certification `STATUS.md` matrix. `journeys.yaml` is the machine index. Has its own `README.md`. |
| `working/` | 13 | Active | Current investigations & execution plans. The dogfood-readiness cluster + `mvp-scope-and-flag-manifest` (the live "what ships" SSOT) live here. |
| `reliability/` | 18 | Canon/Active | Agent Reliability Playbook, CI Plan, Live Canary Plan. `Golden Paths.md` is a **deprecated redirect** → `journeys/`. |
| `operations/` | 2 | Canon | Deploy Checklist + Deploy & Rollback Runbook (co-located here as of 2026-07-03). |
| `launch/` | 5 | Active | App Store / Apple review / TestFlight / privacy-disclosure copy for the first release. |
| `audits/` | 7 | Ledger | Recent standalone audits (privacy trace, cross-repo seam, trust/account). Mostly `RESOLVED`. |
| `archive/` | 64 | History | Completed audit sprints (`2026-05/…`) and graduated investigations (`2026-06/…`). Reference only. |

**Top-level files** (11) are active planning + reference: the `Plan …` docs (each now
carries a dated **Outcome** banner showing shipped-vs-planned), `Owner Action Items.md`,
`Card Catalog.md`, `Atlas — README.md`, `No-Claude-Design Tightening Sprint.md`,
`Workspace Repo Setup.md`, and the `Handoff …` build record.

## Machine artifacts (not prose — do not hand-edit)

- `openapi.json` — backend contract snapshot; frontend types are generated from it, drift-checked in CI.
- `child-repos.ci-lock.json` — cross-repo CI pin.

## Known follow-ups (deferred, optional)

- **Naming:** top-level docs use `Title Case With Spaces` and mixed separators
  (`Plan -` vs `Plan —`), unlike the `kebab-case-YYYY-MM-DD` convention in subfolders.
  A rename pass would improve scannability but touches cross-references in
  `memory/MEMORY.md` and inter-doc links — do it deliberately, not casually.
- The 7 `audits/` files are all `RESOLVED`; fold into `archive/2026-06/` once you're
  sure nothing links to them as live reference.
