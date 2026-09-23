"""Checkpoint 2 · board 02 · Experience A · A little of your world. Seven phones from the ledger; fixture copy only. Nothing here is ruled."""
import os, sys, json
HP = '/private/tmp/claude-501/-Users-feihuyan-Documents-Claude-travel-workspace/122d6063-48c0-4124-ac7f-f94b3c62dc5a/scratchpad/hp'
sys.path.insert(0, HP)
from kit import *
from gen_generous import col, N, FOOT, head, facepile
from gen_generous3 import sect, meta, title, sup, gut, card, author_row
from gen_merge import tbl, blk, daycap, page
from gen_p2_common import (phone2, header, question_line, share_v2, share_line, place_unit, ending as pl_ending, plate, thumb, when_line, src, unc, PLACE_NAMES, PACKET, FRIENDS, notecol)
from gen_p2_04 import maya_print_room, by
from gen_se import OUT, hh, sheet, tag, ROLE, FOOT2

# ── shared package vdl-stage1 0.4.1 (workbench c13ae951): boards that place a shared component load the kernel copy and vdl.css ──
KERNEL_CSS = '_ds/vesper-production-kernel-fc85e38a-72e6-4b40-98a7-fb447dd94529/styles.css'
HEAD_VDL = HEAD.replace('<helmet>', f'<helmet>\n  <link rel="stylesheet" href="{KERNEL_CSS}">\n  <link rel="stylesheet" href="vdl.css">', 1)
assert HEAD_VDL != HEAD, 'helmet not found in HEAD'

def dci(name, h, **props):
    """One shared component instance. Attribute values are plain text; the runtime decodes camelCase props."""
    attrs = ' '.join(f'{k}="{v}"' for k, v in props.items())
    return f'<dc-import name="{name}" {attrs} hint-size="349px,{h}px"></dc-import>'

def inset(label, body, note):
    """A labelled state of an existing slot, drawn beside it. Not a new slot."""
    return (f'<div style="margin-top: 14px; width: 393px; box-sizing: border-box; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px;">'
            f'<div class="kickm">{label}</div>{body}<div class="fn" style="color: #6E6862; line-height: 15px;">{note}</div></div>')


STAMP = 'CHECKPOINT 2 &middot; 2026-09-07'
HAIR = 'rgba(27,23,20,0.10)'

def stamp_line(*parts):
    return f'<div class="fn" style="color: {ANCHOR}; margin-top: 8px; line-height: 15px;">{" &middot; ".join(parts)}</div>'
def rec(actor, entry, gesture, value, audience, owner, recipient, ending):
    """The compact outside-frame record for one material transition."""
    cells = [('ACTOR', actor), ('ENTRY', entry), ('GESTURE', gesture), ('VALUE', value), ('AUDIENCE', audience), ('OWNER', owner), ('RECIPIENT', recipient), ('ENDING', ending)]
    return ('<div style="display: flex; flex-direction: column; gap: 3px; margin-top: 10px; padding-top: 8px; border-top: 1px solid rgba(27,23,20,0.08);">'
            + ''.join(f'<div style="display: flex; gap: 8px; align-items: baseline;"><span class="fn" style="width: 62px; flex: none; color: {MUTE};">{k}</span><span style="font-size: 11.5px; line-height: 15px; color: {INK2};">{v}</span></div>' for k, v in cells) + '</div>')
def cap(n, role, root, day, k, t, s2):
    rc, rb = ROLE[role]
    lab = f'<div style="display: flex; gap: 6px; align-items: center; margin-bottom: 8px;"><span style="{MONO} font-size: 10px; font-weight: 700; color: {MUTE};">{n}</span>{tag(role, rc, rb)}{tag(root, MUTE, "rgba(27,23,20,0.06)")}</div>'
    return lab + daycap(day, k, t, s2) + '<div style="height: 6px;"></div>'
def under(record, stamps):
    return f'<div style="padding: 0 2px;">{rec(*record)}{stamp_line(*stamps)}</div>'
def colu(ph, capt, rec_html):
    return f'<div style="width: 393px; flex: none; display: flex; flex-direction: column;">{capt}{ph}{rec_html}</div>'

