---
doc_type: working
status: active
owner: founder / engineering
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Records the reviewed usefulness, verification boundary, inherited debt, rollback points, and local landing protocol for the four-root workspace, backend, and app convergence.
depends_on:
  - ../systems/four-root-loop-object-surface.md
  - home-and-places-root-implementation-status-2026-09-01.md
  - life-v1-execution-status-2026-09-01.md
  - ../status/current-state.md
---

# Four-root repository convergence baseline

## Outcome

The workspace, backend, and mobile convergence lines are coherent and useful
enough to become the new local baseline. The landing is intentionally a dark
architecture and internal-surface baseline, not a production rollout or a
claim that the four-root product is complete.

The accepted result keeps one governed product model across Home, Chat, Places,
and Life while preserving existing domain owners. It adds typed projections,
Composition anatomy, exact return context, owner-bound Artifact media, a dark
Life Time root, bounded Life refinding, and a content-free Concierge semantic
shadow. It does not introduce a universal writer, replace the mature Places
feed, promote new navigation publicly, or turn generated prose into evidence.

## Reviewed landing set

| Repository | Pre-convergence `main` | Reviewed candidate | Usefulness ruling |
| --- | --- | --- | --- |
| Workspace | `a8580f8` | `codex/dynamic-artifact-contract` | Keep: canonical decisions, contracts, flags, generated API snapshots, preserved research lineage, and cross-repo status now agree. |
| Backend | `193cd419` | `b83d2393c` | Keep: read-only root projections, semantic Composition, source media, Life projection/refinding, custody hardening, dark semantic facade, and canonical four-root orientations share existing owners. |
| App | `e006fae` | `9eb3d87d3` | Keep: internal Home/Places/Life consumers, canonical return handoff, native composition/media rendering, refinding destinations, and root-specific primitives are additive and flag-gated. |

Annotated tag `safety/pre-four-root-convergence-2026-09-01` exists in all three
repositories at the original local `main`. No remote branch is changed by this
landing.

Two preservation branches remain intentionally outside the app baseline:

- `codex/app-local-preservation-2026-09-01` retains a local Life primitive
  draft whose one-line truncations are weaker than the reviewed two-line
  convergence components.
- `codex/artifact-composition-fixtures` retains an older generated-type commit;
  the converged contract is newer and includes `CompositionBriefV1`.

The workspace research-preservation commit is included in the convergence
line, including the unique Life closure and corrected document lifecycle
metadata.

## Verification evidence

### Cross-repository contract

- OpenAPI generation: 3,253,434-byte complete snapshot.
- Active mobile projection: 431 paths, 476 operations, 1,253 schemas.
- Complete snapshot: 564 paths, 626 operations, 1,406 schemas.
- Generated TypeScript exactly matches the mobile projection.
- `make contract-check`: passed, including occasion behavior, ten Place
  identity seams in both directions, and 354 schema bridge types.
- API coverage: 551 active, 13 dark, 62 retiring, zero unflagged operations.
- Alembic graph: one head, `xgraph21`.
- Feature flags: 97 registered, none overdue or unregistered. The Places v2
  renderer remains explicitly default-off and subordinate to the root gate.

### Backend

- Root, Artifact, Life, and API focused suite: 78 passed.
- Semantic-facade and prior-trip custody suite: 34 passed.
- Commit hooks passed, including formatting, import boundaries, timeouts,
  mutable-state checks, broad-exception no-growth, and size budgets.
- Broad exceptions are at the audited ceiling of 1,190. The convergence work
  removed its two broad shadow handlers and narrowed one inherited import
  boundary rather than raising the ceiling.

The full offline suite initially ran under disk exhaustion and produced noisy
failures. After freeing clean worktrees and caches, the exact remaining failure
set was compared against pre-convergence `main`: 24 failures reproduce on
`main`; one convergence-only custody expectation was corrected and its focused
suite now passes. The 24 inherited failures are not admitted as new regressions
and are not silently re-baselined here.

### App

- TypeScript `tsc --noEmit`: passed.
- Canonical Places projection parity: 13 passed after restoring the shared-Trip
  identity boundary for the Lisbon group decision.
- The full serial Jest run exposed eight failing suites before the process
  terminated with exit 139 under resource pressure. A bounded rerun reproduced
  seven on pre-convergence `main`; the single convergence-only failure was
  fixed. The seven inherited failures remain visible and are not converted into
  new acceptance criteria by this landing.

### Documentation

- Workspace governance, inventory, spine, canon budget, release scope, current
  state, living links, compatibility ledger, and Home-surface governance pass.
- Life fixture validation passes: six worlds, six indexes, three full episodes,
  four compositions, fourteen social transitions, and fourteen visual frames
  plus v0.2 additions.
- Child-document governance remains an inherited baseline: 145 issues across
  107 files—71 backend and 36 app files. All four convergence-only app document
  failures were corrected. The remaining files already existed on the original
  child `main` branches and are recorded as cleanup debt, not waived or hidden.

## Useful boundaries preserved

1. Root projections read owner truth; they do not become owners.
2. A Composition is generated return value, not an Artifact or historical fact.
3. Home and Places return value without requiring input; Chat remains the clean
   contribution and agency layer; Life remains stable continuity and refinding.
4. Exact root context survives a handoff without encoding component names.
5. Personal memory admits explicit actor-bound statements, not inferred mood,
   personality, emotional investment, or silence.
6. The existing Places feed, Plan/Trip authorities, provider owners, and
   Atlas/You compatibility machinery remain available during dark migration.
7. All new roots, refinding lanes, and semantic shadows remain default-off.

## Known debt after landing

- Production navigation still defaults to the legacy shell.
- Home and Places do not yet cover their complete accepted unit unions, C2
  multiplayer consequence, C3 causal repair, or F5 provider recovery.
- Life lacks complete Places/People/Threads production lenses, Together write
  paths, dossier-grade destinations for every family, and exact end-to-end
  refinding return.
- Chat has not yet been redesigned or migrated to the full four-root role.
- Real-data ranking, accessibility, performance, device, staging, and human
  value evidence remain promotion gates.
- The 24 inherited backend failures, seven inherited app suites, and 107 child
  docs with lifecycle debt require separate cleanup programs.

## Landing and rollback

Fast-forward local `main` in the order backend, app, workspace only after the
final contract and documentation checks. Add
`baseline/four-root-convergence-2026-09-01` at each landed tip. Retain safety and
preservation refs until a later cleanup confirms no unique commit is needed.
Do not push as part of this local convergence.
