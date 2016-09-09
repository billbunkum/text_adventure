import sys
import textwrap
import time
from drunkQuest import *

"""
TO-FIX:
	1. When Quit on first stage, tallies a stageCount
	2. Remove Health
	3. Add extra Monsters
	4. Output stageCount like they are points
	5. While loop should ONLY end if a) Lose or b) Quit
	6. Add SAVE option for LEADER BOARD of TOP SCORES

"""

WELCOME_SPLASH = ("""You raise your head from the bar-top; the world is swimming. How much have you had to drink? Looking about, you see no one in the bar. Your memory is foggy; you've got to get home...but, alas, there are 3 blocks between you and that sweet heavenly abode! You pull yourself to your feet and nearly vomit. You are, however, no mere mortal who can be disuaded their comfy bed by a little alcohol poisoning. Making your way out into the sick, street light, you hear the dumb sounds of bros chattering and the Orwellian song of police sirens on the whispering wind. Time is short, dear adventurer of the night-stalking wonder! Make haste!""")

ACTIONS = ( "1: FIGHT", "2: FLIGHT", )

def ERROR_CHECKING(choice):
	print("\nYou entered \'{}', an invalid option".format(choice))
	choicesList()
#if choice was None; choicesList() will throw an error once a VALID choice is eventually entered...

class DisplayGoodness():
	def __init__(self, stageCount=0, gameOn=True):
		self.stageCount = 0
		self.gameOn = True

	def titleSplash(self):
		os.system("clear")
		print("""▒█▀▀▄ ▒█▀▀█ ▒█░▒█ ▒█▄░▒█ ▒█░▄▀ 　 ▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀""")
		print("""▒█░▒█ ▒█▄▄▀ ▒█░▒█ ▒█▒█▒█ ▒█▀▄░ 　 ▒█░▒█ ▒█░▒█ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░""")
		print("""▒█▄▄▀ ▒█░▒█ ░▀▄▄▀ ▒█░░▀█ ▒█░▒█ 　 ░▀▀█▄ ░▀▄▄▀ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░""")

	def monstersWin(self):
		print("▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀")
		print("▒█▒█▒█ █░░█ █░░█ ▀▀█ ░░█░░ █▀▀ █▄▄▀ ▀▀█")
		print("▒█░░▒█ ▀▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀▀▀")
		print("			▒█░░▒█ ▀█▀ ▒█▄░▒█")
		print("			▒█▒█▒█ ▒█░ ▒█▒█▒█")
		print("			▒█▄▀▄█ ▄█▄ ▒█░░▀█")

	def wannaPlay(self):
		print("\n", textwrap.fill(WELCOME_SPLASH, width=50))
	#continue1 = ""
		print("\nPress any key to: Start making your way home.") 
		print("...OR...")
		print("Press \'0' to: Lay down on the sidewalk and let the night take you...out of the game.")

	def stage_display(self, stageCount):	
		if stageCount == 0:
			stageCount += 1
			print("\nRemember...You 'lose the game' if you lose an encounter.")
			time.sleep(2)
			print("Prepare for STAGE ONE...")
			time.sleep(2)
			print("\nDrunken fluids swirl in your bowels as you exit the bar.")
			time.sleep(1)
			print("The lonely street calls to you...")
			time.sleep(1)
			print("You begin stumbling forward in the chilly street light.")

			return (stageCount, self.gameOn)

		elif stageCount == 1:
			stageCount += 1
			print("\nReady for STAGE TWO?!")
			return (stageCount, self.gameOn)

		elif stageCount == 2:
			stageCount += 1
			print("\nReady for STAGE THREE?!")
			return (stageCount, self.gameOn)

		else: 
			stageCount += 1
			self.gameOn = False
#			print("\nYou found your way home! You pass out and WIN life, forever.")
			return (stageCount, self.gameOn)
			gameEnd()

class Player():
	def __init__(self, points=0, bonus=0):
		self.points = 0
		self.bonus = 0

	def gainPoints(self):
		self.points += 1
		return self.points

