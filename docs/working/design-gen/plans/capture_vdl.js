// Matched before/after captures of Plans frames by exact frame label, with fit checks. node capture_vdl.js cfg.json
const { chromium } = require('/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core');
const fs = require('fs'), path = require('path');
const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const OUT = cfg.out; fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const ctx = await browser.newContext({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 2 });
  const report = { pages: {}, frames: [] };
  async function open(url, key) {
    const page = await ctx.newPage(); const errs = [];
    page.on('pageerror', e => errs.push('pageerror: ' + e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon/.test(m.text())) errs.push('console: ' + m.text()); });
    page.on('response', r => { if (r.status() >= 400 && !/favicon/.test(r.url())) errs.push(r.status() + ' ' + r.url().split('/serve/')[1]?.split('?')[0]); });
    await page.goto(url, { waitUntil: 'load', timeout: 90000 }); await page.waitForTimeout(4500);
    await page.evaluate(() => document.fonts && document.fonts.ready); report.pages[key] = errs; return page;
  }
  const info = (page, id) => page.evaluate((id) => {
    const lab = [...document.querySelectorAll('.frame .flabel span.n')].find(s => s.textContent.trim() === id); if (!lab) return null;
    const ph = lab.closest('.frame').querySelector('.ph'); if (!ph) return null; const pr = ph.getBoundingClientRect();
    const spill = [], clipped = [];
    ph.querySelectorAll('*').forEach(el => {
      if (![...el.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim())) return;
      const r = el.getBoundingClientRect(); if (!r.width) return; const cs = getComputedStyle(el);
      if (r.right > pr.right + 1 || r.left < pr.left - 1) spill.push(el.textContent.trim().slice(0, 40));
      if (cs.overflow !== 'visible' && el.scrollWidth > el.clientWidth + 1 && cs.textOverflow !== 'ellipsis') clipped.push(el.textContent.trim().slice(0, 40));
    });
    const rows = [...ph.querySelectorAll('.chips, .inline-act')].map(c => new Set([...c.children].filter(k => k.offsetParent).map(k => Math.round(k.getBoundingClientRect().top))).size);
    const r16 = ph.querySelector('.vdl-btn.r16');
    return { vdl: ph.querySelectorAll('.vdl-btn, .vdl-door, .vdl-notice').length, spill, clipped, rows, r16: r16 ? getComputedStyle(r16).borderRadius + ' / ' + getComputedStyle(r16).minHeight : null };
  }, id);
  for (const b of cfg.boards) {
    const pages = { after: await open(b.after, b.key + ' after'), before: await open(b.before, b.key + ' before') };
    for (const id of b.frames) {
      const rec = { board: b.key, id };
      for (const side of ['before', 'after']) {
        const p = pages[side]; const i = await info(p, id); rec[side] = i; if (!i) continue;
        const esc = id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const loc = p.locator('.frame').filter({ has: p.locator('.flabel span.n', { hasText: new RegExp('^' + esc + '$') }) }).locator('.ph').first();
        rec[side + 'Png'] = path.join(OUT, `${b.key}_${id}_${side}.png`); await loc.screenshot({ path: rec[side + 'Png'] });
      }
      report.frames.push(rec);
    }
    if (b.card) { const c = pages.after.locator('.card', { hasText: b.card }).first(); await c.screenshot({ path: path.join(OUT, `${b.key}_ledger.png`) }); }
    await pages.after.close(); await pages.before.close();
  }
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 1));
  const small = await browser.newContext({ viewport: { width: 1700, height: 1000 }, deviceScaleFactor: 1 });
  const frames = report.frames.filter(r => r.afterPng); let gi = 0;
  for (let i = 0; i < frames.length; i += 4) {
    gi++; const g = frames.slice(i, i + 4);
    const cells = g.map(r => `<div><div class="lab">${r.board} · ${r.id}</div><div class="row"><figure><figcaption>BEFORE</figcaption><img src="file://${r.beforePng}"></figure><figure><figcaption>AFTER · SHARED PACKAGE</figcaption><img src="file://${r.afterPng}"></figure></div></div>`).join('');
    const hp = path.join(OUT, `composite-${gi}.html`);
    fs.writeFileSync(hp, `<html><body style="margin:0;background:#E8E2D4"><style>.w{display:grid;grid-template-columns:repeat(2,max-content);gap:30px 36px;padding:26px}.lab{font:700 14px ui-monospace,Menlo,monospace;letter-spacing:1px;margin:0 0 8px;color:#3C352E}.row{display:flex;gap:14px}figure{margin:0}figcaption{font:600 11px ui-monospace,Menlo,monospace;letter-spacing:1px;color:#6E6862;margin:0 0 6px}img{width:393px;display:block;border-radius:24px;box-shadow:0 8px 24px rgba(0,0,0,.14)}</style><div class="w">${cells}</div></body></html>`);
    const p = await small.newPage(); await p.goto('file://' + hp); await p.waitForTimeout(600); await p.screenshot({ path: path.join(OUT, `composite-${gi}.png`), fullPage: true }); await p.close();
  }
  await browser.close();
  for (const r of report.frames) { const a = r.after || {}, b = r.before || {};
    const wrap = JSON.stringify(b.rows) === JSON.stringify(a.rows) ? 'same' : `CHANGED ${JSON.stringify(b.rows)}→${JSON.stringify(a.rows)}`;
    console.log(`${r.board.padEnd(3)} ${r.id.padEnd(4)} | shared nodes before=${b.vdl ?? '–'} after=${a.vdl ?? '–'} | button rows ${wrap} | spill ${a.spill?.length ?? '–'}${a.spill?.length ? ' ' + JSON.stringify(a.spill.slice(0, 2)) : ''} | clipped ${a.clipped?.length ?? '–'}${a.clipped?.length ? ' ' + JSON.stringify(a.clipped.slice(0, 2)) : ''}${a.r16 ? ' | r16 ' + a.r16 : ''}`); }
  const bad = Object.entries(report.pages).filter(([, e]) => e.length); console.log('pages checked:', Object.keys(report.pages).length, '| pages with errors:', bad.length); bad.forEach(([k, e]) => console.log('  ', k, e.slice(0, 4)));
  console.log('composites:', gi);
})().catch(e => { console.error(e); process.exit(1); });
