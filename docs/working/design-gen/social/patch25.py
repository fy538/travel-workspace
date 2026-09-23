"""02.2's recipient choice redrawn in the workbench's own S1 sheet anatomy (02B, 'Who gets it'), so it follows the
shared proposal instead of competing with it. Still proposed there; still proposed here."""
import re
s = open('gen_c2.py').read()
i = s.index('def recipient_inset():'); j = s.index('\ndef reply_result_inset():', i)
NEW = '''def recipient_inset():
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
'''
s = s[:i] + NEW + s[j:]
open('gen_c2.py', 'w').write(s)
print('recipient inset now follows the S1 sheet')
