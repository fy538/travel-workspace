"""05 · One gathering, different participation (package B). One host, one active contributor, one guest without the app,
someone who comes for dinner only, someone who declines. A real objection, a change after agreement, and a short
practical-help comparison. Reuses E1's frames where they already do the job."""
from mp_kit2 import *
import gen_e1
from gen_merge import daycap
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
APP = tag('NO APP', OX, 'rgba(122,46,46,0.10)')

def objection():
    inner = header('Pasta night', 'Saturday &middot; you&rsquo;re hosting', back=True)
    inner += sect('Answers so far', top=20) + gut(original(80, author='Maya', meta='THURSDAY · TO THE GROUP', words='in. bringing the recipe and lemons')
        + f'<div style="margin-top: 14px;">{rule(original(96, author="Priya", meta="THURSDAY · TO THE GROUP", words="can we not do 6? i&rsquo;m at work till 6:30"), 14)}</div>'
        + f'<div style="margin-top: 14px;">{rule(original(80, author="Dana", meta="THURSDAY · TO THE GROUP", words="can&rsquo;t saturday. have fun"), 14)}</div>')
    inner += gut(box(says('You could split it: cooking from 6:00, eating around 7:00, join for either. Priya makes dinner, and the cooking still happens.', 16, 23)
        + f'<div style="margin-top: 10px;">{actions(btn("Send the change"), door("Keep 6:00", MUTE))}</div>'), top=16)
    return phone2(inner, active='Home')

def agreed():
    inner = header('Pasta night', 'Saturday &middot; cooking 6:00, eating 7:00', back=True)
    inner += gut(bubble('new plan: cooking from 6, eating around 7. come for either'), top=18)
    inner += gut(f'<div style="display: flex; flex-direction: column; gap: 8px;">{bubble_in("just dinner works. thank you", "Priya")}{bubble_in("6 for me", "Maya")}</div>', top=10)
    inner += sect('Coming') + gut('<div>'
        + line('Maya &middot; <span style="color: #6E6862;">from 6:00 · the recipe, lemons</span>', mark='dot', color=GREEN)
        + line('Sam &middot; <span style="color: #6E6862;">from 6:45 · Maya&rsquo;s meeting him downstairs</span>', mark='dot', color=GREEN)
        + line('Priya &middot; <span style="color: #6E6862;">dinner, from 7:00 · bread</span>', mark='dot', color=GREEN)
        + line('Dana &middot; <span style="color: #6E6862;">can&rsquo;t come</span>', mark='none', muted=True, last=True) + '</div>')
    return phone2(inner, active='Home')

def changed():
    inner = anchor_row('NEW YORK', 'SATURDAY 4:35 PM')
    inner += orientation('Maya&rsquo;s train was cancelled.', 'She won&rsquo;t make 6:00.')
    inner += gut(original(96, author='Maya', meta='4:31 PM · TO YOU', words='stuck in newark, train cancelled. i&rsquo;ll be there by 8. SORRY'), top=16)
    inner += sect('What was hers tonight') + gut('<div>'
        + line('The recipe and the lemons', mark='hollow', color=OX)
        + line('Meeting Sam downstairs at 6:45', mark='hollow', color=OX, last=True) + '</div>')
    inner += gut(actions(btn('Ask Maya for the recipe'), btn('Tell Sam I&rsquo;ll meet him', False)), top=12)
    inner += gut(quiet('Sam still expects Maya at 6:45.'), top=10)
    return phone2(inner, active='Home')

def sam_update():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div class="fn" style="color: {MUTE};">FROM NORA &middot; SATURDAY 4:40 PM</div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Pasta night, tonight.</div>', top=10)
    inner += gut(original(96, author='Nora', meta='4:40 PM · TO YOU', words='Change of plan: I&rsquo;ll meet you downstairs at 6:45, not Maya. Her train got cancelled.'), top=16)
    inner += sect('Tonight', top=24) + gut('<div>'
        + line('6:45 &middot; <span style="color: #6E6862;">Nora, downstairs</span>', mark='dot', color=GOLDD)
        + line('Eating around 7:00', mark='dot', color=GOLDD, last=True) + '</div>')
    inner += gut(actions(btn('Got it'), door('Reply to Nora', MUTE)), top=18)
    return webframe(inner)

