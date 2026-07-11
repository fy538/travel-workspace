# Claude Design Adjudication Brief — VesperSignature vs. D8 (2026-07-11)

**For:** the human, working in Claude Design (claude.ai/design), canon project `Vesper` @ handoff 134.
**Source:** the zero-trust re-audit campaign's Wave 1 "Voice registers (family)" audit, which found this while re-checking a prior "fully ALIGNED, no known code gaps" verdict — spot-verified directly against both files before writing this brief, not inferred.

**How to use this:** one decision, two shipped realities that contradict each other. Either code changes (a real, ~30-site visual migration) or canon changes (a scoped carve-out, matching the precedent already set by D22's onboarding exception). Don't split the difference — pick one, and if you pick canon-changes, regenerate the specimen in the same session so this doesn't drift again.

---

## D23 — `VesperSignature`'s "+" glyph directly contradicts D8's "never a bare +" rule

**Conflict:** canon's D8 ruling (`vesper-shared.jsx:14-21`) is unambiguous:

> "This two-point spark is the single Vesper mark... A bare '+' or arrow is NOT the brand mark — those are functional compose/add icons and mean something else. **When a surface needs 'Vesper is speaking,' use VesperMark.**"

Code's `components/brand/VesperSignature.tsx` opens with:

```
/**
 * VesperSignature — the canonical visual mark for "Vesper is speaking".
 * ...
 * Use this instead of hand-rolling plus/sparkle/fleuron + Vesper labels.
 */
```

— then renders (`VesperSignature.tsx:89`):

```tsx
<Text style={[styles.plus, ...]}>+</Text>
```

Same job description as canon's own definition of "Vesper is speaking," opposite glyph. `VesperSignature` never imports or touches `VesperMark`. Two components downstream — `VesperAttribution` and `VesperNote` — both wrap `VesperSignature` unchanged, so the "+" is what actually ships everywhere those are used: roughly 30 real consumers spanning chat (message bubbles, recommendation blocks, typing indicator, private notes), Discover/dossier editorial attribution, Places take/spot content, and group-thread privacy notes.

**This isn't drift from neglect.** `VesperSignature` is a maintained, documented primitive with real design investment — four color tones (`gold`/`discover`/`onDark`/`muted`), two scales (`eyebrow` caps / `byline` natural-case editorial), optional suffix/timestamp/rule. Someone built this carefully. It just was never reconciled against D8, or was built on a reading of "Vesper is speaking" that predates D8's ruling.

**What canon *does* sanction a "+" for, narrowly:** `VesperVoiceLine` (`Vesper Productive Type & Material.html:466`) — a gold "+" plus a short line, but scoped tightly to Stay/Costs empty/invite/settled states. That footprint doesn't overlap with `VesperSignature`'s actual usage at all — different surfaces, different job.

**Decide:** one of two directions —

1. **Code owes canon.** `VesperSignature` migrates its "+" to the `VesperMark` spark (matching D8 literally), across all ~30 consumers. This is the bigger lift — needs a real visual pass, not a find-replace, since `VesperMark`'s SVG proportions differ from a text glyph and the component's tone/scale system would need to carry through correctly.
2. **Canon owes code.** `VesperSignature`'s "+" gets an explicit, scoped D8 carve-out — the same shape as D22's onboarding exception — reasoning that a *signature/byline* mark (small, inline, paired with a label) is a different semantic category than the sparkle `VesperMark` (a standalone attention glyph), and the "+" has been the de facto shipped signature mark long enough that it may already be what "Vesper is speaking" reads as to users. If this is the call, canon should name `VesperSignature`'s "+" explicitly in the D8 ruling text, the same way D22 named onboarding's decorative Fleurons, so a future audit doesn't re-flag it as unresolved drift.

**Regenerate:** if ruling (1), add `VesperSignature`'s "+" to `vesper-shared.jsx`'s D8 comment block as a confirmed violation needing conversion (no canon change, code follow-up only). If ruling (2), add a carve-out paragraph to the same comment block naming `VesperSignature` explicitly, the way the existing "ONBOARDING CARVE-OUT (D22, canon 130)" paragraph does — so the exception is documented at its source, not just in this brief.

---

## Smaller, related — no design decision needed, just cite for completeness

These are execution gaps in D8's *already-settled* ruling (Fleuron → VesperMark for genuine attribution), found by the same audit pass. Not blocked on D23 — they can be fixed in code independent of which way D23 goes:

- `components/onboarding/DeferredDiaryGiftSheet.tsx:40-42` still renders `Fleuron` beside literal "VESPER · A SIDE NOTE" / "VESPER · ONE MORE THING" copy — but this sheet is reached from **in-trip chat** (`app/(tabs)/trips/[tripId]/chat.tsx:713`), not onboarding, so D22's onboarding carve-out doesn't apply here. This is squarely D8's territory and was simply missed.
- `components/discover/DiscoverAtoms.tsx` (`LensChip`), `components/discover/DiscoverCoverHome.tsx` ("ATLAS REMEMBERS" row), and `components/places/SpotTake.tsx` all render `Fleuron` under `colors.discover.vesper`/`vesperDeep` — explicitly Vesper-voice-coded colors, on non-onboarding surfaces.
- `components/places/PlaceHome.tsx:68-71` defines a **local function literally named `VesperMark`** that actually renders `Fleuron` — a naming collision that will produce false-positive greps in any future audit ("does Places use VesperMark?" → yes, technically, but it's the wrong mark under the right name).

**Regenerate:** none — these don't need a canon change, just a code fix batch converting the genuine attribution sites (not the PlaceHome collision, which is a rename, not a mark swap).

---

## After you re-export
Run `python3 scripts/canon-drift-check.py` — it will flag `vesper-shared.jsx` as changed if you touch it, which is the signal to re-verify the Voice registers (family) manifest row.
