# Deploy & Rollback Runbook

**Scope:** how to ship, verify, and *undo* a release during dogfooding — backend (Fly), database migrations, the arq worker, the API contract, and the mobile app (EAS/TestFlight). Cross-repo: Travel Agent + Travel App.

This is the runbook the 2026-05-19 release/deploy audit found missing. Keep it next to `Pre-Launch Deploy Surface.md` (env/secret risk) and `Owner Action Items.md` (account/credential gates).

**Golden rule:** the schema rolls *forward*; the app rolls *back*. Migrations are additive (expand/contract — new columns are nullable or carry a `server_default`), so old app code ignores them. **Default rollback = redeploy the previous app image and leave the schema where it is.** Only downgrade the schema in the rare case a migration is itself the fault — and then read §5.3 first.

---

## 1. Pre-deploy gates (must be green)

| Surface | Gate | Command |
|---|---|---|
| Backend | CI `ci.yml` (lint, types, test, **test-db incl. migration up + downgrade round-trip**, eval-replay) | pushed to `main` → GitHub Actions |
| Contract | OpenAPI snapshot fresh + `schema.gen.ts` in sync | `make contract-check && make api-coverage-check` |
| Backend (local) | offline suite | `make test-backend` |
| Frontend | `tsc`, lint, jest, **API-types freshness** | Travel App `ci.yml` |
| Frontend build | full pre-flight (toolchain, eas.json, contract, tests) | `make preflight-eas` |

Do not deploy on a red gate. The `test-db` job now round-trips `alembic downgrade base && alembic upgrade head`, so a structurally-broken downgrade fails CI before it can bite a real rollback.

---

## 2. Backend deploy (Fly)

```bash
cd "Travel Agent"
fly deploy --build-arg GIT_SHA="$(git rev-parse HEAD)"
# builds an identifiable image, runs release_command, then swaps machines
```

What happens (see `fly.toml`):
1. Builds the image from `Dockerfile`.
2. **`release_command = "alembic upgrade head"`** runs in a one-off machine with secrets attached.
   - **If the migration fails, the deploy aborts and the old machines keep serving.** No rollback needed — production is untouched. Fix forward and re-deploy.
3. On migration success, Fly rolls machines: `app` (uvicorn) and `worker` (arq) process groups.
4. Verify the deployed SHA and AI configuration after rollout:
   - `GET /ready` exposes the content-free deployment identity.
   - Admin-authenticated `GET /debug/runtime` adds resolved model roles,
     prompt version, embedding provider, and output-guard mode.

Do not use a bare `fly deploy`: the application will deliberately report
`git_sha=unknown`, making dogfood screenshots and latency traces impossible to
join back to the source that produced them.

First-time deploy + secrets: `make fly-secrets` (emits the paste-ready template; `required` now includes Postgres/Qdrant/Redis). See the `fly.toml` header for the full first-deploy sequence.

---

## 3. Frontend deploy (EAS / TestFlight)

### How EAS Build works (plain English)

Every iOS app has to be compiled into a native binary by Xcode on a Mac. EAS Build rents you a Mac in the cloud so you don't have to run that locally. You push your source code to Expo's servers, they compile it, and hand you a `.ipa` file you can install on a phone.

```
You change code  →  eas build  →  Expo compiles on a cloud Mac  →  install link / TestFlight
```

**What requires a full rebuild vs. not:**
- **Full rebuild required:** adding a new native library, changing permissions, changing the bundle ID or app icon, bumping the SDK version.
- **No rebuild needed (OTA via `eas update`):** any JavaScript/TypeScript change — screens, components, API calls, copy. `eas update` ships a new JS bundle and users get it on next app launch. *We don't have `expo-updates` wired in yet, so this doesn't apply yet — every change currently needs a rebuild.*

### Build profiles

| Profile | Who installs | Auth | Backend | Use for |
|---|---|---|---|---|
| `development` | Simulator only | SKIP_AUTH=true | mock data | Local dev, no phone needed |
| `dogfood` | Your phone (ad-hoc) | SKIP_AUTH=true | vesper-backend.fly.dev | Personal testing on device |
| `preview` | Internal testers (ad-hoc) | Clerk required | vesper-backend.fly.dev | Sharing with early testers |
| `production` | App Store / TestFlight | Clerk required | travelagent.app | Public release |

