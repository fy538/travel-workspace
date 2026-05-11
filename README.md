# Travel Workspace

This folder is the shared workspace for the travel product.

It contains two independent repositories plus the cross-repo tooling that ties them together.

## Repositories

- [Travel Agent](./Travel%20Agent/) — backend API, agent systems, database, OpenAPI source
- [Travel App](./Travel%20App/) — React Native app, UI, generated API types

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
- [docs/openapi.json](./docs/openapi.json) — committed backend schema snapshot
- [travel.code-workspace](./travel.code-workspace) — saved multi-root editor workspace

## Common Commands

```bash
make dev
make dev-backend
make sync-types
make sync-types-snapshot
make typecheck
make doctor
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

### Coordinated branch setup

```bash
./scripts/new-branch.sh trip-group-chat
```

That creates or switches the same branch name in both child repos using the default `codex/` prefix.

### Frontend-only task

Open and work from `Travel App/`

### Backend-only task

Open and work from `Travel Agent/`

## Notes

- Use the parent folder as your Codex project when a task spans both repos.
- Use child repos as the project root when the task is isolated.
- Prefer `git worktree` within each child repo for parallel implementation threads.
