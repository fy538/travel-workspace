// Life · shared-package adoption checks (vdl-stage1 0.3).
// Serves ROOT over HTTP (components only mount over http, not file://). ROOT holds before/ and after/,
// each a full project copy (boards, support.js, and for after/ the package files).
// Writes PNGs to ROOT/_cmp and prints a JSON report.
//   node verify_vdl.mjs ROOT PORT
import { chromium } from '/Users/feihuyan/travel-workspace/travel-app/node_modules/playwright-core/index.mjs';
import fs from 'fs';
import path from 'path';

const ROOT = process.argv[2];
const BASE = `http://127.0.0.1:${process.argv[3] || 8771}/`;
const CMP = path.join(ROOT, '_cmp');
fs.mkdirSync(CMP, { recursive: true });
const url = (side, f) => BASE + side + '/' + encodeURIComponent(f);
const BOARDS = fs.readdirSync(path.join(ROOT, 'after')).filter((f) => f.endsWith('.dc.html') && /^(0|P|R)/.test(f)).sort();

// matched regions: [id, board prefix, text that identifies the frame column]
const CROPS = [
  ['04-object-flight', '04', 'The object page'],
  ['04-wave-tear', '04', 'Two more signatures'],
  ['04-pass-list', '04', 'Passes & tickets'],
  ['05.6-note-result', '05', 'A cue that belongs to a note'],
  ['05.9-ferry', '05', 'Asked: the Sorrento'],
  ['03b-ferry', '03b', 'The ferry'],
  ['R0-pass', 'R0', 'The pass at full size'],
  ['P3.5-offline', 'P3', 'The same page · disconnected return'],
  ['06.6-with', '06', 'Saturday, with it'],
  ['06.7-without', '06', 'The same question, without it'],
  ['03-doors', '03', 'Shared with Maya'],
  ['05-facets', '05', 'The cue, and what it found'],
];

const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const report = { boards: {}, crops: [], overflow: {}, narrow: [], errors: [] };

