"""Boards 19-21 — Live Home (September 23 research and additive assignment).
Three connected studies in the existing Home project: 19 a new city with no plan (a sparse-context visitor),
20 an evening together (host / arrived guest / late joiner / contribute-once, plus a show variation), 21 a travel day
(preparation, a genuine rush, comfortable waiting, weak connectivity, arrival).
Fixtures reuse existing Home and shared worlds: 14's newcomer supply around the pier; the shared fixture ledger's pasta night
(§1, §3, §9.3); 08/09/12's show at The Hall and TAP 214 to Lisbon. Copy: product copy and people's words inside the phones,
provenance as source · when; every reason outside the phone.
Usage: python3 gen_live.py <in_dir holding 12 and 00> <out_dir>
"""
import sys, os, re
IN, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], IN, OUT]
import gen_vdl as G

MONO, SERIF, SANS, CHEV = G.MONO, G.SERIF, G.SANS, G.CHEV
INK, INK2, MUTE, HINT, GOLD, CARD, PAPER, OX = '#1B1714', '#2C2622', '#6E6862', '#8F877C', '#B0853A', '#FBF7EC', '#EFEAE0', '#7A2E2E'
fn, cell, notes, gold, ink = G.fn, G.cell, G.notes, G.gold_door, G.ink_door
opener, TAB = G.home_parts()
chat_head, chat_tail = G.chat_parts()
LIFT = 'box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07)'

def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'
def anchor(place, time, who='N'):
    av = (f'<span style="width: 24px; height: 24px; border-radius: 999px; background: #4A3428; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">{who}</span>' if who else '')
    return (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">'
            f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">{place}</span>'
            f'<span class="fn" style="margin-left: auto;">{time}</span>{av}</div></div>')
