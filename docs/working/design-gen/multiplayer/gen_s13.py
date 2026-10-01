"""19 · The container as a timeline. The same collections as board 08, in the same Life grammar, read over time
instead of by kind: one spine, dates on the left, seasons as section heads, each thing hanging off the spine in its own
form (a wristband, a ticket, a small contact strip, a friend's words, a place with a been mark). Quiet stretches are
drawn as a dashed length of spine, not as absence. A small switch in the masthead moves between By kind and Over time."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
import gen_s6 as L6
import gen_s12 as K
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD19 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)

# ── the switch, in Life's lens-chip style ──
def switch(active='OVER TIME', add=False): return K.switch(active, add)

# ── the spine ──
def season(t, span): return (f'<div style="margin:28px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;">'
                             f'<span class="kicker" style="color:var(--mute);">{t}</span><span class="barmeta" style="margin-left:auto;">{span}</span></div>')
def entry(date, body, meta='', dot='solid', first=False, last=False, meta_color=None):
    """One thing on the spine: its date, a dot, and the thing in its own form."""
    top = '10px' if first else '0'
    bottom = 'calc(100% - 14px)' if last else '0'
    dotcss = {'solid': 'background:var(--ink);', 'hollow': 'background:var(--paper); border:1.3px solid var(--ink); box-sizing:border-box;',
              'gold': 'background:var(--gold);', 'green': 'background:var(--green);'}[dot]
    mc = f' color:{meta_color};' if meta_color else ''
    m = f'<div class="meta" style="margin-top:6px; white-space:normal;{mc}">{meta}</div>' if meta else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:stretch;">'
            f'<div style="width:42px; flex:none; padding-top:9px; text-align:right; font-family:var(--mono); font-size:9.5px; font-weight:500; letter-spacing:0.6px; color:var(--mute); line-height:13px;">{date}</div>'
            f'<div style="width:22px; flex:none; position:relative;"><span style="position:absolute; left:10px; top:{top}; bottom:{bottom}; width:1px; background:var(--hairline);"></span>'
            f'<span style="position:absolute; left:7px; top:11px; width:7px; height:7px; border-radius:4px; {dotcss}"></span></div>'
            f'<div style="flex:1; min-width:0; padding:6px 0 20px 4px;">{body}{m}</div></div>')
def quiet(t):
    """A quiet stretch: the spine goes on, dashed, and says how long."""
    return (f'<div style="margin:0 22px; display:flex; align-items:stretch;"><div style="width:42px; flex:none;"></div>'
            f'<div style="width:22px; flex:none; position:relative;"><span style="position:absolute; left:10px; top:0; bottom:0; width:0; border-left:1.2px dashed rgba(27,23,20,0.22);"></span></div>'
            f'<div style="flex:1; padding:16px 0 24px 4px;"><span class="meta">{t}</span></div></div>')
def now_line():
    return (f'<div style="margin:6px 22px 4px 22px; display:flex; align-items:center; gap:10px;"><span style="font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:1.2px; color:var(--gold-deep); width:42px; text-align:right;">NOW</span>'
            f'<span style="flex:1; height:1px; background:rgba(176,133,58,0.55);"></span></div>')

# ── bodies, each in its own form ──
def title_(t): return f'<div style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{t}</div>'
def words(t): return f'<div style="font-family:var(--serif); font-size:16px; line-height:22px; margin-top:3px; color:#3A332C;">{t}</div>'
def strip(n, start=0): return '<div style="display:flex; gap:5px; margin-top:8px;">' + ''.join(K.riso(start + i, 52) for i in range(n)) + '</div>'
def reply(who, t): return f'<div style="margin-top:8px; border-left:2px solid rgba(27,23,20,0.12); padding-left:10px; font-family:var(--serif); font-size:15px; line-height:20px; color:var(--mute);"><span style="color:var(--ink); font-weight:600;">{who}</span> {t}</div>'
def place(name, where, been=None):
    b = f'<span class="meta" style="margin-left:auto; color:var(--green);">BEEN &middot; {been}</span>' if been else ''
    return f'<div style="display:flex; align-items:baseline; gap:8px;"><span style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{name}</span>{b}</div><div class="rsub" style="margin-top:2px;">{where}</div>'
def open_q(q, t): return title_(q) + words(t)
def bands(*ts): return '<div style="display:flex; gap:7px; flex-wrap:wrap;">' + ''.join(K.band(t) for t in ts) + '</div>'

# ── the artifacts, whole, at four-fifths size ──
# The spine's content column is ~280px; a full artifact is drawn at 349px and zoomed to fit, so it keeps every part.
JS_FIELDS = 'DOORS=11:00 PM;ON=1:00 AM;ADMIT=1 · GENERAL'
def mini(html, z=0.8): return f'<div style="zoom:{z};">{html}</div>'
def admit(title, venue, date, status, fields, band='ADMIT ONE|SAM', sub=None):
    return mini(dci('Ticket', 236, mode='admission', density='full', kicker=f'ADMISSION · {venue.upper()}', date=date, status=status,
                    title=title, sub=sub or f'{venue}, New York', fields=fields, band=band))
def place_card(name, where, glyph_kind=None, good=(), been=None):
    """A place on the timeline, as the same line as everywhere else. A been mark sits under the reason."""
    b = f'<div style="margin-top:5px; font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1px; color:var(--green);">BEEN &middot; {been}</div>' if been else ''
    return S.place_line(name, where, S.good_line(good) if good else '', b)
def link_card():
    return S.link_line()
def place_card_v0(name, where, glyph_kind, good=(), been=None):
    g = f'<div style="display:flex; align-items:center; gap:6px; margin-top:12px; flex-wrap:wrap;"><span class="fn" style="flex:none; margin-right:2px;">GOOD FOR</span>{S.good_for(good)}</div>' if good else ''
    b = f'<div style="margin-top:10px; font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1px; color:var(--green);">BEEN &middot; {been}</div>' if been else ''
    return mini(f'<div style="{S.CARD_CSS} padding:14px 16px;"><div style="display:flex; gap:12px; align-items:center;">{thumb(glyph_kind, 56)}<div style="min-width:0; flex:1;">'
                f'<div class="fn" style="margin-bottom:4px;">A PLACE</div><div style="font-family:var(--serif); font-weight:600; font-size:19px; line-height:23px;">{name}</div>'
                f'<div style="font-size:13px; line-height:18px; color:var(--mute); margin-top:2px;">{where}</div></div></div>{g}{b}</div>')
def link_card_v0():
    return mini(f'<div style="{S.CARD_CSS} padding:14px 16px; display:flex; gap:12px; align-items:center;">{thumb("film", 56)}'
                f'<div style="min-width:0; flex:1;"><div class="fn" style="margin-bottom:4px;">LINK &middot; THE LANTERN&rsquo;S SITE</div>'
                f'<div style="font-family:var(--serif); font-weight:600; font-size:16px; line-height:21px;">This week: one film, through Sunday</div>'
                f'<div style="font-size:13px; line-height:18px; color:var(--ink2, #3A332C); margin-top:2px;">Court Street &middot; 7:15 nightly</div></div></div>')
def menu_card():
    """The paper menu kept from the trip, whole: the dishes as printed, the one that started this underlined in gold."""
    def dish(t, on=False):
        u = 'border-bottom:1.5px solid var(--gold); padding-bottom:1px;' if on else ''
        return f'<div style="font-family:var(--serif); font-size:16px; line-height:26px; text-align:center;"><span style="{u}">{t}</span></div>'
    return mini(f'<div style="{S.PAPER_CSS} padding:16px 20px 18px 20px; border-radius:4px;">'
                f'<div class="fn" style="text-align:center; letter-spacing:2px;">PRIMI</div>'
                f'<div style="margin:8px auto 6px auto; width:40px; height:1px; background:var(--hairline);"></div>'
                + dish('Gnocchi alla sorrentina') + dish('Spaghetti al limone') + dish('Cacio e pepe', True) + dish('Scialatielli ai frutti di mare') +
                f'<div class="fn" style="text-align:center; margin-top:10px;">A MENU &middot; SORRENTO &middot; KEPT AUG 18</div></div>')


JS = admit('John Summit', 'Pacha', 'SEPT 26', 'ON AT 1:00 AM', JS_FIELDS, 'ADMIT ONE|SAM', 'Pacha, New York · doors 11')

# ── 1 · Our New York, over time ──
def ny():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += switch(add=True)
    inner += season('AUTUMN 2026', 'SEPT &mdash; OCT')
    inner += entry('OCT<br>20', title_('The pier at low water') + words('for when one of us needs to walk it off') + strip(2) + reply('Maya', 'next low tide, i&rsquo;m in'), 'YOU ADDED &middot; A PLACE, TWO PHOTOGRAPHS', first=True)
    inner += entry('OCT<br>12', title_('Went to Hato') + words('the two of you, the queue at 6'), 'NORA AND MAYA &middot; BEEN', dot='green')
    inner += entry('OCT<br>5', words('the broth is stupid good') + f'<div style="margin-top:8px;">{place_card("Hato", "Cobble Hill &middot; ramen", "noodles", ("A cold night", "Two of you"))}</div>' + reply('Sam', 'the queue at 8 is a war crime'), 'MAYA ADDED &middot; A PLACE')
    inner += entry('SEPT<br>26', words('pacha. unreal. my ears are still ringing') + f'<div style="margin-top:8px;">{JS}</div>', 'NORA AND MAYA &middot; A NIGHT, BEEN', dot='green')
    inner += entry('SEPT<br>18', words('one film a week and exactly one kind of cake') + f'<div style="margin-top:8px;">{link_card()}</div>', 'SAM ADDED &middot; A LINK')
    inner += entry('SEPT<br>6', words('the thing nobody tells you about the greenmarket is that bread goes first').replace('margin-top:3px; ', ''), 'PRIYA ADDED &middot; A NOTE', last=True)
    inner += season('SUMMER 2026', 'JUN &mdash; AUG')
    inner += entry('JUL<br>5', title_('The greenmarket, first Saturday') + strip(3, 2), 'PRIYA ADDED &middot; THREE PHOTOGRAPHS', first=True, last=True)
    inner += L6.door('The first thing, in June')
    return L6.phone(inner)

# ── 2 · Nights out, over time ──
def nights():
    inner = L6.head('KEPT &middot; WITH SAM &middot; SINCE JUNE 2025', 'Nights out', 'Five nights &mdash; a rhythm more than a plan.')
    inner += switch()
    inner += season('AHEAD', '1')
    inner += entry('SAT', admit('Overmono', 'The warehouse', 'SAT', 'DOORS AT 11:00 PM', 'DOORS=11:00 PM;WITH=SAM;ADMIT=1 · GENERAL', 'ADMIT ONE|SAM HAS IT', 'The warehouse · doors 11'), 'UPCOMING &middot; SAM HAS TICKETS', dot='hollow', first=True, last=True)
    inner += now_line()
    inner += season('THIS YEAR', '3 NIGHTS')
    inner += entry('SEPT<br>26', JS + words('pacha. unreal.') + strip(3), 'YOU AND SAM &middot; ADMISSION, THREE PHOTOGRAPHS', first=True)
    inner += entry('MAY<br>16', admit('Caribou', 'The Mirage', 'MAY 16', 'BEEN', 'WHEN=MAY 16;WITH=SAM;ADMIT=1 · GENERAL') + words('the same door, again'), 'SAM')
    inner += entry('MAY<br>16', place_card('Ottavia', 'A bar', 'glass', ('Before a show',)) , 'YOU &middot; A PLACE', last=True)
    inner += season('2025', '1 NIGHT')
    inner += entry('JUN<br>2025', admit('Four Tet', 'The Mirage', 'JUN 2025', 'BEEN', 'WHEN=JUN 2025;WITH=SAM;ADMIT=1 · GENERAL') + words('the first night, at the Mirage'), 'SAM', first=True, last=True)
    return L6.phone(inner)

# ── 3 · Getting pasta right, over time ──
def pasta():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE AUG 17', 'Getting pasta right', 'Three attempts &mdash; one question still open.')
    inner += switch()
    inner += season('SEPTEMBER', '1')
    inner += entry('SEPT<br>2', title_('Attempt three') + words('held together. still bland') + strip(1, 2), 'A PHOTOGRAPH AND A NOTE', first=True, last=True)
    inner += season('AUGUST', '5')
    inner += entry('AUG<br>30', open_q('Why does it split?', 'the cheese goes in off the heat, apparently'), 'A QUESTION &middot; STILL OPEN', dot='gold', first=True, meta_color='var(--gold-deep)')
    inner += entry('AUG<br>28', title_('Attempt two') + words('split again'), 'A NOTE')
    inner += entry('AUG<br>24', title_('Attempt one') + words('cheese went in over the flame') + strip(1, 4), 'A PHOTOGRAPH AND A NOTE')
    inner += entry('AUG<br>18', menu_card(), 'KEPT FROM YOUR TRIP')
    inner += entry('AUG<br>17', title_('The plate in Sorrento') + words('where this started') + strip(1), 'NICE &rarr; ROME &middot; A PHOTOGRAPH', last=True)
    inner += K.doors2('Add something', 'Ask Maya in')
    return L6.phone(inner)

# ── 4 · quiet, then a return ──
def returned():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Thirteen things &mdash; eight of them places.')
    inner += switch()
    inner += season('WINTER', 'FEB')
    inner += entry('FEB<br>2', title_('Jo&rsquo;s weekend') + words('three from here, sent to jo: hato, the lantern, the pier') + reply('Maya', 'tell her to go at 6'), 'NORA &middot; SENT FROM THIS COLLECTION', first=True, last=True)
    inner += quiet('NOVEMBER &mdash; JANUARY')
    inner += season('AUTUMN 2026', 'SEPT &mdash; OCT')
    inner += entry('OCT<br>20', title_('The pier at low water') + strip(2), 'YOU ADDED &middot; A PLACE', first=True)
    inner += entry('OCT<br>5', place_card('Hato', 'Cobble Hill &middot; ramen', 'noodles', ('A cold night', 'Two of you')), 'MAYA ADDED &middot; A PLACE', last=True)
    inner += L6.door('All thirteen')
    return L6.phone(inner)

# ── 5 · a single night, as its own kept thing ──
def one_night():
    inner = L6.head('KEPT &middot; WITH MAYA &middot; ONE NIGHT', 'Pacha, John Summit', 'Friday into Saturday &mdash; the two of you.')
    inner += switch()
    inner += f'<div style="margin:18px 22px 0 22px;">{S.ticket_full().replace("date=\"TONIGHT\"", "date=\"SEPT 26\"")}</div>'
    inner += season('THE NIGHT', 'SEPT 26 &mdash; 27')
    inner += entry('10:38<br>PM', words('pacha tonight. john summit. on at 1') , 'SAM, TO FRIENDS &middot; WHERE IT CAME FROM', first=True)
    inner += entry('12:30<br>AM', title_('Maya at yours') + words('wearing the boots, don&rsquo;t laugh'), 'MAYA &middot; FROM YOUR CHAT')
    inner += entry('1:00<br>AM', title_('On') + strip(4), 'ON &middot; FOUR PHOTOGRAPHS, TWO OF THEM MAYA&rsquo;S')
    inner += entry('3:40<br>AM', words('home. that was unreal') + f'<div class="rsub" style="margin-top:4px;">Cab back, split &middot; $31 each</div>', 'MAYA', last=True)
    inner += L6.voice('Kept by both of you.')
    return L6.phone(inner)

def cell(k, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap('', k, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('1', 'Our New York, over time', 'The same collection on one spine. Each date says what happened, added or been: Maya adding Hato and the two of them going are two entries.', ny(), (LIFE, P('SHARED'), P('TIMELINE'))),
                 cell('2', 'Nights out, over time', 'The next night sits above a gold NOW line. Below, the nights as they happened, each as its full ticket, and the first a year back.', nights(), (LIFE, P('SHARED'), P('TIMELINE'))),
                 cell('3', 'Getting pasta right, over time', 'Read bottom to top, it is the story: the plate in Sorrento, the kept menu (whole, the dish underlined), three attempts, and the open question marked gold.', pasta(), (LIFE, P('PRIVATE'), P('TIMELINE'))),
                 cell('4', 'A gap, then back', 'November to January, nothing added: a dashed length of spine with its months, and nothing said about it. Then February, when it was useful again.', returned(), (LIFE, P('SHARED'), P('QUIET')))], top=20)
    r2 = rowdiv([cell('5', 'One night, kept on its own', 'The rave kept on its own: the ticket at the top, then the night by the hour, from Sam&rsquo;s share to the cab home.', one_night(), (LIFE, P('SHARED'), P('ONE NIGHT'))),
                 cell('08', 'The same collection, by kind', 'Board 08&rsquo;s version, with the switch set to By kind. Our New York opens over time; this is the other side of its switch.', K.our_ny(), (LIFE, P('BOARD 08'))),
                 notes('WHEN TIME, WHEN KIND', led([
                     ('THE SWITCH', 'By kind and Over time are two readings of the same collection, in Life&rsquo;s lens-chip style under the masthead. Nothing moves between them; nothing is filed twice.'),
                     ('WHICH OPENS FIRST', 'Decided Sept 26: what is in it decides. Collections of dated things open Over time: Nights out, Getting pasta right, a trip, Our New York. Collections kept to consult open By kind: Our places, Restaurants to try, Interesting stuff. A collection of one has no switch.'),
                     ('REMEMBERED', 'Once someone switches, that collection opens their way from then on, for them only. In a shared collection each person keeps their own.'),
                     ('THE SPINE', 'Dates in mono on the left, one hairline, a dot per thing. Seasons are the section heads, with counts. Hollow dot and a gold NOW line for what is ahead; a gold dot and a gold STILL OPEN for a question not yet settled, drawn like any other entry.'),
                     ('A GAP IS DRAWN', 'A long gap is a dashed length of spine with its months. No sentence about it, and no prompt.'),
                     ('ADDED IS NOT BEEN', 'Each date says what happened: someone added a thing, or people went. A chronology of additions never reads as where you were, and a list of ideas never becomes a completion meter.'),
                     ('ONE TYPE FOR WHAT IS KEPT', 'Serif for everything held: the name semibold, a person&rsquo;s words regular under it, replies smaller and muted. Mono for dates and labels. Sans only for the app itself: the switch, the doors, inside the ticket.'),
                     ('WHOLE, NOT CHIPS', 'Tickets and the menu appear whole on the spine at about four-fifths size; places and links are lines, as everywhere. By kind (board 08) is where artifacts shrink to wristbands and chips, because there they are counted; here each is read.'),
                 ]), w=600)])
    html = (HEAD19 + f'<div style="width: 1860px; min-height: {hh("09", 3800)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('09 &middot; THE COLLECTION, OVER TIME', 'The same collections, read as a timeline',
                   'Board 08&rsquo;s grammar and parts, arranged on one spine instead of by kind: dates on the left, seasons as sections, each thing hanging off its date in its own form and saying whether it was added or lived, gaps drawn as dashed spine. '
                   'A switch in the masthead moves between the two readings. Drawn, not tested with anyone.')
            + r1 + r2 + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('09 - The collection over time', html)

if __name__ == '__main__':
    build()
