"""01 · revised (§8.9, §8.10, §8.11): the kit reflects the tested compositions. Composition guidance instead of quotas;
the control model; consumer units with illustrations; states; corrected code labels; the proposed type change flagged."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import N, arow, facepile
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, blk, spec, cell
from gen_placeskit import GRID_CSS, swatches, grammar_map, TOKENS
from gen_p2_common import *
from gen_p2_02 import u_hour, u_noodles, lead_two_piers, plan_pair
from gen_p2_04 import maya_print_room
from gen_artifact import ways_seq_card

def sheet(w, h, kick, ttl, sub, body_html, foot=FOOT):
    return (HEAD.replace('</helmet>', GRID_CSS + FN11 + '</helmet>') + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, ttl, sub) + body_html + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)
def region(t, cells):
    return f'<div class="shead" style="margin: 26px 0 14px 0;"><span>{t}</span><span class="rule"></span></div><div class="grid">' + ''.join(cells) + '</div>'
def sp(inner): return consumer(spec(inner))

def type_change():
    rows = [('SUPPORTING', f'<div style="font-size: 14px; line-height: 19px; color: {MUTE};">Hand-pulled at the counter; no wait before 12:30. Three blocks from Canal Hall.</div>', 'SANS 14/19 &middot; WAS 13/18 AND 12.5/17 &middot; PROPOSED TOKEN CHANGE FOR PLACES'),
            ('DATE, TIME, PRICE', when_line('Saturday 7:15 PM &middot; $12 at the door'), 'SANS 14/19 INK2 &middot; NEVER 10PX MONO FOR A FACT THE DECISION NEEDS'),
            ('UNCERTAINTY', unc('Seats left haven&rsquo;t been confirmed.'), 'SANS 13/18 MUTE &middot; IN THE PERSON&rsquo;S WORDS, ONCE'),
            ('SOURCE', src('From the noodle bar&rsquo;s own listing, posted 5:40 PM'), 'MONO 11 ANCHOR &middot; WAS 10 &middot; ONLY WHERE THE SOURCE MATTERS TO THE DECISION'),
            ('KICK', '<div class="kick">SATURDAY NIGHT &middot; FREE</div>', 'MONO 10/700 GOLD-DEEP &middot; UNCHANGED')]
    return '<div style="display: flex; flex-direction: column; gap: 14px; padding: 10px 22px 0 22px;">' + ''.join(f'<div style="display: flex; flex-direction: column; gap: 4px;"><span class="kickm">{k}</span>{h_}<span class="fn" style="color: {ANCHOR};">{s}</span></div>' for k, h_, s in rows) + '</div>'

GUIDE = [('ONE LEAD', 'One thing leads because it is the most worth seeing, not because a rule says one. It is a card when it is a coherent thing (a possibility, a discovery, a share); the plans of a room are not a lead by default.'),
         ('A COHERENT FIRST COLLECTION', 'Varied reasons to engage, grouped by a heading a person would use (This weekend, Any day, Worth seeing). No item count, no ceremonial ending; the page ends with the ways onward, and further exploration within the same intent is allowed when supply supports it.'),
         ('EXCLUSIONS ARE SELECTIVE', 'A question returns what fits. Something that does not fit appears only when the person asked about it, selected it, relied on it, or would benefit from the alternate time. The map may keep background geography.'),
         ('CONTAINMENT FOR RECOGNITION', 'A card makes a unit recognizable, comparable and actionable. It is not a reward for an internal object category, and not every fact needs one.'),
         ('NOTHING INTERNAL', 'No result-set announcements, no supply economics, no instructions about how to experience a reading, no restoration notes. Material uncertainty stays, in the person&rsquo;s words, once.'),
         ('PICTURES', 'Illustrations, tagged as such on the plate. A friend&rsquo;s picture is theirs; never implied to be a real person&rsquo;s photograph in a fixture.'),
         ('A POSSIBILITY OVER AN EXPLANATION', 'When the packet has a well-chosen possibility, it leads; understanding supports it (which pier, what view, when) rather than competing with it. An explanation earns the lead only by its usefulness.'),
         ('PEOPLE CONTEXT INSIDE THE QUESTION', '&ldquo;With Maya&rdquo; changes relevance within the current question and keeps the hours in force. One authorized reason is enough; nothing is inferred about her. A friend&rsquo;s venue note may inform an occurrence and is labelled as about the venue, never as her sharing or attending it.'),
         ('CONTEXT IS NOT A SCHEDULE', 'Saved places justify relevance, not appointed stops. Maturity shows as timing, a useful connection, a resurfaced place with honest hours, or less effort.')]
def guide():
    return '<div style="display: flex; flex-direction: column; gap: 10px; padding: 8px 22px 0 22px;">' + ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px;"><span class="kickm">{k}</span><span style="font-size: 12.5px; line-height: 17px; color: {INK2};">{t}</span></div>' for k, t in GUIDE) + '</div>'

def illo_gallery():
    kinds = ['room', 'loaf', 'pier', 'hall', 'market', 'quay', 'film', 'noodles', 'library', 'organ', 'table', 'loop', 'terrace']
    return '<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; padding: 8px 22px 0 22px;">' + ''.join(f'<div><div style="border-radius: 10px; overflow: hidden;">{illo(k, 70, 78)}</div><div class="fn" style="color: {MUTE}; margin-top: 3px;">{k.upper()}</div></div>' for k in kinds) + '</div>'

def board():
    A = [cell('tokens', 'EXISTS', spec(swatches()), 'UNCHANGED &middot; ONE PALETTE ACROSS ROOTS'),
         cell('type inside a Places phone', 'PROPOSED', sp(type_change()), 'A TOKEN CHANGE FOR ACCESSIBILITY AND HIERARCHY, FLAGGED: SUPPORTING 13&rarr;14/19, META 10&rarr;11 &middot; ON EVERY REVISED PHONE'),
         cell('composition guidance', 'GUIDANCE', spec(guide()), 'REPLACES THE FIRST EXPORT&rsquo;S QUOTA-LIKE LAWS &middot; THE KIT DESCRIBES THE TESTED COMPOSITIONS; IT DOES NOT CONSTRAIN THEM'),
         cell('illustrations', 'FIXTURE MEDIA', spec(illo_gallery()), 'THIRTEEN SCENES, TWO OR THREE INKS, A GRAIN &middot; EXPLICITLY ILLUSTRATIVE &middot; A PLATE CARRIES A SMALL TAG')]
    B = [cell('header', 'EXISTS', sp(header('NEW YORK', 'Friday') + header('The Harbor Print Room', 'Red Hook', back=True) + header('SORRENTO', 'From New York &middot; before any visit')), 'CITY, ONE LINE, SEARCH, MAP &middot; MAP IS HERE ONLY &middot; NO MEASUREMENT OR ORIGIN TALK'),
         cell('the question line, and the way in to friends', 'PROPOSED', sp(question_line() + question_line('Saturday evening') + question_line('Saturday evening', ctx='From friends') + question_line('Saturday evening', ctx='With Maya') + question_line('Somewhere comfortable to sit for an hour') + gut(friends_entry(), top=14)), 'EMPTY = A QUIET, CONCRETE HINT &middot; ONE QUESTION PILL WITH &times; &middot; ONE CONTEXT CHIP IN UMBER &middot; FROM FRIENDS IS ALSO A ROW WITH FACES UNDER THE LEAD, NOT ONLY A SHEET ROW (&sect;9.8)'),
         cell('the sheet', 'PROPOSED', sp(question_sheet()), 'THREE ROWS, WHEN &middot; WHERE &middot; WHO &middot; ANY MAY STAY AS IT IS &middot; SHOW ME IS THE ONLY COMMITMENT'),
         cell('the map', 'EXISTS &middot; ADAPT', spec(grammar_map()), 'UNCHANGED &middot; BACKGROUND GEOGRAPHY MAY STAY WITHOUT BEING A REJECTED RESULT')]
    C = [cell('lead card', 'ADAPT', sp(gut(lead_two_piers(), top=8)), 'A PICTURE, A KICK, A TITLE, THE SUBSTANCE, DATE OR PRICE, ONE UNCERTAINTY, A DOOR &middot; CODE: experience / editorial'),
         cell('event and place units', 'EXISTS &middot; ADAPT', sp(gut('<div>' + u_hour() + u_noodles() + place_unit('quay', 'Red Hook', 'Eighteen minutes on the map; about forty to get in', 'Harbor first, a scheduled way in, a flexible way out.', last=True) + '</div>', top=8)), 'THUMBNAIL OR DATE TILE &middot; TITLE 17 &middot; DATE/PRICE 14 &middot; ONE LINE OF SUBSTANCE &middot; UNCERTAINTY ONCE &middot; CODE: candidate; DATED EVENT = VISUAL TREATMENT, REPRESENTATION TO VERIFY'),
         cell('a friend&rsquo;s share', 'BUILD', sp(gut(maya_print_room(150), top=8)), 'PICTURE, PERSON, WORDS, PLACE, A SECOND PERSON&rsquo;S LINE, REPLY TO THE PERSON &middot; CODE: socialCard IS A SENTENCE STRIP; THIS RECEIVING VIEW IS NOT IMPLEMENTED'),
         cell('a contribution line', 'ADAPT', sp(gut('<div>' + share_line('S', 'Sam', 'Sit on the left side, that&rsquo;s where the speakers are.', 'Canal Hall') + share_line('M', 'Maya', 'Counter seat, the beef one. Twelve sharp or you wait.', 'The noodle counter', kind='noodles', last=True) + '</div>', top=8)), 'PERSON &middot; PLACE &middot; THEIR SENTENCE &middot; A THUMBNAIL WHEN THERE IS A PICTURE &middot; GROUPED BY WHERE')]
    D = [cell('a sequence', 'ADAPT', sp(gut(ways_seq_card('Saturday, if the afternoon is open', [('2:40', 'Low water on the pier', 'The shaded side after two.', 'SUNSET PARK'), ('4:10', 'The bakery, on the way back', 'You saved it Friday. Open till five.', '9 MIN ON FOOT')], meta_t='From the tide table and your saved places'), top=8)), 'COMPOSED FROM STRUCTURED STATE &middot; SAYS WHAT IT IS COMPOSED FROM IN ONE LINE &middot; RECOMPOSED WHEN INPUTS CHANGE'),
         cell('a change', 'BUILD', sp(gut(card(f'<div class="kick" style="color: {OX};">CHANGED &middot; 5:40 PM</div>' + f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 25px; margin-top: 6px;">The noodle bar stops taking orders at 9 tonight</div>' + sup('It won&rsquo;t work for your 9:30; the listening hour is untouched.', INK2) + src('From the noodle bar&rsquo;s own listing') + f'<div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.08);">{title("One thing to decide: where dinner is at 9:30", 15, 20, 600)}</div>' + door('Suggest one to Maya and Alex')), top=8)), 'WHAT CHANGED AND ITS SOURCE &middot; WHAT IT MAKES IMPOSSIBLE &middot; WHAT STANDS &middot; THE SMALLEST DECISION &middot; OXBLOOD ONLY HERE'),
         cell('a prepared message', 'BUILD', sp(gut(card(f'<div class="kick" style="color: {MUTE};">TO MAYA AND ALEX &middot; NOT SENT</div><div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK}; margin-top: 8px;">Would 9:30 at the noodle bar work instead of 8:15?</div>' + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 12px;">{door("Send to Maya and Alex")}{door("Change the wording", MUTE)}</div>') + '<div style="height: 10px;"></div>' + card(f'<div class="kick" style="color: {GOLDD};">SENT TO MAYA AND ALEX &middot; 12:34</div>' + f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 8px;">{facepile(["M", "A"], 24, -6)}<span style="font-size: 13px; color: {MUTE};">Dinner is 8:15 until you change it.</span></div>'), top=8)), 'RECIPIENTS NAMED &middot; SENT ONLY ON TAP &middot; READBACK IN ONE LINE &middot; DEPENDS ON A PRE-PLAN MESSAGE TO PEOPLE (ARRANGEMENTS)'),
         cell('states', 'ADAPT', sp(gut(f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK2};">Nothing from friends around Red Hook yet.</div>' + '<div style="height: 18px;"></div>' + f'<div style="padding: 18px 12px; text-align: center; border: 1px solid {HAIR}; border-radius: 12px;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK2};">This share is no longer available.</div></div>' + '<div style="height: 18px;"></div>' + src('Maya&rsquo;s note about the bakery is gone. The bakery&rsquo;s own hours still say Sunday; the stop stands.'), top=8)), 'EMPTY SCOPE: ONE SENTENCE, THEN THE WORLD &middot; UNAVAILABLE: SHORT, ON THE EXACT ITEM &middot; REPAIRED: ONE LINE ON THE DEPENDENT UNIT')]
    body_html = region('A &middot; TOKENS, TYPE, GUIDANCE, PICTURES', A) + region('B &middot; THE CONTROL MODEL', B) + region('C &middot; UNITS', C) + region('D &middot; SEQUENCES, CHANGES, MESSAGES, STATES', D)
    families = [['candidate', 'PlacesFeedCardView &middot; candidateCard', 'EXISTS', 'event and place units, rows on the map form'],
                ['editorial', 'editorialCard, editorialFeedCard', 'EXISTS', 'lead card when the lead is a discovery; a reading'],
                ['experience', 'experienceCard', 'EXISTS', 'lead card when the lead is a possibility; the sequence (composition producer missing)'],
                ['memory', 'memoryCard', 'EXISTS', 'the record at its place'],
                ['notice', 'noticePromptCard', 'EXISTS', 'a change; a fact row'],
                ['social', 'socialCard (FriendFeedCard)', 'EXISTS AS A SENTENCE STRIP', 'the contribution line; the share card and the share view are NOT implemented'],
                ['semantic unit', 'PlacesSemanticUnitCard', 'EXISTS', 'a bare finding'],
                ['map', 'PlacesMapCanvas, PlacesPinPeekCard, PlaceAreaMap', 'EXISTS', 'the map form; pin peek'],
                ['result-set identity', 'backend/places/result_set.py + map, search, sections, collections', 'EXISTS (SCOPE + QUERY)', 'time and social source are NOT in the identity; map return goes to the scope, not the query'],
                ['question line, chip, sheet', '&mdash;', 'PROPOSED', 'the control model on 03'],
                ['dated event', 'candidate cards carry dates today', 'REPRESENTATION TO VERIFY', 'a visual treatment, not a new noun; verify whether series and occurrence are distinct in the catalog']]
    body_html += ('<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk('CODE FAMILIES &middot; LABELS CORRECTED AGAINST CODE (&sect;8.10)', tbl(['FAMILY', 'WHERE', 'STATUS', 'WHAT IT CARRIES HERE'], families)) + '</div>')
    return sheet(1720, hh('01', 5200), f'{STAMP} &middot; 01 &middot; DESIGN SYSTEM &middot; REVISED 09-07 (&sect;8&ndash;&sect;10)', '01 &middot; The Places kit, as tested',
                 'Reconciled through the three critiques: the kit now describes the compositions on 02 through 07 rather than constraining them. Composition guidance replaces quota-like laws; the control model (header, question line, context chip, sheet) is drawn; units carry illustrations and readable dates and prices; the type change is flagged as a proposal; code labels are corrected against the repository.', body_html)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '01 - Design System.dc.html'), 'w').write(html); print('wrote 01 v2', len(html))
