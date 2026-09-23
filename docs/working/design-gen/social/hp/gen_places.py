import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
OUT = os.path.join(os.path.dirname(__file__), 'boards'); os.makedirs(OUT, exist_ok=True)

CHEVRON_DOWN = '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" style="flex: none;"><path d="M2.5 4L5 6.5L7.5 4" stroke="#6E6862" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def scope_header(scope, sub, back=False, live=None):
    left = BACK if back else ''
    lv = f'<span style="display: inline-flex; align-items: center; gap: 6px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {OX};"><span style="width: 6px; height: 6px; border-radius: 3px; background: {OX};"></span>{live}</span>' if live else ''
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{left}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;{" display: flex; align-items: center; gap: 5px;" if scope == scope.upper() else ""}">{scope}{CHEVRON_DOWN if scope == scope.upper() else ""}</div>'
            f'<div style="font-size: 14px; line-height: 19px; color: #6E6862;">{sub}</div></div>{lv}{SEARCH}{MAPI}</div>')

def field_head(kick, top=22):
    return f'<div style="padding: {top}px 22px 0 22px;"><div class="shead" style="color: {GOLDD};"><span>{kick}</span><span class="rule"></span></div></div>'

def map_wash(h, svg_inner, top=10):
    return (f'<div style="margin: {top}px 22px 0 22px; height: {h}px; border-radius: 12px; position: relative; overflow: hidden; background: repeating-linear-gradient(0deg, rgba(27,23,20,0.05) 0 1px, transparent 1px 26px), repeating-linear-gradient(90deg, rgba(27,23,20,0.05) 0 1px, transparent 1px 26px), {WASH};">'
            f'<svg width="349" height="{h}" viewBox="0 0 349 {h}" fill="none" style="position: absolute; inset: 0; width: 100%; height: 100%;">{svg_inner}</svg></div>')

