import discord
import asyncio
import logging
import random


#characters █ '░' ↕ ↔  ☺ 
#◦  #altcode 2007 :stop_button: :pause_button: :black_large_square: :white_large_square: 
#############################################################################################################################
#Set up the maze portion of the bot, skip this if you want to get to the discord half
#
class tile (object):
    id = ""
    xCord = 0
    yCord = 0
    #false means wall true means passable
    north =  False
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
                return("██")
            else:
                return("↕█")
        elif  (direction.lower() == "south"):
            if (self.south == False):
                return("██")
            else:
                return("↕█")
        elif  (direction.lower() == "east"):
            if (self.east == False):
                return("█")
            else:
                return("↔")
        elif  (direction.lower() == "west"):
            if (self.west == False):
                return("█")
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

########################MAZE#########################

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
        #print(self.grid)
        self.makeGridWalls()
        self.newGoal()
        self.newPlayerPosition()
        self.victory = False
        self.id = id(self)

    #draws the maze,
    #if you're trying to change a character, you also need to look at the tile object and change that
    #one other thing, if the maze would be past the 2k discord character limit, this wont fully work,
    #so you could try limiting the valid sizes, or send the maze in multiple messages,
    #probably by spliting the string and sending each individual one as its own message,
    #just rember the ``` s to keep it looking like a code block
    #difficult because I dont call the ?PrintMaze command in other commands, instead a message that is the
    #maze converted to a string, so you'd have to find all of those and change them in the discord commands
    def __str__(self):
        string = "^NORTH^\n```"
        for y in range((self.size - 1),-1,-1):
            #for exery x cord
            string += "█"
            for x in self.grid:
                toBeJoined = x[y].stringWallPicture("north")
                string += toBeJoined
        
            #new line
            string += "\n█"
            
            for x in self.grid:
                if self.playerPosition is x[y]:
                    toBeJoined = "☺"
                elif self.goal is x[y]:
                    toBeJoined = "X"
                else:
                    toBeJoined = "░"
                    
                toBeJoined += x[y].stringWallPicture("east")
                string += toBeJoined
                
            #new Line
            string += "\n"
            
        for i in range(self.size):
            string+= "██"

        string+= "█```"
        return(string)

    # = only if its the same object, not same configuration
    def __eq__(self, other):
        try:
            if self.id == other.id:
                return(True)
        except(AttributeError):
            return(False)
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
            if not possiblePlayerPosition is self.goal:
                self.playerPosition = possiblePlayerPosition
                newplayerposition = True


#works, I think
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
        

#Doesnt work, wont visit all tiles
#while fixing, id recommand uncommentint the print statements,
#be warrneed though, it will take a long time with them all uncommented,
#so use small maze sizes untill your ready to comment them out and test with a big maze
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
            #print(str(len(listInMaze))+" of "+str(self.size**2))
            #print(currentpoint.stringWallDesc())
            
            
            #looped part, intitalize the info about current point
            currentx = currentpoint.xCord
            currenty = currentpoint.yCord

            #print(currentpoint)
            #print(currentx,currenty) 
            
            #chose a direction to go
            #0 is north. 1 is south. 2 is east 3 is west
            direction = random.randrange(4)
           # print(direction)

            #resets counter
            connectionCounter = 0

            if (direction == 0) and (currenty < (self.size - 1)):
                #print("Valid Direction")
                if any(self.grid[currentx][(currenty+1)].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    #print("One in list")
                    if any(self.grid[currentx][(currenty+1)].id == point.id for point in listInMaze) and (any(currentpoint.id == point.id for point in listInMaze)):
                        #print("Both in List")
                              
                        if (self.grid[currentx][(currenty+1)].north):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].south):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].east):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty+1)].west):
                            connectionCounter += 1

                        #print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3) and (currentpoint.north == False):
                            currentpoint.north = True
                            self.grid[currentx][(currenty+1)].south = True
                            currentpoint = self.grid[currentx][(currenty+1)]
                            #print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[currentx][(currenty+1)]
                            #print("Leaving the Walls alone and moving to "+str(currentpoint))
                            
                        
                    elif (currentpoint.north == False):
                        currentpoint.north = True
                        self.grid[currentx][(currenty+1)].south = True
                        listInMaze.append( self.grid[currentx][(currenty+1)])
                        currentpoint = self.grid[currentx][(currenty+1)]
                        #print("Deleting a wall and moving to "+str(currentpoint))
                        
                    else:
                        currentpoint = self.grid[currentx][(currenty+1)]
                        #print("Leaving the Walls alone and moving to "+str(currentpoint)) 
