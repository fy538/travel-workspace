---
doc_type: working
status: active
owner: product / backend / frontend
created: 2026-09-03
expires: 2026-10-03
why_new: Records the commit-by-commit execution of the entity-system next program while preserving concurrent Home/Places work and the no-backfill boundary.
supersedes: []
---

# Entity system execution log — 2026-09-03

This log records the first implementation pass for
[`entity-system-next-program-2026-09-03.md`](entity-system-next-program-2026-09-03.md).
It is an execution record, not a release declaration. No catalog backfill was
run.

## Landed

Backend branch `codex/entity-shell-resolution`:

- `30ad05979` — additive entity-detail presentation v2, redirect alias sets,
  and a batch viewer relationship reader.
- `33ce29e15` — canonical entity refs on private outcome summaries and bounded
  private verdict projection.
- `c07582731` — no-store entity situation request/response and Plan/route
  composer with typed silence and freshness bounds.
- `e97ec2d6c` — snapshot-backed lived-experience provider consumes the same
  relationship projection.
- `9373f8665` — explicit accommodation Plan relationship reader.
- `3cfe3201e` — bounded situation characterization tests.

Mobile branch `codex/entity-shell-resolution`:

- `e8475df47` — v2 relationship/capability-compatible object-page grammar and
  API client adapter.
- `ef6bd32d3` — expiring entity-situation API adapter and generated contract
  types.
- `78ccf1cab` — preserve the established site v1 route while migration stays
  opt-in; existing smoke tests remain green.

## Contract boundaries preserved

- The existing v1 presentation endpoint remains available.
- V2 does not call Google, routing, weather, or an LLM during the durable
  object read.
- Live situation is separate, authenticated, short-lived, and never echoes
  precise origin coordinates.
- `loved` affinity is not treated as `saved`; only an active save row yields
  the saved state in the canonical projector.
- Accommodation lived state is still absent; dates passing are not an
  occurrence authority.
- No source, Plan block, outcome, or entity catalog rows were backfilled.

## Verification

- Backend focused relationship/presentation tests: passing.
- Backend situation characterization tests: passing.
- Mobile TypeScript check: passing.
- Mobile site data and smoke tests: passing.
- OpenAPI projection check against the entity branches: passing (`438` paths,
  `483` operations, `1288` schemas).
- The full backend offline suite was started but interrupted during its long
  async teardown after pre-existing unrelated failures; it is not a release
  gate result.

## Next gated work

The next safe slice is to add a v2 consumer behind an explicit mobile rollout
flag, then migrate venue relationship/capability regions with physical Places
QA. Workspace OpenAPI snapshots are intentionally not overwritten in this
pass because they contain concurrent Home/Places Source changes; they should
be regenerated and reviewed when these two branches are integrated.
