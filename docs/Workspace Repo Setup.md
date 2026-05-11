# Workspace Repo Setup

Travel Workspace is its own Git repository that coordinates two independent
child repositories:

- `Travel Agent`
- `Travel App`

It is not a superproject and does not use Git submodules. The child repo
directories are ignored by the workspace repo and keep their own histories.

## Local Layout

```text
Travel Workspace/
  .git/
  AGENTS.md
  README.md
  Makefile
  docs/
  scripts/
  .github/
  Travel Agent/   # independent git repo, ignored by parent
  Travel App/     # independent git repo, ignored by parent
```

## First-Time Setup

Clone the workspace repo, then bootstrap the child repos:

```bash
git clone <travel-workspace-url> "Travel Workspace"
cd "Travel Workspace"
make bootstrap
make doctor
make contract-check
```

`make bootstrap` clones the default child repos:

```text
https://github.com/fy538/travel-agent.git
https://github.com/fy538/travel-app.git
```

Override them if needed:

```bash
TRAVEL_AGENT_REPO=git@github.com:fy538/travel-agent.git \
TRAVEL_APP_REPO=git@github.com:fy538/travel-app.git \
make bootstrap
```

## Creating The Workspace Remote

If this local workspace repo has no remote yet:

```bash
git remote add origin <travel-workspace-url>
git push -u origin main
```

Recommended repo name:

```text
travel-workspace
```

Keep it private if the docs, workflows, or snapshots should not be public.

## What The Workspace Tracks

Track:

- Cross-repo docs and operating manuals.
- Cross-repo scripts and Makefile targets.
- Reliability traces, prompt templates, and CI.
- Committed OpenAPI snapshot at `docs/openapi.json`.
- Workspace editor/config files intended for the team.

Do not track:

- `Travel Agent/` source files.
- `Travel App/` source files.
- Child repo `.env` files, caches, build output, or dependencies.
- Git submodule pointers.

## Health Checks

Run:

```bash
make doctor
```

The doctor verifies:

- Both child repos exist.
- Child repo source is not tracked by the workspace repo.
- Child repo paths are ignored by workspace Git.
- Key local tools are installed.
- Workspace and child repo remotes are visible.

Run:

```bash
make status
```

That prints Git status for the workspace and both child repos separately.
