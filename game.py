import sys
import textwrap
from text_adv import *

"""
need ERROR_CHECKING()
need new CLASS for passing all these damn arguments
"""

#not at all flexible right now
def ERROR_CHECKING(choice):
	print("\nYou entered \'{}', an invalid option".format(choice))
	print("\nYou must choose either \'1' or \'0'")

#testing points...should call
	points = 0
	choicesActionList(monster, actions, bonus, points)	

class Monster(): #runs calculations
	def __init__(self, name="baddie", bonus=0):
		self.name = name
		self.monsterName = ""
		self.bonus = 0

	def generateMonster(self, monster):
		if monster > 0:
			self.monsterName = "cops"
			cops(self)
		else:
			self.monsterName = "bros"
			bros(self)

	def modifyMonster(self, choice, actions, stageONE, bonus):
		if choice == "1":
			print("\nYou chose...to FIGHT!")
		elif choice == "2":
			print("\nYou chose...to FLEE!")
		
		else:
#need to pass enough for choicesActionList(player_choice, actions, monster, bonus)
			ERROR_CHECKING(choice)
		
#to do logic
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
#	monster.monsterName = "cops"
	
	print("\n")
	description = """A handful of the boys in blue approach. They are swinging their billy clubs like they mean it. One steps between you and where you're stumbling; he holds up his hand and says, 'Good evening, ya doin' alright, son?' Meanwhile, the other cops snicker in the background."""
	print("\n")
	print(textwrap.fill(description))
	
#	return monster.monsterName

#this will calculate rolls for monsters & the player
def randomRoll(monster, bonus):
	player_bid = randint(1,12)
	monster_bid = randint(1,12)

	if player_bid > monster_bid:
		return True
	elif player_bid == monster_bid:
		print("You lucky bastard. The round continues. Choose again!")
#need arguments for choiceActionList()
		choicesActionList()
	else:
		return False
	pass

def choicesActionList(monster, actions, bonus, points):
	print("\n")
	print("\nYou may choose to either fight or to run away:")
	for action in actions:
		print(action)
	player_choice = input("> Enter a number: ")
	monster.modifyMonster(player_choice, actions, monster, bonus)

def describeStage(stageCount, gameOn):
	if stageCount == 0:
		print("\nDrunken fluids swirl in your bowels as you exit the bar.")
		print("The lonely street calls to you...")
		print("You begin stumbling forward in the chilly street light.")
	elif stageCount == 1:
		pass
	elif stageCount == 2:
		pass
	else: #Win Condition
		gameOn = False
		print("\nYou found your way home. You pass out and win life.")
		return gameOn

def gameEnd(gameOn, monster, bonus, actions, points):
	print("\nYour night has ended. Thanks for playing!")
	gameOn = False
	gamePlay(gameOn, monster, bonus, actions, points)

def game(monster, actions, stageCount, points): #runs first from main()
#setting variables...maybe need to be elsewhere eventually
	bonus = 0
	gameOn = True

	print("\n", textwrap.fill(WELCOME_SPLASH, width=50))
	#continue1 = ""
	print("\nPress any key to: Start making your way home.") 
	print("...OR...")
	print("Press \'0' to: Lay down on the sidewalk and let the night take you...out of the game.")
	continue1 = input("> ")
	
	if continue1 == "0":
		gameEnd(gameOn, monster, bonus, actions, points)
	else:
		describeStage(stageCount, gameOn)
		gamePlay(gameOn, monster, actions, bonus, points)

def gamePlay(gameOn, monster, actions, bonus, points):
	if gameOn == True:
		stageONE = Monster()
		stageONE.generateMonster(monster)
		choicesActionList(stageONE, actions, bonus, points)
	else:
		sys.exit
