"""17 · Kept things. The threads/collections layer of the September 22 handoff (§3, §4, §9 compositions 1-4): a personal
collection started from one item and left alone; possibilities kept apart from supported history, with a correction; a
private exploration selectively shared; and a small circle building something unevenly, with replies on the material
itself and no contribution ranking. Personal by default; nobody has to learn the word thread."""
import re
from mp_kit2 import *
from gen_merge import daycap
from gen_p2_common import illo
import gen_s1 as S
from gen_s1 import (status, share, post, footer, sep, page_bar, CARD_CSS, photo_grid, photo_thumb, paper_map,
                    chat_field, _g, PIN_P, MARK_P, X_P, place_card)
from mp_kit2 import bubble
from gen_s5 import title_block
import gen_s6 as L6
import gen_s12 as K
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD17 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)

def card(inner, pad='14px 16px'): return f'<div style="{CARD_CSS} padding: {pad};">{inner}</div>'
def kick(t, color=None): return f'<div class="fn" style="{f"color: {color};" if color else ""}">{t}</div>'
def ser(t, size=19, lh=24): return f'<div style="{SERIF} font-weight: 600; font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def body(t, color=INK2, size=14, lh=20): return f'<div style="font-size: {size}px; line-height: {lh}px; color: {color};">{t}</div>'
def head_page(kicker, title, sub):
    return page_bar(kicker) + f'<div style="padding: 16px 22px 0 22px;">{ser(title, 28, 32)}<div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 4px;">{sub}</div></div>'
def item(kind, title, sub, stamp, mark=None, last=False):
    """One kept thing, whatever it is: a link, a photograph, a place, an attempt."""
    bb = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.08);'
    m = f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 6px;"><span style="width: 7px; height: 7px; border-radius: 50%; background: {GREEN}; flex: none;"></span><span class="fn" style="color: {GREEN};">{mark}</span></div>' if mark else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 13px 0;{bb}">{thumb(kind, 54)}'
            f'<div style="flex: 1; min-width: 0;">{ser(title, 17, 21)}<div style="font-size: 14px; line-height: 20px; color: {INK}; margin-top: 4px;">{sub}</div>'
            f'<div class="fn" style="margin-top: 4px;">{stamp}</div>{m}</div></div>')
def reply(who, when, text):
    return (f'<div style="padding: 9px 0 9px 14px; border-left: 2px solid rgba(27,23,20,0.10);">'
            f'<div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 14px; font-weight: 600;">{who}</span><span class="fn">{when}</span></div>'
            f'<div style="font-size: 15px; line-height: 21px; margin-top: 3px;">{text}</div></div>')

# ── 1 · from one item ──
def c1_keep():
    inner = anchor_row('NEW YORK', 'TUESDAY 8:12 PM')
    inner += gut(share('Sam', '7:40 PM · TO FRIENDS', 'this is the cinema. one film a week and exactly one kind of cake',
                       extra=card(f'{kick("LINK &middot; THE LANTERN&rsquo;S SITE")}<div style="margin-top: 4px;">{ser("This week: one film, through Sunday", 16, 21)}</div>'), kept=True), top=20)
    inner += gut(card(f'{kick("KEPT")}<div style="margin-top: 6px;">{body("Where do you want it?", INK, 15, 21)}</div>'
                      + f'<div style="margin-top: 12px; border-top: 1px solid rgba(27,23,20,0.08);">'
                      + f'<div style="display: flex; align-items: center; gap: 10px; padding: 11px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">{_g(MARK_P, MUTE, 16)}<span style="font-size: 15px;">Just kept <span style="color: {MUTE};">&middot; findable in Life</span></span></div>'
                      + f'<div style="display: flex; align-items: center; gap: 10px; padding: 11px 0;">{_g("<path d=\'M10 4v12M4 10h12\'/>", GOLDD, 16)}<span style="font-size: 15px; color: {GOLDD};">New collection</span></div></div>'
                      + f'<div style="margin-top: 10px;">{body("You can name it now or later. Nothing else is needed.", MUTE, 13, 18)}</div>'), top=14)
    return phone2(inner, active='Home')
