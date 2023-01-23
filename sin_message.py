from math import sin
from shutil import get_terminal_size
from sys import exit
from time import sleep

width, height = get_terminal_size()
width -= 1

print('Sin message by Al Sweigart.')
print('Press Ctrl-C to quit.\n')
print(f'What message do you want to display? (Max {width // 2} chars)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (width // 2):
        break
    print(f'Message has to be 1 to {width // 2} chars.')

step = 0.0
multiplier = (width - len(message)) / 2
try:
    while True:
        sin_of_step = sin(step)
        padding = ' ' * int((sin_of_step + 1) * multiplier)
        print(padding + message)
        sleep(0.1)
        step += 0.25
except KeyboardInterrupt:
    exit()
