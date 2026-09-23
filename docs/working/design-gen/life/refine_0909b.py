# -*- coding: utf-8 -*-
"""Sep 9 second pass (handoff §0 'fresh six-project review'): continuation, retrieval reason,
source route, and the Home-stack navigation correction. Run: python3 refine_0909b.py <src> <out>"""
import re, sys, os
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def sub1(t, a, b, name=""):
    assert t.count(a) == 1, f"{name or a[:60]!r}: found {t.count(a)}"; return t.replace(a, b, 1)
def append_before_end(t, block):
    i = t.rfind('</div>\n</x-dc>'); assert i > 0; return t[:i] + block + t[i:]
TAG = re.compile(r'<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>', re.S)
def walk_end(s, start):
    depth = 0; j = start
    while True:
        m = TAG.search(s, j); assert m
        nm = m.group(2).lower()
        if nm in ('path','circle','rect','line','br','img','text'): j = m.end(); continue
        if not m.group(1) and not m.group(3).rstrip().endswith('/'): depth += 1
        elif m.group(1):
            depth -= 1
            if depth == 0: return m.end()
        j = m.end()

CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ROOT393 = '<div style="width: 393px; background: var(--paper); color: var(--ink); font-family: var(--sans); box-sizing: border-box; display: flex; flex-direction: column;">'
t03 = load("03 - Open something in my life.dc.html")
i = t03.find('<div style="border-top:1px solid var(--hairline); background:var(--card); display:flex; padding:10px 22px 22px 22px; margin-top:26px;">')
TAB = t03[i:walk_end(t03, i)]
assert TAB.count('>Home<') == 1 and TAB.count('font-weight:600;">Life<') == 1
def tab_active(name):
    """Move the active state (ink icon + 600 weight) to another tab."""
    t = TAB.replace('<span style="font-size:10px; font-weight:600;">Life</span>', '<span style="font-size:10px; font-weight:500; color:var(--mute);">Life</span>')
    t = t.replace(f'<span style="font-size:10px; font-weight:500; color:var(--mute);">{name}</span>', f'<span style="font-size:10px; font-weight:600;">{name}</span>', 1)
    # icon strokes: Life's ink strokes back to mute, the named tab's mute strokes to ink
    li = t.find('font-weight:500; color:var(--mute);">Life<'); ls = t.rfind('<svg', 0, li)
    t = t[:ls] + t[ls:li].replace('#1B1714', '#6E6862') + t[li:]
    ni = t.find(f'font-weight:600;">{name}<'); ns = t.rfind('<svg', 0, ni)
    t = t[:ns] + t[ns:ni].replace('#6E6862', '#1B1714') + t[ni:]
    return t
m0 = t03.find('SHARED RECORD &middot; SINCE 2019'); ms = t03.rfind('<div style="padding: 20px 22px 0 22px', 0, m0)
MAST = t03[ms:walk_end(t03, ms)]
def mast(kicker, name, read):
    m = sub1(MAST, 'SHARED RECORD &middot; SINCE 2019', kicker, "mast kicker")
    m = sub1(m, '>Shared with Maya<', f'>{name}<', "mast name")
    return sub1(m, 'Twelve shared episodes across six years.', read, "mast read")
MARK = {'page': 'M3.5 1.8 H11.5 V13.2 H3.5 Z M5.5 4.8 H9.5 M5.5 7.3 H9.5 M5.5 9.8 H8', 'plane': 'M1.8 8.6 L13.2 3.4 L9.8 8.2 L11.4 12 L9.6 12.4 L7.4 9.2 L3.6 10.4 Z',
        'book': 'M2.5 2.5 H7 Q7.5 2.5 7.5 3 V12.5 Q7 12 2.5 12 Z M12.5 2.5 H8 Q7.5 2.5 7.5 3 V12.5 Q8 12 12.5 12 Z', 'coast': 'M1.6 9.6 Q3.8 7.2 6 9.6 Q8.2 12 10.4 9.6 Q12.2 7.6 13.4 8.8 M4 5.6 Q6 3.6 8 5.6 Q10 7.6 12 5.6'}
