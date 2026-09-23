"""E1 · Getting into the room. The newcomer and the host. 'Invitation is not incorporation.'"""
from mp_kit2 import *

# ── 1 · Sam's invitation: everything on it is Nora's ──
def invitation():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div class="fn" style="color: {MUTE};">FROM NORA</div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 25px; line-height: 31px; letter-spacing: -0.2px;">Pasta night, Saturday.</div>', top=10)
    inner += gut(original(130, author='Nora', meta='THURSDAY · TO YOU', words='You said you missed cooking with people since the move. This is the low-key version of that. Come hungry.'), top=16)
    inner += sect('The evening', top=26) + gut('<div>'
        + line('Cooking from 6:00. Eating around 7:00. Join for either.', mark='dot', color=GOLDD)
        + line('Four of us, in my kitchen', mark='dot', color=GOLDD)
        + line('Maya&rsquo;s bringing the recipe', mark='dot', color=GOLDD, last=True) + '</div>')
    inner += sect('Who&rsquo;s coming', top=26) + gut('<div>'
        + person('M', 'Maya', 'my oldest friend here')
        + person('P', 'Priya', 'started coming in the spring') + '</div>' + prov('NORA WROTE THESE'))
    inner += gut(actions(btn('I&rsquo;ll come'), btn('Just dinner', False), door('Can&rsquo;t this time', MUTE)), top=22)
    return webframe(inner)

# ── 2 · Sam's own page: a private question becomes his own request ──
def brief():
    inner = f'<div style="padding: 20px 22px 0 22px;">{chip("JUST YOU")}</div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Saturday, for you.</div>', top=10)
    inner += gut(bubble('could i arrive with someone? i don&rsquo;t know the building'), top=18)
    inner += gut(says('That&rsquo;s Nora&rsquo;s to arrange. Want to ask her?'), top=14)
    inner += gut(f'<div class="vdl-field" style="border-radius: 12px; min-height: 52px; align-items: flex-start; padding: 12px 14px;"><span class="vk-t-bodyMd">Could I arrive with someone? I don&rsquo;t know the building.</span></div>'
        + f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">{chip("TO NORA · FROM YOU")}</div>'
        + f'<div style="margin-top: 10px;">{actions(btn("Send to Nora"), door("Keep it to myself", MUTE))}</div>', top=12)
    inner += sect('Friday', top=26) + gut(original(96, author='Nora', meta='FRIDAY · TO YOU', words='Maya can meet you downstairs at 6:45. She&rsquo;ll text you.'))
    return webframe(inner)

# ── 3 · The host: a request with a name on it, and the person who agreed to help ──
def host():
    inner = header('Pasta night', 'Saturday &middot; you&rsquo;re hosting', back=True)
    inner += sect('From Sam', top=20) + gut(original(96, author='Sam', meta='THURSDAY · TO YOU', words='Could I arrive with someone? I don&rsquo;t know the building.'))
    inner += sect('You and Maya') + gut(f'<div style="display: flex; flex-direction: column; gap: 8px;">{bubble("can you meet sam downstairs at 6:45? he doesn&rsquo;t know the building")}{bubble_in("sure. send me his number")}</div>')
    inner += sect('Coming') + gut('<div>'
        + line('Maya &middot; <span style="color: #6E6862;">from 6:00 · the recipe, and lemons</span>', mark='dot', color=GREEN)
        + line('Sam &middot; <span style="color: #6E6862;">from 6:45, with Maya</span>', mark='dot', color=GREEN)
        + line('Priya &middot; <span style="color: #6E6862;">just dinner · bread</span>', mark='dot', color=GREEN, last=True) + '</div>')
    return phone2(inner, active='Home')

# ── 4 · The morning after ──
def after():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 8px;"><span class="fn" style="color: {MUTE};">SUNDAY</span>{chip("JUST YOU")}</div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Nora&rsquo;s dinner, last night.</div>', top=10)
    inner += gut(box(person('M', 'Maya', 'from Nora&rsquo;s dinner &middot; the lemon argument')
        + f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 16px;">'
        + f'<div>{actions(btn("Remember Maya"))}<div style="margin-top: 8px;">{plain("You&rsquo;ll find her as &ldquo;Maya, from Nora&rsquo;s dinner.&rdquo;", INK2, 14, 20)}</div></div>'
        + f'<div>{actions(btn("Swap numbers", False))}<div style="margin-top: 8px;">{plain("She gets asked too. Two yeses, and you each have the other&rsquo;s.", INK2, 14, 20)}</div></div></div>'), top=16)
    inner += sect('Also from last night', top=26) + gut('<div>'
        + row('Priya &middot; <span style="color: #6E6862;">brought the bread</span>', mark='hollow')
        + row('The Sorrento recipe &middot; <span style="color: #6E6862;">Maya&rsquo;s version won</span>', mark='hollow', last=True) + '</div>')
    return webframe(inner)

