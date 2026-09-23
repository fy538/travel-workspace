"""10P · Photo exchange, simulated (September 21 export reviews).
A stateful prototype of board 10's path, not a switch between prewritten frames. State lives in script and is
rendered into the phone on every change, so it survives the hosted runtime re-mounting the page:
  G  the general selection (Life's, mixed, any picture)          -- cancel always restores it
  P  the pending send (Social's: the share-eligible part of G, minus what is confirmed delivered)
  words, the optional line, typed into a real field               -- kept through Not now, failure and retry
Outcomes follow the reconciled rule offered to Life 04c: only a confirmed send completes; delivered items leave P;
retry sends only confirmed-undelivered items; an unknown result offers a status check, never an ordinary resend.
Clicks use one delegated listener on `data-act`. Notices are drawn with the shared Notice's own vdl-notice markup,
because the component's props are fixed at mount. Nothing is sent. Fixture; PROPOSED."""
import os, sys, json
from gen_c8 import *
from gen_c8 import record_head, maya_home, viewer
from gen_generous import head as _head

def act(a, html, extra=''):
    return f'<span data-act="{a}"{extra} style="cursor: pointer;">{html}</span>'

META = {p: {'author': v[0], 'w': v[1][0], 'h': v[1][1], 'dark': v[4], 'prov': v[3].replace('&middot;', '·'), 'what': v[2].replace('&rsquo;', '’')} for p, v in PH.items()}

# ───────────────────────────── skeleton frames; the script fills the parts marked with ids ─────────────────────────────
def ph_frame():
    S = 110
    cells = ''.join(f'<div data-act="tile" data-pid="{p}" style="position: relative; width: {S}px; height: {S}px; cursor: pointer;">{ph(p, S, S, 8)}'
                    + (by_badge(PH[p][0][0]) if PH[p][0] != 'Nora' else '') + '<span class="mk"></span></div>' for p in RECORD)
    inner = record_head('<span id="ph-head"></span>')
    inner += '<div id="ph-note" style="padding: 14px 22px 0 22px;"></div>'
    inner += gut(f'<div style="display: grid; grid-template-columns: repeat(3, {S}px); gap: 9px;">{cells}</div>', top=16)
    inner += '<div id="ph-line" style="padding: 12px 22px 0 22px;"></div><div id="ph-bar" style="padding: 18px 22px 0 22px;"></div>'
    return phone(inner, 0, active='Life')

def share_frame():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{act("notnow", BACK)}'
             f'<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;" id="s-head">SHARE</span></div></div>')
    inner += '<div id="s-note" style="padding: 14px 22px 0 22px;"></div>'
    inner += gut(f'<div id="s-tiles" style="display: flex; gap: 8px; align-items: flex-end;"></div><div class="fn" style="color: {ANCHOR}; margin-top: 8px;">IN THIS ORDER &middot; ALL YOURS</div><div id="s-ex"></div>', top=18)
    inner += gut('<div class="vdl-field" style="min-height: 44px; align-items: center;"><input id="s-words" type="text" placeholder="Add a line" autocomplete="off" '
                 'class="vk-t-bodyMd" style="border: 0; outline: 0; background: transparent; width: 100%; color: var(--vk-ink00); font: inherit; padding: 0;"></div>', top=18)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div>'
                 f'<div style="display: flex; align-items: center; gap: 10px;"><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">M</span><span class="vk-t-bodySmMedium">Maya</span></span>{door("Change", MUTE)}</div>'
                 f'<div id="s-scope" style="font-size: 13px; line-height: 19px; color: {INK2}; margin-top: 10px;"></div>', top=20)
    send_btn = '<span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">Send</span>'
    inner += gut(f'<div style="display: flex; align-items: center; gap: 16px;">{act("send", send_btn)}{act("notnow", door("Not now", MUTE))}</div>', top=24)
    return phone2(inner, active='Life')

