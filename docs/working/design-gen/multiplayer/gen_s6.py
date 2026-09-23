"""15 · Shared with Maya. The thread and Life's shared record are one object, drawn in Life's own grammar: Life board 07's
stylesheet and panels are used verbatim (life/07.html, downloaded from Life e72a2fd2), and only what is new is changed:
an Ours row and section, her note as a post rather than a quotation (decision 2), the chat as a conversation row, and
Ours pages built from Life's section heads, rows and withdrawal wording. The Life project itself is not modified."""
import os, re
from mp_common import write, hh
from gen_s1 import paper_map

HERE = os.path.dirname(os.path.abspath(__file__))
L = open(os.path.join(HERE, 'life', '07.html')).read()
PREFIX = L[:L.index('<div class="cb"')]
SUFFIX = '\n</x-dc>\n</body>\n</html>\n'

def match_div(s, start):
    """Return the end index of the <div ...> that opens at start."""
    depth, i = 0, start
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0: return start + m.end()
    raise ValueError('unbalanced')
def panel_phone(caption):
    a = L.index('<div class="cphone">', L.index(caption))
    return L[a:match_div(L, a)]

P_REST = panel_phone('Sunday &middot; the note arrives')
P_OPEN = panel_phone('Opened &middot; her note, then the record')

# ── Life's own parts, lifted from the opened record ──
CHROME = P_OPEN[P_OPEN.index('<div style="padding: 20px 22px 0 22px;'):P_OPEN.index('<div style="display:flex; flex-direction:column; gap:6px; padding-top:4px;">')]
TAB = P_OPEN[P_OPEN.index('<div style="flex-grow:1;"></div>'):P_OPEN.rindex('</div></div>')]
PHONE_OPEN = '<div class="cphone"><div style="width: 393px; background: var(--paper); color: var(--ink); font-family: var(--sans); box-sizing: border-box; display: flex; flex-direction: column;">'
CHEV = '<svg class="chev" width="13" height="13" viewBox="0 0 13 13" fill="none"><path d="M4.5 2.5L9 6.5L4.5 10.5" stroke="#B5AFA5" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def G(path):
    return f'<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex:none; opacity:0.62;"><path d="{path}" stroke="#1B1714" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FORK = G('M5 1.8 V6 M7.5 1.8 V6 M10 1.8 V6 M5 6 Q7.5 7.6 10 6 M7.5 6.8 V13.2')
GLASS = G('M4.4 1.8 H10.6 L9.8 6.4 Q9.4 8.6 7.5 8.6 Q5.6 8.6 5.2 6.4 Z M7.5 8.6 V12.4 M5.2 12.8 H9.8')
MARK = G('M4.2 1.8 H10.8 V13.2 L7.5 10.6 L4.2 13.2 Z')
POT = G('M2.4 6.4 H12.6 Q12.2 11.6 7.5 11.6 Q2.8 11.6 2.4 6.4 Z M9.8 5.6 L12.4 2')
FILM = G('M2 3.4 H13 V11.6 H2 Z M2 5.8 H13 M2 9.2 H13')
WAVE = G('M1.6 6 Q3.6 4.2 5.6 6 T9.6 6 T13.4 6 M1.6 9.6 Q3.6 7.8 5.6 9.6 T9.6 9.6 T13.4 9.6')
BUBBLE = G('M2 3 H13 V10 H7 L4 12.6 V10 H2 Z')

def phone(inner): return PHONE_OPEN + inner + TAB + '</div></div>'
def head(kicker, title, sub):
    return (CHROME + '<div style="display:flex; flex-direction:column; gap:6px; padding-top:4px;">'
            f'<span class="kicker" style="color:var(--mute);">{kicker}</span>'
            f'<span style="font-family:var(--serif); font-weight:600; font-size:26px; line-height:30px; letter-spacing:-0.5px;">{title}</span>'
            f'<span style="font-family:var(--serif); font-weight:600; font-size:19px; line-height:25px; letter-spacing:-0.3px; color:var(--mute);">{sub}</span></div></div>')
def sec(k, count='', top=34):
    c = f'<span class="barmeta" style="margin-left:auto;">{count}</span>' if count else ''
    return f'<div style="margin:{top}px 22px 0 22px; border-top:1px solid var(--hairline); padding-top:10px; display:flex; align-items:baseline;"><span class="kicker" style="color:var(--mute);">{k}</span>{c}</div>'
