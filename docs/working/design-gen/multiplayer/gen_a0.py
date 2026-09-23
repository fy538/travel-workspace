"""00 · Start here. The index for the ten exploratory directions, with what is and is not claimed."""
from mp_common import *

V = lambda k, t: f'{tag(k.upper(), *VERDICT[k])} <span style="color: {INK2};">{t}</span>'

DIRS = [
    ['<b>D1</b>', 'A little window into my friends&rsquo; lives', 'Feeling involved', 'Someone shares an ordinary moment',
     'Enjoy awareness without performance or reply debt', '4 frames + 1 inset', V('retain', 'the baseline of ordinary receiving; held to the ease bar, not a novelty bar')],
    ['<b>D2</b>', 'A living shared world', 'Feeling involved', 'A continuing pair or small circle',
     'Things that matter to us stay available without curation', '3 frames + 1 inset', V('rework', 'the unprompted arrival is the idea; the circle destination is not yet earned')],
    ['<b>D3</b>', 'Borrowing experience and perspective', 'Expanding my world', 'A friend&rsquo;s observation or experience',
     'Better understanding, or a more usable possibility', '3 frames, 2 variants', V('retain', 'clearest differentiating benefit in the portfolio; variant B the least proven')],
    ['<b>D4</b>', 'Small acts of help', 'Expanding my world', 'A bounded offer or need',
     'Give or receive practical care without a big undertaking', '3 frames + 1 inset', V('merge', 'a deliberate share with an answer and an expiry; explore as a variant of D1')],
    ['<b>D5</b>', 'A possibility becomes something we do', 'Being together', 'An appealing activity',
     'Make it happen together with little coordination', '3 frames + 1 inset', V('retain', 'reduces both imagining and arranging; degrades gracefully to a solo Sunday')],
    ['<b>D6</b>', 'Me and you', 'Being together', 'A desire to see a particular person',
     'Find something that works for these people now', '3 frames', V('rework', 'may be a different opening sentence into D5 rather than a different shape')],
    ['<b>D7</b>', 'Happy for company', 'Being together', 'Someone is doing something anyway',
     'Allow participation without organising anything', '3 frames', V('rework', 'the least technological and most humane; the anxiety question is unresolved')],
    ['<b>D8</b>', 'Help us enjoy this moment', 'Being together', 'People are already doing something',
     'Remove friction or enrich the moment, then recede', '3 frames', V('retain', 'frame 2 is the portfolio&rsquo;s best single argument for the whole product')],
    ['<b>D9</b>', 'Something playful between us', 'Being together', 'A playful impulse or shared material',
     'Fun, surprise, or a conversation worth having', '2 frames', V('defer', 'deliberately under-invested; needs human evidence a drawing cannot supply')],
    ['<b>D10</b>', 'The next time is better', 'Carrying forward', 'A present intention meets useful past evidence',
     'Continuity without starting from zero or keeping a journal', '3 frames', V('retain', 'the long bet; slowest to verify, most dependent on the rest of the app')],
]

