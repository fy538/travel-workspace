"""The Multiplayer copy lint, pointed at the Places boards. Same regexes and lanes; the only change is that Places' mono notes are
class="vdl-t-metaLine" (after the shared-package adoption) or class="fn", so both count as mono notes."""
import re, glob, collections, sys
sys.path.insert(0, '/Users/feihuyan/travel-workspace/docs/working/design-gen/multiplayer')
src = open('/Users/feihuyan/travel-workspace/docs/working/design-gen/multiplayer/copy_lint.py').read()
head = src[:src.index('W=lambda')]
head = head.replace("elif inp and 'fn' in cl: k='foot'", "elif inp and ('fn' in cl or 'vdl-t-metaLine' in cl): k='foot'")
exec(head)
W = lambda ts: sum(len(t.split()) for t in ts)
tot = collections.Counter(); per = []
NEG = re.compile(r"\b(not|no|never|nothing|nobody|none|without)\b", re.I)
for f in sorted(glob.glob('out2/*.dc.html')):
    b = f.split('/')[-1][:2]
    if b in ('05', '06'): continue
    p = P(); p.feed(open(f).read()); by = collections.defaultdict(list)
    for k, t in p.out: by[k].append(t)
    allp = by['product'] + by['foot'] + by['annot'] + by['label']
    fl = {}
    for name, rx, s in (('narrates', NARR, allp), ('no-x-no-y', TRI, allp), ('negated-provenance', NOTX, by['foot']), ('british', BRIT, allp + by['human']), ('uncontracted', UNC, by['product']), ('reflex', REFLEX, by['product'])):
        n = sum(1 for t in s if rx.search(t))
        if n: fl[name] = n
    neg_foot = sum(1 for t in by['foot'] if NEG.search(t))
    for k in by: tot[k] += W(by[k])
    per.append((b, W(by['product']), W(by['human']), W(by['foot']), len(by['foot']), neg_foot, fl))
print(f"{'board':<6}{'product':>8}{'people':>8}{'mono':>6}{'lines':>7}{'neg':>5}  flags")
for b, pw, hw, fw, fl_n, ng, fl in per: print(f"{b:<6}{pw:>8}{hw:>8}{fw:>6}{fl_n:>7}{ng:>5}  {'; '.join(f'{v} {k}' for k, v in fl.items()) or 'clean'}")
T = sum(tot.values()) or 1
print(f"\nin-phone words {T}: product {100*tot['product']//T}% · people {100*tot['human']//T}% · mono notes {100*tot['foot']//T}% · labels {100*tot['label']//T}% · explainer boxes {100*tot['annot']//T}%")
