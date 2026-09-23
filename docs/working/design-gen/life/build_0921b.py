#!/usr/bin/env python3
"""04c · One photo path — a tappable prototype for the September 21 export review.

Usage: build_0921b.py SRC_DIR OUT_DIR

Connects Life's collection → original/browse → general selection → Social's recipient preview →
Not now (same selection) or a simulated send (sent / didn't send / not sure / 1 of 2) → the same
origin; and Home's direct opening of the same viewer and return. No real messages, no writes.

Reuses 04b's helpers (build_0921.py) and the owners' words: Social 10.2 (preview, set outcomes) and
Social 09.3 (whole-send failure and uncertainty). Taps are bound by explicit data-go targets; the
component buttons inside Notice are bound by their rendered labels (shadow roots are walked).
"""
import json
import os
import runpy
import sys
import tempfile

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
_argv = sys.argv
sys.argv = [os.path.join(HERE, 'build_0921.py'), SRC, tempfile.mkdtemp()]
G = runpy.run_path(os.path.join(HERE, 'build_0921.py'))
sys.argv = _argv

phone, gut, sect, door, row, dci, prov = G['phone'], G['gut'], G['sect'], G['door'], G['row'], G['dci'], G['prov']
photo, badge, justified, grid, strip, attribution, topbar = (G['photo'], G['badge'], G['justified'], G['grid'], G['strip'],
                                                             G['attribution'], G['topbar'])
RECORD, ALL5, SELHEAD, BACKBTN, ORDER, ROWS, TABBAR = (G['RECORD'], G['ALL5'], G['SELHEAD'], G['BACKBTN'], G['ORDER'],
                                                        G['ROWS'], G['TABBAR'])
rep, HEAD, TAIL = G['rep'], G['HEAD'], G['TAIL']


def go(markup, target, first=None):
    """Bind the first element of `markup` (or the first occurrence of `first` in it) to a frame."""
    anchor = first or '<'
    i = markup.find(anchor)
    assert i >= 0, (target, anchor[:40])
    j = markup.find(' ', i)
    return markup[:j] + f' data-go="{target}"' + markup[j:]


def dgo(text, target):
    return f'<div style="display:flex; align-items:center;"><span class="vdl-door vk-t-bodySmMedium" data-go="{target}">{text}</span></div>'


def tile_go(markup, pid, target):
    a = f'role="img" aria-label="{pid}"'
    assert markup.count(a) >= 1, pid
    return markup.replace(a, a + f' data-go="{target}"', 1)


def back(markup, target):
    return markup.replace(BACKBTN, go(BACKBTN, target), 1)


def home_tabbar(tab):
    """The same tab bar with Home active: owner identity never selects the tab (the Home-stack rule)."""
    t = rep(tab, '<span style="font-size:10px; font-weight:600;">Life</span>',
            '<span style="font-size:10px; font-weight:500; color:var(--mute);">Life</span>')
    t = rep(t, '<span style="font-size:10px; font-weight:500; color:var(--mute);">Home</span>',
            '<span style="font-size:10px; font-weight:600;">Home</span>')
    li = t.find('font-weight:500; color:var(--mute);">Life<'); ls = t.rfind('<svg', 0, li)
    t = t[:ls] + t[ls:li].replace('#1B1714', '#6E6862') + t[li:]
    hi = t.find('font-weight:600;">Home<'); hs = t.rfind('<svg', 0, hi)
    return t[:hs] + t[hs:hi].replace('#6E6862', '#1B1714') + t[hi:]


HOME_TAB = home_tabbar(TABBAR)


def home_phone(inner, minh=None):
    return phone(inner, minh).replace(TABBAR, HOME_TAB, 1)


# ── Life path ─────────────────────────────────────────────────────────────────────
a1 = phone(RECORD + sect('PHOTOGRAPHS', '5', top=26) + gut(justified(ORDER), top=14) + gut(dgo('See all 5', 'a2'), top=14)
           + sect('THE EVENING') + gut(door('In order, with the pictures'), top=12), 760)
