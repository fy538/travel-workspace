"""Places revision 2 (handoff §8, 2026-09-07): the shared material for the revised boards.
- an expanded synthetic world packet with several strong lead candidates (food, music, outdoor, low-cost social, indoor, spatial discovery)
- illustrative imagery drawn as SVG (explicitly illustrations; never a real person's photograph)
- consumer-copy helpers with no internal explanations inside the phone; annotations live outside
- the control model: city + search + map in the header; one editable question line; a context chip
- a finisher that raises supporting text to 14/19 and mono meta to 11px inside Places phones (a proposed token change, flagged on 09)
Fixture copy only. Nothing here is ruled."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, facepile, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, card, fact, author_row
from gen_places import scope_header, map_wash, places_phone
from gen_merge import tbl, blk, daycap, page, notecol as _nc
from gen_placeskit import STAMP, OUT
from gen_artifact import large as _large

HAIR = 'rgba(27,23,20,0.10)'
def notecol(t, blocks, w=520): return _nc(t, blocks, w=w)
def hh(k, d=1400):
    H = json.load(open(os.path.join(OUT, 'heights.json'))) if os.path.exists(os.path.join(OUT, 'heights.json')) else {}
    return H[k] if k in H else d

# ───────────────────────────── the finisher: consumer type, no doctrine ─────────────────────────────
def consumer(html):
    """Raise supporting text and meta inside a phone. 13/18 and 12.5/17 → 14/19; the 10px mono footnote → 11px. Proposed token change, flagged on 09."""
    html = html.replace('font-size: 13px; line-height: 18px', 'font-size: 14px; line-height: 19px').replace('font-size: 12.5px; line-height: 17px', 'font-size: 14px; line-height: 19px')
    html = html.replace('class="fn"', 'class="fn fn11"')
    return html
FN11 = '<style>.fn11 { font-size: 11px !important; letter-spacing: 0.8px; }</style>'
def phone2(inner, active='Places'):
    return consumer(phone(inner, 0, active=active))
def large(html, k=1.3): return _large(html, k)

# ───────────────────────────── illustrations (SVG, two or three inks, explicit) ─────────────────────────────
GRAIN = '<defs><pattern id="g" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.7" fill="rgba(27,23,20,0.10)"/><circle cx="4" cy="4" r="0.6" fill="rgba(27,23,20,0.07)"/></pattern></defs>'
def _svg(h, inner, bg=WASH, w=349):
    return (f'<svg width="100%" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" style="display: block;">{GRAIN}<rect width="{w}" height="{h}" fill="{bg}"/>{inner}<rect width="{w}" height="{h}" fill="url(#g)"/></svg>')

def illo(kind, h=150, w=349):
    G, GD, I, P, PL, OXC = GOLD, GOLDD, INK, PAPER, PLAN, OX
    k = kind
    if k == 'room':   # a wall opened to a threshold; light across the floor
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#E4DCC9"/><rect x="0" y="{h*0.62:.0f}" width="{w}" height="{h*0.38:.0f}" fill="#D3C8AE"/>'
             f'<rect x="{w*0.36:.0f}" y="{h*0.12:.0f}" width="{w*0.3:.0f}" height="{h*0.5:.0f}" fill="#F4EEDD"/><rect x="{w*0.36:.0f}" y="{h*0.12:.0f}" width="6" height="{h*0.5:.0f}" fill="{I}" opacity="0.8"/><rect x="{w*0.66:.0f}" y="{h*0.12:.0f}" width="6" height="{h*0.5:.0f}" fill="{I}" opacity="0.8"/>'
             f'<path d="M{w*0.36:.0f} {h*0.62:.0f} L{w*0.2:.0f} {h} L{w*0.82:.0f} {h} L{w*0.66:.0f} {h*0.62:.0f} Z" fill="#F4EEDD" opacity="0.7"/><rect x="{w*0.08:.0f}" y="{h*0.4:.0f}" width="{w*0.14:.0f}" height="{h*0.22:.0f}" fill="{G}" opacity="0.55"/>')
    elif k == 'loaf':
        s = (f'<rect x="0" y="{h*0.7:.0f}" width="{w}" height="{h*0.3:.0f}" fill="#D9CDB0"/><ellipse cx="{w*0.5:.0f}" cy="{h*0.66:.0f}" rx="{w*0.26:.0f}" ry="{h*0.2:.0f}" fill="{GD}"/><ellipse cx="{w*0.5:.0f}" cy="{h*0.6:.0f}" rx="{w*0.24:.0f}" ry="{h*0.18:.0f}" fill="{G}"/>'
             f'<path d="M{w*0.34:.0f} {h*0.55:.0f} Q{w*0.42:.0f} {h*0.42:.0f} {w*0.5:.0f} {h*0.55:.0f} Q{w*0.58:.0f} {h*0.42:.0f} {w*0.66:.0f} {h*0.55:.0f}" stroke="#F4EEDD" stroke-width="3" fill="none" stroke-linecap="round"/>'
             + ''.join(f'<circle cx="{w*0.36+i*13:.0f}" cy="{h*0.62+(i%3)*4:.0f}" r="1.6" fill="#F4EEDD"/>' for i in range(8)))
    elif k == 'pier':
        s = (f'<rect x="0" y="0" width="{w}" height="{h*0.55:.0f}" fill="#E9D9B8"/><circle cx="{w*0.62:.0f}" cy="{h*0.5:.0f}" r="{h*0.22:.0f}" fill="{G}"/><rect x="0" y="{h*0.55:.0f}" width="{w}" height="{h*0.45:.0f}" fill="{PL}" opacity="0.55"/>'
             f'<rect x="0" y="{h*0.55:.0f}" width="{w}" height="4" fill="#F4EEDD" opacity="0.6"/><rect x="{w*0.05:.0f}" y="{h*0.6:.0f}" width="{w*0.6:.0f}" height="8" fill="{I}"/>' + ''.join(f'<rect x="{w*0.1+i*40:.0f}" y="{h*0.68:.0f}" width="4" height="{h*0.25:.0f}" fill="{I}"/>' for i in range(5))
             + f'<circle cx="{w*0.4:.0f}" cy="{h*0.5:.0f}" r="5" fill="{I}"/><rect x="{w*0.4-3:.0f}" y="{h*0.53:.0f}" width="6" height="14" fill="{I}"/>')
    elif k == 'hall':
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#3A322B"/><rect x="{w*0.3:.0f}" y="{h*0.18:.0f}" width="{w*0.4:.0f}" height="{h*0.5:.0f}" fill="#4A3F36"/>'
             f'<rect x="{w*0.44:.0f}" y="{h*0.3:.0f}" width="{w*0.12:.0f}" height="{h*0.38:.0f}" fill="{I}"/><circle cx="{w*0.5:.0f}" cy="{h*0.42:.0f}" r="9" fill="{G}"/>'
             + ''.join(f'<rect x="{w*0.08+(i%6)*(w*0.15):.1f}" y="{h*0.72+(i//6)*h*0.09:.1f}" width="{w*0.1:.1f}" height="{max(3,h*0.04):.1f}" rx="2" fill="#6E6862"/>' for i in range(12)))
    elif k == 'market':
        s = (f'<rect x="0" y="{h*0.65:.0f}" width="{w}" height="{h*0.35:.0f}" fill="#D9CDB0"/>' + ''.join(f'<path d="M{20+i*110} {h*0.35:.0f} L{100+i*110} {h*0.35:.0f} L{110+i*110} {h*0.55:.0f} L{10+i*110} {h*0.55:.0f} Z" fill="{GD if i%2 else G}"/><rect x="{16+i*110}" y="{h*0.55:.0f}" width="4" height="{h*0.3:.0f}" fill="{I}"/><rect x="{102+i*110}" y="{h*0.55:.0f}" width="4" height="{h*0.3:.0f}" fill="{I}"/><rect x="{24+i*110}" y="{h*0.68:.0f}" width="72" height="14" fill="{P}"/>' for i in range(3))
             + f'<circle cx="{w*0.5:.0f}" cy="{h*0.78:.0f}" r="5" fill="{I}"/><circle cx="{w*0.56:.0f}" cy="{h*0.8:.0f}" r="5" fill="{I}"/>')
    elif k == 'quay':
        s = (f'<rect x="0" y="0" width="{w}" height="{h*0.4:.0f}" fill="#E9D9B8"/><rect x="0" y="{h*0.4:.0f}" width="{w}" height="{h*0.6:.0f}" fill="{PL}" opacity="0.5"/><rect x="0" y="{h*0.38:.0f}" width="{w*0.5:.0f}" height="{h*0.12:.0f}" fill="#D9CDB0"/>'
             f'<path d="M0 {h*0.38:.0f} L{w*0.5:.0f} {h*0.38:.0f} L{w*0.5:.0f} 0" stroke="#C9BC9C" stroke-width="10" fill="none"/>' + ''.join(f'<path d="M{w*0.55+i*60:.0f} {h*0.7:.0f} q20 -12 40 0 l-4 8 h-32 z" fill="{I}"/>' for i in range(3)))
    elif k == 'film':
        s = (f'<rect x="0" y="0" width="{w}" height="{h*0.6:.0f}" fill="#2E2823"/><rect x="{w*0.25:.0f}" y="{h*0.1:.0f}" width="{w*0.5:.0f}" height="{h*0.38:.0f}" fill="#F4EEDD"/><rect x="0" y="{h*0.6:.0f}" width="{w}" height="{h*0.4:.0f}" fill="#4B5A3C" opacity="0.8"/>'
             + ''.join(f'<ellipse cx="{30+i*40+(i%2)*10:.0f}" cy="{h*0.72+(i%3)*8:.0f}" rx="6" ry="4" fill="{I}"/>' for i in range(8)))
    elif k == 'noodles':
        s = (f'<rect x="0" y="{h*0.65:.0f}" width="{w}" height="{h*0.35:.0f}" fill="#8A6628" opacity="0.5"/><ellipse cx="{w*0.5:.0f}" cy="{h*0.6:.0f}" rx="{w*0.22:.0f}" ry="{h*0.1:.0f}" fill="{I}"/><path d="M{w*0.28:.0f} {h*0.6:.0f} Q{w*0.5:.0f} {h*1.0:.0f} {w*0.72:.0f} {h*0.6:.0f} Z" fill="{I}"/>'
             f'<ellipse cx="{w*0.5:.0f}" cy="{h*0.6:.0f}" rx="{w*0.2:.0f}" ry="{h*0.08:.0f}" fill="{G}"/><path d="M{w*0.36:.0f} {h*0.58:.0f} q10 -8 20 0 t20 0 t20 0" stroke="#F4EEDD" stroke-width="2.5" fill="none"/><rect x="{w*0.62:.0f}" y="{h*0.22:.0f}" width="3" height="{h*0.4:.0f}" fill="{I}" transform="rotate(20 {w*0.62:.0f} {h*0.22:.0f})"/>')
    elif k == 'library':
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#DCD2BC"/><rect x="0" y="{h*0.55:.0f}" width="{w}" height="{h*0.08:.0f}" fill="{I}" opacity="0.85"/>' + ''.join(f'<rect x="{w*0.08+i*w*0.23:.1f}" y="{h*0.36:.0f}" width="{w*0.075:.1f}" height="{max(3,h*0.05):.1f}" fill="{G}"/><rect x="{w*0.115+i*w*0.23:.1f}" y="{h*0.44:.0f}" width="2" height="{h*0.11:.0f}" fill="{I}"/>' for i in range(4))
             + ''.join(f'<rect x="{w*0.06+i*w*0.063:.1f}" y="{h*0.08:.0f}" width="{w*0.04:.1f}" height="{h*0.2:.0f}" fill="{GD if i%3 else I}" opacity="0.7"/>' for i in range(15)))
    elif k == 'organ':
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#E4DCC9"/>' + ''.join(f'<rect x="{w*0.08+i*(w*0.84/12):.1f}" y="{h*0.1+abs(6-i)*h*0.04:.1f}" width="{w*0.84/12*0.6:.1f}" height="{h*0.75-abs(6-i)*h*0.04:.1f}" rx="2" fill="{I if i%2 else "#4A3F36"}"/>' for i in range(12)))
    elif k == 'table':
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#DCD2BC"/><path d="M{w*0.1:.0f} {h*0.5:.0f} L{w*0.9:.0f} {h*0.5:.0f} L{w*0.8:.0f} {h*0.7:.0f} L{w*0.2:.0f} {h*0.7:.0f} Z" fill="{GD}"/>' + ''.join(f'<circle cx="{w*0.18+i*44:.0f}" cy="{h*0.4:.0f}" r="7" fill="{I}"/>' for i in range(7)) + ''.join(f'<circle cx="{w*0.2+i*60:.0f}" cy="{h*0.58:.0f}" r="6" fill="{P}"/>' for i in range(5)))
    elif k == 'loop':
        s = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="{PL}" opacity="0.35"/><path d="M0 {h*0.5:.0f} Q{w*0.25:.0f} {h*0.2:.0f} {w*0.5:.0f} {h*0.5:.0f} T{w} {h*0.5:.0f}" stroke="#F4EEDD" stroke-width="18" fill="none"/><path d="M0 {h*0.5:.0f} Q{w*0.25:.0f} {h*0.2:.0f} {w*0.5:.0f} {h*0.5:.0f} T{w} {h*0.5:.0f}" stroke="{G}" stroke-width="3" stroke-dasharray="8 8" fill="none"/><circle cx="{w*0.5:.0f}" cy="{h*0.5:.0f}" r="6" fill="{I}"/>')
    elif k == 'terrace':
        s = (f'<rect x="0" y="0" width="{w}" height="{h*0.45:.0f}" fill="#E9D9B8"/><rect x="0" y="{h*0.45:.0f}" width="{w}" height="{h*0.55:.0f}" fill="#7A8A5C" opacity="0.6"/>' + ''.join(f'<rect x="0" y="{h*0.45+i*18:.0f}" width="{w}" height="3" fill="#D9CDB0"/>' for i in range(4)) + ''.join(f'<circle cx="{30+i*45}" cy="{h*0.6+(i%2)*14:.0f}" r="5" fill="{G}"/>' for i in range(7)))
    else:
        s = ''
    return _svg(h, s, w=w)

def plate(kind, h=150, tag='ILLUSTRATION &middot; NOT A PHOTOGRAPH'):
    """A media plate inside a card. The corner tag names what the drawing is standing in for; no drawing is a person's own photograph."""
    return (f'<div style="height: {h}px; margin: -16px -16px 12px -16px; position: relative; overflow: hidden;">{illo(kind, h)}'
            f'<span style="position: absolute; left: 10px; bottom: 8px; {MONO} font-size: 9px; letter-spacing: 1px; color: rgba(244,238,221,0.9); background: rgba(27,23,20,0.55); padding: 2px 6px; border-radius: 4px;">{tag}</span></div>')
