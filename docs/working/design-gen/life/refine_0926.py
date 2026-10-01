"""September 26: bounded corrections to the Life companion project, plus the ruling sheet.

  04.5   Photographs stops competing with 04b. The header drops "7 UNPLACED" (04.4 counts seven unplaced
         things across every kind, not seven photographs, and 04b.6 draws no count asking to be cleared).
         The at-rest "Export these photographs / Delete selected" doors go: selection and its doors are
         04b.11's, where each door counts only what it can reach. The note points to 04b.
         (04b.14's map gains the matching row in build_0921.py.)
  06.8   The van answer loses the invented streets and the claims attached to them (loading hours, a lot's
         size limit); the in-strip line narrating what was not used moves out of the product (the note
         already says it).
  03 03b 04 05   American spelling: canceled.
  D0     Decisions to rule: every open Life choice, the boards that draw it, the real alternatives,
         a recommendation, what changes on approval, and a ruling line.
  00     Lists D0; nineteen boards.

Usage: python3 refine_0926.py SRC OUT   (SRC = verified mirror of the live project; OUT receives changed boards)
"""
import os, re, sys

SRC, OUT = sys.argv[1], sys.argv[2]
rd = lambda n: open(os.path.join(SRC, n), encoding='utf-8').read()


def rep(s, old, new, count=1):
    n = s.count(old)
    assert n == count, (old[:80], n, count)
    return s.replace(old, new)


def div_end(s, i):
    d = 0
    for m in re.finditer(r'<(/?)div\b[^>]*>', s[i:]):
        d += -1 if m.group(1) else 1
        if d == 0:
            return i + m.end()
    raise AssertionError('unbalanced from %d' % i)


def balanced(name, s):
    assert len(re.findall(r'<div\b', s)) == s.count('</div>'), (name, 'unbalanced divs')
    return s


out = {}

# ── 04 ───────────────────────────────────────────────────────────────────────
b = rd('04 - My original things.dc.html')
b = rep(b, '214 HELD &middot; 7 UNPLACED &middot; 2019 &mdash; NOW', '214 HELD &middot; 2019 &mdash; NOW')
k = b.index('>Export these photographs<')
start = b.rindex('<div style="margin:32px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:4px;">', 0, k)
end = div_end(b, start)
doors = b[start:end]
assert re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', doors)).strip() == 'Export these photographs Delete selected', doors
b = b[:start] + b[end:]
b = rep(b, '<div class="cnote">The grid, by year and episode; an overflow tile, never a gallery mode. Select, then act.</div>',
        '<div class="cnote">The grid, by year and episode; an overflow tile, never a gallery mode. A picture opens whole in the one '
        'viewer (04b.2), and Back returns to the same place here. Select starts 04b.11&rsquo;s selection, where each door counts only '
        'what it can reach, so the grid carries no doors of its own. Unplaced things are counted once, across every kind, on 04.4.</div>')
b = rep(b, 'CANCELLED', 'CANCELED', b.count('CANCELLED'))
assert 'Delete selected' in b  # 04.6 Passes & tickets keeps its own doors; only the photographs panel changes
out['04 - My original things.dc.html'] = balanced('04', b)

# ── 03 / 03b / 05: spelling ──────────────────────────────────────────────────
for n in ('03 - Open something in my life.dc.html', '03b - Inside a record.dc.html', '05 - Find it again.dc.html'):
    s = rd(n)
    hits = len(re.findall(r'(?i)cancelled', s))
    assert hits, n
    s = re.sub(r'Cancelled', 'Canceled', s)
    s = re.sub(r'cancelled', 'canceled', s)
    assert not re.search(r'(?i)cancelled', s)
    out[n] = s

# ── 06.8 ─────────────────────────────────────────────────────────────────────
b = rd('06 - Give once, get value back.dc.html')
b = rep(b, 'Van&rsquo;s fine: Van Brunt has loading spots before eleven, and the Beard Street lot takes anything under twenty feet.',
        'Van&rsquo;s the right call for a table. Bring a blanket and a couple of straps so it doesn&rsquo;t slide on the way back.')