a2 = back(ALL5, 'a1').replace('color:var(--gold-deep);">SELECT</span>', 'color:var(--gold-deep);" data-go="a5">SELECT</span>', 1)
a2 = phone(tile_go(tile_go(a2 + grid(ROWS), 'PH-01', 'a3'), 'PH-04', 'a4'), 700)
a3 = phone(back(G['viewer']('PH-01', '4 OF 5', attribution('Maya', 'M', 'SAT 8:25 PM'), ['Reply to Maya'],
                            extra=tile_go(strip('PH-01'), 'PH-04', 'a4'))
                + sect('IN', top=26) + row('Pasta night', 'Sat Sep 19 &middot; at Nora&rsquo;s', 'SEP 19'), 'a2'), 900)
a4 = phone(back(G['viewer']('PH-04', '5 OF 5', gut(prov('YOUR CAMERA &middot; SAT 10:40 PM'), top=16), ['Share'],
                            extra=tile_go(strip('PH-04'), 'PH-01', 'a3')), 'a2'), 900)

CHOSEN = ('PH-01', 'PH-02', 'PH-04')          # the ledger's mixed selection: Maya's table and two of Nora's
OWN = ['PH-02', 'PH-03', 'PH-04']              # Nora's own, in time order: the only share-eligible pictures here
ASPECT, CHECK = G['ASPECT'], G['CHECK']


def sel_grid(rows):
    """The same grid as 04b, every tile toggleable: its check and ring follow the live selection (class pp-on)."""
    out = []
    for r in rows:
        h = (349 - 6 * (len(r) - 1)) / sum(ASPECT[q] for q in r)
        out.append('<div style="display:flex; gap:6px;">' + ''.join(
            f'<div class="pp-tile" data-pid="{q}" style="position:relative; width:{h * ASPECT[q]:.1f}px; height:{h:.1f}px; border-radius:4px; '
            f'overflow:hidden; flex:none;">{photo(q, w=h * ASPECT[q])}{badge(q)}<span class="pp-chk">{CHECK}</span></div>' for q in r) + '</div>')
    return gut('<div style="display:flex; flex-direction:column; gap:6px;">' + ''.join(out) + '</div>', top=14)


def notice(cls, title, body, button=None, target=None):
    """Notice.dc.html's own markup and classes, written out so its words can follow the count and its button binds directly."""
    btn = (f'<div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap"><span class="vdl-btn primary vk-t-labelSemibold" '
           f'style="color:var(--vk-color-white);min-height:36px;padding:0 14px" data-go="{target}">{button}</span></div>') if button else ''
    return gut(f'<div class="vdl-notice {cls}"><span class="vdl-dot"></span><div style="flex:1;min-width:0">'
               f'<div class="vk-t-bodySmMedium" style="color:inherit">{title}</div>'
               f'<div class="vk-t-bodySm" style="color:var(--vk-ink40);margin-top:2px">{body}</div>{btn}</div></div>', top=14)


SEL = ('<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;"><span class="kicker" style="color:var(--ink);">'
       '<span data-bind="nsel">3</span> SELECTED</span>'
       '<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto;" data-go="a2">Done</span></div>'
       '<div style="padding: 10px 22px 0 22px;"><span class="kicker" style="color:var(--mute);">PASTA NIGHT &middot; PHOTOGRAPHS</span></div>')
ACTS = gut('<div style="display:flex; gap:8px; border-top:1px solid var(--hairline); padding-top:14px;">'
           '<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1; padding:0 8px;" data-go="a6" data-need="own">Share <span data-bind="nown">2</span></span>'
           '<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1; padding:0 8px;" data-need="own">Export <span data-bind="nown">2</span></span>'
           '<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1; padding:0 8px;" data-need="own">Delete <span data-bind="nown">2</span></span></div>', top=20) \
    + gut('<div class="rsub" data-if="PH-01">Maya&rsquo;s photo stays with the dinner.</div>'
          '<div class="rsub" data-if="PH-05">Dana&rsquo;s photo stays with the dinner.</div>', top=10)
a5 = phone(SEL + sel_grid(ROWS) + ACTS, 700)

