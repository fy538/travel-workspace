#!/usr/bin/env bash
# Dogfood substrate status — validate manifests and summarize scenario readiness.
# No LLM calls; coding agents extend manifests/seed when data is missing.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$WORKSPACE_DIR/travel-agent"
CONTENT_DIR="$AGENT_DIR/tools/dogfood/content"

header() {
  printf "\n== %s ==\n" "$1"
}

if [[ ! -d "$AGENT_DIR" ]]; then
  echo "travel-agent not found at $AGENT_DIR" >&2
  exit 1
fi

header "Manifest validation"
(
  cd "$AGENT_DIR"
  PYTHONPATH=. python -m tools.dogfood.content.validate
)

header "Scenario registry summary"
python3 - <<'PY' "$CONTENT_DIR/scenarios.yaml" "$CONTENT_DIR/packs.yaml"
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

scenarios_path = Path(sys.argv[1])
packs_path = Path(sys.argv[2])
data = yaml.safe_load(scenarios_path.read_text())
scenarios = data.get("scenarios") or {}

by_lane: dict[str, list[str]] = {}
for sid, row in scenarios.items():
    lane = row.get("lane", "unknown")
    by_lane.setdefault(lane, []).append(sid)

print(f"scenarios: {len(scenarios)} total")
for lane in sorted(by_lane):
    ids = ", ".join(sorted(by_lane[lane]))
    print(f"  {lane}: {len(by_lane[lane])} — {ids}")

packs = yaml.safe_load(packs_path.read_text()).get("packs") or {}
print(f"\npacks: {len(packs)} registered")
for pack_id in sorted(packs):
    print(f"  - {pack_id}")

wedge = scenarios.get("S4-lisbon-group-planning")
if wedge:
    print("\nWedge S4 (lisbon-group-planning):")
    print(f"  status: {wedge.get('status')}")
    print(f"  persona: {wedge.get('persona')} ({wedge.get('account')})")
    print(f"  packs: {', '.join(wedge.get('packs') or [])}")
    print("  seed: cd travel-agent && PYTHONPATH=. python -m tools.dogfood.content.seed manifests/lisbon-phase1.yaml --apply")
PY

header "Local Postgres probe (logic QA / seed)"
if command -v psql >/dev/null 2>&1; then
  if PGPASSWORD=localdev psql -h localhost -U vesper -d vesper -c 'SELECT 1' >/dev/null 2>&1; then
    echo "✓ vesper@localhost:5432 reachable (make certify-logic ready)"
  else
    echo "⚠ vesper DB not reachable — logic QA scenarios skip locally."
    echo "  CI runs them via travel-app logic-qa + agent test-db jobs."
    echo "  Local fix: start postgis/postgis with POSTGRES_USER=vesper POSTGRES_DB=vesper"
  fi
else
  echo "psql not installed — skipping Postgres probe"
fi

printf "\nDogfood status check complete.\n"
