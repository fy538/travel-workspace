"""10 - States: the Home states Home & Places proved (MP5, C2, HP C3, F4) that the new project never carried,
drawn on the current fixture and in the current forms. Endings (withdrawal, narrowing, block); the occasion
lived through (the push, the silence after); a kept intention returning (with its reasons inline); attributed
friends (two lanes on one axis). Fixture copy only."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
import gen_merge as gm
import gen_seam as gs
import gen_artifact as ga
from gen_generous import caption, col, head, FOOT, N, WEEK_SUN, ending, arow, facepile, collapsed
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact, COLD, author_row
from gen_generous4 import ways_card
from gen_merge import page, daycap, tbl, hh, STAMP
from gen_seam import mark, chip, row_mark
from gen_artifact import ways_seq_card, handoff_artifact, method, PASS

OUT = gm.OUT
HAIR = 'rgba(27,23,20,0.10)'

# ───────────────────────────── row one · endings (MP5 on the current pages) ─────────────────────────────
def sunday_withdrawn():
    """Maya withdrew her bakery share. The sequence recompiles from what remains: no gap where she was, no silhouette."""
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(ways_seq_card('Today, in order', [
        ('1:40', 'Low water on the pier', 'The flood line, walked: the granite kerbs show where the gates&rsquo; protection ends. Until four.', '12 MIN BY BIKE'),
        ('3:30', 'The bakery you saved, on the way back', 'Saved Friday, not yet visited; open till five. Your save is yours, whatever else changed.', ''),
    ], alts=[('Stay in: the skillet, preheated dry', 'TONIGHT &middot; THE METHOD IS BELOW')], meta_t='ONE RIDE, TWO THINGS &middot; TIDE TABLE &middot; YOUR SAVED PLACE'), top=22)
    inner += sect('In motion') + gut(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you'])
                                     + arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D'])
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
                                     + row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(COLD())
    inner += gut(method('The crust split where the pan was coldest. Heat the skillet dry first.', ['Four minutes dry, on high, before any oil.', 'Then oil, then dough; the edge sets before the middle steams.', 'Lid on for the last minute if the top is pale.'], meta_t='FROM YOUR THURSDAY NOTE'), top=26)
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def monday_narrowed():
    """Dana narrowed her bookshop to city precision. One addressed unit is left unspent, so the region does not render; Maya's noodle bar goes inline (Treatment 1 for one unit)."""
    inner = g3.h2_read() + gut(g3.alex_card(), top=22)
    inner += sect('In motion') + gut(arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers &middot; a bookshop, somewhere in Brooklyn</span>', avatars=['D'])
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted &middot; Maya sent a place for after</span>')
                                     + row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed', last=True))
    inner += sect('This week') + gut(g3.market_card() + '<div style="height: 26px;"></div>'
        + handoff_artifact('M', 'Maya', 'SATURDAY &middot; TO YOU', 'This one after the show, it&rsquo;s open till one and you won&rsquo;t need a table.', 'dining', 'The noodle bar', 'THREE BLOCKS FROM THE HALL &middot; OPEN TILL 1', 'The noodle bar'))
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=24)
    inner += sect('Worth knowing') + gut(COLD())
    inner += g5.END_MON()
    return phone(inner, 0)