def life_viewer():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{act("lback", BACK)}'
             f'<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">PASTA NIGHT</span><span class="fn" style="margin-left: auto;" id="lv-pos"></span></div></div>')
    inner += gut(f'<div id="lv-img" style="display: flex; justify-content: center;"></div><div class="fn" style="color: {ANCHOR}; margin-top: 8px;" id="lv-prov"></div>', top=16)
    return phone2(inner, active='Life')

def home_view(pid, pos, nxt):
    inner = viewer(pid, pos)
    inner = inner.replace(BACK, act('hback', BACK), 1).replace(f'<span class="fn" style="margin-left: auto;">{pos} OF 2</span>', act(nxt, f'<span class="fn">{pos} OF 2</span>', ' style="margin-left: auto; cursor: pointer;"'), 1)
    inner += gut(f'<div style="display: flex; align-items: center; min-height: 44px; border: 1px solid rgba(27,23,20,0.14); border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {GHOST}; flex: 1;">Reply to Nora</span></div>', top=16)
    return phone2(inner, active='Home')

def home_frame():
    h = maya_home()
    return h.replace(door('Open'), act('hopen', door('Open')), 1)

F = [('ph', 'LIFE &middot; NORA &middot; PASTA NIGHT &middot; PHOTOGRAPHS', ph_frame()),
     ('lv', 'LIFE &middot; THE ORIGINAL', life_viewer()),
     ('s1', 'SOCIAL &middot; THE SHARE PREVIEW', share_frame()),
     ('h1', 'HOME &middot; MAYA &middot; SUNDAY 10:05', home_frame()),
     ('v1', 'HOME &middot; THE VIEWER, 1 OF 2', home_view('PH-02', 1, 'hnext')),
     ('v2', 'HOME &middot; THE VIEWER, 2 OF 2', home_view('PH-04', 2, 'hprev'))]

