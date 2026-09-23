# -*- coding: utf-8 -*-
"""Sep 9 second-pass strategy alignment (handoff §0): selective application, softly-ahead vs timely,
the proposed continuity comparison, and repeated-copy reconciliation. Run: python3 refine_0909c.py <src> <out>"""
import re, sys, os
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def sub1(t, a, b, name=""):
    assert t.count(a) == 1, f"{name or a[:50]!r}: found {t.count(a)}"; return t.replace(a, b, 1)
def append_before_end(t, b):
    i = t.rfind('</div>\n</x-dc>'); assert i > 0; return t[:i] + b + t[i:]
TAG = re.compile(r'<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>', re.S)
def walk_end(s, start):
    d = 0; j = start
    while True:
        m = TAG.search(s, j); assert m
        if m.group(2).lower() in ('path','circle','rect','line','br','img','text'): j = m.end(); continue
        if not m.group(1) and not m.group(3).rstrip().endswith('/'): d += 1
        elif m.group(1):
            d -= 1
            if d == 0: return m.end()
        j = m.end()
CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ROOT393 = '<div style="width: 393px; background: var(--paper); color: var(--ink); font-family: var(--sans); box-sizing: border-box; display: flex; flex-direction: column;">'
t03 = load("03 - Open something in my life.dc.html")
i = t03.find('<div style="border-top:1px solid var(--hairline); background:var(--card); display:flex; padding:10px 22px 22px 22px; margin-top:26px;">')
TAB = t03[i:walk_end(t03, i)]
m0 = t03.find('SHARED RECORD &middot; SINCE 2019'); ms = t03.rfind('<div style="padding: 20px 22px 0 22px', 0, m0)
MAST = t03[ms:walk_end(t03, ms)]
def mast(k, n, r):
    m = sub1(MAST, 'SHARED RECORD &middot; SINCE 2019', k); m = sub1(m, '>Shared with Maya<', f'>{n}<')
    return sub1(m, 'Twelve shared episodes across six years.', r)
MARK = {'page':'M3.5 1.8 H11.5 V13.2 H3.5 Z M5.5 4.8 H9.5 M5.5 7.3 H9.5 M5.5 9.8 H8','coast':'M1.6 9.6 Q3.8 7.2 6 9.6 Q8.2 12 10.4 9.6 Q12.2 7.6 13.4 8.8 M4 5.6 Q6 3.6 8 5.6 Q10 7.6 12 5.6','fork':'M5 1.8 V6 M7.5 1.8 V6 M10 1.8 V6 M5 6 Q7.5 7.6 10 6 M7.5 6.8 V13.2','glass':'M4.4 1.8 H10.6 L9.8 6.4 Q9.4 8.6 7.5 8.6 Q5.6 8.6 5.2 6.4 Z M7.5 8.6 V12.4 M5.2 12.8 H9.8'}
def bar(k, meta='', top=34):
    m = f'<span class="barmeta" style="margin-left:auto;">{meta}</span>' if meta else ''
    return f'<div style="margin:{top}px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{k}</span>{m}</div>'
def orow(k, text, meta, quiet=False):
    op = ' opacity:0.62;' if quiet else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:44px; border-bottom:1px solid var(--hair-thin);{op}"><svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex:none; opacity:0.62;"><path d="{MARK[k]}" stroke="#1B1714" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="child" style="flex-grow:1;">{text}</span><span class="meta">{meta}</span>{CHEV}</div>')
def voice(t, top=14): return f'<div class="voice" style="margin:{top}px 22px 0 22px;">{t}</div>'
def meta_line(t): return f'<div style="margin:12px 22px 0 22px;"><span style="font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:0.7px; color:var(--mute); line-height:17px;">{t}</span></div>'
def screen(*p): return ROOT393 + ''.join(p) + '<div style="flex-grow:1;"></div>' + TAB + '</div>'
def ctx(where, lines, receipt=None):
    ls = ''.join(f'<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:{6 if i else 8}px;">{l}</div>' for i, l in enumerate(lines))
    r = f'<div style="margin-top:12px; padding-top:9px; border-top:1px solid var(--hair-thin); font-family:var(--mono); font-size:9.5px; letter-spacing:0.7px; text-transform:uppercase; color:var(--mute);">{receipt}</div>' if receipt else ''
    return f'<div style="width:393px; background:var(--card); border:1px solid var(--hairline); border-radius:12px; padding:16px 20px 18px 20px; box-sizing:border-box;"><div class="kicker" style="color:var(--mute);">{where}</div>{ls}{r}</div>'
def panel(cap, content, note='', phone=True, status=None, fid=''):
    n = f'<div class="cnote">{note}</div>' if note else ''
    st = '<span class="cpill rev">Review</span>' if status == 'rev' else ''
    f = f'<span class="ccap" style="color:var(--mute-light)">{fid}</span>' if fid else ''
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center"><span class="ccap">{cap}</span>{st}{f}</div>'
            f'<div class="{"cphone" if phone else "cctx"}">{content}</div>{n}</div>')
