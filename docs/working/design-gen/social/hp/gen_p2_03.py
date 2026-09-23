"""03 - B · revised (§8.5, §8.6): the question as an editable line; results are evening options; excluded things appear only
when asked, selected or depended on; one lightweight interaction sequence (enter, combine, empty, clear, city, map, detail, back)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N, arow
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_p2_02 import u_hour, u_film, u_noodles, u_library, u_table, u_pier, plan_pair, lead_film

P = PACKET
def hour_lead():
    return lead_card('hall', 'SATURDAY 7&ndash;9 PM &middot; CANAL HALL', 'The listening hour', 'One recording played end to end in the back room, lights down. About sixty seats, no bar; doors 6:45.', when='$12 at the door', unknown='Seats left for this Saturday haven&rsquo;t been confirmed.', door_text='This Saturday&rsquo;s hour', h=170)

def b_scroll(extra_under_hour='', return_strip=None):
    inner = header('NEW YORK', 'Friday') + question_line('Saturday evening')
    lead = hour_lead()
    if extra_under_hour: lead = lead.replace(f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Seats left for this Saturday haven&rsquo;t been confirmed.</div>', f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 4px;">Seats left for this Saturday haven&rsquo;t been confirmed.</div>{extra_under_hour}')
    inner += gut(lead, top=20)
    inner += sect('Also Saturday evening') + gut('<div>' + u_film('Saturday&rsquo;s film') + place_unit('pier', 'The pier at sunset', 'Sunset 7:04 &middot; free', 'The west pier; bring a jacket, it turns cold fast.') + place_unit('noodles', 'The noodle counter', 'Till 10 &middot; $14&ndash;18', 'Hand-pulled at the counter; three blocks from the hall.') + place_unit('table', 'The long table at the caf&eacute;', 'Till 11 &middot; coffee, wine', 'A communal table for twelve; regulars, room for strangers.', last=True) + '</div>')
    inner += gut(ending(['Saturday afternoon instead', 'Around Red Hook', 'Just Saturday, anything']), top=28)
    return phone2(inner)

def enter_phone():
    inner = header('NEW YORK', 'Friday') + question_line()
    inner += gut(f'<div style="height: 120px;"></div>', top=0)
    inner += question_sheet(when='Any time', where='All of New York', who='Just me').replace('What are you looking for?', 'What are you looking for?')
    return phone2(inner)

def constraint_phone():
    inner = header('NEW YORK', 'Friday') + question_line('Somewhere comfortable to sit for an hour')
    inner += gut(place_unit('library', 'The reading room at the branch library', 'Friday till 8 &middot; free', 'Long tables, lamps, quiet. Downtown.', door_text='The branch library'), top=14)
    inner += gut('<div>' + place_unit('table', 'The long table at the caf&eacute;', 'Till 11 &middot; coffee', 'A communal table; noisier, warmer.') + place_unit('room', 'The Print Room&rsquo;s side room', 'Tue&ndash;Sun 11&ndash;6', 'A bench in the exhibition; quiet on weekdays.') + place_unit('pier', 'The pier at low water', 'Any time &middot; free', 'Outdoors, benches along the flood line; shade after two.', last=True) + '</div>')
    inner += gut(ending(['Near a place instead', 'Just me, any time']), top=28)
    return phone2(inner)

def combined_phone():
    """Saturday evening + From friends: the event's own current facts, and a friend's venue note separately attributed and labelled as about the venue."""
    inner = header('NEW YORK', 'Friday') + question_line('Saturday evening', ctx='From friends')
    inner += gut(f'<div style="font-size: 14px; line-height: 19px; color: {MUTE};">Nobody shared this Saturday itself. Two friends know two of these places.</div>', top=14)
    inner += gut('<div>' + event_unit('SAT', '13', 'The listening hour at Canal Hall', P['hour']['when'], P['hour']['price'], P['hour']['note'], P['hour']['unknown'], 'This Saturday&rsquo;s hour', kind='hall') + '</div>', top=10)
    inner += gut(share_line('S', 'Sam', 'Sit on the left side, that&rsquo;s where the speakers are.', 'about Canal Hall &middot; not this Saturday', last=True), top=0)
    inner += gut('<div>' + u_film('Saturday&rsquo;s film') + '</div>', top=10)
    inner += gut(share_line('A', 'Alex', 'The lawn by the pier for the film. Get there at eight for a spot.', 'about the lawn &middot; from a film last month', last=True), top=0)
    inner += gut(ending(['Saturday evening, everyone', 'From friends, any time']), top=28)
    return phone2(inner)

def truly_empty_phone():
    inner = header('NEW YORK', 'Friday') + question_line('Sunday evening', ctx='From friends')
    inner += gut(f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK2};">Nothing from friends for Sunday evening.</div>', top=22)
    inner += sect('Sunday evening, anyway') + gut('<div>' + place_unit('table', 'The long table at the caf&eacute;', 'Till 11 &middot; coffee, wine', 'A communal table for twelve; regulars, room for strangers.') + place_unit('noodles', 'The noodle counter', 'Till 10 &middot; $14&ndash;18', 'Hand-pulled at the counter.', last=True) + '</div>')
    inner += gut(ending(['Sunday evening, everyone', 'From friends, any time']), top=28)
    return phone2(inner)

def with_maya_phone():
    """People context changes relevance within Saturday evening; it does not replace the question or waive the hours."""
    inner = header('NEW YORK', 'Friday') + question_line('Saturday evening', ctx='With Maya')
    inner += gut(lead_card('pier', 'SATURDAY &middot; SUNSET 7:04 &middot; FREE', 'The pier at sunset, with Maya', 'You kept her note about it to do together. The west pier faces the sunset; it turns cold fast after, she says, so bring a jacket.', when='Free &middot; twenty minutes from the noodle bar', door_text='The pier', h=170,
                          extra=f'<div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{author_row("M", "Maya", "LAST MONTH")}<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 6px;">&ldquo;Went back for the pier at sunset. Bring a jacket, it turns cold fast.&rdquo;</div><div class="fn" style="color: {ANCHOR}; margin-top: 4px;">You kept this, to do with her</div></div>'), top=14)
    inner += sect('Also Saturday evening, for two') + gut('<div>' + place_unit('table', 'The long table at the caf&eacute;', 'Till 11 &middot; coffee, wine', 'Somewhere to talk; four blocks from the pier.') + event_unit('SAT', '13', '<i>Playtime</i> on the lawn by the pier', 'Saturday 8:30 PM', 'free', 'Tati&rsquo;s city of glass; the same lawn as the pier, easy after sunset.', kind='film') + event_unit('SAT', '13', 'The listening hour at Canal Hall', 'Saturday 7&ndash;9 PM', '$12 at the door', 'Lights down, no talking. Right if that is the point of the evening.', last=True, kind='hall') + '</div>')
    inner += sect('Another time') + gut('<div>' + place_unit('room', 'The Harbor Print Room', 'Closes at 6 on Saturday', 'Her favorite, but not an evening. Saturday afternoon fits.', door_text='Saturday afternoon, with Maya', last=True) + '</div>')
    inner += gut(ending(['Just me, Saturday evening', 'Maya&rsquo;s shares']), top=28)
    return phone2(inner)

def cleared_phone():
    inner = header('NEW YORK', 'Friday') + question_line()
    inner += gut(f'<div style="font-size: 14px; line-height: 19px; color: {MUTE};">Back to everything. Saturday evening is one tap away in the line above.</div>', top=14)
    inner += gut(lead_film(), top=14)
    inner += sect('This weekend') + gut('<div>' + u_hour() + u_pier() + '</div>')
    inner += gut(ending(['Explore the waterfront', 'Around Red Hook']), top=28)
    return phone2(inner)

def map_phone():
    inner = header('NEW YORK', 'Friday') + question_line('Saturday evening')
    svg = ('<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/><path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120 L349 300 L0 300 Z" fill="rgba(61,80,102,0.10)"/>'
           '<rect x="172" y="38" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M172 43 H184" stroke="#1B1714" stroke-width="1.4"/><text x="190" y="44" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">CANAL HALL &#183; 7&#8211;9</text>'
           '<circle cx="40" cy="80" r="6" fill="#1B1714"/><text x="52" y="84" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE NOODLE COUNTER</text>'
           '<circle cx="262" cy="192" r="26" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="252" cy="206" r="5" fill="#B0853A"/><rect x="266" y="176" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M266 181 H278" stroke="#1B1714" stroke-width="1.4"/>'
           '<text x="120" y="236" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PIER &#183; PLAYTIME 8:30</text>'
           '<circle cx="90" cy="120" r="6" fill="#1B1714"/><text x="102" y="124" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE LONG TABLE</text>'
           '<circle cx="112" cy="150" r="6" fill="none" stroke="#B5AFA5" stroke-width="1.2"/><text x="124" y="154" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#B5AFA5">RED HOOK</text>')
    inner += map_wash(300, svg, top=14)
    inner += gut('<div>' + row('The listening hour &middot; <span style="color: #6E6862;">Canal Hall &middot; 7&ndash;9</span>', mark='dashed', color=INK) + row('<i>Playtime</i> &middot; <span style="color: #6E6862;">the lawn by the pier &middot; 8:30</span>', mark='dashed', color=INK) + row('The noodle counter &middot; <span style="color: #6E6862;">till 10</span>', mark='solid', color=INK) + row('The long table &middot; <span style="color: #6E6862;">till 11</span>', mark='solid', color=INK, last=True) + '</div>', top=14)
    return phone2(inner)

def board():
    row1 = [col(b_scroll(), daycap('FRIDAY &middot; &ldquo;SOMETHING SATURDAY EVENING&rdquo;', 'THE RESULTS', 'Evening options, and only evening options', 'THE QUESTION IS ONE PILL WITH &times; &middot; THE HOUR LEADS; FOUR MORE FIT &middot; THE MARKET AND THE EXHIBITION ARE NOT LISTED, BECAUSE THEY DO NOT FIT')),
            col(map_phone(), daycap('THE SAME QUESTION &middot; MAP', 'THE MAP FORM', 'The same five things where they are; Red Hook as background', 'MAP IS IN THE HEADER ONLY &middot; BACKGROUND GEOGRAPHY IS NOT AN INACTIVE RESULT')),
            col(enter_phone(), daycap('TAP THE LINE', 'ENTERING A QUESTION', 'One sheet, three rows; any of them may stay as it is', 'WHEN &middot; WHERE &middot; WHO &middot; NOT A WIZARD; &ldquo;SHOW ME&rdquo; IS THE ONLY COMMITMENT')),
            notecol('Directing discovery without learning our nouns', [
                ('THE CONTROL MODEL', N('Three dimensions, three places: the header holds the city, search and map; the line under it holds the question as one pill and, when chosen, one context chip; the sheet behind the line has three rows, when, where, who. Map access is no longer repeated. Nothing announces sets or revisions.')),
                ('EXCLUSIONS, SELECTIVE', N('A Saturday-evening question returns evening options. The morning market and the exhibition that closes at six are not listed and not ghosted; they were not asked about, selected or relied on. Board 08 C5 is corrected accordingly. The map keeps Red Hook as background geography without treating it as a rejected result.')),
                ('THE FIRST VIEWPORT', N('The hour with its picture, price and one uncertainty; the film; the start of the list. The person can decide whether it is their kind of evening without tapping.')),
            ])]
    row2 = [col(constraint_phone(), daycap('1 &middot; AN ORDINARY CONSTRAINT', '&ldquo;SOMEWHERE COMFORTABLE TO SIT FOR AN HOUR&rdquo;', 'Typed in the line; answered with places', 'NO CATEGORY TAXONOMY &middot; THE BEST FIT FIRST, THREE MORE WITH THEIR DIFFERENCE')),
            col(combined_phone(), daycap('2 &middot; SATURDAY EVENING + FROM FRIENDS', 'COMBINED: THE EVENT&rsquo;S FACTS, A FRIEND&rsquo;S VENUE NOTE', 'Sam knows the hall, not this Saturday; the label says which', 'VENUE-LEVEL CONTEXT IS NOT DISCARDED (&sect;9.4) &middot; NOBODY IS IMPLIED TO HAVE SHARED OR TO BE GOING')),
            col(with_maya_phone(), daycap('3 &middot; &ldquo;WITH MAYA&rdquo;', 'A SHARED POSSIBILITY INSIDE SATURDAY EVENING', 'One authorized reason; the hours still in force', 'THE PRINT ROOM CLOSES AT SIX AND SAYS SO UNDER &ldquo;ANOTHER TIME&rdquo; (&sect;9.3) &middot; NOTHING SENT TO HER')),
            col(cleared_phone(), daycap('4 &middot; CLEAR', 'THE QUESTION CLEARED', 'Back to everything; the question is one tap away', 'CLEARING PRESERVES THE CITY AND THE POSITION; CHANGING CITY PRESERVES THE QUESTION (05)')),
            ]
    row3 = [col(truly_empty_phone(), daycap('2b &middot; SUNDAY EVENING + FROM FRIENDS', 'TRULY EMPTY', 'Says so once; keeps Sunday evening; offers the world', 'THE COMPARISON &sect;9.4 ASKS FOR: A GENUINELY EMPTY FRIENDS CONTEXT BESIDE A USEFUL ONE')),
            notecol('The sequence, answered', [
                ('THE FIVE QUESTIONS FROM &sect;8.6', tbl(['', 'QUESTION', 'ANSWER ON THIS BOARD'], [
                    ['1', 'Enter a place, neighborhood, category or ordinary constraint', 'Type it into the line (phone 5) or pick from the sheet (phone 3); the line shows what governs'],
                    ['2', 'Combine Saturday evening with From friends; return when empty', 'Phone 6: the event&rsquo;s own facts plus a friend&rsquo;s venue note, labelled as about the venue; phone 2b: a truly empty case says so once and keeps the time; one door removes the chip'],
                    ['3', 'Choose &ldquo;with Maya&rdquo; or an existing dinner as context', 'Phone 7 and 06: a context chip in umber changes relevance inside Saturday evening. What makes it better than a list of her places: one authorized reason (the person kept her pier note to do together), a place to talk, the same lawn after, and the hour explained for two; her favorite that closes at six is offered for the afternoon with the tradeoff said. Nothing sent'],
                    ['4', 'What clearing preserves; what changing city preserves', 'Phone 8: clearing keeps city and position; 05: changing city keeps the question'],
                    ['5', 'Map toggle, detail, back', 'Phone 2: same things where they are; 02 and 06: detail and back restore the scroll and the question']])),
                ('WHAT &ldquo;WITH MAYA&rdquo; MAY AND MAY NOT USE', N('Used: one kept share, in her words, that the person chose to do with her; the current question; listed hours; her practical note. Not used: her calendar, her availability, any inferred preference, past enjoyment as a wish to repeat. People context changes relevance within the question; it never replaces the question or waives a constraint.')),
                ('PROPOSED VERSUS SUPPORTED', N('The result-set identity in code carries scope and a query digest; it does not yet carry time or a social source, and the mobile map path returns to the scope, not to a query. The line, the chip and the sheet are proposals. The map form and the detail return are supported today.')),
            ], w=1720)]
    html = two_rows(1900, '03', f'{STAMP} &middot; 03 &middot; B &middot; SOMETHING SATURDAY EVENING &middot; REVISED 09-07 (&sect;8&ndash;&sect;10)', '03 &middot; B &middot; Directing discovery without learning our nouns',
                    'Revised through the three critiques: the question is an editable line with one context chip and a three-row sheet behind it; results are the things that fit, and excluded things appear only when asked for, selected or relied on; the map is in the header only. Then the interaction sequence: an ordinary constraint; Saturday evening with friends, where a venue note is labelled as about the venue, beside a truly empty case; &ldquo;with Maya&rdquo; as a shared possibility that keeps the evening&rsquo;s hours; and clearing.', row1,
                    'THE INTERACTION SEQUENCE', 'Enter, combine, choose a context, clear', row2, default_h=5600)
    html = html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + ''.join(row3) + '</div>' + '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 03', changelog([
        ['Results', 'Five evening options with their prices and one uncertainty each', 'The question is a pill with &times;; excluded things are not shown', 'Hours and prices are fixture listings', 'Time in the result-set identity'],
        ['Map', 'The same five, where they are', 'Map is one header control', '&mdash;', 'Map return to a query, not just a scope'],
        ['Sheet', 'A way to say when, where, who', 'Three rows, one commitment', '&mdash;', 'The sheet is a proposal'],
        ['Constraint', 'Four places to sit, with their difference', 'Typed language works as a question', 'Fixture', 'Natural-language constraints in search'],
        ['Combined', 'The hour&rsquo;s facts with Sam&rsquo;s seat note beside them, labelled as about the hall', 'Removing the source keeps the time', 'Sam&rsquo;s and Alex&rsquo;s notes are venue-level, under their grants; the occurrence facts are the listing&rsquo;s', 'Social source in the result-set identity; venue-vs-occurrence labelling'],
        ['With Maya', 'A shared possibility inside the evening: the pier she wrote about, kept to do together', 'A context chip, distinct from her shares; hours still in force', 'One kept share; listed hours; sunset time', 'Kept-intention context (Life 31)'],
        ['Clear', 'Everything, with the question one tap away', 'City and position kept', '&mdash;', '&mdash;']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)
    return html

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '03 - B - Something Saturday Evening.dc.html'), 'w').write(html); print('wrote 03 v2', len(html))
