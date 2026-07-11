# Vesper Design Canon — Session C1: Contrast & Truth (2026-07-06)

Scope: the two fresh-eyes findings that reach USERS (not just implementers): systemic WCAG contrast failures, and substrate fictions. Five items, all with exact targets. Ledger rows as items land.

---

## 1. Fix the contrast failures at the token level

Measured (WCAG relative luminance): every mute-tier token fails AA 4.5:1 at the caption/body-secondary sizes where it's used; muteSoft fails even the 3:1 large-text floor; gold-on-mat fails outright.
- In design-system.jsx AND each live fork's palette const: darken the mute tier to ≥4.5:1 on its own paper — target ≈ #6E6862 for mute-on-#EFEAE0 (verify per fork's actual paper; keep the warm hue, drop lightness).
- muteSoft (#B5AFA5 family, ~1.9–2.1:1): record the rule "muteSoft is decorative-only — never carries text"; where it currently colors text, step up to the fixed mute.
- Gold #B0853A on mats (2.80:1): rule "gold text only at large/bold sizes on cardWarm; on mats use goldDeep #8A6628"; goldDeep-on-bg (4.37) passes large-text only — same restriction.
- Record all three rules in a short "Contrast floor" note under Platform Stances. The dark register passes everywhere — untouched.

## 2. Fix the gold/goldDeep semantic inversion

trip-document-canon.jsx (DT) and trust-kit.jsx (TC) define gold=#8A6628 / goldDeep=#A9863F — inverted vs canon (gold=#B0853A, goldDeep=#8A6628); TC also forks ink (#211B15). Swap the values to canon semantics (visual output should barely change since both hues stay in the family; where it visibly shifts, canon wins). One landmine defused: two same-week boards currently render "gold" as different hues.

## 3. Substrate wording fixes (all verified against the backend — exact lines)

- vesper-state-system-app.jsx ~209: "Checking Oct 12–17 weather patterns" → truthful loading line ("Reading your saved places · Drafting day 1") — no forecast substrate exists.
- trips-home-canon-screens.jsx ~206: drop "and the week's weather" from the interstitial.
- notifications-app.jsx ~367: "based on your Alfama walk last June" → "based on the places you saved in Alfama last June" (no GPS history; saves/affinity are the real source).
- deck-readiness-taxonomy.jsx ~22: drop "no packing list, no boarding pass saved" — contradicts Imminent Hero States' own "Never" list (which wins).
- booking-screens-1.jsx ~67: "counter seats you liked" → venue-level preference wording.
- Add one sourcing rule to Discover Detail + Universal Search impl notes: "walk-minutes render only when computed by the distance resolver with a real anchor; LLM-authored distances are forbidden in dossier prose."

## 4. Re-spec the Flight deck card (the canon's one true fiction)

vesper-home-voicecard.jsx VCFlight + vesper-home-deck.jsx DeckFlight claim delay DETECTION ("slipped to 9:40 · I already looked") + rebook price deltas. No substrate: Duffel is search/offers/holds only; no schedule-change webhooks, no flight monitoring, no member↔flight linkage. Re-spec BOTH artboards to the substrate-true version: the card triggers on USER-REPORTED change ("My flight moved") or a booking-record update — Vesper responds with held-options framing, no "I already looked" claim, no live delta. Record the ambitious version as a BUILD requirement row (schedule-change webhooks; gated with G2–G4 booking work) so the intent isn't lost.

## 5. Migrate the 8 remaining 390px frames to 393

booking-kit, vesper-external-sharing-app, vesper-guide-reader-app, vesper-photo-intake-app, vesper-proposal-detail-app, vesper-saved-collections-app, vesper-trip-settings-app, vesper-discover-map-app (the newest surface is on the wrong width — the fork is still propagating). Mechanical find-replace width={390}→width={393} on phone frames only (not mock widths like 340/350); console-check each page.

## Definition of done

All mute text ≥4.5:1 on its paper · muteSoft text-free · gold rules recorded · inversion fixed · six wording fixes in · Flight card substrate-true + BUILD row · zero 390 phone frames · export.
