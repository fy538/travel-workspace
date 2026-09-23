"""Trip-day Home scroll (2026-09-08) — composed by slicing the LIVE boards, since the 09-07 generators were lost.
Usage: python3 gen_trip.py <live_dir> <out_dir>
  live_dir holds 00.html 01.html 03.html 07.html fetched from the project's serve URLs.
Adds: a third SELECTED column on 03 (the trip day), three cells on 01, a deletion-test section on 07, index text on 00.
"""
import re, sys, os, subprocess, struct, zlib

LIVE, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
INK, INK2, MUTE, HINT, GOLD, GOLDD, CARD, PAPER = '#1B1714', '#2C2622', '#6E6862', '#8F877C', '#B0853A', '#8A6628', '#FBF7EC', '#EFEAE0'
MONO = "'JetBrains Mono', ui-monospace, monospace"
SERIF = "'EB Garamond', Georgia, serif"
HAIR = 'rgba(27,23,20,0.07)'
CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left: 6px;"><path d="M2 6.5H10M6.5 3L10 6.5L6.5 10" stroke="#8A6628" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def h03(): return open(f'{LIVE}/03.html').read()

def phone_open():
    return f'<div style="width: 393px; min-height: 0; background: {PAPER}; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK}; display: flex; flex-direction: column; box-sizing: border-box; ">'