##                else:
##                    currentpoint = random.choice(listInMaze)
##                    print("Chosing a Random Point"+str(currentpoint))

    
            elif (direction == 1) and( currenty > 0):
                #print("Valid Direction")
                if any(self.grid[currentx][(currenty-1)].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    #print("One in list")
                    if any(self.grid[currentx][(currenty-1)].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        currentpoint = self.grid[currentx][(currenty-1)]
                        #print("Both in List")
                        if (self.grid[currentx][(currenty-1)].north):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].south):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].east):
                            connectionCounter += 1
                        if (self.grid[currentx][(currenty-1)].west):
                            connectionCounter += 1

                        #print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 4) and (currentpoint.south == False):
                            currentpoint.south = True
                            self.grid[currentx][(currenty-1)].north = True
                            currentpoint = self.grid[currentx][(currenty-1)]
                            #print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[currentx][(currenty-1)]
                            #print("Leaving the Walls alone and moving to "+str(currentpoint))
                        
                    elif (currentpoint.south == False):
                        currentpoint.south = True
                        self.grid[currentx][(currenty-1)].north = True
                        listInMaze.append( self.grid[currentx][(currenty-1)])
                        currentpoint = self.grid[currentx][(currenty-1)]
                        #print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[currentx][(currenty-1)]
                        #print("Leaving the Walls alone and moving to "+str(currentpoint))
##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            elif direction == 2 and currentx < (self.size -1):
                #print("Valid Direction")
                if any(self.grid[(currentx+1)][currenty].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    #print("One in list")
                    if any(self.grid[(currentx+1)][currenty].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        #print("Both in List")
                        if (self.grid[(currentx+1)][currenty].north):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].south):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].east):
                            connectionCounter += 1
                        if (self.grid[(currentx+1)][currenty].west):
                            connectionCounter += 1

                        #print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3) and (currentpoint.east == False):
                            currentpoint.east = True
                            self.grid[(currentx+1)][currenty].west = True
                            currentpoint = self.grid[(currentx+1)][currenty]
                            #print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[(currentx+1)][currenty]
                            #print("Leaving the Walls alone and moving to "+str(currentpoint))
                            
                    elif (currentpoint.east == False):
                        currentpoint.east = True
                        self.grid[(currentx+1)][currenty].west = True
                        listInMaze.append(self.grid[(currentx+1)][currenty])
                        currentpoint = self.grid[(currentx+1)][currenty]
                        #print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[(currentx+1)][currenty]
                        #print("Leaving the Walls alone and moving to "+str(currentpoint))
##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            elif (direction == 3) and (currentx > (0)):
                #print("Valid Direction")
                if any(self.grid[(currentx-1)][currenty].id == point.id for point in listInMaze) or any(currentpoint.id == point.id for point in listInMaze):
                    #print("One in list")
                    if any(self.grid[(currentx-1)][currenty].id == point.id for point in listInMaze) and any(currentpoint.id == point.id for point in listInMaze):
                        #print("Both in List")
                        if (self.grid[(currentx-1)][currenty].north):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].south):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].east):
                            connectionCounter += 1
                        if (self.grid[(currentx-1)][currenty].west):
                            connectionCounter += 1

                        #print(connectionCounter, " Connections")

                        # not entirley open but 
                        if (connectionCounter < 3 )and (currentpoint.west == False):
                            currentpoint.west = True
                            self.grid[(currentx-1)][currenty].east = True
                            currentpoint = self.grid[(currentx-1)][currenty]
                            #print("Deleting a wall and moving to "+str(currentpoint))
                        else:
                            currentpoint = self.grid[(currentx-1)][currenty]
                            #print("Leaving the Walls alone and moving to "+str(currentpoint))

                    elif (currentpoint.west == False):
                        currentpoint.west = True
                        self.grid[(currentx-1)][currenty].east = True
                        listInMaze.append(self.grid[(currentx-1)][currenty])
                        currentpoint = self.grid[(currentx-1)][currenty]
                        #print("Deleting a wall and moving to "+str(currentpoint))

                    else:
                        currentpoint = self.grid[(currentx-1)][currenty]
                        #print("Leaving the Walls alone and moving to "+str(currentpoint))

