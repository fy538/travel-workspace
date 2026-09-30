"""17 · Around a collection. The four moments boards 08 and 09 do not show, in the same Life grammar: keeping something
(where does it go), correcting a wrong association (said in one line), sharing with one friend (the whole collection,
or not at all), and using the collection later (Jo's weekend, answered from the friends' own words). Recut 2026-09-23 from
eight frames: Restaurants to try, the place page before the correction, and Quiet were dropped as covered by 18 and 19."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
from gen_s1 import share, CARD_CSS, _g, MARK_P, paper_map
import gen_s6 as L6
import gen_s12 as K
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD17 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)

# ── parts ──
def serif_words(t, top=12):
    return f'<div style="margin:{top}px 22px 0 22px; font-family:var(--serif); font-size:16px; line-height:22px; color:#3A332C;">{t}</div>'
def link_card():
    return S.link_line()
def with_sheet(phone_html, sheet_inner):
    """A bottom sheet over a dimmed phone, clipped to the phone's rounded frame."""
    return (f'<div style="position:relative; width:393px; flex:none;">{phone_html}'
            f'<div style="position:absolute; inset:0; border-radius:26px; overflow:hidden; pointer-events:none;">'
            f'<div style="position:absolute; inset:0; background:rgba(27,23,20,0.28);"></div>'
            f'<div style="position:absolute; left:0; right:0; bottom:0; background:var(--card); border-radius:18px 18px 0 0; box-shadow:0 -6px 24px rgba(27,23,20,0.14); padding:10px 0 30px 0;">'
            f'<div style="width:36px; height:4px; border-radius:2px; background:rgba(27,23,20,0.18); margin:0 auto 14px auto;"></div>{sheet_inner}</div></div></div>')
def sheet_head(kick, title):
    return (f'<div style="margin:0 22px;"><span class="kicker" style="color:var(--mute);">{kick}</span>'
            f'<div style="font-family:var(--serif); font-size:22px; line-height:27px; font-weight:600; margin-top:4px;">{title}</div></div>')
def pick(glyph, title, sub, meta='', on=None):
    box = ''
    if on is not None:
        box = ('<span style="width:20px; height:20px; border-radius:5px; flex:none; display:inline-flex; align-items:center; justify-content:center; '
               + ('background:var(--ink);"><svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M2.5 6.2l2.3 2.3 4.7-5" stroke="#FBF7EC" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
                  if on else 'border:1.3px solid rgba(27,23,20,0.30); box-sizing:border-box;"></span>'))
    s = f'<span class="rsub">{sub}</span>' if sub else ''
    m = f'<span class="meta">{meta}</span>' if meta else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:52px; border-bottom:1px solid var(--hair-thin);">{glyph}'
            f'<div style="flex-grow:1; display:flex; flex-direction:column; gap:2px; padding:7px 0;"><span style="font-family:var(--serif); font-size:16px; line-height:21px; font-weight:600;">{title}</span>{s}</div>{m}{box}</div>')
def button(t):
    return (f'<div style="margin:18px 22px 0 22px; height:46px; border-radius:23px; background:var(--ink); color:#FBF7EC; display:flex; align-items:center; justify-content:center; '
            f'font-family:var(--sans); font-size:15px; font-weight:600;">{t}</div>')
PLUS = L6.G('M7.5 3 V12 M3 7.5 H12')
BOOK = L6.G('M4 2.5 H11 V12.8 L7.5 10.3 L4 12.8 Z')

