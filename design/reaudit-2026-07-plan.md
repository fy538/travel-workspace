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

**Wave 0 — instrumentation + complete the map** ✅ DONE 2026-07-11 (commit `30e3f8d`)
- `scripts/canon-surface-orphans.py` — inverse sweep, sibling to `canon-drift-check.py`. Buckets MAPPED/PARTIAL/ORPHAN/EXCLUDED with a reachability grep on orphan files (catches the DeckCompareFace class: imported nowhere ≠ a real audit target).
- Consumed the arch-simp FE deletion list as an EXCLUDED bucket (0 hit this run — those files still live at top-level under already-partial dirs, will re-check once arch-simp's Tier 0 lands).
- **First run found 45 orphans, not the estimated 7** — most "unmapped" surface code was simply missing from existing rows' `code:` lists. Backfilled Chat/Itinerary/Onboarding (falsely unmapped — real audit work already happened this week), expanded 11 existing rows, mapped all 7 originally-scoped blanks, and surfaced one nobody had scoped at all: **Voice (narration + live mic)** — real, shipped, dark-subsystem code with zero manifest presence, not even a blank row.
- Trust & Controls and Saved & Collections came back Atlas-adjacent (only call sites are `app/atlas/*`); Guide & Collection Reader came back Discover-adjacent (`components/discover/reader/`, dossier/angle routes) — noted in-row so their audit fate follows those freeze decisions rather than running independently.
- Final state: **0 orphans**, 39 rows (28 stale / 8 unmapped-now-mapped / 1 pending-canon / 2 deferred).
- **Not yet built**: the code-movement check (flag rows whose `code:` paths moved since `code_verified_at`) — no row has a `code_verified_at` stamp yet since none has been re-verified this campaign. Build this once Wave 1 starts producing verified rows.

**Wave 1 — families first (8 surfaces)** ✅ DONE 2026-07-11 (commit `f65ddf2`, workspace; `c7f20ada`, travel-app)
- Tokens · Buttons · Row System · Sheets · State System (family) · Header system · Voice registers · Cards kit — each audited by a parallel agent (full canon+code reads, file:line-cited findings), with 3 of the most consequential claims spot-verified directly before trusting: all confirmed accurate.
- Result: **7 partial, 1 gap** (Voice registers). Every row now carries a real `aligned_at:134` + `code_verified_at` (travel-app HEAD sha) stamp — the first genuinely re-earned verdicts in this campaign.
- **Two prior "aligned" verdicts were wrong**, caught only by re-reading the actual files: Header system's "no code change" claim (story.tsx's `MemoryStoryHeader` is a real unmigrated fork, deliberately deferred by the J1 brief, closed anyway by a later session without re-checking); Voice registers' "fully ALIGNED, no known code gaps" (VesperSignature — the primitive behind ~30 chat/notes/Discover/Places consumers — renders a bare `+`, which canon's D8 explicitly names as NOT the brand mark).
- **Fixed live**: Row System's `failed` booking overlay had a halo canon explicitly rules out (travel-app `c7f20ada`).
- **Not fixed yet, flagged as fix-batch candidates**: Buttons' missing ghost-variant border + never-built CostsReceiptButton notch silhouette; Cards kit's Trust spine color off by one hex digit; Sheets' unused `edit` chrome (canon's own SectionEditSheet doesn't use it); State System's ErrorState/StateScreen fork (two visual treatments of one blessed tier, live simultaneously).
- Code-movement check: still not built — now has real `code_verified_at` stamps to check against, this is unblocked for whenever it's worth building.

