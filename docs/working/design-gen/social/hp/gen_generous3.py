"""Vesper — Home · generous-value pass, revision 3: targeted corrections A–E on the revision-2 baseline.
Keeps the richer Home; restores selective containment; gives typography distinct
jobs (section heading / content title / metadata / supporting text); removes the
miniature design rationale from every unit; shows the onboarding result instead
of describing it; classifies every unit by production class outside the phone."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
from gen_generous import (span, photo, callouts, facepile, arow, compare2, collapsed, ending, WEEK_SUN, WEEK_MON,
                          caption, col, board_page, head, FOOT, N, body)

OUT = os.path.join(os.path.dirname(__file__), 'homeproj'); V1 = os.path.join(os.path.dirname(__file__), 'v1phones'); V2 = os.path.join(os.path.dirname(__file__), 'v2phones')
def v1(name): return open(os.path.join(V1, name + '.html')).read()
def v2(name): return open(os.path.join(V2, name + '.html')).read()

# ───────────────────────────── v2 components · four typographic jobs ─────────────────────────────
def sect(t, top=40):
    """Section heading: occasional, plain-language navigation. Sans 13/600 ink, sentence case, hairline — not a mono kicker."""
    return (f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 12px; padding-bottom: 10px;">'
            f'<span style="font-size: 13px; font-weight: 600; letter-spacing: 0.1px; color: {INK};">{t}</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.12);"></span></div></div>')

def meta(t, top=6):
    """Metadata: restrained mono for time, distance, date, source. One line."""
    return f'<div class="fn" style="margin-top: {top}px; color: {ANCHOR};">{t}</div>'

def title(t, size=17, lh=22, w=500):
    return f'<div style="{SERIF} font-size: {size}px; line-height: {lh}px; font-weight: {w}; color: {INK};">{t}</div>'

def sup(t, col=None):
    """Supporting text: enough to deliver the distinction."""
    return f'<div style="font-size: 13px; line-height: 18px; color: {col or MUTE}; margin-top: 4px;">{t}</div>'

def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'

def u2(t, text='', media='', meta_t='', door_text=None, size=17, lh=22):
    out = '<div style="display: flex; flex-direction: column;">' + title(t, size, lh)
    if text: out += sup(text)
    out += media
    if meta_t: out += meta(meta_t)
    if door_text: out += door(door_text)
    return out + '</div>'

def card(inner, pad='16px', bg=CARD):
    return (f'<div style="background: {bg}; border-radius: 18px; box-shadow: 0 6px 18px rgba(27,23,20,0.10), 0 1px 3px rgba(27,23,20,0.06); padding: {pad}; display: flex; flex-direction: column; overflow: hidden;">{inner}</div>')

def author_row(letter, who, when):
    return (f'<div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none;">{letter}</span>'
            f'<span style="font-size: 13px; font-weight: 600; color: {INK};">{who}</span><span class="fn" style="color: {ANCHOR};">{when}</span></div>')

def share_card(letter, who, when, words, plate_h=0, plate_cap='', meta_t='', door_text=None):
    """A friend's photograph and words: one media-led card; authorship belongs to the unit."""
    pl = (f'<div style="height: {plate_h}px; margin: -16px -16px 12px -16px; background: #2A241E; position: relative;"><div class="fn" style="position: absolute; left: 16px; bottom: 12px; color: #8F877C;">{plate_cap}</div></div>') if plate_h else ''
    inner = pl + author_row(letter, who, when) + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">&ldquo;{words}&rdquo;</div>'
    if meta_t: inner += meta(meta_t, 8)
    if door_text: inner += door(door_text)
    return card(inner)

def handoff_card(letter, who, when, words, meta_t, door_text):
    inner = author_row(letter, who, when) + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">&ldquo;{words}&rdquo;</div>' + meta(meta_t, 8) + door(door_text)
    return card(inner)

def ways_card(t, items, meta_t=''):
    """A prepared afternoon: one contained card with a readable shape. items: [(title, one clause)]"""
    inner = title(t, 20, 25, 600)
    OR = f'<div style="display: flex; align-items: center; gap: 10px; margin: 6px 0;"><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span><span class="fn" style="color: {ANCHOR};">OR</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span></div>'
    for i, (a, b, when) in enumerate(items):
        if i: inner += OR
        inner += (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: {8 if i else 12}px 0 4px 0;">'
                  f'<span style="width: 8px; height: 8px; border-radius: 4px; border: 1.5px solid {ANCHOR}; box-sizing: border-box; flex: none; margin-top: 7px;"></span>'
                  f'<div style="flex: 1;">{title(a, 16, 21)}{sup(b)}<div class="fn" style="color: {ANCHOR}; margin-top: 3px;">{when}</div></div></div>')
    if meta_t: inner += meta(meta_t, 10)
    return card(inner)

def arr_card(status, t, text, instrument='', people='', meta_t='', door_text=None, status_col=PLAN):
    """A shared arrangement: contained, with integrated people and timing. Plan-ink status; not an urgency crown."""
    inner = (f'<div style="display: flex; align-items: center; gap: 7px; margin-bottom: 6px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {status_col};"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {status_col};">{status}</span></div>'
             + title(t, 20, 25, 600) + (sup(text, INK2) if text else '') + instrument)
    if people: inner += f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">{people}</div>'
    if meta_t: inner += meta(meta_t, 8)
    if door_text: inner += door(door_text)
    return card(inner)

def fact(label, text, last=False):
    """A simple service update or city fact: one concise row."""
    bb = ' border-bottom: 1px solid rgba(27,23,20,0.07);' if last else ''
    return (f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 10px 0; border-top: 1px solid rgba(27,23,20,0.07);{bb}"><span class="fn" style="color: {ANCHOR};">{label}</span>'
            f'<span style="font-size: 14px; line-height: 19px; color: {INK};">{text}</span></div>')

def reading_card(source, t, text, door_text):
    """Substantial reading: a satisfying preview with owned depth behind it."""
    inner = (f'<div style="display: flex; gap: 14px; align-items: flex-start;"><div class="hatch" style="width: 56px; height: 56px; border-radius: 12px; flex: none;"></div>'
             f'<div style="flex: 1; min-width: 0;"><span class="fn" style="color: {ANCHOR};">{source}</span>{title(t, 17, 22)}</div></div>' + sup(text) + door(door_text))
    return card(inner, bg=WASH)

def ticket_stub(hall, day, doors, w=150, sample=True):
    """A ticket-shaped input, drawn as a stub."""
    return (f'<div style="width: {w}px; flex: none; border: 1px {"dashed" if sample else "solid"} rgba(27,23,20,0.35); border-radius: 10px; padding: 10px 12px; background: {PAPER}; display: flex; flex-direction: column; gap: 4px; position: relative;">'
            f'<span class="fn" style="color: {ANCHOR};">{day}</span><span style="{SERIF} font-size: 15px; line-height: 19px; font-weight: 600; color: {INK};">{hall}</span><span class="fn" style="color: {INK};">DOORS {doors}</span>'
            f'<span style="position: absolute; right: -6px; top: 50%; width: 12px; height: 12px; border-radius: 6px; background: {CARD}; margin-top: -6px;"></span></div>')

RARROW = f'<svg width="22" height="22" viewBox="0 0 22 22" fill="none" style="flex: none; align-self: center;"><path d="M4 11H17M12 6L17 11L12 16" stroke="{GOLD}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def sample_card(label, input_html, result_title, instrument, facts, doors):
    """Onboarding sample: the result itself, clearly labelled, with an optional way to try it."""
    inner = (f'<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;"><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.8px; color: {MUTE}; border: 1px dashed rgba(27,23,20,0.35); border-radius: 999px; padding: 3px 9px;">SAMPLE</span><span class="fn" style="color: {ANCHOR};">{label}</span></div>'
             f'<div style="display: flex; gap: 10px; align-items: stretch;">{input_html}{RARROW}<div style="flex: 1; min-width: 0;">{title(result_title, 17, 22, 600)}</div></div>'
             + instrument + '<div style="display: flex; flex-direction: column; gap: 4px; margin-top: 10px;">' + ''.join(f'<div style="font-size: 13px; line-height: 18px; color: {INK};">{f}</div>' for f in facts) + '</div>'
             + '<div style="display: flex; gap: 18px; align-items: center; margin-top: 4px;">' + ''.join(door(d, c) for d, c in doors) + '</div>')
    return card(inner)

