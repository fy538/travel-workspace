"""12 · Cards. How a shared place (and a shared link) looks inside a share, on the timeline, and as a link, drawn four
ways so the founder can pick by eye: the card we have (a generic link preview), A the house card (an artifact in the
ticket's family), B a line (Life's row grammar, no box), C the map as the picture. All three alternatives drop the
fake thumbnail (Entity lab ruling: a photo or nothing) and the live hours, and set the sender's "good for" as words."""
import re
from mp_kit2 import *
import gen_s1 as S
import gen_s2 as S2
import gen_s6 as L6
import gen_s12 as K
import gen_s13 as T

LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEADC = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)
PAPER, INK2_, MUTE_ = '#FBF7EC', '#3A332C', '#6E6862'
EDGE = {'red': 'rgba(196,96,79,0.78)', 'green': 'rgba(78,122,111,0.72)', 'gold': 'rgba(176,133,58,0.75)'}
PIN = L6.G('M7.5 13.5 C4 10 3 8 3 6.2 A4.5 4.5 0 0 1 12 6.2 C12 8 11 10 7.5 13.5 Z M7.5 7.6 a1.4 1.4 0 1 0 0.01 0')
LINK = K.LINKG

# ── A · the house card: a place as an object, in the ticket's family ──
def house(name, where, good, edge='red'):
    """Sleeker (2026-09-25, after the founder preferred B's restraint): hairline paper, a thin colour spine, no shadow,
    no perforation; the name one size down; the reason under a single hairline."""
    return (f'<div style="background:{PAPER}; border-radius:6px; border:1px solid rgba(27,23,20,0.12); border-left:3px solid {EDGE[edge]}; padding:12px 16px 13px 15px;">'
            f'<div style="display:flex; align-items:center; gap:6px;">{PIN}<span style="font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:1.3px; color:{MUTE_}; text-transform:uppercase;">{where}</span></div>'
            f'<div style="font-family:var(--serif); font-size:23px; line-height:28px; font-weight:600; letter-spacing:-0.3px; margin-top:5px;">{name}</div>'
            f'<div style="margin-top:9px; padding-top:8px; border-top:1px solid rgba(27,23,20,0.10); font-family:var(--serif); font-size:16px; line-height:22px; color:{INK2_};">{good}</div></div>')
def clipping(source, headline, line):
    return (f'<div style="background:{PAPER}; border-radius:6px; border:1px solid rgba(27,23,20,0.12); border-left:3px solid rgba(27,23,20,0.55); padding:12px 16px 13px 15px;">'
            f'<div style="display:flex; align-items:center; gap:6px;">{LINK}<span style="font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:1.3px; color:{MUTE_}; text-transform:uppercase;">{source}</span></div>'
            f'<div style="font-family:var(--serif); font-size:19px; line-height:24px; font-weight:600; margin-top:5px;">{headline}</div>'
            f'<div style="margin-top:9px; padding-top:8px; border-top:1px solid rgba(27,23,20,0.10); font-family:var(--serif); font-size:16px; line-height:22px; color:{INK2_};">{line}</div></div>')

# ── B · a line: Life's row, no box ──
def line_place(name, where, good):
    return (f'<div style="border-top:1px solid rgba(27,23,20,0.12); border-bottom:1px solid rgba(27,23,20,0.12); padding:11px 0; display:flex; gap:11px; align-items:flex-start;">'
            f'<div style="padding-top:4px;">{PIN}</div><div style="flex:1; min-width:0;">'
            f'<div style="display:flex; align-items:baseline; gap:8px; flex-wrap:wrap;"><span style="font-family:var(--serif); font-size:19px; line-height:24px; font-weight:600;">{name}</span><span class="rsub">{where}</span></div>'
            f'<div style="font-family:var(--serif); font-size:16px; line-height:22px; color:{INK2_}; margin-top:2px;">{good}</div></div>'
            f'<div style="padding-top:6px;">{L6.CHEV}</div></div>')
