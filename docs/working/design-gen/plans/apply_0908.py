#!/usr/bin/env python3
"""September 8 corrections to existing Plans boards (05 D4, 08 P10, 07, 00). argv[1] = mirror dir."""
import sys, os, re
S = sys.argv[1]
def edit(f, pairs):
    p = os.path.join(S, f); t = open(p).read()
    for a, b in pairs:
        assert a in t, (f, a[:80]); t = t.replace(a, b, 1)
    open(p, 'w').write(t); print('edited', f[:14])
# ---- 05 D4: recipient states match actual answers; no "settled" while Sam has not answered
edit('05 D - The Day Changes While People Move.dc.html', [
 ('<span class="n">D4</span>SETTLED AT EIGHT · THE RESERVATION STILL SAYS SEVEN <span class="s">one legible mismatch</span>',
  '<span class="n">D4</span>MOVED TO EIGHT · SAM HASN’T ANSWERED · THE RESERVATION STILL SAYS SEVEN <span class="s">one legible mismatch · recipient states match actual answers</span>'),
 ('<div class="thesis">Bookstore at three, the café if it rains, dinner at eight with Maya and Sam.</div>\n              <div class="gap-l"></div>\n              <div class="receipt ink">Sent — Maya and Sam have 8:00</div>',
  '<div class="thesis">Bookstore at three, the café if it rains, dinner at eight with Maya. Sam hasn’t answered.</div>\n              <div class="gap-l"></div>\n              <div class="receipt ink">Updated to 8:00 · sent to Maya and Sam</div>'),
])
t = open(os.path.join(S, '05 D - The Day Changes While People Move.dc.html')).read()
t = re.sub(r'(<span class="n">D4</span>.*?<div class="ann">\s*<div class="k">)([^<]*)(</div>)',
           lambda m: m.group(1) + 'PERSONAL FIXED POINT · AGREEMENT · RESERVATION · AND WHO HAS ACTUALLY ANSWERED' + m.group(3), t, count=1, flags=re.S)
t = t.replace('</p>\n          <div class="fx">S4 · “show the practical mismatch rather than a confident done”',
  '</p>\n          <p><b>Sept 8 correction.</b> The thesis and the label no longer say “settled” or “with Maya and Sam” while Sam has not answered: the owner’s update moved the time (D3, Update &amp; send); it did not move Sam’s participation or the restaurant’s table by implication. The receipt says what was updated and to whom, not that they “have” it — sending is not delivery, delivery is not acceptance. Contrast 11 I1b, where a sent proposal changes nothing at all until people answer.</p>\n          <div class="fx">S4 · “show the practical mismatch rather than a confident done”', 1)
