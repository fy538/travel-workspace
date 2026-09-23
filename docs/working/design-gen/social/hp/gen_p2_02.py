"""02 - A · revised (§8.2, §8.3, §8.4, §8.9): a newcomer in an abundant city. Three strong lead candidates on one
expanded packet, the opened detail and its return, thin supply, a long-names test and a 1.3× text test.
No internal explanation inside any phone; annotations are outside. Fixture copy only."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N
from gen_generous3 import sect, title, sup, gut, card, fact
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_places02 import plan_pair

P = PACKET
def viewport_marker(col_html, y=812):
    """A dashed line at the first viewport's end, drawn beside the phone, not inside it."""
    return col_html.replace('<div style="width: 393px; flex: none; display: flex; flex-direction: column;">', f'<div style="width: 393px; flex: none; display: flex; flex-direction: column; position: relative;"><div style="position: absolute; left: -6px; right: -6px; top: {y}px; border-top: 1.5px dashed {OX}; pointer-events: none; z-index: 2;"><span class="fn" style="position: absolute; right: 0; top: -14px; color: {OX};">FIRST VIEWPORT</span></div>', 1)

# ───────────────────────────── units of the assortment ─────────────────────────────
def u_film(door_text='Saturday&rsquo;s film'): return event_unit('SAT', '13', P['film']['name'], P['film']['when'], P['film']['price'], P['film']['note'], P['film']['unknown'], door_text, kind='film')
def u_hour(): return event_unit('SAT', '13', 'The listening hour at Canal Hall', P['hour']['when'], P['hour']['price'], P['hour']['note'], P['hour']['unknown'], 'This Saturday&rsquo;s hour', kind='hall')
def u_market(): return event_unit('SAT', '13', P['market']['name'], P['market']['when'], P['market']['price'], P['market']['note'])
def u_pier(): return place_unit('pier', P['pier']['name'], P['pier']['when'], P['pier']['note'])
def u_noodles(): return place_unit('noodles', P['noodles']['name'], P['noodles']['when'] + ' &middot; ' + P['noodles']['price'], P['noodles']['note'])
def u_library(): return place_unit('library', P['library']['name'], P['library']['when'] + ' &middot; ' + P['library']['price'], P['library']['note'])
def u_loop(last=True): return place_unit('loop', P['loop']['name'], P['loop']['when'] + ' &middot; ' + P['loop']['price'], P['loop']['note'], last=last)
def u_table(): return place_unit('table', P['table']['name'], P['table']['when'] + ' &middot; ' + P['table']['price'], P['table']['note'])
def u_organ(last=False): return event_unit('SUN', '14', P['organ']['name'], P['organ']['when'], P['organ']['price'], P['organ']['note'], last=last)
def u_exhibition():
    return (title('One room, before and after', 17, 22, 600) + sup('The Print Room&rsquo;s side room: a corridor and four closed rooms until 2024, one room now, the old wall a threshold. <i>Rooms Remade</i> shows both, through Sunday.', INK2) + plan_pair()
            + when_line('Red Hook &middot; Tue&ndash;Sun 11&ndash;6') + unc(P['print_room']['unknown']) + door('The Print Room'))
def u_two_piers():
    return (title('Two piers, two directions', 17, 22, 600) + sup(P['two_piers']['text'], INK2) + when_line('Sunset 7:04 this week') + door('The piers, on the map'))

def lead_two_piers():
    return lead_card('pier', 'WORTH KNOWING THIS WEEK', 'Two piers, two directions', P['two_piers']['text'], when='Sunset is at 7:04 this week; either pier, about forty minutes on the L from downtown.', door_text='The piers, on the map', h=180,
                     extra=f'<div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{title("Saturday, on the west pier: the film on the lawn, 8:30", 15, 20, 600)}{when_line("Free &middot; starts at dark &middot; bring something to sit on")}</div>')
def lead_film():
    return lead_card('film', 'SATURDAY NIGHT &middot; FREE', 'A film on the lawn by the pier', 'Sunset Park&rsquo;s lawn, the screen up at dark, the harbor behind it. Bring something to sit on.', when='Saturday 8:30 PM &middot; free', unknown='Rain plan not posted.', door_text='Saturday&rsquo;s film', h=180,
                     extra=f'<div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{title("Before it: the pier, right there, faces west", 15, 20, 600)}{when_line("Sunset 7:04 &middot; the harbor view is the other pier, in Red Hook, another night")}</div>')
