# Workspace Makefile — Travel Agent + Travel App
#
# Run from: /Users/feihuyan/Documents/Claude/Travel Workspace/
#
# Each sub-project has its own Makefile with fine-grained targets.
# This file wires the cross-repo workflows that span both repos.

include dogfood.mk

.PHONY: bootstrap dev dev-backend sync-types typecheck doctor status help
.PHONY: new-worktree land-worktree worktrees
.PHONY: contract-check mock-real-parity golden-path-qa journey-wedge-qa offline-qa reliability-report reliability-gate mock-slug-parity
.PHONY: certify-fast certify-logic certify-corpus certify-visual certify-visual-cloud certify-live maestro-flow-check journey-registry-check dogfood-status corpus-check dogfood-city dogfood-promote dogfood-env-check dogfood-journey-live-api qa-persona dogfood-status-sync
.PHONY: preflight-eas fly-secrets verify docs-governance-check docs-child-governance-check docs-inventory-check docs-inventory-report docs-spine-check docs-status-check docs-status-sync docs-links-check docs-check compatibility-check card-arrival-check

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

# ── Concurrent agent lanes ──────────────────────────────────────────────────────

new-worktree: ## Create an isolated worktree lane in both repos: make new-worktree NAME=my-feature
	@./scripts/new-worktree.sh $(NAME)

land-worktree: ## Rebase, push to main, and tear down a worktree lane: make land-worktree NAME=my-feature
	@./scripts/land-worktree.sh $(NAME)

worktrees: ## List active worktree lanes for both child repos
	@echo "== Travel Agent =="
	@cd travel-agent && git worktree list
	@echo ""
	@echo "== Travel App =="
	@cd travel-app && git worktree list

# ── Reliability ───────────────────────────────────────────────────────────────

contract-check: ## Verify full OpenAPI → app projection → generated types
	@./scripts/contract-check.sh

api-coverage-check: ## Audit operation consumers, lifecycle policy, and OpenAPI method coverage
	@python3 ./scripts/api_contract_audit.py

smoke: ## Drive the happy path against a backend (default localhost:8000). Override with PRELAUNCH_HOST=https://...
	@./scripts/smoke-happy-path.sh

pre-launch: verify ## Pre-launch gate: verify + happy-path smoke. Override target with PRELAUNCH_HOST.
	@./scripts/smoke-happy-path.sh

preflight-eas: ## Pre-flight before EAS production build (toolchain + projectId + env + tests). MUST be green before running 'eas build'.
	@./scripts/preflight-eas-build.sh

fly-secrets: ## Emit a paste-ready 'fly secrets set' template for first-time Fly.io deploy. Pipe to a file and edit.
	@./scripts/fly-secrets-template.sh

mock-real-parity: ## Moved — use `make verify` (mock/API seam tests included)
	@echo "⚠ mock-real-parity merged into make verify (architecture-simplification 2026-07)"
	@$(MAKE) verify

golden-path-qa: ## Deprecated — use `make journey-wedge-qa`
	@echo "⚠ golden-path-qa renamed to journey-wedge-qa (architecture-simplification 2026-07)"
	@$(MAKE) journey-wedge-qa

journey-wedge-qa: ## Journey wedge gate: J02/J05/J06 scenario pytest + mock-walk Jest
	@chmod +x ./scripts/golden-path-qa.sh
	@./scripts/golden-path-qa.sh

mock-slug-parity: ## Gate: dogfood corpus city slugs have mock angle + destination fixtures
	@chmod +x ./scripts/mock-slug-parity-check.sh
	@./scripts/mock-slug-parity-check.sh

offline-qa: ## Moved — use `make verify`
	@echo "⚠ offline-qa merged into make verify (architecture-simplification 2026-07)"
	@$(MAKE) verify

reliability-report: ## Print a cheap reliability snapshot without running tests
	@./scripts/reliability-report.sh

reliability-gate: ## Gate on eval reliability baseline — exits 1 if any checks are broken (<50% pass rate)
	@cd travel-agent && PYTHONPATH=. python -m tools.eval.cli reliability \
		--agent concierge \
		--exit-code \
		--verbose

# ── Tests ─────────────────────────────────────────────────────────────────────

test-backend: ## Run offline backend tests
	@cd travel-agent && SKIP_AUTH=true PYTHONPATH=. pytest tests/ -q -k "not requires_postgres and not requires_api_keys"

test-frontend: ## Run frontend Jest tests
	@cd travel-app && npx jest --no-coverage

test-all: test-backend test-frontend ## Run all tests (offline)

certify-fast: ## Tier-1 certify ladder: corpus-check + contract + journey Jest + maestro-flow-check + offline backend pytest
	@$(MAKE) corpus-check
	@$(MAKE) contract-check
	@$(MAKE) journey-registry-check
	@cd travel-app && npm run --silent qa:logic:check-drift
	@cd travel-app && npm test -- __tests__/journeys/ --runInBand
	@$(MAKE) maestro-flow-check
	@$(MAKE) test-backend

