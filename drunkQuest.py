import sys
import os
from random import randint
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
#STEP 1
		game()
	else:
		print("Thanks, bye.")
		sys.exit

if __name__ == "__main__":
	main()