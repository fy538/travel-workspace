# Workspace Makefile — Travel Agent + Travel App
#
# Run from: /Users/feihuyan/Documents/Claude/Travel Workspace/
#
# Each sub-project has its own Makefile with fine-grained targets.
# This file wires the cross-repo workflows that span both repos.

.PHONY: bootstrap dev dev-backend sync-types typecheck doctor status help ci-review
.PHONY: new-worktree land-worktree worktrees
.PHONY: contract-check mock-real-parity golden-path-qa journey-wedge-qa offline-qa reliability-report reliability-gate mock-slug-parity
.PHONY: certify-fast certify-logic certify-corpus certify-visual certify-visual-cloud certify-live maestro-flow-check journey-registry-check dogfood-status seed-s4-local seed-s4-fly corpus-check dogfood-city dogfood-promote dogfood-env-check dogfood-fly-smoke dogfood-five-pack-verify dogfood-five-pack-live-api dogfood-five-pack-simulator dogfood-journey-live-api dogfood-journey-j04-chat-eval dogfood-maestro-s4-local dogfood-maestro-fly import-latent-corpus tier-a-spot-check tier-b-spot-check qa-persona dogfood-status-sync
.PHONY: preflight-eas fly-secrets verify

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

golden-path-qa: journey-wedge-qa ## Deprecated alias — use journey-wedge-qa or certify-logic

journey-wedge-qa: ## Journey wedge gate: J02/J05/J06 scenario pytest + mock-walk Jest
	@chmod +x ./scripts/golden-path-qa.sh
	@./scripts/golden-path-qa.sh

mock-slug-parity: ## Gate: dogfood corpus city slugs have mock angle + destination fixtures
	@chmod +x ./scripts/mock-slug-parity-check.sh
	@./scripts/mock-slug-parity-check.sh

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

maestro-flow-check: ## Gate: every .maestro flow parses + visual-qa script refs resolve (offline, no simulator)
	@python3 scripts/validate-maestro-flows.py --app-dir travel-app

certify-logic: ## Tier-2 certify ladder: journey scenario pytest (requires Postgres, excludes corpus-dependent tests)
	@cd travel-agent && SKIP_AUTH=true PYTHONPATH=. pytest tests/scenarios/ \
	  -m "requires_postgres and not requires_dogfood_wedge" -q

certify-corpus: ## Tier-2b certify ladder: discover_queries compose tests (requires seeded wedge corpus)
	@echo "Running corpus-dependent discover tests (requires 'make dogfood-city CITY=lisbon APPLY=1 ENRICH=1')..."
	@cd travel-agent && SKIP_AUTH=true PYTHONPATH=. pytest tests/scenarios/ \
	  -m requires_dogfood_wedge -v --tb=short

certify-visual: ## Tier-3 certify ladder: wedge Maestro flows (needs simulator + Metro)
	@export JAVA_HOME="$${JAVA_HOME:-/opt/homebrew/opt/openjdk}" && \
	 export PATH="$$JAVA_HOME/bin:$$HOME/.maestro/bin:$$PATH" && \
	 cd travel-app && npm run --silent visual-qa:wedge

certify-visual-cloud: ## Activate Maestro Cloud PR gate: add secrets to GitHub repo settings
	@echo "Visual QA cloud gate (.github/workflows/visual-qa-cloud.yml) is ready."
	@echo "Add two secrets to the fy538/travel-app GitHub repo settings → Secrets and variables → Actions:"
	@echo "  MAESTRO_CLOUD_API_KEY  — from console.maestro.dev (create a project, copy the API key)"
	@echo "  EXPO_TOKEN             — from expo.dev → account settings → access tokens"
	@echo "Once set, PRs will auto-gate on wedge flows 24+25 via Maestro Cloud managed devices."
	@echo "The workflow skips gracefully if the secret is absent, so it never blocks PRs before configured."

certify-live: ## Tier-4 dogfood preflight + live-walk checklist (human: two Clerk accounts)
	@chmod +x ./scripts/certify-live.sh ./scripts/seed-s4-fly.sh
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

import-latent-corpus: ## Phase 2c catalog import. Usage: make import-latent-corpus TIER=a|b [APPLY=1] [CITY=paris] [PROFILE=local|fly] [GLOBAL_EMBED_ONLY=1]
	@chmod +x ./scripts/import-latent-corpus.sh ./scripts/dogfood-env.sh
	@APPLY="$(APPLY)" PROFILE="$(PROFILE)" GLOBAL_EMBED_ONLY="$(GLOBAL_EMBED_ONLY)" ./scripts/import-latent-corpus.sh TIER=$(or $(TIER),a) $(if $(CITY),CITY=$(CITY),)

tier-a-spot-check: ## Verify Tier A cities in PG + Qdrant. Usage: make tier-a-spot-check [PROFILE=local|fly]
	@chmod +x ./scripts/tier-a-spot-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/tier-a-spot-check.sh