def monday_blocked():
    """Nadia blocked Maya. No region, no clause on the show row, no banner, no dimmed slot: the page is complete at its new size. Occurrences stand in Life."""
    inner = g3.h2_read() + gut(g3.alex_card().replace(facepile(['A', 'M', 'you'], 24, -7), facepile(['A', 'you'], 24, -7)).replace('4 GOING', '3 GOING'), top=22)
    inner += sect('In motion') + gut(arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D'])
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
                                     + row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed', last=True))
    inner += sect('This week') + gut(g3.market_card() + '<div style="height: 26px;"></div>'
        + u2('Sunday morning is Dana&rsquo;s; her bookshop opens at eleven', 'Dana: &ldquo;this one, for Sunday? I want the poetry shelf in the back.&rdquo;', meta_t='COURT STREET &middot; OPENS 11 &middot; ADDRESSED TO YOU THURSDAY'))
    inner += sect('Worth knowing') + gut(COLD())
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += g5.END_MON()
    return phone(inner, 0)

def provenance_col():
    def prov(av, col_, t, dashed=False):
        a = (f'<span style="width: 20px; height: 20px; border-radius: 10px; background: {PAPER}; border: 1px dashed rgba(27,23,20,0.3); color: {MUTE}; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; flex: none;">&mdash;</span>' if dashed
             else f'<span style="width: 20px; height: 20px; border-radius: 10px; background: {col_}; color: {CARD}; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; flex: none;">{av}</span>')
        return f'<div style="display: flex; gap: 9px; align-items: flex-start; padding: 6px 0; border-top: 1px solid rgba(27,23,20,0.06); font-size: 12px; line-height: 16px; color: {MUTE if dashed else INK};">{a}<span>{t}</span></div>'
    before = prov('M', INK, 'Maya&rsquo;s share &middot; friends, through Sunday &middot; withdraw sits with her, always') + prov('N', UMBER, 'Your saved bakery &middot; saved Friday &middot; yours') + prov('V', UMBER, 'The sequence &middot; composed &middot; expires with its sources')
    after = prov('', '', 'A shared source was withdrawn by its owner &middot; this view was rebuilt &middot; 09-06', dashed=True) + prov('N', UMBER, 'Your saved bakery &middot; saved Friday &middot; yours, untouched') + prov('V', UMBER, 'The sequence &middot; recomposed from what remains')
    return (f'<div style="width: 440px; flex: none; display: flex; flex-direction: column;">' + caption('THE INSPECTION &middot; WHY THIS', 'Provenance, before and after', 'HONEST THAT, SILENT WHAT &middot; NO TITLE, SNIPPET OR THUMBNAIL OF THE WITHDRAWN THING SURVIVES')
            + f'<div style="padding: 10px 0 0 0;"><div class="kickm">BEFORE &middot; THREE SOURCES</div>{before}</div>'
            + f'<div style="padding: 18px 0 0 0;"><div class="kickm">AFTER &middot; TWO, AND AN HONEST LINE</div>{after}</div>'
            + f'<div style="padding: 22px 0 0 0; display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE PARAPHRASE ORACLE</div>{N("&ldquo;sesame loaf&rdquo; &middot; &ldquo;what did Maya say about the bakery&rdquo; &rarr; nothing returns, on Home, in Places, in Life, in Chat. Chat answers: &ldquo;That was shared with you once and has been withdrawn; I don&rsquo;t keep a copy.&rdquo; A generated paraphrase is a copy (MP5, ruled).")}</div>'
            + f'<div style="padding: 18px 0 0 0; display: flex; flex-direction: column; gap: 8px;"><div class="kickm">THE BLOCK</div>{N("Block outranks everything (block &gt; revocation &gt; shield &gt; exclusion &gt; snooze &gt; rank). It suppresses the relationship&rsquo;s rendering, openings, relays, scope pills, and status reception. It edits the future, not the past: the dinner she came to stays in Life as the occasion&rsquo;s record. She learns nothing. Unblock restores the licence to render future grants, no old grant.")}</div>'
            + '</div>')

# ───────────────────────────── row two · the occasion lived through (C2) ─────────────────────────────
def push_frame():
    """Saturday 6:50 PM: a push, not a page. The medium is chosen by the situation."""
    ladder = ''.join(f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 4px 0;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {c}; width: 64px; flex: none;">{k}</span><span style="font-size: 12.5px; line-height: 17px; color: {c};">{v}</span></div>'
                     for k, v, c in [('SCREEN', 'would demand eyes at a bar', MUTE), ('VOICE', 'wrong room for it', MUTE), ('PUSH', 'one line, consumed in two seconds', GREEN), ('DEFER', 'too late to matter after 7', MUTE), ('SILENCE', 'would strand the four of you early', MUTE)])
    inner = anchor_row('NEW YORK &middot; SATURDAY', '6:50 PM')
    inner += gut(f'<div style="background: #2A241E; border-radius: 14px; padding: 14px 16px; display: flex; flex-direction: column; gap: 6px;"><div style="font-size: 14px; line-height: 19px; color: {CARD};">The park is on. Alex moved it to 7:00; nothing to do. Maya knows.</div><div class="fn" style="color: rgba(251,247,236,0.55);">ONE BOUNDED PUSH &middot; NO OPEN-THE-APP DEMAND &middot; 6:50</div></div>', top=22)
    inner += gut(f'<div style="padding-top: 8px;"><div class="kickm" style="margin-bottom: 6px;">THE MEDIUM, CHOSEN BY THE SITUATION</div>{ladder}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 15px; line-height: 22px; color: {MUTE}; font-style: italic;">If she opens Home anyway, it is the Thursday-after page with one row changed to 7:00. Nothing else moved.</div>', top=22)
    inner += gut(door('Saturday, the arrangement') + meta('PLAN LANE &middot; THE OCCASION OWNS THE CHANGE', 0), top=22)
    return phone(inner, 0)

def sunday_after():
    """The morning after Alex's birthday. Home says nothing about it: the evening happened; no unit narrates that the product coordinated it."""
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:40 AM')
    inner += orientation('Clear. Low water at 2:20.', '58&deg; by noon &middot; Dana lands Saturday.')
    inner += gut(ways_card('Today', [
        ('The pier at low water', 'The first quiet walk of the week; the flood line shows until five.', 'LOW WATER 2:20&ndash;5'),
        ('Stay in', 'The noodle shop delivers until ten.', 'ANY TIME'),
    ]), top=22)
    inner += sect('In motion') + gut(arow('Dana &middot; lands Saturday &middot; <span style="color: #6E6862;">Sunday morning is hers &middot; the bookshop on Court Street</span>', avatars=['D'])
                                     + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(u2('The cold broke overnight; the river side is back within a degree of the avenue', 'The masonry and the water are holding the same heat again. The four-degree split returns with the next clear, still night.', meta_t='TWO NEARBY STATIONS + FORECAST &middot; FIXTURE'))
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("admission", "THE HALL")}{chip("dining", "Alex&rsquo;s birthday", None, serif=True)}</div>' + meta('HELD SAYS NOTHING &middot; THE SHOW AND THE PARK ARE IN THE RECORD, WITHOUT A DOT', 8), top=32)
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:D', ''), 'Dana', INK)],
                    'Saturday, Dana lands.')
    return phone(inner, 0)

