"""08 - Seam with Life: the ticket at every scale from Life's pass (09B / 01A6) down to Home's row mark,
three Home phones with the borrowed elements in place, the door map, and the two rulings Home needs
before it borrows. Fixture copy only. Pass anatomy and chip grammar lifted from Vesper — Life & Anchors."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
from gen_generous import caption, col, head, FOOT, N, WEEK_SUN, ending, arow, collapsed, span
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, COLD, kept_row
from gen_generous4 import ways_card, h1_floor
from gen_merge import page, daycap, tbl, blk, STAMP, hh

OUT = os.path.join(os.path.dirname(__file__), 'merged')
VIOLET = '#7C5BA8'; HAIR = 'rgba(27,23,20,0.10)'; HAIRT = 'rgba(27,23,20,0.06)'

# ───────────────────────────── Life's glyphs (01A6 / 09B / 25) ─────────────────────────────
G = {
    'admission': 'M2.4 12.6 V5.4 Q7.5 1.4 12.6 5.4 V12.6 M5.4 12.6 V8.6 Q7.5 6.6 9.6 8.6 V12.6 M1.4 12.6 H13.6',
    'flight': 'M1.8 8.6 L13.2 3.4 L9.8 8.2 L11.4 12 L9.6 12.4 L7.4 9.2 L3.6 10.4 Z',
    'dining': 'M5 1.8 V6 M7.5 1.8 V6 M10 1.8 V6 M5 6 Q7.5 7.6 10 6 M7.5 6.8 V13.2',
    'ferry': 'M1.6 9.6 Q3.8 7.2 6 9.6 Q8.2 12 10.4 9.6 Q12.2 7.6 13.4 8.8 M4 5.6 Q6 3.6 8 5.6 Q10 7.6 12 5.6',
}
def mark(kind, size=15, op=0.62, color=INK):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 15 15" fill="none" style="flex: none; opacity: {op};"><path d="{G[kind]}" stroke="{color}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def chip(kind, text, dot=None, serif=False):
    """01A6 v3: one line, h26; mark + identity + at most one dot (ring = upcoming, green = live, grey = unused)."""
    d = ''
    if dot == 'ring': d = f'<span style="width: 6px; height: 6px; border-radius: 3px; border: 1.3px solid {PLAN}; box-sizing: border-box; flex: none;"></span>'
    if dot == 'live': d = f'<span style="width: 5px; height: 5px; border-radius: 3px; background: {GREEN}; flex: none;"></span>'
    if dot == 'unused': d = f'<span style="width: 5px; height: 5px; border-radius: 3px; background: {GHOST}; opacity: 0.7; flex: none;"></span>'
    t = (f'<span style="{SERIF} font-size: 11px; font-weight: 600; white-space: nowrap; position: relative; top: -0.5px;">{text}</span>' if serif
         else f'<span style="{MONO} font-size: 8.5px; font-weight: 700; letter-spacing: 0.5px; color: {INK}; white-space: nowrap;">{text}</span>')
    return (f'<span style="height: 26px; border-radius: 13px; background: {CARD}; border: 1px solid {HAIR}; display: inline-flex; align-items: center; gap: 6px; padding: 0 10px; flex: none; box-sizing: border-box; box-shadow: 0 1px 2px rgba(27,23,20,0.05);">'
            + mark(kind, 12, 0.7) + t + d + '</span>')

def row_mark(kind, text, last=False, muted=False):
    """Home's 44px row (§12.7 g) whose subject is a kept object: the lead is Life's kind mark, not a status dot."""
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.06);' if last else ''
    return (f'<div class="row" style="padding: 8px 0;{bb}">{mark(kind)}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {MUTE if muted else INK};">{text}</span>{CHEV}</div>')

def kept_chip_row(kind, text, tail='in Life'):
    return (f'<div class="row" style="padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span class="kickm" style="flex: none;">KEPT</span>{chip(kind, text, "ring")}'
            f'<span style="font-size: 13px; color: {MUTE}; flex: 1;">{tail}</span><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Undo</span></div>')

# ───────────────────────────── the admission pass (09B signature) ─────────────────────────────
def truths(items, lbl_col=GHOST):
    return '<div style="display: flex; gap: 26px;">' + ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px;"><span style="{MONO} font-size: 8px; font-weight: 700; letter-spacing: 1px; color: {lbl_col};">{l}</span><span style="{MONO} font-size: 13px; font-weight: 500; color: {INK};">{v}</span></div>' for l, v in items) + '</div>'

def pass_admission(w=349, kick='ADMISSION &middot; THE HALL', date='FRIDAY', name='The Hall', sub='Friday &middot; doors 8', tr=(('DOORS', '8:00'), ('ENTRY', 'GENERAL'), ('NR', '2210')),
                   band_l='ADMIT ONE', band_r='UPCOMING', band_r_col=GHOST, status=None, sample=False, extra='', elevated=False, pad=18, name_size=24):
    """Life 09B: corner cut + admit band. status = (color, text) renders Home's status line above the name when the pass is the live crown."""
    shadow = '0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06)' if elevated else '0 2px 8px rgba(27,23,20,0.08)'
    border = f'1.5px dashed rgba(27,23,20,0.35)' if sample else f'1px solid {HAIR}'
    out = (f'<div style="width: {w}px; background: {CARD}; border: {border}; border-radius: {18 if elevated else 14}px; box-shadow: {shadow}; overflow: hidden; position: relative; box-sizing: border-box; '
           f'clip-path: polygon(0 0, calc(100% - 22px) 0, 100% 22px, 100% 100%, 0 100%);">')
    out += f'<div style="padding: 16px {pad}px 0 {pad}px; display: flex; align-items: baseline; gap: 8px;">'
    if sample: out += f'<span style="font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {MUTE}; border: 1px dashed rgba(27,23,20,0.35); border-radius: 999px; padding: 2px 7px; flex: none;">SAMPLE</span>'
    out += f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {VIOLET};">{kick}</span><span style="{MONO} font-size: 10px; font-weight: 500; letter-spacing: 0.8px; color: {GHOST}; margin-left: auto; white-space: nowrap;">{date}</span></div>'
    if status:
        out += f'<div style="padding: 12px {pad}px 0 {pad}px; display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {status[0]}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {status[0]};">{status[1]}</span></div>'
    out += (f'<div style="padding: {8 if status else 12}px {pad}px 0 {pad}px; display: flex; flex-direction: column; gap: 2px;"><span style="{SERIF} font-size: {name_size}px; line-height: {name_size + 4}px; font-weight: 600;">{name}</span>'
            f'<span style="font-size: 12px; line-height: 16px; color: {MUTE};">{sub}</span></div>')
    out += f'<div style="padding: 14px {pad}px 16px {pad}px;">{truths(tr)}</div>'
    out += extra
    out += (f'<div style="background: rgba(124,91,168,0.10); border-top: 1px solid {HAIRT}; display: flex; align-items: center; padding: 9px {pad}px;">'
            f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 2.5px; color: {VIOLET};">{band_l}</span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {band_r_col}; margin-left: auto;">{band_r}</span></div>')
    return out + '</div>'

def live_pass_crown():
    """Friday, the live window: the pass IS the crown (01A: 'live = the pass gains elevation, oxblood threshold, live facts replace static ones. Same anatomy'). The consequence sits between the truths and the admit band."""
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT}; margin: 0 0 0 0;">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">Leave from work by 7:05, not from home</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">After ten the trains skip your stop; the way home is a surface route, 25 minutes longer.</div>'
             + span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=313)
             + f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Open the way there</span></div>'
             f'<div class="fn">YOUR TICKET + THE HALL&rsquo;S LATE SERVICE &middot; CHECKED 5:40 &middot; NOTHING BOOKED</div></div>')
    return f'<div style="margin: 22px 22px 0 22px;">' + pass_admission(w=349, date='TONIGHT', sub='Doors 8 &middot; set times posted at 6', tr=(('DOORS', '8:00'), ('LEAVE BY', '7:05'), ('WAY HOME', '+25 MIN')),
                                                              band_r='TONIGHT', band_r_col=OX, status=(OX, 'TONIGHT &middot; DOORS 8:00'), extra=extra, elevated=True) + '</div>'

