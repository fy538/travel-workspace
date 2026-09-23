"""Board 09 · Sending, access and control (September 12 coverage assignment).
Seven compact slots: one eligible recipient resolved, the preview and Send, the result; the sender's own edit and
withdraw with its result or failure; the supported safety controls and what they actually do; and a conditional
guest access sequence. Shared components where they exist (Notice, the sheet, field, buttons, recipient token);
local construction where the package has none, each named. Fixture; PROPOSED."""
import os, sys
from gen_c2 import *
from gen_c2 import HP, HEAD_VDL, dci, inset, KERNEL_CSS
from gen_c3 import linkframe, guestbar, pill, person_row
sys.path.insert(0, HP)
from kit import row, anchor_row
from gen_generous import arow
from gen_se import hh, tbl, blk, FOOT2, STAMP, ROLE, tag

WORDS = 'The side room was my favorite. Go on a weekday, it was empty.'

def sheet_block(inner):
    return f'<div class="vdl-sheet" style="border-radius: 18px; padding-bottom: 18px;"><div class="vdl-sheet-handle"></div>{inner}</div>'

def cand(letter, name, how, on, bg='#1B1714'):
    tick = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7.2l2.6 2.6L11 4.4" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' if on else '')
    return (f'<div style="display: grid; grid-template-columns: 28px 1fr 16px; column-gap: 12px; align-items: center; padding: 11px 0; border-bottom: 0.5px solid var(--vk-borderHairline);">'
            f'<span class="vk-t-capsMicro" style="width: 28px; height: 28px; border-radius: 14px; background: {bg}; color: #FBF7EC; display: flex; align-items: center; justify-content: center; font-weight: 700;">{letter}</span>'
            f'<div><div class="vk-t-bodyMd" style="color: var(--vk-ink00);">{name}</div><div class="vdl-t-supportLine" style="color: var(--vk-ink60);">{how}</div></div>{tick}</div>')

# ───────────────────────────── 09.1 · who gets it, among eligible people ─────────────────────────────
def who_sheet():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; THE HARBOR PRINT ROOM</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 150, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 10px;">{WORDS}</div>', top=16)
    body = ('<div class="vdl-sheet-head"><div class="vdl-t-metaLine" style="color: var(--vk-ink60);">YOUR SHARE</div><div class="vdl-t-sectionHeading" style="font-size: 15px; margin-top: 2px;">Who gets it</div></div>'
            '<div style="border-top: 0.5px solid var(--vk-borderHairline);">'
            + cand('F', 'Friends', 'everyone you&rsquo;re connected with', False, '#8A6628')
            + cand('N', 'Nora Lin', 'friend &middot; the pasta nights', True)
            + cand('N', 'Nora Kaye', 'friend &middot; from work', False)
            + cand('P', 'Priya', 'friend &middot; the Red Hook walk', False) + '</div>'
            '<div class="vdl-field pill focused" style="margin-top: 14px;"><span class="vk-t-bodyMd">nora</span></div>'
            '<div class="vk-t-caption" style="color: var(--vk-ink60); margin-top: 6px;">Two people you&rsquo;re connected with are called Nora. The line under each name is how you know them.</div>'
            '<div class="vdl-sheet-actions"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white); width: 100%; box-sizing: border-box;">Done</span></div>')
    inner += gut(sheet_block(body), top=18)
    return phone2(inner, active='Places')

def nomatch_inset():
    body = ('<div class="vdl-field pill focused"><span class="vk-t-bodyMd">norra</span></div>'
            '<div class="vk-t-caption" style="color: var(--vk-ink60);">No one you&rsquo;re connected with is called norra. Check the spelling, or choose Friends.</div>'
            '<div class="vdl-t-supportLine" style="color: var(--vk-ink40);">The list only ever holds people already connected to Maya. Nothing searches her phone, and choosing someone here grants nothing beyond this one share.</div>')
    return inset('09.1, THE SAME SHEET &middot; NO MATCH', body,
                 'SHARED &middot; .vdl-field &middot; NO CONTACTS IMPORT, NO GENERAL FRIENDS GRANT &middot; A SECOND NORA IS FIXTURE, FOR TELLING TWO APART')

