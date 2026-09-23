"""Replace the phone functions of a board generator (everything from the first numbered section comment to build()),
switch it onto mp_kit2, and record the decisions that moved off the screen."""
import re, sys
def apply(fname, new_funcs, offscreen, first_marker='\n# ── 1'):
    s = open(fname).read()
    s = s.replace('from mp_common import *', 'from mp_kit2 import *', 1)
    i = s.index(first_marker); j = s.index('\ndef build():')
    s = s[:i] + '\n' + new_funcs.strip('\n') + '\n' + s[j:]
    note = "<b>Decided, not displayed:</b> " + ' &middot; '.join(offscreen) + '.'
    if 'offscreen=' in s or 'Decided, not displayed' in s:
        pass
    elif 'nc = review(' in s:
        k = s.rindex("extras=("); s = s[:k] + f"offscreen={offscreen!r},\n        " + s[k:]
    else:
        k = s.rindex(', w=440)'); s = s[:k] + f"\n        + N({note!r})" + s[k:]
    open(fname, 'w').write(s)
