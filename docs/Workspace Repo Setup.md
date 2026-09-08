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
  travel-agent/   # independent git repo, ignored by parent
  travel-app/     # independent git repo, ignored by parent
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

- `travel-agent/` source files.
- `travel-app/` source files.
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


## Coordinated lanes and runtime ownership

`scripts/new-worktree.sh <name>` creates all three independent worktrees under
`../<workspace-name>--<name>/`, with lowercase child paths. The default records
each repository's current HEAD; `--base REF` deliberately selects another base.
Existing spaced-name checkouts are adopted by lowercase symlinks during
`make bootstrap`; they are not cloned again or rewritten. Linked worktree `.git`
files are supported. An invalid or already occupied lane fails visibly.

The gitignored `.workspace-lane.json` records base revisions, branch and an
isolated Compose project with distinct Postgres, Qdrant, API and Expo host ports.
It contains no credentials. Set its exclusive `device` assignment before native
QA and coordinate that device with other sessions. Source isolation alone does
not reserve a simulator or a physical phone. Ports are checked again at startup;
if another process claimed one, update the lane assignment before retrying.

Install a Python 3.13 virtual environment and the generated `requirements-dev.txt`
inside this lane's backend; use `npm ci` inside its app. Never share a mutable
node_modules directory across concurrent installs. `make deps-compile-dev` in
the backend regenerates its dev lock from `requirements-dev.in` layered on the
runtime pins. Run `pre-commit install --hook-type pre-commit --hook-type pre-push`
in each repo; declared hook stages do not prove the hooks are installed.

`scripts/dev.sh --print-runtime` prints sanitized resource ownership. Startup
waits for Compose health, applies migrations to that lane's selected local DB,
then waits for API/Expo readiness. A child failure propagates a nonzero status
and stops only process groups launched by that invocation. It leaves Compose
volumes/services intact for reuse; stop the named project deliberately when done.
Do not point this launcher at a production DSN. Shared stacks require an explicit
operator runbook and ownership agreement; the automated lane defaults isolated.

Offline tests need no database. Database acceptance requires an explicitly
provisioned disposable target: set `TEST_DATABASE_URL` and
`TEST_DATABASE_DISPOSABLE=1`; use a separate database/project from dogfood data.
The cleanup fixture only runs for declared DB tests under that opt-in. Record
skips and quarantine; `--run-quarantined` removes the historical xfail mask.

`land-worktree.sh` checks branch identity, cleanliness and integration with
origin/main, then runs `make verify` before optionally publishing branches.
Integrate upstream and refresh immutable cross-repo pins deliberately; it never
rebases one repo behind the other repos' pins, pushes main, mutates a canonical
checkout or deletes a lane. Partial multi-repo pushes cannot be atomic; retain
the lane and report which remote branches were published if a push fails.

## Agent instruction discovery

Each repo owns AGENTS.md; Claude Code imports it through `@AGENTS.md` in its
CLAUDE.md. Codex reads AGENTS files from its project root to the launch directory;
a child launched as a separate Git project must follow its explicit workspace
pointer. `.claude/rules` is Claude-specific path scoping, so AGENTS contains a
manual task-to-rule map for other agents. Check actual discovery from workspace,
child and linked-worktree launch contexts before claiming the setup is active.

The optional Codex SessionStart hook calls the read-only orientation script.
Changed hooks require the user's trust review in `/hooks`; scripts can be tested
without treating static JSON as proof of installed/trusted execution. Existing
local hook overrides must be inspected for duplicate canonical-path commands.
See [Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
and [hook trust and discovery](https://learn.chatgpt.com/docs/hooks).


September 7 discovery check: the bundled Codex 0.153.3 app-server `hooks/list`
resolved this linked workspace worktree's project hook source to the canonical
checkout's `.codex/hooks.json`; it reported that hook as **untrusted**. Child Git
roots returned no workspace hook. Therefore a lane-local JSON edit alone does
not activate the hook. After landing, review the canonical hook in `/hooks`,
restart/resume, and verify its actual source and trust status. Until then run
`python3 scripts/session-context.py` from the workspace (or the same script via
its absolute path from a child). It finds the current coordinated lane from cwd.
This read-only command was tested separately; no hook trust was bypassed.
