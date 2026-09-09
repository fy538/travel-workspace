"""03 · The situations, recomposed (review: bounded pass items 1 and 2). Row 1, bounded supply: four different absences, told apart, none answered with an input request.
Row 2, one afternoon two ways: unhurried exploration against a constrained visit with an access and a time requirement, Plans' parent-aware response as the donor."""
from fix import *
from kinds import *
import instruments as I
import gen19v3 as g
def missing_history():
    """No history: the world is full; nothing is missing but the person's past. This is 01's cold start, unchanged."""
    return g.v3(False)
def missing_friends():
    """History but no friends: the person's own returns are on the places; From friends is simply absent, not an empty invitation."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset. Saturday, 7:04.', 'Kept Tuesday · your third this year · the film on the lawn after') + ask()
    body += gut(f'<div style="display: flex; flex-direction: column;">{kick("SATURDAY AT THE PIER · YOUR THIRD THIS YEAR")}{I.pier_line()}<div style="margin-top: 12px;">{serifline("Sunset from the west pier at 7:04; it turns cold fast. You were last here in May, at low water; the film on the lawn is new.")}</div>{fn("YOU, MAY 9 AND JULY 20", 8)}<div style="margin-top: 8px;">{doors(("The pier", GOLDD))}</div></div>', top=24)
    sh = list(g.SHELF); sh[0] = ('The noodle counter', 'Hand-pulled · you, twice in August', 'CASH')
    body += sect('Any day') + gut(browse_shelf(sh)) + g.redhook(False) + g.evening(False) + g.understanding() + g.sunday(False) + g.morning(False) + gut(door_list(['Another neighborhood', 'Sunday, all day']), top=24)
    return phone(body)
def shared_supply():
    """The place-relative view of Home 14's bounded supply set: the same supported locality (New York), the same time (Saturday 9:30, Home 14.3) and the same source set.
    Items: the flea (its own notice, Saturdays through October); Open House New York (Oct 17–18; timed-site registration closed Thursday; walk-in sites need none); the L notice (MTA; single-tracking after 11 PM Mon–Thu);
    the forecast (two stations); the tide table; one chapter of The Harbor Book. No friends, no history, no chosen places."""
    body = anchor('NEW YORK', 'SATURDAY 9:30 AM') + orientation('The flea, under the bridge, until three.', 'Clear, 41&deg; · Saturdays through October · nothing else has changed since Thursday') + ask()
    body += gut('<div>' + prow('The flea, under the bridge', 'FROM 8 UNTIL 3 · THE BREAD STALL SELLS OUT BY TEN · THE MARKET&rsquo;S OWN NOTICE', first=True, last=True) + '</div>' + door('Directions'), top=24)
    body += sect('Open House, October 17 and 18') + gut('<div>' + prow('The walk-in sites', 'NO REGISTRATION NEEDED · OCT 17–18', first=True) + prow('The timed sites', 'REGISTRATION CLOSED THURSDAY', last=True) + '</div>')
    body += sect('Getting around') + gut(hours_register([('THE L', 'Normal today; single-tracking after 11 PM, Monday to Thursday'), ('THE TIDE', 'Low water 2:40 to 5; high 8:40')]))
    body += sect('Worth understanding') + gut(g.FLOOD(118) + fn('THE HARBOR BOOK · CH. 4 · 4 MIN', 12) + f'<div style="margin-top: 4px;">{serifline("The pumps under the park finish what the gates cannot", 17, 22)}</div>' + sup('The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.') + door('Read the chapter'))
    body += gut(door_list(['Another neighborhood']), top=24)
    return phone(body)
def unavailable_information():
    """Current information unavailable: the field keeps what it knows, dates it, and does not ask the person to supply it."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset, from Maya&rsquo;s share. Saturday, 7:04.', 'Hours and tides as last seen Thursday · the listings are not reachable right now') + ask()
    body += gut(f'<div style="display: flex; flex-direction: column;">{kick("SATURDAY AT THE PIER · AS LAST SEEN THURSDAY")}{I.pier_line()}<div style="margin-top: 12px;">{serifline("Sunset from the west pier at 7:04; it turns cold fast. Low water from 2:40 as of Thursday; the film at 8:30 if the lawn&rsquo;s listing still holds.")}</div>{fn("MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo; · NOTHING FRESH SINCE THURSDAY", 8)}<div style="margin-top: 8px;">{doors(("The pier", GOLDD), ("Ask Maya about Saturday", MUTE))}</div></div>', top=24)
    body += sect('Any day') + gut(browse_shelf(g.SHELF[:2])) + gut(consequence('WHAT IS NOT FRESH', 'Every hour and every tide here is Thursday&rsquo;s. Nothing is invented to fill the gap, and nothing asks you to.'), top=16)
    body += g.redhook(True) + gut(door_list(['Another neighborhood', 'Try again']), top=24)
    return phone(body)
