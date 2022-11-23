from random import random, shuffle, choice
from sys import exit, stdout
from time import sleep

try:
    from bext import fg, clear, goto
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
''')

pause_length = 0.2
wide_fall_chance = 50
screen_width = 80
screen_height = 26
X = 0
Y = 1
sand = chr(9617)
wall = chr(9608)
hourglass = set()
for i in range(18, 37):
    hourglass.add((i, 1))
    hourglass.add((i, 23))
for i in range(1, 5):
    hourglass.add((18, i))
    hourglass.add((36, i))
    hourglass.add((18, i + 19))
    hourglass.add((36, i + 19))
for i in range(8):
    hourglass.add((19 + i, 5 + i))
    hourglass.add((35 - i, 5 + i))
    hourglass.add((25 - i, 13 + i))
    hourglass.add((29 + i, 13 + i))
initial_sand = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        initial_sand.add((x, y + 4))


def main():
    fg('yellow')
    clear()
    goto(0, 0)
    print('Ctrl-C to quit.', end='')
    for wallie in hourglass:
        goto(wallie[X], wallie[Y])
        print(wall, end='')
    while True:
        all_sand = list(initial_sand)
        for sandy in all_sand:
            goto(sandy[X], sandy[Y])
            print(sand, end='')
        run_hourglass_simulation(all_sand)


def run_hourglass_simulation(all_sand):
    while True:
        shuffle(all_sand)
        sand_moved_on_this_step = False
        for i, sandy in enumerate(all_sand):
            if sandy[Y] == screen_height - 1:
                continue
            no_sand_below = (sandy[X], sandy[Y] + 1) not in all_sand
            no_wall_below = (sandy[X], sandy[Y] + 1) not in hourglass
            can_fall_down = no_sand_below and no_wall_below
            if can_fall_down:
                goto(sandy[X], sandy[Y])
                print(' ', end='')
                goto(sandy[X], sandy[Y])
                print(sand, end='')
                all_sand[i] = (sandy[X], sandy[Y] + 1)
                sand_moved_on_this_step = True
            else:
                below_left = (sandy[X] - 1, sandy[Y] + 1)
                no_sand_below_left = below_left not in all_sand
                no_wall_below_left = below_left not in hourglass
                left = (sandy[X] - 1, sandy[Y])
                no_wall_left = left not in hourglass
                not_on_left_edge = sandy[X] > 0
                can_fall_left = no_sand_below_left and no_wall_below_left and \
                                no_wall_left and not_on_left_edge

                below_right = (sandy[X] + 1, sandy[Y] + 1)
                no_sand_below_right = below_right not in all_sand
                no_wall_below_right = below_right not in hourglass
                right = (sandy[X] + 1, sandy[Y])
                no_wall_right = right not in hourglass
                not_on_right_edge = sandy[X] < screen_width - 1
                can_fall_right = (no_sand_below_right and no_wall_right and
                                 no_wall_below_right and not_on_right_edge)

                falling_direction = None
                if can_fall_left and not can_fall_right:
                    falling_direction = -1
                elif not can_fall_left and can_fall_right:
                    falling_direction = 1
                elif can_fall_left and can_fall_right:
                    falling_direction = choice((-1, 1))
                if random() * 100 <= wide_fall_chance:
                    below_two_left = (sandy[X] - 2, sandy[Y] + 1)
                    no_sand_below_two_left = below_two_left not in all_sand
                    no_wall_below_two_left = below_two_left not in hourglass
                    not_on_second_to_left_edge = sandy[X] > 1
                    can_fall_two_left = (can_fall_left and
                                         no_wall_below_two_left and
                                         no_sand_below_two_left and
                                         not_on_second_to_left_edge)
                    below_two_right = (sandy[X] + 2, sandy[Y] + 1)
                    no_sand_below_two_right = below_two_right not in all_sand
                    no_wall_below_two_right = below_two_right not in hourglass
                    not_on_second_to_right_edge = sandy[X] < screen_width - 2
                    can_fall_two_right = (can_fall_right and
                                         no_wall_below_two_right and
                                         no_sand_below_two_right and
                                         not_on_second_to_right_edge)
                    if can_fall_two_right and not can_fall_two_left:
                        falling_direction = 2
                    elif not can_fall_two_right and can_fall_two_left:
                        falling_direction = -2
                    elif can_fall_two_right and can_fall_two_left:
                        falling_direction = choice((-2, 2))
                if falling_direction == None:
                    continue
                goto(sandy[X], sandy[Y])
                print(' ', end='')
                goto(sandy[X] + falling_direction, sandy[Y] + 1)
                print(sand, end='')
                all_sand[i] = (sandy[X] + falling_direction, sandy[Y] + 1)
                sand_moved_on_this_step = True
        stdout.flush()
        sleep(pause_length)
        if not sand_moved_on_this_step:
            sleep(2)
            for sandy in all_sand:
                goto(sandy[X], sandy[Y])
                print(' ', end='')
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
