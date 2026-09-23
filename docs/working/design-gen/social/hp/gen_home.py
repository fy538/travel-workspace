import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

LIVE = os.path.join(os.path.dirname(__file__), '..', 'live')
OUT = os.path.join(os.path.dirname(__file__), 'boards'); os.makedirs(OUT, exist_ok=True)

def live(name): return open(os.path.join(LIVE, name)).read()
def between(s, a, b): i = s.index(a); j = s.index(b, i); return s[i:j]

# ───────────────────────────── instruments (fixture) ─────────────────────────────
TIDE_SAT = '''<svg width="317" height="66" viewBox="0 0 317 66" fill="none" style="width: 100%; height: auto; margin-top: 8px;">
  <path d="M2 44 Q40 12 84 12 Q126 12 154 34 Q182 56 226 56 Q268 56 315 34 L315 66 L2 66 Z" fill="rgba(61,80,102,0.20)"/>
  <path d="M2 44 Q40 12 84 12 Q126 12 154 34 Q182 56 226 56 Q268 56 315 34" stroke="#3D5066" stroke-width="2.4" fill="none" stroke-linecap="round"/>
  <rect x="188" y="58" width="80" height="6" rx="3" fill="#B0853A"/>
  <circle cx="84" cy="12" r="4.5" fill="#1B1714"/>
  <text x="94" y="16" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">HIGH 8:10</text>
  <text x="188" y="48" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">LOW WATER &#183; 1:40&#8211;4</text>
  <text x="2" y="9" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">6A</text>
  <text x="300" y="9" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">6P</text>
</svg>'''

def rhythm_bars(values, peak, now_i, w=317):
    n = len(values); slot = w / n; bw = 16; mx = max(values); H = 44
    parts = []
    for i, v in enumerate(values):
        h = max(4, round(v / mx * H)); x = i * slot + (slot - bw) / 2; y = H - h
        col = '#B0853A' if peak[0] <= i <= peak[1] else 'rgba(27,23,20,0.11)'
        parts.append(f'<rect x="{x:.1f}" y="{y}" width="{bw}" height="{h}" rx="6" fill="{col}"/>')
    nx = now_i * slot + slot / 2
    parts.append(f'<circle cx="{nx:.1f}" cy="{H + 8}" r="3" fill="#1B1714"/>')
    return f'<svg width="{w}" height="{H + 14}" viewBox="0 0 {w} {H + 14}" fill="none" style="width: 100%; height: auto; margin-top: 8px;">{"".join(parts)}</svg>'

def market_crown():
    bars = rhythm_bars([2, 4, 7, 10, 12, 9, 6, 4, 2, 1], (3, 4), 1)
    labels = ('<div style="display: flex; justify-content: space-between; margin-top: 2px;">'
              '<span class="fn" style="color: #8F877C;">8A</span>'
              '<span style="font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: #8A6628;">PEAK 9&#8211;11</span>'
              '<span class="fn" style="color: #8F877C;">1P</span></div>')
    theo = (f'<div style="display: flex; gap: 10px; align-items: flex-start; margin-top: 10px;">'
            f'<span style="width: 22px; height: 22px; border-radius: 11px; background: {INK}; color: {CARD}; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none; margin-top: 1px;">T</span>'
            f'<div style="flex: 1;"><div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK};">&ldquo;The bread stall sells out by ten &mdash; go early or don&rsquo;t bother.&rdquo;</div>'
            f'<div class="fn" style="margin-top: 3px;">THEO &middot; SHARED TUESDAY &middot; AUDIENCE: YOU &middot; THIS MOVES YOUR WINDOW TO 9:30</div></div></div>')
    return crown(PLAN, 'THIS MORNING &middot; MARKET UNTIL 1',
                 'Go to the market before half past nine',
                 'The stalls peak at ten; Theo says the bread is gone by then.',
                 bars + labels + theo,
                 cta='Open the market', fn='RHYTHM FROM PAST SATURDAYS &middot; NOTHING SAVED OR PLANNED')

