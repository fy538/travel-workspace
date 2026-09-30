"""22 · Type. The same three screens (a share, a kept collection, the timeline) set four ways, so the serif/sans pairing
can be judged by eye: A as drawn (EB Garamond), B the same face with body serif set ~15% larger, C Source Serif 4 and
D Newsreader at A's sizes. Lowercase heights at 16px were measured in headless Chrome on 2026-09-23 (canvas
actualBoundingBoxAscent of 'x' / font size). Nothing outside this board changes; the serif is canon across Life,
Places and Home."""
import re
from mp_kit2 import *
import gen_s1 as S
import gen_s12 as K
import gen_s13 as T

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400'
         '&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap">')
# B: Life's serif body classes, set ~15% larger inside the B column only
B_CSS = ('.tB .child{font-size:17px;line-height:23px}.tB .voice,.tB .cq{font-size:19.5px;line-height:26px}')
HEADT = HEAD_VDL.replace('</helmet>', f'{FONTS}<style>{B_CSS}</style>\n</helmet>', 1)

XH = {'EB Garamond': 40.5, 'Source Serif 4': 48.6, 'Newsreader': 44.0, 'System sans': 52.6}
STACK = {'EB Garamond': "'EB Garamond', Georgia, serif", 'Source Serif 4': "'Source Serif 4', Georgia, serif",
         'Newsreader': "'Newsreader', Georgia, serif", 'System sans': "-apple-system, BlinkMacSystemFont, system-ui, sans-serif"}

def scale_serif(h, f=1.15, cap=18):
    """Body serif only (inline sizes up to 18px); titles and display sizes stay as drawn."""
    def fix(m):
        st = m.group(1)
        if not re.search(r"--serif|EB Garamond|vk-font-serif", st): return m.group(0)
        fs = re.search(r'font-size:\s*([\d.]+)px', st)
        if not fs or float(fs.group(1)) > cap: return m.group(0)
        st = re.sub(r'(font-size|line-height):\s*([\d.]+)px', lambda k: f'{k.group(1)}:{round(float(k.group(2)) * f * 2) / 2:g}px', st)
        return f'style="{st}"'
    return re.sub(r'style="([^"]*)"', fix, h)

def swap(h, face):
    return h.replace("'EB Garamond'", f"'{face}'").replace('"EB Garamond"', f'"{face}"')

def crop(ph, h=640, off=0):
    return (f'<div style="width:393px; height:{h}px; overflow:hidden; position:relative; flex:none;">'
            f'<div style="margin-top:-{off}px;">{ph}</div>'
            f'<div style="position:absolute; left:0; right:0; bottom:0; height:90px; background:linear-gradient(rgba(216,209,197,0), #D8D1C5);"></div></div>')

def column(key, phones):
    if key == 'A': return phones
    if key == 'B': return [f'<div class="tB">{scale_serif(p)}</div>' for p in phones]
    face = {'C': 'Source Serif 4', 'D': 'Newsreader'}[key]
    var = f"--serif:'{face}',Georgia,serif; --vk-font-serif:'{face}',Georgia,serif;"
    return [f'<div style="{var}">{swap(p, face)}</div>' for p in phones]

# ── the specimen strip: the same word, the same size, four lowercase heights ──
def specimen(face, role):
    fs, base, w = 64, 84, 300
    xh = XH[face] / 100 * fs
    svg = (f'<svg width="{w}" height="104" viewBox="0 0 {w} 104" style="display:block;">'
           f'<line x1="0" x2="{w}" y1="{base}" y2="{base}" stroke="rgba(27,23,20,0.28)" stroke-width="1"/>'
           f'<line x1="0" x2="{w}" y1="{base - xh:.1f}" y2="{base - xh:.1f}" stroke="#B0853A" stroke-width="1" stroke-dasharray="3 3"/>'
           f'<text x="0" y="{base}" font-family="{STACK[face]}" font-size="{fs}" fill="#1B1714">broth</text></svg>')
    return (f'<div style="width:393px; flex:none;">'
            f'<div style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1.2px; color:#6E6862;">{role}</div>'
            f'<div style="font-family:{STACK[face]}; font-size:22px; line-height:28px; font-weight:600; margin-top:4px;">{face}</div>'
            f'<div style="margin-top:14px;">{svg}</div>'
            f'<div style="font-family:{STACK[face]}; font-size:16px; line-height:22px; margin-top:12px;">the broth is stupid good &middot; Hato &middot; 16px</div>'
            f'<div style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1px; color:#8A6628; margin-top:8px;">LOWERCASE {XH[face]:g}% OF THE SIZE</div></div>')

