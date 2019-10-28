#maze creation test


#########
#imports
import random



#######################
#classes
class tile (object):
    id = ""
    xCord = 0
    yCord = 0
    #false means wall true means passable
    north = False
    south = False
    east = False
    west = False

    def __init__(self,x,y):
        """Creates a walless tile for (x,y)."""
        self.xCord = x
        self.yCord = y
        self.id = id(self)


    def __str__(self):
        selfAsString = "("+str(self.xCord)+","+str(self.yCord)+")"
        return selfAsString


    def __eq__(self, other):
        if self.id == other.id:
            return(True)
        else:
            return(False)

    def stringWallPicture(self,direction):
        """str->str, input must be 'north', 'south', 'east' or 'west'.
        """
        if (direction.lower() == "north"):
            if (self.north == False):
                return("--")
            else:
                return("↕|")
        elif  (direction.lower() == "south"):
            if (self.south == False):
                return("--")
            else:
                return("↕|")
        elif  (direction.lower() == "east"):
            if (self.east == False):
                return("|")
            else:
                return("↔")
        elif  (direction.lower() == "west"):
            if (self.west == False):
                return("|")
            else:
                return("↔")
        else:
            return("?")
            
        

    def stringWallDesc(self):
        if self.north == False:
            north = "Wall"
        else:
            north = "Open"

        if self.south == False:
            south = "Wall"
        else:
            south = "Open"

        if self.east == False:
            east = "Wall"
        else:
            east = "Open"

        if self.west == False:
            west = "Wall"
        else:
            west = "Open"
            
        return("North: ",north," South: ",south," East: ",east," West: ", west)

#######################MAZE#########################

class maze (object):
    id =""
    goal = tile(0,0)
    playerPosition = tile(0,0) 
    grid = []
    #mostly for refrence 
    size =  1
    victory = False


    def __init__(self,size):
        """Requires an intiger number for the size of the maze.
        Must Pass a valid number, determin if valid in main."""
        self.size = size
        self.makeBlankGrid(size)
        self.makeGridWalls()
        self.newGoal()
        self.newPlayerPosition()
        self.victory = False
        self.id = id(self)

    #draws the maze    
    def __str__(self):
        string = ""
        for y in range((self.size - 1),-1,-1):
            #for exery x cord
            string += "|"
            for x in self.grid:
                toBeJoined = x[y].stringWallPicture("north")
                string += toBeJoined
        
            #new line
            string += "\n|"
            
            for x in self.grid:
                if self.playerPosition is x[y]:
                    toBeJoined = "O"
                elif self.goal is x[y]:
                    toBeJoined = "!"
                else:
                    toBeJoined = "X"
                    
                toBeJoined += x[y].stringWallPicture("east")
                string += toBeJoined
                
            #new Line
            string += "\n"
            
        for i in range(self.size):
            string+= "--"    
        return(string)

    # = only if its the same object, not same configuration
    def __eq__(self, other):
        if self.id == other.id:
            return(True)
        else:
            return(False)
                
#works I think
    def randomPoint(self):
        """Chose a random point in the maze and return its object."""
        #chose an x cord
        randomX = random.randrange(self.size)
        #skip choosing a y cordnit to this choosing the point
        randomPoint = random.choice(self.grid[randomX])

        #return the point eg its tile object
        return (randomPoint)

#unknown, 
    def newPlayerPosition(self):
        """Chooses a new valid player position."""
        newplayerposition = False
        while not newplayerposition:
            possiblePlayerPosition = self.randomPoint()
            if possiblePlayerPosition is not self.goal:
                self.playerPosition = possiblePlayerPosition
                newplayerposition = True


#unknwon
    def newGoal (self):
        """chose a random point in the maze thats not the goal and make it the goal."""
        self.goal = self.randomPoint()

#works
    def makeBlankGrid (self, size):
        """ int -> void makes a blank grid of size passed in."""
        #make a list of blank lists
        self.grid = [[]for x in range(size)]
        
        for x in range(size):
            #print("Made X column: ",x)
            
            for y in range (size):
                self.grid[x].append(tile(x,y))
                #print("Made y cordnit: ", y)
        
        #print("self grid is ", self.grid)
        
#incomplete untested
#also currently unimplemented
    def adjacent(self,tile):
        """Hopefully returns an itorator or list of all adjacent tiles"""
        adjacentTiles = []
        if tile.xCord < self.size:
            adjacentTiles += self.grid[tile.yCord][tile.xCord +1]
        if tile.yCord < self.size:
            adjacentTiles += self.grid[tile.yCord+1][tile.xCord]
        if tile.xCord > 0:
            adjacentTiles += self.grid[tile.yCord][tile.xCord-1]
        if tile.yCord > 0:
            adjacentTiles += self.grid[tile.yCord-1][tile.xCord]
        return adjacentTiles

        
