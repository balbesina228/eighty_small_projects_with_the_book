from math import sin, cos
from sys import platform, exit
from os import system
from time import sleep

pause_amount = 0.1
width, height = 80, 24
scale_x = (width - 4) // 8
scale_y = (height - 4) // 8
scale_y *= 2
translate_x = (width - 4) // 2
translate_y = (height - 4) // 2
line_char = chr(9608)
x_rotate_speed = 0.03
y_rotate_speed = 0.08
z_rotate_speed = 0.13
x_num = 0
y_num = 1
z_num = 2


def line(x1, y1, x2, y2):
    points = []
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]
    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    is_reversed = x1 > x2
    if is_reversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y2
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        for current_x in range(x2, x1 - 1, -1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y <= 0:
                current_y -= y_direction
                extra_y += delta_x
    else:
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y1
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        for current_x in range(x1, x2 + 1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y < 0:
                current_y += y_direction
                extra_y += delta_x
    return points


def rotate_point(x, y, z, ax, ay, az):
    rotated_x = x
    rotated_y = (y * cos(ax)) - (z * sin(ax))
    rotated_z = (y * sin(ax)) + (z * cos(ax))
    x, y, z = rotated_x, rotated_y, rotated_z

    rotated_x = (z * sin(ay)) + (x * cos(ay))
    rotated_y = y
    rotated_z = (z * cos(ay)) - (x * sin(ay))
    x, y, z = rotated_x, rotated_y, rotated_z

    rotated_x = (x * cos(az)) - (y * sin(az))
    rotated_y = (x * sin(az)) + (y * cos(az))
    rotated_z = z

    return (rotated_x, rotated_y, rotated_z)


def adjust_point(point):
     return ((int(point[x_num]) * scale_x + translate_x),
            (int(point[y_num] * scale_y + translate_y)))


'''
cube_corners points
     0---1
    /|  /|
   2---3 |
   | 4-|-5
   |/  |/
   6---7
'''
cube_corners = [[-1, -1, -1], [1, -1, -1], [-1, -1, 1], [1, -1, 1],
                [-1, 1, -1], [1, 1, -1], [-1, 1, 1], [1, 1, 1]]
rotated_corners = [None, None, None, None, None, None, None, None]
x_rotation = 0.0
y_rotation = 0.0
z_rotation = 0.0

try:
    while True:
        x_rotation += x_rotate_speed
        y_rotation += y_rotate_speed
        z_rotation += z_rotate_speed
        for i in range(len(cube_corners)):
            x = cube_corners[i][x_num]
            y = cube_corners[i][y_num]
            z = cube_corners[i][z_num]
            rotated_corners[i] = rotate_point(x, y, z, x_rotation,
                                              y_rotation, z_rotation)
        cube_points = []
        for from_corner_index, to_corner_index in ((0, 1), (1, 3), (3, 2), (2, 0),
                                                   (0, 4), (1, 5), (2, 6), (3, 7),
                                                   (4, 5), (5, 7), (7, 6), (6, 4)):
            from_x, from_y = adjust_point(rotated_corners[from_corner_index])
            to_x, to_y = adjust_point(rotated_corners[to_corner_index])
            points_on_line = line(from_x, from_y, to_x, to_y)
            cube_points.extend(points_on_line)
        cube_points = tuple(frozenset(cube_points))
        for y in range(height):
            for x in range(width):
                if (x, y) in cube_points:
                    print(line_char, end='', flush=False)
                else:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)
        sleep(pause_amount)
        if platform == 'win32':
            system('cls')
        else:
            system('clear')
except KeyboardInterrupt:
    print('Rotating Cube by Al Sweigart')
    exit()
