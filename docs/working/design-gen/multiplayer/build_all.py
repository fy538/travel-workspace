"""Generate the twelve boards of the project (00-11) into out/. The archive (00-06 doctrine boards, A0, C1, the D/E
directions) was deleted from the Design project on 2026-09-23; its generators (gen_00, gen_01, gen_a0, gen_b1, gen_c1*,
gen_d*, gen_e*, gen_g*, gen_w*, gen_r1) are kept for history but still write the OLD names and are not built here."""
import subprocess, os, glob
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
GENS = ['gen_idx', 'gen_s1', 'gen_s2', 'gen_s15', 'gen_s14', 'gen_s4', 'gen_s8', 'gen_s6', 'gen_s12', 'gen_s13', 'gen_s9', 'gen_t1']
os.makedirs(OUT, exist_ok=True)
for f in glob.glob(os.path.join(OUT, '*.dc.html')): os.remove(f)
for g in GENS:
    r = subprocess.run(['python3', g + '.py'], cwd=HERE, capture_output=True, text=True)
    if r.returncode: raise SystemExit(f'{g} failed:\n{r.stderr[-800:]}')
print('\n'.join(sorted(os.path.basename(x) for x in glob.glob(os.path.join(OUT, '*.dc.html')))))
