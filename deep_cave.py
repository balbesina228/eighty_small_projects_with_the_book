from time import sleep
from sys import exit
from random import randint

width = 85
pause_amount = 0.05

print('Deep cave by Al Sweigart.\nPress Ctrl-C to stop.')
sleep(2)
left_width = 20
gap_width = 30

while True:
    right_width = width - gap_width - left_width
    print('#' * left_width + ' ' * gap_width + '#' * right_width)

    try:
        sleep(pause_amount)
    except KeyboardInterrupt:
        exit()
    dice_roll = randint(1,6)
    if dice_roll == 1 and right_width > 1:
        left_width += 1
    elif dice_roll == 2 and left_width > 1:
        left_width -= 1
    else:
        pass
    dice_roll = randint(1,6)
    if dice_roll == 1 and gap_width > 2:
        gap_width -= 1
    elif dice_roll == 2 and left_width + gap_width < width - 1 and right_width > 1 and left_width > 1:
        gap_width += 1
    else:
        pass
