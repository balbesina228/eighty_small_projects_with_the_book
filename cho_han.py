from random import randint
from sys import exit

japanese_numbers = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''
Cho-Han.
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000

while True:
    print(f'You have {purse} mon. How much will you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            exit()
        elif not pot.isdecimal():
            print(f'Enter a number from 1 to {purse}.')
        elif int(pot) > purse:
            print('You don\'t have so much.')
        else:
            pot = int(pot)
            break

    first_die = randint(1,6)
    second_die = randint(1,6)
    print('''
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.
''')
    dice_str = f' {first_die} - {second_die} '
    print('Is it CHO(even) or HAN(odd)?')
    while True:
        response = input('> ').upper()
        if response != 'CHO' and response != 'HAN':
            print('   CHO(even) or HAN(odd)?')
            continue
        else:
            break
    sum_of_dice = first_die + second_die
    print('The dealer lifts the cup to reveal:')
    print(japanese_numbers[first_die] + ' - ' + japanese_numbers[second_die])
    print(' ',dice_str, f'\nThe sum is {sum_of_dice}.')
    if sum_of_dice % 2 == 0:
        answer = 'CHO'
    else:
        answer = 'HAN'
    if response == answer:
        print(f'You win {pot} mon.')
        purse += pot
        print('The house collects a', pot // 10, 'mon fee.')
        purse -= (pot // 10)
    else:
        print(f'You lose {pot} mon.')
        purse -= pot
        if purse == 0:
            print('You have run out of money!\nThanks for playing!')
            exit()
