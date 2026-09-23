import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const url = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 1980, height: 1400 }, deviceScaleFactor: 1 });
await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(4000);
const info = await p.evaluate(() => {
  const root = [...document.querySelectorAll('div')].find(d => d.style.minHeight && d.style.background);
  root.style.minHeight = '0px';
  const rows = [...document.querySelectorAll('div')].filter(d => (d.getAttribute('style')||'').includes('padding-top: 26px')).map(e => { const r = e.getBoundingClientRect(); return { top: Math.round(r.top + scrollY), h: Math.round(r.height) }; });
  const spills = [...root.querySelectorAll('*')].filter(e => e.childElementCount===0 && e.textContent.trim() && e.getBoundingClientRect().right > root.getBoundingClientRect().right - 31).length;
  return { h: Math.ceil(root.getBoundingClientRect().height), unresolved: document.querySelectorAll('dc-import:not([data-dc-mounted])').length, spills, rows };
});
console.log(JSON.stringify(info));
let i = 1; for (const r of info.rows) { await p.screenshot({ path: `shots/c1v2-${i++}.png`, clip: { x: 0, y: r.top, width: 1980, height: r.h + 10 }, fullPage: true }); }
await b.close();
