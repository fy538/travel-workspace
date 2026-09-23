"""September 21 export review of board 10: general vs Share-specific selection, outcome-specific return,
derived labels that survive a withdrawn or partial pair, and the set labelled a bounded proposal."""
import re
s = open('gen_c8.py').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
def swap_fn(name, nxt, new):
    global s
    i = s.index(f'def {name}('); j = s.index(nxt, i); s = s[:i] + new + s[j:]

rep("RECORD = ['PH-01', 'PH-02', 'PH-03', 'PH-04', 'PH-05']   # the evening's record, as Life lists it",
    "RECORD = ['PH-05', 'PH-02', 'PH-03', 'PH-01', 'PH-04']   # the evening's record in Life 04b's order (by time)\nGEN = ['PH-02', 'PH-01', 'PH-04']                        # Life 04b.11's general selection: three, one of them Maya's")

swap_fn('select_phone', '\n# ───────────────────────────── 10.2', '''def check():
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
    inner += gut('<div style="display: flex; align-items: center; gap: 10px; border-top: 1px solid rgba(27,23,20,0.12); padding-top: 14px;">'
                 f'<span style="font-size: 15px; font-weight: 600; color: {INK}; flex: 1;">3 selected</span>'
                 '<span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white);">Share 2</span>'
                 '<span class="vdl-btn secondary pill vk-t-labelSemibold">Export 2</span><span class="vdl-btn secondary pill vk-t-labelSemibold">Delete 2</span></div>', top=18)
    return phone(inner, 0, active='Life')

def share_mode_inset():
    body = (grid('share') + f'<div style="font-size: 13px; line-height: 19px; color: {INK2};">Maya&rsquo;s table and Dana&rsquo;s dish are theirs to share.</div>')
    return inset('10.1, THE OTHER MODE &middot; STARTED FROM SHARE', body,
                 'WHEN NORA BEGINS WITH SHARE, ONLY SHARE-ELIGIBLE PICTURES CAN BE TICKED; PH-01 AND PH-05 SHOW THEIR AUTHOR AND STAY VISIBLE &middot; THE GENERAL SELECTION ABOVE (LIFE 04b.11) KEEPS THE MIXED SET &middot; SELECTING OR SEEING A PICTURE GRANTS NOTHING')
''')

rep("SHARE &middot; 2 PHOTOS</span></div></div>'\n    inner += gut(f'<div style=\"width: 250px;\">{pair(250, 6, label=True)}</div><div class=\"fn\" style=\"color: {ANCHOR}; margin-top: 8px;\">IN THIS ORDER &middot; BOTH YOURS</div>', top=18)",
    "SHARE &middot; 2 OF YOUR 3</span></div></div>'\n    inner += (gut(notice, top=14) if notice else '')\n    inner += gut(f'<div style=\"width: 250px;\">{pair(250, 6, label=True)}</div><div class=\"fn\" style=\"color: {ANCHOR}; margin-top: 8px;\">IN THIS ORDER &middot; BOTH YOURS</div>'\n                 f'<div style=\"display: flex; align-items: center; gap: 10px; margin-top: 12px;\">{ph(\"PH-01\", *fit(\"PH-01\", 30), 5, \"\")}<span style=\"font-size: 13px; line-height: 18px; color: {INK2};\">Maya&rsquo;s table isn&rsquo;t in this share. It stays with the dinner.</span></div>', top=18)")
rep("def share_phone():", "def share_phone(notice=''):")

