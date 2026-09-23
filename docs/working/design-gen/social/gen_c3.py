"""Checkpoint 2 · board 03 · Experience B · An easier way to get together. Eight slots; fixture copy only. Nothing here is ruled."""
import os, sys
from gen_c2 import *
from gen_c2 import HP
sys.path.insert(0, HP)
from gen_generous import ending as week_ending, arow, orientation as _orient
from gen_generous3 import COLD, fact, u2
from gen_artifact import ways_seq_card
from kit import anchor_row, orientation, crown, row, dm

def linkframe(inner, url='vesper.app/d/7k2m'):
    bar = (f'<div style="display: flex; align-items: center; gap: 8px; padding: 12px 14px; border-bottom: 1px solid rgba(27,23,20,0.08);">'
           f'<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><rect x="2" y="5" width="8" height="6" rx="1.2" stroke="{MUTE}" stroke-width="1.2"/><path d="M4 5V3.5a2 2 0 014 0V5" stroke="{MUTE}" stroke-width="1.2"/></svg>'
           f'<span style="{MONO} font-size: 10px; letter-spacing: 0.6px; color: {MUTE};">{url}</span><span class="fn" style="margin-left: auto; color: {GHOST};">NO APP</span></div>')
    return f'<div style="width: 393px; background: {PAPER}; {SANS} color: {INK}; display: flex; flex-direction: column; box-sizing: border-box; border: 1px solid rgba(27,23,20,0.06);">{bar}{inner}<div style="flex-grow: 1;"></div><div style="padding: 14px 22px 18px 22px; border-top: 1px solid rgba(27,23,20,0.06);"><div class="fn" style="color: {GHOST};">YOUR LINK &middot; FROM NORA</div></div></div>'
def guestbar(t):
    return f'<div style="padding: 20px 22px 0 22px;"><div class="kick" style="color: {GOLDD};">{t}</div></div>'
def pill(t, primary=True):
    return (f'<span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 11px 20px; font-size: 15px; font-weight: 600;">{t}</span>' if primary
            else f'<span style="border: 1px solid rgba(27,23,20,0.18); color: {INK}; border-radius: 999px; padding: 10px 18px; font-size: 15px; font-weight: 500;">{t}</span>')
def preview_card(kick, t, lines, note=''):
    body = ''.join(f'<div style="font-size: 14px; line-height: 20px; color: {INK2};">{l}</div>' for l in lines)
    return card(f'<div class="kick" style="color: {GOLDD};">{kick}</div>' + title(t, 18, 23, 600) + f'<div style="margin-top: 6px; display: flex; flex-direction: column; gap: 2px;">{body}</div>' + (meta(note, 8) if note else ''))
def person_row(letter, name, state, last=False):
    return arow(f'{name} &middot; <span style="color: #6E6862;">{state}</span>', avatars=[letter], last=last)
def contribution(letter, who, when, words, media='', scope=''):
    return card((media or '') + author_row(letter, who, when) + f'<div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 8px;">{words}</div>' + (meta(scope, 8) if scope else ''))

