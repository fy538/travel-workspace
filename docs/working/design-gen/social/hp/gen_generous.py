"""Vesper — Home · the generous-value pass (H0–H5).
Thesis: a short visit worthwhile, a longer visit rewarding. One priority
organizes the page; it does not exhaust what the page offers. All world facts
are fixtures and are labelled so on every board."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
from gen_home import live, between, PASSAGE_CH4
from gen_homeproj import extract_div, lift_phone

OUT = os.path.join(os.path.dirname(__file__), 'homeproj'); os.makedirs(OUT, exist_ok=True)
FX = 'FIXTURE'

# ───────────────────────────── the generous system · components ─────────────────────────────
def body(t, col=None): return f'<div style="font-size: 12.5px; line-height: 17px; color: {col or MUTE};">{t}</div>'
def small(t): return f'<div class="fn">{t}</div>'
def gut(inner, top=0): return f'<div style="padding: {top}px 22px 0 22px;">{inner}</div>'

def facepile(letters, size=22, tuck=-7):
    out = '<span style="display: inline-flex; align-items: center; flex: none;">'
    for i, l in enumerate(letters):
        col = UMBER if l == 'you' else INK
        t = 'N' if l == 'you' else l
        out += f'<span style="width: {size}px; height: {size}px; border-radius: 999px; background: {col}; color: {CARD}; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {PAPER}; margin-left: {tuck if i else 0}px;">{t}</span>'
    return out + '</span>'

def unit(kick, title, text='', media='', door_text=None, fn='', big=False, kick_col=None):
    """A bare unit on paper: gold kicker · serif title that carries the finding · grey proof/limit · optional media · optional door."""
    ts = 'font-size: 22px; line-height: 26px; font-weight: 600; letter-spacing: -0.2px;' if big else 'font-size: 17px; line-height: 22px; font-weight: 500;'
    out = f'<div style="display: flex; flex-direction: column; gap: 5px;"><span class="kick" style="color: {kick_col or GOLDD};">{kick}</span>'
    out += f'<span style="{SERIF} {ts} color: {INK};">{title}</span>'
    if text: out += body(text, INK2 if big else MUTE)
    out += media
    if door_text: out += door(door_text)
    if fn: out += small(fn)
    return out + '</div>'

def share(letter, who, when, words, plate_h=0, plate_cap='', meta='', door_text=None):
    """An authored human share: the author's actual words, kept theirs, with audience + expiry visible."""
    pl = ''
    if plate_h:
        pl = (f'<div style="height: {plate_h}px; border-radius: 12px; background: #2A241E; position: relative; overflow: hidden; margin: 4px 0 2px 0;">'
              f'<div class="fn" style="position: absolute; left: 14px; bottom: 12px; color: #8F877C;">{plate_cap}</div></div>')
    out = (f'<div style="display: flex; gap: 12px; align-items: flex-start;">'
           f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex: none;">{letter}</span>'
           f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 13px; font-weight: 600; color: {INK};">{who}</span><span class="fn">{when}</span></div>'
           + pl + f'<div style="{SERIF} font-size: 17px; line-height: 23px; color: {INK};">&ldquo;{words}&rdquo;</div>')
    if meta: out += body(meta)
    if door_text: out += door(door_text)
    return out + '</div></div>'

def arow(text, avatars=None, mark='dot', color=MUTE, last=False):
    """In-motion row with an optional facepile lead (a person or persons are the subject)."""
    if avatars:
        lead = facepile(avatars, 28, -8)
        bb = ' border-bottom: 1px solid rgba(27,23,20,0.06);' if last else ''
        return f'<div class="row" style="padding: 8px 0;{bb}">{lead}<span style="font-size: 15px; line-height: 20px; flex: 1; color: {INK};">{text}</span>{CHEV}</div>'
    return row(text, mark=mark, color=color, last=last)

def three_ways(kick, items):
    """'Today, three ways' — a compact field of grounded alternatives; each a title + payoff clause. items: [(title, payoff)]"""
    out = f'<div style="display: flex; flex-direction: column; gap: 4px;"><span class="kick" style="color: {GOLDD};">{kick}</span>'
    for i, (t, p) in enumerate(items):
        bt = 'border-top: 1px solid rgba(27,23,20,0.06);' if i else ''
        out += (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 9px 0; {bt}"><span class="kick" style="min-width: 12px; color: {ANCHOR}; padding-top: 3px;">{i+1}</span>'
                f'<div style="flex: 1;"><div style="{SERIF} font-size: 16px; line-height: 21px; font-weight: 500; color: {INK};">{t}</div>{body(p)}</div></div>')
    return out + '</div>'

def compare2(a_k, a_v, a_s, b_k, b_v, b_s):
    """A bare two-column contrast (no container): kicker · big value · one clause each."""
    def side(k, v, s): return (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 3px;"><span class="kickm">{k}</span>'
                               f'<span style="{SERIF} font-size: 26px; line-height: 30px; font-weight: 600; color: {INK};">{v}</span>{body(s)}</div>')
    return f'<div style="display: flex; gap: 18px; margin-top: 6px; padding-top: 8px; border-top: 1px solid rgba(27,23,20,0.06);">{side(a_k, a_v, a_s)}{side(b_k, b_v, b_s)}</div>'

def span(label_a, a0, a1, a_end, label_b=None, b0=0, b1=0, b_end='', start='', end='', w=349):
    """Arrival-span instrument on a bare line; a = gold span, b = dashed hollow alternative."""
    s = f'<svg width="{w}" height="{74 if label_b else 50}" viewBox="0 0 {w} {74 if label_b else 50}" fill="none" style="width: 100%; height: auto; margin-top: 8px;">'
    s += f'<text x="{a0}" y="11" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">{label_a}</text>'
    s += f'<rect x="2" y="22" width="{w-4}" height="6" rx="3" fill="rgba(27,23,20,0.07)"/><rect x="{a0}" y="18" width="{a1-a0}" height="14" rx="7" fill="#B0853A"/>'
    s += f'<text x="{a1+8}" y="29" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">{a_end}</text>'
    if label_b:
        s += f'<text x="{b0}" y="52" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">{label_b}</text>'
        s += f'<rect x="{b0}" y="58" width="{b1-b0}" height="8" rx="4" fill="none" stroke="#6E6862" stroke-width="1.2" stroke-dasharray="3 3"/>'
        s += f'<text x="{b1+8}" y="66" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#6E6862">{b_end}</text>'
    y = 47 if not label_b else 84
    if label_b: s = s.replace(f'height="74" viewBox="0 0 {w} 74"', f'height="88" viewBox="0 0 {w} 88"')
    s += f'<text x="2" y="{y}" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">{start}</text><text x="{w-2}" y="{y}" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">{end}</text>'
    return s + '</svg>'

def photo(h, cap, callouts=()):
    out = f'<div style="height: {h}px; border-radius: 12px; background: #2A241E; position: relative; overflow: hidden; margin-top: 6px;">'
    for n, x, y in callouts:
        out += f'<span style="position: absolute; left: {x}px; top: {y}px; width: 22px; height: 22px; border-radius: 11px; background: {GOLD}; color: {INK}; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center;">{n}</span>'
    return out + f'<div class="fn" style="position: absolute; left: 14px; bottom: 12px; color: #8F877C;">{cap}</div></div>'

def callouts(items):
    return '<div style="display: flex; flex-direction: column; gap: 5px; margin-top: 8px;">' + ''.join(
        f'<div style="display: flex; gap: 10px; font-size: 14px; line-height: 19px; color: {INK};"><span class="kick" style="min-width: 12px;">{n}</span><span>{t}</span></div>' for n, t in items) + '</div>'

def people_region(units, door_text='Everything shared with you'):
    """The conditional 'From your people' grouping: only renders when ≥2 units of authored material are not already used in full above; ends with the pull door."""
    out = section('FROM YOUR PEOPLE') + '<div style="padding: 0 22px; display: flex; flex-direction: column; gap: 26px;">' + ''.join(units)
    return out + f'<div>{door(door_text)}<div class="fn" style="margin-top: -6px;">LIFE &middot; PEOPLE &middot; EVERYTHING ADDRESSED OR SHARED TO YOU, BY PERSON, NEVER RANKED</div></div></div>'

def city_unit(kick, title, text, fn='FROM THE CITY &middot; NOT INFERRED FROM YOU'):
    return unit(kick, title, text, fn=fn, kick_col=MUTE)

def ending(days, line, top=40):
    """How a page ends now: the coming days as a banded seam + one forward line. No relief language."""
    return week_seam(days, top=top) + f'<div style="padding: 16px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">{line}</div></div>'

def collapsed(kick, items):
    """Reachable, compressed: the rest of the page folded to one-line titles while a priority holds."""
    out = f'<div style="display: flex; flex-direction: column; gap: 4px;"><span class="kickm">{kick}</span>'
    for t in items:
        out += f'<div style="display: flex; align-items: center; gap: 10px; min-height: 36px; border-top: 1px solid rgba(27,23,20,0.06);"><span style="font-size: 14px; color: {MUTE}; flex: 1;">{t}</span>{CHEV}</div>'
    return out + '</div>'

def sample_unit(title, text, door_text, try_text):
    """A clearly labelled demonstration: sample input + sample result, inspectable without uploading anything."""
    return (f'<div style="border: 1px dashed rgba(27,23,20,0.28); border-radius: 12px; padding: 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div style="display: flex; align-items: center; gap: 8px;"><span class="kick" style="color: {MUTE};">SAMPLE &middot; NOT YOURS</span><span class="fn">A MADE-UP TICKET, READ THE WAY YOURS WOULD BE</span></div>'
            f'<div style="{SERIF} font-size: 17px; line-height: 22px; font-weight: 500; color: {INK};">{title}</div>{body(text)}'
            f'<div style="display: flex; gap: 18px; align-items: center;">{door(door_text)}{door(try_text, INK)}</div></div>')

