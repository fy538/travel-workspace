"""D5 · A possibility becomes something we do. An appealing option survives contact with another person's needs."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

def bubble(t, mine=True):
    if mine:
        return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 290px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'
    return f'<div style="display: flex;"><div style="max-width: 290px; background: {CARD}; border: 1px solid {HAIR}; color: {INK}; border-radius: 18px 18px 18px 4px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'

# ── 1 · Worth doing alone ──
def solo():
    inner = anchor_row('NEW YORK', 'SATURDAY 7:30 PM')
    inner += orientation('A slow Sunday in Carroll Gardens.', 'Market, canal, coffee. About three hours.')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 160, tag="THE MARKET &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut('<div>'
        + row('The greenmarket &middot; <span style="color: #6E6862;">8:00&ndash;2:00, busiest at 11:00</span>', mark='dot', color=GOLDD)
        + row('Along the canal &middot; <span style="color: #6E6862;">twenty minutes, flat</span>', mark='dot', color=GOLDD)
        + row('Coffee at the end &middot; <span style="color: #6E6862;">until 4:00</span>', mark='dot', color=GOLDD, last=True) + '</div>' + prov('LISTINGS &middot; SAT'), top=12)
    inner += gut(actions(door('Ask someone along')), top=14)
    return phone2(inner, active='Home')

# ── 2 · One sentence out, one constraint back, and a yes to the change ──
def ask():
    inner = bar('MAYA', 'SATURDAY 7:34 PM')
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">SUNDAY &middot; CARROLL GARDENS</div>' + says('Market, the canal, coffee at the end.', 16, 23), '14px'), top=18)
    inner += gut(bubble('want to do this tomorrow?'), top=12)
    inner += gut(bubble('yes but i need to be home by 4', mine=False), top=12)
    inner += gut(says('Home by four works if you start at 10:00 and finish coffee by 2:30. The market peaks at 11:00 anyway.'), top=16)
    inner += gut(bubble('10 at the market gate? done by 2:30 so you&rsquo;re home by 4'), top=12)
    inner += gut(bubble('perfect', mine=False), top=12)
    return phone2(inner, active='Chat')

# ── 3 · What's agreed ──
def agreed():
    inner = header('Sunday with Maya', 'Maya said yes &middot; Saturday 7:41 PM', back=True)
    inner += gut(dci('InviteCard', 260, view='answered', kicker='YOU AND MAYA',
                     title='The market, the canal, coffee', **{'lines': 'WHEN=Sunday, 10:00|done by 2:30;WHERE=Carroll Gardens|meet at the market gate;WITH=You and Maya'},
                     answer='perfect', stamp='MAYA · SATURDAY 7:41 PM'), top=18)
    inner += sect('Settled') + gut('<div>'
        + row('Market gate, 10:00', mark='dot', color=GREEN)
        + row('Done by 2:30, so Maya&rsquo;s home by 4:00', mark='dot', color=GREEN, last=True) + '</div>')
    inner += sect('Still loose') + gut('<div>'
        + row('Which stalls, and how long', mark='dashed', color=MUTE)
        + row('Whether coffee happens', mark='dashed', color=MUTE, last=True) + '</div>')
    inner += gut(actions(door('Something changed')), top=12)
    return phone2(inner, active='Home')

def inset_decline():
    body = (N('If Maya had said no.') + box(plain('can&rsquo;t this week') + f'<div style="margin-top: 6px;">{plain("Maya · Saturday 7:36 PM", MUTE, 13, 18)}</div>', '12px 14px')
            + N('Sunday in Carroll Gardens stays on Home exactly as it was.'))
    return inset('2, THE OTHER ANSWER', body, 'A DECLINE CHANGES NOTHING ELSE ON THE SCREEN')

def build():
    cols = [
        col(solo(), cap('1', 'Worth doing alone', 'A complete answer with nobody else in it. Sharing is optional from here.', tags=(EX, PF))),
        col(ask() + inset_decline(), cap('2', '&ldquo;Fancy this?&rdquo; &mdash; and a real constraint', 'She needs to be home by four, which is not the same as leaving at four. Nora proposes the change herself, and it is agreed only when Maya says yes.', tags=(EX,))),
        col(agreed(), cap('3', 'What is agreed, and what stays loose', 'The line between an intention and a commitment, drawn explicitly.', tags=(EX, SH('InviteCard')))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'One friend. No shared history is needed; the constraint arrives from her, in her words, rather than from anything inferred about her.'),
        ('INITIATOR EFFORT', 'Open Home, one tap to ask, two words. The possibility was already assembled before anyone was involved.'),
        ('FRIEND EFFORT', 'Read one card, answer in a sentence. She never enters a form, sets availability, or joins anything.'),
        ('KNOWN INPUTS', 'Listed market hours, labelled as listed and not checked. Her stated four o&rsquo;clock. Not used: her calendar, her location, her past attendance.'),
        ('AUDIENCE EFFECT', 'One person. No Occasion, no calendar entry, no confirmed attendance is created by interest alone &mdash; frame 3 says so on the card.'),
        ('LOW PARTICIPATION', 'The inset: she declines, and the Sunday is untouched. No re-invitation, no substitute friend proposed.'),
        ('ONE CHANGE', 'Her constraint is the change. It moves a start time and nothing else.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Sending a link and a message is the obvious alternative and works fine. Rendering that message as a prettier card is not an advantage.'),
        ('DIFFERENTIATING?', 'One thing only: the constraint lands on an option that already exists, so the answer is &ldquo;start at ten&rdquo; rather than a fresh round of &ldquo;what do you want to do?&rdquo;. That is real, and it is small.'),
        ('SYSTEM ADVANTAGE', 'Partly shown: the same object carries the solo value, the ask, the answer and the agreement without ever becoming a plan document. Whether that holds when four people answer is not tested here.'),
        ('REJECTION TEST', 'Reject instant event forms. Reject itinerary bureaucracy. Reject precision nobody asked for &mdash; the calendar-mindset research is the direct warning, and frame 3&rsquo;s &ldquo;still loose&rdquo; list is the response to it.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('retain',
        'The strongest &ldquo;being together&rdquo; candidate: it reduces both the imagining and the arranging, and it degrades gracefully to a solo Sunday.',
        'at what point does a loose intention need an owner &mdash; and who is accountable when two people each believe the other was going to confirm?')
        + N('<b>Named omission:</b> only one friend answers. What happens when three do, with three different constraints, is the obvious next canvas and is not drawn.')
        + N('<b>Overlap flagged for Pass B:</b> shares its whole second half with D6 and D7. The distinct part is only the starting point.')
        + N('<b>Decided, not displayed:</b> interest alone creates no Occasion, calendar entry or confirmed attendance &middot; a decline triggers no re-invitation and no substitute friend &middot; precision appears only where someone is relying on it &middot; nothing is reserved.'), w=440)
    return write('D5 - A possibility becomes something we do', board(
        bw(3, (600, 520, 440)), hh('D5', 1900),
        'D5 &middot; BEING TOGETHER &middot; EXPLORATORY',
        'A possibility becomes something we do',
        'That looks worthwhile; I would like to do it with someone. The payoff is that an appealing possibility survives contact '
        'with another person&rsquo;s needs, without restarting. Hours, market, people and the Sunday are fixtures.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
