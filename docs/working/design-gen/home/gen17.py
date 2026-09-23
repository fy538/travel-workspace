"""Board 17 — Delivery and Return (September 12 coverage assignment).
One delivery/return canvas: a private requested result, a friend's offering and a consequential change arrive while
away; each is shown as entry -> useful in-app value -> the exact destination -> return to the same Home context, with
the interrupted cases (stale/deleted destination, authentication interruption, denied notification permission).
Donors: Home 02 (the selected ordinary scroll and its units), 11 (return and continuity), 12 (Chat aperture, Why this,
the three degraded states), 16 (the shared reader continuation), Plans 90 (recovery states), Entity 05 (row opening and
unavailable). Shared construction: OriginalReader (open, full, withdrawn), Notice, .vdl-door. Platform rules reused
from travel-app/docs/surfaces/notifications-alerts/contract.md — nothing here re-specifies that surface.
Usage: python3 gen17.py <in_dir> <out_dir>
"""
import sys, os, re
IN, OUT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], IN, OUT]
import gen_vdl as G

MONO, SERIF, SANS, CHEV, HATCH = G.MONO, G.SERIF, G.SANS, G.CHEV, G.HATCH
INK, MUTE, HINT, GOLD, GOLDD, CARD, PAPER, OX = '#1B1714', '#6E6862', '#8F877C', '#B0853A', '#8A6628', '#FBF7EC', '#EFEAE0', '#7A2E2E'
fn, cell, notes, gold, ink = G.fn, G.cell, G.notes, G.gold_door, G.ink_door
opener, TAB = G.home_parts()

def anchor(time, right='N'):
    return (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">'
            f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">NEW YORK &middot; SUNDAY</span>'
            f'<span class="fn" style="margin-left: auto;">{time}</span><span style="width: 24px; height: 24px; border-radius: 999px; background: #4A3428; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-left: 10px; flex: none;">{right}</span></div></div>')
def read(title, sub):
    return (f'<div style="padding: 6px 22px 0 22px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 34px; letter-spacing: -0.01em; text-wrap: balance;">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 7px;">{sub}</div></div>')
def sect(name, mark=''):
    m = f'<span class="fn" style="color: {HINT};">{mark}</span>' if mark else ''
    return (f'<div style="padding: 34px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;">'
            f'<span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{name}</span>{m}<span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')
def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'
def unit(title, body='', meta='', extra='', top=0):
    b = f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{body}</div>' if body else ''
    m = fn(meta, mt=6) if meta else ''
    return gut(f'<div style="display: flex; flex-direction: column;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK}; text-wrap: balance;">{title}</div>{b}{extra}{m}</div>', top)
def row(mark, text, last=False, sub=''):
    b = '' if last else ' border-bottom: 1px solid rgba(27,23,20,0.06);'
    s = f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{sub}</div>' if sub else ''
    return (f'<div class="row" style="padding: 10px 0; align-items: flex-start;{b}">{mark}<div style="flex: 1; min-width: 0;">'
            f'<div style="font-size: 15px; line-height: 20px; color: {INK};">{text}</div>{s}</div><span style="padding-top: 3px;">{CHEV}</span></div>')
def facepile(letters):
    out = '<span style="display: inline-flex; align-items: center; flex: none; padding-top: 2px;">'
    for i, l in enumerate(letters):
        bg = '#4A3428' if l == 'N' else INK
        out += (f'<span style="width: 26px; height: 26px; border-radius: 999px; background: {bg}; color: {CARD}; font-size: 10px; font-weight: 700; '
                f'display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {PAPER}; margin-left: {0 if i == 0 else -8}px;">{l}</span>')
    return out + '</span>'
def glyph(d, op='0.62'):
    return f'<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex: none; opacity: {op}; margin-top: 3px;"><path d="{d}" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
