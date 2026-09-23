#!/usr/bin/env node
/**
 * Export the Vesper Production Kernel's token layer from travel-app source.
 *
 * Compiles travel-app's token constants and writes the Claude Design assets:
 *   styles.css   CSS custom properties, type-role classes, material/recipe classes
 *   tokens.json  the same values, machine-readable
 *   Tokens.html  the kernel's generated Tokens card (it consumes styles.css)
 *
 * Usage:
 *   node scripts/design_kernel_export.mjs --out <dir> [--app <travel-app>] [--since <rev>]
 *   node scripts/design_kernel_export.mjs --check <styles.css> [--app <travel-app>]
 *
 * --check compares a published styles.css stamp with current source: exit 0 when
 * the token hash matches, 1 on drift, 2 on tool failure. Output is deterministic
 * for a given source revision; unmapped fonts or style keys fail rather than guess.
 */
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const GENERATOR_VERSION = 1;
const SOURCES = [
  'constants/colors.ts',
  'constants/layout.ts',
  'constants/textVariants.ts',
  'constants/fonts.ts',
  'constants/cardSurface.ts',
  'constants/headerChrome.ts',
  'components/ui/state/stateTokens.ts',
  'components/ui/segmentedTokens.ts',
];
const FONT_IMPORT =
  'https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=JetBrains+Mono:wght@400;500;700&display=swap';
const FAMILIES = {
  serif: '"EB Garamond", Georgia, "Times New Roman", serif',
  sans: '-apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", system-ui, sans-serif',
  mono: '"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace',
};

function fail(message, code = 2) {
  process.stderr.write(`design_kernel_export: ${message}\n`);
  process.exit(code);
}

function arg(name) {
  const i = process.argv.indexOf(name);
  if (i < 0) return undefined;
  const value = process.argv[i + 1];
  if (!value || value.startsWith('--')) fail(`${name} needs a value`);
  return value;
}

const workspace = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const app = path.resolve(arg('--app') ?? path.join(workspace, 'travel-app'));
const outDir = arg('--out');
const checkFile = arg('--check');
const since = arg('--since');
if (!outDir && !checkFile) {
  fail('usage: --out <dir> [--since <rev>] | --check <styles.css>   [--app <travel-app>]');
}

function git(...args) {
  try {
    return execFileSync('git', ['-C', app, ...args], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
  } catch (error) {
    fail(`git ${args.join(' ')} failed: ${String(error.stderr || error.message).trim()}`);
  }
}

function loadSources() {
  const tsc = path.join(app, 'node_modules/.bin/tsc');
  if (!fs.existsSync(tsc)) fail(`tsc not found at ${tsc}; install travel-app dependencies`);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'vk-tokens-'));
  try {
    // Token modules only touch Platform/StyleSheet at load time.
    const stub = path.join(tmp, 'node_modules/react-native');
    fs.mkdirSync(stub, { recursive: true });
    fs.writeFileSync(
      path.join(stub, 'index.js'),
      "module.exports = { Platform: { OS: 'ios', select: (o) => o.ios ?? o.default }, StyleSheet: { create: (x) => x, flatten: (x) => x, hairlineWidth: 0.5 } };\n",
    );
    try {
      execFileSync(
        tsc,
        [...SOURCES, '--outDir', path.join(tmp, 'out'), '--rootDir', '.', '--module', 'commonjs',
          '--target', 'es2020', '--skipLibCheck', '--esModuleInterop'],
        { cwd: app, stdio: ['ignore', 'pipe', 'pipe'] },
      );
    } catch (error) {
      fail(`tsc failed:\n${error.stdout ?? ''}${error.stderr ?? ''}`);
    }
    const req = createRequire(path.join(tmp, 'out', 'index.js'));
    const load = (p) => req(path.join(tmp, 'out', p.replace(/\.ts$/, '.js')));
    return {
      colors: load('constants/colors.ts'),
      layout: load('constants/layout.ts'),
      text: load('constants/textVariants.ts').textVariants,
      fonts: load('constants/fonts.ts'),
      card: load('constants/cardSurface.ts'),
      header: load('constants/headerChrome.ts').headerChrome,
      state: load('components/ui/state/stateTokens.ts'),
      segmented: load('components/ui/segmentedTokens.ts').segmentedTokens,
    };
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

function canonical(value) {
  if (Array.isArray(value)) return value.map(canonical);
  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.keys(value).sort()
        .map((k) => [k, canonical(value[k])])
        .filter(([, v]) => v !== undefined),
    );
  }
  return typeof value === 'function' ? undefined : value;
}

