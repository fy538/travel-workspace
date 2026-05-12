#!/usr/bin/env bash
# Daily CI/CD dashboard — read the same numbers each day so drift becomes visible.
#
# What this surfaces:
#   • Last 10 main CI runs per repo  → catches creeping flakiness or red runs
#   • Workflow duration trend        → catches step-bloat before it bites
#   • Open PRs with stuck CI         → catches "fix it later" debt
#   • Dependabot PR age              → catches dep updates rotting in the queue
#   • Recent Reliability dispatches  → catches the cross-repo chain stalling
#
# Run nightly; ~5 seconds. Exit 0 unconditionally — this is a report, not a gate.

set -euo pipefail

# ── Colors ──────────────────────────────────────────────────────────────────
if [[ -t 1 ]]; then
  green='\033[0;32m'; yellow='\033[0;33m'; red='\033[0;31m'
  bold='\033[1m'; dim='\033[2m'; reset='\033[0m'
else
  green=''; yellow=''; red=''; bold=''; dim=''; reset=''
fi

ok()    { printf "${green}✓${reset} %s\n" "$*"; }
warn()  { printf "${yellow}⚠${reset} %s\n" "$*"; }
bad()   { printf "${red}✗${reset} %s\n" "$*"; }
note()  { printf "${dim}  %s${reset}\n" "$*"; }
hdr()   { printf "\n${bold}── %s ──${reset}\n" "$*"; }

# ── Per-repo CI snapshot ────────────────────────────────────────────────────
repo_health() {
  local repo="$1"
  local name="$2"

  local data
  data=$(gh run list --repo "$repo" --branch main --limit 10 --workflow=CI \
    --json conclusion,createdAt,startedAt,updatedAt 2>/dev/null || echo "[]")

  if [[ "$data" == "[]" ]]; then
    bad "$name: no CI runs found"
    return
  fi

  local total green_count red_count
  total=$(echo "$data" | jq 'length')
  green_count=$(echo "$data" | jq '[.[] | select(.conclusion == "success")] | length')
  red_count=$(echo "$data" | jq '[.[] | select(.conclusion == "failure" or .conclusion == "cancelled")] | length')

  # Average duration in seconds (startedAt → updatedAt)
  local avg_sec
  avg_sec=$(echo "$data" | jq -r '
    [.[] | select(.startedAt != "" and .updatedAt != "") |
     ((.updatedAt | fromdateiso8601) - (.startedAt | fromdateiso8601))]
    | if length > 0 then (add / length | floor) else 0 end
  ')
  local avg_disp="${avg_sec}s"
  if (( avg_sec >= 60 )); then
    avg_disp="$((avg_sec / 60))m$((avg_sec % 60))s"
  fi

  if (( red_count == 0 )); then
    ok "$name: ${green_count}/${total} green, avg ${avg_disp}"
  else
    bad "$name: ${green_count}/${total} green (${red_count} red), avg ${avg_disp}"
    local last_fail
    last_fail=$(echo "$data" | jq -r '
      [.[] | select(.conclusion == "failure" or .conclusion == "cancelled")][0]
      | .createdAt[:10] + " " + (.conclusion // "—")
    ' 2>/dev/null)
    [[ -n "$last_fail" ]] && note "most recent red: $last_fail"
  fi
}

# ── Open PRs ────────────────────────────────────────────────────────────────
prs() {
  local repo="$1"
  local name="$2"

  local data
  data=$(gh pr list --repo "$repo" --state open --json number,title,createdAt,statusCheckRollup 2>/dev/null || echo "[]")
  local count
  count=$(echo "$data" | jq 'length')

  if (( count == 0 )); then
    ok "$name: 0 open PRs"
    return
  fi

  # PRs with red CI
  local red
  red=$(echo "$data" | jq -r '
    .[] | select(any(.statusCheckRollup[]?; .conclusion == "FAILURE" or .conclusion == "CANCELLED"))
    | "#\(.number) \(.title[:60])"' 2>/dev/null)

  if [[ -n "$red" ]]; then
    warn "$name: $count open PRs, some with red CI:"
    echo "$red" | while read -r line; do note "$line"; done
  else
    ok "$name: $count open PRs, all CI green or pending"
  fi
}

# ── Dependabot age ──────────────────────────────────────────────────────────
dependabot_age() {
  local repo="$1"
  local name="$2"

  local data
  data=$(gh pr list --repo "$repo" --state open --author "dependabot[bot]" --json number,title,createdAt 2>/dev/null || echo "[]")
  local count
  count=$(echo "$data" | jq 'length')

  if (( count == 0 )); then
    ok "$name dependabot: 0 open"
    return
  fi

  # Bucket by age (days)
  local now_ts
  now_ts=$(date +%s)
  local old
  old=$(echo "$data" | jq -r --argjson now "$now_ts" '
    .[] | select(((($now - (.createdAt | fromdateiso8601)) / 86400) | floor) >= 7)
    | "  #\(.number) (\((($now - (.createdAt | fromdateiso8601)) / 86400) | floor)d) \(.title[:50])"
  ')

  if [[ -n "$old" ]]; then
    warn "$name dependabot: $count open, some >7d old:"
    echo "$old" | while read -r line; do printf "${dim}%s${reset}\n" "$line"; done
  else
    ok "$name dependabot: $count open, all <7d"
  fi
}

# ── Workspace Reliability ───────────────────────────────────────────────────
reliability() {
  local data
  data=$(gh run list --repo fy538/travel-workspace --workflow=Reliability --limit 5 \
    --json conclusion,displayTitle,createdAt 2>/dev/null || echo "[]")

  local success_count cancelled_count failure_count
  success_count=$(echo "$data" | jq '[.[] | select(.conclusion == "success")] | length')
  cancelled_count=$(echo "$data" | jq '[.[] | select(.conclusion == "cancelled")] | length')
  failure_count=$(echo "$data" | jq '[.[] | select(.conclusion == "failure")] | length')

  if (( failure_count > 0 )); then
    bad "Reliability: ${success_count}/5 success, ${failure_count} failed, ${cancelled_count} cancelled"
  elif (( cancelled_count > 0 )); then
    warn "Reliability: ${success_count}/5 success, ${cancelled_count} cancelled (concurrency-induced is fine)"
  else
    ok "Reliability: ${success_count}/5 success"
  fi
}

# ── Main ────────────────────────────────────────────────────────────────────
printf "${bold}CI/CD review — $(date '+%Y-%m-%d %H:%M')${reset}\n"

hdr "Last 10 main CI runs"
repo_health fy538/travel-agent "Travel Agent"
repo_health fy538/travel-app   "Travel App"

hdr "Cross-repo Reliability"
reliability

hdr "Open PRs"
prs fy538/travel-agent "Travel Agent"
prs fy538/travel-app   "Travel App"

hdr "Dependabot drift"
dependabot_age fy538/travel-agent "Travel Agent"
dependabot_age fy538/travel-app   "Travel App"

printf "\n${dim}For details: gh run list --repo <repo> --limit 20${reset}\n"
