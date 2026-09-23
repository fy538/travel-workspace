"""14 · Ours. A thing two people own: a page, not a chat. The first one is a list of places. It grows only when one of
them adds something, in their own words; it records only what they actually did; nothing counts up, nothing decays,
nothing has to be kept alive. A year later it is a record of the friendship. Founder, 2026-09-21: "a way better
friend streak, not a daily habit, something that's actually more memorable"."""
from mp_kit2 import *
from gen_merge import daycap
from gen_p2_common import illo
import gen_s1 as S
from gen_s1 import status, photo_grid, photo_thumb, verbs, where_line, CARD_CSS, page_bar, paper_map, composer, footer
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')

def cover(kind='map', h=160, tag_='MAP &middot; ILLUSTRATION'):
    art = paper_map(h) if kind == 'map' else illo(kind, h, 393)
    return (f'<div style="height: {h}px; position: relative; overflow: hidden; border-radius: 0;">{art}'
            f'<span style="position: absolute; left: 22px; bottom: 10px; {MONO} font-size: 9px; letter-spacing: 1px; color: rgba(244,238,221,0.9); background: rgba(27,23,20,0.55); padding: 2px 6px; border-radius: 4px;">{tag_}</span></div>')
def mosaic(kinds, h=150):
    n = len(kinds); w = 393 // n
    return (f'<div style="height: {h}px; display: flex; gap: 2px; overflow: hidden;">' + ''.join(f'<div style="width: {w}px; height: {h}px; overflow: hidden;">{illo(k, h, w)}</div>' for k in kinds) + '</div>')
def title_block(t, faces_, ledger):
    return (f'<div style="padding: 18px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;"><span style="{MONO} font-size: 9px; letter-spacing: 1.2px; color: {GOLDD};">OURS</span>{facepile(faces_, 22, -7)}</div>'
            f'<div style="{SERIF} font-weight: 600; font-size: 30px; line-height: 34px; margin-top: 8px; color: {INK};">{t}</div>'
            f'<div class="fn" style="margin-top: 8px; letter-spacing: 1px;">{ledger}</div></div>')
def entry(kind, name, where, words, by, when, been=None, last=False):
    """One place, in the adder's words. Been is a fact one of them set, with a date; never inferred."""
    bb = '' if last else f' border-bottom: 1px solid rgba(27,23,20,0.08);'
    b = f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 6px;"><span style="width: 7px; height: 7px; border-radius: 50%; background: {GREEN}; flex: none;"></span><span class="fn" style="color: {GREEN};">BEEN &middot; {been}</span></div>' if been else ''
    return (f'<div style="display: flex; gap: 14px; align-items: flex-start; padding: 14px 0;{bb}">{thumb(kind, 60)}'
            f'<div style="flex: 1; min-width: 0;"><div style="{SERIF} font-weight: 600; font-size: 18px; line-height: 22px; color: {INK};">{name}</div>'
            f'<div style="font-size: 13px; line-height: 18px; color: {MUTE}; margin-top: 1px;">{where}</div>'
            f'<div style="font-size: 15px; line-height: 21px; color: {INK}; margin-top: 6px;">{words}</div>'
            f'<div class="fn" style="margin-top: 4px;">{by.upper()} &middot; {when}</div>{b}</div></div>')
def doors_row():
    """Three soft buttons for the page: add a place, see them on the map, send the list."""
    from gen_s1 import _g, CAL_P, PIN_P, QUOTE_P
    PLUS = '<path d="M10 4v12M4 10h12"/>'
    def pill(p, t, c):
        return (f'<span style="display: inline-flex; align-items: center; gap: 7px; height: 34px; padding: 0 14px; border-radius: 17px; {CARD_CSS}">'
                f'{_g(p, c, 15)}<span style="font-size: 14px; font-weight: 500; color: {c};">{t}</span></span>')
    return f'<div style="display: flex; gap: 10px;">{pill(PLUS, "Add", GOLDD)}{pill(PIN_P, "Map", INK)}{pill(QUOTE_P, "Send", INK)}</div>'

