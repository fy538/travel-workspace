#!/usr/bin/env python3
"""Sept 9: 05 D8 takes Social 03.6/03.7's actor-specific form; 00 index. argv[1] = mirror dir."""
import sys, os
S=sys.argv[1]
def edit(f, pairs):
    p=os.path.join(S,f); t=open(p).read()
    for a,b in pairs:
        assert a in t,(f,a[:80]); t=t.replace(a,b,1)
    open(p,'w').write(t); print('edited',f[:14])
edit('05 D - The Day Changes While People Move.dc.html', [
 ('<div class="thesis">Nora moved dinner from 7:00 to 8:00 a few minutes ago. Same place.</div>',
  '<div class="thesis">Nora moved dinner to eight, same place. You said yes to seven; that stays yours until you say otherwise.</div>'),
 ('<span class="n">D8</span>SAM, ON THE F, SEES THE CHANGE <span class="s">dinner-only participant · actionable, not alarming</span>',
  '<span class="n">D8</span>SAM, ON THE F, SEES THE CHANGE <span class="s">dinner-only participant · the dinner’s new start and his own answer stay distinct (Social 03.6/03.7 form)</span>'),
])
edit('00 Start Here.dc.html', [
 ('<div class="r"><span class="rk">Sept 8 · consolidation</span>',
  '<div class="r"><span class="rk">Sept 9 · practical completeness</span><span>Board 12 refined: a near table is an alternative, not fulfillment (W2/W3/W5); the 10:40 home leaves the reception by 10:15, or the 11:45 (X2–X4); C1–C2 added — the current arrangement after a change and the sentences Plans supplies to Home 08c and Life P3.4/P3.5, in dates and facts, not doctrine; 05 D8 takes Social’s actor-specific form. Continuing-help semantics still PROPOSED.</span></div>\n            <div class="r"><span class="rk">Sept 8 · consolidation</span>'),
 ('Bounded continuing help: a current check that is not a watch, following asked for in words with one scope card, a useful result, coverage lost, silence and the return (W1–W5, PROPOSED).',
  'Bounded continuing help: a current check that is not a watch, following asked for in words with one scope card, a near match mentioned without ending the request, coverage lost, silence and the return (W1–W5, PROPOSED). Current, captured, changed: the plan after a change and what it supplies to Home and Life (C1–C2).'),
])
print('done')
