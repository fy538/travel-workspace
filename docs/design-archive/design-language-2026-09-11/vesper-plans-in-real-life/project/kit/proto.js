/* VESPER — PLANS IN REAL LIFE · kit/proto.js · 2026-09-04 · rev §0.5 2026-09-05
   Scripted prototype runtime for "10 Interactive". EXPLORATION · NOT PRODUCTION.
   - One SHARED plan state, plus one PRIVATE record per viewpoint (ask sheet, offer, preview, receipt, note,
     in-flight request, draft, screen). Switching the research viewer never shows another person's private
     exchange or offers recovery controls for their request; the shared accepted result shows for everyone (§0.5 D3).
   - Every control changes state or fails honestly (no predetermined success screens).
   - Language routes are RECOGNIZERS (regex + state guard). They route; they never parse or invent numbers.
   - Private reversible actions push a SCOPED undo entry (the keys that action changed, with their prior values).
     Undo repairs only that change — never another person's independent response (§0.5 D2). A send clears the
     stack: no Undo past a send; a correction is another change.
   - Re-entry (Home ↔ page) never touches state; Back never undoes an edit.
   All facts are synthetic fixtures. */
(function () {
  /* the runtime can evaluate helmet scripts more than once; one closure must own the state */
  if (window.__PIRL_LOADED) return; window.__PIRL_LOADED = true;
  var VIEWERS = ['you', 'maya', 'sam'];
  var SHARED = {
    viewer: 'you',
    walk: 'walk',            // walk | cafe
    bookstore: 'suggested',  // suggested | added
    bookstore_by: '',        // you | maya
    grant: 'no',             // no | yes | ended
    sam: 'unknown',          // unknown | dinner | no
    dinner: '7:00',          // 7:00 | 8:00
    sent8: 'no',             // no | yes
    sam8: '',                // '' | ok | cant
    reservation: '7:00',     // 7:00 | 8:00
    maya_asked: 'no',        // no | yes
    maya_sent: 'no',         // no | yes — Maya explicitly sent a suggestion to Nora
    rain: 'yes',
    sim: 'none'              // research chrome: none | slow | fail | unknown — failure injection for the NEXT change
  };
  var PRIVATE = {
    screen: 'page',          // page | home
    preview: '',             // '' | cafe | dinner8
    ask: 'closed',           // closed | open — the assistance field (§0.1–0.2 pill)
    offer: 'no',             // no | suggest | ask8 — an explicit-send offer after a contributor's edit-like ask (never auto-sent)
    receipt: '', receipt_kind: 'none', note: '',
    save: 'idle',            // idle | pending | failed | unknown — the state of this person's last change request
    save_label: '',          // generated label of the in-flight action (specification aid)
    req_text: '',            // the person's authored words for the in-flight / failed request (kept)
    req_id: '',              // execution identity of that request
    draft: ''                // unaccepted words kept as a recoverable draft (Not now / cancelled)
  };
  function fresh() {
    var s = Object.assign({}, SHARED); s.priv = {};
    VIEWERS.forEach(function (v) { s.priv[v] = Object.assign({}, PRIVATE); });
    return s;
  }
  var state = fresh();
  var undo = { you: [], maya: [], sam: [] };   // scoped entries per viewpoint
  var timers = { you: null, maya: null, sam: null };
  var log = [];
  var actor = null;   // set while a deferred callback runs on behalf of the person who made the request

  function who() { return actor || state.viewer; }
  function P(v) { return state.priv[v || who()]; }
  function val(k) { return (k in PRIVATE) ? P()[k] : state[k]; }
  function set(patch) { Object.keys(patch).forEach(function (k) { if (k in PRIVATE) P()[k] = patch[k]; else state[k] = patch[k]; }); }
  function receipt(text, kind) { var p = P(); p.receipt = text; p.receipt_kind = kind || 'gold'; p.note = ''; }
  function note(text) { P().note = text; }

  /* ---- scoped undo: an entry names the action and the prior values of exactly the keys it changed ---- */
  var UNDO_KEYS = { add_bookstore: ['bookstore', 'bookstore_by'], grant: ['grant'], end_grant: ['grant'], use_cafe: ['walk'], back_to_walk: ['walk'], forward: ['reservation'] };
  var UNDO_TEXT = {
    add_bookstore: function () { return 'Willow & Page is back to a suggestion'; },
    grant: function () { return 'Maya can no longer change the afternoon'; },
    end_grant: function () { return 'Maya can change the afternoon again'; },
    use_cafe: function () { return 'the walk is back'; },
    back_to_walk: function () { return 'the café is back'; },
    forward: function (prior) { return 'the reservation reads ' + prior.reservation + ' again'; }
  };
  function snapshot(id) {
    var prior = {}; (UNDO_KEYS[id] || []).forEach(function (k) { prior[k] = state[k]; });
    var stack = undo[who()]; stack.push({ id: id, prior: prior }); if (stack.length > 20) stack.shift();
  }

  /* ---- derived text (deterministic; the only place numbers/sentences are composed) ---- */
  function derived() {
    var d = {}; var p = P();
    var afternoon = state.bookstore === 'added' ? 'Bookstore at three, ' : 'An afternoon out, ';
    var walk = state.walk === 'cafe' ? 'the café if it rains' : 'the river after';
    d.thesis = afternoon + walk + ', dinner at ' + (state.dinner === '8:00' ? 'eight' : 'seven') + ' with Maya' + (state.sam === 'no' ? '' : ' and Sam') + '.';
    d.thesis_maya = 'You can ' + (state.grant === 'yes' ? 'shape the afternoon. ' : 'suggest for the afternoon. ') + 'Dinner is Nora’s to change.';
    d.thesis_sam = state.dinner === '8:00' && state.sam8 === '' ? 'Nora moved dinner from 7:00 to 8:00. Same place.' : 'You’re joining at dinner. ' + (state.dinner === '8:00' ? 'Eight' : 'Seven') + ' o’clock, Court Street.';
    d.dinner = state.dinner;
    d.dinner_word = state.dinner === '8:00' ? 'eight' : 'seven';
    d.reservation = state.reservation;
    d.people = 'you, Maya' + (state.sam === 'dinner' ? ', Sam' : state.sam === 'no' ? '' : ', Sam');
    d.sam_line = state.sam === 'unknown' ? 'Sam hasn’t answered the invitation yet' : state.sam === 'no' ? 'Sam can’t make it' : (state.sent8 === 'yes' ? (state.sam8 === 'ok' ? 'Sam said 8 works' : state.sam8 === 'cant' ? 'Sam can’t do 8' : 'Sam hasn’t answered the change yet') : 'Sam joins here');
    d.bookstore_by = state.bookstore_by === 'maya' ? 'Maya added' : state.bookstore_by === 'you' ? 'you added' : '';
    d.bookstore_by_maya = state.bookstore_by === 'maya' ? 'added by you' : 'Nora added';
    d.chapter_aft = state.grant === 'yes' ? 'Afternoon · with Maya' : 'Afternoon';
    d.chapter_aft_maya = state.grant === 'yes' ? 'Afternoon · you can edit' : 'Afternoon · Nora’s';
    d.receipt = p.receipt; d.note = p.note;
    d.cafe_k = 'Rain from about 4 · the afternoon only · Maya would see it';
    d.walk_sup = state.walk === 'cafe' ? 'Willow & Page café · dry · open till 7' : 'Brooklyn Bridge Park · you and Maya · whenever';
    d.walk_title = state.walk === 'cafe' ? 'The café at Willow & Page' : 'A walk to the river';
    d.walk_time = '~4:30';
    d.home_line = 'The table’s ' + (state.reservation === state.dinner ? 'confirmed for ' + d.dinner_word : 'still booked for ' + state.reservation + ' — you’re meeting at ' + state.dinner) + '. ' + (state.sam === 'dinner' ? (state.sent8 === 'yes' ? (state.sam8 === 'ok' ? 'Sam said 8 works.' : state.sam8 === 'cant' ? 'Sam can’t do 8.' : 'Sam hasn’t answered the change yet.') : 'Sam’s in.') : 'Sam hasn’t answered yet.');
    d.save_label = p.save_label; d.req_text = p.req_text; d.draft = p.draft;
    var shown = Object.assign({}, state); delete shown.priv; shown['private · ' + state.viewer] = p;
    d.state_json = JSON.stringify(shown, null, 1).replace(/[{}"]/g, '').trim();
    d.undo_count = String(undo[state.viewer].length);
    return d;
  }

  /* ---- show/hide grammar: "k:v|v;k2:v" (AND of clauses, OR within), "!k:v" negates a clause, "undo" = this person's stack non-empty ---- */
  function visible(expr) {
    return expr.split(';').every(function (clause) {
      clause = clause.trim(); if (!clause) return true;
      if (clause === 'undo') return undo[state.viewer].length > 0;
      if (clause === '!undo') return undo[state.viewer].length === 0;
      var neg = clause[0] === '!'; if (neg) clause = clause.slice(1);
      var i = clause.indexOf(':'); var k = clause.slice(0, i); var vals = clause.slice(i + 1).split('|');
      var hit = vals.indexOf(String(val(k))) >= 0;
      return neg ? !hit : hit;
    });
  }

  function render() {
    var root = document.querySelector('[data-proto]'); if (!root) return;
    var d = derived();
    /* idempotent: only touch the DOM when a value differs, so a re-render triggered by the observer settles */
    root.querySelectorAll('[data-show]').forEach(function (el) { var h = !visible(el.getAttribute('data-show')); if (el.hidden !== h) el.hidden = h; });
    root.querySelectorAll('[data-bind]').forEach(function (el) { var k = el.getAttribute('data-bind'); if (k in d && el.textContent !== d[k]) el.textContent = d[k]; });
    root.querySelectorAll('[data-viewer]').forEach(function (el) { el.classList.toggle('on', el.getAttribute('data-viewer') === state.viewer); });
    var p = P(state.viewer);
    var live = document.getElementById('proto-live'); if (live && live.textContent !== (p.receipt || p.note || '')) live.textContent = p.receipt || p.note || '';
  }

  function composer(v) { return document.querySelector((v || state.viewer) === 'maya' ? '#c-maya' : '#c-you'); }

  /* ---- actions: every id is a real state change or an honest refusal ---- */
  var ACT = {
    /* research viewer switch: changes whose eyes we look through; touches nobody's private record */
    'viewer:you': function () { state.viewer = 'you'; },
    'viewer:maya': function () { state.viewer = 'maya'; },
    'viewer:sam': function () { state.viewer = 'sam'; },
    'go:home': function () { set({ screen: 'home', ask: 'closed' }); },
    'go:page': function () { set({ screen: 'page' }); },
    'ask:open': function () { set({ ask: 'open' }); var inp = composer(); if (inp && P().draft && !inp.value) inp.value = P().draft; },
    'ask:close': function () { set({ ask: 'closed', offer: 'no' }); note('Closed. Nothing changed.'); },
    'chat:handoff': function () { set({ ask: 'closed' }); note('More room in Chat isn’t built in this prototype — it would carry Saturday and what you said into Chat, the same assistant with more space, and return here clean.'); },
    'reset': function () { VIEWERS.forEach(function (v) { clearTimeout(timers[v]); undo[v].length = 0; }); state = fresh(); log.length = 0; document.querySelectorAll('[data-composer]').forEach(function (i) { i.value = ''; }); },
    'undo': function () {
      var stack = undo[who()]; if (!stack.length) { note('Nothing to undo.'); return; }
      var e = stack.pop(); Object.keys(e.prior).forEach(function (k) { state[k] = e.prior[k]; });
      receipt('Undone — ' + UNDO_TEXT[e.id](e.prior), 'ink');
    },

    'add_bookstore': function () { if (state.bookstore === 'added') { note('Willow & Page is already in the afternoon.'); return; } snapshot('add_bookstore'); set({ bookstore: 'added', bookstore_by: 'you' }); receipt('Added Willow & Page to the afternoon at 3'); },
    'leave_bookstore': function () { note('Left as Maya’s suggestion. Nothing changed.'); },
    'grant': function () { if (state.grant === 'yes') { note('Maya can already change the afternoon.'); return; } snapshot('grant'); set({ grant: 'yes' }); receipt('Maya can now change the afternoon · dinner stays fixed'); },
    'end_grant': function () { if (state.grant !== 'yes') { note('Maya isn’t editing the afternoon right now.'); return; } snapshot('end_grant'); set({ grant: 'ended' }); receipt('Maya’s editing ended · her edits stay · she’s still coming', 'ink'); },
    'maya_add': function () {
      if (state.grant !== 'yes') { set({ offer: 'suggest', ask: 'open' }); note('Four works — the shop is open till 7. This is Nora’s afternoon, so nothing changed. Send it to her as your suggestion?'); return; }
      if (state.bookstore === 'added') { note('Willow & Page is already in the afternoon.'); return; }
      set({ bookstore: 'added', bookstore_by: 'maya' }); receipt('Added — Nora will see it. No approval needed.'); undo.maya.length = 0; /* crosses to Nora's view: not privately undoable */
    },
    'maya:suggest': function () { set({ offer: 'no', maya_sent: 'yes', ask: 'closed' }); receipt('Sent to Nora as a suggestion — she decides', 'ink'); },
    'offer:clear': function () { set({ offer: 'no', ask: 'closed' }); note('Kept to yourself. Nothing sent, nothing changed.'); },
    'maya_ask8': function () { if (state.dinner === '8:00') { note('Dinner is already at 8.'); return; } set({ offer: 'ask8', ask: 'open' }); note('Eight is possible for the table (they hold till 8:15). Dinner is Nora’s to change, so nothing changed. Send this to Nora as a question?'); },
    'maya:send_ask8': function () { set({ offer: 'no', maya_asked: 'yes', ask: 'closed' }); receipt('Sent to Nora as a question — dinner is hers to change', 'ink'); },
    'sam_in': function () { set({ sam: 'dinner' }); receipt('You’re in for dinner — Nora sees that, nothing else about you'); },
    'sam_cant': function () { set({ sam: 'no' }); receipt('Noted — Nora sees you can’t. Nothing else.', 'ink'); },
    'sam_ok8': function () { set({ sam8: 'ok' }); receipt('Nora sees that 8 works for you'); },
    'sam_cant8': function () { set({ sam8: 'cant' }); receipt('Nora sees you can’t do 8', 'ink'); },
    'preview:cafe': function () { if (state.walk === 'cafe') { note('You already have the café.'); return; } set({ preview: 'cafe' }); },
    'use_cafe': function () { snapshot('use_cafe'); set({ walk: 'cafe', preview: '' }); receipt('Changed — the café instead of the walk · dinner didn’t move'); },
    'keep_walk': function () { set({ preview: '' }); note('Kept the walk. Nothing changed.'); },
    'back_to_walk': function () { if (state.walk !== 'cafe') { note('The walk is already the plan.'); return; } snapshot('back_to_walk'); set({ walk: 'walk' }); receipt('Back to the walk'); },
    'preview:dinner8': function () { if (state.dinner === '8:00') { note('Dinner is already at 8.'); return; } set({ preview: 'dinner8' }); },
    'not_yet': function () { set({ preview: '' }); note('Not sent. Dinner is still at ' + state.dinner + '.'); },
    'send8': function () { set({ dinner: '8:00', sent8: 'yes', sam8: '', preview: '', maya_asked: 'no' }); undo.you.length = 0; receipt('Sent — Maya and Sam have 8:00', 'ink'); },
    'open_link': function () { receipt('Back from the Georgian room’s page — nothing here changed', 'ink'); },
    'forward': function () { if (state.reservation === state.dinner) { note('The reservation already says ' + state.dinner + '.'); return; } snapshot('forward'); set({ reservation: state.dinner }); receipt('Reservation now ' + state.dinner + ' · from your forwarded email · GR-2291 · 3'); },
    'keep7': function () { set({ maya_asked: 'no' }); note('Kept 7:00. Maya will see that it stands.'); }
  };

  /* ---- scripted recognizers (route only; guarded by state; unsupported input preserves state) ---- */
  var ROUTES = {
    you: [
      { re: /let maya|maya (can )?help|maya.*edit/i, act: 'grant' },
      { re: /take it from here|i.ll handle|end maya|stop maya/i, act: 'end_grant' },
      { re: /add (the )?(bookstore|willow)|willow.*(add|in)/i, act: 'add_bookstore' },
      { re: /(caf[eé]|rain|dry|indoor)/i, act: 'preview:cafe', when: { walk: 'walk' } },
      { re: /walk/i, act: 'back_to_walk', when: { walk: 'cafe' } },
      { re: /(8|eight)/i, act: 'preview:dinner8', when: { dinner: '7:00' } },
      { re: /forward/i, act: 'forward' },
      { re: /undo/i, act: 'undo' }
    ],
    maya: [
      { re: /add|bookstore|willow/i, act: 'maya_add' },
      { re: /(8|eight|later)/i, act: 'maya_ask8' }
    ],
    sam: []
  };
  function route(text) {
    var list = ROUTES[state.viewer] || [];
    for (var i = 0; i < list.length; i++) {
      var r = list[i];
      if (!r.re.test(text)) continue;
      if (r.when && !Object.keys(r.when).every(function (k) { return state[k] === r.when[k]; })) continue;
      var ok = commit(r.act, text); log.push(state.viewer + ' › ' + text + ' → ' + r.act + (ok ? '' : ' (held; words kept)')); if (!ok) return false;
      var p = P(); if (p.offer === 'no' && p.save === 'idle') p.ask = 'closed'; return true;
    }
    note('Nothing changed — that isn’t something this prototype can act on here. Your words are kept; supported phrases are listed beside the phone.');
    log.push(state.viewer + ' › ' + text + ' → (unsupported, no change)');
    return false;
  }

  /* ---- §0.3/§0.5 · save simulation (research chrome). Mutating private actions go through commit():
         slow → pending then apply; fail → pending then failed, nothing changed, words kept;
         unknown → pending, then 'checking…' (no promise that nothing changed), then reconciled once — retry is held until then.
         The request belongs to the person who made it: its card, its words and its recovery controls show only on their view. */
  var MUTATING = { 'add_bookstore': 1, 'use_cafe': 1, 'back_to_walk': 1, 'grant': 1, 'end_grant': 1, 'maya_add': 1, 'forward': 1 };
  var LABELS = { 'add_bookstore': 'Adding Willow & Page at 3', 'use_cafe': 'Swapping the walk for the café', 'back_to_walk': 'Putting the walk back', 'grant': 'Letting Maya change the afternoon', 'end_grant': 'Ending Maya’s editing', 'maya_add': 'Adding Willow & Page', 'forward': 'Recording the forwarded confirmation' };
  function asOwner(owner, fn) { var prev = actor; actor = owner; try { fn(); } finally { actor = prev; } }
  /* returns true when the action ran or was accepted for execution; false when it was held (this person's relevant
     mutation while another of theirs is in flight). Navigation, close, viewer, reset and research controls are never held. */
  function commit(id, text) {
    var owner = state.viewer; var p = P(owner);
    if (MUTATING[id] && (p.save === 'pending' || p.save === 'unknown')) { note('Still saving “' + (p.req_text || p.save_label) + '” — that’s kept; this one waits until it’s known.'); return false; }
    if (!MUTATING[id] || state.sim === 'none') { ACT[id](); return true; }
    var mode = state.sim; state.sim = 'none';
    set({ save: 'pending', save_label: LABELS[id] || id, req_text: text || (LABELS[id] || id), req_id: id, ask: 'closed', draft: '', note: '' });
    clearTimeout(timers[owner]);
    timers[owner] = setTimeout(function () { asOwner(owner, function () {
      if (p.save !== 'pending') return; // cancelled before commit
      if (mode === 'slow') { set({ save: 'idle', save_label: '', req_text: '', req_id: '' }); ACT[id](); render(); return; }
      if (mode === 'fail') { set({ save: 'failed', note: '' }); render(); return; }
      set({ save: 'unknown', note: '' }); render();   /* the card says: checking whether it went through; the request is still here */
      timers[owner] = setTimeout(function () { asOwner(owner, function () {
        var rid = p.req_id; set({ save: 'idle', save_label: '', req_text: '', req_id: '' }); ACT[rid](); p.receipt = p.receipt + ' · it had gone through'; render();
      }); }, 1800);
    }); }, 1500);
    return true;
  }
  ACT['sim:slow'] = function () { set({ sim: 'slow' }); note('Next change will save slowly.'); };
  ACT['sim:fail'] = function () { set({ sim: 'fail' }); note('Next change will fail to save.'); };
  ACT['sim:unknown'] = function () { set({ sim: 'unknown' }); note('Next change will be interrupted mid-save.'); };
  ACT['sim:none'] = function () { set({ sim: 'none' }); note('Simulation off.'); };
  ACT['save:retry'] = function () { var p = P(); if (p.save !== 'failed') return; var id = p.req_id; set({ save: 'idle', save_label: '', req_text: '', req_id: '' }); if (id) ACT[id](); };
  ACT['save:dismiss'] = function () { var p = P(); if (p.save !== 'failed') return; var words = p.req_text; set({ save: 'idle', save_label: '', req_text: '', req_id: '', draft: words }); note('Not now. Nothing changed — your words are kept as a draft.'); };
  ACT['save:cancel'] = function () { var p = P(); if (p.save !== 'pending') return; clearTimeout(timers[who()]); var words = p.req_text; set({ save: 'idle', save_label: '', req_text: '', req_id: '', draft: words }); note('Cancelled before it saved. Nothing changed — your words are kept as a draft.'); };
  /* Discard removes the matching restored draft from state AND from this person's field; a different or newly edited input is left alone (§0.5 D1) */
  ACT['draft:discard'] = function () { var p = P(); var d = (p.draft || '').trim(); var inp = composer(); if (inp && d && inp.value.trim() === d) inp.value = ''; set({ draft: '' }); note('Draft discarded. Nothing changed.'); };

  function onClick(e) {
    var el = e.target.closest ? e.target.closest('[data-act]') : null; if (!el) return;
    var id = el.getAttribute('data-act'); if (!ACT[id]) return;
    e.preventDefault(); commit(id); log.push(state.viewer + ' › tap ' + id); render();
  }
  function onSubmit(e) {
    var btn = e.target.closest ? e.target.closest('[data-send]') : null; if (!btn) return;
    var input = document.querySelector(btn.getAttribute('data-send')); if (!input) return;
    var text = (input.value || '').trim(); if (!text) { note('Say what you’d change.'); render(); return; }
    if (route(text)) input.value = ''; render();
  }
  function onKey(e) {
    if (e.key !== 'Enter') return; var input = e.target; if (!input.matches || !input.matches('[data-composer]')) return;
    var text = (input.value || '').trim(); if (!text) return; if (route(text)) input.value = ''; render();
  }

  function init() {
    if (init.done) return; var root = document.querySelector('[data-proto]'); if (!root) return; init.done = true;
    document.addEventListener('click', onClick); document.addEventListener('click', onSubmit); document.addEventListener('keydown', onKey);
    render();
  }
  /* the runtime may re-mount the template after our first render; re-apply state on any subtree change */
  var mo = new MutationObserver(function () { init(); if (init.done) render(); });
  mo.observe(document.documentElement, { childList: true, subtree: true });
  setTimeout(render, 300); setTimeout(render, 1200);
  if (document.readyState !== 'loading') init(); else document.addEventListener('DOMContentLoaded', init);
  /* the exposed helper takes the same path as a tap: through commit(), so simulation and duplicate-prevention apply.
     say(text) takes the same path as typing into the current viewer's field and pressing Send. */
  window.PIRL = {
    get state() { return state; }, get priv() { return state.priv[state.viewer]; }, get undo() { return undo; }, log: log, render: render,
    act: function (id) { var ok = commit(id); render(); return ok; },
    say: function (text) { var inp = composer(); if (inp) inp.value = text; var ok = route(text); if (ok && inp) inp.value = ''; render(); return ok; },
    field: function () { var inp = composer(); return inp ? inp.value : null; }
  };
})();