def caption(k, t, s2=''):
    return f'<div style="display: flex; flex-direction: column; gap: 3px; padding: 0 0 10px 2px;"><div class="kick" style="color: {GOLDD};">{k}</div><div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px; color: {INK};">{t}</div><div class="fn" style="line-height: 14px;">{s2}</div></div>'

def col(ph, cap, w=393):
    ph = re.sub(r'(<div style="width: 393px;[^"]*?)min-height: \d+px;', r'\1min-height: 0;', ph, count=1)
    return f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column;">{cap}{ph}</div>'

def head(kick, title, sub):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 26px;"><div class="kick">{kick}</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">{title}</div>'
            f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">{sub}</div></div>')

def board_page(w, h, kick, title, sub, cols, foot):
    return (HEAD + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, title, sub) + '<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols) + '</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)

FOOT = 'EVERY WORLD FACT (WEATHER, TIDES, HOURS, RHYTHMS, SERVICE, DATES), EVERY PASSAGE AND EVERY PERSON IS A DESIGN FIXTURE &middot; PHOTOGRAPH PLATES ARE SLOTS &middot; DESIGN DOCTRINE STAYS OUTSIDE THE PHONE &middot; A STATIC MOCKUP PROVES NO LIVE BEHAVIOUR'
N = lambda t: f'<div style="font-size: 12.5px; line-height: 18px; color: {INK2};">{t}</div>'

# ───────────────────────────── the shared week (Persona A, extended) ─────────────────────────────
WEEK_SUN = [('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE),
            ('THU', dm('dashed', MUTE), '28&deg;', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'Alex', INK)]

def in_motion_A(today='SUN', with_alex=True, with_dana=True, with_show=True, dentist='Dentist Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; at nine &middot; walk, the bus is slower</span>'):
    rows = []
    if with_alex: rows.append(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still open &middot; he asked for &ldquo;walkable from the L, not a restaurant&rdquo;</span>', avatars=['A', 'M', 'you']))
    if with_dana: rows.append(arow('Dana &middot; Saturday the 19th &middot; <span style="color: #6E6862;">&ldquo;keep Sunday morning for me&rdquo; &middot; she sent a bookshop for it</span>', avatars=['D']))
    if with_show: rows.append(row('The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">from your ticket &middot; set times not posted</span>', mark='solid', color=GOLD))
    rows.append(row(dentist, mark='dashed'))
    rows[-1] = rows[-1].replace('padding: 8px 0;"', 'padding: 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06);"')
    return section('IN MOTION') + gut(''.join(rows))

# ───────────────────────────── H1 · ordinary Sunday, generous ─────────────────────────────
def h1_generous():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', 'Warming to 54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    # dominance: the strongest current unit — a friend's authored share that is timely today. Not a crown: nothing operational is at stake.
    inner += gut(share('M', 'Maya', 'SHARED FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY',
                       'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.',
                       plate_h=150, plate_cap='MAYA&rsquo;S PHOTOGRAPH &middot; THE PLATE IS A SLOT',
                       meta='14 minutes by bike from you &middot; open now &middot; her words, kept hers. Nothing to reply to.',
                       door_text='The bakery, in Places'), top=22)
    # the coming days: three grounded ways to spend the day, none assigned
    inner += gut(three_ways('TODAY, THREE WAYS', [
        ('The loaf, then the water: bakery by 10:30, low water on the pier at 1:40', 'One ride, two things that only happen today. The pier is 9 minutes from the bakery.'),
        ('The flood line on your coffee route, walked at low water', 'Between 1:40 and 4 the granite kerbs show exactly where the gates&rsquo; protection ends. From chapter 3 of the harbor book.'),
        ('Stay in. Tonight&rsquo;s skillet, preheated dry', 'Thursday&rsquo;s soggy crust was the pan, not the dough. Four minutes dry before the oil fixes it.'),
    ]), top=32)
    inner += in_motion_A()
    # understanding now: a compact, source-backed explanation tied to a change this week — not the harbor book
    inner += section('UNDERSTANDING NOW') + gut(unit('THURSDAY&rsquo;S COLD &middot; WHY YOUR ROUTE SPLITS',
                                                     'The river side of your walk will run four degrees colder than the avenue on Thursday night',
                                                     'Open water and an unbroken wind fetch keep the waterfront blocks from holding the day&rsquo;s heat; two streets in, the masonry gives it back for hours. The forecast prints one number; the walk has two.',
                                                     compare2('RIVER SIDE &middot; 9 PM', '24&deg;', 'wind off the water, no stored heat', 'THE AVENUE &middot; 9 PM', '28&deg;', 'masonry, sheltered, holds the day'),
                                                     fn='FORECAST + STREET FORM &middot; A BOUNDED MECHANISM, NOT A PROMISE &middot; NOTHING TO DO'))
    # something to try: usable, complete on the surface
    inner += section('SOMETHING TO TRY') + gut(unit('CARRIED FORWARD &middot; FROM THURSDAY&rsquo;S NOTE',
                                                    'The crust split along the seam where the pan was coldest',
                                                    'Your note said &ldquo;soggy at the edge&rdquo;. The edge is where a cold pan meets dough first. Heat the skillet dry for four minutes, then oil, then dough &mdash; the edge sets before the middle steams.',
                                                    fn='YOUR OBSERVATION + ONE MECHANISM &middot; TRY IT OR DON&rsquo;T &middot; NOTHING IS KEPT UNLESS YOU SAY SO'))
    # a wider world: relevant local life, explicitly not inferred from a personal trace
    inner += section('THE CITY THIS WEEK') + gut('<div style="display: flex; flex-direction: column; gap: 22px;">'
        + city_unit('OPEN HOUSE WEEKEND &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; the walk-in sites need none', 'The pump station under the park is on this year&rsquo;s list &mdash; the one the harbor book describes from outside.')
        + city_unit('THE FLEA &middot; SATURDAYS THIS MONTH', 'Reopened under the bridge, 10 to 5, through October', 'Nine minutes from the market. Neither depends on the other.')
        + '</div>')
    # the reading, as optional depth with a real payoff in the preview — no longer the page's whole substance
    inner += section('WHEN YOU HAVE FOUR MINUTES') + gut(unit('THE HARBOR BOOK &middot; CH. 4', 'The pumps under the park finish what the gates cannot',
        'The two iron squares you step over at the crossing are the pump intakes: on a falling tide the creek drains itself, on a rising one the water inside the gates has nowhere to go without them.', door_text='Read the chapter', fn='YOUR COPY, P. 74&ndash;77 &middot; THE READER CONTINUES FROM HERE, IT DOES NOT RESTART'))
    inner += ending(WEEK_SUN, 'Friday the show. Saturday the market before ten, then Alex. Dana on the 19th.')
    return phone(inner, 0)

H1_NOTES = notecol('What each unit earns', [
    ('THE FIRST VIEWPORT', N('Read + Maya&rsquo;s share + the three ways. A short visit gets: today&rsquo;s weather, one warm timed thing from a person, and three complete alternatives. No crown: nothing operational is at stake on this Sunday, and dominance does not require a card.')),
    ('MAYA&rsquo;S SHARE', ledger([('LANE', 'Attributed human contribution (authored share, friends, through Sunday)'), ('PAYOFF ON VIEW', 'The loaf, the day, the hour, the distance. Her words, her photograph.'), ('DEMAND', 'None. No reply owed; the door goes to the Place.'), ('WHY HERE', 'It is the only thing on the page that is true today only. Removing her removes the value &mdash; not decoration.')])),
    ('TODAY, THREE WAYS', ledger([('LANE', 'Prepared possibilities (coming days)'), ('PAYOFF', 'Three distinct days: out early, out late, in. Each line carries its own reason.'), ('DEMAND', 'None; numbered, not ranked. &ldquo;Stay in&rdquo; is a full option, not a fallback.'), ('EARNS', 'The alternative the old page lacked: if the reading did not interest me, two other good reasons to stay.')])),
    ('IN MOTION', ledger([('CHANGE', 'Alex&rsquo;s Saturday is a shared arrangement in motion with his own words inside the row; Dana&rsquo;s handoff (the bookshop) rides in her row. Two people, no task owed.'), ('DEMAND', 'The place for Saturday is open, but it is Alex&rsquo;s to decide; the row says so.')])),
    ('UNDERSTANDING NOW', ledger([('OPERATION', 'Explain + differentiate: a mechanism the person did not supply, on a change this week (Thursday&rsquo;s cold).'), ('SOURCE', 'Forecast + street form; bounded. Not the harbor book &mdash; range.'), ('PAYOFF', 'Complete on view: two numbers and why.')])),
    ('SOMETHING TO TRY', ledger([('OPERATION', 'Explain, from the person&rsquo;s own note. A usable technique in three lines; not a lesson.'), ('DEMAND', 'None. Nothing kept unless they say so.')])),
    ('THE CITY THIS WEEK', ledger([('LANE', 'World value, explicitly not inferred from a trace (kicker in mute, footnote says so).'), ('WHY', 'A wider world without pretending it was personal. One of them touches the pump station the reading is about &mdash; a link, not a claim.')])),
    ('THE READING', ledger([('CHANGE', 'Demoted from the whole page to optional depth. The preview carries a real payoff (what the two iron squares are), then a door. Not the full chapter inline.')])),
    ('THE ENDING', N('The week seam plus one forward line. No &ldquo;nothing needs you&rdquo;: low obligation is shown by the absence of any ask on the page, and the last line is anticipation, not relief.')),
    ('RETAINED &middot; REMOVED &middot; ADDED', N('<b>Retained:</b> anchor, read, in-motion rows, the seam, the harbor chapter (as depth), Dana&rsquo;s guarantee in her row. <b>Removed:</b> the reading as the page&rsquo;s only substance; the coda&rsquo;s relief language; the dentist as a standalone concern (now one row). <b>Added:</b> Maya&rsquo;s share, three ways, understanding now, something to try, the city, Alex&rsquo;s arrangement.')),
], w=470)

def H1():
    cur = gh.a3_phone()
    cols = [col(cur, caption('CURRENT &middot; FOR COMPARISON', 'The quiet Sunday as delivered', 'ONE READING, THE SEAM, TWO ROWS, RELIEF AS THE CODA')),
            col(h1_generous(), caption('H1 &middot; PROPOSED', 'The generous Sunday', 'SHORT VISIT: READ + A FRIEND&rsquo;S LOAF + THREE WAYS &middot; LONGER VISIT: UNDERSTANDING, A TECHNIQUE, THE CITY, THE READING')),
            H1_NOTES]
    return board_page(1440, 3050, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H1 &middot; ORDINARY SUNDAY, MATURE CONTEXT &middot; PROPOSAL', 'H1 &middot; A short visit worthwhile, a longer visit rewarding',
                      'Persona A&rsquo;s quiet Sunday recomposed. One item may dominate (today it is a friend&rsquo;s timed share, not a crown); three grounded alternatives; then materially different payoffs down the scroll &mdash; a mechanism, a technique, the city, the reading as optional depth. The ending is the week, not reassurance.', cols, FOOT)

# ───────────────────────────── H2 · socially active week ─────────────────────────────
def h2_top(read, sub):
    inner = anchor_row('NEW YORK &middot; MONDAY', '6:40 PM')
    inner += orientation(read, sub)
    return inner

def h2_field(with_maya_inline=True, with_theo=True, with_dana_inline=True):
    """The prospective field shared by both treatments; social material integrated where its effect lands."""
    u = []
    u.append(unit('SATURDAY MORNING &middot; THE MARKET', 'The bread is gone by ten; go at 9:30, not eleven',
                  ('The stalls peak from nine. <b>Theo</b>, who goes most weeks: &ldquo;the bread stall sells out by ten &mdash; go early or don&rsquo;t bother; the cheese people are fine till noon.&rdquo;' if with_theo else 'The stalls peak from nine; bread thins out first.'),
                  gh.rhythm_bars([1, 2, 3, 5, 6, 4, 3, 2, 1, 1], (2, 5), 1, w=349) + '<div style="display: flex; justify-content: space-between;"><span class="fn">8A</span><span class="kick" style="color: #8A6628;">PEAK 9&ndash;11</span><span class="fn">1P</span></div>',
                  fn=('THE MARKET&rsquo;S RHYTHM + THEO&rsquo;S NOTE (MAY-USE, AUDIENCE: YOU) &middot; HIS NOTE MOVED THE WINDOW FROM 11 TO 9:30' if with_theo else 'THE MARKET&rsquo;S RHYTHM FROM PAST SATURDAYS')))
    u.append(unit('SUNDAY WITH DANA &middot; HER MORNING', 'The bookshop she sent opens at eleven; the loaf Maya found is gone by then' if with_maya_inline else 'The bookshop she sent opens at eleven',
                  ('Dana: &ldquo;this one, for Sunday?&rdquo; &mdash; addressed to you Thursday. ' if with_dana_inline else '') + ('Maya&rsquo;s bakery is six minutes from it. Loaf first, then the shop, and the morning is hers as she asked.' if with_maya_inline else 'The morning stays hers, as she asked.'),
                  fn='DANA&rsquo;S HANDOFF (ADDRESSED, USE: YES) ' + ('+ MAYA&rsquo;S SHARE (FRIENDS, THROUGH SUNDAY)' if with_maya_inline else '') + ' &middot; NOTHING IS BOOKED OR PROMISED'))
    return section('THE COMING DAYS') + gut('<div style="display: flex; flex-direction: column; gap: 26px;">' + ''.join(u) + '</div>')

def h2_understanding():
    return section('UNDERSTANDING NOW') + gut(unit('THURSDAY&rsquo;S COLD &middot; WHY YOUR ROUTE SPLITS', 'The river side of your walk will run four degrees colder than the avenue on Thursday night',
        'Open water and an unbroken wind fetch keep the waterfront blocks from holding the day&rsquo;s heat; two streets in, the masonry gives it back for hours.',
        compare2('RIVER SIDE &middot; 9 PM', '24&deg;', 'wind off the water', 'THE AVENUE &middot; 9 PM', '28&deg;', 'masonry holds the day'), fn='FORECAST + STREET FORM &middot; BOUNDED'))

WEEK_MON = [('MON', dm('solid', INK), 'today', INK), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('dashed', MUTE), '28&deg;', MUTE),
            ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'Alex', INK), ('SUN', dm('av:D', ''), 'Dana', INK)]

