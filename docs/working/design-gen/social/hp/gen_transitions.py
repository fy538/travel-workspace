import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_home import market_crown, PASSAGE_CH3, TIDE_SAT, rhythm_bars
OUT = os.path.join(os.path.dirname(__file__), 'boards'); os.makedirs(OUT, exist_ok=True)

def frame(title, inner, h=620, w=393):
    """A cropped phone slice: no tab bar, paper, fixed height, with a mono caption above."""
    return (f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 8px;">'
            f'<div class="kickm">{title}</div>'
            f'<div style="width: {w}px; height: {h}px; overflow: hidden; background: {PAPER}; border-radius: 12px; {SANS} color: {INK}; box-sizing: border-box; position: relative;">{inner}'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 40px; background: linear-gradient(to bottom, rgba(239,234,224,0), {PAPER});"></div></div></div>')

def arrow_col(label_txt):
    return (f'<div style="width: 92px; flex: none; display: flex; flex-direction: column; align-items: center; gap: 8px; padding-top: 300px;">'
            f'<svg width="40" height="16" viewBox="0 0 40 16" fill="none"><path d="M2 8 H34 M28 2 L34 8 L28 14" stroke="#8A6628" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<div class="kick" style="text-align: center; line-height: 14px;">{label_txt}</div></div>')

def spec(rows):
    out = '<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0 22px; margin-top: 26px; padding-top: 18px; border-top: 1px solid rgba(27,23,20,0.10);">'
    for k, v in rows:
        out += f'<div style="display: flex; flex-direction: column; gap: 6px;"><div class="kickm">{k}</div><div style="font-size: 12.5px; line-height: 18px; color: {INK2};">{v}</div></div>'
    return out + '</div>'

def head(num, title, sub):
    return (f'<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 22px;">{label(GREEN, "PROPOSAL", "HP value pass 09-04 &middot; transition " + num)}'
            f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">{title}</div>'
            f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 900px;">{sub}</div></div>')

def wrap(inner, h, w=1560):
    return HEAD + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; padding: 26px 32px 30px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">' + inner + '</div>' + TAIL

def reading_unit_compact(read=False):
    if read:
        return (f'<div style="padding: 44px 22px 0 22px;"><div class="shead"><span>ONE WAY THE WORLD CAN OPEN</span><span class="rule"></span></div>'
                f'<div class="row" style="margin-top: 8px; border-bottom: 1px solid rgba(27,23,20,0.06);"><span style="width: 7px; height: 7px; border-radius: 4px; border: 1.5px solid {GREEN}; box-sizing: border-box; flex: none;"></span><span style="font-size: 15px; flex: 1; color: {MUTE};">The flood line, ch. 3 &middot; read</span>{CHEV}</div></div>')
    return (f'<div style="padding: 44px 22px 0 22px;"><div class="shead"><span>ONE WAY THE WORLD CAN OPEN</span><span class="rule"></span></div><div style="height: 8px;"></div>'
            + unit_open('FROM YOUR READING &middot; THE HARBOR BOOK &middot; CH. 3', 'Low water at 2:40 puts the flood line under your coffee route', 'The gates the chapter describes are the ones on your walk.', plate='thumb')
            + TIDE_SAT + passage(PASSAGE_CH3[:1]) + '</div>')

# ───────────────────────────── C1 · contribution → reading → return ─────────────────────────────
def c1():
    f1 = frame('1 &middot; HOME, SATURDAY 8:50 &middot; THE UNIT IS ALREADY COMPLETE',
               anchor_row('NEW YORK &middot; SATURDAY', '8:50 AM') + orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two.', 26, 30)
               + f'<div style="margin: 22px 22px 0 22px; height: 120px; border-radius: 18px; background: {CARD}; box-shadow: 0 6px 18px rgba(27,23,20,0.10);"><div style="padding: 16px;"><div class="fn">THE MARKET CROWN, ABOVE &middot; NOT PART OF THIS TRANSITION</div></div></div>'
               + reading_unit_compact(), h=760)
    reader = (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{BACK}<div style="flex: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE HARBOR BOOK &middot; CH. 3</div><div style="font-size: 12.5px; color: {MUTE};">From Home &middot; 6 min &middot; your copy</div></div></div>'
              f'<div style="padding: 22px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 29px; letter-spacing: -0.2px;">The gates, and what they choose</div>'
              + passage(PASSAGE_CH3 + ['The chapter goes on to the pumps &mdash; the two grates at your crossing &mdash; and to the 1938 storm that sized them. Read on, or stop here; the boundary is already legible.'])
              + f'<div style="{SERIF} font-style: italic; font-size: 15px; line-height: 22px; color: {MUTE}; margin-top: 4px;">The book explains the mechanism; the tide table says when you can see it.</div>'
              + door('Keep this as a page') + '</div>')
    f2 = frame('2 &middot; THE READING &middot; EDITORIAL READER (CHAT LANE OWNS IT)', reader, h=760)
    f3 = frame('3 &middot; BACK &middot; HOME, SAME SCROLL, THE UNIT STEPS DOWN',
               anchor_row('NEW YORK &middot; SATURDAY', '9:04 AM') + orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two.', 26, 30)
               + f'<div style="margin: 22px 22px 0 22px; height: 120px; border-radius: 18px; background: {CARD}; box-shadow: 0 6px 18px rgba(27,23,20,0.10);"><div style="padding: 16px;"><div class="fn">THE MARKET CROWN &middot; UNCHANGED</div></div></div>'
               + reading_unit_compact(read=True) + f'<div style="padding: 0 22px;">{door("Walk it at low water")}</div>', h=760)
    inner = head('C1', 'Home contribution &rarr; substantive reading &rarr; return to Home',
                 'The unit on Home is complete on view (the passage is composed there). Opening it is optional depth, not the toll for the value. The reader is the Chat lane&rsquo;s editorial family; Home does not grow a second reader.')
    inner += f'<div style="display: flex; align-items: flex-start;">{f1}{arrow_col("TAP THE TITLE")}{f2}{arrow_col("BACK")}{f3}</div>'
    inner += spec([
        ('IMMEDIATE TAP RESPONSE', 'Push, from the unit. The unit&rsquo;s title and kicker persist as the reader&rsquo;s header so nothing jumps. No write, no &ldquo;opened&rdquo; state sent anywhere.'),
        ('DESTINATION', 'The editorial reader (Chat lane, board 17&ndash;20 family): the passage continued, the source line, one italic limit, and the &ldquo;Keep this as a page&rdquo; door. Owner: the Source (the book) &mdash; the reader is a composition over it.'),
        ('BACK', 'Pop to Home at the exact scroll. The unit steps down to one read row (hollow green mark) for this compile only; at the next compile it is absent (G3). The door to the walk survives because it is the practical branch, not the reading.'),
        ('LATER RE-ENTRY', 'The passage is findable in Life under the book (Time and Threads lenses), not on Home. If kept as a page, the kept composition appears in Life&rsquo;s kept drawer with its own identity.'),
        ('PERSISTED', 'Nothing by reading. Only an explicit Keep. Reading does not infer interest in harbors, tides, or walks.'),
    ])
    return wrap(inner, 1160)

# ───────────────────────────── C2 · possibility → Places → entity page → retained intent ─────────────────────────────
def entity_stub():
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{BACK}<div style="flex: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE MARKET</div><div style="font-size: 12.5px; color: {MUTE};">From Places &middot; this morning</div></div></div>'
            f'<div class="hatch" style="margin: 18px 22px 0 22px; height: 150px; border-radius: 12px; display: flex; align-items: flex-end; padding: 12px 14px; box-sizing: border-box;"><span class="fn" style="color: {GOLDD};">PHOTOGRAPH &middot; YOURS FROM THE 22ND, OR NOTHING</span></div>'
            f'<div style="padding: 16px 22px 0 22px; display: flex; flex-direction: column; gap: 6px;"><div class="kick">MARKET &middot; PRODUCE, BREAD, CHEESE &middot; SATURDAYS 8&ndash;1</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 29px;">The Saturday market</div>'
            f'<div style="display: flex; gap: 18px; margin-top: 4px;"><div><div class="fn">OPEN</div><div style="font-size: 15px; font-weight: 600;">until 1 today</div></div><div><div class="fn">BREAD</div><div style="font-size: 15px; font-weight: 600;">gone by ten &middot; Theo</div></div></div>'
            f'<div style="{SERIF} font-size: 15px; line-height: 22px; color: {INK2}; margin-top: 6px;">Forty-odd stalls on the square since 1998; the bread and cheese people are the ones that sell out<sup style="color: {GOLDD};">1</sup>. Theo&rsquo;s note says go by ten<sup style="color: {GOLDD};">T</sup>.</div>'
            f'<div style="display: flex; gap: 18px; margin-top: 10px;"><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Directions</span><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Keep this place</span><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Their site</span></div>'
            f'<div class="fn" style="margin-top: 12px;">ENTITY LANE&rsquo;S PAGE (BOARD 06) &middot; DRAWN AS A STUB &middot; NOT REDRAWN HERE</div></div>')

def c2():
    f1 = frame('1 &middot; HOME &middot; THE MARKET CROWN', anchor_row('NEW YORK &middot; SATURDAY', '8:50 AM') + orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two.', 26, 30) + market_crown(), h=700)
    focus = (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{BACK}<div style="flex: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE MARKET</div><div style="font-size: 12.5px; color: {MUTE};">Saturday &middot; 8:55 &middot; open until 1</div></div>{MAPI}</div>'
             f'<div class="fn" style="padding: 8px 22px 0 22px;">FROM HOME &middot; THIS MORNING &middot; THEO&rsquo;S NOTE RIDES ALONG</div>'
             f'<div style="margin: 14px 22px 0 22px; height: 110px; border-radius: 12px; background: repeating-linear-gradient(0deg, rgba(27,23,20,0.05) 0 1px, transparent 1px 26px), repeating-linear-gradient(90deg, rgba(27,23,20,0.05) 0 1px, transparent 1px 26px), {WASH};"></div>'
             f'<div style="padding: 24px 22px 0 22px;"><div class="shead" style="color: {GOLDD};"><span>THIS MORNING&rsquo;S READ</span><span class="rule"></span></div>'
             f'<div style="{SERIF} font-size: 18px; line-height: 25px; margin-top: 8px;">Go before half past nine. The stalls peak at ten; the bread is gone by then.</div>'
             + rhythm_bars([2, 4, 7, 10, 12, 9, 6, 4, 2, 1], (3, 4), 1) + '</div>'
             f'<div style="padding: 22px 22px 0 22px;"><div class="shead"><span>YOUR TRACE HERE</span><span class="rule"></span></div><div style="font-size: 14px; margin-top: 8px;">Three Saturdays this year.</div></div>')
    f2 = frame('2 &middot; PLACES &middot; FOCUS, WITH THE MORNING AS CONTEXT', focus, h=700)
    f3 = frame('3 &middot; THE PLACE ITSELF &middot; ENTITY PAGE (STUB)', entity_stub(), h=700)
    f4 = frame('4 &middot; AFTER &ldquo;KEEP THIS PLACE&rdquo; &middot; READBACK, THEN BACK', entity_stub().replace('<span style="font-size: 13px; font-weight: 500; color: #8A6628;">Keep this place</span>', f'<span style="font-size: 13px; font-weight: 500; color: {MUTE};">Kept</span>')
               + f'<div style="margin: 12px 22px 0 22px; display: flex; gap: 8px; align-items: center;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {GOLDD};">KEPT &middot; NO DATE, NO PLAN &middot; FINDABLE IN LIFE &middot; UNDO</span></div>', h=700)
    inner = head('C2', 'Home possibility &rarr; Places context &rarr; the place itself &rarr; an optional retained intent',
                 'Three doors, one identity. The market on Home, in the Places Focus, and on the entity page is the same Place; what changes is the incoming context, never the facts. Keeping is optional and writes exactly one thing.')
    inner += f'<div style="display: flex; align-items: flex-start;">{f1}{arrow_col("OPEN THE MARKET")}{f2}{arrow_col("TAP THE NAME")}{f3}{arrow_col("KEEP")}{f4}</div>'
    inner += spec([
        ('IMMEDIATE TAP RESPONSE', 'Crown &rarr; Focus: push with the envelope (origin Home unit, interval this morning, Theo&rsquo;s grant, no unresolved decision). Focus &rarr; entity page: push with the Focus handle. Keep: the verb turns to &ldquo;Kept&rdquo; in place; one readback line appears under it.'),
        ('DESTINATION', 'Focus is Places&rsquo; (B4). The entity page is the Entity lane&rsquo;s selected page (board 06: plate, kicker, the pair, short paragraphs with citations, text verbs) &mdash; shown as a stub, not redrawn. Theo&rsquo;s note appears there as a byline citation, not a second card.'),
        ('BACK', 'Entity &rarr; Focus &rarr; Home, each at the exact scroll. Home&rsquo;s crown is unchanged by the visit; if kept, the crown&rsquo;s footnote gains &ldquo;KEPT&rdquo; at the next compile and nothing else moves.'),
        ('LATER RE-ENTRY', 'From Life (Places lens: held Places) or from any future Home/Places unit about the market. The kept Place carries no date and no Plan; it is a saved place, not a planned visit (Life lane&rsquo;s distinction).'),
        ('PERSISTED', 'Only the Keep, as a Place relationship owned by the person. Opening any of the three pages writes nothing; returning from &ldquo;Their site&rdquo; marks nothing.'),
    ])
    return wrap(inner, 1160, w=1920)

# ───────────────────────────── C3 · a retained possibility, useful later, never an obligation ─────────────────────────────
def c3():
    keep = (f'<div style="display: flex; align-items: center; gap: 12px; padding: 24px 22px 0 22px;">{BACK}<div style="flex: 1;"><div style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE BOOKHALL</div><div style="font-size: 12.5px; color: {MUTE};">Saturday 3:40 &middot; open until 11</div></div></div>'
            f'<div class="hatch" style="margin: 18px 22px 0 22px; height: 120px; border-radius: 12px;"></div>'
            f'<div style="padding: 16px 22px 0 22px; display: flex; flex-direction: column; gap: 6px;"><div class="kick">BOOKSHOP &middot; READING ROOM UPSTAIRS &middot; UNTIL 11</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 29px;">The bookhall</div>'
            f'<div style="{SERIF} font-size: 15px; line-height: 22px; color: {INK2};">Quiet upstairs after seven; the ground floor is the shop.</div>'
            f'<div style="display: flex; gap: 18px; margin-top: 10px;"><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Directions</span><span style="font-size: 13px; font-weight: 500; color: {GOLDD};">Keep this place</span></div>'
            f'<div style="margin-top: 14px; padding: 12px 14px; background: {CARD}; border-radius: 12px; display: flex; flex-direction: column; gap: 8px;"><div class="fn" style="color: {GOLDD};">YOU TYPED, IN CHAT, FROM THIS PAGE</div>'
            f'<div style="{SERIF} font-size: 15px; line-height: 21px;">&ldquo;keep this for a free evening &mdash; don&rsquo;t plan around it&rdquo;</div>'
            f'<div style="display: flex; gap: 8px; align-items: center;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {GOLDD};">KEPT AS AN OPTION &middot; NO DATE &middot; NOTHING BUILT AROUND IT</span></div></div>'
            f'<div class="fn" style="margin-top: 10px;">INTENTION WITHOUT A NAMED PLAN &middot; A PROPOSAL OF THE COMPONENTS &amp; PLAN TASK, NOT A STORAGE MODEL</div></div>')
    f1 = frame('1 &middot; SATURDAY &middot; KEPT AS AN OPTION, IN THE PERSON&rsquo;S WORDS', keep, h=700)
    later = (anchor_row('NEW YORK &middot; THURSDAY', '6:20 PM') + orientation('Clear, mild, and nothing on tonight.', 'Two weeks on &middot; Dana&rsquo;s visit was Saturday.', 26, 30)
             + section('ONE WAY THE EVENING CAN OPEN', top=32)
             + '<div style="padding: 0 22px;">' + unit_open('YOU KEPT THIS FOR AN EVENING LIKE THIS', 'The bookhall &middot; quiet upstairs after seven, open until 11', '18 minutes from you. You said not to plan around it, so nothing is.', plate='thumb') + door('Open the bookhall') + '</div>'
             + f'<div style="padding: 26px 22px 0 22px;"><div class="fn">IT APPEARS BECAUSE THE EVENING IS OPEN AND THE PLACE IS OPEN &middot; IT WILL NOT ASK TWICE</div></div>')
    f2 = frame('2 &middot; TWO WEEKS LATER &middot; A FREE EVENING &middot; IT APPEARS AS A POSSIBILITY', later, h=700)
    ignored = (anchor_row('NEW YORK &middot; FRIDAY', '7:10 PM') + orientation('A warm Friday. Nothing is booked.', 'Nothing needs you tonight.', 26, 30)
               + f'<div style="padding: 32px 22px 0 22px;"><div class="fn">NO BOOKHALL UNIT &middot; NOT &ldquo;STILL KEPT&rdquo; &middot; NOT &ldquo;YOU DIDN&rsquo;T GO&rdquo;</div></div>'
               + coda('Nothing here needs an answer.', 'NOTHING NEEDS YOU TONIGHT')
               + f'<div style="margin: 30px 22px 0 22px; padding: 12px 14px; border-top: 1px solid rgba(27,23,20,0.10);"><div class="kickm">LIFE &middot; PLACES LENS &middot; HELD</div><div class="row" style="border-top: none;"><span style="width: 7px; height: 7px; border-radius: 4px; background: {GOLD};"></span><span style="font-size: 15px; flex: 1;">The bookhall &middot; <span style="color: {MUTE};">kept for a free evening</span></span>{CHEV}</div><div class="fn">QUIET, FINDABLE, RELEASABLE &middot; NO OVERDUE</div></div>')
    f3 = frame('3 &middot; IGNORED &middot; THE NEXT OPEN EVENING, AND WHERE IT RESTS', ignored, h=700)
    inner = head('C3', 'A retained possibility becomes useful later without becoming an obligation',
                 'The person keeps a place in their own words. It comes back once, when an evening and the place are both open, as a possibility &mdash; and when ignored it goes nowhere, creates nothing, and stays findable.')
    inner += f'<div style="display: flex; align-items: flex-start;">{f1}{arrow_col("TWO WEEKS")}{f2}{arrow_col("IGNORED")}{f3}</div>'
    inner += spec([
        ('IMMEDIATE TAP RESPONSE', 'Frame 1: the sentence is typed into Chat from the page with the place as context; readback appears in place. No naming wizard, no Plan created, no date asked.'),
        ('DESTINATION', 'Frame 2: the possibility is a Home horizon unit, uncarded, one door to the place. Frame 3: Life&rsquo;s Places lens holds it as a kept option (Life lane&rsquo;s anatomy, board 10 drawers).'),
        ('BACK', 'From the bookhall page back to the Home unit at its scroll. Ignoring is not an action; there is nothing to go back from.'),
        ('LATER RE-ENTRY', 'It may appear again on a later open evening (arbitration: only if no stronger current unit takes the seat); it never appears as overdue, and never twice in a week. Release from Life removes it everywhere.'),
        ('PERSISTED', 'One retained intention in the person&rsquo;s words, owned by them. Assumption flagged: &ldquo;intention without a named Plan&rdquo; is the Components &amp; Plan task&rsquo;s proposal; this board shows its Home/Places consequence only.'),
    ])
    return wrap(inner, 1160)

# ───────────────────────────── C4 · a shared perspective changes a possibility ─────────────────────────────
def c4():
    arrive = (anchor_row('NEW YORK &middot; TUESDAY', '8:12 PM') + f'<div style="padding: 22px 22px 0 22px;"><div class="shead"><span>SHARED WITH YOU</span><span class="rule"></span></div></div>'
              f'<div style="margin: 14px 22px 0 22px; background: {CARD}; border-radius: 12px; box-shadow: 0 1px 2px rgba(27,23,20,0.05); padding: 14px 16px; display: flex; gap: 12px; align-items: flex-start;">'
              f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; flex: none;">T</span>'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: 5px;"><div class="kickm">THEO &middot; A NOTE ABOUT THE MARKET</div><div style="{SERIF} font-size: 17px; line-height: 24px;">&ldquo;The bread stall sells out by ten &mdash; go early or don&rsquo;t bother.&rdquo;</div><div class="fn">AUDIENCE: YOU &middot; USE: YES &middot; RETAIN: UNTIL HE PULLS IT &middot; NO REPLY OWED</div></div></div>'
              f'<div style="padding: 14px 22px 0 22px;"><div class="fn">ONE BOUNDED PUSH, CONSUMED IN TWO SECONDS &middot; NO THREAD OPENED &middot; NOTHING TO ACCEPT</div></div>')
    f1 = frame('1 &middot; TUESDAY &middot; THE NOTE ARRIVES (CHAT&rsquo;S CARD, HOME&rsquo;S SEAM)', arrive, h=620)
    f2 = frame('2 &middot; SATURDAY &middot; THE POSSIBILITY, CHANGED AND ATTRIBUTED', anchor_row('NEW YORK &middot; SATURDAY', '8:50 AM') + orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two.', 26, 30) + market_crown(), h=620)
    crown_after = crown(PLAN, 'THIS MORNING &middot; MARKET UNTIL 1', 'Go to the market before eleven', 'The stalls peak at ten and thin out after.',
                        rhythm_bars([2, 4, 7, 10, 12, 9, 6, 4, 2, 1], (3, 4), 1)
                        + '<div style="display: flex; justify-content: space-between; margin-top: 2px;"><span class="fn" style="color: #8F877C;">8A</span><span style="font-family: JetBrains Mono, monospace; font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: #8A6628;">PEAK 9&#8211;11</span><span class="fn" style="color: #8F877C;">1P</span></div>',
                        cta='Open the market', fn='RHYTHM FROM PAST SATURDAYS &middot; NOTHING SAVED OR PLANNED')
    f3 = frame('3 &middot; IF THEO WITHDRAWS &middot; THE SAME MORNING, RECOMPILED', anchor_row('NEW YORK &middot; SATURDAY', '8:50 AM') + orientation('Clear and cold. Nothing is booked.', 'Warming to 48&deg; by two.', 26, 30) + crown_after
               + f'<div style="padding: 14px 22px 0 22px;"><div class="fn">NO TRACE OF THE NOTE &middot; NO &ldquo;THEO REMOVED&rdquo; &middot; THE WINDOW REVERTS TO THE RHYTHM ALONE</div></div>', h=620)
    inner = head('C4', 'A shared perspective changes a possibility without requiring a group workspace',
                 'Theo&rsquo;s note is one bounded contribution under one grant. It changes the market possibility&rsquo;s timing on Home and Places, with his name on the change. There is no group, no thread, no reply debt, and withdrawal unwinds it cleanly.')
    inner += f'<div style="display: flex; align-items: flex-start;">{f1}{arrow_col("SATURDAY")}{f2}{arrow_col("WITHDRAWN")}{f3}</div>'
    inner += spec([
        ('IMMEDIATE TAP RESPONSE', 'Frame 1 is not a tap; it is a push line and Chat&rsquo;s attributed card (the existing Invitation/Decision/Brief family&rsquo;s note shape). Tapping the card opens the note&rsquo;s source with its grant ledger. Nothing to accept.'),
        ('DESTINATION', 'Frame 2: the Home crown (A1) and the Places Focus (B4) both compile the note into the window; the attribution line names him. The crown&rsquo;s CTA is the same as without the note.'),
        ('BACK', 'Not applicable to the seam; from the note&rsquo;s source, Back returns to wherever it was opened.'),
        ('LATER RE-ENTRY', 'The note lives in Life&rsquo;s People lens (viewer-relative) as long as the grant stands. It is never a &ldquo;Theo likes markets&rdquo; inference.'),
        ('PERSISTED', 'The contribution, with author, audience, use and retention axes; withdrawal recompiles Home, Places and Life without residue (frame 3). No group workspace, Occasion, or shared plan is created.'),
    ])
    return wrap(inner, 1080)

for name, fn, h in [('HPC1Reading', c1, 1160), ('HPC2Possibility', c2, 1160), ('HPC3Retained', c3, 1160), ('HPC4Shared', c4, 1080)]:
    open(os.path.join(OUT, name + '.dc.html'), 'w').write(fn()); print('wrote', name, h)