### Dogfood build (internal, on your phone)

```bash
cd "Travel App"
eas build --platform ios --profile dogfood
# EAS prints an install link when done — open it on your iPhone
# or it emails you; build takes ~15 min in the free queue
```

- Installs directly on your phone via an ad-hoc provisioning profile (no App Store).
- Registered device: your iPhone UDID `00008140-001210CE2013C01C` is in the provisioning profile.
- Adding a new test device: run `eas device:create` → select "Website" → open the URL on the new phone → re-run the build.
- Credentials live on Expo's server under `@fyan/travel-app` — no local keychain needed.

### Production build (TestFlight / App Store)

```bash
make preflight-eas          # MUST be green — validates eas.json production env, contract, tests
cd "Travel App"
eas build --platform ios --profile production
# then submit from App Store Connect (or `eas submit -p ios --profile production`)
```

- The Clerk `pk_live_` key is an EAS env var (not committed) — see Owner Action Items #3.
- Runtime backstop: `app/_layout.tsx` throws on boot of any release build left in mock / skip-auth mode, or missing the Clerk key.

---

## 4. Post-deploy verification (smoke)

```bash
# Core HTTP + auth + AASA + trip CRUD
PRELAUNCH_HOST=https://<app>.fly.dev make smoke

# Add the deep checks once infra is live (each is opt-in; the concierge
# turn runs a real LLM turn and costs tokens):
PRELAUNCH_HOST=https://<app>.fly.dev \
  SMOKE_VERIFY_WORKER=1 \
  SMOKE_VERIFY_CONCIERGE=1 \
  SMOKE_VERIFY_AUTH=1 PRELAUNCH_JWT=<test JWT> \
  make smoke
```

