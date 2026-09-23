"""E5 · Ours, over years. A relationship's places, rituals and unfinished threads, and permission to let things rest."""
from mp_kit2 import *

# ── 1 · Together ──
def together():
    inner = header('You and Maya', 'Since 2019 &middot; eleven places', back=True)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 8px;">THE GARDEN REOPENED LAST WEEK</div>'
        + original(90, author='Maya', meta='MAY 18 · TO YOU', words='we&rsquo;re going back when the garden reopens')
        + prov('GARDEN LISTING &middot; MON')
        + f'<div style="margin-top: 8px;">{actions(btn("Send to Maya"), door("Not now", MUTE))}</div>'), top=18)
    inner += sect('Places between you') + gut('<div>'
        + row('Been to together &middot; <span style="color: #6E6862;">six</span>', mark='dot', color=GOLDD)
        + row('From Maya &middot; <span style="color: #6E6862;">three, including the Print Room</span>', mark='dot', color=GOLDD)
        + row('Said you&rsquo;d go back &middot; <span style="color: #6E6862;">two</span>', mark='hollow', color=GOLDD, last=True) + '</div>')
    return phone2(inner, active='Life')

# ── 2 · A ritual, asked about ──
def ritual():
    inner = anchor_row('NEW YORK', 'THURSDAY 7:15 PM')
    inner += orientation('First cold Sunday.', '41&deg; by evening. The last two Novembers, that meant soup at Priya&rsquo;s.')
    inner += gut(box(says('Soup at Priya&rsquo;s again?', 18, 25)
        + f'<div style="display: flex; flex-direction: column; gap: 2px; margin-top: 8px;">'
        + door('Yes, if they&rsquo;re up for it') + door('Not this year', MUTE) + door('It was never a thing', MUTE) + '</div>'), top=16)
    inner += gut(quiet('Maya and Priya each get asked the same way.'), top=12)
    return phone2(inner, active='Home')

# ── 3 · Looking forward ──
def anticipation():
    inner = header('Lisbon, in March', 'You and Maya &middot; 23 weeks', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 150, tag="LISBON &middot; ILLUSTRATION")}</div>', top=18)
    inner += gut(original(190, author='Maya', meta='SUNDAY · FOR YOU TWO', words='first morning. coffee here, standing up, before we do anything sensible',
                          place='Café Andorinha, Chiado', placeMeta='OPENS 8:00 · LISTING SUN', door='Reply'), top=16)
    inner += gut(actions(door('Add one of your own')), top=6)
    return phone2(inner, active='Home')

# ── 4 · A friendship at rest ──
def rest():
    inner = header('You and Dana', 'Since 2021', back=True)
    inner += gut(says('Last together: Sorrento, a year ago.', 17, 24, INK2), top=18)
    inner += sect('Between you') + gut('<div>'
        + row('Sorrento, August &middot; <span style="color: #6E6862;">her photos, your notes</span>', mark='hollow')
        + row('The dish she told you to try', mark='hollow', last=True) + '</div>')
    inner += sect('Less of this') + gut('<div>'
        + row('See less from that summer', mark='none')
        + row('Change what Dana sees of yours', mark='none')
        + row('Something more final', mark='none', last=True) + '</div>')
    return phone2(inner, active='Life')

