// 0.4.1 consumer update: matched original/after crops for 02.4, 02.5, 05 D7-A; element order; media loaded; narrow and 1.3x text.
// Serves from http://127.0.0.1:8766 (root = out/). PNGs to out/_cmp/, JSON report to stdout.
import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
import fs from 'fs';
import path from 'path';

const BASE = 'http://127.0.0.1:8766/';
const OUT = path.resolve('out');
const CMP = path.join(OUT, '_cmp');
fs.mkdirSync(CMP, { recursive: true });
const q = (s) => BASE + encodeURIComponent(s);
const BOARDS = { '02': ['02 - A little of your world', 1820], '05': ['05 - The important alternatives', 2260] };
const TARGETS = [['02.4', '02', '02.4'], ['02.5', '02', '02.5'], ['05-D7A', '05', 'A · A1 RECEIVED']];
const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const report = { crops: [], order: [], media: [], errors: [], harness: [] };

async function open(url, w) {
  const page = await browser.newPage({ viewport: { width: w, height: 3000 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => report.errors.push(url.slice(BASE.length) + ' :: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error') report.errors.push(url.slice(BASE.length) + ' :: ' + m.text()); });
  page.on('response', (r) => { if (r.status() >= 400) report.errors.push('HTTP ' + r.status() + ' ' + r.url().slice(BASE.length)); });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(3500);
  return page;
}
async function mark(page, label, tag) {
  return page.evaluate(([label, tag]) => {
    const leaves = [...document.querySelectorAll('body *')].filter((e) => e.childElementCount === 0 && (e.textContent.trim() === label || e.textContent.trim().startsWith(label)));
    for (const s of leaves) { let p = s; while (p && p !== document.body) { const r = p.getBoundingClientRect(); if (r.width >= 380 && r.width <= 400 && r.height > 500) { p.setAttribute('data-cmp', tag); return true; } p = p.parentElement; } }
    return false;
  }, [label, tag]);
}

for (const [side, prefix] of [['before', 'Before shared package - '], ['after', '']]) {
  const pages = {};
  for (const [key, [name, w]] of Object.entries(BOARDS)) pages[key] = await open(q(prefix + name + '.dc.html'), w);
  for (const [id, board, label] of TARGETS) {
    const page = pages[board], tag = side + '-' + id;
    if (!(await mark(page, label, tag))) { report.crops.push({ id, side, ok: false }); continue; }
    await page.locator(`[data-cmp="${tag}"]`).screenshot({ path: path.join(CMP, tag + '.png') });
    // order: her words, the reply field, "From the gallery", "Also about the Print Room", "Asks Vesper, not Maya"
    const o = await page.evaluate((tag) => {
      const col = document.querySelector(`[data-cmp="${tag}"]`);
      const y = (pred) => { const el = [...col.querySelectorAll('*')].find((e) => e.childElementCount === 0 && pred(e.textContent.trim())); return el ? Math.round(el.getBoundingClientRect().top) : null; };
      const seq = {
        words: y((t) => t.startsWith('The side room was my favorite')),
        reply: y((t) => t.startsWith('Reply to Maya') || t.startsWith('That side room. I want')),
        gallery: y((t) => t === 'From the gallery'),
        priya: y((t) => t === 'Also about the Print Room'),
        ask: y((t) => t.startsWith('Asks Vesper, not Maya')),
      };
      const vals = Object.values(seq);
      return { seq, inOrder: vals.every((v) => v !== null) && vals.every((v, i) => i === 0 || v > vals[i - 1]) };
    }, tag);
    report.order.push({ id, side, ...o });
    if (side === 'after') {
      const m = await page.evaluate((tag) => {
        const col = document.querySelector(`[data-cmp="${tag}"]`);
        const img = (sel) => { const i = col.querySelector(sel); return i ? { src: i.getAttribute('src'), loaded: i.complete && i.naturalWidth > 0 } : null; };
        return { media: img('.or-media > img'), thumb: img('.or-thumb > img'), asks: col.querySelectorAll('.or-askn').length };
      }, tag);
      report.media.push({ id, ...m });
    }
  }
  for (const p of Object.values(pages)) await p.close();
}

const comp = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1 });
for (const [id] of TARGETS) {
  const b = `_cmp/before-${id}.png`, a = `_cmp/after-${id}.png`;
  if (!fs.existsSync(path.join(OUT, b)) || !fs.existsSync(path.join(OUT, a))) continue;
  await comp.setContent(`<html><body style="margin:0;background:#F3EEE3;font:600 12px -apple-system,sans-serif;color:#6E6862">
    <div id="w" style="display:flex;gap:28px;padding:18px 20px;align-items:flex-start">
      <div><div style="margin:0 0 8px">ORIGINAL · ${id} · the selected design before the shared package</div><img src="${BASE + b}" style="width:393px;display:block"></div>
      <div><div style="margin:0 0 8px;color:#8A6628">AFTER · ${id} · shared package vdl-stage1 0.4.1</div><img src="${BASE + a}" style="width:393px;display:block"></div>
    </div></body></html>`);
  await comp.waitForTimeout(700);
  await comp.locator('#w').screenshot({ path: path.join(CMP, `pair-${id}.png`) });
}
await comp.close();

