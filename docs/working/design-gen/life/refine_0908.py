# -*- coding: utf-8 -*-
"""Sep 8 bounded refinement of the Life companion project (handoff §0).
Operates on the current export (Downloads/life/project): asserted edits for the
must-corrects, plus three new sequences (formation, ambiguous retrieval, the
captured day) composed from pieces already in the export. Run: python3 refine_0908.py <srcdir> <outdir>"""
import re, sys, os, html

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def sub1(t, a, b, name=""):
    assert t.count(a) == 1, f"{name or a[:60]!r}: found {t.count(a)}"
    return t.replace(a, b, 1)
def subn(t, a, b, n, name=""):
    assert t.count(a) == n, f"{name or a[:60]!r}: found {t.count(a)} (expected {n})"
    return t.replace(a, b)

CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ROOT393 = '<div style="width: 393px; background: var(--paper); color: var(--ink); font-family: var(--sans); box-sizing: border-box; display: flex; flex-direction: column;">'
def between(t, a, b, start=0):
    i = t.find(a, start); assert i >= 0, a[:50]; j = t.find(b, i); assert j > i, b[:50]; return i, j

# ---------- pieces harvested from the export ----------
t03 = load("03 - Open something in my life.dc.html")
i = t03.find('<div style="border-top:1px solid var(--hairline); background:var(--card); display:flex; padding:10px 22px 22px 22px; margin-top:26px;">')
TAB = t03[i:t03.find('</div>\n  </div>', i) + len('</div>\n  </div>')] if False else t03[i:t03.find('>Life</span></div>', i) + len('>Life</span></div>')] + '\n  </div>'
assert TAB.count('>Home<') == 1 and TAB.count('>Life<') == 1
m0 = t03.find('SHARED RECORD &middot; SINCE 2019'); ms = t03.rfind('<div style="padding: 20px 22px 0 22px', 0, m0)
me = t03.find('Twelve shared episodes across six years.', ms); me = t03.find('</div>\n  </div>', me) + len('</div>\n  </div>')
MAST = t03[ms:me]
def mast(kicker, name, read):
    m = sub1(MAST, 'SHARED RECORD &middot; SINCE 2019', kicker, "mast kicker")
    m = sub1(m, '>Shared with Maya<', f'>{name}<', "mast name")
    return sub1(m, 'Twelve shared episodes across six years.', read, "mast read")
t05 = load("05 - Find it again.dc.html")
qs = t05.find('<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:12px;">')
qe = t05.find('<div style="margin:24px 22px 0 22px; border-top:1px solid var(--hairline)', qs)
QUERY = t05[qs:qe]; assert QUERY.count('>pasta<') == 1
def query(q): return QUERY.replace('>pasta<', f'>{q}<', 1)
rs = t05.find('<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:54px; border-bottom:1px solid var(--hair-thin);">')
RESULT = t05[rs:t05.find('</svg>\n  </div>', rs) + len('</svg>\n  </div>')]
assert 'question' in RESULT
def result(title, sub, meta, mark_path=None):
    r = RESULT.replace('The <span style="background:rgba(176,133,58,0.18);">pasta</span> question', title) if 'background:rgba(176,133,58,0.18)' in RESULT else RESULT
    a = r.find('<span style="font-family:var(--serif); font-size:15.5px'); a2 = r.find('>', a) + 1; b = r.find('<span class="rsub">', a2); assert a > 0 and b > a2
    r = r[:a2] + title + '</span>\n      ' + r[b:]
    r = re.sub(r'(<span class="rsub">).*?(</span>)', lambda m: m.group(1) + sub + m.group(2), r, count=1, flags=re.S)
    r = re.sub(r'(<span class="meta">).*?(</span>)', lambda m: m.group(1) + meta + m.group(2), r, count=1, flags=re.S)
    if mark_path: r = re.sub(r'<path d="[^"]*"', f'<path d="{mark_path}"', r, count=1)
    return r