def unhurried():
    """One afternoon, unhurried: the crossing is the point; the rooms upstairs if the mood takes; no times."""
    inner = anchor('THE PRINT ROOM', 'SAT 12:40 PM', back=True, sub='Red Hook · this afternoon')
    inner += orientation('The crossing, then the rooms upstairs if you like.', 'No times to keep · the workshop is open till 6 · the pier and the pool are on the way back', 26, 31)
    inner += gut(photo_plate(150), top=16)
    inner += gut(hours_register([('THE ROOMS', 'Rooms Remade, upstairs, to Sunday'), ('THE CROSSING', 'Every 40 from Pier 11; the boat is half the visit'), ('AROUND', 'The pier, nine minutes; the pool till 8:30 tomorrow')]), top=16)
    inner += sect('Maya and Priya were there') + gut(plural_comparison((('M', 'Maya', 'THURSDAY'), 'THE SIDE ROOM', MAYA_ROOM), (('P', 'Priya', 'A RAINY TUESDAY'), 'THE BACK ROOM', 'The back room to myself for an hour.')))
    inner += gut(door_list(['The next ferry', 'Reply to Maya']), top=24)
    return phone(inner)
def constrained():
    """The same afternoon with a parent who does not do stairs and a 5 o'clock to be back for: the arrival traced through the entrance and the interior; the decisive fact on the surface; a useful alternative that still serves the purpose."""
    inner = anchor('THE PRINT ROOM', 'SAT 12:40 PM', back=True, sub='Red Hook · with your father, back by 5')
    inner += orientation('The rooms are up a flight of stairs; no lift is listed.', 'The crossing and the workshop floor are level · back by 5 means the 3:20 boat', 26, 31)
    inner += gut(I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot'), (2, 'stairs')], 'PIER 11 · WAIT UP TO 40 · LEVEL, THEN STAIRS'), ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot'), (2, 'stairs')], 'EVERY 12 · TWO BLOCKS · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118), top=16)
    inner += gut(consequence('THE DECISIVE FACT', 'The exhibition is upstairs and the listing names no lift. The workshop floor, the crossing and the pier are level; that is the afternoon that serves you both, unless the workshop confirms a lift.'), top=16)
    inner += gut(I.day_band(12, 18, [('13:20', '13:45', '', 'ink'), ('14:00', '15:00', 'THE FLOOR 2–3', 'gold'), ('15:20', '15:45', '', 'ink')], [('17:00', 'BACK BY 5', 'ring')], [('start', 'NOON · 1:20 BOAT OUT', 'start'), ('end', '3:20 BACK', 'end')]), top=16)
    inner += gut(door('Ask the workshop about a lift') + door('The level afternoon: the crossing, the floor, the pier', MUTE), top=8)
    inner += gut(relationship_trace('Maya and Priya wrote about the rooms upstairs.', 'THEIR NOTES, ON THE PLACE'), top=16)
    return phone(inner)
