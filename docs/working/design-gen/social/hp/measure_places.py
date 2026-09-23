import json, os, subprocess, sys
from measure import ink_end, CH
W = {"00 - Index": 1560, "01 - Design System": 1720, "02 - A - The Ordinary Opening": 1900, "03 - B - Something Saturday Evening": 1900, "04 - C - Through My People": 1900, "05 - D - Sorrento Before Arrival": 1900, "06 - E - Taking It Forward": 1900, "07 - The Supply-Rich Opening": 1900, "08 - Decisions and Reuse": 1720}
OUT = 'places'; hp = os.path.join(OUT, 'heights.json')
names = sys.argv[1:] or list(W)
H = json.load(open(hp)) if os.path.exists(hp) else {}
for n in names: H[n[:2]] = 0
json.dump(H, open(hp, 'w'))
subprocess.run(['python3', 'gen_placeskit.py'], check=True); subprocess.run(['python3', 'gen_places02.py'], check=True); subprocess.run(['python3', 'gen_places03.py'], check=True); subprocess.run(['python3', 'gen_places04.py'], check=True); subprocess.run(['python3', 'gen_places05.py'], check=True); subprocess.run(['python3', 'gen_places06.py'], check=True); subprocess.run(['python3', 'gen_places07.py'], check=True); subprocess.run(['python3', 'gen_places08.py'], check=True)
os.makedirs(f'{OUT}/shots', exist_ok=True)
def shoot(n, h):
    subprocess.run([CH, '--headless=new', '--force-device-scale-factor=1', f'--window-size={W[n]},{h}', '--virtual-time-budget=9000', '--hide-scrollbars', f'--screenshot={OUT}/shots/{n[:2]}.png', f'file://{os.getcwd()}/{OUT}/{n}.dc.html'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for n in names: shoot(n, 12000)
for n in names:
    e = ink_end(f'{OUT}/shots/{n[:2]}.png'); H[n[:2]] = e + 30; print(n[:2], 'ink ends', e)
json.dump(H, open(hp, 'w'))
subprocess.run(['python3', 'gen_placeskit.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places02.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places03.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places04.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places05.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places06.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places07.py'], stdout=subprocess.DEVNULL); subprocess.run(['python3', 'gen_places08.py'], stdout=subprocess.DEVNULL)
for n in names: shoot(n, H[n[:2]])
print('final', {n[:2]: H[n[:2]] for n in names})
