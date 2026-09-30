---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No existing document measures, in one place and with evidence, how CI, local gates, environments, release tooling, lane process and background cost currently limit Vesper's speed to a shippable build, nor ranks what to fix versus relax.
promotes_to: null
supersedes: []
---

# Infrastructure, delivery pipeline and process: inventory and speed-to-ship fixes

## Evidence boundary

- **Inspected on:** 2026-09-26.
- **Code baselines:**
  - Read-only baseline: `/Users/feihuyan/travel-workspace--product-map-inventory` at workspace `6ef3dca`, backend `c8c9f5785` and app `43225df35`. These equal `origin/main` in all three repos.
  - The canonical main checkout at `/Users/feihuyan/travel-workspace` has two unpushed local commits (`8a36fab`, `878581b`) and is 57 commits behind `origin/main`.
- **Commands run (all read-only):** `git`, `gh` (runs, jobs, logs, annotations, PRs, branch protection, collaborators, secret names), `eas build:list`, `eas update:list`, `eas env:list` (names only), unauthenticated `GET` requests to production `/health`, `/ready`, `/privacy` and `/health/background-tasks`, and static parsing of registries and docs.
- **Not run:** `make verify`, tests, builds and deploys.
- **Could not observe:**
  - `fly status`, `fly secrets` and machine counts: `flyctl` has no access token on this machine.
  - External consoles: App Store Connect, Apple Developer/APNs, Clerk, Anthropic billing, PostHog, Sentry and Langfuse.
  - Anything said below about those systems comes from repository configuration or `docs/Owner Action Items.md`, and is labelled that way.
- **Input from other agents:** two background-loop and subscriber inventories at `c8c9f5785`. The orchestrator spot-checked parts of them, and I re-checked five citations. They are used in §5.

Statuses below are **observed** (a command output), **config** (read from a committed file), or **inferred** (reasoned from observed facts).

---

## 0. The picture in ten facts

1. **No build of the current product exists on any phone.**
   - The last EAS build of any kind was 2026-08-04: a `dogfood` build of app `605988afa`. `origin/main` is 1,890 app commits later.
   - The last OTA update to the `dogfood` channel was about a month ago.
   - None of the 50 most recent EAS builds used the `production` profile. No TestFlight build has ever been made.
2. **Production backend is six weeks stale.**
   - Production `/ready` reports `git_sha 4a7f3e6f0` (2026-08-14). That is 1,673 backend commits behind `origin/main`.
   - 77 new Alembic migrations are waiting to run against production.
3. **No installable profile shows the current product.**
   - The four-root shell (Home, Places, Life) is behind `EXPO_PUBLIC_FOUR_ROOT_SHELL`, `EXPO_PUBLIC_ROOT_PROJECTION_V2`, `EXPO_PUBLIC_PLACES_ROOT_V2_RENDERER` and `EXPO_PUBLIC_LIFE_ROOT_V1`.
   - None of the six `eas.json` profiles sets any of them (`travel-app/eas.json`; `travel-app/utils/productSystemRollout.ts:74-94`).
4. **Child-repo `main` CI has not passed since mid-May:**
   - Backend's last green `main` run was 2026-05-12, and the app's was 2026-05-13.
   - Since June there have been about 188 backend and about 184 app failed `main` runs, with zero passes.
   - From June to early September most of these were **not code failures.** Annotations read "The job was not started because recent account payments have failed or your spending limit needs to be increased" (checked on a 2026-07-09 backend run and a 2026-08-13 app run).
5. **Today's red CI is caused by credentials, the calendar and missing secrets, not by code:**
   - Workspace `Reliability` fails at private-child checkout because `TRAVEL_WORKSPACE_CI_TOKEN` (created 2026-05-11) no longer authenticates. Its last pass was 2026-07-10.
   - On `main`, backend `test` fails at `check_vesper_world_catalogs.py --runway-days 14`, a date check. The whole offline test suite behind it is then skipped.
   - App `main` fails "Design status is stale".
   - `cron.yml` failed 64 of 64 runs (no `DATABASE_URL` secret).
   - The AI canaries failed 4 of 4 (no `ANTHROPIC_API_KEY` secret).
6. **More failures are already scheduled.** With no code change, these checks go red on these dates:
   - Workspace flag checks: 2026-09-29 (3 flags), 2026-10-02 (1), 2026-10-05 (36) and 2026-10-08 (10).
   - The compatibility ledger: 2026-10-06.
   - API operation-policy reviews: 2026-10-08 (55 operations).
   - The design-gate judge calibration: 2026-10-09.
   - The flag check also runs as a **pre-push hook** in the workspace, so from 2026-09-29 every workspace push is blocked locally.
