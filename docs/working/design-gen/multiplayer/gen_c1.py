"""C1 · Copy, before and after. Six live frames beside the same frames rewritten under the proposed copy rules.
Left of each pair is the frame exactly as it is on its board today; right is a rewrite. Layout is unchanged except
where removing a sentence removed the box that held it."""
from mp_kit2 import *
import gen_d1, gen_d7, gen_e1, gen_e2, gen_e8
from gen_generous import facepile

BEF = tag('BEFORE &middot; AS LIVE TODAY', MUTE, 'rgba(110,104,98,0.12)')
AFT = tag('AFTER &middot; REWRITTEN', GREEN, 'rgba(61,112,80,0.14)')
def msg(t, size=17, lh=24):
    """A person's own words: sans, as typed. Not set in Vesper's serif."""
    return f'<div style="font-size: {size}px; line-height: {lh}px; color: {INK};">{t}</div>'
def chip(t):
    return f'<span style="{MONO} font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {INK2}; border: 1px solid {HAIR}; background: {CARD}; border-radius: 999px; padding: 4px 10px; white-space: nowrap;">{t}</span>'
def webframe(inner):
    return f'<div style="width: 393px; background: {PAPER}; {SANS} color: {INK};">{inner}<div style="height: 22px;"></div></div>'

# ───────── 1 · Home with two shares (D1 frame 2) ─────────
def a_home():
    inner = anchor_row('NEW YORK', 'FRIDAY 8:10 AM')
    inner += orientation('Maya&rsquo;s cake sank. Sam found a cinema.', '61&deg; and clear until four.')
    inner += sect('Maya') + gut(
        f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 150, tag="PHOTO &middot; MAYA")}</div>'
        + f'<div style="margin-top: 10px;">{msg("it sank 😭 still ate half of it")}</div>'
        + prov('MAYA &middot; LAST NIGHT &middot; TO FRIENDS')
        + f'<div style="margin-top: 2px;">{door("Reply")}</div>')
    inner += sect('Sam') + gut(msg('Found a cinema on Court Street that shows one film a week. They sell exactly one kind of cake. I think I love it here!')
        + prov('SAM &middot; WEDNESDAY &middot; TO FRIENDS')
        + f'<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 10px;">This week&rsquo;s film runs through Sunday. Nine minutes from you.</div>'
        + prov('LISTED &middot; NOT CHECKED TODAY'))
    inner += sect('Priya') + gut(msg('bread&rsquo;s out of the oven if anyone&rsquo;s near') + prov('PRIYA &middot; 7:52 AM &middot; TO FRIENDS'))
    inner += sect('Today') + gut(f'<div style="font-size: 15px; line-height: 21px; color: {INK};">Dentist Tuesday at 9:00. I&rsquo;d walk. The bus takes longer.</div>')
    return phone2(inner, active='Home')

# ───────── 2 · The quiet Sunday (D1 frame 4) ─────────
def a_quiet():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:40 AM')
    inner += orientation('Sunday. Clear until four.', 'Open until Tuesday&rsquo;s dentist.')
    inner += sect('A good morning for') + gut('<div>'
        + row('The greenmarket &middot; <span style="color: #6E6862;">open till 2, quietest before 10</span>', mark='dot', color=GOLDD)
        + row('The canal walk &middot; <span style="color: #6E6862;">twenty minutes, flat</span>', mark='dot', color=GOLDD, last=True) + '</div>'
        + prov('LISTED &middot; NOT CHECKED TODAY'))
    inner += sect('From friends this week') + gut('<div>'
        + row('Maya&rsquo;s cake &middot; <span style="color: #6E6862;">Thursday</span>', mark='hollow')
        + row('Sam&rsquo;s cinema &middot; <span style="color: #6E6862;">Wednesday</span>', mark='hollow', last=True) + '</div>')
    return phone2(inner, active='Home')

