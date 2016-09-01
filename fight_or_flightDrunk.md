#Fight or Flight Drunk

// refers to future versions

##Game build

1. The PC (the drunk) begins at THE BAR and must traverse (3) stages before reaching HOME and winning. One of (2) different monsters will attack the PC on each stage. POINTS are accrued as the PC overcomes each monster. 

The PC may choose to FIGHT or FLIGHT. Each monster responds differently to an ACTION depending on its nature; either way, there is chance involved. 

While certain ACTIONS are better for certain monsters, the PC is awarded extra POINTS for choosing the more difficult ACTION. 

//In the end, winning is calculated by 1) arriving HOME and 2) having the most POINTS (stories of drunk adventures).

2. win condition
	- if PC gets HOME (the stage number (4))
		* get HOME by arriving at stage (4)

3. lose condition
	- if PC loses an enounter with a monster

4. encounter a monster at each stage
	- display description of monster
	- type of monster determines EASY action and HARD action
		* easy action grants +2 bonus() to player roll and +1 to action_points if win
		* hard action grants +0 to player roll and +2 to action_points if win

5. player makes an ACTION choice -- player_bid

6. player_bid() gets random roll value + bonus()

7. monster_bid() gets random roll value
	- as bonus() has already been determined, monster_bid() is the same for any monster

8. both values are compared

	- rolls based off random number between 0-12

9. if WIN, determine points
	- player_points = player_points + action_points

10. if LOSE, display player_points and exit game

11. //manner of victory
	- determined by number of final points
		* POOR if 3 points
		* MEDIOCRE if 5 points
		* EPIC if 7 points

##What can be done by the player()
1. FIGHT

2. FLIGHT

5. stageCount auto-increments +1 if win

3. //MOVE
	- moves to next Stage
4. //STAY (to drink more)
	- resets current Stage but grants +1 points	


###OTHER STUFF -- Brainstorming 
* Under-the-hood
2. main() -- initializes: 
	- loads game()
	- saves/loads saved files

3. game()
	- houses everything sans main()

###Classes
1. Stage()
	- simple stage description (1, 2 or 3)
	- calls random Monster() method
		* chooses & displays monster description

	- calls actions() & returns player_roll
	- compares player's & current monster's roll
		* if WIN, compares player's choice to current monster type to add points
		* if LOSE, display splash and exit game

	- determines points()
	- 
	- calls 

2. Monster() -- option is always FIGHT
	- cops & bros
		* returns description
		* returns random FIGHT roll
	- //dellusions

###Functions
1. game()
 	- calls player()
 		* if saved game, calls that player from file
 		* //file includes: top score
 		* otherwise, calls fresh player & calls splash()

	- counts Stage() calls; 
		* calls win() at (3)
	 	* while stageCount < 3 loop?

2. splash()
	- houses:
		* splash screen
		* //graphics
		* current points
		* displays INSTRUCTIONS
		* ACTION choices list

3. win()
	- sums points() and calculates level of win

4. actions()
	- displays ACTION_LIST
	- returns player's numbered choice


###Brainstorming:
1. Both player and monster go at the same time; rolls are compared immediately when player makes her choice of ACTION

2. actions
	- fight
	- flight
	- move
	- //stay

3. monsters (either fight or flight)
	- cops
		* description
		* grant +2 action_points for FIGHT
		* grant +1 action_points for FLIGHT (they are unfit to running)

	- bros
		* description
		* grant +2 action_points for FLIGHT
		* grant +1 action_points for FIGHT (they respect you for being a fellow bro)

	//- dellusions
		* description
		* masks from PC what monster type is generated

4. dialogue
	- description of each stage
	- //added description to monster based on stage & sobriety

5. stages
	- all are identical save for:
		* description (nominal)
		* (1) randomized monster appears

6. points
	- begin play with 0 points
	- awarded points for ACTIONS:
	- //STAY -- +1 point & current stage resets
	- MOVE -- +0 points
	- LOSE -- +0 points & GAME ENDS
	- WIN -- +1 points

##Further versions
1. ask user for no. of drinks (decides difficulty/strategy)
2. different monsters
3. different characters (to play)
4. weapons
5. other actions, e.g. "talk your way out"
6. music for when you die/win/etc.
7. add different types of stages (can be interacted with)
8. multiple monsters
9. points & leader board
10. add STAY action for better strategy