const src = loadSources();
const { colors, vesperPrimitiveTokens: primitives, vesperSemanticTokens: semantic } = src.colors;
const L = src.layout;
const card = src.card;
const tokens = {
  primitives, semantic, colors,
  fontFamily: src.fonts.fontFamily, letterSpacing: src.fonts.letterSpacing,
  text: src.text,
  spacing: L.spacing, radius: L.radius,
  cardRadius: card.cardSurfaceRadius, density: card.cardSurfaceDensity,
  materials: card.cardSurfaceMaterial, recipes: card.cardSurfaceRecipe,
  elevation: L.elevation, letterpress: L.letterpress, focusRing: L.focusRing,
  sectionRhythms: L.sectionRhythms, sheetContentRhythms: L.sheetContentRhythms,
  containerRhythms: L.containerRhythms, cardStackRhythms: L.cardStackRhythms,
  pageChrome: L.pageChrome, iconSizes: L.iconSizes, a11y: L.a11y, layout: L.layout,
  header: src.header,
  stateColors: src.state.stateColors, stateRadii: src.state.stateRadii, stateSpacing: src.state.stateSpacing,
  segmented: src.segmented,
};
const tokenHash = createHash('sha256').update(JSON.stringify(canonical(tokens))).digest('hex').slice(0, 12);
const rev = git('rev-parse', '--short=9', 'HEAD');
const revDate = git('show', '-s', '--format=%cs', 'HEAD');
const dirty = git('status', '--porcelain', '--', ...SOURCES) !== '';
const version = `travel-app@${rev}${dirty ? '+dirty' : ''} tokens:${tokenHash} gen:${GENERATOR_VERSION}`;

if (checkFile) {
  let existing;
  try {
    existing = fs.readFileSync(checkFile, 'utf8');
  } catch (error) {
    fail(`cannot read ${checkFile}: ${error.message}`);
  }
  const found = /--vk-version:\s*"([^"]*)"/.exec(existing)?.[1];
  if (!found) fail(`${checkFile} carries no --vk-version stamp`);
  const stamp = (s) => `${/tokens:(\w+)/.exec(s)?.[1]} gen:${/gen:(\d+)/.exec(s)?.[1]}`;
  if (stamp(found) === stamp(version)) {
    console.log(`current  published "${found}"\n         source    "${version}"`);
    process.exit(0);
  }
  console.log(`DRIFT    published "${found}"\n         source    "${version}"`);
  process.exit(1);
}

// ---- CSS -------------------------------------------------------------------

const px = (v) => (typeof v === 'number' ? (v === 0 ? '0' : `${v}px`) : String(v));
const rule = (selector, decls) => `${selector} {\n${decls.map((d) => `  ${d};`).join('\n')}\n}`;

function vars(prefix, obj, lines, keep = () => true) {
  for (const [k, v] of Object.entries(obj ?? {})) {
    const name = `${prefix}-${k}`;
    if (v && typeof v === 'object') vars(name, v, lines, keep);
    else if ((typeof v === 'string' || typeof v === 'number') && keep(v)) {
      lines.push(`  --vk-${name}: ${typeof v === 'number' ? px(v) : v};`);
    }
  }
}

function fontFor(rn) {
  if (rn === 'System') return { family: 'var(--vk-font-sans)', weight: '400', italic: false };
  let m = /^EBGaramond_(\d{3})[A-Za-z]*(_Italic)?$/.exec(rn);
  if (m) return { family: 'var(--vk-font-serif)', weight: m[1], italic: Boolean(m[2]) };
  m = /^JetBrainsMono_(\d{3})[A-Za-z]*$/.exec(rn);
  if (m) return { family: 'var(--vk-font-mono)', weight: m[1], italic: false };
  fail(`unmapped fontFamily "${rn}"; extend fontFor()`);
}

