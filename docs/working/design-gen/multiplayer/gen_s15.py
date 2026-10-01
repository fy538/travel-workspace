"""21 · Receiving. Home over an ordinary week with a dozen friends sharing. What was sent to you comes first; what has a
time comes next and leaves when its time passes; what was sent to everyone is a quiet section, grouped by person and
capped. Nothing is counted as unread and nothing piles up: what you did not see is in Life, under each person. A quiet
day is allowed to be quiet. Seeing less of someone is private and temporary."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
import gen_s6 as L6
import gen_s12 as K
from gen_s1 import CARD_CSS, share, status, footer, sep, photo_grid, gathering, place_card, _g
from gen_s2 import sheet
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD21 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)

def av(letter, size=28): return f'<span style="width: {size}px; height: {size}px; border-radius: {size//2}px; background: {INK}; color: {CARD}; display: inline-flex; align-items: center; justify-content: center; font-size: {int(size*0.4)}px; font-weight: 700; flex: none;">{letter}</span>'
def mini(letter, name, text, when, more=None, thumbk=None, last=False):
    """A friend's share, compact: who, the words, when. Several from one person fold into one row."""
    bb = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.07);'
    m = f'<div class="fn" style="margin-top: 4px;">{more}</div>' if more else ''
    t = f'<div style="margin-left: auto; flex: none;">{thumb(thumbk, 44)}</div>' if thumbk else ''
    return (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0;{bb}">{av(letter)}'
            f'<div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 14px; font-weight: 600;">{name}</span><span class="fn">{when}</span></div>'
            f'<div style="font-size: 15px; line-height: 21px; margin-top: 2px;">{text}</div>{m}</div>{t}</div>')
def section(t, top=26): return sect(t, top=top)
def home(time, read, sub, me='N'): return avatar_for(anchor_row('NEW YORK', time), me) + orientation(read, sub, 26, 30)

# ── Monday: one thing ──
def monday():
    inner = home('MONDAY 8:10 AM', 'Clear until four.', 'Monday &middot; 61&deg; &middot; your next thing is Thursday')
    inner += section('From friends') + gut(mini('P', 'Priya', 'bread&rsquo;s out of the oven if anyone&rsquo;s near', '7:52 AM', last=True))
    return phone2(inner, active='Home')

def doorway(names, n):
    """Home's one line about place shares: who added places, and a door to Places. The shares themselves live there."""
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.10);">'
            f'{_g(S.PIN_P, MUTE, 16)}<span style="font-size: 14.5px; color: {INK}; flex: 1;">{names} added {n} places</span>'
            f'<span style="font-size: 14px; font-weight: 600; color: {GOLDD};">In Places &rarr;</span></div>')
def chips(active, items=('Near you', 'Saved', 'From friends')):
    c = lambda t: (f'<span style="height: 30px; border-radius: 15px; display: inline-flex; align-items: center; padding: 0 13px; font-size: 13.5px; font-weight: 600; '
                   f'color: {INK if t == active else MUTE}; border: {"1.3px solid " + INK if t == active else "1px solid rgba(27,23,20,0.14)"}; background: {CARD if t == active else "transparent"};">{t}</span>')
    return '<div style="display: flex; gap: 6px;">' + ''.join(c(t) for t in items) + '</div>'
def friend_place(name, where, who, said, when):
    return S.place_line(name, where, f'<b style="font-weight: 600;">{who}</b> {said}', f'<div class="fn" style="margin-top: 4px;">{when}</div>')

# ── Tuesday: eleven things overnight ──
def tuesday():
    """Sept 26: Home carries what is addressed to you, the day's posts with no place in a small strip, and one line about
    place shares. The place shares themselves are in Places (the Sept 5 social split)."""
    inner = home('TUESDAY 7:40 AM', 'Rain from eleven.', 'Tuesday &middot; 58&deg;')
    inner += section('To you') + gut(share('Maya', 'LAST NIGHT · TO YOU', 'saw a dog that looked exactly like sam', extra=S.photo_thumb(120, 'PHOTO &middot; MAYA')))
    inner += section('From friends') + gut(
        mini('D', 'Dana', 'calanques. 7am. nobody', '1:04 AM &middot; MARSEILLE', thumbk='pier')
        + mini('S', 'Sam', 'the new four tet record is actually good', '11:40 PM', last=True))
    inner += gut(doorway('Priya and Sam', 2), top=10)
    return phone2(inner, active='Home')
