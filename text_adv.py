import sys
from game import *

"""
a text-based choose-your-own-adventure

to clear screen:
	import os
	os.system("clear")
"""

def main():
	print("\nAre you a returning player?")
	returning_player = input("\n1: \'Yes'. Press any other key for \'No'")

	if returning_player == "1":
		pass
	else:
		game()

	choice = input("\nPress 0 to quit. Press any key to continue.")
	
	if choice == "0":
		sys.exit
	else:
		game()

if __name__ == "__main__":
	main()