# Social 10P's preview (its words), on the shared constructions: the exact outgoing originals follow the selection, the line is a real field
PREVIEW = ('<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;">' + go(BACKBTN, 'a5')
           + '<span class="kicker" style="margin-left:auto; color:var(--mute);">SHARE &middot; <span data-bind="sharetitle">2 OF YOUR 3</span></span></div>'
           + gut('<div style="display:flex; gap:6px; flex-wrap:wrap;">' + ''.join(
               f'<div data-prev="{q}" style="flex:none; border-radius:4px; overflow:hidden;">{photo(q, h=128)}</div>' for q in OWN) + '</div>', top=16)
           + gut('<span class="meta" data-bind="orderline">IN THIS ORDER &middot; BOTH YOURS</span>', top=10)
           + gut('<div class="rsub" data-if="PH-01">Maya&rsquo;s table isn&rsquo;t in this share. It stays with the dinner.</div>'
                 '<div class="rsub" data-if="PH-05">Dana&rsquo;s dish isn&rsquo;t in this share. It stays with the dinner.</div>', top=8)
           + gut('<div class="vdl-field pill"><input data-draft type="text" placeholder="Add a line" class="vk-t-bodyMd" '
                 'style="border:0; outline:0; background:transparent; width:100%; color:var(--ink); padding:0;"></div>', top=16)
           + gut('<div style="display:flex; align-items:center; gap:8px;"><span class="vdl-t-metaLine" style="color:var(--mute);">TO</span>'
                 '<span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">M</span><span class="vk-t-bodySmMedium">Maya</span></span>'
                 '<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto;">Change</span></div>', top=14)
           + gut('<div class="rsub">Maya sees <span data-bind="these">these two photos</span> and that they&rsquo;re from Saturday at yours, '
                 'until you take them back.</div>', top=14)
           + gut('<div style="display:flex; align-items:center; gap:14px;"><span class="vdl-btn primary pill vk-t-labelSemibold" '
                 'style="color:var(--vk-color-white)" data-go="@send"><span>Send</span></span>'
                 '<span class="vdl-door vk-t-bodySmMedium" data-go="a5">Not now</span></div>', top=18))
a6 = phone(PREVIEW, 760)

# outcomes, in Social 10P's words and mapping; only a confirmed delivery leaves the selection
_e = G['div_end'](PREVIEW, 0)                 # the end of the top bar, by depth (its first </div> is the back button's)
_top, _rest = PREVIEW[:_e], PREVIEW[_e:]
o_failed = phone(_top + notice('oxblood', 'Didn’t send. You’re offline.', '<span data-bind="stillhere">Both photos and Maya are still here.</span>',
                               'Try again', 'o_sent') + _rest, 860)
LIFE_TOP = back(ALL5, 'a1').replace('color:var(--gold-deep);">SELECT</span>', 'color:var(--gold-deep);" data-go="a5">SELECT</span>', 1)
o_sent = phone(LIFE_TOP + notice('sage', 'Sent to Maya · <span data-bind="sentn">2 photos</span>', 'Your selection is cleared.') + grid(ROWS), 760)
PENDING = ('<div style="padding: 20px 22px 0 22px; display:flex; align-items:center;"><span class="kicker" style="color:var(--ink);">1 SELECTED</span>'
           '<span class="vdl-door vk-t-bodySmMedium" style="margin-left:auto;" data-go="@release">Done</span></div>'
           '<div style="padding: 10px 22px 0 22px;"><span class="kicker" style="color:var(--mute);">PASTA NIGHT &middot; PHOTOGRAPHS</span></div>')
o_partial = phone(PENDING + notice('oxblood', 'The pan went. The late table didn’t.', 'Maya has the pan.', 'Send the late table', 'o_retry')
                  + grid(ROWS, chosen=('PH-04',))
                  + gut('<div style="display:flex; gap:8px; border-top:1px solid var(--hairline); padding-top:14px;">'
                        '<span class="vdl-btn secondary vk-t-labelSemibold" style="flex:1;">Share 1</span></div>', top=20), 820)
o_unknown = phone(PENDING + notice('amber', 'Not sure the late table went', 'The pan reached Maya. Nothing is sent again until this is known.',
                                   'Check again', 'o_sent') + grid(ROWS, chosen=('PH-04',)), 760)
