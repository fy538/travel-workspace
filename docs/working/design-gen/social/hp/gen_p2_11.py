"""11 · Two complete paths as ordered frames (§11.4), and P1 · a tappable prototype of the same frames.
Path A: ordinary opening → From friends → a share → reply → return. Path B: possibility → contextual question → dinner update →
changed circumstances → the exact action → readback. Interaction on the prototype is a static state switch; nothing is tested."""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import col, N, facepile
from gen_generous3 import sect, title, sup, gut, card, fact, author_row
from gen_merge import tbl, daycap
from gen_p2_common import *
from gen_p2_02 import field
from gen_p2_04 import dense_phone, opened_phone, by, PLACE_NAMES
from gen_p2_03 import b_scroll
from gen_p2_06 import chat_phone, sent_phone, applied_phone, back_phone, change_phone

# ───────────────────────────── path A frames ─────────────────────────────
def a1(): return field('film', entry='populated')
def a2(): return dense_phone()
def a3(): return opened_phone()
def a4():
    inner = header('Maya', 'Thursday &middot; to friends', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{illo("room", 200)}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{by("Maya", "print_room")[2]}</div>', top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1.5px solid {INK}; border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {INK}; flex: 1;">Saturday afternoon, then? I want the side room.</span><span style="font-size: 13px; font-weight: 600; color: {GOLDD}; flex: none;">Send</span></div>', top=22)
    inner += gut(src('To Maya only'), top=0)
    return phone2(inner)
def a5():
    inner = header('Maya', 'Thursday &middot; to friends', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{illo("room", 200)}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{by("Maya", "print_room")[2]}</div>', top=16)
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">Saturday afternoon, then? I want the side room.</div></div>' + f'<div style="text-align: right; margin-top: 4px;"><span class="fn" style="color: {ANCHOR};">TO MAYA &middot; JUST NOW</span></div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.08); border-bottom: 1px solid rgba(27,23,20,0.08);">{thumb("room", 48)}<div style="flex: 1;">{title(PLACE_NAMES["print_room"], 16, 20, 600)}{when_line("Red Hook &middot; Tue&ndash;Sun 11&ndash;6")}</div>{CHEV}</div>', top=18)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 2px;">' + door('Back to friends') + '</div>', top=22)
    return phone2(inner)
def a6(): return field('film', entry='populated')