def h2_distributed():
    inner = h2_top('Cold coming Thursday. Saturday is Alex&rsquo;s.', 'Mild until then &middot; the place for Saturday is still his to pick &middot; the show Friday.')
    inner += gut(unit('ALEX&rsquo;S BIRTHDAY &middot; SATURDAY &middot; FORMING', 'Four going. Alex wants it walkable from the L and not a restaurant; the pier at 6:30 fits both',
        'His words, in the arrangement. A prepared alternative, not a decision: adoption is his. You owe nothing tonight.',
        span('THE PIER &middot; 6:30&ndash;8', 118, 214, 'SUNSET 7:04', start='4 PM', end='10', w=349), door_text='The Saturday arrangement', fn='OCCASION &middot; ALEX OWNS THE ARRANGEMENT (&ldquo;ONLY ME&rdquo; DEFAULT) &middot; YOU CAN SUGGEST, NOT CHANGE', big=True), top=22)
    inner += in_motion_A(today='MON', with_alex=False)
    inner += h2_field()
    inner += h2_understanding()
    inner += section('SOMETHING TO TRY') + gut(unit('CARRIED FORWARD', 'The crust split along the seam where the pan was coldest', 'Heat the skillet dry for four minutes, then oil, then dough.', fn='YOUR NOTE + ONE MECHANISM'))
    inner += gut(door('Everything shared with you') + small('LIFE &middot; PEOPLE &middot; BY PERSON, NEVER RANKED'), top=36)
    inner += ending(WEEK_MON, 'Friday the show. Saturday the market, then the pier. Sunday, Dana&rsquo;s morning.')
    return phone(inner, 0)

def h2_grouped():
    inner = h2_top('Cold coming Thursday. Saturday is Alex&rsquo;s.', 'Mild until then &middot; the place for Saturday is still his to pick &middot; the show Friday.')
    inner += gut(unit('ALEX&rsquo;S BIRTHDAY &middot; SATURDAY &middot; FORMING', 'Four going. Alex wants it walkable from the L and not a restaurant; the pier at 6:30 fits both',
        'His words, in the arrangement. A prepared alternative, not a decision: adoption is his. You owe nothing tonight.',
        span('THE PIER &middot; 6:30&ndash;8', 118, 214, 'SUNSET 7:04', start='4 PM', end='10', w=349), door_text='The Saturday arrangement', fn='OCCASION &middot; ALEX OWNS THE ARRANGEMENT &middot; YOU CAN SUGGEST, NOT CHANGE', big=True), top=22)
    inner += in_motion_A(today='MON', with_alex=False)
    # the field still carries Theo where his note lands (the market); Maya's share and Dana's handoff are NOT paraphrased above — they appear once, in full, in the region
    inner += h2_field(with_maya_inline=False, with_dana_inline=False)
    inner += people_region([
        share('M', 'Maya', 'FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY', 'The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.', plate_h=140, plate_cap='MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', meta='Six minutes from the bookshop Dana sent. Her words, kept hers.', door_text='The bakery, in Places'),
        share('D', 'Dana', 'THURSDAY &middot; ADDRESSED TO YOU', 'This one, for Sunday? I want the poetry shelf in the back.', meta='A used bookshop on Court Street &middot; opens 11 &middot; a link she sent, with a Place behind it. No reply owed; she lands Saturday.', door_text='The bookshop, in Places'),
    ])
    inner += h2_understanding()
    inner += ending(WEEK_MON, 'Friday the show. Saturday the market, then the pier. Sunday, Dana&rsquo;s morning.')
    return phone(inner, 0)

