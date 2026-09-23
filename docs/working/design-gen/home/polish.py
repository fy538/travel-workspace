"""Aesthetic pass 2026-09-08 — applied to the live Home boards by pattern, inside phone regions only where copy is touched.
Rules: (1) one card physics (radius 16, quiet lift); (2) photo slots as light hatched plates, not dark blocks; (3) design
commentary out of the phone's mono lines (FIXTURE, NO CTA, TWO LINES AT MOST, SLOT); (4) balanced wrapping on reads and titles.
Usage: python3 polish.py <in_dir> <out_dir>   (files named NN.html in, board names out)
"""
import re, sys, os, zlib
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
NAMES = {'13': '13 - Photograph Treatments', '00': '00 - Index', '01': '01 - Parts', '02': '02 - Persona A - The New Yorker', '03': '03 - Persona B - Back from Europe', '04': '04 - Persona C - New User', '05': '05 - Wedge - Trip Forming', '06': '06 - Places - From Friends', '07': '07 - Ledger and Decisions', '08': '08 - Seam with Life', '08b': '08b - Seam with Life - Home to Life', '09': '09 - Forms', '10': '10 - States', '11': '11 - Return and Continuity', '12': '12 - Why This, Chat, and Degraded States'}
LIFT = 'box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07)'
HATCH = 'background: repeating-linear-gradient(135deg, rgba(176,133,58,0.14) 0 7px, rgba(176,133,58,0.05) 7px 14px); border: 1px solid rgba(27,23,20,0.08); box-sizing: border-box'

def phone_regions(h):
    """Spans of phone-like containers (393px wide, paper background)."""
    out = []
    for m in re.finditer(r'<div style="width: 393px;[^"]*background: #EFEAE0', h):
        s = m.start(); depth = 0; e = None
        for mm in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0: e = s + mm.end(); break
        if e and not (out and s < out[-1][1]): out.append((s, e))
    return out

def polish_phone(p):
    # (3) commentary out of mono lines
    for tok in [' &middot; FIXTURE &middot; NO CTA', ' &middot; FIXTURE &middot; TWO LINES AT MOST', ' &middot; NO CTA', ' &middot; TWO LINES AT MOST', ' &middot; FIXTURE', ' &middot; SLOT', 'FIXTURE &middot; ']:
        p = p.replace(tok, '')
    # (2) photo slots: dark block → hatched plate; label colour; numbered markers ink-on-plate
    def slot(m):
        s = m.group(0).replace('background: #2A241E', HATCH).replace('color: #CFC7BA', 'color: #8A6628; font-size: 9px; letter-spacing: 0.7px; right: 12px; line-height: 12px').replace('color: #8F877C;">', 'color: #8A6628; font-size: 9px; letter-spacing: 0.7px; right: 12px; line-height: 12px;">', 1)
        s = s.replace('background: #B0853A; color: #1B1714', 'background: #1B1714; color: #FBF7EC')
        s = s.replace('YOUR PHOTOGRAPH &middot; ', 'PHOTOGRAPH &middot; ')  # the unit's caption already says whose
        return s
    p = re.sub(r'<div style="[^"]*background: #2A241E[^"]*">(?:(?!<div style="[^"]*background: #2A241E).)*?</div>\s*</div>', slot, p, flags=re.S)
    return p

def polish_all(h):
    # (1) card physics, everywhere
    h = h.replace('border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06)', 'border-radius: 16px; ' + LIFT)
    h = h.replace('box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06)', LIFT)
    h = h.replace('border-radius: 14px; padding: 11px 14px 10px; box-shadow: 0 1px 3px rgba(27,23,20,0.06)', 'border-radius: 16px; padding: 12px 14px 10px; ' + LIFT)
    h = re.sub(r'(border-radius: 1[4-8]px;[^"]*?)box-shadow: 0 1px 2px rgba\(27,23,20,0\.05\)', lambda m: m.group(1) + LIFT, h)
    # (4) balanced wrapping on reads and titles
    for pat in ['font-weight: 600; font-size: 30px; line-height: 34px; letter-spacing: -0.01em;', 'font-size: 17px; line-height: 22px; font-weight: 500; color: #1B1714;', 'font-size: 20px; line-height: 25px; font-weight: 600; color: #1B1714;', 'font-size: 22px; line-height: 26px; font-weight: 600; color: #1B1714;', 'font-weight: 600; font-size: 17px; line-height: 22px; color: #1B1714;']:
        h = h.replace(pat, pat + ' text-wrap: balance;')
    return h

# ---- pass 2 (founder, 09-08): the two span instruments, and the double hairline under a section head ----------------
MONO_ = "JetBrains Mono, monospace"
def _x(hours, x0, w): return x0 + hours * (w / 6.0)          # the axis is always 4 PM → 10 PM
def _fit(x, t, x0, w):
    """Anchor a span label at its span's start; if it would run past the axis, right-align it to the axis end."""
    est = len(re.sub(r'&[a-z]+;', 'x', t)) * 6.9
    return (x, 'start') if x + est <= x0 + w else (x0 + w, 'end')
def _label(x, y, t, fill, bold=True, anchor='start'):
    return f'<text x="{x:.1f}" y="{y}" text-anchor="{anchor}" font-family="{MONO_}" font-size="10"{" font-weight=\"700\"" if bold else ""} letter-spacing="0.8" fill="{fill}">{t}</text>'
def single_span_svg(W):
    """One held span (the pier, 6:30–8) with sunset as a moment: a tick through the span, labelled on the axis line."""
    x0, w = 2, W - 4
    a, b, sun = _x(2.5, x0, w), _x(4.0, x0, w), _x(3.067, x0, w)
    return (f'<svg width="{W}" height="52" viewBox="0 0 {W} 52" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
            + _label(*_fit(a, 'THE PIER · 6:30–8', x0, w)[:1], 11, 'THE PIER &middot; 6:30&ndash;8', '#8A6628', anchor=_fit(a, 'THE PIER · 6:30–8', x0, w)[1])
            + f'<rect x="{x0}" y="23" width="{w}" height="6" rx="3" fill="rgba(27,23,20,0.07)"/>'
            + f'<rect x="{a:.1f}" y="20" width="{b - a:.1f}" height="12" rx="6" fill="#B0853A"/>'
            + f'<line x1="{sun:.1f}" y1="15" x2="{sun:.1f}" y2="37" stroke="#1B1714" stroke-width="1.2"/>'
            + _label(sun, 49, 'SUNSET 7:04', '#1B1714', anchor='middle')
            + _label(x0, 49, '4 PM', '#8F877C', bold=False) + _label(x0 + w, 49, '10', '#8F877C', bold=False, anchor='end') + '</svg>')