##                else:
##                    currentpoint = random.choice(listOfTiles)
##                    print("Chosing a Random Point"+str(currentpoint))

            #else:
                #currentpoint = random.choice(listInMaze)
                #print("Final Else activated")

            #print("-----------New Time Through ----------")


        
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
        self.newGoal()
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

        if self.playerPosition == self.goal:
            self.victory = True

        #returns a bool representing if the move was valid and therefore made or ignored
        return(validMove)

#
#End Maze Setup
#############################################################################################################################

#############################################################################################################################
#Start Discord Bot
#
logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    #keeps track of the servers and their mazes
    global ServerDict
    ServerDict = {}

    #intializes the server dictionary
    for server in client.servers:
        #channelDict[item.name] = item
        #print(item)
        ServerDict[(server.name)] = [None, None]
            
        for channel in server.channels:
            if channel.name == "the_maze" or channel.name == "The_Maze":
                ServerDict[(server.name)] = [channel,None]
        

@client.event
async def on_message(message):   
    #these should be nessicary for the maze to function, + make the code look nicer
    username = message.author.name
    channelName = message.channel.name
    serverId = message.channel.server.id
    currentserver = message.channel.server
    currentservername = message.channel.server.name
    themaze = ServerDict[currentservername][0]    
    themazeitem = ServerDict[currentservername][1]
   
    #just some extra print statements to help when writting commands
    print (message.content)
    print (type(message.content))
    print (message.author)
    #more useful info to keep track of the dictonary
    print("server: ",currentservername, "Type: ", type(serverId))
    print("Server Dictonary: ",ServerDict)

 
   ###---COMMANDS---###
   #Gennerally mine start with a ? and use capitol letters 
    if message.content.startswith('?test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        
    elif message.content.startswith('?sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

#incomplete, doesnt work
    #shut down - shuts maze bot down, currently not working, dont know how to make it work :/
    elif message.content.startswith('?MazeBotend'):
        await client.send_message(message.channel, 'Maze bot is shutting down.')
        client.logout()
        client.close()
        #maybe break? idk

#complete, fails, need to add the new channel to the dictionary properly
    #setup - set up maze,creating the text channel, and adding the server to the dictonary if it isnt allready, all and gives the basic commands
    elif message.content.startswith('?SetUp'):
        await client.send_message(message.channel, 'Okay. I, Mazebot, will set up my text channel')

        if themaze is None:
            await client.create_channel(message.server, 'the_maze', type=discord.ChannelType.text)
            print("the attempted server id is ", currentservername)


            for item in message.server.channels:
                if item.name == "the_maze":
                    ServerDict[currentservername] = [item, None]
                    themaze = item
                    print("succsesfully found the maze channel. the dictionary now shows the following for this channel", ServerDict[currentservername])

            themaze.changetopic("WELCOME TO THE MAZE! \nHere we shall begin exploring the wonderfull world of mazes!\nIf you haven't seen me before type ?Help for a list of commands\n To make a new maze type ?NewMaze")        
                    
        else:
            await client.send_message(message.channel, " Umm, I think you've allready run setup because there allready is a maze channel")
       
        await client.send_message(themaze, "WELCOME TO THE MAZE! \nHere we shall begin exploring the wonderfull world of mazes!\nIf you haven't seen me before type ?Help for a list of commands\n To make a new maze type ?NewMaze")

#incomplete/out of date, works
#the map key needs updating, possibly more
    #help - send user the commands
    elif message.content.startswith('?Help'):
        await client.send_message(message.channel, """Here are the commands:
Commands that work anywhere:
?Help - this command, lists all the commands.
?Info - info about Mazebot including author, verson, and more
?SetUp - creates Mazebot's channel so it doesn't clutter the chats.
- - - - - - - - - - - - - - - - - - - - - - - - - -\n
The rest of the commands only work in the_maze channel created by ?SetUp. Note you should only have to use ?Setup the first time you run Mazebot, afterthat on startup it should be able to find the_maze channel again
?NewMaze - Creates an entirly new maze, must be run before ?NewGame will function.
?NewGame - Restarts on the current maze, only succseads if you've allready run ?NewMaze at somepoint
?Move ("north", "south", "east", or "west") - Attempts to move in the direction given, will run into problems if you leave a space after your direction, sorry, directions aren't case sensitive.
?DrawMaze - "draws" the current maze, X is a room H and : mean passable | and - mean unpassable. ! is the goal/exit and O is your current location, each room is ~ a 3 by 3 charicter area
?MapKey - sends what I just told you (the key for ?DrawMaze's maps
?CurrentLocation - says your current location in the maze as a cordnit point, if you're confused, 0,0 is the bottom left and (size - 1, size - 1) is the top right.
?DeleteMazeBot - Makes Mazebot leave the server, and mazebot forgets you ever existed
- - - - - - - - - - - - - - - - - - - - - - - - - -\n
Indirect Commands, eg commands you cant call directly:
?Size - Used when making a new maze expects exactly "?Size " then numbers like "4" that are >1 and not written out, Additionally this will also fail if you left a space at the end  of your message
""")

#probably outdate, tested and works
    #info about bot, its "framework", VERSON/DATE, how to !help and author
    elif message.content.startswith('?Info'):
        await client.send_message(message.channel, "About Maze Bot: Maze bot is a bot to let you generate and solve mazes. Most of the maze commands only work and send to the maze channel so it's important to run ?SetUp when first adding Mazebot to a server")
        await client.send_message(message.channel, "Use ?Help for a full list of commands. Commands start with ? and the words start with a capitol letter, and anyother words in them should also be capitolized.")
        await client.send_message(message.channel, "I, Daniel Peterson made Mazebot for fun and to practice my python since I'm probbably going to be a cs major, and this was a lot of fun. If you're looking throgh the code and i did something in an odd way, that's probbably because I'm still learning.")
        await client.send_message(message.channel, "I used this https://github.com/Rapptz/discord.py verson of the api and python to make Mazebot.\nCurrent Verson:1.0(hopefully) Completed March 2017 unless I forgot to update this part")

#complete, works
    #restarts the current maze 
    elif message.content.startswith('?Restart') and message.channel is themaze:
        await client.send_message(themaze, "Okay lets start again.")
            
        if (themazeitem != None):
            #the maze exists, so dont need to make a new one
            await client.send_message(themaze, "Keeping the Current Layout and resetting your location")

            themazeitem.restartCurrentMaze()

            #tell the player about the maze
            await client.send_message(themaze, str(themazeitem))
            await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
            await client.send_message(themaze, "The Exit is at: "+str(themazeitem.goal))
        else:
            #no maze item so cant do anything in this command
            await client.send_message(themaze, ":thinking: You haven't made a maze yet, type ?NewMaze to make one")

        
    
#complete, works, I think
    #generates a new maze for the player
    elif message.content.startswith('?NewMaze') and  message.channel is themaze :
        await client.send_message(themaze, "Okay you want a new maze then?")
        await client.send_message(themaze, "Let's get cooking, how big do you want it to be? Use ?Size #")

        #var to makesure we correctly get a new size
        #if you want to limit the size a user can input for  a maze, it would be done here
        findsize = True
        invalidsize = True
        while invalidsize:
            while findsize:
                #wait for the ?Size command
                msg = await client.wait_for_message(author=message.author, channel=themaze, check=message.content.startswith('?Size '))

                mazeSize = msg.content[6:]
                print("Maze Size :", mazeSize)

                #input sanity check
                try:
                    mazeSize = int(mazeSize)
                except:
                    await client.send_message(themaze, "Something is borked, :confused: try '?Size #' again, dont add any extra spaces and use the number keys")
                    findsize = True
                else:    
                    findsize = False

            #size value checks        
            if mazeSize > 1:
                invalidsize = False
            else:
                invalidsize = True
                await client.send_message(themaze, ":point_up:  Mazes must be of Size 2 or greater, sorry :neutral_face:")
            
        #dev test print
        print(mazeSize)

        #creates a new maze if there is none for the server, otherwise just gens a new maze using the pre-existing object
        if (themazeitem is None):
            client.send_typing(message.server)
            ServerDict[currentservername][1] = maze(mazeSize)
            themazeitem = ServerDict[currentservername][1]
        else:
            client.send_typing(message.server)
            themazeitem.newMaze(mazeSize)
        
        await client.send_message(themaze, str(themazeitem))
        await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
        await client.send_message(themaze, "The Exit is at: "+str(themazeitem.goal))

#complete, works,tested    *accept when commands are being spammed, but we have bigger problems at that point, such as moving to nonexistant tiles and through walls,
#so im not dealing with input spam
    #direction (?Move (north south east or west))
    elif message.content.startswith('?Move ') and  message.channel is themaze:
        if (themazeitem != None):
            #there is a maze so
            direction = message.content[6:].lower()

            #try and move in the given direction
            if direction == "north":
                #Try to move north
                didwemove = themazeitem.move(direction)

                if didwemove:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":white_check_mark: Successfully moved north. :white_check_mark: Type ?DrawMaze to see an updated map")
                    await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)
                else:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":octagonal_sign: Failed to Move North because of a Wall. :octagonal_sign: Type ?DrawMaze to see the map")
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)                   
                
            elif direction == "south":
                #try to move south
                didwemove = themazeitem.move(direction)

                if didwemove:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":white_check_mark: Successfully moved south. :white_check_mark: Type ?DrawMaze to see an updated map")
                    await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)
                else:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":octagonal_sign: Failed to Move south because of a Wall. :octagonal_sign: Type ?DrawMaze to see the map")
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)                   

            elif direction == "east":
                #try to move south
                didwemove = themazeitem.move(direction)

                if didwemove:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":white_check_mark: Successfully moved east. :white_check_mark: Type ?DrawMaze to see an updated map")
                    await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)
                else:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":octagonal_sign: Failed to Move east because of a Wall. :octagonal_sign: Type ?DrawMaze to see the map")
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)                   
    
            elif direction == "west":
                #try to move south
                didwemove = themazeitem.move(direction)

                if didwemove:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":white_check_mark: Successfully moved west. :white_check_mark: Type ?DrawMaze to see an updated map")
                    await client.send_message(themaze, "You are at: "+str(themazeitem.playerPosition))
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)
                else:
                    currentRoom = themazeitem.playerPosition.stringWallDesc()
                    await client.send_message(themaze, ":octagonal_sign: Failed to Move west because of a Wall. :octagonal_sign: Type ?DrawMaze to see the map")
                    await client.send_message(themaze, "The current room is as follows; "+currentRoom)                   
                
            else:
                #Something about the input was wrong
                await client.send_message(themaze, "I think you had an extra space at the end, this command cant handle something like '?Move North ', instead try '?Move North'.")
            
            if themazeitem.victory:
                await client.send_message(themaze, "You won!!:first_place: You may keep exploring the maze, or try it again with ?Restart or make a ?NewMaze")           
            
        else:
            #no maze item so cant do anything in this command
            await client.send_message(themaze, ":thinking: You haven't made a maze yet, type ?NewMaze to make one")


