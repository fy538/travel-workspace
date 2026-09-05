---
doc_type: working
status: active
owner: product / backend / mobile
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records the bounded execution of the entity acceptance plan, its cross-repository commits, deterministic/real-backend evidence, and gates that remain intentionally open.
supersedes: []
depends_on:
  - docs/working/entity-system-acceptance-plan-2026-09-05.md
  - docs/working/entity-pilot-release-manifest-2026-09-05.md
---

# Entity system execution receipt — 2026-09-05

## Scope and safety boundary

This receipt covers the scoped venue, site, and experience object-page work
authorized by the user's execution instruction. It does not authorize or
perform catalog/provider backfill, production writes, paid research, provider
calls, scheduled refresh, or feature-flag enablement. The rebuilt object page,
research request path, and relationship people-line capability remain
independently gated.

## Landed implementation packages

| Package | Repository | Commit(s) | Outcome |
| --- | --- | --- | --- |
| C1 public sharing | `travel-app` | `7a783afae` | Canonical public name/link only; private Take prose is not shareable. |
| C2 canonical route ownership | `travel-app` | `d667c9a60` | Rebuilt venue/site/experience routes own canonical reads; compatibility reads and provider photo lookup are gated off the rebuilt path. |
| C3 mounted freshness | `travel-app` | `cf12de16a` | Mounted expiry ticks and foreground lifecycle re-evaluate research visibility. |
| C4 research lifecycle | `travel-app` | `1f33413c4` | Request/status identity correlation, bounded active polling, deliberate retry identity, and offline/background guards. |
| C5 people contract | `travel-agent` | `121210dfe` | Server `evaluated_at` plus per-line bounded `valid_until`; lease never extends handoff expiry. |
| C5 people authorization | `travel-agent` | `b7d2a8bde` | Read-time exact-pair roster, active conversation, source anchor/artifact ownership and custody rechecks. |
| C5 people client | `travel-app` | `2fbc592eb`, `bbb597442` | Fail-closed validity, expiry/background/offline hiding, foreground/reconnect validation, race guards, and viewer-cache eviction. |
| C5 sheet behavior | `travel-app` | `c28a9d9c9` | Selected people-line sheet closes when withdrawal/expiry removes its line. |
| C6 owner continuity proof | `travel-agent` | `120c34b31` | Disposable PostgreSQL test proves canonical read, pair withdrawal, and sender revoke behavior. |
| Contract synchronization | workspace + app | `45c0a1c`, `2fbc592eb` | OpenAPI snapshots and generated TypeScript include people validity metadata. |

## Verification evidence

### Backend

- `PYTHONPATH=. .venv/bin/pytest tests/api/test_entity_people_lines.py tests/api/test_entity_research_requests.py tests/research_agent/test_research_queue.py tests/places/test_entity_presentation_read.py tests/places/test_private_entity_contracts.py -q` — **60 passed**.
- `PYTHONPATH=. .venv/bin/pytest tests/places/test_relationships.py tests/domains/relationships/test_persistence_postgres.py tests/domains/relationships/test_consequence_gateway.py tests/domains/relationships/test_models.py -q` — **20 passed**, including the real PostgreSQL people-line test.
- Touched-file Ruff check/format check — **passed**.
- Backend pre-commit size-budget hook remains a repository-wide baseline failure (unrelated oversized files/functions); commits used the single documented skip and do not claim a clean whole-repository hook run.

### Mobile

- Entity/research/object-page selection — **84 passed** across 8 suites.
- People-line lifecycle + mounted expiry selection — **7 passed** across 2 suites.
- `npx tsc --noEmit` — **passed**.
- `npx tsc --project tsconfig.tests.json` — **passed**.
- `npm run lint` — **0 errors, 178 pre-existing warnings** (including the existing object-page max-lines warning).
- `./scripts/sync-types.sh` — **passed**; reviewed `docs/openapi.json`, `docs/openapi.app.json`, and `travel-app/utils/api/schema.gen.ts`.

### QA and design gates

- `npm run qa:polish:scenarios` — **passed**, 31 registered scenarios.
- `npm run qa:design:check -- entity-object` — structural check passed with a warning: no isolated design-reference manifest exists.
- `node scripts/polish-qa/run-polish-qa.mjs entity-object --dry-run` — scaffolded a run with 3 intended flows and **0 captures**. Metro was not reachable; this is not native acceptance.
- The approved `/Users/feihuyan/Downloads/vesper-entity-object-handoff-lab` export is still absent. No pixel-level/design verdict is claimed.

## Current capability verdict

| Capability | Implementation | Deterministic tests | Real backend | Native/design | Enabled |
| --- | --- | --- | --- | --- | --- |
| Core page | Complete for scoped code paths | Complete for listed suites | Existing cheap/read lanes plus route coverage | **Open**: device/native and approved reference capture | **Off by default** |
| Research | Complete lifecycle hardening | Complete for request/status/expiry races | Queue/read tests pass; paid/provider canary not run | **Open**: native and operational canary | **Off by default** |
| People | Complete bounded projection/client guard | Complete for malformed/expiry/background/offline/race/sheet cases | Pair withdrawal/revoke PostgreSQL proof passes | **Open**: two-account device timing and privacy-owner lease decision | **Off by default** |

The people implementation uses the plan's proposed maximum 60-second
visibility lease for unobserved cross-device revocation. That is a bounded
consistency statement, not an instantaneous-revocation promise. The people
flag must remain off until the privacy owner accepts that bound or an existing
owner invalidation channel is proven.

## Remaining owner actions

1. Provide and register the isolated Claude Design export, then capture and
   review iOS and Android rebuilt-page flows against it.
2. Run authenticated two-account native evidence for people withdrawal,
   foreground/reconnect, process restart, and selected-sheet closure.
3. Obtain an explicit privacy-owner decision on the ≤60-second lease (or prove
   an invalidation channel) before people enablement.
4. Keep research/provider spend and all backfill disabled until a separately
   named owner, output inspection plan, budget, and reviewed build exist.

No deployment, merge-to-release, cohort rollout, or backfill claim follows
from this receipt.
