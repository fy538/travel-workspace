"""Board 22 — Making live visible (exploration, 2026-09-23).
Founder: 19/20 look off; 21 closer; "the user needs to know something is live more visually, instead of just a regular card".
Three treatments of the same three live moments, for a pick before 19-21 are rebuilt:
  A live instrument crown · B live band (in-app Live Activity) · C live field (the top of Home changes key).
Live colour = the kernel's state.live (#6B8F5E); urgent keeps oxblood. Pulse is a CSS animation.
Usage: python3 gen_live_explore.py <in_dir holding 12 and 00> <out_dir>
"""
import sys, os
IN, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], IN, OUT]
import gen_vdl as G
MONO, SERIF, SANS, CHEV = G.MONO, G.SERIF, G.SANS, G.CHEV
INK, INK2, MUTE, HINT, GOLD, CARD, PAPER, OX = '#1B1714', '#2C2622', '#6E6862', '#8F877C', '#B0853A', '#FBF7EC', '#EFEAE0', '#7A2E2E'
LIVE, LIVED = '#6B8F5E', '#4E6B43'
opener, TAB = G.home_parts()
fn, cell, notes, gold = G.fn, G.cell, G.notes, G.gold_door
def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'
def phone(*parts): return opener + ''.join(parts) + '<div style="flex-grow: 1;"></div>' + TAB
def anchor(place, time, who='N', color=INK):
    av = f'<span style="width: 24px; height: 24px; border-radius: 999px; background: #4A3428; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">{who}</span>' if who else ''
    return (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px; color: {color};">{place}</span>'
            f'<span class="fn" style="margin-left: auto;">{time}</span>{av}</div></div>')
def read(t, sub='', size=30, color=INK, subc=MUTE):
    lh = {30: 34, 26: 30, 22: 27}[size]
    s = f'<div style="font-size: 12.5px; line-height: 17px; color: {subc}; margin-top: 7px;">{sub}</div>' if sub else ''
    return f'<div style="padding: 6px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: {size}px; line-height: {lh}px; letter-spacing: -0.01em; color: {color}; text-wrap: balance;">{t}</div>{s}</div>'
