"""B1 · Compare and simplify (Pass B). Eighteen directions reduced to the few interactions they actually share, with the
same component drawn across directions as evidence, the comparisons the brief asked for, and a reuse map."""
from mp_kit2 import *

def rcp(letter, name):
    return f'<span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">{letter}</span><span class="vk-t-bodySmMedium">{name}</span></span>'
def mini(label, inner, w=340):
    return (f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 8px;">'
            f'<div style="display: flex; gap: 6px;">{tag(label, MUTE, "rgba(110,104,98,0.12)")}</div>'
            f'<div style="background: {PAPER}; border-radius: 14px; padding: 16px; display: flex; flex-direction: column; gap: 12px; min-height: 250px; box-sizing: border-box;">{inner}</div></div>')
def field(t): return f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 6px 0 10px 0;">{plain(t, size=16, lh=22)}</div>'
def kv(k, v): return f'<div style="display: grid; grid-template-columns: 78px 1fr; column-gap: 10px; align-items: center;"><span class="kickm">{k}</span><div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">{v}</div></div>'
def strip(items): return '<div style="display: flex; gap: 24px; align-items: stretch; flex-wrap: wrap;">' + ''.join(items) + '</div>'
def arrow(): return f'<div style="{MONO} font-size: 11px; color: {ANCHOR}; text-align: center;">&darr; what the others see</div>'

