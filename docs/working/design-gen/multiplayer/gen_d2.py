"""D2 · A living shared world for a small circle. Things that belong to a continuing friendship, available without curation."""
from mp_kit2 import *

EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

def chat_head(when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bubble(t):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div>'

# ── 1 · Asked ──
def asked():
    inner = chat_head('SATURDAY 11:20 AM')
    inner += gut(bubble('what were those places we were talking about?'), top=24)
    inner += gut(says('Four, since June. You&rsquo;ve been to two of them.'), top=18)
    inner += gut('<div>'
        + row('The Harbor Print Room &middot; <span style="color: #6E6862;">Maya, Thursday</span>', mark='dot', color=GOLDD)
        + row('Red Hook on foot, three stops &middot; <span style="color: #6E6862;">Priya, August</span>', mark='dot', color=GOLDD)
        + row('The Lantern &middot; <span style="color: #6E6862;">Sam, Wednesday</span>', mark='hollow', color=GOLDD)
        + row('The greenmarket &middot; <span style="color: #6E6862;">you, twice</span>', mark='hollow', color=GOLDD, last=True) + '</div>', top=14)
    inner += gut(actions(door('Put them on a map')), top=10)
    return phone2(inner, active='Chat')

# ── 2 · Nobody asked ──
def unprompted():
    inner = anchor_row('NEW YORK', 'TUESDAY 6:05 PM')
    inner += orientation('Rain from six.', 'Tuesday &middot; 54&deg; &middot; pasta again Thursday.')
    inner += sect('For your Thursday pasta') + gut(
        original(110, author='Priya', meta='SUNDAY · TO YOU AND MAYA', words='did the cheese off the heat, a handful at a time. it held. also half the pepper')
        + f'<div style="margin-top: 14px;">' + dci('FactPair', 92, tone='plain', a='YOURS', av='Cheese in over the flame', an='YOU · THURSDAY',
              b='HERS', bv='Pan off the heat, cheese in thirds', bn='PRIYA · SUNDAY') + '</div>'
        + f'<div style="margin-top: 6px;">{actions(door("Open your Thursday photo"), door("Reply"))}</div>')
    return phone2(inner, active='Home')

# ── 3 · The circle, at rest ──
def quiet_circle():
    inner = header('Maya, Priya and you', 'Since 2019', back=True)
    inner += gut(says('Last together: Priya&rsquo;s pasta, three weeks ago.', 17, 24, INK2), top=18)
    inner += sect('Between the three of you') + gut('<div>'
        + row('Four places one of you mentioned', mark='hollow')
        + row('Priya&rsquo;s change to the pasta', mark='hollow')
        + row('September&rsquo;s dinner', mark='hollow', last=True) + '</div>')
    inner += gut(pl_ending(['Everyone, in Life']), top=24)
    return phone2(inner, active='Life')

def inset_membership():
    body = (N('Sam joins the three of you in October.')
            + box(plain('Sam sees what&rsquo;s shared with him from October on.', size=14, lh=20), '12px 14px')
            + N('<b>Not decided by this drawing:</b> whether a circle has membership at all, whether anyone can add a fourth person, and whether a contributor can later widen their own past contribution.'))
    return inset('3, THE SAME VIEW &middot; SOMEONE NEW', body, 'HISTORICAL ACCESS AND MEMBERSHIP ARE POLICY DEPENDENCIES')

def build():
    cols = [
        col(asked(), cap('1', 'Asked: &ldquo;what were those places?&rdquo;', 'Retrieval across three people, every line still attributed. Nobody curated anything.', tags=(EX, PF))),
        col(unprompted(), cap('2', 'Nobody asked: her change is already there', 'The unprompted case. A friend&rsquo;s variation arrives beside your own dish, with the actual difference.', tags=(EX, SH('FactPair')))),
        col(quiet_circle() + inset_membership(), cap('3', 'Three weeks of nothing', 'An inactive circle with no guilt copy, plus what happens when someone joins.', tags=(EX,))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'Real history: at least one prior contribution from someone else, and in frame 2 a dish of your own to compare against. This direction genuinely cannot run on day one, and the canvas does not pretend it can.'),
        ('SENDER EFFORT', 'Priya cooked and wrote two sentences. She did not label, tag, file or curate. That is the whole ask.'),
        ('RECIPIENT EFFORT', 'Frame 2 costs nothing: it is already on Home. Frame 1 costs one plain question.'),
        ('AUDIENCE EFFECT', 'Priya chose the three of them. Nothing widens. Nothing becomes a durable group object because she cooked.'),
        ('LOW PARTICIPATION', 'Frame 3 is the honest majority case &mdash; weeks where nobody does anything. It must read as fine, not as a lapsed subscription.'),
        ('ONE CHANGE', 'Someone joins. The inset says what he can and cannot see, and names the parts a mockup does not get to decide.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Message search and pinned items already do frame 1. Competently. Relocating them is not a benefit.'),
        ('DIFFERENTIATING?', 'Only frame 2 is a real candidate: her change reaches the dish it modifies, without anyone maintaining a shared recipe. Frame 1 on its own does <b>not</b> demonstrate an inhabited shared world &mdash; it demonstrates better search.'),
        ('SYSTEM ADVANTAGE', 'Plausible but unproven here: contributions land beside the thing they change rather than in a group feed. That claim needs the object model to hold across roots, which no single canvas can show.'),
        ('REJECTION TEST', 'Reject a friendship workspace whose upkeep exceeds its value. Reject a persistent circle destination adopted before the unprompted arrival is shown to work.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('rework',
        'The unprompted arrival is the idea worth keeping; the circle destination is not yet earned. Explore frame 2 further before drawing any group surface.',
        'does a shared context feel inhabited without a place to go and look at it &mdash; or does removing the destination quietly remove the belonging?')
        + N('<b>Named omission:</b> the brief asks what several people&rsquo;s contributions add beyond a pair. '
            'This board shows one contributor. The three-or-more case is not explored.')
        + N('<b>Dependency:</b> membership and historical access are policy, owned outside this exploration.')
        + N('<b>Decided, not displayed:</b> every line stays attributed; nothing was collected or curated to make the list &middot; no streak, score, or count of how often the three talk &middot; no prompt to plan something &middot; no merged taste profile &middot; a newcomer inherits no back catalogue.'), w=440)
    w = bw(3, (600, 520, 440))
    return write('D2 - A living shared world', board(
        w, hh('D2', 1900),
        'D2 &middot; FEELING INVOLVED &middot; EXPLORATORY',
        'A living shared world for a small circle',
        'Some things belong to a continuing friendship rather than to one event. The payoff is that they stay available '
        'without reconstructing message history or appointing someone to curate a shared workspace. '
        'Cast, dish, dates and places are fixtures.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
