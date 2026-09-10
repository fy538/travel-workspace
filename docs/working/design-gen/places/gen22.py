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
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'Kept Tuesday · your third this year · Sunset Park') + ask()
    body += gut(f'<div style="display: flex; flex-direction: column;">{kick("SATURDAY AT THE PIER · YOUR THIRD THIS YEAR")}{I.pier_line()}<div style="margin-top: 12px;">{serifline("It turns cold fast after sunset; the lawn is nine minutes on, and the film is free if the listing holds.")}</div>{fn("YOU, MAY 9 AND JULY 20", 8)}<div style="margin-top: 8px;">{doors(("The pier", GOLDD))}</div></div>', top=24)
    sh = list(g.SHELF); sh[0] = ('The noodle counter', 'Hand-pulled · you, twice in August', 'CASH')
    body += sect('Any day') + gut(browse_shelf(sh)) + g.redhook(False) + g.evening(False) + g.understanding() + g.sunday(False) + g.morning(False) + gut(door_list(['Another neighborhood', 'Sunday, all day']), top=24)
    return phone(body)
def shared_supply():
    """The place-relative view of the set Home 14.3 opens, after Home re-paired on September 9: the same locality (New York), day and hour (Saturday 9:30).
    Items and dates exactly as Home carries them: the flea (its own notice; Saturdays through October; today 8 to 3; the bread stall by ten); Open House New York (Oct 17-18; timed registration Tuesday noon to Thursday, closed; walk-ins need none);
    the L (MTA; after 11 PM Mon-Thu; normal today; end date unknown); the forecast and tide (clear 41 degrees; low 2:40-5, high 8:40); The Harbor Book ch. 4. Home shows what a person receives; this shows the same set as a field."""
    body = anchor('NEW YORK', 'SATURDAY 9:30 AM') + orientation('The flea, under the bridge, until three.', 'Clear, 41&deg; · Saturdays through October · nothing else has changed since Thursday') + ask()
    body += gut('<div>' + prow('The flea, under the bridge', 'FROM 8 UNTIL 3 · THE BREAD STALL SELLS OUT BY TEN · THE MARKET&rsquo;S OWN NOTICE', first=True, last=True) + '</div>' + door('Directions'), top=24)
    body += sect('Open House, October 17 and 18') + gut('<div>' + prow('The walk-in sites', 'NO REGISTRATION NEEDED · OCT 17&ndash;18', first=True) + prow('The timed sites', 'REGISTRATION CLOSED THURSDAY · IT RAN FROM TUESDAY NOON', last=True) + '</div>')
    body += sect('Getting around') + gut(hours_register([('THE L', 'Normal today; single-tracking after 11 PM, Monday to Thursday'), ('THE TIDE', 'Low water 2:40 to 5; high 8:40')]))
    body += sect('Worth understanding') + gut(g.FLOOD(118) + fn('THE HARBOR BOOK · CH. 4 · 4 MIN', 12) + f'<div style="margin-top: 4px;">{serifline("The pumps under the park finish what the gates cannot", 17, 22)}</div>' + sup('The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.') + door('Read the chapter'))
    body += gut(door_list(['Another neighborhood']), top=24)
    return phone(body)
def scoped_correction():
    """Home's scoped help, received on a place. The person corrects the purpose of the constrained afternoon: it was for their parents.
    The correction is scoped to that visit, like Home 14 row two B: it changes what is offered now and is not kept as a preference."""
    inner = anchor('THE PRINT ROOM', 'SAT 1:05 PM', back=True, sub='Red Hook · with your father, back by 5')
    inner += orientation('The level afternoon, then: the crossing, the floor and the pier.', 'You said the stairs were the problem today, not the place', 26, 31)
    inner += gut(readback('FOR TODAY', '&ldquo;That was for my parents.&rdquo; · the stairs matter this afternoon', GOLDD), top=16)
    inner += gut(hours_register([('THE FLOOR', 'Level from the door; the presses are working till 4'), ('THE ROOMS', 'Upstairs, by a flight of stairs · not this afternoon'), ('THE PIER', 'Nine minutes, level, benches at the end')]), top=16)
    inner += gut(consequence('WHAT THIS CHANGES', 'Today&rsquo;s afternoon is the level one, and the 3:20 boat still gets you back by 5. Nothing is kept about how you like to visit.'), top=16)
    inner += gut(fn('SCOPED TO THIS AFTERNOON · NOT A PREFERENCE, NOT A SETTING', 0), top=16)
    inner += gut(door_list(['The level afternoon', 'Ask the workshop about a lift']), top=24)
    return phone(inner)
