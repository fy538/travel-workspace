"""Sept 12 records: board 13 on 00 (status + map), 07 (coverage disposition) and 12 (W reconciliation).
Usage: python3 records_0912.py <mirror-dir>"""
import sys, os
D = sys.argv[1]
def rep(path, old, new, once=True):
    p = os.path.join(D, path); s = open(p).read()
    if new.split('<span>')[1][:40] in s: print('already', path); return
    assert s.count(old) == 1, (path, s.count(old)); open(p, 'w').write(s.replace(old, new)); print('patched', path)

F13 = '13 Scoped Actions, Drafts, Requested Work.dc.html'
# --- 00 status row ---
a = '<div class="r"><span class="rk">Sept 11 · shared package</span>'
rep('00 Start Here.dc.html', a,
 '<div class="r"><span class="rk">Sept 12 · the family, finished</span><span>Board 13 answers the three details the family had left open: what a row’s “···” opens, scoped to what that stop actually supports; what survives an interruption, a dismissal and a return, with the draft waiting on the row rather than in an inbox; and how asked-for work ends — an acceptance that ends when it answers, one delivery while away, a result on the night it concerns, or a truthful failure that says what stopped. Continuing help (12 W2–W5) keeps its separate, still-proposed decision.</span></div>\n            ' + a)
# --- 00 board map row ---
b = '<div class="r"><span class="rk">Before shared package</span>'
rep('00 Start Here.dc.html', b,
 f'<div class="r"><span class="rk"><a href="?file={F13.replace(" ", "+")}">13 Scoped actions, drafts, requested work</a></span><span><b>Sept 12.</b> What “···” opens on a booked stop of yours, on an option and on a stop from someone else’s schedule (S1–S3). A draft through interruption, dismissal and return, and the rule for safe versus unsafe retry (D1–D3). A finite request end to end: acceptance, the away delivery, the answer on its night, a truthful failure, and the result found with no notification after the night went away (R1–R5). Handback panel: donors, the details now defined, and the finite-work versus continuing-service boundary.</span></div>\n          ' + b)
# --- 07 coverage disposition ---
c = '<div class="r"><span class="rk">Limit</span>'
rep('07 Decisions, Mapping, Reuse.dc.html', c,
 '<div class="r"><span class="rk">Delivered · 2026-09-12</span><span><b>Board 13</b> closes A1’s targeted addition (the row “···” set, scoped per stop kind, with no edit machinery), A2’s and A4’s drawn portions (draft through interruption and dismissal; close is not cancel) and A3’s safe-versus-unsafe retry rule, and connects the finite requested-work sequence end to end with its truthful endings. <b>Still open where it was:</b> the native checks under A2, the shared busy/held action state under A3, the shared draft and Undo treatments under A4, the external-return pattern under A5, and A6’s following decision. One new shared-variant candidate: a list-of-actions sheet row with a destination marker and a scoped note.</span></div>\n          ' + c)
# --- 12 panel row ---
d = '<div class="row2"><span class="rk">Sept 10 pass</span>'
rep('12 Brought In and Followed - Two Bounded Additions.dc.html', d,
 '<div class="row2"><span class="rk">Sept 12 · where this sits now</span><span><b>Board 13 draws the supported end of this family:</b> a current check that answers now (W1’s shape) and finite requested work that leaves, comes back once and closes itself. <b>W2–W5 are unchanged and still proposed</b> — a window, hear-once, coverage loss and Stop remain a separate decision, and board 13 creates no ongoing service. The distinction now exists in customer words rather than annotation: “this ends when I answer — it isn’t watching anything” (13 R1). Where following is supported, its ending and Stop are findable in the same two places 13 uses: the acceptance card and the row the work concerns.</span></div>\n        ' + d)
