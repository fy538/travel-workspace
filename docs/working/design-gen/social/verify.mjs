// Matched before/after crops and narrow / larger-text checks for the shared-package adoption.
// Serves from http://127.0.0.1:8766 (root = out/). Writes PNGs to out/_cmp/ and a JSON report to stdout.
import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
import fs from 'fs';
import path from 'path';

const BASE = 'http://127.0.0.1:8766/';
const OUT = path.resolve('out');
const CMP = path.join(OUT, '_cmp');
fs.mkdirSync(CMP, { recursive: true });
const q = (s) => BASE + encodeURIComponent(s);
const H = JSON.parse(fs.readFileSync(path.join(OUT, 'heights.json'), 'utf8'));
const HB = JSON.parse(fs.readFileSync(path.resolve('before/heights.json'), 'utf8'));

const BOARDS = { '02': ['02 - A little of your world', 1820], '03': ['03 - An easier way to get together', 2260], '05': ['05 - The important alternatives', 2260] };
const TARGETS = [
  ['02.2', '02', '02.2'], ['02.4', '02', '02.4'], ['02.5', '02', '02.5'],
  ['03.1', '03', '03.1'], ['03.2', '03', '03.2'], ['05-D7A', '05', 'A · A1 RECEIVED'],
];

const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const report = { crops: [], errors: [], harness: [] };

