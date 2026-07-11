# scripts/attic — completed-campaign dogfood tooling

Shell scripts for the Tier A/B corpus import and five-pack (Lisbon/Rome/Istanbul/Tokyo/Brooklyn) dogfood campaigns, all marked **PASSED/COMPLETE 2026-06-29** in `docs/journeys/STATUS.md`.

They remain callable via `dogfood.mk` targets (`make import-latent-corpus`, `make dogfood-five-pack-verify`, etc.) but live here so `scripts/` day-to-day surface stays focused on active cross-repo workflows.

**Shared dependency:** `../dogfood-env.sh` (stays in `scripts/` — also used by `dogfood-city`, `dogfood-promote`, and other live Makefile targets).

**Active tooling that stays in `scripts/`:** `dogfood-city.sh`, `dogfood-promote.sh`, `corpus-check.sh`, `dogfood-env-check.sh`, `dogfood-status.sh`, `dogfood-journey-live-api.sh`, `certify-live.sh`, `dogfood-device-cert-live.sh`.

From the 2026-07-11 architecture-simplification audit, Tier 1.