# ───────────────────────────── row three · a kept intention returning (HP C3) ─────────────────────────────
def kept_receipt():
    """Saturday: kept in the person's words, from the Place Focus, through Chat. The receipt on Home the next open."""
    inner = anchor_row('NEW YORK &middot; SATURDAY', '3:40 PM')
    inner += orientation('A clear Saturday. Low water at 1:40.', '60&deg; &middot; the market until one.')
    inner += gut(f'<div class="row" style="padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span class="kickm" style="flex: none;">KEPT</span>{mark("book", 15, 0.7)}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">The reading room over the bookshop &middot; <span style="color: #6E6862;">&ldquo;for a free evening &mdash; don&rsquo;t plan around it&rdquo;</span></span><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Undo</span></div>'
                 + meta('IN YOUR WORDS &middot; NO DATE &middot; NOTHING BUILT AROUND IT &middot; FINDABLE IN LIFE &middot; PLACES', 8), top=22)
    inner += sect('Today in the city') + gut(u2('At low water the old creek mouth shows where the harbor used to come in', 'Along the waterfront streets between 1:40 and 4 the granite kerbs end where the 1911 gates&rsquo; protection ends.', meta_t='TIDE TABLE + THE HARBOR BOOK, CH. 3 &middot; FIXTURE'))
    inner += sect('In motion') + gut(arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D']) + row_mark('admission', 'The show &middot; Friday, doors 8', last=True))
    inner += ending([('SAT', dm('solid', INK), 'today', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE)],
                    'Friday the show. Saturday the 19th, Dana.')
    return phone(inner, 0)

def kept_returns():
    """Two weeks later, a free evening. The kept intention appears once, as a possibility, with its reasons inline (the causal spine, C3)."""
    inner = anchor_row('NEW YORK &middot; THURSDAY', '6:20 PM')
    inner += orientation('Clear, mild, and nothing on tonight.', 'Two weeks on &middot; Dana&rsquo;s visit was Saturday.')
    inner += sect('One way the evening can open', top=30) + gut(u2('The reading room over the bookshop: quiet upstairs after seven, open until eleven', '18 minutes from you. You said not to plan around it, so nothing is.',
        f'<div style="border-top: 1px solid rgba(27,23,20,0.06); padding-top: 8px; margin-top: 8px; display: flex; flex-direction: column; gap: 4px;">'
        + ''.join(f'<div style="display: flex; gap: 10px;"><span class="fn" style="color: {GOLDD};">{i}</span><span style="font-size: 12.5px; line-height: 17px; color: {INK};">{t}</span></div>' for i, t in [('1', 'Kept in your words, two Saturdays ago'), ('2', 'Open tonight: hours read Tuesday'), ('3', 'Your evening is free; nothing else is moving')]) + '</div>',
        meta_t='WHY THIS, INLINE &middot; IT WILL NOT ASK TWICE', door_text='The reading room'))
    inner += sect('In motion') + gut(row('Dentist &middot; Tuesday, done', mark='dashed', muted=True, last=True))
    inner += sect('Worth knowing') + gut(u2('The greenmarket moves indoors from Saturday', 'Same stalls, the hall on the north side; bread still goes by ten.', meta_t='FROM THE MARKET&rsquo;S NOTICE &middot; FIXTURE'))
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('hollow', ''), 'market', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)],
                    'Saturday the market moves indoors.')
    return phone(inner, 0)

