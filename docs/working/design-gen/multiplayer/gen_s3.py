"""12 · The edges of sharing: forwarding, people without Vesper, groups over time, withdrawal. Two frames and four
lines. An eight-frame version with a permission flow was cut on 2026-09-21 as over-complicated."""
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
from gen_s1 import status, share, verbs, place_card, loc_row, LULU, CARD_CSS, chat_field, page_bar
from gen_s2 import sheet, opt, kept_row
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
APP = tag('NO APP', OX, 'rgba(122,46,46,0.10)')

# ── 1 · forwarding is just forwarding ──
def forward():
    inner = avatar_for(bar('JO', 'MONDAY 12:14 PM'), 'N')
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="width: 310px; {CARD_CSS} padding: 14px 16px;">'
        f'{status(60, author="Priya", meta="SUNDAY · TO THE SORRENTO FOUR", words=LULU)}<div style="margin-top: 8px;">{place_card()}</div></div></div>', top=18)
    inner += gut(bubble('for mum and dad&rsquo;s anniversary. priya swears by upstairs'), top=10)
    inner += gut(bubble_in('booked upstairs for the 12th. does priya want to come', 'Jo'), top=8)
    inner += gut(chat_field('Message Jo'), top=16)
    return phone2(inner, active='Chat')

# ── 2 · by link, to someone without Vesper ──
def by_link():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div class="fn" style="color: {MUTE}; letter-spacing: 1px;">FROM NORA</div></div>'
    inner += gut(status(60, author='Nora', meta='12:14 PM · TO YOU', words='for mum and dad&rsquo;s anniversary. priya swears by upstairs'), top=14)
    inner += gut(f'<div style="border-left: 2px solid rgba(27,23,20,0.10); padding-left: 12px;">{status(60, author="Priya", meta="SUNDAY · TO THE SORRENTO FOUR", words=LULU)}</div>', top=12)
    inner += gut(place_card(), top=10)
    inner += gut(chat_field('Reply to Nora', ask=False), top=20)
    return webframe(inner)

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('MONDAY 12:14 PM', '1', 'Passing it on', 'Nora quotes Priya&rsquo;s note into her chat with Jo. Same as any app: the card carries Priya&rsquo;s name and who it was for. No permission step; nothing else happens.', forward(), (P('NORA'),)),
                 cell('MONDAY 12:14 PM', '2', 'By link, to someone without Vesper', 'The same share as a page: Nora&rsquo;s words, Priya&rsquo;s under them, the place, a reply field. Nothing to install; the reply reaches Nora as a comment.', by_link(), (APP, P('JO'))),
                 notes('THE FOUR EDGES, IN ONE LINE EACH', led([
                     ('PASSING ON', 'Quote it to someone, or forward it. The card keeps the author&rsquo;s name and original audience. That is the whole rule; if you don&rsquo;t want something to travel, don&rsquo;t post it.'),
                     ('OUTSIDE VESPER', 'A link opens a page with the share and a reply field. Replies come back as comments. The sender is told &ldquo;by link&rdquo;, never whether it was opened.'),
                     ('GROUPS OVER TIME', 'Someone added to a named group sees what is sent from then on. Someone removed keeps what they got and gets nothing new.'),
                     ('WITHDRAWN', 'Taking a share back removes it everywhere it went: the place, other people&rsquo;s kept things, forwards, link pages. Nothing survives except what other people wrote themselves.'),
                 ]) + N('An earlier version of this board had an eight-frame permission flow for passing a note on, a &ldquo;via&rdquo; chain, and rules about private copies. Removed 2026-09-21 as over-complicated: these are the ordinary answers every social app already gives, and they fit in four lines.'), w=620)], top=0)
    body = r1
    html = (HEAD_VDL + f'<div style="width: 1630px; min-height: {hh("12", 1400)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('12 &middot; SHARING &middot; THE EDGES', 'Passing it on, and the three other edges',
                   'Forwarding, people without Vesper, groups over time, and taking a share back. Two frames and four lines; the ordinary answers. Jo is Nora&rsquo;s sister.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('12 - Passing on outside groups withdrawal', html)

if __name__ == '__main__':
    build()