def kept_row(text, undo=True):
    return (f'<div class="row" style="padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"><span class="kickm" style="flex: none;">KEPT</span><span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">{text}</span>'
            + (f'<span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Undo</span>' if undo else CHEV) + '</div>')

def rows_A(with_alex=True, with_dana=True, with_show=True, dentist='Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', alex_text=None):
    rows = []
    if with_alex: rows.append(arow(alex_text or 'Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you']))
    if with_dana: rows.append(arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D']))
    if with_show: rows.append(row('The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>', mark='solid', color=GOLD))
    rows.append(row(dentist, mark='dashed'))
    rows[-1] = rows[-1].replace('padding: 8px 0;"', 'padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"')
    return sect('In motion') + gut(''.join(rows))

COLD = lambda when='Thursday night': u2(f'{when.capitalize()} the river side of your walk runs four degrees colder than the avenue',
    'Open water and wind keep the waterfront blocks from holding the day&rsquo;s heat; two streets in, masonry gives it back for hours.',
    compare2('RIVER SIDE &middot; 9 PM', '24&deg;', 'wind off the water', 'THE AVENUE &middot; 9 PM', '28&deg;', 'masonry holds the day'), meta_t='TWO NEARBY STATIONS + FORECAST &middot; FIXTURE')
COLD_CITY = lambda when='Thursday night': u2(f'{when.capitalize()} the waterfront streets run four degrees colder than the avenues',
    'Open water and wind keep them from holding the day&rsquo;s heat; two streets in, masonry gives it back for hours.',
    compare2('WATERFRONT &middot; 9 PM', '24&deg;', 'wind off the water', 'THE AVENUES &middot; 9 PM', '28&deg;', 'masonry holds the day'), meta_t='TWO STATIONS + FORECAST &middot; FIXTURE')
SKILLET = u2('The crust split where the pan was coldest', 'Heat the skillet dry for four minutes, then oil, then dough &mdash; the edge sets before the middle steams.', meta_t='FROM YOUR THURSDAY NOTE')
CITY_SUN = ('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.')
            + fact('THE FLEA &middot; SATURDAYS THROUGH OCTOBER', 'Reopened under the bridge, 10 to 5. Nine minutes from the market.', last=True) + '</div>')

# ───────────────────────────── H1 v2 ─────────────────────────────
def h1v2():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 160, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT',
                            'SUNSET PARK &middot; 14 MIN BY BIKE &middot; OPEN NOW', 'The bakery'), top=22)
    inner += gut(ways_card('Today', [
        ('The loaf, then the water', 'Bakery by 10:30; low water on the pier nine minutes on.', 'MORNING &middot; 10:30 &rarr; 1:40'),
        ('The flood line, walked at low water', 'The granite kerbs show where the gates&rsquo; protection ends.', 'AFTERNOON &middot; 1:40&ndash;4'),
        ('Stay in. The skillet, preheated dry', 'Thursday&rsquo;s soggy crust was the pan, not the dough.', 'TONIGHT'),
    ]), top=16)
    inner += rows_A()
    inner += sect('Worth knowing') + gut(COLD() + '<div style="height: 26px;"></div>' + SKILLET)
    inner += sect('The city this week') + gut(CITY_SUN)
    inner += gut(reading_card('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', 'The pumps under the park finish what the gates cannot',
                              'The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.', 'Read the chapter'), top=36)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

H1_NOTES = notecol('Disposition A, on H1', [
    ('A &middot; ALTERNATIVES', N('&ldquo;Today&rdquo; keeps its contained choice set. The numerals are gone; each option carries a hollow mark and its own time window as metadata (morning &middot; afternoon &middot; tonight), and an &ldquo;or&rdquo; hairline separates them. Sequencing cues stay only inside an option (&ldquo;bakery by 10:30; low water nine minutes on&rdquo;). Opening an option opens it; nothing is adopted or scheduled. No selection control was added.')),
    ('B &middot; THE CODA', N('&ldquo;Saturday the market before ten, then Alex&rdquo; promoted a possibility into the week&rsquo;s summary. The line now names only what is held: &ldquo;Friday the show. Saturday, Alex&rsquo;s birthday.&rdquo; Dana&rsquo;s row drops the bookshop clause.')),
    ('UNCHANGED, DELIBERATELY', N('Maya&rsquo;s card, the rows, the cold instrument, the skillet, the city facts, the reading preview, the seam. The cold instrument&rsquo;s numbers stay on the phone as a fixture; H0 now names the data that would support them.')),

    ('PAYOFFS RETAINED', ledger([('MAYA', 'Loaf, day, hour, distance, her photograph'), ('TODAY', 'Three distinct days, each with its reason and window'), ('IN MOTION', 'Alex&rsquo;s arrangement, Dana, the show, the dentist'), ('THE COLD', 'Two numbers and the mechanism'), ('THE SKILLET', 'A usable technique from the person&rsquo;s own note'), ('THE CITY', 'Two dated facts'), ('THE READING', 'The payoff sentence, then the door')])),
], w=440)

def H1():
    cols = [col(v2('h1v2'), caption('BEFORE &middot; REVISION 2', 'Generous, composed', 'THE WORKING BASELINE')),
            col(h1v2(), caption('AFTER &middot; REVISION 3', 'Alternatives, not an itinerary', 'A &middot; UNNUMBERED OPTIONS WITH THEIR OWN WINDOWS &middot; B &middot; CODA NO LONGER RECITES')),
            H1_NOTES]
    return board_page(1440, 2685, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H1 &middot; ORDINARY SUNDAY &middot; PROPOSAL', 'H1 &middot; The generous Sunday, with its choices legible as choices',
                      'Same payoffs as the last pass &mdash; a friend&rsquo;s timed share, three ways to spend the day, a mechanism, a technique, the city, the reading &mdash; with selective containment restored, typography given four distinct jobs, and the miniature design rationale removed from every unit.', cols, FOOT)

# ───────────────────────────── H2 v2 ─────────────────────────────
def alex_card():
    return arr_card('SATURDAY &middot; FORMING &middot; 4 GOING', 'Alex wants it walkable from the L and not a restaurant. The pier at 6:30 fits both.', '',
                    span('THE PIER &middot; 6:30&ndash;8', 118, 214, 'SUNSET 7:04', start='4 PM', end='10', w=349),
                    people=facepile(['A', 'M', 'you'], 24, -7) + f'<span style="font-size: 13px; color: {MUTE};">Alex decides &middot; you can suggest</span>', door_text='The arrangement')

def market_card(with_theo=True):
    inner = title('Saturday market: go at 9:30, not eleven', 20, 25, 600) + sup('The stalls peak from nine; the bread goes first.', INK2)
    inner += gh.rhythm_bars([1, 2, 3, 5, 6, 4, 3, 2, 1, 1], (2, 5), 1, w=349) + f'<div style="display: flex; justify-content: space-between;"><span class="fn">8A</span><span class="fn" style="color: {GOLDD};">PEAK 9&ndash;11</span><span class="fn">1P</span></div>'
    if with_theo:
        inner += (f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(27,23,20,0.07);">'
                  f'<span style="width: 24px; height: 24px; border-radius: 12px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; flex: none;">T</span>'
                  f'<div style="flex: 1;"><div style="{SERIF} font-size: 16px; line-height: 22px; color: {INK};">&ldquo;The bread stall sells out by ten &mdash; go early or don&rsquo;t bother.&rdquo;</div><div class="fn" style="color: {ANCHOR}; margin-top: 3px;">THEO &middot; GOES MOST WEEKS &middot; MOVED YOUR WINDOW FROM 11 TO 9:30</div></div></div>')
    else:
        inner += meta('RHYTHM FROM PAST SATURDAYS')
    return card(inner)

def sunday_unit(inline=True):
    if inline:
        return u2('Sunday with Dana: her bookshop opens at eleven; Maya&rsquo;s loaf is gone by then', 'Dana: &ldquo;this one, for Sunday? I want the poetry shelf in the back.&rdquo; The bakery is six minutes from it.', meta_t='COURT STREET &middot; OPENS 11 &middot; MAYA&rsquo;S SHARE, THROUGH SUNDAY')
    return ''  # T2: Dana's handoff card is her one expression; no Sunday paraphrase