# ───────────────────────────── shared pieces ─────────────────────────────
def standin(h=190, label='PHOTO &middot; STAND-IN'):
    return f'<div class="hatch" style="height: {h}px; border-radius: 12px; display: flex; align-items: flex-end; padding: 10px 12px; box-sizing: border-box;"><span class="fn" style="color: {MUTE};">{label}</span></div>'
def chat_head(when, back=True):
    b = BACK if back else ''
    return f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{b}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">{when}</span></div></div>'
def ctx_chip(t, dot=GOLD):
    return f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {dot};"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {INK};">{t}</span></div>'
def bubble(t, media=''):
    return f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; display: flex; flex-direction: column; gap: 8px; align-items: flex-end;">{media}<div style="background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">{t}</div></div></div>'
def answer(t, sig=''):
    return f'<div style="max-width: 340px; display: flex; flex-direction: column; gap: 10px;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">{t}</div>{(f"<div class=\"fn\" style=\"color: {ANCHOR};\">{sig}</div>" if sig else "")}</div>'
def composer(hint='Ask, or say more'):
    return f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">{hint}</span></div>'
def who_pills(sel='Friends'):
    opts = ['Just me', 'Friends', 'Maya only']
    return '<div style="display: flex; gap: 7px; flex-wrap: wrap;">' + ''.join(
        f'<span style="height: 30px; border-radius: 15px; background: {INK if o == sel else CARD}; color: {CARD if o == sel else INK}; border: 1px solid {"transparent" if o == sel else HAIR}; display: inline-flex; align-items: center; padding: 0 12px; font-size: 14px; font-weight: 500;">{o}</span>' for o in opts) + '</div>'

# ───────────────────────────── 02.1 · the private Ask ─────────────────────────────
def ask_phone():
    inner = chat_head('THURSDAY 7:50 PM')
    inner += gut(bubble('why did the sauce break? this was the Sorrento one', media=f'<div style="width: 220px;">{standin(150, "THE PASTA &middot; HER PHONE &middot; ASSET NOT SOURCED")}</div>'), top=26)
    inner += gut(answer('Too much heat is one possibility; the photograph alone cannot confirm it. For the next attempt: off the heat, a ladle of the starchy water first, then the cheese in small handfuls, stirring until it turns glossy. That gives you one concrete thing to change.'), top=18)
    inner += gut(composer(), top=36)
    return phone(inner, 0, active='Chat')

# ───────────────────────────── 02.2 · the share, deliberately ─────────────────────────────
def share_draft_phone():
    """A friend shares directly from an eligible object: Maya, from the Print Room's place page. No AI prelude, no Occasion, no connection setup."""
    inner = f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">SHARE &middot; THE HARBOR PRINT ROOM</span></div></div>'
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 210, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;"><span style="{SERIF} font-size: 18px; line-height: 25px; color: {INK};">The side room was my favorite. Go on a weekday, it was empty.</span></div>', top=16)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">WHO</div>' + who_pills('Friends').replace('Maya only', 'Nora only') + f'<div style="display: flex; gap: 18px; align-items: baseline; margin-top: 12px;"><span style="font-size: 13px; color: {INK2};">The Print Room, Red Hook &middot; through Sunday</span>{door("Change", MUTE)}</div>', top=22)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 18px;"><span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 12px 22px; font-size: 15px; font-weight: 600;">Send</span>{door("Not now", MUTE)}</div>', top=26)
    return phone2(inner)