# ───────────────────────────── 03.1 · host once ─────────────────────────────
def host_phone():
    inner = chat_head('THURSDAY 8:20 PM')
    inner += gut(bubble('Pasta trial night at mine Saturday at seven. Invite Maya and Sam. Sam can come at seven-thirty; nothing to bring.') + f'<div style="display: flex; justify-content: flex-end; margin-top: 8px;"><div style="font-size: 12.5px; color: {MUTE};">Sam isn&rsquo;t on Vesper. Text him? <span style="color: {INK};">917 555 0143</span> &middot; typed, not found</div></div>', top=26)
    inner += gut(answer('Here&rsquo;s what Maya and Sam would get. Nothing is sent yet.'), top=18)
    inner += gut(dci('InviteCard', 230, view='host', kicker='TO MAYA · EVERYTHING', title='Pasta trial night at Nora’s',
                     lines='WHEN=Saturday from seven;WHERE=Court Street, 3F|the buzzer says N;WITH=Sam;BRING=Nothing',
                     stamp='MAYA CAN ANSWER, SUGGEST, OR JUST COME')
                 + '<div style="height: 12px;"></div>'
                 + dci('InviteCard', 270, view='host', kicker='TO SAM · DINNER ONLY · A LINK, NO APP', title='Pasta trial night at Nora’s',
                       lines='WHEN=Saturday, dinner from seven|come at seven-thirty;WHERE=Carroll Gardens|the exact address after he confirms this number;WITH=Nora and Maya;BRING=Nothing',
                       via='BY TEXT · TO THE NUMBER YOU TYPED', stamp='HE SEES WHEN, WHERE, WHO · NOTHING ELSE OF YOURS · NO CONTACTS SCANNED'), top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 14px;">{pill("Send to Maya and Sam")}{pill("Not yet", False)}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">To change a scope, say it: &ldquo;just dinner for Maya too.&rdquo;</div>', top=18)
    inner += gut(composer('Say it'), top=22)
    return phone(inner, 0, active='Chat')

# ───────────────────────────── 03.2 · Sam's link ─────────────────────────────
def sam_invite():
    """03.2 on the shared InviteCard (view guest, shape pill). The link page's bar and footer stay local."""
    inner = '<div style="padding: 20px 22px 0 22px;">' + dci('InviteCard', 640, view='guest', shape='pill', kicker='FROM NORA · A LINK · NOTHING TO INSTALL',
                title='Pasta trial night. Saturday from seven; come at seven-thirty.',
                note='“Second attempt at the Sorrento thing. Maya’s coming. Bring nothing, honestly.”', noteBy='NORA, THURSDAY',
                lines='Saturday Sep 19 · dinner from seven|you’re expected around seven-thirty;Carroll Gardens, near Court Street|the exact address after a one-time code to this number;With Nora and Maya|',
                **{'from': 'Nora'},
                guestNote='Nora sees your answer as yours once you confirm this number, the same step that unlocks the address. No reason needed either way.',
                answer='I’ll need to leave by nine', stamp='ANYTHING SHE SHOULD KNOW · OPTIONAL · GOES TO NORA ONLY') + '</div>'
    return linkframe(inner)

# ───────────────────────────── 03.3 · Dana contributes from Sorrento ─────────────────────────────
def dana_phone():
    inner = anchor_row('SORRENTO &middot; FRIDAY', '6:10 PM')
    inner += orientation('Warm evening. Nothing needs you.', 'Nora wrote about Saturday.')
    inner += sect('Addressed to you') + gut(card(f'<div class="kick" style="color: {GOLDD};">NORA &middot; FRIDAY &middot; TO YOU</div>' + f'<div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK}; margin-top: 6px;">&ldquo;Not coming, I know. But send me your rag&ugrave; thing if you have a sec, I&rsquo;m doing the Sorrento pasta Saturday.&rdquo;</div>' + meta('SATURDAY&rsquo;S DINNER &middot; YOU&rsquo;RE NOT EXPECTED &middot; SEND ONE THING, IF YOU LIKE', 8)))
    inner += gut(f'<div style="background: {CARD}; border-radius: 18px 18px 0 0; box-shadow: 0 -8px 24px rgba(27,23,20,0.14); padding: 14px 22px 22px 22px;"><div style="width: 36px; height: 4px; border-radius: 2px; background: rgba(27,23,20,0.15); margin: 0 auto 14px auto;"></div>'
                 + title('Send one thing to the dinner', 19, 24, 600)
                 + f'<div style="margin-top: 12px; border-radius: 12px; overflow: hidden;">{standin(150, "THE RAG&Ugrave; &middot; WEDNESDAY &middot; STAND-IN")}</div>'
                 + f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0; margin-top: 10px;"><span style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Brown the soffritto slower than feels right. Twenty minutes, not ten.</span></div>'
                 + f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">To Nora, Maya and Sam.</div>'
                 + f'<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px;">{pill("Send")}{pill("Not now", False)}</div></div>', top=26)
    return phone(inner, 0)

# ───────────────────────────── 03.4 · Nora's dinner page, Friday ─────────────────────────────
def occasion_phone():
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SATURDAY</span><span class="fn" style="margin-left: auto;">FRIDAY 7:30 PM</span></div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 26px; line-height: 32px; letter-spacing: -0.2px;">Pasta trial night. From seven, at yours.</div><div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 8px;">Maya and Sam. Nothing for anyone to bring.</div>', top=14)
    inner += sect('People') + gut('<div>' + person_row('M', 'Maya', 'in &middot; the Print Room first, she says') + person_row('S', 'Sam', 'in, confirmed 8:40 pm &middot; from seven-thirty &middot; leaves by nine') + person_row('D', 'Dana', 'not coming &middot; sent one thing', last=True) + '</div>')
    inner += sect('What people sent') + gut(contribution('D', 'Dana', 'FRIDAY &middot; FROM SORRENTO', 'Brown the soffritto slower than feels right. Twenty minutes, not ten.', media=f'<div style="border-radius: 12px; overflow: hidden; margin-bottom: 10px;">{standin(140, "DANA&rsquo;S RAG&Ugrave; &middot; STAND-IN")}</div>', scope='TO THE DINNER&rsquo;S PEOPLE &middot; HERS TO TAKE BACK')
                                          + '<div style="height: 14px;"></div>'
                                          + contribution('M', 'Maya', 'FRIDAY', 'If you go to the Print Room before dinner, the side room is the one. It empties after four and the shop shuts at five.', scope='A SUGGESTION FOR YOUR AFTERNOON &middot; NOT A CHANGE TO THE DINNER'))
    inner += gut(f'<div style="{SERIF} font-style: italic; font-size: 16px; line-height: 22px; color: {INK2};">Nothing to do. Say it if anything changes.</div>' + composer('Say it'), top=26)
    return phone(inner, 0)

# ───────────────────────────── 03.5 · Nora's Home, Saturday 1:12 pm (copy of R11 Sunday) ─────────────────────────────
WEEK_SAT = [('SAT', dm('solid', INK), 'today', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), 'dentist', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE)]
def home_saturday(branch='unadopted'):
    inner = anchor_row('NEW YORK &middot; SATURDAY', '1:44 PM')
    inner += orientation('Clear, 64&deg;. Dinner at seven, at yours.', 'Maya and Sam &middot; Sam from seven-thirty &middot; nothing to bring.')
    draft = (f'<div style="margin-top: 14px; border: 1px dashed rgba(27,23,20,0.30); border-radius: 10px; padding: 12px 14px;">'
             f'<div class="kickm" style="margin-bottom: 6px;">PREPARED &middot; NOT SENT</div>'
             f'<div style="font-size: 13px; color: {MUTE}; margin-bottom: 6px;">To Maya</div>'
             f'<div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK};">We&rsquo;ll start at seven. Would joining at eight work for you?</div>'
             f'<div style="display: flex; align-items: center; gap: 14px; margin-top: 12px;">{pill("Send proposal")}{door("Edit", MUTE)}</div>'
             f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 10px;">Sending asks Maya. It does not move dinner or answer for her.</div></div>')
    ask = card(f'<div class="kick" style="color: {GOLDD};">MAYA &middot; 1:40 PM</div>' + title('Maya asks: eight instead of seven?', 20, 25, 600)
               + f'<div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 8px;">Dinner starts at seven and the rest of the evening is unchanged. The useful question is whether joining at eight works for her.</div>'
               + f'<div style="display: flex; align-items: center; gap: 12px; margin-top: 14px;">{door("Ask Maya about joining at eight&hellip;")}</div>'
               + draft
               + f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 10px;">Leave it: nothing is sent and seven still stands.</div>')
    inner += gut(ask, top=22)
    inner += gut(ways_seq_card('This afternoon, if you want it', [('4:00', 'The Print Room, the side room', 'Maya says it empties after four and the shop shuts at five.', 'MAYA&rsquo;S SUGGESTION'), ('4:45', 'Home on foot by 5:10', 'Twenty minutes. The pasta from six.', 'YOUR WORDS')],
                              meta_t='The cost: your only free stretch this afternoon, and Maya cannot join until dinner. Listed hours 12&ndash;6, not checked today.'), top=18)
    inner += sect('In motion') + gut('<div>' + person_row('S', 'Sam', 'in &middot; from seven-thirty &middot; leaves by nine') + person_row('D', 'Dana', 'sent the rag&ugrave;, from Sorrento') + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True) + '</div>')
    inner += sect('Worth knowing') + gut(COLD())
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>')
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += week_ending(WEEK_SAT, 'Tonight, the pasta. Seven, at yours.')
    return phone(inner, 0)

# ───────────────────────────── 03.6 · Sam, the adopted branch ─────────────────────────────
def sam_adopted():
    inner = guestbar('FROM NORA &middot; SATURDAY 2:05 PM')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Dinner moved to eight.</div>', top=14)
    inner += gut('<div>' + row('Dinner now from eight &middot; <span style="color: #6E6862;">same place</span>', mark='solid', color=GOLD)
                 + row('Nora still has your seven-thirty and nine &middot; <span style="color: #6E6862;">until you say otherwise</span>', mark='hollow')
                 + row('Maya and Nora have the new time &middot; <span style="color: #6E6862;">the dinner page updated for everyone</span>', mark='hollow', last=True) + '</div>', top=16)
    inner += gut(f'<div style="{SERIF} font-size: 16px; line-height: 23px; color: {INK2};">&ldquo;Maya can&rsquo;t make seven. Eight gives you an hour; sorry about that.&rdquo;</div><div class="fn" style="margin-top: 6px; color: {ANCHOR};">NORA</div>', top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 14px;">{pill("Eight works")}{pill("Can&rsquo;t do eight", False)}</div><div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">If you don&rsquo;t answer, she won&rsquo;t assume yes; she keeps your seven-thirty and nine.</div>', top=24)
    return linkframe(inner)

# ───────────────────────────── 03.7 · Sam arrives ─────────────────────────────
def sam_arrival(start='seven'):
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
            f'<div style="{SERIF} font-weight: 600; font-size: 16px; line-height: 21px;">Dinner from eight.</div>'
            f'<div style="display: flex; flex-direction: column; gap: 4px; font-size: 12.5px; line-height: 17px; color: {INK2};"><div><span class="fn" style="color: {ANCHOR};">IF HE ANSWERED &ldquo;EIGHT WORKS&rdquo; &middot; </span>You&rsquo;re expected around eight. Leaving by nine is fine; she knows it&rsquo;s an hour.</div>'
            f'<div><span class="fn" style="color: {ANCHOR};">IF HE HAS NOT ANSWERED &middot; </span>Nora has you at seven-thirty, leaving by nine. Come when you said; the door is the same.</div></div>'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2};">Court Street, 3F, the buzzer says N &middot; nothing to bring &middot; Dana&rsquo;s rag&ugrave; &middot; one line if late.</div>'
            f'<div class="fn" style="color: {ANCHOR};">THE DINNER&rsquo;S START IS EIGHT; HIS ACCEPTED ARRIVAL IS ONLY WHAT HE SAID &middot; WHO HAS THE NEW TIME: NORA (OWNER), MAYA (PROPOSED IT), SAM (AFFECTED); DANA UNCHANGED &middot; HIS SILENCE IS NOT ACCEPTANCE OF EIGHT</div>'
            f'<div class="fn" style="color: {OX};">NORA&rsquo;S DINNER PAGE, ADOPTED BRANCH: SAM &middot; IN &middot; SEVEN-THIRTY, LEAVES BY NINE &middot; NO ANSWER ON EIGHT (PLANS 05 D3: WHO IS AFFECTED, WHO HAS ANSWERED)</div></div>')

