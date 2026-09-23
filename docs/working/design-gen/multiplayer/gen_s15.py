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

# ── Tuesday: eleven things overnight ──
def tuesday():
    inner = home('TUESDAY 7:40 AM', 'Rain from eleven.', 'Tuesday &middot; 58&deg;')
    inner += section('To you') + gut(share('Maya', 'LAST NIGHT · TO YOU', 'saw a dog that looked exactly like sam', extra=S.photo_thumb(120, 'PHOTO &middot; MAYA')))
    inner += section('From friends') + gut(
        mini('S', 'Sam', 'this is the cinema. one film a week and exactly one kind of cake', '11:40 PM', more='AND 2 MORE FROM SAM', thumbk='film')
        + mini('P', 'Priya', 'the upstairs room at lulu&rsquo;s is the reason to go', '9:40 PM', thumbk='table')
        + mini('D', 'Dana', 'calanques. 7am. nobody', '1:04 AM &middot; MARSEILLE', thumbk='pier', last=True))
    inner += gut(door('Six more from friends', MUTE), top=4)
    return phone2(inner, active='Home')

# ── Friday: things with a time ──
def friday():
    inner = home('FRIDAY 6:30 PM', 'Clear tonight.', 'Friday &middot; 64&deg;')
    inner += section('Tonight') + gut(share('Sam', '6:12 PM · TO FRIENDS', 'pacha tonight. john summit. on at 1', extra=S.ticket_row(), where='Lower East Side'))
    inner += section('This weekend') + gut(mini('N', 'You', 'brunch at hato, saturday 12:30', 'SETTLED', more='PRIYA AND MAYA ARE IN &middot; DANA HASN&rsquo;T SAID', last=True))
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
    inner = home('SUNDAY 10:20 AM', 'A slow Sunday.', 'Sunday &middot; 60&deg; &middot; nothing on today')
    inner += section('From friends') + gut(plain('Nothing new since yesterday.', MUTE, 15, 21))
    inner += section('From your life') + gut(f'<div style="{CARD_CSS} padding: 12px 14px; display: flex; gap: 12px; align-items: center;">{thumb("pier", 44)}<div><div class="fn">A YEAR AGO TODAY</div><div style="{SERIF} font-weight: 600; font-size: 17px; margin-top: 2px;">The pier at low water, with Maya</div></div></div>')
    return phone2(inner, active='Home')

# ── the week, in Life ──
def week_life():
    inner = L6.head('PEOPLE &middot; THIS WEEK', 'From friends', 'Fourteen things &mdash; all of them still here.')
    inner += L6.sec('MAYA', '3', 26) + K.thing(0, 'the dog that looked like sam', 'MON') + K.thing(3, 'it split. i am not ok', 'FRI')
    inner += L6.sec('SAM', '4') + K.thing(1, 'the cinema &middot; one film a week', 'MON') + L6.row1(L6.GLASS, 'Pacha, John Summit', 'FRI')
    inner += L6.sec('PRIYA', '4') + K.thing(5, 'the upstairs room at lulu&rsquo;s', 'MON')
    inner += L6.door('Everyone, this week')
    inner += L6.voice('What you did not open is here, not piling up on Home.')
    return L6.phone(inner)

