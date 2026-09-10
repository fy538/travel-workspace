"""14 - Received from Places: the exact frames Places supplies to the Entity lab's September 9 comparison.
Drawn in the Entity lab's own shell, sliced from its board 09, so the difference is the body and nothing else.
The last frame is Places 08.13 as drawn there, in the Places kit, because understanding of an unvisited place is what it demonstrates."""
import re, html as _h
SRC = open('entity/09.html').read()
PHONE = open('entity/_phoneA.html').read()
HEAD = SRC[:SRC.index('<div style="width:')]
TAIL = '</x-dc>\n</body>\n</html>\n'
BOARD_OPEN = re.search(r'<div style="width:\s*\d+px;[^"]*">', SRC).group(0).replace("width: 1560px", "width: 1820px")
IX = {k: PHONE.index(k) for k in ['<div class="ctx">', '<div class="pair rule">', '<div class="body">', '<div class="srcs">', '<div class="verbs">', '<div class="two">', '<div class="wrow">']}
PRE   = PHONE[:IX['<div class="ctx">']]
POST  = PHONE[IX['<div class="wrow">']:]
def ctx(t): return f'<div class="ctx"><i></i>{t}</div>'
def pair(cells): return '<div class="pair rule">' + ''.join(f'<div><div class="l">{l}</div><div class="v">{v}</div><div class="s">{s}</div></div>' for l, v, s in cells) + '</div>'
def body(paras): return '<div class="body">' + ''.join(f'<div class="para">{p}</div>' for p in paras) + '</div>'
def srcs(items): return '<div class="srcs">' + ''.join(f'<div><span style="width:16px; flex:none;">{m}</span><span>{t}</span></div>' for m, t in items) + '</div>'
def verbs(vs): return '<div class="verbs">' + ''.join(f'<span class="tl"{"" if i == 0 else " style=\"color:#6E6862;\""}>{v} &rarr;</span>' for i, v in enumerate(vs)) + '</div>'
def two(a, b): return '<div class="two"><div><span class="kk">' + a[0] + '</span><span>' + a[1] + '</span></div><div><span class="kk">' + b[0] + '</span><span>' + b[1] + '</span></div></div>'
def phone(c, p, bd, sr, vb, tw):
    return PRE + c + p + bd + sr + vb + '<div style="height:4px;"></div>' + tw + POST
SRC_LIST = [('1', 'A SORRENTO DINING GUIDE [FIXTURE SOURCE]'), ('2', 'A FOOD WRITER&rsquo;S COLUMN, 2026 [FIXTURE SOURCE]'), ('3', 'LISTING &middot; CHECKED 4:02 PM'), ('D', 'DANA &middot; LEFT HERE FOR YOU &middot; AUG 6'), ('F', 'YOU &middot; KEPT &middot; AUG 19')]
P_GARDEN = 'A garden restaurant on the Sorrento cliff, set among lemon trees a few streets back from the piazza. People go for the courses rather than the view, which comes free with the table.<span class="c">1</span><span class="c">2</span>'
P_KITCHEN = 'The kitchen runs a set sequence in the evening. The provolone course is the one the regulars talk about; the fish is whatever came in that morning, priced accordingly.<span class="c">2</span>'
P_WEEKEND = 'Worth reserving on weekends. On a weeknight you can usually walk in before eight.<span class="c">1</span>'
P_DANA = 'Dana was here in August and left a line for you: <em>&ldquo;the table at the edge, order whatever they caught, nothing else.&rdquo;</em><span class="f">D</span> You kept it a week later for the lemons.<span class="f y">F</span>'
P_EDGE = 'Book the edge table, go on a weeknight, and let them run the courses. The edge has the same view as the seats inside and the better light.<span class="c">1</span>'
def discover():
    """Opened to look at it. Two facts, the identity, and one earned connection: why the courses run the way they do. No reservation pressure, no weeknight advice, no route."""
    return phone(ctx('FROM THE MAP &middot; SORRENTO &middot; OPENED TO LOOK'),
                 pair([('OPEN UNTIL', '11 tonight', 'LISTING &middot; 4:02 PM'), ('THE ROOM', 'A garden, three terraces', 'THE LOWEST ONE IS THE CLIFF EDGE')]),
                 body([P_GARDEN, P_KITCHEN,
                       'The set sequence is a lemon-terrace habit, not a chef&rsquo;s conceit: the kitchen is small because the terraces were dug for trees, so one sequence a night is what the room can cook. It is why the fish changes and the courses do not.<span class="c">2</span>']),
                 srcs(SRC_LIST[:2] + [SRC_LIST[2]]),
                 verbs(['Ask Vesper', 'Leave for someone']),
                 two(('PRICE', '&euro;&euro;&euro; &middot; about &euro;55 a head'), ('TABLE', 'Reserve &rarr; &middot; weekends fill')))
