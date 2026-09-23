"""06 · Something that continues (package C). Three friends and a fourth in Sorrento try to get one dish right over two
weeks. What each of them sent becomes a usable version, with disagreements left in. Someone benefits without contributing.
Three weeks later it is used again, and one person chooses to say thanks."""
from mp_kit2 import *
from gen_merge import daycap
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
APP = tag('NO APP', OX, 'rgba(122,46,46,0.10)')

def thread():
    inner = header('The Sorrento pasta', 'You, Maya, Priya, Dana &middot; two weeks', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden; margin-bottom: 12px;">{plate("room", 120, tag="PHOTO &middot; YOURS &middot; THU")}</div>'
        + original(80, author='You', initial='N', meta='THU SEPT 24 · TO THE FOUR OF YOU', words='attempt one. it split. why'), top=16)
    inner += gut(rule(original(96, author='Priya', meta='SUN SEPT 27', words='did the cheese off the heat, a handful at a time. it held. also half the pepper'), 14), top=14)
    inner += gut(rule(original(80, author='Maya', meta='SUN SEPT 27', words='half the pepper is a crime. full pepper or it&rsquo;s a different dish'), 14), top=14)
    inner += gut(rule(original(96, author='Dana', meta='SAT OCT 3 · FROM SORRENTO', words='zest goes in at the very end, off the heat. the woman at the place here was very clear about this'), 14), top=14)
    return phone2(inner, active='Life')

def version():
    inner = bar('CHAT', 'THURSDAY OCT 8')
    inner += gut(bubble('ok what&rsquo;s the version that actually held together'), top=22)
    inner += gut(box(f'<div style="{SERIF} font-weight: 600; font-size: 19px; line-height: 25px;">The version that held</div>'
        + '<div class="led" style="margin-top: 12px; grid-template-columns: 22px minmax(0,1fr); row-gap: 10px;">'
          f'<div class="k">1</div><div>Pan off the heat before any cheese goes in. <span style="color: {MUTE};">Priya</span></div>'
          f'<div class="k">2</div><div>Cheese in handfuls, stirring between each. <span style="color: {MUTE};">Priya</span></div>'
          f'<div class="k">3</div><div>Zest at the very end, still off the heat. <span style="color: {MUTE};">Dana, from Sorrento</span></div>'
          f'<div class="k">?</div><div>Pepper: Priya halves it. Maya says full, or it&rsquo;s a different dish. <span style="color: {MUTE};">Not settled</span></div></div>'
        + f'<div style="margin-top: 12px;">{actions(door("See what each of them sent"))}</div>'), top=16)
    inner += gut(plain('Your first attempt had the cheese going in over the flame. That&rsquo;s the step all three changes are about.', INK2, 14, 20), top=12)
    return phone2(inner, active='Chat')

def inset_removed():
    def mini_list(title, rows, note):
        return (f'<div style="flex: 1; background: {CARD}; border: 1px solid {HAIR}; border-radius: 10px; padding: 12px 14px;"><div class="kickm" style="margin-bottom: 8px;">{title}</div>'
                + ''.join(f'<div style="font-size: 13px; line-height: 19px; color: {INK2}; padding: 3px 0;">{r}</div>' for r in rows)
                + f'<div class="fn" style="color: {ANCHOR}; margin-top: 8px; line-height: 15px;">{note}</div></div>')
    body = (N('The test from the brief: take one person&rsquo;s contribution away and see whether the result changes.')
            + f'<div style="display: flex; gap: 10px;">'
            + mini_list('WITH ALL THREE', ['1 · Off the heat', '2 · Cheese in handfuls', '3 · Zest at the end', '? · Pepper, unsettled'], 'FOUR LINES, ONE OPEN QUESTION')
            + mini_list('WITHOUT DANA', ['1 · Off the heat', '2 · Cheese in handfuls', '? · Pepper, unsettled'], 'THE LEMON STEP IS GONE')
            + mini_list('WITHOUT MAYA', ['1 · Off the heat', '2 · Cheese in handfuls', '3 · Zest at the end', '4 · Half the pepper'], 'READS AS SETTLED; IT IS NOT') + '</div>'
            + N('Each removal changes what Nora would cook. If it did not, this would be generated content with names attached.'))
    return f'<div style="margin-top: 14px; width: 832px; box-sizing: border-box; border: 1px dashed rgba(27,23,20,0.28); border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px;"><div class="kickm">2 &middot; THE SAME ANSWER WITH ONE PERSON TAKEN OUT</div>{body}</div>'

def sam_gets():
    inner = f'<div style="padding: 20px 22px 0 22px;"><div class="fn" style="color: {MUTE};">FROM NORA</div></div>'
    inner += gut(original(80, author='Nora', meta='FRI OCT 9 · TO YOU', words='the pasta from last week, the way that finally worked'), top=14)
    inner += gut(box('<div class="led" style="grid-template-columns: 22px minmax(0,1fr); row-gap: 10px;">'
          '<div class="k">1</div><div>Pan off the heat before any cheese goes in.</div>'
          '<div class="k">2</div><div>Cheese in handfuls, stirring between each.</div>'
          '<div class="k">3</div><div>Zest at the very end, still off the heat.</div></div>'), top=14)
    inner += gut(actions(btn('Save'), door('Reply to Nora', MUTE)), top=16)
    return webframe(inner)