# ───────────────────────────── the three phones ─────────────────────────────
def sunday_seam():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(ways_card('Today', [
        ('The sesame loaf, then the water', 'Maya, Friday: &ldquo;Sundays only &mdash; go before eleven or it&rsquo;s gone.&rdquo; Bakery by 10:30; low water on the pier nine minutes on.', 'MORNING &middot; 10:30 &rarr; 1:40 &middot; MAYA&rsquo;S SHARE, IN PLACES'),
        ('The flood line, walked at low water', 'The granite kerbs show where the gates&rsquo; protection ends.', 'AFTERNOON &middot; 1:40&ndash;4'),
    ]), top=22)
    rows = (arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you'])
            + arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D'])
            + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
            + row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed', last=True))
    inner += sect('In motion') + gut(rows)
    inner += sect('Worth knowing') + gut(COLD())
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("admission", "THE HALL", "ring")}{chip("dining", "Alex&rsquo;s birthday", None, serif=True)}</div>' + meta('LIFE &middot; TWO KEPT OBJECTS THIS WEEK &middot; CHIPS ARE PRINT, NOT ROWS', 8), top=32)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def friday_live():
    inner = anchor_row('NEW YORK &middot; FRIDAY', '5:40 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">The show tonight. Leave from work by 7:05.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Clear, 41&deg; by ten &middot; the L is single-tracking after eleven &middot; Alex&rsquo;s birthday tomorrow.</div></div>')
    inner += live_pass_crown()
    inner += sect('In motion') + gut(arow('Alex&rsquo;s birthday &middot; tomorrow, the park at 6:30 &middot; <span style="color: #6E6862;">settled &middot; 4 going</span>', avatars=['A', 'M', 'you'])
                                      + arow('Dana &middot; Saturday the 19th &middot; <span style="color: #6E6862;">unchanged</span>', avatars=['D'], last=True))
    inner += gut(collapsed('THE REST OF FRIDAY &middot; STILL HERE', ['After the show: the noodle bar Maya sent, open till one', 'Tonight&rsquo;s cold on the river side', 'Open House registration closed Tuesday']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'tonight', OX), ('SAT', dm('av:A', ''), 'Alex', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Doors at eight. Tomorrow, the park at 6:30.')
    return phone(inner, 0)

def first_open_seam():
    """04's first open with Life's admission signature as the sample input (L2, dashed, stamped) in place of the hand-drawn stub."""
    stub = pass_admission(w=168, kick='ADMISSION', date='', name='The Hall', sub='Friday &middot; doors 8', tr=(('DOORS', '8:00'),), band_l='ADMIT ONE', band_r='', sample=True, pad=12, name_size=17)
    smp = g3.sample_card('A MADE-UP TICKET, READ THE WAY YOURS WOULD BE', stub, 'Doors at 8. Arrive by 8:40 and you miss nothing.',
                         span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=349),
                         ['Coat check yes &middot; set times posted by the hall the day before', 'After ten, the way home from the hall is a surface route: 25 minutes longer'],
                         [('How it&rsquo;s read', GOLDD), ('Try with yours', INK)])
    html = g3.h3v2_first()
    old = g3.sample_ticket()
    assert old in html
    html = html.replace(old, smp, 1)
    # the return after one contribution: the kept row becomes the chip
    return html

def return_seam():
    html = g3.h3v2_return()
    old = kept_row('Your ticket &middot; Friday &middot; in Life')
    assert old in html
    html = html.replace(old, kept_chip_row('admission', 'THE HALL', 'Friday &middot; in Life'), 1)
    return html

# ───────────────────────────── the flight pass (09B flight signature · 01A states) ─────────────────────────────
def barcode(color=INK):
    xs = [(0,2),(4,1),(7,3),(12,1),(15,2),(19,1),(22,3),(27,2),(31,1),(34,2),(38,3),(43,1),(46,2),(50,1),(53,3),(58,2),(62,1),(65,2),(69,1),(72,3),(77,1),(80,2),(84,1),(87,3)]
    return '<svg width="92" height="26" viewBox="0 0 92 26">' + ''.join(f'<rect x="{x}" y="0" width="{w}" height="26" fill="{color}" opacity="0.75"/>' for x, w in xs) + '</svg>'

def perforation():
    return (f'<div style="position: relative; height: 1px; margin: 2px 0 0 0;"><div style="position: absolute; left: 10px; right: 10px; top: 0; border-top: 1.5px dashed rgba(27,23,20,0.22);"></div>'
            f'<span style="position: absolute; left: -8px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER}; border: 1px solid {HAIR}; box-sizing: border-box;"></span>'
            f'<span style="position: absolute; right: -8px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER}; border: 1px solid {HAIR}; box-sizing: border-box;"></span></div>')

def pass_flight(state='prospective', w=349, extra='', elevated=False):
    """Life 09B flight signature: kick row · city pair · truths · horizontal perforation · stub. States per 01A: prospective (committed, quiet), live (oxblood, provider facts), flown (muted, occurrence-supported)."""
    shadow = '0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06)' if elevated else '0 2px 8px rgba(27,23,20,0.08)'
    kick_col = MUTE if state != 'live' else INK
    date = {'prospective': 'JUN 12 2026', 'live': 'TODAY', 'flown': 'JUN 12 2026'}[state]
    out = f'<div style="width: {w}px; background: {CARD}; border: 1px solid {HAIR}; border-radius: {18 if elevated else 14}px; box-shadow: {shadow}; overflow: hidden; position: relative; box-sizing: border-box;">'
    out += (f'<div style="padding: 16px 18px 0 18px; display: flex; align-items: baseline;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {kick_col};">FLIGHT &middot; TAP 214</span>'
            f'<span style="{MONO} font-size: 10px; font-weight: 500; letter-spacing: 0.8px; color: {OX if state == "live" else GHOST}; margin-left: auto;">{date}</span></div>')
    if state == 'live':
        out += f'<div style="padding: 12px 18px 0 18px; display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">BOARDING 6:05 &middot; LEAVE BY 3:40</span></div>'
    big = 32 if state != 'flown' else 22
    out += (f'<div style="padding: {10 if state == "live" else 14}px 18px 0 18px; display: flex; align-items: center; gap: 14px;">'
            f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="{SERIF} font-size: {big}px; line-height: {big + 2}px; font-weight: 600; letter-spacing: -0.5px;">JFK</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">New York</span></div>'
            + mark('flight', 15, 0.62).replace('flex: none;', 'flex: none; margin-top: -8px;')
            + f'<div style="display: flex; flex-direction: column; gap: 1px; margin-left: auto; text-align: right;"><span style="{SERIF} font-size: {big}px; line-height: {big + 2}px; font-weight: 600; letter-spacing: -0.5px;">LIS</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">Lisbon</span></div></div>')
    tr = {'prospective': (('DEPART', '18:45'), ('ARRIVE', '06:55 +1'), ('SEAT', '24A'), ('CONF', 'TP7Q2K')),
          'live': (('GATE', 'B22'), ('SEAT', '24A'), ('BOARDS', '18:05'), ('DEPART', '18:45')),
          'flown': (('DEPART', '18:45'), ('LANDED', '06:58'), ('SEAT', '24A'))}[state]
    out += f'<div style="padding: 16px 18px 18px 18px;">{truths(tr)}</div>'
    out += extra
    out += perforation()
    if state == 'prospective':
        stub = (f'<span style="width: 6px; height: 6px; border-radius: 3px; background: {PLAN}; flex: none;"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {PLAN};">COMMITTED &middot; JUN 12</span>'
                f'<span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">In the Lisbon plan</span>{ARROW}')
    elif state == 'live':
        stub = f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">CURRENT AS OF 3:12 &middot; GATE FROM PROVIDER</span><span style="margin-left: auto;">{barcode()}</span>'
    else:
        stub = f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">FLOWN &middot; JUN 13 &middot; 06:58</span><span style="margin-left: auto;">{barcode()}</span>'
    out += f'<div style="padding: 13px 18px 15px 18px; display: flex; align-items: center; gap: 7px;">{stub}</div>'
    return out + '</div>'

def live_flight_crown():
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT};">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">Leave now: the A train, then the AirTrain</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">Sixty-two minutes door to gate; security at Terminal 4 is running 30. Bag drop closes at 5:45.</div>'
             + span('DOOR &rarr; GATE &middot; 3:40&ndash;4:45', 40, 150, 'BOARDS 6:05', start='3 PM', end='7', w=313)
             + f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Open the way there</span></div>'
             f'<div class="fn">YOUR TICKET + PROVIDER GATE + SERVICE READ &middot; RE-CHECKS EVERY FEW MINUTES UNTIL BOARDING</div></div>')
    return '<div style="margin: 22px 22px 0 22px;">' + pass_flight('live', extra=extra, elevated=True) + '</div>'

def lisbon_days(today=None):
    days = [('FRI', 'arrive'), ('SAT', 'open'), ('SUN', 'Sintra'), ('MON', 'open'), ('TUE', 'free day'), ('WED', 'home')]
    out = []
    for d, s in days:
        m = dm('solid', GOLD) if d in ('FRI', 'WED') else (dm('solid', INK) if d == 'SUN' else (dm('dashed', MUTE) if d == 'TUE' else dm('hollow', '')))
        out.append((d, m, s, INK if d in ('FRI', 'SUN', 'WED') else MUTE))
    return g4.days_strip(out)

# ───────────────────────────── the flight arc on Home ─────────────────────────────
def booked_phone():
    """Tuesday, nine weeks out, the evening she booked. Life 01A prospective: quiet, no countdown, no checklist; the plan owns urgency later."""
    inner = anchor_row('NEW YORK &middot; TUESDAY', '9:12 PM')
    inner += orientation('Lisbon is booked. Nothing else changes tonight.', 'Nine weeks out &middot; the stay in Alfama still closes Friday &middot; the show this Friday.')
    inner += gut(kept_chip_row('flight', 'JFK&rarr;LIS', 'Jun 12 &middot; from the booking email &middot; in Life'), top=22)
    inner += gut(g4.trip_card('LISBON &middot; JUNE 12&ndash;17 &middot; FORMING', 'Your flight is booked; three seats are still held until Friday. The stay in Alfama is the one open decision.',
                              'Maya asked for a kitchen; Alex asked to keep one day free. Dana and Theo have not answered; the plan does not wait on them.',
                              lisbon_days(), people=g5.facepile(['you', 'M', 'A', 'J'], 24, -7) + f'<span style="font-size: 13px; color: {MUTE};">+ Dana, Theo &middot; invited</span>',
                              meta_t='YOUR FLIGHT BOOKED &middot; 3 SEATS HELD &middot; 2 STAYS OPEN &middot; STAY DECISION BY FRI', door_text='The trip'), top=16)
    inner += sect('In motion') + gut(row('Alfama stay &middot; <span style="color: #6E6862;">two options, sleeps six &middot; decide by Friday</span>', mark='dashed')
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
                                     + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(u2('Two stays sleep six; only one has the kitchen Maya asked for', 'The other is nearer the tram and cheaper by a night. Neither needs a card tonight.', meta_t='FROM THE TWO HELD OPTIONS + TWO CONTRIBUTIONS &middot; FIXTURE'))
    inner += ending([('TUE', dm('solid', INK), 'today', INK), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('dashed', OX), 'stay?', OX), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE)],
                    'Friday the show, and the stay. Lisbon in nine weeks.')
    return phone(inner, 0)

