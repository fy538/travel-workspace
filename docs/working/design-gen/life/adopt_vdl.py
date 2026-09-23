#!/usr/bin/env python3
"""Life adopts the shared design package vdl-stage1 0.3 (workbench c13ae951), plus the
September 10 additive-review corrections to 06.6/06.7.

Usage:  adopt_vdl.py BEFORE_DIR AFTER_DIR [--dry]

Consolidation, not redesign. Every edit is an asserted replacement over the verbatim
markup of the live boards; nothing is redrawn from memory.

  1. Styles   every board links the kernel copy of styles.css and vdl.css, and aliases
              its local tokens to the kernel tokens with identical values (the old value
              stays as the fallback, so nothing changes if a stylesheet fails to load).
  2. Doors    the Door construction (.vdl-door): the typed arrow and the hand-drawn svg
              arrow both become the one drawn arrow. Same 13/500, same gold.
  3. Tickets  full tickets and pass-list rows become the shared Ticket where a mode exists
              (flight, ferry, rail, admission). The road row and the wristband stay local:
              no variant exists yet. The 32pt kept-object chips stay local: the shared
              chip is ~26px and Life's V1 chip size was a founder choice.
  4. Reader   the note found through a person's words becomes OriginalReader retrieval.
  5. Notice   the disconnected strip becomes Notice tone=unavailable.
  6. Floor    facet chips rise from 8.5px to 10px in place (03C: density from spacing,
              not smaller type).
  7. 06       the Red Hook comparison credits only the delta the donor supports and drops
              route specifics the fixture does not supply.
"""
import html
import os
import re
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
DRY = '--dry' in sys.argv
os.makedirs(OUT, exist_ok=True)

KERNEL = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'
LOG = {}


def note(board, what, n=1):
    LOG.setdefault(board, {}).setdefault(what, 0)
    LOG[board][what] += n


def rep(t, a, b, n=1):
    c = t.count(a)
    assert c == n, f'expected {n} of {a[:90]!r}, found {c}'
    return t.replace(a, b)


