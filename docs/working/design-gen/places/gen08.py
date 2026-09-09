"""08 · The Page: the Harbor Print Room opened from the field, drawn with the focus, path, live and social kinds. Populated, cold, and after a change.
The object-page canon governs behaviour: photo or nothing; identity from the seed, not opinion; an explicit Read up, never on open; people lines; a relationship readback."""
from kinds import *
PRIYA_ROOM = 'The back room to myself for an hour.'
def page(state='populated'):
    pop = state not in ('cold',); changed = state == 'changed'; pending = state == 'pending'; unavailable = state == 'unavailable'; gone = state == 'gone'
    time = {'changed': 'SAT 9:10 AM', 'gone': 'TUE 8:15 AM'}.get(state, 'FRI 5:42 PM')
    inner = anchor('THE PRINT ROOM', time, back=True, sub='Red Hook')
    if pending: inner += orientation('The Harbor Print Room.', 'Van Brunt Street · nine minutes from the ferry landing · kept, from Maya&rsquo;s share', 26, 31) + f'<div style="margin: 10px 22px 0 22px; height: 2px; border-radius: 1px; background: rgba(27,23,20,0.08); position: relative;"><div style="position: absolute; left: 0; top: 0; height: 2px; width: 38%; border-radius: 1px; background: {GOLDD};"></div></div>'
    elif unavailable: inner += orientation('Rooms Remade, through Sunday. Open till 6, as last seen.', 'Van Brunt Street · nine minutes from the ferry landing · kept, from Maya&rsquo;s share', 26, 31)
    elif gone: inner += orientation('Closed for good. The workshop has left Van Brunt Street.', 'Posted Tuesday on its own listing · kept, from Maya&rsquo;s share', 26, 31)
    elif changed: inner += orientation('Closed today. Rooms Remade runs to Sunday.', 'Van Brunt Street · nine minutes from the ferry landing · kept, from Maya&rsquo;s share', 26, 31)
    else: inner += orientation('Rooms Remade, through Sunday. Open till 6.', 'Van Brunt Street · nine minutes from the ferry landing · ' + ('kept, from Maya&rsquo;s share' if pop else 'not kept'), 26, 31)
    inner += gut(photo_plate(150), top=16) + gut(identity_map(120), top=12)
    if pending:
        inner += gut(ghost_rows(2), top=16)
    elif gone:
        inner += gut(verdict('The rooms upstairs are gone; the crossing and the pier remain.', 'CLOSED FOR GOOD, POSTED TUESDAY · KEPT TUESDAY, FROM MAYA · NEVER VISITED'), top=16)
    elif changed: inner += gut(verdict('Sunday, then: the last day of the rooms upstairs, and the crossing on a Sunday morning.', 'CLOSED TODAY, POSTED 8:40 · SUNDAY UNCHANGED · TICKETING UNCONFIRMED'), top=16)
    elif unavailable: inner += gut(verdict('Go on a weekday for the side room; Saturday for the crossing itself.', 'MAYA AND PRIYA · HOURS AS LAST SEEN THURSDAY · THE LISTING IS NOT REACHABLE'), top=16)
    elif pop: inner += gut(verdict('Go on a weekday for the side room; Saturday for the crossing itself.', 'MAYA AND PRIYA · HOURS FROM THE LISTING · TICKETING UNCONFIRMED'), top=16)
    else: inner += gut(verdict('A print workshop with the exhibition upstairs; the crossing is half the visit.', 'HOURS FROM THE LISTING · TICKETING UNCONFIRMED · NO ONE YOU KNOW HAS BEEN'), top=16)
    if not pending:
        if gone: rows = [('HOURS', 'Closed for good'), ('THE EXHIBITION', 'Rooms Remade ended Sunday'), ('THE LISTING', 'Says the workshop has left Van Brunt Street; no new address')]
        elif unavailable: rows = [('HOURS', 'Tue–Sun 11–6, as last seen Thursday'), ('THE EXHIBITION', 'Rooms Remade, to Sunday, as last seen'), ('THE LISTING', 'Not reachable since Thursday 5:42 PM')]
        else: rows = [('HOURS', 'Tue–Sun 11–6' if not changed else 'Closed Saturday 8 · Tue–Sun 11–6 otherwise'), ('THE EXHIBITION', 'Rooms Remade, in the two upstairs rooms, to Sunday'), ('TICKETS', 'Not confirmed either way')]
        change = ('Closed today for a private event; posted this morning on the workshop&rsquo;s own listing. Sunday is unchanged.' if changed else 'Closed for good; posted Tuesday on the workshop&rsquo;s own listing.' if gone else None)
        inner += sect('Hours and the exhibition') + gut(hours_register(rows, change=change))
    if pop and not pending:
        inner += sect('From Maya and Priya') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', PRIYA_ROOM)))
        inner += gut(door('Reply to Maya') + door('Ask Vesper privately', MUTE), top=8)
    if pending: inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; not visited.', 'ONE KEPT PLACE · NO VISIT'), top=16)
    elif gone: inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; never visited. The keeping stays in the record.', 'ONE KEPT PLACE · CLOSED BEFORE A VISIT'), top=16)
    elif pop: inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; not visited.', 'ONE KEPT PLACE · NO VISIT'), top=16)
    else: inner += gut(relationship_trace('Not kept, not visited.', 'NOTHING YET'), top=16)
    if not gone:
        inner += sect('Getting there') + gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN · EVERY 40', '9 MIN ON FOOT', '~40') + horizon_doors([('ACCESS', 'The ferry against the B61: what each asks of the afternoon'), ('AROUND', 'The pier and the pool, from the landing')]))
        if not pending: inner += gut(burden_receipt('WHAT THE CROSSING ASKS', 'ON FOOT', '9 minutes from the landing, level, exposed along the water'))
    if pending:
        inner += gut('<div style="height: 36px;"></div>' + ghost_rows(2), top=0)
    elif gone:
        inner += gut('<div style="height: 36px;"></div>' + evidence_apparatus('WHY THIS CHANGED', ['The listing says the workshop has left; no new address is given', 'Rooms Remade ended Sunday, as scheduled', 'The pier, the pool and the counter are unchanged']), top=0)
        inner += gut(consequence('WHAT THIS CHANGES', 'Red Hook by ferry is still the pier, the pool and the counter. The kept place stays in the record as closed; nothing asks you to do anything about it.'), top=16)
        inner += sect('Today') + gut(temporal_posture('DONE', 'Nothing to hold. Maya and Priya&rsquo;s notes stay with the place.', 'CLOSED FOR GOOD'))
    else:
        inner += gut('<div style="height: 36px;"></div>' + (evidence_apparatus('WHY VESPER THINKS THIS', ['Rooms Remade closes Sunday; Saturday is the last day the crossing and the exhibition line up', 'The workshop closes at 6; a 2:00 ferry leaves two hours upstairs and the walk', 'Maya and Priya both went on weekdays, for the empty rooms']) if not changed else evidence_apparatus('WHY THIS CHANGED', ['Closed today, posted this morning', 'Sunday is the last day of Rooms Remade and is unchanged', 'The crossing itself is untouched'])), top=0)
        inner += gut(consequence('WHAT THIS CHANGES SATURDAY', 'The Print Room by 2:30, the crossing back at 5:10; the pier at sunset is another neighborhood, and Red Hook to Sunset Park after 6 isn&rsquo;t listed here yet.' if not changed else 'Saturday in Red Hook is the pier, the pool and the counter; the Print Room moves to Sunday, its last day.'), top=16)
        if unavailable: inner += sect('Today') + gut(temporal_posture('HOLD', 'Nothing needs booking. The listing has been unreachable since Thursday; the hours above are the last seen.', 'LISTING UNREACHABLE'))
        else: inner += sect('Today') + gut(temporal_posture('HOLD' if not changed else 'ACT NOW', 'Nothing needs booking. The ferry is every 40 minutes; the workshop holds no times.' if not changed else 'Sunday is the last day; the 11:20 ferry puts you upstairs by noon.', 'NOTHING TO CONFIRM' if not changed else 'SUNDAY, THE LAST DAY'))
        inner += gut(live_fallback('IF THE EXHIBITION IS TICKETED AND SOLD OUT' if not unavailable else 'IF THE LISTING STAYS UNREACHABLE', 'The workshop floor is open without a ticket; the pier and the pool are the afternoon.' if not unavailable else 'Go on the hours last seen, or ask Maya; the crossing is the same either way.'), top=16)
    if not pending:
        inner += sect('Near it') + gut(possibility_row('The Red Hook pool, before', 'Lap swim, then the Print Room at 11' if not gone else 'Lap swim, then the pier', 'SATURDAY 7–8:30 AM · BRING A LOCK') + next_rows(['The pier, faces the harbor and the Statue', 'The lunch counter on Columbia Street, till 4'], places=True))
    inner += gut(door_list((['Read up on Rooms Remade'] if not gone else []) + ['Back to Red Hook']), top=24)
    return phone(inner)
