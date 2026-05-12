# Daily Digest

Nightly CI/CD + shipping snapshot, generated automatically by a Claude
Code routine around 9pm America/New_York. The routine reads recent
activity across the three repos, judges what's signal vs. noise, and
commits a one-page summary here.

## How to use this

**In the morning**: open `LATEST.md`. It shows the TL;DR blocks from the
last seven daily files in one place. Anything flagged ⚠ or ✗ is worth a
30-second look. Anything quiet means yesterday was quiet — read no
further.

**For an individual day**: open `<YYYY-MM-DD>.md`. Each daily file has the
full breakdown:

- TL;DR — the 30-second read
- What shipped — commits in plain English
- What's stuck — open PRs / dependabot drift / red CI >24h
- Health deltas — only shown when a metric moved meaningfully
- Anomalies — specific weirdness, with the threshold that triggered it

**Catching up after a few days off**: open the most recent
`<YYYY-MM-DD>.md`, then walk backwards. The digest is designed so missing
a day or two doesn't leave you blind — anomalies persist across days
("still elevated") rather than appearing as new.

## Anatomy of the system

```
daily-digest/                       ← This folder. Files committed here daily.
├── README.md                       ← This file (static, hand-written).
├── LATEST.md                       ← Auto-regenerated every run. Last 7 days' TL;DRs.
├── 2026-05-12.md                   ← One per day.
└── ...

.routines/
└── daily-digest.md                 ← The routine's prompt. Edit to tune behaviour.

scripts/
└── digest-inputs.sh                ← Raw data gathering (bash + gh + jq).
                                      The routine runs this, then synthesizes.
```

## Tuning

If the digest is too noisy → tighten the anomaly thresholds in
`.routines/daily-digest.md`. If it's too quiet and missing things → loosen
them. The prompt file is plain Markdown; edits take effect on the next
nightly run.

If the data gathering needs a new field → edit `scripts/digest-inputs.sh`
and the prompt section that consumes it.

## When the routine breaks

A failed run shows up as a digest file containing only an error message
(by design — the prompt instructs the routine not to fabricate when
`digest-inputs.sh` fails). The routine still commits, so the absence of a
file means the routine itself didn't fire. Check
[claude.ai/code/routines](https://claude.ai/code/routines) for run history.
