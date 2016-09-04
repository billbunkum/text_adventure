import sys
from random import randint
from game import *

"""
a text-based choose-your-own-adventure

to clear screen:
	import os
	os.system("clear")
"""

WELCOME_SPLASH = ("""You raise your head from the bar-top; the world is swimming. How much have you had to drink? Looking about, you see no one in the bar. Your memory is foggy; you've got to get home...but, alas, there are 3 blocks between you and that sweet heavenly abode! You pull yourself to your feet and nearly vomit. You are, however, no mere mortal who can be disuaded their comfy bed by a little alcohol poisoning. Making your way out into the sick, street light, you hear the dumb sounds of bros chattering and the Orwellian song of police sirens on the whispering wind. Time is short, dear adventurer of the night-stalking wonder! Make haste!""")

ACTIONS = ( "1: fight", "2: flight", "3: save", )

def main(): #checks if new player, loads game()
	monster = randint(0,1) 
	ACTIONS = ( "Press 1 for FIGHT", "Press 2 for FLIGHT", )
	stageCount = 0
#	points = 0

	print("You wanna play? Press any key for \'Yes' or 0 for \'No'.")
	wannaPlay = input("> ")
	if wannaPlay != "0":
		game(monster, ACTIONS, stageCount)
	else:
		print("Thanks, bye.")
		sys.exit

if __name__ == "__main__":
	main()