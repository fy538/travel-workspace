"""10 · Content-led versus map-led opening, on the same inventory, context and media (§11.4). Rich and sparse supply;
the initial viewport marked; the toggle between them; readings that cannot be plotted shown in relation to the map."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N
from gen_generous3 import sect, title, sup, gut, card, fact
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_p2_02 import field, thin_phone, lead_film, u_hour, u_market, u_pier, u_noodles, u_library, u_table, u_loop, u_organ, u_exhibition, u_two_piers, viewport_marker
from gen_places import map_wash

P = PACKET
def T(x, y, t, bold=True, col='#1B1714', size=10):
    return f'<text x="{x}" y="{y}" font-family="JetBrains Mono, monospace" font-size="{size}" {"font-weight=\"700\"" if bold else ""} letter-spacing="0.8" fill="{col}">{t}</text>'
def dated(x, y): return f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M{x} {y+5} H{x+12}" stroke="#1B1714" stroke-width="1.4"/>'
def dot(x, y, r=6, c='#1B1714'): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'

def rich_map_svg(h=330, focus=None):
    water = f'<path d="M0 {h*0.62:.0f} Q60 {h*0.52:.0f} 120 {h*0.6:.0f} Q180 {h*0.68:.0f} 240 {h*0.52:.0f} Q300 {h*0.4:.0f} 349 {h*0.45:.0f}" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/><path d="M0 {h*0.62:.0f} Q60 {h*0.52:.0f} 120 {h*0.6:.0f} Q180 {h*0.68:.0f} 240 {h*0.52:.0f} Q300 {h*0.4:.0f} 349 {h*0.45:.0f} L349 {h} L0 {h} Z" fill="rgba(61,80,102,0.10)"/>'
    marks = (dated(150, 30) + T(166, 36, 'CANAL HALL &#183; SAT 7:15') + T(166, 48, 'REICH, MUSIC FOR 18', False, '#8F877C')
             + dot(120, 62) + T(132, 66, 'THE NOODLE COUNTER')
             + dot(40, 110) + T(52, 106, 'THE BRANCH LIBRARY') + T(52, 118, 'FRI TILL 8', False, '#8F877C')
             + dated(48, 150) + T(64, 156, 'THE OLD CHURCH &#183; SUN 4') + T(64, 168, 'BACH ON THE ORGAN', False, '#8F877C')
             + dot(196, 108) + T(208, 112, 'THE LONG TABLE')
             + dot(70, 210) + T(82, 206, 'THE PRINT ROOM') + T(82, 218, 'RED HOOK &#183; THROUGH SUN', False, '#8F877C')
             + dot(60, 250, 5, '#B5AFA5') + T(70, 254, 'RED HOOK PIER &#183; HARBOR VIEW', False, '#8F877C', 9)
             + dated(140, 124) + T(156, 130, 'GREENMARKET &#183; SAT AM')
             + f'<circle cx="270" cy="{h-52}" r="32" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/>'
             + dated(276, h-70) + dot(258, h-40, 5, '#B0853A') + T(150, h-12, 'SUNSET PARK &#183; PLAYTIME 8:30') )
    return water + marks

def map_led_phone(sparse=False):
    inner = header('NEW YORK', 'Friday') + question_line()
    if sparse:
        svg = (f'<path d="M0 200 Q60 170 120 190 Q180 210 240 170 Q300 130 349 145" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/><path d="M0 200 Q60 170 120 190 Q180 210 240 170 Q300 130 349 145 L349 330 L0 330 Z" fill="rgba(61,80,102,0.10)"/>'
               + dated(140, 124) + T(156, 130, 'GREENMARKET &#183; SAT AM') + f'<circle cx="270" cy="278" r="32" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/>' + dated(276, 260) + dot(258, 290, 5, '#B0853A') + T(150, 318, 'SUNSET PARK &#183; PLAYTIME 8:30'))
        inner += map_wash(330, svg, top=14)
        inner += gut(friends_entry('none'), top=14)
        inner += gut(lead_film(), top=16)
        inner += sect('This Saturday') + gut('<div>' + u_market() + '</div>')
        inner += gut(ending(['Explore the waterfront', 'Another neighborhood', 'Sunday, all day']), top=30)
        return phone2(inner)
    inner += map_wash(330, rich_map_svg(330), top=14)
    inner += gut(friends_entry('none'), top=14)
    inner += gut(lead_film(), top=16)
    inner += sect('Around Canal Street') + gut('<div>' + u_hour() + u_noodles() + u_table() + '</div>')
    inner += sect('Sunset Park') + gut('<div>' + u_pier() + u_loop(last=True) + '</div>')
    inner += sect('Red Hook') + gut(u_exhibition())
    inner += sect('Downtown') + gut('<div>' + u_library() + u_organ(last=True) + '</div>')
    inner += sect('Saturday morning') + gut('<div>' + u_market() + '</div>')
    inner += sect('Worth knowing') + gut(u_two_piers())
    inner += gut(ending(['Explore the waterfront', 'Around Red Hook', 'Sunday, all day']), top=30)
    return phone2(inner)

def toggle_strip():
    """Content → map → content: the question, the entry and the scroll position survive. Three narrow frames."""
    def mini(label, html):
        return f'<div style="width: 393px; flex: none;"><div class="kickm" style="margin-bottom: 8px;">{label}</div>{html}</div>'
    a = field('film')
    b = map_led_phone()
    return f'<div style="display: flex; gap: 30px; align-items: flex-start;">{mini("1 &middot; THE FIELD, SCROLLED TO SUNSET PARK", a)}{mini("2 &middot; MAP, FROM THE HEADER &middot; SUNSET PARK CENTRED", b)}{mini("3 &middot; BACK TO THE FIELD &middot; SAME POSITION", a)}</div>'

def board():
    row1 = [viewport_marker(col(field('film'), daycap('RICH SUPPLY &middot; CONTENT-LED', 'THE FIELD FIRST', 'The film with its picture, then the weekend', 'THE FIRST VIEWPORT IS ONE POSSIBILITY THE PERSON CAN IMAGINE ENJOYING'))),
            viewport_marker(col(map_led_phone(), daycap('RICH SUPPLY &middot; MAP-LED', 'THE MAP FIRST', 'Twelve things where they are, then the same units', 'THE FIRST VIEWPORT IS WHERE THINGS ARE &middot; THE SAME FILM CARD FOLLOWS &middot; SAME INVENTORY, SAME MEDIA'))),
            viewport_marker(col(thin_phone(), daycap('SPARSE SUPPLY &middot; CONTENT-LED', 'TWO THINGS, THE FIELD FIRST', 'The film, the market, the ways onward', 'STILL A WORTHWHILE VISIT'))),
            viewport_marker(col(map_led_phone(sparse=True), daycap('SPARSE SUPPLY &middot; MAP-LED', 'TWO THINGS, THE MAP FIRST', 'Two marks on a large map, then the same two units', 'THE MAP SPENDS THE VIEWPORT ON TWO MARKS'))),
            ]
    row2 = [notecol('What each expression delivers (observed on rendered frames)', [
                ('OBSERVED', tbl(['', 'CONTENT-LED', 'MAP-LED'], [
                    ['Immediate value, rich', 'A named film with its setting, time and price, and what to do before it, all above the fold', 'Twelve labels on a map: where things are, which cluster near which; the film card arrives after a scroll'],
                    ['Immediate value, sparse', 'The film, the market; done', 'Two marks on a large map; the same two units below'],
                    ['What the map makes easier', 'Nothing yet; the map is one tap away', 'Seeing that the hall, the counter and the table are one area; that Red Hook is across the water; that Sunset Park holds the pier, the film and the loop'],
                    ['Text encountered before the first possibility', 'One card', 'Twelve labels, then one card'],
                    ['Readings that cannot be plotted', 'Sit in the field as units', 'The room comparison anchors to the Print Room mark and the two-piers reading names its two marks; neither is given a coordinate of its own']])),
                ('RECOMMENDATION', N('Content-led for the ordinary opening in a known city, on both rich and sparse supply. Map-led when orientation is the job: an unfamiliar city (05), or a spatial question typed into the line (&ldquo;near Red Hook&rdquo;). The map stays one tap away in the header and keeps the question, the entry and the scroll position when toggled (row below). This is an observation from rendered static frames; it is not validated by use.')),
                ('WHAT REMAINS A HYPOTHESIS', N('That a person prefers a possibility before a map on a first open; that twelve labels read as orientation rather than clutter on a real device; that the toggle feels like one exploration. The rendered visual review and, later, participant observation decide these.')),
            ], w=1000)]
    html = two_rows(1900, '10', f'{STAMP} &middot; 10 &middot; CONTENT-LED VERSUS MAP-LED &middot; SAME EVIDENCE &middot; 09-07 (&sect;11.4)', '10 &middot; Content-led versus map-led, on the same evidence',
                    'The comparison scheduled since &sect;8.11: the same twelve things, the same no-network entry, the same media, rich and sparse, with the first viewport marked. What each expression delivers is recorded from the rendered frames; the recommendation is stated as an observation, not a validation.', row1,
                    'THE TOGGLE', 'Field to map and back: the question, the entry and the position survive', [f'<div style="flex: none;">{toggle_strip()}</div>'], default_h=7000)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; gap: 46px;">' + ''.join(row2) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '10 - Content-led vs Map-led.dc.html'), 'w').write(html); print('wrote 10', len(html))
