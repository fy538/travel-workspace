"""Artifact-led visual value pass (handoff 2026-09-05). A small family of recognizable forms —
held-object instrument, prepared possibility as a sequence, authored contribution with its place,
comparison / paired evidence, usable method, evidence-backed reconstruction — applied to complete
Home scrolls (02, 03, 04), two bounded Places continuations (06), a ledger reconciliation (07),
a priority comparison and a waiting-window treatment (08 row four), and a selected-form sheet (09)
with large-text renders. Same fixture world as every other board. Nothing here is ruled."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
import gen_home as gh
import gen_generous3 as g3
import gen_generous4 as g4
import gen_generous5 as g5
import gen_merge as gm
import gen_seam as gs
from gen_generous import caption, col, head, FOOT, N, WEEK_SUN, ending, arow, facepile, compare2, collapsed, span, photo, callouts, body
from gen_generous3 import sect, meta, title, sup, gut, u2, card, handoff_card, fact, reading_card, kept_row, COLD, author_row
from gen_generous4 import ways_card, h1_floor
from gen_merge import page, daycap, tbl, blk, hh, STAMP
from gen_seam import mark, chip, row_mark, kept_chip_row, pass_admission, live_pass_crown, G, VIOLET, HAIR, HAIRT
from gen_places import scope_header, map_wash, places_phone

OUT = gm.OUT
PASS = 'ARTIFACT-LED PASS 2026-09-05'
G['book'] = 'M2.5 3 H6.5 Q7.5 3 7.5 4 V12.5 Q7.5 11.5 6.5 11.5 H2.5 Z M12.5 3 H8.5 Q7.5 3 7.5 4 V12.5 Q7.5 11.5 8.5 11.5 H12.5 Z'
G['photo'] = 'M2.5 5 H5 L6.2 3.2 H8.8 L10 5 H12.5 V12 H2.5 Z M7.5 10.2 A2.2 2.2 0 1 0 7.5 5.8 A2.2 2.2 0 1 0 7.5 10.2'
G['note'] = 'M3.5 2.5 H11.5 V12.5 H3.5 Z M5.5 5.5 H9.5 M5.5 8 H8.5'

# ───────────────────────────── the forms ─────────────────────────────
def seq_strip(stops, top=10):
    """Prepared possibility as a sequence: time · node on a gold line · title · one practical detail · the leg between. Order is the explanation."""
    out = f'<div style="display: flex; flex-direction: column; margin-top: {top}px;">'
    n = len(stops)
    for i, (t, name, detail, leg) in enumerate(stops):
        last = i == n - 1
        out += ('<div style="display: flex; gap: 12px; align-items: stretch;">'
                f'<div style="width: 44px; flex: none; text-align: right;"><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.8px; color: {INK}; line-height: 21px;">{t}</span></div>'
                f'<div style="width: 12px; flex: none; display: flex; flex-direction: column; align-items: center;"><span style="width: 9px; height: 9px; border-radius: 5px; background: {GOLD}; flex: none; margin-top: 6px;"></span>'
                + ('' if last else f'<span style="width: 2px; flex: 1; background: {GOLD}; opacity: 0.55; margin: 3px 0;"></span>') + '</div>'
                f'<div style="flex: 1; min-width: 0; padding-bottom: {0 if last else 12}px;">{title(name, 16, 21)}{sup(detail)}'
                + (f'<div class="fn" style="color: {ANCHOR}; margin-top: 4px;">{leg}</div>' if leg else '') + '</div></div>')
    return out + '</div>'

def ways_seq_card(t, stops, alts=(), meta_t='', lead_meta=''):
    inner = title(t, 20, 25, 600)
    if lead_meta: inner += meta(lead_meta, 4)
    inner += seq_strip(stops)
    for a, when in alts:
        inner += (f'<div style="display: flex; align-items: center; gap: 10px; margin: 10px 0 2px 0;"><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span><span class="fn" style="color: {ANCHOR};">OR</span><span style="flex: 1; height: 1px; background: rgba(27,23,20,0.08);"></span></div>'
                  f'<div style="padding: 4px 0 2px 0;">{title(a, 16, 21)}<div class="fn" style="color: {ANCHOR}; margin-top: 3px;">{when}</div></div>')
    if meta_t: inner += meta(meta_t, 10)
    return card(inner)

def place_ident(kind, name, line):
    """The place a contribution is about, as one identity strip inside the unit: mark · serif name · one useful line."""
    return (f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(27,23,20,0.07);">{mark(kind, 15, 0.7)}'
            f'<div style="flex: 1; min-width: 0;"><div style="{SERIF} font-size: 16px; line-height: 20px; font-weight: 600; color: {INK};">{name}</div><div class="fn" style="color: {ANCHOR}; margin-top: 2px;">{line}</div></div></div>')

def handoff_artifact(letter, who, when, words, kind, place, line, door_text):
    inner = author_row(letter, who, when) + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 10px;">&ldquo;{words}&rdquo;</div>' + place_ident(kind, place, line) + door(door_text)
    return card(inner)

def paired_evidence(t, text, items, meta_t='', door_text=None):
    """Comparison as paired evidence: quoted excerpts each with the scale or side it belongs to. Bare (canon: findings stay bare)."""
    rows = ''
    for label, quote, scale in items:
        rows += (f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 9px 0; border-top: 1px solid rgba(27,23,20,0.07);">'
                 f'<div style="flex: 1; min-width: 0;"><div style="{SERIF} font-size: 16px; line-height: 21px; color: {INK};">&ldquo;{quote}&rdquo;</div><div class="fn" style="color: {ANCHOR}; margin-top: 3px;">{label}</div></div>'
                 f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {GOLDD}; flex: none; padding-top: 4px; text-align: right;">{scale}</span></div>')
    return u2(t, text, f'<div style="margin-top: 8px; border-bottom: 1px solid rgba(27,23,20,0.07);">{rows}</div>', meta_t=meta_t, door_text=door_text)

def method(t, steps, meta_t='', door_text=None, carded=False):
    """Usable method: a concrete answer without a conversation. Bare by default; the carded variant is the flagged amendment on 09."""
    st = '<div style="display: flex; flex-direction: column; gap: 6px; margin-top: 8px;">' + ''.join(
        f'<div style="display: flex; gap: 12px; align-items: baseline;"><span style="{SERIF} font-size: 18px; font-weight: 600; color: {GOLDD}; width: 16px; flex: none;">{i + 1}</span><span style="font-size: 14px; line-height: 19px; color: {INK};">{s}</span></div>' for i, s in enumerate(steps)) + '</div>'
    inner = u2(t, '', st, meta_t=meta_t, door_text=door_text)
    return card(inner) if carded else inner

def recon_strip(events, meta_t='', door_text=None, t=None, text=''):
    """Evidence-backed reconstruction: a horizontal strip whose marks ARE the evidence (a ticket, photographs); a hatched span where there is none."""
    n = len(events)
    cells = ''
    for i, (time_, kind, label, gap_after) in enumerate(events):
        node = (f'<span style="width: 30px; height: 22px; border-radius: 4px; background: #2A241E; display: inline-block;"></span>' if kind == 'photo'
                else f'<span style="width: 26px; height: 26px; border-radius: 13px; border: 1.3px solid {INK}; display: inline-flex; align-items: center; justify-content: center; box-sizing: border-box; background: {CARD};">{mark(kind, 13, 0.8)}</span>')
        cells += (f'<div style="width: 58px; flex: none; display: flex; flex-direction: column; align-items: center; gap: 3px;"><span style="height: 26px; display: flex; align-items: center;">{node}</span>'
                  f'<span style="{MONO} font-size: 10px; font-weight: 700; color: {INK};">{time_}</span><span class="fn" style="color: {ANCHOR}; white-space: nowrap; font-size: 9px;">{label}</span></div>')
        if i < n - 1:
            if gap_after:
                cells += f'<div style="flex: 3; display: flex; flex-direction: column; align-items: center; gap: 4px; padding-top: 12px; min-width: 0;"><span style="width: 100%; height: 2px; background: repeating-linear-gradient(90deg, rgba(27,23,20,0.25) 0 4px, transparent 4px 8px);"></span><span class="fn" style="color: {GHOST}; white-space: nowrap; font-size: 9px;">{gap_after}</span></div>'
            else:
                cells += f'<div style="flex: 1; padding-top: 12px; min-width: 0;"><span style="display: block; width: 100%; height: 2px; background: {GOLD};"></span></div>'
    strip = f'<div style="display: flex; align-items: flex-start; margin-top: 10px;">{cells}</div>'
    return u2(t, text, strip, meta_t=meta_t, door_text=door_text) if t else strip

def large(html, k=1.3):
    """Larger text: multiply every CSS font-size and line-height in the phone; widths unchanged, so the page must reflow."""
    html = re.sub(r'font-size: (\d+(?:\.\d+)?)px', lambda m: f'font-size: {float(m.group(1)) * k:.1f}px', html)
    html = re.sub(r'line-height: (\d+(?:\.\d+)?)px', lambda m: f'line-height: {float(m.group(1)) * k:.1f}px', html)
    return html

# ───────────────────────────── 02 · Persona A, artifact-led ─────────────────────────────
def sunday_after():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '9:10 AM')
    inner += orientation('Clear and cold. Low water at 1:40.', '54&deg; by noon &middot; Alex&rsquo;s birthday and Dana on Saturday &middot; the show Friday.')
    inner += gut(ways_seq_card('Today, in order', [
        ('10:30', 'The sesame loaf', 'Maya, Friday: &ldquo;Sundays only &mdash; go before eleven or it&rsquo;s gone.&rdquo; Open now.', '9 MIN BY BIKE TO THE PIER'),
        ('1:40', 'Low water on the pier', 'The flood line, walked: the granite kerbs show where the gates&rsquo; protection ends. Until four.', ''),
    ], alts=[('Stay in: the skillet, preheated dry', 'TONIGHT &middot; THE METHOD IS BELOW')], meta_t='ONE RIDE, TWO THINGS THAT ONLY HAPPEN TODAY &middot; MAYA&rsquo;S SHARE, IN PLACES &middot; TIDE TABLE'), top=22)
    inner += sect('In motion') + gut(arow('Alex&rsquo;s birthday &middot; Saturday evening &middot; <span style="color: #6E6862;">4 going &middot; place still his to pick</span>', avatars=['A', 'M', 'you'])
                                     + arow('Dana &middot; lands Saturday the 19th &middot; <span style="color: #6E6862;">Sunday morning is hers</span>', avatars=['D'])
                                     + row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>')
                                     + row('Dentist &middot; Tuesday 9:00 &middot; <span style="color: #6E6862;">24&deg; &middot; walk, the bus is slower</span>', mark='dashed', last=True))
    inner += sect('Worth knowing') + gut(COLD())
    inner += gut(method('The crust split where the pan was coldest. Heat the skillet dry first.', [
        'Four minutes dry, on high, before any oil.', 'Then oil, then dough; the edge sets before the middle steams.', 'Lid on for the last minute if the top is pale.'],
        meta_t='FROM YOUR THURSDAY NOTE &middot; A GENERAL TECHNIQUE, SELECTED BECAUSE OF IT'), top=26)
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none. The pump station under the park is on the list.', last=True) + '</div>')
    inner += gut(reading_card('THE HARBOR BOOK &middot; CH. 4 &middot; 4 MIN', 'The pumps under the park finish what the gates cannot', 'The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.', 'Read the chapter'), top=26)
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS', 0), top=32)
    inner += ending(WEEK_SUN, 'Friday the show. Saturday, Alex&rsquo;s birthday.')
    return phone(inner, 0)

def monday_after():
    inner = g3.h2_read() + gut(g3.alex_card(), top=22) + g5.rows_A5(with_alex=False).replace(
        row('The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted &middot; Maya sent a place for after</span>', mark='solid', color=GOLD),
        row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted &middot; Maya sent a place for after</span>'))
    inner += sect('This week') + gut(g3.market_card())
    inner += sect('Addressed to you') + gut('<div style="display: flex; flex-direction: column; gap: 16px;">'
        + handoff_artifact('D', 'Dana', 'THURSDAY &middot; TO YOU', 'This one, for Sunday? I want the poetry shelf in the back.', 'book', 'A used bookshop on Court Street', 'OPENS 11 &middot; SIX MINUTES FROM THE BAKERY MAYA SHARED', 'The bookshop')
        + handoff_artifact('M', 'Maya', 'SATURDAY &middot; TO YOU', 'This one after the show, it&rsquo;s open till one and you won&rsquo;t need a table.', 'dining', 'The noodle bar', 'THREE BLOCKS FROM THE HALL &middot; OPEN TILL 1 &middot; NO TABLES, A COUNTER', 'The noodle bar')
        + '</div>')
    inner += gut(door('What your friends have shared') + meta('PLACES &middot; FROM FRIENDS &middot; THE CASUAL SHARES, ON THE MAP', 0), top=20)
    inner += sect('Worth knowing') + gut(COLD())
    inner += g5.END_MON()
    return phone(inner, 0)

def persona_a_board():
    row1 = [col(g5.h1v5(), daycap('SUNDAY 9:10 &middot; QUIET', '1 &middot; BEFORE &middot; REVISION 5', 'The generous Sunday as it stood', 'ALTERNATIVES CARD &middot; ROWS &middot; THE COLD &middot; ONE CITY FACT')),
            col(sunday_after(), daycap('SUNDAY 9:10 &middot; QUIET', '2 &middot; AFTER &middot; ARTIFACT-LED', 'The possibility is a sequence; the show wears its mark', 'ORDER EXPLAINS ITSELF &middot; A USABLE METHOD &middot; READING RESTORED AS DEPTH')),
            col(h1_floor(), daycap('SUNDAY 9:10 &middot; QUIET', '3 &middot; THE FLOOR', 'What the first account will see', 'UNCHANGED &middot; ONLY WHAT REAL OWNERS SERVE TODAY')),
            col(g5.h2v5_t2(), daycap('MONDAY 6:40 &middot; SOCIAL', '4 &middot; BEFORE &middot; REVISION 5', 'Addressed to you, as it stood', 'THE HANDOFF CARDS NAME THE PLACE IN METADATA')),
            col(monday_after(), daycap('MONDAY 6:40 &middot; SOCIAL', '5 &middot; AFTER &middot; ARTIFACT-LED', 'The place is integral to the contribution', 'HER WORDS &middot; THE PLACE&rsquo;S IDENTITY STRIP &middot; ONE USEFUL LINE &middot; THE DOOR')),
            col(g3.h2v2_sparse(), daycap('MONDAY 6:40 &middot; SPARSE', '6 &middot; NOTHING ADDRESSED', 'Only Dana this week', 'NO REGION, NO EMPTY MODULE, NO INVITE &middot; UNCHANGED'))]
    row2 = [col(g3.h4v2_before(), daycap('THURSDAY 5:40', '7 &middot; BEFORE', 'The fuller Thursday', 'UNCHANGED')),
            col(g3.h4v2_during(), daycap('THURSDAY 6:05 &middot; PRIORITY', '8 &middot; DURING', 'One decision, 55 minutes', 'UNCHANGED &middot; SEE 08 ROW FOUR FOR THE PRIORITY COMPARISON')),
            col(g3.h4v2_after(), daycap('THURSDAY 7:25', '9 &middot; AFTER', 'The fuller Home returns', 'UNCHANGED')),
            col(g3.life_frame(), daycap('BEHIND THE DOOR', '10 &middot; THE RECORD', 'Life &middot; People', 'UNCHANGED')),
            notecol('What the forms changed on Sunday and Monday', [
                ('SUNDAY', N('The prepared possibility became a sequence: two times, two stops, the leg between them, one practical detail each. Order is the explanation; the &ldquo;or&rdquo; keeps the alternative. The skillet returned as a usable method (three steps, no prose), and the reading preview returned as depth. Both had lost the August 29 deletion test as prose units; as forms they carry a different job each, so the repetition penalty no longer applies. The show row wears its mark (ruled 09-05).')),
                ('MONDAY', N('Each addressed contribution now carries the place it is about as an identity strip inside the card: mark, name, one useful line (hours, distance). Before, the place lived in a mono metadata line. Nothing else moved; Treatment 2 and its condition stand.')),
                ('NOT CHANGED', N('Thursday&rsquo;s three phones, the sparse Monday, the floor, and the record. The priority behaviour is compared on 08 row four, not here.')),
                ('DIAGNOSTICS', N('See 07 for visible words and scroll heights, before and after. The after phones are longer by design; the brief asks for a generous page.')),
            ], w=560)]
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);"><div class="kick" style="color: {GOLDD};">THURSDAY &middot; THE PRIORITY &middot; UNCHANGED ON THIS BOARD</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 18px;">' + ''.join(row2) + '</div>')
    html = page(2620, hh('02'), f'VESPER &middot; HOME &middot; 02 &middot; PERSONA A &middot; THE NEW YORKER &middot; {PASS} &middot; {STAMP}', '02 &middot; Persona A &middot; the New Yorker, before and after the forms',
                'Same evidence, same week. Sunday and Monday drawn twice: as they stood at revision 5, and with the recognizable forms applied (a sequence for the possibility, a method, a reading preview, the place inside the contribution, the mark on the ticket row). Thursday, the floor, the sparse Monday, and the record are unchanged.', row1)
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

# ───────────────────────────── 03 · Persona B, artifact-led ─────────────────────────────
MENUS = paired_evidence('The two menus used &ldquo;local&rdquo; at three different scales', 'The word stayed while the geography widened. Worth knowing before Saturday&rsquo;s dinner, where the same word will come up.', [
    ('THE COURTYARD MENU &middot; SORRENTO &middot; PHOTOGRAPHED TUE', 'local herbs, from the garden', 'THE GARDEN'),
    ('THE COURTYARD MENU &middot; SORRENTO', 'local lemons', 'THE PENINSULA'),
    ('THE HARBOR MENU &middot; AMALFI &middot; PHOTOGRAPHED THU', 'local catch', 'THE COAST'),
], meta_t='FROM TWO MENUS YOU KEPT &middot; SOURCE WORDING PRESERVED', door_text='See the menus together')

def dayzero_after():
    inner = anchor_row('NEW YORK &middot; SUNDAY', '11:20 AM') + orientation('Home. Clear, 64&deg;, low water at 2:40.', 'Landed 6:40 &middot; Saturday is dinner with Maya and Alex.')
    inner += gut(ways_card('This afternoon', [
        ('The pier at low water', 'The first walk back can be the one you know. Low water 2:40 to 5.', 'LOW WATER 2:40&ndash;5'),
        ('Cook the Sorrento dish', 'The method is below; forty minutes, one pan.', 'TONIGHT, OR SATURDAY FOR MAYA AND ALEX'),
        ('Stay in', 'The noodle shop delivers until ten.', 'ANY TIME'),
    ], 'PHOTOS IMPORTING &middot; 412 OF 690'), top=22)
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled &middot; Maya added a photograph Friday</span>', avatars=['M', 'A', 'you'])
                                     + row_mark('flight', 'Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', last=True))
    inner += sect('Worth knowing') + gut(u2('To get the texture you photographed, finish the pasta in the sauce',
        'The film that holds the ridges is a starch emulsion. That is consistent with your photograph. What that kitchen actually did is not known.',
        photo(150, 'YOUR PHOTOGRAPH &middot; SORRENTO &middot; SLOT', [('1', 18, 18), ('2', 300, 84)]) + callouts([('1', 'Film, not pool.'), ('2', 'Integrated at service, not added after.')]),
        meta_t='YOUR PHOTOGRAPH &middot; SORRENTO, LAST TUESDAY'))
    inner += gut(method('The method, for one pan', ['Pull the pasta ninety seconds early; keep a ladle of the water.', 'Into the sauce over heat, with the ladle; toss until the film holds the ridges.', 'Off the heat before it tightens; it keeps tightening on the plate.'],
                        meta_t='A GENERAL TECHNIQUE, SELECTED BECAUSE OF YOUR PHOTOGRAPH', door_text='The whole method'), top=22)
    inner += sect('From the trip') + gut(recon_strip([('9:10', 'ferry', 'TICKET', ''), ('9:14', 'photo', 'HARBOR', ''), ('10:02', 'photo', 'THE QUAY', 'NOTHING KEPT'), ('1:20', 'photo', 'THE STEPS', '')],
        t='Sorrento to Amalfi by ferry: the harbor at 9:14, the quay by 10:02', text='The morning you left the peninsula, from your ticket and three photographs. The rest fills in as photos import; gaps stay gaps.',
        meta_t='TICKET 9:10 &middot; PHOTOGRAPHS 9:14, 10:02, 1:20 &middot; 412 OF 690 IMPORTED', door_text='The trip, in Life'))
    inner += gut(MENUS, top=26)
    inner += sect('The city this week') + gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon.', last=True) + '</div>')
    inner += ending([('SUN', dm('solid', INK), 'today', INK), ('MON', dm('hollow', ''), 'market', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE), ('SAT', dm('av:M', ''), 'dinner', INK)],
                    'Saturday, dinner with Maya and Alex.')
    return phone(inner, 0)

def friday_wait():
    """03 phone 2 brought to the current direction: the temporal posture as a crown with no ask; the hidden system as a bare passage; the capability return as a bare unit with its door; the seam instead of a coda."""
    inner = anchor_row('NEW YORK &middot; FRIDAY', '9:05 AM')
    inner += orientation('Saturday stays open. The heat decides at noon.', 'The waterfront start and the indoor continuation both hold until the noon forecast.')
    inner += crown(PLAN, 'WAIT FOR SIGNAL &middot; FORECAST AT NOON', 'Wait until noon', 'Neither path needs booking before then.',
                   f'<div style="border-top: 1px solid rgba(27,23,20,0.06); padding-top: 10px; margin-top: 6px;"><div class="fn" style="color: {ANCHOR};">IF THE HOTTER BRANCH HOLDS</div><div style="font-size: 14px; line-height: 19px; margin-top: 4px;">Start after 5:30 &middot; shaded approach &middot; indoor continuation near the return</div></div>'
                   f'<div style="{SERIF} font-style: italic; font-size: 16px; line-height: 23px; color: {MUTE}; margin-top: 8px;">I&rsquo;m watching the noon forecast. Unless the branch changes, you won&rsquo;t hear about this again.</div>',
                   cta=None, fn='NEXT CHANGE: THE NOON FORECAST &middot; THE MONITOR EXPIRES WITH THE WINDOW')
    inner += sect('In motion') + gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled</span>', avatars=['M', 'A', 'you'])
                                     + row_mark('flight', 'Return flight refund claim &middot; <span style="color: #6E6862;">airline reviewing</span>', last=True))
    inner += sect('Worth knowing') + gut(u2('Night does not cool every street at the same rate', 'The streets that face the water lose their heat first; the deep cross-streets, walled in masonry, give theirs back for hours. The difference is not the temperature the forecast prints. It is the material under your feet and the air that can or cannot move.',
                                            meta_t='A BOUNDED MECHANISM, ONE SOURCE &middot; IT NEVER CLAIMS MORE THAN THE SOURCE SUPPORTS'))
    inner += gut(u2('Resolve the physical burden first; let interpretation return after', 'Route, shade, water, and a stopping point, then the rest. What Rome taught, applied to a Saturday here.', meta_t='FROM THE ROME DAYS &middot; A CAPABILITY, NOT A MEANING', door_text='Saturday, in Places'), top=26)
    inner += ending([('FRI', dm('solid', INK), 'today', INK), ('SAT', dm('dashed', MUTE), 'noon?', MUTE), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('hollow', ''), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Noon will tell you. Until then, nothing.')
    return phone(inner, 0)

def saturday_evidence():
    """03 phone 3 brought to the current direction: the photograph is the held object, so it is carded; the test and the caution stay bare; the seam ends the page."""
    inner = anchor_row('NEW YORK &middot; SATURDAY', '10:15 AM')
    inner += orientation('A slow weekend. One question from Sorrento.', 'Clear, 64&deg; &middot; nothing on the calendar until Tuesday.')
    inner += gut(card(u2('The last minute may explain more than the ingredient list', 'The cues are consistent with a starch-supported emulsion and pan finishing. They do not prove how this kitchen prepared the dish.',
        photo(190, 'YOUR PHOTOGRAPH &middot; SORRENTO &middot; SLOT', [('1', 18, 18), ('2', 300, 120)]) + callouts([('1', 'Sauce clings as a thin film rather than pooling.'), ('2', 'The finish looks integrated at service, not added afterward.')]),
        meta_t='YOUR OBSERVATION &middot; ONE SOURCE PER MECHANISM', door_text='See the evidence and alternatives')), top=22)
    inner += sect('One way to test it in New York') + gut(u2('Compare when the sauce and pasta come together, not which ingredients are listed', 'A nearby kitchen makes the process observable this weekend; no reservation is required.', meta_t='A CURRENT POSSIBILITY &middot; FIXTURE', door_text='Open the dish in Places'))
    inner += sect('Worth knowing') + gut(u2('&ldquo;Authentic&rdquo; is too blunt for this question', 'Regional practice, restaurant service, ingredient supply, and New York&rsquo;s own Italian and Italian-American histories produce different textures without one becoming the standard.', meta_t='APPEARS ONLY WITH SOURCES AND POSITIONED PERSPECTIVES'))
    inner += ending([('SAT', dm('solid', INK), 'today', INK), ('SUN', dm('hollow', ''), '', MUTE), ('MON', dm('hollow', ''), '', MUTE), ('TUE', dm('dashed', MUTE), '', MUTE), ('WED', dm('hollow', ''), '', MUTE), ('THU', dm('hollow', ''), '', MUTE), ('FRI', dm('hollow', ''), '', MUTE)],
                    'Nothing until Tuesday.')
    return phone(inner, 0)

def persona_b_board():
    cols = [col(g4.h5v4(), daycap('SUNDAY 11:20 &middot; LANDED', '1 &middot; BEFORE &middot; REVISION 4', 'Day zero as it stood', 'ALTERNATIVES &middot; THE DISH AS A FINDING &middot; THE FERRY MORNING AS A LINE')),
            col(dayzero_after(), daycap('SUNDAY 11:20 &middot; LANDED', '2 &middot; AFTER &middot; ARTIFACT-LED', 'A method, a reconstruction with its evidence, a comparison', 'THE PHOTO FINDING &middot; THREE STEPS &middot; THE STRIP&rsquo;S MARKS ARE THE EVIDENCE &middot; THE MENUS')),
            col(friday_wait(), daycap('FRIDAY 9:05 &middot; AVAILABLE', '3 &middot; WAIT UNTIL NOON &middot; REDRAWN', 'The temporal posture, in the current direction', 'NO ASK &middot; BARE MECHANISM &middot; THE SEAM, NOT A CODA')),
            col(saturday_evidence(), daycap('SATURDAY 10:15 &middot; AVAILABLE', '4 &middot; THE DISH, AS EVIDENCE &middot; REDRAWN', 'The photograph is the held object', 'CARDED BECAUSE IT IS AN OBJECT &middot; THE TEST AND THE CAUTION STAY BARE'))]
    notes = [notecol('Coming home, with the forms', [
                ('DAY ZERO', N('The photograph finding stays bare; beneath it a usable method (three steps) answers the question the finding raises, without a conversation. The ferry morning is drawn as a strip whose marks are the evidence itself: a ticket at 9:10, photographs at 9:14, 10:02 and 1:20, a hatched span where nothing was kept. The menus comparison is the one thing on the page the person had not noticed: the same word at three scales, quoted from two menus they photographed.')),
                ('SEAT LAW', N('The menus comparison is Life&rsquo;s adopted Return (Life board 25). While Home delivers it, Life&rsquo;s Return is absent. It appears here because Saturday&rsquo;s dinner makes it timely; on a week without that dinner it stays in Life.')),
                ('PHONES 3 AND 4', N('Brought to the current direction, not merely retyped: the temporal posture keeps its one voice line and no ask; the hidden system is a bare passage with its source line; the capability return is a bare unit with a door to Places; both end on the seam. Saturday cards the photograph because it is a held object; the test and the caution stay bare.')),
                ('NOT A TASK', N('No phone asks the person to cook, reflect, or rest. The method is available; the dinner is settled; the seam names it and nothing else.')),
             ], w=560),
             notecol('Sources and what is claimed', [
                ('THE MENUS', N('Two photographed menus (fixture). Every quoted line is a fixture; the claim is only that one word appears at three scales. No dish, price, or provenance is asserted.')),
                ('THE FERRY MORNING', N('A ticket proves purchase and a scheduled departure; the photographs carry the arrival. The strip never says &ldquo;you boarded&rdquo;; it says what was kept and when.')),
                ('THE METHOD', N('A general technique, retrieved because of the photograph. The photograph does not prove the kitchen used it. The method is usable regardless.')),
             ], w=560)]
    return page(1820, hh('03'), f'VESPER &middot; HOME &middot; 03 &middot; PERSONA B &middot; BACK FROM EUROPE &middot; {PASS} &middot; {STAMP}', '03 &middot; Persona B &middot; back from Europe, with the forms',
                'Day zero before and after; then the two baseline states no revision had reached, now drawn in the current direction. One useful travel-derived result at a time, beside forward-looking New York life.', cols, notes)

# ───────────────────────────── 04 · Persona C, thin-context check ─────────────────────────────
def first_open_after():
    html = gs.first_open_seam()
    old = ('<div>' + row('A photograph of a dish &rarr; <span style="color: #6E6862;">the mechanism behind its texture</span>', mark='hollow')
           + row('A friend&rsquo;s note &rarr; <span style="color: #6E6862;">a better window for the same place</span>', mark='hollow')
           + row('Scattered tickets and photos &rarr; <span style="color: #6E6862;">one recoverable record</span>', mark='hollow', last=True) + '</div>')
    new = ('<div>' + row_mark('photo', 'A photograph of a dish &rarr; <span style="color: #6E6862;">the mechanism behind its texture, and a method</span>')
           + row_mark('note', 'A friend&rsquo;s note &rarr; <span style="color: #6E6862;">a better window for the same place</span>')
           + row_mark('ferry', 'Scattered tickets and photos &rarr; <span style="color: #6E6862;">one recoverable morning, with its evidence</span>', last=True) + '</div>')
    assert old in html
    return html.replace(old, new, 1)

def persona_c_board():
    cols = [col(g3.h3v2_first(), daycap('TUESDAY 8:05 &middot; COLD', '1 &middot; BEFORE &middot; REVISION 3', 'The sample first', 'A HAND-DRAWN STUB &middot; PLAIN CAPABILITY ROWS')),
            col(first_open_after(), daycap('TUESDAY 8:05 &middot; COLD', '2 &middot; AFTER &middot; THIN-CONTEXT CHECK', 'Life&rsquo;s signature as the sample; the capabilities wear their marks', 'NOTHING PERSONAL WRITTEN &middot; NONPERSONAL LANGUAGE KEPT')),
            col(g3.h3v2_sample(), daycap('THE SAMPLE, OPENED', '3 &middot; INSPECTED', 'A ticket and its evening', 'UNCHANGED')),
            col(g3.h3v2_chat(), daycap('TUESDAY 8:12 &middot; CHAT', '4 &middot; ONE CONTRIBUTION', 'Bring the ticket', 'EXISTING BOUNDARY &middot; NOT REDESIGNED')),
            col(gs.return_seam(), daycap('WEDNESDAY 7:30 &middot; THIN', '5 &middot; THE RETURN', 'The receipt as a chip', 'KEPT, ONCE, WITH UNDO &middot; THE CROWN IS THEIRS')),
            col(g3.h3v2_next(), daycap('SATURDAY 9:30 &middot; QUIET, THIN', '6 &middot; NEXT OPEN', 'No further contribution', 'UNCHANGED &middot; A DIFFERENT SAMPLE, AS A RESULT'))]
    notes = [notecol('The thin-context check', [
                ('WHAT CHANGED', N('The sample uses Life&rsquo;s admission signature at L2 (dashed, stamped) instead of a hand-drawn stub, so the demonstration and the real thing share one anatomy. The three capability rows wear the marks of the objects they start from. The kept receipt is the chip. Nothing personal is implied anywhere: no location, workplace, friend, or history.')),
                ('WHAT DID NOT', N('The Chat boundary, the onboarding language, the return crown, and the next-open sample. No intake campaign, no new composer.')),
                ('AT THE FLOOR', N('This page is what a new account sees with only a city supplied. The forms make the value recognizable without making the page busier: one sample, one city fact, three rows, one line.')),
             ], w=560)]
    return page(2700, hh('04'), f'VESPER &middot; HOME &middot; 04 &middot; PERSONA C &middot; THE NEW USER &middot; {PASS} &middot; {STAMP}', '04 &middot; Persona C &middot; a new account, with the forms',
                'First open before and after; then the sample opened, one contribution, the return with its receipt, and the next open. The visual language is applied without implying any personal data.', cols, notes)

# ───────────────────────────── 06 · two bounded Places continuations ─────────────────────────────
def places_route():
    svg = ('<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
           '<path d="M0 170 Q60 140 120 160 Q180 180 240 140 Q300 105 349 120 L349 230 L0 230 Z" fill="rgba(61,80,102,0.10)"/>'
           '<path d="M92 70 Q140 90 176 118 Q206 142 214 156" stroke="#B0853A" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-dasharray="0"/>'
           '<circle cx="92" cy="70" r="9" fill="#1B1714"/><text x="88" y="74" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FBF7EC">M</text>'
           '<text x="108" y="64" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE BAKERY &#183; 10:30</text>'
           '<text x="108" y="76" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">MAYA, FRI &#183; OPEN NOW</text>'
           '<circle cx="214" cy="156" r="6" fill="#B0853A"/>'
           '<text x="226" y="150" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#1B1714">THE PIER &#183; 1:40</text>'
           '<text x="226" y="162" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">LOW WATER TO 4</text>'
           '<text x="130" y="112" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8A6628" transform="rotate(38 130 112)">9 MIN BY BIKE</text>'
           '<path d="M150 190 L349 190" stroke="#3D5066" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/><text x="156" y="205" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#3D5066">THE FLOOD LINE</text>'
           '<circle cx="40" cy="196" r="5" fill="#4A3428"/><text x="50" y="200" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">YOU</text>')
    inner = scope_header('SUNSET PARK &middot; SUNDAY', 'The loaf, then the water &middot; the same two stops as Home&rsquo;s &ldquo;Today&rdquo;, on the ground', back=True)
    inner += map_wash(230, svg)
    inner += gut(seq_strip([('10:30', 'The sesame loaf', 'Maya, Friday: &ldquo;Sundays only &mdash; before eleven.&rdquo; Open now; the loaf goes first.', '9 MIN BY BIKE &middot; DOWNHILL'),
                            ('1:40', 'Low water on the pier', 'Walk the flood line east: the granite kerbs end where the 1911 gates&rsquo; protection ends.', '')], top=4), top=22)
    inner += gut(author_row('M', 'Maya', 'FRIDAY &middot; FRIENDS &middot; THROUGH SUNDAY') + f'<div style="{SERIF} font-size: 16px; line-height: 22px; color: {INK}; margin-top: 8px;">&ldquo;The Sunset Park bakery does the sesame loaf on Sundays only. Go before eleven or it&rsquo;s gone.&rdquo;</div>' + meta('HER SHARE IS WHY THE FIRST STOP IS FIRST &middot; IN THE FRIENDS SCOPE', 6), top=26)
    inner += gut('<div style="display: flex; gap: 18px; align-items: center;">' + door('Open the bakery') + door('Back to Sunday, at Home', MUTE) + '</div>', top=20)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">THE SAME POSSIBILITY, SPATIALLY &middot; NOTHING IS ADOPTED BY OPENING IT</div></div>'
    return places_phone(inner, 0)

def places_cold():
    svg = ('<rect x="0" y="0" width="150" height="230" fill="rgba(42,56,75,0.14)"/><rect x="150" y="0" width="199" height="230" fill="rgba(176,133,58,0.10)"/>'
           '<path d="M0 60 Q60 40 110 62 Q150 80 150 120 Q150 170 110 200 Q60 225 0 215" stroke="#3D5066" stroke-width="2" fill="none" opacity="0.5"/>'
           '<path d="M0 60 Q60 40 110 62 Q150 80 150 120 Q150 170 110 200 Q60 225 0 215 Z" fill="rgba(61,80,102,0.10)"/>'
           '<path d="M70 200 Q120 150 170 120 Q230 90 300 60" stroke="#1B1714" stroke-width="2" fill="none" stroke-dasharray="4 4" opacity="0.7"/>'
           '<text x="16" y="104" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#2A384B">RIVER SIDE</text>'
           '<text x="16" y="132" font-family="EB Garamond, serif" font-size="26" font-weight="600" fill="#1B1714">24&#176;</text>'
           '<text x="16" y="148" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">WIND OFF THE WATER &#183; 9 PM</text>'
           '<text x="196" y="150" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" letter-spacing="0.8" fill="#8A6628">THE AVENUE</text>'
           '<text x="196" y="178" font-family="EB Garamond, serif" font-size="26" font-weight="600" fill="#1B1714">28&#176;</text>'
           '<text x="196" y="194" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">MASONRY HOLDS THE DAY</text>'
           '<text x="190" y="42" font-family="JetBrains Mono, monospace" font-size="9" letter-spacing="0.8" fill="#8F877C">YOUR WALK &#183; TWO STREETS IN</text>'
           '<circle cx="70" cy="200" r="5" fill="#4A3428"/><text x="80" y="204" font-family="JetBrains Mono, monospace" font-size="10" letter-spacing="0.8" fill="#8F877C">YOU</text>')
    inner = scope_header('YOUR WALK &middot; THURSDAY NIGHT', 'The cold split, on the ground &middot; where the four degrees change', back=True)
    inner += map_wash(230, svg)
    inner += gut(u2('Two streets in, the masonry gives the day back', 'The line on the map is your walk. Cross it eastward after nine and the temperature the forecast prints stops being the one you feel.',
                    compare2('RIVER SIDE &middot; 9 PM', '24&deg;', 'wind off the water', 'THE AVENUE &middot; 9 PM', '28&deg;', 'masonry holds the day'), meta_t='TWO NEARBY STATIONS + FORECAST &middot; FIXTURE &middot; THE LINE IS A CLAIM AND SAYS SO'), top=22)
    inner += gut('<div>' + fact('IF YOU WANT THE WARM WAY', 'Two streets east, the whole way; four minutes longer, four degrees warmer.', last=True) + '</div>', top=18)
    inner += gut('<div style="display: flex; gap: 18px; align-items: center;">' + door('Thursday, at Home') + door('The two stations', MUTE) + '</div>', top=20)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">WHAT THE MAP ADDS: WHERE, NOT WHETHER &middot; HOME KEEPS THE FINDING</div></div>'
    return places_phone(inner, 0)

def places_board():
    cols = [col(g5.p1_friends(), daycap('PLACES &middot; FROM FRIENDS', '1 &middot; THE SCOPE AND THE MAP', 'What my people shared, and where', 'UNCHANGED')),
            col(g5.p1_focus(), daycap('PLACE FOCUS &middot; THE BAKERY', '2 &middot; A FRIEND&rsquo;S NOTE BESIDE THE VERDICT', 'The accepted social form', 'UNCHANGED')),
            col(places_route(), daycap('SUNSET PARK &middot; SUNDAY', '3 &middot; THE SAME POSSIBILITY, ON THE GROUND', 'A friend-informed sequence, spatially', 'NEW &middot; FROM HOME&rsquo;S &ldquo;TODAY&rdquo; &middot; THE ROUTE, THE FLOOD LINE, HER NOTE')),
            col(places_cold(), daycap('YOUR WALK &middot; THURSDAY', '4 &middot; THE COMPARISON, ON THE GROUND', 'Where the four degrees change', 'NEW &middot; FROM HOME&rsquo;S &ldquo;WORTH KNOWING&rdquo; &middot; THE MAP ANSWERS WHERE'))]
    notes = [notecol('Two bounded continuations', [
                ('WHAT BECOMES EASIER SPATIALLY', N('Phone 3: the order of the two stops, the leg between them, and the flood line as a line on the ground, with Maya&rsquo;s note as the reason the first stop is first. Phone 4: the finding on Home says four degrees; the map says where the four degrees change and offers the warm way back. Home keeps the finding; Places owns the where.')),
                ('WHAT IS NOT HERE', N('No Places redesign. No copy of the Home feed. No new scope. The friends scope and the Place Focus stand as they were. Marks are authored content at the author&rsquo;s precision; nothing is where anyone is.')),
                ('DOORS', N('Each phone has one door back to the Home unit it came from and one door deeper (the bakery, the two stations). Opening either adopts nothing.')),
             ], w=560)]
    return page(1820, hh('06'), f'VESPER &middot; HOME &middot; 06 &middot; PLACES &middot; FROM FRIENDS + TWO CONTINUATIONS &middot; {PASS} &middot; {STAMP}', '06 &middot; Places: the friends scope, and two Home units continued on the ground',
                'The accepted friends scope and Place Focus, unchanged; then two bounded continuations of Home units: the Sunday sequence as a route, and the cold split as a map. Semantic marks only.', cols, notes)

# ───────────────────────────── 07 · ledger reconciliation + per-form ledger ─────────────────────────────
FORMS_LEDGER = [
    ['Held-object instrument (the pass, the crown, the chip, the mark)', 'Source: a ticket or booking (Life, canonical); result: the timely consequence (Home). ACTUAL: commitment crown, receipts; PROPOSED: pass at L1 on Home, chip, mark', 'What matters about it now: doors, leave-by, gate', 'The pass in Life (L1); return to the same row', 'Read; kept only via an explicit Bring', 'Identity stable (name, kind, route); facts live (gate, boarding, delay)', 'Provider + the person; no audience', 'Structured state + service read', 'Provider change; window entry/exit', 'Prospective: nothing; live: stale-fact line; unknown: no fact claimed', 'Renderer for the pass family; provider seam; unknown: which providers'],
    ['Prepared possibility as a sequence', 'Source: world rhythms, a kept note, a share (owners); result: a derived read assessment (ephemeral)', 'The order, the leg, the one practical detail', 'Places (the route on the ground); return to the card', 'Read; Keep is an explicit gesture with its own owner (open question 1)', 'The stops are identity; times and hours are live', 'A friend&rsquo;s share may inform it within its grant; attributed', 'Composer selection over rhythms + notes; no prose generated', 'A stop&rsquo;s world fact changes; the window passes', 'Fewer stops; never invented', 'Sequence renderer; route seam to Places'],
    ['Authored contribution with its place', 'Source: the addressed note (author + audience owner); the place (Places owner)', 'Their words, and the place&rsquo;s identity and one useful line', 'Place Focus with the note beside the verdict; return to the region', 'Read; reply and use are separate explicit gestures', 'Words and author stable; hours and distance live', 'Author, audience = this person; withdrawal removes the unit', 'Retrieval with audience check', 'Withdrawal; place change', 'Hide; never paraphrase', 'Existing handoff seam (MP1); the place identity read'],
    ['Comparison / paired evidence', 'Source: two kept menus, two stations (owners); result: the distinction (Home now; Life&rsquo;s Return when Home yields)', 'The difference, visible: three scales, two temperatures', 'The sources side by side (Life) or the map (Places)', 'Read', 'Quotes stable; numbers live', 'None; or a friend&rsquo;s lane under grant (heat pattern)', 'Reusable researched content + world data; bespoke synthesis only for the pairing', 'A source withdrawn; a station refresh', 'Without the second source: no comparison', 'Paired-evidence renderer; seat law with Life'],
    ['Usable method', 'Source: a general technique (content library); selected by a photograph or note (private trigger)', 'Three steps and the proportions; usable without a conversation', 'The whole method (a content object); return in place', 'Read; retires after tried or ignored twice', 'Steps stable; nothing live', 'None', 'Reusable researched content; retrieval', 'Content revision', 'Not shown', 'Method renderer; the content library does not yet exist'],
    ['Evidence-backed reconstruction', 'Source: a ticket and photographs (Life custody); result: the sequence (Life-owned; Home shows it once, on day zero)', 'What was kept and when; where nothing was', 'The journey in Life; return to the unit', 'Read; correction lives in Life', 'Marks are the evidence; nothing live', 'Private', 'Structured state from tickets and timestamps; no prose', 'More imports; a correction', 'Not shown until clean', 'Strip renderer; the reconstruction seam (09-02)'],
    ['Control: the bare fact row', 'Source: a city notice (source with freshness)', 'The consequence inside the window', 'The notice', 'Read', 'Stable until expiry', 'None', 'Current world information', 'Expiry', 'Not shown', 'Notice source with licensing (unknown)'],
]
def ledger_board():
    html = gm.ledger_board()
    recon = blk('RULINGS VS HISTORY &middot; RECONCILED 2026-09-05', tbl(['ITEM', 'STANDING', 'WHERE'], [
        ['D-H1 crown only when operational', 'History &middot; withdrawn 09-04', 'decision log below'],
        ['D-H2 / D-H3 one relational opening; social budget', 'Ruled 09-05', 'decision amend-home-composition-canon &sect;2'],
        ['D-H4 present-tense aperture', 'Closed 09-05 by the social split; earlier &ldquo;proposed&rdquo; entries below are history', 'decision &sect;2; 06'],
        ['D-H10 four type roles', 'Ruled 09-05; the &ldquo;proposed amendment&rdquo; entry below is history', 'kernel &sect;12.7 (c)'],
        ['D-H11 production classes and cost', 'Open', 'engineering review'],
        ['Kind mark on object rows; chip as object print; pass in the live window; timeliness clause', 'Ruled 09-05', 'decision home-borrows-life-pass-grammar; kernel &sect;11.16'],
        ['Crown arbitration', 'Provisional; a freedom-preserving alternative is compared on 08 row four', 'kernel &sect;11.16; 08'],
        ['The artifact-led forms (sequence, place-in-contribution, paired evidence, method, reconstruction strip)', 'PROPOSED &middot; not ruled; drawn on 02, 03, 04, 06, 09', 'this ledger, below'],
        ['Carded method; Places chips; kind inks in Home&rsquo;s palette; large-text choices', 'PROPOSED &middot; kept separate from accepted rules', '09'],
    ]))
    forms = blk('PER-FORM LEDGER &middot; ARTIFACT-LED PASS &middot; OUTSIDE THE PHONE', tbl(['FORM', 'SOURCE / RESULT &middot; OWNER &middot; ACTUAL VS PROPOSED', 'VISIBLE PAYOFF', 'TAP OPENS &middot; RETURN', 'READ / KEPT / USED', 'STABLE VS LIVE', 'AUTHORSHIP &middot; AUDIENCE', 'PRODUCTION CLASS', 'TRIGGER &middot; INVALIDATION', 'FALLBACK', 'SEAM &middot; UNKNOWN'], FORMS_LEDGER))
    adopt = blk('RECOMMENDATION &middot; WHAT TO ADOPT FIRST', N('<b>Adopt first:</b> the held-object instrument (already ruled), the sequence for prepared possibilities, and the place identity inside an addressed contribution. All three are structured state or retrieval with no generated prose, and each removes reading. '
        '<b>Adopt with its source:</b> paired evidence and the reconstruction strip, when the sources exist in Life; both are Life-native and Home shows them once. '
        '<b>Defer:</b> the usable method until a technique library exists; the carded method until the bare form proves insufficient. '
        '<b>A plain row or sentence wins</b> for city facts, a dentist, a refund claim, a settled dinner, and any single-source finding: the control on every page stays bare.'))
    diag = blk('DIAGNOSTICS &middot; VISIBLE WORDS AND SCROLL HEIGHT &middot; BEFORE / AFTER (NOT TARGETS)', tbl(['PHONE', 'BEFORE', 'AFTER', 'WHAT THE FORMS ADDED'], [[k] + v for k, v in json.load(open(os.path.join(OUT, 'diag_forms.json'))).items()]) if os.path.exists(os.path.join(OUT, 'diag_forms.json')) else N('Rendered after generation; see the response document.'))
    html = html.replace('<div style="display: flex; flex-direction: column; gap: 34px;">', '<div style="display: flex; flex-direction: column; gap: 34px;">' + recon + forms + adopt + diag, 1)
    html = html.replace(f'07 &middot; LEDGER AND DECISIONS &middot; REVISION 5 &middot; {STAMP}', f'07 &middot; LEDGER AND DECISIONS &middot; {PASS} &middot; {STAMP}')
    html = html.replace('07 &middot; The system, the rulings, the ledger, and the history behind 01&ndash;06', '07 &middot; The system, the rulings reconciled, the per-form ledger, and the history')
    html = re.sub(r'width: 3380px; min-height: \d+px', f'width: 3380px; min-height: {hh("07")}px', html, count=1)
    return html

# ───────────────────────────── 08 · row four: the priority comparison and the waiting window ─────────────────────────────
def alt_crown():
    """Alternative B: the pass stays dominant (cost of missing it is highest) but its optional action is a quiet door, not the page's demanded response."""
    extra = (f'<div style="padding: 0 18px 14px 18px; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid {HAIRT};">'
             f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 24px; letter-spacing: -0.2px; margin-top: 12px;">You land at 9:40, not 6:55. Nothing to do until 8:50.</div>'
             f'<div style="{SERIF} font-size: 15px; line-height: 21px; font-weight: 500; color: {INK2};">The stay&rsquo;s code works at any hour; Maya and Alex land first. Sunday is unchanged.</div>'
             + span('THE NEW ONE &middot; 9:30 PM', 150, 240, 'LAND 9:40 AM', 'THE ORIGINAL &middot; 6:45 PM', 55, 150, 'OUT', start='4 PM', end='10', w=313)
             + f'<div style="display: flex; gap: 18px; align-items: center; margin-top: 6px;">{door("Tell the five the new landing")}{door("The way there", MUTE)}</div>'
             f'<div class="fn">AVAILABLE, NOT DEMANDED &middot; PROVIDER 4:52 &middot; TICKETS AND THE STAY UNCHANGED</div></div>')
    return '<div style="margin: 22px 22px 0 22px;">' + gs.pass_flight_delayed(extra=extra) + '</div>'