swap_fn('result_inset', '\n# ───────────────────────────── 10.3', '''def result_inset():
    """Return by outcome. Only a confirmed send clears the selection; every other ending keeps what Nora chose."""
    def lab(t): return f'<div class="kickm" style="margin-top: 4px;">{t}</div>'
    body = (lab('NOT NOW') + f'<div style="font-size: 13px; line-height: 18px; color: {INK2};">Back to Photographs, same scroll. The same three stay selected.</div>'
            + lab('SENT &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 64, tone='applied', title='Sent to Maya · 2 photos', body='Your selection is cleared.')
            + lab('NOTHING WENT &middot; STAYS ON THE SHARE') + dci('Notice', 120, tone='failed', title='Didn’t send. You’re offline.', body='Both photos and Maya are still here.', primary='Try again', secondary='Not now')
            + lab('PART WENT &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 120, tone='failed', title='The pan went. The late table didn’t.', body='Maya has the pan. The late table is still selected.', primary='Send the late table', secondary='Leave it')
            + lab('NOT KNOWN YET &middot; BACK TO PHOTOGRAPHS') + dci('Notice', 120, tone='unknown', title='Not sure the late table went', body='The pan reached Maya. Nothing is sent again until this is known.', primary='Check again', secondary='Leave it'))
    return inset('10.2, WHERE EACH ENDING RETURNS &middot; STATES OF THE SAME SLOT', body,
                 'SHARED &middot; Notice: applied, failed, unknown &middot; ONLY A CONFIRMED SEND CLEARS THE SELECTION &middot; EACH PICTURE KEEPS ITS OWN RESULT, SO A RETRY SENDS ONLY WHAT DIDN&rsquo;T ARRIVE &middot; SIMULATED IN 10P, NOTHING IS SENT')
''')

# derived labels: the evening plus a count, never "before and after"
rep("entry('photo', 'Pasta night, before and after', '2 photos &middot; Sunday', last=True)", "entry('photo', 'From Pasta night', '2 photos &middot; Sunday', last=True)")
swap_fn('withdraw_inset', '\n# ───────────────────────────── records', '''def withdraw_inset():
    one = lambda p: '<div style="display: flex; gap: 6px; margin: 4px 0 0 36px;">' + ph(p, *fit(p, 44), 6, '') + '</div>'
    body = (f'<div class="kickm">NORA TAKES THE LATE TABLE BACK, THURSDAY</div><div>{entry("photo", "From Pasta night", "1 photo, the pan &middot; Sunday", last=True)}</div>{one("PH-02")}'
            f'<div style="font-size: 12.5px; line-height: 17px; color: {INK2}; margin: 2px 0 0 36px;">In the viewer: <i>Your table photo &middot; 8:25, after this one</i></div>'
            f'<div class="kickm" style="margin-top: 6px;">IF ONLY THE PAN ARRIVED (10.2, PART WENT)</div><div>{entry("photo", "From Pasta night", "1 photo, the pan &middot; Sunday", last=True)}</div>'
            f'<div class="kickm" style="margin-top: 6px;">NORA TAKES BOTH BACK</div><div>{entry("photo", "The table", "Saturday 8:25 &middot; yours")}{entry("dining", "Pasta night", "held in common", last=True)}</div>')
    return inset('10.6, LATER STATES &middot; THE SAME ROWS', body,
                 'TITLES HERE ARE VESPER&rsquo;S, SO THEY DESCRIBE WHAT SURVIVES: THE EVENING AND A COUNT, NEVER A &ldquo;BEFORE AND AFTER&rdquo; WITH ONE SIDE GONE &middot; NORA&rsquo;S OWN WORDS, HAD SHE WRITTEN ANY, WOULD STAY AS WRITTEN &middot; NO GAP, TILE OR REGENERATED STAND-IN &middot; MAYA&rsquo;S TABLE AND THE EVENING STAY')
''')

# scope wording: a bounded proposal, consistently
rep("    ['Policy', 'Set delivery, Friends audiences, guests, independent copies', 'Not adopted. Only the narrow exact-original display to one named recipient is drawn; the 08.2 Keep stays a proposal'],",
    "    ['Policy', 'Delivering a set of originals to one person', 'The two-photo share is a bounded design proposal under the unresolved collection-delivery agreement, not an adopted capability. The adopted agreement covers one exact original to a named recipient'],\n"
    "    ['Policy', 'Friends audiences, guests, independent copies', 'Not adopted; the 08.2 Keep stays a proposal'],")
rep("('Nora', 'Her selection', 'Send', 'Two pictures of the evening to a friend who was there for the middle of it', 'Maya only, until Nora takes them back', 'Contribution', 'Maya', 'Back to the record, with the result'), ('SHARED &middot; .vdl-field, .vdl-recipient, .vdl-btn, Notice', 'T2 &middot; ONE CLEAR SEND', 'LEDGER &sect;10 EVENT, SUN 9:40 AM')),",
    "('Nora', 'Share 2, from her selection', 'Send', 'Two pictures of the evening to a friend who was there for the middle of it', 'Maya only; &ldquo;until you take them back&rdquo; PROPOSED', 'Contribution', 'Maya', 'By outcome (inset)'), ('SHARED &middot; .vdl-field, .vdl-recipient, .vdl-btn, Notice', 'A SET = BOUNDED PROPOSAL, NOT ADOPTED DELIVERY', 'LEDGER &sect;10 EVENT, SUN 9:40 AM')),")
