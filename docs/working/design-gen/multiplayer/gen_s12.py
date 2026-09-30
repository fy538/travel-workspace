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
def question(q, t, meta):
    """A kept question, drawn like any other kept thing: the question as its name, what is known so far, a gold label while it is open."""
    return (f'<div style="margin:12px 22px 0 22px;"><div style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{q}</div>'
            f'<div style="font-family:var(--serif); font-size:16px; line-height:22px; margin-top:3px; color:#3A332C;">{t}</div>'
            f'<div class="meta" style="margin-top:6px; color:var(--gold-deep);">{meta}</div></div>')
def latest(i, title, words_, meta, who, said, when):
    """The newest contribution, first, with a friend's reply under it."""
    return (f'<div style="margin:12px 22px 0 22px; display:flex; gap:12px; align-items:flex-start;">{riso(i, 52)}<div style="flex:1; min-width:0;">'
            f'<div style="font-family:var(--serif); font-size:17px; line-height:22px; font-weight:600;">{title}</div>'
            f'<div style="font-family:var(--serif); font-size:16px; line-height:22px; color:#3A332C; margin-top:2px;">{words_}</div>'
            f'<div class="meta" style="margin-top:5px;">{meta}</div>'
            f'<div style="margin-top:10px; border-left:2px solid rgba(27,23,20,0.12); padding-left:10px;"><span style="font-family:var(--serif); font-size:15px; line-height:20px; font-weight:600;">{who}</span> '
            f'<span style="font-family:var(--serif); font-size:15px; line-height:20px; color:var(--mute);">{said}</span><div class="meta" style="margin-top:3px;">{when}</div></div>'
            f'<div style="margin-top:8px;"><span class="vdl-door vk-t-bodySmMedium">Reply</span></div></div></div>')
def sources(t): return f'<div style="margin:12px 22px 0 22px;"><span style="font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:0.7px; color:var(--mute); line-height:17px;">{t}</span></div>'
def switch(active, add=False):
    def c(t):
        on = t == active
        return (f'<span style="height:26px; border-radius:13px; display:inline-flex; align-items:center; padding:0 12px; font-family:var(--mono); font-size:9.5px; font-weight:700; letter-spacing:1.1px; '
                f'color:{"var(--ink)" if on else "var(--mute)"}; border:{"1.3px solid var(--ink)" if on else "1px solid var(--hairline)"}; background:{"var(--card)" if on else "transparent"};">{t}</span>')
    a = ('<span style="margin-left:auto; display:inline-flex; align-items:center; gap:5px; font-family:var(--sans); font-size:14px; font-weight:600; color:var(--gold-deep);">'
         '<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M6 1.5v9M1.5 6h9" stroke="#8A6628" stroke-width="1.6" stroke-linecap="round"/></svg>Add</span>') if add else ''
    return f'<div style="margin:16px 22px 0 22px; display:flex; gap:6px; align-items:center;">{c("BY KIND")}{c("OVER TIME")}{a}</div>'

def doors2(*ts): return '<div style="margin:22px 22px 0 22px; display:flex; gap:18px;">' + ''.join(f'<span class="vdl-door vk-t-bodySmMedium">{t}</span>' for t in ts) + '</div>'
PLANE = L6.G('M1.8 8.6 L13.2 3.4 L9.8 8.2 L11.4 12 L9.6 12.4 L7.4 9.2 L3.6 10.4 Z')
LINKG = L6.G('M6 9 a2.5 2.5 0 0 1 0-3.5 l2-2 a2.5 2.5 0 0 1 3.5 3.5 l-1 1 M9 6 a2.5 2.5 0 0 1 0 3.5 l-2 2 a2.5 2.5 0 0 1-3.5-3.5 l1-1')
MENU = L6.G('M3 2.2 H12 V12.8 H3 Z M5 5.2 H10 M5 7.6 H10 M5 10 H8')

# ── 1 · Our New York: mixed, shared ──
def our_ny():
    """Sept 26 (§12.3): shared and active. Add is apparent; the latest contribution leads, with Maya's reply; three
    sections, not six (people are in the masthead, replies sit on the thing, the map is a door)."""
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += switch('BY KIND', add=True)
    inner += L6.sec('LATEST', '', 26)
    inner += latest(0, 'The pier at low water', 'for when one of us needs to walk it off', 'YOU &middot; YESTERDAY &middot; TWO PHOTOGRAPHS',
                    'Maya', 'next low tide, i&rsquo;m in', 'THIS MORNING')
    inner += L6.sec('THE THINGS', '12')
    inner += thing(3, 'Hato &middot; the broth is stupid good', 'MAYA')
    inner += thing(1, 'The Lantern &middot; one film a week', 'SAM')
    inner += thing(5, 'The greenmarket &middot; bread goes first', 'PRIYA')
    inner += doors2('All twelve', 'On a map')
    inner += L6.sec('THE PHOTOGRAPHS', '9')
    inner += sheet(4, 9)
    return L6.phone(inner)
def nights():
    inner = L6.head('KEPT &middot; WITH SAM &middot; SINCE JUNE', 'Nights out', 'Five wristbands &mdash; a rhythm more than a plan.')
    inner += switch('BY KIND')
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
    return L6.phone(inner)

