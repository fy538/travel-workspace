# Claude Design Adjudication Brief — Component Consistency (2026-07-09)

**For:** the human, working in Claude Design (claude.ai/design), canon project `Vesper` @ handoff 125.
**Source:** `design/component-consistency-audit-2026-07-09.md` (verified ledger). These are the findings the audit classified **DESIGN-GAP** — the canon disagrees with itself, is missing a spec, or a ruling landed on a page but its specimen `.jsx` wasn't regenerated. **Code cannot proceed on the dependent batches until these are decided**, because there is no single canon to align to.

**How to use this:** each item is a decision, not a task. Make the call in Claude Design, edit the named canon file(s) so the ruling page AND its specimen `.jsx` agree, then re-export the handoff. The "Regenerate" note on each is the thing most often skipped — a ruling page updated while its specimen goes stale is how these gaps were born.

**Working rule (learned from this audit):** when you adjudicate a page, regenerate its specimen `.jsx` in the *same* session. Most of these gaps are exactly that drift.

---

## GATING — these five block code batches CC2–CC4. Do first.

### D1 — Itinerary row: one owner among three canon dialects  ·  *gates CC-cards, unblocks Row System*
**Conflict:** three canon sources define the itinerary/timeline row differently — `row-spec.jsx:213` (TimelineObjectRow: min-height 60, rail 1.5px, node 8/10px), `itinerary-canon.jsx` (SpineRow state register), and `Vesper Row System.html`. Code has `PlanBlockRow` and `TimelineObjectRow` that can't both be right.
**Decide:** bless ONE as the official Row System timeline row. Recommendation: itinerary-canon's `SpineRow` state register, since it carries the block-state grammar the product actually ships.
**Regenerate:** reconcile `row-spec.jsx` and `Vesper Row System.html` to point at the winner; delete the losing dialect's anatomy block.

### D2 — Tab bar: two contradictory specs, kill the dead badge  ·  *gates CC4 chrome*
**Conflict:** `tab-bar.jsx` (VTabBar: radius 30, static docked/inline, **`vesperBadge` default on**) vs the `Vesper Global Chrome.html` bar (different radius/padding, collapse behavior). And `vesperBadge` violates your own recorded NO-badge ruling.
**Decide:** Global Chrome page is canonical. Amend `tab-bar.jsx` to match it; **remove the `vesperBadge` default** outright.
**Regenerate:** `tab-bar.jsx` so the specimen and Global Chrome agree on radius/padding/blur.

### D3 — Sheet field species: VSheetField vs Field  ·  *gates CC4 sheets*
**Conflict:** `sheet-field.jsx` defines `VSheetField` (borderless, hairline-topped row) as the add/edit-sheet field; another canon source uses `Field` (bordered box) for the same sheets. Code hand-rolls both, so there's no target for the stay/costs add-edit migration.
**Decide:** one field species for add/edit sheets. Recommendation: bordered `Field` for data-entry sheets (clearer tap target on device), rescope `VSheetField` to read-rows (stay/costs display).
**Regenerate:** annotate `sheet-field.jsx` with the scope split so it's unambiguous which context each serves.

### D4 — Transact & Trust card families: give them a face  ·  *gates CC-cards*
**Gap:** `Vesper Cards.html` names Transact and Trust as net-new mechanics ("must draw one shared receipt anatomy — header · vesper-line · status · source") but no canonical face specimen exists. Code has no transact/trust branch to build.
**Decide + draw:** design the shared receipt face (the four-part anatomy) and add `FAM` entries (label / spine color / glyph) to the cards kit for both families.
**Regenerate:** `vesper-cards-kit.jsx` / `vesper-cards-families.jsx` with the two new families rendered.

### D5 — Cards kit specimen vs the r14+letterpress ruling  ·  *gates CC-cards*
**Conflict:** `Vesper Cards.html` rules the one paper object = radius 14 + letterpress shadow, six families; but `vesper-cards-kit.jsx` (which `Vesper Action Card Ownership.html` calls the "build from this" source) predates the ruling and renders the old shell.
**Decide:** the 07-09 ruling wins (already shipped in code's `CardSurface`).
**Regenerate:** `vesper-cards-kit.jsx` to r14 + letterpress + six-family FAM (fold D4 into this pass — same file).

---

## NON-GATING — canon hygiene; code has a stopgap or the surface is off-wedge. Batch these whenever.

### D6 — Bless `ErrorState` as a full-page error tier
The State System page (`vesper-state-system-app.jsx:788`) still frames `ErrorState` as legacy debt to be replaced by `StateScreen`, but the H1 ruling blessed a full-page failure look. Add the full-page error specimen to the component kit board and fix the ImplMapping row. (Code ships both today; this just makes the canon honest.)

### D7 — Sub-9pt type floor: scoped exception or raise
The type scale bottoms at `fsMicro 9` (`vesper-tokens.jsx:58`), but the folio ships sub-9 mono stamps — and the canon corpus *itself* has ~82 sub-9 instances (8/8.5 mono kickers) on auth/other pages. Mirror the Atlas ruling-4 precedent: canonize a scoped sub-9 mono-stamp exception in `vesper-tokens.jsx`, or raise the offenders. Pick one and write it into the tokens page.

### D8 — One Vesper mark glyph
Canon has two marks (`vesper-shared.jsx`: `VesperMark` 4+8-point spark SVG vs `VesperEyebrow` '+' plus-mark); code has ~four (incl. Ionicons `sparkles`/`sparkles-outline`). Pick the one true glyph (and, if both survive, the exact contexts for each). This unblocks a clean `components/brand/` port in CC3.

### D9 — Dismissal secondary-action register
`Vesper Cards.html` CARD ACTIONS: navigational secondary = "DM Sans, ink, underlined"; dismissal secondary = "serif italic, mute." The italic dismissal contradicts your own "italic = Vesper voice only" law. Amend the dismissal row to the sans quiet register, or explicitly carve it out as a sanctioned exception. (Drives the CC3 voice sweep — until decided, code can't tell a violation from a rule.)

### D10 — Costs voice-line budget in populated states
`Vesper Productive Type & Material.html` is contradictory-by-admission: QA gate says "no serif/italic in any populated ledger state," but `VesperVoiceLine` is defined for empty/invite states. The open question is narrow: does the ≤1-italic-line-per-viewport budget apply to *populated* costs states? Answer it, then CC3 either blesses or converts the three code sites.

### D11 — Housekeeping (bundle into any session)
- **Handle metric:** `sheet-header.jsx` says 34×4; everything else says 36×4. Re-point at the shared `VHandle` (36×4). No code change.
- **Places header:** the Header Audit still maps Places → Family A3 reader, but the product moved to hero-first (Family B). Amend the Header Audit row to Family B.
- **Motion tokens:** `vesper-tokens.jsx:75-76` vs the motion page vs `constants/motion.ts` disagree by 10–40ms. Pick the module's shipped values (visually near-nil) and make the canon match.
- **PublicHeader wordmark:** `public-header.jsx` renders mono amber "VESPER"; the Header Audit Family shows serif ink. Serif ink shipped and matches the brand-type law — update `public-header.jsx`.
- **Family A registers:** ratify in the Header Audit that Family A = `ProductiveHeader` base + sanctioned registers (ScreenHeader / EditorialMasthead / CompactHeaderBar). Code already does this; the page just needs to say so.

---

## After you re-export
Run `python3 scripts/canon-drift-check.py` — it will flag every surface whose canon files you touched as stale. That's expected; it's the signal telling the code batches below which surfaces to re-verify against the new handoff.