def provisional_inset():
    """The host's provisional state before Sam confirms: an inset beside 03.4, not a slot."""
    return (f'<div style="margin-top: 14px; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div class="kickm">EARLIER FRIDAY &middot; PROVISIONAL &middot; THE SAME 03.4 BEFORE SAM CONFIRMS</div>'
            f'<div>' + person_row('S', 'Sam', 'answered &ldquo;in&rdquo; from the link &middot; not yet confirmed &middot; the address waits', last=True) + '</div>'
            f'<div class="fn" style="color: {ANCHOR};">A LINK-HOLDER RESPONSE IS PROVISIONAL UNTIL THE ONE-TIME CODE TO THE NUMBER NORA TYPED; THE SAME CODE UNLOCKS THE ADDRESS. IF IT NEVER HAPPENS, NORA NEVER SEES A CONFIRMED &ldquo;IN&rdquo;. A DECLINE OR A PRIVATE LINE FOLLOWS THE SAME RULE</div></div>')

def first_host_inset():
    """The first evening: 03.1 when the address is not yet known. Reuse what is known, ask only the missing fact, once, then the same previews."""
    known = ('<div class="vdl-t-supportLine" style="color: #3C352E;">Already known and reused, not asked again: Saturday, seven, Maya, Sam and the number you typed, nothing to bring.</div>')
    ask = ('<div style="display: flex; flex-direction: column; gap: 8px;">'
           '<div style="align-self: flex-start; max-width: 300px; font-family: var(--vk-font-serif); font-size: 16px; line-height: 22px; color: #1B1714;">One thing before the previews: which address should Maya get?</div>'
           '<div style="align-self: flex-end; max-width: 260px; background: #4A3428; color: #FBF7EC; border-radius: 18px; padding: 9px 14px; font-size: 14px; line-height: 19px;">court st 3F, the buzzer says N</div></div>')
    back = '<div class="vdl-t-supportLine" style="color: #3C352E;">Then the same two previews and <b>Send to Maya and Sam</b>, with her words and choices as she wrote them. Next time the address is already known.</div>'
    return inset('03.1, THE FIRST EVENING &middot; ONE MISSING FACT, ASKED ONCE', known + ask + back,
                 'NOT A PROFILE, A CONTACTS IMPORT OR A SETUP FLOW &middot; THE SAME CHAT, ONE ANSWER &middot; COUNTED IN THE WORK TABLE BELOW &middot; GUEST VERIFICATION, RECOVERY AND UNAVAILABLE ACCESS REMAIN NAMED DEPENDENCIES')

