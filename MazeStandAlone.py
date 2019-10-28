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
    size = 0
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
        

#probbably works        
    def makeGridWalls(self):
        """ follow the Prim Algorithum and make a valid maze
        note to self use the self.grid to accses grid"""
        #chose a starting point
        #startingpoint = self.randompoint()
        #unused

        listOfTiles = []
        for x in range(self.size):
            for y in self.grid[x]:
                listOfTiles.append(y)       

        currentpoint = self.randomPoint()

        listInMaze = [currentpoint]

        connectionCounter = 0

        totalinvaliddirections = 0

        while len(listInMaze) < self.size ** 2:
            print(str(len(listInMaze))+" of "+str(self.size**2))
            print(currentpoint.stringWallDesc())
            
            
            #looped part, intitalize the info about current point
            currentx = currentpoint.xCord
            currenty = currentpoint.yCord

            print(currentpoint)
            print(currentx,currenty) 
            
            #chose a direction to go
            #0 is north. 1 is south. 2 is east 3 is west
            direction = random.randrange(4)
            print(direction)

            #resets counter
            connectionCounter = 0

            if (direction == 0) and (currenty < (self.size - 1)):
                print("Valid Direction")
                if any(self.grid[currentx][(currenty+1)].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    print("One in list")
                    if any(self.grid[currentx][(currenty+1)].id == point.id for point in listInMaze) and (any(currentpoint.id == point.id for point in listInMaze)):
                        print("Both in List")
                              
                        if (self.grid[currentx][(currenty+1)].north):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].south):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].east):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].west):
                            connectionCounter += 1

                        print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3) and (currentpoint.north == False):
                            currentpoint.north = True
                            self.grid[currentx][(currenty+1)].south = True
                            currentpoint = self.grid[currentx][(currenty+1)]
                            print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[currentx][(currenty+1)]
                            print("Leaving the Walls alone and moving to "+str(currentpoint))
                            
                        
                    elif (currentpoint.north == False):
                        currentpoint.north = True
                        self.grid[currentx][(currenty+1)].south = True
                        listInMaze.append( self.grid[currentx][(currenty+1)])
                        currentpoint = self.grid[currentx][(currenty+1)]
                        print("Deleting a wall and moving to "+str(currentpoint))
                        
                    else:
                        currentpoint = self.grid[currentx][(currenty+1)]
                        print("Leaving the Walls alone and moving to "+str(currentpoint)) 
##                else:
##                    currentpoint = random.choice(listInMaze)
##                    print("Chosing a Random Point"+str(currentpoint))

    
            elif (direction == 1) and( currenty > 0):
                print("Valid Direction")
                if any(self.grid[currentx][(currenty-1)].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    print("One in list")
                    if any(self.grid[currentx][(currenty-1)].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        currentpoint = self.grid[currentx][(currenty-1)]
                        print("Both in List")
                        if (self.grid[currentx][(currenty-1)].north):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].south):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].east):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].west):
                            connectionCounter += 1

                        print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 4) and (currentpoint.south == False):
                            currentpoint.south = True
                            self.grid[currentx][(currenty-1)].north = True
                            currentpoint = self.grid[currentx][(currenty-1)]
                            print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[currentx][(currenty-1)]
                            print("Leaving the Walls alone and moving to "+str(currentpoint))
                        
                    elif (currentpoint.south == False):
                        currentpoint.south = True
                        self.grid[currentx][(currenty-1)].north = True
                        listInMaze.append( self.grid[currentx][(currenty-1)])
                        currentpoint = self.grid[currentx][(currenty-1)]
                        print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[currentx][(currenty-1)]
                        print("Leaving the Walls alone and moving to "+str(currentpoint))
##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            elif direction == 2 and currentx < (self.size -1):
                print("Valid Direction")
                if any(self.grid[(currentx+1)][currenty].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    print("One in list")
                    if any(self.grid[(currentx+1)][currenty].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        print("Both in List")
                        if (self.grid[(currentx+1)][currenty].north):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].south):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].east):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].west):
                            connectionCounter += 1

                        print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3) and (currentpoint.east == False):
                            currentpoint.east = True
                            self.grid[(currentx+1)][currenty].west = True
                            currentpoint = self.grid[(currentx+1)][currenty]
                            print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[(currentx+1)][currenty]
                            print("Leaving the Walls alone and moving to "+str(currentpoint))
                            
                    elif (currentpoint.east == False):
                        currentpoint.east = True
                        self.grid[(currentx+1)][currenty].west = True
                        listInMaze.append(self.grid[(currentx+1)][currenty])
                        currentpoint = self.grid[(currentx+1)][currenty]
                        print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[(currentx+1)][currenty]
                        print("Leaving the Walls alone and moving to "+str(currentpoint))
##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            elif (direction == 3) and (currentx > (0)):
                print("Valid Direction")
                if any(self.grid[(currentx-1)][currenty].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    print("One in list")
                    if any(self.grid[(currentx-1)][currenty].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        print("Both in List")
                        if (self.grid[(currentx-1)][currenty].north):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].south):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].east):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].west):
                            connectionCounter += 1

                        print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3 )and (currentpoint.west == False):
                            currentpoint.west = True
                            self.grid[(currentx-1)][currenty].east = True
                            currentpoint = self.grid[(currentx-1)][currenty]
                            print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[(currentx-1)][currenty]
                            print("Leaving the Walls alone and moving to "+str(currentpoint))

                    elif (currentpoint.west == False):
                        currentpoint.west = True
                        self.grid[(currentx-1)][currenty].east = True
                        listInMaze.append(self.grid[(currentx-1)][currenty])
                        currentpoint = self.grid[(currentx-1)][currenty]
                        print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[(currentx-1)][currenty]
                        print("Leaving the Walls alone and moving to "+str(currentpoint))

##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            else:
                #currentpoint = random.choice(listInMaze)
                print("Final Else activated")

            print("-----------New Time Through ----------")


        
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
            
            


    
    




        
