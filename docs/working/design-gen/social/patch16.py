"""Handoff §15 (16:38): A carry the dinner branch through arrival; B provisional RSVP; C cleanup."""
MISS = []
def sub(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        n = s.count(old)
        if n == 1: s = s.replace(old, new)
        elif new in s: pass
        else: MISS.append((path, old[:90]))
    open(path, 'w').write(s)
def replace_func(path, name, new_src):
    s = open(path).read()
    i = s.index(f'\ndef {name}(')
    j = s.find('\n# ───', i + 1); k = s.find('\ndef ', i + 1)
    j = min(x for x in (j, k) if x != -1)
    s = s[:i] + '\n' + new_src.rstrip('\n') + '\n' + s[j:]
    open(path, 'w').write(s)

# ───────────────────────────── gen_c3 · B provisional RSVP; A arrival variant ─────────────────────────────
sub('gen_c3.py', [
    ("<div style=\"font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;\">Nora sees your answer. No reason needed either way.</div>",
     "<div style=\"font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;\">Nora sees your answer as yours once you confirm this number, the same step that unlocks the address. No reason needed either way.</div>"),
    ("    inner += sect('People') + gut('<div>' + person_row('M', 'Maya', 'in &middot; the Print Room first, she says') + person_row('S', 'Sam', 'in &middot; from seven-thirty &middot; leaves by nine') + person_row('D', 'Dana', 'not coming &middot; sent one thing', last=True) + '</div>')",
     "    inner += sect('People') + gut('<div>' + person_row('M', 'Maya', 'in &middot; the Print Room first, she says') + person_row('S', 'Sam', 'in, confirmed 8:40 pm &middot; from seven-thirty &middot; leaves by nine') + person_row('D', 'Dana', 'not coming &middot; sent one thing', last=True) + '</div>')"),
    ("    inner += gut('<div>' + row('Same place &middot; <span style=\"color: #6E6862;\">come at eight, or seven-thirty as planned</span>', mark='solid', color=GOLD)\n                 + row('Your nine still stands', mark='hollow', last=True) + '</div>', top=16)",
     "    inner += gut('<div>' + row('Same place &middot; <span style=\"color: #6E6862;\">come at eight, or seven-thirty as planned</span>', mark='solid', color=GOLD)\n                 + row('Your nine still stands', mark='hollow')\n                 + row('Maya and Nora have the new time &middot; <span style=\"color: #6E6862;\">the dinner page updated for everyone</span>', mark='hollow', last=True) + '</div>', top=16)"),
])
replace_func('gen_c3.py', 'sam_arrival', '''def sam_arrival(start='seven'):
    """Parameterized by the arrangement in force: 'seven' (unchanged, recommended) or 'eight' (adopted branch)."""
    exp = 'seven-thirty' if start == 'seven' else 'eight'
    inner = guestbar('SATURDAY 7:10 PM &middot; TONIGHT &middot; VERIFIED' if start == 'seven' else 'SATURDAY 7:40 PM &middot; TONIGHT &middot; VERIFIED &middot; ADOPTED BRANCH')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Dinner from {start}. You&rsquo;re expected around {exp}.</div>', top=14)
    nine = 'Leaving by nine is fine &middot; <span style="color: #6E6862;">she knows</span>' if start == 'seven' else 'Leaving by nine is fine &middot; <span style="color: #6E6862;">she knows; it&rsquo;s an hour</span>'
    inner += gut('<div>' + row('Court Street, 3F &middot; <span style="color: #6E6862;">the buzzer says N; the door sticks, push</span>', mark='solid', color=INK)
                 + row('Nothing to bring &middot; <span style="color: #6E6862;">really</span>', mark='hollow')
                 + row(nine, mark='hollow', last=True) + '</div>', top=16)
    inner += gut(f'<div style="border-radius: 12px; overflow: hidden;">{standin(140, "DANA&rsquo;S RAG&Ugrave; &middot; STAND-IN")}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">Dana sent this from Sorrento. It&rsquo;s what Nora&rsquo;s making.</div>', top=20)
    inner += gut(door('Running late? Say so') + src('One line to Nora.'), top=22)
    return linkframe(inner)

def arrival_variant():
    """The adopted branch's arrival, as a labelled parameterized state of 03.7: an inset, not a slot."""
    return (f'<div style="margin-top: 14px; border: 1px dashed rgba(122,46,46,0.45); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div class="fn" style="color: {OX};">ADOPTED BRANCH &middot; THE SAME 03.7, PARAMETERIZED &middot; ONLY AFTER 03.6</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 16px; line-height: 21px;">Dinner from eight. You&rsquo;re expected around eight.</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2};">Court Street, 3F, the buzzer says N &middot; nothing to bring &middot; leaving by nine is fine; she knows it&rsquo;s an hour &middot; Dana&rsquo;s rag&ugrave; &middot; one line if late.</div>'
            f'<div class="fn" style="color: {ANCHOR};">WHO HAS THE NEW TIME: NORA (OWNER), MAYA (PROPOSED IT), SAM (AFFECTED, ANSWER PENDING UNTIL HE SAYS); DANA&rsquo;S CONTRIBUTION UNCHANGED &middot; HIS SILENCE IS NOT ACCEPTANCE OF EIGHT</div></div>')

def provisional_inset():
    """The host's provisional state before Sam confirms: an inset beside 03.4, not a slot."""
    return (f'<div style="margin-top: 14px; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div class="kickm">EARLIER FRIDAY &middot; PROVISIONAL &middot; THE SAME 03.4 BEFORE SAM CONFIRMS</div>'
            f'<div>' + person_row('S', 'Sam', 'answered &ldquo;in&rdquo; from the link &middot; not yet confirmed &middot; the address waits', last=True) + '</div>'
            f'<div class="fn" style="color: {ANCHOR};">A LINK-HOLDER RESPONSE IS PROVISIONAL UNTIL THE ONE-TIME CODE TO THE NUMBER NORA TYPED; THE SAME CODE UNLOCKS THE ADDRESS. IF IT NEVER HAPPENS, NORA NEVER SEES A CONFIRMED &ldquo;IN&rdquo;. A DECLINE OR A PRIVATE LINE FOLLOWS THE SAME RULE</div></div>')
''')
sub('gen_c3.py', [
    ("    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]\n    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2] + [offline_note()]",
     "    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]\n    cols1[3] = cols1[3][:-6] + provisional_inset() + '</div>'\n    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2] + [offline_note()]\n    cols2[2] = cols2[2][:-6] + arrival_variant() + '</div>'"),
    ("('SATURDAY 7:10 PM', 'HOSPITALITY, NOT GUEST MATCHING', 'Expected around seven-thirty; find the door; nothing to bring', 'SUPPLIED FACTS ONLY &middot; DANA&rsquo;S DISH AS A FOOTHOLD &middot; NO NAVIGATION, NOTHING FOLLOWS HIM &middot; ONE LINE IF LATE')",
     "('SATURDAY 7:10 PM &middot; UNCHANGED-SEVEN ROUTE', 'HOSPITALITY, NOT GUEST MATCHING', 'Expected around seven-thirty; find the door; nothing to bring', 'SUPPLIED FACTS ONLY &middot; DANA&rsquo;S DISH AS A FOOTHOLD &middot; ONE LINE IF LATE &middot; THE ADOPTED BRANCH&rsquo;S ARRIVAL IS THE LABELLED VARIANT BELOW')"),
    ("('FRIDAY 7:30 PM', 'THE DINNER, AS ONE PAGE', 'Who is in, and what people sent, attributed', 'NO COPY-AND-PASTE FOR THE HOST &middot; MAYA&rsquo;S SUGGESTION IS NOT A CHANGE &middot; ONE WAY TO CHANGE ANYTHING: SAY IT')",
     "('FRIDAY 8:45 PM', 'THE DINNER, AS ONE PAGE', 'Who is in (Sam confirmed), and what people sent, attributed', 'NO COPY-AND-PASTE FOR THE HOST &middot; MAYA&rsquo;S SUGGESTION IS NOT A CHANGE &middot; THE PROVISIONAL STATE BEFORE SAM CONFIRMED IS THE INSET BELOW')"),
    ("('SATURDAY 2:05 PM &middot; ADOPTED BRANCH, SEPARATE', 'WHAT CHANGED, FOR HIM ONLY', 'Nora applied eight; one sentence on his row', 'DRAWN ONLY FOR THE ADOPTED BRANCH &middot; HIS ACCEPTANCE IS NOT INVENTED &middot; SILENCE IS NOT ACCEPTANCE')",
     "('SATURDAY 2:05 PM &middot; ADOPTED BRANCH, SEPARATE', 'WHAT CHANGED, TAILORED TO HIM', 'Nora applied eight; his row says what it means for nine; everyone at the dinner has the new time', 'DRAWN ONLY FOR THE ADOPTED BRANCH &middot; HIS ACCEPTANCE IS NOT INVENTED &middot; SILENCE IS NOT ACCEPTANCE &middot; CONTINUES TO THE 03.7 VARIANT')"),
    ("         ('Sam', 'A link, no app', 'Open, answer', 'Understands the evening and his time', 'Nora sees his answer and nothing else about him', 'Occasion (guest view)', '&mdash;', 'I&rsquo;m in; or can&rsquo;t')",
     "         ('Sam', 'A link, no app', 'Open, answer', 'Understands the evening and his time', 'Nora sees a provisional answer; confirmed by the same code that unlocks the address', 'Occasion (guest view)', '&mdash;', 'I&rsquo;m in; or can&rsquo;t')"),
    ("         ('Sam', 'His link', 'Read', 'What changed and what it means for nine', 'Only the relevant recipient consequence', 'Occasion (guest view)', '&mdash;', 'Answer, or not')",
     "         ('Sam', 'His link', 'Read', 'What changed and what it means for nine', 'Tailored to him; Nora and Maya have the new time too', 'Occasion (guest view)', '&mdash;', 'Answer, or not; then the eight arrival')"),
])

# ───────────────────────────── gen_c4 · Home delta bounded; before/after ─────────────────────────────
sub('gen_c4.py', [
    ("    inner += sect('Today') + gut(u2('Bach on the organ at the old church, four o&rsquo;clock', 'The Passacaglia and two chorale preludes, forty minutes, free. The back pews are the good ones for the sound.', meta_t='DOWNTOWN &middot; SUNDAY 4 PM &middot; LISTED, NOT CHECKED TODAY') + door('The old church'))",
     "    inner += sect('Today') + gut(u2('Bach on the organ at the old church, four o&rsquo;clock', 'The Passacaglia and two chorale preludes, forty minutes, free.', meta_t='DOWNTOWN &middot; SUNDAY 4 PM &middot; LISTED, NOT CHECKED TODAY &middot; PRIYA, LAST MONTH: &ldquo;GO EARLY FOR THE BACK PEWS&rdquo;') + door('The old church'))"),
    ("    inner += sect('Tonight') + gut(u2('Hand-pulled noodles at the counter till ten', 'Three blocks from Canal Hall; no wait after nine. $14&ndash;18.', meta_t='CANAL STREET &middot; DAILY 6&ndash;10 &middot; LISTED, NOT CHECKED TODAY') + door('The noodle counter'))",
     "    inner += sect('Tonight') + gut(u2('Hand-pulled noodles at the counter till ten', 'Three blocks from Canal Hall. $14&ndash;18.', meta_t='CANAL STREET &middot; LISTED DAILY 6&ndash;10, NOT CHECKED TODAY') + door('The noodle counter'))"),
    ("One line; the draft carries the place and the proposed start; the photo is one tap away. Sam&rsquo;s old 7:30 and nine stay history, not defaults.", "One line; the draft carries the place and the proposed start; the photo is one tap away."),
    ("('SUNDAY 10:20 AM', 'IT ARRIVES ONCE, AS THE IMAGE', 'From last night; a quiet Sunday with one concrete opening', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION &middot; BACH AT FOUR IS THE WORLD OPENING A QUIET DAY STILL MERITS (HOME-OWNER DELTA) &middot; ALSO IN LIFE')",
     "('SUNDAY 10:20 AM', 'IT ARRIVES ONCE, AS THE IMAGE', 'From last night; a quiet Sunday with a concrete opening', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION &middot; BACH AT FOUR IS AN ILLUSTRATIVE USEFUL OPENING, NOT A RULE OF ONE (HOME-OWNER DELTA) &middot; LISTED FACTS AND AN ATTRIBUTED LINE KEPT APART')"),
])

# ───────────────────────────── gen_c5 · C cleanup ─────────────────────────────
sub('gen_c5.py', [
    ("a proposal arrives as one ask with its cost and no button, and seven stands until the host says otherwise; the guest gets an arrival frame on the day; the evening happens with the phones away.",
     "a proposal arrives as one ask with its cost and a direct action, and seven stands unless the host adopts eight, in which case everyone at the dinner has the new time and the guest&rsquo;s arrival view follows the adopted branch; the guest gets an arrival frame on the day; the evening happens with the phones away."),
    ("the boat couple get their photo from a row on the record; a withdrawal removes only what depended on the note.'))", "the boat couple get their photo from their own record, linked from Life People; a withdrawal removes only what depended on the note.'))"),
    ("    ['Nora wants help, then chooses whether a fragment is worth sharing', '02.1 &rarr; 02.2', 'Works: the answer is complete with nothing kept; the share is a separate gesture', 'The direct share from an existing photo (not via Chat) is asserted in the caption, not drawn', 'Accepted: one caption line; the entry is the Life photo page&rsquo;s Share door'],",
     "    ['Nora wants help with something (02.1); a friend chooses whether a fragment is worth sharing (Maya, 02.2)', '02.1; 02.2 &rarr; 02.7', 'Works: the private answer keeps nothing; Maya shares from the object with no prelude and her return restores it', '&mdash;', 'Corrected after &sect;15: the two paths are independent'],"),
    ("    ['Dana sends one helpful thing from elsewhere without joining or administering', '03.3 &rarr; 03.4', 'Works: her gesture, its scope, its arrival attributed', 'Her after-send state (a receipt with Undo) is not drawn', 'Accepted: it is Home&rsquo;s kept-row form; named in the caption'],",
     "    ['Dana sends one helpful thing from elsewhere without joining or administering', '03.3 &rarr; 03.4', 'Works: her gesture, its scope, its arrival attributed', 'Her after-send readback is not drawn', 'Accepted: an authorized Send with owner readback once (T2), not a private Keep'],"),
    ("    ['Sam later wants the photo, not another social task or a forced friend upgrade', '04.3', 'Works: looking needs nothing; keeping asks one confirmation at the boundary', 'The confirmation presumes the invited contact is a phone number; the channel is now fixed on 03.1', 'Dependency stands (guest identity and delivery proposal)'],",
     "    ['Sam later wants the photo, not another social task or a forced friend upgrade', '04.3', 'Works under branch V: the photograph displays through his verified link as long as Maya leaves it; no separate Keep', 'His number was confirmed earlier for the address; the same principal sees the photo', 'Dependency stands (guest identity and delivery proposal)'],"),
    ("    ['Sam understands the invitation, arrives comfortably, leaves on time', '03.2 &rarr; 03.7', 'Works: address after his answer; his nine in his words; the door; nothing to bring', 'How Sam is reached was unstated: he has no account', 'Fixed on 03.1: &ldquo;by text, to the number you typed; typed, not found&rdquo;; ledger updated'],",
     "    ['Sam understands the invitation, arrives comfortably, leaves on time', '03.2 &rarr; 03.4 (provisional, then confirmed) &rarr; 03.7, or 03.6 &rarr; 03.7 variant', 'Works: a provisional answer on the bare link; the code that unlocks the address confirms it; his nine in his words; each branch reaches its own arrival view', '&mdash;', 'Corrected after &sect;15 A and B'],"),
    ("    ['Plans cd2e1f82 &middot; 04 C', 'The recipient preview names the scope in words (dinner only; the address with his answer); the guest page carries an optional &ldquo;anything she should know&rdquo; line (03.1, 03.2)', 'Guest value before adoption; his constraint in his words', 'Seven sentences unchanged', 'Seam 3 dinner-scoped link; guest constraint', 'Adapt'],",
     "    ['Plans cd2e1f82 &middot; 04 C', 'The recipient preview names the scope in words (dinner only; the exact address only after a one-time code to the number the host typed, branch V); a link-holder answer is provisional until that confirmation; the guest page carries an optional &ldquo;anything she should know&rdquo; line under the same rule (03.1, 03.2, 03.4)', 'Guest value before adoption; response distinguished from confirmed recipient identity', 'Seven sentences unchanged', 'Seam 3 occasion-scoped invitation; recipient verification', 'Adapt'],"),
    ("    ['Plans cd2e1f82 &middot; 05 D / 11', 'The adopted change reaches the affected guest as one sentence on his row with his constraint restated (03.6); the arrival frame is a new state on the guest page (03.7)', 'Only the relevant recipient consequence; hospitality', 'Sentences 4 and 5 unchanged', 'Seam 5 per-recipient readback; seam 3 arrival update', 'Adapt / Replace the static resolved push'],",
     "    ['Plans cd2e1f82 &middot; 05 D / 11', 'The adopted change reaches every person at the dinner, tailored: the guest&rsquo;s row restates his constraint (03.6) and his arrival view follows the adopted branch (03.7 variant); the arrival frame is a parameterized state on the guest page', 'Tailored disclosure, not exclusive disclosure; hospitality', 'Sentences 4 and 5 unchanged', 'Seam 5 per-recipient readback; seam 3 arrival update', 'Adapt / Replace the static resolved push'],"),
    ("        ['Refind a shared photo with its author', '04.5', 'Refind reads itinerary blocks and booking offers only; Life carries a media count, no author', 'Engineering'],",
     "        ['Refind a shared photo with its author', '04.5', 'The legacy Refind reader (blocks and booking offers) cannot return a photograph; Life&rsquo;s owner projections and shadow index work are separate paths whose author and media refs are unverified, not absent', 'Engineering, reconciled with the Life owner&rsquo;s intended index path'],"),
    ("    ['Home 42876b8c &middot; quiet days', 'A quiet Home still carries one concrete, current, usable world opening (04.2: Bach at the old church at four; 04.7: the noodle counter till ten) with its context and destination; not a contribution prompt, not a generic discover door', 'Quiet is low coercion, not low value', 'Posture rules unchanged', 'World-content supply for quiet days (Home owner); the copied baseline does not meet this on its own', 'Delta to the Home owner; dependency marked'],",
     "    ['Home 42876b8c &middot; quiet days', 'A quiet Home still carries concrete, current, usable world openings (04.2: Bach at the old church at four; 04.7: the noodle counter till ten) with context and destination; illustrative, not a rule of exactly one; listed information, attributed experience and current conditions kept apart in the copy', 'Quiet is low coercion, not low value', 'Posture rules unchanged', 'World-content supply and its confidence for quiet days (Home and Content owners); the copied baseline does not meet this on its own', 'Delta to the Home owner; dependency marked'],"),
    ("    ['Respond to an invitation', '03.2', 'Nora sees the answer and his nine', 'The link stays his'],", "    ['Respond to an invitation', '03.2 &rarr; 03.4', 'A provisional answer on the bare link; confirmed by the same one-time code that unlocks the address; then Nora sees it as his', 'The link stays his'],"),
    ("        ['The live change', '03.5 (recommended, unadopted) vs 03.6 (adopted, Sam only)', '&ldquo;Seven stands&rdquo; and &ldquo;moved to eight&rdquo; never coexist in one route; 03.6 is entered only from a labelled adopted branch'],",
     "        ['The live change', 'Unchanged seven: 03.5 &rarr; 03.7. Adopted eight: 03.5 (adopt) &rarr; 03.6 &rarr; 03.7 variant (eight)', 'Each route reaches its own arrival view; &ldquo;seven stands&rdquo; and &ldquo;moved to eight&rdquo; never coexist. Adoption reaches Nora, Maya and Sam (tailored); Dana&rsquo;s contribution is unchanged; Sam&rsquo;s silence is not acceptance of eight'],\n        ['The RSVP', '03.2 &rarr; 03.4', 'Provisional on the bare link; confirmed by the code that unlocks the address; if never confirmed, the host never sees a confirmed &ldquo;in&rdquo;'],"),
])
sub('gen_c5.py', [
    ("    ['Sam', 'His link', 'Read', 'What changed and what it means for nine', 'Only the relevant recipient consequence', 'Occasion (guest view)', '&mdash;', 'Answer, or not'],", ""),
])

# ───────────────────────────── gen_se · board 01 rows ─────────────────────────────
sub('gen_se.py', [
    ("    ['B2', 'Sam', 'A link, no app', 'Open', 'The character of the evening, who invited him, seven-thirty, where, nothing to bring, how to answer', 'Sam sees when, where, who; nothing else of Nora&rsquo;s', 'Occasion (guest view)', '&mdash;', 'I&rsquo;m in &middot; Can&rsquo;t make it (no reason asked)'],",
     "    ['B2', 'Sam', 'A link, no app', 'Open, answer', 'The character of the evening, who invited him, seven-thirty, the neighborhood, nothing to bring, how to answer', 'A provisional answer; confirmed by the one-time code that also unlocks the address (branch V)', 'Occasion (guest view)', 'Nora: provisional, then confirmed', 'I&rsquo;m in &middot; Can&rsquo;t make it (no reason asked)'],"),
    ("    ['B4&prime;', 'Sam', 'His link', 'Read', 'BRANCH, adopted: Nora applied eight; one sentence on his row with what it means for nine', 'Only the relevant recipient consequence; his acceptance is not invented', 'Occasion (guest view)', '&mdash;', 'Answer, or not'],",
     "    ['B4&prime;', 'Sam', 'His link', 'Read', 'BRANCH, adopted: Nora applied eight; one sentence on his row with what it means for nine; everyone at the dinner has the new time', 'Tailored to him; his acceptance is not invented', 'Occasion (guest view)', '&mdash;', 'Answer, or not; then the eight arrival (03.7 variant)'],"),
    ("    ['C1&Prime;', 'Sam', 'His link, later', 'Open', 'The same photograph; the proposed verification at the boundary, if any', 'DEPENDENCY outside the phone: identity or delivery; not granted by the expired invitation', 'Contribution (guest view)', '&mdash;', 'Receive without contributing'],",
     "    ['C1&Prime;', 'Sam', 'His link, later', 'Open', 'The same photograph, displayed through his verified link as long as Maya leaves it; no separate Keep', 'Branch V: his number was confirmed for the address; the same principal sees the photo. DEPENDENCY outside the phone', 'Contribution (guest view)', '&mdash;', 'Receive without contributing'],"),
    ("            ('04.3', 'SAM', 'LINK', 'Later: the same photograph through his link; the proposed verification at the boundary, dependency outside the phone', 'Receive without contributing.'),",
     "            ('04.3', 'SAM', 'LINK', 'Later: the same photograph through his verified link, as long as Maya leaves it; no separate Keep', 'Receive without contributing.'),"),
    ("            ('03.7', 'SAM', 'LINK', 'Saturday evening: &ldquo;expected around seven-thirty&rdquo;; find the host; nothing to bring; Dana&rsquo;s dish as a foothold', 'Phone away.'),",
     "            ('03.7', 'SAM', 'LINK', 'Saturday evening: &ldquo;expected around seven-thirty&rdquo; on the unchanged route, or eight on the adopted branch (the same frame, parameterized); find the host; nothing to bring', 'Phone away.'),"),
    ("            ('03.4', 'NORA', 'OCCASION', 'Friday: Dana&rsquo;s tip and photo, Maya&rsquo;s suggestion, Sam&rsquo;s answer and his nine, each under the row with its scope', 'Nothing to do.'),",
     "            ('03.4', 'NORA', 'OCCASION', 'Friday: Dana&rsquo;s tip and photo, Maya&rsquo;s suggestion, Sam&rsquo;s answer (provisional, then confirmed) and his nine, each under the row with its scope', 'Nothing to do.'),"),
    ("STAMP = 'REVISED PER HANDOFF &sect;14 &middot; 2026-09-07'", "STAMP = 'DESIGN ROUND CLOSED PER HANDOFF &sect;15 &middot; 2026-09-07'"),
])
print('patched; misses:', len(MISS)); [print('  MISS', p, o) for p, o in MISS]
