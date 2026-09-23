"""03 - B · Something Saturday evening: the question made visible; W2 leads; W4 as a different kind of evening; W1 honestly
moved to another time; the W2 occurrence opened with a labelled provider continuation; the return; the question changed."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, compare2, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact
from gen_places import scope_header, map_wash, branch, places_phone, ICON_TIDE, ICON_HALL
from gen_merge import tbl, daycap, page
from gen_placeskit import event_stub, question_control, STAMP, hh, OUT
from gen_places02 import notecol, plan_pair, widening
from gen_seam import chip

Q = 'Saturday evening'
def qc(q=Q, tail='CLEAR &rarr; BACK TO NEW YORK, NOW'):
    return question_control(q, 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', tail)

def lead_w2():
    inner = (f'<div class="kick" style="color: {GOLDD};">SATURDAY &middot; 7&ndash;9 PM &middot; CANAL HALL</div>'
             + f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; margin-top: 6px;">The listening hour: two hours in the hall&rsquo;s back room, one recording played end to end, the lights down.</div>'
             + sup('Admission $12 at the door, as listed. The hall seats about sixty; there is no bar. Doors at 6:45.', INK2)
             + meta('WHAT IT IS, FROM THE HALL&rsquo;S OWN LISTING &middot; WHETHER TICKETS REMAIN IS NOT KNOWN AND NOT CLAIMED', 8)
             + door('This Saturday&rsquo;s hour'))
    return card(inner)

def w4_evening():
    return u2('The pier at sunset, Sunset Park', 'A different kind of evening: outdoors, free, unscheduled. Sunset is 7:04; what the pier is like after dark is not established, and neither is the walk from the bakery.',
              meta_t='A PUBLIC PLACE, NOT AN EVENT &middot; NO WALKING TIME, NO LIGHTING CLAIM, NO FORECAST INVENTED', door_text='The pier')

def not_this_window():
    return ('<div>' + row('The Print Room &middot; <span style="color: #6E6862;">closes at 6 &middot; Sunday afternoon instead</span>', mark='hollow')
            + row('The greenmarket &middot; <span style="color: #6E6862;">Saturday morning &middot; not an evening</span>', mark='hollow', muted=True, last=True) + '</div>'
            + meta('SAID EXPLICITLY, NOT QUIETLY TREATED AS SATURDAY-EVENING INVENTORY', 8))

def adjustments():
    return ('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Saturday afternoon instead') + door('Another neighborhood') + door('Ask a different question') + '</div>'
            + meta('THREE DELIBERATE ADJUSTMENTS &middot; NO FILTER DASHBOARD &middot; EACH ONE NAMES THE NEW QUESTION', 8))

def field_phone(return_strip=False):
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:14 PM')
    if return_strip:
        inner += f'<div style="margin: 10px 22px 0 22px; padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">BACK &middot; SATURDAY EVENING KEPT &middot; THE HOUR STILL SELECTED &middot; SAME POSITION</span></div>'
    inner += qc()
    inner += gut(lead_w2(), top=22)
    inner += sect('A different kind of evening') + gut(w4_evening())
    inner += sect('Not this window') + gut(not_this_window())
    inner += gut(adjustments(), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">TWO THINGS FIT THE QUESTION &middot; TWO ARE SAID NOT TO &middot; NO CHECKLIST BEFORE READING</div></div>'
    return places_phone(inner, 0)

def svg_b(h=260):
    return ('<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
            f'<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120 L349 {h} L0 {h} Z" fill="rgba(61,80,102,0.10)"/>'
            '<rect x="172" y="38" width="12" height="12" rx="2" fill="none" stroke="#1B1714" stroke-width="1.4"/><path d="M172 43 H184" stroke="#1B1714" stroke-width="1.4"/><text x="190" y="44" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">CANAL HALL &#183; SAT 7&#8211;9</text><text x="190" y="56" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE LISTENING HOUR</text>'
            '<circle cx="262" cy="192" r="26" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="252" cy="206" r="5" fill="#B0853A"/>'
            '<text x="140" y="236" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PIER &#183; SUNSET 7:04</text>'
            '<circle cx="112" cy="118" r="7" fill="none" stroke="#B5AFA5" stroke-width="1.4"/><text x="124" y="114" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#B5AFA5">THE PRINT ROOM</text><text x="124" y="126" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#B5AFA5">CLOSES AT 6 &#183; NOT THIS WINDOW</text>'
            f'<text x="12" y="{h-10}" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">NO ORIGIN &#183; THE QUESTION GOVERNS WHAT IS INK</text>')

def map_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:14 PM') + qc(tail='MAP &middot; THE SAME QUESTION')
    inner += map_wash(260, svg_b(260), top=14)
    inner += gut(meta('SAME SET AS THE FIELD &middot; WHAT DOES NOT FIT THE WINDOW IS GHOST INK, NOT REMOVED FROM THE WORLD', 10))
    inner += sect('In this view', top=22) + gut('<div>' + row('The listening hour &middot; <span style="color: #6E6862;">Canal Hall &middot; Sat 7&ndash;9 &middot; $12</span>', mark='dashed', color=INK) + row('The pier at sunset &middot; <span style="color: #6E6862;">Sunset Park &middot; a public place</span>', mark='hollow') + row('The Print Room &middot; <span style="color: #6E6862;">closes at 6 &middot; Sunday afternoon instead</span>', mark='hollow', muted=True, last=True) + '</div>')
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">TOGGLE PRESERVES THE QUESTION, SCOPE AND SET</div></div>'
    return places_phone(inner, 0)

def occurrence_phone():
    inner = scope_header('THE LISTENING HOUR', 'Saturday 13 &middot; 7&ndash;9 PM &middot; Canal Hall', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">One recording, played end to end, in the hall&rsquo;s back room with the lights down.</div>'
                 + sup('This Saturday&rsquo;s occurrence. Doors 6:45 &middot; admission $12 at the door, as listed &middot; about sixty seats &middot; no bar.', INK2), top=22)
    inner += sect('What is known, and not') + gut('<div>' + fact('THE VENUE', 'Canal Hall, on the canal side. The hall and this hour are different things; the hall has other nights.') + fact('AVAILABILITY', 'Not known. The listing says nothing about remaining admission; Vesper does not guess.') + fact('THE WAY THERE', 'No origin is set, so no route or time is given.', last=True) + '</div>')
    inner += gut(f'<div style="border: 1px solid rgba(27,23,20,0.14); border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px;"><span class="kickm">EXTERNAL &middot; CANAL HALL&rsquo;S OWN PAGE</span>{door("Details and admission, at the hall")}<span class="fn" style="color: {ANCHOR};">A LABELLED PROVIDER CONTINUATION &middot; NOT VESPER BOOKING &middot; OPENS OUTSIDE</span></div>', top=26)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Ask Vesper about the hour') + door('Keep', INK) + '</div>', top=22)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">THE EXACT OCCURRENCE, NOT THE VENUE &middot; UNKNOWN LIMITS THE CLAIM, NOT THE DESCRIPTION</div></div>'
    return places_phone(inner, 0)

def changed_question_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:15 PM') + qc('Saturday afternoon', tail='A NEW SET &middot; THE NEW QUESTION GOVERNS')
    inner += gut(f'<div style="padding: 6px 10px; border-radius: 8px; background: {WASH};"><span class="fn" style="color: {MUTE};">THE QUESTION CHANGED &middot; THIS IS A NEW RESULT SET, SAID SO &middot; THE EVENING SET IS NOT RELABELLED</span></div>', top=10)
    inner += gut(u2('The Print Room, and <i>Rooms Remade</i>', 'Open until six on Saturday, which the afternoon supports. The room comparison is the reason to go; tickets for the exhibition are not known.', plan_pair(), meta_t='HOURS SUPPORT THE WINDOW &middot; NOW INK', door_text='The Print Room'), top=22)
    inner += sect('Also Saturday afternoon') + gut('<div>' + event_stub('SAT 13', 'The greenmarket, until one', 'Saturday 8&ndash;1', 'a weekly series', 'THE LAST HOUR OF IT FALLS INSIDE THE AFTERNOON &middot; SAID SO') + '<div style="height: 10px;"></div>' + branch(ICON_TIDE, 'The pier and the bakery, Sunset Park', 'Low water 2:40 to 5', 'the way between them is not established') + '</div>')
    inner += sect('Not this window') + gut('<div>' + row('The listening hour &middot; <span style="color: #6E6862;">7&ndash;9 PM &middot; Saturday evening instead</span>', mark='hollow', muted=True, last=True) + '</div>')
    inner += gut(adjustments().replace('Saturday afternoon instead', 'Saturday evening instead'), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">SAME WORLD, DIFFERENT QUESTION &middot; INK AND GHOST TRADE PLACES &middot; NOTHING INVENTED TO FILL THE AFTERNOON</div></div>'
    return places_phone(inner, 0)

def board():
    row1 = [col(field_phone(), daycap('FRIDAY 12:14 PM &middot; &ldquo;SOMETHING SATURDAY EVENING&rdquo;', '1 &middot; THE QUESTION, VISIBLE AND EDITABLE', 'The hour leads; the pier is a different evening; two things are said not to fit', 'NO FEASIBILITY CHECKLIST BEFORE READING &middot; &ldquo;TICKETS AVAILABLE&rdquo; WITHHELD &middot; THREE ADJUSTMENTS, NO DASHBOARD')),
            col(map_phone(), daycap('THE SAME QUESTION &middot; MAP', '2 &middot; THE MAP FORM', 'What fits the window is ink; what does not is ghost', 'THE PRINT ROOM STAYS ON THE MAP IN GHOST &middot; THE WORLD IS NOT EDITED TO MATCH THE QUESTION')),
            col(occurrence_phone(), daycap('THE HOUR OPENED', '3 &middot; THE EXACT OCCURRENCE', 'Substance, date, venue, what is not known, then the way out', 'PROVIDER CONTINUATION LABELLED AS EXTERNAL &middot; NOT VESPER BOOKING &middot; KEEP AND ASK PRESENT, NOT PRESSED')),
            notecol('Search, time, comparison, relevance, uncertainty', [
                ('1 &middot; VALUE BEFORE ACTION', N('One paragraph that says what the listening hour actually is, from the hall&rsquo;s own listing, with its time and price. The person can decide whether it is their kind of evening without tapping anything. The pier is offered as a genuinely different evening, not a second event.')),
                ('2 &middot; WHY THIS LEAD, WHY THIS ASSORTMENT', N('The question names a window; the hour is the one dated thing inside it, so it leads. The pier fits by kind, not by schedule. The Print Room and the market are in the world but not in the window, and the page says so explicitly instead of quietly dropping them or quietly including them. That is the honest form of &ldquo;relevance&rdquo;.')),
                ('3 &middot; WHAT THE MAP ADDS, WHAT IT CANNOT PLOT', N('The map plots the hour as a dated square and the pier as a stop inside its area. The Print Room stays on the map in ghost ink with its reason: the question governs what is ink, not what exists. No origin, so no route; sunset is a time, not a light level.')),
            ])]
    row2 = [col(field_phone(return_strip=True), daycap('BACK FROM THE HOUR', '4 &middot; THE RETURN', 'Saturday evening kept; the hour still selected; same position', 'THE QUESTION IS PART OF THE RETURN CONTEXT &middot; NOTHING IS MARKED VIEWED &middot; NO NEW FEED')),
            col(changed_question_phone(), daycap('VARIATION &middot; THE QUESTION CHANGES', '5 &middot; SATURDAY AFTERNOON INSTEAD', 'A new result set, said so; ink and ghost trade places', 'BRIEF &sect;6.2 &middot; A DELIBERATE CHANGE OF TIME ESTABLISHES A NEW SET &middot; THE OLD ONE IS NOT RELABELLED')),
            notecol('The opened detail, the return, the supply', [
                ('4 &middot; THE OPENED DETAIL', N('The subject is this Saturday&rsquo;s occurrence, not Canal Hall. The page gives substance, date, venue and what is not known before any action. The continuation is the hall&rsquo;s own page, labelled external, which is where admission is settled; Vesper does not book and does not pretend to. Back restores the question, the selection and the position.')),
                ('5 &middot; SUPPLY TYPE, PER UNIT', tbl(['UNIT', 'SUPPLY', 'WHAT THAT MEANS'], [
                    ['The listening hour (W2)', 'Permitted existing facts', 'The hall&rsquo;s listing: date, window, price, room, doors; availability withheld'],
                    ['The pier at sunset (W4)', 'Permitted existing facts + a sunset time', 'No walking time, lighting or forecast; the uncertainty is stated'],
                    ['&ldquo;Not this window&rdquo;', 'Viewer-neutral selection', 'Hours compared with the question; the reason is printed'],
                    ['The adjustments', 'Structured state', 'Three named questions; each establishes a new set when taken']])),
                ('THE CANON DELTA THIS BOARD LEANS ON', N('The anatomy says the page ends when the next unit does not beat silence. Here the page ends with two things that fit and two that do not, and then names its adjustments. That is the &ldquo;finite first collection, deliberate widening&rdquo; reading the brief asks for; 08 records it as the amendment it is.')),
            ])]
    html = page(1900, hh('03', 4200), f'{STAMP} &middot; 03 &middot; B &middot; SOMETHING SATURDAY EVENING', '03 &middot; B &middot; How do search, time, comparison, relevance and uncertainty work together?',
                'Situation B from the brief: the same world as 02 with an explicit question. The question is visible and editable; the hour leads with what it is; the pier is a different kind of evening; the Print Room and the market are said not to fit rather than quietly dropped; the exact occurrence opens with a labelled provider continuation; the return keeps the question; and changing the question is drawn as the new result set it is.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE RETURN, AND THE QUESTION CHANGED</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Back keeps the question; a new question is a new set</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '03 - B - Something Saturday Evening.dc.html'), 'w').write(html); print('wrote 03', len(html))
