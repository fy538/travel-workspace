"""D9 · Something playful between us. Enjoyment as the complete outcome."""
from mp_kit2 import *
EX = tag('EXPLORATORY', OX, 'rgba(122,46,46,0.10)')
PF = tag('PROPOSED FIXTURE', MUTE, 'rgba(110,104,98,0.10)')
SH = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
EMERGED = tag('EMERGES FROM MATERIAL', UMBER, 'rgba(74,52,40,0.10)')
CHOSEN = tag('DELIBERATELY CHOSEN', PLAN, 'rgba(42,56,75,0.10)')

# ── 1 · What each of you noticed ──
def noticed():
    inner = header('The same walk', 'You and Priya, Saturday', back=True)
    inner += gut(f'<div style="display: flex; gap: 10px;">'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("pier", 130, tag="YOURS &middot; THE CRANES")}</div>'
        f'<div style="flex: 1; border-radius: 12px; overflow: hidden;">{plate("room", 130, tag="PRIYA&rsquo;S &middot; A DOOR")}</div></div>', top=18)
    inner += gut(says('Two hours, the same three streets. You photographed the harbor four times. Priya photographed six doors and no water at all.', 19, 26), top=14)
    inner += gut(actions(btn('Send to Priya'), door('Keep', MUTE)), top=16)
    return phone2(inner, active='Life')

# ── 2 · Something left on purpose ──
def surprise():
    inner = anchor_row('NEW YORK', 'TUESDAY 8:15 AM')
    inner += orientation('Rain until noon.', 'Tuesday &middot; 52&deg;')
    inner += sect('From Maya') + gut(original(190, author='Maya', meta='SUNDAY · TO YOU',
        words='third rack from the back at the print room. look at what someone wrote on the underside',
        place='The Harbor Print Room', placeMeta='TUE–SUN 11:00–6:00 · LISTING TUE', door='Reply'))
    return phone2(inner, active='Home')

def build():
    cols = [
        col(noticed(), cap('1', 'What each of you noticed', 'Play out of material that already exists. No captures, no prompts, no homework.', tags=(EX, EMERGED, PF))),
        col(surprise(), cap('2', 'Something left on purpose &mdash; and ignored', 'A deliberately chosen small activity, with the recipient who never participates.', tags=(EX, CHOSEN, PF))),
    ]
    n1 = notes('WHAT ARRIVES, AND WHAT IT COSTS', led([
        ('MINIMUM CONTEXT', 'Frame 1 needs two people&rsquo;s photographs of one occasion &mdash; modest, but real, and it cannot be faked on day one. Frame 2 needs nothing but a place and a sentence.'),
        ('EFFORT', 'Frame 1: nobody did anything extra; the material was already made. Frame 2: Maya wrote one sentence and chose one person.'),
        ('ASYMMETRY', 'Normal and explicitly drawn. You can enjoy frame 1 without submitting a matching photograph, and Priya can ignore frame 2 entirely.'),
        ('AUDIENCE EFFECT', 'Frame 2 goes to one person and never widens. A surprise must not expose a location or reveal that someone did or did not go.'),
        ('LOW PARTICIPATION', 'Drawn as the second half of frame 2 rather than as an inset: not going is the ordinary outcome and it expires in silence.'),
        ('ONE FAILURE', 'The real failure is not technical. It is that the joke is not funny, which the design cannot fix and should not paper over with charm.'),
    ]), w=600)
    n2 = notes('COMPARED WITH AN ORDINARY APP', led([
        ('BASIC INTERACTION', 'Friends already joke in messages, and messages are very good at it. This is the direction where the ordinary alternative is strongest.'),
        ('DIFFERENTIATING?', 'Frame 1 only: neither person could assemble that comparison from their own camera roll, because half the material is the other person&rsquo;s. That is a genuine capability and a slight one.'),
        ('SYSTEM ADVANTAGE', 'None claimed. Frame 2 is a message with a place attached and should be described that way.'),
        ('REJECTION TEST', 'Reject streaks, leaderboards and forced icebreakers. Reject any engagement mechanic wearing friendship as a costume. Reject making a normal outing carry a capture tax so that play is possible later.'),
    ]), w=520)
    n3 = notes('VERDICT', verdict('defer',
        'Only two frames, and that is the honest amount. Frame 1 is worth keeping as a by-product of D10&rsquo;s retention rather than as a direction of its own; frame 2 is a message with a place on it.',
        'would anyone voluntarily do it a second time without a reminder? The brief says this needs human evidence, and it does &mdash; no drawing can answer it, and a charming presentation is exactly how a bad answer gets hidden.')
        + N('<b>Named omission:</b> the brief&rsquo;s third scene &mdash; amusing differences from a cooking experiment &mdash; is not drawn. '
            'A deliberately chosen longer activity is also not drawn, because nothing here justifies proposing one yet.')
        + N('<b>Deliberately under-invested:</b> polishing this direction would make it look more convincing than the evidence supports.')
        + N('<b>Decided, not displayed:</b> no streak, score or count of who played &middot; Maya is never told whether you went &middot; an unused surprise ends quietly; nobody is reminded &middot; nothing was captured on purpose to make frame 1 possible.'), w=440)
    return write('D9 - Something playful between us', board(
        bw(2, (600, 520, 440)), hh('D9', 1700),
        'D9 &middot; BEING TOGETHER &middot; EXPLORATORY',
        'Something playful between us',
        'That was fun and gave us something to enjoy together. Enjoyment can be the complete outcome &mdash; no learning, planning '
        'or artifact required. Two frames, which is all this direction currently earns. All fixture.',
        cols, (n1, n2, n3)))

if __name__ == '__main__':
    print(build())
