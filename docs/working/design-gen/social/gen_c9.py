"""Board 11 · Social and Multiplayer Shapes, side by side (founder request, 2026-09-26).
Every place where the two social projects contradict each other, as two lanes: Social (3ef10868) on the left,
Multiplayer Shapes (caf916f9) on the right. Each side is the actual frame, cropped from that project's own board,
with its position in one or two sentences and where it is drawn. A comparison, not a ruling."""
import os, struct
from gen_c2 import *

CROPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'crops')
W_IMG = 320
S_COL, M_COL = '#8A6628', '#3E6E99'

def img(cid):
    d = open(os.path.join(CROPS, cid + '.jpg'), 'rb').read(); i = 2
    while True:
        m = d[i + 1]; L = struct.unpack('>H', d[i + 2:i + 4])[0]
        if m in (0xC0, 0xC2): h, w = struct.unpack('>HH', d[i + 5:i + 9]); break
        i += 2 + L
    hd = round(h * W_IMG / w)
    return (f'<img src="media/compare/{cid}.jpg" width="{W_IMG}" height="{hd}" alt="" '
            f'style="display: block; width: {W_IMG}px; height: {hd}px; border-radius: 10px; border: 1px solid rgba(27,23,20,0.12); flex: none;">')

def lane(cid, text, ref, color):
    return (f'<div style="width: 812px; flex: none; display: flex; gap: 26px; align-items: flex-start;">{img(cid)}'
            f'<div style="flex: 1; display: flex; flex-direction: column; gap: 10px; padding-top: 4px;">'
            f'<div style="{SERIF} font-size: 19px; line-height: 27px; color: {INK};">{text}</div>'
            f'<div class="fn" style="color: {color}; line-height: 15px;">{ref}</div></div></div>')

def row(n, title, crux, s, m, note=''):
    nt = (f'<div style="margin-top: 14px; padding: 9px 14px; border-left: 3px solid #7A2E2A; background: rgba(122,46,42,0.06); font-size: 13.5px; line-height: 19px; color: {INK2};">{note}</div>' if note else '')
    return (f'<div style="padding: 30px 0 34px 0; border-top: 1px solid rgba(27,23,20,0.12);">'
            f'<div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 18px;"><span style="{MONO} font-size: 12px; font-weight: 700; color: {MUTE};">{n:02d}</span>'
            f'<span style="{SERIF} font-weight: 600; font-size: 25px; line-height: 30px;">{title}</span>'
            f'<span style="font-size: 15px; line-height: 21px; color: {INK2};">{crux}</span></div>'
            f'<div style="display: flex; gap: 56px; align-items: flex-start;">{lane(s[0], s[1], s[2], S_COL)}'
            f'<div style="width: 1px; align-self: stretch; background: rgba(27,23,20,0.12); flex: none;"></div>{lane(m[0], m[1], m[2], M_COL)}</div>{nt}</div>')

def section(t):
    return f'<div class="kick" style="margin: 36px 0 2px 0; color: {GOLDD}; font-size: 11px;">{t}</div>'

R = []
R.append(section('1 · WHAT A SHARE LOOKS LIKE'))
R.append(row(1, 'Picture or words first', 'What leads when a friend sends photographs.',
    ('01s', 'The pictures lead, whole and side by side. Who sent them, and which evening, sit underneath.', 'SOCIAL 10.3 · ALSO 08.1 · ORIGINAL-FIRST RECEIVING (SELECTED 09-09)'),
    ('01m', 'The words lead, like a status. The pictures are tiled small underneath. A ticket is the exception and stays full size.', 'MULTIPLAYER 01 A2 · FOUNDER DIRECTION 09-21')))
R.append(row(2, 'How a friend’s words are set', 'The same sentence can read as a quotation or as a post.',
    ('02s', 'Her words in the reading serif, as the centrepiece of the shared original reader.', 'SOCIAL 02.4 · OriginalReader, SHARED PACKAGE 0.4.1'),
    ('02m', 'A post in sans, never in quotation marks, and the same on Home and in Life. Board 07 recommends Life change to match.', 'MULTIPLAYER 07 · DECISION 2 · FOUNDER DIRECTION 09-21')))
