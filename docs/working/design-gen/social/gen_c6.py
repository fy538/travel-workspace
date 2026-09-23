"""Board 08 · Continuations (September 8 consolidation): non-spatial receiving, and where a guest returns after a connection. Five slots beyond the 24. Fixture; PROPOSED."""
import os, sys
from gen_c2 import *
from gen_c3 import linkframe, guestbar, pill, person_row, contribution
from gen_c4 import life_head, bar, entry
from gen_c2 import HP
sys.path.insert(0, HP)
from gen_generous import ending as week_ending, arow
from gen_generous3 import u2
from kit import anchor_row, orientation, row, dm
from gen_seam import chip

WEEK_THU = [('THU', dm('solid', INK), 'today', INK), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE)]
LINE = 'Second try. Thinking of Saturday, if anyone&rsquo;s around.'
LINE2 = 'Third try. It held. Dana&rsquo;s twenty minutes.'

# ───────────────────────────── 08.1 · Maya's Home · it arrives once, without a place ─────────────────────────────
def maya_home_thu():
    inner = anchor_row('NEW YORK &middot; THURSDAY', '8:12 PM')
    inner += orientation('Clear evening. Nothing needs you.', 'Nora shared her pasta.')
    inner += sect('From Nora') + gut(card(f'<div style="border-radius: 12px; overflow: hidden; margin-bottom: 10px;">{standin(200, "THE PASTA &middot; HER PHONE, THURSDAY 7:40 PM &middot; ASSET NOT SOURCED")}</div>' + author_row('N', 'Nora', 'TONIGHT &middot; TO FRIENDS &middot; THROUGH SUNDAY')
                                             + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 8px;">{LINE}</div>'
                                             + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 6px;">{door("Open")}{door("Reply", MUTE)}</div>' + meta('HERS &middot; A LINE, NOT AN INVITATION &middot; ALSO UNDER PEOPLE &rarr; NORA', 8)))
    inner += sect('In motion') + gut('<div>' + row('The Print Room &middot; your share &middot; <span style="color: #6E6862;">to friends, through Sunday</span>', mark='solid', color=GOLD) + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True) + '</div>')
    inner += sect('Worth knowing') + gut(u2('The pier at low water is the shaded side after two', 'The warehouses take the sun off the water walk by 2:30; the return by land is the warm way.', meta_t='TIDE TABLE + THE SUN&rsquo;S ANGLE &middot; FIXTURE'))
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("photo", "The pasta, from Nora", "", serif=True)}</div>' + meta('LIFE &middot; PEOPLE &rarr; NORA', 8), top=32)
    inner += week_ending(WEEK_THU, 'A quiet week. Tuesday, the dentist.')
    return phone(inner, 0)

# ───────────────────────────── 08.2 · the original, opened ─────────────────────────────
def pasta_opened():
    inner = header('Nora', 'Thursday &middot; to friends &middot; through Sunday', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{standin(240, "THE PASTA &middot; HER PHONE, THURSDAY 7:40 PM &middot; ASSET NOT SOURCED")}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{LINE}</div>', top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.14); border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {GHOST}; flex: 1;">Reply to Nora</span></div>', top=18)
    inner += gut(f'<div style="display: flex; gap: 22px; align-items: center;">{door("Keep this photograph")}</div>' + src('A copy to reread, until she takes it back.'), top=16)
    inner += sect('Where it lives') + gut('<div>' + entry('note', 'Nora', 'People') + entry('dining', 'Thursday, Sep 17', 'Time', last=True) + '</div>' + src('Hers &middot; to friends &middot; through Sunday'))
    inner += gut(door('Ask about this') + src('Asks Vesper, not Nora'), top=16)
    return phone2(inner, active='Home')