# ── 1 · keep: where does it go ──
def keep():
    """Sept 26 (§12.4): the Keep already happened, privately (board 02). This is the optional second step from its
    receipt: Add to a collection. The shared collection says who will see it."""
    inner = anchor_row('NEW YORK', 'TUESDAY 8:12 PM')
    inner += gut(share('Sam', '7:40 PM · TO FRIENDS', 'this is the cinema. one film a week and exactly one kind of cake', extra=link_card(), kept=True), top=20)
    inner += gut(S.receipt('Kept, just for you', 'Add to a collection', 'Undo'), top=16)
    sheet = (sheet_head('KEPT &middot; THE LANTERN, FROM SAM', 'Add to a collection')
             + f'<div style="margin-top:10px;">'
             + pick(K.riso(3, 40), 'Interesting stuff', 'Yours &middot; three things', 'SEPT 19')
             + pick(K.riso(0, 40), 'Our New York', 'Maya, Sam and Priya will see it', 'OCT 20')
             + f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:50px;">{PLUS}<span style="font-family:var(--sans); font-size:15px; font-weight:500; color:var(--gold-deep);">New collection</span></div></div>')
    return with_sheet(phone2(inner, active='Home'), sheet)
def correct():
    inner = L6.head('PLACE HELD &middot; CARROLL GARDENS', 'Lulu&rsquo;s', 'A place on a list &mdash; not yet been.')
    inner += L6.sec('IN YOUR HISTORY', 'NOTHING YET', 26)
    inner += (f'<div style="margin:10px 22px 0 22px; display:flex; align-items:baseline; gap:10px;">'
              f'<span style="font-family:var(--serif); font-size:16px; line-height:22px; color:var(--mute);">Oct 12 was Sam&rsquo;s evening, not yours.</span>'
              f'<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto; flex:none;">Undo</span></div>')
    inner += L6.sec('THE CONTACT SHEET', '4 PHOTOS') + K.sheet(4, 4)
    inner += L6.sec('FROM FRIENDS', '1')
    inner += serif_words('the upstairs room at lulu&rsquo;s is the reason to go. downstairs gets loud')
    inner += '<div class="meta" style="margin:6px 22px 0 22px;">PRIYA &middot; SEPT 21</div>'
    inner += L6.sec('ALSO HERE')
    inner += L6.row2('Restaurants to try', 'On the list you keep &middot; added from Priya', 'KEPT', None, K.MENU)
    return L6.phone(inner)

# ── 3 · share with Maya: the whole collection, or not at all ──
def invite():
    base = L6.head('KEPT &middot; YOURS ALONE &middot; SINCE AUG 17', 'Getting pasta right', 'Three attempts &mdash; one question still open.')
    base += K.switch('OVER TIME')
    base += L6.sec('THE ATTEMPTS', '3', 26)
    base += K.thing(2, 'Attempt three &middot; held together, still bland', 'SEPT 2')
    base += K.thing(4, 'Attempt two &middot; split again', 'AUG 28')
    base += K.thing(1, 'Attempt one &middot; cheese went in over the flame', 'AUG 24')
    base += L6.sec('THE QUESTION', 'OPEN') + K.question('Why does it split?', 'the cheese goes in off the heat, apparently', 'KEPT AUG 30 &middot; STILL OPEN')
    base += L6.sec('THE DRAWER', '1 KEPT') + K.drawer([K.chip(K.MENU, 'THE MENU &middot; SORRENTO')])
    base += L6.sec('WHERE IT STARTED') + L6.row1(L6.G('M2 8 L13 2.5 L9 13 L7.5 8.5 Z'), 'The plate in Sorrento &middot; Nice &rarr; Rome', 'AUG 17')
    base += '<div style="height:40px;"></div>'
    tiles = ''.join(K.riso(i, 40) for i in (2, 1, 4, 5, 0, 3))
    sheet = (sheet_head('SHARE', 'Getting pasta right')
             + pick(f'<span style="width:28px; height:28px; border-radius:14px; background:var(--ink); color:#FBF7EC; display:inline-flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; flex:none;">M</span>', 'Maya', '', 'CHANGE')
             + L6.sec('SHE SEES', 'ALL SIX', 18)
             + f'<div style="margin:12px 22px 0 22px; display:flex; gap:6px;">{tiles}</div>'
             + '<div class="rsub" style="margin:10px 22px 0 22px; font-size:13px; line-height:18px;">Three attempts, the question, the menu, where it started.</div>'
             + button('Share with Maya')
             + '<div style="margin:12px 22px 0 22px; text-align:center;"><span class="vdl-door vk-t-bodySmMedium">Only some of it? Make a new collection</span></div>')
    return with_sheet(L6.phone(base), sheet)

# ── 4 · use it later: Sunday with Jo and her parents (Sept 26, §12.8) ──
def fit(name, where, who, said, fact, unknown='', on=True):
    """One place that suits the request, in three lines: name, the friend's words (which say why it fits), then what is
    checked and, muted, what is not known."""
    box = ('<span style="width:20px; height:20px; border-radius:5px; flex:none; display:inline-flex; align-items:center; justify-content:center; background:var(--ink);"><svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M2.5 6.2l2.3 2.3 4.7-5" stroke="#FBF7EC" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
           if on else '<span style="display:inline-block; width:20px; height:20px; border-radius:5px; flex:none; border:1.3px solid rgba(27,23,20,0.30); box-sizing:border-box;"></span>')
    u = f'<span style="color:var(--mute);"> &middot; {unknown}</span>' if unknown else ''
    return (f'<div style="margin:0 22px; display:flex; gap:12px; align-items:flex-start; padding:11px 0; border-bottom:1px solid var(--hair-thin);"><div style="flex:1; min-width:0;">'
            f'<div style="display:flex; align-items:baseline; gap:8px; flex-wrap:wrap;"><span style="font-family:var(--serif); font-size:18px; line-height:23px; font-weight:600;">{name}</span><span class="rsub">{where}</span></div>'
            f'<div style="font-family:var(--serif); font-size:15.5px; line-height:21px; color:#3A332C; margin-top:2px;"><b style="font-weight:600;">{who}</b> {said}</div>'
            f'<div style="font-size:13px; line-height:18px; color:var(--green); margin-top:3px;">{fact}{u}</div></div><div style="padding-top:3px;">{box}</div></div>')
def later():
    inner = L6.head('KEPT &middot; WITH MAYA, SAM AND PRIYA &middot; SINCE JUNE', 'Our New York', 'Twelve things &mdash; eight of them places.')
    inner += (f'<div style="margin:18px 22px 0 22px; border-radius:14px; background:var(--card); border:1px solid var(--hairline); padding:10px 14px; display:flex; gap:10px; align-items:flex-start;">'
              f'{S._g(S.SPARK_P, "#8A6628", 16)}<span style="font-family:var(--sans); font-size:15px; line-height:21px; color:var(--ink);">Jo&rsquo;s here with her parents on Sunday. Which of these would suit?</span></div>')
    inner += L6.sec('WOULD SUIT SUNDAY', '3 OF 12', 22)
    inner += fit('Lulu&rsquo;s', 'Carroll Gardens', 'Priya', 'good for a long dinner, with parents', 'Open Sunday from 5', 'a lift upstairs? not known')
    inner += fit('The pier at low water', 'a walk from Jo&rsquo;s', 'You', 'for walking it off', 'Low water 2:40, flat all the way')
    inner += fit('The Lantern', 'Court Street', 'Sam', 'one film a week and exactly one kind of cake', 'Sunday showing at 3:00', on=False)
    inner += '<div style="margin:10px 22px 0 22px; font-size:13px; line-height:18px; color:var(--mute);">Left out: Hato, no bookings and a queue (Sam).</div>'
    inner += K.doors2('Send 2 to Jo', 'Open the collection')
    return L6.phone(inner)
def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('TUESDAY 8:12 PM', '1', 'Keep, then maybe add', 'Keeping already happened, in one tap. Adding to a collection is the optional second step; the shared one says who will see it.', keep(), (LIFE, P('PERSONAL'))),
                 cell('OCT 14', '2', 'Correct: said in one line', 'The Oct 12 payment was Sam&rsquo;s: the visit goes, in one line with an undo. Her photographs, Priya&rsquo;s note and the list entry stay.', correct(), (LIFE, P('CORRECTION'))),
                 cell('OCT 18', '3', 'Share: the whole thing, or not', 'It goes to Maya whole, including what is added later. To share only some, start a new collection with just those. She can add, never change Nora&rsquo;s.', invite(), (LIFE, P('SHARED WHOLE'))),
                 cell('SUNDAY, JO VISITING', '4', 'Use it later: Sunday with Jo and her parents', 'A real question, answered from the collection: three places that fit, in friends&rsquo; own words, with what is checked and what is not. Their words are not sent on.', later(), (LIFE, P('LATER USE')))], top=20)
    n = notes('AROUND A COLLECTION', led([
        ('KEEP ONCE', 'Keep is private and immediate, with Undo. Adding to a collection is a second, optional step; adding to a shared one says who will see it. The same control never sometimes saves and sometimes posts.'),
        ('NO SETUP', 'A collection is a name and the things in it. Nobody picks a type or a purpose.'),
        ('CORRECTIONS ARE ONE LINE', 'Said where the wrong thing was, with an undo. What was independently true stays.'),
        ('SHARED WHOLE', 'A collection is shared whole or not at all, as albums and playlists are. To share only some, make a new collection with just those; the original stays private. Whoever is in sees everything, including what came before them.'),
        ('ADDITIVE', 'People add their own things and reply, and remove only their own. The owner may take any entry out; leaving takes your own entries with you.'),
        ('LATER USE IS THE POINT', 'A collection earns its keep when a real question comes: a short list that fits, why, in the friends&rsquo; own words, with checked facts and unknowns kept apart. No revival prompts in between, and relevance grants no new use of anyone&rsquo;s material. Vesper may use friends&rsquo; words for your own question, credited and within their audience, once the use-grant contract allows it.'),
        ('WHERE THEY LIVE', 'In Life&rsquo;s Threads view, and under the people they are shared with and the places they hold. Friends works forward only; a collection is shared whole, history included (the Sept 26 decision).'),
    ]), w=1710)
    html = (HEAD17 + f'<div style="width: 1780px; min-height: {hh("10", 1900)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 35px 36px 35px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('10 &middot; AROUND A COLLECTION', 'Keeping, correcting, sharing, using it later',
                   'The four moments boards 08 and 09 do not show: where a kept thing goes, a wrong visit taken back, a collection shared whole with one friend, and the collection answering a real question months later. Drawn, not tested with anyone.')
            + r1 + f'<div style="margin-top: 40px;">{n}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('10 - Around a collection', html)

if __name__ == '__main__':
    build()