const ROLE_KEYS = new Set(['fontFamily', 'fontWeight', 'fontSize', 'lineHeight', 'letterSpacing', 'color', 'textTransform', 'fontStyle']);
function roleCss(role, spec) {
  for (const k of Object.keys(spec)) if (!ROLE_KEYS.has(k)) fail(`text role ${role} uses unsupported key ${k}`);
  const f = fontFor(spec.fontFamily ?? 'System');
  const decls = [
    `font-family: ${f.family}`,
    `font-weight: ${spec.fontWeight ?? f.weight}`,
    `font-style: ${spec.fontStyle ?? (f.italic ? 'italic' : 'normal')}`,
    `font-size: ${px(spec.fontSize)}`,
    `line-height: ${spec.lineHeight ? px(spec.lineHeight) : 'normal'}`,
    `letter-spacing: ${spec.letterSpacing !== undefined ? px(spec.letterSpacing) : 'normal'}`,
  ];
  if (spec.textTransform) decls.push(`text-transform: ${spec.textTransform}`);
  if (spec.color) decls.push(`color: ${spec.color}`);
  return decls;
}

const VIEW_KEYS = new Set(['backgroundColor', 'borderWidth', 'borderTopWidth', 'borderBottomWidth', 'borderLeftWidth',
  'borderRightWidth', 'borderColor', 'boxShadow', 'paddingVertical', 'paddingHorizontal', 'borderRadius']);
function viewCss(name, style) {
  for (const k of Object.keys(style)) if (!VIEW_KEYS.has(k)) fail(`${name} uses unsupported style key ${k}`);
  const decls = [];
  const borderColor = style.borderColor ?? 'transparent';
  if (style.backgroundColor) decls.push(`background-color: ${style.backgroundColor}`);
  if (style.borderWidth !== undefined) decls.push(`border: ${px(style.borderWidth)} solid ${borderColor}`);
  for (const side of ['Top', 'Bottom', 'Left', 'Right']) {
    const w = style[`border${side}Width`];
    if (w !== undefined) decls.push(`border-${side.toLowerCase()}: ${px(w)} solid ${borderColor}`);
  }
  if (style.boxShadow) decls.push(`box-shadow: ${style.boxShadow}`);
  if (style.borderRadius !== undefined) decls.push(`border-radius: ${px(style.borderRadius)}`);
  if (style.paddingVertical !== undefined) decls.push(`padding-block: ${px(style.paddingVertical)}`);
  if (style.paddingHorizontal !== undefined) decls.push(`padding-inline: ${px(style.paddingHorizontal)}`);
  return decls;
}

function recipeCss(name, recipe) {
  const material = card.cardSurfaceMaterial[recipe.material];
  const density = card.cardSurfaceDensity[recipe.density];
  const radius = card.cardSurfaceRadius[recipe.radius];
  if (!material || !density || radius === undefined) fail(`recipe ${name} references an unknown material/density/radius`);
  return [
    ...viewCss(`material ${recipe.material}`, material),
    `border-radius: ${px(radius)}`,
    ...viewCss(`density ${recipe.density}`, density),
  ];
}

const root = [
  `  --vk-version: "${version}";`,
  `  --vk-font-serif: ${FAMILIES.serif};`,
  `  --vk-font-sans: ${FAMILIES.sans};`,
  `  --vk-font-mono: ${FAMILIES.mono};`,
  '  /* primitive + semantic palette (colors.ts) */',
  ...Object.entries(primitives).map(([k, v]) => `  --vk-${k}: ${v};`),
  ...Object.entries(semantic).map(([k, v]) => `  --vk-${k}: ${v};`),
  '  /* full color tree: colors.<path> -> --vk-color-<path> */',
];
vars('color', colors, root, (v) => typeof v === 'string');
root.push('  /* layout.ts */');
vars('spacing', L.spacing, root);
vars('radius', L.radius, root);
vars('track', src.fonts.letterSpacing, root);
for (const [k, v] of Object.entries(L.elevation)) {
  if (!v.boxShadow) fail(`elevation.${k} has no boxShadow`);
  root.push(`  --vk-shadow-${k}: ${v.boxShadow};`);
}
root.push(`  --vk-shadow-letterpress: ${L.letterpress.shadow.boxShadow};`);
root.push(`  --vk-letterpress-cardBg: ${L.letterpress.cardBg};`);
root.push(`  --vk-focus-ring: ${L.focusRing.boxShadow};`);
vars('rhythm-section', L.sectionRhythms, root);
vars('rhythm-sheet', L.sheetContentRhythms, root);
vars('rhythm-container', L.containerRhythms, root);
vars('rhythm-cardstack', L.cardStackRhythms, root);
vars('page', L.pageChrome, root);
vars('icon', L.iconSizes, root);
vars('a11y', L.a11y, root);
vars('layout', L.layout, root, (v) => typeof v === 'number');
root.push('  /* cardSurface.ts, headerChrome.ts, state + segmented tokens */');
vars('card-radius', card.cardSurfaceRadius, root);
for (const [k, v] of Object.entries(card.cardSurfaceDensity)) {
  if (v.paddingVertical !== undefined) root.push(`  --vk-density-${k}-y: ${px(v.paddingVertical)};`);
  if (v.paddingHorizontal !== undefined) root.push(`  --vk-density-${k}-x: ${px(v.paddingHorizontal)};`);
}
vars('header', src.header, root);
vars('state-color', src.state.stateColors, root, (v) => typeof v === 'string');
vars('state-radius', src.state.stateRadii, root);
vars('state-space', src.state.stateSpacing, root);
vars('segmented', src.segmented, root);

