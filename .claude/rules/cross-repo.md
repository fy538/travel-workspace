# Cross-repository contract routing

Follow the workspace AGENTS.md API workflow. The full backend source is
`docs/openapi.json`; the generated active-mobile projection is
`docs/openapi.app.json`; the app consumes `travel-app/utils/api/schema.gen.ts`.

Run `./scripts/sync-types.sh` from the coordinated workspace containing this
change's `travel-agent/` and `travel-app/` checkouts. It exports offline by
default. Review all three artifacts and affected consumers. UI-only models and
reviewed adapters follow the schema-bridge manifest; wire models are generated.
