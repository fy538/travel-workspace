/* vdl-pkgcheck.js — live version check for 06 Shared Package.
 * Any element with data-path and data-sha is re-hashed (SHA-256 of the served bytes) and marked
 * data-check="ok" | "changed" | "error". Used only for CSS, which is served byte-exact; components
 * are versioned by etag (see vdl-package.json). Workbench instrument, not part of the package.
 * It starts itself and re-runs for 20s, because the board may re-render after mount and reset
 * a cell that was already marked. */
(function () {
  var results = {};
  function hex(buf) { return Array.prototype.map.call(new Uint8Array(buf), function (b) { return ('0' + b.toString(16)).slice(-2); }).join(''); }
  function paint(cell, r) { cell.textContent = r.text; cell.setAttribute('data-check', r.state); }
  window.vdlPkgCheck = function () {
    Array.prototype.forEach.call(document.querySelectorAll('[data-sha][data-path]'), function (cell) {
      var path = cell.getAttribute('data-path'), sha = cell.getAttribute('data-sha'), key = path + '#' + sha;
      if (results[key] && results[key].state !== 'running') { if (cell.getAttribute('data-check') !== results[key].state) paint(cell, results[key]); return; }
      if (results[key]) return;
      results[key] = { state: 'running', text: 'checking…' };
      fetch(path.split('/').map(encodeURIComponent).join('/'), { cache: 'no-store' })
        .then(function (r) { return r.text(); })
        .then(function (t) { return crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)); })
        .then(function (d) {
          var h = hex(d), ok = h === sha;
          results[key] = { state: ok ? 'ok' : 'changed', text: ok ? 'Matches the recorded sha256' : 'Changed since recording: ' + h.slice(0, 8) + '…' };
          window.vdlPkgCheck();
        })
        .catch(function (e) { results[key] = { state: 'error', text: 'Could not check: ' + e.message }; window.vdlPkgCheck(); });
    });
  };
  var n = 0, t = setInterval(function () { window.vdlPkgCheck(); if (++n >= 40) clearInterval(t); }, 500);
})();
