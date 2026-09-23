#!/usr/bin/env python3
"""Sept 9 second pass: 05 D8 names the displaced time; 07 labels the narrow sentence-6 amendment request; 00 status."""
import sys, os
S=sys.argv[1]
def edit(f, pairs):
    p=os.path.join(S,f); t=open(p).read()
    for a,b in pairs:
        assert a in t,(f,a[:80]); t=t.replace(a,b,1)
    open(p,'w').write(t); print('edited',f[:14])
# ---- item 1 · D8: protect Sam's evening
edit('05 D - The Day Changes While People Move.dc.html', [
 ('<div class="conn"><div class="t">you</div><div class="c">On the F now · <b>you’d arrive about 5:20</b>, so there’s time. Bergen St has a café on the corner; or ride on to Carroll Gardens and walk back.</div></div>',
  '<div class="conn"><div class="t">you</div><div class="c">On the F now · <b>you’d be there about 5:20 — two hours and forty minutes before dinner</b>, an hour more than the seven you set out for. If you’d rather not spend it there, the F back runs every few minutes; coming at eight is yours to choose.</div></div>'),
 ('<span class="n">D8</span>SAM, ON THE F, SEES THE CHANGE <span class="s">dinner-only participant · the dinner’s new start and his own answer stay distinct (Social 03.6/03.7 form)</span>',
  '<span class="n">D8</span>SAM, ON THE F, SEES THE CHANGE <span class="s">the displaced time named · one way forward that is his · the dinner’s new start and his own answer stay distinct</span>'),
 ('<div class="k">THE AFFECTED PERSON’S VIEW</div>\n          <p>Sam’s page leads with the change in the identity block, then arrival guidance derived from where he is, then two real answers. The mismatch reaches him as one honest phrase (“Nora’s on it”), not a red banner. The closing line states the rule about silence in his terms.</p>',
  '<div class="k">THE AFFECTED PERSON’S VIEW · NAME WHAT THE CHANGE COSTS HIM</div>\n          <p>Sam’s page leads with the change in the identity block, then what it actually does to his evening, then two real answers. The mismatch reaches him as one honest phrase (“Nora’s on it”), not a red banner. The closing line states the rule about silence in his terms.</p>\n          <p><b>Sept 9 correction.</b> Arriving at 5:20 for an eight o’clock dinner is 160 minutes in the neighbourhood, and the earlier line (“so there’s time”, then a café or a walk) treated that as a logistics problem already solved. Now the cost is named in plain numbers, and the two quantities are kept apart: the 2h40 he would have, and <b>the hour of it this change added</b> — the rest was his own early start, which is his business and is not asked about or guessed at. The one way forward offered is inside his own participation (come at eight instead; the F runs both ways), not a request to Nora and not an errand invented for him. His preferences are not modelled: nothing says he dislikes waiting, and Social’s separate leave-by-nine fixture is not imported. Declining stays a first-class answer.</p>'),
 ('<div class="fx">justified notification · personal response state · delivered ≠ consent</div>',
  '<div class="fx">justified notification · personal response state · delivered ≠ consent · Sept 9 item 1: the cost named, one voluntary way forward, no invented preferences</div>'),
])
# ---- item 2 · 07: label the narrow amendment request
edit('07 Decisions, Mapping, Reuse.dc.html', [
 ('<div class="li"><span class="n">—</span><span><b>Retired as rules:</b>',
  '<div class="li"><span class="n">Sept 9</span><span><b>AMENDMENT REQUESTED · sentence 6, narrowly.</b> The accepted 2026-09-05 decision says plainly: “Vesper says less; people must ask more,” and “no recommendation carries a button.” Later strategy expects practical preparation before continuing help is accepted. <b>The request:</b> allow <i>one</i> obvious contextual continuation to be offered as a door when it saves the person retyping a decision they have already expressed and re-coordinating people already involved — drawn as 11 I1’s “Prepare a proposal for Maya and Sam” → I1b → I1c. <b>Bounds, all of which stay:</b> Send is always human and the words are editable; nothing changes the arrangement, provider truth or anyone’s participation by being prepared; one door, never a set; no command catalog, recommendation dashboard or unsolicited management; recommendations still appear only when asked or once after a problem. <b>The trade, in work rather than buttons:</b> without it Nora retypes a decision Vesper has just stated and re-addresses two people it already knows (one composition, two recipients, one send); with it she reads a prepared message and sends or edits it (one read, one send). No prompt or check is removed elsewhere. <b>Status:</b> requested, not adopted; the accepted decision is unchanged until a new one supersedes it. Owner: founder.</span></div>\n            <div class="li"><span class="n">—</span><span><b>Retired as rules:</b>'),
])
# ---- 00 status
edit('00 Start Here.dc.html', [
 ('<div class="r"><span class="rk">Sept 9 · practical completeness</span>',
  '<div class="r"><span class="rk">Sept 9 · fresh review</span><span>05 D8 names what the change costs Sam (2h40 there, an hour of it added) and offers one way forward that is his. 12 W2/W3 state held 7:00, wanted 8:00 and offered 8:15 in one reading. Board 12’s handback records the Home 08c ↔ Life P3.4/P3.5 branch check (Home has no post-3:10 state) and a before/after of waiting, prompting, checking and coordination work. 07 carries the narrow sentence-6 amendment <b>request</b> — not adopted.</span></div>\n            <div class="r"><span class="rk">Sept 9 · practical completeness</span>'),
])
print('done')