def h2_sparse():
    inner = h2_top('Cold coming Thursday. Dana lands Saturday.', 'Mild until then &middot; the show Friday &middot; Sunday morning is hers.')
    inner += gut(unit('FRIDAY &middot; THE SHOW &middot; FROM YOUR TICKET', 'Leave from work, not home; the way back is the constraint', 'Doors 8, set times not posted; arriving by 8:40 skips nothing. Surface route home after ten adds 25 minutes.',
        span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=349), door_text='Open Friday evening', fn='YOUR TICKET + SERVICE READ &middot; NOTHING BOOKED', big=True), top=22)
    inner += in_motion_A(today='MON', with_alex=False, with_show=False)
    inner += h2_field(with_maya_inline=False, with_theo=False)
    inner += h2_understanding()
    inner += section('SOMETHING TO TRY') + gut(unit('CARRIED FORWARD', 'The crust split along the seam where the pan was coldest', 'Heat the skillet dry for four minutes, then oil, then dough.', fn='YOUR NOTE + ONE MECHANISM'))
    inner += ending([('MON', dm('solid', INK), 'today', INK), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('dashed', MUTE), '28&deg;', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:D', ''), 'Dana', INK), ('SUN', dm('hollow', ''), 'hers', MUTE)],
                    'Friday the show. Saturday, Dana. Sunday is hers.')
    return phone(inner, 0)

def life_people_frame():
    """Where 'what else have my people shared?' goes: Life · People at rest (existing owner, reused as a stub, not redesigned)."""
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">LIFE &middot; PEOPLE</span><span class="fn" style="margin-left: auto;">SHARED WITH YOU</span></div></div>'
             + orientation_direct('Four people have addressed or shared something with you this month.', 'By person, in their words. Nothing here is ranked or scored.'))
    rows = [('M', 'Maya', 'the bakery photograph &middot; friends &middot; through Sunday'), ('D', 'Dana', 'a bookshop, for Sunday &middot; addressed to you'), ('T', 'Theo', 'the market note &middot; may-use &middot; expires with the season'), ('A', 'Alex', '&ldquo;walkable from the L&rdquo; &middot; in Saturday&rsquo;s arrangement')]
    inner += gut(''.join(row(f'<b>{w}</b> &middot; <span style="color: #6E6862;">{t}</span>', avatar=l, last=(i == 3)) for i, (l, w, t) in enumerate(rows)), top=28)
    inner += gut(door('What you have shared, and with whom') + small('YOUR GRANTS, BY AUDIENCE AND EXPIRY &middot; WITHDRAWAL REMOVES EVERY DEPENDENT LINE'), top=30)
    inner += (f'<div style="padding: 44px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING OWNER &middot; REUSED AS THE PULL DESTINATION &middot; NOT REDESIGNED HERE</div></div>')
    return phone(inner, 0, active='Life')

H2_NOTES = notecol('The comparison, and what it decides', [
    ('IDENTICAL EVIDENCE', N('Both treatments use the same five facts: Alex&rsquo;s arrangement + his words; Theo&rsquo;s market note; Maya&rsquo;s bakery share (friends, through Sunday); Dana&rsquo;s addressed bookshop; the show. Neither treatment was weakened to make the other win.')),
    ('TREATMENT 1 &middot; DISTRIBUTED', N('Every person appears inside the unit their contribution changes: Alex in the arrangement, Theo in the market window, Maya and Dana in Sunday&rsquo;s unit. One door at the foot answers &ldquo;what else have my people shared?&rdquo;. <b>Cost:</b> Maya&rsquo;s photograph and Dana&rsquo;s actual words are compressed to clauses; the people are legible as effects, not as people.')),
    ('TREATMENT 2 &middot; PLUS A CONDITIONAL GROUPING', N('Same top. The Sunday unit no longer paraphrases Maya or Dana; their authored material appears once, in full, in <b>From your people</b> &mdash; photograph, words, audience, expiry &mdash; with the pull door. Theo stays in the market unit because his note is used there in full; he is <b>not</b> repeated in the region (the no-duplication rule). The region renders only when two or more authored units are not already spent above; it disappears when empty (see the sparse variant).')),
    ('SPARSE VARIANT', N('Only Dana this week. No region, no empty module, no invite. Her handoff rides in her row and in Sunday&rsquo;s unit; the show leads because nothing social is timelier.')),
    ('RECOMMENDATION', N('<b>Treatment 2, with the condition.</b> Authored material is warmer and more legible when it keeps its author&rsquo;s form (a photograph and a sentence) than when it is reduced to a clause inside a possibility. The condition (&ge;2 unspent authored units; never a duplicate; disappears when empty) keeps it from becoming a social module. Shared <i>consequences</i> (Alex&rsquo;s arrangement) still appear where they land, above the region.')),
    ('TENSION WITH CANON &middot; REPORTED, NOT RESOLVED', N('MP2&rsquo;s &ldquo;one relational opening&rdquo; law governed dominance: at most one social unit may take the crown. Read as a page-wide cap it would forbid Treatment 2. This pass reads it as a <b>dominance</b> rule (one social cause may lead) and a <b>demand</b> rule (at most one social unit may ask anything), not a count of authored material on a long page. Founder ruling requested (decision D-H2 on the ledger board).')),
    ('BROWSING BEYOND SELECTION', N('The door &ldquo;Everything shared with you&rdquo; goes to the existing Life &middot; People owner (frame at right), by person, never ranked. No fifth tab. If a present-tense aperture is later wanted, its minimum boundary is: consumption-first, finite, entered from this door, returns to the same Home position.')),
], w=440)

def H2():
    cols = [col(h2_distributed(), caption('TREATMENT 1', 'Distributed', 'SOCIAL MATERIAL INSIDE THE UNITS IT CHANGES &middot; ONE PULL DOOR AT THE FOOT')),
            col(h2_grouped(), caption('TREATMENT 2 &middot; RECOMMENDED', 'Distributed + a conditional grouping', '&ldquo;FROM YOUR PEOPLE&rdquo; ONLY WHEN &ge;2 AUTHORED UNITS ARE UNSPENT ABOVE &middot; NEVER A DUPLICATE')),
            col(h2_sparse(), caption('SPARSE-SOCIAL VARIANT', 'Only Dana this week', 'NO REGION, NO EMPTY MODULE, NO INVITE DEMAND')),
            col(life_people_frame(), caption('WHERE THE DOOR GOES', 'Life &middot; People, shared with you', 'EXISTING OWNER &middot; THE PULL-BASED ALTERNATIVE TO HOME&rsquo;S RANKING')),
            H2_NOTES]
    return board_page(2560, 2720, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H2 &middot; SOCIALLY ACTIVE ORDINARY WEEK &middot; PROPOSAL', 'H2 &middot; The present social world, made visible two ways',
                      'Monday evening. Four people, several situations: Alex&rsquo;s birthday arrangement forming, Theo&rsquo;s market judgment, Maya&rsquo;s authored share, Dana&rsquo;s addressed bookshop. Nobody has a task for you. Two treatments on identical evidence, a sparse variant, and the destination for &ldquo;what else have my people shared?&rdquo;.', cols, FOOT)

# ───────────────────────────── H3 · first open → contribution → next open ─────────────────────────────
def h3_first():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '8:05 AM')
    inner += orientation('Clear and cool. The first hard cold arrives Thursday night.', 'You chose New York. Nothing about you is held yet, and nothing needs to be.')
    inner += section('THIS WEEK IN THE CITY', top=28) + gut('<div style="display: flex; flex-direction: column; gap: 26px;">'
        + city_unit('THURSDAY NIGHT &middot; 28&deg;', 'The first frost of the season lands on the waterfront blocks first', 'Open water and wind fetch keep them from holding the day&rsquo;s heat; two streets in, masonry gives it back for hours. If you walk near the river Thursday, that is the four-degree difference.', fn='FORECAST + STREET FORM &middot; FROM THE CITY, NOT FROM YOU')
        + city_unit('THE L &middot; THIS WEEK AFTER 11 PM', 'Single-tracking Monday to Thursday nights: plan on a 20-minute wait between Bedford and 1st', 'Daytime service is normal. The G is unaffected.', fn='SERVICE NOTICE &middot; FROM THE CITY')
        + city_unit('OPEN HOUSE WEEKEND &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; the walk-in sites need none', 'Two hundred buildings, most of them free.', fn='FROM THE CITY')
        + '</div>')
    inner += section('WHAT A TICKET TURNS INTO') + gut(sample_unit('A Friday ticket becomes an evening you can see: doors, the set, the way there, the way home',
        'For a made-up 8 pm show at a real-sized hall: leave from work not home; arriving by 8:40 skips nothing; coat check yes; the last surface route home after ten adds 25 minutes.',
        'See the sample', 'Try this with yours'))
    inner += section('WHAT ELSE TURNS INTO SOMETHING') + gut(three_ways('THREE MORE, EACH A SAMPLE UNTIL IT&rsquo;S YOURS', [
        ('A photograph of a dish &rarr; the mechanism behind the texture', 'What the last minute at the stove did, and how to test it at home. Not a caption.'),
        ('A friend&rsquo;s note &rarr; a better window for the same place', 'Their words stay theirs; the timing changes for you.'),
        ('Scattered tickets and photographs &rarr; one recoverable record', 'The trip as it actually moved, in Life, with the missed leg included.'),
    ]))
    inner += (f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Bring one thing when something has your attention. Until then, the city is enough.</div></div>')
    return phone(inner, 0)

def h3_sample():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SAMPLE &middot; A TICKET, READ</span><span class="kick" style="margin-left: auto; color: {MUTE};">NOT YOURS</span></div></div>')
    inner += orientation_direct('A made-up ticket, read the way yours would be.', 'Nothing here is about you. Every fact is invented for the sample.')
    inner += gut(f'<div style="border: 1px dashed rgba(27,23,20,0.28); border-radius: 18px; padding: 16px; display: flex; flex-direction: column; gap: 6px;">'
                 f'<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {PLAN};"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {PLAN};">SAMPLE &middot; FRIDAY &middot; DOORS 8:00</span></div>'
                 f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 26px; letter-spacing: -0.2px; margin-top: 4px;">Leave for the show from work, not home</div>'
                 f'<div style="{SERIF} font-size: 16px; line-height: 22px; font-weight: 500; color: {INK2};">The way back is the constraint, not the way there.</div>'
                 + span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317)
                 + f'<div class="fn">FROM THE SAMPLE TICKET + A SAMPLE FORECAST &middot; IN THE REAL THING: YOUR TICKET + TONIGHT&rsquo;S SERVICE READ</div></div>', top=22)
    inner += gut(callouts([('1', 'The ticket gives the hall, the date, doors. Set times are read from the hall when posted; until then &ldquo;arriving by 8:40 skips nothing&rdquo; is what the hall&rsquo;s past nights say.'),
                           ('2', 'The way there is timed from wherever you say you are leaving. Nothing about your location is assumed.'),
                           ('3', 'The way home is the part people forget: the surface route after ten, and what it costs.'),
                           ('4', 'Nothing is booked, saved, or shared by reading it. If you bring yours, it is kept in Life and you can undo that in one tap.')]), top=22)
    inner += gut(door('Try this with yours', INK) + small('OPENS CHAT WITH THE TICKET AS THE FIRST THING YOU GIVE &middot; A PHOTO OR A FORWARDED EMAIL'), top=30)
    return phone(inner, 0, active='Home')

