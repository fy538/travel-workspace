"""kit3 · the Places kit on the founder's chosen terms (09-07 late): Home's chrome, rows and people; the canon's kinds and instruments where a section has data.
Rebuilt after the generator loss from the pushed HTML of 19 (chrome, captions, notes, tab bar, the Red Hook map) and the a26e3228 specimen sheets (instruments)."""
import os, re
S = lambda f: open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', f)).read()
_p19 = S('p19.html')
HEAD = _p19[:_p19.find('<div style="width: 1900px')]
_i0 = _p19.find('<div style="width: 1900px'); BOARD_OPEN = _p19[_i0:_p19.find('>', _i0)+1]
TAIL = S('tail.html'); FOOT = S('footblock.html'); TABBAR = S('tabbar.html')
def fix_map(html):
    """The map as sliced from 19: plate radius 12; the pool's label to the left of its disc so it does not clip at the edge."""
    html = html.replace('border-radius: 14px; overflow: hidden;', 'border-radius: 12px; overflow: hidden;', 1)
    return re.sub(r'<text x="(\d+(?:\.\d+)?)" y="([^"]+)"([^>]*)>THE POOL</text>', lambda m: f'<text x="{float(m.group(1))-28:.0f}" y="{m.group(2)}"{m.group(3)} text-anchor="end">THE POOL</text>', html)
REDHOOK_MAP = fix_map(S('redhook_map.html'))
INK='#1B1714'; INK2='#2C2622'; MUTE='#6E6862'; ANCHOR='#8F877C'; GHOST='#B5AFA5'; GOLD='#B0853A'; GOLDD='#8A6628'; UMBER='#4A3428'; OX='#7A2E2E'
CARD='#FBF7EC'; WASH='#E8E2D4'; WATER='#3D5066'; PAPER='#EFEAE0'; BOARD='#F4F0E7'
MONO="font-family: 'JetBrains Mono', ui-monospace, monospace;"; SERIF="font-family: 'EB Garamond', Georgia, serif;"; SANS="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;"
HAIR='rgba(27,23,20,0.10)'; HAIR7='rgba(27,23,20,0.07)'; HAIR6='rgba(27,23,20,0.06)'
HATCH='repeating-linear-gradient(135deg, rgba(176,133,58,0.12) 0 6px, rgba(176,133,58,0.04) 6px 12px)'
SP = dict(xs=4, s=8, m=12, l=16, xl=24, sect=36)   # the only vertical distances
LABEL_W, LABEL_GAP = 72, 14                         # one label column for registers, horizon rows and receipts
ROW_PAD = 10
CHEV='<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="flex: none;"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW=lambda c=GOLDD: f'<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="{c}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
MAPI='<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M3 6.5L8 4.5L12 6.5L17 4.5V13.5L12 15.5L8 13.5L3 15.5V6.5Z" stroke="#6E6862" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 4.5V13.5M12 6.5V15.5" stroke="#6E6862" stroke-width="1.5"/></svg>'
BACK='<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12 4L6 10L12 16" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LB=f'font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="{MUTE}"'; LG=f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{GOLDD}"'; LK=f'font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="{INK}"'

# ── chrome ──
def anchor(scope, time, back=False, sub=None):
    left = BACK if back else ''
    sc = f'<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px; display: inline-flex; align-items: center; gap: 5px;">{scope}' + ('' if back else f'<svg width="9" height="9" viewBox="0 0 9 9" fill="none"><path d="M2 3.5L4.5 6L7 3.5" stroke="{INK}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>') + '</span>'
    if sub: sc = f'<div style="display: flex; flex-direction: column; gap: 2px;">{sc}<span style="font-size: 12.5px; line-height: 17px; color: {MUTE};">{sub}</span></div>'
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{left}{sc}<span class="fn" style="margin-left: auto; color: {MUTE};">{time}</span><span style="margin-left: 10px; display: inline-flex;">{MAPI}</span></div></div>'
def orientation(read, sub, size=30, lh=34): return f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: {size}px; line-height: {lh}px; letter-spacing: -0.01em;">{read}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div></div>'
def chip(t): return f'<span style="display: inline-flex; align-items: center; gap: 6px; background: {INK}; color: {CARD}; border-radius: 999px; padding: 4px 10px; font-size: 13px; font-weight: 500; flex: none;">{t}<span style="font-size: 12px; opacity: 0.7;">&times;</span></span>'
def ask(hint='A place, a time, a kind of evening', q=None, ctx=None):
    body = (chip(q) + (chip(ctx) if ctx else '')) if q else f'<span style="font-size: 14px; color: {MUTE}; flex: 1;">{hint}</span>'
    return (f'<div style="margin: 16px 22px 0 22px; display: flex; align-items: center; gap: 10px; padding: 8px 0; min-height: 44px; box-sizing: border-box; border-top: 1px solid {HAIR}; border-bottom: 1px solid {HAIR};">'
            f'<svg width="15" height="15" viewBox="0 0 16 16" fill="none" style="flex: none;"><circle cx="7" cy="7" r="4.5" stroke="{MUTE}" stroke-width="1.5"/><path d="M10.5 10.5L14 14" stroke="{MUTE}" stroke-width="1.5" stroke-linecap="round"/></svg>{body}</div>')
