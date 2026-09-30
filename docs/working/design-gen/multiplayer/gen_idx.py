"""00 · Start here. The index of the project as it stands on 2026-09-23: the eleven boards after 00, in reading order, one line
each, the founder's rulings so far, and what is still open. No phones; Life's editorial grammar only."""
from mp_kit2 import *

GROUPS = [
    ('SHARING', 'The foundation: what people share with each other, and how it arrives.', [
        ('01', 'Sharing', 'Four shares (words and photos, a gathering, where I&rsquo;ll be, a place), each seen writing, receiving and after.'),
        ('02', 'Sharing: the edges', 'Who it goes to, keeping it, asking, sending by link, taking it back, passing it on.'),
        ('03', 'Receiving', 'Where friends&rsquo; shares arrive: Home for what is sent to you and what has a time; Places for shares about places.'),
        ('04', 'Connecting', 'How people come to be in each other&rsquo;s Vesper.')]),
    ('BETWEEN PEOPLE', 'Two people, or a few, doing something together.', [
        ('05', 'The chat', 'A private chat between two people; Vesper only when asked.'),
        ('06', 'Getting together', 'Conversation-led plans, the ballot demoted, and saying who you were with.'),
        ('07', 'Shared with Maya', 'The relationship record, in Life&rsquo;s own grammar: a record, not a profile.')]),
    ('KEEPING', 'Collections: anything kept, alone or together, in Life.', [
        ('08', 'The collection', 'A kept collection opens like everything else in Life, grouped by kind.'),
        ('09', 'The collection over time', 'The same collections on a timeline, each artifact whole.'),
        ('10', 'Around a collection', 'Keeping something, correcting it, sharing it, using it months later.')]),
    ('STUDIES', 'Questions about the visual language, not the product.', [
        ('11', 'Type', 'Decided: EB Garamond stays. The four-way comparison is kept for reference.')]),
]
RULED = [
    'Sharing is the foundation: four kinds from one composer, one set of verbs (one like, comment, quote into a chat, keep). A like is seen only by the author.',
    'People&rsquo;s words lead: no Vesper line under shares, no quotation marks; a friend&rsquo;s note is a post.',
    'Where it was sent from is off by default; the sender chooses how precise.',
    'A shared place or link is a line: the name, where, and the sender&rsquo;s reason in words. Not a card.',
    'Place shares live in Places, beside the place. Home carries what is sent to you, what has a time, a small strip of posts with no place, and one line pointing to Places.',
    'Friends is one audience, forward only. The place travels freely; a friend&rsquo;s own words and photos stay within the audience they were sent to.',
    'Opening a link, joining what it holds, and becoming friends are separate. One addition through a link works without an account.',
    'The chat between two people is private; Vesper speaks only when asked.',
    'Every occasion has a group chat, on by default. A poll is something a host asks for; only an explicit yes counts as coming.',
    'Keep is private and immediate, with Undo; adding to a collection is a second, optional step.',
    'Collections use Life&rsquo;s grammar and live in its Threads view. Shared whole, history included; contributors remove only their own entries.',
    'Vesper may use a friend&rsquo;s words for your own question, credited and within their audience, once the use-grant contract allows it.',
    'EB Garamond stays the serif.',
]
OPEN = [
    ('PHOTOGRAPHS', 'About twenty ordinary photographs from the founder, to become the shared set for every project.'),
    ('LIFE PROJECT', 'Apply board 07&rsquo;s rulings (a friend&rsquo;s note as a post, the shared list) and place collections in the Threads view.'),
    ('USE GRANTS', 'Amend the contribution use-grant contract before Vesper uses friends&rsquo; words.'),
    ('NOT DRAWN', 'Report on a share, and Block.'),
    ('ENGINEERING', 'A new share and audience model: what is built today is a one-recipient, place-required note.'),
    ('NOT DECIDED', 'Notifications, verifying a guest, how long things are kept, and export.'),
]