const roleEntries = Object.entries(src.text);
const materialEntries = Object.entries(card.cardSurfaceMaterial).filter(([, v]) => Object.keys(v).length > 0);
const recipeEntries = Object.entries(card.cardSurfaceRecipe);

const css = [
  '/* Vesper · Production Kernel — styles.css',
  ' * GENERATED by travel-workspace scripts/design_kernel_export.mjs. Do not hand-edit:',
  ` * regenerate from travel-app and republish. Source: travel-app@${rev} (${revDate}).`,
  ` * Version: ${version}`,
  ' * Naming: --vk-<primitive|semantic>, --vk-color-<colors path>, --vk-<group>-<key>;',
  ' * .vk-t-<textVariant>, .vk-m-<cardSurfaceMaterial>, .vk-r-<cardSurfaceRecipe>. */',
  `@import url("${FONT_IMPORT}");`,
  '',
  rule(':root', []).replace('{\n\n}', `{\n${root.join('\n')}\n}`),
  '',
  `/* Type roles: textVariants.ts (${roleEntries.length}). RN "System" maps to the platform sans stack. */`,
  ...roleEntries.map(([name, spec]) => rule(`.vk-t-${name}`, roleCss(name, spec))),
  '',
  '/* Materials: cardSurfaceMaterial (surface only; add radius/padding or use a recipe). */',
  ...materialEntries.map(([name, style]) => rule(`.vk-m-${name}`, viewCss(`material ${name}`, style))),
  '',
  '/* Recipes: cardSurfaceRecipe = material x radius x density. Prefer these over ad hoc axes. */',
  ...recipeEntries.map(([name, recipe]) => rule(`.vk-r-${name}`, recipeCss(name, recipe))),
  '',
  rule('.vk-page', ['background-color: var(--vk-paper20)', 'color: var(--vk-ink00)', 'font-family: var(--vk-font-sans)']),
  '',
].join('\n');

