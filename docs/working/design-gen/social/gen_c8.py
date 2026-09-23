"""Board 10 · Photos, sent and received (September 21 additive assignment).
Life's fixture set (shared ledger §10, PH-01 to PH-07) carried through Social: Nora selects PH-02 and PH-04 in the
evening's record, previews the exact selection, sends it to Maya (the ledger's Sunday 9:40 am event) or leaves; the
result, including a partial failure; Maya receives the pair whole on Home, opens it in the viewer and returns; the
matched D5 comparison; and later retrieval in Life without a reply. No approved photographs exist: every picture is a
stand-in frame at its real proportions carrying its ledger ID. Shared components where they exist (Notice, field,
buttons, recipient token); local construction where the package has none, each named. Fixture; PROPOSED."""
import os, sys
from gen_c2 import *
from gen_c2 import HP, HEAD_VDL, dci, inset
from gen_c4 import life_head, bar, entry
sys.path.insert(0, HP)
from kit import anchor_row, orientation, row
from gen_se import hh, tbl, blk, FOOT2, STAMP, ROLE, tag
from gen_p2_common import large

CTX = 'PASTA NIGHT &middot; SAT SEP 19 &middot; AT NORA&rsquo;S'
WHEN = 'SUNDAY 9:40 AM &middot; TO YOU'

# Life's set (ledger §10): id -> (author, (w, h), the picture, provenance line, low light)
PH = {
    'PH-01': ('Maya', (4, 3), 'The table, from above (C1)', 'MAYA &middot; SAT 8:25 PM', False),
    'PH-02': ('Nora', (3, 4), 'The pan on the stove, before anyone came', 'NORA &middot; SAT 6:48 PM', False),
    'PH-03': ('Nora', (3, 4), 'The same pan, a second later', 'NORA &middot; SAT 6:48 PM', False),
    'PH-04': ('Nora', (4, 3), 'The table after everyone left, low light', 'NORA &middot; SAT 10:40 PM', True),
    'PH-05': ('Dana', (3, 4), 'Dana&rsquo;s dish, in Sorrento (B2a)', 'DANA &middot; FRI, SORRENTO', False),
}
RECORD = ['PH-05', 'PH-02', 'PH-03', 'PH-01', 'PH-04']   # the evening's record in Life 04b's order (by time)
GEN = ['PH-02', 'PH-01', 'PH-04']                        # Life 04b.11's general selection: three, one of them Maya's
SENT = ['PH-02', 'PH-04']

DARK = 'background: repeating-linear-gradient(135deg, rgba(27,23,20,0.62) 0 7px, rgba(27,23,20,0.52) 7px 14px);'

def ph(pid, w, h, r=10, label=None):
    """A photograph not yet supplied: its real proportions and ledger ID, nothing drawn to pass for it. Low-light
    pictures are dark stand-ins, because the real one is shown dark, as taken."""
    lab = pid if label is None else label
    low = PH[pid][4]
    style = DARK if low else ''
    col = 'rgba(251,247,236,0.75)' if low else MUTE
    return (f'<div class="{"" if low else "hatch"}" style="{style} width: {w}px; height: {h}px; border-radius: {r}px; flex: none; position: relative; box-sizing: border-box;">'
            + (f'<span class="fn" style="position: absolute; left: 8px; bottom: 6px; color: {col};">{lab}</span>' if lab else '') + '</div>')

def fit(pid, H):
    a, b = PH[pid][1]
    return round(H * a / b), H

def pair(total=317, gap=6, label=True):
    """Two pictures of different shapes side by side at one height, both whole: no crop hides part of either."""
    ratios = [PH[p][1][0] / PH[p][1][1] for p in SENT]
    H = round((total - gap) / sum(ratios))
    return (f'<div style="display: flex; gap: {gap}px;">'
            + ''.join(ph(p, round(H * r), H, 10, p if label else '') for p, r in zip(SENT, ratios)) + '</div>')

def tick(n):
    return (f'<span style="position: absolute; top: 6px; right: 6px; width: 22px; height: 22px; border-radius: 11px; background: {INK}; color: #FBF7EC; '
            f'display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700;">{n}</span>')
def ring():
    return '<span style="position: absolute; top: 6px; right: 6px; width: 20px; height: 20px; border-radius: 11px; border: 1.5px solid rgba(27,23,20,0.45); background: rgba(251,247,236,0.6);"></span>'
