#!/usr/bin/env python3
"""Board 13 · Scoped actions, interrupted drafts, requested work (2026-09-12 coverage assignment).
Writes '13 Scoped Actions, Drafts, Requested Work.dc.html' into the mirror dir given as argv[1].
Connects existing donors (90 J2c/J2e/J2g, 90 D5-D7, 08 P2/P10, 12 W1-W5, 11 I1b); nothing is wired.
Finite requested work is supported; continuing-service (following) terms stay PROPOSED."""
import sys, os
OUT = sys.argv[1]

def ph(label, body, sheet=None, fold=True, clock='9:41'):
    s = f'''<div class="phw">
          <div class="ph" data-screen-label="{label}">
            <div class="sb"><span>{clock}</span><span class="r">●●● ᯤ ▮</span></div>
            <div class="page">
{body}
            </div>'''
    if sheet:
        s += '\n            <div class="scrim"></div>\n            <div class="sheet">\n              <div class="hd"></div>\n              <div class="close" aria-label="Close">✕</div>\n' + sheet + '\n            </div>'
    s += '\n          </div>' + ('\n          <div class="fold"><span>↑852</span></div>' if fold and not sheet else '') + '\n        </div>'
    return s

def frame(x, y, n, title, sub, phone, ann_k, ann_ps, fx, tag=None):
    t = f'<span class="tag pp">{tag}</span> ' if tag else ''
    ps = '\n'.join(f'          <p>{p}</p>' for p in ann_ps)
    return f'''      <div class="frame" style="left: {x}px; top: {y}px;">
        <div class="flabel" data-drags-parent="1"><span class="n">{n}</span>{t}{title} <span class="s">{sub}</span></div>
        {phone}
        <div class="ann">
          <div class="k">{ann_k}</div>
{ps}
          <div class="fx">{fx}</div>
        </div>
      </div>'''

CHROME_PLAN = '<div class="chrome"><div class="lft"><div class="ctl">‹</div><div class="people"><div class="av a">BE</div><div class="av">YO</div></div></div><div class="capsule"><div class="slot">MAP</div><div class="slot">···</div></div></div>'
CHROME_WED  = '<div class="chrome"><div class="lft"><div class="ctl">‹</div><div class="people"><div class="av c">MA</div><div class="av b">SA</div></div></div><div class="capsule"><div class="slot">MAP</div></div></div>'
CHROME_HOME = '<div class="chrome"><div class="lft"></div><div class="capsule"><div class="slot">CHAT</div><div class="slot on">HOME</div></div></div>'
PILL = '<div class="pillwrap"><div class="pill">Ask Vesper<span class="mic">MIC</span></div></div>'

# Monday, June 22 — the Nara day (the 03/08/90 fixture)
def mon(rows, kick='Kyoto · Day 6 of 8', extra=''):
    return f'''              {CHROME_PLAN}
              <div class="kick">{kick}</div>
              <div class="titleRow"><div class="dayTitle">Monday, June 22</div><div class="door">Details →</div></div>
              <div class="section-k">Day 6 · Mon, Jun 22<div class="ln"></div></div>
{extra}              <div class="rows">
{rows}
              </div>
              {PILL}'''

ROW_TRAIN = '                <div class="row first"><div class="time">09:02</div><div><div class="ttl">Limited Express to Nara</div><div class="sup">Kintetsu from Kyoto · platform 8</div></div><div class="more">···</div></div>'
ROW_TODAI = '                <div class="row"><div class="time">10:15</div><div><div class="ttl">Tōdai-ji</div><div class="sup">The Great Buddha hall · <span class="who">with Ben</span></div></div><div class="more">···</div></div>'
ROW_KAISEKI = '                <div class="row"><div class="time exact">19:00</div><div><div class="ttl">Kaiseki counter — Gion</div><div class="sup">Back in Kyoto · <span class="src">reserved · 2 seats</span> · <span class="who">with Ben</span></div></div><div class="more">···</div></div>'
ROW_OPTION = '                <div class="row"><div class="time loose word">option</div><div><div class="ttl opt">Hōnen-in, if there’s time before dinner</div><div class="sup">Moss gate · usually quiet · 15 min walk from the ryokan</div></div><div class="more">···</div></div>'

