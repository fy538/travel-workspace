"""Apply the handoff §14 revision to the generators."""
import re
MISS=[]
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

# ───────────────────────────── gen_se.py ─────────────────────────────
s0=open('gen_se.py').read()
s0=s0.replace("STAMP = 'CHECKPOINT 1 REVIEWED &middot; REVISED 2026-09-07'", "STAMP = 'REVISED PER HANDOFF &sect;14 &middot; 2026-09-07'")
for st in ["'REVISED &sect;14: a friend shares directly from the object; a non-photo medium; no policy narration inside phones'", "'REVISED &sect;14: the practical choice carries a direct action; neutral language'", "'REVISED &sect;14: another pasta evening restored; the boat folded into the record; the connection is sought, never prompted'"]:
    s0=s0.replace("'DRAWN &middot; Checkpoint 2'", st, 1)
s0=s0.replace("'DRAWN &middot; recommendations PROPOSED'", "'REVISED &sect;14: fair comparisons (same facts, same grants); D2 and D3 reframed'")
s0=s0.replace("'DRAWN &middot; handback in docs/working/social-experience-design-response-2026-09-07.md'", "'REVISED &sect;14: dispositions per the review; deltas corrected'")
open('gen_se.py','w').write(s0)

# ───────────────────────────── gen_c2.py ─────────────────────────────
sub('gen_c2.py', [
    ("    inner += f'<div style=\"padding: 30px 34px 6px 34px; text-align: center;\"><div class=\"fn\">NOTHING KEPT &middot; NOTHING SHARED &middot; THE PHOTO IS STILL ONLY YOURS</div></div>'\n    return phone(inner, 0, active='Chat')", "    return phone(inner, 0, active='Chat')"),
    ("    inner += gut(ctx_chip('THE PRINT ROOM &middot; PRIVATE &middot; MAYA SEES NOTHING') + f'<div style=\"font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;\">The place and its listing are the context. Maya&rsquo;s photo and words are not sent.</div>', top=26)", "    inner += gut(ctx_chip('THE PRINT ROOM &middot; PRIVATE &middot; MAYA SEES NOTHING'), top=26)"),
    ("sig='LISTED HOURS, NOT CHECKED TODAY &middot; THE GALLERY&rsquo;S NOTES &middot; NOTHING OF MAYA&rsquo;S WAS USED'", "sig='FROM THE LISTING AND THE GALLERY&rsquo;S NOTES &middot; HOURS NOT CHECKED TODAY'"),
    ("    inner += gut(door('Back to the Print Room') + src('Returns to the same scroll'), top=22)", "    inner += gut(door('Back to the Print Room'), top=22)"),
    ("    inner += f'<div style=\"padding: 40px 34px 6px 34px; text-align: center;\"><div class=\"fn\">NO VIEWER LIST &middot; NO COUNT &middot; NO USE REPORT &middot; NOBODY IS OWED A REPLY</div></div>'\n    return phone2(inner)", "    return phone2(inner)"),
    ("src('Friends, through Sunday. That is all this page knows.')", "src('Friends, through Sunday.')"),
])
replace_func('gen_c2.py', 'share_draft_phone', '''def share_draft_phone():
    """A friend shares directly from an eligible object: Maya, from the Print Room's place page. No AI prelude, no Occasion, no connection setup."""
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; THE HARBOR PRINT ROOM</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 210, tag="ILLUSTRATION")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;"><span style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">The side room was my favorite. Go on a weekday, it was empty.</span></div>', top=16)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">WHO</div>' + who_pills('Friends').replace('Maya only', 'Nora only') + f'<div style="display: flex; gap: 18px; align-items: baseline; margin-top: 12px;"><span style="font-size: 13px; color: {INK2};">The Print Room, Red Hook &middot; through Sunday</span>{door("Change", MUTE)}</div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 18px;"><span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 12px 22px; font-size: 15px; font-weight: 600;">Send</span>{door("Not now", MUTE)}</div>', top=26)
    return phone2(inner)
''')
replace_func('gen_c2.py', 'friends_scope_phone', '''def collection_card():
    stops = [('The Harbor Print Room', 'the side room; Tue&ndash;Sun 11&ndash;6'), ('The Red Hook pier', 'the harbor and the Statue'), ('The ferry landing', 'the flexible way out')]
    rows = ''.join(f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 7px 0; border-top: 1px solid rgba(27,23,20,0.06);"><span style="{MONO} font-size: 10px; font-weight: 700; color: {GOLDD}; width: 14px;">{i+1}</span><div style="flex: 1;"><div style="font-size: 15px; color: {INK};">{n}</div><div style="font-size: 13px; color: {MUTE};">{d}</div></div></div>' for i, (n, d) in enumerate(stops))
    mapw = f'<div class="hatch" style="height: 96px; border-radius: 10px; display: flex; align-items: flex-end; padding: 8px 10px; box-sizing: border-box;"><span class="fn" style="color: {MUTE};">MAP &middot; THREE STOPS &middot; ILLUSTRATION</span></div>'
    return card(mapw + author_row('P', 'Priya', 'SATURDAY &middot; A SMALL COLLECTION') + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 8px;">Red Hook on foot, three stops. An hour and a half if you don&rsquo;t sit down.</div><div style="margin-top: 10px;">{rows}</div>' + f'<div style="display: flex; gap: 18px; align-items: center;">{door("Reply to Priya")}{door("Open the map")}</div>')

def friends_scope_phone():
    inner = header('NEW YORK', 'From friends') + question_line(ctx='From friends')
    inner += gut(maya_print_room(with_priya=True), top=18)
    inner += sect('Red Hook') + gut(collection_card())
    inner += sect('The market') + gut('<div>' + share_line('P', 'Priya', 'The pigeons at the market have a system. I have watched it for twenty minutes.', 'The greenmarket', last=True) + '</div>')
    inner += sect('Elsewhere') + gut('<div>' + share_line('D', 'Dana', by('Dana', 'sorrento')[2], 'Sorrento, this week', last=True) + '</div>')
    inner += sect('Red Hook, anyway') + gut(place_unit('pier', 'The Red Hook pier', 'Any time &middot; free', 'Faces the harbor and the Statue; the Sunset Park pier is the one for sunset.', last=True))
    inner += gut(pl_ending(['All of New York', 'Everyone, in Life']), top=28)
    return phone2(inner)
''')
sub('gen_c2.py', [
    ("        ('02.2', 'NORA', 'SHARE', share_draft_phone(), ('THURSDAY 7:58 PM', 'THE SHARE, DELIBERATELY', 'WHO, one line, Send', 'THE DRAFT CARRIES THE PHOTO AND HER LINE: NOT THE QUESTION, NOT THE ANSWER, NOT HER ADDRESS'),\n         ('Nora', 'The answered photo, or any eligible photo', 'Share', 'The smallest audience treatment', 'Friends; nothing else of hers', 'Contribution', 'Friends see a photo and a line', 'Sent once; or kept'), ('FIXTURE', 'AUDIENCE IS THE ONLY AFFORDANCE &middot; D1 STARTING POSITION', 'T1 &middot; RECEIPT WITH UNDO NOT SHOWN HERE')),",
     "        ('02.2', 'MAYA', 'PLACES', share_draft_phone(), ('THURSDAY &middot; FROM THE PLACE PAGE', 'AN EXISTING FRIEND SHARES DIRECTLY', 'From the object; one line; who; Send', 'NO AI PRELUDE, NO OCCASION, NO CONNECTION SETUP &middot; THE AUDIENCE IS A DELIBERATE CHOICE PER SHARE'),\n         ('Maya', 'The Print Room&rsquo;s place page', 'Share', 'Her picture and her words reach the people she chose', 'Friends, through Sunday; place precision as declared', 'Contribution', 'Friends see a photo and a line in their scope', 'Sent once; or not'), ('FIXTURE', 'A SEND CROSSES AN AUDIENCE BOUNDARY: T2, CARRIED BY THE ONE CLEAR SEND', 'D1 &middot; D6: PER-SHARE AUDIENCE')),"),
    ("('THURSDAY &middot; FROM FRIENDS', 'PLACES IS WORTH OPENING', 'Maya&rsquo;s photo; Priya; Dana elsewhere; Red Hook anyway', 'COPY OF R1 WITH THE LEDGER&rsquo;S CAST &middot; NOTHING IS MARKED VIEWED &middot; ENJOY IT AND LEAVE')",
     "('THURSDAY &middot; FROM FRIENDS', 'PLACES IS WORTH OPENING', 'Maya&rsquo;s photo; Priya&rsquo;s three-stop map; the pigeons; Dana elsewhere; Red Hook anyway', 'COPY OF R1 WITH THE LEDGER&rsquo;S CAST &middot; RICH SUPPLY, ONE NON-PHOTO MEDIUM &middot; ENJOY IT AND LEAVE')"),
    ("        ('THE PRIVATE INPUT FIRST', N('02.1 is the &sect;8.1 answer, with nothing kept and nothing offered. 02.2 is a separate gesture reachable from any eligible photo; the draft cannot carry the question, the answer or the address.')),",
     "        ('SHARING WITHOUT A PRELUDE', N('02.2 is a friend sharing from the object itself: Maya, from the Print Room&rsquo;s page, one line, who, Send. No Chat first, no Occasion, no connection to accept. The audience is chosen per share; a send crosses an audience boundary and the one clear Send carries it. 02.1 stays as the private answer that keeps nothing.')),"),
    ("'Seven slots: the private Ask and the deliberate share; the friends scope worth opening and the place opened with its three registers kept apart; Reply and Ask from the same photograph; and the sender&rsquo;s quiet return. Every phone is the ledger&rsquo;s fixture; every world fact is in the unverified register.'",
     "'Seven slots, revised per &sect;14: the private answer that keeps nothing; an existing friend sharing directly from an eligible object; a friends scope with rich supply and one non-photo medium; the place opened with its three registers kept apart; Reply and Ask from the same photograph; the sender&rsquo;s quiet return. Policy stays outside the phones.'"),
])