SEND = [
    mini('D1 &middot; A MOMENT', field('it sank 😭 still ate half of it') + kv('TO', chip('FRIENDS') ) + kv('UNTIL', quiet('Sunday')) + f'<div style="margin-top: auto;">{actions(btn("Send"))}</div>'),
    mini('D4 &middot; AN OFFER', field('made way too much sauce. anyone want some?') + kv('TO', rcp('M','Maya') + rcp('P','Priya')) + kv('UNTIL', quiet('Tuesday')) + kv('THEY CAN', quiet('&ldquo;Yes please&rdquo;')) + f'<div style="margin-top: auto;">{actions(btn("Send"))}</div>'),
    mini('D7 &middot; COMPANY', field('getting coffee and wandering red hook this afternoon. happy for company') + kv('TO', rcp('M','Maya') + rcp('P','Priya')) + kv('UNTIL', quiet('5:00')) + kv('THEY CAN', quiet('&ldquo;I&rsquo;ll come&rdquo;')) + f'<div style="margin-top: auto;">{actions(btn("Send"))}</div>'),
    mini('E3 &middot; LEFT AT A PLACE', field('The corner shop was a bakery when we lived on Sackett Street. Look up. Love, Mom') + kv('TO', rcp('N','Nora')) + kv('WAITS AT', quiet('Court St at Sackett')) + f'<div style="margin-top: auto;">{actions(btn("Leave it here"))}</div>'),
    mini('E7 &middot; A CITY', field('my mexico city, for you. four places, in order') + kv('TO', rcp('N','Nora')) + kv('WAITS AT', quiet('Each of the four places')) + kv('UNTIL', quiet('She&rsquo;s done with it')) + f'<div style="margin-top: auto;">{actions(btn("Send to Nora"))}</div>'),
]
def arr(title, facts, who, extra):
    return (f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 25px;">{title}</div>{quiet(facts)}{who}{extra}')
ARRANGE = [
    mini('D5 &middot; TWO PEOPLE', arr('The market, the canal, coffee', 'Sunday 10:00 · Carroll Gardens', faces('NM', 'You and Maya'),
         kv('SETTLED', quiet('Market gate, 10:00 · Maya leaves by 4:00')) + kv('LOOSE', quiet('Which stalls · whether coffee happens'))), 400),
    mini('E2 &middot; FOUR, WITH A DECIDER', arr('The blue house on Wiltwyck', 'Kingston · two nights · sleeps four in beds', faces('MD', 'Maya and Dana are in'),
         kv('DECIDES', quiet('Nora, Thursday evening')) + kv('MAYA HAS', quiet('Dinners, up to $60 a head, through Sunday')) + actions(btn('I’m in'), btn('Not this one', False))), 400),
    mini('E8 &middot; ONE PERSON OUTSIDE IT', f'<div class="kickm" style="color: {GOLDD};">SURPRISE</div>' + arr('Priya&rsquo;s birthday', 'Saturday the 14th, 7:00, your place', faces('NMD', 'are in on it'),
         quiet('Opens to Priya when she walks in.')), 400),
    mini('D8 &middot; THE WORLD CHANGED', arr('Sunday with Maya', 'Was: the Print Room, 4:00', faces('NM', 'You and Maya'),
         dci('Notice', 70, tone='unavailable', title='Closed early today', body='Gallery notice, 2:40 PM.') + actions(btn('Send Maya the pier instead'))), 400),
]
def word(label, k1, private, k2, shared, src):
    return mini(label, f'<div class="kickm">{k1}</div>{plain(private, size=16, lh=22)}{arrow()}<div class="kickm">{k2}</div>{says(shared, 16, 23)}{prov(src)}', 400)
WORD = [
    word('E2 &middot; A PRIVATE CONSTRAINT', 'SAID TO VESPER', 'i can&rsquo;t go over 150 a night. please don&rsquo;t make it a thing', 'WHAT VESPER THEN SUGGESTS', 'Only houses under $150 a night. Two of the three.', 'NEVER QUOTED &middot; IN A GROUP OF FOUR, NOT GUARANTEED UNGUESSABLE'),
    word('E1 &middot; WORDS HE CHOSE TO SEND', 'ASKED PRIVATELY, THEN SENT', 'Could I arrive with someone? I don&rsquo;t know the building.', 'WHAT NORA RECEIVES', 'The same words, from Sam, with his name on them.', 'SIGNED &middot; HIS CHOICE TO SEND'),
    word('E8 &middot; A NECESSARY ACCOMMODATION', 'ALREADY SHARED WITH FRIENDS', 'Priya: allergic to walnuts', 'WHAT THE COOK SEES', 'Priya&rsquo;s allergic to walnuts.', 'STATED PLAINLY &middot; A SAFETY FACT IS NOT A PREFERENCE'),
]
def yes(label, ask, both, n):
    return mini(label, says(ask, 17, 24) + actions(btn('Yes'), btn('Not now', False)) + quiet(both) + prov(n), 400)
YES = [
    yes('E1 &middot; SWAPPING NUMBERS', 'Swap numbers with Maya?', 'She gets asked too. Two yeses, and you each have the other&rsquo;s.', 'DISCLOSES A NUMBER &middot; BEFORE ANYTHING EXISTS BETWEEN THEM'),
    yes('E5 &middot; RENEWING A RITUAL', 'Soup at Priya&rsquo;s again?', 'Maya and Priya each get asked the same way.', 'CREATES A POSSIBLE PLAN &middot; NOTHING IS AGREED YET'),
    yes('E6 &middot; JOINING A PLACE&rsquo;S REGULARS', 'Say hi at Tilde?', 'Regulars who&rsquo;ve done the same can see your first name here.', 'JOINS AN AUDIENCE THE CANON DOES NOT HAVE &middot; DEFERRED'),
]
V = lambda k, t: f'{tag(k.upper(), *VERDICT[k])} <span style="color: {INK2};">{t}</span>'
COMPARE = [
    ['<b>D5 &middot; D6 &middot; D7</b><br>an activity &middot; a person &middot; &ldquo;I&rsquo;m going anyway&rdquo;', 'Only the first sentence. D5 opens from a possibility on Home or Places; D6 from a question in Chat; D7 from the composer.', 'Everything after someone answers: one answerable send, then one arrangement.', V('merge', 'Shared presentation, three ways in. D6 keeps a <b>discoverable person-first entrance</b> (from Life &middot; People) and needs no destination of its own. D7 stays an opening with a place and a window; an accepted meeting is a different state from an unanswered opening.')],
    ['<b>D1 &middot; D2 &middot; D10</b><br>a moment &middot; shared context &middot; the next time', 'Time. A moment is complete now. Shared context is the same material asked for later. &ldquo;Next time&rdquo; is the same material arriving unasked when it can change something.', 'The reader, and the fact that every piece stays its author&rsquo;s.', V('rework', 'One store, three timings. <b>D2 is now drawn with three contributors</b> (board 06). A continuing shared context is useful; whether it needs a destination of its own stays open, and is not removed here.')],
    ['<b>D3 &middot; D4</b><br>adapt what a friend said &middot; ask a friend', 'Whether the value is the knowledge or the person. If a friend already shared it, Vesper adapts it and cites them. If the point is their involvement, a person asks them.', 'Attribution, and the rule that Vesper never volunteers that a particular friend would know &mdash; unless their own share said so.', V('retain', 'D3 stays. D4 can reuse the send sheet, but an offer and a request keep their own consequences: what was accepted, what was answered, and what is still <b>unanswered</b>.')],
    ['<b>D8 &middot; D9</b><br>help in the moment &middot; play', 'Whether Vesper should be noticed at all. In D8 the best outcome is nine seconds and gone. In D9 the material is the point.', 'Both live off things already made; neither asks anyone to capture anything.', V('retain', 'D8 stays. D9 needs no standalone play product; enjoyment remains a complete outcome wherever it happens.')],
    ['<b>E1 &middot; E2 &middot; E8</b><br>a guest &middot; a group &middot; a surprise', 'Who is outside. A newcomer is outside the friendships; a budget is outside the group&rsquo;s knowledge; Priya is outside the plan.', '<b>The private word</b>: something said to Vesper that shapes a shared thing and arrives unsigned.', V('rework', 'Not one mechanism: a private constraint, sent words and a plain accommodation. See the strip above.')],
    ['<b>E3 &middot; E7 &middot; E4 &middot; D9 frame 2</b><br>a corner &middot; a city &middot; a public note &middot; a rack', 'Audience and size: one person or anyone who asks here; one line or a bundle of four places.', 'A send that <b>waits at a place</b>, and a recipient who agreed to be met there.', V('retain', 'One extension to Send: &ldquo;waits at.&rdquo; E4&rsquo;s public audience stays deferred; the mechanism is the same.')],
    ['<b>E5 &middot; D10 &middot; D2 &middot; E1 frame 4</b><br>years &middot; next time &middot; a circle &middot; someone new', 'How many people and how long.', '<b>Together</b>: what is between these people, in Life, assembled and never maintained.', V('retain', 'One view for two people or five, a week or ten years. It replaces D2&rsquo;s circle and is where &ldquo;Remember Maya&rdquo; lands.')],
]

PRIMS = [
    ['<b>1 &middot; Send</b>', 'A person&rsquo;s words, photo or place &middot; to whom &middot; until when &middot; optionally where it waits &middot; optionally one thing they can answer', 'D1, D4, D7, D9 frame 2, E3, E4, E7', 'The share sheet from Social 09, extended'],
    ['<b>2 &middot; The reader</b>', 'Name and time once, then the words. Reply to them, or ask Vesper privately. Vesper adds at most one line, about the world.', 'every direction', 'OriginalReader, as shared'],
    ['<b>3 &middot; The arrangement</b>', 'What, when, who is in, what is settled and what is loose, who decides. States: a person is outside it; the world changed.', 'D5, D6, D7, D8, E1, E2, E8', 'InviteCard plus Plans&rsquo; lightweight arrangement'],
    ['<b>4 &middot; A private constraint</b>', 'Said to Vesper about a shared thing. It narrows what Vesper suggests and is never quoted. Distinct from words a person sends and from a plain accommodation.', 'E2; E7 frame 4', '<b>Proposed.</b> A guard is reported shipped; that is not a finished experience'],
    ['<b>5 &middot; Mutual yes, silent no</b>', 'Each person is asked alone. All yes: one line for everyone. Any no: nobody hears anything.', 'E1 frame 4, E5 frame 2, E6 frame 2; canon Convergence', '<b>Proposed</b>; only before anything is agreed'],
    ['<b>6 &middot; Together</b>', 'What is between these people: places, things said, things kept. In Life. It also arrives on Home or at a place when it can change something.', 'D2, D10, E5, E7 frame 3, D9 frame 1', '<b>New view</b>; drawn once in the August 9 profile doc and never since'],
]
REUSE = [
    ['<b>Use as it is</b>', 'OriginalReader &middot; InviteCard &middot; Notice &middot; FactPair &middot; SourceList &middot; the share sheet, field, buttons and recipient token &middot; Home&rsquo;s headline &middot; the reader&rsquo;s place row'],
    ['<b>Small extension</b>', 'Send: &ldquo;until&rdquo;, &ldquo;waits at&rdquo;, and one answer the recipient can give &middot; InviteCard: faces on the option, settled and loose, a decider line, a &ldquo;Surprise&rdquo; state, a changed-world state &middot; the reader: a casual-message variant and a place glyph that is not a fork &middot; a &ldquo;Just you&rdquo; chip'],
    ['<b>Genuinely new</b>', 'A private word that reaches the shared thing unsigned &middot; mutual yes, silent no &middot; the Together view &middot; delivery at a place, with the recipient&rsquo;s prior consent'],
    ['<b>No new destination needed</b>', 'A social tab or fifth root &middot; a group workspace that needs upkeep &middot; a standalone play product &middot; a relationship dashboard. <b>Kept:</b> a person-first entrance, a three-person shared context, and the distinct meaning of an offer, a request and an opening.'],
    ['<b>Deferred, with its reason</b>', 'A public audience through a place (E4): canon step 6 of 9 &middot; the nod (E6 frame 2): needs an audience the canon does not have &middot; arrival-timed delivery without the asker present: a consent experiment first'],
]

def build():
    inner = blk('THE QUESTION PASS B ANSWERS', N(
        'Eighteen directions is a list of things people want. It is not eighteen things to build. This board asks what they can share in <b>presentation</b>. '
        'It is a <b>proposed reuse map, not a product grammar and not an engineering order</b>: two existing patterns reused (the reader, the arrangement), one extended (Send), and three proposed additions. '
        'Sharing a sheet does not make an offer, a request, an invitation, an acceptance, an expiry and a cancellation the same thing; each keeps its own meaning and consequence. Revised September 21 after an independent review.'))
    inner += blk('ONE WAY TO SEND &middot; FIVE DIRECTIONS, ONE SHEET', strip(SEND) + N('What varies is the audience, an end, where it waits, and whether there is one thing to answer. Nothing else. An offer, an open afternoon and a city handed to a friend are the same gesture.'))
    inner += blk('ONE ARRANGEMENT &middot; FOUR DIRECTIONS, ONE OBJECT', strip(ARRANGE) + N('Two people or four, a decider or none, one person kept outside it, a closure arriving from the world: these are states of one object, and the canon already names it (&sect;5.2, lightweight arrangements).'))
    inner += blk('THREE THINGS THAT LOOK ALIKE AND ARE NOT &middot; A CONSTRAINT, SENT WORDS, AN ACCOMMODATION', strip(WORD) + N('An earlier version of this strip called all three &ldquo;a private word&rdquo; that &ldquo;arrives unsigned.&rdquo; The review was right that they are three different things: a constraint on what Vesper suggests, words a person chose to send under their own name, and a practical fact that has to be said plainly. Unsigned is not private in a small group. Private-context coordination is a major capability; it is not the test every social value has to pass.'))
    inner += blk('MUTUAL YES &middot; ONE PATTERN, THREE DIFFERENT CONSEQUENCES', strip(YES) + N('These three look alike and are not equivalent: one discloses a number, one may create a plan, one joins an audience. What they share is timing. A silent &ldquo;no&rdquo; suits a tentative convergence <b>before anything is agreed</b>. It does not suit an existing invitation or commitment, where an unanswered state has to stay visible because someone is relying on it (D4 frame 3, E2 frame 3, E8 frame 3).'))
    inner += blk('THE COMPARISONS', tbl(['COMPARED', 'WHAT REALLY DIFFERS', 'WHAT IS SHARED', 'DISPOSITION'], COMPARE))
    inner += blk('THE SIX INTERACTIONS', tbl(['', 'WHAT IT IS', 'DELIVERS', 'BUILT FROM'], PRIMS))
    inner += blk('REUSE MAP', tbl(['', ''], REUSE))
    return write('02 - Six interactions', sheetboard(1900, hh('02', 3400),
        '02 &middot; COMPARE AND SIMPLIFY', 'Eighteen wants, a proposed reuse map',
        'What the directions share, drawn as evidence; the comparisons the brief asked for and three more; and a reuse map. A proposal, not a selection.',
        inner, vdl=True))

if __name__ == '__main__':
    print(build())
