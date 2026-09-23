"""02 - A · The ordinary New York opening: no query, no history, no shares. The content-led field, its map form, the
map-led alternative on the same evidence, the W1 opening (a stable place with no dossier), the return, and thin supply.
Fixture copy only (the brief's W1–W5 mapped onto the shared world). Nothing here is ruled."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, collapsed, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact
from gen_places import scope_header, map_wash, branch, cont_rows, places_phone, ICON_TIDE, ICON_HALL, ICON_MARKET, ICON_BOOK
from gen_merge import tbl, blk, daycap, page
from gen_placeskit import event_stub, question_control, thin_end, no_supply, STAMP, hh, OUT, sheet
from gen_merge import notecol as _nc
import gen_placeskit as pk

def notecol(t, blocks, w=520): return _nc(t, blocks, w=w)

# ───────────────────────────── the room comparison (W5): two small plans ─────────────────────────────
def plan_pair():
    def plan(label, year, inner):
        return (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px;"><svg width="100%" height="96" viewBox="0 0 160 96" fill="none" style="display: block; background: {WASH}; border-radius: 8px;">{inner}</svg>'
                f'<div style="display: flex; justify-content: space-between;"><span class="kickm">{label}</span><span class="fn" style="color: {ANCHOR};">{year}</span></div></div>')
    before = ('<rect x="12" y="12" width="136" height="72" stroke="#1B1714" stroke-width="1.4"/><path d="M12 48 H148" stroke="#1B1714" stroke-width="1.2"/>'
              '<path d="M46 12 V48 M80 12 V48 M114 12 V48" stroke="#1B1714" stroke-width="1.2"/><path d="M46 48 V84 M114 48 V84" stroke="#1B1714" stroke-width="1.2"/>'
              '<text x="66" y="70" font-family="JetBrains Mono, monospace" font-size="8" letter-spacing="0.8" fill="#8F877C">CORRIDOR</text>')
    after = ('<rect x="12" y="12" width="136" height="72" stroke="#1B1714" stroke-width="1.4"/><path d="M12 48 H60 M100 48 H148" stroke="#1B1714" stroke-width="1.2"/>'
             '<path d="M60 44 V52 M100 44 V52" stroke="#B0853A" stroke-width="2" stroke-linecap="round"/><path d="M114 12 V48" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.5"/>'
             '<text x="30" y="72" font-family="JetBrains Mono, monospace" font-size="8" letter-spacing="0.8" fill="#8A6628">ONE ROOM &#183; A THRESHOLD</text>')
    return f'<div style="display: flex; gap: 12px; margin-top: 10px;">{plan("BEFORE", "1962 &middot; PLAN", before)}{plan("AFTER", "2024 &middot; PLAN", after)}</div>'

def lead_w5():
    return u2('One room, before and after reuse', 'The Print Room&rsquo;s side room was a corridor and four closed rooms; the wall that separated them is now a threshold. Seeing the two plans is already the payoff; the exhibition is the optional way further in.',
              plan_pair(), meta_t='<i>ROOMS REMADE</i> &middot; THE HARBOR PRINT ROOM, RED HOOK &middot; THROUGH SUNDAY &middot; REUSABLE COMPARISON, NOT MADE FOR YOU', door_text='The Print Room, and the exhibition')

# ───────────────────────────── the collection ─────────────────────────────
def contrasting_set(ghost_w4=False):
    return ('<div>' + event_stub('SAT 13', 'The listening hour at Canal Hall', 'Saturday 7&ndash;9 PM', 'admission $12', 'A DATED EVENT &middot; TICKETS UNKNOWN &middot; THE HALL ALONE IS NOT THE HOUR', 'This Saturday&rsquo;s hour')
            + f'<div style="height: 10px;"></div>' + branch(ICON_TIDE, 'The pier and the bakery, Sunset Park', 'A public waterside walk with a bakery on the same streets', 'the way between them is not established', ghost=ghost_w4) + '</div>')

def market_row():
    return event_stub('SAT 13', 'The greenmarket', 'This Saturday 8&ndash;1', 'a weekly series', 'THIS OCCURRENCE IS LISTED &middot; LATER SATURDAYS ARE NOT CONFIRMED')

def widening(count='FIVE THINGS'):
    return (f'<div style="padding: 16px 0 0 0;"><div class="fn" style="color: {ANCHOR};">THE FIRST COLLECTION ENDS HERE &middot; {count}</div>'
            + '<div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Another neighborhood') + door('Sunday instead') + door('More of Red Hook') + '</div></div>')

def field_phone(return_strip=False):
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:10 PM')
    if return_strip:
        inner += f'<div style="margin: 10px 22px 0 22px; padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">BACK &middot; THE SAME COLLECTION, THE SAME POSITION &middot; NOTHING IS MARKED AS VIEWED</span></div>'
    inner += question_control('New York, now', 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', 'NO QUESTION YET &middot; NOTHING ASKED OF YOU')
    inner += gut(lead_w5(), top=22)
    inner += sect('Also in the city') + gut(contrasting_set())
    inner += sect('This Saturday') + gut('<div>' + market_row() + '</div>')
    inner += gut(widening(), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">NO LOCATION ASKED &middot; NO INTERESTS ASKED &middot; NO RECAP &middot; NO FRIENDS PROMPT</div></div>'
    return places_phone(inner, 0)

# ───────────────────────────── the map form (same set) ─────────────────────────────
def field_svg(h=260):
    return ('<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
            f'<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120 L349 {h} L0 {h} Z" fill="rgba(61,80,102,0.10)"/>'
            # W1 venue (a place, with an exhibition running)
            '<circle cx="112" cy="118" r="7" fill="#1B1714"/><text x="124" y="114" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PRINT ROOM</text><text x="124" y="126" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">RED HOOK &#183; THROUGH SUN</text>'
            # W2 dated event at Canal Hall
            '<rect x="172" y="38" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M172 43 H184" stroke="#1B1714" stroke-width="1.4"/><text x="190" y="44" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">CANAL HALL &#183; SAT 7</text><text x="190" y="56" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE LISTENING HOUR</text>'
            # W3 market, dated
            '<rect x="30" y="80" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M30 85 H42" stroke="#1B1714" stroke-width="1.4"/><text x="48" y="86" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">GREENMARKET &#183; SAT 8&#8211;1</text>'
            # W4 area: Sunset Park outline with the pier stop and the bakery
            '<circle cx="262" cy="192" r="26" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="252" cy="206" r="5" fill="#B0853A"/><circle cx="276" cy="184" r="4" fill="#1B1714"/>'
            '<text x="140" y="236" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">SUNSET PARK &#183; PIER + BAKERY</text>'
            f'<text x="12" y="{h-10}" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">NO ORIGIN &#183; NOTHING IS &#8220;NEAR YOU&#8221;</text>')

def map_rows(ghost=False):
    c = MUTE if ghost else INK
    return ('<div>' + row('The Print Room &middot; <span style="color: #6E6862;">Red Hook &middot; <i>Rooms Remade</i> through Sunday</span>', mark='solid', color=INK)
            + row('Canal Hall &middot; <span style="color: #6E6862;">the listening hour &middot; Sat 7&ndash;9</span>', mark='dashed', color=INK)
            + row('The greenmarket &middot; <span style="color: #6E6862;">Sat 8&ndash;1 &middot; this occurrence</span>', mark='dashed', color=INK)
            + row('The pier and the bakery &middot; <span style="color: #6E6862;">Sunset Park &middot; an area</span>', mark='hollow', last=True) + '</div>')

def map_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:10 PM')
    inner += question_control('New York, now', 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', 'MAP &middot; THE SAME FIVE THINGS').replace('>Map</span>', ' style="background: #1B1714; color: #FBF7EC;">Map</span>')
    inner += map_wash(260, field_svg(260), top=14)
    inner += gut(meta('THE SAME SET, THE SAME REVISION &middot; PANNING IS INSPECTION &middot; THE ROOM COMPARISON HAS NO POINT AND STAYS BELOW', 10))
    inner += sect('In this view', top=22) + gut(map_rows())
    inner += gut(u2('One room, before and after reuse', 'The comparison that led the field is still the first thing here; it is a reading, not a place.', meta_t='NO COORDINATE &middot; NEVER PLOTTED &middot; W5', door_text='The Print Room'), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">TOGGLE PRESERVES THE QUESTION, SCOPE AND SET &middot; A NEW AREA IS A DELIBERATE ACT</div></div>'
    return places_phone(inner, 0)

def map_led_phone():
    """The comparison the brief asks for: the same evidence, map first. Equally rich; judged on the independent visit it gives."""
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:10 PM')
    inner += map_wash(340, field_svg(340), top=14)
    inner += gut(title('Four places, one comparison, this weekend', 20, 25, 600) + sup('Red Hook has an exhibition through Sunday; Canal Hall has an hour on Saturday night; the greenmarket runs Saturday morning; Sunset Park has the pier and a bakery.'), top=18)
    inner += gut(map_rows(), top=14)
    inner += gut(u2('One room, before and after reuse', 'The Print Room&rsquo;s side room, as a plan: four closed rooms became one.', pk.plan_pair() if hasattr(pk, 'plan_pair') else plan_pair(), meta_t='THE PAYOFF ARRIVES SECOND HERE &middot; THE MAP SPENT THE FIRST VIEWPORT', door_text='The Print Room'), top=26)
    inner += gut(widening(), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">MAP-LED &middot; SAME EVIDENCE &middot; ORIENTATION FIRST, UNDERSTANDING SECOND</div></div>'
    return places_phone(inner, 0)

# ───────────────────────────── W1 opened: a stable place with no dossier ─────────────────────────────
def focus_phone():
    inner = scope_header('THE HARBOR PRINT ROOM', 'Red Hook &middot; a venue &middot; no dossier yet', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">A print workshop in a former warehouse, with an exhibition on through Sunday.</div>'
                 + sup('Tuesday to Sunday 11&ndash;6 &middot; listed hours, not checked today &middot; tickets for the exhibition unknown', MUTE), top=22)
    inner += sect('Rooms Remade &middot; through Sunday') + gut(u2('One room, before and after reuse', 'The side room as a plan: four closed rooms and a corridor became one room; the wall is a threshold.', plan_pair(), meta_t='THE SAME COMPARISON THAT LED THE FIELD &middot; SHOWN ONCE, HERE AT ITS PLACE'))
    inner += sect('Facts') + gut('<div>' + fact('WHERE', 'Van Brunt Street, Red Hook. The B61 stops two blocks away; the ferry landing is a nine-minute walk.') + fact('WHAT IS NOT KNOWN', 'Whether the exhibition is ticketed, and today&rsquo;s hours. Nothing here is inferred from that absence.', last=True) + '</div>')
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('The exhibition, on its own page') + door('Ask Vesper about the Print Room') + door('Keep', INK) + '</div>', top=30)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">THE OBJECT PAGE IS ENTITY&rsquo;S (RE2) &middot; HONEST SPARSE &middot; NO RELATIONSHIP TRACE, NO LECTURE ABOUT IT</div></div>'
    return places_phone(inner, 0)

def thin_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:10 PM')
    inner += question_control('New York, now', 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', 'NO QUESTION YET')
    inner += gut(lead_w5(), top=22)
    inner += sect('This Saturday') + gut('<div>' + market_row() + '</div>')
    inner += gut(widening('TWO THINGS'), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">THIN SUPPLY &middot; TWO REAL THINGS AND THE WAY ONWARD &middot; NO PADDING, NO PROMPT, NO &ldquo;NOTHING HERE&rdquo;</div></div>'
    return places_phone(inner, 0)

# ───────────────────────────── the board ─────────────────────────────
SUPPLY = [['The room comparison (W5)', 'Reusable enrichment', 'Made once for the exhibition; shown to anyone; not made for this viewer'],
          ['The Print Room and its exhibition (W1)', 'Permitted existing facts', 'Listing, hours as listed, the exhibition&rsquo;s dates; tickets unknown stays unknown'],
          ['The listening hour (W2)', 'Permitted existing facts', 'A dated occurrence: date, window, price; availability withheld'],
          ['The greenmarket (W3)', 'Permitted existing facts', 'This Saturday&rsquo;s occurrence; the series identity is separate'],
          ['The pier and the bakery (W4)', 'Viewer-neutral selection', 'Two places in one area; no route claimed because none is established'],
          ['The order of the five', 'Viewer-neutral selection', 'Nothing about this person is held; the order is the evidence&rsquo;s, not a taste']]

def board():
    row1 = [col(field_phone(), daycap('FRIDAY 12:10 PM &middot; NO QUERY, NO HISTORY, NO SHARES', '1 &middot; THE FIELD, CONTENT-LED', 'The room comparison leads; four things follow; the collection ends', 'THE BASELINE (&sect;6.1) &middot; NO LOCATION ASKED &middot; NO INTERESTS ASKED &middot; THE MAP ONE TAP AWAY')),
            col(map_phone(), daycap('THE SAME MOMENT &middot; MAP', '2 &middot; THE MAP FORM', 'The same five things, plotted where they can be', 'SAME SET, SAME REVISION &middot; TWO DATED SQUARES, ONE AREA, ONE VENUE &middot; THE READING STAYS BELOW')),
            col(map_led_phone(), daycap('THE COMPARISON &middot; SAME EVIDENCE', '3 &middot; THE MAP-LED ALTERNATIVE', 'Orientation first; the payoff arrives second', 'EQUALLY RICH &middot; JUDGED ON THE INDEPENDENT VISIT IT GIVES, NOT ON THE MAP')),
            notecol('What the person receives before any action', [
                ('1 &middot; VALUE BEFORE ACTION', N('Two plans of one room, and one sentence that says what changed. That is complete on its own: nothing has to be opened, saved, or visited for it to have been worth the open. The four things after it are different in kind (a dated hour, an outdoor pair, a market morning), not four more of the same.')),
                ('2 &middot; WHY THIS LEAD, WHY THIS ASSORTMENT', N('The comparison is the one unit in the packet that is understandable at a glance and reusable for anyone; it earns the first viewport without a question. The listening hour and the pier pair contrast in character, and the market is time-specific material distinct from its series. Nothing is called &ldquo;for you&rdquo;; no order is a taste.')),
                ('3 &middot; WHAT THE MAP ADDS, WHAT IT CANNOT PLOT', N('The map adds where: two dated squares, one venue, one area outline. It cannot plot the comparison, which has no coordinate and stays a reading below. There is no origin, so nothing is &ldquo;near you&rdquo;. Phone 3 asks the brief&rsquo;s question honestly: with the same evidence, does map-first give a better independent visit? On this evidence it spends the first viewport on orientation and delays the payoff.')),
            ])]
    row2 = [col(focus_phone(), daycap('W1 OPENED', '4 &middot; A STABLE PLACE WITH NO DOSSIER', 'Identity, the exhibition, two facts, what is not known', 'PLACES OPENS THE ENTITY PAGE (RE2); IT DOES NOT REDRAW IT &middot; THE COMPARISON SHOWN ONCE, HERE')),
            col(field_phone(return_strip=True), daycap('BACK', '5 &middot; THE RETURN', 'The same collection, the same position', 'NOTHING IS MARKED AS VIEWED &middot; NOTHING WAS KEPT BY LOOKING &middot; NO NEW FEED AFTER BACK')),
            col(thin_phone(), daycap('VARIATION &middot; THIN SUPPLY', '6 &middot; TWO REAL THINGS', 'The comparison and the market; then the way onward', 'NO PADDING &middot; NO INVITE &middot; THE WORLD IS NOT DECLARED EMPTY')),
            notecol('The opening, the return, and the supply', [
                ('4 &middot; THE OPENED DETAIL', N('The subject is the Print Room itself, not the exhibition; the exhibition is its continuation and has its own page. The page is honestly sparse: listed hours say they are listed, tickets stay unknown, and the absence of a relationship trace is silent rather than explained. The optional next action is the exhibition; Keep and Ask are present, not pressed.')),
                ('5 &middot; SUPPLY TYPE, PER UNIT', tbl(['UNIT', 'SUPPLY', 'WHAT THAT MEANS'], SUPPLY)),
                ('THE NO-LOCATION DEFAULT', N('Every phone on this board runs with New York as a selected scope, not a measured one. The sub-line says so. The map has no origin mark. Nothing changes if location is later granted except that an origin may appear and distances may be stated.')),
            ])]
    html = page(1900, hh('02', 5000), f'{STAMP} &middot; 02 &middot; A &middot; THE ORDINARY NEW YORK OPENING', '02 &middot; A &middot; What can I enjoy, understand or consider without supplying anything?',
                'Situation A from the brief: no query, no history, no shares. The content-led field on the shared fixture world (the brief&rsquo;s W1&ndash;W5 as new venues in it), its map form, the map-led alternative on the same evidence, the Print Room opened as a stable place with no dossier, the return, and the thin-supply variation. Annotations follow &sect;6.4 of the brief.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE OPENING, THE RETURN, THIN SUPPLY</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">One continuation and its return; then less</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '02 - A - The Ordinary Opening.dc.html'), 'w').write(html); print('wrote 02', len(html))