def thumb(kind, size=56):
    return f'<div style="width: {size}px; height: {size}px; border-radius: 12px; overflow: hidden; flex: none;">{illo(kind, size, size)}</div>'

# ───────────────────────────── the control model ─────────────────────────────
def header(city, sub='', back=False, live=None):
    """City + one line, search and map in the header only. Nothing about measurement or origin unless the person asked for directions."""
    return scope_header(city, sub, back=back, live=live)
CLOSE = f'<svg width="12" height="12" viewBox="0 0 12 12" fill="none" style="margin-left: 2px;"><path d="M3 3L9 9M9 3L3 9" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
def question_line(q=None, ctx=None, hint='A place, a time, a kind of evening'):
    """One editable line under the header: the question (with ×), an optional context chip (with ×). Empty = an inviting hint, no demand."""
    pill = lambda t, on: (f'<span style="height: 30px; border-radius: 15px; background: {INK if on else CARD}; color: {CARD if on else INK}; border: 1px solid {"transparent" if on else HAIR}; display: inline-flex; align-items: center; gap: 4px; padding: 0 12px; font-size: 14px; font-weight: 500; white-space: nowrap;">{t}{CLOSE if on else ""}</span>')
    inner = ''
    if q: inner += pill(q, True)
    if ctx: inner += pill(ctx, True).replace(f'background: {INK}', f'background: {UMBER}')
    if not q and not ctx:
        inner += f'<span style="height: 30px; border-radius: 15px; border: 1px dashed rgba(27,23,20,0.25); display: inline-flex; align-items: center; padding: 0 12px; font-size: 14px; color: {MUTE};">{hint}</span>'
    return f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding: 12px 22px 0 22px; align-items: center;">{inner}</div>'

