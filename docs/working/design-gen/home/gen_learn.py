"""15 - Learning and Steering (2026-09-09 second pass): two experience comparisons.
Row one: learnable breadth without an input tax (04 / 14 / 12 / 09).
Row two: steering desired help over time, scoped to the request (Home leads; Places receives).
Usage: python3 gen_learn.py <polished_dir> <out_dir>
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
G = '/Users/feihuyan/travel-workspace/docs/working/design-gen/home/gen_trip.py'
src = open(G).read().split("# ---- board edits")[0]
sys.argv = ['x', IN, OUT]; exec(src.replace("LIVE, OUT = sys.argv[1], sys.argv[2]\nos.makedirs(OUT, exist_ok=True)", "LIVE, OUT = sys.argv[1], sys.argv[2]"))
def h03(): return open(f'{IN}/03 - Persona B - Back from Europe.dc.html').read()
H02 = open(f'{IN}/02 - Persona A - The New Yorker.dc.html').read()
H04 = open(f'{IN}/04 - Persona C - New User.dc.html').read()
CAPTION = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;"
def phone_regions(h):
    out = []
    for m in re.finditer(r'<div style="width: 393px;[^"]*background: #EFEAE0', h):
        s = m.start(); depth = 0
        for mm in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0: out.append(h[s:s + mm.end()]); break
    return out
def element_around(h, marker, must=('radius',)):
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
FIRST_OPEN_04 = phone_regions(H04)[0]
H08B = open(f'{IN}/08b - Seam with Life - Home to Life.dc.html').read()
def piece_phone():
    i = H08B.find('Volcanic ash from the Campi Flegrei'); s0 = H08B.rfind('<div style="width: 393px;', 0, i); depth = 0
    for m in re.finditer(r'<div\b|</div>', H08B[s0:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0: return H08B[s0:s0 + m.end()]
    raise SystemExit('piece not found on 08b')
PIECE_FULL = piece_phone()
def piece_inner():
    """The piece's own content, without its phone shell, so it can be re-shelled with an instruction beneath."""
    inner = PIECE_FULL[PIECE_FULL.index('>') + 1:]
    cut = inner.rfind('<div style="border-top: 1px solid rgba(27,23,20,0.10);')   # the four-root bar
    grow = inner.rfind('<div style="flex-grow: 1;"></div>', 0, cut)
    return inner[:grow if grow > 0 else cut]