# ───────────────────────────── gen_c3.py ─────────────────────────────
sub('gen_c3.py', [
    ("<div style=\"font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;\">To the dinner&rsquo;s people: Nora, Maya and Sam. Not the address, not their answers. Nothing else of yours.</div>", "<div style=\"font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;\">To Nora, Maya and Sam.</div>"),
    ("               + f'<div style=\"{SERIF} font-style: italic; font-size: 15px; line-height: 21px; color: {INK}; margin-top: 10px;\">Say which, or leave it: seven stands.</div>'\n               + meta('SAM&rsquo;S NINE, IN HIS WORDS &middot; NOBODY&rsquo;S AGREEMENT IS ASSUMED &middot; ONE ASK ON THIS PAGE', 8))",
     "               + f'<div style=\"display: flex; align-items: center; gap: 12px; margin-top: 14px;\">{pill(\"Keep seven\", False)}{pill(\"Move to eight\", False)}</div>'\n               + f'<div style=\"font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 10px;\">Or leave it: seven stands.</div>')"),
    ("    inner += gut('<div>' + row('Same place &middot; <span style=\"color: #6E6862;\">come at eight, or seven-thirty as planned; the door&rsquo;s open</span>', mark='solid', color=GOLD)\n                 + row('Your nine still stands &middot; <span style=\"color: #6E6862;\">Nora knows; she moved it anyway</span>', mark='hollow', last=True) + '</div>', top=16)",
     "    inner += gut('<div>' + row('Same place &middot; <span style=\"color: #6E6862;\">come at eight, or seven-thirty as planned</span>', mark='solid', color=GOLD)\n                 + row('Your nine still stands', mark='hollow', last=True) + '</div>', top=16)"),
    ("    inner += gut(door('Running late? Say so') + src('One line to Nora. Nothing here follows you.'), top=22)", "    inner += gut(door('Running late? Say so') + src('One line to Nora.'), top=22)"),
    ("'The change: Maya proposes eight; Sam must leave by nine; one prepared alternative with its tradeoff', 'One ask on the page; the rest of Home keeps its ordinary value'", "'The change: Maya proposes eight; Sam must leave by nine; the alternative with its cost and a direct action', 'One ask on the page; the rest of Home keeps its ordinary value'"),
    ("('SATURDAY 1:44 PM &middot; FULL SCROLL', 'THE CHANGE, AND THE AFTERNOON', 'Maya&rsquo;s eight with its cost; the &sect;8.2 afternoon; the rest of Home intact', 'COPY OF R11 (HOME 02 SUNDAY) WITH THE SOCIAL UNITS SUBSTITUTED &middot; ONE ASK &middot; SEVEN STANDS UNTIL SHE SAYS')",
     "('SATURDAY 1:44 PM &middot; FULL SCROLL', 'THE CHANGE, AND THE AFTERNOON', 'Maya&rsquo;s eight with its cost and a direct action; the &sect;8.2 afternoon; the rest of Home intact', 'COPY OF R11 (HOME 02 SUNDAY) WITH THE SOCIAL UNITS SUBSTITUTED &middot; ONE ASK WITH A USABLE ACTION &middot; SEVEN STANDS IF SHE LEAVES IT')"),
    ("        ('THE CHANGE, TWO BRANCHES', N('03.5 is the recommended route: Maya&rsquo;s eight arrives as one ask with the tradeoff stated and no button; seven stands in every view until Nora says otherwise.", "        ('THE CHANGE, TWO BRANCHES', N('03.5 is the recommended route: Maya&rsquo;s eight arrives as one ask with the tradeoff stated and two direct actions; leaving it is the unadopted ending and seven stands in every view."),
])

