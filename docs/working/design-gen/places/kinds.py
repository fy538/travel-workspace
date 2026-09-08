"""The Places kinds taken from the a26e3228 union and The Page, drawn on the chosen terms. Each is a function; 07 shows them, 08 uses them."""
from fix import *
import gen21
# ── field ──
def glyph_plate(svg, size=44): return f'<div style="width: {size}px; height: {size}px; border-radius: 12px; flex: none; display: flex; align-items: center; justify-content: center; background: {HATCH};">{svg}</div>'
G_HARBOR = f'<svg width="27" height="27" viewBox="0 0 27 27" fill="none"><path d="M4 18 L23 18" stroke="{GOLDD}" stroke-width="1.3" stroke-linecap="round"/><path d="M6 18 Q9 8 13.5 8 Q18 8 21 18" stroke="{GOLDD}" stroke-width="1.3" fill="none"/><path d="M5 22 Q9 20 13.5 22 Q18 24 22 22" stroke="{GOLD}" stroke-width="1.3" fill="none" stroke-linecap="round"/></svg>'
G_PIER = f'<svg width="27" height="27" viewBox="0 0 27 27" fill="none"><path d="M4 16 L23 16" stroke="{GOLDD}" stroke-width="1.3" stroke-linecap="round"/><path d="M7 16 V22 M12 16 V22 M17 16 V22 M22 16 V22" stroke="{GOLDD}" stroke-width="1.2"/><circle cx="19" cy="9" r="2.5" stroke="{GOLD}" stroke-width="1.3"/></svg>'
G_PARK = f'<svg width="27" height="27" viewBox="0 0 27 27" fill="none"><ellipse cx="13.5" cy="15" rx="8" ry="5.5" stroke="{GOLDD}" stroke-width="1.3"/><path d="M3 8 Q8 10 13.5 8 Q19 6 24 8" stroke="{GOLD}" stroke-width="1.3" fill="none" stroke-linecap="round"/></svg>'
def branch_row(svg, name, line, last=False, first=False):
    return f'<div style="display: flex; align-items: center; gap: 14px; min-height: 56px; padding: 6px 0;{"" if first else " border-top: 1px solid " + HAIR6 + ";"}{" border-bottom: 1px solid " + HAIR6 + ";" if last else ""}">{glyph_plate(svg)}<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; font-weight: 600; line-height: 19px;">{name}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">{line}</div></div>{CHEV}</div>'
def branch_lead():
    return '<div>' + branch_row(G_HARBOR, 'Red Hook', 'Harbor first · a scheduled way in · a flexible way out', first=True) + branch_row(G_PIER, 'Sunset Park', 'Continuous land access · easiest to shorten') + branch_row(G_PARK, 'Downtown', 'The market and the church · on foot from the train', last=True) + '</div>'
def returned_understanding():
    return kick('DISTANCE IS NOT THE WHOLE ARRIVAL') + f'<div style="margin-top: 8px;">{serifline("What Sorrento taught: a cliff between two points 180 metres apart. New York&rsquo;s waterfronts separate access differently, by water.", 16, 22)}</div>' + door('Follow the threshold comparison')
def provenance_label(): return f'<div style="display: flex; align-items: center; gap: 8px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {GOLDD};"><span>FROM HOME</span><span style="color: {GHOST};">·</span><span>SATURDAY, THE PIER</span><span style="color: {GHOST};">·</span><span style="color: {ANCHOR}; font-weight: 400;">RENDERED FROM WHAT HOME SENT</span></div>'
# ── focus (the place page) ──
def identity_map(h=150):
    return (f'<div style="height: {h}px; border-radius: 14px; overflow: hidden; position: relative; background: {WASH};"><svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="position: absolute; inset: 0; width: 100%; height: 100%;">'
            f'<path d="M0 0 L0 {h} L120 {h} C112 {h*0.7:.0f} 90 {h*0.5:.0f}50 {h*0.3:.0f} C30 {h*0.2:.0f} 12 {h*0.1:.0f} 0 0 Z" fill="rgba(61,80,102,0.20)"/><path d="M0 0 C12 {h*0.1:.0f} 30 {h*0.2:.0f} 50 {h*0.3:.0f} C90 {h*0.5:.0f} 112 {h*0.7:.0f} 120 {h}" stroke="rgba(61,80,102,0.5)" stroke-width="2" fill="none"/>'
            f'<line x1="150" y1="10" x2="215" y2="{h}" stroke="rgba(27,23,20,0.12)" stroke-width="10"/><line x1="90" y1="{h*0.62:.0f}" x2="349" y2="{h*0.32:.0f}" stroke="rgba(27,23,20,0.12)" stroke-width="7"/>'
            f'<circle cx="236" cy="{h*0.42:.0f}" r="9" fill="{INK}" stroke="{GOLD}" stroke-width="2.5"/><circle cx="118" cy="{h*0.78:.0f}" r="4" fill="{INK}"/>'
            f'<text x="252" y="{h*0.42+4:.0f}" {LK}>THE PRINT ROOM</text><text x="126" y="{h*0.78+4:.0f}" {LB}>THE LANDING · 9 MIN</text></svg></div>')