def two_option_svg(W):
    """Two candidates on one axis, each on its own track; the status is part of the label line, not a tag butting the bar."""
    x0, w = 2, W - 4
    pa, pb, sun = _x(2.5, x0, w), _x(4.0, x0, w), _x(3.067, x0, w)
    ga, gb = _x(3.0, x0, w), _x(5.0, x0, w)
    return (f'<svg width="{W}" height="96" viewBox="0 0 {W} 96" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
            + _label(_fit(pa, 'THE PARK · 6:30–8 · OPEN LATE', x0, w)[0], 11, 'THE PARK &middot; 6:30&ndash;8 &middot; OPEN LATE', '#8A6628', anchor=_fit(pa, 'THE PARK · 6:30–8 · OPEN LATE', x0, w)[1])
            + f'<rect x="{x0}" y="23" width="{w}" height="6" rx="3" fill="rgba(27,23,20,0.07)"/>'
            + f'<rect x="{pa:.1f}" y="20" width="{pb - pa:.1f}" height="12" rx="6" fill="#B0853A"/>'
            + f'<line x1="{sun:.1f}" y1="15" x2="{sun:.1f}" y2="37" stroke="#1B1714" stroke-width="1.2"/>'
            + _label(sun, 48, 'SUNSET 7:04', '#1B1714', anchor='middle')
            + _label(_fit(ga, 'THE GARDEN · 7–9 · NEEDS A NAME', x0, w)[0], 62, 'THE GARDEN &middot; 7&ndash;9 &middot; NEEDS A NAME', '#6E6862', bold=False, anchor=_fit(ga, 'THE GARDEN · 7–9 · NEEDS A NAME', x0, w)[1])
            + f'<rect x="{x0}" y="73" width="{w}" height="6" rx="3" fill="rgba(27,23,20,0.07)"/>'
            + f'<rect x="{ga:.1f}" y="70" width="{gb - ga:.1f}" height="12" rx="6" fill="#FBF7EC" stroke="#6E6862" stroke-width="1.2" stroke-dasharray="3 3"/>'
            + _label(x0, 93, '4 PM', '#8F877C', bold=False) + _label(x0 + w, 93, '10', '#8F877C', bold=False, anchor='end') + '</svg>')
def pass2(h):
    # the instruments: replace each svg that carries the signature texts
    def swap(m):
        svg = m.group(0)
        W = int(re.search(r'<svg width="(\d+)"', svg).group(1))
        if 'NEEDS A NAME' in svg: return two_option_svg(W)
        if 'THE PIER &middot; 6:30&ndash;8' in svg and 'SUNSET 7:04' in svg: return single_span_svg(W)
        return svg
    h = re.sub(r'<svg width="\d+" height="\d+" viewBox="[^"]+" fill="none" style="width: 100%; height: auto; margin-top: 8px;">.*?</svg>', swap, h, flags=re.S)
    # the hairline: a row that opens its group no longer draws its own top line under the section head's
    h = h.replace('.row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); }',
                  '.row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); } .row:first-child { border-top: none; }')
    # a shadow the first pass doubled
    h = h.replace(', 0 5px 14px rgba(27,23,20,0.07), 0 5px 14px rgba(27,23,20,0.07)', ', 0 5px 14px rgba(27,23,20,0.07)')
    return h

# ---- pass 3 (09-08): one grammar for every span instrument --------------------------------------------------------
# axis: hours from the axis start; spans are (label, start_h, end_h, kind) with kind gold | muted | struck; moments are (h, label)
def instrument_svg(W, axis, tracks, moments=(), open_end=None):
    x0, w = 2, W - 4; start_h, end_h, l0, l1 = axis; span_h = end_h - start_h
    X = lambda h: x0 + (h - start_h) * (w / span_h)
    n = len(tracks); H_ = 52 if n == 1 else 96; out = f'<svg width="{W}" height="{H_}" viewBox="0 0 {W} {H_}" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
    ys = [(11, 23, 20)] if n == 1 else [(11, 23, 20), (62, 73, 70)]
    for (label, a, b, kind), (ly, ty, py) in zip(tracks, ys):
        xa, xb = X(a), min(X(b), x0 + w)
        color = {'gold': '#8A6628', 'muted': '#6E6862', 'struck': '#6E6862'}[kind]
        lx, anchor = _fit(xa, re.sub(r'&[a-z]+;', 'x', label), x0, w)
        out += _label(lx, ly, label, color, bold=(kind == 'gold'), anchor=anchor)
        out += f'<rect x="{x0}" y="{ty}" width="{w}" height="6" rx="3" fill="rgba(27,23,20,0.07)"/>'
        if kind == 'gold':
            if open_end == label:
                out += f'<defs><linearGradient id="fade{zlib.crc32(label.encode()) % 9973}" x1="0" x2="1"><stop offset="0.6" stop-color="#B0853A"/><stop offset="1" stop-color="#B0853A" stop-opacity="0"/></linearGradient></defs>'
                out += f'<rect x="{xa:.1f}" y="{py}" width="{xb - xa:.1f}" height="12" rx="6" fill="url(#fade{zlib.crc32(label.encode()) % 9973})"/>'
            else:
                out += f'<rect x="{xa:.1f}" y="{py}" width="{xb - xa:.1f}" height="12" rx="6" fill="#B0853A"/>'
        elif kind == 'muted':
            out += f'<rect x="{xa:.1f}" y="{py}" width="{xb - xa:.1f}" height="12" rx="6" fill="rgba(176,133,58,0.28)"/>'
        else:
            out += f'<rect x="{xa:.1f}" y="{py}" width="{xb - xa:.1f}" height="12" rx="6" fill="#FBF7EC" stroke="#6E6862" stroke-width="1.2" stroke-dasharray="3 3"/>'
            out += f'<line x1="{xa - 3:.1f}" y1="{py + 6}" x2="{xb + 3:.1f}" y2="{py + 6}" stroke="#6E6862" stroke-width="1.2"/>'
    ay = 49 if n == 1 else 93; ty = 23 if n == 1 else 23
    for mo in moments:
        h, label = mo[0], mo[1]; kind = mo[2] if len(mo) > 2 else 'tick'
        xm = X(h); my = 49 if n == 1 else 48
        if kind == 'tick':
            out += f'<line x1="{xm:.1f}" y1="{ty - 8}" x2="{xm:.1f}" y2="{ty + 14}" stroke="#1B1714" stroke-width="1.2"/>'
        else:  # 'after': a muted continuation from the first track's end to h, labelled beneath its middle
            xa = X(tracks[0][2]); out += f'<rect x="{xa:.1f}" y="{py + 2}" width="{xm - xa:.1f}" height="8" rx="4" fill="rgba(176,133,58,0.30)"/>'; xm = (xa + xm) / 2
        est = len(re.sub(r'&[a-z]+;', 'x', label)) * 6.9
        if xm + est / 2 > x0 + w - 26: x_, anc = xm + 3, 'end'
        elif xm - est / 2 < x0 + 34: x_, anc = xm - 3, 'start'
        else: x_, anc = xm, 'middle'
        out += _label(x_, my, label, '#1B1714' if kind == 'tick' else '#6E6862', bold=(kind == 'tick'), anchor=anc)
    out += _label(x0, ay, l0, '#8F877C', bold=False) + _label(x0 + w, ay, l1, '#8F877C', bold=False, anchor='end') + '</svg>'
    return out

