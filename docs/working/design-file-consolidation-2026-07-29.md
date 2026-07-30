---
doc_type: working
status: active
owner: founder / design
created: 2026-07-29
expires: 2026-08-28
why_new: The Vesper Claude Design project feels like a mess, and the assumed cause — orphaned modules and file sprawl — is measurably wrong. This is the first note to build the full reference graph across all 66 pages and 215 modules, establishing that the module layer is 214/215 reachable (one 3.6 KB orphan), that three well-built audit scripts already exist inside the design project, that all three are currently RED and unrun, and that the single uncovered axis is module authority. It reframes consolidation from "restructure the files" to "turn the existing checkers green and wire them", and adjudicates the page-role decisions that blocks on.
promotes_to: a short `design/canon-governance.md` once Track F picks where the audits run; otherwise expires into the Canon Index itself, which is the real deliverable
supersedes: []
source_of_truth_for:
  - design-file-consolidation-evidence-2026-07-29
  - design-page-role-adjudication-2026-07-29
---
# The Vesper design file — consolidation plan

## 0 · Picking this up cold

Claude Design project **Vesper**, `project_id: 551f400f-3da1-42ab-be7f-35f2d28e7c75`.
66 top-level `.html` pages, 215 root `.jsx` modules, plus `archive/` and `scraps/`.

**Read these five files before touching anything** — they are the governance
instruments, and this plan is about them, not about the design work itself:

| File | Role | Coverage today |
|---|---|---|
| `README.md` | states the promises | — |
| `CLAUDE.md` | conventions + settled Vesper Home canon | current (updated 07-29) |
| `Vesper Design Canon Index.html` | the human map — "open this first" | **51 / 66 pages** |
| `Vesper Canon Consolidation & Ownership.html` | the authority ledger | **99 / 215 modules** |
| `vesper-design-manifest.json` | the machine-readable registry | **6 / 66 pages · 38 screens** |

**Start at Track A.** It is the only track that needs founder judgment; every
other track is mechanical once A is decided.

## 1 · What was measured, and how

Method: fetched all 66 pages and all 215 modules, extracted every
`<script src="*.jsx">`, then computed reachability including transitive loads
(at least one module self-loads `root-header.jsx` over a synchronous XHR, so a
`<script>`-tag-only graph would have been wrong).

Then ran the three audit scripts that already live in the project. They are
standalone Node, built-in modules only, and accept `--root`, so they run against
a local mirror without any setup.

```
root pages                      66
root jsx modules               215
referenced by a page <script>  213
reachable incl. transitive     214
ORPHANS                          1     consequence-banner.jsx (3.6 KB)
```

**The module layer is clean.** This is the finding that changes the plan: there
is no dead-module problem to solve. 5.18 MB of modules, 3.6 KB unreachable.

### The three checkers, run 2026-07-29

| Script | Result | Detail |
|---|---|---|
| `audit-consistency.js` | **FAIL** — 4 hard, 2 warn | 17 checks defined |
| `audit-interchange.js` | **FAIL** — 9 hard | all 9 are Trips stack-model screens |
| `audit-typography.js --check` | **STALE** | both generated artifacts out of date |

`audit-consistency.js`'s four hard failures:

1. **Unindexed top-level HTML — 15 pages.** Independently reproduces the manual
   diff exactly. (Two of the 15 are mine, added this session.)
2. **Ungoverned indexed page — 1.** `Vesper Trips Home - Stack Model (Sans)` is
   in the index but carries no governance classification. A distinct defect class
   from #1, and one a manual read would have missed.
3. **Retired fixture names in current prose — 1.** `places-map.jsx:423` uses
   "Jonas" in a demo prop. Mine. One-word fix.
4. **Decorative token on meaningful text — 10 unresolved.** Spread across
   `trips-home-row-studies.jsx`, `vesper-chat-typefork.jsx`, `vesper-history.jsx`.

`audit-interchange.js`'s nine: DOM screen roots present in
`trips-home-stack*.jsx` that no manifest entry declares. The checker discovers
modules from disk (`readdirSync`), so it sees screens the manifest has never
heard of — which is exactly what it is for.