def again():
    inner = anchor_row('NEW YORK', 'THURSDAY OCT 29')
    inner += orientation('Pasta again Saturday.', 'The version that held, and one open argument.')
    inner += gut(box('<div class="led" style="grid-template-columns: 22px minmax(0,1fr); row-gap: 8px;">'
          f'<div class="k">1</div><div>Off the heat <span style="color: {MUTE};">Priya</span></div><div class="k">2</div><div>Cheese in handfuls <span style="color: {MUTE};">Priya</span></div>'
          f'<div class="k">3</div><div>Zest at the end <span style="color: {MUTE};">Dana</span></div></div>'), top=16)
    inner += gut(rule(original(80, author='Maya', meta='TODAY · TO THE FOUR OF YOU', words='bringing a whole pepper mill saturday. to prove a point'), 14), top=14)
    return phone2(inner, active='Home')

def thanks():
    inner = bar('TO DANA', 'SUNDAY NOV 1')
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 170, tag="PHOTO &middot; YOURS")}</div>', top=18)
    inner += gut(f'<div style="border-bottom: 1px solid rgba(27,23,20,0.14); padding: 10px 0;">{plain("zest at the end. you were right. it&rsquo;s a different dish", size=17, lh=24)}</div>', top=14)
    inner += gut(f'<div style="display: grid; grid-template-columns: 22px 1fr; column-gap: 10px; align-items: baseline;"><span style="color: {GHOST};">&ldquo;</span>{plain("About: her message from Sorrento, Oct 3", MUTE, 13, 18)}</div>', top=14)
    inner += gut(f'<div style="display: flex; align-items: center; gap: 10px;">{chip("TO DANA")}</div>', top=12)
    inner += gut(actions(btn('Send'), door('Not now', MUTE)), top=14)
    return phone2(inner, active='Life')

def cell(day, n, title, sub, ph, tags=(), w=393):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub), w=w)

def build():
    r1 = [cell('TWO WEEKS', '1', 'What each of them sent', 'Four people, four messages, one photo. Every piece arrived because its author sent it to these four. Nobody kept a log, and Maya and Priya disagree.', thread(), (P('LIFE'), P('D2, THREE CONTRIBUTORS'))),
          cell('OCT 8', '2', 'On request: the version that held', 'A method Nora can cook from, each step carrying whose it is, and the pepper argument left open.', version() + inset_removed(), (P('CHAT'),), w=832)]
    r2 = [cell('OCT 9', '3', 'Sam gets it, having sent nothing', 'Nora passes on the method in her own message. The others&rsquo; words and names do not travel; they were sent to four people, not to Sam.', sam_gets(), (APP, P('A LINK'))),
          cell('OCT 29', '4', 'Three weeks later', 'Used again. The steps are the same; Maya has reopened the pepper question herself.', again(), (P('HOME'),)),
          cell('NOV 1', '5', '&ldquo;You were right&rdquo;', 'Nora chooses to tell Dana. Nothing prompted it, and Dana would have been told nothing otherwise.', thanks(), (P('LIFE'),))]
    rows = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(r1) + '</div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 8px;">' + ''.join(r2) + '</div>')
    n1 = notes('FOR EACH PERSON', tbl(['', 'RECEIVES', 'WORK THAT DISAPPEARS', 'STAYS THEIRS', 'BARELY USING IT?'], [
        ['<b>Nora</b>', 'A method she can cook from, with its open question', 'Scrolling two weeks of thread; reconciling three people&rsquo;s changes', 'Cooking it; asking; thanking Dana', 'No'],
        ['<b>Priya, Maya</b>', 'Their change, or their objection, still theirs in the result', 'None', 'Trying it; arguing about pepper', 'Yes: one message each'],
        ['<b>Dana</b>, in Sorrento', 'Later, a photo and &ldquo;you were right,&rdquo; if Nora feels like it', 'None', 'One message, because she wanted to', 'Yes. She never meets anyone'],
        ['<b>Sam</b>', 'The method', 'Everything', 'Nothing', 'Yes: one link. Conditional on the guest path'],
    ]), w=900)
    n2 = notes('TWO VALUE TESTS, AND THE ORDINARY ALTERNATIVE', led([
        ('WORTH IT WITHOUT VESPER?', 'Yes. Frame 1 is four friends being funny about pasta, and it would be fine as a group chat forever.'),
        ('DID VESPER ADD ENOUGH?', 'In frame 2 only: it assembled one usable method from four messages over two weeks, kept each step&rsquo;s author, and refused to settle the pepper. The inset shows the result changes when a person is removed. Frames 1, 3 and 5 need nothing from it.'),
        ('A SHARED NOTE', 'A shared note does this if someone maintains it. Nobody here did, and the claim is only that nobody had to.'),
        ('SOURCE ACTS', 'Every line traces to a sent message or a photo. Nothing spoken in a kitchen appears. Using the four messages for a synthesis assumes they were shared with that use allowed; being able to read a message is not that permission.'),
        ('NOT CLAIMED', 'That people want an ongoing shared undertaking, that a fourth contributor abroad is common, or that any of this is enjoyable. One worked example; no project object, no dashboard, no quota.'),
    ]), w=700)
    body = rows + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(0, (900, 700))}px; min-height: {hh("06", 3200)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('06 &middot; PACKAGE C &middot; COMPOSITION', 'Something that continues',
                   'Four friends, one of them in Sorrento, try to get a dish right over two weeks. What they each sent becomes a version someone can cook from, with the disagreement left in. '
                   'One person benefits without contributing, it is used again three weeks later, and one person chooses to say thanks. This is also D2&rsquo;s missing three-contributor case. The separate far-apart story on board 04 stands as it was.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('06 - Something that continues', html)

if __name__ == '__main__':
    print(build())