def c1_coll():
    inner = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE SEPT 8', 'Interesting stuff', 'Three things &mdash; no two alike.')
    inner += L6.sec('THE THINGS', '3 KEPT', 26)
    inner += K.thing(1, 'The Lantern &middot; one film a week, from Sam', 'SEPT 8')
    inner += K.thing(0, 'The blue room at the Frick &middot; the light at four', 'SEPT 19')
    inner += K.thing(5, 'Sourdough, the cold rise &middot; a method to try', 'OCT 2')
    inner += L6.sec('THE SOURCES') + K.sources('1 PHOTOGRAPH (YOUR CAMERA) &middot; 2 LINKS')
    inner += L6.voice('Nothing here needs you.')
    return L6.phone(inner)

# ── 2 · possibilities, and what actually happened ──
def c2_try():
    inner = L6.head('KEPT &middot; YOURS ALONE', 'Restaurants to try', 'Six places &mdash; none of them been to yet.')
    inner += f'<div style="margin:22px 22px 0 22px; border-radius:8px; overflow:hidden; border:1px solid var(--hairline);">{paper_map(140, ((0.2, 0.6), (0.36, 0.36), (0.54, 0.64), (0.7, 0.42), (0.84, 0.66)), 349)}</div>'
    inner += L6.sec('THE PLACES', '6 HELD', 26)
    inner += L6.row2('Lulu&rsquo;s', 'upstairs is the reason to go &middot; from Priya', 'SEPT 21', None, L6.FORK)
    inner += L6.row2('Hato', 'the broth is stupid good &middot; from Maya', 'OCT 5', None, L6.FORK)
    inner += L6.row2('Ceci', 'the one with the wine list sam likes &middot; you', 'OCT 9', None, L6.GLASS)
    inner += L6.door('All six')
    inner += L6.voice('Places you might go. Being here says nothing about having gone.')
    return L6.phone(inner)
def c2_been():
    inner = L6.head('PLACE HELD &middot; CARROLL GARDENS', 'Lulu&rsquo;s', 'One evening &mdash; and a place on a list.')
    inner += L6.sec('IN YOUR HISTORY', 'OCT 12', 26)
    inner += K.thing(3, 'Dinner, upstairs &middot; a card payment at 9:10', 'OCT 12')
    inner += L6.sec('THE CONTACT SHEET', '4 PHOTOS') + K.sheet(4, 4)
    inner += L6.sec('ALSO HERE')
    inner += L6.row2('Restaurants to try', 'Still on the list you keep &middot; added from Priya', 'KEPT', None, K.MENU)
    inner += L6.sec('FROM FRIENDS', '1')
    inner += f'<div style="margin:12px 22px 0 22px; font-family:var(--sans); font-size:16px; line-height:23px;">the upstairs room at lulu&rsquo;s is the reason to go. downstairs gets loud</div><div class="meta" style="margin:6px 22px 0 22px;">PRIYA &middot; SEPT 21</div>'
    inner += K.doors2('See the evening', 'Not a visit')
    return L6.phone(inner)
def c2_fix():
    inner = L6.head('PLACE HELD &middot; CARROLL GARDENS', 'Lulu&rsquo;s', 'A place on a list.')
    inner += L6.sec('IN YOUR HISTORY', 'CORRECTED', 26)
    inner += K.left('The payment on Oct 12 was Sam&rsquo;s; you were not there. It no longer counts as your visit. Your four photographs, Priya&rsquo;s note and the list entry are as they were.')
    inner += L6.sec('THE CONTACT SHEET', '4 PHOTOS') + K.sheet(4, 4)
    inner += L6.sec('ALSO HERE')
    inner += L6.row2('Restaurants to try', 'Still on the list you keep', 'KEPT', None, K.MENU)
    return L6.phone(inner)

# ── 3 · a private exploration, selectively shared ──
def c3_priv():
    return K.pasta()
def c3_invite():
    inner = L6.head('KEPT &middot; YOURS ALONE', 'Ask Maya in', 'Getting pasta right')
    inner += L6.sec('WHAT SHE WOULD SEE', '2', 26)
    inner += K.thing(2, 'Attempt three &middot; held together, still bland', 'SEPT 2')
    inner += K.thing(1, 'Why does it split? &middot; the question', 'AUG 30')
    inner += L6.sec('WHAT STAYS YOURS', '5')
    inner += K.left('Attempts one and two, your notes, the chat where you worked it out, the menu, and where this came from in your trip.')
    inner += L6.voice('She can add her own things and reply. She cannot change or remove yours.')
    inner += K.doors2('Ask her in', 'Pick again')
    return L6.phone(inner)