# ───────────────────────────── path B frames ─────────────────────────────
def b1(): return b_scroll()
def b2(): return chat_phone()
def b3(): return sent_phone()
def b4(): return applied_phone()
def b5(): return back_phone()
def b6(): return change_phone()
def b7():
    inner = header('NEW YORK', 'Saturday 5:52 PM') + question_line('Saturday evening', ctx='Around dinner')
    inner += gut(card(f'<div class="kick" style="color: {GOLDD};">DINNER &middot; MOVED 5:52 PM</div><div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 25px; margin-top: 6px;">Saturday 9:30 &middot; the long table at the caf&eacute; &middot; with Maya and Alex</div>'
                      + f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 10px;">{facepile(["you", "M", "A"], 24, -6)}<span style="font-size: 13px; color: {MUTE};">Maya and Alex have been told. Seating for three isn&rsquo;t confirmed.</span></div>'), top=18)
    inner += sect('Still on tonight') + gut('<div>' + place_unit('hall', 'The listening hour: Reich, <i>Music for 18 Musicians</i>', 'Saturday 7:15 &middot; doors 6:45', 'One continuous hour; then a walk to the caf&eacute;.', last=True) + '</div>')
    inner += gut(ending(['Back to Saturday evening']), top=26)
    return phone2(inner)

A = [('a1', 'The ordinary opening', a1), ('a2', 'From friends', a2), ('a3', 'Maya&rsquo;s share', a3), ('a4', 'Reply, typed', a4), ('a5', 'Sent, to Maya only', a5), ('a6', 'Back to the opening, same position', a6)]
B = [('b1', 'Saturday evening: the hour', b1), ('b2', 'The question, in Chat', b2), ('b3', 'Sent; dinner 8:15', b3), ('b4', 'Answered; dinner moved to 9:30', b4), ('b5', 'Back in Places; the line is current', b5), ('b6', 'Saturday 5:50: the kitchen change, the caf&eacute; selected', b6), ('b7', 'Moved to the caf&eacute;; readback', b7)]

def frames_row(frames, prefix):
    out = ''
    for i, (k, t, fn) in enumerate(frames):
        arrow = '' if i == 0 else f'<div style="width: 26px; flex: none; display: flex; align-items: center; justify-content: center; padding-top: 420px;"><svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 9H14M10 5L14 9L10 13" stroke="{GOLDD}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
        out += arrow + f'<div style="width: 393px; flex: none;"><div class="kickm" style="margin-bottom: 8px; text-transform: uppercase;">{prefix}{i+1} &middot; {t}</div>{fn()}</div>'
    return f'<div style="display: flex; align-items: flex-start; gap: 6px; overflow: visible;">{out}</div>'

def board():
    rowA = frames_row(A, 'A')
    rowB = frames_row(B, 'B')
    html = two_rows(3020, '11', f'{STAMP} &middot; 11 &middot; TWO COMPLETE PATHS &middot; ORDERED FRAMES &middot; 09-07 (&sect;11.4)', '11 &middot; Two complete paths, frame by frame',
                    'Path A: the ordinary opening, From friends, a share, a reply to the person, and the return to the same position. Path B: a possibility, a contextual question, the dinner moved by its organizer, the changed circumstances, the exact action and its readback. Each frame is a rendered static state; the taps between them are the doors and controls visible on the frame before. Interaction is untested; the tappable prototype P1 switches between these same frames.',
                    [f'<div style="flex: none;">{rowA}</div>'], 'PATH B', 'Possibility, question, update, change, exact action, readback', [f'<div style="flex: none;">{rowB}</div>'], default_h=5200)
    notes = tbl(['PATH', 'WHAT IS CURRENT AT THE END', 'NAVIGATION EFFORT', 'WHAT IS UNTESTED'], [
        ['A', 'The opening, at the position the person left; one reply sent to Maya only; Priya&rsquo;s separate visit still labelled as hers', 'Two taps in, one reply, two taps back; no query, no sheet', 'That the row with faces is noticed; that the reply field reads as to Maya alone; scroll restoration on a device'],
        ['B', 'One dinner: Saturday 9:30 at the caf&eacute;, Maya and Alex told, seating unconfirmed; the hour untouched', 'One question, one send, one tap to move the dinner, one tap to move it again after the change; no visit to an arrangements screen', 'The organizer command and shared readback in the arrangements owner; the exact-action door; every timing']])
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', '<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + blk_('WHAT THE TWO PATHS SHOW, AND WHAT THEY DO NOT', notes) + '</div><div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

def blk_(t, html):
    from gen_merge import blk
    return blk(t, html)

# ───────────────────────────── P1 · the tappable prototype ─────────────────────────────
BIND = {  # frame → [(door label prefix, target)]
    'a1': [('From friends', 'a2'), ('Saturday&rsquo;s film', 'b1')],
    'a2': [('Reply to Maya', 'a3'), ('Open', 'a3'), ('All of New York', 'a6'), ('From friends', 'a6')],
    'a3': [('Reply to Maya', 'a4'), ('Ask about the Print Room', 'a3')],
    'a4': [('Send', 'a5')],
    'a5': [('Back to friends', 'a2')],
    'a6': [('From friends', 'a2'), ('Saturday&rsquo;s film', 'b1')],
    'b1': [('This Saturday&rsquo;s hour', 'b2'), ('Saturday evening', 'a1')],
    'b2': [('Send to Maya and Alex', 'b3')],
    'b3': [('Back to Saturday evening', 'b5'), ('The hour, at Canal Hall', 'b4')],
    'b4': [('Move dinner to 9:30', 'b5'), ('Back to Saturday evening', 'b5')],
    'b5': [('This Saturday&rsquo;s hour', 'b6')],
    'b6': [('Move dinner to the caf&eacute;, and tell Maya and Alex', 'b7'), ('Eat at 8:15 instead and skip the hour', 'b1')],
    'b7': [('Back to Saturday evening', 'b5')],
}
def prototype():
    frames = ''.join(f'<section class="frame" data-frame="{k}" style="display: none;"><div class="fl">{t}</div>{fn()}</section>' for k, t, fn in A + B)
    script = """
<script>
(function(){
  var order = %s; var bind = %s;
  var cur = null;
  function show(k){ cur = k; document.querySelectorAll('.frame').forEach(function(s){ var on = s.getAttribute('data-frame') === k; s.classList.toggle('on', on); s.style.display = on ? 'block' : 'none'; s.hidden = !on; }); if (location.hash !== '#' + k) location.hash = k; var i = order.indexOf(k); var pos = document.getElementById('pos'); if (pos) pos.textContent = (i+1) + ' / ' + order.length + ' · ' + k.toUpperCase(); }
  function norm(s){ return (s||'').replace(/\\s+/g,' ').trim(); }
  function wire(){
    document.querySelectorAll('.frame').forEach(function(sec){
      if (sec.getAttribute('data-wired')) return; sec.setAttribute('data-wired', '1');
      var k = sec.getAttribute('data-frame'); var pairs = bind[k] || [];
      pairs.forEach(function(p){
        var label = norm(new DOMParser().parseFromString(p[0], 'text/html').body.textContent);
        var els = Array.prototype.slice.call(sec.querySelectorAll('div, span'));
        els.filter(function(e){ return e.children.length <= 2 && norm(e.textContent).indexOf(label) === 0 && norm(e.textContent).length <= label.length + 4; })
           .forEach(function(e){ e.style.cursor = 'pointer'; e.setAttribute('data-goto', p[1]); e.addEventListener('click', function(ev){ ev.stopPropagation(); show(p[1]); }); });
      });
    });
    var r = document.getElementById('restart'), b = document.getElementById('pathb');
    if (r && !r.getAttribute('data-wired')) { r.setAttribute('data-wired', '1'); r.addEventListener('click', function(){ show('a1'); }); }
    if (b && !b.getAttribute('data-wired')) { b.setAttribute('data-wired', '1'); b.addEventListener('click', function(){ show('b1'); }); }
    var start = cur || (location.hash || '#a1').slice(1); show(order.indexOf(start) >= 0 ? start : 'a1');
  }
  // The host runtime may re-mount the document after this script runs and drop attributes; re-wire on any DOM change and on a short heartbeat.
  var pending = null;
  function later(){ if (pending) return; pending = setTimeout(function(){ pending = null; wire(); }, 60); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire); else wire();
  window.addEventListener('load', wire);
  window.addEventListener('hashchange', function(){ var k = location.hash.slice(1); if (order.indexOf(k) >= 0 && k !== cur) show(k); });
  try { new MutationObserver(function(ms){ for (var i = 0; i < ms.length; i++) { if (ms[i].type === 'childList' && ms[i].addedNodes.length) { later(); return; } } }).observe(document.documentElement, { childList: true, subtree: true }); } catch (e) {}
  var beats = 0; var hb = setInterval(function(){ wire(); if (++beats > 40) clearInterval(hb); }, 300);
})();
</script>""" % (json.dumps([k for k, _, _ in A + B]), json.dumps(BIND))
    style = ('<style>.frame { width: 393px; display: none; } .frame.on { display: block !important; } .fl { font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: #6E6862; margin-bottom: 8px; } '
             '[data-goto]:hover { text-decoration: underline; } .ctl { display: flex; gap: 18px; align-items: center; font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 10px; letter-spacing: 1px; color: #8A6628; margin-bottom: 18px; } .ctl span { cursor: pointer; } .ctl b { color: #1B1714; font-weight: 700; }</style>')
    body = (f'<div style="width: 1000px; min-height: {hh("P1", 3400)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK};">'
            + head(f'{STAMP} &middot; P1 &middot; PROTOTYPE &middot; TWO PATHS, TAPPABLE &middot; 09-07 (&sect;11.4)', 'P1 &middot; Two paths, tappable', 'The same frames as 11, one phone at a time. Tap the doors and controls named on the frame to move; the browser hash carries the frame, so #b6 opens the kitchen change directly. This is a static state switch between rendered frames: it tests nothing about backend behaviour, native accessibility, gestures or timing.')
            + '<div class="ctl"><span id="restart">&larr; START OVER (PATH A)</span><span id="pathb">PATH B &rarr;</span><b id="pos"></b></div>'
            + f'<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="width: 393px; flex: none;">{frames}</div>'
            + f'<div style="width: 440px; flex: none;">' + notecol('Where to tap', [
                ('PATH A', tbl(['FRAME', 'TAP'], [['A1 the opening', 'From friends (the row with faces)'], ['A2 From friends', 'Reply to Maya, or Open, on her card'], ['A3 her share', 'Reply to Maya (the field)'], ['A4 typed', 'Send'], ['A5 sent', 'Back to friends'], ['A2 again', 'All of New York, or the chip&rsquo;s &times;']])),
                ('PATH B', tbl(['FRAME', 'TAP'], [['A1 or A6', 'Saturday&rsquo;s film (leads into Saturday evening)'], ['B1 the hour', 'This Saturday&rsquo;s hour'], ['B2 Chat', 'Send to Maya and Alex'], ['B3 sent', 'The hour, at Canal Hall (jumps to the answer)'], ['B4 answered', 'Move dinner to 9:30'], ['B5 back', 'This Saturday&rsquo;s hour (jumps to Saturday 5:50)'], ['B6 the change', 'Move dinner to the caf&eacute;, and tell Maya and Alex'], ['B7 readback', 'Back to Saturday evening']])),
                ('WHAT THIS IS NOT', N('Not a working app. The time jumps between frames (Friday to Saturday) are the fixture&rsquo;s, not a clock. Doors that are not listed do nothing. Nothing is sent, moved or booked.')),
            ], w=440) + '</div></div></div>')
    return HEAD.replace('</helmet>', FN11 + style + '</helmet>') + body + script + TAIL

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '11 - Two Paths.dc.html'), 'w').write(html); print('wrote 11', len(html))
    html = prototype(); open(os.path.join(OUT, 'P1 - Prototype - Two Paths.dc.html'), 'w').write(html); print('wrote P1', len(html))