# ───────────────────────────── 09.2 · the preview, before Send ─────────────────────────────
def send_preview():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; THE HARBOR PRINT ROOM</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 170, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div>', top=16)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;"><span style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">{WORDS}</span></div>', top=14)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">WHO</div>'
                 f'<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;"><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">N</span><span class="vk-t-bodySmMedium">Nora Lin</span></span>{door("Change", MUTE)}</div>'
                 f'<div style="font-size: 13px; line-height: 19px; color: {INK2}; margin-top: 10px;">She sees this photograph and these words, the place and Red Hook. Through Sunday.</div>', top=20)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 16px;"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">Send</span>{door("Not now", MUTE)}</div>'
                 + src('Your words go exactly as written. Leaving sends nothing.'), top=22)
    return phone2(inner, active='Places')

# ───────────────────────────── 09.3 · sent, or not ─────────────────────────────
def send_result():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">THE HARBOR PRINT ROOM</span></div></div>'
    inner += gut(dci('Notice', 64, tone='applied', title='Sent to Nora Lin · 4:05', body='Nothing else changed.'), top=18)
    inner += gut(dci('Notice', 120, tone='failed', title='Didn’t send. You’re offline.', body='Your words and your choice of Nora are still here.', primary='Try again', secondary='Not now'), top=12)
    inner += gut(dci('Notice', 84, tone='unknown', title='Not sure it went out', body='The send was interrupted. Nothing is sent twice; this resolves either way.'), top=12)
    inner += sect('Either way, the same place') + gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 120, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 10px;">{WORDS}</div>' + src('Back where she was, with her words as she wrote them.'))
    return phone2(inner, active='Places')

