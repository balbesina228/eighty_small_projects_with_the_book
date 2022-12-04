from sys import exit
from random import randint

all_closed = '''
+------+ +------+ +------+
|      | |      | |      |
|   1  | |   2  | |   3  |
|      | |      | |      |
|      | |      | |      |
|      | |      | |      |
+------+ +------+ +------+
'''
first_goat = '''
+------+ +------+ +------+
|  ((  | |      | |      |
|  oo  | |   2  | |   3  |
| /_/|_| |      | |      |
|    | | |      | |      |
|GOAT||| |      | |      |
+------+ +------+ +------+
'''
second_goat = '''
+------+ +------+ +------+
|      | |  ((  | |      |
|   1  | |  oo  | |   3  |
|      | | /_/|_| |      |
|      | |    | | |      |
|      | |GOAT||| |      |
+------+ +------+ +------+
'''
third_goat = '''
+------+ +------+ +------+
|      | |      | |  ((  |
|   1  | |   2  | |  oo  |
|      | |      | | /_/|_|
|      | |      | |    | |
|      | |      | |GOAT|||
+------+ +------+ +------+
'''
first_car_others_goat = """
+------+ +------+ +------+
| CAR! | |  ((  | |  ((  |
|    __| |  oo  | |  oo  |
|  _/  | | /_/|_| | /_/|_|
| /_ __| |    | | |    | |
|   O  | |GOAT||| |GOAT|||
+------+ +------+ +------+
"""

second_car_others_goat = """
+------+ +------+ +------+
|  ((  | | CAR! | |  ((  |
|  oo  | |    __| |  oo  |
| /_/|_| |  _/  | | /_/|_|
|    | | | /_ __| |    | |
|GOAT||| |   O  | |GOAT|||
+------+ +------+ +------+
"""

third_car_others_goat = """
+------+ +------+ +------+
|  ((  | |  ((  | | CAR! |
|  oo  | |  oo  | |    __|
| /_/|_| | /_/|_| |  _/  |
|    | | |    | | | /_ __|
|GOAT||| |GOAT||| |   O  |
+------+ +------+ +------+
"""
print(f'''
The Monty Hall Problem, by Al Sweigart

In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:
{all_closed}
Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:
{third_goat}
You can choose to either open the door you originally picked or swap
to the other unopened door.

It may seem like it doesn't matter if you swap or not, but your odds
do improve if you swap doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.

You can read an explanation of why swapping is better at
https://en.wikipedia.org/wiki/Monty_Hall_problem
''')
swap_wins = 0
swap_losses = 0
stay_wins = 0
stay_losses = 0
while True:
    door_that_has_car = randint(1, 3)
    print(all_closed)
    while True:
        print('Pick a door 1, 2 or 3 (or QUIT)')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        if response == '1' or response == '2' or response == '3':
            break
    door_pick = int(response)
    while True:
        show_goat_door = randint(1, 3)
        if show_goat_door != door_pick and show_goat_door != door_that_has_car:
            break
    if show_goat_door == 1:
        print(first_goat)
    elif show_goat_door == 2:
        print(second_goat)
    elif show_goat_door == 3:
        print(third_goat)
    print(f'Door {show_goat_door} contains a goat!')
    while True:
        print('Do you want to swap doors? (Y/N)')
        swap = input('> ').upper()
        if swap == 'Y' or swap == 'N':
            break
    if swap == 'Y':
        if door_pick == 1 and show_goat_door == 2:
            door_pick = 3
        elif door_pick == 1 and show_goat_door == 3:
            door_pick = 2
        elif door_pick == 2 and show_goat_door == 1:
            door_pick = 3
        elif door_pick == 2 and show_goat_door == 3:
            door_pick = 1
        elif door_pick == 3 and show_goat_door == 1:
            door_pick = 2
        elif door_pick == 3 and show_goat_door == 2:
            door_pick = 1
    if door_that_has_car == 1:
        print(first_car_others_goat)
    elif door_that_has_car == 2:
        print(second_car_others_goat)
    elif door_that_has_car == 3:
        print(third_car_others_goat)
    print(f'Door {door_that_has_car} has the car!')
    if door_pick == door_that_has_car:
        print('You won!')
        if swap == 'Y':
            swap_wins += 1
        else:
            stay_wins += 1
    else:
        print('You lost.')
        if swap == 'Y':
            swap_losses += 1
        else:
            stay_losses += 1
    total_swaps = swap_wins + swap_losses
    if stay_losses != 0:
        swap_success = round(swap_wins / swap_losses * 100, 1)
    else:
        swap_success = 0.0
    total_stays = stay_wins + stay_losses
    if stay_losses != 0:
        stay_success = round(stay_wins / stay_losses * 100, 1)
    else:
        stay_success = 0.0
    print('\nSwapping     ', end='')
    print(f'{swap_wins} wins, {swap_losses} losses, ')
    print(f'success rate {swap_success}%')
    print('Not swapping ', end='')
    print(f'{stay_wins} wins, {stay_losses} losses, ')
    print(f'success rate {stay_success}%\n')
    input('Press enter to repeat the experiment...')