class Monster():
	def __init__(self):
		self.monsterName = ""

	def bros(self): #if monster = 0
		self.monsterName = "bros"

		print("*"*10)
		time.sleep(2)
		print("\nA bro of the night...a 'night bro?' you find yourself thinking,") 
		print("the thought almost makes you laugh but you begin coughing")
		print("as you choke back some vomit...")
		print("*"*10)
		time.sleep(2)
		description1 = """\nA bottle of foul smelling liquor explodes just feet in front of you; green shards of glass scatter every where. Snickering emminates from a tree branch high above you; as you crane your neck in that direction, you see a tall, athletic youth swinging from the branch; a weird symbol is emblazened on his pink sweater."""
		description2 = """\nIs it Greek? The bro drops down to the pavement in front of you blocking your path. 'Where do ya think *hic-cup yer goin', pussy?'"""
		x = input("Press any key to deal with the bros...")
		print("\n")
		print(textwrap.fill(description1))
		print(textwrap.fill(description2))

		return self.monsterName

	def cops(self): #if monster = 1
		self.monsterName = "cops"
		
		print("*"*10)
		time.sleep(2)
		print("\nCops...'Oh great', you mutter as you gauge the situation...")
		print("*"*10)
		time.sleep(2)
		print("\nAs you turn your head, the world swims in front of you...")
		print("you stop gauging the situation just as quickly...")
		time.sleep(1)
		description = """A handful of the boys in blue approach. They are swinging their billy clubs like they mean it. One steps between you and where you're stumbling; he holds up his hand and says, 'Good evening, ya doin' alright, son?' Meanwhile, the other cops snicker in the background."""
		x = input("Press any key to deal with the cops...")
		print("\n")
		print(textwrap.fill(description))
		
		return self.monsterName


class Calculations():
	def __init__(self, player_bid=0, monster_bid=0, gameOn=True, monster_type=3, bonus=0, monsterName="baddies"):
		self.player_bid = 0
		self.monster_bid = 0
		self.gameOn = True
		self.monster_type = 3
		self.bonus = 0
		self.monsterName = "baddies"

	def randomRoll(self, monster_type, choice):
		if (monster_type == 0 and choice == "1"):
			self.bonus = 3
			print("\nYour bonus is: +{}".format(self.bonus))
		elif (monster_type == 1 and choice == "2"):
			self.bonus = 3
			print("\nYour bonus is: +{}".format(self.bonus))

		self.player_bid = (randint(1,12) + self.bonus)
		print("\nYour roll was: {}".format(self.player_bid))

		self.monster_bid = randint(1,12)
		print("\nThe {}' roll was: {}".format(self.monsterName, self.monster_bid))

		return self.player_bid, self.monster_bid

	def compareBids(self, player_bid, monster_bid):
		if player_bid > monster_bid:
			print("You beat them!")
			x = input("Press any key to continue...")
			return True
		elif self.player_bid == self.monster_bid:
			print("You lucky bastard. The round continues. Choose again!")
			y = input("The suspense is killing us...")
			choicesList()

		else:
			print("\nOh no! They beat YOU!")
			z = input("Your ancestors are weeping...press any key to Exit.")	
# need to pass stage (instance of Display) to call stage.monstersWin()
			gameOn = False
			return gameOn

	def generateMonster(self, monster):
		self.monster_type = randint(0,1)

# cops & bors not defined
		if self.monster_type == 0:
			monsterName = monster.bros()
			return monsterName, self.monster_type
		else:
			monsterName = monster.cops()
			return monsterName, self.monster_type

def choicesList():
	print("\n")
	print("\nYou may choose to either fight or to run away:")
	print("\nPress 0 to sit down and give up.")

	for act in ACTIONS:
		print(act)
	
	choice = input("> Enter a number: ")
	
	if choice == "0":
		gameOn = False
		return gameOn, choice
	
	elif choice == "1":
		gameOn = True
		print("You chose...to FIGHT!")
		return gameOn, choice

	elif choice == "2":
		gameOn = True
		print("You chose...to FLEE!")
		return gameOn, choice

	else:
		ERROR_CHECKING(choice)

def gameEnd():
	gameOn = False
	sys.exit

def game(): #runs first from main()
	stageCount = 0

	splash = DisplayGoodness()
	splash.titleSplash()
	splash.wannaPlay()
	continueOption = input("> ")

	if continueOption == "0":
		gameOn = gameEnd()
		gamePlay(gameOn, stageCount)
	else:
		gameOn = True
		gamePlay(gameOn, stageCount)

def gamePlay(gameOn, stageCount):
	stage = DisplayGoodness()
	calcs = Calculations()
	monster = Monster()

	while gameOn:
		if gameOn:

			stageCount, gameOn = stage.stage_display(stageCount)

			player = Player()
		#	points = player.displayPoints()

			monsterName, monster_type = calcs.generateMonster(monster)

			gameOn, choice = choicesList()
			if gameOn:
				player_bid, monster_bid = calcs.randomRoll(monster_type, choice)
			
				gameOn = calcs.compareBids(player_bid, monster_bid)

			if stageCount == 3:
				time.sleep(2)
				print("*"*10)
				print("\nYou found your way home! You pass out and WIN life, forever.")
				print("Thanks for playing.")

		else:
			time.sleep(1)
			print("*"*10)
			print("\nYour night has ended. Thanks for playing!")
			print("\nYou passed {} stages".format((stageCount)))
#doesn't actually exit the game yet
			break

	time.sleep(1)
	print("\n!!!!You passed {} STAGES!!!!".format(stageCount))