def chat_frame():
    """The existing Chat/intake boundary, shown only enough to understand the action and the return."""
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">TUESDAY 8:12 AM</span></div></div>')
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; display: flex; flex-direction: column; gap: 8px;">'
                 f'<div style="height: 110px; border-radius: 10px; background: rgba(251,247,236,0.14); display: flex; align-items: flex-end; padding: 8px;"><span class="fn" style="color: rgba(251,247,236,0.7);">YOUR PHOTO &middot; A TICKET &middot; SLOT</span></div>'
                 f'<div style="font-size: 15px; line-height: 20px;">what&rsquo;s this evening look like</div></div></div>', top=26)
    inner += gut(f'<div style="max-width: 330px; display: flex; flex-direction: column; gap: 10px;">'
                 f'<div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Friday at the hall, doors 8. Leave from work, not home &mdash; the way back is the constraint. Arriving by 8:40 skips nothing; coat check yes. After ten the surface route adds 25 minutes.</div>'
                 f'<div style="border-top: 1px solid rgba(27,23,20,0.10); padding-top: 10px; display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: center; gap: 8px;"><span class="kickm">KEPT</span><span style="font-size: 13px; color: {INK};">Your ticket &middot; Friday &middot; in Life</span><span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">Undo</span></div>'
                 f'<div class="fn">READ FROM THE TICKET + TONIGHT&rsquo;S SERVICE &middot; NOTHING SHARED &middot; NOTHING BOOKED &middot; HOME WILL SHOW FRIDAY UNTIL IT PASSES</div></div></div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">Ask, or bring something else</span></div>', top=40)
    inner += (f'<div style="padding: 30px 34px 6px 34px; text-align: center;"><div class="fn">EXISTING BOUNDARY &middot; BRING &rarr; T1 (APPLY PRIVATELY, THEN RECEIPT WITH UNDO) &middot; NOT REDESIGNED HERE</div></div>')
    return phone(inner, 0, active='Chat')

def h3_return():
    inner = anchor_row('NEW YORK &middot; WEDNESDAY', '7:30 AM')
    inner += orientation('First hard cold of the season arrives tonight.', '18&deg; by morning &middot; wind off the river &middot; Friday&rsquo;s show is set.')
    inner += crown(PLAN, 'FRIDAY &middot; YOUR TICKET', 'Leave for the show from work, not home', 'The way back is the constraint, not the way there.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn='YOUR TICKET + TONIGHT&rsquo;S FORECAST &middot; RE-CHECKS WHEN THE HALL POSTS SET TIMES &middot; NOTHING BOOKED')
    inner += section('SINCE YOU BROUGHT THE TICKET', top=36) + gut(body('It is in Life under this week, with the hall and the night. Nothing else was kept.', INK) + door('The ticket, in Life') + small('ONE THING HELD &middot; UNDO STILL AVAILABLE FROM THERE'))
    inner += section('THIS WEEK IN THE CITY') + gut('<div style="display: flex; flex-direction: column; gap: 26px;">'
        + city_unit('TONIGHT &middot; 18&deg;', 'The waterfront blocks freeze first', 'If you walk near the river tonight, that is the four-degree difference from the avenue.', fn='FORECAST + STREET FORM &middot; FROM THE CITY')
        + city_unit('THE L &middot; TONIGHT AFTER 11', 'Single-tracking; 20-minute waits between Bedford and 1st', 'Friday night is unaffected &mdash; that is why the show&rsquo;s surface route is the only cost.', fn='SERVICE NOTICE &middot; FROM THE CITY &middot; NOW TIED TO YOUR FRIDAY')
        + '</div>')
    inner += section('WHAT ELSE TURNS INTO SOMETHING') + gut(three_ways('TWO MORE, SAMPLES UNTIL THEY&rsquo;RE YOURS', [
        ('A photograph of a dish &rarr; the mechanism behind the texture', 'What the last minute at the stove did.'),
        ('A friend&rsquo;s note &rarr; a better window for the same place', 'Their words stay theirs; the timing changes for you.'),
    ]))
    inner += ending([('WED', dm('solid', INK), 'today', INK), ('THU', dm('dashed', MUTE), '18&deg;', MUTE), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE)],
                    'Friday the show. The rest of the week is the city&rsquo;s.')
    return phone(inner, 0)

def h3_next():
    inner = anchor_row('NEW YORK &middot; SATURDAY', '9:30 AM')
    inner += orientation('A clear Saturday. Low water at 1:40.', 'Warming to 60&deg; &middot; the first weekend after the cold.')
    inner += section('TODAY IN THE CITY', top=28) + gut('<div style="display: flex; flex-direction: column; gap: 26px;">'
        + city_unit('THE GREENMARKET &middot; UNTIL 1', 'The bread stalls thin out by ten; produce holds until noon', 'Nine minutes from the address you gave. Its rhythm from past Saturdays; nobody&rsquo;s note yet.', fn='FROM THE CITY')
        + city_unit('LOW WATER &middot; 1:40&ndash;4', 'At low water the old creek mouth shows where the harbor used to come in', 'Walk the kerb line along the waterfront blocks; the granite ends where the 1911 gates&rsquo; protection ends.', fn='TIDE TABLE + THE HARBOR BOOK, CH. 3 &middot; FROM THE CITY')
        + '</div>')
    inner += section('SINCE YOU LOOKED') + gut(body('Friday&rsquo;s ticket is in Life with the hall and the night. Whether you went is yours to say; nothing was assumed.', INK) + door('The ticket, in Life'))
    inner += section('WHAT A PHOTOGRAPH TURNS INTO') + gut(sample_unit('A photograph of a dish becomes the mechanism behind its texture',
        'For a made-up plate of pasta: the sauce clings as a film, not a pool &mdash; a starch-supported emulsion finished in the pan. How to test it at home tonight.', 'See the sample', 'Try this with yours'))
    inner += ending([('SAT', dm('solid', INK), 'today', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE)],
                    'The market until one. Low water at 1:40. That is Saturday, if you want it.')
    return phone(inner, 0)

H3_NOTES = notecol('Three sources, kept apart', [
    ('1 &middot; NONPERSONAL WORLD VALUE', N('Three city units on the first open, each with a real payoff (the four-degree split, the L after 11, the registration hour). Kicker in mute, footnote &ldquo;from the city, not from you&rdquo;. Based only on the city the person chose. No location permission assumed.')),
    ('2 &middot; CLEARLY LABELLED DEMONSTRATION', N('A dashed unit stamped SAMPLE &middot; NOT YOURS: a made-up ticket read the way theirs would be. Inspectable (phone 2) without uploading anything. The sample sheet says what each part comes from and what is <i>not</i> assumed. Two doors: see the sample / try this with yours.')),
    ('3 &middot; PERSONAL RETURN', N('After one Bring through the existing Chat boundary (phone 3, T1: apply privately, receipt with Undo), Home changes materially (phone 4): the crown is theirs, the L notice becomes tied to their Friday, and one door goes to the ticket in Life. The remaining samples shrink to two and will retire once tried or ignored twice.')),
    ('THE NEXT OPEN', N('Phone 5: no further contribution. No guilt, no &ldquo;you missed&rdquo;, no attendance inferred (&ldquo;whether you went is yours to say&rdquo;). The city carries the page; one new sample appears because a different capability is now the most useful thing to show. Samples retire; they are not a permanent module.')),
    ('WHAT IS ACTUAL VS PROPOSED', ledger([('EXISTS', 'Chat intake with T1 receipt + Undo; Life holds the ticket; the commitment crown; service reads.'), ('NEEDS VERIFICATION', 'A city-scoped world feed with freshness; hall set-time reads; the L notice as a source.'), ('PROPOSED', 'The SAMPLE unit and sheet; sample retirement rules; &ldquo;tied to your Friday&rdquo; linking of a world notice to a held commitment.')])),
    ('NOT DONE', N('No onboarding checklist, meter, invite, account-connection campaign, or carousel. Chat and Life are shown as their existing boundaries only.')),
], w=430)

def H3():
    cols = [col(h3_first(), caption('1 &middot; FIRST OPEN &middot; TUESDAY 8:05', 'Useful without history', 'THE CITY + ONE LABELLED SAMPLE + WHAT ELSE TURNS INTO SOMETHING')),
            col(h3_sample(), caption('2 &middot; THE SAMPLE, INSPECTED', 'A made-up ticket, read', 'STAMPED SAMPLE &middot; SAYS WHAT IS AND IS NOT ASSUMED')),
            col(chat_frame(), caption('3 &middot; ONE CONTRIBUTION &middot; CHAT', 'Bring the ticket', 'EXISTING BOUNDARY &middot; T1 RECEIPT WITH UNDO')),
            col(h3_return(), caption('4 &middot; HOME, WEDNESDAY 7:30', 'The personal return', 'THE CROWN IS THEIRS &middot; A CITY NOTICE NOW TIED TO THEIR FRIDAY &middot; THE TICKET IN LIFE')),
            col(h3_next(), caption('5 &middot; NEXT OPEN &middot; SATURDAY 9:30', 'No further contribution', 'NO GUILT &middot; NO ATTENDANCE INFERRED &middot; A DIFFERENT SAMPLE')),
            H3_NOTES]
    return board_page(2820, 1830, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H3 &middot; FIRST OPEN &rarr; FIRST CONTRIBUTION &rarr; NEXT OPEN &middot; PROPOSAL', 'H3 &middot; Value before contribution, and a real return after one',
                      'Persona C, a first week. Not knowing the person does not mean knowing nothing useful about the world. Three sources kept explicitly apart: the city, a labelled sample, and the person&rsquo;s own return. The invitation follows visible value: &ldquo;Try this with yours&rdquo;.', cols, FOOT)

