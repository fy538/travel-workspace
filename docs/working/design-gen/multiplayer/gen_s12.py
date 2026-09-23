"""18c · The container, in Life's grammar. A kept collection opens the way every held thing in Life opens (Life 03):
a masthead that speaks once, then only the sections it can honestly fill. The drawer holds typed originals (wristbands,
tickets, a menu); the contact sheet holds small photographs; things are rows with riso thumbnails; conversations,
people and places are rows with counts. Life's stylesheet and row/chip/tile markup are lifted from Life 03/07."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
import gen_s6 as L6
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD18 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)

# ── Life's small parts, as Life draws them ──
RISO = ['<circle cx="44" cy="16" r="9" fill="#C4604F" opacity="0.65"/><rect y="34" width="62" height="28" fill="#4E7A6F" opacity="0.5"/>',
        '<circle cx="31" cy="31" r="16" stroke="#C4604F" stroke-width="2.5" fill="none" opacity="0.7"/><path d="M22 34 Q31 24 42 32" stroke="#4E7A6F" stroke-width="2.5" fill="none" opacity="0.65"/>',
        '<path d="M10 52 L30 16 L50 52 Z" fill="#4E7A6F" opacity="0.45"/><circle cx="48" cy="14" r="6" fill="#C4604F" opacity="0.7"/>',
        '<rect x="12" y="12" width="20" height="38" rx="2" fill="#C4604F" opacity="0.55"/><rect x="36" y="22" width="16" height="28" rx="2" fill="#4E7A6F" opacity="0.5"/>',
        '<path d="M6 40 Q20 24 31 36 T56 34" stroke="#4E7A6F" stroke-width="3" fill="none" opacity="0.6"/><circle cx="18" cy="18" r="7" fill="#C4604F" opacity="0.6"/>',
        '<rect x="10" y="30" width="42" height="18" rx="2" fill="#4E7A6F" opacity="0.45"/><circle cx="20" cy="18" r="6" fill="#C4604F" opacity="0.65"/><circle cx="40" cy="18" r="6" fill="#C4604F" opacity="0.65"/>']
def riso(i, size=62, r=4):
    return (f'<div style="width:{size}px; height:{size}px; border-radius:{r}px; overflow:hidden; border:1px solid var(--hairline); flex:none;">'
            f'<svg width="{size}" height="{size}" viewBox="0 0 62 62" style="display:block;"><rect width="62" height="62" fill="#F6F1E4"/>{RISO[i % len(RISO)]}</svg></div>')
def sheet(n_show, total):
    tiles = ''.join(riso(i) for i in range(n_show))
    more = f'<div style="width:62px; height:62px; border-radius:4px; border:1px solid var(--hairline); background:var(--card); display:flex; align-items:center; justify-content:center; font-family:var(--mono); font-size:10px; font-weight:700; color:var(--ink);">+{total - n_show}</div>' if total > n_show else ''
    return f'<div style="margin:14px 22px 0 22px; display:flex; gap:6px; flex-wrap:wrap;">{tiles}{more}</div>'
def chip(glyph, t):
    return (f'<div style="height:32px; border-radius:16px; background:var(--card); border:1px solid var(--hairline); display:inline-flex; align-items:center; gap:7px; padding:0 13px; flex:none; box-sizing:border-box; box-shadow:0 1px 3px rgba(27,23,20,0.06);">'
            f'{glyph}<span style="font-family:var(--mono); font-size:9.5px; font-weight:700; letter-spacing:0.7px; color:var(--ink); white-space:nowrap;">{t}</span></div>')
def band(t, upcoming=False):
    """A wristband: the dark band with notches, as Life 03 draws a night out."""
    dot = '<span style="width:6px; height:6px; border-radius:3px; border:1.2px solid rgba(244,238,221,0.8); margin-left:6px;"></span>' if upcoming else ''
    return (f'<div class="band" style="height:32px; flex:none;"><span class="bandnotch" style="left:-5px; top:11px;"></span><span class="bandnotch" style="right:-5px; top:11px;"></span>'
            f'<span style="font-family:var(--mono); font-size:9.5px; font-weight:700; letter-spacing:0.9px; color:#F4EEDD; white-space:nowrap;">{t}</span>{dot}</div>')
def drawer(items): return f'<div style="margin:14px 22px 0 22px; display:flex; gap:7px; flex-wrap:wrap;">{"".join(items)}</div>'
def thing(i, text, meta, color=None):
    """A kept thing as Life's moment row: riso thumbnail, serif words, a date."""
    mc = f' style="color:{color};"' if color else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:52px; border-bottom:1px solid var(--hair-thin);">{riso(i, 44)}'
            f'<span class="child" style="flex-grow:1;">{text}</span><span class="meta"{mc}>{meta}</span>{L6.CHEV}</div>')
