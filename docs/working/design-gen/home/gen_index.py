"""00 - Index rows for the boards added on 09-08 (08c, 09b, 13). Usage: python3 gen_index.py <polished_00> <out_00>"""
import re, sys
g = open(sys.argv[1]).read()
ROWS = [('>08b - Seam with Life - Home to Life<', '08c - Seam with Life - The Trip Day', 'The ninth whole encounter: the trip-day scroll, the same day after the operator moved the boat, the day page it opens (Life P3.4), the boat from the receipt, the claim from the money row, and what Home does not do', 'New · 09-08'),
        ('>09 - Forms<', '09b - Forms - Large Text', 'Forms, continued: the temporal strip across its day, the photograph rules (reference images graded, the person\'s own untreated), and the six selected scrolls at 1.3× type', 'New · 09-08'),
        ('>12 - Why This, Chat, and Degraded States<', '15 - Learning and Steering', 'Second pass (09-09), two experience comparisons: the same Tuesday content taught by a demonstration and by an ordinary control, plus the secondary-question route that 12 sends through "Why this"; and one subject steered by a spoken instruction, its result, a later encounter and what the instruction did not become', 'Second pass · 09-09 · proposed'),
        ('>12 - Why This, Chat, and Degraded States<', '14 - Three Ordinary Opens', 'Consolidation pass (09-08, revised 09-09): a newcomer across three opens on the supply set Places 03.3 draws and dates as the pair with this board; the first open drawn twice to compare which statement owns the headline, the third twice to tell an honest ending from an unseen part of a seen item; and the same Sunday evening under three kinds of wanted help. PROPOSED stress case, not the Home model', 'Consolidation pass · 09-08 · proposed'),
        ('>12 - Why This, Chat, and Degraded States<', '13 - Photograph Treatments', 'Exploration: the same two reference photographs under eight photographic treatments and three handlings. Warm paper chosen for reference images; the person\'s own photographs stay untreated', 'Exploration · 09-08 · warm paper chosen')]
for key, newname, desc, status in ROWS:
    if newname in g: continue
    i = g.find(key); j = g.find('</tr>', i) + 5; row = g[g.rfind('<tr>', 0, i):j]
    new = row.replace(key[1:-1], newname)
    new = re.sub(r'(<td[^>]*>)(?!0[89][bc]|13 |14 |15 )[^<]*(</td><td[^>]*>)[^<]*(</td></tr>)$', lambda m: m.group(1) + desc + m.group(2) + status + m.group(3), new, count=1)
    g = g[:j] + new + g[j:]
g = g.replace('<b>09</b> is the selected-form sheet', '<b>09</b> is the selected-form sheet (<b>09b</b> its large-text continuation)') if '09b</b>' not in g else g
g = g.replace('<b>08b</b> continues the seam with four things a person can enjoy, open, keep and find again.', '<b>08b</b> continues the seam with four things a person can enjoy, open, keep and find again; <b>08c</b> adds the trip day.') if '08c</b>' not in g else g
g = g.replace('<b>12</b> draws three affordances no board had:', '<b>13</b> is the photograph sheet (warm paper chosen for reference images); <b>14</b> is the bounded-supply stress case, proposed; <b>15</b> is the learning and steering comparison, proposed. <b>12</b> draws three affordances no board had:') if '<b>13</b>' not in g else g

# kind counts: the index must agree with 01 (35 admitted + 3 proposed), and say what a count is not
g = g.replace('Every kind in the 38-kind Home union, as drawn on the current boards; three kinds admitted 09-08 (the temporal strip, the work receipt, the money row) after the comparison with the pre-pivot Trips page',
              'Every kind in the Home union as drawn on the current boards: the 35 the build manifest admits, plus three PROPOSED on 09-08 (the temporal strip, the work receipt, the money row). A kind count is an inventory of what has been drawn, not an implementation or display quota: no page renders all of them, and several are conditional by design')
g = g.replace('Seven kinds admitted (four 09-05, three 09-08); the Home union is 38', 'Four kinds admitted 09-05; three PROPOSED 09-08 &mdash; 35 admitted, 3 proposed, matching 01')
g = g.replace('the 38-kind Home union', 'the Home union (35 admitted, 3 proposed)')

g = g.replace('A Home-only design project.', 'A Home-only design project. Selected 2026-09-09: the generous 02/03 compositions, a benefit-led read on a nonurgent open with weather in support, and 15.3&rsquo;s receiving-first learnability through ordinary doors. Not adopted by that selection: the three proposed kinds on 01, Rule B on 08, and any claim about supply economics. ')
open(sys.argv[2], 'w').write(g); print('index ok', all(n in g for _, n, _, _ in ROWS))