def offline_note():
    return (f'<div style="width: 393px; flex: none; border-radius: 8px; border: 1px dashed rgba(27,23,20,0.28); padding: 22px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px; min-height: 420px;">'
            f'<div class="kick" style="color: {MUTE};">03.8 &middot; STORYBOARD &middot; NO SCREEN</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 28px;">The evening, with the phones away</div>'
            f'<div style="{SERIF} font-size: 16px; line-height: 24px; color: {INK2};">7:32 &middot; Sam finds the buzzer. Nora opens the door before he presses it.<br><br>8:05 &middot; Maya arrives at eight, as she said she would, and eats with them.<br><br>8:25 &middot; The rag&ugrave; is Dana&rsquo;s. Someone photographs the table; it is Maya.<br><br>8:40 &middot; Sam says he has to go at nine and nobody makes it a thing.<br><br>9:02 &middot; He leaves. There is no button for that.</div>'
            f'<div class="fn" style="color: {ANCHOR}; margin-top: auto;">THE UNCHANGED-SEVEN BRANCH: SEVEN STANDS, SO MAYA COMES AT EIGHT AS 03.5 SAYS &middot; NO APP ACTION TO ARRIVE, EAT, OR LEAVE &middot; THE TABLE PHOTOGRAPH IS 04.1, AT 8:25</div></div>')