o_retry = phone(LIFE_TOP + notice('sage', 'Sent to Maya · the late table', 'She now has both. Nothing was sent twice.') + grid(ROWS), 760)

# ── Home path: Home 18 D's "Last night", then the same viewer, then back ─────────
b1 = home_phone('<div style="padding: 20px 22px 0 22px; display:flex; flex-direction:column; gap:8px;">'
                '<span class="kicker" style="color:var(--mute);">NEW YORK &middot; SUNDAY &middot; 11:20 AM</span>'
                '<span style="font-family:var(--serif); font-weight:600; font-size:22px; line-height:27px;">Rooms Remade closes at six today.</span></div>'
                + sect('LAST NIGHT', top=28)
                + gut('<div style="position:relative; border-radius:6px; overflow:hidden;">' + tile_go(photo('PH-01', w=349), 'PH-01', 'b2')
                      + badge('PH-01', 18) + '</div>', top=12)
                + attribution('Maya', 'M', 'SAT 8:25 PM') + gut(door('Reply to Maya'), top=10)
                + '<div style="height:14px;"></div>' + row('Pasta night &middot; at yours', 'SAT &middot; SAM, MAYA', '')
                + gut(door('All five pictures'), top=12), 900)
b2 = home_phone(back(G['viewer']('PH-01', 'PASTA NIGHT &middot; 4 OF 5', attribution('Maya', 'M', 'SAT 8:25 PM'), ['Reply to Maya'],
                                 extra=strip('PH-01')), 'b1'), 900)

FRAMES = [('a1', 'A1 · THE EVENING&rsquo;S RECORD', a1), ('a2', 'A2 · ALL FIVE', a2), ('a3', 'A3 · MAYA&rsquo;S, WHOLE', a3),
          ('a4', 'A4 · THE LATE TABLE, WHOLE', a4), ('a5', 'A5 · CHOOSING · TAP ANY PICTURE', a5),
          ('a6', 'A6 · SOCIAL&rsquo;S PREVIEW · THE EXACT OUTGOING', a6),
          ('o_sent', 'OUTCOME · SENT', o_sent), ('o_failed', 'OUTCOME · NOTHING WENT · STILL ON THE SHARE', o_failed),
          ('o_partial', 'OUTCOME · PART WENT · ONLY THE LATE TABLE PENDING', o_partial),
          ('o_retry', 'OUTCOME · THE LATE TABLE, SENT ON RETRY', o_retry),
          ('o_unknown', 'OUTCOME · NOT KNOWN YET · CHECK, NO RESEND', o_unknown),
          ('b1', 'B1 · HOME, LAST NIGHT', b1), ('b2', 'B2 · THE SAME VIEWER, FROM HOME', b2)]

