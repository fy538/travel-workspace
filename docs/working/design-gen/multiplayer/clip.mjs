import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const [url, out, w, y0, y1] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: +w, height: 1200 }, deviceScaleFactor: 1 });
await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(3500);
await p.screenshot({ path: out, clip: { x: 0, y: +y0, width: +w, height: +y1 - +y0 }, fullPage: true });
console.log(out); await b.close();
