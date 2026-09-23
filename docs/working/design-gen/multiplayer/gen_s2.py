"""11 · Audience, Keep, an ask, a link, withdraw. The rest of sharing: who a share goes to; keeping a friend's share for
yourself; a status whose point is the answers; something from outside with a line on it; taking a share back and what
goes with it. Reuses board 10's shapes. Founder direction, 2026-09-21: "let's do all 6"."""
from mp_kit2 import *
from gen_merge import daycap
from gen_p2_common import illo
import gen_s1 as S
from gen_s1 import status, share, verbs, place_card, to_row, loc_row, where_line, photo_grid, post, LULU, PIN, CARD_CSS, footer, liked_by, sep, page_bar, page_title, to_bar, toolbar, chat_field
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
FOUR = 'THE SORRENTO FOUR'

def sheet(inner):
    return f'<div style="border-top: 1px solid rgba(27,23,20,0.14); background: {CARD}; border-radius: 16px 16px 0 0; padding: 18px 22px 22px 22px; margin-top: 18px;">{inner}</div>'
def opt(label, sub, on=False, faces_=()):
    mark = f'<span style="width: 18px; height: 18px; border-radius: 9px; border: 1.5px solid {INK}; background: {INK if on else "transparent"}; flex: none;"></span>'
    f = f'<span style="margin-left: auto;">{facepile(list(faces_), 20, -6)}</span>' if faces_ else ''
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.08);">{mark}'
            f'<div><div style="font-size: 15px; line-height: 20px; color: {INK}; font-weight: {600 if on else 400};">{label}</div><div style="font-size: 13px; line-height: 18px; color: {MUTE};">{sub}</div></div>{f}</div>')

# ── 1 · who it goes to ──
def audience():
    inner = avatar_for(to_bar('The Sorrento four', ('N', 'M', 'D')), 'P')
    inner += gut(plain(LULU, size=18, lh=26), top=24)
    inner += gut(place_card(), top=16)
    inner += sheet(f'<div class="kickm" style="margin-bottom: 4px;">TO</div>'
        + opt('Friends', 'Everyone you&rsquo;ve added. Never public.', faces_=('N', 'M', 'S', 'D', 'J'))
        + opt('The Sorrento four', 'A group you named in June', on=True, faces_=('N', 'M', 'D'))
        + opt('Court Street', 'A group you named in March', faces_=('N', 'S'))
        + opt('One person', 'Pick someone')
        + f'<div style="margin-top: 12px;">{door("New group", MUTE)}</div>')
    return phone2(inner, active='Chat')

# ── 2 · received, with the audience legible ──
def received_group():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:44 PM')
    inner += gut(share('Priya', '9:40 PM · TO THE SORRENTO FOUR', LULU, extra=place_card(), where='At Lulu&rsquo;s'), top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 8px;">{facepile(["N","M","D"], 20, -6)}{plain("Sent to you, Maya and Dana", MUTE, 13, 18)}</div>', top=10)
    return phone2(inner, active='Home')

# ── 3 · keep ──
def keep_tap():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:46 PM')
    inner += gut(share('Priya', '9:40 PM · TO THE SORRENTO FOUR', LULU, extra=place_card(), where='At Lulu&rsquo;s', kept=True), top=18)
    inner += sheet(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">Kept.</div>'
        + f'<div style="margin-top: 8px;">{plain("In your Life, under Priya and under Lulu&rsquo;s. Priya isn&rsquo;t told.", INK2, 15, 21)}</div>'
        + f'<div style="margin-top: 12px; min-height: 40px; border: 1px solid rgba(27,23,20,0.14); border-radius: 10px; padding: 10px 12px; color: {MUTE}; font-size: 14px;">A note for yourself, if you want one</div>'
        + f'<div style="margin-top: 12px; display: flex; gap: 18px;">{door("Open in Life", GOLDD)}{door("Undo", MUTE)}</div>')
    return phone2(inner, active='Home')

# ── 4 · kept things, in Life ──
def kept_row(letter, who, when, words, thing, kind):
    return (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.07);">{thumb(kind, 48)}'
            f'<div style="flex: 1; min-width: 0;"><div style="font-size: 15px; line-height: 20px; color: {INK}; font-weight: 600;">{thing}</div>'
            f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 2px;">{words}</div>'
            f'<div class="fn" style="margin-top: 4px;">FROM {who.upper()} &middot; {when} &middot; KEPT BY YOU</div></div></div>')
