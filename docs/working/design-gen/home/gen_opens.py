"""14 - Three Ordinary Opens (2026-09-08 consolidation, bounded composition pass items 1 and 2).
Row one: a newcomer in a supported locality (New York) with an explicitly bounded supply set, three ordinary opens, no new
contribution, one expired offering. Row two: the same Sunday evening under three different wanted kinds of help.
Usage: python3 gen_opens.py <polished_dir> <out_dir>
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
G = '/Users/feihuyan/travel-workspace/docs/working/design-gen/home/gen_trip.py'
src = open(G).read().split("# ---- board edits")[0]
sys.argv = ['x', IN, OUT]; exec(src.replace("LIVE, OUT = sys.argv[1], sys.argv[2]\nos.makedirs(OUT, exist_ok=True)", "LIVE, OUT = sys.argv[1], sys.argv[2]"))
def h03(): return open(f'{IN}/03 - Persona B - Back from Europe.dc.html').read()
H02 = open(f'{IN}/02 - Persona A - The New Yorker.dc.html').read()
CAPTION = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;"
def slice_unit(h, marker, start_pat, end_pats):
    i = h.find(marker); s = h.rfind(start_pat, 0, i); ends = [x for x in (h.find(e, i) for e in end_pats) if x > 0]; return h[s:min(ends)]
# donors from the selected Sunday scroll: the skillet method (bare unit) and the harbour-book card
def element_around(h, marker, must=('radius',)):
    """The smallest <div ...> that contains the marker and whose opening tag mentions every word in `must`."""
    i = h.find(marker); pos = i
    for _ in range(40):
        s = h.rfind('<div', 0, pos); tag = h[s:h.find('>', s) + 1]
        depth = 0; e = None
        for m in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if m.group() == '<div' else -1
            if depth == 0: e = s + m.end(); break
        if e and e > i and all(w in tag for w in must): return h[s:e]
        pos = s - 1
    raise SystemExit('no bounding element for ' + marker)
BOOK = element_around(H02, 'THE HARBOR BOOK &middot; CH. 4')
SKILLET = element_around(H02, 'The crust split where the pan was coldest', must=('flex-direction: column',))
def lane(lab, big, sub): return f'<div style="flex: 1;"><div class="fn" style="color: {HINT};">{lab}</div><div style="font-family: {SERIF}; font-size: 22px; line-height: 26px; font-weight: 600; color: {INK}; margin-top: 3px;">{big}</div><div style="font-size: 12px; line-height: 16px; color: {MUTE};">{sub}</div></div>'
def unit(title, body='', lanes='', source=''):
    return (f'<div style="display: flex; flex-direction: column;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK}; text-wrap: balance;">{title}</div>'
            + (f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{body}</div>' if body else '') + (f'<div style="display: flex; gap: 18px; margin-top: 10px;">{lanes}</div>' if lanes else '') + (fn(source, 6) if source else '') + '</div>')
def fact(kick, text, muted=False, last=True):
    return (f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 10px 0; border-top: 1px solid {HAIR};{" border-bottom: 1px solid " + HAIR + ";" if last else ""}"><span class="fn" style="color: {HINT};">{kick}</span>'
            f'<span style="font-size: 14px; line-height: 19px; color: {MUTE if muted else INK};">{text}</span></div>')
def sample_compact():
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 10px 0;"><span style="font-family: {MONO}; font-size: 9px; font-weight: 700; letter-spacing: 1px; color: {HINT}; border: 1px dashed {HINT}; border-radius: 10px; padding: 2px 7px; flex: none;">SAMPLE</span>'
            f'<span style="font-size: 13.5px; line-height: 18px; color: {MUTE}; flex: 1;">A made-up ticket, read the way yours would be: doors, the last train, the way home.</span></div>' + door('Try with yours'))
def seam(days, line):
    out = '<div style="margin: 40px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">'
    for lab, kind, text in days:
        if kind == 'today': m, lc, tc = f'<span class="daym" style="background: {INK};"></span>', INK, INK
        elif kind == 'gold': m, lc, tc = f'<span class="daym" style="background: {GOLD};"></span>', INK, INK
        else: m, lc, tc, text = '<span class="daym" style="border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;"></span>', HINT, 'transparent', '.'
        out += f'<div class="day"><span class="dayl" style="color: {lc};">{lab}</span>{m}<span style="font-size: 10px; color: {tc};">{text}</span></div>'
    out += '</div></div>' + (f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: {INK};">{line}</div></div>' if line else '<div style="height: 10px;"></div>')
    return out
def phone(inner): return phone_open() + inner + '<div style="flex-grow: 1;"></div>' + tabbar() + '</div>'

# --- the ledgered set, as Places 03.3 draws and dates it (the pair with Home 14) -------------------------------------
BOOK_CARD = element_around(H02, 'THE HARBOR BOOK &middot; CH. 4')
def book_row(): return row(dot('solid', GOLD), 'The pumps under the park &middot; ' + mute('The Harbor Book, ch. 4 &middot; 4 min'), last=True)
L_NOTICE = ('THE L &middot; AFTER 11 PM, MON&ndash;THU', 'Single-tracking between Bedford and 1st; daytime is normal.')
def read_pair(title, sub): return read(title, sub)
def open1(benefit_led=False):
    """14.1 · Tuesday 8:05. A: the reading owns the headline (as drawn). B: the strongest received benefit does."""
    if benefit_led:
        inner = anchor('NEW YORK &middot; TUESDAY', '8:05 AM') + read('Registration for the Open House timed sites opens today at noon.', 'Walk-in sites need none &middot; clear and cool &middot; low water on the pier Saturday from 2:40.')
        inner += gut(fact('OPEN HOUSE &middot; OCT 17&ndash;18 &middot; OHNY', 'Timed sites: registration opens today at noon and closes Thursday. Walk-in sites need none.', last=False) + fact(*L_NOTICE), top=22)
    else:
        inner = anchor('NEW YORK &middot; TUESDAY', '8:05 AM') + read('Clear and cool. Low water on the pier Saturday from 2:40.', 'You chose New York. Nothing about you is held.')
        inner += sect('This week in the city') + gut(fact('OPEN HOUSE &middot; OCT 17&ndash;18 &middot; OHNY', 'Registration for the timed sites opens today at noon; walk-in sites need none.', last=False) + fact(*L_NOTICE))
    inner += sect('Worth reading') + gut(BOOK_CARD)
    inner += gut(sample_compact(), top=22)
    if benefit_led:
        inner += gut(f'<div class="fn" style="color: {HINT};">YOU CHOSE NEW YORK &middot; NOTHING ABOUT YOU IS HELD</div>', top=26)
    inner += seam([('TUE', 'today', 'today'), ('WED', 'h', ''), ('THU', 'gold', 'registration'), ('FRI', 'h', ''), ('SAT', 'h', ''), ('SUN', 'h', ''), ('MON', 'h', '')], 'Registration closes Thursday.')
    return phone(inner)
def open2():
    """14.2 · Thursday 7:40 pm. One change, one newly named item; nothing repeated."""
    inner = anchor('NEW YORK &middot; THURSDAY', '7:40 PM') + read('Open House registration closes tonight.', 'Walk-in sites need none &middot; clear, 47&deg; &middot; the flea under the bridge on Saturday.')
    inner += gut(fact('OPEN HOUSE &middot; OCT 17&ndash;18 &middot; OHNY', 'The timed sites close at midnight. The walk-in sites need no registration at all.', last=False)
                 + fact('THE FLEA &middot; SATURDAY, 8 TO 3 &middot; THE MARKET&rsquo;S OWN NOTICE', 'Under the bridge, Saturdays through October; the bread stall sells out by ten.', last=False)
                 + fact('THE L', 'Single-tracking after 11 tonight, as on Monday to Wednesday; daytime is normal.'), top=22)
    inner += sect('Worth reading') + gut(book_row())
    inner += gut(sample_compact(), top=22)
    inner += seam([('THU', 'today', 'today'), ('FRI', 'h', ''), ('SAT', 'gold', 'the flea'), ('SUN', 'h', ''), ('MON', 'h', ''), ('TUE', 'h', ''), ('WED', 'h', '')], 'Saturday, the flea from eight.')
    return phone(inner)
def open3(unseen=False):
    """14.3 · Saturday 9:30. The honest floor; 14.3b the same open when the set still holds something unseen."""
    inner = anchor('NEW YORK &middot; SATURDAY', '9:30 AM') + read('Clear, 41&deg;. The flea is on until three.', 'Nothing else has changed since Thursday.')
    inner += gut(unit('The flea, under the bridge, until three', 'The bread stall sells out by ten; the rest of the stalls hold all day.', '', 'SATURDAYS THROUGH OCTOBER &middot; THE MARKET&rsquo;S OWN NOTICE') + door('Directions'), top=22)
    if unseen:
        inner += sect('Still open') + gut(unit('The timed sites closed on Thursday. The walk-in sites, as before, need no registration', 'October 17 and 18; you can turn up at any of them.', '', 'OHNY &middot; THE WALK-IN LIST &middot; SAID ON TUESDAY AND THURSDAY TOO') + door('The walk-in sites, in Places'))
        inner += sect('Also this week') + gut(fact('THE L', 'Normal today; single-tracking after 11 PM, Monday to Thursday.', muted=True))
        inner += sect('Worth reading') + gut(book_row())
        inner += seam([('SAT', 'today', 'today'), ('SUN', 'h', ''), ('MON', 'h', ''), ('TUE', 'h', ''), ('WED', 'h', ''), ('THU', 'h', ''), ('FRI', 'h', '')], 'The Open House is five weeks out; the walk-ins need nothing.')
    else:
        inner += sect('Also this week') + gut(fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites closed Thursday.', muted=True, last=False) + fact('THE L', 'Normal today; single-tracking after 11 PM, Monday to Thursday.', muted=True))
        inner += sect('Worth reading') + gut(book_row())
        inner += seam([('SAT', 'today', 'today'), ('SUN', 'h', ''), ('MON', 'h', ''), ('TUE', 'h', ''), ('WED', 'h', ''), ('THU', 'h', ''), ('FRI', 'h', '')], 'Nothing else today.')
    return phone(inner)
# row two: the same Sunday evening, three kinds of wanted help
DINNER = row(facepile(['M']), 'Dinner in Brooklyn &middot; tonight at eight &middot; ' + mute('with Maya &middot; arranged'), last=True)
def evening(kind):
    inner = anchor('NEW YORK &middot; SUNDAY', '5:40 PM') + read('Sunday evening. Dinner at eight in Brooklyn.', 'Clear, 49&deg; by eight &middot; the river side runs colder; take the avenue.')
    if kind == 'quiet':
        inner += sect('In motion') + gut(DINNER)
        inner += gut(door('Everything in Life'), top=22)
        inner += seam([('SUN', 'today', 'today'), ('MON', 'h', ''), ('TUE', 'gold', 'dentist'), ('WED', 'h', ''), ('THU', 'h', ''), ('FRI', 'gold', 'the show'), ('SAT', 'h', '')], 'Tonight, Brooklyn with Maya.')
    elif kind == 'steered':
        card = (f'<div style="background: {CARD}; border-radius: 16px; padding: 16px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                f'<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: #2A384B; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: #2A384B;">TONIGHT &middot; CLOSER, SOMEWHERE YOU CAN TALK</span></div>'
                f'<div style="font-family: {SERIF}; font-size: 20px; line-height: 25px; font-weight: 600; margin-top: 8px; text-wrap: balance;">Bar Blondeau, two streets from Maya&rsquo;s: quiet after nine, no music</div>'
                f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Eight minutes from the restaurant on foot; the avenue, not the river. Nothing booked.</div>'
                + fn('FOR TONIGHT &middot; YOU ASKED FOR CLOSER AND QUIETER', 10) + door('Directions') + '</div>')
        inner += gut(card, top=22)
        inner += sect('In motion') + gut(DINNER)
        inner += seam([('SUN', 'today', 'today'), ('MON', 'h', ''), ('TUE', 'gold', 'dentist'), ('WED', 'h', ''), ('THU', 'h', ''), ('FRI', 'gold', 'the show'), ('SAT', 'h', '')], 'Tonight, Brooklyn with Maya.')
    else:
        inner += gut(SKILLET, top=22)
        inner += sect('In motion') + gut(DINNER)
        inner += seam([('SUN', 'today', 'today'), ('MON', 'h', ''), ('TUE', 'gold', 'dentist'), ('WED', 'h', ''), ('THU', 'h', ''), ('FRI', 'gold', 'the show'), ('SAT', 'h', '')], 'Tonight, Brooklyn with Maya.')
    return phone(inner)
def colf(ph, shead, kick, title, fnt):
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;"><div class="shead" style="color: {GOLDD}; margin-bottom: 10px;"><span>{shead}</span><span class="rule"></span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{kick}</div><div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{title}</div><div style="{CAPTION}">{fnt}</div></div>{ph}</div>')
def rowdiv(kick, title, sub, first=False):
    return (f'<div style="{"margin-top: 0;" if first else "margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);"} display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">{kick}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">{title}</div><div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">{sub}</div></div>')
SUPPLY = ('<div style="margin-top: 26px; display: flex; gap: 46px;"><div style="width: 1250px; font-size: 13px; line-height: 19px; color: #2C2622;"><b>The New York bounded set &middot; revision 2 &middot; 2026-09-09 &middot; Home leads.</b> Places 03.3 is the paired frame (&ldquo;the same set Home 14.3 opens&rdquo;): the same locality, day and hour, Home showing what the person receives and Places the same set as a field. The items and their dates: the flea, under the bridge, Saturdays through October, 8 to 3, the bread stall by ten (the market&rsquo;s own notice); Open House New York, October 17&ndash;18, timed registration Tuesday noon to Thursday, walk-in sites need none (OHNY); the L, after 11 PM Monday to Thursday, daytime normal, end date unknown (MTA); the forecast and tide, today clear 41&deg;, low water 2:40 to 5, high 8:40 (two stations, the tide table); The Harbor Book chapter four, no expiry. No friends, no history, no chosen places, no import; nothing generated on open; the sample ticket is the one fixed demonstration and retires after it is ignored twice. Designed supply, not verified provider supply. <b>Revision history:</b> revision 1 (2026-09-08) was the Red Hook set &mdash; the film on the lawn, the greenmarket, the Print Room, the pierogi table, the 1911 sill, 58&deg;, the L ending Friday &mdash; and is superseded for this pair; those items remain Places&rsquo; own on 03.1 and 03.2. The two owners exchanged fixtures in opposite directions on 09-09; this revision resolves that crossing. Home leads it and has drawn it on 14.1&ndash;14.3b; <b>Places 03.3 confirms revision 2 before changing its receiving view.</b> Recorded on 07 (decision log) and here; no separate fixture document.</div><div style="width: 1250px; font-size: 13px; line-height: 19px; color: #2C2622;"><b>Where each item appears:</b> the flea &mdash; named on 14.2, the one live thing on 14.3 and 14.3b. Open House &mdash; opens at noon on 14.1, closes tonight on 14.2, closed on 14.3, and its walk-in sites are the unseen part on 14.3b. The L &mdash; 14.1, and as tonight&rsquo;s last single-tracking on 14.2. Forecast and tide &mdash; the reading on all three. The chapter &mdash; the card on 14.1, a row on 14.2 and 14.3.<br><br><b>Value and effort, open by open:</b> Tuesday gives a deadline the person can still act on and one thing to understand; Thursday gives that deadline&rsquo;s last night and names Saturday; Saturday gives the one live thing. Effort asked of the person: none on any open; nothing is required to receive the next.</div></div>')

row1 = [colf(open1(), 'TUESDAY 8:05 &middot; 14.1 A &middot; AS DRAWN', '14.1 A &middot; THE READING OWNS THE HEADLINE', 'The forecast is the largest statement', 'The 30px read carries the weather and tide, and the account line sits directly under it; the benefit the person can act on today (registration opens at noon) is a 14px row below the fold of the first viewport. Same content as B.'),
        colf(open1(benefit_led=True), 'TUESDAY 8:05 &middot; 14.1 B &middot; THE BENEFIT OWNS THE HEADLINE', '14.1 B &middot; COMPARISON', 'The one thing today makes possible leads', 'Sept 9 item 1: the same content, re-ranked. The registration window owns the read; the forecast and tide keep their place on the second line, where the current job earns it; the account line drops to one mono line at the foot. No new summary, section or hero rule.'),
        colf(open2(), 'THURSDAY 7:40 PM &middot; 14.2 &middot; ONE CHANGE', '14.2 &middot; SECOND OPEN', 'The deadline arrives; the flea is named', 'The change is the registration closing tonight, with the walk-ins named beside it so the closing is not the whole story. The flea is named for Saturday; the chapter drops to a row, unrepeated.'),
        colf(open3(), 'SATURDAY 9:30 &middot; 14.3 &middot; THE HONEST FLOOR', '14.3 &middot; THIRD OPEN', 'One live thing, one closed, a complete ending', 'When the set holds nothing further: the flea is the one live item, the closed registration is shown as closed rather than dropped, the sample has retired, and the page ends. A finite scroll may end; this is the floor, not the model.'),
        colf(open3(unseen=True), 'SATURDAY 9:30 &middot; 14.3b &middot; THE SAME OPEN, A REMINDER AFTER THE DEADLINE', '14.3b &middot; A REMINDER, NOT A NEW INSIGHT', 'The closed door has an open one beside it', 'Corrected 09-09: the walk-ins were already explained on 14.1 A and B and again on 14.2, so this is not new information and is not labelled unseen. It is a reminder, useful again precisely because the deadline has now passed and the person may read &ldquo;closed Thursday&rdquo; as the end of it. 14.3&rsquo;s finite ending is equally valid; the chapter is not re-offered, because its idea was already delivered on Tuesday.')]
row2 = [colf(evening('quiet'), 'SUNDAY 5:40 PM &middot; NOTHING WANTED', 'A &middot; AS IT STANDS', 'A complete low-demand evening', 'The dinner row and the way there. No card is added to make the evening valid.'),
        colf(evening('steered'), 'SUNDAY 5:40 PM &middot; &ldquo;CLOSER, SOMEWHERE WE CAN TALK&rdquo;', 'B &middot; STEERED, FOR TONIGHT', 'The offering changes; nothing about the person is kept', 'H9: one contextual continuation after a useful result, scoped to tonight and not kept as a preference. Plans 08 leads contextual assistance; Home receives the scoped result. PROVISIONAL until Plans confirms the treatment; the venue is a fixture.'),
        colf(evening('home'), 'SUNDAY 5:40 PM &middot; STAYING IN FIRST', 'C &middot; AT HOME', 'The restful material leads', 'The skillet method from the ordinary Sunday leads; the dinner row stays. More history did not mean more content.')]
h = h03(); head = h[:h.find('<div style="width: 1820px')]
board = (f'<div style="width: 2740px; min-height: 5200px; background: #F4F0E7; box-sizing: border-box; padding: 40px 44px 60px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">'
         f'<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 26px;"><div class="kick">VESPER &middot; HOME &middot; 14 &middot; THREE ORDINARY OPENS &middot; CONSOLIDATION PASS &middot; 2026-09-08</div>'
         f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">14 &middot; Three ordinary opens with a bounded supply, and one evening three ways</div>'
         f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">The consolidation assignment&rsquo;s composition pass, items 1 and 2. Row one: a newcomer in New York across three opens with no new contribution, on the supply set Places 03.3 draws and dates as the pair with this board. The first open is drawn twice to compare which statement owns the headline, and the third twice to tell an honest ending from an unseen part of a seen item. Row two compares the same Sunday evening under three kinds of wanted help. PROPOSED compositions; the sibling leads (Plans for contextual assistance) are named where a treatment is theirs.</div></div>'
         + rowdiv('ROW ONE &middot; BOUNDED SUPPLY &middot; A NEWCOMER, THREE OPENS, NOTHING ASKED', 'Receiving stays useful without generation, setup or another card', 'One supported locality; the set is declared below and dated by Places 03.3. What wins each open: the benefit the person can act on, one change, an honest expiry, a complete quiet ending.', first=True)
         + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row1) + '</div>' + SUPPLY
         + rowdiv('ROW TWO &middot; THE SAME EVENING, THREE KINDS OF WANTED HELP', 'An open evening need not be filled; steering changes the offering without a profile', 'Sunday at 5:40 with dinner at eight already arranged. A: nothing wanted. B: the person says &ldquo;closer, somewhere we can talk&rdquo;. C: staying in first. More history does not mean more content.')
         + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>' + '</div>')
open(f'{OUT}/14 - Three Ordinary Opens.dc.html', 'w').write(head + board + '</x-dc></body></html>'); print('14 written')
