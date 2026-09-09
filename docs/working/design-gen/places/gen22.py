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
def unsupported_geography():
    """A city the world supply does not cover: what exists is offered plainly, its scope named, and the person is not asked to fill the gap."""
    body = anchor('KINGSTON', 'FRIDAY 5:40 PM') + orientation('Kingston, this weekend.', 'Three places Vesper can stand behind here · the rest of the town is not covered yet') + ask()
    body += sect('What is covered', 24) + gut('<div>' + prow('The farmers&rsquo; market on the waterfront', 'SATURDAY 9–2 · FROM THE MARKET&rsquo;S OWN LISTING', first=True) + prow('The rail trail to the reservoir', 'ANY TIME · FREE · 11 KM, FLAT · FROM THE COUNTY&rsquo;S MAP') + prow('The old cement works, from the road', 'ANY TIME · SEEN FROM OUTSIDE · A READING BELOW', last=True) + '</div>')
    body += gut(consequence('THE SCOPE', 'Hours and closures are from the places&rsquo; own listings; nothing here is checked on the ground yet. Home carries the same three, nothing more, until coverage grows.'), top=16)
    body += sect('Worth understanding') + gut(fn('READING · 5 MIN', 0) + f'<div style="margin-top: 4px;">{serifline("Why the cement works face the river and the town faces away", 17, 22)}</div>' + sup('The kilns needed the river for barges; the town grew along the road behind them.') + door('The rest of the reading'))
    body += gut(door_list(['Back to New York']), top=24)
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
    inner += gut(relationship_trace('Maya and Priya wrote about the rooms upstairs; their notes stay with the place.', 'THEIR PERSPECTIVE · NOT THIS VISIT&rsquo;S'), top=16)
    return phone(inner)
def board():
    r1 = [viewport(col(missing_history(), caption('03.1 · MISSING HISTORY', 'THE WORLD IS FULL', 'The cold start: nothing missing but the person&rsquo;s past; no invitation to supply it'))),
          viewport(col(missing_friends(), caption('03.2 · MISSING FRIENDS', 'A YEAR OF RETURNS, NO ONE IN THE APP', 'The person&rsquo;s own returns are on the places; From friends is absent, not an empty prompt'))),
          viewport(col(unsupported_geography(), caption('03.3 · UNSUPPORTED GEOGRAPHY', 'KINGSTON: THREE PLACES VESPER CAN STAND BEHIND', 'What is covered, offered plainly with its sources; the scope named; Home carries the same three; no request to fill the gap'))),
          viewport(col(unavailable_information(), caption('03.4 · UNAVAILABLE INFORMATION', 'NOTHING FRESH SINCE THURSDAY', 'Every hour and tide dated; nothing invented; a door to Maya, not a form')))]
    r2 = [viewport(col(unhurried(), caption('03.5 · ONE AFTERNOON · UNHURRIED', 'THE CROSSING IS THE POINT', 'No times to keep; the rooms if the mood takes; the pier and the pool on the way back'))),
          viewport(col(constrained(), caption('03.6 · THE SAME AFTERNOON · CONSTRAINED', 'WITH YOUR FATHER, BACK BY 5', 'The arrival traced through the entrance to the stairs; the decisive fact leads; the level afternoon that still serves both of you; one honest ask to the workshop'))),
          notecol('Bounded supply, and one afternoon two ways (review, bounded pass 1 and 2)', [
              ('FOUR ABSENCES, TOLD APART', N('Missing history is 01&rsquo;s cold start. Missing friends keeps the person&rsquo;s returns and simply has no From friends section. Unsupported geography offers what Vesper can stand behind, names its sources and its scope, and says Home carries the same three. Unavailable information dates every fact and invents nothing. None of them asks the person for input as the fallback; input requests are not the universal answer.')),
              ('ONE AFTERNOON, TWO PURPOSES', N('The same place and afternoon. Unhurried: the crossing is the point, no times, the rooms if the mood takes. Constrained, with a parent who does not do stairs and a 5 o&rsquo;clock: the arrival is traced from Canal Street through the wait, the crossing, the level walk and the stairs; the decisive fact leads; the level afternoon that still serves both is offered as the useful alternative, and one honest ask goes to the workshop about a lift. Plans&rsquo; parent-aware response is the donor; this is not a persona and not an accessibility badge.')),
              ('WHAT MOVED', N('Sorrento before arrival moves to 07 as the section instrument&rsquo;s specimen; the map-unavailable and pending cases fold into unavailable information here and pending on 08. Kingston is a fixture town; its three places and sources are fixture.')),
              ('OPEN', N('Whether unsupported geography should show Home&rsquo;s three as one shared list or two views of it; drawn as a sentence. The lift question is a fixture unknown; a live version reads the venue&rsquo;s access listing. Interaction untested.'))], w=760)]
    return rows_page(2560, '03 · THE SITUATIONS · 09-08 · REVIEW, BOUNDED PASS', '03 · The situations', 'Bounded supply: four different absences told apart, none answered with an input request. Then one afternoon two ways: unhurried, and constrained by access and time.',
                     [('BOUNDED SUPPLY', 'Missing history; missing friends; unsupported geography; unavailable information', r1), ('ONE AFTERNOON, TWO WAYS', 'Unhurried; constrained', r2)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/03 - The Situations.dc.html', 'w').write(h); print('wrote 03', len(h))
