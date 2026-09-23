"""06 - E · revised (§8.8): a coherent baseline (the hour runs 7–9 and is meant to be heard whole; the table is 8:15), an
honest answer that protects the experience, one preparation with a named recipient and a deliberate send, compact readback,
a useful return; then one genuine change and the smallest decision it leaves. One chosen lens inside the phone."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N, arow, facepile
from gen_generous3 import sect, title, sup, gut, card, fact
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_p2_02 import u_hour, u_noodles, u_library, u_table, u_pier
from gen_p2_03 import b_scroll

P = PACKET
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
def answer(html):
    return f'<div style="max-width: 336px; {SERIF} font-size: 17px; line-height: 24px; color: {INK};">{html}</div>'
def ctx_line(t):
    return f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="font-size: 13px; color: {INK};">{t}</span></div>'

def chat_phone():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">FRIDAY 12:31 PM</span></div></div>')
    inner += gut(ctx_line('The listening hour &middot; Saturday 7&ndash;9 &middot; from Places'), top=22)
    inner += gut(bubble('could Maya and I do this after dinner?'), top=20)
    inner += gut(answer('Not after: it runs 7 to 9, and your table is 8:15. Leaving at eight would mean missing the last hour, and it is one piece played whole, so that is the part you would lose.<br><br>Three ways that actually work: keep dinner and skip the hour (it runs again next Saturday); ask Maya and Alex whether 9:30 works for the table; or go to the hour on your own another week.<br><br>Want me to ask them about 9:30?'), top=18)
    inner += gut(card(f'<div class="kick" style="color: {MUTE};">TO MAYA AND ALEX &middot; NOT SENT</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">There&rsquo;s a listening hour at Canal Hall on Saturday, 7 to 9, that I&rsquo;d like to catch. Would 9:30 at the noodle bar work instead of 8:15?</div>'
                      + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 12px;">{door("Send to Maya and Alex")}{door("Change the wording", MUTE)}</div>'), top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">Ask, or change something</span></div>', top=26)
    return consumer(phone(inner, 0, active='Chat'))

def sent_phone():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">FRIDAY 12:34 PM</span></div></div>')
    inner += gut(card(f'<div class="kick" style="color: {GOLDD};">SENT TO MAYA AND ALEX &middot; 12:34</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">There&rsquo;s a listening hour at Canal Hall on Saturday, 7 to 9, that I&rsquo;d like to catch. Would 9:30 at the noodle bar work instead of 8:15?</div>'
                      + f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 12px;">{facepile(["M", "A"], 24, -6)}<span style="font-size: 13px; color: {MUTE};">Dinner is still 8:15 until they say.</span></div>'), top=22)
    inner += gut(answer('Sent. I&rsquo;ll show you their answer here and on Home. Nothing about Saturday has changed yet.'), top=18)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Back to Saturday evening') + door('The hour, at Canal Hall') + '</div>', top=22)
    return consumer(phone(inner, 0, active='Chat'))

def back_phone():
    """B's scroll restored; the hour carries one quiet line of state the person caused."""
    html = b_scroll(extra_under_hour=f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Dinner moved to 9:30, with Maya and Alex.</div>')
    return html

def change_phone():
    """Saturday 5:50 PM. Maya and Alex said yes to 9:30 at 2 PM; the dinner itself still says 8:15. At 5:40 the noodle bar posted last orders at 9. Every option is re-read at 5:50."""
    inner = header('NEW YORK', 'Saturday 5:50 PM') + question_line('Saturday evening', ctx='Around dinner')
    inner += gut(card(f'<div class="kick" style="color: {OX};">CHANGED &middot; 5:40 PM</div><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; margin-top: 6px;">The noodle bar stops taking orders at 9 tonight</div>'
                      + sup('So it won&rsquo;t work for 9:30. Maya and Alex said yes to 9:30 this afternoon; the dinner itself still says 8:15 at the noodle bar, and that still stands. The listening hour is untouched.', INK2) + src('From the noodle bar&rsquo;s own listing, posted 5:40 PM')
                      + f'<div style="margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(27,23,20,0.08);">{title("Yours to decide: where at 9:30, or 8:15 as it stands", 16, 21, 600)}</div>'
                      + '<div style="margin-top: 6px;">' + place_unit('table', 'The long table at the caf&eacute;', 'Open till 11 &middot; four blocks from the hall', 'A communal table; seating for three isn&rsquo;t confirmed.') + place_unit('noodles', 'The counter on Bowery', 'Open till 11 &middot; ten minutes on foot', 'The same kind of bowl; counter seats only, not confirmed for three.', last=True) + '</div>'
                      + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 8px;">{door("Suggest one to Maya and Alex")}{door("Keep 8:15 there and skip the hour", MUTE)}</div>'), top=20)
    inner += sect('Still on tonight') + gut('<div>' + u_hour().replace('This Saturday&rsquo;s hour', 'Doors 6:45') + '</div>')
    inner += sect('Also tonight') + gut('<div>' + place_unit('pier', 'The pier at sunset', 'Sunset 7:04 &middot; free', 'The west pier; bring a jacket, it turns cold fast.') + event_unit('SAT', '13', 'Outdoor film on the lawn', 'Saturday 8:30 PM', 'free', 'Starts at dark; forty minutes from the noodle bar.', kind='film') + u_table().replace('Saturday mornings &middot; coffee', 'Till 11 &middot; coffee, wine') + '</div>')
    inner += sect('Another day') + gut('<div>' + place_unit('pier', 'The pier at low water', 'Low water was 2:40&ndash;5 today', 'Next low water in the afternoon: Sunday, 3:20.', last=True) + '</div>')
    return phone2(inner)

def lens_phone():
    """One chosen lens inside the phone: around Saturday's dinner. The same world, ordered by what fits before and after the table."""
    inner = header('NEW YORK', 'Friday') + question_line('Saturday evening', ctx='Around dinner')
    inner += gut(f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 14px; background: {CARD}; border: 1px solid {HAIR};">{facepile(["M", "A", "you"], 28, -8)}<div style="flex: 1;"><div style="font-size: 15px; font-weight: 600; color: {INK};">Dinner with Maya and Alex</div><div style="font-size: 13px; color: {MUTE};">Saturday 8:15 &middot; the noodle bar &middot; settled</div></div></div>', top=18)
    inner += sect('Before dinner') + gut('<div>' + place_unit('pier', 'The pier at sunset', 'Sunset 7:04 &middot; twenty minutes from the noodle bar', 'The west pier; bring a jacket, it turns cold fast.') + event_unit('SAT', '13', 'The listening hour at Canal Hall', 'Saturday 7&ndash;9 PM', '$12 at the door', 'Runs past your table; you would leave at eight and miss the last hour.', last=True, kind='hall') + '</div>')
    inner += sect('After dinner') + gut('<div>' + event_unit('SAT', '13', 'Outdoor film on the lawn', 'Saturday 8:30 PM', 'free', 'Starts at dark; forty minutes from the noodle bar, so you would arrive late.', kind='film') + place_unit('table', 'The long table at the caf&eacute;', 'Open till 11 &middot; four blocks', 'For after, if the noodle bar closes early.', last=True) + '</div>')
    inner += gut(ending(['Just me, Saturday evening', 'All of Saturday']), top=28)
    return phone2(inner)

def board():
    row1 = [col(chat_phone(), daycap('FROM THE HOUR &middot; CHAT', 'THE ASK, ANSWERED HONESTLY', '&ldquo;Could Maya and I do this after dinner?&rdquo;', 'THE OVERLAP IS NAMED; LEAVING EARLY IS CALLED WHAT IT IS; THREE REAL WAYS; THE SMALLEST DECISION IS ONE QUESTION TO TWO PEOPLE')),
            col(sent_phone(), daycap('ONE DELIBERATE SEND', 'READBACK', 'Sent; nothing about Saturday has changed', 'THE RECIPIENTS ARE NAMED &middot; NOTHING MOVED &middot; TWO DOORS BACK')),
            col(back_phone(), daycap('BACK IN PLACES', 'B&rsquo;S SCROLL, WITH ONE LINE OF STATE', 'Saturday evening kept; the hour says what you did', 'THE QUESTION IS PART OF THE RETURN &middot; ONE QUIET LINE, NOT A LEDGER')),
            notecol('Help that protects the outing', [
                ('THE BASELINE, MADE COHERENT', N('The first export said &ldquo;before dinner would work&rdquo; and proposed leaving at eight from a piece meant to be heard whole. Now the fixture is explicit: one recording, 7 to 9, played end to end; dinner settled at 8:15. The answer says the overlap plainly, names what leaving early costs, and offers three ways that actually work, including doing less. The smallest decision is one question to Maya and Alex, and the person is asked whether to send it.')),
                ('THE JOURNEY, SHORTENED', N('Chat, one send, back. The message is prepared where the question was asked, to named recipients, and goes only when the person taps send. Readback is one line: sent, nothing changed. Service ownership stays with the arrangement; the person does not visit it.')),
                ('WHAT WAS CORRECTED', N('No feasibility invented where duration and transfer were unknown; no &ldquo;clean fit&rdquo; that truncates the event; no visible dependency ledger inside the phone. The pre-Plan send remains a dependency and is recorded on 08, not drawn as a caution on the screen.')),
            ])]
    row2 = [col(change_phone(), daycap('SATURDAY 5:50 PM &middot; ONE GENUINE CHANGE', 'THE KITCHEN CLOSES AT 9', 'What no longer works, what stands now, what is yours to decide', 'EVERY OPTION RE-READ AT 5:50 (&sect;9.6): LOW WATER IS OVER, THE LIBRARY WAS FRIDAY &middot; NOTHING CANCELLED, NOTHING ADOPTED &middot; SEATING NOT CONFIRMED, SAID SO')),
            col(lens_phone(), daycap('ONE LENS, INSIDE THE PHONE', 'AROUND SATURDAY&rsquo;S DINNER', 'The same world, ordered by what fits before and after the table', 'THE DINNER IS A CONTEXT CHIP, NOT A MODE &middot; WHAT DOES NOT FIT SAYS WHY IN ONE LINE')),
            notecol('The change, the lens, the comparison kept outside', [
                ('AFTER THE CHANGE (&sect;9.6)', N('Three things are kept apart. Practical infeasibility: the noodle bar won&rsquo;t work for 9:30 now. Agreement: Maya and Alex said yes to 9:30 this afternoon. Adoption: the dinner itself still says 8:15 at the noodle bar and still stands; nothing was cancelled and nothing was changed on their behalf. Every visible option is re-read at 5:50: low water ended at five and the library was Friday, so they are gone or moved to &ldquo;Another day&rdquo;; the pier at sunset, the film and the long table are still ahead. The two replacement candidates carry hours from their listings and say that seating for three is not confirmed.')),
                ('THE THREE LENSES, KEPT OUT HERE', tbl(['LENS', 'WHAT LEADS', 'WHAT DROPS OR MOVES'], [['Just me', 'The film, the hour, the pier', 'Nothing; the world as on 03'], ['With Maya', 'Her places first: the Print Room, the pier, the counter', 'Nothing drops; order changes'], ['Around Saturday&rsquo;s dinner', 'What fits before and after 8:15 at the noodle bar', 'The hour and the film say why they do not fit cleanly']])),
                ('THE ALTERNATIVE ENDING', N('Read the hour on 03 and leave. It is as complete as any of this.')),
            ])]
    html = two_rows(1900, '06', f'{STAMP} &middot; 06 &middot; E &middot; TAKING IT FORWARD &middot; REVISED 09-07 (&sect;8)', '06 &middot; E &middot; Help that protects what makes the outing worthwhile',
                    'Rebuilt after the first-export critique: the event and the dinner now form a coherent baseline, the answer protects the experience instead of fitting timestamps around it, the proposal journey is Chat, one send, back, and one genuine change is followed by the smallest decision it leaves. One chosen lens is drawn inside the phone; the three-lens comparison stays outside.', row1,
                    'A GENUINE CHANGE, AND ONE LENS', 'What got worse, what stands, what to decide; the same world around the table', row2, default_h=4800)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 06', changelog([
        ['Chat', 'An honest answer that names the overlap and the cost of leaving early; three real ways; one question', 'The message is prepared where it was asked and sent only on tap', 'The hour&rsquo;s duration and form and the dinner&rsquo;s time are supplied facts; Maya&rsquo;s availability is not claimed', 'A pre-Plan message to two people (arrangements owner)'],
        ['Sent', 'Sent; nothing about Saturday changed', 'One line of readback, two doors back', '&mdash;', 'Same'],
        ['Back', 'B&rsquo;s scroll with the current dinner state', 'The question survives the round trip; the line is current, not historical', '&mdash;', '&mdash;'],
        ['Change', 'What no longer works at 9:30, what still stands (8:15 as it is), what is theirs to decide', 'Two candidates with hours; seating not confirmed; one door to suggest, one to keep 8:15', 'The bar&rsquo;s listing at 5:40; the caf&eacute; and counter hours are fixture; every option re-read at 5:50', 'Practical assessment freshness (Integration); agreement vs adoption in the arrangement owner'],
        ['Lens', 'The world ordered around the table', 'A context chip, not a mode; clear returns to the plain question', 'Walking times are fixture', 'A chosen origin for real times']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '06 - E - Taking It Forward.dc.html'), 'w').write(html); print('wrote 06 v2', len(html))
