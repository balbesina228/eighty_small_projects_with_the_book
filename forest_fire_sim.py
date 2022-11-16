from sys import exit
from random import random
from time import sleep

try:
    from bext import fg, goto, clear
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
''')
    exit()

width = 79
height = 22
tree = 'A'
fire = 'W'
empty = '.'
initial_tree_density = 0.01
grow_chance = 0.01
fire_chance = 0.01
pause_length = 0.5


def main():
    forest = create_new_forest()
    clear()
    while True:
        display_forest(forest)
        next_forest = {'width': forest['width'], 'height': forest['height']}
        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in forest:
                    continue
                if forest[(x, y)] == empty and random() <= grow_chance:
                    next_forest[(x, y)] = tree
                elif forest[(x, y)] == tree and random() <= fire_chance:
                    next_forest[(x, y)] = fire
                elif forest[(x, y)] == fire:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == tree:
                                next_forest[(x + ix, y + iy)] = fire
                    forest[(x, y)] = empty
                else:
                    next_forest[(x, y)] = forest[(x, y)]
        forest = next_forest
        sleep(pause_length)


def create_new_forest():
    forest = {'width': width, 'height': height}
    for x in range(width):
        for y in range(height):
            if random() * 100 < initial_tree_density:
                forest[(x, y)] = tree
            else:
                forest[(x, y)] = empty
    return forest


def display_forest(forest):
    goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == tree:
                fg('green')
                print(tree, end='')
            elif forest[(x, y)] == fire:
                fg('orange')
                print(fire, end='')
            elif forest[(x, y)] == empty:
                print(empty, end='')
    print()
    fg('reset')
    print('Grow chance:', grow_chance * 100, '%', end=' | ')
    print('Lightning chance:', fire_chance * 100, '%', end=' | ')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
