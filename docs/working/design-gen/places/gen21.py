"""21 · Three connected journeys, on the chosen terms (§13.6, §14). Ordered static frames; interaction untested."""
from fix import *
import instruments as I
Q1 = 'Near Red Hook, Saturday'
def e2(opened=False):
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + ask(q=Q1) + gut(map_block() + burden_strip(), top=14)
    inner += sect('In Red Hook', 22) + gut(redhook_rows(True, opened)) + sect('Getting in') + gut(getting_in())
    inner += gut(body('Everything here is within twelve minutes of the landing on foot.'), top=14) + gut(door_list(['All of New York', 'Sunset Park instead']), top=24)
    return phone(inner)
def e3():
    inner = anchor('RED HOOK', 'SATURDAY', back=True, sub=Q1) + gut(map_block().replace('height="200"', 'height="200"'), top=14) + gut(burden_strip(), top=4)
    inner += gut(redhook_rows(True, facts=False), top=10)
    return phone(inner)
def e4():
    inner = anchor('THE HARBOR PRINT ROOM', '', back=True, sub='Red Hook · Tue–Sun 11–6') + gut(photo_plate(190), top=18)
    inner += gut(title('Rooms Remade, through Sunday', 20, 25, 600) + sup('A print workshop in a former warehouse on Van Brunt Street; the exhibition is in the two upstairs rooms.') + unc(UNK_ROOM), top=14)
    inner += gut(f'<div style="padding-top: 12px; border-top: 1px solid {HAIR7};">' + author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 16, 22) + '</div>', top=14)
    inner += sect('Getting there') + gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN', '9 MIN ON FOOT', '~40') + getting_in())
    inner += gut(door_list(['Reply to Maya', 'Ask Vesper privately']), top=14)
    return phone(inner)
E = [('THE FIELD', 'Friday, as it stands; the first viewport', lambda: field(True), True), ('A QUESTION TYPED', 'The page becomes map-led because orientation was asked for; the burden strip says what the crossing costs', e2, False),
     ('THE MAP', 'The same exploration, larger; the question stays in the header; the four places without their facts', e3, False), ('A RESULT', 'The Print Room: its photo slot, what is unconfirmed, Maya&rsquo;s words, the crossing; two doors, no primary', e4, False),
     ('BACK', 'The question, the four places and the position preserved; the opened one says so', lambda: e2(True), False)]
def h2():
    inner = anchor('FROM FRIENDS', 'THIS WEEK', back=True, sub='Four people') + gut('<div style="margin-top: 6px;">' + share_row('M', 'Maya', 'THURSDAY', MAYA_ROOM, 'THE HARBOR PRINT ROOM · RED HOOK') + share_row('M', 'Maya', 'TUESDAY', MAYA_PIER, 'THE PIER AT SUNSET · KEPT, WITH MAYA') + share_row('P', 'Priya', 'SATURDAY', PRIYA_PIGEONS, 'THE GREENMARKET · DOWNTOWN') + share_row('T', 'Theo', 'TUESDAY', THEO_BREAD, 'THE GREENMARKET · DOWNTOWN') + share_row('S', 'Sam', 'NOT THIS SATURDAY', SAM_HALL, 'THE LISTENING HOUR AT CANAL HALL', last=True) + '</div>', top=10)
    inner += gut(door_list(['All of New York']), top=20)
    return phone(inner)
def h3(sent=False):
    inner = anchor('MAYA', 'THURSDAY', back=True, sub='To friends') + gut(author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 20, 28), top=18)
    inner += gut(place_strip('The Harbor Print Room', 'RED HOOK · TUE–SUN 11–6'), top=10)
    if sent: inner += gut(readback('SENT', 'To Maya · just now · &ldquo;Saturday afternoon, then? I want the side room.&rdquo;'), top=14)
    inner += gut(door_list((['Reply to Maya'] if not sent else []) + ['Ask Vesper privately']), top=8)
    return phone(inner)
def h_reply():
    inner = anchor('MAYA', 'THURSDAY', back=True, sub='To friends') + gut(author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 20, 28), top=18)
    inner += gut(composer('Reply', 'Saturday afternoon, then? I want the side room.', to='TO MAYA'), top=22)
    return phone(inner)