# ───────────────────────────── 09.4 · her own share, later ─────────────────────────────
def sender_view():
    inner = header('Yours', 'Thursday &middot; to Nora Lin &middot; through Sunday', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 200, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{WORDS}</div>', top=16)
    inner += sect('A reply') + gut('<div>' + share_line('N', 'Nora', 'That side room. I want to see it before Sunday.', 'Thursday 9:12 pm', last=True) + '</div>')
    inner += gut(f'<div style="display: flex; gap: 22px; align-items: center;">{door("Edit")}{door("Take it back", MUTE)}</div>' + src('No viewer list, no count, no report of what she did with it.'), top=24)
    inner += gut(sheet_block('<div class="vdl-sheet-head"><div class="vdl-t-sectionHeading" style="font-size: 15px;">Take it back?</div></div>'
                             '<div class="vdl-t-supportLine" style="color: var(--vk-ink40);">Nora stops seeing your photograph and your words. Her reply stays hers, and anything she kept under your grant stays with her until it expires. She is not told.</div>'
                             '<div class="vdl-sheet-actions"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white); width: 100%; box-sizing: border-box;">Take it back</span>'
                             '<span class="vdl-btn secondary pill vk-t-labelSemibold" style="width: 100%; box-sizing: border-box;">Keep it shared</span></div>'), top=22)
    return phone2(inner, active='Places')

# ───────────────────────────── 09.5 · edited, taken back, or not ─────────────────────────────
def sender_result():
    inner = header('Yours', 'Thursday &middot; through Sunday', back=True)
    inner += gut(dci('Notice', 64, tone='applied', title='Taken back · 9:40', body='Nora no longer sees it.'), top=18)
    inner += gut(dci('Notice', 120, tone='failed', title='Couldn’t take it back yet', body='It is still shared with Nora. Nothing else changed.', primary='Try again', secondary='Not now'), top=12)
    inner += sect('What stays') + gut('<div>' + row('Her reply &middot; <span style="color: #6E6862;">hers; it stays in your thread</span>', mark='hollow')
                                      + row('Priya&rsquo;s note about the Print Room &middot; <span style="color: #6E6862;">hers; untouched</span>', mark='hollow')
                                      + row('Your own photograph &middot; <span style="color: #6E6862;">still yours, still in Life</span>', mark='hollow', last=True) + '</div>'
                                      + src('Taking one share back removes that share, not other people&rsquo;s material.'))
    inner += gut(door('Share it again') + src('A new share, with its own audience and its own end.'), top=20)
    return phone2(inner, active='Places')

# ───────────────────────────── 09.6 · fewer, mute, block, leave ─────────────────────────────
def controls_phone():
    def ctrl(t, effect):
        return (f'<div style="padding: 12px 0; border-bottom: 0.5px solid rgba(27,23,20,0.10);">'
                f'<div class="vk-t-bodyMd" style="color: {INK};">{t}</div>'
                f'<div class="vdl-t-supportLine" style="color: {INK2}; margin-top: 2px;">{effect}</div></div>')
    inner = header('Nora Lin', 'Friend &middot; since 2019', back=True)
    inner += gut(f'<div class="kickm" style="margin-bottom: 6px;">IF YOU WANT LESS OF THIS</div>'
                 + '<div style="border-top: 0.5px solid rgba(27,23,20,0.10);">'
                 + ctrl('Fewer of these', 'Her shares stop arriving on your Home. You can still open them from Life &middot; People.')
                 + ctrl('Mute Nora', 'Nothing of hers reaches you anywhere until you unmute. She is not told.')
                 + ctrl('Leave this evening', 'You come off the dinner&rsquo;s people. The host sees one line; nobody else is told.')
                 + ctrl('Block Nora', 'No contact either way, and no new invitation can reach you from her.')
                 + '</div>', top=18)
    inner += sect('What none of these do') + gut('<div>' + row('Change who came to an evening you both attended', mark='hollow')
                                                 + row('Delete what she wrote, or what you wrote to her', mark='hollow')
                                                 + row('Tell her why, or tell anyone else', mark='hollow', last=True) + '</div>'
                                                 + src('Each is its own choice. None is a step on the way to another.'))
    inner += gut(door('Report something') + src('Goes to Vesper, not to Nora.'), top=20)
    return phone2(inner, active='Life')

# ───────────────────────────── 09.7 · the guest's access step, conditional ─────────────────────────────
def guest_access():
    inner = guestbar('FROM NORA &middot; A LINK &middot; NOTHING TO INSTALL')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">The exact address, once you confirm this number.</div>', top=14)
    inner += gut(f'<div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK2};">You already have the evening: Saturday from seven, Carroll Gardens, nothing to bring. This is only for the door.</div>', top=12)
    inner += gut(f'<div style="display: flex; gap: 8px;">' + ''.join(f'<span style="flex: 1; height: 48px; border: 1px solid rgba(27,23,20,0.18); border-radius: 12px; display: flex; align-items: center; justify-content: center; {SERIF} font-size: 20px; color: {INK};">{c}</span>' for c in ('4', '1', '7', '&nbsp;')) + '</div>'
                 + f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">Sent by text to the number Nora typed. It is good for tonight.</div>', top=20)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 14px;">{pill("Confirm")}{pill("Send it again", False)}</div>', top=18)
    inner += gut(dci('Notice', 96, tone='failed', title='That code doesn’t match', body='Two tries left, or ask Nora to send a new one.', primary='Try again', secondary='Ask Nora'), top=20)
    inner += gut(dci('Notice', 96, tone='stale', title='This code has expired', body='Codes last an evening. Ask Nora for a new one; your answer still stands.', primary='Ask Nora'), top=12)
    return linkframe(inner)

def guest_endings_inset():
    body = ('<div class="vdl-t-supportLine" style="color: #3C352E;"><b>Confirmed.</b> The door facts appear on the same page: Court Street, 3F, the buzzer says N. Nothing else of Nora&rsquo;s opens.</div>'
            '<div class="vdl-t-supportLine" style="color: #3C352E;"><b>The invitation changed.</b> If Nora moves the evening after he confirmed, his page updates in place and says what changed; the code is not asked for again.</div>'
            '<div class="vdl-t-supportLine" style="color: #3C352E;"><b>Reopened.</b> If she sends the invitation again after it lapsed, it arrives as a new link; the old one stays dead rather than silently waking.</div>'
            '<div class="vdl-t-supportLine" style="color: #3C352E;"><b>Unavailable.</b> If the link cannot be checked at all, the page says so and keeps what he already had: the evening, the neighbourhood, his own answer. It does not guess the address.</div>')
    return inset('09.7, CONTINUED &middot; THE ENDINGS &middot; CONDITIONAL', body,
                 'DRAWN ONLY AS THE PROPOSED GUEST BRANCH V &middot; NOT A SELECTED SERVICE: IDENTITY, DELIVERY AND RETENTION FOR A NON-MEMBER REMAIN A SEPARATE AGREEMENT &middot; NOTHING HERE ADOPTS A VERIFICATION MECHANISM')

# ───────────────────────────── the board ─────────────────────────────
DIVISION = [
    ['A deliberate face others can see: what Maya chooses to share and to whom', 'Social', 'Authored per share, never inferred. No occasion profile, no popularity or view count, no compatibility score'],
    ['Choosing, correcting and withdrawing one share; who is eligible to receive it', 'Social', 'Drawn here: 09.1 to 09.5. Friends scope itself remains a separate agreement'],
    ['Mute, fewer, leave, block and report, with their actual effects', 'Social draws entry and effect; You &amp; Trust owns the account-wide switches', 'Coordinated, not duplicated: the same four choices, one vocabulary. Policy stays proposed'],
    ['Account, connections, notifications, retained material, accepted assistance', 'You &amp; Trust', 'Its own project as of September 12; Social links to it and does not restate it'],
    ['The record of what each person shared, contributed and withdrew', 'Life &middot; People', 'One record. Social shows the current share, not a second biography'],
]
COVER = [
    ['Eligible recipient resolution, disambiguation, change, no match', '09.1 with its no-match state; 02.2 keeps the entry', 'Drawn', 'Social', 'Friends-audience agreement for the scope itself'],
    ['The exact outgoing material, Send or leave, and the result', '09.2, 09.3', 'Drawn on the shared Notice', 'Social', 'None'],
    ['The sender&rsquo;s own share: edit, take back, confirm', '09.4', 'Drawn; no shared sender variant exists', 'Shared-library owner', 'Sender variant in a later package'],
    ['Sender result, failure, and what remains with its owner', '09.5', 'Drawn on the shared Notice', 'Social', 'None'],
    ['Supported controls and their actual effects', '09.6', 'Drawn as entry and effect; the policy stays proposed', 'Social with You &amp; Trust', 'Founder ruling on block, mute, disconnect, report'],
    ['Guest access: preview, code, payoff, wrong or expired code, retry, changed or reopened invitation, unavailable', '09.7 and its endings inset', 'Drawn, conditional', 'Guest identity and delivery proposal', 'Selection of the guest service'],
]

def board09():
    P1 = [
        ('09.1', 'MAYA', 'PLACES', who_sheet(), ('THE SHARE &middot; WHO GETS IT', 'ONE RECIPIENT, AMONG PEOPLE SHE IS CONNECTED WITH', 'Two friends called Nora, told apart by how she knows them', 'ELIGIBLE CONNECTIONS ONLY &middot; NO CONTACTS IMPORT &middot; CHOOSING SOMEONE GRANTS NOTHING BEYOND THIS SHARE'),
         ('Maya', 'Her own share', 'Choose or correct', 'The right person, told apart', 'Only people already connected', 'Contribution', '&mdash;', 'Done; or leave it'), ('SHARED &middot; .vdl-sheet, .vdl-field, .vdl-btn', 'FOLLOWS THE WORKBENCH&rsquo;S PROPOSED S1 SHEET (02B)', 'FRIENDS SCOPE: SEPARATE AGREEMENT')),
        ('09.2', 'MAYA', 'PLACES', send_preview(), ('BEFORE SEND', 'HER WORDS, EXACTLY, TO ONE PERSON', 'The recipient, what that person will see, and until when', 'THE PREVIEW IS THE MESSAGE &middot; NOTHING IS SENT UNTIL SEND &middot; LEAVING SENDS NOTHING'),
         ('Maya', 'The share', 'Read it back', 'Her words unchanged; one named recipient', 'Nora Lin only, through Sunday', 'Contribution', 'Nora Lin', 'Send; or not now'), ('SHARED &middot; .vdl-recipient, .vdl-btn', 'T2 &middot; ONE CLEAR SEND', 'FIXTURE')),
        ('09.3', 'MAYA', 'PLACES', send_result(), ('AFTER SEND', 'SENT, NOT SENT, OR NOT YET KNOWN', 'Three truthful endings, then the same place as before', 'PLANS 90 J2c&ndash;J2e SEMANTICS &middot; NOTHING IS SENT TWICE &middot; NO DELIVERY OR READ REPORT ABOUT NORA'),
         ('Maya', 'The share', 'Send', 'A truthful result', 'Nora Lin only', 'Contribution', 'Nora Lin', 'Back to the same place'), ('SHARED &middot; Notice: applied, failed, unknown', 'R8 RECOVERY SEMANTICS', 'FIXTURE')),
    ]
    P2 = [
        ('09.4', 'MAYA', 'PLACES', sender_view(), ('LATER &middot; HER OWN SHARE', 'EDIT, OR TAKE IT BACK', 'One reply, her two controls, and what taking it back means before she does it', 'NO VIEWER LIST, NO COUNT, NO USE REPORT &middot; THE CONFIRMATION SAYS WHAT SURVIVES &middot; NORA IS NOT TOLD'),
         ('Maya', 'Her own contribution', 'Edit or withdraw', 'Control of her own material', 'Nora Lin; her reply stays hers', 'Contribution', 'Nora Lin', 'Take it back; or keep it shared'), ('LOCAL &middot; NO SHARED SENDER VARIANT &middot; REPORTED', 'SHARED &middot; .vdl-sheet, .vdl-btn', 'C4 WITHDRAWAL &middot; RULED')),
        ('09.5', 'MAYA', 'PLACES', sender_result(), ('AFTER TAKING IT BACK', 'THE RESULT, AND WHAT STAYS WITH ITS OWNER', 'Taken back, or not yet; her reply, Priya&rsquo;s note and her own photograph are untouched', 'A WITHDRAWAL REMOVES ONE SHARE, NOT OTHER PEOPLE&rsquo;S MATERIAL &middot; FAILURE IS STATED, NOT HIDDEN'),
         ('Maya', 'Her own contribution', 'Read the result', 'What changed and what did not', 'Nora Lin', 'Contribution', '&mdash;', 'Share it again, or leave it'), ('SHARED &middot; Notice: applied, failed', 'INDEPENDENT MATERIAL KEEPS ITS OWNER', 'FIXTURE')),
        ('09.6', 'NORA', 'LIFE', controls_phone(), ('IF YOU WANT LESS OF THIS', 'FOUR DISTINCT CHOICES, AND WHAT THEY ACTUALLY DO', 'Fewer, mute, leave, block; report goes to Vesper', 'ENTRY AND EFFECT ONLY &middot; NONE IS A STEP TOWARDS ANOTHER &middot; HIDING SOMEONE NEVER CHANGES WHO CAME'),
         ('Nora', 'Life &middot; People &middot; Nora Lin', 'Choose one', 'Less of something, without a negotiation', 'Nobody is told', 'Relationship (proposal)', '&mdash;', 'Done; reversible except block&rsquo;s effect on new invitations'), ('POLICY PROPOSED, NOT ADOPTED', 'COORDINATED WITH YOU &amp; TRUST', 'HOME 10 DELTA: THE COUNT STANDS')),
        ('09.7', 'SAM', 'LINK', guest_access(), ('CONDITIONAL &middot; THE PROPOSED GUEST BRANCH', 'THE ACCESS STEP, AND WHEN IT FAILS', 'Wrong code, expired code, a new one; the evening he already has is never taken away', 'DRAWN AS A PROPOSAL, NOT A SELECTED SERVICE &middot; NO VERIFICATION MECHANISM IS ADOPTED &middot; NO ACCOUNT, NO PROFILE'),
         ('Sam', 'His link', 'Confirm the number', 'The door, once the boundary is satisfied', 'Supplied facts only', 'Occasion (guest view)', 'Nora: nothing new', 'In; or ask for a new code'), ('CONDITIONAL &middot; GUEST IDENTITY AND DELIVERY PROPOSAL', 'SHARED &middot; Notice: failed, stale', 'BRANCH V')),
    ]
    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]
    cols1[0] = cols1[0][:-6] + nomatch_inset() + '</div>'
    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2]
    cols2[3] = cols2[3][:-6] + guest_endings_inset() + '</div>'
    notes = [notecol('What board 09 shows', [
        ('ONE RECIPIENT, RESOLVED', N('09.1 to 09.3 finish the sequence 02.2 starts: the sheet lists only people Maya is already connected with, two friends called Nora are told apart by how she knows them, a mistyped name simply finds nobody, the preview is the message itself, and the result is sent, not sent, or not yet known. Her words are never rewritten on the way.')),
        ('HER OWN SHARE, AFTERWARDS', N('09.4 and 09.5 are the sender&rsquo;s operation, which the recipient&rsquo;s aftermath on 04.9 does not cover. The confirmation says what taking it back does before she does it, and the result says what survives: Nora&rsquo;s reply, Priya&rsquo;s note and Maya&rsquo;s own photograph. Failure is stated plainly and changes nothing.')),
        ('LESS OF SOMETHING', N('09.6 draws entry and effect for the four controls this project has already named, and what none of them does. It adopts no policy: the ruling on block, mute, disconnect and report is still the founder&rsquo;s, and the account-wide versions belong to You &amp; Trust.')),
        ('THE GUEST STEP, CONDITIONALLY', N('09.7 exists only as the proposed guest branch. It draws the boundary as already described, a wrong code, an expired code, a new one, a changed or reopened invitation and an unavailable ending. It selects no verification mechanism and grants nothing: the evening Sam already has is never taken away by a failed code.')),
        ('NOT ON THE MAIN ROUTE', N('These are control and recovery states beside the selected experience, not new steps in it. Board 06&rsquo;s routes are unchanged; the seven slots here are counted in the budget note on 00.')),
    ], w=430)]
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols1) + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">HER OWN SHARE, THE CONTROLS, AND THE GUEST STEP</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Edit or take it back; want less of this; the door, if the guest branch is selected</div></div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols2) + ''.join(notes) + '</div>'
            + '<div style="height: 40px;"></div>' + blk('THE DIVISION, AGREED WITH YOU &amp; TRUST AND LIFE', tbl(['WHAT', 'WHO OWNS IT', 'THE RULE'], DIVISION)
                + N('You &amp; Trust became its own visual-first project on September 12. This table is Social&rsquo;s side of the boundary, offered to that owner: Social draws the deliberate, per-share face and the controls where a person meets them; You &amp; Trust owns the account-wide settings and the service relationship; Life keeps the record. No competing biography, no occasion profile, no engagement score anywhere.'))
            + '<div style="height: 34px;"></div>' + blk('COVERAGE &middot; SEPTEMBER 12 ASSIGNMENT', tbl(['ITEM', 'WHERE', 'STATUS', 'OWNER', 'REMAINING DEPENDENCY'], COVER)))
    return (HEAD_VDL + f'<div style="width: 2260px; min-height: {hh("09")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 09 &middot; SENDING, ACCESS AND CONTROL &middot; {STAMP}', '09 &middot; Sending, access and control',
                   'The compact sender, access and control canvas the September 12 assignment asks for. Seven slots: one eligible recipient resolved, told apart and corrected; the exact outgoing material and Send; the result, truthful in three ways; the sender&rsquo;s own edit and withdrawal with what survives it; the four supported controls and what they actually do; and the guest access step, drawn only as the proposed branch. Receiving still costs the recipient nothing, and no policy is adopted here.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

FILES = {'09 - Sending, access and control': board09}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
