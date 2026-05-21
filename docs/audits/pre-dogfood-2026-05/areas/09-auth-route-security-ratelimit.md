# Pre-Dogfood Area Audit 09 — Auth, Route Security & Rate Limits

Date: 2026-05-21  
Scope: centralized auth dependencies, intentionally public routes, SKIP_AUTH release posture, `_LIMITS` / daily quotas, `scripts/check_route_auth.py`, admin/metrics protection, request-boundary validation.  
Mode: read-only; no product code, test, or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 0 |
| P1 | 2 |
| P2 | 5 |
| TECH-DEBT | 4 |

**Overall posture:** The May 2026 auth audit pass landed hard. Every route under `backend/api/routes/` declares auth (or a documented `# noauth:` escape hatch), `/admin/*` and `/metrics/*` are router-gated on `X-Service-Token`, SKIP_AUTH defaults off and hard-fails boot on prod-like hosts, and CI runs `check_route_auth.py --ci` clean. Per-trip **mutating** routes are covered by `tests/api/test_route_auth_coverage.py` (14 tests green).

**Biggest gap for real testers:** `backend/api/main.py` registers six app-level routes (`/debug/tokens`, `/debug/cost`, four health probes) that **never enter** `check_route_auth.py`'s scan tree. Two debug endpoints return full in-memory LLM token/cost totals with **no auth** — on any reachable dogfood host that is a direct operational leak and a weak cost-recon surface. The gate reports "0 violations" while these routes sit outside its scope.

**Rate-limit shape:** Expensive authenticated paths (chat, search, research, narrate, voice render, plan-similar) use `check_rate_limit` +, for chat, Postgres-backed `check_rate_limit_pg`. Daily caps cover chat tokens (`chat_token_counters`, 1M/day default) and invite SMS/email dispatch (`invite_dispatch_counters`, 20/day). Public content routes (`/api/search/suggest`, `/nearby`) and multipart uploads are the main uncapped surfaces.

---

## Findings

### [P1] — `/debug/tokens` and `/debug/cost` are unauthenticated on the live app

**References:**
- `Travel Agent/backend/api/main.py:293-303` — `@app.get("/debug/tokens")` and `@app.get("/debug/cost")` with no `Depends(get_current_user)` or service token.
- `Travel Agent/backend/core/logging_config.py` — `token_tracker.summary()` / `cost_breakdown()` source the in-memory rolling totals.
- `Travel Agent/scripts/check_route_auth.py:49` — scans only `backend/api/routes/*.py`; does not walk `main.py`.

**Why it matters to a real tester:** Anyone who can reach the dogfood API host (TestFlight builds point at `travel-agent.fly.dev` / `travelagent.app`) can `curl /debug/cost?days=30` and read aggregate LLM spend, model mix, and usage trends without signing in. That confirms the API is live, exposes operational economics, and bypasses the admin-token gate that protects `/metrics/tokens`.

**Repro / deterministic test idea:**
```bash
curl -sS "https://<host>/debug/cost?days=7" | jq '.totals.cost_usd'
curl -sS "https://<host>/debug/tokens" | jq 'keys'
```
Expect HTTP 401/403; observed today: 200 with JSON body.

**Suggested fix direction:** Gate both routes behind `require_admin_token` (or remove them from production builds entirely). Extend `check_route_auth.py` to AST-walk `main.py` `@app.*` decorators so the CI gate cannot miss app-level routes again. Add `# noauth:` only if a route is intentionally public (these are not).

**Confidence:** High.

---

### [P1] — `check_route_auth.py` passes clean but does not cover the full mounted route set

**References:**
- `Travel Agent/scripts/check_route_auth.py:326-329` — glob is `ROUTES_ROOT.glob("*.py")` only under `backend/api/routes/`.
- `Travel Agent/scripts/check_route_auth.py:335-338` — `--emit-baseline` returns **0 rows** (empty allowlist, 0 violations).
- `Travel Agent/tests/scripts/test_check_route_auth.py:218-231` — live smoke asserts exit 0.
- `Travel Agent/.github/workflows/ci.yml:74` — CI runs the script in `--ci` mode.
- `Travel Agent/backend/api/main.py:103-303` — six `@app.get` routes outside the scan tree (`/health`, `/ready`, `/health/external`, `/health/background-tasks`, `/debug/tokens`, `/debug/cost`).
- `Travel Agent/backend/api/router_registry.py:61-115` — 241 routes registered via `_ROUTERS`.