WORK = [
    ['Nora &middot; the host', 'Writes the invitation once, pastes it into two threads and cuts the address out of Sam&rsquo;s by hand. The address is already in her earlier messages to Maya, so she reuses it; search finds Dana&rsquo;s tip. She forwards Dana&rsquo;s photograph and tip to both threads, reads three answers across two threads, and remembers Sam&rsquo;s nine herself when Maya asks about eight. Two weeks later she scrolls up and copies the last invitation', 'The first evening asks her one thing, the address, once (03.1 inset); every evening after, one sentence and one Send, with a preview per recipient (03.1). The answers and contributions arrive on one page, attributed (03.4). Maya&rsquo;s ask arrives with the facts it touches (03.5). Two weeks later the draft already holds the address, the buzzer, the photograph and the dish (04.8)', 'Hand-editing a second version for a guest; reading three threads as one evening; carrying a constraint into a change. Not retyping: a competent thread reuses the address too', 'Choosing the food, cooking it, and saying the invitation in her own words'],
    ['Maya &middot; a friend', 'Sends the photograph in one thread and, if she wants the evening to see it, again in the dinner thread; asks about eight where everyone is reading', 'Shares once from the object itself (02.2); her suggestion lands under the dinner row as a suggestion (03.4); her ask reaches the owner as a decision, not a demand in front of the group (03.5)', 'Sending the same thing twice; a private suggestion read publicly', 'Deciding to share at all, and what to say. She owes no reply, no photograph and no answer'],
    ['Sam &middot; a guest with no account', 'Gets a clear text with when and roughly where; asks for the exact address and the buzzer on the day; says he must leave by nine and says it again if the time changes', 'Opens a link and answers once; confirms his number when the address is needed (03.2, 03.4); the arrival view carries the door, the time and his nine (03.7)', 'Asking for the door on the night, and repeating his own constraint. A good text already answers when and roughly where', 'Deciding whether to come, and saying when he has to go'],
    ['Dana &middot; elsewhere, not attending', 'Nora asks; Dana sends a photograph and a paragraph; Nora forwards both and explains them again', 'One addressed line reaches her; she sends one thing to the dinner&rsquo;s people, attributed, without joining (03.3)', 'The forwarding and re-explaining; her name stays on her contribution', 'Choosing to send something at all. She is owed nothing back'],
    ['The honest total', 'A competent message thread, with search, links and a reused address, does most of this, and everyone already has one', 'What remains: two recipient-specific versions from one sentence; one attributed page instead of three threads; a constraint carried into a change; an arrival view for a person with no account; and a first evening that asks for the address once', 'Assembly and coordination, unevenly: Nora gains most, the recipients only what they use', 'Nothing here removes cooking, choosing, or writing to a friend, and nobody owes equal effort'],
]
FIXTURE_NOTE = ('The fixture hands Vesper the address, the buzzer, Sam&rsquo;s number, Dana&rsquo;s dish and last month&rsquo;s photograph already assembled. '
                'The first-host step on 03.1 now shows the one thing a real first evening must ask, the address, once; it is counted in Nora&rsquo;s row. '
                'The baseline is given the same competence as 05 D7&rsquo;s: search, existing links and a reused address. Vesper is credited only with assembly and coordination it actually removes, not with retyping the thread would not have to do.')