# ───────────────────────────── H4 · priority stress test ─────────────────────────────
def h4_before():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '5:40 PM')
    inner += orientation('Cold coming tonight. The show is tomorrow.', '28&deg; by morning &middot; Saturday is Alex&rsquo;s &middot; the pier at 6:30 is on the table.')
    inner += crown(PLAN, 'FRIDAY &middot; DOORS 8:00', 'Leave for the show from work, not home', 'The way back is the constraint, not the way there.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn='RE-CHECKED THU 5 PM &middot; NOTHING BOOKED')
    inner += in_motion_A(today='THU', with_show=False, dentist='Dentist &middot; Tuesday, done')
    inner += h2_understanding().replace('THURSDAY&rsquo;S COLD', 'TONIGHT&rsquo;S COLD').replace('on Thursday night', 'tonight')
    inner += section('SOMETHING TO TRY') + gut(unit('CARRIED FORWARD', 'The crust split along the seam where the pan was coldest', 'Heat the skillet dry for four minutes, then oil, then dough.', fn='YOUR NOTE + ONE MECHANISM'))
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'Alex', INK), ('SUN', dm('av:D', ''), 'Dana', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)],
                    'Tomorrow the show. Saturday the market, then Alex. Sunday, Dana&rsquo;s morning.')
    return phone(inner, 0)

def h4_during():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '6:05 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">Saturday&rsquo;s place fell through. Alex needs one answer by seven.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">The pier&rsquo;s food hall closed Saturday for a private event &middot; 4 going &middot; the show tomorrow is unchanged.</div></div>')
    inner += crown(OX, 'DECIDE BY 7:00 &middot; ALEX&rsquo;S SATURDAY &middot; 55 MIN', 'Two places still fit &ldquo;walkable from the L, not a restaurant&rdquo;', 'Alex asked the four of you; he decides. Yours is a preference, not a booking.',
                   span('THE PARK, 6:30 &middot; SUNSET 7:04', 118, 214, 'OPEN LATE', 'THE GARDEN, 7 &middot; TILL 9', 140, 222, 'NEEDS A NAME', start='4 PM', end='10', w=317)
                   + f'<div style="font-size: 14px; line-height: 19px; margin-top: 8px; color: {INK};">The park keeps the sunset and needs nothing; the garden is warmer after eight but wants a name for six by 6:30. Maya has said the park.</div>',
                   cta='Tell Alex which', fn='OCCASION &middot; ALEX OWNS THE ARRANGEMENT &middot; YOUR ANSWER GOES TO HIM, NOT TO A BOOKING &middot; EXPIRES AT 7:00 EITHER WAY')
    inner += section('IN MOTION') + gut(row('The show &middot; tomorrow, doors 8 &middot; <span style="color: #6E6862;">unchanged &middot; leave from work</span>', mark='solid', color=GOLD)
                                     + arow('Dana &middot; Saturday the 19th &middot; <span style="color: #6E6862;">unchanged</span>', avatars=['D'], last=True))
    inner += gut(collapsed('THE REST OF THURSDAY &middot; STILL HERE', ['Tonight&rsquo;s cold &middot; why your route splits', 'Something to try &middot; the skillet, preheated dry', 'The city this week &middot; Open House registration']), top=36)
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'Alex &middot; 7?', OX), ('SUN', dm('av:D', ''), 'Dana', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)],
                    'One answer by seven. Everything else is where you left it.')
    return phone(inner, 0)

def h4_after():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '7:25 PM')
    inner += orientation('Saturday is the park at 6:30. Cold tonight.', '28&deg; by morning &middot; the show tomorrow &middot; Alex settled it at 6:52.')
    inner += crown(PLAN, 'FRIDAY &middot; DOORS 8:00', 'Leave for the show from work, not home', 'The way back is the constraint, not the way there.',
                   span('THE SHOW &middot; 8&ndash;10', 140, 250, '+25 HOME', start='5 PM', end='12', w=317), cta='Open Friday evening', fn='RE-CHECKED THU 7 PM &middot; NOTHING BOOKED')
    inner += section('IN MOTION') + gut(arow('Alex&rsquo;s birthday &middot; Saturday, the park at 6:30 &middot; <span style="color: #6E6862;">settled &middot; 4 going &middot; sunset 7:04</span>', avatars=['A', 'M', 'you'])
                                     + arow('Dana &middot; Saturday the 19th &middot; <span style="color: #6E6862;">&ldquo;keep Sunday morning for me&rdquo;</span>', avatars=['D'], last=True))
    inner += h2_understanding().replace('THURSDAY&rsquo;S COLD', 'TONIGHT&rsquo;S COLD').replace('on Thursday night', 'tonight')
    inner += section('SOMETHING TO TRY') + gut(unit('CARRIED FORWARD', 'The crust split along the seam where the pan was coldest', 'Heat the skillet dry for four minutes, then oil, then dough.', fn='YOUR NOTE + ONE MECHANISM'))
    inner += section('THE CITY THIS WEEK') + gut(city_unit('OPEN HOUSE WEEKEND &middot; OCT 17&ndash;18', 'Registration for the timed sites opened Tuesday; the walk-in sites need none', 'The pump station under the park is on this year&rsquo;s list.'))
    inner += ending([('THU', dm('solid', INK), 'today', INK), ('FRI', dm('solid', GOLD), 'the show', MUTE), ('SAT', dm('av:A', ''), 'the park', INK), ('SUN', dm('av:D', ''), 'Dana', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE)],
                    'Tomorrow the show. Saturday the park at 6:30. Sunday, Dana&rsquo;s morning.')
    return phone(inner, 0)

H4_NOTES = notecol('How attention reorganizes, and returns', [
    ('THE CHANGE', N('An ordinary local change, not an airline: the arrangement&rsquo;s place closed for Saturday; Alex (the owner) asked the four for a preference by seven. It is time-sensitive and affects other people, so it takes the dominance budget and the demand budget at once.')),
    ('DURING', ledger([('READ', 'Oxblood, direct: what fell through, what is asked, by when. The show is named as unchanged in the same breath.'), ('CROWN', 'One instrument (two spans on one line), one CTA that goes to Alex, not to a booking. Maya&rsquo;s stated preference is shown as hers. Expiry is explicit: the crown leaves at 7:00 whether or not you answer.'), ('THE REST', 'Compressed, not removed: the field folds to three reachable titles. The seam marks Saturday with the open question. Position and content are preserved for the return.'), ('DEMAND', 'Exactly one ask on the page.')])),
    ('AFTER', N('Alex settled it. The crown returns to Friday (the next commitment), the arrangement becomes a settled row with the outcome inside it, and every folded unit reappears in its place. The page is the &ldquo;before&rdquo; page plus one changed row: no reshuffle for its own sake.')),
    ('WHAT PERSISTS', ledger([('ANSWERING', 'A preference on the Occasion, attributed to you; not a commitment, not a booking.'), ('NOT ANSWERING', 'Nothing. The crown expires; Alex decides; the settled row appears either way.'), ('NEVER', 'A pending badge after 7:00; a &ldquo;you didn&rsquo;t answer&rdquo;.')])),
    ('ACTUAL VS PROPOSED', N('Occasion decision-by-deadline with owner-controlled collaboration exists as accepted direction (Sept 4); the two-span comparison is the Urgent v2 instrument reused; the fold-and-return behaviour is proposed.')),
], w=440)

def H4():
    cols = [col(h4_before(), caption('BEFORE &middot; THURSDAY 5:40', 'The fuller Thursday', 'COMMITMENT CROWN + ARRANGEMENT IN MOTION + THE FIELD')),
            col(h4_during(), caption('DURING &middot; 6:05', 'One decision, 55 minutes', 'THE ARRANGEMENT TAKES DOMINANCE AND DEMAND &middot; THE REST FOLDS, STAYS REACHABLE')),
            col(h4_after(), caption('AFTER &middot; 7:25', 'The fuller Home returns', 'THE SAME PAGE PLUS ONE CHANGED ROW &middot; NO RESHUFFLE')),
            H4_NOTES]
    return board_page(1900, 1870, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H4 &middot; PRIORITY STRESS TEST &middot; PROPOSAL', 'H4 &middot; A genuine priority stays unmistakable inside the richer page',
                      'Same mature account, Thursday evening. Saturday&rsquo;s arrangement loses its place and Alex asks for one preference by seven. Before, during, and after: what takes over, what stays reachable, and how the fuller Home comes back.', cols, FOOT)