def opens(t): return f'<div style="margin:12px 22px 0 22px; border-left:2px solid rgba(176,133,58,0.45); padding-left:12px;"><span style="font-family:var(--serif); font-size:16.5px; line-height:21px; font-weight:600;">{t}</span></div>'
def left(t, doorlabel=None):
    d = f'<div style="display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium">{doorlabel}</span></div>' if doorlabel else ''
    return f'<div style="margin:14px 22px 0 22px; border-left:2px solid rgba(176,133,58,0.45); padding-left:12px; display:flex; flex-direction:column; gap:5px;"><span style="font-size:14px; line-height:19px;">{t}</span>{d}</div>'
def sources(t): return f'<div style="margin:12px 22px 0 22px;"><span style="font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:0.7px; color:var(--mute); line-height:17px;">{t}</span></div>'
def doors2(*ts): return '<div style="margin:22px 22px 0 22px; display:flex; gap:18px;">' + ''.join(f'<span class="vdl-door vk-t-bodySmMedium">{t}</span>' for t in ts) + '</div>'
PLANE = L6.G('M1.8 8.6 L13.2 3.4 L9.8 8.2 L11.4 12 L9.6 12.4 L7.4 9.2 L3.6 10.4 Z')
LINKG = L6.G('M6 9 a2.5 2.5 0 0 1 0-3.5 l2-2 a2.5 2.5 0 0 1 3.5 3.5 l-1 1 M9 6 a2.5 2.5 0 0 1 0 3.5 l-2 2 a2.5 2.5 0 0 1-3.5-3.5 l1-1')
MENU = L6.G('M3 2.2 H12 V12.8 H3 Z M5 5.2 H10 M5 7.6 H10 M5 10 H8')

# ── 1 · Our New York: mixed, shared ──
def our_ny():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += L6.sec('THE THINGS', '12 KEPT', 26)
    inner += thing(0, 'The pier at low water &middot; walk it off', 'OCT 20')
    inner += thing(3, 'Hato &middot; the broth is stupid good', 'OCT 5')
    inner += thing(1, 'The Lantern &middot; one film a week', 'SEPT 18')
    inner += thing(5, 'The greenmarket &middot; bread goes first', 'SEPT 6')
    inner += L6.door('All twelve')
    inner += L6.sec('THE DRAWER', '3 KEPT')
    inner += drawer([band('JOHN SUMMIT'), chip(L6.FORK, 'HATO'), chip(LINKG, 'THE LANTERN')])
    inner += L6.sec('THE CONTACT SHEET', '9 PHOTOS')
    inner += sheet(4, 9)
    inner += L6.sec('THE CONVERSATION', '1 THREAD')
    inner += L6.row1(L6.BUBBLE, 'The queue at 8 &middot; Sam and Maya', '2 MSGS')
    inner += L6.sec('THE PEOPLE', '3')
    inner += L6.row2('Maya, Sam, Priya', 'Nobody counted; Dana is in this and has added nothing', 'PEOPLE')
    inner += L6.sec('THE PLACES', '8 HELD')
    inner += L6.row2('Brooklyn, mostly', 'Cobble Hill, Carroll Gardens, Red Hook', 'MAP')
    inner += L6.voice('Uneven, unhurried, and in each other&rsquo;s words.')
    return L6.phone(inner)