def eve_phone():
    """Thursday June 11, the day before. Not the live window: the pass stays below L2. The crown is Home's consequence with the ticket as one kick line and a door."""
    inner = anchor_row('NEW YORK &middot; THURSDAY', '8:10 PM')
    inner += orientation('Lisbon tomorrow. JFK at 6:45; leave Brooklyn by 3:40.', 'Clear tomorrow &middot; six going, six booked &middot; the stay confirmed, check-in from three.')
    ident = (f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px;">{mark("flight", 13, 0.7)}<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE};">FLIGHT &middot; TAP 214 &middot; JFK&rarr;LIS</span>'
             f'<span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">The ticket</span>{ARROW}</div>')
    inner += crown(PLAN, 'TOMORROW &middot; DEPARTS 6:45 PM', 'Leave Brooklyn by 3:40. Check-in is open now.', 'Terminal 4 security runs 25 to 40 minutes after four; bag drop closes at 5:45. The A train is running normally.',
                   ident + span('DOOR &rarr; GATE &middot; 3:40&ndash;4:45', 40, 150, 'BOARDS 6:05', start='3 PM', end='7', w=317), cta='Check in', fn='YOUR TICKET + THE AIRLINE&rsquo;S CHECK-IN WINDOW &middot; GATE NOT YET POSTED')
    inner += sect('In motion') + gut(arow('Lisbon &middot; six going &middot; <span style="color: #6E6862;">Maya and Alex on the 8:10, land 9:05 &middot; Dana and Theo Saturday</span>', avatars=['you', 'M', 'A', 'J', 'D', 'T'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">confirmed &middot; check-in from 3 &middot; the key is a code</span>', mark='solid', color=GOLD, last=True))
    inner += sect('Worth knowing') + gut('<div>' + fact('JFK &middot; TERMINAL 4 &middot; AFTER 4 PM', 'Security 25 to 40 minutes; the AirTrain from Howard Beach runs every eight.', last=True) + '</div>')
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("flight", "JFK&rarr;LIS", "ring")}{chip("admission", "MUSEO", "ring")}</div>' + meta('LIFE &middot; THE FLIGHT, THE PALACE TICKETS &middot; BOTH UPCOMING', 8), top=32)
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'JFK', INK), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE)],
                    'Tomorrow, JFK at 6:45. Sunday, Sintra.')
    return phone(inner, 0)

def live_flight_phone():
    """Friday June 12, 3:12 PM: the live window. The pass is the crown; provider facts replace static ones; everything else folds."""
    inner = anchor_row('NEW YORK &middot; FRIDAY', '3:12 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Leave now. Boarding at 6:05 from gate B22.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">The A train is running normally &middot; security at Terminal 4 is 30 minutes &middot; Maya and Alex are on the 8:10.</div></div>')
    inner += live_flight_crown()
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, land 9:05 &middot; they know your flight</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the key is a code</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2', 'What Alfama&rsquo;s market sells on Saturdays']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'JFK', OX), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Gate B22 by 4:45. Lisbon at 6:55 tomorrow.')
    return phone(inner, 0)

def flight_ladder():
    def step(k, t, body, spec):
        return (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">{k}</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">{body}</div><div style="padding-top: 8px;">{spec}</div></div>')
    s1 = step('STATE 1 &middot; PROSPECTIVE &middot; NINE WEEKS OUT', 'The pass exists; the plan owns urgency', 'Life 01A: quiet, no countdown, no checklist. On Home this is one KEPT receipt on the evening it was booked, then a chip under the Life door and a mark on the trip&rsquo;s row. The pass itself never renders on Home before its window.',
              f'<div style="display: flex; justify-content: center;">{pass_flight("prospective")}</div>')
    s2 = step('STATE 2 &middot; THE DAY BEFORE &middot; NOT YET THE WINDOW', 'Home&rsquo;s crown, with the ticket as one line', 'The consequence is Home&rsquo;s (leave by, check-in, bag drop); the gate is not posted, so no provider truth is claimed. The ticket appears as its kick line with a door; the pass stays at L1 behind it.',
              f'<div style="display: flex; justify-content: center;">{chip("flight", "JFK&rarr;LIS", "ring")}</div>')
    s3 = step('STATE 3 &middot; LIVE &middot; THE DAY OF', 'The pass gains elevation and becomes the crown', 'Oxblood threshold; gate, seat, boarding from the provider; the consequence and one ask between the truths and the tear; the stub says when it was last true. Everything else on the page folds.',
              f'<div style="display: flex; justify-content: center;">{live_flight_crown().replace("margin: 22px 22px 0 22px", "margin: 0")}</div>')
    s4 = step('STATE 4 &middot; FLOWN &middot; IN LIFE, NOT ON HOME', 'Occurrence-supported print', 'Boarding scan and arrival position support FLOWN; operational identifiers drop. Life keeps this; Home&rsquo;s next open is Lisbon on landing (05, day three) or day zero back in New York (03).',
              f'<div style="display: flex; justify-content: center;">{pass_flight("flown")}</div>')
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('LIFE &rarr; HOME &middot; THE FLIGHT', 'Booked, imminent, live, flown', 'FOUR STATES &middot; ONE ANATOMY &middot; LIFE 01A / 09B &middot; HOME RENDERS THE PASS ONLY IN STATE 3')
            + s1 + s2 + s3 + s4 + '</div>')

FLIGHT_NOTES = notecol('What a flight does to Home, and does not', [
    ('BOOKED &middot; ONE RECEIPT, THEN QUIET', N('The booking email is brought or forwarded (Life 20F); Home&rsquo;s next open shows one KEPT receipt with Undo and the trip card updated (&ldquo;your flight is booked; three seats still held&rdquo;). No crown: nothing operational is at stake for nine weeks. No countdown, no packing list, no &ldquo;prepare for your trip&rdquo; module. Between booking and the day before, the flight is a chip under the Life door and a mark on the trip row, and that is all.')),
    ('THE DAY BEFORE &middot; HOME&rsquo;S CONSEQUENCE, NOT THE PASS', N('The crown is a commitment crown in the planning register: leave by, check-in open, bag drop, security estimate, one ask (check in). The ticket is present as one kick line with a door. Gate and seat are not shown because the gate is not posted; Home claims only what a source supports, the same law as the pass&rsquo;s stub.')),
    ('THE DAY OF &middot; THE PASS IS THE CROWN', N('Life&rsquo;s live state, in Home&rsquo;s live window: the pass elevates, oxblood, provider facts replace static ones, &ldquo;current as of&rdquo; on the stub. Priority law from 02 Thursday applies: one ask, rows unchanged, the rest folded to reachable titles. The seat law holds: while Home owns this delivery, Life&rsquo;s object page shows the same pass but no Return.')),
    ('AFTER &middot; FLOWN LEAVES HOME', N('Once the flight is occurrence-supported, the pass compresses under the journey in Life (01A state 3) and Home shows the next thing: Lisbon on landing. Home never shows FLOWN; the record does not congratulate itself.')),
    ('PRODUCTION', N('Structured state (the ticket from the email, the Trip), two service reads (check-in window; gate and transit on the day), one route. No prose is generated; the truths are the provider&rsquo;s and the stub says when they were last true. Every number here is a fixture.')),
], w=520)

# ───────────────────────────── the flight pass (09B flight signature · 01A states) ─────────────────────────────
def barcode(color=INK):
    xs = [(0,2),(4,1),(7,3),(12,1),(15,2),(19,1),(22,3),(27,2),(31,1),(34,2),(38,3),(43,1),(46,2),(50,1),(53,3),(58,2),(62,1),(65,2),(69,1),(72,3),(77,1),(80,2),(84,1),(87,3)]
    return '<svg width="92" height="26" viewBox="0 0 92 26">' + ''.join(f'<rect x="{x}" y="0" width="{w}" height="26" fill="{color}" opacity="0.75"/>' for x, w in xs) + '</svg>'

def perforation():
    return (f'<div style="position: relative; height: 1px; margin: 2px 0 0 0;"><div style="position: absolute; left: 10px; right: 10px; top: 0; border-top: 1.5px dashed rgba(27,23,20,0.22);"></div>'
            f'<span style="position: absolute; left: -8px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER}; border: 1px solid {HAIR}; box-sizing: border-box;"></span>'
            f'<span style="position: absolute; right: -8px; top: -8px; width: 16px; height: 16px; border-radius: 8px; background: {PAPER}; border: 1px solid {HAIR}; box-sizing: border-box;"></span></div>')

