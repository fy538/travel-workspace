#!/usr/bin/env python3
"""Plans · adopt vdl-stage1 0.3 (2026-09-11). argv[1] = mirror dir, argv[2] = step (before|boards)."""
import sys, os, re, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vdl_adopt as V
S, step = sys.argv[1], sys.argv[2]
P = lambda f: os.path.join(S, f)
CHANGED = ['01 Baseline - The Itinerary Today', '02 A - A Loose Saturday', '03 B - A Planned Trip, Kyoto',
  '04 C - A Shared Afternoon and Dinner', '05 D - The Day Changes While People Move', '06 E - Overlap and the Four Doors',
  '08 Contextual Request - Resting, Active, Resolved', '09 Journeys - Value, Adapt, Coordinate',
  '11 Continuations - Keep, Guest, Incompatible, Conditional, After', '12 Brought In and Followed - Two Bounded Additions',
  '90 Appendix - Change States and Recovery', '91 Appendix - Coverage, Arrival, Peers', '92 Appendix - Interactive Prototype']

if step == 'before':
    assert 'vdl-stage1' not in open(P('kit/plans.css')).read(), 'kit already adopted — before copies would not be originals'
    shutil.copyfile(P('kit/plans.css'), P('kit/plans.before-vdl.css'))
    for n in CHANGED:
        h = open(P(n + '.dc.html')).read()
        assert 'href="vdl.css"' not in h, n + ' already adopted'
        h = h.replace('href="./kit/plans.css"', 'href="./kit/plans.before-vdl.css"')
        h = re.sub(r'(<div class="warn">)', r'\1BEFORE SHARED PACKAGE · FROZEN ORIGINAL KEPT AS THE BEFORE REFERENCE, 2026-09-11 · THE CURRENT BOARD IS “' + n.split(' - ')[0] + r'” · ', h, count=1)
        open(P('Before shared package - ' + n + '.dc.html'), 'w').write(h)
    print('before copies:', len(CHANGED), '+ kit/plans.before-vdl.css')
    sys.exit()

# ---------------- step: boards ----------------
def edit(f, pairs):
    t = open(P(f)).read()
    for a, b in pairs:
        assert a in t, (f[:12], a[:90]); t = t.replace(a, b, 1)
    open(P(f), 'w').write(t)

# 90 · J2c / J2d / J2e → the shared Notice (the states it was derived from)
N = '90 Appendix - Change States and Recovery.dc.html'
edit(N, [
 ('''              <div class="pending"><span class="dot3">···</span> Adding Isuien to Monday, around noon</div>
              <div class="quiet" style="padding:0;">Not on the plan yet. You can close this and come back; it finishes on its own.</div>
              <div class="chips"><div class="chip dis">Send</div><div class="chip quiet">Cancel</div></div>''',
  '''              <dc-import name="Notice" tone="pending" title="Adding Isuien to Monday, around noon" body="Not on the plan yet. You can close this and come back; it finishes on its own." secondary="Cancel" hint-size="353px,112px"></dc-import>'''),
 ('''              <div class="ans" style="color:var(--oxblood);">That didn’t save — the connection dropped. <span style="color:var(--ink);">Nothing on Monday changed.</span></div>
              <div class="chips"><div class="chip pri">Try again</div><div class="chip quiet">Not now</div></div>
              <div class="quiet" style="padding:0;">Your words are kept here if you come back later.</div>''',
  '''              <dc-import name="Notice" tone="failed" title="That didn’t save — the connection dropped." body="Nothing on Monday changed. Your words are kept here if you come back later." primary="Try again" secondary="Not now" hint-size="353px,124px"></dc-import>'''),
 ('''              <div class="pending"><span class="dot3">···</span> Checking whether Isuien was added</div>
              <div class="quiet" style="padding:0;">Your request is still here.</div>
              <div class="chips"><div class="chip dis">Try again</div><div class="chip quiet">Not now</div></div>''',
  '''              <dc-import name="Notice" tone="unknown" title="Checking whether Isuien was added" body="Your request is still here." secondary="Not now" hint-size="353px,100px"></dc-import>'''),
])
t = open(P(N)).read()
NOTE = {'J2c': ('pending', 'The in-flight state is the shared Notice (tone pending), with Cancel as its one action. The disabled Send is no longer drawn: the shared rule shows only actions that can run, and duplicate prevention stays a behaviour, not a greyed control.'),
        'J2d': ('failed', 'The known failure is the shared Notice (tone failed) with Try again and Not now — the only tone that offers a retry.'),
        'J2e': ('unknown', 'The unknown outcome is the shared Notice (tone unknown) with Not now; the held retry is not drawn, because the shared rule offers retry only on a known failure (workbench 02B). Retry stays held until the request is reconciled.')}
