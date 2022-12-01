from os import getcwd, listdir, path
from sys import exit

wall = '#'
empty = ' '
start = 'S'
exit_maze = 'E'
player = '@'
block = chr(9617)


def display_maze(maze):
    for y in range(height):
        for x in range(width):
            if (x, y) == (player_x, player_y):
                print(player, end='')
            elif (x, y) == (exit_x, exit_y):
                print(exit_maze, end='')
            elif maze[(x, y)] == wall:
                print(block, end='')
            else:
                print(maze[(x, y)], end='')
        print()


print('Maze Runner 2D')
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')
    if filename.upper() == 'LIST':
        print('Maze files found in', getcwd())
        for file_in_current_folder in listdir():
            if file_in_current_folder.startswith('maze') and \
                    file_in_current_folder.endswith('.txt'):
                print('  ', file_in_current_folder)
            continue
    if filename.upper() == 'QUIT':
        exit()
    if path.exists(filename):
        break
    print('There is no file named', filename)
mazefile = open(filename)
maze = {}
lines = mazefile.readlines()
player_x, player_y, exit_x, exit_y = None, None, None, None
y = 0
for line in lines:
    width = len(line.rstrip())
    for x, char in enumerate(line.rstrip()):
        assert char in (wall, empty, start, exit_maze), 'Invalid character'\
        f'at column {x + 1}, line {y + 1}'
        if char in (wall, empty):
            maze[(x, y)] = char
        elif char == start:
            player_x, player_y = x, y
            maze[(x, y)] = empty
        elif char == exit_maze:
            exit_x, exit_y = x, y
            maze[(x, y)] = empty
    y += 1
height = y
assert player_x != None and player_y != None, 'No start in maze file'
assert exit_x != None and exit_y != None, 'No exit in maze file'
while True:
    display_maze(maze)
    while True:
        print('                           W')
        print('Enter direction, or QUIT: ASD')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            exit()
        if move not in ['W', 'A', 'S', 'D']:
            print('Invalid direction.')
            continue
        if move == 'W' and maze[(player_x, player_y - 1)] == empty:
            break
        if move == 'A' and maze[(player_x - 1, player_y)] == empty:
            break
        if move == 'S' and maze[(player_x, player_y + 1)] == empty:
            break
        if move == 'D' and maze[(player_x + 1, player_y)] == empty:
            break
        print('You cannot move in that direction')
    if move == 'W':
        while True:
            player_y -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y - 1)] == wall:
                break
            if maze[(player_x - 1, player_y)] == empty or \
                    maze[(player_x + 1, player_y)] == empty:
                break
    elif move == 'S':
        while True:
            player_y += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y + 1)] == wall:
                break
            if maze[(player_x - 1, player_y)] == empty or \
                    maze[(player_x + 1, player_y)] == empty:
                break
    elif move == 'A':
        while True:
            player_x -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x - 1, player_y)] == wall:
                break
            if maze[(player_x, player_y - 1)] == empty or \
                    maze[(player_x, player_y + 1)] == empty:
                break
    elif move == 'D':
        while True:
            player_x += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x + 1, player_y)] == wall:
                break
            if maze[(player_x, player_y - 1)] == empty or \
                    maze[(player_x, player_y + 1)] == empty:
                break
    if (player_x, player_y) == (exit_x, exit_y):
        display_maze(maze)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        exit()