line = re.search(r'<div style="margin-top:12px; padding-top:9px; border-top:1px solid var\(--hair-thin\);[^"]*">The ferry evenings were not used</div>', b)
assert line and b.count('The ferry evenings were not used') == 1
b = b[:line.start()] + b[line.end():]
assert 'Van Brunt' not in b and 'Beard' not in b
out['06 - Give once, get value back.dc.html'] = balanced('06', b)

# ── D0 · Decisions to rule ───────────────────────────────────────────────────
b00 = rd('00 - Start here.dc.html')
HEAD = b00[:b00.index('</helmet>') + len('</helmet>')] + '\n'
TAIL = '\n</x-dc>\n</body>\n</html>\n'

COLS = 'grid-template-columns:40px 290px 150px 460px 410px 170px; column-gap:24px'
th = lambda t: f'<span class="ceye">{t}</span>'
cn = lambda t, extra='': f'<div class="cn" style="font-size:12.5px;line-height:18px;{extra}">{t}</div>'


def choice(letter, text, rec):
    col = 'var(--gold-deep)' if rec else 'var(--ink)'
    return (f'<div style="display:flex;gap:10px;align-items:baseline;padding:3px 0">'
            f'<span style="font-family:var(--mono);font-size:11px;font-weight:700;color:{col};min-width:12px">{letter}</span>'
            f'<span class="cn" style="font-size:12.5px;line-height:18px;flex:1">{text}</span></div>')


def row(num, title, q, drawn, choices, rec, why, then):
    letter = rec[0]
    return (f'<div style="display:grid;{COLS};align-items:start;padding:18px 0;border-bottom:1px solid var(--hairline)">'
            f'<span style="font-family:var(--serif);font-size:24px;font-weight:600;line-height:26px;color:var(--ink)">{num}</span>'
            f'<div><div style="font-family:var(--serif);font-size:18px;font-weight:600;line-height:23px;color:var(--ink)">{title}</div>'
            f'<div style="font-family:var(--serif);font-style:italic;font-size:15px;line-height:21px;color:var(--mute);padding-top:4px">{q}</div></div>'
            + cn(drawn)
            + '<div>' + ''.join(choice(l, t, l == letter) for l, t in choices) + '</div>'
            + f'<div><div style="font-family:var(--serif);font-size:17px;font-weight:600;line-height:22px;color:var(--gold-deep)">{rec}</div>'
            + cn(why, 'padding-top:4px;color:var(--ink)')
            + cn(f'<b style="color:var(--ink)">On approval:</b> {then}', 'padding-top:6px')
            + '</div>'
            '<div style="border:1px solid var(--hairline);border-radius:10px;background:var(--card);height:92px;padding:10px 12px;box-sizing:border-box">'
            '<span class="ceye">Your ruling</span></div>'
            '</div>')