SCRIPT = r"""
<script>
(function(){
  if (window.__P10_LOADED) return; window.__P10_LOADED = true;
  var META = __META__, RECORD = __RECORD__, DARK = __DARK__;
  var S = { frame: 'ph', mode: 'browse', G: [], P: [], words: '', sim: 'sent', phNote: null, sNote: null, viewing: 'PH-02', sent: {} };
  function own(p){ return META[p].author === 'Nora'; }
  function short(p){ return { 'PH-02': 'the pan', 'PH-04': 'the late table', 'PH-03': 'the second pan' }[p] || META[p].what; }
  function tile(p, H, lab){ var m = META[p], w = Math.round(H * m.w / m.h);
    var st = m.dark ? DARK : ''; var cl = m.dark ? '' : 'hatch'; var col = m.dark ? 'rgba(251,247,236,0.75)' : '#6E6862';
    return '<div class="' + cl + '" style="' + st + ' width:' + w + 'px;height:' + H + 'px;border-radius:8px;flex:none;position:relative;box-sizing:border-box;">' + (lab ? '<span class="fn" style="position:absolute;left:8px;bottom:6px;color:' + col + ';">' + lab + '</span>' : '') + '</div>'; }
  function notice(n){ if (!n) return ''; var cls = { failed: 'vdl-notice oxblood', unknown: 'vdl-notice amber', applied: 'vdl-notice sage' }[n.tone];
    var acts = '';
    if (n.primary || n.secondary) { acts = '<div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap">'
      + (n.primary ? '<span data-act="' + n.pa + '" class="vdl-btn primary vk-t-labelSemibold" style="color:var(--vk-color-white);min-height:36px;padding:0 14px;cursor:pointer">' + n.primary + '</span>' : '')
      + (n.secondary ? '<span data-act="' + n.sa + '" class="vdl-btn secondary vk-t-labelSemibold" style="min-height:36px;padding:0 14px;cursor:pointer">' + n.secondary + '</span>' : '') + '</div>'; }
    return '<div class="' + cls + '"><span class="vdl-dot"></span><div style="flex:1;min-width:0"><div class="vk-t-bodySmMedium" style="color:inherit">' + n.title + '</div>'
      + (n.body ? '<div class="vk-t-bodySm" style="color:var(--vk-ink40);margin-top:2px">' + n.body + '</div>' : '') + acts + '</div></div>'; }
  function put(id, html){ var el = document.getElementById(id); if (el && el.getAttribute('data-r') !== html) { el.innerHTML = html; el.setAttribute('data-r', html); } }
  function pendingOf(st){ return S.P.filter(function(x){ return x.st === st; }); }
  function render(){
    document.querySelectorAll('.frame').forEach(function(s){ var on = s.getAttribute('data-frame') === S.frame; if (s.classList.contains('on') !== on) s.classList.toggle('on', on); var d = on ? 'block' : 'none'; if (s.style.display !== d) s.style.display = d; });
    var pos = document.getElementById('pos'); if (pos && pos.textContent !== S.frame) pos.textContent = S.frame;
    // Photographs
    var sel = S.mode === 'select';
    put('ph-head', sel ? '<span data-act="done" style="cursor:pointer;font-size:15px;color:#6E6862;">Done</span>' : '<span data-act="select" style="cursor:pointer;font-size:15px;color:#6E6862;">Select</span>');
    put('ph-note', notice(S.phNote));
    document.querySelectorAll('[data-act="tile"]').forEach(function(t){ var p = t.getAttribute('data-pid'), mk = t.querySelector('.mk'); if (!mk) return;
      var h = '';
      if (sel) h = S.G.indexOf(p) >= 0 ? '<span style="position:absolute;top:6px;right:6px;width:22px;height:22px;border-radius:11px;background:#1B1714;color:#FBF7EC;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;">&#10003;</span>'
                                       : '<span style="position:absolute;top:6px;right:6px;width:20px;height:20px;border-radius:11px;border:1.5px solid rgba(27,23,20,0.45);background:rgba(251,247,236,0.6);"></span>';
      var x = S.P.filter(function(q){ return q.p === p && q.st !== 'delivered'; })[0];
      if (x) h += '<span class="fn" style="position:absolute;right:6px;bottom:6px;background:#FBF7EC;color:' + (x.st === 'unknown' ? '#8A6628' : '#7A2E2A') + ';padding:2px 5px;border-radius:4px;">' + (x.st === 'unknown' ? 'CHECKING' : 'NOT SENT') + '</span>';
      if (mk.getAttribute('data-r') !== h) { mk.innerHTML = h; mk.setAttribute('data-r', h); } });
    var ownSel = S.G.filter(own), others = S.G.filter(function(p){ return !own(p); });
    put('ph-line', sel && others.length ? '<div style="font-size:13px;line-height:19px;color:#4A443F;">' + others.map(function(p){ return META[p].author + '’s photo'; }).join(' and ') + (others.length > 1 ? ' stay' : ' stays') + ' with the dinner.</div>' : '');
    put('ph-bar', sel ? '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;border-top:1px solid rgba(27,23,20,0.12);padding-top:14px;"><span style="font-size:15px;font-weight:600;color:#1B1714;flex:1 0 auto;">' + S.G.length + ' selected</span>'
      + '<span style="font-size:15px;color:#6E6862;">Export ' + ownSel.length + '</span><span style="font-size:15px;color:#6E6862;">Delete ' + ownSel.length + '</span>'
      + '<span data-act="share" class="vdl-btn primary pill vk-t-labelSemibold" style="color:var(--vk-color-white);cursor:pointer;' + (ownSel.length ? '' : 'opacity:0.35;pointer-events:none;') + '">Share ' + ownSel.length + '</span></div>' : '');
    // Share preview
    var go = pendingOf('pending').concat(pendingOf('failed'));
    put('s-head', 'SHARE · ' + go.length + ' PHOTO' + (go.length === 1 ? '' : 'S'));
    put('s-note', notice(S.sNote));
    put('s-tiles', go.map(function(x){ return tile(x.p, 96, x.p); }).join(''));
    var ex = S.G.filter(function(p){ return !own(p); });
    put('s-ex', ex.length ? '<div style="font-size:13px;line-height:18px;color:#4A443F;margin-top:12px;">' + ex.map(function(p){ return META[p].author + '’s ' + (p === 'PH-01' ? 'table' : 'dish'); }).join(' and ') + ' isn’t in this share. It stays with the dinner.</div>' : '');
    put('s-scope', 'Maya sees ' + (go.length === 1 ? 'this photo' : 'these ' + go.length + ' photos') + (S.words ? ', your line' : '') + ' and that they’re from Saturday at yours, until you take them back.');
    var inp = document.getElementById('s-words'); if (inp && inp.value !== S.words && document.activeElement !== inp) inp.value = S.words;
    // Life viewer
    var v = S.viewing, m = META[v]; put('lv-pos', (RECORD.indexOf(v) + 1) + ' OF ' + RECORD.length);
    put('lv-img', m.h > m.w ? tile(v, 440, v + ' · NOT SUPPLIED') : tile(v, 262, v + ' · NOT SUPPLIED')); put('lv-prov', m.prov);
    // outside the phone: what the simulation has delivered, per picture
    var ks = Object.keys(S.sent); put('sent-log', ks.length ? ks.map(function(k){ return k + ' × ' + S.sent[k]; }).join(' · ') : 'nothing yet');
    put('state-log', 'G = [' + S.G.join(', ') + '] · P = [' + S.P.map(function(x){ return x.p + ':' + x.st; }).join(', ') + '] · words = “' + S.words + '”');
    document.querySelectorAll('[data-sim]').forEach(function(e){ var on = e.getAttribute('data-sim') === S.sim; var fw = on ? '700' : '400'; if (e.style.fontWeight !== fw) { e.style.fontWeight = fw; e.style.textDecoration = on ? 'underline' : 'none'; } });
  }
  function deliver(x){ x.st = 'delivered'; S.sent[x.p] = (S.sent[x.p] || 0) + 1; }
  function settle(){ // after a send attempt from the preview
    var go = pendingOf('pending').concat(pendingOf('failed'));
    if (S.sim === 'sent') { go.forEach(deliver); S.phNote = { tone: 'applied', title: 'Sent to Maya · ' + go.length + ' photo' + (go.length === 1 ? '' : 's'), body: 'In Life under Maya. Nothing waits on her reply.' }; S.P = []; S.G = []; S.words = ''; S.mode = 'browse'; S.sNote = null; S.frame = 'ph'; return; }
    if (S.sim === 'failed' || (S.sim === 'partial' && go.length < 2)) { go.forEach(function(x){ x.st = 'pending'; }); S.sNote = { tone: 'failed', title: 'Didn’t send. You’re offline.', body: 'Your photos, Maya and your line are still here.', primary: 'Try again', pa: 'send', secondary: 'Not now', sa: 'notnow' }; S.frame = 's1'; return; }
    go.slice(0, -1).forEach(deliver); var last = go[go.length - 1];
    S.G = []; S.mode = 'browse'; S.sNote = null; S.frame = 'ph';
    if (S.sim === 'partial') { last.st = 'failed'; S.phNote = partialNote(); }
    else { last.st = 'unknown'; S.phNote = { tone: 'unknown', title: 'Not sure ' + short(last.p) + ' went', body: (go.length > 1 ? cap(delivered()) + ' reached Maya. ' : '') + 'Nothing is sent again until this is known.', primary: 'Check again', pa: 'check', secondary: 'Leave it', sa: 'leave' }; }
  }
  function cap(s){ return s.charAt(0).toUpperCase() + s.slice(1); }
  function delivered(){ return S.P.filter(function(x){ return x.st === 'delivered'; }).map(function(x){ return short(x.p); }).join(' and ') || 'Nothing'; }
  function partialNote(){ var f = pendingOf('failed').map(function(x){ return short(x.p); }).join(' and ');
    return { tone: 'failed', title: cap(delivered()) + ' went. ' + cap(f) + ' didn’t.', body: 'Only ' + f + ' is waiting to send.', primary: 'Send ' + f, pa: 'retry', secondary: 'Leave it', sa: 'leave' }; }
  function retry(){ var f = pendingOf('failed'); if (!f.length) return;
    if (S.sim === 'sent' || S.sim === 'partial') { f.forEach(deliver); S.phNote = { tone: 'applied', title: 'Sent to Maya · ' + f.map(function(x){ return short(x.p); }).join(' and '), body: 'Nothing was sent twice.' }; S.P = []; }
    else if (S.sim === 'unknown') { f.forEach(function(x){ x.st = 'unknown'; }); S.phNote = { tone: 'unknown', title: 'Not sure ' + short(f[0].p) + ' went', body: 'Nothing is sent again until this is known.', primary: 'Check again', pa: 'check', secondary: 'Leave it', sa: 'leave' }; }
    else S.phNote = partialNote(); }
  function check(){ var u = pendingOf('unknown'); if (!u.length) return;
    if (S.sim === 'failed') { u.forEach(function(x){ x.st = 'failed'; }); S.phNote = partialNote(); }
    else { u.forEach(deliver); S.phNote = { tone: 'applied', title: cap(short(u[0].p)) + ' reached Maya', body: 'It was sent once.' }; S.P = []; } }
  var A = {
    select: function(){ S.mode = 'select'; S.phNote = null; },
    done: function(){ S.mode = 'browse'; S.G = []; },
    tile: function(el){ var p = el.getAttribute('data-pid'); if (S.mode === 'select') { var i = S.G.indexOf(p); if (i >= 0) S.G.splice(i, 1); else S.G.push(p); } else { S.viewing = p; S.frame = 'lv'; } },
    lback: function(){ S.frame = 'ph'; },
    share: function(){ var mine = RECORD.filter(function(p){ return S.G.indexOf(p) >= 0 && own(p); }); if (!mine.length) return; S.P = mine.map(function(p){ return { p: p, st: 'pending' }; }); S.sNote = null; S.frame = 's1'; },
    notnow: function(){ S.P = []; S.sNote = null; S.mode = 'select'; S.frame = 'ph'; },   // cancel: the mixed selection and the words come back
    send: function(){ settle(); },
    retry: retry, check: check,
    leave: function(){ S.P = []; S.phNote = null; },
    hopen: function(){ S.frame = 'v1'; }, hnext: function(){ S.frame = 'v2'; }, hprev: function(){ S.frame = 'v1'; }, hback: function(){ S.frame = 'h1'; },
  };
  document.addEventListener('click', function(e){
    var t = e.target.closest ? e.target.closest('[data-act],[data-sim],[data-start]') : null; if (!t) return;
    if (t.hasAttribute('data-sim')) S.sim = t.getAttribute('data-sim');
    else if (t.hasAttribute('data-start')) { S.frame = t.getAttribute('data-start'); }
    else { var f = A[t.getAttribute('data-act')]; if (f) f(t); }
    e.preventDefault(); render();
  }, true);
  document.addEventListener('input', function(e){ if (e.target && e.target.id === 's-words') { S.words = e.target.value; render(); } }, true);
  window.P10 = { S: S, render: render };
  var pending = null; function later(){ if (pending) return; pending = setTimeout(function(){ pending = null; render(); }, 60); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render); else render();
  window.addEventListener('load', render);
  try { new MutationObserver(function(ms){ for (var i = 0; i < ms.length; i++) { if (ms[i].type === 'childList' && ms[i].addedNodes.length) { later(); return; } } }).observe(document.documentElement, { childList: true, subtree: true }); } catch (e) {}
  var beats = 0; var hb = setInterval(function(){ render(); if (++beats > 100) clearInterval(hb); }, 300);
})();
</script>"""