def bar(k, meta='', top=34):
    m = f'<span class="barmeta" style="margin-left:auto;">{meta}</span>' if meta else ''
    return f'<div style="margin:{top}px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{k}</span>{m}</div>'
def orow(k, text, meta, quiet=False, chev=True):
    op = ' opacity:0.62;' if quiet else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:44px; border-bottom:1px solid var(--hair-thin);{op}"><svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex:none; opacity:0.62;"><path d="{MARK[k]}" stroke="#1B1714" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="child" style="flex-grow:1;">{text}</span><span class="meta">{meta}</span>{CHEV if chev else ""}</div>')
def voice(t, top=14): return f'<div class="voice" style="margin:{top}px 22px 0 22px;">{t}</div>'
def door(t, top=12): return f'<div style="margin:{top}px 22px 0 22px; display:flex; align-items:center;"><span class="door">{t} &rarr;</span></div>'
def meta_line(t): return f'<div style="margin:12px 22px 0 22px;"><span style="font-family:var(--mono); font-size:10px; font-weight:500; letter-spacing:0.7px; color:var(--mute); line-height:17px;">{t}</span></div>'
def note_line(t): return f'<div style="margin:12px 22px 0 22px; font-family:var(--sans); font-size:13px; line-height:18px; color:var(--mute);">{t}</div>'
def quote(text, meta):
    return (f'<div style="margin:12px 22px 0 22px;"><div style="font-family:var(--serif); font-size:17px; line-height:24px; font-style:italic; color:var(--ink);">&ldquo;{text}&rdquo;</div>'
            f'<div class="meta" style="padding-top:6px;">{meta}</div></div>')
def screen(*parts, tab='Life'): return ROOT393 + ''.join(parts) + '<div style="flex-grow:1;"></div>' + (TAB if tab == 'Life' else tab_active(tab)) + '</div>'
def ctx(where, lines, receipt=None):
    ls = ''.join(f'<div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:{6 if i else 8}px;">{l}</div>' for i, l in enumerate(lines))
    r = f'<div style="margin-top:12px; padding-top:9px; border-top:1px solid var(--hair-thin); font-family:var(--mono); font-size:9.5px; letter-spacing:0.7px; text-transform:uppercase; color:var(--mute);">{receipt}</div>' if receipt else ''
    return f'<div style="width:393px; background:var(--card); border:1px solid var(--hairline); border-radius:12px; padding:16px 20px 18px 20px; box-sizing:border-box;"><div class="kicker" style="color:var(--mute);">{where}</div>{ls}{r}</div>'
def panel(cap, content, note='', phone=True, status=None, fid=''):
    n = f'<div class="cnote">{note}</div>' if note else ''
    st = {'rev': '<span class="cpill rev">Review</span>'}.get(status, '')
    f = f'<span class="ccap" style="color:var(--mute-light)">{fid}</span>' if fid else ''
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center"><span class="ccap">{cap}</span>{st}{f}</div>'
            f'<div class="{"cphone" if phone else "cctx"}">{content}</div>{n}</div>')
def section(k): return f'<div class="csec"><span class="ceye" style="color:var(--gold-deep)">{k}</span></div>'

# ============================================================ 02 · one ongoing interest, later
t = load("02 - An ordinary beginning.dc.html")
book_page = screen(mast('KEPT &middot; SINCE AUG 12', 'Middlemarch, evenings', 'Two notes, in your words.'),
    bar('WHAT YOU&rsquo;VE SAID', '2 NOTES', top=26),
    orow('page', '&ldquo;Started tonight. Slow, in a good way.&rdquo;', 'AUG 12'),
    orow('page', '&ldquo;Page 280, no hurry.&rdquo;', 'SEP 2'),
    voice('That is all the record knows about it.'),
    bar('THE SOURCES'), meta_line('2 NOTES &middot; KEPT VERBATIM'))
