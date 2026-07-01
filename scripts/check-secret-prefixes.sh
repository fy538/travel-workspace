#!/usr/bin/env bash
#
# check-secret-prefixes.sh — guard against real credentials slipping into git.
#
# CANONICAL SOURCE: ~/travel-workspace/scripts/check-secret-prefixes.sh
# Child repos (travel-agent, travel-app) reference this via their
# pre-commit entry: ../scripts/check-secret-prefixes.sh — never copy it.
# If you find a copy in a child repo's scripts/, delete it and re-point.
#
# Why this exists:
#   `detect-secrets` (the pre-commit hook in Travel Agent) does NOT have
#   detectors for the credential shapes WE actually use:
#       - Anthropic        sk-ant-…
#       - Clerk            pk_live_… / sk_live_…
#       - Google APIs      AIzaSy…
#       - PostHog          phc_…
#       - Tavily           tvly-…
#       - Langfuse         pk-lf-… / sk-lf-…
#       - Foursquare       fsq3…
#       - Cloudflare R2    (S3-style — caught by detect-secrets AWS)
#       - Bland.ai         (no prefix — relies on env-var name match)
#
#   It does cover AWS / GitHub / Stripe / Slack / Twilio / OpenAI, so we
#   layer this on top instead of replacing it.
#
# Behavior:
#   - Scans staged files (or all files when run with --all).
#   - Exits 1 on any match. Prints the offending file:line with the
#     prefix that matched.
#   - Always-skip: ``*.env.example``, ``*.secrets.baseline`` (those are
#     allowed to mention prefixes in docstrings / placeholders).
#   - Heuristic: a prefix counts as a "real" credential when followed
#     by at least 16 chars of the right alphabet — skips obvious
#     placeholders like ``sk-ant-…`` (literal ellipsis) or
#     ``pk_live_REPLACE_ME``.
#
# Usage:
#   scripts/check-secret-prefixes.sh                  # staged files only
#   scripts/check-secret-prefixes.sh --all            # whole tree
#   scripts/check-secret-prefixes.sh path/to/file.env # specific files

set -euo pipefail

# Each pattern is grep-extended-regex. We anchor with the prefix and
# require at least 16 chars of the right alphabet after — short enough
# to catch a real key, long enough to skip ``sk-ant-…`` placeholders.
#
# WHEN ADDING A NEW PROVIDER: append a new line to this array. Pre-fix
# with a short comment in the runbook. Keep this list in sync with
# `docs/operations/Secret Rotation Runbook.md`.
PATTERNS=(
  'sk-ant-[A-Za-z0-9_-]{16,}'        # Anthropic live keys
  'pk_live_[A-Za-z0-9]{16,}'         # Clerk live publishable
  'sk_live_[A-Za-z0-9]{16,}'         # Clerk live secret
  'AIzaSy[A-Za-z0-9_-]{16,}'         # Google APIs (Places, Maps, etc.)
  'phc_[A-Za-z0-9]{16,}'             # PostHog
  'tvly-[A-Za-z0-9]{16,}'            # Tavily
  'pk-lf-[A-Za-z0-9]{16,}'           # Langfuse public
  'sk-lf-[A-Za-z0-9]{16,}'           # Langfuse secret
  'fsq3[A-Za-z0-9+/=]{16,}'          # Foursquare service key
  'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.' # Generic JWT (Clerk session, etc.)
)

# Files we never scan even when staged.
SKIP_PATTERNS=(
  '\.env\.example$'
  '\.secrets\.baseline$'
  'check-secret-prefixes\.sh$'      # this script defines the patterns
  'Secret Rotation Runbook\.md$'    # the runbook documents the patterns
  '\.git/'
  '/node_modules/'
  '/\.venv/'
)

skip() {
  local f="$1"
  for p in "${SKIP_PATTERNS[@]}"; do
    if [[ "$f" =~ $p ]]; then return 0; fi
  done
  return 1
}

# Build the file list.
mode="${1:-staged}"
files=()
if [[ "$mode" == "--all" ]]; then
  while IFS= read -r f; do files+=("$f"); done < <(git ls-files)
elif [[ "$mode" == "staged" || -z "$mode" ]]; then
  while IFS= read -r f; do
    [[ -f "$f" ]] && files+=("$f")
  done < <(git diff --cached --name-only --diff-filter=ACM)
else
  # Specific files passed by pre-commit
  for arg in "$@"; do
    [[ -f "$arg" ]] && files+=("$arg")
  done
fi

if [[ ${#files[@]} -eq 0 ]]; then
  exit 0
fi

found_any=0
for f in "${files[@]}"; do
  if skip "$f"; then continue; fi
  for pat in "${PATTERNS[@]}"; do
    matches=$(grep -nE "$pat" "$f" 2>/dev/null || true)
    if [[ -n "$matches" ]]; then
      while IFS= read -r line; do
        echo "❌ Secret prefix match in $f"
        echo "   pattern: $pat"
        echo "   $line"
      done <<< "$matches"
      found_any=1
    fi
  done
done

if [[ $found_any -eq 1 ]]; then
  cat >&2 <<'MSG'

A line above looks like a real credential. Options:
  1. If it IS a real credential — STOP. Move it to your vault (1Password /
     Doppler / host-native secret store), reference it in .env locally,
     and never let it land in git.
  2. If it's an intentional placeholder (e.g. a runbook example), shorten
     it or replace the key body with `<REDACTED>` so it falls below the
     16-char floor.
  3. If you're certain it's safe AND must stay (e.g. published example
     in a teaching doc), append `# pragma: allowlist-secret` to the line.

Failing the commit. Fix and re-stage.
MSG
  exit 1
fi

exit 0
