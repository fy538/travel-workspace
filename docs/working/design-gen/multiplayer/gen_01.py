"""01 · Decisions. Every open decision this exploration produced, in one place, each with its options, a recommendation,
the boards it touches, and a line for the ruling. Edit the RULED line in place when one is made."""
from mp_kit2 import *
OPEN = tag('OPEN', OX, 'rgba(122,46,46,0.10)')
REC = tag('RECOMMENDED', GREEN, 'rgba(61,112,80,0.12)')
def L(path, text): return f'<a href="{path}" style="color: {GOLDD}; text-decoration: none; border-bottom: 1px solid rgba(138,102,40,0.35);">{text}</a>'
D = lambda n, t: L(f'directions/{n}.dc.html'.replace(' ', '%20'), t)
def card(id_, q, why, options, rec, affects, owner):
    opts = ''.join(f'<div style="display: grid; grid-template-columns: 22px 1fr; column-gap: 8px; padding: 7px 0; border-top: 1px solid rgba(27,23,20,0.06);">'
                   f'<span style="{MONO} font-size: 10px; font-weight: 700; color: {GOLDD if i == rec else MUTE}; padding-top: 3px;">{chr(65+i)}</span>'
                   f'<div style="font-size: 13px; line-height: 19px; color: {INK if i == rec else INK2};">{o}{(" &nbsp;" + REC) if i == rec else ""}</div></div>' for i, o in enumerate(options))
    return (f'<div style="background: {CARD}; border: 1px solid {HAIR}; border-radius: 14px; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px; break-inside: avoid;">'
            f'<div style="display: flex; gap: 8px; align-items: center;"><span style="{MONO} font-size: 11px; font-weight: 700; color: {MUTE};">{id_}</span>{OPEN}</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 26px;">{q}</div>'
            f'<div style="font-size: 13px; line-height: 19px; color: {INK2};">{why}</div>'
            f'<div>{opts}</div>'
            f'<div class="led" style="grid-template-columns: 78px minmax(0,1fr); margin-top: 2px;"><div class="k">TOUCHES</div><div>{affects}</div><div class="k">OWNER</div><div>{owner}</div></div>'
            f'<div style="border-top: 1px dashed rgba(27,23,20,0.28); padding-top: 10px; display: grid; grid-template-columns: 78px 1fr; column-gap: 14px; align-items: baseline;">'
            f'<span class="k" style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {OX};">RULED</span><span style="font-size: 14px; color: {GHOST};">&mdash; not yet &mdash;</span></div></div>')
def grid(cards): return '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 22px; align-items: start;">' + ''.join(cards) + '</div>'
def li(items):
    return '<div style="display: flex; flex-direction: column; gap: 7px;">' + ''.join(
        f'<div style="display: flex; gap: 10px; align-items: baseline;"><span style="color: {GHOST}; flex: none;">&mdash;</span><span style="font-size: 13px; line-height: 19px; color: {INK2};">{t}</span></div>' for t in items) + '</div>'