def pass_flight(state='prospective', w=349, extra='', elevated=False):
    """Life 09B flight signature: kick row · city pair · truths · horizontal perforation · stub. States per 01A: prospective (committed, quiet), live (oxblood, provider facts), flown (muted, occurrence-supported)."""
    shadow = '0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06)' if elevated else '0 2px 8px rgba(27,23,20,0.08)'
    kick_col = MUTE if state != 'live' else INK
    date = {'prospective': 'JUN 12 2026', 'live': 'TODAY', 'flown': 'JUN 12 2026'}[state]
    out = f'<div style="width: {w}px; background: {CARD}; border: 1px solid {HAIR}; border-radius: {18 if elevated else 14}px; box-shadow: {shadow}; overflow: hidden; position: relative; box-sizing: border-box;">'
    out += (f'<div style="padding: 16px 18px 0 18px; display: flex; align-items: baseline;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {kick_col};">FLIGHT &middot; TAP 214</span>'
            f'<span style="{MONO} font-size: 10px; font-weight: 500; letter-spacing: 0.8px; color: {OX if state == "live" else GHOST}; margin-left: auto;">{date}</span></div>')
    if state == 'live':
        out += f'<div style="padding: 12px 18px 0 18px; display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">BOARDING 6:05 &middot; LEAVE BY 3:40</span></div>'
    big = 32 if state != 'flown' else 22
    out += (f'<div style="padding: {10 if state == "live" else 14}px 18px 0 18px; display: flex; align-items: center; gap: 14px;">'
            f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="{SERIF} font-size: {big}px; line-height: {big + 2}px; font-weight: 600; letter-spacing: -0.5px;">JFK</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">New York</span></div>'
            + mark('flight', 15, 0.62).replace('flex: none;', 'flex: none; margin-top: -8px;')
            + f'<div style="display: flex; flex-direction: column; gap: 1px; margin-left: auto; text-align: right;"><span style="{SERIF} font-size: {big}px; line-height: {big + 2}px; font-weight: 600; letter-spacing: -0.5px;">LIS</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">Lisbon</span></div></div>')
    tr = {'prospective': (('DEPART', '18:45'), ('ARRIVE', '06:55 +1'), ('SEAT', '24A'), ('CONF', 'TP7Q2K')),
          'live': (('GATE', 'B22'), ('SEAT', '24A'), ('BOARDS', '18:05'), ('DEPART', '18:45')),
          'flown': (('DEPART', '18:45'), ('LANDED', '06:58'), ('SEAT', '24A'))}[state]
    out += f'<div style="padding: 16px 18px 18px 18px;">{truths(tr)}</div>'
    out += extra
    out += perforation()
    if state == 'prospective':
        stub = (f'<span style="width: 6px; height: 6px; border-radius: 3px; background: {PLAN}; flex: none;"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {PLAN};">COMMITTED &middot; JUN 12</span>'
                f'<span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">In the Lisbon plan</span>{ARROW}')
    elif state == 'live':
        stub = f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">CURRENT AS OF 3:12 &middot; GATE FROM PROVIDER</span><span style="margin-left: auto;">{barcode()}</span>'
    else:
        stub = f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">FLOWN &middot; JUN 13 &middot; 06:58</span><span style="margin-left: auto;">{barcode()}</span>'
    out += f'<div style="padding: 13px 18px 15px 18px; display: flex; align-items: center; gap: 7px;">{stub}</div>'
    return out + '</div>'

def live_flight_crown():
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT};">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">Leave now: the A train, then the AirTrain</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">Sixty-two minutes door to gate; security at Terminal 4 is running 30. Bag drop closes at 5:45.</div>'
             + span('DOOR &rarr; GATE &middot; 3:40&ndash;4:45', 40, 150, 'BOARDS 6:05', start='3 PM', end='7', w=313)
             + f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Open the way there</span></div>'
             f'<div class="fn">YOUR TICKET + PROVIDER GATE + SERVICE READ &middot; RE-CHECKS EVERY FEW MINUTES UNTIL BOARDING</div></div>')
    return '<div style="margin: 22px 22px 0 22px;">' + pass_flight('live', extra=extra, elevated=True) + '</div>'

def lisbon_days(today=None):
    days = [('FRI', 'arrive'), ('SAT', 'open'), ('SUN', 'Sintra'), ('MON', 'open'), ('TUE', 'free day'), ('WED', 'home')]
    out = []
    for d, s in days:
        m = dm('solid', GOLD) if d in ('FRI', 'WED') else (dm('solid', INK) if d == 'SUN' else (dm('dashed', MUTE) if d == 'TUE' else dm('hollow', '')))
        out.append((d, m, s, INK if d in ('FRI', 'SUN', 'WED') else MUTE))
    return g4.days_strip(out)

# ───────────────────────────── the flight arc on Home ─────────────────────────────
def booked_phone():
    """Tuesday, nine weeks out, the evening she booked. Life 01A prospective: quiet, no countdown, no checklist; the plan owns urgency later."""
    inner = anchor_row('NEW YORK &middot; TUESDAY', '9:12 PM')
    inner += orientation('Lisbon is booked. Nothing else changes tonight.', 'Nine weeks out &middot; the stay in Alfama still closes Friday &middot; the show this Friday.')
    inner += gut(kept_chip_row('flight', 'JFK&rarr;LIS', 'Jun 12 &middot; from the booking email &middot; in Life'), top=22)
    inner += gut(g4.trip_card('LISBON &middot; JUNE 12&ndash;17 &middot; FORMING', 'Your flight is booked; three seats are still held until Friday. The stay in Alfama is the one open decision.',
                              'Maya asked for a kitchen; Alex asked to keep one day free. Dana and Theo have not answered; the plan does not wait on them.',
                              lisbon_days(), people=g5.facepile(['you', 'M', 'A', 'J'], 24, -7) + f'<span style="font-size: 13px; color: {MUTE};">+ Dana, Theo &middot; invited</span>',
                              meta_t='YOUR FLIGHT BOOKED &middot; 3 SEATS HELD &middot; 2 STAYS OPEN &middot; STAY DECISION BY FRI', door_text='The trip'), top=16)
    inner += sect('In motion') + gut(row('Alfama stay &middot; <span style="color: #6E6862;">two options, sleeps six &middot; decide by Friday</span>', mark='dashed')
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
                                     + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(u2('Two stays sleep six; only one has the kitchen Maya asked for', 'The other is nearer the tram and cheaper by a night. Neither needs a card tonight.', meta_t='FROM THE TWO HELD OPTIONS + TWO CONTRIBUTIONS &middot; FIXTURE'))
    inner += ending([('TUE', dm('solid', INK), 'today', INK), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('dashed', OX), 'stay?', OX), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE)],
                    'Friday the show, and the stay. Lisbon in nine weeks.')
    return phone(inner, 0)

def eve_phone():
    """Thursday June 11, the day before. Not the live window: the pass stays below L2. The crown is Home's consequence with the ticket as one kick line and a door."""
    inner = anchor_row('NEW YORK &middot; THURSDAY', '8:10 PM')
    inner += orientation('Lisbon tomorrow. JFK at 6:45; leave Brooklyn by 3:40.', 'Clear tomorrow &middot; six going, six booked &middot; the stay confirmed, check-in from three.')
    ident = (f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px;">{mark("flight", 13, 0.7)}<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE};">FLIGHT &middot; TAP 214 &middot; JFK&rarr;LIS</span>'
             f'<span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">The ticket</span>{ARROW}</div>')
    inner += crown(PLAN, 'TOMORROW &middot; DEPARTS 6:45 PM', 'Leave Brooklyn by 3:40. Check-in is open now.', 'Terminal 4 security runs 25 to 40 minutes after four; bag drop closes at 5:45. The A train is running normally.',
                   ident + span('DOOR &rarr; GATE &middot; 3:40&ndash;4:45', 40, 150, 'BOARDS 6:05', start='3 PM', end='7', w=317), cta='Check in', fn='YOUR TICKET + THE AIRLINE&rsquo;S CHECK-IN WINDOW &middot; GATE NOT YET POSTED')
    inner += sect('In motion') + gut(arow('Lisbon &middot; six going &middot; <span style="color: #6E6862;">Maya and Alex on the 8:10, land 9:05 &middot; Dana and Theo Saturday</span>', avatars=['you', 'M', 'A', 'J', 'D', 'T'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">confirmed &middot; check-in from 3 &middot; the key is a code</span>', mark='solid', color=GOLD, last=True))
    inner += sect('Worth knowing') + gut('<div>' + fact('JFK &middot; TERMINAL 4 &middot; AFTER 4 PM', 'Security 25 to 40 minutes; the AirTrain from Howard Beach runs every eight.', last=True) + '</div>')
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("flight", "JFK&rarr;LIS", "ring")}{chip("admission", "MUSEO", "ring")}</div>' + meta('LIFE &middot; THE FLIGHT, THE PALACE TICKETS &middot; BOTH UPCOMING', 8), top=32)
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'JFK', INK), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE)],
                    'Tomorrow, JFK at 6:45. Sunday, Sintra.')
    return phone(inner, 0)

def live_flight_phone():
    """Friday June 12, 3:12 PM: the live window. The pass is the crown; provider facts replace static ones; everything else folds."""
    inner = anchor_row('NEW YORK &middot; FRIDAY', '3:12 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Leave now. Boarding at 6:05 from gate B22.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">The A train is running normally &middot; security at Terminal 4 is 30 minutes &middot; Maya and Alex are on the 8:10.</div></div>')
    inner += live_flight_crown()
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, land 9:05 &middot; they know your flight</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the key is a code</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2', 'What Alfama&rsquo;s market sells on Saturdays']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'JFK', OX), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Gate B22 by 4:45. Lisbon at 6:55 tomorrow.')
    return phone(inner, 0)