def acts(items, bound=None):
    o = '\n'.join(
        f'''                <div class="o"><div><div class="ot">{t}</div><div class="os">{s}</div></div><div class="{k}">{mark}</div></div>'''
        for t, s, k, mark in items)
    b = f'\n              <div class="bound">{bound}</div>' if bound else ''
    return f'              <div class="opts">\n{o}\n              </div>{b}'

D_ = ('seehere', '')       # destination — drawn arrow
P_ = ('door2', '')         # a door toward a person / private
Q_ = ('door2 q', '')       # quiet

# ---------- S · what the row “…” opens ----------
S1 = ph('S1 A booked stop of yours', mon(ROW_TRAIN + '\n' + ROW_TODAI + '\n' + ROW_KAISEKI),
 sheet='''              <div class="priv"><span class="p">Private · only you and Vesper</span><span>19:00</span></div>
              <div class="tgt">Kaiseki counter — Gion</div>
              <div class="tgts">Reserved · 2 seats · from your confirmation · with Ben</div>
''' + acts([
   ('See the reservation', 'Your confirmation email, as it arrived', 'seehere', 'Open'),
   ('Open the place', 'The counter, how to get there, tonight’s hours', 'seehere', 'Open'),
   ('Ask about this', 'Private — only you and Vesper', 'door2', 'Ask'),
   ('Say something to Ben', 'He’s on this stop', 'door2', 'Say'),
   ('Move it', 'Yours to move — the booking is in your name', 'door2 q', 'Move'),
 ], 'Cancelling is on the restaurant’s page, not here. Nothing on this list changes the plan on its own.'))

S2 = ph('S2 An option, nothing booked', mon(ROW_TRAIN + '\n' + ROW_TODAI + '\n' + ROW_OPTION),
 sheet='''              <div class="priv"><span class="p">Private · only you and Vesper</span><span>Option</span></div>
              <div class="tgt">Hōnen-in</div>
              <div class="tgts">An option · nothing booked · nobody else is on it</div>
''' + acts([
   ('Open the place', 'The moss gate, hours, the walk from the ryokan', 'seehere', 'Open'),
   ('Ask about this', 'Private — only you and Vesper', 'door2', 'Ask'),
   ('Make it the afternoon', 'Gives it a time and a place in the day', 'door2', 'Keep'),
   ('Not this trip', 'Takes the option off Monday. Undo stays for a while', 'door2 q', 'Drop'),
 ], 'No reservation, so nothing to open; nobody else on it, so nobody to tell.'))

PHILLY = f'''              {CHROME_WED}
              <div class="kick">Saturday · Oct 10 · Philadelphia</div>
              <div class="titleRow"><div class="dayTitle">Jess and Omar’s wedding</div></div>
              <div class="thesis">The dinner at eight is yours to move; home on the 10:40 means leaving by 10:15.</div>
              <div class="gap"></div>
              <div class="rows">
                <div class="row first"><div class="time exact">3:30</div><div><div class="ttl">Ceremony · Old Pine Street</div><div class="sup">412 Pine St · <span class="src">from their schedule</span></div></div><div class="more">···</div></div>
                <div class="row"><div class="time exact">6:00</div><div><div class="ttl">Reception · The Bourse</div><div class="sup">Until eleven · <span class="src">from their schedule</span></div></div><div class="more">···</div></div>
                <div class="row"><div class="time exact">8:00</div><div><div class="ttl">Dinner at the Georgian room</div><div class="sup">Court St · <span class="who">you, Maya, Sam</span> · <span class="src">reserved · GR-3104 · 3</span></div></div><div class="more">···</div></div>
              </div>
              {PILL}'''
S3 = ph('S3 A stop from someone else’s schedule', PHILLY,
 sheet='''              <div class="priv"><span class="p">Private · only you and Vesper</span><span>3:30</span></div>
              <div class="tgt">Ceremony · Old Pine Street</div>
              <div class="tgts">From Jess and Omar’s schedule · kept beside your Saturday</div>
''' + acts([
   ('See their schedule', 'The PDF they sent, as it is', 'seehere', 'Open'),
   ('Ask about this', 'Private — only you and Vesper', 'door2', 'Ask'),
 ], 'Jess and Omar’s schedule isn’t yours to change, so nothing here moves it. Your dinner at eight is the row that’s yours.'))