ASK = t05[t05.find('<div style="margin:26px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:14px; display:flex; flex-direction:column; gap:8px;">'):]
ASK = ASK[:ASK.find('</div>\n  </div>') + len('</div>\n  </div>')]
assert 'Ask Vesper' in ASK
def ask(q): return re.sub(r'(<span class="door">)Ask Vesper[^<]*(</span>)', lambda m: m.group(1) + f'Ask Vesper about {q}' + m.group(2), ASK, count=1)
t02 = load("02 - An ordinary beginning.dc.html")
ws = t02.find(ROOT393); we = t02.find('>THIS WEEK<', ws); we = t02.rfind('<div style="margin:22px 22px 0 22px', 0, we)
WEEK_HEAD = t02[ws + len(ROOT393):we]; assert 'A week, held lightly.' in WEEK_HEAD

MARK = {'fork': 'M5 1.8 V6 M7.5 1.8 V6 M10 1.8 V6 M5 6 Q7.5 7.6 10 6 M7.5 6.8 V13.2', 'glass': 'M4.4 1.8 H10.6 L9.8 6.4 Q9.4 8.6 7.5 8.6 Q5.6 8.6 5.2 6.4 Z M7.5 8.6 V12.4 M5.2 12.8 H9.8',
        'page': 'M3.5 1.8 H11.5 V13.2 H3.5 Z M5.5 4.8 H9.5 M5.5 7.3 H9.5 M5.5 9.8 H8', 'coast': 'M1.6 9.6 Q3.8 7.2 6 9.6 Q8.2 12 10.4 9.6 Q12.2 7.6 13.4 8.8 M4 5.6 Q6 3.6 8 5.6 Q10 7.6 12 5.6',
        'table': 'M2 5.5 H13 M4 5.5 V12.5 M11 5.5 V12.5 M5 2.5 H10', 'photo': 'M2.5 3 H12.5 V12 H2.5 Z M2.5 9.5 L6 6.5 L9 9 L11 7.5 L12.5 9', 'receipt': 'M3.5 1.8 H11.5 V13.2 L9.5 12 L7.5 13.2 L5.5 12 L3.5 13.2 Z M5.5 5 H9.5 M5.5 7.5 H9.5'}
def bar(k, meta='', top=34):
    m = f'<span class="barmeta" style="margin-left:auto;">{meta}</span>' if meta else ''
    return f'<div style="margin:{top}px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{k}</span>{m}</div>'
def erow(title, sub, meta=None, quiet=False, meta_style=''):
    op = ' opacity:0.62;' if quiet else ''
    m = f'<span class="meta"{f" style=\"{meta_style}\"" if meta_style else ""}>{meta}</span>' if meta else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:60px; border-bottom:1px solid var(--hair-thin);{op}"><div style="flex-grow:1; display:flex; flex-direction:column; gap:2px;"><div style="display:flex; align-items:baseline; gap:8px;"><span class="rtitle">{title}</span></div><span class="rsub">{sub}</span></div>{m}{CHEV}</div>')
def orow(k, text, meta, quiet=False, chev=True):
    op = ' opacity:0.62;' if quiet else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:44px; border-bottom:1px solid var(--hair-thin);{op}"><svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex:none; opacity:0.62;"><path d="{MARK[k]}" stroke="#1B1714" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="child" style="flex-grow:1;">{text}</span><span class="meta">{meta}</span>{CHEV if chev else ""}</div>')
def voice(t, top=14): return f'<div class="voice" style="margin:{top}px 22px 0 22px;">{t}</div>'
def door(t, top=12): return f'<div style="margin:{top}px 22px 0 22px; display:flex; align-items:center;"><span class="door">{t} &rarr;</span></div>'
def meta_line(t): return f'<div style="margin:12px 22px 0 22px;"><span style="font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:0.7px; color:var(--mute); line-height:17px;">{t}</span></div>'
def note_line(t): return f'<div style="margin:12px 22px 0 22px; font-family:var(--sans); font-size:13px; line-height:18px; color:var(--mute);">{t}</div>'
def screen(*parts): return ROOT393 + ''.join(parts) + '<div style="flex-grow:1;"></div>' + TAB + '</div>'
def ctx(where, lines, receipt=None):
    ls = ''.join(f'<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:{6 if i else 8}px;">{l}</div>' for i, l in enumerate(lines))
    r = f'<div style="margin-top:12px; padding-top:9px; border-top:1px solid var(--hair-thin); font-family:var(--mono); font-size:9.5px; letter-spacing:0.7px; text-transform:uppercase; color:var(--mute);">{receipt}</div>' if receipt else ''
    return f'<div style="width:393px; background:var(--card); border:1px solid var(--hairline); border-radius:12px; padding:16px 20px 18px 20px; box-sizing:border-box;"><div class="kicker" style="color:var(--mute);">{where}</div>{ls}{r}</div>'