def flight_ladder():
    def step(k, t, body, spec):
        return (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">{k}</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">{body}</div><div style="padding-top: 8px;">{spec}</div></div>')
    s1 = step('STATE 1 &middot; PROSPECTIVE &middot; NINE WEEKS OUT', 'The pass exists; the plan owns urgency', 'Life 01A: quiet, no countdown, no checklist. On Home this is one KEPT receipt on the evening it was booked, then a chip under the Life door and a mark on the trip&rsquo;s row. The pass itself never renders on Home before its window.',
              f'<div style="display: flex; justify-content: center;">{pass_flight("prospective")}</div>')
    s2 = step('STATE 2 &middot; THE DAY BEFORE &middot; NOT YET THE WINDOW', 'Home&rsquo;s crown, with the ticket as one line', 'The consequence is Home&rsquo;s (leave by, check-in, bag drop); the gate is not posted, so no provider truth is claimed. The ticket appears as its kick line with a door; the pass stays at L1 behind it.',
              f'<div style="display: flex; justify-content: center;">{chip("flight", "JFK&rarr;LIS", "ring")}</div>')
    s3 = step('STATE 3 &middot; LIVE &middot; THE DAY OF', 'The pass gains elevation and becomes the crown', 'Oxblood threshold; gate, seat, boarding from the provider; the consequence and one ask between the truths and the tear; the stub says when it was last true. Everything else on the page folds.',
              f'<div style="display: flex; justify-content: center;">{live_flight_crown().replace("margin: 22px 22px 0 22px", "margin: 0")}</div>')
    s4 = step('STATE 4 &middot; FLOWN &middot; IN LIFE, NOT ON HOME', 'Occurrence-supported print', 'Boarding scan and arrival position support FLOWN; operational identifiers drop. Life keeps this; Home&rsquo;s next open is Lisbon on landing (05, day three) or day zero back in New York (03).',
              f'<div style="display: flex; justify-content: center;">{pass_flight("flown")}</div>')
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('LIFE &rarr; HOME &middot; THE FLIGHT', 'Booked, imminent, live, flown', 'FOUR STATES &middot; ONE ANATOMY &middot; LIFE 01A / 09B &middot; HOME RENDERS THE PASS ONLY IN STATE 3')
            + s1 + s2 + s3 + s4 + '</div>')

FLIGHT_NOTES = notecol('What a flight does to Home, and does not', [
    ('BOOKED &middot; ONE RECEIPT, THEN QUIET', N('The booking email is brought or forwarded (Life 20F); Home&rsquo;s next open shows one KEPT receipt with Undo and the trip card updated (&ldquo;your flight is booked; three seats still held&rdquo;). No crown: nothing operational is at stake for nine weeks. No countdown, no packing list, no &ldquo;prepare for your trip&rdquo; module. Between booking and the day before, the flight is a chip under the Life door and a mark on the trip row, and that is all.')),
    ('THE DAY BEFORE &middot; HOME&rsquo;S CONSEQUENCE, NOT THE PASS', N('The crown is a commitment crown in the planning register: leave by, check-in open, bag drop, security estimate, one ask (check in). The ticket is present as one kick line with a door. Gate and seat are not shown because the gate is not posted; Home claims only what a source supports, the same law as the pass&rsquo;s stub.')),
    ('THE DAY OF &middot; THE PASS IS THE CROWN', N('Life&rsquo;s live state, in Home&rsquo;s live window: the pass elevates, oxblood, provider facts replace static ones, &ldquo;current as of&rdquo; on the stub. Priority law from 02 Thursday applies: one ask, rows unchanged, the rest folded to reachable titles. The seat law holds: while Home owns this delivery, Life&rsquo;s object page shows the same pass but no Return.')),
    ('AFTER &middot; FLOWN LEAVES HOME', N('Once the flight is occurrence-supported, the pass compresses under the journey in Life (01A state 3) and Home shows the next thing: Lisbon on landing. Home never shows FLOWN; the record does not congratulate itself.')),
    ('PRODUCTION', N('Structured state (the ticket from the email, the Trip), two service reads (check-in window; gate and transit on the day), one route. No prose is generated; the truths are the provider&rsquo;s and the stub says when they were last true. Every number here is a fixture.')),
], w=520)

# ───────────────────────────── row three · the collision: the same flight, delayed ─────────────────────────────
def pass_flight_delayed(extra='', ask=True):
    """Ranks 1 and 2 on the same object merge: the pass in the recovery register. Original span struck, the new one gold (05 day three)."""
    out = f'<div style="width: 349px; background: {CARD}; border: 1px solid {HAIR}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); overflow: hidden; position: relative; box-sizing: border-box;">'
    out += (f'<div style="padding: 16px 18px 0 18px; display: flex; align-items: baseline;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {INK};">FLIGHT &middot; TAP 214</span>'
            f'<span style="{MONO} font-size: 10px; font-weight: 500; letter-spacing: 0.8px; color: {OX}; margin-left: auto;">TODAY &middot; DELAYED</span></div>')
    out += f'<div style="padding: 12px 18px 0 18px; display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">CHANGED &middot; NOW 9:30 PM &middot; GATE B22 &rarr; B31</span></div>'
    out += (f'<div style="padding: 10px 18px 0 18px; display: flex; align-items: center; gap: 14px;">'
            f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="{SERIF} font-size: 32px; line-height: 34px; font-weight: 600; letter-spacing: -0.5px;">JFK</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">New York</span></div>'
            + mark('flight', 15, 0.62).replace('flex: none;', 'flex: none; margin-top: -8px;')
            + f'<div style="display: flex; flex-direction: column; gap: 1px; margin-left: auto; text-align: right;"><span style="{SERIF} font-size: 32px; line-height: 34px; font-weight: 600; letter-spacing: -0.5px;">LIS</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">Lisbon</span></div></div>')
    out += f'<div style="padding: 16px 18px 18px 18px;">{truths((("GATE", "B31"), ("SEAT", "24A"), ("BOARDS", "20:50"), ("DEPART", "21:30")))}</div>'
    out += extra
    out += perforation()
    out += f'<div style="padding: 13px 18px 15px 18px; display: flex; align-items: center; gap: 7px;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">CURRENT AS OF 4:52 &middot; DELAY FROM PROVIDER</span><span style="margin-left: auto;">{barcode()}</span></div>'
    return out + '</div>'

def delayed_crown(spent=False):
    inst = span('THE NEW ONE &middot; 9:30 PM', 150, 240, 'LAND 9:40 AM', 'THE ORIGINAL &middot; 6:45 PM', 55, 150, 'OUT', start='4 PM', end='10', w=313)
    cta = ('' if spent else f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Tell the five the new landing</span></div>')
    fn = 'TOLD THE FIVE &middot; 5:06 &middot; ONE MESSAGE, NOT FIVE &middot; TICKETS UNCHANGED' if spent else 'ONE MESSAGE, NOT FIVE &middot; PROVIDER 4:52 &middot; TICKETS AND THE STAY UNCHANGED'
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT};">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">You land at 9:40, not 6:55. Nothing else moves.</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">The stay&rsquo;s code works at any hour. Maya and Alex&rsquo;s 8:10 is on time; they land first. Sunday&rsquo;s Sintra train is unchanged.</div>'
             + inst + cta + f'<div class="fn">{fn}</div></div>')
    return '<div style="margin: 22px 22px 0 22px;">' + pass_flight_delayed(extra=extra) + '</div>'

def folded_decision(with_door=False):
    """Rank 3 (a decision with a deadline) folds to one row under the crown, carrying its deadline. It gets the page's ask only once the crown's ask is spent."""
    tail = (f'<span style="font-size: 13px; font-weight: 500; color: {GOLDD}; flex: none;">Answer Dana</span>{ARROW}' if with_door else CHEV)
    return (f'<div class="row" style="padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px solid {OX}; box-sizing: border-box; flex: none;"></span>'
            f'<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">Dana &middot; the Saturday or the Sunday train? &middot; <span style="color: #6E6862;">her ask, by 6 &middot; {"the page&rsquo;s one ask, now" if with_door else "waits under the delay"}</span></span>{tail}</div>')

def delayed_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '4:52 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">TAP 214 is delayed to 9:30. You land at 9:40 tomorrow; nothing else moves.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Gate moved to B31 &middot; Maya and Alex&rsquo;s 8:10 is on time &middot; the stay&rsquo;s code works at any hour.</div></div>')
    inner += delayed_crown()
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they land first</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2', 'Terminal 4 after eight: what stays open']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50 from B31. Lisbon at 9:40 tomorrow.')
    return phone(inner, 0)

def collision_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '4:52 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">TAP 214 is delayed to 9:30. You land at 9:40 tomorrow; nothing else moves.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Gate moved to B31 &middot; Dana asked which train, by six; it can wait until the five know.</div></div>')
    inner += delayed_crown()
    inner += gut(folded_decision(), top=10)
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they land first</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('av:D', ''), 'Dana?', OX), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50 from B31. Dana by six.')
    return phone(inner, 0)

def spent_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '5:10 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Still delayed to 9:30. The five know. Dana is waiting on you.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Boarding 8:50 from B31 &middot; nothing else moved since 4:52.</div></div>')
    inner += delayed_crown(spent=True)
    inner += gut(folded_decision(with_door=True), top=10)
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they have your new landing</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('av:D', ''), 'Dana?', OX), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50. Dana by six.')
    return phone(inner, 0)

