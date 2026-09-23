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
