from sys import exit
from random import randint

print('''Dice Roller, by Al Sweigart al@inventwithpython.com

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program''')

while True:
    try:
        dice_str = input('> ')
        if dice_str.upper() == 'QUIT':
            print('Thanks for playing!')
            exit()

        dice_str = dice_str.lower().replace(' ', '')
        d_index = dice_str.find('d')
        if d_index == -1:
            raise Exception('Missing the "d" character.')

        number_of_dice = dice_str[:d_index]
        if not number_of_dice.isdecimal():
            raise Exception('Missing the number of dice.')
        number_of_dice = int(number_of_dice)

        mod_index = dice_str.find('+')
        if mod_index == -1:
            mod_index = dice_str.find('-')

        if mod_index == -1:
            number_of_sides = dice_str[d_index + 1 :]
        else:
            number_of_sides = dice_str[d_index + 1 : mod_index]
        if not number_of_sides.isdecimal():
            raise Exception('Missing the number of sides.')
        number_of_sides = int(number_of_sides)

        if mod_index == -1:
            mod_amount = 0
        else:
            mod_amount = int(dice_str[mod_index + 1 :])
            if dice_str[mod_index] == '-':
                mod_amount = -mod_amount

        rolls = []
        for i in range(number_of_dice):
            roll_result = randint(1, number_of_sides)
            rolls.append(roll_result)

        print('Total:', sum(rolls) + mod_amount, '(Each die:', end='')
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        if mod_amount != 0:
            mod_sign = dice_str[mod_index]
            print(f', {mod_sign}{abs(mod_amount)}', end='')
        print(')')

    except Exception as exc:
        print('Invalid input. Enter something like "3d6" or "2d10+5".')
        print(f'Input was invalid because: {str(exc)}')
        continue