t = append_before_end(t, section('One ongoing interest, later')
    + '<div class="crow">'
    + panel('Three weeks on &middot; a question about the book', ctx('CHAT &middot; TUE SEP 24', [
        '&ldquo;Who is Casaubon to Dorothea again? I keep losing the thread.&rdquo;',
        'Her husband &mdash; she married him early, against her sister&rsquo;s judgement. Will Ladislaw is his young cousin, which is why the will matters later. Kept to before page 280, where your last note left off; say the word if you&rsquo;re past it.'],
        receipt='Answered &middot; nothing new kept'),
        note='Better help now, not a resumed setup: the answer is shaped by what was entrusted (her own note said page 280) so it does not run ahead of her, and it invites a correction instead of assuming progress. Nothing was logged to make this work.', phone=False, fid='02.7')
    + panel('The book, in Life', book_page,
        note='Two notes and nothing else &mdash; no percentage, no streak, no &ldquo;finish it&rdquo;, no place that needs updating. An ongoing interest is a thing you have said things about, not a project with a state.', fid='02.8')
    + '</div>')
save("02 - An ordinary beginning.dc.html", t)

# ============================================================ 05 · the reason you came
t = load("05 - Find it again.dc.html")
t03b = load("03b - Inside a record.dc.html")
fi = t03b.find('FERRY &middot; ALILAURO'); fs = t03b.rfind(ROOT393, 0, fi)
FERRY = t03b[fs:walk_end(t03b, fs)]
assert FERRY.startswith(ROOT393) and 'WHERE IT LIVES' in FERRY
happened = screen(mast('CHAPTER &middot; AUG 27&ndash;28 2026 &middot; IN NICE &rarr; ROME', 'Rome, and the broken flight home', 'Two cancellations, then Chicago.'),
    bar('WHAT HAPPENED', 'IN ORDER', top=26),
    orow('plane', 'FCO &rarr; JFK &middot; cancelled at the gate', 'AUG 27'),
    orow('page', 'Rebooked &middot; the second one cancelled too', 'AUG 27'),
    orow('plane', 'Out through Chicago, the last seat', 'AUG 28'),
    note_line('When you landed was never established &mdash; nothing kept says.'),
    meta_line('THE DRAWER, PHOTOGRAPHS AND SOURCES ARE FURTHER DOWN'))
t = append_before_end(t, section('The reason you came')
    + '<div class="crow">'
    + panel('Asked: what happened when the flight was cancelled', happened,
        note='The question wants the account, so the account is the page &mdash; in order, with the one thing the record cannot say. No drawer, no source count, no chronological inventory first.', fid='05.8')
    + panel('Asked: the Sorrento&ndash;Capri ferry ticket', FERRY,
        note='The question names an object, so the object opens &mdash; no journey, chapter or dossier detour. Its chain sits below for orientation, and Back returns to the query.', fid='05.9')
    + '</div>')
save("05 - Find it again.dc.html", t)

# ============================================================ 07 · the note's own reader
t = load("07 - The people in my life.dc.html")
reader = screen(mast('A NOTE FROM MAYA &middot; SUNDAY', 'The Paris note', 'Sent to you after Saturday&rsquo;s dinner.'),
    quote('Paris was the same heat. We gave up on the afternoons and stayed by the water until it cooled down &mdash; you two would have liked the river after eight.', 'HERS &middot; CITY-LEVEL &middot; REACHABLE WHILE SHE SHARES IT'),
    bar('WHAT YOU CAN DO', top=30),
    door('Write back'), door('Keep a copy', top=10), door('Ask Vesper about this', top=10),
    note_line('Opening it keeps nothing. You can find it again for as long as she shares it; a copy is yours to reread until she takes the note back.'))
