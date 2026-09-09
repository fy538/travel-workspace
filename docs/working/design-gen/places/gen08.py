"""08 · The Page: the Harbor Print Room opened from the field, drawn with the focus, path, live and social kinds. Populated, cold, and after a change.
The object-page canon governs behaviour: photo or nothing; identity from the seed, not opinion; an explicit Read up, never on open; people lines; a relationship readback."""
from kinds import *
import instruments as I
PRIYA_ROOM = 'The back room to myself for an hour.'
def arrival(stairs=True):
    """The whole arrival, from a named origin: the wait for the ferry, the crossing, the level walk, then the stairs to the rooms upstairs. The last leg is the decisive one for some visits."""
    return I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot')] + ([(2, 'stairs')] if stairs else []), 'PIER 11 · WAIT UP TO 40 · LEVEL, THEN STAIRS UP'),
                             ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot')] + ([(2, 'stairs')] if stairs else []), 'EVERY 12 · TWO BLOCKS · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118)
def page(state='populated'):
    """First reading, in order: what this is and what is compelling; what matters for the visit being considered; a contributed perspective. Depth below: the arrival, why, near it, reading.
    A material change re-reads the dependent lines, not only the header."""
    pop = state != 'cold'; changed = state == 'changed'; pending = state == 'pending'; unavailable = state == 'unavailable'; gone = state == 'gone'
    time = {'changed': 'SAT 9:10 AM', 'gone': 'TUE 8:15 AM'}.get(state, 'FRI 5:42 PM')
    inner = anchor('THE PRINT ROOM', time, back=True, sub='Red Hook')
    # 1 · what this is, and what is compelling here
    if pending: inner += orientation('The Harbor Print Room.', 'Van Brunt Street · a print workshop', 26, 31) + f'<div style="margin: 10px 22px 0 22px; height: 2px; border-radius: 1px; background: rgba(27,23,20,0.08); position: relative;"><div style="position: absolute; left: 0; top: 0; height: 2px; width: 38%; border-radius: 1px; background: {GOLDD};"></div></div>'
    elif gone: inner += orientation('Closed for good.', 'The workshop has left Van Brunt Street; no new address · posted Tuesday on its own listing', 26, 31)
    elif changed: inner += orientation('Closed today; the exhibition ends Sunday.', 'Rooms Remade, in the two rooms upstairs · posted 8:40 on the workshop&rsquo;s own listing', 26, 31)
    elif unavailable: inner += orientation('Rooms Remade, through Sunday.', 'A print workshop with the exhibition upstairs · hours as last seen Thursday; the listing is not reachable', 26, 31)
    else: inner += orientation('Rooms Remade, through Sunday.', 'A print workshop with the exhibition in the two rooms upstairs · open till 6', 26, 31)
    inner += gut(photo_plate(150), top=16)
    if pending: return phone(inner + gut(ghost_rows(2), top=16) + gut(door_list(['Back to Red Hook']), top=24))
    # 2 · what matters for the visit being considered (one decisive fact, one implication)
    if gone:
        inner += gut(hours_register([('THE ROOMS', 'Gone with the workshop'), ('THE EXHIBITION', 'Ended Sunday')]), top=16)
        inner += gut(consequence('WHAT THIS CHANGES', 'Red Hook by ferry is still the pier, the pool and the counter. Nothing here asks anything of you.'), top=16)
    elif changed:
        inner += gut(hours_register([('TODAY', 'Closed for a private event'), ('SUNDAY', 'Open 11–6, the last day of Rooms Remade'), ('TICKETS', 'Not confirmed either way')]), top=16)
        inner += gut(consequence('WHAT THIS CHANGES SATURDAY', 'The Print Room moves to Sunday; the 11:20 ferry puts you upstairs by noon. Saturday in Red Hook is the pier, the pool and the counter.'), top=16)
    elif unavailable:
        inner += gut(hours_register([('HOURS', 'Tue–Sun 11–6, as last seen Thursday'), ('THE EXHIBITION', 'Rooms Remade, to Sunday, as last seen'), ('THE LISTING', 'Not reachable since Thursday 5:42 PM')]), top=16)
        inner += gut(consequence('BEFORE YOU CROSS', 'Nothing here is fresh since Thursday. Ask Maya, who was there then, or go on the hours last seen; the crossing is the same either way.'), top=16)
    else:
        inner += gut(hours_register([('HOURS', 'Tue–Sun 11–6'), ('THE EXHIBITION', 'Rooms Remade, in the two rooms upstairs, to Sunday'), ('TICKETS', 'Not confirmed either way')]), top=16)
        inner += gut(consequence('FOR SATURDAY', 'The last day the crossing and the exhibition line up is Sunday, so Saturday works; the rooms are up a flight of stairs, and ticketing is not confirmed.' if pop else 'The last day the crossing and the exhibition line up is Sunday; the rooms are up a flight of stairs, and ticketing is not confirmed.'), top=16)
    # 3 · a contributed perspective, when there is one; no trace slot when it would say nothing
    if pop and not gone:
        inner += sect('Maya and Priya were there') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', PRIYA_ROOM)) + door('Reply to Maya') + door('Ask Vesper privately', MUTE))
        inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share.', 'NOT YET VISITED'), top=16)
    elif pop and gone:
        inner += sect('Maya and Priya were there') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', PRIYA_ROOM)))
        inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; closed before a visit. The keeping stays in the record.', 'YOUR LAST VISIT · NONE'), top=16)
    # depth: the arrival, why, near it, reading
    if not gone:
        inner += sect('Getting there') + gut(arrival(stairs=True) + horizon_doors([('ACCESS', 'The ferry against the B61: the wait, the crossing, the stairs'), ('AROUND', 'The pier and the pool, from the landing')]))
        inner += sect('Near it') + gut('<div>' + prow('The Red Hook pier', 'FACES THE HARBOR AND THE STATUE · 9 MIN FROM THE ROOMS', first=True) + prow('The lunch counter on Columbia Street', 'TILL 4 · $11 PLATE · STANDING ROOM', last=True) + '</div>')
    inner += gut(door_list((['Why this, and what it rests on'] if not gone else []) + (['Read up on Rooms Remade'] if not gone else []) + ['Back to Red Hook']), top=24)
    return phone(inner)
