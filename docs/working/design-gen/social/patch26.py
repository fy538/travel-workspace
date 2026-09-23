"""Consume vdl-stage1 0.4.1 (adoption reviewed September 11): 02.4, 02.5 and 05 D7-A restore the Print Room illustration
and thumbnail and the selected order original/listing -> Reply -> gallery notes -> Priya -> private Ask, using the shared
reader's show=reader / show=ask composition. No other composition changes. Records the consumed version."""
import re, json
MISS = []
def sub(path, pairs):
    s = open(path).read()
    for old, new in pairs:
        n = s.count(old)
        if n == 1: s = s.replace(old, new)
        elif new in s: pass
        else: MISS.append((path, old[:90], n))
    open(path, 'w').write(s)

# ───────────────────────────── gen_c2 · the reader, split around the host's own sections ─────────────────────────────
s = open('gen_c2.py').read()
i = s.index('def reader_phone('); j = s.index('\ndef recipient_inset(', i)
s = s[:i] + '''def reader_phone(compose=''):
    """02.4 / 02.5 / 05 D7-A on the shared OriginalReader 0.4.1, in the selected order: her original and the listing, Reply,
    then this page's own sections (the gallery's notes, Priya's visit), then the private Ask. show=reader and show=ask are
    the same component, so there is one Ask and no Social-only reader. The media and thumbnail are Social 02.4's own
    Print Room drawings, supplied by file; the label stays as their attribution."""
    props = dict(density='full', show='reader', author='Maya', audience='Thursday · to friends',
                 media='ILLUSTRATION · NOT HER PHOTOGRAPH', mediaSrc='media/print-room-illustration.svg', thumbSrc='media/print-room-thumb.svg',
                 words='The side room was my favorite. Go on a weekday, it was empty.', place='The Harbor Print Room',
                 placeDetail='Red Hook · Tue–Sun 11–6 · *Rooms Remade* through Sunday', placeMeta='Listed hours, not checked today',
                 ask='Ask about the Print Room')
    if compose: props['compose'] = compose
    inner = f'<div style="padding: 20px 22px 0 22px;">{dci("OriginalReader", 640 if compose else 580, **props)}</div>'
    inner += sect('From the gallery') + gut(f'<div style="display: flex; gap: 12px; align-items: flex-start;">{thumb("room", 44)}<div style="flex: 1;">{title("The side room, then and now", 15, 20, 600)}<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 3px;">The print shop that was here left the drying racks; the show hangs the new work on them.</div>{src("The gallery&rsquo;s own notes")}</div></div>')
    inner += sect('Also about the Print Room') + gut('<div>' + share_line('P', 'Priya', by('Priya', 'print_room')[2], 'her own visit, a rainy Tuesday', last=True) + '</div>')
    inner += f'<div style="padding: 16px 22px 0 22px;">{dci("OriginalReader", 48, density="full", show="ask", author="Maya", ask="Ask about the Print Room")}</div>'
    inner += '<div style="height: 18px;"></div>'
    return phone2(inner)
''' + s[j:]
open('gen_c2.py', 'w').write(s)

sub('gen_c2.py', [
    ("('SHARED &middot; OriginalReader full &middot; vdl-stage1 0.3', 'THE GALLERY&rsquo;S NOTES AND PRIYA ARE PLACES CONTENT BELOW THE READER', 'D5 &middot; ORIGINAL LEADS')",
     "('SHARED &middot; OriginalReader full, show reader + ask &middot; vdl-stage1 0.4.1', 'THE SELECTED ORDER: ORIGINAL &rarr; REPLY &rarr; GALLERY NOTES &rarr; PRIYA &rarr; PRIVATE ASK &middot; MEDIA SUPPLIED', 'D5 &middot; ORIGINAL LEADS')"),
    ("('SHARED &middot; OriginalReader full, compose &middot; vdl-stage1 0.3', 'D2 STARTING POSITION: REPLY', 'NO REACTION COUNT &middot; RESULT BELOW')",
     "('SHARED &middot; OriginalReader full, compose, show reader + ask &middot; vdl-stage1 0.4.1', 'D2 STARTING POSITION: REPLY', 'NO REACTION COUNT &middot; RESULT BELOW')"),
])
# every remaining stamp that names the consumed package now names the one version in use
for f in ('gen_c2.py', 'gen_c3.py'):
    t = open(f).read(); t = t.replace('vdl-stage1 0.3', 'vdl-stage1 0.4.1'); open(f, 'w').write(t)