def tabbar():
    """Lift the four-root bar from the donor board. Matches whatever paper it currently sits on
    (polish pass 4 moved it from #FBF7EC to the page paper), and fails loudly rather than silently."""
    h = h03()
    m = re.search(r'<div style="border-top: 1px solid rgba\(27,23,20,0\.10\); background: #[0-9A-F]{6}; display: flex; padding: 10px 22px 22px 22px;[^"]*">', h)
    if not m: raise SystemExit('tabbar: the four-root bar was not found in the donor board')
    i = m.start()
    depth = 0; end = None
    for m in re.finditer(r'<div\b|</div>', h[i:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0: end = i + m.end(); break
    return h[i:end]
def anchor(city, time):
    return (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">{city}</span>'
            f'<span class="fn" style="margin-left: auto;">{time}</span><span style="width: 24px; height: 24px; border-radius: 999px; background: #4A3428; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">N</span></div></div>')
def read(title, sub):
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 34px; letter-spacing: -0.01em;">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div></div>')
def sect(name):
    return (f'<div style="padding: 40px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{name}</span>'
            f'<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'
def fn(t, mt=6, color=HINT): return f'<div class="fn" style="margin-top: {mt}px; color: {color};">{t}</div>'
def mute(t): return f'<span style="color: {MUTE};">{t}</span>'
def row(mark, text, last=False):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    return f'<div class="row" style="padding: 8px 0;{b}">{mark}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">{text}</span>{CHEV}</div>'
def facepile(letters):
    out = '<span style="display: inline-flex; align-items: center; flex: none;">'
    for i, l in enumerate(letters):
        bg = '#4A3428' if l == 'N' else INK
        out += f'<span style="width: 28px; height: 28px; border-radius: 999px; background: {bg}; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {PAPER}; margin-left: {0 if i == 0 else -8}px;">{l}</span>'
    return out + '</span>'
def dot(kind='solid', color=GOLD):
    if kind == 'solid': return f'<span style="width: 7px; height: 7px; border-radius: 4px; background: {color}; flex: none;"></span>'
    return f'<span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px dashed {MUTE}; box-sizing: border-box; flex: none;"></span>'
def euro(): return f'<span style="font-family: {MONO}; font-size: 11px; font-weight: 700; color: {INK}; flex: none; width: 15px; text-align: center; opacity: 0.8;">&euro;</span>'
def door(t): return f'<div style="display: flex; align-items: center; min-height: 44px;"><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">{t}</span>{ARROW}</div>'
def kickm(t): return f'<span class="kickm">{t}</span>'

# ---- the three admitted kinds -------------------------------------------------
def temporal_strip():
    """now_temporal_strip — a band, not a card: what is true right now, and when the day stops asking."""
    stops = [('8:40', 'NOW', 'solid', INK), ('1:00', 'LUNCH', 'solid', GOLD), ('4:00', 'THE WALK', 'solid', GOLD), ('6:00', 'OPEN', 'hollow', HINT)]
    rail = '<div style="display: flex; align-items: center; margin-top: 12px;">'
    for i, (t, l, k, c) in enumerate(stops):
        if i: rail += f'<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.14); margin: 0 6px 14px;"></span>'
        mark = f'<span style="width: 8px; height: 8px; border-radius: 4px; background: {c};"></span>' if k == 'solid' else f'<span style="width: 8px; height: 8px; border-radius: 4px; border: 1.3px solid {c}; box-sizing: border-box;"></span>'
        rail += f'<span style="display: flex; flex-direction: column; align-items: center; gap: 4px; flex: none;">{mark}<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; color: {INK if k == "solid" else HINT};">{t}</span><span class="fn" style="font-size: 9px; color: {HINT};">{l}</span></span>'
    rail += '</div>'
    return (f'<div style="border-top: 1px solid rgba(27,23,20,0.16); border-bottom: 1px solid rgba(27,23,20,0.16); padding: 13px 0 12px;">'
            f'<div style="display: flex; align-items: center; gap: 10px;">{kickm("ON THE TRIP &middot; DAY 3 OF 13")}<span class="fn" style="margin-left: auto;">SORRENTO &middot; NOW</span></div>'
            f'<div style="font-family: {SERIF}; font-size: 20px; line-height: 25px; font-weight: 600; color: {INK}; margin-top: 8px;">Lunch at the harbour at one; the walk under the wall at four, once it is in shade.</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Nothing after six. The evening is open.</div>'
            + rail + fn('YOUR NOTE, THE FORECAST, THE CLIFF&rsquo;S ASPECT &middot; FIXTURE &middot; NO CTA', 8) + '</div>')

def work_receipt():
    """now_work_receipt — two lines about tomorrow's boat, checked overnight; never a list, never a card that asks."""
    def line(ok, t):
        mark = (f'<span style="width: 15px; height: 15px; border-radius: 8px; border: 1.3px solid {INK}; box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; flex: none; margin-top: 2px;"><svg width="9" height="9" viewBox="0 0 10 10" fill="none"><path d="M2 5.2L4.2 7.4L8 3.2" stroke="{INK}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>' if ok
                else f'<span style="width: 15px; height: 15px; border-radius: 8px; border: 1.3px solid {GOLD}; box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; flex: none; margin-top: 2px; font-family: {MONO}; font-size: 9px; font-weight: 700; color: {GOLD};">!</span>')
        return f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 6px 0;">{mark}<span style="font-size: 13.5px; line-height: 19px; color: {INK};">{t}</span></div>'
    return (f'<div style="background: {CARD}; border-radius: 14px; padding: 11px 14px 10px; box-shadow: 0 1px 3px rgba(27,23,20,0.06);">'
            f'<div style="display: flex; align-items: center; gap: 10px;">{kickm("TOMORROW&rsquo;S BOAT")}<span class="fn" style="margin-left: auto;">CHECKED 6:12</span></div>'
            + line(True, 'Your 11:20 to Capri boards from the far quay. Be on it by 11:05.')
            + line(True, 'The 9:40 sold out by nine last week; the 11:20 has room.')
            + fn('THE OPERATOR&rsquo;S TIMETABLE + YOUR TICKET &middot; FIXTURE &middot; TWO LINES AT MOST', 4) + '</div>')

def money_row(last=False):
    """motion_money_row — an amount, its direction, its status. A row, never a card."""
    return row(euro(), 'The cancelled Rome flight &middot; ' + mute('&euro;212 owed to you &middot; claim filed &middot; airline reviewing'), last=last)

# ---- the rest of the scroll, from existing kinds --------------------------------
def mechanism_row():
    def lane(lab, big, sub):
        return (f'<div style="flex: 1;"><div class="fn" style="color: {HINT};">{lab}</div><div style="font-family: {SERIF}; font-size: 22px; line-height: 26px; font-weight: 600; color: {INK}; margin-top: 3px;">{big}</div><div style="font-size: 12px; line-height: 16px; color: {MUTE};">{sub}</div></div>')
    return (f'<div style="display: flex; flex-direction: column;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK};">By four the walk under the wall is in the cliff&rsquo;s shade; the quay stays in the sun until six</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">The tuff face looks north-west, so the shelf below it goes into shadow first; the harbour front holds the afternoon.</div>'
            f'<div style="display: flex; gap: 18px; margin-top: 10px;">{lane("UNDER THE WALL &middot; 4 PM", "27&deg;", "in the cliff&rsquo;s shade")}{lane("THE QUAY &middot; 4 PM", "33&deg;", "full sun till six")}</div>'
            + fn('FORECAST + THE CLIFF&rsquo;S ASPECT &middot; FIXTURE', 6) + '</div>')

def ending(days, line):
    out = '<div style="margin: 40px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">'
    for lab, kind, text in days:
        if kind == 'today': m = f'<span class="daym" style="background: {INK};"></span>'; lc = INK; tc = INK
        elif kind == 'gold': m = f'<span class="daym" style="background: {GOLD};"></span>'; lc = INK; tc = INK
        elif kind == 'ink': m = f'<span class="daym" style="background: {INK};"></span>'; lc = INK; tc = INK
        else: m = '<span class="daym" style="border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;"></span>'; lc = HINT; tc = 'transparent'; text = '.'
        out += f'<div class="day"><span class="dayl" style="color: {lc};">{lab}</span>{m}<span style="font-size: 10px; color: {tc};">{text}</span></div>'
    out += '</div></div>' + f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: {INK};">{line}</div></div>'
    return out

def trip_home():
    inner = anchor('SORRENTO &middot; WEDNESDAY', '8:40 AM')
    inner += read('Sorrento. 31&deg; by two, the boat tomorrow at 11:20.', 'Day three of thirteen &middot; Rome on Monday &middot; dinner at ours the day after you land.')
    inner += gut(temporal_strip(), top=22)
    inner += gut(work_receipt(), top=14)
    inner += sect('In motion') + gut(money_row() + row(facepile(['M', 'A', 'N']), 'Dinner at ours &middot; Aug 29 &middot; ' + mute('you host &middot; Maya and Alex'), last=True))
    inner += sect('Worth knowing') + gut(mechanism_row())
    inner += sect('Continuity') + gut(row(dot('solid', GOLD), 'Nice &rarr; Rome &middot; ' + mute('days one to three &middot; 19 photographs &middot; in Life'), last=True) + door('Everything in Life'))
    inner += ending([('WED', 'today', 'today'), ('THU', 'gold', 'Capri'), ('FRI', 'h', ''), ('SAT', 'h', ''), ('SUN', 'h', ''), ('MON', 'ink', 'Rome'), ('TUE', 'h', '')], 'Tomorrow, Capri by the 11:20.')
    inner += '<div style="flex-grow: 1;"></div>' + tabbar()
    return phone_open() + inner + '</div>'

# ---- board edits ---------------------------------------------------------------
def col(phone, shead, kick, title, fnt):
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;"><div class="shead" style="color: {GOLDD}; margin-bottom: 10px;"><span>{shead}</span><span class="rule"></span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{kick}</div><div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{title}</div><div class="fn" style="line-height: 14px;">{fnt}</div></div>{phone}</div>')

def build_03():
    h = h03()
    # third selected column, appended inside the SELECTED row (the first flex row after the SELECTED head)
    i = h.find('SELECTED &middot; THE CURRENT HOME SCROLLS')
    j = h.find('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 0;">', i)
    # find the end of that row
    depth = 0; end = None
    for m in re.finditer(r'<div\b|</div>', h[j:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0: end = j + m.start(); break
    newcol = col(trip_home(), 'ON THE TRIP &middot; DAY THREE &middot; WEDNESDAY AUG 18', 'SELECTED &middot; TRIP DAY', 'The current trip-day scroll',
                 'NEW 2026-09-08, AFTER THE COMPARISON WITH &ldquo;TRIPS &middot; THE PAGE&rdquo; &middot; THREE KINDS ADMITTED: THE TEMPORAL STRIP, THE WORK RECEIPT, THE MONEY ROW (01; DELETION TEST ON 07) &middot; THE SPINE FOLDED INTO THE SEAM, CONDITIONS INTO THE MECHANISM ROW &middot; LIFE RECORD FIXTURE')
    h = h[:end] + newcol + h[end:]
    h = h.replace('Two states to build against, at their current revision. Each points to its whole encounter on 08b or 11 and its form on 09.',
                  'Three states to build against, at their current revision: day zero, the return after absence, and (new 09-08) an ordinary day on the trip. Each points to its whole encounter on 08b or 11 and its form on 09.')
    h = h.replace('Day zero before and after; then the two baseline states no revision had reached, now drawn in the current direction.',
                  'The selected scrolls first: day zero, the return after absence, and the ordinary trip day. Then the history: day zero before and after, and the two baseline states no revision had reached.')
    return h

def cell(name, grade_html, inner, prov):
    return (f'<div class="cell"><div class="lab"><span class="kn">{name}</span>{grade_html}</div>'
            f'<div style="width: 393px; background: {PAPER}; padding: 4px 0 22px 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">{inner}</div>'
            f'<div class="fn" style="color: {HINT};">{prov}</div></div>')

def build_01():
    h = open(f'{LIVE}/01.html').read()
    G = '<span class="gB">BUILD &middot; ADMITTED 09-08</span>'
    c1 = cell('now_temporal_strip', G, gut(temporal_strip(), top=8), 'AS DRAWN ON 03 &middot; THE TRIP DAY &middot; A BAND, NOT A CARD: WHAT IS TRUE RIGHT NOW AND WHEN THE DAY STOPS ASKING &middot; IN THE DOMINANT UNION; RENDERS ONLY ON A TRIP DAY WITH NO COMMITMENT, DECISION OR CHANGE')
    c2 = cell('now_work_receipt', G, gut(work_receipt(), top=8), 'AS DRAWN ON 03 &middot; THE TRIP DAY &middot; SUBJECT-FIRST (&ldquo;TOMORROW&rsquo;S BOAT&rdquo;), TWO LINES AT MOST, A CHECKED TIME, NO CTA &middot; SITS UNDER THE STRIP, NEVER ALONE; NEVER NARRATES WHAT THE PRODUCT DID')
    c3 = cell('motion_money_row', G, gut(money_row(last=True), top=8), 'AS DRAWN ON 03 &middot; THE TRIP DAY &middot; AMOUNT, DIRECTION, STATUS IN ONE ROW; THE &euro; MARK INSTEAD OF AN ICON PLATE &middot; FALLS OFF WHEN PAID, THEN ONCE AS A SINCE-YOU-LOOKED ROW')
    # insert c1+c2 after the now_temporal_posture cell(s), before now_annotated_evidence; c3 after motion_loose_end_row
    k = h.find('<div class="cell"><div class="lab"><span class="kn">now_annotated_evidence</span>')
    h = h[:k] + c1 + c2 + h[k:]
    k = h.find('<div class="cell"><div class="lab"><span class="kn">motion_all_plans_door</span>')
    h = h[:k] + c3 + h[k:]
    h = h.replace('THE HOME UNION AS DRAWN TODAY (35 KINDS) &middot; MERGED 2026-09-05', 'THE HOME UNION AS DRAWN TODAY (38 KINDS) &middot; MERGED 2026-09-05 &middot; THREE ADMITTED 2026-09-08')
    h = h.replace('One cell per kind in the 35-kind union (build manifest &sect;1.0&ndash;1.6, four kinds admitted 09-05)', 'One cell per kind in the 38-kind union (build manifest &sect;1.0&ndash;1.6; four kinds admitted 09-05, three on 09-08 after the comparison with the pre-pivot Trips page)')
    return h

def build_07():
    h = open(f'{LIVE}/07.html').read()
    td = f'style="font-size: 12.5px; line-height: 17px; color: {INK2}; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;"'
    th = f'style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.9px; color: {HINT}; text-align: left; padding: 0 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.12); font-weight: 400;"'
    rows = [
        ('now_temporal_strip', 'The temporal strip (&ldquo;Tonight&rdquo;; the page&rsquo;s highest-ranked object, priority 96)', 'Remove it and the read has to carry lunch, the walk and the open evening in one sentence, or a crown card renders for a day that has no commitment, decision or change. Neither is honest.', 'KEEPS &middot; joins the dominant union; renders only on a trip day with nothing to decide'),
        ('now_work_receipt', 'The work receipt (&ldquo;I did work while you were asleep&rdquo;, priority 82)', 'Remove it and the person checks the quay and the sold-out boat themselves. The gift is real; its cost is the temptation to narrate. Bounded: subject-first, two lines, a checked time, no CTA.', 'KEEPS, BOUNDED &middot; under the strip only; never alone, never a list'),
        ('motion_money_row', 'The ledger (&ldquo;You are owed &euro;214&rdquo;, priority 95) and the settlement receipt', 'Remove it and money reaches Home only as a wordless loose end. An amount with a direction is the plainest value on the page; a card for it is not (the Trips ledger was a crown body). Home gets the row.', 'KEEPS AS A ROW &middot; never a card; falls off when paid, then once in since-you-looked'),
        ('(the spine)', 'The day shape (&ldquo;days 4&ndash;6 are one open stretch&rdquo;, priority 93)', 'Remove it and nothing is lost that the seam does not already say: the week strip marks Capri and Rome and leaves the empty days empty.', 'FOLDED &middot; into week_shape; no kind'),
        ('(conditions)', 'The conditions receipt (&ldquo;rain from midday&rdquo;, priority 88)', 'Remove the crown version and the mechanism row carries the same fact with its cause (the cliff&rsquo;s aspect), which is the Home way of saying weather.', 'FOLDED &middot; into horizon_mechanism_row; no kind'),
        ('(near you, the offer, candidates, the table, the ladder)', 'Five Trips bodies about places and prices', 'They were relocated to Places on the Trips page itself and stay there. Home receives their result, not their browse.', 'NOT HOME &middot; Places'),
    ]
    tbl = f'<table style="border-collapse: collapse; width: 100%;"><thead><tr><th {th}>KIND</th><th {th}>WHAT THE TRIPS PAGE HAD</th><th {th}>REMOVE IT, AND WHAT IS LOST</th><th {th}>VERDICT</th></tr></thead><tbody>'
    for a, b, c, d in rows:
        tbl += f'<tr><td {td}><span style="font-family: {MONO}; font-size: 11px;">{a}</span></td><td {td}>{b}</td><td {td}>{c}</td><td {td}><b>{d.split(" &middot; ")[0]}</b> &middot; {" &middot; ".join(d.split(" &middot; ")[1:])}</td></tr>'
    tbl += '</tbody></table>'
    block = (f'<div style="display: flex; flex-direction: column; gap: 14px;"><div class="shead"><span>THE TRIP DAY &middot; 2026-09-08 &middot; THREE KINDS UNDER THE DELETION TEST</span><span class="rule"></span></div>'
             f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">The founder compared this project with the pre-pivot &ldquo;Trips &middot; The Page&rdquo; (56 frames, 27 kinds, 9 built). By kind count the unions were already comparable; what Home lacked was the state that page was built for, an ordinary day on a trip, and three objects that only earn their place there. The trip-day scroll is the third selected state on 03. Each candidate was removed from it and judged by what went missing.</div>'
             + tbl + f'<div class="fn" style="color: {HINT};">STATIC BOARD &middot; THE TRIPS PAGE&rsquo;S PRIORITIES ARE ITS OWN (trips_stack.py) AND ARE QUOTED, NOT ADOPTED &middot; THE TRIP DAY&rsquo;S WORLD FACTS (THE BOAT, THE SHADE) ARE FIXTURES</div></div>')
    k = h.find('<div class="shead"><span>HISTORY &middot; THE PHONES THE CURRENT BOARDS REPLACED</span>')
    return h[:k] + block + h[k:]

def build_00():
    h = open(f'{LIVE}/00.html').read()
    h = h.replace('Every kind in the 35-kind Home union, as drawn on the current boards; ten cells now lifted from 11; two drawer specimens remain', 'Every kind in the 38-kind Home union, as drawn on the current boards; three kinds admitted 09-08 (the temporal strip, the work receipt, the money row) after the comparison with the pre-pivot Trips page')
    h = h.replace('Four kinds admitted; the Home union is 35', 'Seven kinds admitted (four 09-05, three 09-08); the Home union is 38')
    h = h.replace('Opens with the selected current scrolls (day zero on the Life record, the return after absence); then the history:', 'Opens with the selected current scrolls (day zero on the Life record, the return after absence, and the ordinary trip day, new 09-08); then the history:')
    h = h.replace('02 and 03 open with the selected current scrolls (ordinary, quiet, and a thin-context unit study; day zero and the return after absence, on one Life-record fixture)', '02 and 03 open with the selected current scrolls (ordinary, quiet, and a thin-context unit study; day zero, the return after absence, and the trip day, on one Life-record fixture)')
    return h

# ---- measure and stamp heights ---------------------------------------------------
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
def png_rows(path):
    d = open(path, 'rb').read(); p = 8; idat = b''
    while p < len(d):
        n = struct.unpack('>I', d[p:p+4])[0]; t = d[p+4:p+8]
        if t == b'IHDR': W, H, bd, ct = struct.unpack('>IIBB', d[p+8:p+18])
        if t == b'IDAT': idat += d[p+8:p+8+n]
        p += 12 + n
    bpp = {2: 3, 6: 4}[ct]; raw = zlib.decompress(idat); stride = W * bpp; out = []; prev = bytearray(stride); i = 0
    for y in range(H):
        f = raw[i]; i += 1; line = bytearray(raw[i:i+stride]); i += stride
        if f:
            for x in range(stride):
                a = line[x-bpp] if x >= bpp else 0; b = prev[x]; c = prev[x-bpp] if x >= bpp else 0
                if f == 1: line[x] = (line[x] + a) & 255
                elif f == 2: line[x] = (line[x] + b) & 255
                elif f == 3: line[x] = (line[x] + (a + b) // 2) & 255
                elif f == 4:
                    pa = abs(b - c); pb = abs(a - c); pc = abs(a + b - 2 * c)
                    line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        out.append(bytes(line)); prev = line
    return W, H, bpp, out
def measure(path, width, guess):
    """Render at half scale, find the last non-background row, return the full-scale content height."""
    shot = path + '.m.png'
    subprocess.run([CH, '--headless=new', '--force-device-scale-factor=0.5', f'--window-size={width},{int(guess * 1.6)}', '--virtual-time-budget=12000', '--hide-scrollbars', f'--screenshot={shot}', 'file://' + os.path.abspath(path)], capture_output=True)
    W, H, bpp, R = png_rows(shot)
    bg = R[H-1][:bpp]; last = 0
    for y in range(H - 1, 0, -1):
        rw = R[y]
        if any(rw[x*bpp:x*bpp+bpp] != bg for x in range(0, W, 37)): last = y; break
    os.remove(shot)
    return (last + 1) * 2

def stamp(h, height):
    m = re.search(r'min-height: (\d{4,})px', h)
    return h.replace(m.group(0), f'min-height: {height}px', 1) if m else h

if __name__ == '__main__':
    outs = {'03 - Persona B - Back from Europe.dc.html': build_03(), '01 - Parts.dc.html': build_01(), '07 - Ledger and Decisions.dc.html': build_07(), '00 - Index.dc.html': build_00()}
    widths = {'03': 1820, '01': 1820, '07': 1820, '00': 1560}
    for name, html in outs.items():
        p = os.path.join(OUT, name); open(p, 'w').write(html)
        m = re.search(r'width: (\d{4})px; min-height: (\d{4,})px', html)
        w, g = (int(m.group(1)), int(m.group(2))) if m else (1820, 8000)
        hgt = measure(p, w + 40, g + 3000) + 60
        open(p, 'w').write(stamp(html, hgt)); print(name, 'width', w, 'height', hgt)
