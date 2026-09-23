"""13 - Photograph Treatments (2026-09-08): the same two photographs under eight photographic treatments (no halftone, no
spot colour), inside a phone-width unit, plus the handling variants (full-width single, matched diptych).
Usage: python3 gen_photo.py <push_dir> <out_dir>
"""
import re, sys, os
IN, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
G = '/Users/feihuyan/travel-workspace/docs/working/design-gen/home/gen_trip.py'
src = open(G).read().split("# ---- board edits")[0]
sys.argv = ['x', IN, OUT]; exec(src.replace("LIVE, OUT = sys.argv[1], sys.argv[2]\nos.makedirs(OUT, exist_ok=True)", "LIVE, OUT = sys.argv[1], sys.argv[2]"))
h8 = open(f'{IN}/08b - Seam with Life - Home to Life.dc.html').read()
srcs = []
for m in re.finditer(r'<img[^>]+src="(data:image/[^"]+)"', h8):
    if m.group(1) not in srcs: srcs.append(m.group(1))
SORRENTO, POSITANO = srcs[0], srcs[1]
CAPTION = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; font-size: 12px; line-height: 17px; letter-spacing: 0; color: #6E6862; max-width: 393px;"
GRAIN = ('<svg width="0" height="0" style="position: absolute;"><filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>'
         '<feColorMatrix type="matrix" values="0 0 0 0 0.5  0 0 0 0 0.45  0 0 0 0 0.4  0 0 0 0.9 0"/></filter></svg>')
# each treatment: (name, css filter on the img, list of overlay layers (background, blend, opacity), extra)
T = [
    ('As it is', 'none', [], ''),
    ('Quiet', 'saturate(0.6) contrast(0.92) brightness(1.03)', [], ''),
    ('Warm paper', 'saturate(0.72) sepia(0.22) contrast(0.95)', [('#EFEAE0', 'multiply', 1.0)], ''),
    ('Warm monotone', 'grayscale(1) sepia(0.55) saturate(1.1) contrast(1.0) brightness(1.03)', [('#B0853A', 'soft-light', 0.35)], ''),
    ('Print', 'contrast(0.86) brightness(1.06) saturate(0.82)', [('radial-gradient(ellipse at center, rgba(27,23,20,0) 55%, rgba(27,23,20,0.28) 100%)', 'normal', 1.0)], 'grain'),
    ('Gold wash', 'saturate(0.78) contrast(0.96)', [('#B0853A', 'soft-light', 0.5)], ''),
    ('Ink', 'grayscale(1) contrast(1.18) brightness(0.98)', [], ''),
    ('Pulled warm', 'hue-rotate(-14deg) saturate(0.62) contrast(0.94) sepia(0.14)', [], ''),
]
def photo(src_, filt, layers, extra, w=349, hgt=220, radius=8, pos='center'):
    inner = f'<img src="{src_}" style="display: block; width: 100%; height: 100%; object-fit: cover; object-position: {pos}; filter: {filt};">'
    for bg, blend, op in layers:
        inner += f'<div style="position: absolute; inset: 0; background: {bg}; mix-blend-mode: {blend}; opacity: {op}; pointer-events: none;"></div>'
    if extra == 'grain':
        inner += f'<svg style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.16; mix-blend-mode: multiply;"><rect width="100%" height="100%" filter="url(#grain)"/></svg>'
    return f'<div style="position: relative; width: {w}px; height: {hgt}px; border-radius: {radius}px; overflow: hidden; isolation: isolate;">{inner}</div>'
def unit(title, ph, cap, recipe, note, wide=False):
    return (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column; gap: 8px;">'
            f'<div style="width: 393px; background: {PAPER}; padding: 20px 22px 22px; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">'
            f'<div style="font-family: {SERIF}; font-size: 17px; line-height: 22px; font-weight: 500; color: {INK}; text-wrap: balance;">{title}</div>'
            f'<div style="margin-top: 10px;">{ph}</div>{fn(cap, 6)}</div>'
            f'<div class="fn" style="color: {GOLDD};">{recipe}</div><div style="{CAPTION}">{note}</div></div>')
TITLE = 'Forty minutes down the coast: no wall, no shelf, a slope into deep water'
CAP = 'REFERENCE PHOTOGRAPH &middot; WIKIMEDIA COMMONS &middot; G. MACLARTY &middot; CC BY 2.0'
TITLE2 = 'The wall under the town is volcanic ash, laid down across the bay and now soft rock'
CAP2 = 'REFERENCE PHOTOGRAPH &middot; WIKIMEDIA COMMONS &middot; P. A. LECLERCQ &middot; CC BY-SA 4.0'
NOTES = ['The control: full chroma, the only saturated blue and green on the page.', 'Chroma pulled to 60%, contrast eased. The picture stops shouting; the sea is still the sea.',
         'Desaturated and warmed, then the page paper multiplied over it: whites become paper, the photograph joins the field.', 'Monotone in the board\'s warm brown, a touch of gold in the midtones. Not a halftone; a smooth print.',
         'Lifted blacks, softened contrast, a fine grain and a slight vignette: a print, not a screen.', 'Full image under a gold soft-light wash: one cast across every photograph on the page.',
         'Ink only, contrast raised: documentary. Loses the blue that says "sea".', 'Blues rotated toward grey-teal, chroma down: the stone warms, the water stops being sky-blue.']
