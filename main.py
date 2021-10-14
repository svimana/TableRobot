from robot import TableRobot
from dynamic import (
    Location, Direction, DirectionFlag, get_direction_flag
)
import traceback

def print_help():
    print('This is a Table Robot Game. Move your robot on a table space 5x5 units.')
    print('Commands (CAPITAL LETTERS ONLY):')
    print('\tHELP - Print this help')
    print('\tEXIT - Terminate the game')
    print('\tPLACE X,Y,Direction - Put the robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.')
    print('\t\tThe table is facing Up (NORTH). Bottom-Left corner has 0,0 coordinate.')
    print('\t\tDirection can be: NORTH/EAST/SOUTH/WEST. Bottom-Left corner has 0,0 coordinate.')
    print('\t\tEAST is to the Right, WEST - Left, South - Down.')
    print('\t\tExample: PLACE 1,1,SOUTH - Robot will be placed at the coordinate 2,2 facing SOUTH')
    print('\tMOVE - Move the robot one unit forward in the direction it is currently facing.')
    print('\tLEFT - Rotate the robot 90 degrees to the left without changing the position of the robot.')
    print('\tRIGHT - Rotate the robot 90 degrees to the right without changing the position of the robot.')
    print('\tREPORT - Announce the X,Y and Direction of the robot.')

def run():
    robot = TableRobot()
    while True:
        try:
            str = input("Enter your command: ")
            if len(str) < 3:
                print("Wrong command. Try again.")
                print_help()
                continue
            line = str.split(' ')
            x = -1
            y = -1
            direction = None
            cmd = ''
            if len(line) > 1:
                # Extracting parameters is defined
                params = line[1].split(',')
                x = int(params[0])
                y = int(params[1])
                direction = Direction(get_direction_flag(params[2]))
            cmd = line[0]
            if cmd == 'EXIT':
                print("Terminating the game. Hope you've enjoyed it and see you back soon!")
                return
            if cmd == 'HELP':
                print_help()
            if not robot.is_on_table() and cmd != 'PLACE':
                print("Sorry, your Robot is not on the table yet. Try PLACE command first.")
            if cmd == 'PLACE':
                if not robot.place(Location(x,y), direction):
                    print('ERROR. Looks like you have missed the table ... Try again')
                    continue
            if cmd == 'REPORT':
                print(robot.print_position())
            if cmd == 'MOVE':
                robot.move()
            if cmd == 'LEFT':
                robot.left()
            if cmd == 'RIGHT':
                robot.right()

        except ValueError:
            traceback.print_exc()
            continue

print_help()
run()