def panel(cap, content, note='', phone=True, status=None, fid=''):
    n = f'<div class="cnote">{note}</div>' if note else ''
    st = {'rev': '<span class="cpill rev">Review</span>', 'cur': '<span class="cpill cur">Current</span>'}.get(status, '')
    fidtxt = f'<span class="ccap" style="color:var(--mute-light)">{fid}</span>' if fid else ''
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center"><span class="ccap">{cap}</span>{st}{fidtxt}</div>'
            f'<div class="{"cphone" if phone else "cctx"}">{content}</div>{n}</div>')
def section(k): return f'<div class="csec"><span class="ceye" style="color:var(--gold-deep)">{k}</span></div>'
def append_before_end(t, block):
    i = t.rfind('</div>\n</x-dc>'); assert i > 0
    return t[:i] + block + t[i:]

# ============================================================ 02 · formation + a week with nothing kept
t = t02
t = sub1(t, 'A third of the way &mdash; no hurry', 'Your note: page 280, no hurry', "02 middlemarch")
t = sub1(t, 'An hour &middot; she kept her note about Vienna', 'She sent her note about Vienna after', "02 dana")
t = sub1(t, 'The old pair retired at 600 km &mdash; kept for the record', 'The old pair retired &mdash; kept, from your note', "02 shoes")
t = subn(t, 'a book, dumplings, a call, a retired pair of shoes', 'a book, dumplings, a call, a retired pair of shoes &mdash; each there because the person said so', 1, "02 para")
empty_head = WEEK_HEAD.replace('A week, held lightly.', 'A quiet week.').replace('SEP 1 &mdash; 7 &middot; 6 THINGS KEPT', 'SEP 8 &mdash; 14 &middot; NOTHING KEPT')
assert empty_head != WEEK_HEAD
empty_week = (ROOT393 + empty_head + bar('LAST WEEK', 'SEP 1 &mdash; 7', top=22)
    + erow('Alex&rsquo;s birthday, the morning after', 'Sunday spilled into pancakes &mdash; worth keeping', meta='SUN')
    + erow('Middlemarch, evenings', 'Your note: page 280, no hurry', meta='ONGOING')
    + erow('The bakery on Court St', 'Back after the summer break &mdash; third in line', meta='TUE')
    + '<div style="margin:26px 22px 0 22px; border-top:1px solid var(--hairline); border-bottom:1px solid var(--hairline); display:flex; align-items:center; min-height:56px;"><span class="door">The full record, by time &rarr;</span><span class="barmeta" style="margin-left:auto;">SEP 1 &mdash; 14</span></div>'
    + '<div style="flex-grow:1;"></div>' + TAB + '</div>')
formation = (section('How a week forms &mdash; and a week that doesn&rsquo;t')
    + '<div class="crow">'
    + panel('Tuesday &middot; a question, answered', ctx('CHAT &middot; TUE SEP 2 &middot; 8:10 AM', ['&ldquo;Is the bakery on Court St open again?&rdquo;', 'Yes &mdash; reopened Sep 1, seven to three, closed Mondays.'], receipt='Answered &middot; nothing kept'),
            note='The immediate job, done. An answer leaves no residue in Life; a question is not a record.', phone=False, fid='02.4')
    + panel('Tuesday &middot; kept, because you said so', ctx('CHAT &middot; TUE SEP 2 &middot; 8:55 AM', ['&ldquo;Went. Third in line. Keep that.&rdquo;', 'Kept.'], receipt='Kept &middot; your words &middot; Tue Sep 2 &middot; Undo'),
            note='The only residue is the sentence the person chose to keep. That is the bakery row on the week above &mdash; and the whole of how it got there.', phone=False, fid='02.5')
    + panel('The week after &middot; nothing kept', empty_week, note='A quiet week is a valid week: no section for it, no prompt, no gap to fill. Last week&rsquo;s record is simply first.', fid='02.6')
    + '</div>')