def life_kept():
    inner = page_bar('LIFE') + page_title('Kept', 'From friends &middot; 3')
    inner += gut(kept_row('P', 'Priya', 'SEPT 21', 'upstairs is the reason to go. good for a long dinner, with parents', 'Lulu&rsquo;s, Carroll Gardens', 'table')
                 + kept_row('D', 'Dana', 'OCT 3', 'zest at the very end, off the heat', 'The Sorrento pasta', 'noodles')
                 + kept_row('S', 'Sam', 'SEPT 18', 'one film a week, one kind of cake', 'The Lantern, Court Street', 'film'), top=16)
    return phone2(inner, active='Life')

# ── 5 · an ask ──
ASK = 'anyone know a good dentist near fort greene? mine retired and i&rsquo;m avoiding it'
def ask_received():
    inner = anchor_row('NEW YORK', 'TUESDAY 8:20 AM')
    inner += gut(share('Nora', '8:02 AM · TO FRIENDS', ASK, where='Fort Greene'), top=18)
    inner += gut(f'<div style="border-left: 2px solid rgba(27,23,20,0.10); padding-left: 12px;">{status(60, author="Maya", meta="8:11 AM · TO FRIENDS", words="dr okafor on lafayette. she&rsquo;s gentle and she&rsquo;ll tell you off exactly once")}</div>', top=12)
    inner += gut(chat_field('Comment to everyone', ask=False), top=16)
    return phone2(inner, active='Home')
def ask_after():
    inner = anchor_row('NEW YORK', 'TUESDAY 6:40 PM')
    inner += gut(post('You', '8:02 AM · TO FRIENDS', ASK, '', 'Fort Greene', me='N') + liked_by('Sam, Dana'), top=20)
    inner += gut(f'<div style="border-left: 2px solid rgba(27,23,20,0.10); padding-left: 12px;">'
        + status(60, author='Maya', meta='8:11 AM · TO FRIENDS', words='dr okafor on lafayette. she&rsquo;s gentle and she&rsquo;ll tell you off exactly once')
        + f'<div style="margin-top: 12px;">{status(60, author="Priya", meta="9:30 AM · TO YOU", words="mine is in the city but honestly worth it. i&rsquo;ll send the number")}</div>'
        + f'<div style="margin-top: 12px;">{status(60, author="You", meta="6:38 PM · TO FRIENDS", words="booked okafor for the 14th. thank you all", me="N")}</div></div>', top=12)
    return phone2(inner, active='Home')

# ── 6 · a link ──
def link_card():
    return (f'<div style="{CARD_CSS} padding: 14px 16px; display: flex; gap: 12px; align-items: center;">{thumb("film", 56)}'
            f'<div style="min-width: 0; flex: 1;"><div class="fn" style="margin-bottom: 4px;">LINK &middot; THE LANTERN&rsquo;S SITE</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 16px; line-height: 21px;">This week: one film, through Sunday</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {INK2}; margin-top: 2px;">Court Street &middot; 7:15 nightly</div></div></div>')
def link_write():
    return S.composer('S', 'this is the cinema. one film a week and exactly one kind of cake', link_card(), where='Court Street', on=('where',))
def link_received():
    inner = anchor_row('NEW YORK', 'WEDNESDAY 4:12 PM')
    inner += gut(share('Sam', '4:10 PM · TO FRIENDS', 'this is the cinema. one film a week and exactly one kind of cake', extra=link_card(), where='Court Street'), top=18)
    return phone2(inner, active='Home')

# ── 7 · withdraw ──
def withdraw():
    inner = avatar_for(anchor_row('NEW YORK', 'SEPT 30 · 7:15 PM'), 'P')
    inner += gut(post('You', 'SEPT 21 · TO THE SORRENTO FOUR', LULU, place_card(), 'At Lulu&rsquo;s', me='P'), top=20)
    inner += sheet(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">Take this back?</div>'
        + f'<div style="margin-top: 8px;">{plain("It comes off Lulu&rsquo;s for Nora, Maya and Dana, and out of Nora&rsquo;s kept things. Sam&rsquo;s comment under it goes too. Nora&rsquo;s reply to you stays in her chat with you.", INK2, 15, 21)}</div>'
        + f'<div style="margin-top: 14px;">{actions(btn("Take it back"), door("Edit instead", MUTE))}</div>')
    return phone2(inner, active='Home')
