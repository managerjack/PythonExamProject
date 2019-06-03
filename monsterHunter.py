#import colorama
#initialize colorama
#print colorama
import random

class Hunter: # My hunter class. This class contains all the variables for the hunter.

    def __init__(self, hunterUpper = '__  __', hunterMiddle = '|*||*|', hunterBottom = '  --  ',
    vertical = 2, horizontal = 'firstRow'):
        self.hunterUpper = hunterUpper
        self.hunterMiddle = hunterMiddle
        self.hunterBottom = hunterBottom
        self._vertical = vertical
        self._horizontal = horizontal


class Monster: # My monster class. This class contains all the variables for the monster.

    def __init__(self, monsterUpper = ' **** ', monsterMiddle ='*0  0*', monsterBottom =' **** ',
    vertical = 0, horizontal = '', monsterCount = 2):
        self.monsterUpper = monsterUpper
        self.monsterMiddle = monsterMiddle
        self.monsterBottom = monsterBottom
        self._vertical = vertical
        self._horizontal = horizontal
        self.monsters = []
        self.monsterCount = monsterCount


class TrapIcon: # My trapIcon class. This class contains all the variables for the trapIcon.

    def __init__ (self, trapIconUpper = '______', trapIconMiddle = '______', trapIconBottom = '@|  |@',
     trapIconCount = 1, horizontal = '', vertical = 0):
        self.trapIconUpper = trapIconUpper
        self.trapIconMiddle = trapIconMiddle
        self.trapIconBottom = trapIconBottom
        self.trapIconCount = trapIconCount
        self.horizontal = horizontal
        self.vertical = vertical
        self.trapIcons = []

class Trap: # My trap class. This class contains all the variables for the trap.

    def __init__(self, trapUpper = ' |  | ', trapMiddle =' |@@| ',  trapBottom ='|____|',
    vertical = 0 ):
        self.trapUpper = trapUpper
        self.trapMiddle = trapMiddle
        self.trapBottom = trapBottom  
        self.vertical = vertical
        self.traps = []
        
class ListTest: # My list class. This class contains all the variables for the game field.

    def __init__(self, slotUpper =  ' ____ ', slotMiddle = '|    |', slotBottom = '|____|',
    firstRowSlotNumber = 0, secondRowSlotNumber = 0, thirdRowSlotNumber = 0, fourthRowSlotNumber = 0):
        self.firstRowSlots = [slotUpper, slotUpper , slotUpper, slotUpper, slotUpper], [slotMiddle, slotMiddle, slotMiddle, slotMiddle, slotMiddle],[slotBottom, slotBottom, slotBottom, slotBottom, slotBottom]
        self.secondRowSlots = [slotUpper, slotUpper , slotUpper, slotUpper, slotUpper], [slotMiddle, slotMiddle, slotMiddle, slotMiddle, slotMiddle],[slotBottom, slotBottom, slotBottom, slotBottom, slotBottom]
        self.thirdRowSlots = [slotUpper, slotUpper , slotUpper, slotUpper, slotUpper], [slotMiddle, slotMiddle, slotMiddle, slotMiddle, slotMiddle],[slotBottom, slotBottom, slotBottom, slotBottom, slotBottom]
        self.fourthRowSlots = [slotUpper, slotUpper , slotUpper, slotUpper, slotUpper], [slotMiddle, slotMiddle, slotMiddle, slotMiddle, slotMiddle],[slotBottom, slotBottom, slotBottom, slotBottom, slotBottom]
        self.firstRowSlotNumber = firstRowSlotNumber
        self.secondRowSlotNumber = secondRowSlotNumber
        self.thirdRowSlotNumber = thirdRowSlotNumber
        self.fourthRowSlotNumber = fourthRowSlotNumber
        self.slotUpper = slotUpper
        self.slotMiddle = slotMiddle
        self.slotBottom = slotBottom

