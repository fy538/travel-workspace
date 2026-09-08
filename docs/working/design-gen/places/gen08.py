"""08 · The Page: the Harbor Print Room opened from the field, drawn with the focus, path, live and social kinds. Populated, cold, and after a change.
The object-page canon governs behaviour: photo or nothing; identity from the seed, not opinion; an explicit Read up, never on open; people lines; a relationship readback."""
from kinds import *
PRIYA_ROOM = 'The back room to myself for an hour.'
def page(state='populated'):
    pop = state != 'cold'; changed = state == 'changed'
    inner = anchor('THE PRINT ROOM', 'FRI 5:42 PM' if not changed else 'SAT 9:10 AM', back=True, sub='Red Hook')
    inner += orientation('Rooms Remade, through Sunday. Open till 6.' if not changed else 'Closed today. Rooms Remade runs to Sunday.', 'Van Brunt Street · nine minutes from the ferry landing · ' + ('kept, from Maya&rsquo;s share' if pop else 'not kept'), 26, 31)
    inner += gut(photo_plate(150), top=16)
    inner += gut(identity_map(120), top=10)
    # verdict and its basis
    if changed: inner += gut(verdict('Sunday, then: the last day of the rooms upstairs, and the crossing on a Sunday morning.', 'CLOSED TODAY, POSTED 8:40 · SUNDAY UNCHANGED · TICKETING UNCONFIRMED'), top=18)
    elif pop: inner += gut(verdict('Go on a weekday for the side room; Saturday for the crossing itself.', 'MAYA AND PRIYA · HOURS FROM THE LISTING · TICKETING UNCONFIRMED'), top=18)
    else: inner += gut(verdict('A print workshop with the exhibition upstairs; the crossing is half the visit.', 'HOURS FROM THE LISTING · TICKETING UNCONFIRMED · NO ONE YOU KNOW HAS BEEN'), top=18)
    # hours register
    rows = [('HOURS', 'Tue–Sun 11–6' if not changed else 'Closed Saturday 8 · Tue–Sun 11–6 otherwise'), ('THE EXHIBITION', 'Rooms Remade, in the two upstairs rooms, to Sunday'), ('TICKETS', 'Not confirmed either way')]
    inner += sect('Hours and the exhibition') + gut(hours_register(rows, change='Closed today for a private event; posted this morning on the workshop&rsquo;s own listing. Sunday is unchanged.' if changed else None))
    # people
    if pop:
        inner += sect('From Maya and Priya') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', PRIYA_ROOM)))
        inner += gut(door('Reply to Maya') + door('Ask Vesper privately', MUTE), top=8)
        inner += gut(relationship_trace('Kept Tuesday, from Maya&rsquo;s share; not visited.', 'ONE KEPT PLACE · NO VISIT'), top=18)
    else:
        inner += gut(relationship_trace('Not kept, not visited.', 'NOTHING YET'), top=18)
    # getting there
    inner += sect('Getting there') + gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN · EVERY 40', '9 MIN ON FOOT', '~40') + horizon_doors([('ACCESS', 'The ferry against the B61: what each asks of the afternoon'), ('AROUND', 'The pier and the pool, from the landing')]))
    inner += gut(burden_receipt('WHAT THE CROSSING ASKS', 'ON FOOT', '9 minutes from the landing, level, exposed along the water'), top=14)
    # path: evidence, consequence
    inner += gut('<div style="height: 36px;"></div>' + evidence_apparatus('WHY VESPER THINKS THIS', ['Rooms Remade closes Sunday; Saturday is the last day the crossing and the exhibition line up', 'The workshop closes at 6; a 2:00 ferry leaves two hours upstairs and the walk', 'Maya and Priya both went on weekdays, for the empty rooms']) if not changed else evidence_apparatus('WHY THIS CHANGED', ['Closed today, posted this morning', 'Sunday is the last day of Rooms Remade and is unchanged', 'The crossing itself is untouched']))
    inner += gut(consequence('WHAT THIS CHANGES SATURDAY', 'The Print Room by 2:30, the crossing back at 5:10; the pier at sunset is another neighborhood, and Red Hook to Sunset Park after 6 isn&rsquo;t listed here yet.' if not changed else 'Saturday in Red Hook is the pier, the pool and the counter; the Print Room moves to Sunday, its last day.'), top=18)
    # live posture and fallback
    inner += sect('Today') + gut(temporal_posture('HOLD' if not changed else 'ACT NOW', 'Nothing needs booking. The ferry is every 40 minutes; the workshop holds no times.' if not changed else 'Sunday is the last day; the 11:20 ferry puts you upstairs by noon.', 'NOTHING TO CONFIRM' if not changed else 'SUNDAY, THE LAST DAY'))
    inner += gut(live_fallback('IF THE EXHIBITION IS TICKETED AND SOLD OUT', 'The workshop floor is open without a ticket; the pier and the pool are the afternoon.'), top=16)
    # possibility, next
    inner += sect('Near it') + gut(possibility_row('The Red Hook pool, before', 'Lap swim, then the Print Room when it opens', 'SATURDAY 7–8:30 AM · BRING A LOCK') + next_rows(['The pier, faces the harbor and the Statue', 'The lunch counter on Columbia Street, till 4']))
    inner += gut(door_list(['Read up on Rooms Remade', 'Back to Red Hook']), top=24)
    return phone(inner)