def read(title, sub='', size=30):
    lh = {30: 34, 22: 27, 17: 23}[size]
    s = f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div>' if sub else ''
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: {size}px; line-height: {lh}px; letter-spacing: -0.01em; text-wrap: balance;">{title}</div>{s}</div>')
def sect(name, top=36):
    return (f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;">'
            f'<span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{name}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
def unit(title, body='', meta='', extra='', top=0):
    b = f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{body}</div>' if body else ''
    m = fn(meta, mt=6) if meta else ''
    return gut(f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK}; text-wrap: balance;">{title}</div>{b}{m}{extra}', top)
GL = {'hall': 'M2.4 12.6 V5.4 Q7.5 1.4 12.6 5.4 V12.6 M5.4 12.6 V8.6 Q7.5 6.6 9.6 8.6 V12.6 M1.4 12.6 H13.6',
      'plane': 'M1.5 9.5l12-6-4 9.5-2-3.5-6 0z', 'msg': 'M2 4.5h11v6H6l-3 2.5V4.5z', 'fork': 'M5 1.8 V6 M7.5 1.8 V6 M10 1.8 V6 M5 6 Q7.5 7.6 10 6 M7.5 6.8 V13.2',
      'key': 'M5 9.5a3 3 0 1 1 2.6-4.5H13v2h-1.5v1.5H10V7H7.6A3 3 0 0 1 5 9.5z', 'walk': 'M8 2.5a1 1 0 1 0 0 .01M7 5l-2 3 2 1v4M7 9l2 4M6 6l3 1 1 2',
      'tram': 'M4 3h7v7H4zM4 7h7M6 12l-1 1.5M9 12l1 1.5M7.5 1v2', 'ticket': 'M2 4h11v2.2a1.3 1.3 0 0 0 0 2.6V11H2V8.8a1.3 1.3 0 0 0 0-2.6z',
      'bell': 'M4 10V7a3.5 3.5 0 0 1 7 0v3l1 1.2H3zM6.2 12.4a1.4 1.4 0 0 0 2.6 0', 'pin': 'M7.5 13s4-3.6 4-7a4 4 0 0 0-8 0c0 3.4 4 7 4 7z',
      'water': 'M1.5 6q1.5-1.5 3 0t3 0 3 0 3 0M1.5 10q1.5-1.5 3 0t3 0 3 0 3 0', 'book': 'M3 2.5h8v10H3zM5 2.5v10'}
def glyph(k, op='0.62'):
    return f'<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex: none; opacity: {op}; margin-top: 3px;"><path d="{GL[k]}" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def face(letters, size=26):
    out = '<span style="display: inline-flex; align-items: center; flex: none; padding-top: 1px;">'
    for i, l in enumerate(letters):
        bg = '#4A3428' if l == 'N' else INK
        out += (f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {bg}; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {PAPER}; margin-left: {0 if i == 0 else -8}px;">{l}</span>')
    return out + '</span>'
def row(mark, text, sub='', last=False, chev=True, meta=''):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    s = f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{sub}</div>' if sub else ''
    m = fn(meta, mt=4) if meta else ''
    c = f'<span style="padding-top: 3px;">{CHEV}</span>' if chev else ''
    return (f'<div class="row" style="padding: 10px 0; align-items: flex-start;{b}">{mark}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 15px; line-height: 20px; color: {INK};">{text}</div>{s}{m}</div>{c}</div>')
def rows(*rs): return gut('<div style="border-top: 1px solid rgba(27,23,20,0.10);">' + ''.join(rs) + '</div>')
def card(inner, top=20, pad='16px 18px'):
    return gut(f'<div style="background: {CARD}; border-radius: 16px; {LIFT}; padding: {pad};">{inner}</div>', top)
def ctitle(t, size=20): return f'<div style="font-family: {SERIF}; font-weight: 600; font-size: {size}px; line-height: {size + 4}px; text-wrap: balance;">{t}</div>'
def cbody(t, mt=6): return f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: {mt}px;">{t}</div>'
def orline(): return f'<div style="display: flex; align-items: center; gap: 10px; margin: 12px 0;"><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.10);"></span><span class="fn" style="color: {HINT};">OR</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.10);"></span></div>'
def said(initial, name, when, words, bg=INK):
    return (f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {bg}; color: {CARD}; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">{initial}</span>'
            f'<span style="font-size: 13px; font-weight: 600;">{name}</span><span class="fn" style="color: {HINT};">{when}</span></div>'
            f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 23px; color: {INK}; margin-top: 8px;">{words}</div>')
def week(days, line):
    def d(k, sub='', on=False, mark=False):
        mk = f'background: {INK};' if on else (f'background: {GOLD};' if mark else 'border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;')
        return (f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 8px 0 6px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {INK if on else HINT};">{k}</span>'
                f'<span style="width: 7px; height: 7px; border-radius: 4px; {mk}"></span><span style="font-size: 10px; color: {MUTE if sub else "transparent"};">{sub or "."}</span></div>')
    return ('<div style="margin: 36px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">'
            + ''.join(d(*x) for x in days) + '</div></div>'
            + f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">{line}</div></div>')
def phone(*parts): return opener + ''.join(parts) + '<div style="flex-grow: 1;"></div>' + TAB
def chat(time, *parts):
    return chat_head.replace('SUNDAY 9:12 AM', time) + ''.join(parts) + chat_tail
def you(t): return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: #4A3428; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div></div>'
def vesper(t, prov=''):
    return (f'<div style="padding: 18px 22px 0 22px;"><div style="max-width: 330px;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: {INK};">{t}</div>'
            + (fn(prov, mt=8) if prov else '') + '</div></div>')
def ctx(label): return (f'<div style="padding: 26px 22px 0 22px;"><div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid rgba(27,23,20,0.10); background: {CARD}; border-radius: 12px; padding: 8px 12px;">'
                        f'<span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px;">{label}</span></div></div>')
def field(t): return f'<div style="padding: 30px 22px 0 22px;"><div style="display: flex; align-items: center; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: #B5AFA5;">{t}</span></div></div>'
def notice(tone, title, body='', primary='', h=64):
    a = f' body="{body}"' if body else ''
    b = f' primary="{primary}"' if primary else ''
    return f'<dc-import name="Notice" tone="{tone}" title="{title}"{a}{b} hint-size="349px,{h}px"></dc-import>'
def larger(h, k=1.3):
    return re.sub(r'(font-size|line-height): ([\d.]+)px', lambda m: f'{m.group(1)}: {float(m.group(2)) * k:.1f}px', h)
def rowwrap(*cells, first=False):
    st = ' margin-top: 26px;' if first else ' margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);'
    return f'<div style="display: flex; gap: 46px; align-items: flex-start;{st}">' + ''.join(cells) + '</div>'
def band(t, sub):
    return (f'<div style="margin-top: 50px;"><div class="kick" style="font-size: 11px;">{t}</div>'
            f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 1100px; margin-top: 6px;">{sub}</div></div>')
def table(heads, rs, minw=1500):
    th = ''.join(f'<th style="text-align: left; font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; padding: 0 12px 6px 0; border-bottom: 1px solid rgba(27,23,20,0.12);">{h}</th>' for h in heads)
    out = f'<div style="overflow-x: auto; margin-top: 10px;"><table style="border-collapse: collapse; min-width: {minw}px;"><tr>{th}</tr>'
    for r in rs:
        out += '<tr>' + ''.join(f'<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 12px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">{c}</td>' for c in r) + '</tr>'
    return out + '</table></div>'
CSS = ('.fn { font-family: ' + MONO + '; font-size: 10px; letter-spacing: 0.9px; color: #B5AFA5; }\n'
       '    .kick { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #8A6628; }\n'
       '    .kickm { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead { display: flex; align-items: center; gap: 10px; font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }\n'
       '    .row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); }\n'
       '    .row:first-child { border-top: none; }\n    .chev { flex: none; }\n'
       '    .lt .vdl-t-excerpt { font-size: 23.4px; line-height: 32.5px; }\n    .lt .vdl-t-sectionHeading, .lt .vk-t-bodySmMedium { font-size: 16.9px; }\n'
       '    .lt .vdl-t-metaLine { font-size: 13px; }\n    .lt .vdl-t-placeName { font-size: 20.8px; line-height: 26px; }')
def board(num, title, kicker, intro, body, width, height):
    head = (f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px;"><div class="kick">{kicker}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">{title}</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px;">{intro}</div></div>')
    root = (f'<div style="width: {width}px; min-height: {height}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; font-family: {SANS}; color: {INK}; display: flex; flex-direction: column;">'
            + head + body + '<div class="fn" style="margin-top: 30px; line-height: 16px;">EVERY PERSON, PLACE, TIME AND WORLD FACT IS A DESIGN FIXTURE &middot; REASONS STAY OUTSIDE THE PHONE &middot; A STATIC FRAME PROVES NO LIVE, PROVIDER OR NATIVE BEHAVIOUR</div></div>')
    return ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;700&display=swap">\n'
            f'  <link rel="stylesheet" href="{G.KERNEL}">\n  <link rel="stylesheet" href="vdl.css">\n  <style>\n    body {{ margin: 0; }}\n    {CSS}\n  </style>\n</helmet>\n'
            + root + '\n</x-dc>\n</body>\n</html>\n')
HEIGHTS = {'19': 9000, '20': 9000, '21': 9000}
try:
    import json; HEIGHTS.update(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'live_heights.json'))))
except Exception: pass

# ============================== 19 · A new city, no plan =========================================================
V = ''   # a visitor: new account, nothing held, no avatar history
def v_open(time='10:40 AM', located=True, seen=False):
    near = '6 MIN ON FOOT &middot; ' if located else ''
    pier = '9 MIN ON FOOT &middot; ' if located else ''
    sub = 'Clear, 58&deg; &middot; you&rsquo;re a few blocks from the water.' if located else 'Clear, 58&deg; in New York.'
    title = 'The flea under the bridge is on until three.' if located else 'Saturday in New York. The flea under the bridge is on until three.'
    return phone(anchor('NEW YORK &middot; SATURDAY', time, V), read(title, sub),
        sect('This afternoon, if you want'),
        unit('The flea, under the bridge', 'The bread stall sells out by ten; the rest of the stalls hold all day.', near + 'THE MARKET&rsquo;S OWN NOTICE &middot; UNTIL 3'),
        gut(orline()),
        unit('The pier at low water, from 2:40', 'The granite kerbs show where the flood gates&rsquo; protection ends. Dry to walk until five.',
             pier + 'TIDE TABLE &middot; TODAY', f'<div style="margin-top: 2px;">{gold("The flood line, walked")}</div>'),
        sect('Worth reading'),
        unit('The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.',
             'THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', f'<div style="margin-top: 2px;">{gold("Read the chapter")}</div>'),
        f'<div style="padding: 28px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">Nothing else today.</div></div>')
def itinerary():
    step = lambda t, a, b, last=False: (f'<div style="display: flex; gap: 14px; padding: 10px 0;{"" if last else " border-bottom: 1px solid rgba(27,23,20,0.06);"}"><span style="font-family: {MONO}; font-size: 12px; font-weight: 700; width: 46px; flex: none; padding-top: 2px;">{t}</span>'
                                        f'<div><div style="font-size: 15px; line-height: 20px;">{a}</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{b}</div></div></div>')
    return phone(anchor('NEW YORK &middot; SATURDAY', '10:40 AM', V), read('Your afternoon in Red Hook.', 'Four stops, planned around low water.'),
        card(ctitle('Today') + '<div style="margin-top: 8px;">'
             + step('10:50', 'The flea, under the bridge', 'Leave by 12:15') + step('12:30', 'Lunch near the water', 'Forty minutes')
             + step('2:40', 'The pier at low water', 'Walk the flood line') + step('4:00', 'The pumps under the park', 'Read on the bench', last=True) + '</div>'
             + f'<div style="margin-top: 12px;"><span class="vdl-btn primary vk-t-labelSemibold" style="color: var(--vk-color-white); min-height: 40px;">Start the afternoon</span></div>'))
def places_pier():
    top = (f'<div style="padding: 24px 22px 0 22px; display: flex; align-items: center;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M12.5 4L7 10L12.5 16" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
           f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE}; margin-left: auto;">PLACES &middot; RED HOOK</span></div>')
    return phone(top, gut(f'<div class="fn" style="color: {MUTE};">THE WEST PIER &middot; LOW WATER 2:40&ndash;5:10</div>'
                          f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 26px; line-height: 30px; margin-top: 6px;">The flood line, walked</div>'
                          f'<div style="font-size: 14px; line-height: 21px; color: {INK2}; margin-top: 10px;">Start at the crossing and follow the granite kerbs toward the water. Where the new kerb meets the old cobbles is where the gates stop protecting the street.</div>', 20),
                 gut(f'<div style="height: 150px; border-radius: 12px; background: #E3DCCB; position: relative; overflow: hidden;">'
                     '<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 58px; background: #BFD6DA;"></div>'
                     '<div style="position: absolute; left: 40px; right: 70px; top: 70px; height: 4px; background: #1B1714; border-radius: 2px;"></div>'
                     '<div style="position: absolute; left: 34px; top: 62px; width: 14px; height: 14px; border-radius: 7px; background: #1B1714;"></div>'
                     '<div style="position: absolute; right: 64px; top: 62px; width: 14px; height: 14px; border-radius: 7px; background: #4A3428;"></div></div>'
                     + fn('THE CROSSING &rarr; THE OLD COBBLES &middot; 600 FT', mt=8), 18),
                 rows(row(glyph('water'), 'Low water 2:40, dry to walk until 5:10', meta='TIDE TABLE &middot; TODAY'),
                      row(glyph('book'), 'Why the pumps matter here', sub='The Harbor Book, ch. 4 &middot; 4 min', last=True)))
def correction_chat():
    return chat('SATURDAY 10:44 AM', ctx('HOME &middot; SATURDAY'),
                you('only here an hour, then meeting a friend in the city'),
                vesper('Then I&rsquo;d do the flea: six minutes from you and on until three. The pier needs the afternoon.', 'FROM WHAT YOU SAID &middot; FOR TODAY'),
                field('Ask, or change it'))
def after_correction():
    return phone(anchor('NEW YORK &middot; SATURDAY', '10:45 AM', V), read('The flea under the bridge is six minutes away.', 'Clear, 58&deg; &middot; on until three.'),
        sect('On your way'),
        unit('The flea, under the bridge', 'The bread stall sells out by ten; the rest of the stalls hold all day.', '6 MIN ON FOOT &middot; THE MARKET&rsquo;S OWN NOTICE &middot; UNTIL 3',
             f'<div style="margin-top: 2px;">{gold("Directions")}</div>'),
        sect('Worth reading'),
        unit('The pumps under the park finish what the gates cannot', '', 'THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', f'<div style="margin-top: 2px;">{gold("Read the chapter")}</div>'),
        f'<div style="padding: 28px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">Nothing else today.</div></div>')
def quiet_interval():
    return phone(anchor('NEW YORK &middot; SATURDAY', '1:15 PM', V), read('Low water on the pier from 2:40.', 'Clear, 61&deg;.', size=22),
        sect('This afternoon, if you want'),
        unit('The pier at low water, from 2:40', 'Dry to walk until five.', '9 MIN ON FOOT &middot; TIDE TABLE', f'<div style="margin-top: 2px;">{gold("The flood line, walked")}</div>'),
        f'<div style="padding: 28px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">Nothing else today.</div></div>')

b19 = (band('ROW ONE &middot; THE FIRST OPEN', 'A visitor&rsquo;s first Saturday in New York. The account holds only the city and, in the selected frame, an approximate location. The same evidence is drawn twice: as openings with practical fit, and as a timed afternoon.')
       + rowwrap(cell('SELECTED &middot; SATURDAY 10:40 AM', '19.1 &middot; OPENINGS, NOT A SCHEDULE', 'Two things this afternoon makes possible, and something to read',
                      'Location on (approximate) &middot; 14&rsquo;s supply &middot; nothing held about the person', v_open()),
                 cell('THE SAME EVIDENCE &middot; NOT CHOSEN', '19.2 &middot; A TIMED AFTERNOON', 'Four stops with times and a start button',
                      'Drawn for comparison only', itinerary()),
                 notes([('WHY 19.1', 'The same four things as 19.2. 19.1 gives each its practical fit (distance, until three, from 2:40) and leaves the choice open; the OR says they are alternatives, not a sequence. 19.2 turns a free afternoon into an appointment book the visitor never asked for, and its start button makes leaving the plan feel like failing it.'),
                        ('WHAT THE PERSON KEEPS', 'Choosing, wandering and stopping. What Vesper carries is the checking: the market&rsquo;s own hours, the tide, the walking distance.'),
                        ('WHAT EARNED THE TOP', 'The flea is the one thing in reach that ends today. The pier is the second opening because it only exists at low water. The reading is here because the pier makes it concrete, not because the visitor has shown an interest.')]), first=True)
       + band('ROW TWO &middot; AN OPENING FOLLOWED, THEN A CORRECTION', 'The pier opens in Places, which owns the destination; Back returns to 19.1 at the same position. Then the visitor tells Chat they are only here an hour.')
       + rowwrap(cell('OPEN &middot; 10:42 AM', '19.3 &middot; THE DESTINATION', 'The flood line, in Places', 'Places owns the page &middot; Back returns to Home as it was', places_pier()),
                 cell('A WRONG INFERENCE &middot; 10:44 AM', '19.4 &middot; &ldquo;ONLY HERE AN HOUR&rdquo;', 'Corrected in ordinary words, in Chat', 'No wizard &middot; the correction is for today only', correction_chat()),
                 cell('THE RESULT &middot; 10:45 AM', '19.5 &middot; HOME, CORRECTED', 'The afternoon opening leaves; the flea leads', 'Scroll and navigation unchanged', after_correction()),
                 notes([('WHAT CHANGED, AND WHAT DIDN&rsquo;T', 'The pier assumed an afternoon here, so it leaves today&rsquo;s page. The sub-line about being near the water goes with it. The flea gains directions because it is now the plan. Nothing records a dislike: the pier stays in Places, and the next Saturday can offer it again.'),
                        ('SCOPE', '&ldquo;Only here an hour&rdquo; corrects the current situation. It changes no preference, no Plan and nothing anyone else holds.')], 520))
       + band('ROW THREE &middot; NO LOCATION, LARGER TEXT, AND AN HOUR WITH NOTHING TO DO', 'The same visitor without location permission, the selected open at 1.3&times; text, and the page after lunch when nothing has changed.')
       + rowwrap(cell('NO LOCATION &middot; 10:40 AM', '19.6 &middot; CITY-LEVEL ONLY', 'The same openings without walking times', 'Location declined &middot; nothing asks for it', v_open(located=False)),
                 cell('LARGER TEXT &middot; 10:40 AM', '19.7 &middot; 19.1 AT 1.3&times;', 'Times and distances stay in the body, not only in the stamp', 'Every type size and leading &times;1.3', '<div class="lt">' + larger(v_open()) + '</div>'),
                 cell('NOTHING TO RESOLVE &middot; 1:15 PM', '19.8 &middot; A HEALTHY HOUR', 'One opening left, then the page ends', 'Read at 22 &middot; no new unit, no nudge', quiet_interval()),
                 notes([('WITHOUT LOCATION', 'The openings stay; only their distances go. Nothing on the page asks for permission. The read names the city, since that is all the account holds.'),
                        ('LARGER TEXT', 'The tide&rsquo;s hours and the flea&rsquo;s closing time are in the body copy and the stamp, so they survive the stamp becoming hard to read.'),
                        ('THE HEALTHY HOUR', 'After the flea the page says less: the pier is the one thing left and the page ends. Putting the phone away is the expected outcome.')], 520))
       + band('SELECTION RATIONALE', '')
       + table(['Value received', 'Effort left with the person', 'What earned prominence', 'Donors reused', 'Unresolved'], [
           ['Orientation (where, until when), two real openings with practical fit, one piece of understanding', 'Choosing, and whether to do anything at all',
            'Time-bound and in reach: the flea ends at three; low water only exists from 2:40', 'Home 14 supply (flea, pier, pumps); 02&rsquo;s flood line; Places destination; 12&rsquo;s Chat turn',
            'Places owns the pier page; approximate-location accuracy; whether a visitor with no history gets these openings at all is a supply question, not a layout one']]))

# ============================== 20 · An evening together =========================================================
LIFE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'life', 'build_0921.py')).read()
_ns = {'gut': lambda inner, top=12: f'<div style="margin:{top}px 22px 0 22px;">{inner}</div>'}
exec(LIFE[LIFE.index('ASPECT = {'):LIFE.index('ORDER = [')], _ns)
lphoto = _ns['photo']
EVE = 'Pasta night &middot; at yours'
def evening_card(lines, extra='', title=EVE, sub='From seven &middot; Sam and Maya'):
    return card(ctitle(title) + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{sub}</div>'
                + '<div style="margin-top: 10px; border-top: 1px solid rgba(27,23,20,0.08);">' + ''.join(lines) + '</div>' + extra)