def branch(icon, title, reason, burden, ghost=False):
    col = MUTE if ghost else INK
    return (f'<div style="display: flex; gap: 14px; align-items: center; min-height: 56px; border-top: 1px solid rgba(27,23,20,0.06); padding: 8px 0;">'
            f'<div class="hatch" style="width: 44px; height: 44px; border-radius: 12px; flex: none; display: flex; align-items: center; justify-content: center;">{icon}</div>'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; font-weight: 600; line-height: 19px; color: {col};">{title}</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">{reason} &middot; {burden}</div></div>{CHEV}</div>')

def cont_rows(items):
    out = '<div style="padding: 32px 22px 0 22px;">'
    for i, (t, count) in enumerate(items):
        c = f'<span class="fn" style="color: {MUTE}; margin-right: 4px;">{count}</span>' if count else ''
        out += f'<div class="row" style="min-height: 52px;{" border-bottom: 1px solid rgba(27,23,20,0.06);" if i == len(items)-1 else ""}"><span style="font-size: 15px; flex: 1;">{t}</span>{c}{CHEV}</div>'
    return out + '</div>'

def places_phone(inner, h): return phone(inner, h, active='Places')

ICON_TIDE = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M3 14 Q7 10 11 14 Q15 18 19 14" stroke="#8A6628" stroke-width="1.4" stroke-linecap="round"/><path d="M3 9 Q7 5 11 9 Q15 13 19 9" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'
ICON_MARKET = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 9 L11 4 L18 9 V18 H4 Z" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 18 V13 H14 V18" stroke="#B0853A" stroke-width="1.3"/></svg>'
ICON_BOOK = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M5 4 H17 V18 H5 Z" stroke="#8A6628" stroke-width="1.4"/><path d="M8 8 H14 M8 11 H14 M8 14 H12" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'
ICON_FERRY = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 13 H18 L16 17 H6 Z" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 13 V8 H14 V13" stroke="#B0853A" stroke-width="1.3"/></svg>'
ICON_BOWL = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 11 H18 C18 15 15 18 11 18 C7 18 4 15 4 11 Z" stroke="#8A6628" stroke-width="1.4"/><path d="M8 7 L14 7" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'
ICON_COUNTER = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 9 H18 M6 9 V17 M16 9 V17" stroke="#8A6628" stroke-width="1.4" stroke-linecap="round"/><path d="M8 6 H14" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'
ICON_TABLE = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><ellipse cx="11" cy="9" rx="7" ry="3" stroke="#8A6628" stroke-width="1.4"/><path d="M5 9 V16 M17 9 V16" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'
ICON_HALL = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 18 V8 L11 4 L18 8 V18" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 18 V12 H14 V18" stroke="#B0853A" stroke-width="1.3"/></svg>'
ICON_TRAIN = '<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><rect x="6" y="4" width="10" height="13" rx="2" stroke="#8A6628" stroke-width="1.4"/><path d="M8 17 L6.5 19 M14 17 L15.5 19 M8 8 H14" stroke="#B0853A" stroke-width="1.3" stroke-linecap="round"/></svg>'

# ───────────────────────────── B1 · open afternoon, no destination ─────────────────────────────
def b1():
    svg = ('<path d="M0 0 L120 0 Q104 40 118 80 Q126 110 110 140 L0 140 Z" fill="rgba(61,80,102,0.12)" stroke="rgba(61,80,102,0.22)"/>'
           '<path d="M150 20 L150 130 M190 20 L190 130 M230 20 L230 130 M270 20 L270 130" stroke="rgba(27,23,20,0.06)" stroke-width="1.2"/>'
           '<path d="M118 78 L330 78" stroke="#B0853A" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 7"/>'
           '<path d="M118 50 Q170 60 200 44 Q240 24 300 30" stroke="#1B1714" stroke-width="1.6" fill="none" stroke-linecap="round"/>'
           '<circle cx="118" cy="50" r="5" fill="#B0853A"/><circle cx="300" cy="30" r="4.5" fill="#1B1714"/>'
           '<text x="128" y="40" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8A6628">THE GATES</text>'
           '<text x="240" y="98" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8A6628">FLOOD LINE</text>'
           '<text x="262" y="24" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#1B1714">YOUR COFFEE</text>')
    inner = scope_header('NEW YORK &middot; NEAR YOU', 'Saturday &middot; 1:05 PM &middot; nothing chosen')
    inner += field_head('ONE LOW-WATER AFTERNOON, AND THREE THINGS THAT DON&rsquo;T NEED IT')
    inner += map_wash(140, svg)
    inner += (f'<div style="padding: 14px 22px 0 22px;"><div style="{SERIF} font-size: 18px; line-height: 25px;">Low water until four puts the flood line under your coffee route &mdash; the one afternoon a week the boundary is walkable.</div>'
              '<svg width="317" height="46" viewBox="0 0 317 46" fill="none" style="width: 100%; height: auto; margin-top: 10px;">'
              '<rect x="2" y="20" width="313" height="8" rx="4" fill="rgba(27,23,20,0.07)"/>'
              '<rect x="60" y="15" width="150" height="18" rx="9" fill="#B0853A"/>'
              '<circle cx="38" cy="24" r="5" fill="#1B1714"/>'
              '<text x="60" y="10" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">LOW WATER &#183; 1:40&#8211;4</text>'
              '<text x="2" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">1 PM</text>'
              '<text x="296" y="44" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">6</text></svg>'
              '<div class="fn" style="margin-top: 2px;">40 MIN ON FOOT &middot; LEVEL &middot; STARTS AT YOUR CORNER &middot; TIDE TABLE READ 12:50</div>'
              + door('Open the walk') + '</div>')
    inner += ('<div style="padding: 26px 22px 0 22px;">'
              + branch(ICON_MARKET, 'The market', 'stalls packing up by 1:30', 'only if you are already near', ghost=True)
              + branch(ICON_BOOK, 'The bookhall', 'open until 11, quiet upstairs', '8 minutes from the walk&rsquo;s end')
              + branch(ICON_FERRY, 'Red Hook, your saved place', 'the 2:20 crossing still runs', 'back by land; the return is the loose end')
              + '</div>')
    inner += cont_rows([('Saved near you', '2'), ('Your New York map', ''), ('Somewhere else &mdash; a place or a question', '')])
    inner += coda('The field is finite. This is all of it today.', 'COUNTED TOWARD &middot; NOTHING HIDDEN')
    return places_phone(inner, 1330)

B1_NOTES = notecol('B1 &middot; an open afternoon, no destination', [
    ('WHAT THE FIELD IS DOING', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">No Plan, no chosen Place. The lead is the one thing that is only possible this afternoon (low water is world truth, the coffee route is the person&rsquo;s own). Three branches follow, each with one reason and one burden, chosen for <b>different access structures</b>: a closing window, an open-late interior, a scheduled crossing. The market is drawn ghost because its reason has nearly expired &mdash; it stays on the list so the field is honest about what it counted.</div>'),
    ('WHAT THIS IS NOT', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">Not a recommendation shelf: no ratings, no popularity, no &ldquo;trending near you&rdquo;. Not Home: the lead explains <i>where</i> and <i>when</i>, not why it matters to the week. Not the Returned-Saturday waterfront: Red Hook appears once, as the saved place it is, with its return-leg burden stated.</div>'),
    ('TAP &middot; BACK &middot; PERSIST', ledger([
        ('OPEN THE WALK', 'Focus on the route as a Place-relation (the flood line), not a venue. Back restores this field and scroll.'),
        ('A BRANCH', 'Focus on that Place with the afternoon as context (interval 1:05&ndash;6). Back returns to the row.'),
        ('SOMEWHERE ELSE', 'The scope sheet (B6). Choosing a scope re-queries the same result set with a new context handle; nothing is written.'),
        ('PERSISTED', 'Nothing. Scope and scroll survive Back only.'),
    ])),
])

# ───────────────────────────── B2 · an explicit practical question ─────────────────────────────
def b2():
    inner = scope_header('NEAR THE HALL &middot; BEFORE 8', 'Friday &middot; 5:40 PM &middot; &ldquo;somewhere to eat before the show&rdquo;')
    inner += field_head('THREE THAT FIT THE WINDOW &middot; DOORS AT 8 IS THE CONSTRAINT')
    # span comparison: three lanes against the doors
    inner += ('<div style="padding: 14px 22px 0 22px;"><svg width="317" height="118" viewBox="0 0 317 118" fill="none" style="width: 100%; height: auto;">'
              '<rect x="262" y="0" width="1.5" height="100" fill="#7A2E2E" opacity="0.7"/>'
              '<text x="256" y="10" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#7A2E2E">DOORS 8</text>'
              '<text x="2" y="26" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">NOODLE BAR</text>'
              '<rect x="60" y="30" width="150" height="12" rx="6" fill="#B0853A"/><circle cx="210" cy="36" r="6" fill="#B0853A"/>'
              '<text x="222" y="40" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">7:25</text>'
              '<text x="2" y="60" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE COUNTER</text>'
              '<rect x="30" y="64" width="100" height="6" rx="3" fill="rgba(27,23,20,0.14)"/><circle cx="130" cy="67" r="5" fill="#EFEAE0" stroke="#6E6862" stroke-width="1.5"/>'
              '<text x="142" y="71" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#6E6862">6:45</text>'
              '<text x="2" y="90" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">THE TRATTORIA</text>'
              '<rect x="100" y="94" width="176" height="6" rx="3" fill="rgba(27,23,20,0.14)"/><circle cx="276" cy="97" r="5" fill="#EFEAE0" stroke="#7A2E2E" stroke-width="1.5"/>'
              '<text x="288" y="101" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#7A2E2E">8:10</text>'
              '<text x="2" y="116" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">5:40</text>'
              '<text x="315" y="116" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">8:30</text></svg>'
              '<div class="fn" style="margin-top: 4px;">SEAT-TO-DOORS, WALKING &middot; HOURS READ 5:38 &middot; NO RESERVATIONS HELD OR MADE</div></div>')
    inner += ('<div style="padding: 18px 22px 0 22px;">'
              + branch(ICON_BOWL, 'The noodle bar on 7th', 'seats by six without a wait, 9 min to the hall', 'closes the kitchen at 9:30 &mdash; no lingering')
              + branch(ICON_COUNTER, 'The counter at the market hall', '4 min to the doors, fastest', 'standing only, and loud')
              + branch(ICON_TABLE, 'The trattoria', 'a table at 6:15 works', '12 min out; a second course risks the doors', ghost=True)
              + '</div>')
    inner += (f'<div style="padding: 22px 22px 0 22px;"><div style="{SERIF} font-size: 15px; line-height: 22px; color: {INK2};">Not on this list: two places that would need a reservation you don&rsquo;t hold. If you want one, their booking pages are a tap away from the place itself &mdash; Vesper won&rsquo;t book for you.</div>'
              + door('Ask about one of these') + '</div>')
    inner += cont_rows([('Everything near the hall, on the map', ''), ('Change the question', '')])
    inner += coda('Three fit. That&rsquo;s the answer, not a menu.', 'THE FIELD IS FINITE')
    return places_phone(inner, 1330)

B2_NOTES = notecol('B2 &middot; an explicit practical question', [
    ('THE QUESTION BECOMES THE SCOPE', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">&ldquo;Somewhere to eat before the show&rdquo; is not a search string; it is a scope with a constraint (doors at 8) and an interval (now until then). The handle shows both. The one instrument is a span comparison: each candidate&rsquo;s seat-to-doors lane against the oxblood constraint &mdash; the gap <i>is</i> the answer. The list below restates nothing; it carries reason and burden per row.</div>'),
    ('EXTERNAL HANDOFF, NOT CHECKOUT', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">Per the contraction direction, the field neither holds nor makes reservations. Places that need one are named as absent, and the reservation link lives on the Place itself (transition C2). Returning from a provider does not mark anything booked.</div>'),
    ('TAP &middot; BACK &middot; PERSIST', ledger([
        ('A ROW', 'Focus with the question as context: the seat-to-doors lane rides along as the Place&rsquo;s current affordance. Back restores the list.'),
        ('ASK ABOUT ONE', 'Chat with origin context (this scope, this candidate set, the constraint). Back returns here; nothing is written unless the person keeps something there.'),
        ('CHANGE THE QUESTION', 'The scope sheet with the question editable. Same result-set contract.'),
        ('PERSISTED', 'Nothing. The question expires with the doors.'),
    ])),
])

# ───────────────────────────── B3 · a curiosity understood without going ─────────────────────────────
def b3():
    diagram = ('<rect x="0" y="0" width="349" height="150" fill="none"/>'
               '<path d="M20 100 L150 100 L150 70 L329 70" stroke="#1B1714" stroke-width="1.6" fill="none"/>'
               '<rect x="20" y="100" width="130" height="30" fill="rgba(61,80,102,0.20)"/>'
               '<text x="28" y="121" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#1B1714">NEAR SIDE &#183; CREEK BED</text>'
               '<text x="160" y="60" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#1B1714">FAR SIDE</text>'
               '<path d="M150 70 L150 130" stroke="#B0853A" stroke-width="3" stroke-linecap="round"/>'
               '<text x="158" y="92" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8A6628">THE SILL</text>'
               '<path d="M92 130 L92 140 M108 130 L108 140" stroke="#7A2E2E" stroke-width="2" stroke-linecap="round"/>'
               '<text x="114" y="142" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#7A2E2E">PUMPS</text>'
               '<text x="240" y="126" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">HARBOR &#8594;</text>')
    inner = (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{BACK}'
             f'<div style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">YOUR COFFEE ROUTE &middot; WHY IT FLOODS</div>'
             f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE};">A question, not a destination</div></div>{MAPI}</div>')
    inner += (f'<div style="padding: 22px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px;">The near side floods because it is the old creek bed</div>'
              f'<div style="{SERIF} font-size: 16px; line-height: 23px; margin-top: 8px; color: {INK2};">Your route crosses a boundary you cannot see from the pavement: one side sits below the sill of the 1911 gates and drains only when the harbor is lower than the street; the other side never needed the gates at all.</div></div>')
    inner += map_wash(150, diagram, top=16)
    rows = [('LEVEL', 'The near side is two to three feet lower &mdash; the filled creek. Rain ponds there before it drains.'),
            ('THE GATES', 'They close on the flood tide. When the harbor is high and it rains, the creek side has nowhere to drain.'),
            ('THE PUMPS', 'Two, under the park corner. Their intake grates are the iron squares at your crossing.')]
    inner += '<div style="padding: 22px 22px 0 22px;">' + ''.join(f'<div style="display: grid; grid-template-columns: 96px 1fr; gap: 12px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.06);"><span class="kick">{k}</span><span style="font-size: 14px; line-height: 19px;">{v}</span></div>' for k, v in rows) + '</div>'
    inner += ('<div style="padding: 26px 22px 0 22px;"><div class="shead"><span>WHY VESPER THINKS THIS</span><span class="rule"></span></div>'
              '<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 10px; font-size: 14px; line-height: 19px;">'
              '<div style="display: flex; gap: 10px;"><span class="kick" style="min-width: 10px;">1</span><span>Your harbor book, chapters 3 and 4</span></div>'
              '<div style="display: flex; gap: 10px;"><span class="kick" style="min-width: 10px;">2</span><span>The city&rsquo;s published flood-zone map for these blocks</span></div>'
              '<div style="display: flex; gap: 10px;"><span class="kick" style="min-width: 10px;">3</span><span>The tide table, read this morning</span></div>'
              '<div style="display: flex; gap: 10px;"><span class="kick" style="min-width: 10px;">4</span><span>Your own route, as you walk it</span></div></div>'
              f'<div style="{SERIF} font-style: italic; font-size: 16px; line-height: 23px; color: {MUTE}; margin-top: 14px;">The book explains the mechanism; the map places your route on it. Neither says which blocks will flood on a given day &mdash; that depends on the tide and the rain together.</div></div>')
    inner += (f'<div style="padding: 26px 22px 0 22px;"><div style="{SERIF} font-size: 15px; line-height: 22px; color: {INK2};">There is nothing to visit. This is complete as read.</div>'
              + door('Keep this reading') + '</div>')
    inner += cont_rows([('Walk the flood line at the next low water', ''), ('The harbor book, in Life', '')])
    inner += coda('Understood, not scheduled.', 'NOTHING TO SAVE OR PLAN')
    return places_phone(inner, 1470)

B3_NOTES = notecol('B3 &middot; a curiosity, understood without going', [
    ('A PATH WITHOUT A DESTINATION', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">This is the Place Path anatomy (relation statement, difference diagram, typed distinctions, evidence apparatus, analogy limit) applied to a question about the person&rsquo;s own block. The diagram earns its place because the relation is spatial &mdash; a level, a sill, a pump. No CTA to go anywhere; the value is the understanding, complete on view.</div>'),
    ('HONESTY', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">The apparatus names what each source contributes and what none of them can say (which day it floods). Fixture: the book, the map, and the tide table are all inventions; the anatomy is the point.</div>'),
    ('TAP &middot; BACK &middot; PERSIST', ledger([
        ('KEEP THIS READING', 'Keeps this exact composition (Chat/editorial Keep rule) &mdash; not the place, not an intention. Readback: &ldquo;Kept &middot; in Life under the harbor book&rdquo;.'),
        ('WALK IT NEXT LOW WATER', 'A door to B1&rsquo;s lead when the next daylight low water is known; otherwise the row is absent, not disabled.'),
        ('BACK', 'To wherever the question was asked (Home unit, Chat, or the field), exact scroll.'),
        ('PERSISTED', 'Only the Keep, if chosen.'),
    ])),
])

# ───────────────────────────── B4 · a friend's perspective under grant ─────────────────────────────
def b4():
    svg = ('<path d="M120 20 L120 130 M200 20 L200 130 M40 60 L320 60 M40 100 L320 100" stroke="rgba(27,23,20,0.06)" stroke-width="1.2"/>'
           '<rect x="130" y="66" width="66" height="30" rx="4" fill="rgba(176,133,58,0.18)" stroke="#8A6628" stroke-width="1.3"/>'
           '<circle cx="144" cy="80" r="5" fill="#B0853A"/>'
           '<text x="140" y="56" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#1B1714">THE MARKET</text>'
           '<text x="130" y="112" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8A6628">BREAD STALL &#183; NW CORNER</text>'
           '<path d="M40 128 Q90 120 128 96" stroke="#1B1714" stroke-width="1.6" stroke-dasharray="1.5 5" fill="none" stroke-linecap="round"/>'
           '<text x="40" y="122" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">YOU &#183; 9 MIN</text>')
    inner = scope_header('THE MARKET', 'Saturday &middot; 8:55 AM &middot; open until 1', back=True)
    inner += map_wash(140, svg, top=22)
    inner += (f'<div style="padding: 28px 22px 0 22px;"><div class="shead" style="color: {GOLDD};"><span>THIS MORNING&rsquo;S READ</span><span class="rule"></span></div>'
              f'<div style="{SERIF} font-size: 18px; line-height: 25px; margin-top: 8px;">Go before half past nine. The stalls peak at ten; the bread is gone by then.</div>')
    # rhythm + attribution mark
    from gen_home import rhythm_bars
    inner += rhythm_bars([2, 4, 7, 10, 12, 9, 6, 4, 2, 1], (3, 4), 1)
    inner += ('<div style="display: flex; justify-content: space-between; margin-top: 2px;"><span class="fn" style="color: #8F877C;">8A</span><span style="font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: #8A6628;">PEAK 9&#8211;11</span><span class="fn" style="color: #8F877C;">1P</span></div>'
              '<div class="fn" style="margin-top: 6px;">WITHOUT THEO&rsquo;S NOTE THIS READ &ldquo;BEFORE ELEVEN&rdquo; &middot; RHYTHM FROM PAST SATURDAYS</div></div>')
    inner += (f'<div style="padding: 28px 22px 0 22px;"><div class="shead"><span>YOUR TRACE HERE</span><span class="rule"></span></div>'
              f'<div style="font-size: 14px; line-height: 19px; margin-top: 8px;">Three Saturdays this year &middot; last on the 22nd.</div></div>')
    inner += (f'<div style="margin: 18px 22px 0 22px; background: {CARD}; border-radius: 12px; box-shadow: 0 1px 2px rgba(27,23,20,0.05); padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start;">'
              f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; flex: none;">T</span>'
              f'<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 5px;"><div class="kickm">THEO &middot; SHARED WITH YOU</div>'
              f'<div style="{SERIF} font-size: 17px; line-height: 24px;">&ldquo;The bread stall sells out by ten &mdash; go early or don&rsquo;t bother. The cheese people are fine till noon.&rdquo;</div>'
              f'<div class="fn">FROM A MARKET NOTE &middot; SHARED TUESDAY &middot; AUDIENCE: YOU &middot; HIS WORDS, KEPT HIS</div></div></div>')
    doors = [('ACCESS', 'Where the bread stall stands, and the quiet way in'), ('ALTERNATIVE', 'The Sunday market in the park &mdash; a later rhythm, no bread')]
    inner += '<div style="padding: 28px 22px 0 22px;">' + ''.join(f'<div style="display: flex; align-items: center; gap: 12px; min-height: 52px; border-top: 1px solid rgba(27,23,20,0.06);{" border-bottom: 1px solid rgba(27,23,20,0.06);" if i == 1 else ""}"><span class="kick" style="min-width: 96px;">{k}</span><span style="font-size: 14px; line-height: 19px; flex-grow: 1;">{v}</span>{CHEV}</div>' for i, (k, v) in enumerate(doors)) + '</div>'
    inner += (f'<div style="padding: 28px 22px 0 22px; display: flex; flex-direction: column; gap: 10px;"><div style="min-height: 44px; background: {UMBER}; border-radius: 12px; display: flex; align-items: center; justify-content: center;"><span style="color: {CARD}; font-size: 14px; font-weight: 600;">Walk there &middot; 9 min</span></div>'
              + door('Ask Vesper about the market') + '</div>')
    inner += coda('Theo changed the time, not the place.', 'HIS NOTE, HIS WORDS &middot; WITHDRAWABLE BY HIM')
    return places_phone(inner, 1520)

B4_NOTES = notecol('B4 &middot; a friend&rsquo;s perspective, under an existing grant', [
    ('THE FRIEND CHANGES THE VALUE', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">Theo&rsquo;s note is not a quote on a card for decoration. It moves the page&rsquo;s read from &ldquo;before eleven&rdquo; (the rhythm alone) to &ldquo;before half past nine&rdquo;, and the page says so in one footnote. His words stay his &mdash; the attributed card is the human lane, separate from Vesper&rsquo;s verified lane (hours, rhythm) &mdash; and the footer states who can withdraw it.</div>'),
    ('WHAT DOES NOT HAPPEN', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">No &ldquo;friends who like this market&rdquo;, no presence, no reply obligation, no inference that Theo likes markets. The grant covers one note, one audience, one use.</div>'),
    ('TAP &middot; BACK &middot; PERSIST', ledger([
        ('WALK THERE', 'Starts a route in the map view with the 9:30 window as the constraint. Not a Plan.'),
        ('THEO&rsquo;S CARD', 'Opens the note&rsquo;s source with its grant ledger (audience, use, retention). Nothing is copied.'),
        ('WITHDRAWAL', 'If Theo pulls the note, this page recompiles: the read reverts to &ldquo;before eleven&rdquo;, the card and the footnote disappear, Home&rsquo;s crown (A1) recompiles the same way.'),
        ('PERSISTED', 'Nothing by viewing.'),
    ])),
])

# ───────────────────────────── B5 · another neighborhood, less history ─────────────────────────────
def b5():
    svg = ('<path d="M0 60 L349 60 M0 100 L349 100 M60 0 L60 140 M140 0 L140 140 M220 0 L220 140 M300 0 L300 140" stroke="rgba(27,23,20,0.06)" stroke-width="1.2"/>'
           '<path d="M20 80 L330 80" stroke="#B0853A" stroke-width="3" stroke-linecap="round"/>'
           '<rect x="150" y="30" width="20" height="20" rx="4" fill="none" stroke="#6E6862" stroke-width="1.4"/>'
           '<text x="24" y="72" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#8A6628">74TH ST &#183; THE FOOD CORRIDOR</text>'
           '<text x="176" y="44" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="1" fill="#1B1714">7 TRAIN</text>')
    inner = scope_header('JACKSON HEIGHTS', 'Saturday afternoon &middot; no history of yours here')
    inner += field_head('WHAT THE WORLD SAYS ABOUT A SATURDAY HERE &middot; NOTHING OF YOURS YET')
    inner += map_wash(140, svg)
    inner += (f'<div style="padding: 14px 22px 0 22px;"><div style="{SERIF} font-size: 18px; line-height: 25px;">One corridor carries most of the afternoon: a dozen kitchens along 74th within four blocks of the 7, busiest between two and five.</div>'
              '<div class="fn" style="margin-top: 8px;">FROM PUBLIC HOURS AND TRANSIT TRUTH &middot; NOT A RECOMMENDATION &middot; READ 1:12 PM</div></div>')
    inner += ('<div style="padding: 22px 22px 0 22px;">'
              + branch(ICON_HALL, 'The corridor itself', 'walkable end to end in 15 min', 'crowded after two on Saturdays')
              + branch(ICON_TRAIN, 'Getting there', '24 min on the 7 from your stop', 'the last express back is 11:40')
              + branch(ICON_BOWL, 'One counter that closes early', 'the momo place shuts at 4', 'cash only, per its own listing')
              + '</div>')
    # scope legibility: what relationships apply here, drawn once, not as permanent pills
    inner += (f'<div style="padding: 28px 22px 0 22px;"><div class="shead"><span>WHAT THIS SCOPE CAN USE</span><span class="rule"></span></div>'
              '<div style="display: flex; flex-direction: column; gap: 0; margin-top: 6px;">'
              f'<div class="row" style="min-height: 44px;"><span style="width: 7px; height: 7px; border-radius: 4px; background: {INK}; flex: none;"></span><span style="font-size: 14px; flex: 1;">World truth &middot; hours, transit, the corridor</span></div>'
              f'<div class="row" style="min-height: 44px;"><span style="width: 7px; height: 7px; border-radius: 4px; border: 1px solid rgba(27,23,20,0.25); box-sizing: border-box; flex: none;"></span><span style="font-size: 14px; flex: 1; color: {MUTE};">Your saves &middot; none here</span></div>'
              f'<div class="row" style="min-height: 44px; border-bottom: 1px solid rgba(27,23,20,0.06);"><span style="width: 7px; height: 7px; border-radius: 4px; border: 1px solid rgba(27,23,20,0.25); box-sizing: border-box; flex: none;"></span><span style="font-size: 14px; flex: 1; color: {MUTE};">Notes shared with you &middot; none cover this place</span></div></div>'
              '<div class="fn" style="margin-top: 8px;">SAME RESULT SET AS THE MAP &middot; SCOPE CHANGES THE VIEW, NEVER THE FACTS</div></div>')
    inner += cont_rows([('Jackson Heights on the map', ''), ('Back to near you', '')])
    inner += coda('New to you, and honest about it.', 'NO HISTORY INVENTED &middot; NO FRIENDS PLACED HERE')
    return places_phone(inner, 1330)

B5_NOTES = notecol('B5 &middot; another neighborhood, with less of your history', [
    ('THE COLD ENTRANCE', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">No saves, no notes, no visits. The field leads with world truth stated as world truth (&ldquo;not a recommendation&rdquo;) and three branches that differ in access structure. It does not pad with a category grid, a mood prompt, or a &ldquo;popular here&rdquo; shelf.</div>'),
    ('SCOPE-CONTROL LEGIBILITY', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;">The relationships a scope can draw on are listed once, in place, as a short ledger &mdash; not as permanent pills. Here two of three are honestly empty. Changing scope from &ldquo;near you&rdquo; to Jackson Heights re-queried the same governed result set with a new context handle; it did not invent social access, and the map shows the same inventory as the list.</div>'),
    ('PROPOSED CONTRACT AMENDMENT (NAMED, NOT ADOPTED)', '<div style="font-size: 12.5px; line-height: 18px; color: #2C2622;"><b>Scope may expose a relationship dimension (&ldquo;with Theo&rdquo;, &ldquo;your saves&rdquo;) only when at least one grant or owner record covers a Place inside the current field.</b> Owner: the Places lane&rsquo;s scope/candidate-set contract, under the Contribution &amp; Consequence axes. Until ruled, the ledger above is drawn from existing rules only.</div>'),
])

# ───────────────────────────── B6 · how map, list, search, comparison and opening relate ─────────────────────────────
def b6():
    box = lambda t, s, x, y, w=250, accent=False: (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; background: {CARD if accent else "transparent"}; border: 1px solid rgba(27,23,20,{0.18 if accent else 0.12}); border-radius: 12px; padding: 12px 14px;">'
                                                   f'<div class="kick" style="color: {GOLDD if accent else MUTE};">{t}</div><div style="font-size: 12.5px; line-height: 18px; color: {INK2}; margin-top: 4px;">{s}</div></div>')
    inner = (f'<div style="width: 1352px; position: relative; height: 700px;">'
             f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">One result set, five ways to hold it</div>'
             f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 760px; margin-top: 6px;">Map, list, search, comparison and opening a place are transformations of one server-governed result set under one context handle. Changing the transformation changes what you see, never what exists. This is the existing candidate-set and scope contract, drawn; the one proposed amendment is on B5.</div>'
             + box('THE RESULT SET &middot; ONE CONTEXT HANDLE', 'Scope (near you / a named place / a question), interval, constraint, and the relationships this viewer may use. Server-governed. The handle is echoed back by every transformation so Back restores it exactly.', 526, 280, 300, accent=True)
             + box('MAP', 'The same inventory as pins. Pan does not re-query; a deliberate &ldquo;search here&rdquo; does, with a new handle. Camera is restored on Back.', 100, 120)
             + box('LIST (THE FIELD)', 'The same inventory as a lead + branches, each with one reason and one burden. Order is the compiler&rsquo;s (B1, B2, B5).', 1000, 120)
             + box('SEARCH / A QUESTION', 'Narrows the scope; the question becomes a constraint on the handle (B2). It never adds inventory that the scope excluded.', 100, 480)
             + box('COMPARISON (PATH)', 'Two or more exact identities from the set, related by a supported difference (B3, the accepted Place Path). Never generic similarity.', 1000, 480)
             + box('OPENING A PLACE (FOCUS)', 'Exits the set into the entity lane&rsquo;s canonical page with the handle as incoming context (C2). Back restores the transformation you left, at the same scroll or camera. Opening writes nothing.', 526, 500, 300)
             + f'<svg width="1352" height="700" viewBox="0 0 1352 700" fill="none" style="position: absolute; inset: 0; pointer-events: none;">'
               '<path d="M350 170 L526 300" stroke="#8A6628" stroke-width="1.5" stroke-dasharray="3 5"/><path d="M1000 170 L826 300" stroke="#8A6628" stroke-width="1.5" stroke-dasharray="3 5"/>'
               '<path d="M350 520 L526 380" stroke="#8A6628" stroke-width="1.5" stroke-dasharray="3 5"/><path d="M1000 520 L826 380" stroke="#8A6628" stroke-width="1.5" stroke-dasharray="3 5"/>'
               '<path d="M676 400 L676 500" stroke="#1B1714" stroke-width="1.8"/><path d="M670 492 L676 500 L682 492" stroke="#1B1714" stroke-width="1.8" fill="none"/>'
               '</svg>'
             + f'<div style="position: absolute; left: 0; top: 640px; width: 1352px;" class="fn">RULES THE DIAGRAM ENCODES &middot; SCOPE CHANGE &ne; FACT CHANGE &middot; NO TRANSFORMATION INVENTS SOCIAL ACCESS &middot; RELATIONSHIP SCOPES APPEAR ONLY WHERE A GRANT OR OWNER RECORD APPLIES (PROPOSED, B5) &middot; OPENING IS NOT SAVING &middot; BACK IS EXACT</div>'
             + '</div>')
    return inner

def write(name, ph, notes, h, w=1000):
    inner = f'<div style="width: 393px; flex: none;">{label(GREEN, "PROPOSAL", "HP value pass 09-04 &middot; not canon until ruled")}{ph}</div>{notes}'
    open(os.path.join(OUT, name + '.dc.html'), 'w').write(board(inner, w, h)); print('wrote', name)

write('HPB1OpenAfternoon', b1(), B1_NOTES, 1460)
write('HPB2BeforeDinner', b2(), B2_NOTES, 1460)
write('HPB3Curiosity', b3(), B3_NOTES, 1600)
write('HPB4FriendNote', b4(), B4_NOTES, 1650)
write('HPB5OtherNeighborhood', b5(), B5_NOTES, 1460)
open(os.path.join(OUT, 'HPB6Relation.dc.html'), 'w').write(board('<div style="display: flex; flex-direction: column; gap: 10px;">' + label(GREEN, 'PROPOSAL', 'HP value pass 09-04 &middot; the relation sheet') + b6() + '</div>', 1400, 800, pad='26px 24px 24px 24px', gap=0)); print('wrote HPB6Relation')