def proto():
    frames = ''.join(f'<section class="frame" data-frame="{k}" style="display: none;"><div class="fl">{t}</div>{fr}</section>' for k, t, fr in F)
    style = ('<style>.frame { width: 393px; display: none; } .frame.on { display: block !important; } '
             '.fl { font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: #6E6862; margin-bottom: 8px; } '
             '.ctl { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 10px; letter-spacing: 1px; color: #8A6628; margin-bottom: 12px; } '
             '.ctl [data-sim], .ctl [data-start] { cursor: pointer; } .log { font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 10px; letter-spacing: 0.6px; color: #4A443F; line-height: 15px; }</style>')
    ctl = ('<div class="ctl"><span data-start="ph">&larr; LIFE: NORA&rsquo;S PHOTOGRAPHS</span><span data-start="h1">HOME: MAYA &rarr;</span><span style="color: #6E6862;">FRAME <b id="pos"></b></span></div>'
           '<div class="ctl"><span style="color: #6E6862;">NEXT SEND, RETRY OR CHECK GIVES:</span><span data-sim="sent">SENT</span><span data-sim="failed">NOTHING WENT</span><span data-sim="partial">PART WENT</span><span data-sim="unknown">NOT KNOWN YET</span></div>'
           '<div class="log" style="margin-bottom: 4px;">DELIVERED, SIMULATED, ALL SHARES THIS SESSION: <span id="sent-log"></span></div><div class="log" style="margin-bottom: 16px; color: #6E6862;">STATE: <span id="state-log"></span></div>')
    rule = tbl(['OUTCOME', 'GENERAL SELECTION (LIFE)', 'PENDING SEND (SOCIAL)', 'OFFERED', 'LANDS ON'], [
        ['Not now', 'Restored, exactly as chosen', 'Discarded; the line is kept as a draft', 'Share again', 'Photographs, selecting'],
        ['Nothing went', 'Kept underneath', 'Unchanged, with the line', 'Try again; Not now', 'The preview'],
        ['Part went', 'Released: the share used it', 'Only what didn&rsquo;t arrive', 'Send only that; Leave it', 'Photographs, with the notice and a NOT SENT mark'],
        ['Not known yet', 'Released', 'The unknown item, marked CHECKING', 'Check again (a status check, not a resend); Leave it', 'Photographs'],
        ['Sent', 'Cleared', 'Empty', 'Nothing; the share is findable in Life', 'Photographs, with a local confirmation'],
    ])
    notes = notecol('How to use it', [
        ('TRY THIS', N('On Photographs, tap Select, then tap PH-02, PH-01 and PH-04 (Maya&rsquo;s can be chosen; Share counts only Nora&rsquo;s). Share 2. Type a line in the field. Not now: the same three come back, and Share 2 shows your line again. Pick NOTHING WENT and Send; the line survives Try again. Pick PART WENT and Send; then pick NOT KNOWN YET and send the late table; then SENT and Check again. The delivered log never counts the pan twice. Tapping a picture while not selecting opens it; back returns to the same grid.')),
        ('THE RULE, OFFERED TO LIFE 04c', rule),
        ('WHAT THIS IS NOT', N('A simulation in the browser. Nothing is sent, stored or synchronized, and the outcomes are picked by hand. Scroll position, swipe, pinch, caching, real delivery and withdrawal propagation are not demonstrated. Photographs are stand-ins with their ledger IDs until approved pictures exist.')),
    ], w=560)
    meta = json.dumps(META, ensure_ascii=False)
    script = SCRIPT.replace('__META__', meta).replace('__RECORD__', json.dumps(RECORD)).replace('__DARK__', json.dumps(DARK))
    body = (f'<div style="width: 1080px; min-height: {hh("10P", 1500)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK};">'
            + _head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 10P &middot; PROTOTYPE &middot; {STAMP}', '10P &middot; Photo exchange, simulated',
                    'Board 10&rsquo;s path with its state kept: a selection you change by tapping, a line you type, a preview built from what you chose, and each simulated outcome returning to the same place with the right thing still waiting. Maya&rsquo;s Home opens the same pictures and returns.')
            + ctl + f'<div style="display: flex; gap: 46px; align-items: flex-start;"><div style="width: 393px; flex: none;">{frames}</div>{notes}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>')
    return HEAD_VDL.replace('</helmet>', style + '</helmet>') + body + script + TAIL

if __name__ == '__main__':
    h = proto(); open(os.path.join(OUT, '10P - Photo exchange, simulated.dc.html'), 'w').write(h); print('wrote 10P', len(h))