def friday():
    inner = home('FRIDAY 6:30 PM', 'Clear tonight.', 'Friday &middot; 64&deg;')
    inner += section('Tonight') + gut(share('Sam', '6:12 PM · TO FRIENDS', 'pacha tonight. john summit. on at 1', extra=S.ticket_row(), where='Lower East Side'))
    inner += section('This weekend') + gut(mini('N', 'You', 'brunch at hato, saturday 12:30', 'SETTLED', more='PRIYA AND MAYA ARE IN', last=True))
    inner += section('From friends') + gut(mini('M', 'Maya', 'finally finished it. it split. i am not ok', '5:02 PM', thumbk='noodles', last=True))
    return phone2(inner, active='Home')

# ── Saturday noon: the time-bound things have gone ──
def saturday():
    inner = home('SATURDAY 12:05 PM', 'Brunch at 12:30.', 'Hato &middot; Cobble Hill &middot; Priya has the table, upstairs')
    inner += section('Today') + gut(f'<div style="{CARD_CSS} padding: 12px 14px; display: flex; gap: 12px; align-items: center;">{thumb("noodles", 44)}<div><div style="{SERIF} font-weight: 600; font-size: 17px;">Brunch at Hato</div><div style="font-size: 13px; color: {MUTE};">12:30 &middot; Priya, Maya, you</div></div></div>')
    inner += section('From friends') + gut(mini('S', 'Sam', 'home. that was unreal', '3:40 AM', thumbk='hall', last=True))
    return phone2(inner, active='Home')

# ── Sunday: nothing new ──
def sunday():
    """Sept 26 (§12.5): quiet from friends, not an empty Home. Home's own value carries on (drawn minimally, as the Home
    project owns it); nothing social is manufactured to fill the gap."""
    inner = home('SUNDAY 10:20 AM', 'Clear until five.', 'Sunday &middot; 60&deg; &middot; nothing on today')
    inner += section('This afternoon') + gut(f'<div style="{CARD_CSS} padding: 12px 14px; display: flex; gap: 12px; align-items: center;">{thumb("pier", 44)}<div><div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 21px;">Low water at the pier, 2:40</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">Ten minutes&rsquo; walk &middot; your place, for walking it off</div></div></div>')
    inner += section('From friends') + gut(plain('Nothing new since yesterday.', MUTE, 15, 21))
    return phone2(inner, active='Home')
def week_life():
    """Sept 26 (§12.5): not a backlog. Under one person in Life People: what Maya shared with you is reachable while she
    leaves it up. It is not your kept collection, not your record, and nothing is counted as unseen."""
    inner = L6.head('PEOPLE &middot; MAYA', 'Maya', 'Friends since 2019.')
    inner += L6.sec('SHARED WITH YOU LATELY', '', 26) + K.thing(0, 'the dog that looked like sam', 'MON') + K.thing(3, 'it split. i am not ok', 'FRI')
    inner += L6.sec('YOU KEPT', '1') + K.thing(1, 'Hato &middot; the broth is stupid good', 'OCT 5')
    inner += L6.door('Shared with Maya')
    return L6.phone(inner)
def places_friends():
    """Sept 26: where place shares live (the Sept 5 social split): Places, a From friends view, each place beside its
    friend's words on a small map."""
    inner = S.page_bar('PLACES')
    inner += gut(chips('From friends'), top=14)
    inner += f'<div style="margin: 14px 22px 0 22px; border-radius: 10px; overflow: hidden; border: 1px solid rgba(27,23,20,0.12);">{S.paper_map(130, ((0.30, 0.56), (0.52, 0.38), (0.72, 0.62)), 349)}</div>'
    inner += section('This week', top=22) + gut(
        friend_place('Lulu&rsquo;s', 'Carroll Gardens', 'Priya', 'good for a long dinner, with parents', 'PRIYA &middot; MONDAY')
        + friend_place('The Lantern', 'Court Street', 'Sam', 'one film a week and exactly one kind of cake', 'SAM &middot; MONDAY'))
    inner += section('Earlier', top=22) + gut(friend_place('Hato', 'Cobble Hill', 'Maya', 'the broth is stupid good', 'MAYA &middot; OCT 5'))
    return phone2(inner, active='Places')