def field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots): 
# This method prints out the field. Depending on the input inside the methods parameter
# ,the field will be updated accordingly
    firstRowSlotNumber = ListTest().firstRowSlotNumber # Storing the row data inside a vairable
    secondRowSlotNumber = ListTest().secondRowSlotNumber
    thirdRowSlotNumber = ListTest().thirdRowSlotNumber
    fourthRowSlotNumber = ListTest().fourthRowSlotNumber

    for slotElement in firstRowSlots:   # Loops through every 'slot'-element in my row lists and prints
        print(*slotElement, sep="\t")   # them out
        firstRowSlotNumber = firstRowSlotNumber + 1

        if firstRowSlotNumber == 5:
            print(*slotElement, sep="\n")
            firstRowSlotNumber = 0

    for slotElement in secondRowSlots:
        print(*slotElement, sep="\t")
        secondRowSlotNumber = secondRowSlotNumber + 1

        if secondRowSlotNumber == 5:
            print(*slotElement, sep="\n")
            secondRowSlotNumber = 0

    for slotElement in thirdRowSlots:
        print(*slotElement, sep="\t")
        thirdRowSlotNumber = thirdRowSlotNumber + 1

        if thirdRowSlotNumber == 5:
            print(*slotElement, sep="\n")
            thirdRowSlotNumber = 0

    for slotElement in fourthRowSlots:
        print(*slotElement, sep="\t")
        fourthRowSlotNumber = fourthRowSlotNumber + 1

        if fourthRowSlotNumber == 5:
            print(*slotElement, sep="\n")
            fourthRowSlotNumber = 0