R.append(row(3, 'A shared place', 'How much of the place comes with the sender’s note.',
    ('03s', 'A place row with an illustrated tile, the listed hours, and a line saying they were not checked today.', 'SOCIAL 02.4 · PLACE ROW IN THE SHARED READER'),
    ('03m', 'A line: the name, where, and the sender’s reason in her own words. No hours and no picture, because those are the place’s own business.', 'MULTIPLAYER 01 D2 · FOUNDER RULING 09-25 (“JUST USE B”)')))
R.append(row(4, 'The composer', 'How a share is made and sent.',
    ('04s', 'Start from the thing, pick one person, then a preview that is exactly what goes. Send or Not now. The line is optional.', 'SOCIAL 09.2 · 10.2'),
    ('04m', 'One composer for everything: To, words, attachments in a toolbar, Send. The kind of share follows from what is attached. Board 07 recommends it replace Social’s preview.', 'MULTIPLAYER 01 A1 · 07 DECISION 3')))
R.append(row(5, 'What travels with it', 'Where it was sent from, and how long it lasts.',
    ('05s', 'Only the thing and its words; the preview states who sees it and until when. No location of the sender. A direct share lasts “until you take them back”, proposed.', 'SOCIAL 09.2 · 10.2 · DURATION PROPOSED'),
    ('05m', 'Every share carries where it was sent from: a neighbourhood by default, the place itself when you are at it, off in one tap. Words and pictures never expire.', 'MULTIPLAYER 01 C1 · 01 “THE SAME FOUR” TABLE')))
R.append(section('2 · WHO IT GOES TO, AND WHO YOU ARE CONNECTED TO'))
R.append(row(6, 'The default audience', 'One person, or everyone.',
    ('06s', 'One named person, chosen from people already connected. Friends as an audience is a separate agreement, not adopted. There are no named groups.', 'SOCIAL 09.1 · 10.2 · FRIENDS SCOPE UNADOPTED'),
    ('06m', 'Friends, a group you named, or one person, with last time’s choice already selected. Most shares go to Friends.', 'MULTIPLAYER 02.1')))
R.append(row(7, 'Becoming connected', 'Who is offered to you, and what connecting gives.',
    ('07s', 'Sam can ask to stay in touch under Nora’s name on his own link; nothing prompts it. It opens a way to share from now on, not everything past. Staying occasion-bound is a complete ending.', 'SOCIAL 04.6 · LEDGER C5'),
    ('07m', 'The occasion page puts “Ask to be friends” beside everyone who was there. Being friends means each sees everything the other shares with Friends.', 'MULTIPLAYER 04.5 · 04.6')))
R.append(section('3 · RESPONDING'))
R.append(row(8, 'Likes, and what the sender learns', 'Whether the author sees any response beyond replies.',
    ('08s', 'No reactions. The author sees the replies sent to her, and no viewer list, count or report of what anyone did.', 'SOCIAL 09.4 · 02.5'),
    ('08m', 'One like. The sender sees who liked it, by name; never a count, never who opened it.', 'MULTIPLAYER 01 A3 · FOUNDER DIRECTION 09-21')))
R.append(row(9, 'Where a reply goes', 'To the author, or under the share for everyone.',
    ('09s', 'Reply reaches the author only. There is no comment thread under a share.', 'SOCIAL 08.2 · 02.5'),
    ('09m', 'Comments sit under the share and go to everyone who got it by default, or to the sender alone. An ask collects its answers in public.', 'MULTIPLAYER 02.5 · 02.6')))
R.append(row(10, 'Passing it on', 'Whether someone else’s material can travel further.',
    ('10s', 'Someone else’s material is not yours to send on. Maya’s table is named at the preview and left out; her share permits no onward sharing without her grant.', 'SOCIAL 10.2 · LEDGER §3 A1, §10 PH-01'),
    ('10m', 'Quote it into a chat or forward it; the card keeps the author and the original audience. No permission step: if you don’t want something to travel, don’t post it.', 'MULTIPLAYER 02.11 · “THE EDGES” RULE, 09-21')))