**Why it matters to a real tester:** The team treats a green `check_route_auth.py` as proof that "every route has auth + LLM routes have rate limits." That proof is incomplete: app-level debug routes slipped through, and future `@app.post(...)` handlers added in `main.py` would never fail CI. The membership test (`test_route_auth_coverage.py`) has the same blind spot — it iterates `_ROUTERS` only.

**Repro / deterministic test idea:**
1. Add a throwaway `@app.get("/debug/leak-test")` in `main.py` without auth.
2. Run `PYTHONPATH=. python scripts/check_route_auth.py --ci`.
3. Observe exit 0 (false negative).

**Suggested fix direction:** Extend the scanner to parse `main.py` (and any future non-router mount points). Add a complementary test that asserts the union of `(method, path)` from `app.routes` matches the scanned set ± documented health/noauth list.

**Confidence:** High.

---

### [P2] — Public search typeahead and spatial endpoints have no rate limit

**References:**
- `Travel Agent/backend/api/routes/search.py:399-405` — `# noauth: public typeahead` on `GET /api/search/suggest`.
- `Travel Agent/backend/api/routes/search.py:548-561` — `# noauth: public spatial search` on `GET /api/search/nearby`.
- `Travel Agent/backend/api/routes/search.py:257-275` — authenticated `POST /api/search` calls `check_rate_limit("search", ...)`.
- `Travel Agent/backend/api/rate_limits.py:24-34` — `_LIMITS` has a `"search"` scope but public GET handlers never call it.

**Why it matters to a real tester:** Discover/marketing surfaces are intentionally public, but a script can hammer `/api/search/suggest?q=a&city=lisbon` or `/api/search/nearby?lat=…&lng=…&city=lisbon` without a token. Each call fans out six Postgres `pg_trgm` queries (suggest) or PostGIS work (nearby). No LLM spend, but real DB/CPU load — the classic pre-auth scraping DoS shape on a single-tenant dogfood host.

**Repro / deterministic test idea:** Loop 500 concurrent unauthenticated suggest requests; watch Postgres connection count and p95 latency. Expect no HTTP 429 today.

**Suggested fix direction:** Add IP-based or global sliding-window limits for `# noauth` search routes (separate scope, e.g. `search_public: 120/min per IP`). Keep authenticated `/api/search` on the existing per-user gate.

**Confidence:** High.

---

### [P2] — Multipart photo/receipt uploads read the full body with no API-level size cap

**References:**
- `Travel Agent/backend/api/routes/trip_photos.py:159-161` — `bytes_ = await file.read()` with no `len` check before processing.
- `Travel Agent/backend/api/routes/expenses.py:667-669` — same pattern on receipt upload; records `file_size_bytes` but does not reject oversized files.
- `Travel Agent/backend/media/settings.py:31` — `max_download_bytes = 15 * 1024 * 1024` applies to **URL rehost**, not direct multipart uploads.
- `Travel Agent/backend/api/routes/chat.py:83-87` — inline chat images capped at ~1.8MB base64 via Pydantic `max_length=2_500_000`.

**Why it matters to a real tester:** An authenticated member can POST a multi-hundred-MB file to `/api/trips/{trip_id}/photos/upload` or `/receipts/upload`. The handler loads it entirely into memory before `rehost_from_bytes` runs. One tester accidentally exporting a camera roll, or a malicious member, can OOM the API process.

**Repro / deterministic test idea:** POST a 50MB JPEG as a trip member; expect 413/422 with a clear size limit. Current behavior: accepts and processes until memory/rehost fails opaquely.

**Suggested fix direction:** Reject `len(content) > N` (e.g. 15MB, aligned with media settings) before EXIF/OCR work. Optionally configure Starlette/FastAPI request body limits at the middleware layer.

**Confidence:** High.

---

### [P2] — In-process rate limits do not coordinate across Fly machines

