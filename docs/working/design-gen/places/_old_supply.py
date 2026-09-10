def shared_supply():
    """The place-relative view of Home 14's bounded supply set: the same supported locality (New York), the same time (Saturday 9:30, Home 14.3) and the same source set.
    Items: the flea (its own notice, Saturdays through October); Open House New York (Oct 17–18; timed-site registration closed Thursday; walk-in sites need none); the L notice (MTA; single-tracking after 11 PM Mon–Thu);
    the forecast (two stations); the tide table; one chapter of The Harbor Book. No friends, no history, no chosen places."""
    body = anchor('NEW YORK', 'SATURDAY 9:30 AM') + orientation('The flea, under the bridge, until three.', 'Clear, 41&deg; · Saturdays through October · nothing else has changed since Thursday') + ask()
    body += gut('<div>' + prow('The flea, under the bridge', 'FROM 8 UNTIL 3 · THE BREAD STALL SELLS OUT BY TEN · THE MARKET&rsquo;S OWN NOTICE', first=True, last=True) + '</div>' + door('Directions'), top=24)
    body += sect('Open House, October 17 and 18') + gut('<div>' + prow('The walk-in sites', 'NO REGISTRATION NEEDED · OCT 17–18', first=True) + prow('The timed sites', 'REGISTRATION CLOSED THURSDAY', last=True) + '</div>')
    body += sect('Getting around') + gut(hours_register([('THE L', 'Normal today; single-tracking after 11 PM, Monday to Thursday'), ('THE TIDE', 'Low water 2:40 to 5; high 8:40')]))
    body += sect('Worth understanding') + gut(g.FLOOD(118) + fn('THE HARBOR BOOK · CH. 4 · 4 MIN', 12) + f'<div style="margin-top: 4px;">{serifline("The pumps under the park finish what the gates cannot", 17, 22)}</div>' + sup('The two iron squares at the crossing are the pump intakes: on a rising tide the water inside the gates has nowhere else to go.') + door('Read the chapter'))
    body += gut(door_list(['Another neighborhood']), top=24)
    return phone(body)
def unavailable_information():