# ---------- D · an interrupted draft ----------
D1 = ph('D1 Back, twelve minutes later', mon(ROW_TRAIN + '\n' + ROW_TODAI + '\n' + ROW_KAISEKI, kick='Kyoto · Day 6 of 8 · tomorrow'), clock='21:31',
 sheet='''              <div class="priv"><span class="p">Private · only you and Vesper</span><span>Tōdai-ji</span></div>
              <div class="ctx">Draft from 12 minutes ago</div>
              <div class="field filled"><span class="txt">ask Ben if ten works instead|</span><span class="mic">MIC</span><span class="go">↑</span></div>
              <div class="doors"><span class="door2 q">Discard draft</span><span class="door2">More room in Chat →</span></div>
              <div class="say">The stop, the day and the words are the ones you left. <span>Nothing was sent.</span></div>''')

D2 = ph('D2 Closed, not cancelled', mon(
  ROW_TRAIN + '\n' +
  '                <div class="row"><div class="time">10:15</div><div><div class="ttl">Tōdai-ji</div><div class="sup">The Great Buddha hall · <span class="who">with Ben</span> · <span class="src">a draft of yours · 12 min ago</span></div></div><div class="more">···</div></div>' + '\n' +
  ROW_KAISEKI, kick='Kyoto · Day 6 of 8 · tomorrow'), clock='21:33')

D3 = ph('D3 Back, and the outcome isn’t known yet', mon(
  ROW_TRAIN + '\n' + ROW_TODAI + '\n' + ROW_KAISEKI, kick='Kyoto · Day 6 of 8 · tomorrow',
  extra='''              <dc-import name="Notice" tone="unknown" title="Checking whether Isuien was added" body="Your request is still here. Monday is as you left it." secondary="Not now" hint-size="353px,104px"></dc-import>
              <div class="undoq">Try again once I know</div>
              <div class="gap"></div>
'''), clock='21:40')

# ---------- R · a finite requested check, end to end ----------
NARA_TOP = f'''              {CHROME_PLAN}
              <div class="kick">Kyoto · Day 6 of 8 · in Nara</div>
              <div class="titleRow"><div class="dayTitle">Monday, June 22</div><div class="door">Details →</div></div>'''
NARA_ROWS = '''              <div class="rows">
                <div class="row first"><div class="time">10:15</div><div><div class="ttl done">Tōdai-ji</div><div class="sup">The Great Buddha hall · <span class="who">with Ben</span></div></div><div class="more q">···</div></div>
                <div class="row"><div class="time exact">19:00</div><div><div class="ttl">Kaiseki counter — Gion</div><div class="sup">Back in Kyoto · <span class="src">reserved · 2 seats</span></div></div><div class="more">···</div></div>
              </div>'''

R1 = ph('R1 Asked, and what was accepted', NARA_TOP + '\n' + NARA_ROWS + '\n              ' + PILL, clock='4:10',
 sheet='''              <div class="priv"><span class="p">Private · only you and Vesper</span><span>Monday night</span></div>
              <div class="kept">“Find us two places near the park for Monday night, and tell me when you have them”</div>
              <div class="qp" style="margin-top:2px;">
                <div class="k">Asked 4:10 · ends when I answer</div>
                <div class="t">Two places to stay near Nara Park, Monday night</div>
                <div class="b"><b>This ends when I answer — it isn’t watching anything.</b> I’ll come back once with what I can see. Nothing on Monday changes until you choose, and the kaiseki counter stays as it is. If I can’t see their availability, I’ll say that instead.</div>
                <div class="chips" style="margin-top:6px;"><div class="chip quiet">Stop</div></div>
              </div>
              <div class="field"><span class="txt">Follow up, or change something…</span><span class="mic">MIC</span><span class="go">↑</span></div>''')