**References:**
- `Travel Agent/backend/api/rate_limits.py:3-5` — documents in-process counter; "on multi-process deploys upgrade to Redis-backed."
- `Travel Agent/backend/api/rate_limits.py:36-64` — module-level `_state` dict + `threading.Lock`.
- `Travel Agent/backend/api/routes/chat.py:233-234` — chat uses **both** `check_rate_limit` and `check_rate_limit_pg` (double gate).
- `Travel Agent/fly.toml:114-117` — concurrency autoscale up to 100 connections; multiple machines possible in production.

**Why it matters to a real tester:** Scopes like `research_quick`, `plan_similar`, `search`, `narrate` rely on in-process limits only. Chat is better protected (Postgres gate). If Fly scales to N machines, per-user caps become N× the configured limit — a compromised Clerk token could spread load across workers and multiply LLM/Qdrant spend.

**Repro / deterministic test idea:** With two uvicorn workers locally, send 30 `concierge_turn` requests in one minute split across workers; observe whether the 31st is rejected (in-process only → often not; with PG → rejected).

**Suggested fix direction:** For dogfood single-machine (`min_machines_running = 1`) this is acceptable short-term. Before multi-machine prod, wire `check_rate_limit_pg` on all `_LIMITS` scopes or move counters to Redis.

**Confidence:** Medium (depends on deploy topology; fly.toml currently keeps one machine).

---

### [P2] — Trip story composition/regeneration has membership but no LLM quota

**References:**
- `Travel Agent/backend/api/routes/memory.py:141-190` — `POST …/story/regenerate` enqueues `compose_trip_story_job` with job dedupe only.
- `Travel Agent/backend/api/routes/memory.py:224-237` — `GET …/story` auto-enqueues composition on first miss (202).
- `Travel Agent/backend/api/rate_limits.py:24-34` — no scope for story composition.
- `Travel Agent/backend/workers/story_jobs.py` — background Sonnet composition (~30–90s per run).

**Why it matters to a real tester:** Any trip member can repeatedly hit regenerate (or poll GET until each job completes, then regenerate again). Job `_job_id` dedupes **concurrent** runs per `(trip_id, user_id)` but not serial spam after completion. A curious tester clicking "regenerate" ten times burns ten Sonnet compositions with no daily cap — unlike chat (`chat_token_counters`) or voice (`voice_quota_counters`).

**Repro / deterministic test idea:** As a trip member, POST regenerate, wait for 200 on GET story, repeat 10×; assert Anthropic spend / `prompt_calls` rows stay under a configured daily ceiling. Today: no ceiling.

**Suggested fix direction:** Add a per-user daily story-compose cap (reuse `rate_limit_events` pattern) or fold composition token spend into `chat_token_counters`.

**Confidence:** Medium.

---

### [P2] — `/health/external` is unauthenticated and triggers outbound Anthropic `count_tokens`

**References:**
- `Travel Agent/backend/api/main.py:144-266` — `@app.get("/health/external")`, no auth.
- `Travel Agent/backend/api/main.py:186-196` — calls `client.messages.count_tokens(...)` when `ANTHROPIC_API_KEY` is set.
- `Travel Agent/fly.toml:128-129` — documents worker/background dependency probing via this endpoint.

**Why it matters to a real tester:** Low-severity cost surface: anyone can poll `/health/external` and each poll may invoke Anthropic's count_tokens API (cheap vs chat, but non-zero and unauthenticated). Also reveals dependency status (Anthropic/Tavily/Redis) to scanners.

**Repro / deterministic test idea:** `while true; do curl -sS https://<host>/health/external; done` — observe Anthropic API call volume. Expect rate limiting or auth; neither exists.

**Suggested fix direction:** Gate behind admin token or move to an internal ops port; replace live Anthropic ping with TCP/connect-only probe for public monitoring.

**Confidence:** Medium.

---

### [TECH-DEBT] — `check_route_auth` LLM trigger list misses several expensive call targets

**References:**
- `Travel Agent/scripts/check_route_auth.py:61-86` — `_LLM_TRIGGERS` set.
- `Travel Agent/backend/api/routes/admin.py:139-176` — `run_reflection`, `refresh_personal_memory` (LLM) with no `check_rate_limit`.
- `Travel Agent/backend/api/routes/memory.py` — story jobs enqueue LLM work without `check_rate_limit` in the route body.