def kept_ignored():
    """Ignored. The next open evening: no unit, not 'still kept', not 'you didn't go'. Life holds it, findable and releasable."""
    inner = anchor_row('NEW YORK &middot; FRIDAY', '7:10 PM')
    inner += orientation('A warm Friday. Nothing is booked.', 'Nothing needs you tonight.')
    inner += sect('Worth knowing', top=30) + gut(u2('The greenmarket moves indoors from tomorrow', 'Same stalls, the hall on the north side; bread still goes by ten.', meta_t='FROM THE MARKET&rsquo;S NOTICE &middot; FIXTURE'))
    inner += gut(f'<div style="padding-top: 26px;"><div class="fn" style="color: {ANCHOR};">NO READING-ROOM UNIT &middot; NOT &ldquo;STILL KEPT&rdquo; &middot; NOT &ldquo;YOU DIDN&rsquo;T GO&rdquo;</div></div>')
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("admission", "THE HALL")}</div>' + meta('THE KEPT PLACE IS IN LIFE &middot; PLACES, NOT ON THIS SHELF: CHIPS ARE FOR PASSES', 8), top=30)
    inner += ending([('FRI', dm('solid', INK), 'today', INK), ('SAT', dm('hollow', ''), 'market', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Tomorrow the market moves indoors.')
    return phone(inner, 0)

def life_places_frame():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">LIFE &middot; PLACES</span><span class="fn" style="margin-left: auto;">HELD</span></div></div>'
             + orientation_direct('Brooklyn, held.', 'Three places kept; none owes you a visit.'))
    inner += gut(row(f'The reading room over the bookshop &middot; <span style="color: #6E6862;">kept for a free evening &middot; in your words</span>', mark='hollow')
                 + row('The Sunset Park bakery &middot; <span style="color: #6E6862;">saved &middot; not yet visited</span>', mark='hollow')
                 + row('The pier &middot; <span style="color: #6E6862;">three afternoons, one evening</span>', mark='solid', color=INK, last=True), top=28)
    inner += gut(meta('QUIET, FINDABLE, RELEASABLE &middot; NO OVERDUE &middot; RELEASE FROM HERE REMOVES IT EVERYWHERE', 0), top=14)
    inner += f'<div style="padding: 40px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING OWNER &middot; NOT REDESIGNED HERE</div></div>'
    return phone(inner, 0, active='Life')

# ───────────────────────────── row four · attributed friends (F4) on Persona B's Home ─────────────────────────────
def lanes_card():
    def lane(av, col_, k, t):
        return (f'<div style="border-top: 1px solid rgba(27,23,20,0.07); padding: 10px 0; display: flex; gap: 10px; align-items: flex-start;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {col_}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none;">{av}</span>'
                f'<div style="flex: 1; min-width: 0;"><div class="fn" style="color: {ANCHOR};">{k}</div><div style="{SERIF} font-size: 16px; line-height: 22px; color: {INK}; margin-top: 2px;">{t}</div></div></div>')
    inner = title('The difference was not simply the temperature', 20, 25, 600) + sup('Two evenings a month apart, at the same hour, under the same heat.', INK2)
    inner += f'<div style="margin-top: 10px;">' + lane('N', UMBER, 'ROME &middot; YOU &middot; 9:10 PM &middot; YOUR SOURCES', 'The route stayed inside dense streets; the river was not part of the evening.') + lane('M', INK, 'PARIS &middot; MAYA &middot; 9:05 PM &middot; HER SOURCES &middot; AUDIENCE: YOU', 'The riverbank became the place to remain outside.') + '</div>'
    inner += f'<div style="border-top: 1px solid rgba(27,23,20,0.07); padding-top: 10px; margin-top: 2px;"><div style="{SERIF} font-style: italic; font-size: 16px; line-height: 23px; color: {MUTE};">The useful contrast is how each route made water available, not who handled the heat better.</div></div>'
    inner += meta('VESPER OWNS ONLY THE CONNECTIVE SENTENCE &middot; UNDER MAYA&rsquo;S MAY-USE AND MAY-NAME &middot; NO ASK RENDERED', 8) + door('Open Rome and Paris in Places')
    return card(inner)

def attributed_home():
    inner = anchor_row('NEW YORK &middot; WEDNESDAY', '7:40 AM')
    inner += orientation('Thursday reaches 34&deg; by two.', 'The first real heat since you landed &middot; Saturday is dinner with Maya and Alex.')
    inner += gut(lanes_card(), top=22)
    inner += sect('Thursday, reshaped for the heat') + gut(ways_seq_card('Thursday, in order', [
        ('8:30', 'Errands, outside, early', 'Before the pavement holds anything.', 'THEN INDOORS UNTIL FIVE'),
        ('5:30', 'The pier, when the sun is off it', 'Maya&rsquo;s water-stop idea, if the hours hold: the river side is the cool side after six.', '9 MIN BY BIKE'),
        ('7:15', 'The bookshop on Court Street to end it', 'Open till nine.', ''),
    ], meta_t='FROM YOUR ROME TRACES + MAYA&rsquo;S NOTE &middot; FALLS BACK TO NORMAL IF THE FORECAST BREAKS'))
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled</span>', avatars=['M', 'A', 'you'])
                                     + row_mark('flight', 'Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', last=True))
    inner += ending([('WED', dm('solid', INK), 'today', INK), ('THU', dm('dashed', OX), '34&deg;', OX), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE)],
                    'Thursday, the heat. Saturday, dinner.')
    return phone(inner, 0)

