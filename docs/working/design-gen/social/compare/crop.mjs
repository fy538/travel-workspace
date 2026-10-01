import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
import fs from 'fs';
const spec = JSON.parse(fs.readFileSync('crops.json', 'utf8')).filter(s => !process.argv[2] || process.argv.slice(2).includes(s[0]));
const PORT = { S: 8773, M: 8772 };
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const pages = {}; const log = [];
for (const [id, side, board, needle, at, pre, H] of spec) {
  const key = side + board;
  if (!pages[key]) { const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 2 });
    await p.goto(`http://127.0.0.1:${PORT[side]}/` + encodeURIComponent(board) + '.dc.html', { waitUntil: 'networkidle' }); await p.waitForTimeout(3000); pages[key] = p; }
  const p = pages[key];
  const r = await p.evaluate(([needle, at, pre, H]) => {
    const phones = [...document.querySelectorAll('div')].filter(d => /width:\s*393px/.test(d.getAttribute('style') || '') && d.getBoundingClientRect().height > 300);
    let top = phones.filter(d => !phones.some(o => o !== d && o.contains(d)));
    let hits = top.filter(ph => ph.innerText.includes(needle)).map(ph => { let cur = ph; for (;;) { const inner = [...cur.querySelectorAll('div')].find(d => d !== cur && /width:\s*393px/.test(d.getAttribute('style') || '') && d.getBoundingClientRect().height > 300 && d.innerText.includes(needle)); if (!inner) return cur; cur = inner; } });
    if (!hits.length) return { err: 'no phone with ' + needle, n: top.length };
    const ph = hits[0]; const pr = ph.getBoundingClientRect(); let y0 = pr.top + scrollY;
    if (at) { const leaf = [...ph.querySelectorAll('*')].find(e => e.childElementCount === 0 && (e.textContent || '').trim().startsWith(at)) || [...ph.querySelectorAll('*')].reverse().find(e => (e.innerText || '').trim().startsWith(at));
      if (!leaf) return { err: 'no anchor ' + at }; y0 = Math.max(y0, leaf.getBoundingClientRect().top + scrollY - pre); }
    const y1 = Math.min(pr.bottom + scrollY, y0 + H);
    return { x: pr.left + scrollX, y: y0, w: pr.width, h: y1 - y0, hits: hits.length };
  }, [needle, at, pre, H]);
  if (r.err) { log.push(id + ' ERR ' + r.err); continue; }
  await p.screenshot({ path: `crops/${id}.jpg`, type: 'jpeg', quality: 86, fullPage: true, clip: { x: r.x, y: r.y, width: r.w, height: r.h } });
  log.push(`${id} ok ${Math.round(r.h)}px hits=${r.hits}`);
}
console.log(log.join('\n')); await b.close();