def question_sheet(when='Saturday evening', where='All of New York', who='Just me'):
    """The one sheet behind the question line: three rows, not a wizard. Any row may stay as it is."""
    r = lambda k, v, opts: (f'<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.08);"><div style="display: flex; align-items: baseline; gap: 10px;"><span class="kickm" style="width: 52px; flex: none;">{k}</span><span style="font-size: 16px; font-weight: 500; color: {INK};">{v}</span></div>'
                            f'<div style="display: flex; gap: 6px; flex-wrap: wrap; padding-left: 62px;">' + ''.join(f'<span style="height: 28px; border-radius: 14px; border: 1px solid {HAIR}; background: {CARD}; display: inline-flex; align-items: center; padding: 0 11px; font-size: 13px; color: {INK};">{o}</span>' for o in opts) + '</div></div>')
    return (f'<div style="background: {CARD}; border-radius: 18px 18px 0 0; box-shadow: 0 -8px 24px rgba(27,23,20,0.14); padding: 14px 22px 26px 22px;"><div style="width: 36px; height: 4px; border-radius: 2px; background: rgba(27,23,20,0.15); margin: 0 auto 14px auto;"></div>'
            + title('What are you looking for?', 20, 25, 600) + f'<div style="margin-top: 10px;">' + r('WHEN', when, ['Now', 'Tonight', 'Saturday afternoon', 'Sunday', 'Any time']) + r('WHERE', where, ['Near a place&hellip;', 'Red Hook', 'Sunset Park', 'Another city&hellip;']) + r('WHO', who, ['From friends', 'With Maya', 'Around Saturday&rsquo;s dinner']) + '</div>'
            + f'<div style="display: flex; gap: 18px; margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(27,23,20,0.10);">{door("Show me")}{door("Clear", MUTE)}</div></div>')