def board():
    r1 = [viewport(col(missing_history(), caption('03.1 · MISSING HISTORY', 'THE WORLD IS FULL', 'The cold start: nothing missing but the person&rsquo;s past; no invitation to supply it'))),
          viewport(col(missing_friends(), caption('03.2 · MISSING FRIENDS', 'A YEAR OF RETURNS, NO ONE IN THE APP', 'The person&rsquo;s own returns are on the places; From friends is absent, not an empty prompt'))),
          viewport(col(shared_supply(), caption('03.3 · BOUNDED SUPPLY, THE PAIR WITH HOME 14', 'NEW YORK, SATURDAY 9:30 · THE SAME SET HOME 14.3 OPENS', 'The place-relative view of Home&rsquo;s bounded set at the same time: the flea as a place with its notice, the Open House sites with the expired registration told from the walk-ins, the L and the tide as getting-around facts, the chapter as the reading; nothing generated, nothing asked'))),
          viewport(col(unavailable_information(), caption('03.4 · UNAVAILABLE INFORMATION', 'NOTHING FRESH SINCE THURSDAY', 'Every hour and tide dated; nothing invented; a door to Maya, not a form')))]
    r2 = [viewport(col(unhurried(), caption('03.5 · ONE AFTERNOON · UNHURRIED', 'THE CROSSING IS THE POINT', 'No times to keep; the rooms if the mood takes; the pier and the pool on the way back'))),
          viewport(col(constrained(), caption('03.6 · THE SAME AFTERNOON · CONSTRAINED', 'WITH YOUR FATHER, BACK BY 5', 'The arrival traced through the entrance to the stairs; the decisive fact leads; the level afternoon that still serves both of you; one honest ask to the workshop'))),
          notecol('Bounded supply, and one afternoon two ways (review, bounded pass 1 and 2)', [
              ('FOUR ABSENCES, TOLD APART', N('Missing history is 01&rsquo;s cold start. Missing friends keeps the person&rsquo;s returns and simply has no From friends section. Bounded supply is now the reconciled pair with Home 14: the same locality, time and source set, rendered place-relative. Unavailable information dates every fact and invents nothing. None of them asks the person for input as the fallback.')),
              ('THE SHARED SUPPLY SET, AS LEDGERED', tbl(['ITEM', 'SOURCE', 'DATES · EXPIRY', 'UNKNOWN', 'HOME 14', 'PLACES 03.3'], [['The flea, under the bridge', 'The market&rsquo;s own notice', 'Saturdays through October; today 8 to 3', 'Whether the bread stall holds past ten', '14.2 named, 14.3 the one live thing', 'The place, its hours, directions'], ['Open House New York', 'OHNY listing', 'Oct 17–18; timed registration Tue noon to Thu, expired; walk-ins need none', 'Which sites are walk-in this year', '14.1 opens, 14.2 open until Sunday, 14.3 closed', 'The walk-in sites as places; the timed sites marked closed'], ['The L service notice', 'MTA', 'After 11 PM Mon–Thu; daytime normal', 'End date of the work', '14.1', 'A getting-around fact; normal today'], ['Forecast and tide', 'Two stations; the tide table', 'Today: clear, 41&deg;; low 2:40–5, high 8:40', 'None', '14.1–14.3 the reading', 'A getting-around fact'], ['The Harbor Book, ch. 4', 'The book', 'No expiry', 'None', '14.1 the card, 14.2–14.3 the row', 'The reading, with the section']])),
              ('ONE AFTERNOON, TWO PURPOSES', N('The same place and afternoon. Unhurried: the crossing is the point, no times, the rooms if the mood takes. Constrained, with a parent who does not do stairs and a 5 o&rsquo;clock: the arrival is traced from Canal Street through the wait, the crossing, the level walk and the stairs; the decisive fact leads; the level afternoon that still serves both is offered as the useful alternative, and one honest ask goes to the workshop about a lift. Plans&rsquo; parent-aware response is the donor; this is not a persona and not an accessibility badge.')),
              ('WHAT MOVED', N('Sorrento before arrival moves to 07 as the section instrument&rsquo;s specimen; the map-unavailable and pending cases fold into unavailable information here and pending on 08. The Kingston specimen of September 8 is withdrawn: it described a shared supply without drawing the pair. Home leads the supply selection for this round; Places renders it. No new city rollout or supply system is requested.')),
              ('OPEN', N('Whether the Open House walk-in sites deserve a pocket with a map once the sites are known; drawn as rows. The lift question on 03.6 is a fixture unknown; a live version reads the venue&rsquo;s access listing. Interaction untested.'))], w=760)]
    return rows_page(2560, '03 · THE SITUATIONS · 09-08 · REVIEW, BOUNDED PASS', '03 · The situations', 'Bounded supply: four absences told apart, none answered with an input request, with 03.3 the reconciled pair with Home 14 (same locality, time and source set). Then one afternoon two ways: unhurried, and constrained by access and time.',
                     [('BOUNDED SUPPLY', 'Missing history; missing friends; the pair with Home 14; unavailable information', r1), ('ONE AFTERNOON, TWO WAYS', 'Unhurried; constrained', r2)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/03 - The Situations.dc.html', 'w').write(h); print('wrote 03', len(h))
