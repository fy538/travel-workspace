# Code Alignment — Batch CC2: Card Chrome Adoption (2026-07-09)

Repo: `~/travel-workspace/travel-app`. Canon mirror: `~/travel-workspace/design/vesper-canon-anchor/project/` (handoff 125, read-only). Ledger: `design/component-consistency-audit-2026-07-09.md`, family **cards**. The six-mechanics core landed clean (`utils/vesperCardFamilies.ts`, the seven faces on `CardShell`+`CardHead`+`ActionRow`, `CardSurface` r14+letterpress). This batch brings the **stragglers** onto that kit.

## Blocked-until
- **Tasks CC2.4 (Transact/Trust) and the kit-specimen reconciliation depend on adjudications D4 + D5** in `adjudication-brief-2026-07-09-component-consistency.md`. Do NOT start CC2.4 until handoff ships those. CC2.1–CC2.3 are unblocked — start there.

## Standing rules
Same as CC1 (git status first; snap to tokens; one commit/task; typecheck+tests green; no push without approval).

## Task CC2.1 — ChatCardFrame onto CardShell  ·  severity HIGH
Canon: `Vesper Cards.html` — one paper object, r14 + letterpress, for every card including chat cards. Code: `ChatCardFrame` (the chat card chrome) hand-rolls its own shell instead of composing `CardShell`/`ui/CardSurface`. Migrate it so chat cards inherit the canonical radius/shadow/padding. Verify the seven in-chat card faces still render identically after (they should get *more* consistent, not less). This is the highest-traffic card surface — highest payoff.

## Task CC2.2 — Hand-rolled card shells onto CardSurface  ·  severity MEDIUM
Canon: same one-paper-object rule. These four bypass `CardSurface` with their own radius (r9–14, drifting):
- `StayCard` (inlines r14 — close, but not via CardSurface)
- `CostsEstimateCard`
- `TripLogCard`
- `FolioReceiptCard`
Migrate each onto `CardSurface`. Where a card needs a genuinely different chrome (e.g. receipt hairline), pass it as a prop rather than forking the shell. Grep for their render sites and confirm no layout regressions.

## Task CC2.3 — Deck shell + five deck faces  ·  severity MEDIUM
Canon: `vesper-deck-entry.jsx` / Deck card specs — deck faces are the same paper object. Code: the Deck shell owns chrome separately and five deck faces (`components/focus-home/**/Deck*Face.tsx`) re-type it. Route them through the shared `CardShell`/`CardSurface`. **CTA pill recipe:** the deck faces also hand-roll their action pills — consolidate onto the one Btn recipe from CC1.1 (`ui/Button`). Note: the audit's original CTA line-cites were partly wrong (they pointed at tag chips, not CTAs) — find the actual CTA pills in each face, don't trust the stale line numbers.

## Task CC2.4 — Transact & Trust faces  ·  severity MEDIUM  ·  BLOCKED on D4+D5
Once D4 (Transact/Trust receipt face designed) + D5 (kit specimen regenerated) ship in a new handoff: add the explicit `transact`/`trust` branch to the face dispatch in `components/vesper-cards/` and build the two faces from the new canon receipt anatomy (header · vesper-line · status · source). Add their `FAM` metadata. Until the handoff lands, leave the fallback face in place.

## Task CC2.5 — De-triplicate family metadata  ·  severity LOW
Family labels / glyphs / colors are defined three times in code. Collapse to one source (extend `utils/vesperCardFamilies.ts`) so a new family (like Transact/Trust) is a one-place edit. Do this last so CC2.4 lands into the consolidated map.

## Done
Chat cards on CardShell · four hand-rolled cards on CardSurface · deck faces + CTAs consolidated · (post-handoff) Transact/Trust faces built · family metadata single-source · report confirms all seven+ faces render on one paper object and lists any face that needed a real chrome prop.
