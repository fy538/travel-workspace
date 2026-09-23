// Headless capture for the Home adoption checks (2026-09-11). System Chrome via playwright-core.
// node shot.js <url> <out.png> [--width 2800] [--sig "text"] [--y 0] [--h 0] [--scale 1] [--textscale 1] [--vw 0]
//  --sig   crop to the 393px phone inside the column whose text contains sig (vdl-refs' rule: the outermost
//          340–440px frame containing the signature, then its first painted 380–400px child)
//  --textscale  multiply every font-size and px line-height inside that phone (a 1.3x larger-text diagnostic)
//  --vw    force the phone to this width (a narrow-width diagnostic)
// Prints JSON: page errors, dc-import count, mounted count, crop box, overflow findings.
const { chromium } = require('/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core');
const a = process.argv.slice(2); const url = a[0], out = a[1];
const opt = (k, d) => { const i = a.indexOf('--' + k); return i >= 0 ? a[i + 1] : d; };
(async () => {
  const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
  const p = await b.newPage({ viewport: { width: +opt('width', 2800), height: 1400 }, deviceScaleFactor: +opt('scale', 1) });
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error' && !/favicon/.test(m.text())) errs.push('console: ' + m.text()); });
  p.on('response', r => { if (r.status() >= 400 && !/favicon/.test(r.url())) errs.push(r.status() + ' ' + decodeURIComponent(r.url().split('?')[0].split('/').pop())); });
  await p.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
  await p.waitForTimeout(+opt('wait', 3000));
  const sig = opt('sig', ''), ts = +opt('textscale', 1), vw = +opt('vw', 0);
  const info = await p.evaluate(({ sig, ts, vw }) => {
    const res = { imports: document.querySelectorAll('dc-import').length };
    res.mounted = [...document.querySelectorAll('dc-import')].filter(e => e.getBoundingClientRect().height > 8).length;
    if (!sig) { res.box = { x: 0, y: 0, w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }; return res; }
    const c = [...document.querySelectorAll('div')].filter(e => { const r = e.getBoundingClientRect(); return r.width >= 340 && r.width <= 440 && r.height >= 400; });
    const outer = c.filter(e => !c.some(o => o !== e && o.contains(e)));
    const hit = outer.find(e => (e.innerText || '').replace(/\s+/g, ' ').includes(sig));
    if (!hit) { res.error = 'signature not found'; return res; }
    const phone = [hit, ...hit.querySelectorAll('div')].find(e => { const r = e.getBoundingClientRect(); const bg = getComputedStyle(e).backgroundColor; return r.width >= 380 && r.width <= 400 && r.height >= 400 && bg !== 'rgba(0, 0, 0, 0)'; }) || hit;
    if (vw) phone.style.width = vw + 'px';
    if (ts !== 1) {
      const all = [phone, ...phone.querySelectorAll('*')];
      const cs = all.map(e => getComputedStyle(e));
      const vals = cs.map(s => [parseFloat(s.fontSize), s.lineHeight]);
      all.forEach((e, i) => { const [fs, lh] = vals[i]; e.style.fontSize = (fs * ts) + 'px'; if (/px$/.test(lh)) e.style.lineHeight = (parseFloat(lh) * ts) + 'px'; });
    }
    // Overflow: any text box that spills outside the phone horizontally, or clips its own text.
    const pr = phone.getBoundingClientRect(); res.overflow = [];
    phone.querySelectorAll('*').forEach(e => {
      const r = e.getBoundingClientRect(); if (!r.width || !(e.innerText || '').trim()) return;
      if (r.right > pr.right + 1 || r.left < pr.left - 1) res.overflow.push('spills: ' + (e.innerText || '').trim().slice(0, 40));
      const s = getComputedStyle(e);
      if ((s.overflow === 'hidden' || s.textOverflow === 'ellipsis') && e.scrollWidth > e.clientWidth + 1 && e.children.length === 0) res.overflow.push('clips: ' + e.innerText.trim().slice(0, 40));
    });
    res.overflow = [...new Set(res.overflow)].slice(0, 12);
    res.box = { x: pr.left + scrollX, y: pr.top + scrollY, w: pr.width, h: pr.height };
    return res;
  }, { sig, ts, vw });
  if (info.box) {
    const y0 = info.box.y + (+opt('y', 0)); const hh = +opt('h', 0) || (info.box.h - (+opt('y', 0)));
    await p.setViewportSize({ width: Math.max(+opt('width', 2800), Math.ceil(info.box.x + info.box.w) + 10), height: 1400 });
    await p.screenshot({ path: out, fullPage: true, clip: { x: info.box.x, y: y0, width: info.box.w, height: hh } });
  }
  console.log(JSON.stringify({ ...info, errs: [...new Set(errs)].slice(0, 12) }));
  await b.close();
})().catch(e => { console.log(JSON.stringify({ fatal: String(e) })); process.exit(1); });