# ── 2 · Nights out: the drawer leads ──
def nights():
    inner = L6.head('KEPT &middot; WITH SAM &middot; SINCE JUNE', 'Nights out', 'Five wristbands &mdash; a rhythm more than a plan.')
    inner += L6.sec('THE DRAWER', '5 KEPT', 26)
    inner += drawer([band('FOUR TET'), band('CARIBOU'), band('JOHN SUMMIT'), band('OVERMONO', upcoming=True), chip(L6.GLASS, 'Ottavia')])
    inner += f'<div style="margin:14px 22px 0 22px;">{S.ticket_full()}</div>'
    inner += L6.sec('THE NIGHTS', '5')
    inner += L6.row1(L6.GLASS, 'John Summit &middot; Pacha, the two of you', 'SEPT 26')
    inner += L6.row1(L6.GLASS, 'Caribou &middot; the same door, again', 'MAY')
    inner += L6.row1(L6.GLASS, 'Four Tet &middot; the first night, at the Mirage', 'JUN 2025')
    inner += L6.row1(L6.GLASS, 'Overmono &middot; Saturday, the warehouse', 'UPCOMING', 'var(--green)')
    inner += L6.sec('THE CONTACT SHEET', '11 PHOTOS')
    inner += sheet(4, 11)
    inner += L6.voice('Twice at the same door &mdash; the record noticed.')
    return L6.phone(inner)

# ── 3 · Getting pasta right: an exploration ──
def pasta():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE AUG 17', 'Getting pasta right', 'Three attempts &mdash; one question still open.')
    inner += L6.sec('THE ATTEMPTS', '3', 26)
    inner += thing(2, 'Attempt three &middot; held together, still bland', 'SEPT 2')
    inner += thing(4, 'Attempt two &middot; split again', 'AUG 28')
    inner += thing(1, 'Attempt one &middot; cheese went in over the flame', 'AUG 24')
    inner += L6.sec('THE QUESTION', 'OPEN')
    inner += left('Why does it split? The cheese goes in off the heat, apparently &mdash; kept Aug 30, not yet settled.', 'Ask about this')
    inner += L6.sec('THE DRAWER', '1 KEPT')
    inner += drawer([chip(MENU, 'THE MENU &middot; SORRENTO')])
    inner += L6.sec('WHERE IT STARTED')
    inner += L6.row1(PLANE, 'The plate in Sorrento &middot; Nice &rarr; Rome', 'AUG 17')
    inner += L6.sec('THE SOURCES')
    inner += sources('3 PHOTOGRAPHS (YOUR CAMERA) &middot; 1 MENU &middot; 1 QUESTION YOU KEPT')
    inner += doors2('Add something', 'Ask Maya in')
    return L6.phone(inner)

# ── 4 · Interesting stuff: three things, nothing else ──
def stuff():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE SEPT 8', 'Interesting stuff', 'Three things &mdash; no two alike.')
    inner += L6.sec('THE THINGS', '3 KEPT', 26)
    inner += thing(0, 'The blue room at the Frick &middot; the light at four', 'SEPT 19')
    inner += thing(5, 'Sourdough, the cold rise &middot; a method to try', 'OCT 2')
    inner += thing(1, 'The Lantern &middot; from Sam', 'SEPT 8')
    inner += L6.sec('THE SOURCES')
    inner += sources('1 PHOTOGRAPH (YOUR CAMERA) &middot; 2 LINKS')
    inner += L6.voice('Nothing here needs you.')
    return L6.phone(inner)

# ── 5 · one thing ──
def one():
    inner = L6.head('KEPT &middot; YOURS ALONE', 'Things for Jo&rsquo;s visit', 'One thing so far.')
    inner += L6.sec('THE THINGS', '1 KEPT', 26)
    inner += thing(3, 'Hato &middot; the broth is stupid good', 'FROM MAYA')
    inner += doors2('Add anything')
    return L6.phone(inner)