ROWS = [
    row('1', 'Who holds a kept intention',
        'When someone keeps &ldquo;jazz on Saturday, loosely,&rdquo; what holds it before any plan exists?',
        'P1.1&ndash;P1.2 &middot; the retained-intention proposal (Sep 6)',
        [('A', 'Its own small record, owned by the person, with no plan, place or time required. A plan item appears only when '
               'the intention enters an arrangement, linked both ways.'),
         ('B', 'A default personal plan that everyone has, holding every loose keep.'),
         ('C', 'Not now. Save stays as it is; nothing soft or dated can be kept.')],
        'A', 'B is a container the person never made &mdash; the planning funnel by the back door. A is what the other lanes can build '
             'against: Places, the entity page and preparation all list this as their blocker.',
        'a decision record, then schema review with Components &amp; Plan. Unblocks row 2.'),
    row('2', 'AHEAD, and how a kept intention reads',
        'Where does a soft intention live next to what&rsquo;s arranged?',
        'P1.3&ndash;P1.6 &middot; docket rulings R1&ndash;R6 (Sep 4)',
        [('A', 'Adopt R1&ndash;R6: one Time section, AHEAD, with two degrees &mdash; arranged, and kept softly in the person&rsquo;s '
               'own words &mdash; absent when nothing is ahead; three keeps with three readbacks; kept-but-unvisited places counted apart.'),
         ('B', 'Adopt AHEAD alone (R1&ndash;R2); hold the keep verbs and the counting.'),
         ('C', 'Not now. Time stays as 01 draws it; the birthday stays under SUMMER.')],
        'A, ruled with row 1', 'The roadmap holds Life&rsquo;s AHEAD until the owner is adopted. The readbacks and the counting are what '
                               'keep AHEAD from turning into a to-do list, so B keeps the risk and drops the guard.',
        '01&rsquo;s Time root changes in place (the birthday leaves SUMMER), with one decision receipt.'),
    row('3', 'What &ldquo;release&rdquo; means',
        'Is releasing something the same as deleting it, and does releasing an intention mean what releasing a source means?',
        '04.4 (Your originals; Withdrawn) &middot; 04b.11 and 09 (Delete)',
        [('A', 'One meaning for both: release means it stops being used, and the original stays yours and findable until you delete it. '
               'Delete means gone.'),
         ('B', 'Release means the original is no longer held (board 39&rsquo;s reading), which makes release and delete nearly the same.'),
         ('C', 'Separate verbs for sources and for intentions.')],
        'A', 'Three consequences, two words, no overlap. It matches what 04.4 already draws, &ldquo;Release a source from use&rdquo; beside '
             '&ldquo;Delete permanently&rdquo;, and board 10B. B would change retention policy to make one word simpler.',
        'the owning contract (Contribution &amp; Consequence) records it. No board changes.'),
    row('4', 'When the record changes on its own',
        'When late material arrives or a grouping is wrong, what changes, and what never does?',
        'P2.1&ndash;P2.7 &middot; already assumed by 04b.9',
        [('A', 'Adopt the four laws: things land by the date they happened, not the day they arrived; counts grow without announcing it; '
               'a wrong grouping splits with one sentence, a receipt, Undo, and old links that still resolve; a chosen title or a '
               'detached photo survives later enrichment.'),
         ('B', 'Adopt placement and counts; hold the split and the durable choices.'),
         ('C', 'Not now.')],
        'A', 'No board changes; the laws constrain how 01, 03 and 04 behave over time. 04b.9 already relies on the first: '
             'Saturday&rsquo;s pictures settle by their own camera times.',
        'one decision receipt; P2 retires to the archive.'),
    row('5', 'What happens to something saved',
        'When the record changes after a piece was saved, what happens to the piece?',
        'P3.1&ndash;P3.5',
        [('A', 'A snapshot by default. New material never rewrites it: a new version is offered, never applied; a corrected fact is marked '
               'where it appears; a source that left is stated absent once; the captured day shows the old and new value side by side. '
               '&ldquo;Make my version&rdquo; stays Later.'),
         ('B', 'Saved pieces stay live and update as the record changes.'),
         ('C', 'Not now.')],
        'A, for the automatic record', 'No one should find a caption they wrote rewritten; B breaks the promise that a saved thing keeps its '
                                       'word. Who holds saved pieces stays open with Components &amp; Plan, and this behavior doesn&rsquo;t depend on the answer.',
        'one decision receipt. The custody owner is named separately.'),
    row('6', 'When a record gets a map',
        'Where does a map appear in Life, and when does it stay away?',
        'P4.1&ndash;P4.6',
        [('A', 'Adopt the admission test &mdash; two or more supported places with movement, a walked plan that diverged, or a kept path; '
               'otherwise no map, no empty slot, no nudge &mdash; and planned-versus-happened as what the map reconciles. Send the kept '
               'path to the contract.'),
         ('B', 'Adopt the test only; leave reconciliation to the dossier.'),
         ('C', 'Not now.')],
        'A', 'A tracked path is location custody, so it belongs to the contract, not a board: consent per occasion, expiring, kept only '
             'when the person chooses to keep it. Everything else on P4 works without it.',
        'the kept path goes to the contract as a drafted amendment; the map organ becomes Current.'),
    row('7', 'The empty record&rsquo;s picture',
        'Does a brand-new Life get an illustration, and which one?',
        '02, Zero record (the gap is marked) &middot; illustration brief &sect;13 (Sep 1)',
        [('A', 'Run round two as the brief proposes: one small ordinary moment, direction A&rsquo;s idea with B&rsquo;s restraint, made '
               'with and without the held-cards glyph. Until one passes, the empty record ships as text.'),
         ('B', 'Drop the asset; the empty record is text for good.'),
         ('C', 'Use round one&rsquo;s refined B as it is.')],
        'A', 'Round one&rsquo;s best candidate still reads as a travel scrapbook &mdash; cup, ticket, landscape &mdash; and the brief '
             'already names the fix. The sentence and the four lenses carry the state meanwhile.',
        'round two is commissioned; the Zero record panel drops its placeholder until an image passes.'),
]