def attributed_after_withdrawal():
    """Maya withdraws her Paris trace before Thursday: the comparison cannot exist; the foundation drops her lane; Thursday recompiles from Rome alone."""
    inner = anchor_row('NEW YORK &middot; WEDNESDAY', '7:40 AM')
    inner += orientation('Thursday reaches 34&deg; by two.', 'The first real heat since you landed &middot; Saturday is dinner with Maya and Alex.')
    inner += sect('Worth knowing', top=26) + gut(u2('Rome&rsquo;s embankments, a month later: the walls you walked are the city&rsquo;s oldest argument with its river', 'Your Rome evenings stayed inside dense streets; the river was never part of them. Thursday here is the first day that reads the same way.', meta_t='REBUILT FROM YOUR OWN RECORD &middot; NO GAP WHERE SHE WAS'))
    inner += sect('Thursday, reshaped for the heat') + gut(ways_seq_card('Thursday, in order', [
        ('8:30', 'Errands, outside, early', 'Before the pavement holds anything.', 'THEN INDOORS UNTIL FIVE'),
        ('7:15', 'The bookshop on Court Street to end it', 'Open till nine.', ''),
    ], meta_t='FROM YOUR ROME TRACES &middot; FALLS BACK TO NORMAL IF THE FORECAST BREAKS'))
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled</span>', avatars=['M', 'A', 'you'])
                                     + row_mark('flight', 'Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', last=True))
    inner += ending([('WED', dm('solid', INK), 'today', INK), ('THU', dm('dashed', OX), '34&deg;', OX), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE)],
                    'Thursday, the heat. Saturday, dinner.')
    return phone(inner, 0)