t = append_before_end(t, section('Her note, opened &mdash; three independent choices')
    + '<div class="crow">'
    + panel('The note&rsquo;s own reader', reader,
        note='Reply, Keep and Ask are three separate choices, none required by the others: you need not keep it to enjoy it or to find it again, and opening it keeps nothing. Keeping makes your own copy under what she allowed &mdash; if she takes the note back, the copy goes with it. Asking is private to you.', fid='07.7')
    + panel('What keeping a place does not do', ctx('THE DISTINCTION', [
        'Lilia is kept by you &mdash; a place in your record since Aug 30.',
        'Maya&rsquo;s note is hers, reachable while she shares it. Keeping the place does not keep her words, and her words do not become yours by being the reason you kept it.'],
        receipt='Returned to Social 08.2 / 08.3 and Entity 12.4'),
        note='The exact distinction the source route needs: an original still accessible through sharing, versus one deliberately retained. Placement, guest and retention agreements remain proposals with their own owners.', phone=False, fid='07.8')
    + '</div>')
save("07 - The people in my life.dc.html", t)

# ============================================================ P3 · Home stack + the ticket that still says 11:20
t = load("P3 - Something I deliberately saved.dc.html")
assert t.count(TAB) >= 2
i4 = t.find('>THIS MORNING &middot; 8:40<'); i5 = t.find('>NO CONNECTION &middot; 9:15 PM<')
assert 0 < i4 < i5
def swap_tab_after(t, idx):
    j = t.find(TAB, idx); assert j > 0
    return t[:j] + tab_active('Home') + t[j+len(TAB):]
t = swap_tab_after(t, i4); t = swap_tab_after(t, t.find('>NO CONNECTION &middot; 9:15 PM<'))
t = sub1(t, '<span class="door">Today&rsquo;s plan, as it is now &rarr;</span>',
         '<span class="door">Today&rsquo;s plan, as it is now &rarr;</span></div><div style="margin:10px 22px 0 22px; display:flex; align-items:center; gap:12px; min-height:44px; border-top:1px solid var(--hair-thin);"><span class="child" style="flex-grow:1; color:var(--mute);">The ticket you hold still says 11:20</span><span class="meta">YOURS</span>' + CHEV, "P3.4 ticket mismatch")
t = sub1(t, 'Tomorrow&rsquo;s ferry &middot; the ticket, as issued', 'Tomorrow&rsquo;s ferry &middot; as issued, 11:20', "P3.5 ticket")
t = sub1(t, 'Home 08c sends &ldquo;Today, as it stands&rdquo; here. Every fact carries its time; the change is a row with the old and new values; one door goes to the plan. Ask from this page binds to the plan as it is now &mdash; a behavior, not a line of copy.',
         'Home 08c sends &ldquo;Today, as it stands&rdquo; here, and the page stays in Home&rsquo;s stack &mdash; the tab does not jump to Life because Life owns the reader. Every fact carries its time; the change is a row with the old and new values; the ticket you already hold is named as the thing that still says 11:20 (the mechanic Plans draws for a reservation that has not moved). One door goes to the plan; Ask binds to the plan as it is now.', "P3.4 note")
t = sub1(t, 'Originals read; the plan shows its last update time; nothing is guessed about what changed after. No cached material is hidden and no shared state is promised current.',
         'Originals read &mdash; including the ticket, which says 11:20 whatever the plan now says; the plan shows its last update time; nothing is guessed about what changed after. Still Home&rsquo;s stack, still Home&rsquo;s tab.', "P3.5 note")
save("P3 - Something I deliberately saved.dc.html", t)

# ============================================================ P1 · a kept place is not her words
t = load("P1 - What I keep ahead of me.dc.html")
t = sub1(t, 'HERS &middot; SHE CAN TAKE IT BACK', 'HERS &middot; REACHABLE WHILE SHE SHARES IT', "P1 note meta")
t = sub1(t, 'Her note, readable as she wrote it; Friday&rsquo;s plan; the place itself. &ldquo;No visits yet&rdquo; stays exactly true, and nothing asks you to go.',
         'Her note, readable as she wrote it; Friday&rsquo;s plan; the place itself. The place is kept by you; the words stay hers. &ldquo;No visits yet&rdquo; stays exactly true, and nothing asks you to go.', "P1 note")
save("P1 - What I keep ahead of me.dc.html", t)
print("done")