HALL = 'M2.4 12.6 V5.4 Q7.5 1.4 12.6 5.4 V12.6 M5.4 12.6 V8.6 Q7.5 6.6 9.6 8.6 V12.6 M1.4 12.6 H13.6'
SINCE = f'<div style="padding: 20px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><span style="height: 1px; flex: 1; background: rgba(27,23,20,0.12);"></span><span class="fn" style="color: {HINT};">SINCE YOU LAST LOOKED &middot; 9:10 AM</span><span style="height: 1px; flex: 1; background: rgba(27,23,20,0.12);"></span></div></div>'
def phone(*parts): return opener + ''.join(parts) + '<div style="flex-grow: 1;"></div>' + TAB
def reader(props): return f'<dc-import name="OriginalReader" {props}></dc-import>'
NOTE = ('density="open" author="Maya" meta="AUG 30 · TO YOU" words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." '
        'place="Lilia" placeMeta="TONIGHT AT EIGHT · WITH MAYA · ARRANGED" door="Tonight, at Lilia" hint-size="349px,200px"')

# ---- Row 1 · entry, while away ------------------------------------------------------------------
def os_row(app, title, sub, when):
    return ('<div style="background: rgba(251,247,236,0.93); border-radius: 18px; padding: 12px 14px; margin-top: 10px;">'
            f'<div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE};">{app}</span>'
            f'<span style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.8px; color: {HINT}; margin-left: auto;">{when}</span></div>'
            f'<div style="font-size: 15px; line-height: 20px; font-weight: 600; color: {INK}; margin-top: 4px;">{title}</div>'
            f'<div style="font-size: 14px; line-height: 19px; color: #2C2622; margin-top: 2px;">{sub}</div></div>')
lock = ('<div style="width: 393px; min-height: 0; background: #221E1A; font-family: ' + SANS + '; display: flex; flex-direction: column; box-sizing: border-box;">'
        '<div style="padding: 30px 22px 0 22px; text-align: center;"><div style="font-family: ' + MONO + '; font-size: 11px; font-weight: 700; letter-spacing: 1.15px; color: rgba(251,247,236,0.62);">SUNDAY 6:02 PM</div>'
        '<div style="font-family: ' + SERIF + '; font-size: 46px; line-height: 52px; color: rgba(251,247,236,0.92); margin-top: 2px;">6:02</div></div>'
        '<div style="padding: 18px 16px 26px 16px;">'
        + os_row('VESPER', 'A result you asked for is ready', 'Open Vesper to read it', '6:02 PM')
        + os_row('VESPER', 'Maya sent you something', 'Her words are in Vesper', '4:48 PM')
        + os_row('VESPER', 'Saturday evening now has a place', 'Alex picked it', '2:31 PM')
        + '</div><div style="flex-grow: 1;"></div></div>')