def h_ask(answered=False):
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">ASK VESPER</span><span class="fn" style="margin-left: auto;">PRIVATE</span></div></div>'
    inner += gut(f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="font-size: 13px; color: {INK};">The Harbor Print Room · from Maya&rsquo;s note</span></div>', top=18)
    if answered:
        inner += gut(bubble('is it ticketed? and can I get there by ferry on Saturday?'), top=18)
        inner += gut(answer('Whether Rooms Remade is ticketed hasn&rsquo;t been confirmed; the workshop itself is open Tuesday to Sunday, 11 to 6. The ferry from Pier 11 runs every 40 minutes and takes 25; the Print Room is nine minutes on foot from the landing.'), top=16)
        inner += gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN · EVERY 40', '9 MIN ON FOOT', '~40'), top=10) + gut(composer('Ask, or change something'), top=22)
    else: inner += gut(composer('Ask', 'is it ticketed? and can I get there by ferry on Saturday?'), top=22)
    return phone(inner)
Hj = [('THE FIELD', 'The From friends card under the opening', lambda: field(True), True), ('FROM FRIENDS', 'Five lines from four people, each once, under its place', h2, False),
      ('THE ORIGINAL', 'Maya&rsquo;s words as a page; the place; two doors, neither required', h3, False), ('BRANCH 1 · BACK', 'Read, and return; nothing sent, nothing required; the field as it was', lambda: field(True), True)]
H2j = [('REPLY, TYPED', 'The composer says who receives it: Maya', h_reply, False), ('SENT', 'The readback on her page; Ask Vesper still available, not required', lambda: h3(True), False), ('BACK', 'The field as it was; one reply sent to Maya; that is this branch&rsquo;s only effect', lambda: field(True), True)]
H3j = [('ASK VESPER, PRIVATELY', 'The header says it is private and what it is about; Maya is not a recipient', lambda: h_ask(False), False), ('THE ANSWER', 'What is unconfirmed, what is known, and the crossing drawn', lambda: h_ask(True), False), ('BACK', 'The field as it was; nothing sent to Maya; that is this branch&rsquo;s only effect', lambda: field(True), True)]
def dinner(sub): return people_row(['M', 'A'], 'Dinner with Maya and Alex', sub)
def band_evening(dinner_t, dinner_lab, extra_marks=(), right='COUNTER TILL 10 · CAFÉ TILL 11'):
    return I.day_band(18, 23, [('19:15', '20:15', 'THE HOUR', 'gold')], [(dinner_t, dinner_lab, 'ring')] + list(extra_marks), [('start', '6:45 DOORS', 'start'), ('end', right, 'end')])
MSG = 'There&rsquo;s a listening hour at Canal Hall on Saturday at 7:15, Reich&rsquo;s Music for 18 Musicians, that I&rsquo;d like to hear whole. Could we make dinner 8:45 instead of 8:15? I&rsquo;d come straight from the hall; it&rsquo;s three minutes.'
def p1():
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + ask(q='Saturday evening', ctx='Around dinner') + gut(dinner('Saturday 8:15 · the noodle counter · yours'), top=14)
    inner += sect('Before dinner') + gut(band_evening('20:15', 'DINNER 8:15') + hour_unit(sup('Ends about 8:15, when your table is. Heard whole, dinner would be about 8:45.')) + door('Hear it whole, dinner at 8:45'))
    inner += sect('Instead') + gut('<div>' + film_row() + '</div>') + gut(door_list(['All of Saturday', 'All of New York']), top=24)
    return phone(inner)
def p2():
    inner = anchor('MOVE DINNER?', 'SATURDAY', back=True, sub='With Maya and Alex') + gut(dinner('Saturday 8:15 · the noodle counter · yours'), top=18)
    inner += gut(title('Dinner at about 8:45, to hear the hour whole', 20, 25, 600) + sup('The hour ends about 8:15. The counter is three minutes from the hall, open till 10, and doesn&rsquo;t hold tables; 8:45 is an arrival, not a booking.') + band_evening('20:45', 'DINNER 8:45'), top=16)
    inner += gut(card(f'<div class="kickm">TO MAYA AND ALEX · NOT SENT</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">{MSG}</div>'), top=16)
    inner += gut(door('Ask Maya and Alex about 8:45') + door('Change the wording', MUTE), top=8)
    return phone(inner)
def p3():
    inner = anchor('MOVE DINNER?', 'SATURDAY', back=True, sub='With Maya and Alex') + gut(dinner('Saturday 8:15 · the noodle counter · yours'), top=18)
    inner += gut(readback('SENT', 'Asked Maya and Alex about 8:45 · Friday 12:34 PM · no answer yet'), top=16) + gut(body('Dinner is still Saturday 8:15.'), top=12)
    inner += gut(door_list(['Back to Saturday evening', 'The hour, at Canal Hall']), top=6)
    return phone(inner)
def p4():
    inner = anchor('MOVE DINNER?', 'SATURDAY', back=True, sub='With Maya and Alex') + gut(dinner('Saturday 8:15 · the noodle counter · yours'), top=18)
    inner += gut(card(author_row('M', 'Maya', '2:04 PM') + quote('8:45 is fine for both of us. Alex says he&rsquo;ll be hungry either way.', 17, 24)), top=16)
    inner += gut(door('Move dinner to 8:45') + door('Leave it at 8:15', MUTE), top=10)
    return phone(inner)
def p5():
    inner = anchor('MOVE DINNER?', 'SATURDAY', back=True, sub='With Maya and Alex') + gut(readback('MOVED', 'Dinner · Saturday 8:45 · the noodle counter · Maya and Alex notified · 2:10 PM'), top=18)
    inner += gut(dinner('Saturday 8:45 · the noodle counter · yours'), top=12) + gut(band_evening('20:45', 'DINNER 8:45'), top=10) + gut(door_list(['Back to Saturday evening']), top=8)
    return phone(inner)
def p6():
    inner = anchor('NEW YORK', 'SATURDAY 5:50 PM') + ask(q='Saturday evening', ctx='Around dinner') + gut(dinner('Saturday 8:45 · the noodle counter · Maya and Alex notified'), top=14)
    changed = (f'<div class="kickm" style="color: {OX};">CHANGED · 5:40 PM</div>' + f'<div style="margin-top: 6px;">{title("The noodle counter stops taking orders at 9 tonight", 20, 25, 600)}</div>' + sup('An 8:45 arrival leaves fifteen minutes to order.') + fn('FROM THE COUNTER&rsquo;S OWN LISTING · POSTED 5:40 PM', 6)
               + band_evening('20:45', 'DINNER 8:45', [('21:00', '', 'dot')], right='LAST ORDERS 9 · CAFÉ TILL 11')
               + f'<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid {HAIR7};">{title("Where else at 8:45", 16, 21, 600)}</div><div>' + prow('The long table at the caf&eacute;', 'OPEN TILL 11 · FOUR MINUTES FROM THE HALL · NO TABLES HELD', first=True, last=True) + '</div>'
               + door('Move dinner to the caf&eacute;, and tell Maya and Alex') + door('Keep 8:45 at the counter', MUTE))
    inner += gut(card(changed), top=14) + sect('Still on tonight') + gut(hour_unit(sup('Doors 6:45.'))) + sect('Instead') + gut('<div>' + film_row() + '</div>')
    return phone(inner)
def p7():
    inner = anchor('NEW YORK', 'SATURDAY 5:52 PM') + ask(q='Saturday evening', ctx='Around dinner') + gut(readback('MOVED', 'Dinner · Saturday 8:45 · the long table at the caf&eacute; · Maya and Alex notified · 5:52 PM'), top=14)
    inner += gut(dinner('Saturday 8:45 · the long table · no tables held'), top=10) + sect('Still on tonight') + gut(band_evening('20:45', 'DINNER 8:45') + hour_unit(sup('Doors 6:45; the caf&eacute; is four minutes after.')))
    inner += sect('Instead') + gut('<div>' + film_row() + '</div>') + gut(door_list(['All of Saturday', 'All of New York']), top=24)
    return phone(inner)
Pj = [('THE POSSIBILITY', 'Saturday evening around an existing dinner; the day band shows the hour ending where the table begins; the film is an evening instead', p1, False),
      ('THE PROPOSED CHANGE', 'Dinner at about 8:45, with the constraint on the band: the hour, the walk, no tables held; one prepared message; asking is the primary', p2, False),
      ('SENT', 'Asked, when, no answer; dinner still 8:15', p3, False), ('AN ANSWER', 'Maya&rsquo;s words; the move is the person&rsquo;s, as organizer', p4, False),
      ('MOVED', 'One dinner at 8:45 on the band; Maya and Alex notified, an effect that has occurred in the fixture', p5, False), ('CHANGED CIRCUMSTANCES', 'Saturday 5:50: last orders at 9 as a dot on the band; fifteen minutes is tight; one alternative, and the dinner can stay', p6, False),
      ('RETURN', 'The field reads the current state: 8:45 at the caf&eacute;, people notified, no tables held; the film still an evening instead', p7, False)]
def frames(js, prefix):
    out = []
    for i, (k, t, fnc, vp) in enumerate(js):
        c = col(fnc(), caption(f'{prefix}{i+1} · {k}', '', t), clip=1000 if vp else None)
        out.append(viewport(c) if vp else c)
    return out
def board():
    notes = [notecol('What each journey shows (§13.6, §14)', [
        ('EXPLORATION', N('Field and map are expressions of the same exploration: the question typed into the field makes the page map-led, the burden strip says what the crossing costs door to door, the map page carries the same four places and the same question, the result page carries the place and Maya&rsquo;s words with two doors and no primary, and Back preserves the question, the four places and the position, marking the one opened. The map&rsquo;s geometry is illustrative, not routing. Five frames; no target exercised.')),
        ('HUMAN RECEIVING', N('From friends is a list of people&rsquo;s own words, once each, under the place each concerns. The original is enjoyed as itself; the two continuations are doors, independent, and neither is prerequisite to the other (§14.4). Branch 1 reads and returns with nothing sent. Branch 2 replies to Maya: the composer names her, the readback sits on her page, the field is unchanged. Branch 3 asks Vesper privately: the header says it is private and what it is about; the answer draws the crossing; Maya is never a recipient. No combined completion state is drawn. The requirements live here, not in the phone (§14.3).')),
        ('PRACTICAL CONTINUATION', N('Why 8:45 and not 9:30 (§14.2): the hour ends about 8:15, leaving with the crowd takes a few minutes, the counter is three minutes away and holds no tables, so 8:45 is an arrival with a margin, not a booking. The day band carries that: the hour as the gold block, dinner as the ring after it, last orders as the dot at 9 on Saturday. The film in Sunset Park is forty minutes from Canal Street and is an evening instead, labelled so at every frame. Asking is the primary on the possibility; the move is the organizer&rsquo;s own action after an answer; &ldquo;notified&rdquo; appears only after the move. The person can move to the caf&eacute; or keep the counter; the field then reads the current state.'))], w=640),
        notecol('What is current at the end; what is not exercised', [
        ('AT THE END', tbl(['JOURNEY', 'CURRENT AT THE END', 'TAPS'], [['Exploration', 'The field with &ldquo;Near Red Hook, Saturday&rdquo; still in it, the Print Room marked as opened; nothing kept, nothing sent', 'One question typed, two taps in, two back'], ['Human receiving, branch 1', 'The field unchanged; nothing sent', 'Two taps in, two back'], ['Human receiving, branch 2', 'One reply sent to Maya; the field unchanged', 'Two taps in, one Send, two back'], ['Human receiving, branch 3', 'One private question answered; nothing sent to Maya; the field unchanged', 'Two taps in, one question, two back'], ['Practical continuation', 'One dinner: Saturday 8:45 at the long table; Maya and Alex notified twice; no tables held; the hour untouched; the film still an evening instead', 'One ask, one Send, one move, one move again after the change']])),
        ('NOT EXERCISED', N('Every transition is an ordered static frame. No target, no Send and no Back were exercised as a connected interaction; nothing here verifies restoration on a device.')),
        ('OWNER DEPENDENCIES', N('The arrangement owner for the dinner (organizer command, shared readback, notification) and for a person&rsquo;s share payload; a sender for a message to a named person; a private question line that is not a message. None exists as drawn; nothing here authorizes them. The five situations of §8 remain in view; these three paths do not reduce Places to one loop.'))], w=760)]
    return rows_page(3130, '21 · THREE CONNECTED JOURNEYS · ORDERED FRAMES · 09-07 (§13.6, §14)', '21 · Three connected journeys, on the chosen terms',
                     'Exploration: field, a question, the map, a result, back. Human receiving: From friends, the original, then three independent branches: read and return; reply to Maya; ask Vesper privately. Practical continuation: a possibility around a dinner, the proposed change with its constraint on the day band, the readback, the organizer&rsquo;s move, a changed circumstance, return. Each frame is a rendered static state in the language of 19; the taps between them are the doors visible on the frame before. Interaction is untested.',
                     [('EXPLORATION', 'Field, question, map, result, back', frames(E, 'E')), ('HUMAN RECEIVING', 'From friends, the original; branch 1: read and return', frames(Hj, 'H')), ('HUMAN RECEIVING · BRANCH 2', 'Reply to Maya, the readback, return', frames(H2j, 'H2.')), ('HUMAN RECEIVING · BRANCH 3', 'Ask Vesper privately, the answer, return', frames(H3j, 'H3.')), ('PRACTICAL CONTINUATION', 'A possibility around a dinner; asked, answered, moved, changed, returned', frames(Pj, 'P')), ('NOTES', 'What each journey shows; what is current at the end; what is not exercised; the owner dependencies', notes)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out', exist_ok=True); h = board(); open('out/21 - Three Connected Journeys.dc.html', 'w').write(h); print('wrote 21', len(h))