PASSAGE_CH3 = [
    'The gates were set into the creek mouth in 1911, after the spring tide of the year before came up the street on a night nobody had marked. They are not a wall. They are two leaves that swing shut on the flood and drift open on the ebb, so that the creek drains but the harbor never enters.',
    'That is why the blocks on the far side of your coffee route stay dry while the near side ponds after rain: the near side sits on the old creek bed, below the sill of the gates, and drains only when the water outside is lower than the water within.',
    'Walk the curb line at low water and you can read the boundary in the pavement itself &mdash; the granite kerbs end where the gates&rsquo; protection ends.',
]
PASSAGE_CH4 = [
    'The pump station under the corner of the park was built to finish what the gates could not. On a falling tide the creek drains itself; on a rising one, with rain behind it, the water inside the gates has nowhere to go.',
    'Two pumps, sized for the storm of 1938, lift it over the sill. Their intake grates are the two iron squares you step over at the crossing &mdash; the only part of the system that is visible from the street.',
    'The chapter&rsquo;s argument is that a neighborhood learns its own hydrology one flood at a time, and forgets it one dry decade at a time.',
]

# ───────────────────────────── A1 · open time, mature context (Saturday) ─────────────────────────────
def a1_phone():
    inner = anchor_row('NEW YORK &middot; SATURDAY', '8:50 AM')
    inner += orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two &middot; Dana next Saturday.')
    inner += market_crown()
    inner += section('IN MOTION')
    inner += '<div style="padding: 0 22px;">' + row('Dana &middot; seven days out &middot; <span style="color: #6E6862;">&ldquo;keep Sunday morning for me&rdquo;</span>', avatar='D') \
             + row('Dentist Tuesday 9:00 &middot; <span style="color: #6E6862;">nothing to do before it</span>', mark='dashed', last=True) + '</div>'
    inner += section('ONE WAY THE WORLD CAN OPEN')
    inner += ('<div style="padding: 0 22px;">'
              + unit_open('FROM YOUR READING &middot; THE HARBOR BOOK &middot; CH. 3',
                          'Low water at 2:40 puts the flood line under your coffee route',
                          'The gates the chapter describes are the ones on your walk. Today the tide shows you where their protection ends.',
                          plate='thumb', plate_label='<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><path d="M8 6 L8 28 L26 28 L26 6 Z" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M12 12 L22 12 M12 16 L22 16 M12 20 L18 20" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>')
              + TIDE_SAT
              + passage(PASSAGE_CH3, 'THE HARBOR BOOK, CH. 3 &middot; YOUR COPY, P. 61&ndash;62 &middot; COMPLETE HERE &middot; NOTHING TO SAVE OR PLAN')
              + door('Walk it at low water') + '</div>')
    inner += coda('A market, a walk, and nothing owed. That&rsquo;s the morning.', 'NOTHING NEEDS YOU TODAY')
    return phone(inner, 1780)