def rowdiv(kick, title, sub):
    return (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: #8A6628;">{kick}</div>'
            f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 24px; line-height: 30px;">{title}</div><div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">{sub}</div></div>')
def grid(cells, per=4):
    out = ''
    for i in range(0, len(cells), per): out += '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cells[i:i+per]) + '</div>'
    return out
row1 = [unit(TITLE, photo(POSITANO, f, l, x), CAP, f'{n.upper()} &middot; filter: {f}' + (' &middot; overlay ' + ', '.join(f"{b} {m} {o}" for b, m, o in l) if l else '') + (' &middot; grain' if x else ''), note) for (n, f, l, x), note in zip(T, NOTES)]
row2 = [unit(TITLE2, photo(SORRENTO, f, l, x), CAP2, n.upper(), 'The same recipe on the other photograph; a treatment has to hold across pictures, not flatter one.') for (n, f, l, x) in [T[1], T[2], T[3], T[4]]]
tw = T[2]
row3 = [unit('The wall under the town, and the slope forty minutes on', photo(SORRENTO, tw[1], tw[2], tw[3], 349, 420, 0, 'center 40%'), CAP2 + ' &middot; FULL WIDTH, 4:5, NO RADIUS', 'HANDLING A &middot; ONE PHOTOGRAPH, FULL WIDTH', 'One photograph as the unit\'s large moment: column width, a taller ratio, no rounding, nothing on it, caption beneath.'),
        unit('Sorrento&rsquo;s cliff is volcanic; Amalfi&rsquo;s is limestone', photo(SORRENTO, tw[1], tw[2], tw[3], 349, 170, 6, 'center 45%') + '<div style="height: 6px;"></div>' + photo(POSITANO, tw[1], tw[2], tw[3], 349, 170, 6, 'center 60%'), 'TUFF, THEN LIMESTONE &middot; THE SAME CROP, THE SAME LIGHT', 'HANDLING B &middot; A MATCHED DIPTYCH, STACKED', 'Two photographs only as a pair: same width, same ratio, same treatment, stacked so the eye compares rock with rock.'),
        unit('Sorrento&rsquo;s cliff is volcanic; Amalfi&rsquo;s is limestone', '<div style="display: flex; gap: 8px;">' + photo(SORRENTO, tw[1], tw[2], tw[3], 170, 118, 8, 'center 45%') + photo(POSITANO, tw[1], tw[2], tw[3], 171, 118, 8, 'center 60%') + '</div>', 'THE CURRENT PAIR, TREATED', 'HANDLING C &middot; THE CURRENT PLATES, SAME TREATMENT', 'The current side-by-side thumbnails with the warm-paper treatment: better, still the arrangement that reads as two stamps.')]
head = h8[:h8.find('<div style="width: 2480px')]
board = (f'<div style="width: 1820px; min-height: 4000px; background: #F4F0E7; box-sizing: border-box; padding: 40px 44px 60px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif; color: {INK};">' + GRAIN
         + f'<div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 26px;"><div class="kick">VESPER &middot; HOME &middot; 13 &middot; PHOTOGRAPH TREATMENTS &middot; EXPLORATION &middot; 2026-09-08</div>'
         f'<div style="font-family: {SERIF}; font-weight: 600; font-size: 30px; line-height: 36px; letter-spacing: -0.01em;">13 &middot; What a photograph has to do to belong on this page</div>'
         f'<div style="font-size: 14px; line-height: 21px; color: {MUTE}; max-width: 980px;">The same two reference photographs, inside the same phone-width unit, under eight photographic treatments: none of them halftone or spot colour, all of them done to the picture as a print would be (chroma, warmth, contrast, grain, a wash). Then the handling: how one photograph should sit, and how a pair should. Nothing here is adopted; it is a sheet to choose from. CSS filters and blend layers, so any choice is a recipe, not an asset.</div></div>'
         + rowdiv('ROW ONE &middot; EIGHT TREATMENTS, ONE UNIT', 'The Positano photograph, eight ways', 'Left to right, top to bottom: the control, then chroma pulled, warmed into paper, warm monotone, print, gold wash, ink, and blues pulled warm.') + grid(row1)
         + rowdiv('ROW TWO &middot; THE OTHER PHOTOGRAPH', 'The same four recipes on the Sorrento wall', 'A treatment is only a treatment if it holds across pictures.') + grid(row2)
         + rowdiv('ROW THREE &middot; HANDLING', 'How a photograph sits, once it is treated', 'The warm-paper recipe carried into the three arrangements that matter: one full-width, a matched pair, and the current thumbnails for comparison.') + grid(row3, 3) + '</div>')
open(f'{OUT}/13 - Photograph Treatments.dc.html', 'w').write(head + board + '</x-dc></body></html>'); print('13 written')
