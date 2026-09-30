"""Board R5 — Live Home rules (2026-09-26). A reference board, not a study: the rules behind 19-21 and 24 written
down so each case is decidable. Draws with the same live-object kit as gen_live.py (imported, which also rebuilds
19-24 into OUT as a side effect; only R5 is written by this script's own loop).
Usage: python3 gen_rules.py <in_dir> <out_dir>
"""
import sys, os, json
import gen_live as L
from gen_live import (MONO, SERIF, SANS, INK, INK2, MUTE, HINT, CARD, PAPER, LIVE, LIVED, CR, CRM, CRL,
                      okick, ofield, live_object, pass_inner, admission_inner, band, table, board, _perf, pulse)

OUT = L.OUT
GOLDK = '#8A6628'

def specimen(inner, w=393, pad='18px 0 20px'):
    """A patch of phone surface so the object's notches read as they do on Home."""
    return f'<div style="width: {w}px; flex: none; background: {PAPER}; border-radius: 14px; padding: {pad}; box-sizing: border-box;">{inner}</div>'
def cap(k, t, s='', w=393):
    return (f'<div style="width: {w}px; margin-top: 10px;"><div class="kick">{k}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 16px; line-height: 21px; margin-top: 3px;">{t}</div>'
            + (f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 3px;">{s}</div>' if s else '') + '</div>')
def fig(obj, k, t, s='', w=393):
    return f'<div style="display: flex; flex-direction: column; width: {w}px; flex: none;">{specimen(obj, w)}{cap(k, t, s, w)}</div>'

def mini_inner(kl, kr, title, sub='', size=26):
    return (f'<div style="padding: 14px 18px 16px;">{okick(kl, kr)}'
            f'<div style="font-family: {SERIF}; font-size: {size}px; line-height: {size + 2}px; font-weight: 600; margin-top: 10px;">{title}</div>'
            + (f'<div style="font-size: 12.5px; line-height: 17px; color: {CRM}; margin-top: 4px;">{sub}</div>' if sub else '') + '</div>')
def cream_mini(kl, kr, title, sub, stub_l, stub_r, used=False):
    op = '0.72' if used else '1'
    return L.gut(f'<div style="background: {CARD}; border-radius: 18px; overflow: hidden; opacity: {op}; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                 f'<div style="padding: 14px 18px 16px;"><div style="display: flex; align-items: baseline;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE};">{kl}</span>'
                 f'<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {HINT};">{kr}</span></div>'
                 f'<div style="font-family: {SERIF}; font-size: 26px; line-height: 28px; font-weight: 600; margin-top: 10px; color: {INK};">{title}</div>'
                 f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 4px;">{sub}</div></div>'
                 + _perf('rgba(27,23,20,0.22)', PAPER)
                 + f'<div style="display: flex; align-items: center; padding: 12px 18px 14px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: {MUTE};">{stub_l}</span>'
                 f'<span style="margin-left: auto; font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {MUTE};">{stub_r}</span></div></div>', 0)
def nothing(line):
    return L.gut(f'<div style="border: 1.5px dashed rgba(27,23,20,0.18); border-radius: 18px; min-height: 150px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 18px;">'
                 f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 23px; color: {MUTE};">{line}</div></div>', 0)

def section(num, title, statement, right, lw=520):
    left = (f'<div style="width: {lw}px; flex: none;"><div style="font-family: {MONO}; font-size: 11px; font-weight: 700; letter-spacing: 1.3px; color: {GOLDK};">{num}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 28px; line-height: 33px; margin-top: 8px; text-wrap: balance;">{title}</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {INK2}; margin-top: 12px;">{statement}</div></div>')
    return (f'<div style="display: flex; gap: 56px; align-items: flex-start; margin-top: 56px; padding-top: 32px; border-top: 1px solid rgba(27,23,20,0.12);">'
            + left + f'<div style="flex: 1; min-width: 0;">{right}</div></div>')
def para(*ps): return ''.join(f'<p style="margin: 0 0 10px;">{p}</p>' for p in ps)
def rules(items):
    return ''.join(f'<div style="display: flex; gap: 14px; padding: 10px 0; border-top: 1px solid rgba(27,23,20,0.08);">'
                   f'<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {GOLDK}; width: 22px; flex: none; padding-top: 3px;">{n}</span>'
                   f'<div><div style="font-size: 14.5px; line-height: 20px; font-weight: 600; color: {INK};">{t}</div>'
                   f'<div style="font-size: 13px; line-height: 19px; color: {MUTE}; margin-top: 2px;">{s}</div></div></div>' for n, t, s in items)
def figrow(*figs, gap=28): return f'<div style="display: flex; gap: {gap}px; align-items: flex-start; flex-wrap: nowrap;">' + ''.join(figs) + '</div>'
def arrow(t):
    return (f'<div style="width: 120px; flex: none; align-self: center; text-align: center; padding-bottom: 60px;">'
            f'<div style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {GOLDK}; line-height: 15px;">{t}</div>'
            f'<div style="height: 1px; background: {GOLDK}; margin: 8px 6px 0; position: relative;"><span style="position: absolute; right: -2px; top: -4px; width: 0; height: 0; border-left: 7px solid {GOLDK}; border-top: 4.5px solid transparent; border-bottom: 4.5px solid transparent;"></span></div></div>')

# ---------------- objects ----------------
def red_hook(coupon=True, time='10:40 AM'):
    inner = (f'<div style="padding: 14px 18px 16px;">{okick("WHERE YOU ARE &middot; BROOKLYN", "SAT")}'
             f'<div style="font-family: {SERIF}; font-size: 30px; line-height: 32px; font-weight: 600; margin-top: 10px;">Red Hook</div>'
             f'<div style="font-size: 12.5px; line-height: 17px; color: {CRM}; margin-top: 4px;">Old piers and warehouses at the water&rsquo;s edge.</div>'
             f'<div style="display: flex; gap: 22px; margin-top: 14px;">{ofield("FLEA", "UNTIL 3")}{ofield("LOW WATER", "2:40")}{ofield("DARK", "6:52")}</div></div>')
    return live_object(inner, 'HERE NOW', time, coupon=(('IN REACH', [('bowl', 'The flea, under the bridge', '6 MIN &middot; UNTIL 3'), ('water', 'The pier at low water', '9 MIN &middot; FROM 2:40')]) if coupon else None))
LILIA = mini_inner('RESERVATION &middot; LILIA', 'SUNDAY', 'Lilia', 'Table for two &middot; with Maya &middot; 8:00')
def lilia(coupon=True):
    return live_object(LILIA, 'LIVE &middot; TONIGHT', 'LEAVE BY 7:49', coupon=(('ON THE WAY', [('fork', 'Ask for the corner table', 'MAYA &middot; AUG 30')]) if coupon else None))
FERRY = mini_inner('FERRY &middot; ALILAURO', 'WED', 'Sorrento to Capri', 'Sails 11:20 from Marina Piccola')
PASS = mini_inner('FLIGHT &middot; TAP 214', 'TODAY', 'JFK to Lisbon', 'Gate B22 &middot; boards 6:05 &middot; seat 24A')
STAY = mini_inner('THE STAY &middot; LISBON', 'SAT', 'Door code 4417', '[Fixture street] 14, second floor')

# ---------------- sections ----------------
S1 = section('01 &middot; THE RULE', 'One thing is live when it is happening now, and the phone can show it is',
    para('Home draws one object live, dark with a pulsing stub, when three things are true. Otherwise Home is its ordinary self, and nothing on it is dark.',
         'Live is a claim about the present. It is never a reward, a nudge or a way to make the page feel busy.'),
    rules([('A', 'It is now', 'The thing is inside its window: you are on your way to it, at it, or it is about to leave without you.'),
           ('B', 'It is held, or it is where you are', 'A ticket, reservation, gathering or stay the person holds; or, away from home with nothing held, the place itself.'),
           ('C', 'The evidence is on the phone', 'The time, the booking or the location that makes it true is present. No evidence, no live object, and nothing asks for permission to get it.')])
    + '<div style="height: 26px;"></div>'
    + figrow(fig(nothing('Nothing is live.<br>Home is its ordinary self.'), 'MOST OF THE TIME', 'No dark object', 'Familiar city, nothing underway: Nadia&rsquo;s Sunday (02, 24.1)'),
             fig(lilia(), 'A HELD THING, NOW', 'The plan&rsquo;s own object turns dark', 'Lilia, twenty minutes before leaving (24.2)'),
             fig(red_hook(), 'WHERE YOU ARE, NOW', 'The place turns dark', 'A new city with nothing held (19, 24.4)')))

S2 = section('02 &middot; FOUR SITUATIONS', 'Where you are and what you hold decide which object, if any',
    para('Two questions, both answered from evidence: is this the person&rsquo;s own city, and do they hold something in it today? The answer picks the object. The object&rsquo;s window (03) then decides when it turns dark.'),
    table(['', 'Nothing held today', 'Something held today'], [
        ['<b>Own city</b>', '<b>Nothing is live.</b> Openings and what is in motion, as ordinary rows. 24.1 &middot; 20.9 after the show',
         '<b>The held thing goes live in its window.</b> Before that it is a cream row or Ticket. 24.2 &middot; 20 &middot; 21.1&ndash;21.3'],
        ['<b>Another city</b>', '<b>The place card is live</b> while location says you are there. 19 &middot; 21.7 &middot; 24.4',
         '<b>The next held thing goes live;</b> between held things, the place card. 24.3 &middot; 21.6']], minw=1100)
    + '<div style="height: 26px;"></div>'
    + figrow(fig(nothing('Nothing is live.'), '24.1 &middot; OWN CITY, NOTHING HELD', 'Ordinary Home', w=318),
             fig(live_object(LILIA, 'LIVE &middot; TONIGHT', 'LEAVE BY 7:49'), '24.2 &middot; OWN CITY, HELD', 'The reservation', w=318),
             fig(live_object(FERRY, 'LIVE &middot; THIS MORNING', 'SAILS 11:20'), '24.3 &middot; ANOTHER CITY, HELD', 'The next held thing', w=318),
             fig(red_hook(coupon=False), '24.4 &middot; ANOTHER CITY, NOTHING HELD', 'The place card', w=318), gap=18))

S3 = section('03 &middot; ONE OBJECT&rsquo;S DAY', 'Cream until its window, dark while it is live, then a used row',
    para('The same object changes state; it is never replaced by a different card. Each change has one trigger, and the trigger is a fact the phone holds.',
         'Urgent and offline are states of the live object, not new objects. Urgent is the only state that may push the rest of Home down (21.2).'),
    figrow(fig(cream_mini('FLIGHT &middot; TAP 214', 'TODAY', 'JFK to Lisbon', 'Gate not yet &middot; boards 6:05', 'LEAVE WORK BY 3:40', 'CREAM'), 'HELD &middot; 10:15 AM', 'Cream, leading the day', 'Today, not yet in its window (21.1)', w=300),
           arrow('LEAVE-BY<br>PASSES'),
           fig(live_object(PASS, 'LIVE', 'BOARDS 6:05'), 'LIVE &middot; 5:20 PM', 'Dark, pulsing green', 'On the way and at the gate (21.3)', w=300),
           arrow('IT IS<br>THREATENED'),
           fig(live_object(PASS, 'URGENT', 'BAG DROP 5:45', urgent=True), 'URGENT &middot; 3:58 PM', 'Oxblood, one recovery', 'The train stops (21.2)', w=300),
           gap=10)
    + '<div style="height: 22px;"></div>'
    + figrow(fig(live_object(STAY, 'OFFLINE', 'AS OF 5:52 PM', still=True), 'STILL &middot; NO CONNECTION', 'The dot stops; it says &ldquo;as of&rdquo;', 'Saved facts stay usable (21.6)', w=300),
             arrow('THE WINDOW<br>CLOSES'),
             fig(cream_mini('ADMISSION &middot; THE HALL', 'FRI', 'The Hall', 'Tonight &middot; used', 'ADMIT ONE', 'USED', used=True), 'USED &middot; 10:52 PM', 'Back to cream, down the page', 'Then it belongs to Life (20.9, 08)', w=300),
             gap=10))

S4 = section('04 &middot; WINDOWS', 'When each kind of object turns dark, and when it stops',
    para('Leave-by is the start time minus the way there and a small margin. It needs a starting point: the current location, or where the person will be (the stay, the office). Without one, the window opens at a fixed lead instead.',
         'Numbers are proposed defaults for the founder to rule on (09), not canon.'),
    table(['Object', 'Before', 'Turns dark', 'Stays dark through', 'Stops', 'Coupon heading', 'Drawn in'], [
        ['Flight pass', 'Cream on the day', 'At leave-by for the airport', 'Check-in, security, the gate', 'Boarding closes; then flown, and Life&rsquo;s', 'BEFORE BOARDING &middot; 33 MIN', '21.1&ndash;21.5'],
        ['Train or ferry ticket', 'Cream on the day', 'At leave-by for the station or pier', 'The walk down, the wait', 'It departs; the next held thing or the place card follows', 'BEFORE THE FERRY', '24.3'],
        ['Reservation', 'A cream row', '20 min before leave-by', 'The walk and the meal', 'Its end time, or the person leaves', 'ON THE WAY', '24.2'],
        ['Gathering, as host', 'The arrangement card', 'At the start time', 'Arrivals and the evening', 'The stated end or the last stated leave', 'BEFORE THEY ARRIVE', '20.3, 20.6'],
        ['Gathering, as guest', 'Invitation or cream row', 'At leave-by', 'The way there and the evening', 'The host&rsquo;s stated end', 'ON YOUR WAY', '20.4'],
        ['Admission', 'Cream on the day', 'At leave-by for the meet', 'The meet and the show', 'The set ends', 'AFTER THE SHOW', '20.7&ndash;20.9'],
        ['Stay', 'A cream row', 'On landing in its city', 'Getting there', 'The person reaches it (location at the stay)', 'NEEDS A CONNECTION, offline', '21.6'],
        ['Place card', 'Never cream', 'Location in another city, nothing held live', 'Moving about', 'A held thing turns dark; they leave; location goes stale (15 min)', 'IN REACH', '19, 21.7, 24.4']], minw=1300))

S5 = section('05 &middot; ONE AT A TIME', 'Only one thing is dark; everything else steps down',
    para('When two things could be live, one wins and the other becomes a coupon item or a row. Other people&rsquo;s plans are never live on your Home: Maya and Alex&rsquo;s flight is a line in Nadia&rsquo;s coupon (21.3).'),
    rules([('1', 'Urgent first', 'A threatened held thing, with one recovery. Only one at a time.'),
           ('2', 'Then the held thing whose window is open', 'If two are open, the one that starts sooner. The other becomes a coupon item.'),
           ('3', 'Then the place card', 'Only when no held thing is in its window, and only away from home.'),
           ('4', 'Otherwise nothing', 'Home is its ordinary self.')])
    + '<div style="height: 26px;"></div>'
    + figrow(fig(red_hook(coupon=False, time='4:05 PM'), 'SATURDAY 4:05 PM', 'The place card, between plans', 'Red Hook, nothing in its window yet', w=340),
             arrow('DINNER&rsquo;S<br>WINDOW OPENS'),
             fig(live_object(mini_inner('RESERVATION &middot; DINNER', 'SAT', 'Dinner at 8:15', 'Table for two &middot; Van Brunt'), 'LIVE &middot; TONIGHT', 'LEAVE BY 7:55',
                             coupon=('ON THE WAY', [('walk', 'Four minutes on foot', 'FROM WHERE YOU ARE')])), 'SATURDAY 7:35 PM', 'The reservation takes over', 'The place card steps down; Red Hook stays in Places', w=340),
             gap=14))

S6 = section('06 &middot; THE COUPON', 'What tears off below is help for this window, or nothing',
    para('The coupon is optional. An empty coupon is never drawn: if nothing fits the time left, the live object stands alone (20.6, the rush in 21.2).'),
    rules([('1', 'Only under a live object', 'Nothing tears off a cream Ticket or a row.'),
           ('2', 'Every item states its fit', 'The mono line says why it fits now: how far, until when, whether it fits before boarding.'),
           ('3', 'One to four items', 'People&rsquo;s words first (Maya&rsquo;s pick), then world facts. No ranking language.'),
           ('4', 'The heading names the window', 'BEFORE BOARDING &middot; 33 MIN, ON YOUR WAY, AFTER THE SHOW, IN REACH, NEEDS A CONNECTION.'),
           ('5', 'Nothing mid-activity', 'At the table or inside the show, the object stays dark and alone.')])
    + '<div style="height: 26px;"></div>'
    + figrow(fig(live_object(PASS, 'LIVE', 'BOARDS 6:05 &middot; 33 MIN', coupon=('BEFORE BOARDING &middot; 33 MIN', [('bowl', 'A noodle counter by B18', '3 MIN &middot; FITS BEFORE 6:05'), ('plane', 'Maya and Alex&rsquo;s 8:10, on time', 'THEY LAND 9:25 &middot; MEET AT THE STAY')])),
                 'HELP FOR THE WAIT', 'Food that fits, and a friend&rsquo;s plan as a line', '21.5'),
             fig(live_object(STAY, 'OFFLINE &middot; ON THIS PHONE', 'AS OF 5:52 PM NY', still=True, coupon=('NEEDS A CONNECTION', [('walk', 'Walking directions', 'THE WRITTEN WAY ABOVE WORKS NOW')])),
                 'HONEST OFFLINE', 'What waits for a signal', '21.6'),
             fig(live_object(admission_inner(), 'LIVE &middot; TONIGHT', 'ADMIT ONE', chamfer=True), 'NOTHING FITS', 'Inside the show, no coupon', '20.7 without its coupon, during the set')))

S7 = section('07 &middot; NEVER LIVE', 'What does not turn dark, however useful',
    para('These are the cases most likely to be argued for later. Each one is ruled out here so the argument starts from a rule.'),
    rules([('&times;', 'Suggestions and openings', 'Only held things and the person&rsquo;s own situation. The flea is a coupon item, never the object.'),
           ('&times;', 'Anything missing its evidence', 'No location, no place card and no leave-by (19.6). A stale booking stays cream with its &ldquo;as of&rdquo;.'),
           ('&times;', 'Your own city with nothing held', 'Home is ordinary (24.1). A neighbourhood you haven&rsquo;t visited is still your city.'),
           ('&times;', 'Other people&rsquo;s plans', 'A coupon line or a row in In motion, never a dark object on your Home.'),
           ('&times;', 'A ticking timer', 'Minutes are a fact at the time of the frame (33 MIN), never a live countdown. Leave-by is a time.'),
           ('&times;', 'A request', 'Live never asks for location, a rating or a photo.')]))

# ---------------- evidence + familiarity (filled from the 09-26 code read) ----------------
EVIDENCE = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rules_evidence.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rules_evidence.json')) else {'rows': [], 'note': '', 'fam': [], 'qs': []}
S8 = section('08 &middot; EVIDENCE', 'What each rule needs, and what the code holds today',
    para(EVIDENCE['note']),
    table(['Signal', 'Decides', 'In code today', 'Gap'], EVIDENCE['rows'], minw=1300)) if EVIDENCE['rows'] else ''
S9 = section('09 &middot; FOR THE FOUNDER', 'Familiar or not, and the numbers',
    para('Everything above depends on one judgement the product cannot yet make well: whether this is the person&rsquo;s own city. The safe failure is an ordinary Home: a missing place card in a new city costs less than a wrong one in your own.'),
    rules(EVIDENCE['fam']) + '<div style="height: 22px;"></div>' + rules(EVIDENCE['qs'])) if EVIDENCE['fam'] else ''

BODY = S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8 + S9
HJ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'live_heights.json')
H = json.load(open(HJ)).get('R5', 6000)
html_ = board('R5', 'When something is live', 'VESPER &middot; HOME &middot; R5 &middot; REFERENCE &middot; LIVE HOME RULES &middot; 2026-09-26 &middot; PROPOSED',
              'The rules behind 19, 20, 21 and 24, written down so each new case can be decided from a rule instead of a drawing. Proposed, not canon: the numbers are starting defaults for the founder to rule on (09).',
              BODY, 2000, H)
open(f'{OUT}/R5 - Reference - Live Rules.dc.html', 'w').write(html_)
print('wrote R5', len(html_))
