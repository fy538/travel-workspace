/* vdl-refs.js — mounts live crops of original donor frames copied under refs/.
 * <div data-ref="refs/social/02 - A little of your world.dc.html" data-sig="THE PRINT ROOM, OPENED"
 *      data-y="0" data-h="800" data-scale="1"></div>
 * The frame is found by a text signature among 340–440px-wide phone frames and shown through an
 * iframe of the copied board. Nothing is redrawn; a missing frame reports data-ref-status="not found". */
(function () {
  function mount(el) {
    if (el.getAttribute('data-ref-status')) return;
    el.setAttribute('data-ref-status', 'loading');
    var scale = parseFloat(el.getAttribute('data-scale') || '1');
    var y = parseFloat(el.getAttribute('data-y') || '0');
    var h = el.hasAttribute('data-h') ? parseFloat(el.getAttribute('data-h')) : null;
    var sig = el.getAttribute('data-sig');
    var f = document.createElement('iframe');
    f.src = el.getAttribute('data-ref').split('/').map(encodeURIComponent).join('/');
    f.title = 'Original frame: ' + sig;
    f.style.cssText = 'position:absolute;left:0;top:0;width:3600px;height:10000px;border:0;transform-origin:0 0;pointer-events:none';
    el.style.position = 'relative';
    el.style.overflow = 'hidden';
    el.appendChild(f);
    function crop(n) {
      var d = null;
      try { d = f.contentDocument; } catch (e) { el.setAttribute('data-ref-status', 'blocked'); return; }
      var all = d && d.body ? Array.prototype.slice.call(d.body.querySelectorAll('*')) : [];
      var c = all.filter(function (e) { var r = e.getBoundingClientRect(); return r.width >= 340 && r.width <= 440 && r.height >= 400; });
      var outer = c.filter(function (e) { return !c.some(function (o) { return o !== e && o.contains(e); }); });
      var hit = outer.filter(function (e) { return (e.innerText || '').replace(/\s+/g, ' ').indexOf(sig) >= 0; })[0];
      if (!hit) { if (n < 40) { setTimeout(function () { crop(n + 1); }, 400); } else { el.setAttribute('data-ref-status', 'not found'); } return; }
      var r = hit.getBoundingClientRect();
      var ch = h !== null ? Math.min(h, r.height - y) : r.height - y;
      f.style.transform = 'scale(' + scale + ') translate(' + (-r.left) + 'px,' + (-(r.top + y)) + 'px)';
      el.style.width = (r.width * scale) + 'px';
      el.style.height = (ch * scale) + 'px';
      el.setAttribute('data-ref-status', 'ok');
    }
    f.addEventListener('load', function () { setTimeout(function () { crop(0); }, 600); });
  }
  window.vdlMountRefs = function () { Array.prototype.forEach.call(document.querySelectorAll('[data-ref]'), mount); };
})();
