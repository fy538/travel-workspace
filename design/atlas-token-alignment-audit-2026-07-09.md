# Atlas ↔ Vesper design-system alignment audit — 2026-07-09

**Compared:** `~/Downloads/vesper 125` (Vesper canon, token SSOT `vesper-tokens.jsx` VP/VS) vs `~/Downloads/atlas-memory-composition-vision 22` (Atlas canon bundle; docs still reference bundle 21 — 22 adds Cold Start Phase 2, dated 07-09).
**Companion brief (the actionable session plan):** `atlas-design-brief-2026-07-09-polish4-token-alignment.md`

> **OUTCOME (same day): Polish 4 applied → bundle 23 = new Atlas canon. DoD grep-verified.** Zero Hanken/Newsreader/`#F4EFE5`/`#F7F3EA`/`#17130F`/`#B88A35`/white bgs; canon paper ramp + status trio + gold text-safety + ink floor + 8px radii in; night `#15110D` + rust/teal/moss art palette kept Atlas-scoped (Ruling 19 on the board records all of it); Implementation Spec §14 rewritten to canon (v7); Vision Board + AtlasComposite deleted from the bundle. **Consciously deferred: the microtype/type-scale snap (10/10.5/12.5/13px etc. remain) and letter-spacing consolidation** — handle at code-alignment time by mapping to FE typography roles, not by repainting the board. §3 adjudications below are now all RESOLVED except that deferral.

## 0. Standing context — what is already decided

- **Typeface/token fork: RESOLVED 2026-07-05** (Polish 1, verified handoff 18): *adopt the app canon.* The Canonical Experience Board is now fully on EB Garamond / DM Sans / JetBrains Mono, ink `#1B1714`, gold `#B0853A` — zero Hanken Grotesk / Newsreader in its markup. **Do not re-open.** (`atlas-design-brief-2026-07-05-polish1.md` §1; Phase-2 brief locks it.)
- Ruling 01 deliberately did **not** migrate paper or the natural palette — that is the remaining fork this audit covers.
- Atlas is **out of scope for the first wedge dogfood** (scoping ruling 2026-07-06). This alignment is a *design-file* pass so the eventual code campaign has a clean target — keep it cheap; it does not gate dogfood.
- Open adjudications from `project_atlas_canon_state` that are **not** design-token questions and stay out of this pass: board→reading vocabulary in code, 36-route governance, `/your-map` ownership, `ATLAS_LLM_ENABLED` posture.

## 1. Per-board triage (the bundle has 4 boards)

| Board | State | Verdict |
|---|---|---|
| **Atlas — Canonical Experience Board** (328KB) | Fonts/ink/gold canon ✓; paper + status-color + microtype drift remain (see §2–§5) | **The live canon — fix in place** |
| **Atlas Implementation Spec v6** (94KB) | Content current (Polish-1 synced, §15 dated 07-05) but **§14 "Design system tokens" normatively prescribes legacy values** (`ink #17130F`, `gold #B88A35`, `Newsreader`, `Hanken Grotesk`, `paper #F4EFE5`) — an engineer following it ships the old system. Document chrome also legacy. | **Load-bearing — rewrite §14 to canon; keep all other content verbatim** |
| **Atlas Vision Board** (168KB) | Fully legacy tokens; every decided frame redrawn in the canon board; unique content = rejected-variant studies (HV/TL/MV/RV rationale) only | **Archive as historical; mark superseded** |
| **AtlasComposite** (29KB) | Interactive zoom-level prototype (ramen study); fully redrawn as canon §4 + Implementation States 07–10; legacy-styled | **Delete-superseded (or archive)** |

## 2. Canonical board — mechanical fixes (no adjudication needed)

