#!/usr/bin/env bash
# doctor.sh — Lightweight workspace health check.
#
# Validates that the parent workspace and both child repos are present,
# then checks for the core tools used in the current workflow.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
APP_DIR="$WORKSPACE_DIR/travel-app"
SNAPSHOT_PATH="$WORKSPACE_DIR/docs/openapi.json"

ok() {
  printf "  \033[32m✓\033[0m %s\n" "$1"
}

warn() {
  printf "  \033[33m⚠\033[0m %s\n" "$1"
}

fail() {
  printf "  \033[31m✗\033[0m %s\n" "$1"
  exit 1
}

header() {
  printf "\n\033[1m%s\033[0m\n" "$1"
}

check_command() {
  local cmd="$1"
  local label="${2:-$1}"
  if command -v "$cmd" >/dev/null 2>&1; then
    ok "$label available"
  else
    warn "$label not found"
  fi
}

check_ignored() {
  local path="$1"
  local label="$2"
  if git -C "$WORKSPACE_DIR" check-ignore -q "$path"; then
    ok "$label ignored by workspace git"
  else
    warn "$label is not ignored by workspace git"
  fi
}

header "Workspace"

[ -d "$AGENT_DIR" ] || fail "travel-agent repo missing at $AGENT_DIR"
[ -d "$APP_DIR" ] || fail "travel-app repo missing at $APP_DIR"
[ -d "$WORKSPACE_DIR/.git" ] || fail "Workspace repo missing .git at $WORKSPACE_DIR"
ok "Workspace repo present"
ok "travel-agent repo present"
ok "travel-app repo present"

tracked_child_files="$(
  git -C "$WORKSPACE_DIR" ls-files -- "travel-agent" "travel-app" 2>/dev/null || true
)"
if [ -n "$tracked_child_files" ]; then
  fail "Workspace is tracking files inside child repos. Remove them from the parent index."
else
  ok "Workspace is not tracking child repo source"
fi

check_ignored "travel-agent/README.md" "travel-agent"
check_ignored "travel-app/README.md" "travel-app"

if [ -f "$SNAPSHOT_PATH" ]; then
  ok "Committed OpenAPI snapshot present"
else
  warn "Committed OpenAPI snapshot missing at $SNAPSHOT_PATH"
fi

header "Git"

check_command git

if git -C "$AGENT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "travel-agent git repo healthy"
else
  fail "travel-agent is not a valid git repo"
fi

if git -C "$APP_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  ok "travel-app git repo healthy"
else
  fail "travel-app is not a valid git repo"
fi

agent_branch="$(git -C "$AGENT_DIR" branch --show-current || true)"
app_branch="$(git -C "$APP_DIR" branch --show-current || true)"
ok "travel-agent branch: ${agent_branch:-detached HEAD}"
ok "travel-app branch: ${app_branch:-detached HEAD}"

header "Tooling"

check_command docker "Docker"
check_command uvicorn "uvicorn"
check_command npx "npx"
check_command python3 "python3"
check_command node "node"

if command -v maestro >/dev/null 2>&1; then
  ok "Maestro CLI available"
  if [ -n "${JAVA_HOME:-}" ] && [ -x "${JAVA_HOME}/bin/java" ]; then
    ok "JAVA_HOME set ($JAVA_HOME)"
  elif [ -x /opt/homebrew/opt/openjdk/bin/java ]; then
    ok "Homebrew openjdk available (/opt/homebrew/opt/openjdk)"
  elif /usr/libexec/java_home >/dev/null 2>&1; then
    ok "Java runtime available (required for Maestro)"
  else
    warn "Java runtime not found — make certify-visual / maestro test will fail"
    warn "Install: brew install openjdk (or brew install --cask temurin)"
  fi
else
  warn "Maestro not found (optional for make certify-visual)"
fi

header "Remotes"

workspace_remote="$(git -C "$WORKSPACE_DIR" remote get-url origin 2>/dev/null || true)"
agent_remote="$(git -C "$AGENT_DIR" remote get-url origin 2>/dev/null || true)"
app_remote="$(git -C "$APP_DIR" remote get-url origin 2>/dev/null || true)"

if [ -n "$workspace_remote" ]; then
  ok "Workspace origin: $workspace_remote"
else
  warn "Workspace has no origin remote"
fi

if [ -n "$agent_remote" ]; then
  ok "travel-agent origin: $agent_remote"
else
  warn "travel-agent has no origin remote"
fi

if [ -n "$app_remote" ]; then
  ok "travel-app origin: $app_remote"
else
  warn "travel-app has no origin remote"
fi

header "Local Postgres (certify / dogfood)"

CANONICAL_DATABASE_URL="postgresql://vesper:localdev@localhost:5432/vesper"
ok "Canonical local DSN: $CANONICAL_DATABASE_URL"

if command -v docker >/dev/null 2>&1; then
  if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx 'research-agent-postgres'; then
    ok "Docker Postgres container running (research-agent-postgres)"
    if (cd "$AGENT_DIR" && docker compose exec -T postgres pg_isready -U vesper >/dev/null 2>&1); then
      ok "Postgres accepts vesper user (matches backend defaults)"
    else
      warn "Container up but vesper role not ready — likely an old volume initialized as research_agent"
      warn "Fix: cd travel-agent && docker compose down -v && docker compose up -d"
    fi
  else
    warn "research-agent-postgres container not running (make dev-backend starts it)"
  fi
else
  warn "Docker not available — skipping container probe"
fi

if command -v psql >/dev/null 2>&1; then
  if PGPASSWORD=localdev psql -U vesper -h localhost -d vesper -c 'SELECT 1' >/dev/null 2>&1; then
    ok "Host psql can connect as vesper@localhost:5432/vesper"
  else
    warn "Host psql cannot connect as vesper@localhost:5432/vesper"
  fi
fi

agent_env="$AGENT_DIR/.env"
if [ -f "$agent_env" ]; then
  env_database_url="$(grep -E '^DATABASE_URL=' "$agent_env" 2>/dev/null | head -1 | cut -d= -f2- || true)"
  if [ -n "$env_database_url" ] && [ "$env_database_url" != "$CANONICAL_DATABASE_URL" ]; then
    warn "travel-agent/.env DATABASE_URL differs from canonical vesper DSN"
    warn "  set: $env_database_url"
    warn "  certify/seed expect: $CANONICAL_DATABASE_URL (or unset DATABASE_URL and use POSTGRES_* defaults)"
  elif [ -n "$env_database_url" ]; then
    ok "travel-agent/.env DATABASE_URL matches canonical local DSN"
  else
    ok "travel-agent/.env has no DATABASE_URL override (backend defaults to vesper)"
  fi
fi

shell_database_url="${DATABASE_URL:-}"
if [ -n "$shell_database_url" ] && [ "$shell_database_url" != "$CANONICAL_DATABASE_URL" ]; then
  warn "Shell DATABASE_URL differs from canonical — make certify-logic / make seed-s4-local may skip or hit wrong DB"
  warn "  export DATABASE_URL='$CANONICAL_DATABASE_URL'"
fi

printf "\n\033[32mWorkspace doctor complete.\033[0m\n"
