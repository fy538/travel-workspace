"""R1 · Recommendation (Pass C handback). The smallest coherent shape, what each direction becomes, what to remove,
and what only a ruling or a person can settle."""
from mp_kit2 import *
V = lambda k, t: f'{tag(k.upper(), *VERDICT[k])} <span style="color: {INK2};">{t}</span>'
NS = lambda t: f'{tag("NO SURFACE", OX, "rgba(122,46,46,0.10)")} <span style="color: {INK2};">{t}</span>'
def li(items):
    return '<div style="display: flex; flex-direction: column; gap: 7px;">' + ''.join(
        f'<div style="display: flex; gap: 10px; align-items: baseline;"><span style="color: {GHOST}; flex: none;">&mdash;</span><span style="font-size: 13px; line-height: 19px; color: {INK2};">{t}</span></div>' for t in items) + '</div>'
def two(a, b, fa=1, fb=1):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="flex: {fa};">{a}</div><div style="flex: {fb};">{b}</div></div>'

SHAPE = [
    ['<b>Send</b>', 'Words, a photo or a place &middot; to whom &middot; until &middot; where it waits &middot; one thing they can answer', 'Extension of the share sheet. An offer, a request and an opening keep their own consequences'],
    ['<b>The reader</b>', 'A person&rsquo;s own words, attributed once; reply, or ask Vesper privately', 'Existing, reused'],
    ['<b>The arrangement</b>', 'What, when, who is in, settled and loose, who decides; a person outside it; the world changing it', 'Existing, reused'],
    ['<b>A private constraint</b>', 'Said to Vesper about a shared thing; narrows what it suggests; never quoted. Not the same as words a person sends, or an accommodation that must be said plainly', 'Proposed'],
    ['<b>Mutual yes</b>', 'Each person asked alone. A silent &ldquo;no&rdquo; only before anything is agreed', 'Proposed'],
    ['<b>Together</b>', 'What is between these people, in Life; arriving on Home or in Places when it can change something', 'Proposed view'],
]
BECOMES = [
    ['D1', 'A little window', 'Send + the reader', V('retain', 'the baseline; held to ease, not novelty')],
    ['D2', 'A living shared world', 'Together; the unprompted arrival stays', V('merge', 'the circle destination goes')],
    ['D3', 'Borrowing perspective', 'The reader; Chat that cites people', V('retain', '')],
    ['D4', 'Small acts of help', 'Send, with one answer and an &ldquo;until&rdquo;', V('merge', 'not an object')],
    ['D5', 'A possibility becomes a plan', 'Send, then the arrangement', V('retain', '')],
    ['D6', 'Me and you', 'A question in Chat', NS('it is an opening sentence')],
    ['D7', 'Happy for company', 'Send, with &ldquo;until&rdquo; and &ldquo;I&rsquo;ll come&rdquo;', V('merge', 'no status or availability object')],
    ['D8', 'Help in the moment', 'Chat; the arrangement&rsquo;s changed-world state', V('retain', 'the changed-world state is the best single argument for the product')],
    ['D9', 'Something playful', 'Content inside Together; a send that waits at a place', NS('needs people, not drawings')],
    ['D10', 'The next time is better', 'Together, arriving', V('retain', 'the long bet')],
    ['E1', 'Getting into the room', 'The arrangement as an invitation + a private word + mutual yes', V('retain', 'sits on the invitation, where growth comes from')],
    ['E2', 'The group decides', 'The arrangement + a private word', V('retain', 'a strong specialization, not an exclusive wedge')],
    ['E3', 'Seeing more through each other', 'Send that waits at a place; Chat routing to a person', V('retain', 'test &ldquo;caring or watched&rdquo; first')],
    ['E4', 'The people of a place', 'The same send, to anyone who asks here', V('defer', 'canon step 6 of 9')],
    ['E5', 'Ours, over years', 'Together + mutual yes', V('retain', '')],
    ['E6', 'The regular', 'Private place memory; the nod is a mutual yes scoped to a place', V('defer', 'needs an audience the canon does not have')],
    ['E7', 'Someone&rsquo;s city, handed to you', 'Send, as a bundle that waits at its places', V('retain', '')],
    ['E8', 'Keeping a secret together', 'The arrangement&rsquo;s &ldquo;Surprise&rdquo; state + a private word', V('retain', 'needs a ruling on which secrets')],
]
REMOVE = [
    'A social tab or fifth root.',
    'A group workspace that someone has to keep up.',
    'A standalone play product, games, streaks, prompts to capture.',
    'A relationship dashboard, or any reading of what kind of pair or group people are.',
    'Screen text whose only job is to say what the product does not do. Pending, unanswered, failed and expired states stay visible wherever someone is relying on them.',
    '<b>Not removed:</b> a person-first way in (D6), a continuing three-person shared context (D2, now board 06), and the distinct meaning of an offer, a request and an opening (D4, D7).',
]
FIRST = [
    ['<b>1 &middot; A private word</b>', 'It is what no group chat can do, it appears on the three strongest boards (E1, E2, E8), and the guard beneath it is already shipped. Design it once: one question, one rule for what comes out.'],
    ['<b>2 &middot; Send, extended</b>', '&ldquo;Until,&rdquo; &ldquo;waits at,&rdquo; and one answer turn a share sheet into D1, D4, D7, E3 and E7. The cheapest breadth in the project.'],
    ['<b>3 &middot; Together</b>', 'Where memory becomes something two people can feel. Slowest to prove, and the stated moat. Prototype it on a pair before any group.'],
]
RULINGS = [
    'May a contributor learn that what they wrote helped someone? The prominence brief says yes; the social brief bans used/viewed reports. (E4 frame 2, D10)',
    'Which secrets will the product keep? Duration, who may set one about whom, and what it may never cover. (E8)',
    'Is &ldquo;people who also chose this, at this place&rdquo; an audience? It is not one of the canon&rsquo;s four. (E6)',
    'May something be delivered when a person arrives somewhere, on their prior yes? The source calls this a consent experiment. (E3, E7)',
    'How is a line said out loud kept at all, and by whose act? (W1 frame 8, D10, E5)',
    'Guest identity and delivery, Friends scope, circle membership and historical access: unchanged, still open, owned elsewhere.',
]
HUMAN = [
    'Does a note from someone you love, arriving on the corner it is about, feel caring or watched?',
    'Does saying nothing about an opening nobody took feel kind, or evasive?',
    'Will three friends each write one line about themselves for a stranger?',
    'Will anyone spend ten minutes handing over a city &mdash; or does it have to take two?',
    'Does a nod that software arranged still feel like a nod?',
    'Is &ldquo;Swap numbers&rdquo; too light for a step that needs her consent?',
    'Would anyone play a second time without a reminder?',
]
DOCS = [
    '<b>Multiplayer Product Strategy</b>: note that Caucus generalizes to &ldquo;a private word&rdquo; (E1, E8 are not group decisions) and Convergence to &ldquo;mutual yes, silent no.&rdquo; No change of doctrine.',
    '<b>The 2026-09-20 brief</b>: its reading-order line lists six modes; the canon has eight (Mandate and Repair are missing).',
    '<b>Voice Canon</b>: adopt or reject the social-copy companion; a casual-message variant of the reader is the one open design question.',
    '<b>Shared package extension queue</b>: Send&rsquo;s three fields; InviteCard&rsquo;s faces, settled/loose, decider, Surprise and changed-world states; the reader&rsquo;s place glyph.',
    '<b>Founder-thread docs</b>: six are past or at their expiry date, including the gathering-psychology doc these boards lean on most.',
    '<b>Shared fixture ledger</b>: untouched. Every new name on these boards is a proposed fixture and none was added.',
]
OMIT = [
    'Looking after someone &middot; family and household &middot; generosity &middot; the socially sparse and the socially overloaded',
    'The far end of a relationship: estrangement, reconciliation, death directives (specified in the Life contract)',
    'A large gathering &middot; a genuine deadlock &middot; repair of a shared plan that falls through &middot; three friends in three cities',
    'Captions and review notes outside the phones still carry the old cadence',
]