T = lambda k: {'pass': tag('PASSES', GREEN, 'rgba(61,112,80,0.12)'), 'part': tag('IN PART', GOLDD, 'rgba(176,133,58,0.14)'), 'diff': tag('DIFFERENTLY', PLAN, 'rgba(42,56,75,0.10)')}[k]
EDIRS = [
    ['<b>E1</b>', 'Getting into the room', 'Belonging', 'An invitation to someone who knows only the host', 'Walk in without rehearsing; be looked after without explaining; keep someone worth knowing', T('pass'), V('retain', 'the largest missed territory, and it sits on the invitation &mdash; where growth comes from')],
    ['<b>E2</b>', 'The group decides', 'Being together', 'Four people and one weekend', 'One coherent choice without a poll; a private limit that is never seen; an organiser relieved of the role', T('pass'), V('retain', 'a strong specialization, absent from all ten; reported closest to shipped code')],
    ['<b>E3</b>', 'Seeing more through each other', 'Expanding my world', 'Several people&rsquo;s attention to one place, including people who are not there', 'A richer world, not a better recommendation', T('pass'), V('retain', 'the most differentiated territory; test whether a place-timed note reads as caring or watched')],
    ['<b>E4</b>', 'The people of a place', 'Expanding my world', 'A concrete question asked from inside a place', 'A positioned answer from people with different standing; for them, that it did some good', T('diff'), V('defer', 'real and large; the canon sequences it at step 6 of 9')],
    ['<b>E5</b>', 'Ours, over years', 'Carrying forward', 'A friendship&rsquo;s places, habits and half-made promises', 'They stay findable; a ritual is asked about, not assumed; a quiet friendship is left in peace', T('pass'), V('retain', 'where the product&rsquo;s memory becomes something two people can feel')],
    ['<b>E6</b>', 'The regular', 'Feeling involved', 'A place a person keeps returning to', 'Being known somewhere, without friendship, invitations or matching', T('part'), V('rework', 'unthought territory; the nod needs study before it is drawn again')],
    ['<b>E7</b>', 'Someone&rsquo;s city, handed to you', 'Expanding my world', 'A move, and a friend who once lived there', 'Her judgment meets you on the right evening, and she never learns how your week is going', T('pass'), V('retain', 'Relay at the scale of a life change; nobody in the repo has drawn it')],
    ['<b>E8</b>', 'Keeping a secret together', 'Being together', 'Something good that depends on one person not knowing', 'A surprise the product helps hold, and an assistant that stays silent without lying', T('pass'), V('retain', 'the moat made delightful, and the hardest ethical line in the project')],
]
CANON = [
    ['<b>8 modes</b> &middot; Handoff, Caucus, Mandate, Our Place, Repair, Convergence, Ritual, Relay', 'Handoff, featured sharing, Repair, a sliver of Our Place', 'Caucus and Mandate (E2) &middot; Ritual and true Convergence (E5) &middot; Relay (E7, E4) &middot; Our Place (E5)', 'Repair of a shared plan'],
    ['<b>6 social units</b>', 'Pair, Solo, a thin circle', 'Host and guest (E1) &middot; Ephemeral party (E2) &middot; Recurring circle (E5)', '<b>Family or household</b>'],
    ['<b>9 kinds of contribution</b>', 'Perspective, evidence, some labor', 'Care and boundaries (E1, E8) &middot; Presence (E1) &middot; Intent (E1) &middot; Initiative (E2) &middot; Meaning (E5)', '&mdash;'],
    ['<b>&sect;1.1 Social accessibility</b> &middot; &ldquo;invitation is not incorporation&rdquo;', '&mdash;', 'E1', 'A large gathering, where topology matters more'],
    ['<b>&sect;7 Resolve, do not poll</b>', '&mdash;', 'E2', 'A genuine deadlock'],
    ['<b>&sect;8 Plural memory; the continuity gradient</b>', 'D10, lightly', 'E1 frame 4 &middot; E5 &middot; E8 frame 4', 'Estrangement, reconciliation, death directives'],
    ['<b>&sect;11 sequencing, steps 5&ndash;9</b>', 'Steps 1&ndash;4 only', 'Step 5 (E5) &middot; step 6 (E4) &middot; step 8 (E5 frame 2)', 'Step 7 reactivation; step 9 co-presence, deliberately'],
]
NARROW = [
    ['No friend map, no live presence', 'Any orientation in your people&rsquo;s worlds'],
    ['No profile ritual, no personas', 'Being known &mdash; the self mirror, the pair-level Together view'],
    ['No viewed, saved or used reports', 'The giver ever learning their contribution changed something'],
    ['No stranger matching', 'The newcomer, the host, the met-once acquaintance, the Place commons'],
    ['Pair-first, for adoption', 'The group of three to eight &mdash; one strong specialization, not an exclusive launch wedge (September 6 consumer strategy)'],
]
UNDRAWN = [
    '<b>Looking after someone</b> &mdash; an ageing parent&rsquo;s outing, a friend in a hard stretch. &ldquo;Care and boundaries&rdquo; is a named contribution kind with no design.',
    '<b>Family and household</b> &mdash; asymmetric authority, members with no account, places as inheritance. Named in the canon as a social unit; drawn nowhere.',
    '<b>Generosity</b> &mdash; treating someone, a place as a gift. The foundations doc calls reciprocity a constitutional tension and leaves it there.',
    '<b>The socially sparse, and the socially overloaded</b> &mdash; for whom the value is fewer things, not more. E4 and E6 reach toward the first; nothing addresses the second.',
    '<b>Long-distance friendship with nothing to hand over</b>, hosting a visitor, and <b>the far end of the lifecycle</b> &mdash; estrangement, reconciliation, death directives &mdash; which the Life contract specifies and no board draws.',
]

