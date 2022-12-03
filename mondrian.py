from sys import exit
from random import randint, choice

try:
    from bext import fg, bg, clear, size
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
''')
    exit()
min_x_increase = 6
max_x_increase = 16
min_y_increase = 3
max_y_increase = 6
white = 'white'
black = 'black'
red = 'red'
yellow = 'yellow'
blue = 'blue'
width, height = size()
width -= 1
height -= 3
while True:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = white
    num_of_segments_to_delete = 0
    x = randint(min_x_increase, max_x_increase)
    while x < width - min_x_increase:
        num_of_segments_to_delete += 1
        for y in range(height):
            canvas[(x, y)] = black
        x += randint(min_x_increase, max_x_increase)
    y = randint(min_y_increase, max_y_increase)
    while y < height - min_y_increase:
        num_of_segments_to_delete += 1
        for x in range(width):
            canvas[(x, y)] = black
        y += randint(min_y_increase, max_y_increase)
    num_of_rectangles_to_paint = num_of_segments_to_delete - 3
    num_of_segments_to_delete = int(num_of_segments_to_delete * 1.5)
    for i in range(num_of_segments_to_delete):
        while True:
            start_x = randint(1, width - 2)
            start_y = randint(1, height - 2)
            if canvas[(start_x, start_y)] == white:
                continue
            if canvas[(start_x - 1, start_y)] == white and \
                canvas[(start_x + 1, start_y)] == white:
                orientation = 'vertical'
            elif canvas[(start_x, start_y - 1)] == white and \
                canvas[(start_x, start_y + 1)] == white:
                orientation = 'horizontal'
            else:
                continue
            points_to_delete = [(start_x, start_y)]
            can_delete_segment = True
            if orientation == 'vertical':
                for change_y in (-1, 1):
                    y = start_y
                    while 0 < y < height - 1:
                        y += change_y
                        if canvas[(start_x - 1, y)] == black and \
                           canvas[(start_x + 1, y)] == black:
                            break
                        elif ((canvas[(start_x - 1, y)] == white and
                               canvas[(start_x + 1, y)] == black) or
                               canvas[(start_x - 1, y)] == black and
                               canvas[(start_x + 1, y)] == white):
                            can_delete_segment = False
                            break
                        else:
                            points_to_delete.append((start_x, y))
            elif orientation == 'horizontal':
                for change_x in (-1, 1):
                    x = start_x
                    while 0 < x < width - 1:
                        x += change_x
                        if canvas[(x, start_y - 1)] == black and \
                           canvas[(x, start_y + 1)] == black:
                            break
                        elif ((canvas[(x, start_y - 1)] == white and
                               canvas[(x, start_y + 1)] == black) or
                               canvas[(x, start_y - 1)] == black and
                               canvas[(x, start_y + 1)] == white):
                            can_delete_segment = False
                            break
                        else:
                            points_to_delete.append((x, start_y))
            if not can_delete_segment:
                continue
            break
        for x, y in points_to_delete:
            canvas[(x, y)] = white
    for x in range(width):
        canvas[(x, 0)] = black
        canvas[(x, height - 1)] = black
    for y in range(height):
        canvas[(0, y)] = black
        canvas[(width - 1, y)] = black
    for i in range(num_of_rectangles_to_paint):
        while True:
            start_x = randint(1, width - 2)
            start_y = randint(1, height - 2)
            if canvas[(start_x, start_y)] != white:
                continue
            else:
                break
        color_to_paint = choice([red, yellow, blue, black])
        points_to_paint = set([(start_x, start_y)])
        while len(points_to_paint) > 0:
            x, y = points_to_paint.pop()
            canvas[(x, y)] = color_to_paint
            if canvas[(x - 1, y)] == white:
                points_to_paint.add((x - 1, y))
            if canvas[(x + 1, y)] == white:
                points_to_paint.add((x + 1, y))
            if canvas[(x, y - 1)] == white:
                points_to_paint.add((x, y - 1))
            if canvas[(x, y + 1)] == white:
                points_to_paint.add((x, y + 1))
    for y in range(height):
        for x in range(width):
            bg(canvas[(x, y)])
            print(' ', end='')
        print()
    try:
        input('Press Enter for another work or Ctrl-C to quit')
    except KeyboardInterrupt:
        exit()