def row1(glyph, text, meta, color=None):
    mc = f' style="color:{color};"' if color else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:44px; border-bottom:1px solid var(--hair-thin);">'
            f'{glyph}<span class="child" style="flex-grow:1;">{text}</span><span class="meta"{mc}>{meta}</span>{CHEV}</div>')
def row2(title, sub, meta, color=None, glyph=''):
    mc = f' style="color:{color};"' if color else ''
    return (f'<div style="margin:0 22px; display:flex; align-items:center; gap:12px; min-height:60px; border-bottom:1px solid var(--hair-thin);">{glyph}'
            f'<div style="flex-grow:1; display:flex; flex-direction:column; gap:2px; padding:8px 0;"><span style="font-family:var(--serif); font-size:16px; line-height:21px; font-weight:600;">{title}</span><span class="rsub">{sub}</span></div>'
            f'<span class="meta"{mc}>{meta}</span>{CHEV}</div>')
def door(t, top=12): return f'<div style="margin:{top}px 22px 0 22px; display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium">{t}</span></div>'
def line(t, top=12): return f'<div style="margin:{top}px 22px 0 22px; font-family:var(--sans); font-size:13px; line-height:18px; color:var(--mute);">{t}</div>'
def voice(t, top=14): return f'<div class="voice" style="margin:{top}px 22px 0 22px;">{t}</div>'
def strip(inner): return f'<div class="cctx"><div style="width:393px; background:var(--card); border:1px solid var(--hairline); border-radius:12px; padding:16px 20px 18px 20px; box-sizing:border-box;">{inner}</div></div>'
def panel(cap, body, note, new=False):
    pill = '<span class="cpill rev">New</span>' if new else '<span class="cpill cur">From Life 07</span>'
    return (f'<div class="cpanel" style="width:393px;"><div style="display:flex;gap:8px;align-items:center"><span class="ccap">{cap}</span>{pill}</div>'
            f'{body}<div class="cnote">{note}</div></div>')

# ── 1 · Life's People lens, verbatim, plus one row: Ours ──
def rest():
    p = P_REST
    anchor = '</div></div><div class="voice">Your account of the time shared'
    assert anchor in p
    ours = (f'\n      <div style="display:flex; align-items:center; gap:12px; min-height:36px;">\n        {MARK}\n'
            f'        <span class="child" style="flex-grow:1;">Ours &middot; our places, the pasta</span>\n        <span class="meta" style="color:var(--gold-deep);">2</span>\n        {CHEV}\n      </div>')
    return p.replace(anchor, '</div>' + ours + anchor[len('</div>'):], 1)

# ── 2 · Chat, as Life draws it: a context strip ──
def chat_strip():
    return strip('<div class="kicker" style="color:var(--mute);">CHAT &middot; MAYA &middot; NOV 2</div>'
        '<div style="font-family:var(--sans); font-size:15px; line-height:21px; color:var(--ink); padding-top:10px;">saw a dog that looked exactly like sam</div>'
        '<div style="font-family:var(--sans); font-size:15px; line-height:21px; color:var(--mute); padding-top:6px;">You: i need to see this dog immediately</div>'
        '<div style="margin-top:12px; padding-top:10px; border-top:1px solid var(--hair-thin); display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium">Shared with Maya</span></div>')

# ── 3 · the record opened: her note as a post, Ours, the conversation ──
def opened():
    p = P_OPEN
    q_start = p.index('<div style="font-family:var(--serif); font-size:17px; line-height:24px; font-style:italic; color:var(--ink);">')
    q_end = p.index('</div>', q_start) + 6
    p = p[:q_start] + ('<div style="font-family:var(--sans); font-size:17px; line-height:24px; color:var(--ink);">paris was the same heat. we gave up on the afternoons and stayed by the water until it cooled down. '
                       'you two would have liked the river after eight</div>') + p[q_end:]
    w = '<span class="vdl-door vk-t-bodySmMedium">Write back, if you want to</span></div>'
    assert w in p
    ours = (sec('OURS', '2 &middot; MADE TOGETHER', 34)
            + row2('Our places', 'Five places, three been to together &middot; since Sept 30', '5', glyph=MARK)
            + row2('The Sorrento pasta', 'The version that held &middot; three attempts', 'OCT 19', glyph=POT)
            + door('Start something with Maya'))
    p = p.replace(w, w + ours, 1)
    src = sec('THE SOURCES')
    assert src in p
    conv = sec('THE CONVERSATIONS', '1') + row2('Maya &amp; you', 'saw a dog that looked exactly like sam &middot; opens in Chat', 'NOV 2', glyph=BUBBLE)
    p = p.replace(src, conv + src, 1)
    return p

