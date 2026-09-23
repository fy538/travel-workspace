"""04 - C · Through my people: the From friends scope, sparse and dense, nearby and elsewhere; the Print Room opened from
the scope with three registers distinguished; a withdrawal; no supply in a sub-scope. Fixture copy only."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, compare2, body, facepile
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, share_card, author_row
from gen_places import scope_header, map_wash, branch, places_phone, ICON_TIDE
from gen_merge import tbl, daycap, page
from gen_placeskit import event_stub, question_control, STAMP, hh, OUT, withdrawn_line, elsewhere_band
from gen_places02 import notecol, plan_pair
from gen_seam import chip

def qc(tail='BACK TO ALL OF NEW YORK', friends=True):
    return question_control('New York, now', 'NEW YORK', friends=friends).replace('CLEAR &rarr; BACK TO NEW YORK', tail)

MAYA = share_card('M', 'Maya', 'THURSDAY &middot; FRIENDS &middot; THROUGH SUNDAY', 'The side room was my favorite.', 150, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'THE HARBOR PRINT ROOM &middot; RED HOOK &middot; <i>ROOMS REMADE</i> THROUGH SUNDAY', 'The Print Room')
def theo_row(last=True):
    return arow('Theo &middot; the greenmarket &middot; <span style="color: #6E6862;">&ldquo;bread gone by ten&rdquo; &middot; Tuesday &middot; may-use</span>', avatars=['T'], last=last)
def alex_row(last=True):
    return arow('Alex &middot; Sunset Park &middot; <span style="color: #6E6862;">&ldquo;the pier at sunset&rdquo; &middot; a neighborhood, not a place</span>', avatars=['A'], last=last)
def maya_bakery_row(last=True):
    return arow('Maya &middot; the Sunset Park bakery &middot; <span style="color: #6E6862;">&ldquo;Sundays only, before eleven&rdquo; &middot; Friday</span>', avatars=['M'], last=last)

def scope_end(count):
    return (f'<div style="padding: 24px 0 0 0;"><div class="fn" style="color: {ANCHOR};">{count} &middot; THE SCOPE ENDS HERE</div>'
            + '<div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">' + door('Back to all of New York') + door('Everything shared with you, by person') + '</div>'
            + meta('THE SECOND DOOR IS LIFE &middot; PEOPLE: THE RECORD, WITH GRANTS &middot; NO &ldquo;INVITE FRIENDS&rdquo; ENDING', 8) + '</div>')

def sparse_phone():
    inner = scope_header('NEW YORK &middot; FROM FRIENDS', 'What two people made visible, and where &middot; nothing is where anyone is now') + qc()
    inner += gut(MAYA, top=22)
    inner += gut(meta('READING THIS IS A COMPLETE OUTCOME &middot; NO PREAMBLE, NO ENRICHMENT UNLESS IT ADDS &middot; THE PRINT ROOM IS THE ONWARD DESTINATION', 10))
    inner += gut('<div>' + theo_row() + '</div>', top=22)
    inner += elsewhere_band().replace(sect('Elsewhere', top=8), sect('Elsewhere'))
    inner += gut(scope_end('ONE SHARE, ONE NOTE, ONE STATUS'))
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">SPARSE MEANS FEWER ORIGINAL CONTRIBUTIONS, NOT INFLATED PLATES OR MANUFACTURED TALK</div></div>'
    return places_phone(inner, 0)

def dense_svg(h=250):
    return ('<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
            f'<path d="M0 150 Q60 120 110 140 Q170 165 230 120 Q290 85 349 100 L349 {h} L0 {h} Z" fill="rgba(61,80,102,0.10)"/>'
            '<circle cx="84" cy="106" r="9" fill="#1B1714"/><text x="80" y="110" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">M</text>'
            '<text x="100" y="102" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PRINT ROOM</text><text x="100" y="114" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THU &#183; PLACE</text>'
            '<circle cx="64" cy="44" r="9" fill="#1B1714"/><text x="60" y="48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">T</text>'
            '<text x="80" y="40" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE GREENMARKET</text><text x="80" y="52" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">NOTE &#183; TUE &#183; PLACE</text>'
            '<circle cx="262" cy="182" r="30" fill="none" stroke="#1B1714" stroke-width="1.2" stroke-dasharray="3 3"/>'
            '<circle cx="272" cy="172" r="9" fill="#1B1714"/><text x="268" y="176" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">A</text>'
            '<circle cx="246" cy="196" r="9" fill="#1B1714"/><text x="242" y="200" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">M</text>'
            '<text x="120" y="226" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">SUNSET PARK &#183; ALEX + THE BAKERY</text>'
            f'<text x="12" y="{h-10}" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">PLACE &#183; NEIGHBORHOOD &#183; CITY: THEIR PRECISION</text>')

def dense_phone():
    inner = scope_header('NEW YORK &middot; FROM FRIENDS', 'What four people made visible, and where &middot; nothing is where anyone is now') + qc()
    inner += map_wash(250, dense_svg(250), top=14)
    inner += sect('Red Hook', top=22) + gut(MAYA.replace('150px', '110px'))
    inner += sect('Sunset Park') + gut('<div>' + maya_bakery_row(last=False) + alex_row() + '</div>')
    inner += sect('The market') + gut('<div>' + theo_row() + '</div>')
    inner += elsewhere_band().replace(sect('Elsewhere', top=8), sect('Elsewhere'))
    inner += gut(scope_end('FOUR PEOPLE &middot; FIVE THINGS'))
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">DENSE: GROUPED BY WHERE, NOT BY WHO &middot; NO POPULARITY ORDER &middot; NO PER-PERSON SECTIONS</div></div>'
    return places_phone(inner, 0)

def focus_from_friends():
    inner = scope_header('THE HARBOR PRINT ROOM', 'Red Hook &middot; from the friends scope', back=True)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">A print workshop in a former warehouse, with an exhibition on through Sunday.</div>', top=22)
    inner += sect('Maya&rsquo;s line') + gut(author_row('M', 'Maya', 'THURSDAY &middot; FRIENDS &middot; THROUGH SUNDAY') + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">&ldquo;The side room was my favorite.&rdquo;</div>' + meta('HER WORDS, HERS &middot; NOT A REVIEW, NOT A CONSENSUS, NOT A REPORT THAT SHE IS THERE', 8))
    inner += sect('The listing') + gut('<div>' + fact('HOURS', 'Tuesday to Sunday 11&ndash;6, as listed; not checked today.') + fact('THE EXHIBITION', '<i>Rooms Remade</i>, through Sunday. Tickets: not known.', last=True) + '</div>')
    inner += sect('The reading') + gut(u2('One room, before and after reuse', 'The side room Maya means, as a plan: four closed rooms became one.', plan_pair(), meta_t='REUSABLE &middot; NOT MADE FOR YOU, NOT MADE FROM HER WORDS'))
    inner += gut('<div style="display: flex; flex-direction: column; gap: 10px;">' + door('Reply to Maya') + meta('TO MAYA &middot; A HUMAN REPLY &middot; NOT SENT UNTIL YOU SEND IT &middot; NOT A MEMORY', 0) + door('Ask Vesper about the Print Room') + meta('PRIVATE &middot; NOTHING SENT TO ANYONE', 0) + door('Keep', INK) + '</div>', top=30)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">THREE REGISTERS, KEPT APART: HER LINE, THE LISTING, THE READING &middot; TWO RECIPIENTS, NEVER CONFUSED</div></div>'
    return places_phone(inner, 0)

def withdrawal_phone():
    inner = scope_header('NEW YORK &middot; FROM FRIENDS', 'What one person made visible, and where') + qc()
    inner += gut(withdrawn_line(), top=22)
    inner += gut('<div>' + theo_row() + '</div>', top=22)
    inner += elsewhere_band().replace(sect('Elsewhere', top=8), sect('Elsewhere'))
    inner += gut(scope_end('ONE NOTE, ONE STATUS'))
    inner += sect('Still in New York') + gut(u2('The Print Room, and <i>Rooms Remade</i>', 'The venue and its exhibition are listed on their own; the room comparison stands. What Maya added is gone.', meta_t='INDEPENDENT WORLD FACTS SURVIVE &middot; THE SHARE DOES NOT RETURN', door_text='The Print Room'))
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">WITHDRAWAL UPDATES LOCALLY &middot; NOTHING ELSE IS RECOMPOSED &middot; NO ECHO OF WHAT LEFT</div></div>'
    return places_phone(inner, 0)

def nosupply_phone():
    inner = scope_header('RED HOOK &middot; FROM FRIENDS', 'Inside New York &middot; the harbor side', back=True) + qc(tail='BACK TO ALL OF RED HOOK')
    inner += gut(f'<div style="padding: 28px 12px 6px 12px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK2};">Nothing from friends about Red Hook yet.</div><div class="fn" style="color: {ANCHOR}; margin-top: 8px;">THIS SCOPE ONLY &middot; THE WORLD IS NOT EMPTY &middot; NOBODY IS ASKED TO POST</div></div>', top=22)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('All of Red Hook') + door('From friends, all of New York') + '</div>', top=20)
    inner += sect('Red Hook, without anyone') + gut(u2('One room, before and after reuse', 'The Print Room&rsquo;s side room, as a plan.', plan_pair(), meta_t='THE SAME REUSABLE COMPARISON &middot; NO FRIEND NEEDED', door_text='The Print Room'))
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">NO-SUPPLY NAMES THE SCOPE, THEN GETS OUT OF THE WAY</div></div>'
    return places_phone(inner, 0)

def board():
    row1 = [col(sparse_phone(), daycap('FRIDAY 12:20 PM &middot; FROM FRIENDS &middot; SPARSE', '1 &middot; ONE SHARE, ONE NOTE, ONE STATUS', 'Maya&rsquo;s photograph and words lead; Theo at his scale; Dana elsewhere', 'NO AI PREAMBLE &middot; READING IS COMPLETE &middot; AN EQUALLY DISCOVERABLE WAY BACK &middot; NO INVITE ENDING')),
            col(dense_phone(), daycap('THE SAME SCOPE &middot; DENSE', '2 &middot; FOUR PEOPLE, FIVE THINGS', 'Grouped by where, on one semantic map', 'PLACE, NEIGHBORHOOD, CITY = THE PRECISION THEY CHOSE &middot; NO POPULARITY ORDER, NO PER-PERSON SECTIONS')),
            col(focus_from_friends(), daycap('THE PRINT ROOM, OPENED FROM THE SCOPE', '3 &middot; THREE REGISTERS KEPT APART', 'Her line, the listing, the reading; two recipients, never confused', 'REPLY TO MAYA &ne; ASK VESPER &middot; NEITHER AUTO-SENDS &middot; A HUMAN REPLY IS NOT A MEMORY')),
            notecol('Ordinary sharing, an absent friend&rsquo;s perspective, the world beyond', [
                ('1 &middot; VALUE BEFORE ACTION', N('Maya&rsquo;s photograph and five words. That is the whole value; nothing paraphrases her and nothing manufactures an insight from her. The scope says who made what visible and at which precision, and says plainly that nothing is where anyone is now.')),
                ('2 &middot; WHY THIS LEAD, WHY THIS ASSORTMENT', N('The person chose the friends question, so authorized human material leads. Maya&rsquo;s share is the one original contribution with a photograph; Theo&rsquo;s note is a line because it is a line. Dense is not more plates: it is the same material grouped by where it is, with the map carrying the density.')),
                ('3 &middot; WHAT THE MAP ADDS, WHAT IT CANNOT PLOT', N('Marks at the precision each person chose: two places, one neighborhood outline. Dana&rsquo;s status is city precision and is never a pin; it lives in the Elsewhere band as a doorway into Sorrento (05). No mark is where anyone is.')),
            ])]
    row2 = [col(withdrawal_phone(), daycap('VARIATION &middot; MAYA TAKES IT BACK', '4 &middot; WITHDRAWAL', 'An honest line; the venue and the reading survive on their own', 'LOCAL UPDATE &middot; DEPENDENT ENRICHMENT GOES WITH IT &middot; THE SHARE NEVER RETURNS')),
            col(nosupply_phone(), daycap('VARIATION &middot; A SUB-SCOPE WITH NOTHING', '5 &middot; NO SUPPLY, FROM FRIENDS', 'Says what is unavailable here, then the world without anyone', 'NAMES THE SCOPE &middot; NEVER &ldquo;NOTHING EXISTS&rdquo; &middot; NEVER AN ENTRANCE FEE')),
            notecol('The opened detail, withdrawal, the supply', [
                ('4 &middot; THE OPENED DETAIL', N('The subject is the Print Room, opened with Maya&rsquo;s line carried in as context. Three registers are typographically distinct and separately sourced: her words (serif, attributed), the listing (fact rows), the reading (a bare unit with the plan pair). Reply and Ask have different recipients and neither sends anything until asked to. Back returns to the friends scope at the same position.')),
                ('5 &middot; SUPPLY TYPE, PER UNIT', tbl(['UNIT', 'SUPPLY', 'WHAT THAT MEANS'], [
                    ['Maya&rsquo;s share (H1)', 'Attributed human material', 'Her photograph and words, under her grant, through Sunday; withdrawable'],
                    ['Theo&rsquo;s note', 'Attributed human material &middot; may-use', 'One line at its scale; rendered only where it changes a place&rsquo;s reading'],
                    ['Dana&rsquo;s status (H2)', 'Attributed &middot; city precision', 'A doorway, never a coordinate; expires with her return'],
                    ['The Print Room listing', 'Permitted existing facts', 'Survives withdrawal because it never depended on the share'],
                    ['The room comparison', 'Reusable enrichment', 'Survives withdrawal for the same reason']])),
                ('THE SOCIAL SPLIT, HELD', N('Casual spatial sharing lives here, in a scope the person chose. Addressed material (Dana&rsquo;s &ldquo;keep Sunday morning for me&rdquo;) lands on Home, not here. The people record is Life&rsquo;s, one door away. Nothing on this board sends, invites, or counts.')),
            ])]
    html = page(1900, hh('04', 4600), f'{STAMP} &middot; 04 &middot; C &middot; THROUGH MY PEOPLE', '04 &middot; C &middot; Can I enjoy ordinary sharing, find an absent friend&rsquo;s perspective, and explore beyond friends without pressure?',
                'Situation C from the brief: the same world with the shared overlays (H1 is Maya&rsquo;s share about the Print Room; H2 is Dana&rsquo;s city-level Sorrento status), the person having chosen From friends. Sparse and dense on one semantic map; the Print Room opened with three registers kept apart; a withdrawal; a sub-scope with no supply. Everything descends from RH1 and the social split of 2026-09-05.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">WITHDRAWAL, AND NOTHING IN A SUB-SCOPE</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">What leaves, leaves cleanly; what is absent is named</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '04 - C - Through My People.dc.html'), 'w').write(html); print('wrote 04', len(html))
