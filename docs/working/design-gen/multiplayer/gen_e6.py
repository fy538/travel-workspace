"""E6 · The regular. Belonging to a place through its people, without friendship and without matching."""
from mp_kit2 import *

# ── 1 · What the place's people told her ──
def known():
    inner = header('Tilde Coffee', 'Court Street &middot; fourteen mornings since May', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 130, tag="TILDE &middot; ILLUSTRATION")}</div>', top=18)
    inner += sect('Told to you here', top=26) + gut('<div>'
        + line('Closed the first week of August &middot; <span style="color: #6E6862;">the owner, July</span>', mark='dot', color=GOLDD)
        + line('Ask for the second roast &middot; <span style="color: #6E6862;">Luca, June</span>', mark='dot', color=GOLDD)
        + line('The back table gets sun until 10:00 &middot; <span style="color: #6E6862;">you, May</span>', mark='dot', color=GOLDD, last=True) + '</div>')
    return phone2(inner, active='Places')

# ── 2 · The nod ──
def nod():
    inner = header('Tilde Coffee', 'Regulars', back=True)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">AT TILDE</div>'
        + says('Let other regulars know you by first name here.', 17, 24)
        + '<div class="led" style="margin-top: 12px; grid-template-columns: 96px minmax(0,1fr);">'
          '<div class="k">SEEN BY</div><div>Regulars who&rsquo;ve done the same</div>'
          '<div class="k">SHOWS</div><div>Your first name and one line you write</div></div>'
        + f'<div style="margin-top: 10px;">{actions(btn("Say hi at Tilde"), door("Not for me", MUTE))}</div>'), top=18)
    inner += sect('Regulars') + gut(original(80, author='Theo', meta='AT TILDE', words='Thursday mornings, usually. Say hello.')
        + f'<div style="margin-top: 16px;">{rule(original(80, author="Ana", meta="AT TILDE", words="the one with the dog"), 16)}</div>')
    return phone2(inner, active='Places')

# ── 3 · When it closes ──
def closing():
    inner = header('Tilde Coffee', 'Last day: Saturday the 30th', back=True)
    inner += gut(dci('Notice', 96, tone='unavailable', title='Closing Saturday the 30th', body='The owner told regulars this week. The lease wasn’t renewed.'), top=18)
    inner += sect('From regulars') + gut(original(96, author='Theo', meta='AT TILDE', words='Eleven years of Thursdays. I proposed at the back table.')
        + f'<div style="margin-top: 16px;">{rule(original(96, author="Ana", meta="AT TILDE", words="they kept a water bowl by the door before anyone asked"), 16)}</div>')
    inner += gut(actions(btn('Leave a line'), door('Keep what you were told here', MUTE)), top=16)
    return phone2(inner, active='Places')

def build():
    cols = [
        col(known(), cap('1', 'What the place&rsquo;s people told her', 'Being a regular is mostly remembering. All of it private, all of it hers.', tags=(EX, PF, PRIV('NORA')))),
        col(nod(), cap('2', 'The nod', 'Mutual, deliberate, scoped to one place. No presence, no messaging, no elsewhere.', tags=(EX, PF, tag('ONLY AT THIS PLACE', GOLDD)))),
        col(closing(), cap('3', 'When it closes', 'A place ending is a social event for the people who belonged to it.', tags=(EX, SH('Notice')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'Frame 1: one person and a place she returns to &mdash; no friends on the product at all. Frame 2 needs a second regular who made the same choice, which at any given caf&eacute; is unlikely for a long time.'),
        ('EFFORT', 'Frame 1: saying &ldquo;keep that&rdquo; three times over four months. Frame 2: one toggle and one line. Frame 3: nothing, or a sentence.'),
        ('KNOWN INPUTS', 'What she chose to keep; what two other people chose to write. Visit counts are hers alone. No one&rsquo;s pattern of attendance is ever shown to anyone else.'),
        ('AUDIENCE EFFECT', 'A new kind of audience: <i>people who also chose this, at this place.</i> It is not friends and not public. Whether the contracts can express a place-scoped mutual audience is an open question.'),
        ('LOW PARTICIPATION', 'Frame 1 is complete with nobody else involved. If no other regular ever turns the nod on, the section simply does not exist.'),
        ('ONE FAILURE', 'Frame 2 read as surveillance: &ldquo;who else comes here.&rdquo; The defence is that nothing is derived &mdash; each line is authored &mdash; but it has to <i>feel</i> that way, and that is untested.'),
    ], [
        ('BASIC INTERACTION', 'Nothing does this, because nothing needs to: people become regulars without software. The bar is whether the product adds anything to a process that already works.'),
        ('WHAT IMPROVES, FOR WHOM', 'Frame 1 is personal memory and improves one person&rsquo;s ordinary week; that is a legitimate benefit and needs no one else. Frame 2 would give someone with few friends on the product a way to be recognized somewhere. Joining a place&rsquo;s regulars is not the same act as swapping numbers or renewing a ritual, and it needs an audience the canon does not have.'),
        ('DIFFERENTIATING?', 'It is the only social value here that needs no friends and no invitation, which is why it matters for the person who has few of either. It is also the most place-native thing in the project.'),
        ('SYSTEM ADVANTAGE', 'A bridge from solo use to other people that involves no matching and no feed. The research finding it rests on: everyday contact with acquaintances is associated with more happiness and belonging.'),
        ('REJECTION TEST', 'Reject &ldquo;here now&rdquo;, last-seen, regulars leaderboards, visit counts shown to others, and any messaging. Reject suggesting one regular to another. Reject a replacement recommendation when a loved place closes.'),
    ], 'rework',
        'Unthought territory with a real research hook and no product precedent. Frame 1 is safe and modest. Frame 2 is the interesting risk and should be studied before it is drawn again.',
        'does a nod that software arranged still feel like a nod &mdash; or is this the one kind of belonging that only works because nobody organised it?',
        offscreen=['Luca is a name she was given, not an account; nothing is known about him beyond the line', 'the nod shows no presence, last-seen or &ldquo;here now&rdquo;, no pattern of attendance, and offers no messaging', 'one-sided interest produces nothing visible', 'when a loved place closes it stays in Life and is never replaced with a recommendation for somewhere similar', 'nothing in the repo proposes frame 2; it is drawn to be argued with'],
        extras=('<b>Source, such as it is:</b> consumer-psychology memo §8 defines &ldquo;fringeships&rdquo; and cites the acquaintance-contact finding, then does not develop it. Foundations doc §6 lists &ldquo;loss or closure&rdquo; among the ways a place relationship changes. No document proposes frames 2 or 3.',
                '<b>Dependency:</b> a place-scoped mutual audience is not one of the four visibility spaces in canon §1.1. It would need a ruling, not a mockup.'))
    return eboard('E6', 'E6 - The regular', 'FEELING INVOLVED', 'The regular',
        'Some of the belonging in a life comes from people who are not friends: the ones who know your order. The payoff is being known somewhere, '
        'and having somewhere to be known, without friendship, invitations or matching. The caf&eacute;, its people and its closing are fixtures.',
        cols, nc, 3)

if __name__ == '__main__':
    print(build())
