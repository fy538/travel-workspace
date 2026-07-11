# dogfood.mk — completed-campaign dogfood targets
#
# Included from the main Makefile. These targets belong to the Tier A/B
# corpus import + five-pack (Lisbon/Rome/Istanbul/Tokyo/Brooklyn) dogfood
# campaigns, all marked PASSED/COMPLETE 2026-06-29 in
# docs/journeys/STATUS.md. They're kept — a future dogfood cohort or a new
# corpus tier will reuse this machinery — but split out of the main
# Makefile so `make help`'s day-to-day surface isn't dominated by a
# finished campaign's tooling.
#
# Reusable city machinery that ISN'T campaign-specific stays in the main
# Makefile: dogfood-city, dogfood-promote, corpus-check, dogfood-env-check,
# dogfood-status, dogfood-status-sync, qa-persona, mock-slug-parity.
#
# Also NOT here despite living in the same dogfood/ family: certify-live
# and dogfood-journey-live-api. Both are active tooling for the still-open
# device-certification / live-transport gap (see Owner Action Items +
# docs/journeys/STATUS.md "Live HTTP" row) — not completed-campaign
# residue. They stay in the main Makefile.
#
# From the 2026-07-11 architecture-simplification audit, Tier 1.
# Campaign shell scripts live in scripts/attic/; this file keeps their Make targets.

.PHONY: import-latent-corpus tier-a-spot-check tier-b-spot-check dogfood-fly-smoke
.PHONY: dogfood-five-pack-verify dogfood-five-pack-live-api dogfood-five-pack-simulator
.PHONY: seed-s4-local seed-s4-fly dogfood-maestro-s4-local dogfood-maestro-fly
.PHONY: dogfood-journey-j04-chat-eval

import-latent-corpus: ## Phase 2c catalog import (Tier A/B, complete 2026-06-29). Usage: make import-latent-corpus TIER=a|b [APPLY=1] [CITY=paris] [PROFILE=local|fly] [GLOBAL_EMBED_ONLY=1]
	@chmod +x ./scripts/attic/import-latent-corpus.sh ./scripts/dogfood-env.sh
	@APPLY="$(APPLY)" PROFILE="$(PROFILE)" GLOBAL_EMBED_ONLY="$(GLOBAL_EMBED_ONLY)" ./scripts/attic/import-latent-corpus.sh TIER=$(or $(TIER),a) $(if $(CITY),CITY=$(CITY),)

tier-a-spot-check: ## Verify Tier A cities in PG + Qdrant (PASSED 2026-06-29). Usage: make tier-a-spot-check [PROFILE=local|fly]
	@chmod +x ./scripts/attic/tier-a-spot-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/attic/tier-a-spot-check.sh

tier-b-spot-check: ## Verify Tier B cities in PG + Qdrant (PASSED 2026-06-29). Usage: make tier-b-spot-check [PROFILE=local|fly]
	@chmod +x ./scripts/attic/tier-b-spot-check.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/attic/tier-b-spot-check.sh

dogfood-fly-smoke: ## Automated Fly substrate smoke after dogfood-promote (PASSED 2026-06-29)
	@chmod +x ./scripts/attic/dogfood-fly-smoke.sh ./scripts/dogfood-env.sh ./scripts/attic/dogfood-five-pack-verify.sh
	@./scripts/attic/dogfood-fly-smoke.sh

dogfood-five-pack-verify: ## Five-pack substrate checks — trips/itinerary venues/discover compose (COMPLETE 2026-06-29). PROFILE=fly|local
	@chmod +x ./scripts/attic/dogfood-five-pack-verify.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" ./scripts/attic/dogfood-five-pack-verify.sh

dogfood-five-pack-live-api: ## Five-pack live HTTP checks (TestClient local or Fly with PRELAUNCH_JWT)
	@chmod +x ./scripts/attic/dogfood-five-pack-live-api.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/attic/dogfood-five-pack-live-api.sh

dogfood-five-pack-simulator: ## Local TestClient API + optional Maestro wedge (RUN_MAESTRO=0 to skip UI)
	@chmod +x ./scripts/attic/dogfood-five-pack-simulator.sh ./scripts/attic/dogfood-five-pack-live-api.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" ./scripts/attic/dogfood-five-pack-simulator.sh

dogfood-journey-j04-chat-eval: ## J04 I4 egress eval on S4 trip (substrate + group history)
	@chmod +x ./scripts/attic/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-env.sh
	@PROFILE="$(PROFILE)" TRANSPORT="$(TRANSPORT)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/attic/dogfood-journey-j04-chat-eval.sh

dogfood-maestro-s4-local: ## Optional UI spot-check: Maestro 26 + J04 eval on local real API (SKIP_AUTH as Mara)
	@chmod +x ./scripts/attic/dogfood-maestro-s4-local.sh ./scripts/attic/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" ./scripts/attic/dogfood-maestro-s4-local.sh

dogfood-maestro-fly: ## Optional UI spot-check: Maestro 26 + J04 eval on Fly (needs PRELAUNCH_JWT_MARA)
	@chmod +x ./scripts/attic/dogfood-maestro-fly.sh ./scripts/attic/dogfood-journey-j04-chat-eval.sh ./scripts/dogfood-journey-live-api.sh ./scripts/dogfood-env.sh
	@RUN_MAESTRO="$(RUN_MAESTRO)" PRELAUNCH_JWT_MARA="$(PRELAUNCH_JWT_MARA)" PRELAUNCH_HOST="$(PRELAUNCH_HOST)" ./scripts/attic/dogfood-maestro-fly.sh

seed-s4-local: ## Seed S4 lisbon-phase1 to local Postgres (requires vesper DB)
	@chmod +x ./scripts/attic/seed-s4-local.sh
	@./scripts/attic/seed-s4-local.sh

seed-s4-fly: ## DEPRECATED — use `make dogfood-promote CITY=lisbon`. Seed S4 to Fly Postgres (dry-run; SEED_S4_FLY_APPLY=1 to write)
	@echo "⚠ seed-s4-fly is deprecated (docs/journeys/STATUS.md Phase 3 decommission) — prefer: make dogfood-promote CITY=lisbon"
	@./scripts/attic/seed-s4-fly.sh
