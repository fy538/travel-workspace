# Workspace Makefile — Travel Agent + Travel App
#
# Run from: /Users/feihuyan/Documents/Claude/Projects/
#
# Each sub-project has its own Makefile with fine-grained targets.
# This file wires the cross-repo workflows that span both repos.

.PHONY: dev dev-backend sync-types typecheck doctor status help

# ── Development ───────────────────────────────────────────────────────────────

dev: ## Start all services: Docker infra + API server + Expo iOS simulator
	@./scripts/dev.sh

dev-backend: ## Start infra + API only (no Expo)
	@./scripts/dev.sh --no-expo

# ── Types ─────────────────────────────────────────────────────────────────────

sync-types: ## Sync OpenAPI schema → Travel App TypeScript types (requires running backend)
	@./scripts/sync-types.sh

sync-types-snapshot: ## Sync types from committed snapshot (no backend needed)
	@./scripts/sync-types.sh --from-snapshot

typecheck: ## Type-check Travel App (tsc --noEmit)
	@cd "Travel App" && npx tsc --noEmit

doctor: ## Validate workspace layout and key local tooling
	@./scripts/doctor.sh

# ── Tests ─────────────────────────────────────────────────────────────────────

test-backend: ## Run offline backend tests
	@cd "Travel Agent" && PYTHONPATH=. pytest tests/ -q -k "not requires_postgres and not requires_api_keys"

test-frontend: ## Run frontend Jest tests
	@cd "Travel App" && npx jest --no-coverage

test-all: test-backend test-frontend ## Run all tests (offline)

status: ## Show git status for workspace + child repos
	@echo ""
	@echo "== Workspace =="
	@git status --short || true
	@echo ""
	@echo "== Travel Agent =="
	@cd "Travel Agent" && git status --short || true
	@echo ""
	@echo "== Travel App =="
	@cd "Travel App" && git status --short || true

# ── Help ──────────────────────────────────────────────────────────────────────

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