# ───────────────────────────── 02.3 · Places · From friends, full scroll ─────────────────────────────
def collection_card():
    stops = [('The Harbor Print Room', 'the side room; Tue&ndash;Sun 11&ndash;6'), ('The Red Hook pier', 'the harbor and the Statue'), ('The ferry landing', 'the flexible way out')]
    rows = ''.join(f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 7px 0; border-top: 1px solid rgba(27,23,20,0.06);"><span style="{MONO} font-size: 10px; font-weight: 700; color: {GOLDD}; width: 14px;">{i+1}</span><div style="flex: 1;"><div style="font-size: 15px; color: {INK};">{n}</div><div style="font-size: 13px; color: {MUTE};">{d}</div></div></div>' for i, (n, d) in enumerate(stops))
    mapw = f'<div class="hatch" style="height: 96px; border-radius: 10px; display: flex; align-items: flex-end; padding: 8px 10px; box-sizing: border-box;"><span class="fn" style="color: {MUTE};">MAP &middot; THREE STOPS &middot; ILLUSTRATION</span></div>'
    return card(mapw + author_row('P', 'Priya', 'SATURDAY &middot; A SMALL COLLECTION') + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 8px;">Red Hook on foot, three stops. An hour and a half if you don&rsquo;t sit down.</div><div style="margin-top: 10px;">{rows}</div>' + f'<div style="display: flex; gap: 18px; align-items: center;">{door("Reply to Priya")}{door("Open the map")}</div>')

def collection_card():
    stops = [('The Harbor Print Room', 'the side room; Tue&ndash;Sun 11&ndash;6'), ('The Red Hook pier', 'the harbor and the Statue'), ('The ferry landing', 'the flexible way out')]
    rows = ''.join(f'<div style="display: flex; gap: 10px; align-items: baseline; padding: 7px 0; border-top: 1px solid rgba(27,23,20,0.06);"><span style="{MONO} font-size: 10px; font-weight: 700; color: {GOLDD}; width: 14px;">{i+1}</span><div style="flex: 1;"><div style="font-size: 15px; color: {INK};">{n}</div><div style="font-size: 13px; color: {MUTE};">{d}</div></div></div>' for i, (n, d) in enumerate(stops))
    mapw = f'<div class="hatch" style="height: 96px; border-radius: 10px; display: flex; align-items: flex-end; padding: 8px 10px; box-sizing: border-box;"><span class="fn" style="color: {MUTE};">MAP &middot; THREE STOPS &middot; ILLUSTRATION</span></div>'
    return card(mapw + author_row('P', 'Priya', 'SATURDAY &middot; A SMALL COLLECTION') + f'<div style="{SERIF} font-size: 18px; line-height: 25px; color: {INK}; margin-top: 8px;">Red Hook on foot, three stops. An hour and a half if you don&rsquo;t sit down.</div><div style="margin-top: 10px;">{rows}</div>' + f'<div style="display: flex; gap: 18px; align-items: center;">{door("Reply to Priya")}{door("Open the map")}</div>')

def friends_scope_phone():
    inner = header('NEW YORK', 'From friends') + question_line(ctx='From friends')
    inner += gut(maya_print_room(with_priya=True), top=18)
    inner += sect('Red Hook') + gut(collection_card())
    inner += sect('The market') + gut('<div>' + share_line('P', 'Priya', 'The pigeons at the market have a system. I have watched it for twenty minutes.', 'The greenmarket', last=True) + '</div>')
    inner += sect('Elsewhere') + gut('<div>' + share_line('D', 'Dana', by('Dana', 'sorrento')[2], 'Sorrento, this week', last=True) + '</div>')
    inner += sect('Red Hook, anyway') + gut(place_unit('pier', 'The Red Hook pier', 'Any time &middot; free', 'Faces the harbor and the Statue; the Sunset Park pier is the one for sunset.', last=True))
    inner += gut(pl_ending(['All of New York', 'Everyone, in Life']), top=28)
    return phone2(inner)

# ───────────────────────────── 02.4 · the Print Room, opened ─────────────────────────────
def opened(reply_text=None, sent=False):
    inner = header('Maya', 'Thursday &middot; to friends', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 240, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{by("Maya", "print_room")[2]}</div>', top=16)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; border-top: 1px solid rgba(27,23,20,0.08); border-bottom: 1px solid rgba(27,23,20,0.08);">{thumb("room", 48)}<div style="flex: 1;">{title(PLACE_NAMES["print_room"], 16, 20, 600)}{when_line("Red Hook &middot; Tue&ndash;Sun 11&ndash;6 &middot; <i>Rooms Remade</i> through Sunday")}{src("Listed hours, not checked today")}</div>{CHEV}</div>', top=18)
    if reply_text is None:
        inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.14); border-radius: 22px; padding: 0 16px;"><span style="font-size: 15px; color: {GHOST}; flex: 1;">Reply to Maya</span></div>', top=18)
    else:
        inner += gut(f'<div style="border: 1.5px solid {INK}; border-radius: 22px; padding: 10px 16px;"><div style="font-size: 15px; line-height: 20px; color: {INK};">{reply_text}</div></div>'
                     f'<div style="display: flex; align-items: center; gap: 14px; margin-top: 10px;"><span style="background: {UMBER}; color: {CARD}; border-radius: 999px; padding: 9px 18px; font-size: 14px; font-weight: 600;">Send to Maya</span><span style="font-size: 12.5px; color: {MUTE};">She&rsquo;ll see this. Nothing else changes.</span></div>', top=18)
    inner += sect('From the gallery') + gut(f'<div style="display: flex; gap: 12px; align-items: flex-start;">{thumb("room", 44)}<div style="flex: 1;">{title("The side room, then and now", 15, 20, 600)}<div style="font-size: 14px; line-height: 19px; color: {INK2}; margin-top: 3px;">The print shop that was here left the drying racks; the show hangs the new work on them.</div>{src("The gallery&rsquo;s own notes")}</div></div>')
    inner += sect('Also about the Print Room') + gut('<div>' + share_line('P', 'Priya', by('Priya', 'print_room')[2], 'her own visit, a rainy Tuesday', last=True) + '</div>')
    inner += gut(door('Ask about the Print Room') + src('Asks Vesper, not Maya'), top=16)
    return phone2(inner)

def reader_phone(compose=''):
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

def recipient_inset():
    """S1/S2 coverage for a share: the workbench's proposed 'Who gets it' sheet (02B lane 1), reused for Maya's share.
    Eligible connections only; one recipient found, told apart, chosen or corrected; the exact outgoing material; send or leave; the result."""
    def cand(letter, name, how, on, bg='#1B1714'):
        tick = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7.2l2.6 2.6L11 4.4" stroke="#1B1714" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' if on else '')
        return (f'<div style="display: grid; grid-template-columns: 28px 1fr 16px; column-gap: 12px; align-items: center; padding: 11px 0; border-bottom: 0.5px solid var(--vk-borderHairline);">'
                f'<span class="vk-t-capsMicro" style="width: 28px; height: 28px; border-radius: 14px; background: {bg}; color: #FBF7EC; display: flex; align-items: center; justify-content: center; font-weight: 700;">{letter}</span>'
                f'<div><div class="vk-t-bodyMd" style="color: var(--vk-ink00);">{name}</div><div class="vdl-t-supportLine" style="color: var(--vk-ink60);">{how}</div></div>{tick}</div>')
    sheet = ('<div class="vdl-sheet" style="border-radius: 18px 18px 18px 18px; padding-bottom: 18px;">'
             '<div class="vdl-sheet-handle"></div>'
             '<div class="vdl-sheet-head"><div class="vdl-t-metaLine" style="color: var(--vk-ink60);">THE HARBOR PRINT ROOM &middot; YOUR SHARE</div><div class="vdl-t-sectionHeading" style="font-size: 15px; margin-top: 2px;">Who gets it</div></div>'
             '<div style="border-top: 0.5px solid var(--vk-borderHairline);">'
             + cand('F', 'Friends', 'everyone you&rsquo;re connected with', False, '#8A6628')
             + cand('N', 'Nora Lin', 'friend &middot; the pasta nights', True)
             + cand('N', 'Nora Kaye', 'friend &middot; from work', False) + '</div>'
             '<div class="vdl-field pill focused" style="margin-top: 14px;"><span class="vk-t-bodyMd">norra</span></div>'
             '<div class="vk-t-caption" style="color: var(--vk-ink60); margin-top: 6px;">No one named norra among the people you&rsquo;re connected with. Check the name. No contacts are scanned.</div>'
             '<div class="vdl-sheet-actions"><span class="vdl-btn primary pill vk-t-labelSemibold" style="color: var(--vk-color-white); width: 100%; box-sizing: border-box;">Done</span></div></div>')
    body = (sheet
            + '<div class="vdl-t-supportLine" style="color: var(--vk-ink40);">Back on the share: Who reads <b>Nora Lin</b>, through Sunday. What goes is exactly what is drawn above it: her photograph, &ldquo;The side room was my favorite. Go on a weekday, it was empty.&rdquo;, the Print Room, Red Hook. Leaving sends nothing.</div>'
            + dci('Notice', 64, tone='applied', title='Sent to Nora only · 4:05', body='Nothing else changed.')
            + dci('Notice', 120, tone='failed', title='Didn’t send. You’re offline.', body='Your words and your choice of Nora are still here.', primary='Try again', secondary='Not now'))
    return inset('02.2, CONTINUED &middot; CHOOSE OR CORRECT ONE RECIPIENT &middot; A STATE OF THE SAME SLOT', body,
                 'FOLLOWS THE WORKBENCH&rsquo;S PROPOSED S1 SHEET (02B, &ldquo;WHO GETS IT&rdquo;), STILL PROPOSED &middot; SHARED &middot; .vdl-sheet, .vdl-field, Notice (PLANS 90 J2c&ndash;J2e) &middot; ELIGIBLE CONNECTIONS ONLY, NO CONTACTS IMPORT, NO GENERAL FRIENDS PERMISSION &middot; A SECOND NORA IS FIXTURE, FOR TELLING TWO APART')

def reply_result_inset():
    body = (dci('Notice', 64, tone='applied', title='Sent to Maya · 9:12', body='Back to her photograph. Nothing else here changed.')
            + dci('Notice', 120, tone='failed', title='Didn’t reach Maya', body='Your reply is still in the field.', primary='Try again', secondary='Not now'))
    return inset('02.5, AFTER SEND TO MAYA &middot; THE RESULT, THEN THE SAME ORIGINAL', body,
                 'SHARED &middot; Notice &middot; THE RETURN IS HER ORIGINAL AS IT WAS, NOT A SUMMARY &middot; 02.6&rsquo;S PRIVATE ASK RETURNS TO THE SAME SCROLL')

# ───────────────────────────── 02.6 · Ask Vesper about this ─────────────────────────────
def ask_about_phone():
    inner = chat_head('THURSDAY 9:04 PM')
    inner += gut(ctx_chip('THE PRINT ROOM &middot; PRIVATE &middot; MAYA SEES NOTHING'), top=26)
    inner += gut(bubble('worth going before Sunday if I only have an hour?'), top=22)
    inner += gut(answer('Yes, if the hour is the side room. The show runs through Sunday and the gallery lists 11 to 6, so a weekday afternoon or Saturday morning both fit an hour; whether it is ticketed isn&rsquo;t confirmed, so bring a card. The pier is four minutes on if the light is good.', sig='FROM THE LISTING AND THE GALLERY&rsquo;S NOTES &middot; HOURS NOT CHECKED TODAY'), top=18)
    inner += gut(composer('Ask more'), top=30)
    inner += gut(door('Back to the Print Room'), top=22)
    return phone(inner, 0, active='Chat')

# ───────────────────────────── 02.7 · Maya's quiet return ─────────────────────────────
def maya_return_phone():
    inner = header('Yours', 'Thursday &middot; to friends &middot; through Sunday', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 220, tag="ILLUSTRATION &middot; NOT HER PHOTOGRAPH")}</div>', top=18)
    inner += gut(f'<div style="{SERIF} font-size: 22px; line-height: 30px; color: {INK};">{by("Maya", "print_room")[2]}</div>' + when_line(PLACE_NAMES['print_room'] + ' &middot; Red Hook'), top=16)
    inner += sect('A reply') + gut('<div>' + share_line('N', 'Nora', 'That side room. I want to see it before Sunday.', 'Thursday 9:12 pm', last=True) + '</div>' + door('Write back'))
    inner += gut(f'<div style="display: flex; gap: 22px; align-items: center;">{door("Edit")}{door("Take it back", MUTE)}</div>' + src('Friends, through Sunday.'), top=26)
    return phone2(inner)

