from time import sleep
from sys import exit

pause = 2
print('Ninety-nine bottles')
sleep(2)
bottles = 99
try:
    while bottles > 1:
        print(bottles, 'bottles of milk on the wall,')
        sleep(pause)
        print(bottles, 'bottles of milk,')
        sleep(pause)
        print('Take one down, pass it around,')
        sleep(pause)
        bottles -= 1
        print(bottles, 'bottles of milk on the wall!')
        sleep(pause)
        print()
    print('1 bottle of milk on the wall,')
    sleep(pause)
    print('1 bottle of milk,')
    sleep(pause)
    print('Take it down, pass it around,')
    sleep(pause)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    exit()