D0 = (HEAD + '<div class="cb" style="width:1760px;padding:38px"><div style="max-width:1060px">'
      '<div style="display:flex;align-items:center;gap:12px"><span class="ceye">D0 &middot; Decisions to rule</span>'
      '<span class="cpill rev">Review</span></div>'
      '<div class="ctitle" style="padding-top:8px">Seven choices the Life boards are waiting on.</div>'
      '<div class="cq" style="padding-top:6px">What needs deciding, and what&rsquo;s recommended?</div>'
      '<div class="cn" style="padding-top:8px;max-width:980px;font-size:13px;line-height:19px">Every open product choice these boards depend on, '
      'ordered so each ruling unblocks the next. Each row names the boards that draw it, the real alternatives, a recommendation and what '
      'changes on approval. <b style="color:var(--ink)">Nothing here is adopted until you rule.</b> Once ruled, adopted boards become Current '
      'and P1&ndash;P4 retire to the archive.</div></div>'
      f'<div style="display:grid;{COLS};padding:26px 0 8px;border-bottom:1.5px solid rgba(27,23,20,0.35)">'
      + th('#') + th('The decision') + th('Drawn on') + th('The choices') + th('Recommended') + th('Ruling') + '</div>'
      + ''.join(ROWS)
      + '<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:48px;padding-top:26px;max-width:1500px">'
        '<div><span class="ceye" style="color:var(--gold-deep)">Also waiting, owned elsewhere</span>'
      + cn('The permitted-copy term behind 07.7&rsquo;s &ldquo;Keep a copy of this note&rdquo; (the contract). Retention for optional '
           'conversational continuity (contract &sect;3.10). Social&rsquo;s placement and guest policy (Social). Approved photographs for '
           'PH-01 to PH-07, shared with Home and Social (you).', 'padding-top:8px')
      + '</div><div><span class="ceye" style="color:var(--gold-deep)">How to rule</span>'
      + cn('Reply with row and letter, for example &ldquo;1A 2A 3A 4A 5A 6B 7A&rdquo;. Each ruling is recorded in the manifest with its date; '
           'adopted boards become Current, and anything declined goes to the archive with its reason.', 'padding-top:8px')
      + '</div></div><div style="height:20px"></div></div>' + TAIL)
assert D0.count('Your ruling') == 7
out['D0 - Decisions to rule.dc.html'] = balanced('D0', D0)

# ── 00: D0 in the index ──────────────────────────────────────────────────────
s = rep(b00, 'SEP 6 2026 · EIGHTEEN BOARDS', 'SEP 6 2026 · NINETEEN BOARDS')
old_sec = '<div class="csec"><span class="ceye" style="color:var(--gold-deep)">Optional &middot; decisions to review, each with a recommendation</span></div>'
d0_row = ('<div style="display:flex;gap:14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--hair-thin);max-width:900px">'
          '<span class="ceye" style="min-width:60px">D0</span>'
          '<span style="font-family:var(--serif);font-size:17px;font-weight:600;min-width:270px;color:var(--ink)">Decisions to rule</span>'
          '<span class="cn" style="flex:1">Seven open choices in one sitting, each with a recommendation and a line for your ruling.</span>'
          '<span class="cpill rev">Review</span></div>')
s = rep(s, old_sec,
        '<div class="csec"><span class="ceye" style="color:var(--gold-deep)">Decisions &middot; D0 gathers them; P1&ndash;P4 draw them</span></div>' + d0_row)
s = rep(s, '<b style="color:var(--ink)">Kept open on purpose:</b>', '<b style="color:var(--ink)">Kept open on purpose, each with a recommendation on D0:</b>')
out['00 - Start here.dc.html'] = balanced('00', s)

os.makedirs(OUT, exist_ok=True)
for n, s in out.items():
    open(os.path.join(OUT, n), 'w', encoding='utf-8').write(s)
    print('%-44s %7d bytes' % (n, len(s.encode('utf-8'))))