def see_less():
    inner = home('TUESDAY 7:42 AM', 'Rain from eleven.', 'Tuesday &middot; 58&deg;')
    inner += section('From friends') + gut(mini('S', 'Sam', 'the new four tet record is actually good', '11:40 PM', more='AND 2 MORE FROM SAM', last=True))
    inner += sheet(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">See less from Sam</div>'
                   + f'<div style="margin-top: 8px;">{plain("His shares stop coming to Home for a while. They are still under Sam in Life, and anything he sends to you alone still comes. Sam isn&rsquo;t told.", INK2, 15, 21)}</div>'
                   + f'<div style="margin-top: 14px; display: flex; gap: 8px;">{btn("For a week")}{btn("Until I change it", False)}</div>')
    return phone2(inner, active='Home')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('MONDAY', '1', 'One thing', 'Home&rsquo;s line about the day, then one friend&rsquo;s post with no place. That is a whole morning.', monday(), (P('HOME'),)),
                 cell('TUESDAY', '2', 'A busy morning', 'What Maya sent you alone comes first. The day&rsquo;s posts with no place sit in a small strip. Priya&rsquo;s and Sam&rsquo;s places are one line pointing to Places.', tuesday(), (P('HOME'), P('BUSY'))),
                 cell('FRIDAY', '3', 'Things with a time', 'Tonight and this weekend sit above everything else because they will not be true tomorrow.', friday(), (P('HOME'), P('TIME-BOUND'))),
                 cell('SATURDAY NOON', '4', 'They leave on time', 'Sam&rsquo;s night went when it was over. Today is the brunch.', saturday(), (P('HOME'), P('EXPIRY')))], top=16)
    r2 = rowdiv([cell('SUNDAY', '5', 'Quiet from friends', 'One grey line, and nothing made up to fill it. Home&rsquo;s own afternoon carries on.', sunday(), (P('HOME'), P('QUIET'))),
                 cell('TUESDAY', '6', 'Places, from friends', 'Where a place share lives: beside the place, in the friend&rsquo;s words, on a small map. Useful with two friends, and again weeks later.', places_friends(), (P('PLACES'), P('FROM FRIENDS'))),
                 cell('ANY TIME', '7', 'Still reachable, under the person', 'What Maya shared stays under Maya while she leaves it up. Not kept for you, and nothing counted as unseen.', week_life(), (P('LIFE'), LIFE)),
                 cell('TUESDAY', '8', 'Seeing less of someone', 'Private and temporary. What he sends to you alone still comes, and he is not told.', see_less(), (P('HOME'), P('PRIVATE')))])
    n1 = notes('HOW HOME ORDERS WHAT ARRIVES', led([
                     ('1 &middot; TO YOU', 'Sent to you alone, or asking you something, before anything sent to everyone. Not automatically above a practical change: a funny photo and a moved table are treated differently.'),
                     ('2 &middot; WITH A TIME', 'Tonight, today, this weekend. Above everything else, and gone when the time has passed.'),
                     ('3 &middot; FROM FRIENDS, TODAY', 'Posts with no place, sent to everyone: a small strip, the day they arrive, three or four at most.'),
                     ('4 &middot; PLACES, NOT HOME', 'A share about a place lives in Places, beside the place, in the friend&rsquo;s words. Home shows one line pointing there.'),
                     ('NO COUNTS', 'No unread numbers, no badges, no &ldquo;you missed&rdquo;. Nothing turns red.'),
                     ('NOTHING PILES UP', 'A share leaves Home when its relevance ends: its time passes, or it is simply old news. It stays reachable under the person while they leave it up. It is never copied into your Life unless you keep it.'),
                     ('NO MADE-UP URGENCY', 'When friends have not posted, nothing social is manufactured to fill the gap. Home&rsquo;s own value carries on.'),
                 ]), w=600)
    n2 = notes('OPEN', led([
        ('HOW MANY', 'Three or four compact rows is a guess. The right cap depends on how many friends people have here, which nobody knows yet.'),
        ('NOTIFICATIONS', 'Board 02&rsquo;s proposal stands: statuses, whereabouts, places and links never ping; invitations, comments on your own share and answers to your ask do.'),
        ('WHY THIS SPLIT', 'It follows the Sept 5 social split, reaffirmed by the Sept 26 decision, and the code already follows it. The earlier version of this board put place shares on Home.'),
        ('WHAT WOULD CHANGE IT', 'If, in real use, place shares in Places go unseen and senders hear nothing back, Home needs to carry more.'),
        ('HOME&rsquo;S OWN CONTENT', 'This board is a specimen of social delivery, not a Home composition. The day line and the afternoon are Home&rsquo;s own work (the Home project), drawn minimally to show friends sitting beside it.'),
    ]), w=620)
    bodyhtml = r1 + r2 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD21 + f'<div style="width: 1860px; min-height: {hh("03", 3000)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('03 &middot; RECEIVING', 'Where friends&rsquo; shares arrive',
                   'An ordinary week of a dozen friends sharing. Home carries what is sent to you, what has a time, and the day&rsquo;s posts with no place; a share about a place lives in Places, beside it, with one line on Home pointing there. '
                   'Nothing is counted, nothing piles up, and a quiet day from friends adds no filler. Drawn, not tested with anyone.')
            + bodyhtml + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('03 - Receiving', html)

if __name__ == '__main__':
    build()