R2 = ph('R2 While she’s away', f'''              {CHROME_HOME}
              <div class="kick">Home · Monday · 6:38 pm</div>
              <div class="roottitle">Nara, then back to Kyoto.</div>
              <div class="qp pv">
                <div class="k">On the lock screen</div>
                <div class="t">Vesper · the two places you asked for</div>
                <div class="b">That is the whole of it. The names, the prices and the walk are inside the app.</div>
              </div>
              <div class="gap"></div>
              <div class="homecard">
                <div class="k">You asked at 4:10</div>
                <div class="t">Two places near the park, Monday night</div>
                <div class="b">Both are free on Monday and walkable from Tōdai-ji. Nothing is booked, and nothing on your Monday changed.</div>
                <div class="chips" style="margin-top:4px;"><div class="chip gold">See them</div></div>
              </div>
              <div class="gap-l"></div>
              <div class="quiet">Home owns this surface. Plans supplies the sentence, the destination and the truthful state — one delivery, not a second inbox.</div>''', fold=False, clock='6:38')

R3 = ph('R3 The answer, on the night it concerns', NARA_TOP + '''
              <div class="gap"></div>
              <div class="recent"><div class="receipt">Two places near the park for Monday night — nothing booked</div><div class="ago">6:38 PM</div></div>
              <div class="gap"></div>
              <div class="rows">
                <div class="row first"><div class="time loose word">night</div><div><div class="ttl opt">Monday night in Nara</div><div class="sup">Nara Kasugano Inn, ¥28,000 · Sanjo Street Hotel, ¥16,000 · <span class="src">see them</span></div></div><div class="more">···</div></div>
                <div class="row"><div class="time exact">19:00</div><div><div class="ttl conflict">Kaiseki counter — Gion</div><div class="sup">Back in Kyoto · <span class="src">reserved · 2 seats</span> · staying in Nara would miss it</div></div><div class="more">···</div></div>
              </div>
              <div class="gap"></div>
              <div class="quiet">Asked 4:10 · answered 6:38 · finished. I’m not looking any more.</div>
              ''' + PILL, clock='6:41')

R4 = ph('R4 A truthful ending instead', NARA_TOP + '''
              <div class="gap"></div>
              <dc-import name="Notice" tone="failed" title="I couldn’t see what’s free on Monday" body="Their site stopped answering at 5:02. Nothing on Monday changed, and I’ve stopped looking." primary="Try again" secondary="Not now" hint-size="353px,132px"></dc-import>
              <div class="gap"></div>
''' + NARA_ROWS + '\n              ' + PILL, clock='5:04')

R5 = ph('R5 No notification, and the night is gone', NARA_TOP.replace('in Nara', 'back in Kyoto') + '''
              <div class="gap"></div>
              <div class="recent"><div class="receipt ink">Two places near the park — you asked at 4:10</div><div class="ago">MONDAY</div></div>
              <div class="gap"></div>
              <div class="qp">
                <div class="k">The night you asked about isn’t in the plan any more</div>
                <div class="t">You’re back in Kyoto on Monday night</div>
                <div class="b">The answer is still here to read, and nothing was added. You found it by opening the plan — I never needed to notify you.</div>
                <div class="chips" style="margin-top:6px;"><div class="chip quiet">Read it</div><div class="chip quiet">Clear it</div></div>
              </div>
              <div class="gap"></div>
''' + NARA_ROWS + '\n              ' + PILL, clock='9:12')

