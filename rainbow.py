from time import sleep
from sys import exit

try:
    from bext import fg
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
    ''')
    exit()
print('Rainbow by Al Sweigart')
print('Press Ctrl-C to stop.')
sleep(3)
indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        fg('red')
        print('##', end='')
        fg('yellow')
        print('##', end='')
        fg('green')
        print('##', end='')
        fg('blue')
        print('##', end='')
        fg('cyan')
        print('##', end='')
        fg('purple')
        print('##')

        if indent_increasing:
            indent += 1
            if indent == 60:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
        sleep(0.2)

except KeyboardInterrupt:
    exit()