def sect(t, top=36): return f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{t}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>'
def gut(h, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{h}</div>'
def kick(t): return f'<div style="display: flex; align-items: center; gap: 10px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {GOLDD};"><span>{t}</span><span style="flex:1;height:1px;background:{HAIR};"></span></div>'
def title(t, size=17, lh=22, w=500): return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; font-weight: {w}; color: {INK};">{t}</div>'
def serifline(t, size=18, lh=25): return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def sup(t, col=None): return f'<div style="font-size: 13px; line-height: 18px; color: {col or MUTE}; margin-top: 4px;">{t}</div>'
def body(t): return f'<div style="font-size: 14px; line-height: 19px; color: {INK2};">{t}</div>'
def fn(t, top=4): return f'<div class="fn" style="margin-top: {top}px; color: {MUTE};">{t}</div>'
def meta(t, top=3): return fn(t, top)
def unc(t): return f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{t}</div>'
def door(t, c=GOLDD, top=0): return f'<div style="display: flex; align-items: center; margin-top: {top}px; min-height: 44px;"><span style="font-size: 13px; font-weight: 500; color: {c};">{t}</span>{ARROW(c)}</div>'
def doors(*ts): return '<div style="display: flex; gap: 18px; align-items: center; flex-wrap: wrap;">' + ''.join(door(t, c) for t, c in ts) + '</div>'
def door_list(items): return '<div style="display: flex; flex-direction: column;">' + ''.join(door(t) for t in items) + '</div>'
def card(inner, pad='16px', bg=CARD): return f'<div style="background: {bg}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: {pad}; display: flex; flex-direction: column; overflow: hidden;">{inner}</div>'
# ── rows and people ──
def prow(name, facts, extra='', last=False, first=False, size=16):
    bt = '' if first else f' border-top: 1px solid {HAIR7};'; bb = f' border-bottom: 1px solid {HAIR7};' if last else ''
    return f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0;{bt}{bb}"><div style="flex: 1; min-width: 0;">{title(name, size, size+5)}{fn(facts, 3)}{extra}</div>{CHEV}</div>'
def nrow(n, name, facts, extra='', last=False, first=False):
    bt = '' if first else f' border-top: 1px solid {HAIR7};'; bb = f' border-bottom: 1px solid {HAIR7};' if last else ''
    num = f'<span style="width: 22px; height: 22px; border-radius: 11px; background: {INK}; color: {CARD}; display: inline-flex; align-items: center; justify-content: center; {MONO} font-size: 10px; font-weight: 700; flex: none; margin-top: 1px;">{n}</span>'
    return f'<div style="display: flex; align-items: flex-start; gap: 12px; padding: 10px 0;{bt}{bb}">{num}<div style="flex: 1; min-width: 0;">{title(name, 16, 21)}{fn(facts, 3)}{extra}</div>{CHEV.replace("flex: none;", "flex: none; margin-top: 4px;")}</div>'
def facepile(letters, size=28, tuck=-8):
    out = '<span style="display: inline-flex; align-items: center; flex: none;">'
    for i, l in enumerate(letters):
        col = UMBER if l == 'you' else INK; t = 'N' if l == 'you' else l
        out += f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {col}; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {PAPER}; margin-left: {tuck if i else 0}px;">{t}</span>'
    return out + '</span>'
def arow(text, avatars=None, last=False, muted=False):
    lead = facepile(avatars, 28, -8) if avatars else f'<span style="width: 7px; height: 7px; border-radius: 4px; background: {MUTE}; flex: none;"></span>'
    bb = f' border-bottom: 1px solid {HAIR6};' if last else ''
    return f'<div class="row" style="padding: {ROW_PAD}px 0;{bb}">{lead}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {MUTE if muted else INK};">{text}</span>{CHEV}</div>'
def dim(t): return f'<span style="color: {MUTE};">{t}</span>'
def author_row(letter, who, when): return f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none;">{letter}</span><span style="font-size: 13px; font-weight: 600; color: {INK};">{who}</span><span class="fn" style="color: {MUTE};">{when}</span></div>'
def quote(t, size=18, lh=25): return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; color: {INK}; margin-top: 8px;">&ldquo;{t}&rdquo;</div>'
def place_strip(name, line): return f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 12px; padding-top: 12px; border-top: 1px solid {HAIR7};"><span style="width: 7px; height: 7px; border-radius: 4px; background: {GOLD}; flex: none;"></span><div style="flex: 1; min-width: 0;"><div style="{SERIF} font-size: 16px; line-height: 20px; font-weight: 600; color: {INK};">{name}</div><div class="fn" style="color: {MUTE}; margin-top: 2px;">{line}</div></div></div>'
def people_row(letters, t, sub): return f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 14px; background: {CARD}; border: 1px solid {HAIR};">{facepile(letters)}<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; font-weight: 600; color: {INK};">{t}</div><div style="font-size: 13px; color: {MUTE};">{sub}</div></div>{CHEV}</div>'
def readback(k, t, color=GOLDD): return f'<div style="display: flex; gap: 12px; align-items: center; padding: 12px 14px; border-radius: 12px; background: {CARD}; border: 1px solid {HAIR};"><span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px; color: {color}; flex: none;">{k}</span><div style="flex: 1; font-size: 13px; line-height: 18px; color: {INK2};">{t}</div></div>'
def composer(placeholder, text=None, to=None):
    inner = f'<span style="font-size: 15px; color: {INK}; flex: 1;">{text}</span>' if text else f'<span style="font-size: 14px; color: {GHOST}; flex: 1;">{placeholder}</span>'
    return ((f'<div class="fn" style="color: {MUTE}; margin-bottom: 8px;">{to}</div>' if to else '') + f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1.5px solid {INK if text else HAIR}; border-radius: 22px; padding: 0 16px; background: {CARD};">{inner}<span style="font-size: 13px; font-weight: 600; color: {GOLDD if text else GHOST}; flex: none;">Send</span></div>')
def bubble(t): return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
def answer(html): return f'<div style="max-width: 336px; {SERIF} font-size: 17px; line-height: 24px; color: {INK};">{html}</div>'
def seq_strip(stops, top=10):
    out = f'<div style="display: flex; flex-direction: column; margin-top: {top}px;">'; n = len(stops)
    for i, (t, name, detail, leg) in enumerate(stops):
        last = i == n - 1
        out += (f'<div style="display: flex; gap: 12px; align-items: stretch;"><div style="width: 44px; flex: none; text-align: right;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {INK}; line-height: 21px;">{t}</span></div>'
                f'<div style="width: 12px; flex: none; display: flex; flex-direction: column; align-items: center;"><span style="width: 9px; height: 9px; border-radius: 5px; background: {GOLD}; flex: none; margin-top: 6px;"></span>' + ('' if last else f'<span style="width: 2px; flex: 1; background: {GOLD}; opacity: 0.55; margin: 3px 0;"></span>') + '</div>'
                f'<div style="flex: 1; min-width: 0; padding-bottom: {0 if last else 12}px;">{title(name, 16, 21)}{sup(detail)}' + (f'<div class="fn" style="color: {MUTE}; margin-top: 4px;">{leg}</div>' if leg else '') + '</div></div>')
    return out + '</div>'
# ── kinds ──
def shelf_item(name, line, chip_):
    plate = f'<div style="height: 84px; border-radius: 12px; position: relative; background: {HATCH};"><span style="position: absolute; left: 10px; top: 9px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD};">PHOTO · TO BE SOURCED</span></div>'
    return (f'<div>{plate}<div style="font-size: 15px; font-weight: 600; letter-spacing: -0.2px; line-height: 19px; margin-top: 7px; min-height: 38px;">{name}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; min-height: 34px;">{line}</div>'
            f'<span style="display: inline-block; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD}; border: 1px solid rgba(138,102,40,0.4); border-radius: 999px; padding: 2.5px 7px; margin-top: 6px;">{chip_}</span></div>')
def browse_shelf(items, kick_t=None): return f'<div style="display: flex; flex-direction: column; gap: 10px;">' + (kick(kick_t) if kick_t else '') + '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px 12px;">' + ''.join(shelf_item(*it) for it in items) + '</div></div>'
def cover(svg_or_none, kick_t, t, h=186):
    inner = svg_or_none or ''
    return (f'<div style="height: {h}px; border-radius: 12px; overflow: hidden; position: relative; background: {HATCH if not svg_or_none else WASH};">{inner}'
            f'<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(27,23,20,0) 42%, rgba(27,23,20,0.70) 100%);"></div>'
            + ('' if svg_or_none else f'<span style="position: absolute; left: 15px; top: 12px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: #F2E6CC;">PHOTOGRAPH · TO BE SOURCED</span>')
            + f'<div style="position: absolute; left: 15px; right: 15px; bottom: 13px;"><div style="{MONO} font-weight: 700; font-size: 10px; letter-spacing: 1.2px; color: #F2E6CC;">{kick_t}</div><div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; color: {CARD}; margin-top: 4px;">{t}</div></div></div>')
def map_box(svg_html): return svg_html
def burden_strip(a='TO PIER 11', bar='THE FERRY · 25 MIN · EVERY 40', b='9 MIN ON FOOT', n='40 MOVING'):
    return (f'<svg width="349" height="46" viewBox="0 0 349 46" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;">'
            f'<path d="M8 24 L44 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><rect x="52" y="18" width="196" height="12" rx="6" fill="{INK}" opacity="0.78"/>'
            f'<path d="M258 24 L306 24" stroke="rgba(27,23,20,0.30)" stroke-width="8" stroke-dasharray="0.1 14" stroke-linecap="round"/><text x="318" y="28" {LK}>{n}</text>'
            f'<text x="52" y="10" {LG}>{bar}</text><text x="8" y="44" {LB}>{a}</text><text x="306" y="44" text-anchor="end" {LB}>{b}</text></svg>')
def day_band(blocks, labels, track=(2, 345), h=56):
    """blocks: (x, w, label) gold; labels: (x, text, anchor). One evening on one track."""
    out = f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="display: block; width: 100%; height: auto; margin-top: 8px;"><rect x="{track[0]}" y="26" width="{track[1]}" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
    for x, w, lab, kind in blocks:
        if kind == 'gold': out += f'<rect x="{x}" y="22" width="{w}" height="16" rx="8" fill="{GOLD}"/><text x="{x}" y="14" {LG}>{lab}</text>'
        elif kind == 'ink': out += f'<rect x="{x}" y="22" width="{w}" height="16" rx="8" fill="{INK}" opacity="0.8"/><text x="{x}" y="14" {LK}>{lab}</text>'
        elif kind == 'ring': out += f'<circle cx="{x}" cy="30" r="6" stroke="{INK}" stroke-width="1.6" fill="{PAPER}"/>' + (f'<text x="{x+10}" y="14" {LK}>{lab}</text>' if lab else '')
        elif kind == 'dot': out += f'<circle cx="{x}" cy="30" r="4" fill="{INK}"/>' + (f'<text x="{x+8}" y="14" {LK}>{lab}</text>' if lab else '')
        elif kind == 'faint': out += f'<rect x="{x}" y="28" width="{w}" height="4" rx="2" fill="rgba(27,23,20,0.16)"/>'
    for x, t, a in labels: out += f'<text x="{x}" y="{h-2}" text-anchor="{a}" {LB}>{t}</text>'
    return out + '</svg>'
def ghost_rows(n=2):
    return ''.join(f'<div style="display: flex; gap: 12px; align-items: center; min-height: 52px; padding: 8px 0; border-top: 1px solid {HAIR7};"><div style="width: 40px; height: 40px; border-radius: 10px; background: {WASH}; flex: none;"></div><div style="flex: 1; display: flex; flex-direction: column; gap: 8px;"><div style="height: 13px; width: {a}%; border-radius: 6px; background: {WASH};"></div><div style="height: 11px; width: {b}%; border-radius: 6px; background: {WASH};"></div></div></div>' for a, b in ((62, 40), (48, 34))[:n])
# ── phones and boards ──
def phone(inner, active='Places'):
    tb = TABBAR if active == 'Places' else TABBAR.replace('color: #1B1714;">Places', 'color: #6E6862;">Places')
    return f'<div style="width: 393px; min-height: 0; position: relative; background: {PAPER}; {SANS} color: {INK}; display: flex; flex-direction: column; box-sizing: border-box;">{inner}<div style="flex-grow: 1;"></div>{tb}</div>'
def caption(k1, k2, t): return f'<div class="shead notes" style="color: {GOLDD}; margin-bottom: 10px;"><span>{k1}</span><span class="rule"></span></div><div class="notes" style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{k2}</div><div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div class="fn" style="line-height: 14px;"></div></div>'
def col(ph, cap, w=393, clip=None):
    inner = f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column;">{cap}{ph}</div>'
    if clip: return f'<div style="width: {w}px; flex: none; position: relative; height: {clip}px; overflow: hidden;">{inner}<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 110px; background: linear-gradient(to bottom, rgba(244,240,231,0), {BOARD} 85%); pointer-events: none;"></div></div>'
    return inner
def viewport(col_html, y=812):
    """The first-viewport marker: a dashed line across the column at the phone's first fold."""
    return col_html.replace('</div>', f'<div class="notes" style="position: absolute; left: -12px; right: -12px; top: {y+130}px; border-top: 1.5px dashed {OX}; pointer-events: none;"><span class="fn" style="position: absolute; right: 0; top: -14px; color: {OX};">FIRST VIEWPORT</span></div></div>', 1) if False else col_html.replace('display: flex; flex-direction: column;">', 'display: flex; flex-direction: column; position: relative;">' + f'<div class="notes" style="position: absolute; left: -12px; right: -12px; top: {y+132}px; border-top: 1.5px dashed {OX}; pointer-events: none; z-index: 2;"><span class="fn" style="position: absolute; right: 0; top: -14px; color: {OX};">FIRST VIEWPORT</span></div>', 1)
TH = 'style="text-align: left; font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: #6E6862; padding: 6px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.14); vertical-align: bottom;"'
TD = 'style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;"'
def tbl(head, rows): return f'<table style="border-collapse: collapse; width: 100%;"><thead><tr>' + ''.join(f'<th {TH}>{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td {TD}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
def N(t): return f'<div style="font-size: 14px; line-height: 21px; color: {INK2};">{t}</div>'
def notecol(t, blocks, w=760): return f'<div class="notes" style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 22px; padding-top: 24px;"><div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 25px; color: {INK};">{t}</div>' + ''.join(f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">{k}</div>{h}</div>' for k, h in blocks) + '</div>'
def headblock(kick_t, ttl, sub): return f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;"><div class="kick">VESPER &middot; PLACES &middot; CREATED 2026-09-07 &middot; {kick_t}</div><div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">{ttl}</div><div class="notes" style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">{sub}</div></div>'
def rows_page(w, kick_t, ttl, sub, rows, h=6000):
    out = ''
    for i, (dk, dt, cols) in enumerate(rows):
        div = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;">' if i else '<div style="display: flex; flex-direction: column; gap: 6px;">') + f'<div class="kick" style="color: {GOLDD};">{dk}</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">{dt}</div></div>'
        out += div + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols) + '</div>'
    op = BOARD_OPEN.replace('width: 1900px', f'width: {w}px').replace(re.search(r'min-height: \d+px', BOARD_OPEN).group(0), f'min-height: {h}px')
    return HEAD + op + headblock(kick_t, ttl, sub) + out + FOOT + TAIL
def set_height(html, h): return re.sub(r'(<div style="width: \d+px; min-height: )\d+(px; background: #F4F0E7)', lambda m: f'{m.group(1)}{h}{m.group(2)}', html, count=1)
