from copy import copy
from os import getcwd, listdir, path
from sys import exit

wall = '#'
empty = ' '
start = 'S'
maze_exit = 'E'
block = chr(9617)
north = 'north'
south = 'south'
west = 'west'
east = 'east'


def wall_str_to_wall_dict(wall_str):
    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, char in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = char
    wall_dict['height'] = height + 1
    wall_dict['width'] = width + 1
    return wall_dict


exit_dict = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I', (3, 0): 'T',
             'height': 1, 'width': 4}
all_open = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................
'''.strip())
closed = {}
closed['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____
'''.strip())
closed['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.
'''.strip())
closed['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________
'''.strip())
closed['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.
'''.strip())
closed['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..
'''.strip())
closed['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..
'''.strip())


def display_wall_dict(wall_dict):
    print(block * (wall_dict['width'] + 2))
    for y in range(wall_dict['height']):
        print(block, end='')
        for x in range(wall_dict['width']):
            wallie = wall_dict[(x, y)]
            if wallie == '.':
                wallie = ' '
            print(wallie, end='')
        print(block)
    print(block * (wall_dict['width'] + 2))


def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    dst_wall_dict = copy(dst_wall_dict)
    for x in range(src_wall_dict['width']):
        for y in range(src_wall_dict['height']):
            dst_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
    return dst_wall_dict


def make_wall_dict(maze, player_x, player_y, player_direction, exit_x, exit_y):
    if player_direction == north:
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if player_direction == south:
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if player_direction == east:
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if player_direction == west:
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))
    section = {}
    for sec, x_off, y_off in offsets:
        section[sec] = maze.get((player_x + x_off, player_y + y_off), wall)
        if (player_x + x_off, player_y + y_off) == (exit_x, exit_y):
            section[sec] = maze_exit
    wall_dict = copy(all_open)
    paste_closed_to = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == wall:
            wall_dict = paste_wall_dict(closed[sec], wall_dict,
                        paste_closed_to[sec][0], paste_closed_to[sec][1])
    if section['C'] == maze_exit:
        wall_dict = paste_wall_dict(exit_dict, wall_dict, 7, 9)
    if section['E'] == maze_exit:
        wall_dict = paste_wall_dict(exit_dict, wall_dict, 0, 11)
    if section['F'] == maze_exit:
        wall_dict = paste_wall_dict(exit_dict, wall_dict, 13, 11)
    return wall_dict


print('Maze runner 3D')
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')
    if filename.upper() == 'LIST':
        print('Maze files found in', getcwd())
        for file_in_current_folder in listdir():
            if (file_in_current_folder.startswith('maze')
            and file_in_current_folder.endswith('.txt')):
                print(' ', file_in_current_folder)
        continue
    if filename.upper() == 'QUIT':
        exit()
    if path.exists(filename):
        break
    print('There is no file named', filename)
mazefile = open(filename)
maze = {}
lines = mazefile.readlines()
px = None
py = None
exit_x = None
exit_y = None
y = 0
for line in lines:
    width = len(line.rstrip())
    for x, char in enumerate(line.rstrip()):
        assert char in (wall, empty, start, maze_exit), f'Invalid character' \
                                                        f' at column {x + 1}, line {y + 1}'
        if char in (wall, empty):
            maze[(x, y)] = char
        elif char == start:
            px, py = x, y
            maze[(x, y)] = empty
        elif char == maze_exit:
            exit_x, exit_y = x, y
            maze[(x, y)] = empty
    y += 1
height = y
assert px != None and py != None, 'No start point in file'
assert exit_x != None and exit_y != None, 'No exit point in file'
p_dir = north
while True:
    display_wall_dict(make_wall_dict(maze, px, py, p_dir, exit_x, exit_y))
    while True:
        print(f'Location ({px}, {py}), direction: {p_dir}')
        print('                       (W)')
        print('Enter the direction: (A) (D)   or QUIT')
        move = input().upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            exit()
        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Enter one of F, L, or R (or W, A, D)')
            continue
        if move == 'F' or move == 'W':
            if p_dir == north and maze[(px, py - 1)] == empty:
                py -= 1
                break
            if p_dir == south and maze[(px, py + 1)] == empty:
                py += 1
                break
            if p_dir == east and maze[(px + 1, py)] == empty:
                px += 1
                break
            if p_dir == west and maze[(px - 1, py)] == empty:
                px -= 1
                break
        elif move == 'L' or move == 'A':
            p_dir = {north: west, west: south,
                   south: east, east: north}[p_dir]
            break
        elif move == 'R' or move == 'D':
            p_dir = {north: east, east: south,
                     south: west, west: north}[p_dir]
            break
        elif move.startswith('T'):
            px, py = move.split()[1].split(',')
            px = int(px)
            py = int(py)
            break
        else:
            print('You cannot move in that direction')
    if (px, py) == (exit_x, exit_y):
        print('You have reached the exit!')
        print('Good job!')
        exit()
