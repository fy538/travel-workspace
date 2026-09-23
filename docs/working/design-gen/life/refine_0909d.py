# -*- coding: utf-8 -*-
"""Sep 9 selection and correction (handoff §0): matched baselines on 06.6/06.7,
honest retained-context receipt on 02.9. Run: python3 refine_0909d.py <src> <out>"""
import sys, os
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def sub1(t, a, b, name=""):
    assert t.count(a) == 1, f"{name or a[:50]!r}: found {t.count(a)}"; return t.replace(a, b, 1)

# ---------- 06.6 / 06.7 · same query, same live check, same competence ----------
t = load("06 - Give once, get value back.dc.html")
t = sub1(t, 'Ferry, if you want the good part: last one back is 8:10 tonight, so the way home is the bridge or a car &mdash; what you did in April.',
         'Take the ferry over &mdash; the part you like. Last one back is 8:10, so come home the way you did in June, over the bridge, or drive back as in April.', "06.6 answer")
t = sub1(t, 'Places checked tonight&rsquo;s sailings &middot; 4:02 pm', 'Places checked tonight&rsquo;s sailings &middot; 4:02 pm &middot; your two evenings', "06.6 receipt")
t = sub1(t, 'What the context removed: re-explaining how she usually goes, and one bad outcome &mdash; arriving at a dock after the last boat. Life supplied the two evenings and her line; the live times are Places&rsquo;, not Life&rsquo;s judgement.',
         'Same question, same live check, same competence as 06.7 &mdash; only eligible history differs. What it buys: a recommendation instead of a list, a way home drawn from what she has actually done, and no round of &ldquo;which way do you usually go?&rdquo;. Life supplied the two evenings and her line; the live times are Places&rsquo;.', "06.6 note")
t = sub1(t, '&ldquo;Meeting Priya in Red Hook at seven &mdash; how should I get there?&rdquo;</div><div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:6px;">Three ways: the ferry, the B61 bus, or a car. Check the last sailing if you take the ferry back.',
         '&ldquo;Meeting Priya in Red Hook at seven &mdash; how should I get there?&rdquo;</div><div style="font-family:var(--serif); font-size:15px; line-height:21px; color:var(--ink); padding-top:6px;">The ferry, the B61, or a car. The last ferry back is 8:10, so if you go over on it you will want another way home.', "06.7 answer")
t = sub1(t, 'Still a good answer &middot; the checking is hers', 'Places checked tonight&rsquo;s sailings &middot; 4:02 pm', "06.7 receipt")
t = sub1(t, 'Not a failure &mdash; a good answer either way. The difference is one round of checking she now has to do herself, and one risk she has to think of. Personalized output does not have to win to be worth having.',
         'The same live check and the same warning: history does not unlock ordinary competence. What is missing is smaller and real &mdash; three options instead of one recommendation, and &ldquo;another way home&rdquo; instead of the two ways she has used. Had the answers come out the same, that would have been a fair result too.', "06.7 note")
save("06 - Give once, get value back.dc.html", t)

# ---------- 02.9 · name the actual consequence ----------
t = load("02 - An ordinary beginning.dc.html")
t = sub1(t, 'Nothing kept &middot; no entry made &middot; no interest recorded', 'Used what you said in September &middot; no new Life entry', "02.9 receipt")
t = sub1(t, 'The improvement is narrow and private: it does not re-ask what she has read, and it keeps to where the conversation left her. Nothing enters Life, no preference is inferred from a question, and she is not told the system remembered.',
         'The improvement is narrow and private: it does not re-ask what she has read, and it keeps to where the conversation left her. Earlier context is genuinely in play &mdash; the receipt says so rather than pretending otherwise &mdash; and the consequence it names is the real one: no new Life entry. No preference is inferred from a question and nothing is announced.', "02.9 note")
save("02 - An ordinary beginning.dc.html", t)
print("done")
