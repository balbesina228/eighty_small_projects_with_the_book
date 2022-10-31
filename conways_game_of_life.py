from random import randint
from copy import deepcopy
from time import sleep
from sys import exit

width = 79
height = 20
alive = '|'
dead = '-'
next_cells = {}

for x in range(width):
    for y in range(height):
        if randint(0,1) == 0:
            next_cells[(x, y)] = alive
        else:
            next_cells[(x, y)] = dead

while True:
    print('\n' * 50)
    cells = deepcopy(next_cells)
    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')
    for x in range(width):
        for y in range(height):
            left = (x - 1) % width
            right = (x + 1) % width
            above = (y - 1) % height
            below = (y + 1) % height

            num_neighbors = 0
            if cells[(left, above)] == alive:
                num_neighbors += 1
            if cells[(x, above)] == alive:
                num_neighbors += 1
            if cells[(right, above)] == alive:
                num_neighbors += 1
            if cells[(left, y)] == alive:
                num_neighbors += 1
            if cells[(right, y)] == alive:
                num_neighbors += 1
            if cells[(left, below)] == alive:
                num_neighbors += 1
            if cells[(x, below)] == alive:
                num_neighbors += 1
            if cells[(right, below)] == alive:
                num_neighbors += 1

            if cells[(x, y)] == alive and (num_neighbors == 2 or
                                           num_neighbors == 3):
                next_cells[(x, y)] = alive
            elif cells[(x, y)] == dead and num_neighbors == 3:
                next_cells[(x, y)] = alive
            else:
                next_cells[(x, y)] = dead
    try:
        sleep(1)
    except KeyboardInterrupt:
        print("Conway's game of life.\nBy Al Sweigart.")
        exit()
