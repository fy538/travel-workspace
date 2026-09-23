// Overflow and larger-text checks for the two new canvases (no before side exists for them).
import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
const SP = process.argv[2];
const overflow = (p) => p.evaluate(() => {
  const out = [];
  const walk = (root) => { for (const e of root.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot);
    const cs = getComputedStyle(e);
    if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') continue;
    if (e.clientWidth > 0 && e.scrollWidth > e.clientWidth + 1 && e.textContent.trim())
      out.push({ cls: String(e.className).slice(0, 26), w: e.clientWidth, sw: e.scrollWidth,
                 clip: cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis', text: e.textContent.trim().replace(/\s+/g, ' ').slice(0, 40) }); } };
  walk(document); return out;
});
const scale = async (p, k) => { await p.evaluate((k) => {
  const all = []; const walk = (r) => { for (const e of r.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot); all.push(e); } };
  walk(document);
  const snap = all.map((e) => { const cs = getComputedStyle(e); return [e, parseFloat(cs.fontSize), cs.lineHeight.endsWith('px') ? parseFloat(cs.lineHeight) : null]; });
  for (const [e, fs, lh] of snap) { e.style.fontSize = (fs * k) + 'px'; if (lh !== null) e.style.lineHeight = (lh * k) + 'px'; }
}, k); await p.waitForTimeout(400); };
const benign = (o) => o.sw - o.w <= 6 && /^(FERRY · ALILAURO|FLIGHT · DELTA 264)/.test(o.text);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const f of ['08 - The actual source.dc.html', '09 - Finishing a local action.dc.html']) {
  const p = await b.newPage({ viewport: { width: 1800, height: 1200 } });
  await p.goto('http://127.0.0.1:8771/after/' + encodeURIComponent(f), { waitUntil: 'networkidle' });
  await p.waitForTimeout(3500);
  const o1 = (await overflow(p)).filter((o) => !benign(o));
  await scale(p, 1.3);
  const o13 = (await overflow(p)).filter((o) => !benign(o));
  await p.screenshot({ path: `${SP}/_cmp/new-${f.slice(0, 2)}-x13.png`, fullPage: true });
  console.log(f.slice(0, 2), 'x1', JSON.stringify(o1.map((o) => `${o.cls || '-'} ${o.w}->${o.sw}${o.clip ? ' clip' : ''} «${o.text}»`)),
              '\n   x1.3', JSON.stringify(o13.map((o) => `${o.cls || '-'} ${o.w}->${o.sw}${o.clip ? ' clip' : ''} «${o.text}»`)));
  await p.close();
}
await b.close();
