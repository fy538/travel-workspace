# Travel Workspace

This folder is the shared workspace for the travel product.

It contains two independent repositories plus the cross-repo tooling that ties them together.

## Repositories

- [Travel Agent](./travel-agent/) — backend API, agent systems, database, OpenAPI source
- [Travel App](./travel-app/) — React Native app, UI, generated API types

## Why this folder exists

This is the right root for:

- backend + frontend feature work
- API contract sync
- shared scripts
- shared docs
- AI-assisted tasks that need both repos in view

This is **not** a superproject for the child repos.

- `Travel Agent` and `Travel App` stay as separate git repositories.
- This repo tracks only workspace-level assets.

## Start Here

- [AGENTS.md](./AGENTS.md) — cross-repo AI and workflow guidance
- [CLAUDE.md](./CLAUDE.md) — existing cross-repo contract notes
- [Workspace Repo Setup](./docs/Workspace%20Repo%20Setup.md) — how to clone/bootstrap this coordination repo
- [docs/openapi.json](./docs/openapi.json) — committed backend schema snapshot
- [docs/openapi.app.json](./docs/openapi.app.json) — generated active-mobile schema projection
- [travel.code-workspace](./travel.code-workspace) — saved multi-root editor workspace

## First-Time Setup

```bash
git clone <travel-workspace-url> "Travel Workspace"
cd "Travel Workspace"
make bootstrap
make doctor
make contract-check
```

`make bootstrap` clones or validates the child repos at `Travel Agent/` and
`Travel App/`. Those folders remain independent Git repos and are ignored by
the workspace repo.

## Common Commands

```bash
make bootstrap
make dev
make dev-backend
make sync-types
make sync-types-snapshot
make typecheck
make doctor
make contract-check
make mock-real-parity
make golden-path-qa
make certify-fast
make certify-logic
make certify-visual
make dogfood-status
make offline-qa
make reliability-report
make test-backend
make test-frontend
make test-all
make status
```

## Recommended Workflow

### Cross-repo feature

1. Work in `Travel Agent`
2. Run `make sync-types`
3. Work in `Travel App`
4. Commit backend and frontend changes in their own repos

### Coordinated worktree lane

```bash
./scripts/new-worktree.sh trip-group-chat
```

That creates a paired worktree lane (siblings of `travel-agent/` and `travel-app/`) on the same branch name in both child repos, for parallel implementation threads. Use `./scripts/land-worktree.sh` to land and clean up the lane.

### Offline reliability workflow

Use these commands when you want Codex or Claude Code to test reliability without
burning product API tokens:

```bash
make contract-check      # OpenAPI snapshot agrees with generated app types
make mock-real-parity    # mock and HTTP API seams still typecheck/test
make golden-path-qa      # focused MVP journey invariants
make offline-qa          # full offline reliability ladder
make reliability-report  # cheap status snapshot
```

See [Agent Reliability Playbook](./docs/reliability/Agent%20Reliability%20Playbook.md)
and the [canonical journey index](./docs/journeys/README.md) for the testing model.
The reliability folder also includes [trace artifacts](./docs/reliability/traces/README.md),
[agent prompt templates](./docs/reliability/prompts/README.md), a
[manual live canary plan](./docs/reliability/Live%20Canary%20Plan.md), and the
[CI plan](./docs/reliability/CI%20Plan.md).

### Frontend-only task

Open and work from `Travel App/`

### Backend-only task

Open and work from `Travel Agent/`

## Notes

- Use the parent folder as your Codex project when a task spans both repos.
- Use child repos as the project root when the task is isolated.
- Prefer `git worktree` within each child repo for parallel implementation threads.
