import json,os,subprocess,sys,urllib.parse
sys.path.insert(0,'/private/tmp/claude-501/-Users-feihuyan-Documents-Claude-travel-workspace/2f24dc15-f019-4b4a-9608-e0e947e79ef9/scratchpad/hp')
from measure import ink_end, CH
W={'00 - Start Here':1560,'01 - Checkpoint 1 - Cast, Ledger, Sequence':2200}
HJ='out/heights.json'; H=json.load(open(HJ)) if os.path.exists(HJ) else {}
for n in W: H[n[:2]]=0
json.dump(H,open(HJ,'w')); subprocess.run(['python3','gen_se.py'],stdout=subprocess.DEVNULL)
os.makedirs('out/shots',exist_ok=True)
def shoot(n,h): subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={W[n]},{h}','--virtual-time-budget=14000','--hide-scrollbars',f'--screenshot=out/shots/{n[:2]}.png','http://127.0.0.1:8766/'+urllib.parse.quote(n)+'.dc.html'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for n in W: shoot(n,12000)
for n in W: e=ink_end(f'out/shots/{n[:2]}.png'); H[n[:2]]=e+30; print(n[:2],'ink ends',e)
json.dump(H,open(HJ,'w')); subprocess.run(['python3','gen_se.py'],stdout=subprocess.DEVNULL)
for n in W: shoot(n,H[n[:2]])
print('final',H)