def lead_exhibition():
    return card(plate('room', 180) + f'<div class="kick" style="color: {GOLDD};">THROUGH SUNDAY &middot; RED HOOK</div>' + f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; margin-top: 6px;">One room, before and after</div>'
                + sup('The Print Room&rsquo;s side room: a corridor and four closed rooms until 2024, one room now, the old wall a threshold. <i>Rooms Remade</i> shows both.', INK2) + plan_pair() + when_line('Tue&ndash;Sun 11&ndash;6') + unc(P['print_room']['unknown']) + door('The Print Room'))

def assortment(lead):
    """The same rich packet under each lead; what the lead took is not repeated."""
    out = ''
    if lead != 'film' and lead != 'piers':
        out += sect('This weekend') + gut('<div>' + u_film() + u_hour() + u_market() + u_pier() + '</div>')
    elif lead == 'piers':
        out += sect('This weekend') + gut('<div>' + u_hour() + u_market() + u_pier() + '</div>')
    else:
        out += sect('This weekend') + gut('<div>' + u_hour() + u_market() + u_pier() + '</div>')
    out += sect('Any day') + gut('<div>' + u_noodles() + u_library() + u_table() + u_loop() + '</div>')
    if lead != 'exhibition':
        out += sect('Worth seeing') + gut(u_exhibition())
    if lead != 'piers' and lead != 'film':
        out += sect('Worth knowing') + gut(u_two_piers())
    elif lead == 'film':
        out += sect('Worth knowing') + gut(u_two_piers().replace('Two piers, two directions', 'Two piers, two directions'))
    out += sect('Sunday') + gut('<div>' + u_organ(last=True) + '</div>')
    return out

def field(lead='piers', return_strip=False, names=None):
    inner = header('NEW YORK', 'Friday')
    inner += question_line()
    lead_html = {'piers': lead_two_piers, 'film': lead_film, 'exhibition': lead_exhibition}[lead]()
    inner += gut(lead_html, top=20)
    inner += gut(friends_entry(), top=16)
    inner += assortment(lead)
    inner += gut(ending(['Explore the waterfront', 'Around Red Hook', 'Sunday, all day']), top=30)
    html = phone2(inner)
    if names:
        for a, b in names.items(): html = html.replace(a, b)
    return html

def focus_phone():
    inner = header('The Harbor Print Room', 'Red Hook', back=True)
    inner += gut(plate('room', 190).replace('margin: -16px -16px 12px -16px', 'margin: 0 0 14px 0; border-radius: 14px'), top=18)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">A print workshop in a former warehouse on Van Brunt Street.</div>' + when_line('Tuesday to Sunday 11&ndash;6 &middot; hours as listed'))
    inner += sect('<i>Rooms Remade</i> &middot; through Sunday') + gut(sup('The side room: a corridor and four closed rooms until 2024, one room now, the old wall a threshold. The show is the two plans and the photographs between them.', INK2) + plan_pair() + unc(P['print_room']['unknown']))
    inner += sect('Getting there') + gut('<div>' + fact('BY BUS', 'The B61 stops two blocks away.') + fact('BY FERRY', 'Nine minutes on foot from the Red Hook landing.', last=True) + '</div>')
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('The exhibition') + door('Ask about the Print Room') + door('Keep', INK) + '</div>', top=28)
    return phone2(inner)

def thin_phone():
    inner = header('NEW YORK', 'Friday') + question_line()
    inner += gut(lead_film(), top=20)
    inner += sect('This Saturday') + gut('<div>' + u_market() + '</div>')
    inner += gut(ending(['Explore the waterfront', 'Another neighborhood', 'Sunday, all day']), top=30)
    return phone2(inner)

LONG = {'The Harbor Print Room': 'The Harbor Print Room and Letterpress Workshop', 'A film on the lawn by the pier': 'Outdoor film: <i>The Long Goodbye</i> on the lawn by the pier', 'The listening hour at Canal Hall': 'The listening hour at Canal Hall, back room', 'The noodle counter': 'The hand-pulled noodle counter on Canal Street'}

