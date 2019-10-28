package maze;

public class Edge {
	//public boolean Complete = false;
	
	public boolean Wall = true;
	public Tile Tile1 = null;
	public Tile Tile2 = null;
	public boolean NorthSouth = false; 
	
    /*xxxxx
     #x1E2x
     #xxxxx
     #xx2xx
     #xxExx
     #xx1xx*/
	
	public Edge(Tile one, Tile two, boolean ns) {
		Tile1 = one;
		Tile2 = two;
		NorthSouth = ns;
	}
	
	public String toStrin() {
		return(Tile1.toString() +" " + Wall + " " + Tile2.toString());
	}
	
	public String strPicOfWall() {
		if (Wall) {
			//look I was having trouble, and it works, mostly it was with red underlines because this is in an if statment and its 1 am
			char[] symbol = {References.WallChar};
			String picture =  new String(symbol);
			return picture;
		} else {
			if(NorthSouth) {
				char[] array = {References.NorthSouthChar};
				return new String(array);
			} else {
				char[] array = {References.EastWestChar};
				return new String(array);
			}
				
			
		}
		//return null;
	}
}
