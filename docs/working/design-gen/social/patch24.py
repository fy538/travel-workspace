"""Shared-package adoption (vdl-stage1 0.3) + September 10 additive review.
Consumes OriginalReader (full), InviteCard (host, guest; pill) and Notice from the workbench c13ae951.
Adds the first-host step, the recipient choice/correction and reply result as insets, and the fair-baseline work account."""
import re
MISS = []
def sub(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        n = s.count(old)
        if n == 1: s = s.replace(old, new)
        elif new in s: pass
        else: MISS.append((path, old[:90], n))
    open(path, 'w').write(s)
def rsub(path, pat, new):
    s = open(path).read(); s2, n = re.subn(pat, lambda m: new, s, count=1, flags=re.S)
    if n != 1: MISS.append((path, pat[:90], n))
    open(path, 'w').write(s2)

VER = 'vdl-stage1 0.3'

# ───────────────────────────── gen_c2 · the shared head, the reader, the insets ─────────────────────────────
sub('gen_c2.py', [
    ("from gen_se import OUT, hh, sheet, tag, ROLE, FOOT2",
     """from gen_se import OUT, hh, sheet, tag, ROLE, FOOT2

# ── shared package vdl-stage1 0.3 (workbench c13ae951): boards that place a shared component load the kernel copy and vdl.css ──
KERNEL_CSS = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'
HEAD_VDL = HEAD.replace('<helmet>', f'<helmet>\\n  <link rel="stylesheet" href="{KERNEL_CSS}">\\n  <link rel="stylesheet" href="vdl.css">', 1)
assert HEAD_VDL != HEAD, 'helmet not found in HEAD'

def dci(name, h, **props):
    \"\"\"One shared component instance. Attribute values are plain text; the runtime decodes camelCase props.\"\"\"
    attrs = ' '.join(f'{k}="{v}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'

def inset(label, body, note):
    \"\"\"A labelled state of an existing slot, drawn beside it. Not a new slot.\"\"\"
    return (f'<div style="margin-top: 14px; width: 393px; box-sizing: border-box; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px;">'
            f'<div class="kickm">{label}</div>{body}<div class="fn" style="color: #6E6862; line-height: 15px;">{note}</div></div>')
"""),
    # the full reader, from the shared component; the place-owned sections stay below it
    ("# ───────────────────────────── 02.6 · Ask Vesper about this ─────────────────────────────",
     """def reader_phone(compose=''):
    \"\"\"02.4 / 02.5 / 05 D7-A on the shared OriginalReader (density full). The gallery's notes and Priya's visit are
    Places content around the reader, not part of it, so they stay local below the component.\"\"\"
    props = dict(density='full', author='Maya', audience='Thursday · to friends', media='ILLUSTRATION · NOT HER PHOTOGRAPH',
                 words='The side room was my favorite. Go on a weekday, it was empty.', place='The Harbor Print Room',
                 placeDetail='Red Hook · Tue–Sun 11–6 · *Rooms Remade* through Sunday', placeMeta='Listed hours, not checked today',
                 ask='Ask about the Print Room')
    if compose: props['compose'] = compose
    inner = f'<div style="padding: 20px 22px 0 22px;">{dci("OriginalReader", 760 if compose else 700, **props)}</div>'
    inner += sect('From the gallery') + gut(f'<div style="display: flex; gap: 12px; align-items: flex-start;">{thumb("room", 44)}<div style="flex: 1;">{title("The side room, then and now", 15, 20, 600)}<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 3px;">The print shop that was here left the drying racks; the show hangs the new work on them.</div>{src("The gallery&rsquo;s own notes")}</div></div>')
    inner += sect('Also about the Print Room') + gut('<div>' + share_line('P', 'Priya', by('Priya', 'print_room')[2], 'her own visit, a rainy Tuesday', last=True) + '</div>')
    inner += '<div style="height: 18px;"></div>'
    return phone2(inner)

def recipient_inset():
    \"\"\"S1/S2 coverage: one account recipient found, disambiguated, chosen or corrected; the exact outgoing material; send or leave; the result.\"\"\"
    cand = lambda letter, name, how, on: (f'<div style="display: flex; align-items: center; gap: 10px; padding: 9px 0; border-bottom: 0.5px solid rgba(27,23,20,0.10);">'
                                         f'<span style="width: 26px; height: 26px; border-radius: 13px; background: #1B1714; color: #FBF7EC; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">{letter}</span>'
                                         f'<div style="flex: 1;"><div class="vk-t-bodyMd" style="color: #1B1714;">{name}</div><div class="vdl-t-supportLine" style="color: #6E6862;">{how}</div></div>'
                                         + (f'<span class="vdl-t-metaLine" style="color: #1B1714;">CHOSEN</span>' if on else '') + '</div>')
    body = (f'<div class="vdl-t-supportLine" style="color: #3C352E;">Change &rarr; Who. Maya types a name; only people she is already connected with can appear.</div>'
            f'<div class="vdl-field pill focused"><span class="vk-t-bodyMd">nora</span></div>'
            f'<div style="border-top: 0.5px solid rgba(27,23,20,0.10);">' + cand('N', 'Nora Lin', 'friend · the pasta nights', True) + cand('N', 'Nora Kaye', 'friend · from work', False) + '</div>'
            f'<div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;"><span class="vdl-t-metaLine" style="color: #6E6862;">WHO</span><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">N</span><span class="vk-t-bodySmMedium">Nora Lin</span></span><span class="vdl-t-supportLine" style="color: #6E6862;">only, through Sunday</span></div>'
            f'<div class="vdl-t-supportLine" style="color: #3C352E;">Goes out exactly as drawn above: her photograph, &ldquo;The side room was my favorite. Go on a weekday, it was empty.&rdquo;, the Print Room, Red Hook.</div>'
            f'<div class="vdl-t-supportLine" style="color: #6E6862;">No match: &ldquo;No one called &lsquo;norra&rsquo; among the people you&rsquo;re connected with.&rdquo; She corrects the name or goes back to Friends. Leaving the sheet sends nothing.</div>'
            + dci('Notice', 64, tone='applied', title='Sent to Nora only · 4:05', body='Nothing else changed.')
            + dci('Notice', 120, tone='failed', title='Didn’t send. You’re offline.', body='Your words and your choice of Nora are still here.', primary='Try again', secondary='Not now'))
    return inset('02.2, CONTINUED &middot; CHOOSE OR CORRECT ONE RECIPIENT &middot; A STATE OF THE SAME SLOT', body,
                 'SHARED &middot; .vdl-field, .vdl-recipient, Notice (applied, failed; PLANS 90 J2c&ndash;J2e SEMANTICS) &middot; ELIGIBLE CONNECTIONS ONLY: NO CONTACTS IMPORT, NO GENERAL FRIENDS PERMISSION &middot; A SECOND NORA IS FIXTURE, FOR DISAMBIGUATION')

def reply_result_inset():
    body = (dci('Notice', 64, tone='applied', title='Sent to Maya · 9:12', body='Back to her photograph. Nothing else here changed.')
            + dci('Notice', 120, tone='failed', title='Didn’t reach Maya', body='Your reply is still in the field.', primary='Try again', secondary='Not now'))
    return inset('02.5, AFTER SEND TO MAYA &middot; THE RESULT, THEN THE SAME ORIGINAL', body,
                 'SHARED &middot; Notice &middot; THE RETURN IS HER ORIGINAL AS IT WAS, NOT A SUMMARY &middot; 02.6&rsquo;S PRIVATE ASK RETURNS TO THE SAME SCROLL')

# ───────────────────────────── 02.6 · Ask Vesper about this ─────────────────────────────"""),
    ("('02.4', 'NORA', 'PLACES', opened(), ('THE PRINT ROOM, OPENED'", "('02.4', 'NORA', 'PLACES', reader_phone(), ('THE PRINT ROOM, OPENED'"),
    ("('02.5', 'NORA', 'IN CONTEXT', opened(reply_text='That side room. I want to see it before Sunday.'),",
     "('02.5', 'NORA', 'IN CONTEXT', reader_phone(compose='That side room. I want to see it before Sunday.'),"),
    ("('COPY OF PLACES 04', 'READING FROM THE GALLERY&rsquo;S NOTES &middot; FIXTURE', 'D5 &middot; ORIGINAL LEADS')",
     "('SHARED &middot; OriginalReader full &middot; " + VER + "', 'THE GALLERY&rsquo;S NOTES AND PRIYA ARE PLACES CONTENT BELOW THE READER', 'D5 &middot; ORIGINAL LEADS')"),
    ("('R1&rsquo;S CONTEXTUAL REPLY, KEPT', 'D2 STARTING POSITION: REPLY', 'NO REACTION COUNT')",
     "('SHARED &middot; OriginalReader full, compose &middot; " + VER + "', 'D2 STARTING POSITION: REPLY', 'NO REACTION COUNT &middot; RESULT BELOW')"),
    ("    cols = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P]\n    row1, row2 = cols[:4], cols[4:]",
     "    cols = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P]\n    cols[1] = cols[1][:-6] + recipient_inset() + '</div>'\n    cols[4] = cols[4][:-6] + reply_result_inset() + '</div>'\n    row1, row2 = cols[:4], cols[4:]"),
    ("    html = (HEAD + f'<div style=\"width: 1820px; min-height: {hh(\"02\")}px;", "    html = (HEAD_VDL + f'<div style=\"width: 1820px; min-height: {hh(\"02\")}px;"),
])

# ───────────────────────────── gen_c3 · InviteCard host and guest; the first-host step; fair work account ─────────────────────────────
rsub('gen_c3.py', r"    inner \+= gut\(preview_card\('TO MAYA &middot; EVERYTHING'.*?NO CONTACTS SCANNED'\), top=16\)\n",
     """    inner += gut(dci('InviteCard', 230, view='host', kicker='TO MAYA · EVERYTHING', title='Pasta trial night at Nora’s',
                     lines='WHEN=Saturday from seven;WHERE=Court Street, 3F|the buzzer says N;WITH=Sam;BRING=Nothing',
                     stamp='MAYA CAN ANSWER, SUGGEST, OR JUST COME')
                 + '<div style="height: 12px;"></div>'
                 + dci('InviteCard', 270, view='host', kicker='TO SAM · DINNER ONLY · A LINK, NO APP', title='Pasta trial night at Nora’s',
                       lines='WHEN=Saturday, dinner from seven|come at seven-thirty;WHERE=Carroll Gardens|the exact address after he confirms this number;WITH=Nora and Maya;BRING=Nothing',
                       via='BY TEXT · TO THE NUMBER YOU TYPED', stamp='HE SEES WHEN, WHERE, WHO · NOTHING ELSE OF YOURS · NO CONTACTS SCANNED'), top=16)
""")
rsub('gen_c3.py', r"def sam_invite\(\):\n.*?    return linkframe\(inner\)\n",
     """def sam_invite():
    \"\"\"03.2 on the shared InviteCard (view guest, shape pill). The link page's bar and footer stay local.\"\"\"
    inner = '<div style="padding: 20px 22px 0 22px;">' + dci('InviteCard', 640, view='guest', shape='pill', kicker='FROM NORA · A LINK · NOTHING TO INSTALL',
                title='Pasta trial night. Saturday from seven; come at seven-thirty.',
                note='“Second attempt at the Sorrento thing. Maya’s coming. Bring nothing, honestly.”', noteBy='NORA, THURSDAY',
                lines='Saturday Sep 19 · dinner from seven|you’re expected around seven-thirty;Carroll Gardens, near Court Street|the exact address after a one-time code to this number;With Nora and Maya|',
                **{'from': 'Nora'},
                guestNote='Nora sees your answer as yours once you confirm this number, the same step that unlocks the address. No reason needed either way.',
                answer='I’ll need to leave by nine', stamp='ANYTHING SHE SHOULD KNOW · OPTIONAL · GOES TO NORA ONLY') + '</div>'
    return linkframe(inner)
""")
sub('gen_c3.py', [
    ("def offline_note():",
     """def first_host_inset():
    \"\"\"The first evening: 03.1 when the address is not yet known. Reuse what is known, ask only the missing fact, once, then the same previews.\"\"\"
    known = ('<div class="vdl-t-supportLine" style="color: #3C352E;">Already known and reused, not asked again: Saturday, seven, Maya, Sam and the number you typed, nothing to bring.</div>')
    ask = ('<div style="display: flex; flex-direction: column; gap: 8px;">'
           '<div style="align-self: flex-start; max-width: 300px; font-family: var(--vk-font-serif); font-size: 16px; line-height: 22px; color: #1B1714;">One thing before the previews: which address should Maya get?</div>'
           '<div style="align-self: flex-end; max-width: 260px; background: #4A3428; color: #FBF7EC; border-radius: 18px; padding: 9px 14px; font-size: 14px; line-height: 19px;">court st 3F, the buzzer says N</div></div>')
    back = '<div class="vdl-t-supportLine" style="color: #3C352E;">Then the same two previews and <b>Send to Maya and Sam</b>, with her words and choices as she wrote them. Next time the address is already known.</div>'
    return inset('03.1, THE FIRST EVENING &middot; ONE MISSING FACT, ASKED ONCE', known + ask + back,
                 'NOT A PROFILE, A CONTACTS IMPORT OR A SETUP FLOW &middot; THE SAME CHAT, ONE ANSWER &middot; COUNTED IN THE WORK TABLE BELOW &middot; GUEST VERIFICATION, RECOVERY AND UNAVAILABLE ACCESS REMAIN NAMED DEPENDENCIES')

def offline_note():"""),
    ("    cols1[3] = cols1[3][:-6] + provisional_inset() + '</div>'",
     "    cols1[0] = cols1[0][:-6] + first_host_inset() + '</div>'\n    cols1[3] = cols1[3][:-6] + provisional_inset() + '</div>'"),
    ("'SEVEN SENTENCES &middot; RULED', 'R7 C1 &middot; COPY', 'THE READBACK IS ONE LINE ON HOME, NOT A PHONE'",
     "'SEVEN SENTENCES &middot; RULED', 'SHARED &middot; InviteCard host &times;2 &middot; " + VER + " &middot; LABELLED FACTS AS REVIEWED ON 02B', 'THE READBACK IS ONE LINE ON HOME, NOT A PHONE'"),
    ("('R7 C2 &middot; ADAPTED', 'PROPOSED BRANCH V: VERIFIED AT THE FIRST SENSITIVE BOUNDARY (THE ADDRESS)",
     "('SHARED &middot; InviteCard guest, pill &middot; " + VER + "', 'PROPOSED BRANCH V: VERIFIED AT THE FIRST SENSITIVE BOUNDARY (THE ADDRESS)"),
    ("    return (HEAD + f'<div style=\"width: 2260px; min-height: {hh(\"03\")}px;", "    return (HEAD_VDL + f'<div style=\"width: 2260px; min-height: {hh(\"03\")}px;"),
])
rsub('gen_c3.py', r"WORK = \[\n.*?\]\nFIXTURE_NOTE = \(.*?\)\n",
     """WORK = [
    ['Nora &middot; the host', 'Writes the invitation once, pastes it into two threads and cuts the address out of Sam&rsquo;s by hand. The address is already in her earlier messages to Maya, so she reuses it; search finds Dana&rsquo;s tip. She forwards Dana&rsquo;s photograph and tip to both threads, reads three answers across two threads, and remembers Sam&rsquo;s nine herself when Maya asks about eight. Two weeks later she scrolls up and copies the last invitation', 'The first evening asks her one thing, the address, once (03.1 inset); every evening after, one sentence and one Send, with a preview per recipient (03.1). The answers and contributions arrive on one page, attributed (03.4). Maya&rsquo;s ask arrives with the facts it touches (03.5). Two weeks later the draft already holds the address, the buzzer, the photograph and the dish (04.8)', 'Hand-editing a second version for a guest; reading three threads as one evening; carrying a constraint into a change. Not retyping: a competent thread reuses the address too', 'Choosing the food, cooking it, and saying the invitation in her own words'],
    ['Maya &middot; a friend', 'Sends the photograph in one thread and, if she wants the evening to see it, again in the dinner thread; asks about eight where everyone is reading', 'Shares once from the object itself (02.2); her suggestion lands under the dinner row as a suggestion (03.4); her ask reaches the owner as a decision, not a demand in front of the group (03.5)', 'Sending the same thing twice; a private suggestion read publicly', 'Deciding to share at all, and what to say. She owes no reply, no photograph and no answer'],
    ['Sam &middot; a guest with no account', 'Gets a clear text with when and roughly where; asks for the exact address and the buzzer on the day; says he must leave by nine and says it again if the time changes', 'Opens a link and answers once; confirms his number when the address is needed (03.2, 03.4); the arrival view carries the door, the time and his nine (03.7)', 'Asking for the door on the night, and repeating his own constraint. A good text already answers when and roughly where', 'Deciding whether to come, and saying when he has to go'],
    ['Dana &middot; elsewhere, not attending', 'Nora asks; Dana sends a photograph and a paragraph; Nora forwards both and explains them again', 'One addressed line reaches her; she sends one thing to the dinner&rsquo;s people, attributed, without joining (03.3)', 'The forwarding and re-explaining; her name stays on her contribution', 'Choosing to send something at all. She is owed nothing back'],
    ['The honest total', 'A competent message thread, with search, links and a reused address, does most of this, and everyone already has one', 'What remains: two recipient-specific versions from one sentence; one attributed page instead of three threads; a constraint carried into a change; an arrival view for a person with no account; and a first evening that asks for the address once', 'Assembly and coordination, unevenly: Nora gains most, the recipients only what they use', 'Nothing here removes cooking, choosing, or writing to a friend, and nobody owes equal effort'],
]
FIXTURE_NOTE = ('The fixture hands Vesper the address, the buzzer, Sam&rsquo;s number, Dana&rsquo;s dish and last month&rsquo;s photograph already assembled. '
                'The first-host step on 03.1 now shows the one thing a real first evening must ask, the address, once; it is counted in Nora&rsquo;s row. '
                'The baseline is given the same competence as 05 D7&rsquo;s: search, existing links and a reused address. Vesper is credited only with assembly and coordination it actually removes, not with retyping the thread would not have to do.')
""")

# ───────────────────────────── gen_c5 · D7-A on the shared reader; 07 records the adoption and coverage ─────────────────────────────
sub('gen_c5.py', [
    ("side('A &middot; A1 RECEIVED &middot; REUSES 02.4; THE AFTERNOON IS 03.5', opened(),", "side('A &middot; A1 RECEIVED &middot; REUSES 02.4; THE AFTERNOON IS 03.5', reader_phone(),"),
    ("    return (HEAD + f'<div style=\"width: 2260px; min-height: {hh(\"05\")}px;", "    return (HEAD_VDL + f'<div style=\"width: 2260px; min-height: {hh(\"05\")}px;"),
    ("    selected = blk('SELECTED DIRECTION &middot; SEPTEMBER 9 DECISION, RECEIVED',",
     """    adopt = blk('SHARED PACKAGE CONSUMED &middot; VDL-STAGE1 0.3 FROM WORKBENCH C13AE951', tbl(['FRAME', 'SHARED COMPONENT', 'VARIANT', 'WHAT STAYED LOCAL'], ADOPT)
                + N('<b>Consumed files:</b> OriginalReader, InviteCard and Notice at the workbench etags recorded in vdl-package.json; vdl.css (sha256 7b6fa1d3&hellip;) and the kernel copy of styles.css (sha256 a843ca5b&hellip;, identical to the published kernel file, stamp travel-app@e2e792913). Boards 02, 03 and 05 load both stylesheets; every other board is unchanged construction. The originals are kept in this project as <i>Before shared package</i> copies of boards 02, 03 and 05. '
                    '<b>Missing variants, reported rather than redrawn:</b> ' + '; '.join(MISSING) + '.'))
    coverage = blk('COVERAGE FOLLOW-THROUGH &middot; SEPTEMBER 10 &middot; EACH ITEM WITH A DISPOSITION, OWNER AND NEXT TRIGGER', tbl(['ITEM', 'FRAMES', 'DISPOSITION', 'OWNER', 'NEXT TRIGGER'], COVERAGE))
    selected = blk('SELECTED DIRECTION &middot; SEPTEMBER 9 DECISION, RECEIVED',"""),
    ("    inner = comp + selected + sep9c +", "    inner = comp + adopt + coverage + selected + sep9c +"),
    ("WORKLEFT = [",
     """ADOPT = [
    ['02.4 &middot; the Print Room, opened', 'OriginalReader', 'density full', 'The gallery&rsquo;s notes and Priya&rsquo;s visit, which are Places content around the reader. The private Ask now sits directly under the reply field, as the shared reader places it, instead of after those sections'],
    ['02.5 &middot; Reply to Maya, in context', 'OriginalReader', 'density full, compose', 'The same place-owned sections; the result below it on the shared Notice'],
    ['05 D7-A &middot; A1 received', 'OriginalReader', 'density full', 'As 02.4'],
    ['03.1 &middot; host once', 'InviteCard &times;2', 'view host, labelled facts, delivery line on Sam&rsquo;s', 'The chat around them: Nora&rsquo;s sentence, the answer line, Send and the field'],
    ['03.2 &middot; Sam&rsquo;s link', 'InviteCard', 'view guest, shape pill', 'The link page&rsquo;s address bar and its footer'],
    ['02.2 continued, 02.5 result', 'Notice', 'tone applied, failed', 'The inset frame around them'],
]
MISSING = [
    'OriginalReader full with an optional Keep and a non-spatial &ldquo;where it lives&rdquo; in place of the place row (08.2; Life 07.7/07.8 is the donor), so 08.2 stays local',
    'OriginalReader for the sender&rsquo;s own share, with its one reply, Edit and Take it back and a withdrawal that can fail (02.7, 04.9), so 02.7 stays local',
    'OriginalReader open or card with a photograph (04.2 and 08.1, a friend&rsquo;s photo arriving on Home), so both stay local',
    'InviteCard for a changed arrangement seen by a guest, with a primary and a secondary answer under his own labels (03.6); the answered view offers two secondary actions only, so 03.6 stays local',
    'InviteCard for the day of arrival (03.7), and the guest link page&rsquo;s bar and footer, neither of which is in the package',
    'An attributed contribution on an occasion page, with its scope line and optional media (03.3, 03.4), not in the package',
]
COVERAGE = [
    ['Choose or correct one recipient, with a no-match case', '02.2 inset; 03.1; 08.4', 'Targeted addition, drawn: a field over eligible connections only, two same-named friends told apart by how they are connected, the chosen recipient token, the exact outgoing material, send or leave, and the result on Notice. No contacts import', 'Shared-library owner, for a recipient picker built on .vdl-field and .vdl-recipient', 'Shared review of a picker component'],
    ['Optional words, audience and time, Change, send or leave', '02.2', 'Existing donor, now with its result on the shared Notice. No posting wizard', 'Shared-library owner', 'Composer component in the next package'],
    ['Reply versus private Ask, and the return', '02.5, 02.6', 'Existing donor, now built on OriginalReader full (compose) with the result on Notice; the Ask returns to the same scroll and the original is not summarised', 'Shared-library owner; Chat owner for 02.6&rsquo;s frame', 'Later native check'],
    ['The sender&rsquo;s own share: edit, take back, and a withdrawal that fails', '02.7, 04.9', 'Owner dependency: the missing sender variant above. No viewer list, no private-use report', 'Shared-library owner, with Plans 90&rsquo;s recovery semantics', 'Next package'],
    ['The first host step', '03.1 inset', 'Targeted addition, drawn: known facts reused, the one missing fact asked once, the same previews and Send; counted in 03&rsquo;s work table', 'Social', 'Founder review of this pass'],
    ['Guest invitation and arrival; later media', '03.2&ndash;03.7, 04.3', 'Existing donor: 03.2 adopted on InviteCard guest. Verification, recovery and unavailable access stay a named dependency of the proposed guest branch, not coverage by RSVP', 'Guest identity proposal owner', 'If the guest branch is selected for delivery'],
]
WORKLEFT = ["""),
])

# ───────────────────────────── gen_se · consumed release on 00 ─────────────────────────────
sub('gen_se.py', [
    ("STAMP = 'SELECTED DIRECTION &middot; RESIDUAL CORRECTIONS &middot; 2026-09-10'", "STAMP = 'SHARED PACKAGE VDL-STAGE1 0.3 CONSUMED &middot; 2026-09-11'"),
    ("'SELECTED: original-first casual receiving is an exemplar; each line carries its own source, so the non-use narration is gone'",
     "'SHARED 0.3: 02.4, 02.5 on OriginalReader full; recipient choice and reply result on Notice; 08.2-style Keep and 02.7 sender view reported as missing variants'"),
    ("'SELECTED: 03.5 prepares one message to Maya and ends in Send proposal; dinner stays at seven; the guest-hospitality sequence 03.7&ndash;03.8 is an exemplar'",
     "'SHARED 0.3: 03.1 on InviteCard host, 03.2 on InviteCard guest; the first-host step added as an inset; the work account given a fair baseline'"),
    ("'CORRECTED: D7&rsquo;s inputs matched, both sides given A1, B2b and Nora&rsquo;s own constraint; 13 frames = UNRESOLVED SCOPE DISCREPANCY'",
     "'SHARED 0.3: D7-A on OriginalReader full; D7&rsquo;s matched inputs unchanged; 13 frames = UNRESOLVED SCOPE DISCREPANCY'"),
    ("'SELECTED DIRECTION: the two exemplars, the prepared-message effects received from the decision, D7&rsquo;s matched inputs, the bounded asset gap, both budget discrepancies'",
     "'SHARED 0.3: what each frame consumes, the missing variants, the coverage follow-through with owners and triggers; both budget discrepancies'"),
])

# ───────────────────────────── measure over HTTP: components are fetched at runtime ─────────────────────────────
for m in ('measure_c2.py', 'measure.py'):
    s = open(m).read()
    if 'http://127.0.0.1:8766/' not in s:
        s = s.replace("import json,os,subprocess,sys", "import json,os,subprocess,sys,urllib.parse", 1)
        s = s.replace("f'file://{os.getcwd()}/out/{n}.dc.html'", "'http://127.0.0.1:8766/'+urllib.parse.quote(n)+'.dc.html'")
        s = s.replace("'--virtual-time-budget=9000'", "'--virtual-time-budget=14000'")
        open(m, 'w').write(s)
    if 'http://127.0.0.1:8766/' not in open(m).read(): MISS.append((m, 'http shoot', 0))

print('patched; misses:', len(MISS)); [print('  MISS', *x) for x in MISS]