def board():
    row1 = [viewport_marker(col(field('film'), daycap('FRIDAY &middot; A NEW ACCOUNT &middot; RICH WORLD', 'LEAD CANDIDATE B &middot; A POSSIBILITY', 'A free film on the lawn, Saturday night; the pier before it', 'RECOMMENDED (&sect;9.2) &middot; SOMETHING TO IMAGINE ENJOYING; THE SPATIAL DISTINCTION SUPPORTS IT (WHICH PIER, WHAT VIEW, WHEN)'))),
            viewport_marker(col(field('piers'), daycap('THE SAME PACKET', 'LEAD CANDIDATE A &middot; A DISCOVERY', 'Two piers, two directions; then a full weekend', 'KEPT AS A COMPARISON &middot; AN EXPLANATION IS NOT INHERENTLY BETTER THAN A WELL-CHOSEN POSSIBILITY'))),
            viewport_marker(col(field('exhibition'), daycap('THE SAME PACKET', 'LEAD CANDIDATE C &middot; THE EXHIBITION', 'One room, before and after', 'KEPT ONLY WHERE ITS VISUAL EVIDENCE EARNS IT &middot; RISKS READING AS A CULTURAL MAGAZINE (§8.3)'))),
            notecol('What changed, and why', [
                ('THE REVISION', N('Internal copy is gone from the phones: no &ldquo;selected, not measured&rdquo;, no result-set announcements, no supply economics, no instructions about how to experience a reading. The world packet grew from five things to twelve, spanning food, music, outdoor, low-cost social, indoor and one spatial discovery. The newcomer gets that whole packet with no personal data; history (07) changes judgment, not access.')),
                ('THE THREE LEADS, ON ONE EVIDENCE', N('B leads (&sect;9.2): a recognizable possibility with atmosphere, time, cost and an easy onward action, and the spatial distinction folded in where it improves it: the pier right there faces west, sunset is 7:04, the harbor view is the other pier another night. A keeps the discovery as the lead for comparison. C is the exhibition, which must earn the lead with its plans and does not. Understanding supports the possibility here; it does not compete with it.')),
                ('THE FIRST VIEWPORT', N('The dashed line marks about 812px. Under B the person sees something they can imagine enjoying Saturday night, what to do before it, and the start of the weekend list. Under A they see an explanation first. Under C, plans of a room.')),
            ])]
    row2 = [col(focus_phone(), daycap('THE PRINT ROOM OPENED', 'THE OPENED DETAIL', 'Identity, the exhibition, how to get there', 'HONESTLY SPARSE &middot; ONE UNCERTAINTY IN PLAIN WORDS &middot; NO RELATIONSHIP TRACE AND NO LECTURE ABOUT ITS ABSENCE')),
            col(thin_phone(), daycap('VARIATION &middot; THIN SUPPLY', 'THIN SUPPLY, KEPT', 'The film, the market, the ways onward', 'NO PADDING, NO PROMPT, NO COUNT &middot; STILL A WORTHWHILE VISIT')),
            col(field('film', names=LONG), daycap('TEST &middot; LONGER NAMES', 'LONG NAMES', 'Four names lengthened; nothing truncates', 'TITLES WRAP TO TWO LINES; DATES AND PRICES STAY ON THEIR OWN LINE')),
            col(large(field('film')), daycap('TEST &middot; TEXT AT 1.3&times;', 'ENLARGED TEXT', 'Everything reflows within 393px', 'SUPPORTING TEXT 14&rarr;18, ROWS 15&rarr;20; NO CONTROL OR FACT DEPENDS ON THE SMALLEST TYPE'))]
    html = two_rows(1900, '02', f'{STAMP} &middot; 02 &middot; A &middot; THE ORDINARY OPENING &middot; REVISED 09-07 (&sect;8&ndash;&sect;10)', '02 &middot; A &middot; A newcomer in an abundant city',
                    'Revised through the three critiques: no internal explanation inside any phone; a twelve-thing packet across food, music, outdoor, low-cost social, indoor and a spatial discovery, with the subjects named; the film-led candidate recommended and two others kept as comparisons; a newcomer with no network, whose From friends entry is quiet; the opened detail; thin supply; a long-names test and a 1.3&times; text test. The map form is on 03; the map-led comparison is the next pass.', row1,
                    'THE DETAIL, THIN SUPPLY, AND TWO TESTS', 'Opened, then less; longer names; larger text', row2, default_h=5600)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 02', changelog([
        ['B', 'A free Saturday-night possibility with the pier before it and which view to expect', 'Nothing asked; the search line is a quiet invitation; From friends is a row with faces', 'Sunset time and pier orientation are fixture facts; the film&rsquo;s time and price are from its listing', 'Dated-event supply; a source for sunset and orientation'],
        ['A', 'The discovery first, kept as a comparison', 'Same', 'Same', 'Same'],
        ['C', 'The exhibition&rsquo;s plans', 'Same', 'The plans are reusable enrichment made once for the show', 'A producer for reusable comparisons'],
        ['Detail', 'Where the Print Room is and how to reach it', 'Three doors, one of them Keep; nothing pressed', 'Bus and ferry facts are fixture listings', 'Provider transit facts'],
        ['Thin', 'Still a worthwhile visit with two things', 'The ways onward are the same as the rich page&rsquo;s', '&mdash;', '&mdash;']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '02 - A - The Ordinary Opening.dc.html'), 'w').write(html); print('wrote 02 v2', len(html))