def later_visit():
    """Three weeks on, the same person opens the same place alone. The correction does not travel: the stairs are a fact of the building again, not a constraint on them.
    What survives is evidence, not inference: the arrangement they share with Maya, and the building's own access facts."""
    inner = anchor('THE PRINT ROOM', 'SAT 10:20 AM', back=True, sub='Red Hook')
    inner += orientation('Ink and Water, upstairs, from Saturday.', 'A print workshop on Van Brunt Street · three weeks after the last visit', 26, 31)
    inner += gut(photo_plate(150), top=16)
    inner += gut(hours_register([('HOURS', 'Tue&ndash;Sun 11&ndash;6'), ('THE ROOMS', 'Upstairs, by a flight of stairs'), ('TICKETS', 'Not confirmed')]), top=16)
    inner += gut(consequence('FOR SATURDAY', 'The new show is upstairs and Saturday is its first day.'), top=16)
    inner += gut(relationship_trace('You came in March, on the level floor, with your father.', 'ONE VISIT · THE ROOMS NOT SEEN'), top=16)
    inner += sect('Getting there') + gut(arr_two() + horizon_doors([('ACCESS', 'The ferry against the B61: the wait, the crossing, the stairs')]))
    inner += gut(door_list(['Why this, and what it rests on', 'Back to Red Hook']), top=24)
    return phone(inner)
def arr_two():
    return I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot'), (2, 'stairs')], 'PIER 11 · EVERY 40 · THE WAIT DRAWN AT 20'),
                             ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot'), (2, 'stairs')], 'EVERY 12 · TWO BLOCKS · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118)