SPECS = {
    'THE SHOW &middot; 8&ndash;10': lambda W: instrument_svg(W, (17, 24, '5 PM', '12'), [('THE SHOW &middot; 8&ndash;10', 20, 22, 'gold')], moments=[(22.83, '+25 HOME', 'after')]),
    'THE PIER &middot; LOW WATER 2:40&ndash;5': lambda W: instrument_svg(W, (14, 18, '2 PM', '6'), [('THE PIER &middot; LOW WATER 2:40&ndash;5', 14.67, 17, 'gold')], moments=[(17.5, 'BACK BY 5:30')]),
    'DOOR &rarr; GATE &middot; 3:40&ndash;4:45': lambda W: instrument_svg(W, (15, 19, '3 PM', '7'), [('DOOR &rarr; GATE &middot; 3:40&ndash;4:45', 15.67, 16.75, 'gold')], moments=[(18.08, 'BOARDS 6:05')]),
    'TRAIN 11:40 &middot; PALACE 1:30': lambda W: instrument_svg(W, (8, 15, '8 AM', '3'), [('TRAIN 11:40 &middot; PALACE 1:30', 11.67, 13.5, 'gold'), ('THE ORIGINAL &middot; 9:10 TRAIN &middot; OUT', 9.17, 11.0, 'struck')], moments=[(14, 'TICKETS 2 PM')]),
    'THE NEW ONE &middot; 9:30 PM': lambda W: instrument_svg(W, (16, 22, '4 PM', '10'), [('THE NEW ONE &middot; 9:30 PM &rarr; LAND 9:40 AM', 21.5, 22.6, 'gold'), ('THE ORIGINAL &middot; 6:45 PM &middot; OUT', 18.75, 20.25, 'struck')], open_end='THE NEW ONE &middot; 9:30 PM &rarr; LAND 9:40 AM'),
}
def pass3(h):
    def swap(m):
        svg = m.group(0); W = int(re.search(r'<svg width="(\d+)"', svg).group(1))
        for sig, fn in SPECS.items():
            if f'>{sig}</text>' in svg: return fn(W)
        return svg
    return re.sub(r'<svg width="\d+" height="\d+" viewBox="[^"]+" fill="none" style="width: 100%; height: auto; margin-top: 8px;">.*?</svg>', swap, h, flags=re.S)

# ---- pass 4 (09-08): one eyebrow, and the tab bar on the page's own paper -------------------------------------------
def pass4(h):
    # a unit's opening line is the sans eyebrow with its register dot (plan ink); mono stays for labels over lanes and rows
    h = h.replace('<div style="display: flex; align-items: center; gap: 10px;"><span class="kickm">',
                  '<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: #2A384B; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: #2A384B;">')
    # the tab bar sits on the page paper, separated by the hairline only
    h = h.replace('border-top: 1px solid rgba(27,23,20,0.10); background: #FBF7EC; display: flex; padding: 10px 22px 22px 22px;',
                  'border-top: 1px solid rgba(27,23,20,0.10); background: #EFEAE0; display: flex; padding: 10px 22px 22px 22px;')
    return h

# ---- pass 5 (09-08, "fix all"): the list's left edge, the ring chip, two copy caps, and captions in sentence case ------
PROPER = set("""Maya Alex Dana Theo Nadia Mira Rafa Jonah Sarah Mike Sorrento Amalfi Capri Positano Rome Nice Naples Paris Lisbon Sintra Porto
Alfama Baixa Kyoto Brooklyn New York Sunset Park Red Hook Court Street Fifth Lilia Roscioli Alilauro Wikimedia Commons Leclercq MacLarty Virgil
Aeneas Campanian Sorrentine Cumae Lattari Campi Flegrei Punta Campanella Marina Grande Monte San Michele Pippo Geol Soc London Home Life Places
Chat Vesper Monday Tuesday Wednesday Thursday Friday Saturday Sunday Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Trips Page Occasion Plan
Europe Italy Europe Nerano Sirens Ramiro Belcanto Bedford Harbor Book Open House Flea Hall Lisbon Sunday Sundays Mondays Fridays Saturdays
Thursdays Tuesdays Wednesdays Nice Rome Alfama Mediterranean Atlantic Andrea Persona""".split())
ACR = set("CTA CC BY SA NC CC0 UNESCO GSL SP JFK FCO SOR PM AM NYC HL HR OK ID MP CSS HTML SVG PNG DC P1 P2 P3 T1 T2 T3 H1 H2 H3 H4 H5 D2 L".split())
def _sentence(t):
    parts = re.split(r'(&[a-z]+;|&#\d+;)', t); out = []
    for i, part in enumerate(parts):
        if i % 2: out.append(part); continue
        words = part.split(' '); res = []
        for j, wd in enumerate(words):
            core = re.sub(r'[^A-Za-z0-9\-/]', '', wd)
            if not core: res.append(wd); continue
            if re.search(r'\d', core) or core in ACR or re.match(r'^[A-Z]{1,2}-\d', core) or core.startswith('§'): res.append(wd); continue
            cap = wd.capitalize() if False else wd[0] + wd[1:].lower()
            lw = wd.lower()
            if core.capitalize() in PROPER: res.append(re.sub(re.escape(core), core.capitalize(), wd, 1)); continue
            if len(core) == 1 and core.isalpha():
                prev = words[j-1].lower() if j else ''
                res.append(wd if prev == 'the' else lw); continue
            res.append(lw)
        out.append(' '.join(res))
    t = ''.join(out)
    # capitalise the first letter and after a full stop
    def cap_first(m): return m.group(1) + m.group(2).upper()
    t = re.sub(r'^(\s*(?:&[a-z]+;\s*)*)([a-z])', cap_first, t)
    t = re.sub(r'(\.\s+)([a-z])', cap_first, t)
    return t