def arbitration_column():
    ranks = tbl(['RANK', 'OBJECT', 'REGISTER', 'WHEN IT LOSES'], [
        ['1', 'A recovery: a held commitment inside its window whose world changed', 'Oxblood crown', 'Never loses; two recoveries tie to the earlier deadline'],
        ['2', 'A live commitment inside its window, unchanged', 'The pass as the crown', 'Merges with 1 when it is the same object; otherwise one row under the crown'],
        ['3', 'A decision asked of this person with a deadline', 'Planning crown', 'One row under the crown carrying its deadline; its ask waits until the crown&rsquo;s ask is spent'],
        ['4', 'A shared arrangement forming, or a prepared possibility', 'Card', 'Its ordinary row or card, lower on the page'],
    ])
    full = g3.crown(PLAN, 'DECIDE BY 6:00 &middot; DANA&rsquo;S TRAIN', 'The Saturday train or the Sunday one?', 'Dana asks; either fits the stay. Yours is a preference, not a booking.', cta='Tell Dana which', fn='EXPIRES AT 6:00').replace('margin: 22px 22px 0 22px', 'margin: 0')
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('THE RULE', 'Which object holds the crown', 'KERNEL &sect;11.16 &middot; RULED 2026-09-05, PROVISIONAL ON THIS ROW &middot; ONE CROWN, ONE ASK')
            + f'<div style="padding: 6px 0 14px 0;">{ranks}</div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">THE MERGE &middot; RANKS 1 AND 2, SAME OBJECT</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">The pass keeps its anatomy and takes the recovery register: oxblood status, the original span struck, the new one gold, the consequence and the one ask between the truths and the tear, a stub that names the provider and the minute.</div></div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">THE FOLD &middot; RANK 3 UNDER RANK 1</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">What Dana&rsquo;s decision would be on its own (below) and what it becomes beneath a recovery: one row with its deadline and no door. When the crown&rsquo;s ask is spent, the row takes the page&rsquo;s one ask.</div>'
            f'<div style="padding-top: 8px;">{full}</div><div style="padding-top: 12px;">{folded_decision()}</div><div style="padding-top: 4px;">{folded_decision(with_door=True)}</div></div>'
            + '</div>')

COLLISION_NOTES = notecol('The collision, and what held', [
    ('WHY THIS ROW', N('Once kept objects can elevate into the crown, several objects can qualify as dominant on one afternoon. The seat law says one seat; nothing said which object wins. This row exercises the ranking on the hardest fixture we have: the same flight delayed, the group downstream of it, and a decision with a deadline arriving at the same time.')),
    ('PHONE 8 &middot; THE MERGE', N('Recovery and live commitment are one object, so the pass takes the recovery register instead of yielding to a separate crown. The consequence is stated as what does not move: the stay&rsquo;s code, the others&rsquo; flight, Sunday. One ask: tell the five, as one message (05&rsquo;s law).')),
    ('PHONE 9 &middot; THE FOLD', N('Dana&rsquo;s train question would be a planning crown on its own (left column). Under a recovery it folds to one row with its deadline and no door. The page still has one ask, and it is the crown&rsquo;s. The seam marks Saturday with her question so the deadline is visible without a second crown.')),
    ('PHONE 10 &middot; THE ASK MOVES', N('At 5:06 the message is sent; the crown keeps its register (the delay is still true) but its ask is spent, so the fold takes the page&rsquo;s one ask: &ldquo;Answer Dana&rdquo; on her row. Demand budget unchanged; dominance unchanged; only the ask moved.')),
    ('WHAT DID NOT HAPPEN', N('No second crown. No stacked banners. No &ldquo;2 things need you&rdquo;. The rest of the page stayed folded and reachable. Nobody in the group was told who asked for what; Dana&rsquo;s question is hers and Nadia&rsquo;s.')),
    ('PROVISIONAL', N('The ranking is recorded in kernel &sect;11.16 and decision 2026-09-05-home-borrows-life-pass-grammar as ruled on this drawing. If the founder reads these three phones and disagrees with the order or the fold, the decision record changes, not the phones.')),
], w=520)

# ───────────────────────────── row three · the collision: the same flight, delayed ─────────────────────────────
def pass_flight_delayed(extra='', ask=True):
    """Ranks 1 and 2 on the same object merge: the pass in the recovery register. Original span struck, the new one gold (05 day three)."""
    out = f'<div style="width: 349px; background: {CARD}; border: 1px solid {HAIR}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); overflow: hidden; position: relative; box-sizing: border-box;">'
    out += (f'<div style="padding: 16px 18px 0 18px; display: flex; align-items: baseline;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {INK};">FLIGHT &middot; TAP 214</span>'
            f'<span style="{MONO} font-size: 10px; font-weight: 500; letter-spacing: 0.8px; color: {OX}; margin-left: auto;">TODAY &middot; DELAYED</span></div>')
    out += f'<div style="padding: 12px 18px 0 18px; display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">CHANGED &middot; NOW 9:30 PM &middot; GATE B22 &rarr; B31</span></div>'
    out += (f'<div style="padding: 10px 18px 0 18px; display: flex; align-items: center; gap: 14px;">'
            f'<div style="display: flex; flex-direction: column; gap: 1px;"><span style="{SERIF} font-size: 32px; line-height: 34px; font-weight: 600; letter-spacing: -0.5px;">JFK</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">New York</span></div>'
            + mark('flight', 15, 0.62).replace('flex: none;', 'flex: none; margin-top: -8px;')
            + f'<div style="display: flex; flex-direction: column; gap: 1px; margin-left: auto; text-align: right;"><span style="{SERIF} font-size: 32px; line-height: 34px; font-weight: 600; letter-spacing: -0.5px;">LIS</span><span style="font-size: 12px; line-height: 16px; color: {MUTE};">Lisbon</span></div></div>')
    out += f'<div style="padding: 16px 18px 18px 18px;">{truths((("GATE", "B31"), ("SEAT", "24A"), ("BOARDS", "20:50"), ("DEPART", "21:30")))}</div>'
    out += extra
    out += perforation()
    out += f'<div style="padding: 13px 18px 15px 18px; display: flex; align-items: center; gap: 7px;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.2px; color: {MUTE};">CURRENT AS OF 4:52 &middot; DELAY FROM PROVIDER</span><span style="margin-left: auto;">{barcode()}</span></div>'
    return out + '</div>'

def delayed_crown(spent=False):
    inst = span('THE NEW ONE &middot; 9:30 PM', 150, 240, 'LAND 9:40 AM', 'THE ORIGINAL &middot; 6:45 PM', 55, 150, 'OUT', start='4 PM', end='10', w=313)
    cta = ('' if spent else f'<div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-top: 10px;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Tell the five the new landing</span></div>')
    fn = 'TOLD THE FIVE &middot; 5:06 &middot; ONE MESSAGE, NOT FIVE &middot; TICKETS UNCHANGED' if spent else 'ONE MESSAGE, NOT FIVE &middot; PROVIDER 4:52 &middot; TICKETS AND THE STAY UNCHANGED'
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT};">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">You land at 9:40, not 6:55. Nothing else moves.</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">The stay&rsquo;s code works at any hour. Maya and Alex&rsquo;s 8:10 is on time; they land first. Sunday&rsquo;s Sintra train is unchanged.</div>'
             + inst + cta + f'<div class="fn">{fn}</div></div>')
    return '<div style="margin: 22px 22px 0 22px;">' + pass_flight_delayed(extra=extra) + '</div>'

def folded_decision(with_door=False):
    """Rank 3 (a decision with a deadline) folds to one row under the crown, carrying its deadline. It gets the page's ask only once the crown's ask is spent."""
    tail = (f'<span style="font-size: 13px; font-weight: 500; color: {GOLDD}; flex: none;">Answer Dana</span>{ARROW}' if with_door else CHEV)
    return (f'<div class="row" style="padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px solid {OX}; box-sizing: border-box; flex: none;"></span>'
            f'<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">Dana &middot; the Saturday or the Sunday train? &middot; <span style="color: #6E6862;">her ask, by 6 &middot; {"the page&rsquo;s one ask, now" if with_door else "waits under the delay"}</span></span>{tail}</div>')

def delayed_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '4:52 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">TAP 214 is delayed to 9:30. You land at 9:40 tomorrow; nothing else moves.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Gate moved to B31 &middot; Maya and Alex&rsquo;s 8:10 is on time &middot; the stay&rsquo;s code works at any hour.</div></div>')
    inner += delayed_crown()
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they land first</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2', 'Terminal 4 after eight: what stays open']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50 from B31. Lisbon at 9:40 tomorrow.')
    return phone(inner, 0)

def collision_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '4:52 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">TAP 214 is delayed to 9:30. You land at 9:40 tomorrow; nothing else moves.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Gate moved to B31 &middot; Dana asked which train, by six; it can wait until the five know.</div></div>')
    inner += delayed_crown()
    inner += gut(folded_decision(), top=10)
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they land first</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('av:D', ''), 'Dana?', OX), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50 from B31. Dana by six.')
    return phone(inner, 0)

def spent_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '5:10 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Still delayed to 9:30. The five know. Dana is waiting on you.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Boarding 8:50 from B31 &middot; nothing else moved since 4:52.</div></div>')
    inner += delayed_crown(spent=True)
    inner += gut(folded_decision(with_door=True), top=10)
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they have your new landing</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('av:D', ''), 'Dana?', OX), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50. Dana by six.')
    return phone(inner, 0)