A1_NOTES = notecol('State 1 &middot; open time, mature context', [
    ('THE FIXTURE, DECLARED ONCE', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">One ordinary New York week, September 10&ndash;13. Held: a Friday concert ticket (GA, doors 8); a Tuesday dentist; Dana arriving Saturday the 19th with one note (&ldquo;keep Sunday morning for me&rdquo;); the harbor book on the shelf, chapters 3&ndash;4 read; last Thursday&rsquo;s skillet correction; one familiar coffee route; Theo&rsquo;s greenmarket note, shared Tuesday under may-use, audience you. World truth: a cold snap Thursday night, low water Saturday 1:40&ndash;4, the market&rsquo;s Saturday rhythm. <b>Nothing from Europe.</b> All facts are fixture inventions.</div>'),
    ('UNIT 1 &middot; THE MARKET CROWN', ledger([
        ('ALREADY KNOWN', 'That the market exists and that Saturday is open.'),
        ('VESPER ADDS', 'The stalls&rsquo; rhythm (peak 9&ndash;11) and, because Theo&rsquo;s note is usable, a specific window: before 9:30. The person&rsquo;s note is the reason the window moved &mdash; that is the human dimension changing the result, not decorating it.'),
        ('WHY NOW', 'It is 8:50 on the one morning it applies. At 10:05 this unit is gone.'),
        ('COMPLETE ON VIEW', 'Yes. The decision is made by reading; the CTA opens the Place, it does not finish the value.'),
        ('OPENING IT DOES', 'Places &middot; Focus on the market, scoped to this morning (transition C2).'),
        ('REMOVE WHEN', 'After 10:00, or if Theo withdraws the note (the window reverts to &ldquo;before eleven&rdquo;, attribution gone), or if the market is closed per world truth.'),
    ])),
    ('UNIT 2 &middot; THE FLOOD-LINE READING', ledger([
        ('ALREADY KNOWN', 'The person owns the book and has read chapter 3.'),
        ('VESPER ADDS', 'The connection: the chapter&rsquo;s gates are the ones on their coffee route, and today&rsquo;s low water makes the boundary visible. The passage is composed on the page &mdash; the promise is fulfilled, not just titled.'),
        ('WHY NOW', 'Low water 1:40&ndash;4 today; the walk is possible in daylight.'),
        ('COMPLETE ON VIEW', 'Yes &mdash; the understanding is complete without walking. The door is optional.'),
        ('OPENING IT DOES', 'Places &middot; the scoped afternoon field (B1); Back returns to this unit.'),
        ('REMOVE WHEN', 'After 4 PM today; it does not return until the next daylight low water on an open day, and never as &ldquo;you missed it&rdquo;.'),
    ])),
    ('WHAT WAS CUT', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">A third opening (a film, a nearby exhibition) died at G11 &mdash; the page is better without it. The week seam is absent: on an open Saturday the week&rsquo;s shape is not the point. No &ldquo;kept for you&rdquo; block: Dana&rsquo;s guarantee is carried inside her row.</div>'),
])

# ───────────────────────────── A2 · an actual commitment (Thursday) ─────────────────────────────
def a2_phone():
    s = live('C1AvailableMature.dc.html')
    crown_html = between(s, '<!-- NOW', '<!-- IN MOTION')
    crown_html = crown_html[crown_html.index('<div'):].rstrip()
    inner = anchor_row('NEW YORK &middot; THURSDAY', '6:40 PM')
    inner += orientation('Cold coming overnight.<br>Friday is already set.', '28&deg; by morning &middot; your Friday ticket holds.')
    inner += crown_html
    inner += section('IN MOTION')
    inner += '<div style="padding: 0 22px;">' + row('Dana &middot; nine days out &middot; <span style="color: #6E6862;">&ldquo;keep Sunday morning for me&rdquo;</span>', avatar='D') \
             + row('Dentist Tuesday 9:00 &middot; <span style="color: #6E6862;">walk, don&rsquo;t wait for the bus</span>', mark='dashed', last=True) + '</div>'
    inner += section('ONE WAY THE WORLD CAN OPEN')
    tide = between(s, '<svg width="240" height="58"', '</svg>') + '</svg>'
    inner += ('<div style="padding: 0 22px;">'
              + unit_open('FROM YOUR READING &middot; THE HARBOR BOOK &middot; CH. 3',
                          'The gates on your coffee route still choose which blocks flood',
                          'Your usual walk sits in the calm of low water &mdash; nothing to visit, save, or plan.',
                          plate='thumb', plate_label='<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><path d="M8 6 L8 28 L26 28 L26 6 Z" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M12 12 L22 12 M12 16 L22 16 M12 20 L18 20" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>')
              + tide.replace('width="240"', 'width="317"').replace('style="margin-top: 6px;"', 'style="width: 100%; height: auto; margin-top: 8px;"')
              + passage(PASSAGE_CH3[:2], 'THE HARBOR BOOK, CH. 3 &middot; YOUR COPY, P. 61 &middot; COMPLETE HERE')
              + '</div>')
    inner += ('<div style="margin: 44px 22px 0 22px; display: flex; flex-direction: column; gap: 6px;"><div class="kick">CARRIED FORWARD</div>'
              f'<div style="display: flex; gap: 10px; align-items: flex-start;">{NOTE}<div style="font-size: 14px; line-height: 19px;">Last Thursday&rsquo;s soggy-crust note is why tonight&rsquo;s skillet version <b style="font-weight: 600;">preheats dry</b>.</div></div>'
              + door('Why this?') + '</div>')
    inner += coda('Tonight is the skillet and a warm kitchen. Friday is handled.', 'NOTHING NEEDS YOU BEFORE FRIDAY')
    return phone(inner, 1620)

A2_NOTES = notecol('State 2 &middot; an actual commitment', [
    ('WHAT CHANGED FROM THE ACCEPTED BOARD', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">C1 &middot; Ordinary Available already lets practical relief lead without turning the page into operations, so the crown is <b>reused verbatim</b>. One change: the reading unit now <b>composes the passage</b> under its curve instead of promising it behind a title. Everything else is the accepted board.</div>'),
    ('UNIT 1 &middot; THE FRIDAY CROWN', ledger([
        ('ALREADY KNOWN', 'The ticket, doors at 8, that the person works until six.'),
        ('VESPER ADDS', 'The constraint is the way back: after ten the surface route adds ~25 minutes. Leave from work, not home.'),
        ('WHY NOW', 'Thursday evening is the last time the plan can change cheaply.'),
        ('COMPLETE ON VIEW', 'Yes. The band is the decision.'),
        ('OPENING IT DOES', '&ldquo;Open Friday evening&rdquo; &rarr; the evening&rsquo;s Plan view (interaction lane), Back returns here.'),
        ('REMOVE WHEN', 'Friday 10 PM, or if set times post (the band re-anchors and the footnote changes).'),
    ])),
    ('UNIT 2 &middot; THE READING', ledger([
        ('ALREADY KNOWN', 'The book; chapter 3.'),
        ('VESPER ADDS', 'The connection to the coffee route and today&rsquo;s tide state; the two paragraphs that make it.'),
        ('WHY NOW', 'Weak: nothing about Thursday requires it. It survives because it is consumable, keeps, and is the one non-operational thing on an operational evening &mdash; the page would be colder without it (C1 finding, counterfactual recorded).'),
        ('COMPLETE ON VIEW', 'Yes.'),
        ('OPENING IT DOES', 'Nothing required. No door on Thursday; the walk is Saturday&rsquo;s.'),
        ('REMOVE WHEN', 'Once read on any screen (G3), or if the book leaves custody.'),
    ])),
    ('UNIT 3 &middot; CARRIED FORWARD', ledger([
        ('ALREADY KNOWN', 'Last week&rsquo;s note.'),
        ('VESPER ADDS', 'That tonight&rsquo;s version changed because of it &mdash; the smallest causal receipt.'),
        ('REMOVE WHEN', 'After tonight; the lineage stays in Life.'),
    ])),
])

# ───────────────────────────── A3 · the next open after no engagement (Sunday) ─────────────────────────────
def a3_phone():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation_direct('A clear, cold Sunday.', 'Warming by noon &middot; nothing needs you today.')
    # value first: a complete reading, not administration
    inner += ('<div style="padding: 22px 22px 0 22px;">'
              + unit_open('SUNDAY READING &middot; THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN',
                          'The pumps under the park finish what the gates cannot',
                          'The two iron squares you step over at the crossing are the only visible part of the system.',
                          plate='thumb', plate_label='<svg width="34" height="34" viewBox="0 0 34 34" fill="none"><rect x="9" y="9" width="7" height="7" stroke="#8A6628" stroke-width="1.4"/><rect x="18" y="9" width="7" height="7" stroke="#8A6628" stroke-width="1.4"/><path d="M8 24 L26 24" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>')
              + passage(PASSAGE_CH4, 'THE HARBOR BOOK, CH. 4 &middot; YOUR COPY, P. 74&ndash;77 &middot; COMPLETE HERE &middot; NOTHING TO SAVE OR PLAN')
              + '</div>')
    # the week's shape as a seam, after the value, zero demand
    inner += week_seam([
        ('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE),
        ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:D', ''), 'Dana', INK)], top=40)
    inner += '<div style="padding: 0 22px;">' + row('Dana &middot; Saturday &middot; <span style="color: #6E6862;">next Sunday morning stays yours &mdash; she asked</span>', avatar='D') \
             + row('Dentist Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; at nine &middot; walk, the bus is slower</span>', mark='dashed', last=True) + '</div>'
    inner += coda('Nothing here needs an answer. It&rsquo;s just a good morning, held.', 'NOTHING NEEDS YOU TODAY')
    return phone(inner, 1330)

A3_NOTES = notecol('State 3 &middot; the next open, after no engagement', [
    ('WHAT HAPPENED BETWEEN', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">Saturday&rsquo;s page was opened at 8:50 and nothing on it was tapped. The market window closed at ten; low water passed at four. <b>Nothing was written.</b> No task, no &ldquo;you missed&rdquo;, no inference that the person dislikes markets or tides. Sunday&rsquo;s page is compiled fresh from owner truth and the clock.</div>'),
    ('THE DIAGNOSIS, ANSWERED', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">The ruled Quiet board led with administration: &ldquo;the week is already in shape&rdquo;, a kept-Sunday crown, then past-show and dentist rows, and only then the market and the reading. Here the order inverts. <b>Value first</b> (a complete reading), the week&rsquo;s shape as a seam, and the standing guarantee folded into Dana&rsquo;s own row as one clause. &ldquo;Friday&rsquo;s show &middot; went&rdquo; is gone: a past event that needs nothing is Life&rsquo;s, not Home&rsquo;s.</div>'),
    ('UNIT 1 &middot; THE SUNDAY READING', ledger([
        ('ALREADY KNOWN', 'The book; chapter 4 has been read.'),
        ('VESPER ADDS', 'The two iron grates at the crossing are the pump intakes &mdash; the chapter located in the person&rsquo;s own route. Not the same unit as Saturday&rsquo;s (G3): different chapter, different mechanism, different place on the walk.'),
        ('WHY NOW', 'Quiet morning, complete on view, four minutes. It is the substance the page has; it is not filler for an empty day.'),
        ('COMPLETE ON VIEW', 'Yes.'),
        ('OPENING IT DOES', 'No door. There is nothing to visit today.'),
        ('REMOVE WHEN', 'Once read; or if a stronger current unit appears (a change to Tuesday, a note from Dana).'),
    ])),
    ('UNIT 2 &middot; THE WEEK SEAM + ROWS', ledger([
        ('ALREADY KNOWN', 'Everything on it.'),
        ('VESPER ADDS', 'Only the Tuesday fact: 24&deg; at nine, walking beats the bus. Dana&rsquo;s clause carries the standing guarantee without a crown.'),
        ('WHY NOW', 'Sunday is when the week is looked at. Zero demand.'),
        ('REMOVE WHEN', 'The seam never leads; it exists only while there is a marked day within seven.'),
    ])),
    ('WHAT RETURNS LATER', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">The market rhythm may return next Saturday morning if the day is open; Theo&rsquo;s note rides with it only while his grant stands. The tide walk returns at the next daylight low water on an open day. Neither returns because it was ignored.</div>'),
])

# ───────────────────────────── A4 · thin history (reused) ─────────────────────────────
def a4_phone():
    s = live('C1ThinWeek.dc.html')
    a = s.index('<div style="width: 393px'); b = s.index('<!-- ═══ SIDE STRIP') if '<!-- ═══ SIDE STRIP' in s else s.index('<!-- side', a) if '<!-- side' in s else None
    if b is None:
        # fall back: take up to the second top-level phone-width div
        b = s.index('<div style="flex: 1; padding: 24px 26px', a)
    ph = s[a:b].rstrip()
    ph = ph.replace('min-height: 1100px;', 'min-height: 1100px; flex: none;', 1)
    return ph

A4_NOTES = notecol('Thin history &middot; one supplied object', [
    ('REUSED AS ACCEPTED', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">C1 &middot; Thin First Week is reused unchanged. One deliberately supplied object (a ticket) plus modest world truth (tonight&rsquo;s forecast) produce a complete crown; the page then says honestly what it holds and stops. No account setup, no profile, no documentation assignment is the admission price.</div>'),
    ('THE ONE UNIT', ledger([
        ('ALREADY KNOWN', 'The ticket.'),
        ('VESPER ADDS', 'Door-to-door timing, coat check, and that arriving by 8:40 skips nothing &mdash; from the ticket and the forecast only.'),
        ('COMPLETE ON VIEW', 'Yes.'),
        ('OPENING IT DOES', 'Nothing required; the Q-and-A on the right (gate 14) ends with no residue.'),
        ('REMOVE WHEN', 'After the show.'),
    ])),
    ('HELD TO THE SAME LAWS', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">The burden strip&rsquo;s carried leg is gold (&sect;12.7 h); one italic voice line (A8). Nothing else on the page was changed for this pass.</div>'),
])

def write(name, phone_html, notes_html, h, w=1000, active='Home'):
    inner = f'<div style="width: 393px; flex: none;">{label(GREEN, "PROPOSAL", "HP value pass 09-04 &middot; not canon until ruled")}{phone_html}</div>{notes_html}'
    open(os.path.join(OUT, name + '.dc.html'), 'w').write(board(inner, w, h))
    print('wrote', name)

if __name__ == '__main__':
    write('HPA1Open', a1_phone(), A1_NOTES, 1900)
    write('HPA2Commitment', a2_phone(), A2_NOTES, 1720)
    write('HPA3NextOpen', a3_phone(), A3_NOTES, 1560)
    write('HPA4Thin', a4_phone(), A4_NOTES, 1200)
