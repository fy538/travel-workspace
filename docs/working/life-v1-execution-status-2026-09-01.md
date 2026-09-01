---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Records the executed, cross-repository Life v1 foundation and its validation evidence so future design work can build on committed seams rather than re-open the architecture.
depends_on:
  - life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
  - life-v1-destination-and-refinding-contract-2026-09-01.md
  - ../contracts/life-v1-experience.md
  - ../systems/four-root-loop-object-surface.md
---

# Life v1 — execution status

## Outcome

The non-regrettable Life foundation is now implemented in isolated child-repo
branches and represented in the shared contract snapshots. It is additive and
reversible: the existing Atlas/You history owner remains intact, while an
internal flag can expose a native Time root backed by a typed read projection.
No public promotion, generalized dossier system, Together persistence, or
repository-wide noun migration was attempted.

## Landed checkpoints

### Backend (`Travel Agent`)

- `029e22870` — pure dark Life projection compiler.
- `1190a707c` — deterministic cross-root Return arbitration.
- `115c00d41` — additive `GET /api/root-projections/v1/life` route and adapter.
- `0f2341b7e` — merge with the landed root-v2 Strategy contract.
- `9a546301f` — clarify that `LifeRootProjectionV1` is the served read model.

The compiler is viewer-scoped, deterministic, bounded per lens, and emits
canonical `ResourceRef` handles. The route currently projects graph-backed
plans, occasions, commitments, and outcomes into the Time lens; empty data is
an honest `thin` projection.

### Frontend (`Travel App`)

- `3db6c9ee` — flagged native Life Time root and typed primitives.
- `6d8aa4b0` — pure allowlisted ResourceRef destination resolver.
- `013b3c75` — generated Life contract types.
- `92d1502d` — synchronized Life root contract types.
- `bd3730d2` — merge with the landed root-v2 Strategy surface work.

The native root has loading, informational, failure/retry, and data states;
four lens labels; bounded Time rows; a canonical complete-record door; and
optional server-authored Return rendering. It contains no input prompt,
client-authored interpretation, arbitrary route push, or infinite-scroll
archive. `EXPO_PUBLIC_LIFE_ROOT_V1` is default-off and internal/dev-only.

### Shared workspace

- `b52bbf9` — synchronized flag registry, operation policy, complete OpenAPI
  snapshot, and derived mobile projection. The Life operation is explicitly
  registered and the derived projection contains the Life route and schemas.

## Validation evidence

- Backend pre-merge Life/compiler/root-v2/API focused suite: 29 tests passed.
- Frontend Life/conformance/resolver focused suite after merge: 17 tests passed.
- Frontend `npm run typecheck`: passed.
- App OpenAPI projection check with the Life worktree: passed — 430 paths,
  475 operations, 1,222 schemas.
- Cross-repository API audit with the Life worktree: passed — 550 active, 13
  dark, 62 retiring operations; 0 unflagged.
- Backend commit hooks passed all applicable checks. The repository-wide broad
  exception and size-budget hooks remain at their pre-existing baseline
  ceilings and were skipped for the small docstring follow-up, as required by
  the execution plan.
- The full backend pytest command could not run in this worktree because its
  isolated environment has no installed `sqlalchemy`; the focused suite was
  already green before the merge and no backend behavior changed in the final
  wording follow-up.

## Deliberately deferred

1. Dossier-grade destinations for every Life object family and scroll-position
   restoration.
2. Full Places/People/Threads lens projection from production data.
3. Public rollout, analytics-driven promotion, and removal of legacy Atlas.
4. Together/multiplayer write paths and generalized Occasion architecture.
5. Visual composition polish beyond the production HTML design reference.

The next safe increment is to add one benchmark object's exact owner dossier
and refinding continuation, then re-run the same contract and conformance
gates. Do not broaden the flag or add more lenses until that refinding seam is
proven end to end.