# ── 4 · Ours, as a page in Life's grammar ──
def our_places(offer=False, left=False):
    inner = head('OURS &middot; WITH MAYA &middot; SINCE SEPT 30', 'Our places', 'Three of five, been to together.' if not left else 'Three places, yours now.')
    inner += f'<div style="margin:18px 22px 0 22px; border-radius:12px; overflow:hidden; border:1px solid var(--hairline);">{paper_map(120, ((0.18, 0.62), (0.36, 0.38), (0.56, 0.66), (0.72, 0.42), (0.86, 0.7)) if not left else ((0.18, 0.62), (0.56, 0.66), (0.86, 0.7)), 349)}</div>'
    if offer:
        inner += ('<div style="margin:18px 22px 0 22px;" class="cstudy"><div style="padding:14px 16px;">'
                  '<div class="kicker" style="color:var(--gold-deep);">FROM YOUR RECORD</div>'
                  '<div style="font-family:var(--serif); font-size:18px; line-height:23px; font-weight:600; padding-top:6px;">Lulu&rsquo;s, on Oct 12?</div>'
                  '<div class="rsub" style="font-size:13px; line-height:18px; padding-top:4px;">A card payment there at 9:10, and two photographs Maya shared with you from that evening.</div>'
                  '<div style="display:flex; gap:18px; align-items:center; padding-top:12px;"><span class="vdl-door vk-t-bodySmMedium">Yes, together</span><span class="vdl-door vk-t-bodySmMedium" style="color:var(--mute);">Not that night</span></div></div></div>')
    GREEN = 'var(--green)'
    if not left:
        inner += sec('THE PLACES', '5', 30)
        inner += row2('Hato', 'the broth is stupid good &middot; Maya, Oct 5', 'BEEN &middot; OCT 12', GREEN, POT)
        inner += row2('Lulu&rsquo;s', 'upstairs. priya swears by it and she was right &middot; you, Sept 30', 'SEPT 30' if offer else 'BEEN &middot; OCT 12', None if offer else GREEN, FORK)
        inner += row2('The greenmarket', 'bread goes first. get there by 9 &middot; Maya, Oct 8', 'BEEN &middot; OCT 18', GREEN, MARK)
        inner += row2('The Lantern', 'one film a week, one kind of cake &middot; you, Sept 30', 'SEPT 30', None, FILM)
        inner += row2('The pier at low water', 'for when one of us needs to walk it off &middot; you, Oct 20', 'OCT 20', None, WAVE)
    else:
        inner += sec('THE PLACES', '3', 30)
        inner += line('Maya stopped sharing her two places on Dec 4. Everything you added is as it was.', 12)
        inner += row2('Lulu&rsquo;s', 'upstairs. priya swears by it and she was right &middot; you, Sept 30', 'BEEN &middot; OCT 12', GREEN, FORK)
        inner += row2('The Lantern', 'one film a week, one kind of cake &middot; you, Sept 30', 'SEPT 30', None, FILM)
        inner += row2('The pier at low water', 'for when one of us needs to walk it off &middot; you, Oct 20', 'OCT 20', None, WAVE)
    inner += door('Add a place') if not left else ''
    return phone(inner)

# ── 5 · a year on, inside the record ──
def a_year():
    inner = head('SHARED RECORD &middot; SINCE 2019', 'Shared with Maya', 'Nineteen shared episodes across seven years.')
    inner += sec('THIS TIME, LAST YEAR', 'OCT 12, 2026', 26)
    inner += row2('Hato, the first time', 'Both of you &middot; four photographs &middot; in Our places', 'OCT 12', None, POT)
    inner += sec('FROM MAYA &middot; YESTERDAY', 'HERS &middot; SHE CAN TAKE IT BACK', 30)
    inner += '<div style="margin:12px 22px 0 22px; font-family:var(--sans); font-size:17px; line-height:24px; color:var(--ink);">the broth is still stupid good</div><div class="meta" style="margin:6px 22px 0 22px; white-space:normal;">HER NOTE &middot; AT HATO</div>'
    inner += door('Write back, if you want to', 10)
    inner += sec('OURS', '4 &middot; MADE TOGETHER')
    inner += row2('Our places', 'Fourteen places, nine been to together', '14', glyph=MARK)
    inner += row2('The Sorrento pasta', 'The version that held', 'OCT 19', glyph=POT)
    return phone(inner)

