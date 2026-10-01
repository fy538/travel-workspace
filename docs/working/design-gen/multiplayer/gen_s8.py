"""16 · Getting together, and saying who you were with. Rewritten 2026-09-22 for the threads/Life-continuity handoff:
voting is demoted to an optional instrument (§8.1, §8.5), gathering is conversation-led (§8.3), availability is never
attendance (§8.4), and "With" is split into three separate things (§8.7). Presence is a bounded expression that goes
stale (§7.1). Home/Chat frames use the sharing kit; the Life frame uses Life's grammar (board 07)."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
from gen_s1 import (status, share, post, footer, sep, CARD_CSS, composer, photo_grid, liked_by, chat_field,
                    _g, WITH_P, OPTS_P, PIN_P, CAL_P, X_P, place_card)
import gen_s6 as L6
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD16 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)
PACHA = 'pacha. unreal. my ears are still ringing'
OPEN = 'thinking hato saturday, late brunch. anyone around?'

def with_line(names, state=None):
    c = MUTE if state else INK2
    w = f'<span class="fn" style="margin-left: 6px;">{state}</span>' if state else ''
    return f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 10px; font-size: 13px; color: {c};">{_g(WITH_P, c, 14)}<span>with {names}</span>{w}</div>'
def card(inner, pad='14px 16px'): return f'<div style="{CARD_CSS} padding: {pad};">{inner}</div>'
def kick(t, color=None): return f'<div class="fn" style="{f"color: {color};" if color else ""}">{t}</div>'
def ser(t, size=19, lh=24): return f'<div style="{SERIF} font-weight: 600; font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def body(t, color=INK2, size=14, lh=20): return f'<div style="font-size: {size}px; line-height: {lh}px; color: {color};">{t}</div>'
def reply(who, when, text, quiet_=False):
    c = MUTE if quiet_ else INK
    return (f'<div style="padding: 10px 0 10px 14px; border-left: 2px solid rgba(27,23,20,0.10);">'
            f'<div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 14px; font-weight: 600; color: {c};">{who}</span><span class="fn">{when}</span></div>'
            f'<div style="font-size: 15px; line-height: 21px; color: {c}; margin-top: 3px;">{text}</div></div>')

# ── A · with ──
def a_write():
    inner = avatar_for(S.to_bar('Friends'), 'N')
    inner += gut(plain(PACHA, size=18, lh=26), top=24)
    inner += gut(photo_grid(3, 96), top=16)
    inner += gut(f'<div style="display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: {INK2};">{_g(WITH_P, INK2, 14)}<span>with <b style="font-weight: 600;">Maya</b></span>{_g(X_P, MUTE, 11)}</div>'
                 + f'<div style="margin-top: 8px;">{S.loc_row("Lower East Side")}</div>', top=14)
    inner += gut(S.toolbar(('photo', 'where', 'with')), top=28)
    return phone2(inner, active='Chat')
def a_maya():
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 11:20 AM'), 'M')
    inner += gut(card(f'<div style="display: flex; align-items: center; gap: 8px;">{_g(WITH_P, GOLDD, 15)}{kick("NORA NAMED YOU", GOLDD)}</div>'
                      + f'<div style="margin-top: 10px;">{body(PACHA, INK, 17, 24)}</div>'
                      + f'<div style="margin-top: 10px;">{photo_grid(3, 90)}</div>'
                      + f'<div class="fn" style="margin-top: 10px;">PACHA &middot; FRIDAY NIGHT &middot; TO HER FRIENDS</div>'
                      + f'<div style="margin-top: 14px; display: flex; gap: 8px;">{btn("Yes, I was there")}{btn("Leave my name off", False)}</div>'), top=20)
    return phone2(inner, active='Home')
def a_after():
    """Sept 26 (§12.2): a compact receipt under the post itself, with its scope and a correction; the shared record is a
    separate, optional door, not a screen explaining what did not happen."""
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 11:22 AM'), 'M')
    inner += gut(status(80, 'Nora', 'SATURDAY 10:52 AM · TO FRIENDS', PACHA) + with_line('Maya')
                 + f'<div style="margin-top: 12px;">{photo_grid(3, 96, "PHOTO &middot; NORA")}</div>', top=20)
    inner += gut(S.receipt('Your name is on it, for Nora&rsquo;s friends', 'Undo'), top=14)
    inner += gut(door('Also keep the night in Shared with Nora', GOLDD), top=10)
    return phone2(inner, active='Home')
def a_sam():
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 11:40 AM'), 'S')
    inner += gut(status(80, 'Nora', 'SATURDAY 10:52 AM · TO FRIENDS', PACHA) + with_line('Maya')
                 + f'<div style="margin-top: 12px;">{photo_grid(3, 108, "PHOTO &middot; NORA")}</div>' + footer('Lower East Side'), top=20)
    return phone2(inner, active='Home')
def a_life():
    inner = L6.head('SHARED RECORD &middot; SINCE 2019', 'Shared with Nora', 'Thirteen shared episodes across six years.')
    inner += L6.sec('THE SHARED RECORD', '13 EPISODES', 26)
    inner += L6.row2('Pacha, John Summit', 'The two of you &middot; you kept it here', 'SEPT 26', 'var(--green)', L6.GLASS)
    inner += L6.row1(L6.G('M1.8 8.6 L13.2 3.4 L9.8 8.2 L11.4 12 L9.6 12.4 L7.4 9.2 L3.6 10.4 Z'), 'Nice &rarr; Rome &middot; the two of you', 'AUG 14&ndash;27')
    inner += L6.row1(L6.FORK, 'Dinner in Brooklyn', 'AUG 29')
    inner += L6.door('All thirteen episodes')
    return L6.phone(inner)

# ── B · an opening, replies, settling ──
def b_open():
    inner = avatar_for(anchor_row('NEW YORK', 'THURSDAY 7:06 PM'), 'M')
    inner += gut(share('Nora', '7:02 PM · TO THE SORRENTO FOUR', OPEN, extra=place_card(good=('Late brunch',), name='Hato', where='Cobble Hill &middot; ramen &middot; from Our New York')), top=20)
    inner += gut(chat_field('Reply to everyone', ask=False), top=14)
    return phone2(inner, active='Home')
def b_replies():
    """Sept 26 (§12.2): the host's steps collapse into one prepared action beside the conversation. Settling and asking
    are one send; each person still answers for themselves."""
    inner = avatar_for(anchor_row('NEW YORK', 'THURSDAY 9:12 PM'), 'N')
    inner += gut(post('You', '7:02 PM · TO THE SORRENTO FOUR', OPEN, '', None, me='N'), top=20)
    inner += gut(reply('Maya', '7:14 PM', 'yes, after noon') + reply('Priya', '8:02 PM', 'count me in any time after 12')
                 + reply('You', '9:10 PM', 'perfect, 12:30 then'), top=12)
    inner += gut(card(f'<div style="display: flex; align-items: baseline; gap: 10px;">{ser("Saturday, 12:30 at Hato", 17, 22)}</div>'
                      + f'<div class="fn" style="margin-top: 4px;">TO THE SORRENTO FOUR</div>'
                      + f'<div style="margin-top: 12px; display: flex; gap: 8px; align-items: center;">{btn("Send as the plan")}{door("Edit", MUTE)}</div>'), top=14)
    return phone2(inner, active='Home')
def b_invite():
    g = card(f'{kick("GATHERING &middot; SATURDAY")}{ser("Brunch at Hato")}'
             + f'<div style="margin-top: 6px;">{body("12:30 &middot; Cobble Hill")}</div>'
             + f'<div style="margin-top: 10px;">{body("You said: yes, after noon", MUTE, 13, 18)}</div>'
             + f'<div style="display: flex; gap: 8px; align-items: center; margin-top: 12px;">{btn("I&rsquo;m in")}{btn("Can&rsquo;t make it", False)}</div>')
    inner = avatar_for(anchor_row('NEW YORK', 'THURSDAY 9:16 PM'), 'M')
    inner += gut(share('Nora', '9:15 PM · TO THE SORRENTO FOUR', 'saturday 12:30 at hato. come if you can', extra=g), top=20)
    return phone2(inner, active='Home')
def b_conditional():
    g = card(f'{kick("GATHERING &middot; SATURDAY")}{ser("Brunch at Hato")}'
             + f'<div style="margin-top: 6px;">{body("12:30 &middot; Cobble Hill")}</div>'
             + f'<div style="margin-top: 12px; display: flex; align-items: center; gap: 8px;">{facepile(["N","P"], 20, -6)}<span style="font-size: 13px; color: {INK2};">Nora and you are in</span></div>'
             + f'<div style="margin-top: 10px;">{body("In &middot; you said any time after 12", GREEN, 13, 19)}</div>'
             + f'<div style="margin-top: 12px;">{btn("Change that", False)}</div>')
    inner = avatar_for(anchor_row('NEW YORK', 'THURSDAY 9:16 PM'), 'P')
    inner += gut(share('Nora', '9:15 PM · TO THE SORRENTO FOUR', 'saturday 12:30 at hato. come if you can', extra=g), top=20)
    return phone2(inner, active='Home')
def b_quiet():
    """Sept 26 (§12.2, §12.8): on the day. Only who is in; nobody's silence is shown. A detail changes through the person
    who holds it (Priya has the table), and the plan carries it; one prepared message if you are late."""
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 12:20 PM'), 'M')
    inner += gut(card(f'{kick("TODAY &middot; 12:30")}{ser("Brunch at Hato")}'
                      + f'<div style="margin-top: 6px;">{body("Cobble Hill")}</div>'
                      + f'<div style="margin-top: 12px; border-top: 1px solid rgba(27,23,20,0.08); padding-top: 10px; display: flex; gap: 10px; align-items: flex-start;">'
                      + f'{_g(PIN_P, GOLDD, 15)}<div><div style="font-size: 14.5px; line-height: 20px; color: {INK};">Upstairs, the back table</div>'
                      + f'<div class="fn" style="margin-top: 2px;">FROM PRIYA &middot; 12:14 PM &middot; SHE HAS THE TABLE</div></div></div>'
                      + f'<div style="margin-top: 12px; display: flex; align-items: center; gap: 8px;">{facepile(["N","P","M"], 20, -6)}<span style="font-size: 13px; color: {INK2};">Nora, Priya and you are in</span></div>'
                      + f'<div style="margin-top: 12px;">{door("Running late? Tell them", GOLDD)}</div>'), top=20)
    return phone2(inner, active='Home')
def b_chat():
    """Sept 26 decision, item 13: sending the plan opens the occasion's group chat, on by default, for everyone invited.
    The plan sits at the top; Vesper only when asked (the gold spark in the composer)."""
    inner = bar('BRUNCH AT HATO', 'SATURDAY 12:02 PM')
    inner += gut(f'<div style="{S.CARD_CSS} padding: 11px 0;"><div class="fn">THE PLAN</div>'
                 f'<div style="font-size: 14.5px; line-height: 20px; color: {INK}; margin-top: 3px;">Saturday 12:30 &middot; Hato, upstairs</div>'
                 f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">Nora, Priya and Maya are in</div></div>', top=14)
    inner += gut(bubble_in('grabbing the table upstairs', 'Priya'), top=14)
    inner += gut(bubble_in('ten minutes late. order me the buns', 'Maya'), top=8)
    inner += gut(bubble('on it'), top=8)
    inner += gut(chat_field('Message the brunch'), top=16)
    return phone2(inner, active='Chat')
def c_tool():
    rows = ''
    for t, who in (('Thu 18th', ('M', 'P')), ('Fri 19th', ('M', 'P', 'D', 'S')), ('Sat 20th', ('D',))):
        rows += (f'<div style="display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid rgba(27,23,20,0.07);">'
                 f'<span style="font-size: 15px; font-weight: 600; color: {INK}; width: 92px;">{t}</span>'
                 f'<span style="margin-left: auto; display: inline-flex; align-items: center; gap: 8px;">{facepile(list(who), 20, -6)}<span class="fn">{len(who)} free</span></span></div>')
    inner = avatar_for(anchor_row('NEW YORK', 'MONDAY 8:40 AM'), 'N')
    inner += gut(card(f'{kick("YOU ASKED FOR TIMES &middot; SIX PEOPLE")}{ser("Which evenings work?")}'
                      + f'<div style="margin-top: 10px;">{rows}</div>'
                      + f'<div style="margin-top: 10px;">{body("Who is free, nothing more. No winner, and nobody is in until you ask them and they answer.", MUTE, 13, 19)}</div>'
                      + f'<div style="margin-top: 12px; display: flex; gap: 8px;">{btn("Settle on the 19th")}{btn("Close this", False)}</div>'), top=20)
    return phone2(inner, active='Home')

# ── D · a bounded expression, and its staleness ──
def d_now():
    inner = avatar_for(S.to_bar('Friends'), 'N')
    inner += gut(plain('around brooklyn all weekend, nothing planned. happy for company', size=18, lh=26), top=24)
    inner += gut(card(f'{kick("UNTIL SUNDAY NIGHT")}{body("After that it stops showing. Saying where you are is one line you write, not something that keeps running.", INK2, 14, 20)}'), top=16)
    inner += gut(S.loc_row('Brooklyn'), top=14)
    inner += gut(S.toolbar(('where', 'when')), top=24)
    return phone2(inner, active='Chat')
def d_stale():
    inner = avatar_for(anchor_row('NEW YORK', 'TUESDAY 9:10 AM'), 'S')
    inner += gut(f'<div style="opacity: 0.55;">{status(80, "Nora", "SATURDAY · TO FRIENDS", "around brooklyn all weekend, nothing planned. happy for company")}</div>'
                 + f'<div style="margin-top: 10px;">{body("That was for last weekend.", MUTE, 13, 18)}</div>', top=20)
    inner += sep() + gut(share('Priya', 'MONDAY 6:02 PM · TO FRIENDS', 'at the market until noon if anyone is near', where='Grand Army Plaza'), top=18)
    return phone2(inner, active='Home')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'
def sechead(k, t, sub):
    return f'<div style="margin-top: 32px;"><div class="kick" style="color: {GOLDD};">{k}</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 29px; margin-top: 4px;">{t}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px; max-width: 1200px;">{sub}</div></div>'

def build():
    sA = sechead('A', 'Saying who you were with', 'Three separate things, kept separate: whether she was there, whether her name shows on your post, and whether the night goes into what the two of you share. One answer from her settles the first two; the third stays her choice, later.')
    rA = rowdiv([cell('SATURDAY 10:52 AM', 'A1', 'Written, with Maya', 'The people icon names who you were with. It asks her; it does not publish her name or file anything.', a_write(), (P('WITH'), P('SENDER'))),
                 cell('SATURDAY 11:20 AM', 'A2', 'Maya is asked, once', 'Two answers, and both are complete: yes I was there, or leave my name off. No inbox, no third question.', a_maya(), (P('WITH'), P('NAMED'))),
                 cell('SATURDAY 11:22 AM', 'A3', 'A receipt, not a screen', 'Her yes leaves one line under the post, with an undo. Keeping the night in what they share is a separate door.', a_after(), (P('WITH'), P('NAMED'))),
                 cell('SATURDAY 11:40 AM', 'A4', 'What Sam sees', 'A line under the words. Nobody is pinned to a photograph, and Sam is told nothing about records.', a_sam(), (P('WITH'), P('RECEIVER')))], top=16)
    rA2 = rowdiv([cell('MAYA&rsquo;S LIFE', 'A5', 'Only because she kept it', 'If she taps the third door, the night joins the record she shares with Nora, marked as hers to keep. If she never does, this row never appears.', a_life(), (P('WITH'), LIFE))])
    sB = sechead('B', 'Getting together, without a ballot', 'An opening, ordinary replies, and one prepared action beside the conversation: send it as the plan. Availability is never attendance: each person still answers for themselves, unless they already said an explicit yes that fits.')
    rB = rowdiv([cell('THURSDAY 7:06 PM', 'B1', 'An opening', 'Not an invitation. Maya can reply, enjoy it, or leave it alone. No attendance machinery appears because a place is attached.', b_open(), (P('OPENING'), P('RECEIVER'))),
                 cell('THURSDAY 9:12 PM', 'B2', 'Replies, and one send', 'A time emerges from three replies. One prepared action beside them sends it as the plan: settling and asking in one step.', b_replies(), (P('SETTLING'), P('AUTHOR'))),
                 cell('THURSDAY 9:16 PM', 'B4', 'Maya is asked anyway', 'She said &ldquo;yes, after noon&rdquo;, which is availability, so she answers for herself. Her words are shown.', b_invite(), (P('ATTENDANCE'), P('RECEIVER')))], top=16)
    rB2 = rowdiv([cell('THURSDAY 9:16 PM', 'B5', 'Priya said count me in', '&ldquo;Count me in any time after 12&rdquo; is a yes with a condition. 12:30 fits, so she is in; a change outside it would ask again.', b_conditional(), (P('ATTENDANCE'), P('RECEIVER'))),
                 cell('SATURDAY 12:20 PM', 'B6', 'On the day', 'Only who is in. Priya, who has the table, says where it is, and the plan carries it to everyone. One prepared message if you are running late.', b_quiet(), (P('ARRANGEMENT'), P('MAYA'))),
                 cell('SATURDAY 12:02 PM', 'B7', 'The brunch&rsquo;s chat', 'Sending the plan opens a chat for everyone invited, on by default. The plan sits at the top; Vesper answers only when asked.', b_chat(), (P('GROUP CHAT'), P('OCCASION'))),
                 cell('MONDAY 8:40 AM', 'C1', 'The optional instrument', 'Six people, three evenings, asked for. It reports who is free and stops there; Nora still settles and still asks.', c_tool(), (P('OPTIONAL POLL'), P('AUTHOR')))])
    rD = rowdiv([cell('SATURDAY 9:02 AM', 'D0', 'Writing it', 'A sentence with an end on it. No location that keeps running, nobody&rsquo;s availability inferred, nothing tracked.', d_now(), (P('PRESENCE'), P('SENDER'))),
                 cell('SATURDAY &rarr; TUESDAY', 'D1', 'A bounded expression, later stale', 'Written by Nora for one weekend. On Tuesday it reads as last weekend&rsquo;s, not as a standing invitation. Priya&rsquo;s runs until noon.', d_stale(), (P('PRESENCE'), P('RECEIVER')))])
    rN = ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' +
          notes('WHAT CHANGED, AND WHY', led([
                     ('VOTING DEMOTED', 'Gathering is an opening, replies, and the host sending it as the plan. Sept 26: the details screen and the separate ask are gone; one send does both.'),
                     ('AVAILABILITY IS NOT ATTENDANCE', 'Everyone answers for themselves. The one exception is an explicit yes with a condition, while the details stay inside it. Only people who are in are shown; nobody&rsquo;s silence is.'),
                     ('THE POLL SURVIVES, SMALLER', 'Asked for, by a host with several people and several dates. It reports who is free: no winner, no silence as consent, nobody enrolled.'),
                     ('WITH, SPLIT IN THREE', 'Being there, her name showing, and the night entering their shared record are three things. Her yes leaves a receipt with an undo; the third is a door she may never use.'),
                     ('PRESENCE IS A SENTENCE', 'Bounded, written, and stale afterwards. No always-on location, last seen, or inferred openness to company.'),
                 ]), w=560)
          + notes('DECIDED, AND STILL OPEN', led([
                     ('CONFLICT &middot; OLDER BOARD', 'Board 06&rsquo;s first version (Sept 21) made pickers automatically in. Superseded here, not by a founder ruling on the underlying question.'),
                     ('CHARTER', 'The group/social charter&rsquo;s voting-first rule is amended by the Sept 26 decision: a poll is something a host asks for.'),
                     ('GROUP CHAT', 'Every occasion has one, on by default (Sept 26 decision). Before a plan is sent, replies on the opening are the conversation.'),
                     ('WITH, DECIDED', 'Someone without an account is a plain name. A group cannot be tagged; people are named.'),
                     ('THE THIRD DOOR', 'Whether keeping the night in a shared record needs Nora&rsquo;s agreement too is unresolved; drawn as Maya&rsquo;s alone.'),
                 ]), w=520)
          + '</div>')
    bodyhtml = sA + rA + rA2 + sB + rB + rB2 + sechead('D', 'Being around, for a while', 'A bounded sentence about where you are, which stops being current.') + rD + rN
    html = (HEAD16 + f'<div style="width: 1860px; min-height: {hh("06", 4800)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('06 &middot; GETTING TOGETHER, AND SAYING WHO YOU WERE WITH', 'Conversation-led, with the ballot demoted',
                   'Rewritten for the September 22 handoff. An opening, replies, and the author settling; availability kept distinct from attendance; the poll kept as an optional instrument a host asks for. &ldquo;With&rdquo; split into three separate things. '
                   'A bounded expression of being around, which goes stale. Drawn, not tested with anyone.')
            + bodyhtml + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('06 - Getting together', html)

if __name__ == '__main__':
    build()