def arbitration_column():
    ranks = tbl(['RANK', 'OBJECT', 'REGISTER', 'WHEN IT LOSES'], [
        ['1', 'A recovery: a held commitment inside its window whose world changed', 'Oxblood crown', 'Never loses; two recoveries tie to the earlier deadline'],
        ['2', 'A live commitment inside its window, unchanged', 'The pass as the crown', 'Merges with 1 when it is the same object; otherwise one row under the crown'],
        ['3', 'A decision asked of this person with a deadline', 'Planning crown', 'One row under the crown carrying its deadline; its ask waits until the crown&rsquo;s ask is spent'],
        ['4', 'A shared arrangement forming, or a prepared possibility', 'Card', 'Its ordinary row or card, lower on the page'],
    ])
    full = g3.crown(PLAN, 'DECIDE BY 6:00 &middot; DANA&rsquo;S TRAIN', 'The Saturday train or the Sunday one?', 'Dana asks; either fits the stay. Yours is a preference, not a booking.', cta='Tell Dana which', fn='EXPIRES AT 6:00').replace('margin: 22px 22px 0 22px', 'margin: 0')
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('THE RULE', 'Which object holds the crown', 'KERNEL &sect;11.16 &middot; RULED 2026-09-05, PROVISIONAL ON THIS ROW &middot; ONE CROWN, ONE ASK')
            + f'<div style="padding: 6px 0 14px 0;">{ranks}</div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">THE MERGE &middot; RANKS 1 AND 2, SAME OBJECT</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">The pass keeps its anatomy and takes the recovery register: oxblood status, the original span struck, the new one gold, the consequence and the one ask between the truths and the tear, a stub that names the provider and the minute.</div></div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">THE FOLD &middot; RANK 3 UNDER RANK 1</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">What Dana&rsquo;s decision would be on its own (below) and what it becomes beneath a recovery: one row with its deadline and no door. When the crown&rsquo;s ask is spent, the row takes the page&rsquo;s one ask.</div>'
            f'<div style="padding-top: 8px;">{full}</div><div style="padding-top: 12px;">{folded_decision()}</div><div style="padding-top: 4px;">{folded_decision(with_door=True)}</div></div>'
            + '</div>')

COLLISION_NOTES = notecol('The collision, and what held', [
    ('WHY THIS ROW', N('Once kept objects can elevate into the crown, several objects can qualify as dominant on one afternoon. The seat law says one seat; nothing said which object wins. This row exercises the ranking on the hardest fixture we have: the same flight delayed, the group downstream of it, and a decision with a deadline arriving at the same time.')),
    ('PHONE 8 &middot; THE MERGE', N('Recovery and live commitment are one object, so the pass takes the recovery register instead of yielding to a separate crown. The consequence is stated as what does not move: the stay&rsquo;s code, the others&rsquo; flight, Sunday. One ask: tell the five, as one message (05&rsquo;s law).')),
    ('PHONE 9 &middot; THE FOLD', N('Dana&rsquo;s train question would be a planning crown on its own (left column). Under a recovery it folds to one row with its deadline and no door. The page still has one ask, and it is the crown&rsquo;s. The seam marks Saturday with her question so the deadline is visible without a second crown.')),
    ('PHONE 10 &middot; THE ASK MOVES', N('At 5:06 the message is sent; the crown keeps its register (the delay is still true) but its ask is spent, so the fold takes the page&rsquo;s one ask: &ldquo;Answer Dana&rdquo; on her row. Demand budget unchanged; dominance unchanged; only the ask moved.')),
    ('WHAT DID NOT HAPPEN', N('No second crown. No stacked banners. No &ldquo;2 things need you&rdquo;. The rest of the page stayed folded and reachable. Nobody in the group was told who asked for what; Dana&rsquo;s question is hers and Nadia&rsquo;s.')),
    ('PROVISIONAL', N('The ranking is recorded in kernel &sect;11.16 and decision 2026-09-05-home-borrows-life-pass-grammar as ruled on this drawing. If the founder reads these three phones and disagrees with the order or the fold, the decision record changes, not the phones.')),
], w=520)

# ───────────────────────────── the ladder column ─────────────────────────────
def ladder():
    def step(k, t, body, spec):
        return (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">{k}</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">{body}</div><div style="padding-top: 8px;">{spec}</div></div>')
    l1 = step('L1 &middot; THE PASS &middot; LIFE&rsquo;S OBJECT PAGE', 'The whole thing, once', 'Life&rsquo;s 09B admission signature: kick row, serif name, truths, corner cut, admit band. Object print speaks (UPCOMING) only when evidence supports it. Renders on the object page, and in Home&rsquo;s live window only.',
              f'<div style="display: flex; justify-content: center;">{pass_admission()}</div>')
    l1b = step('L1 &middot; LIVE &middot; HOME&rsquo;S WINDOW, DAY OF', 'Same anatomy, elevated', 'Life 01A: &ldquo;live = the pass gains elevation, oxblood threshold, live facts replace static ones.&rdquo; On Home the consequence and the one ask sit between the truths and the band. The pass is the crown; nothing is drawn twice.',
               f'<div style="display: flex; justify-content: center;">{live_pass_crown().replace("margin: 22px 22px 0 22px", "margin: 0")}</div>')
    l2 = step('L2 &middot; THE SAMPLE &middot; STAMPED, DASHED', 'The same signature, as a demonstration', 'Our hand-drawn stub on 04 replaced by the admission signature at L2: dashed border, SAMPLE pill, one truth. Below L2 the pass never appears; the ladder drops to the chip.',
              f'<div style="display: flex; justify-content: center;">{pass_admission(w=220, kick="ADMISSION", date="", sub="Friday &middot; doors 8", tr=(("DOORS", "8:00"),), band_r="", sample=True, pad=14, name_size=18)}</div>')
    l3 = step('L3 &middot; THE CHIP &middot; PRINT SHORTHAND', 'One line, one dot at most', 'Life 01A6 v3: mark + identity + at most one dot (ring = upcoming, green = live, grey = unused; held says nothing). Home uses it where a kept object is named: the kept receipt, the Life door&rsquo;s shelf.',
              f'<div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">{chip("admission", "THE HALL", "ring")}{chip("flight", "JFK&rarr;NCE")}{chip("dining", "Alex&rsquo;s birthday", "live", serif=True)}{chip("ferry", "SOR&rarr;CAPRI", "unused")}</div>'
              + f'<div style="padding-top: 12px;">{kept_chip_row("admission", "THE HALL", "Friday &middot; in Life")}</div>')
    l4 = step('L4 &middot; THE MARK &middot; INLINE GLYPH', 'The kind, said once, in ink', 'In a Home row whose subject is a kept object, the lead is the mark instead of a status dot. Kind lives in the mark; state stays in the words. People rows keep the facepile; ephemeral rows keep the dot.',
              f'<div>{row_mark("admission", "The show &middot; Friday, doors 8 &middot; <span style=\'color: #6E6862;\'>set times not posted</span>")}{row_mark("flight", "Return flight refund claim &middot; <span style=\'color: #6E6862;\'>airline reviewing</span>")}{row("Dentist &middot; Tuesday 9:00 &middot; <span style=\'color: #6E6862;\'>walk, the bus is slower</span>", mark="dashed", last=True)}</div>')
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('LIFE &rarr; HOME', 'The ticket at every scale', 'ONE OBJECT &middot; ONE IDENTITY &middot; FOUR SCALES &middot; LIFTED FROM LIFE 09B AND 01A6')
            + l1 + l1b + l2 + l3 + l4 + '</div>')

# ───────────────────────────── the door map + rulings ─────────────────────────────
DOORS = [
    ['The bakery (02 Sunday, inside &ldquo;Today&rdquo;)', 'B &middot; the world&rsquo;s place', 'Places &middot; Place Focus (06)', 'Maya&rsquo;s share rides along as the note beside the verdict; her grant governs'],
    ['The bookshop &middot; The noodle bar (02 Monday, Addressed to you)', 'B &middot; the world&rsquo;s place', 'Places &middot; Place Focus', 'The addressed note is the source (A) shown beside the verdict; not a dossier'],
    ['The arrangement (02 Monday) &middot; Tell Alex which (02 Thursday) &middot; The trip (05)', 'D &middot; the current arrangement', 'Plan / Occasion lane', 'Anatomy, commands, and views belong to the Plan lane; Home carries the envelope only'],
    ['All plans and occasions', 'D &middot; arrangements, listed', 'Plan lane &middot; list', 'Never a Home-owned list'],
    ['What your friends have shared', 'B &middot; places, in the friends scope', 'Places &middot; From friends (06)', 'Casual shares; the record behind it is Life People'],
    ['Everything in Life &middot; Everything shared with you', 'C &middot; the record', 'Life root / Life &middot; People', 'The chip shelf under the door names the kept objects; tapping a chip opens its pass (L1)'],
    ['Open the way there (Friday, live)', 'the live route', 'Home &middot; the live window', 'Stays on Home; the pass unfolds behind the crown, not a new surface'],
    ['Try with yours (04) &middot; Bring something', 'contribution', 'Chat', 'Life 20-family: value-first response, scoped receipt (KEPT chip with Undo)'],
    ['Read the chapter (02, cut) &middot; The trip, in Life (03)', 'C &middot; the dossier', 'Life &middot; the journey / the reading object', 'Life 06A journey grammar; Home never re-renders the dossier'],
    ['How to get it at home (03)', 'C &middot; the thread', 'Life &middot; the pasta thread (13B)', 'The epistemic return; Home shows the finding, Life holds the lineage'],
    ['The ticket (08, the day before) &middot; the KEPT receipt&rsquo;s chip', 'the pass, L1', 'Life &middot; the object page (09A)', 'The pass unfolds with its layered source (the booking email) one fold beneath'],
    ['In the Lisbon plan (on the pass&rsquo;s stub)', 'D &middot; the current arrangement', 'Plan lane &middot; the Trip', 'Life 01A: the plan owns urgency; the pass only points at it'],
    ['The ticket (08, the day before) &middot; the KEPT receipt&rsquo;s chip', 'the pass, L1', 'Life &middot; the object page (09A)', 'The pass unfolds with its layered source (the booking email) one fold beneath'],
    ['In the Lisbon plan (on the pass&rsquo;s stub)', 'D &middot; the current arrangement', 'Plan lane &middot; the Trip', 'Life 01A: the plan owns urgency; the pass only points at it'],
    ['Keep this &middot; (any Home unit)', 'E &middot; a kept snapshot', 'Everything kept &middot; GENERATED', 'Readback: &ldquo;Saved as made &middot; it won&rsquo;t update itself&rdquo; (Life 32)'],
]

