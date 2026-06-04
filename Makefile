# Workspace Makefile — Travel Agent + Travel App
#
# Run from: /Users/feihuyan/Documents/Claude/Travel Workspace/
#
# Each sub-project has its own Makefile with fine-grained targets.
# This file wires the cross-repo workflows that span both repos.

.PHONY: bootstrap dev dev-backend sync-types typecheck doctor status help ci-review
.PHONY: contract-check mock-real-parity golden-path-qa offline-qa reliability-report reliability-gate
.PHONY: preflight-eas fly-secrets

# ── Development ───────────────────────────────────────────────────────────────

bootstrap: ## Clone/validate child repos in this workspace
	@./scripts/bootstrap-repos.sh

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
	@cd travel-app && npx tsc --noEmit

doctor: ## Validate workspace layout and key local tooling
	@./scripts/doctor.sh

# ── Reliability ───────────────────────────────────────────────────────────────

contract-check: ## Verify OpenAPI snapshot matches generated Travel App types
	@./scripts/contract-check.sh

api-coverage-check: ## Verify http.ts only calls URLs that exist in docs/openapi.json
	@python3 ./scripts/api-coverage-check.py

smoke: ## Drive the happy path against a backend (default localhost:8000). Override with PRELAUNCH_HOST=https://...
	@./scripts/smoke-happy-path.sh

pre-launch: offline-qa ## Pre-launch gate: offline QA ladder + happy-path smoke. Override target with PRELAUNCH_HOST.
	@./scripts/smoke-happy-path.sh

preflight-eas: ## Pre-flight before EAS production build (toolchain + projectId + env + tests). MUST be green before running 'eas build'.
	@./scripts/preflight-eas-build.sh

fly-secrets: ## Emit a paste-ready 'fly secrets set' template for first-time Fly.io deploy. Pipe to a file and edit.
	@./scripts/fly-secrets-template.sh

mock-real-parity: ## Check frontend mock/API parity seams without live backend calls
	@./scripts/mock-real-parity.sh

golden-path-qa: ## Run focused deterministic MVP golden-path checks
	@./scripts/golden-path-qa.sh

offline-qa: ## Run the full offline reliability ladder
	@./scripts/offline-qa.sh

reliability-report: ## Print a cheap reliability snapshot without running tests
	@./scripts/reliability-report.sh

reliability-gate: ## Gate on eval reliability baseline — exits 1 if any checks are broken (<50% pass rate)
	@cd travel-agent && PYTHONPATH=. python -m tools.eval.cli reliability \
		--agent concierge \
		--exit-code \
		--verbose

ci-review: ## Nightly CI/CD dashboard across all 3 repos (read the same numbers each day; drift becomes visible)
	@./scripts/ci-review.sh

# ── Tests ─────────────────────────────────────────────────────────────────────

test-backend: ## Run offline backend tests
	@cd travel-agent && PYTHONPATH=. pytest tests/ -q -k "not requires_postgres and not requires_api_keys"

test-frontend: ## Run frontend Jest tests
	@cd travel-app && npx jest --no-coverage

test-all: test-backend test-frontend ## Run all tests (offline)

status: ## Show git status for workspace + child repos
	@echo ""
	@echo "== Workspace =="
	@git status --short || true
	@echo ""
	@echo "== Travel Agent =="
	@cd travel-agent && git status --short || true
	@echo ""
	@echo "== Travel App =="
	@cd travel-app && git status --short || true

# ── Help ──────────────────────────────────────────────────────────────────────

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
