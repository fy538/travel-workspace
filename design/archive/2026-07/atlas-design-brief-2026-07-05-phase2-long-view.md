# Atlas Design Canon — Phase 2: Design Long View for Real (2026-07-05)

Scope: five items. This is a genuine new-screen design session, not a polish pass — Long View exists today only as a paragraph of intent in the Canonical Experience Board, with zero artboards. This session exists to unblock Phase 2c (retiring the Map shelf tile, deferred from the Phase 1 shelf retirement) by giving Long View's geography dimension something real to replace Map with — but scope the whole feature properly while you're in there, not just the piece that unblocks Map.

Working set: `Atlas - Canonical Experience Board.dc.html` (primary — add the new section here), `Atlas Implementation Spec.dc.html` (v6 — add routes/components once decided).

The doctrine, quoted in full (this is everything currently drawn on the subject — you're building from this paragraph, not replacing it):
> "Long View is the unfiltered Atlas — browse without asking. It opens the whole corpus by time, place, people, or theme, without requiring the user to compose a query first." It "lives on the home as a quiet strip ('Since 2023 · The whole Atlas →'), never as the hero." Opening it "shows a chronological atlas layout: year chapters, city nodes, memory counts. Not a search. Not the featured reading. An atlas index."

Governance: this is new canon, not a ruling on existing canon — add a new `DCSection` for Long View, log its creation in §13 the same as any other addition.

---

## 1. Reuse the composition engine — don't build a second backend concept

Before drawing anything, settle the mechanical question: Long View's "browse the whole corpus" is very close to what the composition engine already does for a Reading (compose → arrange as Read/Time/Places/Reel) — the difference is Long View has **no query** (nothing composed, nothing curated, no Vesper narrative voice) and covers **everything**, not one facet-filtered set. The efficient design direction: Long View IS the Time/Places arrangement machinery, invoked with an empty/permissive query, with the editorial narrative layer (headline, Vesper voice line, thesis sentence) stripped out — an index, not a reading. Confirm this framing works visually (does Places' node-and-count treatment read fine without a narrative headline above it?) and record it in the Implementation Spec so an implementing engineer knows this isn't a parallel system to build.

## 2. The home entry point + top-level shell

The "Since 2023 · The whole Atlas →" quiet strip is ALREADY drawn on the Home artboard (between Ways Back In and the learning signal) — do not redraw or move it. What's missing is the screen it opens into: a plain index shell — title ("The whole Atlas" or similar, in the productive/index register, not the editorial reading register), overall memory count, and a mode switcher for the dimensions in item 3. This screen should visually announce "this is a directory, not an authored piece" — flatter, calmer, less composed than a Featured Reading.

## 3. Time and Places dimensions (the two that matter most — Places unblocks Map's retirement)

- **Time (year chapters):** the app currently has two separate, overlapping time-only screens — `almanac.tsx` (a giant year-hero + Jan→Dec month rail, cardless entries) and `timeline.tsx` (a flat chronological list). Note: Almanac's own code comment cites a design precedent ("VariantAlmanac") that no longer exists anywhere in this design bundle — it's an orphaned reference from an earlier, now-inaccessible design generation, so you're not bound to preserve its current treatment. Decide and draw ONE canonical time-mode for Long View, and rule explicitly in §13 what happens to the other two screens (Almanac and Timeline) — merge one into Long View's time mode, keep one as a distinct related-but-different surface, or retire one. Don't leave three time-browsing screens standing.
- **Places (city nodes):** this is the piece that unblocks Map's retirement. Reuse the Places-arrangement visual language already established for composed readings (the node + count treatment, e.g. "TOKYO · 3") — applied here to the WHOLE corpus rather than one query's results. Draw this as a real artboard; this is the one piece of this session that's a hard prerequisite for Phase 2c.

## 4. People and Theme dimensions — scope them explicitly, even if deferred

The doctrine lists four dimensions (time, place, people, theme) but only two are urgent (Places blocks Map's retirement; Time cleans up existing overlap). Decide: does Long View ship v1 with all four as tabs in one switcher, or ship with Time+Places now and defer People+Theme? If deferring, don't draw them, but DO record the decision and note their likely future home (People probably reuses `companions.tsx`'s existing roster material; Theme probably reuses the facet vocabulary already built for compose/steer) so a future session picks up a scoped task, not a blank page.

## 5. Naming hygiene — the "whole Atlas" phrase collision

Minor but worth fixing while establishing this as real canon: the current kept-views screen (`boards.tsx` in code) uses the fallback label "Kept view · The whole Atlas" for a saved query with no facet constraints. That's a coincidental phrase collision, not a functional bug (a kept view with zero filters happens to describe itself the same way Long View is described) — but now that "The whole Atlas" is about to become a real, distinct screen's name, flag this collision in the Implementation Spec so whoever builds Long View renames that fallback label to something that doesn't imply it opens the same screen (e.g. "Kept view · No filters" or similar).

---

## Explicitly OUT of this session

- Do not touch anything about Map's shelf tile or its retirement — that's Phase 2c, a code task, and depends on this session's output existing and being built first (Phase 2b).
- Do not re-open any Phase 1/Polish 1-3 items (typefaces, home hero, compose flow, timeline material inside a Reading, Moment Actions, the visual consistency scale) — those are settled.
- Don't design People/Theme dimensions if you decide to defer them (item 4) — record the decision, don't draw the deferred item.

## Definition of done

Mechanical framing (item 1) recorded in the Implementation Spec · home entry strip + index shell drawn · Time mode decided with an explicit ruling on Almanac/Timeline's fate · Places mode drawn (city nodes over the whole corpus) — this is the hard requirement · People/Theme scope decision recorded either way · naming-collision note added · export a fresh handoff.