ARRIVAL = [
    ['<b>Already there</b> &middot; useful value present on opening, with nothing asked',
     'D2 frame 2 (a friend&rsquo;s change, beside your dish) &middot; D9 frame 1 &middot; D10 frame 2 &middot; <b>E3 frame 2</b> (a note left on a corner) &middot; <b>E5 frame 1</b> &middot; <b>E7 frame 2</b>', 'Covered'],
    ['<b>Asked for</b> &middot; a person asks and receives a useful result',
     'D3 variant A &middot; D4 frame 3 &middot; D6 all frames &middot; D8 frame 1 &middot; D2 frame 1 &middot; <b>E2 frame 1</b> (asked <i>by</i> Vesper, privately) &middot; <b>E4 frame 1</b> &middot; <b>E8 frame 2</b>', 'Covered'],
    ['<b>Changed situation</b> &middot; new information makes a shared situation materially different',
     'D8 frame 2 (a closure reaches an agreed four o&rsquo;clock) &middot; D5&rsquo;s constraint, weakly &middot; <b>E5 frame 2</b> (the first cold Sunday) &middot; <b>E6 frame 3</b> (a loved place closing)', 'Better covered after Pass A&prime;'],
]

CONTEXT = [
    ['<b>Works with one friend and no history</b>', 'D1, D3 variant A, D4, D5, D6 frame 1, D7, D8 frames 1 and 3 &middot; <b>E1, E2, E7, E8</b>'],
    ['<b>Works with no friends on the product at all</b>', '<b>E4</b> as the asker, <b>E6 frame 1</b> &mdash; and the guest in <b>E1</b>, who has no app'],
    ['<b>Needs real prior contribution</b>', 'D2, D3 variant B, D6 frame 2, D9 frame 1 &middot; <b>E3</b>, and contributor supply for <b>E4</b>'],
    ['<b>Needs a shared occasion months earlier</b>', 'D10 &middot; <b>E5</b>, which needs years'],
]

CLAIMS_YES = [
    'Eighteen experience canvases exist &mdash; ten in Pass A, eight in Pass A&prime; &mdash; each with a starting situation, the actual value received, the essential interaction and an ending.',
    'Each direction carries separate review notes: minimum context, effort per person, audience consequence, low participation, one change or failure, and an ordinary-app comparison at three levels.',
    'Each direction carries one qualitative verdict and one unanswered question. Omissions are named on the board they belong to.',
    'The shared design language is consumed, not imitated: components copied at vdl-stage1 0.4.1 from workbench c13ae951.',
]
CLAIMS_NO = [
    'No direction is selected, adopted, ruled on, or scheduled. Verdicts are this exploration&rsquo;s reading, offered for the founder&rsquo;s decision.',
    'Nothing here reopens or closes any Social delivery obligation. The September 12 sender, access, control, asset and guest-identity queues stand exactly as they were.',
    'No policy follows from a drawing: audience and expiry rules (D7), circle membership and historical access (D2), retention and grant windows (D10) are owned elsewhere.',
    'No engineering, schema, notification or guest-identity commitment. No claim of product-market fit, adoption, or that any of this is enjoyable in practice.',
    'The eight Pass A&prime; directions were chosen by this exploration after reading the corpus; the founder has not selected or ranked them.',
    'Passes B and C are done as drawings and argument. Their conclusions &mdash; six interactions, the removals, the order &mdash; are proposals and nothing more.',
]

def li(items, color=INK2):
    return '<div style="display: flex; flex-direction: column; gap: 7px;">' + ''.join(
        f'<div style="display: flex; gap: 10px; align-items: baseline;"><span style="color: {GHOST}; flex: none;">&mdash;</span>'
        f'<span style="font-size: 13px; line-height: 19px; color: {color};">{t}</span></div>' for t in items) + '</div>'

