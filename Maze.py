import random
import Node
import Edge
import math

#characters █ '░' ↕ ↔  ☺
class Maze (object):
    #fields
    id = ""
    Size = 1
    Grid = []
    Victory = False
    #tile object
    Goal = Node.Node(0,0)
    #tile object
    PlayerPosition = Node.Node(0,0)

    #texture pack
    WallChar =       '█'
    NodeChar =       '░'
    NorthSouthChar = '↕'
    EastWestChar =   '↔'
    PlayerChar =     '☺'
    ExitChar =       'X'
    

    #overrides
    ####################################  
    #constructor
    def __init__(self,size):
        #import Node
        #self.Size = size
        #self.Grid = [size]
        self.id = id(self)
        self.newMaze(size)
        Victort = False
        
        
        
    def __str__(self):
        return ("|Player: "+str(self.PlayerPosition)+" |Goal: "+str(self.Goal)+" |Size = "+str(self.Size))

    def __eq__(self, other):
        if not isinstance(other,Maze):
            return (False)
        if self.id == other.id:
            return(True)
        else:
            return(False)
        

    #####################################
    #other methods

    #so we can gen larger mazes and send discord maps of smaller mazes
    #ideally the main program chooses a size that can be printed on discord
    def subsectionString(self,mapsize,centerX,centerY):
        #figure out stuff about what should be on the map
        #(xLowerBoundL,xUpperBoundL) for every row
        xUpperBound = centerX + math.ceil(mapsize/2) #farthest right point
        xLowerBound = centerX - math.floor(mapsize/2) #farthest left point

        #lower is now staying in bounds
        if (xLowerBound < 0):
            xLowerBound = 0

        #upper is now going to stay in bounds
        if (xUpperBound >= self.Size):
            xUpperBound = self.Size-1
            
        yUpperBound = centerY + math.ceil(mapsize/2) #farthest right point
        yLowerBound = centerY - math.floor(mapsize/2) #farthest left point

        #lower is now staying in bounds
        if (yLowerBound < 0):
            yLowerBound = 0

        #upper is now going to stay in bounds
        if (yUpperBound >= self.Size):
            yUpperBound = self.Size-1

            

        #create map string, "" so it's a string item that I can concatanate to
        mapofmaze = ""
        #north walls/paths of grid
        for y in range(yUpperBound,yLowerBound-1,-1): 
            #reset x to the start of where we're mapping
            x = xLowerBound
            while(x<=xUpperBound):
                #draw the tile's northen side
                mapofmaze += self.northernString(self.Grid[y][x])
                x+=1 #incriment x
            #new line, northen edge done
            mapofmaze += self.WallChar +"\n"

        #east west walls/paths of grid
            x = xLowerBound
            while(x<=xUpperBound):
                #draw the tile, and west connection
                mapofmaze += self.middleString(self.Grid[y][x])
                x+=1
            #draw the east connection, incase it isn't the boarder
            mapofmaze += self.Grid[y][(xUpperBound)].East.stringPictureOfWall()+"\n"

        #draw the southern edge of  the map
        x = xLowerBound
        while(x<=xUpperBound):
            mapofmaze += self.southernString(self.Grid[yLowerBound][x])
            x+=1
        mapofmaze += self.WallChar
            
        #return the map
        return(mapofmaze)


    #longer comments above, sorry
    def entireMazeString(self):
        mapofmaze = ""
        for y in range(self.Size-1,-1,-1):
            print(y)
            #northern walls/paths of grid            
            for x in range(self.Size):
                print(y)
                mapofmaze += self.northernString(self.Grid[y][x])
            mapofmaze += self.WallChar +"\n"
            
            #print(mapofmaze) #dev test print
            
            #east west walls/paths of grid)
            for x in range(self.Size): 
                mapofmaze += self.middleString(self.Grid[y][x])
            mapofmaze += self.Grid[y][(self.Size-1)].East.stringPictureOfWall() +"\n"
            
        #also have to do a special case for the bottom string
        #southern walls/paths of grid
        for x in range(self.Size):
            mapofmaze += self.southernString(self.Grid[0][x])
        mapofmaze += self.WallChar
                                               
        #return the maze
        return  mapofmaze

    #generation with recursive back traacker
    #pop == pop, append == push
    def backTraceGenMazeWalls(self):
        """current Node (node object in the maze), stack)"""
        #stack for backtracing
        stack = []
        
        #create list of unvisited cells
        visitedList = []
        for y in range(self.Size):
            visitedList.extend(self.Grid[y])

        #start from a random point
        currentNode = self.randomPoint()
        currentNode.Visited = True
        visitedList.remove(currentNode)

        #while there are unvisited nodes
        while len(visitedList)>0:
            print("current Node: "+str(currentNode.xCord)+" , "+str(currentNode.yCord))

            #initalize unvisited neighbors list
            unvisitedNeighborList = []
            #get adjacent cells
            rawUnvisitedNeighborList = currentNode.getAdjacentNodes()          
            #populate stack with adjacent nodes
            for node in rawUnvisitedNeighborList:
                print("entered for loop")
                if not isinstance(node,Node.Node):
                    #unvisitedNeighborList.remove(node)
                    print("I should probably be throwing an exception, but oh well\n a non node item made it into the neighbor list")
                elif not node.Visited:
                    #unvisitedNeighborList.remove(node)
                    unvisitedNeighborList.append(node)                    

            #if the current cell has any neighbors which have not been visited
            if len(unvisitedNeighborList)>0:
                print(str(unvisitedNeighborList))
                #choose randomly one of the unvisited neighbors
                nextNode = random.choice(unvisitedNeighborList)
                #push current cell onto stack
                stack.append(currentNode)
                #remove wall between current cell and chosen
                if(nextNode.xCord>currentNode.xCord):
                    assert currentNode.West is nextNode.East
                    currentNode.West.Wall = False
                elif(nextNode.xCord<currentNode.xCord):
                    assert currentNode.East is nextNode.West
                    currentNode.East.Wall = False
                elif(nextNode.yCord>currentNode.yCord):
                    assert currentNode.North is nextNode.South
                    currentNode.North.Wall = False
                elif(nextNode.yCord<currentNode.yCord):
                    assert currentNode.South is nextNode.South
                    currentNode.South.Wall = False
                #make the chosen cell current
                currentNode = nextNode
                nextNode = None                
                #mark it as visited
                currentNode.Visited = True
                visitedList.remove(currentNode)
            #else if stack is not empty
            elif len(stack)>0:
                #pop a cell from the stack, make it current
                currentNode = stack.pop()
            else:
                print("current node never updated, something is wrong")
        return

    def makeBlankGrid(self, size):
        self.Size = size
        self.Grid = [[None]*size]*size
        for y in range(size):
            #print("making blank grid at y: "+str(y))
            for x in range(size):
                #print("making tile at x: "+str(x)+" y: "+str(y))
                self.Grid[y][x] = Node.Node(x,y)
                
        #grid of unconnected tiles, now have to make edges
        # # # # work on all north south edges # # # #

        #handle south for all tiles
        for y in range(1,size):
            for x in range(size):
                #create a north south edge
                self.Grid[y][x].South = Edge.Edge(self.Grid[y-1][x],self.Grid[y][x],True)
                #set the northen Node's south
                self.Grid[y-1][x].North = self.Grid[y][x].South

        #make south edge loop on itslef
        for x in range(size):
            currentTile = self.Grid[0][x]
            currentTile.South = Edge.Edge(currentTile,currentTile,True)

        #make north edge loop on itslef
        for x in range(size):
            currentTile = self.Grid[size-1][x]
            currentTile.North = Edge.Edge(currentTile,currentTile,True)

        # # # # all north south edges done # # # #
        # # # # work on all east west edges # # # #

        for y in range(size):
            for x in range(1,size):
                #create a west east edge
                self.Grid[y][x].West = Edge.Edge(self.Grid[y][x-1],self.Grid[y][x],False)
                #set that same edge for the other Node's appropriate Direction
                self.Grid[y][x-1].East = self.Grid[y][x].West
          
        #make estern edge loop back on it'self
        for y in range(size):
            currentTile = self.Grid[y][(size-1)]
            currentTile.East = Edge.Edge(currentTile,currentTile,False)

        for y in range(size):
            currentTile = self.Grid[y][0]
            currentTile.West = Edge.Edge(currentTile,currentTile,False)

        # # # # all east west edges done # # # #
         
        return self.Grid
    

    def newMaze(self,newsize):
        """void->void, does the depth first maze generation on
        the current grid"""
        self.Size = newsize
        self.Grid = self.makeBlankGrid(newsize)
        self.backTraceGenMazeWalls()
        self.newGoal()
        self.newPlayerPosition()
        self.Victory = False
        return

    def restartCurrentMaze(self):
        self.newGoal()
        self.newPlayerPosition()
        self.Victory = False
        return

    def move(self, direction):
        #takes 'north' 'south' 'east' and 'west'
        #make sure direction is lowercase
        if (not direction.islower()):
            direction = direction.lower()
        current = self.PlayerPosition

        if (direction == "north"):
            #going north
            if (current.North.isWall()):
                #can't go this way
                print("Error, there's a wall in the way")
                return False
            else:
                #can go north
                self.PlayerPosition = current.North.Node2
                if (self.PlayerPosition == self.Goal):
                    self.Victory = True
                return True
        elif (direction == "south"):
            #going south
            if (current.South.isWall()):
                #can't go this way
                print("Error, there's a wall in the way")
                return False
            else:
                #can go south
                self.PlayerPosition = current.South.Node1
                if (self.PlayerPosition == self.Goal):
                    self.Victory = True
                return True
        elif (direction == "east"):
            #going east
            if (current.East.isWall()):
                #can't go this way
                print("Error, there's a wall in the way")
                return False
            else:
                #can go East
                self.PlayerPosition = current.East.Node2
                if (self.PlayerPosition == self.Goal):
                    self.Victory = True
                return True
        elif (direction == "west"):
            #going west
            if (current.West.isWall()):
                #can't go this way
                print("Error, there's a wall in the way")
                return False
            else:
                #can go west
                self.PlayerPosition = current.West.Node1
                if (self.PlayerPosition == self.Goal):
                    self.Victory = True
                return True
        else:
            #error
            print("Error tried to move an improperly formatted direction: "+direction)
            return False
        
    ##################################
    #helpers
    def randomPoint(self):
        randY = random.randrange(self.Size-1)
        return random.choice(self.Grid[randY])


    ####### for maze drawing #######
    #for use with map built in function
    def northernString(self, node):
        print(node) #
        result = ""
        result += self.WallChar
        result += node.North.stringPictureOfWall()
        return result
    
    #for use with map built in function
    def middleString(self, node):
        print(node) #
        result = ""
        result += node.West.stringPictureOfWall()
        #if player or exit, special car
        if(node==self.PlayerPosition):
            result += self.PlayerChar
        elif(node==self.Goal):
            result += self.ExitChar
        else:
            result += self.NodeChar
        return result
    
    #for use with map built in function
    def southernString(self, node):
        print(node) #
        result = ""
        result += self.WallChar
        result += node.South.stringPictureOfWall()
        return result
    #######not for use with maze drawing#######

    #choose a new goal
    def newGoal(self):
        newPositionFount = False
        while(not newPositionFount):
            potentalGoal = self.randomPoint()
            if (potentalGoal is not self.PlayerPosition and potentalGoal is not self.Goal):
                self.Goal = potentalGoal
                newPositionFount = True
                return
            elif (self.Size < 2):
                #incase there's only 1 node
                self.Goal = potentalGoal
                newPositionFount = True
                return

    #choose a new player starting position
    def newPlayerPosition(self):
        newPositionFount = False
        while (not newPositionFount):
            potentalPlayerPos = self.randomPoint()
            if (potentalPlayerPos is not self.Goal and potentalPlayerPos is not self.PlayerPosition):
                self.PlayerPosition = potentalPlayerPos
                newPositionFount = True
                return
            elif (self.Size <2):
                #incase the maze is 1 by 1 node
                self.PlayerPosition = potentalPlayerPos
                newPositionFount = True
                return
     ###################################


#what if we built the maze, then fit that into the grid?
    #big problem with visualizeing it, because wouldne nessisarily be a grid
    #could like idk try to draw it?
            
#prims
#pick a node, add all edges to a list, chose one,
#if one only one of the two has been visited
#then delete the wall (set wall field to false)
#add the unvisted node to the maze list
#add the new node's edges to the wall list


#I like recursive back traceing,
#checking for neighbors might be harder with an edge 
#system, without,would rely on the array
