"""09 · Purposes (review §P1, §P4, §P10): the same city and day, four current purposes. Present purpose, relevant context and available evidence change selection, emphasis and depth;
history earns its place by improving the result, not by being displayed. Replaces the fixed-stage rule of the earlier 09."""
from fix import *
from kinds import returned_understanding, consequence
import instruments as I
import gen19v3 as g
def field_a():
    """A little context improves a possibility: one kept place, nothing else known. The keeping changes one line: the pier leads because it is worthwhile and kept; the film follows."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The pier at sunset, then the film on the lawn. Saturday.', 'Kept Tuesday · Sunset Park') + ask()
    body += gut(f'<div style="display: flex; flex-direction: column;">{kick("SATURDAY AT THE PIER · KEPT TUESDAY")}{I.pier_line()}<div style="margin-top: 12px;">{serifline("It turns cold fast after sunset; the lawn is nine minutes on, and the film is free if the listing holds.")}</div>{fn("YOU KEPT THIS ON TUESDAY", 8)}<div style="margin-top: 8px;">{doors(("The pier", GOLDD))}</div></div>', top=24)
    body += sect('Any day') + gut(browse_shelf(g.SHELF)) + g.redhook(False) + g.evening(False) + g.understanding() + g.sunday(False) + g.morning(False) + gut(door_list(['Another neighborhood', 'Sunday, all day']), top=24)
    return phone(body)
def field_b():
    """Accumulated context reduces effort: the person has been to the counter and the hall; the field skips the introduction it no longer needs and leads with the practical fact that matters tonight."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('The hour at Canal Hall, then the counter. Saturday.', 'Seats posted at 5 · your usual table is three minutes on · the pier first if the light holds') + ask()
    unit = (kick('SATURDAY EVENING · THE PART YOU KNOW IS SKIPPED') + I.day_band(18, 23, [('19:15', '20:15', 'THE HOUR', 'gold')], [('20:45', 'THE COUNTER 8:45', 'ring')], [('start', '6:45 DOORS', 'start'), ('end', 'LAST ORDERS 10', 'end')])
            + f'<div style="margin-top: 12px;">{serifline("Seats for the hour are posted at 5. The counter holds no tables; at 8:45 you order on arrival, as you did in August.")}</div>' + fn('YOU, AT THE HALL IN MARCH · AT THE COUNTER TWICE IN AUGUST', 8) + f'<div style="margin-top: 8px;">{doors(("Check seats at 5", GOLDD), ("Your last evening here", MUTE))}</div>')
    body += gut(f'<div style="display: flex; flex-direction: column;">{unit}</div>', top=24)
    body += sect('Any day') + gut(browse_shelf(g.SHELF)) + g.redhook(False) + g.understanding() + g.sunday(False) + g.morning(False) + gut(door_list(['Another neighborhood', 'Sunday, all day']), top=24)
    return phone(body)
def field_c():
    """A friend's contribution changes what becomes possible: Maya's share makes the pier a shared Saturday, not only a place; the door is to her, and From friends leads."""
    return g.v3(True)
def field_d():
    """History is irrelevant: a year of visits, but tonight's purpose is a first: Red Hook by ferry, never done. The field leads with the crossing and says nothing about the year."""
    body = anchor('NEW YORK', 'FRIDAY 5:40 PM') + orientation('Red Hook by ferry, Saturday or Sunday.', 'Twenty-five minutes across from Pier 11 · four places within twelve minutes of the landing · the Print Room to Sunday') + ask(q='Red Hook, this weekend')
    body += gut(REDHOOK_MAP + I.access_compare([('BY FERRY', [(6, 'foot'), (20, 'wait'), (25, 'ride'), (9, 'foot')], 'PIER 11 · WAIT UP TO 40 · LEVEL TO THE LANDING'), ('BY THE B61', [(4, 'foot'), (6, 'wait'), (28, 'ride'), (3, 'foot')], 'EVERY 12 · TWO BLOCKS')], origin='FROM CANAL STREET', h=112) + '<div style="margin-top: 4px;">' + redhook_rows(True) + '</div>', top=24)
    body += sect('Saturday evening') + g.evening(True).replace(sect('Saturday evening'), '', 1) + g.understanding() + gut(door_list(['All of New York', 'Sunday, all day', 'From friends, everything']), top=24)
    return phone(body)
