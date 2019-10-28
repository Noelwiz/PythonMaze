package maze;

public class Tile {
	public int xCord = 0;
	public int yCord = 0;
	
	public Edge North = null;
	public Edge South = null;
	public Edge East = null;
	public Edge West = null;
	
	//dont forget to reset this
	public boolean visited = false;
	
	//constructer
	public Tile(int x, int y) {
		xCord = x;
		yCord = y;
	}
	
	public String toString() {
		//returns debug information
		return("x: "+xCord+" y: "+yCord);
	}
	
	//returns a list of adjacent tiles
	public Tile[] getAdjacent(){
		Tile[] adjacentList = new Tile[4];
		
		//add the northern tile as either null if it's the same, or the tile if it isnt
		if(North != null && North.Tile2 != this) {
			adjacentList[0] = North.Tile2;
		}
		
		//add southern tile or null if same
		if(South.Tile1 != null && South.Tile1 != this) {
			adjacentList[1]=South.Tile2;
		}
		
		//add eastern tile or null if same
		if(East.Tile2!=null&&East.Tile2!=this) {
			adjacentList[2] = East.Tile2;
		}
		
		//add western tile or null if same
		if(West.Tile1!=null&&West.Tile1!=this) {
			adjacentList[3] = West.Tile1;
		}
		
		return adjacentList;
	}
	
	//check if a direction is  a wall
	public boolean isWall(String direction){
		if (direction.equalsIgnoreCase("east")) {
			return East.Wall;
		}
		else if (direction.equalsIgnoreCase("west")) {
			return West.Wall;
		}
		else if (direction.equalsIgnoreCase("north")) {
			return North.Wall;
		}
		else if (direction.equalsIgnoreCase("south")) {
			return South.Wall;
		}
		else {
			System.out.println("isWall in Tile was passed something other than a direction: "+direction);
			return false;
		}
		
	}
	
	//draw a picture of the tile, formerly implemnted as a -> void with a print statement
	//public String Draw(){}

}