# ── seeing less of someone ──
def see_less():
    inner = home('TUESDAY 7:42 AM', 'Rain from eleven.', 'Tuesday &middot; 58&deg;')
    inner += section('From friends') + gut(mini('S', 'Sam', 'this is the cinema. one film a week and exactly one kind of cake', '11:40 PM', more='AND 2 MORE FROM SAM', thumbk='film', last=True))
    inner += sheet(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">See less from Sam</div>'
                   + f'<div style="margin-top: 8px;">{plain("His shares stop coming to Home for a while. They are still under Sam in Life, and anything he sends to you alone still comes. Sam isn&rsquo;t told.", INK2, 15, 21)}</div>'
                   + f'<div style="margin-top: 14px; display: flex; gap: 8px;">{btn("For a week")}{btn("Until I change it", False)}</div>')
    return phone2(inner, active='Home')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('MONDAY', '1', 'One thing', 'Home&rsquo;s own line about the day, then one friend. That is a whole morning.', monday(), (P('HOME'),)),
                 cell('TUESDAY', '2', 'Eleven things overnight', 'What Maya sent you alone comes first, at full size. Everything sent to everyone is below, compact, one row per person: Sam&rsquo;s three fold into one. Six more are a door, not a scroll.', tuesday(), (P('HOME'), P('BUSY'))),
                 cell('FRIDAY', '3', 'Things with a time', 'Tonight and This weekend sit above everything else because they will not be true tomorrow. Brunch shows who said what, never who is behind.', friday(), (P('HOME'), P('TIME-BOUND'))),
                 cell('SATURDAY NOON', '4', 'They leave on time', 'The market post went at noon, as Priya said. Sam&rsquo;s night went when it was over. Today is the brunch.', saturday(), (P('HOME'), P('EXPIRY')))], top=16)
    r2 = rowdiv([cell('SUNDAY', '5', 'A quiet day', 'Nothing new from friends, and Home says so in one grey line. It does not fill the space with suggestions or old posts. One return from Life, a year ago today.', sunday(), (P('HOME'), P('QUIET'))),
                 cell('ANY TIME', '6', 'Where missed things go', 'Nothing piles up on Home. What you did not open is in Life, under each person, for the week. Drawn in Life&rsquo;s grammar.', week_life(), (P('LIFE'), LIFE)),
                 cell('TUESDAY', '7', 'Seeing less of someone', 'Private and temporary. His shares go quiet on Home; what he sends to you alone still comes, and he is not told.', see_less(), (P('HOME'), P('PRIVATE')))])
    n1 = notes('HOW HOME ORDERS WHAT ARRIVES', led([
                     ('1 &middot; TO YOU', 'Anything sent to you alone, or asking you something, first and at full size.'),
                     ('2 &middot; WITH A TIME', 'Tonight, today, this weekend. Above everything else, and gone when the time has passed.'),
                     ('3 &middot; FROM FRIENDS', 'Everything sent to everyone. Compact rows, one per person, newest first, three or four at most; the rest behind one door.'),
                     ('NO COUNTS', 'No unread numbers, no badges, no &ldquo;you missed&rdquo;. Nothing turns red.'),
                     ('NOTHING PILES UP', 'Yesterday&rsquo;s shares leave Home and live in Life under each person. Home is today, not a backlog.'),
                     ('QUIET IS FINE', 'A day with nothing new says so. Home never fills itself.'),
                 ]), w=600)
    n2 = notes('OPEN', led([
        ('HOW MANY', 'Three or four compact rows is a guess. The right cap depends on how many friends people have here, which nobody knows yet.'),
        ('NOTIFICATIONS', 'Board 11&rsquo;s proposal stands: statuses, whereabouts, places and links never ping; invitations, comments on your own share and answers to your ask do.'),
        ('HOME&rsquo;S OWN CONTENT', 'The day line and the Life return are Home&rsquo;s existing work (the Home project). Drawn minimally here, only to show friends sitting beside it rather than taking over.'),
    ]), w=620)
    bodyhtml = r1 + r2 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD21 + f'<div style="width: 1860px; min-height: {hh("21", 3000)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('21 &middot; RECEIVING', 'Home over an ordinary week',
                   'What a dozen friends sharing looks like from Nora&rsquo;s Home, Monday to Sunday. What was sent to you first; what has a time next, gone when it passes; everything else compact, grouped by person, capped. '
                   'Nothing is counted, nothing piles up, and a quiet day stays quiet. Drawn, not tested with anyone.')
            + bodyhtml + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('21 - Receiving', html)

if __name__ == '__main__':
    build()