for fid, (tone, txt) in NOTE.items():
    i = t.index(f'<span class="n">{fid}</span>'); j = t.index('<div class="ann">', i); k = t.index('</div>', t.index('<div class="k">', j)) + 6
    t = t[:k] + f'\n          <p><b>Shared package, 2026-09-11.</b> {txt}</p>' + t[k:]
open(P(N), 'w').write(t)

# every product board: links, buttons, doors (92: the phone only; its research chrome stays board furniture)
for n in CHANGED:
    if n.startswith('12 '): continue          # board 12 is regenerated by gen_12.py, which applies the same helpers
    f = n + '.dc.html'; h = open(P(f)).read()
    h = V.adopt(h, stop_marker='RESEARCH CHROME' if n.startswith('92') else None)
    open(P(f), 'w').write(h)
for f in ['00 Start Here.dc.html', '07 Decisions, Mapping, Reuse.dc.html']:
    h = open(P(f)).read(); open(P(f), 'w').write(V.add_links(h))

# kit/plans.css · tokens from the shared kernel (exact matches only, old values kept as fallbacks)
K = P('kit/plans.css'); css = open(K).read()
MAP = {'--paper':'--vk-paper20','--paper-deep':'--vk-paper30','--card':'--vk-paper05','--card-warm':'--vk-paper00',
 '--ink':'--vk-ink00','--ink-soft':'--vk-ink20','--ink-2':'--vk-ink40','--mute':'--vk-ink60','--mute-soft':'--vk-ink80',
 '--gold':'--vk-gold60','--gold-deep':'--vk-gold80','--gold-soft':'--vk-gold40','--gold-light':'--vk-color-surface-goldLight',
 '--signature':'--vk-color-surface-signatureGold','--planning':'--vk-color-surface-planningInk','--planning-deep':'--vk-color-surface-planningInkDeep',
 '--oxblood':'--vk-color-surface-oxblood','--terracotta':'--vk-color-warning','--success':'--vk-color-success','--action':'--vk-color-action-primary',
 '--hairline':'--vk-borderHairline','--hair-thin':'--vk-borderHairlineSoft',
 '--serif':'--vk-font-serif','--sans':'--vk-font-sans','--mono':'--vk-font-mono',
 '--r-card':'--vk-radius-surfaceCard','--r-chip':'--vk-radius-chip','--r-action':'--vk-radius-cardAction','--r-input':'--vk-radius-input','--r-soft':'--vk-header-softSquareRadius'}
root_i = css.index(':root {'); root_j = css.index('}', root_i)
root = css[root_i:root_j]; n_mapped = 0
for loc, vk in MAP.items():
    m = re.search(r'(\n\s*' + re.escape(loc) + r':\s*)([^;]+);', root)
    assert m, loc
    root = root[:m.start()] + m.group(1) + f'var({vk}, {m.group(2).strip()});' + root[m.end():]; n_mapped += 1
local_left = [x for x in re.findall(r'\n\s*(--[a-z0-9-]+):', root) if x not in MAP]
css = css[:root_i] + root + css[root_j:]
css = css.replace('.seehere::after { content: \'→\'; }', '/* .seehere arrow: now the shared Door’s drawn arrow (.vdl-door, vdl.css) */')
css = ('/* ADOPTS vdl-stage1 0.3 (workbench c13ae951; every file consumed is byte-identical at 0.4) on kernel travel-app@e2e792913 tokens:80d0648dd300.\n'
       f' * Tokens: {n_mapped} re-pointed to exact kernel tokens with the former values as fallbacks; local, no kernel equivalent: {", ".join(local_left)}.\n'
       ' * Buttons and doors use the shared construction (.vdl-btn r16, .vdl-door). The .pl-* rules below are local TONES on that construction,\n'
       ' * reported to the shared owner as missing variants — not a second button. .chip stays only for board furniture (92 research chrome). */\n') + css
css += '''
/* ---------- shared package adoption · 2026-09-11 · local tones on .vdl-btn (missing shared variants, reported) ---------- */
.vdl-btn.pl-quiet { color: var(--mute); padding: 0 8px; }                       /* text action: Plans' drawn geometry kept so rows do not re-wrap */
.vdl-btn.pl-gold  { border-color: rgba(176,133,58,0.5); color: var(--gold-deep); } /* keep / retain */
.vdl-btn.pl-out   { color: var(--planning-deep); }                                 /* leaves Vesper for a provider */
.vdl-btn.pl-out::after { content: '↗'; font-size: 13px; }
.vdl-btn.pl-dis   { opacity: 0.45; pointer-events: none; }                         /* held, not runnable */
'''
open(K, 'w').write(css)
print('tokens re-pointed:', n_mapped, '· local:', local_left)