**Why it matters to a real tester:** Admin routes are service-token gated (acceptable), but the AST gate would not flag a future **authenticated** route that calls `run_reflection` without a rate limit — the trigger list omits it. Same for `compose_trip_story_job`, `generate_snapshot`, etc.

**Suggested fix direction:** Expand `_LLM_TRIGGERS` to include reflection/memory/story entry points, or detect imports from `backend.concierge.reflection`, `refresh_memory`, `invite_snapshot`.

**Confidence:** High.

---

### [TECH-DEBT] — `test_route_auth_coverage.py` only asserts membership on mutating methods

**References:**
- `Travel Agent/tests/api/test_route_auth_coverage.py:45-49` — `_MUTATING_METHODS = {POST, PUT, PATCH, DELETE}`; GET excluded by comment.
- `Travel Agent/tests/api/test_route_auth_coverage.py:132-165` — test skips GET `/api/trips/{trip_id}/…` read paths.

**Why it matters to a real tester:** A new GET that returns trip messages, expenses, or personal memory without `is_trip_member` would not fail this test. Manual scan today shows GET trip routes use `_require_trip_member`, `_require_organizer`, `_require_membership`, or `require_self_or_trip_organizer`, but the gate does not enforce that going forward.

**Suggested fix direction:** Add a sibling test for GET routes under `/api/trips/{trip_id}/` that return trip-scoped payloads (allowlist health/public paths).

**Confidence:** High.

---

### [TECH-DEBT] — `Auth Modes.md` documents removed `get_optional_user`

**References:**
- `Travel Agent/docs/operations/Auth Modes.md:46-58` — still documents `get_optional_user`.
- `Travel Agent/backend/api/auth.py:10-14` — helper removed 2026-05-18 with rationale.

**Why it matters to a real tester:** Operators following the doc might reintroduce optional-auth patterns that the audit deliberately eliminated.

**Suggested fix direction:** Update Auth Modes.md to match `auth.py`; note that all public surfaces use `# noauth:` on the route, not optional JWT.

**Confidence:** High.

---

### [TECH-DEBT] — `.env.example` defaults `SKIP_AUTH=true` (local-only; easy to mis-deploy)

**References:**
- `Travel Agent/.env.example:47` — `SKIP_AUTH=true`.
- `Travel Agent/backend/api/auth.py:37-41` — runtime default is `"false"` (secure).
- `Travel Agent/backend/api/lifecycle.py:68-73` — boot fails if `SKIP_AUTH=true` and `FLY_APP_NAME` or prod-like `ENV` is set.

**Why it matters to a real tester:** Copy-paste `.env.example` to a staging host without Clerk keys enables SKIP_AUTH locally; prod-like hosts are protected by `_validate_startup`, but a host with **neither** `FLY_APP_NAME` nor `ENV=production` set could still run with SKIP_AUTH if an operator copies example env verbatim.

**Suggested fix direction:** Comment loudly in `.env.example` that `SKIP_AUTH=true` is local-dev only; consider `SKIP_AUTH=false` in example with a commented local override block.

**Confidence:** Medium.

---

## Route inventory (auth classification)

### Intentionally unauthenticated (`# noauth:` in `backend/api/routes/`)

| Route pattern | Purpose | LLM / PII risk |
|---|---|---|
| `GET /api/invites/{token}` | Pre-auth invite landing JSON | **LLM** (Haiku snapshot, cached; 20 regen/day per invite) |
| `POST /api/invites/{token}/intake` | Pre-auth chip answers | No LLM; writes pending intake on invite row |
| `GET /invite/{token}` | HTML/OG landing (invite_landing) | Delegates to `view_invite` |
| `GET /.well-known/apple-app-site-association` | Universal Links | Static JSON |
| `GET /api/public/stories/{slug}`, `/stories/{slug}`, card PNG | Public trip story share | Redacted projection only |
| `GET /api/public/stories/{slug}/plan-seed` | Plan-similar preview | No LLM |
| `GET /api/search/suggest`, `/api/search/nearby` | Public discover search | Postgres/PostGIS only; **uncapped** |
| `GET /api/discover/trending`, venues/experiences/dossiers/angles/collections public reads | Editorial/marketing content | Published content only |
| `GET /api/legal/*` | App Store legal text | Static |
| `POST /webhooks/*` | Bland/Twilio | HMAC-verified inline |