# ── 3 · Getting pasta right: an exploration ──
def pasta():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE AUG 17', 'Getting pasta right', 'Three attempts &mdash; one question still open.')
    inner += switch('BY KIND')
    inner += L6.sec('THE ATTEMPTS', '3', 26)
    inner += thing(2, 'Attempt three &middot; held together, still bland', 'SEPT 2')
    inner += thing(4, 'Attempt two &middot; split again', 'AUG 28')
    inner += thing(1, 'Attempt one &middot; cheese went in over the flame', 'AUG 24')
    inner += L6.sec('THE QUESTION', 'OPEN')
    inner += question('Why does it split?', 'the cheese goes in off the heat, apparently', 'KEPT AUG 30 &middot; STILL OPEN')
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
    inner += switch('BY KIND')
    inner += L6.sec('THE THINGS', '3 KEPT', 26)
    inner += thing(0, 'The blue room at the Frick &middot; the light at four', 'SEPT 19')
    inner += thing(5, 'Sourdough, the cold rise &middot; a method to try', 'OCT 2')
    inner += thing(1, 'The Lantern &middot; from Sam', 'SEPT 8')
    inner += L6.sec('THE SOURCES')
    inner += sources('1 PHOTOGRAPH (YOUR CAMERA) &middot; 2 LINKS')
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
    inner += switch('BY KIND')
    inner += f'<div style="margin:22px 22px 0 22px; border-radius:8px; overflow:hidden; border:1px solid var(--hairline);">{S.paper_map(150, ((0.18, 0.62), (0.36, 0.36), (0.56, 0.66), (0.72, 0.42), (0.86, 0.7)), 349)}</div>'
    inner += L6.sec('THE PLACES', '5 HELD', 26)
    inner += L6.row2('Hato', 'the broth is stupid good &middot; Maya', 'BEEN &middot; OCT 12', 'var(--green)', L6.FORK)
    inner += L6.row2('Lulu&rsquo;s', 'upstairs. priya swears by it &middot; you', 'BEEN &middot; OCT 12', 'var(--green)', L6.FORK)
    inner += L6.row2('The pier at low water', 'for when one of us needs to walk it off &middot; you', 'OCT 20', None, L6.WAVE)
    inner += L6.door('All five')
    inner += L6.sec('THE CONTACT SHEET', '7 PHOTOS')
    inner += sheet(3, 7)
    return L6.phone(inner)

def cell(k, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap('', k, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')

def build():
    r1 = rowdiv([cell('1', 'Our New York', 'Shared and active. A quiet + Add takes a photo, place, link or line. The latest addition leads, with Maya&rsquo;s reply; three sections, not six.', our_ny(), (LIFE, P('SHARED'), P('ACTIVE'))),
                 cell('2', 'Nights out', 'The drawer leads because the artifacts are the point: wristbands as bands, the John Summit admission at full size, the nights as rows.', nights(), (LIFE, P('SHARED'), P('ARTIFACTS'))),
                 cell('3', 'Getting pasta right', 'An exploration: attempts as rows, the open question drawn like any other thing, with a gold label, one kept menu, where it started, the sources.', pasta(), (LIFE, P('PRIVATE'))),
                 cell('4', 'Interesting stuff', 'Three unlike things. Only the sections that exist: the things and the sources.', stuff(), (LIFE, P('PRIVATE')))], top=20)
    r2 = rowdiv([cell('5', 'One thing', 'The masthead, one row, and a door. Nothing else pretends to be there, not even the switch: one thing has no order to change.', one(), (LIFE, P('PRIVATE'))),
                 cell('6', 'Our places', 'The map inside the record, as Life P4 rules; places with their adder&rsquo;s words and a green been.', places(), (LIFE, P('SHARED'))),
                 notes('WHY THIS', led([
                     ('TWO READINGS', 'By kind is one of two readings of a collection; Over time (board 09) is the other. A switch under the masthead moves between them, in Life&rsquo;s lens-chip style.'),
                     ('WHICH OPENS FIRST', 'Decided Sept 26: what is in it decides. Collections of dated things open Over time: Nights out, Getting pasta right, a trip, Our New York. Collections kept to consult open By kind: Our places, Restaurants to try, Interesting stuff. A collection of one has no switch.'),
                     ('REMEMBERED', 'Once someone switches, that collection opens their way from then on, for them only. In a shared collection each person keeps their own.'),
                     ('IT IS LIFE', 'A kept collection is a held thing; it opens the way Life 03 opens a journey, a place, a shared record or an evening: a masthead that speaks once, then only the sections it can fill.'),
                     ('ARTIFACTS ARE THE PICTURES', 'Wristbands, tickets, a menu, a place: typed originals in the drawer carry the page. Photographs sit in a contact sheet here; a collection that is mostly photographs can show them larger.'),
                     ('ROWS, NOT CARDS', 'A thing is a riso thumbnail, serif words and a date. No boxes; hairlines between sections only.'),
                     ('COUNTS, NOT BADGES', 'Every section says how many, in mono, right-aligned. That is the only number on the page.'),
                     ('SHARED = A MASTHEAD LINE', '&ldquo;With Maya, Sam and Priya&rdquo; in the kicker, and + Add. No People section and no tally of who added what; each thing says who added it.'),
                     ('FEW SECTIONS', 'Only what makes the material easy to find: an active collection leads with what is new and how to add; an older one with retrieval. No active or archived mode.'),
                 ]), w=600)])
    html = (HEAD18 + f'<div style="width: 1860px; min-height: {hh("08", 3600)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('08 &middot; THE COLLECTION', 'A kept collection opens like everything else in Life',
                   'Editorial, as the Life project is: a masthead, sections with counts, a drawer of typed originals, a contact sheet of photographs, rows with riso thumbnails. '
                   'Drawn with Life 03 and 07&rsquo;s stylesheet and parts. Founder direction, 2026-09-22; the earlier card-based versions were removed.')
            + r1 + r2 + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('08 - The collection', html)

if __name__ == '__main__':
    build()