CAPTION_STYLE = 'font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;'
def captions_outside(h):
    def conv(m): return f'<div style="{CAPTION_STYLE}">{_sentence(m.group(2))}</div>'
    return re.sub(r'<div class="fn" style="(line-height: 14px;|color: #8F877C;)">([^<]+)</div>', conv, h)
def pass5_phone(p):
    # 1. every small row mark sits in a 15px cell at one weight
    def cell_(m):
        inner = m.group(1)
        inner = inner.replace('width: 7px; height: 7px;', 'width: 8px; height: 8px;').replace('border: 1.5px dashed', 'border: 1.3px dashed').replace('border: 1.5px solid', 'border: 1.3px solid')
        return f'<span style="width: 15px; display: inline-flex; justify-content: center; flex: none;"><span style="{inner} flex: none;"></span></span>'
    p = re.sub(r'<span style="(width: 7px; height: 7px; border-radius: 4px; (?:border: 1\.5px (?:dashed|solid) #(?:6E6862|7A2E2E); box-sizing: border-box;|background: #(?:B0853A|1B1714);)) flex: none;"></span>', cell_, p)
    # 2. a card that sits among rows goes bare: the rows' left edge is the list's edge
    opener_re = re.compile(r'<div style="background: #FBF7EC; border-radius: 1[68]px; box-shadow: [^"]*; padding: 16px; display: flex; flex-direction: column; overflow: hidden;">')
    i = 0
    while True:
        mo = opener_re.search(p, i)
        if not mo: break
        i = mo.start(); opener = mo.group(0)
        depth = 0; e = None
        for m in re.finditer(r'<div\b|</div>', p[i:]):
            depth += 1 if m.group() == '<div' else -1
            if depth == 0: e = i + m.end(); break
        if e and p.startswith('<div style="height: 14px;"></div><div class="row"', e):
            p = p[:i] + '<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06); display: flex; flex-direction: column; overflow: hidden;">' + p[i + len(opener):e] + p[e + len('<div style="height: 14px;"></div>'):]
        i += 10
    # 3. the arrangement chip: the dashed seat, not a ring that reads as a control
    p = p.replace('<span style="width: 6px; height: 6px; border-radius: 3px; border: 1.3px solid #2A384B; box-sizing: border-box; flex: none;"></span></span>',
                  '<span style="width: 9px; height: 9px; border-radius: 5px; border: 1.2px dashed #2A384B; box-sizing: border-box; flex: none; margin-left: 1px;"></span></span>')
    # 4–5. copy caps: one mono line per option; the read's sub-line on one line
    p = p.replace('TONIGHT &middot; THE METHOD IS BELOW', 'TONIGHT')
    p = p.replace('Day three of thirteen &middot; Rome on Monday &middot; dinner at ours the day after you land.', 'Day three of thirteen &middot; Rome on Monday.')
    p = p.replace('First open since Aug 28 &middot; Friday the 18th at Lilia with Maya and Alex.', 'First open since Aug 28 &middot; Friday the 18th at Lilia.')
    return p

# ---- pass 6 (09-08, photographs): reference images graded and handled; the person's pair stacked --------------------
GRADE = 'filter: saturate(0.72) sepia(0.22) contrast(0.95);'
PAPER_MULT = '<div style="position: absolute; inset: 0; background: #EFEAE0; mix-blend-mode: multiply; pointer-events: none;"></div>'
def pass6_phone(p):
    # reference plates: 3:2, no rounding, graded, the page paper multiplied over, nothing on the image, the caption beneath
    def plate(m):
        img, cap = m.group(2), m.group(3)
        img = img.replace('display: block;"', 'display: block; ' + GRADE + '"')
        return (f'<div style="height: 233px; border-radius: 0; position: relative; overflow: hidden; margin-top: 10px; isolation: isolate;">{img}{PAPER_MULT}</div>'
                f'<div style="font-family: \'EB Garamond\', Georgia, serif; font-size: 15px; line-height: 20px; color: #1B1714; margin-top: 8px;">{cap}</div>')
    p = re.sub(r'<div style="height: (?:130|150)px; border-radius: 10px; background: #8F877C; position: relative; overflow: hidden; margin-top: 10px;">(<img src="data:image/[^"]+" alt="" style="[^"]*">)()<div style="position: absolute; left: 0; right: 0; bottom: 0; padding: 22px 12px 8px 12px; background: linear-gradient\(transparent, rgba\(27,23,20,0\.72\)\);"><div style="font-family: \'EB Garamond\', Georgia, serif; font-size: 14px; line-height: 18px; color: #FBF7EC;">([^<]+)</div></div></div>',
               lambda m: plate(type('M', (), {'group': lambda self, i: {2: m.group(1), 3: m.group(3)}[i]})()), p)
    # the person's two photographs: a matched pair, stacked, never side by side
    i = 0
    while True:
        i = p.find('<div style="display: flex; gap: 10px; margin-top: 10px;"><div style="flex: 1; min-width: 0;">', i)
        if i < 0: break
        depth = 0; e = None
        for m in re.finditer(r'<div\b|</div>', p[i:]):
            depth += 1 if m.group() == '<div' else -1
            if depth == 0: e = i + m.end(); break
        blk = p[i:e]
        if 'PHOTOGRAPH &middot; AUG' in blk:
            blk = blk.replace('<div style="display: flex; gap: 10px; margin-top: 10px;">', '<div style="margin-top: 10px;">', 1)
            blk = blk.replace('<div style="flex: 1; min-width: 0;">', '<div>', 1).replace('<div style="flex: 1; min-width: 0;">', '<div style="margin-top: 10px;">', 1)
            blk = blk.replace('height: 118px;', 'height: 170px;')
            p = p[:i] + blk + p[e:]
        i += 20
    return p

