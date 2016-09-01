import sys
import textwrap
"""
needs to:
	display WELCOME_SCREEN
		options: "1" play or "0" quit //or look at high scores
	present option for Loading saved files
"""
WELCOME_SCREEN = (
"""You raise your head from the bar-top; the world is swimming. How much have 
you had to drink? Looking about, you see no one in the bar. Your memory is 
foggy; you've got to get home...but, alas, there are 3 blocks between you
and that sweet heavenly abode! 
You pull yourself to your feet and nearly vomit. You are, however, no mere mortal who can be disuaded their comfy bed 
by a little alcohol poisoning. Making your way out into the sick, street 
light, you hear the dumb sounds of bros chattering and the Orwellian song of 
police sirens on the whispering wind. Time is short, dear adventurer of the 
night-stalking wonder! Make haste!""")


class Stage(object):
#calls monster()
	pass

class NewPlayer(object):
	
	def __init__(self, player_points=0):
		pass

def monster():
#cops & bros
	pass

def game():
	print(textwrap.fill(WELCOME_SCREEN, width=50))