tier-b-spot-check: ## Verify Tier B cities in PG + Qdrant. Usage: make tier-b-spot-check [PROFILE=local|fly]
	@chmod +x ./scripts/tier-b-spot-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/tier-b-spot-check.sh

dogfood-promote: ## Promote city pack to Fly + cloud Qdrant. Usage: make dogfood-promote CITY=lisbon [APPLY=1]
	@chmod +x ./scripts/dogfood-promote.sh ./scripts/dogfood-env.sh
	@APPLY="$(APPLY)" ./scripts/dogfood-promote.sh CITY=$(CITY)

dogfood-env-check: ## Print dogfood Postgres+Qdrant stack pairing for PROFILE=local|fly
	@chmod +x ./scripts/dogfood-env-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" APPLY="$(APPLY)" ./scripts/dogfood-env-check.sh

dogfood-fly-smoke: ## Automated Fly substrate smoke after dogfood-promote (API + Fly DB + Rome bridge)
	@chmod +x ./scripts/dogfood-fly-smoke.sh ./scripts/dogfood-env.sh ./scripts/dogfood-five-pack-verify.sh
	@./scripts/dogfood-fly-smoke.sh

dogfood-five-pack-verify: ## Five-pack substrate checks (trips, itinerary venues, discover compose) on PROFILE=fly|local
	@chmod +x ./scripts/dogfood-five-pack-verify.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/dogfood-five-pack-verify.sh

dogfood-five-pack-live-api: ## Five-pack live HTTP checks (TestClient local or Fly with PRELAUNCH_JWT)
	@chmod +x ./scripts/dogfood-five-pack-live-api.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/dogfood-five-pack-live-api.sh

dogfood-five-pack-simulator: ## Local TestClient API + optional Maestro wedge (RUN_MAESTRO=0 to skip UI)
	@chmod +x ./scripts/dogfood-five-pack-simulator.sh ./scripts/dogfood-five-pack-live-api.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" ./scripts/dogfood-five-pack-simulator.sh

dogfood-journey-live-api: ## Two-persona live API cert for J02/J04/J05/J10 (TestClient or Fly+JWT)
	@chmod +x ./scripts/dogfood-journey-live-api.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/dogfood-journey-live-api.sh

dogfood-journey-j04-chat-eval: ## J04 I4 egress eval on S4 trip (substrate + group history)
	@chmod +x ./scripts/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/dogfood-journey-j04-chat-eval.sh

dogfood-maestro-s4-local: ## Maestro 26 + J04 eval on local real API (SKIP_AUTH as Mara)
	@chmod +x ./scripts/dogfood-maestro-s4-local.sh ./scripts/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" ./scripts/dogfood-maestro-s4-local.sh

dogfood-maestro-fly: ## Maestro 26 + J04 eval on Fly (needs PRELAUNCH_JWT_MARA)
	@chmod +x ./scripts/dogfood-maestro-fly.sh ./scripts/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-journey-live-api.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" PRELAUNCH_JWT_MARA="$(PRELAUNCH_JWT_MARA)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/dogfood-maestro-fly.sh

dogfood-status: ## Validate dogfood manifests and print scenario/pack readiness
	@chmod +x ./scripts/dogfood-status.sh ./scripts/seed-s4-local.sh ./scripts/seed-s4-fly.sh
	@./scripts/dogfood-status.sh

qa-persona: ## Full per-persona QA spine: content gates + journeys + visual walk plan (token-free). Usage: make qa-persona PERSONA=mara [GATE=1]
	@python scripts/qa_persona.py --persona $(PERSONA) $(if $(GATE),--gate,)

dogfood-status-sync: ## Regenerate the auto:persona-cert block in docs/journeys/STATUS.md from the seeded world (token-free). CHECK=1 = CI drift guard.
	@python scripts/sync_journey_status.py $(if $(CHECK),--check,)

seed-s4-local: ## Seed S4 lisbon-phase1 to local Postgres (requires vesper DB)
	@chmod +x ./scripts/seed-s4-local.sh
	@./scripts/seed-s4-local.sh

seed-s4-fly: ## Seed S4 to Fly Postgres (dry-run; SEED_S4_FLY_APPLY=1 to write)
	@./scripts/seed-s4-fly.sh

# ── Composite gate ─────────────────────────────────────────────────────────────

verify: ## Single cross-repo "is it green?" gate: backend CI + frontend typecheck + contract drift + API coverage + frontend tests
	@echo "▸ Backend CI (travel-agent: ruff + boundaries + gates + mypy + offline tests)..."
	@$(MAKE) -C travel-agent ci
	@echo "▸ Frontend typecheck (travel-app: tsc --noEmit)..."
	@$(MAKE) typecheck
	@echo "▸ Contract drift (OpenAPI snapshot ↔ generated types)..."
	@$(MAKE) contract-check
	@echo "▸ API coverage (http.ts URLs exist in docs/openapi.json)..."
	@$(MAKE) api-coverage-check
	@echo "▸ Frontend tests (Jest)..."
	@$(MAKE) test-frontend
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
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
