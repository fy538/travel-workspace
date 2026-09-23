// Composes matched before/after crops from verify_vdl.mjs into three review sheets.
//   node sheet_vdl.mjs ROOT PORT      (ROOT served over HTTP; crops in ROOT/_cmp)
import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
import fs from 'fs';
import path from 'path';

const ROOT = process.argv[2];
const BASE = `http://127.0.0.1:${process.argv[3] || 8771}/`;
const SHEETS = {
  'sheet-1-tickets': {
    title: 'Tickets on the shared Ticket',
    sub: 'Same content, same width. 05.9 is a repair: its ticket styles lived on board 04, so every line had fallen back to plain sans.',
    pairs: [['05.9-ferry', '05.9 · the ferry, retrieved'], ['04-object-flight', '04 · the object page (flight)'], ['R0-pass', 'R0 · the pass at full size']],
  },
  'sheet-2-reader-notice-doors': {
    title: 'Reader, notice, doors and facets',
    sub: 'OriginalReader retrieval on 05.6, Notice on P3.5, the shared Door construction on 03, facet labels at 10px on 05.',
    pairs: [['05.6-note-result', '05.6 · a cue that belongs to a note'], ['P3.5-offline', 'P3.5 · the disconnected return'], ['03-doors', '03 · the shared record (doors; clipped caption fixed)'], ['05-facets', '05 · facets 8.5px → 10px']],
  },
  'sheet-3-local-and-06': {
    title: 'Kept local, corrected in place · and 06.6/06.7',
    sub: '04’s pass list stays local (two missing Ticket row variants); stubs rise to 10px, the overrunning title ends in an ellipsis, the reserved violet leaves the admission stub. 06.6/06.7 per the September 10 additive review.',
    pairs: [['04-pass-list', '04 · passes & tickets'], ['06.6-with', '06.6 · with her line'], ['06.7-without', '06.7 · without it']],
  },
};

const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [name, s] of Object.entries(SHEETS)) {
  const cells = s.pairs.map(([id, label]) => `
    <div class="pair"><div class="lab">${label}</div>
      <div class="row"><figure><figcaption>BEFORE</figcaption><img src="/_cmp/before-${id}.png"></figure>
      <figure><figcaption>AFTER · vdl-stage1 0.3</figcaption><img src="/_cmp/after-${id}.png"></figure></div></div>`).join('');
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    body{margin:0;background:#EFEAE0;font-family:-apple-system,system-ui,sans-serif;color:#1B1714;padding:36px 40px}
    h1{font-family:"EB Garamond",Georgia,serif;font-weight:600;font-size:30px;margin:0 0 6px}
    p.sub{margin:0 0 26px;color:#6E6862;font-size:14px;max-width:980px;line-height:20px}
    .grid{display:flex;flex-wrap:wrap;gap:34px;align-items:flex-start}
    .pair{background:#F3EEE3;border:1px solid rgba(27,23,20,.10);border-radius:14px;padding:16px}
    .lab{font:700 11px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:1.2px;text-transform:uppercase;color:#8A6628;margin-bottom:12px}
    .row{display:flex;gap:18px;align-items:flex-start}
    figure{margin:0}
    figcaption{font:600 10px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:1.2px;color:#6E6862;margin-bottom:8px}
    img{display:block;width:393px;height:auto;border-radius:6px}
  </style></head><body><h1>${s.title}</h1><p class="sub">${s.sub}</p><div class="grid">${cells}</div></body></html>`;
  fs.writeFileSync(path.join(ROOT, `_${name}.html`), page);
  const p = await browser.newPage({ viewport: { width: 1780, height: 1000 }, deviceScaleFactor: 1 });
  await p.goto(BASE + `_${name}.html`, { waitUntil: 'networkidle' });
  await p.waitForTimeout(600);
  const out = path.join(ROOT, '_cmp', `${name}.png`);
  await p.screenshot({ path: out, fullPage: true });
  console.log(out);
  await p.close();
}
await browser.close();