def sect(name, top=32):
    return (f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px;">{name}</span>'
            f'<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
def row(text, sub='', last=False, lead=''):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    s = f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{sub}</div>' if sub else ''
    return (f'<div class="row" style="padding: 10px 0; align-items: flex-start;{b}">{lead}<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px;">{text}</div>{s}</div>'
            f'<span style="padding-top: 3px;">{CHEV}</span></div>')
def rows(*r): return gut('<div style="border-top: 1px solid rgba(27,23,20,0.10);">' + ''.join(r) + '</div>')
def face(ls, size=22, ring=PAPER):
    return ''.join(f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {"#4A3428" if l == "N" else INK}; color: {CARD}; font-size: 9.5px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {ring}; margin-left: {0 if i == 0 else -7}px;">{l}</span>' for i, l in enumerate(ls))

def pulse(color=LIVE, label='LIVE', txt=None):
    t = txt or color
    return (f'<span style="display: inline-flex; align-items: center; gap: 7px;"><span class="pulse" style="--pc: {color};"></span>'
            f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {t};">{label}</span></span>')

# ---- the live instruments: one axis grammar, now as a line -------------------------------------------------
def axis_svg(W, t0, t1, spans=(), marks=(), now=None, ticks=(), dark=False, h=70):
    ink = CARD if dark else INK; mute = 'rgba(251,247,236,0.55)' if dark else HINT; track = 'rgba(251,247,236,0.14)' if dark else 'rgba(27,23,20,0.08)'
    x = lambda t: 4 + (t - t0) / (t1 - t0) * (W - 8)
    out = [f'<svg width="{W}" height="{h}" viewBox="0 0 {W} {h}" fill="none" style="display: block; overflow: visible;">',
           f'<rect x="4" y="{h-30}" width="{W-8}" height="4" rx="2" fill="{track}"/>']
    for t, lab in ticks:
        out.append(f'<text x="{x(t):.1f}" y="{h-6}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.6" fill="{mute}">{lab}</text>')
    for i, (a, b, lab, style) in enumerate(spans):
        y = h - 32 - (i % 2) * 0
        col = {'solid': (GOLD if not dark else '#D9BD86'), 'water': '#9DBFC6', 'live': LIVE}[style]
        out.append(f'<rect x="{x(a):.1f}" y="{h-33}" width="{max(6, x(b)-x(a)):.1f}" height="10" rx="5" fill="{col}"/>')
        lx, anc = (x(b), 'end') if (now is not None and x(a) <= x(now) <= x(a) + 7 * len(lab)) else (x(a), 'start')
        out.append(f'<text x="{lx:.1f}" y="{h-40 - (i % 2) * 13}" text-anchor="{anc}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.6" fill="{ink}">{lab}</text>')
    for t, lab, kind in marks:
        cx = x(t); fill = ink if kind == 'set' else 'none'
        out.append(f'<circle cx="{cx:.1f}" cy="{h-28}" r="5" fill="{fill if kind == "set" else (INK2 if dark else PAPER)}" stroke="{ink}" stroke-width="1.5" {"stroke-dasharray=\"2 2\"" if kind == "said" else ""}/>')
        out.append(f'<text x="{cx:.1f}" y="{h-40}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.4" fill="{ink}">{lab}</text>')
    if now is not None:
        nx = x(now)
        out.append(f'<line x1="{nx:.1f}" y1="{h-35}" x2="{nx:.1f}" y2="{h-21}" stroke="{LIVE}" stroke-width="2.5" stroke-linecap="round"/>')
        out.append(f'<circle cx="{nx:.1f}" cy="{h-28}" r="4.5" fill="{LIVE}" stroke="{PAPER if not dark else INK}" stroke-width="1.5"/>')
    out.append('</svg>')
    return ''.join(out)
def journey_svg(W, stops, at, dark=False, h=64):
    """Stops as nodes on a line; done stops filled, the current position a live node."""
    ink = CARD if dark else INK; mute = 'rgba(251,247,236,0.55)' if dark else HINT; track = 'rgba(251,247,236,0.18)' if dark else 'rgba(27,23,20,0.12)'
    n = len(stops); xs = [8 + i * (W - 16) / (n - 1) for i in range(n)]
    out = [f'<svg width="{W}" height="{h}" viewBox="0 0 {W} {h}" fill="none" style="display: block; overflow: visible;">',
           f'<line x1="{xs[0]}" y1="22" x2="{xs[-1]}" y2="22" stroke="{track}" stroke-width="3" stroke-linecap="round"/>']
    done_x = xs[0] + (xs[min(int(at) + 1, n - 1)] - xs[int(at)]) * (at - int(at)) + (xs[int(at)] - xs[0])
    out.append(f'<line x1="{xs[0]}" y1="22" x2="{done_x:.1f}" y2="22" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    for i, (lab, t) in enumerate(stops):
        done = i <= at
        out.append(f'<circle cx="{xs[i]:.1f}" cy="22" r="5" fill="{ink if done else (INK2 if dark else PAPER)}" stroke="{ink}" stroke-width="1.5"/>')
        anchor_ = 'start' if i == 0 else ('end' if i == n - 1 else 'middle')
        out.append(f'<text x="{xs[i]:.1f}" y="46" text-anchor="{anchor_}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.4" fill="{ink}">{lab}</text>')
        out.append(f'<text x="{xs[i]:.1f}" y="59" text-anchor="{anchor_}" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.4" fill="{mute}">{t}</text>')
    out.append(f'<circle cx="{done_x:.1f}" cy="22" r="7" fill="{LIVE}" stroke="{PAPER if not dark else INK}" stroke-width="2"/>')
    out.append('</svg>')
    return ''.join(out)

# ---- the three moments ------------------------------------------------------------------------------------
H = lambda hh, mm=0: hh + mm / 60
M = {
 'city': dict(place='NEW YORK &middot; SATURDAY', time='10:40 AM', who='', live='HERE NOW &middot; RED HOOK',
              title='The flea is on until three.', sub='Low water on the pier from 2:40 &middot; clear, 58&deg;.',
              inst=lambda W, dark=False: axis_svg(W, H(10), H(18), spans=[(H(10), H(15), 'THE FLEA', 'solid'), (H(14, 40), H(17, 10), 'LOW WATER', 'water')],
                                                  now=H(10, 40), ticks=[(H(11), '11'), (H(13), '1'), (H(15), '3'), (H(17), '5')], dark=dark),
              facts='6 min to the flea &middot; 9 to the pier',
              tail=lambda: sect('Worth reading') + gut(f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500;">The pumps under the park finish what the gates cannot</div>' + fn('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', mt=6))),
 'eve': dict(place='NEW YORK &middot; SATURDAY', time='7:25 PM', who='N', live='LIVE &middot; PASTA NIGHT',
             title='Sam around 7:30. Maya at eight.', sub='From seven at yours &middot; Sam leaves by nine.',
             inst=lambda W, dark=False: axis_svg(W, H(18, 45), H(21, 15), marks=[(H(19), 'FROM 7', 'set'), (H(19, 30), 'SAM', 'said'), (H(20), 'MAYA', 'said'), (H(21), 'SAM GOES', 'set')],
                                                 now=H(19, 25), ticks=[(H(19), '7'), (H(20), '8'), (H(21), '9')], dark=dark),
             facts='Times are their own words',
             tail=lambda: sect('For tonight') + gut(f'<div style="display: flex; gap: 10px; align-items: center;">{face(["D"], 26)}<span style="font-size: 13px; font-weight: 600;">Dana</span><span class="fn" style="color: {HINT};">FRI &middot; SORRENTO</span></div>'
                                                    f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 23px; margin-top: 8px;">Fry the zucchini first and let them sit. Twenty minutes, not five.</div>')),
 'gate': dict(place='JFK &middot; TERMINAL 4', time='5:20 PM', who='N', live='LIVE &middot; TAP 214',
              title='Boarding at 6:05 from B22.', sub='45 minutes &middot; a two-minute walk to the gate.',
              inst=lambda W, dark=False: journey_svg(W, [('HOME', '3:40'), ('T4', '5:05'), ('BAGS', 'DONE'), ('B22', 'NOW'), ('BOARD', '6:05'), ('LIS', '6:58')], 3, dark=dark),
              facts='Gate from the airline &middot; 5:18 PM',
              tail=lambda: sect('From Maya') + gut(f'<div style="display: flex; gap: 10px; align-items: center;">{face(["M"], 26)}<span style="font-size: 13px; font-weight: 600;">Maya</span><span class="fn" style="color: {HINT};">4:48 PM</span></div>'
                                                   f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 23px; margin-top: 8px;">we land 9:25, meet you at the stay? bringing the good coffee</div>'))}

# A · live instrument crown: elevated card, live chip, now-line instrument
def A(k):
    m = M[k]
    crown = gut(f'<div style="background: {CARD}; border-radius: 18px; padding: 16px 18px 14px; box-shadow: 0 0 0 1.5px rgba(107,143,94,0.55), 0 10px 26px -10px rgba(27,23,20,0.28);">'
                f'<div style="display: flex; align-items: center;">{pulse(label=m["live"], txt=LIVED)}<span class="fn" style="margin-left: auto; color: {HINT};">{m["time"]}</span></div>'
                f'<div style="margin-top: 14px;">{m["inst"](313)}</div>'
                f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 8px;">{m["facts"]}</div></div>', 18)
    return phone(anchor(m['place'], m['time'], m['who']), read(m['title'], m['sub']), crown, m['tail']())
# B · live band: dark capsule under the anchor, like a Live Activity
def B(k):
    m = M[k]
    band = (f'<div style="margin: 14px 12px 0 12px; background: {INK}; border-radius: 22px; padding: 14px 16px 12px; color: {CARD};">'
            f'<div style="display: flex; align-items: center;">{pulse(label=m["live"], txt="#A9C49C")}<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; color: rgba(251,247,236,0.55); letter-spacing: 0.8px;">{m["time"]}</span></div>'
            f'<div style="font-family: {SERIF}; font-size: 21px; line-height: 25px; font-weight: 600; margin-top: 8px;">{m["title"]}</div>'
            f'<div style="margin-top: 10px;">{m["inst"](345, dark=True)}</div></div>')
    return phone(anchor(m['place'], m['time'], m['who']), band, gut(f'<div style="font-size: 13px; line-height: 18px; color: {MUTE};">{m["sub"]}</div>', 12), m['tail']())
# C · live field: the head of Home changes key
def C(k):
    m = M[k]
    field = (f'<div style="background: #E4EBDC; border-bottom: 1.5px solid rgba(107,143,94,0.55); padding-bottom: 20px;">'
             + anchor(m['place'], m['time'], m['who'], color=LIVED)
             + gut(pulse(label=m['live'], txt=LIVED), 14) + read(m['title'], m['sub'], size=30)
             + gut(f'<div style="margin-top: 16px;">{m["inst"](349)}</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 6px;">{m["facts"]}</div>')
             + '</div>')
    head = opener.replace('background: #EFEAE0', 'background: #EFEAE0', 1)
    return head + field + m['tail']() + '<div style="flex-grow: 1;"></div>' + TAB


# ---- B2 · the band carries the situation's own object ----------------------------------------------------
def band2(chip, time, sentence, artifact, prov='', tone=LIVE, chip_txt='#A9C49C', action=''):
    act = (f'<div style="min-height: 44px; background: {OX}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 12px;">'
           f'<span style="color: {CARD}; font-size: 15px; font-weight: 600;">{action}</span></div>') if action else ''
    pv = f'<div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.9px; color: rgba(251,247,236,0.5); margin-top: 10px;">{prov}</div>' if prov else ''
    return (f'<div style="margin: 14px 12px 0 12px; background: {INK}; border-radius: 22px; padding: 14px 14px 14px; color: {CARD}; --tk-ground: {INK};">'
            f'<div style="display: flex; align-items: center; padding: 0 2px;">{pulse(color=tone, label=chip, txt=chip_txt)}<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; color: rgba(251,247,236,0.55); letter-spacing: 0.8px;">{time}</span></div>'
            f'<div style="font-family: {SERIF}; font-size: 21px; line-height: 25px; font-weight: 600; margin: 8px 2px 12px;">{sentence}</div>'
            f'{artifact}{act}{pv}</div>')

def city_map():
    # a small seeded map: water, two streets, you, the flea, the pier, walking lines
    W, Hh = 341, 170
    svg = (f'<svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" style="display: block;">'
           f'<rect width="{W}" height="{Hh}" fill="#EFE8DA"/>'
           '<path d="M0 118 C60 110 110 128 170 122 C230 116 280 104 341 96 L341 170 L0 170 Z" fill="#BFD6DA"/>'
           '<path d="M0 118 C60 110 110 128 170 122 C230 116 280 104 341 96" stroke="#9DBFC6" stroke-width="1.5" fill="none"/>'
           '<path d="M40 0 L70 118 M150 0 L160 122 M0 40 L341 30 M250 0 L262 108" stroke="#D9D0BC" stroke-width="7" fill="none" stroke-linecap="round"/>'
           '<rect x="196" y="4" width="120" height="16" rx="3" fill="#D9D0BC" opacity="0.9"/>'
           '<path d="M112 70 C150 60 190 40 236 26" stroke="#1B1714" stroke-width="1.6" stroke-dasharray="3 4" fill="none"/>'
           '<path d="M112 70 C140 92 170 104 204 112" stroke="#1B1714" stroke-width="1.6" stroke-dasharray="3 4" fill="none"/>'
           '<circle cx="112" cy="70" r="16" fill="#6B8F5E" opacity="0.18"/><circle cx="112" cy="70" r="6" fill="#6B8F5E" stroke="#FBF7EC" stroke-width="2"/>'
           '<g><circle cx="238" cy="24" r="9" fill="#B0853A"/><text x="238" y="28" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#FBF7EC">1</text></g>'
           '<g><circle cx="206" cy="113" r="9" fill="#3D5066"/><text x="206" y="117" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#FBF7EC">2</text></g>'
           '<text x="184" y="64" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">6 MIN</text>'
           '<text x="146" y="101" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">9 MIN</text>'
           '<text x="92" y="74" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#4E6B43">YOU</text>'
           '<text x="20" y="160" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="1" fill="#3D5066">THE BAY</text></svg>')
    key = lambda n, c, t, s: (f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 8px 12px; border-top: 1px solid rgba(27,23,20,0.08);">'
                              f'<span style="width: 16px; height: 16px; border-radius: 8px; background: {c}; color: {CARD}; font-family: {MONO}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; flex: none;">{n}</span>'
                              f'<span style="font-size: 14px; color: {INK};">{t}</span><span style="margin-left: auto; font-family: {MONO}; font-size: 10px; letter-spacing: 0.8px; color: {MUTE};">{s}</span></div>')
    return (f'<div style="background: {CARD}; border-radius: 14px; overflow: hidden;">{svg}'
            + key('1', GOLD, 'The flea, under the bridge', 'UNTIL 3') + key('2', '#3D5066', 'The pier at low water', 'FROM 2:40') + '</div>')

def table_top():
    W, Hh = 341, 176
    seat = lambda cx, cy, letter, here, lab, lx, ly, anc: (
        (f'<circle cx="{cx}" cy="{cy}" r="17" fill="{"#1B1714" if here else "#FBF7EC"}" stroke="#1B1714" stroke-width="1.5" {"" if here else "stroke-dasharray=\"3 3\""}/>'
         f'<text x="{cx}" y="{cy + 4}" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="{"#FBF7EC" if here else "#1B1714"}">{letter}</text>'
         f'<text x="{lx}" y="{ly}" text-anchor="{anc}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.6" fill="#1B1714">{lab}</text>'))
    plate = lambda cx, cy, full: (f'<circle cx="{cx}" cy="{cy}" r="15" fill="#FBF7EC" stroke="#D9CDB4"/>'
                                  + (f'<ellipse cx="{cx}" cy="{cy}" rx="9" ry="7" fill="#E7C15A"/>' if full else ''))
    svg = (f'<svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" style="display: block;"><rect width="{W}" height="{Hh}" fill="#EFE8DA"/>'
           '<rect x="96" y="40" width="150" height="96" rx="14" fill="#C69A66"/><rect x="96" y="40" width="150" height="96" rx="14" fill="none" stroke="#A97E4E" stroke-width="1.5"/>'
           + plate(136, 70, True) + plate(206, 70, False) + plate(136, 106, False) + plate(206, 106, False)
           + '<rect x="166" y="80" width="10" height="18" rx="3" fill="#6E3B2E"/>'
           + seat(120, 22, 'N', True, 'HERE', 96, 26, 'end')
           + seat(222, 22, 'S', False, 'SAID ~7:30', 246, 26, 'start')
           + seat(136, 154, 'M', False, 'SAID 8:00', 112, 158, 'end')
           + seat(206, 154, '', False, '', 0, 0, 'start').replace('stroke-dasharray="3 3"', 'stroke-dasharray="3 3" opacity="0.35"')
           + '</svg>')
    foot = (f'<div style="display: flex; padding: 8px 12px; border-top: 1px solid rgba(27,23,20,0.08); font-family: {MONO}; font-size: 10px; letter-spacing: 0.8px; color: {MUTE};">'
            f'<span>FROM 7 &middot; AT YOURS</span><span style="margin-left: auto;">SAM GOES 9:00</span></div>')
    return f'<div style="background: {CARD}; border-radius: 14px; overflow: hidden;">{svg}{foot}</div>'

def ticket(props, h):
    return f'<dc-import name="Ticket" {props} hint-size="341px,{h}px"></dc-import>'
PASS = ('mode="flight" density="full" kicker="FLIGHT · TAP 214" date="TODAY" fromCode="JFK" fromName="New York" toCode="LIS" toName="Lisbon" '
        'fields="GATE=B22;BOARDS=18:05;SEAT=24A" barcode="yes"')
def P(*parts): return phone(*parts)
b2 = {
 'city': P(anchor('NEW YORK &middot; SATURDAY', '10:40 AM', ''),
           band2('HERE NOW &middot; RED HOOK', '10:40 AM', 'Two things in reach this afternoon.', city_map(), 'THE MARKET&rsquo;S NOTICE &middot; TIDE TABLE &middot; YOUR APPROXIMATE LOCATION'),
           M['city']['tail']()),
 'eve': P(anchor('NEW YORK &middot; SATURDAY', '7:25 PM'),
          band2('LIVE &middot; PASTA NIGHT', '7:25 PM', 'Sam around 7:30. Maya at eight.', table_top(), 'TIMES ARE THEIR OWN WORDS'),
          M['eve']['tail']()),
 'show': P(anchor('NEW YORK &middot; FRIDAY', '7:22 PM'),
           band2('LIVE &middot; THE HALL', '7:22 PM', 'Meeting Alex at the side door, 7:40.',
                 ticket('mode="admission" density="full" kicker="ADMISSION · THE HALL" date="FRIDAY" status="Tonight · doors 8" title="The Hall" sub="Set times posted at 6" fields="MEET=SIDE DOOR 7:40;WAY HOME=+25 MIN" band="ADMIT ONE|TONIGHT"', 230),
                 'SENT TO ALEX 7:21 &middot; WAITING TO REACH HIM'),
           sect('After the show') + gut(f'<div style="font-size: 15px; line-height: 20px;">The way home is a surface route</div><div style="font-size: 13px; color: {MUTE}; margin-top: 2px;">25 minutes longer after ten</div>')),
 'gate': P(anchor('JFK &middot; TERMINAL 4', '5:20 PM'),
           band2('LIVE &middot; TAP 214', '5:20 PM', 'Boarding at 6:05 from B22.', ticket(PASS + ' status="BOARDING 6:05 · 45 MIN"', 230), 'GATE FROM THE AIRLINE &middot; 5:18 PM'),
           M['gate']['tail']()),
 'rush': P(anchor('NEW YORK &middot; FRIDAY', '3:58 PM'),
           band2('URGENT &middot; TAP 214', '3:58 PM', 'The A is stopped. A car makes bag drop.', ticket(PASS + ' status="BAG DROP CLOSES 5:45"', 230),
                 'TRANSIT ALERT 3:51 &middot; DRIVING TIME 3:57', tone=OX, chip_txt='#E3A7A0', action='Open the way there'),
           gut(f'<div style="font-size: 13px; line-height: 18px; color: {MUTE};">The rest of Friday is still here &middot; Maya and Alex&rsquo;s 8:10 &middot; Lisbon on landing</div>', 14))}
def lane2():
    spec = [('city', 'NEW CITY &middot; 10:40 AM', 'A MAP', 'You, the flea and the pier, with the walk to each', 'Seeded map on the Places map tokens'),
            ('eve', 'EVENING &middot; 7:25 PM', 'THE TABLE', 'Who&rsquo;s at the table and who said when', 'Filled seat = here; dashed = their own time'),
            ('show', 'THE SHOW &middot; 7:22 PM', 'THE ADMISSION', 'The ticket carries the moved meeting point', 'Shared Ticket, admission'),
            ('gate', 'TRAVEL &middot; 5:20 PM', 'THE BOARDING PASS', 'The pass itself, with the gate from the airline', 'Shared Ticket, flight'),
            ('rush', 'TRAVEL &middot; 3:58 PM', 'THE PASS, URGENT', 'Same pass; the band turns oxblood and gains one action', 'The only urgent band')]
    cells = ''.join(cell(f'B+ &middot; {lbl}', f'B+{i + 1} &middot; {nm}', t, s, b2[k]) for i, (k, lbl, nm, t, s) in enumerate(spec))
    return (f'<div style="margin-top: 36px;"><div class="kick" style="font-size: 12px;">B+ &middot; THE BAND CARRIES THE THING ITSELF</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px; margin-top: 6px;">B&rsquo;s dark band, but instead of a timeline every time, it holds the object each situation already has: a map where you are, the table you are hosting, the ticket you are holding, the pass you are boarding with. The pulse and the band say live; the object says what kind.</div></div>'
            f'<div style="display: flex; gap: 40px; align-items: flex-start; margin-top: 22px;">{cells}</div>')


# ---- D · the object itself goes live: no container; a dark object with a green live stub --------------------
CR, CRM, CRL = '#FBF7EC', 'rgba(251,247,236,0.62)', 'rgba(251,247,236,0.16)'
def stub(label, right, tone=LIVE, txt='#A9C49C', barcode=False):
    bc = ('<span style="margin-left: 10px; width: 64px; height: 20px; flex: none; background: repeating-linear-gradient(90deg, #FBF7EC 0 2px, transparent 2px 3px, #FBF7EC 3px 4px, transparent 4px 6px, #FBF7EC 6px 9px, transparent 9px 10px);"></span>' if barcode else '')
    return (f'<div style="position: relative; border-top: 1.5px dashed {CRL}; margin: 0 14px;"><span style="position: absolute; left: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span>'
            f'<span style="position: absolute; right: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span></div>'
            f'<div style="display: flex; align-items: center; padding: 12px 18px 14px;">{pulse(color=tone, label=label, txt=txt)}'
            f'<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {CR};">{right}</span>{bc}</div>')
def dobj(inner, stubhtml, chamfer=False):
    clip = 'clip-path: polygon(0 0, calc(100% - 22px) 0, 100% 22px, 100% 100%, 0 100%);' if chamfer else ''
    return gut(f'<div style="background: {INK}; color: {CR}; border-radius: 18px; overflow: hidden; box-shadow: 0 14px 30px -14px rgba(27,23,20,0.55); {clip}">{inner}{stubhtml}</div>', 18)
def kick(l, r): return (f'<div style="display: flex; align-items: baseline;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {CRM};">{l}</span>'
                        f'<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; letter-spacing: 1px; color: {CRM};">{r}</span></div>')
def dfield(k, v): return (f'<div style="display: flex; flex-direction: column; gap: 3px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {CRM};">{k}</span>'
                          f'<span style="font-family: {MONO}; font-size: 15px; font-weight: 500; color: {CR};">{v}</span></div>')
def dpass(status, urgent=False):
    route = (f'<div style="display: flex; align-items: flex-end; gap: 12px; margin-top: 12px;"><div><div style="font-family: {SERIF}; font-size: 38px; line-height: 38px; font-weight: 600;">JFK</div><div style="font-size: 12px; color: {CRM}; margin-top: 4px;">New York</div></div>'
             f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="margin-bottom: 26px;"><path d="M2.5 9.5 L17.5 3 L12 17.5 L9.5 11 Z M9.5 11 L17.5 3" stroke="{CRM}" stroke-width="1.4" stroke-linejoin="round"/></svg>'
             f'<span style="flex: 1; height: 1px; background: {CRL}; margin-bottom: 36px;"></span>'
             f'<div style="text-align: right;"><div style="font-family: {SERIF}; font-size: 38px; line-height: 38px; font-weight: 600;">LIS</div><div style="font-size: 12px; color: {CRM}; margin-top: 4px;">Lisbon</div></div></div>')
    fields = f'<div style="display: flex; gap: 26px; margin-top: 16px;">{dfield("GATE", "B22")}{dfield("BOARDS", "18:05")}{dfield("SEAT", "24A")}</div>'
    inner = f'<div style="padding: 16px 18px 18px;">{kick("FLIGHT &middot; TAP 214", "TODAY")}{route}{fields}</div>'
    st = stub('URGENT', status, tone='#C0564A', txt='#E3A7A0', barcode=False) if urgent else stub('LIVE', status, barcode=True)
    if urgent: inner = inner.replace(f'background: {INK}', f'background: {INK}')
    return dobj(inner, st)
def dadmission():
    inner = (f'<div style="padding: 16px 18px 18px;">{kick("ADMISSION &middot; THE HALL", "FRIDAY")}'
             f'<div style="font-family: {SERIF}; font-size: 32px; line-height: 34px; font-weight: 600; margin-top: 12px;">The Hall</div>'
             f'<div style="font-size: 12.5px; color: {CRM}; margin-top: 4px;">Set times posted at 6</div>'
             f'<div style="display: flex; gap: 26px; margin-top: 16px;">{dfield("MEET", "SIDE DOOR 7:40")}{dfield("DOORS", "8:00")}</div></div>')
    return dobj(inner, stub('LIVE &middot; TONIGHT', 'ADMIT ONE'), chamfer=True)
def devening():
    def seat(l, state, note):
        here = state == 'here'
        c = (f'<span style="width: 40px; height: 40px; border-radius: 20px; display: inline-flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; '
             + (f'background: {CR}; color: {INK};">' if here else f'border: 1.5px dashed {CRM}; color: {CR};">') + f'{l}</span>')
        return (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px; width: 70px;">{c}'
                f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {CR if here else CRM};">{note}</span></div>')
    empty = (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px; width: 70px;"><span style="width: 40px; height: 40px; border-radius: 20px; border: 1.5px dashed {CRL};"></span>'
             f'<span style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.8px; color: {CRL};">&nbsp;</span></div>')
    inner = (f'<div style="padding: 16px 18px 18px;">{kick("PASTA NIGHT &middot; AT YOURS", "FROM 7")}'
             f'<div style="font-family: {SERIF}; font-size: 26px; line-height: 30px; font-weight: 600; margin-top: 12px;">Four at the table</div>'
             f'<div style="display: flex; justify-content: space-between; margin-top: 16px;">{seat("N", "here", "HERE")}{seat("S", "said", "~7:30")}{seat("M", "said", "8:00")}{empty}</div></div>')
    return dobj(inner, stub('LIVE &middot; TONIGHT', 'SAM GOES 9:00'))
def dmap():
    W, Hh = 349, 176
    svg = (f'<svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" style="display: block;">'
           f'<rect width="{W}" height="{Hh}" fill="{INK}"/>'
           '<path d="M0 124 C60 116 110 134 170 128 C230 122 290 110 349 102 L349 176 L0 176 Z" fill="#2B3D42"/>'
           '<path d="M40 0 L70 124 M150 0 L160 128 M0 44 L349 34 M252 0 L264 114" stroke="#3A342E" stroke-width="7" fill="none" stroke-linecap="round"/>'
           '<path d="M114 74 C150 64 192 44 238 30" stroke="#FBF7EC" stroke-opacity="0.7" stroke-width="1.5" stroke-dasharray="3 4" fill="none"/>'
           '<path d="M114 74 C142 96 172 108 206 116" stroke="#FBF7EC" stroke-opacity="0.7" stroke-width="1.5" stroke-dasharray="3 4" fill="none"/>'
           '<circle cx="114" cy="74" r="16" fill="#6B8F5E" opacity="0.3"/><circle cx="114" cy="74" r="6" fill="#6B8F5E" stroke="#1B1714" stroke-width="2"/>'
           '<circle cx="240" cy="28" r="9" fill="#B0853A"/><text x="240" y="32" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">1</text>'
           '<circle cx="208" cy="117" r="9" fill="#9DBFC6"/><text x="208" y="121" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">2</text>'
           '<text x="186" y="68" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#FBF7EC">6 MIN</text>'
           '<text x="146" y="104" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#FBF7EC">9 MIN</text>'
           '<text x="94" y="78" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#A9C49C">YOU</text></svg>')
    key = lambda n, c, t, r: (f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 9px 18px; border-top: 1px solid {CRL};">'
                              f'<span style="width: 16px; height: 16px; border-radius: 8px; background: {c}; color: {INK}; font-family: {MONO}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; flex: none;">{n}</span>'
                              f'<span style="font-size: 14px; color: {CR};">{t}</span><span style="margin-left: auto; font-family: {MONO}; font-size: 10px; letter-spacing: 0.8px; color: {CRM};">{r}</span></div>')
    inner = svg + key('1', GOLD, 'The flea, under the bridge', 'UNTIL 3') + key('2', '#9DBFC6', 'The pier at low water', 'FROM 2:40')
    return dobj(inner, stub('HERE NOW &middot; RED HOOK', '10:40 AM'))
GLY = {'bowl': 'M2 7.5h11a5.5 5.5 0 0 1-11 0zM5 5.5c0-1 1-1 1-2M8 5.5c0-1 1-1 1-2',
       'walk': 'M8 2.5a1 1 0 1 0 0 .01M7 5l-2 3 2 1v4M7 9l2 4M6 6l3 1 1 2', 'seat': 'M3 9h9v3M4 9V4h7v5M3 12v1.5M12 12v1.5',
       'leaf': 'M3 12c0-6 4-9 9-9 0 5-3 9-9 9zM3 12l5-5', 'plane': 'M1.5 9.5l12-6-4 9.5-2-3.5-6 0z', 'moon': 'M11 10.5A5 5 0 0 1 5.5 3a5 5 0 1 0 5.5 7.5z'}
def companion(head, items):
    def it(g, title, fit, door=''):
        d = f'<span class="vdl-door vk-t-bodySmMedium" style="margin-top: 4px;">{door}</span>' if door else ''
        return (f'<div style="display: flex; gap: 12px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.08);">'
                f'<svg width="16" height="16" viewBox="0 0 15 15" fill="none" style="flex: none; margin-top: 2px;"><path d="{GLY[g]}" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><div style="font-size: 15px; line-height: 20px;">{title}</div>'
                f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {LIVED}; margin-top: 4px;">{fit}</div>{d}</div></div>')
    return gut(f'<div style="margin: 0 10px; background: {CARD}; border-radius: 0 0 16px 16px; padding: 10px 16px 4px; box-shadow: 0 6px 16px -12px rgba(27,23,20,0.35);">'
               f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE}; padding-bottom: 8px;">{head}</div>'
               + ''.join(it(*x) for x in items) + '</div>')
def pageline(t): return gut(f'<div style="font-size: 13px; line-height: 18px; color: {MUTE};">{t}</div>', 12)
cta = lambda t: gut(f'<div style="min-height: 44px; background: #4A3428; border-radius: 12px; display: flex; align-items: center; justify-content: center;"><span style="color: {CARD}; font-size: 15px; font-weight: 600;">{t}</span></div>', 14)
d = {
 'city': phone(anchor('NEW YORK &middot; SATURDAY', '10:40 AM', ''), read('Two things in reach this afternoon.', size=26), dmap(),
               companion('AT THE FLEA', [('bowl', 'Lunch there: the pierogi table, at the bridge end', 'AT THE FLEA &middot; TILL IT SELLS OUT'),
                                        ('seat', 'A bench on the water between the two', 'ON THE WAY TO THE PIER &middot; 4 MIN')]),
               M['city']['tail']()),
 'eve': phone(anchor('NEW YORK &middot; SATURDAY', '7:25 PM'), read('Sam around 7:30. Maya at eight.', size=26), devening(),
              companion('BEFORE THEY ARRIVE', [('leaf', 'Dana: fry the zucchini first, twenty minutes', 'DANA &middot; FRI &middot; THERE&rsquo;S TIME BEFORE 7:30'),
                                               ('moon', 'Sam goes at nine: dessert before he leaves', 'MAYA IS BRINGING IT &middot; 8:00')])),
 'show': phone(anchor('NEW YORK &middot; FRIDAY', '7:22 PM'), read('Meeting Alex at the side door, 7:40.', size=26), dadmission(),
               companion('AFTER THE SHOW', [('bowl', 'The noodle bar Maya sent, open till one', '6 MIN FROM THE HALL &middot; MAYA&rsquo;S PICK', 'Maya&rsquo;s note'),
                                           ('walk', 'The way home is a surface route', '25 MIN LONGER AFTER TEN')]),
               pageline('Sent to Alex 7:21 &middot; waiting to reach him.')),
 'gate': phone(anchor('JFK &middot; TERMINAL 4', '5:20 PM'), read('Boarding at 6:05 from B22.', size=26), dpass('BOARDS 6:05 &middot; 45 MIN'),
               companion('BEFORE BOARDING &middot; 45 MIN', [('bowl', 'A noodle counter by B18', '3 MIN &middot; FITS BEFORE 6:05'),
                                                           ('plane', 'Maya and Alex&rsquo;s 8:10, on time', 'THEY LAND 9:25 &middot; MEET AT THE STAY')]),
               M['gate']['tail']()),
 'rush': phone(anchor('NEW YORK &middot; FRIDAY', '3:58 PM'), read('The A is stopped. A car makes bag drop.', size=26), dpass('BAG DROP 5:45', urgent=True),
               cta('Open the way there'), pageline('Transit alert 3:51 &middot; driving time 3:57 &middot; the rest of Friday is below'))}
def laneD():
    spec = [('city', 'NEW CITY &middot; 10:40 AM', 'THE MAP, LIVE', 'The map itself turns dark, with you pulsing on it', 'Seeded map &middot; kernel map tokens on ink'),
            ('eve', 'EVENING &middot; 7:25 PM', 'THE TABLE, LIVE', 'Four seats: one here, two by their own word, one open', 'Filled = here &middot; dashed = the time they gave'),
            ('show', 'THE SHOW &middot; 7:22 PM', 'THE ADMISSION, LIVE', 'The ticket carries the moved meeting point', 'Chamfered admission anatomy, dark'),
            ('gate', 'TRAVEL &middot; 5:20 PM', 'THE PASS, LIVE', 'The boarding pass is the crown; its stub pulses', 'Pass anatomy from 08 &middot; the noodle counter is a fixture'),
            ('rush', 'TRAVEL &middot; 3:58 PM', 'THE PASS, URGENT', 'Same pass, oxblood stub, one action &mdash; and no companion', 'Nothing competes with the action')]
    cells = ''.join(cell(f'D &middot; {lbl}', f'D{i + 1} &middot; {nm}', t, s, d[k]) for i, (k, lbl, nm, t, s) in enumerate(spec))
    return (f'<div style="margin-top: 36px;"><div class="kick" style="font-size: 12px;">D &middot; THE OBJECT ITSELF GOES LIVE</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px; margin-top: 6px;">Under each live object, a companion tray: one or two things that help around this moment, each with its fit (how far, open till when, fits before boarding). It retires with the object, and in the rush it is absent. No container. The situation&rsquo;s own object sits on the page as the crown, drawn dark while it is live, with a torn-off stub that carries the pulse. Urgent turns the stub oxblood. When the live window ends the object returns to its ordinary cream and moves down the page.</div></div>'
            f'<div style="display: flex; gap: 40px; align-items: flex-start; margin-top: 22px;">{cells}</div>')

def lane(tag, name, desc, fnc, note):
    cells = ''.join(cell(f'{tag} &middot; {lbl}', f'{tag}{i + 1} &middot; {nm}', t, s, fnc(k)) for i, (k, lbl, nm, t, s) in enumerate([
        ('city', 'NEW CITY &middot; 10:40 AM', 'THE AFTERNOON HERE', 'The flea until three, low water from 2:40', 'Board 19&rsquo;s moment'),
        ('eve', 'EVENING &middot; 7:25 PM', 'THE GATHERING', 'From seven, arrivals in their own words', 'Board 20&rsquo;s moment'),
        ('gate', 'TRAVEL &middot; 5:20 PM', 'THE JOURNEY', 'Where she is between home and Lisbon', 'Board 21&rsquo;s moment')]))
    return (f'<div style="margin-top: 50px;"><div class="kick" style="font-size: 12px;">{name}</div><div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px; margin-top: 6px;">{desc}</div></div>'
            f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 22px;">{cells}{notes(note, 440)}</div>')

body = (laneD() + lane2() + lane('A', 'A &middot; A LIVE INSTRUMENT CROWN', 'The read stays; the crown becomes an instrument with a now-line, a pulsing live chip and a green edge. Elevated above everything else on the page.', A,
             [('WHAT SAYS LIVE', 'The pulse, the green ring and the now-line moving along the afternoon. The instrument carries the facts, so the prose gets shorter.'),
              ('RISK', 'The quietest of the three; at a glance it is still a card, only a stronger one.')])
        + lane('B', 'B &middot; A LIVE BAND', 'A dark capsule under the anchor, like a Live Activity: live chip, the one live sentence, a light instrument. Home continues on paper beneath it.', B,
               [('WHAT SAYS LIVE', 'The only dark object on a paper page, pinned at the top. It reads as a system state, the way a ride or a delivery does, and can compact to a single line while scrolling.'),
                ('RISK', 'Dark bands are the strongest signal in the kernel; they must disappear the moment nothing is live, or Home turns into a dashboard.')])
        + lane('C', 'C &middot; A LIVE FIELD', 'The head of Home changes key: a green wash under the anchor, the read and a full-width instrument. Below it, the ordinary page.', C,
               [('WHAT SAYS LIVE', 'The whole top of the page is a different colour for the length of the situation. Nothing needs to be read to know.'),
                ('RISK', 'The loudest: green is new to Home&rsquo;s paper. Urgent would swap the wash for oxblood, so the two must stay clearly apart.')])
        + f'<div style="margin-top: 50px; max-width: 1200px;"><div class="kickm">RECOMMENDATION</div><div style="font-size: 14px; line-height: 21px; color: #2C2622; margin-top: 8px;">'
          'B for the travel day and the evening, where something is genuinely underway and a glanceable state helps; A for the new city, where nothing is underway and a band would overclaim. '
          'All three use the kernel&rsquo;s own live colour (state.live, #6B8F5E) and one axis grammar: spans for windows, filled marks for set times, dashed marks for what people said, a green now-line. Urgent keeps oxblood.</div></div>')

css_extra = ('.pulse { position: relative; width: 8px; height: 8px; border-radius: 4px; background: var(--pc); flex: none; }\n'
             '    .pulse::after { content: ""; position: absolute; inset: -4px; border-radius: 8px; border: 1.5px solid var(--pc); animation: pl 1.6s ease-out infinite; }\n'
             '    @keyframes pl { 0% { transform: scale(0.6); opacity: 0.9; } 100% { transform: scale(1.6); opacity: 0; } }')
CSS = ('.fn { font-family: ' + MONO + '; font-size: 10px; letter-spacing: 0.9px; color: #B5AFA5; }\n'
       '    .kick { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #8A6628; }\n'
       '    .kickm { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead { display: flex; align-items: center; gap: 10px; font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }\n'
       '    .row { display: flex; align-items: center; gap: 12px; min-height: 44px; }\n    .chev { flex: none; }\n    ' + css_extra)
head = ('<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kick">VESPER &middot; HOME &middot; 22 &middot; MAKING LIVE VISIBLE &middot; EXPLORATION &middot; 2026-09-23</div>'
        f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px;">22 &middot; How Home shows that something is live</div>'
        f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px;">Three treatments of the same three moments from 19, 20 and 21, for a choice before those boards are rebuilt. Each makes the live state visible before anything is read, instead of leaving it to a regular card.</div></div>')
root = (f'<div style="width: 2280px; min-height: 4444px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; font-family: {SANS}; color: {INK}; display: flex; flex-direction: column;">'
        + head + body + '<div class="fn" style="margin-top: 30px;">EVERY PERSON, PLACE AND TIME IS A DESIGN FIXTURE &middot; THE PULSE ANIMATES IN THE BROWSER</div></div>')
out = ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
       '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;700&display=swap">\n'
       f'  <link rel="stylesheet" href="{G.KERNEL}">\n  <link rel="stylesheet" href="vdl.css">\n  <style>\n    body {{ margin: 0; }}\n    {CSS}\n  </style>\n</helmet>\n' + root + '\n</x-dc>\n</body>\n</html>\n')
open(f'{OUT}/22 - Live - Making Live Visible.dc.html', 'w').write(out); print('wrote 22', len(out))

# ============================== 23 · The companion tray, five ways ==============================================
TI = {'gate': ('BEFORE BOARDING &middot; 45 MIN', [('bowl', 'A noodle counter by B18', '3 min', 'FITS BEFORE 6:05'),
                                                  ('plane', 'Maya and Alex&rsquo;s 8:10, on time', '9:25', 'THEY LAND &middot; MEET AT THE STAY')]),
      'show': ('AFTER THE SHOW', [('bowl', 'The noodle bar Maya sent', '6 min', 'OPEN TILL 1 &middot; MAYA&rsquo;S PICK'),
                                   ('walk', 'The way home is a surface route', '+25', 'MIN AFTER TEN')])}
def g16(k, col=INK): return f'<svg width="16" height="16" viewBox="0 0 15 15" fill="none" style="flex: none;"><path d="{GLY[k]}" stroke="{col}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def obj_only(k, extra_stub=''):
    if k == 'gate':
        return dpass('BOARDS 6:05 &middot; 45 MIN') if not extra_stub else None
    return dadmission()
# T1 drawer — as lane D
def t1(k):
    head, items = TI[k]
    return companion(head, [(g, t, f'{b.upper()} &middot; {s}') for g, t, b, s in items])
# T2 coupon — the tray is part of the object, below a second perforation
def t2_object(k):
    head, items = TI[k]
    rows = ''.join(f'<div style="display: flex; gap: 12px; align-items: baseline; padding: 10px 0; border-top: 1px solid {CRL};">{g16(g, CRM)}'
                   f'<div style="flex: 1;"><div style="font-size: 15px; line-height: 20px; color: {CR};">{t}</div>'
                   f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: #A9C49C; margin-top: 3px;">{b.upper()} &middot; {s}</div></div></div>' for g, t, b, s in items)
    coupon = (f'<div style="position: relative; border-top: 1.5px dashed {CRL}; margin: 0 14px;"><span style="position: absolute; left: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span>'
              f'<span style="position: absolute; right: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span></div>'
              f'<div style="padding: 12px 18px 8px;"><div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {CRM}; padding-bottom: 6px;">{head}</div>{rows}</div>')
    if k == 'gate':
        base = dpass('BOARDS 6:05 &middot; 45 MIN')
    else:
        base = dadmission()
    # insert the coupon before the closing of the dark object (dobj ends with '</div></div>')
    i = base.rfind('</div></div>')
    return base[:i] + coupon + base[i:]
# T3 two cards side by side
def t3(k):
    head, items = TI[k]
    card = lambda g, t, b, s: (f'<div style="flex: 1; min-width: 0; background: {CARD}; border-radius: 14px; padding: 12px 12px 14px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                               f'<div style="display: flex; align-items: center; gap: 6px;">{g16(g, MUTE)}<span style="margin-left: auto; width: 6px; height: 6px; border-radius: 3px; background: {LIVE};"></span></div>'
                               f'<div style="font-family: {SERIF}; font-size: 28px; line-height: 30px; font-weight: 600; margin-top: 10px;">{b}</div>'
                               f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {LIVED}; margin-top: 2px;">{s}</div>'
                               f'<div style="font-size: 14px; line-height: 19px; margin-top: 10px;">{t}</div></div>')
    return gut(f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE}; margin: 4px 0 10px;">{head}</div>'
               f'<div style="display: flex; gap: 10px;">' + ''.join(card(*x) for x in items) + '</div>', 16)
# T4 leader lines hanging from the live stub
def t4(k):
    head, items = TI[k]
    node = lambda g, t, b, s, last: (f'<div style="position: relative; padding: 0 0 {0 if last else 18}px 30px;">'
                                     f'<span style="position: absolute; left: 3px; top: 7px; width: 9px; height: 9px; border-radius: 5px; background: {PAPER}; border: 2px solid {LIVE};"></span>'
                                     f'<div style="font-size: 15px; line-height: 20px;">{t}</div>'
                                     f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {LIVED}; margin-top: 3px;">{b.upper()} &middot; {s}</div></div>')
    return gut(f'<div style="position: relative; margin: 0 0 0 26px; padding-top: 16px;">'
               f'<span style="position: absolute; left: 7px; top: 0; bottom: 8px; width: 2px; background: linear-gradient({LIVE}, rgba(107,143,94,0.25));"></span>'
               f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {LIVED}; padding: 0 0 12px 30px;">{head}</div>'
               + ''.join(node(*x, i == len(items) - 1) for i, x in enumerate(items)) + '</div>')
# T5 big numbers, magazine
def t5(k):
    head, items = TI[k]
    row = lambda g, t, b, s, first: (f'<div style="display: flex; gap: 14px; align-items: baseline; padding: 12px 0; {"" if first else "border-top: 1px solid rgba(27,23,20,0.08);"}">'
                                     f'<div style="width: 78px; flex: none; font-family: {SERIF}; font-size: 32px; line-height: 32px; font-weight: 600; letter-spacing: -0.02em;">{b}</div>'
                                     f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px;">{t}</div>'
                                     f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {MUTE}; margin-top: 3px;">{s}</div></div></div>')
    return gut(f'<div style="display: flex; align-items: center; gap: 12px; margin: 18px 0 2px;"><span style="font-size: 13px; font-weight: 600;">{head.split(" &middot; ")[0].capitalize()}</span>'
               f'<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div>'
               + ''.join(row(*x, i == 0) for i, x in enumerate(items)))
HEADS = {'gate': (anchor('JFK &middot; TERMINAL 4', '5:20 PM'), read('Boarding at 6:05 from B22.', size=26)),
         'show': (anchor('NEW YORK &middot; FRIDAY', '7:22 PM'), read('Meeting Alex at the side door, 7:40.', size=26))}
def tray_phone(k, v):
    a, r = HEADS[k]
    if v == 2: return phone(a, r, t2_object(k))
    obj = dpass('BOARDS 6:05 &middot; 45 MIN') if k == 'gate' else dadmission()
    return phone(a, r, obj, {1: t1, 3: t3, 4: t4, 5: t5}[v](k))
TV = [(1, 'T1 &middot; DRAWER', 'A cream drawer pulled from under the object', 'Lane D as drawn'),
      (2, 'T2 &middot; COUPON', 'A second tear-off, part of the ticket itself', 'The object grows; nothing sits outside it'),
      (3, 'T3 &middot; TWO CARDS', 'Two small cards, each led by its fit', 'Widget-like; glanceable'),
      (4, 'T4 &middot; LEADER LINES', 'A green line drops from the live stub', 'No box; items hang off the live state'),
      (5, 'T5 &middot; BIG NUMBERS', 'The fit set large, the thing beside it', 'Editorial; no box')]
def trow(k, label):
    cells = ''.join(cell(f'{label}', n, t, s, tray_phone(k, v)) for v, n, t, s in TV)
    return f'<div style="display: flex; gap: 40px; align-items: flex-start; margin-top: 26px;">{cells}</div>'
body23 = (trow('gate', 'AT THE GATE &middot; 5:20 PM')
          + '<div style="margin-top: 44px; border-top: 1px solid rgba(27,23,20,0.12);"></div>'
          + trow('show', 'THE SHOW &middot; 7:22 PM')
          + f'<div style="display: flex; gap: 40px; margin-top: 40px;">' + notes([
              ('T1 DRAWER', 'Clearly secondary to the object and easy to scan. Reads as a separate panel, so the page gains one more box.'),
              ('T2 COUPON', 'The most ticket-like: the help belongs to the thing you are holding, and it tears off with it when the window ends. Needs an object with a stub; the map and the table would have to grow one.'),
              ('T3 TWO CARDS', 'The fastest to glance: the number is the first thing you see. Two cards is the limit; a third turns it into a shelf.')], 560)
          + notes([('T4 LEADER LINES', 'The lightest: help hangs off the live state rather than sitting in a container, and the green line says it belongs to the live moment. Can look like a timeline if items are times.'),
                   ('T5 BIG NUMBERS', 'The most Vesper: serif numbers carry the fit, mono carries the source, no box at all. Loses the visual tie to the object unless it sits right under it.')], 560)
          + '</div>')
head23 = ('<div style="display: flex; flex-direction: column; gap: 8px;"><div class="kick">VESPER &middot; HOME &middot; 23 &middot; THE COMPANION TRAY &middot; EXPLORATION &middot; 2026-09-23</div>'
          f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px;">23 &middot; What sits under a live object, five ways</div>'
          f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px;">The same two items under the same live object (22 lane D), drawn five ways, at the gate and after the show. Only the tray changes.</div></div>')
root23 = (f'<div style="width: 2260px; min-height: 2004px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; font-family: {SANS}; color: {INK}; display: flex; flex-direction: column;">'
          + head23 + body23 + '<div class="fn" style="margin-top: 30px;">EVERY PERSON, PLACE AND TIME IS A DESIGN FIXTURE &middot; THE NOODLE COUNTER AT THE AIRPORT IS INVENTED</div></div>')
out23 = out.replace(out[out.index('<div style="width: 2280px'):out.rindex('\n</x-dc>')], root23)
open(f'{OUT}/23 - Live - The Companion Tray.dc.html', 'w').write(out23); print('wrote 23', len(out23))

# ============================== 23 lane · T2 colour variations =================================================
PALS = [  # name, object bg, coupon bg, coupon is light?, pulse colour, pulse text, note
 ('INK / INK', INK, INK, False, LIVE, '#A9C49C', 'One stock. The coupon is only separated by the tear.'),
 ('INK / TONAL STEP', INK, '#2E2824', False, LIVE, '#A9C49C', 'The coupon one step lighter: part of the ticket, visibly the tear-off.'),
 ('INK / CREAM', INK, CARD, True, LIVE, '#A9C49C', 'Two stocks: the ticket dark, the coupon paper, like a stub printed on cream card.'),
 ('INK / LIVE GREEN', INK, '#26321F', False, LIVE, '#A9C49C', 'The coupon carries the live colour: the helpful part is the live part.'),
 ('INK / UMBER', INK, '#3B2A20', False, LIVE, '#A9C49C', 'The action brown as coupon stock: warm, and ties to Home&rsquo;s one solid action.'),
 ('ALL UMBER', '#35261D', '#453226', False, LIVE, '#A9C49C', 'A warmer live skin overall; less stark than ink on paper.'),
 ('ALL DEEP GREEN', '#1F2A1B', '#2A3824', False, '#8DB57C', '#B5D3A6', 'The whole object is the live colour; nothing else on Home is green.')]
def coupon_html(k, cbg, light):
    head, items = TI[k]
    tx, tm, tl, fit = (INK, MUTE, 'rgba(27,23,20,0.10)', LIVED) if light else (CR, CRM, CRL, '#A9C49C')
    rows = ''.join(f'<div style="display: flex; gap: 12px; align-items: baseline; padding: 10px 0; border-top: 1px solid {tl};">{g16(g, tm)}'
                   f'<div style="flex: 1;"><div style="font-size: 15px; line-height: 20px; color: {tx};">{t}</div>'
                   f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {fit}; margin-top: 3px;">{b.upper()} &middot; {s}</div></div></div>' for g, t, b, s in items)
    perf = 'rgba(27,23,20,0.25)' if light else CRL
    return (f'<div style="background: {cbg}; position: relative;"><div style="position: relative; border-top: 1.5px dashed {perf}; margin: 0 14px;">'
            f'<span style="position: absolute; left: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span>'
            f'<span style="position: absolute; right: -24px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER};"></span></div>'
            f'<div style="padding: 12px 18px 8px;"><div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {tm}; padding-bottom: 6px;">{head}</div>{rows}</div></div>')
def t2_pal(k, obg, cbg, light, pc, pt):
    base = dpass('BOARDS 6:05 &middot; 45 MIN') if k == 'gate' else dadmission()
    base = base.replace(f'background: {INK}; color: {CR}; border-radius: 18px', f'background: {obg}; color: {CR}; border-radius: 18px')
    base = base.replace(f'--pc: {LIVE};', f'--pc: {pc};').replace('color: #A9C49C;">LIVE', f'color: {pt};">LIVE')
    i = base.rfind('</div></div>')
    return base[:i] + coupon_html(k, cbg, light) + base[i:]
def spec(k, pal):
    name, obg, cbg, light, pc, pt, note = pal
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;">'
            f'<div class="kick" style="padding: 0 0 8px 2px;">{name}</div>'
            f'<div style="background: {PAPER}; border-radius: 18px; padding: 4px 0 22px;">{t2_pal(k, obg, cbg, light, pc, pt)}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px; max-width: 380px;">{note if k == "gate" else ""}</div></div>')
lane_col = ('<div style="margin-top: 10px;"><div class="kick" style="font-size: 12px;">T2 &middot; SEVEN COLOURWAYS</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px; margin-top: 6px;">The coupon structure fixed; only the ticket and coupon stock change. Gate above, the show below, on Home&rsquo;s page paper.</div></div>'
            + '<div style="display: flex; gap: 32px; align-items: flex-start; margin-top: 22px;">' + ''.join(spec('gate', p) for p in PALS) + '</div>'
            + '<div style="display: flex; gap: 32px; align-items: flex-start; margin-top: 30px;">' + ''.join(spec('show', p) for p in PALS) + '</div>'
            + '<div style="margin-top: 44px; border-top: 1px solid rgba(27,23,20,0.12);"></div>')
root23b = root23.replace(head23, head23 + lane_col).replace('width: 2260px; min-height: 2004px', 'width: 3050px; min-height: 3065px')
out23b = out.replace(out[out.index('<div style="width: 2280px'):out.rindex('\n</x-dc>')], root23b)
open(f'{OUT}/23 - Live - The Companion Tray.dc.html', 'w').write(out23b); print('wrote 23 with colourways', len(out23b))