def person(initial, name, fact, words='', when='', last=False):
    w = f'<div style="font-family: {SERIF}; font-size: 16px; line-height: 21px; color: {INK}; margin-top: 4px;">&ldquo;{words}&rdquo;</div>' + fn(when, mt=4) if words else ''
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    return (f'<div style="display: flex; gap: 12px; padding: 10px 0;{b}">{face([initial], 26)}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 15px; line-height: 20px;"><span style="font-weight: 600;">{name}</span> &middot; {fact}</div>{w}</div></div>')
def dana():
    return gut(f'<div style="display: flex; gap: 14px; align-items: flex-start;"><div style="flex: none; border-radius: 6px; overflow: hidden;">{lphoto("PH-05", w=96)}</div>'
               f'<div style="flex: 1; min-width: 0;">{said("D", "Dana", "FRI &middot; FROM SORRENTO", "Fry the zucchini first and let them sit. Twenty minutes, not five.")}</div></div>')
def host_before():
    return phone(anchor('NEW YORK &middot; SATURDAY', '3:10 PM'), read('Pasta night at seven. Maya asked about eight.', 'Clear, 64&deg; &middot; Sam leaves by nine.'),
        evening_card([person('S', 'Sam', 'around 7:30', 'have to head out by nine, sorry!', 'SAM &middot; THU &middot; BY TEXT'),
                      person('M', 'Maya', 'asked for eight', 'could we do eight? the afternoon is running long', 'MAYA &middot; 2:52 PM', last=True)],
                     f'<div style="display: flex; gap: 20px; margin-top: 6px;">{ink("Keep seven")}{ink("Move to eight")}</div>'),
        sect('For tonight'), dana(),
        rows(row(glyph('book'), 'Spaghetti alla Nerano', meta='YOUR SCREENSHOT &middot; THU 3:12 PM', last=True)),
        sect('Tomorrow'), unit('Clear, 64&deg;', '', 'FORECAST &middot; 3 PM'),
        week([('SAT', 'today', True), ('SUN', ''), ('MON', ''), ('TUE', ''), ('WED', ''), ('THU', ''), ('FRI', '')], 'Pasta night, from seven.'))