def after_withdraw_places():
    inner = page_bar('PLACES')
    inner += f'<div style="margin-top: 14px;">{plate("table", 140, tag="ILLUSTRATION &middot; NOT A PHOTOGRAPH").replace("margin: -16px -16px 12px -16px;", "margin: 0;")}</div>'
    inner += page_title('Lulu&rsquo;s', 'Carroll Gardens &middot; Italian &middot; open till 11')
    inner += sect('From friends', top=24) + gut(plain('Nothing here now.', MUTE, 15, 21))
    inner += sect('Kept') + gut(f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0;">{thumb("table", 48)}<div><div style="font-size: 15px; line-height: 20px; color: {INK}; font-weight: 600;">Lulu&rsquo;s, Carroll Gardens</div>'
        + f'<div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 2px;">Priya took her note back on Sept 30. You kept the place.</div></div></div>')
    return phone2(inner, active='Places')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('SUNDAY 9:40 PM', '1', 'Who it goes to', 'Tapping &ldquo;To&rdquo; opens the picker: friends, a group you named once, or one person. Last time&rsquo;s choice is already selected. A group is an audience, not a chat.', audience(), (P('AUDIENCE'), P('SENDER'))),
                 cell('SUNDAY 9:44 PM', '2', 'Received, audience legible', 'The same share as board 10 D2, sent to a group. Nora sees who else got it, so she knows who a comment reaches.', received_group(), (P('AUDIENCE'), P('RECEIVER'))),
                 cell('SUNDAY 9:46 PM', '3', 'Keep', 'For her, not for Priya. One tap; it goes under Priya and under Lulu&rsquo;s in her Life, with a note of her own if she wants one. Priya isn&rsquo;t told.', keep_tap(), (P('KEEP'), P('RECEIVER')))], top=0)
    r2 = rowdiv([cell('LATER', '4', 'Kept things, in Life', 'Three friends&rsquo; shares she kept, each with whose it was and when. Each is also under the person and under the place. Keeping it changed nothing for them.', life_kept(), (P('KEEP'), P('LIFE'))),
                 cell('TUESDAY 8:20 AM', '5', 'An ask', 'A status whose point is the answers. Comments go to everyone by default, so the answers help the next person too.', ask_received(), (P('ASK'), P('RECEIVER'))),
                 cell('TUESDAY 6:40 PM', '6', 'What Nora sees', 'Two answers to everyone, one to her alone (the others don&rsquo;t see it), and her own comment closing it. No resolved flag: she says so.', ask_after(), (P('ASK'), P('SENDER')))])
    r3 = rowdiv([cell('WEDNESDAY 4:10 PM', '7', 'A link, written', 'Something from outside, with his words on top. The card shows where it goes and opens there.', link_write(), (P('LINK'), P('SENDER'))),
                 cell('WEDNESDAY 4:12 PM', '8', 'A link, received', 'Same shape as everything else. Because it resolves to a place, keeping it files it under the Lantern in Places as well as under Sam.', link_received(), (P('LINK'), P('RECEIVER'))),
                 cell('SEPT 30', '9', 'Taking it back', 'Priya withdraws the Lulu&rsquo;s note. The sheet says exactly what goes with it and what stays: a comment to her stays hers; a comment under it goes.', withdraw(), (P('WITHDRAW'), P('SENDER')))])
    r4 = rowdiv([cell('OCT 1', '10', 'After: Lulu&rsquo;s, for Nora', 'The note is off the place. Nora&rsquo;s own Keep of the place survives, with a line saying why the note is gone.', after_withdraw_places(), (P('WITHDRAW'), P('RECEIVER'))),
                 notes('THE VERBS, COMPLETE', tbl(['VERB', 'FOR WHOM', 'WHO IS TOLD', 'WHERE IT GOES'], [
                     ['<b>Like</b>', 'The sender', 'The sender, by name', 'Nowhere else'],
                     ['<b>Comment</b>', 'The sender, or everyone who got it', 'The composer says which before you send', 'Under the share'],
                     ['<b>Quote</b>', 'Someone else, or Vesper', 'Whoever that chat is with', 'A chat'],
                     ['<b>Keep</b>', 'You', 'Nobody', 'Your Life: under the person, and under the place or thing'],
                     ['<b>Answer</b>', 'The host (invitations only)', 'The host; everyone invited sees who&rsquo;s in', 'The gathering'],
                 ]), w=560)])
    n2 = notes('AUDIENCE', led([
                     ('THREE CHOICES', 'Friends (everyone you&rsquo;ve added), a group you named once, or one person. Never public.'),
                     ('A GROUP IS NOT A CHAT', 'It is a list with a name. It has no room, no history of its own, no unread count. The shares sent to it live where all shares live.'),
                     ('LEGIBLE ON RECEIPT', 'The receiver sees the audience by name and, for a group, who else got it. A comment&rsquo;s reach is never a surprise.'),
                     ('DEFAULT', 'Last time&rsquo;s choice. Changing it is one tap in the composer.'),
                 ]), w=520)
    n3 = notes('AN ASK, A LINK, TAKING IT BACK', led([
        ('ASK', 'Not a type: a status people answer. Comments default to everyone so the answers accumulate. An answer to the asker alone is possible and stays private. It closes when the asker says so, in a comment. No resolved flag, no bounty, no expiry.'),
        ('LINK', 'Anything from outside, with your words on top. The card shows title, source and a thumbnail; it opens where it came from. If it resolves to a place, it behaves like a place share: Keep files it under the place too.'),
        ('WITHDRAW', 'Your share, gone for everyone: off the place, out of others&rsquo; kept things, comments under it with it. What people wrote <i>to you</i> about it stays theirs. Edit is the gentler door and keeps comments.'),
        ('NOTIFICATIONS', 'Not drawn. Proposed: a status, a whereabouts, a place or a link never ping; an invitation does, and so does a comment on your own share or an answer to your ask.'),
    ]), w=620)
    import gen_s3 as E
    r5 = rowdiv([cell('MONDAY 12:14 PM', '11', 'Passing it on', 'Nora quotes Priya&rsquo;s note into her chat with Jo, her sister. Same as any app: the card carries Priya&rsquo;s name and who it was for. No permission step.', E.forward(), (P('EDGES'), P('NORA'))),
                 cell('MONDAY 12:14 PM', '12', 'By link, to someone without Vesper', 'The same share as a page: Nora&rsquo;s words, Priya&rsquo;s under them, the place, a reply field. Nothing to install; the reply reaches Nora as a comment.', E.by_link(), (P('EDGES'), P('NO APP')))])
    n4 = notes('THE EDGES, IN ONE LINE EACH', led([
        ('PASSING ON', 'Quote it to someone, or forward it. The card keeps the author&rsquo;s name and original audience. If you don&rsquo;t want something to travel, don&rsquo;t post it.'),
        ('OUTSIDE VESPER', 'A link opens a page with the share and a reply field. Replies come back as comments. The sender is told &ldquo;by link&rdquo;, never whether it was opened.'),
        ('GROUPS OVER TIME', 'Someone added to a named group sees what is sent from then on. Someone removed keeps what they got and gets nothing new.'),
        ('WITHDRAWN', 'Taking a share back removes it everywhere it went. Nothing survives except what other people wrote themselves.'),
    ]) + N('Formerly board 12, merged here on 2026-09-22. An earlier eight-frame permission flow for passing things on was cut on 2026-09-21 as over-complicated.'), w=560)
    body = r1 + r2 + r3 + r4 + r5 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12); flex-wrap: wrap;">' + n2 + n3 + n4 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(3, (520, 620))}px; min-height: {hh("11", 5200)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('11 &middot; SHARING &middot; THE REST OF IT', 'Audience, Keep, an ask, a link, taking it back, and the edges',
                   'Who a share goes to, and how the receiver knows. Keeping a friend&rsquo;s share for yourself. A status whose point is the answers. Something from outside with your words on top. And what goes with a share when you take it back. Same shapes as board 10. Drawn, not tested with anyone.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('11 - Audience Keep ask link withdraw', html)

if __name__ == '__main__':
    build()