def line_link(source, headline):
    return (f'<div style="border-top:1px solid rgba(27,23,20,0.12); border-bottom:1px solid rgba(27,23,20,0.12); padding:11px 0; display:flex; gap:11px; align-items:flex-start;">'
            f'<div style="padding-top:4px;">{LINK}</div><div style="flex:1; min-width:0;">'
            f'<div style="font-family:var(--serif); font-size:18px; line-height:23px; font-weight:600;">{headline}</div><div class="rsub" style="margin-top:2px;">{source}</div></div>'
            f'<div style="padding-top:6px;">{L6.CHEV}</div></div>')

# ── C · the map is the picture ──
def map_place(name, where, good, x=0.46, y=0.62):
    w, h = 349, 118
    label = (f'<div style="position:absolute; left:{x*w + 12:.0f}px; top:{y*h - 30:.0f}px; background:{PAPER}; border:1px solid rgba(27,23,20,0.14); border-radius:4px; padding:2px 7px; '
             f'font-family:var(--serif); font-size:14px; line-height:18px; font-weight:600; white-space:nowrap;">{name}</div>')
    return (f'<div><div style="position:relative; border-radius:8px; overflow:hidden; border:1px solid rgba(27,23,20,0.12);">{S.paper_map(h, ((x, y),), w)}{label}</div>'
            f'<div style="display:flex; align-items:baseline; gap:8px; margin-top:9px; flex-wrap:wrap;"><span style="font-family:var(--serif); font-size:19px; line-height:24px; font-weight:600;">{name}</span><span class="rsub">{where}</span></div>'
            f'<div style="font-family:var(--serif); font-size:16px; line-height:22px; color:{INK2_}; margin-top:2px;">{good}</div></div>')

LULU = ('Lulu&rsquo;s', 'Carroll Gardens &middot; Italian', 'Good for a long dinner, with parents.')
HATO = ('Hato', 'Cobble Hill &middot; ramen', 'Good for a cold night, the two of you.')
LANT = ('The Lantern&rsquo;s site &middot; Court Street', 'This week: one film, through Sunday', '7:15 nightly.')
WAYS = {
    'NOW': dict(place=lambda p, e: S.place_card_v0() if p is LULU else T.place_card_v0('Hato', 'Cobble Hill &middot; ramen', 'noodles', ('A cold night', 'Two of you'), 'OCT 12'),
                link=lambda: S.link_card_v0(), mini=False),
    'A': dict(place=lambda p, e: house(*p, edge=e), link=lambda: clipping(*LANT), mini=False),
    'B': dict(place=lambda p, e: line_place(*p), link=lambda: line_link(LANT[0], LANT[1]), mini=False),
    'C': dict(place=lambda p, e: map_place(*p), link=lambda: line_link(LANT[0], LANT[1]), mini=True),
}

# ── the three contexts ──
def crop(ph, h, off=0):
    return (f'<div style="width:393px; height:{h}px; overflow:hidden; position:relative; flex:none; border-radius:26px;">'
            f'<div style="margin-top:-{off}px;">{ph}</div>'
            f'<div style="position:absolute; left:0; right:0; bottom:0; height:70px; background:linear-gradient(rgba(216,209,197,0), #D8D1C5);"></div></div>')
def in_share(k):
    inner = anchor_row('NEW YORK', 'SUNDAY 9:44 PM')
    inner += gut(S.share('Priya', '9:40 PM · TO FRIENDS', S.LULU, extra=WAYS[k]['place'](LULU, 'red')), top=20)
    return crop(phone2(inner, active='Places'), 470)
def on_timeline(k):
    card = WAYS[k]['place'](HATO, 'green')
    if k != 'NOW': card = T.mini(card) if WAYS[k]['mini'] else card
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += K.switch('OVER TIME') + T.season('AUTUMN 2026', 'SEPT &mdash; OCT')
    inner += T.entry('OCT<br>5', T.words('the broth is stupid good') + f'<div style="margin-top:8px;">{card}</div>' + T.reply('Sam', 'the queue at 8 is a war crime'), 'MAYA &middot; A PLACE', first=True)
    return crop(L6.phone(inner), 470, 250)