def h2_read(): return anchor_row('NEW YORK &middot; MONDAY', '6:40 PM') + orientation('Cold coming Thursday. Saturday is Alex&rsquo;s.', 'Mild until then &middot; the show Friday.')
PULL = gut(door('Everything shared with you') + meta('LIFE &middot; PEOPLE &middot; BY PERSON', 0), top=32)
END_MON = lambda: ending(WEEK_MON, 'Friday the show. Saturday, Alex&rsquo;s birthday.')

def h2v2_t1():
    inner = h2_read() + gut(alex_card(), top=22) + rows_A(with_alex=False)
    inner += sect('This week') + gut(market_card() + '<div style="height: 26px;"></div>' + sunday_unit(True))
    inner += sect('Worth knowing') + gut(COLD())
    inner += PULL + END_MON()
    return phone(inner, 0)

def h2v2_t2():
    inner = h2_read() + gut(alex_card(), top=22) + rows_A(with_alex=False)
    inner += sect('This week') + gut(market_card())
    inner += sect('From your people') + gut(share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', 150, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'SUNSET PARK &middot; 14 MIN BY BIKE', 'The bakery')
                                            + '<div style="height: 16px;"></div>' + handoff_card('D', 'Dana', 'THURSDAY &middot; TO YOU', 'This one, for Sunday? I want the poetry shelf in the back.', 'A USED BOOKSHOP ON COURT STREET &middot; OPENS 11 &middot; SIX MINUTES FROM MAYA&rsquo;S BAKERY', 'The bookshop'))
    inner += gut(door('Everything shared with you') + meta('LIFE &middot; PEOPLE &middot; BY PERSON', 0), top=20)
    inner += sect('Worth knowing') + gut(COLD())
    inner += END_MON()
    return phone(inner, 0)

def h2v2_sparse():
    inner = anchor_row('NEW YORK &middot; MONDAY', '6:40 PM') + orientation('Cold coming Thursday. Dana lands Saturday.', 'Mild until then &middot; the show Friday.')
    inner += crown(PLAN, 'FRIDAY &middot; DOORS 8:00', 'Leave for the show from work, not home', 'After ten the trains skip your stop; the way home is a surface route, 25 minutes longer.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn='YOUR TICKET + SERVICE READ')
    inner += rows_A(with_alex=False, with_show=False)
    inner += sect('This week') + gut(market_card(False) + '<div style="height: 26px;"></div>' + u2('Sunday morning is Dana&rsquo;s; her bookshop opens at eleven', 'Dana: &ldquo;this one, for Sunday? I want the poetry shelf in the back.&rdquo;', meta_t='COURT STREET &middot; OPENS 11'))
    inner += sect('Worth knowing') + gut(COLD() + '<div style="height: 26px;"></div>' + SKILLET)
    inner += ending([('MON', dm('solid', INK), 'today', INK), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('dashed', MUTE), '28&deg;', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:D', ''), 'Dana', INK), ('SUN', dm('hollow', ''), 'hers', MUTE)],
                    'Friday the show. Saturday, Dana lands.')
    return phone(inner, 0)

def life_frame():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">LIFE &middot; PEOPLE</span><span class="fn" style="margin-left: auto;">SHARED WITH YOU</span></div></div>'
             + orientation_direct('Four people have shared or addressed something to you this month.', 'By person, in their words.'))
    rws = [('M', 'Maya', 'the bakery photograph &middot; friends &middot; through Sunday'), ('D', 'Dana', 'a bookshop, for Sunday'), ('T', 'Theo', 'the market note &middot; may-use'), ('A', 'Alex', '&ldquo;walkable from the L&rdquo; &middot; in Saturday&rsquo;s arrangement')]
    inner += gut(''.join(row(f'<b>{w}</b> &middot; <span style="color: #6E6862;">{t}</span>', avatar=l, last=(i == 3)) for i, (l, w, t) in enumerate(rws)), top=28)
    inner += gut(door('What you have shared, and with whom'), top=24)
    inner += f'<div style="padding: 40px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING OWNER &middot; NOT REDESIGNED HERE</div></div>'
    return phone(inner, 0, active='Life')

H2_NOTES = notecol('Disposition B, on H2', [
    ('B &middot; DANA, ONCE', N('Revision 2 carried her bookshop in her In-motion row, the Sunday unit, her handoff card, and the coda. Now: <b>Treatment 2</b> keeps her handoff card as the one expression (her words, the shop, opening hour, distance to Maya&rsquo;s bakery &mdash; a distinct fact); the Sunday unit is removed; her row says only what is held (&ldquo;lands Saturday the 19th &middot; Sunday morning is hers&rdquo;); the coda names commitments only. <b>Treatment 1</b>, which has no region, keeps one Sunday unit carrying her words once. Maya appears once in each treatment; Theo once, inside the market.')),
    ('THE CODA', N('&ldquo;Saturday the market, then the pier&rdquo; promoted two possibilities into the week&rsquo;s summary. Now: &ldquo;Friday the show. Saturday, Alex&rsquo;s birthday.&rdquo;')),
    ('RECOMMENDATION, UNCHANGED', N('Treatment 2 with the condition: the region renders only when two or more authored units are not already spent above, never duplicates a note shown in full above, and disappears when empty (sparse variant). Shared consequences (the arrangement) still lead, above the region.')),
    ('TENSION, STILL OPEN', N('D-H2: MP2&rsquo;s &ldquo;one relational opening&rdquo; read as a dominance + demand rule, not a page-wide count. Founder ruling requested.')),
    ('BROWSING BEYOND SELECTION', N('&ldquo;Everything shared with you&rdquo; &rarr; the existing Life &middot; People owner (frame at right). No fifth tab.')),
], w=400)

def H2():
    cols = [col(v2('h2v2_t2'), caption('BEFORE &middot; REVISION 2', 'Treatment 2', 'DANA IN FOUR PLACES')),
            col(h2v2_t1(), caption('TREATMENT 1', 'Distributed', 'SOCIAL MATERIAL INSIDE THE UNITS IT CHANGES &middot; ONE PULL DOOR')),
            col(h2v2_t2(), caption('TREATMENT 2 &middot; RECOMMENDED &middot; REVISION 3', 'Distributed + a conditional grouping', 'DANA ONCE, IN HER OWN CARD &middot; MAYA ONCE &middot; THEO ONCE')),
            col(h2v2_sparse(), caption('SPARSE-SOCIAL VARIANT', 'Only Dana this week', 'NO REGION, NO EMPTY MODULE, NO INVITE')),
            col(life_frame(), caption('WHERE THE DOOR GOES', 'Life &middot; People', 'EXISTING OWNER')),
            H2_NOTES]
    return board_page(2960, 2650, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H2 &middot; SOCIALLY ACTIVE WEEK &middot; PROPOSAL', 'H2 &middot; The present social world, two ways, composed',
                      'Identical evidence in both treatments: Alex&rsquo;s arrangement and his words, Theo&rsquo;s market judgment, Maya&rsquo;s bakery share, Dana&rsquo;s addressed bookshop, the show. Cards for the arrangement, the market, and the authored material; rows for commitments. Each person appears once per treatment.', cols, FOOT)

# ───────────────────────────── H3 v2 ─────────────────────────────
STUB = ticket_stub('The Hall', 'FRI &middot; SAMPLE', '8:00')
def sample_ticket():
    return sample_card('A MADE-UP TICKET, READ THE WAY YOURS WOULD BE', STUB, 'Doors at 8. Arrive by 8:40 and you miss nothing.',
                       span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=349),
                       ['Coat check yes &middot; set times posted by the hall the day before', 'After ten, the way home from the hall is a surface route: 25 minutes longer'],
                       [('How it&rsquo;s read', GOLDD), ('Try with yours', INK)])

