"""00 · Start here. The recommendation, the map of the project, and what each direction became."""
from mp_kit2 import *
import json, os
from gen_r1 import SHAPE, REMOVE, FIRST, V, NS, li, two
FILES = json.load(open(os.path.join(HERE, 'files.json')))
def L(path, text): return f'<a href="{path.replace(" ", "%20")}" style="color: {GOLDD}; text-decoration: none; border-bottom: 1px solid rgba(138,102,40,0.35);">{text}</a>'
def D(key, text=None): return L(f'directions/{FILES[key]}.dc.html', text or key)

BECOMES = [
    ['D1', 'A little window into my friends&rsquo; lives', 'Send + the reader', V('retain', 'the baseline; held to ease, not novelty')],
    ['D2', 'A living shared world', 'Together; now drawn with three contributors on board 06', V('rework', 'a shared context stays useful; its destination is open')],
    ['D3', 'Borrowing experience and perspective', 'The reader; Chat that cites people', V('retain', '')],
    ['D4', 'Small acts of help', 'Reuses Send; offer and request keep their own consequences', V('merge', 'now shows a truly unanswered request')],
    ['D5', 'A possibility becomes something we do', 'Send, then the arrangement', V('retain', '')],
    ['D6', 'Me and you', 'A question in Chat, with a person-first entrance from Life', V('retain', 'an entrance, not a destination')],
    ['D7', 'Happy for company', 'An opening with a place and a window; then an arrangement if someone says yes', V('retain', 'now drawn from both sides')],
    ['D8', 'Help us enjoy this moment', 'Chat; the arrangement&rsquo;s changed-world state', V('retain', 'the best single argument for the product')],
    ['D9', 'Something playful between us', 'Wherever it happens; enjoyment is a complete outcome', NS('no standalone play product')],
    ['D10', 'The next time is better', 'Together, arriving', V('retain', 'the long bet')],
    ['E1', 'Getting into the room', 'A host-authored invitation; a guest&rsquo;s own signed request; mutual yes afterward', V('retain', 'strong; no guest writes a profile')],
    ['E2', 'The group decides', 'The arrangement + a private constraint; an objection and its repair', V('retain', 'a demanding specialization and acquisition candidate, not the only way in')],
    ['E3', 'Seeing more through each other', 'Send that waits at a place; Chat routing to a person', V('retain', 'test &ldquo;caring or watched&rdquo; first')],
    ['E4', 'The people of a place', 'The same send, to anyone who asks here', V('defer', 'canon step 6 of 9')],
    ['E5', 'Ours, over years', 'Together + mutual yes', V('retain', '')],
    ['E6', 'The regular', 'Private place memory; the nod is a mutual yes scoped to a place', V('defer', 'needs an audience the canon does not have')],
    ['E7', 'Someone&rsquo;s city, handed to you', 'Send, as a bundle that waits at its places', V('retain', '')],
    ['E8', 'Keeping a secret together', 'The arrangement&rsquo;s &ldquo;Surprise&rdquo; state', V('retain', 'a celebration and trust stress case, not the lead proof')],
]
ROWS = [[f'<b>{D(k)}</b>', D(k, t), b, d] for k, t, b, d in BECOMES]
TOP = [
    [f'<b>{L("01 - Decisions.dc.html", "01 &middot; Decisions")}</b>', 'Ten open decisions, with options and a recommendation each. Recommendations were revised after the September 21 review. Nothing is ruled.'],
    [f'<b>{L("02 - Six interactions.dc.html", "02 &middot; A proposed reuse map")}</b>', 'What the eighteen directions can share in presentation. Not a product grammar and not a build order.'],
    [f'<b>{L("03 - An ordinary week between friends.dc.html", "03 &middot; An ordinary week between friends")}</b>', 'Package D. A photo, a tiny reply, a friend&rsquo;s place in Places, half an hour in a park; and the same objects across the four roots.'],
    [f'<b>{L("04 - Far apart.dc.html", "04 &middot; Far apart")}</b>', 'Two friends in two cities. Complete without a meetup. The coast comparison now rests on named sources.'],
    [f'<b>{L("05 - One gathering different participation.dc.html", "05 &middot; One gathering, different participation")}</b>', 'Package B. A host, a contributor, a guest with no app, dinner-only, a decline; an objection, a change after agreement; and a help-with-a-move comparison.'],
    [f'<b>{L("06 - Something that continues.dc.html", "06 &middot; Something that continues")}</b>', 'Package C. Four friends get one dish right over two weeks. What each sent becomes a usable version; one person is removed to see if it matters.'],
    [f'<b>{D("E7", "E7 &middot; Someone&rsquo;s city, handed to you")}</b>', 'Package A, in directions/. Three ticks from saved places; received at once; beside the place in Places; a new question a month on; &ldquo;you were right about upstairs.&rdquo;'],
]
EVID = [
    ['<b>Drawn</b>', 'All 27 boards.'],
    ['<b>Source-reviewed</b>', 'By an independent review on September 21, against the current product authorities: the 25 boards that existed then. Boards 05 and 06 and the revisions made since are not yet reviewed.'],
    ['<b>Render-checked</b>', 'By the design agent: every board loads on the live project with no unresolved components and no overflow. The agent looked at the rendered pixels of some boards, not all. This is the agent&rsquo;s report, not an independent check.'],
    ['<b>Interaction-tested</b>', 'None. These are static drawings.'],
    ['<b>Not evaluated</b>', 'Whether anyone wants any of this, whether it feels welcome, private or kind, and whether any of it is supported by shipped code.'],
]
FOLDERS = [
    ['<b>directions/</b>', 'The eighteen direction boards, D1&ndash;D10 and E1&ndash;E8, linked from the table below. Each is an experience left to right, with its review beneath. They are the evidence; the five boards above are the argument.'],
    ['<b>archive/</b>', L('archive/C1 - Copy before and after.dc.html', 'C1 &middot; Copy, before and after') + ' &mdash; six frames in three rounds, and the copy rules every phone now follows. &nbsp; '
        + L('archive/A0 - Method and coverage.dc.html', 'A0 &middot; Method and coverage') + ' &mdash; how the ten became eighteen, the canon measured against both passes, how value arrives, how much context each benefit needs.'],
    ['<b>Five files that are not boards</b>', 'OriginalReader, InviteCard, Notice, FactPair and SourceList are the shared components the boards load, copied from the design-language workbench at vdl-stage1 0.4.1. The runtime looks for them beside the board, so they sit at the top level and inside each folder. Leave them where they are.'],
]

