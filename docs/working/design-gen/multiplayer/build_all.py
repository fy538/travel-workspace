"""Generate every board and lay the output out the way the project is organized: five boards at the top, the eighteen
directions in directions/, and the copy board plus the method page in archive/."""
import subprocess, os, shutil, glob, json
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
GENS = ['gen_00', 'gen_01', 'gen_b1', 'gen_w1', 'gen_w2', 'gen_g5', 'gen_g6', 'gen_s1', 'gen_s2', 'gen_s4', 'gen_s6', 'gen_s8', 'gen_s9', 'gen_s12', 'gen_s13', 'gen_s14', 'gen_s15', 'gen_a0'] + [f'gen_d{i}' for i in range(1, 11)] + [f'gen_e{i}' for i in range(1, 9)]
for sub in ('archive/directions', 'archive'):
    shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True); os.makedirs(os.path.join(OUT, sub))
for f in glob.glob(os.path.join(OUT, '*.dc.html')): os.remove(f)
for g in GENS:
    r = subprocess.run(['python3', g + '.py'], cwd=HERE, capture_output=True, text=True)
    if r.returncode: raise SystemExit(f'{g} failed:\n{r.stderr[-800:]}')
# C1 is frozen: its BEFORE column must show the frames as they were on 2026-09-21, and the frame functions have since changed.
subprocess.run(['python3', 'gen_c1_frozen.py'], cwd=HERE, capture_output=True)
for f in glob.glob(os.path.join(OUT, '*.dc.html')):
    b = os.path.basename(f)
    if b[0] in 'DE' and b[1].isdigit(): shutil.move(f, os.path.join(OUT, 'archive', 'directions', b))
    elif not b.startswith(('10', '11', '13', '15', '16', '17', '18', '19', '20', '21')): shutil.move(f, os.path.join(OUT, 'archive', b))
shutil.copytree(os.path.join(HERE, 'frozen', 'copy'), os.path.join(OUT, 'archive', 'copy'))
tree = {d or '.': sorted(os.path.basename(x) for x in glob.glob(os.path.join(OUT, d, '*.dc.html'))) for d in ('', 'archive', 'archive/directions')}
for k, v in tree.items(): print(f'{k}: {len(v)}')
print('\n'.join('  ' + x for x in tree['.']))