def by_badge(letter):
    return (f'<span class="vk-t-capsMicro" style="position: absolute; left: 6px; top: 6px; width: 22px; height: 22px; border-radius: 11px; background: #8A6628; color: #FBF7EC; '
            f'display: flex; align-items: center; justify-content: center; font-weight: 700;">{letter}</span>')
def cell(pid, S, badge=''):
    return f'<div style="position: relative; width: {S}px; height: {S}px;">{ph(pid, S, S, 8)}{badge}</div>'

# ───────────────────────────── 10.1 · select, inside the evening's record ─────────────────────────────
def check():
    return ('<span style="position: absolute; top: 6px; right: 6px; width: 22px; height: 22px; border-radius: 11px; background: #1B1714; display: flex; align-items: center; justify-content: center;">'
            '<svg width="12" height="12" viewBox="0 0 14 14" fill="none"><path d="M3 7.2l2.6 2.6L11 4.4" stroke="#FBF7EC" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')

def record_head(right):
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">PASTA NIGHT &middot; SAT SEP 19</span>'
             f'<span style="margin-left: auto;">{right}</span></div></div>')
    return inner + gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Photographs</div>'
                       f'<div class="fn" style="color: {ANCHOR}; margin-top: 6px;">5 &middot; 3 YOURS &middot; MAYA &middot; DANA</div>', top=14)

def grid(mode, notice=''):
    """mode: 'browse' (no selection), 'general' (Life 04b.11: any picture can be selected), 'share' (started from Share:
    only share-eligible pictures tick; others show their author)."""
    S = 110; cells = []
    for pid in RECORD:
        author = PH[pid][0]; badge = by_badge(author[0]) if author != 'Nora' else ''
        if mode == 'general':
            badge += check() if pid in GEN else ring()
        elif mode == 'share':
            badge += (tick(SENT.index(pid) + 1) if pid in SENT else ring()) if author == 'Nora' else ''
        cells.append(cell(pid, S, badge))
    return f'<div style="display: grid; grid-template-columns: repeat(3, {S}px); gap: 9px;">{"".join(cells)}</div>'

def select_phone(notice=''):
    """10.1 · Life 04b.11, copied: general selection keeps the mixed set and counts what each action can reach."""
    inner = record_head(door('Done', MUTE)) + (gut(notice, top=14) if notice else '') + gut(grid('general'), top=16)
    inner += gut(f'<div style="font-size: 13px; line-height: 19px; color: {INK2};">Maya&rsquo;s photo stays with the dinner.</div>', top=12)
    inner += gut('<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 10px; border-top: 1px solid rgba(27,23,20,0.12); padding-top: 14px;">'
                 f'<span style="font-size: 15px; font-weight: 600; color: {INK}; flex: 1 0 auto;">3 selected</span>'
                 f'{door("Export 2", MUTE)}{door("Delete 2", MUTE)}'
                 '<span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">Share 2</span></div>', top=18)
    return phone(inner, 0, active='Life')

def share_mode_inset():
    body = (grid('share') + f'<div style="font-size: 13px; line-height: 19px; color: {INK2};">Maya&rsquo;s table and Dana&rsquo;s dish are theirs to share.</div>')
    return inset('10.1, THE OTHER MODE &middot; STARTED FROM SHARE', body,
                 'WHEN NORA BEGINS WITH SHARE, ONLY SHARE-ELIGIBLE PICTURES CAN BE TICKED; PH-01 AND PH-05 SHOW THEIR AUTHOR AND STAY VISIBLE &middot; THE GENERAL SELECTION ABOVE (LIFE 04b.11) KEEPS THE MIXED SET &middot; SELECTING OR SEEING A PICTURE GRANTS NOTHING')

# ───────────────────────────── 10.2 · the exact outgoing selection ─────────────────────────────
def share_phone(notice=''):
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; 2 OF YOUR 3</span></div></div>'
    inner += (gut(notice, top=14) if notice else '')
    inner += gut(f'<div style="width: 250px;">{pair(250, 6, label=True)}</div><div class="fn" style="color: {ANCHOR}; margin-top: 8px;">IN THIS ORDER &middot; BOTH YOURS</div>'
                 f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 12px;">{ph("PH-01", *fit("PH-01", 30), 5, "")}<span style="font-size: 13px; line-height: 18px; color: {INK2};">Maya&rsquo;s table isn&rsquo;t in this share. It stays with the dinner.</span></div>', top=18)
    inner += gut(f'<div class="vdl-field" style="min-height: 44px; align-items: center;"><span class="vk-t-bodyMd" style="color: var(--vk-ink40);">Add a line</span></div>', top=18)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div>'
                 f'<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;"><span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">M</span><span class="vk-t-bodySmMedium">Maya</span></span>{door("Change", MUTE)}</div>'
                 f'<div style="font-size: 13px; line-height: 19px; color: {INK2}; margin-top: 10px;">Maya sees these two photos and that they&rsquo;re from Saturday at yours, until you take them back.</div>', top=20)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 16px;"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">Send</span>{door("Not now", MUTE)}</div>', top=24)
    return phone2(inner, active='Life')

