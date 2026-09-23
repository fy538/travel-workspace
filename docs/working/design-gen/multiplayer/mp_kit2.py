"""Pass A-prime helpers: the eight further directions E1-E8. Same board grammar as D1-D10, plus the private-context test."""
from mp_common import *

EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
PRIV = lambda who: tag(f'PRIVATE TO {who}', UMBER, 'rgba(74,52,40,0.10)')
SHARED = lambda who='THE GROUP': tag(f'SEEN BY {who}', GREEN, 'rgba(61,112,80,0.12)')

def bar(label, when=''):
    w = f'<span class="fn" style="margin-left: auto;">{when}</span>' if when else ''
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">{label}</span>{w}</div></div>'
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
def bubble_in(t, who=''):
    w = f'<div class="fn" style="color: {ANCHOR}; margin: 0 0 4px 4px;">{who}</div>' if who else ''
    return f'<div>{w}<div style="display: flex;"><div style="max-width: 300px; background: {CARD}; border: 1px solid {HAIR}; color: {INK}; border-radius: 18px 18px 18px 4px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div></div>'
def says(t, size=17, lh=24, color=INK):
    return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; color: {color};">{t}</div>'
def box(inner, pad='16px'):
    return f'<div style="border: 1px solid {HAIR}; background: {CARD}; border-radius: 14px; padding: {pad};">{inner}</div>'
def dashed(kick, t):
    k = f'<div class="kickm" style="margin-bottom: 5px;">{kick}</div>' if kick else ''
    return f'<div style="border: 1px dashed rgba(27,23,20,0.25); border-radius: 12px; padding: 12px 14px;">{k}<div style="font-size: 14px; line-height: 20px; color: {INK2};">{t}</div></div>'
def body(t, color=INK2):
    return f'<div style="font-size: 14px; line-height: 20px; color: {color};">{t}</div>'
def prov(t):
    """A per-statement provenance line: who said this, under what standing."""
    return f'<div class="fn" style="color: {ANCHOR}; margin-top: 6px; line-height: 15px;">{t}</div>'
def btn(t, primary=True):
    if primary:
        return f'<span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">{t}</span>'
    return f'<span class="vdl-btn secondary pill vk-t-labelSemibold">{t}</span>'
def actions(*items):
    return '<div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">' + ''.join(items) + '</div>'
def person(letter, name, line=''):
    l = f'<div class="vdl-t-supportLine" style="color: {MUTE};">{line}</div>' if line else ''
    return (f'<div style="display: grid; grid-template-columns: 32px 1fr; column-gap: 12px; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">'
            f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">{letter}</span>'
            f'<div><div style="font-size: 15px; line-height: 20px; color: {INK};">{name}</div>{l}</div></div>')

def line(text, mark='dot', color=MUTE, muted=False, last=False):
    """A descriptive line: same rhythm as a row, but it goes nowhere, so it has no chevron."""
    if mark == 'dashed': lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px dashed {color}; box-sizing: border-box; flex: none;"></span>'
    elif mark == 'hollow': lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px solid {color}; box-sizing: border-box; flex: none;"></span>'
    elif mark == 'none': lead = ''
    else: lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; background: {color}; flex: none;"></span>'
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.06);' if last else ''
    return f'<div class="row" style="padding: 8px 0;{bb}">{lead}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {MUTE if muted else INK};">{text}</span></div>'

from gen_generous import facepile
def original(h, **kw):
    """A person's own words, in the shared reader: name and time once, side by side, then the words."""
    return dci('OriginalReader', h, density='open', **kw)
def chip(t):
    return f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {INK2}; border: 1px solid {HAIR}; background: {CARD}; border-radius: 999px; padding: 4px 10px; white-space: nowrap;">{t}</span>'
def faces(letters, text, size=26):
    return f'<div style="display: flex; align-items: center; gap: 10px;">{facepile(list(letters), size)}<span style="font-size: 14px; color: {INK2};">{text}</span></div>'
def plain(t, color=None, size=15, lh=21):
    return f'<div style="font-size: {size}px; line-height: {lh}px; color: {color or INK};">{t}</div>'
def quiet(t):
    return f'<div style="font-size: 14px; line-height: 20px; color: {MUTE};">{t}</div>'
