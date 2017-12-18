import Edge

class Node (object):
    #fields
    #####
    #I think this will point to the adjacent Nodes or this object itself
    #so if someone tries to go in a direction with a wall, it will just send it
    #back here
    #####
    #other option is an edge class:
    #t/f for wall
    #fields for both nodes
    #if we do generation that involves walls, will be easy,
    #gen with neighbors slightly harder, but still easy
    #traversal, a little tricier
    #note: can set both nodes to be the same if on the edge
    #####
    id = ""
    #location
    xCord = 0
    yCord = 0
    #edges
    North = None
    South = None
    East = None
    West = None
    #maze generation
    Visited = False #track if this has been visited for maze gen algorithem

    WallChar =       '█'
    NodeChar =       '░'
    NorthSouthChar = '↕'
    EastWestChar =   '↔'
    PlayerChar =     '☺'
    ExitChar =       'X'


    
    #constructor
    def __init__(self,x,y):
        import Edge
        self.xCord = x
        self.yCord = y
        self.id = id(self)
        self.Visited=False

    def __eq__ (self,other):
        if not isinstance(other,Node):
            return (False)
        
        if self.id == other.id:
            #print("comparing "+str(self.xCord)+","+str(self.yCord)+" to "+str(other.xCord)+","+str(other.yCord))
            return(True)
        else:
            return(False)

    def __str__(self):
        #I'm realizing this is terrible code, note to self, become better at codes, try morse code!
        northTxt = "null"
        southTxt = "null"
        eastTxt = "null"
        westTxt = "null"
        if (self.North is not None):
            northTxt = self.North.isWallTxt()
        if (self.South is not None):
            southTxt = self.South.isWallTxt()
        if (self.East is not None):
            eastTxt = self.East.isWallTxt()
        if (self.West is not None):
            westTxt = self.West.isWallTxt()
        return("X: "+str(self.xCord)+" Y: "+str(self.yCord)+" North: "+northTxt+" South: "+southTxt+" East: "+eastTxt+" West: "+westTxt)


        
    #other methods
    def getAdjacentNodes(self):
        adjacencyList = []
        if (not self.North.Complete or not self.South.Complete or not self.East.Complete or not self.West.Complete):
            print("Error, tried to get adjacency on tile "+x+","+y+" but there was a unintialized edge")
            return []
        else:
            if (self.North.Node2 is not None) and (self.North.Node2 != self):
                adjacencyList.append(self.North.Node2)
            if (self.South.Node1 is not None) and (self.South.Node12 != self):
                adjacencyList.append(self.South.Node1)
            if (self.East.Node2 is not None) and (self.East.Node2 != self):
                adjacencyList.append(self.East.Node2)
            if (self.West.Node2 is not None) and (self.West.Node2 != self):
                adjacencyList.append(self.West.Node2)
##            adjacencyList.append(self.North.Node2)
##            adjacencyList.append(self.South.Node1)
##            adjacencyList.append(self.East.Node2)
##            adjacencyList.append(self.West.Node2)
            return (adjacencyList)


    #check if a direction is a wall
    def isWall(self, direction):
        if (not direction.islower()):
            direction = direction.lower()
        if direction == north:
            return North.Wall
        elif direction == south:
            return South.Wall
        elif direction == east:
            return East.Wall
        elif direction == west:
            return West.Wall
        else:
            print("Error: invalid direction passed to isWall in Node.py")
            return True


    def Draw(self):
        #first row
        picture = WallChar+WallChar+WallChar+WallChar+WallChar+"\n"
        #second row
        picture =+ WallChar+WallChar
        #is top a wall?
        if (self.North.isWall()):
            picture += WallChar
        else:
            picture += NorthSouthChar
        picture =+ WallChar+WallChar+"\n"
        #middle row
        picture += WallChar
        #is west a wall?
        if (self.West.isWall()):
            picture += WallChar
        else:
            picture += EastWestChar
        picture += NodeChar
        #is east a wall?
        if (self.West.isWall()):
            picture += WallChar
        else:
            picture += EastWestChar
        picture += WallChar+"\n"
        #second to last row
        picture =+ WallChar+WallChar
        #is top a wall?
        if (self.South.isWall()):
            picture += WallChar
        else:
            picture += NorthSouthChar
        picture =+ WallChar+WallChar+"\n"
        #bottom row
        picture += WallChar+WallChar+WallChar+WallChar+WallChar
        
        #print the picture
        print(picture)
        #return the picture incase it's needed
        return picture
    