# ───────────────────────────── H5 · return home, corrected ─────────────────────────────
def h5_generous():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '11:20 AM')
    inner += orientation('Home. Clear, 64&deg;, low water at 2:40.', 'Landed 6:40 &middot; Saturday is dinner with Maya and Alex &middot; nothing is asked of you today.')
    inner += gut(three_ways('THIS AFTERNOON, THREE WAYS', [
        ('The pier at low water, 2:40&ndash;5, then the greenmarket tomorrow until 1', 'The first walk back can be the one you know. The market&rsquo;s bread is gone by ten.'),
        ('The Sorrento dish, for Saturday&rsquo;s three', 'The texture you photographed is mostly timing: sauce meets pasta ninety seconds early, finished in the pan. A dish for three on Saturday is the honest test.'),
        ('Stay in. The Chinatown noodle shop delivers until ten', 'Nothing about the day requires you to be anywhere.'),
    ]), top=22)
    inner += section('IN MOTION') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled &middot; Maya added a photograph to it Friday</span>', avatars=['M', 'A', 'you'])
                                     + row('Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing &middot; nothing needed from you</span>', mark='dashed', last=True))
    inner += section('UNDERSTANDING NOW') + gut(unit('WHAT THE PHOTOGRAPH SHOWS &middot; SORRENTO, LAST TUESDAY', 'The last minute at the stove explains the texture better than the ingredient list',
        'The sauce clings as a thin film rather than pooling, and the finish looks integrated at service. Those cues are consistent with a starch-supported emulsion and pan finishing. They do not prove how that kitchen prepared it.',
        photo(150, 'YOUR PHOTOGRAPH &middot; SORRENTO &middot; SLOT', [('1', 18, 18), ('2', 300, 84)]) + callouts([('1', 'Film, not pool.'), ('2', 'Integrated at service, not added after.')]),
        door_text='Test it Saturday, for three', fn='YOUR OBSERVATION + ONE MECHANISM &middot; ONE SOURCE PER CLAIM &middot; THE DOOR IS A POSSIBILITY, NOT A PLAN'))
    inner += section('FROM THE TRIP, MADE USEFUL') + gut(unit('THE ONE COMPLETE LEG', 'Sorrento &rarr; Amalfi is the only leg documented from departure to arrival',
        'Ferry ticket 9:10, the harbor photograph 9:14, the Amalfi quay 10:02. Every other leg has one end missing &mdash; including the Rome return, which the receipts reconstruct differently from what was intended.',
        f'<div style="display: flex; gap: 10px; align-items: center; margin-top: 8px;"><span class="kick" style="color: {INK};">9:10</span><span style="flex: 1; height: 2px; background: {GOLD};"></span><span class="kick" style="color: {INK};">9:14</span><span style="flex: 1; height: 2px; background: {GOLD};"></span><span class="kick" style="color: {INK};">10:02</span></div>',
        door_text='The trip, in Life', fn='FROM 412 OF 690 PHOTOGRAPHS IMPORTED SO FAR + TICKETS &middot; A RECORD LABELLED AS A RECORD &middot; THE REST FILLS IN AS IMPORT FINISHES'))
    inner += section('THE CITY THIS WEEK') + gut(city_unit('OPEN HOUSE WEEKEND &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon', 'Two hundred buildings, most of them free.'))
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), 'market', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK)],
                    'The water at 2:40, if you want it. Saturday, the dish for three.')
    return phone(inner, 0)

H5_NOTES = notecol('The same system, on the return', [
    ('WHAT CHANGED', N('The current day-zero led with an import card (&ldquo;the trip is settling into Life&rdquo;) and ended by telling the person to unpack. Here the first viewport is New York: weather, low water, three ways to spend the first afternoon back &mdash; one of which carries Europe forward as a dish for Saturday&rsquo;s three, and one of which is staying in.')),
    ('STATUS, COMPACT', N('Import progress is one footnote inside the reconstruction unit (412 of 690). It is never a card, never the lead, never a completion report.')),
    ('THE PAST, MADE USEFUL', ledger([('OPERATION', 'Reconstruction + recurrence: the only complete leg, from tickets and timestamps. A record labelled as a record, with a door to Life.'), ('LIMIT', 'It appears once, low on the page, and only because it is unusually clean. Rome does not become the page.'), ('NOT CLAIMED', 'What the trip meant; that the person should rest, reflect, or resume exploring.')])),
    ('THE DISH', N('Consequential translation: the Sorrento photograph becomes a possibility for Saturday&rsquo;s dinner with Maya and Alex. The door is a possibility, not a plan; nothing is added to the arrangement by reading it.')),
    ('REUSE', N('H1&rsquo;s system unchanged: read &rarr; three ways &rarr; in motion &rarr; understanding &rarr; material made useful &rarr; the city &rarr; the seam. No new template.')),
], w=440)

def H5():
    cur = lift_phone('../hp/homeproj/Board 3 - Persona B - Back from Europe.dc.html'.replace('../hp/homeproj/', OUT + '/'), 0) if False else None
    from gen_homeproj import p2_day0
    cols = [col(p2_day0(), caption('CURRENT &middot; FOR COMPARISON', 'Day zero as delivered', 'AN IMPORT CARD LEADS; &ldquo;UNPACK&rdquo; CLOSES')),
            col(h5_generous(), caption('H5 &middot; PROPOSED', 'Day zero, New York first', 'THREE WAYS &middot; THE DISH FOR SATURDAY &middot; THE ONE COMPLETE LEG &middot; STATUS AS A FOOTNOTE')),
            H5_NOTES]
    return board_page(1440, 2280, 'VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H5 &middot; RETURN-HOME CORRECTIVE &middot; PROPOSAL', 'H5 &middot; Coming home is projecting life forward, not a recap',
                      'Persona B, the Sunday of landing. The same generous system as H1 applied to the return: current-world value first while imports finish, status compact, one worthwhile reconstruction low on the page, Europe carried forward only where it changes something in New York.', cols, FOOT)