def section(k): return f'<div class="csec"><span class="ceye" style="color:var(--gold-deep)">{k}</span></div>'

# ============================================================ 06 · selective application (C04 Red Hook)
t = load("06 - Give once, get value back.dc.html")
redhook = screen(mast('PLACE HELD &middot; BROOKLYN &middot; SINCE 2025', 'Red Hook, and you', 'Two evenings, got there two ways.'),
    bar('THE RECORD', '2 EVENINGS', top=26),
    orow('coast', 'June &middot; over on the ferry, back on foot', 'JUN 14'),
    orow('fork', 'April, in the rain &middot; drove both ways', 'APR 6'),
    bar('WHAT YOU SAID'),
    orow('page', '&ldquo;The ferry is the good part &mdash; it just stops early.&rdquo;', 'JUN 14'),
    voice('Twice is not a habit; the record says how you got there, not what you like.'),
    bar('THE SOURCES'), meta_line('2 EPISODES &middot; 1 NOTE &middot; LIVE TIMES ARE PLACES&rsquo;'))
t = append_before_end(t, section('Context that changes the help &mdash; and context deliberately unused')
    + '<div class="crow">'
    + panel('What the record actually holds', redhook,
        note='Two supported evenings with materially different access, plus one line she wrote. That is the whole donor &mdash; no affinity, no visit count as a verdict (fixture v0.2 C04).', fid='06.5')
    + panel('Saturday, with it', ctx('CHAT &middot; SAT 4:10 PM', [
        '&ldquo;Meeting Priya in Red Hook at seven &mdash; how should I get there?&rdquo;',
        'Ferry, if you want the good part: last one back is 8:10 tonight, so the way home is the bridge or a car &mdash; what you did in April.'],
        receipt='Places checked tonight&rsquo;s sailings &middot; 4:02 pm'),
        note='What the context removed: re-explaining how she usually goes, and one bad outcome &mdash; arriving at a dock after the last boat. Life supplied the two evenings and her line; the live times are Places&rsquo;, not Life&rsquo;s judgement.', phone=False, fid='06.6')
    + panel('The same question, without it', ctx('CHAT &middot; SAT 4:10 PM &middot; NO ENTRUSTED CONTEXT', [
        '&ldquo;Meeting Priya in Red Hook at seven &mdash; how should I get there?&rdquo;',
        'Three ways: the ferry, the B61 bus, or a car. Check the last sailing if you take the ferry back.'],
        receipt='Still a good answer &middot; the checking is hers'),
        note='Not a failure &mdash; a good answer either way. The difference is one round of checking she now has to do herself, and one risk she has to think of. Personalized output does not have to win to be worth having.', phone=False, fid='06.7')
    + panel('Changed purpose &mdash; the same context, unused', ctx('CHAT &middot; TUE 9:20 AM', [
        '&ldquo;Picking up a table from Red Hook this morning &mdash; driving the van.&rdquo;',
        'Van&rsquo;s fine: Van Brunt has loading spots before eleven, and the Beard Street lot takes anything under twenty feet.'],
        receipt='The ferry evenings were not used'),
        note='The old context is real and stays unused: nothing about ferries or last boats belongs to a morning pickup, and the answer is good without it. Relevance is decided by the present job, not by what exists.', phone=False, fid='06.8')
    + '</div>')
save("06 - Give once, get value back.dc.html", t)

# ============================================================ P1 · softly ahead vs usefully timely
t = load("P1 - What I keep ahead of me.dc.html")
t = sub1(t, 'Maya mentioned the corner table. You kept her note in August.', 'Maya mentioned the corner table. The place is yours since August.', "P1 read")
t = sub1(t, 'Her note, readable as she wrote it; Friday&rsquo;s plan; the place itself. The place is kept by you; the words stay hers. &ldquo;No visits yet&rdquo; stays exactly true, and nothing asks you to go.',
         'Her note, readable as she wrote it; Friday&rsquo;s plan; the place itself. This is the kept-place-only case: the place is yours, the words stay hers and remain reachable while she shares them. The retained-note variant &mdash; where she also keeps a copy &mdash; is drawn on 07.7; the two are different and the manifest returns the difference. &ldquo;No visits yet&rdquo; stays exactly true, and nothing asks you to go.', "P1 lilia note")