def assess():
    """Opened to judge Saturday's dinner for four. The facts that decide Saturday lead; the weeknight walk-in advice is not shown, because Saturday is not a weeknight."""
    return phone(ctx('FOR SATURDAY &middot; MAYA&rsquo;S DINNER &middot; 4 OF YOU &middot; AN OPTION, NOT CHOSEN'),
                 pair([('SATURDAY', 'Reserve; weekends fill', 'LISTING &middot; 4:02 PM'), ('FOR FOUR', 'The edge table seats four', 'DANA &middot; AUG 6')]),
                 body(['Saturday is the night this room fills, so a table is the whole question; the kitchen runs one sequence and the fish is whatever came in that morning.<span class="c">2</span><span class="c">3</span>',
                       P_DANA,
                       'Nothing is held here. Reserving happens on the restaurant&rsquo;s own page, and if you forward the confirmation it goes to Saturday.<span class="c">3</span>']),
                 srcs([SRC_LIST[1], SRC_LIST[2], SRC_LIST[3]]),
                 verbs(['Saturday', 'Ask Vesper', 'Leave for someone']),
                 two(('PRICE', '&euro;&euro;&euro; &middot; about &euro;55 a head'), ('TABLE', '<span class="link">Reserve &rarr;</span> &middot; weekends fill')))
def arrangement():
    """Opened from the reservation that exists. The page reads the arrangement back, says when to leave, and sells nothing."""
    return phone(ctx('RESERVED &middot; SATURDAY 8:00 &middot; FROM YOUR CONFIRMATION &middot; ON MAYA&rsquo;S DINNER'),
                 pair([('SATURDAY 8:00', 'Table for four', 'YOUR CONFIRMATION &middot; AUG 21'), ('FROM THE HOTEL', '9 min walk', 'THE PIAZZA, THEN VIA ROTA')]),
                 body(['The courses run about two hours, so a table at eight is the last full sequence of the night.<span class="c">2</span>',
                       'Ask for the edge table when you arrive; Dana&rsquo;s line was <em>&ldquo;the table at the edge, order whatever they caught, nothing else.&rdquo;</em><span class="f">D</span>',
                       'The walk is level to the piazza and then two streets back; nothing here changes the booking, which is the restaurant&rsquo;s.<span class="c">3</span>']),
                 srcs([SRC_LIST[1], SRC_LIST[2], SRC_LIST[3]]),
                 verbs(['Saturday', 'Ask Vesper', 'Directions']),
                 two(('PRICE', '&euro;&euro;&euro; &middot; about &euro;55 a head'), ('TABLE', 'Reserved &middot; from your email &middot; <span class="link">see it &rarr;</span>')))
