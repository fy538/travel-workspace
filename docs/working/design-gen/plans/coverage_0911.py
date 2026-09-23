"""Sept 11: coverage follow-through record on 07 + stale board-10 fix on 08. Usage: python3 coverage_0911.py <mirror-dir>"""
import sys, os
D = sys.argv[1]
def rep(path, old, new):
    p = os.path.join(D, path); s = open(p).read()
    if new in s: print('already', path); return
    assert s.count(old) == 1, (path, old[:60], s.count(old)); open(p, 'w').write(s.replace(old, new)); print('patched', path)
R = lambda k, v: f'          <div class="r"><span class="rk">{k}</span><span>{v}</span></div>\n'
CARD = ('<div class="card">\n          <div class="k">COVERAGE FOLLOW-THROUGH · PLANS AUDIT A1–A6 · DISPOSITION, OWNER, NEXT TRIGGER · 2026-09-11</div>\n'
 + R('A1 · 03 date rail and rows', '<b>Existing selected donor</b>, unchanged by adoption. <b>Targeted addition:</b> what the row “…” opens — a scoped set of row actions, not an edit form on every row. Owner: shared-library owner with Components &amp; Plan. Trigger: the controls canvas defines row actions.')
 + R('A2 · 08 contextual request', '<b>Existing donor, kept local</b>: target, private kicker, field with mic and send, continued answer. <b>Later native check:</b> dismiss, focus, keyboard avoidance and return — the drawn keyboard proves none of it. Owner: native mobile build. Trigger: the first native sheet.')
 + R('A3 · 90 J2c/J2d/J2e', '<b>Adopted:</b> these frames now consume the shared Notice rather than a local copy. <b>Owner dependency:</b> a busy or held action state in the shared controls, so unsafe retry can be held without blocking navigation; 92 simulates that, it does not implement it. Owner: shared-library owner. Trigger: action-control states on the controls canvas.')
 + R('A4 · 90 J2g/J3d', '<b>Behavior donor, owner dependency:</b> recovered draft, discard and scoped Undo need shared control treatments; closing is not cancel, and Undo never erases someone else’s change. The proposed draft retention duration is not adopted. Owner: shared-library owner. Trigger: the shared pending/failed/unknown/draft state set.')
 + R('A5 · 90 D5/D6/D7', '<b>Behavior donor, owner dependency:</b> returning from a provider is not confirmation; a fresh fact is not another person’s answer; a stale alternative revalidates in place. Owner: shared-library owner with Places (external return). Trigger: the shared external-return pattern.')
 + R('A6 · 11 and 12', '<b>Selected donor:</b> 11 I1–I1c prepared-message door (now the shared Door). <b>Proposed capability:</b> 12’s following terms stay proposed — founder decides; no shared row states until then. X1 now reads Ask by default with a separate Keep. Owner: founder (following); C&amp;C owner for a kept schedule’s identity (Q24). Trigger: a following decision.')
 + R('Limit', 'Design coverage, not implementation or verified behavior.')
 + '        </div>\n\n        ')
rep('07 Decisions, Mapping, Reuse.dc.html', '<div class="card">\n          <div class="k">TYPE / MATERIAL MAPPING', CARD + '<div class="card">\n          <div class="k">TYPE / MATERIAL MAPPING')
rep('08 Contextual Request - Resting, Active, Resolved.dc.html', '<span>Board 10 uses scripted recognizers', '<span>Board 92 (the prototype, formerly 10) uses scripted recognizers')