def entry(n, t, s):
    return (f'<div style="display:flex; gap:18px; align-items:baseline; padding:14px 0; border-bottom:1px solid rgba(27,23,20,0.10);">'
            f'<span style="font-family:var(--mono); font-size:13px; font-weight:700; letter-spacing:1px; color:#8A6628; width:30px; flex:none;">{n}</span>'
            f'<div style="flex:1;"><div style="font-family:var(--serif); font-size:21px; line-height:26px; font-weight:600;">{t}</div>'
            f'<div style="font-size:14px; line-height:20px; color:#3A332C; margin-top:3px;">{s}</div></div></div>')
def group(k, sub, items):
    return (f'<div style="margin-top:34px;"><div style="display:flex; align-items:baseline; border-top:1.5px solid rgba(27,23,20,0.55); padding-top:10px;">'
            f'<span style="font-family:var(--mono); font-size:10.5px; font-weight:700; letter-spacing:1.4px;">{k}</span>'
            f'<span style="font-family:var(--mono); font-size:10px; letter-spacing:1px; color:#6E6862; margin-left:auto;">{items[0][0] if len(items) == 1 else items[0][0] + '&ndash;' + items[-1][0]}</span></div>'
            f'<div style="font-family:var(--serif); font-style:italic; font-size:17px; line-height:23px; color:#6E6862; margin-top:6px;">{sub}</div>'
            + ''.join(entry(*i) for i in items) + '</div>')
def listing(k, right, items, dot):
    rows = ''.join(f'<div style="display:flex; gap:12px; padding:9px 0; border-bottom:1px solid rgba(27,23,20,0.08);"><span style="width:7px; height:7px; border-radius:4px; {dot} box-sizing:border-box; flex:none; margin-top:7px;"></span>'
                   f'<span style="font-size:14.5px; line-height:21px;">{t}</span></div>' for t in items)
    return (f'<div style="margin-top:34px;"><div style="border-top:1.5px solid rgba(27,23,20,0.55); padding-top:10px; display:flex; gap:12px;"><span style="font-family:var(--mono); font-size:10.5px; font-weight:700; letter-spacing:1.4px; flex:none;">{k}</span>'
            f'<span style="font-family:var(--mono); font-size:10px; letter-spacing:1px; color:#6E6862; margin-left:auto; text-align:right;">{right}</span></div>{rows}</div>')
def ruled():
    return listing('DECIDED', 'RECORDED SEPT 26 &middot; docs/decisions/2026-09-26-multiplayer-direction.md', RULED, 'background:#3D7050;')
def still_open():
    rows = ''.join(f'<div style="padding:10px 0; border-bottom:1px solid rgba(27,23,20,0.08);"><div style="font-family:var(--mono); font-size:10px; font-weight:700; letter-spacing:1.2px; color:#8A6628;">{k}</div>'
                   f'<div style="font-size:14.5px; line-height:21px; margin-top:3px;">{t}</div></div>' for k, t in OPEN)
    return (f'<div style="margin-top:34px;"><div style="border-top:1.5px solid rgba(27,23,20,0.55); padding-top:10px;"><span style="font-family:var(--mono); font-size:10.5px; font-weight:700; letter-spacing:1.4px;">STILL TO DO</span></div>{rows}</div>')

def build():
    left = ''.join(group(*g) for g in GROUPS)
    right = ruled() + still_open()
    html = (HEAD_VDL + f'<div style="width: 1600px; min-height: {hh("00", 1700)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 48px 36px 48px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('00 &middot; START HERE', 'Vesper, between people',
                   'How people share with each other, spend time together and keep things together, drawn in Life&rsquo;s grammar. Eleven boards, in reading order; what has been decided, recorded September 26; what is still to do. Drawn, not tested with anyone.')
            + f'<div style="display:flex; gap:72px; align-items:flex-start;"><div style="flex:1.25;">{left}</div><div style="flex:1;">{right}</div></div>'
            + f'<div class="fn" style="margin-top: 40px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('00 - Start here', html)

if __name__ == '__main__':
    build()