async function open(url, w, h) {
  const page = await browser.newPage({ viewport: { width: w, height: Math.min(h, 4000) }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => report.errors.push(url + ' :: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon/.test(m.text())) report.errors.push(url + ' :: ' + m.text()); });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(3500);
  return page;
}

async function mark(page, label, tag) {
  return page.evaluate(([label, tag]) => {
    const leaves = [...document.querySelectorAll('body *')].filter((e) => e.childElementCount === 0 && (e.textContent.trim() === label || e.textContent.trim().startsWith(label)));
    for (const s of leaves) {
      let p = s;
      while (p && p !== document.body) {
        const r = p.getBoundingClientRect();
        if (r.width >= 380 && r.width <= 400 && r.height > 500) { p.setAttribute('data-cmp', tag); return { ok: true, h: Math.round(r.height) }; }
        p = p.parentElement;
      }
    }
    return { ok: false };
  }, [label, tag]);
}

for (const [side, prefix, heights] of [['before', 'Before shared package - ', HB], ['after', '', H]]) {
  const pages = {};
  for (const [key, [name, w]] of Object.entries(BOARDS)) pages[key] = await open(q(prefix + name + '.dc.html'), w, heights[key]);
  for (const [id, board, label] of TARGETS) {
    const page = pages[board]; const tag = side + '-' + id;
    const m = await mark(page, label, tag);
    if (!m.ok) { report.crops.push({ id, side, ok: false }); continue; }
    const file = path.join(CMP, tag + '.png');
    await page.locator(`[data-cmp="${tag}"]`).screenshot({ path: file });
    const mounted = await page.locator(`[data-cmp="${tag}"] .or-fh, [data-cmp="${tag}"] .ic-host, [data-cmp="${tag}"] .ic-row, [data-cmp="${tag}"] .vdl-notice`).count();
    report.crops.push({ id, side, ok: true, height: m.h, sharedNodes: mounted });
  }
  for (const p of Object.values(pages)) await p.close();
}

// Side-by-side composites: before | after, same content and width.
const comp = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1 });
for (const [id] of TARGETS) {
  const b = `_cmp/before-${id}.png`, a = `_cmp/after-${id}.png`;
  if (!fs.existsSync(path.join(OUT, b)) || !fs.existsSync(path.join(OUT, a))) continue;
  await comp.goto(BASE + '_cmp/blank.html').catch(() => {});
  await comp.setContent(`<html><body style="margin:0;background:#F3EEE3;font:600 12px -apple-system,sans-serif;color:#6E6862">
    <div id="w" style="display:flex;gap:28px;padding:18px 20px;align-items:flex-start">
      <div><div style="margin:0 0 8px">BEFORE · ${id} · as drawn</div><img src="${BASE + b}" style="width:393px;display:block"></div>
      <div><div style="margin:0 0 8px;color:#8A6628">AFTER · ${id} · shared package vdl-stage1 0.3</div><img src="${BASE + a}" style="width:393px;display:block"></div>
    </div></body></html>`);
  await comp.waitForTimeout(600);
  await comp.locator('#w').screenshot({ path: path.join(CMP, `pair-${id}.png`) });
}
await comp.close();

// Narrow and larger-text harness: each adopted instance at 393 and 320, at 1.0 and 1.3× text.
const INST = {
  'OriginalReader full (02.4)': `<dc-import name="OriginalReader" density="full" author="Maya" audience="Thursday · to friends" media="ILLUSTRATION · NOT HER PHOTOGRAPH" words="The side room was my favorite. Go on a weekday, it was empty." place="The Harbor Print Room" placeDetail="Red Hook · Tue–Sun 11–6 · *Rooms Remade* through Sunday" placeMeta="Listed hours, not checked today" ask="Ask about the Print Room" hint-size="349px,700px"></dc-import>`,
  'OriginalReader full, compose (02.5)': `<dc-import name="OriginalReader" density="full" author="Maya" audience="Thursday · to friends" words="The side room was my favorite. Go on a weekday, it was empty." compose="That side room. I want to see it before Sunday." ask="Ask about the Print Room" hint-size="349px,420px"></dc-import>`,
  'InviteCard host, Sam (03.1)': `<dc-import name="InviteCard" view="host" kicker="TO SAM · DINNER ONLY · A LINK, NO APP" title="Pasta trial night at Nora’s" lines="WHEN=Saturday, dinner from seven|come at seven-thirty;WHERE=Carroll Gardens|the exact address after he confirms this number;WITH=Nora and Maya;BRING=Nothing" via="BY TEXT · TO THE NUMBER YOU TYPED" stamp="HE SEES WHEN, WHERE, WHO · NOTHING ELSE OF YOURS · NO CONTACTS SCANNED" hint-size="349px,270px"></dc-import>`,
  'InviteCard guest (03.2)': `<dc-import name="InviteCard" view="guest" shape="pill" kicker="FROM NORA · A LINK · NOTHING TO INSTALL" title="Pasta trial night. Saturday from seven; come at seven-thirty." note="“Second attempt at the Sorrento thing. Maya’s coming. Bring nothing, honestly.”" noteBy="NORA, THURSDAY" lines="Saturday Sep 19 · dinner from seven|you’re expected around seven-thirty;Carroll Gardens, near Court Street|the exact address after a one-time code to this number;With Nora and Maya|" from="Nora" guestNote="Nora sees your answer as yours once you confirm this number, the same step that unlocks the address. No reason needed either way." answer="I’ll need to leave by nine" stamp="ANYTHING SHE SHOULD KNOW · OPTIONAL · GOES TO NORA ONLY" hint-size="349px,640px"></dc-import>`,
  'Notice failed (02.5 result)': `<dc-import name="Notice" tone="failed" title="Didn’t reach Maya" body="Your reply is still in the field." primary="Try again" secondary="Not now" hint-size="349px,120px"></dc-import>`,
};
const cells = [];
let n = 0;
for (const [label, html] of Object.entries(INST)) for (const w of [393, 320]) cells.push(`<div class="cell" data-i="${n++}" data-label="${label} · ${w}px" style="width:${w}px;box-sizing:border-box;padding:0 16px;background:#EFEAE0;margin:0 0 24px">${html}</div>`);
fs.writeFileSync(path.join(OUT, '_harness.dc.html'), `<!doctype html><html><head><meta charset="utf-8"><script src="./support.js"></script></head><body><x-dc><helmet>
<link rel="stylesheet" href="_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css"><link rel="stylesheet" href="vdl.css"><style>body{margin:0;background:#F3EEE3}</style></helmet>
<div style="padding:20px">${cells.join('')}</div></x-dc></body></html>`);

for (const scale of [1, 1.3]) {
  const page = await open(q('_harness.dc.html'), 900, 4000);
  const res = await page.evaluate((scale) => {
    const out = [];
    const cellsEl = [...document.querySelectorAll('.cell')];
    if (scale !== 1) {
      const all = cellsEl.flatMap((c) => [...c.querySelectorAll('*')]);
      const plan = all.map((el) => { const cs = getComputedStyle(el); return [el, parseFloat(cs.fontSize), cs.lineHeight === 'normal' ? null : parseFloat(cs.lineHeight)]; });
      for (const [el, fs, lh] of plan) { el.style.fontSize = (fs * scale) + 'px'; if (lh) el.style.lineHeight = (lh * scale) + 'px'; }
    }
    for (const c of cellsEl) {
      const cr = c.getBoundingClientRect();
      const spills = [], clips = [];
      for (const el of c.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (!r.width) continue;
        const txt = (el.childElementCount === 0 ? el.textContent.trim() : '').slice(0, 40);
        if (r.right > cr.right + 1 && txt) spills.push(txt);
        const cs = getComputedStyle(el);
        if (txt && (cs.overflow === 'hidden' || cs.overflowX === 'hidden' || cs.textOverflow === 'ellipsis') && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 2)) clips.push(txt);
      }
      out.push({ cell: c.dataset.label, height: Math.round(cr.height), mounted: c.querySelector('dc-import') === null || c.querySelectorAll('div,span').length > 3, spills, clips });
    }
    return out;
  }, scale);
  await page.screenshot({ path: path.join(CMP, `harness-x${scale}.png`), fullPage: true });
  report.harness.push({ scale, cells: res });
  await page.close();
}

await browser.close();
console.log(JSON.stringify(report, null, 1));
