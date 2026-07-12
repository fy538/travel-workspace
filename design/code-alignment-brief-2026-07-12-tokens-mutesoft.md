# Code Alignment Brief — Tokens Campaign (muteSoft + follow-ons) (2026-07-12)

**Status:** T0–T7 landed locally (awaiting push/merge) · **Lane:** Tokens (family)  
**Repo:** `travel-app` from `origin/main` · isolated worktrees · pathspec commits  
**Canon:** `vesper-tokens.jsx`, `token-reference-app.jsx`, `Vesper Design Tokens.html`, Productive Type & Material  
**Prior:** CC4.4 (`d4bc893b`) migrated 104 text sites; CC4.5 locked `check-muteSoft-budget.mjs` at **286**. Remaining ~300 raw `.muteSoft` hits are mixed text + decorative — do **not** blind-replace.

---

## TL;DR

Drive remaining **text-role** `muteSoft`/`ink80` → `mute`/`ink60` (AA). Keep decorative uses. Lower the muteSoft budget as we go. Optionally snap `blue60`/`planningInk` and chip at color-budget leftovers.

| PR | Focus | Target |
|---|---|---|
| **T0** | Classifier + doctrine note | Script/docs: text vs decorative heuristics |
| **T1** | Trips home / folio cluster | Top hotspots: `TripsHomeStyles`, `TripHeroCard`, `TemptHero`, `tripFolioStyles`, `TripFolioHome` |
| **T2** | Stay / Costs / accommodations | `trip-accommodations`, `ExpenseDetail`, `StayCard`/`StayCompare`/`StayRow` |
| **T3** | Discover / chat / search | `DiscoverCoverHome`, `VesperChatCardKit`, `UniversalSearchOverlay` (+ atlas feedback if cheap) |
| **T4** | `planningInk` / `blue60` | Adjudicate snap `#3D5066` → canon `#2A5A8A` **or** document deliberate divergence |
| **T5** | Ratchet + manifest | Lower `BASELINE` in muteSoft (+ color if improved); Tokens row notes |

**Parallel OK:** T1 ∥ T2 ∥ T3 after T0 heuristics are written. T4 independent. T5 last.

---

## Doctrine (locked)

From colors.ts + contrast brief:

- `mute` / `ink60` (`#6E6862`) — lightest ink that may carry **text** (AA).
- `muteSoft` / `ink80` (`#B5AFA5`) — **decorative only**: icon tints, borders, hairlines, underline decoration, empty-state illustration washes, disabled chrome that is not readable copy.
- **Kickers / caps eyebrows:** contested. Notifications canon often uses muteSoft for kickers; Row System says non-Vesper kickers are mute. **Default for this campaign:** if the style is `typography.caps*` / kicker / eyebrow and **≥11px readable label**, migrate to `mute` unless the file is Notifications and already matching notifications-app muteSoft kickers (leave those; note in PR).

### Classification heuristic (T0)

A `.muteSoft` use is **TEXT (migrate → mute)** when it appears as:

- `color: …muteSoft` / `color: colors.*.muteSoft` on a `Text` / typography text style
- style keys clearly named `*Text`, `*Label`, `*Title`, `*Body`, `*Meta`, `*Caption`, `*Subtitle`, `*Kicker` (except Notifications kickers — see above)

A use is **DECORATIVE (keep)** when:

- `borderColor`, `backgroundColor`, `shadowColor`, `tintColor`, icon `color=` on Ionicons/Svg
- underline / decorationColor
- comment or token file defining the alias itself (`constants/colors.ts`)

**UNCLEAR:** leave + list in brief appendix; do not guess.

---

## Explicit OUT of scope

- Redesigning the palette hex set beyond planningInk adjudication.
- muteSoft inside `constants/colors.ts` token definitions.
- Discover/Atlas full surface redesign (only token color swaps in touched files).
- Blind global sed `muteSoft`→`mute`.

---

## PR-T0 — Classifier + doctrine (small, first)

1. Add `scripts/classify-muteSoft.mjs` (dev helper, not CI gate) that walks app/+components/, prints CSV/markdown buckets: TEXT / DECORATIVE / UNCLEAR with file:line.
2. Add short note to `constants/colors.ts` above `muteSoft` if not already crystal-clear (one comment block).
3. Commit on `polish/t0-mutesoft-classifier`.

---

## PR-T1 — Trips home / folio cluster

Migrate TEXT-classified sites in:

