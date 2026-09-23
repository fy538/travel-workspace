#!/usr/bin/env python3
"""Two bounded canvases for the September 12 coverage assignment.

  08 · The actual source        query -> the original email body, photo fit/zoom, document pages,
                                loading, offline, a source that cannot be opened, and the same query back.
  09 · Finishing a local action scope, consequential confirmation, cancellation, partial failure, return,
                                on the selection 04 and workbench 02D already draw.

Usage: build_0915.py SRC_DIR OUT_DIR

Method: the head, the board shell and whole donor frames are sliced verbatim from the live boards;
new frames are written with the project's own classes and the shared package's constructions
(Ticket, Notice, .vdl-sheet, .vdl-btn, .vdl-door). Nothing is redrawn from memory, no new control
family is invented, and no fact enters that the record does not already hold.
"""
import html
import os
import re
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
B05 = open(os.path.join(SRC, '05 - Find it again.dc.html'), encoding='utf-8').read()
B04 = open(os.path.join(SRC, '04 - My original things.dc.html'), encoding='utf-8').read()

HEAD = B05[:B05.find('</helmet>') + len('</helmet>')] + '\n'
TAIL = '</div>\n</x-dc>\n</body>\n</html>\n'


def div_end(t, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', t[start:]):
        depth += -1 if m.group(0) == '</div>' else 1
        if depth == 0:
            return start + m.end()
    raise AssertionError('unbalanced div')


def frame(board, cap):
    """The <div class="cphone">…</div> of the frame whose caption starts with cap."""
    i = board.find(f'<span class="ccap">{cap}')
    assert i >= 0, f'no frame captioned {cap!r}'
    j = board.find('<div class="cphone">', i)
    assert 0 < j - i < 900, f'phone not found under {cap!r}'
    return board[j:div_end(board, j)]


def slice_between(board, a, b, note=''):
    i = board.find(a)
    assert i >= 0, f'missing anchor {a[:60]!r} {note}'
    j = board.find(b, i)
    assert j > i, f'missing end anchor {b[:60]!r} {note}'
    return board[i:j]


# ── the project's own shapes, taken from the live boards ───────────────────────────
PHONE_OPEN = ('<div class="cphone"><div style="width: 393px; background: var(--paper); color: var(--ink); '
              'font-family: var(--sans); box-sizing: border-box; display: flex; flex-direction: column; position:relative;">')
TABBAR = slice_between(B05, '<div style="border-top:1px solid var(--hairline); background:var(--card); display:flex; padding:10px 22px 22px 22px;',
                       '</div></div></div><div class="cnote">') + '</div>'
def slice_div(board, anchor, nth=0, note=''):
    """The whole <div …> that starts at the nth occurrence of anchor."""
    idx, i = -1, -1
    for _ in range(nth + 1):
        i = board.find(anchor, idx + 1)
        assert i >= 0, f'missing anchor {anchor[:60]!r} {note}'
        idx = i
    return board[i:div_end(board, i)]


CHROME = slice_div(B05, '<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;">', note='back + search chrome')


def sect(label, right=''):
    r = f'<span class="barmeta" style="margin-left:auto;">{right}</span>' if right else ''
    return ('<div style="margin:34px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; '
            f'display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{label}</span>{r}</div>')


def gut(inner, top=12):
    return f'<div style="margin:{top}px 22px 0 22px;">{inner}</div>'


def door(text):
    return f'<div style="display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium">{text}</span></div>'


def row(title, sub, meta='', chev=True, glyph=''):
    g = glyph or ''
    c = ('<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" '
         'stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>') if chev else ''
    m = f'<span class="meta">{meta}</span>' if meta else ''
    return ('<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:54px; '
            f'border-bottom:1px solid var(--hair-thin);">{g}<div style="flex-grow:1; display:flex; flex-direction:column; gap:2px;">'
            f'<span style="font-family:var(--serif); font-size:15.5px; line-height:20px; font-weight:600;">{title}</span>'
            f'<span class="rsub">{sub}</span></div>{m}{c}</div>')


def dci(name, h, **props):
    attrs = ' '.join(f'{k}="{html.escape(v, quote=True)}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'


def stamp(text, color='--mute'):
    return f'<span class="meta" style="white-space:normal; line-height:15px; display:block; color:var({color});">{text}</span>'


def sheet(title, body, primary, secondary, tint=''):
    """The shared sheet construction (vdl.css), over the frame it acts on."""
    return ('<div class="vdl-scrim" style="position:absolute; inset:0; display:flex; flex-direction:column; '
            'justify-content:flex-end; padding-top:0;">'
            '<div class="vdl-sheet"><div class="vdl-sheet-handle"></div>'
            f'<div class="vdl-sheet-head"><div style="font-family:var(--serif); font-size:21px; line-height:26px; font-weight:600;">{title}</div></div>'
            f'<div style="font-family:var(--sans); font-size:13.5px; line-height:19px; color:var(--mute);">{body}</div>'
            f'{tint}'
            '<div class="vdl-sheet-actions">'
            f'<span class="vdl-btn primary vk-t-labelSemibold" style="color:var(--vk-color-white)">{primary}</span>'
            f'<span class="vdl-btn secondary vk-t-labelSemibold">{secondary}</span>'
            '</div></div></div>')


def phone(inner, minh=None):
    open_tag = PHONE_OPEN if minh is None else PHONE_OPEN.replace('width: 393px;', f'width: 393px; min-height: {minh}px;')
    # TABBAR is balanced; the two closes are the phone's inner frame and the .cphone shell.
    return open_tag + inner + '<div style="flex-grow:1;"></div>' + TABBAR + '</div></div>'


def panel(cap, ident, body, note, pill=''):
    p = f'<span class="cpill {pill[0]}">{pill[1]}</span>' if pill else ''
    idt = f'<span class="ccap" style="color:var(--mute-light)">{ident}</span>' if ident else ''
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center">'
            f'<span class="ccap">{cap}</span>{p}{idt}</div>{body}<div class="cnote">{note}</div></div>')


def board(eyebrow, pill, title, question, note, rows):
    head = (f'<div class="cb" style="width:1760px;padding:38px"><div style="padding:0 0 10px 0;max-width:1060px">'
            f'<div style="display:flex;align-items:center;gap:12px"><span class="ceye">{eyebrow}</span>'
            f'<span class="cpill {pill[0]}">{pill[1]}</span></div>'
            f'<div class="ctitle" style="padding-top:8px">{title}</div>'
            f'<div class="cq" style="padding-top:6px">{question}</div>'
            f'<div class="cn" style="padding-top:8px;max-width:980px">{note}</div></div>')
    body = ''.join('<div class="crow">' + ''.join(r) + '</div>' for r in rows)
    return HEAD + head + body + TAIL


# ── 08 · the actual source ─────────────────────────────────────────────────────────
_SEARCH = slice_div(B05, '<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:12px;">', note='search + facets')
assert _SEARCH.count('>pasta<') == 1 and 'FOUND IN' not in _SEARCH, 'search slice picked up results'


def searchbar(query):
    """05's own field and lens facets, carrying this canvas's query."""
    return _SEARCH.replace('>pasta<', f'>{query}<', 1)
_PLATE = slice_between(B04, '<svg width="100%" height="120" viewBox="0 0 300 120" style="display:block; border-radius:6px;">',
                       '</svg>', 'photo plate') + '</svg>'


def plate(h, w='100%'):
    """04's drawn photograph, at the height this frame gives it. Same artwork, cropped to fill."""
    return _PLATE.replace('<svg width="100%" height="120"', f'<svg width="{w}" height="{h}"', 1) \
                 .replace('style="display:block; border-radius:6px;"',
                          'preserveAspectRatio="xMidYMid slice" style="display:block; border-radius:6px;"', 1)
FERRY_SOURCE = frame(B05, 'Asked: the Sorrento&ndash;Capri ferry ticket')

EMAIL_HEAD = (gut('<div style="display:flex; gap:26px;">'
                  '<div><div class="kicker" style="color:var(--mute);">FROM</div>'
                  '<div style="font-family:var(--sans); font-size:13.5px; line-height:18px; padding-top:4px;">Alilauro bookings</div></div>'
                  '<div><div class="kicker" style="color:var(--mute);">RECEIVED</div>'
                  '<div style="font-family:var(--sans); font-size:13.5px; line-height:18px; padding-top:4px;">Aug 12, 2026</div></div>'
                  '</div>', top=14))

EMAIL_BODY = gut('<div style="background:var(--card); border:1px solid var(--hairline); border-radius:12px; padding:16px 18px;">'
                 '<div style="font-family:var(--serif); font-size:16px; line-height:24px; color:var(--ink);">'
                 'Sorrento (SOR) &rarr; Marina Grande, Capri<br>19 August 2026 &middot; 11:20<br>Crossing 25 min &middot; Deck: open, aft'
                 '</div>'
                 '</div>', top=14)

f081 = panel('The query, and what it found', '08.1',
             phone(searchbar('ferry capri') + sect('FOUND IN SEVEN YEARS', '2 RESULTS') + sect('PASSES &amp; TICKETS', '1')
                   + gut(dci('Ticket', 58, mode='ferry', density='row', rowTitle='SOR→CAPRI · ALILAURO',
                             rowDetail='In The coast · sailed', stub='AUG 19'), top=8)
                   + sect('EPISODES', '1')
                   + row('The coast &middot; Sorrento, Capri, Amalfi', 'In Nice &rarr; Rome', 'AUG 19'), 1000),
             'The query is the person&rsquo;s own words. The ticket answers first because the question named an object. '
             'Everything below returns here.')

f082 = panel('The object, and where its source lives', '08.2', FERRY_SOURCE,
             'Drawn already (05.9), unchanged. The ticket is a projection: the fields Vesper parsed. '
             '&ldquo;See the original email&rdquo; is the door this canvas continues.')

f083 = panel('The email, as received', '08.3',
             phone(CHROME
                   + sect('THE ORIGINAL &middot; EMAIL')
                   + EMAIL_HEAD + EMAIL_BODY
                   + gut(door('Back to ferry capri'), top=20), 1000),
             'The message itself, in its own lines, behind the door 05.9 offers; the ticket is a projection of these lines. '
             'DECIDED, NOT DISPLAYED: the fixture holds no further prose and none is written. Nothing is re-rendered, summarized or corrected; '
             'a wrong line is wrong in the message as sent.')

f084 = panel('A photograph, whole', '08.4',
             phone(CHROME + gut('<div style="display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">'
                                'PHOTOGRAPH &middot; YOUR CAMERA</span><span class="barmeta" style="margin-left:auto;">FIT</span></div>', top=6)
                   + gut(plate(240), top=12)
                   + gut('<div style="display:flex; align-items:baseline;">'
                         '<span style="font-family:var(--serif); font-size:17px; line-height:22px;">Capri, 4:12pm</span>'
                         '<span class="meta" style="margin-left:auto;">AUG 19</span></div>', top=14)
                   + sect('WHERE IT LIVES')
                   + row('The coast &middot; Sorrento, Capri, Amalfi', 'In Nice &rarr; Rome', 'AUG 19'), 980),
             'The object is the image, so it opens whole before anything is said about it. '
             'Occurrence and containment sit below, as on 04. DECIDED, NOT DISPLAYED: whole image, nothing cropped.')

f085 = panel('The same photograph, closer', '08.5',
             phone(CHROME + gut('<div style="display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">'
                                'PHOTOGRAPH &middot; YOUR CAMERA</span><span class="barmeta" style="margin-left:auto;">2&times;</span></div>', top=6)
                   + gut('<div style="height:240px; border-radius:6px; overflow:hidden; position:relative;">'
                         '<div style="position:absolute; left:-495px; top:-96px; width:698px;">' + plate(480, w='698') + '</div>'
                         '</div>', top=12)
                   , 700),
             'Zoom is reading: the same file, larger. DECIDED, NOT DISPLAYED: nothing is sharpened, re-encoded or generated. '
             'Native pinch, pan, double-tap-to-fit and their behavior under larger text need implementation evidence.')

f086 = panel('A document, page by page', '08.6',
             phone(CHROME + gut('<div style="display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">'
                                'MENU &middot; A KEPT DOCUMENT</span><span class="barmeta" style="margin-left:auto;">PAGE 1 OF 2</span></div>', top=6)
                   + gut('<div style="background:var(--card); border:1px solid var(--hairline); border-radius:10px; padding:18px 20px;">'
                         '<div style="font-family:var(--serif); font-size:17px; line-height:25px;">The Sorrento menu</div>'
                         '<div class="voice" style="padding-top:8px;">&ldquo;&hellip;spaghetti alla Nerano, mantecato al momento&hellip;&rdquo;</div>'
                         '<div style="padding-top:12px;">' + stamp('SCANNED') + '</div></div>', top=12)
                   + gut('<div style="display:flex; gap:7px; align-items:center;">'
                         '<div style="height:24px; border-radius:12px; border:1px solid var(--ink); background:var(--card); display:inline-flex; align-items:center; padding:0 10px;">'
                         '<span style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:0.8px; color:var(--ink);">1</span></div>'
                         '<div style="height:24px; border-radius:12px; border:1px solid var(--hairline); background:transparent; display:inline-flex; align-items:center; padding:0 10px;">'
                         '<span style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:0.8px; color:var(--mute);">2</span></div>'
                         '</div>', top=14)
                   + gut(door('Next page'), top=14)
                   + sect('WHAT IT SUPPORTS')
                   + row('The pasta question', 'Saved source &middot; in The pasta question', 'SOURCE'), 900),
             'A document renders as itself, with its own pages, not ticketified. The page count is the source&rsquo;s, '
             'not a guess: two pages were scanned, so two pages are offered. No text is claimed beyond what was kept.')

f087 = panel('While it opens', '08.7',
             phone(CHROME + gut('<div class="kicker" style="color:var(--mute);">THE ORIGINAL &middot; EMAIL</div>', top=6)
                   + gut(dci('Notice', 44, tone='pending', title='Opening the original…'), top=12)
                   + gut(dci('Ticket', 220, mode='ferry', density='full', kicker='FERRY · ALILAURO', date='AUG 19 2026',
                             fromCode='SOR', fromName='Sorrento', toCode='CAPRI', toName='Marina Grande',
                             fields='SAIL=11:20;CROSSING=25 MIN;DECK=OPEN · AFT', status='SAILED · AUG 19', barcode='yes'), top=14), 700),
             'Loading is a state of the source, not of the record. The projection does not disappear while the original arrives, '
             'and it is still labelled a projection.')

f088 = panel('Offline', '08.8',
             phone(CHROME + gut('<div class="kicker" style="color:var(--mute);">THE ORIGINAL &middot; EMAIL</div>', top=6)
                   + gut(dci('Notice', 92, tone='unavailable', title='No connection',
                             body='The message opens when you’re back online.'), top=12)
                   + sect('FROM THE TICKET')
                   + gut('<div style="font-family:var(--serif); font-size:16px; line-height:24px;">'
                         'Sorrento (SOR) &rarr; Marina Grande &middot; 19 August 2026 &middot; 11:20</div>', top=12)
                   + gut(door('Try again'), top=14), 780),
             'Offline is small: what is here, and when the rest returns. DECIDED, NOT DISPLAYED: nothing stands in for the message. '
             'Actual offline custody &mdash; which originals live on the device at all &mdash; needs implementation evidence.')

f089 = panel('When the source itself will not open', '08.9',
             phone(CHROME + gut('<div class="kicker" style="color:var(--mute);">THE ORIGINAL &middot; EMAIL</div>', top=6)
                   + gut(dci('Notice', 116, tone='failed', title='This message can’t be opened',
                             body='The file is here but can’t be read.', primary='Report this original',
                             secondary='Detach it from the day'), top=12)
                   + sect('FROM THE TICKET')
                   + gut('<div style="font-family:var(--serif); font-size:16px; line-height:24px;">'
                         'Sorrento (SOR) &rarr; Marina Grande &middot; 19 August 2026 &middot; 11:20</div>', top=12), 720),
             'DECIDED, NOT DISPLAYED: no replacement original is generated; a projection never becomes the source; the day and episode are unchanged. '
             'Reporting is repair, detaching is containment, and neither invents '
             'the message back. Causal repair &mdash; what a report actually fixes &mdash; needs implementation evidence.')

f0810 = panel('Back to the same query', '08.10',
              phone(searchbar('ferry capri') + sect('PASSES &amp; TICKETS', '1', )
                    + gut(dci('Ticket', 58, mode='ferry', density='row', rowTitle='SOR→CAPRI · ALILAURO',
                              rowDetail='In The coast · sailed', stub='AUG 19'), top=8), 820),
              'Back is a return, not a new search: the same words, the same facet, the same position. '
              'The countercheck is query &rarr; actual source &rarr; the same query.')

BOARD08 = board('08 &middot; The actual source', ('cur', 'Current'), 'The original, not its summary.',
                'When I ask for the ticket, can I read the message it came from?',
                'A ticket is a projection of a source. This canvas follows the door on 05.9 to the message itself, then to a photograph '
                'that opens whole and zooms, a document with its own pages, and the three honest failures: loading, offline, and an original '
                'that will not open. Nothing is generated to stand in for a source, and Back returns to the same query and position.',
                [[f081, f082, f083, f084], [f085, f086, f087, f088], [f089, f0810]])

# ── 09 · finishing a local action ─────────────────────────────────────────────────
PHOTOS = frame(B04, 'Photographs')
GRID = slice_div(B04, '<div style="margin:12px 22px 0 22px; display:flex; gap:6px; flex-wrap:wrap;', note='photograph grid')
TILE = '<div style="width:65px; height:65px; border-radius:4px; overflow:hidden; border:1px solid var(--hairline); position:relative; flex:none;">'
CHECK = ('<span style="position:absolute; right:3px; top:3px; width:16px; height:16px; border-radius:8px; background:var(--ink); '
         'display:flex; align-items:center; justify-content:center;"><svg width="9" height="9" viewBox="0 0 12 12" fill="none">'
         '<path d="M2.5 6.4 L4.8 8.6 L9.5 3.6" stroke="#FBF7EC" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')


def chosen(grid, n=3):
    """The same grid with its first n tiles marked chosen — the state 02D's specimen shows."""
    out, pos, done = [], 0, 0
    while done < n:
        i = grid.find(TILE, pos)
        assert i >= 0, 'fewer tiles than the selection needs'
        e = div_end(grid, i)
        tile = grid[i:e]
        out.append(grid[pos:i])
        out.append(tile[:-len('</div>')].replace('border:1px solid var(--hairline)', 'border:1.5px solid var(--ink)', 1) + CHECK + '</div>')
        pos, done = e, done + 1
    out.append(grid[pos:])
    return ''.join(out)


SELECTED = chosen(GRID)


def selbar(n):
    return gut('<div style="display:flex; align-items:center;">'
               f'<span class="kicker" style="color:var(--ink);">{n} SELECTED</span>'
               '<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto;">Done</span></div>', top=6)


def actionbar(left, right):
    return gut('<div style="display:flex; gap:10px; border-top:1px solid var(--hairline); padding-top:14px;">'
               f'<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1;">{left}</span>'
               f'<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1;">{right}</span></div>', top=18)


f091 = panel('Choosing, as it already works', '09.1', PHOTOS,
             'Drawn already (04), unchanged. Select, then act: the grid, the count, and the two doors beneath it. '
             'This canvas starts after the choosing.')

f092 = panel('Three chosen, and what they are', '09.2',
             phone(gut('<div style="display:flex; align-items:center;"><span class="kicker" style="color:var(--mute);">'
                       'EVERYTHING KEPT &middot; PHOTOGRAPHS</span></div>', top=20)
                   + selbar(3) + SELECTED
                   + gut('<div class="rsub">Two are yours. One is Maya&rsquo;s, shared into the record on Aug 30.</div>', top=14)
                   + actionbar('Export 3', 'Delete 3'), 900),
             'The workbench specimen ends here. What the three actually are decides what each door can do, '
             'so the mix is stated before anything is pressed.')

f093 = panel('Export: what is yours to take', '09.3',
             phone(gut('<div style="display:flex; align-items:center;"><span class="kicker" style="color:var(--mute);">'
                       'EVERYTHING KEPT &middot; PHOTOGRAPHS</span></div>', top=20) + selbar(3) + SELECTED
                   + sheet('Export 2 of 3',
                           'Your two save as files. Maya&rsquo;s stays in the record; it&rsquo;s hers to share.',
                           'Export 2', 'Cancel'), 900),
             'Export scope is narrower than the selection, and the sheet says so in the person&rsquo;s terms rather than refusing at the end. '
             'Whether a recipient may keep an independent copy at all is still the owner&rsquo;s decision.',
             pill=('rev', 'Review'))

f094 = panel('Delete: the consequence, named', '09.4',
             phone(gut('<div style="display:flex; align-items:center;"><span class="kicker" style="color:var(--mute);">'
                       'EVERYTHING KEPT &middot; PHOTOGRAPHS</span></div>', top=20) + selbar(3) + SELECTED
                   + sheet('Delete 3 photographs?',
                           'They leave your record. The day and its episode stay. Maya still has hers.',
                           'Delete 3', 'Cancel'), 900),
             'Deletion names what goes and what stays, once, at the moment of action. DECIDED, NOT DISPLAYED: it is not correction, detach or release (09.8). '
             'The threshold is carried by words, not by color: oxblood stays a live-time mark in Life.')

f095 = panel('Stopping', '09.5',
             phone(gut('<div style="display:flex; align-items:center;"><span class="kicker" style="color:var(--mute);">'
                       'EVERYTHING KEPT &middot; PHOTOGRAPHS</span></div>', top=20) + selbar(3) + SELECTED
                   + gut('<div class="rsub">Two are yours. One is Maya&rsquo;s, shared into the record on Aug 30.</div>', top=14)
                   + actionbar('Export 3', 'Delete 3'), 900),
             'Cancel returns to the moment before the sheet, with the same three still chosen. '
             'DECIDED, NOT DISPLAYED: nothing was exported or deleted, so nothing says so.')

f096 = panel('When part of it fails', '09.6',
             phone(gut('<div style="display:flex; align-items:center;"><span class="kicker" style="color:var(--mute);">'
                       'EVERYTHING KEPT &middot; PHOTOGRAPHS</span></div>', top=20)
                   + gut(dci('Notice', 128, tone='failed', title='1 of 2 didn’t export',
                             body='One file couldn’t be read. The other is saved where you chose.',
                             primary='Try the one that failed', secondary='Done'), top=14)
                   + sect('WHAT HAPPENED, PER FILE')
                   + row('Capri, 4:12pm', 'Exported &middot; 10:06', 'DONE', chev=False)
                   + row('The stairs, 11:40', 'Not exported &middot; the file could not be read', 'FAILED', chev=False)
                   , 860),
             'Partial failure is reported per file, with the successful part already kept. '
             'Retrying resumes the one that failed instead of running all three again.')

f097 = panel('After it runs', '09.7',
             phone(gut('<div style="display:flex; flex-direction:column; gap:10px;">'
                       '<span class="kicker" style="color:var(--mute);">EVERYTHING KEPT &middot; PHOTOGRAPHS</span>'
                       '<span style="font-family:var(--serif); font-weight:600; font-size:26px; line-height:30px; letter-spacing:-0.5px;">Photographs</span>'
                       '<span class="kicker" style="color:var(--mute);">211 HELD &middot; 7 UNPLACED &middot; 2019 &mdash; NOW</span></div>', top=20)
                   + gut(dci('Notice', 64, tone='applied', title='3 deleted · 10:07', body='Selection cleared.'), top=14)
                   + gut(door('Undo'), top=12) + GRID, 980),
             'The return is the same grid, with the count moved and the selection cleared. '
             'How long Undo lasts, and what deletion does to dependent compositions, need implementation evidence.')

f098 = panel('Four verbs, and who owns them', '09.8',
             phone(gut('<div class="kicker" style="color:var(--mute);">ON ONE OBJECT</div>', top=20)
                   + row('Correct', 'A fact is wrong &middot; the record changes, the object stays', 'LIFE', chev=False)
                   + row('Detach', 'It does not belong to this day &middot; the object stays kept', 'LIFE', chev=False)
                   + row('Release', 'Stop an interpretation being used &middot; the source stays', 'LIFE', chev=False)
                   + row('Delete', 'The original goes &middot; what it supported is marked', 'LIFE', chev=False)
                   + sect('EVERYTHING ELSE')
                   + gut(door('Your data, in Settings'), top=12), 760),
             'The four verbs are kept apart because their consequences differ. DECIDED, NOT DISPLAYED: account-level export, imports, '
             'later use and continuing help stay with You &amp; Trust; Life is not a second settings system. A drawing authorizes no export and no deletion.')

BOARD09 = board('09 &middot; Finishing a local action', ('cur', 'Current'), 'Three chosen, then what actually happens.',
                'When I act on the things I chose, what is in scope, what can I stop, and what if part of it fails?',
                'Selection is already drawn on 04 and on the shared workbench. This canvas finishes it: what each door can actually reach, '
                'a confirmation that names the consequence, a cancel that costs nothing, failure reported per file, and the return. '
                'Export and deletion have different scopes, and nothing here authorizes either.',
                [[f091, f092, f093, f094], [f095, f096, f097, f098]])

open(os.path.join(OUT, '08 - The actual source.dc.html'), 'w', encoding='utf-8').write(BOARD08)
open(os.path.join(OUT, '09 - Finishing a local action.dc.html'), 'w', encoding='utf-8').write(BOARD09)
print('08 frames:', BOARD08.count('class="cpanel"'), 'bytes', len(BOARD08))
print('09 frames:', BOARD09.count('class="cpanel"'), 'bytes', len(BOARD09))
for b, n in ((BOARD08, '08'), (BOARD09, '09')):
    assert b.count('<x-dc>') == 1 and b.rstrip().endswith('</html>'), n
    assert b.count('<div class="cphone">') == b.count('class="cpanel"'), n
    # unbalanced divs nest the next panel inside the previous one and the row silently becomes a column
    assert len(re.findall(r'<div\b', b)) == b.count('</div>'), (n, len(re.findall(r'<div\b', b)), b.count('</div>'))
print('ok ->', OUT)