# ───────── 3 · The morning after a dinner (E1 frame 4) ─────────
def a_after():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 8px;"><span class="fn" style="color: {MUTE};">SUNDAY</span>{chip("JUST YOU")}</div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Nora&rsquo;s dinner, last night.</div>', top=10)
    inner += gut(box(person('M', 'Maya', 'from Nora&rsquo;s dinner &middot; the lemon argument')
        + f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 16px;">'
        + f'<div>{actions(btn("Save Maya"))}<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">Find her later as &ldquo;Maya, from Nora&rsquo;s dinner.&rdquo;</div></div>'
        + f'<div>{actions(btn("Swap details", False))}<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">If she says yes too, you each get the other&rsquo;s number.</div></div></div>'), top=16)
    inner += sect('Also from last night', top=26) + gut('<div>'
        + row('Priya &middot; <span style="color: #6E6862;">brought the bread</span>', mark='hollow')
        + row('The Sorrento recipe &middot; <span style="color: #6E6862;">Maya&rsquo;s version won</span>', mark='hollow', last=True) + '</div>')
    return webframe(inner)

# ───────── 4 · Setting up a surprise (E8 frame 1) ─────────
def a_setup():
    inner = bar('CHAT', 'MONDAY 9:05 PM')
    inner += gut(bubble('surprise dinner for priya&rsquo;s bday. sat the 14th, 7, mine. she can&rsquo;t know'), top=22)
    inner += gut(says('Got it. Surprise for Priya. Maya and Dana are in.'), top=16)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px; color: {GOLDD};">SURPRISE</div>'
        + f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 26px;">Priya&rsquo;s birthday. Saturday at 7:00, your place.</div>'
        + '<div class="led" style="margin-top: 12px; grid-template-columns: 124px minmax(0,1fr);">'
          '<div class="k">IN ON IT</div><div>You, Maya, Dana</div>'
          '<div class="k">OPENS TO PRIYA</div><div>When she walks in</div></div>'), top=14)
    inner += gut(says('One open thing: who gets her there for seven?', 16, 23), top=16)
    inner += gut(actions(door('Ask Maya'), door('Ask Dana')), top=4)
    return phone2(inner, active='Chat')

# ───────── 5 · One suggestion to a group (E2 frame 2) ─────────
def a_room():
    def who(name, state=''):
        if state:
            return row(f'{name} &middot; <span style="color: #6E6862;">{state}</span>', mark='dot', color=GREEN)
        return row(name, mark='hollow', color=MUTE)
    inner = header('October upstate', 'Nora, Maya, Priya, Dana', back=True)
    inner += gut(box(says('I&rsquo;d take the house in Kingston, two nights. It&rsquo;s a ten-minute walk to town and everyone gets a real bed.', 18, 26)
        + f'<div style="margin-top: 12px;">' + dci('FactPair', 92, tone='plain', a='CHECKED', av='Three houses, the walk to town, the beds', an='LISTINGS · NOT CHECKED TODAY',
                                                     b='THE TRAIN', bv='Friday 5:40, back Sunday 4:15', bn='TIMETABLE · FIXTURE') + '</div>'
        + f'<div style="margin-top: 12px;">{actions(btn("I’m in"), btn("Not this one", False))}</div>'), top=18)
    inner += sect('So far') + gut('<div>' + who('Maya', 'in') + who('Dana', 'in') + who('Priya') + who('Nora') + '</div>')
    inner += gut(f'<div style="font-size: 15px; line-height: 21px; color: {INK};">Nora decides Thursday evening.</div>', top=14)
    return phone2(inner, active='Home')

# ───────── 6 · Nobody took up the opening (D7 frame 3) ─────────
def a_alone():
    inner = anchor_row('RED HOOK', 'SUNDAY 4:50 PM')
    inner += orientation('Golden hour at the pier in twenty minutes.', 'West-facing. The light comes straight down the harbor.')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 150, tag="THE PIER &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut('<div>'
        + row('The pier &middot; <span style="color: #6E6862;">four minutes from you</span>', mark='dot', color=GOLDD)
        + row('Ferry back &middot; <span style="color: #6E6862;">every 30 minutes until 7</span>', mark='dot', color=GOLDD, last=True) + '</div>'
        + prov('SUNSET 5:12 &middot; FERRY TIMES LISTED, NOT CHECKED TODAY'), top=12)
    inner += gut(f'<div style="font-size: 14px; line-height: 20px; color: {MUTE};">&ldquo;Happy for company&rdquo; wraps up at five.</div>', top=16)
    return phone2(inner, active='Home')