rep("('10.2', 'NORA', 'LIFE', share_phone(), ('9:40 AM', 'THE EXACT SELECTION, ONE PERSON, SEND', 'The two in order, an optional line left empty, Maya, and until when',",
    "('10.2', 'NORA', 'LIFE', share_phone(), ('9:40 AM', 'THE EXACT TWO, ONE PERSON, SEND', 'Two of her three selected go; Maya&rsquo;s own table is named, not silently dropped',")
rep("('10.1', 'NORA', 'LIFE', select_phone(), ('SUNDAY SEP 20 &middot; 9:38 AM', 'CHOOSE A FEW, IN THE EVENING&rsquo;S OWN RECORD', 'Two of her pictures; Maya&rsquo;s and Dana&rsquo;s stay theirs', 'LIFE&rsquo;S SELECTION DONOR &middot; NO TITLE, NO CAPTION, NO ALBUM &middot; THE NEAR-DUPLICATE IS SIMPLY LEFT'),\n         ('Nora', 'Life &middot; the evening&rsquo;s record', 'Select', 'Two of her own pictures, chosen', 'Nobody yet', 'Nora; Maya (PH-01); Dana (PH-05)', '&mdash;', 'Share; or cancel'), ('SHARED &middot; .vdl-btn', 'LOCAL &middot; SELECTION GRID FOLLOWS LIFE&rsquo;S DONOR', 'LEDGER &sect;10 &middot; PH-01&ndash;PH-05')),",
    "('10.1', 'NORA', 'LIFE', select_phone(), ('SUNDAY SEP 20 &middot; 9:38 AM', 'LIFE 04b.11, COPIED &middot; SOCIAL BEGINS AT SHARE 2', 'Three selected, one of them Maya&rsquo;s; each action counts what it can reach', 'GENERAL SELECTION IS LIFE&rsquo;S &middot; SHARE 2, EXPORT 2, DELETE 2 &middot; NO TITLE, NO CAPTION, NO ALBUM &middot; THE NEAR-DUPLICATE IS SIMPLY LEFT'),\n         ('Nora', 'Life &middot; the evening&rsquo;s photographs', 'Select, then Share 2', 'Her pictures chosen without sorting out whose is whose first', 'Nobody yet', 'Nora; Maya (PH-01); Dana (PH-05)', '&mdash;', 'Share 2; or Done'), ('SHARED &middot; .vdl-btn', 'COPIED FROM LIFE 04b.11; SHARE-SPECIFIC MODE BELOW', 'LEDGER &sect;10 &middot; PH-01&ndash;PH-05')),")
rep("    cols[1] = cols[1][:-6] + result_inset() + '</div>'", "    cols[0] = cols[0][:-6] + share_mode_inset() + '</div>'\n    cols[1] = cols[1][:-6] + result_inset() + '</div>'")
rep("    ['Nora&rsquo;s record, Pasta night', 'Selection (10.1), then Social&rsquo;s share (10.2)', 'The record, selection cleared, with the result (10.2)'],",
    "    ['Nora&rsquo;s Photographs, Pasta night', 'Selection (10.1), then Share 2 (10.2)', 'Not now: same scroll, selection kept. Sent: selection cleared. Nothing went: stays on the share. Part went or not known: back, with only the undelivered picture still selected'],")
rep("    ['Send selected material', '10.1, 10.2', 'Drawn; words optional and left empty', 'Social; selection donor from Life', 'Asset'],",
    "    ['Send selected material', '10.1, 10.2, 10P', 'Drawn from Life&rsquo;s general selection; the ineligible picture is named at the preview; each ending returns by outcome; connected in 10P with simulated results', 'Social; selection is Life&rsquo;s', 'Asset; collection-delivery agreement'],")
rep("'Casual photo sharing and receiving, the September 21 addition, on Life&rsquo;s fixture set.", "'Casual photo sharing and receiving, the September 21 addition, on Life&rsquo;s fixture set; the two-photo share is a bounded design proposal, not an adopted delivery capability.")
open('gen_c8.py', 'w').write(s); print('patched')