def build():
    cols = [
        col(invitation(), cap('1', 'Sam&rsquo;s invitation', 'Everything on it is Nora&rsquo;s: her reason, her description of the evening, her one line about each friend. No guest wrote a profile. &ldquo;Join for either&rdquo; makes dinner-only an ordinary answer.', tags=(EX, PF, SHARED('EVERY GUEST')))),
        col(brief(), cap('2', 'A private question becomes his own request', 'Vesper cannot arrange a person. It says so, and Sam sends Nora his own words with his name on them.', tags=(EX, PRIV('SAM')))),
        col(host(), cap('3', 'Nora, and the friend who said yes', 'A signed request, a human agreement, and only then an answer for Sam. Priya is coming for dinner only, and that is simply what the list says.', tags=(EX, PRIV('NORA')))),
        col(after(), cap('4', 'The morning after', 'Two different acts. Doing nothing ends it.', tags=(EX, PRIV('SAM')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'One host, one guest who knows nobody else. No history, no app on the guest&rsquo;s side. This is a day-one case and arguably <i>the</i> day-one case: it is what every invitation to a non-user already is.'),
        ('HOST EFFORT', 'Two sentences about why him, three lines about the evening. Both optional &mdash; with nothing written, the invitation still works and simply says less. It never invents her reason for her.'),
        ('GUEST EFFORT', 'Read one page. Optionally type one sentence he would otherwise have had to say out loud to a room.'),
        ('OTHER GUESTS', 'Each chose the single line a newcomer sees about them. That is a real cost and an unresolved one: three more people doing a small thing for someone they have not met.'),
        ('AUDIENCE EFFECT', 'Three audiences: every guest sees the invitation; Sam alone sees his page; Nora receives what Sam chose to send, <b>signed</b>. An earlier draft sent it &ldquo;unsigned.&rdquo; In a group of four an unsigned request is not private &mdash; there is one newcomer &mdash; so the board no longer pretends it is.'),
        ('LOW PARTICIPATION', 'Sam can decline in one tap with no reason. After the dinner, &ldquo;let it end here&rdquo; is a first-class outcome and the default if he does nothing.'),
        ('ONE FAILURE', 'The foothold is wrong &mdash; Maya does not want to talk about the recipe. It must be ignorable and must never be presented as something she is expecting.'),
    ], [
        ('BASIC INTERACTION', 'Partiful and a text thread already do the invitation and the RSVP very well. Nothing here should be worse than that at the basics.'),
        ('WHAT IMPROVES, FOR WHOM', 'Sam: he knows what the evening is, that dinner-only is fine, and he is met at the door &mdash; without announcing anything to a room. Nora: one clear request instead of guessing what a newcomer needs. Maya: one small favor she chose to do. What stays human: Nora&rsquo;s invitation, Sam&rsquo;s request, Maya&rsquo;s yes.'),
        ('DIFFERENTIATING?', 'Yes, in two places an event tool does not reach: the newcomer&rsquo;s private page, and the morning after. Event products are strong up to the door and thin after it.'),
        ('SYSTEM ADVANTAGE', 'This is the growth loop and the social value on the same screen. The person receiving the most care here is the one who does not have the app.'),
        ('REJECTION TEST', 'Reject compatibility pairing, assigned icebreakers, a guest profile, and any line that tells Sam what someone thinks of him. Reject a required &ldquo;why you&rdquo; field &mdash; the gathering research calls that an unsupported chore.'),
    ], 'retain',
        'The largest territory the ten directions missed, and the most thoroughly researched in the repo. It also sits exactly on the invitation, which is where growth comes from.',
        'will three existing friends each write one line about themselves for a stranger &mdash; and if they will not, does the page still help Sam enough without it?',
        offscreen=['everything on the invitation is host-authored; no guest is asked to write about themselves', 'no account, profile or reason is needed to answer, and &ldquo;just dinner&rdquo; is an ordinary answer', 'Vesper does not arrange people: Sam&rsquo;s request goes to Nora in his words, signed, because he chose to send it', 'what Sam keeps to himself shapes only what Vesper suggests to Sam', 'Sam hears &ldquo;Maya can meet you&rdquo; only after Maya agreed', 'remembering someone is private; swapping numbers needs her yes too'],
        extras=('<b>Source:</b> gathering-psychology doc §5 (&ldquo;stairs but no ramps&rdquo;), §5.2 (five levels of feeling wanted), §6.5 (hospitality intelligence), §10 (the relationship gradient); canon §1.1.',
                '<b>Dependency:</b> the guest page rests on the same unresolved guest-identity and delivery decision as Social board 09.7. It is drawn as conditional.',
                '<b>Named omission:</b> a larger, less intimate gathering &mdash; twenty people, where topology matters more &mdash; is not drawn.'))
    return eboard('E1', 'E1 - Getting into the room', 'BELONGING', 'Getting into the room',
        'A person can be genuinely invited and still have no way in. The payoff is walking into a room of strangers without rehearsing, '
        'being looked after without having to explain why, and not losing someone worth knowing when the night ends. Four audiences, one evening. All fixture.',
        cols, nc, 4)

if __name__ == '__main__':
    print(build())
