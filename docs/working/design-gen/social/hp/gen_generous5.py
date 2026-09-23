"""Vesper — Home · revision 5: the social split.
Directed and shared-consequential material → Home. Casual sharing → Places, as a 'From friends' scope over the
same world, with a semantic (never biometric) friends map. Life People stays the record.
H1: the casual share leaves the lead; Home projects it inside the possibility it changes.
H2: Treatment 2's region narrows to 'Addressed to you'.
P1 (new): Places · From friends — the scope, the map, and the Place Focus with a friend's note beside the verdict."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
import gen_generous3 as g3
import gen_generous4 as g4
from gen_generous3 import (sect, meta, title, sup, gut, u2, card, author_row, share_card, handoff_card, arr_card, fact,
                           rows_A, COLD, caption, col, board_page, head, FOOT, N, v2, WEEK_SUN, WEEK_MON, ending, facepile, arow, compare2, span)
from gen_generous4 import ways_card, h1_floor, DELETION, v3
from gen_places import scope_header, map_wash, places_phone, ICON_MARKET, ICON_BOWL

OUT = g3.OUT

# ───────────────────────────── H1 rev 5 · the casual share moves to Places ─────────────────────────────
def h1v5():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(ways_card('Today', [
        ('The sesame loaf, then the water', 'Maya, Friday: &ldquo;Sundays only &mdash; go before eleven or it&rsquo;s gone.&rdquo; Bakery by 10:30; low water on the pier nine minutes on.', 'MORNING &middot; 10:30 &rarr; 1:40 &middot; MAYA&rsquo;S SHARE, IN PLACES'),
        ('The flood line, walked at low water', 'The granite kerbs show where the gates&rsquo; protection ends.', 'AFTERNOON &middot; 1:40&ndash;4'),
        ('Stay in. The skillet, preheated dry', 'Four minutes dry, then oil, then dough &mdash; Thursday&rsquo;s soggy crust was the pan, not the dough.', 'TONIGHT'),
    ]), top=22)
    inner += rows_A()
    inner += sect('Worth knowing') + gut(COLD())
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>')
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

H1_NOTES = notecol('The split, applied to Sunday', [
    ('WHAT MOVED', N('Maya&rsquo;s bakery share was casual, not addressed. Under the split it lives in Places under the friends scope. Home projects it only where it changes something today: inside the first option of &ldquo;Today&rdquo;, attributed, with a metadata pointer to where the share lives. The lead card is gone; the prepared alternatives lead, as ruled for a quiet day.')),
    ('THE DOOR', N('&ldquo;What your friends have shared&rdquo; now points to Places in the friends scope, not to Life. Life People stays the record behind it.')),
    ('THE DELETION TEST STILL HOLDS', ledger([(k, r) for k, v, r in DELETION])),
    ('THE FLOOR', N('Unchanged: direct-state read, rows, two horizon rows, the Life door. The floor does not yet have a friends scope either; that is the same backlog.')),
], w=440)

def H1():
    cols = [col(v3('h1v3'), caption('BEFORE &middot; REVISION 3', 'Generous, eight units', 'THE INPUT TO THE DELETION TEST')),
            col(h1v5(), caption('AFTER &middot; REVISION 5', 'Pruned, and split', 'THE CASUAL SHARE MOVES TO PLACES; HOME KEEPS ITS EFFECT')),
            col(h1_floor(), caption('THE FLOOR &middot; REAL OWNERS TODAY', 'What the first account will see', 'DIRECT STATE &middot; ROWS &middot; TWO HORIZONS &middot; THE LIFE DOOR')),
            H1_NOTES]
    return board_page(1880, 2655, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 5 &middot; H1 &middot; ORDINARY SUNDAY &middot; PROPOSAL', 'H1 &middot; The generous Sunday after the social split',
                      'Directed and shared-consequential material stays on Home. Casual sharing lives in Places. The Sunday page keeps the effect of Maya&rsquo;s share inside the possibility it changes and points to where the share itself lives.', cols, FOOT)

# ───────────────────────────── H2 rev 5 · the region narrows to 'Addressed to you' ─────────────────────────────
def alex_card(): return g3.alex_card()
def market_card(with_theo=True): return g3.market_card(with_theo)
def h2_read(): return g3.h2_read()
END_MON = g3.END_MON
SHOW_ROW_MAYA = row('The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted &middot; Maya sent a place for after</span>', mark='solid', color=GOLD)

def rows_A5(with_alex=True):
    rows = []
    if with_alex: rows.append(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you']))
    rows.append(arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D']))
    rows.append(SHOW_ROW_MAYA)
    rows.append(row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed'))
    rows[-1] = rows[-1].replace('padding: 8px 0;"', 'padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"')
    return sect('In motion') + gut(''.join(rows))

def h2v5_t1():
    inner = h2_read() + gut(alex_card(), top=22) + rows_A5(with_alex=False)
    inner += sect('This week') + gut(market_card() + '<div style="height: 26px;"></div>'
        + u2('Sunday with Dana: her bookshop opens at eleven', 'Dana: &ldquo;this one, for Sunday? I want the poetry shelf in the back.&rdquo; Six minutes from the bakery Maya shared.', meta_t='COURT STREET &middot; OPENS 11 &middot; ADDRESSED TO YOU THURSDAY')
        + '<div style="height: 26px;"></div>'
        + u2('After the show Friday: the noodle bar three blocks from the hall', 'Maya: &ldquo;this one after, it&rsquo;s open till one and you won&rsquo;t need a table.&rdquo;', meta_t='ADDRESSED TO YOU SATURDAY &middot; OPEN TILL 1'))
    inner += sect('Worth knowing') + gut(COLD())
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += END_MON()
    return phone(inner, 0)

def h2v5_t2():
    inner = h2_read() + gut(alex_card(), top=22) + rows_A5(with_alex=False)
    inner += sect('This week') + gut(market_card())
    inner += sect('Addressed to you') + gut('<div style="display: flex; flex-direction: column; gap: 16px;">'
        + handoff_card('D', 'Dana', 'THURSDAY &middot; TO YOU', 'This one, for Sunday? I want the poetry shelf in the back.', 'A USED BOOKSHOP ON COURT STREET &middot; OPENS 11 &middot; SIX MINUTES FROM THE BAKERY MAYA SHARED', 'The bookshop')
        + handoff_card('M', 'Maya', 'SATURDAY &middot; TO YOU', 'This one after the show, it&rsquo;s open till one and you won&rsquo;t need a table.', 'THE NOODLE BAR &middot; THREE BLOCKS FROM THE HALL &middot; OPEN TILL 1', 'The noodle bar')
        + '</div>')
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS &middot; THE CASUAL SHARES, ON THE MAP', 0), top=20)
    inner += sect('Worth knowing') + gut(COLD())
    inner += END_MON()
    return phone(inner, 0)

H2_NOTES = notecol('The split, applied to the week', [
    ('WHAT CHANGED', N('The region is now <b>Addressed to you</b>: things people deliberately gave this person, each with its reason. Dana&rsquo;s bookshop and Maya&rsquo;s noodle bar (a new fixture: addressed Saturday, for after Friday&rsquo;s show). Maya&rsquo;s casual bakery share is no longer on Home at all; it lives in Places under the friends scope, and the bookshop card mentions it only as a distance.')),
    ('TREATMENT 1', N('Distributed: the two addressed places sit inside the units they change, the Sunday unit and a new after-the-show unit; the show&rsquo;s row carries a clause. One pull door at the foot, now to Places.')),
    ('TREATMENT 2 &middot; RECOMMENDED', N('The addressed material appears once each, in the person&rsquo;s own words, in a region that exists only because two addressed units were unspent above. The region&rsquo;s condition is unchanged; its content is narrower and its name is honest.')),
    ('D-H4 CLOSES', N('&ldquo;What else have my people shared?&rdquo; is answered by Places in the friends scope (board P1), not by a present-tense band on Life People and not by a fifth surface. Life People stays the record.')),
    ('THE SPARSE VARIANT AND THE LIFE FRAME', N('Unchanged from revision 3 and kept on the canvas page; the sparse week has no addressed material and therefore no region.')),
], w=440)

def H2():
    cols = [col(v3('h2v3_t2') if os.path.exists(os.path.join(os.path.dirname(__file__), 'v3phones', 'h2v3_t2.html')) else v2('h2v2_t2'), caption('BEFORE &middot; REVISION 3', 'From your people', 'A CASUAL SHARE AND A HANDOFF IN ONE REGION')),
            col(h2v5_t1(), caption('TREATMENT 1 &middot; REVISION 5', 'Distributed', 'ADDRESSED PLACES INSIDE THE UNITS THEY CHANGE')),
            col(h2v5_t2(), caption('TREATMENT 2 &middot; RECOMMENDED &middot; REVISION 5', 'Addressed to you', 'ONLY WHAT PEOPLE GAVE THIS PERSON &middot; THE CASUAL SHARES ARE IN PLACES')),
            H2_NOTES]
    return board_page(1880, 2530, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 5 &middot; H2 &middot; SOCIALLY ACTIVE WEEK &middot; PROPOSAL', 'H2 &middot; Home keeps what was addressed; Places keeps what was shared',
                      'Same week, same people. Directed material (Dana&rsquo;s bookshop, Maya&rsquo;s noodle bar for after the show, Alex&rsquo;s arrangement, Theo&rsquo;s note inside the market) stays on Home. Maya&rsquo;s casual bakery share moves to Places. The region is renamed for what it now holds.', cols, FOOT)

# ───────────────────────────── P1 · Places · From friends ─────────────────────────────
def friends_map():
    """Semantic, never biometric: each mark is something a friend deliberately made visible, at the precision they chose."""
    svg = ('<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
           '<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100 L349 230 L0 230 Z" fill="rgba(61,80,102,0.10)"/>'
           # Maya's bakery — Place-precise (she shared the Place)
           '<circle cx="96" cy="92" r="9" fill="#1B1714"/><text x="92" y="96" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">M</text>'
           '<text x="112" y="88" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE BAKERY</text>'
           '<text x="112" y="100" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">SHARED FRI &#183; PLACE</text>'
           # Theo's market — Place-precise (a handoff)
           '<circle cx="196" cy="58" r="9" fill="#1B1714"/><text x="192" y="62" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">T</text>'
           '<text x="212" y="54" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE MARKET</text>'
           '<text x="212" y="66" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">NOTE &#183; TUE &#183; PLACE</text>'
           # Alex — neighborhood precision (he shared a neighborhood, not a place)
           '<circle cx="272" cy="146" r="26" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/>'
           '<circle cx="272" cy="146" r="9" fill="#1B1714"/><text x="268" y="150" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">A</text>'
           '<text x="130" y="196" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">SUNSET PARK</text>'
           '<text x="130" y="208" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE PIER AT SUNSET &#183; NEIGHBORHOOD</text>'
           # you
           '<circle cx="40" cy="176" r="5" fill="#4A3428"/><text x="50" y="180" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">YOU</text>')
    return map_wash(230, svg)

def p1_friends():
    inner = scope_header('NEW YORK &middot; FROM FRIENDS', 'What four people deliberately made visible, and where &middot; nothing is where anyone is now')
    inner += friends_map()
    inner += (f'<div style="padding: 10px 22px 0 22px; display: flex; justify-content: space-between;"><span class="fn" style="color: {ANCHOR};">PLACE &middot; NEIGHBORHOOD &middot; CITY = THE PRECISION THEY CHOSE</span><span class="fn" style="color: {ANCHOR};">ELSEWHERE &darr;</span></div>')
    inner += gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 150, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'SUNSET PARK &middot; 14 MIN BY BIKE &middot; SHARED AS A PLACE', 'The bakery'), top=22)
    inner += gut('<div>' + arow('Theo &middot; the greenmarket &middot; <span style="color: #6E6862;">&ldquo;bread gone by ten&rdquo; &middot; Tuesday &middot; may-use</span>', avatars=['T'])
                 + arow('Alex &middot; Sunset Park &middot; <span style="color: #6E6862;">&ldquo;the pier at sunset&rdquo; &middot; neighborhood, not a place</span>', avatars=['A'], last=True) + '</div>', top=22)
    inner += sect('Elsewhere') + gut(arow('Dana &middot; Sorrento, this week &middot; <span style="color: #6E6862;">a featured status &middot; city precision &middot; until Saturday</span>', avatars=['D'], last=True)
                                     + meta('STATUS IS WHAT SHE CHOSE TO SHOW, NOT WHERE SHE IS &middot; IT EXPIRES WITH HER RETURN', 8))
    inner += gut(door('Everything shared with you, by person') + meta('LIFE &middot; PEOPLE &middot; THE RECORD, WITH GRANTS AND EPOCHS', 0), top=32)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">FOUR PEOPLE &middot; FOUR THINGS &middot; THE SCOPE ENDS HERE</div></div>'
    return places_phone(inner, 0)

def p1_focus():
    """Place Focus for the bakery: Maya's share sits beside the verdict it changes — the four admissible social forms, unchanged."""
    inner = scope_header('THE BAKERY', 'Sunset Park &middot; 14 min by bike &middot; open now', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">Go before eleven on a Sunday; the rest of the week it is a good bakery, not a reason to cross the park.</div>'
                 + sup('Weekday hours 7&ndash;4 &middot; Sunday 7 until the loaf runs out &middot; checked 8:40 AM', MUTE), top=22)
    inner += gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 0, '', 'HER SHARE IS WHY THE VERDICT SAYS SUNDAY', None), top=22)
    inner += sect('Your relationship') + gut(body_line('Saved by you, Friday. No visit yet. Shared to you by one person.'))
    inner += sect('One way in') + gut(u2('The loaf, then the water', 'Bakery by 10:30; low water on the pier nine minutes on.', meta_t='SUNDAY &middot; 10:30 &rarr; 1:40 &middot; THE SAME OPTION HOME OFFERS'))
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Open the walk') + door('Ask Vesper about the bakery') + door('Correct your trace') + '</div>', top=30)
    return places_phone(inner, 0)