- `SMOKE_VERIFY_WORKER=1` → `GET /health/external`; **asserts Redis is reachable** (the arq worker's job intake) and surfaces the Anthropic/Tavily probes. This is how you catch "API green but background jobs dead."
- `SMOKE_VERIFY_CONCIERGE=1` → POSTs a real message to `/api/trips/{id}/messages/stream` and asserts an SSE reply — the actual product flow.
- `/ready` (DB + Qdrant) gates Fly routing; `/health/external` (Anthropic + Tavily + Redis) is monitoring-only and returns 200 with a degraded body — consume it from smoke/alerting, not the routing probe.

If smoke catches a P0 → go to §5.

---

## 5. Rollback

### 5.1 Backend app (the common case)

```bash
cd "Travel Agent"
fly releases                       # find the last-good version + its image ref
fly deploy --image <previous-image-ref>   # redeploy the prior image, no rebuild
```

- This redeploys old code. `release_command` runs again, but `alembic upgrade head` against an already-migrated DB is a **no-op** — so the app rolls back and the schema stays forward. That's intended (see Golden rule).
- Transient single-machine issue (not a bad release)? `fly machine restart <id>` first.

### 5.2 Worker-down checklist

The `worker` process has no HTTP health check, so a failed worker ships "green." If background work (audio prerender, digests, pre-trip, push) stops:

1. `fly status` — are `worker` machines `started`, or crash-looping?
2. `fly logs -i <worker-machine>` — look for `ModuleNotFoundError: arq` (deps regression — arq/redis must be in `requirements.txt`), or a Redis connection error.
3. `SMOKE_VERIFY_WORKER=1 make smoke` — confirms Redis reachability from the app side.
4. Confirm `REDIS_URL` is set: `fly secrets list`.
5. Recover: `fly deploy` (re-roll) or `fly scale count worker=1` if the group scaled to 0.

The app keeps serving synchronous chat without the worker (jobs fall back to inline / are dropped), so this is degradation, not an outage — fix it but you don't have to roll back the whole app for it.

### 5.3 Database migration rollback (rare — only if a migration is the fault)

Most rollbacks need **no** schema downgrade (Golden rule). Downgrade only when a new migration is actively breaking and forward-fix isn't fast enough.

```bash
cd "Travel Agent"
PYTHONPATH=. alembic current        # confirm where you are
PYTHONPATH=. alembic downgrade -1   # step back ONE revision (preferred)
```

**Before downgrading, check the hazard table — some downgrades destroy data or fail on live rows:**

| Revision | Hazard on downgrade | Severity |
|---|---|---|
| `c0a1d2e3f4b5` (observations onboarding source_mode) | **Deletes** `observations` rows with `source_mode='onboarding'` (now pre-deletes so the downgrade no longer aborts — but the rows, which feed Personal Memory synthesis, are gone). | data loss |
| `7e588b9dd09e` (memory story_archive) | **Deletes** `memory_interactions` rows with `surface='story_archive'`. | data loss |
| `e1f3a5c9b2d7` (entity_saves trip_story) | **Deletes** `entity_saves` rows with `entity_type='trip_story'`. | data loss |
| `b5e6a7d9c0f3` (constraint severity backfill) | Lossy data-only inverse — over-promotes hard-constraint severities back to `absolute`. | correctness |

Recent head-ward migrations (incl. `scheduled_tasks` `d8f2a1c9e3b4`) are clean column/table drops — safe to downgrade. **Take a DB snapshot before any downgrade that crosses a hazard row** (`fly postgres` backup, or your managed Postgres provider's PITR).

**Roll-forward recovery (preferred over downgrade for a bad migration):** write a *new* migration that fixes the schema and `fly deploy`. This avoids the data-loss downgrades entirely and keeps the chain linear.

### 5.4 API contract rollback

If the backend shipped a breaking response shape and the app is choking:
- Fastest: roll the backend app back (§5.1) so the response shape matches the shipped app.
- The committed `docs/openapi.json` snapshot is the contract of record; regenerate types with `./scripts/sync-types.sh` after any forward-fix.
- There is **no API version prefix and no min-client-version gate** today, so old TestFlight builds break silently against a breaking backend — prefer additive (expand/contract) response changes during dogfood.

### 5.5 Frontend rollback (TestFlight)

There is **no OTA update channel** (no `expo-updates`), so a JS rollback requires a new build.
- Bad build already with testers: in App Store Connect, stop distributing the bad build and re-promote the previous TestFlight build; testers update via TestFlight.
- For a code fix: bump, `make preflight-eas`, `eas build --profile production`, resubmit.
- Until the fixed build propagates, mitigate server-side (roll the backend back to the shape the old app expects, §5.1/§5.4).

---

## 6. Scenario → response quick map

| Scenario | Response |
|---|---|
| Migration fails during `fly deploy` | Nothing to undo — deploy aborted, old machines still serving. Fix forward, redeploy. |
| API deployed, worker failed | §5.2 worker checklist. App still serves; not an outage. |
| Migration applied but app must roll back | §5.1 app rollback; leave schema forward (additive). |
| Bad migration needs reverting | Prefer roll-forward (§5.3); downgrade only with the hazard table + a snapshot. |
| Backend shipped breaking response shape | §5.1 roll backend back to match the app; forward-fix additively. |
| Env var missing in prod | `fly secrets set …` (re-roll); `/ready` 503 surfaces missing Postgres/Qdrant; `SMOKE_VERIFY_WORKER` surfaces missing Redis. |
| Health green but provider/job path broken | `GET /health/external` (Anthropic/Tavily/Redis) — not gated into `/ready` by design. |
| Old app build vs new backend | No compatibility gate yet — roll backend back or keep response changes additive. |
| Dogfood smoke catches a P0 | Roll back the faulting surface per §5; capture the failing smoke output. |

---

## 7. See also

- `docs/Pre-Launch Deploy Surface.md` — every secret/env var by deploy risk.
- `docs/Owner Action Items.md` — account/credential gates (#3 eas init, #5/#6 domain+SSL, #7 Clerk).
- `Travel Agent/fly.toml` — process groups, release_command, health checks (annotated).
- `Travel Agent/docs/operations/Migration Squash Runbook.md` — chain maintenance (distinct from rollback).
- `scripts/smoke-happy-path.sh` — post-deploy verification (incl. `SMOKE_VERIFY_WORKER` / `SMOKE_VERIFY_CONCIERGE`).