t = append_before_end(t, section('Softly ahead, and the moment it becomes timely')
    + '<div class="crow">'
    + panel('Saturday, 5:40 &mdash; the evening is open', ctx('HOME &middot; SAT SEP 5', [
        'Alex&rsquo;s birthday finished early; nothing else is on tonight.',
        'The jazz you asked to keep in mind: two rooms nearby, sets at 7 and 9:30.'],
        receipt='You asked to keep this in mind &middot; Aug 30 &middot; Not tonight'),
        note='What made it timely is a condition Home already knows &mdash; the evening is open &mdash; not a scheduler. The intention held no watch, set no reminder and asked for nothing while it waited; the cue is one line and can be waved off without changing what is kept.', phone=False, fid='P1.5')
    + panel('The same Saturday, different circumstances', ctx('HOME &middot; SAT SEP 5 &middot; THE EVENING FILLED', [
        'Dinner ran long and the table moved to nine.',
        'Nothing about jazz appears &mdash; it stays where it was.'],
        receipt='No cue &middot; nothing dismissed, nothing expired'),
        note='Quiet non-use is the same design working: the kept intention is unchanged and still findable in AHEAD and in search. Silence here is not a missed reminder, and the record never records that it went unused.', phone=False, fid='P1.6')
    + '</div>'
    + '<div class="cn" style="max-width:900px;padding:6px 0 0 0"><b style="color:var(--ink)">Still proposed:</b> who owns a retained intention, and what expiry means for one, are the pre-Plan questions on the Components&amp;Plan docket &mdash; not settled by these two frames. Home decides elevation from a current condition; Life only keeps the thing findable. Entity 10 draws the same intention made at a place (Hortus, &ldquo;Saturday &middot; loosely&rdquo;) and is the sibling donor.</div>')
save("P1 - What I keep ahead of me.dc.html", t)

# ============================================================ 02 · the proposed continuity comparison
t = load("02 - An ordinary beginning.dc.html")
t = append_before_end(t, section('Proposed &mdash; what an optional agreement would change')
    + '<div class="cn" style="max-width:900px;padding:2px 0 6px 0"><b style="color:var(--ink)">Not adopted.</b> Optional conversational continuity is accepted product direction; its retention terms &mdash; what is kept, for how long, for which later uses &mdash; are pending with the history/use policy owner. Ask/T0 and current expiry remain in force; nothing below is drawn as per-turn saving, and neither branch creates a Life entry, infers an interest, or sends a notification.</div>'
    + '<div class="crow">'
    + panel('Weeks later &mdash; under the optional agreement', ctx('CHAT &middot; OCT 8', [
        '&ldquo;Is the Ladislaw business meant to be a love story or a political one?&rdquo;',
        'Both, and the book keeps refusing to choose. Since you were around Casaubon&rsquo;s will last time, this is the part where that inheritance starts steering it &mdash; still nothing past where you were.'],
        receipt='Nothing kept &middot; no entry made &middot; no interest recorded'),
        note='The improvement is narrow and private: it does not re-ask what she has read, and it keeps to where the conversation left her. Nothing enters Life, no preference is inferred from a question, and she is not told the system remembered.', phone=False, status='rev', fid='02.9')
    + panel('The same question, nothing retained', ctx('CHAT &middot; OCT 8 &middot; NO AGREEMENT', [
        '&ldquo;Is the Ladislaw business meant to be a love story or a political one?&rdquo;',
        'Both &mdash; it keeps refusing to choose. Say roughly where you are and I&rsquo;ll keep the answer behind it.'],
        receipt='Answered &middot; nothing kept'),
        note='The valid branch, and it must stay valid: a good answer, one small question, no debt. Whatever the policy decides, this is what Life looks like when nothing was retained &mdash; which is also every case today.', phone=False, fid='02.10')
    + '</div>')
save("02 - An ordinary beginning.dc.html", t)

# ============================================================ 07 · access / expiry / revocation
t = load("07 - The people in my life.dc.html")
old = '<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:6px;">Maya&rsquo;s note is hers, reachable while she shares it. Keeping the place does not keep her words, and her words do not become yours by being the reason you kept it.</div>'
new = ('<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:6px;">Maya&rsquo;s note is hers. Keeping the place does not keep her words, and her words do not become yours by being the reason you kept it.</div>'
       '<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:6px;">Three different things: you can <i>reach</i> it while she shares it; the share can <i>end</i> on its own date; she can <i>take it back</i>. A copy you kept survives the second and not the third.</div>')
t = sub1(t, old, new, "07.8 three terms")
t = sub1(t, 'The exact distinction the source route needs: an original still accessible through sharing, versus one deliberately retained. Placement, guest and retention agreements remain proposals with their own owners.',
         'The exact distinction the source route needs, in three non-interchangeable terms &mdash; access while shared, the share&rsquo;s own expiry, and revocation by its author &mdash; plus what each does to a copy the recipient kept. Returned to Social 08.2/08.3 and Entity 04/12.4. Placement, guest and retention agreements remain proposals with their own owners.', "07.8 note")
save("07 - The people in my life.dc.html", t)

# ============================================================ P2 · retire the corrected copies
t = load("P2 - Life changes without management.dc.html")
for a, b, n in [('A third of the way &mdash; no hurry', 'Your note: page 280, no hurry', 'P2 book'),
                ('An hour &middot; she kept her note about Vienna', 'She sent her note about Vienna after', 'P2 dana'),
                ('The old pair retired at 600 km &mdash; kept for the record', 'The old pair retired &mdash; kept, from your note', 'P2 shoes')]:
    c = t.count(a); assert c >= 1, f"{n}: 0"
    t = t.replace(a, b)
    print(f"  {n}: {c} replaced")
save("P2 - Life changes without management.dc.html", t)
print("done")
