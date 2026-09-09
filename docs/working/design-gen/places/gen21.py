"""21 · Three connected journeys, on the chosen terms (§13.6, §14). Ordered static frames; interaction untested."""
from fix import *
from kinds import *
import kinds as K
import instruments as I
Q1 = 'Near Red Hook, Saturday'
def e2(opened=False):
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + ask(q=Q1) + gut(map_block() + burden_strip(), top=12)
    inner += sect('In Red Hook', 24) + gut(redhook_rows(True, opened)) + sect('Getting in') + gut(getting_in())
    inner += gut(body('Everything here is within twelve minutes of the landing on foot.'), top=12) + gut(door_list(['All of New York', 'Sunset Park instead']), top=24)
    return phone(inner)
def e3():
    inner = anchor('RED HOOK', 'SATURDAY', back=True, sub=Q1) + gut(map_block().replace('height="200"', 'height="200"'), top=12) + gut(burden_strip(), top=4)
    inner += gut(redhook_rows(True, facts=False), top=12)
    return phone(inner)
def e4():
    inner = anchor('THE HARBOR PRINT ROOM', '', back=True, sub='Red Hook · Tue–Sun 11–6') + gut(photo_plate(190), top=16)
    inner += gut(title('Rooms Remade, through Sunday', 20, 25, 600) + sup('A print workshop in a former warehouse on Van Brunt Street; the exhibition is in the two upstairs rooms.') + unc(UNK_ROOM), top=12)
    inner += gut(f'<div style="padding-top: 12px; border-top: 1px solid {HAIR7};">' + author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 16, 22) + '</div>', top=12)
    inner += sect('Getting there') + gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN', '9 MIN ON FOOT', '~40') + getting_in())
    inner += gut(door_list(['Reply to Maya', 'Ask Vesper privately']), top=12)
    return phone(inner)
E = [('THE FIELD', 'Friday, as it stands; the first viewport', lambda: field(True), True), ('A QUESTION TYPED', 'The page becomes map-led because orientation was asked for; the burden strip says what the crossing costs', e2, False),
     ('THE MAP', 'The same exploration, larger; the question stays in the header; the four places without their facts', e3, False), ('A RESULT', 'The Print Room: its photo slot, what is unconfirmed, Maya&rsquo;s words, the crossing; two doors, no primary', e4, False),
     ('BACK', 'The question, the four places and the position preserved; the opened one says so', lambda: e2(True), False)]
def h2():
    inner = anchor('FROM FRIENDS', 'THIS WEEK', back=True, sub='Four people') + gut('<div style="margin-top: 6px;">' + share_row('M', 'Maya', 'THURSDAY', MAYA_ROOM, 'THE HARBOR PRINT ROOM · RED HOOK') + share_row('M', 'Maya', 'TUESDAY', MAYA_PIER, 'THE PIER AT SUNSET · KEPT, WITH MAYA') + share_row('P', 'Priya', 'SATURDAY', PRIYA_PIGEONS, 'THE GREENMARKET · DOWNTOWN') + share_row('T', 'Theo', 'TUESDAY', THEO_BREAD, 'THE GREENMARKET · DOWNTOWN') + share_row('S', 'Sam', 'NOT THIS SATURDAY', SAM_HALL, 'THE LISTENING HOUR AT CANAL HALL', last=True) + '</div>', top=12)
    inner += gut(door_list(['All of New York']), top=24)
    return phone(inner)
def h3(sent=False):
    inner = anchor('MAYA', 'THURSDAY', back=True, sub='To friends') + gut(author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 20, 28), top=16)
    inner += gut(place_strip('The Harbor Print Room', 'RED HOOK · TUE–SUN 11–6'), top=12)
    if sent: inner += gut(readback('SENT', 'To Maya · just now · &ldquo;Saturday afternoon, then? I want the side room.&rdquo;'), top=12)
    inner += gut(door_list((['Reply to Maya'] if not sent else []) + ['Ask Vesper privately']), top=8)
    return phone(inner)
def h_reply():
    inner = anchor('MAYA', 'THURSDAY', back=True, sub='To friends') + gut(author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 20, 28), top=16)
    inner += gut(composer('Reply', 'Saturday afternoon, then? I want the side room.', to='TO MAYA'), top=24)
    return phone(inner)
