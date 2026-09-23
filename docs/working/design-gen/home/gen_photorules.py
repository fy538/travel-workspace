"""09: the photograph rules row (09-08) — a graded reference image and the person's stacked pair, lifted from the polished 02.
Usage: python3 gen_photorules.py <polished_02> <in_09> <out_09>"""
import re, sys
h2 = open(sys.argv[1]).read(); f9 = open(sys.argv[2]).read()
SERIF = "'EB Garamond', Georgia, serif"; MUTE = '#6E6862'; PAPER = '#EFEAE0'; GOLDD = '#8A6628'
CAPTION = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;"
def unit_from(marker, start_pat='<div style="padding: 22px 22px 0 22px;">', end_pat='<div style="padding: 40px 22px 0 22px;">'):
    i = h2.find(marker); s = h2.rfind(start_pat, 0, i)
    # never run past the phone that holds the unit
    ps = h2.rfind('<div style="width: 393px; min-height: 0; background: #EFEAE0', 0, i); depth = 0; pe = len(h2)
    for m in re.finditer(r'<div\b|</div>', h2[ps:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0: pe = ps + m.start(); break
    ends = [x for x in (h2.find(end_pat, i), h2.find('<div style="flex-grow: 1;">', i)) if 0 < x < pe] + [pe]; return h2[s:min(ends)]
obs = unit_from('The wall under Sorrento is volcanic ash')
cmp_ = unit_from('Sorrento&rsquo;s cliff is volcanic; Amalfi&rsquo;s is limestone. You stood on both.')
def cell(u, cap, note): return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column; gap: 8px;"><div class="kick" style="color: {GOLDD};">{cap}</div>'
                                f'<div style="width: 393px; background: {PAPER}; padding: 0 0 22px; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: #1B1714;">{u}</div><div style="{CAPTION}">{note}</div></div>')
sec = ('<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">PHOTOGRAPHS &middot; THE RULES &middot; 2026-09-08</div>'
       f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">A treated image means reference; an untreated one means yours</div>'
       f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">Reference and world images are graded with one recipe (chroma to 72%, warmed, the page paper multiplied over), shown one per unit at column width and 3:2, no rounding, nothing on the image, the caption beneath. The person&rsquo;s own photographs are never colour-treated: handled only, one per unit or a matched pair stacked at the same crop. Never side-by-side thumbnails. A photograph appears only where it carries the point; where a schematic already does, it goes. Chosen on 13.</div></div>'
       '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">'
       + cell(obs, 'A REFERENCE IMAGE &middot; GRADED, FULL WIDTH, CAPTION BENEATH', 'The observation unit: one graded reference photograph at 3:2, the caption below it in serif, the credit in mono, then the schematic.')
       + cell(cmp_, 'THE PERSON&rsquo;S PAIR &middot; UNTREATED, STACKED, MATCHED', 'The comparison unit: the person&rsquo;s two photographs as a stacked pair at the same crop; slots until they exist, never graded when they do.') + '</div>')
open(sys.argv[3], 'w').write(sec); print('photo rules section written')
