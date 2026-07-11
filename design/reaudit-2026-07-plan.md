# Full Re-Audit 2026-07 — the zero-trust pass

**Decision (2026-07-11):** reset every verification verdict in `surface-manifest.yaml` and re-earn them all against handoff 134. All 25 previously-verified rows (12 `aligned` + 13 `partial`) are now `status: stale`. This supersedes the earlier incremental strategy ("trust old verdicts, audit only the unmapped rows").

## Why reset

1. **Verdicts compounded across 26 handoffs.** `aligned_at` values range 108–129; canon is at 134. The drift-checker guards each individual sync step, but a chain of 26 "no change to your files" checks is a weaker claim than one fresh look.
2. **Code moved underneath every verdict — and nothing tracks that.** `aligned_at` only records canon-side movement. Since handoff 108 the code absorbed batches A–H, CC1–4, D1–D22 follow-ups, and at least two *concurrent* Claude sessions committing to the same repos (the manifest itself took a broken-YAML merge collision this week). "Aligned at 108" says nothing about today's code.
3. **The audit protocol got better mid-campaign.** Early verifications (108-era) predate the disciplines that later audits proved out: verify-before-flagging, substrate-gated classification, whole-file reads, the D-numbered adjudication loop. Early verdicts were made to a lower standard.

## What survives the reset

- **The mapping** (canon files ↔ code paths per surface) — still trusted, that's correspondence, not judgment.
- **`aligned_at`** — kept as history ("last verified at"), with `# was: aligned/partial` comments per row.
- **Notes** — kept verbatim. Partial-row residuals (Deck.tsx raw Modal, costsViewModel `masked:false`, State System H1 migration, …) are live leads the re-audit should confirm or close.
- **The two `deferred` rows** (Discover, Atlas) — those are product freeze decisions, not verification claims. Untouched.
- **`pending-canon`** (Planning-Progress Cards) — a design-side ratification item, not a code audit item. Untouched.

## Exit criteria per surface

A `stale` row returns to `aligned`/`partial` only via a fresh audit pass that:

1. **Reachability check first**: confirm each code file is actually rendered/reachable (imported AND rendered somewhere live) before spending audit effort on it. The architecture-simplification audit caught CC batches polishing `DeckCompareFace.tsx` — zero renders anywhere, 3 alignment commits. Dead code gets flagged for deletion, not aligned.
2. Reads the surface's canon files **fully** (mirror @ ≥134) and its code files **fully**.
3. Produces a findings ledger with `file:line` citations, every finding verified against the actual files before recording (no code-default guesses — trace the real path).
4. Classifies each finding: **code-owes-canon** (→ fix batch) · **canon-owes-code** (→ next D-numbered adjudication brief) · **substrate-gated** (real data doesn't exist yet; not fakeable) · **confirmed-aligned**.
5. Updates the manifest row: re-earned status, `aligned_at: <handoff checked>`, **`code_verified_at: <travel-app HEAD short sha>`** (new field — makes code-side movement trackable next time, closing the blind spot that motivated this reset), fresh notes.

## Waves

**Wave 0 — instrumentation + complete the map** (prerequisite; everything else operates on a complete map)
- Inverse-sweep script: diff `app/` routes + `components/` dirs against all manifest `code:` paths → orphan list (shipped UI with no canon row — how Planning-Progress Cards and Deck.tsx were caught only by accident). Standing command, sibling to `canon-drift-check.py`. Must check **reachability** (imported AND rendered), not just existence — the standing version of arch-simp's one-off orphan hunt, built to catch the DeckCompareFace class.
- Consume the arch-simp FE deletion list (`docs/working/architecture-simplification-2026-07.md`, FE finding 5 + Tier 0): DeckCompareFace, AtlasRoomArt, AtlasYearStepper, DNAStrip, StoryArchiveCard, TripLogCard, VerdictChip, Atlas tombstone routes. These are flagged-for-deletion — exclude from all audit scope; if any manifest row's `code:` paths reference them, note it.
- Code-movement check: flag rows whose `code:` paths have commits after `code_verified_at` (symmetric counterpart to canon drift).
- Backfill the three falsely-unmapped rows (Chat / Itinerary / Onboarding — all had real audit work this week) and map the 7 true blanks (Route & Transport, Booking & Reservation, Trust & Controls, Photo & Media Intake, External Sharing, Guide & Collection Reader, Saved & Collections — all have real code dirs).

**Wave 1 — families first (8 surfaces).** Tokens · Buttons · Row System · Sheets · State System (family) · Header system · Voice registers · Cards kit. Product surfaces compose from these; family verdicts become citable downstream ("title uses `typography.h1Dense` — verified Wave 1") instead of re-derived per screen.

**Wave 2 — wedge-core product surfaces (~13).** The multiplayer-coordination wedge (J02→J05→J12 order of importance): Auth & Invite · People & Collaboration · Chat · Itinerary · Changes · Proposal & Decision Detail · Trips Home · Trip Creation · Global Chrome · Notifications · Costs · External Sharing · Trip Story.

**Wave 3 — remainder (~14).** Stay · Booking & Reservation · Route & Transport · Universal Search · Trust & Controls · Interaction Surfaces · State System (screens) · Motion · Trip Settings & Admin · Places · Photo & Media Intake · Saved & Collections · Guide & Collection Reader · Onboarding.

After each wave: one findings ledger doc, one fix batch (code-owes-canon items), D-items accumulate into the next adjudication brief for Claude Design. Don't let ledgers pile up unfixed across waves — fix-as-you-go kept batches A–H honest.

## Coordination with architecture-simplification-2026-07

The concurrent structural audit (`docs/working/architecture-simplification-2026-07.md`) does not conflict — different axes (structural complexity vs canon↔code fidelity), and its Do-NOT-touch list explicitly protects this campaign's mechanism (manifest + drift-check + mirror + design-alignment loop). Four coordination rules:

1. **Tier-0 deletions land before audits.** Don't audit code arch-simp is about to delete — its orphan list is consumed in Wave 0 and excluded from audit scope. If its Tier-0 FE deletions haven't landed by the time a wave reaches the affected surface, skip those files and note it in the row.
2. **Reachability is an audit precondition** (exit criterion 1) — the DeckCompareFace lesson: alignment campaigns polished a component with zero renders. Never again.
3. **Trips Home / folio = one churn event.** Arch-simp defers splitting `TripFolioHome.tsx` until the queued folio redesign; Wave 2's Trips Home findings should fold into that same redesign/split window, not churn the file separately.
4. **Doc hygiene**: arch-simp archives 66 dated briefs to `design/archive/2026-07/`; this campaign's wave ledgers and briefs follow the same convention as waves close — don't refill the drawer it's emptying.

Where arch-simp's Tier 2–3 rewrites FE files under fresh verdicts (persona Cut 3, typed request wrapper, wire-card-model convergence), `code_verified_at` flags the affected rows for re-check — that's the mechanism working, not a conflict.

## Execution mechanics

- Parallel read-only audit subagents, ~4–6 surfaces per batch; findings spot-verified by the main session against the actual files before any manifest row changes (agent findings are leads, not verdicts).
- Manifest rows are only ever updated by the main session, post-verification — one writer, no merge collisions.
- Canon reference is the mirror (`design/vesper-canon-anchor/project/` @ 134), not Downloads — if a new handoff lands mid-campaign, sync first, then keep going; the drift-checker will say which in-flight verdicts it invalidates.