def board03():
    P1 = [
        ('03.1', 'NORA', 'CHAT', host_phone(), ('THURSDAY 8:20 PM', 'HOST ONCE, NOT A WIZARD', 'One sentence; what Maya gets, what Sam gets; one Send', 'THE PREVIEW IS A USABLE INVITATION, NOT A PERMISSIONS WORKSHEET &middot; A SCOPE IS CORRECTED IN LANGUAGE'),
         ('Nora', 'One sentence to Vesper', 'Say it once', 'Two previews, one per recipient', 'Nothing sent yet', 'Occasion (owner: Nora)', 'Two previews', 'Send; or Not yet'), ('SEVEN SENTENCES &middot; RULED', 'SHARED &middot; InviteCard host &times;2 &middot; vdl-stage1 0.4.1 &middot; LABELLED FACTS AS REVIEWED ON 02B', 'THE READBACK IS ONE LINE ON HOME, NOT A PHONE')),
        ('03.2', 'SAM', 'LINK', sam_invite(), ('FRIDAY &middot; A LINK, NO APP', 'GUEST VALUE BEFORE ADOPTION', 'The evening, who, when, the neighborhood; I&rsquo;m in or can&rsquo;t', 'NO PROFILE &middot; NO REASON ASKED &middot; THE EXACT ADDRESS ONLY AFTER A ONE-TIME CODE TO HIS NUMBER &middot; HIS NINE IN HIS OWN WORDS'),
         ('Sam', 'A link, no app', 'Open, answer', 'Understands the evening and his time', 'Nora sees a provisional answer; confirmed by the same code that unlocks the address', 'Occasion (guest view)', '&mdash;', 'I&rsquo;m in; or can&rsquo;t'), ('SHARED &middot; InviteCard guest, pill &middot; vdl-stage1 0.4.1', 'PROPOSED BRANCH V: VERIFIED AT THE FIRST SENSITIVE BOUNDARY (THE ADDRESS)', 'DEPENDENCY &middot; GUEST IDENTITY AND DELIVERY')),
        ('03.3', 'DANA', 'HOME', dana_phone(), ('FRIDAY 6:10 PM &middot; SORRENTO', 'DANA CONTRIBUTES', 'Nora&rsquo;s line to her; one thing sent to the dinner&rsquo;s people', 'HER GESTURE AND ITS SCOPE, NOT A TIP THAT ARRIVES BY MAGIC &middot; NOT ENROLLED, NO ADDRESS, NO ANSWERS'),
         ('Dana', 'Nora&rsquo;s Friday line, addressed', 'Send one thing', 'A way to be part of the dinner without attending', 'The dinner&rsquo;s people; not the address', 'Contribution', 'Nora, Maya, Sam see it under the row', 'Done; nothing asked of her'), ('B1&prime; &middot; NORA&rsquo;S FRIDAY LINE (LEDGER)', 'DEPENDENCY &middot; A CONTRIBUTOR PATH OUTSIDE MEMBERSHIP', 'FIXTURE')),
        ('03.4', 'NORA', 'OCCASION', occasion_phone(), ('FRIDAY 8:45 PM', 'THE DINNER, AS ONE PAGE', 'Who is in (Sam confirmed), and what people sent, attributed', 'NO COPY-AND-PASTE FOR THE HOST &middot; MAYA&rsquo;S SUGGESTION IS NOT A CHANGE &middot; THE PROVISIONAL STATE BEFORE SAM CONFIRMED IS THE INSET BELOW'),
         ('Nora', 'Home &rarr; the dinner', 'Read', 'Everything that arrived, in place', 'Each contribution at its scope', 'Occasion', 'Each attributed', 'Nothing to do'), ('SEVEN SENTENCES &middot; RULED', 'B2A, B2B, B2C SHOWN', 'FIXTURE')),
    ]
    P2 = [
        ('03.5', 'NORA', 'HOME', home_saturday(), ('SATURDAY 1:44 PM &middot; FULL SCROLL', 'THE PROPOSAL, AND THE AFTERNOON', 'One door prepares one message to Maya; dinner stays at seven; the &sect;8.2 afternoon; the rest of Home intact', 'COPY OF R11 (HOME 02 SUNDAY) WITH THE SOCIAL UNITS SUBSTITUTED &middot; ONE ASK WITH A USABLE ACTION &middot; SEVEN STANDS IF SHE LEAVES IT'),
         ('Nora', 'Home', 'Read', 'The prepared alternative and its cost; a better afternoon', 'Recommended branch: dinner stays at seven in every view', 'Home / Occasion', '&mdash;', 'Leave it: seven stands'), ('COPY OF HOME 02 &middot; 09-05', 'BRANCH &middot; RECOMMENDED &middot; UNADOPTED', 'SENTENCE 6 AS AMENDED (2026-09-09): ONE DOOR MAY OPEN AN ADDRESSED, EDITABLE MESSAGE; THE PERSON SENDS &middot; PREPARE &rarr; EDITABLE MESSAGE &rarr; SEND PROPOSAL, WHICH SENDS WORDS ONLY &middot; SAM&rsquo;S DEPARTURE IS NOT IN THE MESSAGE, HE IS NOT ASKED AGAIN, AND AN UNCHANGED DINNER IS ANNOUNCED TO NOBODY &middot; IF NORA INSTEAD INSTRUCTS A CHANGE, THAT IS PLANS&rsquo; D3 PREVIEW &rarr; UPDATE &amp; SEND, NOT AN EQUAL BUTTON BESIDE THIS ONE')),
        ('03.6', 'SAM', 'LINK', sam_adopted(), ('SATURDAY 2:05 PM &middot; ADOPTED BRANCH, SEPARATE', 'WHAT CHANGED, TAILORED TO HIM', 'Nora applied eight; his seven-thirty and nine stay his until he says; everyone at the dinner has the new time', 'DRAWN ONLY FOR THE ADOPTED BRANCH &middot; THE DINNER&rsquo;S START AND HIS ACCEPTED ARRIVAL STAY DISTINCT &middot; SILENCE IS NOT ACCEPTANCE &middot; CONTINUES TO THE 03.7 VARIANT'),
         ('Sam', 'His link', 'Read', 'What changed; what Nora still has from him', 'Tailored to him; Nora and Maya have the new time too', 'Occasion (guest view)', 'Nora: his answer, or his unchanged seven-thirty and nine', 'Answer, or not; then the arrival for what he said'), ('BRANCH &middot; ADOPTED &middot; NOT THE RECOMMENDED ROUTE', 'ENTERED ONLY THROUGH THE OWNER-INSTRUCTED ROUTE (PLANS&rsquo; PREVIEW &rarr; UPDATE &amp; SEND), NEVER THROUGH 03.5&rsquo;S PROPOSAL DOOR', 'FIXTURE')),
        ('03.7', 'SAM', 'LINK', sam_arrival(), ('SATURDAY 7:10 PM &middot; UNCHANGED-SEVEN ROUTE', 'HOSPITALITY, NOT GUEST MATCHING', 'Expected around seven-thirty; find the door; nothing to bring', 'SUPPLIED FACTS ONLY &middot; DANA&rsquo;S DISH AS A FOOTHOLD &middot; ONE LINE IF LATE &middot; THE ADOPTED BRANCH&rsquo;S ARRIVAL IS THE LABELLED VARIANT BELOW'),
         ('Sam', 'His link, Saturday evening', 'Open', 'The way in, the time, that nothing is expected', 'Supplied facts only', 'Occasion (guest view)', '&mdash;', 'Phone away'), ('NEW &middot; NO SIBLING DRAWS THIS', 'D4 &middot; THE ARRIVAL FRAME &middot; BRANCH V: HIS NUMBER CONFIRMED, SO THE DOOR FACTS SHOW', 'B2D ARRIVAL UPDATE IS THE ONE DOOR')),
    ]
    cols1 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P1]
    cols1[0] = cols1[0][:-6] + first_host_inset() + '</div>'
    cols1[3] = cols1[3][:-6] + provisional_inset() + '</div>'
    cols2 = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P2] + [offline_note()]
    cols2[2] = cols2[2][:-6] + arrival_variant() + '</div>'
    notes = [notecol('What board 03 shows', [
        ('HOST ONCE', N('03.1 is one sentence. The two previews are the invitation each person will get, with the scope said in plain words; the correction path is language. The readback after Send is one line on Home, not a phone.')),
        ('THE GUEST', N('03.2, 03.6 and 03.7 are link pages with no tab bar and no account. His answer on the bare link is provisional; the one-time code to the number Nora typed confirms it and unlocks the exact address in the same step (branch V); until then Nora sees no confirmed &ldquo;in&rdquo;. His nine is in his own words. The arrival frame, parameterized by the branch in force, is the one thing no sibling project draws.')),
        ('DANA', N('03.3 is her gesture: Nora&rsquo;s Friday line reaches her as addressed material on her own Home; the sheet sends one thing to the dinner&rsquo;s people and says what it does not carry. Whether this path exists is a dependency; what she sees is design&rsquo;s to own.')),
        ('THE CHANGE, TWO BRANCHES', N('03.5 takes the amended sentence 6 (September 9): one door opens an addressed, editable message and the person sends it. The question it prepares is the useful one, since dinner still starts at seven and Sam&rsquo;s evening is unchanged: <i>We&rsquo;ll start at seven. Would joining at eight work for you?</i>, to Maya, ending in Send proposal. Sending asks her; it does not move dinner, record her answer, ask Sam again, or announce anything to anyone else, and his departure time is not in it. Leaving it sends nothing. If Nora instead instructs a change outright, that is Plans&rsquo; own preview and Update &amp; send, not a button beside this one; leaving it is the unadopted ending and seven stands in every view. 03.6 is the adopted branch, labelled: the owner applied eight, Nora, Maya and Sam each have the new time in their own view, Sam&rsquo;s row restates his nine, and his answer is not assumed. Each branch reaches its own arrival view: seven-thirty on 03.7; on the 03.7 variant the dinner&rsquo;s start is eight while his expected arrival is only what he answered, and if he answered nothing Nora keeps his seven-thirty and nine (Plans&rsquo; pending-participation treatment, 05 D3). The afternoon sits above the evening, as the review asked.')),
        ('NOT DRAWN', N('B0 is board 05&rsquo;s D1. Maya&rsquo;s own view of her unadopted proposal is the branch label on 03.5. No booking, no expense, no consensus, no guest count.')),
    ], w=430)]
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols1) + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">SATURDAY</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">The day changes, then the evening happens</div></div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(cols2) + ''.join(notes) + '</div>'
            + '<div style="height: 40px;"></div>' + blk('WHAT EACH PERSON IS LEFT DOING &middot; THE SAME EVENING BY MESSAGE AND LINK, AND AS DRAWN', tbl(['PERSON', 'BY MESSAGE AND LINK', 'AS DRAWN', 'WHAT ACTUALLY MOVED', 'WHAT NEVER MOVES'], WORK) + N(FIXTURE_NOTE)))
    return (HEAD_VDL + f'<div style="width: 2260px; min-height: {hh("03")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 03 &middot; AN EASIER WAY TO GET TOGETHER &middot; {STAMP}', '03 &middot; An easier way to get together',
                   'Can interest become a real gathering without turning leisure into planning work or making the host an unpaid operator of the app? Eight slots: host once; Sam&rsquo;s link; Dana contributing from Sorrento; the dinner as one page; Saturday&rsquo;s change on a full-scroll Home in the recommended branch; the adopted branch for Sam alone; the arrival; and the evening with the phones away.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

FILES = {'03 - An easier way to get together': board03}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
