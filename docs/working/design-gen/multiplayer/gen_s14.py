"""20 · Connecting. How two people come to be in each other's Vesper at all. You invite by sending a real thing, not by
asking someone to join; the link is enough to read and reply; joining makes the connection and nothing else; contacts
are asked once and only match people who have your number too; the only other suggestion is someone you were actually
with at an occasion. Ignoring is silent. Home and Chat frames use the sharing kit; the record uses Life's grammar."""
import re
from mp_kit2 import *
from gen_merge import daycap
import gen_s1 as S
import gen_s6 as L6
from gen_s1 import CARD_CSS, status, chat_field, paper_map, footer, sep, _g, WITH_P
from gen_s2 import sheet
from gen_s5 import list_card
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
APP = tag('NO APP', OX, 'rgba(122,46,46,0.10)')
LIFE = tag('LIFE GRAMMAR', GREEN, 'rgba(61,112,80,0.12)')
LIFE_STYLE = re.search(r'<style>(.*?)</style>', L6.PREFIX, re.S).group(1)
HEAD20 = HEAD_VDL.replace('</helmet>', f'<style>{LIFE_STYLE}</style>\n</helmet>', 1)
INVITE = 'come see what we&rsquo;ve been keeping. add to it if you want'

def card(inner, pad='14px 16px'): return f'<div style="{CARD_CSS} padding: {pad};">{inner}</div>'
def kick(t, color=None): return f'<div class="fn" style="{f"color: {color};" if color else ""}">{t}</div>'
def ser(t, size=19, lh=24): return f'<div style="{SERIF} font-weight: 600; font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def body(t, color=INK2, size=14, lh=20, top=0): return f'<div style="font-size: {size}px; line-height: {lh}px; color: {color}; margin-top: {top}px;">{t}</div>'
def av(letter, size=36): return f'<span style="width: {size}px; height: {size}px; border-radius: {size//2}px; background: {INK}; color: {CARD}; display: inline-flex; align-items: center; justify-content: center; font-size: {int(size*0.38)}px; font-weight: 700; flex: none;">{letter}</span>'
def place_line(kind, name, words, who):
    return (f'<div style="display: flex; gap: 12px; align-items: center; padding: 11px 0; border-bottom: 1px solid rgba(27,23,20,0.07);">{thumb(kind, 44)}'
            f'<div><div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 21px;">{name}</div><div style="font-size: 13.5px; line-height: 19px; color: {INK2};">{words} &middot; <span style="color: {MUTE};">{who}</span></div></div></div>')

# ── 1 · Nora invites by sending a thing ──
def invite():
    return S.composer('N', INVITE, list_card().replace('14 places &middot; 9 been &middot; Brooklyn', '3 places &middot; yours so far'), to='Maya &middot; by link', faces_=None)

# ── 2 · Maya, with no app ──
def link_page():
    """Sept 26 (§12.6): value first, and one small invited contribution through the link itself, attributed to the
    person the link was sent to. Whether a guest may add without an account is an open guest-scope choice."""
    inner = f'<div style="padding: 20px 22px 0 22px;"><div class="fn" style="letter-spacing: 1px;">FROM NORA</div></div>'
    inner += gut(status(60, 'Nora', 'TUESDAY · TO YOU', INVITE), top=14)
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 26px; line-height: 30px;">Our places</div>', top=20)
    inner += gut(place_line('table', 'Lulu&rsquo;s', 'upstairs is the reason to go', 'Nora')
                 + place_line('film', 'The Lantern', 'one film a week', 'Nora')
                 + place_line('pier', 'The pier at low water', 'for walking it off', 'Nora'), top=8)
    inner += gut(f'<div style="border: 1px solid rgba(27,23,20,0.16); border-radius: 12px; padding: 10px 12px; background: {CARD};">'
                 f'<div style="font-size: 15px; color: {INK};">Hato</div>'
                 f'<div style="font-size: 14px; color: {INK2}; margin-top: 4px; border-top: 1px solid rgba(27,23,20,0.08); padding-top: 6px;">the broth is stupid good</div>'
                 f'<div style="margin-top: 10px; display: flex; align-items: center; gap: 10px;">{btn("Add, as Maya")}<span style="font-size: 12.5px; color: {MUTE};">Nora and you will see it</span></div></div>', top=16)
    inner += gut(chat_field('Reply to Nora', ask=False), top=14)
    return webframe(inner)
