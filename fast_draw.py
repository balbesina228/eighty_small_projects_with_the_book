from sys import exit
from time import sleep, time
from random import randint

print('''
Fast Draw, by Al Sweigart.

Time to test your reflexes and see if you are the fastest
draw in the west!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears.
''')
input('Press Enter to begin...')

while True:
    print('\nIt is high noon...')
    sleep(randint(20, 50) / 10.0)
    print('DRAW!')
    draw_time = time()
    input()
    time_elapsed = time() - draw_time
    if time_elapsed < 0.01:
        print('You drawed before "DRAW!" appeared! You lose.')
    elif time_elapsed > 0.3:
        time_elapsed = round(time_elapsed, 4)
        print(f'You took {time_elapsed} seconds to draw. Too slow!')
    else:
        time_elapsed = round(time_elapsed, 4)
        print(f'You took {time_elapsed} seconds to draw.')
        print('You are the fastest draw in the west! You win!')

    print('Enter "QUIT" to quit, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        exit()
    else:
        continue