def unavailable_information():
    """Current information unavailable: the field keeps what it knows, dates it, and does not ask the person to supply it."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'Hours and tides as last seen Thursday · the listings are not reachable right now') + ask()
    body += gut(f'<div style="display: flex; flex-direction: column;">{kick("SATURDAY AT THE PIER · AS LAST SEEN THURSDAY")}{I.pier_line()}<div style="margin-top: 12px;">{serifline("It turns cold fast after sunset; the lawn is nine minutes on, and the film is free if the listing holds.")}</div>{fn("MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo; · NOTHING FRESH SINCE THURSDAY", 8)}<div style="margin-top: 8px;">{doors(("The pier", GOLDD), ("Ask Maya about Saturday", MUTE))}</div></div>', top=24)
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
    inner += gut(I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot'), (2, 'stairs')], 'PIER 11 · EVERY 40 · THE WAIT DRAWN AT 20'), ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot'), (2, 'stairs')], 'EVERY 12 · TWO BLOCKS · THE SAME STAIRS')], origin='FROM CANAL STREET', h=118), top=16)
    inner += gut(consequence('THE DECISIVE FACT', 'The exhibition is upstairs and the listing names no lift. The workshop floor, the crossing and the pier are level; that is the afternoon that serves you both, unless the workshop confirms a lift.'), top=16)
    inner += gut(I.day_band(12, 18, [('13:20', '13:45', '', 'ink'), ('14:00', '15:00', 'THE FLOOR 2–3', 'gold'), ('15:20', '15:45', '', 'ink')], [('17:00', 'BACK BY 5', 'ring')], [('start', 'NOON · 1:20 BOAT OUT', 'start'), ('end', '3:20 BACK', 'end')]), top=16)
    inner += gut(door('Ask the workshop about a lift') + door('The level afternoon: the crossing, the floor, the pier', MUTE), top=8)
    inner += gut(relationship_trace('Maya and Priya wrote about the rooms upstairs.', 'THEIR NOTES, ON THE PLACE'), top=16)
    return phone(inner)
def board():
    r1 = [viewport(col(missing_history(), caption('03.1 · MISSING HISTORY', 'THE WORLD IS FULL', 'The cold start: nothing missing but the person&rsquo;s past; no invitation to supply it'))),
          viewport(col(missing_friends(), caption('03.2 · MISSING FRIENDS', 'A YEAR OF RETURNS, NO ONE IN THE APP', 'The person&rsquo;s own returns are on the places; From friends is absent, not an empty prompt'))),
          viewport(col(shared_supply(), caption('03.3 · BOUNDED SUPPLY, THE PAIR WITH HOME 14', 'NEW YORK, SATURDAY 9:30 · THE SAME SET HOME 14.3 OPENS', 'The same locality, day and hour as Home&rsquo;s third open, with Home&rsquo;s dates: the flea as a place with its own notice, the Open House walk-in sites beside the timed ones that closed Thursday, the L and the tide as getting-around facts, the chapter as the reading'))),
          viewport(col(unavailable_information(), caption('03.4 · UNAVAILABLE INFORMATION', 'NOTHING FRESH SINCE THURSDAY', 'Every hour and tide dated; nothing invented; a door to Maya, not a form')))]
    r2 = [viewport(col(unhurried(), caption('03.5 · ONE AFTERNOON · UNHURRIED', 'THE CROSSING IS THE POINT', 'No times to keep; the rooms if the mood takes; the pier and the pool on the way back'))),
          viewport(col(constrained(), caption('03.6 · THE SAME AFTERNOON · CONSTRAINED', 'WITH YOUR FATHER, BACK BY 5', 'The arrival traced through the entrance to the stairs; the decisive fact leads; the level afternoon that still serves both of you; one honest ask to the workshop'))),
          viewport(col(scoped_correction(), caption('03.7 · A CORRECTION, SCOPED TO TODAY', '&ldquo;THAT WAS FOR MY PARENTS&rdquo; · RECEIVED FROM HOME 14 ROW TWO B', 'The purpose of this afternoon is corrected in the moment: the level afternoon is offered, the stairs are named as today&rsquo;s problem, and the line says the correction is not kept'))),
          viewport(col(later_visit(), caption('03.8 · THREE WEEKS ON, ALONE', 'THE CONSTRAINT DOES NOT TRAVEL', 'The same place, a new show: the stairs are a fact of the building again, not a limit on the person; the record says a visit happened on the level floor, and nothing infers a preference from it'))),
          notecol('Bounded supply, and one afternoon two ways (review, bounded pass 1 and 2)', [
              ('FOUR ABSENCES, TOLD APART', N('Missing history is 01&rsquo;s cold start. Missing friends keeps the person&rsquo;s returns and simply has no From friends section. Bounded supply is now the reconciled pair with Home 14: the same locality, time and source set, rendered place-relative. Unavailable information dates every fact and invents nothing. None of them asks the person for input as the fallback.')),
              ('THE SHARED SUPPLY SET, AS LEDGERED · HOME 14 SELECTS, PLACES RENDERS', tbl(['ITEM', 'SOURCE', 'DATES · EXPIRY', 'UNKNOWN', 'HOME 14', 'PLACES 03.3'], [
                  ['The flea, under the bridge', 'The market&rsquo;s own notice', 'Saturdays through October; today 8 to 3; the bread stall by ten', 'Whether the bread stall holds past ten', '14.2 named, 14.3 and 14.3b the one live thing', 'The place, its hours, directions'],
                  ['Open House New York', 'The OHNY listing', 'Oct 17&ndash;18; timed registration Tuesday noon to Thursday; walk-ins need none', 'Which sites are walk-in this year', '14.1 opens today at noon, 14.2 closes tonight, 14.3 closed Thursday, 14.3b the walk-ins', 'The walk-in sites as places; the timed sites marked closed, with the window that ran'],
                  ['The L', 'MTA', 'After 11 PM Mon&ndash;Thu; daytime normal; end date unknown', 'When the work ends', '14.1, and tonight&rsquo;s last on 14.2', 'A getting-around fact; normal today'],
                  ['Forecast and tide', 'Two stations; the tide table', 'Today clear, 41&deg;; low 2:40 to 5, high 8:40', 'None', 'The reading on all three opens', 'The line under the sentence; the tide as a getting-around fact'],
                  ['The Harbor Book, ch. 4', 'The book', 'No expiry', 'None', '14.1 the card, 14.2 and 14.3 the row', 'The reading, with the section instrument']])),
              ('THE REVISION RACE, RESOLVED', N('For half of September 9 the two projects each moved to the other&rsquo;s set: Home dropped the flea for Red Hook while this project dropped the flea for Home&rsquo;s film and pier. Neither ignored the other; both were reading a version that had already moved. Home&rsquo;s response §18.3 names its current fixture, so this board is drawn on that set and dates every item as Home dates it. Home&rsquo;s one returned correction is applied: the Open House cell above now reads the dated window (opens Tuesday noon, closes Thursday, closed on Saturday, the walk-ins beside it) instead of &ldquo;open until Sunday&rdquo;. The film, the greenmarket, the pierogi table, the Print Room and the 1911 sill stay this project&rsquo;s own material on 01, 03.1 and 08, labelled as independent examples, not as the pair.')),
              ('ONE AFTERNOON, TWO PURPOSES', N('The same place and afternoon. Unhurried: the crossing is the point, no times, the rooms if the mood takes. Constrained, with a parent who does not do stairs and a 5 o&rsquo;clock: the arrival is traced from Canal Street through the wait, the crossing, the level walk and the stairs; the decisive fact leads; the level afternoon that still serves both is offered as the useful alternative, and one honest ask goes to the workshop about a lift. Plans&rsquo; parent-aware response is the donor; this is not a persona and not an accessibility badge.')),
              ('WHAT MOVED', N('03.3 returns to the flea and Open House set, which is what Home 14 draws today; the film and pier version drawn earlier on September 9 is withdrawn. Kingston stays withdrawn. 03.7 and 03.8 are new: Home&rsquo;s scoped help (14 row two B, &ldquo;for tonight, you asked for closer and quieter&rdquo;) received on a place, as a correction of purpose and the visit that follows it three weeks later. No new city, supply system or persona set is added.')),
              ('OPEN', N('Whether the Open House walk-in sites deserve a pocket with a map once the sites are known; drawn as rows. The lift question on 03.6 is a fixture unknown; a live version reads the venue&rsquo;s access listing. Whether a correction like 03.7&rsquo;s should leave any trace at all beyond the visit record on 03.8 is the founder&rsquo;s call; nothing is stored here. Interaction untested.'))], w=760)]
    return rows_page(2560, '03 · THE SITUATIONS · 09-09 · THE PAIR, AND A SCOPED CORRECTION', '03 · The situations', 'Bounded supply: four absences told apart, none answered with an input request, with 03.3 the reconciled pair with Home 14 (same locality, time and source set). Then one afternoon two ways, unhurried and constrained by access and time, and what a correction of purpose does: scoped to the afternoon it was said in, and gone three weeks later.',
                     [('BOUNDED SUPPLY', 'Missing history; missing friends; the pair with Home 14; unavailable information', r1), ('ONE AFTERNOON, AND WHAT A CORRECTION DOES', 'Unhurried; constrained; the correction scoped to today; the same place three weeks on', r2)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/03 - The Situations.dc.html', 'w').write(h); print('wrote 03', len(h))