fg = phone(anchor('4:48 PM'), read('The sesame loaf before eleven, then low water at 1:40.', 'Clear and cold, 54&deg; by noon &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           sect('In motion'), gut(f'<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">{reader(NOTE)}</div>'),
           gut('<div style="border: 1px dashed rgba(27,23,20,0.22); border-radius: 12px; padding: 10px 12px; margin-top: 12px;">'
               + fn('ARRIVED WHILE THIS PAGE WAS OPEN &middot; THE UNIT UPDATED IN PLACE', mt=0, color=MUTE)
               + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">No banner, no toast, no sound. The platform list has it; Vesper does not announce it twice.</div></div>', 12))

denied = phone(anchor('6:40 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
               SINCE,
               gut(f'<div style="border-top: 1px solid rgba(27,23,20,0.10); padding-top: 4px;">'
                   + row(glyph(HALL), 'The pump station is on the walk-in list', sub='No registration needed &middot; checked 4:12 PM')
                   + row(facepile(['A', 'M', 'N']), 'Alex picked the place &middot; Otto&rsquo;s, Saturday 7:30', sub='4 going &middot; nothing to answer')
                   + row(glyph('M3 4h9v7H7l-3 3V4z'), 'Maya sent you something', last=True, sub='Her words are in motion, below') + '</div>', 8),
               gut(fn('NOTIFICATIONS ARE OFF ON THIS DEVICE &middot; RESULTS ARRIVE HERE WHEN YOU OPEN', mt=0, color=MUTE)
                   + f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 4px;">You &amp; Trust owns the switch. Vesper does not ask again here, and opening this page does not spend the system prompt.</div>', 20))

row1 = ('<div style="display: flex; gap: 46px; align-items: flex-start;">'
        + cell('OUTSIDE THE APP &middot; SUNDAY 6:02 PM', '1 &middot; ENTRY &middot; WHAT THE PLATFORM SHOWS', 'Generic on the lock screen; the words are behind the destination',
               'Drawn only for copy and routing &middot; the OS presentation is the platform&rsquo;s', lock)
        + cell('ALREADY IN THE APP &middot; 4:48 PM', '2 &middot; ENTRY &middot; ARRIVES WHILE YOU ARE HERE', 'The unit updates in place; nothing flashes',
               'Passive foreground receipt &middot; no banner, no second toast', fg)
        + cell('NO PUSH PERMISSION &middot; 6:40 PM', '3 &middot; ENTRY &middot; NOTHING IS LOST WITHOUT PUSH', 'The same three results, waiting where they belong',
               'Push is never the only path &middot; one quiet line, no repeat prompt', denied)
        + notes([('THE PLATFORM CONTRACT, REUSED', 'All three arrive on the existing <span style="font-family: ' + MONO + '; font-size: 11.5px;">trip_updates_v2</span> channel; none of them needs <span style="font-family: ' + MONO + '; font-size: 11.5px;">needs_action_v2</span>, and <span style="font-family: ' + MONO + '; font-size: 11.5px;">time_critical_travel_v2</span> stays for travel that cannot wait. From the same contract, not re-specified here: private noncritical copy is generic on the lock screen and full copy waits behind the authenticated destination; permission is asked only after a primed value moment, never on mount, and opening this page does not spend it; passive foreground receipt updates without a banner; push and the activity ledger route one item to one destination; default tap is the only system action.'),
                ('HOME IS NOT AN INBOX', 'Each result is drawn where its subject already lives &mdash; the walk-in answer under what the city is doing, Alex&rsquo;s pick on the commitment, Maya&rsquo;s words in motion. The since-you-last-looked line is a reading aid that clears itself, not a queue with a count.'),
                ('ALREADY SEEN IS NOT RE-ANNOUNCED', 'A result read in the app is not prompted again from the ledger, and a delivery that already represents a conversation suppresses its generic unread row.')])
        + '</div>')

# ---- Row 2 · the private requested result -------------------------------------------------------
a1 = phone(anchor('6:40 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           SINCE, sect('The city this week'),
           unit('The pump station is on the walk-in list',
                'Walk-in sites need no registration; the timed sites open Tuesday at noon, which is still true.',
                'YOU ASKED ON FRIDAY &middot; CHECKED ONCE AT 4:12 PM &middot; NOT WATCHED',
                f'<div style="margin-top: 10px;">{gold("What came back")}</div>'),
           sect('In motion'), gut(f'<div style="padding: 6px 0 14px 0;">{reader(NOTE)}</div>'))
a2 = phone(
    f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">WHAT CAME BACK</span><span class="fn" style="margin-left: auto;">SUNDAY 6:41 PM</span></div></div>',
    gut(f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 22px; line-height: 27px; text-wrap: balance;">Is the pump station a walk-in site?</div>'
        f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">You asked on Friday evening. One check, finished.</div>', 20),
    gut('<div style="border-top: 1px solid rgba(27,23,20,0.10); margin-top: 16px; padding-top: 12px;">'
        + f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: {INK};">Yes. The pump station under the park is on the walk-in list; only the timed sites need registration, and that opens Tuesday at noon.</div>'
        + fn('THE OPEN HOUSE LISTING &middot; READ 4:12 PM SUNDAY &middot; FIXTURE SOURCE', mt=10) + '</div>'),
    gut('<div style="margin-top: 16px; border-top: 1px solid rgba(27,23,20,0.06); padding-top: 12px;">'
        + fn('FINITE WORK &middot; THIS CHECK IS FINISHED AND NOTHING IS BEING WATCHED', mt=0, color=MUTE)
        + f'<div style="display: flex; gap: 20px; align-items: center; margin-top: 2px;">{ink("Check it again")}{gold("Open the listing")}</div></div>'),
    gut(fn('OPENING THIS ASKED NOTHING, KEPT NOTHING AND BOOKED NOTHING', mt=0), 8))
a3 = phone(anchor('6:43 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           sect('The city this week'),
           unit('The pump station is on the walk-in list',
                'Walk-in sites need no registration; the timed sites open Tuesday at noon, which is still true.',
                'CHECKED ONCE AT 4:12 PM &middot; READ &middot; NOT WATCHED',
                f'<div style="margin-top: 10px;">{gold("What came back")}</div>'),
           sect('In motion'), gut(f'<div style="padding: 6px 0 14px 0;">{reader(NOTE)}</div>'),
           gut(fn('BACK AT THE SAME PLACE IN THE SCROLL &middot; THE SINCE-YOU-LOOKED LINE IS GONE FOR THIS ONE', mt=0), 16))
row2 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('A &middot; PRIVATE REQUESTED RESULT', '4 &middot; USEFUL VALUE, IN ITS PLACE', 'The answer reads on Home; the door is for the evidence',
               'Donor: 02&rsquo;s city unit and 12&rsquo;s &ldquo;checked once, not watched&rdquo;', a1)
        + cell('THE EXACT DESTINATION', '5 &middot; WHAT CAME BACK', 'The question, the answer, the source and the time',
               'Requested work belongs to Plans / Entity &middot; drawn here as its result', a2)
        + cell('RETURN', '6 &middot; THE SAME PLACE IN THE SCROLL', 'Read, and quiet again',
               'No queue emptied, nothing archived, no second prompt', a3)
        + notes([('ENTRY &rarr; RESULT &rarr; DESTINATION &rarr; RETURN', 'A generic push at 6:02 PM, or nothing at all; the answer already sits under the city section; its door opens the evidence; Back returns to the same scroll position with the item marked read.'),
                 ('FINITE WORK, NOT A WATCH', 'The request was one check. The result says when it was read and that nothing is being watched. &ldquo;Check it again&rdquo; is a new finite request, not a subscription; neither the current fact nor a pending state adopts one.'),
                 ('OPENING IS NOT AUTHORIZING', 'This destination shows information. Nothing was reserved, kept or sent by reading it, and it says so once at the foot.'),
                 ('DEPENDENCY', 'Plans and Entity own requested-work result, failure and return; their 90-recovery and 05 unavailable states are the donors for the failure side. Home draws only the arrival, the reading and the way back.')])
        + '</div>')

# ---- Row 3 · a friend's offering ----------------------------------------------------------------
b1 = phone(anchor('6:40 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           SINCE, sect('In motion'),
           gut(f'<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">{reader(NOTE)}</div>'),
           gut(fn('HER WORDS, NOT A PREVIEW CARD &middot; THE PLATFORM COPY SAID ONLY THAT SHE SENT SOMETHING', mt=0), 12))
b2 = phone(
    gut(reader('density="full" show="reader" author="Maya" audience="Aug 30 · to you" words="…and if you two ever want a proper pasta night — Lilia. Ask for the corner table." '
               'place="Lilia" placeDetail="Court Street · pasta, late" placeMeta="ARRANGED IN PLANS · TONIGHT AT EIGHT" ask="Ask about Lilia" hint-size="349px,460px"'), 20),
    gut(reader('density="full" show="ask" author="Maya" ask="Ask about Lilia" hint-size="349px,56px"'), 14),
    gut(fn('REPLY GOES TO MAYA &middot; ASK GOES TO VESPER, AND SHE SEES NOTHING OF IT', mt=0), 18))
row3 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('B &middot; A FRIEND&rsquo;S OFFERING', '7 &middot; USEFUL VALUE, IN ITS PLACE', 'What she actually wrote, where such things live',
               'The adopted reader on 02 &middot; unchanged by this canvas', b1)
        + cell('THE EXACT DESTINATION', '8 &middot; HER ORIGINAL, OPENED', 'Reply to her, or ask Vesper privately',
               'Shared reader 0.4.1 &middot; the Ask sits after the host&rsquo;s own sections', b2)
        + notes([('RETURN IS ALREADY DRAWN', 'Board 16&rsquo;s continuation carries open &rarr; Reply or private Ask &rarr; return to the same scroll with one compact receipt. It is not redrawn here; this row shows only the delivery half, so the three arrivals can be compared.'),
                 ('HUMAN REPLY IS NOT PRIVATE ASK', 'Reply is addressed to Maya and she sees it. Ask is addressed to Vesper about her note, and she sees nothing. Chat owns the composer and the keyboard contract either way; Home gains no second composer.'),
                 ('WHAT THE PLATFORM SAID', 'The lock screen said only that she sent something. Her words appear after the authenticated destination opens, which is the same rule that keeps a private result generic outside the app.')], 700)
        + '</div>')

# ---- Row 4 · the consequential change ------------------------------------------------------------
c1 = phone(anchor('6:40 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           SINCE, sect('In motion'),
           gut('<div style="border-top: 1px solid rgba(27,23,20,0.10); padding-top: 2px;">'
               + row(facepile(['A', 'M', 'N']), 'Alex&rsquo;s birthday &middot; Saturday evening', sub='Otto&rsquo;s, 7:30 &middot; Alex picked the place &middot; 4 going')
               + row(glyph('M7 3v6a2 2 0 0 0 4 0V3M9 11v6M14 3c-1.5 1.5-1.5 5 0 6.5V17', '0.7'), 'Tonight at Lilia &middot; eight', last=True, sub='With Maya &middot; arranged') + '</div>', 8),
           gut(fn('THE COMMITMENT CHANGED, SO THE COMMITMENT CHANGED &middot; NO NEW CARD, NO BADGE', mt=0), 14))
c2 = phone(
    f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE ARRANGEMENT &middot; IN PLANS</span><span class="fn" style="margin-left: auto;">SUNDAY 6:44 PM</span></div></div>',
    gut(f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 29px; text-wrap: balance;">Alex&rsquo;s birthday</div>'
        f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Saturday evening &middot; four going</div>', 18),
    gut('<div style="border-top: 1px solid rgba(27,23,20,0.10); margin-top: 16px;">'
        + f'<div style="display: flex; gap: 14px; padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span class="fn" style="width: 74px; flex: none; color: {MUTE};">WHERE</span><div style="flex: 1;"><div style="font-size: 15px; line-height: 20px;">Otto&rsquo;s, Court Street</div>{fn("ALEX PICKED IT AT 2:31 PM", mt=3)}</div></div>'
        + f'<div style="display: flex; gap: 14px; padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span class="fn" style="width: 74px; flex: none; color: {MUTE};">WHEN</span><div style="flex: 1;"><div style="font-size: 15px; line-height: 20px;">Saturday 7:30</div>{fn("WAS &ldquo;EVENING, TIME TO COME&rdquo;", mt=3)}</div></div>'
        + f'<div style="display: flex; gap: 14px; padding: 12px 0;"><span class="fn" style="width: 74px; flex: none; color: {MUTE};">WHO KNOWS</span><div style="flex: 1;"><div style="font-size: 15px; line-height: 20px;">Alex, Sam and you</div>{fn("MAYA HAS NOT SEEN THE PLACE YET", mt=3)}</div></div></div>'),
    gut('<div style="margin-top: 14px; border-top: 1px solid rgba(27,23,20,0.06); padding-top: 12px;">'
        + fn('READING THIS CHANGED NOTHING &middot; EACH OF THESE IS A SEPARATE ACT', mt=0, color=MUTE)
        + f'<div style="display: flex; flex-direction: column; gap: 2px; margin-top: 2px;">{ink("Tell Maya where it is")}{ink("Ask Alex to move it later")}</div></div>'),
    gut(fn('PLANS OWNS THIS PAGE AND ITS CONSEQUENCES &middot; DRAWN HERE AS THE DESTINATION HOME POINTS AT', mt=0), 10))
c3 = phone(anchor('6:46 PM'), read('Tonight at Lilia, eight. Two answers came back today.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           sect('In motion'),
           gut('<div style="border-top: 1px solid rgba(27,23,20,0.10); padding-top: 2px;">'
               + row(facepile(['A', 'M', 'N']), 'Alex&rsquo;s birthday &middot; Saturday evening', sub='Otto&rsquo;s, 7:30 &middot; 4 going')
               + row(glyph('M7 3v6a2 2 0 0 0 4 0V3M9 11v6M14 3c-1.5 1.5-1.5 5 0 6.5V17', '0.7'), 'Tonight at Lilia &middot; eight', last=True, sub='With Maya &middot; arranged') + '</div>', 8),
           gut('<div style="margin-top: 12px;"><dc-import name="Notice" tone="applied" title="Told Maya where it is &middot; 6:45" body="Nothing else here changed." hint-size="349px,64px"></dc-import></div>'),
           gut(fn('THE ROW READS AS THE CURRENT TRUTH &middot; THE CHANGE IS NO LONGER NEWS', mt=0), 16))
row4 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('C &middot; A CONSEQUENTIAL CHANGE', '9 &middot; USEFUL VALUE, IN ITS PLACE', 'The commitment carries its own change',
               'Donor: 02&rsquo;s In motion rows and 12&rsquo;s last-known lines', c1)
        + cell('THE EXACT DESTINATION', '10 &middot; THE ARRANGEMENT &middot; OPENING IS NOT AUTHORIZING', 'What changed, who knows, and what is still yours to do',
               'Plans owns the page &middot; the two acts are explicit and separate', c2)
        + cell('RETURN', '11 &middot; HOME, WITH THE CHANGE SETTLED', 'One compact receipt beside the row it belongs to',
               'Shared Notice, tone applied &middot; no banner, no page rewrite', c3)
        + notes([('INFORMATION AND CONSEQUENCE ARE DIFFERENT DOORS', 'Opening the arrangement showed the new place and time and told no one. Telling Maya is an act with a named audience and a receipt; asking Alex to move it is another. Neither happens by arriving, tapping the notification or reading the page.'),
                 ('NOT A DECISION QUEUE', 'Alex picking the place needs nothing from this person, so it arrives as information: no DECIDE chip, no action row, no reminder. The change lands on the commitment that already existed rather than becoming a new unit.'),
                 ('DEPENDENCY', 'Plans owns the arrangement page, its consequence controls and the audience of each act. Social owns whether Maya&rsquo;s copy of the evening updates. Home shows the current truth and the way in.')])
        + '</div>')

# ---- Row 5 · when the target or the session breaks -------------------------------------------------
d1 = phone(anchor('7:05 PM'), read('Tonight at Lilia, eight.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           sect('In motion'),
           gut(f'<div style="padding: 6px 0 14px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">{reader("density=\"open\" author=\"Maya\" meta=\"AUG 30 · TO YOU\" state=\"withdrawn\" hint-size=\"349px,150px\"")}</div>'),
           gut(fn('THE NOTIFICATION POINTED HERE &middot; WHAT SHE TOOK BACK IS GONE, THE REST OF THE PAGE IS NOT', mt=0), 12))
d2 = phone(anchor('7:08 PM'), read('Tonight at Lilia, eight.', 'Clear, 52&deg; &middot; Brooklyn tonight with Maya &middot; the show Friday.'),
           sect('In motion'),
           gut('<div style="margin-top: 4px;"><dc-import name="Notice" tone="unavailable" title="Saturday evening was cancelled" body="Alex cancelled it at 6:58. The place he picked and the thread are still in Plans." primary="Open it in Plans" hint-size="349px,120px"></dc-import></div>'),
           gut('<div style="border-top: 1px solid rgba(27,23,20,0.10); margin-top: 16px; padding-top: 2px;">'
               + row(glyph('M7 3v6a2 2 0 0 0 4 0V3M9 11v6M14 3c-1.5 1.5-1.5 5 0 6.5V17', '0.7'), 'Tonight at Lilia &middot; eight', last=True, sub='With Maya &middot; arranged') + '</div>', 8),
           unit('The pump station is on the walk-in list', 'Walk-in sites need no registration.', 'CHECKED ONCE AT 4:12 PM &middot; NOT WATCHED', top=22),
           gut(fn('ONE REGION SAYS WHAT HAPPENED &middot; TONIGHT, THE ANSWER AND THE REST OF THE PAGE STILL WORK', mt=0), 16))
d3 = phone(
    f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex: none;"><path d="M12.5 4L7 10L12.5 16" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    f'<span style="font-family: {MONO}; font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">WHAT CAME BACK</span><span class="fn" style="margin-left: auto;">SUNDAY 7:12 PM</span></div></div>',
    gut('<div style="margin-top: 18px;"><dc-import name="Notice" tone="pending" title="Sign in again to open this" body="Your session expired while you were away. The result is kept and nothing was opened for you." primary="Sign in" hint-size="349px,130px"></dc-import></div>'),
    gut(f'<div style="margin-top: 18px; border-top: 1px solid rgba(27,23,20,0.10); padding-top: 12px;"><div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">Is the pump station a walk-in site?</div>'
        f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">You asked on Friday evening. The answer is waiting behind the sign-in.</div>'
        + fn('SIGNING IN RETURNS TO THIS PAGE &middot; NOTHING IS SENT, KEPT OR CHANGED WHILE SIGNED OUT', mt=10) + '</div>'))
row5 = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
        + cell('STALE OR DELETED TARGET &middot; HUMAN', '12 &middot; SHE TOOK IT BACK', 'The original is gone; what you wrote stays with you',
               'Shared reader, state withdrawn &middot; Social 04.9 is the donor', d1)
        + cell('STALE OR DELETED TARGET &middot; ARRANGEMENT', '13 &middot; THE DESTINATION IS NO LONGER THERE', 'What happened, what remains, and where it lives now',
               'Shared Notice, tone unavailable &middot; Plans 90 and Entity 05 donors', d2)
        + cell('AUTHENTICATION INTERRUPTION', '14 &middot; SIGN IN AGAIN, LOSE NOTHING', 'The result is kept; the return position is the same page',
               'Shared Notice, tone pending &middot; no consequence while signed out', d3)
        + notes([('A REGION, NOT THE PAGE', 'A dead target, an unavailable source or a stale feed degrades its own region and says so in place. The rest of Home keeps working: tonight is still tonight, the answer is still readable. A whole-page failure is for a whole-page cause, and 12&rsquo;s three states remain the donors for the region-local treatment.'),
                 ('THE POINTER OUTLIVES THE TARGET', 'A notification can arrive for something that is later withdrawn or cancelled. The in-app landing says what happened rather than showing an empty page or a generic error, and it never re-announces the item afterwards.'),
                 ('NO CONSEQUENCE WHILE SIGNED OUT', 'An expired session can interrupt reading. It must not authorize, send or keep anything on the way back, and it returns to the page that was asked for, not to the root.'),
                 ('UNRESOLVED', 'Native owners: keyboard, focus order, screen-reader order, back stack and exact return position; the OS permission flow and per-channel controls in You &amp; Trust; whether Plans keeps a cancelled arrangement readable and for how long. Static frames cannot settle any of these.')])
        + '</div>')

# ---- Board -----------------------------------------------------------------------------------------
def table(heads, rows, minw=1700):
    th = ''.join(f'<th style="text-align: left; font-family: {MONO}; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; padding: 0 10px 6px 0; border-bottom: 1px solid rgba(27,23,20,0.12);">{h}</th>' for h in heads)
    out = f'<div style="overflow-x: auto; margin-top: 10px;"><table style="border-collapse: collapse; min-width: {minw}px;"><tr>{th}</tr>'
    for r in rows:
        out += '<tr>' + ''.join(f'<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">{c}</td>' for c in r) + '</tr>'
    return out + '</table></div>'

donors = table(['Frame', 'Existing donor', 'New here'], [
    ['1 &middot; lock screen', 'The notifications and alerts contract: generic private copy, one destination, default tap only', 'The three arrivals written to its copy budgets'],
    ['2 &middot; arrives while open', '12&rsquo;s aperture frames and the passive-receipt rule', 'The in-place update with no banner'],
    ['3 &middot; push denied', '11&rsquo;s since-you-last-looked return', 'The quiet off-switch line, owned by You &amp; Trust'],
    ['4&ndash;6 &middot; requested result', '02&rsquo;s city section; 12&rsquo;s &ldquo;checked once &middot; not watched&rdquo;', 'The result page: question, answer, source, finite-work line'],
    ['7&ndash;8 &middot; a friend&rsquo;s offering', '02&rsquo;s adopted reader; 16&rsquo;s continuation for the return', 'Only the delivery half; the return is not redrawn'],
    ['9&ndash;11 &middot; consequential change', '02&rsquo;s In motion rows; Plans&rsquo; arrangement', 'The change on the commitment; the two explicit acts'],
    ['12 &middot; withdrawn original', 'Shared reader state=withdrawn (Social 04.9)', 'It standing as the landing of a notification'],
    ['13 &middot; cancelled arrangement', 'Shared Notice unavailable; Plans 90, Entity 05', 'Region-local landing with what remains'],
    ['14 &middot; sign in again', 'Shared Notice pending', 'The kept result and the unchanged return position']])

status = table(['Claim', 'State'], [
    ['Entry, result, destination, return and the three interrupted cases', 'Drawn on this canvas'],
    ['The selected ordinary Home, its units and local steering', 'Selected earlier; unchanged by this canvas'],
    ['Notification categories, permission timing, lock-screen copy, dedupe', 'Implemented contract, reused &mdash; not re-specified here'],
    ['Keyboard, focus, screen-reader order, back stack, exact return position', 'Not verified; native owners'],
    ['Whether a cancelled arrangement stays readable, and for how long', 'Unresolved; Plans'],
    ['Per-channel controls and the permission moment in settings', 'Unresolved; You &amp; Trust'],
    ['Requested-work failure and retry beyond this result', 'Unresolved; Plans / Entity']], 1200)

CSS = ('.fn { font-family: ' + MONO + '; font-size: 10px; letter-spacing: 0.9px; color: #B5AFA5; }\n'
       '    .kick { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #8A6628; }\n'
       '    .kickm { font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead { display: flex; align-items: center; gap: 10px; font-family: ' + MONO + '; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; }\n'
       '    .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }\n'
       '    .row { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid rgba(27,23,20,0.06); }\n'
       '    .row:first-child { border-top: none; }\n    .chev { flex: none; }')

header = ('<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;">'
          '<div class="kick">VESPER &middot; HOME &middot; 17 &middot; DELIVERY AND RETURN &middot; COVERAGE ASSIGNMENT 2026-09-12</div>'
          f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">17 &middot; What arrives while you are away, and how you get back</div>'
          f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">Three arrivals on one Sunday: a private result you asked for, something Maya sent, and Alex picking Saturday&rsquo;s place. '
          'Each is drawn from entry through the useful value on Home, the exact destination that owns it, and the return to the same place in the scroll &mdash; then the three ways it can break. '
          'Existing donors and the shared components only; no new feed, inbox or notification centre, and the platform surface keeps its own contract.</div></div>')

board = ('<div style="width: 2000px; min-height: 4944px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; font-family: ' + SANS + '; color: #1B1714; display: flex; flex-direction: column;">'
         + header + row1 + row2 + row3 + row4 + row5
         + '<div style="margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);"><div class="kickm">DONOR FRAMES AND WHAT IS NEW</div>' + donors + '</div>'
         + '<div style="margin-top: 34px;"><div class="kickm">DRAWN &middot; SELECTED &middot; IMPLEMENTED &middot; VERIFIED</div>' + status + '</div>'
         + '<div class="fn" style="margin-top: 30px; line-height: 16px;">EVERY WORLD FACT, PERSON AND RESULT IS A DESIGN FIXTURE &middot; THE LOCK SCREEN IS DRAWN FOR COPY AND ROUTING ONLY &middot; A STATIC MOCKUP PROVES NO DELIVERY, PERMISSION OR RETURN BEHAVIOUR</div></div>')

html = ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;700&display=swap">\n'
        f'  <link rel="stylesheet" href="{G.KERNEL}">\n  <link rel="stylesheet" href="vdl.css">\n  <style>\n    body {{ margin: 0; }}\n    a {{ color: #8A6628; }}\n    {CSS}\n  </style>\n</helmet>\n'
        + board + '\n</x-dc>\n</body>\n</html>\n')
open(f'{OUT}/17 - Delivery and Return.dc.html', 'w').write(html)
print('wrote 17 - Delivery and Return', len(html), 'readers', html.count('name="OriginalReader"'), 'notices', html.count('name="Notice"'), 'doors', html.count('vdl-door'))

# index row on 00
h = G.rd('00')
TD = '<td style="font-size: 12.5px; line-height: 17px; color: #2C2622; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">'
r17 = ('<tr>' + TD + '17 - Delivery and Return</td>' + TD + 'Coverage assignment (09-12): what arrives while you are away &mdash; a private requested result, a friend&rsquo;s offering and a consequential change &mdash; each from entry through the useful value on Home, the exact destination and the return to the same scroll position, plus the withdrawn original, the cancelled destination and the expired session. Reuses the notifications and alerts contract; adds no feed or inbox</td>'
       + TD + 'Coverage &middot; 09-12 &middot; donors reused</td></tr>')
i = h.find('16 - Shared Language Adoption</td>'); j = h.find('</tr>', i) + 5
open(f'{OUT}/00 - Index.dc.html', 'w').write(h[:j] + r17 + h[j:]); print('wrote 00 - Index with the 17 row')
