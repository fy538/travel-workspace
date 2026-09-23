import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [base, ...names] = process.argv.slice(2);
if (!base || names.length === 0) {
  console.error('Usage: DESIGN_TOKEN="?token=..." PLAYWRIGHT_CORE_MODULE=/path/to/playwright-core/index.mjs node over.mjs BASE_URL BOARD_NAME...');
  process.exit(2);
}

const modulePath = process.env.PLAYWRIGHT_CORE_MODULE || 'playwright-core';
const moduleUrl = path.isAbsolute(modulePath) ? pathToFileURL(modulePath).href : modulePath;
const { chromium } = await import(moduleUrl);
const outputDir = path.join(import.meta.dirname, 'out', 'shots');
fs.mkdirSync(outputDir, { recursive: true });

const browser = await chromium.launch({
  headless: true,
  executablePath: process.env.CHROME_EXECUTABLE || undefined,
});
try {
  for (const name of names) {
    const context = await browser.newContext({
      viewport: { width: 2100, height: 1200 },
      deviceScaleFactor: 0.32,
    });
    try {
      const page = await context.newPage();
      const url = `${base.replace(/\/$/, '')}/${encodeURIComponent(name)}.dc.html${process.env.DESIGN_TOKEN || ''}`;
      await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
      await page.waitForTimeout(2500);
      await page.screenshot({ path: path.join(outputDir, `o_${name.slice(0, 2)}.png`), fullPage: true });
    } finally {
      await context.close();
    }
  }
} finally {
  await browser.close();
}