def build():
    cells = [
        panel('People &middot; a note arrives', rest(), 'Life&rsquo;s People lens exactly as board 07 draws it, with one added row inside Maya&rsquo;s record: Ours, the things the two of you made on purpose.'),
        panel('Chat &middot; the same person', chat_strip(), 'Chat stays a chat. Her name at the top of the conversation opens the same shared record; Life draws Chat as a strip, so it is drawn as one here.', True),
        panel('Opened &middot; her note, Ours, the conversation', opened(), 'Board 07&rsquo;s record, three changes: her note as a post, not a quotation (decision 2); an Ours section after her note; the chat as a conversation row, opening in Chat.', True),
        panel('Ours &middot; our places', our_places(), 'Ours as a page in Life&rsquo;s grammar: a kicker, a serif title, a map because it is a list of places, and each place in its adder&rsquo;s words. Been is green, with a date.', True),
        panel('Ours &middot; been, offered from the record', our_places(offer=True), 'The record has an evening at Lulu&rsquo;s. The page says what it found and asks once. You answer; nothing is asserted about you.', True),
        panel('Ours &middot; when she stops sharing', our_places(left=True), 'Life&rsquo;s withdrawal wording: said once, where the missing thing would have been. Each entry is its adder&rsquo;s and left with her; yours are as they were (decision 1).', True),
        panel('A year on &middot; inside the record', a_year(), 'Life&rsquo;s &ldquo;this time, last year&rdquo;, inside the record, never pushed. Her newest note sits under it, as a post.', True),
    ]
    rows = '<div class="crow">' + ''.join(cells) + '</div>'
    def dec(n, t, body): return f'<div style="width:393px;"><div class="ccap">{n} &middot; {t}</div><div class="cn" style="padding-top:6px;">{body}</div><div class="cnote" style="padding-top:6px;">RULED &mdash; not yet &mdash;</div></div>'
    decisions = ('<div class="csec"><div class="ceye">Four decisions, each with a recommendation</div><div class="crow">'
        + dec('1', 'Ownership', 'Life keeps parallel accounts; the first Ours list drew one shared list. <b>Recommended:</b> Ours is one list made of entries; each entry is its adder&rsquo;s and leaves with them. The shared record stays parallel, as Life rules.')
        + dec('2', 'Quote or post', 'Life 07 sets her note in serif italics with quotation marks. <b>Recommended:</b> a friend&rsquo;s note looks the same on Home and in Life: a post, as drawn here.')
        + dec('3', 'One composer', 'Life 04c shares through the Social project&rsquo;s preview; board 10 drew its own composer. <b>Recommended:</b> one composer, board 10&rsquo;s.')
        + dec('4', 'The ledger', 'Life avoids progress and streaks. <b>Recommended:</b> Ours counts only what happened (places, been, since) and asks nothing; nothing decays.')
        + '</div></div>')
    notdrawn = ('<div class="csec"><div class="ceye">What stays as Life has it</div><div class="cn" style="padding-top:8px; max-width:1200px;">'
        'The record is named for the relationship, not the person: &ldquo;Shared with Maya&rdquo;, no portrait, no profile. Groups have no record of their own; what four people lived is in each person&rsquo;s shared record and in Life&rsquo;s occasions. '
        'People met along the way get a row and nothing more. The Life project is unchanged; if these are ruled, its board 07 gains the Ours row and section and loses the quotation marks.</div></div>')
    top = ('<div style="padding:0 0 10px 0;max-width:1060px"><div style="display:flex;align-items:center;gap:12px"><span class="ceye">15 &middot; Shared with Maya</span><span class="cpill rev">Review</span></div>'
           '<div class="ctitle" style="padding-top:8px">The thread and the shared record are one thing.</div>'
           '<div class="cq" style="padding-top:6px">What does the record hold once the two of you also make things together, and talk?</div>'
           '<div class="cn" style="padding-top:8px;max-width:980px">Drawn in Life&rsquo;s own grammar: board 07&rsquo;s stylesheet and panels, used verbatim. What is new is an Ours section in the shared record, Ours as a page, the chat as a conversation row, and her note as a post. Drawn, not tested with anyone.</div></div>')
    html = PREFIX + f'<div class="cb" style="width:1760px;padding:38px;min-height:{hh("15", 3400)}px">' + top + rows + decisions + notdrawn + '</div>' + SUFFIX
    return write('15 - With Maya', html)

if __name__ == '__main__':
    build()
