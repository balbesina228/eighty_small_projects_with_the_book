from sys import exit
from time import sleep
from random import randint

speed = 0.01
line_pause = 1.5


def slow_print(text, pause_amount=0.1):
    for char in text:
        print(char, flush=True, end='')
        sleep(pause_amount)
    print()
print('niNety-nniinE BoOttels, by Al Sweigart')
print('\n(Press Ctrl-C to quit)')
sleep(2)
bottles = 99
lines = [
    ' bottles of milk on the wall,',
    ' bottles of milk,',
    'Take one down, pass it around,',
    ' bottles of milk on the wall!'
]
try:
    while bottles > 0:
        slow_print(str(bottles) + lines[0], speed)
        sleep(line_pause)
        slow_print(str(bottles) + lines[1], speed)
        sleep(line_pause)
        slow_print(lines[2])
        sleep(line_pause)
        bottles -= 1

        if bottles > 0:
            slow_print(str(bottles) + lines[3], speed)
        else:
            slow_print('No more bottles of milk on the wall!', speed)
        sleep(line_pause)
        print()
        line_num = randint(0, 3)
        line = list(lines[line_num])
        effect = randint(0, 3)
        if effect == 0:
            char_index = randint(0, len(line) - 1)
            line[char_index] = ' '
        elif effect == 1:
            char_index = randint(0, len(line) - 1)
            if line[char_index].isupper():
                line[char_index].lower()
            elif line[char_index].islower():
                line[char_index].upper()
        elif effect == 2:
            char_index = randint(0, len(line) - 2)
            line[char_index], line[char_index + 1] = line[char_index + 1], line[char_index]
        elif effect == 3:
            char_index = randint(0, len(line) - 2)
            line.insert(char_index, line[char_index])
        lines[line_num] = ''.join(line)

except KeyboardInterrupt:
    exit()
