from random import random, choice, randint
from shutil import get_terminal_size
from sys import stdout, exit
from time import sleep

min_stream_length = 6
max_stream_length = 14
pause = 0.1
stream_chars = ['0', '1']
density = 0.02
width = get_terminal_size()[0] - 1
print('Digital stream by Al Sweigart.\nPress Ctrl-C to quit.')
sleep(2)

try:
    columns = [0] * width
    while True:
        for i in range(width):
            if columns[i] == 0:
                if random() <= density:
                    columns[i] = randint(min_stream_length, max_stream_length)

            if columns[i] > 0:
                print(choice(stream_chars), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        stdout.flush()
        sleep(pause)

except KeyboardInterrupt:
    exit()
