#!/usr/bin/env bash
# Emit the raw signal for the nightly digest as a single JSON document.
#
# Separating data-gathering from synthesis keeps the routine's prompt small
# and lets us iterate on the schema without retraining a prompt. The routine
# pipes this into its context, then judges what's signal vs. noise.
#
# Usage:  scripts/digest-inputs.sh > digest-raw.json
# Cost:   ~10s, ~30 GitHub API calls.

set -euo pipefail

# All output is the final JSON. Status messages go to stderr.
log() { printf "[digest-inputs] %s\n" "$*" >&2; }

# ── Repos ────────────────────────────────────────────────────────────────────
AGENT=fy538/travel-agent
APP=fy538/travel-app
WS=fy538/travel-workspace

# ── Helpers ──────────────────────────────────────────────────────────────────
# Last N CI runs on main for a repo. `gh run list` returns most-recent first.
runs_main() {
  local repo="$1"
  local workflow="${2:-CI}"
  gh run list \
    --repo "$repo" --branch main --workflow="$workflow" --limit 30 \
    --json conclusion,createdAt,startedAt,updatedAt,databaseId,displayTitle,event \
    2>/dev/null || echo "[]"
}

# Open PRs with their CI rollup. CI status is only meaningful on the head SHA.
open_prs() {
  local repo="$1"
  gh pr list \
    --repo "$repo" --state open --limit 30 \
    --json number,title,createdAt,updatedAt,author,labels,isDraft,statusCheckRollup \
    2>/dev/null || echo "[]"
}

# Recent commits on main, last 24h. Subjects only; the digest doesn't need diffs.
recent_commits() {
  local repo="$1"
  gh api "repos/$repo/commits?since=$(date -u -v-24H '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date -u -d '24 hours ago' '+%Y-%m-%dT%H:%M:%SZ')&per_page=50" \
    --jq '[.[] | {sha: .sha[:7], subject: (.commit.message | split("\n")[0]), author: .commit.author.name, date: .commit.author.date}]' \
    2>/dev/null || echo "[]"
}

# Per-repo bundle.
repo_bundle() {
  local repo="$1"
  local ci_workflow="${2:-CI}"

  log "gathering $repo..."
  jq -n \
    --argjson runs    "$(runs_main "$repo" "$ci_workflow")" \
    --argjson prs     "$(open_prs "$repo")" \
    --argjson commits "$(recent_commits "$repo")" \
    '{ci_runs: $runs, open_prs: $prs, recent_commits_24h: $commits}'
}

# ── Compute simple baselines (7-day vs prior 7-day) ──────────────────────────
# Avg CI duration over last 7 runs and the 7 before that. Lets the prompt
# spot creep without doing the math itself.
duration_stats() {
  local runs_json="$1"
  echo "$runs_json" | jq '
    [.[] | select(.startedAt != "" and .updatedAt != "") |
     ((.updatedAt | fromdateiso8601) - (.startedAt | fromdateiso8601))]
    | {
        last_7_avg_sec:  (if length >= 7  then (.[0:7]  | add / length | floor) else null end),
        prior_7_avg_sec: (if length >= 14 then (.[7:14] | add / 7      | floor) else null end),
        sample_size: length
      }'
}

# ── Build the output JSON ────────────────────────────────────────────────────
log "starting digest-inputs collection"

agent_bundle=$(repo_bundle "$AGENT")
app_bundle=$(repo_bundle "$APP")
ws_bundle=$(repo_bundle "$WS")
reliability_bundle=$(runs_main "$WS" "Reliability")

agent_duration_stats=$(duration_stats "$(echo "$agent_bundle" | jq '.ci_runs')")
app_duration_stats=$(duration_stats "$(echo "$app_bundle" | jq '.ci_runs')")

# Generated-at timestamp uses America/New_York to match the user's local day.
generated_at=$(TZ='America/New_York' date '+%Y-%m-%dT%H:%M:%S%z')
digest_date=$(TZ='America/New_York' date '+%Y-%m-%d')

log "assembling JSON"

jq -n \
  --arg generated_at "$generated_at" \
  --arg digest_date  "$digest_date" \
  --argjson agent           "$agent_bundle" \
  --argjson app             "$app_bundle" \
  --argjson workspace       "$ws_bundle" \
  --argjson reliability     "$reliability_bundle" \
  --argjson agent_durations "$agent_duration_stats" \
  --argjson app_durations   "$app_duration_stats" \
'{
  generated_at: $generated_at,
  digest_date:  $digest_date,
  repos: {
    "travel-agent":     ($agent     + {duration_stats: $agent_durations}),
    "travel-app":       ($app       + {duration_stats: $app_durations}),
    "travel-workspace": $workspace
  },
  reliability_runs: $reliability
}'

log "done"
