import sys
import textwrap
from text_adv import *

"""
TO-FIX:
	
	**. text_adv.py > game(monster_type, stageCount, ACTIONS) is not actually working how I thought it would...what is going on with these arguments?
	1. stageCount is doing something WEIRD...i'm misunderstanding how passing variables works
	2. setting CLASS variables/arguments is weird; what is it doing when you 'self.gameOn = True w/in def __init__' vs 'gameOn=True as an arg'?
	3. why is gameEnd printing multiple times?
	4. points
	5. Need 'save' button / 'return player'
	6. Restructure - Need new CLASS for passing all these damn arguments

**	Add monsterCounter(), tallies up who you've FOUGHT and FLED from and prints it out.

** How does program continue with Return True/False from a function call?
"""

WELCOME_SPLASH = ("""You raise your head from the bar-top; the world is swimming. How much have you had to drink? Looking about, you see no one in the bar. Your memory is foggy; you've got to get home...but, alas, there are 3 blocks between you and that sweet heavenly abode! You pull yourself to your feet and nearly vomit. You are, however, no mere mortal who can be disuaded their comfy bed by a little alcohol poisoning. Making your way out into the sick, street light, you hear the dumb sounds of bros chattering and the Orwellian song of police sirens on the whispering wind. Time is short, dear adventurer of the night-stalking wonder! Make haste!""")

ACTIONS = ( "1: FIGHT", "2: FLIGHT", )

def ERROR_CHECKING(choice):
	print("\nYou entered \'{}', an invalid option".format(choice))
	#print("\nYou must choose either \'1' or \'0'")
	choicesList()

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
			x = input("Prepare for STAGE ONE...")
			y = input("\nRemember...You lose if you lose an encounter.")
			print("\nDrunken fluids swirl in your bowels as you exit the bar.")
			print("The lonely street calls to you...")
			print("You begin stumbling forward in the chilly street light.")

			return (stageCount, self.gameOn)

		elif stageCount == 1:
			stageCount += 1
			print("\nReady for stage TWO?!")
			return (stageCount, self.gameOn)

		elif stageCount == 2:
			stageCount += 1
			print("\nReady for stage THREE?!")
			return (stageCount, self.gameOn)

		else: 
			stageCount += 1
			gameOn = False
			print("\nYou found your way home! You pass out and WIN life, forever.")
			return (stageCount, self.gameOn)

class Player():
	def __init__(self, health=1, points=0, bonus=0):
		self.health = 1
		self.points = 0
		self.bonus = 0

	def gainPoints(self):
		self.points += 1
		return self.points

	def displayHealth(self):
		print("\n")
		print("Your current health is: {}".format(self.health))
		return self.health

	def loseHealth(self):
		self.health -= 1
		return self.health

class Monster():
	def __init__(self):
		self.monsterName = ""

	def bros(self): #if monster = 0
		self.monsterName = "bros"

		print("\n")
		description1 = """\nA bottle of foul smelling liquor explodes just feet in front of you; green shards of glass scatter every where. Snickering emminates from a tree branch high above you; as you crane your neck in that direction, you see a tall, athletic youth swinging from the branch; a weird symbol is emblazened on his pink sweater."""
		description2 = """\nIs it Greek? The bro drops down to the pavement in front of you blocking your path. 'Where do ya think *hic-cup yer goin', pussy?'"""
		print("\n")
		print(textwrap.fill(description1))
		print(textwrap.fill(description2))

		return self.monsterName

	def cops(self): #if monster = 1
		self.monsterName = "cops"
		
		print("\n")
		description = """A handful of the boys in blue approach. They are swinging their billy clubs like they mean it. One steps between you and where you're stumbling; he holds up his hand and says, 'Good evening, ya doin' alright, son?' Meanwhile, the other cops snicker in the background."""
		print("\n")
		print(textwrap.fill(description))
		
		return self.monsterName


class Calculations():
	def __init__(self, player_bid=0, monster_bid=0, gameOn=True, monster_type=3, bonus=0):
		self.player_bid = 0
		self.monster_bid = 0
		self.gameOn = True
		self.monster_type = 3
		self.bonus = 0

	def randomRoll(self, monster_type, choice):
		if (monster_type == 0 and choice == 1) or (monster_type == 1 and choice == 0):
			self.bonus = 3
		self.player_bid = randint(1,12) + self.bonus
#		print("\nYour roll was: {}".format(self.player_bid))

		self.monster_bid = randint(1,12)
#		print("\nThe {}' roll was: {}".format(self.monsterName, self.monster_bid))

		return self.player_bid, self.monster_bid

	def compareBids(self, player_bid, monster_bid):
		if player_bid > monster_bid:
			print("You beat them!")
			return True
		elif self.player_bid == self.monster_bid:
			print("You lucky bastard. The round continues. Choose again!")
			choicesList()

		else:
			print("\nOh no! They beat YOU!")
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
		gameEnd()
	
	elif choice == "1":
		print("You chose...to FIGHT!")
		return choice

	elif choice == "2":
		print("You chose...to FLEE!")
		return choice
	
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

	while stageCount <= 3:
		if gameOn == True:

			stageCount, gameOn = stage.stage_display(stageCount)

			player = Player()
			health = player.displayHealth()

			monsterName, monster_type = calcs.generateMonster(monster)

			choice = choicesList()
			player_bid, monster_bid = calcs.randomRoll(monster_type, choice)

			gameOn = calcs.compareBids(player_bid, monster_bid)

			#output WIN or LOSE (health 0)

		else:
			print("\nYour night has ended. Thanks for playing!")
			print("\nYou passed {} stages".format(stageCount))
			break

	print("\n!!!!stageCount is: {}!!!!".format(stageCount)) #for testing
