"""13 · The chat. A private chat between two people, and nothing else. Vesper is optional: a door in the composer,
and when used its reply is marked and both see it. When one of them changes something the two of them own (board 18),
a card says so. Redrawn 2026-09-21 after the founder separated the chat from the list."""
from mp_kit2 import *
from gen_merge import daycap
from gen_p2_common import illo
import gen_s1 as S
from gen_s1 import status, ticket_row, photo_thumb, CARD_CSS, chat_field, vesper_reply, asked_bubble
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

vesper = vesper_reply
def quoted(inner):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="width: 300px;">{inner}</div></div>'
def field(ask=True):
    return chat_field('Message Maya', ask)
def ours_card(t, sub):
    return (f'<div style="display: flex; justify-content: center;"><div style="{CARD_CSS} padding: 10px 14px; display: flex; gap: 10px; align-items: center; max-width: 320px;">{thumb("noodles", 40)}'
            f'<div><div style="font-size: 14px; color: {INK};">{t}</div><div class="fn" style="margin-top: 2px;">{sub}</div></div>{CHEV}</div></div>')

def plain_chat():
    inner = bar('MAYA', 'FRIDAY 10:44 PM')
    inner += gut(quoted(ticket_row() + f'<div class="fn" style="margin-top: 4px; text-align: right;">SAM &middot; 10:38 PM &middot; TO FRIENDS</div>'), top=18)
    inner += gut(bubble('are you actually going? i could do 1 if we leave by 3'), top=10)
    inner += gut(bubble_in('yes. i have a ticket. how do we get back', 'Maya'), top=8)
    inner += gut(bubble('cab? split it'), top=8)
    inner += gut(bubble_in('ok. yours at 12:30. wearing the boots, don&rsquo;t laugh', 'Maya'), top=8)
    inner += gut(bubble('i would never'), top=8)
    inner += gut(field(), top=14)
    return phone2(inner, active='Chat')

def asked():
    inner = bar('MAYA', 'FRIDAY 10:47 PM')
    inner += gut(bubble_in('ok. yours at 12:30. wearing the boots, don&rsquo;t laugh', 'Maya'), top=18)
    inner += gut(bubble('i would never'), top=8)
    inner += gut(asked_bubble('how do we get back from pacha at 3am'), top=12)
    inner += gut(vesper('The last train from there is 12:40, so it&rsquo;s a cab. About $30, and Maya&rsquo;s on the way to Nora&rsquo;s.'), top=10)
    inner += gut(bubble_in('fine. cab. split', 'Maya'), top=10)
    inner += gut(field(), top=14)
    return phone2(inner, active='Chat')

def card_in_chat():
    inner = bar('MAYA', 'OCT 5 · 6:12 PM')
    inner += gut(bubble_in('adding this one. the broth is stupid good', 'Maya'), top=18)
    inner += gut(ours_card('Maya added <b>Hato</b> to <b>Our places</b>', 'OURS &middot; 4 PLACES &middot; TAP TO OPEN'), top=10)
    inner += gut(bubble('sunday then. all three?'), top=10)
    inner += gut(bubble_in('absolutely not. two.', 'Maya'), top=8)
    inner += gut(f'<div style="{MONO} font-size: 9px; letter-spacing: 1.1px; color: {MUTE}; text-align: center;">NOV 2</div>', top=14)
    inner += gut(bubble_in('saw a dog that looked exactly like sam', 'Maya'), top=8)
    inner += gut(quoted(photo_thumb(110, 'PHOTO &middot; MAYA')), top=8)
    inner += gut(bubble('i need to see this dog immediately'), top=8)
    inner += gut(field(), top=14)
    return phone2(inner, active='Chat')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('SEPT 26', '1', 'A chat', 'Two people. Sam&rsquo;s share quoted in, and they work it out themselves. The gold spark in the composer is Vesper; nobody touches it.', plain_chat(), (P('CHAT'),)),
                 cell('SEPT 26', '2', 'Asked', 'Nora taps the gold spark in the composer. The question and the answer sit in the chat, marked, seen by both. It uses only what was said here and what each of them has let it use. Then it is gone again.', asked(), (P('CHAT'), P('VESPER, OPTIONAL'))),
                 cell('OCT 5 → NOV 2', '3', 'A card when something of theirs changes', 'Maya added a place to the list they own (board 18). The chat says so in one line; tap to open it. Then the dog.', card_in_chat(), (P('CHAT'), P('OURS')))], top=0)
    n = notes('THE CHAT, AND ONLY THE CHAT', led([
        ('WHAT IT IS', 'A private chat between two people. Bubbles, quotes, photos. It looks like every other chat because it should.'),
        ('VESPER', 'Optional. A door in the composer. When used, the question and the answer are in the chat, marked with who asked, and both see them. It knows what was said here, what was quoted in, and what each person has let it use for the other. It never speaks unasked.'),
        ('WHAT IT IS NOT', 'Not where things are built. Nothing lives at the top of it. What the two of them own lives on its own page (board 18) and the chat only points at it.'),
        ('OPEN', 'What each person has let Vesper use for the other, still. Whether a group chat of three or four gets the same door.'),
    ]) + N('The earlier version of this board put a plan, a list and a method at the top of the thread, formed on a Vesper prompt. Cut 2026-09-21: the list deserved its own page, and Vesper was too present.'), w=620)
    body = r1
    html = (HEAD_VDL + f'<div style="width: 2010px; min-height: {hh("13", 1500)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('13 &middot; THE CHAT', 'A private chat, and Vesper only when asked',
                   'Nora and Maya. A chat like any other. Vesper is a door in the composer, not a presence. When something the two of them own changes, the chat says so in one line and points at it.')
            + '<div style="display: flex; gap: 46px; align-items: flex-start;">' + body + n + '</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('13 - The chat', html)

if __name__ == '__main__':
    build()