def colhead(k, title, sub):
    return (f'<div style="width:393px; flex:none;"><div class="ccap" style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1.2px; color:#8A6628;">{k}</div>'
            f'<div style="font-family:var(--serif); font-size:20px; line-height:26px; font-weight:600; margin-top:4px;">{title}</div>'
            f'<div style="font-size:13px; line-height:19px; color:#6E6862; margin-top:4px;">{sub}</div></div>')

def rowlabel(t):
    return (f'<div style="margin-top:34px; padding-top:10px; border-top:1px solid rgba(27,23,20,0.14); display:flex;">'
            f'<span style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1.3px; color:#6E6862;">{t}</span></div>')

def line(cells, top=14):
    return f'<div style="display:flex; gap:40px; align-items:flex-start; margin-top:{top}px;">' + ''.join(cells) + '</div>'

def build():
    screens = [('THE SHARE &middot; BOARD 01 &middot; A PERSON&rsquo;S WORDS IN SANS, THE PLACE IN SERIF', crop(S.d_receive(), 600)),
               ('A KEPT COLLECTION &middot; BOARD 08 &middot; SERIF ROWS, MONO COUNTS', crop(K.our_ny(), 700)),
               ('THE TIMELINE &middot; BOARD 09 &middot; SERIF NAMES AND WORDS, A PLACE CARD, A TICKET', crop(T.ny(), 740, 232))]
    cols = {k: column(k, [s[1] for s in screens]) for k in 'ABCD'}
    heads = line([colhead('A &middot; NOW', 'EB Garamond, as drawn', 'Rows 15px, words 16px, next to a 15&ndash;17px system sans.'),
                  colhead('B &middot; THE RULES', 'EB Garamond, set larger', 'Body serif about 15% larger (rows 17px, words 18.5px); titles unchanged. Each face one job.'),
                  colhead('C &middot; A SCREEN SERIF', 'Source Serif 4', 'A&rsquo;s sizes, unchanged. Made for screens; the lowercase is close to the sans&rsquo;s.'),
                  colhead('D &middot; A SCREEN SERIF', 'Newsreader', 'A&rsquo;s sizes, unchanged. Editorial, a little warmer than C; between A and C in size.')], top=0)
    rows = ''.join(rowlabel(t) + line([cols[k][i] for k in 'ABCD']) for i, (t, _) in enumerate(screens))
    spec = (rowlabel('THE SAME WORD AT THE SAME SIZE &middot; GOLD DASHES MARK THE TOP OF THE LOWERCASE')
            + line([specimen('EB Garamond', 'THE SERIF NOW'), specimen('System sans', 'THE SANS'),
                    specimen('Source Serif 4', 'CANDIDATE'), specimen('Newsreader', 'CANDIDATE')], top=16))
    n = notes('WHAT TO LOOK AT', led([
        ('SAME SIZE?', 'Where a serif line sits under or beside a sans line, do they read as the same size? In A the serif reads a size smaller: its lowercase is 40% of the font size against the sans&rsquo;s 53%.'),
        ('SMALL ROWS', 'Do the 15px rows on the kept collection feel thin? Garamond was drawn for print; its strokes are fine at book sizes and light on a phone.'),
        ('STILL LIFE?', 'Does C or D still feel like Life: editorial, warm, a held record rather than an app? That is what the serif is for.'),
        ('UNCHANGED', 'The sans (system) and the mono (JetBrains Mono) are the same in all four columns.'),
        ('SCOPE', 'The serif is canon for Life, Places and Home. This board changes nothing else; a change here would be a canon decision.'),
    ]), w=1692)
    html = (HEADT + f'<div style="width: 1788px; min-height: {hh("11", 3000)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 48px 36px 48px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('11 &middot; TYPE', 'The serif and the sans, four ways',
                   'Decided September 26: EB Garamond stays; the typeface canon is unchanged. Kept for reference: the same three screens in Garamond, Garamond larger, and two screen serifs.')
            + spec + f'<div style="margin-top:44px;">{heads}</div>' + rows
            + f'<div style="margin-top:40px;">{n}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('11 - Type', html)

if __name__ == '__main__':
    build()