def original():
    """A friend's contribution, opened from where it arrived: her words first, whole, with the place one line below. No page essay in front of it."""
    inner = ('<div class="ph" style="gap:12px;">'
             '<div style="display:flex; align-items:center; gap:8px;"><span class="a">D</span><div style="flex:1;"><div style="font-weight:600; font-size:14px;">Dana</div><div class="fn" style="color:#6E6862;">LEFT HERE FOR YOU &middot; AUG 6</div></div><span class="kk">SORRENTO</span></div>'
             '<div class="serif" style="font-size:19px; line-height:26px; font-style:italic;">&ldquo;The table at the edge, order whatever they caught, nothing else. Go before the light goes; the lemons are the whole point of the place.&rdquo;</div>'
             '<div class="row hi" style="display:flex; align-items:center; gap:10px;"><div style="flex:1;"><div style="font-weight:600;">Hortus</div><div style="color:#6E6862; font-size:11.5px;">Garden restaurant &middot; Sorrento &middot; open until 11 tonight</div></div><span class="t" style="color:#8F877C;">&rarr;</span></div>'
             '<div class="verbs"><span class="tl">Reply to Dana &rarr;</span><span class="tl" style="color:#6E6862;">Keep it &rarr;</span></div>'
             '<div class="kk" style="text-align:center; padding-top:6px;">&middot; STOP &middot;</div></div>')
    return inner
def col(ph, kick, ttl, sub, w=393):
    return (f'<div style="width:{w}px; flex:none; display:flex; flex-direction:column; gap:8px;">'
            f'<span class="kickm">{kick}</span>'
            f'<div class="serif" style="font-size:17px; line-height:22px; font-weight:600; color:#1B1714;">{ttl}</div>'
            f'<div style="font-size:12.5px; line-height:18px; color:#6E6862;">{sub}</div>{ph}</div>')
