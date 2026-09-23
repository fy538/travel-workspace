import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const [url, out, w] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: +w, height: 1200 }, deviceScaleFactor: 1 });
await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(3500);
// crop to the phones row only: from the top of the board to the notes divider
const y = await p.evaluate(() => { const d = [...document.querySelectorAll('div')].find(e => (e.getAttribute('style')||'').includes('border-top: 1px solid rgba(27,23,20,0.12)')); return d ? Math.round(d.getBoundingClientRect().top + scrollY) : 1400; });
await p.screenshot({ path: out, clip: { x: 0, y: 150, width: +w, height: y - 150 }, fullPage: true });
console.log(out, y); await b.close();
