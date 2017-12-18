class Edge (object):
    #fields
    Complete = True #both nodes initalized
    Wall = True
    Node1 = None #West of edge or South
    Node2 = None #East of edge or North
    id = ""
    NorthSouth = False
    #xxxxx
    #x1E2x
    #xxxxx
    #xx2xx
    #xxExx
    #xx1xx

    #texture pack
    WallChar =       '█'
    NorthSouthChar = '↕'
    EastWestChar =   '↔'
    
                       #west east
                       #south north
    def __init__ (self, node1=None, node2=None, ns=True):
        Node1=node1
        Node2=node2
        Wall = True
        if((node1 is not None) and (node2 is not None)):
            Complete = True
        else:
            Complete = False
        self.id = id(self)
        NorthSouth = ns


    def __eq__(self, other):
        if not isinstance(other,Edge):
            return (False)
        if self.id == other.id:
            return(True)
        else:
            return(False)
        
    #dev test info 
    def __str__(self):
        return (""+self.Node1+" and "+self.Node2)

    #return bool indicating if this is a wall
    def isWall(self):
        return self.Wall

    #say wall or open for Node's dev test info print
    def isWallTxt(self):
        if (self.Wall):
            return ("Wall")
        else:
            return ("Open")


    def stringPictureOfWall(self):
        if(self.Wall):
            return(str(self.WallChar))
        else:
            if (self.NorthSouth):
                return (str(self.NorthSouthChar))
            else:
                return (str(self.EastWestChar))
        



        
