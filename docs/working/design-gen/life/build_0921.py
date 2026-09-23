#!/usr/bin/env python3
"""04b · Ordinary photographs — the Life-led part of the September 21 photo assignment.

Usage: build_0921.py SRC_DIR OUT_DIR      (SRC_DIR = the live project's boards)

Fixture: shared-fixture-world-2026-09-07.md §10 (PH-01 … PH-07, A4). Every picture is a drawn
stand-in and says so outside the phone. Voice: product copy and people's words inside the phone,
provenance as "source · when" in mono, every reason outside the phone (feedback_board_copy_voice).
Also writes the updated 00 - Start here (04b joins the walkthrough after 04).
"""
import html
import os
import re
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
rd = lambda n: open(os.path.join(SRC, n), encoding='utf-8').read()
B05, B04, B06, BP3, B00 = (rd('05 - Find it again.dc.html'), rd('04 - My original things.dc.html'),
                          rd('06 - Give once, get value back.dc.html'), rd('P3 - Something I deliberately saved.dc.html'),
                          rd('00 - Start here.dc.html'))


def div_end(t, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', t[start:]):
        depth += -1 if m.group(0) == '</div>' else 1
        if depth == 0:
            return start + m.end()
    raise AssertionError('unbalanced div')


def slice_div(board, anchor, note=''):
    i = board.find(anchor)
    assert i >= 0, f'missing anchor {anchor[:60]!r} {note}'
    return board[i:div_end(board, i)]


def slice_between(board, a, b, note=''):
    i = board.find(a)
    assert i >= 0, f'missing anchor {a[:60]!r} {note}'
    j = board.find(b, i)
    assert j > i, f'missing end {b[:60]!r} {note}'
    return board[i:j]


def rep(s, a, b, n=1):
    assert s.count(a) == n, (a[:70], s.count(a))
    return s.replace(a, b)


# ── the project's own shapes ───────────────────────────────────────────────────────
HEAD = B05[:B05.find('</helmet>') + len('</helmet>')] + '\n'
TAIL = '</div>\n</x-dc>\n</body>\n</html>\n'
TABBAR = slice_between(B05, '<div style="border-top:1px solid var(--hairline); background:var(--card); display:flex; padding:10px 22px 22px 22px;',
                       '</div></div></div><div class="cnote">') + '</div>'
_SEARCH = slice_div(B05, '<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:12px;">', 'search')
assert _SEARCH.count('>pasta<') == 1 and 'FOUND IN' not in _SEARCH
BACKBTN = slice_div(B05, '<div style="width:34px; height:34px; border-radius:12px; background:rgba(251,247,236,0.85);', 'back button')
# P3.4's day masthead: back + tools, kicker, title, sub — the record-page donor
_mi = BP3.rfind('<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:10px;">', 0, BP3.find('Wednesday, August 18'))
assert _mi >= 0, 'day masthead not found'
_MAST = BP3[_mi:div_end(BP3, _mi)]
assert 'Wednesday, August 18' in _MAST and 'Sorrento, day three.' in _MAST
_CTX_CARD = ('<div style="width:393px; background:var(--card); border:1px solid var(--hairline); border-radius:12px; '
             'padding:16px 20px 18px 20px; box-sizing:border-box;">')
assert _CTX_CARD in B06, 'chat strip card changed on 06'


def masthead(kicker, title, sub):
    m = rep(_MAST, 'DAY &middot; AUG 18 2026 &middot; IN THE COAST &middot; NICE &rarr; ROME', kicker)
    m = rep(m, 'Wednesday, August 18', title)
    return rep(m, 'Sorrento, day three.', sub)


def searchbar(q):
    return _SEARCH.replace('>pasta<', f'>{q}<', 1)


def sect(label, right='', top=34):
    r = f'<span class="barmeta" style="margin-left:auto;">{right}</span>' if right else ''
    return (f'<div style="margin:{top}px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; '
            f'display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{label}</span>{r}</div>')


def gut(inner, top=12):
    return f'<div style="margin:{top}px 22px 0 22px;">{inner}</div>'


def door(text):
    return f'<div style="display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium">{text}</span></div>'


def prov(text):
    return f'<span class="meta" style="white-space:normal; line-height:15px;">{text}</span>'


CHEV = ('<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" '
        'stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def row(title, sub, meta='', lead=''):
    m = f'<span class="meta">{meta}</span>' if meta else ''
    return ('<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:54px; '
            f'border-bottom:1px solid var(--hair-thin);">{lead}<div style="flex-grow:1; display:flex; flex-direction:column; gap:2px;">'
            f'<span style="font-family:var(--serif); font-size:15.5px; line-height:20px; font-weight:600;">{title}</span>'
            f'<span class="rsub">{sub}</span></div>{m}{CHEV}</div>')


def dci(name, h, **props):
    attrs = ' '.join(f'{k}="{html.escape(v, quote=True)}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'


def phone(inner, minh=None):
    style = 'width: 393px; ' + (f'min-height: {minh}px; ' if minh else '')
    return (f'<div class="cphone"><div style="{style}background: var(--paper); color: var(--ink); font-family: var(--sans); '
            'box-sizing: border-box; display: flex; flex-direction: column; position:relative;">'
            + inner + '<div style="flex-grow:1;"></div>' + TABBAR + '</div></div>')


def panel(cap, ident, body, note):
    idt = f'<span class="ccap" style="color:var(--mute-light)">{ident}</span>' if ident else ''
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center">'
            f'<span class="ccap">{cap}</span>{idt}</div>{body}<div class="cnote">{note}</div></div>')


# ── the photographs: drawn stand-ins, one per ledger ID ────────────────────────────
ASPECT = {'PH-01': 4 / 3, 'PH-02': 3 / 4, 'PH-03': 3 / 4, 'PH-04': 4 / 3, 'PH-05': 3 / 4, 'PH-06': 4 / 3,
          'PH-07': 240 / 520, 'A4': 4 / 5}
AUTHOR = {'PH-01': 'M', 'PH-05': 'D'}
_uid = [0]


def _art(pid, u):
    L, P = (320, 240), (240, 320)
    if pid == 'PH-01':  # the table from above, 8:25 pm (Maya)
        return L, (f'<rect width="320" height="240" fill="#B98C5A"/><rect x="0" y="0" width="320" height="240" fill="url(#g{u})" opacity="0.35"/>'
                   '<rect x="24" y="30" width="272" height="180" rx="14" fill="#EFE6D3"/>'
                   + ''.join(f'<circle cx="{x}" cy="{y}" r="34" fill="#FBF7EC" stroke="#D9CDB4"/><ellipse cx="{x}" cy="{y}" rx="21" ry="16" fill="#E7C15A"/>'
                             f'<path d="M{x-14} {y-4} q7 -9 14 0 t14 0 M{x-12} {y+5} q6 -7 12 0 t12 0" stroke="#C99A32" stroke-width="2" fill="none"/>'
                             for x, y in ((92, 88), (228, 88), (160, 170)))
                   + '<circle cx="146" cy="104" r="9" fill="none" stroke="#9FB7B5" stroke-width="3"/><circle cx="180" cy="130" r="9" fill="none" stroke="#9FB7B5" stroke-width="3"/>'
                   '<rect x="250" y="150" width="30" height="46" rx="6" fill="#6E3B2E"/><ellipse cx="64" cy="170" rx="22" ry="12" fill="#D8A25E"/>'
                   f'<defs><linearGradient id="g{u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient></defs>')
    if pid in ('PH-02', 'PH-03'):  # the pan before anyone came; PH-03 a second later
        dx, dy = (0, 0) if pid == 'PH-02' else (7, -5)
        return P, ('<rect width="240" height="320" fill="#D6C7AA"/><rect y="150" width="240" height="170" fill="#2E2B28"/>'
                   '<circle cx="70" cy="290" r="26" fill="none" stroke="#4A4541" stroke-width="4"/>'
                   f'<g transform="translate({dx} {dy})"><rect x="168" y="196" width="72" height="14" rx="7" fill="#3B3632"/>'
                   '<circle cx="118" cy="214" r="64" fill="#3B3632"/><circle cx="118" cy="214" r="54" fill="#E5BE57"/>'
                   '<path d="M84 204 q10 -12 20 0 t20 0 t20 0 M80 222 q10 -12 20 0 t20 0 t20 0 M92 238 q9 -10 18 0 t18 0" stroke="#B8872A" stroke-width="3" fill="none"/></g>'
                   '<path d="M100 150 q-10 -26 4 -52 M128 146 q12 -30 -2 -60 M150 152 q-8 -22 6 -44" stroke="#FFFFFF" stroke-opacity="0.55" stroke-width="5" fill="none" stroke-linecap="round"/>')
    if pid == 'PH-04':  # the table after, low light
        return L, (f'<defs><radialGradient id="c{u}"><stop offset="0" stop-color="#F7C46C" stop-opacity="0.9"/><stop offset="1" stop-color="#F7C46C" stop-opacity="0"/></radialGradient></defs>'
                   '<rect width="320" height="240" fill="#16130F"/><rect x="24" y="44" width="272" height="170" rx="14" fill="#231D18"/>'
                   f'<circle cx="120" cy="112" r="70" fill="url(#c{u})" opacity="0.55"/><circle cx="214" cy="120" r="56" fill="url(#c{u})" opacity="0.4"/>'
                   '<rect x="116" y="96" width="8" height="26" fill="#E9DCC0" opacity="0.8"/><rect x="210" y="104" width="8" height="22" fill="#E9DCC0" opacity="0.7"/>'
                   '<circle cx="84" cy="168" r="28" fill="#2E2823"/><circle cx="252" cy="80" r="24" fill="#2B2520"/><circle cx="170" cy="182" r="10" fill="none" stroke="#3E3730" stroke-width="3"/>')
    if pid == 'PH-05':  # Dana's dish, Sorrento, daylight
        return P, ('<rect width="240" height="320" fill="#3E6E99"/>'
                   + ''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="none" stroke="#6C97BF" stroke-width="2"/>' for x in range(0, 240, 40) for y in range(0, 320, 40))
                   + '<circle cx="120" cy="170" r="92" fill="#FBF7EC"/><circle cx="120" cy="170" r="70" fill="#F1E7CF"/>'
                   '<ellipse cx="116" cy="172" rx="52" ry="40" fill="#E9C766"/><path d="M76 166 q12 -14 24 0 t24 0 t24 0 M80 186 q11 -13 22 0 t22 0 t22 0" stroke="#BF9533" stroke-width="3" fill="none"/>'
                   '<circle cx="150" cy="138" r="14" fill="#6FA05A"/><circle cx="92" cy="146" r="10" fill="#6FA05A"/>'
                   '<circle cx="190" cy="248" r="22" fill="#F4D23F"/><circle cx="190" cy="248" r="15" fill="#FBE98A"/>')
    if pid == 'PH-06':  # a bowl of lemons, no date or place
        return L, ('<rect width="320" height="240" fill="#E6D8BD"/><ellipse cx="160" cy="176" rx="118" ry="30" fill="#C9B894"/>'
                   '<path d="M52 150 Q160 250 268 150 Z" fill="#B4563F"/>'
                   + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="30" ry="24" fill="#EFC53C" stroke="#D2A62A" stroke-width="2"/>' for x, y in ((104, 132), (156, 118), (206, 134), (132, 104), (184, 98)))
                   + '<path d="M170 76 q24 -18 40 -4 q-22 14 -40 4 Z" fill="#4E7A6F"/>')
    if pid == 'PH-07':  # a screenshot of a recipe page
        lines = ''.join(f'<rect x="20" y="{y}" width="{w}" height="7" rx="3" fill="#CFC9BE"/>' for y, w in
                        ((300, 196), (316, 180), (332, 200), (348, 150), (376, 190), (392, 170), (408, 198), (424, 120), (452, 186), (468, 160)))
        return (240, 520), ('<rect width="240" height="520" fill="#FAF8F3"/><rect width="240" height="22" fill="#F0EEE8"/>'
                            '<rect x="12" y="8" width="26" height="6" rx="3" fill="#9A958C"/><rect x="200" y="8" width="28" height="6" rx="3" fill="#9A958C"/>'
                            '<rect x="12" y="34" width="216" height="26" rx="13" fill="#ECE9E1"/>'
                            '<text x="20" y="96" font-family="Georgia, serif" font-size="19" fill="#2A2622">Spaghetti alla</text>'
                            '<text x="20" y="120" font-family="Georgia, serif" font-size="19" fill="#2A2622">Nerano</text>'
                            '<rect x="20" y="138" width="200" height="140" rx="6" fill="#D6C07F"/><ellipse cx="120" cy="210" rx="62" ry="42" fill="#E9C766"/>'
                            '<circle cx="84" cy="182" r="12" fill="#5E8E4C"/><circle cx="150" cy="232" r="10" fill="#5E8E4C"/>' + lines)
    if pid == 'A4':  # Thursday's broken sauce
        return (240, 300), ('<rect width="240" height="300" fill="#8E7B63"/><circle cx="120" cy="150" r="104" fill="#F7F1E4"/>'
                            '<ellipse cx="120" cy="152" rx="70" ry="56" fill="#EBD48E"/>'
                            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F6ECCB"/>' for x, y, r in
                                      ((96, 134, 7), (132, 128, 5), (150, 160, 8), (104, 170, 6), (126, 180, 4), (84, 156, 4), (160, 138, 4)))
                            + '<path d="M78 150 q12 -12 24 0 t24 0 t24 0" stroke="#C8A94F" stroke-width="3" fill="none"/>')
    raise KeyError(pid)


def photo(pid, w=None, h=None, style=''):
    """The stand-in at a size that keeps its shape. Give a width or a height, never both."""
    _uid[0] += 1
    (vw, vh), body = _art(pid, _uid[0])
    a = vw / vh
    if w is None:
        w = h * a
    h = w / a
    return (f'<svg width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {vw} {vh}" style="display:block;{style}" '
            f'role="img" aria-label="{pid}">{body}</svg>')


def badge(pid, size=16):
    if pid not in AUTHOR:
        return ''
    return (f'<span style="position:absolute; left:4px; bottom:4px; width:{size}px; height:{size}px; border-radius:{size//2}px; '
            f'background:var(--ink); color:var(--card); font-family:var(--sans); font-size:{size-7}px; font-weight:700; '
            f'display:flex; align-items:center; justify-content:center;">{AUTHOR[pid]}</span>')


CHECK = ('<span style="position:absolute; right:4px; top:4px; width:18px; height:18px; border-radius:9px; background:var(--ink); box-shadow:0 0 0 1.5px #FBF7EC; '
         'display:flex; align-items:center; justify-content:center;"><svg width="10" height="10" viewBox="0 0 12 12" fill="none">'
         '<path d="M2.5 6.4 L4.8 8.6 L9.5 3.6" stroke="#FBF7EC" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')


def tile(pid, h, chosen=False, failed=False):
    w = h * ASPECT[pid]
    ring = 'outline:2px solid var(--ink); outline-offset:-2px;' if chosen else ''
    if failed:
        inner = (f'<div style="width:{w:.1f}px; height:{h:.1f}px; background:var(--vk-paper30, #E8E2D4); display:flex; flex-direction:column; '
                 'align-items:center; justify-content:center; gap:6px;">'
                 '<svg width="18" height="18" viewBox="0 0 20 20" fill="none"><path d="M16 10a6 6 0 1 1-2-4.5M16 3v3.5h-3.5" stroke="#6E6862" '
                 'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                 '<span style="font-family:var(--sans); font-size:11px; color:var(--mute);">Tap to retry</span></div>')
    else:
        inner = photo(pid, w=w)
    return (f'<div style="position:relative; width:{w:.1f}px; height:{h:.1f}px; border-radius:4px; overflow:hidden; flex:none; {ring}">'
            f'{inner}{badge(pid)}{CHECK if chosen else ""}</div>')


def justified(pids, width=349, gap=6, chosen=(), failed=()):
    """One row whose pictures keep their own shapes and share a height."""
    h = (width - gap * (len(pids) - 1)) / sum(ASPECT[p] for p in pids)
    return (f'<div style="display:flex; gap:{gap}px;">'
            + ''.join(tile(p, h, p in chosen, p in failed) for p in pids) + '</div>')


def grid(rows, chosen=(), failed=()):
    return gut('<div style="display:flex; flex-direction:column; gap:6px;">'
               + ''.join(justified(r, chosen=chosen, failed=failed) for r in rows) + '</div>', top=14)


ORDER = ['PH-05', 'PH-02', 'PH-03', 'PH-01', 'PH-04']        # by time: Dana Fri, 6:48, 6:48, 8:25, 10:40
ROWS = [['PH-05', 'PH-02', 'PH-03'], ['PH-01', 'PH-04']]
RECORD = masthead('DINNER &middot; SAT SEP 19 &middot; AT NORA&rsquo;S', 'Pasta night', 'From seven. Sam and Maya.')


# ── the viewer (Life leads its anatomy) ────────────────────────────────────────────
def topbar(label):
    return ('<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;">' + BACKBTN
            + f'<span class="kicker" style="margin-left:auto; color:var(--mute);">{label}</span></div>')


def strip(current, ids=ORDER):
    return gut('<div style="display:flex; gap:5px; align-items:center; justify-content:center;">'
               + ''.join(f'<div style="flex:none; border-radius:3px; overflow:hidden; '
                         f'{"outline:2px solid var(--ink); outline-offset:1px;" if p == current else "opacity:0.75;"}">{photo(p, h=40)}</div>'
                         for p in ids) + '</div>', top=14)


def attribution(name, initial, when):
    return gut('<div class="vdl-attr"><span class="vdl-avatar sm vk-t-capsMicro" style="color:var(--card);">' + initial + '</span>'
               '<div class="vdl-attr-meta"><span class="vdl-t-sectionHeading">' + name + '</span>'
               f'<span class="vdl-t-metaLine" style="color:var(--mute);">{when}</span></div></div>', top=16)


def viewer(pid, label, provenance, doors, zoom=None, extra=''):
    a = ASPECT[pid]
    if zoom:
        box_h = min(393 / a, 460)
        img = (f'<div style="margin-top:14px; width:393px; height:{box_h:.0f}px; overflow:hidden; position:relative; background:#0F0D0B;">'
               f'<div style="position:absolute; left:{zoom[0]}px; top:{zoom[1]}px;">{photo(pid, w=393 * 2)}</div>'
               '<span style="position:absolute; right:12px; top:12px; padding:3px 8px; border-radius:10px; background:rgba(27,23,20,0.72); '
               'color:#FBF7EC; font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:0.8px;">2&times;</span></div>')
    else:
        img = f'<div style="margin-top:14px;">{photo(pid, w=393) if a >= 0.74 else photo(pid, h=460, style="margin:0 auto;")}</div>'
    return topbar(label) + img + extra + provenance + ''.join(gut(door(d), top=12) for d in doors)


# ── frames ─────────────────────────────────────────────────────────────────────────
f1 = panel('The evening, with its pictures', '04b.1',
           phone(RECORD + sect('PHOTOGRAPHS', '5', top=26) + gut(justified(ORDER), top=14)
                 + gut(door('See all 5'), top=14)
                 + sect('THE EVENING') + gut(door('In order, with the pictures'), top=12), 760),
           'The record holds its pictures in one row that keeps each shape, all five, none cropped to a square. '
           'Maya&rsquo;s and Dana&rsquo;s carry their initial. The record adds nothing to the pictures: no title for them, no caption, no reading.')

f2 = panel('Maya&rsquo;s photograph, whole', '04b.2',
           phone(viewer('PH-01', '4 OF 5', attribution('Maya', 'M', 'SAT 8:25 PM'),
                        ['Reply to Maya'], extra=strip('PH-01'))
                 + sect('IN', top=26) + row('Pasta night', 'Sat Sep 19 &middot; at Nora&rsquo;s', 'SEP 19'), 900),
           'Opened from 04b.1: the whole image edge to edge, then the others from that evening as a strip, then who and when. '
           'Maya&rsquo;s picture offers Reply and nothing that would move or copy it (ledger §10). '
           'Showing a picture does not send it to the model.')

f3 = panel('The next one, tall', '04b.3',
           phone(viewer('PH-02', '2 OF 5', gut(prov('YOUR CAMERA &middot; SAT 6:48 PM'), top=16),
                        ['Share'], extra=strip('PH-02')), 900),
           'A portrait keeps its height: the viewer fits the whole picture instead of cropping it to the screen. '
           'The next thumbnail is the same pan a second later. It sits in the strip like any other picture, with no prompt to clean it up.')

f4 = panel('Closer, in low light', '04b.4',
           phone(viewer('PH-04', '5 OF 5', gut(prov('YOUR CAMERA &middot; SAT 10:40 PM'), top=16), [],
                        zoom=(-300, -150)), 700),
           'The late table stays dark, as taken: no brightening, no enhancement, no generated detail. '
           'Zoom is reading. Native pinch, pan, double-tap and behavior under larger text need implementation evidence.')

ALL5 = ('<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:10px;"><div style="display:flex; align-items:center;">'
        + BACKBTN + '<span style="margin-left:auto; font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1px; color:var(--gold-deep);">SELECT</span></div>'
        '<div style="display:flex; flex-direction:column; gap:6px; padding-top:4px;"><span class="kicker" style="color:var(--mute);">PASTA NIGHT &middot; SAT SEP 19</span>'
        '<span style="font-family:var(--serif); font-weight:600; font-size:26px; line-height:30px; letter-spacing:-0.5px;">Photographs</span>'
        '<span class="kicker" style="color:var(--mute);">5 &middot; 3 YOURS &middot; MAYA &middot; DANA</span></div></div>')

f5 = panel('All five, as taken', '04b.5', phone(ALL5 + grid(ROWS), 700),
           'The set opened whole, in time order, rows sized to the pictures&rsquo; own shapes. '
           'The two pans stand side by side: a near-duplicate is a picture, not a problem to resolve. '
           'Dana&rsquo;s dish is here because she sent it to the dinner, not because it was taken there.')

f6 = panel('A picture with no date or place', '04b.6',
           phone(viewer('PH-06', 'PHOTOGRAPHS &middot; UNPLACED', gut(prov('YOUR PHOTO &middot; NO DATE OR PLACE CAME WITH IT'), top=16),
                        ['Add to a day']), 700),
           'Nothing came with the file, so nothing is guessed: no date, no place, no evening. It lives in Photographs and is complete there. '
           '&ldquo;Add to a day&rdquo; is there if Nora wants it; there is no count of unplaced pictures asking to be cleared.')

f7 = panel('A screenshot among the photographs', '04b.7',
           phone(topbar('SCREENSHOT') + gut('<div style="border:1px solid var(--hairline); border-radius:10px; overflow:hidden; width:220px; margin:0 auto;">'
                                            + photo('PH-07', w=220) + '</div>', top=14)
                 + gut(prov('SCREENSHOT &middot; THU SEP 17 &middot; 3:12 PM'), top=14)
                 + gut(door('Open the page'), top=12), 820),
           'A screenshot opens as the document it shows, at its full height. It is not evidence of the evening, '
           'so it stays out of Pasta night even though the dish is the same. Mixed sources keep their kinds.')

f8 = panel('Asked for the picture, given the picture', '04b.8',
           phone(searchbar('the table photo from saturday') + sect('PHOTOGRAPHS', '1', top=26)
                 + gut('<div style="position:relative; border-radius:6px; overflow:hidden;">' + photo('PH-01', w=349) + badge('PH-01', 18) + '</div>', top=12)
                 + gut(prov('MAYA &middot; SAT 8:25 PM &middot; PASTA NIGHT'), top=10)
                 + sect('EVENINGS', '1') + row('Pasta night', 'Sat Sep 19 &middot; at Nora&rsquo;s', 'SEP 19'), 900),
           'The question names a picture, so the answer is the picture, whole and first. The evening it belongs to follows as a door. '
           'No summary, dossier or tour comes before it; Back returns to this query.')

BRING = dci('Notice', 92, tone='applied', title='4 photos kept · 9:30 am',
            body='3 went into Pasta night. The lemons had no date, so they’re in Photographs.')
f9 = panel('Bringing Saturday&rsquo;s pictures', '04b.9',
           phone(RECORD + gut(BRING, top=18) + gut(door('Undo'), top=10)
                 + sect('PHOTOGRAPHS', '5', top=24) + gut(justified(ORDER), top=14), 760),
           'Nora sends four pictures from her camera through the share sheet, the contract&rsquo;s Bring (§3.2). They settle by their own camera times; '
           'the one without a time stays unplaced. One receipt with Undo, and nothing to name, caption or finish.')

ASK = ('<div class="cctx">' + _CTX_CARD + '<div class="kicker" style="color:var(--mute);">CHAT &middot; THU 7:50 PM</div>'
       '<div style="display:flex; gap:12px; align-items:flex-start; padding-top:10px;"><div style="flex:none; border-radius:6px; overflow:hidden;">'
       + photo('A4', w=72) + '</div><div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink);">'
       'why did the sauce break? this was the Sorrento one</div></div>'
       '<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:10px;">'
       'Too much heat is one possibility; the photo alone cannot confirm it. For the next attempt, try taking the pan off the heat and adding '
       'the cheese gradually with a little starchy pasta water. That gives you one concrete adjustment to try.</div></div></div>')
f10 = panel('Asking with a picture', '04b.10', ASK,
            'The countercase. A picture attached to a question is Ask: it answers the question and does not join Life (contract §3.2, §3.3). '
            'The answer is the ledger&rsquo;s A0, verbatim and synthetic. Chat is drawn as a context strip; its composer is not redesigned here.')

SELHEAD = ('<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;"><span class="kicker" style="color:var(--ink);">3 SELECTED</span>'
           '<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto;">Done</span></div>'
           '<div style="padding: 10px 22px 0 22px;"><span class="kicker" style="color:var(--mute);">PASTA NIGHT &middot; PHOTOGRAPHS</span></div>')
ACTIONS = gut('<div style="display:flex; gap:8px; border-top:1px solid var(--hairline); padding-top:14px;">'
              + ''.join(f'<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1; padding:0 8px;">{t}</span>' for t in ('Share 2', 'Export 2', 'Delete 2'))
              + '</div>', top=20) + gut('<div class="rsub">Maya&rsquo;s photo stays with the dinner.</div>', top=10)
f11 = panel('Three chosen, two can go', '04b.11',
            phone(SELHEAD + grid(ROWS, chosen=('PH-01', 'PH-02', 'PH-04')) + ACTIONS, 700),
            'General selection keeps the mixed set, and each door counts what it can actually reach. Maya&rsquo;s picture is displayed to the dinner '
            'under her grant: Nora can look and reply, not share it on, export it or delete it. Social 10.1&rsquo;s share-only selector offers only '
            'Nora&rsquo;s own pictures; both modes are right for their job. Share opens Social&rsquo;s preview with the exact two outgoing originals and '
            'says there why Maya&rsquo;s isn&rsquo;t among them (prototype 04c). Export and delete outcomes are 09.3&ndash;09.7.')

SENT = dci('Notice', 64, tone='applied', title='Sent to Maya · 2 photos', body='Your selection is cleared.')
f12 = panel('Back after a confirmed send', '04b.12', phone(ALL5 + gut(SENT, top=16) + grid(ROWS), 760),
            'Only a confirmed delivery clears the selection. Not now restores the same mixed selection. The other outcomes are Social 10P&rsquo;s: '
            'nothing went stays on the share with the words kept; part went leaves only the undelivered picture selected and retries only it; '
            'not known yet offers a check, never a resend. All are walked in prototype 04c.')

f13 = panel('One that won&rsquo;t load', '04b.13', phone(ALL5 + grid(ROWS, failed=('PH-05',)), 700),
            'An image that fails keeps its place, its shape and its author&rsquo;s initial, and offers a retry. The set still counts five: '
            'nothing is silently dropped and nothing is drawn in its place. Offline and unreadable sources reuse 08.8 and 08.9.')

EVENING_ROWS = [('PH-05', 'Friday', 'Dana, from Sorrento'), ('PH-02', '6:48 pm', 'Your camera'), ('PH-03', '6:48 pm', 'Your camera'),
                (None, '7:00 pm', 'Dinner, from seven'), ('PH-01', '8:25 pm', 'Maya'), ('PH-04', '10:40 pm', 'Your camera')]


def ev_row(pid, when, who):
    lead = (f'<div style="flex:none; width:46px; display:flex; justify-content:center;"><div style="border-radius:3px; overflow:hidden;">{photo(pid, h=40)}</div></div>'
            if pid else '<div style="flex:none; width:46px;"></div>')
    return ('<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:54px; border-bottom:1px solid var(--hair-thin);">'
            + lead + f'<div style="flex-grow:1; display:flex; flex-direction:column; gap:2px;"><span class="meta" style="color:var(--ink);">{when.upper()}</span>'
            f'<span class="rsub">{who}</span></div>' + (CHEV if pid else '') + '</div>')


f14 = panel('The evening, in order', '04b.14',
            phone(RECORD + sect('THE EVENING', 'IN ORDER', top=26) + ''.join(ev_row(*r) for r in EVENING_ROWS), 760),
            'Derived value that links, not replaces: the evening&rsquo;s one fact placed among its pictures by time, each row opening the original. '
            'No captions are written for the pictures and no one&rsquo;s arrival is inferred from them.')

MAP_ROWS = [('Home, the selected scroll', 'This viewer, directly', 'The same place in Home', 'Home'),
            ('Social, a received share', 'The original first, then this viewer', 'The same receiving screen', 'Social'),
            ('Life, a record (04b.1)', 'This viewer (04b.2)', 'The record, same scroll', 'Life'),
            ('Life, a search (04b.8)', 'The picture', 'The same query', 'Life'),
            ('Life, a selection (04b.11)', 'Social&rsquo;s preview, the exact outgoing', 'Sent: the set, cleared. Not now: the same selection. Nothing went: the share. Part went: only the undelivered, retry it. Not known: check', 'Life &rarr; Social'),
            ('Any, image unavailable', 'The tile keeps its place (04b.13)', 'Unchanged', 'Life')]
MAP = ('<div class="cstudy"><div style="width:393px; background:var(--card); color:var(--ink); font-family:var(--sans); box-sizing:border-box; padding:18px 20px 20px;">'
       '<div class="eyebrow" style="font-size:9px; color:var(--gold-deep); padding-bottom:10px;">ORIGIN AND RETURN &middot; ONE VIEWER, NO DETOUR</div>'
       + ''.join(f'<div style="border-top:1px solid var(--hair-thin); padding:9px 0; display:grid; grid-template-columns:1fr 1fr; column-gap:10px; row-gap:2px;">'
                 f'<span style="font-size:12px; font-weight:600;">{o}</span><span style="font-size:11px; color:var(--mute); text-align:right;">{own}</span>'
                 f'<span style="font-size:11.5px; color:var(--mute);">Opens: {v}</span><span style="font-size:11.5px; color:var(--mute); text-align:right;">Back: {r}</span></div>'
                 for o, v, r, own in MAP_ROWS)
       + '<div style="font-size:11px; line-height:15px; color:var(--mute); padding-top:10px;">A picture opened from Home or Social never routes through the Life index. '
         'The source owner keeps custody; each root shows the same authorized object.</div></div></div>')
f15 = panel('Where a picture opens from, and returns to', '', MAP,
            'Reviewer map, not product UI. Home and Social draw their own entries; this is the shared contract they meet.')

rows = [[f1, f2, f3, f4], [f5, f6, f7, f8], [f9, f10, f11, f12], [f13, f14, f15]]
head = ('<div class="cb" style="width:1760px;padding:38px"><div style="padding:0 0 10px 0;max-width:1060px">'
        '<div style="display:flex;align-items:center;gap:12px"><span class="ceye">04b &middot; Ordinary photographs</span>'
        '<span class="cpill rev">Review</span></div>'
        '<div class="ctitle" style="padding-top:8px">Saturday&rsquo;s pictures, as they came out.</div>'
        '<div class="cq" style="padding-top:6px">Can I look through the evening&rsquo;s pictures, find one again, and share the ones that are mine, without sorting anything?</div>'
        '<div class="cn" style="padding-top:8px;max-width:980px">Extends 04. A proposal for the one viewer Home and Social also open: whole pictures in their own shapes, '
        'neighbors and zoom, a set that needs no naming, and selection whose doors count only what each can reach. '
        'Fixture: ledger §10, PH-01 to PH-07 and A4. <b>Every picture here is a drawn stand-in, not a photograph</b>: natural color and real low-light '
        'noise cannot be judged until approved pictures exist.</div></div>')
BOARD = HEAD + head + ''.join('<div class="crow">' + ''.join(r) + '</div>' for r in rows) + TAIL
assert BOARD.count('<div class="cpanel"') == 15
assert len(re.findall(r'<div\b', BOARD)) == BOARD.count('</div>'), 'unbalanced divs'
open(os.path.join(OUT, '04b - Ordinary photographs.dc.html'), 'w', encoding='utf-8').write(BOARD)

# ── 00: 04b joins the walkthrough after 04 (idempotent: passes through once 04b is listed) ─
def index_with_04b(b00):
    if '<span class="ceye" style="min-width:60px">04b</span>' in b00:
        return b00
    s = rep(b00, 'SEP 6 2026 · SIXTEEN BOARDS', 'SEP 6 2026 · SEVENTEEN BOARDS')
    s = rep(s, 'The default walkthrough &middot; ten boards, one question each', 'The default walkthrough &middot; eleven boards, one question each')
    r04 = re.search(r'<div style="display:flex;gap:14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var\(--hair-thin\);max-width:900px">'
                    r'<span class="ceye" style="min-width:60px">04</span>.*?</div>', s)
    assert r04
    new = (r04.group(0).replace('>04<', '>04b<', 1).replace('>My original things<', '>Ordinary photographs<', 1)
           .replace('Where are the actual photo, ticket, note, or saved piece?',
                    'Can I look through an evening&rsquo;s pictures, find one again, and share the ones that are mine?', 1)
           .replace('<span class="cpill cur">Current</span>', '<span class="cpill rev">Review</span>', 1))
    assert new != r04.group(0) and '>04b<' in new and 'Ordinary photographs' in new and 'cpill rev' in new
    return s.replace(r04.group(0), r04.group(0) + new, 1)


INDEX = index_with_04b(B00)
open(os.path.join(OUT, '00 - Start here.dc.html'), 'w', encoding='utf-8').write(INDEX)
print('04b', len(BOARD), 'bytes · 00 written ·', 'ok ->', OUT)