def board():
    row1 = [viewport(col(page('populated'), caption('THE PAGE · POPULATED', 'THE HARBOR PRINT ROOM, OPENED FROM 01', 'Identity from the seed, a photo slot, the verdict with its basis, the hours register, two people side by side, the trace, the crossing, why and what it changes, the posture, a fallback, what is near'))),
            viewport(col(page('cold'), caption('THE PAGE · COLD', 'THE SAME PLACE, NO ONE YOU KNOW', 'The verdict rests on world facts only; no people section; the trace says nothing yet'))),
            viewport(col(page('changed'), caption('THE PAGE · AFTER A CHANGE', 'SATURDAY 9:10 AM: CLOSED TODAY', 'The change in the hours register with its source; the verdict re-read; the posture becomes act now for Sunday, the last day')))]
    row2 = [viewport(col(page('pending'), caption('THE PAGE · PENDING', 'OPENED; THE FACTS NOT BACK YET', 'Identity, the slot, the map and the trace hold their place; the hairline under the name; two ghost rows where the register and the reasons will be; no verdict until there is one'))),
            viewport(col(page('unavailable'), caption('THE PAGE · THE LISTING UNREACHABLE', 'FRIDAY 5:42 PM: NOTHING FRESH SINCE THURSDAY', 'The register carries the facts as last seen, dated; the basis says the listing is unreachable; the posture holds; the fallback names the two honest moves'))),
            viewport(col(page('gone'), caption('THE PAGE · CLOSED FOR GOOD', 'TUESDAY 8:15 AM: THE WORKSHOP HAS LEFT', 'The verdict re-read; the register says closed with its source; the trace keeps the keeping as a record; no crossing section, no read up; the posture is done'))),
            notecol('The page, and the kinds it needed', [
                ('WHAT IT IS', N('One place opened from the field, drawn with the focus, path, live and social kinds of the a26e3228 union on the chosen terms, in six states. Behaviour follows the object-page canon: photo or nothing; the name and the facts from the seed, never an opinion; Read up as an explicit door, never on open; people as their own lines; the person&rsquo;s relationship to the place as a readback. Every fact is a fixture; nothing verifies the workshop, its hours or its exhibition.')),
                ('KINDS, IN ORDER', tbl(['SECTION', 'KIND', 'ORIGIN'], [['The anchor and the sentence', 'scope handle · orientation', 'Home&rsquo;s kit'], ['The photo slot', 'plate, photo or nothing', 'object-page canon'], ['The map fragment', 'focus_identity_map', 'canon'], ['The claim and its basis', 'focus_verdict · path_evidence_apparatus', 'canon'], ['Hours and the exhibition', 'the hours register · the change', 'The Page'], ['Maya and Priya', 'social_plural_comparison · focus_human_note', 'canon'], ['Your trace', 'focus_relationship_trace', 'canon'], ['Getting there', 'the burden strip · focus_horizon_doors · live_burden_receipt', 'canon'], ['What it changes', 'path_consequence', 'canon'], ['Today', 'live_temporal_posture · live_fallback', 'canon'], ['Near it', 'focus_possibility_row · path_next_rows', 'canon'], ['Doors', 'continuity doors, text arrows', 'Home&rsquo;s kit']])),
                ('THE THREE STATES ADDED', N('Pending keeps what the seed already gives (identity, the slot, the map, the trace) and draws ghost rows where the register and the reasons will be; no verdict is invented. Unreachable dates every fact as last seen and says so in the basis; the posture holds and the fallback names the two honest moves, go on the hours last seen or ask Maya. Closed for good re-reads the verdict, drops the crossing and the read-up door, keeps the keeping in the record as closed, and asks nothing of the person.')),
                ('WHAT IS LEFT OUT, AND WHY', N('The Page&rsquo;s candidate set and candidate rows, its arrangement registers, the stage and the stub-as-list belong to the plan surface that was retired; &ldquo;Add to day&rdquo; is a mechanism. The lag register is Home&rsquo;s job. The canon&rsquo;s solid action seam is drawn as doors, per the founder&rsquo;s choice. The why-this inspector is folded into the basis line under the verdict.')),
                ('OPEN', N('Whether a page needs both a verdict and an evidence list, or the basis line alone; drawn with both so the founder can cut one. The identity map&rsquo;s geometry is illustrative. Interaction untested; the doors are not exercised.'))], w=760)]
    return rows_page(2260, '08 · THE PAGE · 09-08', '08 · The page', 'The Harbor Print Room opened from the field, in six states: populated, cold, after a change; pending, the listing unreachable, closed for good. The focus, path, live and social kinds of the canon on the chosen terms, governed by the object-page rulings.',
                     [('ONE PLACE, THREE STATES', 'Populated; cold; after a change', row1), ('THREE MORE', 'Pending; the listing unreachable; closed for good', row2)], 7600)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/08 - The Page.dc.html', 'w').write(h); print('wrote 08', len(h))
