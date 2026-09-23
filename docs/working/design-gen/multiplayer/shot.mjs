import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const [url, out, w] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: +w || 1500, height: 1400 }, deviceScaleFactor: 1 });
const errs = [];
p.on('pageerror', e => errs.push(e.message));
p.on('console', m => { if (m.type() === 'error' && !/favicon/.test(m.text())) errs.push(m.text()); });
await p.goto(url, { waitUntil: 'networkidle' });
await p.waitForTimeout(3500);
const info = await p.evaluate(() => {
  const root = document.querySelector('x-dc > div') || document.body;
  const r = root.getBoundingClientRect();
  const unresolved = document.querySelectorAll('dc-import:not([data-dc-mounted])').length;
  const probe = [...document.querySelectorAll('*')].filter(e => e.childElementCount === 0 && e.textContent.trim()).length;
  return { w: Math.round(r.width), h: Math.round(r.height), unresolved, leaves: probe,
           readers: document.querySelectorAll('.or-fh, .or-media, .or-words').length,
           notices: document.querySelectorAll('.vdl-notice').length };
});
await p.screenshot({ path: out, fullPage: true });
console.log(JSON.stringify({ ...info, errors: errs.slice(0, 5) }));
await b.close();