def text_of(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()


def div_end(t, start):
    """Index just past the </div> that closes the <div at start."""
    assert t.startswith('<div', start), t[start:start + 40]
    depth = 0
    for m in re.finditer(r'<div\b|</div>', t[start:]):
        depth += -1 if m.group(0) == '</div>' else 1
        if depth == 0:
            return start + m.end()
    raise AssertionError('unbalanced div')


def dci(name, h, **props):
    attrs = ' '.join(f'{k}="{html.escape(v, quote=True)}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'


# ── 1. styles ─────────────────────────────────────────────────────────────────────
ALIAS = {  # Life token value -> kernel token with the identical value
    '#EFEAE0': '--vk-paper20', '#FBF7EC': '--vk-paper00', '#1B1714': '--vk-ink00',
    '#6E6862': '--vk-ink60', '#B5AFA5': '--vk-ink80', '#B0853A': '--vk-gold60',
    '#8A6628': '--vk-gold80', '#7A2E2E': '--vk-color-surface-oxblood',
    '#3D7050': '--vk-color-surface-confirmGreen', '#2A384B': '--vk-color-surface-planningInkDeep',
    'rgba(27,23,20,0.10)': '--vk-borderHairline', 'rgba(27,23,20,0.06)': '--vk-borderHairlineSoft',
}
FONTS = {'--serif': '--vk-font-serif', '--sans': '--vk-font-sans', '--mono': '--vk-font-mono'}


def styles(board, t):
    t = rep(t, '<helmet>', f'<helmet>\n  <link rel="stylesheet" href="{KERNEL}">\n  <link rel="stylesheet" href="vdl.css">')
    m = re.search(r':root\{([^}]*)\}', t)
    assert m, 'no :root'
    out, kept = [], []
    for decl in [d.strip() for d in m.group(1).split(';') if d.strip()]:
        name, val = decl.split(':', 1)
        name, val = name.strip(), val.strip()
        if val in ALIAS:
            out.append(f'{name}:var({ALIAS[val]}, {val})')
        elif name in FONTS:
            out.append(f'{name}:var({FONTS[name]}, {val})')
        else:
            out.append(f'{name}:{val}')
            kept.append(name)
    t = t[:m.start()] + ':root{' + '; '.join(out) + ';}' + t[m.end():]
    note(board, 'tokens aliased to the kernel', len(out) - len(kept))
    note(board, f'tokens kept local ({", ".join(kept) or "none"})', 0)
    return t


# ── 2. doors ──────────────────────────────────────────────────────────────────────
ARROW = ('<svg width="11" height="11" viewBox="0 0 13 13" fill="none" style="margin-left:5px;">'
         '<path d="M2.5 6.5H10M7 3L10.5 6.5L7 10" stroke="#8A6628" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
DOOR = '<span class="vdl-door vk-t-bodySmMedium">'


def doors(board, t):
    t, n1 = re.subn(r'<span class="door">([^<]*)</span>' + re.escape(ARROW), lambda m: f'{DOOR}{m.group(1)}</span>', t)
    t, n2 = re.subn(r'<span class="door">([^<]*?)\s*&rarr;</span>', lambda m: f'{DOOR}{m.group(1)}</span>', t)
    left = len(re.findall(r'class="door"', t))
    note(board, 'doors on the shared Door construction', n1 + n2)
    if left:
        note(board, 'doors left local (other construction)', left)
    return t


# ── 6. type floor: facet chips ────────────────────────────────────────────────────
FACET = re.compile(r'(<div style="height:24px; border-radius:12px; border:1px solid var\(--(?:ink|hairline)\); '
                   r'background:(?:var\(--card\)|transparent); display:inline-flex; align-items:center; padding:0 10px;">'
                   r'<span style="font-family:var\(--mono\); font-size:)8\.5px(; font-weight:700; letter-spacing:0\.8px;)')


def facets(board, t):
    t, n = FACET.subn(r'\g<1>10px\g<2>', t)
    if n:
        note(board, 'facet labels 8.5px -> 10px', n)
    return t


# ── 3. tickets ────────────────────────────────────────────────────────────────────
FERRY = dict(mode='ferry', density='full', kicker='FERRY · ALILAURO', date='AUG 19 2026', fromCode='SOR',
             fromName='Sorrento', toCode='CAPRI', toName='Marina Grande',
             fields='SAIL=11:20;CROSSING=25 MIN;DECK=OPEN · AFT', status='SAILED · AUG 19', barcode='yes')
FLIGHT = dict(mode='flight', density='full', kicker='FLIGHT · DELTA 264', date='AUG 14 2026', fromCode='JFK',
              fromName='New York', toCode='NCE', toName='Nice',
              fields='DEPART=19:40;ARRIVE=09:25 +1;SEAT=23A;CONF=DL8X2K', status='FLOWN · AUG 15 · 09:41', barcode='yes')


def expect_text(region, props):
    """The drawn ticket must say exactly what the component will say."""
    txt = text_of(region)
    want = [props['kicker'], props['date'], props['fromCode'], props['fromName'], props['toCode'], props['toName'],
            props['status']] + [x for kv in props['fields'].split(';') for x in kv.split('=')]
    for w in want:
        assert w in txt, f'drawn ticket lacks {w!r}: {txt[:200]}'
    rest = txt
    for w in sorted(want, key=len, reverse=True):
        rest = rest.replace(w, ' ', 1)
    assert not rest.strip(), f'drawn ticket has text the component would drop: {rest.strip()!r}'


def full_ticket(board, t, anchor, wrapper_prefix, props, keep_wrap):
    """Replace the drawn ticket whose card starts with wrapper_prefix before anchor."""
    i = t.find(anchor)
    assert i >= 0 and t.find(anchor, i + 1) < 0, f'anchor {anchor[:50]!r} not unique'
    a = t.rfind(wrapper_prefix, 0, i)
    assert a >= 0 and i - a < 1200, 'wrapper not found near anchor'
    e = div_end(t, a)
    expect_text(t[a:e], props)
    t = t[:a] + keep_wrap.format(dci('Ticket', 220, **props)) + t[e:]
    note(board, f'full ticket -> Ticket {props["mode"]} full')
    return t


CENTERED = '<div style="display:flex; justify-content:center;"><div style="width:349px; background:var(--card);'
OBJECT_CARD = '<div style="margin:22px 22px 0 22px; background:var(--card); border:1px solid var(--hairline); border-radius:14px;'

# pass-list rows (04): glyph -> mode
ROW = '<div style="margin:8px 22px 0 22px; height:58px;'
GLYPH = {'M1.8 8.6 L13.2': 'flight', 'M1.6 9.6 Q3.8': 'ferry', 'M4 2.5 H11 Q12.5': 'rail',
         'M2.4 12.6 V5.4': 'admission', 'M3 12.5 L6.2 2.5': 'road'}
MISSING = []


STUB = 'font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:0.6px; color:var(--mute); white-space:nowrap;'


def pass_rows(board, t):
    """The pass list stays local as a whole. Ticket's row cannot express two of its selected variants —
    the road mode (NCE→SOR) and the date stub on the leading edge (NYP→BOS, NYP→HUD, VIE→VCE) — and
    converting only the other six would put two row constructions in one list. In place, only the
    corrections the reviewed baseline names: stubs 9px -> 10px (03C), the title that ran over its stub
    now ends in an ellipsis like its subtitle, and the reserved violet leaves the admission stub (02D)."""
    starts = [m.start() for m in re.finditer(re.escape(ROW), t)]
    assert len(starts) == 10, f'expected 10 pass rows, found {len(starts)}'
    out, pos, lead, road = [], 0, [], []
    for a in starts:
        e = div_end(t, a)
        seg = t[a:e]
        title = html.unescape(re.search(r'letter-spacing:0\.5px; white-space:nowrap;">([^<]+)<', seg).group(1))
        path = re.search(r'<path d="([^"]+)"', seg).group(1)
        mode = next((m for k, m in GLYPH.items() if path.startswith(k)), None)
        assert mode, f'unknown glyph in row {title}'
        stub_at = seg.find('<div style="width:82px;')
        body_at = seg.find('<div style="flex-grow:1;')
        if 0 <= stub_at < body_at:
            lead.append(title)
        if mode == 'road':
            road.append(title)
        assert seg.count(STUB) == 1, f'stub style not found once in {title}'
        seg = seg.replace(STUB, STUB.replace('font-size:9px', 'font-size:10px'))
        if title.startswith('FCO→JFK'):
            seg = rep(seg, 'letter-spacing:0.5px; white-space:nowrap;">',
                      'letter-spacing:0.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">')
            note(board, 'pass row title that ran over its stub now ends in an ellipsis (FCO→JFK)')
        if mode == 'admission':
            seg = rep(seg, ' background:rgba(124,91,168,0.07);', '')
            note(board, 'admission stub: reserved violet tint removed, as 02D rules (dot kept)')
        if DRY:
            print(f'   row {title:48s} mode={mode:9s} stub-leading={title in lead}')
        out.append(t[pos:a])
        out.append(seg)
        pos = e
    out.append(t[pos:])
    note(board, 'pass list kept local; stubs 9px -> 10px in place', 10)
    MISSING.append('04 pass list: Ticket row has no road mode (' + ', '.join(road) + ')')
    MISSING.append('04 pass list: Ticket row has no leading-edge stub (' + ', '.join(lead) + ')')
    return ''.join(out)


# ── 4. reader: the note found through her words (05.6) ───────────────────────────
RET_ROW = '<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:54px; border-bottom:1px solid var(--hair-thin);">'


def retrieval(board, t):
    m = re.search(r'Her note &middot; the pasta night</span>\s*<span class="rsub">From Maya &middot; in Shared with Maya</span>', t)
    assert m and len(re.findall(r'Her note &middot; the pasta night</span>\s*<span class="rsub">', t)) == 1
    i = m.start()
    a = t.rfind(RET_ROW, 0, i)
    assert a >= 0 and i - a < 900, 'row shell not found'
    e = div_end(t, a)
    assert text_of(t[a:e]) == 'Her note · the pasta night From Maya · in Shared with Maya AUG 30', text_of(t[a:e])
    t = t[:a] + '<div style="margin:0 22px;">' + dci('OriginalReader', 64, density='retrieval',
                                                      noteTitle='Her note · the pasta night',
                                                      detail='From Maya · in Shared with Maya', date='AUG 30') + '</div>' + t[e:]
    note(board, 'note result -> OriginalReader retrieval')
    return t


# ── 5. notice: the disconnected return (P3.5) ────────────────────────────────────
OFFLINE = ('<div style="margin:22px 22px 0 22px; padding:8px 11px; border:1px dashed var(--hairline); border-radius:8px;">'
           '<span class="meta" style="white-space:normal; line-height:15px; display:block;">NO CONNECTION &middot; 9:15 PM</span></div>')


def notice(board, t):
    t = rep(t, OFFLINE, '<div style="margin:22px 22px 0 22px;">' + dci('Notice', 40, tone='unavailable', title='No connection · 9:15 pm') + '</div>')
    note(board, 'offline strip -> Notice unavailable')
    return t


# ── 7. 06: credit only the supported delta ───────────────────────────────────────
def red_hook(board, t):
    t = rep(t, 'CHAT &middot; SAT 4:10 PM &middot; FROM FORT GREENE</div>', 'CHAT &middot; SAT 4:10 PM</div>')
    t = rep(t, 'CHAT &middot; SAT 4:10 PM &middot; FROM FORT GREENE &middot; NO ENTRUSTED CONTEXT</div>',
            'CHAT &middot; SAT 4:10 PM &middot; NO ENTRUSTED CONTEXT</div>')
    t = rep(t, 'Ferry over from Atlantic Basin &mdash; the part you like. Last boat back is 8:10, so come home the way you did in June: '
               'the walk over the bridge, about fifty minutes. The B61 runs till late if the legs say no.',
            'Take the ferry in &mdash; the part you like. Last boat back is 8:10, so plan the B61 home; it runs till late.')
    t = rep(t, 'Ferry over from Atlantic Basin &mdash; it is the good way in. Last boat back is 8:10, so plan the B61 home; it runs till late.',
            'Take the ferry in &mdash; it is the good way in. Last boat back is 8:10, so plan the B61 home; it runs till late.')
    t = rep(t, '&middot; your two evenings</div>', '&middot; your line about the ferry</div>')
    t = rep(t, 'Same origin, same conditions, same live check, same recommendation as 06.7 &mdash; only eligible history differs. '
               'What it buys is narrow: the return she actually chose and liked in June is offered first, and she is not asked which '
               'she would prefer. The car stays out of it &mdash; taking the ferry over does not put it at the far end. Life supplied '
               'the two evenings and her line; the live times are Places&rsquo;.',
            'Same question, same moment, same live check and the same advice as 06.7 &mdash; only eligible history differs. '
            'What it adds is one phrase: the ferry is offered as the part she likes, because she wrote that it is the good part. '
            'Her June walk home is not offered as tonight&rsquo;s way back; a past mode is not a current route. '
            'Life supplied her line; the live times are Places&rsquo;.')
    t = rep(t, 'A competent answer on its own terms: same origin, same check, a recommendation, and a viable way home. History does not '
               'unlock ordinary transport advice. The delta is one line of fit &mdash; the bridge walk she already knows she likes, offered '
               'instead of the default bus &mdash; and one question not asked. Close to a tie, which is a fair result.',
            'A competent answer on its own terms: the same check, a recommendation and a viable way home. History does not unlock '
            'ordinary transport advice, and neither answer asks her anything. The difference is one phrase of fit &mdash; a tie in '
            'substance, which is a fair result. Where she starts from is Places&rsquo; live input; this fixture does not name it, so '
            'whether the ferry is right for her tonight stays open.')
    for gone in ('FORT GREENE', 'Atlantic Basin', 'chose and liked', 'question not asked', 'bridge'):
        assert gone not in t, gone
    note(board, '06.6/06.7 corrected (origin and route specifics removed, delta credited to her line only)')
    return t


# ── run ───────────────────────────────────────────────────────────────────────────
BOARDS = sorted(f for f in os.listdir(SRC) if f.endswith('.dc.html'))
assert len(BOARDS) == 14, BOARDS
for f in BOARDS:
    b = f.split(' - ')[0]
    t = open(os.path.join(SRC, f), encoding='utf-8').read()
    t = styles(b, t)
    t = doors(b, t)
    t = facets(b, t)
    if b == '04':
        t = full_ticket(b, t, 'FLIGHT &middot; DELTA 264</span>', OBJECT_CARD, FLIGHT, '<div style="margin:22px 22px 0 22px;">{}</div>')
        t = full_ticket(b, t, '<span class="kick">FERRY &middot; ALILAURO</span>', CENTERED, FERRY, '<div>{}</div>')
        t = pass_rows(b, t)
    if b == '05':
        t = full_ticket(b, t, '<span class="kick">FERRY &middot; ALILAURO</span>', CENTERED, FERRY, '<div>{}</div>')
        t = retrieval(b, t)
    if b == '03b':
        t = full_ticket(b, t, '<span class="kick">FERRY &middot; ALILAURO</span>', CENTERED, FERRY, '<div>{}</div>')
    if b == 'R0':
        t = full_ticket(b, t, '<span class="kick">FLIGHT &middot; DELTA 264</span>', CENTERED, FLIGHT, '<div>{}</div>')
    if b == '03':
        # The same inherited 1x overflow fixed on 07 on September 10: a 58-character nowrap caption, 389px wide,
        # in a 349px column. Shortened, not truncated, and allowed to wrap at larger text.
        t = rep(t, '<div class="meta" style="padding-top:6px;">HER NOTE &middot; SENT TO YOU AFTER SATURDAY&rsquo;S DINNER &middot; CITY-LEVEL</div>',
                '<div class="meta" style="padding-top:6px; white-space:normal;">HER NOTE &middot; AFTER SATURDAY&rsquo;S DINNER &middot; CITY-LEVEL</div>')
        note(b, 'clipped caption under her note shortened, as on 07 (inherited 1x overflow)')
    if b == 'P3':
        t = notice(b, t)
    if b == '06':
        t = red_hook(b, t)
    if not DRY:
        open(os.path.join(OUT, f), 'w', encoding='utf-8').write(t)

for b, items in LOG.items():
    print(b)
    for k, v in items.items():
        print(f'   {v:3d}  {k}' if v else f'        {k}')
print('MISSING VARIANTS:')
for m in MISSING:
    print('  ', m)
print('dry run' if DRY else f'written -> {OUT}')