SHAPE = [
    card('S1', 'What is the six-part map, exactly?',
         'Send, the reader, the arrangement, a private constraint, mutual yes, Together. The review accepted it as a way to reuse presentation, and rejected it as six interchangeable primitives: an offer, a request, an invitation, an acceptance and an expiry do not become the same thing by sharing a sheet.',
         ['A <b>provisional reuse map</b> for design. Shared presentation; every meaning and consequence kept distinct.', 'A product grammar that new social work must fit.', 'Set it aside and keep working direction by direction.'], 0,
         L('02%20-%20Six%20interactions.dc.html', '02 A proposed reuse map'), 'Founder &middot; Multiplayer Product Strategy'),
    card('S2', 'Is there a build order yet?',
         'An earlier version proposed a private word, then Send, then Together. The review holds it: a reportedly shipped guard is not a finished experience, and E2 is a specialization, not the selected entrance.',
         ['<b>Hold.</b> Judge by complete receiving value, participation burden and dependencies before ordering anything.', 'A private constraint &rarr; Send, extended &rarr; Together.', 'Send first, because it is visible on day one with one friend.'], 0,
         L('05%20-%20One%20gathering%20different%20participation.dc.html', '05') + ' ' + L('06%20-%20Something%20that%20continues.dc.html', '06') + ' ' + D('E7 - Someones city handed to you', 'E7'), 'Founder'),
    card('S3', 'What comes out?',
         'The first answer removed too much. A send sheet is not a whole lifecycle, and a three-person shared context had not been drawn before it was cut.',
         ['Remove only <b>unnecessary destinations</b>: a social tab, a group workspace needing upkeep, a standalone play product, a relationship dashboard. Keep a person-first entrance, a continuing shared context, and the distinct meaning of an offer, a request and an opening.', 'Also remove the circle context, &ldquo;me and you&rdquo;, and offers and requests as distinct things.', 'Hold; nothing is ruled out yet.'], 0,
         D('D2 - A living shared world', 'D2') + ' ' + D('D4 - Small acts of help', 'D4') + ' ' + D('D6 - Me and you', 'D6') + ' ' + D('D7 - Happy for company', 'D7') + ' ' + L('06%20-%20Something%20that%20continues.dc.html', '06'), 'Founder'),
    card('S4', 'Defer the place commons and the nod?',
         'Strangers reaching each other through a place is real and large; the canon sequences it at step 6 of 9. The nod between regulars needs an audience the canon does not have.',
         ['Defer both. Keep the regular&rsquo;s private place memory, which is personal, not multiplayer.', 'Defer the commons; study the nod now, because it is the only social value that needs no friends.', 'Bring the commons forward.'], 0,
         D('E4 - The people of a place', 'E4') + ' ' + D('E6 - The regular', 'E6'), 'Founder &middot; canon &sect;11'),
]
RULE = [
    card('R1', 'May a giver learn that what they gave did some good?',
         'The prominence brief wants contributors to see what their contribution changed; the social brief bans viewed, saved and used reports. The review notes these are already different things: a person choosing to say thanks (E7 frame 5, board 06 frame 5) is not telemetry. That distinction does not by itself authorize any new contributor analytics.',
         ['Never, anywhere.', 'Between friends, only when the recipient chooses to say so in their own message. For a public note at a place, one nameless, count-free line: &ldquo;part of an answer someone asked for here.&rdquo;', 'Yes, with counts, for public notes.'], 1,
         D('E4 - The people of a place', 'E4 frame 2') + ' ' + D('D10 - The next time is better', 'D10') + ' ' + D('E7 - Someones city handed to you', 'E7'), 'Contribution and Consequence contract'),
    card('R2', 'Which secrets will the product keep?',
         'E8 works because Priya is simply not in the surprise&rsquo;s audience, and because Vesper never says anything untrue to her. That is enough for a birthday and not enough as a general rule.',
         ['None. No arrangement may exclude someone it concerns.', 'Only a <b>Surprise</b>: it has a stated moment when it opens to the person, it is set by someone taking part, and it is for them. Never about money they owe, their safety, their health, their location, or their standing in a group. Vesper never states an untruth, and answers their direct questions about their own commitments truthfully.', 'Any exclusion a group agrees to.'], 1,
         D('E8 - Keeping a secret together', 'E8'), 'Founder &middot; trust and privacy'),
    card('R3', 'Is &ldquo;people who also chose this, at this place&rdquo; an audience?',
         'The canon has four visibility spaces: private, relational, Occasion, friends/public. The nod needs a fifth: mutual and scoped to one place.',
         ['Not now. It waits with E6.', 'Treat it as friends/public expression narrowed to a place, and allow it.', 'Add a fifth space to the canon.'], 0,
         D('E6 - The regular', 'E6 frame 2'), 'Multiplayer Product Strategy &sect;1.1'),
    card('R4', 'May something arrive when you reach a place?',
         'A mother&rsquo;s note on the corner it is about is the image of this exploration. The source doc calls arrival-timed delivery a later consent experiment, and names &ldquo;creepy more often than caring&rdquo; as a falsifier.',
         ['No. It waits in Life until opened.', 'Yes, as an experiment: only with the recipient&rsquo;s prior yes to that sender, only while the app is already open, never as a push.', 'Yes, including a push on arrival.'], 1,
         D('E3 - Seeing more through each other', 'E3 frame 2') + ' ' + D('E7 - Someones city handed to you', 'E7 frame 2'), 'Attention policy &middot; consent'),
    card('R5', 'How is something said out loud kept at all?',
         'The boards no longer keep anything that was only spoken: every retained line is now a message someone sent or a note someone typed. The question remains for the product: private remembrance, an attributed shared claim, and a recording are three different things, and no universal mutual-consent rule is adopted here.',
         ['Only what someone typed, sent or photographed is ever kept.', 'A person can keep their own words. Keeping something someone else said needs their yes as well &mdash; the same mutual yes as everything else.', 'Either person may keep it for themselves, attributed.'], 1,
         L('06%20-%20Something%20that%20continues.dc.html', '06') + ' ' + D('E5 - Ours over years', 'E5') + ' ' + D('D10 - The next time is better', 'D10'), 'Contribution and Consequence contract'),
    card('R6', 'Adopt the social copy rules beside the Voice Canon?',
         'Four voices kept apart; Vesper does not summarize people; boundaries said with the everyday noun; provenance as source and day; absence is absent. Judged by your ear over three rounds, and by nobody else.',
         ['Adopt as working guidance, and ask the shared-package owner for a casual-message variant of the reader.', 'Adopt the rules; leave the reader as it is.', 'Hold until real users have read it.'], 0,
         L('archive/C1%20-%20Copy%20before%20and%20after.dc.html', 'C1 Copy, before and after') + ' &middot; every phone', 'Voice Canon'),
]
PEOPLE = [
    'Does a note from someone you love, arriving on the corner it is about, feel caring or watched? <span style="color: #6E6862;">(E3 &middot; decides R4)</span>',
    'Does saying nothing about an opening nobody took feel kind, or evasive? <span style="color: #6E6862;">(D7 frame 3)</span>',
    'Will three friends each write one line about themselves for a stranger? <span style="color: #6E6862;">(E1)</span>',
    'Will anyone spend ten minutes handing over a city &mdash; or does it have to take two? <span style="color: #6E6862;">(E7)</span>',
    'Does a nod that software arranged still feel like a nod? <span style="color: #6E6862;">(E6 &middot; decides S4)</span>',
    'Is &ldquo;Swap numbers&rdquo; too light for a step that needs her consent? <span style="color: #6E6862;">(E1 frame 4)</span>',
    'Would anyone play a second time without a reminder? <span style="color: #6E6862;">(D9)</span>',
]
ELSEWHERE = [
    'Guest identity and delivery &mdash; the Social project&rsquo;s open dependency; E1&rsquo;s guest page is conditional on it.',
    'Friends scope, and independent recipient copies &mdash; Social.',
    'Circle membership and who sees history &mdash; policy; D2.',
    'Retention windows and grant expiry &mdash; Contribution and Consequence; D10, E5.',
]

