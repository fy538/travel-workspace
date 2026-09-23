"""11 - Return and Continuity: the nine union kinds that had no current drawing, redrawn in the four type roles
and placed on the page they belong to — Home opened after ten days away — beside the next morning, when the
delta has been consumed. 12 - Why This, Chat, and Degraded States: the inspect affordance and its sheet, the one
Chat aperture per page, and three states a first build meets first (stale, provider unknown, import pending).
Fixture copy only. Nothing here is ruled."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
import gen_merge as gm
import gen_seam as gs
import gen_artifact as ga
from gen_generous import caption, col, head, FOOT, N, WEEK_SUN, ending, arow, facepile, collapsed, span, photo, callouts
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, COLD, author_row, reading_card
from gen_generous4 import ways_card
from gen_merge import page, daycap, tbl, hh, STAMP, cell, spec
from gen_seam import mark, chip, row_mark, kept_chip_row, pass_flight, barcode, perforation
from gen_artifact import ways_seq_card, handoff_artifact, method, recon_strip, PASS, large

OUT = gm.OUT
HAIR = 'rgba(27,23,20,0.10)'

# ───────────────────────────── the nine kinds, redrawn ─────────────────────────────
def merged_read():
    return anchor_row('NEW YORK &middot; THURSDAY', '7:40 PM') + orientation('Ten days home. The trip has settled.', 'Nothing needs you tonight &middot; Saturday is dinner with Maya and Alex.')

def prepared_crown():
    return crown(PLAN, 'SATURDAY &middot; 2:00&ndash;8:00 PM', 'Saturday has room for the waterfront', 'A prepared half-day, back by land before dinner.',
                 span('THE PIER &middot; LOW WATER 2:40&ndash;5', 90, 210, 'BACK BY 7:30', start='2 PM', end='8', w=317), cta='Open the Saturday shape', fn='TIDE TABLE + YOUR SAVED PLACES + THE DINNER &middot; NOTHING BOOKED')

def since_rows():
    return (sect('Since you last looked') + gut(row_mark('flight', 'Return flight refund &middot; <span style="color: #6E6862;">paid Tuesday &middot; the claim is closed</span>')
            + row('Your Rome photos finished importing &middot; <span style="color: #6E6862;">690 of 690 &middot; nothing was shared</span>', mark='solid', color=GOLD)
            + arow('Dana &middot; Sunday happened &middot; <span style="color: #6E6862;">the bookshop, then the market</span>', avatars=['D'], last=True) + meta('THREE CHANGES &middot; READ ONCE, THEN THEY ARE ORDINARY ROWS', 8)))

def waiting_row():
    seat = f'<span style="width: 28px; height: 28px; border-radius: 14px; border: 1.5px dashed {ANCHOR}; box-sizing: border-box; flex: none; margin-left: -8px; background: {PAPER};"></span>'
    lead = f'<span style="display: inline-flex; align-items: center; flex: none;">{facepile(["M", "A"], 28, -8)}{seat}</span>'
    return f'<div class="row" style="padding: 8px 0;">{lead}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">waiting on the place call &middot; yours</span></span>{CHEV}</div>'

def status_row(last=False):
    return arow('Theo &middot; just back from Lisbon &middot; <span style="color: #6E6862;">10 days &middot; a featured status, city precision</span>', avatars=['T'], last=last)

def note_door():
    return door('Maya&rsquo;s Red Hook note, when you go') + meta('MAYA &middot; MAY-USE &middot; A DOOR TO THE OBJECT, NOT THE OBJECT', 0)

def authorized_door():
    return door('The Rome and Paris comparison, when you want it') + meta('RENDERS ONLY UNDER MAY-USE &middot; OTHERWISE YIELDS SILENTLY &middot; THE COMPARISON ITSELF IS ON 10', 0)

def settling_card():
    return card(title('The trip has settled into Life', 20, 25, 600) + sup('690 photographs, three tickets, and the ferry morning are in place. One honest return is ready when you want it; nothing was shared.', INK2)
                + meta('SINCE YOU LANDED &middot; TEN DAYS &middot; NO RECAP, NO RATING', 8) + door('Europe, in Life'))

def capability_field():
    return (f'<div style="border-left: 2px solid {GOLD}; padding-left: 12px;">' + u2('Resolve the physical burden first; let interpretation return after', 'Route, shade, water, and a stopping point, then the rest. What the Rome days taught, usable on any hot day here.', meta_t='A CAPABILITY, FROM THE JOURNEY &middot; NOT A MEANING &middot; FEEDS SATURDAY&rsquo;S SHAPE') + '</div>')

def voice_horizon():
    return (f'<div style="{SERIF} font-style: italic; font-size: 17px; line-height: 24px; color: {INK2};">Virgil sends Aeneas along the same Campanian coast you crossed, past the Sirens&rsquo; cliffs traditionally placed on the Sorrentine peninsula, then into Cumae. Rome mapped its founding story onto a coastline people already sailed. It will keep.</div>'
            + meta('ONE THREAD WITH NO DEADLINE &middot; NEVER AN AUTO-SAVE, A REMINDER, OR A LIST ENTRY', 8))

# ───────────────────────────── the pages ─────────────────────────────
def return_page():
    """Persona B, Thursday evening, first open in ten days. The dominant is the return itself: a voice statement promoted into the read; no crown."""
    inner = merged_read()
    inner += since_rows()
    inner += sect('In motion') + gut(waiting_row() + status_row(last=True))
    inner += sect('Worth knowing') + gut(capability_field())
    inner += gut('<div>' + note_door() + '<div style="height: 14px;"></div>' + authorized_door() + '</div>', top=26)
    inner += sect('Continuity') + gut(settling_card() + '<div style="height: 26px;"></div>' + voice_horizon())
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("ferry", "SOR&rarr;AMALFI")}{chip("flight", "FCO&rarr;JFK")}{chip("dining", "Maya and Alex", "ring", serif=True)}</div>' + meta('LIFE &middot; THE JOURNEY, THE FLIGHT HOME, SATURDAY&rsquo;S DINNER', 8), top=32)
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)],
                    'Saturday, dinner with Maya and Alex.')
    return phone(inner, 0)

def next_morning():
    """Friday 9:05, the next open. The delta was consumed; the page returns to its ordinary shape, and Saturday's prepared possibility takes the crown."""
    inner = anchor_row('NEW YORK &middot; FRIDAY', '9:05 AM') + orientation('Clear, 64&deg;. Saturday is open until dinner.', 'Low water at 2:40 &middot; Maya and Alex at 8:15.')
    inner += prepared_crown()
    inner += sect('In motion') + gut(waiting_row().replace('waiting on the place call &middot; yours', 'settled &middot; the noodle bar').replace(f'border: 1.5px dashed {ANCHOR}', 'border: 0; width: 0') + status_row(last=True))
    inner += sect('Worth knowing') + gut(u2('The pier at low water is the shaded side after two', 'The warehouses take the sun off the water walk by 2:30; the return by land is the warm way.', meta_t='TIDE TABLE + THE SUN&rsquo;S ANGLE &middot; FIXTURE'))
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("dining", "Maya and Alex", "ring", serif=True)}</div>' + meta('THE DELTA WAS READ ONCE; IT DOES NOT REPEAT', 8), top=32)
    inner += ending([('FRI', dm('solid', INK), 'today', INK), ('SAT', dm('av:M', ''), 'dinner', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Saturday, the water, then dinner.')
    return phone(inner, 0)

def kinds_map():
    return {re.search(r'<span class="kn">([^<]+)</span>', c).group(1): c for c in kinds_cells()}

def kinds_cells():
    ON = 'AS DRAWN ON 11 &middot; THE RETURN PAGE'
    return [
        cell('now_merged_into_read', 'EXISTS &middot; RULING', spec(merged_read()), ON + ' &middot; THE DOMINANT IS A VOICE STATEMENT; IT PROMOTES INTO THE READ; NO CROWN RENDERS'),
        cell('now_prepared_possibility', 'ADAPT', spec(prepared_crown().replace('margin: 22px 22px 0 22px', 'margin: 8px 22px 0 22px')), 'AS DRAWN ON 11 &middot; THE NEXT MORNING &middot; SERIF TITLE, ONE INSTRUMENT, ONE CTA; OPENING IT ADOPTS NOTHING'),
        cell('continuity_since_you_looked', 'ADAPT', spec(since_rows().replace('padding: 40px 22px 0 22px', 'padding: 8px 22px 0 22px')), ON + ' &middot; A SECTION OF ROWS, ONE PER CHANGE, WITH THE KIND MARK WHERE THE SUBJECT IS A KEPT OBJECT; READ ONCE'),
        cell('people_waiting_row', 'EXISTS', spec(gut(waiting_row() + '<div style="border-top: 1px solid rgba(27,23,20,0.06);"></div>', top=8)), ON + ' &middot; THE DASHED SEAT IS THE ONE OPEN CHAIR; NEVER A GUILT BADGE'),
        cell('people_status_aperture', 'ADAPT', spec(gut(status_row(last=True), top=8)), ON + ' &middot; A FEATURED STATUS AS A DOORWAY; CITY PRECISION; THE STATUS ITSELF LIVES IN PLACES &middot; ELSEWHERE (06)'),
        cell('people_note_door', 'ADAPT', spec(gut(note_door(), top=8)), ON + ' &middot; THE DOOR LAW: GOLD TEXT + THE ONE ARROW; THE NOTE IS THE OBJECT BEHIND IT'),
        cell('people_authorized_door', 'BUILD', spec(gut(authorized_door(), top=8)), ON + ' &middot; RENDERS ONLY UNDER MAY-USE; ITS SILENCE IS NOT AN EMPTY STATE'),
        cell('continuity_settling', 'BUILD', spec(gut(settling_card(), top=8)), ON + ' &middot; A CARD BECAUSE THE JOURNEY IS A COHERENT OBJECT; STATUS AS A CLAUSE, NOT A METER'),
        cell('continuity_capability_field', 'BUILD', spec(gut(capability_field(), top=8)), ON + ' &middot; THE 2PX GOLD LEFT RULE KEPT: IT MARKS A CAPABILITY THAT FEEDS A LATER COMPOSITION'),
        cell('continuity_voice_horizon', 'BUILD', spec(gut(voice_horizon(), top=8)), ON + ' &middot; THE VOICE ITALIC REGISTER, ONE PER PAGE; NO CLOCK, NO DOOR'),
    ]

MAPPING = [
    ['Now', 'The lead: a crown, or the read itself when the dominant is a voice statement', 'No heading; the first thing after the read'],
    ['In motion', '&ldquo;In motion&rdquo;', 'Rows: arrangements, people, commitments, claims'],
    ['Horizons', '&ldquo;Today&rdquo;, &ldquo;This week&rdquo;, &ldquo;Worth knowing&rdquo;, &ldquo;The city this week&rdquo;, &ldquo;Also in the city this week&rdquo;', 'Possibilities, findings, methods, city facts, reading'],
    ['With people (reservoir)', 'Inside the region it changes; &ldquo;Addressed to you&rdquo; only under its condition', 'Never a standing chapter'],
    ['Continuity', '&ldquo;Since you last looked&rdquo;, &ldquo;From the trip&rdquo;, &ldquo;Continuity&rdquo;, the Life door and its shelf', 'Reconstruction, settling, capability, voice, the record'],
    ['The end', 'The seam and one forward line', 'Never a coda'],
]

def return_board():
    cells = kinds_cells()
    under = [notecol('The return after absence', [
                ('THE RULE', N('When the last open is more than a few days back, the dominant is the return itself: a voice statement promoted into the read, no crown. &ldquo;Since you last looked&rdquo; renders once, as rows, one per material change, in the order they happened; then they are ordinary rows or gone. Nothing is a recap and nothing narrates what the product did.')),
                ('WHAT QUALIFIES AS A CHANGE', N('A commitment resolved (the refund paid), an import finished, an occurrence that happened to someone in your rows (Dana&rsquo;s Sunday), a withdrawn source (as an honest line). Not: things Vesper composed while you were away. Ignored suggestions leave no trace.')),
                ('THE CHAIR', N('The waiting row&rsquo;s dashed seat is the one open chair, the decision that is yours. It is not a badge and it does not count down. On Friday it is filled and the row says so.')),
             ], w=520),
             notecol('Region to section heading', [('THE MAPPING, WRITTEN DOWN', tbl(['REGION (CANON)', 'HEADINGS USED ON THESE BOARDS', 'WHAT LIVES THERE'], MAPPING))], w=684)]
    grid = ('<div style="width: 1250px; flex: none;"><div class="grid" style="display: grid; grid-template-columns: repeat(3, 393px); gap: 30px 26px; align-items: start;">' + ''.join(cells) + '</div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 40px; padding-top: 6px; border-top: 1px solid rgba(27,23,20,0.12);">' + ''.join(under) + '</div></div>')
    cols = [f'<div style="display: flex; flex-direction: column; flex: none;">' + caption('THE NINE KINDS &middot; REDRAWN', 'In the four type roles, at phone width', 'THESE WERE DRAWER SPECIMENS ON 01 &middot; EACH NOW HAS A PAGE') + grid + '</div>',
            col(return_page(), daycap('THURSDAY 7:40 PM &middot; FIRST OPEN IN TEN DAYS', '1 &middot; THE RETURN AFTER ABSENCE', 'What changed, what settled, what waits', 'VOICE READ, NO CROWN &middot; THREE CHANGES &middot; THE OPEN CHAIR &middot; TWO DOORS &middot; THE SETTLED TRIP &middot; THE THREAD')),
            col(next_morning(), daycap('FRIDAY 9:05 AM &middot; THE NEXT OPEN', '2 &middot; THE DELTA CONSUMED', 'The ordinary shape returns; Saturday takes the crown', 'SINCE-YOU-LOOKED DOES NOT REPEAT &middot; THE PREPARED HALF-DAY LEADS'))]
    return page(2200, hh('11'), f'VESPER &middot; HOME &middot; 11 &middot; RETURN AND CONTINUITY &middot; THE NINE KINDS, REDRAWN &middot; {PASS} &middot; {STAMP}', '11 &middot; The nine kinds that had no current drawing, on the page they belong to',
                'Nine of the 35 kinds were still August 31 drawer specimens on 01. Each is redrawn here in the four type roles and placed on a return-after-absence page: Persona B opening Home ten days after landing, then the next morning. The region-to-heading mapping the boards use is written down for the first time.', cols)

# ───────────────────────────── 12 · why this, the chat aperture, degraded states ─────────────────────────────
def why_door():
    return f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 6px;"><span class="fn" style="color: {ANCHOR}; flex: 1;">TWO STATIONS + FORECAST &middot; FIXTURE</span><span style="font-size: 12px; font-weight: 500; color: {GOLDD}; flex: none;">Why this</span>{ARROW}</div>'

def cold_with_why():
    return COLD().replace(meta('TWO NEARBY STATIONS + FORECAST &middot; FIXTURE'), why_door())

def why_sheet():
    """The Why-this sheet over the dimmed Sunday page: sources, what is yours, what is inferred, the four controls."""
    base = gut(cold_with_why(), top=22)
    dim = (f'<div style="position: relative;">' + anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM') + orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon.') + sect('Worth knowing') + base
           + f'<div style="position: absolute; inset: 0; background: rgba(27,23,20,0.35);"></div></div>')
    rows = ''.join(f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 8px 0; border-top: 1px solid rgba(27,23,20,0.07);"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {c}; width: 76px; flex: none; padding-top: 2px;">{k}</span><span style="font-size: 13px; line-height: 18px; color: {INK};">{v}</span></div>'
                   for k, v, c in [('SOURCES', 'Two stations, both within a mile of your walk (names in the source list); the forecast at 6:00; the exposure mechanism, one authored entry.', GOLDD),
                                   ('YOURS', 'Your Thursday walk: the route you took twice this month, kept as movement rows.', UMBER),
                                   ('INFERRED', 'The four-degree figure: read from the two stations tonight, not from the prose. It changes when they do.', OX),
                                   ('NOT USED', 'Nothing about you beyond the route. No one else&rsquo;s material.', GHOST)])
    sheet = (f'<div style="margin: -260px 0 0 0; background: {CARD}; border-radius: 18px 18px 0 0; box-shadow: 0 -8px 24px rgba(27,23,20,0.14); padding: 14px 22px 26px 22px; position: relative;">'
             f'<div style="width: 36px; height: 4px; border-radius: 2px; background: rgba(27,23,20,0.15); margin: 0 auto 14px auto;"></div>'
             + title('Why this', 20, 25, 600) + sup('The river side runs four degrees colder than the avenue, Thursday night.') + f'<div style="margin-top: 10px;">{rows}</div>'
             + f'<div style="display: flex; flex-wrap: wrap; gap: 10px 22px; margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(27,23,20,0.10);">{door("Open the sources")}{door("Ask about this")}{door("Not this again", MUTE)}{door("Correct the walk", MUTE)}</div>'
             + meta('NOT THIS AGAIN = EXCLUDE FROM RESURFACING &middot; CORRECT = FIX THE SOURCE, DEPENDENTS RECOMPILE &middot; NOTHING HERE WRITES ANYTHING ABOUT YOU', 10) + '</div>')
    return phone(dim + sheet, 0)

def sunday_with_aperture():
    html = ga.sunday_after()
    old = "meta_t='ONE RIDE, TWO THINGS THAT ONLY HAPPEN TODAY &middot; MAYA&rsquo;S SHARE, IN PLACES &middot; TIDE TABLE'"
    # add the one Chat aperture on the dominant object: a door after the card's meta line
    marker = 'ONE RIDE, TWO THINGS THAT ONLY HAPPEN TODAY &middot; MAYA&rsquo;S SHARE, IN PLACES &middot; TIDE TABLE</div>'
    assert marker in html
    return html.replace(marker, marker + door('Talk about today'), 1)

def chat_seeded():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">SUNDAY 9:12 AM</span></div></div>')
    inner += gut(f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {INK};">TODAY, IN ORDER &middot; SUNDAY &middot; FROM HOME</span></div>'
                 + f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">The sequence, its two stops, Maya&rsquo;s share and the tide table arrive as context. Nothing changes until you say.</div>', top=26)
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">can the pier come first and the bakery after, if I sleep in</div></div>', top=24)
    inner += gut(f'<div style="max-width: 330px; display: flex; flex-direction: column; gap: 10px;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Yes, but the loaf will not last: Maya said before eleven, and low water runs to four. Pier at 1:40, bakery by 3:30 is the other order; the loaf is the risk.</div>'
                 f'<div class="fn" style="color: {ANCHOR};">ANSWER ONLY &middot; THE SEQUENCE ON HOME IS UNCHANGED UNTIL YOU ASK TO CHANGE IT</div></div>', top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">Ask, or change it</span></div>', top=36)
    inner += f'<div style="padding: 30px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING BOUNDARY &middot; CHAT OWNS THE TURN &middot; HOME CARRIED THE ENVELOPE</div></div>'
    return phone(inner, 0, active='Chat')

def stale_page():
    """Opened after two days offline. Nothing is invented: state rows stand; live facts are withheld until the refresh lands, and the page says when it was last true."""
    inner = anchor_row('NEW YORK &middot; SUNDAY', 'AS OF FRI 6:40 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {MUTE};">Sunday. Alex&rsquo;s birthday and Dana on Saturday.</div>'
              f'<div class="fn" style="margin-top: 6px; color: {ANCHOR};">LAST TRUE FRIDAY 6:40 PM &middot; REFRESHING &middot; WEATHER AND TIDE WITHHELD UNTIL THEY ARE CURRENT</div></div>')
    inner += sect('In motion') + gut(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; as of Friday</span>', avatars=['A', 'M', 'you'])
                                     + arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D'])
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times as of Friday</span>')
                                     + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(u2('Thursday night the river side of your walk runs colder than the avenue', 'Open water and wind keep the waterfront blocks from holding the day&rsquo;s heat; two streets in, masonry gives it back for hours.',
        f'<div style="display: flex; gap: 18px; margin-top: 6px; padding-top: 8px; border-top: 1px solid rgba(27,23,20,0.06);"><div style="flex: 1;"><span class="kickm">RIVER SIDE</span><div style="{SERIF} font-size: 26px; line-height: 30px; color: {GHOST};">&mdash;</div></div><div style="flex: 1;"><span class="kickm">THE AVENUE</span><div style="{SERIF} font-size: 26px; line-height: 30px; color: {GHOST};">&mdash;</div></div></div>',
        meta_t='THE MECHANISM HOLDS; THE NUMBERS ARE WITHHELD UNTIL THE STATIONS ANSWER'))
    inner += gut(door('Everything in Life') + meta('THE RECORD IS LOCAL; IT IS NEVER STALE', 0), top=32)
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'Alex', INK)],
                    'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def unknown_pass():
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid rgba(27,23,20,0.06);">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">The airline&rsquo;s feed stopped answering at 4:52. Plan on 6:45 until it does.</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">Gate B22 and boarding at 6:05 are the last things it said. Nothing here is newer than that.</div>'
             f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 6px;">{door("Check with the airline")}{door("The way there", MUTE)}</div>'
             f'<div class="fn">NOT &ldquo;ON TIME&rdquo;, NOT &ldquo;DELAYED&rdquo;: UNKNOWN &middot; RE-ASKING EVERY FEW MINUTES &middot; TICKETS UNCHANGED</div></div>')
    html = pass_flight('live', extra=extra, elevated=True)
    html = html.replace('BOARDING 6:05 &middot; LEAVE BY 3:40', 'STATUS UNKNOWN SINCE 4:52').replace(f'background: {OX}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {OX};">STATUS UNKNOWN', f'background: {MUTE}; flex: none;"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {MUTE};">STATUS UNKNOWN')
    html = html.replace('CURRENT AS OF 3:12 &middot; GATE FROM PROVIDER', 'LAST TRUE 4:52 &middot; THE FEED IS NOT ANSWERING')
    return '<div style="margin: 22px 22px 0 22px;">' + html + '</div>'

def unknown_page():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '5:06 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">TAP 214: nothing new since 4:52. Plan on 6:45.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">The airline&rsquo;s feed is not answering &middot; the board at B22 is the other source &middot; Maya and Alex&rsquo;s 8:10 is on time.</div></div>')
    inner += unknown_pass()
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; their feed is answering</span>', avatars=['M', 'A'], last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', MUTE), 'JFK?', MUTE), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boarding as last posted: 6:05 from B22.')
    return phone(inner, 0)

