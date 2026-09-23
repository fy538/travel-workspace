Regenerate the full backend snapshot, active-mobile projection and app types in
this task's coordinated workspace. Follow AGENTS.md's API contract workflow.

1. Verify the workspace and both child checkout revisions/dirty changes.
2. Run `./scripts/sync-types.sh` (offline export by default).
3. Review `docs/openapi.json`, `docs/openapi.app.json`, and
   `travel-app/utils/api/schema.gen.ts`; fix affected consumers and type errors.
4. Run the relevant API operation/contract checks and stage only intended files.

`--from-snapshot` uses committed input; `--live` queries the selected API.
Neither mode certifies a different backend revision automatically.
