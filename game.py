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

#not at all flexible right now
def ERROR_CHECKING(monster, monster_type, stageCount, choice, actions, bonus):
	print("\nYou entered \'{}', an invalid option".format(choice))
	#print("\nYou must choose either \'1' or \'0'")
	choicesActionList(monster, stageCount, monster_type, actions, bonus)	

class Monster(): #runs calculations
	def __init__(self, monsterName="The baddie"):
		self.monsterName = "The baddie"
#		self.actions = None
#		self.bonus = 0
#		self.points = 0
#		self.player_bid = 0
#		self.monster_bid = 0
#		self.monster_type = None

	def randomRoll(self, choice, monster_type, stageCount, actions, bonus):
		self.player_bid = randint(1,12) + bonus
		print("\nYour roll was: {}".format(self.player_bid))
		self.monster_bid = randint(1,12)
		print("\nThe {}' roll was: {}".format(self.monsterName,self.monster_bid))

		if self.player_bid > self.monster_bid:
			print("You beat them!")
			self.gameOn = True
			return self.gameOn
		elif self.player_bid == self.monster_bid:
			print("You lucky bastard. The round continues. Choose again!")
			choicesActionList(self, stageCount, monster_type, actions, bonus)
		else:
			self.gameOn = False
#			health -= 1
#			return self.gameOn
			print("\nOh no! They beat YOU!")
			print("\n")
			print("▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀")
			print("▒█▒█▒█ █░░█ █░░█ ▀▀█ ░░█░░ █▀▀ █▄▄▀ ▀▀█")
			print("▒█░░▒█ ▀▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀▀▀")
			print("			▒█░░▒█ ▀█▀ ▒█▄░▒█")
			print("			▒█▒█▒█ ▒█░ ▒█▒█▒█")
			print("			▒█▄▀▄█ ▄█▄ ▒█░░▀█")
			gameEnd(self.gameOn, self, stageCount, actions, bonus)


#STEP 5
#really only set the monsterName...also, use to set Bonus or Points??
	def generateMonster(self, monster_type):
		if monster_type > 0:
			cops(self)
			return self.monsterName
		else:
			bros(self)
			return self.monsterName

#STEP 8
	def modifyMonster(self, choice, stageCount, monster_type, actions, bonus):
		if choice == "1":
			print("\nYou chose...to FIGHT!")
			self.randomRoll(choice, monster_type, stageCount, actions, bonus)
			if self.gameOn:
#				reset bonus for next round
				bonus = 0

				gamePlay(self.gameOn, stageCount, monster_type, actions, bonus)
			else:
				gameEnd(self.gameOn, stageCount, monster_type, actions, bonus)
		elif choice == "2":			
			print("\nYou chose...to FLEE!")
			self.randomRoll(choice, stageCount, monster_type, actions, bonus)
			if self.gameOn:
#				reset bonus for next round
				bonus = 0

				gamePlay(self.gameOn, stageCount, monster_type, actions, bonus)
			else:
				gameEnd(self.gameOn, stageCount, monster_type, actions, bonus)
		else:
			ERROR_CHECKING(self, choice, stageCount, monster_type, actions, bonus)
		
#		to do logic
		if self.monsterName == "bros":
			bonus = 0
			pass
		if self.monsterName == "cops":
			bonus = 0
			pass

def bros(monster): #if monster = 0
	monster.monsterName = "bros"

	print("\n")
	description = """A bottle of foul smelling liquor explodes just feet in front of you; green shards of glass scatter every where. Snickering emminates from a tree branch high above you; as you crane your neck in that direction, you see a tall, athletic youth swinging from the branch; a weird symbol is emblazened on his pink sweater. Is it Greek? The bro drops down to the pavement in front of you blocking your path. 'Where do ya think *hic-cup yer goin', pussy?'"""
	print("\n")
	print(textwrap.fill(description))

	return monster.monsterName

def cops(monster): #if monster = 1
	monster.monsterName = "cops"
	
	print("\n")
	description = """A handful of the boys in blue approach. They are swinging their billy clubs like they mean it. One steps between you and where you're stumbling; he holds up his hand and says, 'Good evening, ya doin' alright, son?' Meanwhile, the other cops snicker in the background."""
	print("\n")
	print(textwrap.fill(description))
	
	return monster.monsterName

#STEP 7
def choicesActionList(stageONE, stageCount, monster_type, actions, bonus):
	print("\n")
	print("\nYou may choose to either fight or to run away:")
	print("\nPress 0 to sit down and give up.")
	for act in actions:
		print(act)
	choice = input("> Enter a number: ")
	if choice == "0":
		gameOn = False
		gameEnd(gameOn, stageCount, monster_type, actions, bonus)
	else:
		stageONE.modifyMonster(choice, stageCount, monster_type, actions, bonus)

#STEP 3
def describeStage(stageCount, gameOn):
	if stageCount == 0:
		stageCount += 1
		print("\nDrunken fluids swirl in your bowels as you exit the bar.")
		print("The lonely street calls to you...")
		print("You begin stumbling forward in the chilly street light.")
		return (stageCount, gameOn)
	elif stageCount == 1:
		stageCount += 1
		print("\nReady for stage TWO?!")
		return (stageCount, gameOn)
	elif stageCount == 2:
		stageCount += 1
		print("\nReady for stage THREE?!")
		return (stageCount, gameOn)
	else: 
		stageCount += 1
		gameOn = False
		print("\nYou found your way home! You pass out and WIN life, forever.")
		return (stageCount, gameOn)

def gameEnd(gameOn, stageCount, monster_type, actions, bonus):
	gameOn = False
	gamePlay(gameOn, stageCount, monster_type, actions, bonus)

#STEP 2
def game(actions): #runs first from main()
#setting variables...maybe need to be elsewhere eventually
	bonus = 0
	gameOn = True
	stageCount = 0
	monster_type = None

	print("\n", textwrap.fill(WELCOME_SPLASH, width=50))
	#continue1 = ""
	print("\nPress any key to: Start making your way home.") 
	print("...OR...")
	print("Press \'0' to: Lay down on the sidewalk and let the night take you...out of the game.")
	continueOption = input("> ")
	
	if continueOption == "0":
		gameEnd(gameOn, stageCount, monster_type, actions, bonus)
	else:
		describeStage(stageCount, gameOn)
		gamePlay(gameOn, stageCount, monster_type, actions, bonus)

#STEP 4 & STEP 6
def gamePlay(gameOn, stageCount, monster_type, actions, bonus):
	if gameOn == True:
		monster_type = randint(0,1) #redetermines monster_type
		describeStage(stageCount, gameOn)
##
# How to actually utilize a 'return gameOn'...cos it ain't workin'
	else:
		print("\nYour night has ended. Thanks for playing!")
		print("\nYou passed {} stages".format(stageCount))

	print("\nstageCount is: {}".format(stageCount)) #for testing

	if stageCount < 3:
		stageONE = Monster()
		stageONE.generateMonster(monster_type)

		choicesActionList(stageONE, stageCount, monster_type, actions, bonus)
##
#what does this actually do?