# ───────────────────────────── H0 · ledger, comparison, decisions, handback ─────────────────────────────
def H0():
    def blk(t, html): return f'<div style="display: flex; flex-direction: column; gap: 10px;"><div class="shead"><span>{t}</span><span class="rule"></span></div>{html}</div>'
    def tbl(cols, rows):
        h = ''.join(f'<th style="text-align: left; font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE}; padding: 6px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.14); vertical-align: bottom;">{c}</th>' for c in cols)
        b = ''.join('<tr>' + ''.join(f'<td style="font-size: 12.5px; line-height: 17px; color: {INK2}; padding: 8px 10px 8px 0; border-bottom: 1px solid rgba(27,23,20,0.06); vertical-align: top;">{c}</td>' for c in r) + '</tr>' for r in rows)
        return f'<table style="border-collapse: collapse; width: 100%;"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
    system = blk('THE RECOMMENDED SYSTEM &middot; ONE SKELETON, FOUR BUDGETS', N(
        '<b>Read</b> (world + what dominates, one or two lines) &rarr; <b>Priority</b> (zero or one: a crown only when something operational is at stake; otherwise the strongest unit leads bare) &rarr; '
        '<b>The coming days</b> (two to four grounded alternatives, one of them &ldquo;stay in&rdquo;, each with its reason; social material integrated where it lands) &rarr; <b>In motion</b> (44px rows; people as facepiles inside their own rows) &rarr; '
        '<b>From your people</b> (conditional: &ge;2 authored units not already spent above; never a duplicate; disappears when empty; ends with the pull door) &rarr; <b>Understanding now</b> (one mechanism, complete on view) &rarr; <b>Something to try</b> (one usable technique) &rarr; '
        '<b>Material made useful</b> (a reconstruction or annotated photograph, when unusually strong) &rarr; <b>The city this week</b> (one or two units, marked not-inferred) &rarr; <b>When you have four minutes</b> (optional depth with a real payoff in the preview) &rarr; '
        '<b>The seam + one forward line</b> (no relief language).<br><br>'
        '<b>Budgets:</b> dominance 0–1 &middot; demand &le;1 ask per page (H4 spends it; every other page spends none) &middot; possibility 2–4 &middot; depth behind doors. <b>Length follows value:</b> H4-during is shorter than H4-before by folding, not deleting; H3-first is shorter than H1 because the city is all there is.'))
    ledger_t = blk('PER-UNIT LEDGER &middot; THE UNITS THIS PASS ADDS OR CHANGES', tbl(['UNIT', 'EVIDENCE AVAILABLE', 'VISIBLE PAYOFF', 'REASON TO BE HERE', 'DEMAND', 'DESTINATION', 'ACTUAL / PROPOSED'], [
        ['Authored share as lead (H1)', 'Maya&rsquo;s share: photo + words, friends, expiry', 'Loaf, day, hour, distance', 'Only true today; removing her removes it', 'None', 'The Place', 'Share projection EXISTS (MP1); as Home lead PROPOSED'],
        ['Today, three ways', 'World rhythms + held notes + one &ldquo;stay in&rdquo;', 'Three complete days', 'The alternative when the lead does not interest me', 'None; unranked', 'Places / none', 'PROPOSED (composition); rhythms need an owner with freshness'],
        ['Arrangement in motion (Alex)', 'Occasion + owner&rsquo;s words + attendance', 'What is forming, who owns it, what fits', 'Shared motion, viewer-relevant', 'None (H2) / one (H4)', 'Occasion', 'Owner-controlled collaboration ACCEPTED 09-04; runtime UNVERIFIED'],
        ['From your people (conditional)', '&ge;2 authored units unspent above', 'The author&rsquo;s form: photograph + sentence', 'Authored material is warmer whole than as a clause', 'None', 'Place / Life &middot; People', 'PROPOSED; grant-scoped reads EXIST'],
        ['Understanding now (the cold split)', 'Forecast + street form', 'Two numbers and the mechanism', 'Range beyond one book; ties to this week', 'None', 'None', 'PROPOSED; needs a bounded-mechanism source'],
        ['Something to try (the skillet)', 'The person&rsquo;s own note', 'A technique in three lines', 'Carried forward, usable tonight', 'None', 'None (Keep only if said)', 'Carry-forward EXISTS (Life); composition PROPOSED'],
        ['The city this week', 'City notices, not personal traces', 'A real date, hour, or service fact', 'A wider world, honestly sourced', 'None', 'None / Places', 'PROPOSED; needs a city-scoped feed with freshness'],
        ['The reading as depth', 'The held book', 'The payoff sentence, then a door', 'Depth without being the page', 'None', 'The reader (Chat lane)', 'Reader EXISTS (proposed 09-04)'],
        ['SAMPLE unit + sheet (H3)', 'None &mdash; invented, labelled', 'What a ticket turns into', 'Demonstrate before requesting', 'None', 'Sample sheet / Chat', 'PROPOSED'],
        ['World notice tied to a held commitment (H3-4)', 'Service notice + the ticket', '&ldquo;Friday is unaffected&rdquo;', 'The first personal return beyond the crown', 'None', 'None', 'PROPOSED'],
        ['Fold-and-return (H4)', 'Priority + the prior page', 'The rest stays reachable, then returns unchanged', 'Priority without amnesia', '&mdash;', '&mdash;', 'PROPOSED'],
        ['The one complete leg (H5)', 'Tickets + timestamps', 'The leg, with its times', 'Unusually clean reconstruction', 'None', 'Life', 'Reconstruction EXISTS (09-02); as a Home unit PROPOSED'],
        ['The seam + forward line', 'Held dates', 'The week, and what is next', 'An ending that is anticipation', 'None', 'None', 'Seam EXISTS (&sect;12.7 d); ending PROPOSED'],
    ]))
    before_after = blk('BEFORE / AFTER &middot; RETAINED, REMOVED, ADDED', tbl(['', 'RETAINED', 'REMOVED', 'ADDED'], [
        ['H1 Sunday', 'Read; in-motion rows; the seam; the harbor chapter (as depth); Dana&rsquo;s guarantee in her row', 'The reading as the whole page; &ldquo;nothing needs you&rdquo;; the dentist as a concern', 'Maya&rsquo;s share; three ways; understanding now; something to try; the city; Alex&rsquo;s arrangement'],
        ['H2 week', 'Commitment crown form; rows; the market rhythm with Theo', '&ldquo;Go to the market&rdquo; as an assignment', 'The arrangement unit; the conditional region; the pull door; the Life &middot; People destination'],
        ['H3 new user', 'C1 Thin&rsquo;s crown after the ticket; the Chat T1 receipt', '&ldquo;Bring something&rdquo; as the first offer; weather as the whole page; the ticket&rsquo;s relocation as the whole next open', 'The city; the SAMPLE unit and sheet; &ldquo;tied to your Friday&rdquo;; a next open with a different sample'],
        ['H4 priority', 'The Urgent v2 instrument; the crown grammar', 'Airline recovery as the only urgency fixture', 'An Occasion decision by deadline; fold-and-return'],
        ['H5 return', 'Rows; the dish photograph; the reconstruction', 'The import card as lead; &ldquo;Unpack&rdquo;; &ldquo;since you last looked&rdquo; as a completion report', 'Three ways; the dish as Saturday&rsquo;s possibility; the one complete leg; status as a footnote'],
    ]))
    decisions = blk('DECISION LOG', tbl(['#', 'DECISION OR ASSUMPTION', 'STATUS'], [
        ['D-H1', 'Dominance does not require a crown. A crown renders only when something operational is at stake; otherwise the strongest unit leads bare (H1, H5).', 'Adopted here; consistent with canon &sect;11 Home'],
        ['D-H2', 'The &ldquo;one relational opening&rdquo; law (MP2) is read as a dominance + demand rule, not a page-wide count of authored material. Treatment 2 depends on this reading.', '<b>Founder ruling requested</b>'],
        ['D-H3', 'Social budget: at most one social cause may lead; at most one social unit may ask; authored material below the fold is bounded by the no-duplicate and disappears-when-empty conditions, not by a number.', '<b>Proposed</b>; reported, not silently approved'],
        ['D-H4', 'Browsing beyond selection routes to Life &middot; People (existing owner). No present-tense aperture is created; its minimum boundary is sketched on H2 as an open cross-lane decision.', '<b>Proposed</b>; social-aperture lane owns the aperture question'],
        ['D-H5', 'Codas drop relief language. Low obligation is shown by the absence of asks; the page ends on the week and one forward line.', 'Adopted here; amends 09-04 A3&rsquo;s coda'],
        ['D-H6', 'City units are marked &ldquo;not inferred from you&rdquo; and never claim personalization. They require a city-scoped source with freshness.', 'Proposed; content-production dependency'],
        ['D-H7', 'The SAMPLE convention: dashed container, stamped, inspectable, retires after it is tried or ignored twice. Never a checklist or meter.', 'Proposed'],
        ['D-H8', 'An ignored unit creates no debt and no negative preference; reappearance requires changed evidence, consequence, or context (canon &sect;15.1).', 'Consistent with canon; adopted'],
        ['D-H9', 'Assumption: the Occasion decision-by-deadline (H4) uses the Sept 4 owner-controlled collaboration posture; runtime support is unverified.', 'Assumption on Components &amp; Plan'],
    ]))
    review = blk('THE TWELVE QUESTIONS &middot; ANSWERED PER PAGE', tbl(['Q', 'H1', 'H2 (T2)', 'H3 (first)', 'H4 (during)', 'H5'], [
        ['1 First glance useful without notes', 'Weather, low water, a friend&rsquo;s loaf', 'Alex&rsquo;s Saturday and what fits', 'The cold, the L, a sample', 'What fell through, what is asked, by when', 'Weather, low water, three ways'],
        ['2 Other reasons to stay if the lead bores me', 'Three ways; the cold; the skillet; the city', 'The market; Sunday with Dana; the cold', 'Two more city units; three samples', 'The rest, folded and reachable', 'The dish; the leg; the city'],
        ['3 Received before any ask', 'Everything; no ask', 'Everything; no ask', 'Everything; the sample asks nothing', 'The two options and Maya&rsquo;s view, before &ldquo;tell Alex&rdquo;', 'Everything; no ask'],
        ['4 Longer scroll adds different value', 'Share &rarr; ways &rarr; mechanism &rarr; technique &rarr; city &rarr; reading', 'Arrangement &rarr; days &rarr; people &rarr; mechanism', 'City &rarr; sample &rarr; what else', 'Folded', 'Ways &rarr; photo &rarr; leg &rarr; city'],
        ['5 Ordinary practical competence', 'Low water, the cold split, the skillet', 'The market window, the pier at sunset', 'The L after 11', 'Which place fits by when', 'The dish timing'],
        ['6 Multiplayer through people, not avatars', 'Maya&rsquo;s words + photo; Alex&rsquo;s words', 'Four people in their own words', '&mdash; (no people yet; honest)', 'Alex asks; Maya has answered', 'Maya&rsquo;s photograph on the dinner'],
        ['7 Find shared material beyond selection', 'Door at the foot', 'Region + door &rarr; Life &middot; People', '&mdash;', 'Occasion door', 'Dinner row &rarr; Occasion'],
        ['8 Solo / thin Home still worthwhile', 'Sparse variant on H2', 'Yes (variant 3)', 'Yes, by design', 'Yes', 'Yes'],
        ['9 New users see benefits and how to try', '&mdash;', '&mdash;', 'Three samples + &ldquo;try this with yours&rdquo;', '&mdash;', '&mdash;'],
        ['10 A genuine priority stays unmistakable', 'No priority today; the lead is bare', 'The arrangement leads; nothing asks', 'The sample is not a priority', 'Yes: oxblood read + one crown + one ask', 'No priority today'],
        ['11 Calm compatible with anticipation', 'The forward line', 'The forward line', '&ldquo;the city is enough&rdquo;', '&ldquo;everything else is where you left it&rdquo;', 'The forward line'],
        ['12 Stop freely; continuing still worthwhile', 'Yes; no meter, no ask', 'Yes', 'Yes; samples retire', 'One ask, then it expires', 'Yes'],
    ]))
    handback = blk('HANDBACK &middot; BOARDS, GAPS, AND WHAT A MOCKUP DOES NOT PROVE', N(
        '<b>Boards (project &ldquo;Vesper &mdash; Home&rdquo;):</b> H0 - Ledger and Decisions &middot; H1 - Ordinary Sunday Generous &middot; H2 - Social Week Two Treatments &middot; H3 - First Open to Next Open &middot; H4 - Priority Stress Test &middot; H5 - Return Home Corrected. Previous versions are the four study boards (Board 1&ndash;4), untouched.<br><br>'
        '<b>Content production:</b> a city-scoped notice source with freshness; bounded-mechanism explanations with one source each; world rhythms (market, tide, hall set times) with owners; photographs for every plate. Every passage on these boards is invented.<br>'
        '<b>Engineering verification:</b> grant-scoped reads of authored shares with audience and expiry; Occasion decision-by-deadline under owner-controlled collaboration; a world notice linked to a held commitment; sample retirement; fold-and-return with position preserved; exposure-history suppression without inferred knowledge.<br>'
        '<b>Not shown:</b> large-text renders (listed open); native behaviour; any participant evidence. These are design reviews, not validation. No static page here proves autonomous checking, guaranteed updates, or live re-checks.'))
    inner = (head('VESPER &middot; HOME &middot; GENEROUS-VALUE PASS &middot; H0 &middot; LEDGER, COMPARISON, DECISIONS, HANDBACK', 'H0 &middot; One recommended system, and its ledger',
                  'What the five boards share, what each unit earns, what was retained/removed/added, the decisions that need a ruling, the twelve review questions answered per page, and the gaps kept separate from the design judgment.')
             + '<div style="display: flex; flex-direction: column; gap: 34px;">' + system + ledger_t + before_after + decisions + review + handback + '</div>')
    return (HEAD + f'<div style="width: 1560px; min-height: 2760px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL)

if __name__ == '__main__':
    for name, fn in [('H0 - Ledger and Decisions', H0), ('H1 - Ordinary Sunday Generous', H1), ('H2 - Social Week Two Treatments', H2), ('H3 - First Open to Next Open', H3), ('H4 - Priority Stress Test', H4), ('H5 - Return Home Corrected', H5)]:
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