def record():
    inner = header('Pasta night', 'Saturday, October 3', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 150, tag="PHOTO &middot; SAM &middot; 8:25 PM")}</div>', top=18)
    inner += sect('Who was there') + gut('<div>'
        + line('You', mark='dot', color=GOLDD) + line('Sam &middot; <span style="color: #6E6862;">from 6:45</span>', mark='dot', color=GOLDD)
        + line('Priya &middot; <span style="color: #6E6862;">dinner · left at 8:30</span>', mark='dot', color=GOLDD)
        + line('Maya &middot; <span style="color: #6E6862;">from 8:00, with lemons</span>', mark='dot', color=GOLDD, last=True) + '</div>')
    inner += sect('Also') + gut(original(96, author='Dana', meta='SATURDAY 5:10 PM · TO YOU', words='since i can&rsquo;t come: zest goes in at the very end, off the heat. trust me'))
    return phone2(inner, active='Life')

def help_ask():
    inner = avatar_for(bar('TO FRIENDS', 'MONDAY'), 'P')
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain("moving saturday. any of these would help: an hour of carrying, a car for one run, dinner after", size=17, lh=24)}</div>', top=18)
    inner += gut(f'<div class="kickm" style="margin-bottom: 8px;">TO</div><div style="display: flex; gap: 8px; flex-wrap: wrap;">'
        + ''.join(f'<span class="vdl-recipient"><span class="vdl-avatar ink sm vk-t-capsMicro">{l}</span><span class="vk-t-bodySmMedium">{n}</span></span>' for l, n in (('N','Nora'),('M','Maya'),('D','Dana'))) + '</div>', top=20)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=22)
    return phone2(inner, active='Chat')

def help_state():
    inner = avatar_for(header('Moving, Saturday', 'What you asked for', back=True), 'P')
    inner += sect('A car for one run', top=20) + gut(original(80, author='Nora', meta='TUESDAY · TO YOU', words='i can do the car run, but only until 11')
        + f'<div style="margin-top: 8px;">{actions(btn("Yes, 9:30?"), door("Thanks, I&rsquo;m covered", MUTE))}</div>')
    inner += sect('Dinner after') + gut(original(80, author='Maya', meta='TUESDAY · TO YOU', words='dinner&rsquo;s on me. 7?') + f'<div style="margin-top: 6px;">{quiet("You said yes · Tuesday")}</div>')
    inner += sect('An hour of carrying') + gut(quiet('Nobody yet.') + f'<div style="margin-top: 6px;">{actions(door("Ask someone else"), door("Drop it", MUTE))}</div>')
    return phone2(inner, active='Home')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))

