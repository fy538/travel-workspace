#!/usr/bin/env python3
"""Sept 9 second-pass strategy alignment: A3/A4 waiting, D8 conditional alternative,
07 J2f<->I1 comparison, stale board-10 links. argv[1] = mirror dir."""
import sys, os, re
S = sys.argv[1]
def edit(f, pairs):
    p = os.path.join(S, f); t = open(p).read()
    for a, b in pairs:
        assert a in t, (f, a[:80]); t = t.replace(a, b, 1)
    open(p, 'w').write(t); print('edited', f[:16])

# ---- item 1 · A3 + A4: spare time is not a better evening
edit('02 A - A Loose Saturday.dc.html', [
 ('<div class="fact"><div class="fk">sets</div><div><b>8:30</b> — tight after dinner (leave Theo by 8:12) · <b>10:30</b> — fits, arrive about 9:18</div></div>',
  '<div class="fact"><div class="fk">sets</div><div><b>8:30</b> — tight after dinner (leave Theo by 8:12) · <b>10:30</b> — no rush, though leaving at nine means 9:18 there against 9:45 doors</div></div>'),
 ('<div class="b">Dinner stays exactly as it is. You’d leave when it winds down, around 9:00, and arrive about 9:18 with time to spare. Nothing else moves.</div>',
  '<div class="b">Dinner stays exactly as it is. But leaving when it winds down, about nine, puts you there at 9:18 — doors are 9:45 and the set is 10:30, so that is <b>seventy-two minutes of waiting, twenty-seven of them outside</b>. Staying with Theo until about ten gets you there at 10:18, twelve minutes before the set.</div>'),
 ('<span class="n">A4</span>“MAKE IT LESS RUSHED” · AN EXPLORATORY ALTERNATIVE <span class="s">active · returned, not applied</span>',
  '<span class="n">A4</span>“MAKE IT LESS RUSHED” · WHICH KIND OF UNRUSHED <span class="s">the waiting named · staying longer compared · returned, not applied</span>'),
 ('<div class="k">EXPLORATION RETURNS AN ALTERNATIVE WITHOUT APPLYING IT</div>',
  '<div class="k">SPARE TIME IS NOT A BETTER EVENING</div>\n          <p><b>Sept 9 correction.</b> “Less rushed” was answered by arriving earlier, which is the opposite of what it buys: 9:18 against 9:45 doors is seventy-two minutes of waiting, twenty-seven of them on the street, and A3’s fact line said the same thing without noticing it. Both frames now state the waiting, and the alternative compares the shape that actually removes the rush — <b>staying with Theo longer</b> — using only fixture facts (18 minutes on foot, doors 9:45, set 10:30). Nothing fills the gap: no waiting venue is invented, no second stop is proposed, and the jazz stays a loose option decided on the night. The choice between the two shapes is hers and needs no missing fact; if she wants a third reading she says so in the field.</p>'),
])

# ---- item 2 · D8: conditional alternative with a supported destination and cost
edit('05 D - The Day Changes While People Move.dc.html', [
 ('<div class="conn"><div class="t">you</div><div class="c">On the F now · <b>you’d be there about 5:20 — two hours and forty minutes before dinner</b>, an hour more than the seven you set out for. If you’d rather not spend it there, the F back runs every few minutes; coming at eight is yours to choose.</div></div>',
  '<div class="conn"><div class="t">you</div><div class="c">On the F now · <b>you’d be there about 5:20 — two hours and forty minutes before dinner</b>, an hour more than the seven you set out for. If you were heading over early for something anyway, nothing has changed. If not, home is twelve minutes back on the F and leaving again about half seven still gets you there first.</div></div>'),
 ('The one way forward offered is inside his own participation (come at eight instead; the F runs both ways), not a request to Nora and not an errand invented for him.',
  '<b>Sept 9, second pass:</b> the way forward is now conditional and costed rather than a bare instruction to ride back. It opens by allowing that he may have had his own reason to be over early, in which case the change costs him nothing; only if not does it name a supported destination (home), the round trip from an established fixture (twelve minutes each way on the F) and the time he would leave again (about 7:30) to still arrive first. It stays inside his own participation, is not a request to Nora, and is not an errand invented for him.'),
 ('Declining stays a first-class answer.',
  'Declining stays a first-class answer, and so does leaving the plan alone: “8 works” and “Can’t do 8” are the only two things he is asked for.'),
])

# ---- item 3 · 07: compare the accepted sparse route with the prepared continuation
edit('07 Decisions, Mapping, Reuse.dc.html', [
 ('<b>Status:</b> requested, not adopted; the accepted decision is unchanged until a new one supersedes it. Owner: founder.',
  '<b>The same choice on 09 J2f:</b> Vesper names that Ben’s move lands after the quieter window and stops there; raising it with Ben means the person types the request and the message is composed from nothing (one reconstruction, one composition, one send). The amendment would offer that single continuation as a door with the message already addressed and editable (one read, one send). Both routes end in a human Send, neither touches Ben’s authorized edit, and sending a question changes no arrangement and no one’s answer — the difference is a reconstruction the person no longer performs. <b>Kept distinct from 05 D3’s Update &amp; send,</b> which follows an owner instruction and does change the arrangement. <b>Status:</b> requested, not adopted; the accepted decision is unchanged until a new one supersedes it. Owner: founder. Plans leads this request; siblings should adopt I1b’s reading (a prepared message that changes nothing) rather than selecting outcomes independently.'),
])

# ---- stale board-10 links in the appendices
for f in ['90 Appendix - Change States and Recovery.dc.html', '91 Appendix - Coverage, Arrival, Peers.dc.html',
          '92 Appendix - Interactive Prototype.dc.html']:
    p = os.path.join(S, f); t = open(p).read(); n = t.count('board 10')
    t = t.replace('board 10', 'board 92')
    open(p, 'w').write(t); print('board-10 links fixed in', f[:16], n)
print('done')