def host_after_answer():
    return phone(anchor('NEW YORK &middot; SATURDAY', '3:14 PM'), read('Pasta night at seven.', 'Clear, 64&deg; &middot; Maya comes at eight.'),
        evening_card([person('S', 'Sam', 'around 7:30, leaves by nine'),
                      person('M', 'Maya', 'at eight', 'ok! start without me, I&rsquo;ll bring dessert', 'MAYA &middot; 3:13 PM', last=True)]),
        gut(notice('applied', 'Seven stays &middot; told Maya at 3:13', 'Sam&rsquo;s nine o&rsquo;clock still works.'), 12),
        sect('For tonight'), dana())
def host_gathering():
    return phone(anchor('NEW YORK &middot; SATURDAY', '7:25 PM'), read('Sam around 7:30. Maya at eight.', size=22),
        evening_card([person('S', 'Sam', 'around 7:30, leaves by nine'), person('M', 'Maya', 'at eight, with dessert', last=True)]),
        sect('For tonight'), dana(),
        rows(row(glyph('book'), 'Spaghetti alla Nerano', meta='YOUR SCREENSHOT &middot; THU 3:12 PM', last=True)))
def maya_late():
    return phone(anchor('NEW YORK &middot; SATURDAY', '7:40 PM', 'M'), read('Nora&rsquo;s at eight.', 'Court Street, 3F &middot; the buzzer says N.'),
        card(ctitle('Pasta night &middot; at Nora&rsquo;s') + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">From seven &middot; you said eight</div>'
             + '<div style="margin-top: 10px; border-top: 1px solid rgba(27,23,20,0.08);">'
             + person('N', 'Nora', 'hosting', 'we&rsquo;ll save you a plate', 'NORA &middot; 3:15 PM') + person('S', 'Sam', 'leaves by nine', last=True) + '</div>'
             + f'<div style="margin-top: 6px;">{gold("Court Street, 3F")}</div>'),
        sect('In motion'), rows(row(glyph('msg'), 'Dessert for four', sub='You said you&rsquo;d bring it', last=True)))
def sam_link():
    return (f'<div style="width: 393px; background: {PAPER}; box-sizing: border-box; padding: 22px;">'
            '<dc-import name="InviteCard" view="guest" shape="pill" kicker="FROM NORA" title="Pasta night at Nora&rsquo;s" '
            'lines="Saturday from seven|you said around seven-thirty;Court Street, 3F|the buzzer says N;Maya comes at eight|with dessert" '
            'from="Nora" guestNote="Nora sees your answer. Nothing else is shared." hint-size="349px,560px"></dc-import></div>')