# ───────────────────────────── the board ─────────────────────────────
def divider(kick, ttl, sub):
    return (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">{kick}</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">{ttl}</div><div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">{sub}</div></div>')

def states_board():
    row1 = [col(sunday_withdrawn(), daycap('SUNDAY 9:10 &middot; AFTER MAYA WITHDRAWS', '1 &middot; WITHDRAWAL', 'Recompiled, not amputated', 'THE SEQUENCE REBUILDS FROM WHAT REMAINS &middot; YOUR OWN SAVE STANDS &middot; NO SILHOUETTE &middot; COMPARE 02 PHONE 2')),
            col(monday_narrowed(), daycap('MONDAY 6:40 &middot; AFTER DANA NARROWS', '2 &middot; NARROWING', 'One unspent unit: the region does not render', 'CITY PRECISION &middot; NO PIN, NO DISTANCE, NO ROUTE &middot; MAYA&rsquo;S UNIT GOES INLINE')),
            col(monday_blocked(), daycap('MONDAY 6:40 &middot; AFTER THE BLOCK', '3 &middot; BLOCK', 'Quieter, not emptier', 'NO BANNER, NO DIMMED SLOT &middot; THE PAGE IS COMPLETE AT ITS NEW SIZE')),
            provenance_col()]
    row2 = [col(push_frame(), daycap('SATURDAY 6:50 PM &middot; DURING', '4 &middot; A PUSH, NOT A PAGE', 'The medium is chosen by the situation', 'ONE LINE, TWO SECONDS &middot; NO OPEN-THE-APP DEMAND')),
            col(sunday_after(), daycap('SUNDAY 9:40 &middot; THE MORNING AFTER', '5 &middot; SILENCE IS THE RETURN', 'Home says nothing about the birthday', 'NO RECAP, NO RATING, NO SELF-CONGRATULATION &middot; HELD SAYS NOTHING')),
            notecol('The occasion, lived through', [
                ('DURING', N('Home is not opened at a bar. The one change (Alex moved the park to 7:00) reaches her as a push she can consume in two seconds, and nothing else. If she opens Home anyway it is Thursday&rsquo;s page with one row changed. The Occasion owns the change; Home carries it.')),
                ('AFTER', N('The evening happened. No unit narrates that the product coordinated it; no rating prompt; no &ldquo;how was it&rdquo;. The show and the park sit in the Life shelf as chips with no dot: on Life, everything shown is held, so held says nothing. The following week is the following week.')),
                ('WHAT C2 ALSO DREW, NOT REPEATED HERE', N('The correction after consequence (a chosen place closes; the backup promotes; nobody re-plans) is 02 phone 8. The three viewer-relative records of one night are Life&rsquo;s (Life 17D).')),
            ], w=520)]
    row3 = [col(kept_receipt(), daycap('SATURDAY 3:40 &middot; KEPT, IN HER WORDS', '6 &middot; THE KEEP', 'A place kept for a free evening', 'THROUGH CHAT, FROM THE PLACE &middot; NO DATE &middot; NOTHING BUILT AROUND IT &middot; UNDO')),
            col(kept_returns(), daycap('THURSDAY 6:20 PM &middot; TWO WEEKS LATER', '7 &middot; IT RETURNS, ONCE', 'A possibility with its reasons inline', 'WHY THIS: KEPT, OPEN, FREE &middot; A MOVE, IGNORABLE, EXPIRING')),
            col(kept_ignored(), daycap('FRIDAY 7:10 PM &middot; IGNORED', '8 &middot; NOTHING FOLLOWS', 'Not still kept, not you didn&rsquo;t go', 'NO TRACE ON HOME &middot; FINDABLE IN LIFE')),
            col(life_places_frame(), daycap('BEHIND THE DOOR', '9 &middot; WHERE IT RESTS', 'Life &middot; Places, held', 'QUIET, FINDABLE, RELEASABLE &middot; EXISTING OWNER'))]
    row4 = [col(attributed_home(), daycap('WEDNESDAY 7:40 &middot; THE HEAT COMING', '10 &middot; TWO LANES, ONE AXIS', 'Rome and Paris, compared with permission', 'HER SOURCES, YOUR SOURCES &middot; VESPER OWNS THE CONNECTIVE SENTENCE &middot; NO ASK')),
            col(attributed_after_withdrawal(), daycap('WEDNESDAY 7:40 &middot; IF SHE WITHDRAWS FIRST', '11 &middot; THE FOUNDATION DROPS HER LANE', 'Thursday recompiles from Rome alone', 'NO COMPARISON WITHOUT HER &middot; THE POSSIBILITY LOSES ITS WATER STOP &middot; NO GAP')),
            notecol('Multiplayer as perception', [
                ('WHY IT IS HOME', N('This is not casual sharing. Maya&rsquo;s trace is granted evidence (may-use, may-name) and the value is a difference neither person could establish alone. The social split keeps it on Home; the friends scope in Places gets the map. Removing Maya removes a material part of the value: that is the multiplayer test (Home &amp; Places F4).')),
                ('WHAT IS FORBIDDEN', N('&ldquo;You and Maya experienced Europe in opposite ways&rdquo; (a relationship narrative) and &ldquo;Ask Maya what Paris felt like&rdquo; (labour, reply pressure). Her existing trace already answers; Vesper does not ask her to restate it.')),
                ('THE SEAT LAW', N('This is Life&rsquo;s heat-pattern Return (Life 16). While Home delivers Thursday, Life shows the foundation and the receipt, not the Return.')),
                ('SOURCES', N('Every temperature and time is a fixture. Maya&rsquo;s words are a fixture. Nothing claims how Paris works.')),
            ], w=520)]
    html = page(2620, hh('10'), f'VESPER &middot; HOME &middot; 10 &middot; STATES &middot; FROM HOME &amp; PLACES, REDRAWN ON THE CURRENT PAGES &middot; {PASS} &middot; {STAMP}', '10 &middot; Four states Home &amp; Places proved that this project had not carried',
                'Withdrawal, narrowing and block (MP5); the occasion lived through (C2); a kept intention returning (HP C3); attributed friends (F4). Each redrawn on the current fixture, in the current forms, beside the page it changes. The reference boards R1&ndash;R4 are the originals&rsquo; canon; nothing here is ruled.', row1)
    extra = (divider('THE OCCASION LIVED THROUGH &middot; C2 ON ALEX&rsquo;S BIRTHDAY', 'A push during, silence after', '02 stops on Thursday with the park settled. These two frames are Saturday evening and Sunday morning.')
             + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>'
             + divider('A KEPT INTENTION RETURNING &middot; HP C3 ON THE READING ROOM', 'Keep is the most common gesture, and it had no Home page', 'Kept in her words on a Saturday; back once, two weeks later, with its reasons inline; ignored, and nothing follows; held in Life.')
             + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row3) + '</div>'
             + divider('ATTRIBUTED FRIENDS &middot; F4 ON PERSONA B&rsquo;S HOME', 'Two authored lanes on one verified axis', 'The strongest social value in Home &amp; Places, absent from this project except as a drawer specimen. Drawn on the week after the return, when the first heat makes it timely.')
             + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row4) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', extra + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = states_board(); open(os.path.join(OUT, '10 - States.dc.html'), 'w').write(html); print('wrote 10', len(html))