frames = [
 frame(40,330,'S1','A BOOKED STOP OF YOURS · WHAT “···” OPENS','five entries: two destinations, two doors, one change',S1,
  'THE SET IS WHAT THIS STOP ACTUALLY SUPPORTS',
  ['The overflow is not a menu of everything the app can do. It is the destinations this stop has (the confirmation that made it, the place itself), the two doors the family already uses — private Ask, and saying something to the person who is on the stop — and, only where the stop is yours, the one change that is actually yours to make.',
   'Recognition-first: the doors read as the same private/shared pair everywhere else in the family (08 P2, 11 I1b), not as new verbs. <b>No edit machinery on every stop:</b> there is no field, no form and no second way to do what the day already does. Cancelling the table belongs to the restaurant, and the sheet says so rather than offering a button that cannot keep its promise.'],
  'Sept 12 item 1 · donors 08 P2 (private ask), 11 I1b (a message door), 03 B2 rows · sentences 2, 5'),
 frame(500,330,'S2','AN OPTION, NOTHING BOOKED','four entries: one destination, one door, two changes that are hers',S2,
  'A DIFFERENT STOP, A DIFFERENT SET — AND THE ABSENCES ARE LEGIBLE',
  ['Nothing was booked, so there is no source to open; nobody else is on it, so there is nobody to tell. Both absences are stated in one line rather than shown as greyed-out entries the person has to interpret.',
   'The two changes are the ones an option actually has: give it a time in the day, or take it off Monday. “Not this trip” names its own reversibility (Undo stays for a while) instead of asking for confirmation.'],
  'Sept 12 item 1 · 03 B2 option rows · sentence 3 (possibilities create no approval debt)'),
 frame(960,330,'S3','A STOP FROM SOMEONE ELSE’S SCHEDULE','two entries: read it, or ask privately',S3,
  'SCOPE IS WHAT IS MISSING, NOT A WARNING',
  ['The wedding rows came in as Ask and were kept on an explicit Keep (12 X1/X4). They are read, not owned: the set collapses to the source and a private question. There is no disabled “Move”, no “request a change”, and no explanation of policy — the list is simply short, and one sentence says where the person’s own authority is instead (the dinner at eight).',
   'This is the same rule as S1 and S2 applied to a stop whose owner is someone else; it introduces no new concept and no new state.'],
  'Sept 12 item 1 · 12 X1/X4 · C&amp;C §3.2 · sentence 6'),

 frame(40,1740,'D1','AN INTERRUPTED DRAFT COMES BACK WHOLE','back twelve minutes later · words, subject and day intact',D1,
  'WORDS, SUBJECT AND SELECTED DAY ALL SURVIVE',
  ['90 J2g already recovers the words. What this pass adds is the rest of the address: the sheet returns on <b>the same stop</b> (Tōdai-ji) and behind it the page is still <b>the same selected day</b> (Monday, June 22), so nothing has to be re-found before the sentence can be finished. The age is stated once, plainly.',
   '<b>Native dependency:</b> keyboard restoration, focus and caret position, and the back stack that produced this return cannot be verified by a static frame. Drawn here as the intended result; the native owners verify it.'],
  'Sept 12 item 2 · donor 90 J2g · sentence 4 · native-unverified'),
 frame(500,1740,'D2','CLOSE IS NOT CANCEL — AND THERE IS NO DRAFTS INBOX','the draft waits on the row it is about',D2,
  'WHERE A CLOSED DRAFT WAITS, STATED ON THE STOP',
  ['Dismissing the sheet neither sends nor discards. The unfinished sentence waits on the row it concerns, as one muted clause in the source position — “a draft of yours · 12 min ago” — which is also the way back into it. Tapping the row’s “···” shows the same scoped set as S1.',
   '<b>No new surface:</b> no drafts inbox, no badge, no list of unfinished things to manage. Discard stays explicit and lives only inside the sheet (D1), so nothing is thrown away by leaving. The plan itself never changed.'],
  'Sept 12 item 2 · donor 90 J2g · sentences 2, 4 · no new noun'),
 frame(960,1740,'D3','SAFE RETRY, UNSAFE RETRY, AND FREE NAVIGATION','returned while the outcome is still unknown',D3,
  'A RETRY THAT COULD DOUBLE A CHANGE IS HELD; ONE THAT CANNOT IS OFFERED',
  ['The unknown-outcome state is the shared Notice (90 J2e’s donor, now the package component). It says what is unresolved and that the request is still here; the day behind it is untouched and stays fully navigable — the person can leave, read Tuesday, or open anything else.',
   '<b>The distinction this pass names:</b> where a repeat could add the same thing twice, the retry is held until the outcome is known (“Try again once I know”). Where a repeat cannot — words that were never sent — Try again is offered immediately (R4, and 90 J2d). A pending spinner is not a watch, and an unknown outcome is never reported as “nothing changed”.'],
  'Sept 12 item 2 · donors 90 J2c/J2d/J2e · shared Notice · sentence 7'),

 frame(40,3150,'R1','A FINITE REQUEST, AND WHAT WAS ACCEPTED','asked in words · the acceptance states its own end',R1,
  'IT ENDS WHEN IT ANSWERS — THAT IS THE WHOLE SERVICE',
  ['The acceptance is one card: the subject, the end condition, what does not change, and Stop. The end condition is an <b>answer</b>, not a window — which is exactly what separates finite requested work from the continuing help on board 12, where a window exists because the work is waiting for the world to change.',
   '<b>Not a watch, not a current fact:</b> a current check (12 W1) answers now and says it is not watching; this one leaves and comes back once; following (12 W2–W5) keeps looking until a stated end. The three are different sentences, and only the first two are supported here.'],
  'Sept 12 item 3 · donor 08 P10 · contrast 12 W1/W2 · sentences 2, 7'),
 frame(500,3150,'R2','THE RESULT WHILE SHE IS AWAY','private preview · one useful sentence · one safe destination',R2,
  'ONE DELIVERY SEQUENCE, SHARED — NOT A THIRD DASHBOARD',
  ['The preview outside the app carries the fact that there is an answer and nothing more; the names, prices and walk are inside. The card in Home states the useful result, that nothing is booked and that nothing on Monday changed, with a single destination into the plan.',
   '<b>Ownership:</b> Home owns the away surface and its composition; Plans supplies the sentence, the destination and the truthful state. You &amp; Trust owns the global controls over whether this arrives at all. Three owners, one sequence — no second inbox and no Plans notification centre.'],
  'Sept 12 item 5 · shared §23.3 delivery · notification contract · Home 08c'),
 frame(960,3150,'R3','THE ANSWER LANDS ON THE NIGHT IT CONCERNS','two places · nothing booked · the request closes itself',R3,
  'A RESULT IS A ROW AND A RECEIPT, NOT A REPORT',
  ['The answer attaches to the night it is about, as an ordinary row with the two names and the one door that opens them. The receipt states what came back and that nothing was booked. The consequence she would not otherwise see — staying in Nara would miss the kaiseki counter she has reserved — is named on the row that owns it, in the same form 08 P10 uses.',
   '<b>The ending is said once:</b> “Asked 4:10 · answered 6:38 · finished. I’m not looking any more.” Nothing lingers, nothing has to be dismissed, and no service was created by asking.'],
  'Sept 12 items 3–4 · donors 08 P10, 90 D5 · sentences 1, 4'),
 frame(1420,3150,'R4','THE TRUTHFUL FAILURE','what failed, when, what didn’t change, and that it stopped',R4,
  'A FAILURE IS AN ENDING, NOT A SILENCE',
  ['The shared Notice carries the four things a person needs: what could not be seen, when it stopped being visible (5:02), that nothing on Monday changed, and that the looking has ended. Retry is safe here because nothing was written, so it is offered rather than held (D3’s rule).',
   '<b>Not drawn, deliberately:</b> a spinner that never resolves, a silent expiry, or a “still trying” that quietly becomes a watch. If it cannot finish, it says so and stops.'],
  'Sept 12 items 3–4 · donor 90 J2d · shared Notice · sentence 7'),
 frame(1880,3150,'R5','FOUND WITHOUT A NOTIFICATION, AFTER THE NIGHT WENT AWAY','in-app access · a target that no longer exists',R5,
  'THREE DELIVERY EDGES, ONE PAGE',
  ['<b>No push:</b> she never allowed notifications, so the result simply waits in the plan, found by opening it. The same page is the fallback when permission is denied or revoked — nothing is lost for refusing.',
   '<b>The target is gone:</b> Monday night in Nara is no longer in the plan. The answer neither re-adds the night nor disappears without a word: it is still readable, it says nothing was added, and it can be cleared. <b>Stale, not wrong:</b> the receipt keeps the time it was asked, so its age is legible rather than implied to be current.'],
  'Sept 12 item 5 · shared §23.3 stale/denied/in-app · donor 90 D7 · sentence 4'),
]