### App-level (`main.py`, not in route linter)

| Route | Auth | Notes |
|---|---|---|
| `GET /health`, `/ready` | None | Expected for probes |
| `GET /health/external`, `/health/background-tasks` | None | Dependency introspection |
| `GET /debug/tokens`, `/debug/cost` | **None** | **P1 — should not ship on dogfood host** |
| `GET /openapi.json`, `/docs` | None | FastAPI default; schema exposure expected |

### Authenticated + membership patterns (spot check)

| Area | Pattern | Status |
|---|---|---|
| Chat / conversations | `get_current_user` + `_require_self` + participant/member checks + `check_rate_limit("concierge_turn")` + `check_rate_limit_pg` + `check_chat_quota` | OK |
| Voice token | `Depends(verify_trip_member)` + voice quota | OK |
| Trips CRUD / plan / expenses | `_require_trip_member` throughout | OK |
| Proposals / booking / notifications | Auth + member or self checks | OK |
| Profiles | `get_current_user`; 404 unless `public_profile_enabled` or self | OK |
| Personal memory API | `require_self` on `/api/users/{user_id}/personal-memory` | OK |
| Heartbeat + body `trip_id` | `require_self` + `is_trip_member` before presence upsert | OK (fixed 2026-05-18) |

### Admin / metrics

| Router | Gate | Notes |
|---|---|---|
| `/admin/*` | `dependencies=[Depends(require_admin_token)]` on router | Secure-by-default when `ADMIN_API_TOKEN` unset (403 all) |
| `/metrics/tokens` | Same admin token on router | OK |
| `/api/admin/voice-metrics` | `require_admin_token` on route | OK (docstring still mentions "any authenticated user" — stale) |
| `/api/admin/discover/trending` | `require_admin_token` on POST | OK |
| `/api/curator/photos` | `require_curator_token` on router | OK |

---

## Rate limits & daily quotas

### `_LIMITS` scopes (`backend/api/rate_limits.py`)

| Scope | Window | Cap | Used by |
|---|---:|---:|---|
| `lookup` | 60s | 30 | `/api/lookup` |
| `research_quick` | 3600s | 60 | `/api/research/quick` |
| `research_deep` | 3600s | 6 | `/api/research/deep` |
| `concierge_turn` | 60s | 30 | chat + conversations message POST (+ PG) |
| `search` | 60s | 60 | `POST /api/search` only |
| `narrate` | 60s | 30 | narration routes |
| `voice_render` | 60s | 20 | voice bridge render |
| `take` | 60s | 30 | personal takes |
| `plan_similar` | 3600s | 20 | `POST /api/plan-similar` |

### Daily Postgres counters

| Counter | Default cap | Enforced in |
|---|---:|---|
| Chat tokens | 1,000,000 / user / UTC day | `concierge/chat_quota.py` → `session.py` |
| Invite SMS/email dispatch | 20 / user / UTC day | `notifications/invite_quota.py` → `invites.py` |
| Voice sessions | Phase-bucketed | `voice/quota.py` |

### Invite snapshot LLM regen

- `SNAPSHOT_REGEN_DAILY_CAP = 20` per invite (`trip_invites.py:27`).
- First-ever view may block inline on Haiku if cache cold (`invites.py:643-645`).

---

## SKIP_AUTH release posture

| Control | Location | Verdict |
|---|---|---|
| Default off | `auth.py:41` — `SKIP_AUTH` defaults `"false"` | OK |
| Prod boot guard | `lifecycle.py:68-73` — raises if `SKIP_AUTH=true` and `FLY_APP_NAME` or `ENV ∈ {prod,production,staging}` | OK |
| Dev user validation | `lifecycle.py:74-88` — requires valid `DEFAULT_DEV_USER_ID` UUID when SKIP_AUTH on | OK |
| Clerk required when auth on | `lifecycle.py:95-101` — fails boot without `CLERK_JWKS_URL` | OK |
| Fly deploy template | `fly.toml` — lists `CLERK_JWKS_URL` / `CLERK_ISSUER` in secrets checklist; does **not** set SKIP_AUTH | OK |