def build():
    cols = [
        col(together(), cap('1', 'The two of you, as the subject', 'A message Maya sent in May meets a garden that reopened last week. No reading of what kind of pair they are.', tags=(EX, PF, PRIV('NORA')))),
        col(ritual(), cap('2', 'A ritual, asked about', 'Convergence done carefully: each person privately, and one no means silence for everyone.', tags=(EX, PRIV('EACH OF THE THREE')))),
        col(anticipation(), cap('3', 'Twenty-three weeks away', 'Anticipation as a shared thing in itself, with nothing to administer.', tags=(EX, SHARED('THE TWO OF YOU')))),
        col(rest(), cap('4', 'A friendship at rest', 'No drift warning, no reconnect prompt. Softer and harder controls, all unannounced.', tags=(EX, PRIV('NORA')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'Years. This is the most history-dependent board in the project and cannot be shown honestly on day one. What it needs is small but real: a handful of occasions two people each chose to keep.'),
        ('EFFORT AT THE TIME', 'None beyond living it. &ldquo;Go back when the garden reopens&rdquo; was said out loud in May, by both, and kept because both kept it.'),
        ('EFFORT NOW', 'Reading, and one tap to recognise or reject a guess.'),
        ('KNOWN INPUTS', 'Occasions both people kept; things each deliberately handed the other; a return both of them said. Not used: message frequency, who texts first, how long since contact.'),
        ('AUDIENCE EFFECT', 'Frame 1 is Nora&rsquo;s view of the two of them; Maya has her own, and the two need not agree. &ldquo;What seems to work&rdquo; is never shown to Maya as a claim about her.'),
        ('LOW PARTICIPATION', 'Frame 4 is the low-participation case raised to a principle: a relationship with nothing happening in it is complete as it stands.'),
        ('ONE FAILURE', 'The guess in frame 1 is wrong, or true and unwelcome. One tap retires it, and it is never restated in other words.'),
    ], [
        ('BASIC INTERACTION', 'Photo albums and message search hold the past. Shared notes hold the promises. Both work, and neither knows the garden reopened.'),
        ('WHAT IMPROVES, FOR WHOM', 'Continuity and timing: a message from May meets a garden that reopened last week, and Nora does not have to have remembered either. Frame 2: a ritual is raised without anyone having to be the one who asks. That check happens before anything is agreed, which is the only place a silent &ldquo;no&rdquo; belongs.'),
        ('DIFFERENTIATING?', 'The relationship as the subject, rather than the other person&rsquo;s profile, is a different object from anything a social product offers. The August 9 profile doc called this view the highest-leverage prototype; it was never drawn.'),
        ('SYSTEM ADVANTAGE', 'The canon&rsquo;s own proof signature: &ldquo;a later occasion visibly benefits from confirmed personal, relationship, place and outcome evidence.&rdquo; Memory over performance is the stated moat.'),
        ('REJECTION TEST', 'Reject friendship levels, streaks, neglected-contact rankings and &ldquo;you&rsquo;re drifting apart.&rdquo; Reject a merged taste profile for the pair. Reject treating a repeated pattern as consent to repeat it.'),
    ], 'retain',
        'The long arc is where the product&rsquo;s memory becomes something two people can feel. Frame 2 is the cleanest small demonstration of plural private context in the project.',
        'can &ldquo;what seems to work for you two&rdquo; ever be said without feeling like being analysed &mdash; and should the two people see the same sentence, or each their own?',
        offscreen=['&ldquo;what seems to work&rdquo; is Nora&rsquo;s alone; Maya sees nothing like it unless both keep it', 'twice is evidence, not consent: the ritual is asked about, never assumed', 'each of the three is asked separately; one &ldquo;no&rdquo; means silence for everyone, including who said it', 'no itinerary or checklist is generated for a trip 23 weeks away', 'a quiet friendship gets no drift warning, month count or reconnect prompt', 'each control is its own choice and none is announced'],
        extras=('<b>Source:</b> profile-and-relationship-views doc §12 (Together, unfinished threads, &ldquo;what works for us&rdquo;); canon §4 (Our Place, Ritual, Convergence), §8 continuity gradient; 08-21 strategy §6.6 (anticipation); Life social-lifecycle matrix S08&ndash;S11 (softening without blocking).',
                '<b>Named omission:</b> the far end of the lifecycle &mdash; estrangement, reconciliation as a new epoch, a death directive &mdash; is specified in the Life contract and not drawn here. Co-authored relationship statements (profile doc §24.2) are an open decision.'))
    return eboard('E5', 'E5 - Ours over years', 'CARRYING FORWARD', 'Ours, over years',
        'A friendship has places, habits and half-made promises that belong to neither person alone. The payoff is that they stay findable, a ritual is asked about rather than assumed, '
        'looking forward is allowed to be enough, and a friendship gone quiet is left in peace. All fixture.',
        cols, nc, 4)

if __name__ == '__main__':
    print(build())