def together():
    return phone(anchor('NEW YORK &middot; SATURDAY', '8:40 PM'), read('Saturday evening.', 'Clear, 61&deg;. Tomorrow, clear and 64&deg;.', size=17),
        evening_card([person('S', 'Sam', 'leaves by nine'), person('M', 'Maya', 'here since eight', last=True)], sub='From seven'),
        week([('SAT', 'today', True), ('SUN', ''), ('MON', ''), ('TUE', ''), ('WED', ''), ('THU', ''), ('FRI', '')], 'Nothing else tonight.'))
# the show variation — Persona A (Nadia) and Alex, Friday, The Hall
def show_move():
    return phone(anchor('NEW YORK &middot; FRIDAY', '7:22 PM'), read('Doors at eight. Meeting Alex at the side door.', 'Clear, 41&deg; &middot; the bar across the street is full.'),
        card(f'<div style="display: flex; align-items: baseline;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #3C352E;">ADMISSION &middot; THE HALL</span><span class="fn" style="margin-left: auto;">FRIDAY</span></div>'
             + ctitle('The Hall', 24) + f'<div style="font-size: 12px; color: {MUTE}; margin-top: 2px;">Set times posted at 6</div>'
             + '<div style="margin-top: 12px; border-top: 1px solid rgba(27,23,20,0.08); padding-top: 10px;">'
             + person('A', 'Alex', 'meeting you', last=True)
             + f'<div style="font-size: 14px; line-height: 20px;"><span style="text-decoration: line-through; color: {HINT};">The bar across the street, 7:30</span></div>'
             + '<div style="font-size: 15px; line-height: 20px; margin-top: 4px;">The side door, 7:40</div></div>'
             + gut('', 0) + f'<div style="margin-top: 10px;">{notice("pending", "Waiting to reach Alex", "Sent 7:21. It goes as soon as his phone picks it up.", h=80)}</div>'),
        sect('After the show'), rows(row(glyph('walk'), 'The way home is a surface route', sub='25 minutes longer after ten', meta='THE HALL&rsquo;S LATE SERVICE &middot; CHECKED 5:40', last=True)))
def alex_receives():
    return phone(anchor('NEW YORK &middot; FRIDAY', '7:34 PM', 'A'), read('Nadia moved the meet to the side door, 7:40.', 'The bar across the street is full.', size=22),
        card(said('N', 'Nadia', '7:21 PM', 'bar&rsquo;s packed, side door instead?', '#4A3428')
             + f'<div style="display: flex; gap: 20px; margin-top: 10px;">{ink("Reply to Nadia")}</div>'),
        sect('Tonight'), rows(row(glyph('hall'), 'The Hall &middot; doors 8', sub='Set times posted at 6', last=True)))
def way_home():
    return phone(anchor('NEW YORK &middot; FRIDAY', '10:52 PM'), read('The way home is the surface route tonight.', '25 minutes longer than the train &middot; 38&deg;.', size=22),
        '<div style="height: 18px;"></div>', rows(row(glyph('walk'), 'Surface route from the Hall', sub='Next bus 11:04 &middot; 44 minutes door to door', meta='SERVICE READ &middot; 10:50 PM'),
             row(glyph('msg'), 'Alex&rsquo;s ride', sub='He said he&rsquo;s staying for the last set', last=True, chev=False)),
        f'<div style="padding: 28px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px;">Tomorrow, the park at 6:30.</div></div>')

b20 = (band('ROW ONE &middot; BEFORE &middot; THE HOST', 'Nora hosts pasta night (fixture ledger &sect;1, &sect;9.3): from seven, Sam around 7:30 and leaving by nine, Maya asking about eight. Dana, in Sorrento, contributed once on Friday and holds nothing else.')
       + rowwrap(cell('HOST &middot; SATURDAY 3:10 PM', '20.1 &middot; ONE SHARED DECISION', 'Maya&rsquo;s eight, with Sam&rsquo;s nine beside it', 'Plans owns the arrangement &middot; Dana&rsquo;s tip is a complete contribution', host_before()),
                 cell('AFTER NORA ANSWERS &middot; 3:14 PM', '20.2 &middot; SEVEN STAYS; MAYA COMES AT EIGHT', 'A shared time kept; one person&rsquo;s arrival changed by her', 'Shared Notice, applied', host_after_answer()),
                 notes([('TWO KINDS OF CHANGE', '&ldquo;Move to eight&rdquo; would change the shared arrangement for everyone, so it is Nora&rsquo;s call and Plans carries it. Maya coming at eight changes only her own arrival, and she makes it. The Notice records the one message that went; nothing else was sent.'),
                        ('THE ONE ASK', 'The only decision on the page is the one with a real dependency: Sam leaves at nine. Once answered it leaves; nothing counts down to seven.'),
                        ('DANA', 'She gave a tip and a photograph from Sorrento. It sits under For tonight because it helps the cooking. She has no status, location or reply to keep up.')]), first=True)
       + band('ROW TWO &middot; GATHERING &middot; HOST, LATE JOINER, GUEST', 'The same evening at 7:25&ndash;7:40 from three places. Sam has no account; his view is the invitation link Social owns, drawn with the shared InviteCard.')
       + rowwrap(cell('HOST &middot; 7:25 PM', '20.3 &middot; WHAT&rsquo;S KNOWN', 'Who said when; nothing tracked', 'Arrival times are their own words', host_gathering()),
                 cell('LATE JOINER &middot; 7:40 PM', '20.4 &middot; MAYA&rsquo;S HOME', 'The address and buzzer first; the evening as Nora left it', 'Maya&rsquo;s own Home &middot; her dessert is her own open item', maya_late()),
                 cell('GUEST &middot; SAM&rsquo;S LINK', '20.5 &middot; THE INVITATION, FROM NORA', 'Sam&rsquo;s view, with his own seven-thirty', 'Shared InviteCard, guest &middot; Social owns the link', sam_link()),
                 notes([('UNKNOWN IS NOT LATE', 'At 7:25 nobody&rsquo;s position is known, and the page says only what people said: around 7:30, at eight. If Sam arrives at 7:45 nothing on Nora&rsquo;s page turns red.'),
                        ('DIFFERENT EMPHASIS, ONE OCCASION', 'The host sees who and when; the late joiner sees the address, the buzzer and her own dessert; the guest sees the invitation with his own seven-thirty. None of them sees anyone else&rsquo;s location.')], 520))
       + band('ROW THREE &middot; TOGETHER, AND AFTERWARD', 'During dinner the page has nothing to do. Afterward is board 18 K: Maya&rsquo;s table photograph on Sunday, not redrawn here.')
       + rowwrap(cell('TOGETHER &middot; 8:40 PM', '20.6 &middot; NOTHING TO RESOLVE', 'If Nora glances at her phone, the page is short', 'Direct-state read at 17 &middot; no prompt, no photo request', together()),
                 notes([('WHY SO LITTLE', 'Everyone who is coming is there or has said when. No decision is open, nothing is at risk, and the best thing Home can do during a good dinner is be finished. No reminder to take photos, no request for a rating.'),
                        ('AFTERWARD', '18 K is the selected next morning: Maya&rsquo;s note on the Print Room leads, her table photograph follows, the rest of Home stays. The evening becomes findable in Life as Pasta night; nothing asks Nora to recap it.')], 700))
       + band('ROW FOUR &middot; THE SHOW VARIATION', 'Persona A&rsquo;s Friday at The Hall (08, 09): Nadia moves the meet with Alex when the bar is full; the change reaches Alex on the way; afterward, the way home.')
       + rowwrap(cell('NADIA &middot; FRIDAY 7:22 PM', '20.7 &middot; A MEETING POINT MOVES', 'The change is sent, and says it hasn&rsquo;t arrived yet', 'Shared Notice, pending &middot; no read receipt', show_move()),
                 cell('ALEX &middot; 7:34 PM, EN ROUTE', '20.8 &middot; IT ARRIVES', 'Her words first, then where he&rsquo;s going', 'Reply is optional', alex_receives()),
                 cell('NADIA &middot; 10:52 PM', '20.9 &middot; THE WAY HOME', 'Practical care after the last set', 'The Hall&rsquo;s late service &middot; 08&rsquo;s way-home fact', way_home()),
                 notes([('PENDING, DELIVERED, AGREED', '&ldquo;Waiting to reach Alex&rdquo; is all Nadia&rsquo;s page claims at 7:22. Delivery is not agreement, and there is no seen marker. At 7:34 his page carries her words; whether he agrees is his reply to give.'),
                        ('NO LOCATION', 'Neither sees the other on a map. The meeting point is a place both know, which is what the coordination needed.')], 520))
       + band('SELECTION RATIONALE', '')
       + table(['Value received', 'Effort left with the person', 'What earned prominence', 'Donors reused', 'Unresolved'], [
           ['One real decision resolved; a friend&rsquo;s tip that helps the cooking; the address and buzzer for the late joiner; a moved meeting point that reaches the person on the way; the way home', 'Answering Maya; replying if they want',
            'A dependency (Sam leaves at nine) and a change in reach (the bar is full); everything else stays quiet', 'Fixture ledger &sect;1/&sect;9.3; shared InviteCard and Notice; Life&rsquo;s PH-05; 08/09&rsquo;s Hall and way home; 18 K for afterward',
            'Plans owns the arrangement and its message; Social owns Sam&rsquo;s link and delivery; Alex&rsquo;s delivery state is a platform fact, not a design one']]))

