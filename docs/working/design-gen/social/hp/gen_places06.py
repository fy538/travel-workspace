"""06 - E · Taking W2 forward without losing the exploration: the private ask, the prepared suggestion unsent, the send
through the existing owner and its readback, back to B; and the E variation: for me / with Maya / around the dinner, with
one bounded practical change. Fixture copy only. Thin-guest and pre-Plan capabilities are marked as dependencies."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from kit import *
from gen_generous import caption, col, head, FOOT, N, arow, compare2, body, facepile
from gen_generous3 import sect, meta, title, sup, gut, u2, card, fact
from gen_places import scope_header, map_wash, branch, places_phone, ICON_TIDE
from gen_merge import tbl, daycap, page
from gen_placeskit import question_control, STAMP, hh, OUT, comparison_triplet
from gen_places02 import notecol
from gen_places03 import field_phone as b_field, occurrence_phone, lead_w2, w4_evening
from gen_seam import chip

HAIR = 'rgba(27,23,20,0.10)'
def ctx_pill(t):
    return f'<div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid {HAIR}; background: {CARD}; border-radius: 12px; padding: 8px 12px;"><span style="width: 6px; height: 6px; border-radius: 3px; background: {GOLD};"></span><span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {INK};">{t}</span></div>'

def ask_phone():
    inner = (f'<div style="padding: 24px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 10px;">{BACK}<span style="{MONO} font-weight: 700; font-size: 11px; letter-spacing: 1.15px;">CHAT</span><span class="fn" style="margin-left: auto;">FRIDAY 12:31 PM</span></div></div>')
    inner += gut(ctx_pill('THE LISTENING HOUR &middot; SAT 7&ndash;9 &middot; FROM PLACES') + f'<div style="font-size: 12.5px; line-height: 17px; color: {MUTE}; margin-top: 10px;">The occurrence, its venue, and Saturday&rsquo;s dinner (8:15, Maya and Alex, settled) arrive as context. Nothing about Maya beyond the dinner is used.</div>', top=26)
    inner += gut(f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 300px; background: {UMBER}; color: {CARD}; border-radius: 18px 18px 4px 18px; padding: 12px 14px; font-size: 15px; line-height: 20px;">could Maya and I do this after dinner?</div></div>', top=24)
    inner += gut(f'<div style="max-width: 330px; display: flex; flex-direction: column; gap: 10px;"><div style="{SERIF} font-size: 17px; line-height: 24px; color: {INK};">Not after: the hour runs 7 to 9 and your table is 8:15, so they overlap. Before dinner would work: doors 6:45, and the hall is a short way from the table. Whether Maya is free before dinner I can&rsquo;t know; I have only the dinner itself.</div>'
                 f'<div class="fn" style="color: {ANCHOR};">USED: THE HOUR&rsquo;S WINDOW, THE DINNER&rsquo;S TIME AND PLACE &middot; NOT USED: MAYA&rsquo;S CALENDAR, MESSAGES, OR ANYTHING PRIVATE TO HER</div></div>', top=18)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px; min-height: 44px; border: 1px solid rgba(27,23,20,0.12); border-radius: 999px; padding: 0 16px;"><span style="font-size: 14px; color: {GHOST}; flex: 1;">Ask, or say what to prepare</span></div>', top=30)
    inner += f'<div style="padding: 30px 34px 6px 34px; text-align: center;"><div class="fn">PRIVATE PREPARATION &middot; BOUNDED UNKNOWNS &middot; NOTHING SENT &middot; PLACES UNCHANGED</div></div>'
    return phone(inner, 0, active='Chat')

def suggestion_card(sent=False):
    kick = 'SENT TO MAYA &middot; ONE IDEA &middot; 12:34 PM' if sent else 'PREPARED &middot; NOT SENT'
    inner = (f'<div class="kick" style="color: {GOLDD if sent else MUTE};">{kick}</div>'
             + f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 25px; margin-top: 6px;">The listening hour before dinner, Saturday</div>'
             + sup('Doors 6:45 at Canal Hall; leave by 8 for the 8:15 table. Admission $12 at the door, as listed; whether seats remain is not known.', INK2)
             + f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 10px;">{facepile(["you", "M"], 24, -6)}<span class="fn" style="color: {ANCHOR};">{"AN IDEA SHE CAN ANSWER OR IGNORE &middot; NOTHING IS ARRANGED" if sent else "TO MAYA, IF YOU SEND IT &middot; SENDING AN IDEA IS NOT AN INVITATION SHE ACCEPTED"}</span></div>')
    return card(inner)

def unsent_phone():
    inner = scope_header('THE LISTENING HOUR', 'Saturday 13 &middot; 7&ndash;9 PM &middot; Canal Hall', back=True)
    inner += gut(suggestion_card(), top=22)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 10px;">' + door('Send to Maya') + meta('OPENS THE EXISTING ARRANGEMENT OWNER &middot; EXACT AUDIENCE AND EFFECT ARE DECIDED THERE', 0) + door('Keep it to myself', MUTE) + meta('READ THE HOUR AND LEAVE IS AN EQUALLY COMPLETE ENDING', 0) + '</div>', top=22)
    inner += gut(f'<div style="border: 1px dashed rgba(122,46,46,0.5); border-radius: 12px; padding: 10px 12px;"><span class="fn" style="color: {OX};">DEPENDENCY, OUTSIDE THE DESIGN FRAME &middot; A PRE-PLAN SUGGESTION TO ONE PERSON AND THE THIN-GUEST PATH ARE NOT IMPLEMENTED &middot; THIS DOOR IS NOT A WORKING BUTTON</span></div>', top=26)
    inner += sect('The hour, as before') + gut('<div>' + fact('WHAT IT IS', 'One recording, played end to end, in the back room with the lights down.') + fact('AVAILABILITY', 'Not known. The hall&rsquo;s own page is where it is settled.', last=True) + '</div>')
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">VISIBLY UNSENT &middot; PRIVATE UNTIL THE PERSON CHOOSES &middot; THE EXPLORATION IS STILL UNDERNEATH</div></div>'
    return places_phone(inner, 0)

def sent_phone():
    inner = scope_header('THE LISTENING HOUR', 'Saturday 13 &middot; 7&ndash;9 PM &middot; Canal Hall', back=True)
    inner += gut(suggestion_card(sent=True), top=22)
    inner += gut('<div style="display: flex; flex-direction: column; gap: 10px;">' + door('The idea, with Maya') + meta('THE EXACT DESTINATION: THE ARRANGEMENT OWNER &middot; HER ANSWER, IF ANY, ARRIVES THERE AND ON HOME', 0) + door('Back to Saturday evening') + '</div>', top=22)
    inner += gut(u2('What changed, and what did not', 'One idea reached Maya. No table moved, no seat was bought, nothing was added to Life for having been looked at. Home may show her answer as an addressed consequence; Places shows the hour as it always did.', meta_t='READBACK, CONCISE &middot; NO DUPLICATE EVENT IN HOME OR LIFE MERELY BECAUSE IT WAS VIEWED'), top=26)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">A SUPPORTED EFFECT, READ BACK ONCE &middot; SHARE IS NOT INVITE; INVITE IS NOT ATTENDANCE</div></div>'
    return places_phone(inner, 0)

def back_phone():
    return b_field(return_strip=True)

def triplet_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Friday 12:36 PM') + question_control('Saturday evening', 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', 'ONE WORLD &middot; THREE LENSES &middot; SAME FACTS')
    inner += gut(comparison_triplet(), top=22)
    inner += sect('Around Saturday&rsquo;s dinner') + gut(lead_w2().replace('This Saturday&rsquo;s hour', 'This Saturday&rsquo;s hour, before the table'))
    inner += gut(arow('Dinner with Maya and Alex &middot; Saturday 8:15 &middot; <span style="color: #6E6862;">settled &middot; the noodle bar &middot; supplied context, not changed here</span>', avatars=['M', 'A', 'you'], last=True), top=22)
    inner += gut(u2('The pier at sunset', 'Too far from the table to fit before 8:15 by any way that is known; it stays in the world, not in this lens.', meta_t='A CHANGED QUESTION MAY CHANGE ELIGIBLE CANDIDATES &middot; NOT AN IDENTICAL INVENTORY BY RULE'), top=22)
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">CHOOSING A LENS GRANTS NOTHING, SENDS NOTHING, ADOPTS NOTHING &middot; THE DINNER IS THE OCCASION&rsquo;S, NOT PLACES&rsquo;</div></div>'
    return places_phone(inner, 0)

def change_phone():
    inner = scope_header('NEW YORK', 'Selected, not measured &middot; Saturday 5:50 PM') + question_control('Saturday evening', 'NEW YORK').replace('CLEAR &rarr; BACK TO NEW YORK', 'AROUND THE DINNER &middot; ONE THING CHANGED')
    inner += gut(u2('The noodle bar&rsquo;s kitchen closes at 9 tonight', 'The table is still 8:15; the kitchen&rsquo;s last orders moved earlier than listed. The hour ends at 9, so the plan of hour-then-dinner no longer fits; hour-before-dinner still does, and so does dinner alone.',
                    meta_t='THE CHANGE, EXPLAINED &middot; THE PLACE CHANGED, NOT THE ARRANGEMENT &middot; AS OF 5:40 PM, FROM THE BAR&rsquo;S LISTING'), top=22)
    inner += sect('What still works') + gut('<div>' + branch('<svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M4 18 V8 L11 4 L18 8 V18" stroke="#8A6628" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 18 V12 H14 V18" stroke="#B0853A" stroke-width="1.3"/></svg>', 'The hour, then leave by 8', 'Doors 6:45; the table at 8:15 holds', 'last orders 9') + branch(ICON_TIDE, 'Skip the hour; the table as it is', 'Nothing to change', 'last orders 9') + '</div>')
    inner += gut('<div style="display: flex; flex-direction: column; gap: 10px;">' + door('Change the dinner, with Maya and Alex') + meta('OPENS THE EXISTING ARRANGEMENT OWNER &middot; PLACES DOES NOT MOVE A TABLE', 0) + '</div>', top=22)
    inner += sect('Unaffected') + gut('<div>' + row('The Print Room &middot; <span style="color: #6E6862;">Sunday afternoon instead</span>', mark='hollow', muted=True) + row('The pier at sunset &middot; <span style="color: #6E6862;">a different evening</span>', mark='hollow', muted=True, last=True) + '</div>')
    inner += f'<div style="padding: 36px 34px 6px 34px; text-align: center;"><div class="fn" style="color: {ANCHOR};">ONE BOUNDED CHANGE &middot; ALTERNATIVES OFFERED &middot; THE REST OF THE EXPLORATION PRESERVED &middot; NO BOOKING STORY</div></div>'
    return places_phone(inner, 0)

def board():
    row1 = [col(ask_phone(), daycap('FROM THE HOUR &middot; CHAT', '1 &middot; THE PRIVATE ASK', '&ldquo;Could Maya and I do this after dinner?&rdquo;', 'PREPARATION USES ONLY THE SUPPLIED DINNER FACTS &middot; MAYA&rsquo;S AVAILABILITY IS NOT INFERRED &middot; NOTHING SENT')),
            col(unsent_phone(), daycap('BACK IN PLACES', '2 &middot; A SUGGESTION, VISIBLY UNSENT', 'Prepared, private, with the exact effect decided elsewhere', 'SEND OPENS THE EXISTING OWNER &middot; THIN-GUEST AND PRE-PLAN MARKED AS DEPENDENCIES, NOT WORKING BUTTONS')),
            col(sent_phone(), daycap('AFTER SENDING', '3 &middot; READBACK AND THE EXACT DESTINATION', 'One idea reached Maya; nothing else changed', 'SHARE &ne; INVITE &ne; ATTENDANCE &middot; NO DUPLICATE IN HOME OR LIFE FOR HAVING BEEN VIEWED')),
            notecol('Open, ask, propose, return', [
                ('1 &middot; VALUE BEFORE ACTION', N('The answer to the question is itself the value: the hour and the dinner overlap, so &ldquo;after&rdquo; is out and &ldquo;before&rdquo; is in. It uses the two supplied facts and says plainly what it cannot know. Reading it and doing nothing is complete.')),
                ('2 &middot; WHY THE SUGGESTION LOOKS LIKE THIS', N('It is a card because it is a coherent thing that can be sent; it is marked unsent in mute, and sent in gold-deep with the time. The door that sends it belongs to the existing arrangement owner, which decides audience and effect. The design does not depict a thin-guest or pre-Plan capability that does not exist; it marks the dependency in oxblood outside the phone&rsquo;s own grammar.')),
                ('3 &middot; THE RETURN', N('Back from any of these phones restores 03&rsquo;s Saturday-evening question, form and position (phone 4). Home may show Maya&rsquo;s answer as an addressed consequence; Life may hold the hour only if something eligible was retained. Neither receives a duplicate because the hour was looked at.')),
            ])]
    row2 = [col(back_phone(), daycap('BACK', '4 &middot; B&rsquo;S SCROLL, RESTORED', 'Saturday evening kept; the hour still selected', 'THE ALTERNATIVE ENDING, READ AND LEAVE, LANDS HERE TOO')),
            col(triplet_phone(), daycap('E VARIATION &middot; SHARED CONTEXT', '5 &middot; FOR ME &middot; WITH MAYA &middot; AROUND THE DINNER', 'Same world, three orderings; a lens grants nothing', 'RA15 CARRIED FORWARD &middot; A CHANGED QUESTION MAY CHANGE CANDIDATES &middot; NOT A SIXTH MODE')),
            col(change_phone(), daycap('SATURDAY 5:50 PM &middot; ONE THING CHANGED', '6 &middot; A BOUNDED PRACTICAL CHANGE', 'The kitchen closes early; Places explains and offers what still works', 'RA16 WITHOUT THE BOOKING STORY &middot; THE ARRANGEMENT CHANGES ONLY THROUGH ITS OWNER')),
            notecol('The lenses, the change, the supply', [
                ('5 &middot; THE THREE LENSES', N('The world facts do not move between lenses; order and eligibility do. Around the dinner, the pier drops out because no known way makes it fit before 8:15, and the hour is presented before the table. The dinner itself is supplied context from the Occasion owner and is never edited from here.')),
                ('6 &middot; THE CHANGE', N('A place changed, not the arrangement. Places explains the change with its source and time, offers the alternatives that still work, keeps the unaffected possibilities, and hands any actual change of the dinner to the existing owner. No hold, no booking, no transaction workflow is imported.')),
                ('SUPPLY TYPE, PER UNIT', tbl(['UNIT', 'SUPPLY', 'WHAT THAT MEANS'], [
                    ['The answer in Chat', 'On-demand, bounded', 'Two supplied facts and the hour&rsquo;s window; no private context of Maya&rsquo;s'],
                    ['The suggestion', 'Structured state', 'A sendable object; audience and effect owned elsewhere'],
                    ['The dinner row', 'Owner context (Occasion)', 'Read, never written, from Places'],
                    ['The kitchen change', 'Permitted existing facts, fresh', 'The bar&rsquo;s listing at 5:40; dated on the unit'],
                    ['The three orderings', 'Viewer-relative selection', 'Same corpus; the lens is a question, not a grant']])),
            ])]
    html = page(1900, hh('06', 4600), f'{STAMP} &middot; 06 &middot; E &middot; TAKING IT FORWARD', '06 &middot; E &middot; Can I open, compare, ask, keep, share or propose, then return to the same exploration?',
                'Situation E from the brief, starting from 03&rsquo;s exact scroll and selected occurrence: the private ask in Chat with bounded unknowns, the prepared suggestion visibly unsent, the send through the existing arrangement owner and its readback, and the return to B&rsquo;s question. Then the E variation: the same world for me, with Maya, and around Saturday&rsquo;s dinner, and one bounded practical change. Unsupported capabilities are marked as dependencies, never drawn as working buttons.', row1)
    divider = (f'<div style="margin-top: 40px; padding-top: 26px; border-top: 1px solid rgba(27,23,20,0.12); display: flex; flex-direction: column; gap: 6px;"><div class="kick" style="color: {GOLDD};">THE RETURN, THE LENSES, THE CHANGE</div>'
               f'<div style="{SERIF} font-weight: 600; font-size: 24px; line-height: 30px;">Back to the question; the same world three ways; one thing changes</div></div>'
               '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 26px;">' + ''.join(row2) + '</div>')
    return html.replace('<div class="fn" style="margin-top: 30px; line-height: 16px;">', divider + '<div class="fn" style="margin-top: 30px; line-height: 16px;">', 1)

if __name__ == '__main__':
    html = board(); open(os.path.join(OUT, '06 - E - Taking It Forward.dc.html'), 'w').write(html); print('wrote 06', len(html))
