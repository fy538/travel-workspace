#!/usr/bin/env python3
"""07 adoption ledger + Q24 correction, 00 status (2026-09-11). argv[1] = mirror dir."""
import sys, os
S = sys.argv[1]
def edit(f, pairs):
    p = os.path.join(S, f); t = open(p).read()
    for a, b in pairs:
        assert a in t, (f[:12], a[:90]); t = t.replace(a, b, 1)
    open(p, 'w').write(t); print('edited', f[:14])
f7 = '07 Decisions, Mapping, Reuse.dc.html'
edit(f7, [('an external schedule kept beside a day as evidence with a stable source identity (C&amp;C §3.9 Bring/T1): what is parsed vs what a person reads,',
  'an external schedule is Ask by default — an attachment that accompanies a question is transient (C&amp;C §3.2) — and is kept beside a day only on an explicit Keep, which admits that schedule alone and leaves a compact receipt with Undo; an explicit Bring or import doorway is a separate gesture. Open: stable source identity for a kept schedule, what is parsed vs what a person reads,')])
R = lambda k, v: f'          <div class="r"><span class="rk">{k}</span><span>{v}</span></div>\n'
card = ('        <div class="card">\n          <div class="k">SHARED PACKAGE ADOPTION · vdl-stage1 0.3 · 2026-09-11 · CONSOLIDATION, NOT A REDESIGN</div>\n'
 + R('Consumed', 'From workbench <span class="m">c13ae951</span> (board 06, <span class="m">vdl-package.json</span>), copied byte-for-byte: the kernel <span class="m">styles.css</span>, <span class="m">vdl.css</span> and <span class="m">Notice</span>. Brief §21.5 records a 0.4 that changed only OriginalReader, which Plans does not consume, so everything here is identical at 0.4; the live manifest still reads 0.3 (reported). A later shared change does not reach this project by itself.')
 + R('Adopted · tokens', '30 of the kit’s 33 tokens now read the kernel’s exact tokens, with the former values kept as fallbacks, so nothing moves. Local, with no kernel equivalent: <span class="m">--gold-wash</span>, <span class="m">--gold-edge</span>, <span class="m">--r-rail</span>.')
 + R('Adopted · buttons', 'Every product button on 01–12, 90, 91 and 92’s phone is <span class="m">.vdl-btn r16</span> — the Plans shape the workbench named on 02B — as primary, secondary or a bare text action. The quiet, keep, external and held tones are local modifiers on that one construction (<span class="m">.pl-*</span>) and are reported as missing variants. 92’s research chrome stays board furniture.')
 + R('Adopted · doors', 'Standalone doors use the shared Door’s drawn arrow (<span class="m">.vdl-door</span>), the Plans cleanup 03C named: every “Details”, the sheet doors and the two prepared-message doors. Their colours stay Plans’: gold, planning ink toward a person, mute.')
 + R('Adopted · Notice', '90 J2c, J2d and J2e — the states Notice was derived from — are the shared Notice: pending with Cancel, failed with Try again and Not now, unknown with Not now. Held actions are no longer drawn.')
 + R('Kept · Plans’ selected design', 'The itinerary page, date rail, time gutter and rows (A1, Plans’ own donor); the gold-dot receipt sentence (founder-selected 2026-09-05 — Notice is a tinted box); the contextual-request sheet and its field with mic and send (A2, a later native check); the outgoing and preview cards; the ticket stub.')
 + R('Missing variants · reported, not redrawn', '<b>InviteCard guest</b> has no itinerary-row body (time gutter, serif stop titles, the “from you” arrival line) and no 31/33 title, so 04 C2, 04 C7, 05 D8 and 11 G1 keep their pages; the workbench caption pairs C2 with <span class="m">shape=rounded</span> but never built it. <b>InviteCard answered</b> has no primary with the guest’s own label (05 D8; Social reported the same for 03.6). <b>InviteCard host</b> is per-recipient, while 04 C1 is one combined preview with an itinerary row and facepile. <b>Ticket row</b> truncates the stub’s route at 349, 300 and 227px (measured) and has no provenance line, so 03 B2 and 09 J1a keep the stub. <b>Door</b> has no inline variant whose arrow travels with the last word in wrapping text, so attributed-source doors keep a typed arrow (<span class="m">.vdl-door</span> is inline-flex and would bring back the wrap fixed on 09-05). <b>vdl-btn</b> lacks quiet, keep, external and held tones. <b>FactPair</b> has no stacked gutter-label form (08 P2). The drawn arrow is a fixed 13px and does not scale with text (03 B7 at 135%).')
 + R('Before references', 'Thirteen “Before shared package” boards, frozen with <span class="m">kit/plans.before-vdl.css</span>, so each renders exactly as it did before adoption.')
 + R('Named gaps, unchanged', '12pt mono times, the 31/33 day title, <span class="m">--r-rail</span>, the gold wash and edge — for the textVariants and colors owners.')
 + '        </div>\n\n')
t = open(os.path.join(S, f7)).read()
i = t.index('TYPE / MATERIAL MAPPING'); j = t.rindex('<div class="card">', 0, i)
t = t[:j] + card.lstrip() + '        ' + t[j:]
open(os.path.join(S, f7), 'w').write(t); print('07 ledger inserted')
edit('00 Start Here.dc.html', [
 ('<div class="r"><span class="rk">Sept 10 · selected</span>',
  '<div class="r"><span class="rk">Sept 11 · shared package</span><span>Adopted vdl-stage1 0.3 as a consolidation, not a redesign: kernel tokens under the kit, the shared button and Door on every board, Notice on 90’s three state frames. Plans’ selected compositions are unchanged. Missing shared variants are listed on 07, and the originals are kept as the “Before shared package” boards.</span></div>\n            <div class="r"><span class="rk">Sept 10 · selected</span>'),
 ('<div class="r"><span class="rk"><a href="?file=90+Appendix',
  '<div class="r"><span class="rk">Before shared package</span><span>Thirteen frozen originals of 01–06, 08, 09, 11, 12 and 90–92 as they were before the 2026-09-11 adoption, each on its own frozen kit. Comparison references, not current design.</span></div>\n          <div class="r"><span class="rk"><a href="?file=90+Appendix'),
])