**Wave 2 — wedge-core product surfaces (~13)** ✅ DONE 2026-07-11 (commit `74d0d2f`)
- Auth & Invite · People & Collaboration · Chat · Itinerary · Changes · Proposal & Decision Detail · Trips Home · Trip Creation · Global Chrome · Notifications · Costs · External Sharing · Trip Story — 13 parallel audits, 4 of the most surprising claims spot-verified directly (all confirmed accurate).
- Result: **19 partial, 2 gap**. Every row got `aligned_at:134` + `code_verified_at`.
- Same pattern as Wave 1 — "confirmed" verdicts kept not surviving direct re-check: Changes' "Ask-the-Organizer (net-new)" was never wired into the Changes screen at all (its canon file isn't even loaded by the Changes HTML bundle) — re-homed to Trip Settings & Admin, where the pattern actually lives. Proposal & Decision Detail's "3-states"/"closed-recovery" claims both partly false. Auth and Invite's flagged-as-never-checked sign-in/OTP code got its first real read and found real drift.
- **Trip Story graduates to `gap`** (joining Voice registers): place chips/route-cue hardcoded empty throughout the entire backend projection builder despite full schema+canon spec; the 9:16 share-card and public landing page's CSS/placeholder env vars are byte-identical to the unrelated `invite_landing.py` — strong evidence the invite surface's template was copied wholesale without a Vesper brand pass.
- Global Chrome: real background-alpha miss (0.78 vs canon's 0.92) plus a structural finding — 3 of 6 mapped code files (app-shell/boot) are unfalsifiable against this canon file, which has zero app-shell content. `ErrorBoundary.tsx` re-homed to State System (family), its real canon owner.
- No live fixes this wave — findings ran broader and more judgment-heavy than Wave 1's (product/design calls, not one-line bugs). Left for a scoped fix batch rather than rushed mid-wave.

**Wave 3 — remainder (13, not ~14)** ✅ DONE 2026-07-11 (commit `753fddc`)
- Stay · Trip Settings & Admin · Interaction Surfaces · Motion · Places · Route & Transport · Universal Search · Booking & Reservation · Trust & Controls · Onboarding · Photo & Media Intake · Guide & Collection Reader · Saved & Collections System. ("State System (screens)" from the original list turned out to be a stale duplicate reference — see housekeeping below.)
- 3 of the most surprising claims spot-verified directly (all confirmed): Trip Settings' ungated Vesper-autonomy permissions bug, Motion's canon file having literally zero motion content, and the Wave-1 failed-halo fix surviving a concurrent edit to `PlanBlockRow.tsx`.
- **Manifest housekeeping**: found and fixed two pre-existing duplicates. A standalone `State System` row (same `code:`, different `canon:`) turned out to be content Wave 1's `State System (family)` audit had already read and cited (e.g. `vesper-state-system-app.jsx:143` for D6) — merged and deleted rather than re-auditing. Also caught and fixed a `Universal Search` row I accidentally duplicated mid-edit. Net: 38 rows (down from 40 mid-wave), zero orphans, zero dupes.
- Result: **32 partial total**, no new `gap`-tier surfaces this wave — Stay is the campaign's first case where a confident "5/5 confirmed" claim held up completely unchanged on direct re-check (VESPER PICK backend-gating still honestly undone, blocking-phase vote-arc now has a real endpoint).
- Highlights: Trip Settings & Admin's permissions bug is genuinely security-relevant (any member can silently change group Vesper-autonomy settings, no confirm, no gate). Universal Search's Actions group ships inverted from canon (read-only audit log vs. executable commands) after two previously-deferred features were silently built and never checked. Saved & Collections' state/date/provenance grammar is fully built in the row component but structurally unreachable — the screen's data mapper never sets `state`/`savedAt`, and `provenance` holds venue marketing copy instead of "Saved from X" attribution. Photo & Media Intake's "Remove from trip" deletion is UI-present with no backend delete endpoint anywhere — currently impossible, not just unwired.
- No live fixes this wave, same reasoning as Wave 2 — findings need product/design calls or are too varied for a clean mid-audit sweep.

**Post-wave-3 state**: 38 manifest rows. 1 `unmapped` remains (Voice — narration + live mic, discovered in Wave 0, never assigned to a wave). 2 `deferred` (Discover, Atlas — untouched, product freeze). 1 `pending-canon` (Planning-Progress Cards). Everything else has a fresh Wave 1/2/3 verdict. **Next**: either audit Voice, or shift to executing the accumulated fix-batch backlog across all three waves' findings.

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