#probbably works        
    def makeGridWalls(self):
        """ make a valid maze, somehow
        note to self use the self.grid to accses grid"""
        #start = self.randomPoint
        
##        while (len(stack)>0): #while the stack isnt empty
##            #point = most receently added to stack
##            #delete most recently added from stack
##            current = stack.pop()
##            #if ponit is not discovered
##            if not(current in discovered):
##                #add to discovered
##                discovered.append(current)
##                #delete walls
##                
##                #for all adjacent edges?
##                for tile in self.adjacent(current):
##                    #add to stack
##                    stack.append(tile)
        
#unknow
    def newMaze (self, size):
        """generates a new valid square of size size."""
        self.size = size
        self.makeBlankGrid(size)
        self.makeGridWalls()
        self.newGoal()
        self.newPlayerPosition()
        self.victory = False
        
      
        
#unknown
    def restartCurrentMaze (self):
        """sets the player's position to a random point thats not the maze, and maybe reset any win indicator."""
        self.victory = False
        self.newPlayerPosition()

#works
    def move (self, direction):
        """string -> bool 
takes a move and either updates the position and returns true or returns false."""
        direction = direction.lower()
        validMove = False
        if direction == "north" and self.playerPosition.north:
            self.playerPosition = self.grid[self.playerPosition.xCord][(self.playerPosition.yCord +1)]
            validMove = True
            
        elif direction == "south" and self.playerPosition.south:
            self.playerPosition = self.grid[self.playerPosition.xCord][(self.playerPosition.yCord -1)]
            validMove = True

        elif direction == "east" and self.playerPosition.east:
            self.playerPosition = self.grid[(self.playerPosition.xCord + 1)][self.playerPosition.yCord]
            validMove = True

        elif direction == "west" and self.playerPosition.west:
            self.playerPosition = self.grid[(self.playerPosition.xCord - 1)][self.playerPosition.yCord]
            validMove = True

        if self.playerPosition is self.goal:
            self.victory = True

        #returns a bool representing if the move was valid and therefore made or ignored
        return(validMove)
    



##############
#functions
def done():
    """void -> bool."""
    validresponse = False
    while not validresponse:
        response = input("Are you done playing? 'yes' or 'no'")
        if response.lower() == "yes" or response.lower() == "no":
            validresponse = True
        else:
            print("I think you misstyped, try again please.")

    if response == "yes":
        return(True)
    elif response == "no":
        return(False)
    else:
        return(False)
        
        
######################################################################################################
#main
while not done():
    #new game
    validMazeSize = False
    while not validMazeSize:
        validSizeInput = False
        
        while not validSizeInput:
            newmazesize = input("What size would you like the maze to be as a number, using number keys")
            try:
                newmazesize = int(newmazesize)
                validSizeInput = True
            except(ValueError):
                print("Invalid size")

        if newmazesize >= 2:
            validMazeSize = True

    currentMaze = maze(newmazesize)

    while not currentMaze.victory:
        mazeString = str(currentMaze)
        print(mazeString, "this print statement works")
        print("You are currently at: ", currentMaze.playerPosition)
        print(currentMaze.playerPosition.stringWallDesc())
        print("The end of the maze is at: ", currentMaze.goal)
        print("\nWhere would you like to go? type 'north','south','east', or 'west'") 
        move = input()
        success = currentMaze.move(move)
        if success:
            print("Congradulations you moved")
        else:
            print("Sorry, I don't think that was a valid move")
    #maze is beaten
    
##while not done():
##    questionResponse = input("Do you want to make a new maze ('new'), or keep the current one ('old') or if you want to test the new maze function type 'test'").lower()
##    validMazeSize = False
##    while not validMazeSize:
##        validSizeInput = False
##        
##        while not validSizeInput:
##            newmazesize = input("What size would you like the maze to be as a number, using number keys")
##            try:
##                newmazesize = int(newmazesize)
##                validSizeInput = True
##            except(ValueError):
##                print("Invalid size")
##
##        if newmazesize >= 2:
##            validMazeSize = True
##
##        if questionResponse == "new":
##            currentMaze = maze(newmazesize)
##        elif questionResponse == "old":
##            currentMaze.restartCurrentMaze()
##        elif questionResponse == "test":
##            currentMaze.newMaze(newmazesize)
##
##    while not currentMaze.victory:
##        mazeString = str(currentMaze)
##        print(mazeString, "this print statement works")
##        print("You are currently at: ", currentMaze.playerPosition)
##        print(currentMaze.playerPosition.stringWallDesc())
##        print("The end of the maze is at: ", currentMaze.goal)
##        print("\nWhere would you like to go? type 'north','south','east', or 'west'") 
##        move = input()
##        success = currentMaze.move(move)
##        if success:
##            print("Congradulations you moved")
##        else:
##            print("Sorry, I don't think that was a valid move")
##    #maze is beaten
            
            


    
    




        