# ── 6 · Our places: the map inside the record (Life P4) ──
def places():
    inner = L6.head('KEPT &middot; WITH MAYA &middot; SINCE SEPT 30', 'Our places', 'Five places &mdash; three been to together.')
    inner += f'<div style="margin:22px 22px 0 22px; border-radius:8px; overflow:hidden; border:1px solid var(--hairline);">{S.paper_map(150, ((0.18, 0.62), (0.36, 0.36), (0.56, 0.66), (0.72, 0.42), (0.86, 0.7)), 349)}</div>'
    inner += L6.sec('THE PLACES', '5 HELD', 26)
    inner += L6.row2('Hato', 'the broth is stupid good &middot; Maya', 'BEEN &middot; OCT 12', 'var(--green)', L6.FORK)
    inner += L6.row2('Lulu&rsquo;s', 'upstairs. priya swears by it &middot; you', 'BEEN &middot; OCT 12', 'var(--green)', L6.FORK)
    inner += L6.row2('The pier at low water', 'for when one of us needs to walk it off &middot; you', 'OCT 20', None, L6.WAVE)
    inner += L6.door('All five')
    inner += L6.sec('THE CONTACT SHEET', '7 PHOTOS')
    inner += sheet(3, 7)
    inner += L6.voice('Your places, and hers &mdash; one map.')
    return L6.phone(inner)

def cell(k, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap('', k, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')

def build():
    r1 = rowdiv([cell('1', 'Our New York', 'Mixed and shared. Masthead, the things as rows, the drawer (a wristband, a place, a link), the contact sheet, one conversation, the people, the places, a voice line.', our_ny(), (LIFE, P('SHARED'), P('MIXED'))),
                 cell('2', 'Nights out', 'The drawer leads because the artifacts are the point: wristbands as bands, the John Summit admission at full size, the nights as rows.', nights(), (LIFE, P('SHARED'), P('ARTIFACTS'))),
                 cell('3', 'Getting pasta right', 'An exploration: attempts as rows, the open question in Life&rsquo;s carried-forward style, one kept menu, where it started, the sources.', pasta(), (LIFE, P('PRIVATE'))),
                 cell('4', 'Interesting stuff', 'Three unlike things. Only the sections that exist: the things, the sources, a voice line.', stuff(), (LIFE, P('PRIVATE')))], top=20)
    r2 = rowdiv([cell('5', 'One thing', 'The masthead, one row, and a door. Nothing else pretends to be there.', one(), (LIFE, P('PRIVATE'))),
                 cell('6', 'Our places', 'The map inside the record, as Life P4 rules; places with their adder&rsquo;s words and a green been.', places(), (LIFE, P('SHARED'))),
                 notes('WHY THIS', led([
                     ('IT IS LIFE', 'A kept collection is a held thing; it opens the way Life 03 opens a journey, a place, a shared record or an evening: a masthead that speaks once, then only the sections it can fill.'),
                     ('ARTIFACTS ARE THE PICTURES', 'Wristbands, tickets, a menu, a place: typed originals in the drawer carry the page. Photographs are small, in a contact sheet, as Life keeps them.'),
                     ('ROWS, NOT CARDS', 'A thing is a riso thumbnail, serif words and a date. No boxes; hairlines between sections only.'),
                     ('COUNTS, NOT BADGES', 'Every section says how many, in mono, right-aligned. That is the only number on the page.'),
                     ('SHARED = A MASTHEAD LINE', '&ldquo;With Maya, Sam and Priya&rdquo; in the kicker, and a People section. Nothing else changes.'),
                     ('ONE VOICE LINE', 'Italic, once, at the end, and only when the record noticed something.'),
                 ]), w=600)])
    html = (HEAD18 + f'<div style="width: 1860px; min-height: {hh("18", 3600)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('18 &middot; THE CONTAINER', 'A kept collection opens like everything else in Life',
                   'Editorial, as the Life project is: a masthead, sections with counts, a drawer of typed originals, a contact sheet of small photographs, rows with riso thumbnails, one italic line. '
                   'Drawn with Life 03 and 07&rsquo;s stylesheet and parts. Accepted 2026-09-22; the earlier card-based versions are in archive/.')
            + r1 + r2 + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('18 - The container', html)

if __name__ == '__main__':
    build()