# ───────────────────────────── 08.3 · Life · People · Nora: the pull route ─────────────────────────────
def life_people_nora():
    inner = life_head('LIFE &middot; PEOPLE', 'LATER')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Nora</div><div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 6px;">Friend &middot; since 2019 &middot; New York</div>', top=14)
    inner += bar('SHARED WITH YOU &middot; FINDABLE WHILE SHE SHARES IT') + gut('<div>' + entry('photo', 'The pasta, second try', 'Thursday &middot; to friends &middot; through Sunday') + entry('dining', 'Pasta trial night, at hers', 'Saturday Sep 19 &middot; the dinner you were at', last=True) + '</div>')
    inner += bar('KEPT FROM NORA &middot; YOUR COPY, UNTIL SHE TAKES IT BACK') + gut('<div>' + entry('photo', 'The pasta, second try', 'your copy, until she takes it back', last=True) + '</div>')
    inner += bar('YOURS') + gut('<div>' + entry('photo', 'The Print Room', 'Thursday &middot; to friends') + entry('photo', 'The table', 'Saturday &middot; to Nora and Sam', last=True) + '</div>')
    inner += bar('HELD IN COMMON') + gut('<div>' + entry('note', 'Two evenings', 'this year', last=True) + '</div>')
    inner += gut(door('Everything from Nora'), top=22)
    return phone(inner, 0, active='Life')

# ───────────────────────────── 08.4 · Nora shares to Sam, without a link ─────────────────────────────
def nora_share_sam():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; THE SAUCE, THIRD TRY</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{standin(210, "THE SAUCE &middot; SUNDAY SEP 27 &middot; STAND-IN")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;"><span style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">{LINE2}</span></div>', top=16)
    sel = f'<span style="border: 1.5px solid {INK}; background: {INK}; color: {CARD}; border-radius: 999px; padding: 7px 14px; font-size: 14px;">Maya + Sam</span>'
    oth = ''.join(f'<span style="border: 1px solid rgba(27,23,20,0.18); color: {INK2}; border-radius: 999px; padding: 7px 14px; font-size: 14px;">{t}</span>' for t in ('Friends', 'Just Maya'))
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">WHO</div><div style="display: flex; gap: 8px; flex-wrap: wrap;">{sel}{oth}</div>'
                 + f'<div style="display: flex; gap: 18px; align-items: baseline; margin-top: 12px;"><span style="font-size: 13px; color: {INK2};">Sam &middot; by text, the number he confirmed &middot; through next Sunday</span>{door("Change", MUTE)}</div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 18px;"><span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 12px 22px; font-size: 15px; font-weight: 600;">Send</span>{door("Not now", MUTE)}</div>', top=26)
    return phone2(inner, active='Life')

# ───────────────────────────── 08.5 · Sam returns: the same link, now "From Nora" ─────────────────────────────
def sam_return():
    inner = guestbar('FROM NORA &middot; SUNDAY SEP 27 &middot; YOUR LINK &middot; VERIFIED')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Nora shared something.</div>', top=14)
    inner += gut(f'<div style="border-radius: 12px; overflow: hidden;">{standin(200, "THE SAUCE &middot; STAND-IN")}</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 10px;">&ldquo;{LINE2}&rdquo;</div><div class="fn" style="margin-top: 6px; color: {ANCHOR};">NORA &middot; TO YOU AND MAYA &middot; THROUGH NEXT SUNDAY &middot; HERS TO TAKE BACK</div>', top=18)
    inner += gut(door('Write back to Nora') + src('One line. Nothing else opens.'), top=18)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">ALSO FROM NORA</div><div>' + row('The table, Sep 19 &middot; <span style="color: #6E6862;">Maya&rsquo;s photograph, as long as she leaves it</span>', mark='hollow')
                 + row('Pasta trial night &middot; <span style="color: #6E6862;">Saturday Sep 19, at hers; you were there</span>', mark='hollow', last=True) + '</div>', top=22)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">YOUR END</div><div style="display: flex; gap: 22px; align-items: center;">{door("Fewer of these", MUTE)}{door("Stop", MUTE)}</div>' + src('Neither tells her why. Neither changes what you were part of.'), top=22)
    return linkframe(inner)