# ── 1 · the page ──
def the_page():
    inner = page_bar('LIFE &middot; WITH MAYA')
    inner += f'<div style="margin-top: 14px;">{cover()}</div>'
    inner += title_block('Our places', ['N', 'M'], 'SINCE SEPT 30 &middot; 5 PLACES &middot; 3 BEEN &middot; LAST TOGETHER OCT 12')
    inner += gut(doors_row(), top=14)
    inner += gut(entry('noodles', 'Hato', 'Cobble Hill &middot; ramen', 'the broth is stupid good', 'Maya', 'OCT 5', been='OCT 12 &middot; BOTH OF YOU')
                 + entry('table', 'Lulu&rsquo;s', 'Carroll Gardens &middot; Italian', 'upstairs. priya swears by it and she was right', 'Nora', 'SEPT 30', been='OCT 12 &middot; BOTH OF YOU')
                 + entry('film', 'The Lantern', 'Court Street &middot; cinema', 'one film a week and exactly one kind of cake. sam found it', 'Nora', 'SEPT 30')
                 + entry('market', 'The greenmarket', 'Grand Army Plaza &middot; Saturdays', 'bread goes first. get there by 9 or don&rsquo;t bother', 'Maya', 'OCT 8', been='OCT 18 &middot; MAYA')
                 + entry('pier', 'The pier at low water', 'Red Hook', 'for when one of us needs to walk it off', 'Nora', 'OCT 20', last=True), top=6)
    return phone2(inner, active='Life')

# ── 2 · marking been, the morning after ──
def been_morning():
    inner = page_bar('OUR PLACES &middot; HATO')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 26px; line-height: 30px;">Hato</div><div style="font-size: 14px; color: {MUTE}; margin-top: 2px;">Cobble Hill &middot; ramen &middot; added by Maya, Oct 5</div>', top=14)
    inner += gut(f'<div style="font-size: 15px; line-height: 21px;">the broth is stupid good</div><div class="fn" style="margin-top: 4px;">MAYA &middot; OCT 5</div>', top=14)
    inner += gut(box(f'<div style="{SERIF} font-weight: 600; font-size: 17px; line-height: 22px;">Were you there last night?</div>'
        + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 6px;">Maya marked it. If you were too, it goes down as both of you, and your photos from last night sit here with hers.</div>'
        + f'<div style="margin-top: 12px;">{actions(btn("Yes, both of us"), door("Just Maya", MUTE))}</div>'), top=16)
    inner += gut(photo_grid(2, 120, 'PHOTO &middot; MAYA'), top=14)
    return phone2(inner, active='Life')

# ── 3 · a year later ──
def a_year():
    inner = page_bar('LIFE &middot; WITH MAYA')
    inner += f'<div style="margin-top: 14px;">{mosaic(["noodles", "table", "pier", "market", "film"], 150)}</div>'
    inner += title_block('Our places', ['N', 'M'], 'SINCE SEPT 30, 2026 &middot; 14 PLACES &middot; 9 BEEN &middot; 31 PHOTOS')
    inner += gut(doors_row(), top=14)
    inner += sect('This year', top=20) + gut('<div>'
        + line('Hato &middot; <span style="color: #6E6862;">been 4 times · the first was Oct 12</span>', mark='dot', color=GREEN)
        + line('The pier &middot; <span style="color: #6E6862;">Nov 3, after the thing with Sam</span>', mark='dot', color=GREEN)
        + line('Lulu&rsquo;s &middot; <span style="color: #6E6862;">Maya&rsquo;s birthday, upstairs, Feb 14</span>', mark='dot', color=GREEN)
        + line('The greenmarket &middot; <span style="color: #6E6862;">Maya, 6 Saturdays · you, 0</span>', mark='dot', color=GREEN, last=True) + '</div>')
    inner += sect('Still to do') + gut('<div>' + line('The Lantern &middot; <span style="color: #6E6862;">a year on the list</span>', mark='hollow', color=MUTE) + line('Four more', mark='hollow', color=MUTE, last=True) + '</div>')
    return phone2(inner, active='Life')

# ── 4 · sending it ──
def list_card():
    return (f'<div style="{CARD_CSS} overflow: hidden;">{paper_map(96, ((0.2, 0.6), (0.4, 0.4), (0.62, 0.66), (0.8, 0.45)))}'
            f'<div style="padding: 12px 16px 14px 16px;"><div class="fn">OURS &middot; NORA &amp; MAYA</div><div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 24px; margin-top: 4px;">Our places</div>'
            f'<div style="font-size: 13px; color: {MUTE}; margin-top: 2px;">14 places &middot; 9 been &middot; Brooklyn</div></div></div>')
