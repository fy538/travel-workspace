# Vesper Design Canon — Session C2: One World + Dangling Affordances (2026-07-06)

Scope: consolidate the demo fixture world (one hero trip, one cast, consistent facts) and rule the dangling affordances found on the five core screens. Five items. Ledger rows as items land.

CANONICAL WORLD RULING (record in Canon Consolidation first, then apply):
- **Hero trip:** Lisbon · Oct 12–17 · 5 nights · party of THREE: You ("Maya R. Lin" on paperwork) + Ana + Theo. Stay vote: Casa do Mar (Cais do Sodré, €120/nt, river) beats Tejo Rooms (BAIXA). Fado = Tasca do Chico. Seafood = Ramiro.
- **Group world (party of four):** Kyoto · Jun 14–19 · You + Ana + Theo + MARA — the sanctioned setting for 4-person/group-mechanics artboards (votes 3-of-4, split-4-ways). "Maria", "Sofia", "Jonas" are retired; the fourth chair is always Mara.
- Satellites (Tokyo draft, Porto, Oaxaca dreams) stay as-is — they're explicitly other trips.

---

## 1. Apply the world ruling to the Lisbon-hero contradictions

- Party size: every Lisbon Oct 12–17 artboard says 3 travelers / "2 of 3" / "split three ways". Files where 4-person copy sits on the Lisbon story: changes-screen ("Picked the Alfama apartment… "), row-spec, trips-home group variant, vesper-home-deck ("3 of 4 in"), costs-system ("Split 4 ways · €1,480") → EITHER re-anchor those artboards to the Kyoto group world (preferred for group-mechanics boards) or re-cast to 3.
- Stay ending: Casa do Mar wins everywhere; changes-ledger's "Alfama apartment" + changes-kit's "Casa do Alecrim" entries become Kyoto-world or Casa-do-Mar copy.
- Tejo Rooms = BAIXA in stay-screens' 4 artboards (currently Alfama).

## 2. Re-anchor the two off-world surfaces

- itinerary-canon.jsx: the canonical itinerary screens show "Lisbon · Porto · 4 days · MAY 12–16" with the same cast — re-date/re-shape to the hero trip (Oct 12–17, 5 nights, no ·Porto) so the Document→Itinerary handoff (the wedge demo path) shows one trip.
- vesper-chat-canon.jsx group room: "Kyoto · Jun 14–19" is now the SANCTIONED group world — keep the setting, fix the cast: Maria → Mara.
- Fiction slip: trips-home-canon OrientTrim shows "Septime" (a real Paris restaurant) as dinner on the Tokyo hero → replace with a plausible Tokyo venue.

## 3. Rule the recurring dismissal + the two mystery chips

- **"Not now" semantics** (appears on Trips Home hero AND Trip Document VoteBand): record the rule — "Not now suppresses that card for the session; the cascade re-elevates it only on material change (new vote, deadline within 48h). Never a permanent dismiss without an explicit control." Add one line under each artboard.
- **Trip Document cover ◷ chip**: rule its destination (recommend: opens the Changes timeline — it reads as history). One caption line.
- **ON THE TABLE TableCards** (Trips Home): rule the tap (recommend: card tap opens the trip's decision — same destination as the list-form DraftRow's arrow). One caption line.

## 4. Close the two in-surface gaps on canonical screens

- **Mount a deck entry on FocusHome**: vesper-deck-entry.jsx designs 4 treatments; none is placed on the canonical Home artboard. Pick one (recommend the rail-line treatment — least competition with the hero), mount it on the FocusHome planning artboard, and mark the other three as appendix explorations.
- **Itinerary bottom bar + header**: the "Ask Vesper + Add" compose bar exists only as a comment — either draw it on the canonical screens or delete the comment and record that Itinerary has no compose bar (recommend: draw it; block-add and ask-in-context are real flows). And resolve the header: canonical screens use FocusedHeader which lacks the map icon — add the map-face toggle to FocusedHeader (the second-face doctrine requires an icon that flips the view) and note TripMasthead as appendix.

## 5. Fixture-alignment note + group-chat header ellipsis

- Record in governance (code-side task, not design): "Dev personas must grow theo + mara so canon demo screens are reproducible with fixture data; canon calendar anchors Oct 12 = Sunday."
- Group chat header ⋯ pill: with agency on the header TAP, rule what the ellipsis holds (recommend: thread management — rename, history, mute shortcuts — pointing at the existing thread-management board). One caption line. Also rule the privacy-seam chip: tappable → one-line explainer sheet citing Trust & Controls (recommend) or static (record either way).

## Definition of done

World ruling recorded · zero party-size/stay/venue contradictions on the Lisbon hero · itinerary + chat re-anchored (Kyoto blessed, Maria→Mara, Septime gone) · Not-now/◷/TableCard/⋯/privacy-chip all ruled · deck entry mounted · itinerary compose bar + map toggle resolved · fixture note recorded · export.
