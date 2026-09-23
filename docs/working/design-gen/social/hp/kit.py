# Shared markup kit for the HP value-pass boards. Values are lifted from the
# live boards (C1AvailableMature, HomeUrgent, PlaceFocus, HomeSaturday) after
# the 09-02 law passes: crown serif 22/600, 22px above the crown, radii
# 18/12/999, people = ink, kicker registers mute/gold, ghost anchors #8F877C,
# 10px floor, map plates as wash. Fixture copy only.

INK = '#1B1714'; INK2 = '#2C2622'; MUTE = '#6E6862'; GHOST = '#B5AFA5'; ANCHOR = '#8F877C'
PAPER = '#EFEAE0'; CARD = '#FBF7EC'; WASH = '#E8E2D4'; GOLD = '#B0853A'; GOLDD = '#8A6628'
OX = '#7A2E2E'; UMBER = '#4A3428'; PLAN = '#2A384B'; PLANL = '#3D5066'; GREEN = '#3D7050'

MONO = "font-family: 'JetBrains Mono', ui-monospace, monospace;"
SERIF = "font-family: 'EB Garamond', Georgia, serif;"
SANS = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;"

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;700&display=swap">
  <style>
    body { margin: 0; }
    a { color: #8A6628; } a:hover { color: #4A3428; }
    .fn { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; letter-spacing: 0.9px; color: #B5AFA5; }
    .kick { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #8A6628; }
    .kickm { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }
    .shead { display: flex; align-items: center; gap: 10px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }
    .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }
    .hatch { background: repeating-linear-gradient(135deg, rgba(176,133,58,0.12) 0 7px, rgba(176,133,58,0.04) 7px 14px); }
    .row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); }
    .chev { flex: none; }
    .day { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 8px 0 6px; white-space: nowrap; }
    .dayl { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: #8F877C; }
    .daym { width: 7px; height: 7px; border-radius: 4px; }
    .lab { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; padding: 0 0 10px 2px; display: flex; gap: 8px; align-items: baseline; }
    .lab .s { font-weight: 400; letter-spacing: 0.9px; color: #B5AFA5; }
    .led { display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 6px 14px; font-size: 12.5px; line-height: 18px; color: #2C2622; }
    .led .k { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: #6E6862; padding-top: 3px; }
  </style>
</helmet>
'''
TAIL = '''</x-dc>
</body>
</html>
'''

CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="#8A6628" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BACK = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><circle cx="9" cy="9" r="5.5" stroke="#6E6862" stroke-width="1.5"/><path d="M13.5 13.5L17 17" stroke="#6E6862" stroke-width="1.5" stroke-linecap="round"/></svg>'
MAPI = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M3 6.5L8 4.5L12 6.5L17 4.5V13.5L12 15.5L8 13.5L3 15.5V6.5Z" stroke="#6E6862" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 4.5V13.5M12 6.5V15.5" stroke="#6E6862" stroke-width="1.5"/></svg>'
NOTE = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="flex: none; margin-top: 2px;"><rect x="1" y="1" width="14" height="14" rx="3.5" stroke="#8A6628" stroke-width="1.5"/><path d="M4.5 6 L11.5 6 M4.5 9.5 L9 9.5" stroke="#8A6628" stroke-width="1.3" stroke-linecap="round"/></svg>'

def tabbar(active='Home'):
    def tab(name, path, extra=''):
        on = name == active
        col = INK if on else MUTE
        w = '1.6' if on else '1.5'
        lab = f'<span style="font-size: 10px; font-weight: {600 if on else 500}; letter-spacing: 0.4px; color: {col};">{name}</span>'
        return f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px;"><svg width="21" height="21" viewBox="0 0 21 21" fill="none">{path.replace("STROKE", col).replace("W", w)}{extra.replace("STROKE", col)}</svg>{lab}</div>'
    home = '<path d="M3.5 9.5L10.5 3.5L17.5 9.5V17H12.5V12.5H8.5V17H3.5V9.5Z" stroke="STROKE" stroke-width="W" stroke-linejoin="round"/>'
    chat = '<path d="M3.5 5.5H17.5V14.5H9.5L6 17.5V14.5H3.5V5.5Z" stroke="STROKE" stroke-width="W" stroke-linejoin="round"/>'
    places = '<path d="M10.5 17.5C10.5 17.5 16 12.5 16 8.5C16 5.5 13.5 3.5 10.5 3.5C7.5 3.5 5 5.5 5 8.5C5 12.5 10.5 17.5 10.5 17.5Z" stroke="STROKE" stroke-width="W" stroke-linejoin="round"/>'
    places_x = '<circle cx="10.5" cy="8.5" r="1.8" stroke="STROKE" stroke-width="1.4"/>'
    life = '<path d="M5 3.5H16V17.5H5V3.5Z" stroke="STROKE" stroke-width="W" stroke-linejoin="round"/>'
    life_x = '<path d="M8 3.5V17.5" stroke="STROKE" stroke-width="1.4"/><path d="M10.5 7H13.5M10.5 10H13.5" stroke="STROKE" stroke-width="1.3" stroke-linecap="round"/>'
    return ('<div style="border-top: 1px solid rgba(27,23,20,0.10); background: #FBF7EC; display: flex; padding: 10px 22px 22px 22px; margin-top: 28px;">'
            + tab('Home', home) + tab('Chat', chat) + tab('Places', places, places_x) + tab('Life', life, life_x) + '</div>')

def phone(inner, h, active='Home', extra_style=''):
    return (f'<div style="width: 393px; min-height: {h}px; background: {PAPER}; {SANS} color: {INK}; display: flex; flex-direction: column; box-sizing: border-box; {extra_style}">'
            + inner + '<div style="flex-grow: 1;"></div>' + tabbar(active) + '</div>')

def anchor_row(scope, time, sub=None):
    """Home anchor: mono scope + time + account avatar (Home's only header button)."""
    s = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">'
         f'<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">{scope}</span>'
         f'<span class="fn" style="margin-left: auto;">{time}</span>'
         f'<span style="width: 24px; height: 24px; border-radius: 999px; background: {UMBER}; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">N</span></div>')
    return s + '</div>'

def orientation(read, sub, size=30, lh=34):
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: {size}px; line-height: {lh}px; letter-spacing: -0.01em;">{read}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div></div>')

def orientation_direct(read, sub):
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">{read}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">{sub}</div></div>')

def crown(status_color, status, title, deck, instrument='', cta=None, fn='', extra=''):
    parts = [f'<div style="margin: 22px 22px 0 22px; background: {CARD}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: 16px; display: flex; flex-direction: column; gap: 6px;">',
             f'<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {status_color}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {status_color};">{status}</span></div>',
             f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 26px; letter-spacing: -0.2px; margin-top: 4px;">{title}</div>']
    if deck:
        parts.append(f'<div style="{SERIF} font-size: 16px; line-height: 22px; font-weight: 500; color: {INK2}; margin-top: 2px;">{deck}</div>')
    parts.append(instrument)
    parts.append(extra)
    if cta:
        parts.append(f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">{cta}</span></div>')
    if fn:
        parts.append(f'<div class="fn">{fn}</div>')
    parts.append('</div>')
    return ''.join(parts)

def section(title, mute=True, top=44):
    cls = 'shead' if mute else 'shead'
    col = MUTE if mute else GOLDD
    return f'<div style="padding: {top}px 22px 0 22px;"><div class="{cls}" style="color: {col}; padding-bottom: 8px;"><span>{title}</span><span class="rule"></span></div></div>'

def row(text, mark='dot', color=MUTE, avatar=None, muted=False, last=False, sub=None):
    """Canonical in-motion row (§12.7 g): 44px, status mark + one line + chevron; avatar only when a person is the subject."""
    if avatar:
        lead = f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex: none;">{avatar}</span>'
    elif mark == 'dashed':
        lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px dashed {color}; box-sizing: border-box; flex: none;"></span>'
    elif mark == 'hollow':
        lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px solid {color}; box-sizing: border-box; flex: none;"></span>'
    elif mark == 'none':
        lead = ''
    else:
        lead = f'<span style="width: 7px; height: 7px; border-radius: 4px; background: {color}; flex: none;"></span>'
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.06);' if last else ''
    col = MUTE if muted else INK
    return (f'<div class="row" style="padding: 8px 0;{bb}">{lead}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {col};">{text}</span>{CHEV}</div>')

def door(text, color=GOLDD):
    return f'<div style="display: flex; align-items: center; min-height: 44px;"><span style="font-size: 13px; font-weight: 500; color: {color};">{text}</span>{ARROW}</div>'

def week_seam(days, top=32):
    """Banded seam (§12.7 d), day names at the 10px floor. days: list of (name, mark_html, label, color)."""
    cells = ''
    for name, mark, label, col in days:
        lc = col if label else 'transparent'
        cells += f'<div class="day"><span class="dayl" style="color: {col if col in (OX, INK) else ANCHOR};">{name}</span>{mark}<span style="font-size: 10px; color: {lc};">{label or "."}</span></div>'
    return (f'<div style="margin: {top}px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">{cells}</div></div>')

def dm(kind, color):
    if kind == 'solid': return f'<span class="daym" style="background: {color};"></span>'
    if kind == 'dashed': return f'<span class="daym" style="border: 1.5px dashed {color}; box-sizing: border-box;"></span>'
    if kind == 'hollow': return f'<span class="daym" style="border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;"></span>'
    if kind.startswith('av:'):
        return f'<span style="width: 18px; height: 18px; border-radius: 9px; background: {INK}; color: {CARD}; font-size: 9px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: -5px 0;">{kind[3:]}</span>'
    return ''

def coda(text, fn):
    return (f'<div style="padding: 44px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">{text}</div>'
            f'<div class="fn" style="margin-top: 14px; letter-spacing: 1.3px;">{fn}</div></div>')

def unit_open(kick, title, body, plate=None, plate_label=None):
    """A reading/possibility unit on bare paper: 56px thumb plate + gold kicker + serif 16/500 title + grey body."""
    pl = ''
    if plate == 'thumb':
        pl = f'<div class="hatch" style="width: 56px; height: 56px; border-radius: 12px; flex: none; display: flex; align-items: center; justify-content: center;">{plate_label or ""}</div>'
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start;">{pl}<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px;">'
            f'<span class="kick">{kick}</span><span style="{SERIF} font-weight: 500; font-size: 16px; line-height: 21px; color: {INK};">{title}</span>'
            f'<span style="font-size: 12.5px; line-height: 17px; color: {MUTE};">{body}</span></div></div>')

def passage(paras, cite=None):
    """A composed readable passage — the promise fulfilled on view. serif 15/22 roman ink."""
    ps = ''.join(f'<p style="{SERIF} font-size: 15px; line-height: 22px; color: {INK2}; margin: 0 0 10px 0;">{p}</p>' for p in paras)
    c = f'<div class="fn" style="margin-top: 2px;">{cite}</div>' if cite else ''
    return f'<div style="padding-top: 8px;">{ps}{c}</div>'

def board(inner, w, h, bg='#F4F0E7', pad='26px 24px 24px 24px', gap=46):
    return (HEAD + f'<div style="width: {w}px; min-height: {h}px; background: {bg}; box-sizing: border-box; padding: {pad}; display: flex; gap: {gap}px; align-items: flex-start; {SANS} color: {INK};">'
            + inner + '</div>' + TAIL)

def label(color, t, s):
    return f'<div class="lab" style="color: {color};"><span>{t}</span><span class="s">{s}</span></div>'

def ledger(rows):
    """rows: list of (key, value)"""
    return '<div class="led">' + ''.join(f'<span class="k">{k}</span><span>{v}</span>' for k, v in rows) + '</div>'

def notecol(title, blocks, w=440):
    """A side column of annotation blocks outside the phone: [(kicker, html)]"""
    out = f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 22px; padding-top: 24px;">'
    out += f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 25px; color: {INK};">{title}</div>'
    for k, html in blocks:
        out += f'<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kickm">{k}</div>{html}</div>'
    return out + '</div>'
