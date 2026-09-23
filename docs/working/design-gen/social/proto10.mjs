import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const url = process.argv[2] || 'http://127.0.0.1:8766/' + encodeURIComponent('10P - Photo exchange, simulated') + '.dc.html';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 1040, height: 1500 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(4000);
const tap = async (label) => p.evaluate((label) => {
  const sec = document.querySelector('.frame.on'); const els = [...sec.querySelectorAll('[data-goto]')];
  const el = label === '@back' ? els.find(e => e.tagName.toLowerCase() === 'svg') : els.find(e => (e.textContent || '').replace(/\s+/g, ' ').trim().startsWith(label));
  if (!el) return 'NOT FOUND ' + label + ' in ' + sec.dataset.frame; el.dispatchEvent(new MouseEvent('click', { bubbles: true })); return document.querySelector('.frame.on').dataset.frame; }, label);
const sim = async (v) => p.evaluate((v) => { document.querySelector(`[data-sim="${v}"]`).click(); return v; }, v);
const start = async (k) => p.evaluate((k) => { document.querySelector(`[data-start="${k}"]`).click(); return document.querySelector('.frame.on').dataset.frame; }, k);
const log = [];
const run = async (steps) => { for (const s of steps) { await p.waitForTimeout(700); const r = s[0] === 'sim' ? await sim(s[1]) : s[0] === 'start' ? await start(s[1]) : await tap(s[1]); log.push(s.join(':') + ' -> ' + r); } };
await run([['start','l1'],['tap','PH-02'],['tap','@back'],['tap','Select'],['tap','Share 2'],['tap','Not now'],['tap','Share 2'],['sim','sent'],['tap','Send'],
  ['tap','Select'],['tap','Share 2'],['sim','failed'],['tap','Send'],['tap','Not now'],['tap','Share 2'],['tap','Send'],['tap','Try again'],
  ['tap','Select'],['tap','Share 2'],['sim','partial'],['tap','Send'],['tap','Send the late table'],
  ['tap','Select'],['tap','Share 2'],['sim','unknown'],['tap','Send'],['tap','Check again'],
  ['start','h1'],['tap','Open'],['tap','1 OF 2'],['tap','2 OF 2'],['tap','@back']]);
const notices = await p.evaluate(() => document.querySelectorAll('.vdl-notice').length);
await p.evaluate(() => window.P10.show('l4')); await p.waitForTimeout(300);
await p.screenshot({ path: 'out/shots/p-l4.png', fullPage: false });
console.log(log.join('\n')); console.log('notices mounted', notices, 'errors', JSON.stringify(errs));
await b.close();
