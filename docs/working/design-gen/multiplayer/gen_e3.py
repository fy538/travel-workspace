"""E3 · Seeing more through each other. From preference coordination to shared perception."""
from mp_kit2 import *

def lane(letter, who, what, n):
    return (f'<div style="display: grid; grid-template-columns: 32px 1fr; column-gap: 12px; align-items: start; padding: 10px 0; border-bottom: 1px solid rgba(27,23,20,0.06);">'
            f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: {CARD}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700;">{letter}</span>'
            f'<div><div style="font-size: 15px; line-height: 20px; color: {INK};">{who} <span style="color: {MUTE};">&middot; {n}</span></div>'
            f'<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 2px;">{what}</div></div></div>')

# ── 1 · One walk, three layers ──
def noticed():
    inner = header('Red Hook, Saturday', 'You, Priya and Maya', back=True)
    inner += gut('<div>'
        + lane('N', 'You', 'The cranes, four times, and the ferry coming in.', 'four photos')
        + lane('P', 'Priya', 'Six doors. Painted-over loading bays, mostly.', 'six photos')
        + lane('M', 'Maya', '&ldquo;what is that enormous building with no windows&rdquo;', 'one question') + '</div>', top=16)
    inner += sect('Maya&rsquo;s building') + gut(box(says('The Red Hook Grain Terminal. The state built it in 1922 for grain coming down the Barge Canal: 54 concrete silos, ninety feet high. It ran until 1965 and has stood empty since.', 16, 23)
        + dci('SourceList', 44, items='1=BROOKLYN PUBLIC LIBRARY · “THE RED HOOK GRAIN TERMINAL”;2=RED HOOK WATERSTORIES')))
    return phone2(inner, active='Life')

# ── 2 · Left here, by someone who isn't ──
def left():
    inner = header('Court Street at Sackett', 'Carroll Gardens &middot; you&rsquo;re here', back=True)
    inner += gut(original(210, author='Mom', meta='JUNE · FOR YOU, HERE',
        words='The corner shop was a bakery under another name when we lived on Sackett Street. We bought bread there every Sunday until 1991. Look up. The bracket for the old sign is still on the wall. Love, Mom'), top=18)
    inner += gut(actions(btn('Tell her you found it'), door('Keep', MUTE)), top=14)
    inner += sect('On this corner today') + gut('<div>' + row('The corner shop &middot; <span style="color: #6E6862;">open until 7:00</span>', mark='dot', color=GOLDD, last=True) + '</div>' + prov('LISTING &middot; SAT'))
    return phone2(inner, active='Places')

# ── 3 · Routed to a person ──
def route():
    inner = bar('CHAT', 'SATURDAY 3:10 PM')
    inner += gut(bubble('why are there so many old social clubs around here?'), top=22)
    inner += gut(says('I don&rsquo;t have a source I&rsquo;d trust on these particular clubs.'), top=16)
    inner += gut(box(says('Your mom lived two blocks from here until 1991. I&rsquo;d ask her which club it was, and who went.', 16, 23)
        + prov('HER NOTE ON COURT STREET &middot; JUNE') + f'<div style="margin-top: 8px;">{actions(door("Ask her"))}</div>'), top=14)
    inner += gut(f'<div class="vdl-field" style="border-radius: 12px; min-height: 52px; align-items: flex-start; padding: 12px 14px;"><span class="vk-t-bodyMd" style="color: {GHOST};">To Mom</span></div>', top=14)
    return phone2(inner, active='Chat')