def send_it():
    return composer('N', 'for when you&rsquo;re here in january. maya and i have been working on this', list_card(), to='Dana', faces_=('D',))

# ── 5 · starting one ──
def start_one():
    inner = anchor_row('NEW YORK', 'SEPT 30')
    inner += gut(S.share('Priya', 'SUNDAY · TO THE SORRENTO FOUR', S.LULU, extra=S.place_card(), where='At Lulu&rsquo;s', kept=True), top=20)
    inner += gut((f'<div style="{CARD_CSS} padding: 14px 16px;"><div class="kickm" style="margin-bottom: 8px;">ADD TO</div>'
        + f'<div style="padding: 10px 0; border-bottom: 1px solid rgba(27,23,20,0.08); display: flex; align-items: center; gap: 10px;">{facepile(["N","M"], 20, -6)}<span style="font-size: 15px;">Our places <span style="color: {MUTE};">&middot; with Maya &middot; 2</span></span></div>'
        + f'<div style="padding: 10px 0; border-bottom: 1px solid rgba(27,23,20,0.08); display: flex; align-items: center; gap: 10px;">{facepile(["N"], 20, -6)}<span style="font-size: 15px;">Places to try <span style="color: {MUTE};">&middot; just you &middot; 11</span></span></div>'
        + f'<div style="margin-top: 10px;">{door("New, with someone", GOLDD)}</div></div>'), top=12)
    return phone2(inner, active='Home')

# ── 6 · the same shape, other things ──
def method_page():
    inner = page_bar('LIFE &middot; WITH MAYA')
    inner += f'<div style="margin-top: 14px;">{cover("noodles", 120, "PHOTO &middot; MAYA &middot; ATTEMPT 3")}</div>'
    inner += title_block('The Sorrento pasta', ['N', 'M'], 'SINCE OCT 12 &middot; 3 ATTEMPTS &middot; HELD ON THE SECOND')
    steps = [('1', 'Pan off the heat before any cheese goes in.', 'MAYA · OCT 12'), ('2', 'Cheese in handfuls, stirring between each.', 'MAYA · OCT 12'), ('3', 'Full pepper. Half is bland; ask Nora.', 'MAYA · OCT 19'), ('4', 'Zest at the very end, off the heat.', 'DANA, VIA NORA · OCT 20')]
    inner += gut(''.join(f'<div style="display: grid; grid-template-columns: 22px 1fr; column-gap: 10px; padding: 9px 0; border-bottom: 1px solid rgba(27,23,20,0.07);"><span class="fn">{n}</span><div><div style="font-size: 15px; line-height: 21px;">{t}</div><div class="fn" style="margin-top: 2px;">{by}</div></div></div>' for n, t, by in steps), top=14)
    return phone2(inner, active='Life')
def todo_page():
    inner = page_bar('LIFE &middot; WITH SAM')
    inner += title_block('Before one of us moves', ['N', 'S'], 'SINCE AUG &middot; 7 THINGS &middot; 2 DONE')
    items = [('Swim at the Red Hook pool at 7am', 'SAM · AUG 3', 'DONE · AUG 24 · BOTH OF YOU'), ('The Staten Island ferry, there and back, no reason', 'NORA · AUG 3', 'DONE · SEPT 6'), ('Cook the pasta for Maya&rsquo;s parents', 'NORA · OCT 20', ''), ('See a film at the Lantern', 'SAM · SEPT 18', '')]
    inner += gut(''.join(f'<div style="padding: 12px 0; border-bottom: 1px solid rgba(27,23,20,0.07);"><div style="font-size: 15px; line-height: 21px; color: {INK};">{t}</div><div class="fn" style="margin-top: 3px;">{by}</div>' + (f'<div class="fn" style="margin-top: 3px; color: {GREEN};">{d}</div>' if d else '') + '</div>' for t, by, d in items), top=12)
    return phone2(inner, active='Life')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))
def rowdiv(cells, top=8):
    return f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: {top}px;">' + ''.join(cells) + '</div>'

