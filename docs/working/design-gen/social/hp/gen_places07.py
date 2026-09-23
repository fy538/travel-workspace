"""07 · The supply-rich ordinary opening and its deliberate widening (brief §6.4 richness check), beside the sparse
opening from 02. Nine units, genuinely different reasons to engage, none generated bespoke per row. Fixture copy only."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, reading_card, author_row
from gen_places import scope_header, map_wash, branch, places_phone, ICON_TIDE, ICON_BOOK
from gen_merge import tbl, daycap, page
from gen_placeskit import event_stub, question_control, STAMP, hh, OUT, area_card
from gen_places02 import notecol, plan_pair, lead_w5, market_row, contrasting_set, field_phone as sparse_field
from gen_artifact import ways_seq_card
from gen_seam import chip

def qc(q='New York, now', tail='NO QUESTION YET &middot; NOTHING ASKED OF YOU'):
    return question_control(q, 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', tail)

def rich_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:10 PM &middot; a mature account') + qc()
    # 1 · a prepared possibility as a sequence (structured state over saved places + tide table)
    inner += gut(ways_seq_card('Saturday, if the afternoon is open', [('2:40', 'Low water on the pier', 'The shaded side after two; the flood line east to where the kerbs end.', 'SUNSET PARK'), ('4:10', 'The bakery, on the way back', 'Saved by you Friday; open till five.', '9 MIN ON FOOT')],
                              meta_t='TIDE TABLE + YOUR SAVED PLACES &middot; NOTHING BOOKED, NOTHING ASSUMED ABOUT SATURDAY'), top=22)
    # 2 · the reusable comparison (the Print Room) with one friend line inside the unit
    inner += sect('Worth understanding') + gut(lead_w5().replace("door_text", "door_text") + f'<div style="margin-top: 10px;">{author_row("M", "Maya", "THURSDAY &middot; FRIENDS")}<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 6px;">&ldquo;The side room was my favorite.&rdquo;</div><div class="fn" style="color: {ANCHOR}; margin-top: 4px;">ONE FRIEND LINE INSIDE THE PLACE IT IS ABOUT &middot; THE PAGE DOES NOT SWITCH TO A FRIENDS MODE</div></div>')
    # 3 · a finding (bare)
    inner += gut(u2('The pier at low water is the shaded side after two', 'The warehouses take the sun off the water walk by 2:30; the return by land is the warm way.', meta_t='TIDE TABLE + THE SUN&rsquo;S ANGLE &middot; FIXTURE'), top=26)
    # 4 · a change to something saved
    inner += sect('Changed') + gut('<div>' + fact('THE SUNSET PARK BAKERY &middot; SAVED BY YOU', 'Sunday hours moved: now 7 until the loaf runs out, closed by one. The Sunday you had in mind still works; go early.', last=True) + '</div>' + meta('A PLACE YOU SAVED CHANGED &middot; THEN/NOW, NOT A NOTIFICATION', 8))
    # 5, 6 · dated things
    inner += sect('Also in the city') + gut(contrasting_set())
    inner += sect('This Saturday') + gut('<div>' + market_row() + '</div>')
    # 7 · an area relation
    inner += sect('An area') + gut(area_card())
    # 8 · a reading
    inner += gut(reading_card('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', 'The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes.', 'Read the chapter'), top=26)
    # 9 · continuity doors and the end
    inner += gut('<div>' + row('Saved in New York &middot; <span style="color: #6E6862;">12 places</span>', mark='hollow') + row('Places you have been &middot; <span style="color: #6E6862;">since June</span>', mark='hollow', last=True) + '</div>', top=26)
    inner += gut(f'<div style="padding: 16px 0 0 0;"><div class="fn" style="color: {ANCHOR};">THE FIRST COLLECTION ENDS HERE &middot; NINE THINGS</div><div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Widen to the waterfront') + door('Sunday instead') + door('Follow the exhibition') + '</div></div>', top=10)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">NINE REASONS, NINE KINDS &middot; NOTHING GENERATED PER ROW &middot; NOTHING RECYCLED TO LOOK FRESH</div></div>'
    return places_phone(inner, 0)

def widened_area_phone():
    inner = scope_header('THE WATERFRONT', 'Widened from New York &middot; Red Hook to Sunset Park', back=True) + qc('New York, now', 'WIDENED &middot; A NEW COLLECTION, SAID SO')
    inner += gut(f'<div style="padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">YOU WIDENED TO THE WATERFRONT &middot; NEW MATERIAL, NOT THE FIRST NINE AGAIN</span></div>', top=10)
    inner += gut(u2('Three ways home from the water', 'Red Hook by the ferry or the bus; Brooklyn Bridge Park by land the whole way; Governors Island only by the crossing, which is the point and the constraint.', meta_t='A SPATIAL COMPARISON &middot; REUSABLE &middot; NOT MADE FOR YOU'), top=22)
    inner += gut('<div>' + branch(ICON_TIDE, 'Red Hook', 'Harbor first &middot; scheduled way in', 'flexible way out') + branch(ICON_BOOK, 'Brooklyn Bridge Park', 'Continuous land access', 'easiest to shorten') + branch(ICON_TIDE, 'Governors Island', 'The crossing is the experience', 'the return is least flexible', ghost=True) + '</div>', top=14)
    inner += sect('On the water this week') + gut('<div>' + event_stub('SUN 14', 'The grain terminal, open afternoon', 'Sunday 1&ndash;4', 'free', 'A DATED OPENING &middot; ACCESS BY THE PIER GATE &middot; CAPACITY NOT KNOWN') + '</div>')
    inner += gut(f'<div style="padding: 16px 0 0 0;"><div class="fn" style="color: {ANCHOR};">THIS COLLECTION ENDS HERE &middot; FIVE THINGS</div><div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Back to New York') + door('Further: the harbor islands') + '</div></div>', top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">WIDENING IS A DELIBERATE ACT &middot; IT NAMES ITS SCOPE AND ENDS TOO</div></div>'
    return places_phone(inner, 0)

def widened_time_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Sunday') + qc('Sunday', 'A NEW SET &middot; THE NEW QUESTION GOVERNS')
    inner += gut(f'<div style="padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">SUNDAY INSTEAD &middot; THE SAME WORLD, THE DAY CHANGED &middot; NOT FRIDAY&rsquo;S NINE RE-DATED</span></div>', top=10)
    inner += gut(ways_seq_card('Sunday, if the morning is open', [('10:30', 'The bakery, early', 'Sunday hours: 7 until the loaf runs out; closed by one.', 'YOUR SAVED PLACE &middot; CHANGED HOURS'), ('1:40', 'Low water on the pier', 'The flood line east; the shaded side after two.', 'SUNSET PARK')], meta_t='TIDE TABLE + YOUR SAVED PLACES &middot; THE SAME TWO STOPS AS HOME&rsquo;S SUNDAY, IF HOME OFFERS THEM'), top=22)
    inner += sect('Sunday only') + gut('<div>' + row('The Print Room &middot; <span style="color: #6E6862;"><i>Rooms Remade</i> closes Sunday at 6 &middot; the last day</span>', mark='dashed', color=INK) + row('The greenmarket &middot; <span style="color: #6E6862;">Saturdays &middot; not Sunday</span>', mark='hollow', muted=True, last=True) + '</div>')
    inner += gut(f'<div style="padding: 16px 0 0 0;"><div class="fn" style="color: {ANCHOR};">THIS COLLECTION ENDS HERE &middot; THREE THINGS</div><div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Back to now') + door('Saturday instead') + '</div></div>', top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">TIME WIDENING CHANGES ELIGIBILITY HONESTLY &middot; THE MARKET DROPS OUT AND SAYS WHY</div></div>'
    return places_phone(inner, 0)

SUPPLY = [['1', 'Saturday sequence', 'Viewer-specific selection over structured state', 'Tide table + the person&rsquo;s saved places; composed, not written'],
          ['2', 'The room comparison', 'Reusable enrichment', 'Made once; shown to anyone'],
          ['2b', 'Maya&rsquo;s line inside it', 'Attributed human material', 'One line, in the place it is about; no mode switch'],
          ['3', 'The shaded-side finding', 'Reusable enrichment', 'Tide + sun angle; true for anyone on that pier'],
          ['4', 'The bakery&rsquo;s changed hours', 'Permitted existing facts &middot; viewer-relevant', 'Shown because the person saved the place; then/now'],
          ['5', 'The listening hour', 'Permitted existing facts', 'A dated occurrence'],
          ['6', 'The greenmarket', 'Permitted existing facts', 'This occurrence of a series'],
          ['7', 'Red Hook as an area', 'Reusable enrichment', 'A spatial relation; outline on the map'],
          ['8', 'The Harbor Book chapter', 'Reusable enrichment &middot; licensed', 'Optional depth behind a door'],
          ['9', 'Saved / been', 'Viewer-specific selection', 'Continuity doors with honest counts']]

def board():
    row1 = [col(rich_phone(), daycap('FRIDAY 12:10 PM &middot; NO QUERY &middot; A MATURE ACCOUNT', '1 &middot; THE SUPPLY-RICH OPENING', 'Nine things, nine kinds of reason; the collection still ends', 'A SEQUENCE, A COMPARISON, A FINDING, A CHANGE, TWO DATED THINGS, AN AREA, A READING, TWO DOORS &middot; NOTHING GENERATED PER ROW')),
            col(widened_area_phone(), daycap('&ldquo;WIDEN TO THE WATERFRONT&rdquo;', '2 &middot; DELIBERATE WIDENING BY AREA', 'A new collection with new material, named as widened', 'NOT THE FIRST NINE AGAIN &middot; ENDS TOO &middot; A WAY BACK')),
            col(widened_time_phone(), daycap('&ldquo;SUNDAY INSTEAD&rdquo;', '3 &middot; DELIBERATE WIDENING BY TIME', 'Eligibility changes honestly; the market drops out and says why', 'THE SAME TWO STOPS HOME MAY OFFER ON SUNDAY &middot; THE SEAT LAW DECIDES WHICH ROOT DELIVERS')),
            notecol('The richness check', [
                ('WHAT MAKES IT RICH', N('Not more rows of the same recommendation. Nine units, each a different kind of reason to engage: a prepared sequence, a reusable comparison with one friend line inside it, a finding, a change to something saved, a dated hour, a series occurrence, an area relation, a reading, and two continuity doors. The page still ends and names three ways onward.')),
                ('WHAT IT COSTS', tbl(['#', 'UNIT', 'SUPPLY CLASS', 'NOTE'], SUPPLY)),
                ('THE COUNT', N('Of ten units, six are reusable enrichment or permitted facts anyone could see, three are selections specific to this viewer over structured state, one is attributed human material. Zero are generated on demand. Abundance here is selection and reuse, which is the only kind of abundance a first build can afford.')),
            ])]
    row2 = [col(sparse_field(), daycap('THE SAME MOMENT &middot; NO HISTORY', '4 &middot; THE SPARSE OPENING, FROM 02', 'Useful on its own; not a degraded version of phone 1', 'THE COMPARISON THE BRIEF ASKS FOR &middot; THE NEWCOMER&rsquo;S PAGE IS COMPLETE, NOT APOLOGETIC')),
            notecol('Sparse beside rich', [
                ('THE SAME SKELETON', N('Both pages open the same way: scope, no question, a reusable comparison that is worth seeing on its own, a small contrasting set, a dated occurrence, the end of the collection and the ways onward. The rich page adds what history and a friend network supply (a sequence over saved places, a changed hours line, a friend&rsquo;s sentence) and adds one more reusable unit (the area, the reading). It does not add a different kind of page.')),
                ('WHAT THE SPARSE PAGE NEVER DOES', N('It does not ask for interests, location, or friends. It does not pad with reflection prompts or a welcome. It does not say the world is empty. It ends with the same doors, and the doors lead to the same widened collections drawn here.')),
                ('WHAT DECIDES BETWEEN ROOTS', N('The Saturday and Sunday sequences may also be Home&rsquo;s possibility on those days. The seat law (Life 19, cited on Home 07) gives one present-delivery seat: when Home offers the sequence, Places shows it as the ground it runs on, not as a second offer. This board draws Places as if Home is quiet.')),
            ])]
    html = page(1900, hh('07', 4800), f'{STAMP} &middot; 07 &middot; THE SUPPLY-RICH OPENING AND ITS WIDENING', '07 &middot; Does abundance come from reuse and selection, not bespoke generation per row?',
                'The richness check from &sect;6.4 of the brief: an ordinary New York opening for a mature account with a saved world and a friend network, its two deliberate widenings (by area, by time), and the sparse opening from 02 beside it for the comparison the brief requires. Every unit carries its supply class.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">SPARSE BESIDE RICH</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">The newcomer&rsquo;s page is complete on its own</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '07 - The Supply-Rich Opening.dc.html'), 'w').write(html); print('wrote 07', len(html))