def c3_maya():
    inner = L6.head('KEPT &middot; WITH NORA &middot; SINCE OCT 18', 'Getting pasta right', 'Two of hers &mdash; and yours.')
    inner += L6.sec('THE ATTEMPTS', '3', 26)
    inner += K.thing(4, 'Mine, last night &middot; full pepper. i am telling you', 'OCT 19')
    inner += K.thing(2, 'Attempt three &middot; held together, still bland &middot; Nora', 'SEPT 2')
    inner += L6.sec('THE QUESTION', 'OPEN')
    inner += K.left('Why does it split? The cheese goes in off the heat, apparently &mdash; Nora, Aug 30.', 'Reply')
    inner += L6.sec('THE CONVERSATION', '1 THREAD')
    inner += L6.row1(L6.BUBBLE, 'fine. full pepper. writing it down &middot; Nora', 'OCT 19')
    inner += K.doors2('Add something', 'Reply')
    return L6.phone(inner)

# ── 4 · a small circle ──
def c4_ours():
    return K.our_ny()
def c4_quiet():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Eleven things &mdash; quiet since October.')
    inner += L6.sec('THE THINGS', '11 KEPT', 26)
    inner += K.thing(0, 'The pier at low water &middot; walk it off', 'OCT 20')
    inner += K.thing(3, 'Hato &middot; the broth is stupid good', 'OCT 5')
    inner += L6.door('All eleven')
    inner += L6.sec('THE DRAWER', '3 KEPT') + K.drawer([K.band('JOHN SUMMIT'), K.chip(L6.FORK, 'HATO'), K.chip(K.LINKG, 'THE LANTERN')])
    inner += L6.voice('Nothing here needs you. Nobody is behind.')
    return L6.phone(inner)
def c4_use():
    inner = S.bar('VESPER', 'FEBRUARY 2')
    inner += gut(bubble('jo is here for the weekend and staying in cobble hill. anything from our new york near her?'), top=20)
    inner += gut(card(f'{kick("FROM OUR NEW YORK &middot; THREE NEAR COBBLE HILL")}'
                      + f'<div style="margin-top: 10px;">{body("Hato, two streets away &middot; Maya. The Lantern, a ten-minute walk &middot; Sam. The pier at low water, across the expressway &middot; yours.", INK, 15, 21)}</div>'
                      + f'<div style="margin-top: 10px;">{body("Hato has no bookings on Saturday; the Lantern shows one film, at 7:15.", MUTE, 13, 19)}</div>'
                      + f'<div style="margin-top: 12px; display: flex; gap: 18px; align-items: center;">{door("Send the three to Jo", GOLDD)}{door("Open the collection", MUTE)}</div>'), top=12)
    inner += gut(chat_field('Message', ask=False), top=16)
    return phone2(inner, active='Chat')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'
def sechead(k, t, sub):
    return f'<div style="margin-top: 32px;"><div class="kick" style="color: {GOLDD};">{k}</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 29px; margin-top: 4px;">{t}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px; max-width: 1200px;">{sub}</div></div>'

