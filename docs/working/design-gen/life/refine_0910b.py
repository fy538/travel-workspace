#!/usr/bin/env python3
"""Sep 10 addendum: measured-overflow repairs on the six boards of the residual-corrections pass.

(a) Board 07 carried a real 1x horizontal overflow (389px nowrap caption inside a
    349px column) that predates this pass; the caption is shortened, not truncated.
(b) Four full-width mono caption lines are `.meta`/`.barmeta`, which is nowrap by
    design for inline stamps. Used as a whole-line caption they cannot wrap and
    overflow at 1.3x text. Only those instances are allowed to wrap; the shared
    class and every inline stamp are untouched.
"""
import os, sys

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def load(n): return open(os.path.join(SRC, n), encoding="utf-8").read()
def save(n, s): open(os.path.join(OUT, n), "w", encoding="utf-8").write(s)

def rep(t, a, b, n=1):
    c = t.count(a)
    assert c == n, f"expected {n} of {a[:70]!r}, found {c}"
    return t.replace(a, b)

F07 = "07 - The people in my life.dc.html"
F06 = "06 - Give once, get value back.dc.html"
F02 = "02 - An ordinary beginning.dc.html"

# ---- 07 -------------------------------------------------------------------
t = load(F07)
# (a) real 1x overflow: 58-char nowrap caption in a 349px column
t = rep(t,
    'HER NOTE &middot; SENT TO YOU AFTER SATURDAY&rsquo;S DINNER &middot; CITY-LEVEL',
    'HER NOTE &middot; AFTER SATURDAY&rsquo;S DINNER &middot; CITY-LEVEL')
# (b) let the two full-width note captions wrap at larger text
t = rep(t,
    '<div class="meta" style="padding-top:6px;">HER NOTE',
    '<div class="meta" style="padding-top:6px; white-space:normal;">HER NOTE')
t = rep(t,
    '<div class="meta" style="padding-top:6px;">HERS &middot; CITY-LEVEL',
    '<div class="meta" style="padding-top:6px; white-space:normal;">HERS &middot; CITY-LEVEL')
save(F07, t)

# ---- 06 -------------------------------------------------------------------
t = load(F06)
t = rep(t,
    '<span class="meta" style="padding-top:2px;">FROM THE SOURCE YOU SAVED',
    '<span class="meta" style="padding-top:2px; white-space:normal;">FROM THE SOURCE YOU SAVED')
save(F06, t)

# ---- 02 -------------------------------------------------------------------
t = load(F02)
t = rep(t,
    '<span class="barmeta" style="text-align:center; line-height:16px;">ASSET GAP',
    '<span class="barmeta" style="text-align:center; line-height:16px; white-space:normal;">ASSET GAP')
save(F02, t)

# ---- carry the untouched three through unchanged --------------------------
for n in ("P1 - What I keep ahead of me.dc.html",
          "P2 - Life changes without management.dc.html",
          "P3 - Something I deliberately saved.dc.html"):
    save(n, load(n))

print("ok ->", OUT)