open(os.path.join(S, '05 D - The Day Changes While People Move.dc.html'), 'w').write(t)
# ---- 08 P10: whole-option judgment — the decisive conflict first, then the supported part
edit('08 Contextual Request - Resting, Active, Resolved.dc.html', [
 ('<span class="n">P10</span>“BOOK US A HOTEL IN NARA” · THE SUPPORTED PART, IN PLACE <span class="s">options + external links · boundary stated once · no Chat transfer required</span>',
  '<span class="n">P10</span>“BOOK US A HOTEL IN NARA” · THE FIT FIRST, THEN THE SUPPORTED PART <span class="s">the decisive conflict named · options only after it · boundary stated once</span>'),
 ('<div class="ans">Two that fit a one-night stop near the park, both walkable from Tōdai-ji <span class="fixlabel">FIXTURE OPTIONS</span>:</div>',
  '<div class="ans"><b>Monday night in Nara means missing the 19:00 kaiseki in Gion</b> — it’s reserved for two — and a night at the ryokan you’ve already paid for. If you’d rather stay over, the counter is between you and them to move; Tuesday would start from Nara instead. If that trade is worth it, two that fit near the park, both walkable from Tōdai-ji <span class="fixlabel">FIXTURE OPTIONS</span>:</div>'),
 ('<div class="k">DELIVER THE SUPPORTED VALUE HERE</div>\n          <p>The product does not execute bookings, but the useful part of the request',
  '<div class="k">THE WHOLE-OPTION JUDGMENT FIRST; THEN DELIVER THE SUPPORTED VALUE HERE</div>\n          <p><b>Sept 8 correction (handoff map §4.5).</b> Offering a Nara hotel for Monday without reconciling the Kyoto dinner and the Kyoto stay that night was external-provider honesty without useful assistance. The answer now leads with the decisive conflict — the reserved 19:00 counter in Gion and the paid ryokan night — and the relevant choice, and offers the options only after it, conditionally. Nothing is moved or cancelled by implication; the counter’s reservation is theirs to change with the restaurant.</p>\n          <p>The product does not execute bookings, but the useful part of the request'),
])
# ---- 07: Q23/Q24 + amendment list line
edit('07 Decisions, Mapping, Reuse.dc.html', [
 ('<span class="n">Q20</span><span><b>Notifications (critique)</b>',
  '<span class="n">Q23</span><span><b>Continuing help (Sept 8, board 12 W2–W5, PROPOSED)</b> — the “follow this for me” service row of consumer strategy §3 as design: subject, supported source, window, hear-once treatment, ending by result / coverage loss / expiry / Stop; owner of capability-loss detection is the live engine; no scheduler, dashboard, billing surface or provider execution. Needs a decision before adoption.</span></div>\n            <div class="li"><span class="n">Q24</span><span><b>Brought-in arrangement (Sept 8, board 12 X1–X4)</b> — an external schedule kept beside a day as evidence with a stable source identity (C&amp;C §3.9 Bring/T1): what is parsed vs what a person reads, how it is refreshed or released, and how the competing commitment it collides with is surfaced once. Entity/Life lanes for the source object.</span></div>\n            <div class="li"><span class="n">Q20</span><span><b>Notifications (critique)</b>'),
 ('<div class="li"><span class="n">—</span><span><b>Retired as rules:</b>',
  '<div class="li"><span class="n">Sept 8</span><span><b>Two bounded additions (board 12), compatible with the seven sentences except where marked.</b> <i>Compatible:</i> an arrangement made elsewhere is read back as attributed rows beside the person’s day (sentences 1, 4); “help me choose” gets one judgment because it was asked (sentence 6); “I’ve chosen” gets checks with finite direct choices (sentence 2); a current check says it is not watching. <i>PROPOSED, needs a decision:</i> continuing help asked for in words — one scope card, hear once, ends by result / coverage loss / expiry / Stop (W2–W5; Q23). <i>Corrected:</i> 05 D4 recipient states; 08 P10 whole-option judgment. Sibling deltas for Home 08c, Life 03b, Social 03.6/03.7 and Chat are on board 12’s handback panel.</span></div>\n            <div class="li"><span class="n">—</span><span><b>Retired as rules:</b>'),
])
# ---- 00: index row + status
edit('00 Start Here.dc.html', [
 ('<div class="r"><span class="rk"><a href="?file=90+Appendix',
  '<div class="r"><span class="rk"><a href="?file=12+Brought+In+and+Followed+-+Two+Bounded+Additions.dc.html">12 Brought in and followed</a></span><span><b>Sept 8.</b> An arrangement made elsewhere: a wedding schedule read back as attributed rows, “help me choose” vs “I’ve chosen; help with the checks”, the one competing commitment, the page at 135% (X1–X4b). Bounded continuing help: a current check that is not a watch, following asked for in words with one scope card, a useful result, coverage lost, silence and the return (W1–W5, PROPOSED). Handback panel: Home 08c / Life 03b / Social / Chat deltas, corrections, pending decisions.</span></div>\n          <div class="r"><span class="rk"><a href="?file=90+Appendix'),
 ('<div class="r"><span class="rk">§0.8 · 2026-09-06</span>',
  '<div class="r"><span class="rk">Sept 8 · consolidation</span><span>Corrected 05 D4 (no “settled”/“with Sam” while unanswered; receipt says updated-and-sent) and 08 P10 (the Gion counter and the paid ryokan night lead; hotels follow). Added board 12 with the two bounded additions the shared handoff map asked for. Continuing-help semantics PROPOSED (07 Q23); brought-in source identity Q24. Nothing wired; 92 untouched.</span></div>\n            <div class="r"><span class="rk">§0.8 · 2026-09-06</span>'),
 ('THE DESIGN IS 01–09 + 11 · 90–92 ARE ENGINEERING APPENDIX', 'THE DESIGN IS 01–09, 11, 12 · 90–92 ARE ENGINEERING APPENDIX'),
])
print('done')