def tbl(headers, rows, w=1180):
    th = ''.join(f'<th style="text-align:left; font-family:JetBrains Mono, monospace; font-size:10px; letter-spacing:1.1px; font-weight:700; color:#8F877C; padding:0 10px 8px 0; border-bottom:1px solid rgba(27,23,20,0.14);">{h}</th>' for h in headers)
    tr = ''.join('<tr>' + ''.join(f'<td style="font-size:12.5px; line-height:17px; color:#2C2622; padding:8px 10px 8px 0; border-bottom:1px solid rgba(27,23,20,0.06); vertical-align:top;">{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table style="width:{w}px; border-collapse:collapse; margin-top:4px;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
def note(t, h): return f'<div style="display:flex; flex-direction:column; gap:6px;"><span class="kick">{t}</span><div style="font-size:13px; line-height:19px; color:#2C2622; max-width:1180px;">{h}</div></div>'
def rowdiv(kick, ttl, sub, first=False):
    top = '' if first else 'margin-top:44px; padding-top:26px; border-top:1px solid rgba(27,23,20,0.12);'
    return (f'<div style="{top} display:flex; flex-direction:column; gap:6px;"><span class="kick">{kick}</span>'
            f'<div class="serif" style="font-size:24px; line-height:30px; font-weight:600;">{ttl}</div>'
            f'<div style="font-size:13.5px; line-height:20px; color:#6E6862; max-width:1100px;">{sub}</div></div>')
def board():
    import gen08
    r1 = ('<div style="display:flex; gap:36px; align-items:flex-start; margin-top:24px;">'
          + col(discover(), 'R1 &middot; OPENED TO LOOK', 'Discovery', 'Two facts and one earned connection: why the kitchen runs one sequence. No reservation pressure, no weeknight advice, no route, because nothing is being judged yet')
          + col(assess(), 'R2 &middot; OPENED FOR SATURDAY', 'A visit being assessed', 'Saturday is the question, so the table is the first fact and the weeknight walk-in line is not shown. Dana&rsquo;s words stay where they are; the boundary on booking is stated once')
          + col(arrangement(), 'R3 &middot; OPENED FROM THE RESERVATION', 'An arrangement in use', 'The confirmation read back, when to leave, what to ask for at the door. Nothing sells the place again and nothing here changes the booking')
          + col(original(), 'R4 &middot; A FRIEND&rsquo;S CONTRIBUTION', 'Her original, opened directly', 'Arriving from Dana&rsquo;s note opens Dana&rsquo;s note: her words whole, nothing summarised, nothing marked read, and the place one line below. No page essay in front of the thing that was sent')
          + '</div>')
    r2 = ('<div style="display:flex; gap:36px; align-items:flex-start; margin-top:24px;">'
          + col(gen08.extension('unvisited'), 'R5 &middot; PLACES 08.13, AS DRAWN', 'Understanding without a visit', 'Supplied in the Places kit, not this shell: the point is the content test, not the chrome. A mechanism that survives the destination &mdash; gates against a raised sill &mdash; rather than a summary or a read-up teaser')
          + f'<div style="width:1180px; display:flex; flex-direction:column; gap:22px;">'
          + note('WHAT THIS BOARD IS', 'The four readings Places was asked to supply to this lab&rsquo;s September 9 comparison, drawn in this lab&rsquo;s own shell, sliced from board 09 so that the only difference is the body. Nothing here is adopted; it is what Places selects, offered for the shared destination decision. The fixture is this lab&rsquo;s: Hortus, Dana, Maya&rsquo;s dinner.')
          + note('THE SHELL IS PRESERVED', 'Photograph plate with the same two controls, kind and town, name, faces, one context line, the source list, the map with the seeded identity and the address, the stop. Every frame above carries them unchanged. The proposal is about the body only.')
          + note('WHAT CHANGES, FRAME BY FRAME', tbl(['READING', 'WHAT LEADS', 'WHAT IS NOT SHOWN', 'WHY'], [
              ['R1 &middot; discovery', 'What the place is, and one connection that explains it', 'The reservation push; the weeknight advice; distance from you', 'Nothing is being decided, so advice for a decision would be noise'],
              ['R2 &middot; a visit assessed', 'The table on a Saturday; who it is for; the booking boundary', '&ldquo;On a weeknight you can walk in before eight&rdquo;', 'The person is asking about Saturday; weeknight advice answers a question they did not ask'],
              ['R3 &middot; an arrangement', 'The confirmation, the two hours, what to ask at the door', 'Reserve as a verb; the case for the place', 'The decision is made; selling it again is the failure this frame fixes'],
              ['R4 &middot; a friend&rsquo;s original', 'Her words, whole', 'Four sourced paragraphs before them', 'The reason for opening was her line, so it is what opens'],
              ['R5 &middot; unvisited', 'The mechanism itself', 'Hours, route, an invitation to go', 'What must survive is the contrast, not a teaser for a page']]))
          + note('THE ONE AMENDMENT PROPOSED', 'Withdraw the invariant-body rule; keep the invariant shell. A body that cannot change loses the reason the page was opened, which is what 09C shows when Saturday&rsquo;s dinner is answered with weeknight advice, and what 09B shows when four paragraphs precede the line the person came for. Emphasis, order and selection among already-sourced material change; identity, ownership, sources and the return do not, and nothing is generated on open.')
          + note('NOT PROPOSED', 'No universal renderer, no automatic copying between projects, no new object owner, no stored personalised take, no generation on opening, and no change to social placement. Places&rsquo; own comparison and its selected column live on Places 08; this board is the receiving half.')
          + note('STATUS', 'Static frames, drawn September 9 by the Places lane and pushed here for the lab to accept, amend or refuse. No door was exercised. Every fact, person and address is a fixture, and the photograph plates are slots.')
          + '</div></div>')
    inner = ('<div style="display:flex; flex-direction:column;">'
             + rowdiv('14 &middot; RECEIVED FROM PLACES &middot; 09-09', 'What Places supplies to the shared destination decision', 'Four readings of one place in this lab&rsquo;s shell, plus the unvisited-understanding test, offered for the September 9 comparison of discovery, a visit being assessed and an existing arrangement. The shell is unchanged in every frame; the body follows the reason the page was opened.', first=True)
             + r1 + rowdiv('THE CONTENT TEST, AND THE TERMS', 'Understanding without a visit, and what is proposed', 'The last frame is Places 08.13 exactly as drawn there. Then the terms: what is preserved, what changes, the single amendment proposed and what is not.') + r2 + '</div>')
    return HEAD + BOARD_OPEN + inner + '</div>' + TAIL
if __name__ == '__main__':
    import os; os.makedirs('out2', exist_ok=True); h = board(); open('out2/14 - Received from Places.dc.html', 'w').write(h); print('wrote 14', len(h))