VOICES = [
    ['<b>A person speaking</b>', 'The author', 'As typed. Sans, not Vesper&rsquo;s serif. Different for each person. Never tidied.', '&ldquo;it sank 😭 still ate half of it&rdquo;'],
    ['<b>A person acting</b>', 'You, first person', 'What you would say out loud. Verb first.', '&ldquo;I&rsquo;m in&rdquo; &middot; &ldquo;Not this one&rdquo; &middot; &ldquo;Remember Maya&rdquo;'],
    ['<b>Vesper stating</b>', 'Vesper', 'The state, with a name, a time, a number or a place in it. Then the one open thing.', '&ldquo;Golden hour at the pier in twenty minutes.&rdquo;'],
    ['<b>Vesper advising</b>', 'Vesper', '&ldquo;I&rsquo;d ___. It ___.&rdquo; An opinion, then the consequence in your terms.', '&ldquo;I&rsquo;d take this one. It&rsquo;s ten minutes on foot to town, which the other two aren&rsquo;t.&rdquo;'],
]
CAST = [
    ['<b>Maya</b>', 'Dry. Lowercase, no full stops, one emoji at most.', 'it sank 😭 still ate half of it'],
    ['<b>Priya</b>', 'Brief and practical. Answers the question that was asked.', 'botanic garden cafe. chairs with backs'],
    ['<b>Sam</b>', 'Earnest. Full sentences, the occasional exclamation mark. Newest to the group.', 'Found a cinema on Court Street that shows one film a week. I think I love it here!'],
    ['<b>Nora</b>', 'Fast and lowercase when she is typing to Vesper; warmer and fuller when she writes to a guest.', 'surprise dinner for priya&rsquo;s bday. sat the 14th, 7, mine. she can&rsquo;t know'],
    ['<b>Dana</b>', 'Photographs first. Captions of two or three words.', 'sorrento. again.'],
    ['<b>Nora&rsquo;s mother</b>', 'Complete sentences, careful punctuation, signs off.', 'The corner shop was a bakery when we lived on Sackett Street. Look up. Love, Mom'],
]


# ═════════════════════ V2 · pushed further ═════════════════════
V1T = tag('V1 &middot; FIRST REWRITE', GOLDD, 'rgba(176,133,58,0.14)')
V2T = tag('V2 &middot; PUSHED FURTHER', GREEN, 'rgba(61,112,80,0.14)')
def original(h, **kw):
    """A person's own words in the shared reader: name and time once, side by side, then the words. The house treatment."""
    return dci('OriginalReader', h, density='open', **kw)

def b_home():
    inner = anchor_row('NEW YORK', 'FRIDAY 8:10 AM')
    inner += orientation('Clear until four.', 'Friday &middot; 61&deg; &middot; your next thing is Tuesday at 9:00.')
    inner += sect('From friends') + gut(
        f'<div style="border-radius: 14px; overflow: hidden; margin-bottom: 14px;">{plate("room", 170, tag="PHOTO &middot; MAYA")}</div>'
        + original(100, author='Maya', meta='LAST NIGHT · TO FRIENDS', words='it sank 😭 still ate half of it', door='Reply'))
    inner += gut(f'<div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: 18px;">'
        + original(200, author='Sam', meta='WEDNESDAY · TO FRIENDS', words='Found a cinema on Court Street that shows one film a week. They sell exactly one kind of cake. I think I love it here!',
                   place='The Lantern', placeMeta='TONIGHT 7:15 · 9 MIN AWAY · LISTING THU') + '</div>', top=18)
    inner += gut(f'<div style="border-top: 1px solid rgba(27,23,20,0.08); padding-top: 18px;">'
        + original(90, author='Priya', meta='7:52 AM · TO FRIENDS', words='bread’s out of the oven if anyone’s near', door='Reply') + '</div>', top=18)
    return phone2(inner, active='Home')