# ───────────────────────────── gen_c4.py ─────────────────────────────
sub('gen_c4.py', [
    ("    inner += f'<div style=\"padding: 34px 34px 6px 34px; text-align: center;\"><div class=\"fn\">A DELIBERATE GESTURE &middot; NOT A POST &middot; NOT AN UPLOAD TO AN ALBUM</div></div>'\n    return phone(inner, 0, active='Life')", "    return phone(inner, 0, active='Life')"),
    ("    inner += sect('Addressed to you') + gut(card(f'<div style=\"border-radius: 12px; overflow: hidden; margin-bottom: 10px;\">{standin(210, \"THE TABLE &middot; SATURDAY 7:50 PM &middot; STAND-IN\")}</div>'", "    inner += sect('From last night') + gut(card(f'<div style=\"border-radius: 12px; overflow: hidden; margin-bottom: 10px;\">{standin(210, \"THE TABLE &middot; SATURDAY 7:50 PM &middot; STAND-IN\")}</div>'"),
    ("<div class=\"fn\" style=\"margin-top: 6px; color: {ANCHOR};\">LOOKING NEEDS NOTHING &middot; KEEPING MAY NEED THIS &middot; NO ACCOUNT, NO PROFILE</div>", "<div class=\"fn\" style=\"margin-top: 6px; color: {ANCHOR};\">TO KEEP IT PAST TODAY</div>"),
    ("    inner += bar('WHERE IT LIVES') + gut('<div>' + entry('dining', 'Saturday, Sep 19', 'Time') + entry('note', 'Maya, Sam, Dana', 'People') + entry('photo', 'Two photographs', 'the contact sheet', last=True) + '</div>')",
     "    inner += bar('WHERE IT LIVES') + gut('<div>' + entry('dining', 'Saturday, Sep 19', 'Time') + entry('note', 'Maya, Sam, Dana', 'People') + entry('photo', 'Two photographs', 'the contact sheet', last=True) + '</div>')\n    inner += bar('PROMISED &middot; THE COUPLE FROM THE BOAT') + gut('<div>' + entry('photo', 'The photo at the rail', 'to the address they gave you', last=True) + '</div>' + door('Send it, once') + src('One email, one photo, your words.'))"),
    ("    inner += gut(src('Nothing was saved, promoted or inferred by searching.'), top=22)\n", ""),
    ("    inner += gut(src('Nothing paraphrases the note. Nothing built on it remains. The dinner, her photo and her suggestion were never hers to take with it.'), top=22)", "    inner += gut(src('The dinner, her photo and her suggestion stand.'), top=22)"),
])
replace_func('gen_c4.py', 'sam_choice', '''def sam_choice():
    """Sought, not prompted: on his link's record of the evening, Nora's line offers 'Stay in touch' when he looks for it."""
    inner = guestbar('SATURDAY, AT NORA&rsquo;S &middot; YOUR LINK')
    inner += gut(f'<div style="border-radius: 12px; overflow: hidden;">{standin(120, "THE TABLE &middot; STAND-IN")}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">Maya&rsquo;s photograph, and what Nora wrote.</div>', top=14)
    inner += gut('<div>' + row('Nora &middot; <span style="color: #6E6862;">your host</span>', mark='av:N', last=True) + '</div>' + door('Stay in touch'), top=18)
    inner += gut(f'<div style="background: {CARD}; border-radius: 18px 18px 0 0; box-shadow: 0 -8px 24px rgba(27,23,20,0.14); padding: 14px 22px 22px 22px;"><div style="width: 36px; height: 4px; border-radius: 2px; background: rgba(27,23,20,0.15); margin: 0 auto 14px auto;"></div>'
                 + title('Stay in touch with Nora?', 19, 24, 600) + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">If you both say yes: send each other things, a photo, a place, a recipe, a line; and invite each other without a new link. Nothing else opens.</div>'
                 + f'<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px;">{pill("Yes, if she does")}{pill("Leave it", False)}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">Leaving it is fine. Tonight&rsquo;s photo stays yours either way.</div></div>', top=22)
    return linkframe(inner)
''')
replace_func('gen_c4.py', 'nora_choice', '''def nora_choice():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '6:30 PM')
    inner += orientation('Clear evening. The dentist is done.', 'One thing from Sam.')
    inner += sect('In motion') + gut('<div>' + arow('Sam &middot; would stay in touch, if you would &middot; <span style="color: #6E6862;">things between you, and inviting without a link</span>', avatars=['S']) + row('Dentist &middot; done &middot; <span style="color: #6E6862;">next in six months</span>', mark='solid', color=GOLD, last=True) + '</div>' + f'<div style="display: flex; gap: 18px; align-items: center; padding-top: 10px;">{door("Yes")}{door("Leave it", MUTE)}</div>')
    inner += sect('Worth knowing') + gut(u2('The pier at low water is the shaded side after two', 'The warehouses take the sun off the water walk by 2:30; the return by land is the warm way.', meta_t='TIDE TABLE + THE SUN&rsquo;S ANGLE &middot; FIXTURE'))
    inner += gut(door('Everything in Life') + meta('LIFE', 0), top=32)
    inner += week_ending([('TUE', dm('solid', INK), 'today', INK), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE)], 'A quiet week.')
    return phone(inner, 0)
''')
replace_func('gen_c4.py', 'boat_send', '''def another_evening():
    """The existing-relationship continuation: authorized prior material reduces repeated explanation; new invitations, new answers."""
    inner = chat_head('TWO WEEKS LATER')
    inner += gut(ctx_chip('LAST TIME &middot; SEP 19 &middot; AT YOURS', dot=GOLD), top=26)
    inner += gut(bubble('dinner with maya and sam again? saturday the 3rd'), top=22)
    inner += gut(answer('Same shape as last time? Seven at yours, Sam from seven-thirty and out by nine, Dana&rsquo;s rag&ugrave;. Maya and Sam get fresh invitations for Saturday Oct 3; nothing carries over unless you say so.', sig='FROM SEP 19&rsquo;S RECORD, YOURS &middot; THEIR ANSWERS THEN DO NOT COUNT NOW'), top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 14px;">{pill("Send them")}{pill("Change something", False)}</div>', top=20)
    inner += gut(composer('Say it'), top=22)
    return phone(inner, 0, active='Chat')

def before_after():
    return (f'<div style="display: flex; gap: 12px; margin-top: 10px;">'
            f'<div style="flex: 1; border: 1px dashed rgba(27,23,20,0.25); border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">BEFORE</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">&ldquo;pasta night sat oct 3 at 7, maya + sam, sam can come 7:30 and needs to leave by 9, nothing to bring, at mine, court st 3f&rdquo;</div></div>'
            f'<div style="flex: 1; border: 1px solid rgba(27,23,20,0.10); background: {CARD}; border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">AFTER</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">&ldquo;dinner with maya and sam again? saturday the 3rd&rdquo;</div></div></div>')
''')
sub('gen_c4.py', [
    ("        ('04.2', 'NORA', 'HOME', home_sunday(), ('SUNDAY 10:20 AM', 'IT ARRIVES ONCE, AS THE IMAGE', 'Addressed to you; the rest of Home is a quiet Sunday', 'A VIEW OF ONE SOURCE, NOT AN UPLOAD &middot; ALSO IN LIFE UNDER LAST NIGHT &middot; NO RETROSPECTIVE QUESTION'),",
     "        ('04.2', 'NORA', 'HOME', home_sunday(), ('SUNDAY 10:20 AM', 'IT ARRIVES ONCE, AS THE IMAGE', 'From last night; the rest of Home is a quiet Sunday', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION (TWO-ITEM RULE) &middot; A VIEW OF ONE SOURCE &middot; ALSO IN LIFE'),"),
    ("        ('04.6', 'SAM', 'LINK', sam_choice(), ('AFTER THE PHOTO &middot; OPTIONAL', 'STAY IN TOUCH?', 'The exact capability named; leaving it is complete', 'C5 &middot; SEPARATE FROM RSVP, THE PHOTO AND ANY ACCOUNT &middot; NORA IS NOT TOLD IF HE LEAVES IT'),\n         ('Sam', 'His link, after the photo', 'Choose', 'A named capability, nothing else', 'Nobody is told of a non-answer', 'Relationship (proposal)', 'Nora sees a request, or nothing', 'Bound, or connected'), ('PROPOSED &middot; C5 DEFAULT CAPABILITY: DIRECT PHOTO OR LINE + INVITE WITHOUT A LINK', 'DEPENDENCY &middot; PAIR CIRCLE AS CONTAINER', 'FIXTURE')),",
     "        ('04.6', 'SAM', 'LINK', sam_choice(), ('LATER &middot; HIS LINK &middot; SOUGHT, NOT PROMPTED', 'STAY IN TOUCH?', 'He looks for it under Nora&rsquo;s name; the capability is named; leaving it is fine', 'C5 &middot; NEVER APPENDED AFTER A PHOTO &middot; SEPARATE FROM RSVP, THE PHOTO AND ANY ACCOUNT'),\n         ('Sam', 'His link&rsquo;s record of the evening', 'Seek, then choose', 'A named capability: things between them, inviting without a link', 'Nobody is told of a non-answer', 'Relationship (proposal)', 'Nora sees a request, or nothing', 'Bound, or connected'), ('PROPOSED &middot; C5: ELIGIBLE THINGS BETWEEN TWO PEOPLE + INVITING WITHOUT A LINK', 'DEPENDENCY &middot; A NON-ACCOUNT GUEST NEEDS A VERIFIED PRINCIPAL', 'FIXTURE')),"),
    ("        ('04.7', 'NORA', 'HOME', nora_choice(), ('TUESDAY 6:30 PM', 'HER SIDE OF THE SAME CHOICE', 'One line on Home; yes, or leave it', 'ACCEPT ENABLES THE NAMED CAPABILITY ONLY &middot; IGNORED, DECLINED, ACCEPTED ARE ALL COMPLETE &middot; NO ALL-ACCESS AUDIENCE'),",
     "        ('04.7', 'NORA', 'HOME', nora_choice(), ('TUESDAY 6:30 PM', 'HER SIDE OF THE SAME CHOICE', 'One row in motion; yes, or leave it; the rest of Home intact', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION &middot; ACCEPT ENABLES THE NAMED CAPABILITY ONLY &middot; IGNORED, DECLINED, ACCEPTED ARE ALL COMPLETE'),"),
    ("        ('04.8', 'NORA', 'LIFE', boat_send(), ('LATER &middot; THE BOAT COUPLE', 'THE PROMISED PHOTO, THROUGH THE EMAIL THEY GAVE', 'One send; no friend upgrade', 'THE EDGE CASE, NOT THE CONTINUITY DECISION &middot; NO MATCH LOOKED FOR &middot; WITHOUT AN ADDRESS THE MEMORY STAYS'),\n         ('Nora', 'Life &middot; the boat couple', 'Send once', 'The promised photo through the supplied email', 'One send', 'Contribution', 'An email with one photo', 'Edge case; no-path branch noted'), ('FIXTURE &middot; BRANCH A LEADS', 'DEPENDENCY &middot; EMAIL SEND FROM LIFE', 'C3')),",
     "        ('04.8', 'NORA', 'CHAT', another_evening(), ('TWO WEEKS LATER', 'ANOTHER PASTA EVENING', 'The last one&rsquo;s shape, reused with consent; fresh invitations', 'AUTHORIZED PRIOR MATERIAL REDUCES REPEATED EXPLANATION &middot; NEW OCCASION, NEW CHOICES &middot; NOTHING INHERITED'),\n         ('Nora', 'Chat', 'Say it', 'The last dinner&rsquo;s shape offered back; one Send', 'Maya and Sam get fresh invitations', 'Occasion (new)', 'Two fresh invitations', 'Send; or change something'), ('R8 F2 &middot; REACTIVATION BY REFERENCE', 'BEFORE / AFTER SPECIMEN BELOW', 'THE BOAT COUPLE ARE NOW A ROW ON 04.4')),"),
    ("        ('04.9', 'NORA', 'LIFE', withdrawal(), ('SUNDAY &middot; MAYA&rsquo;S PAGE', 'WITHDRAWAL', 'The Paris note is gone; everything else as it was', 'NO PARAPHRASE REMAINS &middot; A1, B2B, C1 AND THE DINNER STAND &middot; NO NEW CONTACT, NOTHING OWED'),",
     "        ('04.9', 'NORA', 'LIFE', withdrawal(), ('SUNDAY &middot; MAYA&rsquo;S PAGE', 'WITHDRAWAL', 'The Paris note is gone; everything else as it was', 'DEPENDENTS GONE, INDEPENDENT ITEMS STANDING &middot; NO NEW CONTACT'),"),
    ("    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2]",
     "    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s) + (before_after() if n == '04.8' else '')) for n, role, root, ph, c, r, s in P2]"),
    ("        ('THE CHOICE, BOTH SIDES', N('04.6 and 04.7 name exactly what a connection would enable: a photo or a line between them, and inviting without a new link. Nothing else opens. Leaving it is complete on both sides and nobody is told of a non-answer. This is the C5 recommendation; the pair circle is its likely container (capability map, seam 6).')),\n        ('THE BOAT COUPLE', N('04.8 is the edge case the review asked to keep small: the email they gave, one send, nothing of Vesper&rsquo;s attached. Branch b, no path, is the same page without the card.')),",
     "        ('THE CHOICE, BOTH SIDES', N('04.6 is sought: Sam looks under Nora&rsquo;s name on his link&rsquo;s record of the evening; nothing is appended after the photograph. The sheet names what a connection enables: things between them (a photo, a place, a recipe, a line) and inviting without a new link. 04.7 is one row in Nora&rsquo;s In motion. Leaving it is fine on both sides. A non-account guest needs a verified principal for this (guest proposal).')),\n        ('ANOTHER EVENING', N('04.8 restores the existing-relationship continuation: the last dinner&rsquo;s shape comes back from Nora&rsquo;s own record with one line, Maya and Sam get fresh invitations, nothing is inherited. The before/after strip shows the retyping it removes. The boat couple are a compact row on 04.4.')),"),
    ("'Nine slots: Maya&rsquo;s gesture; the photograph arriving for Nora and, later, for Sam; the evening as one record and one retrieval; the ongoing-connection choice from both sides; the boat couple; and withdrawal.'",
     "'Nine slots, revised per &sect;14: Maya&rsquo;s gesture; the photograph arriving for Nora and, later, for Sam; the evening as one record (with the promised boat photo as a row) and one retrieval; the connection sought from Sam&rsquo;s side and answered on Nora&rsquo;s; another pasta evening by reference; and withdrawal.'"),
])
print('patched; misses:', len(MISS)); [print('  MISS', p, o) for p, o in MISS]
