"""D3 · Borrowing experience and perspective. A known person's contribution plus work beyond repeating it."""
from mp_kit2 import *

EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
VA = tag('VARIANT A &middot; PRACTICAL', UMBER, 'rgba(74,52,40,0.10)')
VB = tag('VARIANT B &middot; PERCEPTUAL', PLAN, 'rgba(42,56,75,0.10)')

def chat_head(when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 305px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'

# ── A · Practical ──
def practical():
    inner = chat_head('FRIDAY 4:40 PM')
    inner += gut(bubble('which of maya&rsquo;s places would work for a relaxed afternoon with my parents?'), top=24)
    inner += gut(says('I&rsquo;d take them to the Print Room on a weekday. It&rsquo;s step-free, and the side room has two benches.'), top=18)
    inner += gut(original(200, author='Maya', meta='THURSDAY · TO FRIENDS', words='The side room was my favorite. Go on a weekday, it was empty.',
                          place='The Harbor Print Room', placeMeta='STEP-FREE, LIFT · GALLERY PAGE, TUE'), top=16)
    inner += sect('Still open') + gut('<div>'
        + row('Saturdays &middot; <span style="color: #6E6862;">Maya went on a Thursday</span>', mark='dashed', color=MUTE)
        + row('Today&rsquo;s hours &middot; <span style="color: #6E6862;">listed Tue&ndash;Sun 11:00&ndash;6:00</span>', mark='dashed', color=MUTE, last=True) + '</div>')
    return phone2(inner, active='Chat')

# ── B · Perceptual ──
def perceptual():
    inner = header('Your cliff and Dana&rsquo;s', 'Sorrento, August &middot; Marseille, this week', back=True)
    inner += gut(f'<div style="display: flex; gap: 10px;">'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("room", 140, tag="SORRENTO &middot; YOURS &middot; AUG")}</div>'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("pier", 140, tag="SUGITON &middot; DANA")}</div></div>', top=18)
    inner += gut(says('Two pale coasts on the same sea, made of different things. Yours is volcanic tuff, in cliffs about fifty meters high. Hers is hard white limestone: valleys cut when the sea stood far lower, then flooded when it rose.', 18, 25), top=14)
    inner += gut(dci('FactPair', 108, tone='lead', a='YOURS &middot; SORRENTO', av='Volcanic tuff, cliffs about 50 m', an='FROM THE CAMPANIAN IGNIMBRITE',
                     b='HERS &middot; SUGITON', bv='Limestone valleys, later flooded', bn='ICE-AGE SEA ABOUT 130 M LOWER'), top=14)
    inner += gut(dci('SourceList', 58, items='1=PARC NATIONAL DES CALANQUES · GEOLOGY AND LANDSCAPES;2=J. SEISMOLOGY, 2022 · TUFF CLIFF, SORRENTO PENINSULA;Y=YOUR PHOTO · AUG;D=DANA · TO YOU · TUE'), top=12)
    inner += gut(actions(door('Send to Dana')), top=10)
    return phone2(inner, active='Life')

# ── B′ · Nothing to connect: the original, as sent ──
def nolink():
    inner = bar('FROM FRIENDS')
    inner += gut(original(200, author='Sam', meta='WEDNESDAY · TO FRIENDS',
        words='Found a cinema on Court Street that shows one film a week. They sell exactly one kind of cake. I think I love it here!',
        place='The Lantern', placeMeta='TONIGHT 7:15 · 9 MIN AWAY · LISTING THU', door='Reply'), top=18)
    inner += gut(pl_ending(['Everything from Sam']), top=24)
    return phone2(inner, active='Home')

def build():
    cols = [
        col(practical(), cap('1', 'Her observation, against constraints she never heard', 'The recipient&rsquo;s parents stay private. Her sentence stays hers; the practical parts are marked as other sources.', tags=(EX, VA, SH('SourceList')))),
        col(perceptual(), cap('2', 'Two originals, one earned connection', 'The payoff is something the viewer had not noticed &mdash; why one coast has towns and the other has an arch.', tags=(EX, VB, SH('FactPair')))),
        col(nolink(), cap('3', 'The case where there is nothing to connect', 'Most pairs are this. The honest output is the original and silence.', tags=(EX,))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'One contribution from one friend. Variant B needs a second original, which may be the recipient&rsquo;s own. No circle, no history.'),
        ('SENDER EFFORT', 'Maya wrote one sentence once, months earlier. Being useful here must never make her a standing adviser or generate a request she has to answer.'),
        ('RECIPIENT EFFORT', 'One question in variant A. In variant B, nothing: the pairing is already drawn when she opens it.'),
        ('KNOWN INPUTS', 'Maya&rsquo;s words and her audience; the recipient&rsquo;s stated constraint; clearly labelled third-party facts. Not known: anything Maya did not establish, which frame 1 lists rather than quietly filling in.'),
        ('AUDIENCE EFFECT', 'Nothing travels back. Maya is not told the question was asked, and the parents are never exposed to her.'),
        ('LOW PARTICIPATION', 'Neither variant needs a reply. The voluntary message to Dana is a door, not a repayment step.'),
        ('ONE FAILURE', 'Frame 3: no connection exists. The failure mode to fear is a plausible-sounding bridge, not an empty one.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Saved pins plus a general chatbot answer is a capable alternative and should be credited as one.'),
        ('DIFFERENTIATING?', 'Yes, if and only if a source-specific detail changes the result. Here it is exactly one thing: <i>empty on a weekday</i>, which no general answer would produce and which is the reason the Print Room wins for the parents.'),
        ('SYSTEM ADVANTAGE', 'Variant B is the stronger claim &mdash; it needs her photograph, your photograph, and the permission linking them, which a standalone assistant does not have. It also risks the most: a charming comparison that teaches nothing.'),
        ('REJECTION TEST', 'Reject superficial matches. Reject stale practical claims presented as current. Reject borrowing anything beyond the audience it was shared with. Reject &ldquo;you both love dramatic landscapes.&rdquo;'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('retain',
        'Keep both variants, separately. A is the clearest differentiating benefit in the portfolio; B is the most distinctive and the least proven.',
        'how often does a real pair of contributions actually support an earned connection &mdash; and can the product tell that case from a plausible one before it draws it?')
        + N('<b>Named omission:</b> the Italy/Paris contrast the brief mentions is drawn here as geology. '
            'The version that contrasts two people&rsquo;s <i>experiences</i> without implying equivalence is not explored.')
        + N('<b>Decided, not displayed:</b> Maya is never told the question was asked, or that the parents are visiting &middot; her sentence stays hers; practical additions carry their own source &middot; no claim that two people share a taste &middot; when no connection is earned, the original is shown alone and nothing is said about it.'), w=440)
    w = bw(3, (600, 520, 440))
    return write('D3 - Borrowing experience and perspective', board(
        w, hh('D3', 1900),
        'D3 &middot; EXPANDING MY WORLD &middot; EXPLORATORY',
        'Borrowing experience and perspective',
        'Show me something I would not find, understand, or confidently try alone. A known person&rsquo;s contribution supplies '
        'the perspective; the product does work beyond repeating it. Two variants and one honest failure. '
        'Photographs, people, sources and geology are fixtures.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
