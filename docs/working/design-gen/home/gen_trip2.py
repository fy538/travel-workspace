"""The trip day's whole encounter on 08b (row nine) and the temporal strip's form on 09 (2026-09-08).
Usage: python3 gen_trip2.py <polished_dir> <out_dir>   — reads the polished 03/08b/09, writes new 08b and 09.
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
G = '/Users/feihuyan/travel-workspace/docs/working/design-gen/home/gen_trip.py'
src = open(G).read().split("# ---- board edits")[0]
sys.argv = ['x', IN, OUT]; exec(src.replace("LIVE, OUT = sys.argv[1], sys.argv[2]\nos.makedirs(OUT, exist_ok=True)", "LIVE, OUT = sys.argv[1], sys.argv[2]"))
def h03(): return open(f'{IN}/03 - Persona B - Back from Europe.dc.html').read()
def phone_regions(h):
    out = []
    for m in re.finditer(r'<div style="width: 393px;[^"]*background: #EFEAE0', h):
        s = m.start(); depth = 0; e = None
        for mm in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0: e = s + mm.end(); break
        if e and not (out and s < out[-1][1]): out.append((s, e))
    return out
h = h03(); i = h.find('SELECTED &middot; THE CURRENT HOME SCROLLS'); TRIP = [h[s:e] for s, e in phone_regions(h) if s > i][2]
# the polished eyebrow style for the strip and the receipt
EYE = lambda t, right='': f'<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: #2A384B; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: #2A384B;">{t}</span>{("<span class=\"fn\" style=\"margin-left: auto;\">" + right + "</span>") if right else ""}</div>'
def page_head(kick_t, title, sub):
    circ = lambda inner: f'<span style="width: 32px; height: 32px; border-radius: 16px; border: 1px solid rgba(27,23,20,0.14); display: inline-flex; align-items: center; justify-content: center; background: {CARD};">{inner}</span>'
    back = circ('<svg width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M8.5 2.5L4 6.5L8.5 10.5" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    srch = circ('<svg width="13" height="13" viewBox="0 0 13 13" fill="none"><circle cx="5.6" cy="5.6" r="3.8" stroke="#1B1714" stroke-width="1.4"/><path d="M8.6 8.6L11.5 11.5" stroke="#1B1714" stroke-width="1.5" stroke-linecap="round"/></svg>')
    return (f'<div style="padding: 20px 22px 0 22px; display: flex; align-items: center; justify-content: space-between;">{back}{srch}</div>'
            f'<div style="padding: 22px 22px 0 22px;"><div class="fn" style="color: {HINT};">{kick_t}</div><div style="font-family: {SERIF}; font-weight: 600; font-size: 26px; line-height: 31px; margin-top: 8px; text-wrap: balance;">{title}</div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 6px;">{sub}</div></div>')
def strip_variant(now, title, sub, stops):
    rail = '<div style="display: flex; align-items: center; margin-top: 12px;">'
    for k, (t, l, kind, c) in enumerate(stops):
        if k: rail += '<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.14); margin: 0 6px 14px;"></span>'
        mark = f'<span style="width: 8px; height: 8px; border-radius: 4px; background: {c};"></span>' if kind == 'solid' else f'<span style="width: 8px; height: 8px; border-radius: 4px; border: 1.3px solid {c}; box-sizing: border-box;"></span>'
        rail += f'<span style="display: flex; flex-direction: column; align-items: center; gap: 4px; flex: none;">{mark}<span style="font-family: {MONO}; font-size: 10px; font-weight: 700; color: {INK if kind == "solid" else HINT};">{t}</span><span class="fn" style="font-size: 9px; color: {HINT};">{l}</span></span>'
    rail += '</div>'
    return (f'<div style="border-top: 1px solid rgba(27,23,20,0.16); border-bottom: 1px solid rgba(27,23,20,0.16); padding: 13px 0 12px;">{EYE("ON THE TRIP &middot; DAY 3 OF 13", "SORRENTO &middot; " + now)}'
            f'<div style="font-family: {SERIF}; font-size: 20px; line-height: 25px; font-weight: 600; color: {INK}; margin-top: 8px; text-wrap: balance;">{title}</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{sub}</div>' + rail + '</div>')
S_MORNING = strip_variant('NOW', 'Lunch at the harbour at one; the walk under the wall at four, once it is in shade.', 'Nothing after six. The evening is open.', [('8:40', 'NOW', 'solid', INK), ('1:00', 'LUNCH', 'solid', GOLD), ('4:00', 'THE WALK', 'solid', GOLD), ('6:00', 'OPEN', 'hollow', HINT)])
S_AFTERNOON = strip_variant('1:20 PM', 'Lunch, now. The walk under the wall at four, once it is in shade.', 'Nothing after six. The evening is open.', [('1:20', 'NOW', 'solid', INK), ('4:00', 'THE WALK', 'solid', GOLD), ('6:00', 'OPEN', 'hollow', HINT)])
S_EVENING = strip_variant('6:10 PM', 'The evening is open.', 'Nothing more today. Tomorrow, Capri by the 11:20.', [('6:10', 'NOW', 'solid', INK), ('11:20', 'TOMORROW', 'hollow', HINT)])
def frame(inner): return phone_open() + inner + '<div style="flex-grow: 1;"></div>' + tabbar() + '</div>'
def timed(kick, text, stamp_, last=False, mutedtext=False):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    return (f'<div style="display: flex; align-items: flex-start; gap: 12px; padding: 9px 0;{b}">'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 14.5px; line-height: 19px; color: {MUTE if mutedtext else INK};">{text}</div>'
            + (f'<div class="fn" style="color: {HINT}; margin-top: 3px;">{kick}</div>' if kick else '')
            + f'</div><span class="fn" style="color: {HINT}; flex: none; padding-top: 2px; white-space: nowrap;">{stamp_}</span></div>')
def day_page():
    inner = page_head('DAY &middot; AUG 18 2026 &middot; IN THE COAST &middot; NICE &rarr; ROME', 'Wednesday, August 18', 'Sorrento, day three.')
    inner += sect('This morning &middot; what Home showed') + gut(
        timed('', '31&deg; by two &middot; the shade after', 'TODAY')
        + timed('', 'Nothing after six &middot; the evening is open', 'TODAY')
        + timed('', 'The boat tomorrow &middot; 11:20', 'AS OF 8:40', last=True))
    inner += sect('Changed since') + gut(
        timed('', 'The boat &middot; now 12:40, was 11:20', '3:10 PM', last=True) + door('Today&rsquo;s plan, as it is now'))
    inner += sect('The record of the day so far') + gut(
        timed('', 'The market, the stairs &middot; four photographs', '10:15&ndash;11:40')
        + timed('', 'Lunch &middot; the counter by the harbour', '1:05', last=True))
    return frame(inner)
def home_changed():
    """The trip-day scroll later the same day, after the operator moved the boat."""
    inner = anchor('SORRENTO &middot; WEDNESDAY', '3:20 PM')
    inner += read('The boat tomorrow is 12:40 now.', 'The walk under the wall at four, once it is in shade.')
    inner += gut(S_AFTERNOON.replace('1:20', '3:20').replace('Lunch, now. The walk under the wall at four, once it is in shade.', 'The walk under the wall at four, once it is in shade.').replace('NOW</span>', 'NOW</span>'), top=22)
    inner += gut(f'<div style="background: {CARD}; border-radius: 16px; padding: 12px 14px 10px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                 + EYE('TOMORROW&rsquo;S BOAT', 'CHANGED 3:10')
                 + f'<div style="font-size: 13.5px; line-height: 19px; color: {INK}; margin-top: 8px;">Now 12:40, was 11:20 &middot; the operator moved it. Boarding from the far quay, 12:25.</div>'
                 + fn('THE OPERATOR&rsquo;S NOTICE &middot; YOUR TICKET STANDS', 6) + door('Today&rsquo;s plan') + '</div>', top=14)
    inner += sect('In motion') + gut(money_row() + row(facepile(['M', 'A', 'N']), 'Dinner at ours &middot; Aug 29 &middot; ' + mute('you host &middot; Maya and Alex'), last=True))
    inner += ending([('WED', 'today', 'today'), ('THU', 'gold', 'Capri'), ('FRI', 'h', ''), ('SAT', 'h', ''), ('SUN', 'h', ''), ('MON', 'ink', 'Rome'), ('TUE', 'h', '')], 'Tomorrow, Capri by the 12:40.')
    return frame(inner)
def boat_page():
    inner = page_head('FERRY &middot; ALILAURO &middot; AUG 19 2026', 'Sorrento &rarr; Capri', 'One ticket, one email. Checked once this morning at 6:12.')
    card = (f'<div style="background: {CARD}; border-radius: 16px; padding: 16px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
            f'<div style="display: flex; align-items: baseline; justify-content: space-between;"><span style="font-family: {SERIF}; font-size: 34px; line-height: 38px; font-weight: 600;">SOR</span><span class="fn" style="color: {HINT};">&#8776;</span><span style="font-family: {SERIF}; font-size: 34px; line-height: 38px; font-weight: 600;">CAPRI</span></div>'
            f'<div style="display: flex; justify-content: space-between; margin-top: 2px;"><span class="fn" style="color: {HINT};">SORRENTO &middot; THE FAR QUAY</span><span class="fn" style="color: {HINT};">MARINA GRANDE</span></div>'
            f'<div style="display: flex; gap: 18px; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(27,23,20,0.07);"><div><div class="fn" style="color: {HINT};">DEPARTS</div><div style="font-family: {MONO}; font-size: 15px; font-weight: 700; margin-top: 2px;">11:20</div></div><div><div class="fn" style="color: {HINT};">BOARDS</div><div style="font-family: {MONO}; font-size: 15px; font-weight: 700; margin-top: 2px;">11:05</div></div><div><div class="fn" style="color: {HINT};">CROSSING</div><div style="font-family: {MONO}; font-size: 15px; font-weight: 700; margin-top: 2px;">25 MIN</div></div></div></div>')
    inner += gut(card, top=22)
    inner += sect('This morning&rsquo;s check') + gut(row(dot('solid', INK), 'Boards from the far quay &middot; ' + mute('be on it by 11:05')) + row(dot('solid', INK), 'The 9:40 sold out by nine last week &middot; ' + mute('the 11:20 has room'), last=True) + fn('THE OPERATOR&rsquo;S TIMETABLE + YOUR TICKET &middot; CHECKED ONCE AT 6:12, NOT WATCHED', 8))
    inner += gut(door('Open the email') + door('Back to Home'), top=14)
    return frame(inner)
def claim_page():
    inner = page_head('CLAIM &middot; THE CANCELLED ROME FLIGHT &middot; FILED AUG 15', '&euro;212, owed to you', 'The airline is reviewing. Nothing for you to do; Home says so once when that changes.')
    inner += sect('The record') + gut(row(dot('solid', INK), 'Filed &middot; ' + mute('Aug 15 &middot; the reference is in the email')) + row(dot('solid', GOLD), 'Airline reviewing &middot; ' + mute('since Aug 16')) + row(dot('hollow'), 'Paid &middot; ' + mute('not yet'), last=True) + fn('THE CLAIM EMAIL + THE AIRLINE&rsquo;S STATUS PAGE', 8))
    inner += gut(door('Open the email') + door('Back to Home'), top=14)
    return frame(inner)
def check_card():
    return (f'<div style="background: {CARD}; border-radius: 16px; padding: 16px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07); width: 393px; box-sizing: border-box;">'
            f'<div class="fn" style="color: {HINT};">HOME &middot; ON A TRIP DAY</div><div style="font-family: {SERIF}; font-size: 20px; line-height: 25px; font-weight: 600; margin-top: 6px;">What Home does not do</div>'
            f'<div style="font-size: 13.5px; line-height: 19px; color: {INK2}; margin-top: 8px;">No push about the boat, and no reminder for the quay unless you ask for one. The claim is never a card; when it is paid it appears once in &ldquo;Since you last looked&rdquo; and then is an ordinary row. The strip never asks; at six it says the evening is open and stops.</div>'
            f'<div class="fn" style="color: {HINT}; margin-top: 10px;">SEAT LAW &middot; DELETION TEST ON 07</div></div>')
def colf(phone, shead, kick, title, fnt):
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;"><div class="shead" style="color: {GOLDD}; margin-bottom: 10px;"><span>{shead}</span><span class="rule"></span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{kick}</div><div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{title}</div><div style="{CAPTION}">{fnt}</div></div>{phone}</div>')
CAPTION = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;"
def row_nine():
    divider = ('<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">ROW NINE &middot; TD &middot; AN ORDINARY DAY ON THE TRIP</div>'
               f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">The trip day, and what its three new objects open onto</div>'
               f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">Day three of thirteen in Sorrento (Aug 18): the morning scroll; the same day at 3:20 after the operator moved the boat; the day page it opens (Life P3.4); the boat from the work receipt; the claim from the money row; and what Home does not do. Added 2026-09-08 with the third selected state on 03, reconciled with Life and Plans on 2026-09-09.</div></div>')
    cols = [colf(TRIP, 'WEDNESDAY AUG 18 &middot; DAY THREE &middot; 8:40 AM', '1 &middot; ENCOUNTER &middot; THE TRIP-DAY SCROLL', 'The strip leads; the receipt sits under it', 'The selected scroll from 03. The strip is the dominant; the receipt never renders alone; the money row is a row.'),
            colf(home_changed(), 'THE SAME DAY &middot; 3:20 PM &middot; THE OPERATOR MOVED THE BOAT', '2 &middot; THE CHANGED HOME READING', 'Home re-reads; the change is the read', 'Sept 9 item 4: not only the morning&rsquo;s checked-once frame. The read names the change, the strip drops the stops that have passed, and the receipt carries old value, new value and the time it changed, with one door to today&rsquo;s plan. Plans owns the change and the door&rsquo;s destination (Life P3.4).'),
            colf(day_page(), 'OPENED FROM THE STRIP &middot; A LIFE-OWNED READER, IN HOME&rsquo;S STACK', '3 &middot; OPEN &middot; THE DAY PAGE', 'This morning, what changed since, the day so far', 'Life P3.4 verbatim in structure: this morning&rsquo;s reading with its time, what changed since with its time and one door to today&rsquo;s plan, then the record of the day so far. The reader is Life-owned and stays in Home&rsquo;s stack &mdash; the tab bar still reads Home, because the person did not cross roots. Ask from here binds to the plan as it is now. Disconnected, this page is Life P3.5: originals on the phone, the plan as of its last update, nothing guessed.'),
            colf(boat_page(), 'FROM THE RECEIPT &middot; A LIFE-OWNED READER, IN HOME&rsquo;S STACK', '4 &middot; INSPECT &middot; THE BOAT, THIS MORNING', 'The pass, and this morning&rsquo;s check', 'The morning state, before the 3:10 change on frames 2 and 3. One tap from the receipt to the ticket; the two checked lines are the receipt&rsquo;s own source. A check made once at 6:12, not a watch (Plans 12 W1). The reader stays in Home&rsquo;s stack.'),
            colf(claim_page(), 'FROM THE MONEY ROW &middot; A LIFE-OWNED READER, IN HOME&rsquo;S STACK', '5 &middot; INSPECT &middot; THE CLAIM', '&euro;212, owed to you', 'The money row opens its record: filed, reviewing, not yet paid. No reminder and no nudge; when paid, once in since-you-looked (07).'),
            colf(check_card(), 'CHECK', '6 &middot; NO RETURN', 'What Home does not do', 'Seat law: no push, no reminder unless asked, never a card for the claim, the strip stops at six.')]
    return divider + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols) + '</div>'
def strip_form_section():
    def cell(v, cap, note):
        return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column; gap: 8px;"><div class="kick" style="color: {GOLDD};">{cap}</div>'
                f'<div style="width: 393px; background: {PAPER}; padding: 8px 22px 22px; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">{v}</div><div style="{CAPTION}">{note}</div></div>')
    head = ('<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">THE TEMPORAL STRIP &middot; ITS FORM ACROSS THE DAY &middot; 2026-09-08</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">One band, three moments: what is true now, and when the day stops asking</div>'
            f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">The strip re-reads as the day moves; stops that have passed leave the rail, the sentence shortens, and at six the band says the evening is open and nothing more. It never grows a control.</div></div>')
    cells = [cell(S_MORNING, '8:40 &middot; THE MORNING', 'Four stops. The next two are gold; the open evening is hollow.'), cell(S_AFTERNOON, '1:20 PM &middot; LUNCH, NOW', 'The passed stop is gone from the rail; the sentence starts at now.'), cell(S_EVENING, '6:10 PM &middot; THE EVENING', 'The band closes the day and names tomorrow; no CTA, no summary.')]
    return head + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cells) + '</div>'
b = open(f'{IN}/08b - Seam with Life - Home to Life.dc.html').read()
head = b[:b.find('<div style="width: 2480px')] if '<div style="width: 2480px' in b else b[:b.find('<div style="width: 2')]
board = ('<div style="width: 2920px; min-height: 3200px; background: #F4F0E7; box-sizing: border-box; padding: 40px 44px 60px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: #1B1714;">'
         '<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 26px;"><div class="kick">VESPER &middot; HOME &middot; 08c &middot; SEAM WITH LIFE &middot; THE TRIP DAY &middot; 2026-09-08</div>'
         f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">08c &middot; Home to Life, on a trip day</div>'
         f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">A continuation of 08b, kept as its own board so no board passes 12,000px. The ninth whole encounter: the trip-day scroll selected on 03, and where its three new objects open.</div></div>'
         + row_nine().replace('margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);', 'margin-top: 0;') + '</div>')
open(f'{OUT}/08c - Seam with Life - The Trip Day.dc.html', 'w').write(head + board + '</x-dc></body></html>')
open(f'{OUT}/_strip_section.html', 'w').write(strip_form_section())
print('08b and 09 written')
