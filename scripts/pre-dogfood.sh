#!/usr/bin/env bash
# Static + local-canary preflight for the next device dogfood pass.
#
# This command deliberately does not launch Expo, call live providers, enable
# feature flags, or claim device certification. It proves the pieces that can
# be proven without a phone: schema state, backend contracts, deterministic
# provider/agent seams, app type/ownership checks, and the local-plan surfaces.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
POSTGRES_HOST_PORT="${POSTGRES_HOST_PORT:-15432}"
DATABASE_URL="${DATABASE_URL:-postgresql://vesper:localdev@localhost:${POSTGRES_HOST_PORT}/vesper}"

log() { printf '\n▸ %s\n' "$1"; }
pass() { printf '  ✓ %s\n' "$1"; }
die() { printf '\n✗ %s\n' "$1" >&2; exit 1; }

command -v docker >/dev/null 2>&1 || die "Docker is required for the local Postgres canary."
[ -x "$AGENT_DIR/.venv/bin/python" ] || die "Missing travel-agent/.venv; install backend development dependencies first."
[ -d "$APP_DIR/node_modules" ] || die "Missing travel-app/node_modules; run npm ci first."

log "Checking local Postgres and applying migrations"
if ! (cd "$AGENT_DIR" && docker compose exec -T postgres pg_isready -U vesper >/dev/null 2>&1); then
  die "Postgres is not ready. Start it with: (cd travel-agent && docker compose up -d postgres)"
fi
(cd "$AGENT_DIR" && DATABASE_URL="$DATABASE_URL" PYTHONPATH=. .venv/bin/alembic upgrade head >/dev/null)
(cd "$AGENT_DIR" && PYTHONPATH=. .venv/bin/python scripts/check_alembic_single_head.py >/dev/null)
CURRENT_REVISION="$(cd "$AGENT_DIR" && DATABASE_URL="$DATABASE_URL" PYTHONPATH=. .venv/bin/alembic current)"
EXPECTED_MIGRATION_HEAD="ambientcycle02"
grep -q "$EXPECTED_MIGRATION_HEAD" <<<"$CURRENT_REVISION" || die "Local database is not at the $EXPECTED_MIGRATION_HEAD head: $CURRENT_REVISION"
pass "Postgres reachable; Alembic is at $EXPECTED_MIGRATION_HEAD with one graph head"

log "Running deterministic backend canary"
(cd "$AGENT_DIR" && DATABASE_URL="$DATABASE_URL" SKIP_AUTH=true PYTHONPATH=. .venv/bin/python -m pytest -q \
  tests/concierge/test_promote_tool.py \
  tests/api/test_conversations_api.py \
  tests/concierge/test_turn_loader.py \
  tests/concierge/test_spatial_situation.py \
  tests/concierge/test_distance_tool_semantics.py \
  tests/core/test_ai_runs.py \
  tests/core/test_experience_scope.py \
  tests/planning/test_planning_profiles.py \
  tests/core/test_reachability.py \
  tests/core/test_isochrone.py \
  tests/core/test_occurrence_artifact.py \
  tests/core/test_occurrence_reconciliation.py \
  tests/scenarios/test_local_occasion_closure.py \
  tests/scenarios/test_local_occasion_transport.py \
  tests/scenarios/test_outcome_closure.py \
  tests/core/test_ambient_judgment.py \
  tests/core/test_ambient_dispatch.py \
  tests/home/test_m5_ambient_foundations.py \
  tests/eval/test_experience_loop_metrics.py \
  tests/concierge/test_privacy_redactor.py \
  tests/concierge/test_contextual_privacy.py \
  tests/core/test_smaudit_privacy_egress.py)
pass "Backend local-plan, spatial-provider, artifact, privacy, and invalidation canary passed"

log "Running app deterministic replay and contract checks"
(cd "$APP_DIR" && npx jest --runInBand \
  __tests__/utils/api/mock.test.ts \
  __tests__/constants/featureFlags.test.ts \
  __tests__/utils/localPlanPresentation.test.ts \
  __tests__/components/trips/LocalPlansCard.test.tsx \
  __tests__/components/trips/tripsHomeHeroModel.test.ts \
  __tests__/components/trip-plan/LocalPlanScreen.test.tsx \
  __tests__/journeys/local-occasion-closure.replay.test.tsx \
  __tests__/journeys/local-occasion-transport.replay.test.tsx \
  __tests__/components/trip-plan/OccurrenceArtifactCard.test.tsx \
  __tests__/utils/invalidateHomeProjections.test.ts \
  __tests__/data/read-model-invalidations.test.ts)
(cd "$APP_DIR" && npm run --silent typecheck)
(cd "$APP_DIR" && npm run --silent test:typecheck:contracts)
(cd "$APP_DIR" && npm run --silent api-boundaries)
(cd "$APP_DIR" && npm run --silent query-key-ownership)
(cd "$APP_DIR" && npm run --silent mutation-key-ownership)
pass "App replay surfaces, types, API boundaries, and cache ownership passed"

log "Checking dogfood-only local experience gates"
(cd "$APP_DIR" && node -e '
  const eas = require("./eas.json");
  const env = eas.build?.dogfood?.env ?? {};
  if (env.EXPO_PUBLIC_IS_INTERNAL_BUILD !== "true") process.exit(1);
  if (env.EXPO_PUBLIC_LOCAL_PLAN_DOGFOOD_ENABLED !== "true") process.exit(1);
  if (env.EXPO_PUBLIC_OUTCOME_ARTIFACT_ENABLED !== "true") process.exit(1);
') || die "Dogfood profile must explicitly enable the internal local loop and private outcome artifact."
pass "Dogfood profile explicitly enables the internal-only Friday-night loop"

log "Running cross-repo static gates"
(cd "$WORKSPACE_DIR" && ./scripts/contract-check.sh >/dev/null)
(cd "$WORKSPACE_DIR" && python3 scripts/check_journey_registry.py >/dev/null)
(cd "$WORKSPACE_DIR" && python3 scripts/validate-maestro-flows.py --app-dir travel-app >/dev/null)
(cd "$APP_DIR" && .maestro/../scripts/maestro/check-syntax.sh >/dev/null)
pass "OpenAPI projection, journey registry, and Maestro structure passed"

printf '\nPASS: static, mock, and local-backend canary layers are green.\n'
printf 'DEVICE GATE NOT RUN: dogfood-only flags are enabled, but no simulator or physical device was used.\n'
