"""E8 · Keeping a secret together. The moat made delightful: private context shaping a shared day, undisclosed, without a lie."""
from mp_kit2 import *

# ── 1 · Set up ──
def setup():
    inner = bar('CHAT', 'MONDAY 9:05 PM')
    inner += gut(bubble('surprise dinner for priya&rsquo;s bday. sat the 14th, 7, mine. she can&rsquo;t know'), top=22)
    inner += gut(says('A surprise for Priya, then. Who&rsquo;s in on it?'), top=16)
    inner += gut(bubble('maya and dana'), top=12)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px; color: {GOLDD};">SURPRISE</div>'
        + f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 26px;">Priya&rsquo;s birthday</div>'
        + f'<div style="margin-top: 2px;">{plain("Saturday the 14th, 7:00, your place", INK2)}</div>'
        + f'<div style="margin-top: 14px;">{faces("MD", "Asked just now. No answers yet.")}</div>'
        + f'<div style="margin-top: 10px;">{quiet("Priya sees it when you open it to her.")}</div>'), top=14)
    return phone2(inner, active='Chat')

# ── 2 · Priya's own Saturday ──
def hers():
    inner = avatar_for(bar('CHAT', 'THURSDAY 1:30 PM'), 'P')
    inner += gut(bubble('what should i do saturday night?'), top=22)
    inner += gut(says('You&rsquo;ve got dinner with Maya at 7:00. Want something for the afternoon before it?'), top=16)
    inner += gut(prov('MAYA &middot; ASKED YOU TUESDAY'), top=2)
    inner += gut(actions(door('Yes, something nearby'), door('I&rsquo;m good', MUTE)), top=10)
    return phone2(inner, active='Chat')

# ── 3 · The three of them ──
def conspirators():
    inner = header('Priya&rsquo;s birthday', 'Surprise &middot; you, Maya, Dana', back=True)
    inner += gut(original(80, author='Maya', meta='MONDAY · TO YOU AND DANA', words='in!! i&rsquo;ll get her there. telling her it&rsquo;s dinner w me'), top=18)
    inner += gut(rule(faces('D', 'Dana · asked Monday, hasn&rsquo;t answered', 24)), top=14)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">A GIFT, IF YOU WANT ONE</div>'
        + f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 25px;">The print from the Print Room, about $35 each</div>'
        + f'<div style="margin-top: 10px;">' + original(80, author='Maya', meta='THURSDAY · TO FRIENDS', words='priya stood in front of this for ten minutes') + '</div>'), top=16)
    inner += sect('For the cook') + gut(plain('Priya&rsquo;s allergic to walnuts.') + prov('PRIYA &middot; ALLERGIES, SHARED WITH FRIENDS'))
    return phone2(inner, active='Home')

# ── 4 · Nora opens it ──
def reveal():
    inner = header('Priya&rsquo;s birthday', 'Saturday 7:04 PM', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 160, tag="PHOTO &middot; DANA &middot; 7:04 PM")}</div>', top=18)
    inner += gut(box(says('Open it to Priya?', 18, 25)
        + f'<div style="margin-top: 6px;">{plain("She&rsquo;ll see tonight, who came, and Dana&rsquo;s photo. The planning stays with the three of you.", INK2, 14, 20)}</div>'
        + f'<div style="margin-top: 12px;">{actions(btn("Open it to Priya"), door("Later", MUTE))}</div>'), top=14)
    return phone2(inner, active='Home')

def inset_priya():
    body = (N('Priya&rsquo;s Home on Sunday, after Nora opened it.')
            + box(plain('Your birthday dinner, last night.', size=16, lh=22) + f'<div style="margin-top: 4px;">{plain("Nora opened it to you at 7:04.", MUTE, 13, 18)}</div>', '12px 14px'))
    return inset('4 &middot; WHAT PRIYA THEN SEES', body, 'OPENING IS NORA&rsquo;S ACT, NOT SOMETHING THAT HAPPENS WHEN A DOOR OPENS')

