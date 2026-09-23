"""Vesper — Multiplayer Shapes. Shared board grammar for the ten exploratory directions.
Reuses the Social/Home/Places board kit and the shared design language vdl-stage1 0.4.1
(components copied from workbench c13ae951). Everything drawn is fixture and exploratory;
nothing here is selected, ruled, or adopted."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
HP = os.path.join(HERE, 'hp')
sys.path.insert(0, HP)
from kit import *
from gen_generous import col, N, FOOT, head, facepile, caption
from gen_generous3 import sect, meta, title as ttl_, sup, gut, card, author_row
from gen_merge import tbl, blk
from gen_p2_common import (phone2, header, question_line, share_line, place_unit,
                           ending as pl_ending, plate, thumb, src, unc)

OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
HJ = os.path.join(OUT, 'heights.json')
def hh(k, d=0):
    try: return json.load(open(HJ)).get(k, d)
    except Exception: return d

KERNEL_CSS = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'
HEAD_VDL = HEAD.replace('<helmet>', f'<helmet>\n  <link rel="stylesheet" href="{KERNEL_CSS}">\n  <link rel="stylesheet" href="vdl.css">', 1)
assert HEAD_VDL != HEAD, 'helmet not found in HEAD'

HAIR = 'rgba(27,23,20,0.10)'
STAMP = 'EXPLORATORY &middot; BRAINSTORM ONLY &middot; 2026-09-20'
FOOTX = (FOOT + ' &middot; EVERY CANVAS HERE IS AN EXPLORATION, NOT A SELECTED DESIGN: NOTHING ON THESE BOARDS IS ADOPTED, '
         'RULED, OR PROMISED &middot; NO POLICY, NOTIFICATION, GUEST-IDENTITY OR SCHEMA COMMITMENT FOLLOWS FROM DRAWING IT &middot; '
         'BRIEF: docs/working/claude-design-multiplayer-product-shapes-exploration-2026-09-20.md &middot; '
         'SHARED DESIGN LANGUAGE: vdl-stage1 0.4.1, COPIED FROM WORKBENCH c13ae951')

def dci(name, h, **props):
    """One shared-package component instance."""
    attrs = ' '.join(f'{k}="{v}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'

def inset(label, body, note):
    """A labelled state of an existing frame, drawn beside it. Not a new frame."""
    return (f'<div style="margin-top: 14px; width: 393px; box-sizing: border-box; border: 1px dashed rgba(27,23,20,0.28); '
            f'border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px;">'
            f'<div class="kickm">{label}</div>{body}<div class="fn" style="color: #6E6862; line-height: 15px;">{note}</div></div>')

def tag(t, c=GOLDD, bg='rgba(176,133,58,0.10)'):
    return f'<span style="{MONO} font-size: 9px; font-weight: 700; letter-spacing: 1px; color: {c}; background: {bg}; border-radius: 4px; padding: 2px 6px; white-space: nowrap;">{t}</span>'

def cap(n, t, s2='', tags=()):
    """Frame caption: number, one line of what it is, one quieter line, optional tags."""
    tg = ('<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">' + ''.join(tags) + '</div>') if tags else ''
    return tg + caption(n, t, s2)

def led(pairs):
    """The compact record under a canvas: key on the left, one sentence on the right."""
    return ('<div class="led">' + ''.join(
        f'<div class="k">{k}</div><div>{v}</div>' for k, v in pairs) + '</div>')

def notes(t, html, w=560):
    return f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column; gap: 10px; padding-top: 26px;">{blk(t, html)}</div>'

VERDICT = {
    'retain': (GREEN, 'rgba(61,112,80,0.12)'),
    'merge': (PLAN, 'rgba(42,56,75,0.10)'),
    'rework': (GOLDD, 'rgba(176,133,58,0.14)'),
    'defer': (MUTE, 'rgba(110,104,98,0.10)'),
    'reject': (OX, 'rgba(122,46,46,0.10)'),
}
def verdict(kind, line, question):
    c, bg = VERDICT[kind]
    return (f'<div style="border-left: 3px solid {c}; padding: 2px 0 2px 14px; display: flex; flex-direction: column; gap: 6px;">'
            f'<div style="display: flex; gap: 8px; align-items: center;">{tag(kind.upper(), c, bg)}'
            f'<span style="font-size: 13px; line-height: 18px; color: {INK};">{line}</span></div>'
            f'<div style="{SERIF} font-style: italic; font-size: 14px; line-height: 20px; color: {INK2};">Still unanswered: {question}</div></div>')

def bw(n_phones, note_widths=(), gap=46, pad=64, phone=393):
    """Board width must cover BOTH rows: the phones and the notes beneath them."""
    a = n_phones * phone + max(n_phones - 1, 0) * gap
    b = sum(note_widths) + max(len(note_widths) - 1, 0) * gap
    return max(a, b) + pad

def board(w, h, kick, title_, sub, cols, note_cols=(), foot=FOOTX, vdl=True):
    body = '<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols) + '</div>'
    if note_cols:
        body += ('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; '
                 'border-top: 1px solid rgba(27,23,20,0.12);">' + ''.join(note_cols) + '</div>')
    H = HEAD_VDL if vdl else HEAD
    return (H + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; '
            f'padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, title_, sub) + body
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)

def sheetboard(w, h, kick, title_, sub, inner, foot=FOOTX, vdl=False):
    H = HEAD_VDL if vdl else HEAD
    return (H + f'<div style="width: {w}px; min-height: {h}px; background: #F4F0E7; box-sizing: border-box; '
            f'padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(kick, title_, sub) + f'<div style="display: flex; flex-direction: column; gap: 34px;">{inner}</div>'
            + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{foot}</div></div>' + TAIL)

def write(name, html):
    p = os.path.join(OUT, name + '.dc.html')
    open(p, 'w').write(html)
    return name, len(html.encode())