def h3v2_first():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '8:05 AM')
    inner += orientation('Clear and cool. The first hard cold arrives Thursday night.', 'You chose New York. Nothing about you is held.')
    inner += gut(sample_ticket(), top=22)
    inner += gut(COLD_CITY(), top=30)
    inner += sect('Also in the city this week') + gut('<div>'
        + fact('THE L &middot; AFTER 11 PM, MON&ndash;THU', 'Single-tracking; plan on a 20-minute wait between Bedford and 1st. Daytime is normal.')
        + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none.', last=True) + '</div>')
    inner += sect('What else one thing turns into') + gut('<div>' + row('A photograph of a dish &rarr; <span style="color: #6E6862;">the mechanism behind its texture</span>', mark='hollow')
                 + row('A friend&rsquo;s note &rarr; <span style="color: #6E6862;">a better window for the same place</span>', mark='hollow')
                 + row('Scattered tickets and photos &rarr; <span style="color: #6E6862;">one recoverable record</span>', mark='hollow', last=True) + '</div>')
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Bring one thing when something has your attention.</div></div>'
    return phone(inner, 0)

def h3v2_sample():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SAMPLE &middot; A TICKET, READ</span><span class="fn" style="margin-left: auto; color: {MUTE};">NOT YOURS</span></div></div>')
    inner += orientation_direct('One made-up ticket, and the evening it becomes.', 'Every fact here is invented for the sample.')
    inner += gut(f'<div style="display: flex; justify-content: center;">{ticket_stub("The Hall &middot; Friday", "FRI SEP 18 &middot; SAMPLE", "8:00", w=220)}</div>', top=22)
    inner += gut(f'<div style="display: flex; justify-content: center; margin: 10px 0;"><svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M11 4V17M6 12L11 17L16 12" stroke="{GOLD}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    inner += crown(PLAN, 'SAMPLE &middot; FRIDAY &middot; DOORS 8:00', 'Doors at 8. Arrive by 8:40 and you miss nothing.', 'After ten, the way home from the hall is a surface route: 25 minutes longer.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta=None, fn='COAT CHECK YES &middot; SET TIMES POSTED BY THE HALL THE DAY BEFORE').replace('margin: 22px 22px 0 22px', 'margin: 0 22px')
    inner += gut(callouts([('1', 'Hall, date, doors come from the ticket; set times from the hall when posted.'), ('2', 'The way there is timed only if you say where you leave from.'), ('3', 'The way home comes from the hall&rsquo;s late service.'), ('4', 'Reading a ticket books, saves, and shares nothing. If you bring yours, it is kept in Life with one-tap Undo.')]), top=22)
    inner += gut(door('Try with yours', INK) + meta('OPENS CHAT &middot; A PHOTO OR A FORWARDED EMAIL', 0), top=26)
    return phone(inner, 0)

def h3v2_chat():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">TUESDAY 8:12 AM</span></div></div>')
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; display: flex; flex-direction: column; gap: 8px;">'
                 f'<div style="height: 110px; border-radius: 10px; background: rgba(251,247,236,0.14); display: flex; align-items: flex-end; padding: 8px;"><span class="fn" style="color: rgba(251,247,236,0.7);">YOUR PHOTO &middot; A TICKET &middot; SLOT</span></div>'
                 f'<div style="font-size: 15px; line-height: 20px;">what&rsquo;s this evening look like</div></div></div>', top=26)
    inner += gut(f'<div style="max-width: 330px; display: flex; flex-direction: column; gap: 10px;">'
                 f'<div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Friday at the hall, doors 8. Arrive by 8:40 and you miss nothing; coat check yes. After ten the way home is a surface route, 25 minutes longer.</div>'
                 f'<div style="border-top: 1px solid rgba(27,23,20,0.10); padding-top: 10px;"><div style="display: flex; align-items: center; gap: 8px;"><span class="kickm">KEPT</span><span style="font-size: 13px; color: {INK};">Your ticket &middot; Friday &middot; in Life</span><span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">Undo</span></div></div></div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">Ask, or bring something else</span></div>', top=40)
    inner += f'<div style="padding: 30px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING BOUNDARY &middot; NOT REDESIGNED</div></div>'
    return phone(inner, 0, active='Chat')