#complete, works/tested
    #draw maze ?DrawMaze
    elif message.content.startswith('?DrawMaze') and  message.channel is themaze:
        if (themazeitem != None):
            await client.send_message(themaze, str(themazeitem))

        else:
            #no maze item so cant do anything in this command
            await client.send_message(themaze, ":thinking: You haven't made a maze yet, type ?NewMaze to make one")

#outdated, works/tested
    #map key
    elif  message.content.startswith('?MapKey') and  message.channel is themaze:
    #send a message explaining the map"
        await client.send_message(themaze, """X is a room |H| and : mean passable | and - mean unpassable. ! is the goal/exit and O is your current location. Every row in the map is either the path to the north/south or the path east/west
Meaning that if the map looks like
 walls and space between y=1 and y = 2  |---|
 walls and rooms at y = 1             1 |O:!|
 walls and space between y=0 and y = 1  |H|-|
 walls and rooms at y = 0             0 |X:X|
 walls and space between y=0 and y = -1 |---|
                                         0 1
So the player is the O at (0,1) to the players east is the ! representing the goal at (1,1) there's no wall to the sosuth of the player but there is to the south of the goal.
bassicly this maze is like a sideways U in terms of where the player can go.""")
               

#completed, works/tested
    #current location ?CurrentLocation says players location
    elif message.content.startswith('?CurrentLocation') and  message.channel is themaze:
        if (themazeitem != None):
            await client.send_message(themaze, "You are currently at: "+str(themazeitem.playerPosition))
        else:
            #no maze item so cant do anything in this command
            await client.send_message(themaze, ":thinking: You haven't made a maze yet, type ?NewMaze to make one")

