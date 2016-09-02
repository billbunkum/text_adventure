import sys
import textwrap
from text_adv import *

"""
need ERROR_CHECKING()
"""

class Monster(): #runs calculations
	def __init__(self, name="baddie"):
		self.name = name
		self.monsterName = ""

	def generateMonster(self, monster):
		if monster > 0:
			self.monsterName = "cops"
			cops(self)
		else:
			self.monsterName = "bros"
			bros(self)

	def modifyMonster(self, choice, bonus):
		if choice == "1":
			print("\nYou chose to fight.")
		else:
			print("\nYou chose to flee.")

#to do logic
		if self.monsterName == "bros":
			bonus = 0
		if self.monsterName == "cops":
			bonus = 0

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

def choicesActionList(actions, monster, bonus):
	print("\n")
	print("\nYou may choose to either fight or to run away:")
	for action in actions:
		print(action)
	player_choice = input("> Enter a number: ")
	monster.modifyMonster(player_choice, bonus)

def describeStage():
	print("\nDrunken fluids swirl in your bowels as you exit the bar.")
	print("\nThe lonely street calls to you...")
	print("\nYou begin stumbling forward in the chilly street light.")


def game(monster, actions, stageCount, points):
	print("\n", textwrap.fill(WELCOME_SPLASH, width=50))
	describeStage()
	
	bonus = 0

	stageONE = Monster()
	stageONE.generateMonster(monster)
	
	choicesActionList(actions, stageONE, bonus)
	
