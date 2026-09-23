"""September 21: board 10 (photos, sent and received) indexed on 00, recorded on 07; budget lines updated."""
MISS = []
def sub(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        n = s.count(old)
        if n == 1: s = s.replace(old, new)
        elif new in s: pass
        else: MISS.append((path, old[:80], n))
    open(path, 'w').write(s)

ROW09 = "'NEW &middot; SEPTEMBER 12 COVERAGE ASSIGNMENT &middot; POLICY PROPOSED, NOT ADOPTED'],"
sub('gen_se.py', [
    (ROW09, ROW09 + "\n    ['10 &middot; Photos, sent and received', '5 slots and one matched comparison: Nora selects three of her pasta-night pictures in the evening&rsquo;s record, previews and sends them to Dana, whose tip the evening used; Dana receives them whole on Home, opens and returns, and finds them later in Life without replying', 'NEW &middot; SEPTEMBER 21 ADDITIVE ASSIGNMENT &middot; NO APPROVED PHOTOGRAPHS YET: EVERY FRAME IS A STAND-IN WITH ITS LEDGER ID'],"),
    ("September 8 added board 08&rsquo;s five continuation slots and September 12 added board 09&rsquo;s seven sender, access and control slots, both at the assignment&rsquo;s request, so the project holds 36 against a ceiling of 24; the September 9 second pass adds one comparison frame (05 D7-B, the ordinary messaging control) against a ceiling of 12, its A side reused from 08.2.",
     "September 8 added board 08&rsquo;s five continuation slots, September 12 added board 09&rsquo;s seven sender, access and control slots and September 21 added board 10&rsquo;s five photo slots, each at the assignment&rsquo;s request, so the project holds 41 against a ceiling of 24. Comparison frames: the September 9 second pass added one (05 D7-B, its A side reused from 08.2) and September 21 added three (10.5, the matched D5 treatments of one arrival), so 16 against a ceiling of 12."),
])
sub('gen_c5.py', [
    ("    ['Frame budget: 29 storyboard slots against the 24-slot ceiling (board 08)', 'Unresolved scope discrepancy', 'The five continuation slots were asked for by the September 8 assignment and kept for this review; the ceiling was not amended. Either the ceiling moves or two frames fold (08.3 into 04.5&rsquo;s grammar; 08.4 into 02.2&rsquo;s); the founder decides'],",
     "    ['Frame budget: 41 storyboard slots against the 24-slot ceiling (boards 08, 09, 10); 16 comparison frames against 12 (05 D7-B, 10.5)', 'Unresolved scope discrepancy', 'Boards 08, 09 and 10 were each asked for by an assignment (September 8, 12 and 21) and kept for review; neither ceiling was amended. Either the ceilings move or frames fold (08.3 into 04.5&rsquo;s grammar; 08.4 into 02.2&rsquo;s; 10.6 into 08.3&rsquo;s); the founder decides'],"),
    ("    'An attributed contribution on an occasion page, with its scope line and optional media (03.3, 03.4), not in the package',\n]",
     "    'An attributed contribution on an occasion page, with its scope line and optional media (03.3, 03.4), not in the package',\n"
     "    'OriginalReader with a small photo set: a lead picture, the rest in order, per-image attribution and a casual line in sans rather than the serif quote (10.3, 10.4, 10.6; copy companion &sect;7). Local on board 10; offered to the shared owner only after Life&rsquo;s viewer anatomy is reconciled',\n]"),
    ("    ['Guest access: preview, code, payoff, wrong or expired code, retry, changed or reopened invitation, unavailable ending',",
     "    ['Photos, sent and received: select, preview, send or leave, partial failure, original-first receiving, viewer and return, later retrieval', '10.1&ndash;10.6', 'Drawn September 21 on one fixture set (PH1&ndash;PH6), none supplied: every picture is a stand-in at its real proportions with its ledger ID. 10.5 compares original only, light context and earned enrichment on matched inputs; light context is selected for Home', 'Social, with Life (viewer, selection donor) and Home (placement)', 'Approved photographs; Life&rsquo;s viewer reconciliation; set delivery and copies stay separate agreements'],\n"
     "    ['Guest access: preview, code, payoff, wrong or expired code, retry, changed or reopened invitation, unavailable ending',"),
])
print('misses', MISS)