def seam_board():
    cols = [ladder(),
            col(sunday_seam(), daycap('SUNDAY 9:10 &middot; QUIET', '1 &middot; MARKS AND CHIPS ON AN ORDINARY PAGE', 'The show row wears its mark; the Life door shows its shelf', 'ROW LEAD = KIND MARK FOR KEPT OBJECTS &middot; CHIPS UNDER THE LIFE DOOR')),
            col(friday_live(), daycap('FRIDAY 5:40 &middot; LIVE', '2 &middot; THE PASS AS THE CROWN', 'Life&rsquo;s L1 in Home&rsquo;s live window', 'OXBLOOD THRESHOLD &middot; LIVE TRUTHS &middot; THE CONSEQUENCE BETWEEN TRUTHS AND BAND')),
            col(first_open_seam(), daycap('TUESDAY 8:05 &middot; COLD', '3 &middot; THE SAMPLE, WITH LIFE&rsquo;S SIGNATURE', 'The admission pass at L2 replaces the stub', 'DASHED &middot; STAMPED &middot; ONE TRUTH &middot; SAME RESULT BESIDE IT')),
            col(return_seam(), daycap('WEDNESDAY 7:30 &middot; THIN', '4 &middot; THE RECEIPT AS A CHIP', 'Kept, once, with Undo', 'THE KEPT ROW CARRIES THE CHIP &middot; TAP IT: THE PASS IN LIFE'))]
    notes = [notecol('The door map &middot; where every Home door lands (Life 32: five objects, no copies)', [
                ('A SOURCE &middot; B THE WORLD&rsquo;S PLACE &middot; C THE LIFE DOSSIER &middot; D THE ARRANGEMENT &middot; E A KEPT SNAPSHOT', tbl(['HOME DOOR', 'LANDS ON', 'SURFACE', 'WHAT CARRIES'], DOORS))], w=1180),
             notecol('Two rulings, now ruled', [
                ('1 &middot; THE KIND MARK IS PRINT, NOT A PLATE', N('Kernel &sect;12.7 (g) rules Home rows carry a status mark and no icon plates. Life&rsquo;s kind mark is a 15px inline glyph in ink, one stroke family, never a tinted plate. <b>Ruled:</b> a Home row whose subject is a kept object (a ticket, a booking, a claim) leads with the mark; state stays in the words; people rows keep the facepile; ephemeral rows keep the dot. At most one lead per row. The violet on the admission band is illustration ink (Life 01A2), never UI chrome.')),
                ('RULED 2026-09-05', N('Both rulings are recorded in decision <b>2026-09-05-home-borrows-life-pass-grammar</b> (kernel &sect;12.7 g note, &sect;11.2 note, new &sect;11.16). The crown ranking in row three is ruled provisionally on that drawing.')),
                ('RULED 2026-09-05', N('Both rulings are recorded in decision <b>2026-09-05-home-borrows-life-pass-grammar</b> (kernel &sect;12.7 g note, &sect;11.2 note, new &sect;11.16). The crown ranking in row three is ruled provisionally on that drawing.')),
                ('2 &middot; CHIP LETTERING IS OBJECT PRINT', N('Home&rsquo;s 10px floor is a UI floor. Life exempts chip interiors (8.5px mono, serif 11px for names) as object print, like the lettering on a tag. <b>Ruled:</b> the same exemption on Home, for chips only, and chips only where a kept object is named (the KEPT receipt, the Life door&rsquo;s shelf). Never for UI labels, never as a list.')),
                ('WHAT NOT TO IMPORT', N('Life&rsquo;s 60px record rows, its gold-ruled Returns unit, and the full pass anywhere but the live window. Life 16 composes Home panels to pointers and defers the final form to these boards.')),
             ], w=520),
             notecol('The seam, stated', [
                ('THE SEAT LAW (LIFE 19)', N('One present-delivery seat across surfaces. When Home delivers a consequence from some evidence, Life&rsquo;s matching Return is absent, with no redirect shell. 07 should cite this; it is the rule that keeps 02&rsquo;s &ldquo;Worth knowing&rdquo; and Life&rsquo;s Returns from showing the same thing twice.')),
                ('TIMELINESS (LIFE 17C)', N('An addressed note rests as a quiet stamp on the person&rsquo;s row in Life People; Home admits it only when it earns present attention. <b>Amend the region condition:</b> two or more addressed contributions, unspent above <i>and timely inside the person&rsquo;s window</i>. Dana&rsquo;s bookshop for Sunday and Maya&rsquo;s noodle bar for after the show both pass; a note with no date does not.')),
                ('ONE LOOP', N('Life holds the source, the record, and the one governed foundation. Home delivers the present consequence, once. Places delivers the place-scoped present. Chat continues. The receipt returns to Life as lineage. The ticket above walks that loop: kept in Life, live on Home, a chip on the way back.')),
                ('FIXTURE DRIFT TO RECONCILE', N('Life dates the dinner Aug 29 as &ldquo;Dinner at ours&rdquo;; Home says &ldquo;Dinner in Brooklyn, Saturday 8:15&rdquo;. Life&rsquo;s Alex&rsquo;s birthday is Sat Sep 5; Home&rsquo;s is next Saturday. Same people, same trip, same Rome and Paris comparison, same Aeneas passage.')),
             ], w=520)]
    row2 = [flight_ladder(),
            col(booked_phone(), daycap('TUESDAY 9:12 PM &middot; NINE WEEKS OUT', '5 &middot; JUST BOOKED', 'One receipt, then quiet', 'KEPT CHIP WITH UNDO &middot; THE TRIP CARD UPDATES &middot; NO CROWN, NO COUNTDOWN')),
            col(eve_phone(), daycap('THURSDAY 8:10 PM &middot; THE DAY BEFORE', '6 &middot; IMMINENT', 'Home&rsquo;s consequence; the ticket as one line', 'PLANNING CROWN &middot; LEAVE BY, CHECK IN, BAG DROP &middot; GATE NOT CLAIMED')),
            col(live_flight_phone(), daycap('FRIDAY 3:12 PM &middot; LIVE', '7 &middot; THE DAY OF', 'The pass is the crown', 'OXBLOOD &middot; PROVIDER FACTS &middot; CURRENT AS OF &middot; THE REST FOLDS')),
            FLIGHT_NOTES]
    html = page(2480, hh('08'), f'VESPER &middot; HOME &middot; 08 &middot; THE SEAM WITH LIFE &middot; PROPOSAL &middot; ADDED 2026-09-05 &middot; THE FLIGHT AND THE COLLISION &middot; {STAMP}', '08 &middot; The seam with Life: one ticket, one flight, one collision, and where every door lands',
                'What Home borrows from Vesper &mdash; Life &amp; Anchors (f524c7f0): the pass family at L1 in the live window, the admission signature as the sample, the chip for kept receipts, the kind mark on object rows; the five-object door map; the seat law and the timeliness clause; two rulings the kernel needs before any of it ships. Pass anatomy, chip grammar, and glyphs are lifted from Life boards 09B, 01A2, 01A6, 25, 32. The second row follows one flight from the evening it was booked to the afternoon it boards. The third row delays it and tests the crown ranking (kernel &sect;11.16).', cols, notes)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE FLIGHT &middot; BOOKED, IMMINENT, LIVE, FLOWN &middot; LIFE 01A&rsquo;S FOUR STATES ON HOME</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">A flight to Lisbon, from the booking email to the gate</div>'
               f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">Nadia&rsquo;s own seat on the Lisbon trip from 05. Home changes three times in nine weeks: one receipt the night it is booked, a planning crown the day before, and the pass itself as the crown on the day. In between, nothing: a chip under the Life door and a mark on the trip&rsquo;s row.</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    row3 = [arbitration_column(),
            col(delayed_phone(), daycap('FRIDAY 4:52 PM &middot; AT JFK &middot; DELAYED', '8 &middot; THE MERGE', 'The pass in the recovery register', 'RANKS 1 AND 2, ONE OBJECT &middot; ORIGINAL STRUCK, NEW GOLD &middot; ONE MESSAGE TO FIVE')),
            col(collision_phone(), daycap('FRIDAY 4:52 PM &middot; AND DANA ASKS', '9 &middot; THE FOLD', 'A decision with a deadline, under a recovery', 'ONE CROWN &middot; THE DECISION IS A ROW WITH ITS DEADLINE &middot; STILL ONE ASK')),
            col(spent_phone(), daycap('FRIDAY 5:10 PM &middot; THE MESSAGE SENT', '10 &middot; THE ASK MOVES', 'The crown holds; its ask is spent', 'THE FOLD TAKES THE PAGE&rsquo;S ONE ASK &middot; DOMINANCE UNCHANGED')),
            COLLISION_NOTES]
    divider3 = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE COLLISION &middot; THE SAME FLIGHT, DELAYED &middot; THE GROUP &middot; A DECISION WITH A DEADLINE &middot; KERNEL &sect;11.16</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Three things that could each be the crown, on one page, at 4:52 PM</div>'
                f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">The test of the ranking. TAP 214 is delayed two hours and forty-five minutes; five people downstream need to know; Dana asks which train, by six. One crown, one ask, and the ask moves when it is spent.</div></div>'
                '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row3) + '</div>')
    html = html.replace('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">', divider + divider3 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">', 1)
    return html

if __name__ == '__main__':
    html = seam_board(); open(os.path.join(OUT, '08 - Seam with Life.dc.html'), 'w').write(html); print('wrote 08', len(html))