def build():
    r1 = [cell('THURSDAY', '1', 'Sam&rsquo;s invitation', 'Host-authored, no profiles, and &ldquo;join for either.&rdquo; From E1, unchanged.', gen_e1.invitation(), (APP, P('E1'))),
          cell('THURSDAY', '2', 'One private need', 'He asks Vesper; Vesper cannot arrange a person; he sends Nora his own words. From E1.', gen_e1.brief(), (APP, P('E1'))),
          cell('THURSDAY', '3', 'A real objection', 'Priya can&rsquo;t do 6:00. Dana can&rsquo;t come at all, and gives no reason. Vesper offers one change; Nora decides whether to send it.', objection(), (P('NEW'),)),
          cell('THURSDAY', '4', 'Agreed, in their words', 'The change is agreed when Priya and Maya say so. Dinner-only is a line on the list, not a lesser answer.', agreed(), (P('NEW'),))]
    r2 = [cell('SATURDAY', '5', 'After agreement, the world moves', 'Maya had two jobs tonight. Both are now open, and the screen says who is still relying on the old plan.', changed(), (P('NEW'),)),
          cell('SATURDAY', '6', 'Sam hears it from Nora', 'A signed change, by link. He installed nothing.', sam_update(), (APP, P('NEW'))),
          cell('SUNDAY', '7', 'How it went', 'Four different ways of being there, recorded plainly. Dana was part of it from Sorrento. Nobody is asked to debrief.', record(), (P('NEW'),)),
          cell('THE FOLLOWING WEEK', '8', 'A comparison: help with a move', 'Priya names three useful things. Two are taken up, one by a counter-offer. One is still open, and says so.', help_ask() + f'<div style="height: 18px;"></div>' + help_state(), (P('NEW'), P('D4')))]
    rows = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(r1) + '</div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 8px;">' + ''.join(r2) + '</div>')
    n1 = notes('FOR EACH PERSON: RECEIVES &middot; WORK GONE &middot; EFFORT STILL THEIRS &middot; BARELY USING VESPER?', tbl(['', 'RECEIVES', 'WORK THAT DISAPPEARS', 'STAYS THEIRS', 'BARELY USING IT?'], [
        ['<b>Nora</b>, host', 'One clear request from Sam; one workable change when Priya objects; at 4:35, exactly what Maya&rsquo;s delay leaves undone', 'Guessing what a newcomer needs; re-polling for a time; working out who is affected by a cancelled train', 'Inviting, deciding, meeting Sam at the door', 'No. She is the one person who uses it fully'],
        ['<b>Maya</b>, contributor', 'Nothing she did not ask for', 'None', 'Offering the recipe, agreeing to meet Sam, apologizing in her own words', 'Yes: four messages'],
        ['<b>Sam</b>, guest, no app', 'What the evening is; that dinner-only is fine; someone at the door; the change, from Nora', 'Asking a room of strangers', 'Asking Nora, under his name', 'Yes: two links. <b>Conditional</b> on the unresolved guest path'],
        ['<b>Priya</b>, dinner only', 'A plan she can make', 'Explaining or apologizing', 'Saying 6:00 doesn&rsquo;t work', 'Yes'],
        ['<b>Dana</b>, declined', 'Nothing asked of her', 'An excuse', 'Sending the zest tip, because she felt like it', 'Yes'],
    ]), w=1100)
    n2 = notes('AGAINST A GOOD GROUP CHAT AND AN INVITATION TOOL', led([
        ('WHAT THEY ALREADY DO', 'Everything in frames 3 and 4 is an ordinary thread. Partiful already has private host-visible answers and photos afterward. Nothing here should be harder than those.'),
        ('WHAT DISAPPEARS', 'For Nora only: at 4:35 she does not have to reconstruct that Maya held the recipe <i>and</i> Sam&rsquo;s arrival, or remember that Sam has no way to know. For Sam: he never joins a thread of strangers.'),
        ('WHAT IT COSTS', 'Sam needs a working link path, which does not exist yet. Nora does the most, and still decides everything.'),
        ('HELP, FRAME 8', 'Availability offered, what Priya accepted, and what is still open are three different states. Completion is not tracked. Meal Train already coordinates this well for a household; this is one bounded ask between friends, not that service.'),
    ]), w=620)
    body = rows + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(4, (1100, 620))}px; min-height: {hh("05", 3600)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('05 &middot; PACKAGE B &middot; COMPOSITION', 'One gathering, different participation',
                   'A host, an active contributor, a guest without the app, someone who comes for dinner only, and someone who declines. It has a real objection, a change after everything was agreed, and a natural ending. '
                   'Then one short comparison: the same parts, used for help with a move. Drawn, not tested with anyone.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('05 - One gathering different participation', html)

if __name__ == '__main__':
    print(build())
