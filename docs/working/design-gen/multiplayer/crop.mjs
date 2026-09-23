import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const url = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 1860, height: 1400 }, deviceScaleFactor: 1 });
await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(3500);
const info = await p.evaluate(() => {
  const root = [...document.querySelectorAll('div')].find(d => d.style.minHeight && d.style.background);
  root.style.minHeight = '0px';
  const rows = [...root.querySelectorAll(':scope > div > div')].map(e => { const r = e.getBoundingClientRect(); return { top: Math.round(r.top + scrollY), h: Math.round(r.height) }; });
  return { h: Math.ceil(root.getBoundingClientRect().height), unresolved: document.querySelectorAll('dc-import:not([data-dc-mounted])').length, rows };
});
console.log(JSON.stringify(info));
await p.screenshot({ path: 'shots/c1.png', fullPage: true });
// three crops, one per row of pairs (rows 1..3 of the stacked blocks)
for (let i = 1; i <= 3; i++) { const r = info.rows[i + 3]; await p.screenshot({ path: `shots/c1-row${i}.png`, clip: { x: 0, y: r.top - 8, width: 1860, height: r.h + 16 }, fullPage: true }); }
await b.close();
