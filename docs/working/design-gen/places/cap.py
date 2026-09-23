"""Served captures for matched before/after comparisons. The served board is the truth: it resolves the shared components."""
import subprocess, json, os, sys
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
def shot_url(url, W, H, out, budget=12000):
    subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size={W},{H}', f'--virtual-time-budget={budget}', f'--screenshot={out}', url], capture_output=True, timeout=180)
    return os.path.exists(out)
def compare(name, a, b, W, x, y, w, h, scale=0.6, la='BEFORE · before/', lb='AFTER · SHARED PACKAGE vdl-stage1 0.3'):
    """Two crops of the same region side by side, with labels. a and b are full-board PNGs at width W."""
    ab = os.path.abspath
    cell = lambda png, lab: (f'<div style="display:flex;flex-direction:column;gap:6px"><div style="font:700 11px/1 JetBrains Mono,monospace;letter-spacing:1px;color:#8A6628">{lab}</div>'
                             f'<div style="width:{w*scale:.0f}px;height:{h*scale:.0f}px;overflow:hidden;position:relative;border:1px solid rgba(27,23,20,.15)">'
                             f'<img src="file://{ab(png)}" style="position:absolute;left:{-x*scale:.0f}px;top:{-y*scale:.0f}px;width:{W*scale:.0f}px"></div></div>')
    html = f'<body style="margin:0;background:#F4F0E7"><div style="display:flex;gap:28px;padding:18px">{cell(a, la)}{cell(b, lb)}</div></body>'
    p = f'out2/_cmp_{name}.html'; open(p, 'w').write(html)
    out = f'out2/cmp_{name}.png'; CW, CHh = int(2 * w * scale + 28 + 40), int(h * scale + 60)
    subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files', f'--window-size={CW},{CHh}', '--virtual-time-budget=3000', f'--screenshot={ab(out)}', f'file://{ab(p)}'], capture_output=True, timeout=120)
    return out
if __name__ == '__main__':
    S = json.load(open('out2/_serve.json')); H = json.load(open('out2/_H.json'))
    names = {'01': '01 - The Field', '03': '03 - The Situations', '04': '04 - The Checks and the Opening', '07': '07 - Components', '08': '08 - The Page'}
    for k, b in names.items():
        W, h = H[b]
        for side in ('before', 'after'):
            ok = shot_url(S[side + k], W, h + 600, f'out2/cap_{side}{k}.png'); print(side + k, W, h + 600, ok)