// ---- Tokens.html ---------------------------------------------------------------

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function roleDocs(source) {
  const docs = {};
  const re = /(?:\/\*\*((?:(?!\*\/)[\s\S])*)\*\/\s*)?^ {2}([A-Za-z]\w*):\s*\{/gm;
  for (const m of source.matchAll(re)) {
    if (m[1]) docs[m[2]] = m[1].split('\n').map((l) => l.replace(/^\s*\*\s?/, '')).join(' ').replace(/\s+/g, ' ').trim();
  }
  return docs;
}

function blockKeys(source, declaration) {
  const start = source.indexOf(declaration);
  if (start < 0) return null;
  const body = source.slice(start, source.indexOf('\n};', start));
  return new Set([...body.matchAll(/^ {2}([A-Za-z]\w*):/gm)].map((m) => m[1]));
}

const docs = roleDocs(fs.readFileSync(path.join(app, 'constants/textVariants.ts'), 'utf8'));
let sinceRoles = null;
let sinceRadius = null;
let sincePrimitives = null;
if (since) {
  const at = (file) => git('show', `${since}:${file}`);
  sinceRoles = blockKeys(at('constants/textVariants.ts'), 'export const textVariants');
  sinceRadius = blockKeys(at('constants/layout.ts'), 'export const radius');
  sincePrimitives = blockKeys(at('constants/colors.ts'), 'export const vesperPrimitiveTokens');
}
const isNew = (set, key) => (set && !set.has(key) ? `<span class="new">new since ${esc(since)}</span>` : '');

function specText(spec) {
  const f = fontFor(spec.fontFamily ?? 'System');
  const face = f.family.includes('serif') ? 'serif' : f.family.includes('mono') ? 'mono' : 'sans';
  const parts = [`${face} ${spec.fontSize}/${spec.lineHeight ?? 'auto'}`, `w${spec.fontWeight ?? f.weight}`];
  if (spec.fontStyle === 'italic' || f.italic) parts.push('italic');
  if (spec.letterSpacing !== undefined) parts.push(`track ${spec.letterSpacing}`);
  if (spec.textTransform) parts.push(spec.textTransform);
  return parts.join(' · ');
}

const SAMPLE = { serif: 'Evening on the Tagus', sans: 'Plan the afternoon', mono: '07:40 · LIS' };
function typeTable(title, face) {
  const rows = roleEntries.filter(([, spec]) => fontFor(spec.fontFamily ?? 'System').family.includes(face));
  const body = rows.map(([name, spec]) => `<tr><td class="k">${esc(name)}${isNew(sinceRoles, name)}${docs[name] ? `<div class="doc">${esc(docs[name])}</div>` : ''}</td>` +
    `<td><span class="vk-t-${esc(name)}">${esc(SAMPLE[face])}</span></td><td class="spec">${esc(specText(spec))}</td></tr>`).join('\n');
  return `<h3>${esc(title)} <span class="count">${rows.length}</span></h3>\n<div class="scroll"><table><tr><th>Role / class</th><th>Sample</th><th>Spec</th></tr>\n${body}\n</table></div>`;
}

function swatches(entries, varName, newSet) {
  return `<ul class="grid sw">${entries.map(([k, v]) => `<li style="--c:var(--vk-${esc(varName(k))})"><b>${esc(k)}${isNew(newSet, k)}</b>${esc(v)}</li>`).join('')}</ul>`;
}

function flatten(obj, prefix = '') {
  return Object.entries(obj ?? {}).flatMap(([k, v]) => {
    const key = prefix ? `${prefix}.${k}` : k;
    return v && typeof v === 'object' ? flatten(v, key) : [[key, v]];
  });
}

const colorGroups = Object.entries(colors).filter(([, v]) => v && typeof v === 'object');
const colorTop = Object.entries(colors).filter(([, v]) => typeof v === 'string');
const numTable = (rows, head = ['Token', 'Value']) =>
  `<div class="scroll"><table><tr>${head.map((h) => `<th>${esc(h)}</th>`).join('')}</tr>${rows.map(([k, v]) => `<tr><td class="k">${esc(k)}</td><td>${esc(typeof v === 'number' ? `${v}` : v)}</td></tr>`).join('')}</table></div>`;

const html = `<!-- @dsCard group="Tokens" -->
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>Vesper Kernel — Tokens</title>
<link rel="stylesheet" href="styles.css" />
<style>
  body { margin:0; background:var(--vk-paper20); color:var(--vk-ink00); font-family:var(--vk-font-sans); }
  .wrap { max-width:1000px; margin:0 auto; padding:48px 32px 80px; }
  h1 { font:600 24px/29px var(--vk-font-sans); margin:0 0 4px; }
  .src { font-size:12px; color:var(--vk-ink60); margin-bottom:4px; }
  .stamp { font:500 11px/16px var(--vk-font-mono); color:var(--vk-ink60); margin-bottom:24px; }
  h2 { font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:1.4px; color:var(--vk-ink60); margin:44px 0 12px; border-bottom:0.5px solid var(--vk-borderHairline); padding-bottom:6px; }
  h3 { font-size:14px; font-weight:600; margin:26px 0 8px; }
  .count { font:500 11px var(--vk-font-mono); color:var(--vk-ink60); }
  table { width:100%; border-collapse:collapse; font-size:13px; }
  td, th { text-align:left; padding:8px 10px; border-bottom:0.5px solid var(--vk-borderHairlineSoft); vertical-align:top; }
  th { font-size:10px; font-weight:600; text-transform:uppercase; letter-spacing:1.2px; color:var(--vk-gold80); }
  .k { font:500 12px/17px var(--vk-font-mono); color:var(--vk-ink40); }
  .spec { font:500 11px/17px var(--vk-font-mono); color:var(--vk-ink60); white-space:nowrap; }
  .doc { font:400 12px/17px var(--vk-font-sans); color:var(--vk-ink60); margin-top:3px; max-width:340px; }
  .new { display:inline-block; font:600 9px/14px var(--vk-font-sans); letter-spacing:0.8px; text-transform:uppercase; color:var(--vk-gold80); background:color-mix(in srgb, var(--vk-gold60) 12%, transparent); border-radius:4px; padding:1px 6px; margin-left:6px; vertical-align:1px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(150px, 1fr)); gap:10px; }
  ul.sw { list-style:none; margin:0; padding:0; }
  .sw li { border-radius:10px; border:0.5px solid var(--vk-borderHairline); background:var(--vk-paper00); overflow:hidden; padding:0 9px 7px; font:500 10px/14px var(--vk-font-mono); color:var(--vk-ink60); word-break:break-all; }
  .sw li::before { content:""; display:block; height:36px; margin:0 -9px 7px; background:var(--c); }
  .sw b { display:block; font:600 11px/15px var(--vk-font-mono); color:var(--vk-ink00); }
  .n { font:600 11px/15px var(--vk-font-mono); word-break:break-all; }
  .v { font:500 10px/14px var(--vk-font-mono); color:var(--vk-ink60); word-break:break-all; }
  .scroll { overflow-x:auto; }
  .bar { height:10px; background:var(--vk-gold40); border-radius:2px; }
  .rbox { width:56px; height:36px; background:var(--vk-paper00); border:0.5px solid var(--vk-borderHairline); }
  .tile { min-height:64px; padding:12px; font-size:12px; }
  .tile .n { margin-bottom:4px; }
  .avatars { display:flex; align-items:flex-end; gap:18px; flex-wrap:wrap; }
  .avatar { border-radius:9999px; background:var(--vk-gold40); }
  pre { font:500 12px/18px var(--vk-font-mono); background:var(--vk-paper00); border:0.5px solid var(--vk-borderHairline); border-radius:10px; padding:14px 16px; overflow-x:auto; white-space:pre; }
  p.note { font-size:13px; line-height:20px; color:var(--vk-ink40); max-width:720px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Tokens</h1>
  <div class="src">Generated from travel-app ${esc(SOURCES.join(' · '))}</div>
  <div class="stamp">${esc(version)} · source date ${esc(revDate)} · do not hand-edit</div>

  <h2>Consuming these tokens</h2>
  <p class="note">This page renders from <code>styles.css</code> in this design system, the same file consuming projects load. Colors, spacing and radius are CSS custom properties; each type role, card material and card recipe is a single class. Values mirror production source; if a value here looks wrong, fix <code>travel-app</code> and regenerate rather than editing this page.</p>
  <pre>${esc(`<link rel="stylesheet" href="_ds/<folder>/styles.css">
<h1 class="vk-t-serifMast">Tuesday in Lisbon</h1>
<div class="vk-r-quietObject">…</div>
<div style="padding: var(--vk-spacing-xl); background: var(--vk-paper20)">…</div>`)}</pre>

  <h2>Type — textVariants.ts (${roleEntries.length} roles)</h2>
  <p class="note">Every role in the source file is listed; there is no separate curated subset. Role notes are the source's own doc comments. Serif is EB Garamond, mono is JetBrains Mono, and RN "System" renders here as the platform sans stack.</p>
  ${typeTable('Sans', 'sans')}
  ${typeTable('Serif', 'serif')}
  ${typeTable('Mono', 'mono')}

  <h2>Color — primitives and semantic aliases</h2>
  ${swatches(Object.entries(primitives), (k) => k, sincePrimitives)}
  <h3>Semantic</h3>
  ${swatches(Object.entries(semantic), (k) => k, null)}
  <h3>Named semantic colors</h3>
  ${swatches(colorTop, (k) => `color-${k}`, null)}
  ${colorGroups.map(([group, value]) => `<h3>colors.${esc(group)}</h3>\n${swatches(flatten(value).filter(([, v]) => typeof v === 'string'), (k) => `color-${group}-${k.replace(/\./g, '-')}`, null)}`).join('\n  ')}

  <h2>Spacing — spacing</h2>
  <table><tr><th>Token</th><th>Value</th><th></th></tr>${Object.entries(L.spacing).map(([k, v]) => `<tr><td class="k">--vk-spacing-${esc(k)}</td><td>${v}</td><td style="width:60%"><div class="bar" style="width:var(--vk-spacing-${esc(k)})"></div></td></tr>`).join('')}</table>

  <h2>Radius — radius</h2>
  <table><tr><th>Token</th><th>Value</th><th></th></tr>${Object.entries(L.radius).map(([k, v]) => `<tr><td class="k">--vk-radius-${esc(k)}${isNew(sinceRadius, k)}</td><td>${v}</td><td><div class="rbox" style="border-radius:var(--vk-radius-${esc(k)})"></div></td></tr>`).join('')}</table>
  <h3>Card-surface radius (cardSurfaceRadius)</h3>
  ${numTable(Object.entries(card.cardSurfaceRadius).map(([k, v]) => [`--vk-card-radius-${k}`, v]))}

  <h2>Rhythm</h2>
  <h3>Section rhythms</h3>
  ${numTable(flatten(L.sectionRhythms).map(([k, v]) => [`--vk-rhythm-section-${k.replace(/\./g, '-')}`, v]))}
  <h3>Page and container</h3>
  ${numTable([...flatten(L.pageChrome).map(([k, v]) => [`--vk-page-${k}`, v]), ...flatten(L.containerRhythms).map(([k, v]) => [`--vk-rhythm-container-${k.replace(/\./g, '-')}`, v])])}
  <h3>Sheets and card stacks</h3>
  ${numTable([...flatten(L.sheetContentRhythms).map(([k, v]) => [`--vk-rhythm-sheet-${k}`, v]), ...flatten(L.cardStackRhythms).map(([k, v]) => [`--vk-rhythm-cardstack-${k.replace(/\./g, '-')}`, v])])}

  <h2>Identity, icons and targets</h2>
  <div class="avatars">${Object.entries(L.layout).filter(([k, v]) => /^avatar/.test(k) && typeof v === 'number').map(([k, v]) => `<div><div class="avatar" style="width:${v}px;height:${v}px"></div><div class="n" style="margin-top:6px">${esc(k)}</div><div class="v">${v}</div></div>`).join('')}</div>
  ${numTable([...Object.entries(L.iconSizes).map(([k, v]) => [`--vk-icon-${k}`, v]), ...Object.entries(L.a11y).map(([k, v]) => [`--vk-a11y-${k}`, v])])}

  <h2>Elevation</h2>
  <div class="grid">${Object.keys(L.elevation).map((k) => `<div class="tile" style="background:var(--vk-paper00);border-radius:12px;box-shadow:var(--vk-shadow-${esc(k)})"><div class="n">--vk-shadow-${esc(k)}</div></div>`).join('')}</div>

  <h2>Card surfaces — materials and recipes (cardSurface.ts)</h2>
  <p class="note">Recipes bundle material × radius × density. Prefer <code>.vk-r-*</code>; <code>.vk-m-*</code> is surface only. <code>paperRaised</code> / <code>floatingOverlay</code> remain the spatial or tactile exception.</p>
  <div class="grid">${recipeEntries.map(([k, r]) => `<div class="vk-r-${esc(k)} tile"><div class="n">.vk-r-${esc(k)}</div><div class="v">${esc(`${r.material} · ${r.radius} · ${r.density}`)}</div></div>`).join('')}</div>
</div>
</body>
</html>
`;

fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'styles.css'), css);
fs.writeFileSync(path.join(outDir, 'Tokens.html'), html);
fs.writeFileSync(
  path.join(outDir, 'tokens.json'),
  `${JSON.stringify({ version, source: { repo: 'travel-app', rev, date: revDate, dirty, files: SOURCES }, tokens: canonical(tokens) }, null, 2)}\n`,
);
const newRoles = sinceRoles ? roleEntries.map(([k]) => k).filter((k) => !sinceRoles.has(k)) : [];
console.log(`version ${version}`);
console.log(`roles ${roleEntries.length}${since ? ` (new since ${since}: ${newRoles.join(', ') || 'none'})` : ''}`);
console.log(`materials ${materialEntries.length} · recipes ${recipeEntries.length} · css ${css.length} bytes · html ${html.length} bytes`);