def build():
    inner = blk('THE RECOMMENDATION', N(
        f'<span style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">Eighteen things people want between them, and a proposed map of what they could share: two existing patterns, one extension, three proposed additions. No new root, tab or feed.</span><br><br>'
        'An independent review on September 21 found the human experiences more convincing than the consolidation, and it was right. The map below is a <b>proposed reuse map</b>, not a product grammar or a build order. '
        'The test for a direction is no longer whether it needs several people&rsquo;s private context. It is <b>what improves for the people involved: enjoyment, understanding, timing, total work, coordination or continuity.</b> A friend&rsquo;s photo can be enough. '
        'Nothing here is selected.'))
    inner += blk('READ THESE', tbl(['BOARD', 'WHAT IT DOES'], TOP))
    inner += blk('EVIDENCE, STATED SEPARATELY', tbl(['', ''], EVID))
    inner += blk('A PROPOSED REUSE MAP', tbl(['', 'WHAT IT IS', 'STATUS'], SHAPE))
    inner += blk('WHAT EACH DIRECTION BECAME', tbl(['', 'DIRECTION', 'BECOMES', 'DISPOSITION'], ROWS))
    inner += two(blk('REMOVE', li(REMOVE)), blk('A BUILD ORDER WAS PROPOSED HERE, AND IS HELD', N('An earlier version ranked a private word, then Send, then Together. The review holds that: a reported guard is not a finished experience, and order should follow complete receiving value, participation burden and dependencies. See decision S2.')), 1, 1.1)
    inner += blk('WHERE EVERYTHING IS', tbl(['', ''], FOLDERS))
    inner += blk('READING A DIRECTION BOARD', N(
        'Frames read left to right and are the experience; the three columns beneath are the review. <b>EXPLORATORY</b> means the composition was proposed here and nowhere else. <b>PROPOSED FIXTURE</b> marks a person, place or event invented for these boards; none was added to the shared fixture ledger. '
        'A blue tag names a shared component the frame uses. Every design decision that is not recited on a screen sits in that board&rsquo;s notes under <b>DECIDED, NOT DISPLAYED</b>.'))
    inner += blk('AUTHORITY, AND WHAT THIS DOES NOT CLAIM', N(
        'Brief: <b>docs/working/claude-design-multiplayer-product-shapes-exploration-2026-09-20.md</b>. Handback: <b>docs/working/multiplayer-shapes-exploration-response-2026-09-21.md</b>. Corpus reading: <b>docs/working/multiplayer-corpus-digest-2026-09-20/</b>. Copy rules: <b>docs/working/vesper-social-copy-companion-2026-09-21.md</b>. '
        'Nothing is selected, adopted or scheduled. The Social Experience project and its delivery queue are untouched. A static board proves no behavior, no demand, and nothing about whether any of this is enjoyable.'))
    return write('00 - Start here', sheetboard(1860, hh('00', 2600),
        'VESPER &middot; MULTIPLAYER SHAPES &middot; REVISED SEPTEMBER 21', 'Eighteen wants, four packages, a proposed reuse map',
        'A bounded exploration of what this product could do between people. Eighteen directions; four revision packages that carry the strongest of them end to end; and a provisional map of shared presentation. Start with the packages.',
        inner, vdl=False))

if __name__ == '__main__':
    print(build())
