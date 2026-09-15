"""Build every Places board on the shared package vdl-stage1 0.3, then measure. One entry point, so no board is left stale."""
import re, subprocess, sys, os, json
BOARDS = ['00 - Index', '01 - The Field', '02 - The Journeys', '03 - The Situations', '04 - The Checks and the Opening', '05 - Decisions', '06 - Log', '07 - Components', '08 - The Page', '09 - Purposes', '10 - Scope and Selection']
LINKS = '<link rel="stylesheet" href="_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css" /><link rel="stylesheet" href="vdl.css" />'
# exact matches only: a Places literal becomes the kernel token of the same value (vdl-port's rule, applied rather than annotated)
TOK = [('#1B1714', 'var(--vk-ink00)'), ('#2C2622', 'var(--vk-ink20)'), ('#6E6862', 'var(--vk-ink60)'), ('#8F877C', 'var(--vk-color-surface-ghostAnchor)'), ('#B5AFA5', 'var(--vk-ink80)'),
       ('#B0853A', 'var(--vk-gold60)'), ('#8A6628', 'var(--vk-gold80)'), ('#4A3428', 'var(--vk-color-action-primary)'), ('#7A2E2E', 'var(--vk-color-surface-oxblood)'),
       ('#FBF7EC', 'var(--vk-paper00)'), ('#E8E2D4', 'var(--vk-paper30)'), ('#3D5066', 'var(--vk-color-surface-planningInk)'), ('#EFEAE0', 'var(--vk-paper20)'),
       ('rgba(27,23,20,0.10)', 'var(--vk-borderHairline)'), ('rgba(27,23,20,0.06)', 'var(--vk-borderHairlineSoft)')]
def tokenize(html):
    def one(m):
        v = m.group(1)
        for k, r in TOK: v = re.sub(re.escape(k), r, v, flags=re.I)
        return f'style="{v}"'
    return re.sub(r'style="([^"]*)"', one, html)
def post(html):
    if 'vdl.css' not in html: html = html.replace('<helmet>', '<helmet>' + LINKS, 1)
    html = html.replace('class="fn" style="', 'class="vdl-t-metaLine" style="color: #B5AFA5; ')
    return tokenize(html)
if __name__ == '__main__':
    for g in ['gen07.py', 'gen08.py', 'gen09.py', 'gen10.py', 'renumber.py']:
        r = subprocess.run([sys.executable, g], capture_output=True, text=True)
        if r.returncode: print(r.stderr[-1500:]); sys.exit(1)
        print(g, 'ok')
    for b in BOARDS:
        p = f'out2/{b}.dc.html'; h = open(p).read(); open(p, 'w').write(post(h))
    print('post-processed', len(BOARDS))
