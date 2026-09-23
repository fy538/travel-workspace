import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const [board, needle, out, w] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: +w, height: 1400 } });
await p.goto('http://127.0.0.1:8766/' + encodeURIComponent(board) + '.dc.html', { waitUntil: 'networkidle' }); await p.waitForTimeout(3000);
const y = await p.evaluate((n) => { const el = [...document.querySelectorAll('body *')].find(e => e.childElementCount === 0 && e.textContent.includes(n)); return el ? el.getBoundingClientRect().top + scrollY : -1; }, needle);
await p.screenshot({ path: out, fullPage: true, clip: { x: 0, y: Math.max(0, y - 120), width: Math.min(+w, 1400), height: 420 } });
console.log('y', y); await b.close();