def board():
    caps = [('09.1 · A LITTLE CONTEXT', 'ONE KEPT PLACE, NOTHING ELSE KNOWN', 'The keeping changes one line: the pier leads because it is worthwhile and kept; one door, to the pier; the rest of the field is the world&rsquo;s'),
            ('09.2 · ACCUMULATED CONTEXT', 'THE INTRODUCTION IS SKIPPED', 'The person has been to the hall and the counter; the field leads with the fact that matters tonight (seats at 5, order on arrival) and drops the pitch; one door to the last evening&rsquo;s record in Life'),
            ('09.3 · A FRIEND&rsquo;S CONTRIBUTION', 'THE CURRENT 01', 'Maya&rsquo;s share makes the pier a possible Saturday with her, not only a place; From friends leads the second screen; the doors are to her'),
            ('09.4 · HISTORY IRRELEVANT', 'A YEAR OF VISITS; A FIRST CROSSING', 'Tonight&rsquo;s purpose is new, so the year says nothing; the crossing leads with its whole arrival, waiting drawn apart from movement; the same excellent public answer a newcomer would get')]
    cols = [viewport(col(f(), caption(*c))) for f, c in zip((field_a, field_b, field_c, field_d), caps)]
    delta = tbl(['', 'A LITTLE CONTEXT', 'ACCUMULATED CONTEXT', 'A FRIEND&rsquo;S CONTRIBUTION', 'HISTORY IRRELEVANT'], [
        ['What leads', 'The kept pier, because it is worthwhile', 'The practical fact for tonight; the introduction is skipped', 'Her share; the pier as a Saturday with her', 'The crossing, whole, with its wait'],
        ['What context adds', 'One line: kept Tuesday', 'Two facts the person already learned, applied, not displayed', 'Her words, and a door to her', 'Nothing; a year of visits is silent'],
        ['What is dropped', 'Nothing', 'The pitch for places already known; the shelf stays for the rest', 'Nothing', 'The opening sentence about the pier; the shelf'],
        ['Doors', 'The pier', 'Check seats; your last evening here, in Life', 'The pier; reply to Maya', 'All of New York; Sunday; friends'],
        ['Depth kept', 'Everything below', 'Everything below', 'Everything below', 'The evening, the comparison, the reading']])
    notes = [notecol('The rule, revised (review §P1, §P10, §P4)', [('THE RULE', N('Keep a recognisable visual and interaction grammar. Let present purpose, relevant context and available evidence change selection, emphasis and depth. History earns its place by improving the result, not by being displayed. The four columns are a controlled comparison on one city and one day, not engagement levels: someone can have a year of history, no friends in the app and infrequent use, and the same excellent public answer can be right for the newcomer and the long-term user.')),
                      ('WHAT CHANGED FROM THE STAGES BOARD', N('The earlier 09 held the composition fixed and let stages add visit counts. That rule is withdrawn as a universal; it survives only as the observation that the grammar stays recognisable. Column 2 now skips an introduction because the person has learned it; column 4 shows a year of history saying nothing because the purpose is new. A door to the exact Life record is allowed where it recovers an earlier encounter (column 2); Places is still not the archive.')),
                      ('OPEN', N('Column 2&rsquo;s skipped introduction is a judgment about what the person has learned, not a rule about visit counts; the threshold is not drawn. Lightweight steering (&ldquo;closer, and somewhere we can talk&rdquo;) is carried by the existing Ask and is drawn on 02, not here. Interaction untested.'))], w=1700)]
    return rows_page(2560, '09 · PURPOSES · 09-08 · REVIEW P1, P4, P10', '09 · Purposes', 'The same city and the same Friday, four current purposes: a little context improves a possibility; accumulated context reduces effort; a friend&rsquo;s contribution changes what becomes possible; history is irrelevant. Replaces the fixed-stage rule.',
                     [('ONE CITY, ONE DAY, FOUR PURPOSES', 'What leads, what context adds, what is dropped', cols), ('THE DELTAS', '', [f'<div style="width: 1700px;">{delta}</div>']), ('NOTES', '', notes)], 9000)
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/09 - Purposes.dc.html', 'w').write(h); print('wrote 09', len(h))
