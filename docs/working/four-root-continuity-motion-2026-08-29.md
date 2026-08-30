---
doc_type: working
status: active
owner: founder / design / frontend
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: The 2026-08-29 four-root design boards (Home recovery, Places four-state) make temporal claims — scope that narrows, dominance that moves on a stable skeleton, one encounter across four screens — that the ratified motion language does not yet govern; this proposes the continuity vocabulary that closes that gap without re-legislating interaction motion.
promotes_to: docs/systems/motion-language.md
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/systems/motion-language.md
  - docs/working/places-four-state-design-fixture-brief-2026-08-29.md
  - docs/working/home-surfaces-pre-pivot-recovery-and-post-pivot-direction-2026-08-27.md
  - docs/working/design-kernel-extraction-2026-08-29.md
---

# Four-Root Continuity Motion

## Decision (proposed)

Extend the ratified Motion Language with a **continuity register**: four new
canonical patterns (numbered 9–12, continuing the existing eight) that govern
how identity persists *across* screens and how emphasis moves *within* a
stable page. Nothing here amends the existing patterns, timing tokens, easing
contract, ceremony scarcity, or Reduced Motion rules — those remain owned by
`docs/systems/motion-language.md`, and this document proposes new entries for
that contract, not a parallel doctrine.

**No new durations, curves, or springs are proposed.** Every pattern below
composes from the existing token scale (`duration.instant/fast/base/slow/
promote/demote`, house ease). That is deliberate: the continuity register
should pass the existing motion-governance ratchet unchanged.

## 1. The gap, precisely

The existing vocabulary governs interactions — press, reveal, sheets, lift,
deck, state settle, ceremony. Three claims made by the 08-29 boards fall
outside it:

1. **Scope narrows across screens.** The Places four-state brief (§3)
   requires that "the same scope, focal Place, map position, Sources,
   selection, and return path must visibly persist" from World Field →
   Place Focus → Place Path → Live Reduction. `Workspace Transition`
   (pattern 5) covers entering a separate destination; it does not cover a
   destination that is *the same world, closer*.
2. **Dominance moves on a stable skeleton.** The Home recovery anatomy
   (recovery doc §6.3) keeps five regions in one learnable order while
   posture changes which region dominates. `State Settle` (pattern 6)
   governs one object changing state; nothing governs a *page re-weighting
   its regions* without reflowing its skeleton.
3. **The same object projects across roots.** An Occasion appears on Home as
   attention, in Places as spatial context, in Life as history (recovery doc
   §6.6). No pattern says what motion, if any, connects those projections.

## 2. Continuity laws (extending the brand stance)

L1. **Continuity is proven by what does not move.** A transition between
    states of one encounter is legible because its anchors — scope handle,
    map geometry, selected object, interval — hold or interpolate while
    everything else yields. If no anchor persists, it is a Workspace
    Transition, not continuity.

L2. **One anchor family moves per transition.** The map may interpolate, or
    the dominant unit may travel — never both. Everything non-anchored exits
    at `instant` and re-enters as Soft Reveal.

L3. **Urgency changes register, never adds motion.** ACT NOW arrives as a
    state change (oxblood StatusMeta, compressed content, promoted
    consequence rule) with the same physics as HOLD. No pulse, shake,
    flash, or accelerated loop. (Extends "'Now' is stable.")

L4. **Postures change between glances, not during them.** Home recomposes
    its dominance on entry, return, or an explicit user act — never
    spontaneously while the person is looking at it. A live instrument
    updates its values; a page does not rearrange itself under the reader.

L5. **Cross-root projections make no motion claim.** Switching roots is an
    instant tab change; the same Occasion appearing differently on Home,
    Places, and Life is connected by identity anatomy and naming, not by
    animation. Do not build shared-element transitions across the tab bar.

## 3. Proposed canonical vocabulary (patterns 9–12)

### 9. Scope Narrowing (reverse: Widening)

One world, seen closer. World Field → Place Focus; Place Focus → Place Path.

- Anchors: the scope handle (text crossfades `NEW YORK` → `RED HOOK` over
  `fast`; letters never slide), the map geometry (viewport interpolates
  city → peninsula over `slow`, house ease; the tapped pin/expression is the
  pivot and never leaves the screen), and the selection mark.