# ---- pass 7 (09-08, founder): the two coast units carry less text; the piece keeps the explanation ---------------------
def pass7_phone(p):
    p = p.replace('The wall under Sorrento is volcanic ash. Down the coast the rock changes, and so does everything built on it.', 'The wall under Sorrento is volcanic ash. Down the coast the rock changes.')
    for body in ['Sorrento sits on tuff from the Campi Flegrei eruptions: soft, flat-topped, with a shallow shelf under the water. Past Punta Campanella the coast is the Lattari&rsquo;s older limestone, a slope that runs straight into deep water; the towns there climb instead of sitting.',
                 'Sorrento sits on a shelf of tuff, ash from the Campi Flegrei eruptions: a flat top, a wall, and a wide shallow shelf under the water. Past Punta Campanella the coast is the Lattari&rsquo;s older limestone: a slope that runs straight into deep water.']:
        p = re.sub(r'<div style="font-size: 13px; line-height: 18px; color: #6E6862; margin-top: 4px;">' + re.escape(body) + r'</div>', '', p)
    p = p.replace('REFERENCE PHOTOGRAPH &middot; WIKIMEDIA COMMONS &middot; G. MACLARTY &middot; CC BY 2.0 &middot; NOT YOUR CAMERA', 'WIKIMEDIA COMMONS &middot; G. MACLARTY &middot; CC BY 2.0')
    p = p.replace('REFERENCE PHOTOGRAPH &middot; WIKIMEDIA COMMONS &middot; P. A. LECLERCQ &middot; CC BY-SA 4.0 &middot; NOT YOUR CAMERA', 'WIKIMEDIA COMMONS &middot; P. A. LECLERCQ &middot; CC BY-SA 4.0')
    return p

# ---- pass 8 (09-08, founder): four more text cuts, measured ------------------------------------------------------------
BODY = r'<div style="font-size: 13px; line-height: 18px; color: #6E6862; margin-top: 4px;">'
def pass8_phone(p):
    p = p.replace('Sorrento said it in one word, Roscioli in a sentence: the pasta goes into the sauce early, with a ladle of its water, and the starch binds it at the end.', 'The pasta goes into the sauce early, with a ladle of its water; the starch binds it.')
    p = p.replace('Sorrento to Capri: sailed 11:20, on the island by 4:12, the last swim at Marina Grande', 'Sorrento to Capri: the 11:20, the island by 4:12, the last swim')
    for body in ['One ticket and two photographs make the day. The crossing is twenty-five minutes; what you did until 4:12 was not kept.',
                 'The tuff face looks north-west, so the shelf below it goes into shadow first; the harbour front holds the afternoon.']:
        p = re.sub(BODY + re.escape(body) + r'</div>', '', p)
    # the comparison plates: the date lives in the under-label; the on-plate label goes
    p = re.sub(r'<div class="fn" style="position: absolute; left: 12px; bottom: 10px; color: #8A6628; font-size: 9px; letter-spacing: 0.7px; right: 12px; line-height: 12px;">PHOTOGRAPH &middot; AUG (16|21)</div>', '', p)
    p = p.replace('font-weight: 700;">SORRENTO &middot; TUFF</div>', 'font-weight: 700;">SORRENTO &middot; TUFF &middot; AUG 16</div>').replace('font-weight: 700;">AMALFI &middot; LIMESTONE</div>', 'font-weight: 700;">AMALFI &middot; LIMESTONE &middot; AUG 21</div>')
    return p

# ---- pass 9 (09-08 consolidation assignment): must-corrects and reconciliations, by copy -----------------------------
def pass9_phone(p):
    # 12 · the stale frame: last-known state, an available original, an unavailable fresh assessment — not "never stale"
    p = p.replace('LAST TRUE FRIDAY 6:40 PM &middot; REFRESHING &middot; WEATHER AND TIDE WITHHELD UNTIL THEY ARE CURRENT', 'AS OF FRIDAY 6:40 PM &middot; CHECKING NOW &middot; WEATHER, TIDE AND WHAT IS STILL OPEN WAIT FOR THE CHECK')
    p = p.replace('THE RECORD IS LOCAL; IT IS NEVER STALE', 'YOUR ORIGINALS OPEN OFFLINE &middot; SHARED STATE IS AS OF FRIDAY &middot; CURRENT FACTS WAIT FOR THE CHECK')
    p = p.replace('4 going &middot; as of Friday', '4 going as of Friday &middot; not checked since')
    # 10 · the block: hiding a person never changes attendance; the arrangement owner's count stands
    p = p.replace('SATURDAY &middot; FORMING &middot; 3 GOING', 'SATURDAY &middot; FORMING &middot; 4 GOING')
    # 08c · a check is a check, not a watch
    p = p.replace('<span class="fn" style="margin-left: auto;">CHECKED 6:12</span>', '<span class="fn" style="margin-left: auto;">CHECKED ONCE &middot; 6:12</span>')
    p = p.replace('THE OPERATOR&rsquo;S TIMETABLE + YOUR TICKET &middot; CHECKED 6:12', 'THE OPERATOR&rsquo;S TIMETABLE + YOUR TICKET &middot; CHECKED ONCE AT 6:12, NOT WATCHED')
    p = p.replace('One ticket, one email. Checked this morning at 6:12.', 'One ticket, one email. Checked once this morning at 6:12; nothing follows unless you ask.')
    p = p.replace('Sorrento, day three. The strip is what Home showed at 8:40.', 'Sorrento, day three. As Home read it at 8:40; the arrangement itself lives in the Plan.')
    # 12 · provider unknown: a check on open, not a standing re-ask
    p = re.sub(r'RE-ASKING EVERY [A-Z ]*MINUTES', 'ASKED AGAIN WHEN YOU OPEN &middot; NOT WATCHED', p)
    p = p.replace('LAST HEARD 4:52 &middot; THE FEED IS NOT ANSWERING', 'LAST HEARD 4:52 &middot; THE FEED IS NOT ANSWERING &middot; ASKED AGAIN ON OPEN')
    # ferry: a ticket is a ticket, not evidence of sailing
    p = p.replace('>SAILED<', '>TICKET<').replace('TICKET 11:20 &middot; PHOTOGRAPHS 4:12, 6:40', 'TICKET 11:20 (NOT PROOF OF SAILING) &middot; PHOTOGRAPHS 4:12, 6:40')
    # H7: the source line names the kind of image; grading alone does not
    p = p.replace('WIKIMEDIA COMMONS &middot; G. MACLARTY &middot; CC BY 2.0', 'REFERENCE &middot; WIKIMEDIA COMMONS &middot; G. MACLARTY &middot; CC BY 2.0').replace('WIKIMEDIA COMMONS &middot; P. A. LECLERCQ &middot; CC BY-SA 4.0', 'REFERENCE &middot; WIKIMEDIA COMMONS &middot; P. A. LECLERCQ &middot; CC BY-SA 4.0')
    p = p.replace('REFERENCE &middot; REFERENCE &middot;', 'REFERENCE &middot;')
    return p
