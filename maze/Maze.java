package maze;

import java.util.Random;

public class Maze {
	//id not used, might be fine in java
	public int Size = 1;
	public Tile[][] Grid = null;
	public boolean Solved = false;
	private Tile Exit = null;
	private Tile PlayerPosition = null;
	
	private static Random RandNum= new Random();
	
	
	//constuctor
	public Maze(int size) {
		//generate new maze
		newMaze(size);		
	}
	
	public String toString() {
		//returns debug info
		return "";
	}
	
	//player commands//
	//public boolean move(String direction){}
	
	//public String drawMap(){}
	
	//public String drawMap(int x, int y, int mapsize){}
	
	//public String drawMap(Tile center, int mapsize){}
	
	//end player commands// *note: starting a new maze is below (newMaze, and Restart)
	
	
	//Starting a maze//
 	private void newMaze(int size){
		//hi
		Size = size;
		makeBlankGrid();
		//backTraceGenMazeWalls();
		newExit();
		newPlayerPosition();
		backTraceGenMaze();
		Solved = false;
	}
	
	public void makeBlankGrid() {
		Grid = new Tile[Size][Size];
		//hook up edges everywhere
		
	}
	
	public void restartCurrent() {
		Solved = false;
		newExit();
		newPlayerPosition();
	}
	
	public void backTraceGenMaze() {
		resetVisited();
		return;
	}
	
	//end starting a maze//
	
	private Tile randomPoint() {
		if(Grid == null) {
			return null;
		}
		
		int y = RandNum.nextInt(Size);
		int x = RandNum.nextInt(Size);
		
		return Grid[y][x];
	}
	
	private void newExit() {
		if (Grid == null) {
			return;
		} else if (Size == 1) {
			Exit = Grid[0][0];
		}
		
		boolean notvalid = true;
		
		while(notvalid){
			Tile exitcanadate = randomPoint();
			if (exitcanadate !=null && exitcanadate != PlayerPosition && exitcanadate != Exit) {
				Exit = exitcanadate;
				//techniclly unessisary
				notvalid = false;
				return;
			}			
		}
	}
	
	private void newPlayerPosition() {
		if (Grid == null) {
			return;
		} else if (Size == 1) {
			PlayerPosition = Grid[0][0];
		}
		
		boolean notvalid = true;
		
		while(notvalid){
			Tile positionCanadate = randomPoint();
			if (positionCanadate !=null && positionCanadate != PlayerPosition && positionCanadate != Exit) {
				PlayerPosition = positionCanadate;
				//techniclly unessisary
				notvalid = false;
				return;
			}			
		}
	}
	
	private void resetVisited() {
		for (int x = 0; x < Size; x++) {
			for (int y = 0; y < Size; y++) {
				Grid[x][y].visited = false;
			}
		}
	}
	//methods for drawing a row//
	
	//end methods for drawing a row//
	
}