def board():
    row1 = [viewport(col(page('populated'), caption('08.1 · THE PAGE · A NORMAL VISIT', 'THE HARBOR PRINT ROOM, OPENED FROM 01', 'First reading in three answers: what this is and what is compelling; what matters for Saturday, one decisive fact and its implication; Maya and Priya&rsquo;s perspectives. Depth below: the whole arrival with its stairs, near it, and a door to why'))),
            viewport(col(page('cold'), caption('08.2 · THE PAGE · COLD', 'THE SAME PLACE, NO ONE YOU KNOW', 'The same first reading without a contributed perspective; no trace slot, no rationale about people who are not here'))),
            viewport(col(page('changed'), caption('08.3 · THE PAGE · A MATERIAL CHANGE', 'SATURDAY 9:10 AM: CLOSED TODAY', '&ldquo;Closed today; the exhibition ends Sunday&rdquo; leads; the dependent line moves the visit to Sunday and names the ferry; the arrival and the people are unchanged')))]
    row2 = [viewport(col(page('pending'), caption('08.4 · PENDING', 'OPENED; THE FACTS NOT BACK YET', 'Identity and the slot hold their place; two ghost rows; no verdict, no route, no rationale until there is one'))),
            viewport(col(page('unavailable'), caption('08.5 · THE LISTING UNREACHABLE', 'NOTHING FRESH SINCE THURSDAY', 'Every fact dated as last seen; the implication is honest: ask Maya, or go on the hours last seen; no confident instruction survives underneath'))),
            viewport(col(page('gone'), caption('08.6 · CLOSED FOR GOOD', 'THE WORKSHOP HAS LEFT', 'The register says what is gone; the consequence names what Red Hook still is; no route, no nearby row that leads back in, no read up; the keeping stays in the record'))),
            notecol('The page, recomposed (review §P2, §P6, §P8)', [
                ('THE FIRST READING', N('Three answers in order, then depth. What this is and what is compelling (the sentence, the slot). What matters for the visit being considered (the register and one implication, replacing the verdict, the basis line, the reasons list and the posture). A contributed perspective (Maya and Priya), when there is one. Why it rests on what it rests on is a door, not a default.')),
                ('THE ARRIVAL, WHOLE', N('The access comparison now starts from a named origin, Canal Street, draws waiting apart from movement (dashed), and ends on the stairs to the rooms upstairs. Its totals name their scope: 60 to 80 minutes by ferry depending on the wait; 41 to 47 by bus. The level walk from the landing no longer stands for arrival.')),
                ('AFTER A CHANGE', N('A change re-reads the dependent lines. Closed today moves the visit to Sunday and names the ferry that gets you upstairs by noon. Unreachable leaves no confident instruction under the dated facts. Closed for good drops the route, the read-up door and any nearby row that leads back in; what Red Hook still is takes their place. Cold carries no rationale about people who are not here.')),
                ('WHAT WAS REMOVED', N('The posture module (HOLD to say an ordinary visit needs no booking), the separate burden receipt (folded into the arrival), the reasons list as a default (behind the door), the &ldquo;nothing yet&rdquo; trace for a newcomer, the identity map as a second plate above the fold (the field&rsquo;s map already places it; the arrival draws the approach).')),
                ('OPEN', N('Whether the identity map belongs in depth for someone approaching on foot; drawn nowhere here, kept on 07. Pending and unreachable for the arrival comparison itself. Interaction untested; the doors are not exercised.'))], w=760)]
    return rows_page(2260, '08 · THE PAGE · 09-08 · REVIEW P2, P6, P8', '08 · The page', 'The Harbor Print Room opened from the field, in six states, recomposed after the September 8 review: a smaller first reading with depth intact, the whole arrival with its stairs, and every dependent line re-read after a change.',
                     [('THE FIRST READING, THREE STATES', 'A normal visit; cold; a material change', row1), ('THREE MORE', 'Pending; the listing unreachable; closed for good', row2)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/08 - The Page.dc.html', 'w').write(h); print('wrote 08', len(h))
