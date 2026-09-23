# -*- coding: utf-8 -*-
"""Sep 10 residual corrections (handoff §0 selected direction): equal competent advice,
supported reading boundary, named Keep verbs and eligibility, soft Saturday + saved-version doors.
Run: python3 refine_0910.py <src> <out>"""
import sys, os
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def rep(t, a, b, n=1, name=""):
    c = t.count(a); assert c == n, f"{name or a[:45]!r}: found {c}, expected {n}"
    return t.replace(a, b)

# ============================================================ 1 · 06.6 / 06.7 equal competent advice
t = load("06 - Give once, get value back.dc.html")
t = rep(t, 'CHAT &middot; SAT 4:10 PM</div>', 'CHAT &middot; SAT 4:10 PM &middot; FROM FORT GREENE</div>', 1, "06.6 header")
t = rep(t, 'CHAT &middot; SAT 4:10 PM &middot; NO ENTRUSTED CONTEXT', 'CHAT &middot; SAT 4:10 PM &middot; FROM FORT GREENE &middot; NO ENTRUSTED CONTEXT', 1, "06.7 header")
t = rep(t, 'Take the ferry over &mdash; the part you like. Last one back is 8:10, so come home the way you did in June, over the bridge, or drive back as in April.',
        'Ferry over from Atlantic Basin &mdash; the part you like. Last boat back is 8:10, so come home the way you did in June: the walk over the bridge, about fifty minutes. The B61 runs till late if the legs say no.', 1, "06.6 answer")
t = rep(t, 'Places checked tonight&rsquo;s sailings &middot; 4:02 pm &middot; your two evenings', 'Places checked tonight&rsquo;s sailings and the B61 &middot; 4:02 pm &middot; your two evenings', 1, "06.6 receipt")
t = rep(t, 'The ferry, the B61, or a car. The last ferry back is 8:10, so if you go over on it you will want another way home.',
        'Ferry over from Atlantic Basin &mdash; it is the good way in. Last boat back is 8:10, so plan the B61 home; it runs till late.', 1, "06.7 answer")
t = rep(t, 'Places checked tonight&rsquo;s sailings &middot; 4:02 pm</div></div></div><div class="cnote">The same live check',
        'Places checked tonight&rsquo;s sailings and the B61 &middot; 4:02 pm</div></div></div><div class="cnote">The same live check', 1, "06.7 receipt")
t = rep(t, 'Same question, same live check, same competence as 06.7 &mdash; only eligible history differs. What it buys: a recommendation instead of a list, a way home drawn from what she has actually done, and no round of &ldquo;which way do you usually go?&rdquo;. Life supplied the two evenings and her line; the live times are Places&rsquo;.',
        'Same origin, same conditions, same live check, same recommendation as 06.7 &mdash; only eligible history differs. What it buys is narrow: the return she actually chose and liked in June is offered first, and she is not asked which she would prefer. The car stays out of it &mdash; taking the ferry over does not put it at the far end. Life supplied the two evenings and her line; the live times are Places&rsquo;.', 1, "06.6 note")
t = rep(t, 'The same live check and the same warning: history does not unlock ordinary competence. What is missing is smaller and real &mdash; three options instead of one recommendation, and &ldquo;another way home&rdquo; instead of the two ways she has used. Had the answers come out the same, that would have been a fair result too.',
        'A competent answer on its own terms: same origin, same check, a recommendation, and a viable way home. History does not unlock ordinary transport advice. The delta is one line of fit &mdash; the bridge walk she already knows she likes, offered instead of the default bus &mdash; and one question not asked. Close to a tie, which is a fair result.', 1, "06.7 note")
save("06 - Give once, get value back.dc.html", t)

# ============================================================ 2 · the book boundary, from supplied evidence
t = load("02 - An ordinary beginning.dc.html")
t = rep(t, 'Your note: page 280, no hurry', 'Your note: just reached the Rome chapters', 2, "02 week rows")
t = rep(t, '&ldquo;Page 280, no hurry.&rdquo;', '&ldquo;Just reached the Rome chapters. No hurry.&rdquo;', 1, "02 book page row")
t = rep(t, 'Her husband &mdash; she married him early, against her sister&rsquo;s judgement. Will Ladislaw is his young cousin, which is why the will matters later. Kept to before page 280, where your last note left off; say the word if you&rsquo;re past it.',
        'Her husband &mdash; she married him early, against her sister&rsquo;s judgement, and Rome is where the mismatch starts to show. Will Ladislaw is his young cousin; he turns up there too. Nothing from after the Rome chapters, since that is where you said you were &mdash; say the word if you&rsquo;re past them.', 1, "02.7 answer")
t = rep(t, 'Better help now, not a resumed setup: the answer is shaped by what was entrusted (her own note said page 280) so it does not run ahead of her, and it invites a correction instead of assuming progress. Nothing was logged to make this work.',
        'Better help now, not a resumed setup: the boundary is an event she named &mdash; the Rome chapters &mdash; not a page number that depends on the edition, and it holds back what comes after rather than hinting at it. It invites a correction instead of assuming progress, and nothing was logged to make this work.', 1, "02.7 note")
t = rep(t, 'Both, and the book keeps refusing to choose. Since you were around Casaubon&rsquo;s will last time, this is the part where that inheritance starts steering it &mdash; still nothing past where you were.',
        'Both, and the book keeps refusing to choose. You were in the Rome chapters last time, so staying there: the friction between them is already as much about his politics as about her &mdash; nothing from after that.', 1, "02.9 answer")