def friends_entry(count='18 things this week', letters=('M', 'A', 'P', 'S')):
    """A recognizable way into From friends from the ordinary opening: a row with faces, not a filter."""
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 14px; border-radius: 14px; background: {CARD}; border: 1px solid {HAIR};">{facepile(list(letters), 26, -7)}'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; font-weight: 600; color: {INK};">From friends</div><div style="font-size: 13px; color: {MUTE};">{count}</div></div>{CHEV}</div>')

# ───────────────────────────── consumer units (no doctrine inside) ─────────────────────────────
def when_line(t):
    """Date, time, price in readable sans, not tiny mono."""
    return f'<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 3px;">{t}</div>'
def src(t):
    """Source or freshness in ordinary language, small but readable."""
    return f'<div class="fn" style="margin-top: 5px; color: {ANCHOR};">{t}</div>'
def unc(t):
    """A material uncertainty, in words the person needs for the decision."""
    return f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{t}</div>'

def event_unit(day, num, name, when, price, note='', unknown='', door_text=None, kind=None, last=False):
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.07);' if last else ''
    th = thumb(kind, 56) if kind else (f'<div style="width: 48px; flex: none; text-align: center; border: 1.4px solid {INK}; border-radius: 8px; padding: 4px 0;"><div style="{MONO} font-size: 9px; font-weight: 700; letter-spacing: 0.8px; color: {MUTE};">{day}</div><div style="{SERIF} font-size: 20px; line-height: 22px; font-weight: 600; color: {INK};">{num}</div></div>')
    d = door(door_text) if door_text else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.07);{bb}">{th}'
            f'<div style="flex: 1; min-width: 0;">{title(name, 17, 22, 600)}{when_line(when + (" &middot; " + price if price else ""))}{(sup(note, INK2) if note else "")}{(unc(unknown) if unknown else "")}{d}</div></div>')