- `components/trips/TripsHomeStyles.ts` (14)
- `components/trips/hero/TripHeroCard.tsx` (10)
- `components/trips/TemptHero.tsx` (4)
- `components/trip/tripFolioStyles.ts` (5)
- `components/trip/TripFolioHome.tsx` (3)
- related `TripsHomeCards.tsx` / `StoryReadyEntry.tsx` if TEXT

Lower muteSoft budget by the migrated count.

---

## PR-T2 — Stay / Costs / accommodations

- `app/trip-accommodations/index.tsx` (13)
- `components/expense/ExpenseDetail.tsx` (8)
- `components/stay/StayCard.tsx`, `StayCompare.tsx`, `StayRow.tsx`

Same rules. Keep receipt hairlines / icon tints decorative.

---

## PR-T3 — Discover / chat / search

- `components/discover/DiscoverCoverHome.tsx` (11) — careful: on-dark hero may need `colors.atlas.*` or paper mute, not wrong token on photo
- `components/chat/VesperChatCardKit.tsx` (5)
- `components/search/UniversalSearchOverlay.tsx` (5)
- Optional: `app/atlas/feedback.tsx` (7) if clearly text

On-dark photo chrome: if muteSoft is used as light-on-dark wash, that may be decorative — classify carefully; do not force `mute` if contrast on photo was intentional wash.

---

## PR-T4 — planningInk / blue60

Canon status/productive blue: `#2A5A8A`. Code `blue60` / `planningInk`: `#3D5066`.

Options (pick one in PR):

- **A (prefer):** Snap `blue60` to `#2A5A8A` and verify Stay/Costs “productive” surfaces; adjust Soft/Deep if needed for hierarchy.
- **B:** Document deliberate navy divergence in `colors.ts` + Tokens manifest notes; no value change.

Do not half-snap Soft/Deep without checking Live blues.

---

## PR-T5 — Ratchet + manifest

1. Set `scripts/check-muteSoft-budget.mjs` `BASELINE` to post-migration count.
2. If color-budget drops, lower `BASELINE` there too.
3. Update Tokens (family) `surface-manifest.yaml` notes + `code_verified_at`.
4. Append remaining UNCLEAR list to `design/reaudit-2026-07-open-findings.md`.

---

## Execution log (2026-07-12)

| PR | Branch | Result |
|---|---|---|
| T0 | `polish/t0-mutesoft-classifier` | `classify-muteSoft.mjs` |
| T1 | `polish/t1-mutesoft-trips` | trips/folio TEXT → mute |
| T2 | `polish/t2-mutesoft-stay-costs` | stay/costs TEXT → mute |
| T3 | `polish/t3-mutesoft-discover-chat` | discover/chat/search TEXT → mute |
| T4 | `polish/t4-planning-ink` | Option A: `blue60`/`planningInk` → `#2A5A8A` |
| T5 | `polish/tokens-t5-integrate` | merged T0–T4; muteSoft `BASELINE` **237** |
| T6 | `polish/t6-mutesoft-atlas-text` | Atlas TEXT cluster (+ goodbye, trips/all); **237→211** |

Post-T7 classifier: **Total 134 | TEXT 0 | DECORATIVE 101 | UNCLEAR 33**. Campaign success metric met (≤~200, stretch ≤150). Remaining UNCLEAR is mostly icon/chrome/token-alias/ternary — not blind-migratable.

### Remaining TEXT (post-T7)

**0** — classifier TEXT bucket empty.

### Remaining UNCLEAR (count)

33 sites — icon tints, ActivityIndicator, tab inactive tint, token aliases, a few ternaries. Full list via `node scripts/classify-muteSoft.mjs`. Do not blind-migrate.

---

## Verification (every PR)

```bash
cd travel-app
node scripts/check-muteSoft-budget.mjs
node scripts/classify-muteSoft.mjs   # if present
npx tsc --noEmit -p .
# smoke any touched surface tests if they exist
```

---

## Success metric

| Metric | Before | After campaign |
|---|---|---|
| muteSoft raw count (budget) | 286 | **134** after T7 |
| Known body/caption text on muteSoft in T1–T3 files | many | ~0 |
| planningInk | unreconciled | **snapped** to `#2A5A8A` (T4) |
| Tokens manifest | partial, stale | notes + sha |

Campaign closes when T1–T3 land, budget lowered, T4 decided, T5 bookkeeping done — not when muteSoft hits zero (decorative uses remain by design).