def h3v2_return():
    inner = anchor_row('NEW YORK &middot; WEDNESDAY', '7:30 AM')
    inner += orientation('First hard cold of the season arrives tonight.', '18&deg; by morning &middot; wind off the river &middot; Friday&rsquo;s show is set.')
    inner += crown(PLAN, 'FRIDAY &middot; YOUR TICKET', 'Doors at 8. Arrive by 8:40 and you miss nothing.', 'After ten, the way home from the hall is a surface route: 25 minutes longer.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn='YOUR TICKET + THE HALL&rsquo;S LATE SERVICE &middot; NOTHING BOOKED')
    inner += gut(kept_row('Your ticket &middot; Friday &middot; in Life'), top=22)
    inner += sect('This week in the city') + gut('<div>' + fact('TONIGHT &middot; 18&deg;', 'The waterfront streets freeze first; four degrees colder than the avenues.')
                                                 + fact('THE L &middot; TONIGHT AFTER 11', 'Single-tracking, 20-minute waits. Friday night is unaffected &mdash; the show&rsquo;s only cost is the surface route home.', last=True) + '</div>')
    inner += sect('What else turns into something') + gut('<div>' + row('A photograph of a dish &rarr; <span style="color: #6E6862;">the mechanism behind its texture</span>', mark='hollow')
                                                          + row('A friend&rsquo;s note &rarr; <span style="color: #6E6862;">a better window for the same place</span>', mark='hollow', last=True) + '</div>')
    inner += ending([('WED', dm('solid', INK), 'today', INK), ('THU', dm('dashed', MUTE), '18&deg;', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE)],
                    'Friday the show. The rest of the week is the city&rsquo;s.')
    return phone(inner, 0)

def h3v2_next():
    inner = anchor_row('NEW YORK &middot; SATURDAY', '9:30 AM')
    inner += orientation('A clear Saturday. Low water at 1:40.', '60&deg; &middot; the first weekend after the cold.')
    inner += sect('Today in the city', top=28) + gut(u2('At low water the old creek mouth shows where the harbor used to come in', 'Along the waterfront streets between 1:40 and 4 the granite kerbs end where the 1911 gates&rsquo; protection ends.', meta_t='TIDE TABLE + THE HARBOR BOOK, CH. 3 &middot; FIXTURE')
                                                     + '<div style="height: 18px;"></div><div>' + fact('THE GREENMARKET &middot; UNTIL 1', 'Bread thins out by ten; produce holds until noon.', last=True) + '</div>')
    inner += gut(row('Your ticket &middot; Friday &middot; <span style="color: #6E6862;">in Life &middot; whether you went is yours to say</span>', mark='solid', color=GOLD, last=True), top=22)
    inner += sect('What one thing turns into') + gut(sample_card('A MADE-UP PHOTOGRAPH OF A DISH', f'<div style="width: 96px; height: 72px; border-radius: 10px; background: #2A241E; flex: none; position: relative;"><span style="position: absolute; left: 8px; top: 8px; width: 18px; height: 18px; border-radius: 9px; background: {GOLD}; color: {INK}; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center;">1</span></div>',
                                                                   'The sauce clings as a film, not a pool: finished in the pan, not poured over.', '',
                                                                   ['1 &middot; A thin film that holds the ridges: a starch-supported emulsion', 'To get it at home: sauce meets pasta ninety seconds early, finished in the pan'], [('How it&rsquo;s read', GOLDD), ('Try with yours', INK)]))
    inner += ending([('SAT', dm('solid', INK), 'today', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE)],
                    'The market until one. Low water at 1:40.')
    return phone(inner, 0)

H3_NOTES = notecol('Dispositions C and D, on H3', [
    ('C &middot; ORDER', N('The ticket-to-evening sample is now the first unit after the read, with one worthwhile city offering (the cold) directly beneath it. The L notice and Open House move lower under &ldquo;Also in the city this week&rdquo;. No hero, no intake prompt; the Sample label and both optional actions stay.')),
    ('C &middot; LANGUAGE', N('The cold-start account supplied a city only. &ldquo;Your walk&rdquo; &rarr; &ldquo;the waterfront streets&rdquo;; &ldquo;nine minutes from the address you gave&rdquo; removed. The sample no longer says &ldquo;leave from work&rdquo;: it reads &ldquo;Doors at 8. Arrive by 8:40 and you miss nothing&rdquo;, and the sheet says the way there is timed only if you say where you leave from. The return crown after one ticket uses the same language; no workplace or attendance is implied.')),
    ('D &middot; COPY', N('&ldquo;The way back is the constraint&rdquo; &rarr; &ldquo;After ten, the way home from the hall is a surface route: 25 minutes longer&rdquo; (the service consequence itself). The next-open sample says &ldquo;to get it at home&rdquo; rather than &ldquo;how to test it&rdquo;.')),
    ('THREE SOURCES, STILL APART', N('The city (fact rows and the mechanism), the sample (stamped, dashed stub), and the personal return (the crown after Chat, plus a KEPT row with Undo). Nothing about the person is assumed; &ldquo;whether you went is yours to say&rdquo; stays on the next open because it is a material boundary, not rationale.')),
    ('ACTUAL VS PROPOSED', ledger([('EXISTS', 'Chat intake with T1 receipt + Undo; Life holds the ticket; the commitment crown; service reads.'), ('NEEDS VERIFICATION', 'A city-scoped notice source with freshness; hall set-time reads.'), ('PROPOSED', 'The SAMPLE card and sheet as fixed, reusable demonstrations; retirement after tried or ignored twice; a world notice tied to a held commitment.')])),
], w=400)

def H3():
    cols = [col(v2('h3v2_first'), caption('BEFORE &middot; REVISION 2', 'First open', 'A CITY BRIEFING, THEN THE SAMPLE')),
            col(h3v2_first(), caption('1 &middot; FIRST OPEN &middot; REVISION 3', 'The sample first, one city offering beside it', 'C &middot; THE REST OF THE CITY LOWER &middot; NONPERSONAL LANGUAGE')),
            col(h3v2_sample(), caption('2 &middot; THE SAMPLE, INSPECTED', 'A ticket and its evening', 'STUB &rarr; RESULT &middot; FOUR SHORT NOTES')),
            col(h3v2_chat(), caption('3 &middot; ONE CONTRIBUTION &middot; CHAT', 'Bring the ticket', 'EXISTING BOUNDARY &middot; T1 RECEIPT WITH UNDO')),
            col(h3v2_return(), caption('4 &middot; HOME, WEDNESDAY 7:30', 'The personal return', 'THE CROWN IS THEIRS &middot; KEPT ROW &middot; A NOTICE TIED TO FRIDAY')),
            col(h3v2_next(), caption('5 &middot; NEXT OPEN &middot; SATURDAY 9:30', 'No further contribution', 'NO ATTENDANCE INFERRED &middot; A DIFFERENT SAMPLE, AS A RESULT')),
            H3_NOTES]
    return board_page(3260, 1735, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H3 &middot; FIRST OPEN &rarr; NEXT OPEN &middot; PROPOSAL', 'H3 &middot; Show the transformation; do not describe it',
                      'Persona C&rsquo;s first week. A ticket-shaped input and the evening it becomes are visible before any explanatory copy. The city carries the page; the sample is stamped; the return after one contribution is the crown and a kept row.', cols, FOOT)

# ───────────────────────────── H4 v2 ─────────────────────────────
SHOW_CROWN = lambda fn: crown(PLAN, 'FRIDAY &middot; DOORS 8:00', 'Leave for the show from work, not home', 'After ten the trains skip your stop; the way home is a surface route, 25 minutes longer.',
                              span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn=fn)
CITY_OH = '<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opened Tuesday; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>'
WEEK_THU = lambda sat_label, sat_col=INK: [('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), sat_label, sat_col), ('SUN', dm('av:D', ''), 'Dana', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)]

def h4v2_before():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '5:40 PM') + orientation('Cold coming tonight. The show is tomorrow.', '28&deg; by morning &middot; Saturday is Alex&rsquo;s &middot; the pier at 6:30 is on the table.')
    inner += SHOW_CROWN('RE-CHECKED THU 5 PM &middot; NOTHING BOOKED')
    inner += rows_A(with_show=False, dentist='Dentist &middot; Tuesday, done')
    inner += sect('Worth knowing') + gut(COLD('tonight') + '<div style="height: 26px;"></div>' + SKILLET)
    inner += sect('The city this week') + gut(CITY_OH)
    inner += ending(WEEK_THU('Alex'), 'Tomorrow the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def h4v2_during():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '6:05 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Saturday&rsquo;s place fell through. Alex needs one answer by seven.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">The pier&rsquo;s food hall closed Saturday for a private event &middot; 4 going &middot; the show tomorrow is unchanged.</div></div>')
    inner += crown(OX, 'DECIDE BY 7:00 &middot; ALEX&rsquo;S SATURDAY &middot; 55 MIN', 'Two places still fit &ldquo;walkable from the L, not a restaurant&rdquo;', 'Alex decides; yours is a preference, not a booking.',
                   span('THE PARK, 6:30 &middot; SUNSET 7:04', 118, 214, 'OPEN LATE', 'THE GARDEN, 7 &middot; TILL 9', 140, 222, 'NEEDS A NAME', start='4 PM', end='10', w=317)
                   + f'<div style="font-size: 14px; line-height: 19px; margin-top: 8px; color: {INK};">The park keeps the sunset and needs nothing; the garden is warmer after eight but wants a name for six by 6:30. Maya has said the park.</div>',
                   cta='Tell Alex which', fn='EXPIRES AT 7:00 EITHER WAY')
    inner += sect('In motion') + gut(row('The show &middot; tomorrow, doors 8 &middot; <span style="color: #6E6862;">unchanged</span>', mark='solid', color=GOLD) + arow('Dana &middot; Saturday the 19th &middot; <span style="color: #6E6862;">unchanged</span>', avatars=['D'], last=True))
    inner += gut(collapsed('THE REST OF THURSDAY &middot; STILL HERE', ['Tonight&rsquo;s cold: the river side runs four degrees colder', 'The skillet, preheated dry', 'Open House registration']), top=36)
    inner += ending(WEEK_THU('Alex &middot; 7?', OX), 'One answer by seven. Everything else is where you left it.')
    return phone(inner, 0)

def h4v2_after():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '7:25 PM') + orientation('Saturday is the park at 6:30. Cold tonight.', '28&deg; by morning &middot; the show tomorrow &middot; Alex settled it at 6:52.')
    inner += SHOW_CROWN('RE-CHECKED THU 7 PM &middot; NOTHING BOOKED')
    inner += rows_A(with_show=False, dentist='Dentist &middot; Tuesday, done', alex_text='Alex&rsquo;s birthday &middot; Saturday, the park at 6:30 &middot; <span style="color: #6E6862;">settled &middot; 4 going &middot; sunset 7:04</span>')
    inner += sect('Worth knowing') + gut(COLD('tonight') + '<div style="height: 26px;"></div>' + SKILLET)
    inner += sect('The city this week') + gut(CITY_OH)
    inner += ending(WEEK_THU('the park'), 'Tomorrow the show. Saturday, the park at 6:30.')
    return phone(inner, 0)

H4_NOTES = notecol('Regression check, revision 3', [
    ('WHAT CHANGED HERE', N('Only what the corrections touch everywhere: the crown&rsquo;s deck states the service consequence (&ldquo;after ten the trains skip your stop; surface route, 25 minutes longer&rdquo;), Dana&rsquo;s row carries no bookshop, and the codas name commitments only. Priority behaviour is unchanged: one ask, the rest folded and reachable, the same page plus one changed row afterward.')),
    ('CHECKED', N('Before and after are the H1 system: crown, rows, &ldquo;Worth knowing&rdquo;, the city, the seam. During: oxblood read, one crown with one instrument and one ask, two unchanged rows, the rest folded to three reachable titles, the seam marking Saturday with the open question. After: the before page plus one changed row.')),
    ('WHAT PERSISTS', ledger([('ANSWERING', 'A preference on the Occasion, attributed to you.'), ('NOT ANSWERING', 'Nothing. The crown expires at 7:00; Alex decides.'), ('NEVER', 'A pending badge; &ldquo;you didn&rsquo;t answer&rdquo;.')])),
    ('PRODUCTION', N('Everything on these three phones is structured state (Occasion, commitment, rows), reusable researched content (the mechanism, the technique), or a city notice. The only new work the change triggers is the two-place comparison, composed from the Occasion&rsquo;s candidates; no prose is generated.')),
], w=420)

def H4():
    cols = [col(h4v2_before(), caption('BEFORE &middot; THURSDAY 5:40', 'The fuller Thursday', 'CROWN + ROWS + WORTH KNOWING + THE CITY')),
            col(h4v2_during(), caption('DURING &middot; 6:05', 'One decision, 55 minutes', 'ONE ASK &middot; THE REST FOLDS, STAYS REACHABLE')),
            col(h4v2_after(), caption('AFTER &middot; 7:25', 'The fuller Home returns', 'THE SAME PAGE PLUS ONE CHANGED ROW')),
            H4_NOTES]
    return board_page(1880, 1825, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H4 &middot; PRIORITY STRESS TEST &middot; PROPOSAL', 'H4 &middot; A genuine priority, checked against the revised system',
                      'Same mature account, Thursday evening. Saturday&rsquo;s arrangement loses its place and Alex asks for one preference by seven.', cols, FOOT)

# ───────────────────────────── H5 v2 ─────────────────────────────
def h5v2():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '11:20 AM') + orientation('Home. Clear, 64&deg;, low water at 2:40.', 'Landed 6:40 &middot; Saturday is dinner with Maya and Alex.')
    inner += gut(ways_card('This afternoon', [
        ('The pier at low water', 'The first walk back can be the one you know.', 'LOW WATER 2:40&ndash;5'),
        ('Cook the Sorrento dish', 'Sauce meets pasta ninety seconds early, finished in the pan &mdash; the texture you photographed.', 'TONIGHT, OR SATURDAY FOR MAYA AND ALEX'),
        ('Stay in', 'The noodle shop delivers until ten.', 'ANY TIME'),
    ], 'PHOTOS IMPORTING &middot; 412 OF 690'), top=22)
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled &middot; Maya added a photograph Friday</span>', avatars=['M', 'A', 'you'])
                                     + row('Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(u2('The texture you photographed came from the last minute at the stove',
        'A thin film that holds the ridges, finished in the pan &mdash; a starch-supported emulsion. What that kitchen actually did is not known; this is what the plate shows.',
        photo(150, 'YOUR PHOTOGRAPH &middot; SORRENTO &middot; SLOT', [('1', 18, 18), ('2', 300, 84)]) + callouts([('1', 'Film, not pool.'), ('2', 'Integrated at service, not added after.')]),
        meta_t='YOUR PHOTOGRAPH &middot; SORRENTO, LAST TUESDAY', door_text='How to get it at home'))
    inner += sect('From the trip') + gut(u2('Sorrento to Amalfi by ferry: the harbor at 9:14, the Amalfi quay by 10:02',
        'The morning you left the peninsula, from your ticket and two photographs. The rest of the trip fills in as the photos import; gaps stay gaps.',
        f'<div style="display: flex; gap: 10px; align-items: center; margin-top: 8px;"><span class="kick" style="color: {INK};">9:10</span><span style="flex: 1; height: 2px; background: {GOLD};"></span><span class="kick" style="color: {INK};">9:14</span><span style="flex: 1; height: 2px; background: {GOLD};"></span><span class="kick" style="color: {INK};">10:02</span></div>',
        meta_t='TICKET 9:10 &middot; PHOTOGRAPHS 9:14, 10:02 &middot; 412 OF 690 IMPORTED', door_text='The trip, in Life'))
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon.', last=True) + '</div>')
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), 'market', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK)],
                    'Saturday, dinner with Maya and Alex.')
    return phone(inner, 0)