R.append(row(11, 'A link to someone without Vesper', 'What the link alone lets a person do.',
    ('11s', 'A proposed, conditional guest branch: confirm a one-time code to your number before the exact address or a confirmed answer.', 'SOCIAL 09.7 · 03.2 · GUEST IDENTITY UNSETTLED'),
    ('11m', 'A page anyone holding the link can read and reply on, and perhaps add one thing. The sender is told only “by link”. No verification is drawn.', 'MULTIPLAYER 02.12 · 04.2')))
R.append(section('4 · AFTERWARDS'))
R.append(row(12, 'Taking something back', 'What goes with a withdrawn share.',
    ('12s', 'Only that share goes. What other people wrote stays theirs: the reply, Priya’s note, Maya’s own photograph.', 'SOCIAL 09.4 · 09.5 · C4 WITHDRAWAL'),
    ('12m', 'Gone everywhere: off the place, out of others’ kept things, and the comments under it go too. Only what people wrote to the sender privately stays.', 'MULTIPLAYER 02.9 · 02.10')))
R.append(row(13, 'Friends’ shares on Home', 'One addressed item, or a section of friends.',
    ('13s', 'One item in its own region, with no section around it. Placement is proposed and is Home’s call.', 'SOCIAL 08.1 · 10.3'),
    ('13m', 'A standing “From friends” section: things sent to you first, then compact rows per person, capped, with the rest behind a door.', 'MULTIPLAYER 03.2'),
    note='<b>Both conflict with a ruled decision.</b> The September 5 amendment to Home’s composition puts casual shares from friends in Places · From friends, with Life · People as the record. The code follows that ruling.'))
R.append(row(14, 'Wanting less of someone', 'The controls, and their names.',
    ('14s', 'Fewer, Mute, Leave this evening, Block, and Report to Vesper, each with its stated effect. The account-wide versions belong to You &amp; Trust.', 'SOCIAL 09.6 · POLICY PROPOSED'),
    ('14m', 'See less (for a week, or until changed) and Stop sharing. No block and no report are drawn.', 'MULTIPLAYER 03.7 · 04.8')))
R.append(section('5 · GETTING TOGETHER'))
R.append(row(15, 'The invitation, and its address', 'What the invitation is, and who sees where.',
    ('15s', 'A labelled invitation: when, where, with, bring. The exact address comes only after the guest confirms a code.', 'SOCIAL 03.1 · 03.2 · InviteCard'),
    ('15m', 'A gathering card under the host’s words; InviteCard “read as a form”. The card shows “Court Street, 3F” to every friend it went to.', 'MULTIPLAYER 01 B2 · FOUNDER DIRECTION 09-21')))
R.append(row(16, 'Who counts as coming', 'Whether an earlier reply can stand as a yes.',
    ('16s', 'An answer from a link is provisional until confirmed. Earlier answers are history, never prefilled; only a fresh answer establishes who is coming.', 'SOCIAL 03.4 INSET · LEDGER C3′'),
    ('16m', '“Count me in any time after 12” is taken as a yes: when Nora sends 12:30 as the plan, Priya is in without being asked again.', 'MULTIPLAYER 06 B5')))
R.append(section('6 · VESPER'))
R.append(row(17, 'Vesper between two people', 'A private lane, or a voice in the chat.',
    ('17s', 'Asking Vesper is private: a separate lane whose chip says Maya sees nothing. Reply to a person and Ask are never mixed.', 'SOCIAL 02.6'),
    ('17m', 'Vesper is a door inside the two-person chat. Its answer is marked “asked by Nora · to both of you” and uses what each of them let it use.', 'MULTIPLAYER 05.2 · 01 Q')))
R.append(row(18, 'Vesper using a friend’s words', 'Whether a friend’s share can feed an answer.',
    ('18s', 'Without Maya’s explicit, scoped grant her share is never sent to the model. The answer draws on the listing and the gallery’s notes instead.', 'SOCIAL 02.6 · LEDGER §8.3'),
    ('18m', 'Nora asks a collection which places would suit Sunday and gets a short list built on Priya’s and Sam’s words. The board marks the grant as an open question.', 'MULTIPLAYER 10.4')))