panel = '''      <div class="panel" style="left: 2400px; top: 330px; width: 920px;">
        <div class="k">HANDBACK · SEPTEMBER 12 COVERAGE · DONORS · MISSING DETAILS NOW DEFINED · BOUNDARIES · NATIVE DEPENDENCIES</div>
        <div class="row2"><span class="rk">The assignment</span><span>Scoped row actions (S1–S3), interrupted drafts (D1–D3), requested-work delivery and truthful endings (R1–R5). Nothing here is an operations dashboard: no status board, no queue, no drafts inbox, no notification centre. The readable arrangement, the seven sentences and the September 11 adoption are unchanged; no 0.4.1 migration was needed.</span></div>
        <div class="row2"><span class="rk">Donors reused, not reinvented</span><span><b>90 J2g</b> recovered draft → D1/D2. <b>90 J2c/J2d/J2e</b> pending, failed and unknown → D3 and R4, now as the shared <span class="m">Notice</span>. <b>90 D5/D7</b> provider return and stale alternative → R3/R5. <b>08 P2</b> private ask and <b>11 I1b</b> the message door → the two doors in every S sheet. <b>08 P10</b> options with a named conflict → R3. <b>12 W1/W2</b> current check and following → the contrast R1 is defined against. <b>03 B2</b> rows and gutter → every frame.</span></div>
        <div class="row2"><span class="rk">Missing details now defined</span><span>(1) What “···” opens, per stop kind, with absences stated rather than greyed out. (2) Where a closed draft waits — on the row it concerns, with discard only inside the sheet. (3) The acceptance sentence for finite work, whose end condition is an answer. (4) The closing sentence that ends it once. (5) The stale-target ending, where the answer survives but adds nothing. (6) Safe versus unsafe retry, stated as a rule rather than per screen.</span></div>
        <div class="row2"><span class="rk">Finite work vs continuing service</span><span><b>Supported and drawn here:</b> a current check that answers now and says it is not watching (12 W1); finite requested work that leaves, comes back once and closes (R1–R5). <b>Still proposed, not adopted by this board:</b> continuing help with a window, hear-once, coverage loss and Stop (12 W2–W5). Board 12 already draws scope, expiry and coverage loss; this board does not invent following again, and no frame here creates an ongoing service. Neither a current fact nor a pending state adopts a watch.</span></div>
        <div class="row2"><span class="rk">12 W, reconciled</span><span>W1 is the current-check end of this family and needs no change. W2–W5 keep their proposed status and their own decision gate; where they are supported, their ending and Stop are findable in the same places this board uses — the acceptance card and the row the work concerns. The distinction is stated in customer words on R1 (“this ends when I answer — it isn’t watching anything”), not in a policy paragraph.</span></div>
        <div class="row2"><span class="rk">Delivery, shared</span><span>One sequence across Home, Plans and You &amp; Trust: useful result or meaningful change while away, private preview, one safe destination into the current arrangement, in-app access without push, denied permission, and a stale or deleted target. Home owns the away surface; You &amp; Trust owns the global inspect/stop controls; Plans supplies the sentence, the destination and the truthful state. Reuse the notification contract rather than a Plans-local rule.</span></div>
        <div class="row2"><span class="rk">Native dependencies</span><span>Keyboard restoration, focus and caret, back stack, scroll position, larger text and screen-reader order — D1’s return and every sheet depend on them and static frames cannot verify any of it. Independent participant changes during an interruption (someone else edits the same stop while a draft is open) are drawn only as the rule that Undo never erases another person’s change (90 J3d); the reconciliation itself is a native and engine question.</span></div>
        <div class="row2"><span class="rk">Shared-package note</span><span>The scoped-action list uses the local sheet list construction; the package has no list-of-actions row with a destination marker, a scoped note and a 44px target. Reported as a candidate variant alongside the September 11 list on 07 — not built locally as a competing component, and not urgent: one consumer. <b>Measured on this board:</b> the shared Notice’s own actions render 36px tall (D3, R4), below the 44px minimum every Plans control holds; the component owns that height, so it is reported rather than overridden here.</span></div>
        <div class="row2"><span class="rk">Not commissioned</span><span>Booking execution, payment or expense surfaces, a permissions centre, a drafts or notification inbox, general scheduling, and any adoption of the following terms. No policy is changed by this board; Ask/Bring stays with Contribution &amp; Consequence, guest access and continuing-service scope keep their own gates.</span></div>
        <div class="row2"><span class="rk">Evidence</span><span>Drawn and illustrated; nothing is wired. Board 92 exercises none of these sequences. All people, places, times, prices and availability are synthetic fixtures. Native-unverified; participant-unverified. <b>Drawn / selected / implemented / verified are different things:</b> everything here is drawn, the donors it reuses are selected, none of it is implemented or verified.</span></div>
      </div>'''

