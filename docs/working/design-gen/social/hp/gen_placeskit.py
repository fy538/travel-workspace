"""Vesper — Places (project 516a3ea4): 00 - Index and 01 - Design System.
The design system sheet draws every element the five situations may use, at phone width, graded against code
(EXISTS = a renderer family in travel-app/components/places; ADAPT = drawn on a reference board, not in Places code;
BUILD = Places has no element for it yet). Fixture copy only. Nothing here is ruled."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
import gen_places as gp
import gen_seam as gs
import gen_artifact as ga
from gen_generous import caption, col, head, FOOT, N, arow, facepile, collapsed, span, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, author_row, share_card, reading_card, kept_row
from gen_generous4 import ways_card
from gen_places import scope_header, map_wash, branch, cont_rows, places_phone, ICON_TIDE, ICON_HALL, ICON_MARKET, ICON_BOOK
from gen_merge import tbl, blk, spec, cell
from gen_seam import mark, chip, row_mark, kept_chip_row, G
from gen_artifact import ways_seq_card, handoff_artifact, paired_evidence, method, recon_strip, place_ident

OUT = os.path.join(os.path.dirname(__file__), 'places'); os.makedirs(OUT, exist_ok=True)
STAMP = 'VESPER &middot; PLACES &middot; CREATED 2026-09-07'
HAIR = 'rgba(27,23,20,0.10)'
H = json.load(open(os.path.join(OUT, 'heights.json'))) if os.path.exists(os.path.join(OUT, 'heights.json')) else {}
def hh(k, d=1400): return H[k] if k in H else d

GRID_CSS = ('<style>\n.grid { display: grid; grid-template-columns: repeat(4, 393px); gap: 30px 26px; align-items: start; }\n.cell { display: flex; flex-direction: column; gap: 8px; }\n'
            '.lab { display: flex; align-items: baseline; gap: 8px; border-bottom: 1px solid rgba(27,23,20,0.08); padding: 0 0 4px 0; }\n'
            ".kn { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.6px; color: #6E6862; }\n"
            ".gB, .gA, .gE { font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 9px; font-weight: 700; letter-spacing: 0.8px; margin-left: auto; }\n.gB { color: #7A2E2E; } .gA { color: #8A6628; } .gE { color: #3D7050; }\n</style>")

def sheet(w, h, kick, ttl, sub, body_html, foot=FOOT):
    return (HEAD.replace('</helmet>', GRID_CSS + '</helmet>') + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, ttl, sub) + body_html + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)

def region(t, cells):
    return f'<div class="shead" style="margin: 26px 0 14px 0;"><span>{t}</span><span class="rule"></span></div><div class="grid">' + ''.join(cells) + '</div>'

# ───────────────────────────── A · tokens and type ─────────────────────────────
TOKENS = [('PAPER', PAPER, 'page'), ('CARD', CARD, 'coherent object'), ('WASH', WASH, 'map, reading'), ('INK', INK, 'text, marks'), ('INK2', INK2, 'body'), ('MUTE', MUTE, 'support'),
          ('GHOST', GHOST, 'footnote, anchors'), ('ANCHOR', ANCHOR, 'metadata'), ('GOLD', GOLD, 'instrument, route'), ('GOLDD', GOLDD, 'door, kick'), ('OX', OX, 'live threshold only'), ('UMBER', UMBER, 'you, CTA'), ('PLAN', PLAN, 'water, arrangement'), ('GREEN', GREEN, 'live dot, exists')]
def swatches():
    out = '<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px 14px; padding: 8px 22px 0 22px;">'
    for n, c, r in TOKENS:
        out += (f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 8px; background: {c}; border: 1px solid rgba(27,23,20,0.10); flex: none;"></span>'
                f'<div style="min-width: 0;"><div style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {INK};">{n} <span style="font-weight: 400; color: {ANCHOR};">{c}</span></div><div class="fn" style="color: {MUTE};">{r.upper()}</div></div></div>')
    return out + '</div>'

def type_roles():
    rows = [('THE READ', f'<div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 34px; letter-spacing: -0.3px;">Clear, 64&deg;. Low water at 2:40.</div>', 'SERIF 30/600 &middot; ONE OR TWO LINES &middot; ONLY THE PAGE READ'),
            ('TITLE', f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">Red Hook is slower to enter than the map suggests</div>', 'SERIF 22/600 &middot; A CROWN OR FOCUS TITLE'),
            ('UNIT', title('The pier at low water is the shaded side after two', 17, 22), 'SERIF 17/500 &middot; A BARE UNIT&rsquo;S TITLE'),
            ('ROW', f'<div style="font-size: 15px; line-height: 20px;">Governors Island &middot; <span style="color: {MUTE};">the crossing is the experience</span></div>', 'SANS 15 &middot; A 44PX ROW; THE CLAUSE IN MUTE'),
            ('SUPPORT', sup('The warehouses take the sun off the water walk by 2:30; the return by land is the warm way.'), 'SANS 13/18 MUTE &middot; ENOUGH TO DELIVER THE DISTINCTION'),
            ('VOICE', f'<div style="{SERIF} font-style: italic; font-size: 17px; line-height: 24px; color: {INK2};">Close on a flat map need not mean an easy connection.</div>', 'SERIF ITALIC 17 &middot; VESPER&rsquo;S OWN VOICE, ONE PER PAGE AT MOST'),
            ('KICK / META', '<div class="kick">NEAR THE HARBOR &middot; OPEN SATURDAY</div>' + meta('TIDE TABLE + YOUR SAVED PLACES &middot; FIXTURE', 4), 'MONO 10/700 GOLD-DEEP &middot; MONO 10 ANCHOR &middot; THE 10PX FLOOR'),
            ('OBJECT PRINT', f'<div style="display: flex; gap: 7px;">{chip("ferry", "SOR&rarr;AMALFI")}{chip("dining", "Maya and Alex", "ring", serif=True)}</div>', 'MONO 8.5 / SERIF 11 INSIDE A CHIP OR PASS ONLY &middot; EXEMPT FROM THE FLOOR')]
    out = '<div style="display: flex; flex-direction: column; gap: 14px; padding: 10px 22px 0 22px;">'
    for k, h_, s in rows:
        out += f'<div style="display: flex; flex-direction: column; gap: 4px;"><span class="kickm">{k}</span>{h_}<span class="fn" style="color: {ANCHOR};">{s}</span></div>'
    return out + '</div>'

LAWS = [('ONE LEAD', 'One lead composition at most, then two to four branches, then compact doors. The page ends when the next unit does not beat silence; a first collection may end and offer deliberate widening.'),
        ('THE DOOR', 'A door is gold-deep text and the one arrow. Never a button, never an icon plate, never a chevron on its own line.'),
        ('THE ROW', '44px, one lead per row: a status dot, a facepile when people are the subject, or a kind mark when the subject is a kept object. State stays in the words.'),
        ('CONTAINMENT', 'A card marks a coherent object: a friend&rsquo;s share, a prepared afternoon, an arrangement, a reading. Findings, facts, and techniques stay bare.'),
        ('OXBLOOD', 'The live threshold only: a commitment inside its window whose world changed. Never decoration, never emphasis.'),
        ('MARKS ARE PRINT', 'Kind marks and map marks are one stroke family in ink. Kind inks are illustration ink, never chrome.'),
        ('NO FABRICATED GEOMETRY', 'Nothing is plotted that has no coordinate. City precision is a band below the map; an explanation stays in the field.'),
        ('SILENCE', 'No-supply says what is unavailable in this scope. It never invites, prompts, or claims the world is empty.')]
def laws():
    return '<div style="display: flex; flex-direction: column; gap: 10px; padding: 8px 22px 0 22px;">' + ''.join(
        f'<div style="display: flex; flex-direction: column; gap: 2px;"><span class="kickm">{k}</span><span style="font-size: 12.5px; line-height: 17px; color: {INK2};">{t}</span></div>' for k, t in LAWS) + '</div>'

# ───────────────────────────── B · chrome ─────────────────────────────
def question_control(q='Saturday evening', scope='NEW YORK', friends=False, elsewhere=False):
    pill = lambda t, on=False: (f'<span style="height: 28px; border-radius: 14px; border: 1px solid {"transparent" if on else HAIR}; background: {INK if on else CARD}; color: {CARD if on else INK}; display: inline-flex; align-items: center; padding: 0 12px; font-size: 12.5px; font-weight: 500; white-space: nowrap;">{t}</span>')
    return (f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding: 10px 22px 0 22px; align-items: center;">{pill(q, True)}{pill("From friends", friends)}{pill("Map")}'
            + f'<span class="fn" style="color: {ANCHOR}; margin-left: auto;">CLEAR &rarr; BACK TO {scope}</span></div>')

def scope_row_new(scope='NEW YORK', sub='Selected, not measured &middot; no location asked'):
    return scope_header(scope, sub)

def elsewhere_band():
    return (sect('Elsewhere', top=8) + gut(arow('Dana &middot; Sorrento, this week &middot; <span style="color: #6E6862;">a featured status &middot; city precision &middot; until Saturday</span>', avatars=['D'], last=True)
            + meta('WHAT SHE CHOSE TO SHOW, NOT WHERE SHE IS &middot; NEVER A PIN &middot; A DOORWAY INTO SORRENTO', 8)))

# ───────────────────────────── C · the map grammar ─────────────────────────────
def grammar_map():
    svg = ('<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
           '<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100 L349 240 L0 240 Z" fill="rgba(61,80,102,0.10)"/>'
           '<rect x="200" y="0" width="149" height="90" fill="rgba(176,133,58,0.10)"/><text x="208" y="16" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8A6628">AREA &#183; THE AVENUE SIDE</text>'
           '<circle cx="96" cy="92" r="9" fill="#1B1714"/><text x="92" y="96" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">M</text>'
           '<text x="112" y="88" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE BAKERY</text><text x="112" y="100" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">SHARED &#183; PLACE</text>'
           '<path d="M96 92 Q150 120 196 160" stroke="#B0853A" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
           '<circle cx="196" cy="160" r="6" fill="#B0853A"/><text x="208" y="156" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PIER &#183; 2:40</text><text x="208" y="168" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">LOW WATER TO 5</text>'
           '<circle cx="272" cy="200" r="24" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/><text x="232" y="236" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">SUNSET PARK</text>'
           '<rect x="34" y="28" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M34 33 H46" stroke="#1B1714" stroke-width="1.4"/><text x="52" y="38" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">CANAL HALL &#183; SAT 7 PM</text>'
           '<path d="M120 230 L349 230" stroke="#3D5066" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/><text x="126" y="224" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#3D5066">THE FLOOD LINE &#183; A CLAIM</text>'
           '<circle cx="40" cy="190" r="5" fill="#4A3428"/><text x="50" y="194" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">YOU &#183; ONLY WHEN CHOSEN</text>')
    legend = [('&#9679; avatar', 'A place a person made visible, at place precision', 'RH1 &middot; RS3'),
              ('&#9679; gold', 'A stop in a sequence or route; the gold line is the leg', 'RH1 &middot; RA1'),
              ('dashed circle', 'Neighborhood precision: shared as an area, not a point', 'RH1'),
              ('tinted area', 'A section of the world a finding applies to (the warm side)', 'RH1'),
              ('dated square', 'A dated occurrence at a venue; the venue alone is not the event', 'BUILD'),
              ('dashed line', 'A claim drawn on the ground; labelled as one', 'RH1'),
              ('umber dot', 'You, only with a chosen origin; never inferred', 'RA1'),
              ('no mark', 'City precision, an explanation, a status: below the map, never plotted', 'RH1 &middot; RS5')]
    lg = '<div style="padding: 10px 22px 0 22px; display: flex; flex-direction: column;">' + ''.join(
        f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 6px 0; border-top: 1px solid rgba(27,23,20,0.06);"><span class="kickm" style="width: 96px; flex: none;">{k}</span><span style="font-size: 12.5px; line-height: 17px; color: {INK}; flex: 1;">{t}</span><span class="fn" style="color: {ANCHOR}; flex: none;">{s}</span></div>' for k, t, s in legend) + '</div>'
    return map_wash(240, svg) + lg

# ───────────────────────────── E · new elements Places lacks ─────────────────────────────
def event_stub(kick, venue, when, price, unknown, door_text=None):
    """A dated occurrence: the series and the particular date are distinct; unknowns stay unknown."""
    d = door(door_text) if door_text else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 10px 0; border-top: 1px solid rgba(27,23,20,0.07); border-bottom: 1px solid rgba(27,23,20,0.07);">'
            f'<div style="width: 44px; flex: none; text-align: center; border: 1.4px solid {INK}; border-radius: 8px; padding: 4px 0;"><div style="{MONO} font-size: 9px; font-weight: 700; letter-spacing: 0.8px; color: {MUTE};">{kick.split()[0]}</div><div style="{SERIF} font-size: 20px; line-height: 22px; font-weight: 600; color: {INK};">{kick.split()[1]}</div></div>'
            f'<div style="flex: 1; min-width: 0;">{title(venue, 16, 21, 600)}<div style="font-size: 13px; line-height: 18px; color: {INK2}; margin-top: 2px;">{when} &middot; {price}</div><div class="fn" style="color: {ANCHOR}; margin-top: 4px;">{unknown}</div>{d}</div></div>')

def composed_possibility():
    return ways_seq_card('An exhibition, then dinner near it', [('4:30', '<i>Rooms Remade</i> at the Harbor Print Room', 'Through Sunday; one room before and after reuse.', 'HOURS SUPPORT 4:30 &middot; TICKETS UNKNOWN'),
                                                               ('7:15', 'A table three blocks on', 'Two places fit; neither needs a card tonight.', '')],
                         meta_t='SUGGESTED BY VESPER &middot; NOT AN ADVERTISED EVENT, NOT AN ARRANGEMENT &middot; EXPLORE THE PARTS OR PROPOSE IT')

def pin_peek():
    return (f'<div style="background: {CARD}; border-radius: 14px; box-shadow: 0 6px 18px rgba(27,23,20,0.12); padding: 12px 14px; display: flex; gap: 12px; align-items: center;">'
            f'<div class="hatch" style="width: 44px; height: 44px; border-radius: 10px; flex: none;"></div><div style="flex: 1; min-width: 0;">{title("The Harbor Print Room", 16, 20, 600)}<div class="fn" style="color: {ANCHOR}; margin-top: 2px;">RED HOOK &middot; 18 MIN &middot; EXHIBITION THROUGH SUNDAY</div></div>{door("Open")}</div>')

def area_card():
    return card(title('Red Hook', 20, 25, 600) + sup('Harbor first, a scheduled way in, a flexible way out. Slower to enter than the map distance suggests.', INK2)
                + f'<div style="margin-top: 10px;">{compare2("ON THE MAP", "18 min", "as the crow flies", "GETTING IN", "~40", "ferry or the bus")}</div>'
                + meta('AN AREA, NOT A POINT &middot; OUTLINE ON THE MAP &middot; FIXTURE', 8) + door('Explore Red Hook'))

def withdrawn_line():
    return (f'<div style="padding: 8px 0; border-top: 1px solid rgba(27,23,20,0.06); border-bottom: 1px solid rgba(27,23,20,0.06);"><span style="font-size: 13px; line-height: 18px; color: {MUTE};">Maya took back her note about the Print Room. What it changed here is gone; the venue and its exhibition are still listed on their own.</span></div>'
            + meta('LOCAL UPDATE &middot; THE REST OF THE COLLECTION STANDS &middot; THE SHARE DOES NOT RETURN', 6))

def no_supply():
    return (f'<div style="padding: 20px 12px 6px 12px; text-align: center;"><div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2};">Nothing from friends about Red Hook yet.</div><div class="fn" style="color: {ANCHOR}; margin-top: 6px;">THIS SCOPE ONLY &middot; THE WORLD IS NOT EMPTY</div></div>'
            + f'<div style="display: flex; gap: 18px; justify-content: center; padding-top: 10px;">{door("Back to all of Red Hook")}</div>')

def stale_fact():
    return fact('HOURS &middot; AS OF THREE WEEKS AGO', 'Tuesday to Sunday, 11&ndash;6. Not checked since; the description stands, the &ldquo;open now&rdquo; claim does not.', last=True)

def thin_end():
    return (f'<div style="padding: 16px 0 0 0;"><div class="fn" style="color: {ANCHOR};">THE FIRST COLLECTION ENDS HERE &middot; SEVEN THINGS</div>'
            + '<div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Widen to the waterfront') + door('Another time: Sunday') + door('Follow the exhibition') + '</div></div>')

def comparison_triplet():
    """for me → with Maya → around the dinner: same world facts, changed ordering; a lens grants nothing."""
    lanes = [('FOR ME', ['The Print Room, 4:30', 'The listening hour, 7', 'The pier at low water']), ('WITH MAYA', ['The Print Room, 4:30 &middot; <span style="color: #6E6862;">her note</span>', 'The pier at low water', 'The listening hour, 7']), ('AROUND SATURDAY&rsquo;S DINNER', ['The listening hour, 7 &middot; <span style="color: #6E6862;">ends by 9</span>', 'The Print Room, 4:30', '<span style="color: #B5AFA5;">The pier: too far from the table</span>'])]
    out = '<div style="display: flex; gap: 10px;">'
    for k, items in lanes:
        out += f'<div style="flex: 1; min-width: 0;"><div class="kickm" style="margin-bottom: 6px;">{k}</div>' + ''.join(f'<div style="font-size: 12.5px; line-height: 17px; color: {INK}; padding: 5px 0; border-top: 1px solid rgba(27,23,20,0.06);">{t}</div>' for t in items) + '</div>'
    return out + '</div>' + meta('SAME FACTS, DIFFERENT ORDER &middot; CHOOSING A LENS SENDS NOTHING AND ADOPTS NOTHING', 8)

# ───────────────────────────── the sheet ─────────────────────────────
def design_system():
    A = [cell('tokens', 'EXISTS', spec(swatches()), 'FROM kit.py AND RA8 CANON TOKENS &middot; ONE PALETTE ACROSS ROOTS'),
         cell('type roles', 'EXISTS &middot; RULING', spec(type_roles()), 'FOUR ROLES (DECISION 2026-09-05 &sect;3) + THE READ AND THE VOICE &middot; THE 10PX FLOOR; OBJECT PRINT EXEMPT'),
         cell('laws carried in', 'RULING', spec(laws()), 'KERNEL &sect;11&ndash;&sect;12.7 AND THE 09-05 AMENDMENTS &middot; THE LAST TWO ARE PROPOSED FOR PLACES'),
         cell('the phone', 'EXISTS', spec(places_phone(scope_header('NEW YORK', 'Saturday &middot; 2&ndash;8 PM open') + gut(f'<div style="height: 120px; border-radius: 12px; background: {WASH};"></div>', top=14) + f'<div style="height: 24px;"></div>', 0)), 'THE FRAME EVERY SITUATION USES &middot; 393 WIDE &middot; PLACES ACTIVE IN THE FOUR-ROOT BAR')]
    B = [cell('scope handle', 'EXISTS', spec(scope_header('NEW YORK', 'Saturday &middot; 2&ndash;8 PM open') + scope_header('RED HOOK', 'Inside New York &middot; the harbor side', back=True) + scope_header('RED HOOK &middot; NOW', 'You are here &middot; 40 min before dinner', back=True, live='LIVE &middot; 6:10')), 'RA1&ndash;RA4 &middot; THE SCOPE, ITS SUB-LINE, SEARCH AND MAP &middot; LIVE ONLY INSIDE A WINDOW'),
         cell('question and scope control', 'BUILD', spec(scope_header('NEW YORK', 'Selected, not measured &middot; no location asked') + question_control() + question_control('Sorrento &middot; before arrival', 'NEW YORK', elsewhere=True).replace('CLEAR &rarr; BACK TO NEW YORK', 'ORIGIN UNSET &middot; NO &ldquo;NEAR YOU&rdquo;')), 'BRIEF &sect;6.1 &middot; THE QUESTION IS VISIBLE AND EDITABLE; FROM FRIENDS IS A SCOPE, NOT A MODE; CLEARING RETURNS TO THE PARENT'),
         cell('the map', 'EXISTS &middot; ADAPT', spec(grammar_map()), 'RH1, RS3, RS5, RA1 &middot; ONE ENCODING AT EVERY SCALE &middot; THE DATED SQUARE IS NEW'),
         cell('elsewhere band', 'ADAPT', spec(elsewhere_band()), 'RH1 &middot; CITY PRECISION LIVES BELOW THE MAP &middot; A DOORWAY INTO ANOTHER SCOPE')]
    C = [cell('rows', 'EXISTS', spec(gut(row('The Sunset Park bakery &middot; <span style="color: #6E6862;">saved &middot; not yet visited</span>', mark='hollow') + row('Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', mark='dashed') + row('Open House registration &middot; <span style="color: #6E6862;">Tuesday noon</span>', mark='dot') + row_mark('admission', 'The show &middot; Friday, doors 8') + arow('Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled</span>', avatars=['M', 'A'], last=True), top=8)), 'ONE LEAD PER ROW: DOT (EPHEMERAL), HOLLOW (SAVED), DASHED (PENDING), KIND MARK (KEPT OBJECT), FACEPILE (PEOPLE) &middot; CODE: candidate ROWS'),
         cell('branches', 'EXISTS', spec(gut(branch(ICON_TIDE, 'Red Hook', 'Harbor first &middot; scheduled way in', 'flexible way out') + branch(ICON_HALL, 'Brooklyn Bridge Park', 'Continuous land access', 'easiest to shorten') + branch(ICON_MARKET, 'Governors Island', 'The crossing is the experience', 'the return is least flexible', ghost=True), top=8)), 'RA1 &middot; TWO TO FOUR MEANINGFULLY DIFFERENT PATHS, EACH WITH ITS REASON AND BURDEN &middot; THE HATCHED PLATE IS A SLOT'),
         cell('doors and the fold', 'EXISTS', spec(gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Explore Red Hook') + door('Ask Vesper about the pier') + door('Back to Saturday, at Home', MUTE) + '</div>' + '<div style="height: 18px;"></div>' + collapsed('THE REST &middot; STILL HERE', ['The listening hour at Canal Hall', 'The market, Saturday morning']) + '<div style="height: 18px;"></div>' + cont_rows([('Saved in New York', '12'), ('Places you have been', '')]).replace('padding: 32px 22px 0 22px', 'padding: 0'), top=8)), 'THE DOOR LAW &middot; THE FOLD WHILE SOMETHING LEADS &middot; CONTINUITY ROWS WITH AN HONEST COUNT'),
         cell('facts, stale facts, no supply', 'EXISTS &middot; ADAPT', spec(gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon.') + stale_fact() + '</div>' + no_supply(), top=8)), 'A CITY FACT IS A ROW (code: notice) &middot; STALE KEEPS THE DESCRIPTION, DROPS THE CLAIM &middot; NO-SUPPLY NAMES THE SCOPE')]
    D = [cell('share card', 'EXISTS', spec(gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY', 'The side room was my favorite.', 150, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'THE HARBOR PRINT ROOM &middot; RED HOOK &middot; 18 MIN', 'The Print Room'), top=8)), 'RH1, RA13 &middot; THE ORIGINAL PHOTOGRAPH AND WORDS ARE THE WHOLE VALUE; ENRICHMENT ONLY WHEN IT ADDS &middot; CODE: social'),
         cell('contribution with its place', 'ADAPT', spec(gut(handoff_artifact('D', 'Dana', 'TUESDAY &middot; TO YOU', 'Keep Sunday morning for me; the bookshop on Court Street, then anywhere.', 'dining', 'The bookshop on Court Street', 'CARROLL GARDENS &middot; OPENS 10 &middot; A NOTE, NOT A PLAN', 'The bookshop'), top=8)), 'RH2 FORM 3 &middot; THE PLACE IDENTITY STRIP INSIDE THE UNIT &middot; ADDRESSED MATERIAL LANDS ON HOME; PLACES SHOWS IT AT ITS PLACE'),
         cell('pin peek', 'EXISTS', spec(gut(pin_peek() + '<div style="height: 14px;"></div>' + area_card(), top=8)), 'PlacesPinPeekCard &middot; ONE LINE AND A DOOR OVER THE MAP &middot; THE AREA CARD (BUILD) IS ITS NEIGHBORHOOD-SCALE SIBLING'),
         cell('event stub', 'BUILD', spec(gut('<div>' + event_stub('SAT 13', 'The listening hour at Canal Hall', 'Saturday 7&ndash;9 PM', 'admission $12', 'TICKETS UNKNOWN &middot; THE VENUE ALONE IS NOT THE EVENT', 'This Saturday&rsquo;s hour') + '<div style="height: 10px;"></div>' + event_stub('SAT 13', 'The Saturday market', 'Next occurrence this Saturday, 8&ndash;1', 'a series', 'LATER DATES NOT CONFIRMED &middot; SERIES &ne; OCCURRENCE') + '</div>', top=8)), 'BRIEF &sect;6.3 &middot; THE DATE IS THE LEAD; THE SERIES AND THE OCCURRENCE ARE DISTINCT OBJECTS &middot; NO RENDERER YET')]
    E = [cell('alternatives and the sequence', 'ADAPT', spec(gut(ways_card('This afternoon', [('The pier at low water', 'Low water 2:40 to 5; the shaded side after two.', 'LOW WATER 2:40&ndash;5'), ('The Print Room, then the water', 'The exhibition closes at six; the pier is nine minutes on.', 'TICKETS UNKNOWN')], 'TIDE TABLE + YOUR SAVED PLACES &middot; NOTHING BOOKED'), top=8)), 'RA11, RH2 FORM 2 &middot; UNNUMBERED, &ldquo;OR&rdquo; HAIRLINES &middot; MAY LEAD A QUIET OPEN &middot; CODE: experience'),
         cell('composed possibility', 'BUILD', spec(gut(composed_possibility(), top=8)), 'BRIEF &sect;6.3 &middot; A SEQUENCE VESPER COMPOSED, SAID SO &middot; EXPLORE THE PARTS, ADJUST, OR PROPOSE; NEVER AN EVENT'),
         cell('bare finding and paired evidence', 'EXISTS &middot; ADAPT', spec(gut(u2('Thursday night the river side runs four degrees colder than the avenue', 'Open water and wind keep the waterfront blocks from holding the day&rsquo;s heat.', compare2('RIVER SIDE &middot; 9 PM', '24&deg;', 'wind off the water', 'THE AVENUE &middot; 9 PM', '28&deg;', 'masonry holds the day'), meta_t='TWO STATIONS + FORECAST &middot; FIXTURE') + '<div style="height: 22px;"></div>' + paired_evidence('One room, before and after reuse', 'The enclosed room opens into shared space; the diagram shows what changed.', [('BEFORE &middot; 1962', 'A corridor and four closed rooms', 'PLAN'), ('AFTER &middot; 2024', 'One room, the wall now a threshold', 'PLAN')], meta_t='REUSABLE COMPARISON &middot; NOT ABOUT YOU &middot; W5'), top=8)), 'RA12, RH2 FORMS 4 &middot; FINDINGS STAY BARE &middot; CODE: PlacesSemanticUnitCard / editorial'),
         cell('reading and the record', 'EXISTS', spec(gut(reading_card('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', 'The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes.', 'Read the chapter') + '<div style="height: 18px;"></div>' + recon_strip([('9:10', 'ferry', 'TICKET', ''), ('9:14', 'photo', 'HARBOR', 'NOTHING KEPT'), ('10:02', 'photo', 'THE QUAY', '')], t='Sorrento to Amalfi by ferry, as you left it', text='A ticket and two photographs; the gap stays a gap.', meta_t='LIFE OWNS THIS &middot; PLACES SHOWS IT AT THE PLACE, ONCE', door_text='In Life'), top=8)), 'CODE: editorial, memory &middot; A READING IS OPTIONAL DEPTH BEHIND A DOOR &middot; THE RECORD IS LIFE&rsquo;S, SHOWN HERE AT ITS PLACE')]
    F = [cell('chips, marks, receipts', 'EXISTS &middot; RULING', spec(gut(f'<div style="display: flex; gap: 7px; flex-wrap: wrap;">{chip("admission", "THE HALL &middot; FRI")}{chip("flight", "FCO&rarr;JFK", "ring")}{chip("ferry", "SOR&rarr;AMALFI", "unused")}{chip("dining", "Maya and Alex", "live", serif=True)}</div>'
                                                                        + f'<div style="display: flex; gap: 14px 18px; margin-top: 16px; align-items: center; flex-wrap: wrap;">' + ''.join(f'<span style="display: inline-flex; align-items: center; gap: 6px;">{mark(k, 18, 0.8)}<span class="fn" style="color: {MUTE};">{k.upper()}</span></span>' for k in G) + '</div>'
                                                                        + '<div style="margin-top: 16px;">' + kept_chip_row('dining', 'The Print Room', 'saved, in Life') + '</div>', top=8)), 'DECISION 2026-09-05 (PASS GRAMMAR) &middot; RING = UPCOMING, GREEN = LIVE, GREY = UNUSED &middot; SEVEN KINDS DRAWN; A PLACE KIND IS NEEDED'),
         cell('withdrawn share', 'BUILD', spec(gut(withdrawn_line(), top=8)), 'BRIEF &sect;4 VARIATION &middot; AN HONEST LINE, THEN THE INDEPENDENT WORLD FACTS STAND &middot; NEVER RESURRECTED'),
         cell('the comparison triplet', 'ADAPT', spec(gut(comparison_triplet(), top=8)), 'RA15, RA16 &middot; FOR ME &rarr; WITH MAYA &rarr; AROUND THE DINNER &middot; NOT A SIXTH MODE, NOT A SCOPE TOOLBAR'),
         cell('the first collection ends', 'BUILD', spec(gut(thin_end(), top=8)), 'BRIEF &sect;3 &middot; A FINITE FIRST COLLECTION, THEN DELIBERATE WIDENING &middot; NO RECYCLED MATERIAL, NO INVITE')]
    body_html = region('A &middot; TOKENS, TYPE, LAWS, THE FRAME', A) + region('B &middot; CHROME: SCOPE, QUESTION, MAP, ELSEWHERE', B) + region('C &middot; ROWS, BRANCHES, DOORS, FACTS', C) + region('D &middot; CARDS: SHARES, CONTRIBUTIONS, PEEKS, EVENTS', D) + region('E &middot; UNITS: ALTERNATIVES, COMPOSED, EVIDENCE, READING', E) + region('F &middot; OBJECT PRINT, WITHDRAWAL, LENSES, ENDINGS', F)
    families = [['candidate', 'PlacesFeedCardView &middot; candidateCard', 'rows, branches, pin peek'], ['editorial', 'editorialCard, editorialFeedCard', 'reading card, bare finding, paired evidence'], ['experience', 'experienceCard', 'alternatives, the sequence, composed possibility'],
                ['memory', 'memoryCard', 'the record at its place (reconstruction strip), kept chip row'], ['notice', 'noticePromptCard', 'fact row, stale fact, no-supply line'], ['social', 'socialCard (FriendFeedCard)', 'share card, contribution with its place, elsewhere band'],
                ['semantic unit', 'PlacesSemanticUnitCard', 'bare finding, comparison triplet'], ['map', 'PlacesMapCanvas, PlacesPinPeekCard, PlaceAreaMap', 'the map grammar, pin peek, area card'], ['none yet', '&mdash;', 'question control, event stub, composed possibility, withdrawn line, the collection&rsquo;s end']]
    sources = [['RA1&ndash;RA4', 'Field &rarr; Focus &rarr; Path &rarr; Live Reduction: the states, branches with burdens, the scope handle', 'Its booking, authority and old UI assumptions'],
               ['RA5&ndash;RA10', 'Canon: ordinary open, social anatomy (four admissible forms), degradation, tokens, instruments, specimens', 'That the sparse ordinary-open canvas is the whole old design'],
               ['RA11&ndash;RA14', 'HP 09-04: an open afternoon, curiosity complete without visiting, a friend note as evidence, the relation sheet', 'D2/D3/D6 were ruled; they are pending'],
               ['RA15&ndash;RA16', 'For me / with someone / around an occasion; a practical change inside an exploration', 'Identical inventory across lenses; the MP4 booking story'],
               ['RS1&ndash;RS5', 'Pin languages, four provenances on one map, the map in the app, Sorrento from people', 'Pins as the universal social object; friends rank first; a prompt on every save'],
               ['RH1&ndash;RH3', 'From friends as a scope on a semantic map; the six forms; the 35-kind Home union', 'That Home&rsquo;s regions or crown apply to Places'],
               ['RE1&ndash;RE4', 'The object page: the law, the page, five doors from one place, useful edges', 'That Places redraws the entity page; it opens it'],
               ['RL1&ndash;RL2', 'People records with attribution and withdrawal; a map inside a record', 'That Life is a present-tense feed; that every received item is retained']]
    body_html += ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">'
                  f'<div style="width: 760px; flex: none;">{blk("CODE FAMILIES &middot; travel-app/components/places", tbl(["FAMILY", "RENDERER", "KIT ELEMENTS IT SHOULD CARRY"], families))}</div>'
                  f'<div style="width: 850px; flex: none;">{blk("WHAT EACH REFERENCE BOARD LENDS", tbl(["SOURCE BOARDS (KEPT HERE: RA1, RA6, RA15, RS3, RH1, RE2)", "REUSE", "DO NOT ASSUME"], sources))}</div></div>')
    return sheet(1720, hh('01', 5200), f'{STAMP} &middot; 01 &middot; DESIGN SYSTEM &middot; THE ELEMENTS THE FIVE SITUATIONS MAY USE', '01 &middot; The Places kit',
                 'Every element at phone width, graded against code: EXISTS is a renderer family in the Places workspace today; ADAPT is drawn on a reference board and not yet in Places code; BUILD is an element Places has no form for. Six new elements are proposed here for the brief&rsquo;s five situations: the question control, the dated event stub, the composed possibility, the area card, the withdrawn line, and the collection&rsquo;s end. Fixture copy only.', body_html)

# ───────────────────────────── 00 · index ─────────────────────────────
def index():
    assignment = blk('THE ASSIGNMENT', N('<b>Home brings forward what matters in my life. Places lets me explore what the world could offer &mdash; from here, somewhere else, or through my people.</b> Design one complete, current Places experience: world discovery, personal relevance, human perspectives, practical help. Social is part of it, not its purpose. Reward both &ldquo;I know what I am looking for&rdquo; and &ldquo;show me something worth encountering&rdquo;; deliver value without history, a friend network, map manipulation, or a dossier per candidate. This is completion and rebalancing of the Field &rarr; Focus &rarr; Path grammar, not a new product grammar. Source: <b>docs/working/places-complete-experience-design-handoff-2026-09-07.md</b>.'))
    situations = blk('FIVE SITUATIONS &middot; ONE COMPOSITION FAMILY', tbl(['', 'SITUATION', 'IT MUST ANSWER', 'BOARD', 'STATUS'], [
        ['A', 'Ordinary New York opening; no query, no history, no shares', 'What can I enjoy, understand or consider without supplying more input?', '02', 'Drawn 09-07 &middot; PROPOSED'],
        ['B', 'Purposeful: &ldquo;something Saturday evening&rdquo;', 'How do search, time, comparison, relevance and practical uncertainty work together?', '03', 'Drawn 09-07 &middot; PROPOSED'],
        ['C', 'Through my people: sparse and dense, nearby and elsewhere', 'Can I enjoy ordinary sharing, find an absent friend&rsquo;s perspective, and explore beyond friends without pressure?', '04', 'Drawn 09-07 &middot; PROPOSED'],
        ['D', 'Another city before arrival: Sorrento from New York', 'Can I explore without pretending I am there or granting location?', '05', 'Drawn 09-07 &middot; PROPOSED'],
        ['E', 'Taking a possibility forward, and the for me / with Maya / around the dinner triplet', 'Can I open, compare, ask, keep, share or propose, then return to the same exploration?', '06', 'Drawn 09-07 &middot; PROPOSED'],
        ['', 'The supply-rich opening and its deliberate widening', 'Does abundance come from reuse and selection, not bespoke generation per row?', '07', 'Drawn 09-07 &middot; PROPOSED'],
        ['', 'Decisions, reuse inventory, receiving contract, canon deltas', 'What is proposed, what is reused, what is a canon change, what engineering still owes', '08', 'Drawn 09-07 &middot; PROPOSED']]))
    budget = blk('THE BOARD BUDGET', N('Seven situation boards and one decisions board, then stop. Each situation board shows the full scroll, its map form, one detail opening, one continuation and its return; variations (no location, thin supply, a withdrawn share, stale facts) are drawn inside those boards as phones, never as a screen catalogue. The comparison that settles the map&rsquo;s initial prominence uses the same evidence on both sides.'))
    fixture = blk('THE FIXTURE WORLD &middot; ONE DECISION TAKEN, FLAGGED', N('The brief supplied a fresh packet (W1&ndash;W5, H1, H2). Every other current board runs on the shared fixture world: Maya&rsquo;s Sunset Park bakery share, the pier at low water, the Saturday greenmarket, Dana&rsquo;s city-level Sorrento status, Alex&rsquo;s Saturday, Theo&rsquo;s may-use note. Situations C, D and E cross into Home and Life, so this project maps the packet onto that world rather than starting a second one: <b>W3 is the greenmarket; H1 is Maya; H2 is Dana&rsquo;s existing Sorrento status.</b> W1 (the Harbor Print Room and <i>Rooms Remade</i>), W2 (the listening hour at Canal Hall), W4 (the waterside candidate), and W5 (the room comparison) enter the shared world as new venues. Everything is synthetic; no live availability is invented. <b>If you would rather keep the packet separate, say so before 02 is drawn.</b>'))
    decisions = blk('DECISIONS THIS LANE RESOLVES', tbl(['', 'QUESTION', 'THE BASELINE TO PRESSURE-TEST (BRIEF &sect;6.1)'], [
        ['1', 'Default composition: what makes a no-query opening worthwhile; how purpose changes prominence', 'Content-led field with an immediately available map; lead with something worth understanding; no mandatory crown'],
        ['2', 'Spatial interaction: when map, list, area and route help', 'Map and field share one result set; panning is inspection until a deliberate change; never refresh on a toggle'],
        ['3', 'Content forms: which objects deserve a card, row, comparison or detail', 'Pins are one spatial expression; events, routes, areas and non-spatial material differ (see 01)'],
        ['4', 'Social receiving without a button wall', 'Original material first; enrichment only when it adds; Ask Vesper and Reply to Maya are distinguishable; no reply is a complete ending'],
        ['5', 'Continuation: which owner handles each action; what survives the return', 'Open the existing entity, event, reading or route destination; return to the same exploration; flag thin-guest and pre-Plan gaps']]))
    refs = blk('REFERENCE BOARDS &middot; SIX KEPT FROM FIVE PROJECTS &middot; PRECEDENT, NOT ADOPTION', tbl(['KEPT', 'SOURCE PROJECT', 'WHAT IT LENDS'], [
        ['RA1 World Field', 'Vesper - Home &amp; Places (a26e3228)', 'The state grammar: scope handle, spatial field, lead, finite branches with burdens, continuity doors'],
        ['RA6 Canon Places Social Anatomy', 'Vesper - Home &amp; Places', 'The four admissible social forms and the admission tests'],
        ['RA15 MP3 Scope Comparison', 'Vesper - Home &amp; Places', 'For me / with someone / around an occasion on one world'],
        ['RS3 Pin Languages', 'Vesper - Social Aperture (fac2051b)', 'How a shared mark reads at each precision; what a pin must never claim'],
        ['RH1 Places From Friends', 'Vesper &mdash; Home (42876b8c)', 'The friends scope on a semantic map; the Elsewhere band'],
        ['RE2 The Page', 'Vesper &mdash; Entity Object Handoff Lab (dd48304b)', 'The object page Places opens into and does not redraw']])
        + N('Twenty-four further copies (the rest of Places 1&ndash;4, the canon and specimen boards, HP B1&ndash;B6, MP4, the other Social Aperture, Home, Entity and Life boards) were removed on 09-07 to keep this project legible; 01 distils what they lent, and they remain in their source projects.'))
    complete = blk('COMPLETION TEST', N('A newcomer can enjoy a worthwhile Places visit; an experienced person can encounter the world through their own life and other people; either can take something forward without losing context or acquiring homework. Reject a reskinned section feed, an obligatory cultural essay, or a friends map standing in for the complete product.'))
    outside = blk('WHAT LIVES OUTSIDE THIS PROJECT', N('The brief: <b>docs/working/places-complete-experience-design-handoff-2026-09-07.md</b>. The anatomy: <b>places-consumer-experience-anatomy-2026-08-29.md</b>. The result-set contract: <b>places-result-set-context-contract-2026-09-05.md</b>. The entity program: <b>entity-object-design-overhaul-plan-2026-09-07.md</b>. The social split: <b>docs/decisions/2026-09-05-amend-home-composition-canon.md &sect;2</b>. Code: <b>travel-app/components/places</b> (PlacesWorkspace, PlacesRootExperience, PlacesFeedCardView, renderers/). One canon delta the brief carries and this project will name on 08: a finite first collection with deliberate widening replaces &ldquo;this is all of it today&rdquo; as a ceiling.'))
    inner = (head(f'{STAMP} &middot; 00 &middot; INDEX', 'Vesper &mdash; Places', 'A focused investigation: one complete Places experience across five situations, drawn with the shared kit and six reference boards kept from the five projects it descends from. 01 is the design system; 02&ndash;06 are the five situations, 07 the richness check, 08 the decisions board, all drawn 2026-09-07 and all proposed; R-boards are copied precedent. Everything on every phone is a fixture.')
             + '<div style="display: flex; flex-direction: column; gap: 34px;">' + assignment + situations + budget + fixture + decisions + refs + complete + outside + '</div>')
    return HEAD + f'<div style="width: 1560px; min-height: {hh("00", 2400)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL

FILES = {'00 - Index': index, '01 - Design System': design_system}
if __name__ == '__main__':
    for name, fn in FILES.items():
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
