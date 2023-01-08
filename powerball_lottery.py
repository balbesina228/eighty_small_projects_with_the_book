from random import shuffle, randint

print('''
Powerball Lottery, by Al Sweigart al@inventwithpython.com
Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.
This simulation gives you the thrill of playing without wasting money.
''')

while True:
    print('Enter 5 different numbers from 1 to 69 with spaces between')
    print('each number. For example: "5 17 23 42 50"')
    response = input('> ')
    numbers = response.split()
    if len(numbers) != 5:
        print('Enter 5 numbers')
        continue
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Enter numbers')
        continue
    for i in range(5):
        if not(1 <= numbers[i] <= 69):
            print('Enter numbers from 1 to 69')
            continue
    if len(set(numbers)) != 5:
        print('Enter different numbers')
        continue
    break

while True:
    print('Enter the powerball from 1 to 26')
    powerball = input('> ')
    if 1 <= int(powerball) <= 26 and powerball.isdigit():
        powerball = int(powerball)
        break
    print('Wrong format')
    continue

while True:
    print('How many times do you want to play? (Max: 1 000 000)')
    num_plays = input('> ')
    if 1 <= int(num_plays) <= 1_000_000 and num_plays.isdigit():
        num_plays = int(num_plays)
        break
    print('Wrong format')
    continue

price = '$' + str(2 * num_plays)
print(f"It costs {price} to play {num_plays} times, but don't worry,")
print("I'm sure, you will win it all back.")
input('Press enter to start...')
possible_numbers = list(range(1, 70))
for i in range(num_plays):
    shuffle(possible_numbers)
    winning_numbers = possible_numbers[0:5]
    winning_powerball = randint(1, 26)
    print('The winning numbers are: ', end='')
    all_winning_nums = ''
    for i in range(5):
        all_winning_nums += str(winning_numbers[i]) + ' '
    all_winning_nums += 'and ' + str(winning_powerball)
    print(all_winning_nums.ljust(21), end='')

    if (set(numbers) == set(winning_numbers)
        and powerball == winning_powerball):
        print('\nYou have won the Powerball lottery! Congratulations!')
        break
    else:
        print(' You lost')
print(f'You have wasted {price} money.')
print('Thanks for playing!')
