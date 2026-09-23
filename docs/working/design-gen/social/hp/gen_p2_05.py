"""05 - D · revised (§8.9): keep the orientation insight, pair it with worthwhile possibilities, say uncertainty once,
distinguish distance from travel time, leave Dana's note alone."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_places05 import plan_svg, section_svg
from gen_places import map_wash

S = SORRENTO
def orientation_card():
    return card(f'<div style="margin: -16px -16px 12px -16px; border-radius: 18px 18px 0 0; overflow: hidden;">{map_wash(150, section_svg(), top=0).replace("margin: 0px 22px 0 22px", "margin: 0").replace("border-radius: 12px", "border-radius: 0")}</div>'
                + f'<div class="kick" style="color: {GOLDD};">WORTH KNOWING BEFORE YOU GO</div>'
                + f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; margin-top: 6px;">The town is on a cliff; the water is forty metres down</div>'
                + sup('The reading room and the quay walk are 180 metres apart on the map and a cliff apart on the ground. Stairs, a lift or a road between them aren&rsquo;t listed here yet, so give yourself time between anything up and anything down.', INK2)
                + door('The upper town and the quay, on the map'))

def u_piazza(): return event_unit('THU', '18', S['piazza']['name'], S['piazza']['when'], S['piazza']['price'], S['piazza']['note'], kind='market')
def u_capri(door_text='Capri, for a day'): return place_unit('quay', S['capri']['name'], 'Ferries from 7:30 &middot; 25 minutes each way &middot; ' + S['capri']['price'], 'Fifteen kilometres across the water; the last boat back is 6:40.', S['capri']['unknown'], door_text)
def u_terraces(): return place_unit('terrace', S['terraces']['name'], S['terraces']['when'] + ' &middot; ' + S['terraces']['price'], S['terraces']['note'])
def u_quay(last=False): return place_unit('quay', S['quay']['name'], S['quay']['when'] + ' &middot; ' + S['quay']['price'], S['quay']['note'], last=last)
def u_reading(last=True): return place_unit('library', S['reading_room']['name'], S['reading_room']['when'] + ' &middot; ' + S['reading_room']['price'], 'A small reading room with an exhibition preview.', last=last)

def field_phone(return_strip=False):
    inner = header('SORRENTO', 'From New York &middot; before any visit') + question_line(hint='Anything in Sorrento, any day')
    inner += gut(orientation_card(), top=20)
    inner += sect('Worth a day') + gut('<div>' + u_capri() + u_terraces() + '</div>')
    inner += sect('Any evening') + gut('<div>' + u_piazza() + u_quay(last=True) + '</div>')
    inner += sect('Any morning') + gut('<div>' + u_reading() + '</div>')
    inner += gut(ending(['The upper town', 'Across the harbor', 'Back to New York']), top=28)
    return phone2(inner)

def friends_phone():
    inner = header('SORRENTO', 'From friends') + question_line(ctx='From friends')
    inner += gut(card(author_row('D', 'Dana', 'THIS WEEK') + f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK}; margin-top: 10px;">We spent the late afternoon by the water.</div>' + f'<div style="display: flex; gap: 18px; align-items: center;">{door("Reply to Dana")}</div>'), top=18)
    inner += gut(ending(['All of Sorrento']), top=28)
    return phone2(inner)

def capri_phone():
    inner = header('Capri, for a day', 'From Sorrento', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{illo("quay", 190)}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">Fifteen kilometres across the water; twenty-five minutes by the fast ferry.</div>' + when_line('Ferries from 7:30 &middot; &euro;22 each way &middot; the last boat back is 6:40'), top=16)
    inner += sect('Worth knowing') + gut('<div>' + fact('THE CROSSING', 'Sailings are cancelled in rough sea. Check the morning of; the harbor office posts it by seven.') + fact('THE LAST BOAT', 'Six-forty. Miss it and you are on the island for the night.', last=True) + '</div>')
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('The ferry company&rsquo;s timetable') + src('Opens outside Vesper') + door('Ask about Capri') + door('Keep', INK) + '</div>', top=26)
    return phone2(inner)

def back_phone():
    return field_phone(return_strip=True)

def board():
    row1 = [col(field_phone(), daycap('FRIDAY &middot; SORRENTO, FROM NEW YORK', 'THE FIELD', 'One thing worth knowing, then five things worth doing', 'THE CLIFF LEADS BECAUSE A FLAT MAP HIDES IT &middot; UNCERTAINTY SAID ONCE &middot; DISTANCE AND TIME KEPT APART')),
            col(friends_phone(), daycap('SORRENTO &middot; FROM FRIENDS', 'DANA', 'Her words, unenriched', 'NO TOWN-FACT GLOSS ON HER NOTE &middot; REPLY IS RIGHT THERE')),
            col(capri_phone(), daycap('CAPRI OPENED', 'A DAY ACROSS THE WATER', 'Distance, crossing time, the last boat', 'THE ONE REAL RISK, ONCE &middot; THE TIMETABLE IS EXTERNAL AND SAYS SO')),
            notecol('Another city, inviting', [
                ('THE REVISION', N('The first export opened Sorrento with an access-risk report: unknown steps, unknown lift, unknown hours, repeated three times. Now the orientation insight leads once, in one sentence a person can use (give yourself time between up and down), and five worthwhile things follow: a day on Capri, the lemon terraces, the Thursday piazza market, the quay, the reading room.')),
                ('DISTANCE VERSUS TIME', N('&ldquo;180 metres on the map&rdquo; is distance; &ldquo;a cliff apart on the ground&rdquo; is the consequence; &ldquo;twenty-five minutes by the fast ferry&rdquo; is time from a timetable. None of them is called minutes-apart-in-plan.')),
                ('DANA', N('Her note is her note. It is not glossed with where the water is, and it is not relabelled as advice about conditions. Reply is on the card.')),
            ])]
    row2 = [col(back_phone(), daycap('BACK FROM CAPRI', 'THE RETURN', 'To Sorrento, at the same position', 'THE CHOSEN CITY IS PART OF THE RETURN &middot; NO SNAP BACK TO NEW YORK')),
            notecol('The supply', [
                ('SUPPLY AND REFRESH', tbl(['UNIT', 'SUPPLY CLASS', 'REFRESH'], [['The cliff', 'Reusable enrichment &middot; schematic', 'Stable; replace the schematic with surveyed geometry before real advice'], ['Capri', 'Provider facts (timetable, fare)', 'Per sailing day; cancellations the morning of'], ['The terraces, the quay, the reading room', 'Provider facts + one authored line', 'Hours'], ['The piazza market', 'Dated occurrence', 'Per Thursday'], ['Dana&rsquo;s note', 'Attributed human material', 'Expires with her grant']])),
                ('NOT DRAWN', N('Live sea conditions, a stay, an arrival day, a route from anywhere. The person is exploring a city from another city.')),
            ])]
    html = two_rows(1900, '05', f'{STAMP} &middot; 05 &middot; D &middot; SORRENTO BEFORE ARRIVAL &middot; REVISED 09-07 (&sect;8.9)', '05 &middot; D &middot; Another city, inviting rather than an access-risk report',
                    'Revised after the first-export critique: the orientation insight stays and leads once; five worthwhile possibilities follow; distance and travel time are kept apart; Dana&rsquo;s note is left as she wrote it.', row1, 'THE RETURN', 'Back goes to the chosen city', row2, default_h=3800)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 05', changelog([
        ['Field', 'A cliff a flat map hides, then five things to do', 'One question hint; three doors onward', 'Timetable facts and the schematic are fixture', 'Surveyed geometry; event supply'],
        ['Friends', 'Dana&rsquo;s afternoon, in her words', 'Reply on the card', 'Under her grant', 'Reply to a person'],
        ['Capri', 'Distance, crossing time, the last boat, the one risk', 'The timetable is an external door', 'Fixture timetable', 'Provider timetable'],
        ['Back', 'Sorrento, same position', '&mdash;', '&mdash;', '&mdash;']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '05 - D - Sorrento Before Arrival.dc.html'), 'w').write(html); print('wrote 05 v2', len(html))
