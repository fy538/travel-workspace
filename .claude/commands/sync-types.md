Sync the OpenAPI schema from Travel Agent and regenerate TypeScript types in Travel App.

Steps:
1. Run `./scripts/sync-types.sh` from the workspace root (`/Users/feihuyan/Documents/Claude/Projects/`)
2. If the backend isn't running, use `./scripts/sync-types.sh --from-snapshot` instead
3. Review the diff in `Travel App/utils/api/schema.gen.ts`
4. Fix any TypeScript errors surfaced by tsc
5. Commit `docs/openapi.json` and the Travel App changes together

If you're unsure whether the backend is running, check with:
```bash
curl --silent http://localhost:8000/health | head -5
```