def pass9_board(k, h):
    if k == '10':
        h = h.replace('Quieter, not emptier</div>', 'Quieter, not emptier; the count stands</div>', 1)
        h = h.replace('No banner, no dimmed slot &middot; the Page is complete at its New size', 'No banner, no dimmed slot &middot; attendance is the arrangement owner&rsquo;s fact (four); the blocked person is not shown, not removed &middot; the viewer-safe treatment is Social&rsquo;s to lead: PROVISIONAL')
    if k == '12':
        h = h.replace('The Life door notes that the record is local and never stale.', 'The Life door opens the person&rsquo;s own originals offline; shared state is shown as of Friday and fresh facts wait for the check.')
        h = h.replace('Last true Friday; live facts withheld', 'Last known Friday; a check runs; fresh facts withheld until it returns')
        h = h.replace('State rows stand &middot; the mechanism holds; the numbers wait &middot; the record is never stale', 'Shared state stands as last known &middot; your originals open &middot; the mechanism holds; the numbers and what is still open wait for the check &middot; nothing here is promised current')
    if k == '08':
        h = h.replace('A &middot; PROVISIONAL CANON', 'A &middot; PROVISIONAL CANON (&sect;11.16)').replace('B &middot; FREEDOM-PRESERVING', 'B &middot; PROPOSED, NOT CANON')
        h = h.replace('The waiting window, and the recommendation', 'The waiting window, and the recommendation (proposed; founder decision needed)')
        h = h.replace('Tell the five (CTA); Dana&rsquo;s row has no door until the message is sent', 'Tell the five (CTA); Dana&rsquo;s row stays reachable and keeps its own door (corrected 09-08: a lower-ranked decision is never locked behind another action)')
    if k == '05':
        h = h.replace('applied to the launch wedge:', 'applied to group travel as a specialization of everyday Home (the accepted strategy is everyday-first; &ldquo;launch wedge&rdquo; below is the thesis&rsquo;s earlier claim):')
    if k == '01':
        h = h.replace('THE HOME UNION AS DRAWN TODAY (38 KINDS) &middot; MERGED 2026-09-05 &middot; THREE ADMITTED 2026-09-08', 'THE HOME UNION AS DRAWN TODAY &middot; 35 KINDS ADMITTED + 3 PROPOSED (09-08) &middot; MERGED 2026-09-05')
        h = h.replace('One cell per kind in the 38-kind union (build manifest &sect;1.0&ndash;1.6; four kinds admitted 09-05, three on 09-08 after the comparison with the pre-pivot Trips page)', 'One cell per kind: the 35-kind union the build manifest declares (&sect;1.0&ndash;1.6; four admitted 09-05) plus three PROPOSED on 09-08 after the comparison with the pre-pivot Trips page (the temporal strip, the work receipt, the money row): proposals, not admitted runtime types')
        h = h.replace('<span class="gB">BUILD &middot; ADMITTED 09-08</span>', '<span class="gB">PROPOSED 09-08</span>')
        h = h.replace('grading must not be the only distinction between a reference and persona', 'grading must not be the only distinction between a reference and persona')
        h = h.replace('plate rules (09-08): reference images graded warm paper, 3:2, full width, nothing on them, caption beneath; the person&rsquo;s own photographs untreated, one per unit or a matched stacked pair; never side-by-side thumbnails', 'plate rules (09-08): reference images graded warm paper, 3:2, full width, nothing on them, caption beneath and the source line naming them REFERENCE (grading alone is not the distinction); the person&rsquo;s own photographs untreated; a friend&rsquo;s original named by its author; one per unit or a matched stacked pair; never side-by-side thumbnails')
    return h

# ---- pass 10 (09-09 second pass): ticket vs sailing, a withdrawn source, and the priority recommendation -------------
def pass10_phone(p):
    # HL-3: an issued ticket time is not evidence of sailing
    p = p.replace('Sorrento &rarr; Capri &middot; sailed 11:20', 'Sorrento &rarr; Capri &middot; ticket 11:20')
    p = p.replace('>SAILED &middot; AUG 19<', '>TICKET &middot; AUG 19<')
    p = p.replace('Capri, by the 11:20 ferry.', 'Capri, on the 11:20 ticket.')
    # the return after the correction keeps the correction
    p = p.replace('Sorrento to Capri: sailed 11:20, the stairs by 2:05, the island by 4:12, the last swim',
                  'Sorrento to Capri: the 11:20 ticket unused, the 2:40 boat, the stairs at 2:05, the island by 4:12')
    p = p.replace('TICKET 11:20 &middot; PHOTOGRAPHS 2:05, 4:12, 6:40', 'TICKET 11:20, UNUSED &middot; YOUR WORD 2:40 &middot; PHOTOGRAPHS 2:05, 4:12, 6:40')
    # HL-2: the Sunday claim had one source, and it was withdrawn
    p = p.replace('Sundays only, before eleven. Open when this was saved.', 'Open when this was saved. The Sunday claim came from Maya&rsquo;s note and went with it.')
    return p