COAST_UNIT = element_around(H02, 'Sorrento&rsquo;s cliff is volcanic', must=('flex-direction: column',))
def phone(inner): return phone_open() + inner + '<div style="flex-grow: 1;"></div>' + tabbar() + '</div>'
def unit(title, body='', source='', extra=''):
    return (f'<div style="display: flex; flex-direction: column;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK}; text-wrap: balance;">{title}</div>'
            + (f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">{body}</div>' if body else '') + extra + (fn(source, 6) if source else '') + '</div>')
def fact(kick, text, muted=False, last=True):
    return (f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 10px 0; border-top: 1px solid {HAIR};{" border-bottom: 1px solid " + HAIR + ";" if last else ""}"><span class="fn" style="color: {HINT};">{kick}</span>'
            f'<span style="font-size: 14px; line-height: 19px; color: {MUTE if muted else INK};">{text}</span></div>')
def sample_block():
    return (f'<div style="background: {CARD}; border-radius: 16px; padding: 14px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
            f'<div style="display: flex; align-items: center; gap: 9px;"><span style="font-family: {MONO}; font-size: 9px; font-weight: 700; letter-spacing: 1px; color: {HINT}; border: 1px dashed {HINT}; border-radius: 10px; padding: 2px 7px; flex: none;">SAMPLE</span>'
            f'<span class="fn" style="color: {HINT};">A MADE-UP TICKET, READ THE WAY YOURS WOULD BE</span></div>'
            f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; margin-top: 8px;">Doors at 8. Arrive by 8:40 and you miss nothing.</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">After ten the way home from the hall is a surface route: 25 minutes longer.</div>'
            + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 8px;">{door("How it&rsquo;s read")}{door("Try with yours")}</div></div>')
def seam(days, line):
    out = '<div style="margin: 40px 0 0 0; border-top: 1px solid rgba(27,23,20,0.10); border-bottom: 1px solid rgba(27,23,20,0.06); padding: 2px 22px 4px;"><div style="display: flex;">'
    for lab, kind, text in days:
        if kind == 'today': m, lc, tc = f'<span class="daym" style="background: {INK};"></span>', INK, INK
        elif kind == 'gold': m, lc, tc = f'<span class="daym" style="background: {GOLD};"></span>', INK, INK
        else: m, lc, tc, text = '<span class="daym" style="border: 1px solid rgba(27,23,20,0.15); box-sizing: border-box;"></span>', HINT, 'transparent', '.'
        out += f'<div class="day"><span class="dayl" style="color: {lc};">{lab}</span>{m}<span style="font-size: 10px; color: {tc};">{text}</span></div>'
    return out + '</div></div>' + f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="font-family: {SERIF}; font-size: 17px; line-height: 24px; color: {INK};">{line}</div></div>'
TUE_SEAM = seam([('TUE', 'today', 'today'), ('WED', 'h', ''), ('THU', 'gold', 'registration'), ('FRI', 'h', ''), ('SAT', 'h', ''), ('SUN', 'h', ''), ('MON', 'h', '')], 'Registration closes Thursday.')
OHNY = fact('OPEN HOUSE &middot; OCT 17&ndash;18 &middot; OHNY', 'Timed sites: registration opens today at noon and closes Thursday. Walk-in sites need none.', last=False)
LNOTE = fact('THE L &middot; AFTER 11 PM, MON&ndash;THU', 'Single-tracking between Bedford and 1st; daytime is normal.')
BOOK = element_around(H02, 'THE HARBOR BOOK &middot; CH. 4')
def taught_by_sample():
    inner = anchor('NEW YORK &middot; TUESDAY', '8:05 AM') + read('Registration for the Open House timed sites opens today at noon.', 'Walk-in sites need none &middot; clear and cool &middot; low water on the pier Saturday from 2:40.')
    inner += gut(OHNY + LNOTE, top=22)
    inner += sect('Worth reading') + gut(BOOK)
    inner += sect('What one thing turns into') + gut(sample_block())
    inner += TUE_SEAM
    return phone(inner)
def taught_by_control():
    inner = anchor('NEW YORK &middot; TUESDAY', '8:05 AM') + read('Registration for the Open House timed sites opens today at noon.', 'Walk-in sites need none &middot; clear and cool &middot; low water on the pier Saturday from 2:40.')
    inner += gut(OHNY + LNOTE, top=22)
    inner += gut(door('The walk-in sites, in Places'), top=4)
    inner += sect('Worth reading') + gut(BOOK)
    inner += gut(f'<div class="fn" style="color: {HINT}; line-height: 15px;">A TICKET OR A MENU YOU ALREADY HAVE IS READ THE SAME WAY, IN CHAT</div>', top=26)
    inner += TUE_SEAM
    return phone(inner)
def opened_piece():
    """15.4 — the real opened piece from 08b, exactly as it is drawn there."""
    return PIECE_FULL
def spoken(text):
    return (f'<div style="display: flex; justify-content: flex-end; padding: 2px 0 10px 0;"><span style="background: #2A241E; color: {CARD}; border-radius: 16px 16px 4px 16px; padding: 9px 13px; font-size: 13.5px; line-height: 19px; max-width: 290px;">{text}</span></div>')
def piece_long():
    """15.5 — the same piece, in full, with the instruction spoken on it."""
    return phone(piece_inner() + gut(spoken('I like this subject, but this is too long.'), top=14))
def lane_row(kick, title, body, last=False):
    b = '' if last else f' border-bottom: 1px solid {HAIR};'
    return (f'<div style="padding: 10px 0;{b}"><div class="fn" style="color: {HINT};">{kick}</div>'
            f'<div style="font-family: {SERIF}; font-size: 16px; line-height: 21px; font-weight: 500; color: {INK}; margin-top: 3px;">{title}</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">{body}</div></div>')
def piece_head(kick_right):
    circ = lambda inner: f'<span style="width: 32px; height: 32px; border-radius: 16px; border: 1px solid rgba(27,23,20,0.14); display: inline-flex; align-items: center; justify-content: center; background: {CARD};">{inner}</span>'
    back = circ('<svg width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M8.5 2.5L4 6.5L8.5 10.5" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return (f'<div style="padding: 20px 22px 0 22px; display: flex; align-items: center; justify-content: space-between;">{back}'
            f'<span class="fn" style="color: {HINT};">{kick_right}</span></div>')
def sources_block(compact=True):
    line = ('De Pippo et al., &ldquo;Application of a method to assess coastal hazard: the cliffs of the Sorrento Peninsula and Capri&rdquo;, '
            'Geol. Soc. London Spec. Publ. 322 (2009) &middot; your photographs of Aug 16 and 21 &middot; reference photographs, Wikimedia Commons.')
    head = (f'<div style="display: flex; align-items: baseline; gap: 10px; border-top: 1px solid {HAIR}; padding-top: 10px;">'
            f'<span class="fn" style="color: {INK}; font-weight: 700;">SOURCES</span><span class="fn" style="color: {HINT}; margin-left: auto;">1 PAPER &middot; 2 PHOTOGRAPHS &middot; 2 REFERENCES</span></div>')
    body = '' if compact else f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">{line}</div>'
    return head + body + door('Open the sources')
def piece_short():
    """15.6 — the same piece, shortened: the useful point and the sources stay."""
    inner = piece_head('THE PIECE &middot; SHORTER')
    inner += gut(f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 26px; line-height: 31px; text-wrap: balance;">The same coast, two rocks</div>'
                 + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 6px;">Sorrento stands on ash; Amalfi on limestone.</div>', top=18)
    inner += gut(lane_row('SORRENTO &middot; TUFF', 'A flat top, a wall, a shallow shelf', 'Volcanic ash from the Campi Flegrei, now soft rock.')
                 + lane_row('AMALFI &middot; LIMESTONE', 'No shelf: a slope into deep water', 'The Lattari&rsquo;s older limestone; the towns climb it.', last=True), top=14)
    inner += gut(f'<div style="background: {CARD}; border-radius: 16px; padding: 14px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                 f'<div class="fn" style="color: {HINT};">HOW TO TELL WHICH YOU ARE ON</div>'
                 f'<div style="font-family: {SERIF}; font-size: 16px; line-height: 22px; color: {INK}; margin-top: 6px;">A flat-topped wall with shallow water below it: the ash. A road hanging on a slope above deep water: the limestone.</div></div>', top=16)
    inner += gut(sources_block(compact=True), top=18)
    inner += gut(door('The full piece, with the photographs'), top=2)
    return phone(inner)
def later_full():
    """15.7 — a clearly related piece, same subject and sources, at ordinary depth."""
    inner = piece_head('THE PIECE &middot; SUNDAY')
    inner += gut(f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 26px; line-height: 31px; text-wrap: balance;">Why the towns past Punta Campanella climb instead of sitting</div>'
                 + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 6px;">The same coast you walked in August, from the other end of it.</div>', top=18)
    inner += gut(f'<div style="font-size: 14px; line-height: 21px; color: {INK2};">Where the peninsula is ash, the rock gives a flat top and a shallow shelf, and a town can spread on it: Sorrento sits on that shelf edge with its piers below. Past Punta Campanella the Lattari&rsquo;s Mesozoic limestone and dolomite take over, hard and folded, rising to 1,444 m at Monte San Michele. There is no flat to sit on and no shelf to build a pier on, so the towns go up the slope instead, in terraces, with the sea starting deep at the foot of them.</div>'
                 + f'<div style="font-size: 14px; line-height: 21px; color: {INK2}; margin-top: 10px;">It is the same reason the water changes colour as you go round: the shelf that holds the light at Sorrento simply is not there once the limestone starts.</div>', top=16)
    inner += gut(f'<div style="background: {CARD}; border-radius: 16px; padding: 14px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07);">'
                 f'<div class="fn" style="color: {HINT};">ON YOUR AUG 21 PHOTOGRAPH</div>'
                 f'<div style="font-family: {SERIF}; font-size: 16px; line-height: 22px; color: {INK}; margin-top: 6px;">The houses stand on the terraces, not on a shelf; that is the limestone doing it.</div></div>', top=16)
    inner += gut(sources_block(compact=False), top=18)
    return phone(inner)
def not_become():
    return (f'<div style="background: {CARD}; border-radius: 16px; padding: 16px; box-shadow: 0 1px 2px rgba(27,23,20,0.05), 0 5px 14px rgba(27,23,20,0.07); width: 393px; box-sizing: border-box;">'
            f'<div class="fn" style="color: {HINT};">WHAT THE INSTRUCTION DID NOT BECOME</div>'
            f'<div style="font-family: {SERIF}; font-size: 20px; line-height: 25px; font-weight: 600; margin-top: 6px;">A shorter piece, not a smaller subject</div>'
            f'<div style="font-size: 13.5px; line-height: 19px; color: {INK2}; margin-top: 8px;">Not a topic rejection: the same coast arrives again on Sunday at full length, with its full sources. Not a global mode: nothing else on Home got shorter. Not a preference: nothing was written about the person, and no setting changed. The full piece stayed one door away the whole time.</div>'
            f'<div class="fn" style="color: {HINT}; margin-top: 10px;">PRESENT-REQUEST SCOPE &middot; A PERSISTENT PREFERENCE WOULD BELONG TO THE PREFERENCE/CONTINUITY OWNER AND STAYS PROPOSED</div></div>')
def colf(ph, shead, kick, title, fnt):
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;"><div class="shead" style="color: {GOLDD}; margin-bottom: 10px;"><span>{shead}</span><span class="rule"></span></div>'
            f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{kick}</div><div style="font-family: {SERIF}; font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{title}</div><div style="{CAPTION}">{fnt}</div></div>{ph}</div>')
def rowdiv(kick, title, sub, first=False):
    return (f'<div style="{"margin-top: 0;" if first else "margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);"} display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">{kick}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">{title}</div><div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 1100px;">{sub}</div></div>')
row1 = [colf(FIRST_OPEN_04, '04 &middot; FIRST OPEN &middot; AS DRAWN', '15.1 &middot; THE DONOR', 'What 04 teaches: bring one thing', '04&rsquo;s newcomer learns that a ticket, a menu or a photograph becomes a usable reading. The teaching is excellent and the sample is honest; the risk is that the best receiving position reads as a request for an upload.'),
        colf(taught_by_sample(), 'TUESDAY 8:05 &middot; MATCHED CONTENT &middot; TAUGHT BY DEMONSTRATION', '15.2 &middot; THE SAMPLE AS TEACHER', 'The same page, with the sample', 'The alternative, kept. The bounded set from 14 with 04&rsquo;s sample under its own heading: another supported use is unmistakable and the page still ends, but the two doors both point at giving something, which is what a first open can afford and an ordinary one need not.'),
        colf(taught_by_control(), 'TUESDAY 8:05 &middot; MATCHED CONTENT &middot; TAUGHT BY AN ORDINARY CONTROL &middot; SELECTED', '15.3 &middot; THE CONTROL AS TEACHER &middot; SELECTED', 'The same page, no sample', 'Selected. The same items; another supported use is recognisable from the doors already on the page &mdash; the walk-in list in Places, the chapter &mdash; and one quiet line naming what Chat does with something the person already has. Learnability arrives through the value on the page rather than through a demonstration, and nothing implies an upload. 15.2 stays as the alternative for a first open where nothing else is yet worth opening; both endings are finished.'),
        colf(opened_piece(), 'THE OPENED PIECE, AS 08b DRAWS IT &middot; THE SECONDARY QUESTION', '15.4 &middot; ASK, WITHOUT THE PROVENANCE SHEET', 'One aperture on the object', 'The piece exactly as 08b row five already draws it: &ldquo;Ask about this&rdquo; sits beside &ldquo;Save this piece&rdquo; on the object itself. Corrects 12, where a secondary question had to go through &ldquo;Why this&rdquo;, a door meant for consequential units. Editorial &sect;11 allows one prominent aperture; the question carries the piece and its sources into the existing Chat, with no provenance sheet and no upload first. No Chat layout is redesigned, and 12&rsquo;s inspect sheet keeps its own job.')]
row2 = [colf(piece_long(), 'THURSDAY 8:10 &middot; THE PIECE IN FULL, AS 08b DRAWS IT', '15.5 &middot; BEFORE', 'The whole piece, then the instruction', 'The actual opened piece: the headline, both photographs with their captions, the two paragraphs of rock, how to tell which you are on, and the source list. The instruction is spoken on the piece itself, in the person&rsquo;s words &mdash; no questionnaire, no setting, no profile.'),
        colf(piece_short(), 'THURSDAY 8:11 &middot; THE SAME PIECE, SHORTENED', '15.6 &middot; AFTER', 'The same piece, shorter', 'The same piece, shorter: the two rocks as a pair of lines, &ldquo;how to tell which you are on&rdquo; kept word for word because it is the useful point, and the sources kept with their door. What went: the two paragraphs and the photographs, one door away. Roughly 150 words to 60, with the point and the sources intact.'),
        colf(later_full(), 'SUNDAY &middot; THREE DAYS LATER &middot; THE SAME COAST', '15.7 &middot; THE LATER ENCOUNTER', 'A related piece, at ordinary depth', 'The strong control: the same subject, sources and rock, from the other end of the coast. It arrives whole because Thursday&rsquo;s instruction was about that piece, and a loosely related topic would not have tested that. <b>Its value, assessed on its own:</b> 15.5 answers what the two cliffs are made of; this answers why the built form differs &mdash; terraces instead of a shelf and piers &mdash; and lands on the person&rsquo;s own Aug 21 photograph, so it is a second question about one subject rather than the first one repeated. A reappearance that only restated the tuff-and-limestone distinction would not have earned the slot, and no quota required this one.'),
        colf(not_become(), 'CHECK', '15.8 &middot; WHAT IT DID NOT BECOME', 'A shorter piece, not a smaller subject', 'The three things a local instruction must not turn into, stated as a check: a topic rejection, a global mode, or a written preference. Persistent or cross-session steering stays proposed under the preference/continuity owner; Places receives the same scoped result rather than a second mechanism.')]
head = H02[:H02.find('<div style="width: 2')]
board = (f'<div style="width: 1820px; min-height: 5000px; background: #F4F0E7; box-sizing: border-box; padding: 40px 44px 60px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">'
         f'<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 26px;"><div class="kick">VESPER &middot; HOME &middot; 15 &middot; LEARNING AND STEERING &middot; SECOND PASS &middot; 2026-09-09</div>'
         f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">15 &middot; Two experience comparisons: learning what else Home can do, and steering what it gives</div>'
         f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 1100px;">Not a component inventory. Row one asks whether a person can receive value and recognise another supported use without feeling they owe an upload or a next action, using matched content and ordinary controls; it ends with the secondary-question route that 12 currently sends through &ldquo;Why this&rdquo;. Row two extends one existing subject through a spoken instruction, its useful result, and a later encounter that shows the instruction did not become a preference. PROPOSED compositions; donors are named on each frame.</div></div>'
         + rowdiv('ROW ONE &middot; LEARNABLE BREADTH WITHOUT AN INPUT TAX &middot; 04 / 14 / 12 / 09', 'Another supported use, recognised without being asked for anything', 'The same Tuesday content taught two ways, then the question route. Finished endings are preserved in both; no capability curriculum is added.', first=True)
         + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row1) + '</div>'
         + rowdiv('ROW TWO &middot; STEERING DESIRED HELP OVER TIME &middot; HOME LEADS, PLACES RECEIVES', 'A local instruction changes this result, not the subject and not the person', 'One subject across three encounters, then the check. Present-request scope only; persistent alternatives remain proposed under the actual owner.')
         + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>' + '</div>')
open(f'{OUT}/15 - Learning and Steering.dc.html', 'w').write(head + board + '</x-dc></body></html>'); print('15 written')
