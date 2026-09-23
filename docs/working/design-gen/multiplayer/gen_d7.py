"""D7 · Happy for company. Express willingness without recruiting guests or becoming a host. All three outcomes."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
O1 = tag('OUTCOME 1 &middot; SOMEONE JOINS', GREEN, 'rgba(61,112,80,0.12)')
O2 = tag('OUTCOME 2 &middot; CAN&rsquo;T COME', GOLDD, 'rgba(176,133,58,0.14)')
O3 = tag('OUTCOME 3 &middot; NOBODY ANSWERS', MUTE, 'rgba(110,104,98,0.10)')

def bubble(t, mine=True):
    if mine:
        return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 290px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
    return f'<div style="display: flex;"><div style="max-width: 290px; background: {CARD}; border: 1px solid {HAIR}; color: {INK}; border-radius: 18px 18px 18px 4px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'

OPEN = 'Getting coffee and wandering Red Hook this afternoon. Happy for company.'

OPEN = 'getting coffee and wandering red hook this afternoon. happy for company'
OPEN = 'taking a book to the park around 3. come sit if you want'
# ── 1 · Saying it ──
def express():
    inner = bar('SATURDAY 12:40 PM')
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain(OPEN, size=17, lh=24)}</div>', top=18)
    inner += gut(f'<div class="led" style="grid-template-columns: 70px minmax(0,1fr); row-gap: 12px; align-items: center;">'
        f'<div class="k">TO</div><div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;"><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">M</span><span class="vk-t-bodySmMedium">Maya</span></span>'
        f'<span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">P</span><span class="vk-t-bodySmMedium">Priya</span></span></div>'
        f'<div class="k">WHERE</div><div>Fort Greene Park, the west lawn</div><div class="k">WHEN</div><div>Around 3:00, until 5:00</div></div>', top=20)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=22)
    return phone2(inner, active='Home')

# ── 2 · Maya receives it, and asks for a smaller version ──
def receives():
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 1:05 PM'), 'M')
    inner += orientation('Sun until 5:40.', 'Saturday &middot; 66&deg;')
    inner += sect('From Nora') + gut(original(150, author='Nora', meta='12:41 PM · TO YOU AND PRIYA', words=OPEN,
                          place='Fort Greene Park, west lawn', placeMeta='AROUND 3:00, UNTIL 5:00 · 14 MIN FROM YOU'))
    inner += gut(actions(btn('I&rsquo;ll come'), btn('Reply', False)), top=12)
    inner += gut(bubble('could join for half an hour around 4?'), top=16)
    return phone2(inner, active='Home')

# ── 3 · Nora: one yes to a shorter visit, one different idea ──
def outcomes():
    inner = anchor_row('FORT GREENE', 'SATURDAY 1:20 PM')
    inner += orientation('Maya&rsquo;s asking about 4:00.', 'It&rsquo;s set once you say yes.')
    inner += sect('Maya') + gut(f'<div style="display: flex; flex-direction: column; gap: 8px;">{bubble_in("could join for half an hour around 4?")}{bubble("yes! by the tennis courts")}{bubble_in("see you at 4")}</div>'
        + f'<div style="margin-top: 12px;">{box(faces("NM", "You and Maya · 4:00, by the tennis courts"), "12px 14px")}</div>')
    inner += sect('Priya') + gut(original(96, author='Priya', meta='1:12 PM · TO YOU', words='not today. walk tomorrow morning?', door='Reply'))
    return phone2(inner, active='Home')

# ── 4 · Nobody took it up ──
def alone():
    inner = anchor_row('FORT GREENE', 'SATURDAY 4:50 PM')
    inner += orientation('The west lawn keeps the sun until 5:40.', 'Saturday &middot; 64&deg; &middot; sunset 6:58.')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 170, tag="THE PARK &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut('<div>'
        + row('The farmers&rsquo; stand by the entrance &middot; <span style="color: #6E6862;">until 5:00</span>', mark='dot', color=GOLDD)
        + row('Home &middot; <span style="color: #6E6862;">eighteen minutes on foot</span>', mark='dot', color=GOLDD, last=True) + '</div>'
        + prov('PARK LISTING &middot; SAT'), top=12)
    return phone2(inner, active='Home')

def build():
    cols = [
        col(express(), cap('1', 'Saying it, without becoming a host', 'A sentence, two people, a place she chose and a rough window. Not a status, not her live location.', tags=(EX, PF, SH('.vdl-recipient')))),
        col(receives(), cap('2', 'Maya receives it, and asks for less', 'The recipient&rsquo;s side. She can come, reply, or do nothing; she asks for half an hour at four.', tags=(EX, O1))),
        col(outcomes(), cap('3', 'A shorter visit, and a different idea', 'Interest is not agreement: the meeting exists only after Nora says yes. Priya&rsquo;s counter-offer is a proposal, not a plan.', tags=(EX, O1, O2))),
        col(alone(), cap('4', 'Nobody answered', 'The most likely outcome. The unaccepted opening expires quietly; an accepted meeting would not.', tags=(EX, O3))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'One friend, no history. The sender is already doing the thing, so the value does not depend on anyone joining.'),
        ('SENDER EFFORT', 'One sentence, an audience, one tap. The hard part is social, not procedural, and no interface removes that.'),
        ('RECIPIENT EFFORT', 'One tap to join, or nothing. Answering privately costs a sentence; ignoring it costs nothing and is invisible.'),
        ('KNOWN INPUTS', 'Only the sentence and the audience. Explicitly not used: calendar-derived free time, location, movement, or any inference that someone is probably free.'),
        ('AUDIENCE EFFECT', 'Two named people, expiring at five. Precise location is never exposed by the opening itself &mdash; it is sent by hand after a yes.'),
        ('LOW PARTICIPATION', 'Frame 3 is the design&rsquo;s real test and is given a full frame: silence must read as ordinary, with no count, no unanswered badge, no retry prompt.'),
        ('ONE CHANGE', 'Expiry. It closes the opening without touching anything separately agreed &mdash; if Maya said yes at two, five o&rsquo;clock does not cancel that.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'This is a text message to two friends. That is the honest baseline and it is a good one.'),
        ('DIFFERENTIATING?', 'Two narrow candidates: the opening closes itself, so nobody has to decline a dead invitation late; and a decline is private, so the other recipient never sees who passed. Neither requires AI.'),
        ('SYSTEM ADVANTAGE', 'None claimed. Nothing here needs context, history or generation, which is itself worth noting &mdash; the most humane interaction in the portfolio is also the least technological.'),
        ('REJECTION TEST', 'Reject viewer lists, response counts and read receipts. Reject inferred willingness or availability. Reject amplifying reach. Reject anything that makes an unanswered opening look like a failure.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('rework',
        'Keep the shape, and hold it to the harder question. The research on underestimated appreciation of contact supports the hesitation being real; it does not tell us this interface reduces it.',
        'does this lower the pressure, or just relocate rejection anxiety into a new interface &mdash; where silence is now a product state rather than a friend being busy?')
        + N('<b>Dependency:</b> audience and expiry policy is unresolved and must be reviewed with the owner of Social&rsquo;s sender/access rules. '
            'Nothing here proposes a persistent availability object, and one should not be introduced to make this work.')
        + N('<b>Overlap flagged for Pass B:</b> compare directly with D5. The difference is willingness versus an activity, and it may not survive as two entries.')
        + N('<b>Decided, not displayed:</b> no viewer list, response count or read receipt &middot; a decline is private to the sender; the other recipient never learns of it &middot; her exact spot reaches Maya because Nora sends it, not because Maya accepted &middot; the opening expires without comment and without touching anything separately agreed &middot; an unanswered opening is never shown as unanswered.'), w=440)
    return write('D7 - Happy for company', board(
        bw(4, (600, 520, 440)), hh('D7', 1900),
        'D7 &middot; BEING TOGETHER &middot; EXPLORATORY',
        'Happy for company',
        'I am doing something anyway; company could be nice. The payoff is expressing willingness without recruiting guests or '
        'becoming a host. All three outcomes are drawn, including the one where nobody answers. Fixture throughout.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