frames = ''.join(f'<section class="frame" data-frame="{k}" style="display:none;"><div class="fl">{t}</div>{html}</section>' for k, t, html in FRAMES)
script = """
<script>
(function(){
  if (window.__PHOTOPATH) return; window.__PHOTOPATH = 1;
  var order = %s, CHOSEN = %s, OWN = %s, PAIR = ['PH-02', 'PH-04'];
  var st = { sel: CHOSEN.slice(), draft: '', sending: 2, outcome: 'o_sent', cur: null };
  window.PP = st;
  function frames(){ return Array.prototype.slice.call(document.querySelectorAll('.frame')); }
  function own(){ return OWN.filter(function(p){ return st.sel.indexOf(p) >= 0; }); }
  function pairOnly(){ var o = own(); return o.length === 2 && o[0] === PAIR[0] && o[1] === PAIR[1]; }
  var W = ['', 'one', 'two', 'three'];
  function text(k){
    var n = own().length, N = st.sel.length;
    return { nsel: String(N), nown: String(n),
      sharetitle: N > n ? n + ' OF YOUR ' + N : n + (n === 1 ? ' PHOTO' : ' PHOTOS'),
      orderline: n === 1 ? 'YOURS' : 'IN THIS ORDER \\u00b7 ' + (n === 2 ? 'BOTH YOURS' : 'ALL YOURS'),
      these: n === 1 ? 'this photo' : 'these ' + W[n] + ' photos',
      stillhere: n === 1 ? 'The photo and Maya are still here.' : n === 2 ? 'Both photos and Maya are still here.' : 'All three photos and Maya are still here.',
      sentn: st.sending === 1 ? '1 photo' : st.sending + ' photos' }[k];
  }
  function render(){
    var n = own().length;
    document.querySelectorAll('[data-bind]').forEach(function(e){ var v = text(e.getAttribute('data-bind')); if (v !== undefined && e.textContent !== v) e.textContent = v; });
    document.querySelectorAll('[data-if]').forEach(function(e){ var on = st.sel.indexOf(e.getAttribute('data-if')) >= 0; e.style.display = on ? '' : 'none'; });
    document.querySelectorAll('[data-prev]').forEach(function(e){ var on = own().indexOf(e.getAttribute('data-prev')) >= 0; e.style.display = on ? '' : 'none'; });
    document.querySelectorAll('.pp-tile').forEach(function(e){ e.classList.toggle('pp-on', st.sel.indexOf(e.getAttribute('data-pid')) >= 0); });
    document.querySelectorAll('[data-need="own"]').forEach(function(e){ e.style.opacity = n ? '' : '0.4'; e.style.pointerEvents = n ? '' : 'none'; });
    document.querySelectorAll('[data-draft]').forEach(function(e){ if (e.value !== st.draft) e.value = st.draft; });
    var ok = pairOnly();
    document.querySelectorAll('[data-outcome]').forEach(function(x){
      var o = x.getAttribute('data-outcome'), gated = (o === 'o_partial' || o === 'o_unknown') && !ok;
      x.style.opacity = gated ? '0.35' : ''; x.title = gated ? 'Drawn for the ledger pair: the pan and the late table' : '';
      x.style.fontWeight = o === st.outcome ? '700' : '400'; x.style.color = o === st.outcome ? '#1B1714' : '#8A6628';
    });
  }
  function show(k){
    if (k === '@send') { st.sending = own().length; k = st.outcome; if ((k === 'o_partial' || k === 'o_unknown') && !pairOnly()) k = 'o_sent'; }
    if (k === '@release') { st.sel = []; st.draft = ''; k = 'a2'; }
    if (k === 'o_unknown' || k === 'o_partial') st.sending = 2;
    st.cur = k;
    frames().forEach(function(s){ var on = s.getAttribute('data-frame') === k; s.classList.toggle('on', on); s.style.display = on ? 'block' : 'none'; });
    if (k === 'o_sent' || k === 'o_retry') { st.sel = []; st.draft = ''; }
    if (location.hash !== '#' + k) history.replaceState(null, '', '#' + k);
    var pos = document.getElementById('pos'); if (pos) pos.textContent = 'NOW \\u00b7 ' + k.toUpperCase().replace('_', ' ');
    render();
  }
  function bindOnce(e, ev, fn){ var key = '__pp_' + ev; if (e[key]) return; e[key] = 1; e.addEventListener(ev, fn); }
  function wire(){
    document.querySelectorAll('[data-go]').forEach(function(e){ e.style.cursor = 'pointer'; bindOnce(e, 'click', function(v){ v.stopPropagation(); v.preventDefault(); show(e.getAttribute('data-go')); }); });
    document.querySelectorAll('[data-start]').forEach(function(e){ e.style.cursor = 'pointer'; bindOnce(e, 'click', function(){ show(e.getAttribute('data-start')); }); });
    document.querySelectorAll('[data-outcome]').forEach(function(e){ e.style.cursor = 'pointer'; bindOnce(e, 'click', function(){
      var o = e.getAttribute('data-outcome'); if ((o === 'o_partial' || o === 'o_unknown') && !pairOnly()) return; st.outcome = o; render(); }); });
    document.querySelectorAll('.pp-tile').forEach(function(e){ e.style.cursor = 'pointer'; bindOnce(e, 'click', function(v){
      v.stopPropagation(); var p = e.getAttribute('data-pid'), i = st.sel.indexOf(p);
      if (i >= 0) st.sel.splice(i, 1); else st.sel.push(p); render(); }); });
    document.querySelectorAll('[data-draft]').forEach(function(e){ bindOnce(e, 'input', function(){ st.draft = e.value; render(); }); });
    // The host may re-mount the template after this runs: re-apply the visible frame and the state on every pass.
    var k = st.cur || (location.hash || '#a1').slice(1); if (order.indexOf(k) < 0) k = 'a1';
    var on = document.querySelector('.frame.on');
    if (!on || on.getAttribute('data-frame') !== k) show(k); else render();
  }
  var pending = null; function later(){ if (pending) return; pending = setTimeout(function(){ pending = null; wire(); }, 60); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire); else wire();
  window.addEventListener('load', wire);
  try { new MutationObserver(function(){ later(); }).observe(document.documentElement, { childList: true, subtree: true }); } catch (e) {}
  var beats = 0, hb = setInterval(function(){ wire(); if (++beats > 60) clearInterval(hb); }, 300);
})();
</script>""" % (json.dumps([k for k, _, _ in FRAMES]), json.dumps(list(CHOSEN)), json.dumps(OWN))

