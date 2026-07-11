# Atlas Design Canon — Polish Session 1: Sleeker, Simpler, On-Brand (2026-07-05)

Scope: five items, all polish/simplification of the EXISTING canon — no new features, no scope growth. This session is informed by a July 2026 competitive research pass (Apple Photos/Memory Movies/Journal, Google Ask Photos + Recap, Spotify Wrapped 2025 + Listening Archive, Strava, Polarsteps, Retro/Lapse/Locket, daylist). The doctrine of this file is validated by that research — evidence-first phrasing, honest thin states, living views, private-first all match what won in 2025-26. This session fixes execution-level friction, not thesis.

Working set: `Atlas - Canonical Experience Board.dc.html` (primary), `Atlas Vision Board.dc.html`, `Atlas Implementation Spec.dc.html` (v6), `AtlasComposite.dc.html`.

Governance rule for this session: this file has canon badges and the §13 Final Canon Summary but no consolidation layer. For EVERY ruling below, add a dated entry to §13 (or a small new "Rulings" block beside it) — decision, date, one-line rationale — and update the Implementation Spec where contracts change. Do not leave superseded explorations un-badged: demote them visibly (archived · do-not-implement).

---

## 1. Typeface & token reconciliation — the one big ruling

Current state: this bundle uses Newsreader (display) + Hanken Grotesk (UI), ink `#17130F`, gold `#B88A35`, paper `#F4EFE5`. The Vesper app canon — which every other surface uses and which the codebase CI ratchets enforce — is EB Garamond (serif/expressive) + DM Sans (UI/productive) + JetBrains Mono (labels/evidence), ink `#1B1714`, gold `#B0853A`, with an established paper family.

**Ruling to apply: adopt the app canon.** Atlas is a tab inside Vesper, not a separate product; two serif families a swipe apart read as inconsistency, not sub-brand, and off-canon tokens are permanently expensive against the code ratchets. Atlas's distinctiveness lives in what is genuinely unique to it — the woven plates, the memory spine, the provenance glyphs (○ first · ◑ returned · ● kept · ◎ now), the mono evidence line — not in typefaces.

Do:
- Swap the token block once: EB Garamond replaces Newsreader (display + any italic Vesper-voice lines), DM Sans replaces Hanken Grotesk (UI/chrome/buttons), JetBrains Mono stays (evidence/eyebrows only). Ink → `#1B1714`, gold → `#B0853A`, deep gold → `#8A6628`; keep the rust/teal/moss memory-plate hues (they are Atlas-specific and fine).
- Re-render the two canonical screens that sell the system — Home (default state A) and the opened Reading (Read mode) — so the reconciled type is proven on the flagship, not just declared.
- Record the ruling in §13. Keep italic discipline per app canon: italic serif = Vesper's voice only, never captions or labels.

## 2. Home hero simplification

Current friction (Canonical board §2, screen A): six typographic registers stacked above the fold, and two near-equal CTAs ("Open this reading →" + "Keep"). Research note: every 2025-26 winner reduced chrome around the artifact (Wrapped 2025, iOS 26 Photos keeping photos focal).