def verdict(claim, basis):
    return f'<div style="{SERIF} font-size: 20px; line-height: 26px; color: {INK};">{claim}</div>' + fn(basis, 6)
def hours_register(rows, change=None):
    out = '<div style="display: flex; flex-direction: column;">' + ''.join(f'<div style="display: flex; gap: 12px; align-items: baseline; padding: 7px 0; border-top: 1px solid {HAIR7};"><span class="fn" style="width: 96px; flex: none; color: {ANCHOR};">{k}</span><span style="font-size: 14px; line-height: 19px; color: {INK};">{v}</span></div>' for k, v in rows) + '</div>'
    if change: out += f'<div style="margin-top: 8px; padding: 10px 14px; border-radius: 12px; background: {CARD}; border: 1px solid {HAIR}; display: flex; gap: 12px; align-items: center;"><span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px; color: {OX}; flex: none;">CHANGED</span><div style="font-size: 13px; line-height: 18px; color: {INK2};">{change}</div></div>'
    return out
def relationship_trace(t, sub): return f'<div style="display: flex; gap: 10px; align-items: flex-start;"><span style="width: 7px; height: 7px; border-radius: 4px; background: {UMBER}; flex: none; margin-top: 6px;"></span><div><div style="font-size: 14px; line-height: 19px; color: {INK};">{t}</div>{fn(sub, 3)}</div></div>'
def horizon_doors(items):
    return '<div>' + ''.join(f'<div style="display: flex; gap: 14px; align-items: center; padding: 10px 0;{"" if i else " border-top: 0;"} border-top: 1px solid {HAIR7};"><span class="fn" style="width: 72px; flex: none; color: {GOLDD};">{k}</span><span style="font-size: 14px; line-height: 19px; color: {INK}; flex: 1;">{t}</span>{ARROW()}</div>' for i, (k, t) in enumerate(items)) + '</div>'
def possibility_row(name, line, when):
    return f'<div style="display: flex; gap: 14px; align-items: center;">{glyph_plate("", 56)}<div style="flex: 1; min-width: 0;">{title(name, 16, 21)}<div style="font-size: 13px; line-height: 18px; color: {MUTE};">{line}</div>{fn(when, 3)}</div>{CHEV}</div>'
def stub(name, known, last_line='Nothing more is known about it yet.'):
    return title(name, 17, 22) + sup(known) + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 8px; padding-top: 8px; border-top: 1px solid {HAIR7};">{last_line}</div>'
# ── path ──
def evidence_apparatus(kick_t, items):
    return kick(kick_t) + '<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 8px;">' + ''.join(f'<div style="display: flex; gap: 12px; align-items: baseline;"><span style="{SERIF} font-size: 18px; font-weight: 600; color: {GOLDD}; width: 16px; flex: none;">{i+1}</span><span style="font-size: 14px; line-height: 19px; color: {INK};">{t}</span></div>' for i, t in enumerate(items)) + '</div>'
def consequence(kick_t, t, door_t=None): return kick(kick_t) + f'<div style="margin-top: 8px;">{serifline(t, 16, 22)}</div>' + (door(door_t) if door_t else '')
def next_rows(items): return '<div>' + ''.join(f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0; border-top: 1px solid {HAIR7};"><span style="font-size: 14px; line-height: 19px; color: {INK}; flex: 1;">{t}</span>{ARROW()}</div>' for t in items) + '</div>'
# ── live ──
def burden_receipt(kick_t, k, v): return f'<div style="padding: 12px 14px; border-radius: 12px; background: {CARD}; border: 1px solid {HAIR};"><div class="kickm" style="color: {GOLDD};">{kick_t}</div><div style="display: flex; gap: 12px; align-items: baseline; margin-top: 6px;"><span class="fn" style="color: {ANCHOR}; width: 64px; flex: none;">{k}</span><span style="font-size: 14px; line-height: 19px; color: {INK};">{v}</span></div></div>'
def live_fallback(kick_t, t): return kick(kick_t) + f'<div style="margin-top: 8px;">{serifline(t, 16, 22)}</div>'
def temporal_posture(state, line, dot=None):
    col = {'HOLD': GOLD, 'ACT NOW': OX, 'DONE': INK}.get(state, GOLD)
    return f'<div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: center; gap: 8px;"><span style="width: 7px; height: 7px; border-radius: 4px; background: {col};"></span><span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px; color: {INK};">{state}</span>' + (f'<span class="fn" style="color: {ANCHOR};">· {dot}</span>' if dot else '') + f'</div><div style="{SERIF} font-size: 16px; line-height: 22px; color: {INK};">{line}</div></div>'
# ── social ──
def plural_comparison(a, b):
    def half(who, when, words, left):
        return f'<div style="flex: 1; min-width: 0; {"padding-right: 14px;" if left else "padding-left: 14px; border-left: 1px solid " + HAIR + ";"}">' + author_row(who[0], who[1], '') + f'<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK}; margin-top: 8px;">&ldquo;{words}&rdquo;</div>{fn(who[2] + " · " + when, 4)}</div>'
    return '<div style="display: flex;">' + half(a[0], a[1], a[2], True) + half(b[0], b[1], b[2], False) + '</div>'