t = append_before_end(t, formation)
save("02 - An ordinary beginning.dc.html", t)

# ============================================================ 04 · custody copy
t = load("04 - My original things.dc.html")
t = sub1(t, 'EVERYTHING KEPT &middot; ALL OF IT, YOURS', 'EVERYTHING KEPT &middot; YOURS, AND WHAT OTHERS SHARED WITH YOU', "04 kicker")
save("04 - My original things.dc.html", t)

# ============================================================ 05 · no-result language + ambiguous retrieval
t = t05
t = sub1(t, 'Nothing in the record reaches Lisbon &mdash; no Portugal travel, no bar by that name.', 'Nothing kept mentions a jazz bar in Lisbon &mdash; no ticket, photo, note, or plan does.', "05 noresult")
t = sub1(t, 'The no-result names what the record holds and does not, and offers one wider door that keeps your question. Nothing is made up.', 'The no-result speaks only about what is kept, and offers one wider door that keeps your question.', "05 noresult note")
similar = (ROOT393 + query('dinner at ours') + bar('FOUND IN SEVEN YEARS', '3 RESULTS', top=24) + bar('EVENINGS', '3', top=22)
    + result('Dinner at <span style="background:rgba(176,133,58,0.18);">ours</span>', 'Sat Aug 29 &middot; Maya and Alex &middot; the table ran late', 'AUG 29', MARK['fork'])
    + result('A night at <span style="background:rgba(176,133,58,0.18);">ours</span>', 'Jul 12 &middot; nine people &middot; the long table', 'JUL 12', MARK['table'])
    + result('The long Tuesday', 'Mar 3 &middot; Fort Greene &middot; two of you, in', 'MAR 3', MARK['fork'])
    + voice('Three evenings match. Who was there and when tells them apart.', top=18) + ask('dinner at ours')
    + '<div style="flex-grow:1;"></div>' + TAB + '</div>')
corner = (ROOT393 + query('the place with the corner table') + bar('FOUND IN SEVEN YEARS', '2 RESULTS', top=24) + bar('KEPT PLACES', '1', top=22)
    + result('Lilia', 'Kept from Maya&rsquo;s note &middot; &ldquo;ask for the <span style="background:rgba(176,133,58,0.18);">corner table</span>&rdquo;', 'AUG 30', MARK['coast'])
    + bar('NOTES', '1', top=30)
    + result('Her note &middot; the pasta night', 'From Maya &middot; in Shared with Maya', 'AUG 30', MARK['page'])
    + voice('The cue was hers, not the place&rsquo;s &mdash; the match came through her words.', top=18) + ask('the corner table')
    + '<div style="flex-grow:1;"></div>' + TAB + '</div>')
miss = (ROOT393 + query('the wine from the July table') + bar('FOUND IN SEVEN YEARS', '0 EXACT &middot; 1 NEAR', top=24)
    + note_line('Nothing kept names the wine from July 12 &mdash; the table photograph and the reservation don&rsquo;t say.')
    + bar('NEAR', '1', top=30)
    + result('Alex&rsquo;s receipt &middot; the bottle, named', 'From Aug 29, not July &middot; in Dinner at ours', 'AUG 29', MARK['receipt'])
    + ask('the wine from July 12')
    + '<div style="flex-grow:1;"></div>' + TAB + '</div>')
