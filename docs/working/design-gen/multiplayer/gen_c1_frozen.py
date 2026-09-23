"""C1 · Copy, before and after — frozen. The three-way comparison is kept as the images rendered on 2026-09-21, because
the frame functions it was built from have since been rewritten and can no longer reproduce the true BEFORE column."""
from mp_kit2 import *
from gen_c1 import VOICES, CAST, PUSH
ROWS = [('round2-1-home-with-friends.png', '1 &middot; Home, with friends'), ('round2-2-quiet-sunday.png', '2 &middot; A Sunday with nothing new'),
        ('round2-3-morning-after.png', '3 &middot; The morning after a dinner'), ('round2-4-surprise.png', '4 &middot; Setting up a surprise'),
        ('round2-5-group-suggestion.png', '5 &middot; One suggestion to a group'), ('round2-6-unanswered-opening.png', '6 &middot; Nobody took up the opening')]
def build():
    inner = blk('WHAT THIS PAGE IS', N('Six frames in three rounds, as rendered on September 21: how each stood before, a first rewrite, and the rewrite the founder preferred. '
        'They are kept as images on purpose. The boards these frames came from have been revised twice since, so regenerating this page would show today&rsquo;s frames in the BEFORE column. '
        'Some lines in the right-hand column were later changed again by the independent review &mdash; &ldquo;Maya and Dana are in&rdquo; is one &mdash; and the direction boards carry the current wording.'))
    inner += blk('WHAT THE SECOND REWRITE PUSHED FURTHER', tbl(['', 'WHY'], PUSH))
    for f, t in ROWS:
        inner += blk(t.upper(), f'<img src="copy/{f}" alt="" style="width: 100%; display: block; border-radius: 6px;">')
    inner += blk('FOUR VOICES, KEPT APART', tbl(['VOICE', 'WHOSE', 'GRAMMAR', 'EXAMPLE'], VOICES))
    inner += blk('A CAST SHEET', tbl(['', 'HOW THEY WRITE', 'A LINE OF THEIRS'], CAST))
    return write('C1 - Copy before and after', sheetboard(1980, hh('C1', 6900),
        'C1 &middot; ARCHIVE &middot; COPY, AS JUDGED ON SEPTEMBER 21', 'Copy: before, first rewrite, pushed further',
        'The record of how the copy rules were arrived at. Qualified on September 21 by the review: see the copy companion, section 9.', inner, vdl=False))
if __name__ == '__main__':
    print(build())
