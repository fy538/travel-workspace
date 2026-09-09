"""20 · The checks and the opening sequence, on the chosen terms (§12.9 items 3–4, §13.3). Before-and-after rows retired: the §12 vocabulary is no longer current."""
from fix import *
import instruments as I
import gen08, gen21, gen22
import re
LONG = {'The noodle counter': 'The hand-pulled noodle counter on Canal Street', 'The lunch counter on Columbia Street': 'The Dominican lunch counter on Columbia Street, Red Hook', 'The reading room at the branch library': 'The second-floor reading room at the Carroll Gardens branch library'}
def longnames():
    h = field(True)
    for a, b in LONG.items(): h = h.replace(a, b)
    return h
def enlarge(html):
    """Text at 1.3×: every CSS font-size in the phone scaled; the instruments' SVG labels keep the 10px mono floor, as the canon says they should."""
    return re.sub(r'font-size: (\d+(?:\.\d+)?)px', lambda m: f'font-size: {float(m.group(1))*1.3:.1f}px', html)
def enlarged(): return enlarge(field(True))
def destination(sent=False):
    inner = anchor('THE PIER AT SUNSET', 'SATURDAY', back=True, sub='Kept, with Maya') + gut(photo_plate(200), top=16)
    inner += gut(author_row('M', 'Maya', 'TUESDAY') + quote(MAYA_PIER, 18, 25) + fn('YOU KEPT THIS TO DO WITH MAYA, FROM HER SHARE', 8), top=12)
    if sent: inner += gut(readback('SENT', 'Asked Maya about Saturday · 7:12 PM · no answer yet'), top=12)
    inner += sect('This Saturday') + gut(day_band([(186, 0, 'SUNSET 7:04', 'dot'), (302, 43, '8:30', 'ink')], [(2, 'SATURDAY', 'start'), (345, 'THE FILM · THE LAWN, 9 MIN ON', 'end')]) + '<div style="margin-top: 6px;">' + prow('Sunset at 7:04', 'THE WEST PIER FACES IT · IT TURNS COLD FAST', first=True) + prow('Getting there', 'THE N OR R TO 59TH STREET · TWENTY MINUTES · THE PIER IS NINE MINUTES ON FOOT') + prow('Playtime on the lawn, after', '8:30 · FREE · THE SAME PARK', last=True) + '</div>')
    inner += gut(door_list(['Open the message', 'The pier']) if sent else door('Ask Maya about Saturday') + door('The pier', MUTE), top=12)
    return phone(inner)
