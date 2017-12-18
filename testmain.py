import Maze

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
    

#######MAIN#######
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

    currentMaze = Maze.Maze(newmazesize)

    while not currentMaze.Victory:
        submap = currentMaze.subsectionString(currentMaze.Size-1,(currentMaze.Size-1)//2,(currentMaze.Size-1)//2)
        print("sub map of maze is :\n"+submap)
        mazeString = currentMaze.entireMazeString()
        print(mazeString +"\n this print statement works")
        print("You are currently at: ")
        print(str(currentMaze.PlayerPosition))
        print("The end of the maze is at: ", str(currentMaze.Goal))
        print("\nWhere would you like to go? type 'north','south','east', or 'west'") 
        move = input()
        success = currentMaze.move(move)
        if success:
            print("Congradulations you moved")
        else:
            print("Sorry, I don't think that was a valid move")
    