def import_pending():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '11:20 AM') + orientation('Home. Clear, 64&deg;, low water at 2:40.', 'Landed 6:40 &middot; Saturday is dinner with Maya and Alex.')
    inner += gut(ways_card('This afternoon', [
        ('The pier at low water', 'The first walk back can be the one you know. Low water 2:40 to 5.', 'LOW WATER 2:40&ndash;5'),
        ('Stay in', 'The noodle shop delivers until ten.', 'ANY TIME'),
    ], 'PHOTOS IMPORTING &middot; 120 OF 690'), top=22)
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled</span>', avatars=['M', 'A', 'you'])
                                     + row_mark('flight', 'Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', last=True))
    inner += sect('From the trip') + gut(recon_strip([('9:10', 'ferry', 'TICKET', ''), ('9:14', 'photo', 'HARBOR', 'IMPORT CONTINUES'), ('&middot;', 'photo', 'PENDING', '')],
        t='Sorrento to Amalfi by ferry: the harbor at 9:14, so far', text='One ticket and one photograph are in. The rest of the morning fills in as the import runs; nothing is written until it does.',
        meta_t='TICKET 9:10 &middot; PHOTOGRAPH 9:14 &middot; 120 OF 690 IMPORTED &middot; NO ARRIVAL CLAIMED YET', door_text='The trip, in Life').replace('<span style="width: 30px; height: 22px; border-radius: 4px; background: #2A241E; display: inline-block;"></span></span><span style="font-family: \'JetBrains Mono\', ui-monospace, monospace; font-size: 10px; font-weight: 700; color: #1B1714;">&middot;', '<span class="hatch" style="width: 30px; height: 22px; border-radius: 4px; display: inline-block;"></span></span><span style="font-family: \'JetBrains Mono\', ui-monospace, monospace; font-size: 10px; font-weight: 700; color: #1B1714;">&middot;'))
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon.', last=True) + '</div>')
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), 'market', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK)],
                    'Saturday, dinner with Maya and Alex.')
    return phone(inner, 0)