def build():
    cols = [
        col(noticed(), cap('1', 'One walk, three layers', 'Three people&rsquo;s attention, left side by side. Vesper answers the one question that was asked, from real sources, and does not join the three into a story.', tags=(EX, PF, SHARED('THE THREE'), SH('SourceList')))),
        col(left(), cap('2', 'Left here, by someone who is not', 'A parent&rsquo;s 1991 reaches a daughter&rsquo;s Saturday, on the corner it is about.', tags=(EX, PF, PRIV('NORA')))),
        col(route(), cap('3', 'Routed to a person', 'No trustworthy source, so Vesper says so and points to the person who was there. The message to her starts empty.', tags=(EX, PRIV('NORA')))),
    ]
    nc = review([
        ('MINIMUM CONTEXT', 'Frame 1 needs three people who each kept something from one occasion. Frames 2 and 3 need one person who deliberately left or shared something about a place &mdash; a single contribution, possibly months old.'),
        ('EFFORT AT THE TIME', 'Nobody did anything extra on the walk. Nora&rsquo;s mother wrote three sentences once, in June, and chose a corner.'),
        ('EFFORT LATER', 'Reading. Frame 3 costs Nora one message in her own words, if she wants to send one.'),
        ('KNOWN INPUTS', 'Each person&rsquo;s own captures, pooled because each chose to; a note addressed to one person at one place; one fact a mother told her daughter. Clearly labelled third-party history.'),
        ('AUDIENCE EFFECT', 'Frame 1 exists only among the three, and only from what each added. The mother&rsquo;s note is for Nora and nobody else &mdash; not the walk&rsquo;s other two, not the place&rsquo;s public page.'),
        ('LOW PARTICIPATION', 'If Priya had kept her doors to herself, frame 1 has two lanes and says nothing about her. If Nora never goes to Court Street, the note is simply in Life.'),
        ('ONE FAILURE', 'The connecting story in frame 1 is wrong, or merely plausible. It is sourced and separable: remove the box and three honest lanes remain.'),
    ], [
        ('BASIC INTERACTION', 'A shared album shows the three sets of photographs. A text from a parent carries the bakery story. Both are good and both are already in use.'),
        ('WHAT IMPROVES, FOR WHOM', 'Understanding and enjoyment: each of the three sees what the others noticed, and Maya gets a real answer to her question. Nora: her mother&rsquo;s 1991 on the corner it is about. The mother: three sentences, once. Against a shared album or a text: the note waits where it is about, and the answer about the building comes from named sources.'),
        ('DIFFERENTIATING?', 'Yes &mdash; this is the corpus&rsquo;s own claim for what multiplayer is: &ldquo;from preference coordination to shared perception.&rdquo; Frame 3 is the rarest move in the project: an AI that gets out of the way of a person.'),
        ('SYSTEM ADVANTAGE', 'Needs person, place, time and permission held together. It is the opposite of a feed: the contribution waits in the world for one person rather than being broadcast to many.'),
        ('REJECTION TEST', 'Reject one synthesised group interpretation of the walk. Reject an AI-written message to the mother. Reject delivering a note on arrival without the <i>recipient&rsquo;s</i> consent &mdash; a sender&rsquo;s wish never creates a right to interrupt.'),
    ], 'retain',
        'The most differentiated territory in the repo and the one most specific to this product. Frame 2 is the image to remember from the whole exploration.',
        'do people experience a place-timed note from someone they love as caring, or as being watched? The 08-21 strategy names this as a falsifier, and it should be tested before anything else here.',
        offscreen=['nobody&rsquo;s reading of the walk is the right one, and nothing says what it meant to anyone', 'the note appears because Nora is here and had separately agreed to be met here', 'her mother is not notified that it was opened; telling her is a message Nora writes', 'Vesper finds the person and leaves the message empty'],
        extras=('<b>Source:</b> attention-traces doc §8 (distributed attention, borrowed lenses, routing curiosity), 08-21 strategy §1.3 (asynchronous shared perception, &ldquo;a parent who knew a neighborhood decades ago&rdquo;).',
                '<b>Gated, not assumed:</b> arrival-timed delivery is described in the source as a later consent and attention experiment. Frame 2 draws it with the recipient&rsquo;s prior yes made explicit.',
                '<b>Named omission:</b> divergence that stays unresolved &mdash; two people who disagree about a place, with the disagreement preserved &mdash; is not drawn.'),
        )
    return eboard('E3', 'E3 - Seeing more through each other', 'EXPANDING MY WORLD', 'Seeing more through each other',
        'Several people can inhabit the same place, notice different layers, and help one another experience more &mdash; including people who are not there. '
        'The payoff is a richer world, not a better recommendation. People, photographs, history and the 1991 bakery are fixtures.',
        cols, nc, 3)

if __name__ == '__main__':
    print(build())