def build():
    inner = blk('THE RECOMMENDATION', N(
        f'<span style="{SERIF} font-size: 20px; line-height: 28px; color: {INK};">Build six interactions, not eighteen features. Three exist, one is an extension, three are new &mdash; and no new root, tab or feed is needed for any of them.</span><br><br>'
        'The eighteen directions are things people want. Compared honestly (board B1), they reduce to one way to send, one way to read, one object for anything agreed, and three mechanisms no ordinary app has: a private word that shapes a shared thing, a mutual yes whose &ldquo;no&rdquo; is silent, and a view of what is between particular people. '
        'Composed into an ordinary weekend (W1) and a friendship across an ocean (W2), four of the six carried everything; the other two appear the moment there is a group, a guest or a secret.'))
    inner += blk('THE SHAPE', tbl(['', 'WHAT IT IS', 'STATUS'], SHAPE))
    inner += blk('WHAT EACH DIRECTION BECOMES', tbl(['', 'DIRECTION', 'BECOMES', 'DISPOSITION'], BECOMES))
    inner += two(blk('REMOVE', li(REMOVE)), blk('IF ONLY THREE THINGS, IN THIS ORDER', tbl(['', 'WHY'], FIRST)), 1, 1.1)
    inner += two(blk('NEEDS A RULING, NOT A DRAWING', li(RULINGS)), blk('NEEDS PEOPLE, NOT A DRAWING', li(HUMAN)))
    inner += two(blk('SUGGESTED UPDATES TO OWNER DOCUMENTS', li(DOCS)), blk('NAMED AND NOT DRAWN', li(OMIT)))
    inner += blk('WHAT THIS DOES NOT CLAIM', N(
        'Nothing is selected, adopted or scheduled. The Social delivery queue is untouched. Every disposition is this exploration&rsquo;s reading, offered for the founder&rsquo;s decision. '
        'A static board proves no behavior, no demand, and nothing about whether any of this is enjoyable. The three &ldquo;first&rdquo; items are an order of argument, not an engineering plan.'))
    return write('R1 - Recommendation', sheetboard(1860, hh('R1', 3000),
        'R1 &middot; PASS C &middot; HANDBACK', 'Six interactions, not eighteen features',
        'The smallest coherent shape that delivers the breadth, what each direction becomes, what to remove, and what only a ruling or a person can settle. Supported by B1, W1 and W2.',
        inner, vdl=False))

if __name__ == '__main__':
    print(build())
