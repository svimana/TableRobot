# Table Toy Robot
Demo Python game to operate a toy robot on the table

This is a Table Robot Game. Move your robot on a table space 5x5 units.

Commands (CAPITAL LETTERS ONLY):
	HELP - Print this help
	EXIT - Terminate the game
	PLACE X,Y,Direction - Put the robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
		The table is facing Up (NORTH). Bottom-Left corner has 0,0 coordinate.
		Direction can be: NORTH/EAST/SOUTH/WEST. Bottom-Left corner has 0,0 coordinate.
		EAST is to the Right, WEST - Left, South - Down.		
		Example: PLACE 1,1,SOUTH - Robot will be placed at coordinate 2,2 facing Down
	MOVE - Move the robot one unit forward in the direction it is currently facing.
		Any move that would cause the robot to fall will be ignored.
	LEFT - Rotate the robot 90 degrees to the left without changing the position of the robot.
	RIGHT - Rotate the robot 90 degrees to the right without changing the position of the robot.
	REPORT - Announce the X,Y and Direction of the robot.