journey-registry-check: ## Gate: journeys.yaml ↔ docs ↔ README ↔ persona-cert agree on the journey set (offline, no DB)
	@python3 scripts/check_journey_registry.py

flag-registry-check: ## Gate: no feature flag in docs/flags/registry.yaml is past its review/removal date (offline, no DB)
	@python3 scripts/check_flag_registry.py

docs-governance-check: ## Gate: new workspace Markdown files carry lifecycle metadata
	@python3 scripts/check_docs.py --staged-new

docs-inventory-check: ## Gate: every workspace Markdown file has one reviewed disposition
	@python3 scripts/check_doc_inventory.py --steady

docs-inventory-report: ## Print the complete documentation disposition report
	@python3 scripts/check_doc_inventory.py --details

docs-spine-check: ## Gate: the eight canonical documentation entry points exist and are indexed
	@python3 scripts/check_docs_spine.py

docs-status-check: ## Gate: generated current-state signals match executable registries
	@python3 scripts/render_current_state.py

docs-status-sync: ## Refresh the generated current-state signal table
	@python3 scripts/check_docs.py --write-status

docs-child-governance-check: ## Gate: new child-repo docs satisfy workspace lifecycle metadata
	@python3 scripts/check_child_doc_governance.py

docs-links-check: ## Gate: relative links in living workspace docs resolve
	@python3 scripts/check_living_doc_links.py

docs-check: ## Run all documentation governance gates
	@python3 scripts/check_docs.py --all

maestro-flow-check: ## Gate: Maestro structure, lane metadata, references, configs, and CLI semantics
	@python3 scripts/validate-maestro-flows.py --app-dir travel-app
	@cd travel-app && npm run --silent maestro:metadata:check
	@cd travel-app && scripts/maestro/check-syntax.sh

compatibility-check: ## Gate: every marked compatibility exception has an owned, expiring ledger entry
	@python3 scripts/check_compatibility_ledger.py

card-arrival-check: ## Gate: generated frontend/backend card-arrival registries match the workspace contract
	@python3 scripts/sync-card-arrival-contract.py --check

certify-logic: ## Tier-2 certify ladder: journey scenario pytest (requires Postgres, excludes corpus-dependent tests)
	@cd travel-agent && SKIP_AUTH=true PYTHONPATH=. pytest tests/scenarios/ \
	  -m "requires_postgres and not requires_dogfood_wedge" -q

certify-corpus: ## Tier-2b certify ladder: discover_queries compose tests (requires seeded wedge corpus)
	@echo "Running corpus-dependent discover tests (requires 'make dogfood-city CITY=lisbon APPLY=1 ENRICH=1')..."
	@cd travel-agent && SKIP_AUTH=true PYTHONPATH=. pytest tests/scenarios/ \
	  -m requires_dogfood_wedge -v --tb=short

certify-visual: ## Tier-3 certify ladder: deterministic PR-smoke Maestro lane (needs simulator + app)
	@export JAVA_HOME="$${JAVA_HOME:-/opt/homebrew/opt/openjdk}" && \
	 export PATH="$$JAVA_HOME/bin:$$HOME/.maestro/bin:$$PATH" && \
	 cd travel-app && npm run --silent visual-qa:pr

certify-visual-cloud: ## Activate Maestro Cloud PR gate: add secrets to GitHub repo settings
	@echo "Visual QA cloud gate (.github/workflows/visual-qa-cloud.yml) is ready."
	@echo "Add three secrets to this workspace GitHub repo → Secrets and variables → Actions:"
	@echo "  MAESTRO_CLOUD_API_KEY  — from console.maestro.dev (create a project, copy the API key)"
	@echo "  MAESTRO_CLOUD_PROJECT_ID — Maestro Cloud workspace project ID"
	@echo "  EXPO_TOKEN             — from expo.dev → account settings → access tokens"
	@echo "Once set, PRs will auto-gate on the pr-smoke lane via Maestro Cloud managed devices."
	@echo "The workflow skips gracefully if the secret is absent, so it never blocks PRs before configured."

certify-live: ## Tier-4 dogfood preflight + live-walk checklist (human: two Clerk accounts)
	@chmod +x ./scripts/certify-live.sh ./scripts/attic/seed-s4-fly.sh
	@./scripts/certify-live.sh

design-refresh: ## Close the design-alignment freshness loop: fingerprint canon, list stale surfaces, re-capture + auto-carry/queue-for-judging (needs simulator + Metro)
	@cd travel-app && npm run --silent design:fingerprint
	@cd travel-app && npm run --silent design:routes
	@cd travel-app && npm run --silent design:stale
	@cd travel-app && npm run --silent qa:refresh
	@cd travel-app && npm run --silent design:status
	@cd travel-app && npm run --silent design:briefs
	@echo ""
	@echo "STATUS.md + design-briefs/ regenerated. Open the judge queue printed above (if any) — see"
	@echo "docs/surfaces/_agent-verdict-protocol.md 'Batch judging a refresh queue' for the ritual."

