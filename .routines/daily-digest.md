# Nightly CI/CD digest

You are running as a Claude Code routine on Anthropic's cloud infrastructure,
once per night around 9pm America/New_York. The repo
`fy538/travel-workspace` is cloned to your working directory. Sibling repos
`fy538/travel-agent` and `fy538/travel-app` are also cloned alongside.

Your job: produce one Markdown file at
`daily-digest/<YYYY-MM-DD>.md` summarising the last 24h of activity across
the three repos, then commit it to `main` directly. The file is the
permanent record — you also rewrite `daily-digest/LATEST.md` so the
last seven days' TL;DRs are easy to scan from one place.

## Steps

1. **Gather raw signal**. Run `./scripts/digest-inputs.sh > /tmp/digest-raw.json`
   from the workspace repo. The script emits everything you need — CI runs,
   open PRs, recent commits, duration baselines, reliability runs — as a
   single JSON document. Read it.

2. **Read yesterday's digest** if it exists. Find the most recent file in
   `daily-digest/` excluding `LATEST.md` and `README.md`. Use it to
   note any open issues that resolved or persisted ("PR #8 still red after
   3 days" is more useful than "PR #8 red today" in isolation).

3. **Synthesize**. Write today's file using the format below. Be terse.
   Most days the digest is short. If you find yourself filling sections
   with weak signal, leave them empty.

4. **Rewrite the index**. Update `daily-digest/LATEST.md` to show the TL;DR
   blocks from the last seven daily files (newest first), with a link to
   the full file under each.

5. **Commit and push**. Single commit to main:
   ```
   git add daily-digest/
   git commit -m "digest: <YYYY-MM-DD>"
   git push origin main
   ```
   No PR, no review.

## Output format

```markdown
# Daily Digest — <YYYY-MM-DD>

## TL;DR

- Up to 4 bullets. Each bullet is a single line. Anything important
  enough that the user MUST see it before reading further goes here.
- Use ✓ for healthy, ⚠ for noteworthy, ✗ for broken.
- If everything is genuinely fine, write one bullet: "✓ all quiet".

## What shipped

Group by repo. One line per commit. Translate the commit subject into
plain-English impact, not the git-style headline. Skip merge commits
and dependabot bumps unless the bump itself is interesting.

**Travel Agent**
- <plain-English description of what changed and why it matters>

**Travel App**
- ...

**Travel Workspace**
- ...

Skip a repo entirely if it had no notable changes.

## What's stuck

Only list items that match an anomaly rule (see below). Empty section if
nothing is stuck.

## Health deltas vs 7-day baseline

Show the table only if at least one metric changed meaningfully. Format:

| Metric | Today | 7d avg | Δ |
|---|---|---|---|
| Travel Agent CI duration | 4m32s | 4m20s | +12s |
| Open PRs (all repos) | 6 | 5 | +1 |

Skip the section if nothing's changed.

## Anomalies

Specific things that are weird and the user should look into. Empty
section most days. If non-empty, each item names what's anomalous,
the threshold it crossed, and the most likely cause. Examples:

- Travel Agent CI duration up 22% vs 7-day avg. New step in test-db
  job (eval fixture load) is the likely cause — flag for now, fine if
  stable for a week.

- Travel App PR #8 still red after 3 days. Same ECONNRESET on npm ci.
  Probably worth re-running or closing.

If you'd flag fewer than zero things, write "(none)".
```

## Anomaly thresholds

A signal counts as an anomaly only if it crosses one of these:

- **CI duration**: >20% increase vs 7-day average AND >30s absolute
- **Open-PR count**: >2 PRs older than 7 days, or any PR with red CI >24h
- **Dependabot drift**: any dependabot PR older than 7 days
- **Reliability**: any failed Reliability run in the last 5 (cancelled is fine)
- **Activity gap**: zero commits across all 3 repos in a 24h window
- **Workspace-only deltas**: 0 commits in workspace but >5 in either child
  repo (might mean openapi snapshot drift, type pipeline broken)

If a metric just changed by a small amount with no trend, do NOT flag it.
Most numbers wiggle; only sustained drift matters. Compare to yesterday's
digest — if the same anomaly was already flagged, note "still elevated"
rather than treating it as new.

## What NOT to include

- Don't summarize CI logs verbatim. The point is signal, not transcript.
- Don't include green emoji-spam ("✓ tests pass ✓ lint passes ✓ types pass").
  One TL;DR bullet covers it.
- Don't recommend actions unless an anomaly genuinely needs them.
- Don't list every dependabot PR. Aggregate ("3 open, all <2 days").
- Don't reference yesterday's digest in the body — only in your judgment of
  what's actually new.

## Self-discipline reminder

A great digest is one the user reads in 30 seconds and either nods at
("good, nothing to do") or jumps on one specific thing. If your draft is
longer than ~400 words, you've included noise. Cut.

## Edge cases

- **First run** (no prior digest exists): write `LATEST.md` with just
  today's TL;DR. Note "(first digest)" at the top.
- **`digest-inputs.sh` fails**: don't fabricate data. Write a minimal
  digest that says the data-gathering failed, include the stderr, and
  commit anyway so the user sees something.
- **Nothing happened in 24h**: the digest is one bullet under TL;DR.
  Healthy, even.
- **Routine ran twice in one day** (manual `Run now`): the second run
  overwrites the file. Fine.
