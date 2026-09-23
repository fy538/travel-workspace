# -*- coding: utf-8 -*-
"""Sep 9 pass (handoff §0 "payoff and reconciliation"): asserted edits on the current export.
Run: python3 refine_0909.py <srcdir> <outdir>"""
import sys, os
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, t): open(os.path.join(OUT, n), "w", encoding="utf-8").write(t); print("wrote", n, len(t))
def subn(t, a, b, n, name=""):
    assert t.count(a) == n, f"{name or a[:60]!r}: found {t.count(a)} (expected {n})"; return t.replace(a, b)
def sub1(t, a, b, name=""): return subn(t, a, b, 1, name)
def append_before_end(t, block):
    i = t.rfind('</div>\n</x-dc>'); assert i > 0; return t[:i] + block + t[i:]

# ---------- 02 · formation promise ----------
t = load("02 - An ordinary beginning.dc.html")
t = subn(t, 'Two weeks in &mdash; the record grows as you live it, not as you feed it.', 'Two weeks in &mdash; a dinner, a coffee, a Saturday: what you gave it, held.', 2, "02 thin voice ×2")
t = sub1(t, 'The record grows as you live it, not as you feed it.', 'It will hold what you give it &mdash; a ticket, a photograph, a line worth keeping.', "02 zero line")
t = sub1(t, 'The only residue is the sentence the person chose to keep. That is the bakery row on the week above &mdash; and the whole of how it got there.',
           'The only residue is the sentence the person chose to keep &mdash; that is the bakery row on the week above. This is the valid minimum, not the whole model: relevant ordinary conversation may one day improve later help under an optional agreement (accepted direction, retention terms pending); nothing here draws per-turn saving or changes what a question leaves behind.', "02.5 note")
save("02 - An ordinary beginning.dc.html", t)

# ---------- 06 · the later value, made satisfying ----------
t = load("06 - Give once, get value back.dc.html")
t = sub1(t, 'Starch concentration and temperature change how the cheese proteins clump and how the sauce holds. That is a mechanism, not a verdict on any kitchen &mdash; it says nothing about why all three plates tasted as they did. If you want to see it, one at-home comparison with a single variable would.',
           'Beyond the emulsion you noticed: the cheese proteins clump when the water is too hot or too thin in starch &mdash; so &ldquo;creamy&rdquo; is the sauce holding together, not just fat blending in. That is why it sometimes breaks. It says nothing about what any kitchen did. To see it, if you ever want to: two plates from one pot, one finished on the heat and one off it &mdash; the off-heat plate should stay smooth.', "06 sub")
t = sub1(t, 'After Rome and a saved read, the record returns a bounded mechanism &mdash; why &ldquo;creamy&rdquo; is partly about stability &mdash; and one optional way to see it for yourself. It does not claim to know what any kitchen did.',
           'After Rome and a saved read, the record returns what the first answer could not: why a creamy sauce breaks &mdash; heat and starch concentration decide whether the cheese clumps &mdash; and, if wanted, one two-plate comparison that would show it. It does not claim to know what any kitchen did.', "06 para")
t = sub1(t, 'What is new versus the Aug 17 answer: a supported mechanism from the saved source (starch, temperature, protein stability) and a transferable one-variable test &mdash; not a repeat of the emulsion guess, and not certainty about the kitchens. Fixture C05.',
           'What is new versus Aug 17: the first answer said the finish was an emulsion; the Return explains why such a sauce holds or breaks (protein clumping under heat and thin starch) &mdash; the thing worth knowing next time. The two-plate comparison is optional and names what it would reveal: temperature, not the cheese. Fixture C05; source EXT-CACIO-E-PEPE.', "06 note")
t = sub1(t, 'FROM THE SOURCE YOU SAVED &middot; YOUR THREE PLATES ARE THE OCCASION, NOT THE PROOF', 'FROM THE SOURCE YOU SAVED &middot; AFTER THREE PLATES', "06 meta")
save("06 - Give once, get value back.dc.html", t)

