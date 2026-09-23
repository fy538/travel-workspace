/* vdl-port.js — fidelity reference for the Stage 1 workbench (§17–§19).
 * <div data-port="refs/home/02 - Persona A - The New Yorker.dc.html" data-sig="The current ordinary scroll"
 *      data-report="report-home" [data-y="0" data-h="600"] [data-fit='[{"text":"X","n":0,"dx":0,"dy":0,"why":""}]']></div>
 * Clones the selected donor phone frame with its geometry (diagrams, icons, lines, maps) and its
 * computed styling carried inline. Matched colors become kernel token references; unmatched
 * colors stay. Matched text runs are ANNOTATED with data-role (a kernel role, or a proposed
 * vdl role for a named gap); their size, weight and leading stay copied values, so a change to a
 * role definition does not by itself update this text (§19.2). Changes applied: an accepted ruling
 * where one governs, the 10px floor (one-line labels stay on one line), and any named fit
 * corrections given in data-fit. This is a fidelity diagnostic, not component-built construction. */
(function () {
  var SVGNS = 'http://www.w3.org/2000/svg';
  var SIZE = /^(width|height)$/;
  var SKIP = /^(transition|animation|cursor|will-change|caret|user-select|pointer-events|content$|counter|quotes|page|orphans|widows|speak|view-transition|anchor|position-try|timeline|scroll-|inline-size|block-size|-webkit-(?!line-clamp|box-orient|text-fill-color|text-stroke|mask|box-decoration))/;
  var INH = /^(color|font|line-height|letter-spacing|word-spacing|text-(align|indent|transform|shadow|rendering|wrap|size-adjust)|white-space|word-break|overflow-wrap|hyphens|tab-size|visibility|direction|writing-mode|list-style|fill|stroke|paint-order|-webkit-text-(fill-color|stroke))/;
  var RULINGS = [{ fam: 'serif', size: 30, lh: 34, weight: '600', set: [['font-weight', '700']], role: 'serifMast', why: 'Mast 600 → serifMast 700 (2026-08-30 ruling)' }];
  var ctx = null;

  function famOf(f) { f = (f || '').toLowerCase(); if (/mono|menlo|courier|consolas/.test(f)) return 'mono'; if (/garamond|georgia|times/.test(f)) return 'serif'; return 'sans'; }
  function px(v) { var n = parseFloat(v); return isNaN(n) ? v : Math.round(n * 2) / 2; }

  function buildCtx() {
    if (ctx) return ctx;
    var probe = document.createElement('span');
    probe.style.cssText = 'position:absolute;left:-9999px;top:0';
    document.body.appendChild(probe);
    var names = [], roles = [], fonts = {};
    function walk(rules) {
      Array.prototype.forEach.call(rules || [], function (r) {
        if (r.styleSheet) { try { walk(r.styleSheet.cssRules); } catch (e) {} return; }
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); return; }
        if (!r.selectorText) return;
        if (/:root/.test(r.selectorText)) { for (var i = 0; i < r.style.length; i++) { var n = r.style[i]; if ((n.indexOf('--vk-') === 0 || n.indexOf('--vdl-') === 0) && names.indexOf(n) < 0) names.push(n); } }
        var m = r.selectorText.match(/^\.(vk|vdl)-t-([A-Za-z0-9]+)$/); if (m && roles.indexOf(m[1] + ':' + m[2]) < 0) roles.push(m[1] + ':' + m[2]);
        if (r.cssRules && r.cssRules.length) walk(r.cssRules);
      });
    }
    Array.prototype.forEach.call(document.styleSheets, function (sh) { var rules; try { rules = sh.cssRules; } catch (e) { return; } walk(rules); });
    var rank = function (n) { return /^--vk-(ink|paper|gold)\d/.test(n) ? 0 : /^--vk-color-/.test(n) ? 1 : /^--vk-state-color-/.test(n) ? 2 : /^--vk-/.test(n) ? 3 : 4; };
    names.sort(function (a, b) { return rank(a) - rank(b); });
    var colors = {};
    names.forEach(function (n) {
      if (/^--vk-font-(serif|sans|mono)$/.test(n)) { fonts[n.slice(10)] = n; return; }
      if (/^--vk-font/.test(n)) return;
      probe.style.color = 'rgb(1, 2, 3)'; probe.style.color = 'var(' + n + ')';
      var c = getComputedStyle(probe).color;
      if (c !== 'rgb(1, 2, 3)' && /^rgb\(/.test(c) && !colors[c]) colors[c] = n;
    });
    probe.style.color = '';
    var table = [];
    roles.forEach(function (pr) {
      var parts = pr.split(':');
      probe.className = parts[0] + '-t-' + parts[1]; probe.textContent = 'x';
      var s = getComputedStyle(probe);
      table.push({ role: parts[1], proposed: parts[0] === 'vdl', fam: famOf(s.fontFamily), size: px(s.fontSize), lh: s.lineHeight === 'normal' ? 'normal' : px(s.lineHeight), weight: s.fontWeight, style: s.fontStyle });
    });
    probe.remove();
    var built = { colors: colors, roles: table, fonts: fonts, names: names.length };
    window.vdlPortCtx = built;
    if (names.length && table.length) ctx = built; // cache only once the kernel stylesheet is readable
    return built;
  }

  function mapColor(m, st, c) {
    var p = m.match(/[\d.]+/g); if (!p) return m;
    var a = p.length > 3 ? parseFloat(p[3]) : 1; if (a === 0) return m;
    var key = 'rgb(' + p[0] + ', ' + p[1] + ', ' + p[2] + ')';
    var n = c.colors[key], near = false;
    if (!n) {
      var best = null, bd = 1e9;
      Object.keys(c.colors).forEach(function (k) { var q = k.match(/\d+/g); var d = Math.abs(q[0] - p[0]) + Math.abs(q[1] - p[1]) + Math.abs(q[2] - p[2]); if (d < bd) { bd = d; best = k; } });
      if (best && bd <= 9) { n = c.colors[best]; near = true; }
    }
    if (!n) { var hex = '#' + [p[0], p[1], p[2]].map(function (x) { return ('0' + (+x).toString(16)).slice(-2); }).join('').toUpperCase(); st.colorGaps[hex] = (st.colorGaps[hex] || 0) + 1; return m; }
    if (n.indexOf('--vdl-') === 0) st.colorProposed++; else if (near) st.colorNear++; else st.colorExact++;
    st.tokens[n] = (st.tokens[n] || 0) + 1;
    return a < 1 ? 'color-mix(in srgb, var(' + n + ') ' + Math.round(a * 100) + '%, transparent)' : 'var(' + n + ')';
  }

  function ownText(el) { var s = ''; for (var c = el.firstChild; c; c = c.nextSibling) if (c.nodeType === 3) s += c.nodeValue; return s.trim(); }

  // A size is carried over only when it is not content-driven: the donor element is measured
  // with that dimension set to auto, and the drawn value is kept if the box would change.
  function keepSize(src, p, cs, isRoot) {
    if (isRoot) return p === 'width';
    var tag = src.tagName.toLowerCase();
    if (/^(img|svg|canvas|video|iframe|image)$/.test(tag) || src.namespaceURI === SVGNS) return true;
    if (cs.display === 'inline' || cs.display === 'none' || cs.display === 'contents') return false;
    var before = src.getBoundingClientRect()[p];
    var old = src.style.getPropertyValue(p), prio = src.style.getPropertyPriority(p);
    src.style.setProperty(p, 'auto', 'important');
    var after = src.getBoundingClientRect()[p];
    if (old) src.style.setProperty(p, old, prio); else src.style.removeProperty(p);
    return Math.abs(after - before) > 0.5;
  }

  function styleFor(src, view, def, pcs, isRoot, st, c, pseudo) {
    var cs = view.getComputedStyle(src, pseudo || null), out = [], vals = {};
    for (var i = 0; i < cs.length; i++) { var q = cs[i]; vals[q] = cs.getPropertyValue(q); }
    for (var p in vals) {
      if (SKIP.test(p)) continue;
      var v = vals[p];
      if (SIZE.test(p) && !pseudo && !keepSize(src, p, cs, isRoot)) continue;
      if (!isRoot) { if (INH.test(p) ? (pcs && v === pcs.getPropertyValue(p)) : v === def[p]) continue; }
      if (/rgba?\(/.test(v)) v = v.replace(/rgba?\([^)]*\)/g, function (m) { return mapColor(m, st, c); });
      if (p === 'font-family') v = 'var(' + (c.fonts[famOf(v)] || '--vk-font-sans') + ')';
      out.push([p, v]);
    }
    return { cs: vals, out: out };
  }

  function typeOf(cs, el, st, c) {
    var fam = famOf(cs['font-family']), size = px(cs['font-size']), lh = cs['line-height'] === 'normal' ? 'normal' : px(cs['line-height']);
    var w = String(cs['font-weight']), sty = cs['font-style'];
    var sample = (el.innerText || el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 42);
    if (size < 10) { st.floor.push(fam + ' ' + size + ' · ' + sample); return { floor: true }; }
    for (var i = 0; i < RULINGS.length; i++) { var R = RULINGS[i]; if (R.fam === fam && R.size === size && R.lh === lh && R.weight === w) { st.rulings.push(R.why + ' · ' + sample); return { ruling: R }; } }
    var fit = function (r) { return r.fam === fam && r.size === size && String(r.weight) === w && r.style === 'normal' && (sty === 'normal' || sty === 'italic'); };
    var kern = c.roles.filter(function (r) { return !r.proposed && r.fam === fam && r.size === size && String(r.weight) === w && r.style === sty; });
    var exact = kern.filter(function (r) { return r.lh === lh || r.lh === 'normal'; })[0];
    if (exact) { st.typeExact++; st.roles[exact.role] = (st.roles[exact.role] || 0) + 1; return { role: exact.role }; }
    var prop = c.roles.filter(function (r) { return r.proposed && fit(r) && (r.lh === lh || r.lh === 'normal'); })[0];
    if (prop) { st.typeProposed++; st.proposed[prop.role] = (st.proposed[prop.role] || 0) + 1; return { role: 'vdl:' + prop.role }; }
    var tag = fam + ' ' + size + '/' + lh + ' ' + w + (sty === 'italic' ? ' italic' : '');
    if (kern.length) { st.typeNear++; var k0 = tag + ' → ' + kern[0].role + ' (' + kern[0].size + '/' + kern[0].lh + ')'; st.near[k0] = st.near[k0] || { n: 0, s: sample }; st.near[k0].n++; return { role: kern[0].role, near: true }; }
    st.typeGaps[tag] = st.typeGaps[tag] || { n: 0, s: sample }; st.typeGaps[tag].n++;
    return {};
  }

  function port(src, dst, view, cache, scratch, isRoot, st, c) {
    var key = (src.namespaceURI || '') + '|' + src.tagName, def = cache[key];
    if (!def) {
      var d = src.ownerDocument.createElementNS(src.namespaceURI, src.tagName);
      (src.namespaceURI === SVGNS && src.tagName.toLowerCase() !== 'svg' ? scratch.svg : scratch.div).appendChild(d);
      var dcs = view.getComputedStyle(d); def = {}; for (var i = 0; i < dcs.length; i++) def[dcs[i]] = dcs.getPropertyValue(dcs[i]);
      d.remove(); cache[key] = def;
    }
    var pcs = isRoot ? null : view.getComputedStyle(src.parentElement);
    var r = styleFor(src, view, def, pcs, isRoot, st, c);
    st.elements++;
    if (ownText(src)) {
      var t = typeOf(r.cs, src, st, c);
      if (t.floor) {
        var lhpx = parseFloat(r.cs['line-height']) || parseFloat(r.cs['font-size']) * 1.3;
        r.out.push(['font-size', '10px']);
        if (parseFloat(r.cs['line-height']) < 12) r.out.push(['line-height', 'normal']);
        if (src.getBoundingClientRect().height <= lhpx * 1.5) r.out.push(['white-space', 'nowrap']);
        dst.setAttribute('data-floor', '10');
      }
      if (t.ruling) { t.ruling.set.forEach(function (kv) { r.out.push(kv); }); dst.setAttribute('data-role', t.ruling.role); dst.setAttribute('data-ruling', '1'); }
      if (t.role) dst.setAttribute('data-role', t.role + (t.near ? '~' : ''));
    }
    if (src.tagName === 'IMG') dst.setAttribute('src', src.currentSrc || src.src);
    dst.removeAttribute('class');
    dst.setAttribute('style', r.out.map(function (kv) { return kv[0] + ':' + kv[1]; }).join(';'));
    var sk = src.children, dk = dst.children;
    for (var j = 0; j < sk.length; j++) if (dk[j]) port(sk[j], dk[j], view, cache, scratch, false, st, c);
    ['::before', '::after'].forEach(function (ps) {
      var pc = view.getComputedStyle(src, ps), cn = pc.getPropertyValue('content');
      if (!cn || cn === 'none' || cn === 'normal') return;
      var span = document.createElement('span');
      span.textContent = /^["']/.test(cn) ? cn.slice(1, -1) : '';
      var pr = styleFor(src, view, cache['|SPAN'] || {}, view.getComputedStyle(src), false, st, c, ps);
      span.setAttribute('style', pr.out.map(function (kv) { return kv[0] + ':' + kv[1]; }).join(';'));
      span.setAttribute('data-pseudo', ps);
      if (ps === '::before') dst.insertBefore(span, dst.firstChild); else dst.appendChild(span);
    });
  }

  // Named fit corrections (§19.4): move one label by a stated offset; nothing else changes.
  function applyFits(host, clone, st) {
    var fits = []; try { fits = JSON.parse(host.getAttribute('data-fit') || '[]'); } catch (e) { st.fits.push('data-fit is not valid JSON'); return; }
    fits.forEach(function (f) {
      var hits = Array.prototype.filter.call(clone.querySelectorAll('*'), function (e) { return ownText(e) === f.text; });
      var el = hits[f.n || 0];
      if (!el) { st.fits.push('NOT FOUND · ' + f.text); return; }
      el.style.transform = 'translate(' + (f.dx || 0) + 'px, ' + (f.dy || 0) + 'px) ' + (el.style.transform || '');
      el.setAttribute('data-fit', '1');
      st.fits.push(f.text + ' · ' + f.why);
    });
  }

  function report(st, host) {
    var id = host.getAttribute('data-report'); var box = id && document.getElementById(id); if (!box) return;
    function rows(obj, fmt) { return Object.keys(obj).sort(function (a, b) { return (obj[b].n || obj[b]) - (obj[a].n || obj[a]); }).map(fmt).join(''); }
    function row(label, val) { return '<tr><td class="vk-t-bodySm">' + label + '</td><td class="vk-t-monoValue">' + val + '</td></tr>'; }
    var h = '<p class="vk-t-caption" style="margin:0 0 8px;color:var(--vk-ink40)">Fidelity reference, computed live. Colors are token references; text keeps its copied values and is annotated with the matching role.</p>' +
      '<table class="vdl-table"><tr><th class="vk-t-capsMicro">Measure</th><th class="vk-t-capsMicro">Result</th></tr>' +
      row('Elements carried over, geometry unchanged', st.elements) +
      row('Color uses re-pointed to an exact kernel token', st.colorExact) +
      row('Color uses snapped to a kernel token within 9/765', st.colorNear) +
      row('Color uses re-pointed to a proposed vdl token', st.colorProposed) +
      row('Text runs matching a kernel role (annotated)', st.typeExact) +
      row('Text runs matching a proposed vdl role (annotated, named gap)', st.typeProposed) +
      row('Text runs matching a kernel role’s size and weight, drawn leading kept', st.typeNear) +
      row('Text runs with no role at all', Object.keys(st.typeGaps).reduce(function (s, k) { return s + st.typeGaps[k].n; }, 0)) +
      row('Accepted-ruling cleanups', st.rulings.length) +
      row('Text runs raised to the 10px floor', st.floor.length) +
      row('Named fit corrections', st.fits.length) + '</table>';
    var pr = rows(st.proposed, function (k) { return '<tr><td class="vk-t-monoValue">vdl-t-' + k + '</td><td class="vk-t-monoValue">' + st.proposed[k] + '</td></tr>'; });
    var tg = rows(st.typeGaps, function (k) { return '<tr><td class="vk-t-monoValue">' + k + '</td><td class="vk-t-monoValue">' + st.typeGaps[k].n + '</td><td class="vk-t-bodySm">' + st.typeGaps[k].s + '</td></tr>'; });
    var nr = rows(st.near, function (k) { return '<tr><td class="vk-t-monoValue">' + k + '</td><td class="vk-t-monoValue">' + st.near[k].n + '</td><td class="vk-t-bodySm">' + st.near[k].s + '</td></tr>'; });
    var cg = Object.keys(st.colorGaps).map(function (k) { return '<tr><td class="vk-t-monoValue"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;background:' + k + '"></span>' + k + '</td><td class="vk-t-monoValue">' + st.colorGaps[k] + '</td></tr>'; }).join('');
    var sec = function (t, body) { return '<div class="vk-t-monoStampStrong" style="margin-top:14px;color:var(--vk-gold80)">' + t + '</div><table class="vdl-table">' + (body || '<tr><td class="vk-t-bodySm">None</td></tr>') + '</table>'; };
    h += sec('PROPOSED ROLES MATCHED · KEPT AS DRAWN', pr) + sec('KERNEL SIZE AND WEIGHT, DRAWN LEADING KEPT', nr) + sec('TYPE WITH NO ROLE AT ALL · KEPT AS DRAWN', tg) + sec('COLORS WITH NO TOKEN · KEPT AS DRAWN', cg);
    if (st.rulings.length) h += '<div class="vk-t-monoStampStrong" style="margin-top:14px;color:var(--vk-gold80)">ACCEPTED-RULING CLEANUP</div><p class="vk-t-bodySm" style="margin:4px 0 0">' + st.rulings.join(' • ') + '</p>';
    if (st.floor.length) h += '<div class="vk-t-monoStampStrong" style="margin-top:14px;color:var(--vk-gold80)">RAISED TO THE 10PX FLOOR</div><p class="vk-t-bodySm" style="margin:4px 0 0">' + st.floor.slice(0, 24).join(' • ') + (st.floor.length > 24 ? ' …' : '') + '</p>';
    if (st.fits.length) h += '<div class="vk-t-monoStampStrong" style="margin-top:14px;color:var(--vk-gold80)">NAMED FIT CORRECTIONS</div><p class="vk-t-bodySm" style="margin:4px 0 0">' + st.fits.join(' • ') + '</p>';
    box.innerHTML = h;
  }

  function run(host) {
    if (host.getAttribute('data-port-status')) return;
    host.setAttribute('data-port-status', 'loading');
    var sig = host.getAttribute('data-sig');
    var f = document.createElement('iframe');
    f.src = host.getAttribute('data-port').split('/').map(encodeURIComponent).join('/');
    f.setAttribute('aria-hidden', 'true');
    f.style.cssText = 'position:absolute;left:-20000px;top:0;width:3600px;height:10000px;border:0;opacity:0';
    document.body.appendChild(f);
    function find(n) {
      var d; try { d = f.contentDocument; } catch (e) { host.setAttribute('data-port-status', 'blocked'); return; }
      var all = d && d.body ? Array.prototype.slice.call(d.body.querySelectorAll('*')) : [];
      var cands = all.filter(function (e) { var r = e.getBoundingClientRect(); return r.width >= 340 && r.width <= 440 && r.height >= 400; });
      var outer = cands.filter(function (e) { return !cands.some(function (o) { return o !== e && o.contains(e); }); });
      var hit = outer.filter(function (e) { return (e.innerText || '').replace(/\s+/g, ' ').indexOf(sig) >= 0; })[0];
      var c = buildCtx();
      if (!hit || !c.names || !c.roles.length) { if (n < 50) setTimeout(function () { find(n + 1); }, 400); else host.setAttribute('data-port-status', hit ? 'no kernel' : 'not found'); return; }
      var view = d.defaultView;
      var phone = [hit].concat(Array.prototype.slice.call(hit.querySelectorAll('div'))).filter(function (e) { var r = e.getBoundingClientRect(), b = view.getComputedStyle(e).backgroundColor; return r.width >= 340 && r.width <= 440 && r.height >= 400 && b !== 'rgba(0, 0, 0, 0)'; })[0] || hit;
      (d.fonts ? d.fonts.ready : Promise.resolve()).then(function () {
        var scratch = { div: d.createElement('div') }; scratch.div.style.cssText = 'position:absolute;left:-9999px;top:0'; d.body.appendChild(scratch.div);
        scratch.svg = d.createElementNS(SVGNS, 'svg'); scratch.div.appendChild(scratch.svg);
        var sp = d.createElement('span'); scratch.div.appendChild(sp); var scs = view.getComputedStyle(sp), cache = {}; cache['|SPAN'] = {}; for (var i = 0; i < scs.length; i++) cache['|SPAN'][scs[i]] = scs.getPropertyValue(scs[i]); sp.remove();
        var st = { elements: 0, colorExact: 0, colorNear: 0, colorProposed: 0, colorGaps: {}, tokens: {}, typeExact: 0, typeProposed: 0, typeNear: 0, typeGaps: {}, near: {}, roles: {}, proposed: {}, rulings: [], floor: [], fits: [] };
        var clone = document.importNode(phone, true);
        port(phone, clone, view, cache, scratch, true, st, c);
        clone.style.margin = '0'; clone.style.flex = '0 0 auto';
        host.innerHTML = '';
        var hh = host.getAttribute('data-h');
        if (hh) {
          var wrap = document.createElement('div');
          wrap.style.cssText = 'overflow:hidden;height:' + parseFloat(hh) + 'px;border-radius:var(--vk-radius-card)';
          clone.style.marginTop = (-parseFloat(host.getAttribute('data-y') || '0')) + 'px';
          wrap.appendChild(clone); host.appendChild(wrap);
        } else host.appendChild(clone);
        applyFits(host, clone, st);
        host.setAttribute('data-original-height', Math.round(phone.getBoundingClientRect().height));
        host.setAttribute('data-port-height', Math.round(clone.getBoundingClientRect().height));
        host.setAttribute('data-port-gaps', Object.keys(st.typeGaps).length + ' type, ' + Object.keys(st.colorGaps).length + ' color, ' + st.floor.length + ' floor, ' + st.rulings.length + ' ruling, ' + st.fits.length + ' fit');
        host.vdlPortStats = st;
        report(st, host);
        host.setAttribute('data-port-status', 'ok');
        f.remove();
      });
    }
    f.addEventListener('load', function () { setTimeout(function () { find(0); }, 800); });
  }

  window.vdlMountPorts = function () { Array.prototype.forEach.call(document.querySelectorAll('[data-port]'), run); };
})();