7. **Branch protection cannot be satisfied by a solo founder, so every merge is a bypass anyway.**
   - All three repos require 1 approving review, the last-push approval rule, `enforce_admins: true`, and strict up-to-date branches.
   - The workspace has one collaborator (the founder).
   - The last three recovery PRs (#36, #233, #201) merged with `reviewDecision=REVIEW_REQUIRED`. Workspace #36 also merged while its only required check was failing.
8. **Receipts outweigh code.**
   - Over the last 7 days (all refs), the workspace had 429 non-merge commits: 420 docs-only, with 218.8K lines of doc churn.
   - The two children together had 407 commits, of which 258 touch product code, with 36.4K lines of product-code churn.
   - In today's active lane (`codex/home-value-delivery`), the workspace gained 28 "record…" documentation commits against 16 app and 3 backend commits.
9. **Integration is big-bang.**
   - From 2026-08-15 to 2026-09-22 no PR merged into either child `main`, apart from Dependabot PRs and a few local merges pushed directly on 09-01 to 09-06.
   - Then backend #229 merged 375 commits (+74.7K lines) and app #199 merged 220 commits (+35.6K lines). Both lanes were about 15 days old.
   - The following recovery lane took 59 hours from first commit to merge. It needed 5 CI attempts in each child.
10. **Background LLM work is broadly ungated.**
    - Production reports 29 of 30 lifespan loops running, including every LLM loop.
    - `DISABLE_LLM_BACKGROUND_LOOPS` stops only 6 loops at startup. Several paid paths ignore it.
    - Retired booking execution is still reachable, because `BOOKING_EXECUTION_RETIRED` is absent from `fly.toml`.
    - No spend cap exists in code.
    - PostHog is unset (Owner Action Items §6), and app crash reporting is disabled in every EAS profile.

**Implication:** the fastest route to "across the line" is operational, not architectural. Get one current build onto the phone against a current backend, make `main` green and keep it green, and stop the calendar and the receipts from consuming agent time. §6 ranks the work.

---

## 1. CI/CD

### 1.1 Workflow inventory

There are 17 workflows (3,068 lines of YAML) across the three repos.

| Repo | Workflow | Trigger | Runner | Purpose | Last 14 days (observed) |
|---|---|---|---|---|---|
| workspace (public) | `reliability.yml` "Reliability" | push/PR to main; child dispatch | ubuntu | Checks out both children with `TRAVEL_WORKSPACE_CI_TOKEN`. Then runs OpenAPI freshness, `contract-check`, journey mock-walk, Maestro semantic validation, surface contraction, compatibility/card-arrival, journey/flag registries, doc governance (6 checks), `api-coverage-check`, golden-path QA and the reliability gate | **0/17 passed.** Every run fails at "Check out Travel Agent" with `fatal: could not read Username` |
| workspace | `visual-qa.yml` "Maestro PR smoke" | daily cron 07:00 UTC + dispatch | **macos-15** | Maestro iOS simulator smoke | **0/15** (same checkout failure) |
| workspace | `visual-qa-cloud.yml` | PR | ubuntu → macos | Maestro Cloud gate | 11 "success", but the smoke job is **skipped**: `MAESTRO_CLOUD_API_KEY`, `MAESTRO_CLOUD_PROJECT_ID` and `EXPO_TOKEN` secrets are absent |
| backend | `ci.yml` "CI" | push/PR to main | ubuntu | lint, import-boundaries, typecheck, test (offline), test-db, test-db-migrate, dogfood-persona-gate, eval-replay, package-smoke, dispatch to workspace | PR 1/12 passed; push 0/4 |
| backend | `cron.yml` | 5 daily/weekly crons | ubuntu | venue refresh, cache purge, LLM quality sampling, drift, cancellation SLA, angle promotion, dossier publish | **0/64** (`psycopg2… localhost:5432 refused`, no `DATABASE_URL` secret) |
| backend | `ai-live-canary.yml`, `ai-redteam-canary.yml` | weekly cron | ubuntu | Live model canaries | **0/4** (`ANTHROPIC_API_KEY secret is not configured`) |
| backend | `eval.yml`, `dogfood-persona-gate-full.yml`, `live-booking-canary.yml` | dispatch only | ubuntu | Evals, full persona gate, booking canary | not run |
| backend, app | `labels.yml`, `issue-intake-labels.yml` | label/issue events | ubuntu | Housekeeping | — |
| app | `ci.yml` "CI" | push/PR to main | ubuntu | Lint, Frontend governance (30 budget scripts), Security audit, Visual evidence contracts, Type check, Test, API types freshness, Logic QA journeys, QA tooling contracts, Design alignment gate, dispatch | PR 1/14 passed; push 0/3 |
| app | `design-system-contracts.yml` | push/PR | ubuntu | Design-system contracts | 4/14 passed |
| app | `mobile-stability-device.yml` | dispatch only | macos-15 | Screenshot/performance matrix | not run; needs `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` and `MOBILE_STABILITY_IOS_APP_URL` GitHub secrets, which are absent |

**Secrets per repo (names and dates only, observed):**

- workspace: `TRAVEL_WORKSPACE_CI_TOKEN` (2026-05-11).
- backend: `TRAVEL_WORKSPACE_DISPATCH_TOKEN` (2026-05-11).
- app:
  - `TRAVEL_AGENT_CI_TOKEN` (2026-09-08). This one works: app CI checks out the backend successfully.
  - `TRAVEL_WORKSPACE_DISPATCH_TOKEN` (2026-05-11).
- No repository variables are defined.

### 1.2 Required checks and branch protection (observed)

| Repo | Required checks | Reviews | Other |
|---|---|---|---|
| workspace | `Contract and golden paths` | 1 approval, dismiss stale, **require last-push approval** | strict, enforce_admins, no force-push. Collaborators: `fy538` only. **Visibility: public** |
| backend | `lint`, `import-boundaries`, `typecheck`, `test`, `test-db-migrate`, `test-db`, `dogfood-persona-gate`, `eval-replay` | same | same. Second write collaborator `fiona161616`. Private |
| app | `Lint`, `Type check`, `Test`, `API types freshness`, `Logic QA journeys`, `QA tooling contracts`, `Design alignment gate`, `Frontend governance`, `Security audit`, `Visual evidence contracts` | same | same. Private |

Other repository settings: auto-merge disabled and delete-branch-on-merge disabled everywhere.

**Why this is a speed problem:**

- The "last-push approval" rule plus `enforce_admins` means the founder's own lane branches can never satisfy protection on their own.
- The August session log records the founder disabling `enforce_admins` to admin-merge PR #203 for exactly this reason (`travel-agent/docs/working/session-log-product-model-and-spatial-intelligence-2026-08-06.md:107`).
- `enforce_admins` is on again today. Yet PRs #36, #233 and #201 all merged with `REVIEW_REQUIRED`, and #36 merged with its sole required check red. Protection was therefore relaxed or bypassed at merge time (inferred).
- The rules add a manual toggle to every landing while providing no actual review.
- `strict: true` forces a rebase and a full 13–15 minute rerun of every open PR after each merge.

### 1.3 Long-run CI history (observed)

| Repo | Last green `main` run | `main` runs Jun–Sep | Dominant cause |
|---|---|---|---|
| backend | 2026-05-12 | ≈188 failed, 12 cancelled, 0 passed (no runs in August: Actions disabled until the 09-07 audit) | GitHub billing "job was not started" (Jun–Jul); now the catalog-runway date check |
| app | 2026-05-13 | ≈184 failed, 16 cancelled, 0 passed | Billing (Jun–Aug); now "Design status is stale" |
| workspace | 2026-07-10 | 17 failed since 09-23 | Private checkout credential. It worked on 07-10, so it expired or lost access in between. Creation on 05-11 fits a 60–90-day fine-grained PAT expiry (inferred) |

**Consequences:**

- For roughly four months, "done" could only be claimed from local runs and hand-written receipts. That is the root of the receipt culture described in §4.5.
- `docs/operations/Deploy Checklist.md` §2 already documents the billing failure mode. It suggests `gh pr merge --admin` as the workaround.

### 1.4 What is red right now, and why

| Failure (observed) | Cause | Class | Fix |
|---|---|---|---|
| Workspace `Reliability` and `Maestro PR smoke` | `TRAVEL_WORKSPACE_CI_TOKEN` rejected at child checkout (`could not read Username`) | credential | Founder: issue a fine-grained PAT or GitHub App token with `contents:read` on `travel-agent` and `travel-app`, and replace the secret. Check `TRAVEL_WORKSPACE_DISPATCH_TOKEN` (same creation date) at the same time |
| Backend `test` on main (2026-09-26 run 36210574449) | `check_vesper_world_catalogs.py --runway-days 14`: "must contain at least three rows per band on 2026-10-09: season=0, here=0". The source-reviewed catalog rows expire 2026-10-09 (`backend/home/vesper_workbench/data/{season,here}_windows.yaml`) | **calendar** | Move to a weekly content job. It currently masks `Run offline tests with coverage` (skipped) |
| App `Design alignment gate` on main (run 36210578474) | "Design status is stale. Run: npm run design:status and commit the result". The committed derived status drifted after merge. The policy gate itself passed | derived artifact | Generate status in CI instead of committing it, or regenerate it in pre-push |
| Backend `cron.yml` (64/64) | No `DATABASE_URL`/`POSTGRES_*` secrets; connects to `localhost` | missing secret | Remove the schedule. Owner Action Items §5 already says run ops crons manually until there is real traffic |
| `ai-live-canary`, `ai-redteam-canary` (4/4) | No `ANTHROPIC_API_KEY` secret | missing secret | Add a capped key, or disable the schedules |
| Dependabot PRs (49 since 08-01: 17 backend, 32 app; 20 closed unmerged) | Branch CI red for the reasons above; native bumps such as RN 0.87.1 fail | noise | Security-only updates for native dependencies (§6) |

### 1.5 CI runtime (observed, last green PR runs)

| Repo | Job | Duration |
|---|---|---|
| app (35979539670) | Test | 12.6 min |
| | Logic QA journeys | 10.0 min |
| | Type check | 2.6 min |
| | Lint | 1.7 min |
| | Frontend governance | 1.4 min |
| | Visual evidence contracts | 1.2 min |
| | QA tooling | 1.1 min |
| | Design gate | 1.1 min |
| | API types | 1.1 min |
| | Security audit | 0.7 min |
| backend (35976026080) | test-db | 12.7 min |
| | test (offline) | 8.3 min |
| | import-boundaries | 3.4 min |
| | typecheck | 3.0 min |
| | dogfood-persona-gate | 3.0 min |
| | test-db-migrate | 2.5 min |
| | package-smoke | 2.2 min |
| | eval-replay | 1.9 min |
| | lint | 1.3 min |

**Wall-clock and billed time:**

- Both children take about 13–15 minutes wall-clock with jobs running in parallel.
- Billed Linux time is about 34 job-minutes per app run and about 38 per backend run (inferred from job durations; the billing timing API returned zeros).
- No workflow has path filters, so documentation-only child PRs also run the full 13–15-minute matrix.
- The workspace repo is public, so its minutes are free. The children are private, and they are what exhausted billing before.

### 1.6 Flaky and quarantined tests (observed)

- **Backend:**
  - `tests/flaky_order_baseline.txt` quarantines 53 exact order-dependent tests as non-strict `xfail` (`tests/conftest.py:361-410`), with review date 2026-10-07.
  - `tests/postgres_leak_baseline.txt` holds about 240 tests that touch Postgres undeclared; it is a shrink-only ratchet.
  - There are 57 `skip`/`xfail` markers.
  - The offline suite collects about 17.8K tests (the 08-12 baseline recorded 17,784 passed and 56 xpassed in 440.9 s).
- **App:** no `it.skip`/`xit`. During the recovery lane there were two consecutive `Test` failures, fixed by `efbdba7ec test(chat): await committed reconnect state before stale-stream assertions`. This is a timing flake class, not a product bug.
- **What CI caught on the recovery PR:**
  - Backend runs failed on Alembic drift, offline tests, DB tests, dogfood seeding and the Atlas Postgres canary. These are mostly real regressions.
  - App runs failed on budgets (`size-budgets`, `typography-budget`), the polish-QA self-tests, the design gate, the security audit, and Logic QA and Test.
  - About half the app failures were governance and budget rather than behavior (inferred from job names).

### 1.7 Cross-repo pinning

- The workspace pins child SHAs in `docs/child-repos.ci-lock.json`.
- App CI separately pins workspace and backend SHAs in `travel-app/.github/ci-lock.json`.
- A cross-repo change therefore needs pin bumps in two repos in a specific order: publish children, pin, then rerun. The CI Plan describes this sequencing.
- This is correct for release tuples but heavy for everyday PRs.

---

## 2. Local verification gates and governance load

### 2.1 `make verify` composition (config: workspace `Makefile:337-363`)

1. `make doctor`: layout and tools.
2. `make -C travel-agent ci`, in this order:
   - ruff and format;
   - import boundaries, lazy-import inventory and SCC ratchet;
   - route shadowing;
   - `gates`: 18 structural scripts, including route auth, response-model floor, async/sync DB, `get_tx` ratchet, itinerary writer/consumer/reader boundaries, broad-exception ratchet, Anthropic timeout, trip IDOR, size budgets, prompt contracts, prompt→tool drift, eval-config drift and public-projection leak;
   - **`vesper-world-catalogs` (date runway)**;
   - mypy;
   - offline pytest (about 7.3 min);
   - tool-contract tests;
   - `eval-ci`.
3. `make contract-check`: cross-repo fixtures, OpenAPI → projection → `schema.gen.ts`, occasion behavior contract, and the schema-bridge manifest.
4. `make api-coverage-check`, which **fails on expired `review_by`** for dark/retiring operations (`scripts/api_contract_audit.py:589-608`).
5. `make typecheck` (tsc).
6. Jest: journeys, 6 mock/API seam suites, and `test:offline`.
7. 13 workspace gates:
   - `maestro-flow-check`
   - `journey-registry-check`
   - **`flag-registry-check` (expiry)**
   - `docs-spine-check`, `docs-canon-check`, `docs-release-check`, `docs-status-check`, `docs-links-check`, `docs-child-governance-check`
   - **`compatibility-check` (expiry)**
   - `card-arrival-check`, `chat-card-types-check`

**Timing:**

- **Last recorded pass:** 944.834 s (15.7 min) on 2026-09-24 for the recovery tuple (`docs/working/historical-branch-recovery-audit-2026-09-23.md:86`).
- Backend `ci` alone took 493 s on 2026-08-12 (`docs/reliability/test-loop-baseline.md`).
- The app pre-push hook took about 15 s.
- `verify-changed` exists but is labelled experimental (`Makefile:327`).
- Because `make` stops at the first failure, a date check placed early (catalog runway, before mypy and tests) hides every later signal.

### 2.2 Scheduled date failures (computed from the committed registries)

| Date `main` goes red | Gate | Items | Effect |
|---|---|---|---|
| **already** (since about 09-25) | backend `vesper-world-catalogs --runway-days 14` | Season and Here bands empty on 10-09 | backend CI `test` and `make verify` red |
| **already** | app design status freshness | derived `STATUS` | app required check red on `main` |
| 2026-09-29 | `flag-registry-check` (CI + **workspace pre-push hook**) | `ADAPTIVE_PLACES_ORIENT_SHADOW_ENABLED`, `EXPO_PUBLIC_FOUR_ROOT_SHELL`, `EXPO_PUBLIC_ROOT_PROJECTION_V2` (expire 09-28) | every workspace push blocked locally |
| 2026-10-02 | same | `PLACES_ROOT_V2_RENDERER_ENABLED` | — |
| 2026-10-05 | same | 36 flags (30 backend, 6 app) | — |
| 2026-10-06 | `compatibility-check` | 4 ledger entries (expire 10-05) | `make verify` red |
| 2026-10-08 | `api-coverage-check` | 55 retiring operations (renewed to 10-07 in the recovery lane) | `make verify` red, and workspace CI once the token is fixed |
| 2026-10-08 | `flag-registry-check` | 10 more flags | — |
| 2026-10-08 | schema-bridge | 1 `unmodeled_wire` (`AgentWorkflowCompletionReceipt`) | `contract-check` red |
| ~2026-10-09 | app `design:gate` | judge calibration older than 14 days (scored 2026-09-24T04:19Z by "Codex current session") | required app check red |

**Registries that carry expiry dates (observed):**

- `docs/flags/registry.yaml`: 106 flags, 104 active.
  - 87 default off: 63 backend and 24 app.
  - 56 expire within 30 days.
- `docs/governance/api-operation-policy.json`: 284 operations (207 active, 62 retiring, 15 dark).
  - 194 `review_by` dates.
  - 17 already past on active operations. These are not enforced because only dark and retiring entries are checked.
- `docs/governance/compatibility-ledger.json`: 4 entries, all expiring 10-05.
- `travel-app/scripts/schema-bridge-manifest.json`: 376 entries (199 generated_alias, 113 schema_projection, 51 ui_only, 12 adapter, 1 unmodeled_wire). The expiry is enforced only on `unmodeled_wire`.
- World catalogs: 7 rows.
- Design exemptions (`until`) and judge calibration (14-day freshness).
- `tests/flaky_order_baseline.txt` (review-by 10-07; not enforced).
- Working-doc `expires` (not enforced).

**Pattern:** every expiry is a small manual renewal task that an agent must notice, research and document. The recovery lane spent part of its time re-reviewing 55 API operations and replacing catalog rows only to buy about two weeks (`historical-branch-recovery-audit-2026-09-23.md:2470-2490`). The same work falls due again in October.

### 2.3 Gate inventory and value

About 154 custom gate scripts exist:

- 26 workspace `check|validate|sync|render` scripts;
- 68 backend `check_*.py`;
- 60 app `check-*` scripts;
- 59 app npm scripts named budget, governance, guard, check, ratchet, audit or gate;
- 188 app npm scripts in total, 52 of them `qa:*`.

| Gate family | Catches | Cost today | Verdict |
|---|---|---|---|
| ruff/ESLint, tsc, mypy (baseline), backend offline pytest, app Jest | Real regressions | 8–13 min CI | **Keep blocking** |
| test-db, `test-db-migrate` (autogenerate drift, CHECK-constraint drift, migration lifecycle) | Schema and data safety. **The highest-value gate right now**, with 77 migrations pending in production | 12.7 + 2.5 min | **Keep blocking** |
| OpenAPI freshness, contract-check, API types freshness, card-arrival, chat-card types, cross-repo fixtures | Cross-repo wire drift (the 05-19 incident) | cheap | **Keep blocking** (one owner: app CI, plus local `sync-types`) |
| Route auth, trip IDOR, public-projection leak, secret scanning, import boundaries | Security, privacy and architecture | cheap | **Keep blocking** |
| eval-replay, package-smoke, dogfood-persona-gate | Behavior and packaging | 2–3 min | Keep; strip date-dependent parts from manifest validation |
| Flag, API-policy, compatibility, schema-bridge and catalog **expiry** checks; design calibration and exemption freshness | Stale decisions (useful) | Make `main` red on a schedule; block pushes | **Report-only**: one weekly "governance debt" job that updates a single issue |
| Frontend governance: 30 budgets (size, home-surface, typography ×5, color, shadow, radius, containment, spacing, spinner, muteSoft, sheet ×2, local-button, motion, a11y, release-config, components, public imports, text clamp, date parse, itinerary legacy/deletion) | Design drift | Frequent PR failures; `home-surface-budgets` kept `main` red in August | **Nightly/advisory**, except `release-config`, `date-parse-guard` and accessibility |
| Visual evidence contracts, QA tooling contracts, Maestro flow validation | Self-tests of QA tooling | ~1 min each; unrelated PRs fail | **Path-filtered**: run only when `scripts/polish-qa`, `.maestro` or the design-alignment tooling change |
| Documentation gates (spine, canon, release, status, links, inventory, new-doc governance, child-doc governance) | Documentation hygiene | Pre-push and CI friction; the committed generated docs (`docs/status/current-state.md`, `docs/release/v1-scope.md`) must be regenerated whenever flags change | **Advisory**, except a living-links check in the weekly report |

### 2.4 Governance and documentation load (observed)

- **Workspace:** 729 tracked Markdown files, about 289K lines.
  - `docs/working` holds 361 files and about 228K lines.
  - 396 docs carry `status: active`. Of those, **152 are already past their `expires`**, **186 expire within 14 days**, 23 expire later and 35 have no expiry.
  - 224 files have no front matter (grandfathered).
  - `docs/governance/inventory.yaml` is 1,527 lines (91 glob rules and 291 per-file overrides).
- **Children:** backend about 80K lines of Markdown under `docs/` (5,794 files under `content/staging`); app about 60K lines.
- **Roadmap churn:**
  - The program roadmap reached 5,947 lines and the integration roadmap 7,976 lines before being archived on 09-25/26.
  - The replacement roadmap is 217 lines (good). But the new H1 execution plan (`home-value-composition-execution-plan-2026-09-25.md`) grew to 859 lines within about a day.
  - `docs/working/historical-branch-recovery-audit-2026-09-23.md` is 2,897 lines.
- The 30-day working-doc expiry rule (`scripts/check_doc_governance.py:219-230`) guarantees a steady stream of expired "active" docs. Nothing retires them automatically.

---

## 3. Environments and release path

### 3.1 Backend on Fly

Configuration (`travel-agent/fly.toml`):

- App `vesper-backend`, region `iad`. There is no staging app; only one `fly.toml` exists.
- Process groups:
  - `app`: uvicorn, shared 2 CPU / 2 GB, `min_machines_running=1`, auto-stop **off**.
  - `worker`: arq, 1 CPU / 2 GB.
  - `voice`: LiveKit, 2 CPU / 4 GB, scaled to 0 until the voice secrets exist.
- `release_command = "alembic upgrade head"`.
- External services: Qdrant Cloud, Postgres (Fly or Neon/Supabase) and Upstash Redis.

Selected environment settings:

- `LANGFUSE_ENABLED=true` with user content off.
- OpenAI `text-embedding-3-small`/768.
- `REQUIRE_DISTRIBUTED_TURN_LEASE=true`.
- `DISABLE_LLM_BACKGROUND_LOOPS="false"`.
- `ATLAS_LLM_ENABLED=true`.
- `CONTEXT_COMPILER_SHADOW_ENABLED` at 5%.
- `NOTIFICATION_*` calibration values.
- `BOOKING_EXECUTION_RETIRED` is **absent**.

Observed live state:

- `/health`, `/ready` (Postgres ok, Qdrant ok) and `/privacy` return 200.
- The runtime `git_sha` is `4a7f3e6f0` (2026-08-14 "ops(demo): reconcile Rome second occasion runtime").
- `/health/background-tasks` is **unauthenticated** and reports 29 of 30 loops running. Only `atlas_candidate_backfill` is disabled.
- `cache_invalidation` shows running, which implies `REDIS_URL` is set.

The pending deploy:

- It carries 1,673 commits and **77 migrations** (`git diff --diff-filter=A 4a7f3e6f0 origin/main -- alembic/versions`). This includes the forward-only notification revisions described in `docs/reliability/CI Plan.md`.
- `make deploy` refuses a dirty tree, runs `scripts/check_fly_deploy_config.py`, then `fly deploy --strategy bluegreen`.
- No rehearsal against a copy of production data is scripted.
- **Risk (inferred):** a failed `release_command` aborts the deploy safely. But a migration that succeeds and then misbehaves on real rows has no staging environment to catch it.

### 3.2 Expo/EAS profiles and what the founder can install

| Profile | Distribution | Backend | Notable flags | Current use |
|---|---|---|---|---|
| `e2e-test` | simulator, no credentials | mock | skip auth; 4 dogfood flags | Maestro/CI |
| `development` | dev client, simulator | mock | skip auth | Local; the installed dev clients are stale (see below) |
| `dogfood` | internal (ad hoc), device | Fly | Clerk `pk_test`; 10 legacy dogfood flags; voice on; **crash consent false** | **The only profile ever installed on a device.** Last build 2026-08-04; OTA about a month ago |
| `m1-dogfood` | extends dogfood | Fly | Narrower M1 flag set | Never built (not in the last 50 builds) |
| `billing-sandbox` | extends dogfood | Fly | RevenueCat test store | Never built |
| `preview` | internal | Fly | Everything off | Last built 2026-08-01 (4 finished, 4 errored) |
| `production` | store | Fly | **No Clerk key**, crash consent false | **Never built** |

Last 50 EAS builds (2026-05-23 to 2026-08-04): 39 dogfood (34 finished, 5 errored), 9 preview and 2 development.

**The current product is invisible on every profile.**

- `resolveProductSystemRollout` enables the governed four-root rehearsal only when the internal build has all four `EXPO_PUBLIC_*` root flags (`utils/productSystemRollout.ts:36-59`).
- No profile sets them, so the founder's installed dogfood build shows the legacy roots.
- `releaseEligible: false` is hard-coded (`:67-69`). No store build can show the four-root product without a code change.
- Every current-direction flag is labelled "development or explicit internal builds only" in the registry.

**OTA is unsafe until a new native build exists.**

- `app.json` uses `runtimeVersion: {policy: "appVersion"}` with `version: "1.0.0"`, unchanged since the August build.
- Native dependencies have changed since `605988afa`:
  - `react-native-worklets` 0.11.3 → 0.12.1;
  - `react-native-reanimated` 4.5.3 → 4.6.0;
  - `react-native-purchases` 10.6.0 → 10.7.1;
  - `expo-updates` ~55.0.26 → ~55.0.30;
  - `package.json` diff +88/−56.
- An `eas update --channel dogfood` today would target the August binary with a mismatched native layer. The recovery lane already hit exactly this on a simulator dev client: "Worklets native 0.11.3 versus JS 0.12.1" (workspace commit `827aace`).

**Local native builds are blocked.**

- `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` exists in all three EAS environments (observed via `eas env:list`), so cloud builds are fine.
- It is **absent locally**: not in the shell, `travel-app/.env` or `.env.local`.
- `827aace` records that a matching dev build "was not attempted because the local Mapbox download token … is unset". Today's lane nevertheless recorded simulator "native acceptance", apparently from an existing prebuild (`travel-app/ios` exists in that lane). How reproducible that is remains unverified.

**Security note.**

- `EXPO_PUBLIC_ADMIN_API_TOKEN` is defined in the EAS `preview` environment and in `travel-app/.env`, and is read by `utils/api/opsStatus.ts:24`.
- Every `EXPO_PUBLIC_*` value is inlined into the JavaScript bundle. Any internal build that picks up the `preview` environment therefore carries the backend admin token in extractable form.
- `internal` distribution resolves to the `preview` environment unless configured otherwise (inferred from EAS defaults, since the profiles set no `environment`).

### 3.3 TestFlight blockers (`docs/Owner Action Items.md`, last fully verified 2026-08-09; CI rows refreshed 09-24)

| # | Blocker | Who | Status |
|---|---|---|---|
| 0 | Green CI and protected-main landing | founder + agent | Now: the workspace PAT and date checks (§1.4, §2.2) |
| 3 | App Store Connect app record (`com.fyan.vesper`) plus `INVITE_IOS_APP_STORE_ID`/URL on Fly | founder | ❓ unconfirmed |
| 4 | APNs key uploaded to Expo; `EXPO_PUSH_ENABLED=true` on Fly (default false) | founder | ❓ |
| 5 | Rotate Anthropic and Tavily keys; set an Anthropic monthly spend cap | founder | ❓ |
| 6 | Clerk review phone/OTP | founder | ❓ |
| 7 | Production EAS build. `production` has **no Clerk key**. Either point the first build at the dev tenant (`pk_test`, acceptable for a dogfood cohort) or create a `pk_live` tenant | founder | 🔴 never built |
| 8 | J04/J05/J10 two-device certification | founder + agent | 🔴 0/3. `docs/journeys/evidence-attestations.json` holds only 3 promoted receipts, all `contract` layer from 2026-08-13; **zero device receipts** |
| 9 | Submit to TestFlight | founder | 🔴 |

Not blocking: custom domain, SendGrid, Twilio and Android. The AASA file is already served from the Fly host.

### 3.4 Secrets: have, missing, unknown

| Secret | Where needed | Status |
|---|---|---|
| `TRAVEL_WORKSPACE_CI_TOKEN` | workspace GitHub | **present but invalid** (observed failure) → replace |
| `TRAVEL_WORKSPACE_DISPATCH_TOKEN` | backend and app GitHub | present (2026-05-11); likely the same expiry, unverified (dispatches last ran in May) |
| `ANTHROPIC_API_KEY` | backend GitHub (canaries, eval) | **missing** |
| `DATABASE_URL`/`POSTGRES_*`, `ADMIN_API_TOKEN`, `TRAVEL_AGENT_API_URL` | backend GitHub (`cron.yml`) | **missing**. Recommend disabling the crons rather than adding production DB credentials to CI |
| `MAESTRO_CLOUD_API_KEY`, `MAESTRO_CLOUD_PROJECT_ID`, `EXPO_TOKEN` | workspace GitHub | **missing** (optional; skip unless cloud device runs are wanted) |
| `RNMAPBOX_MAPS_DOWNLOAD_TOKEN` | EAS | present in production, preview and development |
| same | local shell / `~/.netrc` | **missing** (blocks local dev-client builds) |
| same | app GitHub (`mobile-stability-device`) | **missing** |
| `EXPO_PUBLIC_SENTRY_DSN` (+ `SENTRY_ORG`/`SENTRY_PROJECT`/`SENTRY_AUTH_TOKEN` for source maps) | EAS env | **missing**. All profiles set `SENTRY_DISABLE_AUTO_UPLOAD=true` and crash consent false |
| `SENTRY_DSN` | Fly | unknown. The backend is a no-op without it (`backend/core/error_reporting.py:39-41`) |
| `POSTHOG_API_KEY` | Fly | **unset** per Owner Action Items §6. Events are log-only (`backend/core/telemetry.py:284`) |
| `LANGFUSE_PUBLIC_KEY`/`LANGFUSE_SECRET_KEY` | Fly | unknown. Present in local `travel-agent/.env` (names only) |
| Clerk `pk_live` + JWKS/issuer | EAS production + Fly | not created (dev tenant `picked-firefly-95` in use) |
| APNs .p8, App Store Connect API key (for `eas submit`) | Expo/ASC | unconfirmed |
| `EXPO_PUSH_ENABLED=true`, `EXPO_ACCESS_TOKEN` | Fly | the token is reportedly set; the flag defaults false |
| `BOOKING_EXECUTION_RETIRED=true` | `fly.toml` `[env]` | **absent** (see §5) |

### 3.5 Telemetry today

**The founder cannot observe crashes, funnel events or cost spikes.**

- App crash reporting requires a DSN and user consent (`utils/observability.ts:84-96`). No profile provides either.
- Backend Sentry is unverified.
- PostHog is unset, so the activation funnel is dark.
- LLM cost anomalies from `audit_llm_anomalies` (`backend/workers/audio_jobs.py:366-375`) are logged as warnings to `fly logs` only.
- `/metrics/llm` accounting endpoints exist (`backend/api/routes/metrics.py:78-90`), but nothing alerts on them.

---

## 4. Development environment and agent workflow

### 4.1 Lane tooling

- **`scripts/new-worktree.sh <name>` → `worktree_lane.py create`:** creates `../travel-workspace--<name>` with workspace, backend and app worktrees on `codex/<name>` from each current HEAD. It writes `.workspace-lane.json` with an isolated Compose project, free Postgres/Qdrant/API/Expo ports and a device slot.
- **`scripts/land-worktree.sh <name>` → `worktree_lane.py land`:**
  - Requires a clean tree, the lane branch, and `origin/main` as an ancestor. It never rebases for you.
  - Runs the full `make verify` (~16 min) and refuses if the tree changes.
  - Optionally pushes the branches with `--publish`.
  - It opens no PRs, merges nothing and cleans up nothing.
- **Unpublished tooling:** `status`/`retire` subcommands and `make worktrees` exist only on the unpushed local `main` (`8a36fab`) and in the `home-value-delivery` lane. The baseline `origin/main` version supports only `create|land`. Root `AGENTS.md` in the canonical checkout already tells agents to use `retire`.
- `scripts/dev.sh` → `dev_runtime.py`: process supervision and lane runtime selection (`--print-runtime`).
- `scripts/session-context.py`: bounded orientation. It is wired as a Codex `SessionStart` hook (`.codex/hooks.json`, 4,000-character limit).

### 4.2 Current worktrees, branches and simulators (observed)

| Lane | Branch / HEAD | State | Device |
|---|---|---|---|
| canonical `/Users/feihuyan/travel-workspace` | workspace `main` +2/−57 vs origin, with 19 modified and 7 untracked design-gen files. Children `main` 41 and 43 commits behind origin | **stale and dirty** | — |
| `--home-value-delivery` (owner "Home value delivery implementation") | active; +30 workspace, +3 backend, +16 app commits vs origin/main; backend 2 dirty files, app 10 dirty | active H1 lane | iPhone 16 Pro (booted) |
| `--home-human-opening-recovery-2026-09-23` | merged via #36/#233/#201 | retire | reserved |
| `--functional-implementation-…--native-presentation-wave1-2026-09-21` | detached; commits already in `origin/main` | **retire** | "Vesper Presentation 0921" **still booted** |
| `--product-map-inventory` | this read-only inventory | — | iPhone 16 (booted) |
| `--receiving-completion-2026-09-12`, `…--cw4-home-native-2026-09-12` | not Git worktrees: leftover 32 KB/4 KB directories | delete | — |

Three simulators are booted concurrently. Each lane's manifest records an exclusive UDID, which is good: it isolates devices.

### 4.3 QA tooling

- **Maestro:** 392 YAML flows under `travel-app/.maestro`, plus configs for pr, nightly, stability, polish, live, baseline and android.
- **Polish QA:** verdict schemas, agent-judged goldens and a design-alignment status pipeline (`scripts/polish-qa`, `scripts/design-alignment`).
- **Coverage vs execution:** `docs/journeys/STATUS.md` records all 28 journey flows as *defined* and none as device-executed.
- **Cloud and CI device runs are not running:**
  - Maestro Cloud is unconfigured.
  - The macOS smoke fails at checkout.
  - `mobile-stability-device` lacks secrets.
  - The only device evidence therefore comes from agents driving local simulators.

### 4.4 Agent instruction load

**Instruction files:**

- `AGENTS.md`: workspace 115 lines / 841 words; backend 112 / 856; app 159 / 1,083.
- `CLAUDE.md` files are 7–8 line adapters.

**`.claude` configuration:**

- Workspace:
  - 3 workflows (privacy tracer, privacy triage, design-alignment loop; about 955 lines of JS);
  - the `mvp-invariants` skill;
  - 2 commands;
  - the `cross-repo` rule.
- Backend:
  - 9 commands, 8 rules and 3 agents;
  - hooks: ruff format after edits, `.env` read guard, and a stop reminder to run `make ci`/`make verify`.
- App:
  - 2 agents;
  - `design-system.md` rule (346 lines / 2.5K words);
  - hooks: ESLint `--fix` after edits, a block on editing `schema.gen.ts`, and a design-alignment write guard.

**Codex configuration:** `max_concurrent_threads_per_session = 3`, and 3 `world-*` agents in `travel-agent/.codex`.

**Required reading before an app change** is about 21.6K words (about 28K tokens):

- Product Thesis 1.6K words
- Product Model 3.6K words
- What We Believe 2.1K words
- `contribution-and-consequence.md` 5.0K words
- four-root contract 4.3K words
- Task Intake 0.8K words
- design-system rule 2.5K words
- plus the active execution plan (859 lines)

This load is tolerable. The larger cost is the practice of re-reading and re-writing the long working ledgers.

### 4.5 Commit mix, last 7 and 14 days (observed)

Classification:

- **docs:** `*.md`, `docs/`, `design/` or receipts;
- **test:** test paths;
- **tooling/config:** `.github/`, `scripts/`, `tools/`, yaml/json/toml/lock;
- **code:** everything else.

Counts cover all refs, excluding merge commits.

| Repo | Window | Commits | Docs-only | Touch product code | Tests/tooling only | Churn by class (lines) |
|---|---|---|---|---|---|---|
| workspace | 7 days | 429 | **420 (98%)** | 1 | 6 | docs 218,768; tooling 1,008; tests 536 |
| workspace | 14 days | 544 | 535 | 1 | 6 | docs 229,370 |
| backend | 7 days | 195 | 19 | **117 (60%)** | 44 (+15 config) | code 12,214; tests 15,344; config 5,526; docs 4,609 |
| backend | 14 days | 418 | 27 | 292 | 82 | code 46,130; tests 64,102 |
| app | 7 days | 212 | 8 | **141 (67%)** | 47 (+16 config) | code 24,215; tests 14,872; config 6,901; docs 1,251 |
| app | 14 days | 340 | 20 | 241 | 55 | code 40,997; tests 27,383 |

**Where the workspace doc churn lands:**

- Of workspace churn on `origin/main` over 7 days: `docs/design-archive` 82.2K lines (design snapshots), `docs/working/*.md` **36.8K lines** (plans and receipts), and `docs/working/design-gen` 24.7K lines.
- The receipt share alone (36.8K) matches all product-code churn in both children (36.4K).

**Today's lane (`codex/home-value-delivery`, 2026-09-26):**

- 28 workspace commits titled "Record…", "docs(home): record…", "Rebaseline…" or "Clarify…", about one every 15–20 minutes, against 16 app and 3 backend commits.
- They produced 15,272 insertions and 13,902 deletions across 16 workspace files, mostly roadmap archive moves and the growing H1 plan.

### 4.6 Lane start to landing (observed)

| PR | Lane | Commits | First commit → merge | PR open → merge |
|---|---|---|---|---|
| workspace #36 / backend #233 / app #201 | home-human-opening-recovery | 61 / 40 / 42 | **59.4 h** | 49.4 h (5 CI attempts per child; the workspace check never passed) |
| backend #229 / app #199 | consolidation-2026-09-22 | 375 / 220 (merge-parent count) | **363.8 h / 370.6 h (≈15 days)** | 0.1 h (merged 6 minutes after opening) |
| workspace #31 | consolidation | 100+ | 33.5 h | 0.1 h |
| August PRs (#195–#216) | various | 1–70 | 0–15 h | 0–14 h |

The pattern is long-lived multi-repo lanes with no intermediate landing, followed by bulk consolidation and then a recovery lane to re-establish a candidate. The 09-25 roadmap rightly makes landing an owner responsibility, but sets no cadence.

---

## 5. Cost and operations

### 5.1 Configured LLM posture

- **Models:** `claude-haiku-4-5-20251001` for about 35 roles and `claude-sonnet-4-6` for conversation, research synthesis, planning enrichment, proactive turns and post-trip work (`backend/core/model_registry.py:140-208, 257-260`). Any role can be overridden with `MODEL_<ROLE>` (`:219-231`).
- **`AI_MODE`:**
  - Unset means `live` (`backend/core/ai_mode.py`).
  - A set-but-invalid value fails closed to `off`.
  - `cheap` mode allows 3 surfaces with a budget of 2 calls per context.
  - `DISABLED_SURFACES` is a per-surface kill switch (`backend/core/llm.py:329-333`). That is the fastest lever available today.
- **Spend controls:** there is no daily or monthly cap in code. `llm_accounting` records per-call cost and flags anomalies to logs only. The Anthropic console cap is a founder item that has not been confirmed (Owner Action Items §2).
- **Fly footprint (config):**
  - 1 always-on API machine (auto-stop off);
  - 1 worker;
  - 0 voice machines;
  - plus Postgres, Qdrant Cloud and Upstash, which are external.
  - Machine counts could not be verified without Fly authentication.
- **GitHub Actions:** billing already stopped CI once. Child runs cost about 34–38 Linux job-minutes each. The daily macOS smoke is cheap only because it fails in under a minute; macOS minutes bill at 10×.

### 5.2 Background work: production cost and safety risks

These come from the two inventories at `c8c9f5785`. I re-checked `booking_retirement.py:57-60`, `saved_place_watch.py:138-143`, `lifecycle.py:1073`, `group_interjection.py:142`/`planning_autopilot.py:43` and the missing `trip_candidate_backfill.py`. Production runs `4a7f3e6f0` and currently shows the same 30 loop names. Each risk below applies to `main` and ships with the next deploy; most probably apply to production already (inferred).

| # | Risk | Evidence (file:line under `travel-agent/`) | Severity |
|---|---|---|---|
| C1 | **The kill switch misses most paid paths.** `DISABLE_LLM_BACKGROUND_LOOPS` only prevents 6 loops from starting (pre_trip, brief_regen, daily_reflection, proactive, digest, story_backfill; `backend/api/lifecycle.py:420-433, 536-548`). The scheduled-task loop excludes only `farout_read_pool` (`lifecycle.py:1073`). Only 4 subscriber modules check `background_llm_enabled()`. Still spending with the switch set (list below) | see list | **Cost; cannot stop spend quickly** |
| C2 | **Uncapped fan-out** (list below) | see list | Cost/abuse |
| C3 | **Retired booking execution is still reachable in production.** `BOOKING_EXECUTION_RETIRED` defaults to admitted and is absent from `fly.toml` (`backend/core/booking_retirement.py:57-60`). Reachable paths are listed below | see list | **Safety (external calls and payments on a retired product)** |
| C4 | **`saved_place_reopen_scan` is a self-perpetuating paid chain with no flag.** It reschedules itself forever (`backend/places/saved_place_watch.py:138-143`). Up to 20 paid Google Places/Foursquare refreshes per user per day. It is seeded by an operator script (`scripts/schedule_saved_place_reopen_scans.py:47`) | as stated | Cost that grows with every seeded user |
| C5 | **The proactive path is hard-enabled and re-triages.** Group interjection and planning autopilot are hardcoded `enabled: bool = True` (`backend/notifications/group_interjection.py:142`, `backend/concierge/planning_autopilot.py:43`). A WAIT verdict is not stamped, so the conversation is re-triaged with Haiku. The triage LLM picks its own next run with a 1-minute floor (`lifecycle.py:1835-1836`). Each dispatch runs a **Sonnet** concierge turn (`notifications/arbiter.py:366`; `concierge/model_routing.py:246-247`) | as stated | Cost, and noise in group threads |
| C6 | **Guide prerender re-spends when TTS is missing.** Haiku narration runs before Cartesia TTS, and failed rows are re-claimed on every trigger (`backend/guide/prerender.py:129, 260-271`). The Cartesia key is not set ("set when accounts are ready", `fly.toml` header) | as stated | Pure waste |
| C7 | **No spend visibility:** anomalies only logged (`backend/workers/audio_jobs.py:366-375`), PostHog unset, Sentry unverified, no Anthropic cap confirmed | §3.5 | Blind to spikes |
| C8 | `/health/background-tasks` is unauthenticated and enumerates internal loop names (observed live) | live probe | Minor information disclosure |

**C1: paths that keep spending with the kill switch set:**

- Takes: Haiku Curator regeneration on `trip.completed`, `brief.finalized`, `dossier.persisted` and `itinerary.committed` (`backend/core/takes/subscribers.py:217-248, 281-288`).
- Guide narration prerender: Haiku plus TTS for each member × stop (`backend/guide/subscribers.py:197-198`).
- Research:
  - `warm_experience_brief`;
  - `seed_city_full`, up to 1,500 LLM calls per city and 10 cities per day by default (`backend/research_agent/subscribers.py:320-321`; `backend/workers/research_jobs.py:363, 370`).
- `trip_reading_generate`: Sonnet, one new row per itinerary commit (`backend/home/trip_reading/subscriber.py:74, 90, 115-116`).
- Transport nudges: Sonnet turns posted to the **group** (`backend/concierge/transport_subscribers.py:182, 323, 351-367`).
- Invite-intake memory refresh: Haiku (`backend/notifications/invite_delivery_tasks.py:130`).
- `session_dispatcher` Haiku offer ranking.
- `experience_embed` OpenAI embeddings.
- The worker's hourly pre-trip cron (`backend/workers/audio_jobs.py:703-707`).

**Related:** subscribers are registered at `lifecycle.py:325-327`, before the `DISABLE_API_BACKGROUND_TASKS` early return (`:404`). Even that flag only stops the claim loop.

**C2: uncapped fan-out:**

- Curator Take for every venue on `trip.completed` (`takes/subscribers.py:236-248`).
- Cross-trip threads: one `create_task` per member × upcoming trip, with no semaphore (`backend/core/personalization/cross_trip_thread_subscriber.py:84-88`).
- Guide: members × stops with no count cap (`guide/prerender.py:44-50`).
- `session_dispatcher` adds up to 5 in-process booking graphs per 5-second tick, with no cap on in-flight graphs (`backend/booking_agent/tasks/session_dispatcher.py:28-29, 158-162`).
- `daily_reflection` runs 50 users concurrently with no semaphore (`backend/concierge/reflection.py:535-559`). Its "skip if the last run was under an hour ago" rule can never fire at a 4-hour cadence (`:273-289`). Active users are likely reflected up to 6 times a day (inferred).

**C3: booking paths still reachable:**

- Bland.ai restaurant calls (`backend/booking_agent/tasks/restaurant_dispatch.py:293, 357`).
- Provider checkout (`backend/booking_agent/tasks/provider_checkout.py:668`).
- `checkout_reconciliation` has **no retirement gate**. It polls providers every 60 seconds and builds unclosed clients on each tick (`backend/booking_agent/tasks/checkout_reconciliation.py:33-34, 43, 65, 128`).
- Duffel payment stays dark only because `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` defaults false (`backend/booking_agent/config/settings.py:24`).

### 5.3 Cleanup items (not urgent; no production spend or safety impact at current defaults)

- **Advisory-lock key collisions:**
  - `7_831_209_453` is used by anniversary (`lifecycle.py:711`) and stale_claims (`:1168`).
  - `7_831_209_454` is used by unpacked_seasonal (`:814`) and experience_embed (`:1477`).
  - Impact is limited while `ANNIVERSARY_PUSH_ENABLED` and `UNPACKED_SEASONAL_PUSH_ENABLED` stay false. If enabled, a lock miss pushes the loop into a 1-hour retry.
- **Dead import:** `backend/atlas/trip_candidate_backfill.py` does not exist, and the import at `lifecycle.py:924` is dead (`atlas_auto_candidate_enabled()` is hardcoded False, `backend/core/feature_flags.py:505-512`).
- **`pre_trip`** does nothing without `REDIS_URL` but still logs a count (`backend/workers/pre_trip_jobs.py:27-40`; `backend/core/job_queue.py:160`).
- **`cache_invalidation`** without Redis returns cleanly, and the supervisor reports it as "done" (`backend/core/cache_invalidation.py:147-155`; `backend/core/background_tasks.py:236-244`).
- **`validate_worker_registry`** checks registered names only, not liveness (`backend/api/background_runtime.py:36-47`). The supervisor restarts forever with no cap.
- **`digest`:**
  - Its query uses `LIMIT` without `ORDER BY` or a status filter, and runs synchronous DB calls on the event loop (`backend/digest/engine/daily.py:267-280`).
  - It sends no push or email, so its Haiku spend feeds only in-app surfaces.
- **Duplicate registration:** `itinerary_provider_dispatch` is registered twice, and hook order decides which handler wins (`backend/core/event_subscribers.py:56-57`). There is also a dormant duplicate `occasion_reconcile` registrar (`backend/core/db/occurrence_reconciliation.py:784`).
- **No-op or dark registrations:**
  - `ambient_cycle` is registered but never scheduled.
  - `transport_nudge_group_split` writes a row and never acts.
  - `backend/booking_agent/subscribers.py` is a no-op.
- **Stale feature status:** `backend/discover/FEATURE.md` still says "active".

---

## 6. Recommendations, ranked by impact on speed to ship

Owner key:

- **F**: founder only (console access, authority).
- **A**: an agent can do it.
- **F+A**: an agent prepares it and the founder executes the single privileged step.

### Tier 0: this week; each item takes under a day

**R1. Put the current product on the founder's phone, against a current backend (F+A, about 1 day). This is the single biggest unblocker.**

1. **Rehearse the 77 migrations on a copy of production** (A prepares, F runs with Fly access):
   - fork or snapshot the production Postgres (for example `fly postgres fork`, or `pg_dump` → local disposable DB);
   - run `alembic upgrade head` and the `test-db-migrate` checks against it;
   - smoke-test `/ready`.
2. **Deploy backend `main`** with `make deploy` (F).
   - In the same change, add `BOOKING_EXECUTION_RETIRED = "true"` to `fly.toml` `[env]` (A; closes C3).
   - Verify `/ready` `git_sha` equals the merged SHA.
3. **Bump the app `version` to `1.1.0`** (A), or switch `runtimeVersion` to `{"policy": "fingerprint"}`. Old binaries can then never receive an incompatible OTA.
4. **Add a `founder` profile** to `travel-app/eas.json` (A). The variable names are verified against `utils/productSystemRollout.ts`, `utils/lifeRefindFlag.ts`, `constants/featureFlags.ts` and `app/_layout.tsx:464`:

   ```json
   "founder": {
     "extends": "dogfood",
     "environment": "preview",
     "env": {
       "EXPO_PUBLIC_APP_CHANNEL": "founder",
       "EXPO_PUBLIC_IS_INTERNAL_BUILD": "true",
       "EXPO_PUBLIC_FOUR_ROOT_SHELL": "true",
       "EXPO_PUBLIC_ROOT_PROJECTION_V2": "true",
       "EXPO_PUBLIC_PLACES_ROOT_V2_RENDERER": "true",
       "EXPO_PUBLIC_LIFE_ROOT_V1": "true",
       "EXPO_PUBLIC_LIFE_REFIND_LANE": "true",
       "EXPO_PUBLIC_OBJECT_PAGE_REBUILD_ENABLED": "true",
       "EXPO_PUBLIC_CRASH_REPORTING_CONSENT": "true",
       "SENTRY_DISABLE_AUTO_UPLOAD": "false"
     },
     "channel": "founder"
   }
   ```

   - Put `EXPO_PUBLIC_SENTRY_DSN` in the EAS environment, not in `eas.json`.
   - Remove `EXPO_PUBLIC_ADMIN_API_TOKEN` from the EAS `preview` environment and rotate the backend `ADMIN_API_TOKEN`. That token was baked into internal bundles.
   - Legacy dogfood flags inherited from `dogfood` stay as they are unless H1 says otherwise.
5. **Build once** with `eas build -p ios --profile founder` (F; the Mapbox token is already in EAS). **Then ship JavaScript daily** with `eas update --channel founder` (A can run it with `EXPO_TOKEN`). Rebuild only when the fingerprint changes.
6. **Set the H1 backend flags on Fly.** Production is effectively the founder's dogfood environment: there is no external cohort yet (Owner Action Items §2, "Cohort recruitment … OPEN"). Set the backend flags the H1 package needs directly in `fly.toml`, for example root delivery projection, place-content primitive reads and lived-experience exposure where H1 requires them.
7. **Optional, same day:** add a `testflight-internal` profile with store distribution, `EXPO_PUBLIC_IS_INTERNAL_BUILD=true`, the same flags and `channel: testflight`. It needs the App Store Connect record (Owner #3). TestFlight avoids UDID provisioning, and it is the path the first 10 testers need anyway. Store builds can carry `IS_INTERNAL_BUILD=true`: `releaseEligible:false` only prevents *public* release claims.

**R2. Make `main` green today (F: 10 minutes; A: about half a day).**

- **F:** replace `TRAVEL_WORKSPACE_CI_TOKEN` with a fine-grained PAT or GitHub App token scoped to `contents:read` on both children, with a 1-year expiry and a calendar reminder. Check `TRAVEL_WORKSPACE_DISPATCH_TOKEN` at the same time.
- **A:** move `vesper-world-catalogs` out of `make -C travel-agent ci` and the CI `test` job into a weekly report. Until then, stop ordering it before tests.
- **A:** make `design:status` a CI-generated artifact, or regenerate it in the app pre-push hook, so merges cannot leave it stale.
- **A:** remove the `schedule:` triggers from:
  - backend `cron.yml` (0/64);
  - `ai-live-canary.yml` and `ai-redteam-canary.yml`, until a capped key is added;
  - workspace `visual-qa.yml`, until the token is fixed and someone actually reads the result.
- **F:** confirm the GitHub billing spending limit on the account that owns the private children. Billing already killed CI for about 3 months.

**R3. Right-size branch protection for a solo founder (F, 10 minutes).**

- Set required approvals to **0** in all three repos, and drop "require approval of the most recent push". If you want review, request an agent `/code-review` or the second collaborator as advisory. Every recent merge already bypassed the rule.
- Keep `enforce_admins` on, so checks still apply to the founder. Set `strict: false`: rebuild-on-rebase adds 15 minutes per landing.
- Required checks become the core set only:
  - **backend:** `lint`, `typecheck`, `test`, `test-db`, `test-db-migrate`, `import-boundaries`;
  - **app:** `Lint`, `Type check`, `Test`, `API types freshness`;
  - **workspace:** `Contract and golden paths`, once it contains only contract checks (see R4).
- Enable auto-merge and delete-branch-on-merge, so agents can `gh pr merge --auto` and walk away.
- Decide deliberately whether `travel-workspace` should stay **public**. It holds the full product strategy, the API snapshot, the design archive and receipts.

**R4. Turn the calendar gates into reports (A, about 1 day).**

Every date-based failure should stop being able to fail `main`. Specifically:

| Gate | Change |
|---|---|
| `check_flag_registry.py` | Warn and exit 0 on overdue flags. Remove the pre-push hook stage from workspace `.pre-commit-config.yaml:37-42` |
| `api_contract_audit.py` expired-policy | Report-only. Keep consumer-coverage and method checks blocking |
| `check_compatibility_ledger.py` expiry | Report-only |
| schema-bridge `unmodeled_wire` expiry | Report-only |
| `check_vesper_world_catalogs.py` | Weekly job; failure opens an issue |
| design gate calibration (>14 days) and exemption `until` | Warning |
| `flaky_order_baseline` review date | Report |

Then add one scheduled workflow, `governance-debt.yml` (weekly), that runs them all and updates a single pinned GitHub issue. Renew the 55 API operations and 36 flags **once, in bulk**, with a single long date (for example 2026-12-31). Do not do it item by item with research notes.

### Tier 1: next 1–2 weeks

**R5. Trunk-based cadence rules** (add to root `AGENTS.md` under "Git and runtime ownership"; A drafts, F approves):

- At most **one implementation lane**, plus one optional independent lane, as the 09-25 roadmap already states.
- **Land to `main` at least once per working day**, or once every 20 commits, behind flags. Every surface in flight is already dark by default: 87 default-off flags. Unfinished work is safe to merge.
- **No lane lives longer than 3 days** without landing. A lane older than that is split or abandoned, never consolidated in bulk.
- Retire a lane the same day it merges: remove the worktree, shut down its simulator and delete its branch. Retire the two merged lanes and the two leftover directories now (§4.2). Push or drop the two local canonical `main` commits and fast-forward the children's `main`.
- Cross-repo pins (`docs/child-repos.ci-lock.json`, `travel-app/.github/ci-lock.json`): for PRs, check out sibling `main` (or the same-named branch if it exists). Keep pins only for release-certification tuples, and bump them with a script.

**R6. Receipts diet (A; F approves the rule).**

- Evidence goes in the **PR description**, in CI artifacts (logs and screenshots), or in one `gh pr comment` per checkpoint. It does not go in workspace commits.
- A lane may add **at most one documentation commit per landed package**, plus contract or doc changes the code actually requires.
- Working plans have a hard cap, for example ≤300 lines, enforced by the existing `docs-canon-check` word-budget mechanism. When a plan exceeds it, move history to the archive at landing, not mid-lane.
- Stop adding `expires` to every working doc (the 30-day rule creates about 180 new expiries a fortnight), or let a script archive expired working docs automatically.
- Measure it: the ratio of docs-only commits to code commits per lane. Today it is about 28:19. The target is ≤1:5.

**R7. A fast inner loop (A).**

- Add `make verify-fast`, targeting under 3 minutes: ruff on changed Python files, tsc, `jest --findRelatedTests` on changed TS files, `pytest` on changed test modules, and `contract-check` only when backend models or routes changed.
- Promote `verify-changed` once `scripts/measure_verification.py` shows it catches what matters.
- Keep full `make verify` (about 16 minutes) for `land`, and let CI cover the rest.
- Add `paths-ignore: ['**/*.md', 'docs/**']` to child CI for PRs. Use a docs-only no-op job with the same required names, so required checks still report.
- Move the 30 frontend governance budgets, Visual evidence contracts and QA tooling contracts to `pull_request` with path filters, and add a nightly run.

**R8. Cost safety before more dogfood traffic (F+A, half a day).**

- **F:**
  - set the Anthropic monthly spend cap;
  - set `POSTHOG_API_KEY`, `SENTRY_DSN` and `EXPO_PUSH_ENABLED=true` on Fly;
  - upload the APNs key to Expo.
- **A (stop-gap):** set `DISABLED_SURFACES` on Fly for surfaces H1 does not need:
  - guide narration (no Cartesia key; C6);
  - research `seed_city_full` and warm;
  - transport nudges;
  - trip reading, unless H1 needs it.
- **A (code):**
  - route `audit_llm_anomalies` to Sentry;
  - make `background_llm_enabled()` a check inside `call_llm` for every background surface, so the kill switch is real (C1);
  - cap the Takes, cross-trip and guide fan-out (C2);
  - put a flag on `saved_place_reopen_scan` (C4);
  - make the interjection and autopilot enable flags environment-driven and stamp WAIT verdicts (C5);
  - require admin auth on `/health/background-tasks` (C8).
- **A:** fix the cleanup items in §5.3 opportunistically. The lock-key collisions must be fixed before anyone enables the anniversary or unpacked pushes.

**R9. Dependabot policy (A).** Keep security updates. Make native React Native and Expo version updates monthly and grouped, or ignore them for `react-native`, `react-native-*` native modules and `expo*` until after TestFlight. Every native bump forces a new binary and breaks OTA compatibility.

**R10. Local native builds (F, 5 minutes).** Put the Mapbox secret download token in `~/.netrc` (`machine api.mapbox.com login mapbox password sk…`) or the shell profile. Rebuild the simulator dev clients once, so agents' simulator evidence matches current native modules.

### Tier 2: after the first founder build is running

**R11. Close the TestFlight path.** Work the Owner Action Items in order:

1. App Store Connect record;
2. APNs;
3. key rotation;
4. Clerk review number;
5. the `testflight-internal` build;
6. J04/J05/J10 on two devices;
7. submit.

Use the `pk_test` Clerk tenant for the cohort, as the Owner doc already allows.

**R12. Add a staging database (optional).** A `fly postgres fork` refreshed nightly is enough for migration rehearsal. A separate staging app is not needed for a solo founder while production *is* dogfood.

**R13. Stop committing generated status documents** (`docs/status/current-state.md`, `docs/release/v1-scope.md`, design `STATUS`). Render them on demand in CI artifacts. Flipping a flag should never require regenerating three documents.

### Definition of done (propose adding to `mvp-invariants` and root `AGENTS.md`)

A user-visible change is **done** only when all of the following hold. Anything less is "merged" or "candidate".

1. **Merged to `main`** with the core required checks green, not sitting on a lane.
2. **The backend is deployed** if it changed: production `/ready` `git_sha` equals the merge SHA.
3. **It has reached the founder's device:**
   - through the `founder` OTA channel (record the update group ID), or
   - through a new `founder` or TestFlight build if native code changed (record the EAS build ID).
4. **It was exercised on the physical device against production:**
   - The flow is walked on the phone. The agent can pre-walk it on a simulator, which counts as `device_mock`.
   - One screenshot or screen recording is attached to the PR, **or** one line is appended to a single `DONE` log: date, build or update ID, backend SHA, flow, pass/fail and the founder's initials.
5. **Signals are clean:** the flow's PostHog event arrives, and Sentry shows no new error class for that build within 24 hours.
6. **No per-slice receipt document:** the PR and the one-line log are the receipt. The existing promotion pipeline (`docs/journeys/evidence-attestations.json`) remains for formal certification (for example J04/J05/J10), not for daily work.

---

## 7. Open questions and unverified items

- **Fly (needs `fly auth login`):** actual machine counts, VM sizes, secrets set (`SENTRY_DSN`, `POSTHOG_API_KEY`, `LANGFUSE_*`, `EXPO_PUSH_ENABLED`, `REDIS_URL`), and the Postgres provider.
- **Credentials:** whether `TRAVEL_WORKSPACE_DISPATCH_TOKEN` is also expired, and the exact reason `TRAVEL_WORKSPACE_CI_TOKEN` fails (expiry vs revoked access). Only the failure itself is observed.
- **Migrations:** whether the 77 migrations are safe on real production rows. This needs the rehearsal in R1.
- **Local simulator reproducibility:** how the `home-value-delivery` lane produced a current simulator binary without a local Mapbox token (for example a cached pod or prebuild). This matters for whether R10 is urgent.
- **Cost:** actual LLM spend. Run `GET /metrics/llm` or `ops_readout.py` with admin access, and check the Anthropic console.
- **Milestone ownership:** the Owner Action Items header still names M1 Plan Repair as the current milestone, while the 09-25 roadmap names H1 Home value delivery. The founder should state which one the TestFlight path serves. The recommendations above assume H1 on the `founder` profile, with TestFlight following.
