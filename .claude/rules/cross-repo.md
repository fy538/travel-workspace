# Cross-Repo Rules

When working across Travel Agent (backend) and Travel App (frontend):

## API Contract

- Backend types are canonical. TypeScript types in Travel App that mirror backend
  models must be **generated**, not hand-written.
- Generated file: `Travel App/utils/api/schema.gen.ts` — never edit this manually.
- Committed snapshot: `docs/openapi.json` (workspace repo) — the SINGLE source of
  truth that every type-gen tool reads (sync-types, contract-check,
  api-coverage-check, and the Travel App npm scripts via `../docs/openapi.json`).
  Regenerate by running `./scripts/sync-types.sh`.
- `Travel Agent/docs/openapi.json` is a local-only artifact (`make export-openapi`);
  nothing cross-repo consumes it. Don't treat it as the contract.

## Sync Workflow

```bash
# After any backend model or route change:
./scripts/sync-types.sh
# Then fix any TypeScript errors before committing.
```

## Import conventions in Travel App

```typescript
// Generated backend types (from Pydantic models):
import type { components } from '@/utils/api/schema.gen'
type Trip = components['schemas']['Trip']

// Hand-written UI types (display, component props) stay in types/:
import type { APITrip } from '@/types/trip'  // Only for UI-specific fields
```

## Never

- Hand-write a TypeScript type that duplicates a Pydantic model
- Edit schema.gen.ts directly
- Add a backend field without running sync-types