| Drift | Where / count | Canon target |
|---|---|---|
| **Stale token panel** still declares `Newsreader` / `Hanken Grotesk` (contradicts Ruling 01 and the board's own rendering) | Design-tokens panel, ~L1513–1529 | Rewrite panel to canon families + values — **highest priority**, it's the board's self-documentation |
| `#F7F3EA` as on-plate light ink + polaroid borders | ×~70 | `#FBF7EC` (paper00) |
| `#F6F1E7→#F1EBD8` gradient paper (Time mode bg) | ×6 | flat `#EFEAE0` — gradient paper isn't a canon concept |
| `#FFF` backgrounds (active nav pill, preview cards, stat cells) | ×19 | `#FBF7EC` — canon has no pure white |
| Small/regular gold `#B0853A` text on paper mats (mono eyebrows everywhere) | large share of ×190 | `#8A6628` (goldDeep) — canon text-safety: gold60 only large/bold on raised |
| Ink rendered as opacity ramp `rgba(27,23,20,.2–.78)` incl. text at .22–.35 — lighter than the canon text floor | ×~400 | map .7–.78→`#2C2622`/`#3C352E`, .4–.55→`#6E6862`; **nothing below mute carries text** |
| Radius `6px` stragglers | ×2 | 8px |
| Italic on a *user* quote (Implementation States 01) | ×1 | roman — italic = Vesper's voice only |
| Letter-spacing scattered across 17 values (.02–.22em) | — | normalize to ~3 steps matching canon mono conventions |

## 3. Canonical board — adjudications (ruling vs canon, decide in session)

1. **Paper fork.** `#F4EFE5` is the board's *declared* paper token (×54 as screen bg; ×~570 as the on-dark light-ink system). The canon ramp (`#EFEAE0` page / `#F7F2E7` card / `#FBF7EC` raised / `#F3EEE3` soft) appears **zero** times. *Recommended ruling:* adopt the ramp — same logic as the typeface ruling ("Atlas is a tab inside Vesper"); page = `#EFEAE0`, raised = `#FBF7EC`, mats = `#F3EEE3`; on-dark light ink = `#FBF7EC`-based ramp. Visual delta is subtle.
2. **Night doctrine.** `#15110D` ("dark thinks, cream serves" — Ruling 18) is load-bearing doctrine, not drift: compose/map/reel/cold-start are deliberately dark, and the dark→cream transition *is* the "shape was found" signature. Vesper canon has no dark-surface tokens. *Recommended ruling:* **keep the doctrine**; canonize `night #15110D` (+ deep variants) as Atlas-scoped semantic tokens appended to `vesper-tokens.jsx`, and align dark-text-on-gold CTAs to ink00 `#1B1714`.
3. **Status colors in the art palette.** Moss `#64734D` doubles as positive-status text ("● live", "confirmed"), rust `#A85F43` as warning/correction/thin, teal `#435C68` as chip bg — a parallel status system bypassing canon oxblood/sage/ink-blue, with rust doing double duty (art + warning) that canon's separation was designed to avoid. *Recommended ruling:* **status semantics → canon trio** (sage `#2E5A3A`+tint, oxblood `#7A2E2E`+tint, ink-blue `#2A5A8A`+tint); **rust/teal/moss stay strictly as the place/photo art palette** (per Polish 1: Atlas's distinctiveness = woven plates, spine, glyphs — not chrome colors).
4. **Microtype + radius micro-canon.** Board Rulings 05 (mono floor ~10px, evidence lines 10–11px) and 13 (4px "tight chip" tier, ×127) conflict with the Vesper scale (9/11/12/…) and the canonical **VTag** recipe (h18 / r9 / mono 8 / ls +0.4). *Recommended ruling:* Vesper canon wins at the component boundary — evidence chips become VTag with Atlas tint maps; type snaps 10→9/11, 12.5/13→12, 13.5→14, 15→15.5, 16/18→17, 22→20/24, 26/27→24, 32/34→30. (Board-chrome sizes like the 80px masthead are exempt — they're presentation, not product.)
5. **Solid-colored compose chips** (`#A85F43`/`#435C68` bg + × dismiss) — an idiom foreign to Vesper (paper + hairline chips elsewhere). Decide: retokenize to hairline chips, or bless as compose-only Atlas idiom (they sit on the dark surface, so a dark-surface chip treatment may be legitimate).
6. **Mode-rail active = 2px gold underline** — not a chat/trips idiom (Vesper uses fills/pills). Low-stakes; decide keep (Atlas signature) or align.

## 4. What is genuinely Atlas and should NOT be "fixed"

- Provenance glyphs ○ first · ◑ returned · ● kept · ◎ now (gold mono) — Atlas signature, Rulings 11–12.
- Rust/teal/moss **as photo-placeholder plate art**, deterministic-by-theme ("color encodes place") — doctrine, keep.
- Woven plates, memory spine, mono evidence lines, serif-first content density.
- Dark immersive compose/map/reel surfaces (pending adjudication 2 above — keep the doctrine, tokenize the values).
- `#0B0A08` ×64 = phone-bezel mockup chrome — ignore entirely.

## 5. Cross-file notes

- Workspace docs (`code-alignment-brief-2026-07-05-atlas-long-view-2b-2c.md`, `atlas-user-journeys-2026-07-06.md`, batch-E brief) still cite bundle **21** — update refs to the post-session bundle.
- Vesper canon = handoff 108+ (mirror `design/vesper-canon-anchor/`), contains no Atlas pages; Atlas runs its own campaign (`surface-manifest.yaml` lines 364–369, freeze decision still flagged OPEN there).
- The FE already enforces canon via CI ratchets (typography roles, color budget) — every value the design file keeps off-canon will surface as ratchet friction at implementation time. Aligning the file now is cheaper than exempting code later.

## 6. Fix-effort estimate

Mechanical fixes (§2) are find-and-replace-shaped: ~1 short Claude-design session. Adjudications (§3) are six one-line decisions; recommendations above make five of them "accept recommended." Implementation Spec §14 rewrite: ~15 minutes. Archive/delete of the two legacy boards: bookkeeping.
