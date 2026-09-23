"""Large-text sheet (2026-09-08): the six selected scrolls at 1.3× type, same 393px width, appended to 09 - Forms.
Usage: python3 gen_largetext.py <polished_dir> <out_dir>
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
def phone_regions(h):
    out = []
    for m in re.finditer(r'<div style="width: 393px;[^"]*background: #EFEAE0', h):
        s = m.start(); depth = 0; e = None
        for mm in re.finditer(r'<div\b|</div>', h[s:]):
            depth += 1 if mm.group() == '<div' else -1
            if depth == 0: e = s + mm.end(); break
        if e and not (out and s < out[-1][1]): out.append((s, e))
    return out
def selected_phones(path, n):
    h = open(path).read(); i = h.find('SELECTED &middot; THE CURRENT HOME SCROLLS')
    return [h[s:e] for s, e in phone_regions(h) if s > i][:n]
def scale(p, k=1.3):
    def fs(m): return f'font-size: {round(float(m.group(1)) * k, 1)}px'
    def lh(m): return f'line-height: {round(float(m.group(1)) * k, 1)}px'
    p = re.sub(r'font-size: ([\d.]+)px', fs, p); p = re.sub(r'line-height: ([\d.]+)px', lh, p)
    p = re.sub(r'font-size="(\d+)"', lambda m: f'font-size="{round(int(m.group(1)) * k, 1)}"', p)   # svg labels
    # the .fn / .kick / .kickm / .dayl classes carry their sizes in the board css; add an inline override so they scale too
    p = re.sub(r'class="fn"( style=")?', lambda m: f'class="fn" style="font-size: 13px; ' if m.group(1) else 'class="fn" style="font-size: 13px;"', p)
    return p
A = selected_phones(f'{IN}/02 - Persona A - The New Yorker.dc.html', 3); B = selected_phones(f'{IN}/03 - Persona B - Back from Europe.dc.html', 3)
caps = ['Ordinary · Sunday', 'Quiet · Thursday', 'Thin · unit study', 'Day zero · Friday', 'Returned · Wednesday', 'On the trip · Wednesday']
def col(p, cap): return f'<div style="width: 393px; flex: none; display: flex; flex-direction: column; gap: 8px;"><div class="kick" style="color: #8A6628;">{cap.upper()}</div>{scale(p)}</div>'
rows = ''.join(f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">{"".join(col(p, c) for p, c in grp)}</div>' for grp in (list(zip(A, caps[:3])), list(zip(B, caps[3:]))))
sec = ('<div style="margin-top: 60px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;">'
       '<div class="kick" style="color: #8A6628;">LARGE TEXT &middot; 1.3&times; &middot; THE SIX SELECTED SCROLLS &middot; 2026-09-08</div>'
       '<div style="font-family: \'EB Garamond\', Georgia, serif; font-weight: 600; font-size: 24px; line-height: 30px;">Every selected scroll at the largest common accessibility size, same width</div>'
       '<div style="font-size: 13.5px; line-height: 20px; color: #6E6862; max-width: 980px;">Type and leading scaled 1.3×, widths unchanged, so every unit shows how it reflows: what wraps, what stays on one line, what a bounded instrument does when its labels grow. Nothing was re-composed for this sheet; what breaks here is a defect in the unit, not in the sheet.</div></div>' + rows)
h = open(f'{IN}/09 - Forms.dc.html').read()
head = h[:h.find('<div style="width: 1560px')]
head = head.replace('09 &middot; FORMS', '09b &middot; FORMS &middot; CONTINUED')
extra = ''.join(open(f'{OUT}/{f}').read() for f in ('_strip_section.html', '_photo_section.html') if os.path.exists(f'{OUT}/{f}'))
board = ('<div style="width: 1560px; min-height: 6000px; background: #F4F0E7; box-sizing: border-box; padding: 40px 44px 60px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: #1B1714;">'
         '<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 26px;"><div class="kick">VESPER &middot; HOME &middot; 09b &middot; FORMS &middot; LARGE TEXT &middot; 2026-09-08</div>'
         '<div style="font-family: \'EB Garamond\', Georgia, serif; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">09b &middot; Forms, continued: the strip, the photographs, and large text</div>'
         '<div style="font-size: 14px; line-height: 21px; color: #6E6862; max-width: 980px;">A continuation of 09, kept as its own board so no board passes the 12,000px the runtime renders reliably. Three sheets added 2026-09-08: the temporal strip across its day, the photograph rules chosen on 13, and the six selected scrolls at 1.3&times;.</div></div>'
         + extra.replace('margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);', 'margin-top: 0;', 1) + sec + '</div>')
open(f'{OUT}/09b - Forms - Large Text.dc.html', 'w').write(head + board + '</x-dc></body></html>'); print('written 09b', len(A), len(B))