#completed, untested, doesnt work if maze bot doesnt have chat premisson at least
    #leave server ?DeleteMazeBot
    elif message.content.startswith('?DeleteMazeBot'):
    #delete roll as well first
        await client.send_message(message.channel, "Okay, bye forever, don't forget to delete my role if that didn't happen")       
        await client.leave_server(currentserver)
        del ServerDict[currentserver]
        
#
#End Discord Bot
#############################################################################################################################
        

     
#############################################################################################################################
#Start Main Program
#

#web hook to redirect to adding the bot to a server
#https://discordapp.com/api/oauth2/authorize?client_id=286987637791784960&scope=webhook.incoming&redirect_uri=https%3A%2F%2Fnicememe.website&response_type=code
#https://discordapp.com/oauth2/authorize?client_id= 286987637791784960&scope=bot&permissions=603999344
#https://discordapp.com/api/oauth2/Mjg2OTg3NjM3NzkxNzg0OTYw.C6OQBw.Evz1GDuwOP3rQ8ldQ9cJ7jT5ad8

#&scope=bot&permissions=603999344

#NOTE TO SELF CHANGE &PREMISSIONS=####### TO SOMETHING THAT ALSO ALOWS SERVER MANAGING!
#print a message with a url to add the bot incase someone hasnt run the bot before
print(""" If this is the first time running the bot please copy and paste the following URL into a browser:
https://discordapp.com/api/oauth2/authorize?client_id=286987637791784960&scope=bot&permissions=603999344
Then Once you added Mazebot to you're server type ?SetUp to get started and/or ?Info to find out about Mazebot 
""")

#log on, requrires string 
client.run("[bot token goes here]")

input("Press enter to quit Mazebot")

#
#End Main
##############################################################################################################

#Refrence Code from the API I haven't deleted yet

##        Asking for a follow-up question:
##
##        .. code-block:: python
##            :emphasize-lines: 6
##
##            @client.event
##            async def on_message(message):
##                if message.content.startswith('$start'):
##                    await client.send_message(message.channel, 'Type $stop 4 times.')
##                    for i in range(4):
##                        msawait client.wait_for_message(author=message.author, content='$stop')
##                        fmt = '{} left to go...'
##                        await client.send_message(message.channel, fmt.format(3 - i))
##
##                    await client.send_message(message.channel, 'Good job!')
##        Parameters
##        -----------
##        timeout : float
##            The number of seconds to wait before returning ``None``.
##        author : :class:`Member` or :class:`User`
##            The author the message must be from.
##        channel : :class:`Channel` or :class:`PrivateChannel` or :class:`Object`
##            The channel the message must be from.
##        content : str
##            The exact content the message must have.
##        check : function
##            A predicate for other complicated checks. The predicate must take
##            a :class:`Message` as its only parameter.
##
##        Returns
##        --------
##        :class:`Message`
##            The message that you requested for.
##        """