def h_ask(answered=False):
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">ASK VESPER</span><span class="fn" style="margin-left: auto;">PRIVATE</span></div></div>'
    inner += gut(f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="font-size: 13px; color: {INK};">The Harbor Print Room · from Maya&rsquo;s note</span></div>', top=16)
    if answered:
        inner += gut(bubble('is it ticketed? and can I get there by ferry on Saturday?'), top=16)
        inner += gut(answer('Whether Rooms Remade is ticketed hasn&rsquo;t been confirmed; the workshop itself is open Tuesday to Sunday, 11 to 6. The ferry from Pier 11 runs every 40 minutes and takes 25; the Print Room is nine minutes on foot from the landing.'), top=16)
        inner += gut(burden_strip('TO PIER 11', 'THE FERRY · 25 MIN · EVERY 40', '9 MIN ON FOOT', '~40'), top=12) + gut(composer('Ask, or change something'), top=24)
    else: inner += gut(composer('Ask', 'is it ticketed? and can I get there by ferry on Saturday?'), top=24)
    return phone(inner)
Hj = [('THE FIELD', 'The From friends card under the opening', lambda: field(True), True), ('FROM FRIENDS', 'Five lines from four people, each once, under its place', h2, False),
      ('THE ORIGINAL', 'Maya&rsquo;s words as a page; the place; three doors, none required: reply, ask privately, make it Saturday', h3, False), ('BRANCH 1 · BACK', 'Read, and return; nothing sent, nothing required; the field as it was', lambda: field(True), True)]
H2j = [('REPLY, TYPED', 'The composer says who receives it: Maya', h_reply, False), ('SENT', 'The readback on her page; Ask Vesper still available, not required', lambda: h3(True), False), ('BACK', 'The field as it was; one reply sent to Maya; that is this branch&rsquo;s only effect', lambda: field(True), True)]
H3j = [('ASK VESPER, PRIVATELY', 'The header says it is private and what it is about; Maya is not a recipient', lambda: h_ask(False), False), ('THE ANSWER', 'What is unconfirmed, what is known, and the crossing drawn', lambda: h_ask(True), False), ('BACK', 'The field as it was; nothing sent to Maya; that is this branch&rsquo;s only effect', lambda: field(True), True)]
def dinner(sub): return people_row(['M', 'A'], 'Dinner with Maya and Alex', sub)
def band_evening(marks, right='COUNTER TILL 10 · CAFÉ TILL 11', hour_kind='gold'):
    return I.day_band(18, 23, [('19:15', '20:15', 'THE HOUR', hour_kind)], marks, [('start', '6:45 DOORS', 'start'), ('end', right, 'end')])
def hour_unit(extra=''):
    return (title('The listening hour at Canal Hall', 17, 22) + sup('Reich, Music for 18 Musicians, heard whole. Lights down, no talking; doors 6:45.') + fn('SATURDAY 7:15 PM · $12 · CANAL STREET', 4) + extra)
MSG = 'There&rsquo;s a listening hour at Canal Hall on Saturday at 7:15 that I&rsquo;d like to hear whole; it ends about 8:15. Could we make dinner 8:45? I&rsquo;d come straight from the hall.'
def p1():
    """The possibility, with the decisive constraint on the surface: seats are not confirmed. Nothing moves until they are."""
    inner = anchor('NEW YORK', 'FRIDAY 5:40 PM') + ask(q='Saturday evening', ctx='Around dinner') + gut(dinner('Saturday 8:15 · the noodle counter · yours'), top=12)
    inner += sect('Before dinner') + gut(band_evening([('20:15', 'DINNER 8:15', 'ring')], hour_kind='faint') + hour_unit(unc('Seats for Saturday aren&rsquo;t confirmed; the hall posts them at 5.') + sup('Heard whole, it ends when your table begins; dinner would be about 8:45.')) + door('Check seats, then ask about 8:45') + door('Keep dinner at 8:15 and skip the hour', MUTE))
    inner += sect('Instead') + gut('<div>' + film_row() + '</div>') + gut(door_list(['All of Saturday', 'All of New York']), top=24)
    return phone(inner)
def p2():
    """The conditional step: seats first. The rearrangement is not offered as ready until the hour is."""
    inner = anchor('THE HOUR, SATURDAY', 'FRIDAY 5:40 PM', back=True, sub='Canal Hall')
    inner += gut(K.hours_register([('SEATS', 'Posted by the hall at 5 PM Friday; not yet'), ('DOORS', '6:45; about an hour, ends 8:15'), ('YOUR TABLE', '8:15 at the noodle counter, three minutes away')]), top=16)
    inner += gut(K.consequence('WHAT DEPENDS ON WHAT', 'If there are seats, dinner would move to about 8:45 and Maya and Alex would be asked. If not, dinner stays at 8:15 and the hour plays again next Saturday.'), top=16)
    inner += gut(readback('WAITING', 'Seats not posted yet · you&rsquo;ll hear here and on Home when they are'), top=16)
    inner += gut(door_list(['Back to Saturday evening']), top=24)
    return phone(inner)
def p3():
    """Seats confirmed at 5:10. The proposal, now grounded; asking is the primary; the dinner is unchanged until answered."""
    inner = anchor('THE HOUR, SATURDAY', 'FRIDAY 5:12 PM', back=True, sub='Canal Hall')
    inner += gut(readback('SEATS', 'Posted 5:10 PM · seats left for Saturday · $12 at the door'), top=16)
    inner += gut(band_evening([('20:45', 'DINNER 8:45?', 'ring')]), top=12)
    inner += gut(card(f'<div class="kickm">TO MAYA AND ALEX · NOT SENT</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">{MSG}</div>'), top=16)
    inner += gut(door('Ask Maya and Alex about 8:45') + door('Change the wording', MUTE) + door('Leave dinner at 8:15', MUTE), top=8)
    return phone(inner)
def p4():
    """Sent, answered, moved: one page, three lines of state, because the person acts once. Notified appears only after the move."""
    inner = anchor('MOVE DINNER?', 'FRIDAY 2:10 PM', back=True, sub='With Maya and Alex')
    inner += gut(readback('SENT', 'Asked Maya and Alex about 8:45 · Friday 12:34 PM'), top=16)
    inner += gut(card(author_row('M', 'Maya', '2:04 PM') + quote('8:45 is fine for both of us. Alex says he&rsquo;ll be hungry either way.', 17, 24)), top=12)
    inner += gut(band_evening([('20:45', 'DINNER 8:45', 'ring')]), top=12)
    inner += gut(door('Move dinner to 8:45') + door('Leave it at 8:15', MUTE), top=8)
    inner += gut(readback('MOVED', 'Dinner · Saturday 8:45 · the noodle counter · Maya and Alex notified · 2:10 PM'), top=16)
    inner += gut(door_list(['Back to Saturday evening']), top=16)
    return phone(inner)
def p5():
    """Saturday 5:50: last orders at 9. The evening is re-read whole. The existing dinner is preserved as an option; the café is offered only as what it is: open late, a table for three not held."""
    inner = anchor('NEW YORK', 'SATURDAY 5:50 PM') + ask(q='Saturday evening', ctx='Around dinner') + gut(dinner('Saturday 8:45 · the noodle counter · Maya and Alex notified'), top=12)
    changed = (f'<div class="kickm" style="color: {OX};">CHANGED · 5:40 PM</div>' + f'<div style="margin-top: 6px;">{title("The noodle counter stops taking orders at 9 tonight", 20, 25, 600)}</div>' + fn('FROM THE COUNTER&rsquo;S OWN LISTING · POSTED 5:40 PM', 6)
               + band_evening([('20:45', 'DINNER 8:45', 'ring'), ('21:00', '', 'dot')], right='LAST ORDERS 9 · CAFÉ TILL 11')
               + K.consequence('WHAT THIS CHANGES', 'Arriving at 8:45 leaves fifteen minutes to order. The evening still works if you order the moment you sit; it does not if the hour runs long.')
               + f'<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid {HAIR7};">{title("Three honest ways", 16, 21, 600)}</div><div>' + prow('Keep 8:45 at the counter, order on arrival', 'YOUR DINNER AS ARRANGED · MAYA AND ALEX NEED NOTHING NEW', first=True) + prow('Leave the hour at 8:15 and keep dinner as it was', 'THE HOUR PLAYS AGAIN NEXT SATURDAY') + prow('The long table at the caf&eacute;', 'OPEN TILL 11 · NO TABLES HELD · A TABLE FOR THREE ISN&rsquo;T CONFIRMED · ASK BEFORE MOVING', last=True) + '</div>'
               + door('Keep 8:45 at the counter') + door('Ask the caf&eacute; about a table for three', MUTE))
    inner += gut(card(changed), top=12) + sect('Still on tonight') + gut(hour_unit(sup('Doors 6:45; seats confirmed Friday.'))) + sect('Instead') + gut('<div>' + film_row() + '</div>')
    return phone(inner)
def p6():
    """Return: the field reads the current state. The dinner is as arranged; the counter's change is on it; nothing was moved on an unconfirmed table."""
    inner = anchor('NEW YORK', 'SATURDAY 5:52 PM') + ask(q='Saturday evening', ctx='Around dinner')
    inner += gut(dinner('Saturday 8:45 · the noodle counter · order on arrival, last orders 9'), top=12)
    inner += sect('Still on tonight') + gut(band_evening([('20:45', 'DINNER 8:45', 'ring'), ('21:00', '', 'dot')], right='LAST ORDERS 9') + hour_unit(sup('Doors 6:45; it ends about 8:15, three minutes from the counter.')))
    inner += sect('Instead') + gut('<div>' + film_row() + '</div>') + gut(door_list(['All of Saturday', 'All of New York']), top=24)
    return phone(inner)
Pj = [('THE POSSIBILITY', 'The decisive constraint on the surface: seats are not confirmed, so the hour is faint on the band and nothing moves; the existing dinner is a door of its own', p1, False),
      ('SEATS FIRST', 'The conditional step: what depends on what, and a waiting readback; no rearrangement is offered as ready', p2, False),
      ('SEATS CONFIRMED, THE PROPOSAL', 'Grounded now; the message is short and editable; asking is the primary, leaving the dinner is a door', p3, False),
      ('ASKED, ANSWERED, MOVED', 'One page for the person&rsquo;s one act: the send, Maya&rsquo;s words, the move, and notified only after it', p4, False),
      ('CHANGED CIRCUMSTANCES', 'Last orders at 9 as the dot; the evening re-read whole; three honest ways, and the caf&eacute; offered only as what it is: open late, a table not held', p5, False),
      ('RETURN', 'The field reads the current state: dinner as arranged, order on arrival; nothing moved on an unconfirmed table', p6, False)]
def h3(sent=False):
    inner = anchor('MAYA', 'THURSDAY', back=True, sub='To friends') + gut(author_row('M', 'Maya', 'THURSDAY') + quote(MAYA_ROOM, 20, 28), top=16)
    inner += gut(place_strip('The Harbor Print Room', 'RED HOOK · TUE–SUN 11–6'), top=12)
    if sent: inner += gut(readback('SENT', 'To Maya · just now · &ldquo;Saturday afternoon, then? I want the side room.&rdquo;'), top=12)
    inner += gut(door_list((['Reply to Maya'] if not sent else []) + ['Ask Vesper privately', 'Make it Saturday, with Maya']), top=8)
    return phone(inner)
def h_arrange(sent=False):
    """Branch 4: an intentional arrangement from her note, through the arrangement owner's own command: one proposal to Maya, a time, the place; nothing is arranged until she answers."""
    inner = anchor('SATURDAY, WITH MAYA?', 'THURSDAY', back=True, sub='The Harbor Print Room')
    inner += gut(place_strip('The Harbor Print Room', 'RED HOOK · TUE–SUN 11–6 · ROOMS REMADE, TO SUNDAY'), top=16)
    inner += gut(I.day_band(11, 18, [('14:00', '16:00', 'THE ROOMS', 'gold')], [('13:20', 'FERRY 1:20', 'dot')], [('start', 'SATURDAY', 'start'), ('end', 'CLOSES 6', 'end')]), top=12)
    if not sent:
        inner += gut(card(f'<div class="kickm">TO MAYA · NOT SENT</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">Saturday at the Print Room, the 1:20 ferry, two o&rsquo;clock upstairs? I want the side room you wrote about.</div>'), top=16)
        inner += gut(door('Propose Saturday to Maya') + door('Change the wording', MUTE), top=8)
    else:
        inner += gut(readback('PROPOSED', 'To Maya · Saturday 2:00 at the Print Room · not arranged until she answers'), top=16)
        inner += gut(door_list(['Back to Maya&rsquo;s note']), top=16)
    return phone(inner)
H4j = [('MAKE IT SATURDAY, WITH MAYA', 'An intentional arrangement from her note: the place, a time on the band, one short proposal; the arrangement owner&rsquo;s command, not a Places planner', lambda: h_arrange(False), False), ('PROPOSED', '&ldquo;From Maya&rdquo; is her share; &ldquo;with Maya&rdquo; only once she answers; the readback says so', lambda: h_arrange(True), False), ('BACK', 'The field as it was; one proposal out; nothing arranged', lambda: field(True), True)]
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
        ('PRACTICAL CONTINUATION (REVIEW §P8)', N('The chain is complete now. Seats for the hour were unconfirmed, so the possibility shows that as the decisive constraint (the hour faint on the band) and offers a seat check before any rearrangement; the existing dinner is a door of its own at every step. Once seats are posted, the proposal is grounded and short; asking is the primary. The send, Maya&rsquo;s answer and the move share one page because the person acts once; notified appears only after the move. On Saturday the change is re-read against the whole evening: 8:45 leaves fifteen minutes to order, so three honest ways are offered, and the caf&eacute; is described as what it is, open late with no table for three confirmed, never as a workable dinner. The person keeps the counter; nothing moves on an unconfirmed table.'))], w=640),
        notecol('What is current at the end; what is not exercised', [
        ('AT THE END', tbl(['JOURNEY', 'CURRENT AT THE END', 'TAPS'], [['Exploration', 'The field with &ldquo;Near Red Hook, Saturday&rdquo; still in it, the Print Room marked as opened; nothing kept, nothing sent', 'One question typed, two taps in, two back'], ['Human receiving, branch 1', 'The field unchanged; nothing sent', 'Two taps in, two back'], ['Human receiving, branch 2', 'One reply sent to Maya; the field unchanged', 'Two taps in, one Send, two back'], ['Human receiving, branch 3', 'One private question answered; nothing sent to Maya; the field unchanged', 'Two taps in, one question, two back'], ['Human receiving, branch 4', 'One proposal to Maya for Saturday 2:00; nothing arranged until she answers', 'Two taps in, one Send, one back'], ['Practical continuation', 'One dinner: Saturday 8:45 at the noodle counter, order on arrival; Maya and Alex notified once; the hour with seats confirmed; the film still an evening instead', 'One seat check, one ask, one Send, one move; nothing moved after the change']])),
        ('NOT EXERCISED', N('Every transition is an ordered static frame. No target, no Send and no Back were exercised as a connected interaction; nothing here verifies restoration on a device.')),
        ('OWNER DEPENDENCIES', N('The arrangement owner for the dinner (organizer command, shared readback, notification) and for a person&rsquo;s share payload; a sender for a message to a named person; a private question line that is not a message. None exists as drawn; nothing here authorizes them. The five situations of §8 remain in view; these three paths do not reduce Places to one loop.'))], w=760)]
    return rows_page(3130, '21 · THREE CONNECTED JOURNEYS · ORDERED FRAMES · 09-07 (§13.6, §14)', '21 · Three connected journeys, on the chosen terms',
                     'Exploration: field, a question, the map, a result, back. Human receiving: From friends, the original, then three independent branches: read and return; reply to Maya; ask Vesper privately. Practical continuation: a possibility around a dinner, the proposed change with its constraint on the day band, the readback, the organizer&rsquo;s move, a changed circumstance, return. Each frame is a rendered static state in the language of 19; the taps between them are the doors visible on the frame before. Interaction is untested.',
                     [('EXPLORATION', 'Field, question, map, result, back', frames(E, 'E')), ('HUMAN RECEIVING', 'From friends, the original; branch 1: read and return', frames(Hj, 'H')), ('HUMAN RECEIVING · BRANCH 2', 'Reply to Maya, the readback, return', frames(H2j, 'H2.')), ('HUMAN RECEIVING · BRANCH 3', 'Ask Vesper privately, the answer, return', frames(H3j, 'H3.')), ('HUMAN RECEIVING · BRANCH 4', 'An intentional arrangement, through the owner', frames(H4j, 'H4.')), ('PRACTICAL CONTINUATION', 'A possibility around a dinner; seats first, then asked, answered and moved; changed; returned', frames(Pj, 'P')), ('NOTES', 'What each journey shows; what is current at the end; what is not exercised; the owner dependencies', notes)], 7000)
if __name__ == '__main__':
    import os; os.makedirs('out', exist_ok=True); h = board(); open('out/21 - Three Connected Journeys.dc.html', 'w').write(h); print('wrote 21', len(h))
