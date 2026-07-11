# Atlas Design Canon — Polish Session 3: Visual Consistency Sweep (2026-07-05)

Scope: five items, all pure visual craft — token/scale consistency, no structural or copy changes. Found by grepping the actual markup for radius/padding/color/glyph values across the whole Canonical Experience Board, not by eyeballing screenshots. Nothing here touches typefaces, the home hero, the compose flow, Timeline's material (all settled in Polish 1/2), or Moment Actions.

Working set: `Atlas - Canonical Experience Board.dc.html`.

Governance: log each fix as one line in the §13 Rulings Log ("Polish 3, visual sweep — no doctrine change").

---

## 1. Fix the provenance glyph mismatch

The four evidence-provenance states are ○ first · ◑ returned · ● kept · ◎ now. In the current markup, "first" renders as a small bullet character (`◦`, noticeably smaller/lighter than its siblings) while returned/kept/now render as full-weight circles. Since Polish 2 anchored these glyphs to the timeline rail at a deliberately readable size, the mismatch is now the most visible inconsistency in the memory spine.

Do: replace every instance of the small "first" bullet with a circle glyph at the SAME visual weight/size as ◑●◎ (open/unfilled ring rather than filled, to preserve the semantic distinction between "first" and "kept," but matched in stroke weight and diameter). Audit every place this glyph appears — timeline beats, any reference/legend boards, the Places/Map arrangement if item 2 below adopts it — and fix all instances in one pass, not just the timeline.

## 2. Unify the evidence-state visual language across all four arrangements

Currently, Time mode uses the ○◑●◎ glyph system; the Places (map) arrangement uses an entirely different encoding — colored gradient city nodes with a ring highlight reserved for "now." These are the same four states describing the same moments, rendered two incompatible ways depending on which arrangement you're in.

Do: apply the same ○◑●◎ vocabulary to map nodes — e.g., the node's outer ring or a small badge on each city marker uses the matching glyph, so a user moving between Time and Places recognizes "this is the same kind of moment" at a glance. Keep the city-color coding (it encodes place, not evidence-state — that's a different, legitimate dimension) but layer the provenance glyph on top rather than replacing it with an unrelated ring/highlight convention. Apply the same check to Read and Reel if either currently shows provenance through some other means — one glyph vocabulary, four arrangements.

## 3. Collapse the card/plate radius scale

Current state: 14 distinct small-radius values in active use (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16px), excluding pills (999px) and avatar/node circles (44/54px) which are fine as-is.

Do: define a 3-tier radius scale and re-map every element to it:
- **Tight (≈3-4px)** — small chips, tags, inline badges, evidence-source labels
- **Standard (≈8px)** — cards, plates, sheets, buttons, most containers
- **Soft (≈12px)** — larger enclosing surfaces (full sheet corners, hero card containers)

Go through the file and snap every off-scale value (1,2,5,6,7,9,10,11,14,16) to the nearest tier. If the app's own token system already defines a radius scale (check `design-system.jsx` from the main Vesper file, since Polish 1 already adopted that file's typefaces/colors), use ITS scale instead of inventing a new one — consistency with the app matters more than the specific numbers chosen here.

## 4. Collapse chip padding to two defined sizes

Current state: ~10 distinct padding combinations across chip-shaped elements (facet chips, tags, mini-badges, filter pills), with no evident compact/standard distinction.

Do: define exactly two chip sizes and re-map every chip to one of them:
- **Compact** — small inline tags, evidence-source badges, glyph+label combos (e.g. "RECEIPT CONFIRMED")
- **Standard** — interactive chips a user taps/removes (facet chips in compose, filter chips, "Is this right?" affordance)

Every chip in the file should visibly belong to one of these two sizes — no in-between values.

## 5. Standardize the primary CTA button shape

Current state: the black primary-action button (Compose/Keep/Open/Recompose) renders as a full pill (999px radius) in some places and a near-square button (3px radius) in others; supporting cream-background card containers cycle through 8/9/10/12px with no evident logic (this overlaps with item 3's scale — apply it here specifically to buttons since they're the most-clicked, most-visible element).

Do: pick ONE shape for the primary CTA button (recommend the "Standard" tier from item 3, ≈8px — matches the app's productive-register button convention rather than a pill, which reads as more casual/social than Atlas's editorial register) and apply it to every primary action button in the file: Compose this view, Open this reading, Keep, Recompose, Steer.

---

## Definition of done

Glyph weights matched across all instances · Places/Map nodes carry the same provenance vocabulary as Time mode · radius scale collapsed to 3 defined tiers with every element re-mapped · chip padding collapsed to 2 defined sizes · primary CTA button shape unified everywhere · each fix logged in §13 · export a fresh handoff.