H5_NOTES = notecol('Dispositions A and D, on H5', [
    ('A &middot; ALTERNATIVES', N('&ldquo;This afternoon&rdquo; is unnumbered; each option carries its own window (low water 2:40&ndash;5 &middot; tonight, or Saturday &middot; any time), separated by &ldquo;or&rdquo;.')),
    ('D &middot; THE DISH', N('&ldquo;A dish for three is the honest test&rdquo; is gone. The option reads as a cooking possibility with its technique; the finding&rsquo;s door is &ldquo;How to get it at home&rdquo;. Saturday&rsquo;s dinner is never made into validation work, and the coda names only the dinner.')),
    ('D &middot; THE JOURNEY', N('&ldquo;The only leg documented from departure to arrival&rdquo; is gone. The unit is the ferry morning itself &mdash; the harbor at 9:14, the Amalfi quay by 10:02, from a ticket and two photographs &mdash; with evidence quality in the supporting line (&ldquo;gaps stay gaps&rdquo;). A departure ticket is not treated as proof of boarding; the photographs carry the arrival.')),
    ('CHECKED', N('H1&rsquo;s composition unchanged: read, a prepared-afternoon card, rows, &ldquo;Worth knowing&rdquo; (the photograph as a media-led finding), &ldquo;From the trip&rdquo; (one reconstruction, low), the city, the seam. Import progress is one metadata clause on the afternoon card.')),
    ('PRODUCTION', N('The dish explanation is reusable researched content (a general mechanism) selected because of the person&rsquo;s photograph; only the two callouts are personal. The leg is structured state composed from tickets and timestamps. No bespoke prose is required for this page.')),
], w=420)

def H5():
    cols = [col(v2('h5v2'), caption('BEFORE &middot; REVISION 2', 'New York first, composed', 'THE WORKING BASELINE')),
            col(h5v2(), caption('AFTER &middot; REVISION 3', 'Alternatives, and the journey itself', 'A &middot; UNNUMBERED OPTIONS &middot; D &middot; THE DISH AS A POSSIBILITY, THE FERRY MORNING AS THE UNIT')),
            H5_NOTES]
    return board_page(1440, 2165, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H5 &middot; RETURN HOME &middot; PROPOSAL', 'H5 &middot; Coming home, checked against the revised system',
                      'Persona B, the Sunday of landing. Current-world value first while imports finish; status as one clause; one reconstruction low on the page.', cols, FOOT)

