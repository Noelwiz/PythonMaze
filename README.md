# PythonMaze
maze for a pythone maze bot

Note to myself:
okay, create a "maze" object, with properties like size, goal, position ect generate it, store it as a global variable maybe that will alow us to work with this

could require size for the int function, and instead gen it after getting size from the user, via the response

hmm if i do global current maze, what happens when we have multiple servers, will servers using the same bot user share  mazes? can we fix that?

if problem try importing my maze class in the loged on as part of the script,
might also want to use try when importing, would be like "from file name import class name"

maybe a second class of tiles, with a north south east west property as well as a positon? 

https://en.wikipedia.org/wiki/Maze_generation_algorithm 
maze gen
start bot left go to top of row making tiles then new x

check all sides if a side wont exist eg: top edge or left side ect, set it to a wall.

if it allready exists make it match

else rng it

then if a tile would be all walls, change one non permint side (fails with last tile in middle potentally)

order:
-corners
-sides
-middle


could gen then test with a bot, bot must reach every tile, or invalid, if invalid regen

alt: start full, then at point a, chose a random existant cell, delete the connecting walls move on, do this untill all adject cells have been visited, then start at a cell missed and do it again, and again

https://en.wikipedia.org/wiki/Prim%27s_algorithm 
https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim.27s_algorithm 

YO USE A DICTIONARY SO EACH SERVER CAN HAVE ITS OWN MAZE!!!! STORE THE DICTIONARY AS A GLOBAL

Csci chapter 16 stuff is relivent to life