R.append(section('7 · SETS'))
R.append(row(19, 'Sharing part of a set', 'Some of the pictures, or all of them.',
    ('19s', 'Select any of an evening’s pictures; Share sends the two that are hers. Part of a set can go.', 'SOCIAL 10.1 · 10.2'),
    ('19m', 'A collection is shared whole or not at all. To share only some, make a new collection with just those.', 'MULTIPLAYER 10.3 · FOUNDER DIRECTION'),
    note='These only fit together if an evening’s record is not a collection. Neither project says so.'))
R.append(section('8 · THE FIXTURE WORLD'))
R.append(row(20, 'The same people, different lives', 'Both projects draw Nora’s circle, differently.',
    ('20s', 'Sam has no account and is reached by text. Pasta night is Saturday Sep 19 from seven, in Carroll Gardens. Dana is in Sorrento and not attending.', 'SOCIAL 03.4 · SHARED FIXTURE LEDGER'),
    ('20m', 'Sam has an account and friends who like his Pacha post. Pasta night cooks from 6, eats at 7 at Court Street 3F, and is also dated October 3. Dana is in Marseille. Jo, Lulu’s, Hato and Pacha are not in the ledger.', 'MULTIPLAYER 01 C3 · 01 B1 · 03.2 · 04.6')))

AGREE = ['No counts, badges or unread numbers', 'No read receipts; opening is never reported', 'Receiving and leaving is a complete ending; nothing is owed back',
         'No contacts import', 'A share stays reachable under the person while it is shared, and is copied only if you keep it',
         'Keep is private; the sender is not told', 'People’s own words are never rewritten', 'No group chat']

def board11():
    lanes = (f'<div style="display: flex; gap: 56px; margin-top: 26px; position: sticky; top: 0;">'
             f'<div style="width: 812px; padding: 14px 18px; border-top: 4px solid {S_COL}; background: #FBF7EC;"><div class="kick" style="color: {S_COL};">LEFT LANE · SOCIAL EXPERIENCE · 3ef10868</div>'
             f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">Boards 02–10. Its rules come from the handoffs, the shared fixture ledger and the contribution contract; most are drawn as proposals, a few as selected.</div></div>'
             f'<div style="width: 1px; flex: none;"></div>'
             f'<div style="width: 812px; padding: 14px 18px; border-top: 4px solid {M_COL}; background: #FBF7EC;"><div class="kick" style="color: {M_COL};">RIGHT LANE · MULTIPLAYER SHAPES · caf916f9</div>'
             f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">Boards 01–10. Its rules are mostly the direction you gave in review, Sept 20–25, listed on its board 00 and not yet recorded as decisions.</div></div></div>')
    agree = (f'<div style="margin-top: 20px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);"><div class="kick" style="color: {MUTE};">WHERE THEY ALREADY AGREE</div>'
             f'<div style="display: flex; flex-wrap: wrap; gap: 8px 28px; margin-top: 12px; font-size: 15px; line-height: 22px; color: {INK2};">'
             + ''.join(f'<span>{a}</span>' for a in AGREE) + '</div></div>')
    return (HEAD_VDL + f'<div style="width: 1820px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 40px 32px; {SANS} color: {INK};">'
            + head('VESPER · SOCIAL EXPERIENCE · 11 · SIDE BY SIDE · 2026-09-26', '11 · Where the two social projects disagree',
                   'Every contradiction between this project and Multiplayer Shapes, as two lanes. Each side is the actual frame, cropped from that project’s own board, with what it says and where it is drawn. Twenty disagreements in eight groups. This board compares; it rules nothing.')
            + lanes + ''.join(R) + agree
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">CROPS RENDERED 2026-09-26 FROM EACH PROJECT’S OWN GENERATORS (docs/working/design-gen/social AND /multiplayer), WHICH REBUILD THE LIVE BOARDS · PHOTOGRAPHS IN BOTH ARE STAND-INS · A STATIC COMPARISON: NOTHING HERE IS A DECISION</div></div>' + TAIL)

if __name__ == '__main__':
    h = board11(); open(os.path.join(OUT, '11 - Where the two social projects disagree.dc.html'), 'w').write(h); print('wrote 11', len(h))