const R = (extra) => `<dc-import name="OriginalReader" density="full" author="Maya" ask="Ask about the Print Room" ${extra}></dc-import>`;
const FULL = 'audience="Thursday · to friends" media="ILLUSTRATION · NOT HER PHOTOGRAPH" mediaSrc="media/print-room-illustration.svg" thumbSrc="media/print-room-thumb.svg" words="The side room was my favorite. Go on a weekday, it was empty." place="The Harbor Print Room" placeDetail="Red Hook · Tue–Sun 11–6 · *Rooms Remade* through Sunday" placeMeta="Listed hours, not checked today"';
const INST = {
  'reader, show reader (02.4)': R(`show="reader" ${FULL} hint-size="349px,580px"`),
  'reader, compose, show reader (02.5)': R(`show="reader" ${FULL} compose="That side room. I want to see it before Sunday." hint-size="349px,640px"`),
  'private Ask, show ask': R('show="ask" hint-size="349px,48px"'),
};
const cells = []; let n = 0;
for (const [label, html] of Object.entries(INST)) for (const w of [393, 320]) cells.push(`<div class="cell" data-label="${label} · ${w}px" style="width:${w}px;box-sizing:border-box;padding:0 16px;background:#EFEAE0;margin:0 0 24px">${html}</div>`);
fs.writeFileSync(path.join(OUT, '_harness.dc.html'), `<!doctype html><html><head><meta charset="utf-8"><script src="./support.js"></script></head><body><x-dc><helmet>
<link rel="stylesheet" href="_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css"><link rel="stylesheet" href="vdl.css"><style>body{margin:0;background:#F3EEE3}</style></helmet>
<div style="padding:20px">${cells.join('')}</div></x-dc></body></html>`);
for (const scale of [1, 1.3]) {
  const page = await open(q('_harness.dc.html'), 900);
  const res = await page.evaluate((scale) => {
    const cellsEl = [...document.querySelectorAll('.cell')];
    if (scale !== 1) {
      const plan = cellsEl.flatMap((c) => [...c.querySelectorAll('*')]).map((el) => { const cs = getComputedStyle(el); return [el, parseFloat(cs.fontSize), cs.lineHeight === 'normal' ? null : parseFloat(cs.lineHeight)]; });
      for (const [el, fs, lh] of plan) { el.style.fontSize = (fs * scale) + 'px'; if (lh) el.style.lineHeight = (lh * scale) + 'px'; }
    }
    return cellsEl.map((c) => {
      const cr = c.getBoundingClientRect(); const spills = [], clips = [];
      for (const el of c.querySelectorAll('*')) {
        const r = el.getBoundingClientRect(); if (!r.width) continue;
        const txt = (el.childElementCount === 0 ? el.textContent.trim() : '').slice(0, 40);
        if (txt && r.right > cr.right + 1) spills.push(txt);
        const cs = getComputedStyle(el);
        if (txt && (cs.overflow === 'hidden' || cs.overflowX === 'hidden' || cs.textOverflow === 'ellipsis') && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 2)) clips.push(txt);
      }
      return { cell: c.dataset.label, height: Math.round(cr.height), spills, clips };
    });
  }, scale);
  await page.screenshot({ path: path.join(CMP, `harness041-x${scale}.png`), fullPage: true });
  report.harness.push({ scale, cells: res });
  await page.close();
}
await browser.close();
console.log(JSON.stringify(report, null, 1));
