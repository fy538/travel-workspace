"""05 - D · Sorrento before arrival: a deliberate switch of scope with no origin; the vertical distinction leads because
orientation is the job; Dana's city-level status in the friends expression; the quay walk opened; the return to Sorrento."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, author_row
from gen_places import scope_header, map_wash, branch, places_phone
from gen_merge import tbl, daycap, page
from gen_placeskit import question_control, STAMP, hh, OUT
from gen_places02 import notecol

def qc(q='Sorrento &middot; before arrival', tail='ORIGIN UNSET &middot; NO &ldquo;NEAR YOU&rdquo; &middot; NO TRIP REQUIRED', friends=False):
    return question_control(q, 'SORRENTO', friends=friends).replace('CLEAR &rarr; BACK TO SORRENTO', tail)

def plan_svg(h=200):
    return ('<rect x="0" y="0" width="349" height="' + str(h) + '" fill="rgba(42,56,75,0.06)"/>'
            f'<path d="M0 {h-70} Q80 {h-90} 160 {h-60} Q250 {h-30} 349 {h-50} L349 {h} L0 {h} Z" fill="rgba(61,80,102,0.14)"/><path d="M0 {h-70} Q80 {h-90} 160 {h-60} Q250 {h-30} 349 {h-50}" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
            '<circle cx="150" cy="62" r="7" fill="#1B1714"/><text x="162" y="58" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE READING ROOM</text><text x="162" y="70" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">UPPER TOWN &#183; S1</text>'
            f'<circle cx="176" cy="{h-58}" r="6" fill="#B0853A"/><text x="188" y="{h-62}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE QUAY WALK</text><text x="188" y="{h-50}" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">LOWER QUAY &#183; S2</text>'
            f'<path d="M150 69 L176 {h-64}" stroke="#1B1714" stroke-width="1" stroke-dasharray="3 3" opacity="0.5"/><text x="60" y="{h-96}" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">~180 M IN PLAN</text>'
            f'<text x="12" y="{h-10}" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">PLAN VIEW &#183; SCHEMATIC &#183; NOT SURVEYED</text>')

def section_svg():
    return ('<rect x="0" y="0" width="349" height="150" fill="rgba(176,133,58,0.06)"/>'
            '<path d="M0 118 L120 118 L120 40 L349 40" stroke="#1B1714" stroke-width="1.6" fill="none"/><path d="M0 118 L120 118 L120 40 L349 40 L349 150 L0 150 Z" fill="rgba(27,23,20,0.06)"/>'
            '<path d="M0 126 Q40 122 90 126 L120 126" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
            '<circle cx="200" cy="38" r="6" fill="#1B1714"/><text x="212" y="20" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE READING ROOM</text><text x="212" y="32" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">ABOUT +40 M</text>'
            '<circle cx="70" cy="112" r="6" fill="#B0853A"/><text x="14" y="104" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE QUAY WALK</text><text x="14" y="140" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">SEA LEVEL</text>'
            '<path d="M120 46 L120 112" stroke="#7A2E2E" stroke-width="1.4" stroke-dasharray="2 3"/><text x="128" y="84" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#7A2E2E">THE CONNECTION: NOT VERIFIED</text>'
            '<text x="128" y="96" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">STEPS? A LIFT? A ROAD? UNKNOWN</text>'
            '<text x="226" y="140" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">SECTION &#183; SCHEMATIC</text>')

def lead():
    return u2('Close on the map, far apart on the ground', 'The reading room sits in the upper town, about forty metres above the quay walk. In plan they are a few minutes apart; how you get between them is not known here: no verified steps, lift, or road, and no time.',
              map_wash(150, section_svg(), top=10).replace('margin: 10px 22px 0 22px', 'margin: 10px 0 0 0'), meta_t='S3 &middot; SCHEMATIC, LABELLED AS ONE &middot; THE PAYOFF IS THE VERTICAL RELATIONSHIP, NOT A ROUTE PROMISE')

def two_places():
    return ('<div>' + branch('<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M5 4 H17 V18 H5 Z" stroke="#8A6628" stroke-width="1.4"/><path d="M8 8 H14 M8 11 H14 M8 14 H12" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>', 'The reading room, upper town', 'A small reading room with an exhibition preview', 'hours not known &middot; steps to the door: not known')
            + branch('<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M3 14 Q7 10 11 14 Q15 18 19 14" stroke="#8A6628" stroke-width="1.4" stroke-linecap="round"/><path d="M3 9 Q7 5 11 9 Q15 13 19 9" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>', 'The quay walk, lower town', 'A public walk along the water at sea level', 'step-free along the quay itself &middot; the way down: not known') + '</div>'
            + meta('KNOWN ACCESS CHARACTERISTICS ONLY &middot; NO ARRIVAL DATE, NO BOOKING, NO LOCATION PRESUMED', 8))

def widening():
    return ('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('The upper town') + door('The other side of the harbor') + door('Another time of day') + '</div>'
            + meta('AREA AND TIME, WITHOUT A TRIP &middot; THE SCOPE STAYS SORRENTO UNTIL YOU CHANGE IT', 8))

def field_phone(return_strip=False):
    inner = scope_header('SORRENTO', 'Selected from New York &middot; no origin set &middot; before any visit')
    if return_strip:
        inner += f'<div style="margin: 10px 22px 0 22px; padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">BACK &middot; TO SORRENTO, NOT TO NEW YORK &middot; SAME POSITION</span></div>'
    inner += qc()
    inner += map_wash(200, plan_svg(200), top=14)
    inner += gut(lead(), top=22)
    inner += sect('Two places, what is known') + gut(two_places())
    inner += gut(widening(), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">ORIENTATION IS THE JOB, SO THE MAP EARNS THE FIRST VIEWPORT HERE &middot; ROUTE-FROM-HERE NEEDS A CHOSEN ORIGIN</div></div>'
    return places_phone(inner, 0)

def friends_phone():
    inner = scope_header('SORRENTO &middot; FROM FRIENDS', 'What one person made visible, at city precision') + qc(tail='BACK TO ALL OF SORRENTO', friends=True)
    inner += gut(author_row('D', 'Dana', 'THIS WEEK &middot; A FEATURED STATUS &middot; CITY PRECISION') + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">&ldquo;We spent the late afternoon by the water.&rdquo;</div>'
                 + meta('HER PAST AFTERNOON, IN HER WORDS &middot; NOT ADVICE ABOUT CURRENT CONDITIONS &middot; NOT A SPOT, NOT A PIN', 8), top=22)
    inner += gut(u2('Where &ldquo;by the water&rdquo; could mean', 'Sorrento&rsquo;s water is at the quay, forty metres below the upper town. That is a fact about the town, not about where Dana was.', meta_t='THE ONLY ENRICHMENT: A TOWN FACT &middot; NOTHING INFERRED ABOUT HER'), top=26)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 10px;">' + door('Reply to Dana') + meta('TO DANA &middot; NOT SENT UNTIL YOU SEND IT', 0) + door('All of Sorrento') + '</div>', top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">ONE STATUS &middot; THE SCOPE ENDS &middot; BROADER EXPLORATION DOES NOT NEED HER</div></div>'
    return places_phone(inner, 0)

def quay_phone():
    inner = scope_header('THE QUAY WALK', 'Sorrento &middot; lower town &middot; a public walk', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">A walk along the water at sea level, below the town.</div>' + sup('Step-free along the quay itself. How you reach it from the upper town is not known here.', INK2), top=22)
    inner += sect('What is known, and not') + gut('<div>' + fact('LEVEL', 'Sea level; the town above is about forty metres up. The connection between them is not verified.') + fact('HOURS', 'A public space; no hours are listed and none are assumed.') + fact('THE WAY THERE', 'Route-from-here needs a chosen origin. None is set, and none is inferred.', last=True) + '</div>')
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Ask Vesper about the quay') + door('Keep', INK) + '</div>', top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">A SUPPORTED PLACE, OPENED &middot; BACK RETURNS TO SORRENTO</div></div>'
    return places_phone(inner, 0)

def board():
    row1 = [col(field_phone(), daycap('FRIDAY 12:26 PM &middot; SCOPE: SORRENTO', '1 &middot; THE VERTICAL DISTINCTION LEADS', 'Plan view, then the section: close on the map, far apart on the ground', 'ORIGIN UNSET &middot; NO &ldquo;NEAR YOU&rdquo; &middot; NO TRIP &middot; THE SCHEMATIC SAYS IT IS ONE')),
            col(friends_phone(), daycap('SORRENTO &middot; FROM FRIENDS', '2 &middot; DANA, AT CITY PRECISION', 'Her past afternoon in her words; one town fact; no pin', 'NOT RELABELLED AS ADVICE &middot; NOT A SPOT &middot; BROADER EXPLORATION STANDS WITHOUT HER')),
            col(quay_phone(), daycap('THE QUAY WALK OPENED', '3 &middot; A SUPPORTED PLACE', 'Level, hours, the way there: known or said unknown', 'ROUTE-FROM-HERE NEEDS A REAL CHOSEN ORIGIN &middot; NOTHING PRESUMED ABOUT ARRIVAL')),
            notecol('Exploring another city without pretending to be there', [
                ('1 &middot; VALUE BEFORE ACTION', N('One spatial fact a flat map hides: the two places are minutes apart in plan and forty metres apart in height, and the connection is not known. Understanding that is the payoff, and it is complete without an arrival date, a booking, or a route.')),
                ('2 &middot; WHY THIS LEAD, WHY THIS ASSORTMENT', N('Orientation is the job in a city one has not visited, so the map and the section earn the first viewport here, which they did not on 02. The two places are presented with the access characteristics that are known and nothing more. Dana&rsquo;s status appears only in the friends expression, in her words, as her past afternoon.')),
                ('3 &middot; WHAT THE MAP ADDS, WHAT IT CANNOT PLOT', N('Plan view adds relative position; the section adds level. Neither plots a connection, because none is verified; the section draws the gap in oxblood and names the unknowns. Dana is not on either drawing. The schematic is labelled as schematic on the phone itself.')),
            ])]
    row2 = [col(field_phone(return_strip=True), daycap('BACK FROM THE QUAY', '4 &middot; THE RETURN', 'To Sorrento, not to New York; same position', 'THE CHOSEN SCOPE IS PART OF THE RETURN &middot; NO AUTOMATIC SNAP BACK TO THE HOME CITY')),
            notecol('The opened detail, the return, the supply', [
                ('4 &middot; THE OPENED DETAIL', N('The subject is the quay walk. Its page says what is known (level, that the quay itself is step-free) and what is not (the way down, hours). Route-from-here is a door that needs an origin and says so; it does not silently use New York. Back returns to the Sorrento field at the same position.')),
                ('5 &middot; SUPPLY TYPE, PER UNIT', tbl(['UNIT', 'SUPPLY', 'WHAT THAT MEANS'], [
                    ['The plan and the section (S3)', 'Reusable enrichment &middot; schematic', 'Illustrative geometry, labelled; replaced by verified material before any real-world advice'],
                    ['The reading room (S1), the quay walk (S2)', 'Permitted existing facts', 'Only the access characteristics that are known; hours and connection absent'],
                    ['Dana&rsquo;s status (H2)', 'Attributed &middot; city precision', 'Her words about her afternoon; never a coordinate, never current advice'],
                    ['The widening doors', 'Structured state', 'Area and time inside Sorrento; no Trip is created or required']])),
                ('WHAT IS NOT DRAWN', N('Live conditions, a ferry or train from anywhere, a stay, weather, an arrival day. The person is exploring a city from another city; the page never pretends otherwise. Replace S1&ndash;S3 with a reviewed real-source packet before evaluating any of this as advice.')),
            ])]
    html = page(1900, hh('05', 3600), f'{STAMP} &middot; 05 &middot; D &middot; SORRENTO BEFORE ARRIVAL', '05 &middot; D &middot; Can I explore Sorrento from New York without pretending I am there?',
                'Situation D from the brief, on the synthetic Sorrento packet (S1 a reading room in the upper town, S2 the quay walk, S3 a schematic of the level difference) with Dana&rsquo;s city-level status as the friends expression. Origin unset, no location asked, no Trip required; the map earns the first viewport because orientation is the job; the return goes back to Sorrento.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE RETURN</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Back goes to the chosen city</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '05 - D - Sorrento Before Arrival.dc.html'), 'w').write(html); print('wrote 05', len(html))