def place_unit(kind, name, line, note='', unknown='', door_text=None, last=False):
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.07);' if last else ''
    d = door(door_text) if door_text else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.07);{bb}">{thumb(kind, 56)}'
            f'<div style="flex: 1; min-width: 0;">{title(name, 17, 22, 600)}{when_line(line)}{(sup(note, INK2) if note else "")}{(unc(unknown) if unknown else "")}{d}</div></div>')

def lead_card(kind, kick, name, text, when='', unknown='', door_text=None, h=170, extra=''):
    inner = plate(kind, h) + f'<div class="kick" style="color: {GOLDD};">{kick}</div>' + f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; margin-top: 6px;">{name}</div>' + sup(text, INK2)
    if when: inner += when_line(when)
    if unknown: inner += unc(unknown)
    inner += extra
    if door_text: inner += door(door_text)
    return card(inner)

def share_v2(letter, who, when, words, kind=None, place='', line='', reply=True, h=170, extra=''):
    """A friend's share: their picture (illustrative) and their words first; the place under it; Reply to the person right there, small."""
    inner = (plate(kind, h) if kind else '') + author_row(letter, who, when) + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">{words}</div>'
    if place: inner += f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);"><div style="flex: 1; min-width: 0;"><div style="{SERIF} font-size: 16px; line-height: 20px; font-weight: 600; color: {INK};">{place}</div>{when_line(line) if line else ""}</div></div>'
    inner += extra
    doors = door(f'Reply to {who.split()[0]}') if reply else ''
    if place: doors += door('Open')
    if doors: inner += f'<div style="display: flex; gap: 18px; align-items: center;">{doors}</div>'
    return card(inner)

