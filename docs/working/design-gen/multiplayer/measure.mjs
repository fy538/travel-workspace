import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
import fs from 'fs';
const B = process.argv[2], T = process.argv[3];
const FILES = JSON.parse(fs.readFileSync(process.env.PATHS || 'paths.json', 'utf8'));
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const out = {}, report = [];
for (const [key, name] of Object.entries(FILES)) {
  const p = await b.newPage({ viewport: { width: 2000, height: 1200 }, deviceScaleFactor: 1 });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error' && !/favicon|404/.test(m.text())) errs.push(m.text()); });
  await p.goto(`${B}/${name.split('/').map(encodeURIComponent).join('/')}.dc.html${T}`, { waitUntil: 'networkidle' });
  await p.waitForTimeout(3200);
  const r = await p.evaluate(() => {
    const root = [...document.querySelectorAll('div')].find(d => d.style.minHeight);
    root.style.minHeight = '0px';
    const rect = root.getBoundingClientRect();
    // overflow: any element whose right edge exceeds the board's padded content box
    const cb = rect.right - 32;
    const spills = [...root.querySelectorAll('*')].filter(e => {
      const q = e.getBoundingClientRect();
      return q.width > 0 && q.right > cb + 1 && e.childElementCount === 0 && e.textContent.trim();
    }).map(e => e.textContent.trim().slice(0, 34));
    return { w: Math.round(rect.width), h: Math.ceil(rect.height),
             unresolved: document.querySelectorAll('dc-import:not([data-dc-mounted])').length,
             spills: [...new Set(spills)].slice(0, 6) };
  });
  out[key] = r.h + 30;
  report.push({ key, ...r, errors: errs.slice(0, 3) });
  await p.close();
}
fs.writeFileSync('out/heights.json', JSON.stringify(out, null, 1));
console.log(JSON.stringify(report, null, 1));
await b.close();
