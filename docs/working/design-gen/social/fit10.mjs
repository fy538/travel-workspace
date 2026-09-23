import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const scale of [1, 1.3]) {
  const p = await b.newPage({ viewport: { width: 2260, height: 1400 } });
  await p.goto('http://127.0.0.1:8766/' + encodeURIComponent(process.argv[2]) + '.dc.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  const r = await p.evaluate((scale) => {
    const phones = [...document.querySelectorAll('div[style*="width: 393px; min-height"]')];
    const outer = phones.filter(d => !phones.some(o => o !== d && o.contains(d)));
    if (scale !== 1) { const plan = outer.flatMap(c => [...c.querySelectorAll('*')]).map(el => { const cs = getComputedStyle(el); return [el, parseFloat(cs.fontSize), cs.lineHeight === 'normal' ? null : parseFloat(cs.lineHeight)]; }); for (const [el, fs, lh] of plan) { el.style.fontSize = fs * scale + 'px'; if (lh) el.style.lineHeight = lh * scale + 'px'; } }
    const spills = [], clips = [];
    for (const c of outer) { const cr = c.getBoundingClientRect(); for (const el of c.querySelectorAll('*')) { const r = el.getBoundingClientRect(); if (!r.width) continue; const t = el.childElementCount === 0 ? el.textContent.trim().slice(0, 40) : ''; if (t && r.right > cr.right + 1) spills.push(t); const cs = getComputedStyle(el); if (t && (cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis') && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 2)) clips.push(t); } }
    return { phones: outer.length, spills, clips };
  }, scale);
  console.log('scale', scale, JSON.stringify(r));
  await p.close();
}
await b.close();