style = ('<style>.frame{width:393px;display:none}.frame.on{display:block!important}'
         '.pp-tile .pp-chk{display:none}.pp-tile.pp-on .pp-chk{display:block}.pp-tile.pp-on{outline:2px solid #1B1714;outline-offset:-2px}'
         '.fl{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;font-weight:700;letter-spacing:1.1px;color:#6E6862;margin-bottom:8px}'
         '[data-go]:hover{opacity:.85}.ctl{display:flex;flex-wrap:wrap;gap:16px;align-items:center;font-family:"JetBrains Mono",ui-monospace,monospace;'
         'font-size:10px;letter-spacing:1px;color:#8A6628;margin-bottom:18px}.ctl span{cursor:pointer}.ctl b{color:#1B1714;font-weight:700}'
         '.nt td{font-size:12px;line-height:16px;padding:6px 8px;border-top:1px solid rgba(27,23,20,.08);vertical-align:top}</style>')

TAP = [('A1', 'See all 5'), ('A2', 'Maya&rsquo;s picture or the late table; SELECT'), ('A3', 'The late table in the strip, or Back'),
       ('A5', 'Tap any picture to choose or unchoose; Share n; Done'),
       ('A6', 'Type a line if you like; Not now keeps your selection and words; Send gives the outcome picked above'),
       ('Nothing went', 'Try again, or Not now (back to your selection)'), ('Part went', 'Send the late table (only it), or Done'),
       ('Not known yet', 'Check again (nothing is resent), or Done'), ('B1', 'Maya&rsquo;s picture'), ('B2', 'Back: the same place in Home')]
notes = ('<div style="width:470px; flex:none; font-family:var(--sans); color:var(--ink);">'
         '<div class="fl" style="color:#8A6628">WHERE TO TAP</div><table class="nt" style="border-collapse:collapse; width:100%;">'
         + ''.join(f'<tr><td style="width:120px; font-weight:600;">{a}</td><td>{b}</td></tr>' for a, b in TAP) + '</table>'
         '<div class="fl" style="color:#8A6628; margin-top:22px;">WHAT THIS DEMONSTRATES</div>'
         '<div class="cn" style="font-size:12px; line-height:17px;">'
         '<p style="margin:0 0 8px;"><b>A live selection.</b> A5 starts with the ledger&rsquo;s three (Maya&rsquo;s table and two of Nora&rsquo;s); any picture '
         'can be chosen or unchosen, and the counts, the preview&rsquo;s pictures and its words follow. Maya&rsquo;s and Dana&rsquo;s pictures can be in a general '
         'selection; Share only ever carries Nora&rsquo;s own, and the preview says why the others aren&rsquo;t in it.</p>'
         '<p style="margin:0 0 8px;"><b>Cancel keeps what you did.</b> Not now returns to the same selection; the line you typed is still there when you come back, '
         'and after a failed send. Only a confirmed delivery clears the selection and the line.</p>'
         '<p style="margin:0 0 8px;"><b>Social 10P&rsquo;s outcomes, one model.</b> Nothing went: still on the share, Try again. Part went: only the late table '
         'stays selected, and its retry sends only it. Not known yet: Check again, and nothing is resent meanwhile. Part went and Not known yet are drawn for '
         'the ledger&rsquo;s pair (the pan and the late table) and are offered only when that pair is what&rsquo;s going.</p>'
         '<p style="margin:0 0 8px;"><b>One viewer, no detour.</b> Home&rsquo;s Last night opens the same viewer with Home&rsquo;s tab kept; Back lands on Home.</p></div>'
         '<div class="fl" style="color:#8A6628; margin-top:18px;">OWNERS AND LIMITS</div>'
         '<div class="cn" style="font-size:12px; line-height:17px;">A6 and the outcomes are Social&rsquo;s (10P), carried here on the same shared constructions. '
         'One difference is flagged back to Social: 10P&rsquo;s Not known yet frame still shows &ldquo;Share 1&rdquo;; this board offers only the check, since an '
         'uncertain delivery is not a failure to resend. B1 carries Home 18 D&rsquo;s Last night region only to start the path. &ldquo;Until you take them back&rdquo; '
         'is Social&rsquo;s proposed default. Pictures are drawn stand-ins (ledger §10). <b>Not demonstrated:</b> scroll position (these phones are drawn full '
         'height), native gestures, timing, accessibility, caching or delivery. Nothing is sent, exported or deleted.</div></div>')

