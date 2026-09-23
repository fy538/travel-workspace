# AGENTS.md — Travel Workspace

This is the cross-repository coordination workspace for Vesper. The workspace,
`travel-agent/` (Python/FastAPI/Postgres/Qdrant), and `travel-app/` (React Native/
Expo/TypeScript) are three independent Git repositories. Keep their histories
separate; never convert the children into submodules. Shared docs, scripts,
contracts and meta tooling belong here; product source belongs in the children.

## Task context

1. Establish actual paths, branches, HEADs, worktrees and dirty changes before
   substantive edits: `git status --short`, `git branch -a`, `git worktree list`
   in each affected repo. `python3 scripts/session-context.py` gives a bounded
   orientation from this workspace or a descendant. Committed history and
   uncommitted work both matter; remembered status is only a dated observation.
2. Use `docs/README.md` to find the relevant authority. Read the affected child's
   `AGENTS.md`, its Task Intake, owner contract and nearest implementation/tests.
   Onboarding is for setup or unfamiliar architecture; expand context when the
   task or an explicit rule requires it. Claude-specific adapters are in
   `CLAUDE.md`; shared rules are owned here and in the child AGENTS files.
3. State intended behavior, owning layer and acceptance evidence before changing
   behavior. One sentence is enough for a small change. Classify uncertainty as
   unresolved until evidence supports or refutes it; reviewer votes are not proof.
4. Use an isolated coordinated lane when another session owns the same files.
   `scripts/new-worktree.sh <name>` creates a workspace plus both child worktrees
   from their recorded current HEADs. `--base REF` is explicit. Run cross-repo
   commands inside that lane, never against an unrelated canonical sibling.

For Chat input, share/intake, memory write-back, Occasion contribution, receipts,
correction, audience effects or delegated action, read
`docs/systems/contribution-and-consequence.md`: it owns gesture resolution,
five-axis authority, owner handoff and causal repair across repositories.

## API contract

The complete backend snapshot is `docs/openapi.json`. The workspace derives
`docs/openapi.app.json` from active mobile operations and their governance;
`travel-app/utils/api/schema.gen.ts` is generated from that projection.

After backend models/routes change:

1. Update backend implementation and tests in this lane's `travel-agent/`.
2. Run `./scripts/sync-types.sh` from this lane's workspace. It exports offline
   by default. `--from-snapshot` regenerates from committed input; `--live` uses
   an explicitly selected running backend.
3. Review the full snapshot, app projection, generated types and consumers
   together. Resolve frontend breakage before finishing.
4. Run `make api-coverage-check` after adding, adopting or retiring an endpoint.

Never hand-edit generated types or duplicate backend wire models in TypeScript.
UI-specific models and reviewed adapters follow the app's schema-bridge policy.

## Verification and delivery

Run focused checks during iteration and retain the relevant Task Intake contract,
integration, behavioral and visual evidence. `make verify` remains the coordinated
pre-push gate; `verify-changed` is experimental and does not replace it.

For setup or verification changes, prove the command in its intended environment:
record checkout/tool versions, required services and packaged inputs. Distinguish
a defined check, an executed check and a required merge check. Missing tools,
crashes and unavailable services are unverified/error states. Consequential
checker changes need representative valid, violating and tool-failure cases.

Report exact commands, revisions and evidence boundaries: passed, failed,
blocked, unrun or stale. Name skipped/quarantined tests. Mocked tests, carried
verdicts and another agent's review prove only their stated boundaries. Record
measurements with `scripts/measure_verification.py`; do not infer productivity
improvements from fewer instructions or more tests.

Update the existing owner doc/check when a defect exposes missing context.
Preserve its rationale; avoid adding a permanent global rule for every incident.
Follow `docs/governance/README.md` for documentation lifecycle and admission.

## Git and runtime ownership

- Name branches descriptively with the `codex/` prefix unless the task specifies
  otherwise. A commit lands on the branch currently checked out; verify it.
- Stage explicit filenames; never `git add -A` or `git add .`. Preserve another
  session's edits and branches. Do not switch or fast-forward its checkout.
- `scripts/land-worktree.sh <name>` requires clean, current lane branches and
  runs `make verify` before any publishing. `--publish` pushes lane branches for
  protected-main PR review. It does not push main or remove worktrees.
- A worktree isolates files, not services. The lane's `.workspace-lane.json`
  records Compose project, Postgres/Qdrant/API/Expo ports and exclusive device.
  Check `scripts/dev.sh --print-runtime` before starting it. Details and legacy
  layout support live in `docs/Workspace Repo Setup.md`.
- Backend DB tests require `TEST_DATABASE_URL` and `TEST_DATABASE_DISPOSABLE=1`.
  Never run fixture cleanup against an ambient development/production database.
- Existing user authorization applies to necessary implementation work. Preserve
  founder review for unresolved product/authority/architecture choices; do not
  ask the same permission again just because an authorized fix touches a named file.
  Deployment, publication and product-policy changes need their own authorization.

## Commands and setup

Run from the actual workspace/lane root, not a hardcoded personal path:

```bash
make bootstrap             # clone/adopt lowercase independent child checkouts
make doctor                # source/tooling checks; services are opt-in
make dev-backend            # isolated infra + migrations + supervised API
make dev                   # also starts Expo; select the intended device
make sync-types            # offline backend export + projection + frontend types
make sync-types-snapshot   # regenerate from committed full snapshot
make typecheck
make test-backend           # offline; no DB probing or cleanup
make test-frontend
make verify
make status
```

Private child access, Python 3.13, Node/Expo prerequisites and cloud setup are in
`README.md` and `docs/Workspace Repo Setup.md`. Actual GitHub check names, token
requirements and tested revision tuples live in `docs/reliability/CI Plan.md`.
