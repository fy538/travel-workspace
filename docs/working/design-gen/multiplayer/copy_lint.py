"""Copy lint for the boards. Measures what kind of text sits inside phone frames and flags the habits the copy rules ban."""
import re, glob, sys, collections
from html.parser import HTMLParser
VOID={'br','img','input','meta','link','hr','path','circle','rect','line','source'}
class P(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.stack=[]; s.out=[]; s.skip=0
    def handle_starttag(s,tag,attrs):
        a=dict(attrs); st=a.get('style','') or ''; cl=(a.get('class','') or '').split()
        if tag in('svg','script','style'): s.skip+=1
        inp=any(x for x in s.stack); k=None
        if tag=='div' and st.startswith('width: 393px;') and 'dashed' not in st and ('min-height' in st or '#EFEAE0' in st): k='phone'
        elif inp and 'dashed' in st: k='annot'
        elif inp and 'fn' in cl: k='foot'
        elif inp and 'border-radius: 18px 18px' in st: k='human'
        if tag=='dc-import' and inp and a.get('name')=='OriginalReader': s.out.append(('human', a.get('words','')))
        if tag not in VOID: s.stack.append(k)
    def handle_endtag(s,tag):
        if tag in('svg','script','style'): s.skip=max(0,s.skip-1)
        if tag not in VOID and s.stack: s.stack.pop()
    def handle_data(s,d):
        t=' '.join(d.split())
        if s.skip or len(t)<3 or 'phone' not in s.stack: return
        k=next((x for x in reversed(s.stack) if x),None)
        if k=='phone': k='human' if '“' in t else ('label' if t.isupper() else 'product')
        s.out.append((k,t))
NARR=re.compile(r"\b(is|are|was) (never |not )?(told|notified|shown|contacted|suggested|matched|announced)\b|\b(nobody else|no one else|nothing (is|was|here|about)|does not (notify|tell)|not told|never told|sees nothing)\b",re.I)
TRI=re.compile(r"\b[Nn]o [^,.;]{2,40}, no [^,.;]{2,40}")
NOTX=re.compile(r"\bnot (checked|an?|the)\b|, not \w",re.I)
BRIT=re.compile(r"\b(recognis\w+|organis\w+|neighbourhood\w*|favour\w*|colour\w*|afterwards|whilst|realis\w+|summaris\w+|centre|ageing|learnt|caf&eacute;)\b",re.I)
UNC=re.compile(r"\b(it is|she is|he is|you are|they are|does not|do not|is not|are not|did not|will not|would not|has not|have not|that is|there is|cannot)\b",re.I)
REFLEX=re.compile(r"\b(Got it|Certainly|Of course|Happy to)\b")
W=lambda ts: sum(len(t.split()) for t in ts)
tot=collections.Counter(); bad=0
print(f"{'board':<6}{'product':>8}{'people':>8}{'boxes':>7}{'notes':>7}  flags")
for f in sorted([f for f in glob.glob('out/**/*.dc.html', recursive=True) if re.match(r'(D\d+|E\d+|03|04) ', f.split('/')[-1])], key=lambda x:(x.split('/')[-1][0], int(re.findall(r'\d+', x.split('/')[-1])[0]))):
    p=P(); p.feed(open(f).read()); by=collections.defaultdict(list)
    for k,t in p.out: by[k].append(t)
    allp=by['product']+by['foot']+by['annot']+by['label']
    fl=[]
    if by['annot']: fl.append(f"{len(by['annot'])} explainer box lines")
    for name,rx,src in (('narrates',NARR,allp),('no-x-no-y',TRI,allp),('negated-provenance',NOTX,by['foot']),('british',BRIT,allp+by['human']),('uncontracted',UNC,by['product']),('reflex',REFLEX,by['product'])):
        n=sum(1 for t in src if rx.search(t))
        if n: fl.append(f'{n} {name}')
    bad+=len(fl)
    b=f.split('/')[-1].split(' ')[0]
    for k in by: tot[k]+=W(by[k])
    print(f"{b:<6}{W(by['product']):>8}{W(by['human']):>8}{W(by['annot']):>7}{W(by['foot']):>7}  {'; '.join(fl) or 'clean'}")
T=sum(tot.values()) or 1
print(f"\nin-phone words {T}: product {100*tot['product']//T}% · people {100*tot['human']//T}% · explainer boxes {100*tot['annot']//T}% · mono notes {100*tot['foot']//T}% · labels {100*tot['label']//T}%")