# ───────────────────────────── H0 v2 ─────────────────────────────
def H0(diag):
    def blk(t, html): return f'<div style="display: flex; flex-direction: column; gap: 10px;"><div class="shead"><span>{t}</span><span class="rule"></span></div>{html}</div>'
    def tbl(cols, rows):
        h = ''.join(f'<th style="text-align: left; font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; padding: 6px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.14); vertical-align: bottom;">{c}</th>' for c in cols)
        b = ''.join('<tr>' + ''.join(f'<td style="font-size: 12.5px; line-height: 17px; color: {INK2}; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">{c}</td>' for c in r) + '</tr>' for r in rows)
        return f'<table style="border-collapse: collapse; width: 100%;"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
    system = blk('THE RECOMMENDED COMPOSITION &middot; REVISED', N(
        '<b>Read</b> (one or two lines) &rarr; <b>the lead</b>: whatever is strongest now, in the form that fits it &mdash; a commitment crown, a shared-arrangement card, a friend&rsquo;s media-led share, a prepared-afternoon card &rarr; <b>In motion</b> (rows) &rarr; a small number of further units, each in the form that fits the material: '
        'cards for coherent objects and experiences (an arrangement, a share, a prepared afternoon, a reading preview), instruments for comparisons, bare units for findings and techniques, fact rows for service updates and city notices &rarr; <b>the seam + one forward line</b>.<br><br>'
        '<b>Typography, four jobs:</b> section heading (sans 13/600, sentence case, hairline; only where it navigates) &middot; content title (serif, first line of every unit) &middot; metadata (one mono line: time, distance, date, source) &middot; supporting text (one or two sentences). '
        '<b>Containment, selective:</b> cards make objects recognizable; they are not reserved for urgency (D-H1 withdrawn) and not applied to every sentence. <b>Budgets</b> describe judgment, not quotas: one thing may dominate, few may ask, several may be enjoyable without action, depth stays behind doors. '
        '<b>Rationale off the surface:</b> what stays visible is authorship, audience where it matters, the sample mark, and a material uncertainty.'))
    diag_t = blk('BEFORE / AFTER DIAGNOSTICS &middot; VISIBLE WORDS AND SCROLL HEIGHT (NOT TARGETS)', tbl(['PHONE', 'REVISION 1', 'REVISION 2', 'REVISION 3', 'WHAT REVISION 3 CHANGED'], [
        ['H1 Sunday', diag['h1v1'], diag['h1v2'], diag['h1v3'], 'Unnumbered options with windows; Dana&rsquo;s row and the coda stop paraphrasing'],
        ['H2 Treatment 2', diag['h2v1_t2'], diag['h2v2_t2'], diag['h2v3_t2'], 'Dana once (her card); the Sunday unit removed; the coda names commitments only'],
        ['H3 first open', diag['h3v1_first'], diag['h3v2_first'], diag['h3v3_first'], 'Sample first; one city offering beside it; the rest lower; nonpersonal language'],
    ]))
    disp = blk('DISPOSITIONS &middot; SECTION 5.3, A&ndash;E', tbl(['', 'CORRECTION', 'DISPOSITION', 'LEFT UNCHANGED, AND WHY'], [
        ['A', 'Alternatives are not an itinerary (H1, H5)', 'Applied: unnumbered options, hollow marks, each with its own time window, &ldquo;or&rdquo; hairlines between them. Sequencing only inside an option. No selection control added.', 'The card stays contained and consumable; the option titles keep their verbs because they describe the option, not an instruction.'],
        ['B', 'Preserve the person, remove the echoes (H2)', 'Applied: Dana appears once in Treatment 2 (her handoff card, with the distinct distance-to-bakery fact); her row and the codas on every board stop paraphrasing; the Sunday unit is removed from T2 and kept once in T1, which has no region.', 'Alex&rsquo;s arrangement stays as a card <i>and</i> a settled row on H4-after because the row carries a new fact (settled, where, when).'],
        ['C', 'Reveal the product before the city briefing (H3)', 'Applied: sample first, the cold beneath it, the L and Open House lower. &ldquo;Your walk&rdquo; &rarr; &ldquo;the waterfront streets&rdquo;; no workplace, starting point, or attendance implied in the sample or the return crown.', 'The cold stays on the first screen as the one worthwhile city offering; the Sample label and both actions unchanged.'],
        ['D', 'Replace analytical framing with the useful result (H3, H5)', 'Applied: the three named phrases and their siblings rewritten as the practical consequence, the cooking possibility, and the ferry morning. Uncertainty kept in supporting lines.', '&ldquo;What that kitchen actually did is not known&rdquo; and &ldquo;gaps stay gaps&rdquo; remain: material uncertainty, not process narration.'],
        ['E', 'Distinguish reuse from prediction, inference, and measured cost (H0)', 'Applied: the cold row names station data or a microclimate model and marks the four-degree figure a fixture; the photograph row is inference (vision, retrieval, uncertainty) before reuse; every &ldquo;none new&rdquo; became &ldquo;no new generation expected&rdquo; with the applicable retrieval, permission, media, refresh, and provider costs; the sample separates one-time preparation from delivery and maintenance. The handback separates design intent, verified implementation, and measured economics.', 'No mechanism library, data provider, or infrastructure is commissioned to make the ledger look complete; unknowns stay unknown.'],
    ]))
    prod = blk('PRODUCTION LEDGER &middot; EVERY VISIBLE UNIT, BY CLASS', tbl(['UNIT', 'PRODUCTION CLASS', 'LIKELY TRIGGER', 'REUSE / AUDIENCE SCOPE', 'FRESHNESS / INVALIDATION', 'FALLBACK', 'COST &middot; NOT MEASURED'], [
        ['Read (weather, low water, what dominates)', 'Structured state + world information', 'Each open; composed, not written', 'Per person; world facts shared', 'Forecast/tide refresh; held dates change', 'World line only', 'Weather/tide source pricing'],
        ['Commitment crown (the show)', 'Structured state', 'A held commitment within its window', 'Per person', 'Service read; hall posts set times', 'Crown without the instrument', 'Service-read frequency'],
        ['Arrangement card (Alex)', 'Structured state (Occasion) + owner&rsquo;s words', 'Occasion changes', 'Participants only', 'Any Occasion write; expiry', 'Row only', 'No new generation expected; retrieval, permission checks, refresh apply'],
        ['Friend&rsquo;s share (Maya)', 'Human-authored', 'Grant exists and is timely', 'Author&rsquo;s audience, until expiry', 'Withdrawal/narrowing removes it and derivatives', 'Not shown', 'Media delivery'],
        ['Handoff (Dana)', 'Human-authored + Place', 'Addressed material', 'Recipient only', 'Withdrawal; Place change', 'Row only', 'No new generation expected; retrieval, permission checks, refresh apply'],
        ['Theo&rsquo;s note inside the market', 'Human-authored (may-use)', 'Grant covers the market', 'Recipient only', 'Grant expiry reverts the window', 'Rhythm without the quote', 'No new generation expected; grant check + retrieval'],
        ['Today / This afternoon card', 'Personal relevance (select + connect)', 'Open on a day with &ge;2 grounded options', 'Per person', 'Any option&rsquo;s world fact changes', 'Fewer items; never invented', 'Rhythm/tide owners'],
        ['Market rhythm instrument', 'Current world information', 'Weekly', 'Shared across people', 'Season/schedule change', 'Hours only', 'Source availability'],
        ['The cold split (mechanism + numbers)', 'Reusable researched content (the exposure mechanism) + world information (two station observations or a microclimate model)', 'A forecast condition matches a stored mechanism <b>and</b> station data exists for both sides', 'Shared explanation; the two numbers are per-location data, not inference from the prose', 'Forecast/station refresh re-composes numbers, not prose', 'Without station data: a bounded explanation with no exact figures (&ldquo;colder near the water&rdquo;)', 'Station/forecast provider; authoring the mechanism; <b>the four-degree figure is a fixture, not a supported prediction</b>'],
        ['The skillet technique', 'Reusable researched content, selected by the person&rsquo;s note', 'The note exists; not yet tried', 'Shared technique; private trigger', 'Retires after tried or ignored twice', 'Not shown', 'No new generation expected; retrieval + retirement bookkeeping'],
        ['City fact rows', 'Current world information', 'Notice within window and city', 'Shared', 'Notice expiry', 'Not shown', 'Notice source + licensing'],
        ['Reading preview', 'Optional depth (existing content object)', 'Held book; chapter unread', 'Personal copy', 'Once opened', 'Not shown', 'Rights per source'],
        ['Sample card + sheet', 'Fixed, labelled demonstration', 'No personal history for that capability', 'Shared across accounts', 'Retires after tried or ignored twice', 'The city carries the page', 'One-time preparation; delivery and maintenance ongoing (media, refresh when the hall fixture changes)'],
        ['The dish photograph finding', 'Personal relevance <b>via inference</b>: a vision pass on the photograph, retrieval of a matching mechanism, uncertainty handling; reusable prose only after that work', 'A photograph with a plausible match', 'Private', 'Correction invalidates callouts', 'Photo without callouts, or not shown', 'Vision + retrieval per photograph; false-match risk; not eliminated by reusing the prose'],
        ['The one complete leg', 'Structured state (reconstruction)', 'Import milestone', 'Private', 'More imports; corrections', 'Not shown until clean', 'Import processing'],
        ['Priority crown with two-place comparison (H4)', 'Structured state (Occasion candidates)', 'Owner asks a decision by deadline', 'Participants', 'Deadline; owner settles', 'Rows only', 'No new generation expected; Occasion reads, deadline timer'],
        ['Bespoke synthesis', 'Targeted generation', 'Only when a cross-source result earns it', 'Per evidence scope', 'Source change/revocation', 'Silence', '<b>Unknown</b>: frequency, tokens, reuse rate'],
    ]))
    ops = blk('OPERATING BEHAVIOURS DESIGNED TOWARD', N('Opening Home retrieves and composes; it does not launch writing jobs per slot. New work is justified by a source change, a stale fact, a new authorized contribution, or deliberate exploration &mdash; not by a repeat visit. Live facts (hours, forecast, service) are separated from durable explanation so an update re-composes numbers without rewriting prose. Generated results are kept and reused while valid. If deeper work is unavailable or over budget, the page stays useful with structured state, human material, and city facts; no fabricated result, no loading promise, no assignment to the person. '
        '<b>Cost unknowns named:</b> generation frequency, token/tool usage, reuse rate, and cost per active user are not known from static boards; the producer&rsquo;s per-call limits and prompt caching do not establish account-level economics.'))
    decisions = blk('DECISION LOG &middot; REVISED', tbl(['#', 'DECISION OR ASSUMPTION', 'STATUS'], [
        ['D-H1', '<s>A crown renders only when something operational is at stake.</s> <b>Withdrawn.</b> Cards make coherent objects and experiences recognizable; containment is selective, not reserved for urgency.', 'Withdrawn this pass'],
        ['D-H2', 'The &ldquo;one relational opening&rdquo; law (MP2) read as a dominance + demand rule, not a page-wide count of authored material. Treatment 2 depends on this reading.', '<b>Founder ruling requested</b>'],
        ['D-H3', 'Social budget: one social cause may lead; one social unit may ask; authored material below is bounded by no-duplicate and disappears-when-empty, not a number.', 'Proposed; reported'],
        ['D-H4', 'Browsing beyond selection routes to Life &middot; People; no present-tense aperture created.', 'Proposed; social-aperture lane owns the question'],
        ['D-H5', 'Codas drop relief language; pages end on the seam and one forward line.', 'Adopted'],
        ['D-H6', 'City facts are marked by their source metadata, not by a disclaimer; they need a city-scoped source with freshness and licensing.', 'Proposed; content-production dependency'],
        ['D-H7', 'The SAMPLE convention: a stamped, dashed input and its result; fixed and reusable across accounts; retires after tried or ignored twice.', 'Proposed'],
        ['D-H8', 'Ignored units create no debt and no negative preference.', 'Consistent with canon; adopted'],
        ['D-H9', 'H4 uses the Sept 4 owner-controlled collaboration posture; runtime unverified.', 'Assumption on Components &amp; Plan'],
        ['D-H10', 'Typography roles: sans section heading / serif content title / one mono metadata line / short supporting text. Tested here within the existing system; the kernel&rsquo;s kicker registers (&sect;12.7 c) would need amending if adopted.', '<b>Proposed amendment</b> to the design kernel'],
        ['D-H11', 'Production classes per unit (human-authored / structured / retrieved-reusable / personally adapted / bespoke) with trigger, reuse, freshness, fallback are proposed responsibilities for engineering review, not claims of current implementation.', 'Proposed; engineering review'],
    ]))
    review = blk('THE FIFTEEN QUESTIONS &middot; PER PAGE', tbl(['Q', 'H1', 'H2 (T2)', 'H3 (first)', 'H4 (during)', 'H5'], [
        ['1 First glance useful', 'Weather, low water, Maya&rsquo;s loaf', 'Alex&rsquo;s Saturday', 'The cold, the L, a sample', 'What fell through, by when', 'Weather, low water, three ways'],
        ['2 Other reasons to stay', 'Today, the cold, the skillet, the city, the reading', 'The market, Sunday, the cold', 'Two facts, three capabilities', 'The rest, folded', 'The dish, the leg, the city'],
        ['3 Received before any ask', 'Everything; no ask', 'Everything; no ask', 'Everything', 'Both options and Maya&rsquo;s view', 'Everything; no ask'],
        ['4 Longer scroll adds different value', 'Share &rarr; ways &rarr; rows &rarr; findings &rarr; city &rarr; reading', 'Arrangement &rarr; rows &rarr; week &rarr; people &rarr; finding', 'City &rarr; sample &rarr; capabilities', 'Folded', 'Ways &rarr; rows &rarr; photo &rarr; leg &rarr; city'],
        ['5 Ordinary competence', 'Low water, the cold, the skillet', 'The market window, the pier', 'The L after 11', 'Which place fits', 'The dish timing'],
        ['6 People, not avatars', 'Maya&rsquo;s photograph and words', 'Four people in their own words', '&mdash;', 'Alex asks; Maya answered', 'Maya&rsquo;s photograph on the dinner'],
        ['7 Find shared material', 'Door at the foot', 'Region + door', '&mdash;', 'Occasion door', 'Dinner row'],
        ['8 Solo / thin still worthwhile', 'Sparse variant on H2', 'Yes', 'Yes', 'Yes', 'Yes'],
        ['9 New users see benefits', '&mdash;', '&mdash;', 'Stub &rarr; evening; three rows', '&mdash;', '&mdash;'],
        ['10 Priority unmistakable', 'No priority today', 'The arrangement leads', 'No priority', 'Yes', 'No priority'],
        ['11 Calm with anticipation', 'The forward line', 'The forward line', '&ldquo;Bring one thing&rdquo;', '&ldquo;where you left it&rdquo;', 'The forward line'],
        ['12 Stop freely', 'Yes', 'Yes', 'Yes', 'One ask, then it expires', 'Yes'],
        ['13 Section / object / title / metadata distinguishable', 'Sans headings; three cards; serif titles; one mono line', 'Same; two card kinds + rows', 'Same; stub + result', 'Same; oxblood read + crown', 'Same'],
        ['14 Capability shown as a result', '&mdash;', '&mdash;', 'Yes: stub &rarr; evening', '&mdash;', 'Yes: photo &rarr; finding'],
        ['15 Without new generation', 'All but none: share, state, rhythm, stored mechanism, technique, notices, reading', 'All', 'All (sample is fixed)', 'All (comparison composed)', 'All but the two callouts'],
    ]))
    handback = blk('HANDBACK &middot; DESIGN INTENT / VERIFIED IMPLEMENTATION / MEASURED ECONOMICS KEPT APART', N('<b>Design intent (these boards):</b> the composition, the production classes, the triggers and fallbacks as proposed responsibilities. <b>Verified implementation:</b> only what earlier passes established &mdash; Chat intake with T1 receipt and Undo, Life holding a ticket, the commitment crown, service reads, share projection under grants (MP1), reconstruction (09-02). Everything else on the ledger is unverified. <b>Measured economics:</b> none. Generation frequency, token and tool usage, reuse rate, retrieval and provider costs, and cost per active user are unmeasured; nothing here shows the fuller Home is affordable or unaffordable.<br><br><b>Boards (project &ldquo;Vesper &mdash; Home&rdquo;), revised in place with revision 2 kept beside them:</b> H0 - Ledger and Decisions &middot; H1 - Ordinary Sunday Generous &middot; H2 - Social Week Two Treatments &middot; H3 - First Open to Next Open &middot; H4 - Priority Stress Test &middot; H5 - Return Home Corrected. Board 1&ndash;4 untouched.<br><br>'
        '<b>Content production:</b> a city notice source with freshness and licensing; a library of bounded mechanisms with one source each; world rhythms with owners; photographs for plates; the fixed sample demonstrations.<br>'
        '<b>Engineering verification:</b> grant-scoped share reads with audience and expiry; Occasion decision-by-deadline; a notice linked to a held commitment; sample retirement; fold-and-return; exposure suppression without inferred knowledge; separation of live facts from durable explanation; result retention and reuse.<br>'
        '<b>Not shown:</b> large-text renders; native behaviour; participant evidence. No static page proves live behaviour or economics.'))
    inner = (head('VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; REVISION 3 &middot; H0 &middot; DISPOSITIONS, PRODUCTION, DECISIONS, HANDBACK', 'H0 &middot; One composition, five dispositions, and a ledger that does not overclaim',
                  'The dispositions for section 5.3 A&ndash;E; diagnostics across three revisions; every visible unit classified by production class with reuse separated from prediction and inference, and cost named as unmeasured; the decision log; the fifteen questions; the handback with design intent, verified implementation, and measured economics kept apart.')
             + '<div style="display: flex; flex-direction: column; gap: 34px;">' + system + disp + diag_t + prod + ops + decisions + review + handback + '</div>')
    return (HEAD + f'<div style="width: 1560px; min-height: 3665px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL)

PHONES_FOR_DIAG = {'h1v3': h1v2, 'h2v3_t2': h2v2_t2, 'h3v3_first': h3v2_first}

if __name__ == '__main__':
    import json
    diag = json.load(open(os.path.join(OUT, 'diag.json'))) if os.path.exists(os.path.join(OUT, 'diag.json')) else {}
    diag = {k: diag.get(k, '&mdash;') for k in ['h1v1','h1v2','h1v3','h2v1_t2','h2v2_t2','h2v3_t2','h3v1_first','h3v2_first','h3v3_first']}
    for name, fn in [('H1 - Ordinary Sunday Generous', H1), ('H2 - Social Week Two Treatments', H2), ('H3 - First Open to Next Open', H3), ('H4 - Priority Stress Test', H4), ('H5 - Return Home Corrected', H5)]:
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
    open(os.path.join(OUT, 'H0 - Ledger and Decisions.dc.html'), 'w').write(H0(diag)); print('wrote H0')
    # standalone phones for the diagnostics render
    os.makedirs(os.path.join(OUT, 'diag'), exist_ok=True)
    for k, fn in PHONES_FOR_DIAG.items():
        open(os.path.join(OUT, 'diag', k + '.html'), 'w').write(HEAD + fn() + TAIL)
    for k in ['h1v1', 'h2v1_t2', 'h3v1_first']:
        open(os.path.join(OUT, 'diag', k + '.html'), 'w').write(HEAD + v1(k) + TAIL)
    for k in ['h1v2', 'h2v2_t2', 'h3v2_first']:
        open(os.path.join(OUT, 'diag', k + '.html'), 'w').write(HEAD + v2(k) + TAIL)
