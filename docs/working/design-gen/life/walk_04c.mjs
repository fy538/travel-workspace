// Click through 04c and assert every landing frame and every piece of state it claims to keep.
//   node walk_04c.mjs SCRATCH [PORT]        LIVE_URL=<serve_url> node walk_04c.mjs SCRATCH
import { chromium } from '/Users/feihuyan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs';
const SP = process.argv[2], PORT = process.argv[3] || '8772';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 1200, height: 1100 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
const URL0 = process.env.LIVE_URL || `http://127.0.0.1:${PORT}/after/` + encodeURIComponent('04c - One photo path.dc.html');
await p.goto(URL0 + '#a1', { waitUntil: 'networkidle' }); await p.waitForTimeout(4000);
const log = []; let n = 0;
const ok = (what, cond, got) => log.push({ what, ok: !!cond, got });
const at = () => p.evaluate(() => { const f = document.querySelector('.frame.on'); return f && f.getAttribute('data-frame'); });
const sel = () => p.evaluate(() => [...document.querySelectorAll('.frame.on .pp-tile.pp-on')].map(e => e.getAttribute('data-pid')).sort().join(','));
const prev = () => p.evaluate(() => [...document.querySelectorAll('.frame.on [data-prev]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.getAttribute('data-prev')).join(','));
const bind = (k) => p.evaluate((k) => { const e = document.querySelector('.frame.on [data-bind="' + k + '"]'); return e && e.textContent; }, k);
const draft = () => p.evaluate(() => { const e = document.querySelector('.frame.on [data-draft]'); return e ? e.value : null; });
const shown = (t) => p.evaluate((t) => [...document.querySelectorAll('.frame.on *')].some(e => e.children.length === 0 && e.textContent.trim() === t && getComputedStyle(e).display !== 'none' && e.offsetParent !== null), t);
const staticChecks = () => p.evaluate(() => [...document.querySelectorAll('.frame.on span')].filter(e => { const c = getComputedStyle(e); return c.position === 'absolute' && c.width === '18px' && c.borderRadius === '9px' && e.offsetParent !== null; }).length);
async function expect(want, what) {
  await p.waitForTimeout(300); const got = await at();
  try { await p.locator('.frame.on').screenshot({ path: `${SP}/_cmp/walk-${String(++n).padStart(2, '0')}-${got}.png`, timeout: 5000 }); } catch (e) {}
  ok(what, got === want, got);
}
const tap = async (sel_) => { try { await p.locator('.frame.on ' + sel_).first().click({ timeout: 3000 }); } catch (e) { ok('tap ' + sel_ + ' on ' + (await at()), false, 'not found'); } };
const tile = (pid) => tap(`.pp-tile[data-pid="${pid}"]`);
const outcome = (o) => p.locator(`[data-outcome="${o}"]`).click();

await expect('a1', 'open the record');
await tap('[data-go="a2"]'); await expect('a2', 'See all 5');
await tap('svg[aria-label="PH-01"][data-go="a3"]'); await expect('a3', 'Maya’s picture, whole');
await tap('svg[aria-label="PH-04"][data-go="a4"]'); await expect('a4', 'strip → the late table');
await tap('[data-go="a2"]'); await expect('a2', 'Back → all five');
await tap('[data-go="a5"]'); await expect('a5', 'SELECT');
ok('starts with the ledger’s three', (await sel()) === 'PH-01,PH-02,PH-04', await sel());
// a non-default selection
await tile('PH-03'); await tile('PH-04');
ok('non-default selection: + the near-duplicate, − the late table', (await sel()) === 'PH-01,PH-02,PH-03', await sel());
ok('counts follow: 3 selected, Share 2', (await bind('nsel')) === '3' && (await bind('nown')) === '2', `${await bind('nsel')}/${await bind('nown')}`);
await tap('[data-go="a6"]'); await expect('a6', 'Share 2 → the preview');
ok('preview carries exactly the two chosen of hers', (await prev()) === 'PH-02,PH-03', await prev());
ok('preview title: 2 OF YOUR 3', (await bind('sharetitle')) === '2 OF YOUR 3', await bind('sharetitle'));
ok('Maya’s table explained locally', await shown('Maya’s table isn’t in this share. It stays with the dinner.'), '');
await p.locator('.frame.on [data-draft]').fill('the pan, before you came');
await tap('[data-go="a5"]'); await expect('a5', 'Not now → the selection');
ok('Not now kept the non-default selection', (await sel()) === 'PH-01,PH-02,PH-03', await sel());
await tap('[data-go="a6"]'); await expect('a6', 'Share again');
ok('the typed line survived Not now', (await draft()) === 'the pan, before you came', await draft());
await outcome('o_partial');
ok('part went is refused for a non-pair selection', (await p.evaluate(() => window.PP.outcome)) === 'o_sent', await p.evaluate(() => window.PP.outcome));
await outcome('o_failed'); await tap('[data-go="@send"]'); await expect('o_failed', 'Send → nothing went, still on the share');
ok('the line survived the failure', (await draft()) === 'the pan, before you came', await draft());
ok('the same two are still going', (await prev()) === 'PH-02,PH-03', await prev());
ok('failure words follow the count', (await bind('stillhere')) === 'Both photos and Maya are still here.', await bind('stillhere'));
await tap('[data-go="a5"]'); await expect('a5', 'Not now from the failure → the selection');
ok('selection kept after the failure', (await sel()) === 'PH-01,PH-02,PH-03', await sel());
await tap('[data-go="a6"]'); await tap('[data-go="@send"]'); await expect('o_failed', 'Send again → nothing went');
await tap('[data-go="o_sent"]'); await expect('o_sent', 'Try again → sent');
ok('sent count is the two that went', (await bind('sentn')) === '2 photos', await bind('sentn'));
await tap('[data-go="a5"]'); await expect('a5', 'SELECT after the send');
ok('a confirmed send cleared the selection', (await sel()) === '', await sel());
// the ledger's pair: part went, retry only the late table
await tile('PH-01'); await tile('PH-02'); await tile('PH-04');
await tap('[data-go="a6"]'); await outcome('o_partial'); await tap('[data-go="@send"]'); await expect('o_partial', 'the pair → part went');
ok('only the undelivered picture stays selected', (await staticChecks()) === 1 && (await shown('1 SELECTED')), await staticChecks());
await tap('[data-go="o_retry"]'); await expect('o_retry', 'Send the late table');
ok('retry names only the late table', await shown('Sent to Maya · the late table'), '');
// not known yet: a check, never a resend
await tap('[data-go="a5"]'); await tile('PH-02'); await tile('PH-04'); await tap('[data-go="a6"]');
await outcome('o_unknown'); await tap('[data-go="@send"]'); await expect('o_unknown', 'the pair → not known yet');
ok('no resend offered while not known', !(await shown('Share 1')), '');
await tap('[data-go="o_sent"]'); await expect('o_sent', 'Check again → sent');
// Done releases a pending-send selection
await tap('[data-go="a5"]'); await tile('PH-02'); await tile('PH-04'); await tap('[data-go="a6"]');
await outcome('o_partial'); await tap('[data-go="@send"]'); await expect('o_partial', 'part went again');
await tap('[data-go="@release"]'); await expect('a2', 'Done → back to all five');
await tap('[data-go="a5"]'); ok('Done released the pending selection', (await sel()) === '', await sel());
// Home path
await p.locator('[data-start="b1"]').click(); await expect('b1', 'Home, Last night');
await tap('svg[aria-label="PH-01"][data-go="b2"]'); await expect('b2', 'the same viewer, from Home');
const homeTab = await p.evaluate(() => { const f = document.querySelector('.frame.on'); const s = [...f.querySelectorAll('span')].find(x => x.textContent.trim() === 'Home'); return s && getComputedStyle(s).fontWeight; });
ok('Home tab stays active', homeTab === '600', homeTab);
await tap('[data-go="b1"]'); await expect('b1', 'Back → Home');
// larger text on the preview
await p.locator('[data-start="a1"]').click(); await tap('[data-go="a2"]'); await tap('[data-go="a5"]');
await tile('PH-02'); await tile('PH-04'); await tap('[data-go="a6"]'); await p.waitForTimeout(300);
await p.evaluate(() => { const all = [...document.querySelector('.frame.on').querySelectorAll('*')]; const snap = all.map(e => { const c = getComputedStyle(e); return [e, parseFloat(c.fontSize), c.lineHeight.endsWith('px') ? parseFloat(c.lineHeight) : null]; }); for (const [e, fs, lh] of snap) { e.style.fontSize = fs * 1.3 + 'px'; if (lh) e.style.lineHeight = lh * 1.3 + 'px'; } });
await p.waitForTimeout(300); try { await p.locator('.frame.on').screenshot({ path: `${SP}/_cmp/walk-a6-x13.png` }); } catch (e) {}
const spill = await p.evaluate(() => [...document.querySelector('.frame.on').querySelectorAll('*')].filter(e => e.clientWidth > 0 && e.scrollWidth > e.clientWidth + 2 && e.textContent.trim()).map(e => e.textContent.trim().slice(0, 30)));
ok('preview at 1.3× text: no spill', spill.length === 0, spill.slice(0, 4).join(' | '));
await b.close();
const fail = log.filter(l => !l.ok);
console.log(JSON.stringify({ errors: errs, pass: log.length - fail.length, of: log.length, fail }, null, 1));
console.log(log.map(l => `${l.ok ? 'ok  ' : 'FAIL'} ${l.what}${l.got !== '' && l.got !== undefined ? '  (' + l.got + ')' : ''}`).join('\n'));