def build():
    r1 = rowdiv([cell('OCT 20', '1', 'The page', 'A cover, a title, the two of them, and a ledger of what has actually happened. Each place in the adder&rsquo;s words, with who and when. Been is a green line with a date.', the_page(), (P('OURS'), P('LIFE'))),
                 cell('OCT 13 · MORNING', '2', 'Marking been', 'Maya marked Hato last night. Nora is asked once: both of you? Her photos join Maya&rsquo;s. Nothing is inferred from a phone&rsquo;s location.', been_morning(), (P('OURS'), P('LIFE'))),
                 cell('A YEAR ON', '3', 'What it becomes', 'Fourteen places, nine been, thirty-one photos, and the year in a few lines. This is the streak: not days in a row, but things done together, in your own words. Nothing here was earned by opening the app.', a_year(), (P('OURS'), P('LIFE')))], top=0)
    r2 = rowdiv([cell('DEC 2', '4', 'Sending it', 'The same composer as board 10, to Dana. She gets the list as it is today, with both their words on each place; she can&rsquo;t add to it. It stays Nora&rsquo;s and Maya&rsquo;s.', send_it(), (P('OURS'), P('SHARE'))),
                 cell('SEPT 30', '5', 'Starting one', 'The keep glyph on a friend&rsquo;s share offers where to put it. A list with someone starts from a thing, not from a blank page; &ldquo;New, with someone&rdquo; is the whole setup.', start_one(), (P('OURS'), P('HOME'))),
                 cell('OTHER SHAPES', '6', 'The same page, for other things', 'A method with Maya; a list of things to do with Sam. Same cover, same faces, same ledger, same words-with-names.', method_page() + '<div style="height: 18px;"></div>' + todo_page(), (P('OURS'), P('LIFE')))])
    n1 = notes('WHY IT IS NOT A STREAK', led([
        ('NOTHING COUNTS UP', 'The ledger counts places and times been. Not days, not opens, not messages. Two friends who see each other twice a year have a real list.'),
        ('NOTHING DECAYS', 'A list untouched for six months is exactly as it was. No reminder, no &ldquo;keep it alive&rdquo;, no expiring flame.'),
        ('IT GROWS BY LIVING', 'It changes only when one of them adds a place, in their words, or says they were there. Both are deliberate. Nothing is inferred from location or from the chat.'),
        ('IT IS THEIRS', 'Two owners. Either adds, either marks been, either removes. Nobody else can add, even when it is sent.'),
    ]), w=560)
    n2 = notes('WHY IT IS MEMORABLE', led([
        ('WORDS WITH NAMES', '&ldquo;the broth is stupid good · MAYA · OCT 5&rdquo; is the unit. Not a pin. A year of these reads like a friendship.'),
        ('DATES THAT MEAN SOMETHING', 'Been-dates are the nights. &ldquo;The pier, Nov 3, after the thing with Sam&rdquo; is what a person remembers; the page keeps it.'),
        ('PHOTOS FROM BOTH', 'When both were there, both people&rsquo;s photos of that night sit on the entry. The list becomes the album without anyone making one.'),
        ('IT IS A PAGE', 'Serif, paper, stamps, a cover. It looks like a kept thing in Life because it is one, and nothing like the chat.'),
    ]), w=560)
    n3 = notes('NOT DRAWN, AND OPEN', led([
        ('THREE OR MORE', 'A list owned by four is the same page with a harder ledger. Not drawn.'),
        ('LOOKING BACK', 'Whether the page ever says &ldquo;a year ago tonight&rdquo; on its own. Leaning no: the page is there when you open it.'),
        ('SENDING', 'Whether sending needs both owners. Frame 4 offers &ldquo;Ask Maya first&rdquo; and does not require it.'),
        ('THE MAP', 'The Map door opens Places with only these pins. Not drawn here; it is Places&rsquo; existing scope chooser.'),
    ]), w=400)
    body = r1 + r2 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12); flex-wrap: wrap;">' + n1 + n2 + n3 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(3, (560, 560, 400))}px; min-height: {hh("14", 3600)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('14 &middot; OURS', 'A list two people own',
                   'A page, not a chat. Our places, with Maya: each place in the adder&rsquo;s words, when they were there, both people&rsquo;s photos. It grows only when one of them does something and it never decays. '
                   'A year later it is a record of the friendship. The same page works for a method or a list of things to do. Drawn, not tested with anyone.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('14 - Ours', html)

if __name__ == '__main__':
    build()
