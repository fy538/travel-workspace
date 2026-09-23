import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
const SP = process.argv[2], CMP = SP + '/_cmp';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const f of ['08 - The actual source.dc.html', '09 - Finishing a local action.dc.html']) {
  const p = await b.newPage({ viewport: { width: 1800, height: 1200 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error' && !/favicon|404 \(File not found\)/.test(m.text())) errs.push(m.text()); });
  await p.goto('http://127.0.0.1:8771/after/' + encodeURIComponent(f), { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  const c = {}; for (const s of ['.cpanel', '.tk', '.vdl-notice', '.vdl-sheet', '.vdl-door', 'dc-import']) c[s] = await p.locator(s).count();
  const size = await p.evaluate(() => ({ w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }));
  await p.screenshot({ path: `${CMP}/new-${f.slice(0, 2)}.png`, fullPage: true });
  console.log(f.slice(0, 2), JSON.stringify(c), JSON.stringify(size), 'errors', JSON.stringify(errs));
  await p.close();
}
await b.close();