def result_inset():
    """Return by outcome. Only a confirmed send clears the selection; every other ending keeps what Nora chose."""
    def lab(t): return f'<div class="kickm" style="margin-top: 4px;">{t}</div>'
    body = (lab('NOT NOW') + f'<div style="font-size: 13px; line-height: 18px; color: {INK2};">Back to Photographs, same scroll. The same three stay selected.</div>'
            + lab('SENT &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 64, tone='applied', title='Sent to Maya · 2 photos', body='Your selection is cleared.')
            + lab('NOTHING WENT &middot; STAYS ON THE SHARE') + dci('Notice', 120, tone='failed', title='Didn’t send. You’re offline.', body='Both photos and Maya are still here.', primary='Try again', secondary='Not now')
            + lab('PART WENT &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 120, tone='failed', title='The pan went. The late table didn’t.', body='Only the late table is waiting to send.', primary='Send the late table', secondary='Leave it')
            + lab('NOT KNOWN YET &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 120, tone='unknown', title='Not sure the late table went', body='The pan reached Maya. Nothing is sent again until this is known.', primary='Check again', secondary='Leave it')
            + f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2};">After part went or not known, the three-picture selection is released: the share used it. What waits is only the undelivered picture, marked on its tile. Not now and nothing went keep the selection.</div>')
    return inset('10.2, WHERE EACH ENDING RETURNS &middot; STATES OF THE SAME SLOT', body,
                 'SHARED &middot; Notice: applied, failed, unknown &middot; GENERAL SELECTION (LIFE) AND PENDING SEND (SOCIAL) ARE KEPT APART &middot; A RETRY SENDS ONLY WHAT IS CONFIRMED UNDELIVERED; AN UNKNOWN RESULT GETS A STATUS CHECK, NOT A RESEND &middot; A SENT SHARE IS NOT A TASK ON NORA&rsquo;S HOME &middot; SIMULATED IN 10P')

# ───────────────────────────── 10.3 · Maya's Home: it arrives whole ─────────────────────────────
def arrival(ctx=True, extra=''):
    c = f'<div class="fn" style="color: {ANCHOR}; margin-top: 8px;">{CTX}</div>' if ctx else ''
    return card(pair() + '<div style="height: 12px;"></div>' + author_row('N', 'Nora', WHEN) + c + extra
                + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 10px;">{door("Open")}{door("Reply", MUTE)}</div>')

def maya_home():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '10:05 AM').replace('>N</span></div>', '>M</span></div>')  # Maya's account, not the kit's default Nora
    inner += orientation('A slow Sunday.', 'Your Print Room share ends tonight.')
    inner += sect('From Nora') + gut(arrival())
    inner += sect('In motion') + gut('<div>' + row('The Print Room &middot; your share &middot; <span style="color: #6E6862;">to friends, until tonight</span>', mark='solid', color=GOLD)
                                    + row('Dentist &middot; Tuesday 9:00', mark='dashed', last=True) + '</div>')
    return phone(inner, 0, active='Home')

def large_inset():
    """The selected arrival (10.5 B) at 1.3x text: inline sizes scaled by the kit's large(), mono lines by a scoped rule."""
    css = '<style>.lt130 .fn, .lt130 .kickm { font-size: 13px; line-height: 17px; }</style>'
    body = css + f'<div class="lt130" style="width: 349px;">{large(arrival())}</div>'
    return inset('10.3, LARGER TEXT &middot; 1.3&times; &middot; THE SELECTED ARRIVAL', body,
                 'THE PHOTOS KEEP THEIR SIZE, SHAPE AND ORDER; THE AUTHOR, TIME AND EVENING REFLOW BELOW THEM &middot; NOTHING TRUNCATES')

# ───────────────────────────── 10.4 · the viewer, and back ─────────────────────────────
def viewer(pid, pos, top=24):
    big = fit(pid, 440) if PH[pid][1] == (3, 4) else (349, 262)
    strip = '<div style="display: flex; gap: 6px; justify-content: center;">' + ''.join(
        f'<div style="padding: 2px; border-radius: 8px; border: 1.5px solid {INK if p == pid else "transparent"};">{ph(p, *fit(p, 44), 6, "")}</div>' for p in SENT) + '</div>'
    head_ = (f'<div style="padding: {top}px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}'
             f'<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">NORA</span><span class="fn" style="margin-left: auto;">{pos} OF 2</span></div></div>')
    img = gut(f'<div style="display: flex; justify-content: center;">{ph(pid, *big, 12, pid + " &middot; NOT SUPPLIED")}</div>'
              f'<div class="fn" style="color: {ANCHOR}; margin-top: 8px;">{PH[pid][3]}</div>', top=16)
    return head_ + img + gut(strip, top=12)

def viewer_phone():
    inner = viewer('PH-02', 1)
    inner += gut(f'<div style="display: flex; align-items: center; min-height: 44px; border: 1px solid rgba(27,23,20,0.14); border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {GHOST}; flex: 1;">Reply to Nora</span></div>', top=16)
    inner += sect('Where it lives') + gut('<div>' + entry('dining', 'Pasta night', 'Saturday Sep 19 &middot; at Nora&rsquo;s') + entry('photo', 'Your table photo', '8:25 &middot; between these two', last=True) + '</div>')
    return phone2(inner, active='Home')

def lowlight_inset():
    body = viewer('PH-04', 2, top=0)
    return inset('10.4, THE SECOND PHOTO &middot; LOW LIGHT, SHOWN AS TAKEN', body,
                 'NO BRIGHTENING, NO FILTER, NO CROP TO FIT &middot; THE CAMERA TIME IS THE ONLY CONTEXT ON THE PICTURE &middot; CLOSE RETURNS TO MAYA&rsquo;S HOME AT THE SAME POSITION, NOT TO A LIFE INDEX')

# ───────────────────────────── 10.5 · D5, matched: three treatments of the same arrival ─────────────────────────────
def compare_block():
    frames = [
        ('A &middot; ORIGINAL ONLY', 'The two photos, who sent them and when', arrival(ctx=False)),
        ('B &middot; LIGHT CONTEXT &middot; SELECTED FOR HOME', 'A, plus which evening they come from, the record they were shared out of', arrival()),
        ('C &middot; EARNED ENRICHMENT', 'B, plus Maya&rsquo;s own 8:25 photo placed between them in time',
         arrival(extra=f'<div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid rgba(27,23,20,0.08);">{entry("photo", "Your table photo", "8:25 &middot; between these two", last=True)}</div>')),
    ]
    cols = ''.join(f'<div style="width: 349px; flex: none; display: flex; flex-direction: column; gap: 8px;"><div class="kick" style="color: {GOLDD if "SELECTED" in k else MUTE};">{k}</div>'
                   f'<div style="font-size: 13px; line-height: 18px; color: {INK2}; min-height: 36px;">{s}</div>{f}</div>' for k, s, f in frames)
    same = tbl(['INPUT', 'A', 'B', 'C'], [
        ['PH-02 and PH-04 in Nora&rsquo;s order, each with its own author and camera time', 'Yes', 'Yes', 'Yes'],
        ['The evening they were shared out of (Maya was there)', 'Held, not shown', 'Shown', 'Shown'],
        ['PH-01, Maya&rsquo;s own photo, 8:25', 'Held, not shown', 'Held, not shown', 'Shown as a link, in time order'],
        ['Grant', 'Display to Maya until Nora takes them back', 'The same', 'The same; PH-01 is Maya&rsquo;s; nothing goes to a model'],
    ])
    return (f'<div style="display: flex; flex-direction: column; gap: 14px;"><div class="kick" style="color: {GOLDD};">10.5 &middot; 05 D5, MATCHED &middot; THE SAME ARRIVAL THREE WAYS</div>'
            f'<div style="display: flex; gap: 24px; align-items: flex-start;">{cols}</div>{same}'
            + N('<b>Selected: B on Home.</b> Nora sent no line, so the evening is the one piece of context, and it comes from her own record. '
                '<b>C inside the opened view only</b> (10.4, &ldquo;Where it lives&rdquo;): Maya&rsquo;s own photograph at 8:25 sits between Nora&rsquo;s 6:48 and 10:40, so together they are the evening before she came, while she was there, and after she left. That is earned without reading a picture, because it is only times and authorship. On Home it would put a second object beside Nora&rsquo;s. '
                '<b>A is a complete ending</b>, and it is what B becomes for a picture with no evening, like PH-06. None of the three adds a caption, a feeling or anything said on Nora&rsquo;s behalf.')
            + '</div>')

# ───────────────────────────── 10.6 · later, in Life, without a reply ─────────────────────────────
def maya_life():
    inner = life_head('LIFE &middot; PEOPLE', 'WED SEP 23')
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px; letter-spacing: -0.2px;">Nora</div><div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 6px;">Friend &middot; since 2019 &middot; New York</div>', top=14)
    thumbs = '<div style="display: flex; gap: 6px; margin: 4px 0 8px 36px;">' + ''.join(ph(p, *fit(p, 52), 6, '') for p in SENT) + '</div>'
    inner += bar('SHARED WITH YOU') + gut('<div>' + entry('photo', 'From Pasta night', '2 photos &middot; Sunday', last=True) + '</div>' + thumbs)
    inner += bar('YOURS') + gut('<div>' + entry('photo', 'The table', 'Saturday 8:25 &middot; to Nora and Sam') + entry('photo', 'The Print Room', 'Thursday &middot; to friends', last=True) + '</div>')
    inner += bar('HELD IN COMMON') + gut('<div>' + entry('dining', 'Pasta night', 'Saturday Sep 19 &middot; at Nora&rsquo;s', last=True) + '</div>')
    inner += gut(door('Everything from Nora'), top=22)
    return phone(inner, 0, active='Life')

def withdraw_inset():
    one = lambda p: '<div style="display: flex; gap: 6px; margin: 4px 0 0 36px;">' + ph(p, *fit(p, 44), 6, '') + '</div>'
    body = (f'<div class="kickm">NORA TAKES THE LATE TABLE BACK, THURSDAY</div><div>{entry("photo", "From Pasta night", "1 photo, the pan &middot; Sunday", last=True)}</div>{one("PH-02")}'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2}; margin: 2px 0 0 36px;">In the viewer: <i>Your table photo &middot; 8:25, after this one</i></div>'
            f'<div class="kickm" style="margin-top: 6px;">IF ONLY THE PAN ARRIVED (10.2, PART WENT)</div><div>{entry("photo", "From Pasta night", "1 photo, the pan &middot; Sunday", last=True)}</div>'
            f'<div class="kickm" style="margin-top: 6px;">NORA TAKES BOTH BACK</div><div>{entry("photo", "The table", "Saturday 8:25 &middot; yours")}{entry("dining", "Pasta night", "held in common", last=True)}</div>')
    return inset('10.6, LATER STATES &middot; THE SAME ROWS', body,
                 'TITLES HERE ARE VESPER&rsquo;S, SO THEY DESCRIBE WHAT SURVIVES: THE EVENING AND A COUNT, NEVER A &ldquo;BEFORE AND AFTER&rdquo; WITH ONE SIDE GONE &middot; NORA&rsquo;S OWN WORDS, HAD SHE WRITTEN ANY, WOULD STAY AS WRITTEN &middot; NO GAP, TILE OR REGENERATED STAND-IN &middot; MAYA&rsquo;S TABLE AND THE EVENING STAY')

# ───────────────────────────── records ─────────────────────────────
FIX = [
    ['PH-01 = C1', 'Maya', 'Landscape', 'In the record; Maya&rsquo;s. Nora can look and reply, not send it on'],
    ['PH-02', 'Nora', 'Portrait', 'Sent to Maya, first'],
    ['PH-03', 'Nora', 'Portrait', 'The near-duplicate; in the record, left unselected, not a cleanup task'],
    ['PH-04', 'Nora', 'Landscape, low light', 'Sent to Maya, second; shown dark, as taken'],
    ['PH-05 = B2a', 'Dana', 'Portrait', 'In the record as Dana&rsquo;s contribution; not Nora&rsquo;s to send'],
    ['PH-06', 'Nora', 'Landscape', 'Not in this share: no camera data, unplaced in Life. Referenced in 10.5 as what A looks like'],
    ['PH-07', 'Nora', 'Portrait screenshot', 'Not used on this board'],
]
ROUTES = [
    ['Maya&rsquo;s Home, &ldquo;From Nora&rdquo;', 'The viewer at the tapped photo (10.4)', 'Home, same scroll position; the region unchanged'],
    ['Life &middot; People &middot; Nora, the shared row', 'The same viewer, same order', 'The same People row'],
    ['Nora&rsquo;s Photographs, Pasta night', 'Selection (10.1), then Share 2 (10.2)', 'Not now: same scroll, selection kept. Sent: selection cleared. Nothing went: stays on the share. Part went or not known: back, with only the undelivered picture still selected'],
    ['Reply, from the viewer', 'The reply field in place', 'The same photo; Nora gets the reply, nothing else'],
    ['&ldquo;Your table photo&rdquo;, in the viewer', 'Maya&rsquo;s own PH-01 in her own viewer', 'Back to Nora&rsquo;s set at the same photo'],
]
GAPS = [
    ['Asset', 'PH-01 to PH-07: no approved ordinary photographs exist (ledger &sect;10)', 'Stand-ins at real proportions; PH-04 dark because the picture is. Natural color, texture and noise cannot be judged until approved pictures replace them by ID'],
    ['Design', 'Life&rsquo;s viewer and collection anatomy (Life leads)', '10.4 is the minimum a receiver needs; reconcile with Life&rsquo;s proposal before any of it goes to the workbench'],
    ['Design', 'A shared-reader variant for a small set with no words', 'Drawn locally here; offered to the shared owner after reconciliation, with the casual-line question from the copy companion &sect;7'],
    ['Policy', 'Delivering a set of originals to one person', 'The two-photo share is a bounded design proposal under the unresolved collection-delivery agreement, not an adopted capability. The adopted agreement covers one exact original to a named recipient'],
    ['Policy', 'Friends audiences, guests, independent copies', 'Not adopted; the 08.2 Keep stays a proposal'],
    ['Policy', 'Until when a direct share shows', '&ldquo;Until you take them back&rdquo; is this board&rsquo;s proposed default; the author can still set an end'],
    ['Native verification', 'Pinch, swipe, caching, partial upload and retry, correction and withdrawal propagation', 'Engineering; nothing on this board establishes them'],
]
RULE = [
    ['Not now', 'Restored, exactly as chosen', 'Discarded; the line kept as a draft', 'Share again', 'Photographs, selecting, same place'],
    ['Nothing went', 'Kept underneath', 'Unchanged, with the line', 'Try again; Not now', 'The preview'],
    ['Part went', 'Released: the share used it', 'Only what didn&rsquo;t arrive', 'Send only that; Leave it', 'Photographs, notice, NOT SENT on the tile'],
    ['Not known yet', 'Released', 'The unknown picture, marked CHECKING', 'Check again (status, not resend); Leave it', 'Photographs'],
    ['Sent', 'Cleared', 'Empty', 'Nothing; findable in Life', 'Photographs, local confirmation; no Home task'],
]
COVER = [
    ['Send selected material', '10.1, 10.2, 10P', 'Drawn from Life&rsquo;s general selection; the ineligible picture is named at the preview; each ending returns by outcome; connected in 10P with simulated results', 'Social; selection is Life&rsquo;s', 'Asset; collection-delivery agreement'],
    ['Receive something complete', '10.3, 10.4', 'Drawn; opening and leaving is the ending', 'Social with Home', 'Asset; Life viewer reconciliation'],
    ['Keep a set coherent', '10.2 order, 10.3 pair, 10.4 position and per-photo author and time', 'Drawn', 'Social', 'None'],
    ['Add only justified help', '10.5', 'Compared on matched inputs; B selected for Home, C inside the viewer', 'Social', 'None'],
    ['Find it later without earning it', '10.6 and its later states', 'Drawn', 'Life &middot; People', 'Keep proposal (08.2) still open'],
]

def board10():
    P1 = [
        ('10.1', 'NORA', 'LIFE', select_phone(), ('SUNDAY SEP 20 &middot; 9:38 AM', 'LIFE 04b.11, COPIED &middot; SOCIAL BEGINS AT SHARE 2', 'Three selected, one of them Maya&rsquo;s; each action counts what it can reach', 'GENERAL SELECTION IS LIFE&rsquo;S &middot; SHARE 2, EXPORT 2, DELETE 2 &middot; NO TITLE, NO CAPTION, NO ALBUM &middot; THE NEAR-DUPLICATE IS SIMPLY LEFT'),
         ('Nora', 'Life &middot; the evening&rsquo;s photographs', 'Select, then Share 2', 'Her pictures chosen without sorting out whose is whose first', 'Nobody yet', 'Nora; Maya (PH-01); Dana (PH-05)', '&mdash;', 'Share 2; or Done'), ('SHARED &middot; .vdl-btn', 'COPIED FROM LIFE 04b.11; SHARE-SPECIFIC MODE BELOW', 'LEDGER &sect;10 &middot; PH-01&ndash;PH-05')),
        ('10.2', 'NORA', 'LIFE', share_phone(), ('9:40 AM', 'THE EXACT TWO, ONE PERSON, SEND', 'Two of her three selected go; Maya&rsquo;s own table is named, not silently dropped', 'THE PREVIEW IS WHAT GOES &middot; RECIPIENT FROM 09.1&rsquo;S CHOOSER &middot; NO PHOTO-LIBRARY PERMISSION, NO OCCASION CREATED'),
         ('Nora', 'Share 2, from her selection', 'Send', 'Two pictures of the evening to a friend who was there for the middle of it', 'Maya only; &ldquo;until you take them back&rdquo; PROPOSED', 'Contribution', 'Maya', 'By outcome (inset)'), ('SHARED &middot; .vdl-field, .vdl-recipient, .vdl-btn, Notice', 'A SET = BOUNDED PROPOSAL, NOT ADOPTED DELIVERY', 'LEDGER &sect;10 EVENT, SUN 9:40 AM')),
        ('10.3', 'MAYA', 'HOME', maya_home(), ('SUNDAY 10:05 AM', 'IT ARRIVES WHOLE', 'Both pictures first, whole and side by side; who and which evening; her Sunday goes on below', 'ONE ITEM, SO ONE REGION &middot; OPENING AND LEAVING IS THE ENDING &middot; PLACEMENT FOLLOWS 08.1&rsquo;S PROPOSAL'),
         ('Maya', 'Home, Sunday', 'Look; open', 'The evening before she came and after she left', 'Maya only', 'Contribution / Home', '&mdash;', 'Enjoy it and leave'), ('LIGHT CONTEXT, SELECTED IN 10.5', 'HOME 13 &middot; PERSONAL PICTURES UNTREATED', 'FIXTURE')),
        ('10.4', 'MAYA', 'HOME', viewer_phone(), ('10:06 AM', 'OPEN, BROWSE, REPLY IF SHE WANTS, CLOSE', 'One of two, with its own author and camera time; back to the same place on Home', 'OPENS DIRECTLY, NOT THROUGH LIFE &middot; THE ORDER IS NORA&rsquo;S &middot; A REPLY REACHES NORA ONLY'),
         ('Maya', 'The pair', 'Browse', 'The whole picture, at its own shape', 'Maya; a reply goes to Nora', 'Nora&rsquo;s originals', 'Nora, if she replies', 'Home, same position'), ('LOCAL &middot; MINIMUM VIEWER; LIFE LEADS THE ANATOMY', 'THE EARNED ROW (10.5 C) LIVES HERE', 'FIXTURE')),
    ]
    cols = [colu(ph_, cap(n, role, root, *c), under(r, s)) for n, role, root, ph_, c, r, s in P1]
    cols[0] = cols[0][:-6] + share_mode_inset() + '</div>'
    cols[1] = cols[1][:-6] + result_inset() + '</div>'
    cols[2] = cols[2][:-6] + large_inset() + '</div>'
    cols[3] = cols[3][:-6] + lowlight_inset() + '</div>'
    p6 = colu(maya_life(), cap('10.6', 'MAYA', 'LIFE', 'WEDNESDAY SEP 23', 'LATER, WITHOUT HAVING REPLIED', 'Findable while Nora shares them, beside what is Maya&rsquo;s own', 'NO REPLY OR UPLOAD FIRST &middot; FINDABLE WHILE SHARED IS NOT A COPY &middot; 08.3&rsquo;S GRAMMAR'),
              under(('Maya', 'Life &middot; People &middot; Nora', 'Open', 'The pair again, days later', 'Maya only', 'Life', '&mdash;', 'Open, or leave'), ('LIFE SEQUENCES &middot; RULED', 'REFIND OVER A PHOTO IS A DEPENDENCY (SEAM 7)', 'FIXTURE')))
    p6 = p6[:-6] + withdraw_inset() + '</div>'
    notes = [notecol('What board 10 shows', [
        ('ONE SET, END TO END', N('Life&rsquo;s fixture set, and its Sunday 9:40 share: Nora sends Maya the pan at 6:48, before anyone came, and the table at 10:40, after everyone left. Maya arrived at 8:05, so these are the parts of the evening she missed. They are worth something because of who sent them, with no line and no help from Vesper.')),
        ('WHAT IT REUSES', N('09.1&rsquo;s recipient chooser and 02&rsquo;s direct share; 08.1&ndash;08.3&rsquo;s receiving, opening and pull route; 04&rsquo;s later retrieval; 09.3&rsquo;s truthful results, plus the partial failure only a set can have.')),
        ('MIXED AUTHORS', N('The record holds Maya&rsquo;s table (PH-01) and Dana&rsquo;s dish (PH-05) beside Nora&rsquo;s own. In Life&rsquo;s general selection Nora can select Maya&rsquo;s with her own, and each action counts only what it can reach: Share 2. The preview then names the one left out. Starting from Share instead, only her own can be ticked. Neither mode grants anything.')),
        ('NO PHOTOGRAPHS YET', N('Every frame is a stand-in at the picture&rsquo;s real proportions with its ledger ID; PH-04 is dark because the real picture is. Nothing is drawn to pass for a friend&rsquo;s photograph. Approved pictures replace them by ID.')),
    ], w=430)]
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(cols) + ''.join(notes) + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">WHAT HELP THE ARRIVAL EARNS, AND FINDING IT LATER</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">The same arrival three ways; then Maya&rsquo;s Life on Wednesday</div></div>'
            + f'<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;"><div style="width: 1100px; flex: none;">{compare_block()}</div>{p6}</div>'
            + '<div style="height: 40px;"></div>' + blk('THE FIXTURE SET &middot; LIFE&rsquo;S, FROM THE SHARED LEDGER &sect;10 &middot; HOW THIS BOARD USES IT', tbl(['ID', 'AUTHOR', 'FRAMING', 'USE HERE'], FIX)
                + N('Life recorded the set first; Social reuses its IDs and its Sunday 9:40 event rather than keeping its own. <b>None is supplied.</b>'))
            + '<div style="height: 34px;"></div>' + blk('WHERE IT OPENS, AND WHERE IT RETURNS', tbl(['ORIGIN', 'OPENS', 'RETURNS TO'], ROUTES))
            + '<div style="height: 34px;"></div>' + blk('ONE OUTCOME RULE &middot; SOCIAL 10.2 AND 10P, OFFERED TO LIFE 04c', tbl(['OUTCOME', 'GENERAL SELECTION (LIFE)', 'PENDING SEND (SOCIAL)', 'OFFERED', 'LANDS ON'], RULE)
                + N('Life 04c currently keeps all three selected with Share 2 after every outcome, so a Share 2 after a partial send would send the pan again; 10P previously showed the pending picture as a one-item selection. Both are replaced by this rule, and Life&rsquo;s copied outcome frames and their text are Life&rsquo;s to update. A completed share leaves a local confirmation and is findable in Life; nothing on Nora&rsquo;s Home waits on Maya&rsquo;s reply.'))
            + '<div style="height: 34px;"></div>' + blk('GAPS, KEPT SEPARATE', tbl(['KIND', 'WHAT', 'STATUS'], GAPS))
            + '<div style="height: 34px;"></div>' + blk('COVERAGE &middot; SEPTEMBER 21 ASSIGNMENT', tbl(['ITEM', 'WHERE', 'STATUS', 'OWNER', 'REMAINING DEPENDENCY'], COVER)))
    return (HEAD_VDL + f'<div style="width: 2260px; min-height: {hh("10")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 10 &middot; PHOTOS, SENT AND RECEIVED &middot; {STAMP}', '10 &middot; Photos, sent and received',
                   'Casual photo sharing and receiving, the September 21 addition, on Life&rsquo;s fixture set; the two-photo share is a bounded design proposal, not an adopted delivery capability. On Sunday morning Nora picks two of her pictures from Saturday&rsquo;s pasta night and sends them to Maya. The same pair is followed from selection to the exact preview, Send and its result, Maya&rsquo;s Home, the viewer and back, and her Life a few days later, with the matched D5 comparison between. Maps, notes and recipes stay exchangeable as before; this board adds photographs without narrowing the exchange to them.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)

FILES = {'10 - Photos, sent and received': board10}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