def b_quiet():
    inner = anchor_row('NEW YORK', 'SUNDAY 9:40 AM')
    inner += orientation('Clear until four.', 'Sunday &middot; 58&deg; &middot; the greenmarket is at its quietest before 10:00.')
    inner += sect('Near you this morning') + gut('<div>'
        + row('The greenmarket &middot; <span style="color: #6E6862;">until 2:00</span>', mark='dot', color=GOLDD)
        + row('The canal walk &middot; <span style="color: #6E6862;">twenty minutes, flat</span>', mark='dot', color=GOLDD, last=True) + '</div>'
        + prov('MARKET LISTING &middot; SAT'))
    inner += sect('From friends this week') + gut('<div>'
        + row('Maya&rsquo;s cake &middot; <span style="color: #6E6862;">Thursday</span>', mark='hollow')
        + row('Sam at The Lantern &middot; <span style="color: #6E6862;">Wednesday</span>', mark='hollow', last=True) + '</div>')
    return phone2(inner, active='Home')

def b_after():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div style="display: flex; align-items: center; gap: 8px;"><span class="fn" style="color: {MUTE};">SUNDAY</span>{chip("JUST YOU")}</div></div>'
    inner += gut(f'<div style="{SERIF} font-weight: 600; font-size: 23px; line-height: 29px;">Nora&rsquo;s dinner, last night.</div>', top=10)
    inner += gut(box(person('M', 'Maya', 'from Nora&rsquo;s dinner &middot; the lemon argument')
        + f'<div style="margin-top: 14px; display: flex; flex-direction: column; gap: 16px;">'
        + f'<div>{actions(btn("Remember Maya"))}<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">You&rsquo;ll find her as &ldquo;Maya, from Nora&rsquo;s dinner.&rdquo;</div></div>'
        + f'<div>{actions(btn("Swap numbers", False))}<div style="font-size: 14px; line-height: 20px; color: {INK2}; margin-top: 8px;">She gets asked too. Two yeses, and you each have the other&rsquo;s.</div></div></div>'), top=16)
    inner += sect('Also from last night', top=26) + gut('<div>'
        + row('Priya &middot; <span style="color: #6E6862;">brought the bread</span>', mark='hollow')
        + row('The Sorrento recipe &middot; <span style="color: #6E6862;">Maya&rsquo;s version won</span>', mark='hollow', last=True) + '</div>')
    return webframe(inner)

def b_setup():
    inner = bar('CHAT', 'MONDAY 9:05 PM')
    inner += gut(bubble('surprise dinner for priya&rsquo;s bday. sat the 14th, 7, mine. she can&rsquo;t know'), top=22)
    inner += gut(says('A surprise for Priya, then. Maya and Dana are in.'), top=16)
    inner += gut(box(f'<div class="kickm" style="margin-bottom: 6px; color: {GOLDD};">SURPRISE</div>'
        + f'<div style="{SERIF} font-weight: 600; font-size: 20px; line-height: 26px;">Priya&rsquo;s birthday</div>'
        + f'<div style="font-size: 15px; line-height: 21px; color: {INK2}; margin-top: 2px;">Saturday the 14th, 7:00, your place</div>'
        + f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 14px;">{facepile(["N", "M", "D"], 26)}<span style="font-size: 14px; color: {INK2};">are in on it</span></div>'
        + f'<div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 10px;">Opens to Priya when she walks in.</div>'), top=14)
    inner += gut(says('Who&rsquo;s getting her there for 7:00?', 17, 24), top=18)
    inner += gut(actions(door('Ask Maya'), door('Ask Dana')), top=2)
    return phone2(inner, active='Chat')