def first_home():
    """Sept 26 (§12.6): joining Our places is joining that one thing. Friends is a separate, explicit step, and joining
    subscribes her to nothing else. No contacts request."""
    inner = avatar_for(anchor_row('NEW YORK', 'TUESDAY 8:40 PM'), 'M')
    inner += orientation('Our places, with Nora.', 'Four places. Your Hato is in it.')
    inner += gut(list_card().replace('14 places &middot; 9 been &middot; Brooklyn', '4 places &middot; with Nora'), top=18)
    inner += gut(f'<div style="display: flex; gap: 18px;">{door("Open it", GOLDD)}{door("Reply to Nora", MUTE)}</div>', top=8)
    inner += sep(24) + gut(f'<div style="display: flex; align-items: center; gap: 12px;">{av("N", 32)}<div style="flex: 1;"><div style="font-size: 15px; color: {INK};">Nora</div>'
                           f'<div style="font-size: 13px; color: {MUTE}; margin-top: 1px;">In Our places with you</div></div>{door("Ask to be friends", GOLDD)}</div>', top=18)
    return phone2(inner, active='Home')
def nora_hears():
    """Sept 26 (§12.6): the sender hears about the contribution, in the shared thing. Never "opened your link"."""
    inner = avatar_for(anchor_row('NEW YORK', 'TUESDAY 8:45 PM'), 'N')
    inner += gut(card(f'<div style="display: flex; align-items: center; gap: 12px;">{av("M", 40)}<div>{ser("Maya added Hato", 18, 22)}{body("To Our places &middot; &ldquo;the broth is stupid good&rdquo;", INK2, 14, 20, 2)}</div></div>'
                      + f'<div style="margin-top: 12px; display: flex; gap: 18px;">{door("Open Our places", GOLDD)}{door("Reply", MUTE)}</div>'), top=20)
    inner += sep(24) + gut(S.share('Priya', '7:52 PM · TO FRIENDS', 'bread&rsquo;s out of the oven if anyone&rsquo;s near'), top=18)
    return phone2(inner, active='Home')
def contacts():
    """Sept 26 (§12.6): becoming friends is its own act, asked by one and answered by the other."""
    inner = avatar_for(anchor_row('NEW YORK', 'WEDNESDAY 9:02 AM'), 'N')
    inner += gut(card(f'<div style="display: flex; align-items: center; gap: 12px;">{av("M", 40)}<div>{ser("Maya asked to be friends", 18, 22)}{body("You&rsquo;d each see what the other shares with friends.", MUTE, 13.5, 19, 2)}</div></div>'
                      + f'<div style="margin-top: 14px; display: flex; gap: 8px;">{btn("Be friends")}{btn("Not now", False)}</div>'), top=20)
    return phone2(inner, active='Home')
def from_occasion():
    inner = avatar_for(page_bar_('PASTA NIGHT'), 'S')
    inner += f'<div style="padding: 16px 22px 0 22px;">{ser("Pasta night", 28, 32)}{body("Saturday, October 3 &middot; Nora&rsquo;s", MUTE, 14, 20, 4)}</div>'
    inner += sect('Who was there', top=24) + gut(
        f'<div style="display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid rgba(27,23,20,0.07);">{av("N", 32)}<span style="font-size: 15px;">Nora</span><span class="fn" style="margin-left: auto;">FRIENDS</span></div>'
        + f'<div style="display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 1px solid rgba(27,23,20,0.07);">{av("M", 32)}<span style="font-size: 15px;">Maya</span><span style="margin-left: auto;">{door("Ask to be friends", GOLDD)}</span></div>'
        + f'<div style="display: flex; align-items: center; gap: 12px; padding: 11px 0;">{av("P", 32)}<span style="font-size: 15px;">Priya</span><span style="margin-left: auto;">{door("Ask to be friends", GOLDD)}</span></div>')
    return phone2(inner, active='Life')
def page_bar_(label): return S.page_bar(label)

# ── 7 · the record starts small ──
def first_record():
    inner = L6.head('SHARED RECORD &middot; SINCE TUESDAY', 'Shared with Nora', 'One thing so far.')
    inner += L6.sec('OURS', '1 &middot; MADE TOGETHER', 26)
    inner += L6.row2('Our places', 'Lulu&rsquo;s &middot; the Lantern &middot; the pier &middot; Hato', '4', glyph=L6.MARK)
    inner += L6.sec('FROM NORA', '1')
    inner += f'<div style="margin:12px 22px 0 22px; font-family:var(--sans); font-size:16px; line-height:23px;">{INVITE}</div><div class="meta" style="margin:6px 22px 0 22px;">NORA &middot; TUESDAY</div>'
    inner += L6.door('Write back', 10)
    return L6.phone(inner)

