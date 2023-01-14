from time import sleep
from sys import exit

print('''
Rock, Paper, Scissors, by Al Sweigart
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')
wins = 0
losses = 0
ties = 0
while True:
    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        print('Enter your move: (R)ock,  (P)aper, (S)cissors, (Q)uit')
        player_move = input().upper()
        if player_move == 'Q':
            print('Thanks for playing!')
            exit()
        if player_move in ('R', 'P', 'S'):
            break
        else:
            print('Enter R, P, S or Q.')
    if player_move == 'R':
        print('ROCK versus...')
        player_move = 'rock'
        computer_move = 'scissors'
    if player_move == 'P':
        print('PAPER versus...')
        player_move = 'paper'
        computer_move = 'rock'
    if player_move == 'S':
        print('SCISSORS versus...')
        player_move = 'scissors'
        computer_move = 'paper'
    sleep(0.5)
    print('1...')
    sleep(0.25)
    print('2...')
    sleep(0.25)
    print('3...')
    sleep(0.25)
    print(computer_move.upper())
    sleep(0.5)
    print('You win!')
    wins += 1
