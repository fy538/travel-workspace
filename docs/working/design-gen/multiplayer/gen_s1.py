"""10 · Sharing. Three shares side by side, each seen three times: written, received, and what the sender sees after.
A: words and a picture. B: a gathering invitation (the Social 03 / Plans 04 InviteCard). C: going to John Summit,
as an update with the ticket (the Life Ticket, admission mode). One like, a comment, a quote into a chat with a person.
Under the author's words, where there is something to say, one line from Vesper for the reader. Founder direction,
2026-09-21: do not reinvent the wheel; one kind of like; a real ticket artifact."""
from mp_kit2 import *
from gen_merge import daycap
from gen_p2_common import illo
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
NEW = P('NEW')
CAKE = 'it sank &#128557; still ate half of it'
PACHA = 'pacha tonight. john summit. on at 1'

def ticket_full():
    return dci('Ticket', 236, mode='admission', density='full', kicker='ADMISSION · PACHA', date='TONIGHT', status='ON AT 1:00 AM',
               title='John Summit', sub='Pacha, New York · doors 11', fields='DOORS=11:00 PM;ON=1:00 AM;ADMIT=1 · GENERAL', band='ADMIT ONE|SAM')
def ticket_row():
    return dci('Ticket', 58, mode='admission', density='row', rowTitle='John Summit · Pacha', rowDetail='Tonight · on at 1:00 AM', stub='1 AM')

# ───────────────────────── the sharing kit, aesthetic pass 2026-09-21 ─────────────────────────
# One card treatment (the Life ticket's: paper, soft shadow, no border). Actions are glyphs, not words with arrows.
# Location lives on the footer row, left, in grey. Explanations stay outside the phone.
CARD_CSS = 'background: #FBF8F1; border-radius: 12px; box-shadow: 0 1px 2px rgba(27,23,20,0.08), 0 6px 18px rgba(27,23,20,0.06);'
def _g(path, c, size=18, fill='none', sw='1.6'):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 20 20" fill="{fill}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="flex: none; display: block;">{path}</svg>'
HEART_P = '<path d="M10 16.5s-6-3.7-6-8.2A3.3 3.3 0 0 1 10 6.4a3.3 3.3 0 0 1 6 1.9c0 4.5-6 8.2-6 8.2z"/>'
BUBBLE_P = '<path d="M4 5.5h12a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H9l-3.5 2.5V14.5H4a1 1 0 0 1-1-1v-7a1 1 0 0 1 1-1z"/>'
QUOTE_P = '<path d="M11 4.5l5 4.5-5 4.5M16 9H9a5 5 0 0 0-5 5v1.5"/>'
MARK_P = '<path d="M6 3.5h8a.5.5 0 0 1 .5.5v12.5L10 13.5l-4.5 3V4a.5.5 0 0 1 .5-.5z"/>'
PIN_P = '<path d="M10 18s-6-5.2-6-9.5a6 6 0 0 1 12 0C16 12.8 10 18 10 18z"/><circle cx="10" cy="8.5" r="2"/>'
CAM_P = '<rect x="2.5" y="5.5" width="15" height="11" rx="2"/><circle cx="10" cy="11" r="3"/><path d="M7 5.5l1.2-2h3.6l1.2 2"/>'
MIC_P = '<rect x="7.5" y="2.5" width="5" height="9" rx="2.5"/><path d="M4.5 9.5a5.5 5.5 0 0 0 11 0M10 15v2.5"/>'
CAL_P = '<rect x="3" y="4.5" width="14" height="12.5" rx="2"/><path d="M3 8.5h14M7 2.5v3.5M13 2.5v3.5"/>'
PLACE_P = '<path d="M3.5 8.5l1.5-4.5h10l1.5 4.5M3.5 8.5v8h13v-8M3.5 8.5c0 1.4 1.4 2 2.2 2s2.2-.6 2.2-2c0 1.4 1.3 2 2.1 2s2.1-.6 2.1-2c0 1.4 1.4 2 2.2 2s2.2-.6 2.2-2M8 16.5v-3.5h4v3.5"/>'
X_P = '<path d="M5 5l10 10M15 5L5 15"/>'
SPARK_P = '<path d="M10 2.5l1.6 5.2 5.4 1.8-5.4 1.8L10 16.5l-1.6-5.2L3 9.5l5.4-1.8z"/>'
UP_P = '<path d="M10 15.5v-11M5.5 9L10 4.5 14.5 9"/>'
WITH_P = '<circle cx="7.5" cy="7" r="2.8"/><path d="M2.5 16.5c.6-3 2.6-4.6 5-4.6s4.4 1.6 5 4.6"/><circle cx="13.8" cy="7.8" r="2.2"/><path d="M13.4 12c1.9.1 3.4 1.5 4 4"/>'
OPTS_P = '<rect x="3" y="3.5" width="4" height="4" rx="1"/><rect x="3" y="12.5" width="4" height="4" rx="1"/><path d="M4 5.5l1 1 1.6-2M10 5.5h7M10 14.5h7"/>'
DOTS = f'<svg width="20" height="20" viewBox="0 0 20 20" style="flex: none;"><circle cx="4.5" cy="10" r="1.5" fill="{INK}"/><circle cx="10" cy="10" r="1.5" fill="{INK}"/><circle cx="15.5" cy="10" r="1.5" fill="{INK}"/></svg>'
PIN = _g(PIN_P, 'currentColor', 13)