def pass10_board(k, h):
    if k == '08b':
        h = h.replace('THE FERRY DAY, FROM A TICKET AND TWO PHOTOGRAPHS', 'THE FERRY DAY, FROM A TICKET AND TWO PHOTOGRAPHS')
        h = h.replace('the ferry pass one tap away; the correction &ldquo;I took the 2:40 boat&rdquo; and its effect on the strip and the saved piece; and Home when the import finished while the day was open.',
                      'the ferry pass one tap away; the correction &ldquo;I took the 2:40 boat&rdquo; and its effect on the strip and the saved piece; and Home when the import finished while the day was open. Corrected 09-09: the ticket time is never drawn as evidence of sailing, and the return after the correction keeps the 2:40 boat with the 11:20 ticket unused &mdash; one branch, not two.')
    if k == '07':
        h = h.replace('<div class="shead"><span>HISTORY &middot; THE PHONES THE CURRENT BOARDS REPLACED</span>', '<div style="margin-top: 34px; padding-top: 22px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 8px;"><div class="kick" style="color: #8A6628;">SHARED FIXTURE REVISION &middot; RECORDED 2026-09-09</div><div style="font-family: \'EB Garamond\', Georgia, serif; font-weight: 600; font-size: 20px; line-height: 26px;">The New York bounded set &middot; revision 2 &middot; Home leads</div><div style="font-size: 13.5px; line-height: 20px; color: #6E6862; max-width: 980px;">Drawn on Home 14.1&ndash;14.3b and paired with Places 03.3. The set: the flea under the bridge (the market&rsquo;s own notice; Saturdays through October, today 8 to 3); Open House New York (OHNY; Oct 17&ndash;18, timed registration Tuesday noon to Thursday, walk-ins need none); the L (MTA; after 11 PM Monday to Thursday, daytime normal, end date unknown); the forecast and tide (two stations and the tide table; clear 41&deg;, low water 2:40 to 5, high 8:40); The Harbor Book chapter four (no expiry). Revision 1 (09-08, the Red Hook set) is superseded for this pair and remains Places&rsquo; own material on 03.1 and 03.2. The two owners exchanged fixtures in opposite directions on 09-09; Home leads this revision and Places 03.3 confirms it before changing its receiving view. Every value is a design fixture, not verified provider supply.</div></div>' + '<div class="shead"><span>HISTORY &middot; THE PHONES THE CURRENT BOARDS REPLACED</span>')
    if k == '08':
        h = h.replace('Adopt B&rsquo;s separation of demanded response from available action, and B&rsquo;s waiting posture. Keep A&rsquo;s ranking as the tie-break when cost of delay cannot be judged from evidence. Record this as an amendment to &sect;11.16, not a silent change: the founder decides.',
                      'Evaluate two questions separately: which object should be visually dominant, and which object demands a response from the person. A ranks them together; B separates them and adds the waiting posture. Neither is adopted by this drawing &mdash; the accepted crown behaviour stands until the founder decides, and any change is recorded as an amendment to &sect;11.16, not made silently.')
    return h

# ---- pass 11 (09-10, selected direction): benefit-led reads on the selected scrolls; the corrected returned strip ----
SUN_OLD = 'Clear and cold. Low water at 1:40.'
SUN_NEW = 'The sesame loaf before eleven, then low water at 1:40.'
DZ_OLD  = 'Home. Clear, 79&deg;.'
DZ_NEW  = 'The first walk back, at low water from 3:10.'
SUN_SUBS = [('54&deg; by noon &middot; Brooklyn tonight with Maya &middot; the show Friday.', 'Clear and cold, 54&deg; by noon &middot; Brooklyn tonight with Maya &middot; the show Friday.')]
DZ_SUBS  = [('Landed 6:40 &middot; dinner at ours tomorrow with Maya and Alex.', 'Home. Clear, 79&deg; &middot; landed 6:40 &middot; dinner at ours tomorrow with Maya and Alex.')]
def _lead(h, old, new, subs, count=-1):
    h = h.replace(old, new, count) if count > 0 else h.replace(old, new)
    for a, b in subs:
        if b not in h: h = h.replace(a, b)
    return h
# the reconstruction strip: the corrected sailing becomes its own evidenced mark
STAIRS_TAIL = '>2:05</span><span class="fn" style="color: #8F877C; white-space: nowrap; font-size: 9px;">THE STAIRS</span></div>'
GOLD_LINK = '<div style="flex: 1; padding-top: 12px; min-width: 0;"><span style="display: block; width: 100%; height: 2px; background: #B0853A;"></span></div>'
SAILED_MARK = ('<div style="width: 58px; flex: none; display: flex; flex-direction: column; align-items: center; gap: 3px;">'
               '<span style="height: 26px; display: flex; align-items: center;">'
               '<span style="width: 26px; height: 26px; border-radius: 13px; border: 1.3px solid #8A6628; display: inline-flex; align-items: center; justify-content: center; box-sizing: border-box; background: #FBF7EC;">'
               '<svg width="12" height="12" viewBox="0 0 15 15" fill="none"><path d="M4.4 9.8c-1.5 0-2.5-1-2.5-2.4 0-1.7 1.3-3.3 3.4-4.1l.6 1c-1.2.6-2 1.4-2.1 2.2 1.2.1 2 .9 2 2 0 .8-.6 1.3-1.4 1.3zm5.8 0c-1.5 0-2.5-1-2.5-2.4 0-1.7 1.3-3.3 3.4-4.1l.6 1c-1.2.6-2 1.4-2.1 2.2 1.2.1 2 .9 2 2 0 .8-.6 1.3-1.4 1.3z" fill="#8A6628"/></svg></span></span>'
               '<span style="font-family: \'JetBrains Mono\', ui-monospace, monospace; font-size: 10px; font-weight: 700; color: #1B1714;">2:40</span>'
               '<span class="fn" style="color: #8F877C; white-space: nowrap; font-size: 9px;">SAILED</span></div>')