## 2 · The diagnosis

**The design file is not disorganized. It is unaudited.**

Everything needed to keep it coherent already exists and is well built: five
governance instruments, seventeen consistency checks, a screen-level interchange
audit with a hard-failure contract, a deterministic typography inventory with a
`--check` mode. The `README` even states the model correctly — pages are
"governed and trustworthy for their declared role", not all canon, with history
retained as evidence.

What is missing is that **nobody runs the checkers**, so every working session
adds pages and modules at root and the instruments fall behind. The felt "mess"
is not too many files; it is that the map no longer answers *which page do I
open* for a given surface:

| Surface | Pages today |
|---|---|
| Places | 7 |
| Trips home | 8 |
| Vesper Home | 3 |
| Chat | 3 |
| Type / material | 3 |

That is the same conclusion reached for Places earlier this week — the problem
was findability, not design — arrived at independently and now at file scale.

## 3 · The one uncovered axis

Worth stating precisely, because the first hypothesis was wrong. The Ownership
ledger *is* checked — `audit-consistency.js` check #3, "indexed pages absent
from governance ledger [HARD]" — but it checks **pages**, not **modules**.

So of the two registry axes:

- **Pages → index → ledger** is covered in both directions, and is at 51/66 and
  failing loudly.
- **Modules → authority status** is covered by nothing, and is at 99/215.

The axis with no checker is the axis that drifted twice as far. That is the
causal argument for Track F, and it is measured rather than asserted.

## 4 · Tracks

### Track A — Adjudicate page roles *(founder judgment; blocks B)*

The only real decisions here. For each family: name one canon, classify the
rest. Roles come from the `README`'s existing vocabulary — **canon**,
**companion**, **instrument**, **folded source**, **history**.

Recommendations below; §6 carries the two that are genuinely open.

**Places (7)**
| Page | Role |
|---|---|
| `PLACES - CORE.html` | **CANON** — already ruled by the founder |
| `PLACES - COMPONENT MAP.html` | instrument — the 49-component catalogue |
| `Vesper Places.html` | **CANON** for venue detail — a different surface, keep |
| `PLACES - SURFACE COMPONENTS PASS 5.html` | folded source |
| `PLACES - FOUNDATION SHELL & SCOPE PASS 4.html` | folded source |
| `PLACES - COMPONENT POLISH PASS 3.html` | folded source |
| `PLACES - CONTEXTUAL PLACE WORKSPACE.html` | folded source |

**Trips home (8)**
| Page | Role |
|---|---|
| `Vesper Trips Home - Stack Model (Sans).html` | **CANON** — clears failure #2 |
| `TRIPS - DESIGN vs CODE.html` | instrument — the fidelity record |
| `Vesper Trips Imminent Hero States.html` | companion |
| `Vesper Trips Hero Asset Catalog.html` | companion |
| `Vesper Trips Home - Stack Model.html` | history — serif fork, rejected by audit |
| `Vesper Trips Home - Type Correction.html` | folded source — the serif audit |
| `Vesper Trips Home - Row Studies.html` | folded source |
| `Vesper Trips Home.html` | history — superseded by the stack model |

**Vesper Home (3)** — `Home - Workbench` = **CANON** (`CLAUDE.md` already states
this outright), `Vesper Home` = history, `Home - History` = instrument.

**Chat (3)** — `Vesper Chat` = canon, `Chat Working States` = companion,
`Chat - Type Fork` = folded source.

**Type (3)** — `Productive Type & Material` = companion, `Depth Ladder` =
companion, `TYPE - SERIF CANDIDATES` = folded source (decision made: EB Garamond).

### Track B — Register, don't delete *(mechanical after A)*

Write the 15 missing pages into the Canon Index with their Track A role, and add
the one missing governance row. Turns `audit-consistency.js` failures #1 and #2
green.

**Do not move folded sources to `archive/`.** Three reasons:

1. The `README` already sanctions history at root — "historical top-level pages
   remain as evidence". Declaring a role satisfies both the checker and the
   founder's actual complaint.
2. Archiving a page changes module reachability. Those four Places passes are
   backed by ~34 modules (`places-polish-*`, `places-workspace-*`,
   `places-surface-*`, `places-foundation-*`). Archive the pages and those
   modules go unreachable, where a naïve reading of Track E's rule would then
   classify them as deletable. That would destroy real design work.
3. It is reversible later and irreversible-ish now. `archive/` stays reserved for
   pages whose material is *fully* superseded **and** whose modules are already
   unreachable — which today is none of them.

### Track C — Extend the machine manifest

Add the 9 undeclared Trips stack screens to `vesper-design-manifest.json`. Turns
`audit-interchange.js` green.

Then decide its scope — see §6. At 6/66 pages the manifest is not yet a registry
of the design file; it is a registry of six pages.

### Track D — Clear the residual failures

- `places-map.jsx:423` — replace the retired fixture name.
- The 10 decorative-token flags — each is a real call (`muteSoft` on text that
  carries meaning), not a false positive to suppress.
- `node audit-typography.js --write` to regenerate both artifacts.

### Track E — Close the module-authority axis

Backfill authority status for the 116 untracked modules, then add check #18 to
`audit-consistency.js`: *every root `.jsx` has a tracked authority status.*

**Do not hand-classify 116 modules.** Derive the default from the reachability
graph, which already exists and is cheap to recompute:

- reachable from a **canon or companion** page → `active`
- reachable **only** from a history or folded-source page → `folded`
- **unreachable** → candidate for deletion (today: exactly one file)

Then hand-classify only the exceptions. This is the same "reuse, don't rebuild"
move that Places made when the ranker turned out to already exist.

### Track F — Wire it so it stays green

The mechanism question, and the one that decides whether this plan is worth
anything in a month. The checkers are standalone Node with `--root` support, so
running them is trivial — the open question is *where*. See §6; the `DesignSync`
tooling is the obvious candidate and should be checked before anything new is
built.

## 5 · Sequencing

```
A (roles)  ──► B (register)  ──┐
C (manifest) ─────────────────┼──►  all three checkers GREEN  ──► F (wire)
D (residual) ─────────────────┘
                    E (module axis) ──► check #18 ──► F
```

A blocks B. C, D, E are independent of A and of each other. F should come last
but be *decided* early — a green checker nobody runs is the exact state this
plan exists to fix.

## 6 · Open decisions

**D1 · Manifest scope.** Should `vesper-design-manifest.json` cover all 66 pages,
or stay a screen-level registry for surfaces heading into code?
*Recommendation:* **stay narrow, and say so in the file.** Its value is
design↔code interchange — 38 screens with route keys, owner components and
capture receipts. Expanding it to governance pages and specimen boards would
dilute that and duplicate the Canon Index. Add a one-line scope statement so
6/66 reads as a boundary rather than as 9% coverage. The checker already
enforces the distinction (it hard-fails on "governance content classified as a
product screen"), which is evidence the narrow reading is the designed one.

**D2 · Where the audits run.** No recommendation yet — this needs a look at
`DesignSync` first, which may already move design files into the repo where
`scripts/` and CI could run the audits unchanged. If it does, this is
configuration. If it does not, the honest fallback is a documented one-command
check plus session discipline, which is weaker and should be named as weaker
rather than dressed up.

## 7 · Out of scope

- Any design change. This plan touches governance metadata, one fixture name,
  ten colour tokens, and generated artifacts. No layout, no copy, no components.
- The `archive/` and `scraps/` trees. `archive/` has its own manifest and is
  already coherent; `scraps/` is scratch by definition.
- The gutter reconciliation (22 vs 16) from `TRIPS - DESIGN vs CODE.html`. It is
  a design decision, tracked there, and independent of this plan.
- Deleting `consequence-banner.jsx`. It is 3.6 KB and unreachable, but "delete
  the one orphan" is Track E's output, not a separate errand.