def build():
    cols = [
        col(setup(), cap('1', 'Set up, and two friends asked', 'Nora names who is in on it. They have been asked; nobody is &ldquo;in&rdquo; until they say so.', tags=(EX, PF, PRIV('NORA')))),
        col(hers(), cap('2', 'Priya asks about Saturday', 'Nothing disclosed and nothing untrue said: Maya really did ask her to dinner.', tags=(EX, PRIV('PRIYA')))),
        col(conspirators(), cap('3', 'The three of them', 'Maya said yes in her own words. Dana has not answered, and the screen says that. The allergy is stated plainly to the person cooking.', tags=(EX, PRIV('THE THREE')))),
        col(reveal() + inset_priya(), cap('4', 'Nora opens it', 'The reveal is something a person does, with a preview of what Priya will and will not see.', tags=(EX, PRIV('NORA')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'Two conspirators and one person being surprised. Works with no history at all. The allergy was already shared with her friends; nothing private of Priya&rsquo;s is used.'),
        ('ORGANIZER EFFORT', 'One sentence. The rest is the ordinary work of a surprise, which people enjoy and should keep.'),
        ('SUBJECT EFFORT', 'None, by definition. Frame 2 is the only contact she has with it, and she does not know it happened.'),
        ('KNOWN INPUTS', 'Nora&rsquo;s sentence; Maya&rsquo;s reply; a photo Maya shared with friends; and Priya&rsquo;s allergy, which she had already shared with her friends. An allergy is a safety fact and is shown plainly. An earlier draft hid it like a budget preference; those are not the same kind of thing. A private spending limit, if someone had one, would narrow the gift ideas without being shown.'),
        ('AUDIENCE EFFECT', 'A deliberately exclusive audience with a stated end. At the reveal the shared core opens to her; each person&rsquo;s contributions and the planning thread stay under their authors&rsquo; control.'),
        ('LOW PARTICIPATION', 'Dana never opens the app: she still gets one line by text about Friday&rsquo;s collection. The subject participating is, of course, the failure case.'),
        ('ONE FAILURE', 'A leak. It is a one-shot failure with no recovery, which is the argument for making exclusion structural &mdash; she is not in the audience &mdash; rather than a filter applied to what she is shown.'),
    ], [
        ('BASIC INTERACTION', 'A group chat without her in it. That is how every surprise is organised today and it works. The chat cannot stop her own assistant, calendar or shared album from giving it away.'),
        ('WHAT IMPROVES, FOR WHOM', 'Priya: a surprise that her own assistant does not spoil. Nora: she can see who has actually answered. The cook: an allergy in front of her, not buried in an old thread. This is a useful stress case for trust, not the lead proof of the product.'),
        ('DIFFERENTIATING?', 'Yes, and it grows with the product: the more Vesper is part of Priya&rsquo;s ordinary week, the more a surprise needs it to be trustworthy. No chat app has that problem, and so none can solve it.'),
        ('SYSTEM ADVANTAGE', 'The foundations doc already states the principle for a proposal on Capri: &ldquo;a private protected anchor may legitimately shape a shared day without being disclosed.&rdquo; Nobody has drawn the everyday version.'),
        ('REJECTION TEST', 'Reject any untrue statement to the subject, including by omission dressed as a suggestion. Reject steering her. Reject protected anchors that outlive their stated end, and any use of this to keep someone out of something that concerns their safety, money or consent.'),
    ], 'retain',
        'Keep it as a celebration and trust stress case. Frame 2 is where the line is held or lost. It is not the first thing to show anyone about this product.',
        'is &ldquo;she is not in the audience&rdquo; enough of a rule &mdash; or does a product that can keep a happy secret from someone need a founder-level boundary on which secrets it will keep?',
        offscreen=['Priya is not in the surprise&rsquo;s audience until Nora opens it to her', 'Vesper says nothing untrue to Priya: Maya&rsquo;s invitation is real, and without it Saturday would read as free', 'asked is not in: Dana stays &ldquo;hasn&rsquo;t answered&rdquo; until she answers', 'an allergy is shown plainly to the cook; a private spending limit would narrow gift ideas without being shown', 'opening it is Nora&rsquo;s act; the planning thread stays with its authors'],
        extras=('<b>Source:</b> foundations doc §3.14 (the Capri proposal, protected anchor, arrival-state quality); canon §1.2 rule 6 (&ldquo;private input may constrain a group-safe result &hellip; the shared explanation does not reveal the private rationale&rdquo;); Interaction Design §13 (pattern-detection defence). No document proposes surprise, gifts or celebration as a social direction.',
                '<b>Ruling needed:</b> the limits of a protected anchor. Duration, who may set one about whom, and what it may never cover are policy, not design.',
                '<b>Named omission:</b> milestones that are not surprises &mdash; an anniversary, a farewell &mdash; and generosity without secrecy, such as treating someone, are not drawn.'))
    return eboard('E8', 'E8 - Keeping a secret together', 'BEING TOGETHER', 'Keeping a secret together',
        'Some of the best things people do for each other depend on one person not knowing. The payoff is a surprise that the product helps hold rather than threatens, '
        'shaped by private limits nobody sees &mdash; and an assistant that stays silent without ever saying something untrue. All fixture.',
        cols, nc, 4)

if __name__ == '__main__':
    print(build())
