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
LT13 = ('<style>.lt13 .vk-t-serifMast{font-size:39px;line-height:44.2px}.lt13 .vdl-t-unitTitle{font-size:22.1px;line-height:28.6px}.lt13 .vk-t-serifTitle,.lt13 .vdl-t-placeName{font-size:20.8px;line-height:26px}'
        '.lt13 .vdl-t-excerpt{font-size:23.4px;line-height:32.5px}.lt13 .vdl-t-sectionHeading,.lt13 .vk-t-bodySmMedium{font-size:16.9px}.lt13 .vdl-t-supportLine{font-size:16.25px}.lt13 .vdl-t-metaLine{font-size:13px}.lt13 .vdl-t-placeStamp{font-size:14.3px}</style>')
def enlarge(html):
    """Text at 1.3×: every CSS font-size in the phone scaled; the instruments' SVG labels keep the 10px mono floor, as the canon says they should."""
    h = re.sub(r'font-size: (\d+(?:\.\d+)?)px', lambda m: f'font-size: {float(m.group(1))*1.3:.1f}px', html)
    h = re.sub(r'line-height: (\d+(?:\.\d+)?)px', lambda m: f'line-height: {float(m.group(1))*1.3:.1f}px', h)
    return LT13 + f'<div class="lt13">{h}</div>'
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
    r1 = [col(longnames(), caption('04.6 · CHECK · LONG NAMES', 'THREE NAMES LENGTHENED', 'Serif names wrap to two lines; the mono facts stay one; the shelf&rsquo;s plates keep their height'), clip=1100),
          col(enlarged(), caption('04.7 · CHECK · TEXT AT 1.3×', 'EVERY CSS SIZE SCALED', 'Nothing truncates; the instruments keep their labels at the 10px mono floor and their size, as the canon says instruments should'), clip=1100),
          notecol('The checks', [('WHAT IS CHECKED', N('The two checks that the chosen language changes: long names in serif rows and on the shelf, and text at 1.3×. The no-media check is no longer a check: a photo slot is a hatched plate by default, so the scroll as drawn is the no-photograph state. The map unavailable and results pending cases are on 22.')), ('WHAT THE INSTRUMENTS DO AT 1.3×', N('SVG labels are attributes, not CSS, so they do not scale; the canon sets a 10px mono floor inside instruments and the sentence beneath each instrument is its accessibility label. At 1.3× the serif sentence grows and the instrument does not; the reading stays whole.'))], w=560)]
    r1b = [col(enlarge(gen08.page('populated')), caption('04.8 · CHECK · 1.3× · THE PAGE', 'THE PRINT ROOM ENLARGED', 'The register, the comparison and the reasons hold; the two-column comparison stays two columns'), clip=1100),
           col(enlarge(gen21.e2()), caption('04.9 · CHECK · 1.3× · A JOURNEY FRAME', 'THE QUESTION TYPED, ENLARGED', 'The chip grows with the text; the map and the burden strip keep their size and labels'), clip=1100),
           col(enlarge(gen22.constrained()), caption('04.10 · CHECK · 1.3× · A SITUATION', 'THE CONSTRAINED AFTERNOON, ENLARGED', 'The access comparison keeps its scale and labels; the register and the decisive fact wrap; nothing truncates'), clip=1100),
           notecol('The checks, elsewhere', [('WHAT HOLDS', N('The page, a journey frame and a situation at 1.3×. Instruments keep their size and their labels at the mono floor; the sentence under each is the reading. Chips, rows and registers grow with the text and wrap; nothing truncates.')), ('WHAT TO WATCH', N('The two-column comparison on the page narrows to about 150 pixels a column at 1.3×; a third line in a quote would cramp it. The map fragment&rsquo;s labels do not grow, by design.'))], w=560)]
    r1c = [col(enlarge(gen08.page_purpose('arrangement')), caption('04.11 · CHECK · 1.3× · THE ARRANGEMENT READING', 'THE PAGE OPENED FROM SATURDAY&rsquo;S PLAN, ENLARGED', 'New on September 9: the plan readback, the leave-by sentence and the timed arrival at 1.3×; the readback wraps to two lines and the comparison keeps its scale'), clip=1100),
           col(enlarge(gen08.extension('there')), caption('04.12 · CHECK · 1.3× · AT THE PIER', 'THE SITUATED READING, ENLARGED', 'New on September 9: the section keeps its size and its labels at the mono floor while the sentence grows; the not-sensed line wraps to two lines and the register&rsquo;s label column holds'), clip=1100),
           notecol('The two new readings, enlarged', [('WHAT IS CHECKED', N('The readings drawn on September 9 had not been seen at 1.3&times;: the page opened from an arrangement (08.9) and the situated reading at the pier (08.11). Both are checked here rather than assumed from the earlier pass.')),
               ('WHAT HOLDS', N('The plan readback wraps to two lines and keeps its label column; the leave-by sentence and the timed comparison hold their scale, with the instrument&rsquo;s labels at the 10px mono floor. On the pier frame the section keeps its size while the sentence grows; the line saying nothing is sensed wraps to two lines rather than truncating.'))], w=560)]
    r2 = [viewport(col(field(True), caption('04.1 · THE OPENING', 'THE PIER, FROM MAYA&rsquo;S SHARE', 'The door on the opening: the pier; a second door asks Maya about Saturday'), clip=1000)),
          col(destination(), caption('04.2 · WHAT IT OPENS', 'THE KEPT POSSIBILITY', 'Its photo slot, her words, the kept line; the evening on one band; the three facts; one prepared message to Maya as the door, the venue as a second. Nothing to re-keep')),
          col(field(True), caption('04.3 · BACK, NOTHING SENT', 'THE FIELD WHERE IT WAS', 'Entry, question and position restored; nothing has changed'), clip=1000),
          col(destination(True), caption('04.4 · IF THE MESSAGE IS SENT', 'A COMPACT READBACK', 'Asked, when, no answer yet. Asking is not arranging: Maya has not accepted anything and no arrangement exists')),
          col(returned_sent(), caption('04.5 · BACK, AFTER SENDING', 'THE SAME FIELD, ONE LINE MORE', 'The opening carries the readback under Maya&rsquo;s words; the rest of the field is untouched'), clip=1000)]
    dest = tbl(['DOOR ON THE FIELD', 'WHERE IT GOES', 'DRAWN AT', 'OWNER · STATUS'], [
        ['The pier (the opening)', 'The place, as a page', 'Places 08.1', 'Place; the object-page canon · selected'],
        ['Ask Maya about Saturday', 'One prepared message to Maya; sent on Send', 'Places 04.2, 04.4', 'The messaging sender (Social) · selected'],
        ['Reply to Maya (From friends)', 'Her original first, then a reply to her only', 'Places 02 H3, H2.1 · Social 02.5', 'Social, original-first receiving · selected'],
        ['Ask Vesper privately', 'A private question about the place; Maya is never a recipient', 'Places 02 H3.1 · Social 02.6', 'Chat&rsquo;s owner, in context · selected'],
        ['Make it Saturday, with Maya', 'One proposal through the arrangement owner; nothing arranged until she answers', 'Places 02 H4.1', 'The arrangement owner (Plan) · selected; the owner&rsquo;s view not drawn here'],
        ['Everything from friends, here and elsewhere', 'Friends&rsquo; originals in this city; a friend&rsquo;s original without a place is not pinned here', 'Places 02 H2 · Social 08.1&ndash;08.3', 'Social · Elsewhere selected; non-spatial placement is Social&rsquo;s named proposal (Home&rsquo;s addressed region, Life&rsquo;s reader, Life &middot; People), not adopted here'],
        ['Your last evening here', 'The exact record of an earlier encounter, found by the place', 'Places 09.2 · Life 03b, 05', 'Life, direct retrieval · selected'],
        ['What has changed since', 'The current plan against the remembered one', 'Life P3', 'Life, current against remembered · selected; not drawn on this project'],
        ['A place typed into the question', 'The field, map-led, then the place', 'Places 02 E2, E4', 'Places · selected']])
    r3 = [notecol('Where the doors go (review, bounded pass 3)', [('THE MAP OF DESTINATIONS', dest), ('THE RULE', N('The field connects to its actual destinations rather than describing them. Social 08.1 to 08.3 were inspected before citing: a friend&rsquo;s original without a place arrives once in Home&rsquo;s addressed region, opens to Life&rsquo;s exact-source reader, and is found again under the person; that placement is Social&rsquo;s named proposal and is not adopted here, so nothing non-spatial is pinned on the field, and Elsewhere keeps the geographic social value. Life&rsquo;s retrieval (03b, 05) and current-against-remembered (P3) were inspected for the record door. This project draws the door and the return, not a destination&rsquo;s interior.'))], w=1180),
          notecol('Opening, destination, return (§13.3)', [
              ('THE TARGET', N('&ldquo;The pier&rdquo; opens the place; &ldquo;Ask Maya about Saturday&rdquo; opens one prepared message. A possibility kept from her share is not an outing with her: the sentence says from, the fact line says kept, not yet arranged, and only her answer would make it with. Frames 04.4 and 04.5 show the send as a readback; nothing says the outing is arranged.')),
              ('OWNER DEPENDENCY', N('The kept possibility&rsquo;s page (04.2) is a design proposal. Its owner is unresolved: the retained-intention proposal of September 6 is unadopted, and the Life manifest lists the intention owner as pending. Nothing here claims a canonical writer.')),
              ('WHAT WAS EXERCISED', N('Ordered static frames. No door and no Back were exercised as a connected interaction.'))], w=560)]
    return rows_page(2260, '20 · THE CHECKS · THE OPENING SEQUENCE · 09-07 (§12.9, §13.3)', '20 · The checks, the opening sequence',
                     'The two checks the chosen language changes, long names and text at 1.3×; and the opening&rsquo;s door, what it opens, and how the person returns, with a readback only where a message was sent. Interaction untested.',
                     [('CHECKS', 'Long names; text at 1.3×', r1), ('CHECKS, ELSEWHERE', 'Text at 1.3× on the page, a journey frame, a situation', r1b), ('CHECKS · THE SEPTEMBER 9 READINGS', 'Text at 1.3× on the arrangement reading and on the pier', r1c), ('OPENING, DESTINATION, RETURN (§13.3)', 'Five ordered frames; a readback only where a message was sent', r2), ('WHERE THE DOORS GO', 'The field&rsquo;s continuations, their destinations and their owners', r3)], 4600)
if __name__ == '__main__':
    import os; os.makedirs('out', exist_ok=True); h = board(); open('out/20 - Before and After.dc.html', 'w').write(h); print('wrote 20', len(h))
