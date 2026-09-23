import json, os, subprocess, sys
from measure import ink_end, CH
W = {"00 - Index": 1560, "01 - Design System": 1720, "02 - A - The Ordinary Opening": 1900, "03 - B - Something Saturday Evening": 1900, "04 - C - Through My People": 1900, "05 - D - Sorrento Before Arrival": 1900, "06 - E - Taking It Forward": 1900, "07 - The Supply-Rich Opening": 1900, "08 - Decisions and Reuse": 1720, "09 - Revision Log": 1560, "10 - Content-led vs Map-led": 1900, "11 - Two Paths": 3020, "P1 - Prototype - Two Paths": 1000}
GEN = {"02": "gen_p2_02.py", "07": "gen_p2_07.py", "04": "gen_p2_04.py", "06": "gen_p2_06.py", "03": "gen_p2_03.py", "05": "gen_p2_05.py", "01": "gen_p2_01.py", "08": "gen_p2_08.py", "00": "gen_p2_00.py", "09": "gen_p2_09.py", "10": "gen_p2_10.py", "11": "gen_p2_11.py", "P1": "gen_p2_11.py"}
OUT = 'places'; hp = os.path.join(OUT, 'heights.json')
names = sys.argv[1:]
H = json.load(open(hp))
for n in names: H[n[:2]] = 0
json.dump(H, open(hp, 'w'))
def regen():
    for n in names: subprocess.run(['python3', GEN[n[:2]]], check=True, stdout=subprocess.DEVNULL)
regen()
def shoot(n, h):
    subprocess.run([CH, '--headless=new', '--force-device-scale-factor=1', f'--window-size={W[n]},{h}', '--virtual-time-budget=9000', '--hide-scrollbars', f'--screenshot={OUT}/shots/{n[:2]}.png', f'file://{os.getcwd()}/{OUT}/{n}.dc.html'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for n in names: shoot(n, 12000)
for n in names:
    e = ink_end(f'{OUT}/shots/{n[:2]}.png'); H[n[:2]] = e + 30; print(n[:2], 'ink ends', e)
json.dump(H, open(hp, 'w')); regen()
for n in names: shoot(n, H[n[:2]])
print('final', {n[:2]: H[n[:2]] for n in names})
