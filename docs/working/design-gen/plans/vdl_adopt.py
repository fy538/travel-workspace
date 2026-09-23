"""Shared-package adoption helpers for Plans (vdl-stage1 0.3; consumed files identical at 0.4).
Converts Plans' local controls onto the shared construction without changing composition.
Idempotent: re-running on an adopted file changes nothing."""
import re
KERNEL = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'
LINKS = (f'<link rel="stylesheet" href="{KERNEL}" />\n'
         '        <link rel="stylesheet" href="vdl.css" />\n        ')
BTN = {
    'chip pri':   'vdl-btn r16 primary vk-t-labelSemibold',
    'chip':       'vdl-btn r16 secondary vk-t-labelSemibold',
    'chip quiet': 'vdl-btn r16 pl-quiet vk-t-labelSemibold',
    'chip gold':  'vdl-btn r16 secondary pl-gold vk-t-labelSemibold',
    'chip out':   'vdl-btn r16 secondary pl-out vk-t-labelSemibold',
    'chip dis':   'vdl-btn r16 secondary pl-dis vk-t-labelSemibold',
}
def add_links(h):
    if 'href="vdl.css"' in h: return h
    k = '<link rel="stylesheet" href="./kit/plans.css" />'
    assert k in h, 'no kit link'
    return h.replace(k, LINKS + k, 1)
def convert_chips(h, stop_marker=None):
    head, tail = (h.split(stop_marker, 1) if stop_marker and stop_marker in h else (h, None))
    unknown = set(re.findall(r'class="(chip(?: [a-z]+)*)"', head)) - set(BTN)
    assert not unknown, f'unmapped chip variants: {unknown}'
    head = re.sub(r'class="(chip(?: [a-z]+)*)"', lambda m: f'class="{BTN[m.group(1)]}"', head)
    return head if tail is None else head + stop_marker + tail
def convert_doors(h):
    # standalone doors: the typed arrow becomes the shared Door's drawn arrow
    h = re.sub(r'<(div|span) class="(door|door2(?: [a-z]+)*)"((?: [a-z-]+="[^"]*")*)>([^<]*?) →<',
               lambda m: f'<{m.group(1)} class="{m.group(2)} vdl-door"{m.group(3)}>{m.group(4)}<', h)
    h = re.sub(r'class="seehere"', 'class="seehere vdl-door"', h)
    return h
def adopt(h, stop_marker=None):
    return convert_doors(convert_chips(add_links(h), stop_marker))