def build():
    s1 = sechead('1', 'One thing, kept', 'A collection starts from something you already wanted to keep, with a casual name and nothing else to fill in. It can hold anything, and it can stay like this forever.')
    r1 = rowdiv([cell('TUESDAY 8:12 PM', '1.1', 'Keeping Sam&rsquo;s link', 'Keep asks one question: where. Just kept, or a new collection. No purpose, no type, no members.', c1_keep(), (P('PERSONAL'), P('FROM A SHARE'))),
                 cell('OCT 9', '2.1', 'Restaurants to try', 'A place list with the map inside the record. Possibilities only: being on it says nothing about having gone, or having liked it.', c2_try(), (P('POSSIBILITY'), P('LIFE'))),
                 cell('OCT 13', '2.2', 'What actually happened', 'The place page: an evening in your history, four photographs, the list it is still on, and Priya&rsquo;s note. Three different truths, none collapsed.', c2_been(), (P('HISTORY'), P('PLACES')))], top=16)
    s2 = sechead('2', 'A wrong association, corrected', 'The payment was Sam&rsquo;s. The visit goes; the photographs, the note and the list entry stay.')
    r2 = rowdiv([cell('OCT 14', '2.3', 'Not a visit', 'Said once, where the visit was. What was independently true is untouched.', c2_fix(), (P('CORRECTION'), P('PLACES'))),
                 cell('OCT 18', '3.2', 'Asking Maya in', 'Starting from board 18&rsquo;s Getting pasta right. Exactly what she would see, and exactly what stays yours: the other attempts, your notes, the chat, the trip it came from.', c3_invite(), (P('SELECTIVE'), P('LIFE'))),
                 cell('OCT 19', '3.3', 'What Maya can do', 'She adds her own attempt and replies. She cannot edit or remove Nora&rsquo;s. Both names stay on their own things.', c3_maya(), (P('SHARED'), P('MAYA')))])
    s3 = sechead('3', 'A few friends, building something', 'Four people, uneven contributions, nobody counted. Replies sit on the thing they are about, not in a room of their own.')
    r3 = rowdiv([cell('FEBRUARY', '4.2', 'Quiet, and fine', 'Board 18&rsquo;s Our New York, four months on. The subtitle says so; the voice line says nobody is behind. No revival prompt.', c4_quiet(), (P('QUIET'), P('LIFE'))),
                 cell('FEBRUARY 2', '4.3', 'Useful again, on a real question', 'Jo is visiting. The collection answers where, in the friends&rsquo; own words, with two current facts. This is what later use is for.', c4_use(), (P('LATER USE'), P('CHAT')))])
    n1 = notes('WHAT THESE ARE', led([
                     ('NOT ONE TYPE', 'A mixed collection, a list of possibilities, a record of what happened, and an exploration in progress are four different intents. Nobody picks a type: keeping something and naming it is the whole setup.'),
                     ('PERSONAL FIRST', 'Every one of these works alone. Another person is an option, never a prerequisite, and never arrives by accident.'),
                     ('KEEPING IS NOT POSTING', 'Keep puts something in your own Life. Adding to something shared is a different, named action.'),
                     ('ADDITIVE, NOT EDITORIAL', 'Anyone in a shared collection adds their own things and replies. Nobody edits or removes another person&rsquo;s.'),
                     ('NOBODY IS COUNTED', 'No contribution totals, no ranking, no streak, no prompt to the quiet one.'),
                 ]), w=560)
    n2 = notes('OPEN, AND CONFLICTS', led([
        ('NAMING', '&ldquo;Kept&rdquo; is used here for all of it; the handoff leaves naming open. Nobody has to know the word thread.'),
        ('WHERE THEY LIVE IN LIFE', 'Drawn under Life. Whether simple lists sit beside Time, Places, People and Threads, or inside them, is a Life decision, not taken here.'),
        ('CONFLICT &middot; JOINING', 'Board 12 ruled that someone added to a group sees only what comes after. The handoff says historical access is still open. Recorded; the invite here is to selected material, which sidesteps it.'),
        ('CONFLICT &middot; GROUP CHAT', 'Replies on an item are drawn; a room for the four is not. Consistent with the Sept 21 ruling and with a thread-level conversation.'),
        ('RETENTION', 'The kept question in 3.1 is an explicitly kept item, not a conversation Vesper decided to remember. Nothing here claims a retention agreement that does not exist.'),
        ('SOURCES', 'The visit evidence in 2.2 is a labelled fixture: a card payment and the person&rsquo;s own photographs. No claim that either exists in the product today.'),
    ]), w=620)
    bodyhtml = s1 + r1 + s2 + r2 + s3 + r3 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD17 + f'<div style="width: 1860px; min-height: {hh("17", 4200)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('17 &middot; KEPT THINGS', 'Collections, possibilities, history, and one exploration',
                   'What people keep together, and how it stays useful. A collection from one item; possibilities kept apart from what actually happened, with a correction; a private exploration opened to one friend on selected material; '
                   'and a few friends building something unevenly. Personal by default. Drawn, not tested with anyone.')
            + bodyhtml + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('17 - Kept things', html)

if __name__ == '__main__':
    build()