# ── 8 · stepping back ──
def remove():
    inner = L6.head('SHARED RECORD &middot; SINCE 2023', 'Shared with Sam', 'Four things &mdash; a few nights out.')
    inner += L6.sec('THE SHARED RECORD', '4', 26)
    inner += L6.row1(L6.GLASS, 'John Summit &middot; Pacha', 'SEPT 26')
    inner += L6.row1(L6.GLASS, 'Caribou &middot; the same door, again', 'MAY')
    inner += sheet(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">Stop sharing with Sam?</div>'
                   + f'<div style="margin-top: 8px;">{plain("Nothing new goes between you. What each of you already has stays with each of you. Sam isn&rsquo;t told; he just stops seeing new things from you.", INK2, 15, 21)}</div>'
                   + f'<div style="margin-top: 14px;">{actions(btn("Stop sharing"), door("See less instead", MUTE))}</div>')
    return L6.phone(inner)

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('TUESDAY 8:10 PM', '1', 'Inviting, by sending something', 'Nora doesn&rsquo;t ask Maya to join Vesper. She sends her Our places, by link, with a line of her own. The invitation is the thing.', invite(), (P('INVITE'), P('NORA'))),
                 cell('TUESDAY 8:22 PM', '2', 'The link, with no app', 'Maya reads and replies without installing anything, and can add one place through the link, as herself. More than that asks for an account.', link_page(), (APP, P('MAYA'))),
                 cell('TUESDAY 8:40 PM', '3', 'Joining one thing', 'Her first Home is what she joined, with her Hato in it. Joining isn&rsquo;t becoming friends; that is a separate door. No contacts request.', first_home(), (P('JOINED'), P('MAYA'))),
                 cell('TUESDAY 8:45 PM', '4', 'Nora hears what Maya added', 'One card about the shared thing: what Maya added and her words. Never that she opened the link. No badge, no count of people joined.', nora_hears(), (P('CONTRIBUTION'), P('NORA')))], top=16)
    r2 = rowdiv([cell('WEDNESDAY 9:02 AM', '5', 'Becoming friends, separately', 'Maya asks; Nora answers. Friends see what each other shares with friends. Not now tells Maya nothing.', contacts(), (P('FRIENDS'), P('NORA'))),
                 cell('SUNDAY', '6', 'From an occasion', 'Sam met Maya and Priya at pasta night, so the evening&rsquo;s page lets him ask to be friends. Nowhere else suggests strangers.', from_occasion(), (P('OCCASION'), P('SAM'))),
                 cell('MAYA&rsquo;S LIFE', '7', 'The record starts small', 'Maya&rsquo;s shared record with Nora on its first day: Our places with its four places, and Nora&rsquo;s note. No tally of whose are whose.', first_record(), (P('RECORD'), LIFE)),
                 cell('LATER', '8', 'Stepping back', 'Stopping sharing ends what goes between you from now on. What each already has stays theirs. See less is the gentler door.', remove(), (P('ENDING'), LIFE))])
    n = notes('THE RULES, PROPOSED', led([
        ('INVITE WITH A THING', 'You invite someone by sending them something real: a list, a night, an invitation. Never a bare &ldquo;join Vesper&rdquo;.'),
        ('THE LINK IS ENOUGH', 'Reading and replying need nothing installed, and one addition through the link works too, attributed to the person it was sent to. If an account is needed, say so honestly and keep what they were doing.'),
        ('THREE STEPS, KEPT APART', 'Opening a link, joining the thing it holds, and becoming friends are three different acts. Joining one collection never subscribes you to someone&rsquo;s friends posts.'),
        ('NO CONTACTS ASK', 'Value comes before any setup. The earlier contacts-matching frame is removed; the social handoff rules out contacts import.'),
        ('NO STRANGERS', 'The only other suggestion is someone you were with at an occasion, on that occasion&rsquo;s page. No people-you-may-know, no friend-of-friend lists.'),
        ('SILENT NO', 'Not now tells nobody anything. Stopping sharing tells the other person nothing; they just stop seeing new things.'),
        ('NO OPEN RECEIPTS', 'The sender hears what was added or said, never that a link was opened.'),
    ]), w=620)
    n2 = notes('OPEN', led([
        ('GUEST IDENTITY', 'One addition through a link is decided (the Sept 26 decision). How the person it was sent to is verified is not.'),
        ('ACCOUNT', 'Phone number is assumed as the identity. Whether it is, and how that meets the existing sign-in, is not decided here.'),
        ('THE LINK&rsquo;S LIFE', 'How long a link page lives, and whether the sender can close it, is open (as on board 02).'),
        ('GROUPS', 'Inviting several people with one link, and what they see of each other, is not drawn.'),
    ]), w=520)
    bodyhtml = r1 + r2 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n + n2 + '</div>'
    html = (HEAD20 + f'<div style="width: 1860px; min-height: {hh("04", 3000)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('04 &middot; CONNECTING', 'How people come to be in each other&rsquo;s Vesper',
                   'You invite by sending something real; the link is enough to read, reply and perhaps add one thing; joining that thing, and becoming friends, are separate acts; the only suggestion is someone you were with. '
                   'Every earlier board assumes this has already happened. Drawn, not tested with anyone.')
            + bodyhtml + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('04 - Connecting', html)

if __name__ == '__main__':
    build()
