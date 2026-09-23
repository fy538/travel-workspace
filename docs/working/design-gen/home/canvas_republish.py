"""Rebuild the published canvas artifact (claude.ai/code artifact 790957aa) from the current boards, without the lost seed script.
The artifact keeps its whole state in <script id="appifact-doc"> as JSON: {title, content:{files:{...}}, comments}. We swap each
artboard's source for the current board, add new artboards (08c, 09b) at the foot of the reading page, and refresh heights.
Usage: python3 canvas_republish.py <artifact_html_in> <boards_dir> <out_html> [heights.json]
"""
import sys, json, re, os
src, boards, out = sys.argv[1:4]
MAP = {'Main.dc.html': '00 - Index', 'c01.dc.html': '01 - Parts', 'c02.dc.html': '02 - Persona A - The New Yorker', 'c03.dc.html': '03 - Persona B - Back from Europe', 'c04.dc.html': '04 - Persona C - New User', 'c05.dc.html': '05 - Wedge - Trip Forming', 'c06.dc.html': '06 - Places - From Friends', 'c07.dc.html': '07 - Ledger and Decisions', 'c08.dc.html': '08 - Seam with Life', 'c08b.dc.html': '08b - Seam with Life - Home to Life', 'c09.dc.html': '09 - Forms', 'c10.dc.html': '10 - States', 'c11.dc.html': '11 - Return and Continuity', 'c12.dc.html': '12 - Why This, Chat, and Degraded States'}
NEW = {'c08c.dc.html': '08c - Seam with Life - The Trip Day', 'c09b.dc.html': '09b - Forms - Large Text', 'c13.dc.html': '13 - Photograph Treatments', 'c14.dc.html': '14 - Three Ordinary Opens', 'c15.dc.html': '15 - Learning and Steering'}
h = open(src).read()
i = h.find('id="appifact-doc"'); s = h.find('>', i) + 1; e = h.find('</script>', s)
doc = json.loads(h[s:e]); files = doc['content']['files']
def dims(html):
    m = re.search(r'width: (\d{4})px; min-height: (\d{4,})px', html); return (int(m.group(1)), int(m.group(2))) if m else (None, None)
canvas = json.loads(files['canvas.json'])
by_file = {a['file']: a for a in canvas['artboards']}
for cf, name in {**MAP, **NEW}.items():
    p = os.path.join(boards, name + '.dc.html')
    if not os.path.exists(p): print('missing', name); continue
    html = open(p).read(); files[cf] = html; w, hh = dims(html)
    if cf in by_file:
        if hh: by_file[cf]['h'] = hh
        if w: by_file[cf]['w'] = w
    else:
        base = by_file.get({'c08c.dc.html': 'c08b.dc.html', 'c09b.dc.html': 'c09.dc.html', 'c13.dc.html': 'c12.dc.html', 'c14.dc.html': 'c13.dc.html', 'c15.dc.html': 'c14.dc.html'}[cf], {})
        a = {k: v for k, v in base.items()}; a.update({'file': cf, 'title': name.replace(' - ', ' · '), 'w': w, 'h': hh, 'x': base.get('x', 0), 'y': base.get('y', 0) + base.get('h', 0) + 160})
        canvas['artboards'].append(a); by_file[cf] = a; print('added artboard', cf, 'at', a['x'], a['y'])
files['canvas.json'] = json.dumps(canvas, ensure_ascii=False)
blob = json.dumps(doc, ensure_ascii=False).replace('<', '\\u003c')
open(out, 'w').write(h[:s] + blob + h[e:]); print('wrote', out, len(blob))