# ───────────────────────────── the board ─────────────────────────────
def board02():
    P = [
        ('02.1', 'NORA', 'CHAT', ask_phone(), ('THURSDAY 7:50 PM', 'THE PRIVATE ASK', 'A photo and a question; one possible cause and one thing to change', 'THE &sect;8.1 SPECIMEN, REVISED &middot; HEAT IS ONE POSSIBILITY, NOT A DIAGNOSIS FROM A PHOTOGRAPH &middot; NO GUARANTEE ABOUT SATURDAY&rsquo;S BATCH &middot; NO SAVE PROMPT, NO SHARE PROMPT'),
         ('Nora', 'Chat, a photo of the pasta', 'Ask', 'The written answer; nothing kept', 'Private (T0); no post, no memory', 'Chat', '&mdash;', 'Done. Or share, deliberately'), ('FIXTURE', 'SYNTHETIC TECHNIQUE &middot; NO LIBRARY', 'T0 &middot; RULED')),
        ('02.2', 'MAYA', 'PLACES', share_draft_phone(), ('THURSDAY &middot; FROM THE PLACE PAGE', 'AN EXISTING FRIEND SHARES DIRECTLY', 'From the object; one line; who; Send', 'NO AI PRELUDE, NO OCCASION, NO CONNECTION SETUP &middot; THE AUDIENCE IS A DELIBERATE CHOICE PER SHARE'),
         ('Maya', 'The Print Room&rsquo;s place page', 'Share', 'Her picture and her words reach the people she chose', 'Friends, through Sunday; place precision as declared', 'Contribution', 'Friends see a photo and a line in their scope', 'Sent once; or not'), ('FIXTURE', 'A SEND CROSSES AN AUDIENCE BOUNDARY: T2, CARRIED BY THE ONE CLEAR SEND', 'D1 &middot; D6: PER-SHARE AUDIENCE')),
        ('02.3', 'NORA', 'PLACES', friends_scope_phone(), ('THURSDAY &middot; FROM FRIENDS', 'PLACES IS WORTH OPENING', 'Maya&rsquo;s photo; Priya&rsquo;s three-stop map; the pigeons; Dana elsewhere; Red Hook anyway', 'COPY OF R1 WITH THE LEDGER&rsquo;S CAST &middot; RICH SUPPLY, ONE NON-PHOTO MEDIUM &middot; ENJOY IT AND LEAVE'),
         ('Nora', 'Places &middot; From friends', 'Open', 'A friend&rsquo;s view of a place; the wider world', 'Nothing kept by looking', 'Places', '&mdash;', 'Enjoy it and leave'), ('COPY OF PLACES 04 &middot; 09-07', 'C6, C7 GIVEN', 'A1 MAY-SEE &middot; A3 A DOORWAY')),
        ('02.4', 'NORA', 'PLACES', reader_phone(), ('THE PRINT ROOM, OPENED', 'THREE THINGS KEPT APART', 'Her words; the listing; the gallery&rsquo;s notes', 'ORIGINAL FIRST &middot; DATED WORLD INFORMATION IN THE UNVERIFIED REGISTER &middot; EACH LINE CARRIES ITS OWN SOURCE, SO NO SENTENCE HAS TO SAY WHAT IT IS NOT &middot; DISPLAY IS NOT RETENTION AND NOT AI PERMISSION'),
         ('Nora', 'The share', 'Open', 'Her line, the place, what the gallery says', 'Same', 'Places / Entity', '&mdash;', 'Back to the same scroll'), ('SHARED &middot; OriginalReader full, show reader + ask &middot; vdl-stage1 0.4.1', 'THE SELECTED ORDER: ORIGINAL &rarr; REPLY &rarr; GALLERY NOTES &rarr; PRIYA &rarr; PRIVATE ASK &middot; MEDIA SUPPLIED', 'D5 &middot; ORIGINAL LEADS')),
        ('02.5', 'NORA', 'IN CONTEXT', reader_phone(compose='That side room. I want to see it before Sunday.'), ('THE SAME PLACE', 'REPLY TO MAYA, IN CONTEXT', 'Her words; the recipient obvious; no trip to Chat', 'THE COMPOSE / SEND BOUNDARY CARRIES THE CLARITY &middot; NOT A MEMORY, NOT AN EDIT TO THE PLACE'),
         ('Nora', 'The same photo', 'Reply to Maya', 'Her words to Maya', 'Maya only; sends nothing until sent', 'Chat (directed)', 'Maya: a message from Nora', 'Back to the photo'), ('SHARED &middot; OriginalReader full, compose, show reader + ask &middot; vdl-stage1 0.4.1', 'D2 STARTING POSITION: REPLY', 'NO REACTION COUNT &middot; RESULT BELOW')),
        ('02.6', 'NORA', 'CHAT', ask_about_phone(), ('THE SAME PLACE', 'ASK VESPER ABOUT THIS', 'Private; Maya receives nothing; world help only', 'WITHOUT THE &sect;8.3 GRANT A1 IS NOT SENT TO THE MODEL &middot; THE CHIP SAYS WHO IS ASKED &middot; RETURN RESTORES THE SCROLL'),
         ('Nora', 'The same photo', 'Ask Vesper about this', 'A private answer from the listing and the gallery&rsquo;s notes', 'Nobody; Maya receives nothing', 'Chat (private)', '&mdash;', 'Return restores the question, form and scroll'), ('FIXTURE', 'THE ONE CHAT APERTURE PER PAGE &middot; GIVEN', 'T0')),
        ('02.7', 'MAYA', 'PLACES', maya_return_phone(), ('MAYA, LATER', 'THE SENDER&rsquo;S QUIET RETURN', 'Her share is still hers; a reply arrived', 'EDIT &middot; TAKE IT BACK &middot; NO VIEWER LIST, NO COUNT, NO USE REPORT &middot; SILENCE NEEDS NO EXPLAINING'),
         ('Maya', 'Her own contribution', 'Look', 'Her photo is hers; Nora&rsquo;s reply', 'No viewer list, no use report', 'Contribution', 'Herself', 'Nothing owed'), ('FIXTURE', 'R5&rsquo;S USE REPORT NOT INHERITED', 'C4 WITHDRAWAL IS ON 04')),
    ]
    cols = [colu(ph, cap(n, role, root, *c), under(r, s)) for n, role, root, ph, c, r, s in P]
    cols[1] = cols[1][:-6] + recipient_inset() + '</div>'
    cols[4] = cols[4][:-6] + reply_result_inset() + '</div>'
    row1, row2 = cols[:4], cols[4:]
    notes = [notecol('What board 02 shows', [
        ('RECEIVE AND LEAVE IS COMPLETE', N('02.3 ends after Maya&rsquo;s photograph. No reply, save or summary is asked. The scope is the ledger&rsquo;s cast (Maya, Priya, Dana) on the Places project&rsquo;s own composition; the wider world sits under it so Red Hook is worth opening even with three friends.')),
        ('TWO RECIPIENTS, TWO FRAMES', N('02.5 and 02.6 start from the same photograph. Reply is the reference&rsquo;s in-context composer with Maya named at the send boundary. Ask is a Chat frame whose chip names Vesper and says Maya sees nothing; it answers from the listing and the gallery&rsquo;s notes because the ledger&rsquo;s scoped-use assumption (&sect;8.3) is not taken here. Board 05 draws the granted variant beside it.')),
        ('SHARING WITHOUT A PRELUDE', N('02.2 is a friend sharing from the object itself: Maya, from the Print Room&rsquo;s page, one line, who, Send. No Chat first, no Occasion, no connection to accept. The audience is chosen per share; a send crosses an audience boundary and the one clear Send carries it. 02.1 stays as the private answer that keeps nothing.')),
        ('THE SENDER', N('02.7 keeps R5&rsquo;s exclusion: no &ldquo;used in&rdquo; report. Maya sees her share, one reply, Edit and Take it back. On board 04 the same page is where withdrawal happens.')),
        ('NOT DRAWN', N('B0 (&ldquo;thinking of Saturday&rdquo;) is board 05&rsquo;s D1 pair. A Paris/Rome contrast is omitted per the ledger. The KEPT receipt with Undo after 02.2 is the Home project&rsquo;s kept-row form and is not repeated here.')),
    ], w=430)]
    body = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(row1) + '</div>'
            + f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">FROM THE SAME PHOTOGRAPH</div><div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Reply, ask, and what the sender sees</div></div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + ''.join(notes) + '</div>')
    html = (HEAD_VDL + f'<div style="width: 1820px; min-height: {hh("02")}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head(f'VESPER &middot; SOCIAL EXPERIENCE &middot; 02 &middot; A LITTLE OF YOUR WORLD &middot; {STAMP}', '02 &middot; A little of your world',
                   'Can giving and receiving feel casual while the material opens real value, without a post-production ritual or a demand to act? Seven slots, revised per &sect;14: the private answer that keeps nothing; an existing friend sharing directly from an eligible object; a friends scope with rich supply and one non-photo medium; the place opened with its three registers kept apart; Reply and Ask from the same photograph; the sender&rsquo;s quiet return. Policy stays outside the phones.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOT2}</div></div>' + TAIL)
    return html

FILES = {'02 - A little of your world': board02}
if __name__ == '__main__':
    for n, f in FILES.items():
        h = f(); open(os.path.join(OUT, n + '.dc.html'), 'w').write(h); print('wrote', n, len(h))
