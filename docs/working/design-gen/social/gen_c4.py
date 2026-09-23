"""Checkpoint 2 · board 04 · Experience C · Something stays with us. Nine slots; fixture copy only. Nothing here is ruled."""
import os, sys
from gen_c2 import *
from gen_c3 import linkframe, guestbar, pill, person_row, contribution, WEEK_SAT
from gen_c2 import HP
sys.path.insert(0, HP)
from gen_generous import ending as week_ending, arow
from gen_generous3 import fact, u2
from kit import anchor_row, orientation, row, dm
from gen_seam import chip, row_mark

WEEK_SUN = [('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('hollow', ''), '', MUTE)]
def life_head(kick, when):
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">{kick}</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def bar(t):
    return f'<div style="padding: 22px 22px 0 22px;"><div class="shead"><span>{t}</span><span class="rule"></span></div></div>'
def entry(kind, t, sub, last=False):
    return row_mark(kind, f'{t} &middot; <span style="color: #6E6862;">{sub}</span>', last=last)

# ───────────────────────────── 04.1 · Maya contributes the table photograph ─────────────────────────────
def maya_contribute():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SATURDAY &middot; AT NORA&rsquo;S</span><span class="fn" style="margin-left: auto;">9:40 PM</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{standin(250, "THE TABLE &middot; 8:25 PM &middot; HER PHONE &middot; ASSET NOT SOURCED")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;"><span style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">The hour your camera missed.</span></div><div class="fn" style="margin-top: 6px; color: {ANCHOR};">ONE LINE, OR NONE</div>', top=18)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div><div style="display: flex; align-items: center; gap: 10px;">{facepile(["N", "S"], 28, -8)}<span style="font-size: 15px; color: {INK};">Nora and Sam &middot; tonight&rsquo;s people</span></div><div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 10px;">Only them. It stays yours to take back. Sam gets it through his link.</div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 18px;"><span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 12px 22px; font-size: 15px; font-weight: 600;">Send</span>{door("Keep it to myself", MUTE)}</div>', top=26)
    return phone(inner, 0, active='Life')

# ───────────────────────────── 04.2 · Nora's Home, Sunday: the photo arrives ─────────────────────────────
def home_sunday():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '10:20 AM')
    inner += orientation('Clear and mild. Bach at the old church at four.', 'Maya sent a photograph from last night.')
    inner += sect('From last night') + gut(card(f'<div style="border-radius: 12px; overflow: hidden; margin-bottom: 10px;">{standin(210, "THE TABLE &middot; SATURDAY 8:25 PM &middot; ASSET NOT SOURCED")}</div>' + author_row('M', 'Maya', 'LAST NIGHT &middot; TO YOU AND SAM')
                                                  + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 8px;">The hour your camera missed.</div>'
                                                  + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 6px;">{door("Write back")}</div>' + meta('HERS &middot; TO THE DINNER&rsquo;S PEOPLE &middot; ALSO IN LIFE, UNDER LAST NIGHT', 8)))
    inner += sect('Today') + gut(u2('Bach on the organ at the old church, four o&rsquo;clock', 'The Passacaglia and two chorale preludes, forty minutes, free.', meta_t='DOWNTOWN &middot; SUNDAY 4 PM &middot; LISTED, NOT CHECKED TODAY &middot; PRIYA, LAST MONTH: &ldquo;GO EARLY FOR THE BACK PEWS&rdquo;') + door('The old church'))
    inner += sect('In motion') + gut('<div>' + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True) + '</div>')
    inner += gut(door('Everything in Life') + f'<div style="display: flex; gap: 7px; flex-wrap: wrap; padding-top: 8px;">{chip("dining", "Last night, at yours", "", serif=True)}</div>' + meta('LIFE &middot; THE DINNER, WITH WHAT EACH PERSON ADDED', 8), top=32)
    inner += week_ending(WEEK_SUN, 'Bach at four. Tuesday, the dentist.')
    return phone(inner, 0)

# ───────────────────────────── 04.3 · Sam, later: the same photograph ─────────────────────────────
def sam_photo():
    inner = guestbar('FROM MAYA &middot; THROUGH YOUR LINK &middot; SUNDAY')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Maya sent a photograph from last night.</div>', top=14)
    inner += gut(f'<div style="border-radius: 12px; overflow: hidden;">{standin(230, "THE TABLE &middot; SATURDAY 8:25 PM &middot; ASSET NOT SOURCED")}</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 10px;">&ldquo;The hour your camera missed.&rdquo;</div><div class="fn" style="margin-top: 6px; color: {ANCHOR};">MAYA &middot; TO YOU AND NORA</div>', top=18)
    inner += gut('<div>' + row('Stays here for you as long as Maya leaves it', mark='solid', color=GOLD) + row('The evening&rsquo;s details closed on Sunday', mark='hollow', last=True) + '</div>', top=18)
    inner += gut(door('Write back to Maya') + src('One line to Maya.'), top=22)
    return linkframe(inner)

# ───────────────────────────── 04.4 · Life · People · the dinner ─────────────────────────────
def life_record():
    inner = life_head('LIFE &middot; PEOPLE', 'LATER')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Pasta trial night, at yours</div><div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 6px;">Saturday Sep 19 &middot; with Maya and Sam &middot; you hosted</div>', top=14)
    inner += bar('WHAT EACH PERSON ADDED &middot; THEIRS') + gut('<div>' + arow('Maya &middot; the table photograph &middot; <span style="color: #6E6862;">the hour your camera missed</span>', avatars=['M'])
                                                              + arow('Dana &middot; the rag&ugrave;, from Sorrento &middot; <span style="color: #6E6862;">&ldquo;slower than feels right&rdquo;</span>', avatars=['D'])
                                                              + arow('Sam &middot; &ldquo;I&rsquo;ll need to leave by nine&rdquo; &middot; <span style="color: #6E6862;">and he did</span>', avatars=['S'], last=True) + '</div>')
    inner += bar('YOUR ACCOUNT &middot; ONLY YOU') + gut(f'<div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK2};">The sauce held. Dana was right about the twenty minutes.</div>')
    inner += bar('WHERE IT LIVES') + gut('<div>' + entry('dining', 'Saturday, Sep 19', 'Time') + entry('note', 'Maya, Sam, Dana', 'People') + entry('photo', 'Two photographs', 'the contact sheet', last=True) + '</div>')
    return phone(inner, 0, active='Life')

def boat_inset():
    """A separate record, linked from Life People; not nested in the dinner. An inset within the budget, not a slot."""
    return (f'<div style="margin-top: 14px; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div class="kickm">A SEPARATE RECORD &middot; LIFE &middot; PEOPLE &middot; LINKED, NOT NESTED</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 16px; line-height: 21px;">The couple from the boat</div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2};">Sorrento &rarr; Amalfi ferry, August &middot; met once. Holds the photo you promised and the address they wrote on the ferry receipt.</div>'
            f'<div style="display: flex; gap: 14px; align-items: center;">{door("Send the photo, once")}</div>'
            f'<div class="fn" style="color: {ANCHOR};">ITS OWN RECORD; SEARCH REACHES EITHER &middot; NO-PATH BRANCH: THE SAME RECORD WITHOUT THE DOOR</div></div>')

# ───────────────────────────── 04.5 · refinding ─────────────────────────────
def life_search():
    inner = life_head('LIFE', 'LATER')
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1.5px solid {INK}; border-radius: 999px; padding: 0 16px;"><span style="font-size: 15px; color: {INK}; flex: 1;">the photo maya sent from that dinner</span></div>', top=18)
    inner += bar('MOST LIKELY') + gut(card(f'<div style="border-radius: 12px; overflow: hidden; margin-bottom: 10px;">{standin(160, "THE TABLE &middot; STAND-IN")}</div>' + title('The table, Saturday Sep 19', 17, 22, 600) + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 4px;">Maya &middot; sent to you and Sam &middot; in <i>Pasta trial night, at yours</i></div>' + meta('MATCHED: MAYA, PHOTOGRAPH, A DINNER YOU HOSTED &middot; LIVES UNDER PEOPLE &rarr; MAYA, AND TIME &rarr; SEP 19', 8) + door('Open')))
    inner += bar('ALSO') + gut('<div>' + entry('photo', 'Dana&rsquo;s rag&ugrave;, from Sorrento', 'sent Friday, for the dinner', last=True) + '</div>')
    return phone(inner, 0, active='Life')

# ───────────────────────────── 04.6 / 04.7 · the ongoing-connection choice ─────────────────────────────
def sam_choice():
    """Sought, not prompted: on his link's record of the evening, Nora's line offers 'Stay in touch' when he looks for it. Branch V: his number is verified, so the request can be his."""
    inner = guestbar('SATURDAY, AT NORA&rsquo;S &middot; YOUR LINK')
    inner += gut(f'<div style="border-radius: 12px; overflow: hidden;">{standin(120, "THE TABLE &middot; STAND-IN")}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">Maya&rsquo;s photograph of the table. Saturday Sep 19, from seven, at Nora&rsquo;s.</div>', top=14)
    inner += gut('<div>' + row('Maya &middot; <span style="color: #6E6862;">her photograph, to you and Nora, as long as she leaves it</span>', mark='av:M') + row('Nora &middot; <span style="color: #6E6862;">your host</span>', mark='av:N', last=True) + '</div>' + door('Stay in touch'), top=18)
    inner += gut(f'<div style="background: {CARD}; border-radius: 18px 18px 0 0; box-shadow: 0 -8px 24px rgba(27,23,20,0.14); padding: 14px 22px 22px 22px;"><div style="width: 36px; height: 4px; border-radius: 2px; background: rgba(27,23,20,0.15); margin: 0 auto 14px auto;"></div>'
                 + title('Stay in touch with Nora?', 19, 24, 600) + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">If you both say yes, you can share things and invite each other again.</div>'
                 + f'<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px;">{pill("Yes, if she does")}{pill("Leave it", False)}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">Leaving it is fine.</div></div>', top=22)
    return linkframe(inner)

def nora_choice():
    inner = anchor_row('NEW YORK &middot; TUESDAY', '6:30 PM')
    inner += orientation('Clear evening. The noodle counter is open till ten.', 'One thing from Sam.')
    inner += sect('In motion') + gut('<div>' + arow('Sam &middot; would stay in touch, if you would &middot; <span style="color: #6E6862;">share things and invite each other again</span>', avatars=['S']) + row('Dentist &middot; done &middot; <span style="color: #6E6862;">next in six months</span>', mark='solid', color=GOLD, last=True) + '</div>' + f'<div style="display: flex; gap: 18px; align-items: center; padding-top: 10px;">{door("Yes")}{door("Leave it", MUTE)}</div>')
    inner += sect('Tonight') + gut(u2('Hand-pulled noodles at the counter till ten', 'Three blocks from Canal Hall. $14&ndash;18.', meta_t='CANAL STREET &middot; LISTED DAILY 6&ndash;10, NOT CHECKED TODAY') + door('The noodle counter'))
    inner += gut(door('Everything in Life') + meta('LIFE', 0), top=32)
    inner += week_ending([('TUE', dm('solid', INK), 'today', INK), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('hollow', ''), '', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE)], 'Noodles tonight, if you like. A quiet week.')
    return phone(inner, 0)

# ───────────────────────────── 04.8 · the boat couple ─────────────────────────────
def another_evening():
    """The existing-relationship continuation: Vesper recovers what usefully carries forward (place, start time, the photo), not old personal constraints. New invitations, new answers."""
    inner = chat_head('TWO WEEKS LATER')
    inner += gut(ctx_chip('LAST TIME &middot; SEP 19 &middot; AT YOURS', dot=GOLD), top=26)
    inner += gut(bubble('dinner with maya and sam again? saturday the 3rd'), top=22)
    inner += gut(answer('Here&rsquo;s a draft for another pasta evening at yours on Saturday, October 3, with Maya and Sam. Last time you started at seven; keep that time?'), top=18)
    inner += gut(card(f'<div class="kick" style="color: {GOLDD};">DRAFT &middot; NOT SENT</div>' + title('Pasta evening at Nora&rsquo;s', 18, 23, 600)
                      + f'<div style="margin-top: 6px; display: flex; flex-direction: column; gap: 2px;"><div style="font-size: 14px; line-height: 20px; color: {INK2};">Saturday Oct 3 &middot; from seven, proposed</div><div style="font-size: 14px; line-height: 20px; color: {INK2};">Court Street, 3F &middot; nothing to bring</div><div style="font-size: 14px; line-height: 20px; color: {INK2};">Maya and Sam &middot; fresh invitations; their answers decide</div></div>'
                      + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 8px;">{door("The table, last time")}</div>'
                      + f'<div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(27,23,20,0.08); font-size: 13px; line-height: 19px; color: {INK2};">From last time: the address and the buzzer, that nothing is brought, the photograph, and Dana&rsquo;s rag&ugrave;.<br>Not from last time: who can come and when. Maya and Sam answer again.</div>'), top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 14px;">{pill("Send with seven")}{pill("Change something", False)}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">Or leave it here.</div>', top=18)
    return phone(inner, 0, active='Chat')

def before_after():
    return (f'<div style="display: flex; gap: 12px; margin-top: 10px;">'
            f'<div style="flex: 1; border: 1px dashed rgba(27,23,20,0.25); border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">BEFORE &middot; SAME CURRENT FACTS</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">Nora types the new arrangement herself (&ldquo;sat oct 3, 7, at mine, court st 3f, maya + sam, nothing to bring&rdquo;), then searches Life for the table photo to mention it.</div></div>'
            f'<div style="flex: 1; border: 1px solid rgba(27,23,20,0.10); background: {CARD}; border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">AFTER &middot; SAME CURRENT FACTS</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">One line. The draft recovers the address, the buzzer, nothing-to-bring, the photograph and Dana&rsquo;s dish, and proposes last time&rsquo;s seven. Availability is the one thing it does not carry forward.</div></div></div>')

def before_after():
    return (f'<div style="display: flex; gap: 12px; margin-top: 10px;">'
            f'<div style="flex: 1; border: 1px dashed rgba(27,23,20,0.25); border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">BEFORE</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">&ldquo;pasta night sat oct 3 at 7, maya + sam, nothing to bring, at mine, court st 3f&rdquo;</div></div>'
            f'<div style="flex: 1; border: 1px solid rgba(27,23,20,0.10); background: {CARD}; border-radius: 8px; padding: 10px 12px;"><div class="kickm" style="margin-bottom: 4px;">AFTER</div><div style="font-size: 12px; line-height: 16px; color: {INK2};">&ldquo;dinner with maya and sam again? saturday the 3rd&rdquo;</div></div></div>')

# ───────────────────────────── 04.9 · withdrawal ─────────────────────────────
def withdrawal():
    inner = life_head('LIFE &middot; PEOPLE &middot; MAYA', 'SUNDAY')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Maya</div><div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 6px;">Shared with you &middot; a record since 2019</div>', top=14)
    inner += gut(f'<div style="{SERIF} font-style: italic; font-size: 16px; line-height: 23px; color: {INK2};">Maya took back her Paris note on Sunday. Everything else here is as it was.</div>', top=18)
    inner += bar('FROM HER &middot; HERS') + gut('<div>' + entry('photo', 'The Print Room', 'Thursday &middot; to friends &middot; through today') + entry('photo', 'The table, Saturday', 'to you and Sam') + entry('note', 'The side room, after four', 'her suggestion for Saturday', last=True) + '</div>')
    inner += bar('HELD IN COMMON') + gut('<div>' + entry('dining', 'Pasta trial night, Sep 19', 'you hosted') + entry('dining', 'Two more evenings', 'this year', last=True) + '</div>')
    inner += gut(src('The dinner, her photo and her suggestion stand.'), top=22)
    return phone(inner, 0, active='Life')

def board04():
    P1 = [
        ('04.1', 'MAYA', 'OCCASION', maya_contribute(), ('SATURDAY 9:40 PM', 'THE PHOTO THE HOST NEVER TOOK', 'Maya contributes the table, deliberately, to tonight&rsquo;s people', 'A GESTURE, NOT AN ARRIVAL &middot; TO NORA AND SAM ONLY &middot; HERS TO TAKE BACK &middot; NOT A POST, NOT AN ALBUM'),
         ('Maya', 'The dinner, Saturday night', 'Contribute', 'Her photo to the dinner&rsquo;s people', 'The agreed audience; her grant', 'Contribution', 'Nora and Sam, later', 'Done; nothing asked'), ('FIXTURE', 'C1 &middot; AFFECTED-PERSON RIGHTS APPLY', 'T2 &middot; THE ONE CLEAR SEND &middot; OWNER READBACK ONCE')),
        ('04.2', 'NORA', 'HOME', home_sunday(), ('SUNDAY 10:20 AM', 'IT ARRIVES ONCE, AS THE IMAGE', 'From last night; a quiet Sunday with a concrete opening', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION &middot; BACH AT FOUR IS AN ILLUSTRATIVE USEFUL OPENING, NOT A RULE OF ONE (HOME-OWNER DELTA) &middot; LISTED FACTS AND AN ATTRIBUTED LINE KEPT APART'),
         ('Nora', 'Home, Sunday', 'Open', 'The table photograph, the image itself', 'Agreed audience', 'Contribution / Home', '&mdash;', 'Enjoy it; nothing asked'), ('HOME SOCIAL SPLIT &middot; RULED', 'ADDRESSED REGION &middot; ONE ITEM', 'FIXTURE')),
        ('04.3', 'SAM', 'LINK', sam_photo(), ('SUNDAY &middot; HIS LINK &middot; VERIFIED', 'THE SAME PHOTOGRAPH, LATER', 'Displayed through his verified link as long as Maya leaves it', 'BRANCH V: HIS NUMBER WAS CONFIRMED FOR THE ADDRESS; THE SAME PRINCIPAL SEES THE PHOTO &middot; THE EVENING&rsquo;S DETAILS CLOSED SUNDAY &middot; NO ACCOUNT'),
         ('Sam', 'His link, later', 'Open', 'The same photograph', 'Maya&rsquo;s delivery to the dinner&rsquo;s people; until she takes it back', 'Contribution (guest view)', '&mdash;', 'Receive without contributing'), ('DEPENDENCY &middot; LATER MEDIA DELIVERY TO A VERIFIED NON-MEMBER', 'GUEST PROPOSAL &sect;3', 'FIXTURE')),
        ('04.4', 'NORA', 'LIFE', life_record(), ('LATER &middot; LIFE &middot; PEOPLE', 'THE EVENING AS ONE RECORD', 'What each person added, theirs; her account, hers alone', 'RECOGNITION, NOT MAINTENANCE &middot; SAM&rsquo;S &ldquo;LEAVE BY NINE&rdquo; HERE IS HIS SUPPLIED PARTICIPATION, NOT A LEAK &middot; THE BOAT COUPLE ARE A SEPARATE RECORD (INSET)'),
         ('Nora', 'Life &middot; People', 'Open', 'The dinner as one record', 'Attributed; her account private', 'Life', '&mdash;', 'Recognition, not maintenance'), ('COPY OF R3&rsquo;S GRAMMAR', 'LIFE SEQUENCES &middot; RULED', 'THE BOAT INSET IS NOT A SLOT')),
        ('04.5', 'NORA', 'LIFE', life_search(), ('LATER &middot; LIFE SEARCH', 'ONE RETRIEVAL', '&ldquo;the photo maya sent from that dinner&rdquo;', 'A DOOR WITH ITS CONTAINMENT AND WHY IT MATCHED &middot; RETRIEVAL WRITES NOTHING'),
         ('Nora', 'Life search', 'Find', 'A door with its containment', 'Retrieval writes nothing', 'Life', '&mdash;', 'Open, or leave'), ('LIFE REFINDING &middot; RULED', 'REFIND OVER A PHOTO IS A DEPENDENCY (CAPABILITY MAP SEAM 7)', 'FIXTURE')),
    ]
    P2 = [
        ('04.6', 'SAM', 'LINK', sam_choice(), ('LATER &middot; HIS LINK &middot; SOUGHT, NOT PROMPTED', 'STAY IN TOUCH?', 'His record holds Maya&rsquo;s photograph and the dinner&rsquo;s shared facts, nothing Nora wrote for herself; he looks under her name; leaving it is fine', 'C5 &middot; NEVER APPENDED AFTER A PHOTO &middot; BRANCH V: HIS VERIFIED NUMBER IS THE PRINCIPAL &middot; SEPARATE FROM RSVP AND THE PHOTO'),
         ('Sam', 'His link&rsquo;s record of the evening', 'Seek, then choose', 'A named capability: things between them, inviting without a link', 'Nobody is told of a non-answer', 'Relationship (proposal)', 'Nora sees a request, or nothing', 'Bound, or connected'), ('PROPOSED &middot; C5: SHARE THINGS AND INVITE EACH OTHER AGAIN', 'DEPENDENCY &middot; THE VERIFIED CONTACT AS PRINCIPAL (GUEST PROPOSAL)', 'FIXTURE')),
        ('04.7', 'NORA', 'HOME', nora_choice(), ('TUESDAY 6:30 PM', 'HER SIDE OF THE SAME CHOICE', 'One row in motion; yes, or leave it; a concrete evening opening', 'ONE ITEM, SO NO ADDRESSED-TO-YOU SECTION &middot; A QUIET EVENING STILL CARRIES ONE USABLE WORLD OPENING (HOME-OWNER DELTA)'),
         ('Nora', 'Home, later', 'Choose', 'Sam&rsquo;s request as one line', 'No past material, location or future inclusion', 'Relationship (proposal)', 'Sam sees the answer, or nothing', 'Ignored, declined or accepted'), ('PROPOSED &middot; C5', 'HOME ADDRESSED REGION', 'FIXTURE')),
        ('04.8', 'NORA', 'CHAT', another_evening(), ('TWO WEEKS LATER', 'ANOTHER PASTA EVENING', 'What last time supplies, named: the address, the buzzer, nothing to bring, the photograph, the dish; and what it does not: anyone&rsquo;s availability', 'WHAT USEFULLY CARRIES FORWARD, NOT OLD STATE &middot; OLD AVAILABILITY IS NEVER SHOWN AS CURRENT &middot; THEIR ANSWERS DECIDE &middot; SHE MAY LEAVE THE DRAFT &middot; ONE COMPARISON, NOT A MEMORY LOOP ASKED OF EVERY SHARE'),
         ('Nora', 'Chat', 'Say it', 'A private draft: place, proposed seven, the people named; the photo reachable', 'Maya and Sam get fresh invitations; nothing prefilled from their side', 'Occasion (new, on Send)', 'Two fresh invitations', 'Send with seven; change something; or leave it'), ('R8 F2 &middot; REACTIVATION BY REFERENCE', 'BEFORE / AFTER, SAME CURRENT FACTS', 'DRAFT = PRIVATE PREPARATION UNDER ASK; NO PLAN PERSISTS UNTIL SEND')),
        ('04.9', 'NORA', 'LIFE', withdrawal(), ('SUNDAY &middot; MAYA&rsquo;S PAGE', 'WITHDRAWAL', 'The Paris note is gone; everything else as it was', 'DEPENDENTS GONE, INDEPENDENT ITEMS STANDING &middot; NO NEW CONTACT'),
         ('Nora', 'Life, Sunday', 'Read', 'One honest line', 'A2 and its derivatives gone', 'Contribution', '&mdash;', 'Nothing owed'), ('COPY OF R3&rsquo;S WORDING', 'CORRECTION CONTRACT &middot; RULED', 'FIXTURE')),
    ]
    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]
    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s) + (before_after() if n == '04.8' else '')) for n, role, root, ph, c, r, s in P2]
    cols1[3] = cols1[3][:-6] + boat_inset() + '</div>'
    notes = [notecol('What board 04 shows', [
        ('ONE SOURCE, THREE VIEWS', N('04.1 is Maya&rsquo;s gesture; 04.2 and 04.3 are Nora&rsquo;s and Sam&rsquo;s receipts of the same photograph; 04.4 and 04.5 find it again. No frame invents a second copy or a feed. What Sam holds later (04.6) is named exactly: Maya&rsquo;s photograph, for as long as she leaves it, and the dinner&rsquo;s shared facts; Nora&rsquo;s account on 04.4 stays hers, and his own &ldquo;leave by nine&rdquo; appearing in her record is his supplied participation, not a leak. Where he returns after a connection is board 08.')),
        ('SAM, LATER', N('He can look at the photograph through his verified link for as long as Maya leaves it (branch V): his number was confirmed earlier for the address, and the same principal sees the photo. There is no separate Keep and no second verification. Identity and later media delivery for a non-member remain a dependency outside the phone.')),
        ('THE CHOICE, BOTH SIDES', N('04.6 is sought: Sam looks under Nora&rsquo;s name on his link&rsquo;s record of the evening; nothing is appended after the photograph. The sheet names what a connection enables: things between them (a photo, a place, a recipe, a line) and inviting without a new link. 04.7 is one row in Nora&rsquo;s In motion. Leaving it is fine on both sides. A non-account guest needs a verified principal for this (guest proposal).')),
        ('ANOTHER EVENING', N('04.8 now names the benefit exactly. From the authorized previous outcome: the address and the buzzer, that nothing is brought, the table photograph, Dana&rsquo;s dish, and last time&rsquo;s seven as a proposal. Not from it: anyone&rsquo;s availability. Sam&rsquo;s old arrival and departure stay history, not defaults; his and Maya&rsquo;s fresh answers decide. The draft is private preparation until Send; Nora may leave it. Both sides of the before/after use the same current facts. The boat couple are their own record, linked from Life People as an inset beside 04.4, not nested in the dinner.')),
        ('WITHDRAWAL', N('04.9 uses R3&rsquo;s wording. The note is gone with what derived from it; her photo, her suggestion and the dinner were never hers to take with it.')),
    ], w=430)]
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols1) + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">CONTINUATION AND ENDINGS</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Stay connected, or not; send the promised photo; take a note back</div></div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols2) + ''.join(notes) + '</div>')
    return (HEAD + f'<div style="width: 2260px; min-height: {hh("04")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 04 &middot; SOMETHING STAYS WITH US &middot; {STAMP}', '04 &middot; Something stays with us',
                   'Does shared life become easier to recover and continue without becoming another archive to curate or a friendship-maintenance obligation? Nine slots, revised per &sect;14: Maya&rsquo;s gesture; the photograph arriving for Nora and, later, for Sam; the evening as one record (with the promised boat photo as a row) and one retrieval; the connection sought from Sam&rsquo;s side and answered on Nora&rsquo;s; another pasta evening by reference; and withdrawal.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

FILES = {'04 - Something stays with us': board04}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
