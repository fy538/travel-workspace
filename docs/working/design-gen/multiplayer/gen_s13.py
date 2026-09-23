"""19 · The container as a timeline. The same collections as board 18, in the same Life grammar, read over time
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
def switch(active='OVER TIME'):
    def c(t):
        on = t == active
        return (f'<span style="height:26px; border-radius:13px; display:inline-flex; align-items:center; padding:0 12px; font-family:var(--mono); font-size:9.5px; font-weight:700; letter-spacing:1.1px; '
                f'color:{"var(--ink)" if on else "var(--mute)"}; border:{"1.3px solid var(--ink)" if on else "1px solid var(--hairline)"}; background:{"var(--card)" if on else "transparent"};">{t}</span>')
    return f'<div style="margin:16px 22px 0 22px; display:flex; gap:6px;">{c("BY KIND")}{c("OVER TIME")}</div>'

# ── the spine ──
def season(t, span): return (f'<div style="margin:28px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;">'
                             f'<span class="kicker" style="color:var(--mute);">{t}</span><span class="barmeta" style="margin-left:auto;">{span}</span></div>')
def entry(date, body, meta='', dot='solid', first=False, last=False):
    """One thing on the spine: its date, a dot, and the thing in its own form."""
    top = '10px' if first else '0'
    bottom = 'calc(100% - 14px)' if last else '0'
    dotcss = {'solid': 'background:var(--ink);', 'hollow': 'background:var(--paper); border:1.3px solid var(--ink); box-sizing:border-box;',
              'gold': 'background:var(--gold);', 'green': 'background:var(--green);'}[dot]
    m = f'<div class="meta" style="margin-top:6px; white-space:normal;">{meta}</div>' if meta else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:stretch;">'
            f'<div style="width:42px; flex:none; padding-top:9px; text-align:right; font-family:var(--mono); font-size:9.5px; font-weight:500; letter-spacing:0.6px; color:var(--mute); line-height:13px;">{date}</div>'
            f'<div style="width:22px; flex:none; position:relative;"><span style="position:absolute; left:10px; top:{top}; bottom:{bottom}; width:1px; background:var(--hairline);"></span>'
            f'<span style="position:absolute; left:7px; top:11px; width:7px; height:7px; border-radius:4px; {dotcss}"></span></div>'
            f'<div style="flex:1; min-width:0; padding:6px 0 20px 4px;">{body}{m}</div></div>')
def quiet(t):
    """A quiet stretch: the spine goes on, dashed, and says how long."""
    return (f'<div style="margin:0 22px; display:flex; align-items:stretch;"><div style="width:42px; flex:none;"></div>'
            f'<div style="width:22px; flex:none; position:relative;"><span style="position:absolute; left:10px; top:0; bottom:0; width:0; border-left:1.2px dashed rgba(27,23,20,0.22);"></span></div>'
            f'<div style="flex:1; padding:14px 0 22px 4px;"><span class="voice" style="font-size:15px;">{t}</span></div></div>')
def now_line():
    return (f'<div style="margin:6px 22px 4px 22px; display:flex; align-items:center; gap:10px;"><span style="font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:1.2px; color:var(--gold-deep); width:42px; text-align:right;">NOW</span>'
            f'<span style="flex:1; height:1px; background:rgba(176,133,58,0.55);"></span></div>')

# ── bodies, each in its own form ──
def title_(t): return f'<div style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{t}</div>'
def words(t): return f'<div style="font-family:var(--sans); font-size:15px; line-height:21px; margin-top:4px;">{t}</div>'
def strip(n, start=0): return '<div style="display:flex; gap:5px; margin-top:8px;">' + ''.join(K.riso(start + i, 52) for i in range(n)) + '</div>'
def reply(who, t): return f'<div style="margin-top:8px; border-left:2px solid rgba(27,23,20,0.12); padding-left:10px; font-size:14px; line-height:19px; color:var(--mute);"><span style="color:var(--ink); font-weight:600;">{who}</span> {t}</div>'
def place(name, where, been=None):
    b = f'<span class="meta" style="margin-left:auto; color:var(--green);">BEEN &middot; {been}</span>' if been else ''
    return f'<div style="display:flex; align-items:baseline; gap:8px;"><span style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{name}</span>{b}</div><div class="rsub" style="margin-top:2px;">{where}</div>'
def open_q(t): return f'<div style="border-left:2px solid rgba(176,133,58,0.45); padding-left:12px;"><span style="font-size:14.5px; line-height:20px;">{t}</span><div style="margin-top:4px;"><span class="vdl-door vk-t-bodySmMedium">Ask about this</span></div></div>'
def bands(*ts): return '<div style="display:flex; gap:7px; flex-wrap:wrap;">' + ''.join(K.band(t) for t in ts) + '</div>'

# ── 1 · Our New York, over time ──
def ny():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += switch()
    inner += season('AUTUMN 2026', 'SEPT &mdash; OCT')
    inner += entry('OCT<br>20', title_('The pier at low water') + words('for when one of us needs to walk it off') + strip(2), 'NORA &middot; A PLACE, TWO PHOTOGRAPHS', first=True)
    inner += entry('OCT<br>5', place('Hato', 'Cobble Hill &middot; ramen', 'OCT 12') + words('the broth is stupid good') + reply('Sam', 'the queue at 8 is a war crime'), 'MAYA &middot; A PLACE')
    inner += entry('SEPT<br>26', bands('JOHN SUMMIT') + words('pacha. unreal. my ears are still ringing'), 'NORA, WITH MAYA &middot; A NIGHT')
    inner += entry('SEPT<br>18', title_('The Lantern') + words('one film a week and exactly one kind of cake'), 'SAM &middot; A LINK')
    inner += entry('SEPT<br>6', f'<div style="font-family:var(--serif); font-size:18px; line-height:25px;">the thing nobody tells you about the greenmarket is that bread goes first</div>', 'PRIYA &middot; A NOTE', last=True)
    inner += season('SUMMER 2026', 'JUN &mdash; AUG')
    inner += entry('JUL<br>5', title_('The greenmarket, first Saturday') + strip(3, 2), 'PRIYA &middot; THREE PHOTOGRAPHS', first=True, last=True)
    inner += L6.door('The first thing, in June')
    return L6.phone(inner)

# ── 2 · Nights out, over time ──
def nights():
    inner = L6.head('KEPT &middot; WITH SAM &middot; SINCE JUNE 2025', 'Nights out', 'Five wristbands &mdash; a rhythm more than a plan.')
    inner += switch()
    inner += season('AHEAD', '1')
    inner += entry('SAT', bands('OVERMONO') + words('the warehouse. doors at 11'), 'UPCOMING &middot; SAM HAS TICKETS', dot='hollow', first=True, last=True)
    inner += now_line()
    inner += season('THIS YEAR', '3 NIGHTS')
    inner += entry('SEPT<br>26', f'<div>{S.ticket_row()}</div>' + words('pacha. unreal.') + strip(3), 'YOU AND SAM &middot; ADMISSION, THREE PHOTOGRAPHS', first=True)
    inner += entry('MAY<br>16', bands('CARIBOU') + words('the same door, again'), 'SAM')
    inner += entry('MAY<br>16', f'<div style="display:flex;">{K.chip(L6.GLASS, "Ottavia")}</div>' + words('before the show'), 'YOU &middot; A PLACE', last=True)
    inner += season('2025', '1 NIGHT')
    inner += entry('JUN<br>2025', bands('FOUR TET') + words('the first night, at the Mirage'), 'SAM', first=True, last=True)
    inner += L6.voice('Twice at the same door &mdash; the record noticed.')
    return L6.phone(inner)

# ── 3 · Getting pasta right, over time ──
def pasta():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE AUG 17', 'Getting pasta right', 'Three attempts &mdash; one question still open.')
    inner += switch()
    inner += season('SEPTEMBER', '1')
    inner += entry('SEPT<br>2', title_('Attempt three') + words('held together. still bland') + strip(1, 2), 'A PHOTOGRAPH AND A NOTE', first=True, last=True)
    inner += season('AUGUST', '5')
    inner += entry('AUG<br>30', open_q('Why does it split? The cheese goes in off the heat, apparently.'), 'A QUESTION YOU KEPT &middot; OPEN', dot='gold', first=True)
    inner += entry('AUG<br>28', title_('Attempt two') + words('split again'), 'A NOTE')
    inner += entry('AUG<br>24', title_('Attempt one') + words('cheese went in over the flame') + strip(1, 4), 'A PHOTOGRAPH AND A NOTE')
    inner += entry('AUG<br>18', f'<div style="display:flex;">{K.chip(K.MENU, "THE MENU &middot; SORRENTO")}</div>', 'KEPT FROM YOUR TRIP')
    inner += entry('AUG<br>17', title_('The plate in Sorrento') + words('where this started') + strip(1), 'NICE &rarr; ROME &middot; A PHOTOGRAPH', last=True)
    inner += K.doors2('Add something', 'Ask Maya in')
    return L6.phone(inner)

# ── 4 · quiet, then a return ──
def returned():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Thirteen things &mdash; back after the winter.')
    inner += switch()
    inner += season('WINTER', 'FEB')
    inner += entry('FEB<br>2', title_('Jo&rsquo;s weekend') + words('three from here, sent to jo: hato, the lantern, the pier') + reply('Maya', 'tell her to go at 6'), 'NORA &middot; SENT FROM THIS COLLECTION', first=True, last=True)
    inner += quiet('Quiet &middot; four months. Nothing was asked of anyone.')
    inner += season('AUTUMN 2026', 'SEPT &mdash; OCT')
    inner += entry('OCT<br>20', title_('The pier at low water') + strip(2), 'NORA &middot; A PLACE', first=True)
    inner += entry('OCT<br>5', place('Hato', 'Cobble Hill &middot; ramen', 'OCT 12'), 'MAYA &middot; A PLACE', last=True)
    inner += L6.door('All thirteen')
    return L6.phone(inner)

# ── 5 · a single night, as its own kept thing ──
def one_night():
    inner = L6.head('KEPT &middot; WITH MAYA &middot; ONE NIGHT', 'Pacha, John Summit', 'Friday into Saturday &mdash; the two of you.')
    inner += switch()
    inner += f'<div style="margin:18px 22px 0 22px;">{S.ticket_full()}</div>'
    inner += season('THE NIGHT', 'SEPT 26 &mdash; 27')
    inner += entry('10:38<br>PM', words('pacha tonight. john summit. on at 1') , 'SAM, TO FRIENDS &middot; WHERE IT CAME FROM', first=True)
    inner += entry('12:30<br>AM', title_('Maya at yours') + words('wearing the boots, don&rsquo;t laugh'), 'MAYA &middot; FROM YOUR CHAT')
    inner += entry('1:00<br>AM', bands('JOHN SUMMIT') + strip(4), 'ON &middot; FOUR PHOTOGRAPHS, TWO OF THEM MAYA&rsquo;S')
    inner += entry('3:40<br>AM', words('home. that was unreal') + f'<div class="rsub" style="margin-top:4px;">Cab back, split &middot; $31 each</div>', 'MAYA', last=True)
    inner += L6.voice('Kept by both of you.')
    return L6.phone(inner)

def cell(k, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap('', k, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('1', 'Our New York, over time', 'The same twelve things as board 18, on one spine. Seasons are the sections; each thing hangs off its date in its own form: photographs as a small strip, a night as its wristband, a note as serif words, a reply under the thing it answers.', ny(), (LIFE, P('SHARED'), P('TIMELINE'))),
                 cell('2', 'Nights out, over time', 'The next night sits above a gold NOW line with a hollow dot. Below it, the nights as they happened: a ticket, a wristband, a place before the show, the first night a year back.', nights(), (LIFE, P('SHARED'), P('TIMELINE'))),
                 cell('3', 'Getting pasta right, over time', 'Read bottom to top, it is the story: the plate in Sorrento, the kept menu, three attempts, and the open question marked gold.', pasta(), (LIFE, P('PRIVATE'), P('TIMELINE'))),
                 cell('4', 'Quiet, then back', 'Four months with nothing, drawn as a dashed length of spine with one italic line. Then February, when it was useful again.', returned(), (LIFE, P('SHARED'), P('QUIET')))], top=20)
    r2 = rowdiv([cell('5', 'One night, kept on its own', 'The rave as a kept thing: the admission at the top, then the night by the hour, from Sam&rsquo;s share to the cab home. Times replace dates on the spine.', one_night(), (LIFE, P('SHARED'), P('ONE NIGHT'))),
                 cell('18', 'The same collection, by kind', 'Board 18&rsquo;s version, for comparison. The switch moves between the two; neither is the default everywhere.', K.our_ny(), (LIFE, P('BOARD 18'))),
                 notes('WHEN TIME, WHEN KIND', led([
                     ('THE SWITCH', 'By kind and Over time are two readings of the same collection, in Life&rsquo;s lens-chip style under the masthead. Nothing moves between them; nothing is filed twice.'),
                     ('OVER TIME SUITS', 'A night, a trip, an exploration, anything with a story or a rhythm: Nights out, Getting pasta right, one evening.'),
                     ('BY KIND SUITS', 'Anything used as a reference: Restaurants to try, Our places, a list you consult rather than reread.'),
                     ('THE SPINE', 'Dates in mono on the left, one hairline, a dot per thing. Seasons are the section heads, with counts. Hollow dot and a gold NOW line for what is ahead; a gold dot for something still open.'),
                     ('QUIET IS DRAWN', 'A long gap is a dashed length of spine and one italic line, not an empty space and not a prompt.'),
                     ('SAME PARTS AS 18', 'Masthead, wristbands, the ticket, riso photographs, a friend&rsquo;s words, a been mark. Only the arrangement changes.'),
                 ]), w=600)])
    html = (HEAD19 + f'<div style="width: 1860px; min-height: {hh("19", 3800)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('19 &middot; THE CONTAINER, OVER TIME', 'The same collections, read as a timeline',
                   'Board 18&rsquo;s grammar and parts, arranged on one spine instead of by kind: dates on the left, seasons as sections, each thing hanging off its date in its own form, quiet stretches drawn as dashed spine. '
                   'A switch in the masthead moves between the two readings. Drawn, not tested with anyone.')
            + r1 + r2 + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('19 - The container over time', html)

if __name__ == '__main__':
    build()