def where_line(w, top=8):
    """Where the sender was: a neighborhood, or the place itself when they are at it. Never an address."""
    return f'<div style="display: flex; align-items: center; gap: 5px; margin-top: {top}px; font-size: 13px; line-height: 18px; color: {MUTE};">{PIN}<span>{w}</span></div>'
def footer(where=None, liked=False, kept=False, glyphs=True, top=12):
    """One quiet row under a post: where it was sent from on the left, four glyphs on the right."""
    w = f'<span style="display: inline-flex; align-items: center; gap: 5px; font-size: 13px; color: {MUTE};">{PIN}{where}</span>' if where else ''
    g = ''
    if glyphs:
        heart = _g(HEART_P, GOLDD if liked else MUTE, 19, fill=GOLDD if liked else 'none')
        mark = _g(MARK_P, GOLDD if kept else MUTE, 19, fill=GOLDD if kept else 'none')
        g = f'<span style="margin-left: auto; display: inline-flex; gap: 22px; align-items: center;">{heart}{_g(BUBBLE_P, MUTE, 19)}{_g(QUOTE_P, MUTE, 19)}{mark}</span>'
    return f'<div style="display: flex; align-items: center; min-height: 28px; margin-top: {top}px;">{w}{g}</div>'
def verbs(join=None, liked=False, kept=False):
    return footer(None, liked, kept, top=0)
def liked_by(names):
    return f'<div style="display: flex; align-items: center; gap: 7px; margin-top: 12px; font-size: 13px; color: {MUTE};">{_g(HEART_P, GOLDD, 14, fill=GOLDD)}<span>{names}</span></div>'
def _meta(m):
    return '<span style="display: inline-block; width: 8px;"></span>'.join(m.split(' · '))
def status(h, author, meta, words, where=None, me=None, **kw):
    """A person's own post: name and time once, then their words in plain type. Not a quotation."""
    letter = (me or author[0]) if author == 'You' else author[0]
    return (f'<div><div style="display: flex; align-items: center; gap: 10px;"><span style="width: 28px; height: 28px; border-radius: 14px; background: {INK}; color: {CARD}; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex: none;">{letter}</span>'
            f'<span style="font-size: 15px; font-weight: 600; color: {INK};">{author}</span><span class="fn">{_meta(meta)}</span></div>'
            f'<div style="font-size: 17px; line-height: 24px; color: {INK}; margin-top: 10px;">{words}</div>{where_line(where) if where else ""}</div>')
def original(h, **kw):
    return status(h, **kw)
def tagline(t):
    return ''
def sep(top=22):
    """Posts in a feed are separated by space and a hairline, not by section heads."""
    return f'<div style="margin: {top}px 22px 0 22px; border-top: 1px solid rgba(27,23,20,0.08);"></div>'
def page_bar(label):
    """A page gets a back chevron, its label, and one menu. No search or map in a page header."""
    return f'<div style="padding: 24px 22px 0 22px; display: flex; align-items: center; gap: 10px;">{BACK}<span class="fn" style="letter-spacing: 1px;">{label}</span><span style="margin-left: auto;">{DOTS}</span></div>'
def page_title(t, sub=''):
    s = f'<div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 4px;">{sub}</div>' if sub else ''
    return f'<div style="padding: 16px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 28px; line-height: 32px; color: {INK};">{t}</div>{s}</div>'

