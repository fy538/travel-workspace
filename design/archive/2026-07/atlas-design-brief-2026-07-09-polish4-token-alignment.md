# Atlas — Polish 4: token alignment to Vesper app canon (2026-07-09)

**Paste this whole document into the Atlas design project. It is self-contained — every value you need is inline.**

## Context (read once)

This project (the Atlas memory/composition boards) is one surface of a larger app, Vesper. The rest of the app is designed in a separate project against a single token canon. On 2026-07-05 (this board's own Ruling 01, in the rulings log on the Canonical Experience Board) we decided Atlas adopts the app canon — "Atlas is a tab inside Vesper, not a separate product." That session migrated **typefaces, ink, and gold**. This session finishes the job: **paper, status colors, microtype, radii, and the stale self-documentation** — plus the Implementation Spec's token block, which still teaches engineers the old system.

Do NOT re-open anything settled in Polish 1–3 or Phase 2 (typefaces, home hero, compose flow, timeline material inside a Reading, Moment Actions, Long View structure).

## The Vesper app canon (the complete reference — use these exact values)

**Type families (three only):**
- EB Garamond (serif) — expressive titles & Vesper's voice. Weight 500 for display; italic ONLY when Vesper herself is speaking or for editorial ledes — never on user quotes, values, dates, or money.
- DM Sans (sans) — all UI: buttons, pills, tabs, rows, metadata, field values. 600 = control weight.
- JetBrains Mono — kickers, eyebrows, evidence lines, codes, timestamps. Always uppercase + tracked.

**Type scale (px):** 9 (micro/kickers) · 11 (caption) · 12 (meta) · 14 (body) · 15.5 (row title) · 17 (lede) · 20 (title) · 24 (display) · 30 (hero). No sizes off this scale in product UI.

**Paper ramp (warm neutrals, no pure white anywhere):**
- `#EFEAE0` — canonical page/screen background
- `#F7F2E7` — card
- `#FBF7EC` — raised/lifted surface (also the light "ink" on dark surfaces)
- `#F3EEE3` — soft mat
- `#E8E2D4` — sunken / board backdrop
- `#E1D9C8` — deepest backdrop

**Ink ramp (warm near-black → warm grey):**
- `#1B1714` — primary text
- `#2C2622` — soft primary
- `#3C352E` — secondary body
- `#6E6862` — muted text. THIS IS THE FLOOR: the lightest color that may carry text.
- `#B5AFA5` — decorative only, never text.

**Gold accent (Vesper's voice):**
- `#B0853A` — only as LARGE or BOLD text on raised surfaces, or as fills/CTAs
- `#8A6628` — gold TEXT on paper mats (small labels, eyebrows)
- `#D9BD86` — fills and edges only

**Status trio (always rendered as tinted bg + same-hue text, never saturated fill + white text):**
- OK/resolved/live: sage `#2E5A3A` on tint `#EFF5EF`, border `rgba(46,90,58,0.25)`
- Warning/broken/correction: oxblood `#7A2E2E` on tint `#FBF0F0`, border `rgba(122,46,46,0.25)`
- Navigation/open/facet: ink-blue `#2A5A8A` on tint `#EDF2F8`, border `rgba(42,90,138,0.25)`

**Hairlines:** `rgba(27,23,20,0.06 / 0.09 / 0.10 / 0.14)`, drawn at 0.5px. Cards sit on hairline "seats," not drop shadows; real shadows are reserved for sheets and keepsake objects.

**Radii:** 8 (small) · 12 (medium) · 20 (large/sheets) · 999 (pills). No 4px or 6px tiers.

**Canonical micro-tag recipe ("VTag" — use for all evidence/status chips):** height 18, radius 9, padding 0 7px, JetBrains Mono 8px weight 700, letter-spacing +0.4, tinted bg + same-hue text per the status trio.

**Mono label conventions:** labels 8.5–9px / weight 700 / letter-spacing ~1.4–2px equivalent, uppercase. Three tracking steps only: labels ~1.4, kickers ~2, wide display ~.18em.

## Step 0 — Confirm six rulings (recommendations inline)

- **R1 Paper:** replace the `#F4EFE5` paper fork with the canon ramp. Screens → `#EFEAE0`, raised cards → `#FBF7EC`, mats → `#F3EEE3`. ACCEPT.
- **R2 Night:** KEEP the dark material doctrine ("dark thinks, cream serves" — Ruling 18). `#15110D` becomes an official Atlas-scoped token `night` (with `nightDeep #0E0B08` and the map-field darks). One change: dark text on gold CTAs becomes ink `#1B1714` instead of `#15110D`.
- **R3 Status:** status semantics move to the canon trio above. The natural palette — rust `#A85F43`, teal `#435C68`, moss `#64734D` — is KEPT but strictly for photo-plate gradients, map pins, and year bars (art), never for chrome, status text, or chip backgrounds.
- **R4 Microtype/radius:** the Vesper scale wins. Evidence chips adopt the VTag recipe above (replacing the 10px/4px-radius chips of board Rulings 05/13). Type sizes snap to the canon scale (mapping in Step 1.6).
- **R5 Compose chips:** the solid rust/teal facet chips in the compose flow restyle as dark-surface chips: `night` bg, `#FBF7EC` text, 0.5px light hairline `rgba(251,247,236,0.25)`. No solid art-color fills.
- **R6 Mode rail:** the 2px gold underline active state on the Read/Time/Places/Reel rail is KEPT as an Atlas dark-surface idiom — document it in the component section.

## Step 1 — Canonical Experience Board fixes

1. **Rewrite the Design-tokens panel** (bottom of the board, near the rulings log — it still declares "Newsreader" and "Hanken Grotesk", contradicting Ruling 01 and the board's own rendering). Replace its contents with:
   - type.display: EB Garamond 500 (600 editorial roman only)
   - type.ui: DM Sans 400–700
   - type.evidence: JetBrains Mono 700, uppercase, tracked
   - ink: #1B1714 / #2C2622 / #3C352E / #6E6862 (text floor) / #B5AFA5 (decorative only)
   - paper: #EFEAE0 page / #F7F2E7 card / #FBF7EC raised / #F3EEE3 mat / #E8E2D4 sunken
   - accent: #B0853A (large/bold on raised only) / #8A6628 (text on mats) / #D9BD86 (fills)
   - night: #15110D (Atlas liminal surfaces — dark thinks, cream serves)
   - status: sage #2E5A3A · oxblood #7A2E2E · ink-blue #2A5A8A (+ tint bgs)
   - art palette (plates/pins/year-bars only, never chrome): rust #A85F43 · teal #435C68 · moss #64734D
2. **Global paper swap:** every `#F4EFE5` background (phone screens, fallback-grid mats) → per R1. Every use of `#F4EFE5`/`rgba(244,239,229,…)` as light text or hairlines on dark surfaces → `#FBF7EC`/`rgba(251,247,236,…)`. Every `#F7F3EA` (light text over photo plates) → `#FBF7EC`. The Time-mode gradient background (`#F6F1E7→#F1EBD8`) → flat `#EFEAE0` (gradient paper isn't a canon concept). Every `#FFF`/white background (active nav pill, preview cards, stat cells) → `#FBF7EC`.
3. **Gold text-safety sweep:** every small mono eyebrow/label currently `#B0853A` sitting on cream paper → `#8A6628`. Gold on dark surfaces, and large/bold gold on raised surfaces, stay `#B0853A`.
4. **Status recolor:** "● live" / "confirmed" / positive evidence chips: moss → sage + `#EFF5EF` tint. "thin" / "you corrected this" / "Never say" / the ❌ doctrine lines: rust → oxblood + `#FBF0F0` tint. Facet/nav chips: teal → ink-blue + `#EDF2F8` (or hairline treatment). Do NOT touch gradient photo plates, map pins, year bars, or polaroid fills — that's the art palette.
5. **Ink ramp → semantic inks:** text drawn as ink-opacity `rgba(27,23,20,.7–.78)` → `#2C2622` or `#3C352E`; `.4–.55` → `#6E6862`; anything lighter than `.4` may not carry text — promote it to `#6E6862` or demote the element to decorative.
6. **Type & radius snap:** 10 → 9 (labels) or 11 (evidence lines needing legibility); 10.5 → 11; 12.5/13 → 12; 13.5 → 14; 15 → 15.5; 16/18 → 17; 22 → 20 or 24; 26/27 → 24; 32/34 → 30. Chips adopt the VTag recipe (h18/r9/mono 8/700/ls +0.4). Radius 4px and 6px → 8px everywhere except within the VTag recipe (r9). Letter-spacing consolidates to the three canon steps. (Board masthead/annotation chrome is exempt — presentation, not product.)
7. **Micro-fixes:** de-italicize the italic *user* quote in the Implementation States screens (italic = Vesper's voice only; user words are roman). Add a new dated entry to the rulings log: "Ruling 19 (2026-07-09) — Polish 4: paper, status colors, microtype, radii reconciled to Vesper app canon; night + art palette canonized as Atlas-scoped tokens."

## Step 2 — Implementation Spec v6 → v7

- **Rewrite §14 "Design system tokens"** to exactly match the Step 1.1 token block. Today it still prescribes `ink #17130F`, `gold #B88A35`, `paper #F4EFE5`, `Newsreader`, `Hanken Grotesk` — an engineer following it would ship the pre-Polish-1 system. This block is the single most important change of the session.
- Keep §1–§13 and §15 content untouched (data contracts, Memory Truth Rules, scoring model, state flow, P0 slice, fallback states are current and load-bearing).
- If not restyling the document's own chrome, add a banner: "Chrome pre-dates Polish 1 — the §14 tokens are normative; the styling of this document is not."

## Step 3 — Legacy boards

- **Atlas Vision Board:** add a banner "SUPERSEDED (2026-07-09) — historical. Decided frames redrawn in the Canonical Experience Board; retained only for the HV/TL/MV/RV variation rationale." Don't restyle it.
- **AtlasComposite:** delete it (its content exists as the canon board's Arrangement Modes section + Implementation States 07–10), or give it the same superseded banner.

## Definition of done (checkable on the export)

Zero occurrences anywhere (including token panels): `Hanken Grotesk`, `Newsreader`, `#F4EFE5`, `#F7F3EA`, `#17130F`, `#B88A35`, white `#FFF` backgrounds. No `#A85F43`/`#64734D`/`#435C68` outside gradient plates/pins/year-bars. No text lighter than `#6E6862` on paper. Implementation Spec §14 identical to the canon board's token panel.
