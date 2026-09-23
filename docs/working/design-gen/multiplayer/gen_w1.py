"""03 · An ordinary week between friends (package D, composition 1). The same objects across the four roots, placed where
the accepted split puts them: casual non-spatial shares on Home, a friend's place in Places, addressed things on Home."""
from mp_kit2 import *
import gen_d1, gen_d7
from gen_merge import daycap
P = lambda t: tag(t, PLAN, 'rgba(42,56,75,0.10)')
END = tag('ENDS HERE', GREEN, 'rgba(61,112,80,0.12)')

def places_note():
    inner = header('Court Street', 'Carroll Gardens &middot; from friends', back=True)
    inner += gut(f'<div style="border-radius: 14px; overflow: hidden;">{plate("room", 120, tag="THE LANTERN &middot; ILLUSTRATION")}</div>', top=16)
    inner += gut(original(170, author='Sam', meta='WEDNESDAY · TO FRIENDS', words='Found a cinema on Court Street that shows one film a week. They sell exactly one kind of cake. I think I love it here!',
                          place='The Lantern', placeMeta='TONIGHT 7:15 · 9 MIN AWAY · LISTING THU'), top=14)
    inner += gut(actions(door('Ask Sam'), door('What&rsquo;s showing', MUTE)), top=6)
    inner += sect('Also on Court Street') + gut('<div>'
        + row('Tilde Coffee &middot; <span style="color: #6E6862;">open until 6:00</span>', mark='dot', color=GOLDD)
        + row('The corner shop at Sackett &middot; <span style="color: #6E6862;">open until 7:00</span>', mark='dot', color=GOLDD, last=True) + '</div>' + prov('LISTINGS &middot; THU'))
    return phone2(inner, active='Places')

def cell(day, n, title, sub, ph, tags=()):
    return col(ph, (f'<div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 7px;">{"".join(tags)}</div>' if tags else '') + daycap(day, n, title, sub))

ROOTS = [
    ['<b>Maya&rsquo;s cake</b><br>casual, no place', 'Featured doorway, the accepted non-spatial exception (frame 1)', '&mdash;', 'Reply composes here or in place; Ask is private', 'Findable later under Maya'],
    ['<b>Sam&rsquo;s cinema</b><br>casual, a place', '<b>Not copied here</b>', '<b>From friends</b>, beside The Lantern, with today&rsquo;s listing as a separate line (frame 4)', '&ldquo;Ask Sam&rdquo; is a message to Sam; &ldquo;What&rsquo;s showing&rdquo; is a private question', 'Under Sam, and under the place'],
    ['<b>Nora&rsquo;s park opening</b><br>addressed', 'On Maya&rsquo;s and Priya&rsquo;s Home, because it was sent to them; on Nora&rsquo;s when someone answers (frames 5, 6)', 'The park is a chosen place, not her position', 'Written here', 'The afternoon, once it happened'],
    ['<b>Priya&rsquo;s city</b> (E7)', 'The evening it arrives', 'Beside each place, whenever Nora opens Places there', 'Nora&rsquo;s private question about her parents', 'Findable under Priya for as long as Nora keeps it'],
    ['<b>The pasta</b> (06)', 'The Thursday before she cooks it again', '&mdash;', 'Where she asks for the version that held', 'The shared thread itself'],
]
ANSWERS = [
    ['Enjoyable or useful?', 'A friend&rsquo;s joke about a cake; a cinema nine minutes away showing something tonight; half an hour with Maya in a park.'],
    ['Work that disappeared', 'Little, and that is honest: a message thread does frames 1 to 3 as well. Frame 4 saves finding Sam&rsquo;s message again when Nora is on Court Street. Frame 6 saves nothing; it just keeps interest and agreement apart.'],
    ['Commitment understood?', 'Replying to Maya reaches Maya only. Sam&rsquo;s note asks for nothing. The park is agreed only when Nora says yes to four o&rsquo;clock.'],
    ['A little, a no, or nothing?', 'Sam answers with two emoji. Priya says &ldquo;not today&rdquo; and offers tomorrow. Nora reads Sam&rsquo;s note and never replies. All three are whole.'],
]

def build():
    r1 = [cell('FRIDAY', '1', 'A friend&rsquo;s moment', 'Non-spatial, casual, on Home. From D1.', gen_d1.home(), (P('HOME'), P('D1'))),
          cell('FRIDAY', '2', 'A small reply', 'The original stays in view. Only Maya gets it.', gen_d1.opened(), (P('HOME'), P('D1'))),
          cell('FRIDAY', '3', 'Maya gets it', 'Beside what it was about. Sam&rsquo;s reply is two emoji.', gen_d1.maya_gets(), (P('HOME'), P('D1'), END))]
    r2 = [cell('SATURDAY', '4', 'A friend&rsquo;s place, in Places', 'Nora is on Court Street and opens Places. Sam&rsquo;s note sits beside the cinema it is about. She reads it and says nothing.', places_note(), (P('PLACES'), P('NEW'), END)),
          cell('SATURDAY', '5', 'An open afternoon', 'A place she chose and a rough window. From D7.', gen_d7.express(), (P('HOME'), P('D7'))),
          cell('SATURDAY', '6', 'One shorter visit, one other idea', 'Agreed only when she says yes. From D7.', gen_d7.outcomes(), (P('HOME'), P('D7')))]
    rows = ('<div style="display: flex; gap: 46px; align-items: flex-start;">' + ''.join(r1) + '</div>'
            + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 8px;">' + ''.join(r2) + '</div>')
    n1 = notes('PACKAGE D &middot; THE SAME OBJECTS ACROSS THE FOUR ROOTS', tbl(['OBJECT', 'HOME', 'PLACES', 'CHAT', 'LIFE'], ROOTS)
        + N('This follows the accepted split in the Social brief &sect;4: Places owns casual authored places; Home carries addressed value, shared consequences and the one non-spatial Status exception; Chat is input and private preparation; Life is continuity. '
            'An earlier version of this board was a weekend that put five of eight frames on Home, including Sam&rsquo;s cinema. That was a drawing, not a proposal to change the split, and it has been corrected. No story here visits all four roots.'), w=1100)
    n2 = notes('THE FOUR QUESTIONS', tbl(['', ''], ANSWERS)
        + N('<b>Does it feel like friends&rsquo; lives or another inbox?</b> Unanswerable from a drawing. What the drawing can show is that nothing here has an unread state and the only thing that waits on Nora is a question Maya actually asked.'), w=620)
    body = rows + '<div style="display: flex; gap: 46px; align-items: flex-start; margin-top: 34px; border-top: 1px solid rgba(27,23,20,0.12);">' + n1 + n2 + '</div>'
    html = (HEAD_VDL + f'<div style="width: {bw(3, (1100, 620))}px; min-height: {hh("03", 3000)}px; background: #F4F0E7; box-sizing: border-box; padding: 30px 32px 36px 32px; {SANS} color: {INK}; display: flex; flex-direction: column;">'
            + head('03 &middot; PACKAGE D &middot; COMPOSITION', 'An ordinary week between friends',
                   'A photograph, one tiny reply, a friend&rsquo;s place note where it helps, something enjoyed without responding, and half an hour in a park. Five of the six frames already existed; the one new frame is the one the review said was missing: receiving through people in Places.')
            + body + f'<div class="fn" style="margin-top: 30px; line-height: 16px;">{FOOTX}</div></div>' + TAIL)
    return write('03 - An ordinary week between friends', html)

if __name__ == '__main__':
    print(build())
