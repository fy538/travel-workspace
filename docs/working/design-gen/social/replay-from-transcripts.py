import json,os,subprocess,glob,re
ops=json.load(open('dd693465_ops.json'))
SE='/private/tmp/claude-501/-Users-feihuyan-Documents-Claude-travel-workspace/dd693465-9a7a-4a81-8b5c-b3e3dc5ad6a0/scratchpad/se'
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SKIP={117,122,138,139,140,141}
for f in glob.glob(SE+'/*.py'): os.remove(f)
H={}
for f in glob.glob('/Users/feihuyan/Downloads/vesper-social-experience/project/0[0-7] - *.dc.html'):
    s=open(f).read(); m=re.search(r'height:\s*(\d{4})px',s)
    if m: H[os.path.basename(f)[:2]]=int(m.group(1))
os.makedirs(SE+'/out/shots',exist_ok=True); json.dump(H,open(SE+'/out/heights.json','w'))
log=open('replay4.log','w')
for i,o in enumerate(ops):
    if i<80 or i in SKIP or (o['ts'] or '')<'2026-09-07T18:21': continue
    if o['t']=='Write':
        fp=o['fp']; os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w').write(o['inp']['content']); log.write(f'{i} W {fp}\n')
    elif o['t']=='Edit':
        fp=o['fp']; s=open(fp).read(); a=o['inp']['old_string']; b=o['inp']['new_string']
        if a not in s: log.write(f'{i} EDIT-MISS {fp}\n'); continue
        s=s.replace(a,b) if o['inp'].get('replace_all') else s.replace(a,b,1); open(fp,'w').write(s); log.write(f'{i} E {fp}\n')
    else:
        c=o['cmd']
        if i==125: c=f'cd {SE} && python3 patch16.py'
        if i==119: c=f'cd {SE} && python3 patch15.py'
        if i==100: c=c[c.index('cd /private/tmp'):]
        c=c.replace(CHROME,'/usr/bin/true')
        r=subprocess.run(['zsh','-c',c],capture_output=True,text=True,timeout=120)
        log.write(f'{i} B rc={r.returncode} '+c.split('&&',1)[-1].strip().replace('\n',' | ')[:120]+'\n'+(r.stderr[-400:]+'\n' if r.returncode else '')+(r.stdout[-400:]+'\n' if 'patch' in c else ''))
        for p in glob.glob(SE+'/out/shots/*.png'): os.remove(p)
log.close()
json.dump(H,open(SE+'/out/heights.json','w'))