async function open(u, w = 1800) {
  const page = await browser.newPage({ viewport: { width: w, height: 1200 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => report.errors.push(u + ' :: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|404 \(File not found\)/.test(m.text())) report.errors.push(u + ' :: ' + m.text()); });
  await page.goto(u, { waitUntil: 'networkidle' });
  await page.waitForTimeout(3500);
  return page;
}

// the frame column (.cpanel) whose caption contains the label
async function markPanel(page, label, tag) {
  return page.evaluate(([label, tag]) => {
    const norm = (s) => (s || '').replace(/\s+/g, ' ').trim();
    const panels = [...document.querySelectorAll('.cpanel')];
    const hit = panels.find((p) => { const cap = p.querySelector('.ccap'); return cap && norm(cap.textContent).startsWith(label); })
      || panels.find((p) => norm(p.textContent).includes(label));
    if (!hit) return { ok: false };
    hit.setAttribute('data-cmp', tag);
    const r = hit.getBoundingClientRect();
    return { ok: true, w: Math.round(r.width), h: Math.round(r.height) };
  }, [label, tag]);
}

// every element (piercing open shadow roots) whose content spills sideways
async function overflow(page) {
  return page.evaluate(() => {
    const out = [];
    const walk = (root) => {
      for (const e of root.querySelectorAll('*')) {
        if (e.shadowRoot) walk(e.shadowRoot);
        const cs = getComputedStyle(e);
        if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') continue;
        if (e.clientWidth > 0 && e.scrollWidth > e.clientWidth + 1 && e.textContent.trim()) {
          const clip = cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis';
          out.push({ cls: String(e.className).slice(0, 40), w: e.clientWidth, sw: e.scrollWidth, clip, text: e.textContent.trim().replace(/\s+/g, ' ').slice(0, 48) });
        }
      }
    };
    walk(document);
    return out;
  });
}

// Two passes: read every element's own computed size first, then write size x k. Writing while
// walking would compound for elements that inherit their size (a nested chevron grew 25x).
async function scaleText(page, k) {
  await page.evaluate((k) => {
    const all = [];
    const walk = (root) => { for (const e of root.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot); all.push(e); } };
    walk(document);
    const snap = all.map((e) => { const cs = getComputedStyle(e); return [e, parseFloat(cs.fontSize), cs.lineHeight.endsWith('px') ? parseFloat(cs.lineHeight) : null]; });
    for (const [e, fs, lh] of snap) {
      e.style.fontSize = (fs * k) + 'px';
      if (lh !== null) e.style.lineHeight = (lh * k) + 'px';
    }
  }, k);
  await page.waitForTimeout(400);
}

const MOUNT = ['.tk', '.tr', '.or-ret', '.vdl-notice', '.vdl-door', 'dc-import'];
const X13 = ['04-object-flight', '05.6-note-result', '05.9-ferry', 'P3.5-offline', '04-pass-list'];
// The ticket's side notches are drawn 6px outside the card on purpose (the tear); not a spill.
const benign = (o) => o.sw - o.w <= 6 && /^(FERRY · ALILAURO|FLIGHT · DELTA 264)/.test(o.text);
const key = (o) => o.cls + '|' + o.text.slice(0, 30);
for (const side of ['before', 'after']) {
  for (const f of BOARDS) {
    const page = await open(url(side, f));
    const counts = {};
    for (const s of MOUNT) counts[s] = await page.locator(s).count();
    const size = await page.evaluate(() => ({ w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }));
    report.boards[f] = report.boards[f] || {};
    report.boards[f][side] = { ...counts, ...size };
    await page.screenshot({ path: path.join(CMP, `full-${side}-${f.split(' - ')[0]}.png`), fullPage: true });
    for (const [id, board, label] of CROPS) {
      if (!f.startsWith(board + ' ')) continue;
      const tag = side + '-' + id;
      const m = await markPanel(page, label, tag);
      if (!m.ok) { report.crops.push({ id, side, ok: false }); continue; }
      await page.locator(`[data-cmp="${tag}"]`).screenshot({ path: path.join(CMP, tag + '.png') });
      report.crops.push({ id, side, ok: true, w: m.w, h: m.h });
    }
    // the same measurement on both sides, so a spill is only "new" if the before did not have it
    const o1 = await overflow(page);
    await scaleText(page, 1.3);
    const o13 = await overflow(page);
    report.overflow[side + ':' + f] = { x1: o1, x13: o13 };
    for (const [id, board] of CROPS) {
      if (!f.startsWith(board + ' ') || !X13.includes(id)) continue;
      const loc = page.locator(`[data-cmp="${side}-${id}"]`);
      if (await loc.count()) await loc.screenshot({ path: path.join(CMP, `${side}-${id}-x13.png`) });
    }
    await page.close();
  }
}

// every shared instance Life uses, at 320px and at 1.3x text
const instances = [...new Set(BOARDS.flatMap((f) => (fs.readFileSync(path.join(ROOT, 'after', f), 'utf8').match(/<dc-import [^>]*><\/dc-import>/g) || [])))];
const harness = `<!DOCTYPE html><html><head><meta charset="utf-8" /><script src="./support.js"></script></head><body><x-dc><helmet>
<link rel="stylesheet" href="_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css" /><link rel="stylesheet" href="vdl.css" /></helmet>
<div style="width:320px;padding:0;background:#EFEAE0;display:flex;flex-direction:column;gap:14px">${instances.map((s, i) => `<div data-i="${i}">${s.replace(/hint-size="[^"]*"/, 'hint-size="320px,60px"')}</div>`).join('\n')}</div></x-dc></body></html>`;
fs.writeFileSync(path.join(ROOT, 'after', '_narrow.dc.html'), harness);
{
  const page = await open(url('after', '_narrow.dc.html'), 360);
  report.narrow.push({ scale: 1, instances: instances.length, spill: await overflow(page) });
  await page.screenshot({ path: path.join(CMP, 'narrow-320-x1.png'), fullPage: true });
  await scaleText(page, 1.3);
  report.narrow.push({ scale: 1.3, instances: instances.length, spill: await overflow(page) });
  await page.screenshot({ path: path.join(CMP, 'narrow-320-x13.png'), fullPage: true });
  await page.close();
}

await browser.close();
fs.writeFileSync(path.join(CMP, 'report.json'), JSON.stringify(report, null, 1));
const brief = {
  errors: report.errors,
  boards: Object.fromEntries(Object.entries(report.boards).map(([f, v]) => [f.split(' - ')[0], v])),
  crops: report.crops.filter((c) => !c.ok),
  // spills present after but not before, at the same scale; the ticket notch excluded as drawn
  overflowNew: Object.fromEntries(BOARDS.map((f) => {
    const a = report.overflow['after:' + f], b = report.overflow['before:' + f];
    const diff = (x) => { const had = new Set(b[x].map(key)); return a[x].filter((o) => !had.has(key(o)) && !benign(o)).map((o) => `${o.cls || '-'} ${o.w}->${o.sw}${o.clip ? ' (clipped)' : ''} «${o.text.slice(0, 34)}»`); };
    return [f.split(' - ')[0], { x1: diff('x1'), x13: diff('x13') }];
  })),
  narrow: report.narrow.map((n) => ({ scale: n.scale, instances: n.instances, spill: n.spill.filter((o) => !benign(o)).map((o) => `${o.cls || '-'} ${o.w}->${o.sw} «${o.text.slice(0, 30)}»`) })),
};
console.log(JSON.stringify(brief, null, 1));
