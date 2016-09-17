import sys
import os
from gameFile import *
"""
a text-based choose-your-own-adventure

to clear screen:
	import os
	os.system("clear")
"""

def main():
	print("\nYou wanna play? Press any key for \'Yes' or 0 for \'No'.")
	wannaPlay = input("> ")
	if wannaPlay != "0":
		game = RunTheGame()
		game.game()
	else:
		print("Thanks, bye.")
		sys.exit

if __name__ == "__main__":
	main()