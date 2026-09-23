"""Vesper — Home · the merge (2026-09-05). One telling: every phone drawn once, only the current
revision, ordered as a reader would read it. 01 Parts is regenerated from the 35-kind union as
drawn on the current boards; process and history move to 07 Ledger; the September 4 baseline is
archived as Z1–Z4."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
import gen_generous as g1
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
import gen_homeproj as gp
from gen_generous import caption, col, head, FOOT, N, WEEK_SUN, ending, arow, facepile, compare2, collapsed
from gen_generous3 import sect, meta, title, sup, gut, u2, card, handoff_card, ways_card as _wc, fact, reading_card, kept_row, COLD
from gen_generous4 import ways_card, h1_floor, DELETION, v3
from gen_generous3 import v2
from gen_homeproj import extract_div

SRC = os.path.join(os.path.dirname(__file__), 'homeproj')
OUT = os.path.join(os.path.dirname(__file__), 'merged'); os.makedirs(OUT, exist_ok=True)
H = json.load(open(os.path.join(OUT, 'heights.json'))) if os.path.exists(os.path.join(OUT, 'heights.json')) else {}
def hh(name, default=0): return H.get(name, default)

STAMP = 'MERGED 2026-09-05'

# ───────────────────────────── page composer: phones in a row, notes below ─────────────────────────────
def page(w, h, kick, ttl, sub, cols, notes=(), foot=FOOT, row_labels=None):
    body = '<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols) + '</div>'
    if notes:
        body += '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + ''.join(notes) + '</div>'
    return (HEAD + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, ttl, sub) + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)

def daycap(day, k, t, s2=''):
    """caption with a day label above (the week reads left to right)."""
    return f'<div class="shead" style="color: {GOLDD}; margin-bottom: 10px;"><span>{day}</span><span class="rule"></span></div>' + caption(k, t, s2)

# ───────────────────────────── 01 · Parts ─────────────────────────────
def find_block(html, needle, opener):
    i = html.index(needle); s = html.rindex(opener, 0, i); return extract_div(html, s)
CARD_OPEN = '<div style="background: #FBF7EC; border-radius: 18px; box-shadow'
CROWN_OPEN = '<div style="margin: 22px 22px 0 22px; background: #FBF7EC; border-radius: 18px;'
U2_OPEN = '<div style="display: flex; flex-direction: column;">'

def drawer_cells():
    """The 08-31 drawer cells (Study 1), by kind, with their lag lines, for kinds no current board redrew."""
    s = open(os.path.join(SRC, 'Main.dc.html')).read()
    css = s[s.index('<style>') + 7:s.index('</style>')]
    cells = {}
    for m in re.finditer(r'<div class="cell"><div class="lab"><span class="kn">(\w+)</span>', s):
        cells[m.group(1)] = extract_div(s, m.start())
    return cells, css

def scope_css(css, prefix='.drawer'):
    out = []
    for rule in css.split('}'):
        if '{' not in rule: continue
        sel, body = rule.split('{', 1)
        sels = [x.strip() for x in sel.split(',') if x.strip()]
        sels = [f'{prefix} {x}' if not x.startswith('body') and not x.startswith('@') else x for x in sels]
        out.append(', '.join(sels) + ' {' + body + '}')
    return '\n'.join(out)

def spec(inner, bg=PAPER):
    return f'<div style="width: 393px; background: {bg}; padding: 4px 0 22px 0; box-sizing: border-box; {SANS} color: {INK};">{inner}</div>'

def cell(kind, grade, inner, source, lag=None):
    g = {'BUILD': 'gB', 'ADAPT': 'gA', 'EXISTS': 'gE'}.get(grade.split()[0], 'gA')
    out = f'<div class="cell"><div class="lab"><span class="kn">{kind}</span><span class="{g}">{grade}</span></div>{inner}<div class="fn" style="color: {ANCHOR};">{source}</div>'
    if lag: out += f'<div class="fn" style="color: {OX};">LAGS A RULED LAW &middot; {lag}</div>'
    return out + '</div>'

def parts():
    dc, dcss = drawer_cells()
    def lifted(kind, note):
        c = dc[kind]
        return f'<div class="drawer">{c}</div>'.replace('<div class="cell">', '<div class="cell" style="gap: 6px;">', 1), note
    h1 = g5.h1v5(); h2 = g5.h2v5_t2(); h4d = g3.h4v2_during(); h5 = g4.h5v4(); h6o = g4.h6_organizer(); h6j = g4.h6_joiner(); h6l = g4.h6_live(); h3f = g3.h3v2_first(); fl = h1_floor()
    ON = lambda b: f'AS DRAWN ON {b}'
    import gen_return as gr
    KC = gr.kinds_map()
    DR = 'FROM THE 08-31 DRAWER &middot; NOT REDRAWN ON ANY CURRENT BOARD'
    regions = [
        ('CHROME AND THE READ', [
            cell('world_read', 'BUILD', spec(anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM') + orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')), ON('02 &middot; SUNDAY') + ' &middot; AT THE FLOOR THE READ DROPS TO DIRECT STATE (02, PHONE 2)'),
            cell('root_shell', 'EXISTS &middot; DARK', spec(tabbar('Home').replace('margin-top: 28px;', 'margin-top: 8px;')), 'THE FOUR-ROOT BAR &middot; HOME &middot; CHAT &middot; PLACES &middot; LIFE &middot; ' + ON('EVERY PHONE')),
            cell('week_shape', 'BUILD', spec(ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.', top=8)), 'THE SEAM + ONE FORWARD LINE &middot; HOW EVERY PAGE NOW ENDS (D-H5: NO RELIEF CODA) &middot; ' + ON('02&ndash;05')),
        ]),
        ('NOW &middot; THE DOMINANT UNION (EXACTLY ONE RENDERS)', [
            cell('now_commitment_instrument', 'ADAPT', spec(g3.SHOW_CROWN('YOUR TICKET + SERVICE READ').replace('margin: 22px 22px 0 22px', 'margin: 8px 22px 0 22px')), ON('02 &middot; THURSDAY') + ' &middot; SERIF 22/600 TITLE, ONE ARRIVAL SPAN, ONE CTA'),
            cell('now_decision', 'ADAPT', spec(find_block(h4d, 'Two places still fit', CROWN_OPEN).replace('margin: 22px 22px 0 22px', 'margin: 8px 22px 0 22px')), ON('02 &middot; THURSDAY, DURING') + ' &middot; ONE ASK WITH A DEADLINE; THE TWO-PLACE COMPARISON COMPOSED FROM THE OCCASION&rsquo;S CANDIDATES'),
            cell('now_recovery_instrument', 'BUILD', spec(find_block(h6l, 'Leave at 11:10', CROWN_OPEN).replace('margin: 22px 22px 0 22px', 'margin: 8px 22px 0 22px')), ON('05 &middot; DAY THREE') + ' &middot; OXBLOOD REGISTER; THE ORIGINAL SPAN STRUCK, THE NEW ONE GOLD; ONE MESSAGE TO THE GROUP'),
            KC['now_prepared_possibility'],
            cell('now_temporal_posture', 'BUILD', *lifted('now_temporal_posture', DR + ' &middot; THE SAME CROWN CARRIES 03 &middot; FRIDAY (TYPE ROLES APPLIED THERE)')),
            cell('now_annotated_evidence', 'BUILD', spec(gut(find_block(h5, 'finish the pasta in the sauce', U2_OPEN), top=8)), ON('03 &middot; SUNDAY') + ' &middot; NOW A BARE FINDING WITH THE PHOTOGRAPH AS MEDIA, NOT A CROWN (CANON &sect;1: FINDINGS STAY BARE); ADVICE, NOT A KNOWN CAUSE'),
            cell('now_attributed_comparison', 'BUILD', spec(gut(find_block(h6o, 'Two stays sleep six', U2_OPEN), top=8)), ON('05 &middot; ORGANIZER') + ' &middot; TWO LANES INSIDE A BARE UNIT, COMPOSED FROM HELD OPTIONS + TWO CONTRIBUTIONS'),
            cell('now_invitation', 'ADAPT', spec(f'<div style="padding: 24px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Bring one thing when something has your attention.</div></div>' + gut(door('Try with yours', INK) + meta('OPENS CHAT &middot; A PHOTO OR A FORWARDED EMAIL', 0), top=10)), ON('04 &middot; FIRST OPEN') + ' &middot; REDUCED TO ONE LINE AND A DOOR; THE SAMPLE LEADS THE COLD POSTURE (BELOW)'),
            cell('now_sample_demonstration', 'BUILD &middot; ADMITTED 09-05', spec(gut(g3.sample_ticket(), top=8)), ON('04 &middot; FIRST OPEN, AND 05 &middot; JOINER') + ' &middot; STAMPED, DASHED INPUT &rarr; RESULT; FIXED AND REUSABLE; RETIRES AFTER TRIED OR IGNORED TWICE'),
            KC['now_merged_into_read'],
        ]),
        ('IN MOTION', [
            cell('motion_occasion_row', 'ADAPT', spec(gut(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you'], last=True), top=8)), ON('02 &middot; SUNDAY') + ' &middot; 44PX, FACEPILE ONLY BECAUSE PEOPLE ARE THE SUBJECT'),
            cell('motion_loose_end_row', 'ADAPT', spec(gut(row('Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', mark='dashed', last=True), top=8)), ON('03 &middot; SUNDAY') + ' &middot; STATUS MARK, NO ICON PLATE'),
            cell('motion_all_plans_door', 'EXISTS', spec(gut(door('All plans and occasions') + meta('DOOR.TSX &middot; GOLD TEXT + THE ONE ARROW', 0), top=8)), 'THE DOOR LAW, UNCHANGED'),
        ]),
        ('HORIZONS', [
            cell('horizon_prepared_alternatives', 'BUILD &middot; ADMITTED 09-05', spec(gut(find_block(h1, 'The sesame loaf, then the water', CARD_OPEN), top=8)), ON('02 &middot; SUNDAY') + ' &middot; UNNUMBERED, &ldquo;OR&rdquo; HAIRLINES, NO MARKS THAT READ AS CONTROLS; MAY LEAD ON A QUIET DAY'),
            cell('horizon_mechanism_row', 'ADAPT', spec(gut(COLD(), top=8)), ON('02 &middot; SUNDAY') + ' &middot; A BARE UNIT WITH A TWO-LANE INSTRUMENT; THE FOUR-DEGREE FIGURE IS A FIXTURE (07)'),
            cell('horizon_world_fact_row', 'BUILD &middot; ADMITTED 09-05', spec(gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>', top=8)), ON('02, 03, 04') + ' &middot; MARKED BY ITS SOURCE, NEVER A STANDING SECTION'),
            cell('horizon_editorial_passage', 'ADAPT', spec(gut(reading_card('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', 'The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.', 'Read the chapter'), top=8)), 'DRAWN IN REVISION 3, THEN CUT FROM 02 BY THE DELETION TEST (07) &middot; THE FORM STANDS; OPTIONAL DEPTH BEHIND A DOOR'),
            cell('horizon_aperture_row', 'EXISTS', spec(gut(row('The Sunset Park bakery &middot; <span style="color: #6E6862;">saved &middot; not yet visited</span>', mark='hollow', last=True), top=8)), ON('02 &middot; THE FLOOR') + ' &middot; A SAVED, UNVISITED PLACE AS ONE ROW'),
            cell('horizon_hidden_system', 'BUILD', *lifted('horizon_hidden_system', DR + ' &middot; 03 &middot; FRIDAY CARRIES THE SAME PASSAGE UNDER THE FOUR TYPE ROLES')),
        ]),
        ('WITH PEOPLE (A RESERVOIR, NOT A CHAPTER)', [
            cell('people_authored_region', 'BUILD &middot; ADMITTED 09-05', spec(find_block(h2, 'Addressed to you', '<div style="padding: 40px 22px 0 22px;">').replace('padding: 40px 22px 0 22px', 'padding: 8px 22px 0 22px') + gut(find_block(h2, 'The bookshop', '<div style="display: flex; flex-direction: column; gap: 16px;">')) + gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS &middot; THE CASUAL SHARES, ON THE MAP', 0), top=20)), ON('02 &middot; MONDAY') + ' &middot; RENDERS ONLY WHEN &ge;2 ADDRESSED CONTRIBUTIONS ARE UNSPENT ABOVE; ENDS WITH THE PULL DOOR TO PLACES'),
            cell('people_gathering', 'ADAPT', spec(gut(g3.alex_card(), top=8)), ON('02 &middot; MONDAY') + ' &middot; THE SHARED ARRANGEMENT AS A CARD: PLAN-INK STATUS, ONE SPAN, THE FACEPILE AT WEIGHT'),
            cell('people_participants_row', 'EXISTS', spec(gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled &middot; Maya added a photograph Friday</span>', avatars=['M', 'A', 'you'], last=True), top=8)), ON('03 &middot; SUNDAY')),
            KC['people_status_aperture'],
            KC['people_note_door'],
            KC['people_waiting_row'],
            KC['people_authorized_door'],
        ]),
        ('CONTINUITY', [
            cell('continuity_reconstruction', 'BUILD', spec(gut(find_block(h5, 'Sorrento to Amalfi by ferry', U2_OPEN), top=8)), ON('03 &middot; SUNDAY') + ' &middot; THE FERRY MORNING FROM A TICKET AND TWO PHOTOGRAPHS; GAPS STAY GAPS'),
            cell('continuity_life_door', 'EXISTS', spec(gut(door('Everything in Life') + meta('LIFE &middot; THE TICKET, THE NOTE, THE SAVED PLACE', 0), top=8)), ON('02 &middot; THE FLOOR')),
            KC['continuity_settling'],
            KC['continuity_capability_field'],
            KC['continuity_since_you_looked'],
            KC['continuity_voice_horizon'],
        ]),
        ('DRAWN ON THE BOARDS &middot; NOT IN THE HOME UNION', [
            cell('share_card &rarr; Places', 'PLACES', spec(gut(g3.share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 160, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'SUNSET PARK &middot; 14 MIN BY BIKE &middot; OPEN NOW', 'The bakery'), top=8)), 'THE CASUAL SHARE &middot; MOVED OFF HOME BY THE SOCIAL SPLIT (09-05) &middot; LIVES IN PLACES &middot; FROM FRIENDS (06); HOME KEEPS ONLY ITS EFFECT INSIDE &ldquo;TODAY&rdquo;'),
            cell('kept_row', 'EXISTS &middot; CHAT', spec(gut(kept_row('Your ticket &middot; Friday &middot; in Life'), top=8)), ON('04 &middot; WEDNESDAY') + ' &middot; THE T1 RECEIPT WITH UNDO, SHOWN ON HOME AFTER ONE CONTRIBUTION'),
            cell('collapsed (the fold)', 'BUILD', spec(gut(collapsed('THE REST OF THURSDAY &middot; STILL HERE', ['Tonight&rsquo;s cold: the river side runs four degrees colder', 'The skillet, preheated dry', 'Open House registration']), top=8)), ON('02 &middot; THURSDAY, DURING') + ' &middot; WHILE A PRIORITY HOLDS, THE REST FOLDS TO REACHABLE TITLES'),
        ]),
    ]
    body = head(f'VESPER &middot; HOME &middot; 01 &middot; PARTS &middot; THE HOME UNION AS DRAWN TODAY (35 KINDS) &middot; {STAMP}', 'Every part of Home, as it is drawn on the current boards',
                'One cell per kind in the 35-kind union (build manifest &sect;1.0&ndash;1.6, four kinds admitted 09-05), each lifted from the board that draws it now, with its grade and where to find it. Ten kinds that were still August 31 drawer specimens on 09-05 were redrawn on 11 (the return page) on 09-06; two (the temporal posture, the hidden system) remain drawer specimens, labelled so, with their lag lines kept. The last row holds three forms the boards use that are not Home kinds.')
    for t, cs in regions:
        body += f'<div class="shead" style="margin: 26px 0 14px 0;"><span>{t}</span><span class="rule"></span></div><div class="grid">' + ''.join(cs) + '</div>'
    body += f'<div class="fn" style="margin-top: 30px; line-height: 16px;">GRADES AND NAMES: docs/working/home-and-places-build-manifest-2026-08-30.md &sect;1 &middot; {FOOT}</div>'
    extra = ('<style>\n.grid { display: grid; grid-template-columns: repeat(4, 393px); gap: 30px 26px; align-items: start; }\n.cell { display: flex; flex-direction: column; gap: 8px; }\n'
             '.lab { display: flex; align-items: baseline; gap: 8px; border-bottom: 1px solid rgba(27,23,20,0.08); padding: 0 0 4px 0; }\n'
             ".kn { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.6px; color: #6E6862; }\n"
             ".gB, .gA, .gE { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 9px; font-weight: 700; letter-spacing: 0.8px; margin-left: auto; }\n.gB { color: #7A2E2E; } .gA { color: #8A6628; } .gE { color: #3D7050; }\n"
             + scope_css(dcss) + '\n.drawer .cell { padding: 0; } .drawer .lab { display: none; }\n</style>')
    doc = HEAD.replace('</helmet>', extra + '</helmet>') + f'<div style="width: 1720px; min-height: {hh("01")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + body + '</div>' + TAIL
    return doc

# ───────────────────────────── 02 · Persona A ─────────────────────────────
def persona_a():
    cols = [col(g5.h1v5(), daycap('SUNDAY 9:10 &middot; QUIET', '1 &middot; THE CEILING', 'A generous quiet Sunday', 'ALTERNATIVES LEAD &middot; ROWS &middot; THE COLD &middot; ONE CITY FACT &middot; THE FRIENDS DOOR')),
            col(h1_floor(), daycap('SUNDAY 9:10 &middot; QUIET', '2 &middot; THE FLOOR', 'What the first account will see', 'ONLY WHAT REAL OWNERS SERVE TODAY &middot; DIRECT STATE &middot; ROWS &middot; TWO HORIZONS')),
            col(g5.h2v5_t2(), daycap('MONDAY 6:40 &middot; SOCIAL', '3 &middot; ADDRESSED TO YOU', 'The week with two things addressed', 'ALEX&rsquo;S ARRANGEMENT LEADS &middot; THE REGION HOLDS ONLY WHAT WAS GIVEN TO HER')),
            col(g3.h2v2_sparse(), daycap('MONDAY 6:40 &middot; SPARSE', '4 &middot; NOTHING ADDRESSED', 'Only Dana this week', 'NO REGION, NO EMPTY MODULE, NO INVITE')),
            col(g3.h4v2_before(), daycap('THURSDAY 5:40', '5 &middot; BEFORE', 'The fuller Thursday', 'CROWN + ROWS + WORTH KNOWING + THE CITY')),
            col(g3.h4v2_during(), daycap('THURSDAY 6:05 &middot; PRIORITY', '6 &middot; DURING', 'One decision, 55 minutes', 'ONE ASK &middot; THE REST FOLDS, STAYS REACHABLE')),
            col(g3.h4v2_after(), daycap('THURSDAY 7:25', '7 &middot; AFTER', 'The fuller Home returns', 'THE SAME PAGE PLUS ONE CHANGED ROW')),
            col(g3.life_frame(), daycap('BEHIND THE DOOR', '8 &middot; THE RECORD', 'Life &middot; People', 'BY PERSON, WITH GRANTS &middot; EXISTING OWNER, NOT REDESIGNED'))]
    notes = [notecol('Reading the week', [
                ('ONE PERSON, ONE SKELETON', N('Nadia, a mature New York account in an ordinary week. Read left to right: a quiet Sunday at the ceiling and at the floor, the social Monday with and without addressed material, and Thursday before, during, and after a priority. Same read &rarr; lead &rarr; rows &rarr; a few units &rarr; seam on every phone.')),
                ('THE SOCIAL SPLIT, VISIBLE', N('Maya&rsquo;s casual bakery share is not on any of these phones; it lives in Places (06). Sunday keeps its effect inside the first option of &ldquo;Today&rdquo;, attributed. Monday&rsquo;s region holds only what was addressed: Dana&rsquo;s bookshop and Maya&rsquo;s noodle bar for after the show. The pull door on both points to Places &middot; From friends.')),
             ], w=560),
             notecol('Priority, checked', [
                ('DURING', N('Oxblood read, one crown with one instrument and one ask, two unchanged rows, the rest folded to three reachable titles, the seam marking Saturday with the open question.')),
                ('WHAT PERSISTS', ledger([('ANSWERING', 'A preference on the Occasion, attributed to you.'), ('NOT ANSWERING', 'Nothing. The crown expires at 7:00; Alex decides.'), ('NEVER', 'A pending badge; &ldquo;you didn&rsquo;t answer&rdquo;.')])),
             ], w=560),
             notecol('The floor, and the gap', [
                ('THE FLOOR', N('Phone 2 is what the real owners can serve today (implementation status, 2026-09-01): commitments and occasions, saved Places, addressed handoffs, receipts, the Life door. No world-read producer, no friends scope, no mechanism library, no city source. Nothing is invented to fill a slot.')),
                ('WHAT THE GAP SAYS', N('The distance between phone 1 and phone 2 is the content-production and owner-read backlog on 07, not a design defect. Judge the design at the floor as well as the ceiling. The deletion test that pruned phone 1 from eight units to five is on 07.')),
             ], w=560)]
    return page(3530, hh('02'), f'VESPER &middot; HOME &middot; 02 &middot; PERSONA A &middot; THE NEW YORKER &middot; ONE WEEK, EIGHT PHONES &middot; REVISION 5 &middot; {STAMP}', '02 &middot; Persona A &middot; the New Yorker in an ordinary week',
                'Sunday quiet at the ceiling and at the floor; Monday with and without addressed material; Thursday before, during, and after a priority; and the record behind the door. Every phone is the current revision; the earlier versions and the tests that produced these are on 07.', cols, notes)

# ───────────────────────────── 03 · Persona B ─────────────────────────────
SENTENCE = {'IN MOTION': 'In motion', 'THE HIDDEN SYSTEM': 'The hidden system', 'WHAT THE JOURNEY NOW LETS YOU DO': 'What the journey now lets you do',
            'ONE WAY TO TEST THE DISTINCTION IN NEW YORK': 'One way to test the distinction in New York', '&ldquo;AUTHENTIC&rdquo; IS TOO BLUNT FOR THIS QUESTION': '&ldquo;Authentic&rdquo; is too blunt for this question',
            'SINCE YOU LAST LOOKED': 'Since you last looked'}
def _sect(t, mute=True, top=44): return sect(SENTENCE.get(t, t.capitalize()), top=top)
def _unit_open(kick, t, body, plate=None, plate_label=None):
    pl = f'<div class="hatch" style="width: 56px; height: 56px; border-radius: 12px; flex: none; display: flex; align-items: center; justify-content: center;">{plate_label or ""}</div>' if plate == 'thumb' else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start;">{pl}<div style="flex: 1; min-width: 0;">' + u2(t, body, meta_t=SENTENCE.get(kick, kick)) + '</div></div>')
def persona_b_baseline(fn):
    old = (gp.section, gp.unit_open); gp.section = _sect; gp.unit_open = _unit_open
    try: return fn()
    finally: gp.section, gp.unit_open = old

def persona_b():
    cols = [col(g4.h5v4(), daycap('SUNDAY 11:20 &middot; LANDED', '1 &middot; DAY ZERO', 'New York first, while the trip settles', 'ALTERNATIVES &middot; ROWS &middot; THE DISH AS A FINDING &middot; THE FERRY MORNING &middot; THE CITY')),
            col(persona_b_baseline(gp.p2_temporal), daycap('FRIDAY 9:05 &middot; AVAILABLE', '2 &middot; WAIT UNTIL NOON', 'A temporal posture: a crown with no CTA', 'BASELINE 09-04 &middot; TYPE ROLES APPLIED 09-05 &middot; COMPOSITION NOT YET REVISED')),
            col(persona_b_baseline(gp.p2_evidence), daycap('SATURDAY 10:15 &middot; AVAILABLE', '3 &middot; THE DISH, AS EVIDENCE', 'Annotated evidence: photography leads', 'BASELINE 09-04 &middot; TYPE ROLES APPLIED 09-05 &middot; COMPOSITION NOT YET REVISED'))]
    notes = [notecol('Coming home', [
                ('DAY ZERO', N('Current-world value first while imports finish; status as one metadata clause; one reconstruction low on the page. The two P0 corrections stand: no marks on alternatives that read as controls, and a cooking headline that gives advice without asserting what a kitchen did.')),
                ('THE DISH', N('&ldquo;To get the texture you photographed, finish the pasta in the sauce&rdquo; is a bare finding with the photograph as media (canon &sect;1: findings stay bare). Saturday&rsquo;s dinner is never made into validation work.')),
             ], w=560),
             notecol('Phones 2 and 3 &middot; what a revision would change', [
                ('APPLIED HERE', N('Section headings in the sans role; the reading units in the serif-title / metadata roles. Nothing else was touched, so these two phones are honest about where the baseline stands.')),
                ('NOT YET APPLIED', N('The relief codas would become the seam and one forward line (D-H5). Phone 3&rsquo;s photograph crown would become a bare finding, as on phone 1, unless the evidence itself is the day&rsquo;s dominant. The italic voice line inside phone 2&rsquo;s crown is the one voice moment per page and stays.')),
                ('WHY THEY ARE HERE', N('They are the only drawings of two union kinds &mdash; the temporal posture and annotated evidence as a crown &mdash; and the return persona has no other states drawn. Superseded phones (day zero as a settling crown, the legacy Saturday, the Rome disruption) are on Z3.')),
             ], w=560)]
    return page(1360, hh('03'), f'VESPER &middot; HOME &middot; 03 &middot; PERSONA B &middot; BACK FROM EUROPE &middot; REVISION 4 &middot; {STAMP}', '03 &middot; Persona B &middot; the traveler just back from Europe',
                'Nice &rarr; Sorrento &rarr; Amalfi &rarr; Rome, now home in New York. Day zero at the current revision, then the two baseline states no revision has yet reached, with the type roles applied and the rest left as it stands.', cols, notes)

# ───────────────────────────── 04 · Persona C ─────────────────────────────
def persona_c():
    cols = [col(g3.h3v2_first(), daycap('TUESDAY 8:05 &middot; COLD', '1 &middot; FIRST OPEN', 'The sample first, one city offering beside it', 'NOTHING HELD &middot; NONPERSONAL LANGUAGE &middot; THE REST OF THE CITY LOWER')),
            col(g3.h3v2_sample(), daycap('THE SAMPLE, OPENED', '2 &middot; INSPECTED', 'A ticket and its evening', 'STUB &rarr; RESULT &middot; FOUR SHORT NOTES &middot; TRY WITH YOURS')),
            col(g3.h3v2_chat(), daycap('TUESDAY 8:12 &middot; CHAT', '3 &middot; ONE CONTRIBUTION', 'Bring the ticket', 'EXISTING BOUNDARY &middot; T1 RECEIPT WITH UNDO')),
            col(g3.h3v2_return(), daycap('WEDNESDAY 7:30 &middot; THIN', '4 &middot; THE RETURN', 'The personal return', 'THE CROWN IS THEIRS &middot; KEPT ROW &middot; A NOTICE TIED TO FRIDAY')),
            col(g3.h3v2_next(), daycap('SATURDAY 9:30 &middot; QUIET, THIN', '5 &middot; NEXT OPEN', 'No further contribution', 'NO ATTENDANCE INFERRED &middot; A DIFFERENT SAMPLE, AS A RESULT'))]
    notes = [notecol('Show the transformation; do not describe it', [
                ('THE ORDER', N('The ticket-to-evening sample is the first unit after the read, with one worthwhile city offering directly beneath it. No hero, no intake prompt. The city carries the page; the sample is stamped; the return after one contribution is the crown and a kept row.')),
                ('THE LANGUAGE', N('The account supplied a city only. &ldquo;The waterfront streets&rdquo;, never &ldquo;your walk&rdquo;; the sample never says where anyone leaves from; &ldquo;whether you went is yours to say&rdquo; on the next open is a material boundary, not rationale.')),
             ], w=560),
             notecol('Three sources, kept apart', [
                ('ACTUAL VS PROPOSED', ledger([('EXISTS', 'Chat intake with T1 receipt + Undo; Life holds the ticket; the commitment crown; service reads.'), ('NEEDS VERIFICATION', 'A city-scoped notice source with freshness; hall set-time reads.'), ('PROPOSED', 'The SAMPLE card and sheet as fixed, reusable demonstrations; retirement after tried or ignored twice; a world notice tied to a held commitment.')])),
             ], w=560)]
    return page(2240, hh('04'), f'VESPER &middot; HOME &middot; 04 &middot; PERSONA C &middot; THE NEW USER &middot; FIRST OPEN &rarr; NEXT OPEN &middot; REVISION 3 &middot; {STAMP}', '04 &middot; Persona C &middot; a new account, first open to next open',
                'No history, no profile, no saved places. A ticket-shaped input and the evening it becomes are visible before any explanatory copy; one contribution through Chat; the return; the next open with nothing further brought.', cols, notes)

# ───────────────────────────── 05 · Wedge, 06 · Places ─────────────────────────────
def wedge():
    cols = [col(g4.h6_organizer(), daycap('TUESDAY 8:40 &middot; PLANNING', '1 &middot; ORGANIZER', 'A trip forming, nine weeks out', 'ONE DECISION, FRIDAY &middot; CONTRIBUTIONS INSIDE THE ARRANGEMENT')),
            col(g4.h6_joiner(), daycap('TUESDAY 9:05 &middot; COLD', '2 &middot; JOINER', 'Invitation is not incorporation', 'HOST INTENT, A HELD SEAT, THREE ANSWERS, A SAMPLE')),
            col(g4.h6_live(), daycap('LISBON &middot; SUNDAY 8:20 &middot; URGENT', '3 &middot; DAY THREE', 'The shared day reshapes', 'RECOVERY DOMINANT &middot; ONE MESSAGE TO SIX &middot; PRIVATE STAYS PRIVATE'))]
    notes = [g4.H6_NOTES.replace('width: 430px', 'width: 560px')]
    n = g4.H6_NOTES
    notes = [notecol('The wedge, on Home', [('WHY THIS BOARD', N('The thesis names group travel as the launch wedge and &ldquo;keeping a shared experience coherent as reality changes&rdquo; as the product wedge. This board shows the arc: an organizer&rsquo;s Home while a trip forms, a joiner&rsquo;s first Home after an invite, and the live day under change.')),
                                              ('ORGANIZER', ledger([('LEAD', 'The trip as a shared-arrangement card: who has joined, what is open, when it closes. One decision on the page, and it is the organizer&rsquo;s.'), ('PEOPLE', 'Contributions appear as contributions, inside the arrangement and the comparison; no poll, no profile.'), ('DEMAND', 'One, with a Friday deadline. Everything else completes on view.')]))], w=560),
             notecol('Joiner and live change', [('JOINER', ledger([('INVITATION IS NOT INCORPORATION', 'Host intent in her words; one permissioned foothold (the held seat); three ways to answer, including a quiet decline; nothing shared about the joiner.'), ('VALUE BEFORE GROUP WORK', 'The same sample as 04 sits beneath: the product is useful before the joiner does anything for the group.')])),
                                                ('LIVE CHANGE', ledger([('PRIORITY', 'Recovery dominant, oxblood read, one instrument (the original span struck through, the new one gold), one ask that goes to the group as one message.'), ('PRIVATE STAYS PRIVATE', '&ldquo;Two of six asked to keep it slow; the group does not need to know who&rdquo; &mdash; the unattributed-aggregate law (kernel &sect;11.12.8).')]))], w=560)]
    return page(1360, hh('05'), f'VESPER &middot; HOME &middot; 05 &middot; THE WEDGE &middot; A TRIP FORMING &middot; REVISION 4 &middot; {STAMP}', '05 &middot; Group travel on Home: forming, invited, and under change',
                'The same skeleton, budgets, and type roles as 02&ndash;04, applied to the launch wedge: an organizer with one decision, a joiner who owes nothing tonight, and a live day that reshapes without exposing anyone. Lisbon and every person here are fixtures.', cols, notes)

def places():
    cols = [col(g5.p1_friends(), daycap('PLACES &middot; FROM FRIENDS', '1 &middot; THE SCOPE AND THE MAP', 'What my people shared, and where', 'FOUR PEOPLE, FOUR THINGS, THREE PRECISIONS &middot; IT ENDS')),
            col(g5.p1_focus(), daycap('PLACE FOCUS &middot; THE BAKERY', '2 &middot; A FRIEND&rsquo;S NOTE BESIDE THE VERDICT', 'The accepted social form, unchanged', 'FROM THE MAP, OR FROM HOME&rsquo;S &ldquo;TODAY&rdquo;'))]
    notes = [g5.P1_NOTES.replace('width: 440px', 'width: 560px') if 'width: 440px' in g5.P1_NOTES else g5.P1_NOTES.replace('flex: none; display: flex; flex-direction: column; gap: 22px;', 'flex: none; display: flex; flex-direction: column; gap: 22px; width: 560px;', 1)]
    cols = [c.replace('THE PIER AT SUNSET &#183; NEIGHBORHOOD', 'THE PIER &#183; NEIGHBORHOOD') for c in cols]
    cols = [c.replace('THE PIER AT SUNSET &#183; NEIGHBORHOOD', 'THE PIER &#183; NEIGHBORHOOD') for c in cols]
    return page(920, hh('06'), f'VESPER &middot; HOME &middot; 06 &middot; PLACES &middot; FROM FRIENDS &middot; REVISION 5 &middot; {STAMP}', '06 &middot; Casual sharing lives in Places, on a map that is semantic, not biometric',
                'Where Home&rsquo;s pull door lands. One scope over the same world, marks at the precision each person chose, a city-level &ldquo;Elsewhere&rdquo; for featured statuses, and the record behind it in Life People. Nothing here shows where anyone is.', cols, notes)

# ───────────────────────────── 07 · Ledger and decisions (+ history) ─────────────────────────────
def ledger_board():
    diag = json.load(open(os.path.join(SRC, 'diag.json')))
    html = g5.H0(diag)
    html = html.replace('GENEROUS-VALUE PASS &middot; REVISION 5 &middot; H0 &middot; THE SOCIAL SPLIT, CANON EVENTS, DISPOSITIONS, PRODUCTION, HANDBACK', f'07 &middot; LEDGER AND DECISIONS &middot; REVISION 5 &middot; {STAMP}')
    html = html.replace('The dispositions for section 5.3 A&ndash;E; diagnostics across three revisions;', 'Left: the social split, the canon events, the recommended composition, the dispositions for section 5.3 A&ndash;E, diagnostics across three revisions,')
    html = html.replace('and measured economics kept apart.', 'and measured economics kept apart. Right: the history behind 01&ndash;06 &mdash; the phones the current boards replaced, the alternative treatment that lost, the deletion test, and what moved under the social split.', 1)
    html = html.replace('H0 &middot; One composition, five dispositions, and a ledger that does not overclaim', '07 &middot; The system, the rulings, the ledger, and the history behind 01&ndash;06')
    html = html.replace('Board 1&ndash;4 untouched.', 'The September 4 baseline is archived as Z1&ndash;Z4.')
    html = html.replace('H0 - Ledger and Decisions &middot; H1 - Ordinary Sunday Generous &middot; H2 - Social Week Two Treatments &middot; H3 - First Open to Next Open &middot; H4 - Priority Stress Test &middot; H5 - Return Home Corrected',
                        'merged 09-05 into 01 Parts &middot; 02 Persona A &middot; 03 Persona B &middot; 04 Persona C &middot; 05 Wedge &middot; 06 Places &middot; 07 this ledger')
    pre, rest = html.split('<div style="display: flex; flex-direction: column; gap: 34px;">', 1)
    blocks, foot = rest.rsplit('<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)
    before = [col(v3('h1v3'), caption('BEFORE &middot; SUNDAY &middot; REVISION 3', 'Generous, eight units', 'THE INPUT TO THE DELETION TEST &rarr; 02 PHONE 1')),
              col(v3('h2v3_t2'), caption('BEFORE &middot; MONDAY &middot; REVISION 3', 'From your people', 'A CASUAL SHARE AND A HANDOFF IN ONE REGION &rarr; 02 PHONE 3')),
              col(v2('h3v2_first'), caption('BEFORE &middot; FIRST OPEN &middot; REVISION 2', 'A city briefing, then the sample', '&rarr; 04 PHONE 1')),
              col(v2('h5v2'), caption('BEFORE &middot; DAY ZERO &middot; REVISION 2', 'New York first, composed', '&rarr; 03 PHONE 1'))]
    alt = [col(g5.h2v5_t1(), caption('ALTERNATIVE CONSIDERED &middot; MONDAY', 'Treatment 1 &middot; distributed', 'ADDRESSED PLACES INSIDE THE UNITS THEY CHANGE &middot; NOT RECOMMENDED')),
           notecol('The deletion test (August 29 ruling), on Sunday', [('THE TEST', N('The smaller composition wins when it preserves the strongest value and range. Each unit was removed in turn and the loss named. Eight units in, five out.')), ('RESULTS', ledger([(k, f'{v} &middot; {r}') for k, v, r in DELETION]))], w=520),
           notecol('What moved, and why', [('SUNDAY', N('Maya&rsquo;s bakery share was casual, not addressed. Under the split it lives in Places under the friends scope; Home projects it only where it changes something today, inside the first option of &ldquo;Today&rdquo;, attributed. The lead card is gone; the prepared alternatives lead, as ruled for a quiet day.')),
                                            ('MONDAY', N('Treatment 1 distributes the two addressed places into the units they change. Treatment 2 (02, phone 3) shows them once each, in the person&rsquo;s own words, in a region that exists only because two addressed units were unspent above. Recommended: Treatment 2; the region&rsquo;s name is now honest about what it holds.')),
                                            ('THE RETURN AND THE FIRST OPEN', N('Day zero: unnumbered alternatives, the dish as a possibility, the ferry morning as the unit; then the two P0 corrections. First open: the sample before the city briefing, nonpersonal language, the useful result instead of analytical framing.'))], w=520)]
    right = ('<div style="width: 1710px; flex: none; display: flex; flex-direction: column; gap: 34px;">'
             f'<div class="shead"><span>HISTORY &middot; THE PHONES THE CURRENT BOARDS REPLACED</span><span class="rule"></span></div><div style="display: flex; gap: 46px; align-items: flex-start;">{"".join(before)}</div>'
             f'<div class="shead"><span>ALTERNATIVES AND TESTS</span><span class="rule"></span></div><div style="display: flex; gap: 46px; align-items: flex-start;">{"".join(alt)}</div></div>')
    html = (pre + '<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="width: 1560px; flex: none;"><div style="display: flex; flex-direction: column; gap: 34px;">' + blocks + '</div>' + right + '</div>'
            + '<div class="fn" style="margin-top: 30px; line-height: 16px;">' + foot)
    html = re.sub(r'width: 1560px; min-height: \d+px; background: #F4F0E7', f'width: 3380px; min-height: {hh("07")}px; background: #F4F0E7', html, count=1)
    return html

# ───────────────────────────── Z · archive ─────────────────────────────
def archive():
    out = {}
    s = open(os.path.join(SRC, 'Main.dc.html')).read()
    s = re.sub(r'class="kick">VESPER &middot; HOME &middot; STUDY &middot; BOARD 1[^<]*', f'class="kick">VESPER &middot; HOME &middot; Z1 &middot; ARCHIVE &middot; BASELINE 09-04 &middot; THE INVENTORY AS IT STOOD ON 08-31 (31 KINDS) &middot; SUPERSEDED BY 01 - PARTS &middot; {STAMP}', s, count=1)
    out['Z1 - Baseline 09-04 - Inventory'] = s
    for n, src, sup_ in [(2, 'Board 2 - Persona A - New Yorker', '02'), (3, 'Board 3 - Persona B - Back from Europe', '03'), (4, 'Board 4 - Persona C - New User', '04')]:
        s = open(os.path.join(SRC, src + '.dc.html')).read()
        s = s.replace('class="kick">VESPER &middot; HOME &middot; STUDY &middot; ONE PERSONA, FIVE OPENS &middot; FULL SCROLLS &middot; FIXTURE COPY ONLY',
                      f'class="kick">VESPER &middot; HOME &middot; Z{n} &middot; ARCHIVE &middot; BASELINE 09-04 &middot; ONE PERSONA, FIVE OPENS, UNREVISED &middot; SUPERSEDED BY {sup_} &middot; {STAMP}', 1)
        out[f'Z{n} - Baseline 09-04 - ' + src.split(' - ', 1)[1]] = s
    return out

# ───────────────────────────── 00 · Index ─────────────────────────────
def tbl(cols, rows):
    h = ''.join(f'<th style="text-align: left; font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; padding: 6px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.14); vertical-align: bottom;">{c}</th>' for c in cols)
    b = ''.join('<tr>' + ''.join(f'<td style="font-size: 12.5px; line-height: 17px; color: {INK2}; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table style="border-collapse: collapse; width: 100%;"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def blk(t, html): return f'<div style="display: flex; flex-direction: column; gap: 10px;"><div class="shead"><span>{t}</span><span class="rule"></span></div>{html}</div>'

BOARDS = [
    ('01 - Parts', 'Every kind in the 35-kind Home union, as drawn on the current boards; ten cells now lifted from 11; two drawer specimens remain', 'Current &middot; regenerated 09-06', 'reading'),
    ('02 - Persona A - The New Yorker', 'One ordinary week: Sunday and Monday before and after the forms (a sequence, a method, the place inside the contribution, the ticket mark), the floor, the sparse Monday, Thursday before / during / after, the Life record', 'Artifact-led pass &middot; 09-05 &middot; forms PROPOSED', 'reading'),
    ('03 - Persona B - Back from Europe', 'Day zero before and after (a method, the reconstruction strip, the menus comparison); the temporal posture and the dish redrawn in the current direction', 'Artifact-led pass &middot; 09-05 &middot; baseline phones brought current', 'reading'),
    ('04 - Persona C - New User', 'First open before and after (Life&rsquo;s signature as the sample; marks on the capability rows), the sample opened, one contribution, the return with its chip receipt, the next open', 'Artifact-led pass &middot; 09-05 &middot; thin-context check', 'reading'),
    ('05 - Wedge - Trip Forming', 'Group travel on Home: organizer, joiner, and a live day under change', 'Revision 4 &middot; 09-05', 'reading'),
    ('06 - Places - From Friends', 'The friends scope and Place Focus, unchanged; two bounded continuations of Home units on the ground: the Sunday sequence as a route, the cold split as a map', 'Artifact-led pass &middot; 09-05 &middot; two continuations NEW', 'reading'),
    ('07 - Ledger and Decisions', 'Rulings vs history reconciled; the per-form ledger (source, owner, payoff, tap, stable vs live, production class, trigger, fallback, seam); the adoption recommendation; before / after diagnostics; the system, dispositions, production ledger, decision log, the fifteen questions, the history', 'Artifact-led pass &middot; 09-05', 'ledger'),
    ('09 - Forms', 'The selected-form sheet: six forms at standard, compact and expanded or spatial expression; a bare control; the coastline comparison as a form without its research; two phones at 1.3&times; text; reading order for every non-text form', 'Artifact-led pass &middot; 09-05 &middot; PROPOSED', 'seam'),
    ('09 - Forms', 'The selected-form sheet: six forms at standard, compact and expanded or spatial expression; a bare control; the coastline comparison as a form without its research; two phones at 1.3&times; text; reading order for every non-text form', 'Artifact-led pass &middot; 09-05 &middot; PROPOSED', 'seam'),
    ('08 - Seam with Life', 'What Home borrows from Vesper &mdash; Life &amp; Anchors: the pass at L1 in the live window, the admission signature as the sample, the chip for kept receipts, the kind mark on object rows; one flight from the booking email to the gate (booked, the day before, live, flown); the collision (the flight delayed, the group, a decision with a deadline) as the test of the crown ranking; the five-object door map; the seat law and the timeliness clause; row four: rule A vs rule B on the same collision, and the waiting window', 'Ruled 09-05 (pass grammar); crown rule A provisional, rule B compared &middot; DECISION NEEDED', 'seam'),
    ('09 - Forms', 'The selected-form sheet: six forms at standard, compact and expanded or spatial expression; a bare control; the coastline comparison as a form without its research; two phones at 1.3&times; text; reading order for every non-text form', 'Artifact-led pass &middot; 09-05 &middot; PROPOSED', 'seam'),
    ('09 - Forms', 'The selected-form sheet: six forms at standard, compact and expanded or spatial expression; a bare control; the coastline comparison as a form without its research; two phones at 1.3&times; text; reading order for every non-text form', 'Artifact-led pass &middot; 09-05 &middot; PROPOSED', 'seam'),
    ('08 - Seam with Life', 'What Home borrows from Vesper &mdash; Life &amp; Anchors: the pass at L1 in the live window, the admission signature as the sample, the chip for kept receipts, the kind mark on object rows; one flight from the booking email to the gate (booked, the day before, live, flown); the collision (the flight delayed, the group, a decision with a deadline) as the test of the crown ranking; the five-object door map; the seat law and the timeliness clause; row four: rule A vs rule B on the same collision, and the waiting window', 'Ruled 09-05 (pass grammar); crown rule A provisional, rule B compared &middot; DECISION NEEDED', 'seam'),
    ('10 - States', 'Four Home states Home &amp; Places proved that this project had not carried, redrawn on the current pages: withdrawal / narrowing / block; the occasion lived through (a push during, silence after); a kept intention returning; attributed friends', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('11 - Return and Continuity', 'The nine union kinds that had no current drawing (the merged read, the prepared possibility, since-you-looked, the waiting row, the status aperture, the note door, the authorized door, settling, the capability field, the voice horizon), redrawn in the four type roles and placed on a return-after-absence page: Persona B ten days after landing, then the next morning; the region-to-heading mapping written down', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('12 - Why This, Chat, and Degraded States', 'Three affordances Home had no component for: the Why-this door on a consequential unit and its sheet (sources, yours, inferred, not used; four controls); the one Chat aperture per page and the seeded turn; three degraded states drawn as phones: stale, provider unknown, import pending', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('R1&ndash;R4 - Reference', 'Copied from Home &amp; Places (a26e3228) as reference canon: the Home posture matrix; the admission compiler (eleven gates, the precedence chain); the instruments sheet; the grant moment (T2 as one human choice)', 'Reference &middot; 08-31 canon, unrevised', 'reference'),
    ('10 - States', 'Four Home states Home &amp; Places proved that this project had not carried, redrawn on the current pages: withdrawal / narrowing / block; the occasion lived through (a push during, silence after); a kept intention returning; attributed friends', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('11 - Return and Continuity', 'The nine union kinds that had no current drawing (the merged read, the prepared possibility, since-you-looked, the waiting row, the status aperture, the note door, the authorized door, settling, the capability field, the voice horizon), redrawn in the four type roles and placed on a return-after-absence page: Persona B ten days after landing, then the next morning; the region-to-heading mapping written down', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('12 - Why This, Chat, and Degraded States', 'Three affordances Home had no component for: the Why-this door on a consequential unit and its sheet (sources, yours, inferred, not used; four controls); the one Chat aperture per page and the seeded turn; three degraded states drawn as phones: stale, provider unknown, import pending', 'Added 09-06 &middot; PROPOSED', 'seam'),
    ('R1&ndash;R4 - Reference', 'Copied from Home &amp; Places (a26e3228) as reference canon: the Home posture matrix; the admission compiler (eleven gates, the precedence chain); the instruments sheet; the grant moment (T2 as one human choice)', 'Reference &middot; 08-31 canon, unrevised', 'reference'),
    ('Z1&ndash;Z4 - Baseline 09-04', 'The September 4 study as drawn from the accepted parts: the 08-31 inventory and three personas &times; five opens. Never revised; kept because 07 cites them', 'Archive', 'archive'),
]
def index():
    reading = blk('READING ORDER', N('<b>01</b> shows what Home is made of. <b>02&ndash;04</b> show three people&rsquo;s weeks, every phone the current revision, ordered as the days run. <b>05</b> is the wedge, <b>06</b> is where casual sharing went. <b>07</b> holds the system, the rulings, the production ledger, and the history: what each phone replaced, the alternative that lost, the deletion test. <b>08</b> is the seam with the Life project: one ticket at four scales, one flight, the collision, and two priority rules compared. <b>09</b> is the selected-form sheet made after the pages worked: six forms at their scales, a bare control, large-text reflows, reading order. Everything on 09 is proposed, not ruled. <b>10</b> draws the four Home states the older project proved and this one had not carried. <b>11</b> gives the last nine undrawn kinds a page: the return after absence. <b>12</b> draws three affordances no board had: the Why-this sheet, the Chat aperture, and the degraded states. <b>R1&ndash;R4</b> are reference copies of that project&rsquo;s Home canon boards. <b>Z1&ndash;Z4</b> are the September 4 baseline, archived. Nothing on any board is drawn twice.'))
    boards = blk('BOARDS &middot; STATUS', tbl(['BOARD', 'WHAT IT SHOWS', 'STATUS'], [[b, w, s] for b, w, s, _ in BOARDS]))
    fixture = blk('THE FIXTURE WORLD &middot; ONE TABLE &middot; EVERYTHING INVENTED', tbl(['WHO / WHAT', 'ROLE', 'HELD FACTS'], [
        ['Nadia (the account, avatar N)', 'Persona A: the New Yorker in an ordinary week; organizer of the Lisbon trip on 05', 'Friday concert ticket (the hall, doors 8); dentist Tuesday 9:00; harbor book ch. 3&ndash;4 read; a skillet note from Thursday; a coffee route; a saved bakery'],
        ['Dana', 'Friend; lands Saturday the 19th', 'Note &ldquo;keep Sunday morning for me&rdquo;; addressed a used bookshop on Court Street for that Sunday; featured a city-level Status from Sorrento this week'],
        ['Maya', 'Friend', 'Casual share, Friday, friends audience through Sunday: the Sunset Park bakery&rsquo;s sesame loaf, Sundays only, before eleven (a photograph); addressed the noodle bar near the hall for after Friday&rsquo;s show; asked for a kitchen on the Lisbon trip'],
        ['Theo', 'Friend, may-use grant', 'Greenmarket note: &ldquo;bread stall sells out by ten&rdquo;; the market runs Saturdays 8&ndash;1; the joiner on 05'],
        ['Alex', 'Friend; his birthday is Saturday', 'Arrangement forming, 4 going, place open; &ldquo;walkable from the L, not a restaurant&rdquo;; shared Sunset Park as a neighborhood; asked for a free day in Lisbon'],
        ['Persona B (avatar N)', 'Just back from Nice &rarr; Sorrento &rarr; Amalfi &rarr; Rome', 'Dinner with Maya and Alex Saturday 8:15; a refund claim; 412 of 690 photos imported; a Sorrento dish photograph; the ferry morning Sorrento &rarr; Amalfi'],
        ['Persona C (avatar N)', 'A new account that chose New York', 'Nothing held; one ticket after 04 step 3'],
        ['World', 'Fixture weather, tides, rhythms, notices', 'Cold snap Thursday night 28&deg;; low water Saturday 1:40&ndash;4 (Sunday 2:40&ndash;5 on 03); the market peak 9&ndash;11; Open House Oct 17&ndash;18, registration Tuesday noon; the L single-tracking after 11; the Sintra train out until noon on 05'],
    ]))
    ruled = blk('RULED &middot; 2026-09-02 TO 2026-09-05', tbl(['WHEN', 'RULING', 'WHERE IT LIVES'], [
        ['09-02', 'Page-level composition laws (a)&ndash;(i); the hero plate stays', 'kernel &sect;12.7'],
        ['09-04', 'D-H1 (crown only when operational) withdrawn by the founder&rsquo;s review', '07; decision record'],
        ['09-05', 'Containment marks a coherent object (not completion)', 'decision 2026-09-05 &sect;1; kernel &sect;5.1'],
        ['09-05', 'The people region is conditional; holds only what was addressed; the one-relational-opening law is a dominance + demand rule (D-H2, D-H3)', 'decision &sect;2; Home root contract rule 1'],
        ['09-05', 'Four typographic roles replace the two-kicker rule (D-H10)', 'decision &sect;3; kernel &sect;12.7 (c)'],
        ['09-05', 'Four kinds admitted; the Home union is 35', 'decision &sect;4; build manifest &sect;1.6; 01'],
        ['09-05', 'The social split: Home = addressed and shared-consequential; Places = casual sharing as a friends scope on a semantic map; Life People = the record (D-H4 closed)', 'decision &sect;2 (the split); 06'],
        ['09-05', '<b>Artifact-led forms proposed, not ruled:</b> the sequence, the place inside a contribution, paired evidence, the bare method, the reconstruction strip. <b>Decision needed:</b> priority rule A vs B (08 row four); the carded method (&sect;5.1); kind inks in the palette', '02, 03, 04, 06, 09; 07 per-form ledger'],
        ['09-05', '<b>Artifact-led forms proposed, not ruled:</b> the sequence, the place inside a contribution, paired evidence, the bare method, the reconstruction strip. <b>Decision needed:</b> priority rule A vs B (08 row four); the carded method (&sect;5.1); kind inks in the palette', '02, 03, 04, 06, 09; 07 per-form ledger'],
        ['09-05', 'Home borrows Life&rsquo;s pass grammar: the kind mark on object rows; chip lettering as object print; the L1 pass on Home only in its live window; the timeliness clause on the Addressed-to-you region; the seat law cited. <b>Crown arbitration (recovery &gt; live commitment &gt; decision with a deadline &gt; forming arrangement) ruled provisionally on 08 row three</b>', 'decision 2026-09-05-home-borrows-life-pass-grammar; kernel &sect;11.16, &sect;12.7 (g); 08'],
        ['09-05', '<b>Artifact-led forms proposed, not ruled:</b> the sequence, the place inside a contribution, paired evidence, the bare method, the reconstruction strip. <b>Decision needed:</b> priority rule A vs B (08 row four); the carded method (&sect;5.1); kind inks in the palette', '02, 03, 04, 06, 09; 07 per-form ledger'],
        ['09-05', '<b>Artifact-led forms proposed, not ruled:</b> the sequence, the place inside a contribution, paired evidence, the bare method, the reconstruction strip. <b>Decision needed:</b> priority rule A vs B (08 row four); the carded method (&sect;5.1); kind inks in the palette', '02, 03, 04, 06, 09; 07 per-form ledger'],
        ['09-05', 'Home borrows Life&rsquo;s pass grammar: the kind mark on object rows; chip lettering as object print; the L1 pass on Home only in its live window; the timeliness clause on the Addressed-to-you region; the seat law cited. <b>Crown arbitration (recovery &gt; live commitment &gt; decision with a deadline &gt; forming arrangement) ruled provisionally on 08 row three</b>', 'decision 2026-09-05-home-borrows-life-pass-grammar; kernel &sect;11.16, &sect;12.7 (g); 08'],
    ]))
    open_items = blk('OPEN', N('<b>D-H11</b> production classes and cost &mdash; needs an engineering trace, not a design ruling. <b>The crown ranking</b> (kernel &sect;11.16) is ruled provisionally on 08 row three; the founder&rsquo;s read of those three phones confirms or changes the order. <b>Kind inks</b> (the violet admission band) are not yet in Home&rsquo;s kit palette. <b>The crown ranking</b> (kernel &sect;11.16) is ruled provisionally on 08 row three; the founder&rsquo;s read of those three phones confirms or changes the order. <b>Kind inks</b> (the violet admission band) are not yet in Home&rsquo;s kit palette. <b>Persona B</b> phones 2&ndash;3 have the type roles but not the revised composition. <b>The floor</b> on 02 is the honest target for the first internal account; closing the gap is the content-production and owner-read backlog on 07. <b>Large-text renders</b> have not been run. <b>The friends map</b> draws what people made visible, never where they are; the founder&rsquo;s reading of &ldquo;where my friends are&rdquo; is not yet confirmed against that.'))
    outside = blk('WHAT LIVES OUTSIDE THIS PROJECT', N('Canon and rulings: <b>docs/decisions/2026-09-05-amend-home-composition-canon.md</b>, <b>docs/working/design-kernel-extraction-2026-08-29.md</b>, <b>docs/working/home-and-places-build-manifest-2026-08-30.md</b>, <b>travel-app/docs/surfaces/home-root/contract.md</b>. The assignment and its history: <b>docs/working/claude-design-vesper-home-generous-value-handoff-2026-09-04.md</b> and its response doc (revisions 1&ndash;5, then the merge). Implementation status: <b>docs/working/home-and-places-root-implementation-status-2026-09-01.md</b>. The sibling project <b>Vesper - Home &amp; Places</b> (a26e3228) holds the accepted canon boards, the critique passes, and the HP 09-04 value pass; this project does not duplicate them.'))
    inner = (head(f'VESPER &middot; HOME &middot; 00 &middot; INDEX &middot; {STAMP}', 'Vesper &mdash; Home', 'A Home-only design project. Twelve current boards in reading order, four reference boards, &mdash; the parts, three people&rsquo;s weeks, the wedge, Places, the ledger &mdash; and four archived baseline boards. Every phone is drawn once, at its current revision; earlier versions, alternatives, and tests live on 07. Everything on every phone is a fixture.')
             + '<div style="display: flex; flex-direction: column; gap: 34px;">' + reading + boards + fixture + ruled + open_items + outside + '</div>')
    return HEAD + f'<div style="width: 1560px; min-height: {hh("00", 1900)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL

FILES = {
    '00 - Index': index, '01 - Parts': parts, '02 - Persona A - The New Yorker': persona_a, '03 - Persona B - Back from Europe': persona_b,
    '04 - Persona C - New User': persona_c, '05 - Wedge - Trip Forming': wedge, '06 - Places - From Friends': places, '07 - Ledger and Decisions': ledger_board,
}
if __name__ == '__main__':
    for name, fn in FILES.items():
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
    for name, html in archive().items():
        open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