# ───────────────────────────── the board ─────────────────────────────
def board08():
    P1 = [
        ('08.1', 'MAYA', 'HOME', maya_home_thu(), ('THURSDAY 8:12 PM', 'IT ARRIVES ONCE, WITHOUT A PLACE', 'Nora&rsquo;s pasta and a line, to friends; no map, no pin, no occasion; her week unchanged', 'REUSES 05 D1-A AS THE SENDER STATE &middot; ONE ITEM, SO NO SECTION &middot; AN OPENING IS NOT THE RECIPIENT&rsquo;S AGENDA: NOTHING ON HER WEEK &middot; PLACEMENT IS A NAMED PROPOSAL (RIGHT)'),
         ('Maya', 'Home, Thursday', 'Open', 'Nora&rsquo;s photograph and line, without a place', 'To friends; nothing kept by looking', 'Contribution / Home', '&mdash;', 'Enjoy it and leave'), ('PROPOSED &middot; THE ADDRESSED REGION FOR A SHARE WHOSE AUDIENCE INCLUDES YOU', 'HOME SOCIAL SPLIT &middot; RULED &middot; NOT BROADENED SILENTLY', 'FIXTURE')),
        ('08.2', 'MAYA', 'LIFE', pasta_opened(), ('THE PASTA, OPENED', 'THE EXACT SOURCE, AND THE ONE OPTIONAL KEEP', 'Her photograph, her line, who, until when; Reply to her; Ask privately; keep a copy if you want one', 'WORDING AGREED WITH LIFE 07.7 / 07.8 &middot; OPENING KEEPS NOTHING; IT STAYS FINDABLE WHILE SHE SHARES IT; A COPY IS YOURS TO REREAD UNTIL SHE TAKES IT BACK &middot; SHARE EXPIRY AND HER TAKING IT BACK ARE DIFFERENT CONDITIONS, AND THE COPY SURVIVES ONLY THE FIRST &middot; A KEPT PLACE IS YOURS; KEEPING A PLACE DOES NOT KEEP HER WORDS (ENTITY 12.4) &middot; HOME-ORIGIN STACK PRESERVED &middot; THE SOURCE AGREEMENT BEHIND THE COPY IS PROPOSED, NOT ADOPTED'),
         ('Maya', 'The share', 'Open', 'Her line and the photograph, exactly; optionally a private copy', 'Same; Reply reaches Nora only; a Keep is not disclosed to her', 'Life (original) / Contribution', 'Nora, if she replies', 'Back to Home, same scroll'), ('COPY OF R4&rsquo;S GRAMMAR', '02.5 / 02.6 TREATMENT REUSED &middot; ENTITY 12.4&rsquo;S THREE EFFECTS, NOT ITS AUTOMATIC RECEIPT', 'KEEP CONTINUATION PROPOSED')),
        ('08.3', 'MAYA', 'LIFE', life_people_nora(), ('LATER &middot; LIFE &middot; PEOPLE', 'THE PULL ROUTE, AND THE ONE DISTINCTION', 'Findable while she shares it; your copy until she takes it back; yours; held in common', 'COPY OF R3&rsquo;S GRAMMAR &middot; LIFE 04&rsquo;S &ldquo;YOURS, AND WHAT OTHERS SHARED WITH YOU&rdquo; &middot; FINDABLE-WHILE-SHARED AND DELIBERATELY KEPT ARE TWO ROWS, NOT ONE &middot; NEITHER OPENING AN ORIGINAL NOR KEEPING A PLACE ESTABLISHES RETENTION &middot; NO SOCIAL TAB, NO FEED'),
         ('Maya', 'Life &middot; People &middot; Nora', 'Open', 'What Nora shared with her, while it lasts; what she shared with Nora', 'Attributed; each still its author&rsquo;s; nothing kept by refinding', 'Life', '&mdash;', 'Open, or leave'), ('LIFE SEQUENCES &middot; RULED', 'REFIND OVER A PHOTO IS A DEPENDENCY (SEAM 7)', 'FIXTURE')),
    ]
    P2 = [
        ('08.4', 'NORA', 'LIFE', nora_share_sam(), ('SUNDAY SEP 27 &middot; 6:40 PM', 'A THING FOR SAM, WITHOUT A LINK', 'From her own photograph in Life: one line; Maya and Sam; Send', 'WHAT CONNECTION ENABLED, AND ALL IT ENABLED &middot; SAM BY TEXT, NO APP &middot; THE AUDIENCE STILL CHOSEN PER SHARE'),
         ('Nora', 'Her photograph, Sunday', 'Share', 'One thing to two people', 'Maya; Sam by text; through next Sunday', 'Contribution', 'Maya on Home; Sam on his link page', 'Sent once; or not'), ('C5 &middot; PROPOSED', 'T2 &middot; THE ONE CLEAR SEND', 'FIXTURE')),
        ('08.5', 'SAM', 'LINK', sam_return(), ('SUNDAY 6:52 PM &middot; HIS LINK &middot; VERIFIED', 'WHERE HE RETURNS', 'The same link, now &ldquo;From Nora&rdquo;: the new thing, what he already had, and his end of it', 'NO ACCOUNT, NO APP &middot; THE VERIFIED NUMBER IS THE PRINCIPAL (BRANCH V) &middot; FEWER AND STOP ARE HIS ALONE &middot; ENJOY IT AND LEAVE'),
         ('Sam', 'A text; his link', 'Open', 'Something new from Nora; what he already had', 'Nora&rsquo;s audience choice; his number as principal', 'Relationship (proposal) / Contribution (guest view)', '&mdash;', 'Enjoy it and leave; or fewer; or stop'), ('C5 &middot; PROPOSED &middot; GUEST PROPOSAL &sect;3', 'MUTE, STOP, BLOCK, REPORT ARE DISTINCT; NONE CHANGES WHO ATTENDED', 'FIXTURE')),
    ]
    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]
    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2]
    prop = notecol('Placement, proposed', [
        ('THE EXTENSION, EXACTLY', N('The September 5 amendment already gives a casual share with no Place two homes: a Status doorway on Home while featured, and Life &middot; People after. 08 extends that permitted treatment in one step: the fuller original itself arrives once in Home&rsquo;s addressed region when the share&rsquo;s audience includes you (Friends eligibility as the arrival condition), under the same two-item rule 04.2 uses. That is the whole delta. It is not evidence that nonspatial social material had no home, not a new feed, not a social root, and no root is reopened. Place-bound shares still open in Places, and nothing is forced onto a map.')),
        ('THE ORIGIN STACK', N('08.2 is a Life-owned source opened from Home, so it keeps its Home-origin stack: the tab bar stays on Home and Back restores Home&rsquo;s scroll. It becomes a Life page only if the person deliberately crosses roots, which 08.3 is. The alternative, Places &middot; From friends without a pin, is fair for a person who lives in Places, but it asks a photograph of pasta to stand near a map.')),
        ('THE PULL ROUTE', N('Life &middot; People &middot; Nora holds everything between the two of them, attributed both ways, and Life search finds it by its words (04.5&rsquo;s grammar). Nothing is written by looking. This is the recommended durable route; Home is the arrival, not the archive.')),
        ('WHAT THIS DOES NOT DECIDE', N('The Friends audience remains the friends-audience proposal; this board assumes it as a fixture. The retention agreement behind &ldquo;Keep this photograph&rdquo; is proposed, not adopted, and no grant is implemented here. The Home review (September 8, &ldquo;with people&rdquo; kinds) keeps the addressed region for contributions addressed to the person and relocates casual status to Places by default; whether a friends-audience original arrives as addressed material or as the featured-Status doorway is Home&rsquo;s call, and the delta above is written so either answer is a small change.')),
        ('THE ASSETS, AND THE GAP', N('Every photographic plate on these boards is a labelled stand-in, and the frames therefore argue that a friend&rsquo;s original is the whole benefit while showing nothing worth looking at. The four that matter are named on their plates: the pasta (Nora&rsquo;s phone, Thursday 7:40 pm), the table (Maya&rsquo;s phone, Saturday 8:25 pm), the Print Room (Maya&rsquo;s own visit) and Dana&rsquo;s rag&ugrave; (Sorrento, Wednesday). The Print Room alone has an authored plate, the Places project&rsquo;s own illustration; the rest read &ldquo;asset not sourced&rdquo;. Ordinary rights-cleared photographs, unpolished and unstaged, are still needed and are their own scope: this pass contacts nobody and imports no private library. The authored words beside each plate are real fixture material and carry what they can meanwhile.')),
        ('WHAT IS NOT INHERITED', N('Entity 04.08&rsquo;s automatic receipt (&ldquo;used in tonight &middot; she can see this use&rdquo;) stays out of this route: private use does not acquire a visibility consequence by being copied from a reference, and no reaction or sender consumption score exists anywhere here. Entity 12.4&rsquo;s three named effects are inherited; its useful / keep / send set does not replace human Reply, which stays in the action set beside the private Ask.')),
    ], w=430)
    notes = notecol('What board 08 shows', [
        ('SOMETHING WITHOUT A PLACE', N('08.1 to 08.3 take board 05&rsquo;s D1-A (Nora&rsquo;s pasta and a line, to friends, no guest count) from its sender state to a recipient: it arrives once, opens to the exact source, and is found again under the person. No occasion, no pin, no reply owed. Nora&rsquo;s &ldquo;thinking of Saturday&rdquo; is her opening, not Maya&rsquo;s agenda: Maya&rsquo;s week does not change until she does something, and enjoying it with no response is a complete ending. The photograph itself is the benefit; no interpretation of it is produced or required before she can enjoy it.')),
        ('AFTER A CONNECTION', N('08.4 and 08.5 continue 04.6 and 04.7 after both said yes. Connection enabled exactly what the sheet named: Nora can address Sam without a new link, and his link is where he returns; it now says &ldquo;From Nora&rdquo; and holds what he already had. He has no account and needs none. Fewer and Stop are his; neither tells her why and neither changes what he was part of.')),
        ('THE GUEST&rsquo;S PRIVATE ASK', N('The same pill everyone has (Plans 11 G1): on his link, &ldquo;Ask about this&rdquo; would ask Vesper, not Nora, from the supplied facts only. Not drawn as a slot; it is the 02.6 treatment on a link page.')),
        ('NOT DRAWN', N('Dana receiving something worthwhile through these people; a busy friends scope; a second one-friend variant. The assignment names these as later, not closure requirements.')),
    ], w=430)
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols1) + prop + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">SUNDAY SEP 27 &middot; AFTER BOTH SAID YES</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Where Sam returns, and what reaches him</div></div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols2) + notes + '</div>')
    return (HEAD + f'<div style="width: 2260px; min-height: {hh("08")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 08 &middot; CONTINUATIONS &middot; {STAMP}', '08 &middot; Continuations',
                   'Two continuations the September 8 assignment named as missing from the selected experience: a friend&rsquo;s original that has no place, received, opened, optionally kept, and found again; and where a guest returns after both people chose to stay in touch. One exact-original route across Home and Life, with continuing shared access, a deliberate Keep and keeping a place kept apart. Five slots beyond the twenty-four-slot ceiling, drawn on existing families and recorded on 00 and 07 as an unresolved scope discrepancy, not compliance; the placement extends the September 5 Status-doorway permission and remains a named proposal.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

FILES = {'08 - Continuations': board08}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