def share_line(letter, who, words, place, kind=None, last=False):
    """A compact contribution: avatar, words, the place; a thumbnail when there is a picture."""
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.06);' if last else ''
    th = thumb(kind, 44) if kind else ''
    return (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 10px 0; border-top: 1px solid rgba(27,23,20,0.06);{bb}">'
            f'<span style="width: 28px; height: 28px; border-radius: 14px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none; margin-top: 2px;">{letter}</span>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px; color: {INK};"><span style="font-weight: 600;">{who}</span> &middot; {place}</div><div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 2px;">{words}</div></div>{th}{CHEV}</div>')

def ending(doors, note=''):
    """How a collection ends: naturally, with the ways onward. No count, no ceremony."""
    out = '<div style="display: flex; flex-direction: column; gap: 2px; padding-top: 6px;">' + ''.join(door(d) for d in doors) + '</div>'
    if note: out += src(note)
    return out

# ───────────────────────────── the packet (synthetic; the shared world plus new venues) ─────────────────────────────
PACKET = {
    'print_room': dict(kind='room', name='The Harbor Print Room', where='Red Hook', hours='Tue&ndash;Sun 11&ndash;6', event='<i>Rooms Remade</i>, through Sunday', unknown='Whether the exhibition is ticketed hasn&rsquo;t been confirmed.'),
    'hour': dict(kind='hall', name='The listening hour at Canal Hall', when='Saturday 7&ndash;9 PM', price='$12 at the door', note='One recording played end to end in the back room, lights down. About sixty seats, no bar; doors 6:45.', unknown='Seats left for this Saturday haven&rsquo;t been confirmed.'),
    'market': dict(kind='market', name='The greenmarket', when='Saturday 8&ndash;1', price='free', note='Bread goes first; produce holds till one.'),
    'pier': dict(kind='pier', name='The pier at low water', when='Saturday 2:40&ndash;5', price='free', note='Walk the flood line east to where the granite kerbs end; shade on the water side after two.'),
    'film': dict(kind='film', name='Outdoor film on the lawn', when='Saturday 8:30 PM', price='free', note='By the pier in Sunset Park; bring something to sit on. Starts at dark.', unknown='Rain plan not posted.'),
    'noodles': dict(kind='noodles', name='The noodle counter', when='Daily 12&ndash;3, 6&ndash;10', price='$14&ndash;18', note='Hand-pulled at the counter; no wait before 12:30. Three blocks from Canal Hall.'),
    'library': dict(kind='library', name='The reading room at the branch library', when='Friday till 8', price='free', note='Long tables, lamps, quiet. Somewhere to sit for an hour.'),
    'organ': dict(kind='organ', name='Organ recital at the old church', when='Sunday 4 PM', price='free', note='Forty minutes; the back pews are the good ones for the sound.'),
    'table': dict(kind='table', name='The long table at the caf&eacute;', when='Saturday mornings', price='coffee', note='A communal table for twelve; regulars, room for strangers.'),
    'loop': dict(kind='loop', name='The waterfront loop', when='Any time', price='free', note='Five kilometres, flat, shaded after two; water at the far end.'),
    'two_piers': dict(kind='pier', name='Two piers, two directions', text='The Sunset Park pier faces west, into the sunset. The Red Hook pier faces the harbor and the Statue. Same evening light, opposite views; pick by what you want to see.'),
    'red_hook': dict(kind='quay', name='Red Hook', text='Harbor first, a scheduled way in, a flexible way out. Eighteen minutes on the map, about forty to get in by ferry or bus.'),
}
SORRENTO = {
    'reading_room': dict(kind='library', name='The reading room, upper town', when='Mornings', price='free', note='A small reading room with an exhibition preview; forty metres above the quay.'),
    'quay': dict(kind='quay', name='The quay walk', when='Any time', price='free', note='Along the water at sea level, step-free along the quay itself.'),
    'piazza': dict(kind='market', name='Thursday evening market in the piazza', when='Thursdays 6&ndash;10 PM', price='free', note='Food stalls and a band after eight; the upper town.'),
    'capri': dict(kind='quay', name='Capri, for a day', when='Ferries from 7:30', price='&euro;22 each way', note='Fifteen kilometres across the water; twenty-five minutes by the fast ferry. The last boat back is 6:40.', unknown='Sailings are cancelled in rough sea; check the morning of.'),
    'terraces': dict(kind='terrace', name='The lemon terraces walk', when='Mornings, till noon', price='free', note='Above the town; stepped paths, shade under the nets.'),
}
FRIENDS = [  # letter, name, words, place key, kind (picture) or None, group
    ('M', 'Maya', 'The side room was my favorite. Go on a weekday, it was empty.', 'print_room', 'room', 'Red Hook'),
    ('P', 'Priya', 'Rainy Tuesday, the back room to myself for an hour.', 'print_room', None, 'Red Hook'),
    ('P', 'Priya', 'The Red Hook pier at seven: the whole harbor lit up.', 'red_hook', 'pier', 'Red Hook'),
    ('S', 'Sam', 'Sit on the left side, that&rsquo;s where the speakers are.', 'hour', None, 'Canal side'),
    ('M', 'Maya', 'Counter seat, the beef one. Twelve sharp or you wait.', 'noodles', 'noodles', 'Canal side'),
    ('S', 'Sam', 'Best lunch near the hall. Cash only, still.', 'noodles', None, 'Canal side'),
    ('M', 'Maya', 'Sesame loaf, Sundays only. Before eleven or it&rsquo;s gone.', 'bakery', 'loaf', 'Sunset Park'),
    ('M', 'Maya', 'Went back for the pier at sunset. Bring a jacket, it turns cold fast.', 'pier', 'pier', 'Sunset Park'),
    ('A', 'Alex', 'The lawn by the pier for the film. Get there at eight for a spot.', 'film', None, 'Sunset Park'),
    ('A', 'Alex', 'I run the loop on Saturdays, early. It&rsquo;s flat the whole way.', 'loop', 'loop', 'Sunset Park'),
    ('A', 'Alex', 'Sunset Park, generally. The pier at sunset.', 'sunset_park', None, 'Sunset Park'),
    ('T', 'Theo', 'Bread stall sells out by ten.', 'market', None, 'The market'),
    ('T', 'Theo', 'The reading room upstairs is open late on Fridays. Nobody knows.', 'library', 'library', 'Downtown'),
    ('M', 'Maya', 'Went last month, sat at the back. Forty minutes, then coffee.', 'organ', 'organ', 'Downtown'),
    ('P', 'Priya', 'The organ one is lovely. Go early for the back pews.', 'organ', None, 'Downtown'),
    ('M', 'Maya', 'The long table on Saturday mornings. Talk to whoever&rsquo;s there.', 'table', 'table', 'Downtown'),
    ('D', 'Dana', 'Back at the bookshop where we met. Ten years this month.', 'bookshop', None, 'Carroll Gardens'),
    ('P', 'Priya', 'The pigeons at the market have a system. I have watched it for twenty minutes.', 'market', None, 'The market'),
    ('A', 'Alex', 'First time round the loop without stopping. Barely.', 'loop', 'loop', 'Sunset Park'),
    ('M', 'Maya', 'Tuesday, seven.', 'pier', 'pier', 'Sunset Park'),
    ('P', 'Priya', 'Fell asleep in the organ one, happily. Ask Maya, she stayed awake.', 'organ', None, 'Downtown'),
    ('D', 'Dana', 'We spent the late afternoon by the water.', 'sorrento', None, 'Elsewhere'),
]
PLACE_NAMES = {'print_room': 'The Harbor Print Room', 'red_hook': 'The Red Hook pier', 'hour': 'Canal Hall', 'noodles': 'The noodle counter', 'bakery': 'The Sunset Park bakery', 'pier': 'The pier, Sunset Park', 'film': 'The lawn by the pier', 'loop': 'The waterfront loop', 'sunset_park': 'Sunset Park', 'market': 'The greenmarket', 'library': 'The branch library', 'organ': 'The old church', 'table': 'The caf&eacute; with the long table', 'bookshop': 'The bookshop on Court Street', 'sorrento': 'Sorrento'}

# ───────────────────────────── board helpers ─────────────────────────────
def two_rows(w, key, kick, ttl, sub, row1, div_kick, div_title, row2, default_h=4600):
    html = page(w, hh(key, default_h), kick, ttl, sub, row1)
    html = html.replace('</helmet>', FN11 + '</helmet>', 1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">{div_kick}</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">{div_title}</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

def one_row(w, key, kick, ttl, sub, row1, default_h=3000):
    return page(w, hh(key, default_h), kick, ttl, sub, row1).replace('</helmet>', FN11 + '</helmet>', 1)

def changelog(rows):
    """The outside-phone change log the review asks for: value delivered, interaction clearer, evidence, dependencies."""
    return tbl(['PHONE', 'VALUE DELIVERED', 'INTERACTION NOW CLEARER', 'EVIDENCE BEHIND PRACTICAL CLAIMS', 'UNRESOLVED DEPENDENCY'], rows)