def alt_phone():
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '4:52 PM')
    inner += (f'<div style="padding: 6px 22px 0 22px;"><div style="{SERIF} font-weight: 600; font-size: 22px; line-height: 27px; letter-spacing: -0.2px; color: {OX};">TAP 214 is delayed to 9:30. Nothing to do until 8:50. Dana needs an answer by six.</div>'
              f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 6px;">Gate moved to B31 &middot; the five can be told whenever you like.</div></div>')
    inner += alt_crown()
    inner += gut(gs.folded_decision(with_door=True), top=10)
    inner += sect('In motion') + gut(arow('Maya and Alex &middot; <span style="color: #6E6862;">the 8:10, on time &middot; they land first</span>', avatars=['M', 'A'])
                                     + row('Alfama stay &middot; <span style="color: #6E6862;">check-in from 3 tomorrow &middot; the code works any hour</span>', mark='solid', color=GOLD, last=True))
    inner += gut(collapsed('THE REST &middot; STILL HERE', ['Lisbon on landing: the stay, the code, the walk from the tram', 'Sunday: Sintra, the 9:10 train, palace tickets at 2']), top=36)
    inner += ending([('FRI', dm('solid', OX), 'delayed', OX), ('SAT', dm('av:D', ''), 'Dana?', OX), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Dana by six. Boards at 8:50 from B31.')
    return phone(inner, 0)

def wait_phone():
    """The long, safe waiting window: the pass is true and needs nothing for three hours. Breadth returns: food near the gate, reading, a friend's perspective, Sunday."""
    inner = anchor_row('JFK &middot; TERMINAL 4 &middot; FRIDAY', '5:40 PM')
    inner += orientation('Three hours at the gate. Boarding at 8:50 from B31.', 'Delayed to 9:30 &middot; the five know &middot; Dana answered: the Sunday train.')
    ident = (f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px;">{mark("flight", 13, 0.7)}<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1.1px; color: {MUTE};">TAP 214 &middot; JFK&rarr;LIS &middot; GATE B31 &middot; BOARDS 8:50</span>'
             f'<span style="margin-left: auto; font-size: 13px; font-weight: 500; color: {GOLDD};">The ticket</span>{ARROW}</div>')
    inner += gut(card(f'<div style="display: flex; align-items: center; gap: 7px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {PLAN};"></span><span style="font-size: 11px; font-weight: 600; letter-spacing: 0.8px; color: {PLAN};">WAITING &middot; NOTHING NEEDED UNTIL 8:50</span></div>' + ident + meta('CURRENT AS OF 5:40 &middot; GATE FROM PROVIDER &middot; RE-CHECKS UNTIL BOARDING', 10)), top=22)
    inner += sect('While you wait') + gut('<div>' + fact('TERMINAL 4 &middot; NEAR B31', 'The noodle counter at B30 is open until ten; the bookshop by B24 closes at nine.', ) + fact('CHARGING', 'Under the B31 seats, both sides.', last=True) + '</div>')
    inner += gut(handoff_artifact('M', 'Maya', 'WEDNESDAY &middot; TO YOU', 'For the first night: the corner table at the place under the stay, they hold it till nine if you ask.', 'dining', 'The tasca under the stay', 'ALFAMA &middot; TWO MINUTES FROM THE DOOR &middot; TILL LATE', 'The tasca'), top=26)
    inner += gut(reading_card('THE LISBON CHAPTER &middot; 6 MIN', 'Why the trams climb the way they do', 'The 1901 line was laid on the old mule routes; the gradients are the animals&rsquo;, not the engineers&rsquo;.', 'Read the chapter'), top=22)
    inner += sect('Sunday') + gut(u2('Sintra: the 9:10 train, the palace at two', 'Tickets are for 2 PM; the morning is open. The market in Alfama runs until one if you would rather start slow.', meta_t='PALACE TICKETS &middot; IN LIFE &middot; THE TRAIN TIME FROM THE OPERATOR', door_text='Sunday, in the trip'))
    inner += ending([('FRI', dm('solid', PLAN), 'B31', INK), ('SAT', dm('solid', INK), 'Lisbon', INK), ('SUN', dm('solid', INK), 'Sintra', INK), ('MON', dm('hollow', ''), 'open', MUTE), ('TUE', dm('dashed', MUTE), 'free', MUTE), ('WED', dm('solid', GOLD), 'home', MUTE), ('THU', dm('hollow', ''), '', MUTE)],
                    'Boards at 8:50. Lisbon at 9:40 tomorrow.')
    return phone(inner, 0)

def priority_column():
    t = tbl(['', 'A &middot; PROVISIONAL CANON', 'B &middot; FREEDOM-PRESERVING'], [
        ['What is dominant', 'The highest rank present: recovery &gt; live commitment &gt; decision &gt; arrangement', 'The object whose delay would cost most, given its deadline, dependencies, and available actions'],
        ['The one ask', 'Belongs to the crown until spent; a folded decision waits', 'Belongs to whoever has a <i>demanded</i> response with a deadline; the crown&rsquo;s optional action is a door'],
        ['Delayed flight + Dana', 'Tell the five (CTA); Dana&rsquo;s row has no door until the message is sent', 'The pass stays dominant; &ldquo;tell the five&rdquo; is a quiet door; Dana&rsquo;s row carries the page&rsquo;s ask'],
        ['Other objects', 'Fold to one row under the crown; reachable, no door', 'Fold to one row under the crown; reachable, with their own door if they have a deadline'],
        ['Waiting window', 'Not addressed: the live posture folds the page', 'The pass compacts to a held state; breadth returns while nothing is needed'],
        ['Demand budget', 'One ask on the page', 'One demanded response on the page; optional actions do not count'],
    ])
    return (f'<div style="width: 470px; flex: none; display: flex; flex-direction: column;">'
            + caption('THE COMPARISON', 'Two priority rules on one collision', 'A = KERNEL &sect;11.16 AS RULED PROVISIONALLY &middot; B = THE BRIEF&rsquo;S ALTERNATIVE &middot; DECISION NEEDED')
            + f'<div style="padding: 6px 0 14px 0;">{t}</div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">WHAT B CHANGES IN THE CANON</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">The one-ask rule is reread as one <i>demanded</i> response per page. An available action on the dominant object is a door, not a CTA, unless the object itself demands it (a boarding call, a check-in that closes). The ranking becomes a tie-break within &ldquo;what would delay cost&rdquo;, not the first question. Dominance and demand separate: the pass can be the largest thing on the page while Dana holds the only ask.</div></div>'
            + f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 8px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">WHAT B RISKS</div><div style="font-size: 12px; line-height: 17px; color: {MUTE};">&ldquo;Cost of delay&rdquo; needs a judgment the composer must make from evidence: deadline, dependency, and whether an action is corrective. Where that evidence is missing, B degrades to A. A is simpler to build and to predict; B is more honest to the person&rsquo;s time.</div></div>'
            + '</div>')

PRIORITY_NOTES = notecol('The waiting window, and the recommendation', [
    ('PHONE 12 &middot; WAITING', N('At 5:40 the pass is true and needs nothing for three hours. Under the accepted live posture the page would stay folded. Here the pass compacts to a held state (planning register, one identity line, a door), and breadth returns: two facts about the gate, Maya&rsquo;s addressed tasca for the first night, the Lisbon chapter, Sunday. Every unit is grounded; none is urgent; nothing asks. This is the breadth treatment the brief asked to see separately.')),
    ('THE RUSH IS NOT THE WAIT', N('Phone 7 on row two (3:12 PM, leave now) stays folded: a departure rush. Phone 12 is a wait. The same object, two postures, decided by whether anything is needed of the person in the next hour, not by whether a ticket is live.')),
    ('RECOMMENDATION', N('Adopt B&rsquo;s separation of demanded response from available action, and B&rsquo;s waiting posture. Keep A&rsquo;s ranking as the tie-break when cost of delay cannot be judged from evidence. Record this as an amendment to &sect;11.16, not a silent change: the founder decides.')),
    ('IGNORED AND DISMISSED', N('If Dana&rsquo;s row is ignored past six, it becomes a plain row: &ldquo;Dana asked which train; she chose Sunday.&rdquo; No badge, no debt. If the five are never told, nothing follows; they see the landing time on the trip. Completed actions become one line in the crown&rsquo;s footer, as on phone 10.')),
], w=520)

def seam_board():
    html = gs.seam_board()
    row4 = [priority_column(),
            col(gs.collision_phone(), daycap('FRIDAY 4:52 PM &middot; RULE A &middot; BASELINE', '11a &middot; PROVISIONAL CANON', 'Dana waits under the delay', 'LABELED BASELINE &middot; THE CROWN HOLDS THE ONLY ASK')),
            col(alt_phone(), daycap('FRIDAY 4:52 PM &middot; RULE B &middot; ALTERNATIVE', '11b &middot; FREEDOM-PRESERVING', 'The pass is dominant; Dana holds the ask', 'TELL THE FIVE IS A DOOR &middot; ANSWER DANA IS THE DEMANDED RESPONSE')),
            col(wait_phone(), daycap('FRIDAY 5:40 PM &middot; THREE HOURS TO BOARD', '12 &middot; THE WAITING WINDOW', 'The pass holds; breadth returns', 'COMPACT HELD STATE &middot; FOOD, A NOTE, A CHAPTER, SUNDAY &middot; NOTHING ASKS')),
            PRIORITY_NOTES]
    divider4 = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE PRIORITY COMPARISON &middot; RULE A VS RULE B &middot; AND THE WAITING WINDOW &middot; DECISION NEEDED</div>'
                f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Must one task be the price of another? Two rules on the same afternoon</div>'
                f'<div style="font-size: 13.5px; line-height: 20px; color: {MUTE}; max-width: 980px;">Row three drew the provisional rule. This row draws the brief&rsquo;s alternative beside it, then the state neither rule addressed: a live ticket with three safe hours in front of it.</div></div>'
                '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row4) + '</div>')
    html = html.replace('<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">', divider4 + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">', 1)
    html = html.replace('THE FLIGHT AND THE COLLISION &middot; MERGED 2026-09-05', f'THE FLIGHT, THE COLLISION, THE PRIORITY COMPARISON &middot; {PASS}')
    html = html.replace('08 &middot; The seam with Life: one ticket, one flight, one collision, and where every door lands', '08 &middot; The seam with Life: one ticket, one flight, one collision, two priority rules')
    html = re.sub(r'width: 2480px; min-height: \d+px', f'width: 2480px; min-height: {hh("08")}px', html, count=1)
    return html

# ───────────────────────────── 09 · the selected-form sheet + large text ─────────────────────────────
def frame(inner, w=393, bg=PAPER):
    return f'<div style="width: {w}px; background: {bg}; padding: 6px 0 20px 0; box-sizing: border-box; {SANS} color: {INK};">{inner}</div>'

def sheet_col(t, sub, blocks, w=440):
    out = f'<div style="width: {w}px; flex: none; display: flex; flex-direction: column;">' + caption(t, sub[0], sub[1])
    for k, html_, note in blocks:
        out += (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 18px 0 10px 0; border-top: 1px solid {HAIR};"><div class="kick" style="color: {GOLDD};">{k}</div>{html_}'
                f'<div style="font-size: 12px; line-height: 17px; color: {MUTE};">{note}</div></div>')
    return out + '</div>'

def unfilled_comparison():
    return u2('Two coastlines, one distinction &mdash; not yet researched', 'The form: paired evidence around a formation or settlement contrast. The claims, figures, and any diagram require research; nothing here asserts a height, a geology, or a measured scale.',
              f'<div style="display: flex; gap: 12px; margin-top: 10px;"><div class="hatch" style="flex: 1; height: 96px; border-radius: 12px; display: flex; align-items: flex-end; padding: 8px;"><span class="fn" style="color: {ANCHOR};">SORRENTO &middot; PLATE &middot; SLOT</span></div><div class="hatch" style="flex: 1; height: 96px; border-radius: 12px; display: flex; align-items: flex-end; padding: 8px;"><span class="fn" style="color: {ANCHOR};">A COMPARABLE COAST &middot; SLOT</span></div></div>'
              + f'<div style="display: flex; gap: 18px; margin-top: 8px;"><div style="flex: 1;"><span class="kickm">SORRENTO</span><div style="height: 10px; margin-top: 6px; border-radius: 4px; background: rgba(27,23,20,0.06);"></div><div style="height: 10px; margin-top: 4px; border-radius: 4px; background: rgba(27,23,20,0.06); width: 70%;"></div></div><div style="flex: 1;"><span class="kickm">THE OTHER COAST</span><div style="height: 10px; margin-top: 6px; border-radius: 4px; background: rgba(27,23,20,0.06);"></div><div style="height: 10px; margin-top: 4px; border-radius: 4px; background: rgba(27,23,20,0.06); width: 60%;"></div></div></div>',
              meta_t='RESEARCH REQUIRED &middot; CLAIMS NOT WRITTEN &middot; NOT ON ANY PHONE')

def forms_sheet():
    c1 = sheet_col('1 &middot; HELD-OBJECT INSTRUMENT', ('The ticket at its scales', 'RULED 09-05 &middot; L1 IN THE LIVE WINDOW ONLY &middot; CHIP &middot; MARK'), [
        ('STANDARD &middot; THE PASS (L1)', f'<div style="display: flex; justify-content: center;">{pass_admission()}</div>', 'Identity stable: kick, name, kind. Facts live. The band is object print.'),
        ('COMPACT &middot; THE ROW AND THE CHIP', frame(gut(row_mark('admission', 'The show &middot; Friday, doors 8 &middot; <span style="color: #6E6862;">set times not posted</span>', last=True) + f'<div style="padding-top: 12px; display: flex; gap: 7px;">{chip("admission", "THE HALL", "ring")}{chip("flight", "JFK&rarr;LIS", "ring")}</div>')), 'A small row is not a miniature pass: mark, one line, state in words. The chip names a kept object and nothing else.'),
        ('EXPANDED &middot; LIVE, AS THE CROWN', f'<div style="display: flex; justify-content: center;">{live_pass_crown().replace("margin: 22px 22px 0 22px", "margin: 0")}</div>', 'The consequence and one ask between truths and band. Each fact has one principal location: doors in the truths, leave-by in the status line, the way home in the deck.'),
    ])
    c2 = sheet_col('2 &middot; PREPARED POSSIBILITY', ('A sequence, or a compact set', 'PROPOSED &middot; DERIVED READ ASSESSMENT &middot; OPENING ADOPTS NOTHING'), [
        ('STANDARD &middot; THE SEQUENCE', frame(gut(ways_seq_card('Today, in order', [('10:30', 'The sesame loaf', 'Maya, Friday: &ldquo;before eleven.&rdquo; Open now.', '9 MIN BY BIKE'), ('1:40', 'Low water on the pier', 'The flood line, walked. Until four.', '')], alts=[('Stay in: the skillet, preheated dry', 'TONIGHT')], meta_t='ONE RIDE, TWO THINGS THAT ONLY HAPPEN TODAY'))), 'Order is the explanation; the leg is the practical detail; the &ldquo;or&rdquo; keeps it a possibility, not an itinerary.'),
        ('COMPACT &middot; THE ALTERNATIVE SET', frame(gut(ways_card('This afternoon', [('The pier at low water', 'The first walk back can be the one you know.', 'LOW WATER 2:40&ndash;5'), ('Stay in', 'The noodle shop delivers until ten.', 'ANY TIME')]))), 'When there is no order to explain, the accepted alternatives card (rev 4) is the compact form.'),
        ('ON THE GROUND &middot; PLACES', frame(map_wash(150, '<path d="M92 50 Q140 70 176 98 Q206 122 214 126" stroke="#B0853A" stroke-width="2.4" fill="none"/><circle cx="92" cy="50" r="7" fill="#1B1714"/><circle cx="214" cy="126" r="6" fill="#B0853A"/><text x="106" y="46" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">THE BAKERY</text><text x="226" y="122" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#1B1714">THE PIER</text>', top=0)), 'The same two stops as a route. Places owns where; Home keeps the order.'),
    ])
    c3 = sheet_col('3 &middot; AUTHORED CONTRIBUTION', ('Their words, and the place', 'PROPOSED &middot; AUTHOR + AUDIENCE OWNER &middot; WITHDRAWAL REMOVES IT'), [
        ('STANDARD &middot; ADDRESSED, WITH ITS PLACE', frame(gut(handoff_artifact('M', 'Maya', 'SATURDAY &middot; TO YOU', 'This one after the show, it&rsquo;s open till one and you won&rsquo;t need a table.', 'dining', 'The noodle bar', 'THREE BLOCKS FROM THE HALL &middot; OPEN TILL 1', 'The noodle bar'))), 'Authorship integral: the avatar and name lead, her words are serif, the place is one identity strip. No paraphrase.'),
        ('COMPACT &middot; THE ROW', frame(gut(arow('Maya &middot; the noodle bar, for after the show &middot; <span style="color: #6E6862;">addressed Saturday &middot; open till 1</span>', avatars=['M'], last=True))), 'When the contribution is spent above, it is one row: her name, the place, the reason.'),
        ('CASUAL &middot; IN PLACES ONLY', frame(gut(g3.share_card('M', 'Maya', 'FRIDAY &middot; FRIENDS', 'The Sunset Park bakery does the sesame loaf on Sundays only.', 120, 'MAYA&rsquo;S PHOTOGRAPH &middot; SLOT', 'SUNSET PARK &middot; SHARED AS A PLACE', 'The bakery'))), 'The casual share stays in Places (the social split). Home shows only its effect inside a possibility.'),
    ])
    c4 = sheet_col('4 &middot; COMPARISON / PAIRED EVIDENCE', ('The difference, visible', 'BARE BY CANON &middot; SOURCES SIDE BY SIDE &middot; A LINE IS A CLAIM'), [
        ('STANDARD &middot; TWO LANES', frame(gut(COLD())), 'The accepted two-lane instrument: two numbers, one clause each, the source line. Bare.'),
        ('STANDARD &middot; PAIRED EVIDENCE', frame(gut(MENUS)), 'Three quoted excerpts, each with its scale. The claim is only what the quotes show. Bare.'),
        ('THE FORM WITHOUT ITS RESEARCH', frame(gut(unfilled_comparison())), 'The coastline comparison the brief names: drawn as a form only. No claim is written until research supports it.'),
    ])
    c5 = sheet_col('5 &middot; USABLE METHOD', ('A concrete answer, no conversation', 'PROPOSED &middot; REUSABLE CONTENT &middot; RETIRES AFTER TRIED OR IGNORED TWICE'), [
        ('STANDARD &middot; BARE (CANON)', frame(gut(method('The method, for one pan', ['Pull the pasta ninety seconds early; keep a ladle of the water.', 'Into the sauce over heat, with the ladle; toss until the film holds the ridges.', 'Off the heat before it tightens.'], meta_t='A GENERAL TECHNIQUE, SELECTED BECAUSE OF YOUR PHOTOGRAPH', door_text='The whole method'))), 'Findings and techniques stay bare. Three numbered steps read as a method without a card.'),
        ('CARDED &middot; THE FLAGGED AMENDMENT', frame(gut(method('The method, for one pan', ['Pull the pasta ninety seconds early; keep a ladle of the water.', 'Into the sauce over heat, with the ladle; toss until the film holds the ridges.', 'Off the heat before it tightens.'], meta_t='A GENERAL TECHNIQUE', door_text='The whole method', carded=True))), 'If a reusable method needs to read as a held object (it can be kept, it recurs), this is the exact amendment to &sect;5.1: &ldquo;a bounded, reusable method&rdquo; joins the coherent objects. Not adopted; shown for the decision.'),
    ])
    c6 = sheet_col('6 &middot; EVIDENCE-BACKED RECONSTRUCTION', ('The marks are the evidence', 'PROPOSED &middot; LIFE-OWNED &middot; HOME SHOWS IT ONCE'), [
        ('STANDARD &middot; THE STRIP', frame(gut(recon_strip([('9:10', 'ferry', 'TICKET', ''), ('9:14', 'photo', 'HARBOR', ''), ('10:02', 'photo', 'THE QUAY', 'NOTHING KEPT'), ('1:20', 'photo', 'THE STEPS', '')], t='Sorrento to Amalfi by ferry', text='From your ticket and three photographs. Gaps stay gaps.', meta_t='TICKET 9:10 &middot; PHOTOGRAPHS 9:14, 10:02, 1:20', door_text='The trip, in Life'))), 'A ticket node, photograph nodes, a hatched span where nothing was kept. The strip never asserts boarding.'),
        ('COMPACT &middot; THE ROW', frame(gut(row_mark('ferry', 'Sorrento &rarr; Amalfi &middot; the ferry morning &middot; <span style="color: #6E6862;">a ticket and three photographs</span>', last=True))), 'One row with the kind mark when the reconstruction is not the unit of the day.'),
        ('CONTROL &middot; THE BARE FACT ROW', frame(gut('<div>' + fact('OPEN HOUSE &middot; OCT 17&ndash;18', 'Registration for the timed sites opens Tuesday at noon; walk-in sites need none.', last=True) + '</div>')), 'On every page, at least one unit stays this plain. Simple findings stay simple.'),
    ])
    lt = (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;">' + caption('LARGER TEXT &middot; 1.3&times;', 'The Sunday page, reflowed', 'EVERY FONT-SIZE AND LINE-HEIGHT &times;1.3 &middot; WIDTHS UNCHANGED &middot; NOTHING SHRUNK TO FIT')
          + large(sunday_after()) + '</div>')
    lt2 = (f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;">' + caption('LARGER TEXT &middot; 1.3&times;', 'The live pass, reflowed', 'THE PASS, THE TRUTHS, THE BAND, THE CTA AT 1.3&times;')
           + large(gs.live_flight_phone()) + '</div>')
    notes = [notecol('Reading order and non-visual alternatives', [
                ('THE SEQUENCE', N('Read top to bottom: time, name, detail, then the leg to the next stop. Screen readers get the same order; the gold line carries no information the times do not.')),
                ('THE TWO-LANE COMPARISON', N('Left lane then right lane, each as kicker, value, clause. The number is the claim; the colour is not. A text alternative: &ldquo;River side 24&deg;, wind off the water; the avenue 28&deg;, masonry holds the day.&rdquo;')),
                ('THE RECONSTRUCTION STRIP', N('Left to right in time. Each mark names its kind and time in text; the hatched span is announced as &ldquo;nothing kept until 1:20&rdquo;. No hover, no precision tap: every node is also the unit&rsquo;s door.')),
                ('THE MAPS (06)', N('Announced as a list: the stops in order with their times, the flood line as a sentence, the two temperatures as a sentence. The map clarifies; it is never the only carrier.')),
                ('LARGE TEXT', N('At 1.3&times; the sequence, the pass, and the rows reflow within 393px. The chip does not scale (object print); the row beside it does. The band&rsquo;s object print is the one element that stays small, by the ruled exemption; it is never the only carrier of its fact.')),
             ], w=560),
             notecol('What is proposed here, kept apart from what is ruled', [
                ('RULED', N('The held-object instrument at its scales (decision home-borrows-life-pass-grammar).')),
                ('PROPOSED', N('The sequence; the place inside an addressed contribution; paired evidence; the bare method; the reconstruction strip; the compact rows with kind marks for possibility and reconstruction.')),
                ('FLAGGED AMENDMENTS', N('The carded method (&sect;5.1); kind inks in Home&rsquo;s palette (the violet band); chips in Places; the demanded-vs-available reading of the one-ask rule (08 row four).')),
                ('NOT SHOWN', N('Native behaviour, real photography, provider integrations, cost. The 1.3&times; render is a reflow test, not an accessibility audit.')),
             ], w=560)]
    body = '<div style="display: flex; gap: 46px; align-items: flex-start;">' + c1 + c2 + c3 + '</div>'
    body += '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + c4 + c5 + c6 + '</div>'
    body += '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12);">' + lt + lt2 + ''.join(notes) + '</div>'
    return (HEAD + f'<div style="width: 1560px; min-height: {hh("09")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; HOME &middot; 09 &middot; THE FORMS &middot; SELECTED-FORM SHEET &middot; {PASS} &middot; {STAMP}', '09 &middot; Six forms, at the scales they appear, and one control',
                   'The supporting sheet, made after the pages worked. Each form at its standard expression, its compact expression, and an expanded or spatial one where useful; a control that stays bare; the coastline comparison drawn as a form without its research; two phones at 1.3&times; text; reading order for every non-text form.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT}</div></div>' + TAIL)

# ───────────────────────────── diagnostics ─────────────────────────────
PAIRS = {
    '02 Sunday': (g5.h1v5, sunday_after, 'A sequence with a leg; a three-step method; the reading preview; the ticket mark'),
    '02 Monday': (g5.h2v5_t2, monday_after, 'The place identity strip inside each addressed card'),
    '03 Day zero': (g4.h5v4, dayzero_after, 'A method; the strip with four evidence marks; the menus comparison'),
    '04 First open': (g3.h3v2_first, first_open_after, 'The admission signature as the sample; marks on the capability rows'),
}
def words(html):
    t = re.sub(r'<style.*?</style>', '', html, flags=re.S); t = re.sub(r'<[^>]+>', ' ', t); t = re.sub(r'&[a-z]+;|&#\d+;', ' ', t)
    return len([w for w in t.split() if any(c.isalpha() for c in w)])

FILES = {'02 - Persona A - The New Yorker': persona_a_board, '03 - Persona B - Back from Europe': persona_b_board, '04 - Persona C - New User': persona_c_board,
         '06 - Places - From Friends': places_board, '07 - Ledger and Decisions': ledger_board, '08 - Seam with Life': seam_board, '09 - Forms': forms_sheet}

if __name__ == '__main__':
    os.makedirs(os.path.join(OUT, 'diag'), exist_ok=True)
    for k, (before, after, _) in PAIRS.items():
        for tag, fn in (('before', before), ('after', after)):
            open(os.path.join(OUT, 'diag', f'{k.replace(" ", "_")}_{tag}.html'), 'w').write(HEAD + fn() + TAIL)
    for name, fn in FILES.items():
        html = fn(); open(os.path.join(OUT, name + '.dc.html'), 'w').write(html); print('wrote', name, len(html))