def body_line(t): return f'<div style="font-size: 14px; line-height: 19px; color: {INK};">{t}</div>'

P1_NOTES = notecol('Places · From friends', [
    ('THE SCOPE', N('A fourth scope beside &ldquo;for me&rdquo;, &ldquo;with Maya&rdquo;, and &ldquo;for Friday dinner&rdquo;, over the same map and the same field. It shows what friends deliberately made visible and where. It is finite: four people, four things, and it ends. It is ranked by situation (what is usable this week), never by person.')),
    ('THE MAP IS SEMANTIC', N('Every mark answers: is this where they were, what they shared, or what is in a plan; who authored it; at what precision; for which audience; until when. Maya and Theo shared a Place, so their marks are Place-precise. Alex shared a neighborhood, so his mark is a dashed ring. Dana featured a city-level Status, so she is under &ldquo;Elsewhere&rdquo;, not on the map. Nobody&rsquo;s current location appears, and nothing is inferred from presence.')),
    ('WHAT IT IS NOT', N('Not a friends feed (it ends; recency breaks ties, it does not admit). Not a friend map (no live position, no rings that mean &ldquo;here now&rdquo;). Not a people browser (no profiles, no counts, no ranking of people).')),
    ('PLACE FOCUS', N('Unchanged from the accepted Places anatomy: the friend&rsquo;s note sits beside the verdict it changes, under its grant, and disappears with it. The &ldquo;one way in&rdquo; is the same option Home offers, so the two roots agree.')),
    ('HOME&rsquo;S DOOR', N('&ldquo;What your friends have shared&rdquo; on Home lands here with the scope selected. Back returns to the exact Home unit. Life People remains the record behind &ldquo;by person&rdquo;.')),
    ('PRODUCTION', N('Grant-scoped share reads (MP1) exist for addressed Place handoffs; a friends-scope composer over shares, statuses, and handoffs is new; the precision ladder and the city-level &ldquo;Elsewhere&rdquo; band need the featured-Status substrate. Nothing here requires location permission from anyone.')),
], w=440)