amb = (section('When the cue is imperfect')
    + '<div class="crow">'
    + panel('Three similar evenings', similar, note='Supported candidates, told apart by who and when &mdash; the target is one tap, the others stay doors. No chooser, no taxonomy.', fid='05.5')
    + panel('A cue that belongs to a note', corner, note='&ldquo;The corner table&rdquo; is Maya&rsquo;s phrase, so the place is found through her note. The note itself is the second door.', fid='05.6')
    + panel('A partial-record miss', miss, note='What is kept cannot answer; the nearest supported thing is offered with its date so it is not mistaken for the answer. The question survives on the wider door.', fid='05.7')
    + '</div>')
t = append_before_end(t, amb)
save("05 - Find it again.dc.html", t)

# ============================================================ 06 · the Return per fixture C05
t = load("06 - Give once, get value back.dc.html")
t = sub1(t, 'One mechanism, three plates', 'For cacio e pepe, &ldquo;creamy&rdquo; is partly a stability problem', "06 title")
t = sub1(t, 'Both Rome plates finished the way the Sorrento one did. With the source you read since, the emulsion you noticed in one kitchen now holds across three &mdash; the technique, not the place.',
           'Starch concentration and temperature change how the cheese proteins clump and how the sauce holds. That is a mechanism, not a verdict on any kitchen &mdash; it says nothing about why all three plates tasted as they did. If you want to see it, one at-home comparison with a single variable would.', "06 sub")
t = sub1(t, 'THREE PLATES &middot; AUG 17&ndash;25 &middot; AND THE SOURCE YOU SAVED', 'FROM THE SOURCE YOU SAVED &middot; YOUR THREE PLATES ARE THE OCCASION, NOT THE PROOF', "06 meta")
t = sub1(t, 'See the three plates', 'See the source', "06 door")
t = sub1(t, 'After Rome adds two more plates and a saved read, the record returns what one photo could not support: it is the technique, not the kitchen.',
           'After Rome and a saved read, the record returns a bounded mechanism &mdash; why &ldquo;creamy&rdquo; is partly about stability &mdash; and one optional way to see it for yourself. It does not claim to know what any kitchen did.', "06 para")
t = sub1(t, 'What is new versus the Aug 17 answer: two more plates and a saved read. One photo supported a guess about one kitchen; three plates and the source support a claim about the technique. That increment is the Return.',
           'What is new versus the Aug 17 answer: a supported mechanism from the saved source (starch, temperature, protein stability) and a transferable one-variable test &mdash; not a repeat of the emulsion guess, and not certainty about the kitchens. Fixture C05.', "06 note")
save("06 - Give once, get value back.dc.html", t)

# ============================================================ 07 · each viewer's permitted originals
t = load("07 - The people in my life.dc.html")
t = sub1(t, '>THE THREE OF YOU</span>', '>WHAT THE THREE OF YOU CAN SEE</span>', "07 held meta")
t = sub1(t, '>THEIRS</span>', '>THEIRS &middot; SHARED TO THE TABLE</span>', "07 added meta")
t = sub1(t, 'What each person added to the same night and what it gave you: Maya&rsquo;s photograph fills the hour your camera missed; Alex&rsquo;s receipt names the bottle. Your own line stays yours alone.',
           'Your view of the night: the originals shared to the table (Maya&rsquo;s photograph fills the hour your camera missed; Alex&rsquo;s receipt names the bottle) plus your own line, which only you see. Maya&rsquo;s and Alex&rsquo;s pages hold the same shared originals and their own accounts &mdash; never yours.', "07 dinner note")
t = sub1(t, 'The note is gone; nothing paraphrases it. The dinners, her photograph, and everything held in common are exactly as they were.',
           'On reopening, the record says once what left; nothing paraphrases it. The dinners, her photograph, and everything held in common are exactly as they were. The People root at rest carries no announcement &mdash; the explanation lives where the missing thing would have been.', "07 withdraw note")
save("07 - The people in my life.dc.html", t)