def b_room():
    inner = header('October upstate', 'Nora, Maya, Priya, Dana', back=True)
    inner += gut(box(f'<div style="{SERIF} font-weight: 600; font-size: 21px; line-height: 27px;">The blue house on Wiltwyck</div>'
        + f'<div style="font-size: 14px; line-height: 20px; color: {MUTE}; margin-top: 2px;">Kingston &middot; two nights &middot; sleeps four in beds</div>'
        + f'<div style="margin-top: 12px;">{says("I&rsquo;d take this one. It&rsquo;s ten minutes on foot to town, which the other two aren&rsquo;t, and nobody ends up on a sofa.", 16, 23)}</div>'
        + f'<div style="margin-top: 12px;">' + dci('FactPair', 92, tone='plain', a='LOOKED AT', av='Three houses, side by side', an='LISTINGS · TUE',
                                                     b='THE TRAIN', bv='Fri 5:40 out, Sun 4:15 back', bn='TIMETABLE · TUE') + '</div>'
        + f'<div style="display: flex; align-items: center; gap: 10px; margin-top: 14px;">{facepile(["M", "D"], 26)}<span style="font-size: 14px; color: {INK2};">Maya and Dana are in</span></div>'
        + f'<div style="margin-top: 14px;">{actions(btn("I’m in"), btn("Not this one", False))}</div>'), top=18)
    inner += gut(f'<div style="font-size: 15px; line-height: 21px; color: {INK};">Nora decides Thursday evening.</div>', top=16)
    return phone2(inner, active='Home')

def b_alone():
    inner = anchor_row('RED HOOK', 'SUNDAY 4:50 PM')
    inner += orientation('Golden hour at the pier in twenty minutes.', 'It faces west, so the light comes straight down the harbor. The far benches keep it longest.')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("pier", 170, tag="THE PIER &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut('<div>'
        + row('The pier &middot; <span style="color: #6E6862;">four minutes from you</span>', mark='dot', color=GOLDD)
        + row('Ferry back &middot; <span style="color: #6E6862;">on the :10 and :40 until 7:10</span>', mark='dot', color=GOLDD, last=True) + '</div>'
        + prov('SUNSET 5:12 &middot; FERRY TIMETABLE, SUN'), top=12)
    return phone2(inner, active='Home')

def triple(n, title, before, v1, v2, pushed):
    def c(tagx, ph, sub):
        return col(ph, f'<div style="display: flex; gap: 6px; margin-bottom: 7px;">{tagx}</div>' + caption(n, title, sub))
    note = (f'<div style="width: 470px; flex: none; padding-top: 86px;"><div class="shead" style="margin-bottom: 10px;"><span>V1 &rarr; V2</span><span class="rule"></span></div>'
            + ''.join(f'<div style="display: flex; gap: 10px; align-items: baseline; margin-bottom: 9px;"><span style="color: {GHOST}; flex: none;">&mdash;</span><span style="font-size: 13px; line-height: 19px; color: {INK2};">{t}</span></div>' for t in pushed) + '</div>')
    return (f'<div style="display: flex; gap: 46px; align-items: flex-start; border-top: 1px solid rgba(27,23,20,0.12); padding-top: 26px;">'
            + c(BEF, before, 'As it stands on its board.') + c(V1T, v1, 'The rewrite you saw.') + c(V2T, v2, 'The same rules, pushed.') + note + '</div>')

PUSH = [
    ['<b>Vesper does not summarize people.</b>', 'V1&rsquo;s headline &mdash; &ldquo;Maya&rsquo;s cake sank&rdquo; &mdash; retold her joke in Vesper&rsquo;s voice before she got to tell it. In V2 the headline is about the day, which is Vesper&rsquo;s to say, and the friends speak for themselves.'],
    ['<b>People&rsquo;s words go in the shared reader.</b>', 'V1 set messages in sans with a mono stamp underneath, which made friends look processed. The selected design already has a treatment for a person&rsquo;s own words: name and time once, side by side, then the words. V2 uses that component as it is.'],
    ['<b>Provenance says what it is and when.</b>', '&ldquo;LISTING &middot; THU&rdquo;, not &ldquo;NOT CHECKED TODAY&rdquo;. V1 also had a box headed CHECKED with &ldquo;not checked today&rdquo; under it.'],
    ['<b>Things have names.</b>', 'The Lantern. The blue house on Wiltwyck. The canon&rsquo;s own good lines are full of proper nouns (&ldquo;the 7:30 at Taberna&rdquo;); vague nouns were a large part of why mine read like a template. All fixtures.'],
    ['<b>The rhythm varies.</b>', 'V1 swapped one tic for another: two short beats, everywhere. &ldquo;Got it. Surprise for Priya.&rdquo; &ldquo;I&rsquo;d walk. The bus takes longer.&rdquo; V2 lets a sentence run when it has a reason to.'],
    ['<b>Fewer words; let the object carry it.</b>', 'Faces on the option instead of a list of who said yes. Filler removed: the dentist line, &ldquo;open until Tuesday&rsquo;s dentist&rdquo;, the line about the opening wrapping up.'],
]

