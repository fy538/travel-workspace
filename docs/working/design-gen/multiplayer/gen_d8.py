"""D8 · Help us enjoy what we are already doing. Remove an obstacle, then recede."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
ASKED = tag('ASKED FOR', UMBER, 'rgba(74,52,40,0.10)')
CHANGED = tag('CHANGED SITUATION', OX, 'rgba(122,46,46,0.10)')

def chat_head(when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bubble(t, media=''):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; display: flex; flex-direction: column; gap: 8px; align-items: flex-end;">{media}<div style="background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div></div>'

# ── 1 · Mid-cooking ──
def sauce():
    inner = chat_head('SATURDAY 7:48 PM')
    inner += gut(bubble('it&rsquo;s gone grainy. can i save it?',
                        media=f'<div style="width: 210px; border-radius: 10px; overflow: hidden;">{plate("room", 130, tag="PHOTO &middot; YOURS")}</div>'), top=24)
    inner += gut(says('Pan off the heat, a splash of the pasta water, then stir hard. It usually comes back.'), top=18)
    inner += gut(quiet('Too much heat is the usual cause.'), top=10)
    return phone2(inner, active='Chat')

# ── 2 · Something changed ──
def changed():
    inner = anchor_row('NEW YORK', 'SATURDAY 3:20 PM')
    inner += orientation('The Print Room closed at 3:00 today.', 'You&rsquo;re meeting Maya there at 4:00.')
    inner += gut(dci('Notice', 96, tone='unavailable', title='Closed early · staff shortage', body='Gallery notice, 2:40 PM.'), top=16)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">TWO MINUTES AWAY, OPEN</div>'
        + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">The pier, then coffee on Van Brunt</div>'
        + f'<div style="margin-top: 8px;">{says("I&rsquo;d keep the same corner. You&rsquo;re both already heading to Red Hook.", 16, 23)}</div>'
        + dci('SourceList', 44, items='1=GALLERY NOTICE · 2:40 PM;2=CAF&Eacute; LISTING · SAT')), top=14)
    inner += sect('Your 4:00 with Maya') + gut('<div>' + row('Still set for the Print Room', mark='dashed', color=OX, last=True) + '</div>')
    inner += gut(actions(btn('Send this to Maya'), door('Leave it', MUTE)), top=14)
    return phone2(inner, active='Home')

# ── 3 · Apart, then together ──
def museum():
    inner = header('The Harbor Print Room', 'With Maya and Priya', back=True)
    inner += gut(quiet('Maya and Priya went ahead at 2:40.'), top=18)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px;">THE DRYING RACKS</div>'
        + says('They&rsquo;re the print shop&rsquo;s own. The show hangs new work on them.', 17, 24)
        + dci('SourceList', 30, items='1=GALLERY NOTES · TUE')), top=14)
    inner += sect('Here') + gut('<div>'
        + row('Two benches &middot; <span style="color: #6E6862;">the side room</span>', mark='dot', color=GOLDD)
        + row('Closes at 6:00 &middot; <span style="color: #6E6862;">listing, Tue</span>', mark='dot', color=GOLDD, last=True) + '</div>')
    inner += sect('Maya, Priya') + gut(bubble('side room whenever'))
    return phone2(inner, active='Places')

def build():
    cols = [
        col(sauce(), cap('1', 'Nine seconds, mid-cooking', 'A short question, a usable answer, and no follow-through of any kind.', tags=(EX, ASKED, PF))),
        col(changed(), cap('2', 'The situation changed; the agreement did not', 'A real closure reaches an agreed outing. Vesper prepares; the person decides and sends.', tags=(EX, CHANGED, SH('Notice')))),
        col(museum(), cap('3', 'Apart, then back together', 'Differing attention without synchronisation. One person holds a phone; three people benefit.', tags=(EX, SH('SourceList')))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'Frames 1 and 3 need nothing but the moment. Frame 2 needs one agreed arrangement between two people &mdash; the only prerequisite in the direction.'),
        ('WHO OPERATES', 'One person, on one phone. Nobody else installs, joins, opens a session or carries an active interface. This is the constraint the whole direction is built around.'),
        ('EFFORT', 'Frame 1: a photograph and six words. Frame 2: reading one card and deciding whether to send it. Frame 3: one ordinary message.'),
        ('KNOWN INPUTS', 'The photograph; the agreed four o&rsquo;clock; the gallery&rsquo;s own posted notice, labelled and timed. Not used: anyone&rsquo;s position, nobody&rsquo;s attention state.'),
        ('SHARED CONSEQUENCE', 'The heart of frame 2: an applied change to a shared arrangement is a different act from a fresh private option. The board refuses to let the product make it &mdash; it prepares, and a person sends.'),
        ('LOW PARTICIPATION', 'Frame 3&rsquo;s other two never open anything. Frame 1 ends with deliberate silence.'),
        ('ONE FAILURE', 'If the closure notice were wrong, the cost lands on two people standing outside a gallery. That is why it is sourced and timed on the card, not asserted.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Search and maps already answer frames 1 and 3 competently. A cook with a phone has always been able to look this up.'),
        ('DIFFERENTIATING?', 'Only frame 2, and specifically because the closure is matched to an arrangement that already exists. A maps notification tells you a place is shut; it does not know two people agreed to meet there at four.'),
        ('SYSTEM ADVANTAGE', 'This is the clearest instance of the changed-situation mode in the portfolio, and the clearest case where the advantage depends on the arrangement being a real object the rest of the app already holds.'),
        ('REJECTION TEST', 'Reject persistent narration. Reject unsolicited tasks. Reject anything that keeps a group on their phones. Reject a &ldquo;together mode&rdquo; adopted before frame 2 is shown to be worth its interruption.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('retain',
        'Frame 2 is the portfolio&rsquo;s best argument for the whole product. Frames 1 and 3 are good manners and thin differentiation &mdash; keep them as constraints on frame 2, not as separate claims.',
        'what is the true cost of being wrong? A changed-situation interruption that is unhelpful twice is worse than one that never arrives, and no static canvas can measure that rate.')
        + N('<b>Named omission:</b> the brief asks for at least one scene combining enrichment with practical conditions. '
            'Frame 3 does that thinly &mdash; the explanation and the bench sit side by side rather than genuinely interacting.')
        + N('<b>Hypothesis, not requirement:</b> a separate &ldquo;together mode&rdquo; is not drawn anywhere here, deliberately.')
        + N('<b>Decided, not displayed:</b> no follow-up question, no &ldquo;how did it go?&rdquo; &middot; the situation changed by itself; the arrangement changes only when a person sends it &middot; Maya is not told until Nora tells her &middot; nobody&rsquo;s position or attention is shared &middot; one person operates the app; nobody else installs or joins anything.'), w=440)
    return write('D8 - Help us enjoy this moment', board(
        bw(3, (600, 520, 440)), hh('D8', 1900),
        'D8 &middot; BEING TOGETHER &middot; EXPLORATORY',
        'Help us enjoy what we are already doing',
        'Help with this moment, then let us continue. A useful intervention removes an obstacle or returns attention to the world '
        'and the people present. One asked-for answer, one changed situation, one afternoon apart and back together. All fixture.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
