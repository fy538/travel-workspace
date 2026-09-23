// Render boards from the local server; report errors, mounts, overflow at 1x and 1.3x; save full-page captures.
//   node shot_boards.mjs SCRATCH "04b - Ordinary photographs" "00 - Start here" ...
import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const [SP, ...names] = process.argv.slice(2);
const overflow = (p) => p.evaluate(() => {
  const out = [];
  const walk = (root) => { for (const e of root.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot);
    const cs = getComputedStyle(e);
    if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') continue;
    if (e.clientWidth > 0 && e.scrollWidth > e.clientWidth + 2 && e.textContent.trim())
      out.push(`${String(e.className).slice(0, 22) || e.tagName} ${e.clientWidth}->${e.scrollWidth} «${e.textContent.trim().replace(/\s+/g, ' ').slice(0, 36)}»`); } };
  walk(document); return out;
});
const scale = async (p, k) => { await p.evaluate((k) => {
  const all = []; const walk = (r) => { for (const e of r.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot); all.push(e); } };
  walk(document);
  const snap = all.map((e) => { const cs = getComputedStyle(e); return [e, parseFloat(cs.fontSize), cs.lineHeight.endsWith('px') ? parseFloat(cs.lineHeight) : null]; });
  for (const [e, fs, lh] of snap) { e.style.fontSize = (fs * k) + 'px'; if (lh !== null) e.style.lineHeight = (lh * k) + 'px'; }
}, k); await p.waitForTimeout(400); };
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const n of names) {
  const f = n.endsWith('.dc.html') ? n : n + '.dc.html';
  const p = await b.newPage({ viewport: { width: 1800, height: 1200 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error' && !/favicon|404 \(File not found\)/.test(m.text())) errs.push(m.text()); });
  await p.goto(`http://127.0.0.1:${process.env.PORT || 8771}/after/` + encodeURIComponent(f), { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  const c = {}; for (const s of ['.cpanel', '.tk', '.vdl-notice', '.vdl-sheet', '.vdl-door', 'dc-import', 'svg[role=img]']) c[s] = await p.locator(s).count();
  const size = await p.evaluate(() => ({ w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }));
  const tag = f.split(' - ')[0];
  await p.screenshot({ path: `${SP}/_cmp/b-${tag}.png`, fullPage: true });
  const o1 = await overflow(p);
  await scale(p, 1.3);
  const o13 = await overflow(p);
  await p.screenshot({ path: `${SP}/_cmp/b-${tag}-x13.png`, fullPage: true });
  console.log(tag, JSON.stringify(c), JSON.stringify(size), 'errors', JSON.stringify(errs));
  console.log('   overflow x1 ', JSON.stringify(o1.filter(s => !/^cphone 391->393/.test(s))));
  console.log('   overflow x1.3', JSON.stringify(o13.filter(s => !/^cphone 391->393/.test(s))));
  await p.close();
}
await b.close();