design-refresh-dry: ## Same as design-refresh but with no simulator/Maestro (--dry-run) — verifies the pipeline wiring only
	@cd travel-app && npm run --silent design:fingerprint
	@cd travel-app && npm run --silent design:routes
	@cd travel-app && npm run --silent design:stale
	@cd travel-app && node scripts/design-alignment/refresh-stale.mjs --dry-run
	@cd travel-app && npm run --silent design:status
	@cd travel-app && npm run --silent design:briefs

corpus-check: ## Gate: every dogfood manifest slug resolves in DB or staging (wedge by default)
	@chmod +x ./scripts/corpus-check.sh
	@./scripts/corpus-check.sh

dogfood-city: ## Connect corpus + seed a city. Usage: make dogfood-city CITY=lisbon [APPLY=1] [ENRICH=1] [PROFILE=local|fly]
	@chmod +x ./scripts/dogfood-city.sh ./scripts/dogfood-env.sh
	@APPLY="$(APPLY)" ENRICH="$(ENRICH)" PROFILE="$(PROFILE)" ./scripts/dogfood-city.sh CITY=$(CITY)

dogfood-promote: ## Promote city pack to Fly + cloud Qdrant. Usage: make dogfood-promote CITY=lisbon [APPLY=1]
	@chmod +x ./scripts/dogfood-promote.sh ./scripts/dogfood-env.sh
	@APPLY="$(APPLY)" ./scripts/dogfood-promote.sh CITY=$(CITY)

dogfood-env-check: ## Print dogfood Postgres+Qdrant stack pairing for PROFILE=local|fly
	@chmod +x ./scripts/dogfood-env-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" APPLY="$(APPLY)" ./scripts/dogfood-env-check.sh

dogfood-journey-live-api: ## Two-persona live API cert for J02/J04/J05/J10 (TestClient or Fly+JWT) — active toward the live-transport gap
	@chmod +x ./scripts/dogfood-journey-live-api.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/dogfood-journey-live-api.sh

dogfood-status: ## Validate dogfood manifests and print scenario/pack readiness
	@chmod +x ./scripts/dogfood-status.sh ./scripts/attic/seed-s4-local.sh ./scripts/attic/seed-s4-fly.sh
	@./scripts/dogfood-status.sh

qa-persona: ## Full per-persona QA spine: content gates + journeys + visual walk plan (token-free). Usage: make qa-persona PERSONA=mara [GATE=1]
	@python scripts/qa_persona.py --persona $(PERSONA) $(if $(GATE),--gate,)

dogfood-status-sync: ## Regenerate the auto:persona-cert block in docs/journeys/STATUS.md from the seeded world (token-free). CHECK=1 = CI drift guard.
	@python scripts/sync_journey_status.py $(if $(CHECK),--check,)

# ── Composite gate ─────────────────────────────────────────────────────────────

verify: ## Single cross-repo pre-push gate (absorbs offline-qa + mock-real-parity)
	@echo "▸ Workspace doctor..."
	@$(MAKE) doctor
	@echo "▸ Backend CI (travel-agent: ruff + boundaries + gates + mypy + offline tests)..."
	@$(MAKE) -C travel-agent ci
	@echo "▸ Contract drift (OpenAPI snapshot ↔ generated types)..."
	@$(MAKE) contract-check
	@echo "▸ API operation registry + consumer coverage..."
	@$(MAKE) api-coverage-check
	@echo "▸ Frontend typecheck (travel-app: tsc --noEmit)..."
	@$(MAKE) typecheck
	@echo "▸ Journey mock-walk (tier 1 Jest)..."
	@cd travel-app && npm test -- __tests__/journeys/ --runInBand
	@echo "▸ Mock/API seam tests..."
	@cd travel-app && npx jest --runInBand \
		__tests__/utils/api/mock.test.ts \
		__tests__/utils/api/http.test.ts \
		__tests__/data/notifications.test.ts \
		__tests__/data/proposals.test.ts \
		__tests__/data/privacy.test.ts \
		__tests__/data/planState.test.ts
	@echo "▸ Frontend offline tests..."
	@cd travel-app && npm run test:offline
	@echo "▸ Workspace governance and evidence-integrity gates..."
	@$(MAKE) maestro-flow-check journey-registry-check flag-registry-check \
		docs-spine-check docs-status-check docs-links-check docs-child-governance-check \
		compatibility-check card-arrival-check
	@echo "✓ verify: all cross-repo gates green"

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
	@grep -hE '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
