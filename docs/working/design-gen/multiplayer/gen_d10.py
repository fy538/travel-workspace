"""D10 · The next time is better. Continuity without a journal."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

# ── 1 · What is kept, and how it got there ──
def kept():
    inner = header('September&rsquo;s dinner', 'Saturday the 19th &middot; four people', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 150, tag="PHOTO &middot; SAM &middot; 8:25 PM")}</div>', top=18)
    inner += sect('Kept from that evening') + gut(
        original(80, author='Sam', meta='SEPT 19 · PHOTO, TO THE FOUR OF YOU', words='the table 🍝')
        + f'<div style="margin-top: 16px;">{rule(original(96, author="Priya", meta="SEPT 20 · TO YOU", words="did the cheese off the heat, a handful at a time. it held"), 16)}</div>'
        + f'<div style="margin-top: 16px;">{rule(original(96, author="Sam", meta="SEPT 20 · TO YOU", words="Great night! 7 was a scramble for me though."), 16)}</div>')
    return phone2(inner, active='Life')

# ── 2 · Months later ──
def later():
    inner = anchor_row('NEW YORK', 'THURSDAY 5:40 PM')
    inner += orientation('Pasta again Saturday.', 'Two things from September&rsquo;s messages.')
    inner += gut(box(dci('FactPair', 96, tone='plain', a='LAST TIME', av='Cheese in over the flame. 7:00.',
              an='SEPT 19', b='THIS TIME', bv='Off the heat, in handfuls. 7:30?', bn='PRIYA · SAM, SEPT 20')
        + f'<div style="margin-top: 12px;">{says("Sam said 7:00 was a scramble, so I&rsquo;d ask people for 7:30.", 16, 23)}</div>'
        + f'<div style="margin-top: 4px;">{actions(door("See their messages"))}</div>'), top=16)
    return phone2(inner, active='Home')

# ── 3 · Correct it, or let it lapse ──
def correct():
    inner = header('From September&rsquo;s dinner', 'Two messages and a photo', back=True)
    inner += gut(original(96, author='Sam', meta='SEPT 20 · TO YOU', words='Great night! 7 was a scramble for me though.'), top=18)
    inner += gut(actions(door('Don&rsquo;t use this'), door('Remove from Life', MUTE)), top=8)
    inner += gut(dci('Notice', 64, tone='applied', title='Won’t be used', body='Sam’s message stays in your thread with him.'), top=14)
    inner += sect('Sam&rsquo;s photo') + gut(plain('Here through November.', INK2, 14, 20))
    return phone2(inner, active='Life')

def build():
    cols = [
        col(kept(), cap('1', 'Three small things, all someone&rsquo;s', 'Two messages people sent and one photo. Nothing here was said out loud and captured; each piece arrived because its author sent it.', tags=(EX, PF))),
        col(later(), cap('2', 'Months later: the specific difference', 'Not a recap. Two changes and the reason for each.', tags=(EX, SH('FactPair')))),
        col(correct(), cap('3', 'Disagree with it, or let it lapse', 'Inspection, correction, and an ending where nothing is renewed.', tags=(EX, SH('Notice')))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'The most context-dependent direction in the portfolio: one prior shared occasion, months earlier. It cannot run on day one, and pretending otherwise would be the easiest lie on these boards.'),
        ('WHAT IT NEEDS', 'Honestly tested in frame 2: one retained line from Priya is enough to change something. The photograph and the timing remark improve it; they are not required for it to work.'),
        ('EFFORT AT THE TIME', 'None. Nobody debriefed, rated, or captured anything. Priya said a sentence in a kitchen and Sam took a photograph he wanted anyway.'),
        ('EFFORT LATER', 'Reading two lines. The difference is presented; nothing is searched for.'),
        ('RETENTION AND OWNERSHIP', 'Every piece stays its author&rsquo;s. Sam&rsquo;s photograph lives under his grant and leaves when the grant lapses &mdash; drawn in frame 3 as a normal ending, not a loss to be prevented.'),
        ('LOW PARTICIPATION', 'Frame 3: the correction is private and nobody is told they were wrong. Letting it lapse is offered beside correcting it.'),
        ('ONE FAILURE', 'The retained line is wrong, or contested. Two people may remember the evening differently and the product does not adjudicate.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Searching messages and photo albums genuinely works, and people do it. A prettier recap is not an improvement.'),
        ('DIFFERENTIATING?', 'Yes, narrowly: the lesson arrives <i>at the moment it can be used</i> &mdash; Thursday, before Saturday&rsquo;s cooking &mdash; rather than being something you must think to go and look for. Retrieval is the ordinary app&rsquo;s job; arrival is not.'),
        ('SYSTEM ADVANTAGE', 'The strongest claim in the portfolio, and the slowest to verify: it needs months of real retention across several people before it can be observed at all.'),
        ('REJECTION TEST', 'Reject compulsory debriefs and comprehensive capture. Reject a shared journal. Reject turning every memory into an action prompt. Reject inheriting a guest list, a preference or an availability from the last time.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('retain',
        'Keep, and treat it as the portfolio&rsquo;s long bet. It is the direction whose value most depends on the rest of the app doing its job quietly for months.',
        'what is genuinely better next time &mdash; and would the single retained line from Priya have been enough on its own, without the photograph or the timing remark?')
        + N('<b>Named omission:</b> the brief&rsquo;s alternative scene &mdash; returning to a neighbourhood and finding something not tried last time, plus a new friend&rsquo;s tip &mdash; is not drawn. '
            'Emotional continuity is also under-drawn here relative to practical continuity; the CHI 2026 review suggests the practical side is the under-explored one, which is why it leads.')
        + N('<b>Dependency:</b> retention windows and grant expiry are Contribution-and-Consequence policy, not decided by this canvas.')
        + N('<b>Decided, not displayed:</b> past attendance is never a guest list for next time &middot; nobody is asked to debrief, rate or capture &middot; a correction is private; nobody is told they were wrong &middot; a lapsed grant leaves without a renewal prompt &middot; two people may remember it differently and the product does not adjudicate.'), w=440)
    return write('D10 - The next time is better', board(
        bw(3, (600, 520, 440)), hh('D10', 1900),
        'D10 &middot; CARRYING FORWARD &middot; EXPLORATORY',
        'The next time is better',
        'We should not have to start from zero every time. Useful pieces of shared life stay available when they can improve the '
        'present, without anyone maintaining a journal. One evening, three retained things, one later Saturday. All fixture.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
