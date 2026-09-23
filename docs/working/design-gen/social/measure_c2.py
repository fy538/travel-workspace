import json,os,subprocess,sys,urllib.parse
sys.path.insert(0,'/private/tmp/claude-501/-Users-feihuyan-Documents-Claude-travel-workspace/2f24dc15-f019-4b4a-9608-e0e947e79ef9/scratchpad/hp')
from measure import ink_end, CH
W={'02 - A little of your world':1820,'03 - An easier way to get together':2260,'04 - Something stays with us':2260,'05 - The important alternatives':2260,'06 - Connected route':1820,'07 - Decisions and return to the app':1820,'08 - Continuations':2260,'09 - Sending, access and control':2260,'10 - Photos, sent and received':2260}
names=sys.argv[1:]
HJ='out/heights.json'; H=json.load(open(HJ))
for n in names: H[n[:2]]=0
json.dump(H,open(HJ,'w')); [subprocess.run(['python3',g],stdout=subprocess.DEVNULL) for g in ('gen_c2.py','gen_c3.py','gen_c4.py','gen_c5.py','gen_c6.py','gen_c7.py','gen_c8.py')]
os.makedirs('out/shots',exist_ok=True)
def shoot(n,h): subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={W[n]},{h}','--virtual-time-budget=14000','--hide-scrollbars',f'--screenshot=out/shots/{n[:2]}.png','http://127.0.0.1:8766/'+urllib.parse.quote(n)+'.dc.html'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for n in names: shoot(n,12000)
for n in names: e=ink_end(f'out/shots/{n[:2]}.png'); H[n[:2]]=e+30; print(n[:2],'ink ends',e)
json.dump(H,open(HJ,'w')); [subprocess.run(['python3',g],stdout=subprocess.DEVNULL) for g in ('gen_c2.py','gen_c3.py','gen_c4.py','gen_c5.py','gen_c6.py','gen_c7.py','gen_c8.py')]
for n in names: shoot(n,H[n[:2]])
print('final',{n[:2]:H[n[:2]] for n in names})
