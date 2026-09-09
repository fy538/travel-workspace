"""08 · The Page: the Harbor Print Room opened from the field, drawn with the focus, path, live and social kinds. Populated, cold, and after a change.
The object-page canon governs behaviour: photo or nothing; identity from the seed, not opinion; an explicit Read up, never on open; people lines; a relationship readback."""
from kinds import *
import instruments as I
PRIYA_ROOM = 'The back room to myself for an hour.'
def arrival(stairs=True):
    """The whole arrival, from a named origin: the wait for the ferry, the crossing, the level walk, then the stairs to the rooms upstairs. The last leg is the decisive one for some visits."""
    return I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot')] + ([(2, 'stairs')] if stairs else []), 'PIER 11 · WAIT UP TO 40 · LEVEL, THEN STAIRS UP'),
                             ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot')] + ([(2, 'stairs')] if stairs else []), 'EVERY 12 · TWO BLOCKS · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118)
def ctx(t): return f'<div style="padding: 0 22px;">{fn(t, 8)}</div>'
def page(state='populated', context=None):
    """First reading, in order: what this is and what is compelling; what matters for the visit being considered; a contributed perspective. Depth below: the arrival, why, near it, reading.
    A material change re-reads the dependent lines, not only the header."""
    pop = state != 'cold'; changed = state == 'changed'; pending = state == 'pending'; unavailable = state == 'unavailable'; gone = state == 'gone'
    time = {'changed': 'SAT 9:10 AM', 'gone': 'TUE 8:15 AM'}.get(state, 'FRI 5:42 PM')
    inner = anchor('THE PRINT ROOM', time, back=True, sub='Red Hook')
    # 1 · what this is, and what is compelling here
    if pending: inner += orientation('The Harbor Print Room.', 'Van Brunt Street · a print workshop', 26, 31) + f'<div style="margin: 10px 22px 0 22px; height: 2px; border-radius: 1px; background: rgba(27,23,20,0.08); position: relative;"><div style="position: absolute; left: 0; top: 0; height: 2px; width: 38%; border-radius: 1px; background: {GOLDD};"></div></div>'
    elif gone: inner += orientation('Closed for good.', 'The workshop has left Van Brunt Street; no new address · posted Tuesday on its own listing', 26, 31)
    elif changed: inner += orientation('Closed today.', 'A private event · posted 8:40 on the workshop&rsquo;s own listing · Rooms Remade runs to Sunday', 26, 31)
    elif unavailable: inner += orientation('Rooms Remade, through Sunday, as of Thursday.', 'A print workshop on Van Brunt Street · the listing is not reachable right now', 26, 31)
    else: inner += orientation('Rooms Remade, through Sunday.', 'A print workshop on Van Brunt Street', 26, 31)
    if context: inner += ctx(context)
    inner += gut(photo_plate(150), top=16)
    if pending: return phone(inner + gut(ghost_rows(2), top=16) + gut(door_list(['Back to Red Hook']), top=24))
    # 2 · what matters for the visit being considered (one decisive fact, one implication)
    if gone:
        inner += gut(hours_register([('THE ROOMS', 'Gone with the workshop'), ('THE EXHIBITION', 'Ended Sunday')]), top=16)
        inner += gut(consequence('RED HOOK, STILL', 'The pier, the pool and the counter, by the same ferry.'), top=16)
    elif changed:
        inner += gut(hours_register([('SUNDAY', 'Open 11–6 · the last day'), ('THE ROOMS', 'Upstairs, by a flight of stairs'), ('TICKETS', 'Not confirmed')]), top=16)
        inner += gut(consequence('IF YOU STILL WANT THE ROOMS', 'Sunday is the last chance. The 11:20 ferry would have you upstairs by noon; nothing is arranged. Today, Red Hook is still the pier, the pool and the counter.'), top=16)
    elif unavailable:
        inner += gut(hours_register([('HOURS', 'Tue–Sun 11–6, as of Thursday'), ('THE ROOMS', 'Upstairs, by a flight of stairs'), ('THE LISTING', 'Not reachable since Thursday 5:42 PM')]), top=16)
        inner += gut(consequence('BEFORE YOU CROSS', 'Ask Maya, who was there Thursday, or go on the hours as of Thursday.'), top=16)
    else:
        inner += gut(hours_register([('HOURS', 'Tue–Sun 11–6'), ('THE ROOMS', 'Upstairs, by a flight of stairs'), ('TICKETS', 'Not confirmed')]), top=16)
        inner += gut(consequence('FOR SATURDAY', 'Saturday works, and Sunday is the last day.'), top=16)
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
def page_purpose(purpose):
    """The same place under the same shell, read for the purpose it was opened with. Discover: two facts and one earned connection, no arrival comparison, no verdict.
    Assess a visit: 08.1. Use an arrangement: the plan projected as a readback, the arrival timed, the first door back to the plan. The context adds a line and never a fact (Entity 09's rule, kept)."""
    if purpose == 'assess': return page('populated', context='FROM MAYA&rsquo;S SHARE · FOR SATURDAY, NOT YET ARRANGED')
    if purpose == 'discover':
        inner = anchor('THE PRINT ROOM', 'FRI 5:42 PM', back=True, sub='Red Hook')
        inner += orientation('A print workshop, upstairs on Van Brunt Street.', 'Rooms Remade through Sunday · twelve minutes from the landing', 26, 31) + ctx('FROM RED HOOK, BY FERRY · OPENED TO LOOK')
        inner += gut(photo_plate(150), top=16)
        inner += gut(hours_register([('HOURS', 'Tue–Sun 11–6'), ('THE ROOMS', 'Upstairs, by a flight of stairs')]), top=16)
        inner += gut(kick('WHY THE ROOMS ARE UPSTAIRS') + f'<div style="margin-top: 8px;">{serifline("The workshop stands on the creek bed, below the 1911 sill; the presses are a flight up for the same reason the pier floods before the street. The stairs are part of why it is still here.", 16, 22)}</div>' + fn('THE HARBOR BOOK · CH. 4 · THE SAME SILL AS THE PIER', 8) + door('Why the pier floods before the street does'), top=16)
        inner += sect('Maya and Priya were there') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', PRIYA_ROOM)) + door('Reply to Maya'))
        inner += sect('Near it') + gut('<div>' + prow('The Red Hook pier', 'FACES THE HARBOR AND THE STATUE · 9 MIN FROM THE ROOMS', first=True) + prow('The lunch counter on Columbia Street', 'TILL 4 · $11 PLATE · STANDING ROOM', last=True) + '</div>')
        inner += gut(door_list(['Read up on Rooms Remade', 'Back to Red Hook']), top=24)
        return phone(inner)
    inner = anchor('THE PRINT ROOM', 'SAT 11:05 AM', back=True, sub='Red Hook')
    inner += orientation('Rooms Remade, through Sunday.', 'A print workshop on Van Brunt Street', 26, 31) + ctx('SATURDAY 2:30 · WITH MAYA · FROM THE PLAN')
    inner += gut(photo_plate(150), top=16)
    inner += gut(readback('THE PLAN', 'Saturday 2:30, with Maya · she knows the side room'), top=16)
    inner += gut(hours_register([('TODAY', 'Open till 6'), ('THE ROOMS', 'Upstairs, by a flight of stairs'), ('TICKETS', 'Not confirmed · ask at the door')]), top=16)
    inner += gut(consequence('FOR 2:30', 'The 1:20 ferry has you upstairs before two; by the B61, leave Canal Street by 1:35.'), top=16)
    inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; arranged Thursday.', 'NOT YET VISITED'), top=16)
    inner += sect('Getting there for 2:30') + gut(I.access_compare([('THE 1:20 FERRY', [(6, 'foot'), (8, 'wait'), (25, 'ride'), (9, 'foot'), (2, 'stairs')], 'PIER 11 · LEAVE BY 1:06 · UPSTAIRS BEFORE 2'), ('THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot'), (2, 'stairs')], 'EVERY 12 · LEAVE BY 1:35 · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118))
    inner += gut(door_list(['Open the plan', 'Message Maya', 'Back to Saturday']), top=24)
    return phone(inner)
def rules_table():
    return tbl(['THE RULE', 'ENTITY 09 · 11 · 12', 'PLACES 08', 'SELECTED · PROPOSED'], [
        ['The shell', 'Photo, kind and town, name, faces, one context line; the same every time (09 A to C)', 'Anchor, sentence, plate, people', 'Selected: Entity&rsquo;s invariant shell, drawn here as the anchor, one sentence, the plate, the people line and one context line'],
        ['The body', 'The same two paragraphs and two fact rows (PRICE, TABLE) whatever the origin; &ldquo;context adds one line and never a fact&rdquo; (09)', 'A reading chosen by what the page was opened for', 'Selected: the reading below the shell follows the purpose (08.7 to 08.9); the context still adds one line and never a fact. Proposed to Entity: withdraw the invariant-body rule, keep the invariant shell'],
        ['Arrival', '&ldquo;9 min walk · 4 min drive&rdquo; from you, this once (09 A, 12.1)', 'The whole arrival from a named origin: wait, crossing, level walk, stairs', 'Selected: the one-line distance when discovering; the comparison when a visit is assessed or timed (08.8, 08.9, 03.6)'],
        ['Advice', '&ldquo;Go on a weeknight&rdquo; stays in the body when the page is opened for Saturday&rsquo;s dinner (09 C)', 'One consequence line, re-read for the occasion', 'Selected: the consequence names the occasion it serves (FOR SATURDAY, FOR 2:30); advice that does not fit the purpose is not shown'],
        ['A friend&rsquo;s contribution', 'Her line where it always is on the page; the context line says you came from her note (09 B)', 'Her words in the people section; Reply to her', 'Selected: opening her contribution goes straight to the exact original (Social 02.5), not to this page; the page cites her words and offers Reply'],
        ['Your history', 'One relationship line and the door &ldquo;Your history here&rdquo; (11 B); Life holds the record and returns with &ldquo;Open the place&rdquo; (11 C)', 'One trace line; 09.2&rsquo;s door into Life', 'Selected: Entity 11&rsquo;s pair of doors, as drawn; no door when there is no history (08.2)'],
        ['Handoffs and the arrangement', 'Directions and Reserve as interstitials; return is not a booking; a forwarded confirmation belongs to the arrangement and the page projects it (12.1 to 12.3)', 'The plan as a readback; Open the plan first', 'Selected: Entity 12 as drawn; 08.9 projects the plan and books nothing. Vesper does not book, hold or pay'],
        ['Not adopted', 'A universal renderer; automatic copying between pages; a new object owner', 'The section-heavy Focus anatomy (Entity 11 A)', 'Neither: one shell, purpose-chosen readings, the existing owners; no sections']])
def board():
    row1 = [viewport(col(page('populated', context='FROM MAYA&rsquo;S SHARE · FOR SATURDAY, NOT YET ARRANGED'), caption('08.1 · THE PAGE · A NORMAL VISIT', 'THE HARBOR PRINT ROOM, OPENED FROM 01', 'Each fact once: the exhibition and its last day in the sentence, the hours, the stairs and the tickets in the register, one line for Saturday; then Maya and Priya; then the whole arrival'))),
            viewport(col(page('cold'), caption('08.2 · THE PAGE · COLD', 'THE SAME PLACE, NO ONE YOU KNOW', 'The same first reading without a contributed perspective; no trace slot, no rationale about people who are not here'))),
            viewport(col(page('changed'), caption('08.3 · THE PAGE · A MATERIAL CHANGE', 'SATURDAY 9:10 AM: CLOSED TODAY', '&ldquo;Closed today&rdquo; leads; Sunday is offered as the last chance, not as a reschedule: nothing is arranged, no plan moved; the arrival and the people are unchanged')))]
    row3 = [viewport(col(page_purpose('discover'), caption('08.7 · OPENED TO DISCOVER IT', 'FROM THE FIELD&rsquo;S POCKET, FRIDAY', 'The shell, two facts, and one earned connection: why the rooms are upstairs, from the same sill as the pier; no arrival comparison and no verdict, because no visit is being judged'))),
            viewport(col(page_purpose('assess'), caption('08.8 · OPENED TO ASSESS A VISIT', 'FROM MAYA&rsquo;S SHARE, FOR SATURDAY · THIS IS 08.1', 'The same shell; the reading is what matters for Saturday: the register, one consequence, the people, the whole arrival with its stairs'))),
            viewport(col(page_purpose('arrangement'), caption('08.9 · OPENED FROM AN ARRANGEMENT', 'SATURDAY 2:30 WITH MAYA · FROM THE PLAN', 'The same shell; the plan projected as a readback, the arrival timed to 2:30, the first door back to the plan; the page chooses, books and moves nothing'))),
            notecol('The place reading, selected versus proposed (Entity 09, 11, 12 inspected September 9)', [('THE COMPARISON', N('One place, three purposes, one shell. Entity&rsquo;s rule is an invariant body with two fact rows; this project&rsquo;s is a reading chosen by purpose. Both keep the shell and the source rules. The table says what is selected here and what is proposed back to the Entity lab; nothing is copied automatically and no owner changes.')), ('THE RULES', rules_table()), ('THE EARNED CONNECTION', N('08.7 carries the optional breadth item once: a causal connection, drawn from the same 1911 sill the field explains, that changes what a visitor notices about the stairs without asking for an outing. It is not a quota; 08.1 to 08.6 carry none.'))], w=1180)]
    row2 = [viewport(col(page('pending'), caption('08.4 · PENDING', 'OPENED; THE FACTS NOT BACK YET', 'Identity and the slot hold their place; two ghost rows; no verdict, no route, no rationale until there is one'))),
            viewport(col(page('unavailable'), caption('08.5 · THE LISTING UNREACHABLE', 'NOTHING FRESH SINCE THURSDAY', 'Every fact dated as last seen; the implication is honest: ask Maya, or go on the hours last seen; no confident instruction survives underneath'))),
            viewport(col(page('gone'), caption('08.6 · CLOSED FOR GOOD', 'THE WORKSHOP HAS LEFT', 'The register says what is gone; the consequence names what Red Hook still is; no route, no nearby row that leads back in, no read up; the keeping stays in the record'))),
            notecol('The page, recomposed (review §P2, §P6, §P8)', [
                ('THE FIRST READING', N('Three answers in order, then depth, and each fact once: the exhibition and its last day live in the sentence; the hours, the stairs and the tickets live in the register; the Saturday line says only what follows. What matters for the visit replaces the verdict, the basis line, the reasons list and the posture. A contributed perspective (Maya and Priya), when there is one. Why is a door.')),
                ('THE ARRIVAL, WHOLE', N('The access comparison now starts from a named origin, Canal Street, draws waiting apart from movement (dashed), and ends on the stairs to the rooms upstairs. Its totals name their scope: 60 to 80 minutes by ferry depending on the wait; 41 to 47 by bus. The level walk from the landing no longer stands for arrival.')),
                ('AFTER A CHANGE', N('A change re-reads the dependent lines. Closed today offers Sunday as the last chance for the rooms and names the ferry that would do it; it does not move a visit, because this is a kept place, not an arrangement, and a changed plan needs its own event through the arrangement owner. Unreachable leaves no confident instruction under the dated facts. Closed for good drops the route, the read-up door and any nearby row that leads back in. Cold carries no rationale about people who are not here.')),
                ('WHAT WAS REMOVED', N('The posture module (HOLD to say an ordinary visit needs no booking), the separate burden receipt (folded into the arrival), the reasons list as a default (behind the door), the &ldquo;nothing yet&rdquo; trace for a newcomer, the identity map as a second plate above the fold (the field&rsquo;s map already places it; the arrival draws the approach).')),
                ('OPEN', N('Whether the identity map belongs in depth for someone approaching on foot; drawn nowhere here, kept on 07. Pending and unreachable for the arrival comparison itself. Interaction untested; the doors are not exercised.'))], w=760)]
    return rows_page(2560, '08 · THE PAGE · 09-09 · ENTITY 09, 11, 12 COMPARED', '08 · The page', 'The Harbor Print Room in six states, then the same place opened for three purposes against the Entity lab&rsquo;s invariant page: one shell, a reading chosen by purpose, the whole arrival when a visit is judged or timed.',
                     [('THE FIRST READING, THREE STATES', 'A normal visit; cold; a material change', row1), ('THREE MORE', 'Pending; the listing unreachable; closed for good', row2), ('ONE PLACE, THREE PURPOSES', 'Discover; assess a visit; use an arrangement · against Entity 09, 11, 12', row3)], 9000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/08 - The Page.dc.html', 'w').write(h); print('wrote 08', len(h))
