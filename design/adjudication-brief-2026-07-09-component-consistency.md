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

## BUTTON VARIANT TAXONOMY — surfaced during CC1.1 execution (2026-07-09)

Different origin from D1–D11 above: these weren't found by the canon audit — they surfaced while actually converting ~25 hand-rolled CTAs onto the shared `ui/Button` component (Bucket 1, 11 commits, `e5d39291..d4da4157` on `cc1-atom-adoption`). Every item below has a concrete file:line and, where relevant, an exact hex value — verified by reading the code, not inferred from a screenshot. **These don't block CC2–CC4** (card chrome / voice / sheets — unrelated surfaces); they block finishing the CTA-conversion work and future Button call sites.

### D12 — Button variant taxonomy — **RESOLVED, recorded for the audit trail**
**Decision (made 2026-07-09, fast-tracked against existing canon rather than a full session):** the canon (`buttons.jsx` VBtn: r22 pill, h44/h36) already disagreed with code's `ui/Button` (was r12 rounded-rect). Adopted canon: Button's `sm`/`md` sizes are now the r22 stadium pill; `auth` (r14/h52) stays the sanctioned exception. Added a `tint` variant (subtle espresso-tint fill + action text) for low-emphasis fill CTAs that previously had no home. Shipped in `a0a7c657`. No further action — this entry exists so a reader of this doc doesn't wonder why Button's shape changed mid-project.

### D13 — Solid-emphasis destructive/urgency fill  ·  affects 4+ sites
**The gap:** Button's `danger` variant is text-only (red text, transparent background) — but several real CTAs use a **solid** warning/danger fill, and one wants a specific text color Button can't currently express at all:
- `components/trip-plan/ChangeStudioSheet.tsx:329` "I understand — see alternatives" — solid `terracotta[600]` fill, white text (booked-block risk acknowledge gate).
- `components/trip-plan/MoveBlockSheet.tsx:488` "I understand — continue" — identical solid `terracotta[600]` treatment (same species, different sheet).
- `components/focus-home/DeckCallFace.tsx:159` — dynamic accent fill (`oxblood` for urgency, muted when `isExpired`), disabled wiring on `isExpired||isPending`. Not solid-color-fixed like the other two — accent-driven.
- `components/expense/ExpenseDetail.tsx` "Delete expense" — text-only `terracotta[400]` (a **different**, lighter terracotta than the above — softer, restrained, deliberately less alarming for an inline scroll action). **Button has no mechanism to override just the label text color** — only a container-level `style` prop. Left hand-rolled; could not convert even if the color were approved, without an API change.

**Two separable questions:**
1. Should Button get a **solid-fill danger/warning variant** for hard-gate acknowledge patterns (terracotta[600]/white)? Recommend yes — this is a real, recurring pattern (2 near-identical sites already, DeckCallFace is a close cousin).
2. Should Button expose a way to **override just the label color** (a `textColor` prop), so cases like the softer inline `terracotta[400]` delete don't require forking the whole component? Recommend yes, low-risk addition — many design systems have this as an escape hatch precisely for restrained/soft destructive actions.

### D14 — Per-surface button primitives  ·  affects 2 local component families, real counts below
**The gap:** two areas of the app built their own local button system before `ui/Button` existed, and now Button and these primitives both exist with overlapping purpose:
- **`CostsReceiptButton`** (`components/expense/CostsPrimitives.tsx:44`) — `{tone, ghost, full}` props, a receipt-shaped visual family. **3 call sites**: `CostsHeader.tsx`, `CostsEmptyState.tsx:57` ("Add first expense"), `CostsBalanceSheet.tsx`. Low count, and distinct enough visually (ticket/receipt framing) that it reads as a deliberately different species, not debt.
- **`StayButton`/`SBtn`** (`components/stay/StayCard.tsx:31`) — `{tone, ghost}` props. **10 call sites**: `StayCard.tsx` (2), `StayCompare.tsx` (2), `StayHome.tsx` (6, incl. `:144` "+ Add somewhere to stay"). Meaningfully more reused than the receipt button.
- **Precedent that consolidation is tractable:** `DeckBtn` in `components/focus-home/DeckStructuredFace.tsx` was exactly this kind of local wrapper and got folded into `Button` cleanly during CC1.1c (now composes `Button` internally, call sites unchanged) — worth looking at as the template if the decision is "fold in."
- **Also gated on this decision:** `components/trip-plan/ConflictResolutionSheet.tsx` "Keep it" — a flat `#F5F4EF` (`colors.background.secondary`) fill that matches neither `tint` (6% alpha) nor `secondary` (outline). Not a named primitive like the two above, but the same underlying question: does the app want a **soft neutral-fill** button species, and if so what's its token?

