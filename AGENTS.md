# AGENTS.md — Travel Workspace

## Purpose

This folder is the **cross-repo workspace root** for the travel product.

It coordinates two independent repositories:

| Repo | Path | Stack | Purpose |
|---|---|---|---|
| `Travel Agent` | `./Travel Agent/` | Python, FastAPI, Postgres, Qdrant | Backend API, agent systems, database, OpenAPI source |
| `Travel App` | `./Travel App/` | React Native, Expo, TypeScript | Mobile client, UI, generated API types |

This is a **workspace repo**, not a superproject:

- Keep `Travel Agent` and `Travel App` as separate git repositories.
- Do **not** convert them into submodules.
- Use this parent folder for shared docs, shared scripts, and cross-repo workflows.

Read each repo's own `AGENTS.md` / `CLAUDE.md` for repo-specific rules.

## Working Model

Use this workspace root when:

- a task spans backend + frontend
- you are syncing API contract changes
- you are editing shared docs or scripts
- you want Codex to see both repos in one project

Use a child repo root when:

- the task is isolated to one codebase
- you want tighter context and fewer accidental cross-repo edits

## Cross-Repo Contract

### API schema

The backend exposes OpenAPI at:

- live: `http://localhost:8000/openapi.json`
- committed snapshot: `./docs/openapi.json`

The frontend consumes generated types from:

- `Travel App/utils/api/schema.gen.ts`

### Required workflow for backend API changes

When backend models or routes change:

1. Update backend code and tests in `Travel Agent`
2. Run `./scripts/sync-types.sh` from this workspace root
3. Review `docs/openapi.json`
4. Review `Travel App/utils/api/schema.gen.ts`
5. Fix any frontend type breakage before finishing

Do not hand-maintain TypeScript copies of backend schema models when generated types are appropriate.

## Commands

Run these from `/Users/feihuyan/Documents/Claude/Travel Workspace`:

```bash
make dev                  # backend infra + API + Expo
make dev-backend          # backend infra + API only
make sync-types           # fetch live OpenAPI and regenerate frontend types
make sync-types-snapshot  # regenerate from committed snapshot
make typecheck            # frontend typecheck
make doctor               # workspace health check
make test-backend         # backend offline tests
make test-frontend        # frontend Jest
make test-all             # offline backend + frontend tests
make status               # quick cross-repo git status
```

## Git Guidance

- Treat this repo as a lightweight coordination layer.
- Keep child-repo history in the child repos.
- Avoid storing product source code directly in this parent repo.
- It is okay for this repo to track:
  - shared docs
  - scripts
  - workspace files
  - meta tooling

Recommended git model:

- one branch in `Travel Agent` per backend change
- one branch in `Travel App` per frontend change
- this parent repo changes only when shared tooling/docs/workspace config changes

## Suggested Local Setup

- Open this parent folder as a Codex project for cross-repo work.
- Keep a saved multi-root editor workspace that includes:
  - `Travel Agent`
  - `Travel App`
  - this parent repo's `docs/` and `scripts/`
- Use `git worktree` inside each child repo when you want parallel feature branches or multiple AI threads.

## Files In This Repo

- `AGENTS.md` — cross-repo AI guidance
- `CLAUDE.md` — existing cross-repo guidance for Claude-oriented workflows
- `README.md` — human-readable workspace map
- `Makefile` — cross-repo commands
- `docs/openapi.json` — committed API snapshot
- `scripts/dev.sh` — start local stack
- `scripts/doctor.sh` — validate workspace/tooling setup
- `scripts/new-branch.sh` — coordinated child-repo branch helper
- `scripts/sync-types.sh` — regenerate frontend API types
- `travel.code-workspace` — editor workspace file

## Cursor Cloud specific instructions

### Prerequisite: child repo access

This workspace coordinates two **private** child repos (`fy538/travel-agent` and `fy538/travel-app`). The Cursor GitHub App installation must be granted access to both repos, otherwise `make bootstrap` and all downstream commands will fail. The repos must be added under **Settings → GitHub Apps → Cursor → Repository access** for the `fy538` GitHub account.

### System dependencies (pre-installed in the VM snapshot)

- **Python 3.13** — installed via `deadsnakes` PPA (`python3.13`, `python3.13-venv`, `python3.13-dev`)
- **Node.js 20** — managed by `nvm` (pre-installed in the base image)
- **Docker Engine 28.x** — configured with `fuse-overlayfs` storage driver and `iptables-legacy` for nested-container compatibility

### Starting Docker

Docker daemon is not auto-started. Run before any `docker compose` operation:

```bash
sudo dockerd &>/tmp/dockerd.log &
sleep 3
```

### Bootstrap sequence (once child repos are accessible)

```bash
make bootstrap                                              # clone child repos
cd "Travel Agent" && python3.13 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt
cd "Travel App" && npm ci
```

### Running services

See `README.md` and `CLAUDE.md` for the full command reference. Key commands:

- `make dev-backend` — Docker infra (Postgres + Qdrant) + API server (no Expo)
- `make test-backend` — offline pytest (skips `requires_postgres` and `requires_api_keys`)
- `make test-frontend` — Jest
- `make typecheck` — `tsc --noEmit` in Travel App
- `make contract-check` — verify OpenAPI snapshot ↔ generated types

### Environment variables

The backend requires `ANTHROPIC_API_KEY` for AI features. Set `SKIP_AUTH=true` to bypass Clerk JWT auth in dev. Database and Qdrant URLs are auto-configured by `docker-compose.yml` defaults.
