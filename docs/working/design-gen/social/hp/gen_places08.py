"""08 · Decisions, reuse inventory, receiving contract, canon deltas, dependencies, content cost. A sheet, not phones."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import head, FOOT, N
from gen_merge import tbl, blk
from gen_placeskit import STAMP, hh, OUT

def board():
    decisions = blk('THE FIVE DECISIONS &middot; WHAT THE BOARDS RECOMMEND &middot; PROPOSED, NOT RULED', tbl(['', 'QUESTION', 'RECOMMENDATION', 'EVIDENCE'], [
        ['1', 'Default composition', 'Content-led field with the map one tap away, by default. Map-led earns the first viewport only when orientation is the job: an unvisited scope, or a question that is itself spatial. No mandatory crown; one lead, then a small contrasting set, then the collection ends and names its widenings.', '02 phones 1 and 3 (same evidence); 05 phone 1; 07'],
        ['2', 'Spatial interaction', 'Map and field share one result set and revision; the toggle preserves question, scope, set and position. Panning is inspection. A change of city, question, time or friends scope is a deliberate act that establishes a new set and says so on the page. Out-of-window things stay on the map in ghost ink with their reason.', '02 phone 2; 03 phones 2 and 5; 05 phone 4'],
        ['3', 'Content forms', 'Pins are one expression. New forms: the dated event stub (series &ne; occurrence), the area card (outline, not a point), the composed possibility (says Vesper composed it), the question control, the withdrawn line, the collection&rsquo;s end. Findings stay bare; shares and sendable things are cards.', '01; 02 through 07'],
        ['4', 'Social receiving', 'From friends is a scope the person chooses; inside it, the original material leads with no preamble and enrichment only where it adds one fact. Outside it, one friend line may sit inside the place it is about without switching the page. Reply to a person and Ask Vesper have distinct recipients and neither auto-sends. Withdrawal is a local honest line; no-supply names the scope. Never an invite ending.', '04 all phones; 07 phone 1'],
        ['5', 'Continuation', 'Open the existing destination: the entity page (Entities), the exact occurrence, the reading, the route; a provider continuation is labelled external. Return restores scope, question, form, selection and position. Sending an idea goes through the existing arrangement owner and reads back once; nothing is duplicated into Home or Life for having been viewed.', '02 phones 4&ndash;5; 03 phones 3&ndash;4; 05 phone 4; 06 phones 1&ndash;4']]))
    inventory = blk('KEEP &middot; ADAPT &middot; REPLACE &middot; THE EXISTING COMPONENTS AND SECTIONS', tbl(['COMPONENT / SECTION', 'DISPOSITION', 'WHY'], [
        ['PlacesWorkspace, PlacesRootExperience', 'KEEP', 'The mature section-based workspace is the container; the boards compose within it, they do not replace it'],
        ['PlacesSectionFeed (semantic units before the section feed)', 'ADAPT', 'Generated understanding takes the lead only when it is the best unit; it is not a layer above the feed by default (02, 07)'],
        ['PlacesFeedCardView card families (candidate, editorial, experience, memory, notice, social)', 'KEEP &middot; ADAPT', 'Each family maps to kit elements on 01; the assortment must be legible as different kinds of reason, not a section per producer'],
        ['FriendFeedCard (socialCard)', 'REPLACE', 'The person, sentence and place-name strip becomes the share card with the original photograph, and the onward destination (04)'],
        ['PlacesMapCanvas, PlacesPinPeekCard, PlaceAreaMap', 'ADAPT', 'One map encoding at every scale: avatar pins, gold stops, dashed neighborhoods, tinted areas, dated squares, no mark for city precision; pin peek stays'],
        ['PlacesSearchState, search utilities', 'ADAPT', 'Search is the question made visible; the question control carries it; clearing returns to the parent scope'],
        ['PlacesCollectionScreen (saved, been)', 'KEEP', 'Continuity doors with honest counts at the end of the field'],
        ['PlaceHome mast (placesHomeMast)', 'DEMOTE', 'Only at true cold start or a newly entered city; never a paragraph on every visit (anatomy &sect;3.2)'],
        ['EntityObjectPage / ObjectPageRebuild', 'KEEP &middot; NOT REDRAWN', 'Places opens it; the three registers on 04 phone 3 are context carried in, not a new page'],
        ['PlacesSemanticUnitCard', 'ADAPT', 'The bare finding and paired evidence forms; no card unless the unit is a coherent object'],
        ['Result-set identity (PlacesResultSetRef)', 'DEPEND', 'The visible intent model on 02, 03 and 05 assumes it; until the producer and consumers exist, the map and field cannot claim to be the same set']]))
    receiving = blk('THE RECEIVING CONTRACT &middot; OBJECT, SOURCE, ACTION, DESTINATION, RETURN STATE', tbl(['OBJECT', 'SOURCE', 'ACTION', 'DESTINATION', 'RETURN STATE'], [
        ['A stable venue (the Print Room)', 'Canonical Place owner', 'Open', 'The entity page (Entities)', 'Same scope, question, set, position; nothing marked viewed'],
        ['A dated occurrence (the listening hour)', 'Event supply (Content)', 'Open; then external', 'The occurrence page; the hall&rsquo;s own page, labelled', 'Question and selection kept'],
        ['A series (the greenmarket)', 'Event supply', 'Inspect this occurrence', 'The occurrence, never the series as if it were one', 'Same'],
        ['A reusable comparison (the rooms)', 'Reusable enrichment', 'Read; open its place', 'In place; the entity page', 'Same'],
        ['A friend&rsquo;s share (Maya)', 'Contribution owner, under grant', 'Read; reply; open its place', 'In place; Chat/People for the reply; the entity page', 'Same; withdrawal updates locally'],
        ['A city-level status (Dana)', 'Contribution owner &middot; city precision', 'Open the doorway', 'The other city&rsquo;s scope', 'Back returns to the previous scope'],
        ['A prepared suggestion', 'Chat preparation', 'Send', 'The arrangement owner', 'Readback once; back to the question'],
        ['A place changed (bakery hours)', 'Canonical Place owner', 'Read', 'The entity page', 'Same'],
        ['The record at its place (the ferry)', 'Life index', 'Open in Life', 'The dossier (Life)', 'Back to Places at the same position'],
        ['A widening door', 'Structured state', 'Widen', 'A new collection, named', 'Back to the previous collection']]))
    deltas = blk('PROPOSED CANON CHANGES &middot; EACH AN EXACT CASE AND DELTA', tbl(['#', 'CANON TODAY', 'PROPOSED', 'CASE'], [
        ['C1', 'Anatomy &sect;2.5 / &sect;9.4: the page ends when the next unit does not beat silence; &ldquo;this is all of it today&rdquo;', 'A finite first collection ends and names its deliberate widenings by area, time and subject; widening produces a new named collection with new material', '02 phone 1, 07 phones 2&ndash;3'],
        ['C2', 'Places union (34 kinds): no dated-occurrence kind; events are venues with dates', 'Add the dated event stub as a kind; series and occurrence are distinct objects; the venue alone is not the event', '02, 03, 07'],
        ['C3', 'No composed-possibility kind on Places', 'A sequence Vesper composed renders as one, says so, and is never an advertised event or an arrangement', '01, 07'],
        ['C4', 'Search replaces the feed', 'The question is a visible, editable control; clearing returns to the parent scope; a changed question is a new set, said so', '03 phones 1 and 5'],
        ['C5', 'Out-of-window material is dropped', 'It stays on the map in ghost ink with its reason, and in a &ldquo;Not this window&rdquo; group with the alternative time named', '03'],
        ['C6', 'Social anatomy: four admissible forms', 'Unchanged; add the withdrawn line and the friends no-supply line as required treatments; one friend line may sit inside a place outside the friends scope', '04, 07'],
        ['C7', 'Map default (anatomy &sect;12.3: no map-first redesign)', 'Content-led by default; map-led earned when orientation is the job (an unvisited scope, a spatial question)', '02 phone 3 vs 1; 05 phone 1']]))
    deps = blk('UNRESOLVED DEPENDENCIES AND IMPLEMENTATION GAPS', tbl(['DEPENDENCY', 'OWNER', 'WHAT THE BOARDS ASSUME'], [
        ['A pre-Plan suggestion to one person; the thin-guest path', 'Arrangements (existing owner)', '06 phones 2&ndash;3 mark the send as a dependency, not a working button'],
        ['PlacesResultSetRef producer and consumers', 'Places backend', 'Every same-set claim on 02, 03, 05'],
        ['Event supply: dated occurrences, series identity, freshness, licensing', 'Content', 'The listening hour, the market, the grain terminal opening'],
        ['Provider-specific media and map rights', 'Content', 'Photograph plates are slots; map and list availability per provider'],
        ['Practical assessment (fresh / stale / unknown)', 'Integration', '03 and 06: unknown availability, the kitchen change, stale hours treatment'],
        ['Route-from-origin', 'Places + a chosen origin', 'Never drawn without one; 05 says so on the phone'],
        ['Reusable enrichment: the room comparison, the shaded-side finding, the three ways home', 'Content', 'Made once; the boards do not assume a producer exists'],
        ['Reply to a person from a share', 'Chat / People', 'A distinct recipient from Ask; not a memory']]))
    cost = blk('CONTENT COST &middot; CLASSES, NOT ESTIMATES', tbl(['BOARD', 'PROVIDER FACTS', 'REUSABLE ENRICHMENT', 'VIEWER-SPECIFIC SELECTION', 'ON-DEMAND GENERATION'], [
        ['02 &middot; A', '4 (venue, hour, market, area pair)', '1 (the rooms)', '1 (the order of five, viewer-neutral)', '0'],
        ['03 &middot; B', '3 (hour, pier, hours compared)', '0', '2 (&ldquo;not this window&rdquo;, the adjustments)', '0'],
        ['04 &middot; C', '2 (listing, exhibition)', '1 (the rooms)', '3 (three attributed contributions under grant)', '0'],
        ['05 &middot; D', '2 (the two places&rsquo; access)', '1 (the schematic, labelled)', '1 (Dana&rsquo;s status)', '0'],
        ['06 &middot; E', '2 (the hour, the kitchen change)', '0', '2 (the dinner row, the three orderings)', '1 (the Chat answer, bounded to two facts)'],
        ['07', '4', '4 (rooms, finding, area, reading)', '3 (sequence, changed hours, doors)', '0']]))
    open_items = blk('OPEN &middot; FOR THE FOUNDER', N('<b>The fixture world.</b> This project mapped the brief&rsquo;s packet onto the shared world (00). Say so if it should stay separate. <b>The map default</b> (C7) is the one comparison the brief said visual work should settle; 02 and 05 draw both sides on the same evidence and recommend content-led with an earned map-led case. <b>The event stub</b> (C2) is a kind admission and therefore a canon event. <b>The dependency on arrangements</b> (06) is the largest gap between what is drawn and what can be built; nothing here should be read as a claim that it works. <b>Not drawn:</b> night and dark; live conditions; a real-data evaluation, which needs a reviewed source packet.'))
    inner = (head(f'{STAMP} &middot; 08 &middot; DECISIONS, REUSE, RECEIVING, DELTAS', '08 &middot; What is proposed, what is reused, what is a canon change, what engineering still owes',
                  'The decisions board the brief asks for in &sect;7: the five decisions with the boards&rsquo; recommendations, the keep / adapt / replace inventory of existing components, the receiving contract, the proposed canon changes as exact cases and deltas, the unresolved dependencies, and the content-cost classes per board. Nothing here is ruled; every row points at the phone that is its evidence.')
             + '<div style="display: flex; flex-direction: column; gap: 34px;">' + decisions + inventory + receiving + deltas + deps + cost + open_items + '</div>')
    return HEAD + f'<div style="width: 1720px; min-height: {hh("08", 4200)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '08 - Decisions and Reuse.dc.html'), 'w').write(html); print('wrote 08', len(html))