**The decision, now with real numbers:** StayButton's 10-site reuse favors folding into Button (one edit fixes 10 places, following the DeckBtn precedent) — add whatever props are missing (likely a `tone`-equivalent). CostsReceiptButton's 3 sites and distinct ticket-shaped visual identity favor blessing it as a sanctioned local species instead — low leverage to fold in, and it may be deliberately not a generic button. Recommend confirming both calls in the design session, not just accepting this read.

### D15 — On-dark button treatment  ·  affects 3 sites, 1 file
**The gap:** `components/trips/TripsHomeViews.tsx` has cream (`#F2EAD9`) and ink pills ("Tell Vesper a place" at line 116, "Walk me there" at lines 581/614) that sit on **dark scene overlay photography**, not the paper/cardWarm surfaces Button's `tint`/`primary` tokens assume. A blind snap to `tint` (6% alpha espresso) would be closer to invisible than the current opaque cream. Also: these pills have a trailing icon (arrow-forward); Button only supports a **leading** icon.

**The decision:** does Button need an `onDark` treatment (inverted contrast for photo/dark backgrounds), or do these three stay as a documented exception? Given it's isolated to one file/pattern (the hero photo overlay), a documented local exception may be more proportionate than a new Button variant used in exactly one place — but flagging both options since the trailing-icon gap would need solving either way.

### D16 (new, unnumbered in the original DESIGN-GAP list) — Dense inline row-chip species  ·  recurring pattern, not a one-off
**The gap:** `components/trip-plan/PlanBlockRow.tsx` has two small affordances embedded in a dense, indented (`paddingLeft: 56`) itinerary row — "Change" (`changeButton`: r8, `paddingVertical: spacing.xxs`, `paddingHorizontal: spacing.sm`) and "Done" (`doneChip`, checkmark + text, no fill at all). The "Done" affordance carries an explicit in-code design comment: *"Light affordance — secondary text, no filled bg."* Button's floor is a **44px-minimum, card/sheet-footer-scaled pill** — forcing either of these onto it would make a small, glanceable inline chip suddenly dominate a dense list row.

**This isn't isolated to PlanBlockRow.** A repo-wide grep for the same "small radius + xxs/xs padding" combination also turns up `NowModeStrip.tsx` and `BlockProposedBanner.tsx` — both of which the original component-consistency audit already separately flagged as "distinct species, LEAVE" (segmented/toggle-over-dark-card). Between these, there's a real, recurring pattern: **compact, low-emphasis affordances embedded inside dense list/timeline rows are a different UI species from card-footer CTAs**, and right now the app has no shared primitive for them — every instance is a bespoke local `Tap` + styles.

**The decision:** worth a small `InlineChip`/`RowAction` primitive (compact, no 44px floor, optional fill) as a sibling to `Button` rather than an extension of it? This is lower urgency than D13–D15 (nothing is actively broken; these are all correctly still hand-rolled) but worth resolving before more of these accumulate — it's exactly the kind of "same thing re-typed per surface" pattern this whole audit exists to catch before it does.

### Priority for the design session
Recommend this order, roughly by leverage/urgency: **D14** (highest call-site count, unblocks the Costs and Stay surfaces broadly) → **D13** (small site count but touches trust/destructive-action correctness) → **D16** (define the primitive now, before more dense-row chips accumulate) → **D15** (isolated, lowest urgency, may resolve to "leave as documented exception" with no code change at all).

---

## After you re-export
Run `python3 scripts/canon-drift-check.py` — it will flag every surface whose canon files you touched as stale. That's expected; it's the signal telling the code batches below which surfaces to re-verify against the new handoff.
