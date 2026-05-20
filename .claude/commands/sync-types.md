Regenerate the OpenAPI snapshot and the Travel App TypeScript types from it.

`docs/openapi.json` (workspace repo) is the single source of truth — every
type-gen tool reads it. `sync-types.sh` regenerates it OFFLINE (no running
backend needed) via Travel Agent's `export_openapi.py`.

Steps:
1. Run `./scripts/sync-types.sh` from the workspace root
2. Review the diff in `Travel App/utils/api/schema.gen.ts`
3. Fix any TypeScript errors surfaced by tsc
4. Commit `docs/openapi.json` and the Travel App changes together

Modes:
- `./scripts/sync-types.sh` — default; regenerate offline from backend models
- `./scripts/sync-types.sh --from-snapshot` — use the committed snapshot as-is
- `./scripts/sync-types.sh --live` — pull from a running backend (curl localhost:8000)