# ---------- P3.4 / P3.5 · timestamps, changed facts, destinations ----------
t = load("P3 - Something I deliberately saved.dc.html")
t = sub1(t, '>AS HOME SHOWED IT &middot; 8:40 THIS MORNING</span><span class="barmeta" style="margin-left:auto;">A READING, NOT THE PLAN</span>', '>THIS MORNING &middot; 8:40</span><span class="barmeta" style="margin-left:auto;">WHAT HOME SHOWED</span>', "P3 capture bar")
t = sub1(t, '>SINCE THEN</span><span class="barmeta" style="margin-left:auto;">THE PLAN IS THE AUTHORITY</span>', '>CHANGED SINCE</span><span class="barmeta" style="margin-left:auto;">3:10 PM</span>', "P3 since bar")
t = sub1(t, 'The boat moved to 12:40 &middot; changed 3:10 pm</span><span class="meta">IN THE PLAN</span>', 'The boat &middot; now 12:40, was 11:20</span><span class="meta">3:10 PM</span>', "P3 boat row")
t = sub1(t, '<span class="door">Open the current plan &rarr;</span>', '<span class="door">Today&rsquo;s plan, as it is now &rarr;</span>', "P3 door")
t = sub1(t, '<div class="voice" style="margin:14px 22px 0 22px;">Ask about today uses the plan as it is now, not this morning&rsquo;s reading.</div>', '', "P3 ask voice")
t = sub1(t, 'NO CONNECTION &middot; 9:15 PM &middot; WHAT FOLLOWS IS WHAT THE PHONE HOLDS', 'NO CONNECTION &middot; 9:15 PM', "P3 offline banner")
t = sub1(t, '>YOUR ORIGINALS</span><span class="barmeta" style="margin-left:auto;">READABLE</span>', '>YOUR ORIGINALS</span><span class="barmeta" style="margin-left:auto;">ON THIS PHONE</span>', "P3 originals bar")
t = sub1(t, '>THE PLAN</span><span class="barmeta" style="margin-left:auto;">LAST KNOWN &middot; 3:10 PM</span>', '>TODAY&rsquo;S PLAN</span><span class="barmeta" style="margin-left:auto;">AS OF 3:10 PM</span>', "P3 plan bar")
t = sub1(t, 'Whether it has changed since can&rsquo;t be checked now.', 'Not updated since 3:10 pm.', "P3 offline note")
t = sub1(t, 'adopt the three-part reading &mdash; what Home showed (captured, dated), what the plan says now (the authority, one door), and what the phone holds when disconnected (originals readable, shared state last-known, freshness withheld)? <b style="color:var(--gold-deep)">Recommended:</b> adopt; Home 08c relabels its strip as a reading, the Plan lane owns the continuation, custody and retention unchanged.',
           'adopt the three-part page &mdash; this morning&rsquo;s strip with its time, what changed since with its time and one door to today&rsquo;s plan, and the disconnected version (originals on the phone, the plan as of its last update, nothing guessed)? <b style="color:var(--gold-deep)">Recommended:</b> adopt; Home 08c carries the same 8:40 time on its strip, Plans owns the change and the door&rsquo;s destination, custody and retention unchanged. Ownership is stated here, not on the phone.', "P3 decision")
t = sub1(t, 'Home 08c sends &ldquo;Today, as it stands&rdquo; here. The capture keeps its time; the plan&rsquo;s later change is a separate section with one door to the plan itself. Ask never operates on the 8:40 reading.',
           'Home 08c sends &ldquo;Today, as it stands&rdquo; here. Every fact carries its time; the change is a row with the old and new values; one door goes to the plan. Ask from this page binds to the plan as it is now &mdash; a behavior, not a line of copy.', "P3.4 note")
t = sub1(t, 'Originals read; the last-known plan state carries its time; freshness is withheld rather than guessed. No cached material is hidden and no shared state is promised current.',
           'Originals read; the plan shows its last update time; nothing is guessed about what changed after. No cached material is hidden and no shared state is promised current.', "P3.5 note")
save("P3 - Something I deliberately saved.dc.html", t)

# ---------- 07 + 03 · shared vs kept, on the shared record's lane ----------
for n in ["07 - The people in my life.dc.html", "03 - Open something in my life.dc.html"]:
    t = load(n)
    k = t.count('Sent to you, for the heat conversation &middot; city-level only')
    t = subn(t, 'Sent to you, for the heat conversation &middot; city-level only', 'Sent to you Sunday &middot; reachable while she shares it &middot; city-level', k, f"{n} note lane")
    k2 = t.count('From Saturday&rsquo;s dinner &middot; shared with everyone who was there')
    t = subn(t, 'From Saturday&rsquo;s dinner &middot; shared with everyone who was there', 'Shared to the dinner &middot; kept by you Aug 30, under her grant', k2, f"{n} photo lane")
    save(n, t)
print("done")
