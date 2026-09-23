"""Vesper — Home · revision 4: the 'fix all' pass.
(1) the two P0 corrections from the connected-experience plan (no hollow circles on alternatives;
    H5's cooking headline is advice, not a known cause);
(2) H1 run through the August 29 marginal-deletion test, pruned, and drawn beside its Quiet FLOOR —
    only what real owners supply today;
(3) one wedge board (H6): a group trip forming — organizer, joiner, and live change;
(4) H0 records the canon events of 2026-09-05."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
import gen_generous3 as g3
from gen_generous3 import (sect, meta, title, sup, gut, u2, card, author_row, share_card, handoff_card, arr_card, fact,
                           reading_card, ticket_stub, sample_card, kept_row, rows_A, COLD, COLD_CITY, CITY_SUN, caption, col,
                           board_page, head, FOOT, N, v2, WEEK_SUN, WEEK_MON, ending, facepile, arow, compare2, collapsed, span, photo, callouts)
from gen_generous import ending as _ending

OUT = g3.OUT
V3 = os.path.join(os.path.dirname(__file__), 'v3phones')
def v3(name): return open(os.path.join(V3, name + '.html')).read()

# ───────────────────────────── P0 corrections ─────────────────────────────
def ways_card(t, items, meta_t=''):
    """A prepared window with alternatives (horizon_prepared_alternatives): unnumbered, no marks that read as controls; an 'or' hairline separates options."""
    inner = title(t, 20, 25, 600)
    OR = f'<div style="display: flex; align-items: center; gap: 10px; margin: 8px 0 4px 0;"><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span><span class="fn" style="color: {ANCHOR};">OR</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span></div>'
    for i, (a, b, when) in enumerate(items):
        if i: inner += OR
        inner += f'<div style="padding: {6 if i else 12}px 0 4px 0;">{title(a, 16, 21)}{sup(b)}<div class="fn" style="color: {ANCHOR}; margin-top: 3px;">{when}</div></div>'
    if meta_t: inner += meta(meta_t, 10)
    return card(inner)
g3.ways_card = ways_card  # H5/H1 in g3 pick this up

def h5v4():
    # rebuild H5's phone from g3 with the corrected headline
    html = g3.h5v2()
    html = html.replace('The texture you photographed came from the last minute at the stove',
                        'To get the texture you photographed, finish the pasta in the sauce')
    html = html.replace('A thin film that holds the ridges, finished in the pan &mdash; a starch-supported emulsion. What that kitchen actually did is not known; this is what the plate shows.',
                        'Sauce meets pasta ninety seconds early with a ladle of starchy water; the film that holds the ridges is a starch emulsion. That is consistent with your photograph. What that kitchen actually did is not known.')
    return html

# ───────────────────────────── H1 · deletion test → pruned ─────────────────────────────
def h1v4():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 160, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT',
                            'SUNSET PARK &middot; 14 MIN BY BIKE &middot; OPEN NOW', 'The bakery'), top=22)
    inner += gut(ways_card('Today', [
        ('The loaf, then the water', 'Bakery by 10:30; low water on the pier nine minutes on.', 'MORNING &middot; 10:30 &rarr; 1:40'),
        ('The flood line, walked at low water', 'The granite kerbs show where the gates&rsquo; protection ends.', 'AFTERNOON &middot; 1:40&ndash;4'),
        ('Stay in. The skillet, preheated dry', 'Four minutes dry, then oil, then dough &mdash; Thursday&rsquo;s soggy crust was the pan, not the dough.', 'TONIGHT'),
    ]), top=16)
    inner += rows_A()
    inner += sect('Worth knowing') + gut(COLD())
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>')
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def h1_floor():
    """The Quiet FLOOR: what the real owners supply today, per the 2026-09-01 implementation status. Nothing invented to fill a slot."""
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    # direct-state read (17px): there is nothing to interpret; one true condition only if the Moment read supplies it
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Sunday. Alex&rsquo;s birthday and Dana on Saturday; the show Friday.</div>'
              f'<div class="fn" style="margin-top: 6px; color: {ANCHOR};">DIRECT STATE &middot; NO WORLD READ PRODUCER YET &middot; A CONDITION LINE APPEARS ONLY IF THE MOMENT READ SUPPLIES ONE</div></div>')
    inner += rows_A()
    inner += sect('Horizons') + gut('<div>' + row('The Sunset Park bakery &middot; <span style="color: #6E6862;">saved &middot; not yet visited</span>', mark='hollow')
                                    + row('The greenmarket &middot; <span style="color: #6E6862;">Theo sent this &middot; Saturdays 8&ndash;1</span>', avatar='T', last=True) + '</div>')
    inner += gut(door('Everything in Life') + meta('LIFE &middot; THE TICKET, THE NOTE, THE SAVED PLACE', 0), top=32)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

DELETION = [
    ('Maya&rsquo;s share', 'The only thing on the page true today only; her photograph and words', '<b>Keep</b>'),
    ('Today (three ways)', 'The alternative when the lead does not interest me; the window&rsquo;s shape', '<b>Keep</b> &mdash; the skillet technique folds into its third option'),
    ('In motion', 'Alex&rsquo;s arrangement, Dana, the show, the dentist', '<b>Keep</b>'),
    ('The cold split', 'The one mechanism tied to a change this week', '<b>Keep</b> (numbers marked fixture; H0 names the data they need)'),
    ('The skillet as its own unit', 'Nothing: the Today card already carries the technique in one clause. Two units on one subject', '<b>Cut</b> &mdash; repetition penalty (same subject, same source)'),
    ('Open House fact', 'A Tuesday-noon deadline inside the person&rsquo;s window', '<b>Keep</b>'),
    ('The flea fact', 'Nothing that changes this week; &ldquo;neither depends on the other&rdquo; admitted it', '<b>Cut</b> &mdash; no why-now'),
    ('The reading preview', 'Optional depth; the same source the brief said to stop leaning on. Available in Life and the reader', '<b>Cut</b> &mdash; loses to the smaller composition'),
]

H1_NOTES = notecol('The deletion test, and the floor', [
    ('THE TEST', N('The August 29 ruling: the smaller composition wins when it preserves the strongest value and range. Each unit was removed in turn and the loss named. Eight units in, five out.')),
    ('RESULTS', ledger([(k, f'{v} &middot; {r}') for k, v, r in DELETION])),
    ('THE FLOOR', N('The right phone is what the real owners can serve <b>today</b> (implementation status, 2026-09-01): Experience Graph commitments and occasions, saved Places, addressed handoffs, action receipts, the Life door. No world-read producer, no share projection beyond addressed Place handoffs, no mechanism library, no city source. The read drops to direct state. Nothing is invented to fill a slot. This is the page the first internal account will open, and the Quiet floor ruling says it is the modal state.')),
    ('WHAT THE GAP SAYS', N('The distance between the middle and right phones is the content-production and owner-read backlog, not a design defect. The design must be judged at the floor as well as the ceiling.')),
    ('P0 CORRECTION APPLIED', N('The hollow circles on the alternatives are gone; the options are separated by &ldquo;or&rdquo; hairlines and their own windows only.')),
], w=440)

def H1():
    cols = [col(v3('h1v3'), caption('BEFORE &middot; REVISION 3', 'Generous, eight units', 'THE INPUT TO THE DELETION TEST')),
            col(h1v4(), caption('AFTER &middot; REVISION 4', 'Pruned to five', 'MAYA &middot; TODAY &middot; ROWS &middot; THE COLD &middot; ONE CITY FACT')),
            col(h1_floor(), caption('THE FLOOR &middot; REAL OWNERS TODAY', 'What the first account will see', 'DIRECT STATE &middot; ROWS &middot; TWO HORIZONS &middot; THE LIFE DOOR')),
            H1_NOTES]
    return board_page(1880, 2655, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 4 &middot; H1 &middot; ORDINARY SUNDAY &middot; PROPOSAL', 'H1 &middot; The generous Sunday, pruned, beside its floor',
                      'Revision 3 run through the August 29 marginal-deletion test: three units lose. The third phone is the honest floor &mdash; only what real owners supply today &mdash; so the page can be judged where the first internal account will actually open it.', cols, FOOT)

# ───────────────────────────── H6 · the wedge: a group trip forming ─────────────────────────────
def trip_card(status, t, text, instrument='', people='', meta_t='', door_text=None, status_col=PLAN):
    return arr_card(status, t, text, instrument, people, meta_t, door_text, status_col)

def days_strip(days):
    """A compact trip-days strip: (label, mark html, sub)"""
    cells = ''.join(f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 8px 0 6px;"><span class="dayl" style="color: {ANCHOR};">{d}</span>{m}<span style="font-size: 10px; color: {c};">{s or "."}</span></div>' for d, m, s, c in days)
    return f'<div style="margin-top: 10px; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 0 4px;"><div style="display: flex;">{cells}</div></div>'

def h6_organizer():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '8:40 PM')
    inner += orientation('Lisbon is nine weeks out. Four of six have joined.', 'Flights held for four &middot; two stays still open &middot; nothing due tonight.')
    inner += gut(trip_card('LISBON &middot; JUNE 12&ndash;17 &middot; FORMING', 'Four of six have joined. The stay in Alfama is the one open decision, and it closes Friday.',
                           'Dana and Theo have not answered; the plan does not wait on them. Maya asked for a kitchen; Alex asked to keep one day free.',
                           days_strip([('FRI', dm('solid', GOLD), 'arrive', INK), ('SAT', dm('hollow', ''), 'open', MUTE), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free day', MUTE), ('WED', dm('solid', GOLD), 'home', INK)]),
                           people=facepile(['you', 'M', 'A', 'J'], 24, -7) + f'<span style="font-size: 13px; color: {MUTE};">+ Dana, Theo &middot; invited</span>',
                           meta_t='FLIGHTS HELD &middot; 2 STAYS OPEN &middot; STAY DECISION BY FRI &middot; YOU OWN THE ARRANGEMENT', door_text='The trip'), top=22)
    inner += sect('In motion') + gut(row('Alfama stay &middot; <span style="color: #6E6862;">two options, sleeps six &middot; decide by Friday</span>', mark='dashed')
                                     + arow('Maya &middot; <span style="color: #6E6862;">&ldquo;somewhere with a kitchen, please&rdquo; &middot; in the arrangement</span>', avatars=['M'])
                                     + row('The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">unchanged</span>', mark='solid', color=GOLD, last=True))
    inner += sect('Worth knowing') + gut(u2('Two stays sleep six; only one has the kitchen Maya asked for and a day-free walk to the water Alex wanted',
        'The other is nearer the tram and cheaper by a night. Neither needs a card tonight.',
        compare2('STAY A &middot; ALFAMA', 'kitchen', 'six beds &middot; 12 min to water', 'STAY B &middot; BAIXA', 'tram', 'six beds &middot; a night cheaper'), meta_t='FROM THE TWO HELD OPTIONS + TWO CONTRIBUTIONS &middot; FIXTURE'))
    inner += gut(door('Everything shared with you') + meta('LIFE &middot; PEOPLE &middot; BY PERSON', 0), top=32)
    inner += ending([('TUE', dm('solid', INK), 'today', INK), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('dashed', OX), 'stay?', OX), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE)],
                    'Friday the show, and the stay. Lisbon in nine weeks.')
    return phone(inner, 0)

def h6_joiner():
    """Theo's first Home after tapping the invite: host intent, one permissioned foothold, one optional contribution, a way to decline. No profile, no group work."""
    inner = anchor_row('NEW YORK &middot; TUESDAY', '9:05 PM')
    inner += orientation_direct('Nadia invited you to Lisbon, June 12 to 17.', 'You chose New York. Nothing else about you is held.')
    inner += gut(trip_card('LISBON &middot; JUNE 12&ndash;17 &middot; YOU ARE INVITED', 'Six people, five nights. Nadia&rsquo;s words: &ldquo;a slow week near the water, one day in Sintra, and one day nobody plans.&rdquo;',
                           'Four have joined. Flights are held for the first four; a seat is held for you until Friday.',
                           days_strip([('FRI', dm('solid', GOLD), 'arrive', INK), ('SAT', dm('hollow', ''), 'open', MUTE), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free day', MUTE), ('WED', dm('solid', GOLD), 'home', INK)]),
                           people=facepile(['N', 'M', 'A', 'J'], 24, -7) + f'<span style="font-size: 13px; color: {MUTE};">joined &middot; Nadia hosts</span>',
                           meta_t='HER INTENT, IN HER WORDS &middot; YOUR SEAT HELD TO FRIDAY &middot; NOTHING IS SHARED ABOUT YOU', door_text='The trip'), top=22)
    inner += gut(f'<div style="display: flex; flex-direction: column; gap: 4px;">' + title('Three ways to answer, none owed tonight', 17, 22)
                 + '<div>' + row('I&rsquo;m in &middot; <span style="color: #6E6862;">joins; asks nothing else</span>', mark='solid', color=INK)
                 + row('I&rsquo;m in, and I can bring one thing &middot; <span style="color: #6E6862;">a place, a date limit, a note &mdash; optional</span>', mark='hollow')
                 + row('Not this one &middot; <span style="color: #6E6862;">declines quietly; nobody sees a refusal</span>', mark='hollow', last=True) + '</div></div>', top=30)
    inner += sect('What one thing turns into') + gut(sample_card('A MADE-UP TICKET, READ THE WAY YOURS WOULD BE', ticket_stub('The Hall', 'FRI &middot; SAMPLE', '8:00'), 'Doors at 8. Arrive by 8:40 and you miss nothing.',
                       span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=349),
                       ['Coat check yes &middot; set times posted by the hall the day before', 'After ten, the way home from the hall is a surface route: 25 minutes longer'],
                       [('How it&rsquo;s read', GOLDD), ('Try with yours', INK)]))
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Lisbon holds a seat for you until Friday. That is the only date on this page.</div></div>'
    return phone(inner, 0)

def h6_live():
    """Day 3 in Lisbon: the tram line to Sintra is out; the shared day reshapes. Recovery dominant; the field folds; nobody's private constraint is exposed."""
    inner = anchor_row('LISBON &middot; SUNDAY', '8:20 AM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">The Sintra train is out until noon. The day still works, later.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Six of you &middot; the palace tickets are for 2 PM &middot; the 11:40 train is running.</div></div>')
    inner += crown(OX, 'CHANGED &middot; SINTRA &middot; DECIDE BY 10:00', 'Leave at 11:10 for the 11:40; you reach the palace by 1:30', 'The morning opens up. Two of six asked to keep it slow; the group does not need to know who.',
                   span('TRAIN 11:40 &middot; PALACE 1:30', 118, 222, 'TICKETS 2 PM', 'THE ORIGINAL &middot; 9:10 TRAIN', 40, 118, 'OUT', start='8 AM', end='3', w=317)
                   + f'<div style="font-size: 14px; line-height: 19px; margin-top: 8px; color: {INK};">The morning in Alfama instead: the market is open until one and it is a ten-minute walk from the stay.</div>',
                   cta='Tell everyone the 11:40', fn='SERVICE READ 8:14 &middot; YOU HOST &middot; ONE MESSAGE, NOT SIX &middot; TICKETS UNCHANGED')
    inner += sect('In motion') + gut(arow('Six of you &middot; <span style="color: #6E6862;">all up &middot; two asked for a slow morning</span>', avatars=['you', 'M', 'A', 'J', 'D', 'T'])
                                     + row('Dinner &middot; Alfama, 8:30 &middot; <span style="color: #6E6862;">unchanged &middot; booked by Maya</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST OF SUNDAY &middot; STILL HERE', ['The palace, read before you go', 'The way back: last train 7:20', 'What Alfama&rsquo;s market sells on Sundays']), top=36)
    inner += ending([('FRI', dm('solid', GOLD), 'arrived', MUTE), ('SAT', dm('solid', INK), '', MUTE), ('SUN', dm('solid', OX), 'today', OX), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Sintra at 1:30. Dinner at 8:30. The morning is yours.')
    return phone(inner, 0)

H6_NOTES = notecol('The wedge, on Home', [
    ('WHY THIS BOARD', N('The thesis still names group travel as the launch wedge and &ldquo;keeping a shared experience coherent as reality changes&rdquo; as the product wedge. No Home board showed either. This one shows the arc: an organizer&rsquo;s Home while a trip forms, a joiner&rsquo;s first Home after an invite, and the live day under change.')),
    ('ORGANIZER', ledger([('LEAD', 'The trip as a shared-arrangement card: who has joined, what is open, when it closes. One decision on the page (the stay), and it is the organizer&rsquo;s.'), ('PEOPLE', 'Maya&rsquo;s and Alex&rsquo;s contributions appear as contributions, inside the arrangement and the comparison; no poll, no profile.'), ('DEMAND', 'One, with a Friday deadline. Everything else completes on view.')])),
    ('JOINER', ledger([('INVITATION IS NOT INCORPORATION', 'Host intent in her words; one permissioned foothold (the held seat); three ways to answer, including a quiet decline; nothing shared about the joiner.'), ('VALUE BEFORE GROUP WORK', 'The same sample as H3 sits beneath: the product is useful before the joiner does anything for the group.'), ('NOT SHOWN', 'A preference sheet, a group chat, a role, a compatibility read.')])),
    ('LIVE CHANGE', ledger([('PRIORITY', 'Recovery dominant, oxblood read, one instrument (the original span struck through, the new one gold), one ask that goes to the group as one message.'), ('PRIVATE STAYS PRIVATE', '&ldquo;Two of six asked to keep it slow; the group does not need to know who&rdquo; &mdash; the unattributed-aggregate law (kernel §11.12.8).'), ('THE REST', 'Folded to three reachable titles; dinner unchanged as a row.')])),
    ('PRODUCTION', N('Everything here is structured state (Trip/Plan, Commitments, invitations, contributions) plus one service read and one two-option comparison composed from held options. No bespoke prose. The Trip owner is the mature substrate the thesis says remains canonical inside a Trip.')),
    ('FIXTURE', N('Lisbon, the stays, the tram outage, the palace tickets, and every person are design fixtures. No real Lisbon fact is claimed.')),
], w=430)

def H6():
    cols = [col(h6_organizer(), caption('1 &middot; ORGANIZER &middot; NINE WEEKS OUT', 'A trip forming', 'PLANNING &middot; ONE DECISION, FRIDAY &middot; CONTRIBUTIONS INSIDE THE ARRANGEMENT')),
            col(h6_joiner(), caption('2 &middot; JOINER &middot; FIRST HOME AFTER THE INVITE', 'Invitation is not incorporation', 'COLD &middot; HOST INTENT, A HELD SEAT, THREE ANSWERS, A SAMPLE')),
            col(h6_live(), caption('3 &middot; DAY THREE &middot; THE TRAIN IS OUT', 'The shared day reshapes', 'URGENT &middot; RECOVERY DOMINANT &middot; ONE MESSAGE TO SIX &middot; PRIVATE STAYS PRIVATE')),
            H6_NOTES]
    return board_page(1880, 1775, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 4 &middot; H6 &middot; THE WEDGE &middot; PROPOSAL', 'H6 &middot; Group travel on Home: forming, invited, and under change',
                      'The one state family the Home boards never showed. The same skeleton, budgets, and type roles as H1&ndash;H5, applied to the launch wedge: an organizer with one decision, a joiner who owes nothing tonight, and a live day that reshapes without exposing anyone.', cols, FOOT)

# ───────────────────────────── H0 additions ─────────────────────────────
def H0(diag):
    html = g3.H0(diag)
    canon = ('<div style="display: flex; flex-direction: column; gap: 10px;"><div class="shead"><span>CANON EVENTS &middot; 2026-09-05 &middot; RULED</span><span class="rule"></span></div>'
             + N('<b>docs/decisions/2026-09-05-amend-home-composition-canon.md</b> (local commits d078608, 03837fc in the workspace repo; 1ce1818b8 in travel-app). '
                 '<b>1 Containment</b> &mdash; kernel §5.1 now reads &ldquo;a card marks a coherent object or experience&rdquo;; findings, techniques, and facts stay bare; the crown keeps its meaning. '
                 '<b>2 People region</b> &mdash; R1&rsquo;s &ldquo;only when the gathering is the dominant subject&rdquo; is replaced by the conditional rule; the one-relational-opening law is a dominance + demand rule. <b>D-H2 and D-H3 are ruled.</b> '
                 '<b>3 Type roles</b> &mdash; kernel §12.7 (c) superseded by the four roles. <b>D-H10 ruled.</b> '
                 '<b>4 Four kinds admitted</b> &mdash; horizon_prepared_alternatives, horizon_world_fact_row, people_authored_region, now_sample_demonstration; the Home union is 35. The build manifest and the Home root contract cite the decision. '
                 '<b>Still open:</b> D-H4 (a present-tense aperture, social-aperture lane) and D-H11 (production classes, engineering review).')
             + N('<b>Revision 4 boards:</b> H1 pruned by the August 29 deletion test (eight units &rarr; five) and drawn beside its floor; H5&rsquo;s cooking headline made advice, not cause; alternatives lose their hollow marks; H6 added for the wedge. Diagnostics: ' + diag.get('h1v4', '&mdash;') + ' (H1 rev 4) &middot; ' + diag.get('h1floor', '&mdash;') + ' (H1 floor).')
             + '</div>')
    html = html.replace("<div style=\"display: flex; flex-direction: column; gap: 34px;\">", "<div style=\"display: flex; flex-direction: column; gap: 34px;\">" + canon, 1)
    html = html.replace('REVISION 3 &middot; H0 &middot; DISPOSITIONS, PRODUCTION, DECISIONS, HANDBACK', 'REVISION 4 &middot; H0 &middot; CANON EVENTS, DISPOSITIONS, PRODUCTION, HANDBACK')
    html = html.replace("['D-H1', '<s>A crown renders only", "['D-H1', '<s>A crown renders only")  # unchanged
    html = html.replace('<b>Founder ruling requested</b>', '<b>Ruled 2026-09-05</b> (canon amendment §2)')
    html = html.replace("'<b>Proposed amendment</b> to the design kernel'", "'<b>Ruled 2026-09-05</b> (canon amendment §3)'")
    html = html.replace('Proposed; reported', 'Ruled 2026-09-05 (canon amendment §2)')
    html = html.replace('min-height: 3665px', 'min-height: 3860px')
    return html

PHONES_FOR_DIAG = {'h1v4': h1v4, 'h1floor': h1_floor}

if __name__ == '__main__':
    import json
    diag = json.load(open(os.path.join(OUT, 'diag.json'))) if os.path.exists(os.path.join(OUT, 'diag.json')) else {}
    for name, fn in [('H1 - Ordinary Sunday Generous', H1), ('H6 - Wedge Trip Forming', H6)]:
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
    # H5 with the corrected headline and the corrected alternatives; H2 unchanged in content
    cols = [col(v2('h5v2'), caption('BEFORE &middot; REVISION 2', 'New York first, composed', 'THE WORKING BASELINE')),
            col(h5v4(), caption('AFTER &middot; REVISION 4', 'Advice, not a known cause', 'A &middot; NO MARKS ON ALTERNATIVES &middot; D &middot; &ldquo;TO GET THE TEXTURE&hellip;, FINISH THE PASTA IN THE SAUCE&rdquo;')),
            g3.H5_NOTES.replace('Dispositions A and D, on H5', 'Dispositions A and D, on H5 &middot; P0 corrections applied')]
    open(os.path.join(OUT, 'H5 - Return Home Corrected.dc.html'), 'w').write(board_page(1440, 2180, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 4 &middot; H5 &middot; RETURN HOME &middot; PROPOSAL', 'H5 &middot; Coming home, with the two P0 corrections',
        'The connected-experience plan named two remaining corrections: no marks on alternatives that read as controls, and a cooking headline that gives advice without asserting what a kitchen did. Both applied.', cols, FOOT)); print('wrote H5')
    open(os.path.join(OUT, 'H0 - Ledger and Decisions.dc.html'), 'w').write(H0(diag)); print('wrote H0')
    os.makedirs(os.path.join(OUT, 'diag'), exist_ok=True)
    for k, fn in PHONES_FOR_DIAG.items():
        open(os.path.join(OUT, 'diag', k + '.html'), 'w').write(HEAD + fn() + TAIL)