def link_share(k):
    inner = anchor_row('NEW YORK', 'TUESDAY 8:12 PM')
    inner += gut(S.share('Sam', '7:40 PM · TO FRIENDS', 'this is the cinema. one film a week and exactly one kind of cake', extra=WAYS[k]['link']()), top=20)
    return crop(phone2(inner, active='Home'), 470)

def rowhead(k, title, sub):
    return (f'<div style="margin-top:44px; border-top:1.5px solid rgba(27,23,20,0.55); padding-top:12px; display:flex; gap:40px; align-items:baseline;">'
            f'<span style="font-family:var(--mono); font-size:11px; font-weight:700; letter-spacing:1.3px; color:#8A6628; width:60px; flex:none;">{k}</span>'
            f'<span style="font-family:var(--serif); font-size:24px; line-height:29px; font-weight:600; width:330px; flex:none;">{title}</span>'
            f'<span style="font-size:14px; line-height:20px; color:#3A332C; max-width:760px;">{sub}</span></div>')
def colheads():
    t = lambda s: f'<div style="width:393px; flex:none; font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1.3px; color:{MUTE_};">{s}</div>'
    return f'<div style="display:flex; gap:40px; margin-top:34px;">{t("A PLACE, INSIDE A SHARE")}{t("A PLACE, ON THE TIMELINE")}{t("A LINK, INSIDE A SHARE")}</div>'
def row(k):
    return f'<div style="display:flex; gap:40px; margin-top:16px;">{in_share(k)}{on_timeline(k)}{link_share(k)}</div>'

def build():
    rows = (rowhead('BEFORE', 'The card we had', 'A rounded box with a shadow, an abstract tile, a grey line with live hours, and the sender&rsquo;s reason as grey pills. The same shape as every app&rsquo;s link preview.') + row('NOW')
            + rowhead('A', 'The house card, sleeker', 'B&rsquo;s restraint with a little object to it: hairline paper, a thin colour spine, where in small capitals, the name, and the reason under one hairline. No shadow, no perforation. A link is the same card with an ink spine.') + row('A')
            + rowhead('B', 'A line &middot; chosen', 'No box at all: the pin, the name, where, and the reason underneath, between two hairlines, the way Life draws a place. A link is the same line with its headline.') + row('B')
            + rowhead('C', 'The map is the picture', 'A small paper map with the one pin, the name beside it, and the reason underneath. Honest when there is no photograph. Links have no map, so they fall back to B.') + row('C'))
    n = notes('WHAT CHANGES, IN ALL THREE', led([
        ('NO FAKE PICTURE', 'The abstract tile goes. A place shows a real photograph when the sender took one, and otherwise no picture (the Entity lab&rsquo;s ruling: a photo or nothing).'),
        ('THE REASON IS WORDS', '&ldquo;Good for a long dinner, with parents&rdquo; is why Priya shared it. It is set as a sentence, not as filter pills.'),
        ('NO LIVE FACTS', '&ldquo;Open till 11&rdquo; goes. Hours are Places&rsquo; job, on the place itself, where they can be current.'),
        ('TWO TYPEFACES, NOT FOUR', 'Serif for the name and the reason; small capitals or a grey line for where. No pills.'),
        ('ONE FAMILY', 'A: the ticket for a night, the house card for a place, the same card with an ink spine for a link. B: everything is a line, like Life&rsquo;s rows. C: places get a map, the rest are lines.'),
    ]), w=1260)
    html = (HEADC + f'<div style="width: 1356px; min-height: {hh("12", 2600)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 48px 36px 48px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('12 &middot; CARDS', 'A shared place, four ways',
                   'The card we had and three alternatives, each shown inside a share, on the timeline, and applied to a link. B, the line, was chosen on 2026-09-25 and now replaces the card on every board. Drawn, not tested with anyone.')
            + colheads() + rows + f'<div style="margin-top:44px;">{n}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('12 - Cards', html)

if __name__ == '__main__':
    build()