- Non-anchored content: exits `instant`, arrives Soft Reveal with the
  standard `stagger`.
- Widening (back) restores the exact origin scroll position; the followed
  branch carries a quiet followed-mark (a state, not an animation).
- Reduced Motion: viewport jumps; scope handle and content crossfade only.

### 10. Dominance Shift (promote / recede)

The page re-weights; the skeleton holds. Home posture changes; ACT NOW
promoting the consequence rule above the crown.

- The gaining region steps up containment/elevation in place over
  `duration.promote` (320); the yielding region steps down over
  `duration.demote` (260) — reusing the existing token pair as the generic
  dominance vocabulary, not just the carousel's.
- Recede never removes: a region losing dominance drops to a quieter
  register and stays (the temporal form of "quiet is a posture, not a
  content count").
- At most one promote and one recede per recomposition; other regions
  change treatment instantly.
- Reduced Motion: instant register change, order preserved.

### 11. Medium Switch

Same state, alternate medium — map ↔ composition on any Places state
(fixture brief §3.3 row 5).

- Pinned: selection, scope, viewport center, filters, path, scroll anchor.
- The two media crossfade over `base`; no slide, no push — this is not
  navigation and must not feel like it.
- The switch control itself uses Press; the switch never re-ranks or
  re-fetches content.
- Reduced Motion: same, already opacity-only.

### 12. Instrument Hold

A live instrument stays still while its truth updates — Live Reduction,
countdowns, freshness lines.

- Values update in place with zero layout shift; a changed value announces
  itself with a brief ink or gold emphasis fade over `fast`, never with
  movement.
- Posture transitions inside the instrument (HOLD → ACT NOW) compose from
  State Settle (the StatusMeta line) plus at most one Dominance Shift (the
  consequence rule) — see L3.
- The instrument's map and sequence are one Medium pair: a route change
  updates both in one State Settle, never sequentially.
- Reduced Motion: emphasis fade only, which is already the pattern.

## 4. Transition map for the shipped boards

| From → To | Pattern | Anchors held |
| --- | --- | --- |
| World Field → Place Focus | Scope Narrowing | scope handle, map (city→peninsula), selection |
| Place Focus → Place Path | Scope Narrowing (shallow: handle gains `· ACCESS`; map yields to diagram via Medium-style crossfade) | handle, focal Place, interval |
| Place Path → Live Reduction | Dominance Shift (the consequence door promotes into the instrument) + provenance label | interval, dinner constraint, route |
| Home crown → Live Reduction | Workspace Transition (existing pattern 5) with the provenance label as origin receipt | proposition, interval |
| Any Places state, map ↔ composition | Medium Switch | selection, viewport, scroll |
| Home posture change (between glances) | Dominance Shift | all five regions' order |
| Root ↔ root | none (L5) | — |
| Back, anywhere | Widening / platform back | origin scroll, followed-marks |

## 5. What this does not authorize

- No navigation-motion adapter or instrumentation layer (the contract's
  existing restraint stands until an implementation is justified).
- No shared-element library adoption; patterns 9–12 are contracts for
  whoever implements the four-root shell, not a build order.
- No change to the motion-governance registry; implementations adopt
  existing tokens and file-registry review.

## 6. Open questions (founder)

1. **Map interpolation vs crossfade.** Scope Narrowing assumes the map
   viewport can interpolate city → peninsula. With Mapbox that is a camera
   move; with illustrated/diagram geometry it may have to be a crossfade
   with a pinned pivot. Rule which fidelity the contract requires, or allow
   both with the pivot law as the invariant.
2. **Does Widening animate?** Back could reverse the narrowing (symmetric,
   calm, slower) or simply cut with scroll restored (the existing "exits
   are quick" bias). Proposed default: cut; reserve reverse interpolation
   for the map-led transitions only.
3. **First-open of Home.** Does the dominant region promote on cold open
   (a deliberate 320ms arrival) or arrive settled? Proposed: arrive settled;
   promotion is for *changes*, not introductions.

## 7. Acceptance additions

To the contract's five acceptance questions, continuity surfaces add two:

6. Which anchors persist through this transition, and does anything
   non-anchored move? (L1/L2)
7. Can the person tell they are in the same encounter after the transition
   without re-reading the header? If not, the anchors are wrong.