Do:
- **One CTA on the hero: "Open this reading →".** Keep moves INSIDE the opened reading (you keep a reading after reading it, not from its cover). Update the Impl Spec P0 component list and the Keep state-machine entry accordingly.
- **Merge the eyebrow and evidence line into one mono line** — "ATLAS NOTICES · 14 SHORES · 5 CITIES · SINCE 2023" — one register instead of two.
- **Add a one-line selection-provenance note** under the hero (quiet mono): e.g. "3 new moments since May · surfaced today." Rationale: research shows unexplained AI selection reads as random (Google Recap); explained selection reads as intentional (Spotify Listening Archive's "remarkable days").
- **One-cell caption rule:** Vesper's caption inside the mosaic never fragments across grid cells. The current "polished" variant splits one sentence across two tiles ("Rivers, harbours, the cold Atlantic —" / "you book the room with a view…") — fix that instance and record the rule: the voice occupies exactly one cell, sized to fit, or moves below the mosaic.

## 3. Compose flow: material continuity + retrieval trust

Current friction (§3): cream home → near-black "archive awake" input sheet → back to cream for the heard-chips screen → composition. The dark moment is good drama; the mid-flow round trip is jarring. And the heard screen is the single most load-bearing trust surface in the product — the research verdict on Google Ask Photos (users fled; Google shipped an escape toggle in 2026) is that NL-over-a-closed-corpus fails silently unless the user can SEE and CORRECT what was matched.

Do:
- **The dark sheet owns the whole ask:** compose.input AND compose.heard both render on the dark sheet (chips restyled for dark). Cream returns only at `compose.ready` — the reading arriving IS the return to daylight. Update the state-machine section of the Impl Spec (§7) to note the material assignment per state.
- **Heard screen gains a matched-evidence line:** under the chips, one mono line — "41 moments · 6 places · 2 years match" — live-updating as chips are edited. This makes retrieval errors correctable BEFORE composition. Add `matchedCounts` to the heard-state data contract note.
- **Consent sentence in the aperture** (one quiet line at the sheet's foot, permanent): "Nothing is analyzed until you ask. Nothing leaves Atlas unless you share it." (Day One's opt-in posture, stated as plainly as they state it.)

## 4. Ways Back In: resolve to ONE canonical layout

Current state: four competing explorations (A editorial list — tagged recommended · B magazine grid · C swipeable deck · D almanac index). Unresolved explorations are how implementation drift happens.

**Ruling to apply: A (editorial list) is canonical for the full "Views you keep" screen.** It carries the two things that make kept views living — evidence counts and freshness state (● live / ↑ updated / active / thin / archived) — at higher density than B or C, and it matches the app's Row System sensibility. The small-plate horizontal strip remains the HOME form (unchanged). Demote B, C, D to archived explorations with do-not-implement badges. Note in §13: the deck (C) may return post-dogfood as a browse *mode*, not the default.

Also: give the 5-state freshness model one compact legend row on the canonical screen so the glyph vocabulary is self-documenting.

## 5. Material + microtype doctrine board

Three inconsistencies to close with one small rules board:

- **One material language.** Flat woven plates are the Atlas default everywhere. The polaroid-stack-with-drop-shadow treatment currently on the timeline is RESERVED as the Time-mode signature only (it earns its tactility there — Wrapped-2025-style analog warmth) and never appears on home, readings, or kept views. Record as a two-line rule with one do/don't pair.
- **Mono microtype floor.** The 8–9px mono labels are below comfortable device legibility. Set the floor: no mono label below the equivalent of 10px at 393pt width; evidence lines 10–11px; eyebrows may compensate with letterspacing, not size. Adjust the canonical Home + Reading renders to comply (this pairs with item 1's re-render — one pass).
- **Chrome references, not redraws.** The bottom glass nav drawn in this file should be a REFERENCE to the Vesper Global Chrome canon (the floating pill with collapse behavior), not an independently drawn nav. Replace the drawn nav on canonical screens with the canon pill and add a pointer note. Same for any sheet chrome: reference Interaction Surfaces.

---

## Explicitly OUT of this session (do not start)

- The DNA-vs-evidence-doctrine adjudication, /your-map and /dna-card coverage, and the 36-route ownership table — those are the separate "Atlas Consolidation & Ownership" session.
- Any new arrangement mode, sharing surface, or gimmick (no spatial/parallax effects — research verdict: delightful once, ignored after).
- Vocabulary renames in code (board→reading) — code-side decision, tracked separately.

## Definition of done

Tokens/typefaces reconciled + flagship screens re-rendered · hero has one CTA + merged evidence line + provenance line + one-cell caption rule · compose flow is dark-until-ready with matched-evidence counts + consent line · Ways Back In has exactly one canonical layout with a freshness legend · material/microtype/chrome rules board exists · every ruling dated in §13 · export a fresh handoff.