save("02 - An ordinary beginning.dc.html", t)

# ============================================================ 3 · named Keep verbs, eligibility, honest limits
t = load("07 - The people in my life.dc.html")
t = rep(t, '<span class="door">Keep a copy &rarr;</span>', '<span class="door">Keep a copy of this note &rarr;</span>', 1, "07.7 keep door")
t = rep(t, 'Opening it keeps nothing. You can find it again for as long as she shares it; a copy is yours to reread until she takes the note back.',
        'Opening it keeps nothing, and seeing it does not make it yours. You can find it again for as long as she shares it; a copy is yours to reread until she takes the note back. Ask uses this note and your own record, nothing else of hers. Anything already off the app &mdash; a screenshot, a paste elsewhere &mdash; is beyond all of this.', 1, "07.7 note line")
t = rep(t, 'Reply, Keep and Ask are three separate choices, none required by the others: you need not keep it to enjoy it or to find it again, and opening it keeps nothing. Keeping makes your own copy under what she allowed &mdash; if she takes the note back, the copy goes with it. Asking is private to you.',
        'Reply, Keep and Ask are three separate choices, none required by the others: you need not keep it to enjoy it or to find it again, and opening it keeps nothing. <b style="color:var(--ink)">&ldquo;Keep a copy of this note&rdquo; is not &ldquo;Keep the place&rdquo;</b> &mdash; one retains a permitted copy of her original, the other adds Lilia to your places; an unqualified &ldquo;Keep it&rdquo; (Entity 14 R4) does not say which. The copy door is agreement-dependent: it needs a permitted-copy term that is still proposed. Ask is private and eligible material only.', 1, "07.7 note")
t = rep(t, 'Three different things: you can <i>reach</i> it while she shares it; the share can <i>end</i> on its own date; she can <i>take it back</i>. A copy you kept survives the second and not the third.',
        'Three different things: you can <i>reach</i> it while she shares it; the share can <i>end</i> on its own date; she can <i>take it back</i>. A copy you kept survives the second and not the third. What already left the app cannot be recalled by any of them.', 1, "07.8 terms")
save("07 - The people in my life.dc.html", t)

# ============================================================ 4a · P1, the soft Saturday preserved
t = load("P1 - What I keep ahead of me.dc.html")
t = rep(t, 'Kept &middot; private &middot; your words, no date claimed &middot; Undo', 'Kept &middot; private &middot; Saturday, loosely &middot; your words &middot; Undo', 1, "P1 receipt")
t = rep(t, 'Two degrees, never three. When Saturday passes untouched the jazz row simply leaves; the intention stays findable in search and Everything kept.',
        'Two degrees, never three. The soft Saturday is kept as she said it &mdash; a reference, not an appointment, with no time, no invitation and nothing to confirm. When Saturday passes untouched the row simply leaves; the intention stays findable in search and Everything kept.', 1, "P1 after note")
save("P1 - What I keep ahead of me.dc.html", t)

# ============================================================ 4b · P3, the ticket the operator did not reissue + the current-resource door
t = load("P3 - Something I deliberately saved.dc.html")
t = rep(t, 'The boat &middot; now 12:40, was 11:20</span><span class="meta">3:10 PM</span>',
        'The boat &middot; now 12:40, was 11:20 &middot; the operator moved it</span><span class="meta">3:10 PM</span>', 1, "P3.4 boat row")
t = rep(t, 'The ticket you hold still says 11:20', 'The ticket you hold still says 11:20 &mdash; it was not reissued', 1, "P3.4 ticket row")
t = rep(t, 'Tomorrow&rsquo;s ferry &middot; as issued, 11:20', 'Tomorrow&rsquo;s ferry &middot; as issued, 11:20 &middot; not reissued', 1, "P3.5 ticket")
t = rep(t, 'Home 08c sends &ldquo;Today, as it stands&rdquo; here, and the page stays in Home&rsquo;s stack',
        'Home 08c&rsquo;s 3:20 state and this page now agree: the operator moved the sailing at 3:10, so the plan reads 12:40 while the ticket still reads 11:20 &mdash; a changed sailing, not a changed booking. The page stays in Home&rsquo;s stack', 1, "P3.4 note")
t = rep(t, '<span class="door">Make a new version from what arrived since &rarr;</span>',
        '<span class="door">Make a new version from what arrived since &rarr;</span></div><div style="margin:10px 22px 0 22px; display:flex; align-items:center;"><span class="door">These places today, as Places reads them &rarr;</span>', 1, "P3.2 current door")
t = rep(t, 'Fourteen photos arrived, a fact was corrected, one shared photo left. The piece: marked where a fact changed, absent where a source left, the caption untouched, a new version offered &mdash; never applied.',
        'Fourteen photos arrived, a fact was corrected, one shared photo left. The piece: marked where a fact changed, absent where a source left, the caption untouched, a new version offered &mdash; never applied. The second door is separately labeled and goes elsewhere: today&rsquo;s reading of those places, from Places. Purpose-responsive selection happens there and never rewrites the kept version or a human original.', 1, "P3.2 note")
save("P3 - Something I deliberately saved.dc.html", t)

# ============================================================ 4c · P2 keeps the same book note
t = load("P2 - Life changes without management.dc.html")
t = rep(t, 'Your note: page 280, no hurry', 'Your note: just reached the Rome chapters', 2, "P2 week rows")
save("P2 - Life changes without management.dc.html", t)
print("done")
