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
grep -q "(head)" <<<"$CURRENT_REVISION" || die "Local database is not at the current Alembic head: $CURRENT_REVISION"
pass "Postgres reachable; Alembic is at the current graph head with one graph head"

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
  tests/api/test_plan_state.py \
  tests/concierge/test_change_proposals.py \
  tests/concierge/test_structured_messages.py \
  tests/scenarios/test_lisbon_alpha_front_half.py \
  tests/scenarios/test_lisbon_alpha_provisioning.py \
  tests/scenarios/test_lisbon_group_disruption_contract.py \
  tests/scenarios/test_lisbon_group_disruption_replay.py \
  tests/scenarios/test_local_occasion_closure.py \
  tests/scenarios/test_local_occasion_transport.py \
  tests/scenarios/test_outcome_closure.py \
  tests/scenarios/test_second_occasion_compounds.py \
  tests/core/test_occasion_context.py \
  tests/core/test_ambient_judgment.py \
  tests/core/test_ambient_dispatch.py \
  tests/home/test_m5_ambient_foundations.py \
  tests/eval/test_experience_loop_metrics.py \
  tests/concierge/test_privacy_redactor.py \
  tests/concierge/test_contextual_privacy.py \
  tests/core/test_smaudit_privacy_egress.py)
pass "Backend rescue, proposal-delivery, local-plan, outcome-compounding, privacy, and invalidation canary passed"

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
  __tests__/screens/conversation-create.smoke.test.tsx \
  __tests__/utils/conversationCreateIntent.test.ts \
  __tests__/utils/takeSomewhere.test.ts \
  __tests__/utils/invalidateProposalReadModels.test.ts \
  __tests__/hooks/useTripAuthorityObserver.test.tsx \
  __tests__/utils/tripEventStream.test.ts \
  __tests__/components/react-query-app-state-bridge.test.tsx \
  __tests__/data/proposals.test.ts \
  __tests__/hooks/usePlanProposalUndo.test.ts \
  __tests__/components/trip/proposal-detail/ProposalDetailScreen.test.tsx \
  __tests__/config/groupTripBuildProfiles.test.ts \
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
  const profile = eas.build?.["m1-dogfood"] ?? {};
  const env = profile.env ?? {};
  if (profile.extends !== "dogfood") process.exit(1);
  if (profile.channel !== "m1-dogfood") process.exit(1);
  if (env.EXPO_PUBLIC_IS_INTERNAL_BUILD !== "true") process.exit(1);
  if (env.EXPO_PUBLIC_USE_MOCK_API !== "false") process.exit(1);
  if (env.EXPO_PUBLIC_SKIP_AUTH !== "false") process.exit(1);
  if (env.EXPO_PUBLIC_GROUP_TRIP_MICRO_JOURNEY_ENABLED !== "true") process.exit(1);
  if (env.EXPO_PUBLIC_LOCAL_PLAN_DOGFOOD_ENABLED !== "true") process.exit(1);
  if (env.EXPO_PUBLIC_OUTCOME_ARTIFACT_ENABLED !== "true") process.exit(1);
  for (const flag of [
    "EXPO_PUBLIC_TRIP_EDITORIAL_MAP_ENABLED",
    "EXPO_PUBLIC_TRIPS_NEAR_YOU_DOGFOOD_ENABLED",
    "EXPO_PUBLIC_TRIP_FEEL_STATIC_EXPLORATION_ENABLED",
    "EXPO_PUBLIC_PLACES_READING_SPINE_ENABLED",
    "EXPO_PUBLIC_PLACES_SAVED_UNPLACED_ENABLED",
    "EXPO_PUBLIC_VOICE_ENABLED",
  ]) {
    if (env[flag] !== "false") process.exit(1);
  }
') || die "M1 dogfood profile must enable only the Plan-repair spine and explicitly darken unrelated experiments."
pass "M1 dogfood profile isolates the Plan-repair, outcome, and private-artifact spine"

log "Running cross-repo static gates"
(cd "$WORKSPACE_DIR" && ./scripts/contract-check.sh >/dev/null)
(cd "$WORKSPACE_DIR" && python3 scripts/validate-maestro-flows.py --app-dir travel-app >/dev/null)
(cd "$APP_DIR" && .maestro/../scripts/maestro/check-syntax.sh >/dev/null)
pass "OpenAPI projection and Maestro structure passed"

log "Verifying active product-proof anchors actually pass (not just exist)"
# Postgres is already up and migrated above, so this is the right place to
# also EXECUTE every active proof's registered anchors — a registered anchor
# that exists but is currently red must block dogfood certification, not
# silently count as validated evidence.
(cd "$WORKSPACE_DIR" && python3 scripts/check_journey_registry.py --verify-passes)
pass "Journey registry in sync and every active proof anchor executed clean"

printf '\nPASS: static, mock, and local-backend canary layers are green.\n'
printf 'DEVICE GATE NOT RUN: dogfood-only flags are enabled, but no simulator or physical device was used.\n'
