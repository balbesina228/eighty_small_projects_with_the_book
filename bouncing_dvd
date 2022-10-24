from sys import exit, stdout
from random import choice, randint
from time import sleep

try:
    import bext
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
    ''')
    exit

width, height = bext.size()
width -= 2

number_of_logos = 10 # (!) Try to change!
pause_amount = 0.5 # (!) Try to change!
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan', 'white']

up_right = 'ur'
up_left = 'ul'
down_right = 'dr'
down_left = 'dl'
directions = (up_right, up_left, down_left, down_right)
color = 'color'
x = 'x'
y = 'y'
dir = 'direction'

def main():
    bext.clear()
    logos = []
    for i in range(number_of_logos):
        logos.append({
            color: choice(colors),
            x: randint(1, width - 4),
            y: randint(1, height - 4),
            dir: choice(directions)
            })
        if logos[-1][x] % 2 == 1:
            logos[-1][x] -= 1

    corner_bounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[x], logo[y])
            print('   ', end='')

            original_direction = logo[dir]
            #CORNERS
            if logo[x] == 0 and logo[y] == 0:
                logo[dir] = down_right
                corner_bounces += 1
            elif logo[x] == 0 and logo[y] == height - 1:
                logo[dir] = up_right
                corner_bounces += 1
            elif logo[x] == width - 3 and logo[y] == 0:
                logo[dir] = down_left
                corner_bounces += 1
            elif logo[x] == width - 3 and logo[y] == height - 1:
                logo[dir] = up_left
                corner_bounces += 1
            #LEFT SIDE
            elif logo[x] == 0 and logo[dir] == up_left:
                logo[dir] = up_right
            elif logo[x] == 0 and logo[dir] == down_left:
                logo[dir] = down_right
            #RIGHT SIDE
            elif logo[x] == width - 3 and logo[dir] == up_right:
                logo[dir] = up_left
            elif logo[x] == width - 3 and logo[dir] == down_right:
                logo[dir] = down_left
            #UP SIDE
            elif logo[y] == 0 and logo[dir] == up_left:
                logo[dir] = down_left
            elif logo[y] == 0 and logo[dir] == up_right:
                logo[dir] = down_right
            #DOWN SIDE
            elif logo[y] == height - 1 and logo[dir] == down_left:
                logo[dir] = up_left
            elif logo[y] == height - 1 and logo[dir] == down_right:
                logo[dir] = up_right

            if logo[dir] != original_direction:
                logo[color] = choice(colors)

            if logo[dir] == up_right:
                logo[x] += 2
                logo[y] -= 1
            elif logo[dir] == up_left:
                logo[x] -= 2
                logo[y] -= 1
            elif logo[dir] == down_right:
                logo[x] += 2
                logo[y] += 1
            elif logo[dir] == down_left:
                logo[x] -= 2
                logo[y] += 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corner_bounces, end='')
        for logo in logos:
            bext.goto(logo[x], logo[y])
            bext.fg(logo[color])
            print('DVD', end='')

        bext.goto(0, 0)

        stdout.flush()
        sleep(pause_amount)

if __name__ == '__main__':
    main()