# ============================================================ P3 · a captured day, later (Review)
t = load("P3 - Something I deliberately saved.dc.html")
capture_rows = (bar('AS HOME SHOWED IT &middot; 8:40 THIS MORNING', 'A READING, NOT THE PLAN', top=26)
    + orow('coast', '31&deg; by two &middot; the shade after', 'TODAY')
    + orow('table', 'Nothing after six &middot; the evening is open', 'TODAY')
    + orow('coast', 'The boat tomorrow &middot; 11:20', 'AS OF 8:40'))
captured = screen(mast('DAY &middot; AUG 18 2026 &middot; IN THE COAST &middot; NICE &rarr; ROME', 'Wednesday, August 18', 'Sorrento, day three.'),
    capture_rows,
    bar('SINCE THEN', 'THE PLAN IS THE AUTHORITY'),
    orow('coast', 'The boat moved to 12:40 &middot; changed 3:10 pm', 'IN THE PLAN'),
    door('Open the current plan', top=10),
    voice('Ask about today uses the plan as it is now, not this morning&rsquo;s reading.'),
    bar('THE RECORD OF THE DAY', 'SO FAR'),
    orow('photo', 'The market, the stairs &middot; four photographs', '10:15&ndash;11:40'),
    orow('fork', 'Lunch &middot; the counter by the harbour', '1:05'))
disconnected = screen(mast('DAY &middot; AUG 18 2026 &middot; IN THE COAST &middot; NICE &rarr; ROME', 'Wednesday, August 18', 'Sorrento, day three.'),
    '<div style="margin:22px 22px 0 22px; padding:8px 11px; border:1px dashed var(--hairline); border-radius:8px;"><span class="meta" style="white-space:normal; line-height:15px; display:block;">NO CONNECTION &middot; 9:15 PM &middot; WHAT FOLLOWS IS WHAT THE PHONE HOLDS</span></div>',
    bar('YOUR ORIGINALS', 'READABLE'),
    orow('photo', 'The market, the stairs &middot; four photographs', '10:15&ndash;11:40'),
    orow('receipt', 'Tomorrow&rsquo;s ferry &middot; the ticket, as issued', 'SOR&rarr;CAPRI'),
    bar('THE PLAN', 'LAST KNOWN &middot; 3:10 PM'),
    orow('coast', 'The boat &middot; 12:40', 'AS OF 3:10', quiet=True),
    note_line('Whether it has changed since can&rsquo;t be checked now.'),
    bar('THIS MORNING&rsquo;S READING', 'AS OF 8:40', top=26),
    orow('table', 'Nothing after six &middot; the evening is open', 'AS OF 8:40', quiet=True))
cap = (section('A captured day, later &mdash; reconciling Home 08c with the plan')
    + '<div class="cn" style="max-width:900px;padding:2px 0 6px 0"><b style="color:var(--ink)">Decision:</b> adopt the three-part reading &mdash; what Home showed (captured, dated), what the plan says now (the authority, one door), and what the phone holds when disconnected (originals readable, shared state last-known, freshness withheld)? <b style="color:var(--gold-deep)">Recommended:</b> adopt; Home 08c relabels its strip as a reading, the Plan lane owns the continuation, custody and retention unchanged.</div>'
    + '<div class="crow">'
    + panel('The day page &middot; captured, then changed', captured, note='Home 08c sends &ldquo;Today, as it stands&rdquo; here. The capture keeps its time; the plan&rsquo;s later change is a separate section with one door to the plan itself. Ask never operates on the 8:40 reading.', status='rev', fid='P3.4')
    + panel('The same page &middot; disconnected return', disconnected, note='Originals read; the last-known plan state carries its time; freshness is withheld rather than guessed. No cached material is hidden and no shared state is promised current.', status='rev', fid='P3.5')
    + '</div>')
t = append_before_end(t, cap)
save("P3 - Something I deliberately saved.dc.html", t)

for n in ["00 - Start here.dc.html", "01 - My life, four ways.dc.html", "03 - Open something in my life.dc.html", "03b - Inside a record.dc.html", "P1 - What I keep ahead of me.dc.html", "P2 - Life changes without management.dc.html", "P4 - A map inside a record.dc.html", "R0 - Reference.dc.html"]:
    pass  # untouched
print("done")