def rule(inner, top=18):
    return f'<div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: {top}px;">{inner}</div>'
def webframe(inner):
    return f'<div style="width: 393px; background: {PAPER}; {SANS} color: {INK};">{inner}<div style="height: 22px;"></div></div>'
def avatar_for(html, letter):
    """anchor_row() draws Nora's account avatar; on anyone else's phone, swap the letter."""
    return html.replace('flex: none;">N</span>', f'flex: none;">{letter}</span>')

def review(costs, compare, kind, line, question, extras=(), widths=(600, 520, 440), offscreen=()):
    """The three review columns. `compare` must include the private-context test row."""
    if offscreen:
        costs = list(costs) + [('DECIDED, NOT DISPLAYED', 'These are design decisions. They hold, and the screen does not recite them: ' + ' &middot; '.join(offscreen))]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led(costs), w=widths[0])
    n2 = notes('COMPARED WITH AN ORDINARY APP', led(compare), w=widths[1])
    n3 = notes('VERDICT', verdict(kind, line, question) + ''.join(N(e) for e in extras), w=widths[2])
    return (n1, n2, n3)

def eboard(key, fname, kick, title_, sub, cols, note_cols, nphones):
    return write(fname, board(bw(nphones, (600, 520, 440)), hh(key, 1800),
                              f'{key} &middot; {kick} &middot; PASS A&prime; &middot; EXPLORATORY', title_, sub, cols, note_cols))

# ───────────────────────── Life skin, 2026-09-22 ─────────────────────────
# Every board in the project wears Life's board grammar: the taupe board, rounded phone frames, Life's header, a gold
# mono caption above each frame and a short note below it, and riso placeholders instead of the old figure
# illustrations. Patched here, once, so every generator that imports this kit gets it.
import re as _re, os as _os, hashlib as _hl
import gen_generous as _gg, gen_merge as _gm, gen_p2_common as _pc
_LIFE07 = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'life', '07.html')
try:
    _LIFE_STYLE = _re.search(r'<style>(.*?)</style>', open(_LIFE07).read(), _re.S).group(1)
except Exception:
    _LIFE_STYLE = ''
HEAD_VDL = HEAD_VDL.replace('</helmet>', f'<style>{_LIFE_STYLE}</style>\n</helmet>', 1)
BOARD_BG = '#D8D1C5'

def head(kick, title, sub, pill='Review'):
    return (f'<div style="padding: 0 0 10px 0; margin-bottom: 18px; max-width: 1100px;">'
            f'<div style="display: flex; align-items: center; gap: 12px;"><span class="ceye">{kick}</span><span class="cpill rev">{pill}</span></div>'
            f'<div class="ctitle" style="padding-top: 8px;">{title}</div>'
            f'<div class="cn" style="padding-top: 10px; max-width: 1000px; font-size: 13px; line-height: 19px;">{sub}</div></div>')

_NOTE = '<!--NOTE-->'
def daycap(day, k, t, s2=''):
    top = f'{k} &middot; {day}' if day else f'{k}'
    above = (f'<div class="ccap" style="margin-bottom: 5px;">{top}</div>'
             f'<div style="{SERIF} font-weight: 600; font-size: 18px; line-height: 23px; color: {INK}; margin-bottom: 12px;">{t}</div>')
    note = f'<div class="cnote" style="margin-top: 10px; font-size: 12px; line-height: 17px;">{s2}</div>' if s2 else ''
    return above + _NOTE + note
def col(ph, cap, w=393):
    ph = _re.sub(r'(<div style="width: 393px;[^"]*?)min-height: \d+px;', r'\1min-height: 0;', ph, count=1)
    above, note = (cap.split(_NOTE, 1) + [''])[:2] if _NOTE in cap else (cap, '')
    return f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column;">{above}{ph}{note}</div>'

def tag(t, c=GOLDD, bg='rgba(176,133,58,0.14)'):
    return (f'<span style="display: inline-flex; align-items: center; height: 18px; padding: 0 8px; border-radius: 9px; {MONO} font-size: 8px; '
            f'font-weight: 700; letter-spacing: 1px; color: {c}; background: {bg}; white-space: nowrap;">{t}</span>')

_orig_phone2 = _pc.phone2
def phone2(inner, active='Places'):
    return f'<div class="cphone" style="width: 393px; flex: none;">{_orig_phone2(inner, active)}</div>'
