"""Vesper — Home: the four-board study. Board 1 = the inventory (lifted from the
accepted specimen drawer, regrouped, flagged where a specimen lags a ruled law);
Boards 2–4 = three personas × five full scrolls each, composed with the kit and
lifted from the live boards where a full-scroll state already exists."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
from gen_home import market_crown, PASSAGE_CH3, PASSAGE_CH4, TIDE_SAT, rhythm_bars, live, between

OUT = os.path.join(os.path.dirname(__file__), 'homeproj'); os.makedirs(OUT, exist_ok=True)

# ───────────────────────────── helpers ─────────────────────────────
def extract_div(s, start):
    """Return the balanced <div ...>...</div> beginning at index `start`."""
    i = start; depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        if m.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return s[start:start + m.end()]
        else:
            depth += 1
    raise ValueError('unbalanced')

def lift_phone(name, nth=0):
    s = live(name); idx = -1
    for _ in range(nth + 1):
        idx = s.index('<div style="width: 393px', idx + 1)
    return extract_div(s, idx)

def caption(k, t, s2=''):
    return f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{k}</div><div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div class="fn" style="line-height: 14px;">{s2}</div></div>'

def col(ph, cap):
    ph = re.sub(r'(<div style="width: 393px;[^"]*?)min-height: \d+px;', r'\1min-height: 0;', ph, count=1)
    ph = ph.replace('border-right: 1px dashed rgba(138,102,40,0.35); ', '')
    ph = ph.replace('<circle cx="84" cy="12" r="4.5" fill="#1B1714"/>\n  <text x="94" y="16"', '<circle cx="84" cy="12" r="4.5" fill="#1B1714"/>\n  <text x="98" y="16"')
    return f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;">{cap}{ph}</div>'

def persona_board(title, sub, cols, h):
    head = (f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;">'
            f'<div class="kick">VESPER &middot; HOME &middot; STUDY &middot; ONE PERSONA, FIVE OPENS &middot; FULL SCROLLS &middot; FIXTURE COPY ONLY</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">{title}</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">{sub}</div></div>')
    return (HEAD + f'<div style="width: 2320px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head + '<div style="display: flex; gap: 56px; align-items: flex-start;">' + ''.join(cols) + '</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">EVERY WORLD FACT (TIMES, HOURS, FARES, WEATHER, TIDES, RHYTHMS) IS A FIXTURE INVENTION &middot; PHOTOGRAPH PLATES ARE SLOTS, NEVER FABRICATED IMAGERY &middot; THE SAME SKELETON ON EVERY SCROLL SO RHYTHM IS COMPARABLE</div></div>' + TAIL)

# ───────────────────────────── BOARD 1 · the inventory ─────────────────────────────
REGIONS = [
    ('CHROME AND THE READ', ['world_read', 'root_shell', 'now_merged_into_read']),
    ('NOW · THE DOMINANT UNION (EXACTLY ONE RENDERS)', ['now_commitment_instrument', 'now_prepared_possibility', 'now_decision', 'now_recovery_instrument', 'now_temporal_posture', 'now_annotated_evidence', 'now_attributed_comparison', 'now_invitation']),
    ('IN MOTION', ['motion_occasion_row', 'motion_loose_end_row', 'motion_all_plans_door']),
    ('HORIZONS', ['horizon_editorial_passage', 'horizon_mechanism_row', 'horizon_aperture_row', 'horizon_hidden_system']),
    ('WITH PEOPLE (A RESERVOIR, NOT A CHAPTER)', ['people_note_door', 'people_participants_row', 'people_waiting_row', 'people_authorized_door', 'people_gathering']),
    ('CONTINUITY', ['continuity_reconstruction', 'continuity_capability_field', 'continuity_since_you_looked', 'continuity_life_door', 'continuity_settling', 'continuity_voice_horizon']),
]
LAGS = {
    'now_commitment_instrument': 'crown title still sans 19.5 — ruled serif 22/600 (§12.7 e / A1); instrument missing here',
    'now_prepared_possibility': 'sans title — ruled serif; one instrument per crown',
    'now_decision': 'sans title — ruled serif',
    'now_recovery_instrument': 'tinted box inside the crown — ruled bare line (A6); progress track → arrival span (Urgent v2)',
    'now_temporal_posture': 'sans title — ruled serif; otherwise the cleanest crown in the drawer',
    'now_annotated_evidence': 'plate is a slot (ruled 09-02); callout numerals are the one legend the system allows',
    'now_attributed_comparison': 'two-lane card inside the crown — a container in a crown (A6 family)',
    'now_invitation': 'sans title — ruled serif',
    'motion_occasion_row': '56px row with plate — ruled 44px, plate only for a person (§12.7 g)',
    'motion_loose_end_row': 'icon plate — ruled: status mark, no icon plates (§12.7 g)',
    'horizon_editorial_passage': 'hatch plate stays as a photo slot (founder ruling 09-02)',
    'people_gathering': 'quietPanel card — the one carded people form; facepile ink/umber per A2',
    'continuity_settling': 'carded — a crown by another name; Day-0 dominant, so allowed once',
    'continuity_capability_field': 'gold left rule was stripped 08-31; now kicker-carried',
}

def board1():
    s = live('SpecimenHome.dc.html')
    helmet = between(s, '<helmet>', '</helmet>') + '</helmet>'
    cells = {}
    for m in re.finditer(r'<!-- (\w+)(?: [^>]*)?-->\s*<div class="cell">', s):
        kind = m.group(1)
        if kind in cells: continue
        start = s.index('<div class="cell">', m.start())
        cells[kind] = extract_div(s, start)
    missing = [k for _, ks in REGIONS for k in ks if k not in cells]
    if missing: print('MISSING specimens:', missing)
    body = (f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;">'
            f'<div class="kick">VESPER &middot; HOME &middot; STUDY &middot; BOARD 1 &middot; WHAT HOME IS MADE OF &middot; LIFTED FROM THE ACCEPTED SPECIMEN DRAWER (08-31) &middot; REGROUPED BY REGION</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">Every component, section and card Home can render</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">One specimen per kind, drawn once, at the manifest&rsquo;s names and grades (BUILD &middot; ADAPT &middot; EXISTS). The drawer is shown <b>as it stands</b>; where a specimen lags a law ruled since (the 09-02 critique passes, kernel &sect;12.7), the lag is named in oxblood under the cell so the gap between the parts and the pages is visible. Boards 2&ndash;4 compose these parts into fifteen full scrolls.</div></div>')
    for title, kinds in REGIONS:
        body += f'<div class="shead" style="margin: 26px 0 14px 0;"><span>{title}</span><span class="rule"></span></div>'
        body += '<div class="grid">'
        for k in kinds:
            cell = cells.get(k, f'<div class="cell"><div class="lab"><span class="kn">{k}</span></div><div class="fn">specimen missing from the drawer</div></div>')
            lag = LAGS.get(k)
            if lag:
                cell = cell[:cell.rindex('</div>')] + f'<div class="fn" style="color: {OX}; margin-top: 6px;">LAGS A RULED LAW &middot; {lag.upper()}</div></div>'
            body += cell
        body += '</div>'
    body += (f'<div class="shead" style="margin: 26px 0 14px 0;"><span>THE REST &middot; HOW A PAGE ENDS</span><span class="rule"></span></div><div class="grid">'
             f'<div class="cell"><div class="lab"><span class="kn">rest_close</span><span class="gE">EXISTS</span></div>{coda("That is everything that needs you tonight. The rest keeps.", "NOTHING ELSE WAITS")}<div class="fn">CENTRED SERIF LINE + GHOST STAMP &middot; PAGES END, THEY DO NOT STOP</div></div>'
             f'<div class="cell"><div class="lab"><span class="kn">week_shape (seam)</span><span class="gB">BUILD</span></div>'
             + week_seam([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:D', ''), 'Dana', INK)], top=6).replace('padding: 2px 22px 4px', 'padding: 2px 0 4px')
             + f'<div class="fn">BANDED SEAM, NEVER AN OUTLINED BOX (&sect;12.7 D) &middot; DAY NAMES AT THE 10PX FLOOR</div></div>'
             f'<div class="cell"><div class="lab"><span class="kn">section_header</span><span class="gE">EXISTS</span></div><div style="display: flex; flex-direction: column; gap: 14px; padding: 6px 0;"><div class="shead"><span>IN MOTION</span><span class="rule"></span></div><div class="shead" style="color: {GOLDD};"><span>ONE WAY THE WORLD CAN OPEN</span><span class="rule"></span></div></div><div class="fn">TWO REGISTERS PER SCREEN: MUTE = SECTION &middot; GOLD = UNIT (&sect;12.7 C)</div></div></div>')
    body += f'<div class="fn" style="margin-top: 30px; line-height: 16px;">GRADES AND NAMES: docs/working/home-and-places-build-manifest-2026-08-30.md &middot; SPECIMEN MARKUP LIFTED VERBATIM FROM &ldquo;Specimens - Home&rdquo; &middot; FIXTURE COPY ONLY &middot; MEDIA DOCTRINE: HATCH = POSSIBILITY, PHOTOGRAPH = EVIDENCE</div>'
    doc = ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n' + helmet
           + f'<div style="width: 1240px; min-height: 3300px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + body + '</div>' + TAIL)
    # the drawer's helmet lacks a few kit classes the added cells use
    doc = doc.replace('</style>', '.day { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 8px 0 6px; white-space: nowrap; } .dayl { font-family: JetBrains Mono, ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; } .daym { width: 7px; height: 7px; border-radius: 4px; } .shead { display: flex; align-items: center; gap: 10px; font-family: JetBrains Mono, ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.3px; color: #6E6862; } .shead .rule { flex: 1; height: 1px; background: rgba(27,23,20,0.10); }\n  </style>', 1)
    return doc

# ───────────────────────────── shared units for the personas ─────────────────────────────
def in_motion(rows):
    return section('IN MOTION') + '<div style="padding: 0 22px;">' + ''.join(rows) + '</div>'

def reading_unit():
    return (section('ONE WAY THE WORLD CAN OPEN') + '<div style="padding: 0 22px;">'
            + unit_open('FROM YOUR READING &middot; THE HARBOR BOOK &middot; CH. 3', 'The gates on your coffee route still choose which blocks flood', 'Your usual walk sits in the calm of low water &mdash; nothing to visit, save, or plan.', plate='thumb',
                        plate_label='<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><path d="M8 6 L8 28 L26 28 L26 6 Z" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M12 12 L22 12 M12 16 L22 16 M12 20 L18 20" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>')
            + passage(PASSAGE_CH3[:2], 'THE HARBOR BOOK, CH. 3 &middot; COMPLETE HERE') + '</div>')

# ─── P1 · the New Yorker, ordinary week ───
def p1_planning():
    span = ('<svg width="317" height="96" viewBox="0 0 317 96" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
            '<text x="2" y="11" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">THE NOODLE BAR &#183; WALK-IN</text>'
            '<rect x="2" y="19" width="200" height="12" rx="6" fill="#B0853A"/><circle cx="202" cy="25" r="6" fill="#B0853A"/>'
            '<text x="214" y="29" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">7:15 &#183; 9 MIN</text>'
            '<text x="2" y="52" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE TRATTORIA &#183; NEEDS A TABLE</text>'
            '<rect x="2" y="59" width="260" height="6" rx="3" fill="rgba(27,23,20,0.10)"/><circle cx="262" cy="62" r="5" fill="#EFEAE0" stroke="#6E6862" stroke-width="1.5"/>'
            '<text x="274" y="66" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#6E6862">8:00</text>'
            '<text x="2" y="90" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">FROM WORK</text><text x="315" y="90" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">DANA&#8217;S TRAIN 10:40</text></svg>')
    inner = anchor_row('NEW YORK &middot; WEDNESDAY', '7:20 PM')
    inner += orientation('Dana lands Saturday.<br>One evening to shape.', 'Mild all week &middot; nothing else is asked of you.')
    inner += crown(PLAN, 'SATURDAY WITH DANA &middot; TWO DECISIONS OPEN', 'Dinner is the only thing to decide', 'Where, and whether it needs a table. Sunday morning is already hers.',
                   span, cta='Compare the two', fn='NOTHING BOOKED &middot; DECIDE BY FRIDAY, OR THE WALK-IN DECIDES FOR YOU')
    inner += in_motion([row('Dana &middot; three days out &middot; <span style="color: #6E6862;">&ldquo;keep Sunday morning for me&rdquo;</span>', avatar='D'),
                        row('Dentist Tuesday 9:00 &middot; <span style="color: #6E6862;">nothing to do before it</span>', mark='dashed', last=True)])
    inner += reading_unit()
    inner += coda('One decision, and it can wait until Friday.', 'NOTHING NEEDS YOU TONIGHT')
    return phone(inner, 1560)

def p1_live():
    band = ('<svg width="317" height="46" viewBox="0 0 317 46" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
            '<rect x="2" y="22" width="313" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
            '<rect x="128" y="17" width="92" height="18" rx="9" fill="#B0853A"/><rect x="228" y="22" width="80" height="8" rx="4" fill="rgba(122,46,46,0.45)"/>'
            '<circle cx="104" cy="26" r="5" fill="#1B1714"/>'
            '<text x="128" y="10" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">THE SHOW &#183; 8&#8211;10</text>'
            '<text x="252" y="10" fill="#7A2E2E" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8">+25 HOME</text>'
            '<text x="2" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">5 PM</text><text x="296" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">12</text></svg>')
    inner = anchor_row('NEW YORK &middot; FRIDAY', '6:55 PM')
    inner += orientation_direct('Leave now. The 2 is running normally.', 'Doors at 8 &middot; 28 minutes door to door from your desk.')
    inner += crown(PLAN, 'LIVE &middot; DOORS 8:00 &middot; 65 MIN', 'Walk to the 2 at Wall Street; you arrive by 7:35', 'Coat check yes. Set times not posted &mdash; arriving by 8:40 skips nothing.',
                   band, cta='Open the route', fn='SERVICE READ 6:54 &middot; RE-CHECKS EVERY 5 MIN UNTIL YOU ARRIVE')
    inner += in_motion([row('The way home after ten &middot; <span style="color: #6E6862;">surface route, +25 &middot; decide then</span>', mark='dashed', last=True)])
    inner += coda('Everything else waits until tomorrow.', 'LIVE &middot; THE FIELD YIELDS TO THE ROUTE')
    return phone(inner, 1180)

# ─── P2 · the returned traveler ───
def p2_day0():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '11:20 AM')
    inner += orientation('Home. The trip is settling.', 'Landed 6:40 &middot; photos importing &middot; nothing shared, nothing asked.')
    inner += (f'<div style="margin: 22px 22px 0 22px; background: {CARD}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: 16px; display: flex; gap: 14px; align-items: flex-start;">'
              f'<div class="blob" style="width: 56px; height: 56px; border-radius: 12px; flex: none; background: radial-gradient(90px 70px at 35% 40%, rgba(176,133,58,0.35), transparent 70%), radial-gradient(70px 60px at 72% 68%, rgba(122,46,46,0.13), transparent 70%), #E8E2D4;"></div>'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {MUTE};">SINCE YOU LANDED</div>'
              f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 26px; letter-spacing: -0.2px;">The trip is settling into Life</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">Photos importing &middot; nothing shared &middot; one honest return waiting when it is ready.</div>'
              f'<div class="fn" style="margin-top: 4px;">NO RECAP &middot; NO RATING PROMPT &middot; THE JOURNEY OPENS IN LIFE WHEN IMPORT FINISHES</div></div></div>')
    inner += in_motion([row('Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing &middot; nothing needed from you</span>', mark='dashed'),
                        row('Dinner in Brooklyn &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">with Maya and Alex &middot; settled</span>', avatar='M', last=True)])
    inner += (section('SINCE YOU LAST LOOKED') + '<div style="padding: 0 22px;"><div style="font-size: 14px; line-height: 19px;">Your Rome photos finished importing into Life. Nothing was shared.</div>' + door('Europe, in Life') + '</div>')
    inner += coda('Unpack. New York will keep until you look up.', 'NOTHING NEEDS YOU TODAY')
    return phone(inner, 1260)

def p2_temporal():
    inner = anchor_row('NEW YORK &middot; FRIDAY', '9:05 AM')
    inner += orientation('Saturday stays open.<br>The heat decides at noon.', 'The heat-sensitive branch resolves with the noon forecast.')
    inner += crown(PLAN, 'WAIT FOR SIGNAL &middot; FORECAST AT NOON', 'Wait until noon', 'The waterfront start and the indoor continuation both remain feasible. Neither needs booking before then.',
                   f'<div style="border-top: 1px solid rgba(27,23,20,0.06); padding-top: 10px; margin-top: 6px;"><div class="kickm">IF THE HOTTER BRANCH HOLDS</div><div style="font-size: 14px; line-height: 19px; margin-top: 4px;">Start after 5:30 &middot; shaded approach &middot; indoor continuation near the return</div></div>'
                   f'<div style="{SERIF} font-style: italic; font-size: 16px; line-height: 23px; color: {MUTE}; margin-top: 8px;">I&rsquo;m watching the noon forecast. Unless the branch changes, you won&rsquo;t hear about this again.</div>',
                   cta=None, fn='NEXT CHANGE: FORECAST CHECK AT 12:00 &middot; MONITOR EXPIRES WITH THE WINDOW &middot; NO CTA &mdash; CLOSURE, NOT HOMEWORK')
    inner += (section('THE HIDDEN SYSTEM') + '<div style="padding: 0 22px;">'
              + unit_open('NIGHT DOES NOT COOL EVERY STREET AT THE SAME RATE', 'Water, shade, stored heat and airflow make the same city feel different block by block after sunset', 'Bounded mechanism, source-backed &mdash; it never claims more causal precision than the sources support.', plate='thumb',
                          plate_label='<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><path d="M6 12 H28 M6 18 H24 M6 24 H20" stroke="#8A6628" stroke-width="1.4" stroke-linecap="round"/></svg>')
              + passage(['On a still evening the streets that face the water lose their heat first; the deep cross-streets, walled in masonry, give theirs back for hours. The difference is not the temperature the forecast prints. It is the material under your feet and the air that can or cannot move.'], 'FROM TONIGHT&rsquo;S STORM PASSAGE &middot; KEEPS &middot; NO CLOCK') + '</div>')
    inner += (section('WHAT THE JOURNEY NOW LETS YOU DO') + f'<div style="padding: 0 22px;"><div style="font-size: 14px; line-height: 19px;">Resolve the physical burden first. Let interpretation return only after the route, shade, water and stopping point work.</div><div class="fn" style="margin-top: 6px;">A CAPABILITY RETURN &mdash; IT DOES NOT CLAIM WHAT ROME MEANT TO YOU</div>' + door('Open Saturday in Places') + '</div>')
    inner += coda('Noon will tell you. Until then, nothing.', 'ONE THRESHOLD, THEN SILENCE')
    return phone(inner, 1560)

def p2_evidence():
    plate = ('<div style="margin-top: 8px; height: 190px; border-radius: 12px; background: #2A241E; position: relative; overflow: hidden;">'
             f'<span style="position: absolute; left: 18px; top: 18px; width: 22px; height: 22px; border-radius: 11px; background: {GOLD}; color: {INK}; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center;">1</span>'
             f'<span style="position: absolute; right: 28px; bottom: 52px; width: 22px; height: 22px; border-radius: 11px; background: {GOLD}; color: {INK}; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center;">2</span>'
             f'<div class="fn" style="position: absolute; left: 18px; bottom: 16px; color: #8F877C;">YOUR PHOTOGRAPH &middot; SORRENTO &middot; THE PLATE IS A SLOT</div></div>'
             f'<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 10px;">'
             f'<div style="display: flex; gap: 10px; font-size: 14px; line-height: 19px;"><span class="kick" style="min-width: 12px;">1</span><span>Sauce clings as a thin film rather than pooling.</span></div>'
             f'<div style="display: flex; gap: 10px; font-size: 14px; line-height: 19px;"><span class="kick" style="min-width: 12px;">2</span><span>The finish looks integrated at service, not added afterward.</span></div></div>'
             f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Those cues are consistent with a starch-supported emulsion and pan finishing. They do not prove how this kitchen prepared the dish.</div>')
    inner = anchor_row('NEW YORK &middot; SATURDAY', '10:15 AM')
    inner += orientation('A slow weekend.<br>One question from Sorrento.', 'Clear, 64&deg; &middot; nothing on the calendar until Tuesday.')
    inner += crown(PLAN, 'YOUR PHOTOGRAPH &middot; THE DISH', 'The last minute may explain more than the ingredient list', '', plate, cta=None, fn='YOUR OBSERVATION &middot; ONE SOURCE PER MECHANISM &middot; NOT PROOF OF THIS KITCHEN')
    inner += (f'<div style="padding: 10px 22px 0 22px;">{door("See the evidence and alternatives")}</div>')
    inner += (section('ONE WAY TO TEST THE DISTINCTION IN NEW YORK') + f'<div style="padding: 0 22px;"><div style="font-size: 14px; line-height: 19px;">Compare when the sauce and pasta come together, not only which ingredients are listed. A current nearby possibility makes that process observable this weekend; no reservation is required now.</div>' + door('Open the dish in Places') + '</div>')
    inner += (section('&ldquo;AUTHENTIC&rdquo; IS TOO BLUNT FOR THIS QUESTION') + f'<div style="padding: 0 22px;"><div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK2};">Regional practice, restaurant service, ingredient supply, and New York&rsquo;s own Italian and Italian-American histories can produce different textures without one becoming the universal standard.</div><div class="fn" style="margin-top: 6px;">APPEARS ONLY WITH SOURCES AND POSITIONED PERSPECTIVES &middot; A TECHNIQUE CLAIM NEVER BECOMES CULTURAL SUPERIORITY</div></div>')
    inner += coda('The photo is evidence, not the terminal product.', 'NOTHING NEEDS YOU TODAY')
    return phone(inner, 1600)

# ─── P3 · the new user ───
def p3_cold():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '8:05 AM')
    inner += orientation_direct('Clear and cool. That is all that is known.', 'Nothing has been brought yet. Nothing needs to be.')
    inner += (f'<div style="margin: 22px 22px 0 22px; background: {CARD}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: 16px; display: flex; gap: 14px; align-items: flex-start;">'
              f'<div class="hatch" style="width: 56px; height: 56px; border-radius: 12px; flex: none;"></div>'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 26px; letter-spacing: -0.2px;">Bring something</div>'
              f'<div style="{SERIF} font-size: 16px; line-height: 22px; font-weight: 500; color: {INK2};">A ticket, a place, a photo, a plan &mdash; whatever already has your attention.</div>'
              + door('Start with what you have') + f'<div class="fn">NO SETUP &middot; NO PROFILE &middot; NO QUESTIONS FIRST</div></div></div>')
    inner += coda('Until then, the weather is the whole page. That&rsquo;s honest.', 'NOTHING ELSE IS CLAIMED')
    return phone(inner, 900)

def p3_after():
    inner = anchor_row('NEW YORK &middot; SATURDAY', '9:30 AM')
    inner += orientation_direct('A clear Saturday.', 'Warming to 60&deg; &middot; nothing needs you today.')
    inner += (section('SINCE YOU LAST LOOKED', top=28) + f'<div style="padding: 0 22px;"><div style="font-size: 14px; line-height: 19px;">Friday&rsquo;s ticket is in Life, with the hall and the night. Nothing else was kept.</div>' + door('The show, in Life') + '</div>')
    inner += coda('One good evening is on the board. That&rsquo;s a week.', 'NOTHING NEEDS YOU TODAY')
    return phone(inner, 820)

def p3_reservation():
    band = ('<svg width="317" height="46" viewBox="0 0 317 46" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
            '<rect x="2" y="22" width="313" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
            '<rect x="140" y="17" width="110" height="18" rx="9" fill="#B0853A"/><circle cx="70" cy="26" r="5" fill="#1B1714"/>'
            '<text x="140" y="10" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">TABLE 7:30 &#183; TWO</text>'
            '<text x="2" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">5 PM</text><text x="296" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">10</text></svg>')
    inner = anchor_row('NEW YORK &middot; THURSDAY', '5:40 PM')
    inner += orientation_direct('Tonight&rsquo;s table is at 7:30.', 'From the confirmation you forwarded &middot; light rain until seven.')
    inner += crown(PLAN, 'TONIGHT &middot; YOUR RESERVATION', 'Leave at 7:05; the walk is eleven minutes under awnings', 'The confirmation says 7:30 for two. It does not say the table is still held &mdash; only the restaurant can.',
                   band, cta='Open the walk', fn='FROM THE FORWARDED CONFIRMATION + TONIGHT&rsquo;S FORECAST &middot; VESPER DID NOT BOOK THIS, AND WILL NOT CHANGE IT')
    inner += coda('A table and an umbrella. That&rsquo;s the evening.', 'NOTHING ELSE READ')
    return phone(inner, 980)

def p3_note():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '8:12 PM')
    inner += orientation_direct('Theo sent you a note about the market.', 'It is the first thing anyone has shared with you here.')
    inner += (f'<div style="margin: 22px 22px 0 22px; background: {CARD}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: 16px; display: flex; gap: 12px; align-items: flex-start;">'
              f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; flex: none;">T</span>'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px;"><div class="kickm">THEO &middot; THE SATURDAY MARKET</div>'
              f'<div style="{SERIF} font-size: 18px; line-height: 25px;">&ldquo;The bread stall sells out by ten &mdash; go early or don&rsquo;t bother. The cheese people are fine till noon.&rdquo;</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">The market runs Saturdays 8&ndash;1, nine minutes from you. Vesper has no rhythm for it yet &mdash; his note is the only timing you have.</div>'
              + door('The market, in Places') + f'<div class="fn">AUDIENCE: YOU &middot; USE: YES &middot; NO REPLY OWED &middot; HIS WORDS, KEPT HIS</div></div></div>')
    inner += coda('One note, one place. Nothing to accept.', 'NOTHING NEEDS YOU TONIGHT')
    return phone(inner, 960)

# ───────────────────────────── assemble the persona boards ─────────────────────────────
def board2():
    cols = [col(gh.a1_phone(), caption('OPEN 1 &middot; SATURDAY 8:50', 'Open time', 'AVAILABLE &middot; A PREPARED POSSIBILITY WITH A FRIEND&rsquo;S NOTE, AND A COMPLETE READING')),
            col(gh.a2_phone(), caption('OPEN 2 &middot; THURSDAY 6:40', 'A commitment', 'AVAILABLE &middot; THE FRIDAY TICKET, PREPARED; RELIEF LEADS WITHOUT OPERATIONS')),
            col(p1_planning(), caption('OPEN 3 &middot; WEDNESDAY 7:20', 'One decision open', 'PLANNING &middot; AT MOST ONE UNRESOLVED DECISION; THE FIELD STAYS')),
            col(p1_live(), caption('OPEN 4 &middot; FRIDAY 6:55', 'On the way', 'LIVE &middot; THE COMMITMENT AS A ROUTE; THE FIELD YIELDS')),
            col(gh.a3_phone(), caption('OPEN 5 &middot; SUNDAY 9:10', 'The next open, after nothing was tapped', 'QUIET &middot; VALUE FIRST, ZERO DEMAND'))]
    return persona_board('Persona A &middot; the New Yorker in an ordinary week',
                         'Mature context, no travel: a Friday concert ticket, a Tuesday dentist, Dana arriving next Saturday with one note, the harbor book on the shelf, a coffee route, and Theo&rsquo;s greenmarket note under a grant. Five opens across one week &mdash; open, commitment, planning, live, quiet &mdash; on the same skeleton.', cols, 2010)

def board3():
    sat = lift_phone('HomeSaturday.dc.html')
    urg = lift_phone('HomeUrgentV2.dc.html', 3)
    cols = [col(p2_day0(), caption('OPEN 1 &middot; SUNDAY, LANDED', 'Day zero', 'RETURNED &middot; SETTLING; NEW YORK STAYS FOREGROUND')),
            col(sat, caption('OPEN 2 &middot; FRIDAY 5:12', 'The returned Saturday', 'RETURNED &middot; THE ACCEPTED FLAGSHIP, AS IT STANDS ON THE CANON BOARD')),
            col(urg, caption('OPEN 3 &middot; SUNDAY 7:48, ROME', 'The return, disrupted', 'URGENT &middot; RECOVERY DOMINANT WITH ONE INSTRUMENT (URGENT V2)')),
            col(p2_temporal(), caption('OPEN 4 &middot; FRIDAY 9:05', 'Wait until noon', 'AVAILABLE &middot; A TEMPORAL POSTURE: A CROWN WITH NO CTA')),
            col(p2_evidence(), caption('OPEN 5 &middot; SATURDAY 10:15', 'The dish, as evidence', 'AVAILABLE &middot; ANNOTATED EVIDENCE: PHOTOGRAPHY LEADS'))]
    return persona_board('Persona B &middot; the traveler just back from Europe',
                         'Nice &rarr; Sorrento &rarr; Amalfi &rarr; Rome, now home in New York with Maya and Alex, a refund claim, photographs importing, and one Rome disruption behind them. Five opens: day zero, the returned Saturday, the disrupted return, a heat-driven wait, and a dish photograph. Current life must stay foreground; only material transfer from Europe may appear.', cols, 2280)

def board4():
    thin = lift_phone('C1ThinWeek.dc.html')
    cols = [col(p3_cold(), caption('OPEN 1 &middot; TUESDAY, FIRST OPEN', 'Nothing brought yet', 'COLD &middot; ONE INVITATION, NEVER SETUP HOMEWORK')),
            col(thin, caption('OPEN 2 &middot; WEDNESDAY 7:30', 'One ticket', 'THIN &middot; ONE SUPPLIED OBJECT + WORLD TRUTH = A COMPLETE CROWN')),
            col(p3_after(), caption('OPEN 3 &middot; SATURDAY, AFTER THE SHOW', 'The morning after', 'QUIET, THIN &middot; HONEST ABSENCE, THE TICKET IN LIFE')),
            col(p3_reservation(), caption('OPEN 4 &middot; THURSDAY 5:40', 'A forwarded reservation', 'AVAILABLE &middot; EXTERNAL RESERVATION READ, NEVER BOOKED')),
            col(p3_note(), caption('OPEN 5 &middot; TUESDAY 8:12', 'A friend&rsquo;s note, no history', 'SOCIAL &middot; THE NOTE IS THE ONLY TIMING; NOTHING TO ACCEPT'))]
    return persona_board('Persona C &middot; the new user with almost nothing held',
                         'A first week: no history, no profile, no saved places. What arrives is one object at a time &mdash; nothing, a ticket, the morning after, a forwarded reservation, a friend&rsquo;s note. The test is whether Home is worth opening before Vesper knows the person at all, without turning the first week into homework.', cols, 1140)

if __name__ == '__main__':
    open(os.path.join(OUT, 'Main.dc.html'), 'w').write(board1()); print('wrote Main (board 1)')
    open(os.path.join(OUT, 'PersonaA.dc.html'), 'w').write(board2()); print('wrote PersonaA')
    open(os.path.join(OUT, 'PersonaB.dc.html'), 'w').write(board3()); print('wrote PersonaB')
    open(os.path.join(OUT, 'PersonaC.dc.html'), 'w').write(board4()); print('wrote PersonaC')
