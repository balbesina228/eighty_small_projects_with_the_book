from sys import exit, stdout
from random import randint, choice
from copy import copy
from time import sleep

try:
    from bext import goto, fg, size, bg, clear
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
''')
    exit()
width, height = size()
width -=1
height -=1
num_of_ants = 10
pause = 0.1
ant_up = '^'
ant_down = 'v'
ant_left = '<'
ant_right = '>'
ant_color = 'red'
black_tile = 'black'
white_tile = 'white'
north = 'north'
south = 'south'
east = 'east'
west = 'west'


def main():
    fg(ant_color)
    bg(white_tile)
    clear()
    board = {'width': width, 'height': height}
    ants = []
    for i in range(num_of_ants):
        ant = {
            'x': randint(0, width - 1),
            'y': randint(0, height - 1),
            'direction': choice([north, south, west, east])
        }
        ants.append(ant)
    changed_tiles = []
    while True:
        display_board(board, ants, changed_tiles)
        next_board = copy(board)
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                next_board[(ant['x'], ant['y'])] = False
                if ant['direction'] == north:
                    ant['direction'] = east
                elif ant['direction'] == east:
                    ant['direction'] = south
                elif ant['direction'] == south:
                    ant['direction'] = west
                elif ant['direction'] == west:
                    ant['direction'] = north
            else:
                next_board[(ant['x'], ant['y'])] = True
                if ant['direction'] == north:
                    ant['direction'] = west
                elif ant['direction'] == west:
                    ant['direction'] = south
                elif ant['direction'] == south:
                    ant['direction'] = east
                elif ant['direction'] == east:
                    ant['direction'] = north
            changed_tiles.append((ant['y'], ant['y']))
            if ant['direction'] == north:
                ant['y'] -= 1
            elif ant['direction'] == west:
                ant['x'] -= 1
            elif ant['direction'] == south:
                ant['y'] += 1
            elif ant['direction'] == east:
                ant['x'] += 1
            ant['x'] %= width
            ant['y'] %= height
            changed_tiles.append((ant['x'], ant['y']))
        board = next_board


def display_board(board, ants, changed_tiles):
    for x, y in changed_tiles:
        goto(x, y)
        if board.get((x, y), False):
            bg(black_tile)
        else:
            bg(white_tile)
        ant_is_here = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                ant_is_here = True
                if ant['direction'] == north:
                    print(ant_up, end='')
                elif ant['direction'] == south:
                    print(ant_down, end='')
                elif ant['direction'] == west:
                    print(ant_left, end='')
                elif ant['direction'] == east:
                    print(ant_right, end='')
                break
        if not ant_is_here:
            print(' ', end='')
    goto(0, height)
    bg(white_tile)
    print('Ctrl-C to quit', end='')
    stdout.flush()
    sleep(pause)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Langton's ant")
        exit()