def build():
    inner = ''
    inner += blk('PASS A &middot; THE BRIEF&rsquo;S TEN DIRECTIONS', tbl(
        ['', 'DIRECTION', 'THEME', 'STARTS FROM', 'IMMEDIATE HUMAN PAYOFF', 'DRAWN', 'THIS EXPLORATION&rsquo;S READING'], DIRS))
    inner += blk('PASSES B AND C &middot; SEPTEMBER 21', tbl(['BOARD', 'WHAT IT DOES'], [
        ['<b>B1</b> &middot; Compare and simplify', 'Eighteen wants reduced to six interactions. The same component is drawn across different directions as evidence; seven comparisons; a reuse map.'],
        ['<b>W1</b> &middot; One weekend, and a return', 'Eight frames of an ordinary Friday to Sunday and one Saturday in November. Includes a receive that leads nowhere and an opening nobody takes.'],
        ['<b>W2</b> &middot; Far apart', 'Two friends in two cities. Complete without a meetup, a trip or a plan.'],
        ['<b>R1</b> &middot; Recommendation', 'Six interactions, not eighteen features: what each direction becomes, what to remove, what needs a ruling, what needs people.'],
        ['<b>C1</b> &middot; Copy, before and after', 'Six frames in three rounds; the rules every phone now follows.'],
    ]))
    inner += blk('WHY A SECOND PASS', N(
        'The ten directions above descend from one subsection of the canon, <b>&sect;1 &ldquo;Social benefit before social structure&rdquo;</b>, and nearly all of them are friend-to-friend, pair-scale, local and present-tense. '
        'Read against the whole social corpus &mdash; about fifteen thousand lines of canon, founder-thread strategy, research and contracts &mdash; they cover roughly three of the canon&rsquo;s eight modes and two of its six social units. '
        'Pass A&rsquo;s own verdicts kept reaching the same sentence: <i>a group message does this.</i>'))
    inner += f'<div style="display: flex; gap: 46px; align-items: flex-start;">'
    inner += f'<div style="flex: 0.8;">' + blk('HOW IT NARROWED &middot; A BOUNDARY AGAINST A MECHANISM TOOK A VALUE WITH IT', tbl(['THE BOUNDARY, WHICH WAS RIGHT', 'THE VALUE THAT WENT WITH IT'], NARROW)) + '</div>'
    inner += f'<div style="flex: 1.2;">' + blk('THE TEST EVERY PASS A&prime; DIRECTION IS HELD TO', N(
        f'<span style="{SERIF} font-size: 19px; line-height: 27px; color: {INK};">Does it need private context from more than one person, shaping a shared result, without that context being disclosed?</span><br><br>'
        'If not, ordinary messaging is the better product. The August 7 strategy names governed private context across several people as the one link competitors cannot copy. '
        'What a chat structurally cannot do: keep a surprise from someone whose own assistant knows about it; ask each person privately and let one &ldquo;no&rdquo; mean silence for everyone; give a newcomer a private way in; '
        'hold one evening as several different memories; leave something on a street corner for one person to find. '
        '<b>Strangers, where they appear at all, reach each other through a Place and a deliberate act &mdash; never through presence, proximity or matching</b> (canon &sect;12 against &sect;11 step 6).')) + '</div></div>'
    inner += blk('PASS A&prime; &middot; EIGHT FURTHER DIRECTIONS', tbl(
        ['', 'DIRECTION', 'THEME', 'STARTS FROM', 'HUMAN PAYOFF', 'PRIVATE-CONTEXT TEST', 'THIS EXPLORATION&rsquo;S READING'], EDIRS))
    inner += blk('THE CANON, AGAINST BOTH PASSES', tbl(['WHAT THE CANON NAMES', 'IN D1&ndash;D10', 'ADDED BY E1&ndash;E8', 'STILL NOT DRAWN'], CANON))
    inner += blk('NAMED AND NOT YET DRAWN', li(UNDRAWN))
    inner += f'<div style="display: flex; gap: 46px; align-items: flex-start;">'
    inner += f'<div style="flex: 1.15;">' + blk('HOW VALUE ARRIVES, AND WHERE IT IS SHOWN', tbl(['MODE', 'DRAWN ON', 'COVERAGE'], ARRIVAL)) + '</div>'
    inner += f'<div style="flex: 0.85;">' + blk('HOW MUCH CONTEXT EACH BENEFIT NEEDS', tbl(['', 'DIRECTIONS'], CONTEXT)) + '</div></div>'
    inner += f'<div style="display: flex; gap: 46px; align-items: flex-start;">'
    inner += f'<div style="flex: 1;">' + blk('WHAT THESE BOARDS DO ESTABLISH', li(CLAIMS_YES)) + '</div>'
    inner += f'<div style="flex: 1;">' + blk('WHAT THEY DO NOT', li(CLAIMS_NO)) + '</div></div>'
    inner += blk('READING THEM', N(
        'Each direction board reads left to right: the frames are the experience, the columns beneath are the review. '
        'A dashed box is a labelled state of the frame above it, not an extra screen. '
        '<b>EXPLORATORY</b> means the composition is a proposal made here and nowhere else. '
        '<b>PROPOSED FIXTURE</b> marks a person, object or event invented for this brief &mdash; it is not an addition to anyone&rsquo;s actual history, '
        'and it does not enter the shared fixture ledger. '
        'A blue tag names a shared-package component the frame consumes. '
        'Every world fact &mdash; hours, closures, ferry times, geology &mdash; is a fixture, and where a frame would depend on current information it says so on the frame.'))
    inner += blk('HOW THE SCREENS TALK &middot; COPY PASS, SEPTEMBER 21', N(
        'Every phone on D1&ndash;D10 and E1&ndash;E8 was rewritten after the founder found the copy strange. Measured before the pass, <b>39% of the words inside the phones were not product copy</b>: '
        'explanations to the reviewer and statements of what the product refuses to do, set in the app&rsquo;s own type. After it: explainer boxes 0%, mono notes 4% (provenance only), and people&rsquo;s own words up from 7% to 16%. '
        'The rules are the Voice Canon&rsquo;s object-first rule and Editorial Canon &sect;13.3, plus four a social product needs. '
        '<b>Four voices, kept apart:</b> a person speaking (as typed, in the shared reader, never tidied) &middot; a person acting (buttons in their own words: &ldquo;I&rsquo;m in&rdquo;) &middot; '
        'Vesper stating (the state, with a name, time, number or place in it) &middot; Vesper advising (&ldquo;I&rsquo;d ___. It ___.&rdquo;). '
        'Vesper does not summarize people. Boundaries use the everyday noun that already contains them (&ldquo;Surprise&rdquo;, &ldquo;Just you&rdquo;, &ldquo;Until 5:00&rdquo;). Provenance says source and day. '
        'Every design decision that used to be recited on a screen now sits in that board&rsquo;s review notes under <b>DECIDED, NOT DISPLAYED</b>. '
        'Board <b>C1</b> shows six frames before, after a first rewrite, and pushed further. Place names such as The Lantern, Tilde and Lul&uacute;&rsquo;s are fixtures invented for these frames.'))
    inner += blk('THE DESIGN LANGUAGE', N(
        'Components, stylesheets and the production-kernel copy were copied from workbench <b>c13ae951</b> at <b>vdl-stage1 0.4.1</b>, '
        'the version declared in its own vdl-package.json. Adoption is by copy at that version, not live synchronisation; vdl-package.json ships in this project as the record. '
        'Eleven components are available; these boards consume five &mdash; OriginalReader, InviteCard, Notice, FactPair, SourceList &mdash; plus the shared sheet, field, button and recipient styles. '
        'The board grammar (phone frames, section rules, captions, labelled insets) is the same one the Social, Home and Places projects use. '
        '<b>Not consumed:</b> the newer S2 instrument library in that workbench, which is undeclared in the manifest and is another lane&rsquo;s work in progress.'))
    inner += blk('AUTHORITY AND SOURCES', N(
        'Brief: <b>docs/working/claude-design-multiplayer-product-shapes-exploration-2026-09-20.md</b>. The corpus reading behind Pass A&prime;, with five reader digests and section citations, is in <b>docs/working/multiplayer-corpus-digest-2026-09-20/</b>. '
        'This exploration is separate from and additive to the Social Experience project (3ef10868), whose accepted boards and unfinished delivery queue are untouched &mdash; '
        'a separate project is the strongest guarantee of that. Where a direction reuses Social&rsquo;s settled work (sender controls, send results, the guest link), it is named and reused, not redesigned. '
        'The cast &mdash; Nora, Maya, Priya, Sam, Dana &mdash; comes from the shared fixture ledger; everything marked PROPOSED FIXTURE was invented for this brief. '
        'The research cited in the brief supports mechanisms and questions, not fit: it is quoted on the boards only where it argues <i>against</i> something.'))
    return write('A0 - Method and coverage', sheetboard(
        1860, hh('A0', 3300),
        'A0 &middot; ARCHIVE &middot; HOW THE EXPLORATION WAS RUN',
        'Method and coverage',
        'A bounded comparative exploration of the full multiplayer opportunity: what each shape gives a person, what it costs '
        'each person involved, and whether it beats an ordinary app. Pass A drew the brief&rsquo;s ten directions; Pass A&prime; adds eight after the founder judged those too narrow. '
        'Rough honest breadth is worth more at this stage than a few persuasive demos. Nothing here is selected.',
        inner))

if __name__ == '__main__':
    print(build())