def returned_sent(): return field_with(f'<div class="fn" style="margin-top: 4px; color: {GOLDD};">ASKED MAYA ABOUT SATURDAY · NO ANSWER YET</div>')
def board():
    r1 = [col(longnames(), caption('CHECK · LONG NAMES', 'THREE NAMES LENGTHENED', 'Serif names wrap to two lines; the mono facts stay one; the shelf&rsquo;s plates keep their height'), clip=1100),
          col(enlarged(), caption('CHECK · TEXT AT 1.3×', 'EVERY CSS SIZE SCALED', 'Nothing truncates; the instruments keep their labels at the 10px mono floor and their size, as the canon says instruments should'), clip=1100),
          notecol('The checks', [('WHAT IS CHECKED', N('The two checks that the chosen language changes: long names in serif rows and on the shelf, and text at 1.3×. The no-media check is no longer a check: a photo slot is a hatched plate by default, so the scroll as drawn is the no-photograph state. The map unavailable and results pending cases are on 22.')), ('WHAT THE INSTRUMENTS DO AT 1.3×', N('SVG labels are attributes, not CSS, so they do not scale; the canon sets a 10px mono floor inside instruments and the sentence beneath each instrument is its accessibility label. At 1.3× the serif sentence grows and the instrument does not; the reading stays whole.'))], w=560)]
    r1b = [col(enlarge(gen08.page('populated')), caption('CHECK · 1.3× · THE PAGE', 'THE PRINT ROOM ENLARGED', 'The register, the comparison and the reasons hold; the two-column comparison stays two columns'), clip=1100),
           col(enlarge(gen21.e2()), caption('CHECK · 1.3× · A JOURNEY FRAME', 'THE QUESTION TYPED, ENLARGED', 'The chip grows with the text; the map and the burden strip keep their size and labels'), clip=1100),
           col(enlarge(gen22.sorrento()), caption('CHECK · 1.3× · A SITUATION', 'SORRENTO ENLARGED', 'The section keeps its scale bar and labels; serif rows wrap to two lines'), clip=1100),
           notecol('The checks, elsewhere', [('WHAT HOLDS', N('The page, a journey frame and a situation at 1.3×. Instruments keep their size and their labels at the mono floor; the sentence under each is the reading. Chips, rows and registers grow with the text and wrap; nothing truncates.')), ('WHAT TO WATCH', N('The two-column comparison on the page narrows to about 150 pixels a column at 1.3×; a third line in a quote would cramp it. The map fragment&rsquo;s labels do not grow, by design.'))], w=560)]
    r2 = [viewport(col(field(True), caption('1 · THE OPENING', 'THE PIER, WITH MAYA', 'The door on the opening'), clip=1000)),
          col(destination(), caption('2 · WHAT IT OPENS', 'THE KEPT POSSIBILITY', 'Its photo slot, her words, the kept line; the evening on one band; the three facts; one prepared message to Maya as the door, the venue as a second. Nothing to re-keep')),
          col(field(True), caption('3 · BACK, NOTHING SENT', 'THE FIELD WHERE IT WAS', 'Entry, question and position restored; nothing has changed'), clip=1000),
          col(destination(True), caption('4 · IF THE MESSAGE IS SENT', 'A COMPACT READBACK', 'Asked, when, no answer yet. Asking is not arranging: Maya has not accepted anything and no arrangement exists')),
          col(returned_sent(), caption('5 · BACK, AFTER SENDING', 'THE SAME FIELD, ONE LINE MORE', 'The opening carries the readback under Maya&rsquo;s words; the rest of the field is untouched'), clip=1000)]
    r3 = [notecol('Opening, destination, return (§13.3)', [
              ('THE TARGET', N('&ldquo;The pier, with Maya&rdquo; opens the kept possibility as a page: her picture&rsquo;s slot, the kept line, this Saturday on one band, three facts, one prepared message to Maya, the venue as a second door. Reading and leaving preserve the state; there is no re-keeping. Preparing a message, sending it, receiving an answer and applying an authorized arrangement are four different things; frames 4 and 5 show only the second, as a readback, and nothing on either page says the outing is arranged.')),
              ('OWNER DEPENDENCY', N('This page is a design proposal. The kept intention&rsquo;s owner is unresolved: the retained-intention proposal of September 6 is unadopted, and the Life manifest lists the intention owner as pending. Life indexes the record; nothing here claims a canonical writer or that this destination exists.')),
              ('WHAT WAS EXERCISED', N('Ordered static frames. No target and no Back were exercised as a connected interaction.'))], w=760),
          notecol('What this board no longer carries', [('RETIRED', N('The before-and-after crops of the §12 polish, the two assortment treatments not chosen, and the thumbnail selection are retired with the §12 vocabulary; they are recorded in the response doc, §16, §17 and §20. The media and identity comparison was withdrawn at the founder&rsquo;s request on September 7.'))], w=560)]
    return rows_page(2260, '20 · THE CHECKS · THE OPENING SEQUENCE · 09-07 (§12.9, §13.3)', '20 · The checks, the opening sequence',
                     'The two checks the chosen language changes, long names and text at 1.3×; and the opening&rsquo;s door, what it opens, and how the person returns, with a readback only where a message was sent. Interaction untested.',
                     [('CHECKS', 'Long names; text at 1.3×', r1), ('CHECKS, ELSEWHERE', 'Text at 1.3× on the page, a journey frame, a situation', r1b), ('OPENING, DESTINATION, RETURN (§13.3)', 'Five ordered frames; a readback only where a message was sent', r2), ('NOTES', 'Where the correction lives, what was exercised, what was retired', r3)], 4600)
if __name__ == '__main__':
    import os; os.makedirs('out', exist_ok=True); h = board(); open('out/20 - Before and After.dc.html', 'w').write(h); print('wrote 20', len(h))