**Verdict:** SKIP_AUTH cannot be enabled on a correctly configured Fly/staging boot path. Residual risk is a mis-labeled host (no `FLY_APP_NAME`, `ENV` unset) with copied `.env.example`.

---

## `scripts/check_route_auth.py` gate

| Check | Result (this audit) |
|---|---|
| `PYTHONPATH=. python scripts/check_route_auth.py` | **PASS** — 0 violations, 0 stale allowlist rows |
| `PYTHONPATH=. python scripts/check_route_auth.py --ci` | **PASS** |
| `pytest tests/scripts/test_check_route_auth.py` | **14 passed** |
| `pytest tests/api/test_route_auth_coverage.py` | **4 passed** |
| Baseline file `check_route_auth_baseline.tsv` | **Absent** (empty allowlist — all routes compliant) |
| Route modules scanned | 54 files under `backend/api/routes/` (excludes `_*.py` helpers) |
| Routes **not** scanned | 6 `@app.*` handlers in `main.py` |

---

## Input validation (boundary spot check)

| Surface | Validation | Gap |
|---|---|---|
| Chat message | `min_length=1`, `max_length=10_000`; images `max_length=4`, base64 cap | OK |
| Research body | `query` max 500 chars | OK |
| Search suggest | `q` max 200, `limit` le 20 | OK |
| Invite intake | Pydantic `InviteIntakeRequest` | OK |
| Receipt/photo upload | Content-type allowlist | **No max file size** (P2 above) |
| CORS | Explicit origins; rejects `*` with credentials; prod requires https | OK (`main.py:46-97`) |

---

## Positive signals

- Central auth module with secure defaults; `get_optional_user` removed to prevent accidental optional-auth endpoints.
- Router-level admin/curator/metrics gates — new admin routes inherit protection automatically.
- Chat path uses defense-in-depth: JWT + trip membership + per-minute rate limit + Postgres rate limit + daily token quota + input guardrails (S-1).
- Public invite/story surfaces use bearer-token / unguessable-slug models, not wide-open IDs.
- CI enforces route auth lint on every PR; membership regression test covers mutating trip routes and body-embedded `trip_id`.
- CORS tightened (explicit methods/headers; no wildcard admin-token leakage via `allow_headers=["*"]`).

---

## Known / Accepted

- **Public invite landing LLM (`GET /api/invites/{token}`)** — Intentionally unauthenticated; invite token is the credential. Haiku snapshot is cached with 1h TTL and 20 regens/invite/day. First-view inline generation is accepted for OG preview quality. Privacy risk of organizer PM in snapshot is tracked in **Area Audit 01**, not re-opened here.
- **Public story/share JSON and HTML** — Unguessable slug; server-side redaction via `get_public_story_by_slug`. No auth required by design.
- **Health liveness/readiness (`/health`, `/ready`)** — Unauthenticated; required for Fly probes (`fly.toml:120-126`). `/ready` returns dependency error strings — acceptable for infra routing.
- **Webhook routes** — `# noauth:` with inline HMAC verification (Bland AI, Twilio). Exempted in `test_route_auth_coverage._EXEMPTIONS`.
- **Admin LLM triggers (`/admin/users/{id}/reflect`, `/refresh-memory`)** — No per-route rate limit; accepted because `ADMIN_API_TOKEN` is secure-by-default unset and constant-time compared. Operator tooling, not end-user surface.
- **O-4 resolved (2026-05-16)** — `chat_token_counters` / `invite_dispatch_counters` migrations active; daily gates no longer fail-open.
- **In-process rate limiter** — Accepted for single-machine dogfood (`min_machines_running = 1` in `fly.toml`); upgrade path documented in `rate_limits.py`.
- **OpenAPI / docs exposure** — Standard FastAPI; frontend contract depends on `/openapi.json`. Not treated as a vulnerability for this product stage.