def why_board():
    cols = [col(phone(anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM') + orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon.') + sect('Worth knowing') + gut(cold_with_why()) + gut(f'<div style="padding-top: 20px;"><div class="fn" style="color: {ANCHOR};">THE METADATA LINE IS THE TRUST FOOTPRINT; &ldquo;WHY THIS&rdquo; IS ITS DOOR &middot; ONLY ON CONSEQUENTIAL UNITS (INFERENCE, SOCIAL MATERIAL, WORLD DATA); NEVER ON A PLAIN FACT ROW</div></div>'), 0),
                daycap('THE AFFORDANCE', '1 &middot; WHY THIS, ON THE UNIT', 'The metadata line becomes a door', 'ONE SMALL DOOR AT THE END OF THE TRUST FOOTPRINT &middot; NOT A BUTTON, NOT AN ICON')),
            col(why_sheet(), daycap('THE SHEET', '2 &middot; WHY THIS, OPENED', 'Sources, yours, inferred, not used; four controls', 'CONTRACT &sect;3.8: CORRECT, EXCLUDE, RELEASE, OPEN THE SOURCES &middot; WRITES NOTHING ABOUT YOU')),
            col(sunday_with_aperture(), daycap('THE CHAT APERTURE', '3 &middot; ONE DOOR PER PAGE, ON THE DOMINANT OBJECT', '&ldquo;Talk about today&rdquo; under the sequence', 'EDITORIAL CANON &sect;11: ONE OBJECT-LEVEL APERTURE MAY HAND OFF TO CHAT &middot; EVERY OTHER UNIT REACHES CHAT THROUGH WHY THIS')),
            col(chat_seeded(), daycap('CHAT &middot; SEEDED', '4 &middot; THE TURN, WITH THE OBJECT AS CONTEXT', 'Answer only; Home is unchanged until asked', 'THE ENVELOPE ARRIVES &middot; NO SECOND COMPOSER ON HOME &middot; EXISTING BOUNDARY'))]
    row2 = [col(stale_page(), daycap('SUNDAY &middot; OPENED AFTER TWO DAYS OFFLINE', '5 &middot; STALE', 'Last true Friday; live facts withheld', 'STATE ROWS STAND &middot; THE MECHANISM HOLDS; THE NUMBERS WAIT &middot; THE RECORD IS NEVER STALE')),
            col(unknown_page(), daycap('FRIDAY 5:06 PM &middot; THE FEED STOPS', '6 &middot; PROVIDER UNKNOWN', 'Not on time, not delayed: unknown', 'THE PASS KEEPS ITS LAST TRUTHS AND SAYS WHEN &middot; NO FABRICATED GATE &middot; A DOOR TO THE OTHER SOURCE')),
            col(import_pending(), daycap('SUNDAY 11:20 &middot; 120 OF 690', '7 &middot; IMPORT PENDING', 'The strip shows what is in, and stops', 'ONE TICKET, ONE PHOTOGRAPH &middot; NO ARRIVAL CLAIMED &middot; THE HATCH IS THE IMPORT')),
            notecol('Three states a first build meets first', [
                ('STALE', N('Opened after two days without a connection. The state rows are what they were on Friday and say so; the read drops to direct state in the mute colour with a last-true line; the cold split keeps its mechanism and withholds its numbers. Nothing is invented to look fresh. The Life door notes that the record is local and never stale.')),
                ('PROVIDER UNKNOWN', N('The airline&rsquo;s feed stops answering on the day of. The pass keeps the last things it said and the minute it said them; the status line is mute, not oxblood, because nothing is known to have changed; the CTA becomes a door to the other source (the board at the gate). Unknown is a state with its own words, never smoothed into &ldquo;on time&rdquo;.')),
                ('IMPORT PENDING', N('Day zero with a fifth of the photographs in. The reconstruction strip draws only the evidence that exists and ends in a hatched pending node; the arrival is not claimed. The alternatives card carries the count as one clause, as before.')),
                ('NOT DRAWN', N('Night and dark (kernel &sect;11.3, deferred). Screen-reader order for the sheet: title, the claim, the four rows in order, the doors in order.')),
             ], w=430)]
    html = page(1820, hh('12'), f'VESPER &middot; HOME &middot; 12 &middot; WHY THIS, THE CHAT APERTURE, AND DEGRADED STATES &middot; {PASS} &middot; {STAMP}', '12 &middot; Three affordances Home had no component for',
                'The inspect door and its sheet on a consequential unit; the one Chat aperture per page and the seeded turn it opens; and the three degraded states the ledger only named: stale, provider unknown, import pending.', cols)
    extra = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">DEGRADED STATES &middot; STALE, UNKNOWN, PENDING</div>'
             f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Honest when the world stops answering</div></div>'
             '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', extra + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

FILES = {'11 - Return and Continuity': return_board, '12 - Why This, Chat, and Degraded States': why_board}
if __name__ == '__main__':
    for name, fn in FILES.items():
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