# ───────────────────────────── gen_c5 · 07 records the consumed version and the restored order ─────────────────────────────
sub('gen_c5.py', [
    ("adopt = blk('SHARED PACKAGE CONSUMED &middot; VDL-STAGE1 0.3 FROM WORKBENCH C13AE951',", "adopt = blk('SHARED PACKAGE CONSUMED &middot; VDL-STAGE1 0.4.1 FROM WORKBENCH C13AE951',"),
    ("N('<b>Consumed files:</b> OriginalReader, InviteCard and Notice at the workbench etags recorded in vdl-package.json; vdl.css (sha256 7b6fa1d3&hellip;) and the kernel copy of styles.css (sha256 a843ca5b&hellip;, identical to the published kernel file, stamp travel-app@e2e792913). Boards 02, 03 and 05 load both stylesheets; every other board is unchanged construction. The originals are kept in this project as <i>Before shared package</i> copies of boards 02, 03 and 05. '",
     "N('<b>Consumed files, vdl-stage1 0.4.1:</b> OriginalReader at etag 1789153753071940 (13,559 bytes); InviteCard and Notice byte-identical to 0.3 (etags 1789098056754095, 1789081717510486); vdl.css (sha256 7b6fa1d3&hellip;, unchanged since 0.3; its internal version string still reads 0.3) and the kernel copy of styles.css (sha256 a843ca5b&hellip;, identical to the published kernel file, stamp travel-app@e2e792913); media/print-room-illustration.svg and media/print-room-thumb.svg, Social 02.4&rsquo;s own drawings, by recorded sha256. The project&rsquo;s vdl-consumed.json lists them. Adoption is by copy at these versions, not live synchronization. Boards 02, 03 and 05 load both stylesheets. The originals are kept as <i>Before shared package</i> copies of boards 02, 03 and 05. '"),
    ("    ['02.4 &middot; the Print Room, opened', 'OriginalReader', 'density full', 'The gallery&rsquo;s notes and Priya&rsquo;s visit, which are Places content around the reader. The private Ask now sits directly under the reply field, as the shared reader places it, instead of after those sections'],",
     "    ['02.4 &middot; the Print Room, opened', 'OriginalReader', 'density full; show reader, then show ask; supplied media and thumbnail', 'The gallery&rsquo;s notes and Priya&rsquo;s visit, which this page owns, placed between the reader and the private Ask: the selected order is restored, and the Print Room drawing and thumbnail are back'],"),
    ("    ['02.5 &middot; Reply to Maya, in context', 'OriginalReader', 'density full, compose', 'The same place-owned sections; the result below it on the shared Notice'],",
     "    ['02.5 &middot; Reply to Maya, in context', 'OriginalReader', 'density full, compose; show reader, then show ask; supplied media and thumbnail', 'As 02.4, with the editor and Send kept; the result below it on the shared Notice'],"),
    ("    ['05 D7-A &middot; A1 received', 'OriginalReader', 'density full', 'As 02.4'],",
     "    ['05 D7-A &middot; A1 received', 'OriginalReader', 'density full; show reader, then show ask; supplied media and thumbnail', 'As 02.4. Both sides of the comparison now carry the Print Room drawing again'],"),
])