def webframe(inner):
    return (f'<div class="cphone" style="width: 393px; flex: none; border-radius: 16px;"><div style="background: {PAPER}; {SANS} color: {INK};">'
            f'<div style="padding: 10px 16px; border-bottom: 1px solid rgba(27,23,20,0.08); {MONO} font-size: 9px; letter-spacing: 1px; color: {MUTE};">A PAGE &middot; NO APP NEEDED</div>'
            f'{inner}<div style="height: 22px;"></div></div></div>')

# riso placeholders, as Life keeps photographs: paper ground, two inks, one motif per kind
_RISO = ['<circle cx="44" cy="16" r="9" fill="#C4604F" opacity="0.65"/><rect y="34" width="62" height="28" fill="#4E7A6F" opacity="0.5"/>',
         '<circle cx="31" cy="31" r="16" stroke="#C4604F" stroke-width="2.5" fill="none" opacity="0.7"/><path d="M22 34 Q31 24 42 32" stroke="#4E7A6F" stroke-width="2.5" fill="none" opacity="0.65"/>',
         '<path d="M10 52 L30 16 L50 52 Z" fill="#4E7A6F" opacity="0.45"/><circle cx="48" cy="14" r="6" fill="#C4604F" opacity="0.7"/>',
         '<rect x="12" y="12" width="20" height="38" rx="2" fill="#C4604F" opacity="0.55"/><rect x="36" y="22" width="16" height="28" rx="2" fill="#4E7A6F" opacity="0.5"/>',
         '<path d="M6 40 Q20 24 31 36 T56 34" stroke="#4E7A6F" stroke-width="3" fill="none" opacity="0.6"/><circle cx="18" cy="18" r="7" fill="#C4604F" opacity="0.6"/>',
         '<rect x="10" y="30" width="42" height="18" rx="2" fill="#4E7A6F" opacity="0.45"/><circle cx="20" cy="18" r="6" fill="#C4604F" opacity="0.65"/><circle cx="40" cy="18" r="6" fill="#C4604F" opacity="0.65"/>']
_KIND = {'room': 0, 'loaf': 1, 'pier': 4, 'hall': 3, 'market': 5, 'quay': 4, 'film': 3, 'noodles': 1, 'library': 3, 'organ': 3, 'table': 5, 'loop': 4, 'terrace': 2}
def illo(kind, h=150, w=349):
    i = _KIND.get(kind, int(_hl.md5(str(kind).encode()).hexdigest(), 16) % len(_RISO))
    return (f'<svg width="100%" height="{h}" viewBox="0 0 62 62" preserveAspectRatio="xMidYMid slice" style="display: block; width: {w}px; max-width: 100%;">'
            f'<rect width="62" height="62" fill="#F6F1E4"/>{_RISO[i]}</svg>')
def thumb(kind, size=56):
    return f'<div style="width: {size}px; height: {size}px; border-radius: 6px; overflow: hidden; flex: none; border: 1px solid rgba(27,23,20,0.10); box-sizing: border-box;">{illo(kind, size, size)}</div>'

for _m in (_gg, _gm, _pc):
    for _n, _f in (('head', head), ('col', col), ('daycap', daycap), ('phone2', phone2), ('illo', illo), ('thumb', thumb)):
        if hasattr(_m, _n): setattr(_m, _n, _f)

# Tags above a frame only when they say something the caption does not: no app, or a proposed piece.
_TAGROW = _re.compile(r'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">(.*?)</div>', _re.S)
_KEEP = ('NO APP', 'PROPOSED')
def _prune_tags(cap):
    def keep(m):
        spans = _re.findall(r'<span[^>]*>.*?</span>', m.group(1), _re.S)
        kept = [s for s in spans if any(k in _re.sub(r'<[^>]+>', '', s) for k in _KEEP)]
        return f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 8px;">{"".join(kept)}</div>' if kept else ''
    return _TAGROW.sub(keep, cap, count=1)
_col_skin = col
def col(ph, cap, w=393):
    return _col_skin(ph, _prune_tags(cap), w)
for _m in (_gg, _gm, _pc):
    if hasattr(_m, 'col'): setattr(_m, 'col', col)