def playerInput(): # This method is responsible for handling the player's input in the console
                   # , monster spawn and movement, trap spawn and collision detection   
    vertical = Hunter()._vertical  # Variables from each and every class are being stored inside a
    horizontal = Hunter()._horizontal   #variable

    hunterUpper = Hunter().hunterUpper
    hunterMiddle = Hunter().hunterMiddle
    hunterBottom = Hunter().hunterBottom

    firstRowSlots = ListTest().firstRowSlots
    secondRowSlots = ListTest().secondRowSlots
    thirdRowSlots = ListTest().thirdRowSlots
    fourthRowSlots = ListTest().fourthRowSlots

    monsters = Monster().monsters
    monsterCount = Monster().monsterCount
    monsterUpper = Monster().monsterUpper
    monsterMiddle = Monster().monsterMiddle
    monsterBottom = Monster().monsterBottom
    
    monVertical = Monster()._vertical
    monHorizontal = Monster()._horizontal 

    trapIcons = TrapIcon().trapIcons
    trapIconCount = TrapIcon().trapIconCount
    trapIconHorizontal = TrapIcon().horizontal
    trapIconVertical = TrapIcon().vertical
    trapIconUpper = TrapIcon().trapIconUpper
    trapIconMiddle = TrapIcon().trapIconMiddle
    trapIconBottom = TrapIcon().trapIconBottom

    trapsList = Trap().traps
    trapUpper = Trap().trapUpper
    trapMiddle = Trap().trapMiddle
    trapBottom = Trap().trapBottom
    trapVertical = Trap().vertical

    traps = 0 # The amount of traps in store
    score = 0 # The amount of score  

    playing = True # Checks whether the player have lost or not
    
    while playing: # While the player haven't lost
        command = input() # The program will keep checking for next terminal input
       
        if command == 'traps' and command != '':   # Check how many traps are in store
            print('You have: ' + str(traps) + ' traps')

        if command != 'traps':  # Displays the score for every input
            print('\t\t\t\t' + 'SCORE: ' + str(score))

        if command == 'left' and horizontal == 'firstRow':  # Character movement depending on row position
            vertical = vertical - 1 # Pointing towards the slot to the left of the hunter 
            
            firstRowSlots[0][vertical] = hunterUpper  # Replacing the slot strings with hunter strings
            firstRowSlots[1][vertical] = hunterMiddle
            firstRowSlots[2][vertical] = hunterBottom

            firstRowSlots[0][vertical+1] = ListTest().slotUpper # Replacing the players previous position
            firstRowSlots[1][vertical+1] = ListTest().slotMiddle    # with the field slot, to prevent duplicates
            firstRowSlots[2][vertical+1] = ListTest().slotBottom    # of hunterstrings on the field
           
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots) # Updating the field with new values
            command = '' # Setting input to be something else to prevent going into other input funtions
        
        if command == 'left' and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --
            
            vertical = vertical - 1

            secondRowSlots[0][vertical] = hunterUpper
            secondRowSlots[1][vertical] = hunterMiddle
            secondRowSlots[2][vertical] = hunterBottom

            secondRowSlots[0][vertical+1] = ListTest().slotUpper
            secondRowSlots[1][vertical+1] = ListTest().slotMiddle
            secondRowSlots[2][vertical+1] = ListTest().slotBottom
           
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'left' and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --
           
            vertical = vertical - 1

            thirdRowSlots[0][vertical] = hunterUpper
            thirdRowSlots[1][vertical] = hunterMiddle
            thirdRowSlots[2][vertical] = hunterBottom

            thirdRowSlots[0][vertical+1] = ListTest().slotUpper
            thirdRowSlots[1][vertical+1] = ListTest().slotMiddle
            thirdRowSlots[2][vertical+1] = ListTest().slotBottom
           
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'left' and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --
            
            vertical = vertical - 1

            fourthRowSlots[0][vertical] = hunterUpper
            fourthRowSlots[1][vertical] = hunterMiddle
            fourthRowSlots[2][vertical] = hunterBottom

            fourthRowSlots[0][vertical+1] = ListTest().slotUpper
            fourthRowSlots[1][vertical+1] = ListTest().slotMiddle
            fourthRowSlots[2][vertical+1] = ListTest().slotBottom
           
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''

        if command == 'right' and horizontal == 'firstRow': # -- SAME RECIPE AS ABOVE --
            
            vertical = vertical + 1

            firstRowSlots[0][vertical] = hunterUpper
            firstRowSlots[1][vertical] = hunterMiddle
            firstRowSlots[2][vertical] = hunterBottom

            firstRowSlots[0][vertical-1] = ListTest().slotUpper
            firstRowSlots[1][vertical-1] = ListTest().slotMiddle
            firstRowSlots[2][vertical-1] = ListTest().slotBottom
            
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'right' and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --
         
            vertical = vertical + 1

            secondRowSlots[0][vertical] = hunterUpper
            secondRowSlots[1][vertical] = hunterMiddle
            secondRowSlots[2][vertical] = hunterBottom

            secondRowSlots[0][vertical-1] = ListTest().slotUpper
            secondRowSlots[1][vertical-1] = ListTest().slotMiddle
            secondRowSlots[2][vertical-1] = ListTest().slotBottom
            
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'right' and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --
          
            vertical = vertical + 1

            thirdRowSlots[0][vertical] = hunterUpper
            thirdRowSlots[1][vertical] = hunterMiddle
            thirdRowSlots[2][vertical] = hunterBottom

            thirdRowSlots[0][vertical-1] = ListTest().slotUpper
            thirdRowSlots[1][vertical-1] = ListTest().slotMiddle
            thirdRowSlots[2][vertical-1] = ListTest().slotBottom
            
            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'right' and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --
          
            vertical = vertical + 1

            fourthRowSlots[0][vertical] = hunterUpper
            fourthRowSlots[1][vertical] = hunterMiddle
            fourthRowSlots[2][vertical] = hunterBottom

            fourthRowSlots[0][vertical-1] = ListTest().slotUpper
            fourthRowSlots[1][vertical-1] = ListTest().slotMiddle
            fourthRowSlots[2][vertical-1] = ListTest().slotBottom 

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
            command = ''
        
        if command == 'down' and horizontal == 'firstRow': # If player wants to go down
        
            secondRowSlots[0][vertical] = hunterUpper   # Move the hunter to a row below the current row
            secondRowSlots[1][vertical] = hunterMiddle
            secondRowSlots[2][vertical] = hunterBottom

            firstRowSlots[0][vertical] = ListTest().slotUpper # Set hunter's revious row position to the field
            firstRowSlots[1][vertical] = ListTest().slotMiddle  # slot
            firstRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'secondRow'
            command = ''
        
        if command == 'down' and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --
        
            thirdRowSlots[0][vertical] = hunterUpper
            thirdRowSlots[1][vertical] = hunterMiddle
            thirdRowSlots[2][vertical] = hunterBottom

            secondRowSlots[0][vertical] = ListTest().slotUpper
            secondRowSlots[1][vertical] = ListTest().slotMiddle
            secondRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'thirdRow'
            command = ''
        
        if command == 'down' and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --
        
            fourthRowSlots[0][vertical] = hunterUpper
            fourthRowSlots[1][vertical] = hunterMiddle
            fourthRowSlots[2][vertical] = hunterBottom

            thirdRowSlots[0][vertical] = ListTest().slotUpper
            thirdRowSlots[1][vertical] = ListTest().slotMiddle
            thirdRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'fourthRow'
            command = ''

        if command == 'up' and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --
        
            firstRowSlots[0][vertical] = hunterUpper
            firstRowSlots[1][vertical] = hunterMiddle
            firstRowSlots[2][vertical] = hunterBottom

            secondRowSlots[0][vertical] = ListTest().slotUpper
            secondRowSlots[1][vertical] = ListTest().slotMiddle
            secondRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'firstRow'
            command = ''
        
        if command == 'up' and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --
        
            secondRowSlots[0][vertical] = hunterUpper
            secondRowSlots[1][vertical] = hunterMiddle
            secondRowSlots[2][vertical] = hunterBottom

            thirdRowSlots[0][vertical] = ListTest().slotUpper
            thirdRowSlots[1][vertical] = ListTest().slotMiddle
            thirdRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'secondRow'
            command = ''

        if command == 'up' and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --
        
            thirdRowSlots[0][vertical] = hunterUpper
            thirdRowSlots[1][vertical] = hunterMiddle
            thirdRowSlots[2][vertical] = hunterBottom

            fourthRowSlots[0][vertical] = ListTest().slotUpper
            fourthRowSlots[1][vertical] = ListTest().slotMiddle
            fourthRowSlots[2][vertical] = ListTest().slotBottom

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

            horizontal = 'thirdRow'
            command = ''

        if command == 'quit': # If the player wants to quit playing, program will stop
            playing = False

        if command == 'left trap' and traps > 0 and horizontal == 'firstRow': # Trap placements depending on 
                                                                              # hunter position and traps in store  
            trapVertical = vertical - 1 # Place trap to the left of hunter

            firstRowSlots[0][trapVertical] = trapUpper      # Set the row slot 
            firstRowSlots[1][trapVertical] = trapMiddle
            firstRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]      # Store the trap inside the traplist
            trapsList.append(trap)
            traps = traps - 1       # Decrease amount of traps by 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots) # Update the field

        if command == 'left trap' and traps > 0 and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical - 1

            secondRowSlots[0][trapVertical] = trapUpper
            secondRowSlots[1][trapVertical] = trapMiddle
            secondRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'left trap' and traps > 0 and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical - 1

            thirdRowSlots[0][trapVertical] = trapUpper
            thirdRowSlots[1][trapVertical] = trapMiddle
            thirdRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'left trap' and traps > 0 and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical - 1

            fourthRowSlots[0][trapVertical] = trapUpper
            fourthRowSlots[1][trapVertical] = trapMiddle
            fourthRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'right trap' and traps > 0 and horizontal == 'firstRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical + 1

            firstRowSlots[0][trapVertical] = trapUpper
            firstRowSlots[1][trapVertical] = trapMiddle
            firstRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'right trap' and traps > 0 and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical + 1

            secondRowSlots[0][trapVertical] = trapUpper
            secondRowSlots[1][trapVertical] = trapMiddle
            secondRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'right trap' and traps > 0 and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical + 1

            thirdRowSlots[0][trapVertical] = trapUpper
            thirdRowSlots[1][trapVertical] = trapMiddle
            thirdRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'right trap' and traps > 0 and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical + 1

            fourthRowSlots[0][trapVertical] = trapUpper
            fourthRowSlots[1][trapVertical] = trapMiddle
            fourthRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'up trap' and traps > 0 and horizontal == 'firstRow': # -- SAME RECIPE AS ABOVE --

            fourthRowSlots[0][vertical] = trapUpper
            fourthRowSlots[1][vertical] = trapMiddle
            fourthRowSlots[2][vertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'up trap' and traps > 0 and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --

            firstRowSlots[0][vertical] = trapUpper
            firstRowSlots[1][vertical] = trapMiddle
            firstRowSlots[2][vertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'up trap' and traps > 0 and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --

            secondRowSlots[0][vertical] = trapUpper
            secondRowSlots[1][vertical] = trapMiddle
            secondRowSlots[2][vertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'up trap' and traps > 0 and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --

            thirdRowSlots[0][vertical] = trapUpper
            thirdRowSlots[1][vertical] = trapMiddle
            thirdRowSlots[2][vertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        
        if command == 'down trap' and traps > 0 and horizontal == 'firstRow': # -- SAME RECIPE AS ABOVE --

            secondRowSlots[0][vertical] = trapUpper
            secondRowSlots[1][vertical] = trapMiddle
            secondRowSlots[2][vertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'down trap' and traps > 0 and horizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical

            thirdRowSlots[0][trapVertical] = trapUpper
            thirdRowSlots[1][trapVertical] = trapMiddle
            thirdRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'down trap' and traps > 0 and horizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical
            
            fourthRowSlots[0][trapVertical] = trapUpper
            fourthRowSlots[1][trapVertical] = trapMiddle
            fourthRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)

        if command == 'down trap' and traps > 0 and horizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --

            trapVertical = vertical

            firstRowSlots[0][trapVertical] = trapUpper
            firstRowSlots[1][trapVertical] = trapMiddle
            firstRowSlots[2][trapVertical] = trapBottom
            
            trap = [trapUpper, trapMiddle, trapBottom]
            trapsList.append(trap)
            traps = traps - 1

            field(firstRowSlots, secondRowSlots, thirdRowSlots, fourthRowSlots)
        # Checking collision bewteen the hunter and a nearby trap. If collided, player loses.
        if firstRowSlots[0][trapVertical] == firstRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if secondRowSlots[0][trapVertical] == secondRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if thirdRowSlots[0][trapVertical] == thirdRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if fourthRowSlots[0][trapVertical] == fourthRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        # Spawning monsters, when there are monsters in store
        if monsterCount > 0 and command == '':
        
            monster = [monsterUpper, monsterMiddle, monsterBottom]
            monsters.append(monster)    # Add monster to the monsterlist

            randomInt = random.randint(0, 7) # Generate random number to determind where the monster
                                                # will spawn depending on the number
            for monster in monsters: # For each monster in the list
                    # Check the random value and spawn the monster according to the value
                    if randomInt == 0:
                        
                        monVertical = 0  # Spawning to the far left side

                        firstRowSlots[0][monVertical] = monster[0] # Spawning far left side on the firstrow
                        firstRowSlots[1][monVertical] = monster[1]
                        firstRowSlots[2][monVertical] = monster[2]

                        monHorizontal = 'firstRow' # Set monster's horizontal position to 'firstRow'

                    if randomInt == 1: # -- SAME RECIPE AS ABOVE --

                        monVertical = 4  
                    
                        firstRowSlots[0][monVertical] = monster[0]
                        firstRowSlots[1][monVertical] = monster[1]
                        firstRowSlots[2][monVertical] = monster[2]

                        monHorizontal = 'firstRow'

                    if randomInt == 2: # -- SAME RECIPE AS ABOVE --

                        monVertical = 0

                        fourthRowSlots[0][0] = monster[0]
                        fourthRowSlots[1][0] = monster[1]
                        fourthRowSlots[2][0] = monster[2] 

                        monHorizontal = 'fourthRow'

                    if randomInt == 3: # -- SAME RECIPE AS ABOVE --

                        monVertical = 4  
                    
                        fourthRowSlots[0][4] = monster[0]
                        fourthRowSlots[1][4] = monster[1]
                        fourthRowSlots[2][4] = monster[2]

                        monHorizontal = 'fourthRow' 
                    
                    if randomInt == 4: # -- SAME RECIPE AS ABOVE --

                        monVertical = 4  
                    
                        secondRowSlots[0][4] = monster[0]
                        secondRowSlots[1][4] = monster[1]
                        secondRowSlots[2][4] = monster[2]

                        monHorizontal = 'secondRow' 

                    if randomInt == 5: # -- SAME RECIPE AS ABOVE --

                        monVertical = 0  
                    
                        secondRowSlots[0][0] = monster[0]
                        secondRowSlots[1][0] = monster[1]
                        secondRowSlots[2][0] = monster[2]

                        monHorizontal = 'secondRow' 
                    
                    if randomInt == 6: # -- SAME RECIPE AS ABOVE --

                        monVertical = 0  
                    
                        thirdRowSlots[0][0] = monster[0]
                        thirdRowSlots[1][0] = monster[1]
                        thirdRowSlots[2][0] = monster[2]

                        monHorizontal = 'thirdRow' 

                    if randomInt == 7: # -- SAME RECIPE AS ABOVE --

                        monVertical = 4  
                    
                        thirdRowSlots[0][4] = monster[0]
                        thirdRowSlots[1][4] = monster[1]
                        thirdRowSlots[2][4] = monster[2]

                        monHorizontal = 'thirdRow' 

            monsterCount = monsterCount - 1 # Monster spawned, decrease value of monster in store
        # Check collision between the hunter and a nearby monster. If collided, player loses.
        if firstRowSlots[0][monVertical] == firstRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if secondRowSlots[0][monVertical] == secondRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if thirdRowSlots[0][monVertical] == thirdRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if fourthRowSlots[0][monVertical] == fourthRowSlots[0][vertical] and horizontal == monHorizontal:
                            print('\t\t' + 'GAME OVER' + '\t\t')
                            playing = False

        if command == '': # Function for handling monster movement after spawn

            if monVertical == 4: # If monster is on the far right side of a row, prevent it from going
                monVertical = monVertical - 1   # any further
            if monVertical == 0: # If monster is on the far left side of a row, prevent it from going
                monVertical = monVertical + 1 # any further
            

            if monHorizontal == 'firstRow': # Depending on monster row postion, 
                                            # move monster either left or right
                monVertical = monVertical + 1

                firstRowSlots[0][monVertical] = monster[0]
                firstRowSlots[1][monVertical] = monster[1]
                firstRowSlots[2][monVertical] = monster[2]

                firstRowSlots[0][monVertical-1] = ListTest().slotUpper
                firstRowSlots[1][monVertical-1] = ListTest().slotMiddle
                firstRowSlots[2][monVertical-1] = ListTest().slotBottom
            
            if monHorizontal == 'secondRow': # -- SAME RECIPE AS ABOVE --

                monVertical = monVertical - 1

                secondRowSlots[0][monVertical] = monster[0]
                secondRowSlots[1][monVertical] = monster[1]
                secondRowSlots[2][monVertical] = monster[2]

                secondRowSlots[0][monVertical+1] = ListTest().slotUpper
                secondRowSlots[1][monVertical+1] = ListTest().slotMiddle
                secondRowSlots[2][monVertical+1] = ListTest().slotBottom
            
            if monHorizontal == 'thirdRow': # -- SAME RECIPE AS ABOVE --

                monVertical = monVertical + 1

                thirdRowSlots[0][monVertical] = monster[0]
                thirdRowSlots[1][monVertical] = monster[1]
                thirdRowSlots[2][monVertical] = monster[2]

                thirdRowSlots[0][monVertical-1] = ListTest().slotUpper
                thirdRowSlots[1][monVertical-1] = ListTest().slotMiddle
                thirdRowSlots[2][monVertical-1] = ListTest().slotBottom


            if monHorizontal == 'fourthRow': # -- SAME RECIPE AS ABOVE --

                monVertical = monVertical - 1

                fourthRowSlots[0][monVertical] = monster[0]
                fourthRowSlots[1][monVertical] = monster[1]
                fourthRowSlots[2][monVertical] = monster[2]

                fourthRowSlots[0][monVertical+1] = ListTest().slotUpper
                fourthRowSlots[1][monVertical+1] = ListTest().slotMiddle
                fourthRowSlots[2][monVertical+1] = ListTest().slotBottom

        # Check collision between a nearby trap and a nearby monster. If collided, score increased,
        # monster removed from list and monster in store increased
        if firstRowSlots[0][monVertical] == trapUpper:
                            print('\t\t' + 'KILLED MONSTER' + '\t\t')
                            monsters.remove(monster)
                            #trapsList.remove(trap)
                            monsterCount = monsterCount + 1
                            score = score + 1
        
        if secondRowSlots[0][monVertical] == trapUpper:
                            print('\t\t' + 'KILLED MONSTER' + '\t\t')
                            monsters.remove(monster)
                            #trapsList.remove(trap)
                            monsterCount = monsterCount + 1
                            score = score + 1

        if thirdRowSlots[0][monVertical] == trapUpper:
                            print('\t\t' + 'KILLED MONSTER' + '\t\t')
                            monsters.remove(monster)
                            #trapsList.remove(trap)
                            monsterCount = monsterCount + 1
                            score = score + 1

        if fourthRowSlots[0][monVertical] == trapUpper:
                            print('\t\t' + 'KILLED MONSTER' + '\t\t')
                            monsters.remove(monster)
                            #trapsList.remove(trap)
                            monsterCount = monsterCount + 1
                            score = score + 1

        # Spawn trapIcons on the field for the hunter to collect traps 
        if trapIconCount > 0 and command == '':
        
            randomInt = random.randint(0, 7) # Random generated number to determind icon position
            trapIcon = [trapIconUpper, trapIconMiddle, trapIconBottom] # Add icon to trapIconList 
            trapIcons.append(trapIcon)
       
            for icon in trapIcons: # For each 'icon'-element in list
                    # Spawn trapicon at position depending on the random value generated
                    if randomInt == 0:
                        
                        trapIconHorizontal = 'firstRow'
                        trapIconVertical = 0

                        firstRowSlots[0][trapIconVertical] = icon[0]
                        firstRowSlots[1][trapIconVertical] = icon[1]
                        firstRowSlots[2][trapIconVertical] = icon[2]

                    if randomInt == 1:
                        
                        trapIconHorizontal = 'firstRow'
                        trapIconVertical = 4

                        firstRowSlots[0][trapIconVertical] = icon[0]
                        firstRowSlots[1][trapIconVertical] = icon[1]
                        firstRowSlots[2][trapIconVertical] = icon[2]

                    if randomInt == 2:
                        
                        trapIconHorizontal = 'fourthRow'
                        trapIconVertical = 0

                        fourthRowSlots[0][trapIconVertical] = icon[0]
                        fourthRowSlots[1][trapIconVertical] = icon[1]
                        fourthRowSlots[2][trapIconVertical] = icon[2]

                    if randomInt == 3:
                        
                        trapIconHorizontal = 'fourthRow'
                        trapIconVertical = 4

                        fourthRowSlots[0][trapIconVertical] = icon[0]
                        fourthRowSlots[1][trapIconVertical] = icon[1]
                        fourthRowSlots[2][trapIconVertical] = icon[2]
                    
                    if randomInt == 4:
                        
                        trapIconHorizontal = 'secondRow'
                        trapIconVertical = 0

                        secondRowSlots[0][trapIconVertical] = icon[0]
                        secondRowSlots[1][trapIconVertical] = icon[1]
                        secondRowSlots[2][trapIconVertical] = icon[2]

                    if randomInt == 5:
                        
                        trapIconHorizontal = 'secondRow'
                        trapIconVertical = 4

                        secondRowSlots[0][trapIconVertical] = icon[0]
                        secondRowSlots[1][trapIconVertical] = icon[1]
                        secondRowSlots[2][trapIconVertical] = icon[2]
                    
                    if randomInt == 6:
                        
                        trapIconHorizontal = 'thirdRow'
                        trapIconVertical = 0

                        thirdRowSlots[0][trapIconVertical] = icon[0]
                        thirdRowSlots[1][trapIconVertical] = icon[1]
                        thirdRowSlots[2][trapIconVertical] = icon[2]

                    if randomInt == 7:
                        
                        trapIconHorizontal = 'thirdRow'
                        trapIconVertical = 4

                        thirdRowSlots[0][trapIconVertical] = icon[0]
                        thirdRowSlots[1][trapIconVertical] = icon[1]
                        thirdRowSlots[2][trapIconVertical] = icon[2]

            trapIconCount = trapIconCount - 1 # After spawn, decrease trap icons in store
        # Check collision bewteen the hunter and a nearby trapIcon. If collided increase amount of traps in store
        # and increase trapicons in store
        if firstRowSlots[0][trapIconVertical] == firstRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)

        if firstRowSlots[0][trapIconVertical] == firstRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)

        if secondRowSlots[0][trapIconVertical] == secondRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)
                            
        if secondRowSlots[0][trapIconVertical] == secondRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)
                            
        if thirdRowSlots[0][trapIconVertical] == thirdRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)

        if thirdRowSlots[0][trapIconVertical] == thirdRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)                            

        if fourthRowSlots[0][trapIconVertical] == fourthRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)

        if fourthRowSlots[0][trapIconVertical] == fourthRowSlots[0][vertical] and horizontal == trapIconHorizontal:
                            traps = traps + 1
                            trapIconCount = trapIconCount + 1
                            #trapIcons.remove(trapIcon)
playerInput() # Run the player inout method