def board():
    cols = [viewport(col(page('populated'), caption('THE PAGE · POPULATED', 'THE HARBOR PRINT ROOM, OPENED FROM 01', 'Identity from the seed, a photo slot, the verdict with its basis, the hours register, two people side by side, the trace, the crossing, why and what it changes, the posture, a fallback, what is near'))),
            viewport(col(page('cold'), caption('THE PAGE · COLD', 'THE SAME PLACE, NO ONE YOU KNOW', 'The verdict rests on world facts only; no people section; the trace says nothing yet'))),
            viewport(col(page('changed'), caption('THE PAGE · AFTER A CHANGE', 'SATURDAY 9:10 AM: CLOSED TODAY', 'The change in the hours register with its source; the verdict re-read; the posture becomes act now for Sunday, the last day'))),
            notecol('The page, and the kinds it needed', [
                ('WHAT IT IS', N('One place opened from the field, drawn with the focus, path, live and social kinds of the a26e3228 union on the chosen terms. Behaviour follows the object-page canon: photo or nothing; the name and the facts from the seed, never an opinion; Read up as an explicit door, never on open; people as their own lines; the person&rsquo;s relationship to the place as a readback. Every fact is a fixture; nothing verifies the workshop, its hours or its exhibition.')),
                ('KINDS, IN ORDER', tbl(['SECTION', 'KIND', 'ORIGIN'], [['The anchor and the sentence', 'scope handle · orientation', 'Home&rsquo;s kit'], ['The map fragment', 'focus_identity_map', 'canon'], ['The photo slot', 'plate, photo or nothing', 'object-page canon'], ['The claim and its basis', 'focus_verdict · path_evidence_apparatus', 'canon'], ['Hours and the exhibition', 'the hours register · the change', 'The Page'], ['Maya and Priya', 'social_plural_comparison · focus_human_note', 'canon'], ['Your trace', 'focus_relationship_trace', 'canon'], ['Getting there', 'the burden strip · focus_horizon_doors · live_burden_receipt', 'canon'], ['What it changes', 'path_consequence', 'canon'], ['Today', 'live_temporal_posture · live_fallback', 'canon'], ['Near it', 'focus_possibility_row · path_next_rows', 'canon'], ['Doors', 'continuity doors, text arrows', 'Home&rsquo;s kit']])),
                ('WHAT IS LEFT OUT, AND WHY', N('The Page&rsquo;s candidate set and candidate rows, its arrangement registers, the stage and the stub-as-list belong to the plan surface that was retired; &ldquo;Add to day&rdquo; is a mechanism. The lag register (surfacing what you were not looking for) is Home&rsquo;s job. The canon&rsquo;s solid action seam is drawn as doors, per the founder&rsquo;s choice. The why-this inspector is folded into the basis line under the verdict.')),
                ('OPEN', N('Whether a page needs both a verdict and an evidence list, or the basis line alone; drawn with both so the founder can cut one. The identity map&rsquo;s geometry is illustrative. The change state is one case; pending and unavailable states for a page are not drawn. Interaction untested; the doors are not exercised.'))], w=760)]
    return rows_page(2260, '08 · THE PAGE · 09-08', '08 · The page', 'The Harbor Print Room opened from the field, populated, cold and after a change: the focus, path, live and social kinds of the canon on the chosen terms, governed by the object-page rulings.',
                     [('ONE PLACE, THREE STATES', 'Populated; cold; after a change', cols)], 5200)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/08 - The Page.dc.html', 'w').write(h); print('wrote 08', len(h))