def pass11_board(k, h):
    if k in ('02', '03'):
        d = h.find('HISTORY &middot; EARLIER GENERATIONS')
        sel, rest = (h[:d], h[d:]) if d > 0 else (h, '')
        sel = _lead(sel, SUN_OLD, SUN_NEW, SUN_SUBS) if k == '02' else _lead(sel, DZ_OLD, DZ_NEW, DZ_SUBS)
        h = sel + rest
    if k in ('08b', '09', '09b', '01'):
        h = _lead(h, SUN_OLD, SUN_NEW, SUN_SUBS)
        h = _lead(h, DZ_OLD, DZ_NEW, DZ_SUBS)
    if k == '08b':
        # the corrected sailing as its own event, between the stairs and the island
        h = h.replace(STAIRS_TAIL + GOLD_LINK, STAIRS_TAIL + GOLD_LINK + SAILED_MARK + GOLD_LINK, 1)
        h = h.replace('One ticket and three photographs make the day. The crossing is twenty-five minutes; the morning after it was not kept.',
                      'One ticket, your correction and three photographs make the day. The crossing is twenty-five minutes; the hours before the stairs were not kept.')
        h = h.replace('TICKET 11:20, UNUSED &middot; YOUR WORD 2:40 &middot; PHOTOGRAPHS 2:05, 4:12, 6:40',
                      'TICKET 11:20, UNUSED &middot; SAILED 2:40, FROM YOUR CORRECTION &middot; PHOTOGRAPHS 2:05, 4:12, 6:40')
        # the five-mark strip leaves the gap column narrow; its label is shortened there only
        j = h.find('the stairs at 2:05, the island by 4:12')
        if j > 0:
            k = h.find('NOTHING KEPT', j)
            if k > 0: h = h[:k] + 'NOT KEPT' + h[k + len('NOTHING KEPT'):]
            # five marks in 393px: the labels must wrap rather than collide when type is scaled up
            end = h.find('TICKET 11:20, UNUSED', j)
            if end > j:
                seg = h[j:end].replace('white-space: nowrap; font-size: 9px;', 'font-size: 9px; line-height: 11px; text-align: center;')
                h = h[:j] + seg + h[end:]
    if k in ("02", "03"):
        h = h.replace("SELECTED &middot; THE CURRENT HOME SCROLLS &middot; 2026-09-07", "SELECTED &middot; THE CURRENT HOME SCROLLS &middot; 2026-09-09 &middot; BENEFIT-LED READ ON A NONURGENT OPEN")
    if k == "07":
        h = h.replace("STATIC BOARD &middot; THE TRIPS PAGE&rsquo;S PRIORITIES ARE ITS OWN (trips_stack.py) AND ARE QUOTED, NOT ADOPTED",
                      "STATIC BOARD &middot; THE TRIPS PAGE&rsquo;S PRIORITIES ARE ITS OWN (trips_stack.py) AND ARE QUOTED, NOT ADOPTED &middot; THE VERDICTS BELOW SAY WHAT A KIND WOULD BE FOR IF ADMITTED: THE TEMPORAL STRIP, THE WORK RECEIPT AND THE MONEY ROW REMAIN PROPOSED, AND THE 09-09 LAYOUT SELECTION DOES NOT ADMIT THEM OR CERTIFY SUPPLY ECONOMICS")
    if k == '01':
        h = h.replace('AS DRAWN ON 02 &middot; SUNDAY &middot; AT THE FLOOR THE READ DROPS TO DIRECT STATE (02, PHONE 2)',
                      'AS DRAWN ON 02 &middot; SUNDAY, SELECTED &middot; BENEFIT-LED ON A NONURGENT OPEN (09-09 SELECTION): THE STRONGEST ADMITTED BENEFIT LEADS AND WEATHER SUPPORTS &middot; AT THE FLOOR THE READ DROPS TO DIRECT STATE (02, PHONE 2)')
    return h

for k, name in NAMES.items():
    src = f'{IN}/{k}.html'
    if not os.path.exists(src): continue
    h = open(src).read(); before = h
    parts = []; last = 0
    for s, e in phone_regions(h):
        parts.append(captions_outside(h[last:s])); parts.append(pass10_phone(pass9_phone(pass8_phone(pass7_phone(pass6_phone(pass5_phone(polish_phone(h[s:e])))))))); last = e
    parts.append(captions_outside(h[last:])); h = pass4(pass3(pass2(polish_all(''.join(parts)))))
    h = pass11_board(k, pass10_board(k, pass9_board(k, h)))
    if k == '13':
        h = h.replace('EXPLORATION &middot; 2026-09-08</div>', 'EXPLORATION &middot; 2026-09-08 &middot; WARM PAPER CHOSEN FOR REFERENCE IMAGES</div>')
        h = h.replace('Nothing here is adopted; it is a sheet to choose from.', 'Chosen 2026-09-08: warm paper for reference and world images, applied as a rule; the person&rsquo;s own photographs stay untreated and are handled (one per unit, full width, or a matched stacked pair). The rules are on 09.')
    if k == '01':
        h = h.replace('Photograph plates are slots', 'Photograph plates are slots; plate rules (09-08): reference images graded warm paper, 3:2, full width, nothing on them, caption beneath; the person&rsquo;s own photographs untreated, one per unit or a matched stacked pair; never side-by-side thumbnails')
    open(f'{OUT}/{name}.dc.html', 'w').write(h)
    print(f'{k}: {len(phone_regions(before))} phones, {sum(before.count(t) for t in ["&middot; FIXTURE", "&middot; NO CTA", "&middot; SLOT", "TWO LINES AT MOST"])} tokens before → {sum(h.count(t) for t in ["&middot; FIXTURE", "&middot; NO CTA", "&middot; SLOT", "TWO LINES AT MOST"])} after (captions keep theirs), slots {before.count("#2A241E")}→{h.count("#2A241E")}, balance {h.count("text-wrap: balance")}, spans {h.count("SUNSET 7:04")}, dbl-shadow {h.count(", 0 5px 14px rgba(27,23,20,0.07), 0 5px 14px")}')