def photo_grid(n=3, size=100, tag_='PHOTO'):
    """Several pictures tile under the words at the same small size, as on WeChat."""
    kinds = ('room', 'loaf', 'table')
    return '<div style="display: flex; gap: 6px;">' + ''.join(f'<div style="width: {size}px; height: {size}px; border-radius: 8px; overflow: hidden; position: relative;">{illo(kinds[i % 3], size, size)}' + (f'<span style="position: absolute; left: 5px; bottom: 5px; {MONO} font-size: 8px; letter-spacing: 1px; color: rgba(244,238,221,0.9); background: rgba(27,23,20,0.55); padding: 2px 5px; border-radius: 4px;">{tag_}</span>' if i == 0 else '') + '</div>' for i in range(n)) + '</div>'
def photo_thumb(size=150, tag_='PHOTO &middot; MAYA'):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 8px; overflow: hidden; position: relative;">{illo("room", size, size)}'
            f'<span style="position: absolute; left: 6px; bottom: 6px; {MONO} font-size: 8px; letter-spacing: 1px; color: rgba(244,238,221,0.9); background: rgba(27,23,20,0.55); padding: 2px 5px; border-radius: 4px;">{tag_}</span></div>')
def gathering(answer=None):
    """The gathering as an attachment: what, when, where, who is in, and the answer. Not a form."""
    who = f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 10px;">{facepile(["M","P"], 20, -6)}<span style="font-size: 13px; color: {INK2};">Maya, Priya are in</span></div>'
    ans = ''
    if answer == 'ask': ans = f'<div style="display: flex; gap: 8px; align-items: center; margin-top: 14px;">{btn("I&rsquo;m in")}{btn("Can&rsquo;t make it", False)}</div>'
    if answer == 'in': ans = f'<div style="margin-top: 10px;">{plain("You&rsquo;re in · from 6:45", GREEN, 13, 18)}</div>'
    return (f'<div style="{CARD_CSS} padding: 14px 16px;">'
            f'<div class="fn" style="margin-bottom: 6px;">GATHERING &middot; SATURDAY</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px;">Pasta night at Nora&rsquo;s</div>'
            f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">Cooking from 6, eating around 7<br>Court Street, 3F</div>{who}{ans}</div>')
def post(author, meta, words, extra='', where=None, h=80, me=None):
    """Sender's own view: words, what is attached, where it was sent from. No action glyphs on your own post."""
    e = f'<div style="margin-top: 12px;">{extra}</div>' if extra else ''
    return status(h, author=author, meta=meta, words=words, me=me) + e + (footer(where, glyphs=False) if where else '')
def share(author, meta, words, extra='', line_=None, join=None, liked=False, h=80, where=None, kept=False, me=None, **kw):
    e = f'<div style="margin-top: 12px;">{extra}</div>' if extra else ''
    return status(h, author=author, meta=meta, words=words, me=me) + e + footer(where, liked, kept)

def to_row(names):
    return ''
def to_bar(to, faces_=None):
    """The composer's header: close, and who it goes to as one tappable line."""
    f = facepile(list(faces_), 18, -6) if faces_ else ''
    return (f'<div style="padding: 22px 22px 0 22px; display: flex; align-items: center; gap: 12px;">{_g(X_P, INK, 18)}'
            f'<span style="display: inline-flex; align-items: center; gap: 8px; height: 32px; padding: 0 14px; border-radius: 16px; {CARD_CSS}">'
            f'<span style="font-size: 13px; color: {MUTE};">To</span><span style="font-size: 14px; font-weight: 600; color: {INK};">{to}</span>{f}{CHEV}</span></div>')
def loc_row(w):
    """Where the phone is, as one small grey line with an x. Nothing at all when it is off."""
    if not w: return ''
    return f'<div style="display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: {MUTE};">{PIN}<span>{w}</span>{_g(X_P, MUTE, 11)}</div>'
def toolbar(on=(), primary='Send'):
    """Everything you can attach, as glyphs, with Send on the right. Gold means attached."""
    icons = [('photo', CAM_P), ('voice', MIC_P), ('where', PIN_P), ('when', CAL_P), ('place', PLACE_P), ('with', WITH_P), ('options', OPTS_P)]
    g = ''.join(_g(p, GOLDD if k in on else MUTE, 21) for k, p in icons)
    return (f'<div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: 14px; display: flex; align-items: center;">'
            f'<span style="display: inline-flex; gap: 14px; align-items: center;">{g}</span><span style="margin-left: auto;">{btn(primary)}</span></div>')
def composer(letter, text, attach, names=None, hint=None, primary='Send', alt=None, when='', where=None, to='Friends', on=(), faces_=None):
    inner = avatar_for(to_bar(to, faces_), letter)
    inner += gut(plain(text, size=18, lh=26), top=24)
    inner += gut(attach, top=16)
    if where: inner += gut(loc_row(where), top=14)
    inner += gut(toolbar(on, primary), top=28)
    return phone2(inner, active='Chat')

def chat_field(ph='Message', ask=True):
    """A chat composer: Ask Vesper as one gold glyph, the field, a round send."""
    a = f'<span style="width: 40px; height: 40px; border-radius: 20px; display: inline-flex; align-items: center; justify-content: center; {CARD_CSS} flex: none;">{_g(SPARK_P, GOLDD, 18)}</span>' if ask else ''
    return (f'<div style="display: flex; gap: 8px; align-items: center;">{a}'
            f'<div style="flex: 1; height: 40px; border-radius: 20px; border: 1px solid rgba(27,23,20,0.12); background: {CARD}; display: flex; align-items: center; padding: 0 16px; font-size: 15px; color: {MUTE};">{ph}</div>'
            f'<span style="width: 40px; height: 40px; border-radius: 20px; background: {UMBER}; display: inline-flex; align-items: center; justify-content: center; flex: none;">{_g(UP_P, CARD, 18, sw="2")}</span></div>')
def vesper_reply(t, who='Nora'):
    return (f'<div style="border-left: 2px solid {GOLDD}; padding: 6px 0 6px 12px;">'
            f'<div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">{_g(SPARK_P, GOLDD, 11)}<span style="{MONO} font-size: 9px; letter-spacing: 1.1px; color: {GOLDD};">VESPER &middot; ASKED BY {who.upper()} &middot; TO BOTH OF YOU</span></div>'
            f'{plain(t, INK2, 14, 20)}</div>')
def asked_bubble(t, who='NORA'):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="display: flex; align-items: center; gap: 5px; padding: 0 4px 4px 0;">{_g(SPARK_P, GOLDD, 10)}<span style="{MONO} font-size: 9px; letter-spacing: 1px; color: {GOLDD};">{who} ASKED VESPER</span></div></div>' + bubble(t)

def paper_map(h=150, pins=((0.22, 0.58), (0.38, 0.34), (0.55, 0.62), (0.71, 0.40), (0.84, 0.70)), w=393):
    """A paper map: cream ground, hairline streets, water, gold pins. The cover of a list of places."""
    streets = ''.join(f'<line x1="{x1*w:.0f}" y1="{y1*h:.0f}" x2="{x2*w:.0f}" y2="{y2*h:.0f}" stroke="rgba(27,23,20,{a})" stroke-width="{sw}"/>' for x1, y1, x2, y2, a, sw in (
        (0, .2, 1, .12, .10, 1), (0, .45, 1, .5, .14, 1.4), (0, .78, 1, .86, .10, 1), (.12, 0, .2, 1, .10, 1), (.3, 0, .34, 1, .08, 1),
        (.48, 0, .46, 1, .14, 1.4), (.64, 0, .68, 1, .08, 1), (.8, 0, .9, 1, .10, 1), (0, .95, .6, 0, .07, 1), (.35, 1, 1, .25, .07, 1)))
    water = f'<path d="M0 {h*0.88:.0f} C {w*0.2:.0f} {h*0.8:.0f}, {w*0.35:.0f} {h*1.02:.0f}, {w*0.6:.0f} {h*0.92:.0f} S {w*0.9:.0f} {h*0.84:.0f}, {w} {h*0.9:.0f} L {w} {h} L 0 {h} Z" fill="#DCE3E0"/>'
    park = f'<rect x="{w*0.58:.0f}" y="{h*0.08:.0f}" width="{w*0.14:.0f}" height="{h*0.22:.0f}" rx="4" fill="#E3E6D6"/>'
    ps = ''.join(f'<g transform="translate({x*w:.0f},{y*h:.0f})"><path d="M0 0 C -6 -7, -7 -10, -7 -13 A 7 7 0 0 1 7 -13 C 7 -10, 6 -7, 0 0 Z" fill="{GOLDD}"/><circle cx="0" cy="-13" r="2.6" fill="#F4EEDD"/></g>' for x, y in pins)
    return f'<svg width="100%" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" style="display: block;"><rect width="{w}" height="{h}" fill="#F1EBDD"/>{water}{park}{streets}{ps}</svg>'

# ── A · words and pictures ──
def a_write():
    return composer('M', CAKE, photo_grid(3, 96), where='Fort Greene', on=('photo', 'where'))
def a_receive():
    inner = anchor_row('NEW YORK', 'SATURDAY 8:10 AM')
    inner += gut(share('Maya', 'LAST NIGHT · TO FRIENDS', CAKE, extra=photo_grid(3, 108, 'PHOTO &middot; MAYA'), where='Fort Greene'), top=20)
    inner += sep() + gut(share('Priya', 'FRIDAY 7:52 PM · TO FRIENDS', 'bread&rsquo;s out of the oven if anyone&rsquo;s near'), top=18)
    return phone2(inner, active='Home')
def a_after():
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 10:30 AM'), 'M')
    inner += gut(post('You', 'LAST NIGHT · TO FRIENDS', CAKE, photo_grid(3, 96, "PHOTO &middot; YOURS"), 'Fort Greene', me='M') + liked_by('Nora, Sam'), top=20)
    inner += sep() + gut(original(80, author='Sam', meta='8:14 AM · TO YOU', words='structurally questionable is generous'), top=18)
    inner += gut(original(80, author='Priya', meta='9:02 AM · TO FRIENDS', words='half is the correct amount of a sunken cake'), top=18)
    return phone2(inner, active='Home')

# ── B · a gathering invitation ──
def b_write():
    return composer('N', 'pasta night saturday. cooking from 6, eating around 7. come for either', gathering().replace('Maya, Priya are in', 'Nobody yet'), on=('when', 'place'))
def b_receive():
    inner = avatar_for(anchor_row('NEW YORK', 'THURSDAY 9:14 PM'), 'S')
    inner += gut(share('Nora', 'THURSDAY 9:10 PM · TO FRIENDS', 'pasta night saturday. cooking from 6, eating around 7. come for either', extra=gathering('ask')), top=20)
    return phone2(inner, active='Home')
def b_after():
    inner = page_bar('GATHERING')
    inner += page_title('Pasta night', 'Saturday &middot; cooking 6:00, eating 7:00 &middot; Court Street, 3F')
    inner += gut(f'<div style="display: flex; align-items: center; gap: 8px;">{facepile(["M","S","P"], 22, -7)}<span style="font-size: 14px; color: {INK2};">Maya, Sam, Priya are in</span></div>', top=14)
    inner += sect('Answers', top=26) + gut('<div>'
        + line('Maya &middot; <span style="color: #6E6862;">from 6:00 · bringing the recipe</span>', mark='dot', color=GREEN)
        + line('Sam &middot; <span style="color: #6E6862;">from 6:45 · &ldquo;could i arrive with someone?&rdquo;</span>', mark='dot', color=GREEN)
        + line('Priya &middot; <span style="color: #6E6862;">dinner only · &ldquo;at work till 6:30&rdquo;</span>', mark='dot', color=GREEN)
        + line('Dana &middot; <span style="color: #6E6862;">can&rsquo;t come</span>', mark='none', muted=True, last=True) + '</div>')
    inner += gut(actions(btn('Reply to Sam'), door('Change the plan', MUTE)), top=20)
    return phone2(inner, active='Home')

# ── C · going to John Summit, as an update ──
def c_write():
    return composer('S', PACHA, ticket_full(), where='Lower East Side', on=('where',))
def c_receive():
    inner = anchor_row('NEW YORK', 'FRIDAY 10:41 PM')
    inner += gut(share('Sam', '10:38 PM · TO FRIENDS', PACHA, extra=ticket_full(), where='Lower East Side'), top=20)
    inner += sep() + gut(share('Priya', '7:52 PM · TO FRIENDS', 'bread&rsquo;s out of the oven if anyone&rsquo;s near'), top=18)
    return phone2(inner, active='Home')
def c_after():
    inner = avatar_for(anchor_row('NEW YORK', 'SATURDAY 12:10 AM'), 'S')
    inner += gut(post('You', '10:38 PM · TO FRIENDS', PACHA, ticket_full(), 'Lower East Side', me='S') + liked_by('Nora, Maya, Dana'), top=20)
    inner += sep() + gut(original(80, author='Maya', meta='10:47 PM · TO YOU', words='coming. nora too, we&rsquo;re leaving by 3'), top=18)
    inner += gut(original(80, author='Priya', meta='10:51 PM · TO YOU', words='screaming. have fun. photos or it didn&rsquo;t happen'), top=18)
    return phone2(inner, active='Home')

# ── D · a place, and what it's good for ──
LULU = 'the upstairs room at lulu&rsquo;s is the reason to go. downstairs gets loud. best long dinner i&rsquo;ve had this year'
def good_for(items=('A long dinner', 'With parents')):
    return ''.join(f'<span style="font-size: 12px; font-weight: 500; color: {INK2}; background: rgba(27,23,20,0.05); border-radius: 999px; padding: 3px 10px; white-space: nowrap;">{c}</span>' for c in items)
def place_card(good=('A long dinner', 'With parents'), by=None):
    """The place as an attachment: name, where, what kind, and what the sender says it is good for."""
    return (f'<div style="{CARD_CSS} padding: 14px 16px;">'
            f'<div style="display: flex; gap: 12px; align-items: center;">{thumb("table", 56)}<div style="min-width: 0; flex: 1;">'
            f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 23px;">Lulu&rsquo;s</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 2px;">Carroll Gardens &middot; Italian &middot; open till 11</div></div></div>'
            f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 12px; flex-wrap: wrap;"><span class="fn" style="flex: none; margin-right: 2px;">GOOD FOR</span>{good_for(good)}</div></div>')
def d_write():
    return composer('P', LULU, place_card(), where='At Lulu&rsquo;s', on=('place', 'where'))
def d_receive():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:44 PM')
    inner += gut(share('Priya', '9:40 PM · TO FRIENDS', LULU, extra=place_card(), where='At Lulu&rsquo;s'), top=20)
    inner += sep() + gut(share('Maya', 'LAST NIGHT · TO FRIENDS', CAKE, extra=photo_thumb(110)), top=18)
    return phone2(inner, active='Home')
def d_after():
    inner = avatar_for(anchor_row('NEW YORK', 'MONDAY 8:15 AM'), 'P')
    inner += gut(post('You', 'SUNDAY 9:40 PM · TO FRIENDS', LULU, place_card(), 'At Lulu&rsquo;s', me='P') + liked_by('Nora, Sam, Dana'), top=20)
    inner += sep() + gut(original(80, author='Nora', meta='10:02 PM · TO YOU', words='booking it for my parents on the 3rd. upstairs, noted'), top=18)
    inner += gut(original(80, author='Sam', meta='MONDAY 7:50 AM · TO FRIENDS', words='downstairs is where the fun is though'), top=18)
    return phone2(inner, active='Home')
def d_places():
    """Weeks later, in Places: the place, and Priya's words beside it."""
    inner = page_bar('PLACES')
    inner += f'<div style="margin-top: 14px;">{plate("table", 140, tag="ILLUSTRATION &middot; NOT A PHOTOGRAPH").replace("margin: -16px -16px 12px -16px;", "margin: 0;")}</div>'
    inner += page_title('Lulu&rsquo;s', 'Carroll Gardens &middot; Italian &middot; open till 11')
    inner += sect('From friends', top=24) + gut(status(80, author='Priya', meta='SEPT 21 · TO FRIENDS', words=LULU)
        + f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 10px; flex-wrap: wrap;"><span class="fn" style="margin-right: 2px;">GOOD FOR</span>{good_for()}</div>' + footer('Sent from here'))
    inner += sep() + gut(status(60, author='Sam', meta='SEPT 22 · TO FRIENDS', words='downstairs is where the fun is though') + footer(), top=18)
    return phone2(inner, active='Places')

# ── the quote, into a chat with Maya ──
def quote_chat():
    inner = bar('MAYA', 'FRIDAY 10:44 PM')
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="width: 300px;">{ticket_row()}<div class="fn" style="margin-top: 4px; text-align: right;">SAM &middot; 10:38 PM &middot; TO FRIENDS</div></div></div>', top=18)
    inner += gut(bubble('are you actually going? i could do 1 if we leave by 3'), top=10)
    inner += gut(bubble_in('yes. i have a ticket. how do we get back', 'Maya'), top=8)
    inner += gut(asked_bubble('how do we get back from there at 3'), top=12)
    inner += gut(vesper_reply('The last train is 12:40, so it&rsquo;s a cab. Maya, you&rsquo;re on the way to Nora&rsquo;s.'), top=10)
    inner += gut(bubble_in('ok. cab. split it', 'Maya'), top=10)
    inner += gut(chat_field('Message Maya'), top=16)
    return phone2(inner, active='Chat')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'
def colhead(k, t, s):
    return f'<div style="width: 393px;"><div class="kick" style="color: {GOLDD};">{k}</div><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; margin-top: 4px;">{t}</div><div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">{s}</div></div>'

def build():
    heads = rowdiv([colhead('A', 'Words and pictures', 'Maya, to friends. Nothing is asked of anyone.'),
                    colhead('B', 'A gathering invitation', 'Nora, to friends. She is asking, so each person answers her. The gathering sits under her words as a card.'),
                    colhead('C', 'Where I&rsquo;ll be, with the ticket', 'Sam, to friends. An update, not an invitation. The ticket is the Life ticket, admission mode, at full size wherever the share appears.'),
                    colhead('D', 'A place I love', 'Priya, to friends. A recommendation, with what it is good for in her words. The place keeps her words: whoever opens it later sees them beside it.')], top=0)
    r1 = rowdiv([cell('FRIDAY 11:52 PM', 'A1', 'Written', 'Six words, three pictures tiled small, where she is. Gold in the toolbar is what is attached. Nothing is asked of anyone.', a_write(), (P('SENDER'),)),
                 cell('THURSDAY 9:10 PM', 'B1', 'Written', 'Her sentence, and the gathering card as they will see it. The calendar is on, so she is asking: each of them answers her, not the group. No location; the card already says where.', b_write(), (P('SENDER'),)),
                 cell('FRIDAY 10:38 PM', 'C1', 'Written', 'His sentence, his ticket, and where he is now, which is not Pacha yet. The calendar is off: an update, not an invitation. Nothing is asked of anyone.', c_write(), (P('SENDER'),)),
                 cell('SUNDAY 9:40 PM', 'D1', 'Written', 'Her sentence, sent from the table at Lulu&rsquo;s, the place under it, and two &ldquo;good for&rdquo; she chose. Hours are the world&rsquo;s; the occasion is hers. The note stays with the place for everyone she sent it to.', d_write(), (P('SENDER'),))], top=26)
    r2 = rowdiv([cell('SATURDAY 8:10 AM', 'A2', 'Nora gets it', 'Her words, the pictures, and one quiet footer: where it was sent from, then heart, comment, quote and keep as glyphs.', a_receive(), (P('RECEIVER'),)),
                 cell('THURSDAY 9:14 PM', 'B2', 'Sam gets it', 'Her words, then the gathering as a card: what, when, where, who&rsquo;s in, and the answer. His answer goes to Nora; everyone invited sees who&rsquo;s in, nobody sees who said no.', b_receive(), (P('RECEIVER'),)),
                 cell('FRIDAY 10:41 PM', 'C2', 'Nora gets it', 'His words, the ticket at full size, and the three verbs. If she&rsquo;s coming, she says so.', c_receive(), (P('RECEIVER'),)),
                 cell('SUNDAY 9:44 PM', 'D2', 'Nora gets it', 'Her words, the place, what it is good for, and the three verbs.', d_receive(), (P('RECEIVER'),))])
    r3 = rowdiv([cell('SATURDAY 10:30 AM', 'A3', 'What Maya sees', 'Who liked it, by name. One comment to her, one to everyone.', a_after(), (P('SENDER'),)),
                 cell('FRIDAY', 'B3', 'What Nora sees', 'Four answers in their words, and what each one needs from her.', b_after(), (P('SENDER'),)),
                 cell('SATURDAY 12:10 AM', 'C3', 'What Sam sees', 'Who liked it, and two comments; one of them says who&rsquo;s coming. Not who opened it.', c_after(), (P('SENDER'),)),
                 cell('MONDAY 8:15 AM', 'D3', 'What Priya sees', 'Who liked it; Nora is booking it; Sam disagrees, to everyone. Nothing tells her whether anyone went.', d_after(), (P('SENDER'),))])
    r4 = rowdiv([cell('WEEKS LATER', 'D4', 'In Places, beside the place', 'Nora opens Lulu&rsquo;s. Priya&rsquo;s words and her &ldquo;good for&rdquo; are there, with Sam&rsquo;s disagreement under them. This is how a share makes the world richer: it stays with the thing it was about.', d_places(), (P('RECEIVER'), P('PLACES'))),
                 cell('FRIDAY 10:44 PM', 'Q', 'Quoted, to Maya', 'C, pulled into a chat with a person. Nora asks Vesper how they get back; its answer is marked with who asked, and both of them see it.', quote_chat(), (P('RECEIVER'), P('PERSON CHAT · PROPOSED'))),
                 notes('THE SAME FOUR, SIDE BY SIDE', tbl(['', 'A · WORDS AND PICTURES', 'B · COME', 'C · WHERE I&rsquo;LL BE', 'D · A PLACE I LOVE'], [
                     ['<b>Asked of the receiver</b>', 'Nothing', 'An answer, to the sender', 'Nothing', 'Nothing'],
                     ['<b>Receiver can</b>', 'Like, comment, quote, keep', 'Answer, like, comment, quote', 'Like, comment, quote, keep', 'Like, comment, quote, keep; find it again on the place'],
                     ['<b>Sender sees</b>', 'Names who liked; comments', 'Each answer, in its words', 'Names who liked; comments', 'Names who liked; comments. Never who went'],
                     ['<b>Expires</b>', 'Never', 'With the event', 'With the time', 'Never; it stays on the place'],
                     ['<b>Afterwards, in Life</b>', 'Hers; yours if you kept it', 'The evening, for those who went', 'The night, for those who went', 'Under Priya, and under the place, for everyone she sent it to'],
                 ]) + N('One composer. The user never picks a type: attach a ticket or a time and it is C; attach a place with no time and it is D; ask, and it is B. The audience choice is the same every time: one friend, a group, or friends. Never public.'), w=820)])
    n2 = notes('ONE LIKE', led([
        ('WHAT', 'A heart. One kind. It means &ldquo;I saw this and I&rsquo;m glad.&rdquo; No options, no reactions row.'),
        ('WHO SEES', 'The sender, by name. Never a count, never other receivers. Opening is not a like; there is no &ldquo;seen&rdquo;.'),
        ('COMMENT', 'To the sender. On B, answers are answers, not comments. On a share sent to a group, the composer says whether the group will see it.'),
        ('KEEP', 'For you, not for the sender: puts the share into your own Life, under the person and under the place or thing it was about. The sender is not told. Board 11 shows it.'),
        ('QUOTE', 'Into a chat with a person, or your own chat with Vesper. The original keeps its author and date; on C it carries the ticket row. This is where Vesper speaks, if anywhere: in the chat, when asked, not under the share.'),
    ]), w=560)
    n3 = notes('THE ARTIFACTS ARE THE EXISTING ONES', led([
        ('TICKET', 'The Life ticket (a typed original keeps its type): admission mode at full size wherever the share appears; the row only when it is quoted into a chat. Copied from the Life project, unmodified.'),
        ('WHERE FROM', 'Every share can carry where it was sent from: a neighborhood by default, the place itself when the sender is at it, off in one tap, never an address. It is the sender&rsquo;s line, not a live location. On C it is where Sam is now, not where he will be; on D it is the place, which is why the note can land there.'),
        ('PLACE', 'The place card: name, where, kind, hours from the world, and &ldquo;good for&rdquo; in the sender&rsquo;s words, never inferred. It is the same object Places already has; the share attaches the words to it. Priya is never told who went.'),
        ('INVITATION', 'Not the Social 03 / Plans 04 InviteCard: as a share it read as a form. Here the gathering is an attachment under Nora&rsquo;s words, the same shape as the photo and the ticket: what, when, where, who&rsquo;s in, and the answer on the card. The full invitation page still exists behind it.'),
    ]), w=560)
    n4 = notes('OPEN', led([
        ('PERSON CHATS', 'A chat with a person inside Vesper is proposed and does not exist.'),
        ('WHOSE CONTEXT', 'In Q, Vesper knows Maya&rsquo;s ticket and Nora&rsquo;s address. On what permission it may say both to both is unruled.'),
        ('A LINE UNDER THE SHARE', 'An earlier version put one line from Vesper under the words (distance, a clash, who else is going). Removed on 2026-09-21 as noise. If it ever returns, it is only where Vesper knows something about the reader&rsquo;s own life the sender could not.'),
        ('WHO SEES WHO&rsquo;S IN', 'Drawn: everyone invited sees who is in, never who declined. Whether that holds when the audience is all friends rather than a named group is the open part.'),
        ('PACHA', 'The venue and the act are real names the founder used as the example; the ticket details around them are fixtures.'),
    ]), w=560)
    body = heads + r1 + r2 + r3 + r4 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12); flex-wrap: wrap;">' + n2 + n3 + n4 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(4, (560, 560))}px; min-height: {hh("10", 4400)}px; background: #D8D1C5; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('10 &middot; SHARING &middot; THE SOCIAL FOUNDATION', 'Four shares, seen three times',
                   'Words and pictures; a gathering invitation; where I&rsquo;ll be tonight, with the ticket; a place I love, and what it is good for. One shape for all four: the author, their words, and the thing attached under the words, smaller. Each one written, received, and as the sender sees it afterwards. '
                   'On the receiving side, the verbs everyone knows: one like, a comment, a quote into a chat with a person, and keep, for yourself. Nothing from Vesper under the share; it speaks in the chat, when asked. Drawn, not tested with anyone.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('10 - Sharing', html)

if __name__ == '__main__':
    build()