head = ('<div class="cb" style="width:1100px;padding:38px"><div style="padding:0 0 14px 0;max-width:980px">'
        '<div style="display:flex;align-items:center;gap:12px"><span class="ceye">04c &middot; One photo path</span><span class="cpill rev">Review</span></div>'
        '<div class="ctitle" style="padding-top:8px">The pictures, one path, tappable.</div>'
        '<div class="cq" style="padding-top:6px">From the evening to a friend and back, and from Home to the same picture and back.</div></div>'
        '<div class="ctl"><span data-start="a1">&larr; LIFE PATH</span><span data-start="b1">HOME PATH &rarr;</span>'
        '<span style="color:#6E6862; cursor:default;">SEND GIVES:</span>'
        '<span data-outcome="o_sent">SENT</span><span data-outcome="o_failed">NOTHING WENT</span>'
        '<span data-outcome="o_partial">PART WENT</span><span data-outcome="o_unknown">NOT KNOWN YET</span><b id="pos"></b></div>'
        f'<div style="display:flex; gap:46px; align-items:flex-start;"><div style="width:393px; flex:none;">{frames}</div>{notes}</div></div>')
BOARD = HEAD.replace('</helmet>', style + '</helmet>') + head + script + TAIL
assert BOARD.count('<section class="frame"') == len(FRAMES)
open(os.path.join(OUT, '04c - One photo path.dc.html'), 'w', encoding='utf-8').write(BOARD)

# ── 00: 04c joins the walkthrough after 04b (idempotent) ──────────────────────────
b00 = open(os.path.join(SRC, '00 - Start here.dc.html'), encoding='utf-8').read()
if '<span class="ceye" style="min-width:60px">04c</span>' not in b00:
    import re
    m = re.search(r'<div style="display:flex;gap:14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var\(--hair-thin\);max-width:900px">'
                  r'<span class="ceye" style="min-width:60px">04b</span>.*?</div>', b00)
    assert m, '04b row missing from 00'
    new = (m.group(0).replace('>04b<', '>04c<', 1).replace('>Ordinary photographs<', '>One photo path<', 1)
           .replace('Can I look through an evening&rsquo;s pictures, find one again, and share the ones that are mine?',
                    'Tap through it: the evening to a friend and back, and Home to the same picture and back.', 1))
    assert '>04c<' in new and 'One photo path' in new and 'Tap through it' in new
    b00 = rep(b00, 'SEP 6 2026 · SEVENTEEN BOARDS', 'SEP 6 2026 · EIGHTEEN BOARDS')
    b00 = rep(b00, 'The default walkthrough &middot; eleven boards, one question each', 'The default walkthrough &middot; twelve boards, one question each')
    b00 = b00.replace(m.group(0), m.group(0) + new, 1)
open(os.path.join(OUT, '00 - Start here.dc.html'), 'w', encoding='utf-8').write(b00)
print('04c', len(BOARD), 'bytes ·', len(FRAMES), 'frames · 00 written ·', 'ok ->', OUT)
