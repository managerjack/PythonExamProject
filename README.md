# PythonExamProject
MyPythonGame

			ASSIGNMENT #4: Make your own application

Application:

	A python game inside the terminal. The game is an arcade game, where you play
	as a monsterhunter, who hunts for monsters by placing traps down for the
	monsters chasing you. 

Requirements:

	- No GUI implementation
	- Display and update the scoretext. Increase the scoretext by a certain amount for each monster killed.
	- 2 seperate lists containing the amount of monsters and traps left.
	- If a monster steps on a trap, the monster and the trap will be removed from the list.
	- If the player/monsterhunter steps on a trap, the player loses the game.
	- An input variable to detect user input for whenever the player wants to move, place traps or
	  check how many traps the player has in store.
	- The game should contain the following terminal input commands: "up", "down", "left", "right", "trap".
	- The player should be able to combine input commands with empty space, ex. "left trap right trap".
	- Traps cannot be placed at player's/monsterhunter's position, but around him, ex. "trap left", to place
	  a trap to the left of the player/monsterhunter.
	- Detect collision for whenever the player/monsterhunter or a monster steps on a trap.
	- Random generate traps by random turns over the field, so the player can pick them up and use them.
  
  Guide:
  
  1. You start the game by typing 'python monsterHunter.py' in the terminal.
  2. You should be able to see yourself, the player, on a 5x4 squared field.
  3. From here on, you can type either of the following commands in the terminal for movement: 
     'up', 'left', 'right' or 'down' to move one square.
  4. Monsters will appear on the field at your second movement. Your goal is to kill the monsters before they kill you.
  5. You kill them by using your traps. You can see how many traps you have in store by typing in the terminal:
     'traps' to see how many you have in store.
  6. If you do have traps in store, you can place at any position around you by typing:
     'left trap', 'right trap', 'up trap' or 'down trap' to place your trap.
  7. If you don't have any traps, you have to go look for the trapIcons on the field. By colliding with
     a trapIcon, you get a random amount of traps.
  8. Once a monster collides with a trap, they die and you get a point. Then a new monster appears.
     (If you see a text displaying 'GAME OVER' at the start of the game, that means you collided with a monster.
     It happens quite a lot, but you can just start the game again)