def build():
    inner = blk('WHAT V2 PUSHES FURTHER', tbl(['', 'WHY'], PUSH))
    inner += triple('1', 'Home, with friends', gen_d1.home(), a_home(), b_home(),
        ['Headline is the day. Vesper no longer retells Maya&rsquo;s joke above Maya.', 'Each friend is one shared-reader unit: name, time, words. No section per person, no stamp under the message.', 'Vesper&rsquo;s one line about Sam&rsquo;s cinema moved into the reader&rsquo;s own place row, and gained a name and tonight&rsquo;s showing.', 'The dentist section is gone; it was filler under the wrong heading.'])
    inner += triple('2', 'A Sunday with nothing new', gen_d1.quiet(), a_quiet(), b_quiet(),
        ['&ldquo;Open until Tuesday&rsquo;s dentist&rdquo; failed the read-aloud test. Replaced with something true about this morning.', 'Provenance names its source and day.'])
    inner += triple('3', 'The morning after a dinner', gen_e1.after(), a_after(), b_after(),
        ['&ldquo;Save Maya&rdquo; &rarr; &ldquo;Remember Maya&rdquo;. You save files; you remember people.', '&ldquo;Swap details&rdquo; &rarr; &ldquo;Swap numbers&rdquo;, and the consent step is said plainly: she gets asked too.'])
    inner += triple('4', 'Setting up a surprise', gen_e8.setup(), a_setup(), b_setup(),
        ['Faces instead of an &ldquo;IN ON IT&rdquo; label and a list.', 'Title, then the practical line beneath it, the way a calendar entry reads.', '&ldquo;Got it.&rdquo; removed &mdash; an assistant&rsquo;s reflex, not a voice.'])
    inner += triple('5', 'One suggestion to a group', gen_e2.room(), a_room(), b_room(),
        ['The house has a name and one line of facts, so the advice can be about <i>why</i>.', 'The reason now compares: ten minutes on foot, &ldquo;which the other two aren&rsquo;t.&rdquo; That is what makes it advice and not description.', 'Yeses shown as faces on the option.', 'CHECKED / &ldquo;not checked today&rdquo; contradiction fixed.'])
    inner += triple('6', 'Nobody took up the opening', gen_d7.alone(), a_alone(), b_alone(),
        ['One more true thing about the light, which is the only subject this screen has.', 'The &ldquo;wraps up at five&rdquo; line removed. It expires without comment.', 'Ferry times written the way a timetable is spoken.'])
    inner += blk('FOUR VOICES, KEPT APART', tbl(['VOICE', 'WHOSE', 'GRAMMAR', 'EXAMPLE'], VOICES))
    inner += blk('A CAST SHEET, SO SIX PEOPLE STOP SOUNDING LIKE ONE', tbl(['', 'HOW THEY WRITE', 'A LINE OF THEIRS'], CAST))
    return write('C1 - Copy before and after', sheetboard(
        3 * 393 + 3 * 46 + 470 + 64, hh('C1', 7000),
        'C1 &middot; COPY &middot; A PROPOSAL, FOR YOUR EAR &middot; SECOND ROUND',
        'Copy: before, first rewrite, pushed further',
        'Six frames from the live boards, the rewrite you saw, and a second rewrite that pushes the same rules harder. '
        'Nothing else on the project has been changed. Names of places are fixtures invented for these frames.',
        inner, vdl=True))

if __name__ == '__main__':
    print(build())
