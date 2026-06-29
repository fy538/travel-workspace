#!/usr/bin/env bash
# Shared dogfood environment profile resolution (local workbench vs Fly certified).
#
# Source from dogfood-city.sh / dogfood-env-check.sh — do not execute directly.
#
# Profiles bind Postgres + Qdrant as an atomic pair:
#   local → Docker Postgres + Docker Qdrant
#   fly   → PROD_DATABASE_URL + cloud Qdrant (.env)
set -euo pipefail

: "${AGENT_DIR:?AGENT_DIR must be set by caller}"

PROFILE="${PROFILE:-local}"
ALLOW_MIXED="${ALLOW_MIXED:-0}"

LOCAL_DATABASE_URL="${LOCAL_DATABASE_URL:-postgresql://vesper:localdev@localhost:5432/vesper}"
LOCAL_QDRANT_URL="${LOCAL_QDRANT_URL:-http://localhost:6333}"

_is_local_host() {
  case "${1:-}" in
    ""|localhost|127.0.0.1|::1) return 0 ;;
    *) return 1 ;;
  esac
}

_host_from_url() {
  local url="$1"
  PYTHONPATH="$AGENT_DIR" python -c 'from urllib.parse import urlsplit; import sys; print(urlsplit(sys.argv[1]).hostname or "")' "$url"
}

_dogfood_load_fly_database_url() {
  local env_prod="$AGENT_DIR/.env.prod"
  if [[ ! -f "$env_prod" ]]; then
    echo "ERROR: PROFILE=fly requires $env_prod with PROD_DATABASE_URL" >&2
    return 1
  fi
  (
    cd "$AGENT_DIR"
    PYTHONPATH=. python - <<'PY'
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(".env.prod"), override=False)
print(os.environ.get("PROD_DATABASE_URL", ""))
PY
  )
}

_dogfood_load_cloud_qdrant_env() {
  local env_file="$AGENT_DIR/.env"
  if [[ -f "$env_file" ]]; then
    # shellcheck disable=SC1090
    set -a
    # shellcheck source=/dev/null
    source "$env_file"
    set +a
  fi
  if [[ -z "${QDRANT_URL:-}" ]]; then
    echo "ERROR: PROFILE=fly requires QDRANT_URL in travel-agent/.env" >&2
    return 1
  fi
}

dogfood_apply_profile() {
  case "$PROFILE" in
    local)
      export DATABASE_URL="$LOCAL_DATABASE_URL"
      export QDRANT_URL="$LOCAL_QDRANT_URL"
      unset QDRANT_API_KEY 2>/dev/null || true
      export ENVIRONMENT="${ENVIRONMENT:-development}"
      export DOGFOOD_DOTENV_OVERRIDE=false
      ;;
    fly)
      local prod_url
      prod_url="$(_dogfood_load_fly_database_url)" || return 1
      if [[ -z "$prod_url" ]]; then
        echo "ERROR: PROD_DATABASE_URL is empty in travel-agent/.env.prod" >&2
        return 1
      fi
      _dogfood_load_cloud_qdrant_env || return 1
      export DATABASE_URL="$prod_url"
      export ENVIRONMENT="${ENVIRONMENT:-production}"
      export DOGFOOD_DOTENV_OVERRIDE=false
      ;;
    *)
      echo "ERROR: unknown PROFILE='$PROFILE' (expected local|fly)" >&2
      return 1
      ;;
  esac

  local pg_host qdrant_host
  pg_host="$(_host_from_url "$DATABASE_URL")"
  qdrant_host="$(_host_from_url "$QDRANT_URL")"

  if [[ "$PROFILE" == "local" ]] && ! _is_local_host "$pg_host" && [[ "$ALLOW_MIXED" != "1" ]]; then
    echo "ERROR: PROFILE=local but DATABASE_URL host is '$pg_host' (not local)." >&2
    echo "  Set PROFILE=fly for remote Postgres, or ALLOW_MIXED=1 to override." >&2
    return 1
  fi

  if [[ "$PROFILE" == "local" ]] && ! _is_local_host "$qdrant_host" && [[ "$ALLOW_MIXED" != "1" ]]; then
    echo "ERROR: PROFILE=local but QDRANT_URL host is '$qdrant_host' (not local Docker)." >&2
    echo "  Split-brain guard: local Postgres must pair with local Qdrant." >&2
    echo "  Re-run with PROFILE=local and QDRANT_URL=$LOCAL_QDRANT_URL, or ALLOW_MIXED=1." >&2
    return 1
  fi

  if [[ "$PROFILE" == "fly" ]] && _is_local_host "$pg_host"; then
    echo "ERROR: PROFILE=fly but DATABASE_URL host is local." >&2
    return 1
  fi

  if [[ "$PROFILE" == "fly" ]] && _is_local_host "$qdrant_host"; then
    echo "ERROR: PROFILE=fly but QDRANT_URL host is local." >&2
    return 1
  fi

  DOGFOOD_ALLOW_PROD=()
  if [[ "$PROFILE" == "fly" && "${APPLY:-0}" == "1" ]]; then
    DOGFOOD_ALLOW_PROD=(--allow-prod)
    export DOGFOOD_HAS_ALLOW_PROD=1
  else
    export DOGFOOD_HAS_ALLOW_PROD=0
  fi

  export DOGFOOD_PROFILE="$PROFILE"
  export DOGFOOD_PG_HOST="$pg_host"
  export DOGFOOD_QDRANT_HOST="$qdrant_host"
}

dogfood_print_stack() {
  local safe_dsn
  safe_dsn="$(
    PYTHONPATH="$AGENT_DIR" python -c 'from tools.dogfood.ops_guard import redact_dsn; import os; print(redact_dsn(os.environ.get("DATABASE_URL", "")))'
  )"
  echo "▸ profile=$PROFILE  postgres_host=$DOGFOOD_PG_HOST  qdrant_host=$DOGFOOD_QDRANT_HOST"
  echo "  DATABASE_URL=${safe_dsn}"
  echo "  QDRANT_URL=${QDRANT_URL}"
}

dogfood_allow_prod_flag() {
  if [ "${DOGFOOD_HAS_ALLOW_PROD:-0}" = "1" ]; then
    echo --allow-prod
  fi
}