def build():
    inner = blk('HOW TO USE THIS BOARD', N(
        'Ten decisions came out of this exploration. Each card has the question, why it matters, the options, a recommendation, the boards it touches, and who owns the answer. <b>The recommendations on S1&ndash;S3 were changed on September 21 to follow an independent review; no RULED line was filled by that update.</b> '
        'Nothing is ruled. When you decide one, edit its <b>RULED</b> line in place &mdash; it is ordinary text &mdash; and the board becomes the record. '
        'A recommendation is an argument, not a default: leaving a card open changes nothing.'))
    inner += blk('THE SHAPE &middot; FOUR DECISIONS ABOUT WHAT THIS IS', grid(SHAPE))
    inner += blk('SIX RULINGS &middot; THINGS A DRAWING CANNOT SETTLE', grid(RULE))
    inner += f'<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="flex: 1.2;">' + blk('NOT DECISIONS &middot; SEVEN THINGS ONLY PEOPLE CAN ANSWER', li(PEOPLE)) + '</div><div style="flex: 1;">' + blk('OPEN, AND OWNED ELSEWHERE', li(ELSEWHERE)) + '</div></div>'
    return write('01 - Decisions', sheetboard(1860, hh('01', 3200),
        '01 &middot; DECISIONS &middot; ALL OPEN', 'Ten decisions',
        'What this exploration needs from the founder, in one place. Four about the shape, six rulings, and the questions that need people rather than a decision.',
        inner, vdl=False))

if __name__ == '__main__':
    print(build())
