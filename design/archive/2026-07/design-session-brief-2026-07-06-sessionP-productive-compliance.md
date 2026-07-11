# Vesper Design Canon — Session P: Productive Compliance (2026-07-06)

Scope: pay the oldest recorded debt in the bundle — the "produce productive-compliance passes for Stay / Costs / Booking / Trust" action recorded in the first governance pass and never executed. Fresh-eyes audits (language + component lenses) found exactly what this pass exists to catch; every finding below carries file:line evidence. Five items. No new features, no new pages.

Standing rules: governance rows first, flip as landed · 393×852 frames · design-system.jsx tokens, NO new local palettes · Interaction Surfaces is LOCKED — it wins every conflict below by prior adjudication.

---

## 1. Re-chrome Stay + Costs sheets onto the Interaction Surfaces spec

`stay-system.jsx` `SSheet` (~line 37) and `costs-system.jsx` `Sheet` (~line 42) are byte-identical twins of each other and conform to a pre-IS chrome: radius 26/34, handle 38×4 r4 at 11px, Cancel/title/Save top bar. The LOCKED IS spec (`vesper-interaction-surfaces-app.jsx` ~184 + `Handle`): radius 20, handle 36×4 r2 hairDark at 10px, kicker+title+close header, 5 snap presets. Rework both sheet shells (and the boards that use them — StaySheet ×7, AddSheet ×4, ExpenseDetail) onto IS chrome. The session-2 adjudication already converted field VALUES to DM Sans; this completes the sheet CONTAINER. BalanceSheet: chrome conforms, but its adjudicated serif card content stays — do not re-litigate.

## 2. De-italicize productive metadata (system data is never italic)

Italic is currently applied to money, dates, and values on PRODUCTIVE pages — system data wearing the voice's clothes:
- `stay-screens.jsx`: ~92 (hold value), ~510 (TERMS value), ~512 (differentiator)
- `costs-screens.jsx`: ~19 ("Settled Oct 19"), ~179 ("owes you €72" — italic money), ~190 ("across 4 travelers · 4 payments to clear"), ~262 ("· paid")
All → roman. Add one line to the register rules in Canon Consolidation: "italic never touches values, dates, or money on productive surfaces."

## 3. Attribute or flatten italic help text

Unattributed italic prose reads as Vesper's voice without earning it. Each instance either gets the spark glyph (becomes a real voice line — max one per sheet/screen) or goes roman sans (system explanation):
- `stay-screens.jsx`: ~33 ("A hold isn't a booking yet…"), ~257 (privacy note "Group sees the stay; only you see €600"), ~542 ("Too close to call — your group should pick")
- `booking-screens-2.jsx`: ~154 (cancel policy), ~166 (multi-traveler explainer), ~195/208/221 (state explainers), ~77 (italic form placeholder → roman)
- `vesper-trip-settings-app.jsx`: ~400 ("Dates help Vesper shape a real itinerary")
- `trust-kit.jsx`: ~133 — an italic-paragraph COMPONENT used as standard body copy across Trust & Controls. Decide once: voice-attribute the few lines that genuinely are Vesper speaking; everything else roman. This is systemic on that page, not one-off.

## 4. The compliance pass itself: Stay · Costs · Booking · Trust & Controls · Trip Settings & Admin

With 1–3 done, run the recorded checklist per page and capture the evidence the governance file has been waiting for: DM Sans leads all surfaces and overlays · at most one attributed voice moment per screen · no decorative card overuse · CTA scale consistent · row shapes trace to Row System (or note the delta) · states compose from State System. Then flip each page's §03 status from NEEDS VISUAL PASS to CANON OWNED with a dated "compliance pass 2026-07-06" note. Trip Settings & Admin is included because it is the only canon page never touched by any session — its pass is likely quick (it was born DM Sans-led).

## 5. Standalone accommodation detail chrome (closes the last coverage-tail item worth drawing)

`/accommodation/[accommodationId]` exists in the app as a standalone route; Stay's ConfirmedDetail artboard assumes trip-tab context ("your share", trip chrome). Draw ONE variant frame: the same detail composition in standalone chrome (own back affordance, no trip tab assumptions) — per the snap rule this is composition, not new design. Record in the route mapping that the standalone route uses this variant.

## Definition of done

Sheets wear IS chrome · zero italic values/dates/money on productive pages · every italic line on the five pages is either spark-attributed or roman · five §03 statuses flipped with dated compliance notes · standalone accommodation frame exists · export a fresh handoff.