HEAD = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="./support.js"></script>
  </head>
  <body>
    <x-dc>
      <helmet data-dc-atomics>
        <meta name="design_doc_mode" content="canvas" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap" />
        <link rel="stylesheet" href="./kit/plans.css" />
        <style>
          .x { min-height: 4650px; }
          .jlab { position: absolute; font-family: var(--mono); font-size: 11px; font-weight: 700; letter-spacing: 1.2px; color: var(--planning-deep); }
          .sheet .opts .o .seehere, .sheet .opts .o .door2 { font-family: var(--mono); font-size: calc(10.5px * var(--ts)); letter-spacing: 1px; text-transform: uppercase; min-height: 0; }
          .sheet .opts .o .seehere { color: var(--gold-deep); }
          .sheet .opts .o { min-height: 52px; }
          .sheet .tgts { margin-top: -2px; }
          .sheet .ctx { margin-top: 2px; }
        </style>
      </helmet>

      <div class="board-h" style="width: 1400px;">
        <div class="warn">EXPLORATION · NOT CANON · NOT PRODUCTION · SEPTEMBER 12 COVERAGE ASSIGNMENT · ALL PEOPLE, PLACES, TIMES, PRICES AND AVAILABILITY ARE SYNTHETIC FIXTURES · CONTINUING-SERVICE TERMS REMAIN PROPOSED · NOTHING IS WIRED</div>
        <div class="id">13 · SCOPED ACTIONS, INTERRUPTED DRAFTS, REQUESTED WORK · WHAT “···” OPENS (S1–S3) · DRAFTS THROUGH INTERRUPTION (D1–D3) · A FINITE REQUEST END TO END (R1–R5) · 2026-09-12</div>
        <h1>Finish the interaction family: what a stop’s actions are, what survives an interruption, and how asked-for work ends.</h1>
        <div class="lede">Three unfinished details, drawn from the family that already exists rather than from a new surface. <b>Scoped actions:</b> the row’s “···” opens exactly what that stop supports — its destinations, the private and shared doors the family already uses, and only the changes that are actually the person’s to make; a stop from someone else’s schedule simply has a shorter list. <b>Interrupted drafts:</b> the words, the stop and the selected day all come back together, a closed sheet is not a cancelled one, and the unfinished sentence waits on the row it concerns instead of in an inbox. <b>Requested work:</b> a finite request states that it ends when it answers, delivers one useful sentence and one safe destination while she is away, lands on the night it concerns, closes itself — and, when it cannot finish, says what failed, when, what did not change, and that it has stopped. Continuing help keeps its separate, still-proposed decision.</div>
      </div>

      <div class="jlab" style="left: 40px; top: 300px;">WHAT “···” OPENS · THE SET IS THE STOP’S, NOT THE APP’S</div>
      <div class="jlab" style="left: 40px; top: 1710px;">A DRAFT THROUGH INTERRUPTION, DISMISSAL AND RETURN · CLOSE IS NOT CANCEL</div>
      <div class="jlab" style="left: 40px; top: 3120px;">A FINITE REQUESTED CHECK, END TO END · REQUEST → ACCEPTANCE → AWAY → RESULT OR TRUTHFUL FAILURE → THE CURRENT ARRANGEMENT</div>

FRAMES

PANEL

      <div class="x"></div>
    </x-dc>
    <script type="text/x-dc" data-dc-script data-props='{}'>
      class Component extends DCLogic {
        renderVals() { return {}; }
      }
    </script>
  </body>
</html>
'''
doc = HEAD.replace('FRAMES', '\n'.join(frames)).replace('PANEL', panel)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import vdl_adopt as V
doc = V.adopt(doc)
open(os.path.join(OUT, '13 Scoped Actions, Drafts, Requested Work.dc.html'), 'w').write(doc)
print('wrote board 13', len(doc), 'chars ·', doc.count('vdl-btn'), 'shared buttons ·', doc.count('vdl-door'), 'doors ·', doc.count('dc-import'), 'Notices')
