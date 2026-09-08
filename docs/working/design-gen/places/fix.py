"""Shared fixture copy and the units that several boards draw (the field, the Red Hook pocket, the hour, the film)."""
from kit3 import *
import gen19v3 as g
UNK_ROOM = 'Whether the exhibition is ticketed hasn&rsquo;t been confirmed.'; UNK_HOUR = 'Seats left for this Saturday haven&rsquo;t been confirmed.'
MAYA_ROOM = 'The side room was my favorite. Go on a weekday, it was empty.'; MAYA_PIER = 'Tuesday, seven.'
PRIYA_PIGEONS = 'The pigeons at the market have a system. I have watched it for twenty minutes.'; THEO_BREAD = 'The bread stall sells out by ten; go early or don&rsquo;t bother.'; SAM_HALL = 'Sit on the left side, that&rsquo;s where the speakers are.'
def field(populated=True): return g.v3(populated)
def field_with(extra_after_fact):
    h = field(True); k = 'MAYA, TUESDAY · &ldquo;TUESDAY, SEVEN.&rdquo;</div>'; assert k in h
    return h.replace(k, k + extra_after_fact, 1)
def map_block(): return REDHOOK_MAP
def redhook_rows(populated=True, opened=False, facts=True):
    return ('<div>' + nrow(1, 'The Harbor Print Room', 'TUE–SUN 11–6 · ROOMS REMADE, TO SUNDAY', (unc(UNK_ROOM) if facts else '') + (fn('MAYA WAS THERE THURSDAY', 4) if populated and facts else '') + (f'<div class="fn" style="margin-top: 4px; color: {GOLDD};">OPENED JUST NOW</div>' if opened else ''), first=True)
            + nrow(2, 'The Red Hook pier', 'FACES THE HARBOR AND THE STATUE') + nrow(3, 'The Red Hook pool', 'LAP SWIM 7–8:30 AM · BRING A LOCK') + nrow(4, 'The lunch counter on Columbia Street', 'TILL 4 · $11 PLATE · STANDING ROOM', last=True) + '</div>')
def getting_in(): return '<div>' + prow('The ferry from Pier 11', 'EVERY 40 MINUTES · 25 MINUTES ACROSS · 9 MIN ON FOOT TO THE PRINT ROOM', first=True) + prow('The B61 bus', 'EVERY 12 MINUTES · TWO BLOCKS FROM THE PRINT ROOM', last=True) + '</div>'
def hour_unit(extra=''):
    return (title('The listening hour at Canal Hall', 17, 22) + sup('Reich, Music for 18 Musicians, heard whole. Lights down, no talking; doors 6:45.') + unc(UNK_HOUR) + fn('SATURDAY 7:15 PM · $12 · CANAL STREET', 8) + extra)
def film_row(last=True, first=True): return prow('Playtime on the lawn by the pier', '8:30 · FREE · SUNSET PARK, FORTY MINUTES FROM CANAL STREET', first=first, last=last)
def photo_plate(h=200, label='PHOTO · TO BE SOURCED'): return f'<div style="height: {h}px; border-radius: 12px; position: relative; background: {HATCH};"><span style="position: absolute; left: 10px; top: 9px; {MONO} font-size: 10px; font-weight: 700; letter-spacing: 0.9px; color: {GOLDD};">{label}</span></div>'
def share_row(letter, who, when, words, place, last=False):
    return f'<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 0;{" border-bottom: 1px solid " + HAIR7 + ";" if last else ""} border-top: 1px solid {HAIR7};">{facepile([letter])}<div style="flex: 1; min-width: 0;"><div style="display: flex; gap: 8px; align-items: baseline;"><span style="font-size: 13px; font-weight: 600; color: {INK};">{who}</span><span class="fn" style="color: {ANCHOR};">{when}</span></div><div style="{SERIF} font-size: 15px; line-height: 21px; color: {INK}; margin-top: 3px;">&ldquo;{words}&rdquo;</div>{fn(place, 3)}</div>{CHEV}</div>'