def P1():
    cols = [col(p1_friends(), caption('1 &middot; PLACES &middot; FROM FRIENDS', 'The scope and the map', 'FOUR PEOPLE, FOUR THINGS, THREE PRECISIONS &middot; IT ENDS')),
            col(p1_focus(), caption('2 &middot; PLACE FOCUS &middot; THE BAKERY', 'A friend&rsquo;s note beside the verdict', 'THE ACCEPTED SOCIAL FORM, UNCHANGED')),
            P1_NOTES]
    return board_page(1440, 1610, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 5 &middot; P1 &middot; PLACES &middot; FROM FRIENDS &middot; PROPOSAL', 'P1 &middot; Casual sharing lives in Places, on a map that is semantic, not biometric',
                      'Where the pull question is answered: what have my people shared, and where. One scope over the same world, marks at the precision each person chose, a city-level &ldquo;Elsewhere&rdquo; for featured statuses, and the record behind it in Life People.', cols, FOOT)

# ───────────────────────────── H0 rev 5 addendum ─────────────────────────────
def H0(diag):
    html = g4.H0(diag)
    add = ('<div style="display: flex; flex-direction: column; gap: 10px;"><div class="shead"><span>THE SOCIAL SPLIT &middot; 2026-09-05 &middot; RULED (AMENDS CANON §2)</span><span class="rule"></span></div>'
           + N('<b>Home</b> takes what is directed and what is shared-consequential: addressed to me, invited, a contribution to our arrangement, a decision asked of me, a plan edit under a grant, a change to a shared occasion. It shows the consequence, not the notification; one ask per page. '
               '<b>Places</b> takes casual sharing as a &ldquo;From friends&rdquo; scope over the same world, with a semantic map (what people deliberately made visible, at the precision they chose; never where anyone is). '
               '<b>Life People</b> stays the record. The conditional region on Home narrows to <b>Addressed to you</b>. <b>D-H4 closes</b>: the pull question is answered by Places, not by a present-tense band on Life or a fifth surface. '
               'Boards: H1 rev 5, H2 rev 5, P1 (new). Decision record §2 amended; Home root contract rule 1 cites it.')
           + '</div>')
    html = html.replace("<div style=\"display: flex; flex-direction: column; gap: 34px;\">", "<div style=\"display: flex; flex-direction: column; gap: 34px;\">" + add, 1)
    html = html.replace('REVISION 4 &middot; H0 &middot; CANON EVENTS', 'REVISION 5 &middot; H0 &middot; THE SOCIAL SPLIT, CANON EVENTS')
    html = html.replace("Browsing beyond selection routes to Life &middot; People; no present-tense aperture created.', 'Proposed; social-aperture lane owns the question'", "Browsing beyond selection routes to <b>Places &middot; From friends</b> (P1); Life &middot; People is the record; no present-tense band, no fifth surface.', '<b>Ruled 2026-09-05</b> (the social split)'")
    html = html.replace('min-height: 3860px', 'min-height: 3990px')
    return html

if __name__ == '__main__':
    import json
    diag = json.load(open(os.path.join(OUT, 'diag.json'))) if os.path.exists(os.path.join(OUT, 'diag.json')) else {}
    for name, fn in [('H1 - Ordinary Sunday Generous', H1), ('H2 - Social Week Two Treatments', H2), ('P1 - Places From Friends', P1)]:
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
    open(os.path.join(OUT, 'H0 - Ledger and Decisions.dc.html'), 'w').write(H0(diag)); print('wrote H0')