# ============================== 21 · A travel day ================================================================
def fpass(state='', urgent=False, compact=False):
    kick = ('<div style="display: flex; align-items: baseline;">'
            f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #3C352E;">FLIGHT &middot; TAP 214</span>'
            f'<span class="fn" style="margin-left: auto;">TODAY</span></div>')
    st = (f'<div style="display: flex; align-items: center; gap: 7px; margin-top: 8px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX};"></span>'
          f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">{state}</span></div>') if state else ''
    codes = (f'<div style="display: flex; align-items: flex-end; gap: 10px; margin-top: 10px;"><div><div style="font-family: {SERIF}; font-size: 30px; line-height: 32px; font-weight: 600;">JFK</div><div style="font-size: 12px; color: {MUTE};">New York</div></div>'
             f'<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.25); margin-bottom: 22px;"></span>'
             f'<div style="text-align: right;"><div style="font-family: {SERIF}; font-size: 30px; line-height: 32px; font-weight: 600;">LIS</div><div style="font-size: 12px; color: {MUTE};">Lisbon</div></div></div>')
    def f(k, v): return f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: #6E6862;">{k}</span><span style="font-family: {MONO}; font-size: 14px; font-weight: 500;">{v}</span></div>'
    fields = f'<div style="display: flex; gap: 22px; margin-top: 12px;">{f("GATE", "B22")}{f("SEAT", "24A")}{f("BOARDS", "18:05")}{f("DEPART", "18:45")}</div>'
    if compact:
        return kick + st + f'<div style="font-family: {SERIF}; font-size: 20px; line-height: 24px; font-weight: 600; margin-top: 8px;">JFK &rarr; Lisbon</div>' + fields
    return kick + st + codes + fields
def prep():
    return phone(anchor('NEW YORK &middot; FRIDAY', '10:15 AM'), read('Lisbon tonight. Leave work by 3:40.', 'Clear, 64&deg; &middot; Maya and Alex are on the 8:10.'),
        card(fpass(compact=True).replace('>B22<', '>&mdash;<')
             + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 12px;">The A train, then the AirTrain: sixty-two minutes door to gate. Bag drop closes at 5:45.</div>'
             + fn('YOUR TICKET &middot; GATE NOT POSTED YET', mt=8)),
        rows(row(glyph('bell'), 'Gate and delay changes', sub='Told to you here and by notification, until you board', meta='YOU ASKED &middot; ENDS AT BOARDING'),
             row(glyph('key'), 'Lisbon on landing', sub='The stay, the door code, the walk from the tram', meta='ON THIS PHONE &middot; WORKS OFFLINE', last=True)),
        sect('In motion'), rows(row(face(['M', 'A']), 'Maya and Alex &middot; the 8:10', sub='Landing 9:25 tomorrow'),
                                row(glyph('ticket'), 'Sintra on Sunday', sub='The 9:10 train &middot; palace at 2', last=True)),
        sect('For the flight'), unit('The pumps under the park finish what the gates cannot', '', 'THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN &middot; SAVED OFFLINE'),
        week([('FRI', 'tonight', True), ('SAT', 'Lisbon'), ('SUN', 'Sintra', False, True), ('MON', ''), ('TUE', ''), ('WED', 'home'), ('THU', '')], 'Tonight, the 6:45 to Lisbon.'))
def rush(scale=1.0):
    h = phone(anchor('NEW YORK &middot; FRIDAY', '3:58 PM'), read('The A is stopped. A car makes bag drop.', size=22),
        card(fpass('BAG DROP CLOSES 5:45', urgent=True, compact=True)
             + f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 19px; line-height: 24px; margin-top: 14px;">Take a car from the corner now</div>'
             + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">The A is stopped at Broadway Junction with no restart time. A car reaches Terminal 4 by 5:05 in today&rsquo;s traffic.</div>'
             + f'<div style="min-height: 44px; background: #4A3428; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 12px;"><span style="color: {CARD}; font-size: 15px; font-weight: 600;">Open the way there</span></div>'
             + fn('TRANSIT ALERT 3:51 PM &middot; DRIVING TIME 3:57 PM', mt=8)),
        rows(row(glyph('msg'), 'The rest of Friday is still here', sub='Maya and Alex&rsquo;s 8:10 &middot; Lisbon on landing &middot; Sunday', last=True)))
    return h
def waiting():
    return phone(anchor('JFK &middot; TERMINAL 4', '5:20 PM'), read('Boarding at 6:05 from B22.', '45 minutes &middot; the gate is a two-minute walk.', size=22),
        card(fpass(compact=True) + fn('GATE FROM THE AIRLINE &middot; 5:18 PM', mt=10), pad='14px 18px'),
        sect('From Maya'),
        gut('<div style="padding: 4px 0 6px;"><dc-import name="OriginalReader" density="open" author="Maya" meta="4:48 PM · TO YOU" '
            'words="we land 9:25, meet you at the stay? bringing the good coffee" hint-size="349px,150px"></dc-import></div>'),
        sect('For the flight'),
        unit('The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes.', 'THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN &middot; SAVED OFFLINE',
             f'<div style="margin-top: 2px;">{gold("Read the chapter")}</div>'),
        sect('Saturday in Lisbon'), unit('Nothing booked until Sunday', 'The stay is ten minutes from the river; the morning is yours.', 'YOUR TRIP &middot; SAT OPEN'),
        week([('FRI', 'tonight', True), ('SAT', 'Lisbon'), ('SUN', 'Sintra', False, True), ('MON', ''), ('TUE', ''), ('WED', 'home'), ('THU', '')], 'Maya and Alex land at 9:25.'))
def skip_chat():
    return chat('FRIDAY 5:31 PM', ctx('SINTRA &middot; SUNDAY'), you('skip sintra for me on sunday, I&rsquo;ll stay in town'),
                vesper('Sintra stays on for Maya and Alex; I&rsquo;ve taken you off it. Your palace ticket is still yours to use or return in the provider&rsquo;s app.', 'THE TRIP &middot; YOUR PART ONLY'),
                field('Ask, or change it'))
def skip_result():
    return phone(anchor('JFK &middot; TERMINAL 4', '5:32 PM'), read('Boarding at 6:05 from B22.', size=22),
        card(fpass(compact=True), pad='14px 18px'),
        sect('In motion'), rows(row(face(['M', 'A']), 'Sintra on Sunday &middot; Maya and Alex', sub='The 9:10 train &middot; you&rsquo;re staying in town'),
                                row(glyph('ticket'), 'Your palace ticket, Sunday at 2', sub='Unused &middot; return it in the provider&rsquo;s app', last=True)),
        week([('FRI', 'tonight', True), ('SAT', 'Lisbon'), ('SUN', 'open'), ('MON', ''), ('TUE', ''), ('WED', 'home'), ('THU', '')], 'Sunday is yours.'))
def offline():
    stale = f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {MUTE}; border: 1px solid rgba(27,23,20,0.18); border-radius: 8px; padding: 2px 6px;">OFFLINE</span>'
    return phone(anchor('LISBON &middot; SATURDAY', '7:12 AM'), read('The stay is twelve minutes from the tram.', 'Landed 6:58 &middot; this page is from 5:52 PM in New York.', size=22),
        gut(f'<div style="display: flex; align-items: center; gap: 8px;">{stale}<span style="font-size: 13px; color: {MUTE};">Everything below works without a connection unless it says otherwise.</span></div>', 14),
        card(ctitle('The stay', 19) + '<div style="margin-top: 8px; border-top: 1px solid rgba(27,23,20,0.08);">'
             + row(glyph('pin'), '[Fixture street] 14, second floor', chev=False)
             + row(glyph('key'), 'Door code 4417', sub='Then the key box inside, left of the stairs', chev=False)
             + row(glyph('tram'), 'From the tram stop', sub='Uphill on the left, past the tiled church; the third blue door', chev=False, last=True) + '</div>'
             + fn('YOUR BOOKING &middot; SAVED ON THIS PHONE', mt=8)),
        rows(row(glyph('walk'), 'Walking directions', sub='Need a connection; the written way above works now', chev=False),
             row(face(['M', 'A']), 'Maya and Alex&rsquo;s 8:10', sub='On time when last checked', meta='AS OF 5:52 PM NEW YORK', chev=False),
             row(glyph('msg'), 'Your note to Maya', sub='Waiting to send &middot; goes when you&rsquo;re connected', chev=False),
             row(glyph('ticket'), 'Palace tickets, Sunday', sub='Open in the provider&rsquo;s app', last=True)))
def arrival():
    return phone(anchor('LISBON &middot; SATURDAY', '11:40 AM'), read('Saturday in Lisbon is open. Maya and Alex are at the stay.', 'Clear, 72&deg; &middot; Sintra is Sunday, for them.'),
        sect('If you want'),
        unit('The viewpoint above the stay', 'Ten minutes uphill; the light on the river is best before one.', '10 MIN ON FOOT &middot; FIXTURE VIEWPOINT', f'<div style="margin-top: 2px;">{gold("The way up")}</div>'),
        gut(orline()),
        unit('The market by the river', 'Open until two on Saturdays; the fish stalls close first.', '14 MIN ON FOOT &middot; THE MARKET&rsquo;S OWN HOURS'),
        sect('In motion'), rows(row(face(['M', 'A']), 'Maya and Alex', sub='Landed 9:31 &middot; at the stay'),
                                row(glyph('ticket'), 'Your palace ticket, Sunday at 2', sub='Unused &middot; return it in the provider&rsquo;s app', last=True)),
        week([('SAT', 'today', True), ('SUN', 'open'), ('MON', ''), ('TUE', ''), ('WED', 'home'), ('THU', ''), ('FRI', '')], 'Home on Wednesday.'))

b21 = (band('ROW ONE &middot; PREPARATION, THE RUSH, AND THE WAIT', 'Persona A&rsquo;s Friday (08, 12): TAP 214 JFK&rarr;Lisbon at 6:45, Maya and Alex on the 8:10. The same Home at 10:15, at 3:58 when the A train stops, and at 5:20 at the gate.')
       + rowwrap(cell('PREPARATION &middot; FRIDAY 10:15 AM', '21.1 &middot; LIVE, AND STILL BROAD', 'The flight leads; the rest of Friday stays', 'One accepted responsibility, with its end stated', prep()),
                 cell('A GENUINE RUSH &middot; 3:58 PM', '21.2 &middot; URGENT', 'One recovery, one action; the rest folds to a row', 'The only Urgent frame in the suite', rush()),
                 cell('COMFORTABLE WAITING &middot; 5:20 PM', '21.3 &middot; LIVE AGAIN, BROAD AGAIN', 'Through security with 45 minutes: Maya, reading, Saturday', 'The pass compacts; nothing is urgent', waiting()),
                 notes([('WHY THE PAGE NARROWS AND WIDENS', 'At 10:15 the flight is a healthy commitment, so it leads without taking the page. At 3:58 a stopped train threatens bag drop, the only case in this suite where Home suppresses the field. At 5:20 the pressure is gone, so breadth returns. The Home contract already allows this (Live is not attention protection), so it doesn&rsquo;t rely on 08&rsquo;s proposed Rule B.'),
                        ('FACT, OPTION, RESPONSIBILITY', 'Facts: the flight, the leave-by time, bag drop. Options: a chapter to read, Saturday&rsquo;s open morning. The one accepted responsibility, gate and delay changes, says who asked and when it ends: at boarding.'),
                        ('NO COUNTDOWN', 'Leave-by appears as a time, not a timer, and the rush frame drops it for the one action that matters.')], 520), first=True)
       + band('ROW TWO &middot; A CHANGE OF PLAN, AND LANDING WITHOUT SIGNAL', 'At the gate Nadia drops Sintra for herself. On landing her phone has no connection yet.')
       + rowwrap(cell('CHANGED INTENTION &middot; 5:31 PM', '21.4 &middot; &ldquo;SKIP SINTRA FOR ME&rdquo;', 'Her part changes; the trip does not', 'Chat, in ordinary words &middot; Plans owns the trip', skip_chat()),
                 cell('THE RESULT &middot; 5:32 PM', '21.5 &middot; HOME AFTER', 'Sunday opens for her; Sintra stays for Maya and Alex', 'Her ticket is left for her to decide', skip_result()),
                 cell('WEAK CONNECTIVITY &middot; SATURDAY 7:12 AM', '21.6 &middot; LANDED, OFFLINE', 'Each item says what still works', 'Saved on the phone vs needs a connection vs waiting to send', offline()),
                 notes([('SCOPE OF &ldquo;SKIP SINTRA&rdquo;', 'It changes Nadia&rsquo;s participation only. Maya and Alex keep the day; nobody is messaged on her behalf; the palace ticket is not cancelled, because returning it is her decision in the provider&rsquo;s app.'),
                        ('ITEM BY ITEM', 'Address, door code and the written way from the tram work offline. Walking directions say they need a connection. Maya and Alex&rsquo;s flight shows when it was last true. The note to Maya is waiting, not sent. The palace ticket opens in its own app rather than as a screenshot of a changing code.'),
                        ('LEGIBLE WHEN IT MATTERS', 'The door code and the way from the tram are body text, not stamps, so they hold at larger sizes and one-handed on a pavement.')], 520))
       + band('ROW THREE &middot; ARRIVAL, AND THE RUSH AT LARGER TEXT', 'The flight becomes Life&rsquo;s (FLOWN, 08 state 4). Home is a Saturday in a city with nothing booked.')
       + rowwrap(cell('ARRIVAL &middot; SATURDAY 11:40 AM', '21.7 &middot; THE DASHBOARD GOES', 'Two optional openings, the people, the one open item', 'No flight card; Saturday is not turned into a plan', arrival()),
                 cell('LARGER TEXT &middot; 3:58 PM', '21.8 &middot; 21.2 AT 1.3&times;', 'The action and bag drop still read first', 'Every type size and leading &times;1.3', '<div class="lt">' + larger(rush()) + '</div>'),
                 notes([('WHAT RETIRES', 'The pass, leave-by time, gate responsibility and offline banner are gone: the flight is flown and belongs to Life. What stays is what is still unresolved, the unused palace ticket, and what is useful now.'),
                        ('OPENINGS, NOT AN ITINERARY', 'The viewpoint and the market are alternatives with their practical fit (distance, best before one, closes at two). The morning belongs to Nadia, Maya and Alex.'),
                        ('THE RUSH, LARGER', 'At 1.3&times; the recovery sentence, bag drop and the one button stay in the first screen; the folded row moves down, which is the point.')], 700))
       + band('SELECTION RATIONALE', '')
       + table(['Value received', 'Effort left with the person', 'What earned prominence', 'Donors reused', 'Unresolved'], [
           ['Leave-by and the way there; a recovery when the train stops; breadth back at the gate; a friend&rsquo;s note; the stay usable offline; an open Saturday', 'Choosing a car; skipping Sintra; returning the ticket, or not',
            'The flight while it leads the day; the stopped train only while it threatens bag drop; afterwards, what is still open', '08 flight ladder, day-of pass, flown state; 12 provider-unknown and stale patterns; shared reader; 14&rsquo;s reading',
            'Airline and transit feeds; what the gate-change responsibility can actually promise; offline storage of the booking; the palace ticket&rsquo;s provider; Plans owns participation']]))

# ============================== write ============================================================================
BOARDS = {
    '19': ('19 - Live - A New City', '19 &middot; A new city, with no plan', 'VESPER &middot; HOME &middot; 19 &middot; LIVE HOME &middot; STUDY ONE &middot; 2026-09-23',
           'A visitor with nothing held but the city, on a Saturday by the water. Openings with practical fit against a timed afternoon; one followed to its destination; a wrong inference corrected in ordinary words; no location; larger text; an hour with nothing to do.', b19, 2000),
    '20': ('20 - Live - An Evening Together', '20 &middot; An evening together', 'VESPER &middot; HOME &middot; 20 &middot; LIVE HOME &middot; STUDY TWO &middot; 2026-09-23',
           'Pasta night from the host, the late joiner and the guest, with one friend who contributed once from far away; a shared time kept while one arrival changes; the evening itself, when nothing is needed; and a show where the meeting point moves while someone is on the way.', b20, 2000),
    '21': ('21 - Live - A Travel Day', '21 &middot; A travel day', 'VESPER &middot; HOME &middot; 21 &middot; LIVE HOME &middot; STUDY THREE &middot; 2026-09-23',
           'The same Home through a flight to Lisbon: broad in the morning, narrow for the one real rush, broad again at the gate; a change to one person&rsquo;s part of the trip; landing without a connection; and a Saturday with nothing booked.', b21, 2000)}
for k, (fname, title, kicker, intro, body, w) in BOARDS.items():
    html_ = board(k, title, kicker, intro, body, w, HEIGHTS[k])
    open(f'{OUT}/{fname}.dc.html', 'w').write(html_)
    print('wrote', fname, len(html_), 'readers', html_.count('name="OriginalReader"'), 'notices', html_.count('name="Notice"'), 'invites', html_.count('name="InviteCard"'))
h = G.rd('00')
TD = '<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">'
rowsx = ''.join('<tr>' + TD + n + '</td>' + TD + d + '</td>' + TD + 'Live Home &middot; 09-23 &middot; proposed studies</td></tr>' for n, d in [
    ('19 - Live - A New City', 'A sparse-context visitor on a Saturday by the water: openings with practical fit versus a timed afternoon, one followed to Places and back, a correction in Chat, no location, larger text, a healthy hour'),
    ('20 - Live - An Evening Together', 'Pasta night as host, late joiner and guest, with a contribute-once friend; a shared time kept while one arrival changes; the evening with nothing to do; the show variation with a moved meeting point'),
    ('21 - Live - A Travel Day', 'TAP 214 to Lisbon: preparation, the one urgent rush, comfortable waiting, &ldquo;skip Sintra for me&rdquo;, landing offline item by item, arrival with the dashboard gone')])
i = h.find('18 - Ordinary Photographs</td>'); j = h.find('</tr>', i) + 5
assert i > 0
open(f'{OUT}/00 - Index.dc.html', 'w').write(h[:j] + rowsx + h[j:]); print('wrote 00 with rows 19-21')
