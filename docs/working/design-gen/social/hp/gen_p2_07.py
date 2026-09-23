"""07 · revised (§8.4, §8.5, §8.10): world supply held constant; little context beside rich context; thin supply kept;
the natural end and further exploration without ceremony; supply classes with refresh responsibilities."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N, arow
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_p2_02 import field, u_hour, u_market, u_noodles, u_library, u_table, u_loop, u_organ, u_two_piers, u_film, plan_pair, thin_phone
from gen_artifact import ways_seq_card
from gen_places02 import plan_pair

P = PACKET
def rich_context_phone():
    """The same twelve things, for an account with a saved world and friends: better selection and judgment, not more world."""
    inner = header('NEW YORK', 'Friday') + question_line()
    inner += gut(lead_card('film', 'SATURDAY NIGHT &middot; FREE', 'A film on the lawn by the pier', 'Sunset Park&rsquo;s lawn, the screen up at dark, the harbor behind it. Alex says get there by eight for a spot.', when='Saturday 8:30 PM &middot; free', unknown='Rain plan not posted.', door_text='Saturday&rsquo;s film', h=180,
                          extra=f'<div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{title("Before it, if you like: the pier at sunset, right there", 15, 20, 600)}{when_line("Sunset 7:04 &middot; low water is over by five, so that is a separate afternoon")}</div>'
                          + f'<div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{title("Your saved bakery closes at five", 15, 20, 600)}{when_line("A separate afternoon possibility, not part of the evening")}</div>'), top=20)
    inner += gut(friends_entry(), top=16)
    inner += sect('This weekend') + gut('<div>' + u_hour() + u_market() + '</div>')
    inner += sect('Changed') + gut('<div>' + fact('THE SUNSET PARK BAKERY &middot; YOU SAVED IT', 'Sunday hours moved: now 7 until the loaf runs out, closed by one. Sunday still works; go early.', last=True) + '</div>')
    inner += sect('Worth seeing') + gut(title('One room, before and after', 17, 22, 600) + sup('The Print Room&rsquo;s side room, then and now. <i>Rooms Remade</i>, through Sunday.', INK2) + plan_pair()
                                       + f'<div style="margin-top: 10px;">{author_row("M", "Maya", "THURSDAY")}<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 6px;">&ldquo;The side room was my favorite. Go on a weekday, it was empty.&rdquo;</div></div>' + when_line('Red Hook &middot; Tue&ndash;Sun 11&ndash;6') + door('The Print Room'))
    inner += sect('Any day') + gut('<div>' + u_noodles() + u_library() + u_table() + u_loop() + '</div>')
    inner += sect('Worth knowing') + gut(u_two_piers())
    inner += sect('Sunday') + gut('<div>' + u_organ(last=True) + '</div>')
    inner += gut('<div>' + row('Saved in New York &middot; <span style="color: #6E6862;">12 places</span>', mark='hollow') + row('Places you have been &middot; <span style="color: #6E6862;">since June</span>', mark='hollow', last=True) + '</div>', top=26)
    inner += gut(ending(['Explore the waterfront', 'Around Red Hook', 'Sunday, all day']), top=24)
    return phone2(inner)

def waterfront_phone():
    """After 'Explore the waterfront': more within the same intent, naturally; the end is the end of the supply, not a ceremony."""
    inner = header('The waterfront', 'Red Hook to Sunset Park &middot; from New York', back=True) + question_line()
    inner += gut(lead_card('quay', 'GETTING THERE IS THE THING', 'Three ways home from the water', 'Red Hook by the ferry or the bus; Brooklyn Bridge Park by land the whole way; Governors Island only by the crossing, which is the point and the constraint.', door_text='The three, on the map', h=160), top=20)
    inner += sect('On the water this weekend') + gut('<div>' + event_unit('SUN', '14', 'The grain terminal, open afternoon', 'Sunday 1&ndash;4', 'free', 'Through the pier gate; the top floor is the reason to go.', 'Capacity not posted.', kind='quay') + u_film('Saturday&rsquo;s film') + place_unit('pier', 'The Red Hook pier', 'Any time &middot; free', 'Faces the harbor and the Statue; the other pier for sunset.') + place_unit('loop', 'The waterfront loop', 'Any time &middot; free', 'Five kilometres, flat, shaded after two.', last=True) + '</div>')
    inner += sect('Eating on the way') + gut('<div>' + place_unit('table', 'The long table at the caf&eacute;', 'Saturday mornings &middot; coffee', 'A communal table for twelve; regulars, room for strangers.') + place_unit('loaf', 'The Sunset Park bakery', 'Sunday 7 until the loaf runs out', 'Sesame loaf, Sundays only.', last=True) + '</div>')
    inner += gut(ending(['Back to New York', 'Further: the harbor islands'], note='That is the waterfront this weekend, as far as the listings go.'), top=30)
    return phone2(inner)

SUPPLY = [['The film, with the pier and the bakery placed around it', 'Selection over structured state', 'Listing + sunset + saved places + a friend&rsquo;s time note', 'Recompose when any input changes'],
          ['Two piers, two directions', 'Reusable enrichment', 'Orientation and sunset time', 'Stable; sunset refreshes daily'],
          ['The room comparison', 'Reusable enrichment', 'Made once for the show', 'Expires with the exhibition'],
          ['The changed hours', 'Provider fact, viewer-relevant', 'The bakery&rsquo;s listing', 'Refresh on listing change; shown because the person saved the place'],
          ['Maya&rsquo;s line', 'Attributed human material', 'Her share, under her grant', 'Recompile on withdrawal; expires with her grant'],
          ['The film, the hour, the market, the recital', 'Provider facts', 'Listings', 'Refresh per occurrence; availability stays unclaimed'],
          ['The noodle counter, the library, the table, the loop', 'Provider facts', 'Listings and one authored line each', 'Refresh hours; authored lines are stable'],
          ['Saved / been', 'Viewer-specific selection', 'The person&rsquo;s own record', 'Live counts']]

def board():
    row1 = [col(field('film'), daycap('FRIDAY &middot; RICH WORLD &middot; LITTLE CONTEXT', 'A NEW ACCOUNT', 'The whole packet, no personal data', 'IDENTICAL TO 02 CANDIDATE B &middot; THE WORLD IS NOT GATED BEHIND HISTORY')),
            col(rich_context_phone(), daycap('THE SAME WORLD &middot; RICH CONTEXT', 'A MATURE ACCOUNT', 'Same twelve things; better judgment, not a longer day', 'THE SAME FILM LEADS; A FRIEND&rsquo;S TIMING NOTE; THE PIER AS AN OPTION, NOT A STOP; THE SAVED BAKERY RESURFACED WITH ITS HONEST HOURS; A CHANGE TO A SAVED PLACE')),
            col(thin_phone(), daycap('THIN WORLD &middot; LITTLE CONTEXT', 'THIN SUPPLY, KEPT', 'A bounded, useful collection', 'THE FOURTH CELL, THIN WORLD + RICH CONTEXT, USES ELIGIBLE CONTEXT WITHOUT INVENTING INVENTORY; NOT DRAWN SEPARATELY')),
            notecol('World supply versus personal context', [
                ('THE 2&times;2', tbl(['WORLD SUPPLY', 'LITTLE PERSONAL CONTEXT', 'RICH PERSONAL CONTEXT'], [['Thin', 'Phone 3: a useful bounded collection, no input entrance fee', 'Eligible context used, no invented inventory (annotated, not drawn)'], ['Rich', 'Phone 1: generous, varied discovery immediately', 'Phone 2: better selection, connections and practical judgment']])),
                ('WHAT MATURITY ADDS, AND DOES NOT (&sect;9.5)', N('Phone 2 leads with the same film. What context adds is judgment: Alex&rsquo;s note about when to arrive, the pier named as an option beforehand rather than an appointed stop, the saved bakery resurfaced with its honest closing time as a separate afternoon, and a change to a place the person saved. No schedule is composed; saved places justify relevance, not a longer day. The twelve things are the same twelve things.')),
                ('THE END OF A COLLECTION', N('No count, no &ldquo;the first collection ends here&rdquo;. The page ends with the ways onward, and &ldquo;Explore the waterfront&rdquo; replaces &ldquo;Widen&rdquo;, which narrowed. Phone 4 shows what that door gives: more within the same intent, and an ending that is the end of the listings, said in one plain sentence.')),
            ])]
    row2 = [col(waterfront_phone(), daycap('&ldquo;EXPLORE THE WATERFRONT&rdquo;', 'FURTHER, WITHIN THE SAME INTENT', 'New material, a natural end', 'NOT THE FIRST PAGE AGAIN &middot; NO CEREMONY &middot; A WAY BACK AND A WAY FURTHER')),
            notecol('What each unit costs to keep true', [
                ('SUPPLY AND REFRESH', tbl(['UNIT', 'SUPPLY CLASS', 'SOURCE', 'REFRESH RESPONSIBILITY'], SUPPLY)),
                ('THE HONEST VERSION OF &ldquo;ZERO GENERATED&rdquo;', N('Nothing on these phones is written for this person on demand. That does not make them free: reusable enrichment has to be produced and kept current, provider facts have to be refreshed per occurrence, and the sequence has to be recomposed when any of its inputs change. The table names who owes what. No cost estimate is claimed.')),
                ('HOME AND PLACES ON THE SAME SATURDAY', N('If Home offers the Saturday sequence that day, a person who comes to Places on purpose still finds it here, as the ground it runs on. One seat for proactive delivery does not mean hiding relevant content from deliberate exploration; the two expressions are drawn on 08.')),
            ])]
    html = two_rows(1900, '07', f'{STAMP} &middot; 07 &middot; ABUNDANCE AND CONTEXT &middot; REVISED 09-07 (&sect;8&ndash;&sect;10)', '07 &middot; Does more world produce more possibility even for a new account?',
                    'Revised through the three critiques: world supply is held constant. A new account with no network and a mature account with a populated one see the same twelve things; maturity improves judgment, not the length of the day, and the actual context difference is named. Thin supply is kept. The end of a collection is natural, and further exploration within the same intent is drawn. Every unit carries its supply class and who is responsible for keeping it true.', row1,
                    'FURTHER EXPLORATION, AND WHAT IT COSTS', 'More within the same intent; who keeps each unit true', row2, default_h=5000)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CHANGE LOG &middot; 07', changelog([
        ['1', 'The full packet for a newcomer', 'Nothing asked; same ending doors as the mature page', 'All listings are fixture; sunset is a fixture time', 'Event supply; orientation source'],
        ['2', 'The same film, with better judgment around it; a change to a saved place', 'One card; the pier is an option, the bakery a separate afternoon', 'Sunset + tide + saved places + Alex&rsquo;s time note', 'The friend note&rsquo;s grant'],
        ['3', 'Two real things and the ways onward', 'Same', '&mdash;', '&mdash;'],
        ['4', 'The waterfront as a place to get to, with what is on this weekend', '&ldquo;Explore&rdquo; widens; the end says it is the end of the listings', 'The grain terminal opening and the pier facts are fixture', 'Dated-event supply']])) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '07 - The Supply-Rich Opening.dc.html'), 'w').write(html); print('wrote 07 v2', len(html))