# ───────────────────────────── gen_se · 00 statuses and stamp ─────────────────────────────
sub('gen_se.py', [
    ("STAMP = 'SHARED PACKAGE VDL-STAGE1 0.3 CONSUMED &middot; 2026-09-11'", "STAMP = 'SHARED PACKAGE VDL-STAGE1 0.4.1 CONSUMED &middot; 2026-09-11'"),
    ("'SHARED 0.3: 02.4, 02.5 on OriginalReader full; recipient choice and reply result on Notice; 08.2-style Keep and 02.7 sender view reported as missing variants'",
     "'SHARED 0.4.1: 02.4 and 02.5 restore the Print Room drawing and the selected order, original to Reply to gallery notes to Priya to private Ask; recipient choice and reply result on Notice'"),
    ("'SHARED 0.3: 03.1 on InviteCard host, 03.2 on InviteCard guest; the first-host step added as an inset; the work account given a fair baseline'",
     "'SHARED 0.4.1 (InviteCard unchanged since 0.3): 03.1 on InviteCard host, 03.2 on InviteCard guest; the first-host inset; the fair-baseline work account'"),
    ("'SHARED 0.3: D7-A on OriginalReader full; D7&rsquo;s matched inputs unchanged; 13 frames = UNRESOLVED SCOPE DISCREPANCY'",
     "'SHARED 0.4.1: D7-A restored like 02.4, so both sides carry the drawing; matched inputs unchanged; 13 frames = UNRESOLVED SCOPE DISCREPANCY'"),
    ("'SHARED 0.3: what each frame consumes, the missing variants, the coverage follow-through with owners and triggers; both budget discrepancies'",
     "'SHARED 0.4.1: what each frame consumes at which version, the missing variants, the coverage follow-through; both budget discrepancies'"),
])

# ───────────────────────────── the consumed-version record, shipped with the project ─────────────────────────────
rec = {
    "consumer": "Vesper — Social Experience (3ef10868)",
    "package": "vdl-stage1 0.4.1",
    "workbench": "c13ae951-0977-4bac-90a6-c964146a9ca6",
    "recorded": "2026-09-11",
    "method": "copied at the recorded versions; not live synchronization",
    "kernel": {"stamp": "travel-app@e2e792913 tokens:80d0648dd300 gen:1", "styles_css_sha256": "a843ca5ba6fe7595ff05c629ed88be8f3051e073a51cda4500e18ee5910d7f6c"},
    "files": [
        {"path": "vdl.css", "sha256": "7b6fa1d3dfccc92c59be1193cd68cdb032845a54c0316540e3ab58fe0b968515", "note": "unchanged since 0.3; its --vdl-version string still reads 0.3"},
        {"path": "OriginalReader.dc.html", "workbench_etag": "1789153753071940", "bytes": 13559},
        {"path": "InviteCard.dc.html", "workbench_etag": "1789098056754095", "bytes": 9231, "note": "byte-identical to 0.3"},
        {"path": "Notice.dc.html", "workbench_etag": "1789081717510486", "bytes": 2531, "note": "byte-identical to 0.3"},
        {"path": "media/print-room-illustration.svg", "sha256": "ecfe1b1519f0f0392526a73193e6336f3d57c7125646914527fe98d3922c020b", "source": "Social 02.4's own illustration"},
        {"path": "media/print-room-thumb.svg", "sha256": "d4eb4d93a799d02613dea8824d350918302c4c7b60cce1d3781d8d29afa2f628", "source": "Social 02.4's own place thumbnail"},
    ],
    "instances": {
        "02 - A little of your world": ["02.4 OriginalReader full show=reader+ask, mediaSrc, thumbSrc", "02.5 OriginalReader full compose show=reader+ask, mediaSrc, thumbSrc", "02.2 inset Notice applied+failed", "02.5 result Notice applied+failed"],
        "03 - An easier way to get together": ["03.1 InviteCard host x2", "03.2 InviteCard guest shape=pill"],
        "05 - The important alternatives": ["05 D7-A OriginalReader full show=reader+ask, mediaSrc, thumbSrc"],
    },
    "kept_local": ["08.2 nonspatial reader with Keep", "02.7 sender-owned share", "04.2 and 08.1 photo on Home", "03.6 changed arrangement for a guest", "03.7 arrival and the guest link frame", "03.3 and 03.4 attributed contributions"],
}
open('out/vdl-consumed.json', 'w').write(json.dumps(rec, indent=2, ensure_ascii=False) + '\n')

left = [f for f in ('gen_c2.py', 'gen_c3.py', 'gen_c5.py', 'gen_se.py') if 'vdl-stage1 0.3' in open(f).read() or 'VDL-STAGE1 0.3' in open(f).read()]
print('patched; misses:', len(MISS), '; files still naming 0.3:', left); [print('  MISS', *x) for x in MISS]
